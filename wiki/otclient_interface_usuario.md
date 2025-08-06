---
tags: [otclient, ui, interface, usuario, wikipedia, habdel]
type: wikipedia
status: active
priority: alta
created: 2025-08-05
updated: 2025-08-05
aliases: [Interface Usuário OTClient, UI OTClient, OTClient User Interface]
---

# 🖥️ **Interface do Usuário - OTClient**

> [!info] **Baseado na pesquisa Habdel**
> Esta página é baseada na pesquisa detalhada da **OTCLIENT-007** realizada pelo sistema Habdel.

---

## 🎯 **Visão Geral**

O **Sistema de Interface do Usuário (UI)** do OTClient é responsável por toda a apresentação visual e interação com o usuário. Baseado em um sistema de widgets hierárquico e um motor de layout flexível, permite criar interfaces complexas e responsivas usando tanto código Lua quanto arquivos OTUI.

### **Características Principais**
- **Sistema de Widgets**: Componentes reutilizáveis e customizáveis
- **Layouts Flexíveis**: Ancoragem, grid, horizontal, vertical e box layouts
- **Sistema de Estilos**: Temas e estilos centralizados
- **Eventos Interativos**: Cliques, arrastar, teclado e mouse
- **Renderização Otimizada**: Sistema de draw pools para performance
- **Suporte a OTUI**: Linguagem declarativa para interfaces

---

## 🏗️ **Arquitetura do Sistema**

### **Estrutura Hierárquica**
```
UI System (C++/Lua)
├── UIManager (Gerenciamento Global)
├── UIWidget (Widget Base)
├── Layouts (Sistema de Layout)
│   ├── AnchorLayout (Ancoragem)
│   ├── GridLayout (Grid)
│   ├── HorizontalLayout (Horizontal)
│   ├── VerticalLayout (Vertical)
│   └── BoxLayout (Box)
├── Widgets Especializados
│   ├── UIButton (Botões)
│   ├── UITextEdit (Edição de Texto)
│   ├── UIWindow (Janelas)
│   ├── UIImage (Imagens)
│   └── UIText (Texto)
└── Style System (Sistema de Estilos)
```

### **Componentes Principais**

#### **1. UIManager (`src/framework/ui/uimanager.cpp`)**
```cpp
// Gerenciador global da interface
class UIManager {
    // Gerenciamento de widgets
    // Sistema de layouts
    // Renderização e atualização
    // Eventos de mouse e teclado
};
```

#### **2. UIWidget (`src/framework/ui/uiwidget.cpp`)**
```cpp
// Widget base para todos os componentes
class UIWidget {
    // Propriedades básicas (posição, tamanho, visibilidade)
    // Sistema de eventos
    // Gerenciamento de filhos
    // Estilos e temas
};
```

#### **3. Sistema de Layouts**
```cpp
// Layout de ancoragem (mais flexível)
class UIAnchorLayout : public UILayout {
    // Ancoragem de widgets aos cantos/centro
    // Redimensionamento automático
};

// Layout em grid
class UIGridLayout : public UILayout {
    // Organização em linhas e colunas
    // Espaçamento configurável
};
```

---

## 🔧 **APIs e Interfaces**

### **Criação e Gerenciamento de Widgets**

#### **Criação de Widgets**
```lua
-- Criar widget básico
local widget = g_ui.createWidget('UIWidget')

-- Criar widget com pai
local button = g_ui.createWidget('UIButton', parentWidget)

-- Criar widget por ID
local widget = g_ui.getWidgetById('meuWidget')

-- Criar widget a partir de OTUI
local widget = g_ui.createWidgetFromOTUI('interface.otui', 'widgetName')
```

#### **Propriedades de Widgets**
```lua
-- Posição e tamanho
widget:setPosition({ x = 10, y = 20 })
widget:setSize({ width = 200, height = 100 })
widget:setRect({ x = 10, y = 20, width = 200, height = 100 })

-- Visibilidade
widget:setVisible(true)
widget:setEnabled(true)
widget:setFocusable(true)

-- Estilo e aparência
widget:setId('meuWidget')
widget:setText('Texto do Widget')
widget:setImageSource('imagem.png')
widget:setColor('#FF0000')
widget:setOpacity(0.8)
```

### **Sistema de Layouts**

#### **AnchorLayout (Ancoragem)**
```lua
-- Layout mais flexível - ancoragem aos cantos
local layout = g_ui.createWidget('UIAnchorLayout')
layout:addChild(widget, { 
    anchorTop = true, 
    anchorBottom = true,
    anchorLeft = true,
    anchorRight = true 
})

-- Ancoragem específica
layout:addChild(widget, { 
    anchorTop = true, 
    anchorLeft = true,
    marginTop = 10,
    marginLeft = 10
})
```

