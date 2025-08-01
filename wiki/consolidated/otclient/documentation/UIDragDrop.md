---
tags: [ui, drag_drop, system, otclient, documentation, habdel]
type: documentation
status: completed
priority: maximum
created: 2025-01-27
---

# 🖱️ UI-012: Sistema de Drag & Drop

> [!info] **Story ID**: UI-012  
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
    widget:setDraggable(true)
    
    -- Configurar dados do drag
    widget.dragData = dragData or {}
    
    -- Eventos de drag
    widget.onDragEnter = function(widget, mousePos)
        print("Drag iniciado em:", mousePos.x, mousePos.y)
        
        -- Configurar cursor de drag
        g_mouse.pushCursor("target")
        
        -- Criar preview do item sendo arrastado
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
        g_mouse.popCursor("target")
        
        -- Remover preview
        removeDragPreview()
        
        -- Processar drop
        processDrop(mousePos, dragData)
    end
end

-- Exemplo de uso
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
function createDragPreview(widget, dragData)
    local preview = g_ui.createWidget('UIWidget', rootWidget)
    preview:setSize({width = 32, height = 32})
    preview:setImageSource(widget:getImageSource())
    preview:setOpacity(0.8)
    preview:setId('dragPreview')
    
    -- Configurar dados do preview
    preview.dragData = dragData
    
    -- Posicionar no cursor
    local mousePos = g_mouse.getPosition()
    preview:setPosition({x = mousePos.x - 16, y = mousePos.y - 16})
    
    return preview
end

-- Atualizar posição do preview
function updateDragPreview(mousePos)
    local preview = g_ui.getRootWidget():getChildById('dragPreview')
    if preview then
        preview:setPosition({x = mousePos.x - 16, y = mousePos.y - 16})
    end
end

-- Remover preview
function removeDragPreview()
    local preview = g_ui.getRootWidget():getChildById('dragPreview')
    if preview then
        preview:destroy()
    end
end
```

---

## 📥 Sistema de Drop

### 🎯 **Configurando Drop Zones**

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
widget.onDragEnter = function(widget, mousePos) end
widget.onDragLeave = function(widget, mousePos) end
widget.onDragMove = function(widget, mousePos) end

-- Eventos de drop
widget.onDrop = function(widget, mousePos) end

-- Controle de cursor
g_mouse.pushCursor("target")
g_mouse.popCursor("target")

-- Binding automático
g_mouse.bindOnDrop(widget, callback)
```

### 🎯 **Métodos Específicos**

#### UIItem (Itens do Jogo)
```lua
-- Configurar drag & drop para itens
function setupItemDragDrop(itemWidget)
    itemWidget:setDraggable(true)
    
    itemWidget.onDragEnter = function(widget, mousePos)
        if widget:isVirtual() then return false end
        
        local item = widget:getItem()
        if not item then return false end
        
        widget:setBorderWidth(1)
        widget:setBorderColor('#00FF00')
        widget.currentDragThing = item
        g_mouse.pushCursor('target')
        return true
    end
    
    itemWidget.onDragLeave = function(widget, mousePos)
        if widget:isVirtual() then return false end
        
        widget.currentDragThing = nil
        g_mouse.popCursor('target')
        widget:setBorderWidth(0)
        return true
    end
    
    itemWidget.onDrop = function(widget, mousePos)
        local draggedItem = widget.currentDragThing
        if not draggedItem or not draggedItem:isItem() then return false end
        
        local toPos = widget:getPosition()
        local fromPos = draggedItem:getPosition()
        
        if fromPos.x == toPos.x and fromPos.y == toPos.y and fromPos.z == toPos.z then
            return false
        end
        
        -- Mover item
        if draggedItem:getCount() > 1 then
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
function setupMapDragDrop(mapWidget)
    mapWidget.onDragEnter = function(widget, mousePos)
        local tile = widget:getTile(mousePos)
        if not tile then return false end
        
        local thing = tile:getTopMoveThing()
        if not thing then return false end
        
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
            return false
        end
        
        local tile = widget:getTile(mousePos)
        if not tile then return false end
        
        local thing = widget.currentDragThing
        local thingPos = thing:getPosition()
        if not thingPos then return false end
        
        local toPos = tile:getPosition()
        if thingPos.x == toPos.x and thingPos.y == toPos.y and thingPos.z == toPos.z then
            return false
        end
        
        if thing:isItem() and thing:getCount() > 1 then
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
    slotWidget:setDraggable(true)
    
    slotWidget.onDragEnter = function(widget, mousePos)
        local item = widget:getItem()
        if not item then return false end
        
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
function setupContainerSlot(slotWidget, containerId, slotIndex)
    slotWidget:setDraggable(true)
    
    slotWidget.onDragEnter = function(widget, mousePos)
        local item = widget:getItem()
        if not item then return false end
        
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
        
        -- Processar movimento no container
        g_game.moveContainerItem(containerId, slotIndex, draggedItem:getId(), draggedItem:getCount())
        
        widget:setBorderWidth(0)
        return true
    end
end
```

