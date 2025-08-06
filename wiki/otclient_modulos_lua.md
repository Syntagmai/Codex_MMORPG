---
tags: [otclient, lua, modulos, gamelib, wikipedia, habdel]
type: wikipedia
status: active
priority: alta
created: 2025-08-05
updated: 2025-08-05
aliases: [Módulos Lua OTClient, Lua Modules OTClient, OTClient Lua Modules]
---

# 📦 **Módulos Lua - OTClient**

> [!info] **Baseado na pesquisa Habdel**
> Esta página é baseada na pesquisa detalhada da **OTCLIENT-008** realizada pelo sistema Habdel.

---

## 🎯 **Visão Geral**

O **Sistema de Módulos Lua** do OTClient é responsável por organizar e gerenciar toda a lógica de jogo e funcionalidades específicas através de módulos modulares e reutilizáveis. Estes módulos fornecem APIs de alto nível para interação com o jogo, gerenciamento de dados e criação de funcionalidades personalizadas.

### **Características Principais**
- **Modularidade**: Sistema de módulos independentes e reutilizáveis
- **APIs de Alto Nível**: Interfaces simplificadas para funcionalidades complexas
- **Gerenciamento de Estado**: Controle centralizado do estado do jogo
- **Eventos e Callbacks**: Sistema de eventos para comunicação entre módulos
- **Bibliotecas Especializadas**: gamelib, corelib e módulos específicos
- **Carregamento Dinâmico**: Módulos carregados sob demanda

---

## 🏗️ **Arquitetura do Sistema**

### **Estrutura Hierárquica**
```
Modules System (Lua)
├── gamelib/ (Biblioteca de Jogo)
│   ├── game.lua (Lógica Principal)
│   ├── player.lua (Gerenciamento de Jogador)
│   ├── creature.lua (Criaturas e NPCs)
│   ├── items.lua (Sistema de Itens)
│   ├── spells.lua (Sistema de Magias)
│   ├── protocol.lua (Comunicação)
│   └── const.lua (Constantes)
├── corelib/ (Biblioteca Core)
│   ├── util.lua (Utilitários)
│   ├── network.lua (Rede)
│   └── ui.lua (Interface)
└── game_*/ (Módulos Específicos)
    ├── game_inventory/ (Inventário)
    ├── game_skills/ (Habilidades)
    ├── game_questlog/ (Quests)
    └── game_* (Outros módulos)
```

### **Componentes Principais**

#### **1. gamelib (`modules/gamelib/`)**
```lua
-- Biblioteca principal de jogo
-- Fornece APIs de alto nível para funcionalidades do jogo
local gamelib = {
    game = require('gamelib.game'),
    player = require('gamelib.player'),
    creature = require('gamelib.creature'),
    items = require('gamelib.items'),
    spells = require('gamelib.spells'),
    protocol = require('gamelib.protocol'),
    const = require('gamelib.const')
}
```

#### **2. Sistema de Módulos**
```lua
-- Estrutura de um módulo OTClient
-- modules/meu_modulo/meu_modulo.otmod
{
    name = "meu_modulo",
    description = "Descrição do módulo",
    author = "Autor",
    autoload = true,
    autoloadPriority = 1000,
    script = "meu_modulo.lua",
    dependencies = { "gamelib" }
}
```

#### **3. Gerenciamento de Módulos**
```lua
-- APIs para gerenciamento de módulos
g_modules.loadModule("nome_modulo")
g_modules.unloadModule("nome_modulo")
g_modules.isModuleLoaded("nome_modulo")
g_modules.reloadModule("nome_modulo")
```

---

## 🔧 **APIs e Interfaces**

### **Biblioteca de Jogo (gamelib)**

#### **Game (`gamelib.game.lua`)**
```lua
-- APIs principais do jogo
g_game.login(account, password, character)
g_game.logout()
g_game.forceLogout()

-- Estado do jogo
g_game.isOnline()
g_game.isConnecting()
g_game.isLogging()
g_game.isLoggingOut()

-- Informações do servidor
g_game.getServerProtocol()
g_game.getServerVersion()
g_game.getServerTime()
```

