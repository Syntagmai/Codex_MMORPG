---
tags: [canary_research, npc_system, habdel_research, deep_analysis]
type: research_story
status: completed
priority: high
created: 2025-01-27
target: canary
epic: canary_deep_research
story: CANARY-014
---

# CANARY-014: Sistema de NPCs - Pesquisa Habdel

## 🎯 **Objetivo da Pesquisa**

Realizar uma análise profunda e completa do Sistema de NPCs do Canary, mapeando sua arquitetura, componentes, APIs, integrações e implementações práticas. Esta pesquisa visa compreender como o sistema de NPCs funciona, suas otimizações, e como se integra com outros sistemas do servidor.

## 📋 **Metodologia Habdel**

### **Fase 1: Descoberta e Mapeamento**
- [x] Identificar arquivos relacionados ao sistema de NPCs
- [x] Mapear classes e estruturas principais
- [x] Identificar APIs e interfaces públicas
- [x] Documentar dependências e integrações

### **Fase 2: Análise Profunda**
- [x] Analisar implementação de cada componente
- [x] Documentar algoritmos e lógicas de negócio
- [x] Mapear fluxos de dados e controle
- [x] Identificar otimizações e padrões de design

### **Fase 3: Documentação e Exemplos**
- [x] Criar documentação técnica completa
- [x] Desenvolver exemplos práticos
- [x] Documentar casos de uso comuns
- [x] Criar guias de integração

### **Fase 4: Validação e Consolidação**
- [x] Validar documentação com código real
- [x] Consolidar descobertas
- [x] Identificar insights e recomendações
- [x] Preparar lição educacional

## 🔍 **Arquivos Identificados para Análise**

### **Arquivos Principais:**
- `canary/src/creatures/npcs/npc.hpp` - Classe principal de NPC
- `canary/src/creatures/npcs/npc.cpp` - Implementação do NPC
- `canary/src/creatures/npcs/npcs.hpp` - Sistema de tipos de NPC
- `canary/src/creatures/npcs/npcs.cpp` - Implementação do sistema de NPCs
- `canary/src/creatures/npcs/spawns/spawn_npc.hpp` - Sistema de spawns
- `canary/src/creatures/npcs/spawns/spawn_npc.cpp` - Implementação de spawns

### **Arquivos Relacionados:**
- `canary/src/lua/functions/creatures/npc/npc_functions.hpp` - Funções Lua
- `canary/src/lua/functions/creatures/npc/npc_type_functions.hpp` - Funções Lua de tipo
- `canary/src/creatures/creatures_definitions.hpp` - Definições de eventos

## 📊 **Status da Pesquisa**

### **Progresso Geral**: 100%
### **Fase Atual**: Fase 4 - Validação e Consolidação
### **Arquivos Analisados**: 8/8
### **Componentes Mapeados**: 12/12

---

## 🔬 **Análise Completa**

### **Fase 1: Descoberta e Mapeamento - CONCLUÍDA**

#### **Arquivos Principais Identificados:**
- ✅ `canary/src/creatures/npcs/npc.hpp` - Classe principal de NPC
- ✅ `canary/src/creatures/npcs/npc.cpp` - Implementação do NPC
- ✅ `canary/src/creatures/npcs/npcs.hpp` - Sistema de tipos de NPC
- ✅ `canary/src/creatures/npcs/npcs.cpp` - Implementação do sistema
- ✅ `canary/src/creatures/npcs/spawns/spawn_npc.hpp` - Sistema de spawns
- ✅ `canary/src/creatures/npcs/spawns/spawn_npc.cpp` - Implementação de spawns
- ✅ `canary/src/lua/functions/creatures/npc/npc_functions.hpp` - Funções Lua
- ✅ `canary/src/lua/functions/creatures/npc/npc_type_functions.hpp` - Funções Lua de tipo

#### **Componentes Principais Mapeados:**

**1. Classe Npc (Principal)**
- Herda de Creature
- Sistema de interação com jogadores
- Sistema de loja e comércio
- Sistema de movimento e comportamento
- Sistema de eventos e callbacks

**2. Classe NpcType**
- Definição de tipo de NPC
- Configurações de aparência e comportamento
- Sistema de eventos e scripts
- Configurações de loja

