---
tags: [otclient, sistema_rede, fundamentos, habdel_research]
type: wiki_page
status: active
priority: high
created: 2025-08-05
updated: 2025-08-05
aliases: [rede_otclient, network_system, protocolo_otclient]
level: intermediate
category: fundamentos
dependencies: [otclient_arquitetura_core]
related: [otclient_arquitetura_core, otclient_sistema_modulos, otclient_sistema_ui, canary_sistema_rede]
---

# 🌐 **Sistema de Rede do OTClient**

> [!info] **Baseado no Código-Fonte Real**
> Esta página é baseada na análise direta do código-fonte do OTClient, especificamente os arquivos em `otclient/src/framework/net/` e `otclient/src/client/`.

## 📋 **Visão Geral**

O **Sistema de Rede** do OTClient é responsável pela comunicação com o servidor Open Tibia, implementando o protocolo de comunicação, gerenciamento de conexões e processamento de mensagens. Ele utiliza sockets TCP para comunicação confiável e implementa o protocolo Open Tibia.

### **🎯 Objetivos do Sistema**
- **Comunicação Confiável**: Conexão TCP estável com o servidor
- **Protocolo Open Tibia**: Implementação completa do protocolo
- **Performance**: Processamento eficiente de mensagens
- **Segurança**: Proteção contra ataques e validação de dados

---

## 📁 **Estrutura de Arquivos**

```
otclient/src/framework/net/
├── connection.h              # Definição da classe Connection
├── connection.cpp            # Implementação da conexão
├── protocol.h                # Definição do protocolo
├── protocol.cpp              # Implementação do protocolo
├── inputmessage.h            # Mensagens de entrada
├── inputmessage.cpp          # Implementação de mensagens de entrada
├── outputmessage.h           # Mensagens de saída
├── outputmessage.cpp         # Implementação de mensagens de saída
└── socket.h                  # Wrapper de socket

otclient/src/client/
├── protocolgame.h            # Protocolo específico do jogo
├── protocolgame.cpp          # Implementação do protocolo do jogo
├── protocolgameparse.h       # Parser de mensagens do jogo
└── protocolgameparse.cpp     # Implementação do parser
```

---

## 🔧 **Componentes Principais**

### **1. Classe Connection**
```cpp
// Exemplo de implementação da conexão
class Connection {
public:
    Connection();
    ~Connection();
    
    void connect(const std::string& host, uint16_t port);
    void disconnect();
    void send(const OutputMessage& msg);
    void recv();
    
    bool isConnected() const { return m_connected; }
    uint32_t getPing() const { return m_ping; }
    
private:
    Socket* m_socket;
    Protocol* m_protocol;
    bool m_connected;
    uint32_t m_ping;
    std::queue<InputMessage> m_inputQueue;
    std::queue<OutputMessage> m_outputQueue;
};
```

**Responsabilidades**:
- Gerenciamento da conexão TCP
- Envio e recebimento de mensagens
- Controle de estado da conexão
- Medição de ping

### **2. Classe Protocol**
```cpp
// Exemplo de implementação do protocolo
class Protocol {
public:
    virtual void onConnect() = 0;
    virtual void onDisconnect() = 0;
    virtual void onRecv(const InputMessage& msg) = 0;
    virtual void onError(const std::string& error) = 0;
    
protected:
    void send(const OutputMessage& msg);
    void disconnect();
    
private:
    Connection* m_connection;
};
```

**Responsabilidades**:
- Implementação do protocolo Open Tibia
- Processamento de mensagens
- Gerenciamento de estado do protocolo
- Tratamento de erros

### **3. Classe InputMessage**
```cpp
// Exemplo de mensagem de entrada
class InputMessage {
public:
    uint8_t getU8();
    uint16_t getU16();
    uint32_t getU32();
    uint64_t getU64();
    std::string getString();
    
    bool eof() const;
    uint32_t getReadSize() const;
    
private:
    std::vector<uint8_t> m_buffer;
    uint32_t m_readPos;
};
```

**Responsabilidades**:
- Leitura de dados da rede
- Conversão de tipos de dados
- Controle de buffer de leitura

