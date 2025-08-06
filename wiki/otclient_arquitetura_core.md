---
tags: [otclient, arquitetura_core, fundamentos, habdel_research]
type: wiki_page
status: active
priority: high
created: 2025-08-05
updated: 2025-08-05
aliases: [arquitetura_otclient, core_otclient, estrutura_otclient]
level: intermediate
category: fundamentos
dependencies: [wikipedia_canary_otclient, guia_navegacao]
related: [otclient_sistema_modulos, otclient_sistema_rede, otclient_sistema_ui, otclient_sistema_graficos]
---

# 🏗️ **Arquitetura Core do OTClient**

> [!info] **Baseado no Código-Fonte Real**
> Esta página é baseada na análise direta do código-fonte do OTClient, especificamente os arquivos em `otclient/src/` e `otclient/modules/`.

## 📋 **Visão Geral**

O **OTClient** é o cliente oficial do Open Tibia, responsável por renderizar o jogo, gerenciar a interface do usuário e comunicar-se com o servidor. Sua arquitetura é modular e extensível, permitindo personalizações através de módulos Lua.

### **🎯 Objetivos da Arquitetura**
- **Modularidade**: Sistema de módulos independentes
- **Extensibilidade**: APIs Lua para customização
- **Performance**: Renderização otimizada em C++
- **Compatibilidade**: Suporte a diferentes protocolos

---

## 📁 **Estrutura de Arquivos**

```
otclient/
├── src/                    # Código-fonte C++ principal
│   ├── main.cpp           # Ponto de entrada da aplicação
│   ├── framework/         # Framework core do cliente
│   │   ├── core/          # Sistema core (inicialização, configuração)
│   │   ├── graphics/      # Sistema de renderização
│   │   ├── ui/            # Sistema de interface
│   │   ├── net/           # Sistema de rede
│   │   ├── sound/         # Sistema de áudio
│   │   ├── luaengine/     # Motor Lua
│   │   └── util/          # Utilitários
│   └── client/            # Lógica específica do cliente
├── modules/               # Módulos Lua do sistema
│   ├── corelib/           # Biblioteca core Lua
│   ├── gamelib/           # Biblioteca de jogo Lua
│   ├── client/            # Módulos do cliente
│   └── game_*/            # Módulos de funcionalidades do jogo
├── data/                  # Dados do cliente
└── init.lua               # Script de inicialização Lua
```

---

## 🔧 **Componentes Principais**

### **1. Sistema Core (framework/core/)**
```cpp
// Exemplo de inicialização do sistema core
class Application {
public:
    void init();
    void run();
    void terminate();
    
private:
    GraphicsEngine* m_graphics;
    NetworkManager* m_network;
    LuaEngine* m_lua;
    UIManager* m_ui;
};
```

**Responsabilidades**:
- Inicialização e configuração do sistema
- Gerenciamento do ciclo de vida da aplicação
- Coordenação entre subsistemas

### **2. Sistema de Gráficos (framework/graphics/)**
```cpp
// Exemplo de renderização
class GraphicsEngine {
public:
    void beginFrame();
    void drawSprite(const SpritePtr& sprite, const Point& pos);
    void drawText(const std::string& text, const Point& pos);
    void endFrame();
    
private:
    Renderer* m_renderer;
    TextureManager* m_textures;
};
```

**Responsabilidades**:
- Renderização 2D de sprites e texto
- Gerenciamento de texturas
- Otimização de performance gráfica

### **3. Sistema de UI (framework/ui/)**
```cpp
// Exemplo de widget UI
class Widget {
public:
    virtual void draw() = 0;
    virtual void update() = 0;
    virtual void onMousePress(const Point& pos, MouseButton button);
    
protected:
    Rect m_rect;
    bool m_visible;
    bool m_enabled;
};
```

**Responsabilidades**:
- Sistema de widgets e layouts
- Gerenciamento de eventos de interface
- Renderização de elementos UI

### **4. Sistema de Rede (framework/net/)**
```cpp
// Exemplo de conexão de rede
class Connection {
public:
    void connect(const std::string& host, uint16_t port);
    void send(const OutputMessage& msg);
    void recv();
    
private:
    Socket* m_socket;
    Protocol* m_protocol;
};
```

**Responsabilidades**:
- Comunicação com o servidor
- Implementação do protocolo Open Tibia
- Gerenciamento de conexões

### **5. Motor Lua (framework/luaengine/)**
```cpp
// Exemplo de integração Lua
class LuaEngine {
public:
    void init();
    void loadScript(const std::string& path);
    void callFunction(const std::string& name, ...);
    
private:
    lua_State* m_state;
    std::vector<std::string> m_scripts;
};
```

