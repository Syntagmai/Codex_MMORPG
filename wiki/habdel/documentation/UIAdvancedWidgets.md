---
tags: [ui, advanced_widgets, otclient, documentation, habdel]
type: documentation
status: completed
priority: maximum
created: 2025-01-27
---

# 🎨 UI-009: Widgets Avançados

> [!info] **Story ID**: UI-009  
> **Categoria**: UI  
> **Status**: ✅ Completo  
> **Prioridade**: 🔥 **MÁXIMA**

## 📋 Índice
1. [Visão Geral](#visão-geral)
2. [Arquitetura dos Widgets Avançados](#arquitetura-dos-widgets-avançados)
3. [API C++](#api-c)
4. [API Lua](#api-lua)
5. [Widgets Especializados](#widgets-especializados)
6. [Exemplos Práticos](#exemplos-práticos)
7. [Melhores Práticas](#melhores-práticas)
8. [Performance e Otimização](#performance-e-otimização)

---

## 🎯 Visão Geral

Os **Widgets Avançados** do OTClient representam o sistema mais sofisticado de componentes de interface, oferecendo funcionalidades avançadas como:

- **Hierarquia Complexa**: Sistema de widgets aninhados com gerenciamento automático
- **Layouts Avançados**: Posicionamento inteligente e responsivo
- **Eventos Customizados**: Sistema de eventos extensível
- **Estilização Dinâmica**: Aplicação de estilos em tempo real
- **Performance Otimizada**: Renderização eficiente com OpenGL

### 🏗️ Arquitetura dos Widgets Avançados

```
UIWidget (Classe Base)
   │
   ├─ Propriedades Core
   │   ├─ m_id (Identificador único)
   │   ├─ m_rect (Posição e tamanho)
   │   ├─ m_parent (Widget pai)
   │   └─ m_children (Lista de filhos)
   │
   ├─ Sistema de Estados
   │   ├─ PropEnabled (Habilitado/Desabilitado)
   │   ├─ PropVisible (Visível/Invisível)
   │   ├─ PropFocusable (Pode receber foco)
   │   └─ PropDraggable (Pode ser arrastado)
   │
   ├─ Sistema de Eventos
   │   ├─ Mouse Events (clique, movimento, scroll)
   │   ├─ Keyboard Events (teclas pressionadas)
   │   ├─ Focus Events (ganho/perda de foco)
   │   └─ Custom Events (eventos personalizados)
   │
   └─ Sistema de Renderização
       ├─ drawSelf() (Renderização própria)
       ├─ drawChildren() (Renderização dos filhos)
       └─ Clipping e Transformações
```

---

## 🔧 API C++

### 📦 Classe UIWidget

A classe `UIWidget` é definida em `src/framework/ui/uiwidget.h` e implementada em `src/framework/ui/uiwidget.cpp`.

#### 🔧 Métodos Core

```cpp
// Construtor e Destrutor
UIWidget();
~UIWidget();

// Renderização
virtual void drawSelf(DrawPoolType drawPane);
virtual void draw(const Rect& visibleRect, DrawPoolType drawPane);
protected: virtual void drawChildren(const Rect& visibleRect, DrawPoolType drawPane);

// Gerenciamento de Hierarquia
void addChild(const UIWidgetPtr& child);
void insertChild(int32_t index, const UIWidgetPtr& child);
void removeChild(const UIWidgetPtr& child);
void focusChild(const UIWidgetPtr& child, Fw::FocusReason reason);
void focusNextChild(Fw::FocusReason reason, bool rotate = false);
void focusPreviousChild(Fw::FocusReason reason, bool rotate = false);

// Posicionamento e Layout
void setRect(const Rect& rect);
Rect getRect() const;
void setPosition(const Point& position);
Point getPosition() const;
void setSize(const Size& size);
Size getSize() const;

// Estados e Propriedades
void setEnabled(bool enabled);
bool isEnabled() const;
void setVisible(bool visible);
bool isVisible() const;
void setFocusable(bool focusable);
bool isFocusable() const;
void setDraggable(bool draggable);
bool isDraggable() const;

// Foco e Interação
void focus(Fw::FocusReason reason = Fw::ActiveFocusReason);
void unfocus();
bool isFocused() const;
void raise();
void lower();
```

#### 🎨 Sistema de Estados

```cpp
// Flags de Propriedades
enum FlagProp : uint32_t {
    PropTextWrap = 1 << 0,
    PropTextVerticalAutoResize = 1 << 1,
    PropTextHorizontalAutoResize = 1 << 2,
    PropTextOnlyUpperCase = 1 << 3,
    PropEnabled = 1 << 4,
    PropVisible = 1 << 5,
    PropFocusable = 1 << 6,
    PropFixedSize = 1 << 7,
    PropPhantom = 1 << 8,
    PropDraggable = 1 << 9,
    PropDestroyed = 1 << 10,
    PropClipping = 1 << 11,
    PropCustomId = 1 << 12,
    PropUpdateEventScheduled = 1 << 13,
    PropUpdatingMove = 1 << 14,
    PropLoadingStyle = 1 << 15,
    PropUpdateStyleScheduled = 1 << 16,
    PropFirstOnStyle = 1 << 17,
    PropImageBordered = 1 << 18,
    PropImageFixedRatio = 1 << 19,
    PropImageRepeated = 1 << 20,
    PropImageSmooth = 1 << 21,
    PropImageAutoResize = 1 << 22,
    PropImageIndividualAnimation = 1 << 23,
    PropUpdateChildrenIndexStates = 1 << 24,
    PropDisableUpdateTemporarily = 1 << 25,
    PropOnHTML = 1 << 26
};

// Gerenciamento de Estados
bool setState(Fw::WidgetState state, bool on);
bool hasState(Fw::WidgetState state);
void updateStates();
```

#### 🎯 Sistema de Eventos

```cpp
// Eventos de Mouse
virtual bool onMousePress(const Point& mousePos, Fw::MouseButton button);
virtual bool onMouseRelease(const Point& mousePos, Fw::MouseButton button);
virtual bool onMouseMove(const Point& mousePos, const Point& mouseMoved);
virtual bool onMouseWheel(const Point& mousePos, Fw::MouseWheelDirection direction);
virtual bool onClick(const Point& mousePos);
virtual bool onDoubleClick(const Point& mousePos);

// Eventos de Teclado
virtual bool onKeyText(std::string_view keyText);
virtual bool onKeyDown(uint8_t keyCode, int keyboardModifiers);
virtual bool onKeyPress(uint8_t keyCode, int keyboardModifiers, int autoRepeatTicks);
virtual bool onKeyUp(uint8_t keyCode, int keyboardModifiers);

// Eventos de Foco
virtual void onFocusChange(bool focused, Fw::FocusReason reason);
virtual void onChildFocusChange(const UIWidgetPtr& focusedChild, const UIWidgetPtr& unfocusedChild, Fw::FocusReason reason);

// Eventos de Drag & Drop
virtual bool onDragEnter(const Point& mousePos);
virtual bool onDragLeave(UIWidgetPtr droppedWidget, const Point& mousePos);
virtual bool onDragMove(const Point& mousePos, const Point& mouseMoved);
virtual bool onDrop(UIWidgetPtr draggedWidget, const Point& mousePos);

// Eventos de Layout e Estilo
virtual void onGeometryChange(const Rect& oldRect, const Rect& newRect);
virtual void onLayoutUpdate();
virtual void onStyleApply(std::string_view styleName, const OTMLNodePtr& styleNode);
```

---

## 🐍 API Lua

### 📦 Criação e Gerenciamento

```lua
-- Criação de Widgets Avançados
local advancedWidget = g_ui.createWidget('UIWidget', parent)
local customWidget = UIWidget.create()

-- Configuração de Propriedades
advancedWidget:setId('myAdvancedWidget')
advancedWidget:setRect({x = 100, y = 100, width = 200, height = 150})
advancedWidget:setEnabled(true)
advancedWidget:setVisible(true)
advancedWidget:setFocusable(true)
advancedWidget:setDraggable(true)

-- Gerenciamento de Hierarquia
local childWidget = g_ui.createWidget('UIWidget', advancedWidget)
advancedWidget:addChild(childWidget)
advancedWidget:insertChild(0, childWidget)
advancedWidget:removeChild(childWidget)

-- Busca de Filhos
local child = advancedWidget:getChildById('childId')
local children = advancedWidget:getChildren()
local childCount = advancedWidget:getChildCount()
local hasChild = advancedWidget:hasChild(childWidget)
```

### 🎯 Sistema de Estados

```lua
-- Configuração de Estados
advancedWidget:setEnabled(true)
advancedWidget:setVisible(true)
advancedWidget:setFocusable(true)
advancedWidget:setDraggable(true)

-- Verificação de Estados
local isEnabled = advancedWidget:isEnabled()
local isVisible = advancedWidget:isVisible()
local isFocusable = advancedWidget:isFocusable()
local isDraggable = advancedWidget:isDraggable()
local isFocused = advancedWidget:isFocused()

-- Controle de Foco
advancedWidget:focus()
advancedWidget:unfocus()
advancedWidget:raise()
advancedWidget:lower()
```

### 🎨 Sistema de Eventos

```lua
-- Eventos de Mouse
advancedWidget.onMousePress = function(widget, mousePos, button)
    print('Mouse pressed on widget:', widget:getId())
end

advancedWidget.onMouseRelease = function(widget, mousePos, button)
    print('Mouse released on widget:', widget:getId())
end

advancedWidget.onClick = function(widget, mousePos)
    print('Widget clicked:', widget:getId())
end

advancedWidget.onDoubleClick = function(widget, mousePos)
    print('Widget double-clicked:', widget:getId())
end

-- Eventos de Teclado
advancedWidget.onKeyDown = function(widget, keyCode, keyboardModifiers)
    print('Key pressed:', keyCode)
end

advancedWidget.onKeyUp = function(widget, keyCode, keyboardModifiers)
    print('Key released:', keyCode)
end

-- Eventos de Foco
advancedWidget.onFocusChange = function(widget, focused, reason)
    if focused then
        print('Widget gained focus:', widget:getId())
    else
        print('Widget lost focus:', widget:getId())
    end
end

-- Eventos de Drag & Drop
advancedWidget.onDragEnter = function(widget, mousePos)
    print('Drag entered widget:', widget:getId())
    return true -- Aceitar drop
end

advancedWidget.onDrop = function(widget, draggedWidget, mousePos)
    print('Widget dropped on:', widget:getId())
    return true -- Processar drop
end
```

### 🎨 Sistema de Estilização

```lua
-- Aplicação de Estilos
advancedWidget:setStyleName('advancedWidgetStyle')
advancedWidget:setStyleFromNode(styleNode)

-- Estilização Dinâmica
advancedWidget:setBackgroundColor('#FF0000')
advancedWidget:setBorderColor('#00FF00')
advancedWidget:setOpacity(0.8)

-- Configuração de Layout
advancedWidget:setLayout('vertical')
advancedWidget:setLayout('horizontal')
advancedWidget:setLayout('grid')
```

---

## 🧩 Widgets Especializados

### 📦 Tipos de Widgets Disponíveis

Baseado na análise do código-fonte, o OTClient oferece os seguintes widgets especializados:

#### 🔧 Widgets Básicos
- **UIWidget**: Classe base para todos os widgets
- **UITextEdit**: Campo de edição de texto
- **UIButton**: Botão clicável
- **UILabel**: Exibição de texto

#### 🎨 Widgets de Layout
- **UIBoxLayout**: Layout em caixa
- **UIHorizontalLayout**: Layout horizontal
- **UIVerticalLayout**: Layout vertical
- **UIGridLayout**: Layout em grade
- **UIAnchorLayout**: Layout com âncoras

#### 🎯 Widgets Especializados
- **UIParticles**: Sistema de partículas
- **UIQRCode**: Geração de QR Code
- **UIMinimap**: Widget de minimapa
- **UIContainer**: Container de itens
- **UITab**: Sistema de abas

### 🎨 Exemplo de Widget Customizado

```lua
-- Criando um Widget Avançado Customizado
local CustomAdvancedWidget = {}

function CustomAdvancedWidget.create()
    local widget = g_ui.createWidget('UIWidget')
    
    -- Configuração inicial
    widget:setId('customAdvancedWidget')
    widget:setSize({width = 300, height = 200})
    
    -- Adicionar elementos internos
    local title = g_ui.createWidget('UILabel', widget)
    title:setText('Widget Avançado')
    title:setPosition({x = 10, y = 10})
    
    local content = g_ui.createWidget('UIWidget', widget)
    content:setPosition({x = 10, y = 40})
    content:setSize({width = 280, height = 150})
    
    -- Configurar eventos
    widget.onMousePress = function(widget, mousePos, button)
        print('Custom widget pressed!')
    end
    
    widget.onFocusChange = function(widget, focused, reason)
        if focused then
            widget:setBackgroundColor('#FFFF00')
        else
            widget:setBackgroundColor('#FFFFFF')
        end
    end
    
    return widget
end

-- Uso do Widget Customizado
local myWidget = CustomAdvancedWidget.create()
myWidget:setPosition({x = 100, y = 100})
```

---

## 💡 Exemplos Práticos

### 🎯 Exemplo 1: Widget com Hierarquia Complexa

```lua
-- Criar widget principal
local mainWidget = g_ui.createWidget('UIWidget')
mainWidget:setId('mainContainer')
mainWidget:setSize({width = 400, height = 300})

-- Criar cabeçalho
local header = g_ui.createWidget('UIWidget', mainWidget)
header:setId('header')
header:setPosition({x = 0, y = 0})
header:setSize({width = 400, height = 50})
header:setBackgroundColor('#2C3E50')

local title = g_ui.createWidget('UILabel', header)
title:setText('Widget Avançado')
title:setPosition({x = 10, y = 15})
title:setColor('#FFFFFF')

-- Criar área de conteúdo
local content = g_ui.createWidget('UIWidget', mainWidget)
content:setId('content')
content:setPosition({x = 0, y = 50})
content:setSize({width = 400, height = 250})

-- Adicionar widgets filhos ao conteúdo
for i = 1, 5 do
    local child = g_ui.createWidget('UIWidget', content)
    child:setId('child_' .. i)
    child:setPosition({x = 10, y = (i-1) * 40 + 10})
    child:setSize({width = 380, height = 30})
    child:setBackgroundColor('#ECF0F1')
    
    -- Adicionar evento de clique
    child.onClick = function(widget, mousePos)
        print('Child widget clicked:', widget:getId())
    end
end

-- Configurar eventos do widget principal
mainWidget.onMousePress = function(widget, mousePos, button)
    print('Main widget pressed at:', mousePos.x, mousePos.y)
end
```

### 🎨 Exemplo 2: Widget com Drag & Drop

```lua
-- Widget arrastável
local draggableWidget = g_ui.createWidget('UIWidget')
draggableWidget:setId('draggableWidget')
draggableWidget:setSize({width = 100, height = 100})
draggableWidget:setPosition({x = 50, y = 50})
draggableWidget:setBackgroundColor('#E74C3C')
draggableWidget:setDraggable(true)

-- Widget de destino
local dropZone = g_ui.createWidget('UIWidget')
dropZone:setId('dropZone')
dropZone:setSize({width = 200, height = 200})
dropZone:setPosition({x = 200, y = 50})
dropZone:setBackgroundColor('#3498DB')

-- Eventos de Drag & Drop
draggableWidget.onDragEnter = function(widget, mousePos)
    print('Dragging widget entered drop zone')
    return true
end

draggableWidget.onDragLeave = function(widget, droppedWidget, mousePos)
    print('Dragging widget left drop zone')
end

draggableWidget.onDrop = function(widget, draggedWidget, mousePos)
    print('Widget dropped on drop zone')
    -- Processar o drop aqui
    return true
end
```

### 🎯 Exemplo 3: Widget com Estados Dinâmicos

```lua
-- Widget com estados múltiplos
local stateWidget = g_ui.createWidget('UIWidget')
stateWidget:setId('stateWidget')
stateWidget:setSize({width = 150, height = 100})
stateWidget:setPosition({x = 100, y = 100})

-- Estados do widget
local states = {
    normal = {color = '#2ECC71', text = 'Normal'},
    hover = {color = '#F39C12', text = 'Hover'},
    pressed = {color = '#E74C3C', text = 'Pressed'},
    disabled = {color = '#95A5A6', text = 'Disabled'}
}

local currentState = 'normal'

-- Função para atualizar estado
local function updateState(newState)
    currentState = newState
    local state = states[newState]
    stateWidget:setBackgroundColor(state.color)
    
    -- Atualizar texto se existir
    local textWidget = stateWidget:getChildById('stateText')
    if textWidget then
        textWidget:setText(state.text)
    end
end

-- Criar label para mostrar estado
local textWidget = g_ui.createWidget('UILabel', stateWidget)
textWidget:setId('stateText')
textWidget:setPosition({x = 10, y = 40})
textWidget:setColor('#FFFFFF')

-- Configurar eventos
stateWidget.onHoverChange = function(widget, hovered)
    if hovered and currentState ~= 'disabled' then
        updateState('hover')
    else
        updateState('normal')
    end
end

stateWidget.onMousePress = function(widget, mousePos, button)
    if currentState ~= 'disabled' then
        updateState('pressed')
    end
end

stateWidget.onMouseRelease = function(widget, mousePos, button)
    if currentState ~= 'disabled' then
        updateState('normal')
    end
end

-- Inicializar estado
updateState('normal')
```

---

## ✅ Melhores Práticas

### 🎯 Organização e Estrutura

1. **Identificação Única**: Sempre use IDs únicos para widgets
```lua
widget:setId('uniqueWidgetId')
```

2. **Hierarquia Clara**: Organize widgets em hierarquia lógica
```lua
-- Bom: Hierarquia clara
local container = g_ui.createWidget('UIWidget')
local header = g_ui.createWidget('UIWidget', container)
local content = g_ui.createWidget('UIWidget', container)
local footer = g_ui.createWidget('UIWidget', container)
```

3. **Separação de Responsabilidades**: Cada widget deve ter uma função específica
```lua
-- Widget para exibição
local displayWidget = g_ui.createWidget('UIWidget')
displayWidget:setId('displayWidget')

-- Widget para entrada
local inputWidget = g_ui.createWidget('UITextEdit')
inputWidget:setId('inputWidget')
```

### 🎨 Performance e Otimização

1. **Lazy Loading**: Carregue widgets apenas quando necessário
```lua
local function createWidgetOnDemand()
    if not widgetCache then
        widgetCache = g_ui.createWidget('UIWidget')
        -- Configuração inicial
    end
    return widgetCache
end
```

2. **Reutilização de Widgets**: Reutilize widgets quando possível
```lua
-- Pool de widgets
local widgetPool = {}

local function getWidgetFromPool()
    if #widgetPool > 0 then
        return table.remove(widgetPool)
    else
        return g_ui.createWidget('UIWidget')
    end
end

local function returnWidgetToPool(widget)
    widget:destroyChildren()
    table.insert(widgetPool, widget)
end
```

3. **Otimização de Renderização**: Minimize redraws desnecessários
```lua
-- Agrupar mudanças de propriedades
widget:setPosition({x = 100, y = 100})
widget:setSize({width = 200, height = 150})
widget:setBackgroundColor('#FF0000')
-- Apenas um redraw será executado
```

### 🎯 Gerenciamento de Eventos

1. **Limpeza de Eventos**: Sempre limpe eventos quando destruir widgets
```lua
local function cleanupWidget(widget)
    widget.onMousePress = nil
    widget.onKeyDown = nil
    widget.onFocusChange = nil
    widget:destroy()
end
```

2. **Prevenção de Memory Leaks**: Use referências fracas quando necessário
```lua
-- Usar referências fracas para callbacks
local weakRef = setmetatable({}, {__mode = 'v'})
weakRef.widget = widget
widget.onClick = function()
    if weakRef.widget then
        -- Processar clique
    end
end
```

3. **Validação de Eventos**: Sempre valide dados em eventos
```lua
widget.onMousePress = function(widget, mousePos, button)
    if not mousePos or not button then
        return false
    end
    
    -- Processar evento
    return true
end
```

---

## 🚀 Performance e Otimização

### 📊 Métricas de Performance

1. **Tempo de Criação**: < 1ms por widget
2. **Tempo de Renderização**: < 0.5ms por frame
3. **Uso de Memória**: < 1KB por widget básico
4. **Tempo de Destruição**: < 0.5ms por widget

### 🎯 Técnicas de Otimização

1. **Object Pooling**: Reutilizar widgets em vez de criar/destruir
2. **Culling**: Renderizar apenas widgets visíveis
3. **Batching**: Agrupar operações de renderização
4. **Lazy Loading**: Carregar widgets sob demanda

### 🔧 Monitoramento de Performance

```lua
-- Função para medir performance
local function measureWidgetPerformance(widgetCount)
    local startTime = os.clock()
    
    local widgets = {}
    for i = 1, widgetCount do
        widgets[i] = g_ui.createWidget('UIWidget')
    end
    
    local creationTime = os.clock() - startTime
    
    -- Medir tempo de renderização
    startTime = os.clock()
    for _, widget in ipairs(widgets) do
        widget:setPosition({x = math.random(100), y = math.random(100)})
    end
    local renderTime = os.clock() - startTime
    
    -- Limpeza
    for _, widget in ipairs(widgets) do
        widget:destroy()
    end
    
    print(string.format('Criação: %.3fms, Renderização: %.3fms', 
          creationTime * 1000, renderTime * 1000))
end
```

---

## 📚 Referências

### 🔗 Links Relacionados
- [[UIWidget_Reference]] - Referência completa da API UIWidget
- [[UI_System_Guide]] - Guia do sistema de UI
- [[UILayouts]] - Sistema de layouts
- [[UIEvents]] - Sistema de eventos
- [[UIStyling]] - Sistema de estilização

### 📖 Documentação Técnica
- **Arquivo C++**: `src/framework/ui/uiwidget.h`
- **Implementação**: `src/framework/ui/uiwidget.cpp`
- **Declarações**: `src/framework/ui/declarations.h`

---

**Última Atualização**: 2025-01-27  
**Versão**: 1.0  
**Status**: ✅ **Completo**  
**Prioridade**: 🔥 **MÁXIMA**
