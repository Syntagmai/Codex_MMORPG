---
tags: [exercise, canary, scripting_system, hands_on, modules, lua_integration]
type: exercise
status: active
priority: high
created: 2025-08-05
level: intermediate
duration: 3-4 horas
prerequisites: [canary_server_overview, canary_core_architecture, canary_scripting_system]
aliases: [Build Scripting System, Module System Exercise, Lua Integration Exercise]
---

# 🎮 Construindo o Sistema de Scripting

## Exercício Prático de Construção do Sistema de Scripting do Canary

Este exercício guia você através da implementação completa do sistema de scripting do Canary, incluindo módulos Lua, interceptação de recvbyte e gerenciamento de delays.

## 🎯 Objetivos do Exercício

- ✅ Implementar sistema de módulos Lua completo
- ✅ Configurar interceptação de recvbyte
- ✅ Implementar gerenciamento de delays
- ✅ Criar módulos customizados funcionais
- ✅ Testar e validar o sistema completo

## 📋 Pré-requisitos

- [ ] Ambiente de desenvolvimento configurado
- [ ] Código-fonte do Canary baixado
- [ ] Compilador C++ configurado
- [ ] Lua 5.3 instalado
- [ ] Conhecimento básico de C++ e Lua
- [ ] Módulos anteriores concluídos

## 🔧 Passo a Passo

### **Passo 1: Preparação da Estrutura**

```bash
# 1. Navegar para o diretório do projeto
cd canary/

# 2. Criar estrutura de módulos
mkdir -p src/lua/modules/
mkdir -p data/modules/
mkdir -p data/modules/scripts/

# 3. Verificar dependências Lua
ls -la /usr/include/lua5.3/
```

### **Passo 2: Implementação das Classes Base**

#### **2.1 Criar classe Module**

```cpp
// src/lua/modules/module.hpp
#pragma once
#include "lua/lua_script_interface.hpp"
#include "game/events/event.hpp"
#include <memory>
#include <string>

enum class ModuleType_t {
    MODULE_TYPE_RECVBYTE,
    MODULE_TYPE_NONE
};

class Module : public Event {
public:
    explicit Module(LuaScriptInterface* interface);
    ~Module() override = default;
    
    bool configureEvent(const pugi::xml_node& node) override;
    ModuleType_t getEventType() const { return type; }
    bool isLoaded() const { return loaded; }
    
    void executeOnRecvbyte(const std::shared_ptr<Player>& player, NetworkMessage& msg) const;
    uint8_t getRecvbyte() const { return recvbyte; }
    int16_t getDelay() const { return delay; }
    
    void clearEvent();
    void copyEvent(const Module_ptr& module);
    
protected:
    std::string getScriptEventName() const override;
    
private:
    ModuleType_t type;
    uint8_t recvbyte {};
    int16_t delay {};
    bool loaded;
};
```

#### **2.2 Implementar Module.cpp**

```cpp
// src/lua/modules/module.cpp
#include "module.hpp"
#include "lua/lua_script_interface.hpp"
#include "creatures/players/player.hpp"
#include "network/network_message.hpp"

Module::Module(LuaScriptInterface* interface) : Event(interface), type(ModuleType_t::MODULE_TYPE_NONE), loaded(false) {}

bool Module::configureEvent(const pugi::xml_node& node) {
    // Configurar tipo do módulo
    std::string typeStr = node.attribute("type").as_string();
    if (typeStr == "recvbyte") {
        type = ModuleType_t::MODULE_TYPE_RECVBYTE;
    }
    
    // Configurar recvbyte
    recvbyte = node.attribute("recvbyte").as_uint();
    
    // Configurar delay
    delay = node.attribute("delay").as_int(1000);
    
    // Carregar script Lua
    std::string scriptFile = node.attribute("script").as_string();
    if (!scriptFile.empty()) {
        loaded = getScriptInterface()->loadFile("data/modules/scripts/" + scriptFile);
    }
    
    return loaded;
}

void Module::executeOnRecvbyte(const std::shared_ptr<Player>& player, NetworkMessage& msg) const {
    if (!loaded || !player) {
        return;
    }
    
    // Verificar se jogador pode executar o módulo
    if (!player->canRunModule(recvbyte)) {
        return;
    }
    
    // Executar script Lua
    getScriptInterface()->executeFunction("onRecvbyte", player, msg, recvbyte);
    
    // Definir delay
    player->setModuleDelay(recvbyte, delay);
}

std::string Module::getScriptEventName() const {
    return "onRecvbyte";
}
```

