---
tags: [canary, arquitetura, core, servidor, c++, inicialização, serviços]
type: course
status: published
level: intermediate
created: 2025-01-27
updated: 2025-01-27
aliases: [canary_core_architecture, canary_server_architecture, canary_initialization]
---

# Arquitetura Core do Canary

> [!info] **Sobre este Guia**
> Este guia apresenta a arquitetura core do sistema Canary, focando nos componentes fundamentais, estrutura de inicialização e gerenciamento de serviços. Baseado na análise técnica da [[habdel/CANARY-002|CANARY-002]], este documento fornece uma compreensão profunda da arquitetura interna do servidor.

## 🎯 **Visão Geral da Arquitetura Core**

O sistema Canary possui uma arquitetura core robusta e modular, baseada em C++ moderno com gerenciamento de serviços, configuração dinâmica e inicialização estruturada.

### **Características da Arquitetura Core**
- **Modularidade**: Componentes bem separados e reutilizáveis
- **Thread Safety**: Sincronização adequada com mutex
- **Async/Await**: Inicialização assíncrona para performance
- **Extensibilidade**: Fácil adição de novos serviços
- **Error Handling**: Sistema robusto de exceções

## 🏗️ **Componentes Principais**

### **1. CanaryServer (Servidor Principal)**

**Localização**: `src/canary_server.hpp`, `src/canary_server.cpp`

**Responsabilidades**:
- Inicialização e gerenciamento do servidor
- Coordenação de todos os subsistemas
- Gerenciamento de ciclo de vida
- Tratamento de erros e exceções

**Estrutura Principal**:
```cpp
class CanaryServer {
public:
    explicit CanaryServer(
        Logger &logger,
        RSA &rsa,
        ServiceManager &serviceManager
    );

    int run();

private:
    enum class LoaderStatus : uint8_t {
        LOADING,
        LOADED,
        FAILED
    };

    Logger &logger;
    RSA &rsa;
    ServiceManager &serviceManager;

    LoaderStatus loaderStatus = LoaderStatus::LOADING;
    std::mutex loaderMutex;
    std::condition_variable loaderCV;

    void logInfos();
    void loadConfigLua();
    void validateDatapack();
    void initializeDatabase();
    void loadModules();
    void setWorldType();
    void loadMaps() const;
    void setupHousesRent();
};
```

### **2. ServiceManager (Gerenciador de Serviços)**

**Localização**: `src/server/server.hpp`

**Responsabilidades**:
- Gerenciamento de portas e serviços
- Aceitação de conexões
- Roteamento de protocolos
- Controle de ciclo de vida dos serviços

**Estrutura Principal**:
```cpp
class ServiceManager {
public:
    void run();
    void stop();
    
    template <typename ProtocolType>
    bool add(uint16_t port);
    
    bool is_running() const {
        return acceptors.empty() == false;
    }

private:
    phmap::flat_hash_map<uint16_t, ServicePort_ptr> acceptors;
    asio::io_service io_service;
    Signals signals { io_service };
    asio::high_resolution_timer death_timer { io_service };
    bool running = false;
};
```

**ServicePort (Porta de Serviço)**:
```cpp
class ServicePort : public std::enable_shared_from_this<ServicePort> {
public:
    explicit ServicePort(asio::io_service &init_io_service);
    
    void open(uint16_t port);
    void close() const;
    bool add_service(const Service_ptr &new_svc);
    Protocol_ptr make_protocol(bool checksummed, NetworkMessage &msg, 
                              const Connection_ptr &connection) const;

private:
    asio::io_service &io_service;
    std::unique_ptr<asio::ip::tcp::acceptor> acceptor;
    std::vector<Service_ptr> services;
    uint16_t serverPort = 0;
    bool pendingStart = false;
};
```

### **3. ConfigManager (Gerenciador de Configuração)**

**Localização**: `src/config/configmanager.hpp`, `src/config/configmanager.cpp`

**Responsabilidades**:
- Carregamento e gerenciamento de configurações
- Suporte a múltiplos tipos de dados
- Validação de configurações
- Recarregamento dinâmico

