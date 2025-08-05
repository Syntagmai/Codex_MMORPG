---
tags: [bmad, agent, template, system]
type: template
aliases: [Agent Template, Template de Agente]
status: template
---

# Template de Agente BMAD

## 📋 Informações do Agente

- **Nome**: [Nome do Agente]
- **Tipo**: [Especialização]
- **Versão**: 1.0
- **Status**: Ativo
- **Criado em**: [Data]

## 🎯 Propósito

[Descrição clara do propósito e responsabilidades do agente]

## 🧠 Capacidades

### ✅ **Habilidades Principais**
- [Habilidade 1]
- [Habilidade 2]
- [Habilidade 3]

### 🔧 **Ferramentas Disponíveis**
- [Ferramenta 1]
- [Ferramenta 2]
- [Ferramenta 3]

### 📚 **Conhecimento Especializado**
- [Área de conhecimento 1]
- [Área de conhecimento 2]
- [Área de conhecimento 3]

## 🔄 Workflow Padrão

### 1. **Recebimento de Tarefa**
```lua
-- Exemplo de recebimento
    --  Exemplo de recebimento (traduzido)
function receiveTask(task)
    -- Função: receiveTask
    -- Processamento da tarefa
    --  Processamento da tarefa (traduzido)
end
```

### 2. **Análise de Contexto**
```lua
-- Exemplo de análise
function analyzeContext(context)
    -- Função: analyzeContext
    -- Análise do contexto
end
```

### 3. **Execução**
```lua
-- Exemplo de execução
function executeTask(task)
    -- Função: executeTask
    -- Execução da tarefa
end
```

### 4. **Relatório**
```lua
-- Exemplo de relatório
function generateReport(results)
    -- Função: generateReport
    -- Geração do relatório
end
```

## 🔗 **Links Automáticos**

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

## 🔗 Integração

### **Agentes Relacionados**
- [Agente relacionado 1] - [Tipo de relação]
- [Agente relacionado 2] - [Tipo de relação]

### **Sistemas Externos**
- [Sistema 1] - [Tipo de integração]
- [Sistema 2] - [Tipo de integração]

## 📊 Métricas de Performance

### **Indicadores de Sucesso**
- [Métrica 1]: [Meta]
- [Métrica 2]: [Meta]
- [Métrica 3]: [Meta]

### **Monitoramento**
- [Indicador de monitoramento 1]
- [Indicador de monitoramento 2]

## 🔧 Configuração

### **Parâmetros Padrão**
#### Nível Basic
```json
{
  "timeout": 300,
  "retry_attempts": 3,
  "priority": "medium"
}
```

#### Nível Intermediate
```json
{
  "timeout": 300,
  "retry_attempts": 3,
  "priority": "medium"
}
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```json
{
  "timeout": 300,
  "retry_attempts": 3,
  "priority": "medium"
}
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

### **Variáveis de Ambiente**
- `AGENT_LOG_LEVEL`: [Nível de log]
- `AGENT_TIMEOUT`: [Timeout em segundos]
- `AGENT_MODE`: [Modo de operação]

## 📝 Exemplos de Uso

### **Cenário 1: [Descrição]**
#### Nível Basic
```lua
-- Exemplo de código
local agent = AgentTemplate.new()
agent:processTask("exemplo_tarefa")
```

#### Nível Intermediate
```lua
-- Exemplo de código
local agent = AgentTemplate.new()
agent:processTask("exemplo_tarefa")
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
-- Exemplo de código
local agent = AgentTemplate.new()
agent:processTask("exemplo_tarefa")
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

### **Cenário 2: [Descrição]**
#### Nível Basic
```lua
-- Exemplo de código
local result = agent:analyzeData(data)
```

#### Nível Intermediate
```lua
-- Exemplo de código
local result = agent:analyzeData(data)
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
-- Exemplo de código
local result = agent:analyzeData(data)
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

## 🚨 Tratamento de Erros

### **Erros Comuns**
- [Erro 1]: [Solução]
- [Erro 2]: [Solução]
- [Erro 3]: [Solução]

### **Recuperação**
```lua
-- Exemplo de recuperação
function handleError(error)
    -- Função: handleError
    -- Tratamento do erro
    --  Tratamento do erro (traduzido)
end
```

## 📚 Documentação Adicional

### **Referências**
- [Link para documentação 1]
- [Link para documentação 2]

### **Tutoriais**
- [Tutorial 1]
- [Tutorial 2]

---

## 🔄 Atualizações

### **Histórico de Versões**
- **v1.0**: Versão inicial
- **v1.1**: [Melhoria 1]
- **v1.2**: [Melhoria 2]

### **Próximas Melhorias**
- [Melhoria planejada 1]
- [Melhoria planejada 2]

---

*Template criado pelo Sistema BMAD - OTClient Documentation* 