### **Passo 3: Implementação do Gerenciador**

#### **3.1 Criar ModulesManager**

```cpp
// src/lua/modules/modules_manager.hpp
#pragma once
#include "module.hpp"
#include "lua/lua_script_interface.hpp"
#include <map>
#include <memory>

class ModulesManager {
public:
    static ModulesManager& getInstance();
    
    void executeOnRecvbyte(uint32_t playerId, NetworkMessage& msg, uint8_t byte) const;
    Module_ptr getEventByRecvbyte(uint8_t recvbyte, bool force);
    bool registerModule(const Module_ptr& module, const pugi::xml_node& node);
    void clear();
    
protected:
    LuaScriptInterface& getScriptInterface();
    std::string getScriptBaseName() const;
    Event_ptr getEvent(const std::string& nodeName);
    
private:
    using ModulesList = std::map<uint8_t, Module_ptr>;
    ModulesList recvbyteList;
    LuaScriptInterface scriptInterface;
};

constexpr auto g_modules = ModulesManager::getInstance;
```

#### **3.2 Implementar ModulesManager.cpp**

```cpp
// src/lua/modules/modules_manager.cpp
#include "modules_manager.hpp"
#include "creatures/players/player.hpp"
#include "network/network_message.hpp"
#include <iostream>

ModulesManager::ModulesManager() {
    scriptInterface.initState();
}

ModulesManager& ModulesManager::getInstance() {
    static ModulesManager instance;
    return instance;
}

void ModulesManager::executeOnRecvbyte(uint32_t playerId, NetworkMessage& msg, uint8_t byte) const {
    auto it = recvbyteList.find(byte);
    if (it != recvbyteList.end()) {
        auto module = it->second;
        if (module && module->isLoaded()) {
            // Buscar jogador (simplificado)
            auto player = std::make_shared<Player>(playerId);
            module->executeOnRecvbyte(player, msg);
        }
    }
}

Module_ptr ModulesManager::getEventByRecvbyte(uint8_t recvbyte, bool force) {
    auto it = recvbyteList.find(recvbyte);
    if (it != recvbyteList.end()) {
        return it->second;
    }
    return nullptr;
}

bool ModulesManager::registerModule(const Module_ptr& module, const pugi::xml_node& node) {
    if (!module) {
        return false;
    }
    
    uint8_t recvbyte = module->getRecvbyte();
    recvbyteList[recvbyte] = module;
    
    std::cout << "Módulo registrado com recvbyte: 0x" << std::hex << (int)recvbyte << std::endl;
    return true;
}

LuaScriptInterface& ModulesManager::getScriptInterface() {
    return scriptInterface;
}

std::string ModulesManager::getScriptBaseName() const {
    return "modules";
}
```

### **Passo 4: Configuração de Módulos**

#### **4.1 Criar arquivo de configuração XML**

```xml
<!-- data/modules/modules.xml -->
<?xml version="1.0" encoding="UTF-8"?>
<modules>
    <module name="ChatModule" type="recvbyte" script="chat_module.lua" recvbyte="0x96" delay="500">
        <description>Módulo para interceptar mensagens de chat</description>
        <author>Seu Nome</author>
        <version>1.0</version>
    </module>
    
    <module name="MovementModule" type="recvbyte" script="movement_module.lua" recvbyte="0x64" delay="100">
        <description>Módulo para interceptar movimentos</description>
        <author>Seu Nome</author>
        <version>1.0</version>
    </module>
    
    <module name="CustomModule" type="recvbyte" script="custom_module.lua" recvbyte="0x32" delay="1000">
        <description>Módulo customizado para funcionalidade específica</description>
        <author>Seu Nome</author>
        <version>1.0</version>
    </module>
</modules>
```

