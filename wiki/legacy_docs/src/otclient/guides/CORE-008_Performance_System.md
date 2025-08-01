
# CORE-008: Sistema de Performance

<div class="info"> **Sistema Completo de Performance e Otimização**
> Documentação completa do sistema de performance do OTClient, incluindo otimização de memória, CPU, GPU, profiling avançado e técnicas de melhoria de performance para desenvolvimento eficiente.

## 📋 Índice
- [#Visão Geral](#Visão Geral.md)
- [#Sistema de Profiling](#Sistema de Profiling.md)
- [#Otimização de Memória](#Otimização de Memória.md)
- [#Otimização de CPU](#Otimização de CPU.md)
- [#Otimização de GPU](#Otimização de GPU.md)
- [#Monitor de Performance](#Monitor de Performance.md)
- [#Técnicas de Otimização](#Técnicas de Otimização.md)
- [#Exemplos Práticos](#Exemplos Práticos.md)
- [#Melhores Práticas](#Melhores Práticas.md)

---

## 🎯 Visão Geral

O sistema de performance do OTClient oferece ferramentas completas para otimização e monitoramento:

### **⚡ Componentes Principais:**
- **Profiling Avançado**: Análise detalhada de performance
- **Otimização de Memória**: Gerenciamento eficiente de memória
- **Otimização de CPU**: Redução de carga de processamento
- **Otimização de GPU**: Aceleração por hardware
- **Monitor em Tempo Real**: Acompanhamento contínuo de métricas
- **Técnicas de Otimização**: Estratégias comprovadas de melhoria

### 🏗️ **Arquitetura do Sistema**

```
Sistema de Performance
   │
   ├─ Performance Profiler
   │   ├─ CPU Profiling
   │   ├─ Memory Profiling
   │   ├─ GPU Profiling
   │   └─ Network Profiling
   │
   ├─ Optimization Engine
   │   ├─ Memory Optimization
   │   ├─ CPU Optimization
   │   ├─ GPU Optimization
   │   └─ Cache Optimization
   │
   ├─ Performance Monitor
   │   ├─ Real-time Metrics
   │   ├─ Performance Alerts
   │   ├─ Performance Reports
   │   └─ Trend Analysis
   │
   └─ Optimization Tools
       ├─ Code Analyzer
       ├─ Memory Leak Detector
       ├─ Performance Advisor
       └─ Optimization Suggestions
```

---

## 📊 Sistema de Profiling

### 🎯 **Profiling de CPU**

```lua
-- Sistema de profiling de CPU
local CPUProfiler = {}

CPUProfiler.functions = {}
CPUProfiler.callStack = {}
CPUProfiler.enabled = false

function CPUProfiler.start()
    CPUProfiler.enabled = true
    CPUProfiler.functions = {}
    CPUProfiler.callStack = {}
    print("CPU Profiler iniciado")
end

function CPUProfiler.stop()
    CPUProfiler.enabled = false
    CPUProfiler.generateReport()
end

function CPUProfiler.profileFunction(funcName, func)
    if not CPUProfiler.enabled then
        return func
    end
    
    return function(...)
        local startTime = g_clock.millis()
        local startMemory = collectgarbage("count")
        
        -- Adicionar à pilha de chamadas
        table.insert(CPUProfiler.callStack, funcName)
        
        -- Executar função
        local result = func(...)
        
        -- Remover da pilha
        table.remove(CPUProfiler.callStack)
        
        -- Calcular métricas
        local endTime = g_clock.millis()
        local endMemory = collectgarbage("count")
        
        local duration = endTime - startTime
        local memoryDelta = endMemory - startMemory
        
        -- Registrar métricas
        if not CPUProfiler.functions[funcName] then
            CPUProfiler.functions[funcName] = {
                calls = 0,
                totalTime = 0,
                totalMemory = 0,
                minTime = math.huge,
                maxTime = 0,
                avgTime = 0
            }
        end
        
        local stats = CPUProfiler.functions[funcName]
        stats.calls = stats.calls + 1
        stats.totalTime = stats.totalTime + duration
        stats.totalMemory = stats.totalMemory + memoryDelta
        stats.minTime = math.min(stats.minTime, duration)
        stats.maxTime = math.max(stats.maxTime, duration)
        stats.avgTime = stats.totalTime / stats.calls
        
        return result
    end
end

function CPUProfiler.generateReport()
    print("=== CPU Profiler Report ===")
    
    -- Ordenar funções por tempo total
    local sortedFunctions = {}
    for funcName, stats in pairs(CPUProfiler.functions) do
        table.insert(sortedFunctions, {name = funcName, stats = stats})
    end
    
    table.sort(sortedFunctions, function(a, b)
        return a.stats.totalTime > b.stats.totalTime
    end)
    
    -- Exibir top 10 funções mais lentas
    for i = 1, math.min(10, #sortedFunctions) do
        local func = sortedFunctions[i]
        local stats = func.stats
        
        print(string.format("%d. %s", i, func.name))
        print(string.format("   Calls: %d", stats.calls))
        print(string.format("   Total Time: %dms", stats.totalTime))
        print(string.format("   Avg Time: %.2fms", stats.avgTime))
        print(string.format("   Min/Max: %dms/%dms", stats.minTime, stats.maxTime))
        print(string.format("   Memory Delta: %.2f KB", stats.totalMemory))
        print()
    end
end
```

### 🧠 **Profiling de Memória**

```lua
-- Sistema de profiling de memória
local MemoryProfiler = {}

MemoryProfiler.snapshots = {}
MemoryProfiler.enabled = false
MemoryProfiler.autoSnapshot = false
MemoryProfiler.snapshotInterval = 5000  -- 5 segundos

function MemoryProfiler.start()
    MemoryProfiler.enabled = true
    MemoryProfiler.snapshots = {}
    MemoryProfiler.lastSnapshot = g_clock.millis()
    print("Memory Profiler iniciado")
end

function MemoryProfiler.stop()
    MemoryProfiler.enabled = false
    MemoryProfiler.generateMemoryReport()
end

function MemoryProfiler.takeSnapshot(name)
    if not MemoryProfiler.enabled then
        return
    end
    
    local memory = collectgarbage("count")
    local timestamp = g_clock.millis()
    
    MemoryProfiler.snapshots[name] = {
        memory = memory,
        timestamp = timestamp,
        uptime = timestamp
    }
    
    print(string.format("Memory Snapshot [%s]: %.2f KB", name, memory))
    return memory
end

function MemoryProfiler.autoSnapshotUpdate()
    if not MemoryProfiler.enabled or not MemoryProfiler.autoSnapshot then
        return
    end
    
    local currentTime = g_clock.millis()
    if currentTime - MemoryProfiler.lastSnapshot >= MemoryProfiler.snapshotInterval then
        MemoryProfiler.takeSnapshot("auto_" .. os.date("%H:%M:%S"))
        MemoryProfiler.lastSnapshot = currentTime
    end
end

function MemoryProfiler.detectMemoryLeaks()
    print("=== Memory Leak Detection ===")
    
    local snapshots = MemoryProfiler.snapshots
    local snapshotNames = {}
    
    for name, _ in pairs(snapshots) do
        table.insert(snapshotNames, name)
    end
    
    table.sort(snapshotNames)
    
    for i = 2, #snapshotNames do
        local prevName = snapshotNames[i-1]
        local currName = snapshotNames[i]
        
        local prevMemory = snapshots[prevName].memory
        local currMemory = snapshots[currName].memory
        
        local memoryDiff = currMemory - prevMemory
        local timeDiff = snapshots[currName].timestamp - snapshots[prevName].timestamp
        
        if memoryDiff > 1000 then  -- Mais de 1MB de crescimento
            print(string.format("Potential Memory Leak: %s -> %s", prevName, currName))
            print(string.format("  Memory Growth: %.2f KB", memoryDiff))
            print(string.format("  Time Elapsed: %dms", timeDiff))
            print(string.format("  Growth Rate: %.2f KB/s", memoryDiff / (timeDiff / 1000)))
            print()
        end
    end
end
```

---

## 🧠 Otimização de Memória

### 🎯 **Gerenciamento de Memória**

```lua
-- Sistema de otimização de memória
local MemoryOptimizer = {}

MemoryOptimizer.cache = {}
MemoryOptimizer.cacheSize = 100
MemoryOptimizer.enabled = true

function MemoryOptimizer.init()
    MemoryOptimizer.setupMemoryOptimization()
    MemoryOptimizer.startMemoryMonitor()
end

function MemoryOptimizer.setupMemoryOptimization()
    -- Configurar coleta de lixo agressiva
    collectgarbage("setpause", 110)  -- Mais agressivo
    collectgarbage("setstepmul", 200)  -- Passos maiores
    
    -- Configurar cache inteligente
    MemoryOptimizer.cache = {}
    MemoryOptimizer.cacheSize = g_settings.getNumber("performance.cacheSize", 100)
end

function MemoryOptimizer.startMemoryMonitor()
    -- Monitor de memória em tempo real
    connect(g_app, 'onRun', function()
        MemoryOptimizer.monitorMemory()
    end)
end

function MemoryOptimizer.monitorMemory()
    local memory = collectgarbage("count")
    
    -- Alertas de memória alta
    if memory > 50000 then  -- 50MB
        print("WARNING: High memory usage detected: " .. memory .. " KB")
        MemoryOptimizer.optimizeMemory()
    end
    
    -- Limpeza automática de cache
    if memory > 30000 then  -- 30MB
        MemoryOptimizer.cleanCache()
    end
end

function MemoryOptimizer.optimizeMemory()
    print("Executando otimização de memória...")
    
    -- Forçar coleta de lixo
    collectgarbage("collect")
    
    -- Limpar cache
    MemoryOptimizer.cleanCache()
    
    -- Limpar recursos não utilizados
    MemoryOptimizer.cleanUnusedResources()
    
    local newMemory = collectgarbage("count")
    print("Otimização concluída. Memória: " .. newMemory .. " KB")
end

function MemoryOptimizer.cleanCache()
    -- Limpar cache antigo
    local currentTime = g_clock.millis()
    local toRemove = {}
    
    for key, item in pairs(MemoryOptimizer.cache) do
        if currentTime - item.timestamp > 300000 then  -- 5 minutos
            table.insert(toRemove, key)
        end
    end
    
    for _, key in ipairs(toRemove) do
        MemoryOptimizer.cache[key] = nil
    end
    
    -- Manter apenas os itens mais recentes
    local cacheSize = MemoryOptimizer.cacheSize
    local cacheItems = {}
    
    for key, item in pairs(MemoryOptimizer.cache) do
        table.insert(cacheItems, {key = key, timestamp = item.timestamp})
    end
    
    table.sort(cacheItems, function(a, b)
        return a.timestamp > b.timestamp
    end)
    
    for i = cacheSize + 1, #cacheItems do
        MemoryOptimizer.cache[cacheItems[i].key] = nil
    end
end

function MemoryOptimizer.cleanUnusedResources()
    -- Limpar recursos gráficos não utilizados
    if g_graphics then
        g_graphics.cleanUnusedTextures()
        g_graphics.cleanUnusedShaders()
    end
    
    -- Limpar recursos de áudio não utilizados
    if g_sounds then
        g_sounds.cleanUnusedSounds()
    end
end
```

### 🔄 **Cache Inteligente**

```lua
-- Sistema de cache inteligente
local SmartCache = {}

SmartCache.cache = {}
SmartCache.maxSize = 100
SmartCache.enabled = true

function SmartCache.get(key, generator, ttl)
    if not SmartCache.enabled then
        return generator()
    end
    
    local item = SmartCache.cache[key]
    local currentTime = g_clock.millis()
    
    -- Verificar se item existe e não expirou
    if item and (not ttl or currentTime - item.timestamp < ttl) then
        item.accessCount = item.accessCount + 1
        item.lastAccess = currentTime
        return item.value
    end
    
    -- Gerar novo valor
    local value = generator()
    
    -- Armazenar no cache
    SmartCache.cache[key] = {
        value = value,
        timestamp = currentTime,
        lastAccess = currentTime,
        accessCount = 1
    }
    
    -- Verificar tamanho do cache
    SmartCache.checkCacheSize()
    
    return value
end

function SmartCache.checkCacheSize()
    local cacheSize = 0
    for _ in pairs(SmartCache.cache) do
        cacheSize = cacheSize + 1
    end
    
    if cacheSize > SmartCache.maxSize then
        SmartCache.evictLeastUsed()
    end
end

function SmartCache.evictLeastUsed()
    local items = {}
    
    for key, item in pairs(SmartCache.cache) do
        table.insert(items, {
            key = key,
            score = item.accessCount / (g_clock.millis() - item.lastAccess + 1)
        })
    end
    
    table.sort(items, function(a, b)
        return a.score < b.score
    end)
    
    -- Remover 20% dos itens menos usados
    local toRemove = math.floor(#items * 0.2)
    for i = 1, toRemove do
        SmartCache.cache[items[i].key] = nil
    end
end
```

---

## ⚡ Otimização de CPU

### 🎯 **Otimização de Loops**

```lua
-- Sistema de otimização de CPU
local CPUOptimizer = {}

CPUOptimizer.frameBudget = 16  -- 60 FPS = 16ms por frame
CPUOptimizer.enabled = true

function CPUOptimizer.init()
    CPUOptimizer.setupFrameBudget()
    CPUOptimizer.startFrameMonitor()
end

function CPUOptimizer.setupFrameBudget()
    -- Configurar orçamento de frame
    CPUOptimizer.frameBudget = g_settings.getNumber("performance.frameBudget", 16)
    
    -- Configurar otimizações automáticas
    CPUOptimizer.enabled = g_settings.getBoolean("performance.cpuOptimization", true)
end

function CPUOptimizer.startFrameMonitor()
    -- Monitor de frame em tempo real
    connect(g_app, 'onRun', function()
        CPUOptimizer.monitorFrameTime()
    end)
end

function CPUOptimizer.monitorFrameTime()
    local frameTime = g_app.getFrameTime()
    
    if frameTime > CPUOptimizer.frameBudget then
        print("WARNING: Frame time exceeded budget: " .. frameTime .. "ms")
        CPUOptimizer.optimizeFrame()
    end
end

function CPUOptimizer.optimizeFrame()
    -- Reduzir qualidade visual temporariamente
    if g_graphics then
        g_graphics.setQuality("low")
    end
    
    -- Reduzir frequência de atualizações
    CPUOptimizer.reduceUpdateFrequency()
    
    -- Limpar operações desnecessárias
    CPUOptimizer.cleanUnnecessaryOperations()
end

function CPUOptimizer.reduceUpdateFrequency()
    -- Reduzir frequência de atualizações de UI
    if g_ui then
        g_ui.setUpdateFrequency(30)  -- 30 FPS para UI
    end
    
    -- Reduzir frequência de atualizações de rede
    if g_game then
        g_game.setNetworkUpdateFrequency(10)  -- 10 updates por segundo
    end
end

function CPUOptimizer.cleanUnnecessaryOperations()
    -- Cancelar operações não críticas
    CPUOptimizer.cancelNonCriticalOperations()
    
    -- Reduzir complexidade de cálculos
    CPUOptimizer.simplifyCalculations()
end
```

### 🔄 **Processamento Assíncrono**

```lua
-- Sistema de processamento assíncrono
local AsyncProcessor = {}

AsyncProcessor.tasks = {}
AsyncProcessor.maxConcurrent = 4
AsyncProcessor.enabled = true

function AsyncProcessor.init()
    AsyncProcessor.setupAsyncProcessing()
end

function AsyncProcessor.setupAsyncProcessing()
    AsyncProcessor.maxConcurrent = g_settings.getNumber("performance.maxConcurrentTasks", 4)
    AsyncProcessor.enabled = g_settings.getBoolean("performance.asyncProcessing", true)
end

function AsyncProcessor.addTask(task, priority)
    if not AsyncProcessor.enabled then
        task()  -- Executar síncrono
        return
    end
    
    table.insert(AsyncProcessor.tasks, {
        task = task,
        priority = priority or 0,
        timestamp = g_clock.millis()
    })
    
    -- Ordenar por prioridade
    table.sort(AsyncProcessor.tasks, function(a, b)
        return a.priority > b.priority
    end)
end

function AsyncProcessor.processTasks()
    if #AsyncProcessor.tasks == 0 then
        return
    end
    
    local processed = 0
    local maxProcessed = AsyncProcessor.maxConcurrent
    
    while #AsyncProcessor.tasks > 0 and processed < maxProcessed do
        local taskData = table.remove(AsyncProcessor.tasks, 1)
        
        -- Executar tarefa
        local success, error = pcall(taskData.task)
        
        if not success then
            print("Async task error: " .. tostring(error))
        end
        
        processed = processed + 1
    end
end

-- Exemplo de uso
function AsyncProcessor.example()
    -- Tarefa de alta prioridade
    AsyncProcessor.addTask(function()
        -- Processamento pesado
        local result = heavyComputation()
        print("Heavy computation completed: " .. result)
    end, 10)
    
    -- Tarefa de baixa prioridade
    AsyncProcessor.addTask(function()
        -- Limpeza de dados
        cleanupOldData()
    end, 1)
end
```

---

## 🎮 Otimização de GPU

### 🎯 **Otimização de Renderização**

```lua
-- Sistema de otimização de GPU
local GPUOptimizer = {}

GPUOptimizer.enabled = true
GPUOptimizer.qualityLevel = "high"
GPUOptimizer.maxDrawCalls = 1000

function GPUOptimizer.init()
    GPUOptimizer.setupGPUOptimization()
    GPUOptimizer.startGPUMonitor()
end

function GPUOptimizer.setupGPUOptimization()
    -- Configurar qualidade baseada no hardware
    GPUOptimizer.qualityLevel = g_settings.getString("performance.gpuQuality", "high")
    GPUOptimizer.maxDrawCalls = g_settings.getNumber("performance.maxDrawCalls", 1000)
    
    -- Configurar otimizações de GPU
    if g_graphics then
        GPUOptimizer.configureGraphics()
    end
end

function GPUOptimizer.configureGraphics()
    local quality = GPUOptimizer.qualityLevel
    
    if quality == "low" then
        g_graphics.setTextureQuality("low")
        g_graphics.setShaderQuality("low")
        g_graphics.setAntiAliasing(false)
        g_graphics.setShadowQuality("none")
    elseif quality == "medium" then
        g_graphics.setTextureQuality("medium")
        g_graphics.setShaderQuality("medium")
        g_graphics.setAntiAliasing(true)
        g_graphics.setShadowQuality("low")
    elseif quality == "high" then
        g_graphics.setTextureQuality("high")
        g_graphics.setShaderQuality("high")
        g_graphics.setAntiAliasing(true)
        g_graphics.setShadowQuality("high")
    end
end

function GPUOptimizer.startGPUMonitor()
    -- Monitor de GPU em tempo real
    connect(g_app, 'onRun', function()
        GPUOptimizer.monitorGPU()
    end)
end

function GPUOptimizer.monitorGPU()
    if not g_graphics then
        return
    end
    
    local drawCalls = g_graphics.getDrawCalls()
    local gpuTime = g_graphics.getGPUTime()
    
    -- Alertas de GPU sobrecarregada
    if drawCalls > GPUOptimizer.maxDrawCalls then
        print("WARNING: High GPU draw calls: " .. drawCalls)
        GPUOptimizer.optimizeGPU()
    end
    
    if gpuTime > 16 then  -- Mais de 16ms
        print("WARNING: High GPU time: " .. gpuTime .. "ms")
        GPUOptimizer.optimizeGPU()
    end
end

function GPUOptimizer.optimizeGPU()
    -- Reduzir qualidade visual
    GPUOptimizer.reduceVisualQuality()
    
    -- Otimizar renderização
    GPUOptimizer.optimizeRendering()
    
    -- Limpar recursos GPU
    GPUOptimizer.cleanGPUResources()
end

function GPUOptimizer.reduceVisualQuality()
    -- Reduzir qualidade de texturas
    g_graphics.setTextureQuality("medium")
    
    -- Desabilitar efeitos visuais
    g_graphics.setPostProcessing(false)
    g_graphics.setBloom(false)
    g_graphics.setMotionBlur(false)
    
    -- Reduzir distância de renderização
    g_graphics.setRenderDistance(50)
end

function GPUOptimizer.optimizeRendering()
    -- Usar instancing para objetos similares
    g_graphics.enableInstancing(true)
    
    -- Otimizar culling
    g_graphics.setCullingOptimization(true)
    
    -- Reduzir complexidade de shaders
    g_graphics.setShaderComplexity("low")
end

function GPUOptimizer.cleanGPUResources()
    -- Limpar texturas não utilizadas
    g_graphics.cleanUnusedTextures()
    
    -- Limpar shaders não utilizados
    g_graphics.cleanUnusedShaders()
    
    -- Limpar buffers não utilizados
    g_graphics.cleanUnusedBuffers()
end
```

---

## 📊 Monitor de Performance

### 🎯 **Monitor em Tempo Real**

```lua
-- Sistema de monitor de performance
local PerformanceMonitor = {}

PerformanceMonitor.enabled = false
PerformanceMonitor.interval = 1000  -- 1 segundo
PerformanceMonitor.lastUpdate = 0
PerformanceMonitor.metrics = {}

function PerformanceMonitor.start()
    PerformanceMonitor.enabled = true
    PerformanceMonitor.lastUpdate = g_clock.millis()
    PerformanceMonitor.metrics = {}
    print("Performance Monitor iniciado")
end

function PerformanceMonitor.stop()
    PerformanceMonitor.enabled = false
    PerformanceMonitor.generateFinalReport()
end

function PerformanceMonitor.update()
    if not PerformanceMonitor.enabled then
        return
    end
    
    local currentTime = g_clock.millis()
    if currentTime - PerformanceMonitor.lastUpdate >= PerformanceMonitor.interval then
        PerformanceMonitor.collectMetrics()
        PerformanceMonitor.lastUpdate = currentTime
    end
end

function PerformanceMonitor.collectMetrics()
    local metrics = {
        timestamp = g_clock.millis(),
        fps = g_app.getFps(),
        memory = collectgarbage("count"),
        cpu = PerformanceMonitor.getCPUUsage(),
        gpu = PerformanceMonitor.getGPUUsage(),
        network = PerformanceMonitor.getNetworkUsage()
    }
    
    table.insert(PerformanceMonitor.metrics, metrics)
    
    -- Manter apenas últimas 100 métricas
    if #PerformanceMonitor.metrics > 100 then
        table.remove(PerformanceMonitor.metrics, 1)
    end
    
    -- Verificar alertas
    PerformanceMonitor.checkAlerts(metrics)
end

function PerformanceMonitor.checkAlerts(metrics)
    -- Alerta de FPS baixo
    if metrics.fps < 30 then
        print("ALERT: Low FPS detected: " .. metrics.fps)
    end
    
    -- Alerta de memória alta
    if metrics.memory > 50000 then
        print("ALERT: High memory usage: " .. metrics.memory .. " KB")
    end
    
    -- Alerta de CPU alta
    if metrics.cpu > 80 then
        print("ALERT: High CPU usage: " .. metrics.cpu .. "%")
    end
end

function PerformanceMonitor.generateFinalReport()
    if #PerformanceMonitor.metrics == 0 then
        return
    end
    
    print("=== Performance Monitor Final Report ===")
    
    -- Calcular médias
    local avgFPS = 0
    local avgMemory = 0
    local avgCPU = 0
    
    for _, metrics in ipairs(PerformanceMonitor.metrics) do
        avgFPS = avgFPS + metrics.fps
        avgMemory = avgMemory + metrics.memory
        avgCPU = avgCPU + metrics.cpu
    end
    
    avgFPS = avgFPS / #PerformanceMonitor.metrics
    avgMemory = avgMemory / #PerformanceMonitor.metrics
    avgCPU = avgCPU / #PerformanceMonitor.metrics
    
    print(string.format("Average FPS: %.2f", avgFPS))
    print(string.format("Average Memory: %.2f KB", avgMemory))
    print(string.format("Average CPU: %.2f%%", avgCPU))
    
    -- Encontrar picos
    local minFPS = math.huge
    local maxMemory = 0
    local maxCPU = 0
    
    for _, metrics in ipairs(PerformanceMonitor.metrics) do
        minFPS = math.min(minFPS, metrics.fps)
        maxMemory = math.max(maxMemory, metrics.memory)
        maxCPU = math.max(maxCPU, metrics.cpu)
    end
    
    print(string.format("Min FPS: %.2f", minFPS))
    print(string.format("Max Memory: %.2f KB", maxMemory))
    print(string.format("Max CPU: %.2f%%", maxCPU))
end
```

---

## 🛠️ Técnicas de Otimização

### 🎯 **Otimização de Código**

```lua
-- Técnicas de otimização de código
local CodeOptimizer = {}

function CodeOptimizer.optimizeLuaCode()
    -- 1. Usar local em vez de global
    local optimizedFunction = function()
        local localVar = 10  -- Mais rápido que global
        return localVar * 2
    end
    
    -- 2. Evitar criação de tabelas em loops
    local optimizedLoop = function()
        local result = {}
        for i = 1, 1000 do
            result[i] = i * 2  -- Pré-alocar tabela
        end
        return result
    end
    
    -- 3. Usar ipairs em vez de pairs quando possível
    local optimizedIteration = function(t)
        for i, v in ipairs(t) do  -- Mais rápido que pairs
            -- Processar valor
        end
    end
    
    -- 4. Evitar concatenação de strings em loops
    local optimizedString = function()
        local parts = {}
        for i = 1, 100 do
            table.insert(parts, tostring(i))
        end
        return table.concat(parts)  -- Mais eficiente
    end
    
    return {
        optimizedFunction = optimizedFunction,
        optimizedLoop = optimizedLoop,
        optimizedIteration = optimizedIteration,
        optimizedString = optimizedString
    }
end

function CodeOptimizer.optimizeDataStructures()
    -- 1. Usar tabelas com índices numéricos
    local optimizedTable = {}
    for i = 1, 100 do
        optimizedTable[i] = i  -- Índices numéricos são mais rápidos
    end
    
    -- 2. Pré-alocar tabelas quando possível
    local preallocatedTable = {}
    for i = 1, 1000 do
        preallocatedTable[i] = 0
    end
    
    -- 3. Usar metatables para otimização
    local optimizedMetatable = {
        __index = function(t, k)
            return rawget(t, k) or 0
        end
    }
    
    return {
        optimizedTable = optimizedTable,
        preallocatedTable = preallocatedTable,
        optimizedMetatable = optimizedMetatable
    }
end
```

---

## 💡 Exemplos Práticos

### 🎯 **Exemplo de Uso Completo**

```lua
-- Exemplo completo de uso do sistema de performance
function setupPerformanceSystem()
    -- Inicializar sistema de profiling
    CPUProfiler.start()
    MemoryProfiler.start()
    
    -- Inicializar otimizadores
    MemoryOptimizer.init()
    CPUOptimizer.init()
    GPUOptimizer.init()
    
    -- Inicializar processamento assíncrono
    AsyncProcessor.init()
    
    -- Inicializar cache inteligente
    SmartCache.enabled = true
    
    -- Inicializar monitor de performance
    PerformanceMonitor.start()
    
    print("Sistema de performance inicializado com sucesso")
end

-- Exemplo de otimização de função
function optimizedFunction()
    -- Usar profiling
    CPUProfiler.startTimer("optimizedFunction")
    MemoryProfiler.takeSnapshot("before")
    
    -- Usar cache inteligente
    local result = SmartCache.get("expensiveCalculation", function()
        return expensiveCalculation()
    end, 60000)  -- Cache por 1 minuto
    
    -- Usar processamento assíncrono para tarefas não críticas
    AsyncProcessor.addTask(function()
        cleanupOldData()
    end, 1)  -- Baixa prioridade
    
    -- Finalizar profiling
    CPUProfiler.endTimer("optimizedFunction")
    MemoryProfiler.takeSnapshot("after")
    
    return result
end

-- Exemplo de monitoramento contínuo
function continuousMonitoring()
    -- Atualizar monitores
    PerformanceMonitor.update()
    MemoryProfiler.autoSnapshotUpdate()
    
    -- Verificar otimizações necessárias
    if collectgarbage("count") > 30000 then
        MemoryOptimizer.optimizeMemory()
    end
    
    if g_app.getFps() < 30 then
        GPUOptimizer.optimizeGPU()
    end
end
```

---

## ✅ Melhores Práticas

### 🎯 **Recomendações de Performance**

1. **Otimização de Memória**
   - Use `local` em vez de variáveis globais
   - Limpe tabelas não utilizadas
   - Use cache inteligente para dados caros
   - Monitore vazamentos de memória

2. **Otimização de CPU**
   - Evite loops desnecessários
   - Use processamento assíncrono
   - Otimize algoritmos críticos
   - Monitore tempo de frame

3. **Otimização de GPU**
   - Reduza draw calls
   - Use instancing quando possível
   - Otimize shaders
   - Monitore tempo de GPU

4. **Profiling**
   - Use profiling regularmente
   - Monitore métricas em tempo real
   - Identifique gargalos
   - Otimize baseado em dados

### 🚨 **Considerações Importantes**

- **Balanceamento**: Equilibre qualidade visual e performance
- **Adaptação**: Adapte qualidade baseada no hardware
- **Monitoramento**: Monitore continuamente
- **Otimização**: Otimize proativamente, não reativamente

---

## 📊 Métricas e KPIs

### 📈 **Indicadores de Performance**

- **FPS**: Frames por segundo (meta: >30)
- **Memory Usage**: Uso de memória em KB (meta: <50MB)
- **CPU Usage**: Uso de CPU em % (meta: <80%)
- **GPU Time**: Tempo de GPU em ms (meta: <16ms)
- **Load Time**: Tempo de carregamento em ms (meta: <1000ms)

### 🔍 **Relatórios de Performance**

```json
{
  "timestamp": "2025-01-27T10:30:00Z",
  "metrics": {
    "fps": 60,
    "memory": 25000,
    "cpu": 45,
    "gpu": 12,
    "loadTime": 800
  },
  "optimizations": {
    "memoryOptimized": true,
    "gpuOptimized": false,
    "cacheHitRate": 0.85
  }
}
```

---

**Story ID**: CORE-008  
**Categoria**: CORE  
**Status**: ✅ Completo  
**Última Atualização**: 2025-01-27 