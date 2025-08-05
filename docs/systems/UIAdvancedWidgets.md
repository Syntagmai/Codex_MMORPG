
# 🎨 UI-009: Widgets Avançados

## 📋 **Visão Geral**

Os **Widgets Avançados** do OTClient são componentes de interface especializados que oferecem funcionalidades complexas e interativas. Esta documentação cobre todos os widgets avançados disponíveis no sistema UI do OTClient.

---

## 🎯 **Widgets Avançados Disponíveis**

### **1. UITable - Tabelas Avançadas**

O `UITable` é um widget especializado para exibição de dados em formato tabular com recursos avançados.

#### **Características Principais:**
- **Ordenação**: Suporte a ordenação por colunas
- **Seleção**: Seleção de linhas com feedback visual
- **Cabeçalhos**: Cabeçalhos configuráveis
- **Estilização**: Estilos personalizáveis para linhas e colunas
- **Dados Dinâmicos**: Adição e remoção dinâmica de dados

#### **API Principal:**

```lua
-- Criação de tabela
local table = UITable.create()

-- Adicionar cabeçalho
table:addHeader({
    {text = "Nome", width = 100},
    {text = "Valor", width = 80},
    {text = "Status", width = 60}
})

-- Adicionar linha de dados
table:addRow({
    {text = "Item 1", style = "TableCell"},
    {text = "100", style = "TableCell"},
    {text = "Ativo", style = "TableCell"}
})

-- Configurar ordenação
table:setSorting(1, TABLE_SORTING_ASC)

-- Selecionar linha
table:selectRow(rowWidget)
```

#### **Eventos Disponíveis:**
- `onSelectionChange`: Chamado quando uma linha é selecionada
- `onSortingChange`: Chamado quando a ordenação muda

---

### **2. UIScrollArea - Área de Rolagem**

O `UIScrollArea` fornece funcionalidade de rolagem para widgets que excedem o espaço disponível.

#### **Características Principais:**
- **Rolagem Vertical e Horizontal**: Suporte a ambos os tipos de rolagem
- **Scrollbars Automáticos**: Configuração automática de barras de rolagem
- **Rolagem Invertida**: Suporte a rolagem invertida
- **Navegação por Mouse**: Suporte a roda do mouse

#### **API Principal:**

```lua
-- Criação de área de rolagem
local scrollArea = UIScrollArea.create()

-- Configurar scrollbar vertical
scrollArea:setVerticalScrollBar(verticalScrollBar)

-- Configurar scrollbar horizontal
scrollArea:setHorizontalScrollBar(horizontalScrollBar)

-- Configurar rolagem invertida
scrollArea:setInverted(true)

-- Garantir que um widget seja visível
scrollArea:ensureChildVisible(childWidget)

-- Atualizar barras de rolagem
scrollArea:updateScrollBars()
```

#### **Eventos Disponíveis:**
- `onScrollChange`: Chamado quando a posição de rolagem muda

---

### **3. UIScrollBar - Barra de Rolagem**

O `UIScrollBar` é o componente responsável pela navegação em áreas roláveis.

#### **Características Principais:**
- **Orientação**: Vertical ou horizontal
- **Valores Configuráveis**: Mínimo, máximo e valor atual
- **Navegação por Mouse**: Suporte a roda do mouse
- **Atalhos de Teclado**: Ctrl+Click para ir ao início/fim
- **Exibição de Valor**: Opção para mostrar o valor atual

#### **API Principal:**

```lua
-- Criação de scrollbar
local scrollBar = UIScrollBar.create()

-- Configurar orientação
scrollBar:setOrientation('vertical') -- ou 'horizontal'

-- Configurar valores
scrollBar:setRange(0, 100)
scrollBar:setValue(50)
scrollBar:setStep(5)

-- Configurar navegação por mouse
scrollBar:setMouseScroll(true)

-- Incrementar/Decrementar
scrollBar:increment(10)
scrollBar:decrement(5)
```

#### **Eventos Disponíveis:**
- `onValueChange`: Chamado quando o valor muda

---

### **4. UIPopupScrollMenu - Menu Popup com Rolagem**

O `UIPopupScrollMenu` é um menu popup que suporta rolagem para muitas opções.

#### **Características Principais:**
- **Rolagem Automática**: Para menus com muitas opções
- **Posicionamento Inteligente**: Posicionamento automático
- **Navegação por Mouse**: Suporte a roda do mouse
- **Estilização**: Estilos personalizáveis