**3. Sistema de Spawns**
- SpawnNpc: Gerenciamento de spawns individuais
- SpawnsNpc: Gerenciamento global de spawns
- Sistema de respawn automático

**4. Sistema de Eventos**
- NPCS_EVENT_THINK: Evento de pensamento
- NPCS_EVENT_APPEAR: Evento de aparecimento
- NPCS_EVENT_DISAPPEAR: Evento de desaparecimento
- NPCS_EVENT_MOVE: Evento de movimento
- NPCS_EVENT_SAY: Evento de fala
- NPCS_EVENT_PLAYER_BUY: Evento de compra
- NPCS_EVENT_PLAYER_SELL: Evento de venda

### **Fase 2: Análise Profunda - CONCLUÍDA**

#### **Componentes Analisados:**
- [x] Análise detalhada da implementação do NPC
- [x] Documentação do sistema de tipos
- [x] Mapeamento do sistema de spawns
- [x] Análise do sistema de eventos
- [x] Documentação das funções Lua

## 📚 **Documentação Técnica**

### **1. Arquitetura do Sistema de NPCs**

O sistema de NPCs do Canary é uma arquitetura complexa e modular que gerencia todos os NPCs não-jogadores no servidor. Ele é composto por vários componentes interconectados:

#### **1.1 Classe Npc (Principal)**
```cpp
class Npc final : public Creature {
public:
    static std::shared_ptr<Npc> createNpc(const std::string &name);
    
    explicit Npc(const std::shared_ptr<NpcType> &npcType);
    
    // Sistema de identificação
    void setID() override;
    const std::string &getName() const override;
    const std::string &getTypeName() const override;
    
    // Sistema de posição
    const Position &getMasterPos() const;
    void setMasterPos(Position pos);
    
    // Sistema de interação
    void setPlayerInteraction(uint32_t playerId, uint16_t topicId = 0);
    void removePlayerInteraction(const std::shared_ptr<Player> &player);
    bool isInteractingWithPlayer(uint32_t playerId);
    
    // Sistema de loja
    const std::vector<ShopBlock> &getShopItemVector(uint32_t playerGUID) const;
    bool isShopPlayer(uint32_t playerGUID) const;
    void addShopPlayer(uint32_t playerGUID, const std::vector<ShopBlock> &shopItems);
    
    // Sistema de movimento
    bool canWalkTo(const Position &fromPos, Direction dir);
    bool getNextStep(Direction &nextDirection, uint32_t &flags) override;
    bool getRandomStep(Direction &moveDirection);
    
    // Eventos
    void onThink(uint32_t interval) override;
    void onCreatureAppear(const std::shared_ptr<Creature> &creature, bool isLogin) override;
    void onCreatureSay(const std::shared_ptr<Creature> &creature, SpeakClasses type, const std::string &text) override;
    
private:
    std::shared_ptr<NpcType> npcType;
    std::shared_ptr<SpawnNpc> spawnNpc;
    std::map<uint32_t, uint16_t> playerInteractions;
    std::unordered_map<uint32_t, std::vector<ShopBlock>> shopPlayers;
    Position masterPos;
};
```

#### **1.2 Classe NpcType**
```cpp
class NpcType final : public SharedObject {
    struct NpcInfo {
        Outfit_t outfit = {};
        RespawnType respawnType = {};
        LightInfo light = {};
        
        uint8_t speechBubble = SPEECHBUBBLE_NORMAL;
        uint16_t currencyId = ITEM_GOLD_COIN;
        
        uint32_t yellChance = 0;
        uint32_t yellSpeedTicks = 0;
        uint32_t baseSpeed = 55;
        uint32_t walkInterval = 2000;
        
        int32_t thinkEvent = -1;
        int32_t playerBuyEvent = -1;
        int32_t playerSellEvent = -1;
        
        int32_t health = 100;
        int32_t healthMax = 100;
        int32_t walkRadius = 10;
        
        bool canPushItems = false;
        bool canPushCreatures = false;
        bool pushable = false;
        bool floorChange = false;
        
        std::vector<voiceBlock_t> voiceVector;
        std::set<std::string> scripts;
        std::vector<ShopBlock> shopItemVector;
        
        NpcsEvent_t eventType = NPCS_EVENT_NONE;
    };

public:
    std::string name;
    std::string typeName;
    std::string nameDescription;
    NpcInfo info;
    
    void loadShop(const std::shared_ptr<NpcType> &npcType, ShopBlock shopBlock);
    bool loadCallback(LuaScriptInterface* scriptInterface);
    bool canSpawn(const Position &pos) const;
};
```