**Estrutura Principal**:
```cpp
class ConfigManager {
public:
    static ConfigManager &getInstance();
    
    bool load();
    bool reload();
    
    // Getters tipados
    [[nodiscard]] const std::string &getString(const ConfigKey_t &key) const;
    [[nodiscard]] int32_t getNumber(const ConfigKey_t &key) const;
    [[nodiscard]] bool getBoolean(const ConfigKey_t &key) const;
    [[nodiscard]] float getFloat(const ConfigKey_t &key) const;
    
    // Features OTC
    OTCFeatures getEnabledFeaturesOTC() const;
    OTCFeatures getDisabledFeaturesOTC() const;

private:
    mutable std::unordered_map<ConfigKey_t, std::string> m_configString;
    mutable std::unordered_map<ConfigKey_t, bool> m_configBoolean;
    mutable std::unordered_map<ConfigKey_t, int32_t> m_configInteger;
    mutable std::unordered_map<ConfigKey_t, float> m_configFloat;
    
    std::unordered_map<ConfigKey_t, ConfigValue> configs;
    std::string configFileLua = { "config.lua" };
    bool loaded = false;
};
```

**Tipos de Configuração Suportados**:
```cpp
using ConfigValue = std::variant<std::string, int32_t, bool, float>;
```

### **4. DatabaseManager (Gerenciador de Banco de Dados)**

**Localização**: `src/database/databasemanager.hpp`

**Responsabilidades**:
- Gerenciamento de conexões com banco de dados
- Migrações e atualizações
- Otimização de tabelas
- Configuração de banco de dados

**Estrutura Principal**:
```cpp
class DatabaseManager {
public:
    // Verificação de estrutura
    static bool tableExists(const std::string &table);
    static int32_t getDatabaseVersion();
    static bool isDatabaseSetup();
    
    // Manutenção
    static bool optimizeTables();
    static void updateDatabase();
    
    // Configuração
    static bool getDatabaseConfig(const std::string &config, int32_t &value);
    static void registerDatabaseConfig(const std::string &config, int32_t value);
};
```

## 🔄 **Fluxo de Inicialização**

### **Estrutura Completa de Inicialização**

```mermaid
graph TD
    A[CanaryServer Constructor] --> B[Logger initialization]
    A --> C[RSA initialization]
    A --> D[ServiceManager initialization]
    A --> E[Game state: STARTUP]
    
    F[CanaryServer::run] --> G[Dispatcher initialization]
    G --> H[Async startup event]
    
    H --> I[loadConfigLua]
    H --> J[validateDatapack]
    H --> K[initializeDatabase]
    H --> L[loadModules]
    H --> M[setWorldType]
    H --> N[loadMaps]
    H --> O[setupHousesRent]
    O --> P[g_game().start]
    
    Q[Service Management] --> R[ServiceManager::run]
    R --> S[Acceptors initialization]
    S --> T[Protocol handling]
    
    P --> U[Game State: NORMAL]
    T --> U
    U --> V[Server online]
```

### **Estados do Servidor**

```cpp
enum GameState_t : uint8_t {
    GAME_STATE_STARTUP = 0,
    GAME_STATE_INIT = 1,
    GAME_STATE_NORMAL = 2,
    GAME_STATE_CLOSED = 3,
    GAME_STATE_SHUTDOWN = 4,
    GAME_STATE_CLOSING = 5
};
```

### **Tratamento de Erros**

```cpp
class FailedToInitializeCanary : public std::exception {
private:
    std::string message;

public:
    explicit FailedToInitializeCanary(const std::string &msg) :
        message("Canary load couldn't be completed. " + msg) { }

    const char* what() const noexcept override {
        return message.c_str();
    }
};
```

## 🔧 **APIs Principais**

### **Inicialização do Servidor**

#### **Nível Básico**
```cpp
// Criação do servidor
CanaryServer server(logger, rsa, serviceManager);

// Execução do servidor
int result = server.run();

// Verificação de status
if (result == EXIT_SUCCESS) {
    // Servidor iniciado com sucesso
} else {
    // Erro na inicialização
}
```

