---
tags: [example, canary, setup, configuration, beginner, practical]
type: code_example
status: active
priority: high
created: 2025-08-05
level: beginner
feature: [server_setup, configuration, environment]
aliases: [Canary Setup, Server Configuration, Canary Configuration]
---

# 🔧 Configuração do Servidor Canary
## Implementação Prática de Setup do Servidor

> [!info] **Sobre Este Exemplo**
> Implementação específica e funcional de configuração do servidor Canary.

## 🎯 **Objetivo**
Demonstrar como configurar e inicializar um servidor Canary básico para desenvolvimento de MMORPG.

## 📁 **Arquivos Envolvidos**
- `canary/config.lua.dist` - Configuração principal
- `canary/src/server.cpp` - Servidor principal
- `canary/data/` - Dados do servidor
- `canary/src/database/` - Sistema de banco de dados

## 🔧 **Código Principal**

### **Configuração do Servidor (config.lua)**
```lua
-- Configuração principal do Canary
useAnyDatapackFolder = false
dataPackDirectory = "data-otservbr-global"
coreDirectory = "data"

-- Configurações de rede
ip = "127.0.0.1"
port = 7172
maxPlayers = 1000

-- Configurações de banco de dados
mysqlHost = "127.0.0.1"
mysqlUser = "root"
mysqlPass = ""
mysqlDatabase = "canary"

-- Configurações de segurança
rsaKeyFile = "key.pem"
encryptionType = "sha1"
```

### **Inicialização do Servidor (server.cpp)**
```cpp
// canary/src/server.cpp
class CanaryServer {
public:
    void initialize() {
        // Inicializar sistemas core
        initializeLogger();
        initializeDatabase();
        initializeNetwork();
        initializeGameSystems();
    }
    
private:
    void initializeLogger() {
        // Configurar sistema de logs
        Logger::getInstance().setLevel("info");
    }
    
    void initializeDatabase() {
        // Conectar ao banco de dados
        Database::getInstance().connect();
    }
    
    void initializeNetwork() {
        // Configurar rede
        NetworkManager::getInstance().bind(ip, port);
    }
    
    void initializeGameSystems() {
        // Inicializar sistemas de jogo
        Game::getInstance().initialize();
    }
};
```

## 🔧 **Script Lua (Inicialização)**
```lua
-- canary/lua/scripts/init.lua
function onServerStart()
    print("Canary Server iniciando...")
    
    -- Carregar configurações
    loadConfig()
    
    -- Inicializar sistemas
    initializeGameSystems()
    
    -- Carregar mapas
    loadMaps()
    
    -- Carregar NPCs
    loadNPCs()
    
    print("Canary Server iniciado com sucesso!")
end

function loadConfig()
    -- Carregar configurações do servidor
    local config = require("config")
    print("Configurações carregadas")
end

function initializeGameSystems()
    -- Inicializar sistemas de jogo
    print("Sistemas de jogo inicializados")
end
```

## 🔧 **Interface de Configuração**
```cpp
// canary/src/config/config_manager.cpp
class ConfigManager {
public:
    static ConfigManager& getInstance() {
        static ConfigManager instance;
        return instance;
    }
    
    void loadConfig(const std::string& filename) {
        // Carregar arquivo de configuração
        lua_State* L = luaL_newstate();
        luaL_openlibs(L);
        
        if (luaL_dofile(L, filename.c_str()) != 0) {
            throw std::runtime_error("Erro ao carregar configuração");
        }
        
        // Extrair configurações
        extractConfig(L);
        lua_close(L);
    }
    
private:
    void extractConfig(lua_State* L) {
        // Extrair valores da configuração Lua
        lua_getglobal(L, "ip");
        serverIP = lua_tostring(L, -1);
        
        lua_getglobal(L, "port");
        serverPort = lua_tointeger(L, -1);
    }
};
```

## 🔗 **Links Relacionados**
- **Conceito Base**: [[wiki/concepts/canary_server_overview|Visão Geral do Canary]]
- **Análise Completa**: [[habdel/CANARY-001|Análise Técnica do Setup]]
- **Exercício**: [[wiki/exercises/setup_canary_server|Configurar Servidor Canary]]
- **Projeto**: [[wiki/projects/basic_canary_server|Servidor Básico Canary]]

## ✅ **Teste do Exemplo**
Para testar esta configuração:

1. **Compilar o servidor**:
```bash
cd canary
mkdir build && cd build
cmake ..
make
```

2. **Configurar banco de dados**:
```sql
CREATE DATABASE canary;
USE canary;
SOURCE canary/schema.sql;
```

3. **Executar o servidor**:
```bash
./canary
```

## 🎯 **Próximos Passos**
- **Próximo Exemplo**: [[wiki/examples/canary_database_setup|Configuração de Banco de Dados]]
- **Exercício Relacionado**: [[wiki/exercises/setup_canary_server|Exercício de Setup]]
- **Projeto**: [[wiki/projects/basic_canary_server|Projeto Servidor Básico]]

---

> [!tip] **Dica de Implementação**
> Sempre teste a configuração em ambiente de desenvolvimento antes de usar em produção.

**Nível**: Beginner  
**Funcionalidade**: Server Setup  
**Status**: Ativo 