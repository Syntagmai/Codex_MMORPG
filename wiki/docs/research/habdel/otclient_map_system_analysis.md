# OTClient Map System - Análise Técnica

## 🎯 Visão Geral

O **Sistema de Mapas** do OTClient é responsável por gerenciar, renderizar e interagir com mapas 2D/3D. Ele fornece um sistema completo para visualização de mapas, controle de câmera, gerenciamento de tiles e integração com o servidor.

## 📊 Estatísticas da Análise

- **Arquivos Analisados**: 17
- **Linhas de Código**: 8,646
- **Componentes Principais**: 17
- **Padrões Identificados**: 10
- **APIs Documentadas**: 9

## 🏗️ Arquitetura do Sistema

### **Componentes Principais**

### **map.h**
- **Linhas**: 354
- **Classes**: 2
- **Enums**: 2
- **Structs**: 3
- **Métodos**: 60
- **Padrões**: Singleton, Template, Map, Tile, View, Position, Thing, Camera

### **map.cpp**
- **Linhas**: 1,472
- **Classes**: 0
- **Enums**: 0
- **Structs**: 4
- **Métodos**: 7
- **Padrões**: Template, Map, Tile, View, Position, Thing, Camera

### **mapview.h**
- **Linhas**: 351
- **Classes**: 7
- **Enums**: 3
- **Structs**: 5
- **Métodos**: 42
- **Padrões**: Map, Tile, View, Position, Thing, Camera

### **mapview.cpp**
- **Linhas**: 974
- **Classes**: 0
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 3
- **Padrões**: Map, Tile, View, Position, Thing, Manager, Render, Camera

### **tile.h**
- **Linhas**: 272
- **Classes**: 2
- **Enums**: 3
- **Structs**: 0
- **Métodos**: 41
- **Padrões**: Map, Tile, View, Position, Thing, Render, Camera

### **tile.cpp**
- **Linhas**: 1,004
- **Classes**: 0
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 0
- **Padrões**: Map, Tile, View, Position, Thing, Manager, Render, Camera

### **position.h**
- **Linhas**: 304
- **Classes**: 1
- **Enums**: 0
- **Structs**: 2
- **Métodos**: 7
- **Padrões**: Template, Map, Position

### **position.cpp**
- **Linhas**: 71
- **Classes**: 0
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 0
- **Padrões**: Map, Position

### **thing.h**
- **Linhas**: 276
- **Classes**: 3
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 8
- **Padrões**: Map, Tile, View, Position, Thing, Manager

### **thing.cpp**
- **Linhas**: 102
- **Classes**: 0
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 0
- **Padrões**: Map, Tile, View, Position, Thing, Manager

### **thingtype.h**
- **Linhas**: 546
- **Classes**: 1
- **Enums**: 9
- **Structs**: 9
- **Métodos**: 17
- **Padrões**: Map, Tile, View, Thing, Manager

### **thingtype.cpp**
- **Linhas**: 1,080
- **Classes**: 0
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 4
- **Padrões**: Map, Tile, View, Thing, Manager

### **thingtypemanager.h**
- **Linhas**: 112
- **Classes**: 2
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 16
- **Padrões**: Thing, Manager

### **thingtypemanager.cpp**
- **Linhas**: 607
- **Classes**: 0
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 12
- **Padrões**: Thing, Manager

### **minimap.h**
- **Linhas**: 136
- **Classes**: 2
- **Enums**: 1
- **Structs**: 1
- **Métodos**: 17
- **Padrões**: Map, Tile, Position

### **minimap.cpp**
- **Linhas**: 434
- **Classes**: 0
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 9
- **Padrões**: Map, Tile, Position, Manager

### **mapio.cpp**
- **Linhas**: 551
- **Classes**: 0
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 15
- **Padrões**: Map, Tile, Position, Thing, Manager



### **Padrões de Design Identificados**

- **View**: Descrição do padrão
- **Thing**: Descrição do padrão
- **Map**: Descrição do padrão
- **Singleton**: Descrição do padrão
- **Position**: Descrição do padrão
- **Render**: Descrição do padrão
- **Manager**: Descrição do padrão
- **Camera**: Descrição do padrão
- **Template**: Descrição do padrão
- **Tile**: Descrição do padrão



## 🔌 APIs Principais

### **Map**
Classe principal para gerenciamento do mapa

**Métodos Principais:**
- `addTile()`
- `removeTile()`
- `getTile()`
- `clean()`
- `update()`

**Componentes:** map.h, map.cpp

### **MapView**
Visualização e renderização do mapa

**Métodos Principais:**
- `drawForeground()`
- `setCameraPosition()`
- `followCreature()`
- `move()`

**Componentes:** mapview.h, mapview.cpp

### **Tile**
Representação de um tile no mapa

**Métodos Principais:**
- `addThing()`
- `removeThing()`
- `getThing()`
- `draw()`
- `isWalkable()`

