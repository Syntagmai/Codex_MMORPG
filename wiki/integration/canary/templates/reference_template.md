---
tags: [canary, reference, template, documentation, integration, otclient]
type: reference_template
status: template
priority: medium
created: 2025-01-27
---

# 📚 Template de Referência Canary

> [!info] **Template ID**: CANARY-REFERENCE-TEMPLATE  
> **Categoria**: Documentação de Referência  
> **Status**: Template  
> **Prioridade**: Média

## 📋 Estrutura Padrão

### **🎯 Seção 1: Visão Geral**
- **Nome**: Identificação da referência
- **Versão**: Versão documentada
- **Categoria**: Tipo de referência
- **Compatibilidade**: Versões suportadas

### **📖 Seção 2: Referência Completa**
- **Métodos**: Todos os métodos disponíveis
- **Propriedades**: Propriedades e atributos
- **Eventos**: Eventos emitidos
- **Constantes**: Constantes definidas

### **🔧 Seção 3: Exemplos de Uso**
- **Exemplos básicos**: Uso simples
- **Exemplos avançados**: Casos complexos
- **Padrões**: Padrões de uso comuns
- **Anti-padrões**: O que evitar

### **🔍 Seção 4: Detalhes Técnicos**
- **Implementação**: Como funciona internamente
- **Performance**: Considerações de performance
- **Limitações**: Limitações conhecidas
- **Dependências**: Dependências internas

### **📋 Seção 5: Índice e Busca**
- **Índice alfabético**: Lista ordenada
- **Índice por categoria**: Agrupamento lógico
- **Busca rápida**: Referência rápida
- **Links relacionados**: Referências cruzadas

---

## 📝 **Template de Conteúdo**

### **🎯 Visão Geral**

#### **Informações Básicas:**
- **Nome**: [Nome da Referência]
- **Versão**: v1.0.0
- **Categoria**: [API/Classe/Sistema/Protocolo]
- **Compatibilidade**: Canary v1.0.0+, OTClient v1.0.0+

#### **Descrição:**
Esta referência documenta **[descrição da funcionalidade]** do Canary, fornecendo informações completas sobre **[aspectos específicos]** para integração com o OTClient.

#### **Uso Principal:**
- **Desenvolvimento**: Para desenvolvedores criando integrações
- **Manutenção**: Para manutenção de sistemas existentes
- **Debugging**: Para resolução de problemas
- **Otimização**: Para melhorias de performance

---

### **📖 Referência Completa**

#### **Métodos Principais:**

##### **`canary.methodName(param1, param2)`**
**Descrição**: Descrição detalhada do método
**Parâmetros**:
- `param1` (type): Descrição do parâmetro
- `param2` (type): Descrição do parâmetro
**Retorno**: `type` - Descrição do retorno
**Exemplo**:
```lua
local result = canary.methodName("value1", "value2")
print(result)
```

##### **`canary.asyncMethod(param, callback)`**
**Descrição**: Método assíncrono
**Parâmetros**:
- `param` (type): Parâmetro de entrada
- `callback` (function): Função de callback
**Retorno**: `void`
**Exemplo**:
```lua
canary.asyncMethod("data", function(result)
    print("Resultado: " .. result)
end)
```

#### **Propriedades:**

##### **`canary.propertyName`**
**Tipo**: `type`
**Descrição**: Descrição da propriedade
**Acesso**: Read/Write
**Exemplo**:
```lua
-- Ler propriedade
local value = canary.propertyName

-- Definir propriedade
canary.propertyName = "new value"
```

##### **`canary.readOnlyProperty`**
**Tipo**: `type`
**Descrição**: Propriedade somente leitura
**Acesso**: Read Only
**Exemplo**:
```lua
local value = canary.readOnlyProperty
-- canary.readOnlyProperty = "value" -- ERRO!
```

#### **Eventos:**

##### **`canary:on("eventName", callback)`**
**Descrição**: Evento emitido quando **[condição]**
**Parâmetros do Callback**:
- `data` (object): Dados do evento
- `timestamp` (number): Timestamp do evento
**Exemplo**:
```lua
canary:on("eventName", function(data, timestamp)
    print("Evento recebido: " .. data.message)
end)
```

##### **`canary:once("eventName", callback)`**
**Descrição**: Evento que executa apenas uma vez
**Parâmetros**: Mesmos do evento normal
**Exemplo**:
```lua
canary:once("eventName", function(data)
    print("Evento único: " .. data.message)
end)
```

#### **Constantes:**

##### **`canary.CONSTANT_NAME`**
**Valor**: `value`
**Descrição**: Descrição da constante
**Uso**: Para **[propósito específico]**
**Exemplo**:
```lua
if status == canary.CONSTANT_NAME then
    print("Status correto")
end
```

