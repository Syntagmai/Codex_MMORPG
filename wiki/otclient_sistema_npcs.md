---
tags: [otclient, sistema, npcs, npc, trade, chat, quests, wiki]
type: wiki_page
status: published
priority: high
created: 2025-08-05
updated: 2025-08-05
---

# 🗣️ **Sistema de NPCs - OTClient**

> [!info] **Sistema de Interação com NPCs**
> O sistema de NPCs do OTClient gerencia interações com NPCs, comércio, diálogos e fornece APIs para automação de interações com NPCs.

---

## 📋 **Visão Geral**

O **Sistema de NPCs** do OTClient é responsável por:

- **Interação com NPCs**: Diálogos e conversas
- **Sistema de Comércio**: Compra e venda de itens
- **Sistema de Quests**: Missões e tarefas
- **Auto-Trade**: Automação de comércio
- **NPC Tracking**: Rastreamento de NPCs específicos

---

## 🏗️ **Arquitetura do Sistema**

### **Componentes Principais**

```cpp
// Estrutura principal do sistema de NPCs
class NPCSystem {
    std::map<uint32_t, NPCPtr> m_npcs;              // NPCs conhecidos
    NPCPtr m_currentNPC;                            // NPC atual
    std::vector<TradeItem> m_tradeItems;            // Itens para comércio
    std::vector<QuestInfo> m_quests;                // Informações de quests
    bool m_tradeWindowOpen;                         // Janela de comércio aberta
};
```

### **Hierarquia de NPCs**

```
NPCSystem
├── NPCInteraction (Interação com NPCs)
│   ├── Chat (Conversa)
│   ├── Trade (Comércio)
│   └── Quests (Missões)
├── NPCTypes (Tipos de NPCs)
│   ├── Merchant (Mercador)
│   ├── QuestGiver (Doador de Quest)
│   ├── Banker (Banqueiro)
│   └── Trainer (Treinador)
└── NPCAutomation (Automação)
    ├── AutoTrade (Auto-Comércio)
    ├── AutoQuest (Auto-Quest)
    └── NPCTracking (Rastreamento)
```

---

## 🔧 **APIs e Interfaces**

### **Interação com NPCs**

```lua
-- Falar com NPC
g_game.talk(message)

-- Falar com NPC específico
g_game.talkPrivate(Otc.MessagePrivate, npcName, message)

-- Abrir comércio com NPC
g_game.openNpcTrade(npcName)

-- Fechar comércio
g_game.closeNpcTrade()

-- Comprar item de NPC
g_game.buyItem(item, amount, ignoreCapacity, buyWithBackpack)

-- Vender item para NPC
g_game.sellItem(item, amount, ignoreEquipped)
```

### **Gerenciamento de NPCs**

```lua
-- Obter NPC por nome
local npc = g_map.getCreatureByName(npcName)

-- Verificar se criatura é NPC
local isNPC = creature:isNpc()

-- Obter NPCs próximos
local npcs = g_map.getSpectatorsInRangeEx(centerPos, multiFloor, minX, maxX, minY, maxY)

-- Filtrar apenas NPCs
local function getNearbyNPCs()
    local creatures = g_map.getSpectatorsInRangeEx(
        g_game.getLocalPlayer():getPosition(),
        true, -10, 10, -10, 10
    )
    
    local npcs = {}
    for _, creature in ipairs(creatures) do
        if creature:isNpc() then
            table.insert(npcs, creature)
        end
    end
    
    return npcs
end
```

### **Sistema de Comércio**

```lua
-- Obter itens do NPC
local npcItems = g_game.getNpcItems()

-- Obter itens do jogador para venda
local playerItems = g_game.getPlayerItems()

-- Verificar preço de item
local price = g_game.getItemPrice(item)

-- Comprar item com mochila
g_game.buyItem(item, amount, false, true)

-- Vender item ignorando equipado
g_game.sellItem(item, amount, true)
```

---

## 📚 **Exemplos Práticos**

### **Exemplo 1: Sistema de Auto-Trade**

