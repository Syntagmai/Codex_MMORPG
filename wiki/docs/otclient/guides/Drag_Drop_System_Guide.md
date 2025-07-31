---
tags: [otclient, drag-drop, ui, interaction, system, guide, documentation]
status: completed
aliases: [Sistema de Drag Drop, Drag and Drop, UI Interaction, Drag System]
---

# Drag & Drop System Guide

> [!info] Este guia documenta o sistema completo de drag and drop do OTClient, incluindo arrastar widgets, drop zones, feedback visual e integração com o sistema de inventário e containers.

## 📋 Índice
- [[#Visão Geral]]
- [[#Sistema de Drag]]
- [[#Sistema de Drop]]
- [[#Drop Zones]]
- [[#Feedback Visual]]
- [[#Integração com Inventário]]
- [[#Integração com Containers]]
- [[#Drag Customizado]]
- [[#Performance e Otimização]]
- [[#Exemplos Práticos]]
- [[#Melhores Práticas]]

---

## 🎯 Visão Geral

O sistema de drag and drop do OTClient oferece:

- **Drag Intuitivo**: Arrastar widgets com feedback visual
- **Drop Zones**: Áreas específicas para receber itens
- **Validação**: Verificação de compatibilidade de drop
- **Feedback Visual**: Indicadores visuais durante drag
- **Integração Completa**: Sistema de inventário e containers
- **Drag Customizado**: Implementações específicas

### 🏗️ **Arquitetura do Sistema**

```
Sistema Drag & Drop
   │
   ├─ Drag Engine
   │   ├─ Início do drag
   │   ├─ Movimento do cursor
   │   └─ Finalização do drag
   │
   ├─ Drop System
   │   ├─ Drop zones
   │   ├─ Validação
   │   └─ Processamento
   │
   ├─ Visual Feedback
   │   ├─ Cursor customizado
   │   ├─ Preview do item
   │   └─ Indicadores de drop
   │
   └─ Integration
       ├─ Inventário
       ├─ Containers
       └─ Sistemas customizados
```

---

## 🖱️ Sistema de Drag

### 🎯 **Iniciando um Drag**

```lua
-- Configurar widget para ser arrastável
function setupDraggableWidget(widget, dragData)
    widget:setDraggable(true)
    
    -- Configurar dados do drag
    widget.dragData = dragData or {}
    
    -- Eventos de drag
    widget.onDragStart = function(widget, mousePos)
        print("Drag iniciado em:", mousePos.x, mousePos.y)
        
        -- Configurar cursor de drag
        g_mouse.setCursor("drag")
        
        -- Criar preview do item sendo arrastado
        createDragPreview(widget, dragData)
        
        return true  -- Permitir drag
    end
    
    widget.onDragMove = function(widget, mousePos)
        -- Atualizar posição do preview
        updateDragPreview(mousePos)
    end
    
    widget.onDragEnd = function(widget, mousePos)
        print("Drag finalizado em:", mousePos.x, mousePos.y)
        
        -- Restaurar cursor
        g_mouse.setCursor("default")
        
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
    dropZone.onDropEnter = function(widget, dragData)
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
    
    dropZone.onDropLeave = function(widget, dragData)
        print("Item saiu da zona de drop")
        
        -- Restaurar aparência
        widget:setBackgroundColor('#444444')
        widget:setOpacity(0.3)
    end
    
    dropZone.onDrop = function(widget, dragData, mousePos)
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
    local zoneData = dropZone.zoneData
    
    -- Verificar tipo de item
    if zoneData.acceptedTypes then
        for _, acceptedType in ipairs(zoneData.acceptedTypes) do
            if dragData.type == acceptedType then
                return true
            end
        end
        return false
    end
    
    -- Verificar ID específico
    if zoneData.acceptedIds then
        for _, acceptedId in ipairs(zoneData.acceptedIds) do
            if dragData.id == acceptedId then
                return true
            end
        end
        return false
    end
    
    return true  -- Aceitar por padrão
end
```

### 🔄 **Processamento de Drop**

```lua
-- Processar drop na zona
function processDrop(dropZone, dragData)
    local zoneData = dropZone.zoneData
    
    -- Executar callback personalizado
    if zoneData.onDropCallback then
        zoneData.onDropCallback(dropZone, dragData)
    end
    
    -- Ações específicas por tipo
    if dragData.type == 'item' then
        processItemDrop(dropZone, dragData)
    elseif dragData.type == 'spell' then
        processSpellDrop(dropZone, dragData)
    elseif dragData.type == 'hotkey' then
        processHotkeyDrop(dropZone, dragData)
    end
end

-- Processar drop de item
function processItemDrop(dropZone, dragData)
    local zoneData = dropZone.zoneData
    
    if zoneData.action == 'move' then
        -- Mover item
        moveItem(dragData.source, zoneData.target, dragData.id, dragData.count)
        
    elseif zoneData.action == 'use' then
        -- Usar item
        useItem(dragData.id, dragData.count)
        
    elseif zoneData.action == 'equip' then
        -- Equipar item
        equipItem(dragData.id)
        
    elseif zoneData.action == 'trade' then
        -- Adicionar ao trade
        addToTrade(dragData.id, dragData.count)
    end
end
```

---

## 🎯 Drop Zones

### 📦 **Zona de Inventário**

```lua
-- Criar zona de drop para inventário
function createInventoryDropZone(parent, slotId)
    local dropZone = createDropZone(parent, {
        type = 'inventory',
        slotId = slotId,
        acceptedTypes = {'item'},
        action = 'move',
        onDropCallback = function(zone, dragData)
            print("Item dropado no slot", slotId)
            
            -- Mover item para o slot
            if dragData.source == 'inventory' then
                -- Movimento interno do inventário
                g_game.moveItem(dragData.id, dragData.count, slotId)
            elseif dragData.source == 'container' then
                -- Do container para inventário
                g_game.moveItemFromContainer(dragData.containerId, dragData.id, dragData.count, slotId)
            end
        end
    })
    
    dropZone:setId('inventorySlot_' .. slotId)
    return dropZone
end

-- Setup completo do inventário
function setupInventoryDragDrop()
    local inventory = modules.game_inventory.getInventoryPanel()
    
    -- Criar zonas de drop para cada slot
    for i = 1, 20 do  -- 20 slots de inventário
        local slot = inventory:getChildById('slot' .. i)
        if slot then
            createInventoryDropZone(slot, i)
        end
    end
end
```

### 🎒 **Zona de Container**

```lua
-- Criar zona de drop para container
function createContainerDropZone(parent, containerId, slotId)
    local dropZone = createDropZone(parent, {
        type = 'container',
        containerId = containerId,
        slotId = slotId,
        acceptedTypes = {'item'},
        action = 'move',
        onDropCallback = function(zone, dragData)
            print("Item dropado no container", containerId, "slot", slotId)
            
            -- Mover item para o container
            if dragData.source == 'inventory' then
                -- Do inventário para container
                g_game.moveItemToContainer(dragData.id, dragData.count, containerId, slotId)
            elseif dragData.source == 'container' then
                -- Entre containers
                g_game.moveItemBetweenContainers(dragData.containerId, dragData.id, dragData.count, containerId, slotId)
            end
        end
    })
    
    dropZone:setId('container_' .. containerId .. '_slot_' .. slotId)
    return dropZone
end

-- Setup de container
function setupContainerDragDrop(containerId)
    local container = modules.game_containers.getContainer(containerId)
    if not container then return end
    
    local containerPanel = container:getContainerPanel()
    
    -- Criar zonas de drop para cada slot do container
    for i = 1, 20 do  -- 20 slots por container
        local slot = containerPanel:getChildById('slot' .. i)
        if slot then
            createContainerDropZone(slot, containerId, i)
        end
    end
end
```

### 🎮 **Zona de Hotkey**

```lua
-- Criar zona de drop para hotkey
function createHotkeyDropZone(parent, hotkeyId)
    local dropZone = createDropZone(parent, {
        type = 'hotkey',
        hotkeyId = hotkeyId,
        acceptedTypes = {'item', 'spell'},
        action = 'assign',
        onDropCallback = function(zone, dragData)
            print("Item/spell dropado no hotkey", hotkeyId)
            
            if dragData.type == 'item' then
                -- Atribuir item ao hotkey
                g_game.assignHotkey(hotkeyId, 'item', dragData.id)
            elseif dragData.type == 'spell' then
                -- Atribuir spell ao hotkey
                g_game.assignHotkey(hotkeyId, 'spell', dragData.id)
            end
        end
    })
    
    dropZone:setId('hotkey_' .. hotkeyId)
    return dropZone
end

-- Setup de hotkeys
function setupHotkeyDragDrop()
    local hotkeyPanel = modules.game_hotkeys.getHotkeyPanel()
    
    -- Criar zonas de drop para cada hotkey
    for i = 1, 12 do  -- 12 hotkeys
        local hotkey = hotkeyPanel:getChildById('hotkey' .. i)
        if hotkey then
            createHotkeyDropZone(hotkey, i)
        end
    end
end
```

---

## 🎨 Feedback Visual

### 🖱️ **Cursor Customizado**

```lua
-- Configurar cursor de drag
function setupDragCursor()
    -- Cursor para item
    g_mouse.setCursorImage("drag_item", "/images/cursors/drag_item")
    
    -- Cursor para spell
    g_mouse.setCursorImage("drag_spell", "/images/cursors/drag_spell")
    
    -- Cursor para hotkey
    g_mouse.setCursorImage("drag_hotkey", "/images/cursors/drag_hotkey")
end

-- Mudar cursor baseado no tipo de drag
function updateDragCursor(dragData)
    if dragData.type == 'item' then
        g_mouse.setCursor("drag_item")
    elseif dragData.type == 'spell' then
        g_mouse.setCursor("drag_spell")
    elseif dragData.type == 'hotkey' then
        g_mouse.setCursor("drag_hotkey")
    else
        g_mouse.setCursor("drag")
    end
end
```

### 🎯 **Indicadores de Drop**

```lua
-- Criar indicador de drop válido
function createValidDropIndicator()
    local indicator = g_ui.createWidget('UIWidget', rootWidget)
    indicator:setSize({width = 32, height = 32})
    indicator:setImageSource('/images/ui/drop_valid')
    indicator:setId('dropIndicator')
    indicator:hide()
    
    return indicator
end

-- Criar indicador de drop inválido
function createInvalidDropIndicator()
    local indicator = g_ui.createWidget('UIWidget', rootWidget)
    indicator:setSize({width = 32, height = 32})
    indicator:setImageSource('/images/ui/drop_invalid')
    indicator:setId('dropIndicatorInvalid')
    indicator:hide()
    
    return indicator
end

-- Mostrar indicador de drop
function showDropIndicator(mousePos, isValid)
    local indicator = g_ui.getRootWidget():getChildById('dropIndicator')
    local invalidIndicator = g_ui.getRootWidget():getChildById('dropIndicatorInvalid')
    
    if isValid then
        if indicator then
            indicator:setPosition({x = mousePos.x - 16, y = mousePos.y - 16})
            indicator:show()
        end
        if invalidIndicator then
            invalidIndicator:hide()
        end
    else
        if invalidIndicator then
            invalidIndicator:setPosition({x = mousePos.x - 16, y = mousePos.y - 16})
            invalidIndicator:show()
        end
        if indicator then
            indicator:hide()
        end
    end
end

-- Esconder indicadores
function hideDropIndicators()
    local indicator = g_ui.getRootWidget():getChildById('dropIndicator')
    local invalidIndicator = g_ui.getRootWidget():getChildById('dropIndicatorInvalid')
    
    if indicator then
        indicator:hide()
    end
    if invalidIndicator then
        invalidIndicator:hide()
    end
end
```

---

## 🎒 Integração com Inventário

### 📦 **Sistema de Inventário Drag & Drop**

```lua
-- Configurar item do inventário para drag
function setupInventoryItemDrag(itemWidget, itemData)
    itemWidget:setDraggable(true)
    itemWidget.dragData = {
        type = 'item',
        id = itemData.id,
        count = itemData.count,
        source = 'inventory',
        slotId = itemData.slotId
    }
    
    -- Eventos de drag
    itemWidget.onDragStart = function(widget, mousePos)
        updateDragCursor(widget.dragData)
        createDragPreview(widget, widget.dragData)
        return true
    end
    
    itemWidget.onDragMove = function(widget, mousePos)
        updateDragPreview(mousePos)
        
        -- Verificar se está sobre uma zona de drop válida
        local dropZone = getDropZoneAtPosition(mousePos)
        if dropZone then
            local isValid = canAcceptDrop(dropZone, widget.dragData)
            showDropIndicator(mousePos, isValid)
        else
            hideDropIndicators()
        end
    end
    
    itemWidget.onDragEnd = function(widget, mousePos)
        g_mouse.setCursor("default")
        removeDragPreview()
        hideDropIndicators()
        
        -- Processar drop
        local dropZone = getDropZoneAtPosition(mousePos)
        if dropZone and canAcceptDrop(dropZone, widget.dragData) then
            processDrop(dropZone, widget.dragData)
        end
    end
end

-- Setup completo do inventário
function setupInventoryDragDrop()
    local inventory = modules.game_inventory.getInventoryPanel()
    
    -- Configurar cada slot do inventário
    for i = 1, 20 do
        local slot = inventory:getChildById('slot' .. i)
        if slot then
            -- Criar zona de drop
            createInventoryDropZone(slot, i)
            
            -- Configurar item para drag (se existir)
            local item = slot:getChildById('item')
            if item then
                local itemData = {
                    id = item:getItemId(),
                    count = item:getItemCount(),
                    slotId = i
                }
                setupInventoryItemDrag(item, itemData)
            end
        end
    end
end
```

---

## 📦 Integração com Containers

### 🎒 **Sistema de Container Drag & Drop**

```lua
-- Configurar item do container para drag
function setupContainerItemDrag(itemWidget, containerData)
    itemWidget:setDraggable(true)
    itemWidget.dragData = {
        type = 'item',
        id = containerData.id,
        count = containerData.count,
        source = 'container',
        containerId = containerData.containerId,
        slotId = containerData.slotId
    }
    
    -- Eventos de drag (similar ao inventário)
    itemWidget.onDragStart = function(widget, mousePos)
        updateDragCursor(widget.dragData)
        createDragPreview(widget, widget.dragData)
        return true
    end
    
    itemWidget.onDragMove = function(widget, mousePos)
        updateDragPreview(mousePos)
        
        local dropZone = getDropZoneAtPosition(mousePos)
        if dropZone then
            local isValid = canAcceptDrop(dropZone, widget.dragData)
            showDropIndicator(mousePos, isValid)
        else
            hideDropIndicators()
        end
    end
    
    itemWidget.onDragEnd = function(widget, mousePos)
        g_mouse.setCursor("default")
        removeDragPreview()
        hideDropIndicators()
        
        local dropZone = getDropZoneAtPosition(mousePos)
        if dropZone and canAcceptDrop(dropZone, widget.dragData) then
            processDrop(dropZone, widget.dragData)
        end
    end
end

-- Setup de container específico
function setupContainerDragDrop(containerId)
    local container = modules.game_containers.getContainer(containerId)
    if not container then return end
    
    local containerPanel = container:getContainerPanel()
    
    -- Configurar cada slot do container
    for i = 1, 20 do
        local slot = containerPanel:getChildById('slot' .. i)
        if slot then
            -- Criar zona de drop
            createContainerDropZone(slot, containerId, i)
            
            -- Configurar item para drag (se existir)
            local item = slot:getChildById('item')
            if item then
                local itemData = {
                    id = item:getItemId(),
                    count = item:getItemCount(),
                    containerId = containerId,
                    slotId = i
                }
                setupContainerItemDrag(item, itemData)
            end
        end
    end
end
```

---

## 🎨 Drag Customizado

### 🎭 **Sistema de Drag Personalizado**

```lua
-- Drag customizado para spells
function setupSpellDrag(spellWidget, spellData)
    spellWidget:setDraggable(true)
    spellWidget.dragData = {
        type = 'spell',
        id = spellData.id,
        name = spellData.name,
        source = 'spellbook'
    }
    
    spellWidget.onDragStart = function(widget, mousePos)
        g_mouse.setCursor("drag_spell")
        
        -- Criar preview do spell
        local preview = g_ui.createWidget('UIWidget', rootWidget)
        preview:setSize({width = 48, height = 48})
        preview:setImageSource('/images/spells/' .. spellData.id)
        preview:setOpacity(0.8)
        preview:setId('spellDragPreview')
        
        local mousePos = g_mouse.getPosition()
        preview:setPosition({x = mousePos.x - 24, y = mousePos.y - 24})
        
        return true
    end
    
    spellWidget.onDragMove = function(widget, mousePos)
        local preview = g_ui.getRootWidget():getChildById('spellDragPreview')
        if preview then
            preview:setPosition({x = mousePos.x - 24, y = mousePos.y - 24})
        end
    end
    
    spellWidget.onDragEnd = function(widget, mousePos)
        g_mouse.setCursor("default")
        
        local preview = g_ui.getRootWidget():getChildById('spellDragPreview')
        if preview then
            preview:destroy()
        end
        
        -- Processar drop do spell
        local dropZone = getDropZoneAtPosition(mousePos)
        if dropZone and dropZone.zoneData.type == 'hotkey' then
            g_game.assignHotkey(dropZone.zoneData.hotkeyId, 'spell', spellData.id)
        end
    end
end

-- Drag customizado para hotkeys
function setupHotkeyDrag(hotkeyWidget, hotkeyData)
    hotkeyWidget:setDraggable(true)
    hotkeyWidget.dragData = {
        type = 'hotkey',
        id = hotkeyData.id,
        action = hotkeyData.action,
        source = 'hotkey'
    }
    
    hotkeyWidget.onDragStart = function(widget, mousePos)
        g_mouse.setCursor("drag_hotkey")
        
        -- Criar preview do hotkey
        local preview = g_ui.createWidget('UIWidget', rootWidget)
        preview:setSize({width = 32, height = 32})
        preview:setImageSource('/images/hotkeys/' .. hotkeyData.id)
        preview:setOpacity(0.8)
        preview:setId('hotkeyDragPreview')
        
        local mousePos = g_mouse.getPosition()
        preview:setPosition({x = mousePos.x - 16, y = mousePos.y - 16})
        
        return true
    end
    
    hotkeyWidget.onDragMove = function(widget, mousePos)
        local preview = g_ui.getRootWidget():getChildById('hotkeyDragPreview')
        if preview then
            preview:setPosition({x = mousePos.x - 16, y = mousePos.y - 16})
        end
    end
    
    hotkeyWidget.onDragEnd = function(widget, mousePos)
        g_mouse.setCursor("default")
        
        local preview = g_ui.getRootWidget():getChildById('hotkeyDragPreview')
        if preview then
            preview:destroy()
        end
        
        -- Processar drop do hotkey
        local dropZone = getDropZoneAtPosition(mousePos)
        if dropZone and dropZone.zoneData.type == 'hotkey' then
            -- Trocar hotkeys
            local sourceId = hotkeyData.id
            local targetId = dropZone.zoneData.hotkeyId
            g_game.swapHotkeys(sourceId, targetId)
        end
    end
end
```

---

## ⚡ Performance e Otimização

### 🚀 **Otimizações de Performance**

```lua
-- Pool de previews para reutilização
local PreviewPool = {}
PreviewPool.previews = {}

function PreviewPool.getPreview()
    if #PreviewPool.previews > 0 then
        return table.remove(PreviewPool.previews)
    else
        return g_ui.createWidget('UIWidget', rootWidget)
    end
end

function PreviewPool.releasePreview(preview)
    preview:hide()
    table.insert(PreviewPool.previews, preview)
end

-- Cache de drop zones
local DropZoneCache = {}
DropZoneCache.zones = {}

function cacheDropZone(zone)
    table.insert(DropZoneCache.zones, zone)
end

function getDropZoneAtPosition(pos)
    for _, zone in ipairs(DropZoneCache.zones) do
        if zone:containsPoint(pos) then
            return zone
        end
    end
    return nil
end

-- Limitar verificações de drop
local lastDropCheck = 0
local DROP_CHECK_INTERVAL = 50  -- ms

function shouldCheckDrop()
    local currentTime = g_clock.millis()
    if currentTime - lastDropCheck > DROP_CHECK_INTERVAL then
        lastDropCheck = currentTime
        return true
    end
    return false
end
```

### 🎯 **Configurações de Performance**

```lua
-- Desabilitar drag em configurações baixas
function shouldEnableDrag()
    local fps = g_app.getFps()
    local quality = g_settings.getString("graphics.quality")
    
    return fps > 30 and quality ~= "low"
end

-- Configurar drag condicional
function setupConditionalDrag(widget, dragData)
    if shouldEnableDrag() then
        setupDraggableWidget(widget, dragData)
    else
        -- Fallback para clique simples
        widget.onClick = function()
            handleItemClick(dragData)
        end
    end
end
```

---

### 🎮 **Sistema de Trade Drag & Drop**

```lua
-- Setup de trade com drag & drop
function setupTradeDragDrop()
    local tradeWindow = modules.game_trade.getTradeWindow()
    
    -- Setup do inventário do jogador
    local playerInventory = tradeWindow:getChildById('playerInventory')
    for i = 1, 20 do
        local slot = playerInventory:getChildById('slot' .. i)
        if slot then
            createDropZone(slot, {
                type = 'trade_player',
                slotId = i,
                acceptedTypes = {'item'},
                action = 'add_to_trade',
                onDropCallback = function(zone, dragData)
                    g_game.addToTrade(dragData.id, dragData.count, i)
                end
            })
        end
    end
    
    -- Setup do inventário do outro jogador (só visual)
    local otherInventory = tradeWindow:getChildById('otherInventory')
    for i = 1, 20 do
        local slot = otherInventory:getChildById('slot' .. i)
        if slot then
            -- Slot só para visualização, não aceita drops
            slot:setBackgroundColor('#222222')
        end
    end
end
```

### 🎒 **Sistema de Container Drag & Drop**

```lua
-- Setup de container com drag & drop
function setupContainerSystem()
    -- Quando container é aberto
    connect(g_game, {
        onContainerOpen = function(containerId, container)
            setupContainerDragDrop(containerId)
        end
    })
    
    -- Quando item é adicionado ao container
    connect(g_game, {
        onContainerAddItem = function(containerId, item, slotId)
            local container = modules.game_containers.getContainer(containerId)
            if container then
                local containerPanel = container:getContainerPanel()
                local slot = containerPanel:getChildById('slot' .. slotId)
                
                if slot and item then
                    local itemWidget = slot:getChildById('item')
                    if itemWidget then
                        local itemData = {
                            id = item:getId(),
                            count = item:getCount(),
                            containerId = containerId,
                            slotId = slotId
                        }
                        setupContainerItemDrag(itemWidget, itemData)
                    end
                end
            end
        end
    })
end
```

### 🎨 **Sistema de Hotkey Drag & Drop**

```lua
-- Setup de hotkeys com drag & drop
function setupHotkeySystem()
    local hotkeyPanel = modules.game_hotkeys.getHotkeyPanel()
    
    -- Configurar cada hotkey
    for i = 1, 12 do
        local hotkey = hotkeyPanel:getChildById('hotkey' .. i)
        if hotkey then
            -- Criar zona de drop
            createHotkeyDropZone(hotkey, i)
            
            -- Configurar para drag (se tem conteúdo)
            local content = hotkey:getChildById('content')
            if content then
                local hotkeyData = {
                    id = i,
                    action = content:getData('action'),
                    type = content:getData('type')
                }
                setupHotkeyDrag(hotkey, hotkeyData)
            end
        end
    end
    
    -- Atualizar quando hotkey é atribuído
    connect(g_game, {
        onHotkeyAssigned = function(hotkeyId, action, data)
            local hotkey = hotkeyPanel:getChildById('hotkey' .. hotkeyId)
            if hotkey then
                local content = hotkey:getChildById('content')
                if content then
                    local hotkeyData = {
                        id = hotkeyId,
                        action = action,
                        type = data.type
                    }
                    setupHotkeyDrag(hotkey, hotkeyData)
                end
            end
        end
    })
end
```

---

## ✅ Melhores Práticas

### 🎯 **Uso Eficiente do Sistema**

```lua
-- ✅ BOM: Usar pool de previews
local preview = PreviewPool.getPreview()
preview:setImageSource('/images/items/' .. itemId)
-- ... usar preview ...
PreviewPool.releasePreview(preview)

-- ✅ BOM: Cache de drop zones
cacheDropZone(dropZone)
local zone = getDropZoneAtPosition(mousePos)

-- ✅ BOM: Verificar performance
if shouldEnableDrag() then
    setupDraggableWidget(widget, dragData)
end

-- ❌ EVITE: Criar muitos previews
for i = 1, 100 do
    local preview = g_ui.createWidget('UIWidget', rootWidget)  -- Muito custoso
end

-- ❌ EVITE: Verificar drop constantemente
function onDragMove(widget, mousePos)
    -- Verificar a cada frame é custoso
    local dropZone = getDropZoneAtPosition(mousePos)  -- Sem cache
end
```

### 🔧 **Configuração Adequada**

```lua
-- ✅ BOM: Configurar dados completos
widget.dragData = {
    type = 'item',
    id = itemId,
    count = itemCount,
    source = 'inventory',
    slotId = slotId
}

-- ✅ BOM: Validar drop adequadamente
function canAcceptDrop(dropZone, dragData)
    if not dropZone or not dragData then
        return false
    end
    
    -- Verificar tipo
    if dropZone.zoneData.acceptedTypes then
        local accepted = false
        for _, type in ipairs(dropZone.zoneData.acceptedTypes) do
            if dragData.type == type then
                accepted = true
                break
            end
        end
        if not accepted then
            return false
        end
    end
    
    return true
end

-- ✅ BOM: Limpar recursos adequadamente
function cleanupDragSystem()
    removeDragPreview()
    hideDropIndicators()
    g_mouse.setCursor("default")
end
```

### 🎨 **Design Consistente**

```lua
-- ✅ BOM: Usar constantes para configurações
local DRAG_CONFIG = {
    PREVIEW_SIZE = 32,
    PREVIEW_OPACITY = 0.8,
    CURSOR_OFFSET = 16,
    CHECK_INTERVAL = 50
}

-- ✅ BOM: Usar cores consistentes
local DROP_ZONE_COLORS = {
    DEFAULT = '#444444',
    HOVER = '#666666',
    VALID = '#00FF00',
    INVALID = '#FF0000'
}

-- ✅ BOM: Funções padronizadas
function createStandardDropZone(parent, zoneData)
    local dropZone = createDropZone(parent, zoneData)
    dropZone:setBackgroundColor(DROP_ZONE_COLORS.DEFAULT)
    return dropZone
end

function createStandardDragPreview(widget, dragData)
    local preview = PreviewPool.getPreview()
    preview:setSize({width = DRAG_CONFIG.PREVIEW_SIZE, height = DRAG_CONFIG.PREVIEW_SIZE})
    preview:setOpacity(DRAG_CONFIG.PREVIEW_OPACITY)
    preview:setImageSource(widget:getImageSource())
    return preview
end
```

O sistema de drag and drop do OTClient oferece ferramentas poderosas para criar interfaces intuitivas e responsivas. Use estas práticas para garantir performance e consistência em suas aplicações. 
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

