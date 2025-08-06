---
tags: [integration, data_sync, synchronization, otclient, canary, wiki, canary_otclient]
type: wiki_page
status: active
priority: high
created: 2025-08-05
updated: 2025-08-05
aliases: [Sincronização Dados, Sync Dados, Data Sync, Sincronização Cliente Servidor]
---

# 🔄 **Sincronização de Dados - OTClient vs Canary**

> [!info] **Baseado na Pesquisa Habdel**
> Esta página é baseada na pesquisa detalhada da **[INTEGRATION-005: Comparação de Funcionalidades](../../habdel/INTEGRATION-005.md)** realizada pelo sistema Habdel.

---

## 🎯 **Visão Geral**

A **Sincronização de Dados** entre OTClient e Canary é um sistema crítico que garante a consistência e integridade dos dados entre cliente e servidor. Este sistema gerencia a sincronização de estados de jogo, inventários, posições, status e outras informações essenciais para o funcionamento do MMORPG.

### **Características Principais**
- **Sincronização em tempo real** de estados de jogo
- **Consistência de dados** entre cliente e servidor
- **Resolução de conflitos** automática
- **Otimização de tráfego** de rede
- **Recuperação de erros** robusta

---

## 🔄 **Tipos de Sincronização**

### **📊 Sincronização de Estados**

#### **Estados do Jogador**
```lua
-- Estados do jogador que precisam ser sincronizados
local PlayerStates = {
    -- Informações básicas
    BASIC_INFO = {
        id = "uint32",
        name = "string",
        level = "uint32",
        experience = "uint32",
        health = "uint32",
        maxHealth = "uint32",
        mana = "uint32",
        maxMana = "uint32"
    },
    
    -- Posição e movimento
    POSITION = {
        x = "uint16",
        y = "uint16",
        z = "uint8",
        direction = "uint8"
    },
    
    -- Status e condições
    STATUS = {
        conditions = "array",
        skills = "array",
        stats = "array"
    },
    
    -- Inventário
    INVENTORY = {
        items = "array",
        capacity = "uint32",
        weight = "uint32"
    },
    
    -- Equipamento
    EQUIPMENT = {
        head = "uint16",
        neck = "uint16",
        body = "uint16",
        legs = "uint16",
        feet = "uint16",
        shield = "uint16",
        weapon = "uint16"
    }
}
```

#### **Estados do Mundo**
```lua
-- Estados do mundo que precisam ser sincronizados
local WorldStates = {
    -- Mapa e tiles
    MAP = {
        tiles = "array",
        creatures = "array",
        items = "array"
    },
    
    -- Criaturas
    CREATURES = {
        id = "uint32",
        type = "uint16",
        position = "position",
        health = "uint32",
        direction = "uint8"
    },
    
    -- Itens no mundo
    ITEMS = {
        id = "uint32",
        type = "uint16",
        position = "position",
        count = "uint32"
    },
    
    -- Efeitos visuais
    EFFECTS = {
        id = "uint32",
        type = "uint16",
        position = "position",
        duration = "uint32"
    }
}
```

---

## 🏗️ **Implementação do Sistema de Sincronização**

