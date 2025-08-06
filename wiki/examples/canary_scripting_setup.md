---
tags: [example, canary, scripting_system, modules, lua, recvbyte, delays]
type: code_example
status: active
priority: high
created: 2025-08-05
level: intermediate
feature: [scripting, modules, lua_integration, network_interception]
aliases: [Canary Scripting Setup, Module Configuration, Lua Integration Example]
---

# 🔧 Configuração do Sistema de Scripting

## Implementação Prática do Sistema de Scripting do Canary

Este exemplo demonstra como configurar e implementar o sistema de scripting do Canary, incluindo módulos Lua, interceptação de recvbyte e gerenciamento de delays.

## 🎯 Configuração Básica

### **1. Estrutura de Módulos**

```cpp
// src/lua/modules/modules.hpp
#pragma once
#include "lua/lua_script_interface.hpp"
#include "game/functions/game_reload.hpp"
#include <map>
#include <memory>

class Module : public Event {
public:
    explicit Module(LuaScriptInterface* interface);
    
    bool configureEvent(const pugi::xml_node& node) override;
    ModuleType_t getEventType() const { return type; }
    bool isLoaded() const { return loaded; }
    
    void executeOnRecvbyte(const std::shared_ptr<Player>& player, NetworkMessage& msg) const;
    uint8_t getRecvbyte() const { return recvbyte; }
    int16_t getDelay() const { return delay; }
    
protected:
    std::string getScriptEventName() const override;
    
private:
    ModuleType_t type;
    uint8_t recvbyte {};
    int16_t delay {};
    bool loaded;
};
```

### **2. Gerenciador de Módulos**

```cpp
// src/lua/modules/modules_manager.hpp
#pragma once
#include "modules.hpp"
#include <map>

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

### **3. Gerenciamento de Delays do Jogador**

```cpp
// src/creatures/players/player_modules.hpp
#pragma once
#include <map>
#include <cstdint>

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

## 🔧 Configuração Avançada

### **4. Configuração XML de Módulos**

```xml
<!-- data/modules/custom_module.xml -->
<?xml version="1.0" encoding="UTF-8"?>
<modules>
    <module name="CustomModule" script="custom_module.lua" recvbyte="0x64" delay="1000">
        <description>Módulo customizado para funcionalidade específica</description>
        <author>Seu Nome</author>
        <version>1.0</version>
    </module>
    
    <module name="ChatModule" script="chat_module.lua" recvbyte="0x96" delay="500">
        <description>Módulo para interceptar mensagens de chat</description>
        <author>Seu Nome</author>
        <version>1.0</version>
    </module>
</modules>
```

### **5. Script Lua do Módulo**

```lua
-- data/modules/scripts/custom_module.lua
local customModule = {}

-- Configuração do módulo
customModule.name = "CustomModule"
customModule.version = "1.0"
customModule.author = "Seu Nome"

-- Função executada quando o recvbyte é recebido
function customModule.onRecvbyte(player, msg, byte)
    -- Verificar se o jogador pode executar o módulo
    if not player:canRunModule(byte) then
        return false
    end
    
    -- Processar a mensagem
    local messageType = msg:getByte()
    local messageData = msg:getString()
    
    -- Implementar lógica customizada
    if messageType == 0x01 then
        -- Processar tipo 1
        customModule:processType1(player, messageData)
    elseif messageType == 0x02 then
        -- Processar tipo 2
        customModule:processType2(player, messageData)
    end
    
    -- Definir delay para próxima execução
    player:setModuleDelay(byte, 1000)
    
    return true
end

-- Funções auxiliares
function customModule:processType1(player, data)
    print("Processando tipo 1 para jogador: " .. player:getName())
    -- Implementar lógica específica
end

function customModule:processType2(player, data)
    print("Processando tipo 2 para jogador: " .. player:getName())
    -- Implementar lógica específica
end

-- Registrar o módulo
registerModule(customModule)
```

### **6. Sistema de Recarregamento**

```cpp
// src/game/functions/game_reload.hpp
#pragma once
#include <cstdint>

enum class Reload_t : uint8_t {
    RELOAD_TYPE_NONE,
    RELOAD_TYPE_ALL,
    RELOAD_TYPE_MODULES,  // Recarregamento específico de módulos
    // ... outros tipos
};

class GameReload {
public:
    static bool init(Reload_t reloadType);
    static uint8_t getReloadNumber(Reload_t reloadTypes);
    
private:
    static bool reloadModules();
    static bool reloadModuleScripts();
    static bool reloadModuleConfigs();
};
```

## 🧪 Testando o Sistema

### **7. Script de Teste de Módulos**

```cpp
// test_modules.cpp
#include "lua/modules/modules_manager.hpp"
#include "creatures/players/player.hpp"
#include <iostream>

class ModuleTester {
public:
    static void testModuleSystem() {
        std::cout << "=== Teste do Sistema de Módulos ===" << std::endl;
        
        // Testar carregamento de módulos
        auto& modulesManager = g_modules();
        
        // Simular mensagem de rede
        NetworkMessage msg;
        msg.addByte(0x64);  // Recvbyte do módulo customizado
        msg.addString("Teste de módulo");
        
        // Testar execução
        uint32_t playerId = 1;
        modulesManager.executeOnRecvbyte(playerId, msg, 0x64);
        
        // Verificar se módulo foi executado
        auto module = modulesManager.getEventByRecvbyte(0x64, false);
        if (module && module->isLoaded()) {
            std::cout << "Módulo carregado com sucesso" << std::endl;
        } else {
            std::cout << "Erro no carregamento do módulo" << std::endl;
        }
        
        std::cout << "=== Teste Concluído ===" << std::endl;
    }
};
```

### **8. Script Lua de Teste**

```lua
-- test_module.lua
local testModule = {}

function testModule.onRecvbyte(player, msg, byte)
    print("Teste: Módulo executado para jogador " .. player:getName())
    print("Teste: Byte recebido: 0x" .. string.format("%02X", byte))
    
    -- Simular processamento
    local data = msg:getString()
    print("Teste: Dados recebidos: " .. data)
    
    -- Retornar sucesso
    return true
end

-- Registrar módulo de teste
registerModule(testModule)
```

## 🔗 Links Relacionados

- **Conceito**: [[concepts/canary_scripting_system|Sistema de Scripting do Canary]]
- **Exercício Prático**: [[exercises/build_scripting_system|Construindo o Sistema de Scripting]]
- **Análise Técnica**: [[habdel/CANARY-006|CANARY-006: Sistema de Módulos]]
- **Módulo Educacional**: [[modules/02_canary/03_scripting_system|Módulo: Sistema de Scripting]]

## 📚 Recursos Adicionais

- **Tópico Canary**: [[topics/canary|Índice Canary]]
- **Templates**: [[templates/example_template|Template de Exemplo]]
- **Arquitetura Core**: [[examples/canary_core_setup|Configuração da Arquitetura Core]] 