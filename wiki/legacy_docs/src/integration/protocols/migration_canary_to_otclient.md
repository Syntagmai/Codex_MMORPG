
# 🔄 Guia de Migração: Canary → OTClient

## 📋 Visão Geral

Este guia fornece instruções detalhadas para migrar projetos e módulos do **Canary** para o **OTClient**, adaptando funcionalidades avançadas para compatibilidade com o ambiente OTClient.

### 🎯 Objetivo

Migrar código Canary para OTClient de forma segura e eficiente, mantendo:
- ✅ Funcionalidade essencial
- ✅ Performance otimizada
- ✅ Compatibilidade de protocolos
- ✅ Interface de usuário funcional

---

## 🔍 **1. Preparação para Migração**

### 📊 Análise de Recursos

#### **Verificação de Recursos Disponíveis**
```bash
# Executar análise de recursos
python check_resources.py --source canary --target otclient --module meu_modulo

# Gerar relatório de limitações
python generate_limitations_report.py --source canary --target otclient --output relatorio_limitacoes.json
```

#### **Checklist de Preparação**
- [ ] **Análise de funcionalidades** - Identificar recursos avançados Canary
- [ ] **Verificação de APIs** - Mapear APIs específicas Canary
- [ ] **Análise de protocolos** - Validar compatibilidade com OTClient
- [ ] **Verificação de limitações** - Identificar recursos não disponíveis
- [ ] **Backup do código** - Criar backup completo antes da migração

### 🛠️ Ferramentas de Análise

#### **Scripts de Análise de Recursos**
```python
# Análise de recursos disponíveis
def analyze_resource_availability(module_path: str) -> Dict[str, Any]:
    """Analisa disponibilidade de recursos Canary no OTClient"""
    
    analysis = {
        "availability_score": 0.0,
        "missing_features": [],
        "workarounds": [],
        "migration_complexity": "low"
    }
    
    # Verificar recursos avançados Canary
    canary_features = detect_canary_features(module_path)
    for feature in canary_features:
        if not is_otclient_available(feature):
            analysis["missing_features"].append(feature)
            analysis["workarounds"].append(generate_workaround(feature))
    
    # Calcular score de disponibilidade
    analysis["availability_score"] = calculate_availability_score(analysis)
    
    return analysis
```

---

## 🔧 **2. Adaptação de Funcionalidades**

### 📦 Recursos Avançados

#### **Sistema de UI Avançado**
#### Inicialização e Configuração
```lua
-- Código original Canary
local function createAdvancedCanaryUI()
    local advancedButton = AdvancedUI.createButton({
        text = "Botão Avançado",
        animations = {
            hover = "fade_in",
            click = "bounce"
        },
        effects = {
            glow = true,
            shadow = true
        },
        onClick = function()
            print("Botão avançado clicado!")
        end
    })
end

-- Código adaptado para OTClient
local function createBasicOTClientUI()
    if OTClient then
        -- Implementação básica OTClient
        local button = g_ui.createWidget('Button', parent)
        button:setText("Botão Avançado")
        
        -- Simular efeitos básicos
        button.onHoverChange = function(widget, hovered)
            if hovered then
                widget:setOpacity(0.8)
            else
                widget:setOpacity(1.0)
            end
```

#### Funcionalidade 1
```lua
        end
        
        button.onClick = function()
            print("Botão avançado clicado!")
        end
    else
        -- Fallback Canary
        local advancedButton = AdvancedUI.createButton({
            text = "Botão Avançado",
            animations = {
                hover = "fade_in",
                click = "bounce"
            },
            effects = {
                glow = true,
                shadow = true
            },
            onClick = function()
                print("Botão avançado clicado!")
            end
        })
```

#### Finalização
```lua
    end
end
```

#### **Sistema de Rede Avançado**
#### Inicialização e Configuração
```lua
-- Código original Canary
local function connectAdvancedCanary()
    AdvancedNetwork.connect({
        host = server,
        port = port,
        encryption = "AES256",
        compression = true,
        retry_policy = {
            max_attempts = 5,
            backoff_delay = 1000
        },
        onConnect = function()
            AdvancedNetwork.login(username, password)
        end
    })
end

-- Código adaptado para OTClient
local function connectBasicOTClient()
    if OTClient then
        -- Implementação básica OTClient
        g_game.connect(server, port)
        g_game.login(username, password)
        
        -- Implementar retry básico
        local retryCount = 0
        local maxRetries = 3
        
        g_game.onConnectionError = function()
            if retryCount < maxRetries then
                retryCount = retryCount + 1
                print("Tentativa " .. retryCount .. " de reconexão...")
                scheduleEvent(function()
                    g_game.connect(server, port)
                end, 2000)
```