#### **API Principal:**

```lua
-- Criação de menu popup
local menu = UIPopupScrollMenu.create()

-- Adicionar opções
menu:addOption("Opção 1", function() print("Opção 1 selecionada") end)
menu:addOption("Opção 2", function() print("Opção 2 selecionada") end)

-- Configurar passo de rolagem
menu:setScrollbarStep(20)

-- Exibir menu
menu:display({x = 100, y = 100})
```

---

### **5. UIMoveableTabBar - Barra de Abas Movível**

O `UIMoveableTabBar` é uma barra de abas que permite reordenação por drag & drop.

#### **Características Principais:**
- **Drag & Drop**: Reordenação de abas por arrastar
- **Navegação**: Navegação entre abas
- **Menus Contextuais**: Menus de clique direito
- **Drop Targets**: Áreas de destino para drop

#### **API Principal:**

```lua
-- Criação de barra de abas movível
local tabBar = UIMoveableTabBar.create()

-- Adicionar abas
local tab1 = tabBar:addTab("Aba 1", panel1)
local tab2 = tabBar:addTab("Aba 2", panel2)

-- Configurar espaçamento
tabBar:setTabSpacing(5)

-- Configurar área de drop
tabBar:setDropTarget(dropWidget, function(tabBar, draggedTab)
    print("Tab dropada em:", dropWidget:getId())
end)

-- Mover aba programaticamente
tabBar:moveTab(tab1, 1) -- Move uma posição para frente
```

#### **Eventos Disponíveis:**
- `onTabDrop`: Chamado quando uma aba é dropada
- `onTabLeftClick`: Chamado no clique direito da aba

---

### **6. UISplitter - Divisor de Painéis**

O `UISplitter` permite redimensionar painéis adjacentes.

#### **Características Principais:**
- **Redimensionamento**: Redimensionamento de painéis
- **Orientação**: Vertical ou horizontal
- **Margens Relativas**: Suporte a margens relativas
- **Feedback Visual**: Feedback visual durante o redimensionamento

#### **API Principal:**

```lua
-- Criação de splitter
local splitter = UISplitter.create()

-- Configurar orientação
splitter:setOrientation('vertical') -- ou 'horizontal'

-- Configurar margem relativa
splitter:setRelativeMargin(true)

-- Verificar se pode atualizar margem
local canUpdate = splitter:canUpdateMargin(newMargin)
```

---

### **7. UIInputBox - Caixa de Entrada Avançada**

O `UIInputBox` é uma caixa de diálogo especializada para entrada de dados.

#### **Características Principais:**
- **Múltiplos Campos**: Suporte a diferentes tipos de campos
- **Validação**: Validação de entrada
- **Callbacks**: Callbacks para OK e Cancel
- **Estilização**: Estilos personalizáveis

#### **Tipos de Campos Disponíveis:**

```lua
-- Criação de input box
local inputBox = UIInputBox.create("Título", okCallback, cancelCallback)

-- Campo de texto simples
inputBox:addLineEdit("Nome:", "Valor padrão", 50)

-- Campo de texto multilinha
inputBox:addTextEdit("Descrição:", "Texto padrão", 100, 3)

-- Checkbox
inputBox:addCheckBox("Ativar opção", true)

-- ComboBox
inputBox:addComboBox("Categoria:", "Opção 1", "Opção 2", "Opção 3")

-- SpinBox
inputBox:addSpinBox("Quantidade:", 0, 100, 50, 5)

-- Exibir
inputBox:display("OK", "Cancelar")
```

---

### **8. UIRadioGroup - Grupo de Radio Buttons**

O `UIRadioGroup` gerencia um grupo de radio buttons com seleção única.

#### **Características Principais:**
- **Seleção Única**: Apenas um item selecionado por vez
- **Gerenciamento Automático**: Gerenciamento automático de estados
- **Eventos**: Eventos de mudança de seleção

#### **API Principal:**

```lua
-- Criação de grupo de radio
local radioGroup = UIRadioGroup.create()

-- Adicionar widgets
radioGroup:addWidget(radioButton1)
radioGroup:addWidget(radioButton2)
radioGroup:addWidget(radioButton3)

-- Selecionar widget
radioGroup:selectWidget(radioButton2)

-- Obter widget selecionado
local selected = radioGroup:getSelectedWidget()

-- Limpar seleção
radioGroup:clearSelected()
```

