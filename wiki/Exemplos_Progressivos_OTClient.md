---
title: Exemplos Progressivos OTClient
tags: [exemplos, progressivos, basico, intermediario, avancado, tutorial]
type: guide
status: active
priority: alta
created: 2025-08-04
updated: 2025-08-04
---

# 🚀 **EXEMPLOS PROGRESSIVOS - OTClient**

> [!info] **APRENDA PASSO A PASSO**
> Este guia apresenta exemplos progressivos do básico ao avançado para desenvolvimento de módulos OTClient.

---

## 📋 **ÍNDICE DETALHADO**

### **🎯 Navegação Rápida**
1. [Nível Básico - Primeiros Passos](#-nível-básico---primeiros-passos)
2. [Nível Intermediário - Funcionalidades](#-nível-intermediário---funcionalidades)
3. [Nível Avançado - Sistemas Complexos](#-nível-avançado---sistemas-complexos)
4. [Projetos Práticos](#-projetos-práticos)

---

## 🌱 **NÍVEL BÁSICO - PRIMEIROS PASSOS**

### **📝 Exemplo 1: Olá Mundo Simples**

**Objetivo**: Criar um módulo que exibe uma mensagem simples.

#### Nível Basic
```lua
-- ========================================
-- MÓDULO BÁSICO - OLÁ MUNDO
-- ========================================
-- Este é o exemplo mais simples possível
-- Demonstra a estrutura básica de um módulo

HelloWorld = {}

-- Função de inicialização
function HelloWorld.init()
    -- Exibe mensagem no console
    print("Olá, mundo! Módulo carregado com sucesso!")
    
    -- Adiciona botão no menu principal
    local button = modules.client_topmenu.addLeftButton(
        'helloButton',
        'Olá Mundo',
        '/images/topbuttons/logout'
    )
    
    -- Define o que acontece quando clicar no botão
    button.onClick = function()
        print("Botão clicado! Olá, mundo!")
    end
end

-- Função de finalização
function HelloWorld.terminate()
    print("Módulo HelloWorld finalizado!")
end
```

#### Nível Intermediate
```lua
-- ========================================
-- MÓDULO BÁSICO - OLÁ MUNDO
-- ========================================
-- Este é o exemplo mais simples possível
-- Demonstra a estrutura básica de um módulo

HelloWorld = {}

-- Função de inicialização
function HelloWorld.init()
    -- Exibe mensagem no console
    print("Olá, mundo! Módulo carregado com sucesso!")
    
    -- Adiciona botão no menu principal
    local button = modules.client_topmenu.addLeftButton(
        'helloButton',
        'Olá Mundo',
        '/images/topbuttons/logout'
    )
    
    -- Define o que acontece quando clicar no botão
    button.onClick = function()
        print("Botão clicado! Olá, mundo!")
    end
end

-- Função de finalização
function HelloWorld.terminate()
    print("Módulo HelloWorld finalizado!")
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
-- ========================================
-- MÓDULO BÁSICO - OLÁ MUNDO
-- ========================================
-- Este é o exemplo mais simples possível
-- Demonstra a estrutura básica de um módulo

HelloWorld = {}

-- Função de inicialização
function HelloWorld.init()
    -- Exibe mensagem no console
    print("Olá, mundo! Módulo carregado com sucesso!")
    
    -- Adiciona botão no menu principal
    local button = modules.client_topmenu.addLeftButton(
        'helloButton',
        'Olá Mundo',
        '/images/topbuttons/logout'
    )
    
    -- Define o que acontece quando clicar no botão
    button.onClick = function()
        print("Botão clicado! Olá, mundo!")
    end
end

-- Função de finalização
function HelloWorld.terminate()
    print("Módulo HelloWorld finalizado!")
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

**O que aprender**:
- Estrutura básica de um módulo
- Funções `init()` e `terminate()`
- Como adicionar botões no menu
- Como usar `print()` para debug

---

### **📝 Exemplo 2: Contador Simples**

**Objetivo**: Criar um contador que incrementa a cada clique.

#### Nível Basic
```lua
-- ========================================
-- CONTADOR SIMPLES
-- ========================================
-- Demonstra como armazenar e modificar dados
-- Mostra interação básica com interface

SimpleCounter = {}

-- Variável para armazenar o contador
local clickCount = 0
local counterButton

function SimpleCounter.init()
    -- Cria botão no menu
    counterButton = modules.client_topmenu.addLeftButton(
        'counterButton',
        'Contador: 0',
        '/images/topbuttons/logout'
    )
    
    -- Define ação do clique
    counterButton.onClick = function()
        -- Incrementa o contador
        clickCount = clickCount + 1
        
        -- Atualiza o texto do botão
        counterButton:setText('Contador: ' .. clickCount)
        
        -- Exibe no console
        print("Contador: " .. clickCount)
    end
end

function SimpleCounter.terminate()
    print("Contador finalizado! Total de cliques: " .. clickCount)
end
```

#### Nível Intermediate
```lua
-- ========================================
-- CONTADOR SIMPLES
-- ========================================
-- Demonstra como armazenar e modificar dados
-- Mostra interação básica com interface

SimpleCounter = {}

-- Variável para armazenar o contador
local clickCount = 0
local counterButton

function SimpleCounter.init()
    -- Cria botão no menu
    counterButton = modules.client_topmenu.addLeftButton(
        'counterButton',
        'Contador: 0',
        '/images/topbuttons/logout'
    )
    
    -- Define ação do clique
    counterButton.onClick = function()
        -- Incrementa o contador
        clickCount = clickCount + 1
        
        -- Atualiza o texto do botão
        counterButton:setText('Contador: ' .. clickCount)
        
        -- Exibe no console
        print("Contador: " .. clickCount)
    end
end

function SimpleCounter.terminate()
    print("Contador finalizado! Total de cliques: " .. clickCount)
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
-- ========================================
-- CONTADOR SIMPLES
-- ========================================
-- Demonstra como armazenar e modificar dados
-- Mostra interação básica com interface

SimpleCounter = {}

-- Variável para armazenar o contador
local clickCount = 0
local counterButton

function SimpleCounter.init()
    -- Cria botão no menu
    counterButton = modules.client_topmenu.addLeftButton(
        'counterButton',
        'Contador: 0',
        '/images/topbuttons/logout'
    )
    
    -- Define ação do clique
    counterButton.onClick = function()
        -- Incrementa o contador
        clickCount = clickCount + 1
        
        -- Atualiza o texto do botão
        counterButton:setText('Contador: ' .. clickCount)
        
        -- Exibe no console
        print("Contador: " .. clickCount)
    end
end

function SimpleCounter.terminate()
    print("Contador finalizado! Total de cliques: " .. clickCount)
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

**O que aprender**:
- Como armazenar dados em variáveis
- Como atualizar interface dinamicamente
- Interação básica com widgets

---

## 🔧 **NÍVEL INTERMEDIÁRIO - FUNCIONALIDADES**

### **📝 Exemplo 3: Janela Personalizada**

**Objetivo**: Criar uma janela customizada com múltiplos elementos.

#### Inicialização e Configuração
```lua
-- ========================================
-- JANELA PERSONALIZADA
-- ========================================
-- Demonstra como criar interfaces complexas
-- Mostra uso de diferentes widgets

CustomWindow = {}

-- Variáveis do módulo
local mainWindow
local menuButton

function CustomWindow.init()
    -- Cria a janela principal
    mainWindow = g_ui.createWidget('MainWindow', rootWidget)
    mainWindow:setId('customWindow')
    mainWindow:setText('Janela Personalizada')
    mainWindow:setSize({width = 300, height = 200})
    mainWindow:centerIn('parent')
    mainWindow:hide() -- Inicia oculta
    
    -- Adiciona elementos à janela
    local label = g_ui.createWidget('Label', mainWindow)
    label:setText('Esta é uma janela personalizada!')
    label:setPosition({x = 10, y = 30})
    
    -- Botão para fechar
    local closeButton = g_ui.createWidget('Button', mainWindow)
    closeButton:setText('Fechar')
    closeButton:setPosition({x = 10, y = 150})
    closeButton.onClick = function()
        mainWindow:hide()
    end
```

#### Finalização
```lua
    
    -- Botão no menu para abrir a janela
    menuButton = modules.client_topmenu.addLeftButton(
        'customWindowButton',
        'Janela Custom',
        '/images/topbuttons/logout'
    )
    menuButton.onClick = function()
        mainWindow:show()
        mainWindow:raise()
        mainWindow:focus()
    end
end

function CustomWindow.terminate()
    mainWindow:destroy()
    menuButton:destroy()
end
```

**O que aprender**:
- Como criar janelas personalizadas
- Uso de diferentes widgets (Label, Button)
- Posicionamento e dimensionamento
- Controle de visibilidade

---

### **📝 Exemplo 4: Sistema de Configuração**

**Objetivo**: Criar um sistema que salva e carrega configurações.

#### Inicialização e Configuração
```lua
-- ========================================
-- SISTEMA DE CONFIGURAÇÃO
-- ========================================
-- Demonstra persistência de dados
-- Mostra como salvar/carregar configurações

ConfigSystem = {}

-- Configurações padrão
local config = {
    enabled = true,
    soundVolume = 50,
    autoSave = true,
    theme = 'dark'
}

-- Nome do arquivo de configuração
local configFile = 'config_system.json'

function ConfigSystem.init()
    -- Carrega configurações salvas
    ConfigSystem.loadConfig()
    
    -- Cria interface de configuração
    ConfigSystem.createConfigWindow()
    
    -- Adiciona botão no menu
    local button = modules.client_topmenu.addLeftButton(
        'configButton',
        'Configurações',
        '/images/topbuttons/logout'
    )
    button.onClick = function()
        ConfigSystem.showConfigWindow()
    end
```

#### Funcionalidade 1
```lua
end

function ConfigSystem.loadConfig()
    -- Tenta carregar configurações do arquivo
    local file = io.open(configFile, 'r')
    if file then
        local content = file:read('*all')
        file:close()
        
        -- Converte JSON para tabela (simplificado)
        local success, loadedConfig = pcall(json.decode, content)
        if success then
            config = loadedConfig
            print("Configurações carregadas com sucesso!")
        end
    end
end

function ConfigSystem.saveConfig()
    -- Salva configurações no arquivo
    local file = io.open(configFile, 'w')
    if file then
        local content = json.encode(config)
        file:write(content)
        file:close()
        print("Configurações salvas com sucesso!")
    end
```

#### Funcionalidade 2
```lua
end

function ConfigSystem.createConfigWindow()
    -- Cria janela de configurações
    local window = g_ui.createWidget('MainWindow', rootWidget)
    window:setId('configWindow')
    window:setText('Configurações')
    window:setSize({width = 400, height = 300})
    window:centerIn('parent')
    window:hide()
    
    -- Adiciona controles de configuração
    local enabledCheck = g_ui.createWidget('CheckBox', window)
    enabledCheck:setText('Habilitado')
    enabledCheck:setPosition({x = 10, y = 30})
    enabledCheck:setChecked(config.enabled)
    enabledCheck.onCheckChange = function(widget, checked)
        config.enabled = checked
        ConfigSystem.saveConfig()
    end
    
    -- Botão para salvar
    local saveButton = g_ui.createWidget('Button', window)
    saveButton:setText('Salvar')
    saveButton:setPosition({x = 10, y = 250})
    saveButton.onClick = function()
        ConfigSystem.saveConfig()
        window:hide()
    end
```

#### Finalização
```lua
end

function ConfigSystem.showConfigWindow()
    local window = rootWidget:getChildById('configWindow')
    if window then
        window:show()
        window:raise()
        window:focus()
    end
end

function ConfigSystem.terminate()
    ConfigSystem.saveConfig()
end
```

**O que aprender**:
- Persistência de dados
- Manipulação de arquivos
- Interface de configuração
- Uso de CheckBox e outros controles

---

## 🚀 **NÍVEL AVANÇADO - SISTEMAS COMPLEXOS**

### **📝 Exemplo 5: Sistema de Eventos**

**Objetivo**: Criar um sistema que reage a eventos do jogo.

#### Inicialização e Configuração
```lua
-- ========================================
-- SISTEMA DE EVENTOS
-- ========================================
-- Demonstra como conectar e reagir a eventos
-- Mostra sistema de callbacks avançado

EventSystem = {}

-- Lista de eventos registrados
local registeredEvents = {}
local eventWindow

function EventSystem.init()
    -- Cria janela para mostrar eventos
    EventSystem.createEventWindow()
    
    -- Registra eventos importantes
    EventSystem.registerGameEvents()
    
    -- Adiciona botão no menu
    local button = modules.client_topmenu.addLeftButton(
        'eventButton',
        'Eventos',
        '/images/topbuttons/logout'
    )
    button.onClick = function()
        EventSystem.showEventWindow()
    end
```

#### Funcionalidade 1
```lua
end

function EventSystem.registerGameEvents()
    -- Evento de login
    connect(g_game, { onLoginAdvice = EventSystem.onLogin })
    connect(g_game, { onLogout = EventSystem.onLogout })
    
    -- Evento de morte
    connect(g_game, { onDeath = EventSystem.onDeath })
    
    -- Evento de nível
    connect(g_game, { onLevelChange = EventSystem.onLevelChange })
    
    -- Evento de experiência
    connect(g_game, { onExperienceChange = EventSystem.onExperienceChange })
end

function EventSystem.onLogin()
    EventSystem.addEvent("Login", "Jogador fez login no servidor")
end

function EventSystem.onLogout()
```

#### Funcionalidade 2
```lua
    EventSystem.addEvent("Logout", "Jogador fez logout do servidor")
end

function EventSystem.onDeath()
    EventSystem.addEvent("Morte", "Jogador morreu!")
end

function EventSystem.onLevelChange(level)
    EventSystem.addEvent("Nível", "Subiu para o nível " .. level)
end

function EventSystem.onExperienceChange(exp)
    EventSystem.addEvent("Experiência", "Ganhou " .. exp .. " de experiência")
end

function EventSystem.addEvent(type, message)
    -- Adiciona evento à lista
    local event = {
        type = type,
        message = message,
        time = os.date('%H:%M:%S')
    }
```

#### Funcionalidade 3
```lua
    
    table.insert(registeredEvents, event)
    
    -- Mantém apenas os últimos 50 eventos
    if #registeredEvents > 50 then
        table.remove(registeredEvents, 1)
    end
    
    -- Atualiza interface
    EventSystem.updateEventWindow()
    
    -- Exibe no console
    print(string.format("[%s] %s: %s", event.time, event.type, event.message))
end

function EventSystem.createEventWindow()
    eventWindow = g_ui.createWidget('MainWindow', rootWidget)
    eventWindow:setId('eventWindow')
    eventWindow:setText('Sistema de Eventos')
    eventWindow:setSize({width = 500, height = 400})
    eventWindow:centerIn('parent')
    eventWindow:hide()
    
    -- Lista de eventos
    local eventList = g_ui.createWidget('TextList', eventWindow)
    eventList:setId('eventList')
    eventList:setPosition({x = 10, y = 30})
    eventList:setSize({width = 480, height = 320})
    
    -- Botão para limpar
    local clearButton = g_ui.createWidget('Button', eventWindow)
    clearButton:setText('Limpar Eventos')
    clearButton:setPosition({x = 10, y = 360})
    clearButton.onClick = function()
        registeredEvents = {}
        EventSystem.updateEventWindow()
    end
```

#### Funcionalidade 4
```lua
end

function EventSystem.updateEventWindow()
    local eventList = eventWindow:getChildById('eventList')
    if eventList then
        eventList:clearChildren()
        
        -- Adiciona eventos à lista (do mais recente para o mais antigo)
        for i = #registeredEvents, 1, -1 do
            local event = registeredEvents[i]
            local item = g_ui.createWidget('TextListItem', eventList)
            item:setText(string.format("[%s] %s: %s", 
                event.time, event.type, event.message))
        end
    end
end

function EventSystem.showEventWindow()
    if eventWindow then
        eventWindow:show()
        eventWindow:raise()
        eventWindow:focus()
        EventSystem.updateEventWindow()
    end
```

#### Finalização
```lua
end

function EventSystem.terminate()
    -- Desconecta todos os eventos
    disconnect(g_game, { onLoginAdvice = EventSystem.onLogin })
    disconnect(g_game, { onLogout = EventSystem.onLogout })
    disconnect(g_game, { onDeath = EventSystem.onDeath })
    disconnect(g_game, { onLevelChange = EventSystem.onLevelChange })
    disconnect(g_game, { onExperienceChange = EventSystem.onExperienceChange })
    
    if eventWindow then
        eventWindow:destroy()
    end
end
```

**O que aprender**:
- Sistema de eventos do OTClient
- Como conectar/desconectar eventos
- Interface com listas dinâmicas
- Gerenciamento de dados em tempo real

---

## 🎯 **PROJETOS PRÁTICOS**

### **📝 Projeto 1: Sistema de Notificações**

**Objetivo**: Criar um sistema completo de notificações.

#### Inicialização e Configuração
```lua
-- ========================================
-- SISTEMA DE NOTIFICAÇÕES
-- ========================================
-- Projeto completo com múltiplas funcionalidades
-- Demonstra integração de conceitos avançados

NotificationSystem = {}

-- Configurações
local config = {
    enabled = true,
    soundEnabled = true,
    autoHide = true,
    maxNotifications = 5,
    displayTime = 5000
}

-- Lista de notificações ativas
local activeNotifications = {}
local notificationWindow

function NotificationSystem.init()
```

#### Funcionalidade 1
```lua
    -- Carrega configurações
    NotificationSystem.loadConfig()
    
    -- Cria janela de notificações
    NotificationSystem.createNotificationWindow()
    
    -- Registra eventos
    NotificationSystem.registerEvents()
    
    -- Adiciona botão no menu
    local button = modules.client_topmenu.addLeftButton(
        'notificationButton',
        'Notificações',
        '/images/topbuttons/logout'
    )
    button.onClick = function()
        NotificationSystem.showNotificationWindow()
    end
    
    print("Sistema de Notificações iniciado!")
end
```

#### Funcionalidade 2
```lua

function NotificationSystem.createNotificationWindow()
    notificationWindow = g_ui.createWidget('MainWindow', rootWidget)
    notificationWindow:setId('notificationWindow')
    notificationWindow:setText('Sistema de Notificações')
    notificationWindow:setSize({width = 400, height = 300})
    notificationWindow:centerIn('parent')
    notificationWindow:hide()
    
    -- Lista de notificações
    local notificationList = g_ui.createWidget('TextList', notificationWindow)
    notificationList:setId('notificationList')
    notificationList:setPosition({x = 10, y = 30})
    notificationList:setSize({width = 380, height = 220})
    
    -- Controles
    local enabledCheck = g_ui.createWidget('CheckBox', notificationWindow)
    enabledCheck:setText('Habilitado')
    enabledCheck:setPosition({x = 10, y = 260})
    enabledCheck:setChecked(config.enabled)
    enabledCheck.onCheckChange = function(widget, checked)
        config.enabled = checked
        NotificationSystem.saveConfig()
    end
```

#### Funcionalidade 3
```lua
end

function NotificationSystem.registerEvents()
    -- Eventos de jogo
    connect(g_game, { onLoginAdvice = function() 
        NotificationSystem.showNotification("Sistema", "Login realizado com sucesso!", "success") 
    end})
    
    connect(g_game, { onDeath = function() 
        NotificationSystem.showNotification("Morte", "Você morreu!", "error") 
    end})
    
    connect(g_game, { onLevelChange = function(level) 
        NotificationSystem.showNotification("Nível", "Parabéns! Nível " .. level, "success") 
    end})
end

function NotificationSystem.showNotification(title, message, type)
    if not config.enabled then
        return
    end
```

#### Funcionalidade 4
```lua
    
    -- Cria notificação
    local notification = {
        id = os.time() .. math.random(1000, 9999),
        title = title,
        message = message,
        type = type or "info",
        time = os.date('%H:%M:%S')
    }
    
    -- Adiciona à lista
    table.insert(activeNotifications, notification)
    
    -- Remove notificações antigas
    while #activeNotifications > config.maxNotifications do
        table.remove(activeNotifications, 1)
    end
    
    -- Atualiza interface
    NotificationSystem.updateNotificationWindow()
    
    -- Exibe notificação temporária
    NotificationSystem.showTemporaryNotification(notification)
    
    -- Reproduz som se habilitado
    if config.soundEnabled then
        NotificationSystem.playNotificationSound(type)
    end
```

#### Funcionalidade 5
```lua
end

function NotificationSystem.showTemporaryNotification(notification)
    -- Cria notificação temporária na tela
    local tempWindow = g_ui.createWidget('MainWindow', rootWidget)
    tempWindow:setId('tempNotification_' .. notification.id)
    tempWindow:setText(notification.title)
    tempWindow:setSize({width = 300, height = 80})
    tempWindow:setPosition({x = 10, y = 10})
    
    local messageLabel = g_ui.createWidget('Label', tempWindow)
    messageLabel:setText(notification.message)
    messageLabel:setPosition({x = 10, y = 30})
    
    -- Remove após tempo definido
    scheduleEvent(function()
        tempWindow:destroy()
    end, config.displayTime)
end

function NotificationSystem.updateNotificationWindow()
```

#### Funcionalidade 6
```lua
    local notificationList = notificationWindow:getChildById('notificationList')
    if notificationList then
        notificationList:clearChildren()
        
        for i = #activeNotifications, 1, -1 do
            local notification = activeNotifications[i]
            local item = g_ui.createWidget('TextListItem', notificationList)
            item:setText(string.format("[%s] %s: %s", 
                notification.time, notification.title, notification.message))
        end
    end
end

function NotificationSystem.playNotificationSound(type)
    -- Reproduz som baseado no tipo de notificação
    local soundFile = "/sounds/notification.ogg"
    
    if type == "error" then
        soundFile = "/sounds/error.ogg"
    elseif type == "success" then
        soundFile = "/sounds/success.ogg"
    end
```

#### Funcionalidade 7
```lua
    
    -- Reproduz som (implementação simplificada)
    print("Reproduzindo som: " .. soundFile)
end

function NotificationSystem.showNotificationWindow()
    if notificationWindow then
        notificationWindow:show()
        notificationWindow:raise()
        notificationWindow:focus()
        NotificationSystem.updateNotificationWindow()
    end
end

function NotificationSystem.loadConfig()
    -- Carrega configurações (implementação simplificada)
    print("Configurações carregadas")
end

function NotificationSystem.saveConfig()
    -- Salva configurações (implementação simplificada)
    print("Configurações salvas")
end
```

#### Finalização
```lua

function NotificationSystem.terminate()
    -- Limpa notificações temporárias
    for _, notification in ipairs(activeNotifications) do
        local tempWindow = rootWidget:getChildById('tempNotification_' .. notification.id)
        if tempWindow then
            tempWindow:destroy()
        end
    end
    
    -- Desconecta eventos
    disconnect(g_game, { onLoginAdvice = NotificationSystem.showNotification })
    disconnect(g_game, { onDeath = NotificationSystem.showNotification })
    disconnect(g_game, { onLevelChange = NotificationSystem.showNotification })
    
    if notificationWindow then
        notificationWindow:destroy()
    end
    
    print("Sistema de Notificações finalizado!")
end
```

**O que aprender**:
- Sistema completo e integrado
- Gerenciamento de múltiplas funcionalidades
- Interface avançada
- Integração com eventos do jogo

---

## 📚 **PRÓXIMOS PASSOS**

### **🎯 Para Continuar Aprendendo**

1. **Explore a Documentação**: Leia os guias completos na wiki
2. **Experimente**: Modifique os exemplos e veja o que acontece
3. **Crie Seus Próprios Módulos**: Use os exemplos como base
4. **Participe da Comunidade**: Compartilhe seus projetos

### **🔗 Links Úteis**

- [[Guia_Inicio_Rapido|Guia de Início Rápido]]
- [[Module_Development_Guide|Guia Completo de Desenvolvimento]]
- [[Troubleshooting_Comum|Solução de Problemas]]
- [[Glossario_Tecnico|Glossário Técnico]]

---

> [!success] **PRONTO PARA COMEÇAR!**
> Agora você tem uma base sólida para desenvolver módulos OTClient. Comece com os exemplos básicos e evolua gradualmente para projetos mais complexos. 
## 🔗 **Links Automáticos**

> [!info] **Links Gerados Automaticamente**
> Estes links foram criados automaticamente pelo sistema de linkagem da categoria **UI_Systems**

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]
- [[../maps/styles_index|Índice de Estilos]]
- [[../maps/search_index|Busca por UI Systems]]

### **🧭 Navegação**
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]
- [[../maps/category_indices|Índices por Categoria]]
- [[../maps/relationships|Relacionamentos]]

### **📊 Métricas da Categoria**
- **Categoria**: UI_Systems
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

