---
tags: [otclient, sistema, inventario, inventory, itens, containers, slots, wiki]
type: wiki_page
status: published
priority: high
created: 2025-08-05
updated: 2025-08-05
---

# 🎒 **Sistema de Inventário - OTClient**

> [!info] **Sistema de Gerenciamento de Itens**
> O sistema de inventário do OTClient gerencia itens do jogador, containers, slots de equipamento e fornece APIs para automação de gerenciamento de itens.

---

## 📋 **Visão Geral**

O **Sistema de Inventário** do OTClient é responsável por:

- **Slots de Equipamento**: Gerenciamento de itens equipados
- **Containers**: Abertura e gerenciamento de containers
- **Auto-Organização**: Scripts de organização automática
- **Loot Management**: Sistema de coleta automática
- **Item Tracking**: Rastreamento de itens específicos

---

## 🏗️ **Arquitetura do Sistema**

### **Componentes Principais**

```cpp
// Estrutura principal do sistema de inventário
class InventorySystem {
    std::map<uint8_t, ItemPtr> m_inventorySlots;     // Slots de equipamento
    std::map<uint8_t, ContainerPtr> m_containers;    // Containers abertos
    uint32_t m_capacity;                             // Capacidade total
    uint32_t m_freeCapacity;                         // Capacidade livre
    std::vector<ItemPtr> m_items;                    // Lista de itens
};
```

### **Hierarquia de Slots**

```
InventorySystem
├── EquipmentSlots (Slots de Equipamento)
│   ├── Head (Cabeça)
│   ├── Neck (Pescoço)
│   ├── Back (Costas)
│   ├── Body (Corpo)
│   ├── Right (Mão Direita)
│   ├── Left (Mão Esquerda)
│   ├── Legs (Pernas)
│   ├── Feet (Pés)
│   ├── Finger (Dedo)
│   └── Ammo (Munição)
├── Containers (Containers)
│   ├── Backpack (Mochila)
│   ├── Bags (Bolsas)
│   └── Boxes (Caixas)
└── ItemManagement (Gerenciamento de Itens)
    ├── AutoSort (Auto-Organização)
    ├── LootFilter (Filtro de Loot)
    └── ItemTracking (Rastreamento)
```

---

## 🔧 **APIs e Interfaces**

### **Gerenciamento de Slots**

```lua
-- Obter item em slot específico
local item = g_game.getLocalPlayer():getInventoryItem(slot)
-- slot: InventorySlotHead, InventorySlotNeck, etc.

-- Verificar se slot está ocupado
local hasItem = g_game.getLocalPlayer():hasInventoryItem(slot)

-- Obter todos os itens do inventário
local items = g_game.getLocalPlayer():getInventoryItems()

-- Encontrar item específico no inventário
local item = g_game.findPlayerItem(itemId, subType, tier)
```

### **Gerenciamento de Containers**

```lua
-- Abrir container
g_game.openContainer(containerId, item)

-- Fechar container
g_game.closeContainer(containerId)

-- Obter container por ID
local container = g_game.getContainer(containerId)

-- Adicionar item ao container
g_game.move(item, container, count)

-- Remover item do container
g_game.move(item, player, count)
```

### **Operações com Itens**

```lua
-- Usar item do inventário
g_game.useInventoryItem(itemId)

-- Usar item com outro item
g_game.useInventoryItemWith(itemId, targetItem)

-- Mover item
g_game.move(item, destination, count)

-- Jogar item fora
g_game.move(item, ground, count)
```

---

## 📚 **Exemplos Práticos**

### **Exemplo 1: Sistema de Auto-Organização**

```lua
-- Sistema básico de auto-organização
local function autoOrganizeInventory()
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    -- Definir categorias de itens
    local categories = {
        weapons = {2383, 2377, 2378, 2379, 2380}, -- Swords, axes, etc.
        armors = {2465, 2466, 2467, 2468, 2469},  -- Armors, helmets, etc.
        potions = {7618, 7588, 7591, 8473},       -- Health, mana potions
        runes = {3155, 3160, 3174, 3189},         -- Haste, teleport, etc.
        food = {3600, 3601, 3602, 3603}           -- Food items
    }
    
    -- Organizar por categoria
    for category, itemIds in pairs(categories) do
        for _, itemId in ipairs(itemIds) do
            local item = g_game.findPlayerItem(itemId, -1)
            if item then
                -- Mover para container específico se disponível
                local container = g_game.getContainer(0) -- Backpack
                if container then
                    g_game.move(item, container, item:getCount())
                end
            end
        end
    end
    
    print("Inventário organizado automaticamente")
end

-- Executar auto-organização a cada 5 minutos
scheduleEvent(autoOrganizeInventory, 300000)
```

