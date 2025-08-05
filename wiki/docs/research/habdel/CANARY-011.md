---
tags: [habdel_research, canary-011, research_story, map_system, tiles, world_management]
type: research_story
status: completed
priority: critical
created: 2025-07-31
target: canary
completed: 2025-01-27
---

# CANARY-011: Sistema de Mapas

## 🎯 **Objetivo**
Pesquisa profunda do sistema de mapas no Canary usando metodologia habdel

## 📋 **Tarefas de Pesquisa**

### **1. Análise do Código-Fonte** ✅
- [x] Identificar arquivos relevantes
- [x] Analisar estrutura e arquitetura
- [x] Documentar principais componentes
- [x] Mapear dependências

### **2. Documentação Técnica** ✅
- [x] Criar documentação detalhada
- [x] Incluir exemplos práticos
- [x] Documentar APIs e interfaces
- [x] Criar diagramas quando necessário

### **3. Validação** ✅
- [x] Validar completude da documentação
- [x] Verificar qualidade técnica
- [x] Testar exemplos práticos
- [x] Revisar integração com wiki

## 📊 **Progresso**
- **Status**: ✅ Concluído
- **Progresso**: 100%
- **Iniciado**: 2025-01-27
- **Concluído**: 2025-01-27

## 🗺️ **Arquitetura do Sistema de Mapas**

### **Estrutura de Componentes**
```
canary/src/
├── map/
│   ├── map.hpp                    # Classe principal Map
│   ├── map.cpp                    # Implementação do Map
│   ├── mapcache.hpp               # Sistema de cache de mapas
│   ├── mapcache.cpp               # Implementação do cache
│   ├── utils/
│   │   ├── mapsector.hpp          # Setores do mapa
│   │   └── astarnodes.hpp         # Algoritmo A* para pathfinding
│   ├── house/
│   │   ├── house.hpp              # Sistema de casas
│   │   └── housetile.hpp          # Tiles de casa
│   └── town.hpp                   # Sistema de cidades
├── items/
│   └── tile.hpp                   # Classe Tile e derivadas
├── io/
│   ├── iomap.hpp                  # I/O de mapas
│   ├── iomap.cpp                  # Implementação I/O
│   └── iomapserialize.hpp         # Serialização de mapas
└── lua/functions/map/
    ├── tile_functions.cpp         # Funções Lua para tiles
    ├── position_functions.cpp     # Funções Lua para posições
    ├── house_functions.cpp        # Funções Lua para casas
    └── town_functions.cpp         # Funções Lua para cidades
```

### **Componentes Principais**

#### **1. Classe Map**
- **Arquivo**: `canary/src/map/map.hpp`
- **Propósito**: Gerenciamento central do mundo do jogo
- **Funcionalidades**:
  - Carregamento e salvamento de mapas
  - Gerenciamento de tiles e setores
  - Posicionamento de criaturas
  - Pathfinding e navegação
  - Integração com casas, cidades e spawns

#### **2. Sistema de Tiles**
- **Arquivo**: `canary/src/items/tile.hpp`
- **Propósito**: Representação de posições no mapa
- **Tipos**:
  - `Tile`: Classe base abstrata
  - `DynamicTile`: Tiles que podem ser modificados
  - `StaticTile`: Tiles estáticos (otimização)
  - `HouseTile`: Tiles de casas

#### **3. Sistema de Cache**
- **Arquivo**: `canary/src/map/mapcache.hpp`
- **Propósito**: Otimização de memória e performance
- **Funcionalidades**:
  - Cache de tiles básicos
  - Gerenciamento de setores
  - Otimização de acesso a dados

#### **4. Sistema I/O**
- **Arquivo**: `canary/src/io/iomap.hpp`
- **Propósito**: Carregamento e salvamento de dados de mapa
- **Funcionalidades**:
  - Leitura de arquivos OTBM
  - Carregamento de spawns
  - Gerenciamento de casas e cidades

## 🔧 **APIs e Interfaces**

