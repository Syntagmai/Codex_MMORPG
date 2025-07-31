
# Guias de Migração OTClient ↔ Canary

## 📋 Visão Geral

Este documento fornece guias detalhados para migração bidirecional entre os sistemas **OTClient** e **Canary**, incluindo preparação, adaptação de código, testes e validação.

### 🎯 Objetivo

Permitir aos desenvolvedores:
- Migrar código de OTClient para Canary
- Migrar código de Canary para OTClient
- Manter compatibilidade entre sistemas
- Validar migrações com testes automatizados

---

## 🔄 Migração OTClient → Canary

### 📋 Fase 1: Preparação

#### 1.1 Análise de Compatibilidade

```bash
# Executar análise de compatibilidade
python check_compatibility.py --source otclient --target canary

# Gerar relatório detalhado
python generate_migration_report.py --source otclient --target canary --detailed
```

#### 1.2 Verificação de Recursos

```lua
-- Verificar recursos disponíveis no Canary
local function checkCanaryResources()
    local resources = {
        "advanced_ui_components",
        "enhanced_graphics_engine",
        "extended_protocol_support",
        "advanced_scripting_engine",
        "improved_network_stack"
    }
    
    local available = {}
    for _, resource in ipairs(resources) do
        if isResourceAvailable(resource) then
            table.insert(available, resource)
        end
    end
    
    return available
end
```

#### 1.3 Backup e Versionamento

```bash
# Criar backup do código OTClient
git checkout -b migration/otclient-to-canary
git add .
git commit -m "Backup antes da migração OTClient → Canary"

# Criar snapshot da estrutura atual
python create_snapshot.py --name "otclient_pre_migration"
```

### 🔧 Fase 2: Adaptação de Código

#### 2.1 Adaptação de APIs

```lua
-- Código original OTClient
local function oldOTClientFunction()
    local button = g_ui.createWidget('Button', parent)
    button:setText("Clique aqui")
    button.onClick = function()
        print("Botão clicado!")
    end
end

-- Código adaptado para Canary
local function newCanaryFunction()
    if Canary then
        -- Usar API avançada do Canary
        local button = g_ui.createWidget('AdvancedButton', parent)
        button:setText("Clique aqui")
        button:setStyle("modern")
        button.onClick = function()
            print("Botão clicado com estilo moderno!")
        end
    else
        -- Fallback para OTClient
        local button = g_ui.createWidget('Button', parent)
        button:setText("Clique aqui")
        button.onClick = function()
            print("Botão clicado!")
        end
    end
end
```

#### 2.2 Adaptação de Protocolos

```lua
-- Protocolo OTClient
local function otclientProtocol()
    local protocol = g_game.getProtocol()
    protocol:sendExtendedOpcode(0x01, "Hello OTClient")
end

-- Protocolo Canary
local function canaryProtocol()
    if Canary then
        local protocol = g_game.getProtocol()
        protocol:sendExtendedOpcode(0x01, "Hello Canary", {
            version = "2.0",
            features = {"advanced_ui", "enhanced_graphics"}
        })
    else
        -- Fallback para OTClient
        local protocol = g_game.getProtocol()
        protocol:sendExtendedOpcode(0x01, "Hello OTClient")
    end
end
```

#### 2.3 Adaptação de UI

```lua
-- UI OTClient
local function createOTClientUI()
    local window = g_ui.createWidget('Window', rootWidget)
    window:setText("Janela OTClient")
    window:setSize({width = 300, height = 200})
end

-- UI Canary
local function createCanaryUI()
    if Canary then
        local window = g_ui.createWidget('ModernWindow', rootWidget)
        window:setText("Janela Canary")
        window:setSize({width = 300, height = 200})
        window:setTheme("dark")
        window:enableAnimations(true)
    else
        -- Fallback para OTClient
        local window = g_ui.createWidget('Window', rootWidget)
        window:setText("Janela OTClient")
        window:setSize({width = 300, height = 200})
    end
end
```