### **Exemplo 2: Sistema de Auto-Loot**

```lua
-- Sistema de auto-loot com filtros
local function autoLoot()
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    -- Lista de itens para coletar automaticamente
    local lootList = {
        -- Itens valiosos
        {id = 3031, name = "Gold Coin", priority = 1},
        {id = 3035, name = "Platinum Coin", priority = 1},
        {id = 3043, name = "Crystal Coin", priority = 1},
        
        -- Potions
        {id = 7618, name = "Health Potion", priority = 2},
        {id = 7588, name = "Strong Health Potion", priority = 2},
        {id = 7591, name = "Great Health Potion", priority = 2},
        
        -- Runes
        {id = 3155, name = "Haste Spell", priority = 3},
        {id = 3160, name = "Teleport Spell", priority = 3},
        
        -- Food
        {id = 3600, name = "Bread", priority = 4},
        {id = 3601, name = "Meat", priority = 4}
    }
    
    -- Verificar capacidade
    local freeCapacity = player:getFreeCapacity()
    if freeCapacity < 100 then -- Menos de 100 oz livres
        print("Capacidade baixa: " .. freeCapacity .. " oz")
        return
    end
    
    -- Procurar itens no chão
    local playerPos = player:getPosition()
    local items = g_map.findItemsById(3031, 50) -- Procurar gold coins
    
    for pos, item in pairs(items) do
        local distance = playerPos:getDistanceFrom(pos)
        
        if distance <= 2 then -- Item próximo
            -- Verificar se está na lista de loot
            for _, lootItem in ipairs(lootList) do
                if item:getId() == lootItem.id then
                    -- Tentar coletar o item
                    g_game.move(item, playerPos, item:getCount())
                    print("Coletando: " .. lootItem.name)
                    break
                end
            end
        end
    end
end

-- Executar auto-loot a cada 2 segundos
scheduleEvent(autoLoot, 2000)
```

### **Exemplo 3: Sistema de Gerenciamento de Capacidade**

```lua
-- Sistema de gerenciamento de capacidade
local function manageCapacity()
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    local freeCapacity = player:getFreeCapacity()
    local totalCapacity = player:getCapacity()
    local usedCapacity = totalCapacity - freeCapacity
    local capacityPercent = (usedCapacity / totalCapacity) * 100
    
    -- Alertas de capacidade
    if capacityPercent >= 90 then
        print("⚠️ Capacidade crítica: " .. capacityPercent .. "%")
        
        -- Tentar jogar itens menos importantes
        local lowPriorityItems = {3600, 3601, 3602} -- Food items
        
        for _, itemId in ipairs(lowPriorityItems) do
            local item = g_game.findPlayerItem(itemId, -1)
            if item then
                g_game.move(item, player:getPosition(), item:getCount())
                print("Descartando item de baixa prioridade: " .. item:getName())
                break
            end
        end
    elseif capacityPercent >= 80 then
        print("⚠️ Capacidade alta: " .. capacityPercent .. "%")
    end
    
    -- Auto-reabastecimento de potions
    if capacityPercent < 70 then
        local healthPotion = g_game.findPlayerItem(7618, -1)
        if not healthPotion then
            -- Tentar comprar potions se tiver dinheiro
            local goldCoins = g_game.findPlayerItem(3031, -1)
            if goldCoins and goldCoins:getCount() >= 100 then
                print("Reabastecendo potions...")
                -- Lógica de compra aqui
            end
        end
    end
end

-- Executar gerenciamento de capacidade a cada 30 segundos
scheduleEvent(manageCapacity, 30000)
```

---

## 🎮 **Sistema de Containers**

### **Gerenciamento Avançado de Containers**

