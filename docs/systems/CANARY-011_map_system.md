---
tags: [canary_lesson, map_system, tiles, world_management, game_development]
type: lesson
status: published
priority: high
created: 2025-01-27
target: canary
---

# CANARY-011: Sistema de Mapas - Lição Educacional

## 🎯 **Objetivo da Lição**
Compreender o sistema de mapas do Canary, sua arquitetura, implementação e uso prático no desenvolvimento de servidores MMORPG.

## 📚 **Teoria**

### **O que é o Sistema de Mapas?**
O Sistema de Mapas do Canary é responsável por gerenciar todo o mundo do jogo, desde o carregamento de mapas até o posicionamento de criaturas e itens. Ele utiliza uma arquitetura baseada em tiles para criar um mundo virtual imersivo e eficiente.

### **Conceitos Fundamentais**

#### **1. Tiles**
- **Definição**: Unidade básica do mapa (32x32 pixels)
- **Propósito**: Representar uma posição específica no mundo
- **Tipos**: Estáticos, Dinâmicos, Casa

#### **2. Sistema de Coordenadas**
- **Position**: Localização 3D (x, y, z)
- **Setores**: Agrupamento de tiles para otimização
- **Cache**: Sistema de cache para performance

#### **3. Carregamento de Mapas**
- **OTBM**: OpenTibia Binary Map (formato binário)
- **XML**: Spawns, casas, cidades (formato texto)
- **Lazy Loading**: Carregamento sob demanda

### **Arquitetura do Sistema**

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Map Class     │    │  Tile System    │    ┌  I/O System     │
│                 │    │                 │    │                 │
│ loadMap()       │───▶│ getTile()       │───▶│ loadOTBM()      │
│ placeCreature() │    │ addThing()      │    │ parseXML()      │
│ getPath()       │    │ hasProperty()   │    │ saveMap()       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  MapCache       │    │  MapSector      │    │  Lua Functions  │
│                 │    │                 │    │                 │
│ setBasicTile()  │    │ getTiles()      │    │ Tile()          │
│ createSector()  │    │ addTile()       │    │ getPosition()   │
│ flush()         │    │ removeTile()    │    │ addItem()       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 💻 **Exemplos Práticos**

### **1. Carregamento de Mapa**

#### Nível Basic
```cpp
// Exemplo 1: Carregamento do mapa principal
void Game::loadMainMap() {
    const std::string mapName = g_configManager().getString(MAP_NAME);
    const std::string mapPath = "data/world/" + mapName + ".otbm";
    
    // Carrega mapa com todos os componentes
    g_game().map.loadMap(mapPath, true, true, true, true, true);
}

// Exemplo 2: Carregamento de mapa customizado
void Game::loadCustomMap(const std::string &mapName, int customMapIndex) {
    const std::string mapPath = "data/world/custom/" + mapName + ".otbm";
    
    // Carrega mapa customizado
    g_game().map.loadMapCustom(mapName, true, true, true, true, customMapIndex);
}

// Exemplo 3: Carregamento seletivo
void Game::loadMapComponents(const std::string &mapPath) {
    // Carrega apenas componentes específicos
    g_game().map.loadMap(mapPath, false, false, true, false, false);
}
```

