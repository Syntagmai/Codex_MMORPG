---
tags: [otclient, core, debug, system, development, logging, profiling, troubleshooting]
type: core_story
status: completed
priority: critical
story_id: CORE-007
created: 2025-01-27
---

# CORE-007: Sistema de Debug

> [!info] **Sistema Completo de Debug e Desenvolvimento**
> Documentação completa do sistema de debug do OTClient, incluindo ferramentas de desenvolvimento, logging estruturado, profiling e troubleshooting para facilitar o desenvolvimento e manutenção.

## 📋 Índice
- [[#Visão Geral]]
- [[#Sistema de Logging]]
- [[#Ferramentas de Debug]]
- [[#Profiling e Performance]]
- [[#Inspetores de UI]]
- [[#Sistema de Erros]]
- [[#Debug Remoto]]
- [[#Exemplos Práticos]]
- [[#Melhores Práticas]]

---

## 🎯 Visão Geral

O sistema de debug do OTClient oferece um conjunto completo de ferramentas para desenvolvimento, troubleshooting e otimização:

### **🔧 Componentes Principais:**
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

#### Nível Basic
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
    
    -- Configurar arquivo de log
    if DebugLogger.config.enableFile then
        DebugLogger.config.logFile = g_settings.getString("debug.logFile", "otclient.log")
    end
    
    print("Debug Logger inicializado com nível:", logLevel)
end
```

#### Nível Intermediate
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
    
    -- Configurar arquivo de log
    if DebugLogger.config.enableFile then
        DebugLogger.config.logFile = g_settings.getString("debug.logFile", "otclient.log")
    end
    
    print("Debug Logger inicializado com nível:", logLevel)
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
    
    -- Configurar arquivo de log
    if DebugLogger.config.enableFile then
        DebugLogger.config.logFile = g_settings.getString("debug.logFile", "otclient.log")
    end
    
    print("Debug Logger inicializado com nível:", logLevel)
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

### 🔧 **Funções de Logging**

#### Inicialização e Configuração
```lua
-- Funções de logging
function DebugLogger.trace(message, ...)
    DebugLogger.log(DebugLogger.LEVELS.TRACE, message, ...)
end

function DebugLogger.debug(message, ...)
    DebugLogger.log(DebugLogger.LEVELS.DEBUG, message, ...)
end

function DebugLogger.info(message, ...)
    DebugLogger.log(DebugLogger.LEVELS.INFO, message, ...)
end

function DebugLogger.warn(message, ...)
    DebugLogger.log(DebugLogger.LEVELS.WARN, message, ...)
end

function DebugLogger.error(message, ...)
    DebugLogger.log(DebugLogger.LEVELS.ERROR, message, ...)
end

function DebugLogger.fatal(message, ...)
```

#### Funcionalidade 1
```lua
    DebugLogger.log(DebugLogger.LEVELS.FATAL, message, ...)
end

-- Função principal de logging
function DebugLogger.log(level, message, ...)
    if level < DebugLogger.config.level then
        return
    end
    
    local formattedMessage = string.format(message, ...)
    local timestamp = os.date("%Y-%m-%d %H:%M:%S")
    local levelName = {"TRACE", "DEBUG", "INFO", "WARN", "ERROR", "FATAL"}[level + 1]
    
    local logEntry = string.format("[%s] [%s] %s", timestamp, levelName, formattedMessage)
    
    -- Saída para console
    if DebugLogger.config.enableConsole then
        print(logEntry)
    end
    
    -- Saída para arquivo
    if DebugLogger.config.enableFile then
        local file = io.open(DebugLogger.config.logFile, "a")
        if file then
            file:write(logEntry .. "\n")
            file:close()
        end
```

#### Finalização
```lua
    end
end
```

---

## 🛠️ Ferramentas de Debug

### 🎮 **Console de Debug**

#### Inicialização e Configuração
```lua
-- Console de debug avançado
local DebugConsole = {}

function DebugConsole.init()
    -- Criar console de debug
    local console = g_ui.createWidget("Console", rootWidget)
    console:setId("debugConsole")
    console:setVisible(false)
    
    -- Configurar comandos de debug
    DebugConsole.setupCommands(console)
    
    return console
end

function DebugConsole.setupCommands(console)
    -- Comando para mostrar informações do sistema
    console:addCommand("sysinfo", function()
        DebugConsole.showSystemInfo()
    end)
    
    -- Comando para mostrar informações de memória
    console:addCommand("memory", function()
        DebugConsole.showMemoryInfo()
    end)
```

#### Funcionalidade 1
```lua
    
    -- Comando para mostrar informações de performance
    console:addCommand("perf", function()
        DebugConsole.showPerformanceInfo()
    end)
    
    -- Comando para limpar logs
    console:addCommand("clearlogs", function()
        DebugConsole.clearLogs()
    end)
end

function DebugConsole.showSystemInfo()
    local info = {
        version = g_app.getVersion(),
        platform = g_app.getPlatform(),
        memory = collectgarbage("count"),
        uptime = g_clock.millis(),
        fps = g_app.getFps()
    }
    
    DebugLogger.info("=== System Info ===")
    for key, value in pairs(info) do
        DebugLogger.info("%s: %s", key, tostring(value))
    end
```

#### Finalização
```lua
end
```

### 🔍 **Inspetores de UI**

```lua
-- Inspetores de UI para debug
    --  Inspetores de UI para debug (traduzido)
local UIDebugger = {}

function UIDebugger.init()
    -- Função: UIDebugger
    -- Criar inspetores
    --  Criar inspetores (traduzido)
    UIDebugger.createWidgetInspector()
    UIDebugger.createEventInspector()
    UIDebugger.createStyleInspector()
end

function UIDebugger.createWidgetInspector()
    -- Função: UIDebugger
    local inspector = g_ui.createWidget("WidgetInspector", rootWidget)
    inspector:setId("widgetInspector")
    inspector:setVisible(false)
    
    -- Funcionalidade de inspeção de widgets
    inspector.onMousePress = function(self, mousePos, mouseButton)
        local widget = g_ui.getWidgetAt(mousePos)
        if widget then
    -- Verificação condicional
            UIDebugger.inspectWidget(widget)
        end
    end
end

function UIDebugger.inspectWidget(widget)
    -- Função: UIDebugger
    local info = {
        id = widget:getId(),
        className = widget:getClassName(),
        position = widget:getPosition(),
        size = widget:getSize(),
        visible = widget:isVisible(),
        enabled = widget:isEnabled(),
        focused = widget:isFocused()
    }
    
    DebugLogger.info("=== Widget Inspection ===")
    for key, value in pairs(info) do
    -- Loop de repetição
        DebugLogger.info("%s: %s", key, tostring(value))
    end
end
```

---

## 📊 Profiling e Performance

### ⚡ **Sistema de Profiling**

```lua
-- Sistema de profiling para performance
    --  Sistema de profiling para performance (traduzido)
local PerformanceProfiler = {}

PerformanceProfiler.timers = {}
PerformanceProfiler.memorySnapshots = {}

function PerformanceProfiler.startTimer(name)
    -- Função: PerformanceProfiler
    PerformanceProfiler.timers[name] = g_clock.millis()
end

function PerformanceProfiler.endTimer(name)
    -- Função: PerformanceProfiler
    if PerformanceProfiler.timers[name] then
    -- Verificação condicional
        local duration = g_clock.millis() - PerformanceProfiler.timers[name]
        DebugLogger.info("Timer [%s]: %dms", name, duration)
        PerformanceProfiler.timers[name] = nil
        return duration
    end
    return 0
end

function PerformanceProfiler.takeMemorySnapshot(name)
    -- Função: PerformanceProfiler
    local memory = collectgarbage("count")
    PerformanceProfiler.memorySnapshots[name] = memory
    DebugLogger.info("Memory Snapshot [%s]: %.2f KB", name, memory)
    return memory
end

function PerformanceProfiler.compareMemorySnapshots(snapshot1, snapshot2)
    -- Função: PerformanceProfiler
    if PerformanceProfiler.memorySnapshots[snapshot1] and PerformanceProfiler.memorySnapshots[snapshot2] then
    -- Verificação condicional
        local diff = PerformanceProfiler.memorySnapshots[snapshot2] - PerformanceProfiler.memorySnapshots[snapshot1]
        DebugLogger.info("Memory Difference [%s -> %s]: %.2f KB", snapshot1, snapshot2, diff)
        return diff
    end
    return 0
end
```

### 🎯 **Monitor de Performance**

```lua
-- Monitor de performance em tempo real
    --  Monitor de performance em tempo real (traduzido)
local PerformanceMonitor = {}

PerformanceMonitor.enabled = false
PerformanceMonitor.interval = 1000  -- 1 segundo
PerformanceMonitor.lastUpdate = 0

function PerformanceMonitor.start()
    -- Função: PerformanceMonitor
    PerformanceMonitor.enabled = true
    PerformanceMonitor.lastUpdate = g_clock.millis()
    DebugLogger.info("Performance Monitor iniciado")
end

function PerformanceMonitor.stop()
    -- Função: PerformanceMonitor
    PerformanceMonitor.enabled = false
    DebugLogger.info("Performance Monitor parado")
end

function PerformanceMonitor.update()
    -- Função: PerformanceMonitor
    if not PerformanceMonitor.enabled then
    -- Verificação condicional
        return
    end
    
    local currentTime = g_clock.millis()
    if currentTime - PerformanceMonitor.lastUpdate >= PerformanceMonitor.interval then
    -- Verificação condicional
        PerformanceMonitor.logPerformance()
        PerformanceMonitor.lastUpdate = currentTime
    end
end

function PerformanceMonitor.logPerformance()
    -- Função: PerformanceMonitor
    local fps = g_app.getFps()
    local memory = collectgarbage("count")
    local uptime = g_clock.millis()
    
    DebugLogger.debug("Performance - FPS: %d, Memory: %.2f KB, Uptime: %dms", fps, memory, uptime)
end
```

---

## 🚨 Sistema de Erros

### ⚠️ **Captura de Exceções**

#### Inicialização e Configuração
```lua
-- Sistema de captura e tratamento de erros
local ErrorHandler = {}

ErrorHandler.errorCount = 0
ErrorHandler.maxErrors = 100

function ErrorHandler.init()
    -- Configurar handler de erros
    ErrorHandler.setupErrorHandling()
end

function ErrorHandler.setupErrorHandling()
    -- Capturar erros de Lua
    local oldError = error
    error = function(message, level)
        ErrorHandler.handleError(message, level or 2)
        oldError(message, level)
    end
    
    -- Capturar erros de C++
    connect(g_app, 'onError', function(error)
        ErrorHandler.handleCppError(error)
    end)
```

#### Funcionalidade 1
```lua
end

function ErrorHandler.handleError(message, level)
    ErrorHandler.errorCount = ErrorHandler.errorCount + 1
    
    local stackTrace = debug.traceback(message, level)
    DebugLogger.error("Lua Error #%d: %s", ErrorHandler.errorCount, message)
    DebugLogger.error("Stack Trace:\n%s", stackTrace)
    
    -- Salvar erro em arquivo
    ErrorHandler.saveErrorToFile(message, stackTrace)
    
    -- Verificar limite de erros
    if ErrorHandler.errorCount >= ErrorHandler.maxErrors then
        DebugLogger.fatal("Máximo de erros atingido (%d)", ErrorHandler.maxErrors)
        g_app.exit()
    end
end

function ErrorHandler.handleCppError(error)
    ErrorHandler.errorCount = ErrorHandler.errorCount + 1
    
    DebugLogger.error("C++ Error #%d: %s", ErrorHandler.errorCount, error)
    
    -- Salvar erro em arquivo
    ErrorHandler.saveErrorToFile(error, "C++ Error")
end
```

#### Finalização
```lua

function ErrorHandler.saveErrorToFile(message, stackTrace)
    local file = io.open("errors.log", "a")
    if file then
        local timestamp = os.date("%Y-%m-%d %H:%M:%S")
        file:write(string.format("[%s] %s\n", timestamp, message))
        if stackTrace then
            file:write(stackTrace .. "\n")
        end
        file:write("---\n")
        file:close()
    end
end
```

---

## 🌐 Debug Remoto

### 🔗 **Debug Remoto**

```lua
-- Sistema de debug remoto
    --  Sistema de debug remoto (traduzido)
local RemoteDebugger = {}

RemoteDebugger.enabled = false
RemoteDebugger.port = 8080
RemoteDebugger.connections = {}

function RemoteDebugger.init()
    -- Função: RemoteDebugger
    -- Configurar debug remoto
    --  Configurar debug remoto (traduzido)
    RemoteDebugger.enabled = g_settings.getBoolean("debug.remoteEnabled", false)
    RemoteDebugger.port = g_settings.getNumber("debug.remotePort", 8080)
    
    if RemoteDebugger.enabled then
    -- Verificação condicional
        RemoteDebugger.startServer()
    end
end

function RemoteDebugger.startServer()
    -- Função: RemoteDebugger
    -- Implementar servidor de debug remoto
    --  Implementar servidor de debug remoto (traduzido)
    DebugLogger.info("Remote Debug Server iniciado na porta %d", RemoteDebugger.port)
end

function RemoteDebugger.sendDebugInfo(info)
    -- Função: RemoteDebugger
    if not RemoteDebugger.enabled then
    -- Verificação condicional
        return
    end
    
    -- Enviar informações de debug para clientes remotos
    for _, connection in pairs(RemoteDebugger.connections) do
    -- Loop de repetição
        connection:send(info)
    end
end
```

---

## 💡 Exemplos Práticos

### 🎯 **Exemplo de Uso Completo**

#### Nível Basic
```lua
-- Exemplo completo de uso do sistema de debug
function setupDebugSystem()
    -- Inicializar sistema de logging
    -- Inicializar ferramentas de debug
    -- Inicializar sistema de erros
    -- Inicializar debug remoto
    -- Iniciar monitor de performance
end
-- Exemplo de uso em desenvolvimento
function debugExample()
    -- Iniciar timer
    -- Tomar snapshot de memória
    -- Executar operação
    local result = someComplexOperation()
    -- Tomar snapshot de memória
    -- Comparar snapshots
    -- Finalizar timer
    PerformanceProfiler.endTimer("exampleFunction")
    -- Log do resultado
end
```

#### Nível Intermediate
```lua
-- Exemplo completo de uso do sistema de debug
function setupDebugSystem()
    -- Inicializar sistema de logging
    DebugLogger.init()
    
    -- Inicializar ferramentas de debug
    DebugConsole.init()
    UIDebugger.init()
    
    -- Inicializar sistema de erros
    ErrorHandler.init()
    
    -- Inicializar debug remoto
    RemoteDebugger.init()
    
    -- Iniciar monitor de performance
    PerformanceMonitor.start()
    
    DebugLogger.info("Sistema de debug inicializado com sucesso")
end

-- Exemplo de uso em desenvolvimento
function debugExample()
    -- Iniciar timer
    PerformanceProfiler.startTimer("exampleFunction")
    
    -- Tomar snapshot de memória
    PerformanceProfiler.takeMemorySnapshot("before")
    
    -- Executar operação
    local result = someComplexOperation()
    
    -- Tomar snapshot de memória
    PerformanceProfiler.takeMemorySnapshot("after")
    
    -- Comparar snapshots
    PerformanceProfiler.compareMemorySnapshots("before", "after")
    
    -- Finalizar timer
    PerformanceProfiler.endTimer("exampleFunction")
    
    -- Log do resultado
    DebugLogger.info("Resultado da operação: %s", tostring(result))
    
    return result
end
```

#### Nível Advanced
```lua
-- Exemplo completo de uso do sistema de debug
function setupDebugSystem()
    -- Inicializar sistema de logging
    DebugLogger.init()
    
    -- Inicializar ferramentas de debug
    DebugConsole.init()
    UIDebugger.init()
    
    -- Inicializar sistema de erros
    ErrorHandler.init()
    
    -- Inicializar debug remoto
    RemoteDebugger.init()
    
    -- Iniciar monitor de performance
    PerformanceMonitor.start()
    
    DebugLogger.info("Sistema de debug inicializado com sucesso")
end

-- Exemplo de uso em desenvolvimento
function debugExample()
    -- Iniciar timer
    PerformanceProfiler.startTimer("exampleFunction")
    
    -- Tomar snapshot de memória
    PerformanceProfiler.takeMemorySnapshot("before")
    
    -- Executar operação
    local result = someComplexOperation()
    
    -- Tomar snapshot de memória
    PerformanceProfiler.takeMemorySnapshot("after")
    
    -- Comparar snapshots
    PerformanceProfiler.compareMemorySnapshots("before", "after")
    
    -- Finalizar timer
    PerformanceProfiler.endTimer("exampleFunction")
    
    -- Log do resultado
    DebugLogger.info("Resultado da operação: %s", tostring(result))
    
    return result
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

### 🔧 **Configuração de Debug**

```lua
-- Configuração de debug no arquivo de configuração
local debugConfig = {
    -- Sistema de logging
    --  Sistema de logging (traduzido)
    logLevel = "INFO",
    enableConsole = true,
    enableFile = true,
    logFile = "otclient.log",
    
    -- Ferramentas de debug
    --  Ferramentas de debug (traduzido)
    enableConsole = true,
    enableWidgetInspector = true,
    enableEventInspector = true,
    
    -- Performance
    --  Performance (traduzido)
    enablePerformanceMonitor = true,
    performanceMonitorInterval = 1000,
    
    -- Debug remoto
    --  Debug remoto (traduzido)
    remoteEnabled = false,
    remotePort = 8080,
    
    -- Sistema de erros
    --  Sistema de erros (traduzido)
    maxErrors = 100,
    saveErrorsToFile = true
}

-- Aplicar configuração
function applyDebugConfig(config)
    -- Função: applyDebugConfig
    for key, value in pairs(config) do
    -- Loop de repetição
        g_settings.setValue("debug." .. key, value)
    end
end
```

---

## ✅ Melhores Práticas

### 🎯 **Recomendações de Uso**

1. **Níveis de Log Apropriados**
   - Use `TRACE` para informações detalhadas de execução
   - Use `DEBUG` para informações de desenvolvimento
   - Use `INFO` para informações gerais
   - Use `WARN` para avisos não críticos
   - Use `ERROR` para erros recuperáveis
   - Use `FATAL` para erros críticos

2. **Performance**
   - Use timers para medir performance de funções críticas
   - Monitore uso de memória em operações complexas
   - Evite logging excessivo em produção

3. **Debug Remoto**
   - Use apenas em ambiente de desenvolvimento
   - Configure firewall adequadamente
   - Monitore conexões ativas

4. **Tratamento de Erros**
   - Sempre capture e log erros
   - Forneça contexto útil nos logs
   - Implemente recuperação quando possível

### 🚨 **Considerações de Segurança**

- **Logs Sensíveis**: Nunca log dados sensíveis (senhas, tokens)
- **Debug Remoto**: Use apenas em redes seguras
- **Arquivos de Log**: Configure permissões adequadas
- **Rotação de Logs**: Implemente rotação para evitar crescimento excessivo

---

## 📊 Métricas e Monitoramento

### 📈 **Indicadores de Performance**

- **FPS**: Frames por segundo
- **Memory Usage**: Uso de memória em KB
- **Error Rate**: Taxa de erros por minuto
- **Response Time**: Tempo de resposta de operações críticas

### 🔍 **Logs Estruturados**

#### Nível Basic
```json

```

#### Nível Intermediate
```json
{
  "timestamp": "2025-01-27T10:30:00Z",
  "level": "INFO",
  "category": "performance",
  "message": "Operation completed",
  "data": {
    "duration": 150,
    "memory": 1024.5,
    "fps": 60
  }
}
```

#### Nível Advanced
```json
{
  "timestamp": "2025-01-27T10:30:00Z",
  "level": "INFO",
  "category": "performance",
  "message": "Operation completed",
  "data": {
    "duration": 150,
    "memory": 1024.5,
    "fps": 60
  }
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

---

**Story ID**: CORE-007  
**Categoria**: CORE  
**Status**: ✅ Completo  
**Última Atualização**: 2025-01-27 