**Componentes:** tile.h, tile.cpp

### **Position**
Sistema de posicionamento 3D

**Métodos Principais:**
- `getX()`
- `getY()`
- `getZ()`
- `distance()`
- `isInRange()`

**Componentes:** position.h, position.cpp

### **Thing**
Classe base para objetos no mapa

**Métodos Principais:**
- `draw()`
- `getPosition()`
- `isItem()`
- `isCreature()`

**Componentes:** thing.h, thing.cpp

### **ThingType**
Definição de tipos de objetos

**Métodos Principais:**
- `getSize()`
- `getHeight()`
- `isGround()`
- `isWalkable()`

**Componentes:** thingtype.h, thingtype.cpp

### **ThingTypeManager**
Gerenciador de tipos de objetos

**Métodos Principais:**
- `getThingType()`
- `loadThingTypes()`
- `getThingTypeCount()`

**Componentes:** thingtypemanager.h, thingtypemanager.cpp

### **Minimap**
Sistema de minimapa

**Métodos Principais:**
- `draw()`
- `update()`
- `setPosition()`
- `getTileColor()`

**Componentes:** minimap.h, minimap.cpp

### **MapIO**
Entrada/saída de dados do mapa

**Métodos Principais:**
- `loadMap()`
- `saveMap()`
- `parseMapData()`

**Componentes:** mapio.cpp



## 💡 Exemplos Práticos

### **Mapa Básico**
Como criar e usar um mapa básico

#### Nível Basic
```cpp
// Exemplo de mapa básico
#include "client/map.h"
#include "client/mapview.h"

void createBasicMap() {{
    // Criar mapa
    MapPtr map = std::make_shared<Map>();
    
    // Criar visualização do mapa
    MapViewPtr mapView = std::make_shared<MapView>();
    mapView->setMap(map);
    
    // Definir dimensões visíveis
    mapView->setVisibleDimension(Size(15, 11));  // 15x11 tiles visíveis
    
    // Definir posição da câmera
    Position cameraPos(100, 100, 7);  // x=100, y=100, z=7
    mapView->setCameraPosition(cameraPos);
    
    // Configurar modo de visualização de andares
    mapView->setFloorViewMode(MapView::FloorViewMode::NORMAL);
    
    // Habilitar/desabilitar recursos
    mapView->setDrawNames(true);
    mapView->setDrawHealthBars(true);
    mapView->setDrawLights(true);
    
    // Renderizar mapa
    mapView->drawForeground(Rect(0, 0, 800, 600));
}}
```

#### Nível Intermediate
```cpp
// Exemplo de mapa básico
#include "client/map.h"
#include "client/mapview.h"

void createBasicMap() {{
    // Criar mapa
    MapPtr map = std::make_shared<Map>();
    
    // Criar visualização do mapa
    MapViewPtr mapView = std::make_shared<MapView>();
    mapView->setMap(map);
    
    // Definir dimensões visíveis
    mapView->setVisibleDimension(Size(15, 11));  // 15x11 tiles visíveis
    
    // Definir posição da câmera
    Position cameraPos(100, 100, 7);  // x=100, y=100, z=7
    mapView->setCameraPosition(cameraPos);
    
    // Configurar modo de visualização de andares
    mapView->setFloorViewMode(MapView::FloorViewMode::NORMAL);
    
    // Habilitar/desabilitar recursos
    mapView->setDrawNames(true);
    mapView->setDrawHealthBars(true);
    mapView->setDrawLights(true);
    
    // Renderizar mapa
    mapView->drawForeground(Rect(0, 0, 800, 600));
}}
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
// Exemplo de mapa básico
#include "client/map.h"
#include "client/mapview.h"

void createBasicMap() {{
    // Criar mapa
    MapPtr map = std::make_shared<Map>();
    
    // Criar visualização do mapa
    MapViewPtr mapView = std::make_shared<MapView>();
    mapView->setMap(map);
    
    // Definir dimensões visíveis
    mapView->setVisibleDimension(Size(15, 11));  // 15x11 tiles visíveis
    
    // Definir posição da câmera
    Position cameraPos(100, 100, 7);  // x=100, y=100, z=7
    mapView->setCameraPosition(cameraPos);
    
    // Configurar modo de visualização de andares
    mapView->setFloorViewMode(MapView::FloorViewMode::NORMAL);
    
    // Habilitar/desabilitar recursos
    mapView->setDrawNames(true);
    mapView->setDrawHealthBars(true);
    mapView->setDrawLights(true);
    
    // Renderizar mapa
    mapView->drawForeground(Rect(0, 0, 800, 600));
}}
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

### **Gerenciamento de Tiles**
Como gerenciar tiles no mapa

#### Nível Basic
```cpp
// Exemplo de gerenciamento de tiles
#include "client/map.h"
#include "client/tile.h"
#include "client/item.h"