#### Nível Intermediate
```cpp
// Exemplo 1: Carregamento do mapa principal
void Game::loadMainMap() {
    const std::string mapName = g_configManager().getString(MAP_NAME);
    const std::string mapPath = "data/world/" + mapName + ".otbm";
    
    // Carrega mapa com todos os componentes
    g_game().map.loadMap(mapPath, true, true, true, true, true);
}

// Exemplo 2: Carregamento de mapa customizado
void Game::loadCustomMap(const std::string &mapName, int customMapIndex) {
    const std::string mapPath = "data/world/custom/" + mapName + ".otbm";
    
    // Carrega mapa customizado
    g_game().map.loadMapCustom(mapName, true, true, true, true, customMapIndex);
}

// Exemplo 3: Carregamento seletivo
void Game::loadMapComponents(const std::string &mapPath) {
    // Carrega apenas componentes específicos
    g_game().map.loadMap(mapPath, false, false, true, false, false);
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
// Exemplo 1: Carregamento do mapa principal
void Game::loadMainMap() {
    const std::string mapName = g_configManager().getString(MAP_NAME);
    const std::string mapPath = "data/world/" + mapName + ".otbm";
    
    // Carrega mapa com todos os componentes
    g_game().map.loadMap(mapPath, true, true, true, true, true);
}

// Exemplo 2: Carregamento de mapa customizado
void Game::loadCustomMap(const std::string &mapName, int customMapIndex) {
    const std::string mapPath = "data/world/custom/" + mapName + ".otbm";
    
    // Carrega mapa customizado
    g_game().map.loadMapCustom(mapName, true, true, true, true, customMapIndex);
}

// Exemplo 3: Carregamento seletivo
void Game::loadMapComponents(const std::string &mapPath) {
    // Carrega apenas componentes específicos
    g_game().map.loadMap(mapPath, false, false, true, false, false);
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
// Exemplo 1: Obter tile existente
std::shared_ptr<Tile> Game::getTileAt(const Position &pos) {
    return g_game().map.getTile(pos);
}

// Exemplo 2: Criar tile se não existir
std::shared_ptr<Tile> Game::getOrCreateTileAt(const Position &pos) {
    return g_game().map.getOrCreateTile(pos, true); // isDynamic = true
}

// Exemplo 3: Verificar se posição é válida
bool Game::isValidPosition(const Position &pos) {
    auto tile = g_game().map.getTile(pos);
    return tile != nullptr;
}

// Exemplo 4: Obter tiles vizinhos
std::vector<std::shared_ptr<Tile>> Game::getSurroundingTiles(const Position &pos) {
    auto tile = g_game().map.getTile(pos);
    if (tile) {
        return tile->getSurroundingTiles();
    }
    return {};
}
```

#### Nível Intermediate
```cpp
// Exemplo 1: Obter tile existente
std::shared_ptr<Tile> Game::getTileAt(const Position &pos) {
    return g_game().map.getTile(pos);
}

// Exemplo 2: Criar tile se não existir
std::shared_ptr<Tile> Game::getOrCreateTileAt(const Position &pos) {
    return g_game().map.getOrCreateTile(pos, true); // isDynamic = true
}

// Exemplo 3: Verificar se posição é válida
bool Game::isValidPosition(const Position &pos) {
    auto tile = g_game().map.getTile(pos);
    return tile != nullptr;
}

// Exemplo 4: Obter tiles vizinhos
std::vector<std::shared_ptr<Tile>> Game::getSurroundingTiles(const Position &pos) {
    auto tile = g_game().map.getTile(pos);
    if (tile) {
        return tile->getSurroundingTiles();
    }
    return {};
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
// Exemplo 1: Obter tile existente
std::shared_ptr<Tile> Game::getTileAt(const Position &pos) {
    return g_game().map.getTile(pos);
}

// Exemplo 2: Criar tile se não existir
std::shared_ptr<Tile> Game::getOrCreateTileAt(const Position &pos) {
    return g_game().map.getOrCreateTile(pos, true); // isDynamic = true
}

// Exemplo 3: Verificar se posição é válida
bool Game::isValidPosition(const Position &pos) {
    auto tile = g_game().map.getTile(pos);
    return tile != nullptr;
}

// Exemplo 4: Obter tiles vizinhos
std::vector<std::shared_ptr<Tile>> Game::getSurroundingTiles(const Position &pos) {
    auto tile = g_game().map.getTile(pos);
    if (tile) {
        return tile->getSurroundingTiles();
    }
    return {};
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
    if (newTile) {
            if (g_game().map.placeCreature(pos, creature, false, false)) {
```

