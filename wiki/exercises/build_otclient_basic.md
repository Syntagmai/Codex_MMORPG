---
tags: [exercise, otclient, hands_on, basic_build, client_development, cpp_lua]
type: exercise
status: active
priority: high
created: 2025-08-05
level: beginner
duration: 2-3 horas
prerequisites: [architecture_overview, otclient_introduction]
aliases: [Build OTClient Basic, Client Development Exercise, OTClient Hands-on]
---

# 🎮 Construindo OTClient Básico

## Exercício Prático de Construção do OTClient

Este exercício guia você através da construção de um OTClient básico funcional, incluindo sistema de gráficos, interface do usuário e integração Lua.

## 🎯 Objetivos do Exercício

- ✅ Configurar ambiente de desenvolvimento OTClient
- ✅ Implementar sistema de aplicação básico
- ✅ Criar sistema de gráficos simples
- ✅ Implementar interface do usuário básica
- ✅ Integrar scripting Lua
- ✅ Testar e validar o cliente

## 📋 Pré-requisitos

- [ ] Ambiente de desenvolvimento configurado
- [ ] Compilador C++ (GCC, Clang, ou MSVC)
- [ ] Lua 5.3 instalado
- [ ] OpenGL ou biblioteca gráfica
- [ ] Conhecimento básico de C++ e Lua
- [ ] Módulos anteriores concluídos

## 🔧 Passo a Passo

### **Passo 1: Preparação do Ambiente**

```bash
# 1. Criar estrutura do projeto
mkdir otclient-basic
cd otclient-basic

# 2. Criar estrutura de diretórios
mkdir -p src/{core,graphics,ui,lua,network}
mkdir -p scripts/{modules,init}
mkdir -p data/{textures,sounds,config}
mkdir -p build

# 3. Verificar dependências
lua -v
g++ --version
```

### **Passo 2: Configuração do CMake**

```cmake
# CMakeLists.txt
cmake_minimum_required(VERSION 3.16)
project(OTClientBasic VERSION 1.0.0)

# Configurar C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Encontrar dependências
find_package(Lua 5.3 REQUIRED)
find_package(OpenGL REQUIRED)
find_package(glfw3 REQUIRED)

# Configurar diretórios
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

# Adicionar subdiretórios
add_subdirectory(src)

# Configurar executável principal
add_executable(otclient_basic 
    src/main.cpp
    src/application.cpp
    src/graphics/graphics_engine.cpp
    src/ui/ui_manager.cpp
    src/lua/lua_script_interface.cpp
    src/network/network_manager.cpp
)

# Linkar bibliotecas
target_link_libraries(otclient_basic 
    ${LUA_LIBRARIES}
    OpenGL::GL
    glfw
)

# Incluir diretórios
target_include_directories(otclient_basic PRIVATE
    ${CMAKE_SOURCE_DIR}/src
    ${LUA_INCLUDE_DIR}
)
```

### **Passo 3: Implementação do Core**

#### **3.1 Classe Application**

```cpp
// src/application.hpp
#pragma once
#include <memory>
#include <string>
#include "graphics/graphics_engine.hpp"
#include "ui/ui_manager.hpp"
#include "lua/lua_script_interface.hpp"
#include "network/network_manager.hpp"

class Application {
public:
    Application();
    ~Application();
    
    bool init();
    void run();
    void terminate();
    
    // Getters para acesso global
    static Application& getInstance();
    GraphicsEngine* getGraphicsEngine() { return graphicsEngine.get(); }
    UIManager* getUIManager() { return uiManager.get(); }
    LuaScriptInterface* getLuaInterface() { return luaInterface.get(); }
    NetworkManager* getNetworkManager() { return networkManager.get(); }
    
private:
    bool initGraphics();
    bool initUI();
    bool initLua();
    bool initNetwork();
    
    std::unique_ptr<GraphicsEngine> graphicsEngine;
    std::unique_ptr<UIManager> uiManager;
    std::unique_ptr<LuaScriptInterface> luaInterface;
    std::unique_ptr<NetworkManager> networkManager;
    
    bool running;
    static Application* instance;
};
```