```lua
-- Sistema de gerenciamento de containers
local function setupContainerManagement()
    local containers = {}
    
    -- Função para abrir container
    local function openContainer(item)
        if item and item:isContainer() then
            g_game.openContainer(0, item)
            containers[0] = item
            print("Container aberto: " .. item:getName())
        end
    end
    
    -- Função para organizar containers
    local function organizeContainers()
        for containerId, container in pairs(containers) do
            if container then
                local items = container:getItems()
                
                -- Organizar itens por tipo
                for _, item in ipairs(items) do
                    local itemId = item:getId()
                    
                    -- Mover potions para container específico
                    if itemId == 7618 or itemId == 7588 then -- Health potions
                        local potionContainer = containers[1]
                        if potionContainer then
                            g_game.move(item, potionContainer, item:getCount())
                        end
                    end
                    
                    -- Mover runes para container específico
                    if itemId == 3155 or itemId == 3160 then -- Spells
                        local runeContainer = containers[2]
                        if runeContainer then
                            g_game.move(item, runeContainer, item:getCount())
                        end
                    end
                end
            end
        end
    end
    
    return {
        openContainer = openContainer,
        organizeContainers = organizeContainers,
        containers = containers
    }
end

-- Uso do sistema
local containerManager = setupContainerManagement()
```

### **Exemplo: Sistema de Auto-Refill**

```lua
-- Sistema de auto-refill de containers
local function autoRefillContainers()
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    -- Definir containers para refill
    local refillConfig = {
        {containerId = 1, itemId = 7618, minCount = 10, name = "Health Potions"}, -- Health potions
        {containerId = 2, itemId = 3155, minCount = 5, name = "Haste Spells"},    -- Haste spells
        {containerId = 3, itemId = 3600, minCount = 20, name = "Food"}            -- Food
    }
    
    for _, config in ipairs(refillConfig) do
        local container = g_game.getContainer(config.containerId)
        if container then
            local items = container:getItems()
            local currentCount = 0
            
            -- Contar itens no container
            for _, item in ipairs(items) do
                if item:getId() == config.itemId then
                    currentCount = currentCount + item:getCount()
                end
            end
            
            -- Se quantidade insuficiente, tentar reabastecer
            if currentCount < config.minCount then
                local needed = config.minCount - currentCount
                local sourceItem = g_game.findPlayerItem(config.itemId, -1)
                
                if sourceItem and sourceItem:getCount() >= needed then
                    g_game.move(sourceItem, container, needed)
                    print("Reabastecendo " .. config.name .. ": +" .. needed)
                else
                    print("⚠️ Sem " .. config.name .. " para reabastecer")
                end
            end
        end
    end
end

-- Executar auto-refill a cada 5 minutos
scheduleEvent(autoRefillContainers, 300000)
```

---

## 🔍 **Sistema de Item Tracking**

### **Rastreamento de Itens Específicos**

```lua
-- Sistema de rastreamento de itens
local function setupItemTracking()
    local trackedItems = {}
    
    -- Adicionar item ao rastreamento
    local function trackItem(itemId, name, alertThreshold)
        trackedItems[itemId] = {
            name = name,
            alertThreshold = alertThreshold or 5,
            currentCount = 0
        }
    end
    
    -- Atualizar contagem de itens
    local function updateItemCount()
        local player = g_game.getLocalPlayer()
        if not player then return end
        
        for itemId, itemData in pairs(trackedItems) do
            local item = g_game.findPlayerItem(itemId, -1)
            local count = item and item:getCount() or 0
            
            if count ~= itemData.currentCount then
                itemData.currentCount = count
                
                -- Alertar se quantidade baixa
                if count <= itemData.alertThreshold then
                    print("⚠️ " .. itemData.name .. " baixo: " .. count)
                end
                
                print(itemData.name .. ": " .. count)
            end
        end
    end
    
    -- Configurar itens para rastrear
    trackItem(7618, "Health Potions", 10)
    trackItem(3155, "Haste Spells", 5)
    trackItem(3031, "Gold Coins", 100)
    trackItem(3600, "Food", 20)
    
    return {
        updateItemCount = updateItemCount,
        trackItem = trackItem
    }
end

-- Uso do sistema
local itemTracker = setupItemTracking()
scheduleEvent(itemTracker.updateItemCount, 10000) -- Atualizar a cada 10 segundos
```

### **Sistema de Alertas Inteligentes**

