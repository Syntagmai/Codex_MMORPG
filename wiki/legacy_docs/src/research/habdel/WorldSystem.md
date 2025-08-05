# Sistema de Mundo e Mapas OTClient

O OTClient implementa um sistema completo de mundo e mapas que gerencia terrenos, tiles, criaturas e pathfinding para criar um ambiente de jogo totalmente funcional.

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Arquitetura do Sistema](#arquitetura-do-sistema)
3. [Sistema de Mapas](#sistema-de-mapas)
4. [Sistema de Tiles](#sistema-de-tiles)
5. [Sistema de Criaturas](#sistema-de-criaturas)
6. [Pathfinding](#pathfinding)
7. [Awareness Range](#awareness-range)
8. [MapView e Rendering](#mapview-e-rendering)
9. [Implementação Prática](#implementação-prática)
10. [Melhores Práticas](#melhores-práticas)

## 🎯 Visão Geral

O sistema de mundo do OTClient oferece:

- **Gerenciamento de Mapas**: Carregamento e manipulação de mapas OTBM/OTCM
- **Sistema de Tiles**: Organização hierárquica de objetos no mundo
- **Awareness Range**: Otimização de memória e performance
- **Pathfinding**: Algoritmos A* para navegação inteligente
- **Multi-Floor**: Suporte completo para múltiplos andares
- **Editor Integration**: Ferramentas avançadas para edição de mapas

### 🏗️ **Arquitetura do Mundo**

```
Mundo Global (g_map)
   │
   ├─ Floor 0-15 (FloorData)
   │   │
   │   ├─ Tile Blocks (32x32)
   │   │   │
   │   │   ├─ Tiles individuais
   │   │   │   │
   │   │   │   ├─ Ground
   │   │   │   ├─ Items (empilhados)
   │   │   │   ├─ Creatures
   │   │   │   └─ Effects
   │   │   │
   │   │   └─ Missiles (efeitos de projétil)
   │   │
   │   └─ Criaturas (cache global)
   │
   ├─ MapViews (múltiplas câmeras)
   ├─ Texts (estáticos e animados)
   └─ Light System
```

## 🗺️ Sistema de Mapas

### 📦 **Classe Map (Singleton Global)**

#### Nível Basic
```cpp
// Acesso global ao mapa
extern Map g_map;

// Inicialização e limpeza
g_map.init();
g_map.terminate();
g_map.clean();
```

#### Nível Intermediate
```cpp
// Acesso global ao mapa
extern Map g_map;

// Inicialização e limpeza
g_map.init();
g_map.terminate();
g_map.clean();
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
// Acesso global ao mapa
extern Map g_map;

// Inicialização e limpeza
g_map.init();
g_map.terminate();
g_map.clean();
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

### 🔧 **Operações Básicas com Mapas**

```lua
-- Limpar o mapa completamente
    --  Limpar o mapa completamente (traduzido)
g_map.clean()

-- Limpar apenas objetos dinâmicos (criaturas, efeitos)
g_map.cleanDynamicThings()

-- Limpar textos animados e estáticos
g_map.cleanTexts()

-- Definir tamanho do mapa
    --  Definir tamanho do mapa (traduzido)
g_map.setSize(1024, 1024)  -- width, height
local mapSize = g_map.getSize()

-- Position central do mapa
    --  Position central do mapa (traduzido)
g_map.setCentralPosition({x = 1000, y = 1000, z = 7})
local centralPos = g_map.getCentralPosition()
```

### 🏗️ **Carregamento de Mapas**

```lua
-- Formatos de mapa suportados
    --  Formatos de mapa suportados (traduzido)
-- OTBM: Formato padrão do RME (Remere's Map Editor)
-- OTCM: Formato otimizado do OTClient
    --  OTCM: Formato otimizado do OTClient (traduzido)

-- Em modo editor (FRAMEWORK_EDITOR)
    --  Em modo editor (FRAMEWORK_EDITOR) (traduzido)
g_map.loadOtbm("data/world/map.otbm")
g_map.saveOtbm("data/world/map_export.otbm")

g_map.loadOtcm("data/world/map.otcm")
g_map.saveOtcm("data/world/map_export.otcm")

-- Configurar arquivos auxiliares
    --  Configurar arquivos auxiliares (traduzido)
g_map.setHouseFile("data/world/houses.xml")
g_map.setSpawnFile("data/world/spawns.xml")
g_map.setDescription("Mapa customizado\nCriado com OTClient Editor")
```

## 🎯 Sistema de Tiles

### 📐 **Estrutura Hierárquica**

```cpp
// Organização de Tiles em Blocos
const int BLOCK_SIZE = 32;  // 32x32 tiles por bloco

class TileBlock {
    -- Classe: TileBlock
    std::array<TilePtr, BLOCK_SIZE * BLOCK_SIZE> m_tiles;
};

// Cada floor contém múltiplos TileBlocks
struct FloorData {
    std::unordered_map<uint32_t, TileBlock> tileBlocks;
    std::vector<MissilePtr> missiles;
};
```

### 🔨 **Manipulação de Tiles**

#### Nível Basic
```lua
-- Obter tile em uma posição
local tile = g_map.getTile({x = 1000, y = 1000, z = 7})
-- Criar tile se não existir
local tile = g_map.getOrCreateTile({x = 1000, y = 1000, z = 7})
-- Criar tile vazio
local tile = g_map.createTile({x = 1000, y = 1000, z = 7})
-- Limpar tile específico
-- Verificar se tile existe
if tile then
    print("Tile existe na posição")
end
-- Listar todos os tiles de um floor
local tiles = g_map.getTiles(7)  -- floor 7
    print("Tile encontrado:", tile:getPosition())
end
```

#### Nível Intermediate
```lua
-- Obter tile em uma posição
local tile = g_map.getTile({x = 1000, y = 1000, z = 7})

-- Criar tile se não existir
local tile = g_map.getOrCreateTile({x = 1000, y = 1000, z = 7})

-- Criar tile vazio
local tile = g_map.createTile({x = 1000, y = 1000, z = 7})

-- Limpar tile específico
g_map.cleanTile({x = 1000, y = 1000, z = 7})

-- Verificar se tile existe
if tile then
    print("Tile existe na posição")
end

-- Listar todos os tiles de um floor
local tiles = g_map.getTiles(7)  -- floor 7
for _, tile in ipairs(tiles) do
    print("Tile encontrado:", tile:getPosition())
end
```

#### Nível Advanced
```lua
-- Obter tile em uma posição
local tile = g_map.getTile({x = 1000, y = 1000, z = 7})

-- Criar tile se não existir
local tile = g_map.getOrCreateTile({x = 1000, y = 1000, z = 7})

-- Criar tile vazio
local tile = g_map.createTile({x = 1000, y = 1000, z = 7})

-- Limpar tile específico
g_map.cleanTile({x = 1000, y = 1000, z = 7})

-- Verificar se tile existe
if tile then
    print("Tile existe na posição")
end

-- Listar todos os tiles de um floor
local tiles = g_map.getTiles(7)  -- floor 7
for _, tile in ipairs(tiles) do
    print("Tile encontrado:", tile:getPosition())
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

### 📦 **Manipulação de Objetos nos Tiles**

#### Nível Basic
```lua
-- Adicionar objeto a um tile
local item = Item.create(1234)  -- ID do item
-- Remover objeto específico
-- Remover por posição e stack
-- Obter objeto de um tile
local thing = g_map.getThing({x = 1000, y = 1000, z = 7}, 0)
-- Procurar itens por ID
local items = g_map.findItemsById(1234, 100)  -- ID, máximo
    print("Item encontrado em:", pos)
end
```

#### Nível Intermediate
```lua
-- Adicionar objeto a um tile
local item = Item.create(1234)  -- ID do item
g_map.addThing(item, {x = 1000, y = 1000, z = 7}, -1)  -- stackPos -1 = topo

-- Remover objeto específico
g_map.removeThing(item)

-- Remover por posição e stack
g_map.removeThingByPos({x = 1000, y = 1000, z = 7}, 0)  -- stackPos 0

-- Obter objeto de um tile
local thing = g_map.getThing({x = 1000, y = 1000, z = 7}, 0)

-- Procurar itens por ID
local items = g_map.findItemsById(1234, 100)  -- ID, máximo
for pos, item in pairs(items) do
    print("Item encontrado em:", pos)
end
```

#### Nível Advanced
```lua
-- Adicionar objeto a um tile
local item = Item.create(1234)  -- ID do item
g_map.addThing(item, {x = 1000, y = 1000, z = 7}, -1)  -- stackPos -1 = topo

-- Remover objeto específico
g_map.removeThing(item)

-- Remover por posição e stack
g_map.removeThingByPos({x = 1000, y = 1000, z = 7}, 0)  -- stackPos 0

-- Obter objeto de um tile
local thing = g_map.getThing({x = 1000, y = 1000, z = 7}, 0)

-- Procurar itens por ID
local items = g_map.findItemsById(1234, 100)  -- ID, máximo
for pos, item in pairs(items) do
    print("Item encontrado em:", pos)
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

### 🎨 **Propriedades dos Tiles**

#### Nível Basic
```lua
local tile = g_map.getTile({x = 1000, y = 1000, z = 7})
if tile then
    -- Verificar propriedades
    local isWalkable = tile:isWalkable()
    local isPathable = tile:isPathable()
    local hasCreature = tile:hasCreature()
    local hasGround = tile:hasGround()
    -- Obter ground (chão)
    local ground = tile:getGround()
    -- Contar objetos
    local thingCount = tile:getThingCount()
    -- Obter elevação
    local elevation = tile:getElevation()
    -- Verificar se bloqueia projéteis
    local blocksProjectile = tile:isBlockProjectile()
    -- Obter todos os objetos
    local things = tile:getThings()
        print("Objeto " .. i .. ":", thing:getId())
    end
end
```

#### Nível Intermediate
```lua
local tile = g_map.getTile({x = 1000, y = 1000, z = 7})
if tile then
    -- Verificar propriedades
    local isWalkable = tile:isWalkable()
    local isPathable = tile:isPathable()
    local hasCreature = tile:hasCreature()
    local hasGround = tile:hasGround()
    
    -- Obter ground (chão)
    local ground = tile:getGround()
    
    -- Contar objetos
    local thingCount = tile:getThingCount()
    
    -- Obter elevação
    local elevation = tile:getElevation()
    
    -- Verificar se bloqueia projéteis
    local blocksProjectile = tile:isBlockProjectile()
    
    -- Obter todos os objetos
    local things = tile:getThings()
    for i, thing in ipairs(things) do
        print("Objeto " .. i .. ":", thing:getId())
    end
end
```

#### Nível Advanced
```lua
local tile = g_map.getTile({x = 1000, y = 1000, z = 7})
if tile then
    -- Verificar propriedades
    local isWalkable = tile:isWalkable()
    local isPathable = tile:isPathable()
    local hasCreature = tile:hasCreature()
    local hasGround = tile:hasGround()
    
    -- Obter ground (chão)
    local ground = tile:getGround()
    
    -- Contar objetos
    local thingCount = tile:getThingCount()
    
    -- Obter elevação
    local elevation = tile:getElevation()
    
    -- Verificar se bloqueia projéteis
    local blocksProjectile = tile:isBlockProjectile()
    
    -- Obter todos os objetos
    local things = tile:getThings()
    for i, thing in ipairs(things) do
        print("Objeto " .. i .. ":", thing:getId())
    end
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

## 👥 Sistema de Criaturas

### 🔍 **Gerenciamento de Criaturas**

```lua
-- Adicionar criatura ao mapa
    --  Adicionar criatura ao mapa (traduzido)
local creature = Creature.create()
creature:setName("Demon")
creature:setId(12345)
g_map.addCreature(creature)

-- Buscar criatura por ID
    --  Buscar criatura por ID (traduzido)
local creature = g_map.getCreatureById(12345)
if creature then
    -- Verificação condicional
    print("Criatura encontrada:", creature:getName())
end

-- Remover criatura
    --  Remover criatura (traduzido)
g_map.removeCreatureById(12345)

-- Obter todas as criaturas
    --  Obter todas as criaturas (traduzido)
local creatures = g_map.getCreatures()
for id, creature in pairs(creatures) do
    -- Loop de repetição
    print("Criatura ID " .. id .. ":", creature:getName())
end
```

### 👀 **Sistema de Spectators**

#### Nível Basic
```lua
-- Posição central
local centerPos = {x = 1000, y = 1000, z = 7}
-- Buscar spectators (criaturas visíveis)
local spectators = g_map.getSpectators(centerPos, true)  -- multiFloor = true
    print("Spectator:", creature:getName())
end
-- Buscar spectators para visão
local sightSpectators = g_map.getSightSpectators(centerPos, false)
-- Buscar em range customizado
local rangeSpectators = g_map.getSpectatorsInRange(centerPos, true, 5, 5)
-- Buscar em range assimétrico
local asymmetricSpectators = g_map.getSpectatorsInRangeEx(
-- Buscar por padrão
local patternSpectators = g_map.getSpectatorsByPattern(
```

#### Nível Intermediate
```lua
-- Posição central
local centerPos = {x = 1000, y = 1000, z = 7}

-- Buscar spectators (criaturas visíveis)
local spectators = g_map.getSpectators(centerPos, true)  -- multiFloor = true
for _, creature in ipairs(spectators) do
    print("Spectator:", creature:getName())
end

-- Buscar spectators para visão
local sightSpectators = g_map.getSightSpectators(centerPos, false)

-- Buscar em range customizado
local rangeSpectators = g_map.getSpectatorsInRange(centerPos, true, 5, 5)

-- Buscar em range assimétrico
local asymmetricSpectators = g_map.getSpectatorsInRangeEx(
    centerPos, true,  -- posição, multiFloor
    3, 7,             -- minX, maxX
    2, 5              -- minY, maxY
)

-- Buscar por padrão
local patternSpectators = g_map.getSpectatorsByPattern(
    centerPos, 
    "Demon.*",        -- regex pattern
    Otc.North         -- direção
)
```

#### Nível Advanced
```lua
-- Posição central
local centerPos = {x = 1000, y = 1000, z = 7}

-- Buscar spectators (criaturas visíveis)
local spectators = g_map.getSpectators(centerPos, true)  -- multiFloor = true
for _, creature in ipairs(spectators) do
    print("Spectator:", creature:getName())
end

-- Buscar spectators para visão
local sightSpectators = g_map.getSightSpectators(centerPos, false)

-- Buscar em range customizado
local rangeSpectators = g_map.getSpectatorsInRange(centerPos, true, 5, 5)

-- Buscar em range assimétrico
local asymmetricSpectators = g_map.getSpectatorsInRangeEx(
    centerPos, true,  -- posição, multiFloor
    3, 7,             -- minX, maxX
    2, 5              -- minY, maxY
)

-- Buscar por padrão
local patternSpectators = g_map.getSpectatorsByPattern(
    centerPos, 
    "Demon.*",        -- regex pattern
    Otc.North         -- direção
)
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

## 🛤️ Pathfinding

### 🧭 **Sistema de Navegação**

```lua
-- Encontrar caminho básico
local startPos = {x = 1000, y = 1000, z = 7}
local goalPos = {x = 1010, y = 1010, z = 7}

local path, result = g_map.findPath(startPos, goalPos, 100)  -- maxComplexity

if result == Otc.PathFindResultOk then
    -- Verificação condicional
    print("Caminho encontrado!")
    for i, direction in ipairs(path) do
    -- Loop de repetição
        print("Passo " .. i .. ":", Otc.DirectionToString(direction))
    end
else
    print("Caminho não encontrado:", result)
end

-- Resultados possíveis
-- Otc.PathFindResultOk           - Sucesso
    --  Otc.PathFindResultOk           - Sucesso (traduzido)
-- Otc.PathFindResultNoWay        - Sem caminho
    --  Otc.PathFindResultNoWay        - Sem caminho (traduzido)
-- Otc.PathFindResultTooFar       - Muito distante
    --  Otc.PathFindResultTooFar       - Muito distante (traduzido)
-- Otc.PathFindResultTooManySteps - Muitos passos
    --  Otc.PathFindResultTooManySteps - Muitos passos (traduzido)
```

### ⚡ **Pathfinding Assíncrono**

```lua
-- Encontrar caminho em background
    --  Encontrar caminho em background (traduzido)
g_map.findPathAsync(startPos, goalPos, function(result)
    if result.status == Otc.PathFindResultOk then
    -- Verificação condicional
        print("Caminho assíncrono encontrado!")
        print("Complexidade:", result.complexity)
        
        for i, direction in ipairs(result.path) do
    -- Loop de repetição
            print("Direção " .. i .. ":", direction)
        end
    else
        print("Falha no pathfinding:", result.status)
    end
end)
```

### 🔍 **Pathfinding Avançado**

#### Nível Basic
```lua
-- Encontrar múltiplos caminhos
local paths = g_map.findEveryPath(
    local steps, cost, time, description = table.unpack(pathData)
    print(pathName .. ":", steps .. " passos, custo " .. cost)
end
-- Verificar linha de visão
local canSee = g_map.isSightClear(
if canSee then
    print("Linha de visão livre")
    print("Visão bloqueada")
end
```

#### Nível Intermediate
```lua
-- Encontrar múltiplos caminhos
local paths = g_map.findEveryPath(
    startPos,
    50,  -- distância máxima
    {
        avoid_creatures = "true",
        avoid_fields = "true",
        allow_diagonal = "false"
    }
)

for pathName, pathData in pairs(paths) do
    local steps, cost, time, description = table.unpack(pathData)
    print(pathName .. ":", steps .. " passos, custo " .. cost)
end

-- Verificar linha de visão
local canSee = g_map.isSightClear(
    {x = 1000, y = 1000, z = 7},
    {x = 1005, y = 1005, z = 7}
)

if canSee then
    print("Linha de visão livre")
else
    print("Visão bloqueada")
end
```

#### Nível Advanced
```lua
-- Encontrar múltiplos caminhos
local paths = g_map.findEveryPath(
    startPos,
    50,  -- distância máxima
    {
        avoid_creatures = "true",
        avoid_fields = "true",
        allow_diagonal = "false"
    }
)

for pathName, pathData in pairs(paths) do
    local steps, cost, time, description = table.unpack(pathData)
    print(pathName .. ":", steps .. " passos, custo " .. cost)
end

-- Verificar linha de visão
local canSee = g_map.isSightClear(
    {x = 1000, y = 1000, z = 7},
    {x = 1005, y = 1005, z = 7}
)

if canSee then
    print("Linha de visão livre")
else
    print("Visão bloqueada")
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

## 📡 Awareness Range

### 🎯 **Gerenciamento de Alcance**

#### Nível Basic
```lua
-- Obter awareness range atual
local awareRange = g_map.getAwareRange()
print("Aware Range:", awareRange.left, awareRange.right, awareRange.top, awareRange.bottom)
-- Definir awareness range customizado
-- Resetar para o padrão
-- Verificar se posição está no aware range
local pos = {x = 1000, y = 1000, z = 7}
local isAware = g_map.isAwareOfPosition(pos)
if isAware then
    print("Posição está no range de awareness")
    print("Posição fora do awareness range")
end
```

#### Nível Intermediate
```lua
-- Obter awareness range atual
local awareRange = g_map.getAwareRange()
print("Aware Range:", awareRange.left, awareRange.right, awareRange.top, awareRange.bottom)

-- Definir awareness range customizado
g_map.setAwareRange({
    left = 8,      -- tiles à esquerda
    right = 9,     -- tiles à direita  
    top = 6,       -- tiles acima
    bottom = 7     -- tiles abaixo
})

-- Resetar para o padrão
g_map.resetAwareRange()

-- Verificar se posição está no aware range
local pos = {x = 1000, y = 1000, z = 7}
local isAware = g_map.isAwareOfPosition(pos)

if isAware then
    print("Posição está no range de awareness")
else
    print("Posição fora do awareness range")
end
```

#### Nível Advanced
```lua
-- Obter awareness range atual
local awareRange = g_map.getAwareRange()
print("Aware Range:", awareRange.left, awareRange.right, awareRange.top, awareRange.bottom)

-- Definir awareness range customizado
g_map.setAwareRange({
    left = 8,      -- tiles à esquerda
    right = 9,     -- tiles à direita  
    top = 6,       -- tiles acima
    bottom = 7     -- tiles abaixo
})

-- Resetar para o padrão
g_map.resetAwareRange()

-- Verificar se posição está no aware range
local pos = {x = 1000, y = 1000, z = 7}
local isAware = g_map.isAwareOfPosition(pos)

if isAware then
    print("Posição está no range de awareness")
else
    print("Posição fora do awareness range")
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

### 🌟 **Floor Awareness**

#### Nível Basic
```lua
-- Obter range de floors visíveis
local firstFloor = g_map.getFirstAwareFloor()
local lastFloor = g_map.getLastAwareFloor()

print("Floors visíveis:", firstFloor .. " a " .. lastFloor)

-- Verificar cobertura de posição
local pos = {x = 1000, y = 1000, z = 7}

-- Verificar se está coberto
local isCovered = g_map.isCovered(pos, 0)  -- firstFloor = 0

-- Verificar se está completamente coberto
local isCompletelyCovered = g_map.isCompletelyCovered(pos, 0)

-- Verificar se é possível olhar
local canLook = g_map.isLookPossible(pos)

print("Coberto:", isCovered)
print("Completamente coberto:", isCompletelyCovered)
print("Pode olhar:", canLook)
```

#### Nível Intermediate
```lua
-- Obter range de floors visíveis
local firstFloor = g_map.getFirstAwareFloor()
local lastFloor = g_map.getLastAwareFloor()

print("Floors visíveis:", firstFloor .. " a " .. lastFloor)

-- Verificar cobertura de posição
local pos = {x = 1000, y = 1000, z = 7}

-- Verificar se está coberto
local isCovered = g_map.isCovered(pos, 0)  -- firstFloor = 0

-- Verificar se está completamente coberto
local isCompletelyCovered = g_map.isCompletelyCovered(pos, 0)

-- Verificar se é possível olhar
local canLook = g_map.isLookPossible(pos)

print("Coberto:", isCovered)
print("Completamente coberto:", isCompletelyCovered)
print("Pode olhar:", canLook)
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
-- Obter range de floors visíveis
local firstFloor = g_map.getFirstAwareFloor()
local lastFloor = g_map.getLastAwareFloor()

print("Floors visíveis:", firstFloor .. " a " .. lastFloor)

-- Verificar cobertura de posição
local pos = {x = 1000, y = 1000, z = 7}

-- Verificar se está coberto
local isCovered = g_map.isCovered(pos, 0)  -- firstFloor = 0

-- Verificar se está completamente coberto
local isCompletelyCovered = g_map.isCompletelyCovered(pos, 0)

-- Verificar se é possível olhar
local canLook = g_map.isLookPossible(pos)

print("Coberto:", isCovered)
print("Completamente coberto:", isCompletelyCovered)
print("Pode olhar:", canLook)
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

## 🎥 MapView e Rendering

### 📹 **Sistema de Múltiplas Câmeras**

#### Nível Basic
```lua
-- MapViews são gerenciadas automaticamente pelo sistema
-- Cada widget de mapa possui sua própria MapView

-- A MapView principal é criada automaticamente
-- Múltiplas MapViews permitem:
-- - Múltiplas janelas de mapa
-- - Mini-mapas
-- - Picture-in-picture
-- - Diferentes seguimentos de criaturas

-- Resetar câmera da MapView
g_map.resetLastCamera()

-- Notificar movimento da câmera
g_map.notificateCameraMove({x = 10, y = 5})  -- offset em pixels
```

#### Nível Intermediate
```lua
-- MapViews são gerenciadas automaticamente pelo sistema
-- Cada widget de mapa possui sua própria MapView

-- A MapView principal é criada automaticamente
-- Múltiplas MapViews permitem:
-- - Múltiplas janelas de mapa
-- - Mini-mapas
-- - Picture-in-picture
-- - Diferentes seguimentos de criaturas

-- Resetar câmera da MapView
g_map.resetLastCamera()

-- Notificar movimento da câmera
g_map.notificateCameraMove({x = 10, y = 5})  -- offset em pixels
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
-- MapViews são gerenciadas automaticamente pelo sistema
-- Cada widget de mapa possui sua própria MapView

-- A MapView principal é criada automaticamente
-- Múltiplas MapViews permitem:
-- - Múltiplas janelas de mapa
-- - Mini-mapas
-- - Picture-in-picture
-- - Diferentes seguimentos de criaturas

-- Resetar câmera da MapView
g_map.resetLastCamera()

-- Notificar movimento da câmera
g_map.notificateCameraMove({x = 10, y = 5})  -- offset em pixels
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

### 💡 **Sistema de Iluminação**

#### Nível Basic
```lua
-- Definir luz global do mapa
g_map.setLight({
    intensity = 255,    -- 0-255
    color = 215        -- cor da luz
})

-- Obter configuração atual de luz
local light = g_map.getLight()
print("Intensidade da luz:", light.intensity)
print("Cor da luz:", light.color)

-- Ghost mode (transparência)
g_map.beginGhostMode(0.5)  -- 50% transparência
-- ... fazer operações ...
g_map.endGhostMode()
```

#### Nível Intermediate
```lua
-- Definir luz global do mapa
g_map.setLight({
    intensity = 255,    -- 0-255
    color = 215        -- cor da luz
})

-- Obter configuração atual de luz
local light = g_map.getLight()
print("Intensidade da luz:", light.intensity)
print("Cor da luz:", light.color)

-- Ghost mode (transparência)
g_map.beginGhostMode(0.5)  -- 50% transparência
-- ... fazer operações ...
g_map.endGhostMode()
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
-- Definir luz global do mapa
g_map.setLight({
    intensity = 255,    -- 0-255
    color = 215        -- cor da luz
})

-- Obter configuração atual de luz
local light = g_map.getLight()
print("Intensidade da luz:", light.intensity)
print("Cor da luz:", light.color)

-- Ghost mode (transparência)
g_map.beginGhostMode(0.5)  -- 50% transparência
-- ... fazer operações ...
g_map.endGhostMode()
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

### 🎨 **Colorização e Efeitos**

```lua
-- Colorizar objetos
    --  Colorizar objetos (traduzido)
local item = g_map.getThing({x = 1000, y = 1000, z = 7}, 0)
if item then
    -- Verificação condicional
    g_map.colorizeThing(item, '#FF0000')  -- vermelho
end

-- Remover colorização
g_map.removeThingColor(item)

-- Controlar efeitos flutuantes
    --  Controlar efeitos flutuantes (traduzido)
g_map.setFloatingEffect(true)
local hasFloatingEffects = g_map.isDrawingFloatingEffects()
```

## 📝 Textos no Mundo

### 📜 **Textos Estáticos**

#### Nível Basic
```lua
-- Adicionar texto estático
local staticText = StaticText.create()
-- Remover texto estático
-- Buscar texto em posição
local foundText = g_map.getStaticText({x = 1000, y = 1000, z = 7})
if foundText then
    print("Texto encontrado:", foundText:getText())
end
-- Obter todos os textos estáticos
local staticTexts = g_map.getStaticTexts()
    print("Texto estático:", text:getText())
end
```

#### Nível Intermediate
```lua
-- Adicionar texto estático
local staticText = StaticText.create()
staticText:setText("Loja de Armas")
staticText:setFont("verdana-11px-rounded")
staticText:setColor('#FFFF00')

g_map.addStaticText(staticText, {x = 1000, y = 1000, z = 7})

-- Remover texto estático
g_map.removeStaticText(staticText)

-- Buscar texto em posição
local foundText = g_map.getStaticText({x = 1000, y = 1000, z = 7})
if foundText then
    print("Texto encontrado:", foundText:getText())
end

-- Obter todos os textos estáticos
local staticTexts = g_map.getStaticTexts()
for _, text in ipairs(staticTexts) do
    print("Texto estático:", text:getText())
end
```

#### Nível Advanced
```lua
-- Adicionar texto estático
local staticText = StaticText.create()
staticText:setText("Loja de Armas")
staticText:setFont("verdana-11px-rounded")
staticText:setColor('#FFFF00')

g_map.addStaticText(staticText, {x = 1000, y = 1000, z = 7})

-- Remover texto estático
g_map.removeStaticText(staticText)

-- Buscar texto em posição
local foundText = g_map.getStaticText({x = 1000, y = 1000, z = 7})
if foundText then
    print("Texto encontrado:", foundText:getText())
end

-- Obter todos os textos estáticos
local staticTexts = g_map.getStaticTexts()
for _, text in ipairs(staticTexts) do
    print("Texto estático:", text:getText())
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

### ✨ **Textos Animados**

```lua
-- Adicionar texto animado
    --  Adicionar texto animado (traduzido)
local animatedText = AnimatedText.create()
animatedText:setText("+50 EXP")
animatedText:setColor('#00FF00')
animatedText:setOffset({x = 0, y = -20})  -- movimento

g_map.addAnimatedText(animatedText, {x = 1000, y = 1000, z = 7})

-- Remover texto animado
    --  Remover texto animado (traduzido)
g_map.removeAnimatedText(animatedText)

-- Obter todos os textos animados
    --  Obter todos os textos animados (traduzido)
local animatedTexts = g_map.getAnimatedTexts()
for _, text in ipairs(animatedTexts) do
    -- Loop de repetição
    print("Texto animado:", text:getText())
end
```

## 🎯 Implementação Prática

### 🏰 **Sistema de Casas (Editor Mode)**

#### Nível Basic
```lua
-- Configuração de zonas em modo editor
g_map.setShowZones(true)
g_map.setZoneOpacity(0.7)

-- Configurar cores de zona
g_map.setZoneColor(TILESTATE_HOUSE, '#0000FF')           -- azul para casas
g_map.setZoneColor(TILESTATE_PROTECTIONZONE, '#00FF00') -- verde para PZ
g_map.setZoneColor(TILESTATE_OPTIONALZONE, '#FFFF00')   -- amarelo para optional

-- Mostrar zona específica
g_map.setShowZone(TILESTATE_HOUSE, true)

-- Verificar configurações
local showingZones = g_map.showZones()
local houseColor = g_map.getZoneColor(TILESTATE_HOUSE)
print("Mostrando zonas:", showingZones)
```

#### Nível Intermediate
```lua
-- Configuração de zonas em modo editor
g_map.setShowZones(true)
g_map.setZoneOpacity(0.7)

-- Configurar cores de zona
g_map.setZoneColor(TILESTATE_HOUSE, '#0000FF')           -- azul para casas
g_map.setZoneColor(TILESTATE_PROTECTIONZONE, '#00FF00') -- verde para PZ
g_map.setZoneColor(TILESTATE_OPTIONALZONE, '#FFFF00')   -- amarelo para optional

-- Mostrar zona específica
g_map.setShowZone(TILESTATE_HOUSE, true)

-- Verificar configurações
local showingZones = g_map.showZones()
local houseColor = g_map.getZoneColor(TILESTATE_HOUSE)
print("Mostrando zonas:", showingZones)
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
-- Configuração de zonas em modo editor
g_map.setShowZones(true)
g_map.setZoneOpacity(0.7)

-- Configurar cores de zona
g_map.setZoneColor(TILESTATE_HOUSE, '#0000FF')           -- azul para casas
g_map.setZoneColor(TILESTATE_PROTECTIONZONE, '#00FF00') -- verde para PZ
g_map.setZoneColor(TILESTATE_OPTIONALZONE, '#FFFF00')   -- amarelo para optional

-- Mostrar zona específica
g_map.setShowZone(TILESTATE_HOUSE, true)

-- Verificar configurações
local showingZones = g_map.showZones()
local houseColor = g_map.getZoneColor(TILESTATE_HOUSE)
print("Mostrando zonas:", showingZones)
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

### 📊 **Sistema de Minimapa**

#### Nível Basic
```lua
-- Obter cor do minimapa para posição
local minimapColor = g_map.getMinimapColor({x = 1000, y = 1000, z = 7})
print("Cor do minimapa:", minimapColor)

-- Cores de minimapa típicas:
-- 0   = Preto (vazio)
-- 88  = Verde (grama)
-- 188 = Marrom (terra)
-- 208 = Azul (água)
-- 18  = Cinza (pedra)
```

#### Nível Intermediate
```lua
-- Obter cor do minimapa para posição
local minimapColor = g_map.getMinimapColor({x = 1000, y = 1000, z = 7})
print("Cor do minimapa:", minimapColor)

-- Cores de minimapa típicas:
-- 0   = Preto (vazio)
-- 88  = Verde (grama)
-- 188 = Marrom (terra)
-- 208 = Azul (água)
-- 18  = Cinza (pedra)
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
-- Obter cor do minimapa para posição
local minimapColor = g_map.getMinimapColor({x = 1000, y = 1000, z = 7})
print("Cor do minimapa:", minimapColor)

-- Cores de minimapa típicas:
-- 0   = Preto (vazio)
-- 88  = Verde (grama)
-- 188 = Marrom (terra)
-- 208 = Azul (água)
-- 18  = Cinza (pedra)
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

### 🎮 **Sistema de Jogo Integrado**

#### Inicialização e Configuração
```lua
-- Exemplo: Sistema de Teleporte
function teleportPlayer(targetPos)
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    local currentPos = player:getPosition()
    
    -- Verificar se posição de destino é válida
    if not g_map.isLookPossible(targetPos) then
        print("Posição de destino inválida")
        return
    end
    
    -- Limpar tile atual
    g_map.removeThing(player)
    
    -- Adicionar na nova posição
    g_map.addThing(player, targetPos)
    
    -- Atualizar posição central
    g_map.setCentralPosition(targetPos)
    
    print("Jogador teleportado de", currentPos, "para", targetPos)
end
```

#### Funcionalidade 1
```lua

-- Exemplo: Sistema de Busca de Itens
function findNearbyItems(centerPos, itemId, radius)
    local foundItems = {}
    
    for x = centerPos.x - radius, centerPos.x + radius do
        for y = centerPos.y - radius, centerPos.y + radius do
            local pos = {x = x, y = y, z = centerPos.z}
            local tile = g_map.getTile(pos)
            
            if tile then
                local things = tile:getThings()
                for _, thing in ipairs(things) do
                    if thing:isItem() and thing:getId() == itemId then
                        table.insert(foundItems, {pos = pos, item = thing})
                    end
                end
            end
        end
    end
    
    return foundItems
end
```

#### Finalização
```lua

-- Uso
local items = findNearbyItems({x = 1000, y = 1000, z = 7}, 1234, 5)
print("Encontrados " .. #items .. " itens")
```

## ✅ Melhores Práticas

### 🛡️ **Performance e Otimização**

```lua
-- ✅ BOM: Verificar existência antes de usar
local function safeTileAccess(pos)
    local tile = g_map.getTile(pos)
    if not tile then
    -- Verificação condicional
        return nil
    end
    
    return tile:getThings()
end

-- ✅ BOM: Cache de tiles frequentemente acessados
    --  ✅ BOM: Cache de tiles frequentemente acessados (traduzido)
local tileCache = {}

local function getCachedTile(pos)
    local key = pos.x .. "," .. pos.y .. "," .. pos.z
    
    if not tileCache[key] then
    -- Verificação condicional
        tileCache[key] = g_map.getTile(pos)
    end
    
    return tileCache[key]
end

-- ✅ BOM: Limitar range de busca
    --  ✅ BOM: Limitar range de busca (traduzido)
local function findItemsInRange(centerPos, itemId, maxRange)
    maxRange = math.min(maxRange, 20)  -- limitar busca
    -- ... implementação ...
end

-- ❌ EVITE: Iterar sobre todo o mapa
    --  ❌ EVITE: Iterar sobre todo o mapa (traduzido)
local function findAllItems(itemId)  -- LENTO!
    for x = 0, 2048 do
    -- Loop de repetição
        for y = 0, 2048 do
    -- Loop de repetição
            -- muito custoso
    --  muito custoso (traduzido)
        end
    end
end
```

### 🔒 **Validação e Segurança**

```lua
-- ✅ BOM: Sempre validar posições
local function isValidPosition(pos)
    return pos and 
           type(pos.x) == 'number' and 
           type(pos.y) == 'number' and 
           type(pos.z) == 'number' and
           pos.x >= 0 and pos.x <= 65535 and
           pos.y >= 0 and pos.y <= 65535 and
           pos.z >= 0 and pos.z <= 15
end

-- ✅ BOM: Verificar awareness range
    --  ✅ BOM: Verificar awareness range (traduzido)
local function isPositionVisible(pos)
    return g_map.isAwareOfPosition(pos) and 
           g_map.isLookPossible(pos)
end

-- ✅ BOM: Cleanup apropriado
    --  ✅ BOM: Cleanup apropriado (traduzido)
local function cleanupMap()
    g_map.cleanDynamicThings()  -- preserva mapa base
    g_map.cleanTexts()          -- remove textos temporários
end
```

### 🎯 **Pathfinding Eficiente**

```lua
-- ✅ BOM: Usar complexidade apropriada
    --  ✅ BOM: Usar complexidade apropriada (traduzido)
local function findPathSmart(start, goal)
    local distance = math.abs(start.x - goal.x) + math.abs(start.y - goal.y)
    local complexity = math.min(distance * 2, 500)  -- adaptivo
    
    return g_map.findPath(start, goal, complexity)
end

-- ✅ BOM: Cache de pathfinding
    --  ✅ BOM: Cache de pathfinding (traduzido)
local pathCache = {}
local CACHE_DURATION = 5000  -- 5 segundos

local function getCachedPath(start, goal)
    local key = start.x .. "," .. start.y .. "->" .. goal.x .. "," .. goal.y
    local cached = pathCache[key]
    
    if cached and g_clock.millis() - cached.time < CACHE_DURATION then
    -- Verificação condicional
        return cached.path, cached.result
    end
    
    local path, result = findPathSmart(start, goal)
    pathCache[key] = {
        path = path,
        result = result,
        time = g_clock.millis()
    }
    
    return path, result
end
```

O sistema de mundo e mapas do OTClient oferece funcionalidade completa para jogos 2D isométricos com performance otimizada e flexibilidade máxima para customização.
## 🔗 **Links Automáticos**

> [!info] **Links Gerados Automaticamente**
> Estes links foram criados automaticamente pelo sistema de linkagem da categoria **Legacy**

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]
- [[../maps/search_index|Busca em Arquivos Legados]]
- [[../legacy_docs/README|Documentação Legada]]

### **🧭 Navegação**
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]
- [[../maps/category_indices|Índices por Categoria]]
- [[../maps/relationships|Relacionamentos]]

### **📊 Métricas da Categoria**
- **Categoria**: Legacy
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