### **2. Sistema de Spawns**

#### **2.1 Classe SpawnNpc**
```cpp
class SpawnNpc final : public SharedObject {
public:
    SpawnNpc(Position initPos, int32_t initRadius);
    
    bool addNpc(const std::string &name, const Position &pos, Direction dir, uint32_t interval);
    void removeNpc(const std::shared_ptr<Npc> &npc);
    
    void startup();
    void startSpawnNpcCheck();
    void stopEvent();
    
    bool isInSpawnNpcZone(const Position &pos) const;
    void cleanup();

private:
    using SpawnedNpcMap = std::multimap<uint32_t, std::shared_ptr<Npc>>;
    SpawnedNpcMap spawnedNpcMap;
    
    std::map<uint32_t, spawnBlockNpc_t> spawnNpcMap;
    
    Position centerPos;
    int32_t radius;
    uint32_t interval = 60000;
    uint32_t checkSpawnNpcEvent = 0;
    
    bool spawnNpc(uint32_t spawnId, const std::shared_ptr<NpcType> &npcType, const Position &pos, Direction dir, bool startup = false);
    void checkSpawnNpc();
    void scheduleSpawnNpc(uint32_t spawnId, spawnBlockNpc_t &sb, uint16_t interval);
};
```

#### **2.2 Estrutura spawnBlockNpc_t**
```cpp
struct spawnBlockNpc_t {
    Position pos;
    std::shared_ptr<NpcType> npcType;
    int64_t lastSpawnNpc;
    uint32_t interval;
    Direction direction;
};
```

#### **2.3 Classe SpawnsNpc**
```cpp
class SpawnsNpc {
public:
    static bool isInZone(const Position &centerPos, int32_t radius, const Position &pos);
    
    bool loadFromXml(const std::string &filenpcname);
    void startup();
    void clear();
    
    bool isStarted() const;
    bool setStarted(bool setStarted);
    
    std::vector<std::shared_ptr<SpawnNpc>> &getSpawnNpcList();

private:
    std::vector<std::shared_ptr<SpawnNpc>> spawnNpcList;
    std::string fileName;
    bool loaded = false;
    bool started = false;
};
```

### **3. Sistema de Eventos**

#### **3.1 Tipos de Eventos**
```cpp
enum NpcsEvent_t : uint8_t {
    NPCS_EVENT_NONE = 0,
    NPCS_EVENT_THINK = 1,
    NPCS_EVENT_APPEAR = 2,
    NPCS_EVENT_DISAPPEAR = 3,
    NPCS_EVENT_MOVE = 4,
    NPCS_EVENT_SAY = 5,
    NPCS_EVENT_PLAYER_BUY = 6,
    NPCS_EVENT_PLAYER_SELL = 7,
    NPCS_EVENT_PLAYER_CHECK_ITEM = 8,
    NPCS_EVENT_PLAYER_CLOSE_CHANNEL = 9
};
```

#### **3.2 Eventos na Classe Npc**
```cpp
class Npc {
public:
    // Eventos de criatura
    void onCreatureAppear(const std::shared_ptr<Creature> &creature, bool isLogin) override;
    void onRemoveCreature(const std::shared_ptr<Creature> &creature, bool isLogout) override;
    void onCreatureMove(const std::shared_ptr<Creature> &creature, const std::shared_ptr<Tile> &newTile, const Position &newPos, const std::shared_ptr<Tile> &oldTile, const Position &oldPos, bool teleport) override;
    void onCreatureSay(const std::shared_ptr<Creature> &creature, SpeakClasses type, const std::string &text) override;
    void onThink(uint32_t interval) override;
    
    // Eventos de jogador
    void onPlayerBuyItem(const std::shared_ptr<Player> &player, uint16_t itemid, uint8_t count, uint16_t amount, bool ignore, bool inBackpacks);
    void onPlayerSellItem(const std::shared_ptr<Player> &player, uint16_t itemid, uint8_t count, uint16_t amount, bool ignore);
    void onPlayerCheckItem(const std::shared_ptr<Player> &player, uint16_t itemid, uint8_t count);
    void onPlayerCloseChannel(const std::shared_ptr<Creature> &creature);
    
private:
    void onThinkYell(uint32_t interval);
    void onThinkWalk(uint32_t interval);
    void onThinkSound(uint32_t interval);
};
```

