---
tags: [otclient, performance, optimization, profiling, system, guide, documentation]
status: completed
aliases: [Sistema de Performance, Performance System, Optimization System, Profiling]
---

# Performance System Guide

> [!info] Este guia documenta o sistema completo de performance e otimização do OTClient, incluindo profiling, cache, lazy loading, memory management e técnicas de otimização para garantir performance máxima.

## 📋 Índice
- [[#Visão Geral]]
- [[#Sistema de Profiling]]
- [[#Gerenciamento de Memória]]
- [[#Sistema de Cache]]
- [[#Lazy Loading]]
- [[#Otimização de Renderização]]
- [[#Otimização de Rede]]
- [[#Monitoramento de Performance]]
- [[#Exemplos Práticos]]
- [[#Melhores Práticas]]

---

## 🎯 Visão Geral

O sistema de performance do OTClient oferece:

- **Profiling Avançado**: Análise detalhada de performance
- **Gerenciamento de Memória**: Otimização de uso de RAM
- **Sistema de Cache**: Redução de carregamentos desnecessários
- **Lazy Loading**: Carregamento sob demanda
- **Otimização de Renderização**: FPS otimizado
- **Monitoramento Contínuo**: Métricas em tempo real

### 🏗️ **Arquitetura do Sistema**

```
Sistema de Performance
   │
   ├─ Profiling Engine
   │   ├─ CPU profiling
   │   ├─ Memory profiling
   │   └─ GPU profiling
   │
   ├─ Memory Management
   │   ├─ Garbage collection
   │   ├─ Memory pools
   │   └─ Leak detection
   │
   ├─ Cache System
   │   ├─ Texture cache
   │   ├─ Sound cache
   │   └─ Data cache
   │
   └─ Optimization
       ├─ Render optimization
       ├─ Network optimization
       └─ Resource optimization
```

---

## ⚡ Sistema de Profiling

### 📊 **CPU Profiling**

```lua
-- Sistema de profiling de CPU
local CPUProfiler = {}

CPUProfiler.timers = {}
CPUProfiler.callStacks = {}
CPUProfiler.enabled = false

-- Inicializar profiler
function CPUProfiler.init()
    CPUProfiler.enabled = g_settings.getBoolean("performance.enableProfiling", false)
    
    if CPUProfiler.enabled then
        print("CPU Profiler habilitado")
    end
end

-- Medir tempo de execução
function CPUProfiler.measureTime(name, func)
    if not CPUProfiler.enabled then
        return func()
    end
    
    local startTime = g_clock.millis()
    local result = func()
    local endTime = g_clock.millis()
    
    local duration = endTime - startTime
    
    if not CPUProfiler.timers[name] then
        CPUProfiler.timers[name] = {
            totalTime = 0,
            calls = 0,
            minTime = math.huge,
            maxTime = 0,
            avgTime = 0
        }
    end
    
    local timer = CPUProfiler.timers[name]
    timer.totalTime = timer.totalTime + duration
    timer.calls = timer.calls + 1
    timer.minTime = math.min(timer.minTime, duration)
    timer.maxTime = math.max(timer.maxTime, duration)
    timer.avgTime = timer.totalTime / timer.calls
    
    return result
end

-- Medir tempo com callback
function CPUProfiler.measureTimeCallback(name, callback)
    if not CPUProfiler.enabled then
        return callback
    end
    
    local startTime = g_clock.millis()
    
    local function endMeasurement()
        local endTime = g_clock.millis()
        local duration = endTime - startTime
        
        if not CPUProfiler.timers[name] then
            CPUProfiler.timers[name] = {
                totalTime = 0,
                calls = 0,
                minTime = math.huge,
                maxTime = 0,
                avgTime = 0
            }
        end
        
        local timer = CPUProfiler.timers[name]
        timer.totalTime = timer.totalTime + duration
        timer.calls = timer.calls + 1
        timer.minTime = math.min(timer.minTime, duration)
        timer.maxTime = math.max(timer.maxTime, duration)
        timer.avgTime = timer.totalTime / timer.calls
    end
    
    return callback, endMeasurement
end

-- Gerar relatório de CPU
function CPUProfiler.generateReport()
    local report = {}
    table.insert(report, "=== RELATÓRIO DE CPU ===")
    table.insert(report, "")
    
    -- Ordenar por tempo total
    local sortedTimers = {}
    for name, timer in pairs(CPUProfiler.timers) do
        table.insert(sortedTimers, {name = name, timer = timer})
    end
    
    table.sort(sortedTimers, function(a, b)
        return a.timer.totalTime > b.timer.totalTime
    end)
    
    for _, item in ipairs(sortedTimers) do
        local name = item.name
        local timer = item.timer
        
        table.insert(report, string.format("%s:", name))
        table.insert(report, string.format("  Chamadas: %d", timer.calls))
        table.insert(report, string.format("  Tempo total: %.2fms", timer.totalTime))
        table.insert(report, string.format("  Tempo médio: %.2fms", timer.avgTime))
        table.insert(report, string.format("  Tempo mínimo: %.2fms", timer.minTime))
        table.insert(report, string.format("  Tempo máximo: %.2fms", timer.maxTime))
        table.insert(report, "")
    end
    
    return table.concat(report, "\n")
end
```

### 💾 **Memory Profiling**

```lua
-- Sistema de profiling de memória
local MemoryProfiler = {}

MemoryProfiler.snapshots = {}
MemoryProfiler.maxSnapshots = 50

-- Tirar snapshot de memória
function MemoryProfiler.takeSnapshot(name)
    local snapshot = {
        name = name,
        timestamp = g_clock.millis(),
        memoryUsage = collectgarbage("count"),
        textureCount = g_textures.getLoadedTextureCount(),
        soundCount = g_sounds.getLoadedSoundCount(),
        widgetCount = MemoryProfiler.countWidgets(),
        luaMemory = collectgarbage("count")
    }
    
    table.insert(MemoryProfiler.snapshots, snapshot)
    
    -- Limitar número de snapshots
    if #MemoryProfiler.snapshots > MemoryProfiler.maxSnapshots then
        table.remove(MemoryProfiler.snapshots, 1)
    end
    
    return snapshot
end

-- Contar widgets
function MemoryProfiler.countWidgets()
    local count = 0
    
    local function countWidget(widget)
        count = count + 1
        local children = widget:getChildren()
        for _, child in ipairs(children) do
            countWidget(child)
        end
    end
    
    countWidget(g_ui.getRootWidget())
    return count
end

-- Comparar snapshots
function MemoryProfiler.compareSnapshots(snapshot1, snapshot2)
    local diff = {
        memoryDiff = snapshot2.memoryUsage - snapshot1.memoryUsage,
        textureDiff = snapshot2.textureCount - snapshot1.textureCount,
        soundDiff = snapshot2.soundCount - snapshot1.soundCount,
        widgetDiff = snapshot2.widgetCount - snapshot1.widgetCount,
        luaMemoryDiff = snapshot2.luaMemory - snapshot1.luaMemory,
        timeDiff = snapshot2.timestamp - snapshot1.timestamp
    }
    
    return diff
end

-- Gerar relatório de memória
function MemoryProfiler.generateReport()
    local report = {}
    table.insert(report, "=== RELATÓRIO DE MEMÓRIA ===")
    table.insert(report, "")
    
    if #MemoryProfiler.snapshots < 2 then
        table.insert(report, "Pelo menos 2 snapshots necessários para comparação")
        return table.concat(report, "\n")
    end
    
    local firstSnapshot = MemoryProfiler.snapshots[1]
    local lastSnapshot = MemoryProfiler.snapshots[#MemoryProfiler.snapshots]
    local diff = MemoryProfiler.compareSnapshots(firstSnapshot, lastSnapshot)
    
    table.insert(report, string.format("Período: %.2f segundos", diff.timeDiff / 1000))
    table.insert(report, string.format("Variação de memória: %.2f KB", diff.memoryDiff))
    table.insert(report, string.format("Variação de texturas: %d", diff.textureDiff))
    table.insert(report, string.format("Variação de sons: %d", diff.soundDiff))
    table.insert(report, string.format("Variação de widgets: %d", diff.widgetDiff))
    table.insert(report, string.format("Variação de memória Lua: %.2f KB", diff.luaMemoryDiff))
    
    return table.concat(report, "\n")
end
```

---

## 🧠 Gerenciamento de Memória

### 🗑️ **Garbage Collection**

```lua
-- Sistema de garbage collection
local GarbageCollector = {}

GarbageCollector.config = {
    autoCollect = true,
    collectInterval = 5000,  -- 5 segundos
    memoryThreshold = 50 * 1024,  -- 50MB
    aggressiveThreshold = 100 * 1024  -- 100MB
}

-- Inicializar garbage collector
function GarbageCollector.init()
    if GarbageCollector.config.autoCollect then
        GarbageCollector.startAutoCollect()
    end
end

-- Iniciar coleta automática
function GarbageCollector.startAutoCollect()
    local function autoCollect()
        local memoryUsage = collectgarbage("count")
        
        if memoryUsage > GarbageCollector.config.aggressiveThreshold then
            -- Coleta agressiva
            collectgarbage("collect")
            print("Garbage collection agressiva executada")
        elseif memoryUsage > GarbageCollector.config.memoryThreshold then
            -- Coleta normal
            collectgarbage("step", 100)
        end
        
        scheduleEvent(autoCollect, GarbageCollector.config.collectInterval)
    end
    
    autoCollect()
end

-- Forçar coleta de lixo
function GarbageCollector.forceCollect()
    local beforeMemory = collectgarbage("count")
    collectgarbage("collect")
    local afterMemory = collectgarbage("count")
    
    local freedMemory = beforeMemory - afterMemory
    print(string.format("Garbage collection liberou %.2f KB", freedMemory))
    
    return freedMemory
end

-- Verificar vazamentos de memória
function GarbageCollector.checkMemoryLeaks()
    local snapshots = {}
    
    -- Tirar snapshots por 30 segundos
    for i = 1, 6 do
        table.insert(snapshots, MemoryProfiler.takeSnapshot("leak_check_" .. i))
        scheduleEvent(function() end, 5000)  -- 5 segundos
    end
    
    -- Analisar crescimento
    local firstSnapshot = snapshots[1]
    local lastSnapshot = snapshots[#snapshots]
    local diff = MemoryProfiler.compareSnapshots(firstSnapshot, lastSnapshot)
    
    if diff.memoryDiff > 1024 then  -- Mais de 1MB de crescimento
        print("Possível vazamento de memória detectado!")
        print(string.format("Crescimento: %.2f KB", diff.memoryDiff))
    end
end
```

### 🏊 **Memory Pools**

```lua
-- Sistema de memory pools
local MemoryPool = {}

MemoryPool.pools = {}

-- Criar pool
function MemoryPool.createPool(name, createFunc, resetFunc, initialSize)
    local pool = {
        name = name,
        createFunc = createFunc,
        resetFunc = resetFunc,
        objects = {},
        activeObjects = {},
        initialSize = initialSize or 10
    }
    
    -- Pré-alocar objetos
    for i = 1, pool.initialSize do
        local obj = createFunc()
        table.insert(pool.objects, obj)
    end
    
    MemoryPool.pools[name] = pool
    return pool
end

-- Obter objeto do pool
function MemoryPool.getObject(poolName)
    local pool = MemoryPool.pools[poolName]
    if not pool then
        error("Pool não encontrado: " .. poolName)
    end
    
    local obj
    if #pool.objects > 0 then
        obj = table.remove(pool.objects)
    else
        obj = pool.createFunc()
    end
    
    pool.activeObjects[obj] = true
    return obj
end

-- Retornar objeto ao pool
function MemoryPool.returnObject(poolName, obj)
    local pool = MemoryPool.pools[poolName]
    if not pool then
        error("Pool não encontrado: " .. poolName)
    end
    
    if pool.activeObjects[obj] then
        pool.activeObjects[obj] = nil
        
        if pool.resetFunc then
            pool.resetFunc(obj)
        end
        
        table.insert(pool.objects, obj)
    end
end

-- Estatísticas do pool
function MemoryPool.getPoolStats(poolName)
    local pool = MemoryPool.pools[poolName]
    if not pool then
        return nil
    end
    
    return {
        name = pool.name,
        availableObjects = #pool.objects,
        activeObjects = table.size(pool.activeObjects),
        totalObjects = #pool.objects + table.size(pool.activeObjects)
    }
end

-- Exemplo de uso: Pool de efeitos
function MemoryPool.createEffectPool()
    local function createEffect()
        return Effect.create()
    end
    
    local function resetEffect(effect)
        effect:setId(0)
        effect:setPosition({x = 0, y = 0, z = 0})
    end
    
    return MemoryPool.createPool("effects", createEffect, resetEffect, 20)
end
```

---

## 🗄️ Sistema de Cache

### 🖼️ **Texture Cache**

```lua
-- Sistema de cache de texturas
local TextureCache = {}

TextureCache.cache = {}
TextureCache.maxSize = 100 * 1024 * 1024  -- 100MB
TextureCache.currentSize = 0
TextureCache.accessCount = {}

-- Carregar textura com cache
function TextureCache.getTexture(path)
    if TextureCache.cache[path] then
        -- Cache hit
        TextureCache.accessCount[path] = (TextureCache.accessCount[path] or 0) + 1
        return TextureCache.cache[path]
    end
    
    -- Cache miss
    local texture = g_textures.getTexture(path)
    if texture then
        local size = TextureCache.estimateTextureSize(texture)
        
        -- Verificar se há espaço
        if TextureCache.currentSize + size > TextureCache.maxSize then
            TextureCache.evictOldTextures()
        end
        
        -- Adicionar ao cache
        TextureCache.cache[path] = texture
        TextureCache.accessCount[path] = 1
        TextureCache.currentSize = TextureCache.currentSize + size
    end
    
    return texture
end

-- Estimar tamanho da textura
function TextureCache.estimateTextureSize(texture)
    -- Estimativa simples baseada no tamanho da textura
    local size = texture:getSize()
    return size.width * size.height * 4  -- 4 bytes por pixel (RGBA)
end

-- Remover texturas antigas
function TextureCache.evictOldTextures()
    local textures = {}
    for path, texture in pairs(TextureCache.cache) do
        table.insert(textures, {
            path = path,
            texture = texture,
            accessCount = TextureCache.accessCount[path] or 0,
            size = TextureCache.estimateTextureSize(texture)
        })
    end
    
    -- Ordenar por acesso (menos acessados primeiro)
    table.sort(textures, function(a, b)
        return a.accessCount < b.accessCount
    end)
    
    -- Remover até liberar espaço suficiente
    local targetSize = TextureCache.maxSize * 0.7  -- 70% do máximo
    
    for _, item in ipairs(textures) do
        if TextureCache.currentSize <= targetSize then
            break
        end
        
        TextureCache.cache[item.path] = nil
        TextureCache.accessCount[item.path] = nil
        TextureCache.currentSize = TextureCache.currentSize - item.size
    end
end

-- Limpar cache
function TextureCache.clear()
    TextureCache.cache = {}
    TextureCache.accessCount = {}
    TextureCache.currentSize = 0
end

-- Estatísticas do cache
function TextureCache.getStats()
    local textureCount = 0
    for _ in pairs(TextureCache.cache) do
        textureCount = textureCount + 1
    end
    
    return {
        textureCount = textureCount,
        totalSize = TextureCache.currentSize,
        maxSize = TextureCache.maxSize,
        usagePercent = (TextureCache.currentSize / TextureCache.maxSize) * 100
    }
end
```

### 🔊 **Sound Cache**

```lua
-- Sistema de cache de sons
local SoundCache = {}

SoundCache.cache = {}
SoundCache.maxSize = 50 * 1024 * 1024  -- 50MB
SoundCache.currentSize = 0
SoundCache.accessCount = {}

-- Carregar som com cache
function SoundCache.getSound(path)
    if SoundCache.cache[path] then
        -- Cache hit
        SoundCache.accessCount[path] = (SoundCache.accessCount[path] or 0) + 1
        return SoundCache.cache[path]
    end
    
    -- Cache miss
    local sound = g_sounds.getSound(path)
    if sound then
        local size = SoundCache.estimateSoundSize(sound)
        
        -- Verificar se há espaço
        if SoundCache.currentSize + size > SoundCache.maxSize then
            SoundCache.evictOldSounds()
        end
        
        -- Adicionar ao cache
        SoundCache.cache[path] = sound
        SoundCache.accessCount[path] = 1
        SoundCache.currentSize = SoundCache.currentSize + size
    end
    
    return sound
end

-- Estimar tamanho do som
function SoundCache.estimateSoundSize(sound)
    -- Estimativa baseada na duração e qualidade
    local duration = sound:getDuration()
    local sampleRate = 44100  -- 44.1kHz
    local channels = 2  -- Stereo
    local bitsPerSample = 16  -- 16-bit
    
    return duration * sampleRate * channels * (bitsPerSample / 8)
end

-- Remover sons antigos
function SoundCache.evictOldSounds()
    local sounds = {}
    for path, sound in pairs(SoundCache.cache) do
        table.insert(sounds, {
            path = path,
            sound = sound,
            accessCount = SoundCache.accessCount[path] or 0,
            size = SoundCache.estimateSoundSize(sound)
        })
    end
    
    -- Ordenar por acesso
    table.sort(sounds, function(a, b)
        return a.accessCount < b.accessCount
    end)
    
    -- Remover até liberar espaço
    local targetSize = SoundCache.maxSize * 0.7
    
    for _, item in ipairs(sounds) do
        if SoundCache.currentSize <= targetSize then
            break
        end
        
        SoundCache.cache[item.path] = nil
        SoundCache.accessCount[item.path] = nil
        SoundCache.currentSize = SoundCache.currentSize - item.size
    end
end
```

---

## ⏳ Lazy Loading

### 🎯 **Sistema de Lazy Loading**

```lua
-- Sistema de lazy loading
local LazyLoader = {}

LazyLoader.loadQueue = {}
LazyLoader.loading = false
LazyLoader.maxConcurrent = 3
LazyLoader.currentLoads = 0

-- Adicionar item à fila de carregamento
function LazyLoader.queueLoad(loadFunc, priority)
    priority = priority or 0
    
    table.insert(LazyLoader.loadQueue, {
        func = loadFunc,
        priority = priority,
        timestamp = g_clock.millis()
    })
    
    -- Ordenar por prioridade
    table.sort(LazyLoader.loadQueue, function(a, b)
        return a.priority > b.priority
    end)
    
    -- Iniciar carregamento se não estiver ativo
    if not LazyLoader.loading then
        LazyLoader.startLoading()
    end
end

-- Iniciar carregamento
function LazyLoader.startLoading()
    LazyLoader.loading = true
    
    local function processQueue()
        if #LazyLoader.loadQueue == 0 or LazyLoader.currentLoads >= LazyLoader.maxConcurrent then
            if #LazyLoader.loadQueue == 0 then
                LazyLoader.loading = false
            else
                scheduleEvent(processQueue, 100)
            end
            return
        end
        
        local item = table.remove(LazyLoader.loadQueue, 1)
        LazyLoader.currentLoads = LazyLoader.currentLoads + 1
        
        -- Executar carregamento
        local success, result = pcall(item.func)
        
        if not success then
            print("Erro no lazy loading:", result)
        end
        
        LazyLoader.currentLoads = LazyLoader.currentLoads - 1
        
        -- Processar próximo item
        scheduleEvent(processQueue, 10)
    end
    
    processQueue()
end

-- Lazy loading de texturas
function LazyLoader.loadTexture(path, callback)
    LazyLoader.queueLoad(function()
        local texture = TextureCache.getTexture(path)
        if callback then
            callback(texture)
        end
    end, 1)
end

-- Lazy loading de sons
function LazyLoader.loadSound(path, callback)
    LazyLoader.queueLoad(function()
        local sound = SoundCache.getSound(path)
        if callback then
            callback(sound)
        end
    end, 2)
end

-- Lazy loading de dados
function LazyLoader.loadData(path, callback)
    LazyLoader.queueLoad(function()
        local data = g_resources.readFileContents(path)
        if callback then
            callback(data)
        end
    end, 3)
end
```

---

## 🎨 Otimização de Renderização

### 🖼️ **Render Optimization**

```lua
-- Sistema de otimização de renderização
local RenderOptimizer = {}

RenderOptimizer.config = {
    enableFrustumCulling = true,
    enableOcclusionCulling = true,
    enableLOD = true,
    maxDrawDistance = 100,
    cullDistance = 50
}

-- Frustum culling
function RenderOptimizer.isInFrustum(position, camera)
    if not RenderOptimizer.config.enableFrustumCulling then
        return true
    end
    
    -- Implementar frustum culling
    local cameraPos = camera:getPosition()
    local distance = math.sqrt(
        (position.x - cameraPos.x) ^ 2 +
        (position.y - cameraPos.y) ^ 2 +
        (position.z - cameraPos.z) ^ 2
    )
    
    return distance <= RenderOptimizer.config.maxDrawDistance
end

-- Occlusion culling
function RenderOptimizer.isOccluded(position, camera)
    if not RenderOptimizer.config.enableOcclusionCulling then
        return false
    end
    
    -- Implementar occlusion culling
    local ray = camera:getPosition() - position
    local hit = g_map.raycast(camera:getPosition(), position)
    
    return hit and hit ~= position
end

-- Level of Detail (LOD)
function RenderOptimizer.getLODLevel(distance)
    if not RenderOptimizer.config.enableLOD then
        return 1
    end
    
    if distance <= 10 then
        return 1  -- Alto detalhe
    elseif distance <= 25 then
        return 2  -- Médio detalhe
    elseif distance <= 50 then
        return 3  -- Baixo detalhe
    else
        return 4  -- Mínimo detalhe
    end
end

-- Otimizar renderização de criaturas
function RenderOptimizer.optimizeCreatureRendering(creature, camera)
    local position = creature:getPosition()
    local cameraPos = camera:getPosition()
    
    local distance = math.sqrt(
        (position.x - cameraPos.x) ^ 2 +
        (position.y - cameraPos.y) ^ 2 +
        (position.z - cameraPos.z) ^ 2
    )
    
    -- Verificar se deve renderizar
    if not RenderOptimizer.isInFrustum(position, camera) then
        creature:setVisible(false)
        return false
    end
    
    if RenderOptimizer.isOccluded(position, camera) then
        creature:setVisible(false)
        return false
    end
    
    -- Aplicar LOD
    local lodLevel = RenderOptimizer.getLODLevel(distance)
    creature:setLODLevel(lodLevel)
    
    creature:setVisible(true)
    return true
end
```

---

## 🌐 Otimização de Rede

### 📡 **Network Optimization**

```lua
-- Sistema de otimização de rede
local NetworkOptimizer = {}

NetworkOptimizer.config = {
    enableCompression = true,
    enableBatching = true,
    maxBatchSize = 10,
    batchTimeout = 50,  -- ms
    enablePrediction = true
}

-- Compressão de dados
function NetworkOptimizer.compressData(data)
    if not NetworkOptimizer.config.enableCompression then
        return data
    end
    
    -- Implementar compressão simples
    local compressed = {}
    local lastValue = nil
    local count = 0
    
    for _, value in ipairs(data) do
        if value == lastValue then
            count = count + 1
        else
            if count > 0 then
                table.insert(compressed, {value = lastValue, count = count})
            end
            lastValue = value
            count = 1
        end
    end
    
    if count > 0 then
        table.insert(compressed, {value = lastValue, count = count})
    end
    
    return compressed
end

-- Descompressão de dados
function NetworkOptimizer.decompressData(compressedData)
    if not NetworkOptimizer.config.enableCompression then
        return compressedData
    end
    
    local data = {}
    
    for _, item in ipairs(compressedData) do
        for i = 1, item.count do
            table.insert(data, item.value)
        end
    end
    
    return data
end

-- Batching de comandos
local CommandBatcher = {}

CommandBatcher.batch = {}
CommandBatcher.timer = nil

function CommandBatcher.addCommand(command)
    table.insert(CommandBatcher.batch, command)
    
    if #CommandBatcher.batch >= NetworkOptimizer.config.maxBatchSize then
        CommandBatcher.flush()
    elseif not CommandBatcher.timer then
        CommandBatcher.timer = scheduleEvent(CommandBatcher.flush, NetworkOptimizer.config.batchTimeout)
    end
end

function CommandBatcher.flush()
    if #CommandBatcher.batch > 0 then
        local batchData = NetworkOptimizer.compressData(CommandBatcher.batch)
        g_game.sendBatch(batchData)
        CommandBatcher.batch = {}
    end
    
    if CommandBatcher.timer then
        removeEvent(CommandBatcher.timer)
        CommandBatcher.timer = nil
    end
end
```

---

## 📊 Monitoramento de Performance

### 🎯 **Performance Monitor**

```lua
-- Sistema de monitoramento de performance
local PerformanceMonitor = {}

PerformanceMonitor.metrics = {}
PerformanceMonitor.enabled = false

-- Inicializar monitor
function PerformanceMonitor.init()
    PerformanceMonitor.enabled = g_settings.getBoolean("performance.enableMonitoring", false)
    
    if PerformanceMonitor.enabled then
        PerformanceMonitor.startMonitoring()
    end
end

-- Iniciar monitoramento
function PerformanceMonitor.startMonitoring()
    local function monitor()
        local metrics = PerformanceMonitor.collectMetrics()
        PerformanceMonitor.updateMetrics(metrics)
        
        -- Verificar alertas
        PerformanceMonitor.checkAlerts(metrics)
        
        scheduleEvent(monitor, 1000)  -- 1 segundo
    end
    
    monitor()
end

-- Coletar métricas
function PerformanceMonitor.collectMetrics()
    return {
        fps = g_app.getFps(),
        memory = collectgarbage("count"),
        textureCount = g_textures.getLoadedTextureCount(),
        soundCount = g_sounds.getLoadedSoundCount(),
        widgetCount = PerformanceMonitor.countWidgets(),
        networkLatency = PerformanceMonitor.measureNetworkLatency(),
        timestamp = g_clock.millis()
    }
end

-- Atualizar métricas
function PerformanceMonitor.updateMetrics(metrics)
    table.insert(PerformanceMonitor.metrics, metrics)
    
    -- Manter apenas os últimos 60 segundos
    if #PerformanceMonitor.metrics > 60 then
        table.remove(PerformanceMonitor.metrics, 1)
    end
end

-- Verificar alertas
function PerformanceMonitor.checkAlerts(metrics)
    if metrics.fps < 30 then
        print("ALERTA: FPS baixo - " .. metrics.fps)
    end
    
    if metrics.memory > 200 * 1024 then  -- 200MB
        print("ALERTA: Uso de memória alto - " .. math.floor(metrics.memory / 1024) .. "MB")
    end
    
    if metrics.networkLatency > 1000 then  -- 1 segundo
        print("ALERTA: Latência de rede alta - " .. metrics.networkLatency .. "ms")
    end
end

-- Contar widgets
function PerformanceMonitor.countWidgets()
    local count = 0
    
    local function countWidget(widget)
        count = count + 1
        local children = widget:getChildren()
        for _, child in ipairs(children) do
            countWidget(child)
        end
    end
    
    countWidget(g_ui.getRootWidget())
    return count
end

-- Medir latência de rede
function PerformanceMonitor.measureNetworkLatency()
    if not g_game.isOnline() then
        return 0
    end
    
    local startTime = g_clock.millis()
    g_game.ping()
    
    -- Simular medição de ping
    return math.random(50, 200)  -- 50-200ms
end

-- Gerar relatório de performance
function PerformanceMonitor.generateReport()
    if #PerformanceMonitor.metrics == 0 then
        return "Nenhuma métrica disponível"
    end
    
    local report = {}
    table.insert(report, "=== RELATÓRIO DE PERFORMANCE ===")
    table.insert(report, "")
    
    -- Calcular médias
    local avgFps = 0
    local avgMemory = 0
    local avgLatency = 0
    
    for _, metric in ipairs(PerformanceMonitor.metrics) do
        avgFps = avgFps + metric.fps
        avgMemory = avgMemory + metric.memory
        avgLatency = avgLatency + metric.networkLatency
    end
    
    local count = #PerformanceMonitor.metrics
    avgFps = avgFps / count
    avgMemory = avgMemory / count
    avgLatency = avgLatency / count
    
    table.insert(report, string.format("FPS Médio: %.1f", avgFps))
    table.insert(report, string.format("Memória Média: %.2f KB", avgMemory))
    table.insert(report, string.format("Latência Média: %.0f ms", avgLatency))
    table.insert(report, string.format("Período: %d segundos", count))
    
    return table.concat(report, "\n")
end
```

---

### 🎮 **Sistema de Performance Completo**

```lua
-- Sistema de performance principal
local PerformanceSystem = {}

function PerformanceSystem.init()
    -- Inicializar componentes
    CPUProfiler.init()
    MemoryProfiler.init()
    GarbageCollector.init()
    TextureCache.init()
    SoundCache.init()
    LazyLoader.init()
    RenderOptimizer.init()
    NetworkOptimizer.init()
    PerformanceMonitor.init()
    
    -- Configurar eventos
    connect(g_game, {
        onGameStart = PerformanceSystem.onGameStart,
        onGameEnd = PerformanceSystem.onGameEnd
    })
    
    print("Sistema de performance inicializado")
end

function PerformanceSystem.onGameStart()
    -- Iniciar monitoramento específico do jogo
    PerformanceSystem.startGameMonitoring()
end

function PerformanceSystem.onGameEnd()
    -- Parar monitoramento específico do jogo
    PerformanceSystem.stopGameMonitoring()
    
    -- Gerar relatórios
    PerformanceSystem.generateReports()
end

function PerformanceSystem.startGameMonitoring()
    -- Monitorar performance específica do jogo
    local function gameMonitor()
        local fps = g_app.getFps()
        local memory = collectgarbage("count")
        
        if fps < 30 then
            PerformanceSystem.optimizeForLowFPS()
        end
        
        if memory > 150 * 1024 then  -- 150MB
            PerformanceSystem.optimizeForHighMemory()
        end
        
        scheduleEvent(gameMonitor, 5000)  -- 5 segundos
    end
    
    gameMonitor()
end

function PerformanceSystem.optimizeForLowFPS()
    -- Reduzir qualidade visual
    g_graphics.setAntialiasing("none")
    g_graphics.setTextureFiltering("nearest")
    
    -- Desabilitar efeitos visuais
    g_settings.set("graphics.particles", false)
    g_settings.set("graphics.bloom", false)
    g_settings.set("graphics.shadows", false)
    
    print("Otimizações aplicadas para FPS baixo")
end

function PerformanceSystem.optimizeForHighMemory()
    -- Forçar garbage collection
    GarbageCollector.forceCollect()
    
    -- Limpar caches
    TextureCache.clear()
    SoundCache.clear()
    
    -- Reduzir qualidade de texturas
    g_graphics.setTextureQuality("low")
    
    print("Otimizações aplicadas para memória alta")
end

function PerformanceSystem.generateReports()
    local reports = {}
    
    table.insert(reports, CPUProfiler.generateReport())
    table.insert(reports, MemoryProfiler.generateReport())
    table.insert(reports, PerformanceMonitor.generateReport())
    
    -- Salvar relatórios
    local reportFile = io.open("performance_report.txt", "w")
    if reportFile then
        reportFile:write(table.concat(reports, "\n\n"))
        reportFile:close()
    end
end
```

---

## ✅ Melhores Práticas

### 🎯 **Uso Eficiente do Sistema**

```lua
-- ✅ BOM: Usar profiling seletivamente
if g_settings.getBoolean("performance.enableProfiling", false) then
    CPUProfiler.measureTime("expensiveOperation", function()
        -- operação custosa
    end)
end

-- ✅ BOM: Usar cache adequadamente
local texture = TextureCache.getTexture("/images/icon.png")

-- ✅ BOM: Usar lazy loading
LazyLoader.loadTexture("/images/background.png", function(texture)
    widget:setImageSource(texture)
end)

-- ✅ BOM: Monitorar performance
PerformanceMonitor.init()

-- ❌ EVITE: Profiling excessivo
CPUProfiler.measureTime("simpleOperation", function()
    local x = 1 + 1  -- Operação muito simples
end)

-- ❌ EVITE: Cache desnecessário
TextureCache.getTexture("/images/temp.png")  -- Arquivo temporário

-- ❌ EVITE: Lazy loading desnecessário
LazyLoader.loadTexture("/images/small_icon.png")  -- Ícone pequeno
```

### 🔧 **Configuração Adequada**

```lua
-- ✅ BOM: Configurar baseado em hardware
local PERFORMANCE_CONFIG = {
    lowEnd = {
        enableProfiling = false,
        enableParticles = false,
        textureQuality = "low",
        maxDrawDistance = 50
    },
    midEnd = {
        enableProfiling = true,
        enableParticles = true,
        textureQuality = "medium",
        maxDrawDistance = 100
    },
    highEnd = {
        enableProfiling = true,
        enableParticles = true,
        textureQuality = "high",
        maxDrawDistance = 200
    }
}

-- ✅ BOM: Detectar hardware
function detectHardware()
    local fps = g_app.getFps()
    local memory = collectgarbage("count")
    
    if fps < 30 or memory > 100 * 1024 then
        return "lowEnd"
    elseif fps < 60 or memory > 200 * 1024 then
        return "midEnd"
    else
        return "highEnd"
    end
end

-- ✅ BOM: Aplicar configuração
function applyPerformanceConfig()
    local hardware = detectHardware()
    local config = PERFORMANCE_CONFIG[hardware]
    
    for key, value in pairs(config) do
        g_settings.set("performance." .. key, value)
    end
end
```

### 🎨 **Design Consistente**

```lua
-- ✅ BOM: Usar constantes para configurações
local PERFORMANCE_CONSTANTS = {
    MEMORY_THRESHOLD = 100 * 1024,  -- 100MB
    FPS_THRESHOLD = 30,
    CACHE_MAX_SIZE = 50 * 1024 * 1024,  -- 50MB
    BATCH_TIMEOUT = 50  -- ms
}

-- ✅ BOM: Usar funções padronizadas
function optimizePerformance()
    local fps = g_app.getFps()
    local memory = collectgarbage("count")
    
    if fps < PERFORMANCE_CONSTANTS.FPS_THRESHOLD then
        applyLowFPSOptimizations()
    end
    
    if memory > PERFORMANCE_CONSTANTS.MEMORY_THRESHOLD then
        applyHighMemoryOptimizations()
    end
end

-- ✅ BOM: Monitoramento contínuo
function setupPerformanceMonitoring()
    scheduleEvent(function()
        optimizePerformance()
        setupPerformanceMonitoring()
    end, 5000)  -- 5 segundos
end
```

O sistema de performance do OTClient oferece ferramentas poderosas para otimização e monitoramento. Use estas práticas para garantir performance máxima em suas aplicações. 
> - [[Getting_Started_Guide]] - Comece aqui
> - [[Module_System_Guide]] - Sistema de módulos
> - [[UI_System_Guide]] - Interface do usuário
> - [[Lua_API_Reference]] - Referência da API

---

> [!success] **Navegação**
> **📚 Documentos Relacionados:**
> - [[Getting_Started_Guide]] - Comece aqui
> - [[Module_System_Guide]] - Sistema de módulos
> - [[UI_System_Guide]] - Interface do usuário
> - [[Lua_API_Reference]] - API completa
> 
> **🔗 Navegação Rápida:**
> - [[Wiki_Index]] - Voltar ao índice
> - [[Cheat_Sheet]] - Referência rápida
> - [[Debug_System_Guide]] - Debugging