#### Nível Intermediate
```cpp
// Exemplo 1: Posicionar jogador no mapa
bool Game::placePlayer(const std::shared_ptr<Player> &player, const Position &pos) {
    return g_game().map.placeCreature(pos, player, false, true);
}

// Exemplo 2: Posicionar monstro no mapa
bool Game::spawnMonster(const std::shared_ptr<Monster> &monster, const Position &pos) {
    return g_game().map.placeCreature(pos, monster, true, false);
}

// Exemplo 3: Mover criatura
void Game::moveCreature(const std::shared_ptr<Creature> &creature, const Position &newPos) {
    auto newTile = g_game().map.getTile(newPos);
    if (newTile) {
        g_game().map.moveCreature(creature, newTile, false);
    }
}

// Exemplo 4: Posicionamento com busca de posição livre
bool Game::placeCreatureNear(const std::shared_ptr<Creature> &creature, const Position &center) {
    // Busca posição livre próxima
    for (int dx = -2; dx <= 2; dx++) {
        for (int dy = -2; dy <= 2; dy++) {
            Position pos = center + Position(dx, dy, 0);
            if (g_game().map.placeCreature(pos, creature, false, false)) {
                return true;
            }
        }
    }
    return false;
}
```

#### Nível Advanced
```cpp
// Exemplo 1: Posicionar jogador no mapa
bool Game::placePlayer(const std::shared_ptr<Player> &player, const Position &pos) {
    return g_game().map.placeCreature(pos, player, false, true);
}

// Exemplo 2: Posicionar monstro no mapa
bool Game::spawnMonster(const std::shared_ptr<Monster> &monster, const Position &pos) {
    return g_game().map.placeCreature(pos, monster, true, false);
}

// Exemplo 3: Mover criatura
void Game::moveCreature(const std::shared_ptr<Creature> &creature, const Position &newPos) {
    auto newTile = g_game().map.getTile(newPos);
    if (newTile) {
        g_game().map.moveCreature(creature, newTile, false);
    }
}

// Exemplo 4: Posicionamento com busca de posição livre
bool Game::placeCreatureNear(const std::shared_ptr<Creature> &creature, const Position &center) {
    // Busca posição livre próxima
    for (int dx = -2; dx <= 2; dx++) {
        for (int dy = -2; dy <= 2; dy++) {
            Position pos = center + Position(dx, dy, 0);
            if (g_game().map.placeCreature(pos, creature, false, false)) {
                return true;
            }
        }
    }
    return false;
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
// Exemplo 1: Verificar se pode atirar objeto
bool Game::canThrowObject(const Position &from, const Position &to) {
    return g_game().map.canThrowObjectTo(from, to);
}

// Exemplo 2: Verificar linha de visão
bool Game::hasLineOfSight(const Position &from, const Position &to) {
    return g_game().map.isSightClear(from, to, true);
}

// Exemplo 3: Verificar se pode andar
std::shared_ptr<Tile> Game::canWalkTo(const std::shared_ptr<Creature> &creature, const Position &pos) {
    return g_game().map.canWalkTo(creature, pos);
}

// Exemplo 4: Encontrar caminho
bool Game::findPath(const std::shared_ptr<Creature> &creature, const Position &target, 
                   std::vector<Direction> &path) {
    FindPathParams fpp;
    fpp.maxSearchDist = 50;
    fpp.clearSight = true;
    fpp.allowDiagonal = true;
    
    return g_game().map.getPathMatching(creature, path, 
                                       FrozenPathingConditionCall(), fpp);
}

// Exemplo 5: Verificar distância
bool Game::isInRange(const Position &from, const Position &to, int range) {
    int distance = std::max(std::abs(from.x - to.x), std::abs(from.y - to.y));
    return distance <= range;
}
```

