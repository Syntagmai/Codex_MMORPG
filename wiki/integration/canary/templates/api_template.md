---
tags: [canary, api, template, integration, otclient]
type: api_template
status: template
priority: medium
created: 2025-01-27
---

# 🔌 Template de API Canary

> [!info] **Template ID**: CANARY-API-TEMPLATE  
> **Categoria**: Documentação de API  
> **Status**: Template  
> **Prioridade**: Média

## 📋 Estrutura Padrão

### **🎯 Seção 1: Visão Geral da API**
- **Nome da API**: Identificação clara
- **Versão**: Versão da API
- **Propósito**: Objetivo principal
- **Compatibilidade**: Versões suportadas

### **🔧 Seção 2: Autenticação**
- **Método**: Tipo de autenticação
- **Tokens**: Como obter e usar
- **Permissões**: Níveis de acesso
- **Segurança**: Considerações de segurança

### **📡 Seção 3: Endpoints**
- **Base URL**: URL base da API
- **Métodos HTTP**: GET, POST, PUT, DELETE
- **Parâmetros**: Query, path, body
- **Respostas**: Formatos de resposta

### **📊 Seção 4: Modelos de Dados**
- **Estruturas**: Schemas de dados
- **Tipos**: Tipos de dados
- **Validação**: Regras de validação
- **Exemplos**: Exemplos de dados

### **🎨 Seção 5: Exemplos de Uso**
- **Código**: Exemplos em Lua/JavaScript
- **Integração OTClient**: Exemplos específicos
- **Casos de Uso**: Cenários práticos
- **Tratamento de Erros**: Como lidar com erros

---

## 📝 **Template de Conteúdo**

### **🎯 Visão Geral da API**

#### **Informações Básicas:**
- **Nome**: [Nome da API]
- **Versão**: v1.0.0
- **Base URL**: `https://api.canary.com/v1`
- **Protocolo**: HTTP/HTTPS
- **Formato**: JSON

#### **Propósito:**
A API **[Nome]** do Canary fornece **[descrição da funcionalidade]** para integração com o OTClient. Esta API permite **[objetivos específicos]** de forma segura e eficiente.

#### **Compatibilidade:**
- **Canary**: v1.0.0+
- **OTClient**: v1.0.0+
- **Protocolo**: OpenCode v1.0+

---

### **🔧 Autenticação**

#### **Método de Autenticação:**
#### Nível Basic
```lua
-- Exemplo de autenticação
local headers = {
    ["Authorization"] = "Bearer " .. apiToken,
    ["Content-Type"] = "application/json",
    ["X-API-Version"] = "1.0"
}
```