### **📡 Sistema de Sincronização - OTClient**
```lua
-- Sistema de sincronização no OTClient
local DataSyncSystem = {}

function DataSyncSystem:init()
    self.syncQueue = {}
    self.lastSyncTime = 0
    self.syncInterval = 100 -- 100ms
    self.pendingUpdates = {}
    self.conflictResolution = {}
    self.syncEnabled = true
end

function DataSyncSystem:setupSyncTypes()
    -- Configurar tipos de sincronização
    self.syncTypes = {
        IMMEDIATE = 1,    -- Sincronização imediata
        PERIODIC = 2,     -- Sincronização periódica
        ON_DEMAND = 3,    -- Sincronização sob demanda
        BATCH = 4         -- Sincronização em lote
    }
    
    -- Configurar prioridades
    self.priorities = {
        CRITICAL = 1,     -- Posição, vida, morte
        HIGH = 2,         -- Inventário, equipamento
        MEDIUM = 3,       -- Status, condições
        LOW = 4           -- Efeitos visuais, animações
        BATCH = 5         -- Dados em lote
    }
end

function DataSyncSystem:queueSync(dataType, data, priority, syncType)
    local syncItem = {
        type = dataType,
        data = data,
        priority = priority or self.priorities.MEDIUM,
        syncType = syncType or self.syncTypes.PERIODIC,
        timestamp = os.time(),
        sequence = self:getNextSequence()
    }
    
    -- Adicionar à fila de sincronização
    table.insert(self.syncQueue, syncItem)
    
    -- Ordenar por prioridade
    table.sort(self.syncQueue, function(a, b)
        return a.priority < b.priority
    end)
    
    -- Processar sincronização imediata se necessário
    if syncType == self.syncTypes.IMMEDIATE then
        self:processImmediateSync(syncItem)
    end
end

function DataSyncSystem:processSync()
    if not self.syncEnabled then
        return
    end
    
    local currentTime = os.time()
    if currentTime - self.lastSyncTime < self.syncInterval then
        return
    end
    
    -- Processar itens da fila
    local itemsToSync = {}
    local remainingItems = {}
    
    for _, item in ipairs(self.syncQueue) do
        if self:shouldSyncNow(item) then
            table.insert(itemsToSync, item)
        else
            table.insert(remainingItems, item)
        end
    end
    
    -- Atualizar fila
    self.syncQueue = remainingItems
    
    -- Enviar dados para sincronização
    if #itemsToSync > 0 then
        self:sendSyncData(itemsToSync)
    end
    
    self.lastSyncTime = currentTime
end

function DataSyncSystem:shouldSyncNow(item)
    local currentTime = os.time()
    
    if item.syncType == self.syncTypes.IMMEDIATE then
        return true
    elseif item.syncType == self.syncTypes.PERIODIC then
        return currentTime - item.timestamp >= self.syncInterval
    elseif item.syncType == self.syncTypes.ON_DEMAND then
        return self:hasChanged(item)
    elseif item.syncType == self.syncTypes.BATCH then
        return #self.syncQueue >= 10 -- Batch de 10 itens
    end
    
    return false
end

function DataSyncSystem:sendSyncData(items)
    -- Agrupar itens por tipo
    local groupedData = self:groupSyncData(items)
    
    -- Enviar dados agrupados
    for dataType, data in pairs(groupedData) do
        self:sendSyncMessage(dataType, data)
    end
end

function DataSyncSystem:groupSyncData(items)
    local grouped = {}
    
    for _, item in ipairs(items) do
        if not grouped[item.type] then
            grouped[item.type] = {}
        end
        table.insert(grouped[item.type], item.data)
    end
    
    return grouped
end

function DataSyncSystem:sendSyncMessage(dataType, data)
    local syncMessage = {
        type = "data_sync",
        dataType = dataType,
        data = data,
        timestamp = os.time(),
        clientId = g_game:getPlayerId()
    }
    
    -- Enviar via protocolo
    if g_network then
        g_network:sendMessage(syncMessage)
    end
end

function DataSyncSystem:handleSyncResponse(response)
    -- Processar resposta de sincronização
    if response.success then
        -- Aplicar dados sincronizados
        self:applySyncData(response.data)
        
        -- Limpar conflitos resolvidos
        self:clearResolvedConflicts(response.resolvedConflicts)
    else
        -- Tratar erro de sincronização
        self:handleSyncError(response.error)
    end
end

function DataSyncSystem:applySyncData(data)
    for dataType, syncData in pairs(data) do
        if dataType == "player_state" then
            self:applyPlayerState(syncData)
        elseif dataType == "world_state" then
            self:applyWorldState(syncData)
        elseif dataType == "inventory" then
            self:applyInventory(syncData)
        elseif dataType == "equipment" then
            self:applyEquipment(syncData)
        end
    end
end

function DataSyncSystem:applyPlayerState(data)
    local player = g_game:getPlayer()
    if player then
        -- Aplicar mudanças de estado
        if data.position then
            player:setPosition(data.position)
        end
        
        if data.health then
            player:setHealth(data.health)
        end
        
        if data.mana then
            player:setMana(data.mana)
        end
        
        -- Atualizar UI
        g_ui:updatePlayerDisplay(player)
    end
end

function DataSyncSystem:applyWorldState(data)
    if data.creatures then
        for _, creatureData in ipairs(data.creatures) do
            g_map:updateCreature(creatureData)
        end
    end
    
    if data.items then
        for _, itemData in ipairs(data.items) do
            g_map:updateItem(itemData)
        end
    end
end

function DataSyncSystem:applyInventory(data)
    local inventory = g_game:getInventory()
    if inventory then
        inventory:updateFromSync(data)
        g_ui:updateInventoryDisplay(inventory)
    end
end

function DataSyncSystem:applyEquipment(data)
    local equipment = g_game:getEquipment()
    if equipment then
        equipment:updateFromSync(data)
        g_ui:updateEquipmentDisplay(equipment)
    end
end

function DataSyncSystem:handleSyncError(error)
    print("Sync error: " .. error.message)
    
    -- Implementar estratégias de recuperação
    if error.type == "conflict" then
        self:resolveConflict(error.conflict)
    elseif error.type == "network" then
        self:retrySync(error.data)
    elseif error.type == "validation" then
        self:validateAndFix(error.data)
    end
end

function DataSyncSystem:resolveConflict(conflict)
    -- Implementar resolução de conflitos
    local resolution = self.conflictResolution[conflict.type]
    if resolution then
        resolution(conflict)
    else
        -- Resolução padrão: usar dados do servidor
        self:acceptServerData(conflict.serverData)
    end
end

function DataSyncSystem:retrySync(data)
    -- Reenviar dados após erro de rede
    scheduleEvent(function()
        self:queueSync(data.type, data.data, data.priority, self.syncTypes.IMMEDIATE)
    end, 1000) -- Tentar novamente em 1 segundo
end

function DataSyncSystem:validateAndFix(data)
    -- Validar e corrigir dados inválidos
    local validator = self:getValidator(data.type)
    if validator then
        local fixedData = validator:fix(data.data)
        self:queueSync(data.type, fixedData, data.priority, self.syncTypes.IMMEDIATE)
    end
end

-- Exemplo de uso
DataSyncSystem:queueSync("player_position", {
    x = 100,
    y = 200,
    z = 7,
    direction = 0
}, DataSyncSystem.priorities.CRITICAL, DataSyncSystem.syncTypes.IMMEDIATE)

DataSyncSystem:queueSync("inventory", {
    items = {{id = 1, count = 10}, {id = 2, count = 5}}
}, DataSyncSystem.priorities.HIGH, DataSyncSystem.syncTypes.PERIODIC)
```