---

### **🔧 Exemplos de Uso**

#### **Exemplo 1: Uso Básico**
```lua
-- Configuração básica
local canary = require("canary")

-- Inicializar
canary.init({
    host = "localhost",
    port = 7171
})

-- Conectar
canary.connect()

-- Escutar eventos
canary:on("connected", function()
    print("Conectado!")
end)
```

#### **Exemplo 2: Uso Avançado**
```lua
-- Sistema avançado com múltiplos handlers
local AdvancedUsage = {}

function AdvancedUsage.setup()
    -- Configurar handlers
    canary:on("data", AdvancedUsage.handleData)
    canary:on("error", AdvancedUsage.handleError)
    canary:on("disconnect", AdvancedUsage.handleDisconnect)
    
    -- Configurar propriedades
    canary.timeout = 10000
    canary.retryAttempts = 3
end

function AdvancedUsage.handleData(data)
    -- Processar dados
    if data.type == "game_state" then
        AdvancedUsage.updateGameState(data)
    elseif data.type == "player_info" then
        AdvancedUsage.updatePlayerInfo(data)
    end
end

function AdvancedUsage.handleError(error)
    -- Tratar erros
    print("Erro: " .. error.message)
    
    if error.code == canary.ERROR_CONNECTION_LOST then
        AdvancedUsage.reconnect()
    end
end

function AdvancedUsage.handleDisconnect()
    -- Reconectar automaticamente
    print("Desconectado, tentando reconectar...")
    AdvancedUsage.reconnect()
end

function AdvancedUsage.reconnect()
    canary.connect()
end
```

#### **Exemplo 3: Padrões de Uso**
```lua
-- Padrão: Singleton para integração
local CanaryIntegration = {}

function CanaryIntegration.getInstance()
    if not CanaryIntegration.instance then
        CanaryIntegration.instance = {
            connected = false,
            handlers = {},
            config = {}
        }
    end
    return CanaryIntegration.instance
end

function CanaryIntegration.setup(config)
    local instance = CanaryIntegration.getInstance()
    instance.config = config
    
    -- Configurar handlers
    canary:on("connected", function()
        instance.connected = true
        CanaryIntegration.onConnected()
    end)
    
    canary:on("disconnected", function()
        instance.connected = false
        CanaryIntegration.onDisconnected()
    end)
end

function CanaryIntegration.onConnected()
    print("Canary conectado!")
    -- Lógica adicional
end

function CanaryIntegration.onDisconnected()
    print("Canary desconectado!")
    -- Lógica adicional
end
```

#### **Exemplo 4: Anti-padrões (O que evitar)**
```lua
-- ❌ ANTI-PADRÃO: Não fazer isso
function badExample()
    -- Não verificar se está conectado
    canary.sendData("data") -- Pode falhar
    
    -- Não tratar erros
    local result = canary.processData("data") -- Pode quebrar
    
    -- Não limpar handlers
    canary:on("event", function() end) -- Memory leak
end

-- ✅ PADRÃO CORRETO
function goodExample()
    -- Verificar conexão
    if not canary.isConnected() then
        print("Não conectado!")
        return
    end
    
    -- Tratar erros
    local success, result = pcall(function()
        return canary.processData("data")
    end)
    
    if not success then
        print("Erro: " .. result)
        return
    end
    
    -- Limpar handlers quando necessário
    local handler = function() end
    canary:on("event", handler)
    
    -- Limpar quando não precisar mais
    canary:off("event", handler)
end
```

---

### **🔍 Detalhes Técnicos**

#### **Implementação Interna:**
```lua
-- Estrutura interna (simplificada)
local CanaryInternal = {
    socket = nil,
    handlers = {},
    config = {},
    connected = false
}

function CanaryInternal.connect()
    -- Implementação da conexão
    CanaryInternal.socket = createSocket()
    CanaryInternal.socket:connect(CanaryInternal.config.host, CanaryInternal.config.port)
end

function CanaryInternal.handleMessage(message)
    -- Processamento de mensagens
    local event = message.event
    local data = message.data
    
    if CanaryInternal.handlers[event] then
        for _, handler in ipairs(CanaryInternal.handlers[event]) do
            handler(data)
        end
    end
end
```

#### **Performance:**
- **Conexão**: Estabelecimento em ~100ms
- **Mensagens**: Processamento em ~1ms
- **Memory**: ~1MB por instância
- **CPU**: Baixo impacto (< 1% em uso normal)

