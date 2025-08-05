# Widgets Especializados - OTClient Redemption

Documentação completa dos widgets especializados do OTClient, incluindo minimap, containers, market, tabs e outros componentes avançados da interface.

## 📋 Índice

1. [Minimap Widget](#-minimap-widget)
2. [Container System](#-container-system)
3. [Tab System](#-tab-system)
4. [Market Widgets](#-market-widgets)
5. [Progress Widgets](#-progress-widgets)
6. [Scroll Widgets](#-scroll-widgets)
7. [Split Widgets](#-split-widgets)
8. [Tree Widgets](#-tree-widgets)
9. [Calendar Widgets](#-calendar-widgets)
10. [Exemplos Práticos](#-exemplos-práticos)

## 🗺️ Minimap Widget

### Minimap

**Descrição**: Widget para exibição do minimapa do jogo.

#### Nível Basic
```lua
-- Criar minimap
local minimap = g_ui.createWidget('Minimap', parent)

-- Configurações básicas
minimap:setZoom(2)                       -- Define zoom (1-5)
local zoom = minimap:getZoom()           -- Obtém zoom atual
minimap:setPosition({x = 1000, y = 1000, z = 7}) -- Define posição central

-- Navegação
minimap:setCameraPosition({x = 1000, y = 1000, z = 7}) -- Posição da câmera
local cameraPos = minimap:getCameraPosition() -- Obtém posição da câmera
minimap:followCreature(creature)         -- Segue criatura
minimap:setCrosshair(true)               -- Exibe crosshair central

-- Floors/Andares
minimap:setFloor(7)                      -- Define andar
local floor = minimap:getFloor()         -- Obtém andar atual
minimap:floorUp()                        -- Sobe um andar
minimap:floorDown()                      -- Desce um andar

-- Modo tela cheia
minimap:setFullscreen(true)              -- Modo tela cheia
local fullscreen = minimap:isFullscreen() -- Verifica se em tela cheia

-- Flags e marcadores
minimap:addFlag({x = 1000, y = 1000, z = 7}, 255, "Minha Casa") -- Adiciona flag
minimap:removeFlag({x = 1000, y = 1000, z = 7}) -- Remove flag

-- Eventos
minimap.onPositionChange = function(minimap, position, mousePos)
    print("Clicou na posição:", position.x, position.y, position.z)
end

minimap.onMousePress = function(minimap, mousePos, button)
    if button == MouseRightButton then
        -- Menu de contexto
        local position = minimap:getPosition(mousePos)
        print("Clique direito em:", position.x, position.y, position.z)
    end
end
```

#### Nível Intermediate
```lua
-- Criar minimap
local minimap = g_ui.createWidget('Minimap', parent)

-- Configurações básicas
minimap:setZoom(2)                       -- Define zoom (1-5)
local zoom = minimap:getZoom()           -- Obtém zoom atual
minimap:setPosition({x = 1000, y = 1000, z = 7}) -- Define posição central

-- Navegação
minimap:setCameraPosition({x = 1000, y = 1000, z = 7}) -- Posição da câmera
local cameraPos = minimap:getCameraPosition() -- Obtém posição da câmera
minimap:followCreature(creature)         -- Segue criatura
minimap:setCrosshair(true)               -- Exibe crosshair central

-- Floors/Andares
minimap:setFloor(7)                      -- Define andar
local floor = minimap:getFloor()         -- Obtém andar atual
minimap:floorUp()                        -- Sobe um andar
minimap:floorDown()                      -- Desce um andar

-- Modo tela cheia
minimap:setFullscreen(true)              -- Modo tela cheia
local fullscreen = minimap:isFullscreen() -- Verifica se em tela cheia

-- Flags e marcadores
minimap:addFlag({x = 1000, y = 1000, z = 7}, 255, "Minha Casa") -- Adiciona flag
minimap:removeFlag({x = 1000, y = 1000, z = 7}) -- Remove flag

-- Eventos
minimap.onPositionChange = function(minimap, position, mousePos)
    print("Clicou na posição:", position.x, position.y, position.z)
end

minimap.onMousePress = function(minimap, mousePos, button)
    if button == MouseRightButton then
        -- Menu de contexto
        local position = minimap:getPosition(mousePos)
        print("Clique direito em:", position.x, position.y, position.z)
    end
end
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
-- Criar minimap
local minimap = g_ui.createWidget('Minimap', parent)

-- Configurações básicas
minimap:setZoom(2)                       -- Define zoom (1-5)
local zoom = minimap:getZoom()           -- Obtém zoom atual
minimap:setPosition({x = 1000, y = 1000, z = 7}) -- Define posição central

-- Navegação
minimap:setCameraPosition({x = 1000, y = 1000, z = 7}) -- Posição da câmera
local cameraPos = minimap:getCameraPosition() -- Obtém posição da câmera
minimap:followCreature(creature)         -- Segue criatura
minimap:setCrosshair(true)               -- Exibe crosshair central

-- Floors/Andares
minimap:setFloor(7)                      -- Define andar
local floor = minimap:getFloor()         -- Obtém andar atual
minimap:floorUp()                        -- Sobe um andar
minimap:floorDown()                      -- Desce um andar

-- Modo tela cheia
minimap:setFullscreen(true)              -- Modo tela cheia
local fullscreen = minimap:isFullscreen() -- Verifica se em tela cheia

-- Flags e marcadores
minimap:addFlag({x = 1000, y = 1000, z = 7}, 255, "Minha Casa") -- Adiciona flag
minimap:removeFlag({x = 1000, y = 1000, z = 7}) -- Remove flag

-- Eventos
minimap.onPositionChange = function(minimap, position, mousePos)
    print("Clicou na posição:", position.x, position.y, position.z)
end

minimap.onMousePress = function(minimap, mousePos, button)
    if button == MouseRightButton then
        -- Menu de contexto
        local position = minimap:getPosition(mousePos)
        print("Clique direito em:", position.x, position.y, position.z)
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

### Interface .otui do Minimap

```otui
MinimapWindow < MainWindow
  id: minimapWindow
  !text: tr('Map')
  size: 250 250

  UIWidget
    id: minimapBorder
    anchors.fill: parent
    margin: 10
    image-source: /images/ui/1pixel_down_frame

    Minimap
      id: minimap
      anchors.fill: parent
      margin: 1

  UIWidget
    id: controlPanel
    height: 30
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.bottom: parent.bottom
    margin: 5

    UIButton
      id: zoomInButton
      text: +
      width: 25
      anchors.left: parent.left
      @onClick: |
        local minimap = modules.game_minimap.getMinimap()
        minimap:setZoom(math.min(5, minimap:getZoom() + 1))

    UIButton
      id: zoomOutButton
      text: -
      width: 25
      anchors.left: prev.right
      margin-left: 5
      @onClick: |
        local minimap = modules.game_minimap.getMinimap()
        minimap:setZoom(math.max(1, minimap:getZoom() - 1))

    UIButton
      id: floorUpButton
      text: ↑
      width: 25
      anchors.right: parent.right
      @onClick: |
        local minimap = modules.game_minimap.getMinimap()
        minimap:floorUp()

    UIButton
      id: floorDownButton
      text: ↓
      width: 25
      anchors.right: prev.left
      margin-right: 5
      @onClick: |
        local minimap = modules.game_minimap.getMinimap()
        minimap:floorDown()
```

## 📦 Container System

### Container Widget

**Descrição**: Sistema de containers para itens do jogo.

#### Nível Basic
```lua
-- Criar container
local container = g_ui.createWidget('Container', parent)

-- Configurações
container:setCapacity(20)                -- Define capacidade
local capacity = container:getCapacity() -- Obtém capacidade
container:setName("Backpack")            -- Nome do container
local name = container:getName()         -- Obtém nome

-- Gerenciamento de itens
container:addItem(item, slot)            -- Adiciona item no slot
container:removeItem(slot)               -- Remove item do slot
local item = container:getItem(slot)     -- Obtém item do slot
local items = container:getItems()       -- Lista todos os itens

-- Paginação (para containers grandes)
container:setCurrentPage(1)              -- Define página atual
local page = container:getCurrentPage()  -- Obtém página atual
local maxPages = container:getMaxPages() -- Número máximo de páginas

-- Estados
local hasParent = container:hasParent()  -- Tem container pai
local parent = container:getParentContainer() -- Container pai

-- Eventos
container.onItemAdd = function(container, slot, item)
    print("Item adicionado no slot", slot, ":", item:getId())
end

container.onItemRemove = function(container, slot, item)
    print("Item removido do slot", slot, ":", item:getId())
end

container.onItemUpdate = function(container, slot, item, oldItem)
    print("Item atualizado no slot", slot)
end

container.onOpen = function(container)
    print("Container aberto:", container:getName())
end

container.onClose = function(container)
    print("Container fechado:", container:getName())
end
```

#### Nível Intermediate
```lua
-- Criar container
local container = g_ui.createWidget('Container', parent)

-- Configurações
container:setCapacity(20)                -- Define capacidade
local capacity = container:getCapacity() -- Obtém capacidade
container:setName("Backpack")            -- Nome do container
local name = container:getName()         -- Obtém nome

-- Gerenciamento de itens
container:addItem(item, slot)            -- Adiciona item no slot
container:removeItem(slot)               -- Remove item do slot
local item = container:getItem(slot)     -- Obtém item do slot
local items = container:getItems()       -- Lista todos os itens

-- Paginação (para containers grandes)
container:setCurrentPage(1)              -- Define página atual
local page = container:getCurrentPage()  -- Obtém página atual
local maxPages = container:getMaxPages() -- Número máximo de páginas

-- Estados
local hasParent = container:hasParent()  -- Tem container pai
local parent = container:getParentContainer() -- Container pai

-- Eventos
container.onItemAdd = function(container, slot, item)
    print("Item adicionado no slot", slot, ":", item:getId())
end

container.onItemRemove = function(container, slot, item)
    print("Item removido do slot", slot, ":", item:getId())
end

container.onItemUpdate = function(container, slot, item, oldItem)
    print("Item atualizado no slot", slot)
end

container.onOpen = function(container)
    print("Container aberto:", container:getName())
end

container.onClose = function(container)
    print("Container fechado:", container:getName())
end
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
-- Criar container
local container = g_ui.createWidget('Container', parent)

-- Configurações
container:setCapacity(20)                -- Define capacidade
local capacity = container:getCapacity() -- Obtém capacidade
container:setName("Backpack")            -- Nome do container
local name = container:getName()         -- Obtém nome

-- Gerenciamento de itens
container:addItem(item, slot)            -- Adiciona item no slot
container:removeItem(slot)               -- Remove item do slot
local item = container:getItem(slot)     -- Obtém item do slot
local items = container:getItems()       -- Lista todos os itens

-- Paginação (para containers grandes)
container:setCurrentPage(1)              -- Define página atual
local page = container:getCurrentPage()  -- Obtém página atual
local maxPages = container:getMaxPages() -- Número máximo de páginas

-- Estados
local hasParent = container:hasParent()  -- Tem container pai
local parent = container:getParentContainer() -- Container pai

-- Eventos
container.onItemAdd = function(container, slot, item)
    print("Item adicionado no slot", slot, ":", item:getId())
end

container.onItemRemove = function(container, slot, item)
    print("Item removido do slot", slot, ":", item:getId())
end

container.onItemUpdate = function(container, slot, item, oldItem)
    print("Item atualizado no slot", slot)
end

container.onOpen = function(container)
    print("Container aberto:", container:getName())
end

container.onClose = function(container)
    print("Container fechado:", container:getName())
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

### Interface .otui de Container

```otui
ContainerWindow < MiniWindow
  id: containerWindow
  height: 150

  UIItem
    id: containerIcon
    virtual: true
    size: 16 16
    anchors.top: parent.top
    anchors.left: parent.left
    margin: 4

  UIButton
    id: upButton
    size: 14 14
    anchors.top: containerIcon.top
    anchors.right: minimizeButton.left
    margin-right: 3
    image-source: /images/ui/miniwindow_buttons
    image-clip: 42 0 14 14
    @onClick: Container.navigateUp(self:getParent())

  Panel
    id: pagePanel
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: miniwindowTopBar.bottom
    height: 20
    margin: 2 3 0 3
    background: #00000066
    visible: false

    Label
      id: pageLabel
      anchors.top: parent.top
      anchors.horizontalCenter: parent.horizontalCenter
      margin-top: 2
      text-auto-resize: true

    UIButton
      id: prevPageButton
      text: <
      size: 30 18
      anchors.left: parent.left
      @onClick: Container.previousPage(self:getParent():getParent())

    UIButton
      id: nextPageButton
      text: >
      size: 30 18
      anchors.right: parent.right
      @onClick: Container.nextPage(self:getParent():getParent())

  MiniWindowContents
    id: contentsPanel
    padding-left: 5
    layout:
      type: grid
      cell-size: 34 34
      cell-spacing: 3
      flow: true
```

## 📑 Tab System

### UITabBar e UITab

**Descrição**: Sistema de abas para organizar conteúdo.

#### Nível Basic
```lua
-- Criar tab bar
local tabBar = g_ui.createWidget('UITabBar', parent)

-- Adicionar abas
local tab1 = tabBar:addTab('Aba 1', "Tab 1")
local tab2 = tabBar:addTab('Aba 2', "Tab 2")
local tab3 = tabBar:addTab('Aba 3', "Tab 3")

-- Gerenciar abas
tabBar:selectTab(tab1)                   -- Seleciona aba
local currentTab = tabBar:getCurrentTab() -- Aba atual
tabBar:removeTab(tab2)                   -- Remove aba
tabBar:moveTab(tab1, 2)                  -- Move aba para posição

-- Configurações da aba
tab1:setText("Nova Aba")                 -- Altera texto
tab1:setIcon("/icons/tab1.png")          -- Define ícone
tab1:setCloseable(true)                  -- Permite fechar
tab1:setEnabled(true)                    -- Habilita/desabilita

-- Conteúdo da aba
local content = g_ui.createWidget('UIWidget')
content:setId('tab1Content')
tab1:setContentWidget(content)           -- Define widget de conteúdo

-- Eventos
tabBar.onTabChange = function(tabBar, tab)
    print("Aba alterada para:", tab:getText())
end

tab1.onClose = function(tab)
    print("Aba fechada:", tab:getText())
    return true -- Permite fechar
end

tab1.onClick = function(tab)
    print("Aba clicada:", tab:getText())
end
```

#### Nível Intermediate
```lua
-- Criar tab bar
local tabBar = g_ui.createWidget('UITabBar', parent)

-- Adicionar abas
local tab1 = tabBar:addTab('Aba 1', "Tab 1")
local tab2 = tabBar:addTab('Aba 2', "Tab 2")
local tab3 = tabBar:addTab('Aba 3', "Tab 3")

-- Gerenciar abas
tabBar:selectTab(tab1)                   -- Seleciona aba
local currentTab = tabBar:getCurrentTab() -- Aba atual
tabBar:removeTab(tab2)                   -- Remove aba
tabBar:moveTab(tab1, 2)                  -- Move aba para posição

-- Configurações da aba
tab1:setText("Nova Aba")                 -- Altera texto
tab1:setIcon("/icons/tab1.png")          -- Define ícone
tab1:setCloseable(true)                  -- Permite fechar
tab1:setEnabled(true)                    -- Habilita/desabilita

-- Conteúdo da aba
local content = g_ui.createWidget('UIWidget')
content:setId('tab1Content')
tab1:setContentWidget(content)           -- Define widget de conteúdo

-- Eventos
tabBar.onTabChange = function(tabBar, tab)
    print("Aba alterada para:", tab:getText())
end

tab1.onClose = function(tab)
    print("Aba fechada:", tab:getText())
    return true -- Permite fechar
end

tab1.onClick = function(tab)
    print("Aba clicada:", tab:getText())
end
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
-- Criar tab bar
local tabBar = g_ui.createWidget('UITabBar', parent)

-- Adicionar abas
local tab1 = tabBar:addTab('Aba 1', "Tab 1")
local tab2 = tabBar:addTab('Aba 2', "Tab 2")
local tab3 = tabBar:addTab('Aba 3', "Tab 3")

-- Gerenciar abas
tabBar:selectTab(tab1)                   -- Seleciona aba
local currentTab = tabBar:getCurrentTab() -- Aba atual
tabBar:removeTab(tab2)                   -- Remove aba
tabBar:moveTab(tab1, 2)                  -- Move aba para posição

-- Configurações da aba
tab1:setText("Nova Aba")                 -- Altera texto
tab1:setIcon("/icons/tab1.png")          -- Define ícone
tab1:setCloseable(true)                  -- Permite fechar
tab1:setEnabled(true)                    -- Habilita/desabilita

-- Conteúdo da aba
local content = g_ui.createWidget('UIWidget')
content:setId('tab1Content')
tab1:setContentWidget(content)           -- Define widget de conteúdo

-- Eventos
tabBar.onTabChange = function(tabBar, tab)
    print("Aba alterada para:", tab:getText())
end

tab1.onClose = function(tab)
    print("Aba fechada:", tab:getText())
    return true -- Permite fechar
end

tab1.onClick = function(tab)
    print("Aba clicada:", tab:getText())
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

### Interface .otui com Tabs

```otui
TabbedWindow < MainWindow
  id: tabbedWindow
  !text: tr('Janela com Abas')
  size: 400 300

  UITabBar
    id: tabBar
    height: 25
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: parent.top

  Panel
    id: tabContent
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: tabBar.bottom
    anchors.bottom: parent.bottom
    margin: 5
    border-width: 1
    border-color: #404040

// Conteúdo das abas
UIWidget
  id: tab1Content
  
  UILabel
    !text: tr('Conteúdo da Aba 1')
    anchors.top: parent.top
    anchors.left: parent.left
    margin: 10

  UITextEdit
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: prev.bottom
    margin: 10
    height: 100

UIWidget
  id: tab2Content
  visible: false
  
  UILabel
    !text: tr('Conteúdo da Aba 2')
    anchors.top: parent.top
    anchors.left: parent.left
    margin: 10

  UICheckBox
    !text: tr('Opção 1')
    anchors.left: parent.left
    anchors.top: prev.bottom
    margin: 10

  UICheckBox
    !text: tr('Opção 2')
    anchors.left: parent.left
    anchors.top: prev.bottom
    margin: 10
```

## 💰 Market Widgets

### Market System

**Descrição**: Widgets específicos para o sistema de market.

#### Inicialização e Configuração
```lua
-- Market Principal
local marketWindow = g_ui.displayUI('market')

-- Market Tab Bar (customizado)
local marketTabBar = marketWindow:getChildById('mainTabBar')
marketTabBar:addTab('Browse', 'browse')
marketTabBar:addTab('My Offers', 'myoffers')

-- Market Offers List
local offersList = g_ui.createWidget('UITableView', parent)
offersList:addColumn('Item', 150)
offersList:addColumn('Price', 80)
offersList:addColumn('Amount', 60)
offersList:addColumn('Player', 100)

-- Adicionar oferta
local row = offersList:addRow()
row:setData('item', item)
row:setCell(0, item:getDescription())
row:setCell(1, formatMoney(price))
row:setCell(2, tostring(amount))
row:setCell(3, playerName)

-- Market Search
local searchEdit = g_ui.createWidget('UITextEdit', parent)
searchEdit:setPlaceholder('Search items...')
searchEdit.onTextChange = function(widget, text)
    filterMarketItems(text)
end
```

#### Funcionalidade 1
```lua

-- Market Category Combo
local categoryCombo = g_ui.createWidget('UIComboBox', parent)
categoryCombo:addOption('All Categories', 0)
categoryCombo:addOption('Weapons', 1)
categoryCombo:addOption('Armor', 2)
categoryCombo:addOption('Tools', 3)

-- Market Item Statistics
local statsWidget = g_ui.createWidget('UIWidget', parent)
local priceHistoryChart = g_ui.createWidget('UIChart', statsWidget)
priceHistoryChart:addSeries('Price', '#00FF00')
priceHistoryChart:setData(priceHistory)

-- Events
offersList.onRowSelect = function(tableView, row)
    local item = row:getData('item')
    showItemDetails(item)
end

marketTabBar.onTabChange = function(tabBar, tab)
    local tabName = tab:getData()
    if tabName == 'browse' then
        showBrowseInterface()
    elseif tabName == 'myoffers' then
        showMyOffersInterface()
    end
```

#### Finalização
```lua
end
```

## 📊 Progress Widgets

### UIProgressBar

**Descrição**: Barras de progresso com recursos avançados.

```lua
-- Progress bar básica
local progressBar = g_ui.createWidget('UIProgressBar', parent)
progressBar:setMinimum(0)
progressBar:setMaximum(100)
progressBar:setValue(50)

-- Progress bar com texto
    --  Progress bar com texto (traduzido)
progressBar:setShowText(true)
progressBar:setTextFormat("{value}/{maximum} ({percent}%)")

-- Progress bar animada
    --  Progress bar animada (traduzido)
progressBar:setAnimated(true)
progressBar:setAnimationDuration(500)

-- Cores personalizadas
    --  Cores personalizadas (traduzido)
progressBar:setBackgroundColor('#404040')
progressBar:setForegroundColor('#00AA00')
progressBar:setBorderColor('#FFFFFF')

-- Progress circular
    --  Progress circular (traduzido)
local circularProgress = g_ui.createWidget('UICircularProgress', parent)
circularProgress:setValue(75)
circularProgress:setStartAngle(0)
circularProgress:setSpanAngle(360)
circularProgress:setThickness(10)

-- Multi-progress (várias barras)
local multiProgress = g_ui.createWidget('UIMultiProgress', parent)
multiProgress:addProgress('HP', 80, '#FF0000')
multiProgress:addProgress('MP', 60, '#0000FF')
multiProgress:addProgress('Stamina', 45, '#00FF00')

-- Eventos
    --  Eventos (traduzido)
progressBar.onValueChange = function(progressBar, value, oldValue)
    print("Progresso alterado:", value)
    
    -- Cor baseada no valor
    --  Cor baseada no valor (traduzido)
    if value < 30 then
    -- Verificação condicional
        progressBar:setForegroundColor('#FF0000') -- Vermelho
    elseif value < 70 then
        progressBar:setForegroundColor('#FFAA00') -- Laranja
    else
        progressBar:setForegroundColor('#00AA00') -- Verde
    end
end
```

### Interface .otui de Progress

```otui
ProgressWindow < MainWindow
  !text: tr('Progress Example')
  size: 300 200

  UILabel
    id: healthLabel
    !text: tr('Health:')
    anchors.top: parent.top
    anchors.left: parent.left
    margin: 10

  UIProgressBar
    id: healthBar
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: prev.bottom
    height: 20
    margin: 10 10 5 10
    background-color: #404040
    foreground-color: #FF0000
    minimum: 0
    maximum: 100
    value: 80
    show-text: true
    text-format: {value}/{maximum}

  UILabel
    id: manaLabel
    !text: tr('Mana:')
    anchors.top: healthBar.bottom
    anchors.left: parent.left
    margin: 10 10 5 10

  UIProgressBar
    id: manaBar
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: prev.bottom
    height: 20
    margin: 10 10 5 10
    background-color: #404040
    foreground-color: #0066FF
    minimum: 0
    maximum: 100
    value: 60
    show-text: true

  UICircularProgress
    id: experienceCircle
    anchors.horizontalCenter: parent.horizontalCenter
    anchors.bottom: parent.bottom
    margin-bottom: 20
    size: 60 60
    value: 75
    start-angle: -90
    span-angle: 360
    thickness: 8
    foreground-color: #FFAA00
    background-color: #404040
```

## 📜 Scroll Widgets

### UIScrollArea

**Descrição**: Áreas com scroll personalizado.

#### Nível Basic
```lua
-- Scroll area básica
local scrollArea = g_ui.createWidget('UIScrollArea', parent)
-- Scroll bars
local vScrollBar = g_ui.createWidget('UIScrollBar', scrollArea)
local hScrollBar = g_ui.createWidget('UIScrollBar', scrollArea)
-- Configurações
-- Scroll suave
-- Conteúdo
local content = g_ui.createWidget('UIWidget', scrollArea)
    local item = g_ui.createWidget('UILabel', content)
    if i == 1 then
    end
end
-- Eventos
scrollArea.onScroll = function(scrollArea, offset)
    print("Scroll offset:", offset.x, offset.y)
end
vScrollBar.onValueChange = function(scrollBar, value)
    print("Scroll vertical:", value)
end
```

#### Nível Intermediate
```lua
-- Scroll area básica
local scrollArea = g_ui.createWidget('UIScrollArea', parent)

-- Scroll bars
local vScrollBar = g_ui.createWidget('UIScrollBar', scrollArea)
vScrollBar:setOrientation('vertical')
scrollArea:setVerticalScrollBar(vScrollBar)

local hScrollBar = g_ui.createWidget('UIScrollBar', scrollArea)
hScrollBar:setOrientation('horizontal')
scrollArea:setHorizontalScrollBar(hScrollBar)

-- Configurações
scrollArea:setScrollStep(10)             -- Passo do scroll
scrollArea:setAutoScrollEnabled(true)    -- Auto-scroll automático
scrollArea:scrollToTop()                 -- Scroll para o topo
scrollArea:scrollToBottom()              -- Scroll para baixo

-- Scroll suave
scrollArea:setSmoothScrolling(true)
scrollArea:setScrollAnimationDuration(300)

-- Conteúdo
local content = g_ui.createWidget('UIWidget', scrollArea)
content:setHeight(1000) -- Altura maior que o scroll area
for i = 1, 50 do
    local item = g_ui.createWidget('UILabel', content)
    item:setText('Item ' .. i)
    item:setHeight(20)
    if i == 1 then
        item:addAnchor(AnchorTop, 'parent', AnchorTop)
    else
        item:addAnchor(AnchorTop, 'prev', AnchorBottom)
    end
    item:addAnchor(AnchorLeft, 'parent', AnchorLeft)
    item:addAnchor(AnchorRight, 'parent', AnchorRight)
end

-- Eventos
scrollArea.onScroll = function(scrollArea, offset)
    print("Scroll offset:", offset.x, offset.y)
end

vScrollBar.onValueChange = function(scrollBar, value)
    print("Scroll vertical:", value)
end
```

#### Nível Advanced
```lua
-- Scroll area básica
local scrollArea = g_ui.createWidget('UIScrollArea', parent)

-- Scroll bars
local vScrollBar = g_ui.createWidget('UIScrollBar', scrollArea)
vScrollBar:setOrientation('vertical')
scrollArea:setVerticalScrollBar(vScrollBar)

local hScrollBar = g_ui.createWidget('UIScrollBar', scrollArea)
hScrollBar:setOrientation('horizontal')
scrollArea:setHorizontalScrollBar(hScrollBar)

-- Configurações
scrollArea:setScrollStep(10)             -- Passo do scroll
scrollArea:setAutoScrollEnabled(true)    -- Auto-scroll automático
scrollArea:scrollToTop()                 -- Scroll para o topo
scrollArea:scrollToBottom()              -- Scroll para baixo

-- Scroll suave
scrollArea:setSmoothScrolling(true)
scrollArea:setScrollAnimationDuration(300)

-- Conteúdo
local content = g_ui.createWidget('UIWidget', scrollArea)
content:setHeight(1000) -- Altura maior que o scroll area
for i = 1, 50 do
    local item = g_ui.createWidget('UILabel', content)
    item:setText('Item ' .. i)
    item:setHeight(20)
    if i == 1 then
        item:addAnchor(AnchorTop, 'parent', AnchorTop)
    else
        item:addAnchor(AnchorTop, 'prev', AnchorBottom)
    end
    item:addAnchor(AnchorLeft, 'parent', AnchorLeft)
    item:addAnchor(AnchorRight, 'parent', AnchorRight)
end

-- Eventos
scrollArea.onScroll = function(scrollArea, offset)
    print("Scroll offset:", offset.x, offset.y)
end

vScrollBar.onValueChange = function(scrollBar, value)
    print("Scroll vertical:", value)
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

## ✂️ Split Widgets

### UISplitter

**Descrição**: Divisores redimensionáveis.

#### Nível Basic
```lua
-- Splitter horizontal
local hSplitter = g_ui.createWidget('UISplitter', parent)
hSplitter:setOrientation('horizontal')
hSplitter:setSplitRatio(0.5) -- 50% para cada lado

-- Painéis do splitter
local leftPanel = g_ui.createWidget('UIWidget')
local rightPanel = g_ui.createWidget('UIWidget')
hSplitter:setLeftWidget(leftPanel)
hSplitter:setRightWidget(rightPanel)

-- Splitter vertical
local vSplitter = g_ui.createWidget('UISplitter', parent)
vSplitter:setOrientation('vertical')
vSplitter:setSplitRatio(0.3) -- 30% superior, 70% inferior

-- Configurações
hSplitter:setMinimumSizes(100, 100)      -- Tamanhos mínimos
hSplitter:setResizable(true)             -- Permite redimensionar
hSplitter:setSplitterWidth(5)            -- Largura do divisor

-- Splitter aninhado
local nestedSplitter = g_ui.createWidget('UISplitter', rightPanel)
nestedSplitter:setOrientation('vertical')

-- Eventos
hSplitter.onSplitRatioChange = function(splitter, ratio)
    print("Split ratio alterado:", ratio)
    g_settings.set('window.splitRatio', ratio)
end
```

#### Nível Intermediate
```lua
-- Splitter horizontal
local hSplitter = g_ui.createWidget('UISplitter', parent)
hSplitter:setOrientation('horizontal')
hSplitter:setSplitRatio(0.5) -- 50% para cada lado

-- Painéis do splitter
local leftPanel = g_ui.createWidget('UIWidget')
local rightPanel = g_ui.createWidget('UIWidget')
hSplitter:setLeftWidget(leftPanel)
hSplitter:setRightWidget(rightPanel)

-- Splitter vertical
local vSplitter = g_ui.createWidget('UISplitter', parent)
vSplitter:setOrientation('vertical')
vSplitter:setSplitRatio(0.3) -- 30% superior, 70% inferior

-- Configurações
hSplitter:setMinimumSizes(100, 100)      -- Tamanhos mínimos
hSplitter:setResizable(true)             -- Permite redimensionar
hSplitter:setSplitterWidth(5)            -- Largura do divisor

-- Splitter aninhado
local nestedSplitter = g_ui.createWidget('UISplitter', rightPanel)
nestedSplitter:setOrientation('vertical')

-- Eventos
hSplitter.onSplitRatioChange = function(splitter, ratio)
    print("Split ratio alterado:", ratio)
    g_settings.set('window.splitRatio', ratio)
end
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
-- Splitter horizontal
local hSplitter = g_ui.createWidget('UISplitter', parent)
hSplitter:setOrientation('horizontal')
hSplitter:setSplitRatio(0.5) -- 50% para cada lado

-- Painéis do splitter
local leftPanel = g_ui.createWidget('UIWidget')
local rightPanel = g_ui.createWidget('UIWidget')
hSplitter:setLeftWidget(leftPanel)
hSplitter:setRightWidget(rightPanel)

-- Splitter vertical
local vSplitter = g_ui.createWidget('UISplitter', parent)
vSplitter:setOrientation('vertical')
vSplitter:setSplitRatio(0.3) -- 30% superior, 70% inferior

-- Configurações
hSplitter:setMinimumSizes(100, 100)      -- Tamanhos mínimos
hSplitter:setResizable(true)             -- Permite redimensionar
hSplitter:setSplitterWidth(5)            -- Largura do divisor

-- Splitter aninhado
local nestedSplitter = g_ui.createWidget('UISplitter', rightPanel)
nestedSplitter:setOrientation('vertical')

-- Eventos
hSplitter.onSplitRatioChange = function(splitter, ratio)
    print("Split ratio alterado:", ratio)
    g_settings.set('window.splitRatio', ratio)
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

### Interface .otui com Splitters

```otui
SplitterWindow < MainWindow
  !text: tr('Splitter Example')
  size: 600 400

  UISplitter
    id: mainSplitter
    anchors.fill: parent
    margin: 10
    orientation: horizontal
    split-ratio: 0.3

    // Painel esquerdo
    UIWidget
      id: leftPanel
      background-color: #2A2A2A

      UILabel
        !text: tr('Painel Esquerdo')
        anchors.top: parent.top
        anchors.horizontalCenter: parent.horizontalCenter
        margin-top: 10

      UIListWidget
        id: itemList
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: prev.bottom
        anchors.bottom: parent.bottom
        margin: 10

    // Painel direito
    UIWidget
      id: rightPanel
      background-color: #353535

      UISplitter
        id: rightSplitter
        anchors.fill: parent
        orientation: vertical
        split-ratio: 0.7

        // Painel superior direito
        UIWidget
          id: topRightPanel
          background-color: #404040

          UILabel
            !text: tr('Conteúdo Principal')
            anchors.top: parent.top
            anchors.horizontalCenter: parent.horizontalCenter
            margin-top: 10

        // Painel inferior direito
        UIWidget
          id: bottomRightPanel
          background-color: #2A2A2A

          UILabel
            !text: tr('Propriedades')
            anchors.top: parent.top
            anchors.horizontalCenter: parent.horizontalCenter
            margin-top: 10
```

## 🌳 Tree Widgets

### UITreeView

**Descrição**: Visualização em árvore hierárquica.

#### Inicialização e Configuração
```lua
-- Tree view
local treeView = g_ui.createWidget('UITreeView', parent)

-- Adicionar nós raiz
local rootNode = treeView:addNode('Root')
rootNode:setIcon('/icons/folder.png')
rootNode:setExpanded(true)

-- Adicionar nós filhos
local childNode1 = rootNode:addChild('Child 1')
childNode1:setIcon('/icons/file.png')
childNode1:setData('type', 'file')

local childNode2 = rootNode:addChild('Child 2')
childNode2:setIcon('/icons/folder.png')

-- Sub-nós
local subChild = childNode2:addChild('Sub Child')
subChild:setIcon('/icons/file.png')

-- Configurações
treeView:setShowRootNode(true)           -- Mostra nó raiz
treeView:setExpandOnDoubleClick(true)    -- Expande no duplo clique
treeView:setMultiSelection(false)        -- Seleção múltipla

-- Operações no nó
rootNode:expand()                        -- Expande nó
rootNode:collapse()                      -- Colapsa nó
rootNode:remove()                        -- Remove nó
local expanded = rootNode:isExpanded()   -- Verifica se expandido
local selected = rootNode:isSelected()   -- Verifica se selecionado

-- Navegação
local parent = childNode1:getParent()    -- Nó pai
local children = rootNode:getChildren()  -- Nós filhos
local siblings = childNode1:getSiblings() -- Nós irmãos

-- Eventos
treeView.onNodeSelect = function(treeView, node)
    print("Nó selecionado:", node:getText())
    local data = node:getData('type')
    if data == 'file' then
        openFile(node:getText())
    end
```

#### Finalização
```lua
end

treeView.onNodeExpand = function(treeView, node)
    print("Nó expandido:", node:getText())
    -- Carregar filhos dinamicamente
    loadChildNodes(node)
end

treeView.onNodeDoubleClick = function(treeView, node)
    if node:getData('type') == 'file' then
        editFile(node:getText())
    end
end
```

## 📅 Calendar Widgets

### UICalendar

**Descrição**: Widget de calendário.

#### Nível Basic
```lua
-- Calendar
local calendar = g_ui.createWidget('UICalendar', parent)
-- Data atual
local today = os.date('*t')
calendar:setDate(today.year, today.month, today.day)
-- Configurações
calendar:setMinDate(2020, 1, 1)          -- Data mínima
calendar:setMaxDate(2030, 12, 31)        -- Data máxima
calendar:setFirstDayOfWeek(1)            -- Segunda-feira como primeiro dia
-- Eventos especiais
calendar:addEvent(2025, 1, 15, 'Aniversário', '#FF0000')
calendar:addEvent(2025, 1, 25, 'Reunião', '#0000FF')
-- Navegação
calendar:nextMonth()                     -- Próximo mês
calendar:previousMonth()                 -- Mês anterior
calendar:goToToday()                     -- Ir para hoje
-- Obter informações
local selectedDate = calendar:getSelectedDate()
local currentMonth = calendar:getCurrentMonth()
local currentYear = calendar:getCurrentYear()
-- Eventos
calendar.onDateSelect = function(calendar, year, month, day)
    print("Data selecionada:", day .. "/" .. month .. "/" .. year)
end
calendar.onMonthChange = function(calendar, year, month)
    print("Mês alterado:", month .. "/" .. year)
end
```

#### Nível Intermediate
```lua
-- Calendar
local calendar = g_ui.createWidget('UICalendar', parent)

-- Data atual
local today = os.date('*t')
calendar:setDate(today.year, today.month, today.day)

-- Configurações
calendar:setMinDate(2020, 1, 1)          -- Data mínima
calendar:setMaxDate(2030, 12, 31)        -- Data máxima
calendar:setFirstDayOfWeek(1)            -- Segunda-feira como primeiro dia

-- Eventos especiais
calendar:addEvent(2025, 1, 15, 'Aniversário', '#FF0000')
calendar:addEvent(2025, 1, 25, 'Reunião', '#0000FF')

-- Navegação
calendar:nextMonth()                     -- Próximo mês
calendar:previousMonth()                 -- Mês anterior
calendar:goToToday()                     -- Ir para hoje

-- Obter informações
local selectedDate = calendar:getSelectedDate()
local currentMonth = calendar:getCurrentMonth()
local currentYear = calendar:getCurrentYear()

-- Eventos
calendar.onDateSelect = function(calendar, year, month, day)
    print("Data selecionada:", day .. "/" .. month .. "/" .. year)
    showEventsForDate(year, month, day)
end

calendar.onMonthChange = function(calendar, year, month)
    print("Mês alterado:", month .. "/" .. year)
    loadEventsForMonth(year, month)
end
```

#### Nível Advanced
```lua
-- Calendar
local calendar = g_ui.createWidget('UICalendar', parent)

-- Data atual
local today = os.date('*t')
calendar:setDate(today.year, today.month, today.day)

-- Configurações
calendar:setMinDate(2020, 1, 1)          -- Data mínima
calendar:setMaxDate(2030, 12, 31)        -- Data máxima
calendar:setFirstDayOfWeek(1)            -- Segunda-feira como primeiro dia

-- Eventos especiais
calendar:addEvent(2025, 1, 15, 'Aniversário', '#FF0000')
calendar:addEvent(2025, 1, 25, 'Reunião', '#0000FF')

-- Navegação
calendar:nextMonth()                     -- Próximo mês
calendar:previousMonth()                 -- Mês anterior
calendar:goToToday()                     -- Ir para hoje

-- Obter informações
local selectedDate = calendar:getSelectedDate()
local currentMonth = calendar:getCurrentMonth()
local currentYear = calendar:getCurrentYear()

-- Eventos
calendar.onDateSelect = function(calendar, year, month, day)
    print("Data selecionada:", day .. "/" .. month .. "/" .. year)
    showEventsForDate(year, month, day)
end

calendar.onMonthChange = function(calendar, year, month)
    print("Mês alterado:", month .. "/" .. year)
    loadEventsForMonth(year, month)
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

### Interface .otui de Calendar

```otui
CalendarWindow < MainWindow
  !text: tr('Calendar')
  size: 350 300

  UICalendar
    id: calendar
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: parent.top
    anchors.bottom: buttonPanel.top
    margin: 10

  UIWidget
    id: buttonPanel
    height: 30
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.bottom: parent.bottom
    margin: 10

    UIButton
      id: todayButton
      !text: tr('Today')
      width: 60
      anchors.left: parent.left
      @onClick: |
        local calendar = self:getParent():getParent():getChildById('calendar')
        calendar:goToToday()

    UIButton
      id: addEventButton
      !text: tr('Add Event')
      width: 80
      anchors.right: parent.right
      @onClick: showAddEventDialog()

  // Painel de eventos do dia
  UIWidget
    id: eventsPanel
    anchors.left: calendar.right
    anchors.right: parent.right
    anchors.top: parent.top
    anchors.bottom: buttonPanel.top
    margin: 10
    margin-left: 5
    background-color: #2A2A2A
    border-width: 1
    border-color: #404040

    UILabel
      !text: tr('Events')
      anchors.top: parent.top
      anchors.horizontalCenter: parent.horizontalCenter
      margin-top: 5
      font: verdana-11px-rounded

    UIScrollArea
      id: eventsScroll
      anchors.left: parent.left
      anchors.right: parent.right
      anchors.top: prev.bottom
      anchors.bottom: parent.bottom
      margin: 5
```

## 💡 Exemplos Práticos

### Exemplo 1: File Browser com Tree e Splitter

#### Inicialização e Configuração
```lua
-- modules/file_browser/file_browser.lua
fileBrowser = {}

function fileBrowser.init()
    fileBrowser.window = g_ui.displayUI('file_browser')
    fileBrowser.setupInterface()
    fileBrowser.loadRootDirectory()
end

function fileBrowser.setupInterface()
    local splitter = fileBrowser.window:getChildById('mainSplitter')
    local treeView = fileBrowser.window:getChildById('treeView')
    local contentArea = fileBrowser.window:getChildById('contentArea')
    
    -- Tree events
    treeView.onNodeSelect = function(treeView, node)
        local path = node:getData('path')
        if path then
            fileBrowser.loadDirectory(path)
        end
    end
```

#### Funcionalidade 1
```lua
    
    treeView.onNodeExpand = function(treeView, node)
        local path = node:getData('path')
        if path then
            fileBrowser.loadSubDirectories(node, path)
        end
    end
    
    -- Splitter ratio restore
    local savedRatio = g_settings.getNumber('fileBrowser.splitRatio', 0.3)
    splitter:setSplitRatio(savedRatio)
    
    splitter.onSplitRatioChange = function(splitter, ratio)
        g_settings.set('fileBrowser.splitRatio', ratio)
    end
end

function fileBrowser.loadRootDirectory()
    local treeView = fileBrowser.window:getChildById('treeView')
    local rootPath = g_resources.getWorkDir()
    
    local rootNode = treeView:addNode('OTClient')
    rootNode:setIcon('/icons/folder.png')
    rootNode:setData('path', rootPath)
    rootNode:setExpanded(true)
    
    fileBrowser.loadSubDirectories(rootNode, rootPath)
end
```

#### Funcionalidade 2
```lua

function fileBrowser.loadSubDirectories(parentNode, path)
    local files = g_resources.listDirectoryFiles(path)
    
    for _, file in ipairs(files) do
        local fullPath = path .. '/' .. file
        if g_resources.directoryExists(fullPath) then
            local node = parentNode:addChild(file)
            node:setIcon('/icons/folder.png')
            node:setData('path', fullPath)
        end
    end
end

function fileBrowser.loadDirectory(path)
    local contentArea = fileBrowser.window:getChildById('contentArea')
    contentArea:destroyChildren()
    
    local files = g_resources.listDirectoryFiles(path)
    
    for i, file in ipairs(files) do
        local item = g_ui.createWidget('UILabel', contentArea)
        item:setText(file)
        item:setHeight(20)
        item:addAnchor(AnchorLeft, 'parent', AnchorLeft)
        item:addAnchor(AnchorRight, 'parent', AnchorRight)
        
        if i == 1 then
            item:addAnchor(AnchorTop, 'parent', AnchorTop)
        else
            item:addAnchor(AnchorTop, 'prev', AnchorBottom)
        end
```

#### Finalização
```lua
        
        -- Click event
        item.onClick = function()
            local fullPath = path .. '/' .. file
            if g_resources.fileExists(fullPath) then
                fileBrowser.openFile(fullPath)
            end
        end
    end
end
```

### Exemplo 2: Status Dashboard com Progress Bars

#### Inicialização e Configuração
```lua
-- modules/status_dashboard/status_dashboard.lua
statusDashboard = {}

function statusDashboard.init()
    statusDashboard.window = g_ui.displayUI('status_dashboard')
    statusDashboard.setupProgressBars()
    statusDashboard.startUpdating()
end

function statusDashboard.setupProgressBars()
    local healthBar = statusDashboard.window:getChildById('healthBar')
    local manaBar = statusDashboard.window:getChildById('manaBar')
    local expBar = statusDashboard.window:getChildById('expBar')
    local staminaCircle = statusDashboard.window:getChildById('staminaCircle')
    
    -- Configurar barras
    healthBar:setShowText(true)
    healthBar:setTextFormat("{value}/{maximum}")
    healthBar:setAnimated(true)
    
    manaBar:setShowText(true)
    manaBar:setTextFormat("{value}/{maximum}")
    manaBar:setAnimated(true)
    
    expBar:setShowText(true)
    expBar:setTextFormat("{percent}%")
    
    -- Eventos de mudança de cor
    healthBar.onValueChange = function(bar, value)
        local percent = bar:getPercent()
        if percent < 0.3 then
            bar:setForegroundColor('#FF0000')
        elseif percent < 0.7 then
            bar:setForegroundColor('#FFAA00')
        else
            bar:setForegroundColor('#00AA00')
        end
```

#### Funcionalidade 1
```lua
    end
    
    manaBar.onValueChange = function(bar, value)
        local percent = bar:getPercent()
        if percent < 0.3 then
            bar:setForegroundColor('#FF0066')
        else
            bar:setForegroundColor('#0066FF')
        end
    end
end

function statusDashboard.updateStats()
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    local healthBar = statusDashboard.window:getChildById('healthBar')
    local manaBar = statusDashboard.window:getChildById('manaBar')
    local expBar = statusDashboard.window:getChildById('expBar')
    local staminaCircle = statusDashboard.window:getChildById('staminaCircle')
    
    -- Atualizar HP
    healthBar:setMinimum(0)
    healthBar:setMaximum(player:getMaxHealth())
    healthBar:setValue(player:getHealth())
    
    -- Atualizar Mana
    manaBar:setMinimum(0)
    manaBar:setMaximum(player:getMaxMana())
    manaBar:setValue(player:getMana())
    
    -- Atualizar Experience
    local expPercent = player:getExperiencePercent()
    expBar:setValue(expPercent)
    
    -- Atualizar Stamina
    local stamina = player:getStamina()
    staminaCircle:setValue(math.floor(stamina / 42 * 100)) -- 42 horas = 100%
end
```

#### Finalização
```lua

function statusDashboard.startUpdating()
    statusDashboard.updateStats()
    scheduleEvent(statusDashboard.startUpdating, 1000)
end
```

### Exemplo 3: Data Explorer com Tabs e Search

#### Inicialização e Configuração
```lua
-- modules/data_explorer/data_explorer.lua
dataExplorer = {}

function dataExplorer.init()
    dataExplorer.window = g_ui.displayUI('data_explorer')
    dataExplorer.setupTabs()
    dataExplorer.setupSearch()
    dataExplorer.loadInitialData()
end

function dataExplorer.setupTabs()
    local tabBar = dataExplorer.window:getChildById('tabBar')
    
    -- Adicionar tabs
    local itemsTab = tabBar:addTab('Items', 'items')
    local spellsTab = tabBar:addTab('Spells', 'spells')
    local creaturesTab = tabBar:addTab('Creatures', 'creatures')
    
    tabBar.onTabChange = function(tabBar, tab)
        local tabType = tab:getData()
        dataExplorer.switchToTab(tabType)
    end
```

#### Funcionalidade 1
```lua
    
    -- Selecionar primeira tab
    tabBar:selectTab(itemsTab)
end

function dataExplorer.setupSearch()
    local searchEdit = dataExplorer.window:getChildById('searchEdit')
    local searchButton = dataExplorer.window:getChildById('searchButton')
    
    searchEdit.onTextChange = function(widget, text)
        dataExplorer.filterResults(text)
    end
    
    searchButton.onClick = function()
        local text = searchEdit:getText()
        dataExplorer.performAdvancedSearch(text)
    end
end

function dataExplorer.switchToTab(tabType)
    local contentArea = dataExplorer.window:getChildById('contentArea')
    contentArea:destroyChildren()
    
    if tabType == 'items' then
        dataExplorer.showItemsInterface()
    elseif tabType == 'spells' then
        dataExplorer.showSpellsInterface()
    elseif tabType == 'creatures' then
        dataExplorer.showCreaturesInterface()
    end
```

#### Funcionalidade 2
```lua
end

function dataExplorer.showItemsInterface()
    local contentArea = dataExplorer.window:getChildById('contentArea')
    
    -- Lista de itens
    local itemsList = g_ui.createWidget('UITableView', contentArea)
    itemsList:addColumn('ID', 60)
    itemsList:addColumn('Name', 200)
    itemsList:addColumn('Type', 100)
    itemsList:addColumn('Value', 80)
    
    -- Carregar itens
    for itemId = 100, 200 do
        local item = Item.create(itemId)
        if item then
            local row = itemsList:addRow()
            row:setData('itemId', itemId)
            row:setCell(0, tostring(itemId))
            row:setCell(1, item:getDescription())
            row:setCell(2, item:getTypeName())
            row:setCell(3, tostring(item:getMarketData().value or 0))
        end
```

#### Finalização
```lua
    end
    
    itemsList.onRowSelect = function(tableView, row)
        local itemId = row:getData('itemId')
        dataExplorer.showItemDetails(itemId)
    end
end

function dataExplorer.showItemDetails(itemId)
    local detailsPanel = dataExplorer.window:getChildById('detailsPanel')
    detailsPanel:destroyChildren()
    
    local item = Item.create(itemId)
    if not item then return end
    
    -- Ícone do item
    local itemIcon = g_ui.createWidget('UIItem', detailsPanel)
    itemIcon:setItemId(itemId)
    itemIcon:setSize({width = 32, height = 32})
    
    -- Informações
    local infoLabel = g_ui.createWidget('UILabel', detailsPanel)
    infoLabel:setText(string.format("ID: %d\nName: %s\nWeight: %.2f", 
                                   itemId, 
                                   item:getDescription(),
                                   item:getWeight()))
    infoLabel:setTextWrap(true)
end
```

---

Esta documentação cobre os principais widgets especializados do OTClient, fornecendo exemplos práticos e interfaces completas para cada tipo de widget. Use estes exemplos como base para criar interfaces avançadas e interativas em seus módulos.
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