#### **3.2 Implementação da Application**

```cpp
// src/application.cpp
#include "application.hpp"
#include <iostream>
#include <chrono>
#include <thread>

Application* Application::instance = nullptr;

Application::Application() : running(false) {
    instance = this;
    
    graphicsEngine = std::make_unique<GraphicsEngine>();
    uiManager = std::make_unique<UIManager>();
    luaInterface = std::make_unique<LuaScriptInterface>();
    networkManager = std::make_unique<NetworkManager>();
}

Application::~Application() {
    terminate();
    instance = nullptr;
}

Application& Application::getInstance() {
    return *instance;
}

bool Application::init() {
    std::cout << "🚀 Inicializando OTClient Básico..." << std::endl;
    
    // Inicializar gráficos
    if (!initGraphics()) {
        std::cerr << "❌ Erro ao inicializar gráficos" << std::endl;
        return false;
    }
    
    // Inicializar UI
    if (!initUI()) {
        std::cerr << "❌ Erro ao inicializar UI" << std::endl;
        return false;
    }
    
    // Inicializar Lua
    if (!initLua()) {
        std::cerr << "❌ Erro ao inicializar Lua" << std::endl;
        return false;
    }
    
    // Inicializar rede
    if (!initNetwork()) {
        std::cerr << "❌ Erro ao inicializar rede" << std::endl;
        return false;
    }
    
    running = true;
    std::cout << "✅ OTClient inicializado com sucesso!" << std::endl;
    return true;
}

void Application::run() {
    std::cout << "🔄 Executando loop principal..." << std::endl;
    
    const int targetFPS = 60;
    const auto frameTime = std::chrono::microseconds(1000000 / targetFPS);
    
    while (running) {
        auto frameStart = std::chrono::high_resolution_clock::now();
        
        // Processar eventos
        uiManager->pollEvents();
        
        // Atualizar lógica Lua
        luaInterface->update();
        
        // Renderizar cena
        graphicsEngine->clear();
        uiManager->render();
        graphicsEngine->swapBuffers();
        
        // Atualizar rede
        networkManager->update();
        
        // Controle de FPS
        auto frameEnd = std::chrono::high_resolution_clock::now();
        auto elapsed = std::chrono::duration_cast<std::chrono::microseconds>(frameEnd - frameStart);
        
        if (elapsed < frameTime) {
            std::this_thread::sleep_for(frameTime - elapsed);
        }
    }
}

void Application::terminate() {
    if (running) {
        std::cout << "🛑 Finalizando OTClient..." << std::endl;
        
        luaInterface->shutdown();
        uiManager->shutdown();
        networkManager->disconnect();
        graphicsEngine->shutdown();
        
        running = false;
        std::cout << "✅ OTClient finalizado!" << std::endl;
    }
}

bool Application::initGraphics() {
    return graphicsEngine->init();
}

bool Application::initUI() {
    return uiManager->init();
}

bool Application::initLua() {
    return luaInterface->init();
}

bool Application::initNetwork() {
    return networkManager->init();
}
```

### **Passo 4: Sistema de Gráficos**

#### **4.1 Graphics Engine**

```cpp
// src/graphics/graphics_engine.hpp
#pragma once
#include <string>
#include <map>
#include <GLFW/glfw3.h>

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
    void drawSprite(const std::string& texture, int x, int y, int width, int height);
    void drawText(const std::string& text, int x, int y, float scale = 1.0f);
    
    int getWindowWidth() const { return windowWidth; }
    int getWindowHeight() const { return windowHeight; }
    GLFWwindow* getWindow() const { return window; }
    
private:
    bool initOpenGL();
    bool initShaders();
    void setupViewport();
    
    GLFWwindow* window;
    int windowWidth;
    int windowHeight;
    bool initialized;
    
    std::map<std::string, unsigned int> textures;
};
```

#### **4.2 Implementação do Graphics Engine**

