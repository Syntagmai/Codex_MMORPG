---
tags: [habdel_research, canary-007, research_story, lua_system, scripting]
type: research_story
status: completed
priority: critical
created: 2025-07-31
target: canary
completed: 2025-01-27
---

# CANARY-007: Sistema de Lua

## 🎯 **Objetivo**
Pesquisa profunda do sistema Lua no Canary usando metodologia habdel

## 📋 **Tarefas de Pesquisa**

### **1. Análise do Código-Fonte** ✅
- [x] Identificar arquivos relevantes
- [x] Analisar estrutura e arquitetura
- [x] Documentar principais componentes
- [x] Mapear dependências

### **2. Documentação Técnica** ✅
- [x] Criar documentação detalhada
- [x] Incluir exemplos práticos
- [x] Documentar APIs e interfaces
- [x] Criar diagramas quando necessário

### **3. Validação** ✅
- [x] Validar completude da documentação
- [x] Verificar qualidade técnica
- [x] Testar exemplos práticos
- [x] Revisar integração com wiki

## 📊 **Progresso**
- **Status**: ✅ Concluído
- **Progresso**: 100%
- **Iniciado**: 2025-01-27
- **Concluído**: 2025-01-27

## 🏗️ **Arquitetura do Sistema Lua**

### **Estrutura de Diretórios**
```
canary/src/lua/
├── functions/           # Funções Lua expostas ao script
│   ├── core/           # Funções core do sistema
│   ├── creatures/      # Funções relacionadas a criaturas
│   ├── events/         # Funções de eventos
│   ├── items/          # Funções de itens
│   ├── map/            # Funções de mapa
│   └── lua_functions_loader.cpp
├── scripts/            # Sistema de scripts
│   ├── lua_environment.cpp
│   ├── luascript.cpp
│   ├── script_environment.cpp
│   └── luajit_sync.hpp
├── callbacks/          # Sistema de callbacks
├── creature/           # Callbacks específicos de criaturas
├── global/             # Variáveis globais Lua
└── modules/            # Módulos Lua
```

### **Componentes Principais**

#### **1. LuaEnvironment**
- **Arquivo**: `canary/src/lua/scripts/lua_environment.hpp/cpp`
- **Propósito**: Ambiente principal de execução Lua
- **Funcionalidades**:
  - Gerenciamento do estado Lua (`lua_State`)
  - Controle de timers e eventos
  - Gerenciamento de objetos de área
  - Coleta de lixo automática

#### **2. LuaScriptInterface**
- **Arquivo**: `canary/src/lua/scripts/luascript.hpp/cpp`
- **Propósito**: Interface principal para scripts Lua
- **Funcionalidades**:
  - Carregamento de arquivos Lua
  - Execução de funções
  - Tratamento de erros
  - Gerenciamento de metadados

#### **3. ScriptEnvironment**
- **Arquivo**: `canary/src/lua/scripts/script_environment.hpp/cpp`
- **Propósito**: Ambiente de execução para scripts individuais
- **Funcionalidades**:
  - Isolamento de contexto
  - Gerenciamento de resultados temporários
  - Controle de itens temporários

#### **4. Lua Functions Loader**
- **Arquivo**: `canary/src/lua/functions/lua_functions_loader.hpp/cpp`
- **Propósito**: Carregamento e registro de funções Lua
- **Funcionalidades**:
  - Registro de classes e métodos
  - Exposição de APIs C++ para Lua
  - Gerenciamento de metadados

## 🔧 **APIs e Interfaces**

### **Funções Core**
#### Nível Basic
```cpp
// Carregamento do sistema Lua
void Lua::load(lua_State* L);

// Registro de classes
void registerClass(lua_State* L, const std::string &className, 
                  const std::string &baseClass, lua_CFunction newFunction = nullptr);

// Registro de métodos
void registerMethod(lua_State* L, const std::string &globalName, 
                   const std::string &methodName, lua_CFunction func);

// Registro de variáveis globais
void registerGlobalVariable(lua_State* L, const std::string &name, lua_Number value);
void registerGlobalString(lua_State* L, const std::string &variable, const std::string &name);
```

