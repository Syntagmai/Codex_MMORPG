---
tags: [otclient, comunicacao, protocolo, rede, wikipedia, habdel]
type: wikipedia
status: active
priority: alta
created: 2025-08-05
updated: 2025-08-05
aliases: [Sistema Comunicação OTClient, Communication System OTClient, OTClient Communication System]
---

# 🌐 **Sistema de Comunicação - OTClient**

> [!info] **Baseado na pesquisa Habdel**
> Esta página é baseada na pesquisa detalhada da **OTCLIENT-010** realizada pelo sistema Habdel.

---

## 🎯 **Visão Geral**

O **Sistema de Comunicação** do OTClient é responsável por toda a comunicação com o servidor de jogo, incluindo protocolo de rede, mensagens, criptografia e gerenciamento de conexão. Este sistema garante a comunicação segura e eficiente entre o cliente e o servidor.

### **Características Principais**
- **Protocolo de Rede**: Implementação do protocolo Open Tibia
- **Criptografia**: Segurança na comunicação cliente-servidor
- **Gerenciamento de Conexão**: Estabelecimento e manutenção de conexões
- **Mensagens**: Envio e recebimento de mensagens do jogo
- **Performance Otimizada**: Comunicação eficiente e de baixa latência

---

## 🏗️ **Arquitetura do Sistema**

### **Estrutura Hierárquica**
```
Communication System (C++/Lua)
├── Protocol (Protocolo de Rede)
├── Network (Gerenciamento de Rede)
├── Messages (Mensagens)
├── Encryption (Criptografia)
└── Connection (Conexão)
```

### **Componentes Principais**

#### **1. Protocol (`src/framework/net/protocol.cpp`)**
```cpp
// Implementação do protocolo Open Tibia
class Protocol {
    // Handshake e autenticação
    // Envio e recebimento de mensagens
    // Gerenciamento de estado da conexão
    // Criptografia de dados
};
```

#### **2. Network (`src/framework/net/`)**
```cpp
// Gerenciamento de rede
class Network {
    // Estabelecimento de conexões
    // Gerenciamento de sockets
    // Timeouts e reconexão
    // Buffer de mensagens
};
```

---

## 🔧 **APIs e Interfaces**

### **Conexão com Servidor**
```lua
-- Conectar ao servidor
g_game.connect(host, port)

-- Desconectar do servidor
g_game.disconnect()

-- Verificar status da conexão
g_game.isConnected()
g_game.isConnecting()
g_game.isLogging()
```

### **Login e Autenticação**
```lua
-- Login no servidor
g_game.login(account, password, character)

-- Logout do servidor
g_game.logout()

-- Forçar logout
g_game.forceLogout()

-- Verificar estado do login
g_game.isOnline()
g_game.isLoggingOut()
```

### **Envio de Mensagens**
```lua
-- Enviar mensagem de chat
g_game.talk(message)
g_game.talkChannel(channelId, message)

-- Enviar mensagem privada
g_game.talkPrivate(channelId, message)

-- Enviar comando
g_game.talkChannel(0, "/command")
```

### **Ações do Jogo**
```lua
-- Movimento
g_game.walk(direction)
g_game.turn(direction)
g_game.stop()

-- Combate
g_game.attack(creature)
g_game.follow(creature)
g_game.cancelAttackAndFollow()

-- Itens
g_game.use(item, position)
g_game.useWith(item, target)
g_game.move(item, position, count)
g_game.drop(item, position, count)
```

---

## 📚 **Exemplos Práticos**

### **Exemplo 1: Sistema de Auto-Reconexão**
```lua
local autoReconnect = {}

autoReconnect.config = {
    enabled = true,
    maxAttempts = 5,
    delayBetweenAttempts = 5000, -- 5 segundos
    serverHost = "localhost",
    serverPort = 7172,
    account = "test",
    password = "test",
    character = "Test"
}

function autoReconnect.init()
    connect(g_game, {
        onGameEnd = autoReconnect.onGameEnd,
        onLoginError = autoReconnect.onLoginError
    })
    
    autoReconnect.attempts = 0
end

function autoReconnect.onGameEnd()
    if autoReconnect.config.enabled and autoReconnect.attempts < autoReconnect.config.maxAttempts then
        print("Conexão perdida. Tentando reconectar...")
        autoReconnect.attempts = autoReconnect.attempts + 1
        
        scheduleEvent(function()
            autoReconnect.tryReconnect()
        end, autoReconnect.config.delayBetweenAttempts)
    end
end

function autoReconnect.onLoginError(error)
    if autoReconnect.config.enabled and autoReconnect.attempts < autoReconnect.config.maxAttempts then
        print("Erro de login:", error, ". Tentando novamente...")
        autoReconnect.attempts = autoReconnect.attempts + 1
        
        scheduleEvent(function()
            autoReconnect.tryReconnect()
        end, autoReconnect.config.delayBetweenAttempts)
    end
end

function autoReconnect.tryReconnect()
    print("Tentativa de reconexão", autoReconnect.attempts, "/", autoReconnect.config.maxAttempts)
    
    g_game.connect(autoReconnect.config.serverHost, autoReconnect.config.serverPort)
    
    scheduleEvent(function()
        if g_game.isConnected() then
            g_game.login(autoReconnect.config.account, autoReconnect.config.password, autoReconnect.config.character)
        end
    end, 1000)
end

function autoReconnect.onGameStart()
    autoReconnect.attempts = 0
    print("Reconectado com sucesso!")
end

function autoReconnect.terminate()
    disconnect(g_game, {
        onGameEnd = autoReconnect.onGameEnd,
        onLoginError = autoReconnect.onLoginError
    })
end

return autoReconnect
```

