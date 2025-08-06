---
tags: [example, otclient, setup, configuration, basic_installation, client_setup]
type: code_example
status: active
priority: high
created: 2025-08-05
level: beginner
feature: [client_setup, basic_configuration, lua_integration, graphics_setup]
aliases: [OTClient Setup, Client Configuration, Basic Installation, OTClient Example]
---

# 🎮 Configuração Básica do OTClient

## Implementação Prática da Configuração do OTClient

Este exemplo demonstra como configurar e inicializar o OTClient básico, incluindo setup de gráficos, sistema de eventos e integração Lua.

## 🎯 Configuração Básica

### **1. Estrutura do Projeto**

```cpp
// src/application.hpp
#pragma once
#include <memory>
#include <string>
#include "graphics/graphics_engine.hpp"
#include "network/network_manager.hpp"
#include "ui/ui_manager.hpp"
#include "lua/lua_script_interface.hpp"

class Application {
public:
    Application();
    ~Application();
    
    bool init();
    void run();
    void terminate();
    
private:
    bool initGraphics();
    bool initNetwork();
    bool initUI();
    bool initLua();
    
    std::unique_ptr<GraphicsEngine> graphicsEngine;
    std::unique_ptr<NetworkManager> networkManager;
    std::unique_ptr<UIManager> uiManager;
    std::unique_ptr<LuaScriptInterface> luaInterface;
    
    bool running;
};
```

### **2. Implementação da Aplicação**

```cpp
// src/application.cpp
#include "application.hpp"
#include <iostream>

Application::Application() : running(false) {
    graphicsEngine = std::make_unique<GraphicsEngine>();
    networkManager = std::make_unique<NetworkManager>();
    uiManager = std::make_unique<UIManager>();
    luaInterface = std::make_unique<LuaScriptInterface>();
}

Application::~Application() {
    terminate();
}

bool Application::init() {
    std::cout << "Inicializando OTClient..." << std::endl;
    
    // Inicializar gráficos
    if (!initGraphics()) {
        std::cerr << "Erro ao inicializar gráficos" << std::endl;
        return false;
    }
    
    // Inicializar rede
    if (!initNetwork()) {
        std::cerr << "Erro ao inicializar rede" << std::endl;
        return false;
    }
    
    // Inicializar UI
    if (!initUI()) {
        std::cerr << "Erro ao inicializar UI" << std::endl;
        return false;
    }
    
    // Inicializar Lua
    if (!initLua()) {
        std::cerr << "Erro ao inicializar Lua" << std::endl;
        return false;
    }
    
    running = true;
    std::cout << "OTClient inicializado com sucesso!" << std::endl;
    return true;
}

void Application::run() {
    std::cout << "Executando loop principal..." << std::endl;
    
    while (running) {
        // Processar eventos
        uiManager->pollEvents();
        
        // Atualizar lógica
        luaInterface->update();
        
        // Renderizar cena
        graphicsEngine->clear();
        uiManager->render();
        graphicsEngine->swapBuffers();
        
        // Comunicar com servidor
        networkManager->update();
    }
}

void Application::terminate() {
    if (running) {
        std::cout << "Finalizando OTClient..." << std::endl;
        
        luaInterface->shutdown();
        uiManager->shutdown();
        networkManager->disconnect();
        graphicsEngine->shutdown();
        
        running = false;
        std::cout << "OTClient finalizado!" << std::endl;
    }
}
```

## 🔧 Configuração Avançada

### **3. Sistema de Gráficos**

```cpp
// src/graphics/graphics_engine.hpp
#pragma once
#include <string>

class GraphicsEngine {
public:
    GraphicsEngine();
    ~GraphicsEngine();
    
    bool init();
    void shutdown();
    void clear();
    void swapBuffers();
    void resize(int width, int height);
    
    bool loadTexture(const std::string& name, const std::string& path);
    void drawSprite(const std::string& texture, int x, int y);
    
private:
    bool initOpenGL();
    bool initShaders();
    
    int windowWidth;
    int windowHeight;
    bool initialized;
};
```

### **4. Sistema de Eventos**

```cpp
// src/events/event_dispatcher.hpp
#pragma once
#include <functional>
#include <vector>
#include <memory>

class Event {
public:
    virtual ~Event() = default;
    virtual std::string getType() const = 0;
};

class EventDispatcher {
public:
    using EventCallback = std::function<void(const Event&)>;
    
    void addEventListener(const std::string& eventType, EventCallback callback);
    void removeEventListener(const std::string& eventType);
    void dispatchEvent(const Event& event);
    
private:
    std::vector<std::pair<std::string, EventCallback>> listeners;
};
```

### **5. Integração Lua**

```cpp
// src/lua/lua_script_interface.hpp
#pragma once
#include <lua.hpp>
#include <string>

class LuaScriptInterface {
public:
    LuaScriptInterface();
    ~LuaScriptInterface();
    
    bool init();
    void shutdown();
    void update();
    
    bool loadScript(const std::string& scriptPath);
    bool executeFunction(const std::string& functionName);
    
private:
    lua_State* L;
    bool initialized;
    
    void registerFunctions();
    void registerClasses();
};
```

## 🎮 Scripts Lua de Configuração

### **6. Script de Inicialização**