### **📡 Sistema de Sincronização - Canary**
```cpp
// Sistema de sincronização no Canary
class DataSyncSystem {
private:
    std::map<uint32_t, std::vector<SyncItem>> syncQueues;
    std::map<uint32_t, PlayerState> playerStates;
    std::map<uint32_t, WorldState> worldStates;
    std::chrono::steady_clock::time_point lastSyncTime;
    std::chrono::milliseconds syncInterval;
    bool syncEnabled;
    
public:
    DataSyncSystem() : syncInterval(100ms), syncEnabled(true) {
        setupSyncTypes();
        setupPriorities();
    }
    
    void setupSyncTypes() {
        syncTypes = {
            {"IMMEDIATE", 1},
            {"PERIODIC", 2},
            {"ON_DEMAND", 3},
            {"BATCH", 4}
        };
    }
    
    void setupPriorities() {
        priorities = {
            {"CRITICAL", 1},
            {"HIGH", 2},
            {"MEDIUM", 3},
            {"LOW", 4},
            {"BATCH", 5}
        };
    }
    
    void queueSync(uint32_t playerId, const std::string& dataType, const SyncData& data, 
                   int priority, int syncType) {
        SyncItem item;
        item.type = dataType;
        item.data = data;
        item.priority = priority;
        item.syncType = syncType;
        item.timestamp = std::chrono::steady_clock::now();
        item.sequence = getNextSequence();
        
        // Adicionar à fila do jogador
        syncQueues[playerId].push_back(item);
        
        // Ordenar por prioridade
        std::sort(syncQueues[playerId].begin(), syncQueues[playerId].end(),
                  [](const SyncItem& a, const SyncItem& b) {
                      return a.priority < b.priority;
                  });
        
        // Processar sincronização imediata se necessário
        if (syncType == 1) { // IMMEDIATE
            processImmediateSync(playerId, item);
        }
    }
    
    void processSync() {
        if (!syncEnabled) {
            return;
        }
        
        auto currentTime = std::chrono::steady_clock::now();
        if (currentTime - lastSyncTime < syncInterval) {
            return;
        }
        
        // Processar filas de todos os jogadores
        for (auto& [playerId, queue] : syncQueues) {
            processPlayerSync(playerId, queue);
        }
        
        lastSyncTime = currentTime;
    }
    
    void processPlayerSync(uint32_t playerId, std::vector<SyncItem>& queue) {
        std::vector<SyncItem> itemsToSync;
        std::vector<SyncItem> remainingItems;
        
        for (const auto& item : queue) {
            if (shouldSyncNow(item)) {
                itemsToSync.push_back(item);
            } else {
                remainingItems.push_back(item);
            }
        }
        
        // Atualizar fila
        queue = remainingItems;
        
        // Enviar dados para sincronização
        if (!itemsToSync.empty()) {
            sendSyncData(playerId, itemsToSync);
        }
    }
    
    bool shouldSyncNow(const SyncItem& item) {
        auto currentTime = std::chrono::steady_clock::now();
        auto elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(
            currentTime - item.timestamp);
        
        if (item.syncType == 1) { // IMMEDIATE
            return true;
        } else if (item.syncType == 2) { // PERIODIC
            return elapsed >= syncInterval;
        } else if (item.syncType == 3) { // ON_DEMAND
            return hasChanged(item);
        } else if (item.syncType == 4) { // BATCH
            return syncQueues.size() >= 10;
        }
        
        return false;
    }
    
    void sendSyncData(uint32_t playerId, const std::vector<SyncItem>& items) {
        // Agrupar itens por tipo
        auto groupedData = groupSyncData(items);
        
        // Enviar dados agrupados
        for (const auto& [dataType, data] : groupedData) {
            sendSyncMessage(playerId, dataType, data);
        }
    }
    
    std::map<std::string, std::vector<SyncData>> groupSyncData(const std::vector<SyncItem>& items) {
        std::map<std::string, std::vector<SyncData>> grouped;
        
        for (const auto& item : items) {
            grouped[item.type].push_back(item.data);
        }
        
        return grouped;
    }
    
    void sendSyncMessage(uint32_t playerId, const std::string& dataType, 
                        const std::vector<SyncData>& data) {
        NetworkMessage message;
        message.addU8(0x90); // SYNC_DATA
        message.addU32(playerId);
        message.addString(dataType);
        message.addSyncData(data);
        
        // Enviar para o jogador
        auto player = g_players->getPlayer(playerId);
        if (player) {
            player->sendMessage(message);
        }
    }
    
    void handleSyncRequest(const NetworkMessage& message) {
        uint32_t playerId = message.getU32();
        std::string dataType = message.getString();
        SyncData data = message.getSyncData();
        
        // Processar solicitação de sincronização
        if (dataType == "player_state") {
            handlePlayerStateSync(playerId, data);
        } else if (dataType == "world_state") {
            handleWorldStateSync(playerId, data);
        } else if (dataType == "inventory") {
            handleInventorySync(playerId, data);
        } else if (dataType == "equipment") {
            handleEquipmentSync(playerId, data);
        }
    }
    
    void handlePlayerStateSync(uint32_t playerId, const SyncData& data) {
        auto player = g_players->getPlayer(playerId);
        if (!player) {
            return;
        }
        
        // Validar dados
        if (!validatePlayerState(data)) {
            sendSyncError(playerId, "Invalid player state data");
            return;
        }
        
        // Aplicar mudanças
        if (data.contains("position")) {
            Position pos = data.getPosition("position");
            if (g_map->canMoveTo(player, pos)) {
                player->setPosition(pos);
            }
        }
        
        if (data.contains("health")) {
            uint32_t health = data.getU32("health");
            player->setHealth(health);
        }
        
        if (data.contains("mana")) {
            uint32_t mana = data.getU32("mana");
            player->setMana(mana);
        }
        
        // Confirmar sincronização
        sendSyncConfirmation(playerId, "player_state");
    }
    
    void handleWorldStateSync(uint32_t playerId, const SyncData& data) {
        // Sincronizar estado do mundo
        if (data.contains("creatures")) {
            auto creatures = data.getArray("creatures");
            for (const auto& creatureData : creatures) {
                g_map->updateCreature(creatureData);
            }
        }
        
        if (data.contains("items")) {
            auto items = data.getArray("items");
            for (const auto& itemData : items) {
                g_map->updateItem(itemData);
            }
        }
        
        // Confirmar sincronização
        sendSyncConfirmation(playerId, "world_state");
    }
    
    void handleInventorySync(uint32_t playerId, const SyncData& data) {
        auto player = g_players->getPlayer(playerId);
        if (!player) {
            return;
        }
        
        // Validar inventário
        if (!validateInventory(data)) {
            sendSyncError(playerId, "Invalid inventory data");
            return;
        }
        
        // Aplicar mudanças no inventário
        auto inventory = player->getInventory();
        inventory->updateFromSync(data);
        
        // Confirmar sincronização
        sendSyncConfirmation(playerId, "inventory");
    }
    
    void handleEquipmentSync(uint32_t playerId, const SyncData& data) {
        auto player = g_players->getPlayer(playerId);
        if (!player) {
            return;
        }
        
        // Validar equipamento
        if (!validateEquipment(data)) {
            sendSyncError(playerId, "Invalid equipment data");
            return;
        }
        
        // Aplicar mudanças no equipamento
        auto equipment = player->getEquipment();
        equipment->updateFromSync(data);
        
        // Confirmar sincronização
        sendSyncConfirmation(playerId, "equipment");
    }
    
    void sendSyncConfirmation(uint32_t playerId, const std::string& dataType) {
        NetworkMessage message;
        message.addU8(0x91); // SYNC_CONFIRMATION
        message.addU32(playerId);
        message.addString(dataType);
        message.addU8(1); // Success
        
        auto player = g_players->getPlayer(playerId);
        if (player) {
            player->sendMessage(message);
        }
    }
    
    void sendSyncError(uint32_t playerId, const std::string& error) {
        NetworkMessage message;
        message.addU8(0x92); // SYNC_ERROR
        message.addU32(playerId);
        message.addString(error);
        
        auto player = g_players->getPlayer(playerId);
        if (player) {
            player->sendMessage(message);
        }
    }
    
    bool validatePlayerState(const SyncData& data) {
        // Validar dados do estado do jogador
        if (data.contains("position")) {
            Position pos = data.getPosition("position");
            if (pos.x > 65535 || pos.y > 65535 || pos.z > 255) {
                return false;
            }
        }
        
        if (data.contains("health")) {
            uint32_t health = data.getU32("health");
            uint32_t maxHealth = data.getU32("maxHealth");
            if (health > maxHealth) {
                return false;
            }
        }
        
        return true;
    }
    
    bool validateInventory(const SyncData& data) {
        // Validar dados do inventário
        if (data.contains("items")) {
            auto items = data.getArray("items");
            for (const auto& item : items) {
                if (!validateItem(item)) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
    bool validateEquipment(const SyncData& data) {
        // Validar dados do equipamento
        std::vector<std::string> slots = {"head", "neck", "body", "legs", "feet", "shield", "weapon"};
        
        for (const auto& slot : slots) {
            if (data.contains(slot)) {
                uint16_t itemId = data.getU16(slot);
                if (!g_items->isValidEquipment(slot, itemId)) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
    bool validateItem(const ItemData& item) {
        // Validar dados do item
        if (item.id == 0 || item.id > 65535) {
            return false;
        }
        
        if (item.count == 0 || item.count > 100) {
            return false;
        }
        
        return g_items->isValidItem(item.id);
    }
    
    bool hasChanged(const SyncItem& item) {
        // Verificar se os dados mudaram desde a última sincronização
        // Implementação específica baseada no tipo de dados
        return true; // Simplificado
    }
    
    uint32_t getNextSequence() {
        static uint32_t sequence = 0;
        return ++sequence;
    }
};
```