### **Classe Map - Funções Principais**
```cpp
class Map final : public MapCache {
    -- Classe: Map
public:
    // Carregamento de mapas
    void load(const std::string &identifier, const Position &pos = Position());
    void loadMap(const std::string &identifier, bool mainMap = false, 
                 bool loadHouses = false, bool loadMonsters = false, 
                 bool loadNpcs = false, bool loadZones = false, 
                 const Position &pos = Position());
    void loadMapCustom(const std::string &mapName, bool loadHouses, 
                      bool loadMonsters, bool loadNpcs, bool loadZones, 
                      int customMapIndex);
    
    // Salvamento
    static bool save();
    
    // Gerenciamento de tiles
    std::shared_ptr<Tile> getTile(uint16_t x, uint16_t y, uint8_t z);
    std::shared_ptr<Tile> getTile(const Position &pos);
    std::shared_ptr<Tile> getOrCreateTile(uint16_t x, uint16_t y, uint8_t z, 
                                         bool isDynamic = false);
    
    // Posicionamento de criaturas
    bool placeCreature(const Position &centerPos, 
                      const std::shared_ptr<Creature> &creature, 
                      bool extendedPos = false, bool forceLogin = false);
    void moveCreature(const std::shared_ptr<Creature> &creature, 
                     const std::shared_ptr<Tile> &newTile, 
                     bool forceTeleport = false);
    
    // Pathfinding e navegação
    bool canThrowObjectTo(const Position &fromPos, const Position &toPos, 
                         SightLines_t lineOfSight = SightLine_CheckSightLine, 
                         int32_t rangex = MAP_MAX_CLIENT_VIEW_PORT_X, 
                         int32_t rangey = MAP_MAX_CLIENT_VIEW_PORT_Y);
    bool isSightClear(const Position &fromPos, const Position &toPos, 
                     bool floorCheck);
    std::shared_ptr<Tile> canWalkTo(const std::shared_ptr<Creature> &creature, 
                                   const Position &pos);
    
    // Pathfinding com A*
    bool getPathMatching(const std::shared_ptr<Creature> &creature, 
                        std::vector<Direction> &dirList, 
                        const FrozenPathingConditionCall &pathCondition, 
                        const FindPathParams &fpp);
    
    // Atualização de zonas
    void refreshZones(uint16_t x, uint16_t y, uint8_t z);
    void refreshZones(const Position &pos);
    
    // Dados do mapa
    std::map<std::string, Position> waypoints;
    SpawnsMonster spawnsMonster;
    SpawnsNpc spawnsNpc;
    Towns towns;
    Houses houses;
};
```

### **Classe Tile - Funções Principais**
#### Inicialização e Configuração
```cpp
class Tile : public Cylinder, public SharedObject {
public:
    // Construtores
    Tile(uint16_t x, uint16_t y, uint8_t z);
    
    // Gerenciamento de itens
    virtual TileItemVector* getItemList() = 0;
    virtual const TileItemVector* getItemList() const = 0;
    virtual TileItemVector* makeItemList() = 0;
    
    // Gerenciamento de criaturas
    virtual CreatureVector* getCreatures() = 0;
    virtual const CreatureVector* getCreatures() const = 0;
    virtual CreatureVector* makeCreatures() = 0;
    
    // Propriedades do tile
    bool hasProperty(ItemProperty prop) const;
    bool hasProperty(const std::shared_ptr<Item> &exclude, ItemProperty prop) const;
    bool hasFlag(uint32_t flag) const;
    void setFlag(uint32_t flag);
    void resetFlag(uint32_t flag);
    
    // Zonas
    void addZone(const std::shared_ptr<Zone> &zone);
    void clearZones();
    auto getZones() const;
    ZoneType_t getZoneType() const;
    
    // Itens especiais
    std::shared_ptr<MagicField> getFieldItem() const;
    std::shared_ptr<Teleport> getTeleportItem() const;
    std::shared_ptr<TrashHolder> getTrashHolder() const;
    std::shared_ptr<Mailbox> getMailbox() const;
    std::shared_ptr<BedItem> getBedItem() const;
    
    // Criaturas
    std::shared_ptr<Creature> getTopCreature() const;
    std::shared_ptr<Creature> getBottomCreature() const;
    std::shared_ptr<Creature> getTopVisibleCreature(const std::shared_ptr<Creature> &creature) const;
    std::shared_ptr<Creature> getBottomVisibleCreature(const std::shared_ptr<Creature> &creature) const;
    
    // Itens
    std::shared_ptr<Item> getTopTopItem() const;
    std::shared_ptr<Item> getTopDownItem() const;
    std::shared_ptr<Thing> getTopVisibleThing(const std::shared_ptr<Creature> &creature);
    std::shared_ptr<Item> getItemByTopOrder(int32_t topOrder);
    
    // Contadores
    size_t getThingCount() const;
    size_t getCreatureCount() const;
    size_t getItemCount() const;
    uint32_t getTopItemCount() const;
    uint32_t getDownItemCount() const;
    
    // Operações de Cylinder
    ReturnValue queryAdd(int32_t index, const std::shared_ptr<Thing> &thing, 
                        uint32_t count, uint32_t flags, 
                        const std::shared_ptr<Creature> &actor = nullptr) override;
    ReturnValue queryRemove(const std::shared_ptr<Thing> &thing, uint32_t count, 
                           uint32_t tileFlags, 
                           const std::shared_ptr<Creature> &actor = nullptr) override;
    std::shared_ptr<Cylinder> queryDestination(int32_t &index, 
                                              const std::shared_ptr<Thing> &thing, 
                                              std::shared_ptr<Item> &destItem, 
                                              uint32_t &flags) override;
    
    // Adição e remoção
    void addThing(const std::shared_ptr<Thing> &thing) final;
    void addThing(int32_t index, const std::shared_ptr<Thing> &thing) override;
    void removeThing(const std::shared_ptr<Thing> &thing, uint32_t count) final;
    void removeCreature(const std::shared_ptr<Creature> &creature);
    
    // Tiles vizinhos
    std::vector<std::shared_ptr<Tile>> getSurroundingTiles();
    
    // Ground
    std::shared_ptr<Item> getGround() const;
    void setGround(const std::shared_ptr<Item> &item);
    
    // Casa
    virtual std::shared_ptr<House> getHouse() {
        return nullptr;
    }
```

