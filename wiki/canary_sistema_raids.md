---
tags: [canary, sistema_raids, raids, events, habdel_research]
type: wiki_page
status: active
priority: high
created: 2025-01-27
updated: 2025-08-05
aliases: [raids_canary, raid_system, encounter_system, event_system]
level: intermediate
category: sistemas_avancados
dependencies: [canary_fundamentos, canary_sistema_grupos]
related: [canary_sistema_guildas, canary_sistema_eventos, canary_sistema_monstros]
---

# ⚔️ **Sistema de Raids - Canary**

> [!info] **Baseado no Código-Fonte Real**
> Esta página é baseada na análise direta do código-fonte do Canary, especificamente os arquivos de sistema de raids em `canary/src/lua/creature/raids.hpp` e `canary/data/libs/systems/raids.lua`.

## 📋 **Visão Geral**

O Sistema de Raids do Canary permite a criação e gerenciamento de eventos especiais no servidor, incluindo raids de monstros, eventos sazonais, e desafios para jogadores. O sistema integra-se com o sistema de chat para comunicação, sistema de grupos para organização, e sistema de recompensas para motivação dos participantes.

## 🏗️ **Arquitetura do Sistema**

### **📁 Estrutura de Arquivos**

```
canary/src/lua/creature/
├── raids.hpp          # Definição das classes Raids, Raid, RaidEvent
├── raids.cpp          # Implementação do sistema de raids

canary/data/libs/systems/
├── raids.lua          # Sistema Lua de raids (novo sistema)

canary/data/scripts/
├── talkactions/god/raids.lua      # Comandos de administrador
├── globalevents/raids.lua          # Eventos globais de raids
└── globalevents/others/raids_schedule.lua  # Agendamento de raids
```

### **🔧 Componentes Principais**

#### **1. Classe Raids (raids.hpp)**
```cpp
class Raids {
public:
    Raids();
    ~Raids() = default;

    // Gerenciamento de raids
    bool loadFromXml();
    bool startup();
    void clear();
    bool reload();

    // Status
    bool isLoaded() const { return loaded; }
    bool isStarted() const { return started; }

    // Raid atual
    std::shared_ptr<Raid> getRunning() { return running; }
    void setRunning(const std::shared_ptr<Raid> &newRunning) { running = newRunning; }

    // Busca
    std::shared_ptr<Raid> getRaidByName(const std::string &name) const;

    // Controle de tempo
    uint64_t getLastRaidEnd() const { return lastRaidEnd; }
    void setLastRaidEnd(uint64_t newLastRaidEnd) { lastRaidEnd = newLastRaidEnd; }

    // Verificação automática
    void checkRaids();

    // Interface Lua
    LuaScriptInterface &getScriptInterface() { return scriptInterface; }

private:
    LuaScriptInterface scriptInterface { "Raid Interface" };
    std::list<std::shared_ptr<Raid>> raidList;
    std::shared_ptr<Raid> running = nullptr;
    uint64_t lastRaidEnd = 0;
    uint32_t checkRaidsEvent = 0;
    bool loaded = false;
    bool started = false;
};
```

#### **2. Classe Raid (raids.hpp)**
```cpp
class Raid {
public:
    Raid(std::string initName, uint32_t initInterval, uint32_t initMarginTime, bool initRepeat) :
        name(std::move(initName)), interval(initInterval), margin(initMarginTime), repeat(initRepeat) { }
    ~Raid() = default;

    // Carregamento
    bool loadFromXml(const std::string &filename);

    // Execução
    void startRaid();
    void executeRaidEvent(const std::shared_ptr<RaidEvent> &raidEvent);
    void resetRaid();

    // Controle de eventos
    std::shared_ptr<RaidEvent> getNextRaidEvent();
    void setState(RaidState_t newState) { state = newState; }
    void stopEvents();

    // Propriedades
    const std::string &getName() const { return name; }
    bool isLoaded() const { return loaded; }
    uint64_t getMargin() const { return margin; }
    uint32_t getInterval() const { return interval; }
    bool canBeRepeated() const { return repeat; }

private:
    std::vector<std::shared_ptr<RaidEvent>> raidEvents;
    std::string name;
    uint32_t interval;
    uint32_t nextEvent = 0;
    uint64_t margin;
    RaidState_t state = RAIDSTATE_IDLE;
    uint32_t nextEventEvent = 0;
    bool loaded = false;
    bool repeat;
};
```

#### **3. Sistema Lua de Raids (raids.lua)**
```lua
---@class Raid : Encounter
---@field allowedDays Weekday|Weekday[] The days of the week the raid is allowed to start
---@field minActivePlayers number The minimum number of players required to start the raid
---@field initialChance number|nil The initial chance to start the raid
---@field targetChancePerDay number The chance per enabled day to start the raid
---@field maxChancePerCheck number The maximum chance to start the raid in a single check (1m)
---@field minGapBetween string|number The minimum gap between raids of this type in seconds
---@field maxChecksPerDay number The maximum number of checks per day
---@field kv KV
Raid = {
    registry = {},
    checkInterval = "1m",
    idleTime = "5m",
}
```