#### **Player (`gamelib.player.lua`)**
```lua
-- Gerenciamento do jogador
local player = g_game.getLocalPlayer()

-- Propriedades do jogador
player:getName()
player:getLevel()
player:getExperience()
player:getHealthPercent()
player:getManaPercent()
player:getCap()
player:getStamina()

-- Ações do jogador
player:walk(direction)
player:turn(direction)
player:stop()
player:autoWalk(path)
```

#### **Creature (`gamelib.creature.lua`)**
```lua
-- Gerenciamento de criaturas
local creature = g_map.getCreatureById(id)

-- Propriedades da criatura
creature:getName()
creature:getHealthPercent()
creature:getDirection()
creature:getPosition()
creature:getOutfit()
creature:isNpc()
creature:isMonster()
creature:isPlayer()

-- Ações com criaturas
g_game.attack(creature)
g_game.follow(creature)
g_game.cancelAttackAndFollow()
```

#### **Items (`gamelib.items.lua`)**
```lua
-- Sistema de itens
local item = g_game.getLocalPlayer():getInventoryItem(slot)

-- Propriedades do item
item:getId()
item:getCount()
item:getPosition()
item:getName()
item:getDescription()

-- Ações com itens
g_game.use(item, position)
g_game.useWith(item, target)
g_game.move(item, position, count)
g_game.drop(item, position, count)
```

#### **Spells (`gamelib.spells.lua`)**
```lua
-- Sistema de magias
local spell = g_spells.getSpellByName("exura")

-- Propriedades da magia
spell:getName()
spell:getWords()
spell:getCooldown()
spell:getManaCost()
spell:getVocation()

-- Executar magia
g_game.talk(spell:getWords())
g_game.talkChannel(1, spell:getWords())
```

### **Biblioteca Core (corelib)**

#### **Util (`corelib.util.lua`)**
```lua
-- Funções utilitárias
table.find(t, value)
table.copy(t)
string.split(str, delimiter)
string.trim(str)
math.round(num)
```

#### **Network (`corelib.network.lua`)**
```lua
-- APIs de rede
g_network.connect(host, port)
g_network.disconnect()
g_network.isConnected()
g_network.send(data)
```

---

## 📚 **Exemplos Práticos**

### **Exemplo 1: Módulo de Auto-Healing**
```lua
-- modules/auto_healing/auto_healing.otmod
{
    name = "auto_healing",
    description = "Sistema de cura automática",
    author = "Seu Nome",
    autoload = true,
    autoloadPriority = 1000,
    script = "auto_healing.lua",
    dependencies = { "gamelib" }
}

-- modules/auto_healing/auto_healing.lua
local autoHealing = {}

-- Configurações
autoHealing.config = {
    enabled = true,
    healthThreshold = 70, -- Curar quando vida < 70%
    manaThreshold = 50,   -- Curar quando mana < 50%
    healthSpell = "exura",
    manaSpell = "utura"
}

function autoHealing.init()
    print("Auto Healing inicializado!")
    
    -- Conectar a eventos do jogo
    connect(g_game, { 
        onGameStart = autoHealing.onGameStart,
        onGameEnd = autoHealing.onGameEnd
    })
    
    -- Timer para verificação periódica
    autoHealing.checkTimer = scheduleEvent(autoHealing.checkHealth, 1000)
end

function autoHealing.onGameStart()
    print("Auto Healing ativo!")
    autoHealing.checkTimer = scheduleEvent(autoHealing.checkHealth, 1000)
end

function autoHealing.onGameEnd()
    print("Auto Healing desativado!")
    if autoHealing.checkTimer then
        autoHealing.checkTimer:cancel()
    end
end

function autoHealing.checkHealth()
    if not autoHealing.config.enabled or not g_game.isOnline() then
        return
    end
    
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    -- Verificar vida
    local healthPercent = player:getHealthPercent()
    if healthPercent < autoHealing.config.healthThreshold then
        local healthSpell = g_spells.getSpellByName(autoHealing.config.healthSpell)
        if healthSpell and healthSpell:getCooldown() == 0 then
            g_game.talk(healthSpell:getWords())
            print("Curando vida:", healthPercent .. "%")
        end
    end
    
    -- Verificar mana
    local manaPercent = player:getManaPercent()
    if manaPercent < autoHealing.config.manaThreshold then
        local manaSpell = g_spells.getSpellByName(autoHealing.config.manaSpell)
        if manaSpell and manaSpell:getCooldown() == 0 then
            g_game.talk(manaSpell:getWords())
            print("Curando mana:", manaPercent .. "%")
        end
    end
    
    -- Agendar próxima verificação
    autoHealing.checkTimer = scheduleEvent(autoHealing.checkHealth, 1000)
end

function autoHealing.terminate()
    if autoHealing.checkTimer then
        autoHealing.checkTimer:cancel()
    end
    
    disconnect(g_game, { 
        onGameStart = autoHealing.onGameStart,
        onGameEnd = autoHealing.onGameEnd
    })
    
    print("Auto Healing finalizado!")
end

return autoHealing
```

