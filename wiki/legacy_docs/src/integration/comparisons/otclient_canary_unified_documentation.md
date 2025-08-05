
# Documentação Unificada OTClient-Canary

## 📋 Visão Geral

Esta documentação unifica a documentação dos sistemas **OTClient** e **Canary**, fornecendo uma visão integrada do ecossistema completo de desenvolvimento de clientes para Open Tibia.

### 🎯 Objetivo

Criar uma documentação única e abrangente que permita aos desenvolvedores:
- Entender ambos os sistemas de forma integrada
- Identificar pontos de integração e compatibilidade
- Desenvolver aplicações que funcionem em ambos os ambientes
- Migrar facilmente entre OTClient e Canary

---

## 🏗️ Arquitetura Unificada

### 📁 Estrutura de Diretórios

```
📁 Sistema Unificado OTClient-Canary
├── 📚 Documentação
│   ├── 📖 Guias de Desenvolvimento
│   ├── 🔧 Referências de API
│   ├── 🎨 Templates e Exemplos
│   └── 🔗 Guias de Integração
├── 🔧 Código-Fonte
│   ├── 📦 Módulos Lua
│   ├── 🔧 Scripts Python
│   ├── 📄 Configurações
│   └── 🧪 Testes
├── 🤖 Agentes BMAD
│   ├── 🔄 Workflows de Integração
│   ├── 📊 Relatórios
│   └── 🔍 Validações
└── 🗺️ Mapas e Índices
    ├── 📍 Navegação JSON
    ├── 🏷️ Tags e Categorias
    └── 🔗 Relacionamentos
```

### 🔄 Fluxo de Integração

```
1. 📋 Preparação
   ├── Validação de estrutura
   ├── Verificação de compatibilidade
   └── Criação de templates

2. 🔧 Desenvolvimento
   ├── Código compartilhado
   ├── APIs unificadas
   └── Testes integrados

3. 🧪 Validação
   ├── Testes de compatibilidade
   ├── Validação de performance
   └── Verificação de integridade

4. 🚀 Deploy
   ├── Build unificado
   ├── Deploy automatizado
   └── Monitoramento
```

---

## 📚 Guias de Desenvolvimento

### 🚀 Primeiros Passos

#### 1. Configuração do Ambiente

```bash
# Clonar repositório unificado
git clone https://github.com/otclient/otclient_canary_unified.git
cd otclient_canary_unified

# Instalar dependências
pip install -r requirements.txt

# Configurar ambiente
python setup_integration.py
```

#### 2. Estrutura de Projeto

#### Nível Basic
```lua
-- Exemplo de módulo unificado
local UnifiedModule = {}

function UnifiedModule.init()
    -- Inicialização compatível com ambos os sistemas
    if OTClient then
        -- Código específico OTClient
    elseif Canary then
        -- Código específico Canary
    else
        -- Código compartilhado
    end
end

function UnifiedModule.integrate()
    -- Lógica de integração
    return true
end

return UnifiedModule
```

#### Nível Intermediate
```lua
-- Exemplo de módulo unificado
local UnifiedModule = {}

function UnifiedModule.init()
    -- Inicialização compatível com ambos os sistemas
    if OTClient then
        -- Código específico OTClient
    elseif Canary then
        -- Código específico Canary
    else
        -- Código compartilhado
    end
end

function UnifiedModule.integrate()
    -- Lógica de integração
    return true
end

return UnifiedModule
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
-- Exemplo de módulo unificado
local UnifiedModule = {}

function UnifiedModule.init()
    -- Inicialização compatível com ambos os sistemas
    if OTClient then
        -- Código específico OTClient
    elseif Canary then
        -- Código específico Canary
    else
        -- Código compartilhado
    end
end

function UnifiedModule.integrate()
    -- Lógica de integração
    return true
end

return UnifiedModule
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

#### 3. APIs Unificadas

```lua
-- API unificada para UI
    --  API unificada para UI (traduzido)
local UnifiedUI = {
    -- Componentes compartilhados
    --  Componentes compartilhados (traduzido)
    Button = require('ui.unified.button'),
    TextEdit = require('ui.unified.textedit'),
    Window = require('ui.unified.window'),
    
    -- Sistema de eventos unificado
    --  Sistema de eventos unificado (traduzido)
    EventSystem = require('events.unified'),
    
    -- Gerenciamento de estado
    --  Gerenciamento de estado (traduzido)
    StateManager = require('state.unified')
}

-- API unificada para Game
    --  API unificada para Game (traduzido)