---

## 🛠️ **Exemplos Práticos**

### **Exemplo 1: Sincronização de Posição**
```lua
-- Exemplo: Sincronização de posição do jogador
local PositionSync = {}

function PositionSync:init()
    self.syncSystem = DataSyncSystem:new()
    self.syncSystem:init()
    self.lastPosition = nil
end

function PositionSync:updatePosition(x, y, z, direction)
    local newPosition = {x = x, y = y, z = z, direction = direction}
    
    -- Verificar se a posição mudou
    if not self:positionChanged(newPosition) then
        return
    end
    
    -- Enfileirar sincronização
    self.syncSystem:queueSync(
        "player_position",
        newPosition,
        DataSyncSystem.priorities.CRITICAL,
        DataSyncSystem.syncTypes.IMMEDIATE
    )
    
    self.lastPosition = newPosition
end

function PositionSync:positionChanged(newPosition)
    if not self.lastPosition then
        return true
    end
    
    return newPosition.x ~= self.lastPosition.x or
           newPosition.y ~= self.lastPosition.y or
           newPosition.z ~= self.lastPosition.z or
           newPosition.direction ~= self.lastPosition.direction
end

function PositionSync:handlePositionSync(data)
    -- Aplicar posição sincronizada
    local player = g_game:getPlayer()
    if player then
        player:setPosition(data)
        g_map:updatePlayerPosition(data)
    end
end
```

