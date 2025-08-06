---
tags: [otclient, eventos, sistema, wikipedia, habdel]
type: wikipedia
status: active
priority: alta
created: 2025-08-05
updated: 2025-08-05
aliases: [Sistema Eventos OTClient, Event System OTClient, OTClient Event System]
---

# ⚡ **Sistema de Eventos - OTClient**

> [!info] **Baseado na pesquisa Habdel**
> Esta página é baseada na pesquisa detalhada da **OTCLIENT-009** realizada pelo sistema Habdel.

---

## 🎯 **Visão Geral**

O **Sistema de Eventos** do OTClient é responsável por gerenciar toda a comunicação assíncrona entre componentes, módulos e sistemas. Baseado em um sistema de eventos e callbacks, permite que diferentes partes do cliente se comuniquem de forma desacoplada e eficiente.

### **Características Principais**
- **Eventos Assíncronos**: Comunicação não-bloqueante entre componentes
- **Sistema de Callbacks**: Funções executadas quando eventos ocorrem
- **Desacoplamento**: Componentes independentes se comunicam via eventos
- **Performance Otimizada**: Sistema eficiente de despacho de eventos
- **Debugging Avançado**: Ferramentas para rastreamento de eventos

---

## 🏗️ **Arquitetura do Sistema**

### **Estrutura Hierárquica**
```
Event System (C++/Lua)
├── EventDispatcher (Despachador Central)
├── Event (Definição de Eventos)
├── EventListener (Ouvintes de Eventos)
├── EventManager (Gerenciamento)
└── EventQueue (Fila de Eventos)
```

### **Componentes Principais**

#### **1. EventDispatcher (`src/framework/core/eventdispatcher.cpp`)**
```cpp
// Despachador central de eventos
class EventDispatcher {
    // Registro de listeners
    // Despacho de eventos
    // Gerenciamento de filas
    // Priorização de eventos
};
```

#### **2. Sistema de Eventos Lua**
```lua
-- APIs para gerenciamento de eventos
connect(object, events)
disconnect(object, events)
signalcall(event, ...)
```

---

## 🔧 **APIs e Interfaces**

### **Conexão de Eventos**
```lua
-- Conectar a eventos
connect(g_game, { 
    onGameStart = function()
        print("Jogo iniciado!")
    end,
    onGameEnd = function()
        print("Jogo finalizado!")
    end
})

-- Conectar com função específica
connect(g_game, { onGameStart = minhaFuncao })

-- Desconectar eventos
disconnect(g_game, { onGameStart = nil })
```

### **Emissão de Eventos**
```lua
-- Emitir evento customizado
signalcall('onCustomEvent', data1, data2)

-- Emitir evento com objeto específico
object:signal('onMyEvent', param1, param2)
```