#### **GridLayout (Grid)**
```lua
-- Layout em grid
local grid = g_ui.createWidget('UIGridLayout')
grid:setCellSize({ width = 50, height = 50 })
grid:setCellSpacing(5)

-- Adicionar widgets ao grid
grid:addChild(widget1, { x = 0, y = 0 })
grid:addChild(widget2, { x = 1, y = 0 })
grid:addChild(widget3, { x = 0, y = 1 })
```

#### **HorizontalLayout e VerticalLayout**
```lua
-- Layout horizontal
local hLayout = g_ui.createWidget('UIHorizontalLayout')
hLayout:setSpacing(10)
hLayout:addChild(widget1)
hLayout:addChild(widget2)

-- Layout vertical
local vLayout = g_ui.createWidget('UIVerticalLayout')
vLayout:setSpacing(5)
vLayout:addChild(widget1)
vLayout:addChild(widget2)
```

### **Widgets Especializados**

#### **UIButton (Botões)**
```lua
-- Criar botão
local button = g_ui.createWidget('UIButton')
button:setText('Clique Aqui')
button:setImageSource('button.png')

-- Eventos de botão
connect(button, { 
    onClick = function()
        print('Botão clicado!')
    end,
    onPress = function()
        print('Botão pressionado!')
    end,
    onRelease = function()
        print('Botão solto!')
    end
})
```

#### **UITextEdit (Edição de Texto)**
```lua
-- Criar campo de texto
local textEdit = g_ui.createWidget('UITextEdit')
textEdit:setText('Texto inicial')
textEdit:setMaxLength(100)
textEdit:setMultiline(true)

-- Eventos de texto
connect(textEdit, {
    onTextChange = function(widget, text)
        print('Texto alterado:', text)
    end,
    onEnter = function(widget)
        print('Enter pressionado')
    end
})
```

#### **UIWindow (Janelas)**
```lua
-- Criar janela
local window = g_ui.createWidget('UIWindow')
window:setText('Minha Janela')
window:setSize({ width = 400, height = 300 })
window:setDraggable(true)
window:setResizable(true)

-- Mostrar/ocultar janela
window:show()
window:hide()
window:close()
```

---

## 📚 **Exemplos Práticos**

### **Exemplo 1: Interface de Login**
```lua
-- Criar janela de login
local loginWindow = g_ui.createWidget('UIWindow')
loginWindow:setText('Login')
loginWindow:setSize({ width = 300, height = 200 })
loginWindow:setDraggable(true)

-- Layout vertical para organizar elementos
local layout = g_ui.createWidget('UIVerticalLayout', loginWindow)
layout:setSpacing(10)
layout:setMargin(20)

-- Campo de usuário
local userLabel = g_ui.createWidget('UIText', layout)
userLabel:setText('Usuário:')
userLabel:setTextAlign('left')

local userEdit = g_ui.createWidget('UITextEdit', layout)
userEdit:setPlaceholder('Digite seu usuário')

-- Campo de senha
local passLabel = g_ui.createWidget('UIText', layout)
passLabel:setText('Senha:')
passLabel:setTextAlign('left')

local passEdit = g_ui.createWidget('UITextEdit', layout)
passEdit:setPassword(true)
passEdit:setPlaceholder('Digite sua senha')

-- Botões
local buttonLayout = g_ui.createWidget('UIHorizontalLayout', layout)
buttonLayout:setSpacing(10)

local loginButton = g_ui.createWidget('UIButton', buttonLayout)
loginButton:setText('Entrar')

local cancelButton = g_ui.createWidget('UIButton', buttonLayout)
cancelButton:setText('Cancelar')

-- Eventos
connect(loginButton, { onClick = function()
    local user = userEdit:getText()
    local pass = passEdit:getText()
    print('Login:', user, pass)
end })

connect(cancelButton, { onClick = function()
    loginWindow:close()
end })

-- Mostrar janela
loginWindow:show()
```

