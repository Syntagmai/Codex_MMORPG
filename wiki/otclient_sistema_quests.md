---
tags: [otclient, sistema, quests, quest, missions, tasks, tracking, wiki]
type: wiki_page
status: published
priority: high
created: 2025-08-05
updated: 2025-08-05
---

# 📜 **Sistema de Quests - OTClient**

> [!info] **Sistema de Missões e Tarefas**
> O sistema de quests do OTClient gerencia missões, tarefas, rastreamento de progresso e fornece APIs para automação de quests.

---

## 📋 **Visão Geral**

O **Sistema de Quests** do OTClient é responsável por:

- **Quest Log**: Registro de missões ativas e completadas
- **Quest Tracking**: Rastreamento de progresso de quests
- **Auto-Quest**: Automação de completação de missões
- **Quest Management**: Gerenciamento de múltiplas quests
- **Quest Rewards**: Sistema de recompensas

---

## 🏗️ **Arquitetura do Sistema**

### **Componentes Principais**

```cpp
// Estrutura principal do sistema de quests
class QuestSystem {
    std::map<uint16_t, QuestPtr> m_quests;          // Quests conhecidas
    std::vector<uint16_t> m_activeQuests;           // Quests ativas
    std::vector<uint16_t> m_completedQuests;        // Quests completadas
    QuestPtr m_trackedQuest;                        // Quest sendo rastreada
    std::map<uint16_t, QuestProgress> m_progress;   // Progresso das quests
};
```

### **Hierarquia de Quests**

```
QuestSystem
├── QuestLog (Registro de Quests)
│   ├── ActiveQuests (Quests Ativas)
│   ├── CompletedQuests (Quests Completadas)
│   └── QuestDetails (Detalhes da Quest)
├── QuestTracking (Rastreamento)
│   ├── TrackedQuest (Quest Rastreada)
│   ├── Progress (Progresso)
│   └── Objectives (Objetivos)
└── QuestAutomation (Automação)
    ├── AutoQuest (Auto-Quest)
    ├── QuestNavigation (Navegação)
    └── QuestRewards (Recompensas)
```

---

## 🔧 **APIs e Interfaces**

### **Gerenciamento de Quests**

```lua
-- Solicitar informações de quest
g_game.requestQuestLine(questId)

-- Obter quest log
local questLog = g_game.getQuestLog()

-- Verificar se quest está ativa
local isActive = g_game.isQuestActive(questId)

-- Verificar se quest está completada
local isCompleted = g_game.isQuestCompleted(questId)

-- Rastrear quest
g_game.trackQuest(questId)
```

### **Sistema de Quest Log**

```lua
-- Obter todas as quests
local function getAllQuests()
    local quests = {}
    
    -- Quests ativas
    for questId, questData in pairs(g_game.getActiveQuests()) do
        table.insert(quests, {
            id = questId,
            name = questData.name,
            status = "active",
            progress = questData.progress
        })
    end
    
    -- Quests completadas
    for questId, questData in pairs(g_game.getCompletedQuests()) do
        table.insert(quests, {
            id = questId,
            name = questData.name,
            status = "completed",
            progress = 100
        })
    end
    
    return quests
end

-- Filtrar quests por status
local function filterQuestsByStatus(status)
    local allQuests = getAllQuests()
    local filteredQuests = {}
    
    for _, quest in ipairs(allQuests) do
        if quest.status == status then
            table.insert(filteredQuests, quest)
        end
    end
    
    return filteredQuests
end
```

### **Sistema de Tracking**

```lua
-- Configurar quest para rastreamento
local function trackQuest(questId)
    g_game.trackQuest(questId)
    print("Quest rastreada: " .. questId)
end

-- Obter quest rastreada
local function getTrackedQuest()
    return g_game.getTrackedQuest()
end

-- Atualizar progresso da quest
local function updateQuestProgress(questId, progress)
    local quest = g_game.getQuest(questId)
    if quest then
        quest:setProgress(progress)
        print("Progresso da quest " .. questId .. ": " .. progress .. "%")
    end
end
```

---

## 📚 **Exemplos Práticos**

### **Exemplo 1: Sistema de Auto-Quest**