#### Nível Intermediate
```cpp
// Exemplo 1: Verificar se pode atirar objeto
bool Game::canThrowObject(const Position &from, const Position &to) {
    return g_game().map.canThrowObjectTo(from, to);
}

// Exemplo 2: Verificar linha de visão
bool Game::hasLineOfSight(const Position &from, const Position &to) {
    return g_game().map.isSightClear(from, to, true);
}

// Exemplo 3: Verificar se pode andar
std::shared_ptr<Tile> Game::canWalkTo(const std::shared_ptr<Creature> &creature, const Position &pos) {
    return g_game().map.canWalkTo(creature, pos);
}

// Exemplo 4: Encontrar caminho
bool Game::findPath(const std::shared_ptr<Creature> &creature, const Position &target, 
                   std::vector<Direction> &path) {
    FindPathParams fpp;
    fpp.maxSearchDist = 50;
    fpp.clearSight = true;
    fpp.allowDiagonal = true;
    
    return g_game().map.getPathMatching(creature, path, 
                                       FrozenPathingConditionCall(), fpp);
}

// Exemplo 5: Verificar distância
bool Game::isInRange(const Position &from, const Position &to, int range) {
    int distance = std::max(std::abs(from.x - to.x), std::abs(from.y - to.y));
    return distance <= range;
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
// Exemplo 1: Verificar se pode atirar objeto
bool Game::canThrowObject(const Position &from, const Position &to) {
    return g_game().map.canThrowObjectTo(from, to);
}

// Exemplo 2: Verificar linha de visão
bool Game::hasLineOfSight(const Position &from, const Position &to) {
    return g_game().map.isSightClear(from, to, true);
}

// Exemplo 3: Verificar se pode andar
std::shared_ptr<Tile> Game::canWalkTo(const std::shared_ptr<Creature> &creature, const Position &pos) {
    return g_game().map.canWalkTo(creature, pos);
}

// Exemplo 4: Encontrar caminho
bool Game::findPath(const std::shared_ptr<Creature> &creature, const Position &target, 
                   std::vector<Direction> &path) {
    FindPathParams fpp;
    fpp.maxSearchDist = 50;
    fpp.clearSight = true;
    fpp.allowDiagonal = true;
    
    return g_game().map.getPathMatching(creature, path, 
                                       FrozenPathingConditionCall(), fpp);
}

// Exemplo 5: Verificar distância
bool Game::isInRange(const Position &from, const Position &to, int range) {
    int distance = std::max(std::abs(from.x - to.x), std::abs(from.y - to.y));
    return distance <= range;
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

#### Inicialização e Configuração
```cpp
// Exemplo 1: Adicionar item ao tile
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

// Exemplo 2: Remover item do tile
bool Game::removeItemFromTile(const Position &pos, const std::shared_ptr<Item> &item) {
    auto tile = g_game().map.getTile(pos);
    if (!tile) {
        return false;
    }
```

#### Funcionalidade 1
```cpp
    
    tile->removeThing(item, 1);
    return true;
}

// Exemplo 3: Verificar propriedades do tile
bool Game::isTileWalkable(const Position &pos) {
    auto tile = g_game().map.getTile(pos);
    if (!tile) {
        return false;
    }
    
    return tile->hasProperty(ItemProperty::WALKABLE);
}

// Exemplo 4: Verificar se tile tem criaturas
bool Game::hasCreaturesOnTile(const Position &pos) {
    auto tile = g_game().map.getTile(pos);
    if (!tile) {
        return false;
    }
```

#### Finalização
```cpp
    
    return tile->getCreatureCount() > 0;
}

// Exemplo 5: Obter criatura no topo do tile
std::shared_ptr<Creature> Game::getTopCreature(const Position &pos) {
    auto tile = g_game().map.getTile(pos);
    if (!tile) {
        return nullptr;
    }
    
    return tile->getTopCreature();
}

// Exemplo 6: Verificar campos mágicos
std::shared_ptr<MagicField> Game::getMagicField(const Position &pos) {
    auto tile = g_game().map.getTile(pos);
    if (!tile) {
        return nullptr;
    }
    
    return tile->getFieldItem();
}
```

### **6. Uso via Lua**

#### Inicialização e Configuração
```lua
-- Exemplo 1: Obter tile em posição
local tile = Tile(100, 100, 7)
if tile then
    print("Tile encontrado em posição:", tile:getPosition())