```lua
-- Sistema básico de auto-trade
local function autoTradeWithNPC(npcName, tradeConfig)
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    -- Procurar NPC
    local npc = g_map.getCreatureByName(npcName)
    if not npc then
        print("NPC não encontrado: " .. npcName)
        return
    end
    
    -- Verificar distância
    local distance = player:getPosition():getDistanceFrom(npc:getPosition())
    if distance > 3 then
        print("NPC muito longe: " .. distance .. " tiles")
        return
    end
    
    -- Abrir comércio
    g_game.openNpcTrade(npcName)
    
    -- Aguardar janela de comércio abrir
    scheduleEvent(function()
        -- Comprar itens configurados
        for _, itemConfig in ipairs(tradeConfig.buy) do
            local item = g_game.findNpcItem(itemConfig.id, -1)
            if item then
                g_game.buyItem(item, itemConfig.amount, false, true)
                print("Comprando: " .. item:getName() .. " x" .. itemConfig.amount)
            end
        end
        
        -- Vender itens configurados
        for _, itemConfig in ipairs(tradeConfig.sell) do
            local item = g_game.findPlayerItem(itemConfig.id, -1)
            if item then
                g_game.sellItem(item, itemConfig.amount, true)
                print("Vendendo: " .. item:getName() .. " x" .. itemConfig.amount)
            end
        end
        
        -- Fechar comércio
        g_game.closeNpcTrade()
    end, 1000)
end

-- Configuração de comércio
local tradeConfig = {
    buy = {
        {id = 7618, amount = 50, name = "Health Potions"},
        {id = 7590, amount = 50, name = "Mana Potions"},
        {id = 3600, amount = 100, name = "Food"}
    },
    sell = {
        {id = 3031, amount = 1000, name = "Gold Coins"}, -- Vender gold coins
        {id = 3035, amount = 100, name = "Platinum Coins"} -- Vender platinum coins
    }
}

-- Uso: autoTradeWithNPC("Merchant", tradeConfig)
```

### **Exemplo 2: Sistema de Auto-Quest**

```lua
-- Sistema de auto-quest
local function autoQuest(npcName, questConfig)
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    -- Procurar NPC
    local npc = g_map.getCreatureByName(npcName)
    if not npc then
        print("NPC não encontrado: " .. npcName)
        return
    end
    
    -- Falar com NPC
    g_game.talk("hi")
    
    scheduleEvent(function()
        -- Responder com palavras-chave
        for _, keyword in ipairs(questConfig.keywords) do
            g_game.talk(keyword)
            scheduleEvent(function() end, 500) -- Aguardar resposta
        end
        
        -- Entregar itens se necessário
        for _, itemReq in ipairs(questConfig.requirements) do
            local item = g_game.findPlayerItem(itemReq.id, -1)
            if item and item:getCount() >= itemReq.amount then
                g_game.move(item, npc:getPosition(), itemReq.amount)
                print("Entregando: " .. item:getName() .. " x" .. itemReq.amount)
            end
        end
        
        -- Finalizar conversa
        g_game.talk("bye")
    end, 1000)
end

-- Configuração de quest
local questConfig = {
    keywords = {"quest", "mission", "task"},
    requirements = {
        {id = 3031, amount = 100, name = "Gold Coins"},
        {id = 3600, amount = 50, name = "Food"}
    }
}

-- Uso: autoQuest("QuestGiver", questConfig)
```

### **Exemplo 3: Sistema de NPC Tracking**

```lua
-- Sistema de rastreamento de NPCs
local function setupNPCTracking()
    local trackedNPCs = {}
    
    -- Adicionar NPC ao rastreamento
    local function trackNPC(npcName, npcType, location)
        trackedNPCs[npcName] = {
            type = npcType,
            location = location,
            lastSeen = nil,
            status = "unknown"
        }
    end
    
    -- Verificar NPCs próximos
    local function checkNearbyNPCs()
        local player = g_game.getLocalPlayer()
        if not player then return end
        
        local creatures = g_map.getSpectatorsInRangeEx(
            player:getPosition(),
            true, -15, 15, -15, 15
        )
        
        for _, creature in ipairs(creatures) do
            if creature:isNpc() then
                local npcName = creature:getName()
                local npcData = trackedNPCs[npcName]
                
                if npcData then
                    npcData.lastSeen = os.time()
                    npcData.status = "nearby"
                    npcData.currentLocation = creature:getPosition()
                    
                    print("NPC encontrado: " .. npcName .. " em " .. creature:getPosition():toString())
                end
            end
        end
    end
    
    -- Navegar até NPC
    local function goToNPC(npcName)
        local npcData = trackedNPCs[npcName]
        if npcData and npcData.currentLocation then
            -- Usar sistema de navegação para ir até o NPC
            local path, result = g_map.findPath(
                g_game.getLocalPlayer():getPosition(),
                npcData.currentLocation,
                1000, 0
            )
            
            if result == Otc.PathFindResult.Ok then
                for _, direction in ipairs(path) do
                    g_game.walk(direction)
                    scheduleEvent(function() end, 300)
                end
                print("Navegando até: " .. npcName)
            end
        end
    end
    
    -- Configurar NPCs para rastrear
    trackNPC("Merchant", "trade", Position(100, 100, 7))
    trackNPC("Banker", "bank", Position(101, 100, 7))
    trackNPC("QuestGiver", "quest", Position(102, 100, 7))
    
    return {
        checkNearbyNPCs = checkNearbyNPCs,
        goToNPC = goToNPC,
        trackedNPCs = trackedNPCs
    }
end

-- Uso do sistema
local npcTracker = setupNPCTracking()
scheduleEvent(npcTracker.checkNearbyNPCs, 5000) -- Verificar a cada 5 segundos
```