**Responsabilidades**:
- Execução de scripts Lua
- APIs para módulos
- Integração com sistemas C++

---

## 🔌 **APIs e Interfaces**

### **APIs Lua Principais**
```lua
-- Exemplo de API Lua para módulos
g_ui = require('ui')           -- Sistema de interface
g_graphics = require('graphics') -- Sistema de gráficos
g_network = require('network')   -- Sistema de rede
g_sound = require('sound')       -- Sistema de áudio

-- Exemplo de criação de módulo
function init()
    -- Inicialização do módulo
end

function terminate()
    -- Finalização do módulo
end
```

### **APIs C++ para Lua**
```cpp
// Exemplo de binding C++ para Lua
void bindGraphics(lua_State* L) {
    luabridge::getGlobalNamespace(L)
        .beginClass<GraphicsEngine>("Graphics")
            .addFunction("drawSprite", &GraphicsEngine::drawSprite)
            .addFunction("drawText", &GraphicsEngine::drawText)
        .endClass();
}
```

---

## 🔄 **Fluxo de Dados**

### **1. Inicialização**
```
main.cpp → Application::init() → 
├── GraphicsEngine::init()
├── NetworkManager::init()
├── LuaEngine::init()
└── UIManager::init()
```

### **2. Loop Principal**
```
Application::run() →
├── NetworkManager::update() → Processa mensagens do servidor
├── LuaEngine::update() → Executa scripts Lua
├── UIManager::update() → Atualiza interface
└── GraphicsEngine::render() → Renderiza frame
```

### **3. Comunicação Cliente-Servidor**
```
Cliente → NetworkManager → Protocol → Socket → Servidor
Servidor → Socket → Protocol → NetworkManager → Cliente
```

---

## 💡 **Exemplos Práticos**

### **Nível Básico: Criando um Módulo Simples**
```lua
-- modules/exemplo_basico/init.lua
function init()
    print("Módulo básico inicializado!")
end

function terminate()
    print("Módulo básico finalizado!")
end
```

### **Nível Intermediário: Módulo com Interface**
```lua
-- modules/exemplo_ui/init.lua
local window

function init()
    -- Cria uma janela simples
    window = g_ui.createWidget('Window')
    window:setText('Exemplo de Módulo')
    window:setSize({200, 150})
    window:setPosition({100, 100})
    window:show()
end

function terminate()
    if window then
        window:destroy()
    end
end
```

### **Nível Avançado: Módulo com Rede e Gráficos**
```lua
-- modules/exemplo_avancado/init.lua
local connection
local sprite

function init()
    -- Conecta ao servidor
    connection = g_network.createConnection()
    connection:connect('localhost', 7172)
    
    -- Carrega sprite
    sprite = g_graphics.createSprite('custom_sprite.png')
    
    -- Registra callbacks
    connection:onConnect(function()
        print("Conectado ao servidor!")
    end)
end

function terminate()
    if connection then
        connection:disconnect()
    end
    if sprite then
        sprite:destroy()
    end
end
```

---

## 🎓 **Lições Educacionais**

### **Conceitos Fundamentais**
1. **Arquitetura Modular**: Separação clara de responsabilidades
2. **Integração C++/Lua**: Combinação de performance e flexibilidade
3. **Sistema de Eventos**: Comunicação assíncrona entre componentes
4. **Gerenciamento de Recursos**: Alocação e liberação adequada

### **Padrões de Design**
- **Singleton**: Para sistemas globais (Graphics, Network)
- **Observer**: Para sistema de eventos
- **Factory**: Para criação de widgets e sprites
- **Strategy**: Para diferentes protocolos de rede

### **Boas Práticas**
- Sempre inicializar e finalizar módulos corretamente
- Usar APIs Lua para customizações
- Gerenciar recursos adequadamente
- Seguir o padrão de nomenclatura dos módulos

---

## 🔗 **Páginas Relacionadas**

- [[otclient_sistema_modulos|Sistema de Módulos]] - Como criar e gerenciar módulos
- [[otclient_sistema_rede|Sistema de Rede]] - Comunicação com servidor
- [[otclient_sistema_ui|Sistema de UI]] - Interface do usuário
- [[otclient_sistema_graficos|Sistema de Gráficos]] - Renderização
- [[wikipedia_canary_otclient|Wikipedia Canary + OTClient]] - Visão geral do projeto

---

## 📚 **Referências**

- **Código-fonte**: `otclient/src/framework/`
- **Módulos**: `otclient/modules/`
- **Documentação**: `otclient/docs/`
- **Baseado na pesquisa Habdel**: [[../habdel/OTCLIENT-001|OTCLIENT-001: Análise da Arquitetura Core]] 