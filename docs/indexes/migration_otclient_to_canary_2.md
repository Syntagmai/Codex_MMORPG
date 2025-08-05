---
tags: [migration, otclient, canary, guide, integration, development]
type: documentation
status: active
priority: high
created: 2025-01-27
updated: 2025-01-27
aliases: [otclient_to_canary_migration, migration_guide, otclient_migration]
---

# 🔄 Guia de Migração: OTClient → Canary

## 📋 Visão Geral

Este guia fornece instruções detalhadas para migrar projetos e módulos do **OTClient** para o **Canary**, garantindo compatibilidade e funcionalidade completa no novo ambiente.

### 🎯 Objetivo

Migrar código OTClient para Canary de forma segura e eficiente, mantendo:
- ✅ Funcionalidade completa
- ✅ Performance otimizada
- ✅ Compatibilidade de protocolos
- ✅ Interface de usuário consistente

---

## 🔍 **1. Preparação para Migração**

### 📊 Análise de Compatibilidade

#### **Verificação Automática**
```bash
# Executar análise de compatibilidade
python check_compatibility.py --source otclient --target canary --module meu_modulo

# Gerar relatório detalhado
python generate_migration_report.py --source otclient --target canary --output relatorio_migracao.json
```

#### **Checklist de Preparação**
- [ ] **Análise de dependências** - Verificar módulos e bibliotecas
- [ ] **Verificação de APIs** - Identificar APIs específicas OTClient
- [ ] **Análise de protocolos** - Validar compatibilidade de rede
- [ ] **Verificação de recursos** - Confirmar disponibilidade no Canary
- [ ] **Backup do código** - Criar backup completo antes da migração

### 🛠️ Ferramentas de Migração

#### **Scripts de Análise**
```python
# Análise de compatibilidade
def analyze_compatibility(module_path: str) -> Dict[str, Any]:
    """Analisa compatibilidade de um módulo OTClient com Canary"""
    
    analysis = {
        "compatibility_score": 0.0,
        "issues_found": [],
        "suggestions": [],
        "migration_steps": []
    }
    
    # Verificar APIs específicas OTClient
    otclient_apis = detect_otclient_apis(module_path)
    for api in otclient_apis:
        if not is_canary_compatible(api):
            analysis["issues_found"].append(f"API não compatível: {api}")
            analysis["suggestions"].append(f"Substituir {api} por equivalente Canary")
    
    # Calcular score de compatibilidade
    analysis["compatibility_score"] = calculate_compatibility_score(analysis)
    
    return analysis
```

---

## 🔧 **2. Adaptação de Código**

### 📦 Módulos Core

#### **Sistema de UI**
#### Nível Basic
```lua
-- Código original OTClient
local function createOTClientUI()
    local button = g_ui.createWidget('Button', parent)
    button:setText("Clique aqui")
    button.onClick = function()
        print("Botão clicado!")
    end
end

-- Código adaptado para Canary
local function createCanaryUI()
    if Canary then
        -- Implementação Canary
        local button = UI.createButton({
            text = "Clique aqui",
            onClick = function()
                print("Botão clicado!")
            end
        })
    else
        -- Fallback OTClient
        local button = g_ui.createWidget('Button', parent)
        button:setText("Clique aqui")
        button.onClick = function()
            print("Botão clicado!")
        end
    end
end
```

#### Nível Intermediate
```lua
-- Código original OTClient
local function createOTClientUI()
    local button = g_ui.createWidget('Button', parent)
    button:setText("Clique aqui")
    button.onClick = function()
        print("Botão clicado!")
    end
end

-- Código adaptado para Canary
local function createCanaryUI()
    if Canary then
        -- Implementação Canary
        local button = UI.createButton({
            text = "Clique aqui",
            onClick = function()
                print("Botão clicado!")
            end
        })
    else
        -- Fallback OTClient
        local button = g_ui.createWidget('Button', parent)
        button:setText("Clique aqui")
        button.onClick = function()
            print("Botão clicado!")
        end
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
-- Código original OTClient
local function createOTClientUI()
    local button = g_ui.createWidget('Button', parent)
    button:setText("Clique aqui")
    button.onClick = function()
        print("Botão clicado!")
    end
end

-- Código adaptado para Canary
local function createCanaryUI()
    if Canary then
        -- Implementação Canary
        local button = UI.createButton({
            text = "Clique aqui",
            onClick = function()
                print("Botão clicado!")
            end
        })
    else
        -- Fallback OTClient
        local button = g_ui.createWidget('Button', parent)
        button:setText("Clique aqui")
        button.onClick = function()
            print("Botão clicado!")
        end
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

#### **Sistema de Rede**
#### Nível Basic
```lua
-- Código original OTClient
local function connectOTClient()
    g_game.connect(server, port)
    g_game.login(username, password)