#### Finalização
```lua
            end
        end
    else
        -- Fallback Canary
        AdvancedNetwork.connect({
            host = server,
            port = port,
            encryption = "AES256",
            compression = true,
            retry_policy = {
                max_attempts = 5,
                backoff_delay = 1000
            },
            onConnect = function()
                AdvancedNetwork.login(username, password)
            end
        })
    end
end
```

### 🎮 Sistemas de Jogo Avançados

#### **Sistema de Criaturas Avançado**
#### Inicialização e Configuração
```lua
-- Código original Canary
local function createAdvancedCreatureCanary()
    local advancedCreature = AdvancedGame.Creature.create({
        id = creatureId,
        outfit = outfit,
        direction = direction,
        animations = {
            walk = "smooth_walk",
            attack = "combo_attack",
            death = "dramatic_death"
        },
        effects = {
            aura = "magical_glow",
            particles = "sparkle_trail"
        },
        ai = {
            behavior = "aggressive",
            pathfinding = "advanced"
        }
    })
end
```

#### Funcionalidade 1
```lua

-- Código adaptado para OTClient
local function createBasicCreatureOTClient()
    if OTClient then
        -- Implementação básica OTClient
        local creature = g_map.getCreatureById(creatureId)
        if creature then
            creature:setOutfit(outfit)
            creature:setDirection(direction)
            
            -- Simular efeitos básicos
            if outfit and outfit.mount then
                -- Adicionar efeito básico de montaria
                creature:setMount(outfit.mount)
            end
        end
    else
        -- Fallback Canary
        local advancedCreature = AdvancedGame.Creature.create({
            id = creatureId,
            outfit = outfit,
            direction = direction,
            animations = {
                walk = "smooth_walk",
                attack = "combo_attack",
                death = "dramatic_death"
            },
```

#### Finalização
```lua
            effects = {
                aura = "magical_glow",
                particles = "sparkle_trail"
            },
            ai = {
                behavior = "aggressive",
                pathfinding = "advanced"
            }
        })
    end
end
```

---

## 🧪 **3. Testes de Compatibilidade**

### 📊 Testes de Funcionalidade

#### **Suite de Testes de Recursos**
```python
# Teste de recursos disponíveis
def test_resource_availability():
    """Executa testes de disponibilidade de recursos"""
    
    test_cases = [
        "basic_ui_components",
        "advanced_ui_features", 
        "network_protocols",
        "game_systems",
        "performance_metrics"
    ]
    
    results = {}
    
    for test_case in test_cases:
        print(f"🧪 Testando recursos: {test_case}")
        result = test_resource_availability(test_case)
        results[test_case] = result
        
        if result["available"]:
            print(f"✅ {test_case}: DISPONÍVEL")
        else:
            print(f"⚠️ {test_case}: NÃO DISPONÍVEL - {result['workaround']}")
    
    return generate_resource_report(results)
```

#### **Testes de Performance**
```lua
-- Teste de performance adaptada
    --  Teste de performance adaptada (traduzido)
local function testAdaptedPerformance()
    local startTime = os.clock()
    
    -- Executar operação adaptada
    performAdaptedOperation()
    
    local endTime = os.clock()
    local duration = endTime - startTime
    
    -- Validar performance adaptada
    --  Validar performance adaptada (traduzido)
    if duration > MAX_ADAPTED_TIME then
    -- Verificação condicional
        print("⚠️ Performance adaptada abaixo do esperado: " .. duration .. "s")
        return false
    else
        print("✅ Performance adaptada aceitável: " .. duration .. "s")
        return true
    end
end
```

### 🔍 Validação de Funcionalidade

#### **Checklist de Validação**
- [ ] **Interface básica** - Elementos essenciais funcionando
- [ ] **Comunicação de rede** - Conexão básica funcionando
- [ ] **Sistemas de jogo** - Funcionalidades core funcionando
- [ ] **Performance** - Tempo de resposta aceitável
- [ ] **Estabilidade** - Sem crashes ou erros críticos
- [ ] **Compatibilidade** - Funciona com versões OTClient

---

## 🚀 **4. Deploy e Validação**

### 📦 Processo de Deploy Adaptado

#### **Script de Deploy com Adaptações**
```bash
#!/bin/bash
# deploy_adapted_migration.sh

echo "🚀 Iniciando deploy da migração adaptada..."

# 1. Backup do sistema atual
echo "📦 Criando backup..."
python create_backup.py --target otclient

# 2. Deploy do código adaptado
echo "🔧 Deployando código adaptado..."
python deploy_adapted_code.py --source canary --target otclient

# 3. Validação pós-deploy
echo "🧪 Validando deploy adaptado..."
python validate_adapted_deployment.py --target otclient

# 4. Testes de compatibilidade
echo "🔍 Executando testes de compatibilidade..."
python run_compatibility_tests.py --target otclient

echo "✅ Deploy adaptado concluído!"
```

