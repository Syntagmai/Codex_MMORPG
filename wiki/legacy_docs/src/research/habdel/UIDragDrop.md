
# 🖱️ UI-012: Sistema de Drag & Drop

<div class="info"> **Story ID**: UI-012  
> **Categoria**: UI  
> **Status**: ✅ Completo  
> **Prioridade**: 🔥 **MÁXIMA**

## 📋 Índice
1. [Visão Geral](#visão-geral)
2. [Arquitetura do Sistema](#arquitetura-do-sistema)
3. [Sistema de Drag](#sistema-de-drag)
4. [Sistema de Drop](#sistema-de-drop)
5. [API Lua](#api-lua)
6. [Integração com Itens](#integração-com-itens)
7. [Exemplos Práticos](#exemplos-práticos)
8. [Melhores Práticas](#melhores-práticas)
9. [Performance e Otimização](#performance-e-otimização)

---

## 🎯 Visão Geral

O **Sistema de Drag & Drop** do OTClient oferece funcionalidades avançadas para arrastar e soltar widgets, itens e elementos da interface. O sistema é integrado com o inventário, containers e mapas do jogo.

### 🎨 **Características Principais**

- **Drag Intuitivo**: Arrastar widgets com feedback visual
- **Drop Zones**: Áreas específicas para receber itens
- **Validação**: Verificação de compatibilidade de drop
- **Feedback Visual**: Indicadores visuais durante drag
- **Integração Completa**: Sistema de inventário e containers
- **Drag Customizado**: Implementações específicas

---

## 🏗️ Arquitetura do Sistema

### 🎭 **Estrutura Hierárquica**

```
Sistema Drag & Drop
   │
   ├─ Drag Engine
   │   ├─ Início do drag (onDragEnter)
   │   ├─ Movimento do cursor (onDragMove)
   │   └─ Finalização do drag (onDragLeave)
   │
   ├─ Drop System
   │   ├─ Drop zones (onDrop)
   │   ├─ Validação (canAcceptDrop)
   │   └─ Processamento (processDrop)
   │
   ├─ Visual Feedback
   │   ├─ Cursor customizado (g_mouse.pushCursor)
   │   ├─ Preview do item
   │   └─ Indicadores de drop
   │
   └─ Integration
       ├─ Inventário (UIItem)
       ├─ Containers (UIContainer)
       └─ Mapas (UIGameMap)
```

### 🔄 **Fluxo de Drag & Drop**

```
1. Início do Drag
   ↓
2. Configuração do Cursor
   ↓
3. Criação do Preview
   ↓
4. Movimento do Cursor
   ↓
5. Detecção de Drop Zone
   ↓
6. Validação do Drop
   ↓
7. Processamento do Drop
   ↓
8. Limpeza e Finalização
```

---

## 🖱️ Sistema de Drag

### 🎯 **Configurando Widgets Arrastáveis**

```lua
-- Configurar widget para ser arrastável
function setupDraggableWidget(widget, dragData)
    -- Função: setupDraggableWidget
    widget:setDraggable(true)
    
    -- Configurar dados do drag
    --  Configurar dados do drag (traduzido)
    widget.dragData = dragData or {}
    
    -- Eventos de drag
    --  Eventos de drag (traduzido)
    widget.onDragEnter = function(widget, mousePos)
        print("Drag iniciado em:", mousePos.x, mousePos.y)
        
        -- Configurar cursor de drag
    --  Configurar cursor de drag (traduzido)
        g_mouse.pushCursor("target")
        
        -- Criar preview do item sendo arrastado
    --  Criar preview do item sendo arrastado (traduzido)
        createDragPreview(widget, dragData)
        
        return true  -- Permitir drag
    end
    
    widget.onDragMove = function(widget, mousePos)
        -- Atualizar posição do preview
        updateDragPreview(mousePos)
    end
    
    widget.onDragLeave = function(widget, mousePos)
        print("Drag finalizado em:", mousePos.x, mousePos.y)
        
        -- Restaurar cursor
    --  Restaurar cursor (traduzido)
        g_mouse.popCursor("target")
        
        -- Remover preview
    --  Remover preview (traduzido)
        removeDragPreview()
        
        -- Processar drop
    --  Processar drop (traduzido)
        processDrop(mousePos, dragData)
    end
end

-- Exemplo de uso
    --  Exemplo de uso (traduzido)
local draggableItem = g_ui.createWidget('UIWidget', parent)
setupDraggableWidget(draggableItem, {
    type = 'item',
    id = 1234,
    count = 1,
    source = 'inventory'
})
```

### 🎨 **Preview do Drag**

```lua
-- Criar preview visual do item sendo arrastado
    --  Criar preview visual do item sendo arrastado (traduzido)
function createDragPreview(widget, dragData)
    -- Função: createDragPreview
    local preview = g_ui.createWidget('UIWidget', rootWidget)
    preview:setSize({width = 32, height = 32})
    preview:setImageSource(widget:getImageSource())
    preview:setOpacity(0.8)
    preview:setId('dragPreview')
    
    -- Configurar dados do preview
    --  Configurar dados do preview (traduzido)
    preview.dragData = dragData
    
    -- Posicionar no cursor
    --  Posicionar no cursor (traduzido)
    local mousePos = g_mouse.getPosition()
    preview:setPosition({x = mousePos.x - 16, y = mousePos.y - 16})
    
    return preview
end

-- Atualizar posição do preview
function updateDragPreview(mousePos)
    -- Função: updateDragPreview
    local preview = g_ui.getRootWidget():getChildById('dragPreview')
    if preview then
    -- Verificação condicional
        preview:setPosition({x = mousePos.x - 16, y = mousePos.y - 16})
    end
end

-- Remover preview
    --  Remover preview (traduzido)
function removeDragPreview()
    -- Função: removeDragPreview
    local preview = g_ui.getRootWidget():getChildById('dragPreview')
    if preview then
    -- Verificação condicional
        preview:destroy()
    end
end
```

---

## 📥 Sistema de Drop

### 🎯 **Configurando Drop Zones**

#### Inicialização e Configuração
```lua
-- Criar zona de drop
function createDropZone(parent, zoneData)
    local dropZone = g_ui.createWidget('UIWidget', parent)
    dropZone:setSize({width = 100, height = 100})
    dropZone:setBackgroundColor('#444444')
    dropZone:setOpacity(0.3)
    
    -- Configurar dados da zona
    dropZone.zoneData = zoneData or {}
    
    -- Eventos de drop
    dropZone.onDragEnter = function(widget, mousePos)
        print("Item entrou na zona de drop")
        
        -- Highlight da zona
        widget:setBackgroundColor('#666666')
        widget:setOpacity(0.6)
        
        -- Validar se pode receber o item
        if canAcceptDrop(widget, dragData) then
            widget:setBackgroundColor('#00FF00')
        else
            widget:setBackgroundColor('#FF0000')
        end
```

#### Funcionalidade 1
```lua
    end
    
    dropZone.onDragLeave = function(widget, mousePos)
        print("Item saiu da zona de drop")
        
        -- Restaurar aparência
        widget:setBackgroundColor('#444444')
        widget:setOpacity(0.3)
    end
    
    dropZone.onDrop = function(widget, mousePos)
        print("Item dropado na zona")
        
        -- Processar o drop
        if canAcceptDrop(widget, dragData) then
            processDrop(widget, dragData)
            return true  -- Drop aceito
        else
            return false  -- Drop rejeitado
        end
    end
```

#### Finalização
```lua
    
    return dropZone
end

-- Validar se zona pode aceitar o drop
function canAcceptDrop(dropZone, dragData)
    -- Verificar tipo de item
    if dragData.type == 'item' then
        return dropZone.zoneData.acceptsItems
    elseif dragData.type == 'widget' then
        return dropZone.zoneData.acceptsWidgets
    end
    
    return false
end
```

---

## 🐍 API Lua

### 📦 **Métodos de Drag & Drop**

```lua
-- Configurar widget arrastável
widget:setDraggable(true)

-- Eventos de drag
    --  Eventos de drag (traduzido)
widget.onDragEnter = function(widget, mousePos) end
widget.onDragLeave = function(widget, mousePos) end
widget.onDragMove = function(widget, mousePos) end

-- Eventos de drop
    --  Eventos de drop (traduzido)
widget.onDrop = function(widget, mousePos) end

-- Controle de cursor
    --  Controle de cursor (traduzido)
g_mouse.pushCursor("target")
g_mouse.popCursor("target")

-- Binding automático
g_mouse.bindOnDrop(widget, callback)
```

### 🎯 **Métodos Específicos**

#### UIItem (Itens do Jogo)
```lua
-- Configurar drag & drop para itens
    --  Configurar drag & drop para itens (traduzido)
function setupItemDragDrop(itemWidget)
    -- Função: setupItemDragDrop
    itemWidget:setDraggable(true)
    
    itemWidget.onDragEnter = function(widget, mousePos)
        if widget:isVirtual() then return false end
    -- Verificação condicional
        
        local item = widget:getItem()
        if not item then return false end
    -- Verificação condicional
        
        widget:setBorderWidth(1)
        widget:setBorderColor('#00FF00')
        widget.currentDragThing = item
        g_mouse.pushCursor('target')
        return true
    end
    
    itemWidget.onDragLeave = function(widget, mousePos)
        if widget:isVirtual() then return false end
    -- Verificação condicional
        
        widget.currentDragThing = nil
        g_mouse.popCursor('target')
        widget:setBorderWidth(0)
        return true
    end
    
    itemWidget.onDrop = function(widget, mousePos)
        local draggedItem = widget.currentDragThing
        if not draggedItem or not draggedItem:isItem() then return false end
    -- Verificação condicional
        
        local toPos = widget:getPosition()
        local fromPos = draggedItem:getPosition()
        
        if fromPos.x == toPos.x and fromPos.y == toPos.y and fromPos.z == toPos.z then
    -- Verificação condicional
            return false
        end
        
        -- Mover item
    --  Mover item (traduzido)
        if draggedItem:getCount() > 1 then
    -- Verificação condicional
            modules.game_interface.moveStackableItem(draggedItem, toPos)
        else
            g_game.move(draggedItem, toPos, 1)
        end
        
        widget:setBorderWidth(0)
        return true
    end
end
```

#### UIGameMap (Mapa do Jogo)
```lua
-- Configurar drag & drop para mapa
    --  Configurar drag & drop para mapa (traduzido)
function setupMapDragDrop(mapWidget)
    -- Função: setupMapDragDrop
    mapWidget.onDragEnter = function(widget, mousePos)
        local tile = widget:getTile(mousePos)
        if not tile then return false end
    -- Verificação condicional
        
        local thing = tile:getTopMoveThing()
        if not thing then return false end
    -- Verificação condicional
        
        widget.currentDragThing = thing
        g_mouse.pushCursor('target')
        return true
    end
    
    mapWidget.onDragLeave = function(widget, mousePos)
        widget.currentDragThing = nil
        g_mouse.popCursor('target')
        return true
    end
    
    mapWidget.onDrop = function(widget, mousePos)
        if not widget:canAcceptDrop(widget, mousePos) then
    -- Verificação condicional
            return false
        end
        
        local tile = widget:getTile(mousePos)
        if not tile then return false end
    -- Verificação condicional
        
        local thing = widget.currentDragThing
        local thingPos = thing:getPosition()
        if not thingPos then return false end
    -- Verificação condicional
        
        local toPos = tile:getPosition()
        if thingPos.x == toPos.x and thingPos.y == toPos.y and thingPos.z == toPos.z then
    -- Verificação condicional
            return false
        end
        
        if thing:isItem() and thing:getCount() > 1 then
    -- Verificação condicional
            modules.game_interface.moveStackableItem(thing, toPos)
        else
            g_game.move(thing, toPos, 1)
        end
        
        return true
    end
end
```

---

## 🎮 Integração com Itens

### 🎯 **Sistema de Inventário**

```lua
-- Setup para slots de inventário
function setupInventorySlot(slotWidget, slotIndex)
    -- Função: setupInventorySlot
    slotWidget:setDraggable(true)
    
    slotWidget.onDragEnter = function(widget, mousePos)
        local item = widget:getItem()
        if not item then return false end
    -- Verificação condicional
        
        widget:setBorderWidth(2)
        widget:setBorderColor('#00FF00')
        widget.currentDragThing = item
        g_mouse.pushCursor('target')
        return true
    end
    
    slotWidget.onDragLeave = function(widget, mousePos)
        widget.currentDragThing = nil
        g_mouse.popCursor('target')
        widget:setBorderWidth(0)
        return true
    end
    
    slotWidget.onDrop = function(widget, mousePos)
        local draggedItem = widget.currentDragThing
        if not draggedItem then return false end
    -- Verificação condicional
        
        -- Processar movimento no inventário
        g_game.moveInventoryItem(slotIndex, draggedItem:getId(), draggedItem:getCount())
        
        widget:setBorderWidth(0)
        return true
    end
end
```

### 🎯 **Sistema de Containers**

```lua
-- Setup para container slots
    --  Setup para container slots (traduzido)
function setupContainerSlot(slotWidget, containerId, slotIndex)
    -- Função: setupContainerSlot
    slotWidget:setDraggable(true)
    
    slotWidget.onDragEnter = function(widget, mousePos)
        local item = widget:getItem()
        if not item then return false end
    -- Verificação condicional
        
        widget:setBorderWidth(2)
        widget:setBorderColor('#00FF00')
        widget.currentDragThing = item
        g_mouse.pushCursor('target')
        return true
    end
    
    slotWidget.onDragLeave = function(widget, mousePos)
        widget.currentDragThing = nil
        g_mouse.popCursor('target')
        widget:setBorderWidth(0)
        return true
    end
    
    slotWidget.onDrop = function(widget, mousePos)
        local draggedItem = widget.currentDragThing
        if not draggedItem then return false end
    -- Verificação condicional
        
        -- Processar movimento no container
    --  Processar movimento no container (traduzido)
        g_game.moveContainerItem(containerId, slotIndex, draggedItem:getId(), draggedItem:getCount())
        
        widget:setBorderWidth(0)
        return true
    end
end
```

---

## 💡 Exemplos Práticos

### 🎯 **Exemplo 1: Sistema de Drag & Drop Customizado**

#### Inicialização e Configuração
```lua
local CustomDragDrop = {}

function CustomDragDrop.createDraggableItem(parent, itemData)
    local item = g_ui.createWidget('UIWidget', parent)
    item:setSize({width = 32, height = 32})
    item:setImageSource('/images/items/' .. itemData.id)
    item:setDraggable(true)
    
    -- Configurar dados do item
    item.itemData = itemData
    
    -- Eventos de drag
    item.onDragEnter = function(widget, mousePos)
        print('Iniciando drag do item:', itemData.name)
        
        -- Criar preview
        local preview = g_ui.createWidget('UIWidget', rootWidget)
        preview:setSize({width = 32, height = 32})
        preview:setImageSource(widget:getImageSource())
        preview:setOpacity(0.8)
        preview:setId('customDragPreview')
        
        -- Configurar cursor
        g_mouse.pushCursor('target')
        
        return true
    end
```

#### Funcionalidade 1
```lua
    
    item.onDragMove = function(widget, mousePos)
        local preview = g_ui.getRootWidget():getChildById('customDragPreview')
        if preview then
            preview:setPosition({x = mousePos.x - 16, y = mousePos.y - 16})
        end
    end
    
    item.onDragLeave = function(widget, mousePos)
        print('Finalizando drag do item:', itemData.name)
        
        -- Remover preview
        local preview = g_ui.getRootWidget():getChildById('customDragPreview')
        if preview then
            preview:destroy()
        end
        
        -- Restaurar cursor
        g_mouse.popCursor('target')
    end
    
    return item
end
```

#### Funcionalidade 2
```lua

function CustomDragDrop.createDropZone(parent, zoneData)
    local dropZone = g_ui.createWidget('UIWidget', parent)
    dropZone:setSize({width = 100, height = 100})
    dropZone:setBackgroundColor('#444444')
    dropZone:setOpacity(0.3)
    
    dropZone.zoneData = zoneData
    
    dropZone.onDragEnter = function(widget, mousePos)
        print('Item entrou na zona:', zoneData.name)
        widget:setBackgroundColor('#00FF00')
        widget:setOpacity(0.6)
    end
    
    dropZone.onDragLeave = function(widget, mousePos)
        print('Item saiu da zona:', zoneData.name)
        widget:setBackgroundColor('#444444')
        widget:setOpacity(0.3)
    end
    
    dropZone.onDrop = function(widget, mousePos)
        print('Item dropado na zona:', zoneData.name)
        
        -- Processar o drop
        if zoneData.onDropCallback then
            zoneData.onDropCallback(widget, mousePos)
        end
```

#### Finalização
```lua
        
        widget:setBackgroundColor('#444444')
        widget:setOpacity(0.3)
        return true
    end
    
    return dropZone
end

-- Uso
local item = CustomDragDrop.createDraggableItem(parent, {
    id = 1234,
    name = 'Espada de Fogo'
})

local dropZone = CustomDragDrop.createDropZone(parent, {
    name = 'Zona de Equipamento',
    onDropCallback = function(widget, mousePos)
        print('Item equipado!')
    end
})
```

### 🎨 **Exemplo 2: Sistema de Reorganização de Interface**

```lua
local InterfaceDragDrop = {}

function InterfaceDragDrop.createMovableWindow(parent, windowData)
    -- Função: InterfaceDragDrop
    local window = g_ui.createWidget('MainWindow', parent)
    window:setSize({width = 200, height = 150})
    window:setText(windowData.title)
    window:setDraggable(true)
    
    -- Configurar dados da janela
    --  Configurar dados da janela (traduzido)
    window.windowData = windowData
    
    window.onDragEnter = function(widget, mousePos)
        print('Movendo janela:', windowData.title)
        widget:setOpacity(0.8)
    end
    
    window.onDragLeave = function(widget, mousePos)
        print('Janela movida para:', mousePos.x, mousePos.y)
        widget:setOpacity(1.0)
        
        -- Salvar nova posição
        windowData.position = {x = mousePos.x, y = mousePos.y}
    end
    
    return window
end

function InterfaceDragDrop.createTabBar(parent)
    -- Função: InterfaceDragDrop
    local tabBar = g_ui.createWidget('TabBar', parent)
    tabBar:setDraggable(true)
    
    -- Adicionar tabs
    --  Adicionar tabs (traduzido)
    for i, tabName in ipairs({'Tab 1', 'Tab 2', 'Tab 3'}) do
    -- Loop de repetição
        local tab = tabBar:addTab(tabName)
        tab:setDraggable(true)
        
        tab.onDragEnter = function(widget, mousePos)
            print('Reorganizando tab:', tabName)
        end
        
        tab.onDrop = function(widget, mousePos)
            print('Tab reorganizada:', tabName)
            -- Aqui você implementaria a lógica de reorganização
        end
    end
    
    return tabBar
end
```

---

## ✅ Melhores Práticas

### 🎯 **Configuração Adequada**

```lua
-- ✅ BOM: Validar dados antes do drag
    --  ✅ BOM: Validar dados antes do drag (traduzido)
function validateDragData(widget, dragData)
    -- Função: validateDragData
    if not dragData or not dragData.type then
    -- Verificação condicional
        return false
    end
    
    if dragData.type == 'item' and not dragData.id then
    -- Verificação condicional
        return false
    end
    
    return true
end

-- ✅ BOM: Limpar recursos após drag
function cleanupDrag(widget)
    -- Função: cleanupDrag
    widget.currentDragThing = nil
    widget:setBorderWidth(0)
    g_mouse.popCursor('target')
    
    local preview = g_ui.getRootWidget():getChildById('dragPreview')
    if preview then
    -- Verificação condicional
        preview:destroy()
    end
end

-- ✅ BOM: Usar callbacks para flexibilidade
    --  ✅ BOM: Usar callbacks para flexibilidade (traduzido)
function setupDragDropWithCallback(widget, callbacks)
    -- Função: setupDragDropWithCallback
    widget:setDraggable(true)
    
    if callbacks.onDragStart then
    -- Verificação condicional
        widget.onDragEnter = callbacks.onDragStart
    end
    
    if callbacks.onDragEnd then
    -- Verificação condicional
        widget.onDragLeave = callbacks.onDragEnd
    end
    
    if callbacks.onDrop then
    -- Verificação condicional
        widget.onDrop = callbacks.onDrop
    end
end
```

### 🎨 **Feedback Visual**

```lua
-- ✅ BOM: Feedback visual consistente
    --  ✅ BOM: Feedback visual consistente (traduzido)
function setDragFeedback(widget, isValid)
    -- Função: setDragFeedback
    if isValid then
    -- Verificação condicional
        widget:setBorderColor('#00FF00')
        widget:setBackgroundColor('#004400')
    else
        widget:setBorderColor('#FF0000')
        widget:setBackgroundColor('#440000')
    end
end

-- ✅ BOM: Indicadores de estado
    --  ✅ BOM: Indicadores de estado (traduzido)
function updateDropZoneState(dropZone, state)
    -- Função: updateDropZoneState
    local colors = {
        idle = '#444444',
        hover = '#666666',
        valid = '#00FF00',
        invalid = '#FF0000'
    }
    
    dropZone:setBackgroundColor(colors[state])
end
```

### 🔧 **Validação Robusta**

```lua
-- ✅ BOM: Validação completa de drop
function validateDrop(dropZone, dragData)
    -- Função: validateDrop
    -- Verificar tipo
    --  Verificar tipo (traduzido)
    if not dropZone.zoneData.acceptedTypes then
    -- Verificação condicional
        return false
    end
    
    local accepted = false
    for _, acceptedType in ipairs(dropZone.zoneData.acceptedTypes) do
    -- Loop de repetição
        if dragData.type == acceptedType then
    -- Verificação condicional
            accepted = true
            break
        end
    end
    
    if not accepted then
    -- Verificação condicional
        return false
    end
    
    -- Verificar regras específicas
    if dropZone.zoneData.validationCallback then
    -- Verificação condicional
        return dropZone.zoneData.validationCallback(dropZone, dragData)
    end
    
    return true
end
```

---

## 🚀 Performance e Otimização

### 📊 **Métricas de Performance**

1. **Tempo de Início do Drag**: < 1ms
2. **Tempo de Movimento**: < 0.5ms por frame
3. **Tempo de Validação**: < 0.1ms por drop zone
4. **Uso de Memória**: < 1KB por drag ativo

### 🎯 **Técnicas de Otimização**

```lua
-- Lazy loading de preview
    --  Lazy loading de preview (traduzido)
local previewCache = {}

function getDragPreview(itemId)
    -- Função: getDragPreview
    if not previewCache[itemId] then
    -- Verificação condicional
        previewCache[itemId] = createPreviewForItem(itemId)
    end
    return previewCache[itemId]
end

-- Debounce para validação
local validationTimers = {}

function debouncedValidation(dropZone, dragData, delay)
    -- Função: debouncedValidation
    delay = delay or 100
    
    local zoneId = dropZone:getId()
    
    if validationTimers[zoneId] then
    -- Verificação condicional
        removeEvent(validationTimers[zoneId])
    end
    
    validationTimers[zoneId] = scheduleEvent(function()
        validateDrop(dropZone, dragData)
        validationTimers[zoneId] = nil
    end, delay)
end
```

### 🔧 **Monitoramento de Performance**

```lua
-- Função para medir performance de drag & drop
local function measureDragDropPerformance()
    local startTime = g_clock.millis()
    
    -- Simular drag & drop
    --  Simular drag & drop (traduzido)
    local widget = g_ui.createWidget('UIWidget')
    widget:setDraggable(true)
    
    -- Simular eventos
    --  Simular eventos (traduzido)
    widget:onDragEnter({x = 100, y = 100})
    widget:onDragMove({x = 200, y = 200})
    widget:onDragLeave({x = 300, y = 300})
    
    local endTime = g_clock.millis()
    local totalTime = endTime - startTime
    
    print('Tempo de drag & drop:', totalTime, 'ms')
    
    widget:destroy()
end
```

---

## 📚 Referências

### 🔗 Links Relacionados
- [UIAdvancedWidgets](UIAdvancedWidgets.md) - Widgets Avançados
- [UIAnimations](UIAnimations.md) - Sistema de Animações
- [UIFormWidgets](UIFormWidgets.md) - Widgets de Formulário
- [ItemSystem](ItemSystem.md) - Sistema de Itens

### 📖 Documentação Técnica
- **Sistema de Mouse**: Controle de cursor e eventos
- **UIItem**: Implementação específica para itens
- **UIGameMap**: Implementação para mapas

---

**Última Atualização**: 2025-01-27  
**Versão**: 1.0  
**Status**: ✅ **Completo**  
**Prioridade**: 🔥 **MÁXIMA**