#### **4.2 Criar scripts Lua dos módulos**

```lua
-- data/modules/scripts/chat_module.lua
local chatModule = {}

function chatModule.onRecvbyte(player, msg, byte)
    print("ChatModule: Interceptando mensagem de chat")
    
    -- Ler dados da mensagem
    local message = msg:getString()
    local channel = msg:getByte()
    
    -- Processar mensagem
    if channel == 0x01 then
        print("Chat público: " .. message)
    elseif channel == 0x02 then
        print("Chat privado: " .. message)
    end
    
    return true
end

-- Registrar módulo
registerModule(chatModule)
```

```lua
-- data/modules/scripts/movement_module.lua
local movementModule = {}

function movementModule.onRecvbyte(player, msg, byte)
    print("MovementModule: Interceptando movimento")
    
    -- Ler dados do movimento
    local direction = msg:getByte()
    local x = msg:getU16()
    local y = msg:getU16()
    local z = msg:getByte()
    
    -- Processar movimento
    print("Movimento: " .. direction .. " para (" .. x .. "," .. y .. "," .. z .. ")")
    
    return true
end

-- Registrar módulo
registerModule(movementModule)
```

```lua
-- data/modules/scripts/custom_module.lua
local customModule = {}

function customModule.onRecvbyte(player, msg, byte)
    print("CustomModule: Executando funcionalidade customizada")
    
    -- Implementar lógica customizada
    local action = msg:getByte()
    
    if action == 0x01 then
        print("Ação 1 executada")
        -- Implementar ação 1
    elseif action == 0x02 then
        print("Ação 2 executada")
        -- Implementar ação 2
    end
    
    return true
end

-- Registrar módulo
registerModule(customModule)
```

### **Passo 5: Sistema de Delays**

#### **5.1 Implementar gerenciamento de delays**

```cpp
// src/creatures/players/player_modules.hpp
#pragma once
#include <map>
#include <cstdint>
#include <chrono>

class PlayerModules {
public:
    void setModuleDelay(uint8_t byteOrType, int16_t delay);
    bool canRunModule(uint8_t byteOrType);
    void clearModuleDelays();
    
private:
    std::map<uint8_t, int64_t> moduleDelayMap;
    
    int64_t getCurrentTime() const;
    bool isDelayExpired(uint8_t byteOrType) const;
};
```

#### **5.2 Implementar PlayerModules.cpp**

```cpp
// src/creatures/players/player_modules.cpp
#include "player_modules.hpp"
#include <chrono>

void PlayerModules::setModuleDelay(uint8_t byteOrType, int16_t delay) {
    int64_t currentTime = getCurrentTime();
    int64_t nextExecution = currentTime + delay;
    moduleDelayMap[byteOrType] = nextExecution;
}

bool PlayerModules::canRunModule(uint8_t byteOrType) {
    return isDelayExpired(byteOrType);
}

void PlayerModules::clearModuleDelays() {
    moduleDelayMap.clear();
}

int64_t PlayerModules::getCurrentTime() const {
    auto now = std::chrono::steady_clock::now();
    return std::chrono::duration_cast<std::chrono::milliseconds>(now.time_since_epoch()).count();
}

bool PlayerModules::isDelayExpired(uint8_t byteOrType) const {
    auto it = moduleDelayMap.find(byteOrType);
    if (it == moduleDelayMap.end()) {
        return true; // Sem delay configurado
    }
    
    int64_t currentTime = getCurrentTime();
    return currentTime >= it->second;
}
```

### **Passo 6: Compilação e Teste**

#### **6.1 Atualizar Makefile**

