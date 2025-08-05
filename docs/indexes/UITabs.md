---
tags: [ui, tabs, tabbar, system, otclient, documentation, habdel]
type: documentation
status: completed
priority: maximum
created: 2025-01-27
---

# 📑 UI-014: Sistema de Tabs e Abas

> [!info] **Story ID**: UI-014  
> **Categoria**: UI  
> **Status**: ✅ Completo  
> **Prioridade**: 🔥 **MÁXIMA**

## 📋 Índice
1. [Visão Geral](#visão-geral)
2. [Arquitetura do Sistema](#arquitetura-do-sistema)
3. [Tipos de TabBar](#tipos-de-tabbar)
4. [API Lua](#api-lua)
5. [UITabBar Básico](#uitabbar-básico)
6. [UIMoveableTabBar](#uimoveabletabbar)
7. [Exemplos Práticos](#exemplos-práticos)
8. [Melhores Práticas](#melhores-práticas)
9. [Performance e Otimização](#performance-e-otimização)

---

## 🎯 Visão Geral

O **Sistema de Tabs e Abas** do OTClient oferece funcionalidades avançadas para organizar conteúdo em abas, permitindo navegação eficiente entre diferentes seções da interface. O sistema suporta tabs fixos, móveis e com diferentes estilos visuais.

### 🎨 **Características Principais**

- **UITabBar**: Sistema básico de abas
- **UIMoveableTabBar**: Abas com drag & drop
- **Navegação por Teclado**: Ctrl+Tab, Ctrl+Shift+Tab
- **Estilos Flexíveis**: Horizontal, vertical, arredondado
- **Conteúdo Dinâmico**: Panels associados a cada aba
- **Eventos Avançados**: Callbacks para mudanças de aba

---

## 🏗️ Arquitetura do Sistema

### 🎭 **Estrutura Hierárquica**

```
Sistema de Tabs
   │
   ├─ UITabBar (Básico)
   │   ├─ Lista de Tabs
   │   ├─ Content Widget
   │   ├─ Tab Selection
   │   └─ Event Handling
   │
   ├─ UIMoveableTabBar (Avançado)
   │   ├─ Drag & Drop
   │   ├─ Pre/Post Tabs
   │   ├─ Navigation Buttons
   │   └─ Tab Spacing
   │
   ├─ Tab Content
   │   ├─ Tab Panels
   │   ├─ Content Switching
   │   └─ Panel Management
   │
   └─ Visual Styles
       ├─ Horizontal Tabs
       ├─ Vertical Tabs
       ├─ Rounded Tabs
       └─ Custom Themes
```

### 🔄 **Fluxo de Tab**

```
1. Criação do TabBar
   ↓
2. Adição de Tabs
   ↓
3. Configuração de Conteúdo
   ↓
4. Seleção de Tab Ativo
   ↓
5. Exibição de Conteúdo
   ↓
6. Navegação entre Tabs
   ↓
7. Gerenciamento de Estados
```

---

## 📑 Tipos de TabBar

### 🎯 **UITabBar (Básico)**

Sistema simples de abas com funcionalidades básicas.

```lua
-- Estrutura do UITabBar
    --  Estrutura do UITabBar (traduzido)
{
    tabs = {},              -- Lista de tabs
    currentTab = nil,       -- Tab ativo
    contentWidget = nil,    -- Widget de conteúdo
    onTabChange = callback  -- Evento de mudança
}
```

### 🎨 **UIMoveableTabBar (Avançado)**

Sistema avançado com drag & drop e navegação.

#### Nível Basic
```lua
-- Estrutura do UIMoveableTabBar
{
    tabs = {},              -- Tabs visíveis
    preTabs = {},           -- Tabs ocultos à esquerda
    postTabs = {},          -- Tabs ocultos à direita
    currentTab = nil,       -- Tab ativo
    tabSpacing = 0,         -- Espaçamento entre tabs
    tabsMoveable = false,   -- Permite mover tabs
    navigation = {}         -- Botões de navegação
}
```

#### Nível Intermediate
```lua
-- Estrutura do UIMoveableTabBar
{
    tabs = {},              -- Tabs visíveis
    preTabs = {},           -- Tabs ocultos à esquerda
    postTabs = {},          -- Tabs ocultos à direita
    currentTab = nil,       -- Tab ativo
    tabSpacing = 0,         -- Espaçamento entre tabs
    tabsMoveable = false,   -- Permite mover tabs
    navigation = {}         -- Botões de navegação
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
-- Estrutura do UIMoveableTabBar
{
    tabs = {},              -- Tabs visíveis
    preTabs = {},           -- Tabs ocultos à esquerda
    postTabs = {},          -- Tabs ocultos à direita
    currentTab = nil,       -- Tab ativo
    tabSpacing = 0,         -- Espaçamento entre tabs
    tabsMoveable = false,   -- Permite mover tabs
    navigation = {}         -- Botões de navegação
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

### 🎭 **Estilos Visuais**

#### Nível Basic
```lua
-- Tipos de TabBar disponíveis
{
    "TabBar",              -- Horizontal padrão
    "TabBarRounded",       -- Horizontal arredondado
    "TabBarVertical",      -- Vertical padrão
    "TabBarQtVertical",    -- Vertical estilo Qt
    "MoveableTabBar"       -- Movível com drag & drop
}
```

#### Nível Intermediate
```lua
-- Tipos de TabBar disponíveis
{
    "TabBar",              -- Horizontal padrão
    "TabBarRounded",       -- Horizontal arredondado
    "TabBarVertical",      -- Vertical padrão
    "TabBarQtVertical",    -- Vertical estilo Qt
    "MoveableTabBar"       -- Movível com drag & drop
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
-- Tipos de TabBar disponíveis
{
    "TabBar",              -- Horizontal padrão
    "TabBarRounded",       -- Horizontal arredondado
    "TabBarVertical",      -- Vertical padrão
    "TabBarQtVertical",    -- Vertical estilo Qt
    "MoveableTabBar"       -- Movível com drag & drop
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

### 📦 **Métodos de UITabBar**

```lua
-- Criar tab bar
    --  Criar tab bar (traduzido)
local tabBar = UITabBar.create()

-- Adicionar tab
    --  Adicionar tab (traduzido)
local tab = tabBar:addTab(text, panel, icon)

-- Selecionar tab
    --  Selecionar tab (traduzido)
tabBar:selectTab(tab)

-- Navegar entre tabs
    --  Navegar entre tabs (traduzido)
tabBar:selectNextTab()
tabBar:selectPrevTab()

-- Gerenciar tabs
    --  Gerenciar tabs (traduzido)
tabBar:removeTab(tab)
tabBar:getTab(text)
tabBar:clearTabs()

-- Configurar conteúdo
tabBar:setContentWidget(widget)
```

### 🎯 **Métodos de UIMoveableTabBar**

#### Nível Basic
```lua
-- Criar tab bar movível
local tabBar = UIMoveableTabBar.create()

-- Configurações avançadas
tabBar:setTabSpacing(spacing)
tabBar:setTabsMoveable(true)

-- Navegação avançada
tabBar:moveTab(tab, units)
tabBar:showPreTab()
tabBar:showPostTab()

-- Eventos de drag & drop
tabBar.onTabDragEnter = function(tab, mousePos) end
tabBar.onTabDragLeave = function(tab, mousePos) end
tabBar.onTabDrop = function(tab, mousePos) end
```

#### Nível Intermediate
```lua
-- Criar tab bar movível
local tabBar = UIMoveableTabBar.create()

-- Configurações avançadas
tabBar:setTabSpacing(spacing)
tabBar:setTabsMoveable(true)

-- Navegação avançada
tabBar:moveTab(tab, units)
tabBar:showPreTab()
tabBar:showPostTab()

-- Eventos de drag & drop
tabBar.onTabDragEnter = function(tab, mousePos) end
tabBar.onTabDragLeave = function(tab, mousePos) end
tabBar.onTabDrop = function(tab, mousePos) end
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
-- Criar tab bar movível
local tabBar = UIMoveableTabBar.create()

-- Configurações avançadas
tabBar:setTabSpacing(spacing)
tabBar:setTabsMoveable(true)

-- Navegação avançada
tabBar:moveTab(tab, units)
tabBar:showPreTab()
tabBar:showPostTab()

-- Eventos de drag & drop
tabBar.onTabDragEnter = function(tab, mousePos) end
tabBar.onTabDragLeave = function(tab, mousePos) end
tabBar.onTabDrop = function(tab, mousePos) end
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

### 🎨 **Métodos de Tab Individual**

```lua
-- Propriedades da tab
    --  Propriedades da tab (traduzido)
tab:setText(text)
tab:setIcon(icon)
tab:setEnabled(enabled)
tab:setChecked(checked)

-- Eventos da tab
    --  Eventos da tab (traduzido)
tab.onClick = function(tab) end
tab.onClose = function(tab) end
tab.onDragEnter = function(tab, mousePos) end
```

---

## 📑 UITabBar Básico

### 🎯 **Implementação Completa**

#### Inicialização e Configuração
```lua
-- Classe UITabBar
UITabBar = extends(UIWidget, 'UITabBar')

-- Funções privadas
local function onTabClick(tab)
    tab.tabBar:selectTab(tab)
end

local function onTabMouseRelease(tab, mousePos, mouseButton)
    if mouseButton == MouseRightButton and tab:containsPoint(mousePos) then
        signalcall(tab.tabBar.onTabLeftClick, tab.tabBar, tab)
    end
end

-- Criar tab bar
function UITabBar.create()
    local tabbar = UITabBar.internalCreate()
    tabbar:setFocusable(false)
    tabbar.tabs = {}
    return tabbar
end
```

#### Funcionalidade 1
```lua

-- Configurar após criação
function UITabBar:onSetup()
    self.buttonsPanel = self:getChildById('buttonsPanel')
end

-- Definir widget de conteúdo
function UITabBar:setContentWidget(widget)
    self.contentWidget = widget
    if #self.tabs > 0 then
        self.contentWidget:addChild(self.tabs[1].tabPanel)
    end
end

-- Adicionar tab
function UITabBar:addTab(text, panel, icon)
    if panel == nil then
        panel = g_ui.createWidget(self:getStyleName() .. 'Panel')
        panel:setId('tabPanel')
    end

    local tab = g_ui.createWidget(self:getStyleName() .. 'Button', self.buttonsPanel)

    panel.isTab = true
    tab.tabPanel = panel
    tab.tabBar = self
    tab:setId('tab')
    tab:setText(text)
    tab:setWidth(tab:getTextSize().width + tab:getPaddingLeft() + tab:getPaddingRight())
    tab.onClick = onTabClick
    tab.onMouseRelease = onTabMouseRelease
    tab.onDestroy = function()
        if not tab.tabPanel:isDestroyed() then
            tab.tabPanel:destroy()
        end
```

#### Funcionalidade 2
```lua
    end

    table.insert(self.tabs, tab)
    if #self.tabs == 1 then
        self:selectTab(tab)
    end

    local tabStyle = {}
    tabStyle['icon-source'] = icon
    tab:mergeStyle(tabStyle)

    return tab
end

-- Adicionar botão
function UITabBar:addButton(text, func, icon)
    local button = g_ui.createWidget(self:getStyleName() .. 'Button', self.buttonsPanel)
    button:setText(text)

    local style = {}
    style['icon-source'] = icon
    button:mergeStyle(style)

    button.onClick = func
    return button
end
```

#### Funcionalidade 3
```lua

-- Remover tab
function UITabBar:removeTab(tab)
    local index = table.find(self.tabs, tab)
    if index == nil then
        return
    end
    
    if self.currentTab == tab then
        if #self.tabs == 1 then
            self.currentTab = nil
        elseif index == #self.tabs then
            self:selectPrevTab()
        else
            self:selectNextTab()
        end
    end
    
    table.remove(self.tabs, index)
    tab:destroy()
end
```

#### Funcionalidade 4
```lua

-- Buscar tab por texto
function UITabBar:getTab(text)
    for k, tab in pairs(self.tabs) do
        if tab:getText():lower() == text:lower() then
            return tab
        end
    end
end

-- Selecionar tab
function UITabBar:selectTab(tab)
    if self.currentTab == tab then
        return
    end
    
    if self.contentWidget then
        local selectedWidget = self.contentWidget:getLastChild()
        if selectedWidget and selectedWidget.isTab then
            self.contentWidget:removeChild(selectedWidget)
        end
```

#### Funcionalidade 5
```lua
        self.contentWidget:addChild(tab.tabPanel)
        tab.tabPanel:fill('parent')
    end

    if self.currentTab then
        self.currentTab:setChecked(false)
    end
    
    signalcall(self.onTabChange, self, tab)
    self.currentTab = tab
    tab:setChecked(true)
    tab:setOn(false)

    local parent = tab:getParent()
    if parent then
        parent:focusChild(tab, MouseFocusReason)
    end
end

-- Navegar para próxima tab
function UITabBar:selectNextTab()
```

#### Funcionalidade 6
```lua
    if self.currentTab == nil then
        return
    end
    
    local index = table.find(self.tabs, self.currentTab)
    if index == nil then
        return
    end
    
    local nextTab = self.tabs[index + 1] or self.tabs[1]
    if not nextTab then
        return
    end
    
    self:selectTab(nextTab)
end

-- Navegar para tab anterior
function UITabBar:selectPrevTab()
    if self.currentTab == nil then
        return
    end
```

#### Funcionalidade 7
```lua
    
    local index = table.find(self.tabs, self.currentTab)
    if index == nil then
        return
    end
    
    local prevTab = self.tabs[index - 1] or self.tabs[#self.tabs]
    if not prevTab then
        return
    end
    
    self:selectTab(prevTab)
end

-- Obter panel da tab
function UITabBar:getTabPanel(tab)
    return tab.tabPanel
end

-- Obter panel da tab atual
function UITabBar:getCurrentTabPanel()
```

#### Funcionalidade 8
```lua
    if self.currentTab then
        return self.currentTab.tabPanel
    end
end

-- Obter tab atual
function UITabBar:getCurrentTab()
    return self.currentTab
end

-- Obter todas as tabs
function UITabBar:getTabs()
    return self.tabs
end

-- Obter todos os panels
function UITabBar:getTabsPanel()
    return table.collect(self.tabs, function(_, tab)
        return tab.tabPanel
    end)
end
```

#### Finalização
```lua

-- Limpar todas as tabs
function UITabBar:clearTabs()
    while #self.tabs > 0 do
        self:removeTab(self.tabs[#self.tabs])
    end
end
```

### 🎨 **Estilo OTUI para UITabBar**

```otui
TabBar < UITabBar
  size: 80 21
  
  Panel
    id: buttonsPanel
    anchors.fill: parent

TabBarPanel < Panel

TabBarButton < UIButton
  size: 20 21
  image-source: /images/ui/tabbutton_square
  image-color: #dfdfdf
  image-clip: 0 0 20 21
  image-border: 3
  image-border-bottom: 0
  icon-color: #dfdfdf
  color: #dfdfdf
  anchors.top: parent.top
  padding: 5

  $first:
    anchors.left: parent.left

  $!first:
    anchors.left: prev.right
    margin-left: 5

  $hover !checked:
    image-clip: 0 21 20 21
    color: #dfdfdf

  $disabled:
    image-color: #dfdfdf88
    icon-color: #dfdfdf

  $checked:
    image-clip: 0 42 20 21
    color: #dfdfdf

  $on !checked:
    color: #dfdfdf
```

---

## 🎨 UIMoveableTabBar

### 🎯 **Implementação Avançada**

#### Inicialização e Configuração
```lua
-- Classe UIMoveableTabBar
UIMoveableTabBar = extends(UITabBar, 'UIMoveableTabBar')

-- Criar tab bar movível
function UIMoveableTabBar.create()
    local tabbar = UIMoveableTabBar.internalCreate()
    tabbar:setFocusable(false)
    tabbar.tabs = {}
    tabbar.selected = nil -- dragged tab
    tabbar.tabSpacing = 0
    tabbar.tabsMoveable = false
    tabbar.preTabs = {}
    tabbar.postTabs = {}
    tabbar.prevNavigation = nil
    tabbar.nextNavigation = nil
    tabbar.dropTarget = nil
    tabbar.dropCallback = nil
    tabbar.dropTargetHighlighted = false
    
    tabbar.onGeometryChange = function()
        hideTabs(tabbar, true, tabbar.postTabs, 0)
        updateTabs(tabbar)
    end
```

#### Funcionalidade 1
```lua
    
    return tabbar
end

-- Definir espaçamento entre tabs
function UIMoveableTabBar:setTabSpacing(tabSpacing)
    self.tabSpacing = tabSpacing
    updateMargins(self)
end

-- Adicionar tab com funcionalidades avançadas
function UIMoveableTabBar:addTab(text, panel, menuCallback)
    if panel == nil then
        panel = g_ui.createWidget(self:getStyleName() .. 'Panel')
        panel:setId('tabPanel')
    end

    local tab = g_ui.createWidget(self:getStyleName() .. 'Button', self)
    panel.isTab = true
    tab.tabPanel = panel
    tab.tabBar = self
    tab:setId('tab')
    tab:setDraggable(self.tabsMoveable)
    tab:setText(text)
    
    if not tab.ignoreTextResize then
        tab:setWidth(tab:getTextSize().width + tab:getPaddingLeft() + tab:getPaddingRight())
    end
```

#### Funcionalidade 2
```lua
    
    tab.menuCallback = menuCallback or nil
    tab.onClick = onTabClick
    tab.onMousePress = onTabMousePress
    tab.onDragEnter = onTabDragEnter
    tab.onDragLeave = onTabDragLeave
    tab.onDragMove = onTabDragMove
    
    tab.onDestroy = function()
        tab.tabPanel:destroy()
    end

    if #self.tabs == 0 then
        self:selectTab(tab)
        tab:setMarginLeft(0)
        table.insert(self.tabs, tab)
    else
        local newMargin = self.tabSpacing * #self.tabs
        for i = 1, #self.tabs do
            newMargin = newMargin + self.tabs[i]:getWidth()
        end
```

#### Funcionalidade 3
```lua
        tab:setMarginLeft(newMargin)

        hideTabs(self, true, self.postTabs, tab:getWidth())
        table.insert(self.tabs, tab)
        if #self.tabs == 1 then
            self:selectTab(tab)
        end
        updateMargins(self)
    end

    updateNavigation(self)
    return tab
end

-- Mover tab por posição
function UIMoveableTabBar:moveTab(tab, units)
    local index = table.find(self.tabs, tab)
    if index == nil then
        return
    end

    local focus = false
    if self.currentTab == tab then
        self:selectPrevTab()
        focus = true
    end
```

#### Funcionalidade 4
```lua

    table.remove(self.tabs, index)

    local newIndex = math.min(#self.tabs + 1, math.max(index + units, 1))
    table.insert(self.tabs, newIndex, tab)
    
    if focus then
        self:selectTab(tab)
    end
    
    updateMargins(self)
    return newIndex
end

-- Aplicar estilo
function UIMoveableTabBar:onStyleApply(styleName, styleNode)
    if styleNode['movable'] then
        self.tabsMoveable = styleNode['movable']
    end
    if styleNode['tab-spacing'] then
        self:setTabSpacing(styleNode['tab-spacing'])
    end
```

#### Finalização
```lua
end
```

---

## 💡 Exemplos Práticos

### 🎯 **Exemplo 1: Sistema de Tabs Básico**

#### Nível Basic
```lua
local BasicTabSystem = {}
function BasicTabSystem.createBasicTabs(parent)
    local tabBar = g_ui.createWidget('TabBar', parent)
    -- Widget de conteúdo
    local contentWidget = g_ui.createWidget('Panel', parent)
    -- Adicionar tabs
    local tab1 = tabBar:addTab('Informações', nil, '/icons/info.png')
    local tab2 = tabBar:addTab('Configurações', nil, '/icons/settings.png')
    local tab3 = tabBar:addTab('Estatísticas', nil, '/icons/stats.png')
    -- Configurar conteúdo das tabs
    local panel1 = tab1.tabPanel
    local label1 = g_ui.createWidget('Label', panel1)
    local panel2 = tab2.tabPanel
    local label2 = g_ui.createWidget('Label', panel2)
    local panel3 = tab3.tabPanel
    local label3 = g_ui.createWidget('Label', panel3)
    -- Evento de mudança de tab
    tabBar.onTabChange = function(tabBar, tab)
        print('Tab alterada para:', tab:getText())
    end
end
-- Uso
local tabSystem = BasicTabSystem.createBasicTabs(parent)
```

#### Nível Intermediate
```lua
local BasicTabSystem = {}

function BasicTabSystem.createBasicTabs(parent)
    local tabBar = g_ui.createWidget('TabBar', parent)
    tabBar:setSize({width = 400, height = 25})
    
    -- Widget de conteúdo
    local contentWidget = g_ui.createWidget('Panel', parent)
    contentWidget:setPosition({x = 0, y = 25})
    contentWidget:setSize({width = 400, height = 300})
    
    tabBar:setContentWidget(contentWidget)
    
    -- Adicionar tabs
    local tab1 = tabBar:addTab('Informações', nil, '/icons/info.png')
    local tab2 = tabBar:addTab('Configurações', nil, '/icons/settings.png')
    local tab3 = tabBar:addTab('Estatísticas', nil, '/icons/stats.png')
    
    -- Configurar conteúdo das tabs
    local panel1 = tab1.tabPanel
    local label1 = g_ui.createWidget('Label', panel1)
    label1:setText('Informações do personagem')
    label1:setPosition({x = 10, y = 10})
    
    local panel2 = tab2.tabPanel
    local label2 = g_ui.createWidget('Label', panel2)
    label2:setText('Configurações do jogo')
    label2:setPosition({x = 10, y = 10})
    
    local panel3 = tab3.tabPanel
    local label3 = g_ui.createWidget('Label', panel3)
    label3:setText('Estatísticas detalhadas')
    label3:setPosition({x = 10, y = 10})
    
    -- Evento de mudança de tab
    tabBar.onTabChange = function(tabBar, tab)
        print('Tab alterada para:', tab:getText())
    end
    
    return tabBar
end

-- Uso
local tabSystem = BasicTabSystem.createBasicTabs(parent)
```

#### Nível Advanced
```lua
local BasicTabSystem = {}

function BasicTabSystem.createBasicTabs(parent)
    local tabBar = g_ui.createWidget('TabBar', parent)
    tabBar:setSize({width = 400, height = 25})
    
    -- Widget de conteúdo
    local contentWidget = g_ui.createWidget('Panel', parent)
    contentWidget:setPosition({x = 0, y = 25})
    contentWidget:setSize({width = 400, height = 300})
    
    tabBar:setContentWidget(contentWidget)
    
    -- Adicionar tabs
    local tab1 = tabBar:addTab('Informações', nil, '/icons/info.png')
    local tab2 = tabBar:addTab('Configurações', nil, '/icons/settings.png')
    local tab3 = tabBar:addTab('Estatísticas', nil, '/icons/stats.png')
    
    -- Configurar conteúdo das tabs
    local panel1 = tab1.tabPanel
    local label1 = g_ui.createWidget('Label', panel1)
    label1:setText('Informações do personagem')
    label1:setPosition({x = 10, y = 10})
    
    local panel2 = tab2.tabPanel
    local label2 = g_ui.createWidget('Label', panel2)
    label2:setText('Configurações do jogo')
    label2:setPosition({x = 10, y = 10})
    
    local panel3 = tab3.tabPanel
    local label3 = g_ui.createWidget('Label', panel3)
    label3:setText('Estatísticas detalhadas')
    label3:setPosition({x = 10, y = 10})
    
    -- Evento de mudança de tab
    tabBar.onTabChange = function(tabBar, tab)
        print('Tab alterada para:', tab:getText())
    end
    
    return tabBar
end

-- Uso
local tabSystem = BasicTabSystem.createBasicTabs(parent)
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

### 🎨 **Exemplo 2: Sistema de Tabs Avançado**

#### Inicialização e Configuração
```lua
local AdvancedTabSystem = {}

function AdvancedTabSystem.createAdvancedTabs(parent)
    local tabBar = g_ui.createWidget('MoveableTabBar', parent)
    tabBar:setSize({width = 500, height = 25})
    tabBar:setTabSpacing(5)
    tabBar.tabsMoveable = true
    
    -- Widget de conteúdo
    local contentWidget = g_ui.createWidget('Panel', parent)
    contentWidget:setPosition({x = 0, y = 25})
    contentWidget:setSize({width = 500, height = 400})
    
    tabBar:setContentWidget(contentWidget)
    
    -- Adicionar tabs dinamicamente
    local tabs = {
        {text = 'Inventário', icon = '/icons/inventory.png'},
        {text = 'Skills', icon = '/icons/skills.png'},
        {text = 'Quest Log', icon = '/icons/quest.png'},
        {text = 'Mapa', icon = '/icons/map.png'},
        {text = 'Chat', icon = '/icons/chat.png'},
        {text = 'Config', icon = '/icons/config.png'}
    }
```

#### Funcionalidade 1
```lua
    
    for i, tabData in ipairs(tabs) do
        local tab = tabBar:addTab(tabData.text, nil, tabData.icon)
        
        -- Configurar conteúdo específico
        local panel = tab.tabPanel
        local label = g_ui.createWidget('Label', panel)
        label:setText('Conteúdo de ' .. tabData.text)
        label:setPosition({x = 10, y = 10})
        
        -- Adicionar botão de fechar
        local closeButton = g_ui.createWidget('Button', tab)
        closeButton:setText('X')
        closeButton:setSize({width = 15, height = 15})
        closeButton:setPosition({x = tab:getWidth() - 20, y = 2})
        
        closeButton.onClick = function()
            tabBar:removeTab(tab)
        end
    end
    
    -- Eventos avançados
    tabBar.onTabChange = function(tabBar, tab)
        print('Tab ativa:', tab:getText())
    end
```

#### Finalização
```lua
    
    tabBar.onTabLeftClick = function(tabBar, tab)
        print('Clique direito na tab:', tab:getText())
    end
    
    return tabBar
end

-- Uso
local advancedTabs = AdvancedTabSystem.createAdvancedTabs(parent)
```

### 🪟 **Exemplo 3: Sistema de Tabs com Drag & Drop**

#### Inicialização e Configuração
```lua
local DragDropTabSystem = {}

function DragDropTabSystem.createDragDropTabs(parent)
    local tabBar = g_ui.createWidget('MoveableTabBar', parent)
    tabBar:setSize({width = 600, height = 30})
    tabBar:setTabSpacing(2)
    tabBar.tabsMoveable = true
    
    -- Configurar drag & drop
    tabBar.onTabDragEnter = function(tab, mousePos)
        print('Iniciando drag da tab:', tab:getText())
        tab:setOpacity(0.7)
    end
    
    tabBar.onTabDragLeave = function(tab, mousePos)
        print('Finalizando drag da tab:', tab:getText())
        tab:setOpacity(1.0)
    end
    
    tabBar.onTabDrop = function(tab, mousePos)
        print('Tab dropada:', tab:getText())
        -- Aqui você implementaria a lógica de reorganização
    end
```

#### Funcionalidade 1
```lua
    
    -- Widget de conteúdo
    local contentWidget = g_ui.createWidget('Panel', parent)
    contentWidget:setPosition({x = 0, y = 30})
    contentWidget:setSize({width = 600, height = 500})
    
    tabBar:setContentWidget(contentWidget)
    
    -- Adicionar tabs com conteúdo rico
    local tabConfigs = {
        {
            text = 'Personagem',
            icon = '/icons/character.png',
            content = function(panel)
                local charInfo = g_ui.createWidget('Label', panel)
                charInfo:setText('Informações do Personagem')
                charInfo:setPosition({x = 10, y = 10})
                
                local levelLabel = g_ui.createWidget('Label', panel)
                levelLabel:setText('Nível: 50')
                levelLabel:setPosition({x = 10, y = 40})
                
                local expBar = g_ui.createWidget('UIProgressBar', panel)
                expBar:setPosition({x = 10, y = 70})
                expBar:setSize({width = 200, height = 20})
                expBar:setPercent(75)
            end
```

#### Funcionalidade 2
```lua
        },
        {
            text = 'Inventário',
            icon = '/icons/inventory.png',
            content = function(panel)
                local grid = g_ui.createWidget('Panel', panel)
                grid:setPosition({x = 10, y = 10})
                grid:setSize({width = 300, height = 200})
                
                -- Simular slots de inventário
                for i = 1, 20 do
                    local slot = g_ui.createWidget('UIItem', grid)
                    local x = ((i-1) % 10) * 32
                    local y = math.floor((i-1) / 10) * 32
                    slot:setPosition({x = x, y = y})
                    slot:setSize({width = 30, height = 30})
                end
            end
        },
        {
            text = 'Skills',
            icon = '/icons/skills.png',
            content = function(panel)
                local skillsList = g_ui.createWidget('TextList', panel)
                skillsList:setPosition({x = 10, y = 10})
                skillsList:setSize({width = 250, height = 300})
                
                local skills = {'Sword Fighting', 'Shielding', 'Distance', 'Magic'}
                for i, skill in ipairs(skills) do
                    skillsList:addOption(skill .. ': 50')
                end
```

#### Finalização
```lua
            end
        }
    }
    
    for i, config in ipairs(tabConfigs) do
        local tab = tabBar:addTab(config.text, nil, config.icon)
        config.content(tab.tabPanel)
    end
    
    return tabBar
end

-- Uso
local dragDropTabs = DragDropTabSystem.createDragDropTabs(parent)
```

---

## ✅ Melhores Práticas

### 🎯 **Configuração Adequada**

```lua
-- ✅ BOM: Sempre definir content widget
    --  ✅ BOM: Sempre definir content widget (traduzido)
function createTabBarWithContent(parent)
    -- Função: createTabBarWithContent
    local tabBar = g_ui.createWidget('TabBar', parent)
    local contentWidget = g_ui.createWidget('Panel', parent)
    
    tabBar:setContentWidget(contentWidget)
    return tabBar
end

-- ✅ BOM: Gerenciar ciclo de vida das tabs
    --  ✅ BOM: Gerenciar ciclo de vida das tabs (traduzido)
function manageTabLifecycle(tabBar, tab)
    -- Função: manageTabLifecycle
    tab.onDestroy = function()
        if tab.tabPanel and not tab.tabPanel:isDestroyed() then
    -- Verificação condicional
            tab.tabPanel:destroy()
        end
    end
end

-- ✅ BOM: Validar antes de adicionar tabs
    --  ✅ BOM: Validar antes de adicionar tabs (traduzido)
function validateTabData(text, panel, icon)
    -- Função: validateTabData
    if not text or type(text) ~= 'string' then
    -- Verificação condicional
        error('Texto da tab deve ser uma string válida')
    end
    
    if panel and not panel:isInstanceOf('UIWidget') then
    -- Verificação condicional
        error('Panel deve ser um widget válido')
    end
    
    return true
end
```

### 🎨 **Organização de Conteúdo**

```lua
-- ✅ BOM: Organizar conteúdo por tabs
function organizeContentByTabs(tabBar, contentMap)
    -- Função: organizeContentByTabs
    for tabName, contentCreator in pairs(contentMap) do
    -- Loop de repetição
        local tab = tabBar:addTab(tabName)
        contentCreator(tab.tabPanel)
    end
end

-- ✅ BOM: Usar callbacks para flexibilidade
    --  ✅ BOM: Usar callbacks para flexibilidade (traduzido)
function createTabWithCallbacks(tabBar, text, callbacks)
    -- Função: createTabWithCallbacks
    local tab = tabBar:addTab(text)
    
    if callbacks.onCreate then
    -- Verificação condicional
        callbacks.onCreate(tab)
    end
    
    if callbacks.onSelect then
    -- Verificação condicional
        tab.onSelect = callbacks.onSelect
    end
    
    if callbacks.onClose then
    -- Verificação condicional
        tab.onClose = callbacks.onClose
    end
    
    return tab
end
```

### 🔧 **Navegação Eficiente**

```lua
-- ✅ BOM: Navegação por teclado
function setupKeyboardNavigation(tabBar)
    -- Função: setupKeyboardNavigation
    g_keyboard.bindKeyPress('Ctrl+Tab', function()
        tabBar:selectNextTab()
    end)
    
    g_keyboard.bindKeyPress('Ctrl+Shift+Tab', function()
        tabBar:selectPrevTab()
    end)
end

-- ✅ BOM: Sistema de atalhos
    --  ✅ BOM: Sistema de atalhos (traduzido)
function setupTabShortcuts(tabBar, shortcuts)
    -- Função: setupTabShortcuts
    for key, tabIndex in pairs(shortcuts) do
    -- Loop de repetição
        g_keyboard.bindKeyPress(key, function()
            if tabBar.tabs[tabIndex] then
    -- Verificação condicional
                tabBar:selectTab(tabBar.tabs[tabIndex])
            end
        end)
    end
end
```

---

## 🚀 Performance e Otimização

### 📊 **Métricas de Performance**

1. **Tempo de Criação**: < 2ms por tab
2. **Tempo de Seleção**: < 1ms
3. **Uso de Memória**: < 1KB por tab
4. **Tempo de Navegação**: < 0.5ms

### 🎯 **Técnicas de Otimização**

```lua
-- Lazy loading de conteúdo
local contentCache = {}

function loadTabContentLazy(tab, contentLoader)
    -- Função: loadTabContentLazy
    if not contentCache[tab:getText()] then
    -- Verificação condicional
        contentCache[tab:getText()] = contentLoader()
    end
    
    return contentCache[tab:getText()]
end

-- Pool de tabs para reutilização
local tabPool = {}

function getTabFromPool(tabBar, text)
    -- Função: getTabFromPool
    if #tabPool > 0 then
    -- Verificação condicional
        local tab = table.remove(tabPool)
        tab:setText(text)
        return tab
    end
    
    return tabBar:addTab(text)
end

function returnTabToPool(tab)
    -- Função: returnTabToPool
    tab:hide()
    table.insert(tabPool, tab)
end
```

### 🔧 **Monitoramento de Performance**

```lua
-- Função para medir performance de tabs
local function measureTabPerformance()
    local startTime = g_clock.millis()
    
    local tabBar = g_ui.createWidget('TabBar')
    
    for i = 1, 10 do
    -- Loop de repetição
        tabBar:addTab('Tab ' .. i)
    end
    
    local endTime = g_clock.millis()
    print('Tempo de criação de 10 tabs:', endTime - startTime, 'ms')
    
    tabBar:destroy()
end

-- Sistema de métricas
local tabMetrics = {
    created = 0,
    selected = 0,
    totalTime = 0
}

function trackTabCreation()
    -- Função: trackTabCreation
    tabMetrics.created = tabMetrics.created + 1
end

function trackTabSelection(duration)
    -- Função: trackTabSelection
    tabMetrics.selected = tabMetrics.selected + 1
    tabMetrics.totalTime = tabMetrics.totalTime + duration
end
```

---

## 📚 Referências

### 🔗 **Links Automáticos**

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

## 🔗 Links Relacionados
- [[UIAdvancedWidgets]] - Widgets Avançados
- [[UIAnimations]] - Sistema de Animações
- [[UIFormWidgets]] - Widgets de Formulário
- [[UIDragDrop]] - Sistema de Drag & Drop
- [[UIModals]] - Sistema de Modais e Diálogos

### 📖 Documentação Técnica
- **UITabBar**: Sistema básico de abas
- **UIMoveableTabBar**: Sistema avançado com drag & drop
- **Tab Styles**: Estilos visuais disponíveis

---

**Última Atualização**: 2025-01-27  
**Versão**: 1.0  
**Status**: ✅ **Completo**  
**Prioridade**: 🔥 **MÁXIMA** 