```cpp
// src/graphics/graphics_engine.cpp
#include "graphics_engine.hpp"
#include <iostream>
#include <glad/glad.h>

GraphicsEngine::GraphicsEngine() : window(nullptr), windowWidth(1024), windowHeight(768), initialized(false) {}

GraphicsEngine::~GraphicsEngine() {
    shutdown();
}

bool GraphicsEngine::init() {
    std::cout << "🎨 Inicializando sistema de gráficos..." << std::endl;
    
    // Inicializar GLFW
    if (!glfwInit()) {
        std::cerr << "❌ Falha ao inicializar GLFW" << std::endl;
        return false;
    }
    
    // Configurar GLFW
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    
    // Criar janela
    window = glfwCreateWindow(windowWidth, windowHeight, "OTClient Basic", nullptr, nullptr);
    if (!window) {
        std::cerr << "❌ Falha ao criar janela GLFW" << std::endl;
        glfwTerminate();
        return false;
    }
    
    glfwMakeContextCurrent(window);
    
    // Inicializar GLAD
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
        std::cerr << "❌ Falha ao inicializar GLAD" << std::endl;
        return false;
    }
    
    // Configurar viewport
    setupViewport();
    
    // Inicializar shaders
    if (!initShaders()) {
        std::cerr << "❌ Falha ao inicializar shaders" << std::endl;
        return false;
    }
    
    initialized = true;
    std::cout << "✅ Sistema de gráficos inicializado!" << std::endl;
    return true;
}

void GraphicsEngine::shutdown() {
    if (initialized) {
        if (window) {
            glfwDestroyWindow(window);
            window = nullptr;
        }
        glfwTerminate();
        initialized = false;
    }
}

void GraphicsEngine::clear() {
    glClear(GL_COLOR_BUFFER_BIT);
    glClearColor(0.1f, 0.1f, 0.1f, 1.0f);
}

void GraphicsEngine::swapBuffers() {
    glfwSwapBuffers(window);
    glfwPollEvents();
}

void GraphicsEngine::resize(int width, int height) {
    windowWidth = width;
    windowHeight = height;
    setupViewport();
}

void GraphicsEngine::setupViewport() {
    glViewport(0, 0, windowWidth, windowHeight);
}

bool GraphicsEngine::initShaders() {
    // Shader básico para sprites
    const char* vertexShaderSource = R"(
        #version 330 core
        layout (location = 0) in vec3 aPos;
        layout (location = 1) in vec2 aTexCoord;
        
        out vec2 TexCoord;
        
        void main() {
            gl_Position = vec4(aPos, 1.0);
            TexCoord = aTexCoord;
        }
    )";
    
    const char* fragmentShaderSource = R"(
        #version 330 core
        out vec4 FragColor;
        in vec2 TexCoord;
        
        uniform sampler2D texture1;
        
        void main() {
            FragColor = texture(texture1, TexCoord);
        }
    )";
    
    // Compilar shaders (implementação simplificada)
    std::cout << "📝 Shaders básicos carregados" << std::endl;
    return true;
}
```

### **Passo 5: Sistema de UI**

#### **5.1 UI Manager**

```cpp
// src/ui/ui_manager.hpp
#pragma once
#include <vector>
#include <memory>
#include <string>
#include "widget.hpp"

class UIManager {
public:
    UIManager();
    ~UIManager();
    
    bool init();
    void shutdown();
    void pollEvents();
    void render();
    
    void addWidget(std::shared_ptr<Widget> widget);
    void removeWidget(std::shared_ptr<Widget> widget);
    
    std::shared_ptr<Widget> createButton(const std::string& text, int x, int y, int width, int height);
    std::shared_ptr<Widget> createLabel(const std::string& text, int x, int y);
    std::shared_ptr<Widget> createWindow(const std::string& title, int x, int y, int width, int height);
    
private:
    std::vector<std::shared_ptr<Widget>> widgets;
    bool initialized;
};
```

#### **5.2 Widget Base**

