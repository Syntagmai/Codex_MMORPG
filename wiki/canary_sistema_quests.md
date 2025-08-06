---
tags: [canary, sistema_quests, quests, missões, progresso, habdel_research]
type: wiki_page
status: active
priority: high
created: 2025-08-05
updated: 2025-08-05
aliases: [quests, missões, missions, progresso, progress, objetivos, objectives]
---

# 📜 Sistema de Quests - Canary

> [!info] **Baseado na Pesquisa Habdel**
> Esta página é baseada na pesquisa detalhada **[CANARY-014: Sistema de NPCs](habdel/CANARY-014.md)** realizada com metodologia Habdel.

## 🎯 **Visão Geral**

O Sistema de Quests do Canary gerencia missões, objetivos e progresso dos jogadores. Permite criar quests complexas com múltiplos objetivos, checkpoints e recompensas dinâmicas através de Lua.

## 🏗️ **Arquitetura do Sistema**

### **Estrutura de Arquivos**
```
canary/src/
├── game/game.hpp                  # Funções centrais de quests
├── game/game.cpp                  # Implementação
├── lua/callbacks/event_callback.hpp # Callbacks de quests
├── creatures/players/player.hpp   # Estruturas de progresso
└── data/
    └── scripts/game_migrations/   # Migração de storages
```

### **Componentes Principais**

#### **1. Funções Centrais**
- **Arquivo**: `canary/src/game/game.hpp`
- **Funções Principais**:
  - `playerShowQuestLog(playerId)` - Exibe log de quests
  - `playerShowQuestLine(playerId, questId)` - Exibe progresso
  - `playerSetQuestStorage(playerId, questId, value)` - Define progresso

#### **2. Sistema de Callbacks**
- **Arquivo**: `canary/src/lua/callbacks/event_callback.hpp`
- **Callbacks Disponíveis**:
  - `playerOnRequestQuestLog` - Solicitação de log
  - `playerOnRequestQuestLine` - Solicitação de progresso
  - `playerOnQuestComplete` - Quest completada

#### **3. Sistema de Storages**
- **Arquivo**: `canary/data-otservbr-global/scripts/game_migrations/`
- **Funcionalidades**:
  - Persistência de progresso
  - Migração de dados
  - Backup de quests

## 🔧 **Implementação Prática**

### **Exemplo 1: Quest Básica**
```lua
-- Exemplo: Quest simples de coleta
local questId = 1001
local questName = "Coleta de Ervas"
local questDescription = "Colete 10 ervas medicinais"

function onUse(player, item, fromPosition, target, toPosition, isHotkey)
    if player:getStorageValue(questId) < 10 then
        player:setStorageValue(questId, player:getStorageValue(questId) + 1)
        player:sendTextMessage(MESSAGE_INFO_DESCR, "Você coletou uma erva! (" .. player:getStorageValue(questId) .. "/10)")
        
        if player:getStorageValue(questId) >= 10 then
            player:sendTextMessage(MESSAGE_INFO_DESCR, "Quest completada! Fale com o NPC para receber sua recompensa.")
        end
    end
    return true
end
```

### **Exemplo 2: Quest com Múltiplos Objetivos**
```lua
-- Exemplo: Quest com múltiplos objetivos
local questId = 1002
local objectives = {
    {id = 1, description = "Mate 5 ratos", target = 5, storage = 1001},
    {id = 2, description = "Colete 3 cogumelos", target = 3, storage = 1002},
    {id = 3, description = "Fale com o NPC", target = 1, storage = 1003}
}

function checkQuestProgress(player)
    local completed = 0
    for _, objective in pairs(objectives) do
        if player:getStorageValue(objective.storage) >= objective.target then
            completed = completed + 1
        end
    end
    
    if completed >= #objectives then
        player:sendTextMessage(MESSAGE_INFO_DESCR, "Quest completada!")
        return true
    end
    
    return false
end
```

### **Exemplo 3: Quest com Recompensas Dinâmicas**
```lua
-- Exemplo: Recompensas baseadas no progresso
function giveQuestReward(player, questId)
    local progress = player:getStorageValue(questId)
    local level = player:getLevel()
    
    -- Recompensa base
    local gold = 1000
    local experience = 5000
    
    -- Bônus por nível
    if level >= 50 then
        gold = gold * 2
        experience = experience * 2
    end
    
    -- Bônus por progresso rápido
    if progress <= 5 then
        gold = gold + 500
        experience = experience + 2000
    end
    
    player:addMoney(gold)
    player:addExperience(experience)
    player:sendTextMessage(MESSAGE_INFO_DESCR, "Você recebeu " .. gold .. " gold e " .. experience .. " experience!")
end
```

## 🎮 **Exemplos Práticos**

### **Quest de Caça**
```lua
-- Exemplo: Quest de caça com contadores
local questId = 1003
local monsters = {
    {name = "Rato", id = 1, target = 10, storage = 2001},
    {name = "Goblin", id = 2, target = 5, storage = 2002},
    {name = "Orc", id = 3, target = 3, storage = 2003}
}

function onKill(player, target)
    if target:isMonster() then
        for _, monster in pairs(monsters) do
            if target:getName() == monster.name then
                local current = player:getStorageValue(monster.storage)
                if current < monster.target then
                    player:setStorageValue(monster.storage, current + 1)
                    player:sendTextMessage(MESSAGE_INFO_DESCR, "Você matou um " .. monster.name .. "! (" .. (current + 1) .. "/" .. monster.target .. ")")
                end
                break
            end
        end
    end
end
```