### 📊 Monitoramento de Adaptação

#### **Métricas de Monitoramento**
```lua
-- Sistema de monitoramento adaptado
    --  Sistema de monitoramento adaptado (traduzido)
local AdaptationMonitor = require('monitor.adaptation')

-- Configurar monitoramento
    --  Configurar monitoramento (traduzido)
AdaptationMonitor.configure({
    check_interval = 5000, -- 5 segundos
    alert_threshold = 0.8, -- 80%
    metrics = {
        "basic_functionality",
        "performance_adapted", 
        "compatibility",
        "user_satisfaction"
    }
})

-- Iniciar monitoramento
    --  Iniciar monitoramento (traduzido)
AdaptationMonitor.start()
```

---

## 🔧 **5. Resolução de Problemas**

### 🚨 Problemas Comuns de Adaptação

#### **Problema: Recursos Avançados Não Disponíveis**
#### Nível Basic
```lua
-- Solução: Implementar versão simplificada
local AdaptationLayer = {}

function AdaptationLayer.createAdvancedFeature(config)
    if OTClient then
        -- Versão simplificada para OTClient
        return createBasicVersion(config)
    else
        -- Versão completa para Canary
        return createAdvancedVersion(config)
    end
end
```

#### Nível Intermediate
```lua
-- Solução: Implementar versão simplificada
local AdaptationLayer = {}

function AdaptationLayer.createAdvancedFeature(config)
    if OTClient then
        -- Versão simplificada para OTClient
        return createBasicVersion(config)
    else
        -- Versão completa para Canary
        return createAdvancedVersion(config)
    end
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
-- Solução: Implementar versão simplificada
local AdaptationLayer = {}

function AdaptationLayer.createAdvancedFeature(config)
    if OTClient then
        -- Versão simplificada para OTClient
        return createBasicVersion(config)
    else
        -- Versão completa para Canary
        return createAdvancedVersion(config)
    end
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

#### **Problema: APIs Incompatíveis**
#### Nível Basic
```lua
-- Solução: Adaptador de API
local APIAdapter = {}

function APIAdapter.callAdvancedAPI(apiName, params)
    if OTClient then
        -- Mapear para API básica OTClient
        return mapToBasicAPI(apiName, params)
    else
        -- Usar API avançada Canary
        return callAdvancedAPI(apiName, params)
    end
end
```

#### Nível Intermediate
```lua
-- Solução: Adaptador de API
local APIAdapter = {}

function APIAdapter.callAdvancedAPI(apiName, params)
    if OTClient then
        -- Mapear para API básica OTClient
        return mapToBasicAPI(apiName, params)
    else
        -- Usar API avançada Canary
        return callAdvancedAPI(apiName, params)
    end
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
-- Solução: Adaptador de API
local APIAdapter = {}

function APIAdapter.callAdvancedAPI(apiName, params)
    if OTClient then
        -- Mapear para API básica OTClient
        return mapToBasicAPI(apiName, params)
    else
        -- Usar API avançada Canary
        return callAdvancedAPI(apiName, params)
    end
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

### 📋 Troubleshooting Guide

| Problema | Sintoma | Solução |
|----------|---------|---------|
| **Recursos avançados não funcionam** | Funcionalidades faltando | Implementar versão básica |
| **Performance degradada** | Lag ou travamentos | Otimizar código adaptado |
| **Interface simplificada** | Menos recursos visuais | Usar elementos básicos |
| **Funcionalidades limitadas** | Recursos não disponíveis | Implementar workarounds |

---

## 📚 **6. Recursos Adicionais**

### 🔗 Links Úteis
- **Documentação OTClient**: [wiki/otclient/](wiki/otclient/)
- **APIs Unificadas**: [wiki/docs/otclient_canary_unified_documentation.md](wiki/docs/otclient_canary_unified_documentation.md)
- **Guias de Compatibilidade**: [wiki/integration/](wiki/integration/)

### 🛠️ Ferramentas
- **Integration Agent**: [wiki/bmad/agents/integration_agent.py](wiki/bmad/agents/integration_agent.py)
- **Adaptation Workflow**: [wiki/bmad/workflows/adaptation_workflow.py](wiki/bmad/workflows/adaptation_workflow.py)

---

## 📝 **Histórico de Versões**

### v1.0.0 (2025-01-27)
- ✅ Guia de migração Canary → OTClient
- ✅ Scripts de análise de recursos
- ✅ Templates de código adaptado
- ✅ Testes de compatibilidade
- ✅ Troubleshooting guide

---

*Guia criado pelo Sistema BMAD - Integração Total OTClient-Canary* 