end

-- Exemplo 2: Verificar propriedades do tile
if tile:hasProperty(ITEM_PROPERTY_WALKABLE) then
    print("Tile é caminhável")
end

if tile:hasFlag(TILESTATE_PROTECTIONZONE) then
    print("Tile está em zona de proteção")
end

-- Exemplo 3: Adicionar item ao tile
local item = Item(2160) -- Gold coin
if tile:addItem(item) then
    print("Item adicionado com sucesso")
end

-- Exemplo 4: Obter criaturas no tile
local creatures = tile:getCreatures()
for _, creature in ipairs(creatures) do
    print("Criatura encontrada:", creature:getName())
end
```

#### Funcionalidade 1
```lua

-- Exemplo 5: Verificar se tile tem campo mágico
local field = tile:getFieldItem()
if field then
    print("Tile tem campo mágico:", field:getId())
end

-- Exemplo 6: Obter casa do tile
local house = tile:getHouse()
if house then
    print("Tile pertence à casa:", house:getName())
end

-- Exemplo 7: Limpar tile
tile:sweep()

-- Exemplo 8: Verificar itens no tile
local items = tile:getItems()
for _, item in ipairs(items) do
    print("Item encontrado:", item:getId())
end
```

#### Finalização
```lua

-- Exemplo 9: Obter contagem de itens
local itemCount = tile:getItemCount()
print("Número de itens no tile:", itemCount)

-- Exemplo 10: Verificar propriedades específicas
if tile:hasProperty(ITEM_PROPERTY_BLOCKSOLID) then
    print("Tile bloqueia passagem")
end

if tile:hasProperty(ITEM_PROPERTY_HASHEIGHT) then
    print("Tile tem altura")
end
```

## 🗺️ **Tipos de Tiles e Propriedades**

### **Tipos de Tiles**
| Tipo | Descrição | Uso |
|------|-----------|-----|
| `StaticTile` | Tile estático | Otimização de memória |
| `DynamicTile` | Tile dinâmico | Tiles modificáveis |
| `HouseTile` | Tile de casa | Propriedades especiais |

### **Propriedades de Tiles**
| Propriedade | Descrição | Uso |
|-------------|-----------|-----|
| `WALKABLE` | Pode andar | Movimento de criaturas |
| `BLOCKSOLID` | Bloqueia passagem | Obstáculos |
| `HASHEIGHT` | Tem altura | Elevação |
| `BLOCKPROJECTILE` | Bloqueia projéteis | Combate |
| `BLOCKPATH` | Bloqueia caminho | Pathfinding |

### **Flags de Tiles**
| Flag | Descrição | Uso |
|------|-----------|-----|
| `TILESTATE_PROTECTIONZONE` | Zona de proteção | PvP desabilitado |
| `TILESTATE_NOPVPZONE` | Zona sem PvP | PvP desabilitado |
| `TILESTATE_PVPZONE` | Zona de PvP | PvP forçado |
| `TILESTATE_NOLOGOUT` | Sem logout | Logout desabilitado |
| `TILESTATE_FLOORCHANGE` | Mudança de andar | Teleporte automático |

## 📝 **Exercícios Práticos**

### **Exercício 1: Sistema de Carregamento de Mapas**
Crie um sistema que carregue diferentes tipos de mapas:

```cpp
// Implemente esta função
class MapManager {
    -- Classe: MapManager
public:
    // TODO: Implemente carregamento de mapa principal
    bool loadMainMap(const std::string &mapName);
    
    // TODO: Implemente carregamento de mapa customizado
    bool loadCustomMap(const std::string &mapName, int index);
    
    // TODO: Implemente carregamento seletivo de componentes
    bool loadMapComponents(const std::string &mapPath, bool houses, 
                          bool monsters, bool npcs, bool zones);
    