### **Exemplo 2: Sincronização de Inventário**
```lua
-- Exemplo: Sincronização de inventário
local InventorySync = {}

function InventorySync:init()
    self.syncSystem = DataSyncSystem:new()
    self.syncSystem:init()
    self.lastInventory = {}
end

function InventorySync:updateInventory(inventory)
    local inventoryData = self:serializeInventory(inventory)
    
    -- Verificar se o inventário mudou
    if not self:inventoryChanged(inventoryData) then
        return
    end
    
    -- Enfileirar sincronização
    self.syncSystem:queueSync(
        "inventory",
        inventoryData,
        DataSyncSystem.priorities.HIGH,
        DataSyncSystem.syncTypes.PERIODIC
    )
    
    self.lastInventory = inventoryData
end

function InventorySync:serializeInventory(inventory)
    local data = {
        items = {},
        capacity = inventory:getCapacity(),
        weight = inventory:getWeight()
    }
    
    for i = 1, inventory:getSize() do
        local item = inventory:getItem(i)
        if item then
            table.insert(data.items, {
                id = item:getId(),
                count = item:getCount(),
                slot = i
            })
        end
    end
    
    return data
end

function InventorySync:inventoryChanged(newInventory)
    if #newInventory.items ~= #self.lastInventory.items then
        return true
    end
    
    for i, item in ipairs(newInventory.items) do
        local lastItem = self.lastInventory.items[i]
        if not lastItem or item.id ~= lastItem.id or item.count ~= lastItem.count then
            return true
        end
    end
    
    return false
end

function InventorySync:handleInventorySync(data)
    -- Aplicar inventário sincronizado
    local inventory = g_game:getInventory()
    if inventory then
        inventory:clear()
        
        for _, itemData in ipairs(data.items) do
            local item = g_items:createItem(itemData.id, itemData.count)
            if item then
                inventory:addItem(itemData.slot, item)
            end
        end
        
        g_ui:updateInventoryDisplay(inventory)
    end
end
```