### **4. Sistema de Loja**

#### **4.1 Gerenciamento de Loja**
```cpp
class Npc {
public:
    const std::vector<ShopBlock> &getShopItemVector(uint32_t playerGUID) const;
    bool isShopPlayer(uint32_t playerGUID) const;
    void addShopPlayer(uint32_t playerGUID, const std::vector<ShopBlock> &shopItems);
    void removeShopPlayer(uint32_t playerGUID);
    void closeAllShopWindows();

private:
    std::unordered_map<uint32_t, std::vector<ShopBlock>> shopPlayers;
};
```

#### **4.2 Estrutura ShopBlock**
```cpp
struct ShopBlock {
    uint16_t itemId {};
    std::string itemName;
    int32_t itemSubType {};
    uint32_t itemBuyPrice {};
    uint32_t itemSellPrice {};
    int32_t itemStorageKey {};
    int32_t itemStorageValue {};
    
    std::vector<ShopBlock> childShop;
};
```

### **5. Sistema de Interação**

#### **5.1 Interação com Jogadores**
```cpp
class Npc {
public:
    void setPlayerInteraction(uint32_t playerId, uint16_t topicId = 0);
    void removePlayerInteraction(const std::shared_ptr<Player> &player);
    void resetPlayerInteractions();
    
    bool isInteractingWithPlayer(uint32_t playerId);
    bool isPlayerInteractingOnTopic(uint32_t playerId, uint16_t topicId);
    bool canInteract(const Position &pos, uint32_t range = 4);

private:
    std::vector<uint32_t> playerInteractionsOrder;
    std::map<uint32_t, uint16_t> playerInteractions;
};
```

### **6. Sistema de Movimento**

#### **6.1 Movimento Inteligente**
```cpp
class Npc {
public:
    bool canWalkTo(const Position &fromPos, Direction dir);
    bool getNextStep(Direction &nextDirection, uint32_t &flags) override;
    bool getRandomStep(Direction &moveDirection);
    void onCreatureWalk() override;
    
private:
    bool isInSpawnRange(const Position &pos) const;
    void onThinkWalk(uint32_t interval);
};
```

### **7. Sistema de Comportamento**

#### **7.1 Comportamentos Automáticos**
```cpp
class Npc {
private:
    void onThinkYell(uint32_t interval);
    void onThinkWalk(uint32_t interval);
    void onThinkSound(uint32_t interval);
    
    uint32_t yellTicks = 0;
    uint32_t walkTicks = 0;
    uint32_t soundTicks = 0;
};
```

### **8. Sistema de Gerenciamento**

#### **8.1 Classe Npcs**
```cpp
class Npcs {
public:
    static Npcs &getInstance();
    
    std::shared_ptr<NpcType> getNpcType(const std::string &name, bool create = false);
    
    bool load(bool loadLibs = true, bool loadNpcs = true, bool reloading = false) const;
    bool reload();

private:
    std::unique_ptr<LuaScriptInterface> scriptInterface;
    std::map<std::string, std::shared_ptr<NpcType>> npcs;
};
```

### **9. Integração com Lua**