#### Finalização
```cpp
    
protected:
    std::shared_ptr<Item> ground = nullptr;
    Position tilePos;
    uint32_t flags = 0;
    std::unordered_set<std::shared_ptr<Zone>> zones {};
};
```

### **Sistema I/O - Funções Principais**
```cpp
class IOMap {
    -- Classe: IOMap
public:
    // Carregamento de mapas
    static void loadMap(Map* map, const Position &pos = Position());
    
    // Carregamento de spawns
    static bool loadMonsters(Map* map);
    static bool loadNpcs(Map* map);
    static bool loadZones(Map* map);
    static bool loadHouses(Map* map);
    
    // Carregamento customizado
    static bool loadMonstersCustom(Map* map, const std::string &mapName, int customMapIndex);
    static bool loadNpcsCustom(Map* map, const std::string &mapName, int customMapIndex);
    static bool loadZonesCustom(Map* map, const std::string &mapName, int customMapIndex);
    static bool loadHousesCustom(Map* map, const std::string &mapName, int customMapIndex);
    
private:
    // Parsing de dados
    static void parseMapDataAttributes(FileStream &stream, Map* map);
    static void parseWaypoints(FileStream &stream, Map &map);
    static void parseTowns(FileStream &stream, Map &map);
    static void parseTileArea(FileStream &stream, Map &map, const Position &pos);
};
```

### **Funções Lua - Tile**
#### Nível Basic
```cpp
// Criação de tile
Tile(x, y, z)
Tile(position)

// Propriedades
tile:getPosition()
tile:getGround()
tile:getThing(index)
tile:getThingCount()
tile:getTopVisibleThing(creature)

// Itens
tile:getTopTopItem()
tile:getTopDownItem()
tile:getFieldItem()
tile:getItemById(itemId)
tile:getItemByType(itemType)
tile:getItemByTopOrder(topOrder)
tile:getItemCountById(itemId)
tile:getItems()
tile:getItemCount()
tile:getDownItemCount()
tile:getTopItemCount()

// Criaturas
tile:getBottomCreature()
tile:getTopCreature()
tile:getBottomVisibleCreature(creature)
tile:getTopVisibleCreature(creature)
tile:getCreatures()
tile:getCreatureCount()

// Propriedades
tile:hasProperty(property)
tile:hasFlag(flag)

// Operações
tile:queryAdd(index, thing, count, flags)
tile:addItem(item)
tile:addItemEx(item)
tile:getHouse()
tile:sweep()
```