```lua
-- Sistema básico de auto-quest
local function autoQuest(questConfig)
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    -- Verificar se quest está disponível
    if not g_game.isQuestAvailable(questConfig.id) then
        print("Quest não disponível: " .. questConfig.name)
        return
    end
    
    -- Verificar se já está ativa
    if g_game.isQuestActive(questConfig.id) then
        print("Quest já ativa: " .. questConfig.name)
        return
    end
    
    -- Navegar até NPC da quest
    local npc = g_map.getCreatureByName(questConfig.npcName)
    if npc then
        local distance = player:getPosition():getDistanceFrom(npc:getPosition())
        
        if distance > 3 then
            -- Navegar até NPC
            local path, result = g_map.findPath(
                player:getPosition(),
                npc:getPosition(),
                1000, 0
            )
            
            if result == Otc.PathFindResult.Ok then
                for _, direction in ipairs(path) do
                    g_game.walk(direction)
                    scheduleEvent(function() end, 300)
                end
            end
        end
        
        -- Iniciar quest
        scheduleEvent(function()
            g_game.talk("hi")
            
            scheduleEvent(function()
                g_game.talk("quest")
                
                scheduleEvent(function()
                    -- Entregar itens se necessário
                    for _, itemReq in ipairs(questConfig.requirements) do
                        local item = g_game.findPlayerItem(itemReq.id, -1)
                        if item and item:getCount() >= itemReq.amount then
                            g_game.move(item, npc:getPosition(), itemReq.amount)
                            print("Entregando: " .. item:getName() .. " x" .. itemReq.amount)
                        end
                    end
                    
                    g_game.talk("yes")
                    g_game.talk("bye")
                    
                    print("Quest iniciada: " .. questConfig.name)
                end, 1000)
            end, 1000)
        end, 2000)
    end
end

-- Configuração de quest
local questConfig = {
    id = 1001,
    name = "The Lost Amulet",
    npcName = "QuestGiver",
    requirements = {
        {id = 3031, amount = 100, name = "Gold Coins"},
        {id = 3600, amount = 50, name = "Food"}
    }
}

-- Uso: autoQuest(questConfig)
```

### **Exemplo 2: Sistema de Quest Tracking**

```lua
-- Sistema de rastreamento de quests
local function setupQuestTracking()
    local trackedQuests = {}
    
    -- Adicionar quest ao rastreamento
    local function trackQuest(questId, questName, objectives)
        trackedQuests[questId] = {
            name = questName,
            objectives = objectives or {},
            progress = 0,
            lastUpdate = os.time()
        }
    end
    
    -- Atualizar progresso da quest
    local function updateQuestProgress(questId, objectiveId, progress)
        local quest = trackedQuests[questId]
        if quest then
            quest.objectives[objectiveId] = progress
            quest.lastUpdate = os.time()
            
            -- Calcular progresso total
            local totalProgress = 0
            local totalObjectives = 0
            
            for _, objProgress in pairs(quest.objectives) do
                totalProgress = totalProgress + objProgress
                totalObjectives = totalObjectives + 1
            end
            
            if totalObjectives > 0 then
                quest.progress = totalProgress / totalObjectives
            end
            
            print("Quest " .. quest.name .. ": " .. quest.progress .. "%")
            
            -- Verificar se quest foi completada
            if quest.progress >= 100 then
                print("🎉 Quest completada: " .. quest.name)
                return true
            end
        end
        return false
    end
    
    -- Verificar quests próximas da conclusão
    local function checkNearCompletion()
        for questId, quest in pairs(trackedQuests) do
            if quest.progress >= 90 and quest.progress < 100 then
                print("⚠️ Quest quase completa: " .. quest.name .. " (" .. quest.progress .. "%)")
            end
        end
    end
    
    -- Configurar quests para rastrear
    trackQuest(1001, "The Lost Amulet", {
        [1] = 0, -- Encontrar amuleto
        [2] = 0  -- Entregar para NPC
    })
    
    trackQuest(1002, "Monster Hunt", {
        [1] = 0, -- Matar 10 orcs
        [2] = 0  -- Matar 5 trolls
    })
    
    return {
        trackQuest = trackQuest,
        updateQuestProgress = updateQuestProgress,
        checkNearCompletion = checkNearCompletion,
        trackedQuests = trackedQuests
    }
end

-- Uso do sistema
local questTracker = setupQuestTracking()
scheduleEvent(questTracker.checkNearCompletion, 30000) -- Verificar a cada 30 segundos
```