### **Exemplo 3: Sincronização de Estado do Mundo**
```lua
-- Exemplo: Sincronização de estado do mundo
local WorldSync = {}

function WorldSync:init()
    self.syncSystem = DataSyncSystem:new()
    self.syncSystem:init()
    self.lastWorldState = {}
end

function WorldSync:updateWorldState(worldState)
    local worldData = self:serializeWorldState(worldState)
    
    -- Enfileirar sincronização
    self.syncSystem:queueSync(
        "world_state",
        worldData,
        DataSyncSystem.priorities.MEDIUM,
        DataSyncSystem.syncTypes.BATCH
    )
end

function WorldSync:serializeWorldState(worldState)
    local data = {
        creatures = {},
        items = {},
        effects = {}
    }
    
    -- Serializar criaturas
    for _, creature in ipairs(worldState.creatures) do
        table.insert(data.creatures, {
            id = creature:getId(),
            type = creature:getType(),
            position = creature:getPosition(),
            health = creature:getHealth(),
            direction = creature:getDirection()
        })
    end
    
    -- Serializar itens
    for _, item in ipairs(worldState.items) do
        table.insert(data.items, {
            id = item:getId(),
            type = item:getType(),
            position = item:getPosition(),
            count = item:getCount()
        })
    end
    
    -- Serializar efeitos
    for _, effect in ipairs(worldState.effects) do
        table.insert(data.effects, {
            id = effect:getId(),
            type = effect:getType(),
            position = effect:getPosition(),
            duration = effect:getDuration()
        })
    end
    
    return data
end

function WorldSync:handleWorldSync(data)
    -- Aplicar estado do mundo sincronizado
    if data.creatures then
        for _, creatureData in ipairs(data.creatures) do
            g_map:updateCreature(creatureData)
        end
    end
    
    if data.items then
        for _, itemData in ipairs(data.items) do
            g_map:updateItem(itemData)
        end
    end
    
    if data.effects then
        for _, effectData in ipairs(data.effects) do
            g_map:updateEffect(effectData)
        end
    end
end
```