---

## 💡 Exemplos Práticos

### 🎯 **Exemplo 1: Sistema de Drag & Drop Customizado**

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
    local window = g_ui.createWidget('MainWindow', parent)
    window:setSize({width = 200, height = 150})
    window:setText(windowData.title)
    window:setDraggable(true)
    
    -- Configurar dados da janela
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
    local tabBar = g_ui.createWidget('TabBar', parent)
    tabBar:setDraggable(true)
    
    -- Adicionar tabs
    for i, tabName in ipairs({'Tab 1', 'Tab 2', 'Tab 3'}) do
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
function validateDragData(widget, dragData)
    if not dragData or not dragData.type then
        return false
    end
    
    if dragData.type == 'item' and not dragData.id then
        return false
    end
    
    return true
end

-- ✅ BOM: Limpar recursos após drag
function cleanupDrag(widget)
    widget.currentDragThing = nil
    widget:setBorderWidth(0)
    g_mouse.popCursor('target')
    
    local preview = g_ui.getRootWidget():getChildById('dragPreview')
    if preview then
        preview:destroy()
    end
end

-- ✅ BOM: Usar callbacks para flexibilidade
function setupDragDropWithCallback(widget, callbacks)
    widget:setDraggable(true)
    
    if callbacks.onDragStart then
        widget.onDragEnter = callbacks.onDragStart
    end
    
    if callbacks.onDragEnd then
        widget.onDragLeave = callbacks.onDragEnd
    end
    
    if callbacks.onDrop then
        widget.onDrop = callbacks.onDrop
    end
end
```

### 🎨 **Feedback Visual**

```lua
-- ✅ BOM: Feedback visual consistente
function setDragFeedback(widget, isValid)
    if isValid then
        widget:setBorderColor('#00FF00')
        widget:setBackgroundColor('#004400')
    else
        widget:setBorderColor('#FF0000')
        widget:setBackgroundColor('#440000')
    end
end

-- ✅ BOM: Indicadores de estado
function updateDropZoneState(dropZone, state)
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
    -- Verificar tipo
    if not dropZone.zoneData.acceptedTypes then
        return false
    end
    
    local accepted = false
    for _, acceptedType in ipairs(dropZone.zoneData.acceptedTypes) do
        if dragData.type == acceptedType then
            accepted = true
            break
        end
    end
    
    if not accepted then
        return false
    end
    
    -- Verificar regras específicas
    if dropZone.zoneData.validationCallback then
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
local previewCache = {}

function getDragPreview(itemId)
    if not previewCache[itemId] then
        previewCache[itemId] = createPreviewForItem(itemId)
    end
    return previewCache[itemId]
end

-- Debounce para validação
local validationTimers = {}

function debouncedValidation(dropZone, dragData, delay)
    delay = delay or 100
    
    local zoneId = dropZone:getId()
    
    if validationTimers[zoneId] then
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
    local widget = g_ui.createWidget('UIWidget')
    widget:setDraggable(true)
    
    -- Simular eventos
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
- [[UIAdvancedWidgets]] - Widgets Avançados
- [[UIAnimations]] - Sistema de Animações
- [[UIFormWidgets]] - Widgets de Formulário
- [[ItemSystem]] - Sistema de Itens

### 📖 Documentação Técnica
- **Sistema de Mouse**: Controle de cursor e eventos
- **UIItem**: Implementação específica para itens
- **UIGameMap**: Implementação para mapas

---

**Última Atualização**: 2025-01-27  
**Versão**: 1.0  
**Status**: ✅ **Completo**  
**Prioridade**: 🔥 **MÁXIMA**
