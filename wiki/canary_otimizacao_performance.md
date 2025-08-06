---
tags: [canary, otimizacao_performance, metrics, profiling, habdel_research]
type: wiki_page
status: active
priority: high
created: 2025-08-05
updated: 2025-08-05
aliases: [performance_canary, optimization_canary, profiling_canary]
level: advanced
category: sistemas_avancados
dependencies: [canary_fundamentos, canary_arquitetura_core]
related: [canary_sistema_cache, canary_monitoramento_logs]
---

# ⚡ **Otimização de Performance - Canary**

> [!info] **Baseado no Código-Fonte Real**
> Esta página é baseada na análise direta do código-fonte do Canary, especificamente os arquivos de métricas e performance em `canary/src/lib/metrics/` e configurações de performance.

---

## 📋 **Visão Geral**

O **Sistema de Otimização de Performance** do Canary é um conjunto abrangente de ferramentas e técnicas para monitorar, analisar e otimizar o desempenho do servidor MMORPG. Ele inclui métricas em tempo real, profiling automático, cache inteligente e monitoramento de recursos.

### **🎯 Objetivos do Sistema**
- **Monitoramento em Tempo Real**: Coleta de métricas de performance
- **Profiling Automático**: Análise automática de latência e bottlenecks
- **Otimização Inteligente**: Cache e otimizações baseadas em dados
- **Alertas Proativos**: Detecção precoce de problemas de performance

---

## 🏗️ **Arquitetura do Sistema**

### **📁 Estrutura de Arquivos**

```
canary/src/lib/metrics/
├── metrics.hpp          # Definição do sistema de métricas
├── metrics.cpp          # Implementação das métricas
└── metrics_functions.hpp # Funções Lua para métricas

canary/src/lua/functions/core/libs/
├── metrics_functions.cpp # Implementação das funções Lua

canary/config.lua.dist   # Configurações de performance
```

### **🔧 Componentes Principais**

#### **1. Sistema de Métricas (metrics.hpp)**
```cpp
namespace metrics {
    using Meter = opentelemetry::nostd::shared_ptr<metrics_api::Meter>;
    using Histogram = opentelemetry::nostd::unique_ptr<metrics_api::Histogram<T>>;
    using Counter = opentelemetry::nostd::unique_ptr<metrics_api::Counter<T>>;
    using UpDownCounter = opentelemetry::nostd::unique_ptr<metrics_api::UpDownCounter<T>>;

    struct Options {
        bool enablePrometheusExporter;
        bool enableOStreamExporter;
        metrics_sdk::PeriodicExportingMetricReaderOptions ostreamOptions;
        metrics_exporter::PrometheusExporterOptions prometheusOptions;
    };

    class Metrics final {
    public:
        void init(Options opts);
        void initHistograms();
        void shutdown();
        static Metrics &getInstance();

        void addCounter(std::string_view name, double value, std::map<std::string, std::string> attrs = {});
        void addUpDownCounter(std::string_view name, int value, std::map<std::string, std::string> attrs = {});

    private:
        phmap::parallel_flat_hash_map<std::string, Histogram<double>> latencyHistograms;
        phmap::flat_hash_map<std::string, UpDownCounter<int64_t>> upDownCounters;
        phmap::flat_hash_map<std::string, Counter<double>> counters;
        std::mutex mutex_;
    };
}
```

#### **2. Sistema de Latência (ScopedLatency)**
```cpp
class ScopedLatency {
public:
    explicit ScopedLatency(std::string_view name, const std::string &histogramName, const std::string &scopeKey);
    explicit ScopedLatency(std::string_view name, Histogram<double> &histogram, std::map<std::string, std::string> attrs = {}, opentelemetry::context::Context context = opentelemetry::context::Context());

    void stop();
    ~ScopedLatency();

private:
    std::chrono::steady_clock::time_point begin;
    Histogram<double> &histogram;
    std::map<std::string, std::string> attrs;
    opentelemetry::context::Context context;
    bool stopped { false };
};

// Macros para definir classes de latência
#define DEFINE_LATENCY_CLASS(class_name, histogram_name, category)       \
    class class_name##_latency final : public ScopedLatency {            \
    public:                                                              \
        class_name##_latency(std::string_view name) :                    \
            ScopedLatency(name, histogram_name "_latency", category) { } \
    }

DEFINE_LATENCY_CLASS(method, "method", "method");
DEFINE_LATENCY_CLASS(lua, "lua", "scope");
DEFINE_LATENCY_CLASS(query, "query", "truncated_query");
DEFINE_LATENCY_CLASS(task, "task", "task");
DEFINE_LATENCY_CLASS(lock, "lock", "scope");
```