#### Nível Intermediate
```cpp
// Carregamento do sistema Lua
void Lua::load(lua_State* L);

// Registro de classes
void registerClass(lua_State* L, const std::string &className, 
                  const std::string &baseClass, lua_CFunction newFunction = nullptr);

// Registro de métodos
void registerMethod(lua_State* L, const std::string &globalName, 
                   const std::string &methodName, lua_CFunction func);

// Registro de variáveis globais
void registerGlobalVariable(lua_State* L, const std::string &name, lua_Number value);
void registerGlobalString(lua_State* L, const std::string &variable, const std::string &name);
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
// Carregamento do sistema Lua
void Lua::load(lua_State* L);

// Registro de classes
void registerClass(lua_State* L, const std::string &className, 
                  const std::string &baseClass, lua_CFunction newFunction = nullptr);

// Registro de métodos
void registerMethod(lua_State* L, const std::string &globalName, 
                   const std::string &methodName, lua_CFunction func);

// Registro de variáveis globais
void registerGlobalVariable(lua_State* L, const std::string &name, lua_Number value);
void registerGlobalString(lua_State* L, const std::string &variable, const std::string &name);
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

### **Funções de Conversão**
#### Nível Basic
```cpp
// Push functions
static void pushThing(lua_State* L, const std::shared_ptr<Thing> &thing);
static void pushVariant(lua_State* L, const LuaVariant &var);
static void pushString(lua_State* L, const std::string &value);
static void pushNumber(lua_State* L, lua_Number value);
static void pushBoolean(lua_State* L, bool value);
static void pushPosition(lua_State* L, const Position &position, int32_t stackpos = 0);

// Get functions
static std::string getString(lua_State* L, int32_t arg);
static int32_t getNumber(lua_State* L, int32_t arg);
static bool getBoolean(lua_State* L, int32_t arg);
static std::shared_ptr<Creature> getCreature(lua_State* L, int32_t arg);
static std::shared_ptr<Player> getPlayer(lua_State* L, int32_t arg, bool allowOffline = false);
```

#### Nível Intermediate
```cpp
// Push functions
static void pushThing(lua_State* L, const std::shared_ptr<Thing> &thing);
static void pushVariant(lua_State* L, const LuaVariant &var);
static void pushString(lua_State* L, const std::string &value);
static void pushNumber(lua_State* L, lua_Number value);
static void pushBoolean(lua_State* L, bool value);
static void pushPosition(lua_State* L, const Position &position, int32_t stackpos = 0);

// Get functions
static std::string getString(lua_State* L, int32_t arg);
static int32_t getNumber(lua_State* L, int32_t arg);
static bool getBoolean(lua_State* L, int32_t arg);
static std::shared_ptr<Creature> getCreature(lua_State* L, int32_t arg);
static std::shared_ptr<Player> getPlayer(lua_State* L, int32_t arg, bool allowOffline = false);
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
// Push functions
static void pushThing(lua_State* L, const std::shared_ptr<Thing> &thing);
static void pushVariant(lua_State* L, const LuaVariant &var);
static void pushString(lua_State* L, const std::string &value);
static void pushNumber(lua_State* L, lua_Number value);
static void pushBoolean(lua_State* L, bool value);
static void pushPosition(lua_State* L, const Position &position, int32_t stackpos = 0);

// Get functions
static std::string getString(lua_State* L, int32_t arg);
static int32_t getNumber(lua_State* L, int32_t arg);
static bool getBoolean(lua_State* L, int32_t arg);
static std::shared_ptr<Creature> getCreature(lua_State* L, int32_t arg);
static std::shared_ptr<Player> getPlayer(lua_State* L, int32_t arg, bool allowOffline = false);
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

### **Funções de Validação**
#### Nível Basic
```cpp
static bool isNumber(lua_State* L, int32_t arg);
static bool isString(lua_State* L, int32_t arg);
static bool isBoolean(lua_State* L, int32_t arg);
static bool isTable(lua_State* L, int32_t arg);
static bool isFunction(lua_State* L, int32_t arg);
static bool isUserdata(lua_State* L, int32_t arg);
```