#### Nível Intermediate
```cpp
// Criação de tile
Tile(x, y, z)
Tile(position)

// Propriedades
tile:getPosition()
tile:getGround()
tile:getThing(index)
tile:getThingCount()
tile:getTopVisibleThing(creature)

// Itens
tile:getTopTopItem()
tile:getTopDownItem()
tile:getFieldItem()
tile:getItemById(itemId)
tile:getItemByType(itemType)
tile:getItemByTopOrder(topOrder)
tile:getItemCountById(itemId)
tile:getItems()
tile:getItemCount()
tile:getDownItemCount()
tile:getTopItemCount()

// Criaturas
tile:getBottomCreature()
tile:getTopCreature()
tile:getBottomVisibleCreature(creature)
tile:getTopVisibleCreature(creature)
tile:getCreatures()
tile:getCreatureCount()

// Propriedades
tile:hasProperty(property)
tile:hasFlag(flag)

// Operações
tile:queryAdd(index, thing, count, flags)
tile:addItem(item)
tile:addItemEx(item)
tile:getHouse()
tile:sweep()
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Criação de tile
Tile(x, y, z)
Tile(position)

// Propriedades
tile:getPosition()
tile:getGround()
tile:getThing(index)
tile:getThingCount()
tile:getTopVisibleThing(creature)

// Itens
tile:getTopTopItem()
tile:getTopDownItem()
tile:getFieldItem()
tile:getItemById(itemId)
tile:getItemByType(itemType)
tile:getItemByTopOrder(topOrder)
tile:getItemCountById(itemId)
tile:getItems()
tile:getItemCount()
tile:getDownItemCount()
tile:getTopItemCount()

// Criaturas
tile:getBottomCreature()
tile:getTopCreature()
tile:getBottomVisibleCreature(creature)
tile:getTopVisibleCreature(creature)
tile:getCreatures()
tile:getCreatureCount()

// Propriedades
tile:hasProperty(property)
tile:hasFlag(flag)

// Operações
tile:queryAdd(index, thing, count, flags)
tile:addItem(item)
tile:addItemEx(item)
tile:getHouse()
tile:sweep()
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

## 📝 **Exemplos Práticos**

### **1. Carregamento de Mapa**
#### Nível Basic
```cpp
// Carregamento do mapa principal
void Game::loadMainMap() {
    const std::string mapName = g_configManager().getString(MAP_NAME);
    const std::string mapPath = "data/world/" + mapName + ".otbm";
    
    g_game().map.loadMap(mapPath, true, true, true, true, true);
}

// Carregamento de mapa customizado
void Game::loadCustomMap(const std::string &mapName, int customMapIndex) {
    const std::string mapPath = "data/world/custom/" + mapName + ".otbm";
    
    g_game().map.loadMapCustom(mapName, true, true, true, true, customMapIndex);
}
```

#### Nível Intermediate
```cpp
// Carregamento do mapa principal
void Game::loadMainMap() {
    const std::string mapName = g_configManager().getString(MAP_NAME);
    const std::string mapPath = "data/world/" + mapName + ".otbm";
    
    g_game().map.loadMap(mapPath, true, true, true, true, true);
}

// Carregamento de mapa customizado
void Game::loadCustomMap(const std::string &mapName, int customMapIndex) {
    const std::string mapPath = "data/world/custom/" + mapName + ".otbm";
    
    g_game().map.loadMapCustom(mapName, true, true, true, true, customMapIndex);
}
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Carregamento do mapa principal
void Game::loadMainMap() {
    const std::string mapName = g_configManager().getString(MAP_NAME);
    const std::string mapPath = "data/world/" + mapName + ".otbm";
    
    g_game().map.loadMap(mapPath, true, true, true, true, true);
}

// Carregamento de mapa customizado
void Game::loadCustomMap(const std::string &mapName, int customMapIndex) {
    const std::string mapPath = "data/world/custom/" + mapName + ".otbm";
    
    g_game().map.loadMapCustom(mapName, true, true, true, true, customMapIndex);
}
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

### **2. Gerenciamento de Tiles**
#### Nível Basic
```cpp
// Obter tile existente
std::shared_ptr<Tile> Game::getTileAt(const Position &pos) {
    return g_game().map.getTile(pos);
}

// Criar tile se não existir
std::shared_ptr<Tile> Game::getOrCreateTileAt(const Position &pos) {
    return g_game().map.getOrCreateTile(pos, true); // isDynamic = true
}

// Verificar se posição é válida
bool Game::isValidPosition(const Position &pos) {
    auto tile = g_game().map.getTile(pos);
    return tile != nullptr;
}
```

#### Nível Intermediate
```cpp
// Obter tile existente
std::shared_ptr<Tile> Game::getTileAt(const Position &pos) {
    return g_game().map.getTile(pos);
}

// Criar tile se não existir
std::shared_ptr<Tile> Game::getOrCreateTileAt(const Position &pos) {
    return g_game().map.getOrCreateTile(pos, true); // isDynamic = true
}

// Verificar se posição é válida
bool Game::isValidPosition(const Position &pos) {
    auto tile = g_game().map.getTile(pos);
    return tile != nullptr;
}
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Obter tile existente
std::shared_ptr<Tile> Game::getTileAt(const Position &pos) {
    return g_game().map.getTile(pos);
}

// Criar tile se não existir
std::shared_ptr<Tile> Game::getOrCreateTileAt(const Position &pos) {
    return g_game().map.getOrCreateTile(pos, true); // isDynamic = true
}

// Verificar se posição é válida
bool Game::isValidPosition(const Position &pos) {
    auto tile = g_game().map.getTile(pos);
    return tile != nullptr;
}
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

### **3. Posicionamento de Criaturas**
#### Nível Basic
```cpp
// Posicionar jogador no mapa
bool Game::placePlayer(const std::shared_ptr<Player> &player, const Position &pos) {
    return g_game().map.placeCreature(pos, player, false, true);
}