end

-- Código adaptado para Canary
local function connectCanary()
    if Canary then
        -- Implementação Canary
        Network.connect({
            host = server,
            port = port,
            onConnect = function()
                Network.login(username, password)
            end
        })
    else
        -- Fallback OTClient
        g_game.connect(server, port)
        g_game.login(username, password)
    end
end
```

#### Nível Intermediate
```lua
-- Código original OTClient
local function connectOTClient()
    g_game.connect(server, port)
    g_game.login(username, password)
end

-- Código adaptado para Canary
local function connectCanary()
    if Canary then
        -- Implementação Canary
        Network.connect({
            host = server,
            port = port,
            onConnect = function()
                Network.login(username, password)
            end
        })
    else
        -- Fallback OTClient
        g_game.connect(server, port)
        g_game.login(username, password)
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
-- Código original OTClient
local function connectOTClient()
    g_game.connect(server, port)
    g_game.login(username, password)
end

-- Código adaptado para Canary
local function connectCanary()
    if Canary then
        -- Implementação Canary
        Network.connect({
            host = server,
            port = port,
            onConnect = function()
                Network.login(username, password)
            end
        })
    else
        -- Fallback OTClient
        g_game.connect(server, port)
        g_game.login(username, password)
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

### 🎮 Sistemas de Jogo

#### **Sistema de Criaturas**
#### Nível Basic
```lua
-- Código original OTClient
local function createCreatureOTClient()
    local creature = g_map.getCreatureById(creatureId)
    if creature then
        creature:setOutfit(outfit)
        creature:setDirection(direction)
    end
end

-- Código adaptado para Canary
local function createCreatureCanary()
    if Canary then
        -- Implementação Canary
        local creature = Game.Creature.getById(creatureId)
        if creature then
            creature:setOutfit(outfit)
            creature:setDirection(direction)
        end
    else
        -- Fallback OTClient
        local creature = g_map.getCreatureById(creatureId)
        if creature then
            creature:setOutfit(outfit)
            creature:setDirection(direction)
        end
    end
end
```

#### Nível Intermediate
```lua
-- Código original OTClient
local function createCreatureOTClient()
    local creature = g_map.getCreatureById(creatureId)
    if creature then
        creature:setOutfit(outfit)
        creature:setDirection(direction)
    end
end

-- Código adaptado para Canary
local function createCreatureCanary()
    if Canary then
        -- Implementação Canary
        local creature = Game.Creature.getById(creatureId)
        if creature then
            creature:setOutfit(outfit)
            creature:setDirection(direction)
        end
    else
        -- Fallback OTClient
        local creature = g_map.getCreatureById(creatureId)
        if creature then
            creature:setOutfit(outfit)
            creature:setDirection(direction)
        end
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
-- Código original OTClient
local function createCreatureOTClient()
    local creature = g_map.getCreatureById(creatureId)
    if creature then
        creature:setOutfit(outfit)
        creature:setDirection(direction)
    end
end

-- Código adaptado para Canary
local function createCreatureCanary()
    if Canary then
        -- Implementação Canary
        local creature = Game.Creature.getById(creatureId)
        if creature then
            creature:setOutfit(outfit)
            creature:setDirection(direction)
        end
    else
        -- Fallback OTClient
        local creature = g_map.getCreatureById(creatureId)
        if creature then
            creature:setOutfit(outfit)
            creature:setDirection(direction)
        end
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

---

## 🧪 **3. Testes de Migração**

### 📊 Testes de Compatibilidade

#### **Suite de Testes Automatizados**
```python
# Teste de compatibilidade
def test_migration_compatibility():
    """Executa testes de compatibilidade após migração"""
    
    test_cases = [
        "ui_components",
        "network_protocols", 
        "game_systems",
        "file_formats",
        "performance_metrics"
    ]
    
    results = {}
    
    for test_case in test_cases:
        print(f"🧪 Executando teste: {test_case}")
        result = run_compatibility_test(test_case)
        results[test_case] = result
        
        if result["success"]:
            print(f"✅ {test_case}: PASS")
        else:
            print(f"❌ {test_case}: FAIL - {result['error']}")
    
    return generate_test_report(results)
```

#### **Testes de Performance**
```lua
-- Teste de performance
    --  Teste de performance (traduzido)
local function testPerformance()
    local startTime = os.clock()
    
    -- Executar operação migrada
    performMigratedOperation()
    
    local endTime = os.clock()
    local duration = endTime - startTime
    
    -- Validar performance
    --  Validar performance (traduzido)
    if duration > MAX_ACCEPTABLE_TIME then
    -- Verificação condicional
        print("⚠️ Performance abaixo do esperado: " .. duration .. "s")
        return false
    else
        print("✅ Performance aceitável: " .. duration .. "s")
        return true
    end