### **Eventos do Jogo**
```lua
-- Eventos principais do jogo
connect(g_game, {
    onGameStart = function() end,
    onGameEnd = function() end,
    onLoginAdvice = function(message) end,
    onLoginError = function(error) end,
    onLoginToken = function(unknown) end,
    onPing = function() end,
    onPingBack = function() end,
    onChallenge = function(timestamp, random) end,
    onDeath = function(deathType, penality) end,
    onWalk = function(creature, oldPos, newPos) end,
    onWalkCancel = function(creature) end,
    onWalkFinish = function(creature) end,
    onCreatureMove = function(creature, oldPos, newPos) end,
    onCreatureChangeOutfit = function(creature, outfit) end,
    onCreatureChangeMount = function(creature, mountId) end,
    onCreatureChangeDirection = function(creature, direction) end,
    onCreatureChangeSkull = function(creature, skull) end,
    onCreatureChangeShield = function(creature, shield) end,
    onCreatureChangeEmblem = function(creature, emblem) end,
    onCreatureChangeIcon = function(creature, icon) end,
    onCreatureChangeHealth = function(creature, healthPercent) end,
    onCreatureChangeMana = function(creature, manaPercent) end,
    onCreatureChangeSpeed = function(creature, baseSpeed, speed) end,
    onCreatureChangeOutfit = function(creature, outfit) end,
    onCreatureChangeLight = function(creature, light) end,
    onCreatureChangeCreatureType = function(creature, type) end,
    onCreatureStartCast = function(creature) end,
    onCreatureStopCast = function(creature) end,
    onCreatureAttachEffect = function(creature, effect) end,
    onCreatureDetachEffect = function(creature, effect) end,
    onCreatureUpdate = function(creature) end,
    onCreaturePositionChange = function(creature, oldPos, newPos) end,
    onCreatureAppear = function(creature) end,
    onCreatureDisappear = function(creature) end,
    onCreatureSay = function(creature, type, message, time) end,
    onCreatureChangeVisible = function(creature, visible) end,
    onCreatureChangeIcons = function(creature, icons) end,
    onCreatureChangeState = function(creature, state) end,
    onCreatureChangeUnpassable = function(creature, unpassable) end,
    onCreatureChangeHide = function(creature, hide) end,
    onCreatureChangeSkull = function(creature, skull) end,
    onCreatureChangeShield = function(creature, shield) end,
    onCreatureChangeEmblem = function(creature, emblem) end,
    onCreatureChangeIcon = function(creature, icon) end,
    onCreatureChangeHealth = function(creature, healthPercent) end,
    onCreatureChangeMana = function(creature, manaPercent) end,
    onCreatureChangeSpeed = function(creature, baseSpeed, speed) end,
    onCreatureChangeOutfit = function(creature, outfit) end,
    onCreatureChangeLight = function(creature, light) end,
    onCreatureChangeCreatureType = function(creature, type) end,
    onCreatureStartCast = function(creature) end,
    onCreatureStopCast = function(creature) end,
    onCreatureAttachEffect = function(creature, effect) end,
    onCreatureDetachEffect = function(creature, effect) end,
    onCreatureUpdate = function(creature) end,
    onCreaturePositionChange = function(creature, oldPos, newPos) end,
    onCreatureAppear = function(creature) end,
    onCreatureDisappear = function(creature) end,
    onCreatureSay = function(creature, type, message, time) end,
    onCreatureChangeVisible = function(creature, visible) end,
    onCreatureChangeIcons = function(creature, icons) end,
    onCreatureChangeState = function(creature, state) end,
    onCreatureChangeUnpassable = function(creature, unpassable) end,
    onCreatureChangeHide = function(creature, hide) end
})
```

---

## 📚 **Exemplos Práticos**

### **Exemplo 1: Sistema de Notificações**
```lua
local notificationSystem = {}

function notificationSystem.init()
    -- Conectar a eventos importantes
    connect(g_game, {
        onGameStart = notificationSystem.onGameStart,
        onGameEnd = notificationSystem.onGameEnd,
        onDeath = notificationSystem.onDeath
    })
    
    connect(g_game, {
        onCreatureAppear = notificationSystem.onCreatureAppear,
        onCreatureDisappear = notificationSystem.onCreatureDisappear
    })
end

function notificationSystem.onGameStart()
    notificationSystem.showNotification("Jogo iniciado!", "success")
end

function notificationSystem.onGameEnd()
    notificationSystem.showNotification("Jogo finalizado!", "warning")
end

function notificationSystem.onDeath(deathType, penality)
    notificationSystem.showNotification("Você morreu!", "error")
end

function notificationSystem.onCreatureAppear(creature)
    if creature:isPlayer() then
        notificationSystem.showNotification("Jogador apareceu: " .. creature:getName(), "info")
    end
end

function notificationSystem.onCreatureDisappear(creature)
    if creature:isPlayer() then
        notificationSystem.showNotification("Jogador desapareceu: " .. creature:getName(), "info")
    end
end

function notificationSystem.showNotification(message, type)
    -- Implementar sistema de notificação visual
    print("[" .. type:upper() .. "] " .. message)
end

function notificationSystem.terminate()
    disconnect(g_game, {
        onGameStart = notificationSystem.onGameStart,
        onGameEnd = notificationSystem.onGameEnd,
        onDeath = notificationSystem.onDeath,
        onCreatureAppear = notificationSystem.onCreatureAppear,
        onCreatureDisappear = notificationSystem.onCreatureDisappear
    })
end

return notificationSystem
```