---

## 🎮 **Sistema de Comércio Avançado**

### **Gerenciamento de Preços**

```lua
-- Sistema de gerenciamento de preços
local function setupPriceManagement()
    local priceDatabase = {}
    
    -- Adicionar preço ao banco de dados
    local function addPrice(itemId, itemName, buyPrice, sellPrice, npcName)
        priceDatabase[itemId] = {
            name = itemName,
            buyPrice = buyPrice,
            sellPrice = sellPrice,
            npcName = npcName,
            lastUpdate = os.time()
        }
    end
    
    -- Verificar se item é lucrativo
    local function isProfitable(itemId, currentBuyPrice, currentSellPrice)
        local itemData = priceDatabase[itemId]
        if itemData then
            local profit = currentSellPrice - currentBuyPrice
            local profitMargin = (profit / currentBuyPrice) * 100
            
            return profitMargin > 20 -- 20% de margem de lucro
        end
        return false
    end
    
    -- Auto-compra de itens lucrativos
    local function autoBuyProfitableItems()
        local npcItems = g_game.getNpcItems()
        
        for _, item in ipairs(npcItems) do
            local itemId = item:getId()
            local buyPrice = g_game.getItemPrice(item)
            local sellPrice = priceDatabase[itemId] and priceDatabase[itemId].sellPrice or buyPrice
            
            if isProfitable(itemId, buyPrice, sellPrice) then
                local playerMoney = g_game.getLocalPlayer():getMoney()
                local maxAffordable = math.floor(playerMoney / buyPrice)
                
                if maxAffordable > 0 then
                    local buyAmount = math.min(maxAffordable, 100) -- Máximo 100 por vez
                    g_game.buyItem(item, buyAmount, false, true)
                    print("Comprando item lucrativo: " .. item:getName() .. " x" .. buyAmount)
                end
            end
        end
    end
    
    -- Configurar preços conhecidos
    addPrice(7618, "Health Potion", 45, 50, "Merchant")
    addPrice(7590, "Mana Potion", 56, 65, "Merchant")
    addPrice(3600, "Bread", 2, 3, "Merchant")
    
    return {
        addPrice = addPrice,
        isProfitable = isProfitable,
        autoBuyProfitableItems = autoBuyProfitableItems
    }
end

-- Uso do sistema
local priceManager = setupPriceManagement()
```

### **Sistema de Auto-Refill**

```lua
-- Sistema de auto-refill de itens
local function autoRefillFromNPC(npcName, refillConfig)
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    -- Verificar itens que precisam de refill
    for _, itemConfig in ipairs(refillConfig) do
        local currentItem = g_game.findPlayerItem(itemConfig.id, -1)
        local currentCount = currentItem and currentItem:getCount() or 0
        
        if currentCount < itemConfig.minAmount then
            local needed = itemConfig.targetAmount - currentCount
            
            -- Verificar se tem dinheiro
            local playerMoney = g_game.getLocalPlayer():getMoney()
            local itemPrice = itemConfig.price or 50 -- Preço padrão
            local totalCost = needed * itemPrice
            
            if playerMoney >= totalCost then
                -- Navegar até NPC se necessário
                local npc = g_map.getCreatureByName(npcName)
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
                    
                    -- Comprar itens
                    scheduleEvent(function()
                        g_game.openNpcTrade(npcName)
                        
                        scheduleEvent(function()
                            local npcItem = g_game.findNpcItem(itemConfig.id, -1)
                            if npcItem then
                                g_game.buyItem(npcItem, needed, false, true)
                                print("Refill: " .. itemConfig.name .. " +" .. needed)
                            end
                            
                            g_game.closeNpcTrade()
                        end, 1000)
                    end, 2000)
                end
            else
                print("⚠️ Sem dinheiro para refill: " .. itemConfig.name)
            end
        end
    end
end

-- Configuração de refill
local refillConfig = {
    {id = 7618, name = "Health Potions", minAmount = 10, targetAmount = 100, price = 45},
    {id = 7590, name = "Mana Potions", minAmount = 10, targetAmount = 100, price = 56},
    {id = 3600, name = "Food", minAmount = 20, targetAmount = 200, price = 2}
}

-- Uso: autoRefillFromNPC("Merchant", refillConfig)
```

