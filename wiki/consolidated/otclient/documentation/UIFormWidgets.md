---
tags: [ui, form_widgets, otclient, documentation, habdel]
type: documentation
status: completed
priority: maximum
created: 2025-01-27
---

# 📝 UI-011: Widgets de Formulário

> [!info] **Story ID**: UI-011  
> **Categoria**: UI  
> **Status**: ✅ Completo  
> **Prioridade**: 🔥 **MÁXIMA**

## 📋 Índice
1. [Visão Geral](#visão-geral)
2. [Arquitetura dos Widgets de Formulário](#arquitetura-dos-widgets-de-formulário)
3. [Tipos de Widgets](#tipos-de-widgets)
4. [API Lua](#api-lua)
5. [Sistema de Validação](#sistema-de-validação)
6. [Exemplos Práticos](#exemplos-práticos)
7. [Integração com UIInputBox](#integração-com-uiinputbox)
8. [Melhores Práticas](#melhores-práticas)
9. [Performance e Otimização](#performance-e-otimização)

---

## 🎯 Visão Geral

Os **Widgets de Formulário** do OTClient fornecem controles especializados para entrada de dados, validação e interação com usuário. O sistema oferece uma ampla gama de componentes para criar formulários robustos e responsivos.

### 🎨 **Características Principais**

- **Controles Diversificados**: TextEdit, CheckBox, ComboBox, SpinBox, etc.
- **Sistema de Validação**: Validação em tempo real e feedback visual
- **Integração Completa**: Sistema UIInputBox para diálogos rápidos
- **Estilização Flexível**: Suporte a temas e customização visual
- **Eventos Avançados**: Callbacks para todas as interações
- **Acessibilidade**: Suporte a navegação por teclado e leitores de tela

---

## 🏗️ Arquitetura dos Widgets de Formulário

### 🎭 **Estrutura Hierárquica**

```
Widgets de Formulário
   │
   ├─ Controles de Texto
   │   ├─ UITextEdit (Campo de texto simples)
   │   ├─ MultilineTextEdit (Campo de texto múltiplas linhas)
   │   ├─ PasswordTextEdit (Campo de senha)
   │   └─ TextQtEdit (Campo de texto Qt)
   │
   ├─ Controles de Seleção
   │   ├─ UICheckBox (Caixa de seleção)
   │   ├─ UIComboBox (Lista suspensa)
   │   ├─ UISpinBox (Controle numérico)
   │   └─ UIScrollBar (Barra de rolagem)
   │
   ├─ Controles de Ação
   │   ├─ UIButton (Botão)
   │   ├─ UIInputBox (Caixa de diálogo)
   │   └─ UIProgressBar (Barra de progresso)
   │
   └─ Sistema de Validação
       ├─ Validadores de Entrada
       ├─ Feedback Visual
       └─ Tratamento de Erros
```

### 🔄 **Fluxo de Interação**

```
1. Criação do Widget
   ↓
2. Configuração de Propriedades
   ↓
3. Aplicação de Validação
   ↓
4. Interação do Usuário
   ↓
5. Validação em Tempo Real
   ↓
6. Feedback Visual
   ↓
7. Processamento de Dados
```

---

## 📦 Tipos de Widgets

### 🔤 **Controles de Texto**

#### UITextEdit
Campo de entrada de texto básico com suporte a edição, seleção e formatação.

```lua
-- Criação básica
local textEdit = g_ui.createWidget('UITextEdit', parent)
textEdit:setText('Texto inicial')
textEdit:setMaxLength(100)
textEdit:setEditable(true)

-- Configurações avançadas
textEdit:setMultiline(false)           -- Texto em uma linha
textEdit:setPasswordMode(true)         -- Modo senha
textEdit:setValidCharacters('a-zA-Z')  -- Caracteres permitidos
textEdit:setPlaceholder('Digite aqui...')

-- Eventos
    --  Eventos (traduzido)
textEdit.onTextChange = function(widget, text, oldText)
    print('Texto alterado:', text)
end

textEdit.onEnterPressed = function(widget)
    print('Enter pressionado')
end
```

#### MultilineTextEdit
Campo de texto para múltiplas linhas com suporte a quebra de linha.

```lua
local multilineEdit = g_ui.createWidget('MultilineTextEdit', parent)
multilineEdit:setMultiline(true)
multilineEdit:setTextWrap(true)
multilineEdit:setSize({width = 200, height = 100})

-- Configurar texto com quebras de linha
    --  Configurar texto com quebras de linha (traduzido)
multilineEdit:setText('Linha 1\nLinha 2\nLinha 3')
```

#### PasswordTextEdit
Campo de texto especializado para senhas com ocultação de caracteres.

#### Nível Basic
```lua
local passwordEdit = g_ui.createWidget('PasswordTextEdit', parent)
passwordEdit:setPasswordMode(true)
passwordEdit:setMaxLength(20)
passwordEdit:setPlaceholder('Digite sua senha...')

-- Toggle de visibilidade (se disponível)
passwordEdit:setTextHidden(true)
```

#### Nível Intermediate
```lua
local passwordEdit = g_ui.createWidget('PasswordTextEdit', parent)
passwordEdit:setPasswordMode(true)
passwordEdit:setMaxLength(20)
passwordEdit:setPlaceholder('Digite sua senha...')

-- Toggle de visibilidade (se disponível)
passwordEdit:setTextHidden(true)
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
local passwordEdit = g_ui.createWidget('PasswordTextEdit', parent)
passwordEdit:setPasswordMode(true)
passwordEdit:setMaxLength(20)
passwordEdit:setPlaceholder('Digite sua senha...')

-- Toggle de visibilidade (se disponível)
passwordEdit:setTextHidden(true)
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

### ☑️ **Controles de Seleção**

#### UICheckBox
Caixa de seleção para valores booleanos.

```lua
local checkBox = g_ui.createWidget('UICheckBox', parent)
checkBox:setText('Aceito os termos')
checkBox:setChecked(false)

-- Eventos
    --  Eventos (traduzido)
checkBox.onCheckChange = function(widget, checked)
    print('Estado alterado:', checked)
end
```

#### UIComboBox
Lista suspensa para seleção de opções.

```lua
local comboBox = g_ui.createWidget('UIComboBox', parent)

-- Adicionar opções
comboBox:addOption('Opção 1', 'value1')
comboBox:addOption('Opção 2', 'value2')
comboBox:addOption('Opção 3', 'value3')

-- Configurar opção padrão
comboBox:setCurrentOption('value1')

-- Eventos
    --  Eventos (traduzido)
comboBox.onOptionChange = function(widget, option)
    print('Opção selecionada:', option)
end
```

#### UISpinBox
Controle numérico com incremento/decremento.

```lua
local spinBox = g_ui.createWidget('UISpinBox', parent)

-- Configurar limites e valores
    --  Configurar limites e valores (traduzido)
spinBox:setMinimum(0)
spinBox:setMaximum(100)
spinBox:setValue(50)
spinBox:setStep(5)

-- Eventos
    --  Eventos (traduzido)
spinBox.onValueChange = function(widget, value)
    print('Valor alterado:', value)
end
```

### 🎯 **Controles de Ação**

#### UIButton
Botão para ações do usuário.

```lua
local button = g_ui.createWidget('UIButton', parent)
button:setText('Enviar')
button:setEnabled(true)

-- Eventos
    --  Eventos (traduzido)
button.onClick = function(widget)
    print('Botão clicado!')
end

button.onHoverChange = function(widget, hovered)
    if hovered then
    -- Verificação condicional
        widget:setBackgroundColor('#4CAF50')
    else
        widget:setBackgroundColor('#2196F3')
    end
end
```

#### UIProgressBar
Barra de progresso para indicar status.

```lua
local progressBar = g_ui.createWidget('UIProgressBar', parent)

-- Configurar progresso
    --  Configurar progresso (traduzido)
progressBar:setMinimum(0)
progressBar:setMaximum(100)
progressBar:setValue(75)

-- Animar progresso
    --  Animar progresso (traduzido)
local function animateProgress()
    local currentValue = progressBar:getValue()
    if currentValue < 100 then
    -- Verificação condicional
        progressBar:setValue(currentValue + 1)
        scheduleEvent(animateProgress, 50)
    end
end

animateProgress()
```

---

## 🐍 API Lua

### 📦 **Métodos Comuns**

#### Nível Basic
```lua
-- Configuração básica
widget:setEnabled(true)           -- Habilitar/desabilitar
widget:setVisible(true)           -- Mostrar/ocultar
widget:setFocusable(true)         -- Permitir foco
widget:setId('uniqueId')          -- Definir ID único

-- Posicionamento e tamanho
widget:setPosition({x = 100, y = 100})
widget:setSize({width = 200, height = 30})
widget:setRect({x = 100, y = 100, width = 200, height = 30})

-- Estilização
widget:setBackgroundColor('#FFFFFF')
widget:setBorderColor('#000000')
widget:setOpacity(1.0)
```

#### Nível Intermediate
```lua
-- Configuração básica
widget:setEnabled(true)           -- Habilitar/desabilitar
widget:setVisible(true)           -- Mostrar/ocultar
widget:setFocusable(true)         -- Permitir foco
widget:setId('uniqueId')          -- Definir ID único

-- Posicionamento e tamanho
widget:setPosition({x = 100, y = 100})
widget:setSize({width = 200, height = 30})
widget:setRect({x = 100, y = 100, width = 200, height = 30})

-- Estilização
widget:setBackgroundColor('#FFFFFF')
widget:setBorderColor('#000000')
widget:setOpacity(1.0)
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
-- Configuração básica
widget:setEnabled(true)           -- Habilitar/desabilitar
widget:setVisible(true)           -- Mostrar/ocultar
widget:setFocusable(true)         -- Permitir foco
widget:setId('uniqueId')          -- Definir ID único

-- Posicionamento e tamanho
widget:setPosition({x = 100, y = 100})
widget:setSize({width = 200, height = 30})
widget:setRect({x = 100, y = 100, width = 200, height = 30})

-- Estilização
widget:setBackgroundColor('#FFFFFF')
widget:setBorderColor('#000000')
widget:setOpacity(1.0)
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

### 🎯 **Métodos Específicos por Tipo**

#### UITextEdit
#### Nível Basic
```lua
-- Manipulação de texto
local text = textEdit:getText()
textEdit:appendText(' mais texto')
-- Cursor e seleção
local pos = textEdit:getCursorPos()
-- Configurações
```

#### Nível Intermediate
```lua
-- Manipulação de texto
textEdit:setText('Novo texto')
local text = textEdit:getText()
textEdit:clearText()
textEdit:appendText(' mais texto')

-- Cursor e seleção
textEdit:setCursorPos(5)
local pos = textEdit:getCursorPos()
textEdit:setSelection(0, 10)
textEdit:selectAll()

-- Configurações
textEdit:setMaxLength(100)
textEdit:setEditable(true)
textEdit:setMultiline(true)
textEdit:setPasswordMode(true)
textEdit:setValidCharacters('a-zA-Z0-9')
textEdit:setPlaceholder('Digite aqui...')
```

#### Nível Advanced
```lua
-- Manipulação de texto
textEdit:setText('Novo texto')
local text = textEdit:getText()
textEdit:clearText()
textEdit:appendText(' mais texto')

-- Cursor e seleção
textEdit:setCursorPos(5)
local pos = textEdit:getCursorPos()
textEdit:setSelection(0, 10)
textEdit:selectAll()

-- Configurações
textEdit:setMaxLength(100)
textEdit:setEditable(true)
textEdit:setMultiline(true)
textEdit:setPasswordMode(true)
textEdit:setValidCharacters('a-zA-Z0-9')
textEdit:setPlaceholder('Digite aqui...')
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

#### UICheckBox
```lua
-- Estado
    --  Estado (traduzido)
checkBox:setChecked(true)
local checked = checkBox:isChecked()
checkBox:toggle()

-- Texto
    --  Texto (traduzido)
checkBox:setText('Texto do checkbox')
local text = checkBox:getText()
```

#### UIComboBox
#### Nível Basic
```lua
-- Opções
comboBox:addOption('Texto', 'valor')
comboBox:addOption('Outro texto', 'outro_valor')
comboBox:clearOptions()

-- Seleção
comboBox:setCurrentOption('valor')
local current = comboBox:getCurrentOption()
local currentText = comboBox:getCurrentText()

-- Navegação
comboBox:selectNext()
comboBox:selectPrevious()
```

#### Nível Intermediate
```lua
-- Opções
comboBox:addOption('Texto', 'valor')
comboBox:addOption('Outro texto', 'outro_valor')
comboBox:clearOptions()

-- Seleção
comboBox:setCurrentOption('valor')
local current = comboBox:getCurrentOption()
local currentText = comboBox:getCurrentText()

-- Navegação
comboBox:selectNext()
comboBox:selectPrevious()
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
-- Opções
comboBox:addOption('Texto', 'valor')
comboBox:addOption('Outro texto', 'outro_valor')
comboBox:clearOptions()

-- Seleção
comboBox:setCurrentOption('valor')
local current = comboBox:getCurrentOption()
local currentText = comboBox:getCurrentText()

-- Navegação
comboBox:selectNext()
comboBox:selectPrevious()
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

#### UISpinBox
```lua
-- Valores
    --  Valores (traduzido)
spinBox:setValue(50)
local value = spinBox:getValue()

-- Limites
    --  Limites (traduzido)
spinBox:setMinimum(0)
spinBox:setMaximum(100)
spinBox:setStep(5)

-- Navegação
spinBox:stepUp()
spinBox:stepDown()
```

### 🎭 **Eventos e Callbacks**

```lua
-- Eventos de texto
    --  Eventos de texto (traduzido)
textEdit.onTextChange = function(widget, text, oldText)
    print('Texto alterado de', oldText, 'para', text)
end

textEdit.onEnterPressed = function(widget)
    print('Enter pressionado')
end

textEdit.onFocusChange = function(widget, focused)
    if focused then
    -- Verificação condicional
        print('Campo recebeu foco')
    else
        print('Campo perdeu foco')
    end
end

-- Eventos de seleção
checkBox.onCheckChange = function(widget, checked)
    print('Checkbox alterado:', checked)
end

comboBox.onOptionChange = function(widget, option)
    print('Opção selecionada:', option)
end

spinBox.onValueChange = function(widget, value)
    print('Valor alterado:', value)
end

-- Eventos de ação
button.onClick = function(widget)
    print('Botão clicado')
end

button.onHoverChange = function(widget, hovered)
    if hovered then
    -- Verificação condicional
        widget:setBackgroundColor('#4CAF50')
    else
        widget:setBackgroundColor('#2196F3')
    end
end
```

---

## ✅ Sistema de Validação

### 🎯 **Validação Básica**

#### Nível Basic
```lua
-- Validação de comprimento
function validateLength(text, minLength, maxLength)
    local length = string.len(text)
    return length >= minLength and length <= maxLength
end

-- Validação de email
function validateEmail(email)
    local pattern = '^[%w.]+@[%w]+%.[%w]+$'
    return string.match(email, pattern) ~= nil
end

-- Validação de números
function validateNumber(value, min, max)
    local num = tonumber(value)
    return num and num >= min and num <= max
end

-- Aplicar validação
textEdit.onTextChange = function(widget, text)
    if not validateLength(text, 3, 50) then
        widget:setBorderColor('#FF0000')
        widget:setTooltip('Texto deve ter entre 3 e 50 caracteres')
    else
        widget:setBorderColor('#00FF00')
        widget:setTooltip('')
    end
end
```

#### Nível Intermediate
```lua
-- Validação de comprimento
function validateLength(text, minLength, maxLength)
    local length = string.len(text)
    return length >= minLength and length <= maxLength
end

-- Validação de email
function validateEmail(email)
    local pattern = '^[%w.]+@[%w]+%.[%w]+$'
    return string.match(email, pattern) ~= nil
end

-- Validação de números
function validateNumber(value, min, max)
    local num = tonumber(value)
    return num and num >= min and num <= max
end

-- Aplicar validação
textEdit.onTextChange = function(widget, text)
    if not validateLength(text, 3, 50) then
        widget:setBorderColor('#FF0000')
        widget:setTooltip('Texto deve ter entre 3 e 50 caracteres')
    else
        widget:setBorderColor('#00FF00')
        widget:setTooltip('')
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
-- Validação de comprimento
function validateLength(text, minLength, maxLength)
    local length = string.len(text)
    return length >= minLength and length <= maxLength
end

-- Validação de email
function validateEmail(email)
    local pattern = '^[%w.]+@[%w]+%.[%w]+$'
    return string.match(email, pattern) ~= nil
end

-- Validação de números
function validateNumber(value, min, max)
    local num = tonumber(value)
    return num and num >= min and num <= max
end

-- Aplicar validação
textEdit.onTextChange = function(widget, text)
    if not validateLength(text, 3, 50) then
        widget:setBorderColor('#FF0000')
        widget:setTooltip('Texto deve ter entre 3 e 50 caracteres')
    else
        widget:setBorderColor('#00FF00')
        widget:setTooltip('')
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

### 🔧 **Sistema de Validação Avançado**

#### Inicialização e Configuração
```lua
local ValidationSystem = {}

-- Configuração de validadores
ValidationSystem.validators = {
    required = function(value)
        return value and string.len(value) > 0
    end,
    
    email = function(value)
        local pattern = '^[%w.]+@[%w]+%.[%w]+$'
        return string.match(value, pattern) ~= nil
    end,
    
    minLength = function(value, min)
        return string.len(value) >= min
    end,
    
    maxLength = function(value, max)
        return string.len(value) <= max
    end,
    
    pattern = function(value, pattern)
        return string.match(value, pattern) ~= nil
    end,
```

#### Funcionalidade 1
```lua
    
    range = function(value, min, max)
        local num = tonumber(value)
        return num and num >= min and num <= max
    end
}

-- Aplicar validação a um widget
function ValidationSystem.validate(widget, rules)
    local value = widget:getText()
    local errors = {}
    
    for rule, params in pairs(rules) do
        local validator = ValidationSystem.validators[rule]
        if validator then
            local isValid = validator(value, unpack(params))
            if not isValid then
                table.insert(errors, rule)
            end
        end
    end
```

#### Funcionalidade 2
```lua
    
    -- Aplicar feedback visual
    if #errors > 0 then
        widget:setBorderColor('#FF0000')
        widget:setTooltip('Erro: ' .. table.concat(errors, ', '))
        return false
    else
        widget:setBorderColor('#00FF00')
        widget:setTooltip('')
        return true
    end
end

-- Exemplo de uso
local emailField = g_ui.createWidget('UITextEdit', parent)
emailField.onTextChange = function(widget, text)
    ValidationSystem.validate(widget, {
        required = {},
        email = {},
        minLength = {5},
        maxLength = {100}
    })
```

#### Finalização
```lua
end
```

---

## 💡 Exemplos Práticos

### 🎯 **Exemplo 1: Formulário de Registro**

#### Inicialização e Configuração
```lua
local RegistrationForm = {}

function RegistrationForm.create(parent)
    local form = g_ui.createWidget('Panel', parent)
    form:setSize({width = 400, height = 500})
    form:setLayout('verticalBox')
    form:setPadding(20)
    
    -- Título
    local title = g_ui.createWidget('UILabel', form)
    title:setText('Registro de Usuário')
    title:setTextAlign('center')
    title:setHeight(30)
    
    -- Campo Nome
    local nameLabel = g_ui.createWidget('UILabel', form)
    nameLabel:setText('Nome:')
    nameLabel:setHeight(20)
    
    local nameField = g_ui.createWidget('UITextEdit', form)
    nameField:setHeight(30)
    nameField:setPlaceholder('Digite seu nome completo')
    nameField:setMaxLength(50)
    
    -- Campo Email
    local emailLabel = g_ui.createWidget('UILabel', form)
    emailLabel:setText('Email:')
    emailLabel:setHeight(20)
    
    local emailField = g_ui.createWidget('UITextEdit', form)
    emailField:setHeight(30)
    emailField:setPlaceholder('Digite seu email')
    emailField:setMaxLength(100)
    
    -- Campo Senha
    local passwordLabel = g_ui.createWidget('UILabel', form)
    passwordLabel:setText('Senha:')
    passwordLabel:setHeight(20)
    
    local passwordField = g_ui.createWidget('PasswordTextEdit', form)
    passwordField:setHeight(30)
    passwordField:setPlaceholder('Digite sua senha')
    passwordField:setMaxLength(20)
    
    -- Campo Confirmar Senha
    local confirmLabel = g_ui.createWidget('UILabel', form)
    confirmLabel:setText('Confirmar Senha:')
    confirmLabel:setHeight(20)
    
    local confirmField = g_ui.createWidget('PasswordTextEdit', form)
    confirmField:setHeight(30)
    confirmField:setPlaceholder('Confirme sua senha')
    confirmField:setMaxLength(20)
    
    -- Campo Idade
    local ageLabel = g_ui.createWidget('UILabel', form)
    ageLabel:setText('Idade:')
    ageLabel:setHeight(20)
    
    local ageField = g_ui.createWidget('UISpinBox', form)
    ageField:setHeight(30)
    ageField:setMinimum(13)
    ageField:setMaximum(120)
    ageField:setValue(18)
    
    -- Termos de Uso
    local termsCheckBox = g_ui.createWidget('UICheckBox', form)
    termsCheckBox:setText('Aceito os termos de uso')
    termsCheckBox:setHeight(25)
    
    -- Botões
    local buttonPanel = g_ui.createWidget('Panel', form)
    buttonPanel:setLayout('horizontalBox')
    buttonPanel:setHeight(40)
    
    local registerButton = g_ui.createWidget('UIButton', buttonPanel)
    registerButton:setText('Registrar')
    registerButton:setWidth(100)
    
    local cancelButton = g_ui.createWidget('UIButton', buttonPanel)
    cancelButton:setText('Cancelar')
    cancelButton:setWidth(100)
    
    -- Eventos
    registerButton.onClick = function()
        RegistrationForm.validateAndSubmit(form, {
            name = nameField,
            email = emailField,
            password = passwordField,
            confirm = confirmField,
            age = ageField,
            terms = termsCheckBox
        })
```

#### Funcionalidade 1
```lua
    end
    
    cancelButton.onClick = function()
        form:destroy()
    end
    
    return form
end

function RegistrationForm.validateAndSubmit(form, fields)
    local errors = {}
    
    -- Validação do nome
    if string.len(fields.name:getText()) < 3 then
        table.insert(errors, 'Nome deve ter pelo menos 3 caracteres')
    end
    
    -- Validação do email
    if not string.match(fields.email:getText(), '^[%w.]+@[%w]+%.[%w]+$') then
        table.insert(errors, 'Email inválido')
    end
```

#### Funcionalidade 2
```lua
    
    -- Validação da senha
    if string.len(fields.password:getText()) < 6 then
        table.insert(errors, 'Senha deve ter pelo menos 6 caracteres')
    end
    
    -- Validação da confirmação
    if fields.password:getText() ~= fields.confirm:getText() then
        table.insert(errors, 'Senhas não coincidem')
    end
    
    -- Validação dos termos
    if not fields.terms:isChecked() then
        table.insert(errors, 'Você deve aceitar os termos de uso')
    end
    
    -- Exibir erros ou submeter
    if #errors > 0 then
        print('Erros de validação:')
        for _, error in ipairs(errors) do
            print('- ' .. error)
        end
```

#### Finalização
```lua
    else
        print('Formulário válido! Enviando dados...')
        -- Aqui você enviaria os dados para o servidor
        form:destroy()
    end
end
```

### 🎨 **Exemplo 2: Formulário de Configurações**

#### Inicialização e Configuração
```lua
local SettingsForm = {}

function SettingsForm.create(parent)
    local form = g_ui.createWidget('Panel', parent)
    form:setSize({width = 350, height = 400})
    form:setLayout('verticalBox')
    form:setPadding(15)
    
    -- Título
    local title = g_ui.createWidget('UILabel', form)
    title:setText('Configurações do Jogo')
    title:setTextAlign('center')
    title:setHeight(25)
    
    -- Volume de Som
    local soundLabel = g_ui.createWidget('UILabel', form)
    soundLabel:setText('Volume de Som:')
    soundLabel:setHeight(20)
    
    local soundSlider = g_ui.createWidget('UIScrollBar', form)
    soundSlider:setHeight(20)
    soundSlider:setRange(0, 100)
    soundSlider:setValue(50)
    
    -- Qualidade Gráfica
    local qualityLabel = g_ui.createWidget('UILabel', form)
    qualityLabel:setText('Qualidade Gráfica:')
    qualityLabel:setHeight(20)
    
    local qualityCombo = g_ui.createWidget('UIComboBox', form)
    qualityCombo:setHeight(25)
    qualityCombo:addOption('Baixa', 'low')
    qualityCombo:addOption('Média', 'medium')
    qualityCombo:addOption('Alta', 'high')
    qualityCombo:addOption('Máxima', 'ultra')
    qualityCombo:setCurrentOption('medium')
    
    -- Resolução
    local resolutionLabel = g_ui.createWidget('UILabel', form)
    resolutionLabel:setText('Resolução:')
    resolutionLabel:setHeight(20)
    
    local resolutionCombo = g_ui.createWidget('UIComboBox', form)
    resolutionCombo:setHeight(25)
    resolutionCombo:addOption('800x600', '800x600')
    resolutionCombo:addOption('1024x768', '1024x768')
    resolutionCombo:addOption('1280x720', '1280x720')
    resolutionCombo:addOption('1920x1080', '1920x1080')
    resolutionCombo:setCurrentOption('1024x768')
    
    -- Opções Avançadas
    local advancedLabel = g_ui.createWidget('UILabel', form)
    advancedLabel:setText('Opções Avançadas:')
    advancedLabel:setHeight(20)
    
    local vsyncCheckBox = g_ui.createWidget('UICheckBox', form)
    vsyncCheckBox:setText('V-Sync')
    vsyncCheckBox:setHeight(20)
    vsyncCheckBox:setChecked(true)
    
    local fullscreenCheckBox = g_ui.createWidget('UICheckBox', form)
    fullscreenCheckBox:setText('Tela Cheia')
    fullscreenCheckBox:setHeight(20)
    fullscreenCheckBox:setChecked(false)
    
    local shadowsCheckBox = g_ui.createWidget('UICheckBox', form)
    shadowsCheckBox:setText('Sombras')
    shadowsCheckBox:setHeight(20)
    shadowsCheckBox:setChecked(true)
    
    -- Botões
    local buttonPanel = g_ui.createWidget('Panel', form)
    buttonPanel:setLayout('horizontalBox')
    buttonPanel:setHeight(35)
    
    local applyButton = g_ui.createWidget('UIButton', buttonPanel)
    applyButton:setText('Aplicar')
    applyButton:setWidth(80)
    
    local resetButton = g_ui.createWidget('UIButton', buttonPanel)
    resetButton:setText('Resetar')
    resetButton:setWidth(80)
    
    local cancelButton = g_ui.createWidget('UIButton', buttonPanel)
    cancelButton:setText('Cancelar')
    cancelButton:setWidth(80)
    
    -- Eventos
    applyButton.onClick = function()
        SettingsForm.applySettings({
            sound = soundSlider:getValue(),
            quality = qualityCombo:getCurrentOption(),
            resolution = resolutionCombo:getCurrentOption(),
            vsync = vsyncCheckBox:isChecked(),
            fullscreen = fullscreenCheckBox:isChecked(),
            shadows = shadowsCheckBox:isChecked()
        })
```

#### Funcionalidade 1
```lua
        form:destroy()
    end
    
    resetButton.onClick = function()
        SettingsForm.resetToDefaults(form, {
            soundSlider = soundSlider,
            qualityCombo = qualityCombo,
            resolutionCombo = resolutionCombo,
            vsyncCheckBox = vsyncCheckBox,
            fullscreenCheckBox = fullscreenCheckBox,
            shadowsCheckBox = shadowsCheckBox
        })
    end
    
    cancelButton.onClick = function()
        form:destroy()
    end
    
    return form
end

function SettingsForm.applySettings(settings)
```

#### Finalização
```lua
    print('Aplicando configurações:')
    for key, value in pairs(settings) do
        print(key .. ': ' .. tostring(value))
    end
    -- Aqui você aplicaria as configurações no jogo
end

function SettingsForm.resetToDefaults(form, widgets)
    widgets.soundSlider:setValue(50)
    widgets.qualityCombo:setCurrentOption('medium')
    widgets.resolutionCombo:setCurrentOption('1024x768')
    widgets.vsyncCheckBox:setChecked(true)
    widgets.fullscreenCheckBox:setChecked(false)
    widgets.shadowsCheckBox:setChecked(true)
end
```

---

## 🔗 **Links Automáticos**

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

## 🔗 Integração com UIInputBox

O OTClient oferece o sistema **UIInputBox** para criar diálogos de entrada rápidos e padronizados.

### 🎯 **Criação de InputBox**

```lua
-- InputBox básico de texto
function showTextInput(title, label, callback)
    -- Função: showTextInput
    local inputBox = UIInputBox.create(title, callback)
    inputBox:addLineEdit(label)
    inputBox:display()
end

-- InputBox com múltiplos campos
function showRegistrationInput(callback)
    -- Função: showRegistrationInput
    local inputBox = UIInputBox.create('Registro', callback)
    inputBox:addLineEdit('Nome:')
    inputBox:addLineEdit('Email:')
    inputBox:addLineEdit('Senha:', true)  -- true = campo de senha
    inputBox:addCheckBox('Aceito os termos', false)
    inputBox:addComboBox('País:', 'Brasil', 'Estados Unidos', 'Canadá')
    inputBox:addSpinBox('Idade:', 13, 120, 18, 1)
    inputBox:display('Registrar', 'Cancelar')
end

-- Uso
    --  Uso (traduzido)
showTextInput('Login', 'Usuário:', function(inputBox)
    local username = inputBox:getText()
    print('Usuário:', username)
end)

showRegistrationInput(function(inputBox)
    local name = inputBox:getText(1)
    local email = inputBox:getText(2)
    local password = inputBox:getText(3)
    local terms = inputBox:isChecked(1)
    local country = inputBox:getCurrentOption(1)
    local age = inputBox:getValue(1)
    
    print('Dados do registro:', name, email, password, terms, country, age)
end)
```

### 🎨 **InputBox Customizado**

```lua
local CustomInputBox = {}

function CustomInputBox.create(title, callback)
    -- Função: CustomInputBox
    local inputBox = UIInputBox.create(title, callback)
    
    -- Adicionar campos personalizados
    --  Adicionar campos personalizados (traduzido)
    inputBox:addLineEdit('Nome do Personagem:')
    inputBox:addLineEdit('Servidor:')
    inputBox:addComboBox('Vocação:', 'Sorcerer', 'Druid', 'Paladin', 'Knight')
    inputBox:addSpinBox('Nível:', 1, 1000, 1, 1)
    inputBox:addCheckBox('Personagem principal', true)
    
    return inputBox
end

-- Uso
    --  Uso (traduzido)
local inputBox = CustomInputBox.create('Novo Personagem', function(inputBox)
    local name = inputBox:getText(1)
    local server = inputBox:getText(2)
    local vocation = inputBox:getCurrentOption(1)
    local level = inputBox:getValue(1)
    local isMain = inputBox:isChecked(1)
    
    print('Criando personagem:', name, server, vocation, level, isMain)
end)

inputBox:display('Criar', 'Cancelar')
```

---

## ✅ Melhores Práticas

### 🎯 **Organização e Estrutura**

```lua
-- ✅ BOM: Agrupar campos relacionados
    --  ✅ BOM: Agrupar campos relacionados (traduzido)
local personalInfoPanel = g_ui.createWidget('Panel', form)
personalInfoPanel:setLayout('verticalBox')
personalInfoPanel:setPadding(10)

local nameField = g_ui.createWidget('UITextEdit', personalInfoPanel)
local emailField = g_ui.createWidget('UITextEdit', personalInfoPanel)

-- ✅ BOM: Usar labels descritivos
    --  ✅ BOM: Usar labels descritivos (traduzido)
local nameLabel = g_ui.createWidget('UILabel', form)
nameLabel:setText('Nome Completo:')
nameField:setPlaceholder('Digite seu nome completo')

-- ✅ BOM: Implementar validação em tempo real
nameField.onTextChange = function(widget, text)
    if string.len(text) < 3 then
    -- Verificação condicional
        widget:setBorderColor('#FF0000')
    else
        widget:setBorderColor('#00FF00')
    end
end
```

### 🎨 **Feedback Visual**

```lua
-- ✅ BOM: Feedback visual para estados
    --  ✅ BOM: Feedback visual para estados (traduzido)
function updateFieldState(field, isValid, message)
    -- Função: updateFieldState
    if isValid then
    -- Verificação condicional
        field:setBorderColor('#4CAF50')
        field:setTooltip('')
    else
        field:setBorderColor('#F44336')
        field:setTooltip(message or 'Campo inválido')
    end
end

-- ✅ BOM: Indicadores de progresso
    --  ✅ BOM: Indicadores de progresso (traduzido)
local progressBar = g_ui.createWidget('UIProgressBar', form)
progressBar:setValue(0)

local function updateProgress(current, total)
    local percentage = (current / total) * 100
    progressBar:setValue(percentage)
end
```

### 🔧 **Validação Robusta**

#### Nível Basic
```lua
-- ✅ BOM: Validação completa
function validateForm(fields)
    local errors = {}
    -- Validar campos obrigatórios
        if field.required and string.len(field:getText()) == 0 then
        end
    end
    -- Validar formato de email
    if fields.email and not validateEmail(fields.email:getText()) then
    end
    -- Validar confirmação de senha
    if fields.password and fields.confirm then
        if fields.password:getText() ~= fields.confirm:getText() then
        end
    end
end
-- ✅ BOM: Exibir erros de forma clara
function showErrors(errors)
    local errorText = 'Erros encontrados:\n'
    end
    -- Mostrar em um popup ou label
    print(errorText)
end
```

#### Nível Intermediate
```lua
-- ✅ BOM: Validação completa
function validateForm(fields)
    local errors = {}
    
    -- Validar campos obrigatórios
    for name, field in pairs(fields) do
        if field.required and string.len(field:getText()) == 0 then
            table.insert(errors, name .. ' é obrigatório')
        end
    end
    
    -- Validar formato de email
    if fields.email and not validateEmail(fields.email:getText()) then
        table.insert(errors, 'Email inválido')
    end
    
    -- Validar confirmação de senha
    if fields.password and fields.confirm then
        if fields.password:getText() ~= fields.confirm:getText() then
            table.insert(errors, 'Senhas não coincidem')
        end
    end
    
    return errors
end

-- ✅ BOM: Exibir erros de forma clara
function showErrors(errors)
    local errorText = 'Erros encontrados:\n'
    for _, error in ipairs(errors) do
        errorText = errorText .. '• ' .. error .. '\n'
    end
    
    -- Mostrar em um popup ou label
    print(errorText)
end
```

#### Nível Advanced
```lua
-- ✅ BOM: Validação completa
function validateForm(fields)
    local errors = {}
    
    -- Validar campos obrigatórios
    for name, field in pairs(fields) do
        if field.required and string.len(field:getText()) == 0 then
            table.insert(errors, name .. ' é obrigatório')
        end
    end
    
    -- Validar formato de email
    if fields.email and not validateEmail(fields.email:getText()) then
        table.insert(errors, 'Email inválido')
    end
    
    -- Validar confirmação de senha
    if fields.password and fields.confirm then
        if fields.password:getText() ~= fields.confirm:getText() then
            table.insert(errors, 'Senhas não coincidem')
        end
    end
    
    return errors
end

-- ✅ BOM: Exibir erros de forma clara
function showErrors(errors)
    local errorText = 'Erros encontrados:\n'
    for _, error in ipairs(errors) do
        errorText = errorText .. '• ' .. error .. '\n'
    end
    
    -- Mostrar em um popup ou label
    print(errorText)
end
```

---

## 🚀 Performance e Otimização

### 📊 **Métricas de Performance**

1. **Tempo de Criação de Widget**: < 1ms
2. **Tempo de Validação**: < 0.1ms por campo
3. **Uso de Memória por Formulário**: < 5KB
4. **Limite de Campos por Formulário**: 50 campos

### 🎯 **Técnicas de Otimização**

#### Nível Basic
```lua
-- Lazy loading de validação
local validationCache = {}
function validateField(field, rules)
    local fieldId = field:getId()
    local currentValue = field:getText()
    -- Verificar cache
    if validationCache[fieldId] and validationCache[fieldId].value == currentValue then
    end
    -- Executar validação
    local result = performValidation(currentValue, rules)
    -- Armazenar no cache
end
-- Debounce para validação em tempo real
local validationTimers = {}
function debouncedValidation(field, rules, delay)
    local fieldId = field:getId()
    if validationTimers[fieldId] then
    end
    validationTimers[fieldId] = scheduleEvent(function()
    end, delay)
end
```

#### Nível Intermediate
```lua
-- Lazy loading de validação
local validationCache = {}

function validateField(field, rules)
    local fieldId = field:getId()
    local currentValue = field:getText()
    
    -- Verificar cache
    if validationCache[fieldId] and validationCache[fieldId].value == currentValue then
        return validationCache[fieldId].result
    end
    
    -- Executar validação
    local result = performValidation(currentValue, rules)
    
    -- Armazenar no cache
    validationCache[fieldId] = {
        value = currentValue,
        result = result
    }
    
    return result
end

-- Debounce para validação em tempo real
local validationTimers = {}

function debouncedValidation(field, rules, delay)
    delay = delay or 300
    
    local fieldId = field:getId()
    
    if validationTimers[fieldId] then
        removeEvent(validationTimers[fieldId])
    end
    
    validationTimers[fieldId] = scheduleEvent(function()
        validateField(field, rules)
        validationTimers[fieldId] = nil
    end, delay)
end
```

#### Nível Advanced
```lua
-- Lazy loading de validação
local validationCache = {}

function validateField(field, rules)
    local fieldId = field:getId()
    local currentValue = field:getText()
    
    -- Verificar cache
    if validationCache[fieldId] and validationCache[fieldId].value == currentValue then
        return validationCache[fieldId].result
    end
    
    -- Executar validação
    local result = performValidation(currentValue, rules)
    
    -- Armazenar no cache
    validationCache[fieldId] = {
        value = currentValue,
        result = result
    }
    
    return result
end

-- Debounce para validação em tempo real
local validationTimers = {}

function debouncedValidation(field, rules, delay)
    delay = delay or 300
    
    local fieldId = field:getId()
    
    if validationTimers[fieldId] then
        removeEvent(validationTimers[fieldId])
    end
    
    validationTimers[fieldId] = scheduleEvent(function()
        validateField(field, rules)
        validationTimers[fieldId] = nil
    end, delay)
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

### 🔧 **Monitoramento de Performance**

```lua
-- Função para medir performance de formulários
local function measureFormPerformance(fieldCount)
    local startTime = g_clock.millis()
    
    local form = g_ui.createWidget('Panel')
    local fields = {}
    
    for i = 1, fieldCount do
    -- Loop de repetição
        fields[i] = g_ui.createWidget('UITextEdit', form)
        fields[i]:setText('Teste ' .. i)
    end
    
    local creationTime = g_clock.millis() - startTime
    
    -- Medir tempo de validação
    startTime = g_clock.millis()
    for _, field in ipairs(fields) do
    -- Loop de repetição
        validateField(field, {required = {}, minLength = {3}})
    end
    local validationTime = g_clock.millis() - startTime
    
    -- Limpeza
    --  Limpeza (traduzido)
    form:destroy()
    
    print(string.format('Criação: %dms, Validação: %dms', creationTime, validationTime))
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
- [[UI_System_Guide]] - Guia do sistema de UI
- [[ConfigurationAdvanced]] - Sistema de configuração avançado

### 📖 Documentação Técnica
- **UIInputBox**: Sistema de diálogos de entrada
- **Estilos OTUI**: Arquivos de estilo para widgets
- **Validação**: Sistema de validação de formulários

---

**Última Atualização**: 2025-01-27  
**Versão**: 1.0  
**Status**: ✅ **Completo**  
**Prioridade**: 🔥 **MÁXIMA**
