
# 🪟 Sistema de Modais e Diálogos

<div class="info"> O Sistema de Modais e Diálogos do OTClient oferece funcionalidades avançadas para criar janelas modais, diálogos de confirmação e interfaces de interação com o usuário.

## 📋 Índice
- [#Visão Geral](#Visão Geral.md)
- [#Componentes do Sistema](#Componentes do Sistema.md)
- [#Implementação Prática](#Implementação Prática.md)
- [#Exemplos Práticos](#Exemplos Práticos.md)
- [#Melhores Práticas](#Melhores Práticas.md)

---

## 🎯 Visão Geral

O **Sistema de Modais e Diálogos** do OTClient oferece funcionalidades avançadas para criar janelas modais, diálogos de confirmação e interfaces de interação com o usuário. O sistema é integrado com o protocolo do jogo e oferece diferentes tipos de modais.

### 🎨 **Características Principais**

- **ModalDialog**: Diálogos do servidor com botões e escolhas
- **UIMessageBox**: Caixas de mensagem customizáveis
- **Janelas Modais**: Interfaces que bloqueiam interação
- **Sistema de Botões**: Configuração flexível de ações
- **Integração com Jogo**: Comunicação com servidor
- **Estilização Avançada**: Temas e aparência customizável

---

## 🔧 Componentes do Sistema

### 🏗️ **Arquitetura do Sistema**

```
Sistema de Modais
   │
   ├─ ModalDialog (Servidor)
   │   ├─ Título e Mensagem
   │   ├─ Botões Configuráveis
   │   ├─ Lista de Escolhas
   │   └─ Callbacks de Resposta
   │
   ├─ UIMessageBox (Cliente)
   │   ├─ Título Customizável
   │   ├─ Conteúdo Flexível
   │   ├─ Botões Dinâmicos
   │   └─ Callbacks de Ação
   │
   ├─ Janelas Modais
   │   ├─ setModal(true)
   │   ├─ Bloqueio de Interação
   │   └─ Gerenciamento de Foco
   │
   └─ Sistema de Eventos
       ├─ onEnter/onEscape
       ├─ Keyboard Bindings
       └─ Auto-focus
```

### 🎭 **Tipos de Modais**

#### 🎮 **ModalDialog (Servidor)**

Diálogos enviados pelo servidor do jogo com botões e escolhas predefinidas.

#### Nível Basic
```lua
-- Estrutura do ModalDialog
{
    id = windowId,           -- ID único do diálogo
    title = "Título",        -- Título da janela
    message = "Mensagem",    -- Texto principal
    buttons = {              -- Lista de botões
        {id = 1, text = "OK"},
        {id = 2, text = "Cancelar"}
    },
    choices = {              -- Lista de escolhas (opcional)
        {id = 1, text = "Escolha 1"},
        {id = 2, text = "Escolha 2"}
    },
    enterButton = 1,         -- Botão padrão (Enter)
    escapeButton = 2         -- Botão de escape (ESC)
}
```

#### Nível Intermediate
```lua
-- Estrutura do ModalDialog
{
    id = windowId,           -- ID único do diálogo
    title = "Título",        -- Título da janela
    message = "Mensagem",    -- Texto principal
    buttons = {              -- Lista de botões
        {id = 1, text = "OK"},
        {id = 2, text = "Cancelar"}
    },
    choices = {              -- Lista de escolhas (opcional)
        {id = 1, text = "Escolha 1"},
        {id = 2, text = "Escolha 2"}
    },
    enterButton = 1,         -- Botão padrão (Enter)
    escapeButton = 2         -- Botão de escape (ESC)
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
-- Estrutura do ModalDialog
{
    id = windowId,           -- ID único do diálogo
    title = "Título",        -- Título da janela
    message = "Mensagem",    -- Texto principal
    buttons = {              -- Lista de botões
        {id = 1, text = "OK"},
        {id = 2, text = "Cancelar"}
    },
    choices = {              -- Lista de escolhas (opcional)
        {id = 1, text = "Escolha 1"},
        {id = 2, text = "Escolha 2"}
    },
    enterButton = 1,         -- Botão padrão (Enter)
    escapeButton = 2         -- Botão de escape (ESC)
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

#### 💬 **UIMessageBox (Cliente)**

Caixas de mensagem criadas pelo cliente para confirmações e notificações.

#### Nível Basic
```lua
-- Estrutura do UIMessageBox
{
    title = "Título",        -- Título da janela
    message = "Mensagem",    -- Conteúdo principal
    buttons = {              -- Botões customizáveis
        {text = "OK", callback = function() end},
        {text = "Cancelar", callback = function() end}
    },
    onEnter = callback,      -- Callback para Enter
    onEscape = callback      -- Callback para Escape
}
```

#### Nível Intermediate
```lua
-- Estrutura do UIMessageBox
{
    title = "Título",        -- Título da janela
    message = "Mensagem",    -- Conteúdo principal
    buttons = {              -- Botões customizáveis
        {text = "OK", callback = function() end},
        {text = "Cancelar", callback = function() end}
    },
    onEnter = callback,      -- Callback para Enter
    onEscape = callback      -- Callback para Escape
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
-- Estrutura do UIMessageBox
{
    title = "Título",        -- Título da janela
    message = "Mensagem",    -- Conteúdo principal
    buttons = {              -- Botões customizáveis
        {text = "OK", callback = function() end},
        {text = "Cancelar", callback = function() end}
    },
    onEnter = callback,      -- Callback para Enter
    onEscape = callback      -- Callback para Escape
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

#### 🪟 **Janelas Modais Customizadas**

Janelas criadas pelo desenvolvedor com comportamento modal.

```lua
-- Estrutura de Janela Modal
    --  Estrutura de Janela Modal (traduzido)
{
    modal = true,            -- Comportamento modal
    draggable = true,        -- Arrastável
    focusable = true,        -- Pode receber foco
    onEnter = callback,      -- Callback Enter
    onEscape = callback      -- Callback Escape
}
```

---

## 💡 Implementação Prática

### 🐍 **API Lua**

#### 📦 **Métodos de ModalDialog**

#### Nível Basic
```lua
-- Processar diálogo modal do servidor
g_game.processModalDialog(id, title, message, buttons, enterButton, escapeButton, choices, priority)

-- Responder ao diálogo modal
g_game.answerModalDialog(id, buttonId, choice)

-- Evento de diálogo modal
g_game.onModalDialog = function(id, title, message, buttons, enterButton, escapeButton, choices, priority)
    -- Implementar lógica do diálogo
end
```

#### Nível Intermediate
```lua
-- Processar diálogo modal do servidor
g_game.processModalDialog(id, title, message, buttons, enterButton, escapeButton, choices, priority)

-- Responder ao diálogo modal
g_game.answerModalDialog(id, buttonId, choice)

-- Evento de diálogo modal
g_game.onModalDialog = function(id, title, message, buttons, enterButton, escapeButton, choices, priority)
    -- Implementar lógica do diálogo
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
-- Processar diálogo modal do servidor
g_game.processModalDialog(id, title, message, buttons, enterButton, escapeButton, choices, priority)

-- Responder ao diálogo modal
g_game.answerModalDialog(id, buttonId, choice)

-- Evento de diálogo modal
g_game.onModalDialog = function(id, title, message, buttons, enterButton, escapeButton, choices, priority)
    -- Implementar lógica do diálogo
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

#### 🎯 **Métodos de UIMessageBox**

```lua
-- Criar e exibir message box
    --  Criar e exibir message box (traduzido)
UIMessageBox.display(title, message, buttons, onEnterCallback, onEscapeCallback)

-- Criar message box customizada
    --  Criar message box customizada (traduzido)
local messageBox = g_ui.createWidget('MessageBoxWindow', rootWidget)
messageBox:setText(title)
messageBox:addButton(text, callback)
```

#### 🪟 **Métodos de Janelas Modais**

```lua
-- Configurar janela como modal
    --  Configurar janela como modal (traduzido)
window:setModal(true)

-- Gerenciar visibilidade
    --  Gerenciar visibilidade (traduzido)
window:show()
window:hide()

-- Gerenciar foco
    --  Gerenciar foco (traduzido)
window:focus()
window:raise()
window:lower()

-- Eventos de teclado
    --  Eventos de teclado (traduzido)
window.onEnter = function(widget) end
window.onEscape = function(widget) end
```

### 🎮 **Implementação Completa do ModalDialog**

#### Inicialização e Configuração
```lua
-- Variável global para o diálogo modal
modalDialog = nil

-- Inicializar sistema de modais
function init()
    g_ui.importStyle('modaldialog')
    
    connect(g_game, {
        onModalDialog = onModalDialog,
        onGameEnd = destroyDialog
    })
    
    -- Verificar se já existe diálogo
    local dialog = rootWidget:recursiveGetChildById('modalDialog')
    if dialog then
        modalDialog = dialog
    end
end

-- Destruir diálogo modal
function destroyDialog()
```

#### Funcionalidade 1
```lua
    if modalDialog then
        modalDialog:destroy()
        modalDialog = nil
    end
end

-- Processar diálogo modal do servidor
function onModalDialog(id, title, message, buttons, enterButton, escapeButton, choices, priority)
    -- Evitar múltiplos diálogos
    if modalDialog then
        return
    end
    
    -- Criar widget do diálogo
    modalDialog = g_ui.createWidget('ModalDialog', rootWidget)
    
    -- Configurar elementos do diálogo
    local messageLabel = modalDialog:getChildById('messageLabel')
    local choiceList = modalDialog:getChildById('choiceList')
    local choiceScrollbar = modalDialog:getChildById('choiceScrollBar')
    local buttonsPanel = modalDialog:getChildById('buttonsPanel')
    
    -- Definir título e mensagem
    modalDialog:setText(title)
    messageLabel:setText(message)
    
    -- Configurar lista de escolhas
    local labelHeight
    for i = 1, #choices do
        local choiceId = choices[i][1]
        local choiceName = choices[i][2]
        
        local label = g_ui.createWidget('ChoiceListLabel', choiceList)
        label.choiceId = choiceId
        label:setText(choiceName)
        label:setPhantom(false)
        
        if not labelHeight then
            labelHeight = label:getHeight()
        end
```

#### Funcionalidade 2
```lua
    end
    
    -- Focar primeira escolha
    choiceList:focusChild(choiceList:getFirstChild())
    
    -- Configurar navegação por teclado
    g_keyboard.bindKeyPress('Down', function()
        choiceList:focusNextChild(KeyboardFocusReason)
    end, modalDialog)
    
    g_keyboard.bindKeyPress('Up', function()
        choiceList:focusPreviousChild(KeyboardFocusReason)
    end, modalDialog)
    
    -- Criar botões
    local buttonsWidth = 0
    for i = 1, #buttons do
        local buttonId = buttons[i][1]
        local buttonText = buttons[i][2]
        
        local button = g_ui.createWidget('ModalButton', buttonsPanel)
        button:setText(buttonText)
        button.onClick = function(self)
            local focusedChoice = choiceList:getFocusedChild()
            local choice = 0xFF
            if focusedChoice then
                choice = focusedChoice.choiceId
            end
```

#### Funcionalidade 3
```lua
            g_game.answerModalDialog(id, buttonId, choice)
            destroyDialog()
        end
        buttonsWidth = buttonsWidth + button:getWidth() + button:getMarginLeft() + button:getMarginRight()
    end
    
    -- Calcular dimensões
    local additionalHeight = 0
    if #choices > 0 then
        choiceList:setVisible(true)
        choiceScrollbar:setVisible(true)
        
        additionalHeight = math.min(modalDialog.maximumChoices, 
                                   math.max(modalDialog.minimumChoices, #choices)) * labelHeight
        additionalHeight = additionalHeight + choiceList:getPaddingTop() + choiceList:getPaddingBottom()
    end
    
    -- Ajustar tamanho da janela
    local horizontalPadding = modalDialog:getPaddingLeft() + modalDialog:getPaddingRight()
    buttonsWidth = buttonsWidth + horizontalPadding
    
    modalDialog:setWidth(math.min(modalDialog.maximumWidth,
                                  math.max(buttonsWidth, messageLabel:getWidth(), modalDialog.minimumWidth)))
    
    messageLabel:setWidth(math.min(modalDialog.maximumWidth,
                                   math.max(buttonsWidth, messageLabel:getWidth(), modalDialog.minimumWidth)) -
                              horizontalPadding)
    
    modalDialog:setHeight(modalDialog:getHeight() + additionalHeight + messageLabel:getHeight() - 8)
    
    -- Configurar callbacks de teclado
    local enterFunc = function()
        local focusedChoice = choiceList:getFocusedChild()
        local choice = 0xFF
        if focusedChoice then
            choice = focusedChoice.choiceId
        end
```

#### Finalização
```lua
        g_game.answerModalDialog(id, enterButton, choice)
        destroyDialog()
    end
    
    local escapeFunc = function()
        local focusedChoice = choiceList:getFocusedChild()
        local choice = 0xFF
        if focusedChoice then
            choice = focusedChoice.choiceId
        end
        g_game.answerModalDialog(id, escapeButton, choice)
        destroyDialog()
    end
    
    modalDialog.onEnter = enterFunc
    modalDialog.onEscape = escapeFunc
end
```

### 🎨 **Estilo OTUI para ModalDialog**

```otui
ChoiceListLabel < Label
  font: verdana-11px-monochrome
  background-color: alpha
  text-offset: 2 0
  focusable: true

  $focus:
    background-color: #00000055
    color: #ffffff

ChoiceList < TextList
  id: choiceList
  vertical-scrollbar: choiceScrollBar
  anchors.fill: parent
  anchors.top: prev.bottom
  anchors.bottom: next.top
  margin-top: 4
  margin-bottom: 10
  focusable: false
  visible: false

ChoiceScrollBar < VerticalScrollBar
  id: choiceScrollBar
  anchors.top: choiceList.top
  anchors.bottom: choiceList.bottom
  anchors.right: choiceList.right
  step: 14
  pixels-scroll: true
  visible: false

ModalButton < Button
  text-auto-resize: true
  margin-top: 2
  margin-bottom: 2
  margin-left: 2

  $pressed:
    text-offset: 0 0

ModalDialog < MainWindow
  id: modalDialog
  size: 280 97
  &minimumWidth: 200
  &maximumWidth: 600
  &minimumChoices: 4
  &maximumChoices: 10

  Label
    id: messageLabel
    anchors.top: parent.top
    anchors.left: parent.left
    text-align: left
    text-auto-resize: true
    text-wrap: true

  ChoiceList

  HorizontalSeparator
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.bottom: next.top

  Panel
    id: buttonsPanel
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.bottom: parent.bottom
    height: 24
    layout: horizontalBox
      align-right: true

  ChoiceScrollBar
```

---

## 💡 Exemplos Práticos

### 🎯 **Exemplo 1: Sistema de Confirmação**

```lua
local ConfirmationSystem = {}

function ConfirmationSystem.showConfirmation(title, message, onConfirm, onCancel)
    -- Função: ConfirmationSystem
    local buttons = {
        {text = "Confirmar", callback = function()
            if onConfirm then
    -- Verificação condicional
                onConfirm()
            end
        end},
        {text = "Cancelar", callback = function()
            if onCancel then
    -- Verificação condicional
                onCancel()
            end
        end}
    }
    
    local messageBox = UIMessageBox.display(title, message, buttons)
    
    -- Configurar callbacks de teclado
    --  Configurar callbacks de teclado (traduzido)
    messageBox.onEnter = function()
        if onConfirm then
    -- Verificação condicional
            onConfirm()
        end
        messageBox:destroy()
    end
    
    messageBox.onEscape = function()
        if onCancel then
    -- Verificação condicional
            onCancel()
        end
        messageBox:destroy()
    end
    
    return messageBox
end

-- Uso
    --  Uso (traduzido)
ConfirmationSystem.showConfirmation(
    "Confirmar Ação",
    "Tem certeza que deseja deletar este item?",
    function()
        print("Item deletado!")
    end,
    function()
        print("Ação cancelada!")
    end
)
```

### 🎨 **Exemplo 2: Sistema de Notificação**

```lua
local NotificationSystem = {}

function NotificationSystem.showNotification(title, message, duration)
    -- Função: NotificationSystem
    duration = duration or 3000
    
    local buttons = {
        {text = "OK", callback = function()
            -- Fechar notificação
        end}
    }
    
    local messageBox = UIMessageBox.display(title, message, buttons)
    
    -- Auto-fechar após duração
    scheduleEvent(function()
        if messageBox then
    -- Verificação condicional
            messageBox:destroy()
        end
    end, duration)
    
    return messageBox
end

-- Uso
    --  Uso (traduzido)
NotificationSystem.showNotification(
    "Sucesso!",
    "Item adicionado ao inventário com sucesso!",
    2000
)
```

### 🪟 **Exemplo 3: Modal Customizado**

#### Inicialização e Configuração
```lua
local CustomModalSystem = {}

function CustomModalSystem.createCustomModal(title, content, buttons)
    local modal = g_ui.createWidget('MainWindow', rootWidget)
    modal:setModal(true)
    modal:setText(title)
    modal:setSize({width = 400, height = 300})
    
    -- Configurar conteúdo
    local contentLabel = g_ui.createWidget('Label', modal)
    contentLabel:setText(content)
    contentLabel:setPosition({x = 20, y = 50})
    contentLabel:setSize({width = 360, height = 200})
    contentLabel:setTextWrap(true)
    
    -- Configurar botões
    local buttonPanel = g_ui.createWidget('Panel', modal)
    buttonPanel:setPosition({x = 20, y = 250})
    buttonPanel:setSize({width = 360, height = 30})
    
    local buttonWidth = 360 / #buttons
    for i, buttonData in ipairs(buttons) do
        local button = g_ui.createWidget('Button', buttonPanel)
        button:setText(buttonData.text)
        button:setPosition({x = (i-1) * buttonWidth, y = 0})
        button:setSize({width = buttonWidth - 5, height = 25})
        
        button.onClick = function()
            if buttonData.callback then
                buttonData.callback()
            end
```

#### Funcionalidade 1
```lua
            modal:destroy()
        end
    end
    
    -- Configurar callbacks de teclado
    modal.onEnter = function()
        if buttons[1] and buttons[1].callback then
            buttons[1].callback()
        end
        modal:destroy()
    end
    
    modal.onEscape = function()
        if buttons[#buttons] and buttons[#buttons].callback then
            buttons[#buttons].callback()
        end
        modal:destroy()
    end
    
    modal:show()
    modal:focus()
    
    return modal
end
```

#### Finalização
```lua

-- Uso
CustomModalSystem.createCustomModal(
    "Configurações",
    "Configure as opções do seu personagem:",
    {
        {text = "Salvar", callback = function()
            print("Configurações salvas!")
        end},
        {text = "Cancelar", callback = function()
            print("Configurações canceladas!")
        end}
    }
)
```

---

## ✅ Melhores Práticas

### 🎯 **Uso Eficiente**

#### Inicialização e Configuração
```lua
-- ✅ BOM: Sempre destruir modais após uso
function showModalAndCleanup(title, message)
    local modal = UIMessageBox.display(title, message, {
        {text = "OK", callback = function()
            modal:destroy()  -- Sempre destruir
        end}
    })
    
    -- Callback de escape também deve destruir
    modal.onEscape = function()
        modal:destroy()
    end
end

-- ✅ BOM: Verificar se modal já existe
function showUniqueModal(title, message)
    if g_ui.getWidgetById('uniqueModal') then
        return  -- Modal já existe
    end
    
    local modal = g_ui.createWidget('MainWindow', rootWidget)
    modal:setId('uniqueModal')
    modal:setModal(true)
    -- ... configuração
end
```

#### Funcionalidade 1
```lua

-- ✅ BOM: Usar callbacks para flexibilidade
function createModalWithCallbacks(title, content, callbacks)
    local modal = g_ui.createWidget('MainWindow', rootWidget)
    modal:setModal(true)
    modal:setText(title)
    
    if callbacks.onShow then
        callbacks.onShow(modal)
    end
    
    if callbacks.onHide then
        modal.onDestroy = function()
            callbacks.onHide()
        end
    end
    
    return modal
end

-- ❌ EVITE: Não destruir modais
function badModalExample(title, message)
```

#### Finalização
```lua
    local modal = UIMessageBox.display(title, message, {
        {text = "OK", callback = function()
            -- Modal não é destruído - vazamento de memória!
        end}
    })
end

-- ❌ EVITE: Múltiplos modais simultâneos
function badMultipleModals()
    -- Pode causar problemas de foco e UX
    UIMessageBox.display("Modal 1", "Mensagem 1", {{text = "OK"}})
    UIMessageBox.display("Modal 2", "Mensagem 2", {{text = "OK"}})
end
```

### 🎨 **Feedback Visual**

```lua
-- ✅ BOM: Feedback visual para modais
    --  ✅ BOM: Feedback visual para modais (traduzido)
function showModalWithFeedback(title, message, type)
    -- Função: showModalWithFeedback
    local colors = {
        success = '#27ae60',
        error = '#e74c3c',
        warning = '#f39c12',
        info = '#3498db'
    }
    
    local modal = UIMessageBox.display(title, message, {
        {text = "OK", callback = function()
            modal:destroy()
        end}
    })
    
    -- Aplicar cor baseada no tipo
    --  Aplicar cor baseada no tipo (traduzido)
    if colors[type] then
    -- Verificação condicional
        modal:getChildById('title'):setColor(colors[type])
    end
end

-- ✅ BOM: Animações suaves
function showModalWithAnimation(title, message)
    -- Função: showModalWithAnimation
    local modal = g_ui.createWidget('MainWindow', rootWidget)
    modal:setModal(true)
    modal:setText(title)
    modal:setOpacity(0)
    
    -- Animação de entrada
    modal:setOpacity(0)
    modal:show()
    
    local animation = modal:createAnimation()
    animation:setDuration(200)
    animation:setOpacity(1)
    animation:start()
end
```

### 🔧 **Validação Robusta**

#### Inicialização e Configuração
```lua
-- ✅ BOM: Validação de parâmetros
function validateModalParams(title, message, buttons)
    if not title or type(title) ~= 'string' then
        error('Título deve ser uma string válida')
    end
    
    if not message or type(message) ~= 'string' then
        error('Mensagem deve ser uma string válida')
    end
    
    if not buttons or type(buttons) ~= 'table' then
        error('Botões deve ser uma tabela válida')
    end
    
    for i, button in ipairs(buttons) do
        if not button.text or not button.callback then
            error('Botão ' .. i .. ' deve ter text e callback')
        end
    end
end

-- ✅ BOM: Sistema de prioridade
local modalQueue = {}
local currentModal = nil

function showModalWithPriority(title, message, priority)
```

#### Funcionalidade 1
```lua
    priority = priority or 1
    
    table.insert(modalQueue, {
        title = title,
        message = message,
        priority = priority
    })
    
    table.sort(modalQueue, function(a, b)
        return a.priority > b.priority
    end)
    
    processModalQueue()
end

function processModalQueue()
    if currentModal or #modalQueue == 0 then
        return
    end
    
    local nextModal = table.remove(modalQueue, 1)
    currentModal = UIMessageBox.display(nextModal.title, nextModal.message, {
        {text = "OK", callback = function()
            currentModal:destroy()
            currentModal = nil
            processModalQueue()
        end}
```

#### Finalização
```lua
    })
end
```

O sistema de modais e diálogos oferece ferramentas poderosas para criar interfaces interativas e responsivas no OTClient. Seguindo as melhores práticas e utilizando os exemplos fornecidos, você pode criar modais robustos e eficientes que melhoram significativamente a experiência do usuário.

---

<div class="success"> **Navegação**
> **📚 Documentos Relacionados:**
> - [UI_System_Guide](UI_System_Guide.md) - Sistema de interface básico
> - [Animation_System_Guide](Animation_System_Guide.md) - Sistema de animações
> - [Drag_Drop_System_Guide](Drag_Drop_System_Guide.md) - Sistema de drag and drop
> - [UI_Tabs_System_Guide](UI_Tabs_System_Guide.md) - Sistema de tabs e abas
> 
> **🔗 Navegação Rápida:**
> - [Wiki_Index](Wiki_Index.md) - Voltar ao índice
> - [Cheat_Sheet](Cheat_Sheet.md) - Referência rápida
> - [Getting_Started_Guide](Getting_Started_Guide.md) - Comece aqui 
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