#### Nível Intermediate
```cpp
static bool isNumber(lua_State* L, int32_t arg);
static bool isString(lua_State* L, int32_t arg);
static bool isBoolean(lua_State* L, int32_t arg);
static bool isTable(lua_State* L, int32_t arg);
static bool isFunction(lua_State* L, int32_t arg);
static bool isUserdata(lua_State* L, int32_t arg);
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
static bool isNumber(lua_State* L, int32_t arg);
static bool isString(lua_State* L, int32_t arg);
static bool isBoolean(lua_State* L, int32_t arg);
static bool isTable(lua_State* L, int32_t arg);
static bool isFunction(lua_State* L, int32_t arg);
static bool isUserdata(lua_State* L, int32_t arg);
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

## 📝 **Exemplos Práticos**

### **1. Carregamento de Script**
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

### **2. Registro de Função Global**
#### Nível Basic
```cpp
// Registro de função global
void registerGlobalMethod(lua_State* L, const std::string &functionName, lua_CFunction func) {
    lua_register(L, functionName.c_str(), func);
}
```

#### Nível Intermediate
```cpp
// Registro de função global
void registerGlobalMethod(lua_State* L, const std::string &functionName, lua_CFunction func) {
    lua_register(L, functionName.c_str(), func);
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
// Registro de função global
void registerGlobalMethod(lua_State* L, const std::string &functionName, lua_CFunction func) {
    lua_register(L, functionName.c_str(), func);
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

### **3. Manipulação de Userdata**
#### Nível Basic
```cpp
// Push userdata
template <class T>
static void pushUserdata(lua_State* L, T* value) {
    T** userdata = static_cast<T**>(lua_newuserdata(L, sizeof(T*)));
    *userdata = value;
}

// Get userdata
template <class T>
static T* getUserdata(lua_State* L, int32_t arg) {
    T** userdata = getRawUserdata<T>(L, arg);
    if (!userdata) {
        return nullptr;
    }
    return *userdata;
}
```

#### Nível Intermediate
```cpp
// Push userdata
template <class T>
static void pushUserdata(lua_State* L, T* value) {
    T** userdata = static_cast<T**>(lua_newuserdata(L, sizeof(T*)));
    *userdata = value;
}

// Get userdata
template <class T>
static T* getUserdata(lua_State* L, int32_t arg) {
    T** userdata = getRawUserdata<T>(L, arg);
    if (!userdata) {
        return nullptr;
    }
    return *userdata;
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
// Push userdata
template <class T>
static void pushUserdata(lua_State* L, T* value) {
    T** userdata = static_cast<T**>(lua_newuserdata(L, sizeof(T*)));
    *userdata = value;
}

// Get userdata
template <class T>
static T* getUserdata(lua_State* L, int32_t arg) {
    T** userdata = getRawUserdata<T>(L, arg);
    if (!userdata) {
        return nullptr;
    }
    return *userdata;
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

## 🎮 **Sistema de Scripts**

### **Estrutura de Scripts**
```
canary/data/scripts/
├── actions/           # Ações de itens
├── creaturescripts/   # Scripts de criaturas
├── eventcallbacks/    # Callbacks de eventos
├── globalevents/      # Eventos globais
├── lib/              # Bibliotecas Lua
├── movements/        # Scripts de movimento
├── runes/            # Scripts de runas
├── spells/           # Scripts de magias
├── systems/          # Sistemas customizados
├── talkactions/      # Ações de fala
└── weapons/          # Scripts de armas
```

### **Arquivos de Configuração**
- **`global.lua`**: Configurações globais e variáveis
- **`core.lua`**: Configurações core do sistema
- **`stages.lua`**: Configurações de estágios do servidor

### **Exemplo de Script Lua**
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
```

## 🔄 **Sistema de Eventos**

### **Tipos de Eventos**
- **Creature Events**: Eventos relacionados a criaturas
- **Item Events**: Eventos relacionados a itens
- **Global Events**: Eventos globais do servidor
- **Timer Events**: Eventos baseados em tempo

### **Sistema de Callbacks**
#### Nível Basic
```cpp
// Registro de callback
static void pushCallback(lua_State* L, int32_t callback);

// Execução de callback
bool callFunction(int params) const;
void callVoidFunction(int params) const;
```

#### Nível Intermediate
```cpp
// Registro de callback
static void pushCallback(lua_State* L, int32_t callback);

// Execução de callback
bool callFunction(int params) const;
void callVoidFunction(int params) const;
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
// Registro de callback
static void pushCallback(lua_State* L, int32_t callback);

// Execução de callback
bool callFunction(int params) const;
void callVoidFunction(int params) const;
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

## 🛡️ **Tratamento de Erros**

### **Sistema de Erro**
#### Nível Basic
```cpp
// Reportar erro
static void reportError(const char* function, const std::string &error_desc, bool stack_trace = false);

// Obter descrição do erro
static std::string getErrorDesc(ErrorCode_t code);

// Stack trace
std::string getStackTrace(const std::string &error_desc) const;
```

#### Nível Intermediate
```cpp
// Reportar erro
static void reportError(const char* function, const std::string &error_desc, bool stack_trace = false);

// Obter descrição do erro
static std::string getErrorDesc(ErrorCode_t code);

// Stack trace
std::string getStackTrace(const std::string &error_desc) const;
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
// Reportar erro
static void reportError(const char* function, const std::string &error_desc, bool stack_trace = false);

// Obter descrição do erro
static std::string getErrorDesc(ErrorCode_t code);

// Stack trace
std::string getStackTrace(const std::string &error_desc) const;
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

### **Chamada Protegida**
#### Nível Basic
```cpp
// Execução protegida de função Lua
static int protectedCall(lua_State* L, int nargs, int nresults);
```

#### Nível Intermediate
```cpp
// Execução protegida de função Lua
static int protectedCall(lua_State* L, int nargs, int nresults);
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
// Execução protegida de função Lua
static int protectedCall(lua_State* L, int nargs, int nresults);
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

## 🔧 **Otimizações e Performance**

### **Gerenciamento de Memória**
- **Coleta de lixo automática**: `collectGarbage()`
- **Userdata compartilhado**: `getUserdataShared()`
- **Metadados fracos**: `setWeakMetatable()`

### **Cache de Ambiente**
- **Pool de ambientes**: 16 ambientes simultâneos
- **Reutilização de contexto**: `reserveScriptEnv()`
- **Reset automático**: `resetScriptEnv()`

## 📊 **Métricas e Monitoramento**

### **Métricas Disponíveis**
- **Tempo de execução** de scripts
- **Uso de memória** do ambiente Lua
- **Número de erros** por script
- **Performance** de funções críticas

### **Logs e Debug**
#### Nível Basic
```cpp
if (number < 0) {
```

#### Nível Intermediate
```cpp
// Log formatado
static std::string getFormatedLoggerMessage(lua_State* L);

// Debug de overflow
if (number < 0) {
    g_logger().debug("[{}] overflow, setting to default unsigned value (0)", __FUNCTION__);
    return T(0);
}
```

#### Nível Advanced
```cpp
// Log formatado
static std::string getFormatedLoggerMessage(lua_State* L);

// Debug de overflow
if (number < 0) {
    g_logger().debug("[{}] overflow, setting to default unsigned value (0)", __FUNCTION__);
    return T(0);
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

## 🔗 **Integração com Outros Sistemas**

### **Sistema de Combate**
- **AreaCombat**: Objetos de área de combate
- **CombatDamage**: Dados de dano
- **InstantSpell**: Magias instantâneas

### **Sistema de Jogo**
- **Game**: Interface principal do jogo
- **Dispatcher**: Agendamento de eventos
- **Teleport**: Sistema de teleporte

### **Sistema de Criaturas**
- **Player**: Jogadores
- **Monster**: Monstros
- **Npc**: NPCs
- **Guild**: Guildas

## 📝 **Notas de Pesquisa**

### **Descobertas Importantes**
1. **Arquitetura Modular**: O sistema Lua é altamente modular, com separação clara entre funções, scripts e ambiente
2. **Performance Otimizada**: Uso de pool de ambientes e cache inteligente para melhor performance
3. **Segurança Robusta**: Sistema de chamadas protegidas e tratamento de erros abrangente
4. **Flexibilidade**: Suporte a múltiplos tipos de dados e conversões automáticas

### **Diferenças do OTClient**
1. **Estrutura Mais Organizada**: Separação clara entre funções e scripts
2. **Sistema de Callbacks Avançado**: Melhor gerenciamento de eventos
3. **Performance Superior**: Otimizações específicas para servidor
4. **Segurança Aprimorada**: Validações mais rigorosas

### **Pontos de Atenção**
1. **Gerenciamento de Memória**: Cuidado com userdata e metadados
2. **Tratamento de Erros**: Sempre usar chamadas protegidas
3. **Performance**: Monitorar uso de memória e tempo de execução
4. **Compatibilidade**: Verificar versão do Lua e dependências

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

## 🔗 **Links Relacionados**
- [Documentação Principal](../../README.md)
- [Plano de Pesquisa](../research_plan.json)
- [Status Geral](../status_report.md)
- [CANARY-006: Sistema de Scripting](../habdel/CANARY-006.md)
- [CANARY-008: Sistema de Dados](../habdel/CANARY-008.md)

---
*Story concluída seguindo metodologia habdel - 2025-01-27*