#### **Eventos Disponíveis:**
- `onSelectionChange`: Chamado quando a seleção muda

---

### **9. UIImageView - Visualizador de Imagens Avançado**

O `UIImageView` é um widget especializado para exibição e manipulação de imagens.

#### **Características Principais:**
- **Zoom**: Zoom in/out com roda do mouse
- **Pan**: Arrastar para mover a imagem
- **Posicionamento**: Posicionamento preciso da imagem
- **Drag & Drop**: Suporte a drag & drop

#### **API Principal:**

```lua
-- Criação de image view
local imageView = UIImageView.create()

-- Carregar imagem
imageView:setImageSource("path/to/image.png")

-- Configurar zoom
imageView:setZoom(1.5)

-- Mover imagem
imageView:move(100, 50)

-- Zoom in/out
imageView:zoomIn(centerX, centerY)
imageView:zoomOut(centerX, centerY)
```

---

## 🔧 **Sistema de Drag & Drop**

O OTClient possui um sistema robusto de drag & drop implementado em vários widgets.

### **Widgets com Suporte a Drag & Drop:**

#### **1. UIWindow**
```lua
-- Configurar como arrastável
window:setDraggable(true)

-- Eventos de drag
window.onDragEnter = function(mousePos)
    -- Lógica quando o drag inicia
end

window.onDragMove = function(mousePos, mouseMoved)
    -- Lógica durante o drag
end

window.onDragLeave = function(droppedWidget, mousePos)
    -- Lógica quando o drag termina
end
```

#### **2. UIMiniWindow**
```lua
-- Drag com reordenação automática
miniWindow:setDraggable(true)

-- Configurar restrições
miniWindow.moveOnlyToMain = true -- Só pode mover para painel principal
```

#### **3. UIMoveableTabBar**
```lua
-- Configurar abas como movíveis
tabBar.tabsMoveable = true

-- Configurar área de drop
tabBar:setDropTarget(dropWidget, callback)
```

---

## 🎨 **Sistema de Efeitos**

O OTClient possui um sistema de efeitos visuais para widgets.

### **Efeitos Disponíveis:**

#### **1. Fade In/Out**
```lua
-- Fade in
g_effects.fadeIn(widget, 300) -- 300ms

-- Fade out
g_effects.fadeOut(widget, 300) -- 300ms

-- Cancelar fade
g_effects.cancelFade(widget)
```

#### **2. Blink (Piscar)**
```lua
-- Iniciar blink
g_effects.startBlink(widget, 2000, 500) -- 2s duração, 500ms intervalo

-- Parar blink
g_effects.stopBlink(widget)
```

---

## 📋 **Exemplos Práticos**

### **Exemplo 1: Tabela com Dados Dinâmicos**

```lua
-- Criar tabela
local table = UITable.create()
table:setId("playerTable")

-- Adicionar cabeçalho
table:addHeader({
    {text = "Jogador", width = 120},
    {text = "Nível", width = 60},
    {text = "HP", width = 80},
    {text = "Status", width = 80}
})

-- Adicionar dados
local players = {
    {name = "Player1", level = 50, hp = 100, status = "Online"},
    {name = "Player2", level = 45, hp = 85, status = "Away"},
    {name = "Player3", level = 60, hp = 120, status = "Online"}
}

for _, player in ipairs(players) do
    table:addRow({
        {text = player.name, style = "TableCell"},
        {text = tostring(player.level), style = "TableCell"},
        {text = tostring(player.hp), style = "TableCell"},
        {text = player.status, style = "TableCell"}
    })
end

-- Configurar eventos
table.onSelectionChange = function(table, selectedRow, previousRow)
    if selectedRow then
        print("Jogador selecionado:", selectedRow:getChildByIndex(1):getText())
    end
end
```

### **Exemplo 2: Área de Rolagem com Conteúdo Dinâmico**

```lua
-- Criar área de rolagem
local scrollArea = UIScrollArea.create()
scrollArea:setId("contentArea")

-- Criar scrollbar
local scrollBar = UIScrollBar.create()
scrollBar:setOrientation('vertical')
scrollBar:setRange(0, 1000)

-- Conectar scrollbar à área
scrollArea:setVerticalScrollBar(scrollBar)

-- Adicionar conteúdo dinâmico
local content = g_ui.createWidget("UIVerticalLayout", scrollArea)
for i = 1, 50 do
    local item = g_ui.createWidget("UILabel", content)
    item:setText("Item " .. i)
    item:setHeight(30)
end

-- Configurar eventos
scrollArea.onScrollChange = function(scrollArea, virtualOffset)
    print("Posição de rolagem:", virtualOffset.y)
end
```