local UnifiedGame = {
    -- Sistema de criaturas
    --  Sistema de criaturas (traduzido)
    Creature = require('game.unified.creature'),
    
    -- Sistema de itens
    --  Sistema de itens (traduzido)
    Item = require('game.unified.item'),
    
    -- Sistema de magias
    --  Sistema de magias (traduzido)
    Spell = require('game.unified.spell'),
    
    -- Sistema de combate
    --  Sistema de combate (traduzido)
    Combat = require('game.unified.combat')
}
```

---

## 🔧 Referências de API

### 📦 Módulos Core

#### UI System

```lua
-- Sistema de UI unificado
    --  Sistema de UI unificado (traduzido)
local UI = require('ui.unified')

-- Criar botão
local button = UI.Button.create({
    text = "Clique aqui",
    onClick = function()
        print("Botão clicado!")
    end
})

-- Criar janela
    --  Criar janela (traduzido)
local window = UI.Window.create({
    title = "Minha Janela",
    size = {width = 300, height = 200}
})
```

#### Game System

```lua
-- Sistema de jogo unificado
    --  Sistema de jogo unificado (traduzido)
local Game = require('game.unified')

-- Criar criatura
    --  Criar criatura (traduzido)
local creature = Game.Creature.create({
    name = "Monstro",
    health = 100,
    maxHealth = 100
})

-- Criar item
    --  Criar item (traduzido)
local item = Game.Item.create({
    id = 2160,
    count = 1,
    name = "Crystal Coin"
})
```

#### Network System

```lua
-- Sistema de rede unificado
    --  Sistema de rede unificado (traduzido)
local Network = require('network.unified')

-- Conectar ao servidor
    --  Conectar ao servidor (traduzido)
Network.connect({
    host = "localhost",
    port = 7171,
    onConnect = function()
        print("Conectado!")
    end,
    onDisconnect = function()
        print("Desconectado!")
    end
})
```

### 🎨 Templates de Desenvolvimento

#### Template de Módulo

#### Nível Basic
```lua
-- Template para módulo unificado
local ModuleTemplate = {}

-- Metadados do módulo
ModuleTemplate.metadata = {
    name = "Meu Módulo",
    version = "1.0.0",
    author = "Desenvolvedor",
    description = "Descrição do módulo",
    compatible = {"otclient", "canary"}
}

-- Inicialização
function ModuleTemplate.init()
    -- Código de inicialização
end

-- Configuração
function ModuleTemplate.configure(config)
    -- Código de configuração
end

-- Execução
function ModuleTemplate.execute()
    -- Código de execução
end

-- Limpeza
function ModuleTemplate.cleanup()
    -- Código de limpeza
end

return ModuleTemplate
```

#### Nível Intermediate
```lua
-- Template para módulo unificado
local ModuleTemplate = {}

-- Metadados do módulo
ModuleTemplate.metadata = {
    name = "Meu Módulo",
    version = "1.0.0",
    author = "Desenvolvedor",
    description = "Descrição do módulo",
    compatible = {"otclient", "canary"}
}

-- Inicialização
function ModuleTemplate.init()
    -- Código de inicialização
end

-- Configuração
function ModuleTemplate.configure(config)
    -- Código de configuração
end

-- Execução
function ModuleTemplate.execute()
    -- Código de execução
end

-- Limpeza
function ModuleTemplate.cleanup()
    -- Código de limpeza
end

return ModuleTemplate
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
-- Template para módulo unificado
local ModuleTemplate = {}

-- Metadados do módulo
ModuleTemplate.metadata = {
    name = "Meu Módulo",
    version = "1.0.0",
    author = "Desenvolvedor",
    description = "Descrição do módulo",
    compatible = {"otclient", "canary"}
}

-- Inicialização
function ModuleTemplate.init()
    -- Código de inicialização
end

-- Configuração
function ModuleTemplate.configure(config)
    -- Código de configuração
end

-- Execução
function ModuleTemplate.execute()
    -- Código de execução
end

-- Limpeza
function ModuleTemplate.cleanup()
    -- Código de limpeza
end

return ModuleTemplate
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

#### Template de Interface

#### Nível Basic
```lua
-- Template para interface unificada
local InterfaceTemplate = {}

function InterfaceTemplate.create()
    local interface = {
        -- Propriedades
        visible = false,
        draggable = true,
        
        -- Métodos
        show = function(self)
            self.visible = true
            -- Código específico para mostrar
        end,
        
        hide = function(self)
            self.visible = false
            -- Código específico para esconder
        end,
        
        update = function(self)
            -- Código de atualização
        end
    }
    
    return interface
end

return InterfaceTemplate
```

