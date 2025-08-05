
# Cheat Sheet de Desenvolvimento - OTClient Redemption

Referência rápida para desenvolvimento no OTClient com códigos essenciais, padrões comuns e comandos úteis.


---

## 📋 Índice 📋

1. [Configuração Rápida](#-configuração-rápida)
2. [Estrutura de Módulo](#-estrutura-de-módulo)
3. [Interface Básica](#-interface-básica)
4. [Eventos Comuns](#-eventos-comuns)
5. [APIs Essenciais](#-apis-essenciais)
6. [Comandos de Debug](#-comandos-de-debug)
7. [Patterns e Snippets](#-patterns-e-snippets)
8. [Cores e Constantes](#-cores-e-constantes)
9. [Troubleshooting](#-troubleshooting)


---

## 🚀 Configuração Rápida 🔧

### Criar Novo Módulo 📝

```bash
# Estrutura mínima
modules/
└── meu_modulo/
    ├── init.lua
    ├── meu_modulo.lua
    ├── meu_modulo.otmod
    └── meu_modulo.otui
```

### .otmod Template 📝

#### Nível Basic
```lua
Module
  name: meu_modulo
  description: Descrição do módulo
  author: Seu Nome
  website: https://exemplo.com
  version: 1.0.0
  
  dependencies:
    - game_interface
    - client_topmenu
  
  load-priority: 1000
  
  @onLoad: init.lua
  @onUnload: |
    return terminate()
```

#### Nível Intermediate
```lua
Module
  name: meu_modulo
  description: Descrição do módulo
  author: Seu Nome
  website: https://exemplo.com
  version: 1.0.0
  
  dependencies:
    - game_interface
    - client_topmenu
  
  load-priority: 1000
  
  @onLoad: init.lua
  @onUnload: |
    return terminate()
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
Module
  name: meu_modulo
  description: Descrição do módulo
  author: Seu Nome
  website: https://exemplo.com
  version: 1.0.0
  
  dependencies:
    - game_interface
    - client_topmenu
  
  load-priority: 1000
  
  @onLoad: init.lua
  @onUnload: |
    return terminate()
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

### init.lua Template 📝

```lua
-- init.lua
    --  init.lua (traduzido)
meuModulo = {}

-- Importa as dependências
dofiles {
    'meu_modulo'
}

function init()
    -- Função: init
    meuModulo.init()
end

function terminate()
    -- Função: terminate
    meuModulo.terminate()
end
```


---

## 🏗️ Estrutura de Módulo 📋

### Template Básico do Módulo Principal 📝

#### Inicialização e Configuração
```lua
-- meu_modulo.lua
meuModulo = {}

-- Variáveis locais
local window = nil
local button = nil
local config = {}

function meuModulo.init()
    -- Carrega configurações
    meuModulo.loadConfig()
    
    -- Cria interface
    meuModulo.createInterface()
    
    -- Registra eventos
    meuModulo.connectEvents()
    
    -- Adiciona botão no menu
    button = modules.client_topmenu.addRightGameToggleButton(
        'meuModuloButton',
        'Meu Módulo',
        '/images/icons/meu_icone',
        meuModulo.toggle
    )
end
```

#### Funcionalidade 1
```lua

function meuModulo.terminate()
    -- Desconecta eventos
    meuModulo.disconnectEvents()
    
    -- Salva configurações
    meuModulo.saveConfig()
    
    -- Destroi interface
    if window then
        window:destroy()
        window = nil
    end
    
    -- Remove botão
    if button then
        button:destroy()
        button = nil
    end
end

function meuModulo.createInterface()
```

#### Funcionalidade 2
```lua
    window = g_ui.displayUI('meu_modulo')
    window:hide()
end

function meuModulo.toggle()
    if window:isVisible() then
        window:hide()
    else
        window:show()
        window:raise()
        window:focus()
    end
end

function meuModulo.connectEvents()
    connect(g_game, {
        onGameStart = meuModulo.onGameStart,
        onGameEnd = meuModulo.onGameEnd
    })
end

function meuModulo.disconnectEvents()
```

#### Finalização
```lua
    disconnect(g_game, {
        onGameStart = meuModulo.onGameStart,
        onGameEnd = meuModulo.onGameEnd
    })
end

function meuModulo.onGameStart()
    -- Lógica quando conecta
end

function meuModulo.onGameEnd()
    -- Lógica quando desconecta
    window:hide()
end

function meuModulo.loadConfig()
    config = g_settings.getNode('meuModulo') or {}
end

function meuModulo.saveConfig()
    g_settings.setNode('meuModulo', config)
    g_settings.save()
end
```


---

## 🎨 Interface Básica 📋

### Template .otui 📝

#### Nível Basic
```lua
MeuModuloWindow < MainWindow
  id: meuModuloWindow
  !text: tr('Meu Módulo')
  size: 400 300
  @onEscape: self:hide()

  UIWidget
    id: content
    anchors.fill: parent
    margin: 10
    layout:
      type: verticalBox
      spacing: 5

    UILabel
      id: titleLabel
      !text: tr('Configurações')
      text-align: center
      height: 20

    UITextEdit
      id: textEdit
      placeholder: Digite algo...
      height: 25

    UICheckBox
      id: enabledBox
      !text: tr('Habilitado')
      height: 20

    UIComboBox
      id: optionsCombo
      height: 25

    UIHorizontalSeparator
      margin-top: 10
      margin-bottom: 10

    UIWidget
      id: buttonsPanel
      height: 30
      layout:
        type: horizontalBox
        spacing: 10

      UIButton
        id: saveButton
        !text: tr('Salvar')
        width: 80

      UIButton
        id: cancelButton
        !text: tr('Cancelar')
        width: 80

      UIWidget
        id: spacer
        layout: { type: horizontalBox }
```

#### Nível Intermediate
```lua
MeuModuloWindow < MainWindow
  id: meuModuloWindow
  !text: tr('Meu Módulo')
  size: 400 300
  @onEscape: self:hide()

  UIWidget
    id: content
    anchors.fill: parent
    margin: 10
    layout:
      type: verticalBox
      spacing: 5

    UILabel
      id: titleLabel
      !text: tr('Configurações')
      text-align: center
      height: 20

    UITextEdit
      id: textEdit
      placeholder: Digite algo...
      height: 25

    UICheckBox
      id: enabledBox
      !text: tr('Habilitado')
      height: 20

    UIComboBox
      id: optionsCombo
      height: 25

    UIHorizontalSeparator
      margin-top: 10
      margin-bottom: 10

    UIWidget
      id: buttonsPanel
      height: 30
      layout:
        type: horizontalBox
        spacing: 10

      UIButton
        id: saveButton
        !text: tr('Salvar')
        width: 80

      UIButton
        id: cancelButton
        !text: tr('Cancelar')
        width: 80

      UIWidget
        id: spacer
        layout: { type: horizontalBox }
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
MeuModuloWindow < MainWindow
  id: meuModuloWindow
  !text: tr('Meu Módulo')
  size: 400 300
  @onEscape: self:hide()

  UIWidget
    id: content
    anchors.fill: parent
    margin: 10
    layout:
      type: verticalBox
      spacing: 5

    UILabel
      id: titleLabel
      !text: tr('Configurações')
      text-align: center
      height: 20

    UITextEdit
      id: textEdit
      placeholder: Digite algo...
      height: 25

    UICheckBox
      id: enabledBox
      !text: tr('Habilitado')
      height: 20

    UIComboBox
      id: optionsCombo
      height: 25

    UIHorizontalSeparator
      margin-top: 10
      margin-bottom: 10

    UIWidget
      id: buttonsPanel
      height: 30
      layout:
        type: horizontalBox
        spacing: 10

      UIButton
        id: saveButton
        !text: tr('Salvar')
        width: 80

      UIButton
        id: cancelButton
        !text: tr('Cancelar')
        width: 80

      UIWidget
        id: spacer
        layout: { type: horizontalBox }
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

### Criação de Interface Programática 📝

```lua
-- Janela principal
    --  Janela principal (traduzido)
local window = g_ui.createWidget('UIWindow', rootWidget)
window:setTitle('Minha Janela')
window:setSize({width = 300, height = 200})
window:centerIn('parent')

-- Layout vertical
    --  Layout vertical (traduzido)
local layout = g_ui.createWidget('UIVerticalLayout', window)
layout:setSpacing(5)
layout:setPadding(10)

-- Botão
local button = g_ui.createWidget('UIButton', layout)
button:setText('Clique Aqui')
button:setHeight(25)
button.onClick = function()
    print('Botão clicado!')
end

-- Input de texto
    --  Input de texto (traduzido)
local textEdit = g_ui.createWidget('UITextEdit', layout)
textEdit:setPlaceholder('Digite algo...')
textEdit:setHeight(25)
textEdit.onTextChange = function(widget, text)
    print('Texto alterado: ' .. text)
end

-- Label
    --  Label (traduzido)
local label = g_ui.createWidget('UILabel', layout)
label:setText('Status: Aguardando...')
label:setHeight(20)
```


---

## 📡 Eventos Comuns 📋

### Eventos do Jogo 📝

```lua
connect(g_game, {
    -- Conexão
    onGameStart = function()
        print('Conectado ao jogo')
    end,
    
    onGameEnd = function()
        print('Desconectado do jogo')
    end,
    
    onLoginError = function(message)
        print('Erro de login: ' .. message)
    end,
    
    -- Chat
    --  Chat (traduzido)
    onTalk = function(name, level, mode, message, channelId, pos)
        if mode == TalkType.Say then
    -- Verificação condicional
            print(name .. ' disse: ' .. message)
        end
    end,
    
    -- Criaturas
    --  Criaturas (traduzido)
    onCreatureAppear = function(creature)
        if creature:isPlayer() then
    -- Verificação condicional
            print('Jogador apareceu: ' .. creature:getName())
        end
    end,
    
    -- Stats do jogador
    --  Stats do jogador (traduzido)
    onLocalPlayerStatsChange = function(localPlayer)
        local hp = localPlayer:getHealth()
        local maxHp = localPlayer:getMaxHealth()
        print('HP: ' .. hp .. '/' .. maxHp)
    end
})
```

### Eventos de Interface 📝

```lua
-- Eventos de widget
    --  Eventos de widget (traduzido)
widget.onClick = function(widget)
    print('Clicado!')
end

widget.onDoubleClick = function(widget)
    print('Duplo clique!')
end

widget.onHoverChange = function(widget, hovered)
    if hovered then
    -- Verificação condicional
        widget:setBackgroundColor('#FFFF00')
    else
        widget:setBackgroundColor('#FFFFFF')
    end
end

-- Eventos de texto
    --  Eventos de texto (traduzido)
textEdit.onTextChange = function(textEdit, text, oldText)
    print('Texto mudou de "' .. oldText .. '" para "' .. text .. '"')
end

textEdit.onEnterPressed = function(textEdit)
    local text = textEdit:getText()
    print('Enter pressionado com: ' .. text)
    textEdit:clearText()
end

-- Eventos de combo
    --  Eventos de combo (traduzido)
comboBox.onOptionChange = function(comboBox, optionText, optionData)
    print('Selecionado: ' .. optionText .. ' (data: ' .. optionData .. ')')
end
```


---

## 🔧 APIs Essenciais 📚

### Configurações 📝

```lua
-- Salvar/Carregar configurações
g_settings.set('modulo.config', valor)
local valor = g_settings.getBoolean('modulo.enabled', true)
local numero = g_settings.getNumber('modulo.count', 0)
local texto = g_settings.getString('modulo.name', 'default')
local lista = g_settings.getList('modulo.items')
local node = g_settings.getNode('modulo.data')

-- Salvar
    --  Salvar (traduzido)
g_settings.save()
```

### Jogo 📝

```lua
-- Informações básicas
local online = g_game.isOnline()
local player = g_game.getLocalPlayer()
local name = g_game.getCharacterName()

-- Movimento
    --  Movimento (traduzido)
g_game.walk(North)
g_game.stop()

-- Chat
    --  Chat (traduzido)
g_game.talk('Olá!')
g_game.talkChannel(TalkType.Say, 0, 'Mensagem')

-- Itens
    --  Itens (traduzido)
g_game.use(item)
g_game.useWith(item, target)
g_game.useInventoryItem(2160) -- gold coin

-- Combate
    --  Combate (traduzido)
g_game.attack(creature)
g_game.follow(creature)
g_game.setChaseMode(ChaseOpponent)
```

### Interface 📝

```lua
-- Mensagens
    --  Mensagens (traduzido)
modules.game_textmessage.displayGameMessage('Mensagem')
modules.game_textmessage.displayStatusMessage('Status')

-- Console
    --  Console (traduzido)
modules.game_console.addMessage('Texto', MessageModeStatus)
modules.game_console.sendMessage('comando')

-- Notificações (se módulo personalizado existir)
notify.info('Título', 'Mensagem')
notify.success('Sucesso', 'Operação concluída')
notify.error('Erro', 'Algo deu errado')
```

### Keyboard/Mouse 📝

```lua
-- Bind de teclas
    --  Bind de teclas (traduzido)
g_keyboard.bindKeyPress('F1', function()
    print('F1 pressionado')
end)

g_keyboard.bindKeyDown('Ctrl+S', function()
    print('Ctrl+S')
end)

-- Posição do mouse
local pos = g_mouse.getPosition()
g_mouse.setPosition(100, 200)
```


---

## 🐛 Comandos de Debug 🐛

### Console do Jogo 📝

```lua
-- Adicionar comando personalizado
    --  Adicionar comando personalizado (traduzido)
modules.game_console.addCommand('meucomando', function(args)
    print('Comando executado com args:', table.concat(args, ', '))
end, 'Descrição do comando')

-- Log de debug
    --  Log de debug (traduzido)
print('Debug: valor =', valor)
g_logger.info('Informação importante')
g_logger.warning('Aviso')
g_logger.error('Erro!')

-- Dump de tabela
    --  Dump de tabela (traduzido)
function dump(t)
    -- Função: dump
    for k, v in pairs(t) do
    -- Loop de repetição
        print(k, '=', v)
    end
end
```

### Informações do Sistema 📝

```lua
-- Performance
    --  Performance (traduzido)
local fps = g_graphics.getAverageFPS()
local ping = g_game.getPing()

-- Memória (se disponível)
local mem = collectgarbage('count')

-- Posição do jogador
local player = g_game.getLocalPlayer()
if player then
    -- Verificação condicional
    local pos = player:getPosition()
    print('Posição:', pos.x, pos.y, pos.z)
end
```


---

## 🎭 Patterns e Snippets 📋

### Singleton Pattern 📝

```lua
local MySingleton = {}
local instance = nil

function MySingleton.getInstance()
    -- Função: MySingleton
    if not instance then
    -- Verificação condicional
        instance = {}
        -- Inicialização
        instance.data = {}
        instance.init = function(self)
            -- Lógica de inicialização
        end
    end
    return instance
end
```

### Observer Pattern 📝

```lua
local EventManager = {}

function EventManager.create()
    -- Função: EventManager
    local self = {}
    local listeners = {}
    
    function self:on(event, callback)
    -- Função: self
        if not listeners[event] then
    -- Verificação condicional
            listeners[event] = {}
        end
        table.insert(listeners[event], callback)
    end
    
    function self:emit(event, ...)
    -- Função: self
        if listeners[event] then
    -- Verificação condicional
            for _, callback in ipairs(listeners[event]) do
    -- Loop de repetição
                callback(...)
            end
        end
    end
    
    return self
end

-- Uso
    --  Uso (traduzido)
local events = EventManager.create()
events:on('playerMove', function(pos)
    print('Player moveu para:', pos.x, pos.y)
end)
events:emit('playerMove', {x = 100, y = 100, z = 7})
```

### State Machine 📝

```lua
local StateMachine = {}

function StateMachine.create(initialState)
    -- Função: StateMachine
    local self = {}
    local state = initialState
    local states = {}
    
    function self:addState(name, onEnter, onExit, onUpdate)
    -- Função: self
        states[name] = {
            onEnter = onEnter or function() end,
            onExit = onExit or function() end,
            onUpdate = onUpdate or function() end
        }
    end
    
    function self:setState(newState)
    -- Função: self
        if states[state] then
    -- Verificação condicional
            states[state].onExit()
        end
        state = newState
        if states[state] then
    -- Verificação condicional
            states[state].onEnter()
        end
    end
    
    function self:update()
    -- Função: self
        if states[state] then
    -- Verificação condicional
            states[state].onUpdate()
        end
    end
    
    function self:getState()
    -- Função: self
        return state
    end
    
    return self
end
```

### Timer Utilities 📝

```lua
-- Timer simples
    --  Timer simples (traduzido)
function createTimer(interval, callback, repeat_count)
    -- Função: createTimer
    local count = 0
    local function timerCallback()
        callback()
        count = count + 1
        if not repeat_count or count < repeat_count then
    -- Verificação condicional
            scheduleEvent(timerCallback, interval)
        end
    end
    scheduleEvent(timerCallback, interval)
end

-- Uso
    --  Uso (traduzido)
createTimer(1000, function()
    print('Executado a cada segundo')
end, 5) -- Executa 5 vezes

-- Throttle (limita execução)
function throttle(func, delay)
    -- Função: throttle
    local lastTime = 0
    return function(...)
        local now = g_clock.millis()
        if now - lastTime >= delay then
    -- Verificação condicional
            lastTime = now
            return func(...)
        end
    end
end

-- Debounce (atrasa execução)
function debounce(func, delay)
    -- Função: debounce
    local timer = nil
    return function(...)
        if timer then
    -- Verificação condicional
            removeEvent(timer)
        end
        local args = {...}
        timer = scheduleEvent(function()
            func(unpack(args))
        end, delay)
    end
end
```

### Formatação de Dados 📝

#### Inicialização e Configuração
```lua
-- Formatar números
function formatNumber(num)
    if num >= 1000000 then
        return string.format("%.1fM", num / 1000000)
    elseif num >= 1000 then
        return string.format("%.1fK", num / 1000)
    else
        return tostring(num)
    end
end

-- Formatar tempo
function formatTime(seconds)
    local hours = math.floor(seconds / 3600)
    local minutes = math.floor((seconds % 3600) / 60)
    local secs = seconds % 60
    
    if hours > 0 then
        return string.format("%02d:%02d:%02d", hours, minutes, secs)
    else
        return string.format("%02d:%02d", minutes, secs)
    end
```

#### Funcionalidade 1
```lua
end

-- Capitalizar texto
function capitalize(str)
    return str:sub(1, 1):upper() .. str:sub(2):lower()
end

-- Quebrar texto em linhas
function wrapText(text, maxLength)
    local lines = {}
    local currentLine = ""
    
    for word in text:gmatch("%S+") do
        if #currentLine + #word + 1 <= maxLength then
            if #currentLine > 0 then
                currentLine = currentLine .. " " .. word
            else
                currentLine = word
            end
        else
            if #currentLine > 0 then
                table.insert(lines, currentLine)
            end
```

#### Finalização
```lua
            currentLine = word
        end
    end
    
    if #currentLine > 0 then
        table.insert(lines, currentLine)
    end
    
    return lines
end
```


---

## 🎨 Cores e Constantes 📋

### Cores Comuns 📝

```lua
-- Cores básicas
local Colors = {
    WHITE = '#FFFFFF',
    BLACK = '#000000',
    RED = '#FF0000',
    GREEN = '#00FF00',
    BLUE = '#0000FF',
    YELLOW = '#FFFF00',
    CYAN = '#00FFFF',
    MAGENTA = '#FF00FF',
    
    -- Tons de cinza
    --  Tons de cinza (traduzido)
    GRAY_LIGHT = '#CCCCCC',
    GRAY = '#808080',
    GRAY_DARK = '#404040',
    
    -- Cores da interface
    --  Cores da interface (traduzido)
    UI_BACKGROUND = '#2B2B2B',
    UI_BORDER = '#404040',
    UI_HIGHLIGHT = '#0078D4',
    UI_TEXT = '#FFFFFF',
    UI_TEXT_DISABLED = '#808080',
    
    -- Cores de estado
    --  Cores de estado (traduzido)
    SUCCESS = '#00AA00',
    WARNING = '#FFAA00',
    ERROR = '#AA0000',
    INFO = '#0088FF'
}
```

### Direções 📝

#### Nível Basic
```lua
local Directions = {
    North, South, East, West,
    Northeast, Northwest, Southeast, Southwest
}

-- Conversão texto para direção
local directionMap = {
    n = North, north = North,
    s = South, south = South,
    e = East, east = East,
    w = West, west = West,
    ne = Northeast, northeast = Northeast,
    nw = Northwest, northwest = Northwest,
    se = Southeast, southeast = Southeast,
    sw = Southwest, southwest = Southwest
}
```

#### Nível Intermediate
```lua
local Directions = {
    North, South, East, West,
    Northeast, Northwest, Southeast, Southwest
}

-- Conversão texto para direção
local directionMap = {
    n = North, north = North,
    s = South, south = South,
    e = East, east = East,
    w = West, west = West,
    ne = Northeast, northeast = Northeast,
    nw = Northwest, northwest = Northwest,
    se = Southeast, southeast = Southeast,
    sw = Southwest, southwest = Southwest
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
local Directions = {
    North, South, East, West,
    Northeast, Northwest, Southeast, Southwest
}

-- Conversão texto para direção
local directionMap = {
    n = North, north = North,
    s = South, south = South,
    e = East, east = East,
    w = West, west = West,
    ne = Northeast, northeast = Northeast,
    nw = Northwest, northwest = Northwest,
    se = Southeast, southeast = Southeast,
    sw = Southwest, southwest = Southwest
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

### Teclas Comuns 📝

```lua
local Keys = {
    -- Função
    F1 = 'F1', F2 = 'F2', F3 = 'F3', F4 = 'F4',
    F5 = 'F5', F6 = 'F6', F7 = 'F7', F8 = 'F8',
    F9 = 'F9', F10 = 'F10', F11 = 'F11', F12 = 'F12',
    
    -- Modificadores
    --  Modificadores (traduzido)
    CTRL_S = 'Ctrl+S',
    CTRL_C = 'Ctrl+C',
    CTRL_V = 'Ctrl+V',
    SHIFT_F1 = 'Shift+F1',
    ALT_F4 = 'Alt+F4',
    
    -- Navegação
    ENTER = 'Return',
    ESCAPE = 'Escape',
    TAB = 'Tab',
    SPACE = 'Space',
    UP = 'Up',
    DOWN = 'Down',
    LEFT = 'Left',
    RIGHT = 'Right'
}
```

### IDs de Itens Comuns 📝

```lua
local Items = {
    -- Moedas
    --  Moedas (traduzido)
    GOLD_COIN = 2160,
    PLATINUM_COIN = 2157,
    CRYSTAL_COIN = 2159,
    
    -- Runas básicas
    UH_RUNE = 2273,
    IH_RUNE = 2265,
    SD_RUNE = 2268,
    
    -- Potions
    --  Potions (traduzido)
    HEALTH_POTION = 7618,
    MANA_POTION = 7620,
    STRONG_HEALTH = 7588,
    STRONG_MANA = 7589,
    GREAT_HEALTH = 7591,
    GREAT_MANA = 7590,
    ULTIMATE_HEALTH = 8473,
    GREAT_SPIRIT = 8472,
    
    -- Containers
    --  Containers (traduzido)
    BACKPACK = 1988,
    BAG = 1987,
    GOLDEN_BACKPACK = 5949
}
```


---

## 🔍 Troubleshooting 🔍

### Problemas Comuns 📝

#### Nível Basic
```lua
-- Verificar se módulo está carregado
if not g_modules.isModuleLoaded('meu_modulo') then
    print('Módulo não carregado!')
end
-- Verificar se online
if not g_game.isOnline() then
    print('Não está conectado ao jogo!')
end
-- Verificar se widget existe
if not widget or widget:isDestroyed() then
    print('Widget não existe ou foi destruído!')
end
-- Safe call para funções que podem falhar
local success, result = pcall(function()
    -- Código que pode gerar erro
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Intermediate
```lua
-- Verificar se módulo está carregado
if not g_modules.isModuleLoaded('meu_modulo') then
    print('Módulo não carregado!')
    return
end

-- Verificar se online
if not g_game.isOnline() then
    print('Não está conectado ao jogo!')
    return
end

-- Verificar se widget existe
if not widget or widget:isDestroyed() then
    print('Widget não existe ou foi destruído!')
    return
end

-- Safe call para funções que podem falhar
    -- Código que pode gerar erro
    return minhaFuncaoPerigosa()
end)

if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```lua
-- Verificar se módulo está carregado
if not g_modules.isModuleLoaded('meu_modulo') then
    print('Módulo não carregado!')
    return
end

-- Verificar se online
if not g_game.isOnline() then
    print('Não está conectado ao jogo!')
    return
end

-- Verificar se widget existe
if not widget or widget:isDestroyed() then
    print('Widget não existe ou foi destruído!')
    return
end

-- Safe call para funções que podem falhar
local success, result = pcall(function()
    -- Código que pode gerar erro
    return minhaFuncaoPerigosa()
end)

if not success then
    print('Erro:', result)
end
```

### Debug de Performance 📝

#### Nível Basic
```lua
-- Medir tempo de execução
local startTime = g_clock.millis()
-- ... código a ser medido ...
local endTime = g_clock.millis()
print('Tempo de execução:', (endTime - startTime) .. 'ms')

-- Contadores
local counter = 0
function incrementCounter()
    counter = counter + 1
    if counter % 100 == 0 then
        print('Contador:', counter)
    end
end

-- Profiling simples
local Profile = {}
function Profile.start(name)
    Profile[name] = g_clock.millis()
end

function Profile.stop(name)
    if Profile[name] then
        local elapsed = g_clock.millis() - Profile[name]
        print('Profile [' .. name .. ']:', elapsed .. 'ms')
        Profile[name] = nil
    end
end

-- Uso
Profile.start('operacao')
-- ... código ...
Profile.stop('operacao')
```

#### Nível Intermediate
```lua
-- Medir tempo de execução
local startTime = g_clock.millis()
-- ... código a ser medido ...
local endTime = g_clock.millis()
print('Tempo de execução:', (endTime - startTime) .. 'ms')

-- Contadores
local counter = 0
function incrementCounter()
    counter = counter + 1
    if counter % 100 == 0 then
        print('Contador:', counter)
    end
end

-- Profiling simples
local Profile = {}
function Profile.start(name)
    Profile[name] = g_clock.millis()
end

function Profile.stop(name)
    if Profile[name] then
        local elapsed = g_clock.millis() - Profile[name]
        print('Profile [' .. name .. ']:', elapsed .. 'ms')
        Profile[name] = nil
    end
end

-- Uso
Profile.start('operacao')
-- ... código ...
Profile.stop('operacao')
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
-- Medir tempo de execução
local startTime = g_clock.millis()
-- ... código a ser medido ...
local endTime = g_clock.millis()
print('Tempo de execução:', (endTime - startTime) .. 'ms')

-- Contadores
local counter = 0
function incrementCounter()
    counter = counter + 1
    if counter % 100 == 0 then
        print('Contador:', counter)
    end
end

-- Profiling simples
local Profile = {}
function Profile.start(name)
    Profile[name] = g_clock.millis()
end

function Profile.stop(name)
    if Profile[name] then
        local elapsed = g_clock.millis() - Profile[name]
        print('Profile [' .. name .. ']:', elapsed .. 'ms')
        Profile[name] = nil
    end
end

-- Uso
Profile.start('operacao')
-- ... código ...
Profile.stop('operacao')
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

### Validação de Dados 📝

```lua
-- Validar tipos
    --  Validar tipos (traduzido)
function validateString(value, name)
    -- Função: validateString
    if type(value) ~= 'string' then
    -- Verificação condicional
        error(name .. ' deve ser uma string, recebido: ' .. type(value))
    end
end

function validateNumber(value, name, min, max)
    -- Função: validateNumber
    if type(value) ~= 'number' then
    -- Verificação condicional
        error(name .. ' deve ser um número, recebido: ' .. type(value))
    end
    if min and value < min then
    -- Verificação condicional
        error(name .. ' deve ser >= ' .. min)
    end
    if max and value > max then
    -- Verificação condicional
        error(name .. ' deve ser <= ' .. max)
    end
end

function validateTable(value, name)
    -- Função: validateTable
    if type(value) ~= 'table' then
    -- Verificação condicional
        error(name .. ' deve ser uma tabela, recebido: ' .. type(value))
    end
end

-- Validar posição
function validatePosition(pos)
    -- Função: validatePosition
    if not pos or type(pos) ~= 'table' then
    -- Verificação condicional
        return false
    end
    return pos.x and pos.y and pos.z and
           type(pos.x) == 'number' and
           type(pos.y) == 'number' and
           type(pos.z) == 'number'
end
```

### Comandos de Console Úteis 📝

#### Nível Basic
```lua
-- Listar módulos carregados
/lua for _, module in pairs(g_modules.getModules()) do print(module:getName(), module:isLoaded()) end
-- Verificar FPS
/lua print('FPS:', g_graphics.getAverageFPS())
-- Verificar ping
/lua print('Ping:', g_game.getPing())
-- Posição do jogador
/lua local p = g_game.getLocalPlayer(); if p then print('Pos:', p:getPosition().x, p:getPosition().y, p:getPosition().z) end
-- Recarregar módulo
-- Dump de configurações
/lua for k,v in pairs(g_settings.getNode('modulo') or {}) do print(k,v) end
-- Limpar configurações
```

#### Nível Intermediate
```lua
-- Listar módulos carregados
/lua for _, module in pairs(g_modules.getModules()) do print(module:getName(), module:isLoaded()) end

-- Verificar FPS
/lua print('FPS:', g_graphics.getAverageFPS())

-- Verificar ping
/lua print('Ping:', g_game.getPing())

-- Posição do jogador
/lua local p = g_game.getLocalPlayer(); if p then print('Pos:', p:getPosition().x, p:getPosition().y, p:getPosition().z) end

-- Recarregar módulo
/lua g_modules.reloadModule('nome_do_modulo')

-- Dump de configurações
/lua for k,v in pairs(g_settings.getNode('modulo') or {}) do print(k,v) end

-- Limpar configurações
/lua g_settings.clear(); g_settings.save()
```

#### Nível Advanced
```lua
-- Listar módulos carregados
/lua for _, module in pairs(g_modules.getModules()) do print(module:getName(), module:isLoaded()) end

-- Verificar FPS
/lua print('FPS:', g_graphics.getAverageFPS())

-- Verificar ping
/lua print('Ping:', g_game.getPing())

-- Posição do jogador
/lua local p = g_game.getLocalPlayer(); if p then print('Pos:', p:getPosition().x, p:getPosition().y, p:getPosition().z) end

-- Recarregar módulo
/lua g_modules.reloadModule('nome_do_modulo')

-- Dump de configurações
/lua for k,v in pairs(g_settings.getNode('modulo') or {}) do print(k,v) end

-- Limpar configurações
/lua g_settings.clear(); g_settings.save()
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


---

## 📚 Referências Rápidas 📚

- **Documentação Completa**: `Docs/LuaAPI.md`
- **Guia de Início**: `Docs/GettingStarted.md`
- **Primeiro Módulo**: `Docs/FirstModule.md`
- **Boas Práticas**: `Docs/BestPractices.md`
- **Exemplos**: Pasta `modules/` do cliente

---

**Dica**: Salve este cheat sheet como favorito e consulte sempre que precisar de referências rápidas durante o desenvolvimento!

---

> [!success] Navegação
> - [[Getting_Started_Guide]] - Comece aqui
> - [[Module_System_Guide]] - Desenvolvimento de módulos
> - [[UI_System_Guide]] - Interface do usuário
> - [[Lua_API_Reference]] - Referência completa da API


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