---

## 🔍 **Sistema de Diálogos Inteligentes**

### **Gerenciamento de Conversas**

```lua
-- Sistema de diálogos inteligentes
local function setupIntelligentDialogue()
    local dialogueResponses = {
        ["hi"] = {"hello", "greetings", "good day"},
        ["quest"] = {"mission", "task", "job"},
        ["bye"] = {"farewell", "goodbye", "see you"},
        ["trade"] = {"buy", "sell", "shop"},
        ["bank"] = {"deposit", "withdraw", "balance"}
    }
    
    local function respondToNPC(message)
        local lowerMessage = message:lower()
        
        for keyword, responses in pairs(dialogueResponses) do
            if lowerMessage:find(keyword) then
                local response = responses[math.random(1, #responses)]
                g_game.talk(response)
                return response
            end
        end
        
        -- Resposta padrão
        g_game.talk("yes")
        return "yes"
    end
    
    -- Sistema de diálogo automático
    local function autoDialogue(npcName, dialogueFlow)
        local currentStep = 1
        
        local function executeStep()
            if currentStep <= #dialogueFlow then
                local step = dialogueFlow[currentStep]
                
                if step.action == "say" then
                    g_game.talk(step.message)
                elseif step.action == "wait" then
                    scheduleEvent(executeStep, step.delay or 1000)
                    return
                elseif step.action == "condition" then
                    if step.condition() then
                        g_game.talk(step.trueMessage)
                    else
                        g_game.talk(step.falseMessage)
                    end
                end
                
                currentStep = currentStep + 1
                scheduleEvent(executeStep, 1000)
            end
        end
        
        executeStep()
    end
    
    return {
        respondToNPC = respondToNPC,
        autoDialogue = autoDialogue
    }
end

-- Exemplo de fluxo de diálogo
local dialogueFlow = {
    {action = "say", message = "hi"},
    {action = "wait", delay = 1000},
    {action = "say", message = "quest"},
    {action = "wait", delay = 1000},
    {action = "condition", condition = function() 
        return g_game.findPlayerItem(3031, -1) and g_game.findPlayerItem(3031, -1):getCount() >= 100
    end, trueMessage = "yes", falseMessage = "no"},
    {action = "wait", delay = 1000},
    {action = "say", message = "bye"}
}

-- Uso: autoDialogue("QuestGiver", dialogueFlow)
```

---

## 🔗 **Integração com Outros Sistemas**

### **Sistema de Eventos**

```lua
-- Conectar eventos de NPCs
connect(g_game, {
    onOpenNpcTrade = function(npcName)
        print("Comércio aberto com: " .. npcName)
    end,
    
    onCloseNpcTrade = function()
        print("Comércio fechado")
    end,
    
    onPlayerGoods = function(money, goods)
        print("Dinheiro: " .. money .. " gold")
        for _, item in ipairs(goods) do
            print("Item: " .. item:getName() .. " x" .. item:getCount())
        end
    end
})

connect(LocalPlayer, {
    onMoneyChange = function(money)
        print("Dinheiro alterado: " .. money .. " gold")
    end
})
```

### **Sistema de UI**

