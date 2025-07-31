# Sistema de Eventos UIWidget

O sistema de eventos do OTClient permite criar interfaces interativas e responsivas através de callbacks e manipuladores de eventos que respondem a ações do usuário e mudanças de estado.

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Tipos de Eventos](#tipos-de-eventos)
3. [Eventos de Mouse](#eventos-de-mouse)
4. [Eventos de Teclado](#eventos-de-teclado)
5. [Eventos de Estado](#eventos-de-estado)
6. [Eventos Customizados](#eventos-customizados)
7. [Propagação de Eventos](#propagação-de-eventos)
8. [Exemplos Práticos](#exemplos-práticos)
9. [Melhores Práticas](#melhores-práticas)

## 🎯 Visão Geral

O sistema de eventos do OTClient funciona através de:

- **Callbacks Lua**: Funções definidas no widget que são chamadas quando eventos ocorrem
- **Propagação de Eventos**: Eventos podem "borbulhar" na hierarquia de widgets
- **Prevenção de Propagação**: Eventos podem ser consumidos para impedir propagação
- **Eventos Personalizados**: Possibilidade de criar eventos específicos da aplicação

### 🔄 **Fluxo de Eventos**

```
Evento Ocorre → Widget Filho → Widget Pai → Widget Avô → ... → Root
                     ↓              ↓           ↓
               Pode Consumir   Pode Consumir  Pode Consumir
```

## 🎭 Tipos de Eventos

### 📱 **Eventos de Interação**
- Mouse: cliques, movimento, wheel
- Teclado: teclas pressionadas, liberadas
- Foco: ganhou/perdeu foco

### 🔄 **Eventos de Estado**
- Mudanças de propriedades
- Mudanças de texto
- Mudanças de visibilidade

### ⚡ **Eventos de Sistema**
- Redimensionamento
- Movimentação
- Atualização de layout

## 🖱️ Eventos de Mouse

### 🎯 **Eventos Básicos de Mouse**

```lua
local widget = g_ui.createWidget('UIWidget', parent)

-- Clique simples
widget.onClick = function(widget, mousePos)
    print('Widget clicado na posição:', mousePos.x, mousePos.y)
    return true  -- Consome o evento (impede propagação)
end

-- Duplo clique
widget.onDoubleClick = function(widget, mousePos)
    print('Duplo clique detectado')
    return true
end

-- Botão pressionado
widget.onMousePress = function(widget, mousePos, button)
    if button == MouseLeftButton then
        print('Botão esquerdo pressionado')
        widget:setBackgroundColor('#ff0000')
    elseif button == MouseRightButton then
        print('Botão direito pressionado')
        -- Mostrar menu contextual
    end
    return true
end

-- Botão liberado
widget.onMouseRelease = function(widget, mousePos, button)
    if button == MouseLeftButton then
        print('Botão esquerdo liberado')
        widget:setBackgroundColor('#00ff00')
    end
    return true
end
```

### 🏃 **Eventos de Movimento**

```lua
-- Mouse entrou no widget
widget.onHoverChange = function(widget, hovered)
    if hovered then
        widget:setOpacity(0.8)
        print('Mouse entrou no widget')
    else
        widget:setOpacity(1.0)
        print('Mouse saiu do widget')
    end
end

-- Movimento contínuo do mouse
widget.onMouseMove = function(widget, mousePos, mouseMoved)
    -- mousePos: posição atual
    -- mouseMoved: delta do movimento
    print('Mouse moveu para:', mousePos.x, mousePos.y)
    print('Delta:', mouseMoved.x, mouseMoved.y)
    return false  -- Não consome (permite propagação)
end

-- Roda do mouse
widget.onMouseWheel = function(widget, mousePos, mouseWheel)
    if mouseWheel == MouseWheelUp then
        print('Scroll para cima')
        -- Implementar zoom in ou scroll up
    elseif mouseWheel == MouseWheelDown then
        print('Scroll para baixo')
        -- Implementar zoom out ou scroll down
    end
    return true
end
```

### 🎯 **Eventos de Drag and Drop**

```lua
-- Widget pode ser arrastado
widget:setDraggable(true)

-- Início do arraste
widget.onDragEnter = function(widget, mousePos)
    print('Início do arraste')
    widget:setOpacity(0.5)
    return true
end

-- Durante o arraste
widget.onDragMove = function(widget, mousePos, mouseMoved)
    print('Arrastando:', mousePos.x, mousePos.y)
    return true
end

-- Fim do arraste
widget.onDragLeave = function(widget, droppedWidget, mousePos)
    print('Fim do arraste')
    widget:setOpacity(1.0)
    return true
end

-- Item solto sobre este widget
widget.onDrop = function(widget, draggedWidget, mousePos)
    print('Item solto:', draggedWidget:getId())
    -- Implementar lógica de drop
    return true
end
```

## ⌨️ Eventos de Teclado

### 🔤 **Eventos Básicos de Teclado**

```lua
local textEdit = g_ui.createWidget('TextEdit', parent)

-- Tecla pressionada
textEdit.onKeyDown = function(widget, keyCode, keyModifiers)
    print('Tecla pressionada:', keyCode)
    
    if keyCode == KeyEnter then
        print('Enter pressionado')
        return true  -- Consome o evento
    elseif keyCode == KeyEscape then
        print('Escape pressionado')
        widget:clearFocus()
        return true
    end
    
    return false  -- Permite processamento padrão
end

-- Tecla liberada
textEdit.onKeyUp = function(widget, keyCode, keyModifiers)
    print('Tecla liberada:', keyCode)
    return false
end

-- Tecla pressionada (com repetição automática)
textEdit.onKeyPress = function(widget, keyCode, keyModifiers)
    -- Este evento se repete automaticamente se a tecla ficar pressionada
    if keyCode == KeyArrowUp then
        -- Navegar para cima
        return true
    elseif keyCode == KeyArrowDown then
        -- Navegar para baixo
        return true
    end
    return false
end
```

### 🔣 **Entrada de Texto**

```lua
-- Texto digitado
textEdit.onTextInput = function(widget, text)
    print('Texto digitado:', text)
    -- Validar entrada, aplicar filtros, etc.
    return false  -- Permite processamento padrão
end

-- Texto alterado (após processamento)
textEdit.onTextChange = function(widget, newText, oldText)
    print('Texto mudou de "' .. oldText .. '" para "' .. newText .. '"')
    
    -- Validação em tempo real
    if string.len(newText) > 50 then
        widget:setText(oldText)  -- Reverte se muito longo
        return true
    end
    
    return false
end
```

### ⌨️ **Modificadores de Teclado**

```lua
widget.onKeyDown = function(widget, keyCode, keyModifiers)
    -- Verificar modificadores
    local ctrl = (keyModifiers & KeyboardCtrlModifier) ~= 0
    local shift = (keyModifiers & KeyboardShiftModifier) ~= 0
    local alt = (keyModifiers & KeyboardAltModifier) ~= 0
    
    if ctrl and keyCode == KeyS then
        print('Ctrl+S pressionado - Salvar')
        return true
    elseif ctrl and shift and keyCode == KeyS then
        print('Ctrl+Shift+S pressionado - Salvar Como')
        return true
    elseif alt and keyCode == KeyF4 then
        print('Alt+F4 pressionado - Fechar')
        return true
    end
    
    return false
end
```

## 🔄 Eventos de Estado

### 👁️ **Eventos de Visibilidade e Foco**

```lua
-- Mudança de foco
widget.onFocusChange = function(widget, focused, reason)
    if focused then
        print('Widget ganhou foco, razão:', reason)
        widget:setBorderColor('#0000ff')
    else
        print('Widget perdeu foco')
        widget:setBorderColor('#666666')
    end
end

-- Mudança de visibilidade
widget.onVisibilityChange = function(widget, visible)
    if visible then
        print('Widget ficou visível')
        -- Iniciar animações, carregar dados, etc.
    else
        print('Widget ficou invisível')
        -- Pausar animações, liberar recursos, etc.
    end
end

-- Widget foi destruído
widget.onDestroy = function(widget)
    print('Widget sendo destruído')
    -- Cleanup, salvar estado, etc.
end
```

### 📐 **Eventos de Geometria**

```lua
-- Posição mudou
widget.onGeometryChange = function(widget, oldRect, newRect)
    print('Widget movido/redimensionado')
    print('Rect antigo:', oldRect.x, oldRect.y, oldRect.width, oldRect.height)
    print('Rect novo:', newRect.x, newRect.y, newRect.width, newRect.height)
    
    -- Reagir a mudanças de tamanho
    if newRect.width ~= oldRect.width then
        print('Largura mudou')
        -- Ajustar layout interno
    end
end

-- Layout foi atualizado
widget.onLayoutUpdate = function(widget)
    print('Layout do widget foi atualizado')
    -- Reagir a mudanças de layout
end
```

## ⚡ Eventos Customizados

### 🎨 **Criando Eventos Próprios**

```lua
-- Definir evento customizado
local function fireCustomEvent(widget, eventData)
    if widget.onCustomEvent then
        widget.onCustomEvent(widget, eventData)
    end
end

-- Widget que dispara evento customizado
local dataWidget = g_ui.createWidget('UIWidget', parent)

dataWidget.updateData = function(self, newData)
    self.data = newData
    
    -- Disparar evento customizado
    fireCustomEvent(self, {
        type = 'dataUpdated',
        data = newData,
        timestamp = os.time()
    })
end

-- Widget que escuta evento customizado
dataWidget.onCustomEvent = function(widget, eventData)
    if eventData.type == 'dataUpdated' then
        print('Dados atualizados:', eventData.data)
        print('Timestamp:', eventData.timestamp)
    end
end
```

### 📢 **Sistema de Eventos Global**

```lua
-- Sistema simples de eventos globais
local EventSystem = {}
EventSystem.listeners = {}

function EventSystem.on(eventName, callback)
    if not EventSystem.listeners[eventName] then
        EventSystem.listeners[eventName] = {}
    end
    table.insert(EventSystem.listeners[eventName], callback)
end

function EventSystem.emit(eventName, data)
    if EventSystem.listeners[eventName] then
        for _, callback in ipairs(EventSystem.listeners[eventName]) do
            callback(data)
        end
    end
end

-- Uso do sistema global
EventSystem.on('playerLevelUp', function(data)
    print('Player subiu para level:', data.newLevel)
end)

-- De qualquer lugar no código
EventSystem.emit('playerLevelUp', {newLevel = 50})
```

## 🌊 Propagação de Eventos

### ⬆️ **Bubbling (Propagação para Cima)**

```lua
-- Widget filho
local child = g_ui.createWidget('UIWidget', parent)
child.onClick = function(widget, mousePos)
    print('Clique no filho')
    return false  -- NÃO consome - permite propagação
end

-- Widget pai
local parent = g_ui.createWidget('UIWidget', rootWidget)
parent.onClick = function(widget, mousePos)
    print('Clique propagou para o pai')
    return true  -- Consome aqui
end

-- Resultado: ao clicar no filho, ambos os prints aparecerão
```

### 🛑 **Impedindo Propagação**

```lua
local button = g_ui.createWidget('Button', parent)

button.onClick = function(widget, mousePos)
    print('Botão clicado')
    
    -- Processar lógica do botão
    widget:setText('Clicado!')
    
    return true  -- CONSOME o evento - impede propagação
end

-- O widget pai NÃO receberá este evento
parent.onClick = function(widget, mousePos)
    print('Este print nunca aparecerá')
    return true
end
```

### 🔄 **Eventos Condicionais**

```lua
local conditionalWidget = g_ui.createWidget('UIWidget', parent)

conditionalWidget.onClick = function(widget, mousePos)
    if widget:isEnabled() then
        print('Widget habilitado - processando clique')
        return true  -- Consome
    else
        print('Widget desabilitado - ignorando clique')
        return false  -- Permite propagação
    end
end
```

## 💡 Exemplos Práticos

### 🎮 **Sistema de Menu Contextual**

```lua
local ContextMenu = {}

function ContextMenu.show(widget, items, mousePos)
    local menu = g_ui.createWidget('UIWidget', rootWidget)
    menu:setId('contextMenu')
    menu:setPosition(mousePos)
    menu:setBackgroundColor('#333333')
    menu:setBorderWidth(1)
    menu:setBorderColor('#666666')
    
    local layout = UIVerticalLayout.create(menu)
    menu:setLayout(layout)
    
    for _, item in ipairs(items) do
        local menuItem = g_ui.createWidget('Label', menu)
        menuItem:setText(item.text)
        menuItem:setPadding(5)
        menuItem:setHeight(25)
        
        menuItem.onClick = function()
            if item.callback then
                item.callback()
            end
            menu:destroy()
            return true
        end
        
        menuItem.onHoverChange = function(widget, hovered)
            if hovered then
                widget:setBackgroundColor('#555555')
            else
                widget:setBackgroundColor('#333333')
            end
        end
    end
    
    -- Fechar ao clicar fora
    rootWidget.onMousePress = function(widget, mousePos, button)
        if not menu:containsPoint(mousePos) then
            menu:destroy()
            rootWidget.onMousePress = nil  -- Remove handler
        end
        return false
    end
end

-- Uso do menu contextual
local myWidget = g_ui.createWidget('UIWidget', parent)

myWidget.onMousePress = function(widget, mousePos, button)
    if button == MouseRightButton then
        ContextMenu.show(widget, {
            {text = 'Copiar', callback = function() print('Copiado') end},
            {text = 'Colar', callback = function() print('Colado') end},
            {text = 'Excluir', callback = function() print('Excluído') end}
        }, mousePos)
        return true
    end
    return false
end
```

### 🔍 **Sistema de Tooltip Dinâmico**

```lua
local Tooltip = {}
Tooltip.current = nil

function Tooltip.show(widget, text, delay)
    delay = delay or 500  -- 500ms de delay padrão
    
    if Tooltip.current then
        Tooltip.hide()
    end
    
    scheduleEvent(function()
        if widget:isHovered() then  -- Ainda hovering
            local tooltip = g_ui.createWidget('Label', rootWidget)
            tooltip:setId('tooltip')
            tooltip:setText(text)
            tooltip:setBackgroundColor('#000000bb')
            tooltip:setColor('#ffffff')
            tooltip:setPadding(5)
            tooltip:setFont('verdana-9px-antialised')
            
            -- Posicionar próximo ao mouse
            local mousePos = g_window.getMousePosition()
            tooltip:setPosition({x = mousePos.x + 10, y = mousePos.y + 10})
            
            Tooltip.current = tooltip
        end
    end, delay)
end

function Tooltip.hide()
    if Tooltip.current then
        Tooltip.current:destroy()
        Tooltip.current = nil
    end
end

-- Adicionar tooltip a qualquer widget
function addTooltip(widget, text, delay)
    widget.onHoverChange = function(widget, hovered)
        if hovered then
            Tooltip.show(widget, text, delay)
        else
            Tooltip.hide()
        end
    end
end

-- Uso
local button = g_ui.createWidget('Button', parent)
button:setText('Hover Me')
addTooltip(button, 'Este é um botão especial que faz coisas incríveis!', 300)
```

### 📝 **Sistema de Validação de Formulário**

```lua
local FormValidator = {}

function FormValidator.create()
    local validator = {
        fields = {},
        rules = {}
    }
    
    function validator:addField(widget, rules)
        self.fields[widget] = rules
        
        -- Validação em tempo real
        widget.onTextChange = function(w, newText, oldText)
            validator:validateField(w, newText)
            return false
        end
        
        -- Validação ao perder foco
        widget.onFocusChange = function(w, focused)
            if not focused then
                validator:validateField(w, w:getText())
            end
        end
    end
    
    function validator:validateField(widget, text)
        local rules = self.fields[widget]
        if not rules then return true end
        
        for _, rule in ipairs(rules) do
            if not rule.validate(text) then
                widget:setBorderColor('#ff0000')
                widget.validationError = rule.message
                return false
            end
        end
        
        widget:setBorderColor('#00ff00')
        widget.validationError = nil
        return true
    end
    
    function validator:validateAll()
        local isValid = true
        for widget, _ in pairs(self.fields) do
            if not self:validateField(widget, widget:getText()) then
                isValid = false
            end
        end
        return isValid
    end
    
    return validator
end

-- Uso do validador
local form = g_ui.createWidget('UIWidget', parent)
local validator = FormValidator.create()

local nameField = g_ui.createWidget('TextEdit', form)
validator:addField(nameField, {
    {
        validate = function(text) return string.len(text) >= 3 end,
        message = 'Nome deve ter pelo menos 3 caracteres'
    }
})

local emailField = g_ui.createWidget('TextEdit', form)
validator:addField(emailField, {
    {
        validate = function(text) return string.find(text, '@') ~= nil end,
        message = 'Email deve conter @'
    }
})

local submitButton = g_ui.createWidget('Button', form)
submitButton:setText('Enviar')
submitButton.onClick = function()
    if validator:validateAll() then
        print('Formulário válido!')
    else
        print('Formulário inválido!')
    end
    return true
end
```

## ✅ Melhores Práticas

### 🎯 **Gerenciamento de Eventos**

```lua
-- ✅ BOM: Use return true/false apropriadamente
widget.onClick = function(widget, mousePos)
    -- Processar evento
    doSomething()
    
    return true  -- Consome evento se processou completamente
    -- return false  -- Permite propagação se outros widgets precisam processar
end

-- ✅ BOM: Limpe event handlers ao destruir widgets
widget.onDestroy = function(widget)
    widget.onMouseMove = nil
    widget.onClick = nil
    -- Liberar outros recursos
end
```

### 🚀 **Performance**

```lua
-- ✅ BOM: Evite criar functions pesadas em eventos frequentes
widget.onMouseMove = function(widget, mousePos, mouseMoved)
    -- Use debouncing para operações pesadas
    if not widget.moveTimeout then
        widget.moveTimeout = scheduleEvent(function()
            expensiveOperation()
            widget.moveTimeout = nil
        end, 100)  -- Executa no máximo a cada 100ms
    end
    return false
end

-- ❌ EVITE: Operações pesadas em eventos frequentes
widget.onMouseMove = function(widget, mousePos, mouseMoved)
    -- Esta função será chamada MUITAS vezes por segundo
    expensiveOperation()  -- ❌ Pode causar lag
    return false
end
```

### 🔧 **Debugging de Eventos**

```lua
-- Sistema de debug para eventos
local function debugEvent(widget, eventName)
    local originalHandler = widget[eventName]
    
    widget[eventName] = function(...)
        print('DEBUG:', widget:getId(), eventName, ...)
        
        if originalHandler then
            return originalHandler(...)
        end
        return false
    end
end

-- Usar para debuggar
debugEvent(myWidget, 'onClick')
debugEvent(myWidget, 'onMouseMove')
```

### 🎭 **Padrões de Eventos**

```lua
-- ✅ BOM: Use padrão Observer para múltiplos listeners
local EventEmitter = {}
function EventEmitter:new()
    local obj = {listeners = {}}
    setmetatable(obj, self)
    self.__index = self
    return obj
end

function EventEmitter:on(event, callback)
    if not self.listeners[event] then
        self.listeners[event] = {}
    end
    table.insert(self.listeners[event], callback)
end

function EventEmitter:emit(event, ...)
    if self.listeners[event] then
        for _, callback in ipairs(self.listeners[event]) do
            callback(...)
        end
    end
end

-- Uso
local myWidget = g_ui.createWidget('UIWidget', parent)
local emitter = EventEmitter:new()

emitter:on('click', function() print('Handler 1') end)
emitter:on('click', function() print('Handler 2') end)

myWidget.onClick = function(...)
    emitter:emit('click', ...)
    return true
end
```

O sistema de eventos do OTClient é poderoso e flexível, permitindo criar interfaces altamente interativas e responsivas. Use os padrões e práticas adequadas para garantir performance e manutenibilidade do código.