```lua
-- scripts/init.lua
local otclient = {}

-- Configurações básicas
otclient.config = {
    windowTitle = "OTClient - MMORPG Client",
    windowWidth = 1024,
    windowHeight = 768,
    fullscreen = false,
    vsync = true,
    maxFPS = 60
}

-- Função de inicialização
function otclient.init()
    print("Inicializando scripts Lua...")
    
    -- Carregar módulos básicos
    require("modules/ui")
    require("modules/graphics")
    require("modules/network")
    require("modules/game")
    
    -- Configurar eventos
    otclient.setupEvents()
    
    print("Scripts Lua inicializados!")
end

-- Configurar eventos do sistema
function otclient.setupEvents()
    -- Evento de conexão com servidor
    connect(g_game, { onConnect = function()
        print("Conectado ao servidor!")
    end})
    
    -- Evento de desconexão
    connect(g_game, { onDisconnect = function()
        print("Desconectado do servidor!")
    end})
    
    -- Evento de login
    connect(g_game, { onLoginAdvice = function(message)
        print("Login: " .. message)
    end})
end

-- Função de atualização
function otclient.update()
    -- Atualizar módulos
    if modules.ui then
        modules.ui.update()
    end
    
    if modules.graphics then
        modules.graphics.update()
    end
end

-- Retornar módulo
return otclient
```

### **7. Módulo de Interface**

```lua
-- scripts/modules/ui.lua
local ui = {}

function ui.init()
    print("Inicializando módulo UI...")
    
    -- Criar janela principal
    ui.mainWindow = g_ui.createWidget('MainWindow')
    ui.mainWindow:setSize({width = 1024, height = 768})
    ui.mainWindow:setText('OTClient')
    
    -- Criar menu principal
    ui.mainMenu = g_ui.createWidget('MainMenu', ui.mainWindow)
    ui.mainMenu:addButton('Conectar', function()
        ui.connectToServer()
    end)
    
    ui.mainMenu:addButton('Configurações', function()
        ui.showSettings()
    end)
    
    ui.mainMenu:addButton('Sair', function()
        g_app.exit()
    end)
    
    print("Módulo UI inicializado!")
end

function ui.update()
    -- Atualizar interface
    if ui.mainWindow then
        ui.mainWindow:update()
    end
end

function ui.connectToServer()
    local serverWindow = g_ui.createWidget('ServerWindow')
    serverWindow:setText('Conectar ao Servidor')
    
    -- Campos de conexão
    local hostField = g_ui.createWidget('TextField', serverWindow)
    hostField:setText('localhost')
    
    local portField = g_ui.createWidget('TextField', serverWindow)
    portField:setText('7172')
    
    -- Botão conectar
    local connectButton = g_ui.createWidget('Button', serverWindow)
    connectButton:setText('Conectar')
    connectButton.onClick = function()
        local host = hostField:getText()
        local port = tonumber(portField:getText())
        
        g_game.connect(host, port)
        serverWindow:destroy()
    end
end

function ui.showSettings()
    local settingsWindow = g_ui.createWidget('SettingsWindow')
    settingsWindow:setText('Configurações')
    
    -- Configurações de gráficos
    local graphicsGroup = g_ui.createWidget('GroupBox', settingsWindow)
    graphicsGroup:setText('Gráficos')
    
    local fullscreenCheck = g_ui.createWidget('CheckBox', graphicsGroup)
    fullscreenCheck:setText('Tela Cheia')
    fullscreenCheck:setChecked(g_window.isFullscreen())
    
    local vsyncCheck = g_ui.createWidget('CheckBox', graphicsGroup)
    vsyncCheck:setText('VSync')
    vsyncCheck:setChecked(g_window.isVerticalSync())
end

return ui
```

## 🧪 Testando a Configuração

### **8. Script de Teste**

```cpp
// test_otclient.cpp
#include "application.hpp"
#include <iostream>

class OTClientTester {
public:
    static void testOTClient() {
        std::cout << "=== Teste do OTClient ===" << std::endl;
        
        // Criar aplicação
        Application app;
        
        // Testar inicialização
        if (app.init()) {
            std::cout << "✅ Inicialização bem-sucedida" << std::endl;
            
            // Executar por alguns segundos
            std::cout << "Executando por 5 segundos..." << std::endl;
            // app.run(); // Em um teste real, executaria o loop
            
            // Finalizar
            app.terminate();
            std::cout << "✅ Finalização bem-sucedida" << std::endl;
        } else {
            std::cout << "❌ Erro na inicialização" << std::endl;
        }
        
        std::cout << "=== Teste Concluído ===" << std::endl;
    }
};
```

### **9. Script Lua de Teste**

```lua
-- test_otclient.lua
local test = {}

function test.run()
    print("=== Teste do OTClient Lua ===")
    
    -- Testar módulo principal
    local otclient = require("init")
    otclient.init()
    
    -- Testar módulo UI
    local ui = require("modules/ui")
    ui.init()
    
    -- Simular eventos
    print("Simulando eventos...")
    
    -- Testar conexão
    ui.connectToServer()
    
    -- Testar configurações
    ui.showSettings()
    
    print("=== Teste Lua Concluído ===")
end

-- Executar teste
test.run()
```

## 🔗 Links Relacionados

- **Conceito**: [[concepts/otclient_introduction|Introdução ao OTClient]]
- **Exercício Prático**: [[exercises/build_otclient_basic|Construindo OTClient Básico]]
- **Análise Técnica**: [[habdel/OTCLIENT-021|OTCLIENT-021: Documentação Consolidada]]
- **Módulo Educacional**: [[modules/03_otclient/01_otclient_introduction|Módulo: Introdução ao OTClient]]

## 📚 Recursos Adicionais

- **Tópico OTClient**: [[topics/otclient|Índice OTClient]]
- **Templates**: [[templates/example_template|Template de Exemplo]]
- **Arquitetura Geral**: [[examples/architecture_setup|Configuração da Arquitetura]] 