```cpp
// src/ui/widget.hpp
#pragma once
#include <string>
#include <functional>

class Widget {
public:
    Widget(const std::string& name, int x, int y, int width, int height);
    virtual ~Widget() = default;
    
    virtual void render() = 0;
    virtual void update() = 0;
    virtual bool handleEvent(int eventType, int x, int y);
    
    // Getters e setters
    int getX() const { return x; }
    int getY() const { return y; }
    int getWidth() const { return width; }
    int getHeight() const { return height; }
    std::string getName() const { return name; }
    
    void setPosition(int newX, int newY) { x = newX; y = newY; }
    void setSize(int newWidth, int newHeight) { width = newWidth; height = newHeight; }
    
protected:
    std::string name;
    int x, y, width, height;
    bool visible;
    bool enabled;
};
```

### **Passo 6: Integração Lua**

#### **6.1 Lua Script Interface**

```cpp
// src/lua/lua_script_interface.hpp
#pragma once
#include <lua.hpp>
#include <string>
#include <map>

class LuaScriptInterface {
public:
    LuaScriptInterface();
    ~LuaScriptInterface();
    
    bool init();
    void shutdown();
    void update();
    
    bool loadScript(const std::string& scriptPath);
    bool executeFunction(const std::string& functionName);
    
    // Registro de funções C++ para Lua
    void registerFunctions();
    void registerClasses();
    
private:
    lua_State* L;
    bool initialized;
    
    // Funções auxiliares
    void reportError(const std::string& error);
    bool checkLua(int r);
};
```

#### **6.2 Implementação Lua**

```cpp
// src/lua/lua_script_interface.cpp
#include "lua_script_interface.hpp"
#include "../application.hpp"
#include <iostream>

LuaScriptInterface::LuaScriptInterface() : L(nullptr), initialized(false) {}

LuaScriptInterface::~LuaScriptInterface() {
    shutdown();
}

bool LuaScriptInterface::init() {
    std::cout << "📜 Inicializando interface Lua..." << std::endl;
    
    L = luaL_newstate();
    if (!L) {
        std::cerr << "❌ Falha ao criar estado Lua" << std::endl;
        return false;
    }
    
    luaL_openlibs(L);
    
    // Registrar funções C++
    registerFunctions();
    registerClasses();
    
    initialized = true;
    std::cout << "✅ Interface Lua inicializada!" << std::endl;
    return true;
}

void LuaScriptInterface::shutdown() {
    if (initialized && L) {
        lua_close(L);
        L = nullptr;
        initialized = false;
    }
}

void LuaScriptInterface::update() {
    if (initialized && L) {
        // Executar função de atualização se existir
        lua_getglobal(L, "update");
        if (lua_isfunction(L, -1)) {
            if (lua_pcall(L, 0, 0, 0) != LUA_OK) {
                reportError("Erro ao executar update()");
            }
        }
        lua_pop(L, 1);
    }
}

void LuaScriptInterface::registerFunctions() {
    // Registrar funções básicas
    lua_register(L, "print", [](lua_State* L) -> int {
        const char* message = lua_tostring(L, 1);
        std::cout << "[Lua] " << message << std::endl;
        return 0;
    });
    
    lua_register(L, "getWindowSize", [](lua_State* L) -> int {
        auto& app = Application::getInstance();
        auto graphics = app.getGraphicsEngine();
        
        lua_pushinteger(L, graphics->getWindowWidth());
        lua_pushinteger(L, graphics->getWindowHeight());
        return 2;
    });
}

void LuaScriptInterface::registerClasses() {
    // Registrar classes básicas (simplificado)
    std::cout << "📚 Classes Lua registradas" << std::endl;
}

bool LuaScriptInterface::loadScript(const std::string& scriptPath) {
    if (!initialized) return false;
    
    if (luaL_dofile(L, scriptPath.c_str()) != LUA_OK) {
        reportError("Erro ao carregar script: " + scriptPath);
        return false;
    }
    
    std::cout << "✅ Script carregado: " << scriptPath << std::endl;
    return true;
}

void LuaScriptInterface::reportError(const std::string& error) {
    std::cerr << "❌ [Lua] " << error << std::endl;
    if (L) {
        const char* luaError = lua_tostring(L, -1);
        if (luaError) {
            std::cerr << "   Detalhes: " << luaError << std::endl;
        }
    }
}
```

