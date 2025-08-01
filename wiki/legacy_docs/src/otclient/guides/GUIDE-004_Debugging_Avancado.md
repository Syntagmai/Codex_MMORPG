
# 🔍 Guia de Debugging Avançado - OTClient

## 🎯 **Visão Geral**

Este guia fornece técnicas avançadas de debugging para o OTClient, incluindo ferramentas especializadas, metodologias estruturadas e casos de uso práticos para desenvolvedores e agentes de IA.

## 📚 **Pré-requisitos**

- ✅ Conhecimento básico do OTClient
- ✅ Familiaridade com Lua
- ✅ Compreensão do sistema de debug (CORE-007)
- ✅ Acesso ao console de debug

---

## 🛠️ **1. Ferramentas de Debug Avançadas**

### **1.1 Debug Console Avançado**

```lua
-- Acesso ao console de debug
local debugConsole = g_ui.getRootWidget():recursiveGetChildById('debugConsole')

-- Comandos avançados disponíveis
debugConsole:executeCommand('sysinfo')      -- Informações do sistema
debugConsole:executeCommand('memory')       -- Status da memória
debugConsole:executeCommand('perf')         -- Performance atual
debugConsole:executeCommand('clearlogs')    -- Limpar logs
debugConsole:executeCommand('trace')        -- Ativar trace completo
```

### **1.2 UI Debugger Avançado**

```lua
-- Inspetor de widgets avançado
local uiDebugger = require('ui_debugger')

-- Inspecionar widget específico
uiDebugger:inspectWidget('gameWindow')
uiDebugger:inspectWidget('inventoryPanel')

-- Listar todos os widgets ativos
uiDebugger:listActiveWidgets()

-- Monitorar eventos em tempo real
uiDebugger:monitorEvents('gameWindow', true)
```

### **1.3 Performance Profiler Avançado**

```lua
-- Profiler de performance detalhado
local profiler = require('performance_profiler')

-- Iniciar profiling de função específica
profiler:startFunctionProfile('onCreatureMove')

-- Criar snapshot de memória
profiler:createMemorySnapshot('before_combat')

-- Comparar snapshots
profiler:compareSnapshots('before_combat', 'after_combat')
```

---

## 🔍 **2. Metodologias de Debug Estruturadas**

### **2.1 Debug por Camadas**

```lua
-- Estratégia de debug em camadas
local function debugByLayers(issue)
    -- Camada 1: Verificação básica
    if not debugLayer1(issue) then
        return "Erro na camada 1"
    end
    
    -- Camada 2: Verificação de estado
    if not debugLayer2(issue) then
        return "Erro na camada 2"
    end
    
    -- Camada 3: Verificação de performance
    if not debugLayer3(issue) then
        return "Erro na camada 3"
    end
    
    return "Problema não identificado"
end

function debugLayer1(issue)
    -- Verificações básicas: existência, tipos, valores
    return true
end

function debugLayer2(issue)
    -- Verificações de estado: conexão, autenticação, dados
    return true
end

function debugLayer3(issue)
    -- Verificações de performance: memória, CPU, latência
    return true
end
```

### **2.2 Debug por Cenários**

```lua
-- Debug baseado em cenários específicos
local debugScenarios = {
    combat = {
        preconditions = {'player_logged', 'creature_targeted'},
        checks = {'health_display', 'mana_display', 'combat_animation'},
        postconditions = {'damage_calculated', 'experience_gained'}
    },
    
    inventory = {
        preconditions = {'inventory_open', 'item_selected'},
        checks = {'item_info_display', 'drag_drop_enabled'},
        postconditions = {'item_moved', 'weight_updated'}
    },
    
    networking = {
        preconditions = {'connection_active', 'protocol_version'},
        checks = {'packet_sent', 'response_received'},
        postconditions = {'data_processed', 'ui_updated'}
    }
}

function debugScenario(scenarioName)
    local scenario = debugScenarios[scenarioName]
    if not scenario then
        return "Cenário não encontrado"
    end
    
    -- Verificar pré-condições
    for _, precondition in ipairs(scenario.preconditions) do
        if not checkPrecondition(precondition) then
            return "Falha na pré-condição: " .. precondition
        end
    end
    
    -- Executar verificações
    for _, check in ipairs(scenario.checks) do
        if not performCheck(check) then
            return "Falha na verificação: " .. check
        end
    end
    
    -- Verificar pós-condições
    for _, postcondition in ipairs(scenario.postconditions) do
        if not checkPostcondition(postcondition) then
            return "Falha na pós-condição: " .. postcondition
        end
    end
    
    return "Cenário executado com sucesso"
end
```

