---
tags: [lesson, canary, CANARY, CANARY-007, lua_system, scripting]
type: lesson
status: completed
priority: high
created: 2025-07-29T01:04:09.668291
lesson_id: CANARY-007
course_id: CANARY
duration: 3 horas
difficulty: high
aliases: [Lua System, Sistema Lua, Lição CANARY-007]
---

# Sistema de Lua

Sistema de scripting Lua no Canary

## 🎯 Objetivos da Lição

- Compreender a arquitetura do sistema Lua no Canary
- Aplicar conceitos de scripting em prática
- Desenvolver habilidades de programação Lua
- Preparar-se para próximas lições

## 📚 Conteúdo

## Teoria

### Sistema de Lua
O sistema Lua no Canary é uma implementação robusta e otimizada para servidores MMORPG, oferecendo:

- **Arquitetura Modular**: Separação clara entre funções, scripts e ambiente
- **Performance Otimizada**: Pool de ambientes e cache inteligente
- **Segurança Robusta**: Chamadas protegidas e tratamento de erros
- **Flexibilidade**: Suporte a múltiplos tipos de dados

### Conceitos Fundamentais

#### 1. LuaEnvironment
- **Propósito**: Ambiente principal de execução Lua
- **Funcionalidades**:
  - Gerenciamento do estado Lua (`lua_State`)
  - Controle de timers e eventos
  - Gerenciamento de objetos de área
  - Coleta de lixo automática

#### 2. LuaScriptInterface
- **Propósito**: Interface principal para scripts Lua
- **Funcionalidades**:
  - Carregamento de arquivos Lua
  - Execução de funções
  - Tratamento de erros
  - Gerenciamento de metadados

#### 3. ScriptEnvironment
- **Propósito**: Ambiente de execução para scripts individuais
- **Funcionalidades**:
  - Isolamento de contexto
  - Gerenciamento de resultados temporários
  - Controle de itens temporários

#### 4. Lua Functions Loader
- **Propósito**: Carregamento e registro de funções Lua
- **Funcionalidades**:
  - Registro de classes e métodos
  - Exposição de APIs C++ para Lua
  - Gerenciamento de metadados

## Prática

### Exemplo Básico - Carregamento de Script
#### Nível Basic
```cpp
// Carregamento de arquivo Lua
int32_t LuaScriptInterface::loadFile(const std::string &file, const std::string &scriptName) {
    int ret = luaL_loadfile(luaState, file.c_str());
    if (ret != 0) {
        lastLuaError = popString(luaState);
        return -1;
    }
    
    if (!isFunction(luaState, -1)) {
        return -1;
    }
    
    loadingFile = file;
    setLoadingScriptName(scriptName);
    
    if (!reserveScriptEnv()) {
        return -1;
    }
    
    ScriptEnvironment* env = getScriptEnv();
    env->setScriptId(EVENT_ID_LOADING, this);
    
    ret = protectedCall(luaState, 0, 0);
    if (ret != 0) {
        reportError(nullptr, popString(luaState));
        resetScriptEnv();
        return -1;
    }
    
    resetScriptEnv();
    return 0;
}
```