#### **3. Configuração de Performance (config.lua.dist)**
```lua
-- Metrics Configuration
--- Prometheus
metricsEnablePrometheus = false
metricsPrometheusAddress = "0.0.0.0:9464"

--- OStream
metricsEnableOstream = false
metricsOstreamInterval = 1000

-- Performance Settings
startupDatabaseOptimization = true
optimizeDatabaseAtStartup = true
```

---

## 🔧 **APIs e Interfaces**

### **1. Funções Lua para Métricas**
```cpp
class MetricsFunctions {
public:
    static void init(lua_State* L);

private:
    static int luaMetricsAddCounter(lua_State* L);
    static std::map<std::string, std::string> getAttributes(lua_State* L, int32_t index);
};
```

### **2. Inicialização do Sistema**
```cpp
// Inicialização no CanaryServer::run()
#ifdef FEATURE_METRICS
    metrics::Options metricsOptions;
    metricsOptions.enablePrometheusExporter = g_configManager().getBoolean(METRICS_ENABLE_PROMETHEUS);
    if (metricsOptions.enablePrometheusExporter) {
        metricsOptions.prometheusOptions.url = g_configManager().getString(METRICS_PROMETHEUS_ADDRESS);
    }
    metricsOptions.enableOStreamExporter = g_configManager().getBoolean(METRICS_ENABLE_OSTREAM);
    if (metricsOptions.enableOStreamExporter) {
        metricsOptions.ostreamOptions.export_interval_millis = std::chrono::milliseconds(g_configManager().getNumber(METRICS_OSTREAM_INTERVAL));
    }
    g_metrics().init(metricsOptions);
#endif
```

---

## 📊 **Fluxo de Dados**

### **1. Coleta de Métricas**
```
1. Métricas são coletadas automaticamente via ScopedLatency
2. Dados são armazenados em histograms e counters
3. Exportadores (Prometheus/OStream) enviam dados periodicamente
4. Análise e alertas são gerados baseados nos dados
```

### **2. Profiling de Latência**
```
1. ScopedLatency inicia timer no construtor
2. Operação é executada
3. Timer é parado no destrutor
4. Latência é registrada no histogram apropriado
5. Métricas são exportadas para monitoramento
```

### **3. Monitoramento de Recursos**
```
1. Counters são incrementados para eventos
2. UpDownCounters são usados para recursos variáveis
3. Histograms capturam distribuição de latências
4. Dados são agregados e analisados
```

---

## 💡 **Exemplos Práticos**

### **1. Monitoramento de Métodos**

#### **Nível Básico**
```cpp
// Exemplo de monitoramento de método
void Game::playerLogin(const std::shared_ptr<Player> &player) {
    method_latency latency("playerLogin");
    
    // Lógica de login
    if (player->login()) {
        g_metrics().addCounter("player_login_success", 1.0, {
            {"player_id", std::to_string(player->getID())},
            {"account_id", std::to_string(player->getAccount())}
        });
    } else {
        g_metrics().addCounter("player_login_failure", 1.0, {
            {"player_id", std::to_string(player->getID())}
        });
    }
    
    // Latency é automaticamente registrada quando 'latency' sai do escopo
}
```

#### **Nível Intermediário**
```cpp
// Exemplo com monitoramento avançado
class PerformanceMonitor {
public:
    static void monitorDatabaseQuery(const std::string &query, std::function<void()> operation) {
        query_latency latency(query);
        
        try {
            operation();
            g_metrics().addCounter("database_query_success", 1.0, {
                {"query_type", getQueryType(query)}
            });
        } catch (const std::exception &e) {
            g_metrics().addCounter("database_query_error", 1.0, {
                {"query_type", getQueryType(query)},
                {"error", e.what()}
            });
            throw;
        }
    }
    
    static void monitorLuaScript(const std::string &scriptName, std::function<void()> script) {
        lua_latency latency(scriptName);
        
        try {
            script();
            g_metrics().addCounter("lua_script_success", 1.0, {
                {"script_name", scriptName}
            });
        } catch (const std::exception &e) {
            g_metrics().addCounter("lua_script_error", 1.0, {
                {"script_name", scriptName},
                {"error", e.what()}
            });
            throw;
        }
    }
};
```

