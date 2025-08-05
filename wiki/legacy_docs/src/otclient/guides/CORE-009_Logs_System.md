
# CORE-009: Sistema de Logs

<div class="info"> **Sistema Completo de Logging e Monitoramento**
> Documentação completa do sistema de logs do OTClient, incluindo logging estruturado, níveis de log, rotação de arquivos, monitoramento e análise de logs para desenvolvimento e produção.

## 📋 Índice
- [#Visão Geral](#Visão Geral.md)
- [#Sistema de Logging](#Sistema de Logging.md)
- [#Níveis de Log](#Níveis de Log.md)
- [#Rotação de Arquivos](#Rotação de Arquivos.md)
- [#Logs Estruturados](#Logs Estruturados.md)
- [#Monitoramento de Logs](#Monitoramento de Logs.md)
- [#Análise de Logs](#Análise de Logs.md)
- [#Exemplos Práticos](#Exemplos Práticos.md)
- [#Melhores Práticas](#Melhores Práticas.md)

---

## 🎯 Visão Geral

O sistema de logs do OTClient oferece capacidades completas de logging e monitoramento:

### **📝 Componentes Principais:**
- **Logging Estruturado**: Logs organizados e categorizados
- **Múltiplos Níveis**: TRACE, DEBUG, INFO, WARN, ERROR, FATAL
- **Rotação Automática**: Gerenciamento inteligente de arquivos
- **Logs Estruturados**: Formato JSON para análise
- **Monitoramento em Tempo Real**: Alertas e notificações
- **Análise Avançada**: Ferramentas de análise e relatórios

### 🏗️ **Arquitetura do Sistema**

```
Sistema de Logs
   │
   ├─ Logging Engine
   │   ├─ Log Levels
   │   ├─ Log Categories
   │   ├─ Log Formatters
   │   └─ Log Handlers
   │
   ├─ File Management
   │   ├─ File Rotation
   │   ├─ Compression
   │   ├─ Cleanup
   │   └─ Backup
   │
   ├─ Structured Logging
   │   ├─ JSON Format
   │   ├─ Metadata
   │   ├─ Context
   │   └─ Correlation
   │
   └─ Monitoring & Analysis
       ├─ Real-time Monitoring
       ├─ Log Analysis
       ├─ Performance Metrics
       └─ Error Tracking
```

---

## 📝 Sistema de Logging

### 🎯 **Configuração Principal**

#### Inicialização e Configuração
```lua
-- Sistema de logging principal
local LogSystem = {}

-- Configuração global
LogSystem.config = {
    -- Níveis de log
    level = "INFO",
    levels = {
        TRACE = 0,
        DEBUG = 1,
        INFO = 2,
        WARN = 3,
        ERROR = 4,
        FATAL = 5
    },
    
    -- Configuração de arquivos
    file = {
        enabled = true,
        path = "logs/",
        filename = "otclient.log",
        maxSize = 10 * 1024 * 1024,  -- 10MB
        maxFiles = 5,
        compress = true
    },
```

#### Funcionalidade 1
```lua
    
    -- Configuração de console
    console = {
        enabled = true,
        colors = true,
        timestamp = true
    },
    
    -- Configuração de logs estruturados
    structured = {
        enabled = true,
        format = "json",
        includeMetadata = true,
        includeContext = true
    }
}

-- Inicializar sistema de logs
function LogSystem.init()
    LogSystem.loadConfiguration()
    LogSystem.setupDirectories()
    LogSystem.setupHandlers()
    LogSystem.setupRotation()
    
    print("Sistema de logs inicializado")
end
```

#### Funcionalidade 2
```lua

function LogSystem.loadConfiguration()
    -- Carregar configuração das settings
    LogSystem.config.level = g_settings.getString("logs.level", "INFO")
    LogSystem.config.file.enabled = g_settings.getBoolean("logs.file.enabled", true)
    LogSystem.config.console.enabled = g_settings.getBoolean("logs.console.enabled", true)
    LogSystem.config.structured.enabled = g_settings.getBoolean("logs.structured.enabled", true)
    
    -- Configurar caminho dos logs
    if LogSystem.config.file.enabled then
        LogSystem.config.file.path = g_settings.getString("logs.file.path", "logs/")
        LogSystem.config.file.filename = g_settings.getString("logs.file.filename", "otclient.log")
    end
end

function LogSystem.setupDirectories()
    -- Criar diretório de logs se não existir
    if LogSystem.config.file.enabled then
        local path = LogSystem.config.file.path
        if not io.open(path, "r") then
            os.execute("mkdir -p " .. path)
        end
```

#### Finalização
```lua
    end
end
```

### 🔧 **Handlers de Log**

#### Inicialização e Configuração
```lua
-- Handlers de log
LogSystem.handlers = {}

function LogSystem.setupHandlers()
    -- Handler de arquivo
    if LogSystem.config.file.enabled then
        LogSystem.handlers.file = LogSystem.createFileHandler()
    end
    
    -- Handler de console
    if LogSystem.config.console.enabled then
        LogSystem.handlers.console = LogSystem.createConsoleHandler()
    end
    
    -- Handler estruturado
    if LogSystem.config.structured.enabled then
        LogSystem.handlers.structured = LogSystem.createStructuredHandler()
    end
end

function LogSystem.createFileHandler()
```

#### Funcionalidade 1
```lua
    local handler = {}
    
    handler.write = function(level, message, metadata)
        local filepath = LogSystem.config.file.path .. LogSystem.config.file.filename
        local file = io.open(filepath, "a")
        
        if file then
            local logEntry = LogSystem.formatLogEntry(level, message, metadata)
            file:write(logEntry .. "\n")
            file:close()
            
            -- Verificar rotação
            LogSystem.checkRotation(filepath)
        end
    end
    
    return handler
end

function LogSystem.createConsoleHandler()
    local handler = {}
    
    -- Cores para console
    local colors = {
        TRACE = "\27[36m",  -- Cyan
        DEBUG = "\27[34m",  -- Blue
        INFO = "\27[32m",   -- Green
        WARN = "\27[33m",   -- Yellow
        ERROR = "\27[31m",  -- Red
        FATAL = "\27[35m",  -- Magenta
        RESET = "\27[0m"    -- Reset
    }
```

#### Funcionalidade 2
```lua
    
    handler.write = function(level, message, metadata)
        local logEntry = LogSystem.formatLogEntry(level, message, metadata)
        
        if LogSystem.config.console.colors then
            local color = colors[level] or colors.RESET
            print(color .. logEntry .. colors.RESET)
        else
            print(logEntry)
        end
    end
    
    return handler
end

function LogSystem.createStructuredHandler()
    local handler = {}
    
    handler.write = function(level, message, metadata)
        local structuredLog = LogSystem.createStructuredLog(level, message, metadata)
        local filepath = LogSystem.config.file.path .. "structured.log"
        local file = io.open(filepath, "a")
        
        if file then
            file:write(structuredLog .. "\n")
            file:close()
        end
```

#### Finalização
```lua
    end
    
    return handler
end
```

---

## 📊 Níveis de Log

### 🎯 **Definição de Níveis**

#### Inicialização e Configuração
```lua
-- Níveis de log detalhados
LogSystem.LEVEL_DEFINITIONS = {
    TRACE = {
        level = 0,
        name = "TRACE",
        description = "Informações detalhadas de execução",
        color = "cyan",
        enabled = true
    },
    DEBUG = {
        level = 1,
        name = "DEBUG",
        description = "Informações de desenvolvimento",
        color = "blue",
        enabled = true
    },
    INFO = {
        level = 2,
        name = "INFO",
        description = "Informações gerais",
        color = "green",
        enabled = true
    },
```

#### Funcionalidade 1
```lua
    WARN = {
        level = 3,
        name = "WARN",
        description = "Avisos não críticos",
        color = "yellow",
        enabled = true
    },
    ERROR = {
        level = 4,
        name = "ERROR",
        description = "Erros recuperáveis",
        color = "red",
        enabled = true
    },
    FATAL = {
        level = 5,
        name = "FATAL",
        description = "Erros críticos",
        color = "magenta",
        enabled = true
    }
```

#### Funcionalidade 2
```lua
}

-- Funções de logging por nível
function LogSystem.trace(message, ...)
    LogSystem.log("TRACE", message, ...)
end

function LogSystem.debug(message, ...)
    LogSystem.log("DEBUG", message, ...)
end

function LogSystem.info(message, ...)
    LogSystem.log("INFO", message, ...)
end

function LogSystem.warn(message, ...)
    LogSystem.log("WARN", message, ...)
end

function LogSystem.error(message, ...)
    LogSystem.log("ERROR", message, ...)
end
```

#### Funcionalidade 3
```lua

function LogSystem.fatal(message, ...)
    LogSystem.log("FATAL", message, ...)
end

-- Função principal de logging
function LogSystem.log(level, message, ...)
    -- Verificar se nível está habilitado
    if not LogSystem.isLevelEnabled(level) then
        return
    end
    
    -- Formatar mensagem
    local formattedMessage = string.format(message, ...)
    
    -- Coletar metadados
    local metadata = LogSystem.collectMetadata(level, formattedMessage)
    
    -- Escrever em todos os handlers
    for _, handler in pairs(LogSystem.handlers) do
        if handler.write then
            handler.write(level, formattedMessage, metadata)
        end
```

#### Finalização
```lua
    end
    
    -- Ações especiais para níveis críticos
    if level == "FATAL" then
        LogSystem.handleFatalError(formattedMessage, metadata)
    elseif level == "ERROR" then
        LogSystem.handleError(formattedMessage, metadata)
    end
end

function LogSystem.isLevelEnabled(level)
    local currentLevel = LogSystem.config.levels[LogSystem.config.level]
    local messageLevel = LogSystem.config.levels[level]
    
    return messageLevel >= currentLevel
end
```

### 🔍 **Metadados e Contexto**

#### Inicialização e Configuração
```lua
-- Coleta de metadados
function LogSystem.collectMetadata(level, message)
    local metadata = {
        timestamp = os.date("%Y-%m-%d %H:%M:%S"),
        level = level,
        message = message,
        thread = stdext.getThreadId(),
        uptime = g_clock.millis()
    }
    
    -- Adicionar contexto do jogo
    if g_game and g_game.isOnline() then
        metadata.game = {
            online = true,
            character = g_game.getCharacterName(),
            world = g_game.getWorldName(),
            position = g_game.getLocalPlayer():getPosition()
        }
    else
        metadata.game = {
            online = false
        }
```

#### Funcionalidade 1
```lua
    end
    
    -- Adicionar informações do sistema
    metadata.system = {
        version = g_app.getVersion(),
        platform = g_app.getPlatform(),
        memory = collectgarbage("count"),
        fps = g_app.getFps()
    }
    
    -- Adicionar stack trace para erros
    if level == "ERROR" or level == "FATAL" then
        metadata.stackTrace = debug.traceback()
    end
    
    return metadata
end

function LogSystem.handleError(message, metadata)
    -- Incrementar contador de erros
    LogSystem.errorCount = (LogSystem.errorCount or 0) + 1
    
    -- Salvar erro em arquivo separado
    local errorFile = io.open(LogSystem.config.file.path .. "errors.log", "a")
    if errorFile then
        local errorEntry = LogSystem.formatErrorEntry(message, metadata)
        errorFile:write(errorEntry .. "\n")
        errorFile:close()
    end
```

#### Finalização
```lua
    
    -- Notificar sistema de monitoramento
    LogSystem.notifyMonitoring("ERROR", message, metadata)
end

function LogSystem.handleFatalError(message, metadata)
    -- Log do erro fatal
    LogSystem.handleError(message, metadata)
    
    -- Salvar dump de estado
    LogSystem.saveStateDump(metadata)
    
    -- Notificar sistema de monitoramento
    LogSystem.notifyMonitoring("FATAL", message, metadata)
    
    -- Opcional: encerrar aplicação
    if g_settings.getBoolean("logs.fatal.exit", false) then
        g_app.exit()
    end
end
```

---

## 🔄 Rotação de Arquivos

### 🎯 **Sistema de Rotação**

#### Inicialização e Configuração
```lua
-- Sistema de rotação de arquivos
LogSystem.rotation = {}

function LogSystem.setupRotation()
    LogSystem.rotation.enabled = LogSystem.config.file.enabled
    LogSystem.rotation.maxSize = LogSystem.config.file.maxSize
    LogSystem.rotation.maxFiles = LogSystem.config.file.maxFiles
    LogSystem.rotation.compress = LogSystem.config.file.compress
end

function LogSystem.checkRotation(filepath)
    if not LogSystem.rotation.enabled then
        return
    end
    
    local file = io.open(filepath, "r")
    if not file then
        return
    end
    
    -- Verificar tamanho do arquivo
    file:seek("end")
    local size = file:seek("cur")
    file:close()
    
    if size > LogSystem.rotation.maxSize then
        LogSystem.rotateFile(filepath)
    end
```

#### Funcionalidade 1
```lua
end

function LogSystem.rotateFile(filepath)
    -- Fechar arquivo atual
    local currentFile = io.open(filepath, "r")
    if not currentFile then
        return
    end
    currentFile:close()
    
    -- Rotacionar arquivos existentes
    for i = LogSystem.rotation.maxFiles - 1, 1, -1 do
        local oldFile = filepath .. "." .. i
        local newFile = filepath .. "." .. (i + 1)
        
        if LogSystem.rotation.compress then
            oldFile = oldFile .. ".gz"
            newFile = newFile .. ".gz"
        end
        
        if io.open(oldFile, "r") then
            os.rename(oldFile, newFile)
        end
```

#### Funcionalidade 2
```lua
    end
    
    -- Mover arquivo atual
    local backupFile = filepath .. ".1"
    if LogSystem.rotation.compress then
        backupFile = backupFile .. ".gz"
        LogSystem.compressFile(filepath, backupFile)
        os.remove(filepath)
    else
        os.rename(filepath, backupFile)
    end
    
    -- Criar novo arquivo
    local newFile = io.open(filepath, "w")
    if newFile then
        newFile:write("=== Log Rotation: " .. os.date("%Y-%m-%d %H:%M:%S") .. " ===\n")
        newFile:close()
    end
    
    LogSystem.info("Log file rotated: %s", filepath)
end
```

#### Funcionalidade 3
```lua

function LogSystem.compressFile(source, destination)
    -- Comprimir arquivo usando gzip
    local command = string.format("gzip -c %s > %s", source, destination)
    os.execute(command)
end

function LogSystem.cleanupOldLogs()
    if not LogSystem.rotation.enabled then
        return
    end
    
    local logPath = LogSystem.config.file.path
    local pattern = logPath .. "*.log*"
    
    -- Listar arquivos de log
    local files = {}
    for file in io.popen("ls -t " .. pattern):lines() do
        table.insert(files, file)
    end
    
    -- Manter apenas os arquivos mais recentes
    for i = LogSystem.rotation.maxFiles + 1, #files do
        os.remove(files[i])
        LogSystem.info("Removed old log file: %s", files[i])
    end
```

#### Finalização
```lua
end
```

---

## 📋 Logs Estruturados

### 🎯 **Formato JSON**

#### Inicialização e Configuração
```lua
-- Sistema de logs estruturados
LogSystem.structured = {}

function LogSystem.createStructuredLog(level, message, metadata)
    local structuredLog = {
        timestamp = metadata.timestamp,
        level = level,
        message = message,
        metadata = metadata,
        correlation = LogSystem.getCorrelationId(),
        session = LogSystem.getSessionId()
    }
    
    return LogSystem.encodeJSON(structuredLog)
end

function LogSystem.encodeJSON(data)
    -- Implementação simples de JSON encoding
    local json = "{"
    local first = true
    
    for key, value in pairs(data) do
        if not first then
            json = json .. ","
        end
```

#### Funcionalidade 1
```lua
        first = false
        
        if type(value) == "string" then
            json = json .. string.format('"%s":"%s"', key, LogSystem.escapeJSON(value))
        elseif type(value) == "number" then
            json = json .. string.format('"%s":%s', key, tostring(value))
        elseif type(value) == "boolean" then
            json = json .. string.format('"%s":%s', key, tostring(value))
        elseif type(value) == "table" then
            json = json .. string.format('"%s":%s', key, LogSystem.encodeJSON(value))
        end
    end
    
    json = json .. "}"
    return json
end

function LogSystem.escapeJSON(str)
    return str:gsub('\\', '\\\\'):gsub('"', '\\"'):gsub('\n', '\\n'):gsub('\r', '\\r'):gsub('\t', '\\t')
end

function LogSystem.getCorrelationId()
```

#### Funcionalidade 2
```lua
    -- Gerar ID de correlação para rastrear operações
    if not LogSystem.correlationId then
        LogSystem.correlationId = LogSystem.generateUUID()
    end
    return LogSystem.correlationId
end

function LogSystem.getSessionId()
    -- ID da sessão atual
    if not LogSystem.sessionId then
        LogSystem.sessionId = LogSystem.generateUUID()
    end
    return LogSystem.sessionId
end

function LogSystem.generateUUID()
    -- Gerar UUID simples
    local template = "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx"
    return string.gsub(template, "[xy]", function(c)
        local v = (c == "x") and math.random(0, 0xf) or math.random(8, 0xb)
        return string.format("%x", v)
    end)
```

#### Finalização
```lua
end
```

---

## 📊 Monitoramento de Logs

### 🎯 **Monitor em Tempo Real**

#### Inicialização e Configuração
```lua
-- Sistema de monitoramento de logs
LogSystem.monitoring = {}

function LogSystem.setupMonitoring()
    LogSystem.monitoring.enabled = g_settings.getBoolean("logs.monitoring.enabled", true)
    LogSystem.monitoring.interval = g_settings.getNumber("logs.monitoring.interval", 5000)  -- 5 segundos
    LogSystem.monitoring.lastCheck = 0
    LogSystem.monitoring.metrics = {
        totalLogs = 0,
        errors = 0,
        warnings = 0,
        lastError = nil,
        lastWarning = nil
    }
    
    if LogSystem.monitoring.enabled then
        LogSystem.startMonitoring()
    end
end

function LogSystem.startMonitoring()
```

#### Funcionalidade 1
```lua
    -- Iniciar monitoramento em background
    connect(g_app, 'onRun', function()
        LogSystem.updateMonitoring()
    end)
end

function LogSystem.updateMonitoring()
    if not LogSystem.monitoring.enabled then
        return
    end
    
    local currentTime = g_clock.millis()
    if currentTime - LogSystem.monitoring.lastCheck >= LogSystem.monitoring.interval then
        LogSystem.checkLogMetrics()
        LogSystem.monitoring.lastCheck = currentTime
    end
end

function LogSystem.checkLogMetrics()
    local metrics = LogSystem.monitoring.metrics
    
    -- Verificar taxa de erros
    if metrics.errors > 10 then
        LogSystem.warn("High error rate detected: %d errors", metrics.errors)
    end
```

#### Funcionalidade 2
```lua
    
    -- Verificar último erro
    if metrics.lastError and g_clock.millis() - metrics.lastError.timestamp > 300000 then  -- 5 minutos
        LogSystem.info("No errors in the last 5 minutes")
    end
    
    -- Gerar relatório de métricas
    LogSystem.generateMetricsReport()
end

function LogSystem.generateMetricsReport()
    local metrics = LogSystem.monitoring.metrics
    local report = {
        timestamp = os.date("%Y-%m-%d %H:%M:%S"),
        totalLogs = metrics.totalLogs,
        errors = metrics.errors,
        warnings = metrics.warnings,
        errorRate = metrics.totalLogs > 0 and (metrics.errors / metrics.totalLogs) * 100 or 0
    }
    
    -- Salvar relatório
    local reportFile = io.open(LogSystem.config.file.path .. "metrics.log", "a")
    if reportFile then
        reportFile:write(LogSystem.encodeJSON(report) .. "\n")
        reportFile:close()
    end
```

#### Funcionalidade 3
```lua
end

function LogSystem.notifyMonitoring(level, message, metadata)
    if not LogSystem.monitoring.enabled then
        return
    end
    
    local metrics = LogSystem.monitoring.metrics
    metrics.totalLogs = metrics.totalLogs + 1
    
    if level == "ERROR" or level == "FATAL" then
        metrics.errors = metrics.errors + 1
        metrics.lastError = {
            message = message,
            timestamp = g_clock.millis(),
            metadata = metadata
        }
    elseif level == "WARN" then
        metrics.warnings = metrics.warnings + 1
        metrics.lastWarning = {
            message = message,
            timestamp = g_clock.millis(),
            metadata = metadata
        }
```

#### Finalização
```lua
    end
end
```

---

## 🔍 Análise de Logs

### 🎯 **Ferramentas de Análise**

#### Inicialização e Configuração
```lua
-- Sistema de análise de logs
LogSystem.analysis = {}

function LogSystem.analyzeLogs(options)
    options = options or {}
    local analysis = {
        period = options.period or "24h",
        level = options.level or "ERROR",
        file = options.file or LogSystem.config.file.path .. LogSystem.config.file.filename
    }
    
    LogSystem.info("Iniciando análise de logs: %s", analysis.file)
    
    local results = {
        totalEntries = 0,
        errors = 0,
        warnings = 0,
        topErrors = {},
        performance = {},
        patterns = {}
    }
```

#### Funcionalidade 1
```lua
    
    -- Ler arquivo de log
    local file = io.open(analysis.file, "r")
    if not file then
        LogSystem.error("Arquivo de log não encontrado: %s", analysis.file)
        return results
    end
    
    for line in file:lines() do
        local entry = LogSystem.parseLogEntry(line)
        if entry then
            results.totalEntries = results.totalEntries + 1
            
            -- Contar por nível
            if entry.level == "ERROR" or entry.level == "FATAL" then
                results.errors = results.errors + 1
                LogSystem.analyzeError(entry, results)
            elseif entry.level == "WARN" then
                results.warnings = results.warnings + 1
            end
            
            -- Análise de performance
            LogSystem.analyzePerformance(entry, results)
            
            -- Análise de padrões
            LogSystem.analyzePatterns(entry, results)
        end
```

#### Funcionalidade 2
```lua
    end
    
    file:close()
    
    -- Gerar relatório
    LogSystem.generateAnalysisReport(results)
    
    return results
end

function LogSystem.parseLogEntry(line)
    -- Parser simples para entradas de log
    local pattern = "%[(%d+-%d+-%d+ %d+:%d+:%d+)%] %[(%w+)%] (.+)"
    local timestamp, level, message = line:match(pattern)
    
    if timestamp and level and message then
        return {
            timestamp = timestamp,
            level = level,
            message = message,
            raw = line
        }
```

#### Funcionalidade 3
```lua
    end
    
    return nil
end

function LogSystem.analyzeError(entry, results)
    -- Analisar erros mais comuns
    local errorKey = entry.message:match("^([^:]+)")
    if errorKey then
        results.topErrors[errorKey] = (results.topErrors[errorKey] or 0) + 1
    end
end

function LogSystem.analyzePerformance(entry, results)
    -- Extrair métricas de performance dos logs
    local fps = entry.message:match("FPS: (%d+)")
    local memory = entry.message:match("Memory: ([%d%.]+)")
    
    if fps then
        table.insert(results.performance, {
            timestamp = entry.timestamp,
            fps = tonumber(fps)
        })
```

#### Funcionalidade 4
```lua
    end
    
    if memory then
        table.insert(results.performance, {
            timestamp = entry.timestamp,
            memory = tonumber(memory)
        })
    end
end

function LogSystem.analyzePatterns(entry, results)
    -- Detectar padrões nos logs
    local patterns = {
        "timeout",
        "connection",
        "memory",
        "performance",
        "error"
    }
    
    for _, pattern in ipairs(patterns) do
        if entry.message:lower():find(pattern) then
            results.patterns[pattern] = (results.patterns[pattern] or 0) + 1
        end
```

#### Funcionalidade 5
```lua
    end
end

function LogSystem.generateAnalysisReport(results)
    LogSystem.info("=== Relatório de Análise de Logs ===")
    LogSystem.info("Total de entradas: %d", results.totalEntries)
    LogSystem.info("Erros: %d", results.errors)
    LogSystem.info("Avisos: %d", results.warnings)
    
    -- Top erros
    LogSystem.info("Top Erros:")
    local sortedErrors = {}
    for error, count in pairs(results.topErrors) do
        table.insert(sortedErrors, {error = error, count = count})
    end
    
    table.sort(sortedErrors, function(a, b)
        return a.count > b.count
    end)
    
    for i = 1, math.min(5, #sortedErrors) do
        LogSystem.info("  %d. %s (%d vezes)", i, sortedErrors[i].error, sortedErrors[i].count)
    end
```

#### Finalização
```lua
    
    -- Padrões
    LogSystem.info("Padrões Detectados:")
    for pattern, count in pairs(results.patterns) do
        LogSystem.info("  %s: %d", pattern, count)
    end
end
```

---

## 💡 Exemplos Práticos

### 🎯 **Exemplo de Uso Completo**

#### Inicialização e Configuração
```lua
-- Exemplo completo de uso do sistema de logs
function setupLogSystem()
    -- Inicializar sistema de logs
    LogSystem.init()
    
    -- Configurar monitoramento
    LogSystem.setupMonitoring()
    
    -- Configurar rotação automática
    LogSystem.setupRotation()
    
    -- Log de inicialização
    LogSystem.info("Sistema de logs inicializado com sucesso")
    LogSystem.info("Configuração: level=%s, file=%s, console=%s", 
        LogSystem.config.level,
        LogSystem.config.file.enabled and "enabled" or "disabled",
        LogSystem.config.console.enabled and "enabled" or "disabled"
    )
end

-- Exemplo de logging em diferentes contextos
function exampleLogging()
```

#### Funcionalidade 1
```lua
    -- Log de informação geral
    LogSystem.info("Iniciando operação de exemplo")
    
    -- Log de debug
    LogSystem.debug("Parâmetros: %s, %s", "param1", "param2")
    
    -- Log de trace para detalhes
    LogSystem.trace("Executando passo 1 da operação")
    
    -- Simular operação
    local success, result = pcall(function()
        return someOperation()
    end)
    
    if success then
        LogSystem.info("Operação concluída com sucesso: %s", result)
    else
        LogSystem.error("Erro na operação: %s", result)
    end
    
    -- Log de warning
    if someCondition then
        LogSystem.warn("Condição de atenção detectada")
    end
```

#### Funcionalidade 2
```lua
end

-- Exemplo de análise de logs
function analyzeLogsExample()
    LogSystem.info("Iniciando análise de logs...")
    
    local results = LogSystem.analyzeLogs({
        period = "24h",
        level = "ERROR"
    })
    
    LogSystem.info("Análise concluída: %d erros encontrados", results.errors)
    
    return results
end

-- Exemplo de monitoramento contínuo
function continuousLogging()
    -- Log de métricas do sistema
    LogSystem.info("Sistema - FPS: %d, Memory: %.2f KB", 
        g_app.getFps(), 
        collectgarbage("count")
    )
    
    -- Log de eventos do jogo
    if g_game and g_game.isOnline() then
        LogSystem.info("Game - Character: %s, World: %s", 
            g_game.getCharacterName(),
            g_game.getWorldName()
        )
    end
```

#### Finalização
```lua
    
    -- Log de performance
    LogSystem.debug("Performance - Frame time: %dms", g_app.getFrameTime())
end
```

---

## ✅ Melhores Práticas

### 🎯 **Recomendações de Logging**

1. **Níveis Apropriados**
   - Use `TRACE` para informações detalhadas de execução
   - Use `DEBUG` para informações de desenvolvimento
   - Use `INFO` para informações gerais importantes
   - Use `WARN` para situações que merecem atenção
   - Use `ERROR` para erros recuperáveis
   - Use `FATAL` para erros críticos

2. **Conteúdo dos Logs**
   - Inclua contexto relevante
   - Use mensagens descritivas
   - Evite dados sensíveis
   - Inclua identificadores únicos

3. **Performance**
   - Evite logging excessivo em produção
   - Use níveis apropriados
   - Configure rotação adequada
   - Monitore uso de disco

4. **Manutenção**
   - Revise logs regularmente
   - Configure alertas apropriados
   - Mantenha configurações atualizadas
   - Faça backup de logs importantes

### 🚨 **Considerações de Segurança**

- **Dados Sensíveis**: Nunca log senhas, tokens ou dados pessoais
- **Permissões**: Configure permissões adequadas nos arquivos de log
- **Retenção**: Defina política de retenção de logs
- **Acesso**: Restrinja acesso aos logs de produção

---

## 📊 Métricas e KPIs

### 📈 **Indicadores de Logging**

- **Log Volume**: Número de logs por hora/dia
- **Error Rate**: Taxa de erros (%)
- **Response Time**: Tempo de resposta do sistema de logs
- **Storage Usage**: Uso de armazenamento para logs
- **Log Quality**: Qualidade das mensagens de log

### 🔍 **Relatórios de Logs**

#### Nível Basic
```json

```

#### Nível Intermediate
```json
{
  "timestamp": "2025-01-27T10:30:00Z",
  "metrics": {
    "totalLogs": 1500,
    "errors": 15,
    "warnings": 45,
    "errorRate": 1.0,
    "storageUsed": "25MB"
  },
  "topErrors": [
    {"error": "Connection timeout", "count": 8},
    {"error": "Memory allocation failed", "count": 4}
  ],
  "performance": {
    "avgFPS": 58.5,
    "avgMemory": 24500.2
  }
}
```

#### Nível Advanced
```json
{
  "timestamp": "2025-01-27T10:30:00Z",
  "metrics": {
    "totalLogs": 1500,
    "errors": 15,
    "warnings": 45,
    "errorRate": 1.0,
    "storageUsed": "25MB"
  },
  "topErrors": [
    {"error": "Connection timeout", "count": 8},
    {"error": "Memory allocation failed", "count": 4}
  ],
  "performance": {
    "avgFPS": 58.5,
    "avgMemory": 24500.2
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

**Story ID**: CORE-009  
**Categoria**: CORE  
**Status**: ✅ Completo  
**Última Atualização**: 2025-01-27 