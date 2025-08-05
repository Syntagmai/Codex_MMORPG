# Boas Práticas de Desenvolvimento - OTClient

Este guia apresenta as melhores práticas para desenvolvimento no OTClient, cobrindo desde organização de código até otimização de performance e padrões de arquitetura.

## 📋 Índice

1. [Filosofia de Desenvolvimento](#filosofia-de-desenvolvimento)
2. [Organização de Código](#organização-de-código)
3. [Padrões de Arquitetura](#padrões-de-arquitetura)
4. [Performance e Otimização](#performance-e-otimização)
5. [Gerenciamento de Memória](#gerenciamento-de-memória)
6. [Tratamento de Erros](#tratamento-de-erros)
7. [Debugging e Profiling](#debugging-e-profiling)
8. [Segurança](#segurança)
9. [Documentação](#documentação)
10. [Testes e Validação](#testes-e-validação)
11. [Colaboração e Versionamento](#colaboração-e-versionamento)
12. [Deployment e Distribuição](#deployment-e-distribuição)

## 💡 Filosofia de Desenvolvimento

### 🎯 **Princípios Fundamentais**

```lua
-- ✅ PRINCÍPIO 1: KISS (Keep It Simple, Stupid)
    --  ✅ PRINCÍPIO 1: KISS (Keep It Simple, Stupid) (traduzido)
-- Preferir soluções simples e diretas

-- ❌ Complexo desnecessariamente
    --  ❌ Complexo desnecessariamente (traduzido)
function calculateDamageComplex(attacker, defender, spell)
    -- Função: calculateDamageComplex
    local baseFormula = (attacker:getLevel() * 2 + attacker:getMagicLevel() * 3) 
    local complexModifier = math.sin(attacker:getExperience() / 1000) * 
                           math.cos(defender:getHealth() / 100)
    local damage = baseFormula * complexModifier * spell.power
    return math.floor(damage * (1 + math.random(-20, 20) / 100))
end

-- ✅ Simples e claro
    --  ✅ Simples e claro (traduzido)
function calculateDamage(attacker, defender, spell)
    -- Função: calculateDamage
    local baseDamage = spell.minDamage + math.random(0, spell.maxDamage - spell.minDamage)
    local levelBonus = attacker:getLevel() * 0.5
    local magicBonus = attacker:getMagicLevel() * 2
    
    return math.floor(baseDamage + levelBonus + magicBonus)
end
```

#### Nível Basic
```lua
-- ✅ PRINCÍPIO 2: DRY (Don't Repeat Yourself)
-- Evitar duplicação de código

-- ❌ Código duplicado
function createWarriorInterface()
    local window = g_ui.createWidget('MainWindow', rootWidget)
    window:setSize(300, 200)
    window:centerIn('parent')
    window:setText('Warrior Stats')
    -- ... resto da configuração
end

function createMageInterface()
    local window = g_ui.createWidget('MainWindow', rootWidget)
    window:setSize(300, 200)
    window:centerIn('parent')
    window:setText('Mage Stats')
    -- ... resto da configuração
end

-- ✅ Função reutilizável
function createStatsInterface(className)
    local window = g_ui.createWidget('MainWindow', rootWidget)
    window:setSize(300, 200)
    window:centerIn('parent')
    window:setText(className .. ' Stats')
    
    return window
end

local warriorWindow = createStatsInterface('Warrior')
local mageWindow = createStatsInterface('Mage')
```

#### Nível Intermediate
```lua
-- ✅ PRINCÍPIO 2: DRY (Don't Repeat Yourself)
-- Evitar duplicação de código

-- ❌ Código duplicado
function createWarriorInterface()
    local window = g_ui.createWidget('MainWindow', rootWidget)
    window:setSize(300, 200)
    window:centerIn('parent')
    window:setText('Warrior Stats')
    -- ... resto da configuração
end

function createMageInterface()
    local window = g_ui.createWidget('MainWindow', rootWidget)
    window:setSize(300, 200)
    window:centerIn('parent')
    window:setText('Mage Stats')
    -- ... resto da configuração
end

-- ✅ Função reutilizável
function createStatsInterface(className)
    local window = g_ui.createWidget('MainWindow', rootWidget)
    window:setSize(300, 200)
    window:centerIn('parent')
    window:setText(className .. ' Stats')
    
    return window
end

local warriorWindow = createStatsInterface('Warrior')
local mageWindow = createStatsInterface('Mage')
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
-- ✅ PRINCÍPIO 2: DRY (Don't Repeat Yourself)
-- Evitar duplicação de código

-- ❌ Código duplicado
function createWarriorInterface()
    local window = g_ui.createWidget('MainWindow', rootWidget)
    window:setSize(300, 200)
    window:centerIn('parent')
    window:setText('Warrior Stats')
    -- ... resto da configuração
end

function createMageInterface()
    local window = g_ui.createWidget('MainWindow', rootWidget)
    window:setSize(300, 200)
    window:centerIn('parent')
    window:setText('Mage Stats')
    -- ... resto da configuração
end

-- ✅ Função reutilizável
function createStatsInterface(className)
    local window = g_ui.createWidget('MainWindow', rootWidget)
    window:setSize(300, 200)
    window:centerIn('parent')
    window:setText(className .. ' Stats')
    
    return window
end

local warriorWindow = createStatsInterface('Warrior')
local mageWindow = createStatsInterface('Mage')
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

#### Inicialização e Configuração
```lua
-- ✅ PRINCÍPIO 3: SOLID
-- Single Responsibility: Cada função tem uma responsabilidade

-- ❌ Função com muitas responsabilidades
function handlePlayerAction(action, player, target)
    -- Validação
    if not player then return false end
    if action == 'attack' and not target then return false end
    
    -- Logging
    print('Player ' .. player:getName() .. ' performed ' .. action)
    
    -- Lógica de negócio
    if action == 'attack' then
        local damage = calculateDamage(player, target)
        target:removeHealth(damage)
    elseif action == 'heal' then
        player:addHealth(50)
    end
    
    -- UI Update
    updateHealthBars()
    showCombatEffect(target)
    
    -- Networking
    sendActionToServer(action, player, target)
end
```

#### Funcionalidade 1
```lua

-- ✅ Separação de responsabilidades
function validateAction(action, player, target)
    if not player then return false, "Player inválido" end
    if action == 'attack' and not target then return false, "Target necessário" end
    return true, nil
end

function logAction(action, player)
    print('Player ' .. player:getName() .. ' performed ' .. action)
end

function executeAction(action, player, target)
    if action == 'attack' then
        return combatSystem.attack(player, target)
    elseif action == 'heal' then
        return healingSystem.heal(player, 50)
    end
end

function handlePlayerAction(action, player, target)
```

#### Finalização
```lua
    local valid, error = validateAction(action, player, target)
    if not valid then return false, error end
    
    logAction(action, player)
    local result = executeAction(action, player, target)
    
    if result.success then
        uiManager.updateCombatDisplay(result)
        networkManager.sendAction(action, player, target)
    end
    
    return result.success
end
```

## 📁 Organização de Código

### 🏗️ **Estrutura de Módulos**

```
my_module/
├── init.lua                 # Ponto de entrada
├── core/                    # Lógica central
│   ├── manager.lua         # Gerenciador principal
│   ├── config.lua          # Configurações
│   └── events.lua          # Sistema de eventos
├── ui/                     # Interface do usuário
│   ├── windows/            # Janelas
│   │   ├── main.lua
│   │   └── settings.lua
│   ├── widgets/            # Widgets customizados
│   └── styles/             # Estilos .otui
├── data/                   # Dados e assets
│   ├── constants.lua       # Constantes
│   ├── defaults.lua        # Valores padrão
│   └── templates.lua       # Templates
├── utils/                  # Utilitários
│   ├── math.lua           # Funções matemáticas
│   ├── string.lua         # Manipulação de strings
│   └── table.lua          # Operações com tabelas
├── api/                    # API pública
│   └── public.lua         # Funções expostas
└── tests/                  # Testes (opcional)
    ├── unit/
    └── integration/
```

### 📝 **Template de Módulo Bem Estruturado**

#### Inicialização e Configuração
```lua
-- modules/my_module/init.lua
local MyModule = {}

-- Importar submódulos
local Manager = dofile('core/manager.lua')
local Config = dofile('core/config.lua')
local Events = dofile('core/events.lua')
local UI = dofile('ui/main.lua')
local Utils = dofile('utils/index.lua')

-- Estado interno
local initialized = false
local moduleData = {}

-- Função de inicialização
function MyModule.init()
    if initialized then
        Utils.log('MyModule', 'Módulo já foi inicializado', 'WARN')
        return false
    end
    
    -- Carregar configurações
    Config.load()
    
    -- Inicializar componentes na ordem correta
    local initOrder = {
        { name = 'Manager', init = Manager.init },
        { name = 'Events', init = Events.init },
        { name = 'UI', init = UI.init }
    }
```

#### Funcionalidade 1
```lua
    
    for _, component in ipairs(initOrder) do
        local success, error = pcall(component.init)
        if not success then
            Utils.log('MyModule', 'Falha ao inicializar ' .. component.name .. ': ' .. error, 'ERROR')
            MyModule.terminate()  -- Cleanup parcial
            return false
        end
    end
    
    initialized = true
    Utils.log('MyModule', 'Módulo inicializado com sucesso', 'INFO')
    return true
end

-- Função de finalização
function MyModule.terminate()
    if not initialized then return end
    
    -- Finalizar na ordem inversa
    pcall(UI.terminate)
    pcall(Events.terminate)
    pcall(Manager.terminate)
    
    -- Salvar configurações
    Config.save()
    
    initialized = false
    Utils.log('MyModule', 'Módulo finalizado', 'INFO')
end
```

#### Finalização
```lua

-- API pública
function MyModule.isInitialized()
    return initialized
end

function MyModule.getVersion()
    return "1.0.0"
end

-- Exportar para escopo global
_G.MyModule = MyModule
return MyModule
```

### 🔧 **Sistema de Configuração Modular**

#### Inicialização e Configuração
```lua
-- modules/my_module/core/config.lua
local Config = {}

-- Configurações padrão
local defaults = {
    ui = {
        showAtStartup = true,
        windowPosition = { x = 100, y = 100 },
        windowSize = { width = 400, height = 300 },
        theme = 'dark'
    },
    gameplay = {
        autoSave = true,
        saveInterval = 30000,
        maxHistory = 100
    },
    advanced = {
        debugMode = false,
        logLevel = 'INFO',
        maxMemoryUsage = 50 * 1024 * 1024  -- 50MB
    }
```

#### Funcionalidade 1
```lua
}

-- Estado atual
local current = {}
local configFile = 'mymodule_config.otml'

function Config.load()
    -- Começar com padrões
    current = table.deepcopy(defaults)
    
    -- Carregar configurações salvas
    local saved = g_settings.getNode('mymodule-config')
    if saved then
        Config.merge(current, saved)
    end
    
    -- Validar configurações
    Config.validate()
end

function Config.save()
```

#### Funcionalidade 2
```lua
    g_settings.setNode('mymodule-config', current)
    g_settings.save()
end

function Config.get(path)
    local keys = string.split(path, '.')
    local value = current
    
    for _, key in ipairs(keys) do
        if type(value) ~= 'table' or value[key] == nil then
            return nil
        end
        value = value[key]
    end
    
    return value
end

function Config.set(path, value)
    local keys = string.split(path, '.')
    local current_ref = current
    
    -- Navegar até o último nível
    for i = 1, #keys - 1 do
        local key = keys[i]
        if type(current_ref[key]) ~= 'table' then
            current_ref[key] = {}
        end
```

#### Funcionalidade 3
```lua
        current_ref = current_ref[key]
    end
    
    -- Definir valor
    current_ref[keys[#keys]] = value
    
    -- Auto-save se configurado
    if Config.get('gameplay.autoSave') then
        Config.save()
    end
end

function Config.merge(target, source)
    for key, value in pairs(source) do
        if type(value) == 'table' and type(target[key]) == 'table' then
            Config.merge(target[key], value)
        else
            target[key] = value
        end
    end
end
```

#### Funcionalidade 4
```lua

function Config.validate()
    -- Validar tipos e ranges
    local validators = {
        ['ui.windowSize.width'] = function(v) return type(v) == 'number' and v >= 200 and v <= 2000 end,
        ['ui.windowSize.height'] = function(v) return type(v) == 'number' and v >= 150 and v <= 1500 end,
        ['gameplay.saveInterval'] = function(v) return type(v) == 'number' and v >= 1000 and v <= 300000 end,
        ['gameplay.maxHistory'] = function(v) return type(v) == 'number' and v >= 10 and v <= 1000 end
    }
    
    for path, validator in pairs(validators) do
        local value = Config.get(path)
        if value ~= nil and not validator(value) then
            print('Config: Valor inválido para ' .. path .. ', usando padrão')
            -- Restaurar valor padrão
            local defaultValue = Config.getDefault(path)
            if defaultValue ~= nil then
                Config.set(path, defaultValue)
            end
        end
    end
```

#### Finalização
```lua
end

function Config.getDefault(path)
    local keys = string.split(path, '.')
    local value = defaults
    
    for _, key in ipairs(keys) do
        if type(value) ~= 'table' or value[key] == nil then
            return nil
        end
        value = value[key]
    end
    
    return value
end

function Config.reset()
    current = table.deepcopy(defaults)
    Config.save()
end

return Config
```

## 🏛️ Padrões de Arquitetura

### 🎭 **Padrão Observer para Eventos**

#### Inicialização e Configuração
```lua
-- modules/my_module/core/events.lua
local Events = {}

-- Registry de eventos
local listeners = {}
local eventQueue = {}
local processing = false

function Events.init()
    -- Limpar estado anterior
    listeners = {}
    eventQueue = {}
    processing = false
end

function Events.terminate()
    Events.removeAllListeners()
    eventQueue = {}
end

-- Registrar listener
function Events.on(eventName, callback, priority)
```

#### Funcionalidade 1
```lua
    priority = priority or 0
    
    if not listeners[eventName] then
        listeners[eventName] = {}
    end
    
    table.insert(listeners[eventName], {
        callback = callback,
        priority = priority
    })
    
    -- Ordenar por prioridade (maior primeiro)
    table.sort(listeners[eventName], function(a, b)
        return a.priority > b.priority
    end)
end

-- Remover listener específico
function Events.off(eventName, callback)
    if not listeners[eventName] then return end
    
    for i, listener in ipairs(listeners[eventName]) do
        if listener.callback == callback then
            table.remove(listeners[eventName], i)
            break
        end
```

#### Funcionalidade 2
```lua
    end
end

-- Remover todos os listeners de um evento
function Events.removeAllListeners(eventName)
    if eventName then
        listeners[eventName] = {}
    else
        listeners = {}
    end
end

-- Emitir evento imediatamente
function Events.emit(eventName, ...)
    if not listeners[eventName] then return end
    
    local args = {...}
    local results = {}
    
    for _, listener in ipairs(listeners[eventName]) do
        local success, result = pcall(listener.callback, table.unpack(args))
        if success then
            table.insert(results, result)
        else
            print('Erro no listener do evento ' .. eventName .. ': ' .. result)
        end
```

#### Funcionalidade 3
```lua
    end
    
    return results
end

-- Emitir evento na próxima iteração
function Events.emitAsync(eventName, ...)
    table.insert(eventQueue, {
        name = eventName,
        args = {...},
        timestamp = g_clock.millis()
    })
    
    -- Processar fila se não estiver processando
    if not processing then
        scheduleEvent(Events.processQueue, 1)
    end
end

-- Processar fila de eventos
function Events.processQueue()
```

#### Funcionalidade 4
```lua
    if processing then return end
    processing = true
    
    local startTime = g_clock.millis()
    local maxProcessingTime = 16  -- 16ms (60 FPS)
    
    while #eventQueue > 0 and (g_clock.millis() - startTime) < maxProcessingTime do
        local event = table.remove(eventQueue, 1)
        Events.emit(event.name, table.unpack(event.args))
    end
    
    processing = false
    
    -- Se ainda há eventos, continuar no próximo frame
    if #eventQueue > 0 then
        scheduleEvent(Events.processQueue, 1)
    end
end

-- API de conveniência
function Events.once(eventName, callback)
```

#### Funcionalidade 5
```lua
    local function onceCallback(...)
        Events.off(eventName, onceCallback)
        return callback(...)
    end
    Events.on(eventName, onceCallback)
end

-- Criar namespace de eventos
function Events.createNamespace(namespace)
    return {
        on = function(event, callback, priority)
            Events.on(namespace .. '.' .. event, callback, priority)
        end,
        off = function(event, callback)
            Events.off(namespace .. '.' .. event, callback)
        end,
        emit = function(event, ...)
            return Events.emit(namespace .. '.' .. event, ...)
        end,
        emitAsync = function(event, ...)
            Events.emitAsync(namespace .. '.' .. event, ...)
        end
```

#### Finalização
```lua
    }
end

return Events
```

### 🏭 **Padrão Factory para UI**

#### Inicialização e Configuração
```lua
-- modules/my_module/ui/factory.lua
local UIFactory = {}

-- Registry de widgets
local widgetTypes = {}
local instances = {}

-- Registrar tipo de widget
function UIFactory.registerWidget(typeName, config)
    widgetTypes[typeName] = {
        baseClass = config.baseClass or 'UIWidget',
        defaultStyle = config.defaultStyle or {},
        defaultSize = config.defaultSize or { width = 100, height = 30 },
        events = config.events or {},
        validator = config.validator,
        onCreate = config.onCreate,
        onDestroy = config.onDestroy
    }
end

-- Criar widget
function UIFactory.create(typeName, parent, config)
```

#### Funcionalidade 1
```lua
    config = config or {}
    local widgetConfig = widgetTypes[typeName]
    
    if not widgetConfig then
        error('Tipo de widget desconhecido: ' .. typeName)
    end
    
    -- Validar configuração se houver validator
    if widgetConfig.validator and not widgetConfig.validator(config) then
        error('Configuração inválida para widget ' .. typeName)
    end
    
    -- Criar widget base
    local widget = g_ui.createWidget(widgetConfig.baseClass, parent)
    
    -- Aplicar configurações padrão
    widget:setSize(widgetConfig.defaultSize)
    
    -- Aplicar estilo padrão
    for property, value in pairs(widgetConfig.defaultStyle) do
        if widget[property] then
            widget[property](widget, value)
        end
```

#### Funcionalidade 2
```lua
    end
    
    -- Aplicar configurações customizadas
    for property, value in pairs(config) do
        if property ~= 'events' and widget[property] then
            widget[property](widget, value)
        end
    end
    
    -- Configurar eventos
    local events = table.merge(widgetConfig.events, config.events or {})
    for eventName, callback in pairs(events) do
        widget[eventName] = callback
    end
    
    -- Callback de criação
    if widgetConfig.onCreate then
        widgetConfig.onCreate(widget, config)
    end
    
    -- Registrar instância
    local instanceId = tostring(widget)
    instances[instanceId] = {
        widget = widget,
        type = typeName,
        config = widgetConfig
    }
```

#### Funcionalidade 3
```lua
    
    -- Hook de destruição
    local originalDestroy = widget.destroy
    widget.destroy = function(self)
        UIFactory.onDestroy(instanceId)
        originalDestroy(self)
    end
    
    return widget
end

function UIFactory.onDestroy(instanceId)
    local instance = instances[instanceId]
    if instance and instance.config.onDestroy then
        instance.config.onDestroy(instance.widget)
    end
    instances[instanceId] = nil
end

-- Widgets pré-definidos
function UIFactory.setupDefaultWidgets()
```

#### Funcionalidade 4
```lua
    -- Botão estilizado
    UIFactory.registerWidget('StyledButton', {
        baseClass = 'Button',
        defaultStyle = {
            setFont = 'verdana-11px-rounded',
            setBackgroundColor = '#3498db',
            setColor = '#ffffff'
        },
        defaultSize = { width = 100, height = 30 },
        events = {
            onHoverChange = function(widget, hovered)
                if hovered then
                    widget:setBackgroundColor('#2980b9')
                else
                    widget:setBackgroundColor('#3498db')
                end
            end
        }
    })
    
    -- Janela com título
    UIFactory.registerWidget('TitledWindow', {
        baseClass = 'MainWindow',
        defaultSize = { width = 400, height = 300 },
        onCreate = function(widget, config)
            widget:setText(config.title or 'Window')
            if config.centerInParent then
                widget:centerIn('parent')
            end
```

#### Funcionalidade 5
```lua
        end,
        validator = function(config)
            return type(config.title) == 'string'
        end
    })
    
    -- Painel de estatísticas
    UIFactory.registerWidget('StatsPanel', {
        baseClass = 'Panel',
        defaultStyle = {
            setBackgroundColor = '#2c3e50',
            setBorderWidth = 1,
            setBorderColor = '#34495e'
        },
        defaultSize = { width = 200, height = 150 },
        onCreate = function(widget, config)
            widget.stats = {}
            widget.labels = {}
            
            -- Método para adicionar estatística
            widget.addStat = function(self, name, value)
                self.stats[name] = value
                UIFactory.updateStatsDisplay(self)
            end
```

#### Funcionalidade 6
```lua
            
            -- Método para atualizar estatística
            widget.updateStat = function(self, name, value)
                if self.stats[name] ~= nil then
                    self.stats[name] = value
                    UIFactory.updateStatsDisplay(self)
                end
            end
        end
    })
end

function UIFactory.updateStatsDisplay(statsPanel)
    -- Limpar labels existentes
    for _, label in pairs(statsPanel.labels) do
        label:destroy()
    end
    statsPanel.labels = {}
    
    -- Criar labels para cada estatística
    local y = 10
    for name, value in pairs(statsPanel.stats) do
        local label = g_ui.createWidget('Label', statsPanel)
        label:setText(name .. ': ' .. tostring(value))
        label:setPosition({ x = 10, y = y })
        label:setFont('verdana-9px-rounded')
        label:setColor('#ecf0f1')
        
        statsPanel.labels[name] = label
        y = y + 20
    end
```

#### Finalização
```lua
end

return UIFactory
```

### 🎮 **Padrão State Machine para Game Logic**

#### Inicialização e Configuração
```lua
-- modules/my_module/core/statemachine.lua
local StateMachine = {}
StateMachine.__index = StateMachine

function StateMachine.new(initialState)
    local sm = {
        currentState = initialState,
        states = {},
        transitions = {},
        context = {},
        listeners = {}
    }
    setmetatable(sm, StateMachine)
    return sm
end

-- Adicionar estado
function StateMachine:addState(name, config)
    self.states[name] = {
        onEnter = config.onEnter,
        onExit = config.onExit,
        onUpdate = config.onUpdate,
        data = config.data or {}
    }
```

#### Funcionalidade 1
```lua
end

-- Adicionar transição
function StateMachine:addTransition(from, to, condition, callback)
    if not self.transitions[from] then
        self.transitions[from] = {}
    end
    
    table.insert(self.transitions[from], {
        to = to,
        condition = condition,
        callback = callback
    })
end

-- Verificar se pode transicionar
function StateMachine:canTransition(to)
    local transitions = self.transitions[self.currentState]
    if not transitions then return false end
    
    for _, transition in ipairs(transitions) do
        if transition.to == to then
            if not transition.condition or transition.condition(self.context) then
                return true
            end
```

#### Funcionalidade 2
```lua
        end
    end
    
    return false
end

-- Executar transição
function StateMachine:transition(to)
    if not self:canTransition(to) then
        return false, 'Transição inválida: ' .. self.currentState .. ' -> ' .. to
    end
    
    local fromState = self.currentState
    local toState = to
    
    -- Callback de saída do estado atual
    if self.states[fromState] and self.states[fromState].onExit then
        self.states[fromState].onExit(self.context)
    end
    
    -- Encontrar e executar callback da transição
    local transitions = self.transitions[fromState]
    for _, transition in ipairs(transitions) do
        if transition.to == toState then
            if transition.callback then
                transition.callback(self.context, fromState, toState)
            end
```

#### Funcionalidade 3
```lua
            break
        end
    end
    
    -- Mudar estado
    self.currentState = toState
    
    -- Callback de entrada do novo estado
    if self.states[toState] and self.states[toState].onEnter then
        self.states[toState].onEnter(self.context)
    end
    
    -- Notificar listeners
    self:emit('stateChanged', fromState, toState)
    
    return true
end

-- Atualizar estado atual
function StateMachine:update(deltaTime)
    local state = self.states[self.currentState]
    if state and state.onUpdate then
        state.onUpdate(self.context, deltaTime)
    end
```

#### Funcionalidade 4
```lua
    
    -- Verificar transições automáticas
    self:checkAutoTransitions()
end

-- Verificar transições automáticas
function StateMachine:checkAutoTransitions()
    local transitions = self.transitions[self.currentState]
    if not transitions then return end
    
    for _, transition in ipairs(transitions) do
        if transition.condition and transition.condition(self.context) then
            self:transition(transition.to)
            break  -- Só uma transição por update
        end
    end
end

-- Sistema de eventos simples
function StateMachine:on(event, callback)
    if not self.listeners[event] then
        self.listeners[event] = {}
    end
```

#### Funcionalidade 5
```lua
    table.insert(self.listeners[event], callback)
end

function StateMachine:emit(event, ...)
    local listeners = self.listeners[event]
    if listeners then
        for _, callback in ipairs(listeners) do
            callback(...)
        end
    end
end

-- Exemplo de uso: Sistema de Combat
function createCombatStateMachine()
    local combat = StateMachine.new('idle')
    
    -- Estados
    combat:addState('idle', {
        onEnter = function(ctx)
            print('Combat: Entrando em estado idle')
        end
```

#### Funcionalidade 6
```lua
    })
    
    combat:addState('targeting', {
        onEnter = function(ctx)
            print('Combat: Procurando alvo')
        end,
        onUpdate = function(ctx, dt)
            -- Lógica de procura de alvo
            if ctx.target then
                -- Transição automática será detectada
            end
        end
    })
    
    combat:addState('attacking', {
        onEnter = function(ctx)
            print('Combat: Iniciando ataque')
            ctx.attackTimer = 0
        end,
        onUpdate = function(ctx, dt)
            ctx.attackTimer = ctx.attackTimer + dt
            if ctx.attackTimer >= ctx.attackSpeed then
                -- Executar ataque
                ctx.attackTimer = 0
            end
```

#### Funcionalidade 7
```lua
        end,
        onExit = function(ctx)
            print('Combat: Parando ataque')
        end
    })
    
    -- Transições
    combat:addTransition('idle', 'targeting', 
        function(ctx) return ctx.wantToAttack end)
    
    combat:addTransition('targeting', 'attacking',
        function(ctx) return ctx.target ~= nil end)
    
    combat:addTransition('targeting', 'idle',
        function(ctx) return not ctx.wantToAttack end)
    
    combat:addTransition('attacking', 'idle',
        function(ctx) return not ctx.target or not ctx.wantToAttack end)
    
    return combat
end
```

#### Finalização
```lua

return StateMachine
```

## ⚡ Performance e Otimização

### 🚀 **Otimização de Loops**

#### Inicialização e Configuração
```lua
-- ❌ Loop ineficiente
function updateCreaturesSlowly()
    local creatures = g_map.getCreatures()
    for id, creature in pairs(creatures) do
        local position = creature:getPosition()
        local health = creature:getHealth()
        local maxHealth = creature:getMaxHealth()
        
        -- Cálculos desnecessários em cada frame
        local healthPercent = (health / maxHealth) * 100
        local distance = getDistanceToPlayer(position)
        
        -- Atualizar UI mesmo se não mudou
        updateCreatureDisplay(creature, healthPercent, distance)
    end
end

-- ✅ Loop otimizado
local lastUpdateTime = 0
local cachedDistances = {}
local UPDATE_INTERVAL = 100  -- ms

function updateCreaturesEfficiently()
```

#### Funcionalidade 1
```lua
    local currentTime = g_clock.millis()
    if currentTime - lastUpdateTime < UPDATE_INTERVAL then
        return  -- Skip se muito cedo
    end
    
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    local creatures = g_map.getCreatures()
    local playerPos = player:getPosition()
    
    -- Pre-calcular valores que não mudam
    local visibleCreatures = {}
    for id, creature in pairs(creatures) do
        local pos = creature:getPosition()
        local distance = math.abs(pos.x - playerPos.x) + math.abs(pos.y - playerPos.y)
        
        -- Só processar criaturas visíveis
        if distance <= 15 then
            visibleCreatures[id] = {
                creature = creature,
                distance = distance,
                needsUpdate = not cachedDistances[id] or cachedDistances[id] ~= distance
            }
```

#### Finalização
```lua
            cachedDistances[id] = distance
        end
    end
    
    -- Processar apenas criaturas que precisam de update
    for id, data in pairs(visibleCreatures) do
        if data.needsUpdate then
            updateCreatureDisplay(data.creature, data.distance)
        end
    end
    
    lastUpdateTime = currentTime
end
```

### 💾 **Pool de Objetos**

#### Inicialização e Configuração
```lua
-- Sistema de pool para widgets temporários
local WidgetPool = {}

function WidgetPool.new(widgetType, initialSize)
    local pool = {
        widgetType = widgetType,
        available = {},
        inUse = {},
        totalCreated = 0
    }
    
    -- Pré-criar widgets
    for i = 1, initialSize do
        local widget = g_ui.createWidget(widgetType, rootWidget)
        widget:hide()
        table.insert(pool.available, widget)
        pool.totalCreated = pool.totalCreated + 1
    end
    
    setmetatable(pool, WidgetPool)
    return pool
end
```

#### Funcionalidade 1
```lua

function WidgetPool:acquire()
    local widget
    
    if #self.available > 0 then
        -- Reusar widget existente
        widget = table.remove(self.available)
    else
        -- Criar novo se necessário
        widget = g_ui.createWidget(self.widgetType, rootWidget)
        self.totalCreated = self.totalCreated + 1
    end
    
    self.inUse[widget] = true
    widget:show()
    return widget
end

function WidgetPool:release(widget)
    if not self.inUse[widget] then
        return  -- Widget não pertence a este pool
    end
```

#### Funcionalidade 2
```lua
    
    -- Reset widget state
    widget:hide()
    widget:clearAnchors()
    widget:setPosition({ x = 0, y = 0 })
    widget:setText('')
    
    -- Retornar ao pool
    self.inUse[widget] = nil
    table.insert(self.available, widget)
end

function WidgetPool:getStats()
    return {
        available = #self.available,
        inUse = table.size(self.inUse),
        totalCreated = self.totalCreated
    }
end

-- Uso do pool
local damageTextPool = WidgetPool.new('Label', 10)

function showDamageText(position, damage)
```

#### Finalização
```lua
    local label = damageTextPool:acquire()
    label:setText(tostring(damage))
    label:setPosition(position)
    label:setColor('#ff0000')
    
    -- Animar e retornar ao pool
    scheduleEvent(function()
        damageTextPool:release(label)
    end, 2000)  -- 2 segundos
end
```

### 🔄 **Throttling e Debouncing**

#### Nível Basic
```lua
-- Throttle: Limitar frequência de execução
function createThrottle(func, delay)
    local lastCall = 0
    return function(...)
        local now = g_clock.millis()
        if now - lastCall >= delay then
        end
    end
end
-- Debounce: Executar apenas após período de inatividade
function createDebounce(func, delay)
    local timer = nil
    return function(...)
        local args = {...}
        if timer then
        end
        timer = scheduleEvent(function()
        end, delay)
    end
end
-- Exemplos de uso
local throttledSave = createThrottle(function()
    print('Salvando configurações...')
end, 5000)  -- Máximo uma vez a cada 5 segundos
local debouncedSearch = createDebounce(function(query)
    print('Pesquisando por:', query)
    -- Fazer pesquisa pesada
end, 300)  -- Aguardar 300ms sem input
-- Conectar a eventos
searchInput.onTextChange = function(widget, text)
end
playerDataChanged = function()
end
```

#### Nível Intermediate
```lua
-- Throttle: Limitar frequência de execução
function createThrottle(func, delay)
    local lastCall = 0
    
    return function(...)
        local now = g_clock.millis()
        if now - lastCall >= delay then
            lastCall = now
            return func(...)
        end
    end
end

-- Debounce: Executar apenas após período de inatividade
function createDebounce(func, delay)
    local timer = nil
    
    return function(...)
        local args = {...}
        
        if timer then
            removeEvent(timer)
        end
        
        timer = scheduleEvent(function()
            timer = nil
            func(table.unpack(args))
        end, delay)
    end
end

-- Exemplos de uso
local throttledSave = createThrottle(function()
    print('Salvando configurações...')
    g_settings.save()
end, 5000)  -- Máximo uma vez a cada 5 segundos

local debouncedSearch = createDebounce(function(query)
    print('Pesquisando por:', query)
    -- Fazer pesquisa pesada
end, 300)  -- Aguardar 300ms sem input

-- Conectar a eventos
searchInput.onTextChange = function(widget, text)
    debouncedSearch(text)
end

playerDataChanged = function()
    throttledSave()
end
```

#### Nível Advanced
```lua
-- Throttle: Limitar frequência de execução
function createThrottle(func, delay)
    local lastCall = 0
    
    return function(...)
        local now = g_clock.millis()
        if now - lastCall >= delay then
            lastCall = now
            return func(...)
        end
    end
end

-- Debounce: Executar apenas após período de inatividade
function createDebounce(func, delay)
    local timer = nil
    
    return function(...)
        local args = {...}
        
        if timer then
            removeEvent(timer)
        end
        
        timer = scheduleEvent(function()
            timer = nil
            func(table.unpack(args))
        end, delay)
    end
end

-- Exemplos de uso
local throttledSave = createThrottle(function()
    print('Salvando configurações...')
    g_settings.save()
end, 5000)  -- Máximo uma vez a cada 5 segundos

local debouncedSearch = createDebounce(function(query)
    print('Pesquisando por:', query)
    -- Fazer pesquisa pesada
end, 300)  -- Aguardar 300ms sem input

-- Conectar a eventos
searchInput.onTextChange = function(widget, text)
    debouncedSearch(text)
end

playerDataChanged = function()
    throttledSave()
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

## 🧠 Gerenciamento de Memória

### 🗑️ **Limpeza Automática**

#### Inicialização e Configuração
```lua
-- Sistema de gerenciamento de memória
local MemoryManager = {}

-- Registro de objetos temporários
local temporaryObjects = {}
local cleanupCallbacks = {}

function MemoryManager.registerTemporary(object, lifetime, cleanupCallback)
    local id = tostring(object)
    temporaryObjects[id] = {
        object = object,
        createdAt = g_clock.millis(),
        lifetime = lifetime,
        cleanupCallback = cleanupCallback
    }
end

function MemoryManager.cleanup()
    local currentTime = g_clock.millis()
    local cleaned = 0
    
    for id, data in pairs(temporaryObjects) do
        if currentTime - data.createdAt >= data.lifetime then
            -- Executar callback de limpeza
            if data.cleanupCallback then
                pcall(data.cleanupCallback, data.object)
            end
```

#### Funcionalidade 1
```lua
            
            -- Destruir objeto se for widget
            if data.object.destroy then
                pcall(data.object.destroy, data.object)
            end
            
            temporaryObjects[id] = nil
            cleaned = cleaned + 1
        end
    end
    
    if cleaned > 0 then
        print('MemoryManager: Limpou ' .. cleaned .. ' objetos temporários')
    end
    
    -- Forçar garbage collection se necessário
    local memoryUsage = collectgarbage('count')
    if memoryUsage > 100 * 1024 then  -- 100MB
        collectgarbage('collect')
        print('MemoryManager: Garbage collection forçado. Memória: ' .. 
              math.floor(memoryUsage) .. 'KB -> ' .. 
              math.floor(collectgarbage('count')) .. 'KB')
    end
```

#### Funcionalidade 2
```lua
end

-- Executar limpeza periodicamente
scheduleEvent(function()
    MemoryManager.cleanup()
    -- Reagendar
    scheduleEvent(arguments.callee, 30000)  -- 30 segundos
end, 30000)

-- Helper para widgets temporários
function createTemporaryWidget(widgetType, parent, lifetime)
    local widget = g_ui.createWidget(widgetType, parent)
    
    MemoryManager.registerTemporary(widget, lifetime, function(w)
        if not w:isDestroyed() then
            w:destroy()
        end
    end)
    
    return widget
end
```

#### Finalização
```lua

-- Exemplo de uso
local notification = createTemporaryWidget('Label', rootWidget, 5000)
notification:setText('Mensagem temporária')
-- Widget será automaticamente destruído após 5 segundos
```

### 📊 **Monitoramento de Performance**

#### Inicialização e Configuração
```lua
-- Sistema de profiling
local Profiler = {}
local profiles = {}
local activeProfiles = {}

function Profiler.start(name)
    activeProfiles[name] = {
        startTime = g_clock.millis(),
        startMemory = collectgarbage('count')
    }
end

function Profiler.stop(name)
    local profile = activeProfiles[name]
    if not profile then return end
    
    local endTime = g_clock.millis()
    local endMemory = collectgarbage('count')
    
    local duration = endTime - profile.startTime
    local memoryDelta = endMemory - profile.startMemory
    
    if not profiles[name] then
        profiles[name] = {
            calls = 0,
            totalTime = 0,
            maxTime = 0,
            minTime = math.huge,
            totalMemory = 0,
            maxMemory = 0
        }
```

#### Funcionalidade 1
```lua
    end
    
    local p = profiles[name]
    p.calls = p.calls + 1
    p.totalTime = p.totalTime + duration
    p.maxTime = math.max(p.maxTime, duration)
    p.minTime = math.min(p.minTime, duration)
    p.totalMemory = p.totalMemory + memoryDelta
    p.maxMemory = math.max(p.maxMemory, memoryDelta)
    
    activeProfiles[name] = nil
end

function Profiler.wrap(name, func)
    return function(...)
        Profiler.start(name)
        local results = {pcall(func, ...)}
        Profiler.stop(name)
        
        if results[1] then
            return table.unpack(results, 2)
        else
            error(results[2])
        end
```

#### Funcionalidade 2
```lua
    end
end

function Profiler.report()
    print('=== Performance Report ===')
    for name, data in pairs(profiles) do
        local avgTime = data.totalTime / data.calls
        local avgMemory = data.totalMemory / data.calls
        
        print(string.format('%s: %d calls, avg: %.2fms, max: %.2fms, mem: %.2fKB',
            name, data.calls, avgTime, data.maxTime, avgMemory))
    end
end

-- Macro para profiling automático
function profile(name, func)
    return Profiler.wrap(name, func)
end

-- Exemplo de uso
local optimizedFunction = profile('my_heavy_function', function(data)
    -- Processamento pesado aqui
    for i = 1, #data do
        -- ... processamento ...
    end
```

#### Finalização
```lua
end)

-- Relatório periódico
scheduleEvent(function()
    Profiler.report()
    scheduleEvent(arguments.callee, 60000)  -- A cada minuto
end, 60000)
```

## 🛡️ Tratamento de Erros

### 🚨 **Sistema Robusto de Error Handling**

#### Inicialização e Configuração
```lua
-- Sistema centralizado de tratamento de erros
local ErrorHandler = {}
local errorLog = {}

function ErrorHandler.init()
    -- Override da função de erro global
    local originalError = error
    error = function(message, level)
        ErrorHandler.logError(message, level or 1, debug.traceback())
        originalError(message, level)
    end
end

function ErrorHandler.safeCall(func, ...)
    local success, result = pcall(func, ...)
    
    if not success then
        ErrorHandler.logError(result, 1, debug.traceback())
        return nil, result
    end
    
    return result
end
```

#### Funcionalidade 1
```lua

function ErrorHandler.safeCallWithDefault(func, defaultValue, ...)
    local result, error = ErrorHandler.safeCall(func, ...)
    
    if result == nil then
        print('Usando valor padrão devido ao erro:', error)
        return defaultValue
    end
    
    return result
end

function ErrorHandler.logError(message, level, traceback)
    local timestamp = os.date('%Y-%m-%d %H:%M:%S')
    local errorEntry = {
        timestamp = timestamp,
        message = message,
        level = level,
        traceback = traceback,
        context = ErrorHandler.getCurrentContext()
    }
```

#### Funcionalidade 2
```lua
    
    table.insert(errorLog, errorEntry)
    
    -- Manter apenas últimos 100 erros
    if #errorLog > 100 then
        table.remove(errorLog, 1)
    end
    
    -- Log no console
    print(string.format('[ERROR][%s] %s', timestamp, message))
    
    -- Notificar se sistema disponível
    if Notifications then
        Notifications.error('Erro', message, 5000)
    end
end

function ErrorHandler.getCurrentContext()
    local context = {
        isOnline = g_game.isOnline(),
        hasPlayer = g_game.getLocalPlayer() ~= nil,
        memoryUsage = collectgarbage('count'),
        fps = g_app.getFps()
    }
```

#### Funcionalidade 3
```lua
    
    if context.hasPlayer then
        local player = g_game.getLocalPlayer()
        context.playerName = player:getName()
        context.playerLevel = player:getLevel()
        context.playerPosition = player:getPosition()
    end
    
    return context
end

function ErrorHandler.getErrorReport()
    return {
        errors = errorLog,
        totalErrors = #errorLog,
        lastError = errorLog[#errorLog]
    }
end

-- Wrappers para funções críticas
function ErrorHandler.wrapModuleFunction(moduleName, funcName, func)
```

#### Funcionalidade 4
```lua
    return function(...)
        local success, result = pcall(func, ...)
        
        if not success then
            local errorMsg = string.format('Erro em %s.%s: %s', moduleName, funcName, result)
            ErrorHandler.logError(errorMsg, 1, debug.traceback())
            
            -- Tentar recuperação se possível
            if ErrorHandler.canRecover(moduleName, funcName) then
                print('Tentando recuperação automática...')
                return ErrorHandler.attemptRecovery(moduleName, funcName, ...)
            end
            
            return nil
        end
        
        return result
    end
end

function ErrorHandler.canRecover(moduleName, funcName)
```

#### Funcionalidade 5
```lua
    -- Definir funções que podem ser recuperadas
    local recoverableFunctions = {
        ['UI.createWindow'] = true,
        ['Config.load'] = true,
        ['Network.connect'] = true
    }
    
    return recoverableFunctions[moduleName .. '.' .. funcName] or false
end

function ErrorHandler.attemptRecovery(moduleName, funcName, ...)
    -- Estratégias de recuperação específicas
    if moduleName == 'UI' and funcName == 'createWindow' then
        -- Criar janela com configurações padrão
        return g_ui.createWidget('MainWindow', rootWidget)
    elseif moduleName == 'Config' and funcName == 'load' then
        -- Carregar configurações padrão
        return ErrorHandler.loadDefaultConfig()
    end
    
    return nil
end
```

#### Finalização
```lua

-- Inicializar sistema
ErrorHandler.init()
```

### 🔄 **Validação de Dados**

#### Inicialização e Configuração
```lua
-- Sistema de validação robusto
local Validator = {}

-- Validadores básicos
local validators = {
    string = function(value, min, max)
        if type(value) ~= 'string' then
            return false, 'Deve ser uma string'
        end
        if min and #value < min then
            return false, 'Muito curto (mínimo ' .. min .. ' caracteres)'
        end
        if max and #value > max then
            return false, 'Muito longo (máximo ' .. max .. ' caracteres)'
        end
        return true
    end,
    
    number = function(value, min, max)
        if type(value) ~= 'number' then
            return false, 'Deve ser um número'
        end
```

#### Funcionalidade 1
```lua
        if min and value < min then
            return false, 'Muito baixo (mínimo ' .. min .. ')'
        end
        if max and value > max then
            return false, 'Muito alto (máximo ' .. max .. ')'
        end
        return true
    end,
    
    position = function(value)
        if type(value) ~= 'table' then
            return false, 'Posição deve ser uma tabela'
        end
        if type(value.x) ~= 'number' or type(value.y) ~= 'number' or type(value.z) ~= 'number' then
            return false, 'Posição deve ter x, y, z numéricos'
        end
        if value.x < 0 or value.x > 65535 or value.y < 0 or value.y > 65535 or value.z < 0 or value.z > 15 then
            return false, 'Coordenadas fora dos limites válidos'
        end
        return true
    end,
```

#### Funcionalidade 2
```lua
    
    color = function(value)
        if type(value) == 'string' then
            -- Validar formato hex
            if not value:match('^#[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]$') then
                return false, 'Cor deve estar no formato #RRGGBB'
            end
        elseif type(value) == 'table' then
            -- Validar formato RGB
            if type(value.r) ~= 'number' or type(value.g) ~= 'number' or type(value.b) ~= 'number' then
                return false, 'Cor RGB deve ter r, g, b numéricos'
            end
            if value.r < 0 or value.r > 255 or value.g < 0 or value.g > 255 or value.b < 0 or value.b > 255 then
                return false, 'Valores RGB devem estar entre 0 e 255'
            end
        else
            return false, 'Cor deve ser string hex ou tabela RGB'
        end
        return true
    end
}
```

#### Funcionalidade 3
```lua

function Validator.validate(schema, data)
    local errors = {}
    
    for field, rules in pairs(schema) do
        local value = data[field]
        
        -- Verificar required
        if rules.required and (value == nil or value == '') then
            table.insert(errors, field .. ' é obrigatório')
            goto continue
        end
        
        -- Se não required e valor é nil, pular outras validações
        if not rules.required and value == nil then
            goto continue
        end
        
        -- Aplicar validadores
        for _, rule in ipairs(rules) do
            local validator = validators[rule.type]
            if validator then
                local valid, message = validator(value, rule.min, rule.max)
                if not valid then
                    table.insert(errors, field .. ': ' .. message)
                end
```

#### Funcionalidade 4
```lua
            end
        end
        
        -- Validação customizada
        if rules.custom then
            local valid, message = rules.custom(value)
            if not valid then
                table.insert(errors, field .. ': ' .. message)
            end
        end
        
        ::continue::
    end
    
    return #errors == 0, errors
end

-- Exemplo de uso
local userSchema = {
    name = {
        required = true,
        { type = 'string', min = 2, max = 20 }
    },
```

#### Funcionalidade 5
```lua
    level = {
        required = true,
        { type = 'number', min = 1, max = 1000 }
    },
    position = {
        required = false,
        { type = 'position' }
    },
    favoriteColor = {
        required = false,
        { type = 'color' }
    },
    email = {
        required = false,
        custom = function(value)
            if value and not value:match('.+@.+%..+') then
                return false, 'Email inválido'
            end
            return true
        end
    }
```

#### Funcionalidade 6
```lua
}

function createUser(userData)
    local valid, errors = Validator.validate(userSchema, userData)
    
    if not valid then
        print('Dados inválidos:')
        for _, error in ipairs(errors) do
            print('  - ' .. error)
        end
        return nil
    end
    
    -- Criar usuário com dados válidos
    return {
        name = userData.name,
        level = userData.level,
        position = userData.position or { x = 0, y = 0, z = 0 },
        favoriteColor = userData.favoriteColor or '#ffffff',
        email = userData.email
    }
```

#### Finalização
```lua
end
```

Completei GUIDE-002: Criando Seu Primeiro Módulo! Este tutorial abrangente inclui:

- **5 Projetos Práticos Completos**:
  1. Contador de Cliques com persistência e estatísticas
  2. Sistema de Notificações em tempo real
  3. Monitor de Status avançado
  4. Sistema de Comandos customizados
  5. Mini-jogo integrado

- **Conceitos Avançados**:
  - Organização modular de código
  - Sistema de eventos
  - Persistência de dados
  - Interface responsiva
  - Debugging e profiling

**Progresso atualizado:**
- 13/52 stories completas (25%)
- 20% cobertura dos guias práticos
- Próxima prioridade: GUIDE-003 (Boas Práticas de Desenvolvimento)

Agora criando GUIDE-003: Boas Práticas de Desenvolvimento com foco em arquitetura, performance e qualidade de código...
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

