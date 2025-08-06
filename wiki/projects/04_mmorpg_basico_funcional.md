---
tags: [projects, practical, mmorpg, integration, complete, educational, advanced]
aliases: [mmorpg_basico_funcional, basic_mmorpg, complete_integration_project]
type: practical_project
status: active
priority: high
level: advanced
created: 2025-08-05
updated: 2025-08-05
project: 04
course: integration
prerequisites: [01_servidor_basico_npcs, 02_cliente_interface_simples, 03_sistema_chat_completo, 4.3_tratamento_erros, 4.4_estrategias_teste]
next_project: none
---

# 🎮 **Projeto 4: MMORPG Básico Funcional**

## 🎯 **Visão Geral**

Este projeto prático implementa um MMORPG básico funcional que integra todos os conceitos aprendidos nos projetos anteriores. Você criará um jogo completo com servidor, cliente, NPCs, chat, sistema de combate e persistência de dados.

## 📚 **Objetivos do Projeto**

### **🎯 Ao final deste projeto, você será capaz de:**
- ✅ Integrar todos os sistemas em um MMORPG funcional
- ✅ Implementar sistema de combate e progressão
- ✅ Criar sistema de inventário e itens
- ✅ Implementar persistência de dados
- ✅ Criar interface de jogo completa

## 🏗️ **Estrutura do Projeto**

### **📁 Organização dos Arquivos**
```
projeto_mmorpg_completo/
├── server/
│   ├── src/
│   │   ├── main.cpp              # Servidor principal
│   │   ├── GameServer.hpp        # Servidor do jogo
│   │   ├── GameServer.cpp        # Implementação do servidor
│   │   ├── WorldManager.hpp      # Gerenciador do mundo
│   │   ├── WorldManager.cpp      # Implementação do mundo
│   │   ├── PlayerManager.hpp     # Gerenciador de jogadores
│   │   ├── PlayerManager.cpp     # Implementação de jogadores
│   │   ├── CombatSystem.hpp      # Sistema de combate
│   │   ├── CombatSystem.cpp      # Implementação de combate
│   │   ├── ItemSystem.hpp        # Sistema de itens
│   │   ├── ItemSystem.cpp        # Implementação de itens
│   │   ├── DatabaseManager.hpp   # Gerenciador de banco
│   │   └── DatabaseManager.cpp   # Implementação de banco
│   ├── data/
│   │   ├── maps/
│   │   │   ├── world.tmx         # Mapa do mundo
│   │   │   └── spawn.tmx         # Mapa de spawn
│   │   ├── items/
│   │   │   ├── weapons.lua       # Armas
│   │   │   ├── armor.lua         # Armaduras
│   │   │   └── potions.lua       # Poções
│   │   ├── npcs/
│   │   │   ├── monsters.lua      # Monstros
│   │   │   ├── merchants.lua     # Comerciantes
│   │   │   └── quests.lua        # NPCs de missão
│   │   └── config/
│   │       └── server.conf       # Configuração
│   └── scripts/
│       ├── setup_server.sh       # Configuração
│       └── run_server.sh         # Execução
├── client/
│   ├── src/
│   │   ├── main.cpp              # Cliente principal
│   │   ├── GameClient.hpp        # Cliente do jogo
│   │   ├── GameClient.cpp        # Implementação do cliente
│   │   ├── GameUI.hpp            # Interface do jogo
│   │   ├── GameUI.cpp            # Implementação da interface
│   │   ├── Renderer.hpp          # Sistema de renderização
│   │   ├── Renderer.cpp          # Implementação de renderização
│   │   ├── InputManager.hpp      # Gerenciador de entrada
│   │   └── InputManager.cpp      # Implementação de entrada
│   ├── data/
│   │   ├── ui/
│   │   │   ├── game.otui         # Interface principal
│   │   │   ├── inventory.otui    # Interface de inventário
│   │   │   ├── chat.otui         # Interface de chat
│   │   │   └── character.otui    # Interface de personagem
│   │   ├── graphics/
│   │   │   ├── sprites/          # Sprites do jogo
│   │   │   ├── tilesets/         # Tilesets
│   │   │   └── ui/               # Elementos de UI
│   │   └── config/
│   │       └── client.conf       # Configuração
│   └── scripts/
│       ├── setup_client.sh       # Configuração
│       └── run_client.sh         # Execução
└── shared/
    ├── protocol/
    │   ├── GameProtocol.hpp      # Protocolo do jogo
    │   ├── GameProtocol.cpp      # Implementação do protocolo
    │   ├── MessageTypes.hpp      # Tipos de mensagem
    │   └── MessageTypes.cpp      # Implementação dos tipos
    └── utils/
        ├── Logger.hpp            # Sistema de logging
        └── Config.hpp            # Configurações
```