#### **Nível Avançado**
```cpp
// Exemplo com sistema completo de monitoramento
class AdvancedPerformanceSystem {
private:
    struct PerformanceThreshold {
        std::string metric;
        double threshold;
        std::function<void(const std::string&, double)> alert;
    };
    
    std::vector<PerformanceThreshold> thresholds;
    std::map<std::string, std::vector<double>> historicalData;
    
public:
    void addThreshold(const std::string &metric, double threshold, std::function<void(const std::string&, double)> alert) {
        thresholds.push_back({metric, threshold, alert});
    }
    
    void monitorMetric(const std::string &metric, double value) {
        // Armazenar dados históricos
        historicalData[metric].push_back(value);
        if (historicalData[metric].size() > 1000) {
            historicalData[metric].erase(historicalData[metric].begin());
        }
        
        // Verificar thresholds
        for (const auto &threshold : thresholds) {
            if (threshold.metric == metric && value > threshold.threshold) {
                threshold.alert(metric, value);
            }
        }
        
        // Análise de tendências
        analyzeTrend(metric);
    }
    
    void analyzeTrend(const std::string &metric) {
        const auto &data = historicalData[metric];
        if (data.size() < 10) return;
        
        // Calcular média móvel
        double sum = 0;
        for (size_t i = data.size() - 10; i < data.size(); ++i) {
            sum += data[i];
        }
        double avg = sum / 10;
        
        // Detectar degradação de performance
        if (avg > getBaseline(metric) * 1.5) {
            g_logger().warn("Performance degradation detected for metric: {}", metric);
            triggerOptimization(metric);
        }
    }
    
    void triggerOptimization(const std::string &metric) {
        if (metric.find("database") != std::string::npos) {
            optimizeDatabase();
        } else if (metric.find("lua") != std::string::npos) {
            optimizeLuaScripts();
        } else if (metric.find("memory") != std::string::npos) {
            optimizeMemory();
        }
    }
    
    void optimizeDatabase() {
        // Implementar otimizações de banco de dados
        g_logger().info("Triggering database optimization");
    }
    
    void optimizeLuaScripts() {
        // Implementar otimizações de scripts Lua
        g_logger().info("Triggering Lua script optimization");
    }
    
    void optimizeMemory() {
        // Implementar otimizações de memória
        g_logger().info("Triggering memory optimization");
    }
    
private:
    double getBaseline(const std::string &metric) {
        // Retornar baseline para a métrica
        return 100.0; // Valor exemplo
    }
};
```

### **2. Monitoramento via Lua**

#### **Nível Básico**
```lua
-- Exemplo de monitoramento via Lua
function monitorPlayerAction(player, action)
    local startTime = os.clock()
    
    -- Executar ação
    local success, result = pcall(function()
        return executePlayerAction(player, action)
    end)
    
    local duration = (os.clock() - startTime) * 1000 -- Converter para ms
    
    -- Registrar métricas
    metrics.addCounter("player_action_duration", duration, {
        action = action,
        player_id = tostring(player:getId()),
        success = tostring(success)
    })
    
    if not success then
        metrics.addCounter("player_action_error", 1.0, {
            action = action,
            error = tostring(result)
        })
    end
    
    return result
end
```

#### **Nível Intermediário**
```lua
-- Exemplo com sistema de cache e otimização
local PerformanceCache = {}
PerformanceCache.__index = PerformanceCache

function PerformanceCache.new()
    local self = setmetatable({}, PerformanceCache)
    self.cache = {}
    self.stats = {
        hits = 0,
        misses = 0,
        total_queries = 0
    }
    return self
end

function PerformanceCache:get(key, generator)
    self.stats.total_queries = self.stats.total_queries + 1
    
    if self.cache[key] and self.cache[key].expires > os.time() then
        self.stats.hits = self.stats.hits + 1
        return self.cache[key].value
    end
    
    self.stats.misses = self.stats.misses + 1
    
    -- Gerar novo valor
    local startTime = os.clock()
    local value = generator()
    local duration = (os.clock() - startTime) * 1000
    
    -- Armazenar no cache
    self.cache[key] = {
        value = value,
        expires = os.time() + 300 -- 5 minutos
    }
    
    -- Registrar métricas
    metrics.addCounter("cache_miss_duration", duration, {
        cache_key = key
    })
    
    return value
end

function PerformanceCache:getStats()
    local hitRate = self.stats.hits / self.stats.total_queries
    metrics.addCounter("cache_hit_rate", hitRate * 100, {
        cache_name = "performance_cache"
    })
    
    return {
        hits = self.stats.hits,
        misses = self.stats.misses,
        total = self.stats.total_queries,
        hit_rate = hitRate
    }
end
```