### **Exemplo 3: Sistema de Quest Management**

```lua
-- Sistema de gerenciamento de quests
local function setupQuestManagement()
    local questManager = {
        activeQuests = {},
        completedQuests = {},
        questPriorities = {}
    }
    
    -- Adicionar quest com prioridade
    local function addQuest(questId, questName, priority)
        questManager.activeQuests[questId] = {
            name = questName,
            priority = priority or 1,
            addedTime = os.time(),
            progress = 0
        }
        
        questManager.questPriorities[questId] = priority or 1
        print("Quest adicionada: " .. questName .. " (Prioridade: " .. priority .. ")")
    end
    
    -- Obter próxima quest por prioridade
    local function getNextQuest()
        local highestPriority = 0
        local nextQuest = nil
        
        for questId, quest in pairs(questManager.activeQuests) do
            if quest.priority > highestPriority and quest.progress < 100 then
                highestPriority = quest.priority
                nextQuest = quest
            end
        end
        
        return nextQuest
    end
    
    -- Marcar quest como completada
    local function completeQuest(questId)
        local quest = questManager.activeQuests[questId]
        if quest then
            questManager.completedQuests[questId] = quest
            questManager.activeQuests[questId] = nil
            questManager.questPriorities[questId] = nil
            
            print("🎉 Quest completada: " .. quest.name)
        end
    end
    
    -- Auto-gerenciamento de quests
    local function autoManageQuests()
        local nextQuest = getNextQuest()
        if nextQuest then
            print("Próxima quest: " .. nextQuest.name .. " (Prioridade: " .. nextQuest.priority .. ")")
            
            -- Aqui você pode implementar a lógica para trabalhar na quest
            -- Por exemplo, navegar até o local, coletar itens, etc.
        else
            print("Nenhuma quest ativa para trabalhar")
        end
    end
    
    -- Configurar quests iniciais
    addQuest(1001, "The Lost Amulet", 3) -- Alta prioridade
    addQuest(1002, "Monster Hunt", 2)     -- Média prioridade
    addQuest(1003, "Item Collection", 1)  -- Baixa prioridade
    
    return {
        addQuest = addQuest,
        getNextQuest = getNextQuest,
        completeQuest = completeQuest,
        autoManageQuests = autoManageQuests,
        questManager = questManager
    }
end

-- Uso do sistema
local questManager = setupQuestManagement()
scheduleEvent(questManager.autoManageQuests, 60000) -- Verificar a cada 1 minuto
```

---

## 🎮 **Sistema de Quest Log Avançado**

### **Gerenciamento de Quest Log**

```lua
-- Sistema avançado de quest log
local function setupAdvancedQuestLog()
    local questLog = {
        quests = {},
        filters = {
            showActive = true,
            showCompleted = true,
            showHidden = false,
            showInTracker = true
        }
    }
    
    -- Adicionar quest ao log
    local function addQuestToLog(questId, questData)
        questLog.quests[questId] = {
            id = questId,
            name = questData.name,
            description = questData.description,
            status = questData.status,
            progress = questData.progress,
            objectives = questData.objectives or {},
            rewards = questData.rewards or {},
            addedTime = os.time()
        }
    end
    
    -- Filtrar quests
    local function filterQuests()
        local filteredQuests = {}
        
        for questId, quest in pairs(questLog.quests) do
            local shouldInclude = true
            
            if quest.status == "active" and not questLog.filters.showActive then
                shouldInclude = false
            elseif quest.status == "completed" and not questLog.filters.showCompleted then
                shouldInclude = false
            elseif quest.status == "hidden" and not questLog.filters.showHidden then
                shouldInclude = false
            end
            
            if shouldInclude then
                table.insert(filteredQuests, quest)
            end
        end
        
        return filteredQuests
    end
    
    -- Buscar quest por nome
    local function searchQuest(searchTerm)
        local results = {}
        local lowerSearchTerm = searchTerm:lower()
        
        for questId, quest in pairs(questLog.quests) do
            if quest.name:lower():find(lowerSearchTerm) or 
               (quest.description and quest.description:lower():find(lowerSearchTerm)) then
                table.insert(results, quest)
            end
        end
        
        return results
    end
    
    -- Estatísticas de quests
    local function getQuestStats()
        local stats = {
            total = 0,
            active = 0,
            completed = 0,
            hidden = 0,
            averageProgress = 0
        }
        
        local totalProgress = 0
        
        for _, quest in pairs(questLog.quests) do
            stats.total = stats.total + 1
            
            if quest.status == "active" then
                stats.active = stats.active + 1
                totalProgress = totalProgress + quest.progress
            elseif quest.status == "completed" then
                stats.completed = stats.completed + 1
            elseif quest.status == "hidden" then
                stats.hidden = stats.hidden + 1
            end
        end
        
        if stats.active > 0 then
            stats.averageProgress = totalProgress / stats.active
        end
        
        return stats
    end
    
    return {
        addQuestToLog = addQuestToLog,
        filterQuests = filterQuests,
        searchQuest = searchQuest,
        getQuestStats = getQuestStats,
        questLog = questLog
    }
end

-- Uso do sistema
local advancedQuestLog = setupAdvancedQuestLog()
```