## 🔧 **Implementação**

### **📖 1. Protocolo do Jogo**

#### **🏗️ GameProtocol.hpp**
```cpp
#pragma once
#include <string>
#include <vector>
#include <cstdint>

enum class GameMessageType : uint8_t {
    // Conexão
    CONNECT = 0x01,
    DISCONNECT = 0x02,
    LOGIN = 0x03,
    LOGOUT = 0x04,
    
    // Movimento
    MOVE = 0x10,
    STOP_MOVE = 0x11,
    TELEPORT = 0x12,
    
    // Combate
    ATTACK = 0x20,
    CAST_SPELL = 0x21,
    USE_ITEM = 0x22,
    TAKE_DAMAGE = 0x23,
    
    // Inventário
    PICKUP_ITEM = 0x30,
    DROP_ITEM = 0x31,
    USE_ITEM_INVENTORY = 0x32,
    EQUIP_ITEM = 0x33,
    UNEQUIP_ITEM = 0x34,
    
    // Chat
    SEND_MESSAGE = 0x40,
    RECEIVE_MESSAGE = 0x41,
    
    // Mundo
    SPAWN_PLAYER = 0x50,
    DESPAWN_PLAYER = 0x51,
    SPAWN_NPC = 0x52,
    DESPAWN_NPC = 0x53,
    
    // Interação
    INTERACT_NPC = 0x60,
    TRADE = 0x61,
    QUEST_ACCEPT = 0x62,
    QUEST_COMPLETE = 0x63,
    
    // Sistema
    PING = 0x70,
    PONG = 0x71,
    ERROR = 0xFF
};

struct GameMessage {
    GameMessageType type;
    uint32_t messageId;
    uint32_t timestamp;
    std::string sender;
    std::vector<uint8_t> data;
};

class GameProtocol {
public:
    static std::vector<uint8_t> serialize(const GameMessage& message);
    static GameMessage deserialize(const std::vector<uint8_t>& data);
    
    // Mensagens de conveniência
    static GameMessage createLoginMessage(const std::string& username, const std::string& password);
    static GameMessage createMoveMessage(int x, int y, int direction);
    static GameMessage createAttackMessage(int targetId);
    static GameMessage createPickupItemMessage(int itemId);
    static GameMessage createChatMessage(const std::string& message, const std::string& channel);
    
private:
    static void writeString(std::vector<uint8_t>& data, const std::string& str);
    static std::string readString(const std::vector<uint8_t>& data, size_t& offset);
    static void writeInt(std::vector<uint8_t>& data, int value);
    static int readInt(const std::vector<uint8_t>& data, size_t& offset);
};
```

### **📖 2. Servidor do Jogo**