```lua
-- Sistema de alertas inteligentes para inventário
local function setupInventoryAlerts()
    local alerts = {
        lowHealth = {threshold = 5, message = "Health Potions baixos"},
        lowMana = {threshold = 3, message = "Mana Potions baixos"},
        lowFood = {threshold = 10, message = "Food baixo"},
        lowAmmo = {threshold = 50, message = "Ammo baixo"},
        fullCapacity = {threshold = 95, message = "Capacidade quase cheia"}
    }
    
    local function checkAlerts()
        local player = g_game.getLocalPlayer()
        if not player then return end
        
        -- Verificar health potions
        local healthPotion = g_game.findPlayerItem(7618, -1)
        local healthCount = healthPotion and healthPotion:getCount() or 0
        if healthCount <= alerts.lowHealth.threshold then
            print("🚨 " .. alerts.lowHealth.message .. ": " .. healthCount)
        end
        
        -- Verificar mana potions
        local manaPotion = g_game.findPlayerItem(7590, -1)
        local manaCount = manaPotion and manaPotion:getCount() or 0
        if manaCount <= alerts.lowMana.threshold then
            print("🚨 " .. alerts.lowMana.message .. ": " .. manaCount)
        end
        
        -- Verificar food
        local food = g_game.findPlayerItem(3600, -1)
        local foodCount = food and food:getCount() or 0
        if foodCount <= alerts.lowFood.threshold then
            print("🚨 " .. alerts.lowFood.message .. ": " .. foodCount)
        end
        
        -- Verificar capacidade
        local capacityPercent = ((player:getCapacity() - player:getFreeCapacity()) / player:getCapacity()) * 100
        if capacityPercent >= alerts.fullCapacity.threshold then
            print("🚨 " .. alerts.fullCapacity.message .. ": " .. capacityPercent .. "%")
        end
    end
    
    return checkAlerts
end

-- Uso do sistema
local inventoryAlerts = setupInventoryAlerts()
scheduleEvent(inventoryAlerts, 15000) -- Verificar a cada 15 segundos
```

---

## 🔗 **Integração com Outros Sistemas**

### **Sistema de Eventos**

```lua
-- Conectar eventos de inventário
connect(LocalPlayer, {
    onInventoryChange = function(slot, item, oldItem)
        if item then
            print("Item adicionado no slot " .. slot .. ": " .. item:getName())
        else
            print("Item removido do slot " .. slot .. ": " .. oldItem:getName())
        end
    end,
    
    onFreeCapacityChange = function(freeCapacity)
        print("Capacidade livre alterada: " .. freeCapacity .. " oz")
    end
})

connect(g_game, {
    onOpenContainer = function(containerId, item, name, capacity, hasParent, items)
        print("Container aberto: " .. name .. " (ID: " .. containerId .. ")")
    end,
    
    onCloseContainer = function(containerId)
        print("Container fechado: " .. containerId)
    end,
    
    onContainerAddItem = function(containerId, item, slot)
        print("Item adicionado ao container " .. containerId .. ": " .. item:getName())
    end
})
```

### **Sistema de UI**

```lua
-- Interface de controle de inventário
local function createInventoryControlUI()
    local window = g_ui.createWidget('MainWindow')
    window:setText('Controle de Inventário')
    window:setSize({width = 350, height = 250})
    
    -- Botão de auto-organização
    local organizeButton = g_ui.createWidget('Button', window)
    organizeButton:setText('Auto-Organizar')
    organizeButton:setPosition({x = 10, y = 10})
    organizeButton.onClick = function()
        autoOrganizeInventory()
    end
    
    -- Botão de auto-loot
    local lootButton = g_ui.createWidget('Button', window)
    lootButton:setText('Auto-Loot')
    lootButton:setPosition({x = 10, y = 40})
    lootButton.onClick = function()
        autoLoot()
    end
    
    -- Botão de gerenciamento de capacidade
    local capacityButton = g_ui.createWidget('Button', window)
    capacityButton:setText('Gerenciar Capacidade')
    capacityButton:setPosition({x = 10, y = 70})
    capacityButton.onClick = function()
        manageCapacity()
    end
    
    -- Lista de itens rastreados
    local itemList = g_ui.createWidget('TextList', window)
    itemList:setPosition({x = 10, y = 100})
    itemList:setSize({width = 330, height = 140})
    
    -- Atualizar lista de itens
    local function updateItemList()
        itemList:clearChildren()
        local player = g_game.getLocalPlayer()
        if player then
            local items = player:getInventoryItems()
            for _, item in ipairs(items) do
                local label = g_ui.createWidget('Label', itemList)
                label:setText(item:getName() .. " x" .. item:getCount())
            end
        end
    end
    
    -- Botão de atualizar lista
    local refreshButton = g_ui.createWidget('Button', window)
    refreshButton:setText('Atualizar')
    refreshButton:setPosition({x = 280, y = 10})
    refreshButton.onClick = function()
        updateItemList()
    end
    
    return window
end
```

