---
tags: [otclient, sistema, mapas, renderização, tiles, posição, wiki]
type: wiki_page
status: published
priority: high
created: 2025-08-05
updated: 2025-08-05
---

# 🗺️ **Sistema de Mapas - OTClient**

> [!info] **Sistema de Renderização de Mapas**
> O sistema de mapas do OTClient é responsável por renderizar o mundo do jogo, gerenciar tiles, posições e fornecer funcionalidades de navegação e visualização.

---

## 📋 **Visão Geral**

O **Sistema de Mapas** do OTClient é o núcleo da renderização do mundo do jogo, responsável por:

- **Renderização de Tiles**: Exibição de itens, criaturas e efeitos no mapa
- **Gerenciamento de Posições**: Sistema de coordenadas 3D (X, Y, Z)
- **Navegação**: Pathfinding e movimento pelo mapa
- **Minimap**: Interface de navegação em miniatura
- **Otimização**: Renderização eficiente de grandes áreas

---

## 🏗️ **Arquitetura do Sistema**

### **Componentes Principais**

```cpp
// Estrutura principal do sistema de mapas
class Map {
    std::vector<Floor> m_floors;           // Andares do mapa
    std::vector<MapViewPtr> m_mapViews;    // Visualizações do mapa
    Position m_centerPosition;             // Posição central
    uint8_t m_awareRange;                  // Alcance de visão
};
```

### **Hierarquia de Objetos**

```
Map
├── Floor (Andar)
│   ├── Tile (Bloco)
│   │   ├── Item (Item)
│   │   ├── Creature (Criatura)
│   │   └── Effect (Efeito)
│   └── Position (Posição)
└── MapView (Visualização)
    ├── Camera (Câmera)
    └── Viewport (Área de Visualização)
```

---

## 🔧 **APIs e Interfaces**

### **Gerenciamento de Tiles**

```lua
-- Adicionar coisa ao mapa
g_map.addThing(thing, position, stackPos)

-- Remover coisa do mapa
g_map.removeThingByPos(position, stackPos)

-- Obter coisa em posição
local thing = g_map.getThing(position, stackPos)

-- Encontrar itens por ID
local items = g_map.findItemsById(itemId, maxCount)
```

### **Navegação e Pathfinding**

```lua
-- Encontrar caminho entre posições
local path, result = g_map.findPath(startPos, goalPos, maxComplexity, flags)

-- Obter espectadores em área
local creatures = g_map.getSpectatorsInRangeEx(centerPos, multiFloor, minX, maxX, minY, maxY)

-- Verificar se posição está coberta
local isCovered = g_map.isCovered(position, firstFloor)
```

### **Gerenciamento de Posições**

```lua
-- Criar posição
local pos = Position(x, y, z)

-- Verificar se posição é válida
local isValid = pos:isMapPosition()

-- Calcular distância entre posições
local distance = pos:getDistanceFrom(otherPos)

-- Obter posição relativa
local relative = pos:translated(direction)
```

---

## 📚 **Exemplos Práticos**

### **Exemplo 1: Sistema de Auto-Navegação**

```lua
-- Sistema básico de navegação automática
local function autoWalkTo(targetPosition)
    local player = g_game.getLocalPlayer()
    if not player then return false end
    
    local currentPos = player:getPosition()
    local path, result = g_map.findPath(currentPos, targetPosition, 1000, 0)
    
    if result == Otc.PathFindResult.Ok then
        for _, direction in ipairs(path) do
            g_game.walk(direction)
            scheduleEvent(function() end, 500) -- Aguarda 500ms
        end
        return true
    end
    
    return false
end

-- Uso: autoWalkTo(Position(100, 100, 7))
```

### **Exemplo 2: Sistema de Monitoramento de Área**