#### **Limitações:**
- **Conexões simultâneas**: Máximo 1 por instância
- **Tamanho de mensagem**: Máximo 1MB
- **Rate limiting**: 1000 mensagens/segundo
- **Timeout**: 30 segundos por operação

#### **Dependências:**
- **LuaSocket**: Para comunicação de rede
- **LuaJSON**: Para serialização de dados
- **LuaTimer**: Para timeouts e retry

---

### **📋 Índice e Busca**

#### **Índice Alfabético:**
- **A**
  - `canary.asyncMethod()` - Método assíncrono
  - `canary.autoReconnect` - Propriedade de reconexão automática
- **B**
  - `canary.broadcast()` - Enviar mensagem para todos
- **C**
  - `canary.connect()` - Conectar ao servidor
  - `canary.CONNECTION_TIMEOUT` - Constante de timeout
- **D**
  - `canary.disconnect()` - Desconectar do servidor
- **E**
  - `canary.emit()` - Emitir evento
  - `canary.ERROR_*` - Constantes de erro
- **F**
  - `canary.formatMessage()` - Formatar mensagem
- **G**
  - `canary.getStatus()` - Obter status da conexão
- **H**
  - `canary.handleEvent()` - Manipular evento
- **I**
  - `canary.init()` - Inicializar sistema
  - `canary.isConnected()` - Verificar se está conectado
- **J**
  - `canary.join()` - Entrar em grupo
- **K**
  - `canary.keepAlive` - Propriedade de keep-alive
- **L**
  - `canary.leave()` - Sair de grupo
- **M**
  - `canary.messageQueue` - Fila de mensagens
- **N**
  - `canary.name` - Nome da instância
- **O**
  - `canary.off()` - Remover handler de evento
  - `canary.on()` - Adicionar handler de evento
  - `canary.once()` - Handler de evento único
- **P**
  - `canary.ping()` - Testar conectividade
  - `canary.processData()` - Processar dados
- **Q**
  - `canary.queue` - Fila de operações
- **R**
  - `canary.reconnect()` - Reconectar
  - `canary.retryAttempts` - Tentativas de retry
- **S**
  - `canary.send()` - Enviar dados
  - `canary.status` - Status atual
- **T**
  - `canary.timeout` - Timeout de operações
- **U**
  - `canary.update()` - Atualizar sistema
- **V**
  - `canary.version` - Versão do sistema
- **W**
  - `canary.wait()` - Aguardar operação
- **X**
  - `canary.xhr()` - Requisição HTTP
- **Y**
  - `canary.yield()` - Ceder controle
- **Z**
  - `canary.zeroConfig` - Configuração zero

#### **Índice por Categoria:**

##### **🔗 Conexão:**
- `connect()`, `disconnect()`, `reconnect()`
- `isConnected()`, `getStatus()`
- `ping()`, `timeout`, `retryAttempts`

##### **📡 Comunicação:**
- `send()`, `broadcast()`, `emit()`
- `on()`, `off()`, `once()`
- `handleEvent()`, `processData()`

##### **⚙️ Configuração:**
- `init()`, `update()`, `version`
- `name`, `autoReconnect`, `keepAlive`
- `messageQueue`, `queue`

##### **🔧 Utilitários:**
- `formatMessage()`, `wait()`, `yield()`
- `xhr()`, `zeroConfig`

#### **Busca Rápida:**

##### **Por Funcionalidade:**
- **Conexão**: `connect`, `disconnect`, `reconnect`
- **Eventos**: `on`, `off`, `once`, `emit`
- **Dados**: `send`, `processData`, `formatMessage`
- **Status**: `isConnected`, `getStatus`, `ping`

##### **Por Tipo:**
- **Métodos**: Todos os métodos disponíveis
- **Propriedades**: Todas as propriedades
- **Eventos**: Todos os eventos
- **Constantes**: Todas as constantes

---

## 🔗 **Links Relacionados**

### **📚 Documentação:**
- [Template de Documentação Canary](documentation_template.md)
- [Template de API Canary](api_template.md)
- [Template de Guia Canary](guide_template.md)

### **🔗 Integração:**
- [Protocolo OpenCode](../protocols/opencode_specification.md)
- [Protocolo ExtendedOpen](../protocols/extendedopen_specification.md)
- [Comunicação Cliente-Servidor](../protocols/client_server_communication.md)

### **📖 Referências:**
- [Documentação Oficial Canary](https://canary.wiki/reference)
- [Guia de Integração](../external/integration_guide.md)
- [Sistema de Referência Cruzada](../external/cross_reference_system.md)

---

**Template Criado**: 2025-01-27  
**Responsável**: Documentation Agent  
**Status**: 📋 **Template Ativo**  
**Próximo**: 🔥 **Task 2.4 - Protocolos** 