### **Exemplo 2: Sistema de Ping**
```lua
local pingSystem = {}

pingSystem.config = {
    enabled = true,
    interval = 30000, -- 30 segundos
    timeout = 5000    -- 5 segundos
}

function pingSystem.init()
    connect(g_game, {
        onGameStart = pingSystem.onGameStart,
        onGameEnd = pingSystem.onGameEnd,
        onPing = pingSystem.onPing,
        onPingBack = pingSystem.onPingBack
    })
    
    pingSystem.lastPing = 0
    pingSystem.pingStartTime = 0
end

function pingSystem.onGameStart()
    if pingSystem.config.enabled then
        pingSystem.startPingTimer()
    end
end

function pingSystem.onGameEnd()
    if pingSystem.pingTimer then
        pingSystem.pingTimer:cancel()
    end
end

function pingSystem.startPingTimer()
    pingSystem.pingTimer = scheduleEvent(function()
        if g_game.isOnline() then
            pingSystem.sendPing()
        end
        pingSystem.startPingTimer()
    end, pingSystem.config.interval)
end

function pingSystem.sendPing()
    pingSystem.pingStartTime = g_clock.millis()
    g_game.ping()
end

function pingSystem.onPing()
    -- Servidor enviou ping
    g_game.pingBack()
end

function pingSystem.onPingBack()
    -- Servidor respondeu ao ping
    local pingTime = g_clock.millis() - pingSystem.pingStartTime
    pingSystem.lastPing = pingTime
    print("Ping:", pingTime, "ms")
end

function pingSystem.getLastPing()
    return pingSystem.lastPing
end

function pingSystem.terminate()
    if pingSystem.pingTimer then
        pingSystem.pingTimer:cancel()
    end
    
    disconnect(g_game, {
        onGameStart = pingSystem.onGameStart,
        onGameEnd = pingSystem.onGameEnd,
        onPing = pingSystem.onPing,
        onPingBack = pingSystem.onPingBack
    })
end

return pingSystem
```

---

## 🔗 **Dependências e Integração**

### **Dependências Internas**
- **Protocol**: Implementação do protocolo Open Tibia
- **Network**: Gerenciamento de rede
- **Messages**: Sistema de mensagens
- **Encryption**: Criptografia de dados

### **Integração com Outros Sistemas**
- **Sistema de Jogo**: Ações e eventos do jogo
- **Sistema de Eventos**: Comunicação de eventos
- **Sistema de Módulos**: APIs para módulos
- **Sistema de UI**: Interface de conexão

---

## 🚀 **Melhores Práticas**

### **1. Gerenciamento de Conexão**
```lua
-- Sempre verificar estado antes de enviar
if g_game.isOnline() then
    g_game.talk("Mensagem")
else
    print("Não conectado ao servidor")
end
```

### **2. Tratamento de Erros**
```lua
-- Conectar a eventos de erro
connect(g_game, {
    onLoginError = function(error)
        print("Erro de login:", error)
    end
})
```

---

## 📖 **Referência Completa**

### **APIs de Conexão**
- `g_game.connect(host, port)`
- `g_game.disconnect()`
- `g_game.isConnected()`
- `g_game.isConnecting()`

### **APIs de Login**
- `g_game.login(account, password, character)`
- `g_game.logout()`
- `g_game.forceLogout()`
- `g_game.isOnline()`

### **APIs de Comunicação**
- `g_game.talk(message)`
- `g_game.talkChannel(channelId, message)`
- `g_game.talkPrivate(channelId, message)`
- `g_game.ping()`
- `g_game.pingBack()`

---

## 🎯 **Conclusão**

O **Sistema de Comunicação** do OTClient fornece uma base sólida para comunicação segura e eficiente com o servidor. Com seu protocolo robusto e APIs completas, garante uma experiência de jogo estável e responsiva.

---

## 🔗 **Links Relacionados**

- [[otclient_arquitetura_core|Arquitetura Core do OTClient]]
- [[otclient_sistema_rede|Sistema de Rede]]
- [[otclient_sistema_eventos|Sistema de Eventos]]
- [[otclient_modulos_lua|Módulos Lua]]

---

*Baseado na pesquisa Habdel: OTCLIENT-010 - Sistema de Comunicação* 