#### Nível Intermediate
```lua
-- Template para interface unificada
local InterfaceTemplate = {}

function InterfaceTemplate.create()
    local interface = {
        -- Propriedades
        visible = false,
        draggable = true,
        
        -- Métodos
        show = function(self)
            self.visible = true
            -- Código específico para mostrar
        end,
        
        hide = function(self)
            self.visible = false
            -- Código específico para esconder
        end,
        
        update = function(self)
            -- Código de atualização
        end
    }
    
    return interface
end

return InterfaceTemplate
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
-- Template para interface unificada
local InterfaceTemplate = {}

function InterfaceTemplate.create()
    local interface = {
        -- Propriedades
        visible = false,
        draggable = true,
        
        -- Métodos
        show = function(self)
            self.visible = true
            -- Código específico para mostrar
        end,
        
        hide = function(self)
            self.visible = false
            -- Código específico para esconder
        end,
        
        update = function(self)
            -- Código de atualização
        end
    }
    
    return interface
end

return InterfaceTemplate
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

## 🔗 Guias de Integração

### 🔄 Migração OTClient → Canary

#### 1. Preparação

```bash
# Verificar compatibilidade
python check_compatibility.py --source otclient --target canary

# Gerar relatório de migração
python generate_migration_report.py --source otclient --target canary
```

#### 2. Adaptação de Código

#### Nível Basic
```lua
-- Código original OTClient
local function oldFunction()
    -- Código específico OTClient
end

-- Código adaptado para Canary
local function newFunction()
    if Canary then
        -- Código específico Canary
    else
        -- Código original OTClient
    end
end
```

#### Nível Intermediate
```lua
-- Código original OTClient
local function oldFunction()
    -- Código específico OTClient
end

-- Código adaptado para Canary
local function newFunction()
    if Canary then
        -- Código específico Canary
    else
        -- Código original OTClient
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
local function oldFunction()
    -- Código específico OTClient
end

-- Código adaptado para Canary
local function newFunction()
    if Canary then
        -- Código específico Canary
    else
        -- Código original OTClient
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

#### 3. Testes de Migração

```lua
-- Teste de compatibilidade
    --  Teste de compatibilidade (traduzido)
local function testCompatibility()
    local tests = {
        "ui_components",
        "game_systems", 
        "network_protocols",
        "file_formats"
    }
    
    for _, test in ipairs(tests) do
    -- Loop de repetição
        local result = runTest(test)
        if not result.success then
    -- Verificação condicional
            print("Falha no teste: " .. test)
        end
    end
end
```

### 🔄 Migração Canary → OTClient

#### 1. Verificação de Recursos

```lua
-- Verificar recursos disponíveis
local function checkResources()
    local resources = {
        "advanced_ui",
        "enhanced_graphics",
        "extended_protocols"
    }
    
    for _, resource in ipairs(resources) do
    -- Loop de repetição
        if not isResourceAvailable(resource) then
    -- Verificação condicional
            print("Recurso não disponível: " .. resource)
        end
    end
end
```

#### 2. Adaptação de Funcionalidades

#### Nível Basic
```lua
-- Adaptar funcionalidades avançadas
local function adaptAdvancedFeatures()
    if OTClient then
        -- Implementar versão simplificada
        return implementBasicVersion()
    else
        -- Usar versão completa Canary
        return implementAdvancedVersion()
    end
end
```

#### Nível Intermediate
```lua
-- Adaptar funcionalidades avançadas
local function adaptAdvancedFeatures()
    if OTClient then
        -- Implementar versão simplificada
        return implementBasicVersion()
    else
        -- Usar versão completa Canary
        return implementAdvancedVersion()
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
-- Adaptar funcionalidades avançadas
local function adaptAdvancedFeatures()
    if OTClient then
        -- Implementar versão simplificada
        return implementBasicVersion()
    else
        -- Usar versão completa Canary
        return implementAdvancedVersion()
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

## 🧪 Sistema de Testes

### 📊 Testes de Compatibilidade

```python
# Teste de compatibilidade unificado
def test_compatibility():
    """Executa testes de compatibilidade entre OTClient e Canary."""
    
    test_suites = [
        "ui_compatibility",
        "game_logic_compatibility", 
        "network_compatibility",
        "file_format_compatibility"
    ]
    
    results = {}
    
    for suite in test_suites:
        results[suite] = run_compatibility_test(suite)
    
    return generate_compatibility_report(results)