#### **Nível Intermediário**
```cpp
// Criação do servidor com tratamento de erros
try {
    CanaryServer server(logger, rsa, serviceManager);
    int result = server.run();
    
    if (result == EXIT_SUCCESS) {
        logger.info("Servidor iniciado com sucesso");
    } else {
        logger.error("Erro na inicialização do servidor");
    }
} catch (const FailedToInitializeCanary &e) {
    logger.error("Falha na inicialização: {}", e.what());
    return EXIT_FAILURE;
}
```

#### **Nível Avançado**
```cpp
// Criação do servidor com configuração customizada
class CustomCanaryServer : public CanaryServer {
public:
    CustomCanaryServer(Logger &logger, RSA &rsa, ServiceManager &serviceManager)
        : CanaryServer(logger, rsa, serviceManager) {}
    
    int run() override {
        // Configuração customizada antes da inicialização
        logger.info("Iniciando servidor customizado...");
        
        // Chamar implementação base
        return CanaryServer::run();
    }
};

// Uso
CustomCanaryServer server(logger, rsa, serviceManager);
return server.run();
```

### **Gerenciamento de Serviços**

#### **Nível Básico**
```cpp
// Adicionar serviço em porta específica
serviceManager.add<ProtocolLogin>(7171);  // Porta de login
serviceManager.add<ProtocolGame>(7172);   // Porta do jogo

// Verificar se está rodando
if (serviceManager.is_running()) {
    // Serviços ativos
}

// Parar serviços
serviceManager.stop();
```

#### **Nível Intermediário**
```cpp
// Configuração de múltiplos serviços
std::vector<std::pair<uint16_t, std::string>> services = {
    {7171, "Login Protocol"},
    {7172, "Game Protocol"},
    {7171, "Status Protocol"}
};

for (const auto &[port, name] : services) {
    if (serviceManager.add<ProtocolLogin>(port)) {
        logger.info("Serviço {} adicionado na porta {}", name, port);
    } else {
        logger.error("Falha ao adicionar serviço {} na porta {}", name, port);
    }
}
```

#### **Nível Avançado**
```cpp
// Gerenciamento dinâmico de serviços
class ServiceController {
private:
    ServiceManager &serviceManager;
    std::map<uint16_t, std::string> activeServices;
    
public:
    explicit ServiceController(ServiceManager &sm) : serviceManager(sm) {}
    
    bool addService(uint16_t port, const std::string &name) {
        if (serviceManager.add<ProtocolLogin>(port)) {
            activeServices[port] = name;
            return true;
        }
        return false;
    }
    
    void removeService(uint16_t port) {
        // Implementar remoção de serviço
        activeServices.erase(port);
    }
    
    std::vector<std::string> getActiveServices() const {
        std::vector<std::string> services;
        for (const auto &[port, name] : activeServices) {
            services.push_back(name);
        }
        return services;
    }
};
```

### **Configuração**

#### **Nível Básico**
```cpp
// Carregar configuração
g_configManager().load();

// Obter valores de configuração
std::string serverName = g_configManager().getString(SERVER_NAME);
int32_t maxPlayers = g_configManager().getNumber(MAX_PLAYERS);
bool allowOldProtocol = g_configManager().getBoolean(ALLOW_OLD_PROTOCOL);
float experienceRate = g_configManager().getFloat(EXPERIENCE_RATE);

// Recarregar configuração
g_configManager().reload();
```

#### **Nível Intermediário**
```cpp
// Configuração com validação
class ConfigValidator {
public:
    static bool validateServerConfig() {
        auto &config = g_configManager();
        
        // Validar configurações críticas
        if (config.getString(SERVER_NAME).empty()) {
            logger.error("Nome do servidor não pode estar vazio");
            return false;
        }
        
        if (config.getNumber(MAX_PLAYERS) < 0) {
            logger.error("Número máximo de jogadores deve ser positivo");
            return false;
        }
        
        return true;
    }
    
    static void applyDefaultConfig() {
        auto &config = g_configManager();
        
        // Aplicar configurações padrão se não existirem
        if (config.getString(SERVER_NAME).empty()) {
            config.setString(SERVER_NAME, "Canary Server");
        }
        
        if (config.getNumber(MAX_PLAYERS) == 0) {
            config.setNumber(MAX_PLAYERS, 1000);
        }
    }
};
```

