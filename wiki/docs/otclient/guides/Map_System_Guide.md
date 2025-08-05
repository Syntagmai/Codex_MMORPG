
# Map System Guide

> [!info] Este guia documenta o sistema de mundo e mapas do OTClient, incluindo gerenciamento de tiles, criaturas, pathfinding, awareness range e rendering.


---

## 📋 Índice 📋
- [[#Visão Geral]]
- [[#Sistema de Mapas]]
- [[#Sistema de Tiles]]
- [[#Sistema de Criaturas]]
- [[#Pathfinding]]
- [[#Awareness Range]]
- [[#MapView e Rendering]]
- [[#Implementação Prática]]
- [[#Melhores Práticas]]

---


---

## 🎯 Visão Geral 🎯

O sistema de mundo do OTClient oferece:
- **Gerenciamento de Mapas**: Carregamento e manipulação de mapas OTBM/OTCM
- **Sistema de Tiles**: Organização hierárquica de objetos no mundo
- **Awareness Range**: Otimização de memória e performance
- **Pathfinding**: Algoritmos A* para navegação inteligente
- **Multi-Floor**: Suporte completo para múltiplos andares
- **Editor Integration**: Ferramentas avançadas para edição de mapas

### 🏗️ Arquitetura do Mundo 📝
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

---


---

## 🗺️ Sistema de Mapas ⚙️

### 📦 Classe Map (Singleton Global) 📝
```lua
-- Acesso global ao mapa
    --  Acesso global ao mapa (traduzido)
g_map.init()
g_map.terminate()
g_map.clean()
```

### 🔧 Operações Básicas com Mapas 📝
```lua
-- Limpar o mapa completamente
    --  Limpar o mapa completamente (traduzido)
g_map.clean()

-- Limpar apenas objetos dinâmicos
g_map.cleanDynamicThings()

-- Definir tamanho do mapa
    --  Definir tamanho do mapa (traduzido)
g_map.setSize(1024, 1024)
local mapSize = g_map.getSize()

-- Position central do mapa
    --  Position central do mapa (traduzido)
g_map.setCentralPosition({x = 1000, y = 1000, z = 7})
local centralPos = g_map.getCentralPosition()
```

### 🏗️ Carregamento de Mapas 📝
```lua
-- Formatos de mapa suportados
    --  Formatos de mapa suportados (traduzido)
-- OTBM: Formato padrão do RME (Remere's Map Editor)
-- OTCM: Formato otimizado do OTClient
    --  OTCM: Formato otimizado do OTClient (traduzido)

g_map.loadOtbm("data/world/map.otbm")
g_map.saveOtbm("data/world/map_export.otbm")

g_map.loadOtcm("data/world/map.otcm")
g_map.saveOtcm("data/world/map_export.otcm")

-- Configurar arquivos auxiliares
    --  Configurar arquivos auxiliares (traduzido)
g_map.setHouseFile("data/world/houses.xml")
g_map.setSpawnFile("data/world/spawns.xml")
```

---


---

## 🎯 Sistema de Tiles ⚙️

### 📐 Estrutura Hierárquica 🏗️
```cpp
// Organização de Tiles em Blocos
const int BLOCK_SIZE = 32;  // 32x32 tiles por bloco

class TileBlock {
    -- Classe: TileBlock
    std::array<TilePtr, BLOCK_SIZE * BLOCK_SIZE> m_tiles;
};
```

### 🔨 Manipulação de Tiles 📝
```lua
-- Obter tile em uma posição
local tile = g_map.getTile({x = 1000, y = 1000, z = 7})

-- Criar tile se não existir
local tile = g_map.getOrCreateTile({x = 1000, y = 1000, z = 7})

-- Verificar se tile existe
    --  Verificar se tile existe (traduzido)
if tile then
    -- Verificação condicional
    print("Tile existe na posição")
end

-- Listar todos os tiles de um floor
    --  Listar todos os tiles de um floor (traduzido)
local tiles = g_map.getTiles(7)  -- floor 7
for _, tile in ipairs(tiles) do
    -- Loop de repetição
    print("Tile encontrado:", tile:getPosition())
end
```

### 📦 Manipulação de Objetos nos Tiles 📝
```lua
-- Adicionar objeto a um tile
    --  Adicionar objeto a um tile (traduzido)
local item = Item.create(1234)
g_map.addThing(item, {x = 1000, y = 1000, z = 7}, -1)

-- Remover objeto específico
g_map.removeThing(item)

-- Obter objeto de um tile
    --  Obter objeto de um tile (traduzido)
local thing = g_map.getThing({x = 1000, y = 1000, z = 7}, 0)

-- Procurar itens por ID
    --  Procurar itens por ID (traduzido)
local items = g_map.findItemsById(1234, 100)
for pos, item in pairs(items) do
    -- Loop de repetição
    print("Item encontrado em:", pos)
end
```

### 🎨 Propriedades dos Tiles 📝
```lua
local tile = g_map.getTile({x = 1000, y = 1000, z = 7})
if tile then
    -- Verificação condicional
    local isWalkable = tile:isWalkable()
    local isPathable = tile:isPathable()
    local hasCreature = tile:hasCreature()
    local hasGround = tile:hasGround()
    
    local ground = tile:getGround()
    local thingCount = tile:getThingCount()
    local elevation = tile:getElevation()
    local blocksProjectile = tile:isBlockProjectile()
    
    local things = tile:getThings()
    for i, thing in ipairs(things) do
    -- Loop de repetição
        print("Objeto " .. i .. ":", thing:getId())
    end
end
```

---


---

## 👥 Sistema de Criaturas ⚙️

### 🔍 Gerenciamento de Criaturas 📝
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

### 👀 Sistema de Spectators 📝
#### Nível Basic
```lua
-- Posição central
local centerPos = {x = 1000, y = 1000, z = 7}
-- Buscar spectators (criaturas visíveis)
local spectators = g_map.getSpectators(centerPos, true)
    print("Spectator:", creature:getName())
end
-- Buscar em range customizado
local rangeSpectators = g_map.getSpectatorsInRange(centerPos, true, 5, 5)
-- Buscar por padrão
local patternSpectators = g_map.getSpectatorsByPattern(
```

#### Nível Intermediate
```lua
-- Posição central
local centerPos = {x = 1000, y = 1000, z = 7}

-- Buscar spectators (criaturas visíveis)
local spectators = g_map.getSpectators(centerPos, true)
for _, creature in ipairs(spectators) do
    print("Spectator:", creature:getName())
end

-- Buscar em range customizado
local rangeSpectators = g_map.getSpectatorsInRange(centerPos, true, 5, 5)

-- Buscar por padrão
local patternSpectators = g_map.getSpectatorsByPattern(
    centerPos, 
    "Demon.*",
    Otc.North
)
```

#### Nível Advanced
```lua
-- Posição central
local centerPos = {x = 1000, y = 1000, z = 7}

-- Buscar spectators (criaturas visíveis)
local spectators = g_map.getSpectators(centerPos, true)
for _, creature in ipairs(spectators) do
    print("Spectator:", creature:getName())
end

-- Buscar em range customizado
local rangeSpectators = g_map.getSpectatorsInRange(centerPos, true, 5, 5)

-- Buscar por padrão
local patternSpectators = g_map.getSpectatorsByPattern(
    centerPos, 
    "Demon.*",
    Otc.North
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

---


---

## 🛤️ Pathfinding 📋

### 🧭 Sistema de Navegação 📝
```lua
-- Encontrar caminho básico
local startPos = {x = 1000, y = 1000, z = 7}
local goalPos = {x = 1010, y = 1010, z = 7}

local path, result = g_map.findPath(startPos, goalPos, 100)

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
```

### ⚡ Pathfinding Assíncrono 📝
```lua
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

### 🔍 Pathfinding Avançado 📝
```lua
-- Verificar linha de visão
local canSee = g_map.isSightClear(
    {x = 1000, y = 1000, z = 7},
    {x = 1005, y = 1005, z = 7}
)

if canSee then
    -- Verificação condicional
    print("Linha de visão livre")
else
    print("Visão bloqueada")
end
```

---


---

## 📡 Awareness Range 📋

### 🎯 Gerenciamento de Alcance 📝
```lua
-- Obter awareness range atual
    --  Obter awareness range atual (traduzido)
local awareRange = g_map.getAwareRange()
print("Aware Range:", awareRange.left, awareRange.right, awareRange.top, awareRange.bottom)

-- Definir awareness range customizado
    --  Definir awareness range customizado (traduzido)
g_map.setAwareRange({
    left = 8,
    right = 9,
    top = 6,
    bottom = 7
})

-- Resetar para o padrão
g_map.resetAwareRange()

-- Verificar se posição está no aware range
local pos = {x = 1000, y = 1000, z = 7}
local isAware = g_map.isAwareOfPosition(pos)
```

### 🌟 Floor Awareness 📝
#### Nível Basic
```lua
-- Obter range de floors visíveis
local firstFloor = g_map.getFirstAwareFloor()
local lastFloor = g_map.getLastAwareFloor()

print("Floors visíveis:", firstFloor .. " a " .. lastFloor)

-- Verificar cobertura de posição
local pos = {x = 1000, y = 1000, z = 7}
local isCovered = g_map.isCovered(pos, 0)
local isCompletelyCovered = g_map.isCompletelyCovered(pos, 0)
local canLook = g_map.isLookPossible(pos)
```

#### Nível Intermediate
```lua
-- Obter range de floors visíveis
local firstFloor = g_map.getFirstAwareFloor()
local lastFloor = g_map.getLastAwareFloor()

print("Floors visíveis:", firstFloor .. " a " .. lastFloor)

-- Verificar cobertura de posição
local pos = {x = 1000, y = 1000, z = 7}
local isCovered = g_map.isCovered(pos, 0)
local isCompletelyCovered = g_map.isCompletelyCovered(pos, 0)
local canLook = g_map.isLookPossible(pos)
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
local isCovered = g_map.isCovered(pos, 0)
local isCompletelyCovered = g_map.isCompletelyCovered(pos, 0)
local canLook = g_map.isLookPossible(pos)
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

---


---

## 🎥 MapView e Rendering 📋

### 📹 Sistema de Múltiplas Câmeras 📝
#### Nível Basic
```lua
-- MapViews são gerenciadas automaticamente pelo sistema
-- Cada widget de mapa possui sua própria MapView

-- Resetar câmera da MapView
g_map.resetLastCamera()

-- Notificar movimento da câmera
g_map.notificateCameraMove({x = 10, y = 5})
```

#### Nível Intermediate
```lua
-- MapViews são gerenciadas automaticamente pelo sistema
-- Cada widget de mapa possui sua própria MapView

-- Resetar câmera da MapView
g_map.resetLastCamera()

-- Notificar movimento da câmera
g_map.notificateCameraMove({x = 10, y = 5})
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

-- Resetar câmera da MapView
g_map.resetLastCamera()

-- Notificar movimento da câmera
g_map.notificateCameraMove({x = 10, y = 5})
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

### 💡 Sistema de Iluminação 📝
#### Nível Basic
```lua
-- Definir luz global do mapa
g_map.setLight({
    intensity = 255,
    color = 215
})

-- Obter configuração atual de luz
local light = g_map.getLight()
print("Intensidade da luz:", light.intensity)
print("Cor da luz:", light.color)

-- Ghost mode (transparência)
g_map.beginGhostMode(0.5)
-- ... fazer operações ...
g_map.endGhostMode()
```

#### Nível Intermediate
```lua
-- Definir luz global do mapa
g_map.setLight({
    intensity = 255,
    color = 215
})

-- Obter configuração atual de luz
local light = g_map.getLight()
print("Intensidade da luz:", light.intensity)
print("Cor da luz:", light.color)

-- Ghost mode (transparência)
g_map.beginGhostMode(0.5)
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
    intensity = 255,
    color = 215
})

-- Obter configuração atual de luz
local light = g_map.getLight()
print("Intensidade da luz:", light.intensity)
print("Cor da luz:", light.color)

-- Ghost mode (transparência)
g_map.beginGhostMode(0.5)
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

---


---

## 📝 Textos no Mundo 📋

### 📜 Textos Estáticos 📝
```lua
-- Adicionar texto estático
local staticText = StaticText.create()
staticText:setText("Loja de Armas")
staticText:setFont("verdana-11px-rounded")
staticText:setColor('#FFFF00')

g_map.addStaticText(staticText, {x = 1000, y = 1000, z = 7})

-- Buscar texto em posição
local foundText = g_map.getStaticText({x = 1000, y = 1000, z = 7})
if foundText then
    -- Verificação condicional
    print("Texto encontrado:", foundText:getText())
end
```

### ✨ Textos Animados 📝
```lua
-- Adicionar texto animado
    --  Adicionar texto animado (traduzido)
local animatedText = AnimatedText.create()
animatedText:setText("+50 EXP")
animatedText:setColor('#00FF00')
animatedText:setOffset({x = 0, y = -20})

g_map.addAnimatedText(animatedText, {x = 1000, y = 1000, z = 7})
```

---


---

## 🎯 Implementação Prática 📋

### 🏰 Sistema de Casas (Editor Mode) 📝
```lua
-- Configuração de zonas em modo editor
g_map.setShowZones(true)
g_map.setZoneOpacity(0.7)

-- Configurar cores de zona
    --  Configurar cores de zona (traduzido)
g_map.setZoneColor(TILESTATE_HOUSE, '#0000FF')
g_map.setZoneColor(TILESTATE_PROTECTIONZONE, '#00FF00')
g_map.setZoneColor(TILESTATE_OPTIONALZONE, '#FFFF00')
```

### 📊 Sistema de Minimapa 📝
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

### 🎮 Sistema de Jogo Integrado 📝
```lua
-- Exemplo: Sistema de Teleporte
    --  Exemplo: Sistema de Teleporte (traduzido)
function teleportPlayer(targetPos)
    -- Função: teleportPlayer
    local player = g_game.getLocalPlayer()
    if not player then return end
    -- Verificação condicional
    
    local currentPos = player:getPosition()
    
    if not g_map.isLookPossible(targetPos) then
    -- Verificação condicional
        print("Posição de destino inválida")
        return
    end
    
    g_map.removeThing(player)
    g_map.addThing(player, targetPos)
    g_map.setCentralPosition(targetPos)
    
    print("Jogador teleportado de", currentPos, "para", targetPos)
end
```

---


---

## ✅ Melhores Práticas 📋

### 🛡️ Performance e Otimização 📝
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

### 🔒 Validação e Segurança 📝
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
```

### 🎯 Pathfinding Eficiente 📝
```lua
-- ✅ BOM: Usar complexidade apropriada
    --  ✅ BOM: Usar complexidade apropriada (traduzido)
local function findPathSmart(start, goal)
    local distance = math.abs(start.x - goal.x) + math.abs(start.y - goal.y)
    local complexity = math.min(distance * 2, 500)
    
    return g_map.findPath(start, goal, complexity)
end

-- ✅ BOM: Cache de pathfinding
    --  ✅ BOM: Cache de pathfinding (traduzido)
local pathCache = {}
local CACHE_DURATION = 5000

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
> - [[Getting_Started_Guide]] - Comece aqui
> - [[Module_System_Guide]] - Sistema de módulos
> - [[UI_System_Guide]] - Interface do usuário
> - [[Lua_API_Reference]] - Referência da API

---

> [!success] **Navegação**
> **📚 Documentos Relacionados:**
> - [[Getting_Started_Guide]] - Comece aqui
> - [[Module_System_Guide]] - Sistema de módulos
> - [[UI_System_Guide]] - Interface do usuário
> - [[Lua_API_Reference]] - API completa
> 
> **🔗 Navegação Rápida:**
> - [[Wiki_Index]] - Voltar ao índice
> - [[Cheat_Sheet]] - Referência rápida
> - [[Debug_System_Guide]] - Debugging