### **Exemplo 2: Painel de Status**
```lua
-- Criar painel de status
local statusPanel = g_ui.createWidget('UIWidget')
statusPanel:setSize({ width = 200, height = 100 })
statusPanel:setPosition({ x = 10, y = 10 })

-- Layout de ancoragem para posicionamento preciso
local layout = g_ui.createWidget('UIAnchorLayout', statusPanel)

-- Barra de vida
local healthBar = g_ui.createWidget('UIProgressBar', layout)
healthBar:setText('Vida: 100/100')
healthBar:setPercent(100)
healthBar:setColor('#00FF00')
layout:addChild(healthBar, { 
    anchorTop = true, 
    anchorLeft = true, 
    anchorRight = true,
    marginTop = 5,
    marginLeft = 5,
    marginRight = 5
})

-- Barra de mana
local manaBar = g_ui.createWidget('UIProgressBar', layout)
manaBar:setText('Mana: 50/100')
manaBar:setPercent(50)
manaBar:setColor('#0000FF')
layout:addChild(manaBar, { 
    anchorTop = true, 
    anchorLeft = true, 
    anchorRight = true,
    marginTop = 30,
    marginLeft = 5,
    marginRight = 5
})

-- Barra de experiência
local expBar = g_ui.createWidget('UIProgressBar', layout)
expBar:setText('Exp: 75%')
expBar:setPercent(75)
expBar:setColor('#FFFF00')
layout:addChild(expBar, { 
    anchorTop = true, 
    anchorLeft = true, 
    anchorRight = true,
    marginTop = 55,
    marginLeft = 5,
    marginRight = 5
})
```

### **Exemplo 3: Menu Contextual**
```lua
-- Criar menu contextual
local contextMenu = g_ui.createWidget('UIWidget')
contextMenu:setSize({ width = 150, height = 100 })
contextMenu:setVisible(false)

-- Layout vertical para itens do menu
local layout = g_ui.createWidget('UIVerticalLayout', contextMenu)

-- Itens do menu
local item1 = g_ui.createWidget('UIButton', layout)
item1:setText('Opção 1')
item1:setTextAlign('left')

local item2 = g_ui.createWidget('UIButton', layout)
item2:setText('Opção 2')
item2:setTextAlign('left')

local item3 = g_ui.createWidget('UIButton', layout)
item3:setText('Opção 3')
item3:setTextAlign('left')

-- Função para mostrar menu
function showContextMenu(x, y)
    contextMenu:setPosition({ x = x, y = y })
    contextMenu:setVisible(true)
    contextMenu:focus()
end

-- Função para ocultar menu
function hideContextMenu()
    contextMenu:setVisible(false)
end

-- Eventos dos itens
connect(item1, { onClick = function()
    print('Opção 1 selecionada')
    hideContextMenu()
end })

connect(item2, { onClick = function()
    print('Opção 2 selecionada')
    hideContextMenu()
end })

connect(item3, { onClick = function()
    print('Opção 3 selecionada')
    hideContextMenu()
end })

-- Ocultar menu quando perder foco
connect(contextMenu, { onFocusChange = function(widget, focused)
    if not focused then
        hideContextMenu()
    end
end })
```

---

## 🎨 **Sistema de Estilos**

### **Definição de Estilos**
```lua
-- Definir estilo customizado
g_ui.createStyle('CustomButton', {
    background = '#4A90E2',
    color = '#FFFFFF',
    border = '#2E5C8A',
    borderWidth = 2,
    borderRadius = 5,
    padding = 10,
    font = 'verdana-11px-antialised'
})

-- Aplicar estilo
local button = g_ui.createWidget('UIButton')
button:setStyleName('CustomButton')
```

### **Temas**
```lua
-- Carregar tema
g_ui.loadStyle('themes/dark.otui')

-- Alternar tema
g_ui.setStyle('themes/light.otui')
```

---

## 🔗 **Dependências e Integração**

### **Dependências Internas**
- **UIManager**: Gerenciamento global de widgets
- **UIWidget**: Widget base para todos os componentes
- **Layout System**: Sistema de layouts flexível
- **Style System**: Sistema de estilos e temas
- **Event System**: Sistema de eventos interativos

### **Integração com Outros Sistemas**
- **Sistema de Gráficos**: Renderização de widgets
- **Sistema de Input**: Mouse e teclado
- **Sistema de Lua**: Scripting de interfaces
- **Sistema de Eventos**: Comunicação entre componentes
- **Sistema de Módulos**: Carregamento de interfaces

### **APIs Relacionadas**
```lua
-- Sistema de Gráficos
g_graphics.createTexture()
g_graphics.drawText()
g_graphics.drawRect()

-- Sistema de Input
g_mouse.isPressed()
g_keyboard.isKeyPressed()

-- Sistema de Eventos
connect(widget, events)
disconnect(widget, events)
signalcall(event, ...)
```

---

## 🚀 **Melhores Práticas**