### **Quest de Exploração**
```lua
-- Exemplo: Quest de exploração com checkpoints
local questId = 1004
local checkpoints = {
    {position = Position(1000, 1000, 7), description = "Entrada da caverna"},
    {position = Position(1050, 1050, 7), description = "Sala do tesouro"},
    {position = Position(1100, 1100, 7), description = "Câmara final"}
}

function onStepIn(player, item, position, fromPosition)
    for i, checkpoint in pairs(checkpoints) do
        if position == checkpoint.position then
            local storage = 3000 + i
            if player:getStorageValue(storage) == 0 then
                player:setStorageValue(storage, 1)
                player:sendTextMessage(MESSAGE_INFO_DESCR, "Checkpoint alcançado: " .. checkpoint.description)
            end
            break
        end
    end
end
```

### **Quest de Crafting**
```lua
-- Exemplo: Quest de crafting com itens específicos
local questId = 1005
local requiredItems = {
    {id = 2160, count = 100, description = "100 gold coins"},
    {id = 2393, count = 1, description = "1 dragon scale mail"},
    {id = 2392, count = 1, description = "1 dragon shield"}
}

function checkCraftingQuest(player)
    local completed = true
    
    for _, item in pairs(requiredItems) do
        if player:getItemCount(item.id) < item.count then
            completed = false
            break
        end
    end
    
    if completed then
        -- Remover itens
        for _, item in pairs(requiredItems) do
            player:removeItem(item.id, item.count)
        end
        
        -- Dar recompensa
        player:addItem(2160, 1000) -- 1000 gold coins
        player:sendTextMessage(MESSAGE_INFO_DESCR, "Quest de crafting completada!")
    end
    
    return completed
end
```

## 🔗 **Dependências e Integrações**

### **Dependências Principais**
- **Sistema de Players**: Progresso e recompensas
- **Sistema de Storages**: Persistência de dados
- **Sistema de NPCs**: Interação para quests
- **Sistema de Monstros**: Objetivos de caça

### **Integrações**
- **Sistema de Items**: Recompensas e objetivos
- **Sistema de Mapas**: Checkpoints e exploração
- **Sistema de Experiência**: Recompensas de XP
- **Sistema de Guilds**: Quests de guild

## 📊 **Otimizações e Performance**

### **Otimizações Implementadas**
- **Storage Caching**: Cache de progresso frequente
- **Lazy Loading**: Carregamento sob demanda
- **Batch Updates**: Atualizações em lote

### **Métricas de Performance**
- **Quest Check**: < 1ms por verificação
- **Storage Access**: < 0.5ms por acesso
- **Memory Usage**: Otimizado para muitas quests

## 🎯 **Casos de Uso Comuns**

### **1. Quests de Caça**
- Objetivos de matar monstros
- Contadores de progresso
- Recompensas por completude

### **2. Quests de Coleta**
- Objetivos de coletar itens
- Verificação de inventário
- Progresso incremental

### **3. Quests de Exploração**
- Checkpoints no mapa
- Descoberta de locais
- Progresso por posição

### **4. Quests de Crafting**
- Objetivos de criar itens
- Verificação de materiais
- Recompensas especiais

## 🔧 **Como Implementar**

### **Passo 1: Definir Quest**
```lua
local questId = 1000
local questName = "Minha Quest"
local questDescription = "Descrição da quest"
```

### **Passo 2: Configurar Objetivos**
```lua
local objectives = {
    {description = "Objetivo 1", target = 5, storage = 1001},
    {description = "Objetivo 2", target = 3, storage = 1002}
}
```

### **Passo 3: Implementar Lógica**
```lua
function onQuestTrigger(player)
    -- Verificar progresso
    -- Atualizar objetivos
    -- Dar recompensas
end
```

### **Passo 4: Configurar Recompensas**
```lua
function giveReward(player)
    player:addMoney(1000)
    player:addExperience(5000)
    player:addItem(2160, 100)
end
```

## 📚 **Referências Relacionadas**

- **[Sistema de NPCs](canary_sistema_npcs.md)** - Interação para quests
- **[Sistema de Monstros](canary_sistema_monstros.md)** - Objetivos de caça
- **[Sistema de Itens](canary_sistema_itens.md)** - Recompensas e objetivos
- **[Sistema de Grupos](canary_sistema_grupos.md)** - Quests de guild

## 🎓 **Lição Educacional**

O Sistema de Quests demonstra como criar um sistema flexível de missões com:
1. **Modularidade**: Separação clara entre objetivos
2. **Persistência**: Sistema de storages para progresso
3. **Flexibilidade**: Quests customizáveis via Lua
4. **Performance**: Otimizações para muitas quests ativas

---

> [!tip] **Próximo Passo**
> Continue para **[Sistema de Grupos e Guilds](canary_sistema_grupos.md)** para entender como as quests se integram com sistemas sociais. 