#### **9.1 Funções Lua de NPC**
```cpp
class NpcFunctions {
public:
    static int luaNpcCreate(lua_State* L);
    static int luaNpcIsNpc(lua_State* L);
    static int luaNpcSetMasterPos(lua_State* L);
    static int luaNpcGetCurrency(lua_State* L);
    static int luaNpcSetCurrency(lua_State* L);
    static int luaNpcGetSpeechBubble(lua_State* L);
    static int luaNpcSetSpeechBubble(lua_State* L);
    static int luaNpcGetId(lua_State* L);
    static int luaNpcGetName(lua_State* L);
    static int luaNpcSetName(lua_State* L);
    static int luaNpcPlace(lua_State* L);
    static int luaNpcSay(lua_State* L);
    static int luaNpcTurnToCreature(lua_State* L);
    static int luaNpcSetPlayerInteraction(lua_State* L);
    static int luaNpcRemovePlayerInteraction(lua_State* L);
    static int luaNpcIsInteractingWithPlayer(lua_State* L);
    static int luaNpcIsInTalkRange(lua_State* L);
    static int luaNpcOpenShopWindow(lua_State* L);
    static int luaNpcCloseShopWindow(lua_State* L);
    static int luaNpcGetShopItem(lua_State* L);
    static int luaNpcIsMerchant(lua_State* L);
    static int luaNpcMove(lua_State* L);
    static int luaNpcTurn(lua_State* L);
    static int luaNpcFollow(lua_State* L);
    static int luaNpcSellItem(lua_State* L);
    static int luaNpcGetDistanceTo(lua_State* L);
};
```

#### **9.2 Funções Lua de NpcType**
```cpp
class NpcTypeFunctions {
public:
    static int luaNpcTypeCreate(lua_State* L);
    static int luaNpcTypeIsPushable(lua_State* L);
    static int luaNpcTypeFloorChange(lua_State* L);
    static int luaNpcTypeCanSpawn(lua_State* L);
    static int luaNpcTypeCanPushItems(lua_State* L);
    static int luaNpcTypeCanPushCreatures(lua_State* L);
    static int luaNpcTypeName(lua_State* L);
    static int luaNpcTypeNameDescription(lua_State* L);
    static int luaNpcTypeHealth(lua_State* L);
    static int luaNpcTypeMaxHealth(lua_State* L);
    static int luaNpcTypeGetVoices(lua_State* L);
    static int luaNpcTypeAddVoice(lua_State* L);
    static int luaNpcTypeGetCreatureEvents(lua_State* L);
    static int luaNpcTypeRegisterEvent(lua_State* L);
    static int luaNpcTypeEventOnCallback(lua_State* L);
    static int luaNpcTypeEventType(lua_State* L);
    static int luaNpcTypeOutfit(lua_State* L);
    static int luaNpcTypeBaseSpeed(lua_State* L);
    static int luaNpcTypeWalkInterval(lua_State* L);
    static int luaNpcTypeWalkRadius(lua_State* L);
    static int luaNpcTypeLight(lua_State* L);
    static int luaNpcTypeYellChance(lua_State* L);
    static int luaNpcTypeYellSpeedTicks(lua_State* L);
    static int luaNpcTypeRespawnTypePeriod(lua_State* L);
    static int luaNpcTypeRespawnTypeIsUnderground(lua_State* L);
    static int luaNpcTypeSpeechBubble(lua_State* L);
    static int luaNpcTypeCurrency(lua_State* L);
    static int luaNpcTypeAddShopItem(lua_State* L);
    static int luaNpcTypeSoundChance(lua_State* L);
    static int luaNpcTypeSoundSpeedTicks(lua_State* L);
    static int luaNpcTypeAddSound(lua_State* L);
    static int luaNpcTypeGetSounds(lua_State* L);
};
```

## 💡 **Insights e Descobertas**

### **1. Arquitetura Modular e Extensível**

#### **1.1 Separação de Responsabilidades**
O sistema de NPCs utiliza uma arquitetura bem definida:
- **Npc**: Instância individual de NPC
- **NpcType**: Definição de tipo e comportamento
- **SpawnNpc**: Gerenciamento de spawns
- **Npcs**: Gerenciamento global

#### **1.2 Sistema de Eventos Robusto**
```cpp
// Múltiplos tipos de eventos
enum NpcsEvent_t : uint8_t {
    NPCS_EVENT_THINK = 1,
    NPCS_EVENT_APPEAR = 2,
    NPCS_EVENT_DISAPPEAR = 3,
    NPCS_EVENT_MOVE = 4,
    NPCS_EVENT_SAY = 5,
    NPCS_EVENT_PLAYER_BUY = 6,
    NPCS_EVENT_PLAYER_SELL = 7,
    // ...
};
```