### **1. Estrutura de Widgets**
```lua
-- Use layouts apropriados para organização
local container = g_ui.createWidget('UIWidget')
local layout = g_ui.createWidget('UIVerticalLayout', container)

-- Adicione widgets ao layout
layout:addChild(widget1)
layout:addChild(widget2)
```

### **2. Gerenciamento de Eventos**
```lua
-- Sempre desconecte eventos
local connections = {}

function init()
    connections.click = connect(button, { onClick = onButtonClick })
end

function terminate()
    for _, connection in pairs(connections) do
        disconnect(connection)
    end
end
```

### **3. Performance**
```lua
-- Cache de widgets frequentemente usados
local cachedWidget = g_ui.getWidgetById('meuWidget')

-- Use setVisible em vez de destroy/create
widget:setVisible(false) -- Ocultar
widget:setVisible(true)  -- Mostrar
```

### **4. Responsividade**
```lua
-- Use AnchorLayout para interfaces responsivas
local layout = g_ui.createWidget('UIAnchorLayout')
layout:addChild(widget, { 
    anchorTop = true, 
    anchorBottom = true,
    anchorLeft = true,
    anchorRight = true 
})
```

---

## 🔍 **Debugging e Desenvolvimento**

### **Ferramentas de Debug**
```lua
-- Inspeção de widgets
print(dump(widget))

-- Verificar hierarquia
function printWidgetTree(widget, level)
    level = level or 0
    local indent = string.rep('  ', level)
    print(indent .. widget:getId() .. ' (' .. widget:getClassName() .. ')')
    
    for _, child in pairs(widget:getChildren()) do
        printWidgetTree(child, level + 1)
    end
end

-- Listar todos os widgets
printWidgetTree(g_ui.getRootWidget())
```

### **Desenvolvimento de Interfaces**
```lua
-- Recarregar interface durante desenvolvimento
g_ui.reloadStyle()

-- Verificar widgets por ID
local widget = g_ui.getWidgetById('meuWidget')
if widget then
    print('Widget encontrado:', widget:getClassName())
else
    print('Widget não encontrado')
end
```

---

## 📖 **Referência Completa**

### **Widgets Disponíveis**
- `UIWidget` - Widget base
- `UIButton` - Botões
- `UITextEdit` - Edição de texto
- `UIWindow` - Janelas
- `UIImage` - Imagens
- `UIText` - Texto
- `UIProgressBar` - Barras de progresso
- `UIScrollBar` - Barras de rolagem
- `UIList` - Listas
- `UIComboBox` - Caixas de seleção

### **Layouts Disponíveis**
- `UIAnchorLayout` - Layout de ancoragem
- `UIGridLayout` - Layout em grid
- `UIHorizontalLayout` - Layout horizontal
- `UIVerticalLayout` - Layout vertical
- `UIBoxLayout` - Layout em caixa

### **APIs Principais**
- `g_ui.createWidget(type, parent)`
- `g_ui.getWidgetById(id)`
- `g_ui.getRootWidget()`
- `g_ui.createWidgetFromOTUI(file, name)`
- `g_ui.loadStyle(file)`
- `g_ui.setStyle(file)`
- `widget:setPosition(pos)`
- `widget:setSize(size)`
- `widget:setVisible(visible)`
- `widget:setText(text)`
- `widget:setImageSource(source)`
- `widget:setStyleName(name)`
- `widget:show()`
- `widget:hide()`
- `widget:close()`
- `widget:focus()`
- `widget:addChild(child)`
- `widget:removeChild(child)`
- `connect(widget, events)`
- `disconnect(widget, events)`

---

## 🎯 **Conclusão**

O **Sistema de Interface do Usuário** do OTClient fornece uma base sólida e flexível para criação de interfaces ricas e interativas. Com seu sistema de widgets hierárquico, layouts flexíveis e integração profunda com Lua, permite que desenvolvedores criem experiências de usuário sofisticadas.

### **Próximos Passos**
- Explore os widgets disponíveis
- Experimente com diferentes layouts
- Desenvolva interfaces personalizadas
- Integre com outros sistemas do OTClient

---

## 🔗 **Links Relacionados**

- [[otclient_arquitetura_core|Arquitetura Core do OTClient]]
- [[otclient_sistema_lua|Sistema de Lua]]
- [[otclient_sistema_modulos|Sistema de Módulos]]
- [[otclient_sistema_graficos|Sistema de Gráficos]]
- [[otclient_sistema_rede|Sistema de Rede]]

---

*Baseado na pesquisa Habdel: OTCLIENT-007 - Interface do Usuário* 