### **Exemplo 2: Sistema de Logs**
```lua
local logSystem = {}

function logSystem.init()
    -- Conectar a eventos para logging
    connect(g_game, {
        onWalk = logSystem.onWalk,
        onCreatureMove = logSystem.onCreatureMove,
        onCreatureSay = logSystem.onCreatureSay
    })
end

function logSystem.onWalk(creature, oldPos, newPos)
    if creature:isLocalPlayer() then
        logSystem.log("Player moved from " .. oldPos.x .. "," .. oldPos.y .. " to " .. newPos.x .. "," .. newPos.y)
    end
end

function logSystem.onCreatureMove(creature, oldPos, newPos)
    logSystem.log("Creature " .. creature:getName() .. " moved from " .. oldPos.x .. "," .. oldPos.y .. " to " .. newPos.x .. "," .. newPos.y)
end

function logSystem.onCreatureSay(creature, type, message, time)
    logSystem.log("Creature " .. creature:getName() .. " said: " .. message)
end

function logSystem.log(message)
    local timestamp = os.date("%Y-%m-%d %H:%M:%S")
    print("[" .. timestamp .. "] " .. message)
end

function logSystem.terminate()
    disconnect(g_game, {
        onWalk = logSystem.onWalk,
        onCreatureMove = logSystem.onCreatureMove,
        onCreatureSay = logSystem.onCreatureSay
    })
end

return logSystem
```

---

## 🔗 **Dependências e Integração**

### **Dependências Internas**
- **EventDispatcher**: Despachador central de eventos
- **EventManager**: Gerenciamento de eventos
- **EventQueue**: Fila de eventos
- **LuaEngine**: Interface Lua/C++

### **Integração com Outros Sistemas**
- **Sistema de UI**: Eventos de interface
- **Sistema de Jogo**: Eventos de gameplay
- **Sistema de Rede**: Eventos de comunicação
- **Sistema de Módulos**: Comunicação entre módulos

---

## 🚀 **Melhores Práticas**

### **1. Gerenciamento de Conexões**
```lua
-- Sempre mantenha referência das conexões
local connections = {}

function init()
    connections.gameStart = connect(g_game, { onGameStart = onGameStart })
    connections.gameEnd = connect(g_game, { onGameEnd = onGameEnd })
end

function terminate()
    for _, connection in pairs(connections) do
        disconnect(connection)
    end
end
```

### **2. Eventos Customizados**
```lua
-- Emitir eventos customizados
signalcall('onMyCustomEvent', data1, data2)

-- Escutar eventos customizados
connect(g_game, { onMyCustomEvent = function(data1, data2)
    print("Evento customizado:", data1, data2)
end })
```

---

## 📖 **Referência Completa**

### **APIs Principais**
- `connect(object, events)`
- `disconnect(object, events)`
- `signalcall(event, ...)`
- `object:signal(event, ...)`

### **Eventos Principais**
- Eventos de Jogo: `onGameStart`, `onGameEnd`, `onLoginAdvice`, etc.
- Eventos de Criaturas: `onCreatureAppear`, `onCreatureDisappear`, `onCreatureMove`, etc.
- Eventos de Interface: `onClick`, `onTextChange`, `onFocusChange`, etc.

---

## 🎯 **Conclusão**

O **Sistema de Eventos** do OTClient fornece uma base sólida para comunicação assíncrona entre componentes. Com seu sistema de eventos e callbacks, permite que diferentes partes do cliente se comuniquem de forma eficiente e desacoplada.

---

## 🔗 **Links Relacionados**

- [[otclient_arquitetura_core|Arquitetura Core do OTClient]]
- [[otclient_sistema_lua|Sistema de Lua]]
- [[otclient_sistema_ui|Sistema de UI]]
- [[otclient_modulos_lua|Módulos Lua]]

---

*Baseado na pesquisa Habdel: OTCLIENT-009 - Sistema de Eventos* 