### 🧪 Fase 3: Testes de Migração

#### 3.1 Testes de Compatibilidade

```lua
-- Teste de compatibilidade
local function testCompatibility()
    local tests = {
        "ui_components",
        "game_systems", 
        "network_protocols",
        "file_formats",
        "scripting_engine"
    }
    
    local results = {}
    for _, test in ipairs(tests) do
        local result = runCompatibilityTest(test)
        results[test] = result
        
        if not result.success then
            print("❌ Falha no teste: " .. test)
            print("   Erro: " .. result.error)
        else
            print("✅ Teste passou: " .. test)
        end
    end
    
    return results
end
```

#### 3.2 Testes de Performance

```lua
-- Teste de performance
local function testPerformance()
    local metrics = {
        "fps",
        "memory_usage",
        "network_latency",
        "response_time"
    }
    
    local results = {}
    for _, metric in ipairs(metrics) do
        local value = measurePerformance(metric)
        results[metric] = value
        
        if value < getThreshold(metric) then
            print("⚠️ Performance baixa: " .. metric .. " = " .. value)
        else
            print("✅ Performance OK: " .. metric .. " = " .. value)
        end
    end
    
    return results
end
```

#### 3.3 Testes de Integração

```lua
-- Teste de integração
local function testIntegration()
    local integrationTests = {
        "data_migration",
        "api_compatibility",
        "protocol_handling",
        "ui_rendering"
    }
    
    for _, test in ipairs(integrationTests) do
        local result = executeIntegrationTest(test)
        validateTestResult(result)
    end
end
```

---

## 🔄 Migração Canary → OTClient

### 📋 Fase 1: Verificação de Recursos

#### 1.1 Análise de Dependências

```lua
-- Verificar dependências Canary
local function checkCanaryDependencies()
    local dependencies = {
        "advanced_ui_engine",
        "enhanced_graphics_api",
        "extended_protocol_features",
        "advanced_scripting_language",
        "modern_network_stack"
    }
    
    local missing = {}
    for _, dep in ipairs(dependencies) do
        if not isDependencyAvailable(dep) then
            table.insert(missing, dep)
        end
    end
    
    return missing
end
```

#### 1.2 Identificação de Funcionalidades Avançadas

```lua
-- Identificar funcionalidades avançadas
local function identifyAdvancedFeatures()
    local features = {
        "modern_ui_components",
        "enhanced_graphics_effects",
        "extended_protocol_support",
        "advanced_scripting_capabilities"
    }
    
    local usedFeatures = {}
    for _, feature in ipairs(features) do
        if isFeatureUsed(feature) then
            table.insert(usedFeatures, feature)
        end
    end
    
    return usedFeatures
end
```

### 🔧 Fase 2: Adaptação de Funcionalidades

#### 2.1 Simplificação de UI

```lua
-- UI Canary (avançada)
local function createAdvancedCanaryUI()
    local window = g_ui.createWidget('ModernWindow', rootWidget)
    window:setText("Janela Avançada")
    window:setSize({width = 400, height = 300})
    window:setTheme("dark")
    window:enableAnimations(true)
    window:addShadow()
    window:setOpacity(0.9)
end

-- UI OTClient (simplificada)
local function createSimplifiedOTClientUI()
    if OTClient then
        local window = g_ui.createWidget('Window', rootWidget)
        window:setText("Janela Simplificada")
        window:setSize({width = 400, height = 300})
        -- Funcionalidades avançadas removidas
    else
        -- Usar versão Canary completa
        createAdvancedCanaryUI()
    end
end
```

#### 2.2 Adaptação de Protocolos