    // TODO: Implemente verificação de integridade do mapa
    bool validateMap(const std::string &mapPath);
};
```

### **Exercício 2: Sistema de Posicionamento**
Crie um sistema de posicionamento inteligente:

```cpp
// Implemente esta função
class PositionManager {
    -- Classe: PositionManager
public:
    // TODO: Implemente busca de posição livre
    Position findFreePosition(const Position &center, int radius);
    
    // TODO: Implemente posicionamento de grupo
    bool placeGroup(const std::vector<std::shared_ptr<Creature>> &creatures, 
                   const Position &center);
    
    // TODO: Implemente verificação de colisão
    bool checkCollision(const Position &pos, const std::shared_ptr<Creature> &creature);
    
    // TODO: Implemente posicionamento em área
    bool placeInArea(const std::shared_ptr<Creature> &creature, 
                    const Position &topLeft, const Position &bottomRight);
};
```

### **Exercício 3: Sistema de Pathfinding**
Crie um sistema de navegação avançado:

```cpp
// Implemente esta função
class PathfindingManager {
    -- Classe: PathfindingManager
public:
    // TODO: Implemente busca de caminho com obstáculos
    std::vector<Direction> findPathWithObstacles(const Position &start, 
                                                const Position &end);
    
    // TODO: Implemente busca de caminho para grupo
    std::vector<std::vector<Direction>> findGroupPath(
        const std::vector<std::shared_ptr<Creature>> &creatures, 
        const Position &target);
    
    // TODO: Implemente verificação de linha de visão
    bool hasLineOfSight(const Position &from, const Position &to, 
                       bool checkFloors = true);
    
    // TODO: Implemente cálculo de distância
    int calculateDistance(const Position &from, const Position &to);
};
```

### **Exercício 4: Sistema de Tiles**
Crie um sistema de gerenciamento de tiles:

```cpp
// Implemente esta função
class TileManager {
    -- Classe: TileManager
public:
    // TODO: Implemente criação de tile dinâmico
    std::shared_ptr<Tile> createDynamicTile(const Position &pos);
    
    // TODO: Implemente modificação de propriedades
    bool modifyTileProperties(const Position &pos, uint32_t flags);
    
    // TODO: Implemente verificação de propriedades
    bool hasTileProperty(const Position &pos, ItemProperty property);
    
    // TODO: Implemente limpeza de área
    void clearArea(const Position &topLeft, const Position &bottomRight);
    
    // TODO: Implemente cópia de tile
    bool copyTile(const Position &from, const Position &to);
};
```

### **Exercício 5: Sistema Lua**
Crie scripts Lua que usem o sistema de mapas:

#### Nível Basic
```lua
-- TODO: Implemente estas funções Lua

-- 1. Função para criar área de spawn
function createSpawnArea(centerPosition, radius, creatureType, count)
    -- Cria área de spawn de criaturas
end

-- 2. Função para verificar área segura
function isSafeArea(position, radius)
    -- Verifica se área é segura para jogadores
end

-- 3. Função para criar teleporte
function createTeleport(position, destination)
    -- Cria teleporte entre duas posições
end

-- 4. Função para criar campo mágico
function createMagicField(position, fieldType, damage)
    -- Cria campo mágico com dano específico
end

-- 5. Função para verificar linha de visão
function checkLineOfSight(fromPos, toPos)
    -- Verifica se há linha de visão entre posições
end

-- 6. Função para encontrar caminho
function findPath(startPos, endPos, maxDistance)
    -- Encontra caminho entre duas posições
end

-- 7. Função para criar zona de proteção
function createProtectionZone(topLeft, bottomRight)
    -- Cria zona de proteção
end

-- 8. Função para verificar propriedades de tile
function getTileProperties(position)
    -- Retorna todas as propriedades de um tile
end
```

#### Nível Intermediate
```lua
-- TODO: Implemente estas funções Lua

-- 1. Função para criar área de spawn
function createSpawnArea(centerPosition, radius, creatureType, count)
    -- Cria área de spawn de criaturas
end

-- 2. Função para verificar área segura
function isSafeArea(position, radius)
    -- Verifica se área é segura para jogadores