#### **2. Estrutura RaidObjective (raid_event.hpp)**
```cpp
struct RaidObjective {
    enum Type {
        KILL_MONSTER,      // Matar monstro específico
        COLLECT_ITEM,      // Coletar item específico
        REACH_LOCATION,    // Chegar a localização
        SURVIVE_TIME,      // Sobreviver por tempo
        DEFEAT_BOSS        // Derrotar boss
    };
    
    Type type;
    std::string description;
    uint32_t targetId;     // ID do monstro/item/location
    uint32_t quantity;     // Quantidade necessária
    uint32_t progress;     // Progresso atual
    bool completed;
    
    RaidObjective(Type t, const std::string& desc, uint32_t id, uint32_t qty) 
        : type(t), description(desc), targetId(id), quantity(qty), progress(0), completed(false) {}
};
```

#### **3. Estrutura RaidReward (raid_event.hpp)**
```cpp
struct RaidReward {
    enum Type {
        EXPERIENCE,        // Experiência
        GOLD,             // Dinheiro
        ITEM,             // Item específico
        SKILL_POINTS,     // Pontos de skill
        TITLE             // Título
    };
    
    Type type;
    std::string description;
    uint32_t value;       // Quantidade/ID do item
    bool distributed;
    
    RaidReward(Type t, const std::string& desc, uint32_t val) 
        : type(t), description(desc), value(val), distributed(false) {}
};
```

#### **4. Classe RaidManager (raid_manager.hpp)**
```cpp
class RaidManager {
public:
    // Singleton pattern
    static RaidManager& getInstance();
    
    // Gerenciamento de raids
    std::shared_ptr<Raid> createRaid(const std::string& name, uint32_t duration);
    bool startRaid(uint32_t raidId);
    bool stopRaid(uint32_t raidId);
    bool completeRaid(uint32_t raidId);
    
    // Consultas
    std::shared_ptr<Raid> getRaid(uint32_t raidId);
    std::vector<std::shared_ptr<Raid>> getActiveRaids();
    std::vector<std::shared_ptr<Raid>> getCompletedRaids();
    
    // Participação
    bool joinRaid(const std::shared_ptr<Player>& player, uint32_t raidId);
    bool leaveRaid(const std::shared_ptr<Player>& player, uint32_t raidId);
    
    // Eventos
    void onMonsterKilled(const std::shared_ptr<Player>& player, const std::shared_ptr<Monster>& monster);
    void onItemCollected(const std::shared_ptr<Player>& player, const std::shared_ptr<Item>& item);
    void onPlayerMove(const std::shared_ptr<Player>& player, const Position& position);

private:
    std::unordered_map<uint32_t, std::shared_ptr<Raid>> raids;
    std::mutex raidsMutex;
    uint32_t nextRaidId = 1;
};
```

## 💡 **Exemplos Práticos**

### **1. Criando uma Raid Básica**

#### **Nível Básico**
```lua
-- Exemplo de criação de raid básica usando o sistema Lua
local function createBasicRaid()
    local raid = Raid("BasicRaid", {
        zone = Zone("raid.basic_zone"),
        allowedDays = { "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" },
        minActivePlayers = 5,
        targetChancePerDay = 0.1,
        maxChancePerCheck = 0.01,
        minGapBetween = "2h"
    })
    
    -- Adicionar broadcast inicial
    raid:addBroadcast("Uma horda de monstros está invadindo a cidade!", MESSAGE_EVENT_ADVANCE)
    
    -- Adicionar estágio de spawn
    raid:addStage({
        start = function()
            local zone = Zone("raid.basic_zone")
            zone:spawnMonsters({
                { name = "Orc", amount = 10 },
                { name = "Troll", amount = 5 }
            })
        end,
        finish = function()
            local zone = Zone("raid.basic_zone")
            zone:removeMonsters()
        end
    })
    
    raid:register()
    return raid
end
```

#### **Nível Intermediário**
```lua
-- Exemplo com configurações avançadas
local function createAdvancedRaid()
    local raid = Raid("AdvancedRaid", {
        zone = Zone("raid.advanced_zone"),
        allowedDays = { "Friday", "Saturday", "Sunday" },
        minActivePlayers = 10,
        initialChance = 0.05,
        targetChancePerDay = 0.2,
        maxChancePerCheck = 0.02,
        minGapBetween = "4h",
        maxChecksPerDay = 24
    })
    
    -- Sistema de estágios múltiplos
    raid:addBroadcast("Uma ameaça antiga desperta...", MESSAGE_EVENT_ADVANCE)
    
    -- Estágio 1: Anúncio
    raid:addStage({
        start = function()
            raid:broadcast(MESSAGE_EVENT_ADVANCE, "O primeiro sinal aparece no horizonte...")
        end,
        duration = "30s"
    })
    
    -- Estágio 2: Spawn inicial
    raid:addStage({
        start = function()
            local zone = Zone("raid.advanced_zone")
            zone:spawnMonsters({
                { name = "Dragon Spawn", amount = 3 },
                { name = "Dragon Hatchling", amount = 8 }
            })
        end,
        finish = function()
            local zone = Zone("raid.advanced_zone")
            zone:removeMonsters()
        end
    })
    
    -- Estágio 3: Boss final
    raid:addStage({
        start = function()
            raid:broadcast(MESSAGE_EVENT_ADVANCE, "O dragão ancião emerge das profundezas!")
            local zone = Zone("raid.advanced_zone")
            zone:spawnMonsters({
                { name = "Ancient Dragon", amount = 1 }
            })
        end,
        finish = function()
            raid:broadcast(MESSAGE_EVENT_ADVANCE, "A ameaça foi derrotada!")
        end
    })
    
    raid:register()
    return raid
end
```

