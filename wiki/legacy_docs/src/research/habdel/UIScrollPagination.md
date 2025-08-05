
# 📜 UI-015: Sistema de Scroll e Paginação

<div class="info"> **Story ID**: UI-015  
> **Categoria**: UI  
> **Status**: ✅ Completo  
> **Prioridade**: 🔥 **MÁXIMA**

## 📋 Índice
1. [Visão Geral](#visão-geral)
2. [Arquitetura do Sistema](#arquitetura-do-sistema)
3. [Tipos de Scroll](#tipos-de-scroll)
4. [Sistema de Paginação](#sistema-de-paginação)
5. [API Lua](#api-lua)
6. [UIScrollBar](#uiscrollbar)
7. [UIScrollArea](#uiscrollarea)
8. [Exemplos Práticos](#exemplos-práticos)
9. [Melhores Práticas](#melhores-práticas)
10. [Performance e Otimização](#performance-e-otimização)

---

## 🎯 Visão Geral

O **Sistema de Scroll e Paginação** do OTClient oferece funcionalidades avançadas para navegação em conteúdo extenso, incluindo scrollbars verticais/horizontais, áreas de scroll e sistemas de paginação para organizar dados em páginas.

### 🎨 **Características Principais**

- **UIScrollBar**: Scrollbars verticais e horizontais
- **UIScrollArea**: Áreas de conteúdo com scroll
- **Sistema de Paginação**: Navegação por páginas
- **Scroll por Mouse**: Suporte a wheel do mouse
- **Scroll por Teclado**: Navegação por teclado
- **Estilos Flexíveis**: Diferentes aparências de scrollbar

---

## 🏗️ Arquitetura do Sistema

### 🎭 **Estrutura Hierárquica**

```
Sistema de Scroll e Paginação
   │
   ├─ UIScrollBar
   │   ├─ VerticalScrollBar
   │   ├─ HorizontalScrollBar
   │   ├─ Slider Button
   │   ├─ Increment/Decrement Buttons
   │   └─ Value Display
   │
   ├─ UIScrollArea
   │   ├─ Content Area
   │   ├─ Virtual Offset
   │   ├─ Scroll Bars
   │   └─ Layout Management
   │
   ├─ Sistema de Paginação
   │   ├─ Page Navigation
   │   ├─ Page Indicators
   │   ├─ Items per Page
   │   └─ Page Controls
   │
   └─ Event Handling
       ├─ Mouse Events
       ├─ Keyboard Events
       ├─ Value Changes
       └─ Scroll Events
```

### 🔄 **Fluxo de Scroll**

```
1. Detecção de Overflow
   ↓
2. Criação de ScrollBar
   ↓
3. Configuração de Range
   ↓
4. Eventos de Interação
   ↓
5. Atualização de Posição
   ↓
6. Redesenho do Conteúdo
```

---

## 📜 Tipos de Scroll

### 🎯 **UIScrollBar (Básico)**

Scrollbar padrão com funcionalidades básicas.

```lua
-- Estrutura do UIScrollBar
    --  Estrutura do UIScrollBar (traduzido)
{
    orientation = 'vertical',    -- 'vertical' ou 'horizontal'
    value = 0,                   -- Valor atual
    minimum = 0,                 -- Valor mínimo
    maximum = 100,               -- Valor máximo
    step = 1,                    -- Incremento por passo
    pixelsScroll = false,        -- Scroll por pixels
    mouseScroll = true,          -- Scroll por mouse
    showValue = false            -- Mostrar valor
}
```

### 🎨 **UIScrollArea (Avançado)**

Área de conteúdo com scroll automático.

```lua
-- Estrutura do UIScrollArea
    --  Estrutura do UIScrollArea (traduzido)
{
    verticalScrollBar = nil,     -- Scrollbar vertical
    horizontalScrollBar = nil,   -- Scrollbar horizontal
    virtualOffset = {x=0, y=0},  -- Offset virtual
    inverted = false,            -- Scroll invertido
    alwaysScrollMaximum = false  -- Sempre scroll máximo
}
```

### 📄 **Sistema de Paginação**

Navegação por páginas de conteúdo.

#### Nível Basic
```lua
-- Estrutura de Paginação
{
    currentPage = 1,             -- Página atual
    totalPages = 1,              -- Total de páginas
    itemsPerPage = 25,           -- Itens por página
    totalItems = 0,              -- Total de itens
    navigation = {}              -- Controles de navegação
}
```

#### Nível Intermediate
```lua
-- Estrutura de Paginação
{
    currentPage = 1,             -- Página atual
    totalPages = 1,              -- Total de páginas
    itemsPerPage = 25,           -- Itens por página
    totalItems = 0,              -- Total de itens
    navigation = {}              -- Controles de navegação
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
```lua
-- Estrutura de Paginação
{
    currentPage = 1,             -- Página atual
    totalPages = 1,              -- Total de páginas
    itemsPerPage = 25,           -- Itens por página
    totalItems = 0,              -- Total de itens
    navigation = {}              -- Controles de navegação
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

---

## 🐍 API Lua

### 📦 **Métodos de UIScrollBar**

```lua
-- Criar scrollbar
    --  Criar scrollbar (traduzido)
local scrollBar = UIScrollBar.create()

-- Configurar valores
    --  Configurar valores (traduzido)
scrollBar:setValue(value)
scrollBar:setMinimum(min)
scrollBar:setMaximum(max)
scrollBar:setStep(step)

-- Navegação
scrollBar:increment(count)
scrollBar:decrement(count)
scrollBar:onIncrement()
scrollBar:onDecrement()

-- Propriedades
    --  Propriedades (traduzido)
scrollBar:setOrientation('vertical')
scrollBar:setPixelsScroll(true)
scrollBar:setMouseScroll(true)
```

### 🎯 **Métodos de UIScrollArea**

```lua
-- Criar área de scroll
local scrollArea = g_ui.createWidget('UIScrollArea', parent)

-- Configurar scrollbars
    --  Configurar scrollbars (traduzido)
scrollArea:setVerticalScrollBar(verticalBar)
scrollArea:setHorizontalScrollBar(horizontalBar)

-- Controle de offset
    --  Controle de offset (traduzido)
scrollArea:setVirtualOffset({x=0, y=0})
scrollArea:getVirtualOffset()

-- Atualização
scrollArea:updateScrollBars()
scrollArea:setInverted(true)
```

### 📄 **Métodos de Paginação**

```lua
-- Configurar paginação
function setupPagination(totalItems, itemsPerPage)
    -- Função: setupPagination
    local currentPage = 1
    local totalPages = math.ceil(totalItems / itemsPerPage)
    
    return {
        currentPage = currentPage,
        totalPages = totalPages,
        itemsPerPage = itemsPerPage,
        totalItems = totalItems
    }
end

-- Navegar entre páginas
function nextPage(pagination)
    -- Função: nextPage
    if pagination.currentPage < pagination.totalPages then
    -- Verificação condicional
        pagination.currentPage = pagination.currentPage + 1
        return true
    end
    return false
end

function prevPage(pagination)
    -- Função: prevPage
    if pagination.currentPage > 1 then
    -- Verificação condicional
        pagination.currentPage = pagination.currentPage - 1
        return true
    end
    return false
end
```

---

## 📜 UIScrollBar

### 🎯 **Implementação Completa**

#### Inicialização e Configuração
```lua
-- Classe UIScrollBar
UIScrollBar = extends(UIWidget, 'UIScrollBar')

-- Funções privadas
local function calcValues(self)
    local slider = self:getChildById('sliderButton')
    local decrementButton = self:getChildById('decrementButton')
    local incrementButton = self:getChildById('incrementButton')

    local pxrange, center
    if self.orientation == 'vertical' then
        pxrange = (self:getHeight() - decrementButton:getHeight() - decrementButton:getMarginTop() -
                      decrementButton:getMarginBottom() - incrementButton:getHeight() - incrementButton:getMarginTop() -
                      incrementButton:getMarginBottom())
        center = self:getY() + math.floor(self:getHeight() / 2)
    else -- horizontal
        pxrange = (self:getWidth() - decrementButton:getWidth() - decrementButton:getMarginLeft() -
                      decrementButton:getMarginRight() - incrementButton:getWidth() - incrementButton:getMarginLeft() -
                      incrementButton:getMarginRight())
        center = self:getX() + math.floor(self:getWidth() / 2)
    end
```

#### Funcionalidade 1
```lua

    local range = self.maximum - self.minimum + 1
    local proportion

    if self.pixelsScroll then
        proportion = pxrange / (range + pxrange)
    else
        proportion = math.min(math.max(self.step, 1), range) / range
    end

    local px = math.max(proportion * pxrange, 6)
    px = px - px % 2 + 1

    if self.scrollSize and self:getParent() and self:getParent().scrollSize then
        px = math.max(self:getParent().scrollSize, 14)
    end

    local offset = 0
    if range == 0 or self.value == self.minimum then
        if self.orientation == 'vertical' then
            offset = -math.floor((self:getHeight() - px) / 2) + decrementButton:getMarginRect().height
        else
            offset = -math.floor((self:getWidth() - px) / 2) + decrementButton:getMarginRect().width
        end
```

#### Funcionalidade 2
```lua
    elseif range > 1 and self.value == self.maximum then
        if self.orientation == 'vertical' then
            offset = math.floor((self:getHeight() - px) / 2) - incrementButton:getMarginRect().height
        else
            offset = math.floor((self:getWidth() - px) / 2) - incrementButton:getMarginRect().width
        end
    else
        local percent = (self.value - self.minimum) / range
        if self.orientation == 'vertical' then
            offset = percent * pxrange - math.floor(px / 2)
        else
            offset = percent * pxrange - math.floor(px / 2)
        end
    end

    if self.orientation == 'vertical' then
        slider:setSize({width = px, height = px})
        slider:setPosition({x = center - math.floor(px / 2), y = self:getY() + offset})
    else
        slider:setSize({width = px, height = px})
        slider:setPosition({x = self:getX() + offset, y = center - math.floor(px / 2)})
    end
```

#### Funcionalidade 3
```lua

    if self.showValue then
        local valueLabel = self:getChildById('valueLabel')
        if valueLabel then
            valueLabel:setText(tostring(self.value))
        end
    end
end

local function updateSlider(self)
    if not self.setupDone then
        return
    end
    calcValues(self)
end

local function parseSliderPos(self, slider, mousePos, mouseMoved)
    if not mouseMoved then
        return
    end

    local newvalue
    local decrementButton = self:getChildById('decrementButton')
    local incrementButton = self:getChildById('incrementButton')

    if self.orientation == 'vertical' then
        local pxrange = (self:getHeight() - decrementButton:getHeight() - decrementButton:getMarginTop() -
                            decrementButton:getMarginBottom() - incrementButton:getHeight() - incrementButton:getMarginTop() -
                            incrementButton:getMarginBottom())
        local range = self.maximum - self.minimum + 1
        local percent = (mousePos.y - self:getY() - self.hotDistance) / pxrange
        newvalue = self.minimum + math.floor(percent * range)
    else
        local pxrange = (self:getWidth() - decrementButton:getWidth() - decrementButton:getMarginLeft() -
                            decrementButton:getMarginRight() - incrementButton:getWidth() - incrementButton:getMarginLeft() -
                            incrementButton:getMarginRight())
        local range = self.maximum - self.minimum + 1
        local percent = (mousePos.x - self:getX() - self.hotDistance) / pxrange
        newvalue = self.minimum + math.floor(percent * range)
    end
```

#### Funcionalidade 4
```lua

    newvalue = math.max(self.minimum, math.min(self.maximum, newvalue))
    if newvalue ~= self.value then
        self:setValue(newvalue)
    end
end

local function parseSliderPress(self, slider, pos, button)
    if self.orientation == 'vertical' then
        self.hotDistance = pos.y - slider:getY()
    else
        self.hotDistance = pos.x - slider:getX()
    end
end

-- Criar scrollbar
function UIScrollBar.create()
    local scrollbar = UIScrollBar.internalCreate()
    scrollbar:setFocusable(false)
    scrollbar.value = 0
    scrollbar.minimum = -999999
    scrollbar.maximum = 999999
    scrollbar.step = 1
    scrollbar.orientation = 'vertical'
    scrollbar.pixelsScroll = false
    scrollbar.showValue = false
    scrollbar.symbol = nil
    scrollbar.mouseScroll = true
    scrollbar.scrollSize = nil
    return scrollbar
end
```

#### Funcionalidade 5
```lua

-- Configurar após criação
function UIScrollBar:onSetup()
    self.setupDone = true
    local sliderButton = self:getChildById('sliderButton')
    
    g_mouse.bindAutoPress(self:getChildById('decrementButton'), function()
        self:onDecrement()
    end, 300)
    
    g_mouse.bindAutoPress(self:getChildById('incrementButton'), function()
        self:onIncrement()
    end, 300)
    
    g_mouse.bindPressMove(sliderButton, function(mousePos, mouseMoved)
        parseSliderPos(self, sliderButton, mousePos, mouseMoved)
    end)
    
    g_mouse.bindPress(sliderButton, function(mousePos, mouseButton)
        parseSliderPress(self, sliderButton, mousePos, mouseButton)
    end)
```

#### Funcionalidade 6
```lua

    updateSlider(self)

    if self:getParent() then
        if self:getParent().minimumScrollValue then
            self:setMinimum(self:getParent().minimumScrollValue)
        end
        if self:getParent().maximumScrollValue then
            self:setMaximum(self:getParent().maximumScrollValue)
        end
    end
end

-- Aplicar estilo
function UIScrollBar:onStyleApply(styleName, styleNode)
    for name, value in pairs(styleNode) do
        if name == 'maximum' then
            self:setMaximum(tonumber(value))
        elseif name == 'minimum' then
            self:setMinimum(tonumber(value))
        elseif name == 'step' then
            self:setStep(tonumber(value))
        elseif name == 'orientation' then
            self:setOrientation(value)
        elseif name == 'value' then
            self:setValue(value)
        elseif name == 'pixels-scroll' then
            self.pixelsScroll = true
        elseif name == 'show-value' then
            self.showValue = true
        elseif name == 'symbol' then
            self.symbol = value
        elseif name == 'mouse-scroll' then
            self.mouseScroll = value
        elseif name == 'parent-scroll' then
            self.scrollSize = value
        end
```

#### Funcionalidade 7
```lua
    end
end

-- Eventos de decremento
function UIScrollBar:onDecrement()
    if g_keyboard.isCtrlPressed() then
        self:decrement(self.value)
    elseif g_keyboard.isShiftPressed() then
        self:decrement(10)
    else
        self:decrement()
    end
end

-- Eventos de incremento
function UIScrollBar:onIncrement()
    if g_keyboard.isCtrlPressed() then
        self:increment(self.maximum)
    elseif g_keyboard.isShiftPressed() then
        self:increment(10)
    else
        self:increment()
    end
```

#### Funcionalidade 8
```lua
end

-- Decrementar valor
function UIScrollBar:decrement(count)
    count = count or self.step
    self:setValue(self.value - count)
end

-- Incrementar valor
function UIScrollBar:increment(count)
    count = count or self.step
    self:setValue(self.value + count)
end

-- Definir valor máximo
function UIScrollBar:setMaximum(maximum)
    if maximum == self.maximum then
        return
    end
    self.maximum = maximum
    if self.minimum > maximum then
        self:setMinimum(maximum)
    end
```

#### Funcionalidade 9
```lua
    if self.value > maximum then
        self:setValue(maximum)
    else
        updateSlider(self)
    end
end

-- Definir valor mínimo
function UIScrollBar:setMinimum(minimum)
    if minimum == self.minimum then
        return
    end
    self.minimum = minimum
    if self.maximum < minimum then
        self:setMaximum(minimum)
    end
    if self.value < minimum then
        self:setValue(minimum)
    else
        updateSlider(self)
    end
```

#### Funcionalidade 10
```lua
end

-- Definir valor atual
function UIScrollBar:setValue(value)
    if value == self.value then
        return
    end
    self.value = value
    updateSlider(self)
    signalcall(self.onValueChange, self, value)
end

-- Definir passo
function UIScrollBar:setStep(step)
    self.step = step
end

-- Definir orientação
function UIScrollBar:setOrientation(orientation)
    self.orientation = orientation
    updateSlider(self)
end
```

#### Funcionalidade 11
```lua

-- Evento de mudança de geometria
function UIScrollBar:onGeometryChange()
    updateSlider(self)
end

-- Evento de wheel do mouse
function UIScrollBar:onMouseWheel(mousePos, mouseWheel)
    if not self.mouseScroll or not self:isOn() then
        return false
    end
    
    if mouseWheel == MouseWheelUp then
        if self.orientation == 'vertical' then
            if self.value <= self.minimum then
                return false
            end
            self:decrement()
        else
            if self.value >= self.maximum then
                return false
            end
```

#### Funcionalidade 12
```lua
            self:increment()
        end
    else
        if self.orientation == 'vertical' then
            if self.value >= self.maximum then
                return false
            end
            self:increment()
        else
            if self.value <= self.minimum then
                return false
            end
            self:decrement()
        end
    end
    return true
end

-- Getters
function UIScrollBar:getMaximum()
    return self.maximum
end
```

#### Funcionalidade 13
```lua

function UIScrollBar:getMinimum()
    return self.minimum
end

function UIScrollBar:getValue()
    return math.round(self.value)
end

function UIScrollBar:getStep()
    return self.step
end

function UIScrollBar:getOrientation()
    return self.orientation
end

function UIScrollBar:getShowValue()
    return self.showValue
end

function UIScrollBar:getSymbol()
```

#### Finalização
```lua
    return self.symbol
end

function UIScrollBar:getMouseScroll()
    return self.mouseScroll
end
```

### 🎨 **Estilo OTUI para UIScrollBar**

```otui
ScrollBarSlider < UIButton
  id: sliderButton
  anchors.centerIn: parent
  size: 13 17
  image-source: /images/ui/scrollbar
  image-clip: 0 26 13 13
  image-border: 2
  image-color: #ffffffff
  
  $hover:
    image-clip: 13 26 13 13
    
  $pressed:
    image-clip: 26 26 13 13
    
  $disabled:
    image-color: #ffffff66

ScrollBarValueLabel < Label
  id: valueLabel
  anchors.fill: parent
  color: white
  text-align: center

VerticalScrollBar < UIScrollBar
  orientation: vertical
  width: 13
  height: 39
  image-source: /images/ui/scrollbar
  image-clip: 39 0 13 65
  image-border: 1
  pixels-scroll: true

  UIButton
    id: decrementButton
    anchors.top: parent.top
    anchors.left: parent.left
    image-source: /images/ui/scrollbar
    image-clip: 0 0 13 13
    image-color: #ffffffff
    size: 13 13
    
    $hover:
      image-clip: 13 0 13 13
      
    $pressed:
      image-clip: 26 0 13 13
      
    $disabled:
      image-color: #ffffff66

  UIButton
    id: incrementButton
    anchors.bottom: parent.bottom
    anchors.right: parent.right
    size: 13 13
    image-source: /images/ui/scrollbar
    image-clip: 0 13 13 13
    image-color: #ffffffff
    
    $hover:
      image-clip: 13 13 13 13
      
    $pressed:
      image-clip: 26 13 13 13
      
    $disabled:
      image-color: #ffffff66

  ScrollBarSlider
  ScrollBarValueLabel

HorizontalScrollBar < UIScrollBar
  orientation: horizontal
  height: 13
  width: 39
  image-source: /images/ui/scrollbar
  image-clip: 0 65 52 13
  image-border: 1

  $disabled:
    color: #bbbbbb88

  UIButton
    id: decrementButton
    anchors.top: parent.top
    anchors.left: parent.left
    image-source: /images/ui/scrollbar
    image-clip: 0 39 13 13
    image-color: #ffffffff
    size: 13 13
    
    $hover:
      image-clip: 13 39 13 13
      
    $pressed:
      image-clip: 26 39 13 13
      
    $disabled:
      image-color: #ffffff66

  UIButton
    id: incrementButton
    anchors.bottom: parent.bottom
    anchors.right: parent.right
    size: 13 13
    image-source: /images/ui/scrollbar
    image-clip: 0 52 13 13
    image-color: #ffffffff
    
    $hover:
      image-clip: 13 52 13 13
      
    $pressed:
      image-clip: 26 52 13 13
      
    $disabled:
      image-color: #ffffff66

  ScrollBarSlider
  ScrollBarValueLabel
```

---

## 📜 UIScrollArea

### 🎯 **Implementação Completa**

#### Inicialização e Configuração
```lua
-- Classe UIScrollArea
UIScrollArea = extends(UIWidget, 'UIScrollArea')

-- Aplicar estilo
function UIScrollArea:onStyleApply(styleName, styleNode)
    for name, value in pairs(styleNode) do
        if name == 'vertical-scrollbar' then
            self:setVerticalScrollBar(g_ui.createWidget(value))
        elseif name == 'horizontal-scrollbar' then
            self:setHorizontalScrollBar(g_ui.createWidget(value))
        elseif name == 'inverted' then
            self:setInverted(value)
        elseif name == 'always-scroll-maximum' then
            self:setAlwaysScrollMaximum(value)
        end
    end
end

-- Atualizar scrollbars
function UIScrollArea:updateScrollBars()
    local scrollWidth = math.max(self:getChildrenRect().width - self:getPaddingRect().width, 0)
    local scrollHeight = math.max(self:getChildrenRect().height - self:getPaddingRect().height, 0)

    local scrollbar = self.verticalScrollBar
    if scrollbar then
        if self.inverted then
            scrollbar:setMinimum(-scrollHeight)
            scrollbar:setMaximum(0)
        else
            scrollbar:setMinimum(0)
            scrollbar:setMaximum(scrollHeight)
        end
```

#### Funcionalidade 1
```lua
    end

    local scrollbar = self.horizontalScrollBar
    if scrollbar then
        if self.inverted then
            scrollbar:setMinimum(-scrollWidth)
            scrollbar:setMaximum(0)
        else
            scrollbar:setMinimum(0)
            scrollbar:setMaximum(scrollWidth)
        end
    end

    if self.lastScrollWidth ~= scrollWidth then
        self:onScrollWidthChange()
    end
    if self.lastScrollHeight ~= scrollHeight then
        self:onScrollHeightChange()
    end

    self.lastScrollWidth = scrollWidth
    self.lastScrollHeight = scrollHeight
end
```

#### Funcionalidade 2
```lua

-- Definir scrollbar vertical
function UIScrollArea:setVerticalScrollBar(scrollbar)
    self.verticalScrollBar = scrollbar
    connect(self.verticalScrollBar, 'onValueChange', function(scrollbar, value)
        local virtualOffset = self:getVirtualOffset()
        virtualOffset.y = value
        self:setVirtualOffset(virtualOffset)
        signalcall(self.onScrollChange, self, virtualOffset)
    end)
    self:updateScrollBars()
end

-- Definir scrollbar horizontal
function UIScrollArea:setHorizontalScrollBar(scrollbar)
    self.horizontalScrollBar = scrollbar
    connect(self.horizontalScrollBar, 'onValueChange', function(scrollbar, value)
        local virtualOffset = self:getVirtualOffset()
        virtualOffset.x = value
        self:setVirtualOffset(virtualOffset)
        signalcall(self.onScrollChange, self, virtualOffset)
    end)
```

#### Funcionalidade 3
```lua
    self:updateScrollBars()
end

-- Definir scroll invertido
function UIScrollArea:setInverted(inverted)
    self.inverted = inverted
end

-- Definir sempre scroll máximo
function UIScrollArea:setAlwaysScrollMaximum(value)
    self.alwaysScrollMaximum = value
end

-- Obter offset virtual
function UIScrollArea:getVirtualOffset()
    return self.virtualOffset or {x = 0, y = 0}
end

-- Definir offset virtual
function UIScrollArea:setVirtualOffset(offset)
    self.virtualOffset = offset
    self:updateChildrenOffset()
end
```

#### Finalização
```lua

-- Atualizar offset dos filhos
function UIScrollArea:updateChildrenOffset()
    local offset = self:getVirtualOffset()
    for i = 1, self:getChildCount() do
        local child = self:getChildByIndex(i)
        local pos = child:getPosition()
        child:setPosition({x = pos.x - offset.x, y = pos.y - offset.y})
    end
end

-- Evento de mudança de largura do scroll
function UIScrollArea:onScrollWidthChange()
    -- Implementação específica
end

-- Evento de mudança de altura do scroll
function UIScrollArea:onScrollHeightChange()
    -- Implementação específica
end
```

---

## 💡 Exemplos Práticos

### 🎯 **Exemplo 1: Sistema de Scroll Básico**

```lua
local BasicScrollSystem = {}

function BasicScrollSystem.createBasicScroll(parent)
    -- Função: BasicScrollSystem
    local scrollArea = g_ui.createWidget('UIScrollArea', parent)
    scrollArea:setSize({width = 300, height = 200})
    
    -- Criar scrollbar vertical
    --  Criar scrollbar vertical (traduzido)
    local verticalScrollBar = g_ui.createWidget('VerticalScrollBar', parent)
    verticalScrollBar:setPosition({x = 310, y = 0})
    verticalScrollBar:setSize({width = 13, height = 200})
    
    scrollArea:setVerticalScrollBar(verticalScrollBar)
    
    -- Adicionar conteúdo
    for i = 1, 20 do
    -- Loop de repetição
        local label = g_ui.createWidget('Label', scrollArea)
        label:setText('Item ' .. i)
        label:setPosition({x = 10, y = (i-1) * 25})
        label:setSize({width = 280, height = 20})
    end
    
    return scrollArea
end

-- Uso
    --  Uso (traduzido)
local scrollArea = BasicScrollSystem.createBasicScroll(parent)
```

### 🎨 **Exemplo 2: Sistema de Paginação**

#### Inicialização e Configuração
```lua
local PaginationSystem = {}

function PaginationSystem.createPagination(parent, totalItems, itemsPerPage)
    local pagination = {
        currentPage = 1,
        totalPages = math.ceil(totalItems / itemsPerPage),
        itemsPerPage = itemsPerPage,
        totalItems = totalItems
    }
    
    -- Container principal
    local container = g_ui.createWidget('Panel', parent)
    container:setSize({width = 400, height = 300})
    
    -- Área de conteúdo
    local contentArea = g_ui.createWidget('UIScrollArea', container)
    contentArea:setPosition({x = 0, y = 0})
    contentArea:setSize({width = 400, height = 250})
    
    -- Scrollbar
    local scrollBar = g_ui.createWidget('VerticalScrollBar', container)
    scrollBar:setPosition({x = 410, y = 0})
    scrollBar:setSize({width = 13, height = 250})
    
    contentArea:setVerticalScrollBar(scrollBar)
    
    -- Controles de paginação
    local paginationPanel = g_ui.createWidget('Panel', container)
    paginationPanel:setPosition({x = 0, y = 260})
    paginationPanel:setSize({width = 400, height = 40})
    
    -- Botão anterior
    local prevButton = g_ui.createWidget('Button', paginationPanel)
    prevButton:setText('Anterior')
    prevButton:setPosition({x = 10, y = 10})
    prevButton:setSize({width = 80, height = 20})
    
    prevButton.onClick = function()
        if pagination.currentPage > 1 then
            pagination.currentPage = pagination.currentPage - 1
            PaginationSystem.updateContent(contentArea, pagination)
            PaginationSystem.updateControls(paginationPanel, pagination)
        end
```

#### Funcionalidade 1
```lua
    end
    
    -- Botão próximo
    local nextButton = g_ui.createWidget('Button', paginationPanel)
    nextButton:setText('Próximo')
    nextButton:setPosition({x = 310, y = 10})
    nextButton:setSize({width = 80, height = 20})
    
    nextButton.onClick = function()
        if pagination.currentPage < pagination.totalPages then
            pagination.currentPage = pagination.currentPage + 1
            PaginationSystem.updateContent(contentArea, pagination)
            PaginationSystem.updateControls(paginationPanel, pagination)
        end
    end
    
    -- Label de página
    local pageLabel = g_ui.createWidget('Label', paginationPanel)
    pageLabel:setPosition({x = 150, y = 10})
    pageLabel:setSize({width = 100, height = 20})
    pageLabel:setTextAlign(AlignCenter)
    
    pagination.pageLabel = pageLabel
    
    -- Inicializar conteúdo
    PaginationSystem.updateContent(contentArea, pagination)
    PaginationSystem.updateControls(paginationPanel, pagination)
    
    return container, pagination
end
```

#### Funcionalidade 2
```lua

function PaginationSystem.updateContent(contentArea, pagination)
    -- Limpar conteúdo atual
    contentArea:clearChildren()
    
    -- Calcular itens da página atual
    local startIndex = (pagination.currentPage - 1) * pagination.itemsPerPage + 1
    local endIndex = math.min(startIndex + pagination.itemsPerPage - 1, pagination.totalItems)
    
    -- Adicionar itens
    for i = startIndex, endIndex do
        local item = g_ui.createWidget('Label', contentArea)
        item:setText('Item ' .. i)
        item:setPosition({x = 10, y = (i - startIndex) * 25})
        item:setSize({width = 380, height = 20})
    end
end

function PaginationSystem.updateControls(paginationPanel, pagination)
    local pageLabel = pagination.pageLabel
    pageLabel:setText('Página ' .. pagination.currentPage .. '/' .. pagination.totalPages)
    
    -- Atualizar estado dos botões
    local prevButton = paginationPanel:getChildByIndex(1)
    local nextButton = paginationPanel:getChildByIndex(2)
    
    prevButton:setEnabled(pagination.currentPage > 1)
    nextButton:setEnabled(pagination.currentPage < pagination.totalPages)
end
```

#### Finalização
```lua

-- Uso
local container, pagination = PaginationSystem.createPagination(parent, 100, 10)
```

### 🪟 **Exemplo 3: Sistema de Scroll Avançado**

```lua
local AdvancedScrollSystem = {}

function AdvancedScrollSystem.createAdvancedScroll(parent)
    -- Função: AdvancedScrollSystem
    local scrollArea = g_ui.createWidget('UIScrollArea', parent)
    scrollArea:setSize({width = 500, height = 400})
    
    -- Scrollbar vertical
    --  Scrollbar vertical (traduzido)
    local verticalScrollBar = g_ui.createWidget('VerticalScrollBar', scrollArea)
    verticalScrollBar:setPosition({x = 510, y = 0})
    verticalScrollBar:setSize({width = 13, height = 400})
    verticalScrollBar:setStep(20)
    verticalScrollBar:setPixelsScroll(true)
    
    scrollArea:setVerticalScrollBar(verticalScrollBar)
    
    -- Scrollbar horizontal
    --  Scrollbar horizontal (traduzido)
    local horizontalScrollBar = g_ui.createWidget('HorizontalScrollBar', scrollArea)
    horizontalScrollBar:setPosition({x = 0, y = 410})
    horizontalScrollBar:setSize({width = 500, height = 13})
    horizontalScrollBar:setStep(20)
    horizontalScrollBar:setPixelsScroll(true)
    
    scrollArea:setHorizontalScrollBar(horizontalScrollBar)
    
    -- Conteúdo com grid
    local gridPanel = g_ui.createWidget('Panel', scrollArea)
    gridPanel:setPosition({x = 0, y = 0})
    gridPanel:setSize({width = 800, height = 600})
    
    -- Criar grid de itens
    --  Criar grid de itens (traduzido)
    for row = 1, 20 do
    -- Loop de repetição
        for col = 1, 10 do
    -- Loop de repetição
            local item = g_ui.createWidget('UIItem', gridPanel)
            item:setPosition({x = (col-1) * 80, y = (row-1) * 30})
            item:setSize({width = 75, height = 25})
            item:setText('Item ' .. ((row-1) * 10 + col))
        end
    end
    
    -- Eventos de scroll
    --  Eventos de scroll (traduzido)
    scrollArea.onScrollChange = function(area, offset)
        print('Scroll offset:', offset.x, offset.y)
    end
    
    return scrollArea
end

-- Uso
    --  Uso (traduzido)
local advancedScroll = AdvancedScrollSystem.createAdvancedScroll(parent)
```

---

## ✅ Melhores Práticas

### 🎯 **Configuração Adequada**

```lua
-- ✅ BOM: Sempre definir range adequado
    --  ✅ BOM: Sempre definir range adequado (traduzido)
function setupScrollBarWithRange(scrollBar, min, max, step)
    -- Função: setupScrollBarWithRange
    scrollBar:setMinimum(min)
    scrollBar:setMaximum(max)
    scrollBar:setStep(step)
    scrollBar:setValue(min)
end

-- ✅ BOM: Configurar scroll por pixels quando necessário
function setupPixelScroll(scrollBar, enabled)
    -- Função: setupPixelScroll
    scrollBar:setPixelsScroll(enabled)
    if enabled then
    -- Verificação condicional
        scrollBar:setStep(1)
    end
end

-- ✅ BOM: Validar valores antes de definir
    --  ✅ BOM: Validar valores antes de definir (traduzido)
function validateScrollValue(scrollBar, value)
    -- Função: validateScrollValue
    local min = scrollBar:getMinimum()
    local max = scrollBar:getMaximum()
    
    if value < min then
    -- Verificação condicional
        value = min
    elseif value > max then
        value = max
    end
    
    return value
end
```

### 🎨 **Organização de Conteúdo**

#### Nível Basic
```lua
-- ✅ BOM: Organizar conteúdo em containers
function organizeScrollContent(scrollArea, contentCreator)
    local container = g_ui.createWidget('Panel', scrollArea)
end
-- ✅ BOM: Usar layouts para organização automática
function setupScrollWithLayout(scrollArea, layoutType)
    -- Adicionar conteúdo
        local item = g_ui.createWidget('Label', scrollArea)
    end
end
```

#### Nível Intermediate
```lua
-- ✅ BOM: Organizar conteúdo em containers
function organizeScrollContent(scrollArea, contentCreator)
    local container = g_ui.createWidget('Panel', scrollArea)
    container:setSize({width = 1000, height = 1000}) -- Tamanho virtual
    
    contentCreator(container)
    
    return container
end

-- ✅ BOM: Usar layouts para organização automática
function setupScrollWithLayout(scrollArea, layoutType)
    scrollArea:setLayout(layoutType)
    
    -- Adicionar conteúdo
    for i = 1, 50 do
        local item = g_ui.createWidget('Label', scrollArea)
        item:setText('Item ' .. i)
    end
end
```

#### Nível Advanced
```lua
-- ✅ BOM: Organizar conteúdo em containers
function organizeScrollContent(scrollArea, contentCreator)
    local container = g_ui.createWidget('Panel', scrollArea)
    container:setSize({width = 1000, height = 1000}) -- Tamanho virtual
    
    contentCreator(container)
    
    return container
end

-- ✅ BOM: Usar layouts para organização automática
function setupScrollWithLayout(scrollArea, layoutType)
    scrollArea:setLayout(layoutType)
    
    -- Adicionar conteúdo
    for i = 1, 50 do
        local item = g_ui.createWidget('Label', scrollArea)
        item:setText('Item ' .. i)
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

### 🔧 **Performance Otimizada**

```lua
-- ✅ BOM: Lazy loading de conteúdo
function setupLazyScrollContent(scrollArea, totalItems, itemCreator)
    -- Função: setupLazyScrollContent
    local visibleItems = 20
    local currentOffset = 0
    
    local function loadVisibleItems()
        scrollArea:clearChildren()
        
        for i = currentOffset + 1, math.min(currentOffset + visibleItems, totalItems) do
    -- Loop de repetição
            local item = itemCreator(i)
            scrollArea:addChild(item)
        end
    end
    
    scrollArea.onScrollChange = function(area, offset)
        local newOffset = math.floor(offset.y / 25) -- Altura do item
        if newOffset ~= currentOffset then
    -- Verificação condicional
            currentOffset = newOffset
            loadVisibleItems()
        end
    end
    
    loadVisibleItems()
end
```

---

## 🚀 Performance e Otimização

### 📊 **Métricas de Performance**

1. **Tempo de Criação**: < 1ms por scrollbar
2. **Tempo de Atualização**: < 0.5ms
3. **Uso de Memória**: < 0.5KB por scrollbar
4. **Tempo de Scroll**: < 0.1ms por evento

### 🎯 **Técnicas de Otimização**

```lua
-- Virtual scrolling para grandes listas
    --  Virtual scrolling para grandes listas (traduzido)
local VirtualScrollSystem = {}

function VirtualScrollSystem.createVirtualScroll(parent, totalItems, itemHeight)
    -- Função: VirtualScrollSystem
    local scrollArea = g_ui.createWidget('UIScrollArea', parent)
    local scrollBar = g_ui.createWidget('VerticalScrollBar', scrollArea)
    
    scrollArea:setVerticalScrollBar(scrollBar)
    
    local visibleItems = math.ceil(scrollArea:getHeight() / itemHeight)
    local virtualItems = {}
    
    -- Criar apenas itens visíveis
    for i = 1, visibleItems do
    -- Loop de repetição
        local item = g_ui.createWidget('Label', scrollArea)
        item:setSize({width = scrollArea:getWidth(), height = itemHeight})
        item:setPosition({x = 0, y = (i-1) * itemHeight})
        table.insert(virtualItems, item)
    end
    
    -- Atualizar conteúdo baseado na posição do scroll
    scrollArea.onScrollChange = function(area, offset)
        local startIndex = math.floor(offset.y / itemHeight) + 1
        
        for i, item in ipairs(virtualItems) do
    -- Loop de repetição
            local itemIndex = startIndex + i - 1
            if itemIndex <= totalItems then
    -- Verificação condicional
                item:setText('Item ' .. itemIndex)
                item:setVisible(true)
            else
                item:setVisible(false)
            end
        end
    end
    
    return scrollArea
end
```

### 🔧 **Monitoramento de Performance**

```lua
-- Função para medir performance de scroll
local function measureScrollPerformance()
    local startTime = g_clock.millis()
    
    local scrollBar = g_ui.createWidget('VerticalScrollBar')
    scrollBar:setMinimum(0)
    scrollBar:setMaximum(1000)
    
    for i = 1, 100 do
    -- Loop de repetição
        scrollBar:setValue(i)
    end
    
    local endTime = g_clock.millis()
    print('Tempo de scroll:', endTime - startTime, 'ms')
    
    scrollBar:destroy()
end

-- Sistema de métricas
local scrollMetrics = {
    created = 0,
    updated = 0,
    totalTime = 0
}

function trackScrollCreation()
    -- Função: trackScrollCreation
    scrollMetrics.created = scrollMetrics.created + 1
end

function trackScrollUpdate(duration)
    -- Função: trackScrollUpdate
    scrollMetrics.updated = scrollMetrics.updated + 1
    scrollMetrics.totalTime = scrollMetrics.totalTime + duration
end
```

---

## 📚 Referências

### 🔗 **Links Automáticos**

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

## 🔗 Links Relacionados
- [UIAdvancedWidgets](UIAdvancedWidgets.md) - Widgets Avançados
- [UIAnimations](UIAnimations.md) - Sistema de Animações
- [UIFormWidgets](UIFormWidgets.md) - Widgets de Formulário
- [UIDragDrop](UIDragDrop.md) - Sistema de Drag & Drop
- [UIModals](UIModals.md) - Sistema de Modais e Diálogos
- [UITabs](UITabs.md) - Sistema de Tabs e Abas

### 📖 Documentação Técnica
- **UIScrollBar**: Sistema básico de scrollbars
- **UIScrollArea**: Áreas de conteúdo com scroll
- **Scroll Styles**: Estilos visuais disponíveis

---

**Última Atualização**: 2025-01-27  
**Versão**: 1.0  
**Status**: ✅ **Completo**  
**Prioridade**: 🔥 **MÁXIMA** 