---

## 🎯 **3. Casos de Uso Específicos**

### **3.1 Debug de Problemas de Performance**

```lua
-- Debug específico para problemas de performance
function debugPerformanceIssue()
    local profiler = require('performance_profiler')
    
    -- 1. Identificar gargalos
    profiler:startCPUProfile()
    -- Executar ação problemática
    profiler:stopCPUProfile()
    
    -- 2. Analisar uso de memória
    local memoryBefore = profiler:getMemoryUsage()
    -- Executar ação
    local memoryAfter = profiler:getMemoryUsage()
    
    -- 3. Verificar vazamentos
    if memoryAfter > memoryBefore * 1.5 then
        log("Possível vazamento de memória detectado")
        profiler:createMemorySnapshot('leak_detection')
    end
    
    -- 4. Otimizar se necessário
    if profiler:getAverageFrameTime() > 16.67 then -- 60 FPS
        optimizeRendering()
    end
end

function optimizeRendering()
    -- Reduzir qualidade de renderização
    g_settings.set('graphics-quality', 'low')
    
    -- Limpar cache de texturas
    g_graphics.clearTextureCache()
    
    -- Desabilitar efeitos visuais
    g_settings.set('enable-particles', false)
    g_settings.set('enable-shaders', false)
end
```

### **3.2 Debug de Problemas de Rede**

```lua
-- Debug específico para problemas de rede
function debugNetworkIssue()
    local networkDebugger = require('network_debugger')
    
    -- 1. Verificar conectividade
    if not networkDebugger:checkConnection() then
        return "Problema de conectividade detectado"
    end
    
    -- 2. Monitorar pacotes
    networkDebugger:startPacketMonitoring()
    
    -- 3. Verificar latência
    local latency = networkDebugger:measureLatency()
    if latency > 200 then -- 200ms
        log("Latência alta detectada: " .. latency .. "ms")
    end
    
    -- 4. Verificar perda de pacotes
    local packetLoss = networkDebugger:getPacketLoss()
    if packetLoss > 0.05 then -- 5%
        log("Perda de pacotes detectada: " .. (packetLoss * 100) .. "%")
    end
    
    -- 5. Analisar protocolo
    networkDebugger:analyzeProtocol()
end
```

### **3.3 Debug de Problemas de UI**

```lua
-- Debug específico para problemas de UI
function debugUIIssue()
    local uiDebugger = require('ui_debugger')
    
    -- 1. Verificar hierarquia de widgets
    uiDebugger:printWidgetHierarchy()
    
    -- 2. Verificar eventos
    uiDebugger:monitorEvents('gameWindow', true)
    
    -- 3. Verificar layouts
    uiDebugger:validateLayouts()
    
    -- 4. Verificar recursos
    uiDebugger:checkResources()
    
    -- 5. Verificar acessibilidade
    uiDebugger:checkAccessibility()
end
```

---

## 🔧 **4. Ferramentas de Debug Customizadas**

### **4.1 Debug Logger Avançado**

```lua
-- Logger de debug avançado com categorias
local AdvancedDebugLogger = {
    categories = {
        network = {enabled = true, level = 'debug'},
        ui = {enabled = true, level = 'info'},
        performance = {enabled = true, level = 'warn'},
        game = {enabled = true, level = 'error'}
    }
}

function AdvancedDebugLogger:log(category, level, message, data)
    if not self.categories[category] or not self.categories[category].enabled then
        return
    end
    
    local categoryLevel = self.categories[category].level
    if self:shouldLog(level, categoryLevel) then
        local logEntry = {
            timestamp = os.time(),
            category = category,
            level = level,
            message = message,
            data = data
        }
        
        self:writeLog(logEntry)
    end
end

function AdvancedDebugLogger:shouldLog(level, categoryLevel)
    local levels = {debug = 1, info = 2, warn = 3, error = 4}
    return levels[level] >= levels[categoryLevel]
end
```