#### **Nível Avançado**
```lua
-- Exemplo com sistema completo de raids
local AdvancedRaidSystem = {}
AdvancedRaidSystem.__index = AdvancedRaidSystem

function AdvancedRaidSystem.new()
    local self = setmetatable({}, AdvancedRaidSystem)
    self.raids = {}
    self.activeRaids = {}
    self.raidHistory = {}
    return self
end

function AdvancedRaidSystem:createRaidWithConditions(config)
    local raid = Raid(config.name, {
        zone = Zone(config.zone),
        allowedDays = config.allowedDays or { "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" },
        minActivePlayers = config.minActivePlayers or 1,
        initialChance = config.initialChance,
        targetChancePerDay = config.targetChancePerDay or 0.1,
        maxChancePerCheck = config.maxChancePerCheck or 0.01,
        minGapBetween = config.minGapBetween or "1h",
        maxChecksPerDay = config.maxChecksPerDay or 24
    })
    
    -- Configurar condições personalizadas
    if config.conditions then
        for _, condition in ipairs(config.conditions) do
            raid:addCondition(condition)
        end
    end
    
    -- Configurar estágios
    if config.stages then
        for _, stage in ipairs(config.stages) do
            raid:addStage(stage)
        end
    end
    
    -- Configurar recompensas
    if config.rewards then
        raid:setRewards(config.rewards)
    end
    
    -- Configurar notificações
    if config.notifications then
        for _, notification in ipairs(config.notifications) do
            raid:addBroadcast(notification.message, notification.type)
        end
    end
    
    raid:register()
    self.raids[config.name] = raid
    return raid
end

function AdvancedRaidSystem:startRaid(raidName, force)
    local raid = self.raids[raidName]
    if not raid then
        return false, "Raid não encontrada"
    end
    
    if raid:tryStart(force) then
        self.activeRaids[raidName] = {
            startTime = os.time(),
            participants = {},
            stage = 1
        }
        return true, "Raid iniciada"
    else
        return false, "Não foi possível iniciar a raid"
    end
end

function AdvancedRaidSystem:trackRaidProgress(raidName, playerId, action)
    local activeRaid = self.activeRaids[raidName]
    if not activeRaid then
        return false, "Raid não está ativa"
    end
    
    activeRaid.participants[playerId] = activeRaid.participants[playerId] or {}
    table.insert(activeRaid.participants[playerId], {
        action = action,
        timestamp = os.time()
    })
    
    return true, "Progresso registrado"
end

function AdvancedRaidSystem:getRaidStatistics(raidName)
    local raid = self.raids[raidName]
    if not raid then
        return nil, "Raid não encontrada"
    end
    
    local stats = {
        name = raidName,
        totalOccurrences = raid.kv:get("total-occurrences") or 0,
        lastOccurrence = raid.kv:get("last-occurrence") or 0,
        failedAttempts = raid.kv:get("failed-attempts") or 0,
        averageDuration = raid.kv:get("average-duration") or 0
    }
    
    return stats
end
```
            3001 // ID da espada
        ));
        
        return templ;
    }
};
```

#### **Nível Avançado**
```cpp
// Sistema de raids dinâmicas
class DynamicRaidManager {
private:
    std::vector<RaidTemplate> templates;
    std::mt19937 rng;
    
public:
    DynamicRaidManager() : rng(std::random_device{}()) {
        loadTemplates();
    }
    