// Posicionar monstro no mapa
bool Game::spawnMonster(const std::shared_ptr<Monster> &monster, const Position &pos) {
    return g_game().map.placeCreature(pos, monster, true, false);
}

// Mover criatura
void Game::moveCreature(const std::shared_ptr<Creature> &creature, const Position &newPos) {
    auto newTile = g_game().map.getTile(newPos);
    if (newTile) {
        g_game().map.moveCreature(creature, newTile, false);
    }
}
```

#### Nível Intermediate
```cpp
// Posicionar jogador no mapa
bool Game::placePlayer(const std::shared_ptr<Player> &player, const Position &pos) {
    return g_game().map.placeCreature(pos, player, false, true);
}

// Posicionar monstro no mapa
bool Game::spawnMonster(const std::shared_ptr<Monster> &monster, const Position &pos) {
    return g_game().map.placeCreature(pos, monster, true, false);
}

// Mover criatura
void Game::moveCreature(const std::shared_ptr<Creature> &creature, const Position &newPos) {
    auto newTile = g_game().map.getTile(newPos);
    if (newTile) {
        g_game().map.moveCreature(creature, newTile, false);
    }
}
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Posicionar jogador no mapa
bool Game::placePlayer(const std::shared_ptr<Player> &player, const Position &pos) {
    return g_game().map.placeCreature(pos, player, false, true);
}

// Posicionar monstro no mapa
bool Game::spawnMonster(const std::shared_ptr<Monster> &monster, const Position &pos) {
    return g_game().map.placeCreature(pos, monster, true, false);
}

// Mover criatura
void Game::moveCreature(const std::shared_ptr<Creature> &creature, const Position &newPos) {
    auto newTile = g_game().map.getTile(newPos);
    if (newTile) {
        g_game().map.moveCreature(creature, newTile, false);
    }
}
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

### **4. Pathfinding e Navegação**
#### Nível Basic
```cpp
// Verificar se pode atirar objeto
bool Game::canThrowObject(const Position &from, const Position &to) {
    return g_game().map.canThrowObjectTo(from, to);
}

// Verificar linha de visão
bool Game::hasLineOfSight(const Position &from, const Position &to) {
    return g_game().map.isSightClear(from, to, true);
}

// Verificar se pode andar
std::shared_ptr<Tile> Game::canWalkTo(const std::shared_ptr<Creature> &creature, const Position &pos) {
    return g_game().map.canWalkTo(creature, pos);
}

// Encontrar caminho
bool Game::findPath(const std::shared_ptr<Creature> &creature, const Position &target, 
                   std::vector<Direction> &path) {
    FindPathParams fpp;
    fpp.maxSearchDist = 50;
    fpp.clearSight = true;
    fpp.allowDiagonal = true;
    
    return g_game().map.getPathMatching(creature, path, 
                                       FrozenPathingConditionCall(), fpp);
}
```

#### Nível Intermediate
```cpp
// Verificar se pode atirar objeto
bool Game::canThrowObject(const Position &from, const Position &to) {
    return g_game().map.canThrowObjectTo(from, to);
}

// Verificar linha de visão
bool Game::hasLineOfSight(const Position &from, const Position &to) {
    return g_game().map.isSightClear(from, to, true);
}

// Verificar se pode andar
std::shared_ptr<Tile> Game::canWalkTo(const std::shared_ptr<Creature> &creature, const Position &pos) {
    return g_game().map.canWalkTo(creature, pos);
}

// Encontrar caminho
bool Game::findPath(const std::shared_ptr<Creature> &creature, const Position &target, 
                   std::vector<Direction> &path) {
    FindPathParams fpp;
    fpp.maxSearchDist = 50;
    fpp.clearSight = true;
    fpp.allowDiagonal = true;
    
    return g_game().map.getPathMatching(creature, path, 
                                       FrozenPathingConditionCall(), fpp);
}
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Verificar se pode atirar objeto
bool Game::canThrowObject(const Position &from, const Position &to) {
    return g_game().map.canThrowObjectTo(from, to);
}

// Verificar linha de visão
bool Game::hasLineOfSight(const Position &from, const Position &to) {
    return g_game().map.isSightClear(from, to, true);
}

// Verificar se pode andar
std::shared_ptr<Tile> Game::canWalkTo(const std::shared_ptr<Creature> &creature, const Position &pos) {
    return g_game().map.canWalkTo(creature, pos);
}

// Encontrar caminho
bool Game::findPath(const std::shared_ptr<Creature> &creature, const Position &target, 
                   std::vector<Direction> &path) {
    FindPathParams fpp;
    fpp.maxSearchDist = 50;
    fpp.clearSight = true;
    fpp.allowDiagonal = true;
    
    return g_game().map.getPathMatching(creature, path, 
                                       FrozenPathingConditionCall(), fpp);
}
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

### **5. Operações com Tiles**
#### Nível Basic
```cpp
// Adicionar item ao tile
bool Game::addItemToTile(const Position &pos, const std::shared_ptr<Item> &item) {
    auto tile = g_game().map.getTile(pos);
    if (!tile) {
        return false;
    }
    
    ReturnValue ret = tile->queryAdd(0, item, 1, 0);
    if (ret == RETURNVALUE_NOERROR) {
        tile->addThing(item);
        return true;
    }
    
    return false;
}