end

-- 3. Função para criar teleporte
function createTeleport(position, destination)
    -- Cria teleporte entre duas posições
end

-- 4. Função para criar campo mágico
function createMagicField(position, fieldType, damage)
    -- Cria campo mágico com dano específico
end

-- 5. Função para verificar linha de visão
function checkLineOfSight(fromPos, toPos)
    -- Verifica se há linha de visão entre posições
end

-- 6. Função para encontrar caminho
function findPath(startPos, endPos, maxDistance)
    -- Encontra caminho entre duas posições
end

-- 7. Função para criar zona de proteção
function createProtectionZone(topLeft, bottomRight)
    -- Cria zona de proteção
end

-- 8. Função para verificar propriedades de tile
function getTileProperties(position)
    -- Retorna todas as propriedades de um tile
end
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```lua
-- TODO: Implemente estas funções Lua

-- 1. Função para criar área de spawn
function createSpawnArea(centerPosition, radius, creatureType, count)
    -- Cria área de spawn de criaturas
end

-- 2. Função para verificar área segura
function isSafeArea(position, radius)
    -- Verifica se área é segura para jogadores
end

-- 3. Função para criar teleporte
function createTeleport(position, destination)
    -- Cria teleporte entre duas posições
end

-- 4. Função para criar campo mágico
function createMagicField(position, fieldType, damage)
    -- Cria campo mágico com dano específico
end

-- 5. Função para verificar linha de visão
function checkLineOfSight(fromPos, toPos)
    -- Verifica se há linha de visão entre posições
end

-- 6. Função para encontrar caminho
function findPath(startPos, endPos, maxDistance)
    -- Encontra caminho entre duas posições
end

-- 7. Função para criar zona de proteção
function createProtectionZone(topLeft, bottomRight)
    -- Cria zona de proteção
end

-- 8. Função para verificar propriedades de tile
function getTileProperties(position)
    -- Retorna todas as propriedades de um tile
end
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

## 🎯 **Conceitos-Chave**

### **1. Sistema de Cache**
- **Definição**: Armazenamento temporário de dados frequentes
- **Propósito**: Melhorar performance de acesso
- **Implementação**: MapCache com setores

### **2. Lazy Loading**
- **Definição**: Carregamento sob demanda
- **Propósito**: Reduzir uso inicial de memória
- **Implementação**: Carregamento de tiles quando necessário

### **3. Setores de Mapa**
- **Definição**: Agrupamento de tiles para otimização
- **Propósito**: Melhorar performance de acesso
- **Implementação**: MapSector com hash maps

### **4. Pathfinding**
- **Definição**: Algoritmo para encontrar caminhos
- **Propósito**: Navegação automática de criaturas
- **Implementação**: Algoritmo A* com condições customizáveis

### **5. Sistema de Zonas**
- **Definição**: Áreas com propriedades especiais
- **Propósito**: Controle de comportamento do jogo
- **Implementação**: Flags de tile e sistema de Zone

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

## 🔗 **Integração com Outros Sistemas**

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

## 📊 **Boas Práticas**

### **1. Performance**
- Use cache adequadamente
- Implemente lazy loading
- Otimize acesso a tiles
- Monitore uso de memória

### **2. Escalabilidade**
- Considere mapas grandes
- Implemente setores eficientes
- Use compressão quando apropriado
- Otimize carregamento

### **3. Manutenibilidade**
- Documente modificações
- Use constantes para flags
- Implemente validação
- Mantenha código limpo

### **4. Segurança**
- Valide posições
- Verifique permissões
- Implemente limites
- Proteja contra exploits

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
- [[CANARY-010_particle_system]] - Sistema de Partículas
- [[CANARY-012_combat_system]] - Sistema de Combate
- [Documentação Principal](../../README.md)
- [Pesquisa CANARY-011](../research/habdel/CANARY-011.md)

---
*Lição criada seguindo metodologia habdel - 2025-01-27* 