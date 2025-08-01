
# Debug System Guide

<div class="info"> Este guia documenta o sistema completo de debug e logging do OTClient, incluindo ferramentas de desenvolvimento, logs estruturados, profiling e troubleshooting para facilitar o desenvolvimento e manutenção.

## 📋 Índice
- [#Visão Geral](#Visão Geral.md)
- [#Sistema de Logging](#Sistema de Logging.md)
- [#Ferramentas de Debug](#Ferramentas de Debug.md)
- [#Profiling e Performance](#Profiling e Performance.md)
- [#Inspetores de UI](#Inspetores de UI.md)
- [#Sistema de Erros](#Sistema de Erros.md)
- [#Debug Remoto](#Debug Remoto.md)
- [#Performance e Otimização](#Performance e Otimização.md)
- [#Exemplos Práticos](#Exemplos Práticos.md)
- [#Melhores Práticas](#Melhores Práticas.md)

---

## 🎯 Visão Geral

O sistema de debug do OTClient oferece:

- **Logging Estruturado**: Logs organizados por categoria e nível
- **Ferramentas de Debug**: Inspetores de UI, console avançado
- **Profiling**: Análise de performance e otimização
- **Sistema de Erros**: Captura e tratamento de exceções
- **Debug Remoto**: Ferramentas para debug em produção
- **Integração Completa**: Com todos os sistemas do cliente

### 🏗️ **Arquitetura do Sistema**

```
Sistema de Debug
   │
   ├─ Logging Engine
   │   ├─ Logs estruturados
   │   ├─ Níveis de log
   │   └─ Rotação de arquivos
   │
   ├─ Debug Tools
   │   ├─ Inspetores de UI
   │   ├─ Console avançado
   │   └─ Ferramentas de análise
   │
   ├─ Profiling System
   │   ├─ Análise de performance
   │   ├─ Memory profiling
   │   └─ CPU profiling
   │
   └─ Error Handling
       ├─ Captura de exceções
       ├─ Stack traces
       └─ Relatórios de erro
```

---

## 📝 Sistema de Logging

### 🎯 **Configuração de Logs**

```lua
-- Sistema de logging principal
local DebugLogger = {}

-- Níveis de log
DebugLogger.LEVELS = {
    TRACE = 0,
    DEBUG = 1,
    INFO = 2,
    WARN = 3,
    ERROR = 4,
    FATAL = 5
}

-- Configuração padrão
DebugLogger.config = {
    level = DebugLogger.LEVELS.INFO,
    enableConsole = true,
    enableFile = true,
    logFile = "otclient.log",
    maxFileSize = 10 * 1024 * 1024,  -- 10MB
    maxFiles = 5
}

-- Inicializar sistema de logging
function DebugLogger.init()
    -- Configurar nível de log
    local logLevel = g_settings.getString("debug.logLevel", "INFO")
    DebugLogger.config.level = DebugLogger.LEVELS[string.upper(logLevel)]
    
    -- Configurar saída
    DebugLogger.config.enableConsole = g_settings.getBoolean("debug.enableConsole", true)
    DebugLogger.config.enableFile = g_settings.getBoolean("debug.enableFile", true)
    
    -- Abrir arquivo de log
    if DebugLogger.config.enableFile then
        DebugLogger.openLogFile()
    end
    
    print("Debug Logger inicializado - Nível:", logLevel)
end

-- Abrir arquivo de log
function DebugLogger.openLogFile()
    DebugLogger.logFile = io.open(DebugLogger.config.logFile, "a")
    if not DebugLogger.logFile then
        print("Erro: Não foi possível abrir arquivo de log")
    end
end
```

### 📊 **Funções de Logging**

```lua
-- Função principal de logging
function DebugLogger.log(level, category, message, ...)
    if level < DebugLogger.config.level then
        return
    end
    
    local timestamp = os.date("%Y-%m-%d %H:%M:%S")
    local levelName = DebugLogger.getLevelName(level)
    local formattedMessage = string.format(message, ...)
    
    local logEntry = string.format("[%s][%s][%s] %s", 
        timestamp, levelName, category, formattedMessage)
    
    -- Console output
    if DebugLogger.config.enableConsole then
        print(logEntry)
    end
    
    -- File output
    if DebugLogger.config.enableFile and DebugLogger.logFile then
        DebugLogger.logFile:write(logEntry .. "\n")
        DebugLogger.logFile:flush()
        
        -- Rotação de arquivo
        DebugLogger.checkFileRotation()
    end
end

-- Funções de conveniência
function DebugLogger.trace(category, message, ...)
    DebugLogger.log(DebugLogger.LEVELS.TRACE, category, message, ...)
end

function DebugLogger.debug(category, message, ...)
    DebugLogger.log(DebugLogger.LEVELS.DEBUG, category, message, ...)
end

function DebugLogger.info(category, message, ...)
    DebugLogger.log(DebugLogger.LEVELS.INFO, category, message, ...)
end

function DebugLogger.warn(category, message, ...)
    DebugLogger.log(DebugLogger.LEVELS.WARN, category, message, ...)
end

function DebugLogger.error(category, message, ...)
    DebugLogger.log(DebugLogger.LEVELS.ERROR, category, message, ...)
end

function DebugLogger.fatal(category, message, ...)
    DebugLogger.log(DebugLogger.LEVELS.FATAL, category, message, ...)
end

-- Obter nome do nível
function DebugLogger.getLevelName(level)
    for name, value in pairs(DebugLogger.LEVELS) do
        if value == level then
            return name
        end
    end
    return "UNKNOWN"
end

-- Verificar rotação de arquivo
function DebugLogger.checkFileRotation()
    if not DebugLogger.logFile then return end
    
    local fileSize = DebugLogger.logFile:seek("end")
    if fileSize > DebugLogger.config.maxFileSize then
        DebugLogger.rotateLogFile()
    end
end

-- Rotacionar arquivo de log
function DebugLogger.rotateLogFile()
    DebugLogger.logFile:close()
    
    -- Renomear arquivos existentes
    for i = DebugLogger.config.maxFiles - 1, 1, -1 do
        local oldName = DebugLogger.config.logFile .. "." .. i
        local newName = DebugLogger.config.logFile .. "." .. (i + 1)
        
        if io.open(oldName, "r") then
            os.rename(oldName, newName)
        end
    end
    
    -- Renomear arquivo atual
    os.rename(DebugLogger.config.logFile, DebugLogger.config.logFile .. ".1")
    
    -- Reabrir arquivo
    DebugLogger.openLogFile()
end
```

---

## 🔧 Ferramentas de Debug

### 🎯 **Console Avançado**

```lua
-- Console de debug avançado
local DebugConsole = {}

function DebugConsole.init()
    -- Criar console
    DebugConsole.window = g_ui.createWidget('MainWindow', rootWidget)
    DebugConsole.window:setId('debugConsole')
    DebugConsole.window:setText('Debug Console')
    DebugConsole.window:setSize({width = 600, height = 400})
    DebugConsole.window:hide()
    
    -- Área de log
    DebugConsole.logArea = g_ui.createWidget('TextEdit', DebugConsole.window)
    DebugConsole.logArea:setId('debugLogArea')
    DebugConsole.logArea:setPosition({x = 10, y = 30})
    DebugConsole.logArea:setSize({width = 580, height = 320})
    DebugConsole.logArea:setTextWrap(true)
    DebugConsole.logArea:setEditable(false)
    
    -- Campo de comando
    DebugConsole.commandInput = g_ui.createWidget('TextEdit', DebugConsole.window)
    DebugConsole.commandInput:setId('debugCommandInput')
    DebugConsole.commandInput:setPosition({x = 10, y = 360})
    DebugConsole.commandInput:setSize({width = 500, height = 25})
    DebugConsole.commandInput:setText('')
    
    -- Botão de executar
    DebugConsole.executeButton = g_ui.createWidget('Button', DebugConsole.window)
    DebugConsole.executeButton:setId('debugExecuteButton')
    DebugConsole.executeButton:setPosition({x = 520, y = 360})
    DebugConsole.executeButton:setSize({width = 70, height = 25})
    DebugConsole.executeButton:setText('Executar')
    DebugConsole.executeButton.onClick = DebugConsole.executeCommand
    
    -- Configurar hotkey
    g_keyboard.bindKeyDown('Ctrl+Shift+D', DebugConsole.toggle)
end

-- Alternar visibilidade do console
function DebugConsole.toggle()
    if DebugConsole.window:isVisible() then
        DebugConsole.window:hide()
    else
        DebugConsole.window:show()
        DebugConsole.window:focus()
        DebugConsole.commandInput:focus()
    end
end

-- Executar comando
function DebugConsole.executeCommand()
    local command = DebugConsole.commandInput:getText()
    if command and command ~= '' then
        DebugConsole.executeLuaCommand(command)
        DebugConsole.commandInput:setText('')
    end
end

-- Executar comando Lua
function DebugConsole.executeLuaCommand(command)
    -- Adicionar comando ao log
    DebugConsole.addLog("> " .. command)
    
    -- Executar comando
    local success, result = pcall(loadstring(command))
    
    if success then
        if result then
            DebugConsole.addLog("Resultado: " .. tostring(result))
        end
    else
        DebugConsole.addLog("Erro: " .. tostring(result))
    end
end

-- Adicionar log ao console
function DebugConsole.addLog(message)
    local currentText = DebugConsole.logArea:getText()
    local newText = currentText .. message .. "\n"
    
    -- Limitar tamanho do log
    local lines = {}
    for line in newText:gmatch("[^\r\n]+") do
        table.insert(lines, line)
    end
    
    if #lines > 1000 then
        table.remove(lines, 1)
    end
    
    DebugConsole.logArea:setText(table.concat(lines, "\n"))
    
    -- Scroll para o final
    DebugConsole.logArea:setCursorPos(#newText)
end
```

### 🔍 **Inspetor de UI**

```lua
-- Inspetor de UI
local UIInspector = {}

function UIInspector.init()
    -- Criar janela do inspetor
    UIInspector.window = g_ui.createWidget('MainWindow', rootWidget)
    UIInspector.window:setId('uiInspector')
    UIInspector.window:setText('UI Inspector')
    UIInspector.window:setSize({width = 400, height = 500})
    UIInspector.window:hide()
    
    -- Área de propriedades
    UIInspector.propertiesArea = g_ui.createWidget('TextEdit', UIInspector.window)
    UIInspector.propertiesArea:setId('inspectorProperties')
    UIInspector.propertiesArea:setPosition({x = 10, y = 30})
    UIInspector.propertiesArea:setSize({width = 380, height = 460})
    UIInspector.propertiesArea:setTextWrap(true)
    UIInspector.propertiesArea:setEditable(false)
    
    -- Configurar hotkey
    g_keyboard.bindKeyDown('Ctrl+Shift+I', UIInspector.toggle)
    
    -- Conectar eventos de mouse
    connect(g_mouse, {
        onMousePress = UIInspector.onMousePress
    })
end

-- Alternar visibilidade do inspetor
function UIInspector.toggle()
    if UIInspector.window:isVisible() then
        UIInspector.window:hide()
    else
        UIInspector.window:show()
        UIInspector.window:focus()
    end
end

-- Evento de clique do mouse
function UIInspector.onMousePress(mousePos, button)
    if not UIInspector.window:isVisible() then
        return
    end
    
    -- Encontrar widget na posição
    local widget = g_ui.getWidgetAt(mousePos)
    if widget then
        UIInspector.inspectWidget(widget)
    end
end

-- Inspecionar widget
function UIInspector.inspectWidget(widget)
    local properties = {}
    
    -- Propriedades básicas
    table.insert(properties, "ID: " .. (widget:getId() or "N/A"))
    table.insert(properties, "Tipo: " .. widget:getClassName())
    table.insert(properties, "Visível: " .. tostring(widget:isVisible()))
    table.insert(properties, "Habilitado: " .. tostring(widget:isEnabled()))
    table.insert(properties, "Focado: " .. tostring(widget:isFocused()))
    
    -- Posição e tamanho
    local pos = widget:getPosition()
    local size = widget:getSize()
    table.insert(properties, "Posição: " .. pos.x .. ", " .. pos.y)
    table.insert(properties, "Tamanho: " .. size.width .. "x" .. size.height)
    
    -- Texto
    if widget:getText then
        local text = widget:getText()
        if text and text ~= '' then
            table.insert(properties, "Texto: " .. text)
        end
    end
    
    -- Imagem
    if widget:getImageSource then
        local image = widget:getImageSource()
        if image and image ~= '' then
            table.insert(properties, "Imagem: " .. image)
        end
    end
    
    -- Cores
    if widget:getBackgroundColor then
        local bgColor = widget:getBackgroundColor()
        if bgColor then
            table.insert(properties, "Cor de fundo: " .. bgColor)
        end
    end
    
    if widget:getForegroundColor then
        local fgColor = widget:getForegroundColor()
        if fgColor then
            table.insert(properties, "Cor de frente: " .. fgColor)
        end
    end
    
    -- Filhos
    local children = widget:getChildren()
    if #children > 0 then
        table.insert(properties, "Filhos: " .. #children)
        for i, child in ipairs(children) do
            table.insert(properties, "  " .. i .. ": " .. child:getClassName() .. 
                " (ID: " .. (child:getId() or "N/A") .. ")")
        end
    end
    
    -- Atualizar área de propriedades
    UIInspector.propertiesArea:setText(table.concat(properties, "\n"))
end
```

---

## ⚡ Profiling e Performance

### 📊 **Sistema de Profiling**

```lua
-- Sistema de profiling
local PerformanceProfiler = {}

PerformanceProfiler.timers = {}
PerformanceProfiler.counters = {}
PerformanceProfiler.memorySnapshots = {}

-- Medir tempo de execução
function PerformanceProfiler.measureTime(name, func)
    local startTime = g_clock.millis()
    local result = func()
    local endTime = g_clock.millis()
    
    local duration = endTime - startTime
    
    if not PerformanceProfiler.timers[name] then
        PerformanceProfiler.timers[name] = {
            totalTime = 0,
            calls = 0,
            minTime = math.huge,
            maxTime = 0
        }
    end
    
    local timer = PerformanceProfiler.timers[name]
    timer.totalTime = timer.totalTime + duration
    timer.calls = timer.calls + 1
    timer.minTime = math.min(timer.minTime, duration)
    timer.maxTime = math.max(timer.maxTime, duration)
    
    return result
end

-- Medir tempo com callback
function PerformanceProfiler.measureTimeCallback(name, callback)
    local startTime = g_clock.millis()
    
    local function endMeasurement()
        local endTime = g_clock.millis()
        local duration = endTime - startTime
        
        if not PerformanceProfiler.timers[name] then
            PerformanceProfiler.timers[name] = {
                totalTime = 0,
                calls = 0,
                minTime = math.huge,
                maxTime = 0
            }
        end
        
        local timer = PerformanceProfiler.timers[name]
        timer.totalTime = timer.totalTime + duration
        timer.calls = timer.calls + 1
        timer.minTime = math.min(timer.minTime, duration)
        timer.maxTime = math.max(timer.maxTime, duration)
    end
    
    return callback, endMeasurement
end

-- Contador de chamadas
function PerformanceProfiler.countCall(name)
    if not PerformanceProfiler.counters[name] then
        PerformanceProfiler.counters[name] = 0
    end
    
    PerformanceProfiler.counters[name] = PerformanceProfiler.counters[name] + 1
end

-- Snapshot de memória
function PerformanceProfiler.takeMemorySnapshot(name)
    local memoryUsage = collectgarbage("count")
    PerformanceProfiler.memorySnapshots[name] = {
        memory = memoryUsage,
        timestamp = g_clock.millis()
    }
end

-- Relatório de performance
function PerformanceProfiler.generateReport()
    local report = {}
    table.insert(report, "=== RELATÓRIO DE PERFORMANCE ===")
    table.insert(report, "")
    
    -- Timers
    table.insert(report, "TIMERS:")
    for name, timer in pairs(PerformanceProfiler.timers) do
        local avgTime = timer.calls > 0 and timer.totalTime / timer.calls or 0
        table.insert(report, string.format("  %s: %d calls, %.2fms avg (%.2fms min, %.2fms max)", 
            name, timer.calls, avgTime, timer.minTime, timer.maxTime))
    end
    
    table.insert(report, "")
    
    -- Counters
    table.insert(report, "COUNTERS:")
    for name, count in pairs(PerformanceProfiler.counters) do
        table.insert(report, string.format("  %s: %d", name, count))
    end
    
    table.insert(report, "")
    
    -- Memory snapshots
    table.insert(report, "MEMORY SNAPSHOTS:")
    for name, snapshot in pairs(PerformanceProfiler.memorySnapshots) do
        table.insert(report, string.format("  %s: %.2f KB (at %d ms)", 
            name, snapshot.memory, snapshot.timestamp))
    end
    
    return table.concat(report, "\n")
end
```

### 🎯 **Ferramentas de Análise**

```lua
-- Analisador de performance
local PerformanceAnalyzer = {}

function PerformanceAnalyzer.analyzeFrameTime()
    local frameTimes = {}
    local lastFrameTime = g_clock.millis()
    
    local function measureFrame()
        local currentTime = g_clock.millis()
        local frameTime = currentTime - lastFrameTime
        table.insert(frameTimes, frameTime)
        
        lastFrameTime = currentTime
        
        -- Manter apenas os últimos 100 frames
        if #frameTimes > 100 then
            table.remove(frameTimes, 1)
        end
        
        scheduleEvent(measureFrame, 16)  -- ~60 FPS
    end
    
    measureFrame()
    
    -- Calcular estatísticas
    local totalTime = 0
    local minTime = math.huge
    local maxTime = 0
    
    for _, time in ipairs(frameTimes) do
        totalTime = totalTime + time
        minTime = math.min(minTime, time)
        maxTime = math.max(maxTime, time)
    end
    
    local avgTime = #frameTimes > 0 and totalTime / #frameTimes or 0
    local fps = avgTime > 0 and 1000 / avgTime or 0
    
    return {
        averageFrameTime = avgTime,
        minFrameTime = minTime,
        maxFrameTime = maxTime,
        fps = fps,
        frameCount = #frameTimes
    }
end

-- Analisador de memória
function PerformanceAnalyzer.analyzeMemory()
    local memoryUsage = collectgarbage("count")
    local textureCount = g_textures.getLoadedTextureCount()
    local soundCount = g_sounds.getLoadedSoundCount()
    
    return {
        memoryUsage = memoryUsage,
        textureCount = textureCount,
        soundCount = soundCount
    }
end

-- Analisador de widgets
function PerformanceAnalyzer.analyzeWidgets()
    local widgetCount = 0
    local widgetTypes = {}
    
    local function countWidgets(widget)
        widgetCount = widgetCount + 1
        
        local className = widget:getClassName()
        widgetTypes[className] = (widgetTypes[className] or 0) + 1
        
        local children = widget:getChildren()
        for _, child in ipairs(children) do
            countWidgets(child)
        end
    end
    
    countWidgets(g_ui.getRootWidget())
    
    return {
        totalWidgets = widgetCount,
        widgetTypes = widgetTypes
    }
end
```

---

## 🔍 Inspetores de UI

### 🎯 **Inspetor de Hierarquia**

```lua
-- Inspetor de hierarquia de widgets
local HierarchyInspector = {}

function HierarchyInspector.init()
    -- Criar janela do inspetor
    HierarchyInspector.window = g_ui.createWidget('MainWindow', rootWidget)
    HierarchyInspector.window:setId('hierarchyInspector')
    HierarchyInspector.window:setText('Hierarchy Inspector')
    HierarchyInspector.window:setSize({width = 300, height = 600})
    HierarchyInspector.window:hide()
    
    -- Árvore de widgets
    HierarchyInspector.treeWidget = g_ui.createWidget('UIWidget', HierarchyInspector.window)
    HierarchyInspector.treeWidget:setId('hierarchyTree')
    HierarchyInspector.treeWidget:setPosition({x = 10, y = 30})
    HierarchyInspector.treeWidget:setSize({width = 280, height = 570})
    
    -- Configurar hotkey
    g_keyboard.bindKeyDown('Ctrl+Shift+H', HierarchyInspector.toggle)
end

-- Alternar visibilidade
function HierarchyInspector.toggle()
    if HierarchyInspector.window:isVisible() then
        HierarchyInspector.window:hide()
    else
        HierarchyInspector.window:show()
        HierarchyInspector.refresh()
    end
end

-- Atualizar hierarquia
function HierarchyInspector.refresh()
    -- Limpar árvore
    HierarchyInspector.treeWidget:clearChildren()
    
    -- Construir hierarquia
    local rootWidget = g_ui.getRootWidget()
    HierarchyInspector.buildTree(rootWidget, HierarchyInspector.treeWidget, 0)
end

-- Construir árvore
function HierarchyInspector.buildTree(widget, parentNode, depth)
    local indent = string.rep("  ", depth)
    local nodeText = indent .. widget:getClassName()
    
    if widget:getId() then
        nodeText = nodeText .. " (ID: " .. widget:getId() .. ")"
    end
    
    if not widget:isVisible() then
        nodeText = nodeText .. " [HIDDEN]"
    end
    
    local node = g_ui.createWidget('Label', parentNode)
    node:setText(nodeText)
    node:setPosition({x = 0, y = depth * 20})
    
    -- Adicionar filhos
    local children = widget:getChildren()
    for _, child in ipairs(children) do
        HierarchyInspector.buildTree(child, parentNode, depth + 1)
    end
end
```

---

## ⚠️ Sistema de Erros

### 🎯 **Captura de Exceções**

```lua
-- Sistema de captura de erros
local ErrorHandler = {}

ErrorHandler.errors = {}
ErrorHandler.maxErrors = 100

-- Capturar erro
function ErrorHandler.captureError(error, stackTrace)
    local errorInfo = {
        message = error,
        stackTrace = stackTrace,
        timestamp = g_clock.millis(),
        context = ErrorHandler.getContext()
    }
    
    table.insert(ErrorHandler.errors, errorInfo)
    
    -- Limitar número de erros
    if #ErrorHandler.errors > ErrorHandler.maxErrors then
        table.remove(ErrorHandler.errors, 1)
    end
    
    -- Log do erro
    DebugLogger.error("ERROR", "Erro capturado: " .. error)
    if stackTrace then
        DebugLogger.error("ERROR", "Stack trace: " .. stackTrace)
    end
    
    -- Mostrar erro ao usuário se necessário
    if g_settings.getBoolean("debug.showErrors", false) then
        ErrorHandler.showErrorDialog(error, stackTrace)
    end
end

-- Obter contexto do erro
function ErrorHandler.getContext()
    local context = {}
    
    -- Informações do jogo
    context.gameOnline = g_game.isOnline()
    if context.gameOnline then
        context.player = g_game.getLocalPlayer()
        if context.player then
            context.playerPosition = context.player:getPosition()
            context.playerHealth = context.player:getHealth()
        end
    end
    
    -- Informações do sistema
    context.fps = g_app.getFps()
    context.memory = collectgarbage("count")
    context.uptime = g_clock.millis()
    
    return context
end

-- Mostrar diálogo de erro
function ErrorHandler.showErrorDialog(error, stackTrace)
    local dialog = g_ui.createWidget('MainWindow', rootWidget)
    dialog:setText('Erro Detectado')
    dialog:setSize({width = 500, height = 400})
    
    local textArea = g_ui.createWidget('TextEdit', dialog)
    textArea:setPosition({x = 10, y = 30})
    textArea:setSize({width = 480, height = 320})
    textArea:setText("Erro: " .. error .. "\n\nStack Trace:\n" .. (stackTrace or "N/A"))
    textArea:setEditable(false)
    
    local closeButton = g_ui.createWidget('Button', dialog)
    closeButton:setText('Fechar')
    closeButton:setPosition({x = 200, y = 360})
    closeButton:setSize({width = 100, height = 30})
    closeButton.onClick = function()
        dialog:destroy()
    end
end

-- Relatório de erros
function ErrorHandler.generateErrorReport()
    local report = {}
    table.insert(report, "=== RELATÓRIO DE ERROS ===")
    table.insert(report, "")
    
    for i, error in ipairs(ErrorHandler.errors) do
        table.insert(report, string.format("Erro %d:", i))
        table.insert(report, "  Mensagem: " .. error.message)
        table.insert(report, "  Timestamp: " .. os.date("%Y-%m-%d %H:%M:%S", error.timestamp / 1000))
        
        if error.stackTrace then
            table.insert(report, "  Stack Trace: " .. error.stackTrace)
        end
        
        if error.context then
            table.insert(report, "  Contexto: " .. json.encode(error.context))
        end
        
        table.insert(report, "")
    end
    
    return table.concat(report, "\n")
end
```

---

## 🌐 Debug Remoto

### 🎯 **Sistema de Debug Remoto**

```lua
-- Sistema de debug remoto
local RemoteDebugger = {}

RemoteDebugger.connected = false
RemoteDebugger.port = 8080
RemoteDebugger.host = "localhost"

function RemoteDebugger.init()
    -- Configurar servidor de debug
    RemoteDebugger.server = nil
    
    -- Conectar eventos
    connect(g_game, {
        onGameStart = RemoteDebugger.onGameStart,
        onGameEnd = RemoteDebugger.onGameEnd
    })
end

-- Iniciar servidor de debug
function RemoteDebugger.startServer()
    if RemoteDebugger.server then
        return
    end
    
    -- Aqui você implementaria a conexão com um servidor de debug
    -- Por exemplo, usando WebSockets ou TCP
    
    DebugLogger.info("REMOTE_DEBUG", "Servidor de debug iniciado na porta " .. RemoteDebugger.port)
    RemoteDebugger.connected = true
end

-- Parar servidor de debug
function RemoteDebugger.stopServer()
    if RemoteDebugger.server then
        -- Fechar conexão
        RemoteDebugger.server = nil
        RemoteDebugger.connected = false
        
        DebugLogger.info("REMOTE_DEBUG", "Servidor de debug parado")
    end
end

-- Enviar dados para debug remoto
function RemoteDebugger.sendData(data)
    if not RemoteDebugger.connected then
        return
    end
    
    -- Enviar dados para o servidor de debug
    -- Implementar conforme necessário
end

-- Eventos do jogo
function RemoteDebugger.onGameStart()
    if g_settings.getBoolean("debug.enableRemote", false) then
        RemoteDebugger.startServer()
    end
end

function RemoteDebugger.onGameEnd()
    RemoteDebugger.stopServer()
end
```

---

## ⚡ Performance e Otimização

### 🚀 **Otimizações de Debug**

```lua
-- Configurações de performance para debug
local DebugPerformance = {}

DebugPerformance.config = {
    enableProfiling = false,
    enableMemoryTracking = false,
    enableWidgetTracking = false,
    logLevel = "INFO"
}

-- Configurar debug baseado em performance
function DebugPerformance.configureDebug()
    local fps = g_app.getFps()
    local memory = collectgarbage("count")
    
    if fps < 30 then
        -- Desabilitar debug pesado em performance baixa
        DebugPerformance.config.enableProfiling = false
        DebugPerformance.config.enableMemoryTracking = false
        DebugPerformance.config.enableWidgetTracking = false
        DebugPerformance.config.logLevel = "ERROR"
    elseif fps < 50 then
        -- Debug limitado
        DebugPerformance.config.enableProfiling = true
        DebugPerformance.config.enableMemoryTracking = false
        DebugPerformance.config.enableWidgetTracking = false
        DebugPerformance.config.logLevel = "WARN"
    else
        -- Debug completo
        DebugPerformance.config.enableProfiling = true
        DebugPerformance.config.enableMemoryTracking = true
        DebugPerformance.config.enableWidgetTracking = true
        DebugPerformance.config.logLevel = "INFO"
    end
end

-- Verificar se debug está habilitado
function DebugPerformance.isDebugEnabled()
    return g_settings.getBoolean("debug.enabled", false)
end

-- Verificar se profiling está habilitado
function DebugPerformance.isProfilingEnabled()
    return DebugPerformance.config.enableProfiling and DebugPerformance.isDebugEnabled()
end
```

---

### 🎮 **Sistema de Debug Completo**

```lua
-- Sistema de debug principal
local DebugSystem = {}

function DebugSystem.init()
    -- Inicializar componentes
    DebugLogger.init()
    DebugConsole.init()
    UIInspector.init()
    HierarchyInspector.init()
    PerformanceProfiler.init()
    ErrorHandler.init()
    RemoteDebugger.init()
    
    -- Configurar performance
    DebugPerformance.configureDebug()
    
    -- Conectar eventos de erro
    connect(g_app, {
        onError = ErrorHandler.captureError
    })
    
    DebugLogger.info("DEBUG", "Sistema de debug inicializado")
end

function DebugSystem.terminate()
    -- Gerar relatórios finais
    local performanceReport = PerformanceProfiler.generateReport()
    local errorReport = ErrorHandler.generateErrorReport()
    
    -- Salvar relatórios
    local reportFile = io.open("debug_report.txt", "w")
    if reportFile then
        reportFile:write(performanceReport .. "\n\n" .. errorReport)
        reportFile:close()
    end
    
    DebugLogger.info("DEBUG", "Sistema de debug finalizado")
end

-- Funções de conveniência
function DebugSystem.log(category, message, ...)
    DebugLogger.info(category, message, ...)
end

function DebugSystem.error(category, message, ...)
    DebugLogger.error(category, message, ...)
end

function DebugSystem.measure(name, func)
    if DebugPerformance.isProfilingEnabled() then
        return PerformanceProfiler.measureTime(name, func)
    else
        return func()
    end
end

function DebugSystem.count(name)
    if DebugPerformance.isProfilingEnabled() then
        PerformanceProfiler.countCall(name)
    end
end
```

### 🎨 **Debug de Módulos**

```lua
-- Debug específico para módulos
local ModuleDebugger = {}

function ModuleDebugger.setupModuleDebug(moduleName)
    local module = modules[moduleName]
    if not module then
        DebugLogger.error("MODULE_DEBUG", "Módulo não encontrado: " .. moduleName)
        return
    end
    
    -- Wrapper para funções do módulo
    local originalInit = module.init
    local originalTerminate = module.terminate
    
    module.init = function(...)
        DebugLogger.info("MODULE_DEBUG", "Iniciando módulo: " .. moduleName)
        local startTime = g_clock.millis()
        
        local result = originalInit(...)
        
        local endTime = g_clock.millis()
        DebugLogger.info("MODULE_DEBUG", "Módulo iniciado: " .. moduleName .. 
            " (tempo: " .. (endTime - startTime) .. "ms)")
        
        return result
    end
    
    module.terminate = function(...)
        DebugLogger.info("MODULE_DEBUG", "Finalizando módulo: " .. moduleName)
        
        local result = originalTerminate(...)
        
        DebugLogger.info("MODULE_DEBUG", "Módulo finalizado: " .. moduleName)
        
        return result
    end
    
    DebugLogger.info("MODULE_DEBUG", "Debug configurado para módulo: " .. moduleName)
end

-- Setup automático para todos os módulos
function ModuleDebugger.setupAllModules()
    for moduleName, module in pairs(modules) do
        if module.init and module.terminate then
            ModuleDebugger.setupModuleDebug(moduleName)
        end
    end
end
```

---

## ✅ Melhores Práticas

### 🎯 **Uso Eficiente do Sistema**

```lua
-- ✅ BOM: Usar níveis de log apropriados
DebugLogger.debug("NETWORK", "Pacote recebido: " .. packetType)
DebugLogger.info("GAME", "Jogador conectado: " .. playerName)
DebugLogger.warn("UI", "Widget não encontrado: " .. widgetId)
DebugLogger.error("SYSTEM", "Erro crítico: " .. errorMessage)

-- ✅ BOM: Medir performance seletivamente
if DebugPerformance.isProfilingEnabled() then
    PerformanceProfiler.measureTime("expensiveOperation", function()
        -- operação custosa
    end)
end

-- ✅ BOM: Usar contextos específicos
DebugLogger.info("COMBAT", "Ataque realizado: " .. damage .. " dano")
DebugLogger.info("INVENTORY", "Item movido: " .. itemId)

-- ❌ EVITE: Log excessivo
function onEveryFrame()
    DebugLogger.debug("FRAME", "Frame processado")  -- Muito verboso
end

-- ❌ EVITE: Medir tudo
PerformanceProfiler.measureTime("simpleOperation", function()
    local x = 1 + 1  -- Operação muito simples
end)
```

### 🔧 **Configuração Adequada**

```lua
-- ✅ BOM: Configurar debug baseado em ambiente
local DEBUG_CONFIG = {
    development = {
        logLevel = "DEBUG",
        enableProfiling = true,
        enableUIInspector = true
    },
    production = {
        logLevel = "ERROR",
        enableProfiling = false,
        enableUIInspector = false
    }
}

-- ✅ BOM: Verificar configurações antes de usar
function safeDebugLog(level, category, message, ...)
    if DebugPerformance.isDebugEnabled() then
        DebugLogger.log(level, category, message, ...)
    end
end

-- ✅ BOM: Limpar recursos adequadamente
function cleanupDebugSystem()
    -- Limpar timers
    PerformanceProfiler.timers = {}
    PerformanceProfiler.counters = {}
    
    -- Fechar arquivos de log
    if DebugLogger.logFile then
        DebugLogger.logFile:close()
    end
    
    -- Parar servidor remoto
    RemoteDebugger.stopServer()
end
```

### 🎨 **Design Consistente**

```lua
-- ✅ BOM: Usar categorias padronizadas
local DEBUG_CATEGORIES = {
    SYSTEM = "SYSTEM",
    NETWORK = "NETWORK",
    GAME = "GAME",
    UI = "UI",
    COMBAT = "COMBAT",
    INVENTORY = "INVENTORY",
    MODULE = "MODULE"
}

-- ✅ BOM: Usar níveis consistentes
local DEBUG_LEVELS = {
    TRACE = 0,
    DEBUG = 1,
    INFO = 2,
    WARN = 3,
    ERROR = 4,
    FATAL = 5
}

-- ✅ BOM: Funções de debug padronizadas
function debugLog(category, message, ...)
    DebugLogger.info(category, message, ...)
end

function debugError(category, message, ...)
    DebugLogger.error(category, message, ...)
end

function debugMeasure(name, func)
    return PerformanceProfiler.measureTime(name, func)
end
```

O sistema de debug do OTClient oferece ferramentas poderosas para desenvolvimento e troubleshooting. Use estas práticas para garantir eficiência e manutenibilidade em suas aplicações. 
> - [Getting_Started_Guide](Getting_Started_Guide.md) - Comece aqui
> - [Module_System_Guide](Module_System_Guide.md) - Sistema de módulos
> - [UI_System_Guide](UI_System_Guide.md) - Interface do usuário
> - [Lua_API_Reference](Lua_API_Reference.md) - Referência da API

---

<div class="success"> **Navegação**
> **📚 Documentos Relacionados:**
> - [Getting_Started_Guide](Getting_Started_Guide.md) - Comece aqui
> - [Module_System_Guide](Module_System_Guide.md) - Sistema de módulos
> - [UI_System_Guide](UI_System_Guide.md) - Interface do usuário
> - [Lua_API_Reference](Lua_API_Reference.md) - API completa
> 
> **🔗 Navegação Rápida:**
> - [Wiki_Index](Wiki_Index.md) - Voltar ao índice
> - [Cheat_Sheet](Cheat_Sheet.md) - Referência rápida
> - [Debug_System_Guide](Debug_System_Guide.md) - Debugging

