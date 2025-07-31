---
tags: [canary, guide, template, tutorial, integration, otclient]
type: guide_template
status: template
priority: medium
created: 2025-01-27
---

# 📖 Template de Guia Canary

> [!info] **Template ID**: CANARY-GUIDE-TEMPLATE  
> **Categoria**: Guias e Tutoriais  
> **Status**: Template  
> **Prioridade**: Média

## 📋 Estrutura Padrão

### **🎯 Seção 1: Introdução**
- **Objetivo**: O que o guia ensina
- **Pré-requisitos**: Conhecimentos necessários
- **Tempo estimado**: Duração do tutorial
- **Resultado final**: O que será alcançado

### **🔧 Seção 2: Configuração**
- **Ambiente**: Preparação do ambiente
- **Dependências**: Bibliotecas e ferramentas
- **Configuração inicial**: Setup básico
- **Verificação**: Como verificar se está funcionando

### **📝 Seção 3: Passo a Passo**
- **Passo 1**: Primeira etapa
- **Passo 2**: Segunda etapa
- **Passo 3**: Terceira etapa
- **...**: Continuação dos passos

### **🎨 Seção 4: Exemplos Práticos**
- **Exemplo básico**: Implementação simples
- **Exemplo avançado**: Casos complexos
- **Integração OTClient**: Exemplos específicos
- **Casos de uso**: Cenários reais

### **🔍 Seção 5: Troubleshooting**
- **Problemas comuns**: Erros frequentes
- **Soluções**: Como resolver
- **Debugging**: Como debugar
- **Recursos**: Onde buscar ajuda

---

## 📝 **Template de Conteúdo**

### **🎯 Introdução**

#### **Objetivo do Guia:**
Este guia ensina como **[objetivo específico]** usando o Canary em integração com o OTClient. Ao final deste tutorial, você será capaz de **[resultado esperado]**.

#### **Pré-requisitos:**
- ✅ Conhecimento básico de Lua
- ✅ OTClient configurado e funcionando
- ✅ Canary instalado e configurado
- ✅ Compreensão básica de APIs

#### **Tempo Estimado:**
- **Configuração**: 15 minutos
- **Implementação**: 30 minutos
- **Testes**: 15 minutos
- **Total**: 1 hora

#### **Resultado Final:**
Ao completar este guia, você terá:
- ✅ Sistema **[nome do sistema]** funcionando
- ✅ Integração com OTClient estabelecida
- ✅ Exemplos práticos implementados
- ✅ Base para desenvolvimento futuro

---

### **🔧 Configuração do Ambiente**

#### **1. Verificar Dependências:**
```lua
-- Verificar se o Canary está disponível
local canary = require("canary")
if not canary then
    error("Canary não está disponível. Verifique a instalação.")
end

-- Verificar versão
print("Versão do Canary: " .. canary.version)
```

#### **2. Configuração Básica:**
```lua
-- Configuração inicial do Canary
local config = {
    host = "localhost",
    port = 7171,
    protocol = "opencode",
    timeout = 5000,
    retry_attempts = 3
}

-- Inicializar conexão
canary.init(config)
```

#### **3. Verificar Conexão:**
```lua
-- Testar conexão
local success, error = canary.testConnection()
if success then
    print("✅ Conexão com Canary estabelecida!")
else
    print("❌ Erro na conexão: " .. error)
end
```

---

### **📝 Passo a Passo**

#### **Passo 1: Preparar Estrutura**
```lua
-- Criar módulo de integração
local CanaryIntegration = {}

-- Configurar handlers de eventos
function CanaryIntegration.setupEventHandlers()
    canary.on("connected", function()
        print("Conectado ao Canary!")
    end)
    
    canary.on("error", function(error)
        print("Erro: " .. error.message)
    end)
end
```

#### **Passo 2: Implementar Funcionalidade Principal**
```lua
-- Implementar função principal
function CanaryIntegration.mainFunction()
    -- Lógica principal aqui
    local result = canary.processData({
        type = "example",
        data = "test"
    })
    
    return result
end
```