### **Exemplo 2: Módulo de Loot Tracker**
```lua
-- modules/loot_tracker/loot_tracker.otmod
{
    name = "loot_tracker",
    description = "Rastreador de loot",
    author = "Seu Nome",
    autoload = true,
    autoloadPriority = 1000,
    script = "loot_tracker.lua",
    dependencies = { "gamelib" }
}

-- modules/loot_tracker/loot_tracker.lua
local lootTracker = {}

-- Dados do tracker
lootTracker.data = {
    kills = 0,
    loot = {},
    startTime = 0
}

function lootTracker.init()
    print("Loot Tracker inicializado!")
    
    -- Conectar a eventos
    connect(g_game, { 
        onGameStart = lootTracker.onGameStart,
        onGameEnd = lootTracker.onGameEnd
    })
    
    connect(g_game, { 
        onCreatureDeath = lootTracker.onCreatureDeath 
    })
    
    connect(g_game, { 
        onInventoryChange = lootTracker.onInventoryChange 
    })
end

function lootTracker.onGameStart()
    lootTracker.data.startTime = g_clock.millis()
    lootTracker.data.kills = 0
    lootTracker.data.loot = {}
    print("Loot Tracker iniciado!")
end

function lootTracker.onGameEnd()
    lootTracker.printReport()
end

function lootTracker.onCreatureDeath(creature)
    if creature:isMonster() then
        lootTracker.data.kills = lootTracker.data.kills + 1
        print("Monstro morto:", creature:getName(), "Total:", lootTracker.data.kills)
    end
end

function lootTracker.onInventoryChange(item, oldCount, newCount)
    if newCount > oldCount then
        local itemName = item:getName()
        lootTracker.data.loot[itemName] = (lootTracker.data.loot[itemName] or 0) + (newCount - oldCount)
        print("Loot obtido:", itemName, "Quantidade:", newCount - oldCount)
    end
end

function lootTracker.printReport()
    local sessionTime = (g_clock.millis() - lootTracker.data.startTime) / 1000 / 60 -- minutos
    
    print("=== RELATÓRIO DE LOOT ===")
    print("Tempo de sessão:", math.round(sessionTime), "minutos")
    print("Monstros mortos:", lootTracker.data.kills)
    print("Kills por hora:", math.round(lootTracker.data.kills / sessionTime * 60))
    print("Loot obtido:")
    
    for itemName, count in pairs(lootTracker.data.loot) do
        print("  " .. itemName .. ": " .. count)
    end
end

function lootTracker.terminate()
    disconnect(g_game, { 
        onGameStart = lootTracker.onGameStart,
        onGameEnd = lootTracker.onGameEnd,
        onCreatureDeath = lootTracker.onCreatureDeath,
        onInventoryChange = lootTracker.onInventoryChange
    })
    
    print("Loot Tracker finalizado!")
end

return lootTracker
```