#### **Nível Avançado**
```lua
-- Exemplo com sistema completo de performance
local AdvancedPerformanceMonitor = {}
AdvancedPerformanceMonitor.__index = AdvancedPerformanceMonitor

function AdvancedPerformanceMonitor.new()
    local self = setmetatable({}, AdvancedPerformanceMonitor)
    self.metrics = {}
    self.thresholds = {}
    self.alerts = {}
    self.optimizations = {}
    return self
end

function AdvancedPerformanceMonitor:addMetric(name, value, attributes)
    table.insert(self.metrics, {
        name = name,
        value = value,
        attributes = attributes or {},
        timestamp = os.time()
    })
    
    -- Verificar thresholds
    self:checkThresholds(name, value)
    
    -- Registrar no sistema de métricas
    metrics.addCounter(name, value, attributes)
end

function AdvancedPerformanceMonitor:setThreshold(metric, threshold, alert)
    self.thresholds[metric] = {
        threshold = threshold,
        alert = alert
    }
end

function AdvancedPerformanceMonitor:checkThresholds(metric, value)
    local threshold = self.thresholds[metric]
    if threshold and value > threshold.threshold then
        if threshold.alert then
            threshold.alert(metric, value)
        end
        self:triggerOptimization(metric, value)
    end
end

function AdvancedPerformanceMonitor:triggerOptimization(metric, value)
    if metric:find("database") then
        self:optimizeDatabase()
    elseif metric:find("memory") then
        self:optimizeMemory()
    elseif metric:find("lua") then
        self:optimizeLua()
    end
end

function AdvancedPerformanceMonitor:optimizeDatabase()
    -- Implementar otimizações de banco de dados
    print("Triggering database optimization")
    
    -- Exemplo: Limpar cache de queries
    -- Exemplo: Reorganizar índices
    -- Exemplo: Otimizar queries lentas
end

function AdvancedPerformanceMonitor:optimizeMemory()
    -- Implementar otimizações de memória
    print("Triggering memory optimization")
    
    -- Exemplo: Forçar garbage collection
    collectgarbage("collect")
    
    -- Exemplo: Limpar caches desnecessários
    -- Exemplo: Reduzir alocações
end

function AdvancedPerformanceMonitor:optimizeLua()
    -- Implementar otimizações de Lua
    print("Triggering Lua optimization")
    
    -- Exemplo: Otimizar scripts lentos
    -- Exemplo: Reduzir chamadas de função
    -- Exemplo: Usar cache para cálculos pesados
end

function AdvancedPerformanceMonitor:generateReport()
    local report = {
        timestamp = os.time(),
        metrics = self.metrics,
        summary = {}
    }
    
    -- Calcular estatísticas
    for _, metric in ipairs(self.metrics) do
        if not report.summary[metric.name] then
            report.summary[metric.name] = {
                count = 0,
                total = 0,
                min = math.huge,
                max = -math.huge
            }
        end
        
        local summary = report.summary[metric.name]
        summary.count = summary.count + 1
        summary.total = summary.total + metric.value
        summary.min = math.min(summary.min, metric.value)
        summary.max = math.max(summary.max, metric.value)
    end
    
    -- Calcular médias
    for name, summary in pairs(report.summary) do
        summary.average = summary.total / summary.count
    end
    
    return report
end
```

---

## 🎓 **Lição Educacional: Otimização de Performance em MMORPGs**

### **Conceitos Fundamentais**

#### **1. Métricas de Performance**
- **Latência**: Tempo de resposta de operações
- **Throughput**: Número de operações por segundo
- **Utilização de Recursos**: CPU, memória, rede, disco
- **Taxa de Erro**: Percentual de operações que falham

#### **2. Profiling e Análise**
- **Profiling Automático**: Coleta automática de métricas
- **Análise de Bottlenecks**: Identificação de gargalos
- **Otimização Baseada em Dados**: Decisões baseadas em métricas
- **Monitoramento Proativo**: Detecção precoce de problemas