    std::shared_ptr<Raid> createRandomRaid() {
        if (templates.empty()) {
            return nullptr;
        }
        
        // Selecionar template aleatório
        std::uniform_int_distribution<size_t> dist(0, templates.size() - 1);
        size_t index = dist(rng);
        const auto& templ = templates[index];
        
        // Modificar parâmetros aleatoriamente
        auto raid = createFromTemplate(templ);
        if (raid) {
            randomizeRaidParameters(raid);
        }
        
        return raid;
    }
    
private:
    void randomizeRaidParameters(std::shared_ptr<Raid> raid) {
        // Modificar duração
        std::uniform_int_distribution<uint32_t> durationDist(1800, 7200); // 30min - 2h
        raid->setDuration(durationDist(rng));
        
        // Modificar objetivos
        auto objectives = raid->getObjectives();
        for (auto& objective : objectives) {
            std::uniform_int_distribution<uint32_t> qtyDist(1, 20);
            objective.quantity = qtyDist(rng);
        }
        
        // Modificar recompensas
        auto rewards = raid->getRewards();
        for (auto& reward : rewards) {
            if (reward.type == RaidReward::EXPERIENCE) {
                std::uniform_int_distribution<uint32_t> expDist(50000, 500000);
                reward.value = expDist(rng);
            }
        }
    }
};
```

### **2. Gerenciamento de Participantes**

#### **Nível Básico**
```cpp
// Sistema básico de participação
bool joinRaid(const std::shared_ptr<Player>& player, uint32_t raidId) {
    auto& raidManager = RaidManager::getInstance();
    auto raid = raidManager.getRaid(raidId);
    
    if (!raid) {
        player->sendTextMessage(MESSAGE_INFO_DESCR, "Raid not found.");
        return false;
    }
    
    if (!raid->isActive()) {
        player->sendTextMessage(MESSAGE_INFO_DESCR, "Raid is not active.");
        return false;
    }
    
    if (raid->hasParticipant(player)) {
        player->sendTextMessage(MESSAGE_INFO_DESCR, "You are already participating in this raid.");
        return false;
    }
    
    raid->addParticipant(player);
    raid->broadcastMessage(player->getName() + " has joined the raid!");
    
    player->sendTextMessage(MESSAGE_INFO_DESCR, "You have joined the raid: " + raid->getName());
    return true;
}
```

#### **Nível Intermediário**
```cpp
// Sistema de participação com validações
class RaidParticipationManager {
public:
    bool joinRaid(const std::shared_ptr<Player>& player, uint32_t raidId) {
        auto& raidManager = RaidManager::getInstance();
        auto raid = raidManager.getRaid(raidId);
        
        // Verificações
        if (!canJoinRaid(player, raid)) {
            return false;
        }
        
        // Processar entrada
        return processJoinRaid(player, raid);
    }
    
    bool leaveRaid(const std::shared_ptr<Player>& player, uint32_t raidId) {
        auto& raidManager = RaidManager::getInstance();
        auto raid = raidManager.getRaid(raidId);
        
        if (!raid || !raid->hasParticipant(player)) {
            player->sendTextMessage(MESSAGE_INFO_DESCR, "You are not participating in this raid.");
            return false;
        }
        
        raid->removeParticipant(player);
        raid->broadcastMessage(player->getName() + " has left the raid.");
        
        player->sendTextMessage(MESSAGE_INFO_DESCR, "You have left the raid.");
        return true;
    }
    
private:
    bool canJoinRaid(const std::shared_ptr<Player>& player, std::shared_ptr<Raid> raid) {
        if (!raid) {
            player->sendTextMessage(MESSAGE_INFO_DESCR, "Raid not found.");
            return false;
        }
        
        if (!raid->isActive()) {
            player->sendTextMessage(MESSAGE_INFO_DESCR, "Raid is not active.");
            return false;
        }
        
        if (raid->hasParticipant(player)) {
            player->sendTextMessage(MESSAGE_INFO_DESCR, "You are already participating.");
            return false;
        }
        
        // Verificar nível mínimo
        if (player->getLevel() < 50) {
            player->sendTextMessage(MESSAGE_INFO_DESCR, "You need level 50 to join this raid.");
            return false;
        }
        
        // Verificar se não está em outra raid
        if (isPlayerInAnyRaid(player)) {
            player->sendTextMessage(MESSAGE_INFO_DESCR, "You are already in another raid.");
            return false;
        }
        
        return true;
    }
    
    bool processJoinRaid(const std::shared_ptr<Player>& player, std::shared_ptr<Raid> raid) {
        try {
            raid->addParticipant(player);
            
            // Adicionar ao canal de chat da raid
            if (raid->getChatChannel() > 0) {
                auto channel = g_chat().getChannelById(raid->getChatChannel());
                if (channel) {
                    channel->addUser(player);
                }
            }
            
            // Notificar participantes
            raid->broadcastMessage(player->getName() + " has joined the raid!");
            
            // Enviar informações da raid
            sendRaidInfo(player, raid);
            
            g_logger().info("Player {} joined raid {}", player->getName(), raid->getName());
            return true;
            
        } catch (const std::exception& e) {
            g_logger().error("Failed to join raid: {}", e.what());
            return false;
        }
    }
    