#### **🏗️ GameServer.hpp**
```cpp
#pragma once
#include <string>
#include <memory>
#include <map>
#include <vector>
#include <thread>
#include <atomic>

class WorldManager;
class PlayerManager;
class CombatSystem;
class ItemSystem;
class DatabaseManager;
class Logger;

struct Player {
    int id;
    std::string username;
    int x, y;
    int health, maxHealth;
    int mana, maxMana;
    int level;
    int experience;
    std::vector<int> inventory;
    std::map<std::string, int> equipment;
};

class GameServer {
private:
    std::unique_ptr<WorldManager> worldManager;
    std::unique_ptr<PlayerManager> playerManager;
    std::unique_ptr<CombatSystem> combatSystem;
    std::unique_ptr<ItemSystem> itemSystem;
    std::unique_ptr<DatabaseManager> databaseManager;
    std::unique_ptr<Logger> logger;
    
    std::map<int, std::unique_ptr<Player>> players;
    std::map<int, int> playerSockets; // socket -> playerId
    
    int serverSocket;
    std::atomic<bool> running;
    std::thread acceptThread;
    
    int port;
    std::string serverName;
    
public:
    GameServer();
    ~GameServer();
    
    bool initialize(const std::string& configFile);
    void start();
    void stop();
    bool isRunning() const { return running; }
    
    // Gerenciamento de jogadores
    bool playerLogin(const std::string& username, const std::string& password, int socket);
    void playerLogout(int playerId);
    void playerDisconnect(int socket);
    
    // Processamento de mensagens
    void processMessage(int socket, const GameMessage& message);
    void broadcastToNearbyPlayers(int playerId, const GameMessage& message);
    
private:
    bool loadConfig(const std::string& configFile);
    void setupLogging();
    void setupNetworking();
    void setupSystems();
    void acceptConnections();
    void handleClientMessages(int socket);
    
    // Handlers de mensagens
    void handleLogin(int socket, const GameMessage& message);
    void handleMove(int socket, const GameMessage& message);
    void handleAttack(int socket, const GameMessage& message);
    void handlePickupItem(int socket, const GameMessage& message);
    void handleChat(int socket, const GameMessage& message);
};
```

### **📖 3. Sistema de Combate**

#### **🏗️ CombatSystem.hpp**
```cpp
#pragma once
#include <vector>
#include <map>
#include <memory>

struct CombatAction {
    int attackerId;
    int targetId;
    std::string actionType;
    int damage;
    bool critical;
    uint32_t timestamp;
};

struct CombatStats {
    int attack;
    int defense;
    int criticalChance;
    int criticalMultiplier;
    int accuracy;
    int dodge;
};

class CombatSystem {
private:
    std::vector<CombatAction> combatLog;
    std::map<int, CombatStats> playerStats;
    
public:
    CombatSystem();
    ~CombatSystem();
    
    // Combate
    CombatAction performAttack(int attackerId, int targetId);
    CombatAction performSpell(int casterId, int targetId, const std::string& spellName);
    bool isInCombatRange(int attackerId, int targetId);
    
    // Estatísticas
    void setPlayerStats(int playerId, const CombatStats& stats);
    CombatStats getPlayerStats(int playerId);
    void updateStatsFromEquipment(int playerId, const std::map<std::string, int>& equipment);
    
    // Log
    void addCombatAction(const CombatAction& action);
    std::vector<CombatAction> getRecentCombatLog(int count = 10);
    void clearCombatLog();
    
private:
    int calculateDamage(int attackerId, int targetId, bool isSpell = false);
    bool isCriticalHit(int attackerId);
    bool isHit(int attackerId, int targetId);
    int getRandomValue(int min, int max);
};
```

### **📖 4. Sistema de Itens**

#### **🏗️ ItemSystem.hpp**
```cpp
#pragma once
#include <string>
#include <vector>
#include <map>

enum class ItemType {
    WEAPON,
    ARMOR,
    POTION,
    MATERIAL,
    QUEST
};

struct Item {
    int id;
    std::string name;
    std::string description;
    ItemType type;
    int weight;
    int value;
    bool stackable;
    int maxStack;
    
    // Propriedades específicas
    std::map<std::string, int> properties;
};

class ItemSystem {
private:
    std::map<int, Item> itemDatabase;
    std::map<int, std::vector<int>> playerInventories; // playerId -> itemIds
    
public:
    ItemSystem();
    ~ItemSystem();
    
    // Gerenciamento de itens
    bool loadItemDatabase(const std::string& filePath);
    Item getItem(int itemId);
    bool itemExists(int itemId);
    
    // Inventário
    bool addItemToInventory(int playerId, int itemId, int count = 1);
    bool removeItemFromInventory(int playerId, int itemId, int count = 1);
    bool hasItem(int playerId, int itemId, int count = 1);
    std::vector<std::pair<int, int>> getPlayerInventory(int playerId); // itemId, count
    
    // Equipamento
    bool equipItem(int playerId, int itemId, const std::string& slot);
    bool unequipItem(int playerId, const std::string& slot);
    std::map<std::string, int> getPlayerEquipment(int playerId);
    
    // Criação de itens
    Item createWeapon(int id, const std::string& name, int attack, int durability);
    Item createArmor(int id, const std::string& name, int defense, const std::string& slot);
    Item createPotion(int id, const std::string& name, int healAmount);
    
private:
    void savePlayerInventory(int playerId);
    void loadPlayerInventory(int playerId);
};
```