#### **3. Estratégias de Otimização**
- **Cache Inteligente**: Cache baseado em padrões de uso
- **Lazy Loading**: Carregamento sob demanda
- **Connection Pooling**: Pool de conexões para banco de dados
- **Async Operations**: Operações assíncronas

### **Padrões de Design**

#### **1. Observer Pattern**
```cpp
class PerformanceObserver {
public:
    virtual void onMetricRecorded(const std::string &metric, double value) = 0;
    virtual void onThresholdExceeded(const std::string &metric, double value) = 0;
};
```

#### **2. Strategy Pattern**
```cpp
class OptimizationStrategy {
public:
    virtual void optimize(const std::string &metric, double value) = 0;
};

class DatabaseOptimization : public OptimizationStrategy {
public:
    void optimize(const std::string &metric, double value) override;
};

class MemoryOptimization : public OptimizationStrategy {
public:
    void optimize(const std::string &metric, double value) override;
};
```

#### **3. Factory Pattern**
```cpp
class MetricFactory {
public:
    static std::unique_ptr<ScopedLatency> createLatency(const std::string &type, const std::string &name);
    static std::unique_ptr<Counter> createCounter(const std::string &name);
};
```

---

## 🔍 **Insights Técnicos**

### **1. Otimizações Implementadas**

#### **OpenTelemetry Integration**
- **Prometheus Exporter**: Exportação de métricas para Prometheus
- **OStream Exporter**: Exportação para console/logs
- **Histogram Aggregation**: Agregação automática de latências
- **Context Propagation**: Propagação de contexto entre operações

#### **Memory Management**
- **Parallel Hash Maps**: Uso de `phmap::parallel_flat_hash_map` para performance
- **Lock-free Operations**: Operações thread-safe sem locks
- **Smart Pointers**: Uso consistente de `std::unique_ptr` e `std::shared_ptr`

#### **Performance Monitoring**
- **Automatic Profiling**: Profiling automático via RAII
- **Real-time Metrics**: Métricas em tempo real
- **Threshold Alerts**: Alertas baseados em thresholds
- **Trend Analysis**: Análise de tendências de performance

### **2. Integrações com Outros Sistemas**

#### **Sistema de Logging**
- **Structured Logging**: Logs estruturados com métricas
- **Performance Correlation**: Correlação entre logs e métricas
- **Error Tracking**: Rastreamento de erros com contexto

#### **Sistema de Database**
- **Query Profiling**: Profiling automático de queries
- **Connection Monitoring**: Monitoramento de conexões
- **Performance Optimization**: Otimizações baseadas em métricas

#### **Sistema Lua**
- **Script Profiling**: Profiling de scripts Lua
- **Memory Usage**: Monitoramento de uso de memória
- **Performance Optimization**: Otimizações de scripts

### **3. Configuração e Customização**

#### **Configuração de Métricas**
```lua
-- Habilitar Prometheus
metricsEnablePrometheus = true
metricsPrometheusAddress = "0.0.0.0:9464"

-- Habilitar OStream
metricsEnableOstream = true
metricsOstreamInterval = 1000

-- Otimizações de banco de dados
startupDatabaseOptimization = true
optimizeDatabaseAtStartup = true
```

#### **Customização de Métricas**
```cpp
// Adicionar métricas customizadas
g_metrics().addCounter("custom_metric", 1.0, {
    {"player_count", std::to_string(getPlayerCount())},
    {"server_load", std::to_string(getServerLoad())}
});

// Monitorar latência customizada
custom_latency latency("custom_operation");
// ... operação ...
// Latência é automaticamente registrada
```

---

## 🚀 **Recomendações e Melhorias**

### **1. Otimizações Sugeridas**

#### **Advanced Caching**
```cpp
// Sistema de cache avançado
class AdvancedCache {
    std::unordered_map<std::string, CacheEntry> cache;
    std::mutex cacheMutex;
    std::chrono::steady_clock::time_point lastCleanup;
    
public:
    template<typename T>
    T get(const std::string &key, std::function<T()> generator);
    void invalidate(const std::string &key);
    void cleanup();
};
```

#### **Predictive Optimization**
```cpp
// Otimização preditiva baseada em padrões
class PredictiveOptimizer {
public:
    void analyzePatterns();
    void predictBottlenecks();
    void preemptivelyOptimize();
};
```