### **4.2 Debug Monitor em Tempo Real**

```lua
-- Monitor de debug em tempo real
local DebugMonitor = {
    metrics = {},
    alerts = {},
    thresholds = {
        memory_usage = 0.8, -- 80%
        cpu_usage = 0.9,    -- 90%
        frame_time = 16.67, -- 60 FPS
        latency = 200       -- 200ms
    }
}

function DebugMonitor:startMonitoring()
    self.monitorTimer = scheduleEvent(function()
        self:collectMetrics()
        self:checkThresholds()
        self:updateDisplay()
    end, 1000) -- A cada segundo
end

function DebugMonitor:collectMetrics()
    self.metrics.memory = g_graphics.getMemoryUsage()
    self.metrics.cpu = g_graphics.getCPUUsage()
    self.metrics.frameTime = g_graphics.getAverageFrameTime()
    self.metrics.latency = g_game.getLatency()
end

function DebugMonitor:checkThresholds()
    for metric, value in pairs(self.metrics) do
        local threshold = self.thresholds[metric]
        if threshold and value > threshold then
            self:createAlert(metric, value, threshold)
        end
    end
end

function DebugMonitor:createAlert(metric, value, threshold)
    local alert = {
        timestamp = os.time(),
        metric = metric,
        value = value,
        threshold = threshold,
        severity = 'warning'
    }
    
    table.insert(self.alerts, alert)
    self:notifyAlert(alert)
end
```

---

## 📊 **5. Análise de Debug Avançada**

### **5.1 Análise de Logs Estruturada**

```lua
-- Analisador de logs estruturado
local LogAnalyzer = {
    patterns = {
        error = "ERROR: (.+)",
        warning = "WARNING: (.+)",
        performance = "PERF: (.+)",
        network = "NET: (.+)"
    }
}

function LogAnalyzer:analyzeLogFile(filename)
    local file = io.open(filename, 'r')
    if not file then
        return "Arquivo não encontrado"
    end
    
    local analysis = {
        errors = {},
        warnings = {},
        performance_issues = {},
        network_issues = {}
    }
    
    for line in file:lines() do
        for pattern_type, pattern in pairs(self.patterns) do
            local match = string.match(line, pattern)
            if match then
                table.insert(analysis[pattern_type], {
                    line = line,
                    match = match,
                    timestamp = self:extractTimestamp(line)
                })
            end
        end
    end
    
    file:close()
    return analysis
end

function LogAnalyzer:generateReport(analysis)
    local report = "=== Relatório de Análise de Log ===\n"
    
    for category, items in pairs(analysis) do
        report = report .. "\n" .. string.upper(category) .. " (" .. #items .. "):\n"
        for _, item in ipairs(items) do
            report = report .. "- " .. item.match .. "\n"
        end
    end
    
    return report
end
```

### **5.2 Debug de Performance Comparativo**

```lua
-- Debug de performance comparativo
local PerformanceComparator = {}

function PerformanceComparator:compareVersions(version1, version2)
    local results = {
        version1 = self:measurePerformance(version1),
        version2 = self:measurePerformance(version2),
        differences = {}
    }
    
    -- Comparar métricas
    for metric, value1 in pairs(results.version1) do
        local value2 = results.version2[metric]
        if value2 then
            local difference = ((value2 - value1) / value1) * 100
            results.differences[metric] = {
                absolute = value2 - value1,
                percentage = difference,
                better = difference > 0
            }
        end
    end
    
    return results
end

function PerformanceComparator:measurePerformance(version)
    -- Simular medição de performance
    return {
        frame_time = math.random(10, 20),
        memory_usage = math.random(50, 100),
        cpu_usage = math.random(20, 80),
        load_time = math.random(1000, 5000)
    }
end
```

---

## 🎯 **6. Melhores Práticas de Debug**

### **6.1 Estratégias de Debug**

1. **Debug Incremental**: Comece com verificações básicas e avance para análises complexas
2. **Debug por Eliminação**: Elimine possíveis causas uma por vez
3. **Debug por Comparação**: Compare com comportamento esperado ou versões anteriores
4. **Debug por Isolamento**: Isole o problema em um ambiente controlado