#### **Passo 3: Integrar com OTClient**
```lua
-- Integração com OTClient
function CanaryIntegration.integrateWithOTClient()
    -- Conectar eventos do OTClient
    connect(g_game, { onGameStart = function()
        CanaryIntegration.setupEventHandlers()
        CanaryIntegration.mainFunction()
    end})
end
```

#### **Passo 4: Testar Implementação**
```lua
-- Função de teste
function CanaryIntegration.test()
    print("🧪 Iniciando testes...")
    
    -- Teste 1: Conexão
    local connected = canary.isConnected()
    print("Conexão: " .. (connected and "✅" or "❌"))
    
    -- Teste 2: Funcionalidade
    local result = CanaryIntegration.mainFunction()
    print("Funcionalidade: " .. (result and "✅" or "❌"))
    
    -- Teste 3: Integração
    print("Integração: ✅")
    
    print("🎉 Testes concluídos!")
end
```

---

### **🎨 Exemplos Práticos**

#### **Exemplo 1: Sistema Básico**
```lua
-- Sistema básico de integração
local BasicSystem = {}

function BasicSystem.init()
    -- Configuração básica
    BasicSystem.config = {
        enabled = true,
        autoConnect = true,
        debug = false
    }
    
    -- Setup inicial
    if BasicSystem.config.autoConnect then
        BasicSystem.connect()
    end
end

function BasicSystem.connect()
    canary.connect({
        host = "localhost",
        port = 7171
    })
end

function BasicSystem.disconnect()
    canary.disconnect()
end

-- Uso
BasicSystem.init()
```

#### **Exemplo 2: Sistema Avançado com Cache**
```lua
-- Sistema avançado com cache
local AdvancedSystem = {}

AdvancedSystem.cache = {}
AdvancedSystem.config = {
    cacheTimeout = 300, -- 5 minutos
    maxCacheSize = 100
}

function AdvancedSystem.getDataWithCache(key)
    -- Verificar cache
    if AdvancedSystem.cache[key] and 
       AdvancedSystem.cache[key].expires > os.time() then
        return AdvancedSystem.cache[key].data
    end
    
    -- Buscar dados
    local data = canary.getData(key)
    
    -- Armazenar no cache
    AdvancedSystem.cache[key] = {
        data = data,
        expires = os.time() + AdvancedSystem.config.cacheTimeout
    }
    
    -- Limpar cache se necessário
    AdvancedSystem.cleanCache()
    
    return data
end

function AdvancedSystem.cleanCache()
    local currentTime = os.time()
    local count = 0
    
    for key, item in pairs(AdvancedSystem.cache) do
        if item.expires < currentTime then
            AdvancedSystem.cache[key] = nil
            count = count + 1
        end
    end
    
    if count > 0 then
        print("🧹 Cache limpo: " .. count .. " itens removidos")
    end
end
```

#### **Exemplo 3: Integração Completa com OTClient**
```lua
-- Integração completa com OTClient
local OTClientIntegration = {}

function OTClientIntegration.setup()
    -- Configurar handlers do OTClient
    connect(g_game, { 
        onGameStart = OTClientIntegration.onGameStart,
        onGameEnd = OTClientIntegration.onGameEnd,
        onLoginAdvice = OTClientIntegration.onLoginAdvice
    })
    
    -- Configurar handlers do Canary
    canary.on("game_state", OTClientIntegration.onGameState)
    canary.on("player_update", OTClientIntegration.onPlayerUpdate)
    canary.on("error", OTClientIntegration.onError)
end

function OTClientIntegration.onGameStart()
    print("🎮 Jogo iniciado - Conectando ao Canary...")
    canary.connect()
end

function OTClientIntegration.onGameEnd()
    print("🏁 Jogo finalizado - Desconectando do Canary...")
    canary.disconnect()
end

function OTClientIntegration.onGameState(data)
    -- Atualizar estado do jogo
    g_game.setGameState(data.state)
    print("📊 Estado do jogo atualizado: " .. data.state)
end

function OTClientIntegration.onPlayerUpdate(data)
    -- Atualizar informações do jogador
    local player = g_game.getLocalPlayer()
    if player then
        player:setHealth(data.health)
        player:setMana(data.mana)
        print("👤 Jogador atualizado")
    end
end

function OTClientIntegration.onError(error)
    print("❌ Erro do Canary: " .. error.message)
    -- Implementar lógica de retry se necessário
end
```