### **Passo 7: Scripts Lua**

#### **7.1 Script Principal**

```lua
-- scripts/init.lua
local otclient = {}

-- Configurações
otclient.config = {
    title = "OTClient Basic",
    width = 1024,
    height = 768,
    fullscreen = false
}

-- Função de inicialização
function otclient.init()
    print("🎮 Inicializando OTClient Lua...")
    
    -- Carregar módulos
    require("modules.ui")
    require("modules.graphics")
    require("modules.network")
    
    -- Configurar eventos
    otclient.setupEvents()
    
    print("✅ OTClient Lua inicializado!")
end

-- Configurar eventos
function otclient.setupEvents()
    print("🔗 Configurando eventos...")
    
    -- Evento de conexão
    if g_game and g_game.onConnect then
        g_game.onConnect = function()
            print("🌐 Conectado ao servidor!")
        end
    end
    
    -- Evento de desconexão
    if g_game and g_game.onDisconnect then
        g_game.onDisconnect = function()
            print("❌ Desconectado do servidor!")
        end
    end
end

-- Função de atualização
function update()
    -- Atualizar módulos
    if modules and modules.ui then
        modules.ui.update()
    end
    
    if modules and modules.graphics then
        modules.graphics.update()
    end
end

-- Retornar módulo
return otclient
```

#### **7.2 Módulo UI**

```lua
-- scripts/modules/ui.lua
local ui = {}

function ui.init()
    print("🎨 Inicializando módulo UI...")
    
    -- Criar janela principal
    ui.mainWindow = g_ui.createWidget('MainWindow')
    if ui.mainWindow then
        ui.mainWindow:setSize({width = 1024, height = 768})
        ui.mainWindow:setText('OTClient Basic')
    end
    
    -- Criar menu
    ui.createMainMenu()
    
    print("✅ Módulo UI inicializado!")
end

function ui.createMainMenu()
    if not ui.mainWindow then return end
    
    ui.mainMenu = g_ui.createWidget('MainMenu', ui.mainWindow)
    
    -- Botão conectar
    local connectBtn = g_ui.createWidget('Button', ui.mainMenu)
    connectBtn:setText('Conectar')
    connectBtn:setPosition({x = 10, y = 10})
    connectBtn.onClick = function()
        ui.showConnectDialog()
    end
    
    -- Botão configurações
    local settingsBtn = g_ui.createWidget('Button', ui.mainMenu)
    settingsBtn:setText('Configurações')
    settingsBtn:setPosition({x = 10, y = 50})
    settingsBtn.onClick = function()
        ui.showSettings()
    end
    
    -- Botão sair
    local exitBtn = g_ui.createWidget('Button', ui.mainMenu)
    exitBtn:setText('Sair')
    exitBtn:setPosition({x = 10, y = 90})
    exitBtn.onClick = function()
        g_app.exit()
    end
end

function ui.showConnectDialog()
    local dialog = g_ui.createWidget('Dialog')
    dialog:setText('Conectar ao Servidor')
    dialog:setSize({width = 300, height = 200})
    
    -- Campo host
    local hostLabel = g_ui.createWidget('Label', dialog)
    hostLabel:setText('Host:')
    hostLabel:setPosition({x = 10, y = 30})
    
    local hostField = g_ui.createWidget('TextField', dialog)
    hostField:setText('localhost')
    hostField:setPosition({x = 10, y = 50})
    hostField:setSize({width = 200, height = 25})
    
    -- Campo porta
    local portLabel = g_ui.createWidget('Label', dialog)
    portLabel:setText('Porta:')
    portLabel:setPosition({x = 10, y = 80})
    
    local portField = g_ui.createWidget('TextField', dialog)
    portField:setText('7172')
    portField:setPosition({x = 10, y = 100})
    portField:setSize({width = 200, height = 25})
    
    -- Botão conectar
    local connectBtn = g_ui.createWidget('Button', dialog)
    connectBtn:setText('Conectar')
    connectBtn:setPosition({x = 10, y = 140})
    connectBtn.onClick = function()
        local host = hostField:getText()
        local port = tonumber(portField:getText())
        
        if g_game then
            g_game.connect(host, port)
        end
        
        dialog:destroy()
    end
end

function ui.showSettings()
    local dialog = g_ui.createWidget('Dialog')
    dialog:setText('Configurações')
    dialog:setSize({width = 400, height = 300})
    
    -- Configurações de gráficos
    local graphicsGroup = g_ui.createWidget('GroupBox', dialog)
    graphicsGroup:setText('Gráficos')
    graphicsGroup:setPosition({x = 10, y = 10})
    graphicsGroup:setSize({width = 380, height = 100})
    
    local fullscreenCheck = g_ui.createWidget('CheckBox', graphicsGroup)
    fullscreenCheck:setText('Tela Cheia')
    fullscreenCheck:setPosition({x = 10, y = 20})
    
    local vsyncCheck = g_ui.createWidget('CheckBox', graphicsGroup)
    vsyncCheck:setText('VSync')
    vsyncCheck:setPosition({x = 10, y = 50})
end

function ui.update()
    -- Atualizar widgets
    if ui.mainWindow then
        ui.mainWindow:update()
    end
end

return ui
```