```lua
-- Protocolo Canary (estendido)
local function canaryExtendedProtocol()
    local protocol = g_game.getProtocol()
    protocol:sendExtendedOpcode(0x01, "Advanced Message", {
        version = "2.0",
        features = {"advanced_ui", "enhanced_graphics", "modern_effects"},
        metadata = {
            timestamp = os.time(),
            session_id = generateSessionId()
        }
    })
end

-- Protocolo OTClient (compatível)
local function otclientCompatibleProtocol()
    if OTClient then
        local protocol = g_game.getProtocol()
        protocol:sendExtendedOpcode(0x01, "Compatible Message")
        -- Metadados avançados removidos
    else
        -- Usar protocolo Canary completo
        canaryExtendedProtocol()
    end
end
```

#### 2.3 Adaptação de Scripts

```lua
-- Script Canary (avançado)
local function advancedCanaryScript()
    -- Usar recursos avançados do Canary
    local engine = getAdvancedScriptingEngine()
    engine:executeAsync("complex_script.lua")
    engine:enableDebugMode(true)
    engine:setPerformanceProfile("high")
end

-- Script OTClient (compatível)
local function compatibleOTClientScript()
    if OTClient then
        -- Versão simplificada para OTClient
        local engine = getBasicScriptingEngine()
        engine:execute("simple_script.lua")
        -- Recursos avançados removidos
    else
        -- Usar versão Canary completa
        advancedCanaryScript()
    end
end
```

### 🧪 Fase 3: Validação e Testes

#### 3.1 Testes de Compatibilidade Reversa

```lua
-- Teste de compatibilidade reversa
local function testReverseCompatibility()
    local tests = {
        "basic_ui_components",
        "core_game_systems",
        "standard_protocols",
        "essential_features"
    }
    
    for _, test in ipairs(tests) do
        local result = runReverseCompatibilityTest(test)
        if not result.success then
            print("❌ Falha na compatibilidade reversa: " .. test)
            print("   Solução: " .. result.solution)
        else
            print("✅ Compatibilidade reversa OK: " .. test)
        end
    end
end
```

#### 3.2 Testes de Degradação Graciosa

```lua
-- Teste de degradação graciosa
local function testGracefulDegradation()
    local features = {
        "advanced_ui",
        "enhanced_graphics",
        "extended_protocols"
    }
    
    for _, feature in ipairs(features) do
        local result = testFeatureDegradation(feature)
        if result.degradation_successful then
            print("✅ Degradação graciosa: " .. feature)
        else
            print("❌ Falha na degradação: " .. feature)
        end
    end
end
```

---

## 🔧 Ferramentas de Migração

### 📊 Análise Automática

```python
# Script de análise automática
def analyze_migration_compatibility(source, target):
    """Analisa compatibilidade entre sistemas."""
    
    analysis = {
        'source': source,
        'target': target,
        'compatibility_score': 0,
        'issues': [],
        'recommendations': []
    }
    
    # Analisar APIs
    api_compatibility = analyze_api_compatibility(source, target)
    analysis['api_compatibility'] = api_compatibility
    
    # Analisar protocolos
    protocol_compatibility = analyze_protocol_compatibility(source, target)
    analysis['protocol_compatibility'] = protocol_compatibility
    
    # Analisar recursos
    resource_compatibility = analyze_resource_compatibility(source, target)
    analysis['resource_compatibility'] = resource_compatibility
    
    # Calcular score geral
    analysis['compatibility_score'] = calculate_overall_score(analysis)
    
    return analysis
```

### 🔄 Conversão Automática

```python
# Script de conversão automática
def convert_code(source_code, source_system, target_system):
    """Converte código entre sistemas."""
    
    converted_code = source_code
    
    # Converter APIs
    converted_code = convert_apis(converted_code, source_system, target_system)
    
    # Converter protocolos
    converted_code = convert_protocols(converted_code, source_system, target_system)
    
    # Converter recursos
    converted_code = convert_resources(converted_code, source_system, target_system)
    
    return converted_code
```

### 🧪 Validação Automática