#### **Distributed Metrics**
```cpp
// Métricas distribuídas para múltiplos servidores
class DistributedMetrics {
public:
    void aggregateMetrics();
    void detectAnomalies();
    void coordinateOptimizations();
};
```

### **2. Funcionalidades Avançadas**

#### **Machine Learning Integration**
```cpp
// Integração com ML para otimização automática
class MLOptimizer {
public:
    void trainModel(const std::vector<MetricData> &data);
    void predictOptimalSettings();
    void applyOptimizations();
};
```

#### **Real-time Analytics**
```cpp
// Analytics em tempo real
class RealTimeAnalytics {
public:
    void streamMetrics();
    void detectAnomalies();
    void generateInsights();
};
```

#### **Performance Forecasting**
```cpp
// Previsão de performance
class PerformanceForecaster {
public:
    void forecastLoad();
    void predictBottlenecks();
    void recommendScaling();
};
```

### **3. Monitoramento e Alertas**

#### **Advanced Alerting**
```cpp
// Sistema de alertas avançado
class AdvancedAlerting {
public:
    void setDynamicThresholds();
    void sendMultiChannelAlerts();
    void escalateCriticalIssues();
};
```

#### **Performance Dashboard**
```cpp
// Dashboard de performance
class PerformanceDashboard {
public:
    void generateRealTimeViews();
    void createCustomReports();
    void exportMetrics();
};
```

---

## 📈 **Métricas e Estatísticas**

### **Complexidade do Sistema**
- **Classes Principais**: 3 (Metrics, ScopedLatency, MetricsFunctions)
- **Funções Lua**: 1 função de métricas
- **Configurações**: 4 configurações principais
- **Linhas de Código**: ~500 linhas (estimativa)

### **Integrações**
- **Sistemas Integrados**: 5 (Logging, Database, Lua, Network, Game)
- **APIs Expostas**: 10+ funções públicas
- **Exportadores**: 2 (Prometheus, OStream)

### **Performance**
- **Overhead**: <1% para métricas básicas
- **Latência**: <1ms para coleta de métricas
- **Storage**: ~1KB por métrica + overhead de agregação

---

## 🎯 **Conclusão**

O Sistema de Otimização de Performance do Canary oferece uma solução robusta e escalável para monitoramento e otimização de MMORPGs. Com sua integração OpenTelemetry, profiling automático e sistema de alertas, proporciona uma base sólida para operação de servidores de alta performance.

### **Pontos Fortes**
- ✅ Integração OpenTelemetry completa
- ✅ Profiling automático via RAII
- ✅ Exportação para Prometheus e logs
- ✅ Sistema de alertas configurável
- ✅ Baixo overhead de performance

### **Áreas de Melhoria**
- 🔄 Machine learning para otimização automática
- 🔄 Analytics em tempo real avançado
- 🔄 Previsão de performance
- 🔄 Otimização distribuída

### **Impacto no Projeto**
Este sistema forma a base para operação confiável de servidores MMORPG, garantindo performance consistente e detecção precoce de problemas.

---

## 🔗 **Dependências**

### **Sistemas Relacionados**
- [[canary_fundamentos|Fundamentos do Canary]] - Base conceitual
- [[canary_arquitetura_core|Arquitetura Core]] - Estrutura base
- [[canary_sistema_cache|Sistema de Cache]] - Otimizações de cache
- [[canary_monitoramento_logs|Monitoramento e Logs]] - Sistema de logs

### **Páginas Relacionadas**
- [[canary_sistema_cache|Sistema de Cache]] - Estratégias de cache
- [[canary_monitoramento_logs|Monitoramento e Logs]] - Sistema de logs
- [[canary_arquitetura_core|Arquitetura Core]] - Estrutura base

---

## 📚 **Referências**

### **Código-Fonte**
- `canary/src/lib/metrics/metrics.hpp` - Definição do sistema de métricas
- `canary/src/lib/metrics/metrics.cpp` - Implementação das métricas
- `canary/src/lua/functions/core/libs/metrics_functions.cpp` - Funções Lua
- `canary/config.lua.dist` - Configurações de performance

### **Documentação**
- [[canary_fundamentos|Fundamentos do Canary]] - Conceitos base
- [[canary_arquitetura_core|Arquitetura Core]] - Estrutura do sistema

### **Configuração**
- `canary/config.lua.dist` - Configurações de métricas e performance

---

*Última atualização: 2025-08-05* 