### **Exemplo 3: Módulo de Waypoints**
```lua
-- modules/waypoints/waypoints.otmod
{
    name = "waypoints",
    description = "Sistema de waypoints",
    author = "Seu Nome",
    autoload = true,
    autoloadPriority = 1000,
    script = "waypoints.lua",
    dependencies = { "gamelib" }
}

-- modules/waypoints/waypoints.lua
local waypoints = {}

-- Dados dos waypoints
waypoints.data = {
    points = {},
    currentPath = {},
    isWalking = false
}

function waypoints.init()
    print("Waypoints inicializado!")
    
    -- Carregar waypoints salvos
    waypoints.loadWaypoints()
    
    -- Conectar a eventos
    connect(g_game, { 
        onGameStart = waypoints.onGameStart,
        onGameEnd = waypoints.onGameEnd
    })
    
    connect(g_game, { 
        onWalkFinish = waypoints.onWalkFinish 
    })
end

function waypoints.onGameStart()
    print("Waypoints ativo!")
end

function waypoints.onGameEnd()
    waypoints.stopWalking()
end

function waypoints.onWalkFinish()
    if waypoints.data.isWalking and #waypoints.data.currentPath > 0 then
        table.remove(waypoints.data.currentPath, 1)
        if #waypoints.data.currentPath > 0 then
            waypoints.walkToNext()
        else
            waypoints.data.isWalking = false
            print("Caminho concluído!")
        end
    end
end

function waypoints.addWaypoint(name, position)
    waypoints.data.points[name] = position
    waypoints.saveWaypoints()
    print("Waypoint adicionado:", name, position.x, position.y, position.z)
end

function waypoints.removeWaypoint(name)
    waypoints.data.points[name] = nil
    waypoints.saveWaypoints()
    print("Waypoint removido:", name)
end

function waypoints.walkTo(name)
    local position = waypoints.data.points[name]
    if not position then
        print("Waypoint não encontrado:", name)
        return
    end
    
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    local path = g_map.findPath(player:getPosition(), position, 1000)
    if path then
        waypoints.data.currentPath = path
        waypoints.data.isWalking = true
        waypoints.walkToNext()
        print("Iniciando caminho para:", name)
    else
        print("Caminho não encontrado para:", name)
    end
end

function waypoints.walkToNext()
    if #waypoints.data.currentPath > 0 then
        local nextPos = waypoints.data.currentPath[1]
        g_game.walk(nextPos)
    end
end

function waypoints.stopWalking()
    waypoints.data.isWalking = false
    waypoints.data.currentPath = {}
    g_game.stop()
    print("Caminho interrompido!")
end

function waypoints.loadWaypoints()
    -- Carregar waypoints do arquivo
    local file = io.open("waypoints.txt", "r")
    if file then
        for line in file:lines() do
            local name, x, y, z = line:match("(.+):(%d+),(%d+),(%d+)")
            if name and x and y and z then
                waypoints.data.points[name] = { x = tonumber(x), y = tonumber(y), z = tonumber(z) }
            end
        end
        file:close()
    end
end

function waypoints.saveWaypoints()
    -- Salvar waypoints no arquivo
    local file = io.open("waypoints.txt", "w")
    if file then
        for name, position in pairs(waypoints.data.points) do
            file:write(string.format("%s:%d,%d,%d\n", name, position.x, position.y, position.z))
        end
        file:close()
    end
end

function waypoints.terminate()
    waypoints.stopWalking()
    
    disconnect(g_game, { 
        onGameStart = waypoints.onGameStart,
        onGameEnd = waypoints.onGameEnd,
        onWalkFinish = waypoints.onWalkFinish
    })
    
    print("Waypoints finalizado!")
end

return waypoints
```

---

## 🔗 **Dependências e Integração**

### **Dependências Internas**
- **gamelib**: Biblioteca principal de jogo
- **corelib**: Biblioteca core de utilitários
- **ModuleManager**: Sistema de gerenciamento de módulos
- **EventSystem**: Sistema de eventos
- **LuaEngine**: Interface Lua/C++

### **Integração com Outros Sistemas**
- **Sistema de UI**: Interfaces de módulos
- **Sistema de Rede**: Comunicação com servidor
- **Sistema de Gráficos**: Renderização de elementos
- **Sistema de Eventos**: Comunicação entre módulos
- **Sistema de Lua**: Scripting de funcionalidades

### **APIs Relacionadas**
```lua
-- Sistema de UI
g_ui.createWidget()
g_ui.getWidgetById()

-- Sistema de Rede
g_game.connect()
g_game.disconnect()

-- Sistema de Eventos
connect(object, events)
disconnect(object, events)
signalcall(event, ...)

-- Sistema de Módulos
g_modules.loadModule(name)
g_modules.unloadModule(name)
g_modules.isModuleLoaded(name)
```

---

## 🚀 **Melhores Práticas**