```lua
-- Interface de controle de NPCs
local function createNPCControlUI()
    local window = g_ui.createWidget('MainWindow')
    window:setText('Controle de NPCs')
    window:setSize({width = 400, height = 300})
    
    -- Lista de NPCs próximos
    local npcList = g_ui.createWidget('TextList', window)
    npcList:setPosition({x = 10, y = 10})
    npcList:setSize({width = 200, height = 200})
    
    -- Botão de atualizar lista
    local refreshButton = g_ui.createWidget('Button', window)
    refreshButton:setText('Atualizar NPCs')
    refreshButton:setPosition({x = 220, y = 10})
    refreshButton.onClick = function()
        npcList:clearChildren()
        local npcs = getNearbyNPCs()
        for _, npc in ipairs(npcs) do
            local label = g_ui.createWidget('Label', npcList)
            label:setText(npc:getName() .. " - " .. npc:getPosition():toString())
        end
    end
    
    -- Botão de auto-trade
    local tradeButton = g_ui.createWidget('Button', window)
    tradeButton:setText('Auto-Trade')
    tradeButton:setPosition({x = 220, y = 40})
    tradeButton.onClick = function()
        local selectedNPC = npcList:getSelectedChild()
        if selectedNPC then
            local npcName = selectedNPC:getText():match("^([^-]+)")
            autoTradeWithNPC(npcName, tradeConfig)
        end
    end
    
    -- Botão de auto-quest
    local questButton = g_ui.createWidget('Button', window)
    questButton:setText('Auto-Quest')
    questButton:setPosition({x = 220, y = 70})
    questButton.onClick = function()
        local selectedNPC = npcList:getSelectedChild()
        if selectedNPC then
            local npcName = selectedNPC:getText():match("^([^-]+)")
            autoQuest(npcName, questConfig)
        end
    end
    
    return window
end
```

---

## 📊 **Dependências e Relacionamentos**

### **Dependências Principais**
- **Sistema de Jogo**: APIs de interação com NPCs
- **Sistema de Mapas**: Posicionamento de NPCs
- **Sistema de Inventário**: Gerenciamento de itens para comércio
- **Sistema de Eventos**: Comunicação entre componentes

### **Sistemas Dependentes**
- **Sistema de Quests**: Interação com NPCs de quest
- **Sistema de Comércio**: Compra e venda de itens
- **Sistema de Interface**: Janelas de comércio e diálogo

---

## 🚀 **Melhores Práticas**

### **Otimização de Interações**

1. **Use Delays Apropriados**: Aguarde respostas do servidor
2. **Verifique Distância**: Certifique-se de estar próximo ao NPC
3. **Monitore Dinheiro**: Verifique se tem dinheiro suficiente
4. **Trate Erros**: Implemente tratamento de erros para falhas

### **Padrões de Design**

```lua
-- Padrão State para diferentes estados de interação
local NPCInteractionState = {
    IDLE = "idle",
    TALKING = "talking",
    TRADING = "trading",
    QUESTING = "questing"
}

local NPCInteractionManager = {
    currentState = NPCInteractionState.IDLE,
    currentNPC = nil,
    
    changeState = function(newState, npc)
        NPCInteractionManager.currentState = newState
        NPCInteractionManager.currentNPC = npc
    end,
    
    executeAction = function(action)
        if NPCInteractionManager.currentState == NPCInteractionState.IDLE then
            -- Ações disponíveis quando ocioso
        elseif NPCInteractionManager.currentState == NPCInteractionState.TALKING then
            -- Ações disponíveis durante conversa
        elseif NPCInteractionManager.currentState == NPCInteractionState.TRADING then
            -- Ações disponíveis durante comércio
        end
    end
}
```

---

## 📚 **Referências e Links**

### **Arquivos Relacionados**
- [[otclient_sistema_inventario|Sistema de Inventário]]
- [[otclient_sistema_quests|Sistema de Quests]]
- [[otclient_sistema_comunicacao|Sistema de Comunicação]]

### **APIs Principais**
- `g_game`: API principal do sistema de jogo
- `g_map`: API do sistema de mapas
- `Creature`: Classe base para criaturas (incluindo NPCs)

### **Constantes Importantes**
```lua
-- Tipos de NPCs
NpcIconNone = 0
NpcIconChat = 1
NpcIconTrade = 2
NpcIconQuest = 3
NpcIconTradeQuest = 4

-- Tipos de criatura
CreatureTypePlayer = 0
CreatureTypeMonster = 1
CreatureTypeNpc = 2
CreatureTypeSummonOwn = 3
CreatureTypeSummonOther = 4
CreatureTypeHidden = 5

-- Modos de mensagem
Otc.MessagePrivate = 0
Otc.MessagePrivateRed = 1
Otc.MessagePrivateRedAnonymous = 2
Otc.MessageGamemasterBroadcast = 3
Otc.MessageGamemasterChannel = 4
Otc.MessageGamemasterPrivate = 5
```

---

> [!success] **Conclusão**
> O Sistema de NPCs do OTClient fornece ferramentas completas para interação com NPCs, comércio automatizado e gerenciamento de diálogos, permitindo criar sistemas sofisticados de auto-trade e auto-quest.

---

**📖 Próximo**: [[otclient_sistema_quests|Sistema de Quests]] | **🔙 Anterior**: [[otclient_sistema_inventario|Sistema de Inventário]] 