end
```

### 🔍 Validação de Funcionalidade

#### **Checklist de Validação**
- [ ] **Interface de usuário** - Todos os elementos visuais funcionando
- [ ] **Comunicação de rede** - Conexão e protocolos funcionando
- [ ] **Sistemas de jogo** - Criaturas, itens, magias funcionando
- [ ] **Performance** - Tempo de resposta aceitável
- [ ] **Estabilidade** - Sem crashes ou erros críticos
- [ ] **Compatibilidade** - Funciona com versões antigas

---

## 🚀 **4. Deploy e Validação**

### 📦 Processo de Deploy

#### **Script de Deploy Automatizado**
```bash
#!/bin/bash
# deploy_migration.sh

echo "🚀 Iniciando deploy da migração..."

# 1. Backup do sistema atual
echo "📦 Criando backup..."
python create_backup.py --target canary

# 2. Deploy do código migrado
echo "🔧 Deployando código migrado..."
python deploy_migrated_code.py --source otclient --target canary

# 3. Validação pós-deploy
echo "🧪 Validando deploy..."
python validate_deployment.py --target canary

# 4. Testes de integração
echo "🔍 Executando testes de integração..."
python run_integration_tests.py --target canary

echo "✅ Deploy concluído!"
```

### 📊 Monitoramento Pós-Deploy

#### **Métricas de Monitoramento**
```lua
-- Sistema de monitoramento
    --  Sistema de monitoramento (traduzido)
local MigrationMonitor = require('monitor.migration')

-- Configurar monitoramento
    --  Configurar monitoramento (traduzido)
MigrationMonitor.configure({
    check_interval = 5000, -- 5 segundos
    alert_threshold = 0.9, -- 90%
    metrics = {
        "performance",
        "stability", 
        "compatibility",
        "user_satisfaction"
    }
})

-- Iniciar monitoramento
    --  Iniciar monitoramento (traduzido)
MigrationMonitor.start()
```

---

## 🔧 **5. Resolução de Problemas**

### 🚨 Problemas Comuns

#### **Problema: APIs Incompatíveis**
```lua
-- Solução: Implementar wrapper de compatibilidade
local CompatibilityWrapper = {}

function CompatibilityWrapper.createUIElement(elementType, config)
    -- Função: CompatibilityWrapper
    if Canary then
    -- Verificação condicional
        return CanaryUI.create(elementType, config)
    else
        return g_ui.createWidget(elementType, config.parent)
    end
end
```

#### **Problema: Diferenças de Protocolo**
```lua
-- Solução: Adaptador de protocolo
local ProtocolAdapter = {}

function ProtocolAdapter.sendMessage(message)
    -- Função: ProtocolAdapter
    if Canary then
    -- Verificação condicional
        return CanaryProtocol.send(message)
    else
        return g_game.sendMessage(message)
    end
end
```

### 📋 Troubleshooting Guide

| Problema | Sintoma | Solução |
|----------|---------|---------|
| **UI não renderiza** | Elementos invisíveis | Verificar APIs de UI |
| **Conexão falha** | Timeout de rede | Validar protocolos |
| **Performance lenta** | Lag ou travamentos | Otimizar código |
| **Crashes** | Erros críticos | Verificar compatibilidade |

---

## 📚 **6. Recursos Adicionais**

### 🔗 **Links Automáticos**

> [!info] **Links Gerados Automaticamente**
> Estes links foram criados automaticamente pelo sistema de linkagem da categoria **Documentation**

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]

### **🧭 Navegação**
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]
- [[../maps/category_indices|Índices por Categoria]]
- [[../maps/relationships|Relacionamentos]]

### **📊 Métricas da Categoria**
- **Categoria**: Documentation
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

## 🔗 Links Úteis
- **Documentação Canary**: [wiki/canary/](wiki/canary/)
- **APIs Unificadas**: [wiki/docs/otclient_canary_unified_documentation.md](wiki/docs/otclient_canary_unified_documentation.md)
- **Testes de Integração**: [wiki/integration/](wiki/integration/)

### 🛠️ Ferramentas
- **Integration Agent**: [wiki/bmad/agents/integration_agent.py](wiki/bmad/agents/integration_agent.py)
- **Migration Workflow**: [wiki/bmad/workflows/migration_workflow.py](wiki/bmad/workflows/migration_workflow.py)

---

## 📝 **Histórico de Versões**

### v1.0.0 (2025-01-27)
- ✅ Guia de migração OTClient → Canary
- ✅ Scripts de análise de compatibilidade
- ✅ Templates de código adaptado
- ✅ Testes de validação
- ✅ Troubleshooting guide

---

*Guia criado pelo Sistema BMAD - Integração Total OTClient-Canary* 