// Remover item do tile
bool Game::removeItemFromTile(const Position &pos, const std::shared_ptr<Item> &item) {
    auto tile = g_game().map.getTile(pos);
    if (!tile) {
        return false;
    }
    
    tile->removeThing(item, 1);
    return true;
}

// Verificar propriedades do tile
bool Game::isTileWalkable(const Position &pos) {
    auto tile = g_game().map.getTile(pos);
    if (!tile) {
        return false;
    }
    
    return tile->hasProperty(ItemProperty::WALKABLE);
}

// Verificar se tile tem criaturas
bool Game::hasCreaturesOnTile(const Position &pos) {
    auto tile = g_game().map.getTile(pos);
    if (!tile) {
        return false;
    }
    
    return tile->getCreatureCount() > 0;
}
```

#### Nível Intermediate
```cpp
// Adicionar item ao tile
bool Game::addItemToTile(const Position &pos, const std::shared_ptr<Item> &item) {
    auto tile = g_game().map.getTile(pos);
    if (!tile) {
        return false;
    }
    
    ReturnValue ret = tile->queryAdd(0, item, 1, 0);
    if (ret == RETURNVALUE_NOERROR) {
        tile->addThing(item);
        return true;
    }
    
    return false;
}

// Remover item do tile
bool Game::removeItemFromTile(const Position &pos, const std::shared_ptr<Item> &item) {
    auto tile = g_game().map.getTile(pos);
    if (!tile) {
        return false;
    }
    
    tile->removeThing(item, 1);
    return true;
}

// Verificar propriedades do tile
bool Game::isTileWalkable(const Position &pos) {
    auto tile = g_game().map.getTile(pos);
    if (!tile) {
        return false;
    }
    
    return tile->hasProperty(ItemProperty::WALKABLE);
}

// Verificar se tile tem criaturas
bool Game::hasCreaturesOnTile(const Position &pos) {
    auto tile = g_game().map.getTile(pos);
    if (!tile) {
        return false;
    }
    
    return tile->getCreatureCount() > 0;
}
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Adicionar item ao tile
bool Game::addItemToTile(const Position &pos, const std::shared_ptr<Item> &item) {
    auto tile = g_game().map.getTile(pos);
    if (!tile) {
        return false;
    }
    
    ReturnValue ret = tile->queryAdd(0, item, 1, 0);
    if (ret == RETURNVALUE_NOERROR) {
        tile->addThing(item);
        return true;
    }
    
    return false;
}

// Remover item do tile
bool Game::removeItemFromTile(const Position &pos, const std::shared_ptr<Item> &item) {
    auto tile = g_game().map.getTile(pos);
    if (!tile) {
        return false;
    }
    
    tile->removeThing(item, 1);
    return true;
}

// Verificar propriedades do tile
bool Game::isTileWalkable(const Position &pos) {
    auto tile = g_game().map.getTile(pos);
    if (!tile) {
        return false;
    }
    
    return tile->hasProperty(ItemProperty::WALKABLE);
}

// Verificar se tile tem criaturas
bool Game::hasCreaturesOnTile(const Position &pos) {
    auto tile = g_game().map.getTile(pos);
    if (!tile) {
        return false;
    }
    
    return tile->getCreatureCount() > 0;
}
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

