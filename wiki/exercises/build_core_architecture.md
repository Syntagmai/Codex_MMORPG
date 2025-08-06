---
tags: [exercise, canary, core_architecture, hands_on, server_building, configuration]
type: exercise
status: active
priority: high
created: 2025-08-05
level: intermediate
duration: 2-3 horas
prerequisites: [canary_server_overview, canary_core_architecture]
aliases: [Build Core Architecture, Server Building Exercise, Configuration Exercise]
---

# 🎮 Construindo a Arquitetura Core

## Exercício Prático de Construção da Arquitetura Core do Canary

Este exercício guia você através da construção completa da arquitetura core do Canary, desde a configuração básica até a implementação avançada.

## 🎯 Objetivos do Exercício

- ✅ Configurar todos os componentes core do Canary
- ✅ Implementar sistema de inicialização estruturado
- ✅ Configurar gerenciamento de serviços
- ✅ Implementar sistema de configuração dinâmico
- ✅ Testar e validar a arquitetura completa

## 📋 Pré-requisitos

- [ ] Ambiente de desenvolvimento configurado
- [ ] Código-fonte do Canary baixado
- [ ] Compilador C++ configurado
- [ ] MySQL/MariaDB instalado
- [ ] Conhecimento básico de C++ e Lua

## 🔧 Passo a Passo

### **Passo 1: Preparação do Ambiente**

```bash
# 1. Navegar para o diretório do projeto
cd canary/

# 2. Criar diretório de configuração
mkdir -p config/
mkdir -p logs/
mkdir -p data/

# 3. Verificar estrutura do projeto
ls -la src/
```

### **Passo 2: Configuração Básica**

#### **2.1 Criar arquivo de configuração principal**

```lua
-- config.lua
-- Configurações básicas do servidor
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

-- Configurações de logging
logLevel = "INFO"
logFile = "logs/canary.log"
```

#### **2.2 Configurar banco de dados**

```sql
-- database_setup.sql
CREATE DATABASE IF NOT EXISTS canary_db;
USE canary_db;

-- Criar usuário para o Canary
CREATE USER 'canary_user'@'localhost' IDENTIFIED BY 'canary_pass';
GRANT ALL PRIVILEGES ON canary_db.* TO 'canary_user'@'localhost';
FLUSH PRIVILEGES;
```

### **Passo 3: Implementação dos Componentes Core**

#### **3.1 Criar classe de configuração**

```cpp
// src/config/server_config.hpp
#pragma once
#include <string>
#include <unordered_map>

class ServerConfig {
public:
    static ServerConfig& getInstance();
    
    bool loadConfig(const std::string& configFile);
    std::string getString(const std::string& key) const;
    int getInt(const std::string& key) const;
    bool getBool(const std::string& key) const;
    
private:
    ServerConfig() = default;
    std::unordered_map<std::string, std::string> config;
};
```

#### **3.2 Implementar gerenciador de serviços**

```cpp
// src/server/service_manager.hpp
#pragma once
#include <memory>
#include <vector>
#include <asio.hpp>

class ServiceManager {
public:
    ServiceManager();
    ~ServiceManager();
    
    bool addService(uint16_t port, const std::string& protocol);
    bool start();
    void stop();
    bool isRunning() const;
    
private:
    asio::io_service io_service;
    std::vector<std::shared_ptr<asio::ip::tcp::acceptor>> acceptors;
    bool running = false;
};
```

#### **3.3 Implementar servidor principal**

```cpp
// src/canary_server.hpp
#pragma once
#include "config/server_config.hpp"
#include "server/service_manager.hpp"
#include "database/database_manager.hpp"

class CanaryServer {
public:
    CanaryServer();
    ~CanaryServer();
    
    bool initialize();
    int run();
    void shutdown();
    
private:
    bool loadConfig();
    bool setupDatabase();
    bool setupServices();
    bool loadModules();
    
    ServerConfig& config;
    ServiceManager serviceManager;
    DatabaseManager databaseManager;
};
```