```python
# Script de validação automática
def validate_migration(source_system, target_system, converted_code):
    """Valida migração convertida."""
    
    validation_results = {
        'syntax_valid': False,
        'api_compatible': False,
        'protocol_compatible': False,
        'performance_acceptable': False,
        'tests_passing': False
    }
    
    # Validar sintaxe
    validation_results['syntax_valid'] = validate_syntax(converted_code)
    
    # Validar APIs
    validation_results['api_compatible'] = validate_apis(converted_code, target_system)
    
    # Validar protocolos
    validation_results['protocol_compatible'] = validate_protocols(converted_code, target_system)
    
    # Validar performance
    validation_results['performance_acceptable'] = validate_performance(converted_code)
    
    # Executar testes
    validation_results['tests_passing'] = run_tests(converted_code)
    
    return validation_results
```

---

## 📋 Checklists de Migração

### ✅ Checklist OTClient → Canary

- [ ] **Preparação**
  - [ ] Análise de compatibilidade executada
  - [ ] Backup do código criado
  - [ ] Recursos Canary verificados
  - [ ] Plano de migração definido

- [ ] **Adaptação**
  - [ ] APIs convertidas para Canary
  - [ ] Protocolos adaptados
  - [ ] UI modernizada
  - [ ] Scripts otimizados

- [ ] **Testes**
  - [ ] Testes de compatibilidade passando
  - [ ] Testes de performance aprovados
  - [ ] Testes de integração concluídos
  - [ ] Validação manual realizada

- [ ] **Deploy**
  - [ ] Código migrado validado
  - [ ] Documentação atualizada
  - [ ] Deploy em ambiente de teste
  - [ ] Deploy em produção

### ✅ Checklist Canary → OTClient

- [ ] **Análise**
  - [ ] Dependências identificadas
  - [ ] Funcionalidades avançadas mapeadas
  - [ ] Recursos necessários verificados
  - [ ] Plano de simplificação definido

- [ ] **Adaptação**
  - [ ] UI simplificada
  - [ ] Protocolos compatibilizados
  - [ ] Scripts adaptados
  - [ ] Recursos avançados removidos

- [ ] **Validação**
  - [ ] Compatibilidade reversa verificada
  - [ ] Degradação graciosa testada
  - [ ] Performance validada
  - [ ] Funcionalidade essencial mantida

- [ ] **Deploy**
  - [ ] Código compatível validado
  - [ ] Documentação atualizada
  - [ ] Deploy em ambiente de teste
  - [ ] Deploy em produção

---

## 📚 Recursos Adicionais

### 🔗 Links Úteis

- **Documentação Unificada**: [wiki/docs/otclient_canary_unified_documentation.md](wiki/docs/otclient_canary_unified_documentation.md)
- **Integration Agent**: [wiki/bmad/agents/integration_agent.py](wiki/bmad/agents/integration_agent.py)
- **Integration Workflow**: [wiki/bmad/workflows/integration_workflow.py](wiki/bmad/workflows/integration_workflow.py)

### 📖 Referências

- **API Reference OTClient**: [wiki/otclient/api/](wiki/otclient/api/)
- **API Reference Canary**: [wiki/canary/api/](wiki/canary/api/)
- **Protocolos de Rede**: [wiki/protocols/](wiki/protocols/)

### 🛠️ Ferramentas

- **Análise de Compatibilidade**: `python check_compatibility.py`
- **Conversão Automática**: `python convert_code.py`
- **Validação de Migração**: `python validate_migration.py`

---

## 📝 Histórico de Versões

### v1.0.0 (2025-01-27)
- ✅ Guias de migração OTClient → Canary
- ✅ Guias de migração Canary → OTClient
- ✅ Ferramentas de análise automática
- ✅ Scripts de conversão automática
- ✅ Checklists de validação
- ✅ Testes de compatibilidade

---

*Guias criados pelo Sistema BMAD - Integração Total OTClient-Canary* 