#### **Nível Avançado**
```cpp
// Sistema de configuração hierárquica
class HierarchicalConfig {
private:
    std::map<std::string, ConfigValue> configs;
    std::vector<std::string> configFiles;
    
public:
    void addConfigFile(const std::string &file) {
        configFiles.push_back(file);
    }
    
    bool loadAll() {
        for (const auto &file : configFiles) {
            if (!loadConfigFile(file)) {
                return false;
            }
        }
        return true;
    }
    
    template<typename T>
    T get(const std::string &key, const T &defaultValue = T{}) const {
        auto it = configs.find(key);
        if (it != configs.end()) {
            return std::get<T>(it->second);
        }
        return defaultValue;
    }
    
private:
    bool loadConfigFile(const std::string &file) {
        // Implementar carregamento de arquivo
        return true;
    }
};
```

### **Banco de Dados**

#### **Nível Básico**
```cpp
// Verificar estrutura
if (DatabaseManager::isDatabaseSetup()) {
    // Banco configurado
}

// Obter versão
int32_t version = DatabaseManager::getDatabaseVersion();

// Otimizar tabelas
DatabaseManager::optimizeTables();

// Atualizar banco
DatabaseManager::updateDatabase();
```

#### **Nível Intermediário**
```cpp
// Gerenciamento de migrações
class DatabaseMigrationManager {
public:
    static bool runMigrations() {
        int32_t currentVersion = DatabaseManager::getDatabaseVersion();
        int32_t targetVersion = getLatestMigrationVersion();
        
        for (int32_t version = currentVersion + 1; version <= targetVersion; version++) {
            if (!runMigration(version)) {
                logger.error("Falha na migração para versão {}", version);
                return false;
            }
        }
        
        return true;
    }
    
private:
    static bool runMigration(int32_t version) {
        // Implementar migração específica
        return true;
    }
    
    static int32_t getLatestMigrationVersion() {
        // Retornar versão mais recente disponível
        return 10;
    }
};
```

#### **Nível Avançado**
```cpp
// Sistema de backup e recuperação
class DatabaseBackupManager {
public:
    static bool createBackup(const std::string &backupPath) {
        // Implementar backup
        return true;
    }
    
    static bool restoreBackup(const std::string &backupPath) {
        // Implementar restauração
        return true;
    }
    
    static std::vector<std::string> listBackups() {
        // Listar backups disponíveis
        return {};
    }
};
```

## 📊 **Métricas de Performance**

### **Inicialização**
- **Tempo de Startup**: Configurável (timeout padrão: 10 minutos)
- **Verificação de Status**: A cada 120 segundos durante startup
- **Thread Safety**: Mutex e condition variables para sincronização
- **Async Loading**: Inicialização assíncrona para não bloquear

### **Gerenciamento de Recursos**
- **Memory Management**: Smart pointers e RAII
- **Connection Pooling**: Gerenciamento eficiente de conexões
- **Service Lifecycle**: Controle completo de ciclo de vida
- **Error Recovery**: Tratamento robusto de erros

## 🔗 **Integração com Subsistemas**

### **Dependências Principais**

| Subsistema | Dependência | Propósito |
|------------|-------------|-----------|
| **Game Engine** | CanaryServer | Lógica principal do jogo |
| **Network** | ServiceManager | Comunicação cliente-servidor |
| **Database** | DatabaseManager | Persistência de dados |
| **Configuration** | ConfigManager | Configurações do servidor |
| **Security** | RSA | Criptografia e segurança |
| **Logging** | Logger | Registro de eventos |

### **Inicialização de Subsistemas**

```cpp
// Sequência de inicialização
void CanaryServer::initializeSubsystems() {
    // 1. Configuração
    loadConfigLua();
    
    // 2. Banco de Dados
    initializeDatabase();
    
    // 3. Módulos Lua
    loadModules();
    
    // 4. Mundo e Mapas
    setWorldType();
    loadMaps();
    
    // 5. Jogo
    g_game().start(&serviceManager);
}
```

## 🛠️ **Exemplos Práticos**

### **Exemplo 1: Servidor Básico**

```cpp
#include "canary_server.hpp"

int main() {
    Logger logger;
    RSA rsa;
    ServiceManager serviceManager;
    
    CanaryServer server(logger, rsa, serviceManager);
    return server.run();
}
```