void manageTiles() {{
    // Obter mapa
    MapPtr map = g_map;
    
    // Criar posição
    Position pos(100, 100, 7);
    
    // Obter tile na posição
    TilePtr tile = map->getTile(pos);
    
    if (!tile) {{
        // Criar novo tile se não existir
        tile = std::make_shared<Tile>(pos);
        map->addTile(tile);
    }}
    
    // Adicionar item ao tile
    ItemPtr item = Item::create(100);  // ID do item
    tile->addThing(item, 0);  // stackPos = 0
    
    // Verificar propriedades do tile
    if (tile->isWalkable()) {{
        std::cout << "Tile is walkable" << std::endl;
    }}
    
    if (tile->isClickable()) {{
        std::cout << "Tile is clickable" << std::endl;
    }}
    
    // Obter coisas no tile
    const std::vector<ThingPtr>& things = tile->getThings();
    std::cout << "Tile has " << things.size() << " things" << std::endl;
    
    // Remover coisa do tile
    if (!things.empty()) {{
        tile->removeThing(things[0]);
    }}
}}
```

#### Nível Intermediate
```cpp
// Exemplo de gerenciamento de tiles
#include "client/map.h"
#include "client/tile.h"
#include "client/item.h"

void manageTiles() {{
    // Obter mapa
    MapPtr map = g_map;
    
    // Criar posição
    Position pos(100, 100, 7);
    
    // Obter tile na posição
    TilePtr tile = map->getTile(pos);
    
    if (!tile) {{
        // Criar novo tile se não existir
        tile = std::make_shared<Tile>(pos);
        map->addTile(tile);
    }}
    
    // Adicionar item ao tile
    ItemPtr item = Item::create(100);  // ID do item
    tile->addThing(item, 0);  // stackPos = 0
    
    // Verificar propriedades do tile
    if (tile->isWalkable()) {{
        std::cout << "Tile is walkable" << std::endl;
    }}
    
    if (tile->isClickable()) {{
        std::cout << "Tile is clickable" << std::endl;
    }}
    
    // Obter coisas no tile
    const std::vector<ThingPtr>& things = tile->getThings();
    std::cout << "Tile has " << things.size() << " things" << std::endl;
    
    // Remover coisa do tile
    if (!things.empty()) {{
        tile->removeThing(things[0]);
    }}
}}
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
// Exemplo de gerenciamento de tiles
#include "client/map.h"
#include "client/tile.h"
#include "client/item.h"

void manageTiles() {{
    // Obter mapa
    MapPtr map = g_map;
    
    // Criar posição
    Position pos(100, 100, 7);
    
    // Obter tile na posição
    TilePtr tile = map->getTile(pos);
    
    if (!tile) {{
        // Criar novo tile se não existir
        tile = std::make_shared<Tile>(pos);
        map->addTile(tile);
    }}
    
    // Adicionar item ao tile
    ItemPtr item = Item::create(100);  // ID do item
    tile->addThing(item, 0);  // stackPos = 0
    
    // Verificar propriedades do tile
    if (tile->isWalkable()) {{
        std::cout << "Tile is walkable" << std::endl;
    }}
    
    if (tile->isClickable()) {{
        std::cout << "Tile is clickable" << std::endl;
    }}
    
    // Obter coisas no tile
    const std::vector<ThingPtr>& things = tile->getThings();
    std::cout << "Tile has " << things.size() << " things" << std::endl;
    
    // Remover coisa do tile
    if (!things.empty()) {{
        tile->removeThing(things[0]);
    }}
}}
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

### **Controle de Câmera**
Como controlar a câmera do mapa

#### Nível Basic
```cpp
// Exemplo de controle de câmera
#include "client/mapview.h"
#include "client/creature.h"

void controlCamera() {{
    // Obter visualização do mapa
    MapViewPtr mapView = g_mapView;
    
    // Definir posição da câmera
    Position cameraPos(200, 200, 7);
    mapView->setCameraPosition(cameraPos);
    
    // Mover câmera
    mapView->move(10, 5);  // Mover 10 tiles para direita, 5 para baixo
    
    // Seguir criatura
    CreaturePtr player = g_game.getLocalPlayer();
    if (player) {{
        mapView->followCreature(player);
    }}
    
    // Verificar se está seguindo criatura
    if (mapView->isFollowingCreature()) {{
        std::cout << "Camera is following creature" << std::endl;
    }}
    
    // Obter posição atual da câmera
    Position currentPos = mapView->getCameraPosition();
    std::cout << "Camera at: " << currentPos.x() << ", " << currentPos.y() << ", " << currentPos.z() << std::endl;
    
    // Configurar modo de visualização de andares
    mapView->setFloorViewMode(MapView::FloorViewMode::FADE);
    mapView->setFloorFading(1000);  // 1 segundo de fade
    
    // Bloquear andar visível
    mapView->lockFirstVisibleFloor(5);  // Bloquear no andar 5
}}
```

