---
tags: [example, canary, core_architecture, setup, configuration, service_management]
type: code_example
status: active
priority: high
created: 2025-08-05
level: intermediate
feature: [server_setup, configuration, service_management, database]
aliases: [Canary Core Setup, Server Configuration, Service Management Example]
---

# 🔧 Configuração da Arquitetura Core

## Implementação Prática da Arquitetura Core do Canary

Este exemplo demonstra como configurar e inicializar os componentes principais da arquitetura core do Canary.

## 🎯 Configuração Básica

### **1. Configuração do Servidor Principal**

```cpp
// canary_server_config.cpp
#include "canary_server.hpp"
#include "config/configmanager.hpp"
#include "database/databasemanager.hpp"

class CanaryServerConfig {
public:
    static void initializeServer() {
        // 1. Carregar configurações
        g_configManager().load();
        
        // 2. Configurar logger
        Logger logger;
        logger.setLevel(LogLevel::INFO);
        
        // 3. Configurar RSA
        RSA rsa;
        rsa.loadKeys("private.pem", "public.pem");
        
        // 4. Configurar ServiceManager
        ServiceManager serviceManager;
        
        // 5. Criar e executar servidor
        CanaryServer server(logger, rsa, serviceManager);
        int result = server.run();
        
        if (result != EXIT_SUCCESS) {
            logger.error("Falha na inicialização do servidor");
        }
    }
};
```

### **2. Configuração de Serviços**

```cpp
// service_config.cpp
#include "server/server.hpp"

class ServiceConfiguration {
public:
    static void setupServices(ServiceManager& serviceManager) {
        // Configurar porta de login
        serviceManager.add<ProtocolLogin>(7171);
        
        // Configurar porta do jogo
        serviceManager.add<ProtocolGame>(7172);
        
        // Configurar porta de status (opcional)
        serviceManager.add<ProtocolStatus>(7173);
        
        // Verificar se serviços estão ativos
        if (serviceManager.is_running()) {
            std::cout << "Serviços configurados com sucesso" << std::endl;
        }
    }
};
```

### **3. Configuração de Banco de Dados**

```cpp
// database_config.cpp
#include "database/databasemanager.hpp"

class DatabaseConfiguration {
public:
    static void setupDatabase() {
        // Verificar se banco existe
        if (!DatabaseManager::isDatabaseSetup()) {
            std::cout << "Configurando banco de dados..." << std::endl;
            DatabaseManager::updateDatabase();
        }
        
        // Otimizar tabelas
        DatabaseManager::optimizeTables();
        
        // Verificar versão
        int32_t version = DatabaseManager::getDatabaseVersion();
        std::cout << "Versão do banco: " << version << std::endl;
    }
};
```

## 🔧 Configuração Avançada

### **4. Configuração Lua Dinâmica**

```lua
-- config.lua
-- Configurações do servidor
serverName = "Meu Servidor Canary"
maxPlayers = 1000
experienceRate = 1.0
allowOldProtocol = false

-- Configurações de rede
loginPort = 7171
gamePort = 7172
statusPort = 7173

-- Configurações de banco de dados
databaseHost = "localhost"
databasePort = 3306
databaseName = "canary_db"
databaseUser = "canary_user"
databasePassword = "canary_pass"

-- Configurações de segurança
rsaPrivateKey = "private.pem"
rsaPublicKey = "public.pem"
```

### **5. Script de Inicialização Completo**

```cpp
// main.cpp
#include "canary_server.hpp"
#include "config/configmanager.hpp"
#include "database/databasemanager.hpp"

int main() {
    try {
        // 1. Inicializar configurações
        if (!g_configManager().load()) {
            std::cerr << "Erro ao carregar configurações" << std::endl;
            return EXIT_FAILURE;
        }
        
        // 2. Configurar banco de dados
        DatabaseConfiguration::setupDatabase();
        
        // 3. Configurar logger
        Logger logger;
        logger.setLevel(LogLevel::INFO);
        logger.info("Iniciando servidor Canary...");
        
        // 4. Configurar RSA
        RSA rsa;
        std::string privateKey = g_configManager().getString(RSA_PRIVATE_KEY);
        std::string publicKey = g_configManager().getString(RSA_PUBLIC_KEY);
        
        if (!rsa.loadKeys(privateKey, publicKey)) {
            logger.error("Erro ao carregar chaves RSA");
            return EXIT_FAILURE;
        }
        
        // 5. Configurar ServiceManager
        ServiceManager serviceManager;
        ServiceConfiguration::setupServices(serviceManager);
        
        // 6. Criar e executar servidor
        CanaryServer server(logger, rsa, serviceManager);
        int result = server.run();
        
        if (result == EXIT_SUCCESS) {
            logger.info("Servidor iniciado com sucesso");
        } else {
            logger.error("Erro na execução do servidor");
        }
        
        return result;
        
    } catch (const std::exception& e) {
        std::cerr << "Erro crítico: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }
}
```

## 🧪 Testando a Configuração

### **6. Script de Teste**

```cpp
// test_configuration.cpp
#include <iostream>
#include "config/configmanager.hpp"
#include "database/databasemanager.hpp"

class ConfigurationTester {
public:
    static void testConfiguration() {
        std::cout << "=== Teste de Configuração ===" << std::endl;
        
        // Testar configurações
        std::string serverName = g_configManager().getString(SERVER_NAME);
        int32_t maxPlayers = g_configManager().getNumber(MAX_PLAYERS);
        
        std::cout << "Nome do servidor: " << serverName << std::endl;
        std::cout << "Máximo de jogadores: " << maxPlayers << std::endl;
        
        // Testar banco de dados
        if (DatabaseManager::isDatabaseSetup()) {
            std::cout << "Banco de dados: OK" << std::endl;
        } else {
            std::cout << "Banco de dados: FALHA" << std::endl;
        }
        
        std::cout << "=== Teste Concluído ===" << std::endl;
    }
};
```

## 🔗 Links Relacionados

- **Conceito**: [[concepts/canary_core_architecture|Arquitetura Core do Canary]]
- **Exercício Prático**: [[exercises/build_core_architecture|Construindo a Arquitetura Core]]
- **Análise Técnica**: [[habdel/CANARY-002|CANARY-002: Análise da Arquitetura Core]]
- **Módulo Educacional**: [[modules/02_canary/02_core_architecture|Módulo: Arquitetura Core]]

## 📚 Recursos Adicionais

- **Tópico Canary**: [[topics/canary|Índice Canary]]
- **Templates**: [[templates/example_template|Template de Exemplo]]
- **Configuração Básica**: [[examples/canary_setup|Configuração Básica do Canary]] 