### **Sistema de Quest Rewards**

```lua
-- Sistema de recompensas de quest
local function setupQuestRewards()
    local rewardSystem = {
        rewards = {},
        claimedRewards = {}
    }
    
    -- Adicionar recompensa
    local function addReward(questId, rewardData)
        rewardSystem.rewards[questId] = {
            items = rewardData.items or {},
            experience = rewardData.experience or 0,
            money = rewardData.money or 0,
            skills = rewardData.skills or {},
            claimed = false
        }
    end
    
    -- Verificar se recompensa pode ser coletada
    local function canClaimReward(questId)
        local quest = g_game.getQuest(questId)
        local reward = rewardSystem.rewards[questId]
        
        return quest and quest:isCompleted() and reward and not reward.claimed
    end
    
    -- Coletar recompensa
    local function claimReward(questId)
        if canClaimReward(questId) then
            local reward = rewardSystem.rewards[questId]
            
            -- Processar recompensas
            for _, item in ipairs(reward.items) do
                print("Recompensa: " .. item.name .. " x" .. item.count)
                -- Aqui você pode implementar a lógica para adicionar o item ao inventário
            end
            
            if reward.experience > 0 then
                print("Experiência ganha: " .. reward.experience)
            end
            
            if reward.money > 0 then
                print("Dinheiro ganho: " .. reward.money)
            end
            
            reward.claimed = true
            rewardSystem.claimedRewards[questId] = os.time()
            
            print("🎁 Recompensa coletada para quest: " .. questId)
            return true
        end
        
        return false
    end
    
    -- Auto-coleta de recompensas
    local function autoClaimRewards()
        for questId, reward in pairs(rewardSystem.rewards) do
            if canClaimReward(questId) then
                claimReward(questId)
            end
        end
    end
    
    -- Configurar recompensas
    addReward(1001, {
        items = {
            {id = 3031, name = "Gold Coin", count = 1000},
            {id = 7618, name = "Health Potion", count = 50}
        },
        experience = 5000,
        money = 500
    })
    
    return {
        addReward = addReward,
        canClaimReward = canClaimReward,
        claimReward = claimReward,
        autoClaimRewards = autoClaimRewards,
        rewardSystem = rewardSystem
    }
end

-- Uso do sistema
local questRewards = setupQuestRewards()
scheduleEvent(questRewards.autoClaimRewards, 300000) -- Verificar a cada 5 minutos
```

---

## 🔍 **Sistema de Quest Navigation**

### **Navegação para Quests**