---

## 🔗 **Dependências e Integração**

### **Dependências Internas**
- **[[integracao_protocolo_comunicacao|Protocolo de Comunicação]]** - Sistema de comunicação
- **[[integracao_open_codes|Open Codes]]** - Protocolo básico
- **[[integracao_extended_open_codes|Extended Open Codes]]** - Protocolo avançado

### **Dependências Externas**
- **TCP/IP** - Protocolo de transporte
- **Lua 5.1+** - Linguagem de scripting
- **C++** - Linguagem de implementação

### **Integração com Outros Sistemas**
```lua
-- Exemplo: Integração com sistema de rede
local NetworkSystem = require("modules/network_system")
local DataSyncSystem = require("modules/data_sync_system")

-- Configurar sincronização
DataSyncSystem:setNetworkSystem(NetworkSystem)
DataSyncSystem:setupSyncTypes()
DataSyncSystem:setupPriorities()

-- Iniciar sistema
DataSyncSystem:start()
```

---

## 📚 **Referência de API**

### **Funções Principais**

#### **Sync Management**
- `DataSyncSystem:queueSync(type, data, priority, syncType)` - Enfileira sincronização
- `DataSyncSystem:processSync()` - Processa sincronização
- `DataSyncSystem:handleSyncResponse(response)` - Processa resposta

