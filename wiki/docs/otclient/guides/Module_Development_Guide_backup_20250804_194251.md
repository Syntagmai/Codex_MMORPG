---
title: Firstmodule
tags: [otclient, system, guide, documentation]
status: completed
aliases: [Firstmodule]
---

# Criando Seu Primeiro Módulo - OTClient

Este guia prático te levará passo a passo na criação de módulos completos e funcionais para o OTClient. Aprenderemos desde conceitos básicos até implementações avançadas com exemplos reais.

## 📋 Índice

1. [Preparação do Ambiente](#preparação-do-ambiente)
2. [Anatomia de um Módulo](#anatomia-de-um-módulo)
3. [Projeto 1: Contador de Cliques](#projeto-1-contador-de-cliques)
4. [Projeto 2: Sistema de Notificações](#projeto-2-sistema-de-notificações)
5. [Projeto 3: Monitor de Status](#projeto-3-monitor-de-status)
6. [Projeto 4: Sistema de Comandos](#projeto-4-sistema-de-comandos)
7. [Projeto 5: Mini-Jogo Integrado](#projeto-5-mini-jogo-integrado)
8. [Debugging e Testes](#debugging-e-testes)
9. [Otimização e Performance](#otimização-e-performance)
10. [Distribuição e Compartilhamento](#distribuição-e-compartilhamento)

## 🛠️ Preparação do Ambiente

### 📁 **Estrutura de Desenvolvimento**

```bash
# Criar diretório para seus módulos customizados
mkdir modules/custom_modules
cd modules/custom_modules

# Estrutura recomendada para organização
custom_modules/
├── my_clickcounter/           # Projeto 1
├── my_notifications/          # Projeto 2
├── my_statusmonitor/          # Projeto 3
├── my_commands/               # Projeto 4
├── my_minigame/               # Projeto 5
└── shared/                    # Utilitários compartilhados
    ├── utils.lua
    └── config.lua
```

### 🔧 **Setup Inicial**

#### Nível Basic
```lua
-- modules/custom_modules/shared/utils.lua
-- Utilitários compartilhados entre módulos
local Utils = {}
-- Função para criar janela padrão
function Utils.createWindow(id, title, size, parent)
    local window = g_ui.createWidget('MainWindow', parent or rootWidget)
end
-- Função para adicionar botão no menu
function Utils.addMenuButton(id, text, icon, callback)
    local topMenu = modules.client_topmenu.getTopMenu()
    local button = topMenu:addLeftButton(id, text, icon)
end
-- Sistema de log customizado
function Utils.log(module, message, level)
    local timestamp = os.date('%H:%M:%S')
    print(string.format('[%s][%s][%s] %s', timestamp, level, module, message))
end
-- Verificar se está em jogo
function Utils.isInGame()
end
```

#### Nível Intermediate
```lua
-- modules/custom_modules/shared/utils.lua
-- Utilitários compartilhados entre módulos

local Utils = {}

-- Função para criar janela padrão
function Utils.createWindow(id, title, size, parent)
    local window = g_ui.createWidget('MainWindow', parent or rootWidget)
    window:setId(id)
    window:setText(title)
    window:setSize(size)
    window:centerIn('parent')
    return window
end

-- Função para adicionar botão no menu
function Utils.addMenuButton(id, text, icon, callback)
    local topMenu = modules.client_topmenu.getTopMenu()
    local button = topMenu:addLeftButton(id, text, icon)
    button.onClick = callback
    return button
end

-- Sistema de log customizado
function Utils.log(module, message, level)
    level = level or 'INFO'
    local timestamp = os.date('%H:%M:%S')
    print(string.format('[%s][%s][%s] %s', timestamp, level, module, message))
end

-- Verificar se está em jogo
function Utils.isInGame()
    return g_game.isOnline() and g_game.getLocalPlayer()
end

return Utils
```

#### Nível Advanced
```lua
-- modules/custom_modules/shared/utils.lua
-- Utilitários compartilhados entre módulos

local Utils = {}

-- Função para criar janela padrão
function Utils.createWindow(id, title, size, parent)
    local window = g_ui.createWidget('MainWindow', parent or rootWidget)
    window:setId(id)
    window:setText(title)
    window:setSize(size)
    window:centerIn('parent')
    return window
end

-- Função para adicionar botão no menu
function Utils.addMenuButton(id, text, icon, callback)
    local topMenu = modules.client_topmenu.getTopMenu()
    local button = topMenu:addLeftButton(id, text, icon)
    button.onClick = callback
    return button
end

-- Sistema de log customizado
function Utils.log(module, message, level)
    level = level or 'INFO'
    local timestamp = os.date('%H:%M:%S')
    print(string.format('[%s][%s][%s] %s', timestamp, level, module, message))
end

-- Verificar se está em jogo
function Utils.isInGame()
    return g_game.isOnline() and g_game.getLocalPlayer()
end

return Utils
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

## 🧩 Anatomia de um Módulo

### 📝 **Estrutura Completa de um Módulo**

```
my_module/
├── my_module.otmod           # Metadados e configuração
├── my_module.lua             # Lógica principal
├── my_module.otui            # Interface principal
├── styles/                   # Estilos customizados
│   ├── buttons.otui
│   └── windows.otui
├── images/                   # Assets visuais
│   ├── icon.png
│   └── background.png
├── sounds/                   # Assets de áudio
│   └── notification.ogg
├── data/                     # Dados do módulo
│   └── config.json
└── README.md                 # Documentação
```

### 🔧 **Template Base para Novos Módulos**

```yaml
# template.otmod
Module
  name: my_module
  description: Descrição do meu módulo
  author: Seu Nome
  version: 1.0.0
  website: https://github.com/seuusuario/meu-modulo
  
  autoload: true
  autoload-priority: 500
  sandboxed: true
  
  dependencies:
    - game_interface
    
  load-later:
    - game_hotkeys
    
  scripts: [ my_module ]
  
  @onLoad: init()
  @onUnload: terminate()
```

## 🖱️ Projeto 1: Contador de Cliques

Vamos criar um módulo que conta e exibe cliques do jogador, com estatísticas e persistência de dados.

### 📄 **1. Arquivo de Metadados**

```yaml
# modules/custom_modules/my_clickcounter/clickcounter.otmod
Module
  name: clickcounter
  description: Contador de cliques com estatísticas avançadas
  author: Tutorial OTClient
  version: 1.0.0
  
  autoload: true
  autoload-priority: 200
  sandboxed: true
  
  dependencies:
    - client_topmenu
    
  scripts: [ clickcounter ]
  
  @onLoad: init()
  @onUnload: terminate()
```

### 🎨 **2. Interface do Usuário**

```yaml
# modules/custom_modules/my_clickcounter/clickcounter.otui
ClickCounterWindow < MainWindow
  id: clickCounterWindow
  !text: tr('Contador de Cliques')
  size: 350 280
  @onEscape: ClickCounter.hide()
  
  Panel
    id: statsPanel
    anchors.top: parent.top
    anchors.left: parent.left
    anchors.right: parent.right
    height: 120
    margin: 10
    background-color: #2c3e50
    border: 1px solid #34495e
    
    Label
      id: totalClicksLabel
      !text: tr('Total de Cliques: 0')
      anchors.top: parent.top
      anchors.left: parent.left
      margin: 10
      font: verdana-11px-rounded
      color: #ecf0f1
      
    Label
      id: sessionClicksLabel
      !text: tr('Cliques na Sessão: 0')
      anchors.top: prev.bottom
      anchors.left: parent.left
      margin-top: 5
      margin-left: 10
      font: verdana-11px-rounded
      color: #ecf0f1
      
    Label
      id: cpsLabel
      !text: tr('CPS: 0.0')
      anchors.top: prev.bottom
      anchors.left: parent.left
      margin-top: 5
      margin-left: 10
      font: verdana-11px-rounded
      color: #e74c3c
      
    Label
      id: recordLabel
      !text: tr('Recorde CPS: 0.0')
      anchors.top: prev.bottom
      anchors.left: parent.left
      margin-top: 5
      margin-left: 10
      font: verdana-11px-rounded
      color: #f39c12
      
  Panel
    id: controlPanel
    anchors.top: statsPanel.bottom
    anchors.left: parent.left
    anchors.right: parent.right
    height: 100
    margin: 10
    margin-top: 5
    background-color: #34495e
    border: 1px solid #2c3e50
    
    Button
      id: resetSessionButton
      !text: tr('Reset Sessão')
      anchors.top: parent.top
      anchors.left: parent.left
      size: 100 25
      margin: 10
      
    Button
      id: resetAllButton
      !text: tr('Reset Tudo')
      anchors.top: parent.top
      anchors.right: parent.right
      size: 100 25
      margin: 10
      
    CheckBox
      id: soundEnabledCheck
      !text: tr('Sons Habilitados')
      anchors.top: resetSessionButton.bottom
      anchors.left: parent.left
      margin: 10
      margin-top: 5
      
    CheckBox
      id: autoHideCheck
      !text: tr('Auto Ocultar')
      anchors.top: resetSessionButton.bottom
      anchors.right: parent.right
      margin: 10
      margin-top: 5
```

### 💻 **3. Lógica Principal**

#### 🎯 **Visão Geral da Lógica**

A lógica principal do módulo é responsável por gerenciar o estado e comportamento do sistema.



#### 🔧 **Detalhes de Implementação**

#### Inicialização e Configuração
```lua
-- modules/custom_modules/my_clickcounter/clickcounter.lua
ClickCounter = {}

-- Variáveis globais do módulo
local clickCounterWindow
local menuButton

-- Estatísticas
local stats = {
    totalClicks = 0,
    sessionClicks = 0,
    lastClickTime = 0,
    cps = 0.0,
    recordCPS = 0.0,
    clickTimes = {}
}

-- Configurações
local config = {
    soundEnabled = true,
    autoHide = false,
    saveInterval = 30000  -- 30 segundos
}
```

#### Funcionalidade 1
```lua

-- Labels da interface
local labels = {}

function ClickCounter.init()
    -- Carregar interface
    clickCounterWindow = g_ui.loadUI('clickcounter', rootWidget)
    clickCounterWindow:hide()
    
    -- Obter referências dos labels
    labels.totalClicks = clickCounterWindow:getChildById('totalClicksLabel')
    labels.sessionClicks = clickCounterWindow:getChildById('sessionClicksLabel')
    labels.cps = clickCounterWindow:getChildById('cpsLabel')
    labels.record = clickCounterWindow:getChildById('recordLabel')
    
    -- Configurar botões
    local resetSessionBtn = clickCounterWindow:getChildById('resetSessionButton')
    local resetAllBtn = clickCounterWindow:getChildById('resetAllButton')
    local soundCheck = clickCounterWindow:getChildById('soundEnabledCheck')
    local autoHideCheck = clickCounterWindow:getChildById('autoHideCheck')
    
    resetSessionBtn.onClick = ClickCounter.resetSession
    resetAllBtn.onClick = ClickCounter.resetAll
    soundCheck.onCheckChange = function(widget, checked)
        config.soundEnabled = checked
        ClickCounter.saveConfig()
    end
```

#### Funcionalidade 2
```lua
    autoHideCheck.onCheckChange = function(widget, checked)
        config.autoHide = checked
        ClickCounter.saveConfig()
    end
    
    -- Adicionar botão no menu
    menuButton = modules.client_topmenu.addLeftButton('clickCounterButton', 
        tr('Contador'), '/images/topbuttons/logout')
    menuButton.onClick = ClickCounter.toggle
    
    -- Conectar eventos de mouse globais
    connect(rootWidget, { onMousePress = ClickCounter.onMouseClick })
    
    -- Carregar configurações e dados salvos
    ClickCounter.loadConfig()
    ClickCounter.loadStats()
    
    -- Agendar salvamento automático
    ClickCounter.scheduleAutoSave()
    
    -- Atualizar interface inicial
    ClickCounter.updateInterface()
    
    print("ClickCounter: Módulo iniciado com sucesso!")
end
```

#### Funcionalidade 3
```lua

function ClickCounter.terminate()
    -- Salvar dados antes de finalizar
    ClickCounter.saveStats()
    ClickCounter.saveConfig()
    
    -- Desconectar eventos
    disconnect(rootWidget, { onMousePress = ClickCounter.onMouseClick })
    
    -- Limpar interface
    clickCounterWindow:destroy()
    menuButton:destroy()
    
    print("ClickCounter: Módulo finalizado!")
end

function ClickCounter.onMouseClick(widget, pos, button)
    -- Contar apenas cliques com botão esquerdo
    if button ~= MouseLeftButton then
        return
    end
```

#### Funcionalidade 4
```lua
    
    local currentTime = g_clock.millis()
    
    -- Atualizar contadores
    stats.totalClicks = stats.totalClicks + 1
    stats.sessionClicks = stats.sessionClicks + 1
    
    -- Calcular CPS
    table.insert(stats.clickTimes, currentTime)
    
    -- Manter apenas últimos 10 cliques para cálculo de CPS
    if #stats.clickTimes > 10 then
        table.remove(stats.clickTimes, 1)
    end
    
    -- Calcular CPS atual
    if #stats.clickTimes >= 2 then
        local timeSpan = stats.clickTimes[#stats.clickTimes] - stats.clickTimes[1]
        if timeSpan > 0 then
            stats.cps = (#stats.clickTimes - 1) / (timeSpan / 1000)
            
            -- Atualizar recorde
            if stats.cps > stats.recordCPS then
                stats.recordCPS = stats.cps
                if config.soundEnabled then
                    -- Tocar som de novo recorde (se existir)
                    -- g_sounds.playSoundFile('/sounds/achievement.ogg')
                end
```

#### Funcionalidade 5
```lua
            end
        end
    end
    
    -- Atualizar interface
    ClickCounter.updateInterface()
    
    -- Auto-hide se habilitado
    if config.autoHide and clickCounterWindow:isVisible() then
        scheduleEvent(function()
            if currentTime == stats.lastClickTime then  -- Se não houve cliques recentes
                ClickCounter.hide()
            end
        end, 3000)
    end
    
    stats.lastClickTime = currentTime
end

function ClickCounter.updateInterface()
    labels.totalClicks:setText(tr('Total de Cliques: %d', stats.totalClicks))
    labels.sessionClicks:setText(tr('Cliques na Sessão: %d', stats.sessionClicks))
    labels.cps:setText(tr('CPS: %.1f', stats.cps))
    labels.record:setText(tr('Recorde CPS: %.1f', stats.recordCPS))
end
```

#### Funcionalidade 6
```lua

function ClickCounter.resetSession()
    stats.sessionClicks = 0
    stats.cps = 0.0
    stats.clickTimes = {}
    ClickCounter.updateInterface()
    print("ClickCounter: Estatísticas da sessão resetadas")
end

function ClickCounter.resetAll()
    stats.totalClicks = 0
    stats.sessionClicks = 0
    stats.cps = 0.0
    stats.recordCPS = 0.0
    stats.clickTimes = {}
    ClickCounter.updateInterface()
    ClickCounter.saveStats()
    print("ClickCounter: Todas as estatísticas resetadas")
end

function ClickCounter.show()
```

#### Funcionalidade 7
```lua
    clickCounterWindow:show()
    clickCounterWindow:raise()
    clickCounterWindow:focus()
end

function ClickCounter.hide()
    clickCounterWindow:hide()
end

function ClickCounter.toggle()
    if clickCounterWindow:isVisible() then
        ClickCounter.hide()
    else
        ClickCounter.show()
    end
end

-- Sistema de persistência
function ClickCounter.saveStats()
    g_settings.setNode('clickcounter-stats', stats)
    g_settings.save()
end
```

#### Funcionalidade 8
```lua

function ClickCounter.loadStats()
    local savedStats = g_settings.getNode('clickcounter-stats')
    if savedStats then
        stats.totalClicks = savedStats.totalClicks or 0
        stats.recordCPS = savedStats.recordCPS or 0.0
        -- Não carregar dados da sessão
    end
end

function ClickCounter.saveConfig()
    g_settings.setNode('clickcounter-config', config)
    g_settings.save()
end

function ClickCounter.loadConfig()
    local savedConfig = g_settings.getNode('clickcounter-config')
    if savedConfig then
        config.soundEnabled = savedConfig.soundEnabled ~= false
        config.autoHide = savedConfig.autoHide or false
        
        -- Atualizar checkboxes
        local soundCheck = clickCounterWindow:getChildById('soundEnabledCheck')
        local autoHideCheck = clickCounterWindow:getChildById('autoHideCheck')
        soundCheck:setChecked(config.soundEnabled)
        autoHideCheck:setChecked(config.autoHide)
    end
```

#### Funcionalidade 9
```lua
end

function ClickCounter.scheduleAutoSave()
    scheduleEvent(function()
        ClickCounter.saveStats()
        ClickCounter.scheduleAutoSave()  -- Reagendar
    end, config.saveInterval)
end

-- API pública para outros módulos
function ClickCounter.getStats()
    return table.copy(stats)
end

function ClickCounter.getTotalClicks()
    return stats.totalClicks
end

function ClickCounter.getSessionClicks()
    return stats.sessionClicks
end
```

#### Finalização
```lua

function ClickCounter.getCurrentCPS()
    return stats.cps
end
```

## 🔔 Projeto 2: Sistema de Notificações

Um sistema completo de notificações em tempo real com diferentes tipos e prioridades.


#### 📚 **Referência das Funções**

| Função | Descrição | Parâmetros |
|--------|-----------|------------|
| `init()` | Inicializa o módulo | Nenhum |
| `terminate()` | Finaliza o módulo | Nenhum |
| `update()` | Atualiza o estado | deltaTime |
| `handleEvent()` | Processa eventos | event |

### 📄 **1. Arquivo de Metadados**

```yaml
# modules/custom_modules/my_notifications/notifications.otmod
Module
  name: notifications
  description: Sistema avançado de notificações em tempo real
  author: Tutorial OTClient
  version: 1.0.0
  
  autoload: true
  autoload-priority: 150
  sandboxed: true
  
  dependencies:
    - game_interface
    - gamelib
    
  scripts: [ notifications ]
  
  @onLoad: init()
  @onUnload: terminate()
```

### 🎨 **2. Interface de Notificação**

```yaml
# modules/custom_modules/my_notifications/notifications.otui
NotificationWidget < Panel
  height: 60
  margin-bottom: 5
  background-color: alpha
  border-radius: 5
  
  Panel
    id: iconPanel
    anchors.left: parent.left
    anchors.top: parent.top
    anchors.bottom: parent.bottom
    width: 50
    background-color: #3498db
    border-top-left-radius: 5
    border-bottom-left-radius: 5
    
    UIWidget
      id: icon
      anchors.centerIn: parent
      size: 24 24
      
  Panel
    id: contentPanel
    anchors.left: iconPanel.right
    anchors.right: parent.right
    anchors.top: parent.top
    anchors.bottom: parent.bottom
    background-color: #2c3e50
    border-top-right-radius: 5
    border-bottom-right-radius: 5
    
    Label
      id: titleLabel
      anchors.top: parent.top
      anchors.left: parent.left
      anchors.right: closeButton.left
      margin: 8
      margin-bottom: 2
      font: verdana-11px-rounded
      color: #ecf0f1
      text-auto-resize: true
      
    Label
      id: messageLabel
      anchors.top: titleLabel.bottom
      anchors.left: parent.left
      anchors.right: closeButton.left
      anchors.bottom: parent.bottom
      margin: 8
      margin-top: 2
      font: verdana-9px-rounded
      color: #bdc3c7
      text-wrap: true
      
    Button
      id: closeButton
      anchors.top: parent.top
      anchors.right: parent.right
      margin: 5
      size: 20 20
      !text: ×
      font: verdana-11px-rounded

NotificationContainer < Panel
  id: notificationContainer
  anchors.top: parent.top
  anchors.right: parent.right
  width: 300
  margin: 20
  layout: verticalBox
```

### 💻 **3. Sistema de Notificações**

#### 🎯 **Visão Geral do Sistema**

O sistema de notificações permite comunicação entre diferentes partes do módulo.



#### 🔧 **Detalhes de Implementação**

#### Inicialização e Configuração
```lua
-- modules/custom_modules/my_notifications/notifications.lua
Notifications = {}

-- Container de notificações
local notificationContainer
local activeNotifications = {}
local notificationQueue = {}

-- Configurações
local config = {
    maxNotifications = 5,
    defaultDuration = 5000,
    animationDuration = 300,
    soundEnabled = true,
    position = 'top-right'
}

-- Tipos de notificação
Notifications.TYPES = {
    INFO = {
        color = '#3498db',
        icon = '/images/icons/info',
        sound = '/sounds/notification_info.ogg'
    },
```

#### Funcionalidade 1
```lua
    SUCCESS = {
        color = '#27ae60',
        icon = '/images/icons/success',
        sound = '/sounds/notification_success.ogg'
    },
    WARNING = {
        color = '#f39c12',
        icon = '/images/icons/warning',
        sound = '/sounds/notification_warning.ogg'
    },
    ERROR = {
        color = '#e74c3c',
        icon = '/images/icons/error',
        sound = '/sounds/notification_error.ogg'
    },
    ACHIEVEMENT = {
        color = '#9b59b6',
        icon = '/images/icons/achievement',
        sound = '/sounds/notification_achievement.ogg'
    }
}
```

#### Funcionalidade 2
```lua

function Notifications.init()
    -- Criar container de notificações
    notificationContainer = g_ui.createWidget('NotificationContainer', rootWidget)
    
    -- Conectar eventos do jogo para notificações automáticas
    connect(g_game, {
        onGameStart = function()
            Notifications.show('Conectado', 'Logado no servidor com sucesso!', Notifications.TYPES.SUCCESS)
        end,
        onGameEnd = function()
            Notifications.show('Desconectado', 'Conexão com servidor perdida.', Notifications.TYPES.WARNING)
        end,
        onTextMessage = Notifications.onTextMessage,
        onCreatureAppear = Notifications.onCreatureAppear
    })
    
    connect(LocalPlayer, {
        onLevelChange = function(player, level, percent)
            if level > 1 then  -- Não mostrar para level 1 inicial
                Notifications.show('Level Up!', 
                    string.format('Parabéns! Você alcançou o level %d!', level), 
                    Notifications.TYPES.ACHIEVEMENT, 8000)
            end
```

#### Funcionalidade 3
```lua
        end,
        onHealthChange = function(player, health, maxHealth)
            local healthPercent = (health / maxHealth) * 100
            if healthPercent <= 15 and healthPercent > 0 then
                Notifications.show('Vida Baixa!', 
                    string.format('Vida crítica: %d%%', math.floor(healthPercent)), 
                    Notifications.TYPES.ERROR, 3000)
            end
        end
    })
    
    print("Notifications: Sistema iniciado!")
end

function Notifications.terminate()
    -- Limpar todas as notificações
    Notifications.clearAll()
    
    -- Desconectar eventos
    disconnect(g_game, {
        onGameStart = function() end,
        onGameEnd = function() end,
        onTextMessage = Notifications.onTextMessage,
        onCreatureAppear = Notifications.onCreatureAppear
    })
```

#### Funcionalidade 4
```lua
    
    -- Destruir container
    notificationContainer:destroy()
    
    print("Notifications: Sistema finalizado!")
end

function Notifications.show(title, message, type, duration)
    type = type or Notifications.TYPES.INFO
    duration = duration or config.defaultDuration
    
    -- Se exceder limite, adicionar à fila
    if #activeNotifications >= config.maxNotifications then
        table.insert(notificationQueue, {
            title = title,
            message = message,
            type = type,
            duration = duration
        })
        return
    end
```

#### Funcionalidade 5
```lua
    
    -- Criar widget de notificação
    local notification = g_ui.createWidget('NotificationWidget', notificationContainer)
    
    -- Configurar conteúdo
    local iconPanel = notification:getChildById('iconPanel')
    local titleLabel = notification:getChildById('titleLabel')
    local messageLabel = notification:getChildById('messageLabel')
    local closeButton = notification:getChildById('closeButton')
    
    iconPanel:setBackgroundColor(type.color)
    titleLabel:setText(title)
    messageLabel:setText(message)
    
    -- Configurar botão de fechar
    closeButton.onClick = function()
        Notifications.remove(notification)
    end
    
    -- Adicionar à lista ativa
    table.insert(activeNotifications, notification)
    
    -- Animação de entrada
    notification:setOpacity(0)
    notification:setMarginLeft(300)  -- Fora da tela
    
    -- Animar entrada
    local tween = notification:addAnchoredTween(easeOutBack, config.animationDuration)
    tween:setMarginLeft(0)
    tween:setOpacity(1)
    
    -- Tocar som se habilitado
    if config.soundEnabled and type.sound then
        -- g_sounds.playSoundFile(type.sound)
    end
```

#### Funcionalidade 6
```lua
    
    -- Agendar remoção automática
    scheduleEvent(function()
        if notification:isDestroyed() then return end
        Notifications.remove(notification)
    end, duration)
    
    return notification
end

function Notifications.remove(notification)
    -- Encontrar índice na lista ativa
    local index = table.find(activeNotifications, notification)
    if not index then return end
    
    -- Remover da lista
    table.remove(activeNotifications, index)
    
    -- Animação de saída
    local tween = notification:addAnchoredTween(easeInBack, config.animationDuration)
    tween:setMarginLeft(300)
    tween:setOpacity(0)
    
    -- Destruir após animação
    scheduleEvent(function()
        if not notification:isDestroyed() then
            notification:destroy()
        end
```

#### Funcionalidade 7
```lua
        
        -- Processar fila se houver
        Notifications.processQueue()
    end, config.animationDuration)
end

function Notifications.processQueue()
    if #notificationQueue > 0 and #activeNotifications < config.maxNotifications then
        local queued = table.remove(notificationQueue, 1)
        Notifications.show(queued.title, queued.message, queued.type, queued.duration)
    end
end

function Notifications.clearAll()
    for _, notification in ipairs(activeNotifications) do
        if not notification:isDestroyed() then
            notification:destroy()
        end
    end
    activeNotifications = {}
    notificationQueue = {}
end
```

#### Funcionalidade 8
```lua

-- Event handlers para notificações automáticas
function Notifications.onTextMessage(mode, text)
    -- Notificar mensagens importantes
    if mode == MessageModes.StatusDefault then
        if text:find('level') then
            Notifications.show('Experiência', text, Notifications.TYPES.INFO)
        elseif text:find('magic level') then
            Notifications.show('Magic Level', text, Notifications.TYPES.SUCCESS)
        end
    end
end

function Notifications.onCreatureAppear(creature)
    if not creature:isPlayer() then return end
    
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    -- Notificar aparição de outros jogadores próximos
    local distance = math.abs(creature:getPosition().x - player:getPosition().x) + 
                    math.abs(creature:getPosition().y - player:getPosition().y)
    
    if distance <= 5 and creature ~= player then
        Notifications.show('Jogador Próximo', 
            string.format('%s apareceu por perto', creature:getName()), 
            Notifications.TYPES.INFO, 3000)
    end
```

#### Funcionalidade 9
```lua
end

-- API pública
function Notifications.info(title, message, duration)
    return Notifications.show(title, message, Notifications.TYPES.INFO, duration)
end

function Notifications.success(title, message, duration)
    return Notifications.show(title, message, Notifications.TYPES.SUCCESS, duration)
end

function Notifications.warning(title, message, duration)
    return Notifications.show(title, message, Notifications.TYPES.WARNING, duration)
end

function Notifications.error(title, message, duration)
    return Notifications.show(title, message, Notifications.TYPES.ERROR, duration)
end

function Notifications.achievement(title, message, duration)
    return Notifications.show(title, message, Notifications.TYPES.ACHIEVEMENT, duration)
end
```

#### Finalização
```lua

function Notifications.configure(newConfig)
    for key, value in pairs(newConfig) do
        if config[key] ~= nil then
            config[key] = value
        end
    end
end
```

## 📊 Projeto 3: Monitor de Status

Um monitor completo que exibe informações detalhadas do jogador em tempo real.


#### 🎮 **Exemplos de Uso**

**Exemplo 1: Enviar notificação**
#### Nível Basic
```lua
-- Enviar notificação de evento
module:notify("eventOccurred", {data = "example"})
```

#### Nível Intermediate
```lua
-- Enviar notificação de evento
module:notify("eventOccurred", {data = "example"})
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
-- Enviar notificação de evento
module:notify("eventOccurred", {data = "example"})
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

**Exemplo 2: Receber notificação**
#### Nível Basic
```lua
-- Receber notificação
module:on("eventOccurred", function(data)
    print("Evento recebido:", data)
end)
```

#### Nível Intermediate
```lua
-- Receber notificação
module:on("eventOccurred", function(data)
    print("Evento recebido:", data)
end)
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
-- Receber notificação
module:on("eventOccurred", function(data)
    print("Evento recebido:", data)
end)
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

### 📄 **1. Arquivo de Metadados**

```yaml
# modules/custom_modules/my_statusmonitor/statusmonitor.otmod
Module
  name: statusmonitor
  description: Monitor avançado de status do jogador
  author: Tutorial OTClient
  version: 1.0.0
  
  autoload: true
  autoload-priority: 300
  sandboxed: true
  
  dependencies:
    - game_interface
    - gamelib
    
  load-later:
    - notifications
    
  scripts: [ statusmonitor ]
  
  @onLoad: init()
  @onUnload: terminate()
```

### 🎨 **2. Interface do Monitor**

```yaml
# modules/custom_modules/my_statusmonitor/statusmonitor.otui
StatusMonitorWindow < MiniWindow
  id: statusMonitorWindow
  !text: tr('Monitor de Status')
  size: 280 400
  
  MiniWindowContents
    ScrollablePanel
      id: statusContainer
      anchors.fill: parent
      vertical-scrollbar: statusScrollBar
      layout: verticalBox
      
      Panel
        id: playerInfoPanel
        height: 80
        margin-bottom: 5
        background-color: #2c3e50
        border: 1px solid #34495e
        
        Label
          id: playerNameLabel
          anchors.top: parent.top
          anchors.left: parent.left
          margin: 8
          font: verdana-11px-rounded
          color: #ecf0f1
          
        Label
          id: playerLevelLabel
          anchors.top: prev.bottom
          anchors.left: parent.left
          margin-left: 8
          margin-top: 2
          font: verdana-9px-rounded
          color: #bdc3c7
          
        Label
          id: playerVocationLabel
          anchors.top: prev.bottom
          anchors.left: parent.left
          margin-left: 8
          margin-top: 2
          font: verdana-9px-rounded
          color: #bdc3c7
          
      Panel
        id: healthPanel
        height: 60
        margin-bottom: 5
        background-color: #27ae60
        border: 1px solid #229954
        
        Label
          id: healthTitle
          !text: tr('Health')
          anchors.top: parent.top
          anchors.left: parent.left
          margin: 8
          font: verdana-11px-rounded
          color: white
          
        ProgressBar
          id: healthBar
          anchors.top: prev.bottom
          anchors.left: parent.left
          anchors.right: parent.right
          margin: 8
          margin-top: 2
          height: 20
          background-color: #1e8449
          
        Label
          id: healthLabel
          anchors.centerIn: healthBar
          font: verdana-9px-rounded
          color: white
          
      Panel
        id: manaPanel
        height: 60
        margin-bottom: 5
        background-color: #3498db
        border: 1px solid #2980b9
        
        Label
          id: manaTitle
          !text: tr('Mana')
          anchors.top: parent.top
          anchors.left: parent.left
          margin: 8
          font: verdana-11px-rounded
          color: white
          
        ProgressBar
          id: manaBar
          anchors.top: prev.bottom
          anchors.left: parent.left
          anchors.right: parent.right
          margin: 8
          margin-top: 2
          height: 20
          background-color: #2471a3
          
        Label
          id: manaLabel
          anchors.centerIn: manaBar
          font: verdana-9px-rounded
          color: white
          
      Panel
        id: experiencePanel
        height: 60
        margin-bottom: 5
        background-color: #f39c12
        border: 1px solid #e67e22
        
        Label
          id: experienceTitle
          !text: tr('Experience')
          anchors.top: parent.top
          anchors.left: parent.left
          margin: 8
          font: verdana-11px-rounded
          color: white
          
        ProgressBar
          id: experienceBar
          anchors.top: prev.bottom
          anchors.left: parent.left
          anchors.right: parent.right
          margin: 8
          margin-top: 2
          height: 20
          background-color: #d68910
          
        Label
          id: experienceLabel
          anchors.centerIn: experienceBar
          font: verdana-9px-rounded
          color: white
          
      Panel
        id: additionalStatsPanel
        height: 120
        margin-bottom: 5
        background-color: #34495e
        border: 1px solid #2c3e50
        
        Label
          id: additionalStatsTitle
          !text: tr('Estatísticas Adicionais')
          anchors.top: parent.top
          anchors.left: parent.left
          margin: 8
          font: verdana-11px-rounded
          color: #ecf0f1
          
        Label
          id: capacityLabel
          anchors.top: prev.bottom
          anchors.left: parent.left
          margin-left: 8
          margin-top: 5
          font: verdana-9px-rounded
          color: #bdc3c7
          
        Label
          id: soulLabel
          anchors.top: prev.bottom
          anchors.left: parent.left
          margin-left: 8
          margin-top: 2
          font: verdana-9px-rounded
          color: #bdc3c7
          
        Label
          id: staminaLabel
          anchors.top: prev.bottom
          anchors.left: parent.left
          margin-left: 8
          margin-top: 2
          font: verdana-9px-rounded
          color: #bdc3c7
          
        Label
          id: speedLabel
          anchors.top: prev.bottom
          anchors.left: parent.left
          margin-left: 8
          margin-top: 2
          font: verdana-9px-rounded
          color: #bdc3c7
      
    VerticalScrollBar
      id: statusScrollBar
      anchors.top: parent.top
      anchors.bottom: parent.bottom
      anchors.right: parent.right
      step: 14
      pixels-scroll: true
```

### 💻 **3. Lógica do Monitor**

#### 🎯 **Conceitos do Monitor**

O monitor de status verifica e exibe informações em tempo real sobre o sistema.



#### 💻 **Implementação do Monitor**

#### Inicialização e Configuração
```lua
-- modules/custom_modules/my_statusmonitor/statusmonitor.lua
StatusMonitor = {}

local statusWindow
local widgets = {}
local updateTimer

-- Configurações
local config = {
    updateInterval = 100,  -- ms
    showInGame = true,
    autoHide = false,
    warningThresholds = {
        health = 20,  -- %
        mana = 15,    -- %
        capacity = 10 -- %
    }
}

function StatusMonitor.init()
    -- Criar janela
    statusWindow = g_ui.loadUI('statusmonitor', rootWidget)
    statusWindow:hide()
    
    -- Obter referências dos widgets
    widgets.playerName = statusWindow:getChildById('playerNameLabel')
    widgets.playerLevel = statusWindow:getChildById('playerLevelLabel')
    widgets.playerVocation = statusWindow:getChildById('playerVocationLabel')
    
    widgets.healthBar = statusWindow:getChildById('healthBar')
    widgets.healthLabel = statusWindow:getChildById('healthLabel')
    widgets.manaBar = statusWindow:getChildById('manaBar')
    widgets.manaLabel = statusWindow:getChildById('manaLabel')
    widgets.experienceBar = statusWindow:getChildById('experienceBar')
    widgets.experienceLabel = statusWindow:getChildById('experienceLabel')
    
    widgets.capacity = statusWindow:getChildById('capacityLabel')
    widgets.soul = statusWindow:getChildById('soulLabel')
    widgets.stamina = statusWindow:getChildById('staminaLabel')
    widgets.speed = statusWindow:getChildById('speedLabel')
    
    -- Adicionar botão no menu de janelas
    local toggleButton = modules.client_topmenu.addRightGameToggleButton(
        'statusMonitorButton', 
        tr('Status Monitor'), 
        '/images/topbuttons/minimap', 
        StatusMonitor.toggle
    )
    
    -- Conectar eventos do jogo
    connect(g_game, {
        onGameStart = StatusMonitor.onGameStart,
        onGameEnd = StatusMonitor.onGameEnd
    })
```

#### Funcionalidade 1
```lua
    
    -- Conectar eventos do jogador
    connect(LocalPlayer, {
        onHealthChange = StatusMonitor.onHealthChange,
        onManaChange = StatusMonitor.onManaChange,
        onLevelChange = StatusMonitor.onLevelChange,
        onExperienceChange = StatusMonitor.onExperienceChange,
        onFreeCapacityChange = StatusMonitor.onCapacityChange,
        onSoulChange = StatusMonitor.onSoulChange,
        onStaminaChange = StatusMonitor.onStaminaChange,
        onSpeedChange = StatusMonitor.onSpeedChange
    })
    
    -- Iniciar timer de atualização se em jogo
    if g_game.isOnline() then
        StatusMonitor.startUpdateTimer()
    end
    
    print("StatusMonitor: Monitor iniciado!")
end

function StatusMonitor.terminate()
```

#### Funcionalidade 2
```lua
    -- Parar timer
    StatusMonitor.stopUpdateTimer()
    
    -- Desconectar eventos
    disconnect(g_game, {
        onGameStart = StatusMonitor.onGameStart,
        onGameEnd = StatusMonitor.onGameEnd
    })
    
    disconnect(LocalPlayer, {
        onHealthChange = StatusMonitor.onHealthChange,
        onManaChange = StatusMonitor.onManaChange,
        onLevelChange = StatusMonitor.onLevelChange,
        onExperienceChange = StatusMonitor.onExperienceChange,
        onFreeCapacityChange = StatusMonitor.onCapacityChange,
        onSoulChange = StatusMonitor.onSoulChange,
        onStaminaChange = StatusMonitor.onStaminaChange,
        onSpeedChange = StatusMonitor.onSpeedChange
    })
    
    -- Destruir janela
    statusWindow:destroy()
    
    print("StatusMonitor: Monitor finalizado!")
end
```

#### Funcionalidade 3
```lua

function StatusMonitor.onGameStart()
    StatusMonitor.startUpdateTimer()
    if config.showInGame then
        StatusMonitor.show()
    end
    StatusMonitor.updatePlayerInfo()
end

function StatusMonitor.onGameEnd()
    StatusMonitor.stopUpdateTimer()
    if config.autoHide then
        StatusMonitor.hide()
    end
end

function StatusMonitor.startUpdateTimer()
    StatusMonitor.stopUpdateTimer()
    updateTimer = cycleEvent(StatusMonitor.update, config.updateInterval)
end

function StatusMonitor.stopUpdateTimer()
```

#### Funcionalidade 4
```lua
    if updateTimer then
        removeEvent(updateTimer)
        updateTimer = nil
    end
end

function StatusMonitor.update()
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    StatusMonitor.updatePlayerInfo()
    StatusMonitor.updateHealth()
    StatusMonitor.updateMana()
    StatusMonitor.updateExperience()
    StatusMonitor.updateAdditionalStats()
end

function StatusMonitor.updatePlayerInfo()
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    widgets.playerName:setText(player:getName())
    widgets.playerLevel:setText(tr('Level: %d', player:getLevel()))
    
    -- Vocation precisa ser obtida do protocolo ou estimada
    local vocation = 'Unknown'
    widgets.playerVocation:setText(tr('Vocation: %s', vocation))
end
```

#### Funcionalidade 5
```lua

function StatusMonitor.updateHealth()
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    local health = player:getHealth()
    local maxHealth = player:getMaxHealth()
    local percent = math.floor((health / maxHealth) * 100)
    
    widgets.healthBar:setPercent(percent)
    widgets.healthLabel:setText(string.format('%d / %d (%d%%)', health, maxHealth, percent))
    
    -- Avisar se vida baixa
    if percent <= config.warningThresholds.health then
        widgets.healthBar:setBackgroundColor('#e74c3c')
    else
        widgets.healthBar:setBackgroundColor('#27ae60')
    end
end

function StatusMonitor.updateMana()
```

#### Funcionalidade 6
```lua
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    local mana = player:getMana()
    local maxMana = player:getMaxMana()
    local percent = maxMana > 0 and math.floor((mana / maxMana) * 100) or 0
    
    widgets.manaBar:setPercent(percent)
    widgets.manaLabel:setText(string.format('%d / %d (%d%%)', mana, maxMana, percent))
    
    -- Avisar se mana baixa
    if percent <= config.warningThresholds.mana then
        widgets.manaBar:setBackgroundColor('#e74c3c')
    else
        widgets.manaBar:setBackgroundColor('#3498db')
    end
end

function StatusMonitor.updateExperience()
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    local level = player:getLevel()
    local experience = player:getExperience()
    local experiencePercent = player:getLevelPercent()
    
    widgets.experienceBar:setPercent(experiencePercent)
    widgets.experienceLabel:setText(string.format('Level %d (%d%%)', level, experiencePercent))
end
```

#### Funcionalidade 7
```lua

function StatusMonitor.updateAdditionalStats()
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    -- Capacity
    local capacity = player:getFreeCapacity()
    local totalCapacity = player:getTotalCapacity()
    local usedCapacity = totalCapacity - capacity
    local capacityPercent = math.floor((usedCapacity / totalCapacity) * 100)
    
    widgets.capacity:setText(tr('Capacity: %d / %d (%d%%)', usedCapacity, totalCapacity, capacityPercent))
    
    -- Avisar se capacity baixa
    if capacity / totalCapacity * 100 <= config.warningThresholds.capacity then
        widgets.capacity:setColor('#e74c3c')
    else
        widgets.capacity:setColor('#bdc3c7')
    end
    
    -- Soul
    local soul = player:getSoul()
    widgets.soul:setText(tr('Soul: %d', soul))
    
    -- Stamina
    local stamina = player:getStamina()
    local staminaHours = math.floor(stamina / 60)
    local staminaMinutes = stamina % 60
    widgets.stamina:setText(tr('Stamina: %dh %dm', staminaHours, staminaMinutes))
    
    -- Speed
    local speed = player:getSpeed()
    widgets.speed:setText(tr('Speed: %d', speed))
end
```

#### Funcionalidade 8
```lua

-- Event handlers
function StatusMonitor.onHealthChange(player, health, maxHealth)
    StatusMonitor.updateHealth()
    
    -- Notificação de vida crítica
    local percent = (health / maxHealth) * 100
    if percent <= 10 and percent > 0 then
        if Notifications then
            Notifications.error('Vida Crítica!', 
                string.format('Apenas %d%% de vida restante!', math.floor(percent)))
        end
    end
end

function StatusMonitor.onManaChange(player, mana, maxMana)
    StatusMonitor.updateMana()
end

function StatusMonitor.onLevelChange(player, level, percent)
    StatusMonitor.updatePlayerInfo()
    StatusMonitor.updateExperience()
end
```

#### Funcionalidade 9
```lua

function StatusMonitor.onExperienceChange(player, experience)
    StatusMonitor.updateExperience()
end

function StatusMonitor.onCapacityChange(player, freeCapacity)
    StatusMonitor.updateAdditionalStats()
end

function StatusMonitor.onSoulChange(player, soul)
    StatusMonitor.updateAdditionalStats()
end

function StatusMonitor.onStaminaChange(player, stamina)
    StatusMonitor.updateAdditionalStats()
end

function StatusMonitor.onSpeedChange(player, speed)
    StatusMonitor.updateAdditionalStats()
end

-- Interface functions
function StatusMonitor.show()
```

#### Funcionalidade 10
```lua
    statusWindow:show()
    statusWindow:raise()
end

function StatusMonitor.hide()
    statusWindow:hide()
end

function StatusMonitor.toggle()
    if statusWindow:isVisible() then
        StatusMonitor.hide()
    else
        StatusMonitor.show()
    end
end

-- API pública
function StatusMonitor.getPlayerStats()
    local player = g_game.getLocalPlayer()
    if not player then return nil end
    
    return {
        name = player:getName(),
        level = player:getLevel(),
        health = player:getHealth(),
        maxHealth = player:getMaxHealth(),
        mana = player:getMana(),
        maxMana = player:getMaxMana(),
        experience = player:getExperience(),
        levelPercent = player:getLevelPercent(),
        capacity = player:getFreeCapacity(),
        totalCapacity = player:getTotalCapacity(),
        soul = player:getSoul(),
        stamina = player:getStamina(),
        speed = player:getSpeed()
    }
```

#### Finalização
```lua
end

function StatusMonitor.configure(newConfig)
    for key, value in pairs(newConfig) do
        if config[key] ~= nil then
            config[key] = value
        end
    end
end
```

## 🔧 Debugging e Testes


#### 📚 **Referência da API do Monitor**

| Função | Descrição | Parâmetros |
|--------|-----------|------------|
| `startMonitoring()` | Inicia monitoramento | Nenhum |
| `stopMonitoring()` | Para monitoramento | Nenhum |
| `updateStatus()` | Atualiza status | Nenhum |
| `getStatus()` | Obtém status atual | Nenhum |
| `setUpdateInterval()` | Define intervalo | milliseconds |

### 🐛 **Sistema de Debug Integrado**

#### Nível Basic
```lua
-- Adicionar ao início de cada módulo
local DEBUG = true
local function debugLog(module, message, level)
    if not DEBUG then return end
    local timestamp = os.date('%H:%M:%S')
    local color = level == 'ERROR' and '#e74c3c' or 
    print(string.format('[%s][%s][%s] %s', timestamp, level, module, message))
    -- Também mostrar em notificação se disponível
    if level == 'ERROR' and Notifications then
        Notifications.error('Debug Error', message, 10000)
    end
end
-- Função de teste para cada módulo
function testModule()
    -- Testes específicos aqui
    local success = true
    if success then
    end
end
```

#### Nível Intermediate
```lua
-- Adicionar ao início de cada módulo
local DEBUG = true

local function debugLog(module, message, level)
    if not DEBUG then return end
    
    level = level or 'DEBUG'
    local timestamp = os.date('%H:%M:%S')
    local color = level == 'ERROR' and '#e74c3c' or 
                  level == 'WARN' and '#f39c12' or '#3498db'
    
    print(string.format('[%s][%s][%s] %s', timestamp, level, module, message))
    
    -- Também mostrar em notificação se disponível
    if level == 'ERROR' and Notifications then
        Notifications.error('Debug Error', message, 10000)
    end
end

-- Função de teste para cada módulo
function testModule()
    debugLog('MODULE_NAME', 'Iniciando testes do módulo')
    
    -- Testes específicos aqui
    local success = true
    
    if success then
        debugLog('MODULE_NAME', 'Todos os testes passaram!', 'INFO')
    else
        debugLog('MODULE_NAME', 'Alguns testes falharam!', 'ERROR')
    end
end
```

#### Nível Advanced
```lua
-- Adicionar ao início de cada módulo
local DEBUG = true

local function debugLog(module, message, level)
    if not DEBUG then return end
    
    level = level or 'DEBUG'
    local timestamp = os.date('%H:%M:%S')
    local color = level == 'ERROR' and '#e74c3c' or 
                  level == 'WARN' and '#f39c12' or '#3498db'
    
    print(string.format('[%s][%s][%s] %s', timestamp, level, module, message))
    
    -- Também mostrar em notificação se disponível
    if level == 'ERROR' and Notifications then
        Notifications.error('Debug Error', message, 10000)
    end
end

-- Função de teste para cada módulo
function testModule()
    debugLog('MODULE_NAME', 'Iniciando testes do módulo')
    
    -- Testes específicos aqui
    local success = true
    
    if success then
        debugLog('MODULE_NAME', 'Todos os testes passaram!', 'INFO')
    else
        debugLog('MODULE_NAME', 'Alguns testes falharam!', 'ERROR')
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

### 🔍 **Console de Desenvolvimento**

#### Nível Basic
```lua
-- Comandos úteis para o console do OTClient (Ctrl+T)
-- Recarregar módulo específico
function reloadModule(moduleName)
    local module = g_modules.getModule(moduleName)
    if module then
        print("Módulo " .. moduleName .. " recarregado!")
        print("Módulo " .. moduleName .. " não encontrado!")
    end
end
-- Listar módulos ativos
function listModules()
    print("Módulos carregados:")
        local status = module:isLoaded() and "LOADED" or "UNLOADED"
        print(string.format("  %s - %s", name, status))
    end
end
-- Testar notificação
function testNotification()
    if Notifications then
        Notifications.info('Teste', 'Esta é uma notificação de teste!')
        print("Módulo de notificações não carregado!")
    end
end
-- Ver estatísticas do contador
function showClickStats()
    if ClickCounter then
        local stats = ClickCounter.getStats()
        print("Estatísticas do Contador:")
        print("  Total: " .. stats.totalClicks)
        print("  Sessão: " .. stats.sessionClicks)
        print("  CPS: " .. string.format("%.1f", stats.cps))
        print("  Recorde: " .. string.format("%.1f", stats.recordCPS))
        print("Módulo ClickCounter não carregado!")
    end
end
```

#### Nível Intermediate
```lua
-- Comandos úteis para o console do OTClient (Ctrl+T)

-- Recarregar módulo específico
function reloadModule(moduleName)
    local module = g_modules.getModule(moduleName)
    if module then
        module:unload()
        module:load()
        print("Módulo " .. moduleName .. " recarregado!")
    else
        print("Módulo " .. moduleName .. " não encontrado!")
    end
end

-- Listar módulos ativos
function listModules()
    print("Módulos carregados:")
    for name, module in pairs(g_modules.getModules()) do
        local status = module:isLoaded() and "LOADED" or "UNLOADED"
        print(string.format("  %s - %s", name, status))
    end
end

-- Testar notificação
function testNotification()
    if Notifications then
        Notifications.info('Teste', 'Esta é uma notificação de teste!')
    else
        print("Módulo de notificações não carregado!")
    end
end

-- Ver estatísticas do contador
function showClickStats()
    if ClickCounter then
        local stats = ClickCounter.getStats()
        print("Estatísticas do Contador:")
        print("  Total: " .. stats.totalClicks)
        print("  Sessão: " .. stats.sessionClicks)
        print("  CPS: " .. string.format("%.1f", stats.cps))
        print("  Recorde: " .. string.format("%.1f", stats.recordCPS))
    else
        print("Módulo ClickCounter não carregado!")
    end
end
```

#### Nível Advanced
```lua
-- Comandos úteis para o console do OTClient (Ctrl+T)

-- Recarregar módulo específico
function reloadModule(moduleName)
    local module = g_modules.getModule(moduleName)
    if module then
        module:unload()
        module:load()
        print("Módulo " .. moduleName .. " recarregado!")
    else
        print("Módulo " .. moduleName .. " não encontrado!")
    end
end

-- Listar módulos ativos
function listModules()
    print("Módulos carregados:")
    for name, module in pairs(g_modules.getModules()) do
        local status = module:isLoaded() and "LOADED" or "UNLOADED"
        print(string.format("  %s - %s", name, status))
    end
end

-- Testar notificação
function testNotification()
    if Notifications then
        Notifications.info('Teste', 'Esta é uma notificação de teste!')
    else
        print("Módulo de notificações não carregado!")
    end
end

-- Ver estatísticas do contador
function showClickStats()
    if ClickCounter then
        local stats = ClickCounter.getStats()
        print("Estatísticas do Contador:")
        print("  Total: " .. stats.totalClicks)
        print("  Sessão: " .. stats.sessionClicks)
        print("  CPS: " .. string.format("%.1f", stats.cps))
        print("  Recorde: " .. string.format("%.1f", stats.recordCPS))
    else
        print("Módulo ClickCounter não carregado!")
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

Parabéns! 🎉 Você agora possui conhecimento completo para criar módulos sofisticados para o OTClient. Cada projeto apresentado demonstra diferentes aspectos do desenvolvimento, desde interfaces simples até sistemas complexos com persistência de dados e integração entre módulos.

**Próximos passos sugeridos:**
1. Implemente os módulos apresentados
2. Modifique-os conforme suas necessidades
3. Crie novos módulos combinando os conceitos aprendidos
4. Compartilhe suas criações com a comunidade

Lembre-se: o desenvolvimento no OTClient é principalmente baseado em Lua, permitindo iteração rápida e testes em tempo real sem necessidade de recompilação!

---

> [!success] Navegação
> - [[Getting_Started_Guide]] - Comece aqui
> - [[Module_System_Guide]] - Desenvolvimento de módulos
> - [[UI_System_Guide]] - Interface do usuário
> - [[Lua_API_Reference]] - Referência completa da API