### **Passo 4: Implementação da Inicialização**

#### **4.1 Criar função main**

```cpp
// src/main.cpp
#include "canary_server.hpp"
#include <iostream>
#include <signal.h>

CanaryServer* g_server = nullptr;

void signalHandler(int signal) {
    if (g_server) {
        std::cout << "Recebido sinal " << signal << ", desligando servidor..." << std::endl;
        g_server->shutdown();
    }
}

int main() {
    try {
        // Configurar handler de sinais
        signal(SIGINT, signalHandler);
        signal(SIGTERM, signalHandler);
        
        // Criar servidor
        CanaryServer server;
        g_server = &server;
        
        // Inicializar servidor
        if (!server.initialize()) {
            std::cerr << "Erro na inicialização do servidor" << std::endl;
            return EXIT_FAILURE;
        }
        
        // Executar servidor
        int result = server.run();
        
        if (result == EXIT_SUCCESS) {
            std::cout << "Servidor encerrado com sucesso" << std::endl;
        } else {
            std::cerr << "Erro na execução do servidor" << std::endl;
        }
        
        return result;
        
    } catch (const std::exception& e) {
        std::cerr << "Erro crítico: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }
}
```

### **Passo 5: Compilação e Teste**

#### **5.1 Criar Makefile**

```makefile
# Makefile
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -O2
INCLUDES = -I./src
LIBS = -lasio -lmysqlclient -llua5.3

SRCDIR = src
OBJDIR = obj
BINDIR = bin

SOURCES = $(wildcard $(SRCDIR)/*.cpp)
OBJECTS = $(SOURCES:$(SRCDIR)/%.cpp=$(OBJDIR)/%.o)

TARGET = $(BINDIR)/canary

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(OBJECTS)
	@mkdir -p $(BINDIR)
	$(CXX) $(OBJECTS) -o $@ $(LIBS)

$(OBJDIR)/%.o: $(SRCDIR)/%.cpp
	@mkdir -p $(OBJDIR)
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

clean:
	rm -rf $(OBJDIR) $(BINDIR)
```

#### **5.2 Compilar e executar**

```bash
# Compilar o projeto
make clean
make

# Executar o servidor
./bin/canary
```

### **Passo 6: Validação e Testes**

#### **6.1 Testar conectividade**

```bash
# Testar porta de login
telnet localhost 7171

# Testar porta do jogo
telnet localhost 7172

# Testar porta de status
telnet localhost 7173
```

#### **6.2 Verificar logs**

```bash
# Verificar logs do servidor
tail -f logs/canary.log

# Verificar logs do sistema
journalctl -u canary -f
```

## ✅ Checklist de Conclusão

- [ ] **Ambiente configurado**: Diretórios e dependências
- [ ] **Configuração criada**: Arquivo config.lua funcional
- [ ] **Banco configurado**: MySQL/MariaDB funcionando
- [ ] **Componentes implementados**: Classes core criadas
- [ ] **Servidor compilado**: Projeto compila sem erros
- [ ] **Servidor executado**: Servidor inicia corretamente
- [ ] **Serviços ativos**: Portas respondem corretamente
- [ ] **Logs funcionando**: Sistema de logging ativo
- [ ] **Testes passaram**: Conectividade validada

## 🔗 Links Relacionados

- **Conceito**: [[concepts/canary_core_architecture|Arquitetura Core do Canary]]
- **Exemplo Prático**: [[examples/canary_core_setup|Configuração da Arquitetura Core]]
- **Análise Técnica**: [[habdel/CANARY-002|CANARY-002: Análise da Arquitetura Core]]
- **Módulo Educacional**: [[modules/02_canary/02_core_architecture|Módulo: Arquitetura Core]]

## 📚 Recursos Adicionais

- **Tópico Canary**: [[topics/canary|Índice Canary]]
- **Templates**: [[templates/exercise_template|Template de Exercício]]
- **Configuração Básica**: [[exercises/setup_canary_server|Configuração Básica do Servidor]] 