```lua
-- Monitorar criaturas em área específica
local function monitorArea(centerPos, range)
    local creatures = g_map.getSpectatorsInRangeEx(
        centerPos, 
        true,  -- multiFloor
        -range, range, -range, range
    )
    
    for _, creature in ipairs(creatures) do
        if creature:isMonster() then
            print("Monstro detectado: " .. creature:getName())
        elseif creature:isPlayer() then
            print("Jogador detectado: " .. creature:getName())
        end
    end
    
    return creatures
end

-- Uso: monitorArea(g_game.getLocalPlayer():getPosition(), 5)
```

### **Exemplo 3: Sistema de Coleta Automática**

```lua
-- Coletar itens específicos em área
local function collectItems(itemIds, maxDistance)
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    local playerPos = player:getPosition()
    
    for _, itemId in ipairs(itemIds) do
        local items = g_map.findItemsById(itemId, 100)
        
        for pos, item in pairs(items) do
            local distance = playerPos:getDistanceFrom(pos)
            
            if distance <= maxDistance then
                local path, result = g_map.findPath(playerPos, pos, 1000, 0)
                
                if result == Otc.PathFindResult.Ok then
                    -- Navegar até o item
                    for _, direction in ipairs(path) do
                        g_game.walk(direction)
                        scheduleEvent(function() end, 300)
                    end
                    
                    -- Coletar o item
                    g_game.move(item, playerPos, 1)
                    break
                end
            end
        end
    end
end

-- Uso: collectItems({3031, 3035}, 10) -- Coletar gold coins e platinum coins
```

---

## 🎮 **Sistema de Minimap**

### **Funcionalidades da Minimap**

```lua
-- Controle da minimap
local function setupMinimap()
    -- Configurar zoom
    mapController.ui.minimapBorder.minimap:setZoom(1.0)
    
    -- Configurar posição da câmera
    local player = g_game.getLocalPlayer()
    if player then
        local pos = player:getPosition()
        mapController.ui.minimapBorder.minimap:setCameraPosition(pos)
    end
end

-- Adicionar marcação na minimap
local function addMinimapMark(position, icon, message)
    g_game.addAutomapFlag(position, icon, message)
end

-- Remover marcação da minimap
local function removeMinimapMark(position, icon, message)
    g_game.removeAutomapFlag(position, icon, message)
end
```

### **Exemplo: Sistema de Waypoints**

```lua
-- Sistema de waypoints na minimap
local waypoints = {}

local function addWaypoint(name, position, icon)
    waypoints[name] = {
        position = position,
        icon = icon or 0,
        message = name
    }
    
    g_game.addAutomapFlag(position, icon, name)
    print("Waypoint adicionado: " .. name)
end

local function goToWaypoint(name)
    local waypoint = waypoints[name]
    if waypoint then
        autoWalkTo(waypoint.position)
    else
        print("Waypoint não encontrado: " .. name)
    end
end

-- Uso:
-- addWaypoint("Depot", Position(100, 100, 7), 0)
-- goToWaypoint("Depot")
```

---

## 🔍 **Otimização e Performance**

### **Técnicas de Otimização**

```lua
-- Configurar alcance de consciência
local function optimizeMapRendering()
    -- Reduzir alcance para melhor performance
    g_game.changeMapAwareRange(8, 6) -- X: 8, Y: 6
    
    -- Configurar renderização de animações
    g_map.setShowAnimations(true)
    g_map.setForceShowAnimations(false)
end

-- Sistema de culling para otimização
local function setupEfficientRendering()
    -- Renderizar apenas tiles visíveis
    for _, mapView in ipairs(g_map.getMapViews()) do
        mapView:setVisibleDimension(Size(15, 11)) -- 15x11 tiles visíveis
    end
end
```

### **Monitoramento de Performance**

```lua
-- Monitorar performance do mapa
local function monitorMapPerformance()
    local startTime = g_clock.millis()
    
    -- Operação de renderização
    g_map.notificateTileUpdate(position, thing, operation)
    
    local endTime = g_clock.millis()
    local duration = endTime - startTime
    
    if duration > 16 then -- Mais de 16ms (60 FPS)
        print("Performance baixa detectada: " .. duration .. "ms")
    end
end
```