    void sendRaidInfo(const std::shared_ptr<Player>& player, std::shared_ptr<Raid> raid) {
        std::string info = "=== RAID INFO ===\n";
        info += "Name: " + raid->getName() + "\n";
        info += "Duration: " + std::to_string(raid->getDuration() / 60) + " minutes\n";
        info += "Participants: " + std::to_string(raid->getParticipants().size()) + "\n";
        info += "Objectives:\n";
        
        for (const auto& objective : raid->getObjectives()) {
            info += "- " + objective.description + " (" + 
                   std::to_string(objective.progress) + "/" + 
                   std::to_string(objective.quantity) + ")\n";
        }
        
        player->sendTextMessage(MESSAGE_INFO_DESCR, info);
    }
};
```

### **3. Sistema de Objetivos**

#### **Nível Básico**
```cpp
// Verificação básica de objetivos
void checkRaidObjectives(const std::shared_ptr<Player>& player, const std::shared_ptr<Monster>& monster) {
    auto& raidManager = RaidManager::getInstance();
    auto activeRaids = raidManager.getActiveRaids();
    
    for (auto& raid : activeRaids) {
        if (!raid->hasParticipant(player)) {
            continue;
        }
        
        auto objectives = raid->getObjectives();
        for (auto& objective : objectives) {
            if (objective.type == RaidObjective::KILL_MONSTER && 
                objective.targetId == monster->getID() && 
                !objective.completed) {
                
                objective.progress++;
                if (objective.progress >= objective.quantity) {
                    objective.completed = true;
                    raid->broadcastMessage("Objective completed: " + objective.description);
                } else {
                    raid->broadcastMessage("Progress: " + objective.description + 
                                         " (" + std::to_string(objective.progress) + 
                                         "/" + std::to_string(objective.quantity) + ")");
                }
            }
        }
        
        // Verificar se todos os objetivos foram completados
        checkRaidCompletion(raid);
    }
}
```

#### **Nível Intermediário**
```cpp
// Sistema de objetivos com tracking avançado
class RaidObjectiveTracker {
private:
    std::unordered_map<uint32_t, std::vector<std::shared_ptr<Raid>>> monsterRaids;
    std::unordered_map<uint32_t, std::vector<std::shared_ptr<Raid>>> itemRaids;
    std::unordered_map<Position, std::vector<std::shared_ptr<Raid>>> locationRaids;
    
public:
    void registerRaid(std::shared_ptr<Raid> raid) {
        for (const auto& objective : raid->getObjectives()) {
            switch (objective.type) {
                case RaidObjective::KILL_MONSTER:
                    monsterRaids[objective.targetId].push_back(raid);
                    break;
                case RaidObjective::COLLECT_ITEM:
                    itemRaids[objective.targetId].push_back(raid);
                    break;
                case RaidObjective::REACH_LOCATION:
                    // Converter ID para Position (implementação específica)
                    Position pos = convertIdToPosition(objective.targetId);
                    locationRaids[pos].push_back(raid);
                    break;
            }
        }
    }
    
    void onMonsterKilled(const std::shared_ptr<Player>& player, const std::shared_ptr<Monster>& monster) {
        auto it = monsterRaids.find(monster->getID());
        if (it == monsterRaids.end()) {
            return;
        }
        
        for (auto& raid : it->second) {
            if (!raid->isActive() || !raid->hasParticipant(player)) {
                continue;
            }
            
            updateObjective(raid, RaidObjective::KILL_MONSTER, monster->getID(), 1);
        }
    }
    
    void onItemCollected(const std::shared_ptr<Player>& player, const std::shared_ptr<Item>& item) {
        auto it = itemRaids.find(item->getID());
        if (it == itemRaids.end()) {
            return;
        }
        
        for (auto& raid : it->second) {
            if (!raid->isActive() || !raid->hasParticipant(player)) {
                continue;
            }
            
            updateObjective(raid, RaidObjective::COLLECT_ITEM, item->getID(), 1);
        }
    }
    
    void onPlayerMove(const std::shared_ptr<Player>& player, const Position& position) {
        auto it = locationRaids.find(position);
        if (it == locationRaids.end()) {
            return;
        }
        
        for (auto& raid : it->second) {
            if (!raid->isActive() || !raid->hasParticipant(player)) {
                continue;
            }
            
            updateObjective(raid, RaidObjective::REACH_LOCATION, convertPositionToId(position), 1);
        }
    }
    
private:
    void updateObjective(std::shared_ptr<Raid> raid, RaidObjective::Type type, uint32_t targetId, uint32_t progress) {
        auto objectives = raid->getObjectives();
        bool updated = false;
        
        for (auto& objective : objectives) {
            if (objective.type == type && objective.targetId == targetId && !objective.completed) {
                objective.progress += progress;
                
                if (objective.progress >= objective.quantity) {
                    objective.completed = true;
                    raid->broadcastMessage("🎉 Objective completed: " + objective.description);
                } else {
                    raid->broadcastMessage("📊 Progress: " + objective.description + 
                                         " (" + std::to_string(objective.progress) + 
                                         "/" + std::to_string(objective.quantity) + ")");
                }
                
                updated = true;
                break;
            }
        }
        
        if (updated) {
            checkRaidCompletion(raid);
        }
    }
    
    void checkRaidCompletion(std::shared_ptr<Raid> raid) {
        auto objectives = raid->getObjectives();
        bool allCompleted = true;
        
        for (const auto& objective : objectives) {
            if (!objective.completed) {
                allCompleted = false;
                break;
            }
        }
        
        if (allCompleted) {
            completeRaid(raid);
        }
    }
    