```lua
-- Sistema de navegação para quests
local function setupQuestNavigation()
    local questLocations = {}
    
    -- Adicionar localização de quest
    local function addQuestLocation(questId, location, description)
        questLocations[questId] = {
            position = location,
            description = description,
            discovered = false
        }
    end
    
    -- Navegar até local da quest
    local function navigateToQuest(questId)
        local location = questLocations[questId]
        if location then
            local player = g_game.getLocalPlayer()
            if player then
                local playerPos = player:getPosition()
                local distance = playerPos:getDistanceFrom(location.position)
                
                if distance > 5 then
                    -- Navegar até o local
                    local path, result = g_map.findPath(
                        playerPos,
                        location.position,
                        1000, 0
                    )
                    
                    if result == Otc.PathFindResult.Ok then
                        print("🧭 Navegando para: " .. location.description)
                        
                        for _, direction in ipairs(path) do
                            g_game.walk(direction)
                            scheduleEvent(function() end, 300)
                        end
                        
                        return true
                    else
                        print("❌ Não foi possível encontrar caminho para: " .. location.description)
                        return false
                    end
                else
                    print("✅ Já está no local: " .. location.description)
                    return true
                end
            end
        end
        
        return false
    end
    
    -- Auto-navegação para quests ativas
    local function autoNavigateToQuests()
        local activeQuests = g_game.getActiveQuests()
        
        for questId, quest in pairs(activeQuests) do
            if quest.progress < 100 and questLocations[questId] then
                print("🎯 Navegando para quest: " .. quest.name)
                navigateToQuest(questId)
                break -- Navegar para uma quest por vez
            end
        end
    end
    
    -- Configurar localizações
    addQuestLocation(1001, Position(100, 100, 7), "Casa do NPC QuestGiver")
    addQuestLocation(1002, Position(150, 150, 7), "Floresta dos Orcs")
    addQuestLocation(1003, Position(200, 200, 7), "Caverna dos Trolls")
    
    return {
        addQuestLocation = addQuestLocation,
        navigateToQuest = navigateToQuest,
        autoNavigateToQuests = autoNavigateToQuests,
        questLocations = questLocations
    }
end

-- Uso do sistema
local questNavigation = setupQuestNavigation()
```

---

## 🔗 **Integração com Outros Sistemas**

### **Sistema de Eventos**

```lua
-- Conectar eventos de quests
connect(g_game, {
    onQuestLine = function(questId, questMissions)
        print("Quest recebida: " .. questId)
        for _, mission in ipairs(questMissions) do
            print("  - Missão: " .. mission.name .. " (" .. mission.description .. ")")
        end
    end
})

-- Eventos de progresso de quest
local function onQuestProgress(questId, progress)
    print("Progresso da quest " .. questId .. ": " .. progress .. "%")
    
    if progress >= 100 then
        print("🎉 Quest " .. questId .. " completada!")
    end
end
```

### **Sistema de UI**

```lua
-- Interface de controle de quests
local function createQuestControlUI()
    local window = g_ui.createWidget('MainWindow')
    window:setText('Controle de Quests')
    window:setSize({width = 450, height = 350})
    
    -- Lista de quests ativas
    local activeQuestsList = g_ui.createWidget('TextList', window)
    activeQuestsList:setPosition({x = 10, y = 10})
    activeQuestsList:setSize({width = 200, height = 150})
    
    -- Lista de quests completadas
    local completedQuestsList = g_ui.createWidget('TextList', window)
    completedQuestsList:setPosition({x = 10, y = 170})
    completedQuestsList:setSize({width = 200, height = 150})
    
    -- Botão de atualizar quests
    local refreshButton = g_ui.createWidget('Button', window)
    refreshButton:setText('Atualizar Quests')
    refreshButton:setPosition({x = 220, y = 10})
    refreshButton.onClick = function()
        activeQuestsList:clearChildren()
        completedQuestsList:clearChildren()
        
        local activeQuests = filterQuestsByStatus("active")
        local completedQuests = filterQuestsByStatus("completed")
        
        for _, quest in ipairs(activeQuests) do
            local label = g_ui.createWidget('Label', activeQuestsList)
            label:setText(quest.name .. " (" .. quest.progress .. "%)")
        end
        
        for _, quest in ipairs(completedQuests) do
            local label = g_ui.createWidget('Label', completedQuestsList)
            label:setText(quest.name .. " ✅")
        end
    end
    
    -- Botão de auto-quest
    local autoQuestButton = g_ui.createWidget('Button', window)
    autoQuestButton:setText('Auto-Quest')
    autoQuestButton:setPosition({x = 220, y = 40})
    autoQuestButton.onClick = function()
        local selectedQuest = activeQuestsList:getSelectedChild()
        if selectedQuest then
            local questName = selectedQuest:getText():match("^([^(]+)")
            -- Implementar lógica de auto-quest aqui
            print("Iniciando auto-quest para: " .. questName)
        end
    end
    
    -- Botão de navegação
    local navigateButton = g_ui.createWidget('Button', window)
    navigateButton:setText('Navegar para Quest')
    navigateButton:setPosition({x = 220, y = 70})
    navigateButton.onClick = function()
        local selectedQuest = activeQuestsList:getSelectedChild()
        if selectedQuest then
            local questName = selectedQuest:getText():match("^([^(]+)")
            -- Implementar navegação aqui
            print("Navegando para quest: " .. questName)
        end
    end
    
    -- Estatísticas
    local statsLabel = g_ui.createWidget('Label', window)
    statsLabel:setPosition({x = 220, y = 120})
    statsLabel:setText("Estatísticas:\nAtivas: 0\nCompletadas: 0\nProgresso: 0%")
    
    return window
end
```