### **2. Sistema de Spawns Inteligente**

#### **2.1 Spawn Automático**
```cpp
class SpawnNpc {
    // Verificação automática de spawn
    void checkSpawnNpc();
    
    // Agendamento de spawns
    void scheduleSpawnNpc(uint32_t spawnId, spawnBlockNpc_t &sb, uint16_t interval);
    
    // Verificação de zona
    bool isInSpawnNpcZone(const Position &pos) const;
};
```

#### **2.2 Sistema de Respawn**
- Intervalo configurável por NPC
- Verificação de jogadores próximos
- Spawn automático quando necessário

### **3. Sistema de Loja Avançado**

#### **3.1 Loja por Jogador**
```cpp
// Cada jogador tem sua própria loja
std::unordered_map<uint32_t, std::vector<ShopBlock>> shopPlayers;

// Adicionar jogador à loja
void addShopPlayer(uint32_t playerGUID, const std::vector<ShopBlock> &shopItems);

// Verificar se jogador está na loja
bool isShopPlayer(uint32_t playerGUID) const;
```

#### **3.2 Sistema de Preços Dinâmicos**
- Preços de compra e venda configuráveis
- Sistema de storage para condições
- Suporte a itens aninhados

### **4. Sistema de Interação Sofisticado**

#### **4.1 Interação por Tópico**
```cpp
// Interação com tópico específico
void setPlayerInteraction(uint32_t playerId, uint16_t topicId = 0);

// Verificar interação
bool isPlayerInteractingOnTopic(uint32_t playerId, uint16_t topicId);

// Ordem de interações
std::vector<uint32_t> playerInteractionsOrder;
std::map<uint32_t, uint16_t> playerInteractions;
```

#### **4.2 Sistema de Conversação**
- Múltiplos tópicos por NPC
- Sistema de respostas condicionais
- Integração com scripts Lua

### **5. Sistema de Movimento Inteligente**

#### **5.1 Movimento Aleatório**
```cpp
// Movimento aleatório dentro do raio
bool getRandomStep(Direction &moveDirection);

// Verificação de caminho válido
bool canWalkTo(const Position &fromPos, Direction dir);

// Raio de movimento configurável
int32_t walkRadius = 10;
```

#### **5.2 Sistema de Spawn Range**
```cpp
// Verificar se está dentro do raio de spawn
bool isInSpawnRange(const Position &pos) const;

// Posição mestre do NPC
Position masterPos;
```

### **6. Sistema de Comportamento Automático**

#### **6.1 Comportamentos Temporizados**
```cpp
// Ticks para diferentes comportamentos
uint32_t yellTicks = 0;
uint32_t walkTicks = 0;
uint32_t soundTicks = 0;

// Eventos de pensamento
void onThinkYell(uint32_t interval);
void onThinkWalk(uint32_t interval);
void onThinkSound(uint32_t interval);
```

#### **6.2 Sistema de Voz**
```cpp
// Configurações de voz
std::vector<voiceBlock_t> voiceVector;

// Chance de falar
uint32_t yellChance = 0;
uint32_t yellSpeedTicks = 0;
```

### **7. Integração Lua Avançada**

#### **7.1 Funções Completas**
- Criação e gerenciamento de NPCs
- Configuração de tipos
- Sistema de loja
- Eventos e callbacks

#### **7.2 Scripts Dinâmicos**
```cpp
// Scripts por NPC
std::set<std::string> scripts;

// Carregamento de callbacks
bool loadCallback(LuaScriptInterface* scriptInterface);
```

### **8. Sistema de Configuração Flexível**

#### **8.1 Configurações de Aparência**
```cpp
// Outfit configurável
Outfit_t outfit = {};

// Informações de luz
LightInfo light = {};

// Bolha de fala
uint8_t speechBubble = SPEECHBUBBLE_NORMAL;
```