```

### 🔍 Testes de Integração

```python
# Teste de integração
def test_integration():
    """Executa testes de integração entre sistemas."""
    
    integration_tests = [
        "data_migration",
        "api_compatibility",
        "performance_validation",
        "error_handling"
    ]
    
    for test in integration_tests:
        result = execute_integration_test(test)
        validate_test_result(result)
```

---

## 📈 Métricas e Monitoramento

### 📊 Métricas de Performance

#### Nível Basic
```lua
-- Sistema de métricas unificado
local Metrics = require('metrics.unified')
-- Coletar métricas
-- Gerar relatório
```

#### Nível Intermediate
```lua
-- Sistema de métricas unificado
local Metrics = require('metrics.unified')

-- Coletar métricas
Metrics.collect({
    category = "performance",
    metrics = {
        "fps",
        "memory_usage", 
        "network_latency",
        "response_time"
    }
})

-- Gerar relatório
Metrics.generateReport({
    format = "json",
    include = {"performance", "compatibility", "integration"}
})
```

#### Nível Advanced
```lua
-- Sistema de métricas unificado
local Metrics = require('metrics.unified')

-- Coletar métricas
Metrics.collect({
    category = "performance",
    metrics = {
        "fps",
        "memory_usage", 
        "network_latency",
        "response_time"
    }
})

-- Gerar relatório
Metrics.generateReport({
    format = "json",
    include = {"performance", "compatibility", "integration"}
})
```

### 🔍 Monitoramento de Integração

```lua
-- Monitor de integração
local IntegrationMonitor = require('monitor.integration')

-- Configurar monitoramento
    --  Configurar monitoramento (traduzido)
IntegrationMonitor.configure({
    check_interval = 5000, -- 5 segundos
    alert_threshold = 0.8, -- 80%
    metrics = {"compatibility", "performance", "stability"}
})

-- Iniciar monitoramento
    --  Iniciar monitoramento (traduzido)
IntegrationMonitor.start()
```

---

## 🚀 Deploy e Distribuição

### 📦 Build Unificado

```bash
# Script de build unificado
#!/bin/bash

echo "Iniciando build unificado..."

# Build OTClient
echo "Build OTClient..."
python build_otclient.py

# Build Canary  
echo "Build Canary..."
python build_canary.py

# Build integrado
echo "Build integrado..."
python build_integrated.py

# Validação
echo "Validando builds..."
python validate_builds.py

echo "Build concluído!"
```

### 🚀 Deploy Automatizado

```python
# Script de deploy automatizado
def deploy_unified():
    """Executa deploy unificado dos sistemas."""
    
    # Preparar ambiente
    prepare_deployment_environment()
    
    # Executar builds
    build_otclient()
    build_canary()
    build_integrated()
    
    # Validar builds
    validate_builds()
    
    # Deploy
    deploy_to_production()
    
    # Monitoramento pós-deploy
    start_post_deployment_monitoring()
```

---

## 📚 Recursos Adicionais

### 🔗 Links Úteis

- **Documentação OTClient**: [wiki/otclient/](wiki/otclient/)
- **Documentação Canary**: [wiki/canary/](wiki/canary/)
- **Guias de Integração**: [wiki/integration/](wiki/integration/)
- **Exemplos de Código**: [wiki/examples/](wiki/examples/)

### 📖 Referências

- **API Reference OTClient**: [wiki/otclient/api/](wiki/otclient/api/)
- **API Reference Canary**: [wiki/canary/api/](wiki/canary/api/)
- **Protocolos de Rede**: [wiki/protocols/](wiki/protocols/)
- **Formatos de Arquivo**: [wiki/formats/](wiki/formats/)

### 🛠️ Ferramentas

- **Integration Agent**: [wiki/bmad/agents/integration_agent.py](wiki/bmad/agents/integration_agent.py)
- **Integration Workflow**: [wiki/bmad/workflows/integration_workflow.py](wiki/bmad/workflows/integration_workflow.py)
- **Organization Agent**: [wiki/bmad/agents/intelligent_organization_agent.py](wiki/bmad/agents/intelligent_organization_agent.py)

---

## 📝 Histórico de Versões

### v1.0.0 (2025-01-27)
- ✅ Criação da documentação unificada
- ✅ Integração de APIs OTClient e Canary
- ✅ Templates de desenvolvimento
- ✅ Guias de migração
- ✅ Sistema de testes unificado
- ✅ Métricas e monitoramento

---

*Documentação criada pelo Sistema BMAD - Integração Total OTClient-Canary* 