---

## 📊 **Dependências e Relacionamentos**

### **Dependências Principais**
- **Sistema de Jogo**: APIs de quests
- **Sistema de Mapas**: Navegação para locais de quest
- **Sistema de NPCs**: Interação com NPCs de quest
- **Sistema de Inventário**: Gerenciamento de itens de quest

### **Sistemas Dependentes**
- **Sistema de Recompensas**: Coleta de recompensas de quest
- **Sistema de Interface**: Quest log e tracker
- **Sistema de Navegação**: Auto-navegação para quests

---

## 🚀 **Melhores Práticas**

### **Otimização de Quests**

1. **Priorize Quests**: Use sistema de prioridades para quests
2. **Monitore Progresso**: Acompanhe progresso regularmente
3. **Auto-Navegação**: Use navegação automática para locais de quest
4. **Gerenciamento de Recompensas**: Colete recompensas automaticamente

### **Padrões de Design**

```lua
-- Padrão Observer para mudanças de quest
local QuestObserver = {
    observers = {},
    
    addObserver = function(callback)
        table.insert(QuestObserver.observers, callback)
    end,
    
    notify = function(event, data)
        for _, observer in ipairs(QuestObserver.observers) do
            observer(event, data)
        end
    end
}

-- Padrão Strategy para diferentes tipos de quest
local QuestStrategy = {
    strategies = {},
    
    addStrategy = function(questType, strategy)
        QuestStrategy.strategies[questType] = strategy
    end,
    
    executeStrategy = function(questType, questData)
        local strategy = QuestStrategy.strategies[questType]
        if strategy then
            strategy(questData)
        end
    end
}

-- Estratégias de quest
QuestStrategy.addStrategy("kill", function(questData)
    -- Estratégia para quests de matar criaturas
end)

QuestStrategy.addStrategy("collect", function(questData)
    -- Estratégia para quests de coleta
end)

QuestStrategy.addStrategy("deliver", function(questData)
    -- Estratégia para quests de entrega
end)
```

---

## 📚 **Referências e Links**

### **Arquivos Relacionados**
- [[otclient_sistema_npcs|Sistema de NPCs]]
- [[otclient_sistema_mapas|Sistema de Mapas]]
- [[otclient_sistema_inventario|Sistema de Inventário]]

### **APIs Principais**
- `g_game`: API principal do sistema de jogo
- `g_map`: API do sistema de mapas
- `Quest`: Classe para gerenciamento de quests

### **Constantes Importantes**
```lua
-- Status de quests
QuestStatusNone = 0
QuestStatusActive = 1
QuestStatusCompleted = 2
QuestStatusHidden = 3

-- Tipos de objetivo
ObjectiveTypeKill = 1
ObjectiveTypeCollect = 2
ObjectiveTypeDeliver = 3
ObjectiveTypeTalk = 4
ObjectiveTypeUse = 5

-- Tipos de recompensa
RewardTypeItem = 1
RewardTypeExperience = 2
RewardTypeMoney = 3
RewardTypeSkill = 4
```

---

> [!success] **Conclusão**
> O Sistema de Quests do OTClient fornece ferramentas completas para gerenciamento de missões, rastreamento de progresso e automação de quests, permitindo criar sistemas sofisticados de auto-quest e gerenciamento de recompensas.

---

**📖 Próximo**: [[otclient_sistema_audio|Sistema de Áudio]] | **🔙 Anterior**: [[otclient_sistema_npcs|Sistema de NPCs]] 