### **Exemplo 2: Configuração Customizada**

```cpp
// Carregar configuração customizada
g_configManager().setConfigFileLua("custom_config.lua");
g_configManager().load();

// Verificar configurações críticas
if (!g_configManager().getBoolean(ALLOW_OLD_PROTOCOL)) {
    logger.warn("Old protocol disabled");
}

// Configurar limites
int32_t maxPlayers = g_configManager().getNumber(MAX_PLAYERS);
if (maxPlayers == 0) {
    logger.info("No player limit set");
}
```

### **Exemplo 3: Gerenciamento de Serviços**

```cpp
// Adicionar serviços em portas diferentes
serviceManager.add<ProtocolLogin>(7171);
serviceManager.add<ProtocolGame>(7172);
serviceManager.add<ProtocolStatus>(7171);

// Verificar status
if (serviceManager.is_running()) {
    logger.info("All services running");
} else {
    logger.error("Services not running");
}
```

### **Exemplo 4: Tratamento de Erros**

```cpp
try {
    CanaryServer server(logger, rsa, serviceManager);
    return server.run();
} catch (const FailedToInitializeCanary &e) {
    logger.error("Failed to initialize: {}", e.what());
    return EXIT_FAILURE;
} catch (const std::exception &e) {
    logger.error("Unexpected error: {}", e.what());
    return EXIT_FAILURE;
}
```

## 🔍 **Troubleshooting**

### **Problemas Comuns**

1. **Erro de Inicialização**
   - Verificar logs de erro
   - Validar configurações
   - Verificar dependências

2. **Erro de Serviços**
   - Verificar portas disponíveis
   - Validar protocolos
   - Verificar firewall

3. **Erro de Configuração**
   - Validar arquivo config.lua
   - Verificar sintaxe
   - Validar valores

### **Debug e Logs**

```cpp
// Habilitar logs detalhados
logger.setLevel(LogLevel::DEBUG);

// Verificar status de inicialização
if (loaderStatus == LoaderStatus::FAILED) {
    logger.error("Loader failed to initialize");
}
```

## 📖 **Próximos Passos**

### **Leitura Recomendada**

1. [[canary_sistema_rede|Sistema de Rede]] - Comunicação cliente-servidor
2. [[canary_sistema_ui|Sistema de UI]] - Interfaces do usuário
3. [[canary_sistema_modulos|Sistema de Módulos]] - Extensibilidade
4. [[canary_fundamentos|Fundamentos do Canary]] - Visão geral

### **Recursos Adicionais**

- [[wikipedia_canary_otclient|Wikipedia Canary + OTClient]] - Visão geral completa
- [[guia_navegacao|Guia de Navegação]] - Como navegar pela documentação
- [[glossario_tecnico|Glossário Técnico]] - Termos e conceitos

## 🎯 **Conclusão**

A arquitetura core do Canary demonstra excelente qualidade de design e implementação, oferecendo:

### **✅ Pontos Fortes**
1. **Arquitetura Robusta**: Design modular e bem estruturado
2. **Inicialização Estruturada**: Fluxo claro e organizado
3. **Gerenciamento de Serviços**: Sistema flexível e extensível
4. **Configuração Dinâmica**: Suporte a múltiplos tipos de dados
5. **Tratamento de Erros**: Sistema robusto de exceções

### **🔧 Características Técnicas**
- **C++ Moderno**: Uso de features modernas (smart pointers, RAII)
- **Async/Await**: Inicialização assíncrona para performance
- **Thread Safety**: Sincronização adequada com mutex
- **Modularidade**: Componentes bem separados e reutilizáveis
- **Extensibilidade**: Fácil adição de novos serviços e protocolos

Esta base sólida permite o desenvolvimento e manutenção eficiente do servidor MMORPG, oferecendo uma arquitetura escalável e confiável para aplicações de alta performance.

---

**Tags**: #canary #arquitetura #core #servidor #c++ #inicialização #serviços  
**Nível**: Intermediate  
**Tempo Estimado**: 45 minutos  
**Próximo**: [[canary_sistema_rede|Sistema de Rede]] 