### **Exemplo 3: Barra de Abas Movível**

```lua
-- Criar barra de abas
local tabBar = UIMoveableTabBar.create()
tabBar:setId("mainTabBar")

-- Criar painéis de conteúdo
local panel1 = g_ui.createWidget("UIPanel")
local panel2 = g_ui.createWidget("UIPanel")
local panel3 = g_ui.createWidget("UIPanel")

-- Adicionar conteúdo aos painéis
local label1 = g_ui.createWidget("UILabel", panel1)
label1:setText("Conteúdo da Aba 1")

local label2 = g_ui.createWidget("UILabel", panel2)
label2:setText("Conteúdo da Aba 2")

local label3 = g_ui.createWidget("UILabel", panel3)
label3:setText("Conteúdo da Aba 3")

-- Adicionar abas
local tab1 = tabBar:addTab("Aba 1", panel1)
local tab2 = tabBar:addTab("Aba 2", panel2)
local tab3 = tabBar:addTab("Aba 3", panel3)

-- Configurar área de drop
local dropZone = g_ui.createWidget("UIPanel")
dropZone:setId("dropZone")
tabBar:setDropTarget(dropZone, function(tabBar, draggedTab)
    print("Aba dropada na zona:", draggedTab:getText())
end)
```

---

## 🎯 **Boas Práticas**

### **1. Performance**
- **Lazy Loading**: Carregue widgets apenas quando necessário
- **Reutilização**: Reutilize widgets quando possível
- **Limpeza**: Sempre limpe eventos e referências

### **2. Usabilidade**
- **Feedback Visual**: Forneça feedback visual para ações
- **Consistência**: Mantenha consistência na interface
- **Acessibilidade**: Considere navegação por teclado

### **3. Manutenibilidade**
- **Modularização**: Divida interfaces complexas em módulos
- **Documentação**: Documente widgets customizados
- **Testes**: Teste widgets em diferentes cenários

---

## 🔗 **Integração com Outros Sistemas**

### **1. Sistema de Eventos**
Todos os widgets avançados se integram com o sistema de eventos do OTClient:

```lua
-- Conectar eventos
connect(widget, {
    onValueChange = function(widget, value)
        -- Lógica quando o valor muda
    end,
    onSelectionChange = function(widget, selected, previous)
        -- Lógica quando a seleção muda
    end
})
```

### **2. Sistema de Estilos**
Os widgets avançados suportam estilização via OTUI:

```otui
AdvancedTable < UITable
  table-data: tableData
  column-style: TableCell
  row-style: TableRow
  header-column-style: TableHeaderCell
  header-row-style: TableHeaderRow
```

### **3. Sistema de Layouts**
Integração com layouts para posicionamento automático:

```lua
-- Layout vertical
local layout = UIVerticalLayout.create()
layout:setSpacing(5)
layout:setFitChildren(true)

-- Layout horizontal
local layout = UIHorizontalLayout.create()
layout:setSpacing(10)
layout:setFitChildren(false)
```

---

## 📚 **Referências**

### **Arquivos de Código-Fonte:**
- `modules/corelib/ui/uitable.lua` - Implementação de tabelas
- `modules/corelib/ui/uiscrollarea.lua` - Área de rolagem
- `modules/corelib/ui/uiscrollbar.lua` - Barra de rolagem
- `modules/corelib/ui/uipopupscrollmenu.lua` - Menu popup com rolagem
- `modules/corelib/ui/uimovabletabbar.lua` - Barra de abas movível
- `modules/corelib/ui/uisplitter.lua` - Divisor de painéis
- `modules/corelib/ui/uiinputbox.lua` - Caixa de entrada avançada
- `modules/corelib/ui/uiradiogroup.lua` - Grupo de radio buttons
- `modules/corelib/ui/uiimageview.lua` - Visualizador de imagens

### **Estilos OTUI Relacionados:**
- `data/styles/10-tables.otui` - Estilos para tabelas
- `data/styles/10-scrollbars.otui` - Estilos para scrollbars
- `data/styles/10-tabs.otui` - Estilos para abas

---

**Story Completa**: UI-009: Widgets Avançados  
**Status**: ✅ **Concluída**  
**Próximo**: UI-010: Sistema de Animações 