#### Nível Intermediate
```cpp
// Carregamento de arquivo Lua
int32_t LuaScriptInterface::loadFile(const std::string &file, const std::string &scriptName) {
    int ret = luaL_loadfile(luaState, file.c_str());
    if (ret != 0) {
        lastLuaError = popString(luaState);
        return -1;
    }
    
    if (!isFunction(luaState, -1)) {
        return -1;
    }
    
    loadingFile = file;
    setLoadingScriptName(scriptName);
    
    if (!reserveScriptEnv()) {
        return -1;
    }
    
    ScriptEnvironment* env = getScriptEnv();
    env->setScriptId(EVENT_ID_LOADING, this);
    
    ret = protectedCall(luaState, 0, 0);
    if (ret != 0) {
        reportError(nullptr, popString(luaState));
        resetScriptEnv();
        return -1;
    }
    
    resetScriptEnv();
    return 0;
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
```cpp
// Carregamento de arquivo Lua
int32_t LuaScriptInterface::loadFile(const std::string &file, const std::string &scriptName) {
    int ret = luaL_loadfile(luaState, file.c_str());
    if (ret != 0) {
        lastLuaError = popString(luaState);
        return -1;
    }
    
    if (!isFunction(luaState, -1)) {
        return -1;
    }
    
    loadingFile = file;
    setLoadingScriptName(scriptName);
    
    if (!reserveScriptEnv()) {
        return -1;
    }
    
    ScriptEnvironment* env = getScriptEnv();
    env->setScriptId(EVENT_ID_LOADING, this);
    
    ret = protectedCall(luaState, 0, 0);
    if (ret != 0) {
        reportError(nullptr, popString(luaState));
        resetScriptEnv();
        return -1;
    }
    
    resetScriptEnv();
    return 0;
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

### Exemplo Avançado - Script Lua Completo
```lua
-- Exemplo de script de ação
function onUse(player, item, fromPosition, target, toPosition, isHotkey)
    -- Função: onUse
    if player:getStorageValue(1000) == 1 then
    -- Verificação condicional
        player:sendTextMessage(MESSAGE_INFO_DESCR, "Você já usou este item.")
        return false
    end
    
    player:setStorageValue(1000, 1)
    player:addItem(2160, 100) -- 100 crystal coins
    player:sendTextMessage(MESSAGE_INFO_DESCR, "Você recebeu 100 crystal coins!")
    
    return true
end

-- Exemplo de evento de criatura
    --  Exemplo de evento de criatura (traduzido)
function onDeath(creature, corpse, killer, mostDamageKiller, unjustified, mostDamageUnjustified)
    -- Função: onDeath
    if creature:isPlayer() then
    -- Verificação condicional
        local player = creature:getPlayer()
        player:sendTextMessage(MESSAGE_EVENT_ADVANCE, "Você morreu!")
        
        -- Log da morte
    --  Log da morte (traduzido)
        logEvent("Player death", {
            player = player:getName(),
            killer = killer and killer:getName() or "Unknown",
            position = creature:getPosition():toString()
        })
    end
    
    return true
end

-- Exemplo de evento global
    --  Exemplo de evento global (traduzido)
function onThink(interval)
    -- Função: onThink
    -- Executar a cada 5 minutos
    --  Executar a cada 5 minutos (traduzido)
    if interval % 300 == 0 then
    -- Verificação condicional
        broadcastMessage("Servidor funcionando normalmente!", MESSAGE_STATUS_WARNING)
    end
    
    return true
end
```

## 💡 Conceitos-Chave

**LuaEnvironment**: Ambiente principal de execução Lua
**LuaScriptInterface**: Interface para scripts Lua
**ScriptEnvironment**: Ambiente isolado para scripts
**APIs C++**: Exposição de funcionalidades C++ para Lua
**Tratamento de Erros**: Sistema robusto de tratamento de erros
**Performance**: Otimizações específicas para servidor

## 🧪 Exercícios

### Exercício 1: Básico
Criar um script Lua simples que adiciona um item ao jogador quando ele usa um item específico.

```lua
function onUse(player, item, fromPosition, target, toPosition, isHotkey)
    -- Função: onUse
    player:addItem(2160, 10) -- 10 crystal coins
    player:sendTextMessage(MESSAGE_INFO_DESCR, "Você recebeu 10 crystal coins!")
    return true
end
```

### Exercício 2: Intermediário
Criar um sistema de quest que verifica se o jogador tem itens específicos e recompensa com experiência.

```lua
function onUse(player, item, fromPosition, target, toPosition, isHotkey)
    -- Função: onUse
    local requiredItems = {2160, 2160, 2160} -- 3 crystal coins
    local hasAllItems = true
    
    for _, itemId in ipairs(requiredItems) do
    -- Loop de repetição
        if player:getItemCount(itemId) < 1 then
    -- Verificação condicional
            hasAllItems = false
            break
        end
    end
    
    if hasAllItems then
    -- Verificação condicional
        -- Remove os itens
    --  Remove os itens (traduzido)
        for _, itemId in ipairs(requiredItems) do
    -- Loop de repetição
            player:removeItem(itemId, 1)
        end
        
        -- Adiciona experiência
        player:addExperience(1000)
        player:sendTextMessage(MESSAGE_INFO_DESCR, "Quest completada! +1000 exp")
    else
        player:sendTextMessage(MESSAGE_INFO_DESCR, "Você precisa de 3 crystal coins!")
    end
    
    return true
end
```

### Exercício 3: Avançado
Criar um sistema de teleporte com verificação de nível e custo.

```lua
function onUse(player, item, fromPosition, target, toPosition, isHotkey)
    -- Função: onUse
    local requiredLevel = 50
    local cost = 1000 -- gold coins
    local destination = Position(1000, 1000, 7)
    
    if player:getLevel() < requiredLevel then
    -- Verificação condicional
        player:sendTextMessage(MESSAGE_INFO_DESCR, "Você precisa ser nível " .. requiredLevel .. "!")
        return false
    end
    
    if player:getMoney() < cost then
    -- Verificação condicional
        player:sendTextMessage(MESSAGE_INFO_DESCR, "Você precisa de " .. cost .. " gold coins!")
        return false
    end
    
    player:removeMoney(cost)
    player:teleportTo(destination)
    player:sendTextMessage(MESSAGE_INFO_DESCR, "Teleporte realizado! Custo: " .. cost .. " gold coins")
    
    return true
end
```

## 📝 Resumo

## Pontos Principais

- **Arquitetura Modular**: Sistema bem organizado com separação clara de responsabilidades
- **Performance**: Otimizações específicas para servidor MMORPG
- **Segurança**: Sistema robusto de tratamento de erros e validações
- **Flexibilidade**: Suporte completo a diferentes tipos de dados e operações
- **Integração**: Interface eficiente entre C++ e Lua

## Aplicação
- **Scripts de Itens**: Criar funcionalidades para itens especiais
- **Eventos de Criaturas**: Implementar comportamentos customizados
- **Sistemas de Quest**: Desenvolver missões e objetivos
- **Eventos Globais**: Criar funcionalidades do servidor

## Benefícios
- **Produtividade**: Desenvolvimento rápido de funcionalidades
- **Manutenibilidade**: Código organizado e bem estruturado
- **Performance**: Execução eficiente de scripts
- **Segurança**: Proteção contra erros e exploits

## Próximos Passos
- Estudar sistema de eventos avançados
- Aprender sobre callbacks e timers
- Explorar integração com outros sistemas
- Praticar desenvolvimento de scripts complexos

## 🔗 Próxima Lição

[[CANARY-008_animation_system]] - Próxima lição

---

**Duração**: 3 horas  
**Dificuldade**: high  
**Status**: completed 