### **6.2 Ferramentas Recomendadas**

- **Debug Console**: Para comandos rápidos e verificações básicas
- **UI Debugger**: Para problemas de interface
- **Performance Profiler**: Para problemas de performance
- **Network Debugger**: Para problemas de rede
- **Log Analyzer**: Para análise de logs históricos

### **6.3 Checklist de Debug**

```lua
local debugChecklist = {
    "Verificar logs de erro",
    "Confirmar reprodução do problema",
    "Isolar componentes afetados",
    "Verificar dependências",
    "Testar em ambiente limpo",
    "Comparar com comportamento esperado",
    "Documentar passos para reprodução",
    "Implementar correção",
    "Testar correção",
    "Documentar solução"
}
```

---

## 📝 **7. Exemplos Práticos**

### **7.1 Debug de Crash do Cliente**

```lua
-- Debug de crash do cliente
function debugClientCrash()
    -- 1. Capturar informações do sistema
    local systemInfo = {
        os = g_system.getOS(),
        memory = g_system.getMemoryInfo(),
        graphics = g_graphics.getInfo(),
        network = g_game.getConnectionInfo()
    }
    
    -- 2. Verificar logs recentes
    local recentLogs = getRecentLogs(100) -- Últimas 100 linhas
    
    -- 3. Verificar estado do jogo
    local gameState = {
        player = g_game.getLocalPlayer(),
        creatures = g_map.getCreatures(),
        items = g_game.getLocalPlayer():getInventoryItems()
    }
    
    -- 4. Criar relatório de crash
    local crashReport = {
        timestamp = os.time(),
        system_info = systemInfo,
        recent_logs = recentLogs,
        game_state = gameState
    }
    
    -- 5. Salvar relatório
    saveCrashReport(crashReport)
    
    return crashReport
end
```

### **7.2 Debug de Problema de Login**

```lua
-- Debug de problema de login
function debugLoginIssue()
    local steps = {
        "Verificar conectividade de rede",
        "Verificar credenciais",
        "Verificar servidor",
        "Verificar protocolo",
        "Verificar cache"
    }
    
    for i, step in ipairs(steps) do
        print("Passo " .. i .. ": " .. step)
        local result = executeDebugStep(step)
        if not result.success then
            return "Falha no passo " .. i .. ": " .. result.error
        end
    end
    
    return "Login debug concluído com sucesso"
end

function executeDebugStep(step)
    if step == "Verificar conectividade de rede" then
        return {success = g_game.isOnline()}
    elseif step == "Verificar credenciais" then
        return {success = g_game.getAccountName() ~= ""}
    -- ... outros passos
    end
    
    return {success = true}
end
```

---

## 🔄 **8. Integração com Sistema de Debug**

### **8.1 Uso com CORE-007**

Este guia complementa o sistema de debug documentado no **CORE-007**, fornecendo:

- ✅ Técnicas avançadas de debugging
- ✅ Ferramentas customizadas
- ✅ Metodologias estruturadas
- ✅ Casos de uso práticos
- ✅ Melhores práticas

### **8.2 Benefícios para Agentes**

- **Autonomia**: Agentes podem debugar problemas complexos
- **Eficiência**: Metodologias estruturadas aceleram resolução
- **Qualidade**: Ferramentas avançadas melhoram diagnóstico
- **Documentação**: Casos práticos facilitam aprendizado

---

## 📊 **Status do Guia**

### **✅ Concluído:**
- ✅ Ferramentas de debug avançadas
- ✅ Metodologias estruturadas
- ✅ Casos de uso específicos
- ✅ Ferramentas customizadas
- ✅ Análise avançada
- ✅ Melhores práticas
- ✅ Exemplos práticos
- ✅ Integração com CORE-007

### **🎯 Próximo:**
- 🔄 GUIDE-005: Guia de Performance e Otimização

---

**Guia Criado**: 2025-01-27  
**Responsável**: Sistema de Task Manager  
**Status**: ✅ **COMPLETO**  
**Próximo**: 🔥 **GUIDE-005 - Performance e Otimização** 