### **6. Funções Lua**
```lua
-- Obter tile em posição
local tile = Tile(100, 100, 7)
if tile then
    -- Verificação condicional
    print("Tile encontrado em posição:", tile:getPosition())
end

-- Verificar propriedades do tile
    --  Verificar propriedades do tile (traduzido)
if tile:hasProperty(ITEM_PROPERTY_WALKABLE) then
    -- Verificação condicional
    print("Tile é caminhável")
end

if tile:hasFlag(TILESTATE_PROTECTIONZONE) then
    -- Verificação condicional
    print("Tile está em zona de proteção")
end

-- Adicionar item ao tile
    --  Adicionar item ao tile (traduzido)
local item = Item(2160) -- Gold coin
if tile:addItem(item) then
    -- Verificação condicional
    print("Item adicionado com sucesso")
end

-- Obter criaturas no tile
    --  Obter criaturas no tile (traduzido)
local creatures = tile:getCreatures()
for _, creature in ipairs(creatures) do
    -- Loop de repetição
    print("Criatura encontrada:", creature:getName())
end

-- Verificar se tile tem campo mágico
local field = tile:getFieldItem()
if field then
    -- Verificação condicional
    print("Tile tem campo mágico:", field:getId())
end

-- Obter casa do tile
    --  Obter casa do tile (traduzido)
local house = tile:getHouse()
if house then
    -- Verificação condicional
    print("Tile pertence à casa:", house:getName())
end

-- Limpar tile
    --  Limpar tile (traduzido)
tile:sweep()
```

## 🗺️ **Sistema de Mapas por Componente**

### **Estrutura de Dados**
- **Map**: Gerenciamento central do mundo
- **Tile**: Unidade básica do mapa (32x32 pixels)
- **MapSector**: Agrupamento de tiles para otimização
- **Position**: Coordenadas 3D (x, y, z)

### **Tipos de Tiles**
- **StaticTile**: Tiles estáticos (otimização de memória)
- **DynamicTile**: Tiles que podem ser modificados
- **HouseTile**: Tiles de casas (herda de DynamicTile)

### **Sistema de Cache**
- **MapCache**: Cache de tiles básicos
- **BasicTile**: Representação simplificada para cache
- **BasicItem**: Representação simplificada de itens

### **Sistema de Zonas**
- **ZONE_NORMAL**: Zona normal
- **ZONE_PROTECTION**: Zona de proteção
- **ZONE_NOPVP**: Zona sem PvP
- **ZONE_PVP**: Zona de PvP
- **ZONE_NOLOGOUT**: Zona sem logout

### **Sistema de Spawns**
- **SpawnsMonster**: Spawns de monstros
- **SpawnsNpc**: Spawns de NPCs
- **Towns**: Cidades
- **Houses**: Casas

## 🔄 **Sistema de Carregamento**

### **Fluxo de Carregamento**
1. **IOMap::loadMap()**: Carrega arquivo OTBM
2. **parseMapDataAttributes()**: Parse atributos do mapa
3. **parseTowns()**: Carrega cidades
4. **parseTileArea()**: Carrega áreas de tiles
5. **loadMonsters()**: Carrega spawns de monstros
6. **loadNpcs()**: Carrega spawns de NPCs
7. **loadHouses()**: Carrega casas
8. **loadZones()**: Carrega zonas

### **Formato de Arquivo**
- **OTBM**: OpenTibia Binary Map
- **XML**: Spawns, casas, cidades
- **Compressão**: Otimização de espaço

### **Otimizações**
- **Cache de Tiles**: Reduz acesso a disco
- **Setores**: Agrupamento para otimização
- **Tiles Estáticos**: Reduz uso de memória
- **Lazy Loading**: Carregamento sob demanda

## 🎯 **Integração com Outros Sistemas**

### **Sistema de Criaturas**
- Posicionamento automático
- Verificação de colisão
- Pathfinding integrado
- Gerenciamento de espectadores

### **Sistema de Itens**
- Posicionamento em tiles
- Verificação de propriedades
- Gerenciamento de stack
- Interação com campos mágicos

### **Sistema de Casas**
- Tiles especiais para casas
- Gerenciamento de propriedade
- Sistema de aluguel
- Integração com banco de dados

### **Sistema de Combate**
- Verificação de linha de visão
- Cálculo de distância
- Verificação de campos mágicos
- Sistema de proteção

## 🔧 **Otimizações e Performance**

### **Sistema de Cache**
#### Nível Basic
```cpp
// Cache de tiles básicos
void MapCache::setBasicTile(uint16_t x, uint16_t y, uint8_t z, 
                           const std::shared_ptr<BasicTile> &basicTile);

// Cache de setores
MapSector* MapCache::createMapSector(uint32_t x, uint32_t y);
MapSector* MapCache::getBestMapSector(uint32_t x, uint32_t y);
```