### **📖 5. Cliente do Jogo**

#### **🏗️ GameClient.hpp**
```cpp
#pragma once
#include <string>
#include <memory>
#include <vector>
#include <thread>
#include <atomic>

class NetworkManager;
class GameUI;
class Renderer;
class InputManager;
class Logger;

struct GameState {
    int playerId;
    std::string playerName;
    int x, y;
    int health, maxHealth;
    int mana, maxMana;
    int level;
    int experience;
    std::vector<std::pair<int, int>> inventory; // itemId, count
    std::map<std::string, int> equipment;
};

class GameClient {
private:
    std::unique_ptr<NetworkManager> networkManager;
    std::unique_ptr<GameUI> gameUI;
    std::unique_ptr<Renderer> renderer;
    std::unique_ptr<InputManager> inputManager;
    std::unique_ptr<Logger> logger;
    
    GameState gameState;
    std::vector<GameState> nearbyPlayers;
    std::vector<std::string> chatMessages;
    
    std::atomic<bool> connected;
    std::atomic<bool> loggedIn;
    std::thread receiveThread;
    
public:
    GameClient();
    ~GameClient();
    
    bool initialize(const std::string& configFile);
    void run();
    void shutdown();
    
    // Conexão
    bool connectToServer(const std::string& address, int port);
    bool login(const std::string& username, const std::string& password);
    void disconnect();
    bool isConnected() const { return connected; }
    bool isLoggedIn() const { return loggedIn; }
    
    // Ações do jogo
    bool move(int direction);
    bool attack(int targetId);
    bool pickupItem(int itemId);
    bool useItem(int itemId);
    bool sendChatMessage(const std::string& message);
    
    // Interface
    void showUI();
    void hideUI();
    void updateUI();
    
    // Getters
    const GameState& getGameState() const { return gameState; }
    const std::vector<GameState>& getNearbyPlayers() const { return nearbyPlayers; }
    const std::vector<std::string>& getChatMessages() const { return chatMessages; }
    
private:
    bool loadConfig(const std::string& configFile);
    void setupLogging();
    void setupUI();
    void setupRenderer();
    void setupInput();
    void receiveMessages();
    void processMessage(const GameMessage& message);
    void updateGameState(const GameMessage& message);
};
```

### **📖 6. Interface do Jogo**

#### **🏗️ GameUI.hpp**
```cpp
#pragma once
#include <string>
#include <vector>
#include <memory>
#include <functional>

class GameClient;
class Widget;

class GameUI {
private:
    GameClient* client;
    std::vector<std::unique_ptr<Widget>> widgets;
    
    // Áreas da interface
    std::unique_ptr<Widget> mainWindow;
    std::unique_ptr<Widget> gameArea;
    std::unique_ptr<Widget> statusBar;
    std::unique_ptr<Widget> inventoryWindow;
    std::unique_ptr<Widget> chatWindow;
    std::unique_ptr<Widget> characterWindow;
    
    bool inventoryVisible;
    bool chatVisible;
    bool characterVisible;
    
public:
    GameUI(GameClient* client);
    ~GameUI();
    
    void show();
    void hide();
    bool isVisible() const;
    
    // Gerenciamento de janelas
    void showInventory();
    void hideInventory();
    void toggleInventory();
    
    void showChat();
    void hideChat();
    void toggleChat();
    
    void showCharacter();
    void hideCharacter();
    void toggleCharacter();
    
    // Atualizações
    void updateStatusBar();
    void updateInventory();
    void updateChat();
    void updateCharacter();
    void addChatMessage(const std::string& message);
    
    // Eventos
    void onKeyPress(int key);
    void onMouseClick(int x, int y, int button);
    void onMouseMove(int x, int y);
    
private:
    void setupUI();
    void loadLayout();
    void setupEventHandlers();
    void updateGameArea();
    void renderPlayer();
    void renderNearbyPlayers();
    void renderUI();
};
```