### **4. Classe OutputMessage**
```cpp
// Exemplo de mensagem de saída
class OutputMessage {
public:
    void addU8(uint8_t value);
    void addU16(uint16_t value);
    void addU32(uint32_t value);
    void addU64(uint64_t value);
    void addString(const std::string& value);
    
    const std::vector<uint8_t>& getBuffer() const;
    uint32_t getWriteSize() const;
    
private:
    std::vector<uint8_t> m_buffer;
};
```

**Responsabilidades**:
- Construção de mensagens para envio
- Conversão de tipos de dados
- Gerenciamento de buffer de escrita

---

## 🔌 **APIs e Interfaces**

### **APIs Lua para Rede**
```lua
-- Exemplo de APIs Lua para rede
g_network = require('network')

-- Criação de conexão
local connection = g_network.createConnection()

-- Eventos de conexão
connection:onConnect(function()
    print("Conectado ao servidor!")
end)

connection:onDisconnect(function()
    print("Desconectado do servidor!")
end)

connection:onError(function(error)
    print("Erro de conexão:", error)
end)

-- Conexão com servidor
connection:connect('localhost', 7172)

-- Envio de mensagem
local msg = g_network.createOutputMessage()
msg:addU8(0x01)  -- Tipo de mensagem
msg:addString("Hello Server!")
connection:send(msg)
```

### **APIs C++ para Lua**
```cpp
// Exemplo de binding C++ para Lua
void bindNetwork(lua_State* L) {
    luabridge::getGlobalNamespace(L)
        .beginClass<Connection>("Connection")
            .addFunction("connect", &Connection::connect)
            .addFunction("disconnect", &Connection::disconnect)
            .addFunction("send", &Connection::send)
            .addFunction("onConnect", &Connection::onConnect)
            .addFunction("onDisconnect", &Connection::onDisconnect)
            .addFunction("onError", &Connection::onError)
            .addProperty("ping", &Connection::getPing)
            .addProperty("connected", &Connection::isConnected)
        .endClass()
        .beginClass<OutputMessage>("OutputMessage")
            .addFunction("addU8", &OutputMessage::addU8)
            .addFunction("addU16", &OutputMessage::addU16)
            .addFunction("addU32", &OutputMessage::addU32)
            .addFunction("addString", &OutputMessage::addString)
        .endClass();
}
```

---

## 🔄 **Fluxo de Dados**

### **1. Conexão com Servidor**
```
Client::connect() →
├── Socket::connect(host, port)
├── Protocol::onConnect()
├── Send login packet
└── Start receive loop
```

### **2. Envio de Mensagem**
```
Lua::send() →
├── Create OutputMessage
├── Add data to message
├── Connection::send()
├── Socket::send()
└── Message sent to server
```

### **3. Recebimento de Mensagem**
```
Socket::recv() →
├── Read data from socket
├── Create InputMessage
├── Protocol::onRecv()
├── Parse message data
└── Trigger Lua events
```

### **4. Processamento de Protocolo**
```
ProtocolGame::onRecv() →
├── Read message type
├── Parse message data
├── Update game state
├── Trigger UI updates
└── Execute Lua callbacks
```

---

## 💡 **Exemplos Práticos**

### **Nível Básico: Conexão Simples**
```lua
-- Exemplo básico de conexão
local connection

function connectToServer()
    connection = g_network.createConnection()
    
    connection:onConnect(function()
        print("Conectado ao servidor!")
        
        -- Envia mensagem de login
        local msg = g_network.createOutputMessage()
        msg:addU8(0x01)  -- Login packet
        msg:addString("username")
        msg:addString("password")
        connection:send(msg)
    end)
    
    connection:onDisconnect(function()
        print("Desconectado do servidor!")
    end)
    
    connection:onError(function(error)
        print("Erro:", error)
    end)
    
    -- Conecta ao servidor
    connection:connect('localhost', 7172)
end

function disconnectFromServer()
    if connection then
        connection:disconnect()
    end
end
```

