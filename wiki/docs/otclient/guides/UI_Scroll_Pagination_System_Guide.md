
# 📜 Sistema de Scroll e Paginação

> [!info] O Sistema de Scroll e Paginação do OTClient oferece funcionalidades avançadas para navegação em conteúdo extenso, incluindo scrollbars verticais/horizontais, áreas de scroll e sistemas de paginação para organizar dados em páginas.


---

## 📋 Índice 📋
- [[#Visão Geral]]
- [[#Componentes do Sistema]]
- [[#Implementação Prática]]
- [[#Exemplos Práticos]]
- [[#Melhores Práticas]]

---


---

## 🎯 Visão Geral 🎯

O **Sistema de Scroll e Paginação** do OTClient oferece funcionalidades avançadas para navegação em conteúdo extenso, incluindo scrollbars verticais/horizontais, áreas de scroll e sistemas de paginação para organizar dados em páginas.

### 🎨 **Características Principais** 📝

- **UIScrollBar**: Scrollbars verticais e horizontais
- **UIScrollArea**: Áreas de conteúdo com scroll
- **Sistema de Paginação**: Navegação por páginas
- **Scroll por Mouse**: Suporte a wheel do mouse
- **Scroll por Teclado**: Navegação por teclado
- **Estilos Flexíveis**: Diferentes aparências de scrollbar

---


---

## 🔧 Componentes do Sistema ⚙️

### 🏗️ **Arquitetura do Sistema** 📝

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

### 🔄 **Fluxo de Scroll** 📝

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

### 🎭 **Estrutura de Dados** 🏗️

#### 📜 **UIScrollBar (Básico)**

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

#### 🎨 **UIScrollArea (Avançado)**

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

#### 📄 **Sistema de Paginação**

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


---

## 💡 Implementação Prática 📋

### 🐍 **API Lua** 📝

#### 📦 **Métodos de UIScrollBar**

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

#### 🎯 **Métodos de UIScrollArea**

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

#### 📄 **Métodos de Paginação**

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

function goToPage(pagination, page)
    -- Função: goToPage
    if page >= 1 and page <= pagination.totalPages then
    -- Verificação condicional
        pagination.currentPage = page
        return true
    end
    return false
end
```

### 🎮 **Implementação Completa do Sistema** 💻

#### Inicialização e Configuração
```lua
-- Sistema completo de Scroll e Paginação
local ScrollPaginationSystem = {}

-- Configurações padrão
ScrollPaginationSystem.defaults = {
    itemsPerPage = 25,
    scrollStep = 1,
    mouseScroll = true,
    keyboardScroll = true,
    showPageInfo = true
}

-- Criar scrollbar vertical
function ScrollPaginationSystem.createVerticalScrollBar(parent)
    local scrollBar = g_ui.createWidget('VerticalScrollBar', parent)
    
    -- Configurações padrão
    scrollBar:setMinimum(0)
    scrollBar:setMaximum(100)
    scrollBar:setValue(0)
    scrollBar:setStep(1)
    scrollBar:setMouseScroll(true)
    
    -- Eventos
    scrollBar.onValueChange = function(widget, value)
        ScrollPaginationSystem.onScrollValueChange(widget, value)
    end
```

#### Funcionalidade 1
```lua
    
    return scrollBar
end

-- Criar scrollbar horizontal
function ScrollPaginationSystem.createHorizontalScrollBar(parent)
    local scrollBar = g_ui.createWidget('HorizontalScrollBar', parent)
    
    -- Configurações padrão
    scrollBar:setMinimum(0)
    scrollBar:setMaximum(100)
    scrollBar:setValue(0)
    scrollBar:setStep(1)
    scrollBar:setMouseScroll(true)
    
    -- Eventos
    scrollBar.onValueChange = function(widget, value)
        ScrollPaginationSystem.onScrollValueChange(widget, value)
    end
    
    return scrollBar
end
```

#### Funcionalidade 2
```lua

-- Criar área de scroll
function ScrollPaginationSystem.createScrollArea(parent, options)
    options = options or {}
    
    local scrollArea = g_ui.createWidget('UIScrollArea', parent)
    
    -- Configurar tamanho
    if options.size then
        scrollArea:setSize(options.size)
    end
    
    -- Configurar posição
    if options.position then
        scrollArea:setPosition(options.position)
    end
    
    -- Criar scrollbars se necessário
    if options.verticalScroll then
        local verticalBar = ScrollPaginationSystem.createVerticalScrollBar(scrollArea)
        scrollArea:setVerticalScrollBar(verticalBar)
    end
```

#### Funcionalidade 3
```lua
    
    if options.horizontalScroll then
        local horizontalBar = ScrollPaginationSystem.createHorizontalScrollBar(scrollArea)
        scrollArea:setHorizontalScrollBar(horizontalBar)
    end
    
    -- Configurar offset virtual
    if options.virtualOffset then
        scrollArea:setVirtualOffset(options.virtualOffset)
    end
    
    -- Configurar scroll invertido
    if options.inverted then
        scrollArea:setInverted(options.inverted)
    end
    
    return scrollArea
end

-- Criar sistema de paginação
function ScrollPaginationSystem.createPagination(parent, totalItems, itemsPerPage)
```

#### Funcionalidade 4
```lua
    local pagination = {
        currentPage = 1,
        totalPages = math.ceil(totalItems / itemsPerPage),
        itemsPerPage = itemsPerPage,
        totalItems = totalItems,
        onPageChange = nil
    }
    
    -- Container principal
    local container = g_ui.createWidget('Panel', parent)
    container:setSize({width = 400, height = 300})
    
    -- Área de conteúdo
    local contentArea = ScrollPaginationSystem.createScrollArea(container, {
        size = {width = 400, height = 250},
        position = {x = 0, y = 0},
        verticalScroll = true
    })
    
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
        if ScrollPaginationSystem.prevPage(pagination) then
            ScrollPaginationSystem.updateContent(contentArea, pagination)
            ScrollPaginationSystem.updateControls(paginationPanel, pagination)
            
            if pagination.onPageChange then
                pagination.onPageChange(pagination.currentPage)
            end
```

#### Funcionalidade 5
```lua
        end
    end
    
    -- Botão próximo
    local nextButton = g_ui.createWidget('Button', paginationPanel)
    nextButton:setText('Próximo')
    nextButton:setPosition({x = 310, y = 10})
    nextButton:setSize({width = 80, height = 20})
    
    nextButton.onClick = function()
        if ScrollPaginationSystem.nextPage(pagination) then
            ScrollPaginationSystem.updateContent(contentArea, pagination)
            ScrollPaginationSystem.updateControls(paginationPanel, pagination)
            
            if pagination.onPageChange then
                pagination.onPageChange(pagination.currentPage)
            end
        end
    end
    
    -- Label de página
    local pageLabel = g_ui.createWidget('Label', paginationPanel)
    pageLabel:setPosition({x = 150, y = 10})
    pageLabel:setSize({width = 100, height = 20})
    pageLabel:setTextAlign(AlignCenter)
    
    pagination.pageLabel = pageLabel
    pagination.prevButton = prevButton
    pagination.nextButton = nextButton
    pagination.contentArea = contentArea
    
    -- Inicializar conteúdo
    ScrollPaginationSystem.updateContent(contentArea, pagination)
    ScrollPaginationSystem.updateControls(paginationPanel, pagination)
    
    return container, pagination
end
```

#### Funcionalidade 6
```lua

-- Atualizar conteúdo da página
function ScrollPaginationSystem.updateContent(contentArea, pagination)
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
    
    -- Atualizar scrollbars
    contentArea:updateScrollBars()
end
```

#### Funcionalidade 7
```lua

-- Atualizar controles de paginação
function ScrollPaginationSystem.updateControls(paginationPanel, pagination)
    local pageLabel = pagination.pageLabel
    pageLabel:setText('Página ' .. pagination.currentPage .. '/' .. pagination.totalPages)
    
    -- Atualizar estado dos botões
    local prevButton = pagination.prevButton
    local nextButton = pagination.nextButton
    
    prevButton:setEnabled(pagination.currentPage > 1)
    nextButton:setEnabled(pagination.currentPage < pagination.totalPages)
end

-- Navegar para próxima página
function ScrollPaginationSystem.nextPage(pagination)
    if pagination.currentPage < pagination.totalPages then
        pagination.currentPage = pagination.currentPage + 1
        return true
    end
    return false
end
```

#### Funcionalidade 8
```lua

-- Navegar para página anterior
function ScrollPaginationSystem.prevPage(pagination)
    if pagination.currentPage > 1 then
        pagination.currentPage = pagination.currentPage - 1
        return true
    end
    return false
end

-- Ir para página específica
function ScrollPaginationSystem.goToPage(pagination, page)
    if page >= 1 and page <= pagination.totalPages then
        pagination.currentPage = page
        return true
    end
    return false
end

-- Evento de mudança de valor do scroll
function ScrollPaginationSystem.onScrollValueChange(widget, value)
```

#### Funcionalidade 9
```lua
    -- Implementar lógica de scroll customizada se necessário
    print("Scroll value changed to: " .. value)
end

-- Configurar navegação por teclado
function ScrollPaginationSystem.setupKeyboardNavigation(pagination)
    g_keyboard.bindKeyPress('PageUp', function()
        if ScrollPaginationSystem.prevPage(pagination) then
            ScrollPaginationSystem.updateContent(pagination.contentArea, pagination)
            ScrollPaginationSystem.updateControls(pagination.paginationPanel, pagination)
        end
    end)
    
    g_keyboard.bindKeyPress('PageDown', function()
        if ScrollPaginationSystem.nextPage(pagination) then
            ScrollPaginationSystem.updateContent(pagination.contentArea, pagination)
            ScrollPaginationSystem.updateControls(pagination.paginationPanel, pagination)
        end
    end)
    
    g_keyboard.bindKeyPress('Home', function()
        if ScrollPaginationSystem.goToPage(pagination, 1) then
            ScrollPaginationSystem.updateContent(pagination.contentArea, pagination)
            ScrollPaginationSystem.updateControls(pagination.paginationPanel, pagination)
        end
```

#### Finalização
```lua
    end)
    
    g_keyboard.bindKeyPress('End', function()
        if ScrollPaginationSystem.goToPage(pagination, pagination.totalPages) then
            ScrollPaginationSystem.updateContent(pagination.contentArea, pagination)
            ScrollPaginationSystem.updateControls(pagination.paginationPanel, pagination)
        end
    end)
end
```

### 🎨 **Estilo OTUI para Scroll e Paginação** 📝

```otui
ScrollPaginationWindow < MainWindow
  size: 500 400
  &minimumSize: 400 300

  Panel
    id: contentPanel
    anchors.fill: parent
    layout: verticalBox

    UIScrollArea
      id: scrollArea
      size: 0 0
      vertical-scrollbar: true
      horizontal-scrollbar: false

      Panel
        id: contentContainer
        size: 0 0
        layout: verticalBox

    Panel
      id: paginationPanel
      size: 0 40
      layout: horizontalBox

      Button
        id: prevButton
        text: "Anterior"
        size: 80 0

      Label
        id: pageInfo
        text: "Página 1/1"
        size: 0 0
        text-align: center

      Button
        id: nextButton
        text: "Próximo"
        size: 80 0

VerticalScrollBar
  size: 13 0
  background-color: #2c2c2c
  border-color: #404040

  Button
    id: slider
    size: 13 20
    background-color: #606060
    border-color: #808080

HorizontalScrollBar
  size: 0 13
  background-color: #2c2c2c
  border-color: #404040

  Button
    id: slider
    size: 20 13
    background-color: #606060
    border-color: #808080

ScrollableList < Panel
  layout: verticalBox
  vertical-scrollbar: true

  Panel
    id: content
    size: 0 0
    layout: verticalBox

PaginationControls < Panel
  size: 0 30
  layout: horizontalBox

  Button
    id: firstPage
    text: "Primeira"
    size: 60 0

  Button
    id: prevPage
    text: "Anterior"
    size: 60 0

  Label
    id: pageIndicator
    text: "1/1"
    size: 0 0
    text-align: center

  Button
    id: nextPage
    text: "Próximo"
    size: 60 0

  Button
    id: lastPage
    text: "Última"
    size: 60 0
```

---


---

## 💡 Exemplos Práticos 💡

### 🎯 **Exemplo 1: Lista com Scroll Simples** 🎮

```lua
local SimpleScrollList = {}

function SimpleScrollList.create(parent, items)
    -- Função: SimpleScrollList
    -- Container principal
    --  Container principal (traduzido)
    local container = g_ui.createWidget('Panel', parent)
    container:setSize({width = 300, height = 200})
    
    -- Área de scroll
    --  Área de scroll (traduzido)
    local scrollArea = ScrollPaginationSystem.createScrollArea(container, {
        size = {width = 300, height = 200},
        verticalScroll = true
    })
    
    -- Adicionar itens
    --  Adicionar itens (traduzido)
    for i, itemText in ipairs(items) do
    -- Loop de repetição
        local item = g_ui.createWidget('Label', scrollArea)
        item:setText(itemText)
        item:setPosition({x = 10, y = (i - 1) * 25})
        item:setSize({width = 280, height = 20})
    end
    
    return container
end

-- Uso
    --  Uso (traduzido)
local items = {"Item 1", "Item 2", "Item 3", "Item 4", "Item 5"}
local list = SimpleScrollList.create(parent, items)
```

### 🎨 **Exemplo 2: Sistema de Paginação Avançado** 🎮

#### Inicialização e Configuração
```lua
local AdvancedPaginationSystem = {}

function AdvancedPaginationSystem.create(parent, data, itemsPerPage)
    local pagination = {
        currentPage = 1,
        totalPages = math.ceil(#data / itemsPerPage),
        itemsPerPage = itemsPerPage,
        totalItems = #data,
        data = data
    }
    
    -- Container principal
    local container = g_ui.createWidget('Panel', parent)
    container:setSize({width = 600, height = 400})
    
    -- Área de conteúdo
    local contentArea = ScrollPaginationSystem.createScrollArea(container, {
        size = {width = 600, height = 350},
        verticalScroll = true
    })
    
    -- Controles de paginação
    local paginationPanel = g_ui.createWidget('Panel', container)
    paginationPanel:setPosition({x = 0, y = 360})
    paginationPanel:setSize({width = 600, height = 40})
    
    -- Botões de navegação
    local firstButton = g_ui.createWidget('Button', paginationPanel)
    firstButton:setText('Primeira')
    firstButton:setPosition({x = 10, y = 10})
    firstButton:setSize({width = 60, height = 20})
    
    local prevButton = g_ui.createWidget('Button', paginationPanel)
    prevButton:setText('Anterior')
    prevButton:setPosition({x = 80, y = 10})
    prevButton:setSize({width = 60, height = 20})
    
    local nextButton = g_ui.createWidget('Button', paginationPanel)
    nextButton:setText('Próximo')
    nextButton:setPosition({x = 450, y = 10})
    nextButton:setSize({width = 60, height = 20})
    
    local lastButton = g_ui.createWidget('Button', paginationPanel)
    lastButton:setText('Última')
    lastButton:setPosition({x = 520, y = 10})
    lastButton:setSize({width = 60, height = 20})
    
    -- Indicador de página
    local pageLabel = g_ui.createWidget('Label', paginationPanel)
    pageLabel:setPosition({x = 250, y = 10})
    pageLabel:setSize({width = 100, height = 20})
    pageLabel:setTextAlign(AlignCenter)
    
    -- Função para atualizar conteúdo
    local function updateContent()
        contentArea:clearChildren()
        
        local startIndex = (pagination.currentPage - 1) * pagination.itemsPerPage + 1
        local endIndex = math.min(startIndex + pagination.itemsPerPage - 1, pagination.totalItems)
        
        for i = startIndex, endIndex do
            local item = g_ui.createWidget('Label', contentArea)
            item:setText(pagination.data[i])
            item:setPosition({x = 10, y = (i - startIndex) * 30})
            item:setSize({width = 580, height = 25})
        end
```

#### Funcionalidade 1
```lua
        
        contentArea:updateScrollBars()
    end
    
    -- Função para atualizar controles
    local function updateControls()
        pageLabel:setText(pagination.currentPage .. '/' .. pagination.totalPages)
        
        firstButton:setEnabled(pagination.currentPage > 1)
        prevButton:setEnabled(pagination.currentPage > 1)
        nextButton:setEnabled(pagination.currentPage < pagination.totalPages)
        lastButton:setEnabled(pagination.currentPage < pagination.totalPages)
    end
    
    -- Eventos dos botões
    firstButton.onClick = function()
        pagination.currentPage = 1
        updateContent()
        updateControls()
    end
    
    prevButton.onClick = function()
        if pagination.currentPage > 1 then
            pagination.currentPage = pagination.currentPage - 1
            updateContent()
            updateControls()
        end
```

#### Funcionalidade 2
```lua
    end
    
    nextButton.onClick = function()
        if pagination.currentPage < pagination.totalPages then
            pagination.currentPage = pagination.currentPage + 1
            updateContent()
            updateControls()
        end
    end
    
    lastButton.onClick = function()
        pagination.currentPage = pagination.totalPages
        updateContent()
        updateControls()
    end
    
    -- Inicializar
    updateContent()
    updateControls()
    
    return container, pagination
end
```

#### Finalização
```lua

-- Uso
local data = {}
for i = 1, 100 do
    table.insert(data, "Item de dados " .. i)
end

local container, pagination = AdvancedPaginationSystem.create(parent, data, 10)
```

### 🪟 **Exemplo 3: Scroll Infinito** 🎮

#### Inicialização e Configuração
```lua
local InfiniteScrollSystem = {}

function InfiniteScrollSystem.create(parent, dataLoader)
    local system = {
        currentItems = {},
        isLoading = false,
        hasMore = true,
        dataLoader = dataLoader,
        pageSize = 20
    }
    
    -- Container principal
    local container = g_ui.createWidget('Panel', parent)
    container:setSize({width = 400, height = 300})
    
    -- Área de scroll
    local scrollArea = ScrollPaginationSystem.createScrollArea(container, {
        size = {width = 400, height = 300},
        verticalScroll = true
    })
    
    -- Função para carregar mais dados
    local function loadMoreData()
        if system.isLoading or not system.hasMore then
            return
        end
```

#### Funcionalidade 1
```lua
        
        system.isLoading = true
        
        -- Simular carregamento assíncrono
        scheduleEvent(function()
            local newData = system.dataLoader(system.pageSize)
            
            if newData and #newData > 0 then
                -- Adicionar novos itens
                for _, item in ipairs(newData) do
                    table.insert(system.currentItems, item)
                    
                    local itemWidget = g_ui.createWidget('Label', scrollArea)
                    itemWidget:setText(item)
                    itemWidget:setPosition({x = 10, y = (#system.currentItems - 1) * 25})
                    itemWidget:setSize({width = 380, height = 20})
                end
                
                scrollArea:updateScrollBars()
            else
                system.hasMore = false
            end
```

#### Funcionalidade 2
```lua
            
            system.isLoading = false
        end, 100)
    end
    
    -- Evento de scroll para detectar quando chegar ao final
    local scrollBar = scrollArea:getVerticalScrollBar()
    scrollBar.onValueChange = function(widget, value)
        local maxValue = widget:getMaximum()
        
        -- Se chegou ao final, carregar mais dados
        if value >= maxValue - 10 and not system.isLoading and system.hasMore then
            loadMoreData()
        end
    end
    
    -- Carregar dados iniciais
    loadMoreData()
    
    return container, system
end
```

#### Finalização
```lua

-- Exemplo de uso
local function sampleDataLoader(pageSize)
    local data = {}
    for i = 1, pageSize do
        table.insert(data, "Item carregado " .. i)
    end
    return data
end

local container, infiniteScroll = InfiniteScrollSystem.create(parent, sampleDataLoader)
```

---


---

## ✅ Melhores Práticas 📋

### 🎯 **Uso Eficiente** 📝

#### Inicialização e Configuração
```lua
-- ✅ BOM: Sempre configurar valores mínimos e máximos
function createProperScrollBar(parent)
    local scrollBar = g_ui.createWidget('VerticalScrollBar', parent)
    scrollBar:setMinimum(0)
    scrollBar:setMaximum(100)
    scrollBar:setValue(0)
    return scrollBar
end

-- ✅ BOM: Usar UIScrollArea para conteúdo extenso
function createScrollableContent(parent, items)
    local scrollArea = g_ui.createWidget('UIScrollArea', parent)
    scrollArea:setVerticalScrollBar(createProperScrollBar(scrollArea))
    
    for i, item in ipairs(items) do
        local widget = g_ui.createWidget('Label', scrollArea)
        widget:setText(item)
        widget:setPosition({x = 10, y = (i - 1) * 25})
    end
    
    scrollArea:updateScrollBars()
    return scrollArea
end
```

#### Funcionalidade 1
```lua

-- ✅ BOM: Implementar paginação para grandes datasets
function createPaginatedList(parent, data, itemsPerPage)
    local pagination = {
        currentPage = 1,
        totalPages = math.ceil(#data / itemsPerPage),
        itemsPerPage = itemsPerPage,
        data = data
    }
    
    local container = g_ui.createWidget('Panel', parent)
    local contentArea = createScrollableContent(container, {})
    
    local function updatePage()
        contentArea:clearChildren()
        
        local startIndex = (pagination.currentPage - 1) * pagination.itemsPerPage + 1
        local endIndex = math.min(startIndex + pagination.itemsPerPage - 1, #data)
        
        local pageData = {}
        for i = startIndex, endIndex do
            table.insert(pageData, data[i])
        end
```

#### Funcionalidade 2
```lua
        
        createScrollableContent(contentArea, pageData)
    end
    
    updatePage()
    return container, pagination
end

-- ❌ EVITE: Não configurar limites do scrollbar
function badScrollBar(parent)
    local scrollBar = g_ui.createWidget('VerticalScrollBar', parent)
    -- Falta configuração de minimum/maximum
    return scrollBar
end

-- ❌ EVITE: Não atualizar scrollbars após mudanças
function badContentUpdate(scrollArea, items)
    scrollArea:clearChildren()
    
    for i, item in ipairs(items) do
        local widget = g_ui.createWidget('Label', scrollArea)
        widget:setText(item)
    end
```

#### Finalização
```lua
    -- Falta updateScrollBars()
end
```

### 🎨 **Organização de Código** 📝

#### Inicialização e Configuração
```lua
-- ✅ BOM: Separar responsabilidades
local ScrollManager = {
    scrollAreas = {},
    paginationSystems = {}
}

function ScrollManager:createScrollArea(parent, options)
    local scrollArea = g_ui.createWidget('UIScrollArea', parent)
    
    if options.verticalScroll then
        local verticalBar = self:createVerticalScrollBar(scrollArea)
        scrollArea:setVerticalScrollBar(verticalBar)
    end
    
    if options.horizontalScroll then
        local horizontalBar = self:createHorizontalScrollBar(scrollArea)
        scrollArea:setHorizontalScrollBar(horizontalBar)
    end
    
    table.insert(self.scrollAreas, scrollArea)
    return scrollArea
end
```

#### Funcionalidade 1
```lua

function ScrollManager:createVerticalScrollBar(parent)
    local scrollBar = g_ui.createWidget('VerticalScrollBar', parent)
    scrollBar:setMinimum(0)
    scrollBar:setMaximum(100)
    scrollBar:setValue(0)
    scrollBar:setMouseScroll(true)
    return scrollBar
end

function ScrollManager:createHorizontalScrollBar(parent)
    local scrollBar = g_ui.createWidget('HorizontalScrollBar', parent)
    scrollBar:setMinimum(0)
    scrollBar:setMaximum(100)
    scrollBar:setValue(0)
    scrollBar:setMouseScroll(true)
    return scrollBar
end

-- ✅ BOM: Sistema de eventos para paginação
local PaginationEventSystem = {
    listeners = {}
}
```

#### Finalização
```lua

function PaginationEventSystem:addEventListener(event, callback)
    if not self.listeners[event] then
        self.listeners[event] = {}
    end
    
    table.insert(self.listeners[event], callback)
end

function PaginationEventSystem:triggerEvent(event, data)
    if self.listeners[event] then
        for _, callback in ipairs(self.listeners[event]) do
            callback(data)
        end
    end
end

-- Uso
PaginationEventSystem:addEventListener('pageChange', function(pageData)
    print("Página mudou para: " .. pageData.page)
end)
```

### 🔧 **Performance e Otimização** 📝

#### Inicialização e Configuração
```lua
-- ✅ BOM: Virtualização para listas grandes
local VirtualizedList = {}

function VirtualizedList.create(parent, totalItems, itemHeight, visibleHeight)
    local visibleCount = math.ceil(visibleHeight / itemHeight)
    local scrollArea = ScrollPaginationSystem.createScrollArea(parent, {
        verticalScroll = true
    })
    
    local virtualItems = {}
    local visibleItems = {}
    
    -- Criar apenas itens visíveis
    for i = 1, visibleCount do
        local item = g_ui.createWidget('Label', scrollArea)
        item:setSize({width = 0, height = itemHeight})
        table.insert(visibleItems, item)
    end
    
    local function updateVisibleItems(scrollValue)
        local startIndex = math.floor(scrollValue / itemHeight) + 1
        local endIndex = math.min(startIndex + visibleCount - 1, totalItems)
        
        for i, item in ipairs(visibleItems) do
            local itemIndex = startIndex + i - 1
            if itemIndex <= totalItems then
                item:setText("Item " .. itemIndex)
                item:setPosition({x = 10, y = (i - 1) * itemHeight})
                item:setVisible(true)
            else
                item:setVisible(false)
            end
```

#### Funcionalidade 1
```lua
        end
    end
    
    -- Configurar scrollbar
    local scrollBar = scrollArea:getVerticalScrollBar()
    scrollBar:setMaximum(totalItems * itemHeight - visibleHeight)
    scrollBar.onValueChange = function(widget, value)
        updateVisibleItems(value)
    end
    
    return scrollArea
end

-- ✅ BOM: Debounce para eventos de scroll
local scrollDebounce = nil

function debouncedScrollHandler(scrollValue)
    if scrollDebounce then
        removeEvent(scrollDebounce)
    end
    
    scrollDebounce = scheduleEvent(function()
        -- Processar scroll
        processScrollUpdate(scrollValue)
        scrollDebounce = nil
    end, 16)  -- ~60fps
```

#### Funcionalidade 2
```lua
end

-- ✅ BOM: Pool de widgets para paginação
local WidgetPool = {
    available = {},
    inUse = {}
}

function WidgetPool:getWidget()
    if #self.available > 0 then
        local widget = table.remove(self.available)
        table.insert(self.inUse, widget)
        return widget
    end
    
    local widget = g_ui.createWidget('Label')
    table.insert(self.inUse, widget)
    return widget
end

function WidgetPool:returnWidget(widget)
```

#### Finalização
```lua
    widget:hide()
    widget:setText("")
    
    table.removevalue(self.inUse, widget)
    table.insert(self.available, widget)
end

function WidgetPool:clear()
    for _, widget in ipairs(self.inUse) do
        widget:destroy()
    end
    
    for _, widget in ipairs(self.available) do
        widget:destroy()
    end
    
    self.inUse = {}
    self.available = {}
end
```

### 🎨 **Estilização e Temas** 📝

#### Inicialização e Configuração
```lua
-- ✅ BOM: Sistema de temas para scroll
local scrollThemes = {
    default = {
        backgroundColor = '#2c2c2c',
        sliderColor = '#606060',
        borderColor = '#404040',
        hoverColor = '#808080'
    },
    
    light = {
        backgroundColor = '#f5f5f5',
        sliderColor = '#cccccc',
        borderColor = '#dddddd',
        hoverColor = '#bbbbbb'
    },
    
    dark = {
        backgroundColor = '#1a1a1a',
        sliderColor = '#404040',
        borderColor = '#2a2a2a',
        hoverColor = '#505050'
    }
```

#### Funcionalidade 1
```lua
}

function applyScrollTheme(scrollBar, themeName)
    local theme = scrollThemes[themeName] or scrollThemes.default
    
    scrollBar:setBackgroundColor(theme.backgroundColor)
    scrollBar:setBorderColor(theme.borderColor)
    
    local slider = scrollBar:getChildById('slider')
    if slider then
        slider:setBackgroundColor(theme.sliderColor)
        slider:setBorderColor(theme.borderColor)
    end
end

-- ✅ BOM: Animações suaves
function createSmoothScrollArea(parent)
    local scrollArea = ScrollPaginationSystem.createScrollArea(parent, {
        verticalScroll = true
    })
    
    local scrollBar = scrollArea:getVerticalScrollBar()
    local lastValue = scrollBar:getValue()
    
    scrollBar.onValueChange = function(widget, value)
        local delta = value - lastValue
        
        -- Animação suave
        local animation = scrollArea:createAnimation()
        animation:setDuration(150)
        animation:setProperty('virtualOffset', {
            x = scrollArea:getVirtualOffset().x,
            y = scrollArea:getVirtualOffset().y + delta
        })
```

#### Funcionalidade 2
```lua
        animation:start()
        
        lastValue = value
    end
    
    return scrollArea
end

-- ✅ BOM: Indicadores visuais de carregamento
function createLoadingIndicator(parent)
    local indicator = g_ui.createWidget('Panel', parent)
    indicator:setSize({width = 100, height = 20})
    
    local label = g_ui.createWidget('Label', indicator)
    label:setText('Carregando...')
    label:setTextAlign(AlignCenter)
    label:setSize({width = 100, height = 20})
    
    -- Animação de pontos
    local dots = 0
    local animationEvent = periodicalEvent(function()
        dots = (dots + 1) % 4
        local text = 'Carregando'
        for i = 1, dots do
            text = text .. '.'
        end
```

#### Finalização
```lua
        label:setText(text)
    end, 500)
    
    return indicator, animationEvent
end
```

O sistema de scroll e paginação oferece ferramentas poderosas para navegação em conteúdo extenso no OTClient. Seguindo as melhores práticas e utilizando os exemplos fornecidos, você pode criar interfaces eficientes e responsivas que melhoram significativamente a experiência do usuário.

---

> [!success] **Navegação**
> **📚 Documentos Relacionados:**
> - [[UI_System_Guide]] - Sistema de interface básico
> - [[UI_Tabs_System_Guide]] - Sistema de tabs e abas
> - [[UI_Modals_System_Guide]] - Sistema de modais e diálogos
> - [[Game_Trading_System_Guide]] - Sistema de trade e economia
> 
> **🔗 Navegação Rápida:**
> - [[Wiki_Index]] - Voltar ao índice
> - [[Cheat_Sheet]] - Referência rápida
> - [[Getting_Started_Guide]] - Comece aqui 