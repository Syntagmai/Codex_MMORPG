---
tags: [otclient, ui, widgets, layouts, events, styling, guide, documentation]
status: completed
aliases: [Widgets, Interface do Usuário, OTClient UI, Sistema de UI, Interface, UI, Layouts, UI System]
---

# UI System Guide

> [!info] Este guia documenta o sistema de interface do usuário do OTClient, incluindo widgets, layouts, eventos, estilização e APIs de UI.

## 📋 Índice
- [[#Visão Geral]]
- [[#Sistema de Widgets]]
- [[#Layouts e Posicionamento]]
- [[#Sistema de Eventos]]
- [[#Estilização e Temas]]
- [[#APIs de UI]]
- [[#Criando Widgets Customizados]]
- [[#Melhores Práticas]]

---

## 🎯 Visão Geral

O sistema de UI do OTClient oferece:
- **Widgets Flexíveis**: Sistema hierárquico de elementos de interface
- **Layouts Avançados**: Posicionamento automático e responsivo
- **Sistema de Eventos**: Manipulação de entrada do usuário
- **Estilização CSS-like**: Aplicação de estilos usando sintaxe similar ao CSS
- **Performance Otimizada**: Renderização eficiente com OpenGL

### 🏗️ Arquitetura da UI
```
UI Manager (g_ui)
   │
   ├─ Root Widget
   │   │
   │   ├─ Main Windows
   │   │   ├─ Game Interface
   │   │   ├─ Inventory
   │   │   └─ Chat
   │   │
   │   ├─ Modal Dialogs
   │   │   ├─ Confirmations
   │   │   └─ Input Dialogs
   │   │
   │   └─ Overlays
   │       ├─ Notifications
   │       └─ Tooltips
   │
   ├─ Style System
   ├─ Event System
   └─ Resource Manager
```

---

## 🧩 Sistema de Widgets

### 📦 Classe UIWidget

O `UIWidget` é a classe base para todos os elementos de interface no OTClient.

#### 🔧 Métodos Core
```lua
-- Gerenciamento de hierarquia
widget:addChild(childWidget)
widget:removeChild(childWidget)
widget:getChildById('childId')
widget:getChildren()

-- Visibilidade e foco
widget:show()
widget:hide()
widget:focus()
widget:raise()
widget:lower()

-- Propriedades
widget:setId('myWidget')
widget:setEnabled(true)
widget:setVisible(true)
widget:setSize({width = 100, height = 50})
widget:setPosition({x = 10, y = 20})
```

#### 🎨 Propriedades dos Widgets
```lua
-- Obter propriedades
local id = widget:getId()
local size = widget:getSize()
local position = widget:getPosition()
local isVisible = widget:isVisible()
local isEnabled = widget:isEnabled()
local isFocused = widget:isFocused()

-- Definir propriedades
widget:setText('Hello World')
widget:setFont('verdana-11px-antialised')
widget:setColor('#FFFFFF')
widget:setBackgroundColor('#000000')
widget:setOpacity(0.8)
```

### 🎯 Widgets Principais

#### 📝 Label
```lua
local label = g_ui.createWidget('Label', parent)
label:setText('Texto do label')
label:setFont('verdana-11px-antialised')
label:setColor('#FFFFFF')
label:setTextAlign('center')
```

#### 🔘 Button
```lua
local button = g_ui.createWidget('Button', parent)
button:setText('Clique aqui')
button:setImage('/images/button.png')
button.onClick = function(widget)
    print('Botão clicado!')
end
```

#### 📋 Panel
```lua
local panel = g_ui.createWidget('Panel', parent)
panel:setSize({width = 200, height = 150})
panel:setBackgroundColor('#2c3e50')
panel:setBorderWidth(2)
panel:setBorderColor('#34495e')
```

#### 📦 Container
```lua
local container = g_ui.createWidget('UIWidget', parent)
container:setLayout('UIHorizontalLayout')
container:setSize({width = 300, height = 100})

-- Adicionar widgets ao container
local label1 = g_ui.createWidget('Label', container)
label1:setText('Item 1')

local label2 = g_ui.createWidget('Label', container)
label2:setText('Item 2')
```

---

## 📐 Layouts e Posicionamento

### 🎯 Sistema de Anchors

O sistema de anchors permite posicionamento relativo entre widgets.

#### 🔗 Tipos de Anchor
```lua
-- Anchors básicos
widget:addAnchor('left', 'parent', 'left')
widget:addAnchor('right', 'parent', 'right')
widget:addAnchor('top', 'parent', 'top')
widget:addAnchor('bottom', 'parent', 'bottom')

-- Anchors para centralização
widget:addAnchor('center', 'parent', 'center')
widget:addAnchor('hcenter', 'parent', 'hcenter')
widget:addAnchor('vcenter', 'parent', 'vcenter')

-- Anchors customizados
widget:addAnchor('left', 'otherWidget', 'right')
widget:addAnchor('bottom', 'otherWidget', 'top')
```

#### 📏 Exemplos de Posicionamento
```lua
-- Widget que preenche o pai
local fullWidget = g_ui.createWidget('UIWidget', parent)
fullWidget:addAnchor('left', 'parent', 'left')
fullWidget:addAnchor('right', 'parent', 'right')
fullWidget:addAnchor('top', 'parent', 'top')
fullWidget:addAnchor('bottom', 'parent', 'bottom')

-- Widget centralizado
local centerWidget = g_ui.createWidget('UIWidget', parent)
centerWidget:addAnchor('center', 'parent', 'center')
centerWidget:setSize({width = 100, height = 50})

-- Widget ancorado a outro
local button = g_ui.createWidget('Button', parent)
button:setSize({width = 80, height = 30})
button:addAnchor('left', 'parent', 'left')
button:addAnchor('bottom', 'parent', 'bottom')
button:setMargin({left = 10, bottom = 10})
```

### 🎨 Layouts Automáticos

#### 📊 UIHorizontalLayout
```lua
local container = g_ui.createWidget('UIWidget', parent)
container:setLayout('UIHorizontalLayout')
container:setSize({width = 300, height = 50})

-- Adicionar widgets horizontalmente
for i = 1, 3 do
    local button = g_ui.createWidget('Button', container)
    button:setText('Botão ' .. i)
    button:setSize({width = 80, height = 30})
end
```

#### 📈 UIVerticalLayout
```lua
local container = g_ui.createWidget('UIWidget', parent)
container:setLayout('UIVerticalLayout')
container:setSize({width = 200, height = 150})

-- Adicionar widgets verticalmente
for i = 1, 3 do
    local label = g_ui.createWidget('Label', container)
    label:setText('Linha ' .. i)
    label:setSize({width = 180, height = 30})
end
```

#### 🎯 UIGridLayout
```lua
local container = g_ui.createWidget('UIWidget', parent)
container:setLayout('UIGridLayout')
container:setGridSize({columns = 3, rows = 2})
container:setSize({width = 300, height = 100})

-- Adicionar widgets em grid
for i = 1, 6 do
    local button = g_ui.createWidget('Button', container)
    button:setText('Item ' .. i)
end
```

---

## 🎛️ Sistema de Eventos

### 📡 Eventos de Mouse
```lua
-- Eventos básicos de mouse
widget.onClick = function(widget)
    print('Widget clicado:', widget:getId())
end

widget.onDoubleClick = function(widget)
    print('Widget clicado duas vezes')
end

widget.onRightClick = function(widget)
    print('Botão direito clicado')
end

widget.onMouseEnter = function(widget)
    print('Mouse entrou no widget')
end

widget.onMouseLeave = function(widget)
    print('Mouse saiu do widget')
end

widget.onMousePress = function(widget, button)
    print('Botão pressionado:', button)
end

widget.onMouseRelease = function(widget, button)
    print('Botão solto:', button)
end
```

### ⌨️ Eventos de Teclado
```lua
-- Eventos de teclado
widget.onKeyPress = function(widget, keyCode, keyboardModifiers)
    print('Tecla pressionada:', keyCode)
    
    if keyCode == Key_Escape then
        widget:hide()
    elseif keyCode == Key_Enter then
        -- Executar ação
    end
end

widget.onKeyRelease = function(widget, keyCode, keyboardModifiers)
    print('Tecla solta:', keyCode)
end

widget.onTextInput = function(widget, text)
    print('Texto digitado:', text)
end
```

### 🔄 Eventos de Foco
```lua
widget.onFocusChange = function(widget, focused)
    if focused then
        print('Widget recebeu foco')
        widget:setBackgroundColor('#3498db')
    else
        print('Widget perdeu foco')
        widget:setBackgroundColor('#2c3e50')
    end
end
```

### 🎮 Eventos Customizados
```lua
-- Disparar evento customizado
widget:fireEvent('customEvent', {data = 'value'})

-- Escutar evento customizado
widget.onCustomEvent = function(widget, data)
    print('Evento customizado recebido:', data.data)
end

-- Eventos com parâmetros
widget:fireEvent('itemSelected', {itemId = 123, itemName = 'Sword'})
widget.onItemSelected = function(widget, itemData)
    print('Item selecionado:', itemData.itemName)
end
```

---

## 🎨 Estilização e Temas

### 🎭 Sistema de Estilos

#### 📝 Aplicando Estilos
```lua
-- Estilo inline
widget:setStyle('background-color: #2c3e50; color: white; border: 1px solid #34495e;')

-- Estilo via propriedades
widget:setBackgroundColor('#2c3e50')
widget:setColor('#FFFFFF')
widget:setBorderWidth(1)
widget:setBorderColor('#34495e')
```

#### 🎨 Estilos CSS-like
```lua
-- Aplicar múltiplos estilos
g_ui.setStyleSheet([[
  MainWindow {
    background-color: #2c3e50;
    border: 1px solid #34495e;
    border-radius: 5px;
  }
  
  Button {
    background-color: #3498db;
    color: white;
    border: none;
    border-radius: 3px;
    padding: 5px 10px;
  }
  
  Button:hover {
    background-color: #2980b9;
  }
  
  Button:pressed {
    background-color: #1f5f8b;
  }
  
  Label {
    color: #ecf0f1;
    font: verdana-11px-antialised;
  }
]])
```

#### 🎯 Seletores Avançados
```lua
-- Estilos específicos por ID
g_ui.setStyleSheet([[
  #myButton {
    background-color: #e74c3c;
    color: white;
  }
  
  #myButton:hover {
    background-color: #c0392b;
  }
  
  .error {
    color: #e74c3c;
    font-weight: bold;
  }
  
  .success {
    color: #27ae60;
    font-weight: bold;
  }
]])
```

### 🌈 Sistema de Cores
```lua
-- Cores predefinidas
local colors = {
    primary = '#3498db',
    secondary = '#2ecc71',
    danger = '#e74c3c',
    warning = '#f39c12',
    info = '#3498db',
    light = '#ecf0f1',
    dark = '#2c3e50'
}

-- Aplicar cores
widget:setColor(colors.primary)
widget:setBackgroundColor(colors.light)
```

---

## 🔧 APIs de UI

### 🎯 Gerenciamento de Widgets
```lua
-- Criar widget
local widget = g_ui.createWidget('UIWidget', parent)

-- Buscar widget por ID
local widget = g_ui.getWidgetById('myWidget')

-- Obter widget raiz
local rootWidget = g_ui.getRootWidget()

-- Destruir widget
widget:destroy()

-- Verificar existência
if widget then
    print('Widget existe')
end
```

### 🎨 Carregamento de Interfaces
```lua
-- Carregar interface do arquivo .otui
local window = g_ui.loadUI('myinterface', parent)
window:hide()

-- Exibir interface
g_ui.displayUI('myinterface')

-- Destruir interface
window:destroy()
```

### 📊 Gerenciamento de Janelas
```lua
-- Criar janela modal
local modal = g_ui.createWidget('MainWindow', rootWidget)
modal:setModal(true)
modal:show()
modal:focus()

-- Criar janela não-modal
local window = g_ui.createWidget('MainWindow', rootWidget)
window:setModal(false)
window:show()

-- Gerenciar z-order
window:raise()  -- Trazer para frente
window:lower()  -- Enviar para trás
```

### 🎛️ Sistema de Configuração
```lua
-- Salvar configuração de UI
g_settings.set('ui.windowSize', {width = 800, height = 600})
g_settings.set('ui.theme', 'dark')

-- Carregar configuração
local windowSize = g_settings.getSize('ui.windowSize')
local theme = g_settings.getString('ui.theme')

-- Aplicar configuração
g_window.resize(windowSize)
applyTheme(theme)
```

---

## 🛠️ Criando Widgets Customizados

### 🎯 Widget Básico
```lua
-- Criar widget customizado
local CustomWidget = {}

function CustomWidget.create(parent)
    local widget = g_ui.createWidget('UIWidget', parent)
    
    -- Configurar propriedades
    widget:setId('customWidget')
    widget:setSize({width = 200, height = 100})
    
    -- Adicionar elementos internos
    local label = g_ui.createWidget('Label', widget)
    label:setText('Widget Customizado')
    label:setPosition({x = 10, y = 10})
    
    local button = g_ui.createWidget('Button', widget)
    button:setText('Ação')
    button:setPosition({x = 10, y = 50})
    button.onClick = function()
        print('Ação executada!')
    end
    
    return widget
end

-- Uso
local myWidget = CustomWidget.create(parent)
```

### 🎨 Widget com Estilo Customizado
```lua
-- Widget com estilo próprio
local StyledWidget = {}

function StyledWidget.create(parent)
    local widget = g_ui.createWidget('UIWidget', parent)
    
    -- Aplicar estilo customizado
    widget:setStyle([[
        background-color: linear-gradient(to bottom, #3498db, #2980b9);
        border: 2px solid #2c3e50;
        border-radius: 8px;
        padding: 10px;
    ]])
    
    -- Adicionar conteúdo
    local title = g_ui.createWidget('Label', widget)
    title:setText('Título')
    title:setFont('verdana-11px-bold')
    title:setColor('#FFFFFF')
    title:setPosition({x = 10, y = 10})
    
    return widget
end
```

### 🔄 Widget com Eventos Customizados
```lua
-- Widget com eventos próprios
local EventWidget = {}

function EventWidget.create(parent)
    local widget = g_ui.createWidget('UIWidget', parent)
    
    -- Eventos customizados
    widget.onValueChanged = function(widget, newValue)
        print('Valor alterado para:', newValue)
    end
    
    widget.onStateChanged = function(widget, newState)
        print('Estado alterado para:', newState)
    end
    
    -- Métodos públicos
    widget.setValue = function(widget, value)
        widget.value = value
        widget:fireEvent('valueChanged', value)
    end
    
    widget.getValue = function(widget)
        return widget.value
    end
    
    return widget
end

-- Uso
local eventWidget = EventWidget.create(parent)
eventWidget:setValue('novo valor')
```

---

## ✅ Melhores Práticas

### 🛡️ Performance e Otimização
```lua
-- ✅ BOM: Reutilizar widgets
local widgetPool = {}

local function getWidget()
    if #widgetPool > 0 then
        return table.remove(widgetPool)
    else
        return g_ui.createWidget('UIWidget', parent)
    end
end

local function recycleWidget(widget)
    widget:hide()
    table.insert(widgetPool, widget)
end

-- ✅ BOM: Limitar número de widgets
local function createLimitedWidgets(count)
    local widgets = {}
    for i = 1, math.min(count, 100) do
        local widget = g_ui.createWidget('UIWidget', parent)
        table.insert(widgets, widget)
    end
    return widgets
end

-- ❌ EVITE: Criar widgets desnecessários
local function badPractice()
    for i = 1, 1000 do
        local widget = g_ui.createWidget('UIWidget', parent)
        -- widget usado apenas uma vez
    end
end
```

### 🔒 Validação e Segurança
```lua
-- ✅ BOM: Validar widgets antes de usar
local function safeWidgetOperation(widget)
    if not widget or not widget:isVisible() then
        return false
    end
    
    -- Operação segura
    widget:setText('Texto seguro')
    return true
end

-- ✅ BOM: Verificar existência de elementos
local function safeChildAccess(parent, childId)
    if not parent then return nil end
    
    local child = parent:getChildById(childId)
    if not child then
        print('Child não encontrado:', childId)
        return nil
    end
    
    return child
end
```

### 🎯 Organização de Código
```lua
-- ✅ BOM: Módulo bem organizado
local MyUIModule = {}

-- Variáveis privadas
local mainWindow
local widgets = {}

-- Função de inicialização
function MyUIModule.init()
    mainWindow = g_ui.loadUI('myinterface')
    mainWindow:hide()
    
    -- Configurar eventos
    connect(g_game, {
        onGameStart = MyUIModule.show,
        onGameEnd = MyUIModule.hide
    })
end

-- Função de finalização
function MyUIModule.terminate()
    if mainWindow then
        mainWindow:destroy()
    end
    
    disconnect(g_game, {
        onGameStart = MyUIModule.show,
        onGameEnd = MyUIModule.hide
    })
end

-- Funções públicas
function MyUIModule.show()
    if mainWindow then
        mainWindow:show()
        mainWindow:focus()
    end
end

function MyUIModule.hide()
    if mainWindow then
        mainWindow:hide()
    end
end

return MyUIModule
```
> - [[Getting_Started_Guide]] - Primeiros passos
> - [[Module_System_Guide]] - Sistema de módulos
> - [[Lua_API_Reference]] - Referência da API
> - [[OTUI_Module_Development_Guide]] - Desenvolvimento OTUI





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

