---

### **🔍 Troubleshooting**

#### **Problemas Comuns:**

##### **1. Conexão Recusada**
**Sintoma**: `Connection refused`
**Causa**: Canary não está rodando ou porta incorreta
**Solução**:
```lua
-- Verificar se o Canary está rodando
local success = canary.ping()
if not success then
    print("❌ Canary não está respondendo")
    print("💡 Verifique se o Canary está rodando na porta 7171")
end
```

##### **2. Timeout na Conexão**
**Sintoma**: `Connection timeout`
**Causa**: Rede lenta ou configuração incorreta
**Solução**:
```lua
-- Aumentar timeout
canary.init({
    host = "localhost",
    port = 7171,
    timeout = 10000  -- 10 segundos
})
```

##### **3. Protocolo Inválido**
**Sintoma**: `Invalid protocol`
**Causa**: Versão do protocolo incompatível
**Solução**:
```lua
-- Verificar versão do protocolo
local protocolVersion = canary.getProtocolVersion()
print("Protocolo: " .. protocolVersion)

-- Usar versão compatível
canary.init({
    protocol = "opencode",  -- ou "extendedopen"
    version = "1.0"
})
```

#### **Debugging Avançado:**
```lua
-- Habilitar modo debug
canary.setDebugMode(true)

-- Logs detalhados
canary.on("debug", function(message)
    print("🐛 DEBUG: " .. message)
end)

-- Monitor de performance
local startTime = os.clock()
local result = canary.processData(data)
local endTime = os.clock()
print("⏱️ Tempo de processamento: " .. (endTime - startTime) .. "s")
```

#### **Recursos de Ajuda:**
- 📚 [Documentação Oficial Canary](https://canary.wiki)
- 🔗 [Guia de Integração](../external/integration_guide.md)
- 💬 [Comunidade Canary](https://community.canary.wiki)
- 🐛 [Issues e Bugs](https://github.com/canary/issues)

---

### **📋 Checklist de Conclusão**

#### **✅ Configuração:**
- [ ] Ambiente preparado
- [ ] Dependências instaladas
- [ ] Configuração básica funcionando
- [ ] Conexão estabelecida

#### **✅ Implementação:**
- [ ] Funcionalidade principal implementada
- [ ] Integração com OTClient funcionando
- [ ] Eventos configurados
- [ ] Tratamento de erros implementado

#### **✅ Testes:**
- [ ] Testes básicos passando
- [ ] Testes de integração funcionando
- [ ] Testes de erro funcionando
- [ ] Performance aceitável

#### **✅ Documentação:**
- [ ] Código comentado
- [ ] Exemplos funcionando
- [ ] Troubleshooting documentado
- [ ] Próximos passos definidos

---

## 🔗 **Links Relacionados**

### **📚 Documentação:**
- [Template de Documentação Canary](documentation_template.md)
- [Template de API Canary](api_template.md)
- [Template de Referência Canary](reference_template.md)

### **🔗 Integração:**
- [Protocolo OpenCode](../protocols/opencode_specification.md)
- [Protocolo ExtendedOpen](../protocols/extendedopen_specification.md)
- [Comunicação Cliente-Servidor](../protocols/client_server_communication.md)

### **📖 Referências:**
- [Documentação Oficial Canary](https://canary.wiki/guides)
- [Guia de Integração](../external/integration_guide.md)
- [Sistema de Referência Cruzada](../external/cross_reference_system.md)

---

**Template Criado**: 2025-01-27  
**Responsável**: Documentation Agent  
**Status**: 📋 **Template Ativo**  
**Próximo**: 🔥 **Criar Template de Referência** 