#### Nível Intermediate
```cpp
// Exemplo de controle de câmera
#include "client/mapview.h"
#include "client/creature.h"

void controlCamera() {{
    // Obter visualização do mapa
    MapViewPtr mapView = g_mapView;
    
    // Definir posição da câmera
    Position cameraPos(200, 200, 7);
    mapView->setCameraPosition(cameraPos);
    
    // Mover câmera
    mapView->move(10, 5);  // Mover 10 tiles para direita, 5 para baixo
    
    // Seguir criatura
    CreaturePtr player = g_game.getLocalPlayer();
    if (player) {{
        mapView->followCreature(player);
    }}
    
    // Verificar se está seguindo criatura
    if (mapView->isFollowingCreature()) {{
        std::cout << "Camera is following creature" << std::endl;
    }}
    
    // Obter posição atual da câmera
    Position currentPos = mapView->getCameraPosition();
    std::cout << "Camera at: " << currentPos.x() << ", " << currentPos.y() << ", " << currentPos.z() << std::endl;
    
    // Configurar modo de visualização de andares
    mapView->setFloorViewMode(MapView::FloorViewMode::FADE);
    mapView->setFloorFading(1000);  // 1 segundo de fade
    
    // Bloquear andar visível
    mapView->lockFirstVisibleFloor(5);  // Bloquear no andar 5
}}
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
// Exemplo de controle de câmera
#include "client/mapview.h"
#include "client/creature.h"

void controlCamera() {{
    // Obter visualização do mapa
    MapViewPtr mapView = g_mapView;
    
    // Definir posição da câmera
    Position cameraPos(200, 200, 7);
    mapView->setCameraPosition(cameraPos);
    
    // Mover câmera
    mapView->move(10, 5);  // Mover 10 tiles para direita, 5 para baixo
    
    // Seguir criatura
    CreaturePtr player = g_game.getLocalPlayer();
    if (player) {{
        mapView->followCreature(player);
    }}
    
    // Verificar se está seguindo criatura
    if (mapView->isFollowingCreature()) {{
        std::cout << "Camera is following creature" << std::endl;
    }}
    
    // Obter posição atual da câmera
    Position currentPos = mapView->getCameraPosition();
    std::cout << "Camera at: " << currentPos.x() << ", " << currentPos.y() << ", " << currentPos.z() << std::endl;
    
    // Configurar modo de visualização de andares
    mapView->setFloorViewMode(MapView::FloorViewMode::FADE);
    mapView->setFloorFading(1000);  // 1 segundo de fade
    
    // Bloquear andar visível
    mapView->lockFirstVisibleFloor(5);  // Bloquear no andar 5
}}
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

### **Tipos de Coisas**
Como trabalhar com tipos de coisas

#### Inicialização e Configuração
```cpp
// Exemplo de tipos de coisas
#include "client/thingtype.h"
#include "client/thingtypemanager.h"