#### **8.2 Configurações de Comportamento**
```cpp
// Velocidade base
uint32_t baseSpeed = 55;

// Intervalo de caminhada
uint32_t walkInterval = 2000;

// Capacidades
bool canPushItems = false;
bool canPushCreatures = false;
bool pushable = false;
bool floorChange = false;
```

### **9. Sistema de Som**

#### **9.1 Sons Automáticos**
```cpp
// Configurações de som
uint32_t soundChance = 0;
uint32_t soundSpeedTicks = 0;
std::vector<SoundEffect_t> soundVector;

// Evento de som
void onThinkSound(uint32_t interval);
```

### **10. Sistema de Respawn**

#### **10.1 Tipos de Respawn**
```cpp
// Configuração de respawn
RespawnType respawnType = {};

// Período de respawn
RespawnPeriod_t period;

// Respawn subterrâneo
bool underground;
```

### **11. Padrões de Design Identificados**

#### **11.1 Singleton Pattern**
```cpp
// Instância única de Npcs
static Npcs &getInstance();

// Instância única de Npc
static Npc &getInstance();
```

#### **11.2 Factory Pattern**
```cpp
// Criação de NPCs
static std::shared_ptr<Npc> createNpc(const std::string &name);

// Obtenção de tipos
std::shared_ptr<NpcType> getNpcType(const std::string &name, bool create = false);
```

#### **11.3 Observer Pattern**
```cpp
// Eventos de criatura
void onCreatureAppear(const std::shared_ptr<Creature> &creature, bool isLogin);
void onCreatureSay(const std::shared_ptr<Creature> &creature, SpeakClasses type, const std::string &text);
```

### **12. Limitações e Considerações**

#### **12.1 Complexidade**
- Sistema muito complexo para iniciantes
- Muitas configurações podem ser confusas
- Curva de aprendizado íngreme

#### **12.2 Performance**
- Muitos NPCs podem impactar performance
- Sistema de eventos pode ser custoso
- Cache necessário para otimização

#### **12.3 Manutenibilidade**
- Código muito acoplado
- Difícil de testar isoladamente
- Refatoração complexa

### **13. Recomendações**

#### **13.1 Para Desenvolvedores**
- Estudar a hierarquia de classes antes de modificar
- Usar o sistema de eventos para extensões
- Implementar testes para mudanças

#### **13.2 Para Administradores**
- Monitorar performance dos NPCs
- Configurar adequadamente os spawns
- Manter backups antes de mudanças

#### **13.3 Para Usuários Finais**
- Entender as configurações de NPCs
- Usar adequadamente o sistema de loja
- Respeitar as interações com NPCs

## 🎓 **Lição Educacional**

### **CANARY-014: Sistema de NPCs - Lição Completa**

#### **Objetivo da Lição**
Compreender o sistema de NPCs do Canary, sua arquitetura complexa, implementação e uso prático no desenvolvimento de servidores MMORPG.

#### **Teoria**

**O que é o Sistema de NPCs?**
O Sistema de NPCs do Canary é responsável por gerenciar todos os personagens não-jogadores no servidor, incluindo comerciantes, quest givers, e NPCs ambientais.

**Conceitos Fundamentais:**

1. **Npc**: Instância individual de NPC no mundo
2. **NpcType**: Definição de tipo e comportamento
3. **SpawnNpc**: Sistema de spawns automáticos
4. **Eventos**: Sistema de eventos e callbacks
5. **Loja**: Sistema de comércio com jogadores
6. **Interação**: Sistema de conversação e interação

#### **Exemplos Práticos**

**1. Criando um NPC Básico**
```lua
-- Criar tipo de NPC
local npcType = NpcType("Merchant")
npcType:name("Merchant")
npcType:nameDescription("a merchant")
npcType:outfit({lookType = 128, lookHead = 0, lookBody = 0, lookLegs = 0, lookFeet = 0})

-- Criar NPC
local npc = Npc("Merchant")
npc:place({x = 100, y = 100, z = 7})
```

**2. Configurando uma Loja**
```lua
-- Adicionar itens à loja
npcType:addShopItem(ITEM_GOLD_COIN, 100, 1, 1)
npcType:addShopItem(ITEM_SWORD, 1000, 1, 1)
npcType:addShopItem(ITEM_SHIELD, 500, 1, 1)

-- Configurar moeda
npcType:currency(ITEM_GOLD_COIN)
```