```makefile
# Makefile
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -O2
INCLUDES = -I./src -I/usr/include/lua5.3
LIBS = -lasio -lmysqlclient -llua5.3 -lpugixml

SRCDIR = src
OBJDIR = obj
BINDIR = bin

SOURCES = $(wildcard $(SRCDIR)/*.cpp) $(wildcard $(SRCDIR)/lua/modules/*.cpp) $(wildcard $(SRCDIR)/creatures/players/*.cpp)
OBJECTS = $(SOURCES:$(SRCDIR)/%.cpp=$(OBJDIR)/%.o)

TARGET = $(BINDIR)/canary

.PHONY: all clean test

all: $(TARGET)

$(TARGET): $(OBJECTS)
	@mkdir -p $(BINDIR)
	$(CXX) $(OBJECTS) -o $@ $(LIBS)

$(OBJDIR)/%.o: $(SRCDIR)/%.cpp
	@mkdir -p $(dir $@)
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

test: $(TARGET)
	./$(TARGET) --test-modules

clean:
	rm -rf $(OBJDIR) $(BINDIR)
```

#### **6.2 Script de teste**

```cpp
// test_scripting_system.cpp
#include "lua/modules/modules_manager.hpp"
#include "creatures/players/player_modules.hpp"
#include <iostream>

class ScriptingSystemTester {
public:
    static void testScriptingSystem() {
        std::cout << "=== Teste do Sistema de Scripting ===" << std::endl;
        
        // Testar gerenciador de módulos
        auto& modulesManager = g_modules();
        
        // Testar gerenciamento de delays
        PlayerModules playerModules;
        
        // Testar delay
        playerModules.setModuleDelay(0x96, 1000);
        std::cout << "Delay configurado para 0x96" << std::endl;
        
        // Verificar se pode executar
        if (playerModules.canRunModule(0x96)) {
            std::cout << "Módulo pode executar" << std::endl;
        } else {
            std::cout << "Módulo em delay" << std::endl;
        }
        
        // Simular mensagem
        NetworkMessage msg;
        msg.addByte(0x96);
        msg.addString("Teste de chat");
        
        // Executar módulo
        modulesManager.executeOnRecvbyte(1, msg, 0x96);
        
        std::cout << "=== Teste Concluído ===" << std::endl;
    }
};
```

### **Passo 7: Validação e Testes**

#### **7.1 Testar carregamento de módulos**

```bash
# Compilar o projeto
make clean
make

# Executar testes
make test

# Verificar logs
tail -f logs/canary.log
```

#### **7.2 Testar módulos individualmente**

```bash
# Testar módulo de chat
echo "Testando módulo de chat..."
./bin/canary --test-module=chat

# Testar módulo de movimento
echo "Testando módulo de movimento..."
./bin/canary --test-module=movement

# Testar módulo customizado
echo "Testando módulo customizado..."
./bin/canary --test-module=custom
```

## ✅ Checklist de Conclusão

- [ ] **Estrutura criada**: Diretórios e arquivos de módulos
- [ ] **Classes implementadas**: Module e ModulesManager
- [ ] **Configuração XML**: Arquivo de configuração de módulos
- [ ] **Scripts Lua**: Módulos funcionais implementados
- [ ] **Sistema de delays**: Gerenciamento de delays implementado
- [ ] **Compilação**: Projeto compila sem erros
- [ ] **Testes funcionando**: Módulos executam corretamente
- [ ] **Logs ativos**: Sistema de logging funcionando
- [ ] **Validação completa**: Todos os testes passaram

## 🔗 Links Relacionados

- **Conceito**: [[concepts/canary_scripting_system|Sistema de Scripting do Canary]]
- **Exemplo Prático**: [[examples/canary_scripting_setup|Configuração do Sistema de Scripting]]
- **Análise Técnica**: [[habdel/CANARY-006|CANARY-006: Sistema de Módulos]]
- **Módulo Educacional**: [[modules/02_canary/03_scripting_system|Módulo: Sistema de Scripting]]

## 📚 Recursos Adicionais

- **Tópico Canary**: [[topics/canary|Índice Canary]]
- **Templates**: [[templates/exercise_template|Template de Exercício]]
- **Arquitetura Core**: [[exercises/build_core_architecture|Construindo a Arquitetura Core]] 