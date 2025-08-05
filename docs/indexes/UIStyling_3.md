# Sistema de Estilização e Temas UIWidget

O OTClient utiliza um sistema de estilização baseado em CSS que permite criar interfaces visuais consistentes e facilmente personalizáveis através de arquivos `.otui` e definição de estilos programáticos.

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Arquivos .otui](#arquivos-otui)
3. [Sintaxe de Estilização](#sintaxe-de-estilização)
4. [Propriedades de Estilo](#propriedades-de-estilo)
5. [Seletores e Hierarquia](#seletores-e-hierarquia)
6. [Estados e Pseudoclasses](#estados-e-pseudoclasses)
7. [Temas e Variações](#temas-e-variações)
8. [Estilização Programática](#estilização-programática)
9. [Exemplos Práticos](#exemplos-práticos)
10. [Melhores Práticas](#melhores-práticas)

## 🎯 Visão Geral

O sistema de estilização do OTClient oferece:

- **Sintaxe CSS-like**: Familiar para desenvolvedores web
- **Herança de Estilos**: Widgets herdam propriedades dos pais
- **Estados Dinâmicos**: Estilos baseados em hover, pressed, focused, etc.
- **Temas Modulares**: Fácil troca de aparência completa
- **Propriedades Extensas**: Cores, bordas, imagens, fontes, posicionamento

### 🏗️ **Estrutura do Sistema**

```
data/styles/
├── 10-*.otui          # Estilos base (widgets básicos)
├── 20-*.otui          # Estilos intermediários
├── 30-*.otui          # Estilos específicos
└── modules/*/         # Estilos específicos de módulos
```

## 📄 Arquivos .otui

Os arquivos `.otui` (OTClient UI) contêm definições de estilo usando sintaxe similar ao CSS.

### 📝 **Estrutura Básica**

```otui
// Comentário de linha
/* Comentário de bloco */

// Definição de estilo base
WidgetName < BaseWidget
  property: value
  another-property: value

// Estilo derivado
SpecialWidget < WidgetName
  override-property: new-value
  additional-property: value

// Estilo com ID específico
SpecialWidget#myId
  unique-property: value
```

### 🎨 **Exemplo Completo**

```otui
// Estilo base para botões
Button < UIWidget
  font: verdana-11px-antialised
  color: #f4f4f4ff
  size: 106 24
  text-offset: 0 0
  text-align: center
  image-source: /images/ui/button
  image-border: 3
  padding: 5 10 5 10
  
  $hover:
    color: #ffffff

  $pressed:
    image-clip: 0 24 106 24
    text-offset: 1 1

  $disabled:
    color: #999999
    opacity: 0.6

// Botão específico vermelho
RedButton < Button
  color: #ff0000
  image-source: /images/ui/red_button
  
  $hover:
    color: #ff4444

// Botão com ID específico
Button#saveButton
  image-source: /images/ui/save_button
  text: Save
```

## 🎨 Sintaxe de Estilização

### 📐 **Propriedades de Dimensão**

```otui
Widget < UIWidget
  // Tamanho fixo
  size: 100 50
  width: 100
  height: 50
  
  // Tamanhos mínimo/máximo
  min-size: 50 25
  max-size: 200 100
  min-width: 50
  max-width: 200
  min-height: 25
  max-height: 100
  
  // Posicionamento
  anchors.top: parent.top
  anchors.left: parent.left
  anchors.right: parent.right
  anchors.bottom: parent.bottom
  anchors.horizontalCenter: parent.horizontalCenter
  anchors.verticalCenter: parent.verticalCenter
```

### 🎨 **Propriedades de Cor**

```otui
ColoredWidget < UIWidget
  // Cores usando diferentes formatos
  color: #ff0000                    // Hexadecimal RGB
  color: #ff0000ff                  // Hexadecimal RGBA
  color: red                        // Nome da cor
  color: rgb(255, 0, 0)             // Função RGB
  color: rgba(255, 0, 0, 255)       // Função RGBA
  
  // Cor de fundo
  background-color: #333333
  background-color: rgba(50, 50, 50, 128)
  
  // Opacidade
  opacity: 0.8                      // 80% opaco
```

### 🖼️ **Propriedades de Imagem**

```otui
ImageWidget < UIWidget
  // Imagem de fundo
  image-source: /images/ui/background.png
  image-repeated: false
  image-smooth: true
  image-fixed-ratio: true
  image-auto-resize: false
  
  // Posicionamento da imagem
  image-offset: 10 10
  image-clip: 0 0 100 100
  image-rect: 0 0 100 100
  image-size: 100 100
  
  // 9-slice (bordas escaláveis)
  image-border: 5                   // Todos os lados
  image-border-top: 5
  image-border-right: 10
  image-border-bottom: 5
  image-border-left: 10
  
  // Cor da imagem (tint)
  image-color: #ff0000
```

### 🔤 **Propriedades de Texto**

```otui
TextWidget < UIWidget
  // Fonte e cor
  font: verdana-11px-antialised
  color: #ffffff
  
  // Alinhamento
  text-align: left                  // left, right, center
  text-vertical-align: middle       // top, middle, bottom
  text-offset: 5 3
  
  // Comportamento do texto
  text-wrap: true
  text-auto-resize: false
  text-only-upper-case: false
  
  // Texto específico
  text: "Hello World"
```

### 📏 **Margens e Padding**

```otui
SpacedWidget < UIWidget
  // Margens (espaço externo)
  margin: 10                        // Todos os lados
  margin-top: 15
  margin-right: 20
  margin-bottom: 10
  margin-left: 5
  
  // Padding (espaço interno)
  padding: 8                        // Todos os lados
  padding-top: 12
  padding-right: 16
  padding-bottom: 8
  padding-left: 4
```

### 🔲 **Propriedades de Borda**

```otui
BorderWidget < UIWidget
  // Largura da borda
  border-width: 2                   // Todos os lados
  border-width-top: 3
  border-width-right: 2
  border-width-bottom: 3
  border-width-left: 2
  
  // Cor da borda
  border-color: #666666             // Todos os lados
  border-color-top: #888888
  border-color-right: #444444
  border-color-bottom: #222222
  border-color-left: #666666
```

## 🎯 Seletores e Hierarquia

### 🏷️ **Tipos de Seletores**

```otui
// Seletor de tipo (nome do widget)
Button
  color: #ffffff

// Seletor de ID
Button#saveButton
  color: #00ff00

// Seletor de classe (usando estilo como classe)
.important
  border-width: 2
  border-color: #ff0000

// Herança de estilo
PrimaryButton < Button
  background-color: #007acc

// Múltipla herança
SpecialButton < PrimaryButton
  text: "Special"
```

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

## 🔗 **Herança e Cascata**

```otui
// Estilo base
BaseWindow < UIWidget
  background-color: #2a2a2a
  border-width: 1
  border-color: #555555
  padding: 10

// Janela específica herda do base
GameWindow < BaseWindow
  size: 400 300
  // Herda: background-color, border-width, border-color, padding

// Sobrescreve propriedades específicas
GameWindow#inventory < GameWindow
  size: 200 400
  background-color: #1a1a1a         // Sobrescreve a cor de fundo
  // Mantém: border-width, border-color, padding
```

## 🎭 Estados e Pseudoclasses

### 🔄 **Estados Básicos**

```otui
InteractiveButton < UIWidget
  color: #cccccc
  background-color: #333333
  
  // Estado hover (mouse sobre)
  $hover:
    color: #ffffff
    background-color: #444444
  
  // Estado pressed (pressionado)
  $pressed:
    background-color: #222222
    text-offset: 1 1
  
  // Estado focused (com foco)
  $focused:
    border-color: #0080ff
    border-width: 2
  
  // Estado disabled (desabilitado)
  $disabled:
    color: #666666
    opacity: 0.5
  
  // Estado checked (marcado)
  $checked:
    background-color: #008000
```

### 📍 **Estados de Posição**

```otui
ListItem < UIWidget
  background-color: #2a2a2a
  
  // Primeiro item da lista
  $first:
    border-top-width: 2
  
  // Último item da lista
  $last:
    border-bottom-width: 2
  
  // Item no meio
  $middle:
    border-top-width: 1
    border-bottom-width: 1
  
  // Item alternado (para zebra striping)
  $alternate:
    background-color: #333333
```

### 🎨 **Estados Compostos**

```otui
SmartButton < UIWidget
  color: #cccccc
  
  // Hover E enabled
  $hover !disabled:
    color: #ffffff
  
  // Pressed E focused
  $pressed $focused:
    border-color: #ff0000
  
  // Checked OU pressed
  $checked, $pressed:
    background-color: #444444
```

## 🎨 Temas e Variações

### 🌙 **Tema Escuro Completo**

```otui
// dark_theme.otui
UIWidget
  color: #e0e0e0
  background-color: #2a2a2a

Button < UIWidget
  background-color: #3a3a3a
  border-color: #555555
  
  $hover:
    background-color: #4a4a4a
  
  $pressed:
    background-color: #1a1a1a

TextEdit < UIWidget
  background-color: #1a1a1a
  color: #ffffff
  border-color: #555555
  
  $focused:
    border-color: #0080ff

Window < UIWidget
  background-color: #2a2a2a
  border-color: #555555
```

### ☀️ **Tema Claro**

```otui
// light_theme.otui
UIWidget
  color: #333333
  background-color: #f0f0f0

Button < UIWidget
  background-color: #e0e0e0
  border-color: #cccccc
  
  $hover:
    background-color: #d0d0d0
  
  $pressed:
    background-color: #c0c0c0

TextEdit < UIWidget
  background-color: #ffffff
  color: #333333
  border-color: #cccccc
  
  $focused:
    border-color: #0080ff

Window < UIWidget
  background-color: #f8f8f8
  border-color: #cccccc
```

### 🎮 **Tema de Jogo**

```otui
// game_theme.otui
GameButton < UIWidget
  image-source: /images/ui/game/button
  image-border: 4
  color: #fff2cc
  font: cipsoftFont
  
  $hover:
    image-source: /images/ui/game/button_hover
  
  $pressed:
    image-source: /images/ui/game/button_pressed

GamePanel < UIWidget
  image-source: /images/ui/game/panel
  image-border: 8
  padding: 12

HealthBar < UIWidget
  background-color: #8b0000
  border-color: #444444
  
  $!full:
    background-color: #ff0000
```

## 💻 Estilização Programática

### 🔧 **Aplicando Estilos via Lua**

```lua
-- Aplicar estilo por nome
    --  Aplicar estilo por nome (traduzido)
widget:setStyle('ButtonRedBig')

-- Aplicar estilo de um nó OTML
local styleNode = g_ui.importStyle('MyCustomStyle')
widget:applyStyle(styleNode)

-- Mesclar estilo (mantém propriedades existentes)
widget:mergeStyle(styleNode)

-- Definir propriedades individuais
    --  Definir propriedades individuais (traduzido)
widget:setBackgroundColor('#ff0000')
widget:setBorderWidth(2)
widget:setBorderColor('#000000')
widget:setFont('verdana-11px-antialised')
```

### 🎨 **Criando Estilos Dinamicamente**

#### Nível Basic
```lua
-- Função para criar estilo dinâmico
local function createDynamicStyle(baseColor, size)
    local style = {
end
-- Aplicar estilo dinâmico
local widget = g_ui.createWidget('UIWidget', parent)
local dynamicStyle = createDynamicStyle('#ff00ff', {width = 100, height = 50})
    -- Converter propriedade CSS para método Lua
    if property == 'background-color' then
    elseif property == 'border-width' then
    -- ... outros mapeamentos
    end
end
```

#### Nível Intermediate
```lua
-- Função para criar estilo dinâmico
local function createDynamicStyle(baseColor, size)
    local style = {
        ['background-color'] = baseColor,
        ['size'] = size.width .. ' ' .. size.height,
        ['border-width'] = '1',
        ['border-color'] = '#000000'
    }
    
    return style
end

-- Aplicar estilo dinâmico
local widget = g_ui.createWidget('UIWidget', parent)
local dynamicStyle = createDynamicStyle('#ff00ff', {width = 100, height = 50})

for property, value in pairs(dynamicStyle) do
    -- Converter propriedade CSS para método Lua
    if property == 'background-color' then
        widget:setBackgroundColor(value)
    elseif property == 'border-width' then
        widget:setBorderWidth(tonumber(value))
    -- ... outros mapeamentos
    end
end
```

#### Nível Advanced
```lua
-- Função para criar estilo dinâmico
local function createDynamicStyle(baseColor, size)
    local style = {
        ['background-color'] = baseColor,
        ['size'] = size.width .. ' ' .. size.height,
        ['border-width'] = '1',
        ['border-color'] = '#000000'
    }
    
    return style
end

-- Aplicar estilo dinâmico
local widget = g_ui.createWidget('UIWidget', parent)
local dynamicStyle = createDynamicStyle('#ff00ff', {width = 100, height = 50})

for property, value in pairs(dynamicStyle) do
    -- Converter propriedade CSS para método Lua
    if property == 'background-color' then
        widget:setBackgroundColor(value)
    elseif property == 'border-width' then
        widget:setBorderWidth(tonumber(value))
    -- ... outros mapeamentos
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

### 🎭 **Sistema de Temas Dinâmico**

```lua
local ThemeManager = {}
ThemeManager.currentTheme = 'dark'
ThemeManager.themes = {}

-- Registrar tema
    --  Registrar tema (traduzido)
function ThemeManager.registerTheme(name, styleFile)
    -- Função: ThemeManager
    ThemeManager.themes[name] = styleFile
end

-- Aplicar tema
    --  Aplicar tema (traduzido)
function ThemeManager.applyTheme(themeName)
    -- Função: ThemeManager
    if not ThemeManager.themes[themeName] then
    -- Verificação condicional
        print('Tema não encontrado:', themeName)
        return
    end
    
    -- Carregar arquivo de estilo
    --  Carregar arquivo de estilo (traduzido)
    local styleFile = ThemeManager.themes[themeName]
    g_ui.importStyle(styleFile)
    
    ThemeManager.currentTheme = themeName
    
    -- Atualizar todos os widgets visíveis
    ThemeManager.updateAllWidgets(rootWidget)
end

-- Atualizar widgets recursivamente
    --  Atualizar widgets recursivamente (traduzido)
function ThemeManager.updateAllWidgets(widget)
    -- Função: ThemeManager
    -- Re-aplicar estilo atual
    --  Re-aplicar estilo atual (traduzido)
    if widget:getStyleName() and widget:getStyleName() ~= '' then
    -- Verificação condicional
        widget:setStyle(widget:getStyleName())
    end
    
    -- Processar filhos
    --  Processar filhos (traduzido)
    for _, child in ipairs(widget:getChildren()) do
    -- Loop de repetição
        ThemeManager.updateAllWidgets(child)
    end
end

-- Registrar temas
    --  Registrar temas (traduzido)
ThemeManager.registerTheme('dark', 'dark_theme')
ThemeManager.registerTheme('light', 'light_theme')
ThemeManager.registerTheme('game', 'game_theme')

-- Aplicar tema
    --  Aplicar tema (traduzido)
ThemeManager.applyTheme('dark')
```

## 💡 Exemplos Práticos

### 🎮 **Interface de Jogo Completa**

```otui
// game_interface.otui

// Painel principal do jogo
GamePanel < UIWidget
  background-color: #1a1a1a
  border-width: 2
  border-color: #444444
  padding: 8

// Barra de vida estilizada
HealthBar < UIWidget
  height: 20
  background-color: #2a0000
  border-width: 1
  border-color: #666666
  
  // Barra de preenchimento
  UIWidget
    id: fill
    anchors.left: parent.left
    anchors.top: parent.top
    anchors.bottom: parent.bottom
    background-color: #ff0000
    width: 0  // Será atualizado dinamicamente

// Slot de inventário
InventorySlot < UIWidget
  size: 34 34
  background-color: #333333
  border-width: 1
  border-color: #666666
  
  $hover:
    border-color: #aaaaaa
  
  $!empty:
    background-color: #444444

// Botão de ação
ActionButton < UIWidget
  size: 32 32
  image-source: /images/ui/action_button
  image-border: 2
  
  $pressed:
    image-clip: 0 32 32 32
  
  $disabled:
    image-color: #666666
    opacity: 0.5
  
  $cooldown:
    image-color: #0066cc
    opacity: 0.8

// Janela de chat
ChatWindow < UIWidget
  background-color: #000000aa
  border-width: 1
  border-color: #666666
  padding: 4
  
  // Área de texto
  TextEdit
    id: chatInput
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.bottom: parent.bottom
    height: 20
    background-color: #1a1a1a
    color: #ffffff
    
    $focused:
      border-color: #0080ff

// Minimap estilizado
Minimap < UIWidget
  size: 150 150
  background-color: #000000
  border-width: 2
  border-color: #444444
  
  // Zoom buttons
  Button#zoomIn
    anchors.top: parent.top
    anchors.right: parent.right
    size: 20 20
    text: "+"
    
  Button#zoomOut
    anchors.top: prev.bottom
    anchors.right: parent.right
    size: 20 20
    text: "-"
```

### 🎨 **Sistema de Notificações**

```otui
// notifications.otui

// Base para notificações
Notification < UIWidget
  height: 60
  margin: 5
  padding: 10
  border-width: 1
  border-color: #666666
  opacity: 0.9
  
  // Ícone da notificação
  UIWidget
    id: icon
    anchors.left: parent.left
    anchors.verticalCenter: parent.verticalCenter
    size: 32 32
    margin-right: 10
  
  // Texto da notificação
  Label
    id: text
    anchors.left: prev.right
    anchors.right: closeButton.left
    anchors.verticalCenter: parent.verticalCenter
    text-wrap: true
  
  // Botão fechar
  Button
    id: closeButton
    anchors.right: parent.right
    anchors.top: parent.top
    size: 16 16
    text: "×"

// Notificação de sucesso
SuccessNotification < Notification
  background-color: #004400
  border-color: #008800
  
  UIWidget#icon:
    image-source: /images/ui/icons/success.png

// Notificação de erro
ErrorNotification < Notification
  background-color: #440000
  border-color: #880000
  
  UIWidget#icon:
    image-source: /images/ui/icons/error.png

// Notificação de informação
InfoNotification < Notification
  background-color: #000044
  border-color: #000088
  
  UIWidget#icon:
    image-source: /images/ui/icons/info.png

// Notificação de warning
WarningNotification < Notification
  background-color: #444400
  border-color: #888800
  
  UIWidget#icon:
    image-source: /images/ui/icons/warning.png
```

### 📋 **Formulário Estilizado**

```otui
// form.otui

// Container do formulário
FormContainer < UIWidget
  background-color: #2a2a2a
  border-width: 1
  border-color: #555555
  padding: 20

// Label do formulário
FormLabel < Label
  color: #cccccc
  font: verdana-11px-antialised
  text-align: left
  height: 20
  margin-bottom: 5

// Campo de entrada
FormInput < TextEdit
  height: 30
  background-color: #1a1a1a
  color: #ffffff
  border-width: 1
  border-color: #666666
  padding: 5
  margin-bottom: 15
  
  $focused:
    border-color: #0080ff
    background-color: #222222
  
  $error:
    border-color: #ff0000
    background-color: #2a1a1a

// Campo de senha
FormPassword < FormInput
  text-hidden: true

// Área de texto
FormTextArea < FormInput
  height: 80
  multiline: true

// Checkbox estilizado
FormCheckbox < UIWidget
  size: 20 20
  background-color: #1a1a1a
  border-width: 1
  border-color: #666666
  
  $checked:
    background-color: #0080ff
    image-source: /images/ui/icons/check.png
  
  $hover:
    border-color: #aaaaaa

// Botão do formulário
FormButton < Button
  height: 35
  background-color: #0080ff
  color: #ffffff
  border-width: 0
  font: verdana-11px-antialised
  
  $hover:
    background-color: #0099ff
  
  $pressed:
    background-color: #0066cc

// Botão secundário
FormButtonSecondary < FormButton
  background-color: #666666
  
  $hover:
    background-color: #777777
  
  $pressed:
    background-color: #555555
```

## ✅ Melhores Práticas

### 🎯 **Organização de Estilos**

```otui
// ✅ BOM: Organize estilos de forma hierárquica
BaseWidget < UIWidget
  font: verdana-11px-antialised
  color: #ffffff

BaseButton < BaseWidget
  size: 100 30
  text-align: center

PrimaryButton < BaseButton
  background-color: #0080ff

SecondaryButton < BaseButton
  background-color: #666666

// ❌ EVITE: Repetir propriedades comuns
RedButton < UIWidget
  font: verdana-11px-antialised  // Repetição
  color: #ffffff                 // Repetição
  size: 100 30                   // Repetição
  text-align: center             // Repetição
  background-color: #ff0000
```

### 🎨 **Nomenclatura Consistente**

```otui
// ✅ BOM: Use nomenclatura clara e consistente
MainMenuButton < Button
GamePanelBackground < UIWidget
InventorySlotEmpty < UIWidget
ChatMessagePlayer < Label

// ❌ EVITE: Nomes confusos ou inconsistentes
Btn1 < Button
MyThing < UIWidget
Stuff < UIWidget
```

### 🔄 **Uso Eficiente de Estados**

```otui
// ✅ BOM: Use estados apropriadamente
InteractiveButton < UIWidget
  background-color: #333333
  
  $hover:
    background-color: #444444    // Sutil mudança no hover
  
  $pressed:
    background-color: #222222    // Clara indicação de pressed
  
  $disabled:
    opacity: 0.5                 // Indica claramente estado disabled

// ❌ EVITE: Estados que confundem o usuário
ConfusingButton < UIWidget
  background-color: #333333
  
  $hover:
    background-color: #ff0000    // Mudança muito drástica
  
  $pressed:
    background-color: #333333    // Sem indicação visual
```

### 📐 **Responsive Design**

```otui
// ✅ BOM: Use propriedades que se adaptam
ResponsivePanel < UIWidget
  min-width: 200
  max-width: 800
  padding: 10
  
  // Use anchors para responsividade
  anchors.left: parent.left
  anchors.right: parent.right

// Para diferentes tamanhos de tela
ResponsivePanel#mobile
  min-width: 100
  padding: 5

ResponsivePanel#desktop
  min-width: 300
  padding: 15
```

### 🎨 **Paleta de Cores Consistente**

```otui
// Defina uma paleta de cores no início
// Primary: #0080ff
// Secondary: #666666
// Success: #00aa00
// Error: #ff0000
// Warning: #ffaa00
// Background: #2a2a2a
// Text: #ffffff

PrimaryButton < Button
  background-color: #0080ff

SecondaryButton < Button
  background-color: #666666

SuccessMessage < Label
  color: #00aa00

ErrorMessage < Label
  color: #ff0000
```

### ⚡ **Performance**

```otui
// ✅ BOM: Use image-border para elementos escaláveis
ScalableButton < UIWidget
  image-source: /images/ui/button
  image-border: 3              // Permite escalar sem distorção

// ❌ EVITE: Imagens que não escalam bem
FixedButton < UIWidget
  image-source: /images/ui/button_100x30.png  // Só funciona para 100x30
```

O sistema de estilização do OTClient oferece flexibilidade máxima para criar interfaces visualmente atraentes e funcionais. Use as práticas recomendadas para manter código limpo e interfaces consistentes.