---

## 📊 **Dependências e Relacionamentos**

### **Dependências Principais**
- **Sistema de Jogo**: APIs de gerenciamento de itens
- **Sistema de Mapas**: Posicionamento de itens no chão
- **Sistema de Eventos**: Comunicação entre componentes
- **Sistema de Protocolo**: Comunicação com servidor

### **Sistemas Dependentes**
- **Sistema de Combate**: Uso de itens de combate
- **Sistema de NPCs**: Comércio de itens
- **Sistema de Quests**: Itens de missão

---

## 🚀 **Melhores Práticas**

### **Otimização de Inventário**

1. **Use Filtros Inteligentes**: Configure filtros de loot adequadamente
2. **Monitore Capacidade**: Verifique capacidade antes de coletar itens
3. **Organize Regularmente**: Execute auto-organização periodicamente
4. **Priorize Itens**: Defina prioridades para diferentes tipos de itens

### **Padrões de Design**

```lua
-- Padrão Observer para mudanças no inventário
local InventoryObserver = {
    observers = {},
    
    addObserver = function(callback)
        table.insert(InventoryObserver.observers, callback)
    end,
    
    notify = function(event, data)
        for _, observer in ipairs(InventoryObserver.observers) do
            observer(event, data)
        end
    end
}

-- Padrão Strategy para diferentes tipos de organização
local InventoryStrategy = {
    strategies = {},
    
    addStrategy = function(name, strategy)
        InventoryStrategy.strategies[name] = strategy
    end,
    
    executeStrategy = function(name, context)
        local strategy = InventoryStrategy.strategies[name]
        if strategy then
            strategy(context)
        end
    end
}

-- Estratégias de organização
InventoryStrategy.addStrategy("byType", function(items)
    -- Organizar por tipo de item
end)

InventoryStrategy.addStrategy("byValue", function(items)
    -- Organizar por valor do item
end)

InventoryStrategy.addStrategy("byWeight", function(items)
    -- Organizar por peso do item
end)
```

---

## 📚 **Referências e Links**

### **Arquivos Relacionados**
- [[otclient_sistema_combate|Sistema de Combate]]
- [[otclient_sistema_npcs|Sistema de NPCs]]
- [[otclient_sistema_quests|Sistema de Quests]]

### **APIs Principais**
- `g_game`: API principal do sistema de jogo
- `LocalPlayer`: Classe do jogador local
- `Item`: Classe base para itens
- `Container`: Classe para containers

### **Constantes Importantes**
```lua
-- Slots de inventário
InventorySlotHead = 1
InventorySlotNeck = 2
InventorySlotBack = 3
InventorySlotBody = 4
InventorySlotRight = 5
InventorySlotLeft = 6
InventorySlotLeg = 7
InventorySlotFeet = 8
InventorySlotFinger = 9
InventorySlotAmmo = 10

-- Tipos de item
ItemTypeNone = 0
ItemTypeDepot = 1
ItemTypeMailbox = 2
ItemTypeTrashHolder = 3
ItemTypeContainer = 4
ItemTypeDoor = 5
ItemTypeMagicWall = 6
ItemTypeTeleport = 7
ItemTypeBed = 8
ItemTypeKey = 9
```

---

> [!success] **Conclusão**
> O Sistema de Inventário do OTClient fornece ferramentas completas para gerenciamento de itens, containers e automação de organização, permitindo criar sistemas sofisticados de auto-loot e gerenciamento de capacidade.

---

**📖 Próximo**: [[otclient_sistema_npcs|Sistema de NPCs]] | **🔙 Anterior**: [[otclient_sistema_combate|Sistema de Combate]] 