#### **Data Validation**
- `DataSyncSystem:validateData(data)` - Valida dados
- `DataSyncSystem:resolveConflict(conflict)` - Resolve conflitos
- `DataSyncSystem:retrySync(data)` - Reenvia sincronização

---

## 🎯 **Melhores Práticas**

### **1. Priorização**
```lua
-- ✅ Bom: Usar prioridades apropriadas
DataSyncSystem:queueSync("position", data, DataSyncSystem.priorities.CRITICAL)
DataSyncSystem:queueSync("inventory", data, DataSyncSystem.priorities.HIGH)

-- ❌ Ruim: Usar prioridades incorretas
DataSyncSystem:queueSync("position", data, DataSyncSystem.priorities.LOW)
```

### **2. Validação**
```lua
-- ✅ Bom: Validar dados antes de sincronizar
if DataSyncSystem:validateData(data) then
    DataSyncSystem:queueSync(type, data, priority)
else
    print("Invalid data, skipping sync")
end

-- ❌ Ruim: Sincronizar sem validação
DataSyncSystem:queueSync(type, data, priority) -- Sem validação
```

### **3. Tratamento de Erros**
```lua
-- ✅ Bom: Tratar erros de sincronização
DataSyncSystem:handleSyncError = function(error)
    if error.type == "conflict" then
        DataSyncSystem:resolveConflict(error.conflict)
    elseif error.type == "network" then
        DataSyncSystem:retrySync(error.data)
    end
end

-- ❌ Ruim: Ignorar erros
DataSyncSystem:handleSyncError = function(error)
    print("Sync error: " .. error.message) -- Sem tratamento
end
```

---

## 🔍 **Debugging e Troubleshooting**

### **Debug de Sincronização**
```lua
-- Função para debug de sincronização
function DataSyncSystem:debugSync()
    print("=== Data Sync Debug ===")
    print("Queue Size: " .. #self.syncQueue)
    print("Last Sync: " .. self.lastSyncTime)
    print("Sync Enabled: " .. tostring(self.syncEnabled))
    
    for i, item in ipairs(self.syncQueue) do
        print("  Item " .. i .. ": " .. item.type .. " (Priority: " .. item.priority .. ")")
    end
end
```

### **Debug de Conflitos**
```lua
-- Função para debug de conflitos
function DataSyncSystem:debugConflicts()
    print("=== Conflict Debug ===")
    print("Pending Conflicts: " .. #self.pendingConflicts)
    
    for _, conflict in ipairs(self.pendingConflicts) do
        print("  Conflict: " .. conflict.type .. " - " .. conflict.description)
    end
end
```

---

## 📖 **Recursos Adicionais**

### **Documentação Relacionada**
- **[[integracao_protocolo_comunicacao|Protocolo de Comunicação]]** - Sistema de comunicação
- **[[integracao_open_codes|Open Codes]]** - Protocolo básico
- **[[integracao_extended_open_codes|Extended Open Codes]]** - Protocolo avançado

### **Exemplos de Código**
- **[[integracao_exemplos_sync|Exemplos de Sincronização]]** - Exemplos práticos
- **[[integracao_implementacao_sync|Implementação de Sync]]** - Implementações

### **Ferramentas de Desenvolvimento**
- **[[integracao_ferramentas_sync|Ferramentas de Sync]]** - Ferramentas para desenvolvimento
- **[[integracao_debug_sync|Debug de Sync]]** - Ferramentas de debug

---

## 🎯 **Próximos Passos**

1. **Configure Sync** - Configure o sistema de sincronização
2. **Implemente Validação** - Implemente validação de dados
3. **Teste Sincronização** - Teste a sincronização de dados
4. **Otimize Performance** - Otimize para melhor performance
5. **Monitore Conflitos** - Monitore e resolva conflitos

---

> [!success] **Conclusão**
> O sistema de sincronização de dados entre OTClient e Canary garante a consistência e integridade dos dados, fornecendo uma base robusta para o funcionamento do MMORPG. 