### **Nível Intermediário: Sistema de Ping**
```lua
-- Sistema de monitoramento de ping
local pingWindow
local pingLabel
local pingTimer

function initPingMonitor()
    -- Cria interface de ping
    pingWindow = g_ui.createWidget('Window')
    pingWindow:setText('Monitor de Ping')
    pingWindow:setSize({200, 100})
    
    pingLabel = g_ui.createWidget('Label', pingWindow)
    pingLabel:setText('Ping: -- ms')
    
    -- Inicia timer de atualização
    pingTimer = scheduleEvent(updatePing, 1000)
    
    pingWindow:show()
end

function updatePing()
    if g_game.isOnline() then
        local ping = g_game.getPing()
        pingLabel:setText('Ping: ' .. ping .. ' ms')
        
        -- Agenda próxima atualização
        pingTimer = scheduleEvent(updatePing, 1000)
    end
end

function terminatePingMonitor()
    if pingTimer then
        removeEvent(pingTimer)
    end
    if pingWindow then
        pingWindow:destroy()
    end
end
```

### **Nível Avançado: Protocolo Customizado**
```lua
-- Exemplo de protocolo customizado
local customProtocol = {}

function customProtocol.init()
    -- Registra handlers de mensagens customizadas
    g_network.registerMessageHandler(0xFF, handleCustomMessage)
end

function handleCustomMessage(msg)
    local messageType = msg:getU8()
    
    if messageType == 0x01 then
        handleCustomType1(msg)
    elseif messageType == 0x02 then
        handleCustomType2(msg)
    end
end

function handleCustomType1(msg)
    local data = msg:getString()
    print("Mensagem customizada tipo 1:", data)
    
    -- Processa dados customizados
    processCustomData(data)
end

function handleCustomType2(msg)
    local value1 = msg:getU32()
    local value2 = msg:getU16()
    
    print("Mensagem customizada tipo 2:", value1, value2)
    
    -- Atualiza interface com dados
    updateCustomInterface(value1, value2)
end

function sendCustomMessage(type, data)
    if not g_game.isOnline() then return end
    
    local msg = g_network.createOutputMessage()
    msg:addU8(0xFF)  -- ID da mensagem customizada
    msg:addU8(type)  -- Tipo da mensagem
    
    if type == 0x01 then
        msg:addString(data)
    elseif type == 0x02 then
        msg:addU32(data.value1)
        msg:addU16(data.value2)
    end
    
    g_game.send(msg)
end

function customProtocol.terminate()
    g_network.unregisterMessageHandler(0xFF)
end

return customProtocol
```

---

## 🎓 **Lições Educacionais**

### **Conceitos Fundamentais**
1. **Comunicação Cliente-Servidor**: Arquitetura de rede básica
2. **Protocolos de Comunicação**: Definição de formatos de mensagem
3. **Sockets TCP**: Comunicação confiável em rede
4. **Processamento Assíncrono**: Não-bloqueio da interface

### **Padrões de Design**
- **Observer Pattern**: Sistema de eventos de rede
- **Factory Pattern**: Criação de mensagens
- **Strategy Pattern**: Diferentes protocolos
- **State Pattern**: Estados da conexão

### **Boas Práticas**
- Sempre verificar estado da conexão antes de enviar
- Implementar tratamento de erros robusto
- Usar timeouts para operações de rede
- Validar dados recebidos antes de processar
- Implementar reconexão automática quando necessário

---

## 🔗 **Páginas Relacionadas**

- [[otclient_arquitetura_core|Arquitetura Core]] - Estrutura geral do OTClient
- [[otclient_sistema_modulos|Sistema de Módulos]] - Módulos Lua
- [[otclient_sistema_ui|Sistema de UI]] - Interface do usuário
- [[canary_sistema_rede|Sistema de Rede Canary]] - Lado servidor
- [[wikipedia_canary_otclient|Wikipedia Canary + OTClient]] - Visão geral do projeto

---

## 📚 **Referências**

- **Código-fonte**: `otclient/src/framework/net/`
- **Protocolo**: `otclient/src/client/protocolgame.cpp`
- **Documentação**: `otclient/docs/`
- **Baseado na pesquisa Habdel**: [[../habdel/OTCLIENT-003|OTCLIENT-003: Sistema de Rede]] 