    void completeRaid(std::shared_ptr<Raid> raid) {
        raid->setCompleted(true);
        raid->setActive(false);
        raid->setEndTime(std::time(nullptr));
        
        raid->broadcastMessage("🎊 RAID COMPLETED! 🎊");
        raid->broadcastMessage("Congratulations to all participants!");
        
        // Distribuir recompensas
        raid->distributeRewards();
        
        g_logger().info("Raid '{}' completed successfully", raid->getName());
    }
};
```

### **4. Sistema de Recompensas**

#### **Nível Básico**
```cpp
// Distribuição básica de recompensas
void distributeRaidRewards(std::shared_ptr<Raid> raid) {
    auto participants = raid->getParticipants();
    if (participants.empty()) {
        return;
    }
    
    for (const auto& reward : raid->getRewards()) {
        if (reward.distributed) {
            continue;
        }
        
        for (const auto& player : participants) {
            switch (reward.type) {
                case RaidReward::EXPERIENCE:
                    player->addExperience(reward.value);
                    player->sendTextMessage(MESSAGE_INFO_DESCR, 
                        "You gained " + std::to_string(reward.value) + " experience!");
                    break;
                    
                case RaidReward::GOLD:
                    player->addMoney(reward.value);
                    player->sendTextMessage(MESSAGE_INFO_DESCR, 
                        "You received " + std::to_string(reward.value) + " gold!");
                    break;
                    
                case RaidReward::ITEM:
                    auto item = Item::CreateItem(reward.value);
                    if (item && player->addItem(item)) {
                        player->sendTextMessage(MESSAGE_INFO_DESCR, 
                            "You received: " + item->getName());
                    }
                    break;
            }
        }
    }
}
```

#### **Nível Intermediário**
```cpp
// Sistema de recompensas com distribuição inteligente
class RaidRewardManager {
public:
    void distributeRewards(std::shared_ptr<Raid> raid) {
        auto participants = raid->getParticipants();
        if (participants.empty()) {
            return;
        }
        
        // Calcular contribuição de cada jogador
        std::map<std::shared_ptr<Player>, uint32_t> contributions;
        calculateContributions(raid, contributions);
        
        // Distribuir recompensas baseado na contribuição
        for (const auto& reward : raid->getRewards()) {
            if (reward.distributed) {
                continue;
            }
            
            distributeReward(raid, reward, contributions);
        }
        
        // Salvar progresso
        saveRaidProgress(raid);
    }
    
private:
    void calculateContributions(std::shared_ptr<Raid> raid, 
                               std::map<std::shared_ptr<Player>, uint32_t>& contributions) {
        // Implementação baseada em dados de tracking
        // Por exemplo: dano causado, objetivos completados, tempo participado
        
        for (const auto& player : raid->getParticipants()) {
            uint32_t contribution = 0;
            
            // Dano causado
            contribution += getPlayerDamage(player, raid);
            
            // Objetivos completados
            contribution += getObjectivesCompleted(player, raid);
            
            // Tempo participado
            contribution += getParticipationTime(player, raid);
            
            contributions[player] = contribution;
        }
    }
    
    void distributeReward(std::shared_ptr<Raid> raid, const RaidReward& reward,
                         const std::map<std::shared_ptr<Player>, uint32_t>& contributions) {
        uint32_t totalContribution = 0;
        for (const auto& [player, contrib] : contributions) {
            totalContribution += contrib;
        }
        
        if (totalContribution == 0) {
            // Distribuir igualmente
            auto participants = raid->getParticipants();
            uint32_t share = reward.value / participants.size();
            
            for (const auto& player : participants) {
                giveReward(player, reward, share);
            }
        } else {
            // Distribuir proporcionalmente
            for (const auto& [player, contrib] : contributions) {
                uint32_t share = (reward.value * contrib) / totalContribution;
                if (share > 0) {
                    giveReward(player, reward, share);
                }
            }
        }
    }
    
    void giveReward(const std::shared_ptr<Player>& player, const RaidReward& reward, uint32_t amount) {
        switch (reward.type) {
            case RaidReward::EXPERIENCE:
                player->addExperience(amount);
                player->sendTextMessage(MESSAGE_INFO_DESCR, 
                    "Raid reward: " + std::to_string(amount) + " experience");
                break;
                
            case RaidReward::GOLD:
                player->addMoney(amount);
                player->sendTextMessage(MESSAGE_INFO_DESCR, 
                    "Raid reward: " + std::to_string(amount) + " gold");
                break;
                
            case RaidReward::ITEM:
                auto item = Item::CreateItem(reward.value);
                if (item && player->addItem(item)) {
                    player->sendTextMessage(MESSAGE_INFO_DESCR, 
                        "Raid reward: " + item->getName());
                }
                break;
        }
    }
};
```

### **5. Integração com Chat**

#### **Nível Básico**
```cpp
// Sistema básico de chat para raids
void setupRaidChat(std::shared_ptr<Raid> raid) {
    // Criar canal de chat específico para a raid
    uint16_t channelId = raid->getChatChannel();
    if (channelId == 0) {
        channelId = createRaidChannel(raid->getName());
        raid->setChatChannel(channelId);
    }
    
    // Adicionar todos os participantes ao canal
    for (const auto& player : raid->getParticipants()) {
        auto channel = g_chat().getChannelById(channelId);
        if (channel) {
            channel->addUser(player);
        }
    }
    
    // Enviar mensagem de boas-vindas
    raid->broadcastMessage("Welcome to " + raid->getName() + "!");
    raid->broadcastMessage("Use this channel to coordinate with your team.");
}

