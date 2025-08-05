# Sistema de Layouts UIWidget

O sistema de layouts do OTClient fornece mecanismos poderosos para organizar e posicionar widgets automaticamente, criando interfaces responsivas e bem estruturadas.

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Tipos de Layout](#tipos-de-layout)
3. [Sistema de Âncoras](#sistema-de-âncoras)
4. [Layouts de Caixa](#layouts-de-caixa)
5. [Layout de Grade](#layout-de-grade)
6. [Margens e Padding](#margens-e-padding)
7. [Exemplos Práticos](#exemplos-práticos)
8. [Melhores Práticas](#melhores-práticas)

## 🎯 Visão Geral

O sistema de layouts do OTClient oferece múltiplas abordagens para posicionamento:

- **Posicionamento Manual**: Coordenadas fixas (x, y)
- **Sistema de Âncoras**: Posicionamento relativo a outros widgets
- **Layouts Automáticos**: Organizações predefinidas (vertical, horizontal, grade)
- **Layouts Híbridos**: Combinação de diferentes técnicas

### 🏗️ Hierarquia de Layout

```
UIWidget (base)
├── Manual Positioning
├── Anchor System
└── Automatic Layouts
    ├── UIAnchorLayout (padrão)
    ├── UIVerticalLayout
    ├── UIHorizontalLayout
    └── UIGridLayout
```

## 🔧 Tipos de Layout

### 1. **UIAnchorLayout** (Padrão)

Layout baseado em âncoras que permite posicionamento relativo sofisticado.

#### Nível Basic
```lua
-- Âncoras são adicionadas automaticamente ao widget
-- Não precisa criar explicitamente o UIAnchorLayout
local widget = g_ui.createWidget('UIWidget', parent)
widget:addAnchor(AnchorTop, 'parent', AnchorTop)
widget:addAnchor(AnchorLeft, 'parent', AnchorLeft)
```

#### Nível Intermediate
```lua
-- Âncoras são adicionadas automaticamente ao widget
-- Não precisa criar explicitamente o UIAnchorLayout
local widget = g_ui.createWidget('UIWidget', parent)
widget:addAnchor(AnchorTop, 'parent', AnchorTop)
widget:addAnchor(AnchorLeft, 'parent', AnchorLeft)
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
-- Âncoras são adicionadas automaticamente ao widget
-- Não precisa criar explicitamente o UIAnchorLayout
local widget = g_ui.createWidget('UIWidget', parent)
widget:addAnchor(AnchorTop, 'parent', AnchorTop)
widget:addAnchor(AnchorLeft, 'parent', AnchorLeft)
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

### 2. **UIVerticalLayout**

Organiza widgets filhos verticalmente (um abaixo do outro).

#### Nível Basic
```lua
local container = g_ui.createWidget('UIWidget', parent)
local layout = UIVerticalLayout.create(container)
container:setLayout(layout)

-- Configurações do layout vertical
layout:setSpacing(5)           -- Espaço entre widgets
layout:setFitChildren(true)    -- Redimensiona container para caber filhos
layout:setAlignBottom(true)    -- Alinha filhos na parte inferior
```

#### Nível Intermediate
```lua
local container = g_ui.createWidget('UIWidget', parent)
local layout = UIVerticalLayout.create(container)
container:setLayout(layout)

-- Configurações do layout vertical
layout:setSpacing(5)           -- Espaço entre widgets
layout:setFitChildren(true)    -- Redimensiona container para caber filhos
layout:setAlignBottom(true)    -- Alinha filhos na parte inferior
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
local container = g_ui.createWidget('UIWidget', parent)
local layout = UIVerticalLayout.create(container)
container:setLayout(layout)

-- Configurações do layout vertical
layout:setSpacing(5)           -- Espaço entre widgets
layout:setFitChildren(true)    -- Redimensiona container para caber filhos
layout:setAlignBottom(true)    -- Alinha filhos na parte inferior
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

### 3. **UIHorizontalLayout**

Organiza widgets filhos horizontalmente (lado a lado).

#### Nível Basic
```lua
local container = g_ui.createWidget('UIWidget', parent)
local layout = UIHorizontalLayout.create(container)
container:setLayout(layout)

-- Configurações do layout horizontal
layout:setSpacing(10)          -- Espaço entre widgets
layout:setFitChildren(true)    -- Redimensiona container
layout:setAlignRight(true)     -- Alinha filhos à direita
```

#### Nível Intermediate
```lua
local container = g_ui.createWidget('UIWidget', parent)
local layout = UIHorizontalLayout.create(container)
container:setLayout(layout)

-- Configurações do layout horizontal
layout:setSpacing(10)          -- Espaço entre widgets
layout:setFitChildren(true)    -- Redimensiona container
layout:setAlignRight(true)     -- Alinha filhos à direita
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
local container = g_ui.createWidget('UIWidget', parent)
local layout = UIHorizontalLayout.create(container)
container:setLayout(layout)

-- Configurações do layout horizontal
layout:setSpacing(10)          -- Espaço entre widgets
layout:setFitChildren(true)    -- Redimensiona container
layout:setAlignRight(true)     -- Alinha filhos à direita
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

### 4. **UIGridLayout**

Organiza widgets em uma grade regular.

#### Nível Basic
```lua
local container = g_ui.createWidget('UIWidget', parent)
local layout = UIGridLayout.create(container)
container:setLayout(layout)

-- Configurações da grade
layout:setCellSize({width = 50, height = 50})
layout:setCellSpacing(5)
layout:setNumColumns(4)        -- 4 colunas
layout:setFlow(true)           -- Fluxo horizontal
```

#### Nível Intermediate
```lua
local container = g_ui.createWidget('UIWidget', parent)
local layout = UIGridLayout.create(container)
container:setLayout(layout)

-- Configurações da grade
layout:setCellSize({width = 50, height = 50})
layout:setCellSpacing(5)
layout:setNumColumns(4)        -- 4 colunas
layout:setFlow(true)           -- Fluxo horizontal
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
local container = g_ui.createWidget('UIWidget', parent)
local layout = UIGridLayout.create(container)
container:setLayout(layout)

-- Configurações da grade
layout:setCellSize({width = 50, height = 50})
layout:setCellSpacing(5)
layout:setNumColumns(4)        -- 4 colunas
layout:setFlow(true)           -- Fluxo horizontal
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

## ⚓ Sistema de Âncoras

As âncoras permitem posicionamento relativo entre widgets, criando layouts responsivos.

### 📍 **Tipos de Âncora**

```lua
-- Bordas
    --  Bordas (traduzido)
AnchorTop, AnchorBottom, AnchorLeft, AnchorRight

-- Centros
    --  Centros (traduzido)
AnchorHorizontalCenter, AnchorVerticalCenter

-- Exemplos combinados
    --  Exemplos combinados (traduzido)
widget:addAnchor(AnchorTop, 'parent', AnchorTop)           -- Cola no topo do pai
widget:addAnchor(AnchorBottom, 'prev', AnchorTop)          -- Cola abaixo do widget anterior
widget:addAnchor(AnchorLeft, 'parent', AnchorLeft)         -- Cola na esquerda do pai
widget:addAnchor(AnchorRight, 'parent', AnchorRight)       -- Cola na direita do pai
```

### 🎯 **Referências de Widget**

#### Nível Basic
```lua
-- Referenciar widgets para âncoras
widget:addAnchor(AnchorTop, 'parent', AnchorTop)           -- Widget pai
widget:addAnchor(AnchorTop, 'prev', AnchorBottom)          -- Widget anterior
widget:addAnchor(AnchorTop, 'next', AnchorTop)             -- Próximo widget
widget:addAnchor(AnchorTop, 'widgetId', AnchorBottom)      -- Widget específico por ID
```

#### Nível Intermediate
```lua
-- Referenciar widgets para âncoras
widget:addAnchor(AnchorTop, 'parent', AnchorTop)           -- Widget pai
widget:addAnchor(AnchorTop, 'prev', AnchorBottom)          -- Widget anterior
widget:addAnchor(AnchorTop, 'next', AnchorTop)             -- Próximo widget
widget:addAnchor(AnchorTop, 'widgetId', AnchorBottom)      -- Widget específico por ID
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
-- Referenciar widgets para âncoras
widget:addAnchor(AnchorTop, 'parent', AnchorTop)           -- Widget pai
widget:addAnchor(AnchorTop, 'prev', AnchorBottom)          -- Widget anterior
widget:addAnchor(AnchorTop, 'next', AnchorTop)             -- Próximo widget
widget:addAnchor(AnchorTop, 'widgetId', AnchorBottom)      -- Widget específico por ID
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

### 🔧 **Métodos de Âncora**

#### Nível Basic
```lua
-- Adicionar âncora
widget:addAnchor(anchorEdge, hookedWidgetId, hookedEdge)

-- Remover âncora específica
widget:removeAnchor(AnchorTop)

-- Quebrar todas as âncoras
widget:breakAnchors()

-- Métodos de conveniência
widget:fill('parent')              -- Preenche o pai completamente
widget:centerIn('parent')          -- Centraliza no pai
```

#### Nível Intermediate
```lua
-- Adicionar âncora
widget:addAnchor(anchorEdge, hookedWidgetId, hookedEdge)

-- Remover âncora específica
widget:removeAnchor(AnchorTop)

-- Quebrar todas as âncoras
widget:breakAnchors()

-- Métodos de conveniência
widget:fill('parent')              -- Preenche o pai completamente
widget:centerIn('parent')          -- Centraliza no pai
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
-- Adicionar âncora
widget:addAnchor(anchorEdge, hookedWidgetId, hookedEdge)

-- Remover âncora específica
widget:removeAnchor(AnchorTop)

-- Quebrar todas as âncoras
widget:breakAnchors()

-- Métodos de conveniência
widget:fill('parent')              -- Preenche o pai completamente
widget:centerIn('parent')          -- Centraliza no pai
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

## 📦 Layouts de Caixa

### 🔝 **Layout Vertical**

Organiza elementos de cima para baixo.

```lua
local listContainer = g_ui.createWidget('UIWidget', parent)
listContainer:setId('verticalList')

-- Criar e configurar layout vertical
    --  Criar e configurar layout vertical (traduzido)
local verticalLayout = UIVerticalLayout.create(listContainer)
verticalLayout:setSpacing(2)
verticalLayout:setFitChildren(true)
listContainer:setLayout(verticalLayout)

-- Adicionar itens - serão organizados automaticamente
for i = 1, 5 do
    -- Loop de repetição
    local item = g_ui.createWidget('Label', listContainer)
    item:setText('Item ' .. i)
    item:setHeight(25)
end
```

### ↔️ **Layout Horizontal**

Organiza elementos da esquerda para a direita.

```lua
local buttonBar = g_ui.createWidget('UIWidget', parent)
buttonBar:setId('buttonBar')

-- Criar layout horizontal
    --  Criar layout horizontal (traduzido)
local horizontalLayout = UIHorizontalLayout.create(buttonBar)
horizontalLayout:setSpacing(10)
horizontalLayout:setAlignRight(false)  -- Alinha à esquerda
buttonBar:setLayout(horizontalLayout)

-- Adicionar botões
local actions = {'Save', 'Load', 'Cancel'}
for _, action in ipairs(actions) do
    -- Loop de repetição
    local button = g_ui.createWidget('Button', buttonBar)
    button:setText(action)
    button:setWidth(80)
end
```

## 🔷 Layout de Grade

Ideal para inventários, paletas de cores, selecionadores de ícones.

```lua
local inventoryGrid = g_ui.createWidget('UIWidget', parent)
inventoryGrid:setId('inventory')

-- Configurar layout de grade
    --  Configurar layout de grade (traduzido)
local gridLayout = UIGridLayout.create(inventoryGrid)
gridLayout:setCellSize({width = 32, height = 32})
gridLayout:setCellSpacing(1)
gridLayout:setNumColumns(8)           -- 8 colunas
gridLayout:setNumLines(6)             -- 6 linhas 
gridLayout:setFlow(true)              -- Fluxo da esquerda->direita, cima->baixo
inventoryGrid:setLayout(gridLayout)

-- Adicionar slots do inventário
for slot = 1, 48 do  -- 8x6 = 48 slots
    -- Loop de repetição
    local itemSlot = g_ui.createWidget('UIWidget', inventoryGrid)
    itemSlot:setId('slot' .. slot)
    itemSlot:setBackgroundColor('#333333')
    itemSlot:setBorderWidth(1)
    itemSlot:setBorderColor('#666666')
end
```

### ⚙️ **Configurações Avançadas de Grade**

#### Nível Basic
```lua
-- Direção do fluxo
-- Número fixo de colunas/linhas
-- Tamanho automático baseado no conteúdo
gridLayout:setUniformHeight(true)      -- Altura uniforme
gridLayout:setUniformWidth(true)       -- Largura uniforme
```

#### Nível Intermediate
```lua
-- Direção do fluxo
gridLayout:setFlow(true)               -- Horizontal primeiro
gridLayout:setFlow(false)              -- Vertical primeiro

-- Número fixo de colunas/linhas
gridLayout:setNumColumns(4)            -- Força 4 colunas
gridLayout:setNumLines(3)              -- Força 3 linhas

-- Tamanho automático baseado no conteúdo
gridLayout:setAutoSpacing(true)        -- Espaçamento automático
gridLayout:setUniformHeight(true)      -- Altura uniforme
gridLayout:setUniformWidth(true)       -- Largura uniforme
```

#### Nível Advanced
```lua
-- Direção do fluxo
gridLayout:setFlow(true)               -- Horizontal primeiro
gridLayout:setFlow(false)              -- Vertical primeiro

-- Número fixo de colunas/linhas
gridLayout:setNumColumns(4)            -- Força 4 colunas
gridLayout:setNumLines(3)              -- Força 3 linhas

-- Tamanho automático baseado no conteúdo
gridLayout:setAutoSpacing(true)        -- Espaçamento automático
gridLayout:setUniformHeight(true)      -- Altura uniforme
gridLayout:setUniformWidth(true)       -- Largura uniforme
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

## 📏 Margens e Padding

### 🔲 **Margens** (Espaço Externo)

Espaço ao redor do widget, fora de suas bordas.

```lua
-- Margem uniforme
    --  Margem uniforme (traduzido)
widget:setMargin(10)                   -- 10px em todos os lados

-- Margens específicas
widget:setMarginTop(15)
widget:setMarginRight(20)
widget:setMarginBottom(10)
widget:setMarginLeft(5)

-- Margens combinadas
    --  Margens combinadas (traduzido)
widget:setMarginHorizontal(20)         -- Esquerda e direita
widget:setMarginVertical(10)           -- Cima e baixo
```

### 🔳 **Padding** (Espaço Interno)

Espaço interno do widget, entre suas bordas e o conteúdo.

```lua
-- Padding uniforme
    --  Padding uniforme (traduzido)
widget:setPadding(8)                   -- 8px em todos os lados

-- Padding específico
widget:setPaddingTop(12)
widget:setPaddingRight(16)
widget:setPaddingBottom(8)
widget:setPaddingLeft(4)

-- Padding combinado
    --  Padding combinado (traduzido)
widget:setPaddingHorizontal(15)        -- Esquerda e direita
widget:setPaddingVertical(10)          -- Cima e baixo
```

### 📐 **Interação Margin + Padding + Layout**

#### Nível Basic
```lua
local container = g_ui.createWidget('UIWidget', parent)
container:setPadding(20)               -- Espaço interno para conteúdo

-- Layout vertical com espaçamento
local layout = UIVerticalLayout.create(container)
layout:setSpacing(5)                   -- Espaço entre filhos
container:setLayout(layout)

-- Filhos com margens individuais
local child1 = g_ui.createWidget('Label', container)
child1:setText('Primeiro item')
child1:setMarginBottom(10)             -- Margem extra abaixo

local child2 = g_ui.createWidget('Label', container)
child2:setText('Segundo item')
child2:setMarginHorizontal(15)         -- Margens laterais
```

#### Nível Intermediate
```lua
local container = g_ui.createWidget('UIWidget', parent)
container:setPadding(20)               -- Espaço interno para conteúdo

-- Layout vertical com espaçamento
local layout = UIVerticalLayout.create(container)
layout:setSpacing(5)                   -- Espaço entre filhos
container:setLayout(layout)

-- Filhos com margens individuais
local child1 = g_ui.createWidget('Label', container)
child1:setText('Primeiro item')
child1:setMarginBottom(10)             -- Margem extra abaixo

local child2 = g_ui.createWidget('Label', container)
child2:setText('Segundo item')
child2:setMarginHorizontal(15)         -- Margens laterais
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
local container = g_ui.createWidget('UIWidget', parent)
container:setPadding(20)               -- Espaço interno para conteúdo

-- Layout vertical com espaçamento
local layout = UIVerticalLayout.create(container)
layout:setSpacing(5)                   -- Espaço entre filhos
container:setLayout(layout)

-- Filhos com margens individuais
local child1 = g_ui.createWidget('Label', container)
child1:setText('Primeiro item')
child1:setMarginBottom(10)             -- Margem extra abaixo

local child2 = g_ui.createWidget('Label', container)
child2:setText('Segundo item')
child2:setMarginHorizontal(15)         -- Margens laterais
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

## 💡 Exemplos Práticos

### 📋 **Janela de Diálogo Completa**

#### Nível Basic
```lua
-- Janela principal
local dialog = g_ui.createWidget('MainWindow', rootWidget)
-- Container do conteúdo com padding
local content = g_ui.createWidget('UIWidget', dialog)
-- Layout vertical para organizar seções
local mainLayout = UIVerticalLayout.create(content)
-- Seção superior: Título
local titleLabel = g_ui.createWidget('Label', content)
-- Seção do meio: Form horizontal
local formContainer = g_ui.createWidget('UIWidget', content)
local formLayout = UIHorizontalLayout.create(formContainer)
local nameLabel = g_ui.createWidget('Label', formContainer)
local nameEdit = g_ui.createWidget('TextEdit', formContainer)
-- Seção inferior: Botões
local buttonContainer = g_ui.createWidget('UIWidget', content)
local buttonLayout = UIHorizontalLayout.create(buttonContainer)
local cancelButton = g_ui.createWidget('Button', buttonContainer)
local okButton = g_ui.createWidget('Button', buttonContainer)
```

#### Nível Intermediate
```lua
-- Janela principal
local dialog = g_ui.createWidget('MainWindow', rootWidget)
dialog:setId('exampleDialog')
dialog:setText('Layout Example')
dialog:setSize({width = 400, height = 300})
dialog:centerIn('parent')

-- Container do conteúdo com padding
local content = g_ui.createWidget('UIWidget', dialog)
content:setId('content')
content:fill('parent')
content:setPadding(20)

-- Layout vertical para organizar seções
local mainLayout = UIVerticalLayout.create(content)
mainLayout:setSpacing(15)
content:setLayout(mainLayout)

-- Seção superior: Título
local titleLabel = g_ui.createWidget('Label', content)
titleLabel:setText('Configurações')
titleLabel:setTextAlign(AlignCenter)
titleLabel:setFont('verdana-11px-monochrome')

-- Seção do meio: Form horizontal
local formContainer = g_ui.createWidget('UIWidget', content)
formContainer:setHeight(30)

local formLayout = UIHorizontalLayout.create(formContainer)
formLayout:setSpacing(10)
formContainer:setLayout(formLayout)

local nameLabel = g_ui.createWidget('Label', formContainer)
nameLabel:setText('Nome:')
nameLabel:setWidth(60)

local nameEdit = g_ui.createWidget('TextEdit', formContainer)
nameEdit:setWidth(200)

-- Seção inferior: Botões
local buttonContainer = g_ui.createWidget('UIWidget', content)
buttonContainer:setHeight(30)

local buttonLayout = UIHorizontalLayout.create(buttonContainer)
buttonLayout:setSpacing(10)
buttonLayout:setAlignRight(true)
buttonContainer:setLayout(buttonLayout)

local cancelButton = g_ui.createWidget('Button', buttonContainer)
cancelButton:setText('Cancelar')
cancelButton:setWidth(80)

local okButton = g_ui.createWidget('Button', buttonContainer)
okButton:setText('OK')
okButton:setWidth(80)
```

#### Nível Advanced
```lua
-- Janela principal
local dialog = g_ui.createWidget('MainWindow', rootWidget)
dialog:setId('exampleDialog')
dialog:setText('Layout Example')
dialog:setSize({width = 400, height = 300})
dialog:centerIn('parent')

-- Container do conteúdo com padding
local content = g_ui.createWidget('UIWidget', dialog)
content:setId('content')
content:fill('parent')
content:setPadding(20)

-- Layout vertical para organizar seções
local mainLayout = UIVerticalLayout.create(content)
mainLayout:setSpacing(15)
content:setLayout(mainLayout)

-- Seção superior: Título
local titleLabel = g_ui.createWidget('Label', content)
titleLabel:setText('Configurações')
titleLabel:setTextAlign(AlignCenter)
titleLabel:setFont('verdana-11px-monochrome')

-- Seção do meio: Form horizontal
local formContainer = g_ui.createWidget('UIWidget', content)
formContainer:setHeight(30)

local formLayout = UIHorizontalLayout.create(formContainer)
formLayout:setSpacing(10)
formContainer:setLayout(formLayout)

local nameLabel = g_ui.createWidget('Label', formContainer)
nameLabel:setText('Nome:')
nameLabel:setWidth(60)

local nameEdit = g_ui.createWidget('TextEdit', formContainer)
nameEdit:setWidth(200)

-- Seção inferior: Botões
local buttonContainer = g_ui.createWidget('UIWidget', content)
buttonContainer:setHeight(30)

local buttonLayout = UIHorizontalLayout.create(buttonContainer)
buttonLayout:setSpacing(10)
buttonLayout:setAlignRight(true)
buttonContainer:setLayout(buttonLayout)

local cancelButton = g_ui.createWidget('Button', buttonContainer)
cancelButton:setText('Cancelar')
cancelButton:setWidth(80)

local okButton = g_ui.createWidget('Button', buttonContainer)
okButton:setText('OK')
okButton:setWidth(80)
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

### 🎮 **Interface de Jogo com Múltiplos Layouts**

#### Inicialização e Configuração
```lua
-- Interface principal
local gameInterface = g_ui.createWidget('UIWidget', rootWidget)
gameInterface:setId('gameUI')
gameInterface:fill('parent')

-- Painel superior (horizontal)
local topPanel = g_ui.createWidget('UIWidget', gameInterface)
topPanel:setId('topPanel')
topPanel:setHeight(40)
topPanel:addAnchor(AnchorTop, 'parent', AnchorTop)
topPanel:addAnchor(AnchorLeft, 'parent', AnchorLeft)
topPanel:addAnchor(AnchorRight, 'parent', AnchorRight)

local topLayout = UIHorizontalLayout.create(topPanel)
topLayout:setSpacing(5)
topLayout:setAlignRight(true)
topPanel:setLayout(topLayout)

-- Botões do topo
local menuItems = {'File', 'Edit', 'View', 'Help'}
for _, item in ipairs(menuItems) do
    local menuButton = g_ui.createWidget('Button', topPanel)
    menuButton:setText(item)
    menuButton:setWidth(60)
end
```

#### Finalização
```lua

-- Painel lateral esquerdo (vertical)
local leftPanel = g_ui.createWidget('UIWidget', gameInterface)
leftPanel:setId('leftPanel')
leftPanel:setWidth(200)
leftPanel:addAnchor(AnchorTop, 'topPanel', AnchorBottom)
leftPanel:addAnchor(AnchorLeft, 'parent', AnchorLeft)
leftPanel:addAnchor(AnchorBottom, 'parent', AnchorBottom)

local leftLayout = UIVerticalLayout.create(leftPanel)
leftLayout:setSpacing(10)
leftPanel:setLayout(leftLayout)

-- Widgets do painel esquerdo
local minimap = g_ui.createWidget('UIWidget', leftPanel)
minimap:setHeight(150)
minimap:setBackgroundColor('#223322')

local inventory = g_ui.createWidget('UIWidget', leftPanel)
inventory:setHeight(200)

-- Grade de inventário
local invLayout = UIGridLayout.create(inventory)
invLayout:setCellSize({width = 32, height = 32})
invLayout:setCellSpacing(2)
invLayout:setNumColumns(6)
inventory:setLayout(invLayout)

-- Área central de jogo
local gameArea = g_ui.createWidget('UIWidget', gameInterface)
gameArea:setId('gameArea')
gameArea:addAnchor(AnchorTop, 'topPanel', AnchorBottom)
gameArea:addAnchor(AnchorLeft, 'leftPanel', AnchorRight)
gameArea:addAnchor(AnchorRight, 'parent', AnchorRight)
gameArea:addAnchor(AnchorBottom, 'parent', AnchorBottom)
gameArea:setBackgroundColor('#001122')
```

## ✅ Melhores Práticas

### 🎯 **Escolha do Layout Apropriado**

1. **Use Âncoras** para interfaces responsivas e posicionamento relativo
2. **Use Layouts Verticais/Horizontais** para listas e barras de ferramentas
3. **Use Layout de Grade** para inventários, paletas e grids uniformes
4. **Combine diferentes layouts** em containers aninhados para interfaces complexas

### 🚀 **Performance**

```lua
-- ✅ BOM: Configure layout antes de adicionar muitos filhos
    --  ✅ BOM: Configure layout antes de adicionar muitos filhos (traduzido)
local container = g_ui.createWidget('UIWidget', parent)
local layout = UIVerticalLayout.create(container)
layout:setSpacing(5)
container:setLayout(layout)

-- Agora adicione os filhos
    --  Agora adicione os filhos (traduzido)
for i = 1, 100 do
    -- Loop de repetição
    local child = g_ui.createWidget('Label', container)
    child:setText('Item ' .. i)
end

-- ❌ EVITE: Reconfigurar layout após adicionar muitos filhos
-- Isso força recálculos desnecessários
```

### 🎨 **Design Responsivo**

#### Nível Basic
```lua
-- Use âncoras para criar interfaces que se adaptam ao tamanho da tela
local widget = g_ui.createWidget('UIWidget', parent)

-- Preenche largura total, altura fixa
widget:addAnchor(AnchorLeft, 'parent', AnchorLeft)
widget:addAnchor(AnchorRight, 'parent', AnchorRight)
widget:setHeight(50)

-- Centralizado com largura máxima
widget:addAnchor(AnchorHorizontalCenter, 'parent', AnchorHorizontalCenter)
widget:setWidth(400)
widget:setMaxWidth(600)  -- Não excede 600px em telas grandes
```

#### Nível Intermediate
```lua
-- Use âncoras para criar interfaces que se adaptam ao tamanho da tela
local widget = g_ui.createWidget('UIWidget', parent)

-- Preenche largura total, altura fixa
widget:addAnchor(AnchorLeft, 'parent', AnchorLeft)
widget:addAnchor(AnchorRight, 'parent', AnchorRight)
widget:setHeight(50)

-- Centralizado com largura máxima
widget:addAnchor(AnchorHorizontalCenter, 'parent', AnchorHorizontalCenter)
widget:setWidth(400)
widget:setMaxWidth(600)  -- Não excede 600px em telas grandes
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
-- Use âncoras para criar interfaces que se adaptam ao tamanho da tela
local widget = g_ui.createWidget('UIWidget', parent)

-- Preenche largura total, altura fixa
widget:addAnchor(AnchorLeft, 'parent', AnchorLeft)
widget:addAnchor(AnchorRight, 'parent', AnchorRight)
widget:setHeight(50)

-- Centralizado com largura máxima
widget:addAnchor(AnchorHorizontalCenter, 'parent', AnchorHorizontalCenter)
widget:setWidth(400)
widget:setMaxWidth(600)  -- Não excede 600px em telas grandes
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

### 🔧 **Debugging de Layouts**

```lua
-- Ativar bordas temporárias para visualizar layouts
local function debugLayout(widget)
    widget:setBorderWidth(1)
    widget:setBorderColor('#ff0000')
    
    -- Aplicar recursivamente aos filhos
    --  Aplicar recursivamente aos filhos (traduzido)
    for _, child in ipairs(widget:getChildren()) do
    -- Loop de repetição
        debugLayout(child)
    end
end

-- debugLayout(myComplexWidget)
    --  debugLayout(myComplexWidget) (traduzido)
```

### 📱 **Layouts Aninhados**

#### Nível Basic
```lua
-- Combine diferentes layouts para máxima flexibilidade
local mainContainer = g_ui.createWidget('UIWidget', parent)

-- Layout principal vertical
local mainLayout = UIVerticalLayout.create(mainContainer)
mainContainer:setLayout(mainLayout)

-- Header com layout horizontal
local header = g_ui.createWidget('UIWidget', mainContainer)
header:setHeight(40)
local headerLayout = UIHorizontalLayout.create(header)
header:setLayout(headerLayout)

-- Corpo com layout de grade
local body = g_ui.createWidget('UIWidget', mainContainer)
local bodyLayout = UIGridLayout.create(body)
bodyLayout:setCellSize({width = 64, height = 64})
body:setLayout(bodyLayout)

-- Footer com âncoras customizadas
local footer = g_ui.createWidget('UIWidget', mainContainer)
footer:setHeight(30)
-- Footer usa âncoras internas para posicionamento específico
```

#### Nível Intermediate
```lua
-- Combine diferentes layouts para máxima flexibilidade
local mainContainer = g_ui.createWidget('UIWidget', parent)

-- Layout principal vertical
local mainLayout = UIVerticalLayout.create(mainContainer)
mainContainer:setLayout(mainLayout)

-- Header com layout horizontal
local header = g_ui.createWidget('UIWidget', mainContainer)
header:setHeight(40)
local headerLayout = UIHorizontalLayout.create(header)
header:setLayout(headerLayout)

-- Corpo com layout de grade
local body = g_ui.createWidget('UIWidget', mainContainer)
local bodyLayout = UIGridLayout.create(body)
bodyLayout:setCellSize({width = 64, height = 64})
body:setLayout(bodyLayout)

-- Footer com âncoras customizadas
local footer = g_ui.createWidget('UIWidget', mainContainer)
footer:setHeight(30)
-- Footer usa âncoras internas para posicionamento específico
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
-- Combine diferentes layouts para máxima flexibilidade
local mainContainer = g_ui.createWidget('UIWidget', parent)

-- Layout principal vertical
local mainLayout = UIVerticalLayout.create(mainContainer)
mainContainer:setLayout(mainLayout)

-- Header com layout horizontal
local header = g_ui.createWidget('UIWidget', mainContainer)
header:setHeight(40)
local headerLayout = UIHorizontalLayout.create(header)
header:setLayout(headerLayout)

-- Corpo com layout de grade
local body = g_ui.createWidget('UIWidget', mainContainer)
local bodyLayout = UIGridLayout.create(body)
bodyLayout:setCellSize({width = 64, height = 64})
body:setLayout(bodyLayout)

-- Footer com âncoras customizadas
local footer = g_ui.createWidget('UIWidget', mainContainer)
footer:setHeight(30)
-- Footer usa âncoras internas para posicionamento específico
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

O sistema de layouts do OTClient oferece flexibilidade máxima para criar interfaces profissionais e responsivas. Combine diferentes técnicas conforme necessário para obter os melhores resultados.