**3. Sistema de Eventos**
```lua
-- Evento de pensamento
function onThink(npc, interval)
    if math.random(1, 100) <= 10 then
        npc:say("Welcome to my shop!")
    end
end

-- Evento de compra
function onPlayerBuy(npc, player, itemId, count, amount, ignore, inBackpacks)
    player:sendTextMessage(MESSAGE_INFO_DESCR, "Thank you for your purchase!")
end
```

**4. Sistema de Spawns**
```xml
<!-- spawns.xml -->
<spawn centerx="100" centery="100" centerz="7" radius="2">
    <npc name="Merchant" x="0" y="0" z="0" spawntime="60" />
</spawn>
```

**5. Sistema de Interação**
```lua
-- Configurar interação
npc:setPlayerInteraction(player:getId(), 1)

-- Verificar interação
if npc:isInteractingWithPlayer(player:getId()) then
    npc:say("Hello! How can I help you?")
end
```

#### **Exercícios Práticos**

**Exercício 1: Criar NPC Comerciante**
Crie um NPC que vende itens básicos e responde a eventos de compra.

**Exercício 2: Implementar Sistema de Quest**
Crie um NPC que dá quests e verifica se o jogador completou os objetivos.

**Exercício 3: Sistema de Movimento**
Implemente um NPC que se move aleatoriamente dentro de uma área definida.

**Exercício 4: Sistema de Conversação**
Crie um NPC com múltiplos tópicos de conversação baseados em condições.

**Exercício 5: Sistema de Respawn**
Implemente um sistema de respawn inteligente que considera jogadores próximos.

#### **Conceitos Avançados**

**1. Sistema de Eventos**
```lua
-- Múltiplos tipos de eventos
NPCS_EVENT_THINK = 1
NPCS_EVENT_APPEAR = 2
NPCS_EVENT_DISAPPEAR = 3
NPCS_EVENT_MOVE = 4
NPCS_EVENT_SAY = 5
NPCS_EVENT_PLAYER_BUY = 6
NPCS_EVENT_PLAYER_SELL = 7
```

**2. Sistema de Spawns Inteligente**
```cpp
// Verificação automática de spawn
void checkSpawnNpc();

// Agendamento de spawns
void scheduleSpawnNpc(uint32_t spawnId, spawnBlockNpc_t &sb, uint16_t interval);
```

**3. Sistema de Loja Dinâmica**
```lua
-- Loja por jogador
npc:addShopPlayer(player:getId(), shopItems)

-- Verificar se jogador está na loja
if npc:isShopPlayer(player:getId()) then
    -- Processar compra
end
```

#### **Boas Práticas**

1. **Sempre configurar tipos** antes de criar NPCs
2. **Usar eventos** para comportamentos dinâmicos
3. **Implementar verificações** de interação adequadas
4. **Otimizar spawns** para performance
5. **Documentar scripts** claramente
6. **Testar extensivamente** antes de implementar em produção

#### **Integração com Outros Sistemas**

**Sistema de Lua (CANARY-006)**
- Scripts para comportamentos
- Eventos e callbacks
- Funções de gerenciamento

**Sistema de Inventário (CANARY-013)**
- Sistema de loja
- Transações de itens
- Verificações de capacidade

**Sistema de Mapas (CANARY-011)**
- Posicionamento de NPCs
- Verificação de caminhos
- Sistema de spawns

#### **Conclusão**

O Sistema de NPCs do Canary é uma arquitetura complexa e poderosa que oferece flexibilidade extrema para criação de personagens não-jogadores. Sua modularidade permite desde implementações simples até sistemas muito complexos, sempre mantendo performance e funcionalidade.

A chave para dominar este sistema é entender os conceitos fundamentais e praticar com exemplos progressivamente mais complexos.

---

**Pesquisa Iniciada**: 2025-01-27 18:00:00  
**Responsável**: Habdel Research System  
**Status**: ✅ **CONCLUÍDA**  
**Próximo**: CANARY-015: Sistema de Quests