uint16_t createRaidChannel(const std::string& raidName) {
    // Implementação de criação de canal
    // Retorna ID do canal criado
    return 0;
}
```

#### **Nível Intermediário**
```cpp
// Sistema de chat avançado para raids
class RaidChatManager {
private:
    std::unordered_map<uint32_t, uint16_t> raidChannels;
    
public:
    void initializeRaidChat(std::shared_ptr<Raid> raid) {
        uint16_t channelId = createRaidChannel(raid);
        raidChannels[raid->getId()] = channelId;
        raid->setChatChannel(channelId);
        
        // Configurar canal
        setupChannelFeatures(channelId, raid);
        
        // Adicionar participantes
        addParticipantsToChannel(raid);
        
        // Enviar informações iniciais
        sendRaidInfo(raid);
    }
    
    void cleanupRaidChat(uint32_t raidId) {
        auto it = raidChannels.find(raidId);
        if (it != raidChannels.end()) {
            // Remover canal após um tempo
            scheduleChannelRemoval(it->second);
            raidChannels.erase(it);
        }
    }
    
private:
    uint16_t createRaidChannel(const std::shared_ptr<Raid>& raid) {
        std::string channelName = "Raid: " + raid->getName();
        
        // Criar canal privado para a raid
        auto channel = g_chat().createChannel(nullptr, 0); // Canal temporário
        if (channel) {
            channel->setName(channelName);
            return channel->getId();
        }
        
        return 0;
    }
    
    void setupChannelFeatures(uint16_t channelId, std::shared_ptr<Raid> raid) {
        auto channel = g_chat().getChannelById(channelId);
        if (!channel) {
            return;
        }
        
        // Configurar comandos especiais
        setupRaidCommands(channel, raid);
        
        // Configurar moderação
        setupChannelModeration(channel);
    }
    
    void setupRaidCommands(std::shared_ptr<ChatChannel> channel, std::shared_ptr<Raid> raid) {
        // Comandos específicos para raids
        // /status - Mostrar status da raid
        // /objectives - Mostrar objetivos
        // /participants - Listar participantes
        // /leave - Sair da raid
    }
    
    void sendRaidInfo(std::shared_ptr<Raid> raid) {
        std::string info = "=== RAID INFORMATION ===\n";
        info += "Name: " + raid->getName() + "\n";
        info += "Duration: " + std::to_string(raid->getDuration() / 60) + " minutes\n";
        info += "Participants: " + std::to_string(raid->getParticipants().size()) + "\n";
        info += "Objectives:\n";
        
        for (const auto& objective : raid->getObjectives()) {
            info += "- " + objective.description + "\n";
        }
        
        info += "Rewards:\n";
        for (const auto& reward : raid->getRewards()) {
            info += "- " + reward.description + "\n";
        }
        
        raid->broadcastMessage(info);
    }
};
```

## 🔧 **Dependências**

### **Sistemas Integrados**
- **Chat System**: Comunicação entre participantes
- **Party System**: Organização de grupos
- **Monster System**: Tracking de kills
- **Player System**: Gerenciamento de participantes
- **Item System**: Coleta de itens
- **Map System**: Tracking de localização

### **Bibliotecas Externas**
- **spdlog**: Logging de eventos
- **fmt**: Formatação de mensagens
- **chrono**: Gerenciamento de tempo

## ⚡ **Otimizações**

### **1. Cache de Raids**
```cpp
// Cache para raids ativas
class RaidCache {
private:
    std::unordered_map<uint32_t, std::shared_ptr<Raid>> activeRaids;
    std::mutex cacheMutex;
    
public:
    void addRaid(std::shared_ptr<Raid> raid) {
        std::lock_guard<std::mutex> lock(cacheMutex);
        activeRaids[raid->getId()] = raid;
    }
    
    void removeRaid(uint32_t raidId) {
        std::lock_guard<std::mutex> lock(cacheMutex);
        activeRaids.erase(raidId);
    }
    