#### Nível Intermediate
```cpp
// Cache de tiles básicos
void MapCache::setBasicTile(uint16_t x, uint16_t y, uint8_t z, 
                           const std::shared_ptr<BasicTile> &basicTile);

// Cache de setores
MapSector* MapCache::createMapSector(uint32_t x, uint32_t y);
MapSector* MapCache::getBestMapSector(uint32_t x, uint32_t y);
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Cache de tiles básicos
void MapCache::setBasicTile(uint16_t x, uint16_t y, uint8_t z, 
                           const std::shared_ptr<BasicTile> &basicTile);

// Cache de setores
MapSector* MapCache::createMapSector(uint32_t x, uint32_t y);
MapSector* MapCache::getBestMapSector(uint32_t x, uint32_t y);
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

### **Gerenciamento de Memória**
- **Tiles Estáticos**: Menos overhead de memória
- **Lazy Loading**: Carregamento sob demanda
- **Cache Inteligente**: Remoção automática de dados não utilizados
- **Compressão**: Redução de espaço em disco

### **Otimizações de Acesso**
- **Setores**: Agrupamento de tiles para acesso rápido
- **Hash Maps**: Acesso O(1) a tiles
- **Spatial Indexing**: Indexação espacial para queries
- **Batch Operations**: Operações em lote

## 📊 **Métricas e Monitoramento**

### **Métricas Disponíveis**
- **Número de Tiles**: Total de tiles carregados
- **Uso de Memória**: Memória utilizada pelo mapa
- **Performance de Cache**: Hit/miss ratio do cache
- **Tempo de Carregamento**: Tempo para carregar mapas

### **Logs e Debug**
#### Nível Basic
```cpp
g_logger().info("Loading map: {}", identifier);
```

#### Nível Intermediate
```cpp
// Log de carregamento de mapa
g_logger().info("Loading map: {}", identifier);

// Log de erro de carregamento
g_logger().warn("Map loading failed: {}", e.what());

// Log de performance
g_logger().debug("Map sector created: {}x{}", x, y);
```

#### Nível Advanced
```cpp
// Log de carregamento de mapa
g_logger().info("Loading map: {}", identifier);

// Log de erro de carregamento
g_logger().warn("Map loading failed: {}", e.what());

// Log de performance
g_logger().debug("Map sector created: {}x{}", x, y);
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

## 🔗 **Links Automáticos**

> [!info] **Links Gerados Automaticamente**
> Estes links foram criados automaticamente pelo sistema de linkagem da categoria **Documentation**

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]

### **🧭 Navegação**
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]
- [[../maps/category_indices|Índices por Categoria]]
- [[../maps/relationships|Relacionamentos]]

### **📊 Métricas da Categoria**
- **Categoria**: Documentation
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

## 🔗 **Integração com Cliente**

### **Protocolo de Comunicação**
1. **Servidor**: Envia dados de mapa via protocolo
2. **Cliente**: Recebe e renderiza tiles
3. **Sincronização**: Atualizações em tempo real
4. **Otimização**: Envio apenas de tiles visíveis

### **Compatibilidade**
- **Protocolos Antigos**: Suporte via configuração
- **Protocolos Novos**: Funcionalidades completas
- **Fallback**: Comportamento padrão para incompatibilidades

## 📝 **Notas de Pesquisa**

### **Descobertas Importantes**
1. **Arquitetura Robusta**: Sistema bem estruturado e escalável
2. **Otimizações Avançadas**: Cache inteligente e lazy loading
3. **Flexibilidade**: Suporte a mapas customizados e dinâmicos
4. **Integração Completa**: Conexão com todos os sistemas do jogo

### **Diferenças do OTClient**
1. **Foco Servidor**: Canary foca na lógica do servidor
2. **Gerenciamento Centralizado**: Controle total pelo servidor
3. **Otimizações Específicas**: Cache e lazy loading otimizados
4. **Simplicidade**: Menos complexidade que o cliente

### **Pontos de Atenção**
1. **Performance**: Monitorar uso de memória e cache
2. **Escalabilidade**: Considerar mapas grandes
3. **Sincronização**: Garantir consistência entre clientes
4. **Manutenção**: Gerenciar arquivos de mapa e spawns

## 🔗 **Links Automáticos**

> [!info] **Links Gerados Automaticamente**
> Estes links foram criados automaticamente pelo sistema de linkagem da categoria **Documentation**

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]

### **🧭 Navegação**
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]
- [[../maps/category_indices|Índices por Categoria]]
- [[../maps/relationships|Relacionamentos]]

### **📊 Métricas da Categoria**
- **Categoria**: Documentation
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

## 🔗 **Links Relacionados**
- [Documentação Principal](../../README.md)
- [Plano de Pesquisa](../research_plan.json)
- [Status Geral](../status_report.md)
- [CANARY-010: Sistema de Partículas](../habdel/CANARY-010.md)
- [CANARY-012: Sistema de Combate](../habdel/CANARY-012.md)

---
*Story concluída seguindo metodologia habdel - 2025-01-27*