---

## 🔗 **Integração com Outros Sistemas**

### **Sistema de Eventos**

```lua
-- Conectar eventos do mapa
connect(g_map, {
    onTileUpdate = function(position, thing, operation)
        if operation == Otc.OperationAdd then
            print("Item adicionado em: " .. position:toString())
        elseif operation == Otc.OperationRemove then
            print("Item removido de: " .. position:toString())
        end
    end
})
```

### **Sistema de UI**

```lua
-- Interface de controle do mapa
local function createMapControlUI()
    local window = g_ui.createWidget('MainWindow')
    window:setText('Controle do Mapa')
    
    local zoomSlider = g_ui.createWidget('Slider', window)
    zoomSlider:setRange(0.5, 3.0)
    zoomSlider:setValue(1.0)
    zoomSlider.onValueChange = function(value)
        for _, mapView in ipairs(g_map.getMapViews()) do
            mapView:setZoom(value)
        end
    end
    
    return window
end
```

---

## 📊 **Dependências e Relacionamentos**

### **Dependências Principais**
- **Sistema de Gráficos**: Renderização de sprites e efeitos
- **Sistema de Eventos**: Comunicação entre componentes
- **Sistema de Protocolo**: Recebimento de dados do servidor
- **Sistema de UI**: Interface de usuário

### **Sistemas Dependentes**
- **Sistema de Combate**: Posicionamento de criaturas
- **Sistema de Inventário**: Posicionamento de itens
- **Sistema de NPCs**: Posicionamento de NPCs
- **Sistema de Quests**: Marcações no mapa

---

## 🚀 **Melhores Práticas**

### **Otimização de Código**

1. **Use Pathfinding com Limites**: Defina `maxComplexity` para evitar loops infinitos
2. **Cache de Posições**: Evite recriar objetos `Position` frequentemente
3. **Renderização Eficiente**: Use `setShowAnimations(false)` quando não necessário
4. **Gerenciamento de Memória**: Limpe referências não utilizadas

### **Padrões de Design**

```lua
-- Padrão Observer para mudanças no mapa
local MapObserver = {
    observers = {},
    
    addObserver = function(callback)
        table.insert(MapObserver.observers, callback)
    end,
    
    notify = function(event, data)
        for _, observer in ipairs(MapObserver.observers) do
            observer(event, data)
        end
    end
}

-- Uso
MapObserver.addObserver(function(event, data)
    if event == 'tileUpdate' then
        print("Tile atualizado: " .. data.position:toString())
    end
end)
```

---

## 📚 **Referências e Links**

### **Arquivos Relacionados**
- [[otclient_sistema_graficos|Sistema de Gráficos]]
- [[otclient_sistema_eventos|Sistema de Eventos]]
- [[otclient_sistema_protocolo|Sistema de Protocolo]]

### **APIs Principais**
- `g_map`: API principal do sistema de mapas
- `Position`: Classe para gerenciamento de posições
- `Tile`: Classe para gerenciamento de tiles
- `MapView`: Classe para visualização do mapa

### **Constantes Importantes**
```lua
-- Tipos de operação
Otc.OperationAdd = 0
Otc.OperationRemove = 1
Otc.OperationMove = 2

-- Resultados de pathfinding
Otc.PathFindResult.Ok = 0
Otc.PathFindResult.NoWay = 1
Otc.PathFindResult.TooFar = 2
```

---

> [!success] **Conclusão**
> O Sistema de Mapas do OTClient fornece uma base sólida para renderização e navegação no mundo do jogo, com APIs poderosas para pathfinding, gerenciamento de tiles e otimização de performance.

---

**📖 Próximo**: [[otclient_sistema_combate|Sistema de Combate]] | **🔙 Anterior**: [[otclient_sistema_comunicacao|Sistema de Comunicação]] 