### **📖 7. Layout da Interface**

#### **🏗️ game.otui**
```otui
MainWindow
  id: game_window
  size: 1024 768
  @onEscape: self:close()
  
  Panel
    id: game_area
    size: 800 600
    pos: 0 0
    background-color: black
    @onMouseClick: self:getParent():onGameAreaClick(x, y, button)
    @onMouseMove: self:getParent():onGameAreaMove(x, y)
    
  Panel
    id: status_bar
    size: 1024 50
    pos: 0 600
    background-color: #2a2a2a
    
    Label
      id: health_label
      text: "Vida: 100/100"
      font: verdana-11px-antialised
      color: #00ff00
      pos: 10 15
      
    Label
      id: mana_label
      text: "Mana: 50/50"
      font: verdana-11px-antialised
      color: #0000ff
      pos: 150 15
      
    Label
      id: level_label
      text: "Nível: 1"
      font: verdana-11px-antialised
      color: white
      pos: 250 15
      
    Label
      id: experience_label
      text: "Exp: 0/100"
      font: verdana-11px-antialised
      color: #ffff00
      pos: 350 15
      
  Panel
    id: sidebar
    size: 224 600
    pos: 800 0
    background-color: #2a2a2a
    
    Button
      id: inventory_button
      text: "Inventário"
      font: verdana-11px-antialised
      size: 200 30
      pos: 12 10
      @onClick: self:getParent():toggleInventory()
      
    Button
      id: character_button
      text: "Personagem"
      font: verdana-11px-antialised
      size: 200 30
      pos: 12 50
      @onClick: self:getParent():toggleCharacter()
      
    Button
      id: chat_button
      text: "Chat"
      font: verdana-11px-antialised
      size: 200 30
      pos: 12 90
      @onClick: self:getParent():toggleChat()
      
    Panel
      id: quick_slots
      size: 200 200
      pos: 12 130
      background-color: #1a1a1a
      
      Label
        id: quick_slots_label
        text: "Slots Rápidos"
        font: verdana-11px-antialised
        color: white
        pos: 10 10
        
  Panel
    id: inventory_window
    size: 400 300
    pos: 312 234
    background-color: #3a3a3a
    visible: false
    
    Label
      id: inventory_title
      text: "Inventário"
      font: verdana-11px-antialised
      color: white
      pos: 10 10
      
    Button
      id: close_inventory_button
      text: "X"
      font: verdana-11px-antialised
      size: 20 20
      pos: 370 10
      @onClick: self:getParent():hideInventory()
      
    Grid
      id: inventory_grid
      size: 380 250
      pos: 10 40
      columns: 8
      rows: 6
      
  Panel
    id: chat_window
    size: 400 300
    pos: 312 234
    background-color: #3a3a3a
    visible: false
    
    Label
      id: chat_title
      text: "Chat"
      font: verdana-11px-antialised
      color: white
      pos: 10 10
      
    Button
      id: close_chat_button
      text: "X"
      font: verdana-11px-antialised
      size: 20 20
      pos: 370 10
      @onClick: self:getParent():hideChat()
      
    ScrollablePanel
      id: chat_messages
      size: 380 220
      pos: 10 40
      vertical-scrollbar: true
      background-color: #1a1a1a
      
    TextEdit
      id: chat_input
      text: ""
      font: verdana-11px-antialised
      size: 300 25
      pos: 10 270
      @onKeyPress: self:getParent():onChatKeyPress(key)
      
    Button
      id: send_chat_button
      text: "Enviar"
      font: verdana-11px-antialised
      size: 70 25
      pos: 320 270
      @onClick: self:getParent():onSendChatClicked()
```

## 🎯 **Exercícios Práticos**

### **🔧 Exercício 1: Sistema de Missões**
Implemente um sistema completo de missões:

```cpp
// Template para implementação
class QuestSystem {
public:
    struct Quest {
        int id;
        std::string title;
        std::string description;
        std::vector<std::string> objectives;
        std::map<std::string, int> rewards;
        bool repeatable;
    };
    
    struct PlayerQuest {
        int questId;
        std::string status; // "active", "completed", "failed"
        std::vector<int> progress;
        uint32_t startTime;
    };
    
    bool acceptQuest(int playerId, int questId);
    bool completeQuest(int playerId, int questId);
    bool updateQuestProgress(int playerId, int questId, int objectiveIndex, int progress);
    std::vector<PlayerQuest> getPlayerQuests(int playerId);
};
```

### **🔧 Exercício 2: Sistema de Crafting**
Implemente sistema de criação de itens:

```cpp
// Template para implementação
class CraftingSystem {
public:
    struct Recipe {
        int id;
        std::string name;
        std::map<int, int> ingredients; // itemId, count
        int resultItemId;
        int resultCount;
        int requiredLevel;
        std::string requiredSkill;
    };
    
    bool canCraft(int playerId, int recipeId);
    bool craftItem(int playerId, int recipeId);
    std::vector<Recipe> getAvailableRecipes(int playerId);
    void addRecipe(const Recipe& recipe);
};
```

### **🔧 Exercício 3: Sistema de Clãs**
Implemente sistema de clãs e guildas:

```cpp
// Template para implementação
class ClanSystem {
public:
    struct Clan {
        int id;
        std::string name;
        std::string description;
        int leaderId;
        std::vector<int> members;
        int level;
        int experience;
        std::map<std::string, int> permissions;
    };
    
    bool createClan(int leaderId, const std::string& name);
    bool joinClan(int playerId, int clanId);
    bool leaveClan(int playerId);
    bool promoteMember(int clanId, int playerId, const std::string& rank);
    Clan getClan(int clanId);
};
```

## 📊 **Avaliação e Verificação**

### **✅ Checklist de Conclusão**
- [ ] Servidor MMORPG compila e executa
- [ ] Cliente conecta e faz login
- [ ] Sistema de movimento funciona
- [ ] Sistema de combate implementado
- [ ] Sistema de inventário funcional
- [ ] Chat integrado ao jogo
- [ ] NPCs interativos
- [ ] Persistência de dados
- [ ] Interface responsiva

### **🎯 Critérios de Avaliação**
- **Funcionalidade**: Jogo é jogável
- **Integração**: Todos os sistemas funcionam juntos
- **Performance**: Jogo roda suavemente
- **Interface**: UI é intuitiva e responsiva
- **Persistência**: Dados são salvos corretamente
- **Escalabilidade**: Suporta múltiplos jogadores

## 🔗 **Links Relacionados**

### **📚 Projetos Pré-requisitos**
- [[01_servidor_basico_npcs|Projeto 1: Servidor Básico com NPCs]]
- [[02_cliente_interface_simples|Projeto 2: Cliente com Interface Simples]]
- [[03_sistema_chat_completo|Projeto 3: Sistema de Chat Completo]]

### **📚 Módulos Relacionados**
- [[../modules/04_integration/4.3_tratamento_erros|Módulo 4.3: Tratamento de Erros]]
- [[../modules/04_integration/4.4_estrategias_teste|Módulo 4.4: Estratégias de Teste]]

### **🔗 Documentação Técnica**
- [[../../habdel/INTEGRATION-001|INTEGRATION-001: Comparação de Arquiteturas]]
- [[../../habdel/INTEGRATION-002|INTEGRATION-002: Análise de Protocolos]]

## 📝 **Notas de Implementação**

### **⚠️ Considerações Importantes**
1. **Performance**: Otimize para múltiplos jogadores simultâneos
2. **Sincronização**: Mantenha estado consistente entre cliente e servidor
3. **Segurança**: Implemente validação de dados no servidor
4. **Escalabilidade**: Design para crescimento futuro

### **🔧 Melhorias Futuras**
- Sistema de PvP
- Dungeons e raids
- Sistema de economia
- Crafting avançado
- Sistema de pets
- Eventos sazonais

---

> [!success] **Projeto Concluído**
> ✅ **Status**: Projeto 4 - MMORPG Básico Funcional
> 🎯 **Próximo**: Task 23.6 - Sistema de Navegação e Índices
> 📚 **Nível**: Avançado 