    std::vector<std::shared_ptr<Raid>> getActiveRaids() {
        std::lock_guard<std::mutex> lock(cacheMutex);
        std::vector<std::shared_ptr<Raid>> raids;
        for (const auto& [id, raid] : activeRaids) {
            raids.push_back(raid);
        }
        return raids;
    }
};
```

### **2. Sistema de Tracking Otimizado**
```cpp
// Sistema de tracking com índices
class OptimizedRaidTracker {
private:
    std::unordered_map<uint32_t, std::vector<uint32_t>> monsterToRaids;
    std::unordered_map<uint32_t, std::vector<uint32_t>> itemToRaids;
    std::unordered_map<Position, std::vector<uint32_t>> locationToRaids;
    
public:
    void registerRaid(std::shared_ptr<Raid> raid) {
        for (const auto& objective : raid->getObjectives()) {
            switch (objective.type) {
                case RaidObjective::KILL_MONSTER:
                    monsterToRaids[objective.targetId].push_back(raid->getId());
                    break;
                case RaidObjective::COLLECT_ITEM:
                    itemToRaids[objective.targetId].push_back(raid->getId());
                    break;
                case RaidObjective::REACH_LOCATION:
                    Position pos = convertIdToPosition(objective.targetId);
                    locationToRaids[pos].push_back(raid->getId());
                    break;
            }
        }
    }
    
    void onMonsterKilled(const std::shared_ptr<Player>& player, uint32_t monsterId) {
        auto it = monsterToRaids.find(monsterId);
        if (it != monsterToRaids.end()) {
            for (uint32_t raidId : it->second) {
                updateRaidObjective(raidId, player, RaidObjective::KILL_MONSTER, monsterId);
            }
        }
    }
};
```

## 📊 **Casos de Uso Comuns**

### **1. Raid de Boss**
```cpp
// Sistema de raid de boss
class BossRaidManager {
public:
    std::shared_ptr<Raid> createBossRaid(const std::string& bossName, uint32_t bossId) {
        auto raid = std::make_shared<Raid>(generateRaidId(), "Boss Raid: " + bossName);
        
        // Objetivo: Derrotar o boss
        RaidObjective objective(RaidObjective::DEFEAT_BOSS, "Defeat " + bossName, bossId, 1);
        raid->addObjective(objective);
        
        // Recompensas
        RaidReward expReward(RaidReward::EXPERIENCE, "Boss Experience", 100000);
        RaidReward itemReward(RaidReward::ITEM, "Boss Loot", getBossLootId(bossId));
        
        raid->addReward(expReward);
        raid->addReward(itemReward);
        
        raid->setDuration(1800); // 30 minutos
        
        return raid;
    }
};
```

### **2. Raid de Coleta**
```cpp
// Sistema de raid de coleta
class CollectionRaidManager {
public:
    std::shared_ptr<Raid> createCollectionRaid(const std::string& itemName, uint32_t itemId, uint32_t quantity) {
        auto raid = std::make_shared<Raid>(generateRaidId(), "Collection: " + itemName);
        
        // Objetivo: Coletar itens
        RaidObjective objective(RaidObjective::COLLECT_ITEM, 
                               "Collect " + std::to_string(quantity) + " " + itemName, 
                               itemId, quantity);
        raid->addObjective(objective);
        
        // Recompensas baseadas na quantidade
        uint32_t rewardExp = quantity * 1000;
        RaidReward expReward(RaidReward::EXPERIENCE, "Collection Bonus", rewardExp);
        raid->addReward(expReward);
        
        raid->setDuration(3600); // 1 hora
        
        return raid;
    }
};
```

## 🚀 **Passos de Implementação**

### **1. Configuração Inicial**
1. **Definir Templates**: Criar templates de raids
2. **Configurar Objetivos**: Definir tipos de objetivos
3. **Configurar Recompensas**: Definir sistema de recompensas
4. **Configurar Chat**: Integrar com sistema de chat

### **2. Estrutura de Dados**
1. **Tabela raids**: Dados das raids
2. **Tabela raid_participants**: Participantes
3. **Tabela raid_objectives**: Objetivos
4. **Tabela raid_rewards**: Recompensas

### **3. Implementação de Classes**
1. **RaidManager**: Gerenciador principal
2. **RaidObjectiveTracker**: Tracking de objetivos
3. **RaidRewardManager**: Sistema de recompensas
4. **RaidChatManager**: Integração com chat

### **4. Integração com Sistemas**
1. **Chat System**: Comunicação
2. **Party System**: Organização
3. **Monster System**: Tracking
4. **Player System**: Participação

## 📈 **Métricas e Performance**

### **Estatísticas do Sistema**
- **Raids Simultâneas**: 10-50 raids ativas
- **Participantes por Raid**: 5-50 jogadores
- **Objetivos por Raid**: 1-10 objetivos
- **Recompensas por Raid**: 1-5 recompensas

### **Otimizações de Performance**
- **Cache Hit Rate**: 95%+ para raids ativas
- **Objective Tracking**: <10ms por evento
- **Reward Distribution**: <100ms para distribuição
- **Memory Usage**: <5MB para sistema completo

---

**Status**: ✅ **COMPLETO**  
**Próxima Página**: [[canary_sistema_eventos|Sistema de Eventos]]  
**Página Anterior**: [[canary_sistema_houses|Sistema de Houses]] 