### **1. Estrutura de Módulos**
```lua
-- Sempre use estrutura modular
local meuModulo = {}

function meuModulo.init()
    -- Inicialização
end

function meuModulo.terminate()
    -- Limpeza
end

return meuModulo
```

### **2. Gerenciamento de Eventos**
```lua
-- Sempre desconecte eventos
local connections = {}

function meuModulo.init()
    connections.gameStart = connect(g_game, { 
        onGameStart = meuModulo.onGameStart 
    })
end

function meuModulo.terminate()
    for _, connection in pairs(connections) do
        disconnect(connection)
    end
end
```

### **3. Tratamento de Erros**
```lua
-- Use pcall para operações críticas
local success, result = pcall(function()
    return operacaoCritica()
end)

if not success then
    print("Erro:", result)
end
```

### **4. Performance**
```lua
-- Cache de objetos frequentemente usados
local cachedPlayer = g_game.getLocalPlayer()

-- Use scheduleEvent para operações não críticas
scheduleEvent(function()
    -- Operação não crítica
end, 1000)
```

---

## 🔍 **Debugging e Desenvolvimento**

### **Ferramentas de Debug**
```lua
-- Console de debug
g_logger.debug("Mensagem de debug")
g_logger.info("Mensagem de informação")
g_logger.warning("Aviso")
g_logger.error("Erro")

-- Inspeção de objetos
print(dump(objeto))

-- Profiling
local startTime = g_clock.millis()
-- ... código ...
local endTime = g_clock.millis()
print("Tempo de execução:", endTime - startTime, "ms")
```

### **Desenvolvimento de Módulos**
```lua
-- Recarregar módulo durante desenvolvimento
g_modules.reloadModule("meu_modulo")

-- Verificar dependências
for name, module in pairs(g_modules.getModules()) do
    print("Módulo:", name, "Carregado:", module:isLoaded())
end
```

---

## 📖 **Referência Completa**

### **APIs de Game**
- `g_game.login(account, password, character)`
- `g_game.logout()`
- `g_game.isOnline()`
- `g_game.getLocalPlayer()`
- `g_game.walk(direction)`
- `g_game.turn(direction)`
- `g_game.stop()`
- `g_game.attack(creature)`
- `g_game.follow(creature)`
- `g_game.use(item, position)`
- `g_game.move(item, position, count)`
- `g_game.talk(message)`

### **APIs de Player**
- `player:getName()`
- `player:getLevel()`
- `player:getExperience()`
- `player:getHealthPercent()`
- `player:getManaPercent()`
- `player:getCap()`
- `player:getStamina()`
- `player:getPosition()`
- `player:getDirection()`
- `player:getOutfit()`

### **APIs de Creature**
- `creature:getName()`
- `creature:getHealthPercent()`
- `creature:getDirection()`
- `creature:getPosition()`
- `creature:getOutfit()`
- `creature:isNpc()`
- `creature:isMonster()`
- `creature:isPlayer()`

### **APIs de Items**
- `item:getId()`
- `item:getCount()`
- `item:getPosition()`
- `item:getName()`
- `item:getDescription()`

### **APIs de Spells**
- `spell:getName()`
- `spell:getWords()`
- `spell:getCooldown()`
- `spell:getManaCost()`
- `spell:getVocation()`

---

## 🎯 **Conclusão**

O **Sistema de Módulos Lua** do OTClient fornece uma base sólida e flexível para desenvolvimento de funcionalidades de jogo. Com suas APIs de alto nível, sistema modular e integração profunda com o cliente, permite que desenvolvedores criem módulos poderosos e personalizados.

### **Próximos Passos**
- Explore os módulos existentes em `modules/`
- Experimente com as APIs de gamelib
- Desenvolva módulos personalizados
- Integre com outros sistemas do OTClient

---

## 🔗 **Links Relacionados**

- [[otclient_arquitetura_core|Arquitetura Core do OTClient]]
- [[otclient_sistema_lua|Sistema de Lua]]
- [[otclient_sistema_ui|Sistema de UI]]
- [[otclient_sistema_rede|Sistema de Rede]]
- [[otclient_sistema_graficos|Sistema de Gráficos]]

---

*Baseado na pesquisa Habdel: OTCLIENT-008 - Módulos Lua* 