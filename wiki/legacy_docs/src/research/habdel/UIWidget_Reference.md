# Guia de Referência UIWidget do OTClient

Esta documentação de referência fornece uma visão geral do sistema UIWidget no OTClient, detalhando funções disponíveis, propriedades e padrões de uso para ajudar desenvolvedores a criar e modificar elementos de interface.

## Índice
1. [Uso Básico de Widget](#uso-básico-de-widget)
2. [Criação de Widget](#criação-de-widget)
3. [Hierarquia de Widget](#hierarquia-de-widget)
4. [Posicionamento e Dimensionamento](#posicionamento-e-dimensionamento)
5. [Estilização](#estilização)
6. [Manipulação de Texto](#manipulação-de-texto)
7. [Imagens e Ícones](#imagens-e-ícones)
8. [Eventos e Interação](#eventos-e-interação)
9. [Layouts](#layouts)
10. [Widgets Especiais](#widgets-especiais)

## Uso Básico de Widget

UIWidgets são os blocos fundamentais de construção de interface no OTClient. Eles podem conter outros widgets, exibir texto e imagens, lidar com entrada do usuário e muito mais.

### Criação de Widget

```lua
-- Criar um widget básico
local widget = g_ui.createWidget('UIWidget', parent)

-- Criar um widget com estilo predefinido
local button = g_ui.createWidget('Button', parent)

-- Criar um widget estaticamente
local customWidget = UIWidget.create()
```

### Destruição de Widget

```lua
-- Destruir um widget
widget:destroy()

-- Destruir todos os filhos de um widget
widget:destroyChildren()
```

## Hierarquia de Widget

Widgets são organizados em uma hierarquia onde cada widget pode ter um pai e múltiplos filhos.

### Adicionando e Removendo Filhos

```lua
-- Adicionar um widget filho
parent:addChild(child)

-- Inserir um filho em uma posição específica
parent:insertChild(index, child)

-- Remover um filho
parent:removeChild(child)

-- Verificar se o widget tem um filho específico
local hasChild = parent:hasChild(child)

-- Obter contagem de filhos
local count = parent:getChildCount()
```

### Encontrando Filhos

```lua
-- Obter filho por ID
local child = parent:getChildById('myChildId')

-- Obter filho por posição
local child = parent:getChildByPos(Point(x, y))

-- Obter filho por índice
local child = parent:getChildByIndex(index)

-- Obter filho por ID recursivamente
local child = parent:recursiveGetChildById('myDeepChildId')

-- Obter todos os filhos
local children = parent:getChildren()
```

### Manipulando Ordem dos Filhos

```lua
-- Abaixar um filho (mover para trás)
parent:lowerChild(child)

-- Elevar um filho (mover para frente)
parent:raiseChild(child)

-- Mover filho para um índice específico
parent:moveChildToIndex(child, index)

-- Reordenar filhos
parent:reorderChildren(childrenList)
```

## Posicionamento e Dimensionamento

### Posicionamento Básico

```lua
-- Definir posição diretamente
widget:setPosition({x = 10, y = 20})
widget:setX(10)
widget:setY(20)

-- Obter posição
local pos = widget:getPosition()
local x = widget:getX()
local y = widget:getY()

-- Mover widget relativamente à posição atual
widget:move(10, 20)
```

### Dimensionamento

```lua
-- Definir tamanho
widget:setSize({width = 100, height = 50})
widget:setWidth(100)
widget:setHeight(50)

-- Obter tamanho
local size = widget:getSize()
local width = widget:getWidth()
local height = widget:getHeight()

-- Redimensionar widget
widget:resize(10, 10) -- Adicionar 10px à largura e altura

-- Definir tamanho fixo (não pode ser alterado por layouts)
widget:setFixedSize(true)
```

### Âncoras e Layout

```lua
-- Adicionar âncora (sistema de posicionamento sofisticado)
widget:addAnchor(AnchorTop, 'parent', AnchorTop)
widget:addAnchor(AnchorHorizontalCenter, 'parent', AnchorHorizontalCenter)

-- Remover âncora
widget:removeAnchor(AnchorTop)

-- Centralizar widget no pai
widget:centerIn('parent')

-- Preencher pai
widget:fill('parent')

-- Quebrar todas as âncoras
widget:breakAnchors()
```

### Margens e Preenchimento

```lua
-- Definir margens (espaço fora do widget)
widget:setMargin(5)                     -- Todos os lados
widget:setMarginTop(10)
widget:setMarginRight(10)
widget:setMarginBottom(10)
widget:setMarginLeft(10)
widget:setMarginHorizontal(10)          -- Esquerda e direita
widget:setMarginVertical(10)            -- Cima e baixo

-- Definir preenchimento (espaço dentro do widget)
widget:setPadding(5)                    -- Todos os lados
widget:setPaddingTop(10)
widget:setPaddingRight(10)
widget:setPaddingBottom(10)
widget:setPaddingLeft(10)
widget:setPaddingHorizontal(10)         -- Esquerda e direita
widget:setPaddingVertical(10)           -- Cima e baixo
```

## Estilização

### Estilização Básica

```lua
-- Definir nome do estilo
widget:setStyle('ButtonRedBig')

-- Aplicar/mesclar estilos
widget:applyStyle(styleNode)
widget:mergeStyle(styleNode)

-- Definir ID (importante para estilização)
widget:setId('myButton')
```

### Cores e Opacidade

```lua
-- Definir cor principal
widget:setColor('#FF0000')  -- vermelho

-- Definir cor de fundo
widget:setBackgroundColor('#00FF00')  -- verde

-- Definir opacidade
widget:setOpacity(0.5)  -- 50% transparente
```

### Bordas

```lua
-- Definir largura da borda
widget:setBorderWidth(2)                 -- Todos os lados
widget:setBorderWidthTop(2)
widget:setBorderWidthRight(2)
widget:setBorderWidthBottom(2)
widget:setBorderWidthLeft(2)

-- Definir cor da borda
widget:setBorderColor('#0000FF')         -- Todos os lados
widget:setBorderColorTop('#0000FF')
widget:setBorderColorRight('#0000FF')
widget:setBorderColorBottom('#0000FF')
widget:setBorderColorLeft('#0000FF')
```

## Manipulação de Texto

```lua
-- Definir texto
widget:setText('Olá Mundo')

-- Definir texto colorido (com markup)
widget:setColoredText('Olá |red|Mundo')

-- Obter texto
local text = widget:getText()

-- Definir alinhamento do texto
widget:setTextAlign(AlignCenter)  -- Opções: AlignLeft, AlignRight, AlignCenter

-- Definir quebra de texto
widget:setTextWrap(true)

-- Auto-redimensionar baseado no texto
widget:setTextAutoResize(true)
widget:resizeToText()

-- Definir fonte
widget:setFont('verdana-11px-antialised')
```

## Imagens e Ícones

### Imagem de Fundo

```lua
-- Definir origem
widget:setImageSource('/caminho/para/imagem.png')

-- Definir a partir de base64
widget:setImageSourceBase64('base64string')

-- Definir posicionamento
widget:setImageClip(Rect(0, 0, 100, 100))
widget:setImageOffset(Point(10, 10))
widget:setImageOffsetX(10)
widget:setImageOffsetY(10)

-- Definir dimensionamento
widget:setImageWidth(100)
widget:setImageHeight(100)
widget:setImageSize({width = 100, height = 100})
widget:setImageRect(Rect(x, y, width, height))

-- Definir propriedades
widget:setImageColor('#FF0000')
widget:setImageFixedRatio(true)
widget:setImageRepeated(true)
widget:setImageSmooth(true)
widget:setImageAutoResize(true)

-- Definir borda da imagem para escalonamento 9-slice
widget:setImageBorder(5)  -- Todos os lados
widget:setImageBorderTop(5)
widget:setImageBorderRight(5)
widget:setImageBorderBottom(5)
widget:setImageBorderLeft(5)
```

### Ícones

```lua
-- Definir ícone
widget:setIcon('/caminho/para/icone.png')

-- Definir posicionamento do ícone
widget:setIconClip(Rect(0, 0, 20, 20))
widget:setIconOffset(Point(5, 5))
widget:setIconOffsetX(5)
widget:setIconOffsetY(5)

-- Definir dimensionamento do ícone
widget:setIconWidth(20)
widget:setIconHeight(20)
widget:setIconSize({width = 20, height = 20})
widget:setIconRect(Rect(x, y, width, height))

-- Definir propriedades do ícone
widget:setIconColor('#FF0000')
widget:setIconAlign(AlignCenter)
```

## Eventos e Interação

### Gerenciamento de Estado

```lua
-- Habilitar/Desabilitar
widget:setEnabled(true)
widget:enable()
widget:disable()
local enabled = widget:isEnabled()

-- Mostrar/Ocultar
widget:setVisible(true)
widget:show()
widget:hide()
local visible = widget:isVisible()

-- Foco
widget:focus()
widget:setFocusable(true)
local focused = widget:isFocused()

-- Verificar estados
local active = widget:isActive()
local hovered = widget:isHovered()
local pressed = widget:isPressed()
```

### Propriedades Especiais

```lua
-- Definir como fantasma (não bloqueia mouse)
widget:setPhantom(true)

-- Definir como arrastável
widget:setDraggable(true)

-- Definir estado marcado (para checkboxes, etc.)
widget:setChecked(true)

-- Habilitar/desabilitar recorte de conteúdo
widget:setClipping(true)
```

### Captura de Entrada

```lua
-- Capturar entrada do mouse (capturar todos os eventos do mouse)
widget:grabMouse()
widget:ungrabMouse()

-- Capturar entrada do teclado
widget:grabKeyboard()
widget:ungrabKeyboard()
```

## Layouts

Layouts controlam como os widgets são organizados dentro de seu pai.

### Tipos de Layout Disponíveis

```lua
-- Criar layouts
local anchorLayout = UIAnchorLayout.create(parent)
local horizontalLayout = UIHorizontalLayout.create(parent)
local verticalLayout = UIVerticalLayout.create(parent)
local gridLayout = UIGridLayout.create(parent)

-- Definir um layout em um widget
widget:setLayout(layout)

-- Obter layout atual
local layout = widget:getLayout()
```

### Layouts de Caixa Vertical/Horizontal

```lua
-- Definir espaçamento entre elementos
boxLayout:setSpacing(10)

-- Fazer layout redimensionar para caber filhos
boxLayout:setFitChildren(true)

-- Específico vertical: alinhar na parte inferior
verticalLayout:setAlignBottom(true)

-- Específico horizontal: alinhar à direita
horizontalLayout:setAlignRight(true)
```

### Layout de Grade

```lua
-- Definir tamanho da célula
gridLayout:setCellSize({width = 50, height = 50})
gridLayout:setCellWidth(50)
gridLayout:setCellHeight(50)

-- Definir espaçamento entre células
gridLayout:setCellSpacing(5)

-- Definir direção do fluxo
gridLayout:setFlow(true)  -- fluxo horizontal

-- Definir número de colunas/linhas
gridLayout:setNumColumns(3)
gridLayout:setNumLines(2)
```

## Widgets Especiais

### Edição de Texto

```lua
-- Criar um editor de texto
local textEdit = g_ui.createWidget('TextEdit', parent)

-- Definir posição do cursor
textEdit:setCursorPos(5)

-- Definir seleção
textEdit:setSelection(2, 5)  -- selecionar caracteres do índice 2 ao 5

-- Definir propriedades
textEdit:setTextHidden(true)           -- modo senha
textEdit:setMultiline(true)            -- permitir múltiplas linhas
textEdit:setEditable(true)             -- permitir edição
textEdit:setSelectable(true)           -- permitir seleção
textEdit:setValidCharacters('0-9')     -- permitir apenas números

-- Definir comprimento máximo
textEdit:setMaxLength(100)

-- Obter/modificar texto
textEdit:appendText(' texto adicional')
textEdit:removeCharacter(false)        -- backspace
textEdit:cut()
textEdit:copy()
textEdit:paste()
textEdit:wrapText()
```

## Melhores Práticas

1. **Use layouts sempre que possível** - Eles simplificam o posicionamento e tornam as interfaces responsivas.
2. **Defina IDs para todos os widgets importantes** - Facilita a estilização e localização deles.
3. **Use âncoras para posicionamento responsivo** - Elas se adaptam às mudanças de tamanho do pai.
4. **Não abuse do posicionamento fixo** - Torna as interfaces menos adaptáveis a diferentes resoluções.
5. **Agrupe widgets relacionados** - Use um widget container para agrupar elementos relacionados.
6. **Use hierarquia adequada** - Mantenha a árvore de widgets organizada para melhor manutenção.
7. **Separe estilo do código** - Use arquivos de estilo externos quando possível.

## Padrões Comuns

### Criando uma Janela Simples

```lua
-- Criar janela principal
local window = g_ui.createWidget('MainWindow', rootWidget)
window:setId('myWindow')
window:setText('Minha Janela')
window:setSize({width = 300, height = 200})
window:setDraggable(true)

-- Adicionar um rótulo
local label = g_ui.createWidget('Label', window)
label:setId('infoLabel')
label:setText('Olá Mundo')
label:setTextAlign(AlignCenter)
label:addAnchor(AnchorHorizontalCenter, 'parent', AnchorHorizontalCenter)
label:addAnchor(AnchorTop, 'parent', AnchorTop)
label:setMarginTop(20)

-- Adicionar um botão
local button = g_ui.createWidget('Button', window)
button:setId('actionButton')
button:setText('Clique em Mim')
button:addAnchor(AnchorHorizontalCenter, 'parent', AnchorHorizontalCenter)
button:addAnchor(AnchorBottom, 'parent', AnchorBottom)
button:setMarginBottom(20)
```

### Criando uma Lista com Itens

```lua
-- Criar uma lista
local list = g_ui.createWidget('UIWidget', parent)
list:setId('myList')
list:setLayout(UIVerticalLayout.create(list))
list:getLayout():setSpacing(2)

-- Adicionar itens à lista
for i = 1, 10 do
    local item = g_ui.createWidget('ListItem', list)
    item:setText('Item ' .. i)
    item:setId('item' .. i)
end
```

### Criando uma Grade de Itens

```lua
-- Criar um container de grade
local grid = g_ui.createWidget('UIWidget', parent)
grid:setId('itemGrid')
local gridLayout = UIGridLayout.create(grid)
gridLayout:setNumColumns(4)
gridLayout:setCellSize({width = 40, height = 40})
gridLayout:setCellSpacing(5)
grid:setLayout(gridLayout)

-- Adicionar itens à grade
for i = 1, 16 do
    local item = g_ui.createWidget('UIWidget', grid)
    item:setId('gridItem' .. i)
    item:setBackgroundColor('#' .. string.format('%06x', i * 1000))
end
```

Esta referência deve ajudá-lo a entender e utilizar o rico sistema UIWidget no OTClient para criar interfaces complexas e interativas. 