### **Passo 8: Compilação e Teste**

#### **8.1 Main Function**

```cpp
// src/main.cpp
#include "application.hpp"
#include <iostream>
#include <exception>

int main() {
    try {
        std::cout << "🎮 OTClient Basic - Iniciando..." << std::endl;
        
        // Criar aplicação
        Application app;
        
        // Inicializar
        if (!app.init()) {
            std::cerr << "❌ Falha na inicialização" << std::endl;
            return EXIT_FAILURE;
        }
        
        // Executar loop principal
        app.run();
        
        // Finalizar
        app.terminate();
        
        std::cout << "✅ OTClient Basic finalizado com sucesso!" << std::endl;
        return EXIT_SUCCESS;
        
    } catch (const std::exception& e) {
        std::cerr << "💥 Erro crítico: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }
}
```

#### **8.2 Compilação**

```bash
# Compilar o projeto
mkdir build
cd build
cmake ..
make

# Executar
./bin/otclient_basic
```

## ✅ Checklist de Conclusão

- [ ] **Ambiente configurado**: Estrutura de diretórios criada
- [ ] **CMake configurado**: Sistema de build funcionando
- [ ] **Application implementada**: Classe principal criada
- [ ] **Graphics Engine**: Sistema de gráficos básico
- [ ] **UI Manager**: Sistema de interface do usuário
- [ ] **Lua Integration**: Scripting Lua integrado
- [ ] **Scripts criados**: Scripts Lua funcionais
- [ ] **Compilação**: Projeto compila sem erros
- [ ] **Execução**: Cliente executa corretamente
- [ ] **Testes**: Funcionalidades básicas testadas

## 🔗 Links Relacionados

- **Conceito**: [[concepts/otclient_introduction|Introdução ao OTClient]]
- **Exemplo Prático**: [[examples/otclient_setup|Configuração Básica do OTClient]]
- **Análise Técnica**: [[habdel/OTCLIENT-021|OTCLIENT-021: Documentação Consolidada]]
- **Módulo Educacional**: [[modules/03_otclient/01_otclient_introduction|Módulo: Introdução ao OTClient]]

## 📚 Recursos Adicionais

- **Tópico OTClient**: [[topics/otclient|Índice OTClient]]
- **Templates**: [[templates/exercise_template|Template de Exercício]]
- **Arquitetura Geral**: [[exercises/build_core_architecture|Construindo a Arquitetura Core]] 