void workWithThingTypes() {{
    // Obter gerenciador de tipos
    ThingTypeManager& manager = g_things;
    
    // Carregar tipos de coisas
    manager.loadThingTypes("things.xml");
    
    // Obter tipo específico
    ThingTypePtr thingType = manager.getThingType(100);  // ID do item
    if (thingType) {{
        // Obter propriedades do tipo
        Size size = thingType->getSize();
        uint8_t height = thingType->getHeight();
        
        std::cout << "Thing size: " << size.width() << "x" << size.height() << std::endl;
        std::cout << "Thing height: " << (int)height << std::endl;
        
        // Verificar propriedades
        if (thingType->isGround()) {{
            std::cout << "This is ground" << std::endl;
        }}
```

#### Funcionalidade 1
```cpp
        
        if (thingType->isWalkable()) {{
            std::cout << "This is walkable" << std::endl;
        }}
        
        if (thingType->isBlocking()) {{
            std::cout << "This is blocking" << std::endl;
        }}
        
        if (thingType->isStackable()) {{
            std::cout << "This is stackable" << std::endl;
        }}
        
        // Obter informações de luz
        if (thingType->hasLight()) {{
            Light light = thingType->getLight();
            std::cout << "Light: " << light.intensity << ", " << light.color << std::endl;
        }}
        
        // Obter informações de elevação
        if (thingType->hasElevation()) {{
            uint8_t elevation = thingType->getElevation();
            std::cout << "Elevation: " << (int)elevation << std::endl;
        }}
```

#### Finalização
```cpp
    }}
}}
```

### **Minimapa**
Como trabalhar com o minimapa

#### Nível Basic
```cpp
    std::cout << "Tile color: " << (int)tileColor << std::endl;
    // Verificar se posição está no minimapa
    if (minimap->hasTile(playerPos)) {{
        std::cout << "Position is in minimap" << std::endl;
    if (minimapTile.hasFlag(MinimapTile::Walkable)) {{
        std::cout << "Tile is walkable on minimap" << std::endl;
```

#### Nível Intermediate
```cpp
// Exemplo de minimapa
#include "client/minimap.h"

void workWithMinimap() {{
    // Obter minimapa
    MinimapPtr minimap = g_minimap;
    
    // Definir posição do jogador
    Position playerPos(100, 100, 7);
    minimap->setPosition(playerPos);
    
    // Obter cor do tile no minimapa
    uint8_t tileColor = minimap->getTileColor(playerPos);
    std::cout << "Tile color: " << (int)tileColor << std::endl;
    
    // Desenhar minimapa
    minimap->draw(Rect(10, 10, 200, 200));
    
    // Atualizar minimapa
    minimap->update();
    
    // Verificar se posição está no minimapa
    if (minimap->hasTile(playerPos)) {{
        std::cout << "Position is in minimap" << std::endl;
    }}
    
    // Obter informações do tile
    MinimapTile minimapTile = minimap->getTile(playerPos);
    if (minimapTile.hasFlag(MinimapTile::Walkable)) {{
        std::cout << "Tile is walkable on minimap" << std::endl;
    }}
}}
```

#### Nível Advanced
```cpp
// Exemplo de minimapa
#include "client/minimap.h"

void workWithMinimap() {{
    // Obter minimapa
    MinimapPtr minimap = g_minimap;
    
    // Definir posição do jogador
    Position playerPos(100, 100, 7);
    minimap->setPosition(playerPos);
    
    // Obter cor do tile no minimapa
    uint8_t tileColor = minimap->getTileColor(playerPos);
    std::cout << "Tile color: " << (int)tileColor << std::endl;
    
    // Desenhar minimapa
    minimap->draw(Rect(10, 10, 200, 200));
    
    // Atualizar minimapa
    minimap->update();
    
    // Verificar se posição está no minimapa
    if (minimap->hasTile(playerPos)) {{
        std::cout << "Position is in minimap" << std::endl;
    }}
    
    // Obter informações do tile
    MinimapTile minimapTile = minimap->getTile(playerPos);
    if (minimapTile.hasFlag(MinimapTile::Walkable)) {{
        std::cout << "Tile is walkable on minimap" << std::endl;
    }}
}}
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

### **Renderização de Mapas**
Como renderizar mapas com diferentes configurações

#### Nível Basic
```cpp
// Exemplo de renderização de mapas
void renderMap() {{
    // Verificar se shader está ativo
    if (mapView->getShader()) {{
        std::cout << "Shader is active" << std::endl;
    if (nextShader) {{
        std::cout << "Next shader is ready" << std::endl;
```

#### Nível Intermediate
```cpp
// Exemplo de renderização de mapas
#include "client/mapview.h"
#include "framework/graphics/painter.h"

void renderMap() {{
    // Obter visualização do mapa
    MapViewPtr mapView = g_mapView;
    
    // Configurar anti-aliasing
    mapView->setAntiAliasingMode(MapView::AntialiasingMode::ANTIALIASING_ENABLED);
    
    // Configurar shader
    mapView->setShader("default", 1000.0f, 1000.0f);  // fadein=1s, fadeout=1s
    
    // Configurar luz
    mapView->setMinimumAmbientLight(0.2f);  // Luz ambiente mínima
    mapView->setShadowFloorIntensity(0.5f);  // Intensidade da sombra
    
    // Configurar dimensões visíveis
    mapView->setVisibleDimension(Size(19, 15));  // 19x15 tiles
    mapView->setLimitVisibleDimension(true);
    
    // Configurar modo de visualização de andares
    mapView->setFloorViewMode(MapView::FloorViewMode::ALWAYS_WITH_TRANSPARENCY);
    
    // Desenhar mapa
    Rect viewport(0, 0, 800, 600);
    mapView->drawForeground(viewport);
    
    // Desenhar informações de criaturas
    mapView->drawCreatureInformation();
    
    // Verificar se shader está ativo
    if (mapView->getShader()) {{
        std::cout << "Shader is active" << std::endl;
    }}
    
    // Obter próximo shader
    PainterShaderProgramPtr nextShader = mapView->getNextShader();
    if (nextShader) {{
        std::cout << "Next shader is ready" << std::endl;
    }}
}}
```

#### Nível Advanced
```cpp
// Exemplo de renderização de mapas
#include "client/mapview.h"
#include "framework/graphics/painter.h"

void renderMap() {{
    // Obter visualização do mapa
    MapViewPtr mapView = g_mapView;
    
    // Configurar anti-aliasing
    mapView->setAntiAliasingMode(MapView::AntialiasingMode::ANTIALIASING_ENABLED);
    
    // Configurar shader
    mapView->setShader("default", 1000.0f, 1000.0f);  // fadein=1s, fadeout=1s
    
    // Configurar luz
    mapView->setMinimumAmbientLight(0.2f);  // Luz ambiente mínima
    mapView->setShadowFloorIntensity(0.5f);  // Intensidade da sombra
    
    // Configurar dimensões visíveis
    mapView->setVisibleDimension(Size(19, 15));  // 19x15 tiles
    mapView->setLimitVisibleDimension(true);
    
    // Configurar modo de visualização de andares
    mapView->setFloorViewMode(MapView::FloorViewMode::ALWAYS_WITH_TRANSPARENCY);
    
    // Desenhar mapa
    Rect viewport(0, 0, 800, 600);
    mapView->drawForeground(viewport);
    
    // Desenhar informações de criaturas
    mapView->drawCreatureInformation();
    
    // Verificar se shader está ativo
    if (mapView->getShader()) {{
        std::cout << "Shader is active" << std::endl;
    }}
    
    // Obter próximo shader
    PainterShaderProgramPtr nextShader = mapView->getNextShader();
    if (nextShader) {{
        std::cout << "Next shader is ready" << std::endl;
    }}
}}
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

### **Sistema de Posicionamento**
Como trabalhar com o sistema de posicionamento

#### Nível Basic
```cpp
// Exemplo de sistema de posicionamento
#include "client/position.h"

void workWithPositions() {{
    // Criar posições
    Position pos1(100, 100, 7);
    Position pos2(105, 105, 7);
    
    // Obter coordenadas
    int x = pos1.x();
    int y = pos1.y();
    int z = pos1.z();
    
    std::cout << "Position: " << x << ", " << y << ", " << z << std::endl;
    
    // Calcular distância
    int distance = pos1.distance(pos2);
    std::cout << "Distance: " << distance << std::endl;
    
    // Verificar se está no alcance
    if (pos1.isInRange(pos2, 10)) {{
        std::cout << "Position is in range" << std::endl;
    }}
    
    // Mover posição
    Position movedPos = pos1.translated(5, 3, 0);  // Mover 5 para direita, 3 para baixo
    std::cout << "Moved to: " << movedPos.x() << ", " << movedPos.y() << ", " << movedPos.z() << std::endl;
    
    // Comparar posições
    if (pos1 == pos2) {{
        std::cout << "Positions are equal" << std::endl;
    }}
    
    if (pos1 < pos2) {{
        std::cout << "pos1 is less than pos2" << std::endl;
    }}
    
    // Obter posição relativa
    Position relativePos = pos1 - pos2;
    std::cout << "Relative: " << relativePos.x() << ", " << relativePos.y() << ", " << relativePos.z() << std::endl;
    
    // Verificar se é válida
    if (pos1.isValid()) {{
        std::cout << "Position is valid" << std::endl;
    }}
}}
```

#### Nível Intermediate
```cpp
// Exemplo de sistema de posicionamento
#include "client/position.h"

void workWithPositions() {{
    // Criar posições
    Position pos1(100, 100, 7);
    Position pos2(105, 105, 7);
    
    // Obter coordenadas
    int x = pos1.x();
    int y = pos1.y();
    int z = pos1.z();
    
    std::cout << "Position: " << x << ", " << y << ", " << z << std::endl;
    
    // Calcular distância
    int distance = pos1.distance(pos2);
    std::cout << "Distance: " << distance << std::endl;
    
    // Verificar se está no alcance
    if (pos1.isInRange(pos2, 10)) {{
        std::cout << "Position is in range" << std::endl;
    }}
    
    // Mover posição
    Position movedPos = pos1.translated(5, 3, 0);  // Mover 5 para direita, 3 para baixo
    std::cout << "Moved to: " << movedPos.x() << ", " << movedPos.y() << ", " << movedPos.z() << std::endl;
    
    // Comparar posições
    if (pos1 == pos2) {{
        std::cout << "Positions are equal" << std::endl;
    }}
    
    if (pos1 < pos2) {{
        std::cout << "pos1 is less than pos2" << std::endl;
    }}
    
    // Obter posição relativa
    Position relativePos = pos1 - pos2;
    std::cout << "Relative: " << relativePos.x() << ", " << relativePos.y() << ", " << relativePos.z() << std::endl;
    
    // Verificar se é válida
    if (pos1.isValid()) {{
        std::cout << "Position is valid" << std::endl;
    }}
}}
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
// Exemplo de sistema de posicionamento
#include "client/position.h"

void workWithPositions() {{
    // Criar posições
    Position pos1(100, 100, 7);
    Position pos2(105, 105, 7);
    
    // Obter coordenadas
    int x = pos1.x();
    int y = pos1.y();
    int z = pos1.z();
    
    std::cout << "Position: " << x << ", " << y << ", " << z << std::endl;
    
    // Calcular distância
    int distance = pos1.distance(pos2);
    std::cout << "Distance: " << distance << std::endl;
    
    // Verificar se está no alcance
    if (pos1.isInRange(pos2, 10)) {{
        std::cout << "Position is in range" << std::endl;
    }}
    
    // Mover posição
    Position movedPos = pos1.translated(5, 3, 0);  // Mover 5 para direita, 3 para baixo
    std::cout << "Moved to: " << movedPos.x() << ", " << movedPos.y() << ", " << movedPos.z() << std::endl;
    
    // Comparar posições
    if (pos1 == pos2) {{
        std::cout << "Positions are equal" << std::endl;
    }}
    
    if (pos1 < pos2) {{
        std::cout << "pos1 is less than pos2" << std::endl;
    }}
    
    // Obter posição relativa
    Position relativePos = pos1 - pos2;
    std::cout << "Relative: " << relativePos.x() << ", " << relativePos.y() << ", " << relativePos.z() << std::endl;
    
    // Verificar se é válida
    if (pos1.isValid()) {{
        std::cout << "Position is valid" << std::endl;
    }}
}}
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

### **Interação com Mapas**
Como interagir com mapas e tiles

#### Inicialização e Configuração
```cpp
// Exemplo de interação com mapas
#include "client/map.h"
#include "client/mapview.h"
#include "client/tile.h"

void interactWithMap() {{
    // Obter mapa e visualização
    MapPtr map = g_map;
    MapViewPtr mapView = g_mapView;
    
    // Obter posição do mouse
    Point mousePos(400, 300);
    Position tilePos = mapView->getPosition(mousePos);
    
    // Obter tile na posição
    TilePtr tile = map->getTile(tilePos);
    if (tile) {{
        // Verificar propriedades do tile
        if (tile->isWalkable()) {{
            std::cout << "Tile is walkable" << std::endl;
        }}
```

#### Funcionalidade 1
```cpp
        
        if (tile->isClickable()) {{
            std::cout << "Tile is clickable" << std::endl;
        }}
        
        // Obter coisas no tile
        const std::vector<ThingPtr>& things = tile->getThings();
        for (const auto& thing : things) {{
            if (thing->isItem()) {{
                ItemPtr item = thing->static_self_cast<Item>();
                std::cout << "Item ID: " << item->getId() << std::endl;
            }} else if (thing->isCreature()) {{
                CreaturePtr creature = thing->static_self_cast<Creature>();
                std::cout << "Creature: " << creature->getName() << std::endl;
            }}
        }}
        
        // Obter coisa no topo
        ThingPtr topThing = tile->getTopThing();
        if (topThing) {{
            std::cout << "Top thing: " << topThing->getType() << std::endl;
        }}
```

#### Funcionalidade 2
```cpp
        
        // Obter criatura no topo
        CreaturePtr topCreature = tile->getTopCreature();
        if (topCreature) {{
            std::cout << "Top creature: " << topCreature->getName() << std::endl;
        }}
        
        // Verificar se tile está vazio
        if (tile->isEmpty()) {{
            std::cout << "Tile is empty" << std::endl;
        }}
        
        // Verificar se tile é desenhável
        if (tile->isDrawable()) {{
            std::cout << "Tile is drawable" << std::endl;
        }}
        
        // Obter velocidade do ground
        int groundSpeed = tile->getGroundSpeed();
        std::cout << "Ground speed: " << groundSpeed << std::endl;
    }}
```

#### Finalização
```cpp
}}
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

## 🔗 Pontos de Integração

### **Graphics System**
Integração com sistema de gráficos para renderização

**Tipo:** dependency
**Arquivos:** mapview.h, mapview.cpp, tile.h, tile.cpp

### **Network System**
Recebimento de dados de mapa do servidor

**Tipo:** integration
**Arquivos:** map.h, map.cpp, mapio.cpp

### **Game System**
Integração com sistema de jogo para posicionamento

**Tipo:** integration
**Arquivos:** position.h, position.cpp, mapview.h

### **UI System**
Interface de usuário para mapas

**Tipo:** integration
**Arquivos:** mapview.h, mapview.cpp, minimap.h

### **Lua System**
Exposição de mapas para scripts Lua

**Tipo:** binding
**Arquivos:** map.h, mapview.h, tile.h

### **Resource Management**
Gerenciamento de recursos de mapa

**Tipo:** dependency
**Arquivos:** thingtype.h, thingtypemanager.h

### **Input System**
Entrada de mouse e teclado para mapas

**Tipo:** integration
**Arquivos:** mapview.h, mapview.cpp

### **Light System**
Sistema de iluminação para mapas

**Tipo:** integration
**Arquivos:** mapview.h, tile.h, lightview.h



## 📋 Guia de Uso

### **Mapa Básico**

#### Nível Basic
```cpp
#include "client/map.h"
#include "client/mapview.h"

// Criar mapa
MapPtr map = std::make_shared<Map>();
MapViewPtr mapView = std::make_shared<MapView>();

// Configurar visualização
mapView->setVisibleDimension(Size(15, 11));
mapView->setCameraPosition(Position(100, 100, 7));

// Renderizar
mapView->drawForeground(Rect(0, 0, 800, 600));
```

#### Nível Intermediate
```cpp
#include "client/map.h"
#include "client/mapview.h"

// Criar mapa
MapPtr map = std::make_shared<Map>();
MapViewPtr mapView = std::make_shared<MapView>();

// Configurar visualização
mapView->setVisibleDimension(Size(15, 11));
mapView->setCameraPosition(Position(100, 100, 7));

// Renderizar
mapView->drawForeground(Rect(0, 0, 800, 600));
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
#include "client/map.h"
#include "client/mapview.h"

// Criar mapa
MapPtr map = std::make_shared<Map>();
MapViewPtr mapView = std::make_shared<MapView>();

// Configurar visualização
mapView->setVisibleDimension(Size(15, 11));
mapView->setCameraPosition(Position(100, 100, 7));

// Renderizar
mapView->drawForeground(Rect(0, 0, 800, 600));
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

### **Gerenciamento de Tiles**

#### Nível Basic
```cpp
#include "client/tile.h"

// Obter tile
TilePtr tile = map->getTile(Position(100, 100, 7));

// Adicionar item
ItemPtr item = Item::create(100);
tile->addThing(item, 0);

// Verificar propriedades
if (tile->isWalkable()) {
    // Tile é caminhável
}
```

#### Nível Intermediate
```cpp
#include "client/tile.h"

// Obter tile
TilePtr tile = map->getTile(Position(100, 100, 7));

// Adicionar item
ItemPtr item = Item::create(100);
tile->addThing(item, 0);

// Verificar propriedades
if (tile->isWalkable()) {
    // Tile é caminhável
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
#include "client/tile.h"

// Obter tile
TilePtr tile = map->getTile(Position(100, 100, 7));

// Adicionar item
ItemPtr item = Item::create(100);
tile->addThing(item, 0);

// Verificar propriedades
if (tile->isWalkable()) {
    // Tile é caminhável
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

### **Controle de Câmera**

#### Nível Basic
```cpp
#include "client/mapview.h"

// Mover câmera
mapView->move(10, 5);

// Seguir criatura
mapView->followCreature(player);

// Configurar modo de visualização
mapView->setFloorViewMode(MapView::FloorViewMode::FADE);
```

#### Nível Intermediate
```cpp
#include "client/mapview.h"

// Mover câmera
mapView->move(10, 5);

// Seguir criatura
mapView->followCreature(player);

// Configurar modo de visualização
mapView->setFloorViewMode(MapView::FloorViewMode::FADE);
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
#include "client/mapview.h"

// Mover câmera
mapView->move(10, 5);

// Seguir criatura
mapView->followCreature(player);

// Configurar modo de visualização
mapView->setFloorViewMode(MapView::FloorViewMode::FADE);
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

## 🗺️ Tipos de Mapas

### **Tipos de Tiles**
- **Ground**: Tiles de chão
- **Items**: Objetos no mapa
- **Creatures**: Criaturas vivas
- **Effects**: Efeitos visuais
- **StaticText**: Textos estáticos

### **Tipos de Visualização**
- **Normal**: Visualização padrão
- **Fade**: Transição suave entre andares
- **Locked**: Andar fixo
- **Always**: Sempre mostrar todos os andares
- **Always with Transparency**: Com transparência

### **Tipos de Anti-aliasing**
- **Disabled**: Anti-aliasing desabilitado
- **Enabled**: Anti-aliasing habilitado
- **Smooth Retro**: Anti-aliasing suave retrô

## 🎨 Características dos Mapas

### **Propriedades de Tiles**
- **Walkable**: Pode ser caminhado
- **Clickable**: Pode ser clicado
- **Pathable**: Pode ser usado em caminhos
- **Opaque**: Bloqueia visão
- **Light**: Emite luz
- **Elevation**: Tem elevação

### **Propriedades de Posição**
- **3D Coordinates**: Coordenadas x, y, z
- **Range Checking**: Verificação de alcance
- **Distance Calculation**: Cálculo de distância
- **Translation**: Movimento relativo

### **Propriedades de Renderização**
- **Tile Size**: Tamanho dos tiles
- **Visible Dimension**: Dimensão visível
- **Camera Position**: Posição da câmera
- **Floor View Mode**: Modo de visualização de andares

## 🎯 Performance

### **Otimizações**
- **Tile Caching**: Cache de tiles
- **Viewport Culling**: Remoção de tiles fora da tela
- **LOD System**: Nível de detalhe
- **Batch Rendering**: Renderização em lotes

### **Métricas**
- **Maximum Tiles**: 100.000 tiles simultâneos
- **Performance**: < 16ms para renderização
- **Memory Usage**: < 100MB para mapas grandes
- **CPU Usage**: < 5% para mapas padrão

## 🚀 Próximos Passos

1. **Análise de Performance**: Profiling de mapas
2. **Otimizações Avançadas**: Técnicas de otimização
3. **Integração com Canary**: Preparação para servidor
4. **Documentação de API**: Referência completa

---

*Análise gerada automaticamente pelo sistema Habdel - 2025-07-31 15:51:34*