#### Nível Intermediate
```lua
-- Exemplo de autenticação
local headers = {
    ["Authorization"] = "Bearer " .. apiToken,
    ["Content-Type"] = "application/json",
    ["X-API-Version"] = "1.0"
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
```lua
-- Exemplo de autenticação
local headers = {
    ["Authorization"] = "Bearer " .. apiToken,
    ["Content-Type"] = "application/json",
    ["X-API-Version"] = "1.0"
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

#### **Obtenção de Token:**
```lua
-- Solicitar token de acesso
    --  Solicitar token de acesso (traduzido)
local response = http.post("https://api.canary.com/auth", {
    username = "user",
    password = "pass"
})

local token = response.data.access_token
```

#### **Níveis de Permissão:**
- **Read**: Apenas leitura
- **Write**: Leitura e escrita
- **Admin**: Acesso completo
- **System**: Acesso de sistema

---

### **📡 Endpoints**

#### **Base URL:**
```
https://api.canary.com/v1
```

#### **Endpoints Principais:**

##### **GET /api/[resource]**
```lua
-- Buscar recursos
    --  Buscar recursos (traduzido)
local response = http.get("https://api.canary.com/v1/[resource]", {
    headers = headers,
    params = {
        limit = 10,
        offset = 0,
        filter = "active"
    }
})
```

**Parâmetros:**
- `limit` (number): Número máximo de resultados
- `offset` (number): Deslocamento para paginação
- `filter` (string): Filtro de resultados

**Resposta:**
#### Nível Basic
```json
{
    "success": true,
    "data": [
        {
            "id": 1,
            "name": "Example",
            "status": "active"
        }
    ],
    "pagination": {
        "total": 100,
        "limit": 10,
        "offset": 0
    }
}
```

#### Nível Intermediate
```json
{
    "success": true,
    "data": [
        {
            "id": 1,
            "name": "Example",
            "status": "active"
        }
    ],
    "pagination": {
        "total": 100,
        "limit": 10,
        "offset": 0
    }
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
    "success": true,
    "data": [
        {
            "id": 1,
            "name": "Example",
            "status": "active"
        }
    ],
    "pagination": {
        "total": 100,
        "limit": 10,
        "offset": 0
    }
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

##### **POST /api/[resource]**
```lua
-- Criar novo recurso
    --  Criar novo recurso (traduzido)
local response = http.post("https://api.canary.com/v1/[resource]", {
    headers = headers,
    body = {
        name = "New Resource",
        description = "Description",
        status = "active"
    }
})
```

**Body:**
#### Nível Basic
```json
{
    "name": "string",
    "description": "string",
    "status": "active|inactive"
}
```

#### Nível Intermediate
```json
{
    "name": "string",
    "description": "string",
    "status": "active|inactive"
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
    "name": "string",
    "description": "string",
    "status": "active|inactive"
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

**Resposta:**
#### Nível Basic
```json
{
    "success": true,
    "data": {
        "id": 123,
        "name": "New Resource",
        "description": "Description",
        "status": "active",
        "created_at": "2025-01-27T10:00:00Z"
    }
}
```

#### Nível Intermediate
```json
{
    "success": true,
    "data": {
        "id": 123,
        "name": "New Resource",
        "description": "Description",
        "status": "active",
        "created_at": "2025-01-27T10:00:00Z"
    }
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
    "success": true,
    "data": {
        "id": 123,
        "name": "New Resource",
        "description": "Description",
        "status": "active",
        "created_at": "2025-01-27T10:00:00Z"
    }
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

##### **PUT /api/[resource]/{id}**
```lua
-- Atualizar recurso existente
    --  Atualizar recurso existente (traduzido)
local response = http.put("https://api.canary.com/v1/[resource]/123", {
    headers = headers,
    body = {
        name = "Updated Resource",
        status = "inactive"
    }
})
```

##### **DELETE /api/[resource]/{id}**
```lua
-- Remover recurso
    --  Remover recurso (traduzido)
local response = http.delete("https://api.canary.com/v1/[resource]/123", {
    headers = headers
})
```

---

### **📊 Modelos de Dados**

#### **Estrutura de Recurso:**
#### Nível Basic
```json
{
    "id": "number",
    "name": "string",
    "description": "string",
    "status": "enum",
    "created_at": "datetime",
    "updated_at": "datetime",
    "metadata": "object"
}
```

#### Nível Intermediate
```json
{
    "id": "number",
    "name": "string",
    "description": "string",
    "status": "enum",
    "created_at": "datetime",
    "updated_at": "datetime",
    "metadata": "object"
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
    "id": "number",
    "name": "string",
    "description": "string",
    "status": "enum",
    "created_at": "datetime",
    "updated_at": "datetime",
    "metadata": "object"
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

#### **Tipos de Dados:**
- **number**: Números inteiros ou decimais
- **string**: Texto (UTF-8)
- **boolean**: true/false
- **datetime**: ISO 8601 format
- **enum**: Valores predefinidos
- **object**: Objeto JSON
- **array**: Array de valores

#### **Validação:**
```lua
-- Exemplo de validação
local function validateResource(data)
    if not data.name or #data.name < 3 then
    -- Verificação condicional
        return false, "Nome deve ter pelo menos 3 caracteres"
    end
    
    if not data.status or not (data.status == "active" or data.status == "inactive") then
    -- Verificação condicional
        return false, "Status deve ser 'active' ou 'inactive'"
    end
    
    return true
end
```

---

### **🎨 Exemplos de Uso**

#### **Exemplo 1: Integração Básica com OTClient**
```lua
-- Módulo de integração Canary
local CanaryAPI = {}

function CanaryAPI.init(config)
    -- Função: CanaryAPI
    CanaryAPI.baseURL = config.baseURL or "https://api.canary.com/v1"
    CanaryAPI.token = config.token
    CanaryAPI.headers = {
        ["Authorization"] = "Bearer " .. CanaryAPI.token,
        ["Content-Type"] = "application/json"
    }
end

function CanaryAPI.getResources(params)
    -- Função: CanaryAPI
    local response = http.get(CanaryAPI.baseURL .. "/resources", {
        headers = CanaryAPI.headers,
        params = params
    })
    
    if response.success then
    -- Verificação condicional
        return response.data
    else
        error("Erro na API: " .. response.error)
    end
end

-- Uso no OTClient
    --  Uso no OTClient (traduzido)
CanaryAPI.init({
    baseURL = "https://api.canary.com/v1",
    token = "your-token"
})

local resources = CanaryAPI.getResources({
    limit = 10,
    filter = "active"
})
```

#### **Exemplo 2: Sistema de Cache**
```lua
-- Sistema de cache para otimizar chamadas
    --  Sistema de cache para otimizar chamadas (traduzido)
local cache = {}

function CanaryAPI.getResourceWithCache(id)
    -- Função: CanaryAPI
    -- Verificar cache
    --  Verificar cache (traduzido)
    if cache[id] and cache[id].expires > os.time() then
    -- Verificação condicional
        return cache[id].data
    end
    
    -- Buscar da API
    --  Buscar da API (traduzido)
    local response = http.get(CanaryAPI.baseURL .. "/resources/" .. id, {
        headers = CanaryAPI.headers
    })
    
    if response.success then
    -- Verificação condicional
        -- Armazenar no cache (5 minutos)
    --  Armazenar no cache (5 minutos) (traduzido)
        cache[id] = {
            data = response.data,
            expires = os.time() + 300
        }
        return response.data
    else
        error("Erro na API: " .. response.error)
    end
end
```

#### **Exemplo 3: Tratamento de Erros Robusto**
```lua
-- Sistema robusto de tratamento de erros
    --  Sistema robusto de tratamento de erros (traduzido)
function CanaryAPI.safeRequest(method, endpoint, data)
    -- Função: CanaryAPI
    local success, result = pcall(function()
        local response = http[method](CanaryAPI.baseURL .. endpoint, {
            headers = CanaryAPI.headers,
            body = data
        })
        
        if not response.success then
    -- Verificação condicional
            error({
                type = "api_error",
                code = response.status,
                message = response.error
            })
        end
        
        return response.data
    end)
    
    if not success then
    -- Verificação condicional
        if type(result) == "table" and result.type == "api_error" then
    -- Verificação condicional
            -- Erro da API
    --  Erro da API (traduzido)
            logError("API Error: " .. result.message)
            return nil, result
        else
            -- Erro de rede/sistema
    --  Erro de rede/sistema (traduzido)
            logError("System Error: " .. tostring(result))
            return nil, {
                type = "system_error",
                message = tostring(result)
            }
        end
    end
    
    return result
end
```

---

### **🔍 Códigos de Status HTTP**

#### **Sucesso:**
- **200 OK**: Requisição bem-sucedida
- **201 Created**: Recurso criado
- **204 No Content**: Requisição bem-sucedida sem conteúdo

#### **Erro do Cliente:**
- **400 Bad Request**: Dados inválidos
- **401 Unauthorized**: Autenticação necessária
- **403 Forbidden**: Acesso negado
- **404 Not Found**: Recurso não encontrado
- **422 Unprocessable Entity**: Dados válidos mas não processáveis

#### **Erro do Servidor:**
- **500 Internal Server Error**: Erro interno
- **502 Bad Gateway**: Erro de gateway
- **503 Service Unavailable**: Serviço indisponível

---

### **📋 Checklist de Implementação**

#### **✅ Configuração:**
- [ ] Token de API configurado
- [ ] Headers corretos definidos
- [ ] Base URL configurada
- [ ] Tratamento de erros implementado

#### **✅ Funcionalidades:**
- [ ] CRUD básico implementado
- [ ] Paginação funcionando
- [ ] Filtros aplicados
- [ ] Cache implementado (se necessário)

#### **✅ Integração OTClient:**
- [ ] Módulo de integração criado
- [ ] Eventos configurados
- [ ] UI atualizada com dados
- [ ] Tratamento de erros na UI

#### **✅ Testes:**
- [ ] Testes de conectividade
- [ ] Testes de autenticação
- [ ] Testes de dados
- [ ] Testes de erros

---

## 🔗 **Links Automáticos**

> [!info] **Links Gerados Automaticamente**
> Estes links foram criados automaticamente pelo sistema de linkagem da categoria **Integration**

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]
- [[../integration/README|Sistema de Integração]]
- [[../maps/canary_integration_map|Mapa de Integração Canary]]

### **🧭 Navegação**
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]
- [[../maps/category_indices|Índices por Categoria]]
- [[../maps/relationships|Relacionamentos]]

### **📊 Métricas da Categoria**
- **Categoria**: Integration
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

## 🔗 **Links Relacionados**

### **📚 Documentação:**
- [Template de Documentação Canary](documentation_template.md)
- [Template de Guia Canary](guide_template.md)
- [Template de Referência Canary](reference_template.md)

### **🔗 Integração:**
- [Protocolo OpenCode](../protocols/opencode_specification.md)
- [Protocolo ExtendedOpen](../protocols/extendedopen_specification.md)
- [Comunicação Cliente-Servidor](../protocols/client_server_communication.md)

### **📖 Referências:**
- [Documentação Oficial Canary](https://canary.wiki/api)
- [Guia de Integração](../external/integration_guide.md)
- [Sistema de Referência Cruzada](../external/cross_reference_system.md)

---

**Template Criado**: 2025-01-27  
**Responsável**: Documentation Agent  
**Status**: 📋 **Template Ativo**  
**Próximo**: 🔥 **Criar Template de Guia** 