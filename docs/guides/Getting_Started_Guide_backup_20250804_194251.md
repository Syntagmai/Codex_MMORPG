---
title: Gettingstarted
tags: [otclient, system, guide, documentation]
status: completed
aliases: [Gettingstarted]
---

# Getting Started - OTClient Redemption

Bem-vindo ao OTClient - Redemption! Este guia te ajudará a dar os primeiros passos no desenvolvimento e customização do cliente Tibia mais avançado e flexível disponível.

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Instalação e Setup](#instalação-e-setup)
3. [Primeira Execução](#primeira-execução)
4. [Estrutura do Projeto](#estrutura-do-projeto)
5. [Conceitos Fundamentais](#conceitos-fundamentais)
6. [Primeiro Módulo](#primeiro-módulo)
7. [Customização Básica](#customização-básica)
8. [Desenvolvimento Local](#desenvolvimento-local)
9. [Debugging e Ferramentas](#debugging-e-ferramentas)
10. [Próximos Passos](#próximos-passos)

## 🎯 Visão Geral

### 🚀 **O que é o OTClient - Redemption?**

O OTClient - Redemption é um cliente Tibia alternativo de código aberto que oferece:

- **Flexibilidade Total**: Sistema modular baseado em Lua
- **Performance Moderna**: C++20 com multi-threading e otimizações avançadas
- **Compatibilidade**: Suporte para protocolos 7.72 até 14.12
- **Extensibilidade**: Sistema de módulos, shaders, efeitos e muito mais
- **Multiplataforma**: Windows, Linux, macOS e Android

### 🏗️ **Arquitetura do Sistema**

```
OTClient - Redemption
   │
   ├─ Engine C++ (Core)
   │   ├─ Graphics (OpenGL)
   │   ├─ Audio (OpenAL)  
   │   ├─ Network (Asio)
   │   └─ Lua Engine (LuaJIT)
   │
   ├─ Framework Lua
   │   ├─ CoreLib (utilitários)
   │   ├─ GameLib (APIs do jogo)
   │   └─ ModuleLib (sistema de módulos)
   │
   └─ Módulos de Jogo
       ├─ Interface (UI)
       ├─ Game Logic (regras)
       └─ Extensions (customizações)
```

## 🛠️ Instalação e Setup

### 📥 **Download e Pré-Requisitos**

```bash
# Clone do repositório
git clone https://github.com/mehah/otclient.git
cd otclient

# Dependências necessárias (já incluídas via vcpkg):
# - LuaJIT 2.1
# - OpenGL 2.0+
# - OpenAL
# - Asio
# - PhysFS
# - Protobuf
```

### 🔧 **Compilação (Apenas se Necessário)**

⚠️ **IMPORTANTE**: A compilação só é necessária se você modificar código C++ ou dependências.

```bash
# Linux/macOS - Build rápido
./recompile.sh

# Windows - Build manual
cmake --preset windows-release
cmake --build --preset windows-release

# Verificar se a compilação foi bem-sucedida
./otclient --version
```

### 📁 **Estrutura de Arquivos**

```
OTClient/
├── src/                    # Código fonte C++ (não modificar frequentemente)
├── data/                   # Dados do cliente
│   ├── images/            # Sprites e texturas
│   ├── sounds/            # Arquivos de áudio
│   ├── fonts/             # Fontes personalizadas
│   └── setup.otml         # Configuração principal
├── modules/               # Módulos Lua (principal área de desenvolvimento)
│   ├── corelib/          # Biblioteca fundamental
│   ├─ gamelib/           # APIs do jogo
│   ├── client_*/         # Módulos do cliente
│   └── game_*/           # Módulos do jogo
├── init.lua              # Arquivo de inicialização
└── CLAUDE.md             # Documentação para desenvolvimento
```

## 🚀 Primeira Execução

### 🎮 **Executando o Cliente**

```bash
# Executar o OTClient
./otclient

# Com parâmetros específicos
./otclient --data-dir=./data --config=custom.otml

# Modo debug
./otclient --debug --verbose
```

### 🔧 **Configuração Inicial**

1. **Configurar Servidor**:
#### Nível Basic
```lua
-- Em init.lua, configurar servidores padrão
Servers_init = {
    ["http://127.0.0.1/login.php"] = {
        ["port"] = 80,
        ["protocol"] = 1412,
        ["httpLogin"] = true
    },
    ["otserver.com"] = {
        ["port"] = 7171,
        ["protocol"] = 1098,
        ["httpLogin"] = false
    }
}
```

#### Nível Intermediate
```lua
-- Em init.lua, configurar servidores padrão
Servers_init = {
    ["http://127.0.0.1/login.php"] = {
        ["port"] = 80,
        ["protocol"] = 1412,
        ["httpLogin"] = true
    },
    ["otserver.com"] = {
        ["port"] = 7171,
        ["protocol"] = 1098,
        ["httpLogin"] = false
    }
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
```lua
-- Em init.lua, configurar servidores padrão
Servers_init = {
    ["http://127.0.0.1/login.php"] = {
        ["port"] = 80,
        ["protocol"] = 1412,
        ["httpLogin"] = true
    },
    ["otserver.com"] = {
        ["port"] = 7171,
        ["protocol"] = 1098,
        ["httpLogin"] = false
    }
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

2. **Configurar Resolução**:
```lua
-- Em modules/startup/startup.lua
    --  Em modules/startup/startup.lua (traduzido)
local size = { width = 1920, height = 1080 }  -- Sua resolução preferida
g_window.resize(size)
```

3. **Configurar Opções Gráficas**:
#### Nível Basic
```lua
-- Acessível via interface ou g_settings
g_settings.set('graphics.fullscreen', false)
g_settings.set('graphics.vsync', true)
g_settings.set('graphics.antialiasing', '2x')
```

#### Nível Intermediate
```lua
-- Acessível via interface ou g_settings
g_settings.set('graphics.fullscreen', false)
g_settings.set('graphics.vsync', true)
g_settings.set('graphics.antialiasing', '2x')
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```lua
-- Acessível via interface ou g_settings
g_settings.set('graphics.fullscreen', false)
g_settings.set('graphics.vsync', true)
g_settings.set('graphics.antialiasing', '2x')
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

## 📂 Estrutura do Projeto

### 🧩 **Sistema de Módulos**

Cada funcionalidade é um módulo independente:

```
modules/game_interface/         # Módulo de interface
├── interface.otmod            # Metadados do módulo
├── gameinterface.lua          # Lógica principal
├── gameinterface.otui         # Layout da interface
└── styles/                    # Estilos adicionais
    └── countwindow.otui
```

### 📄 **Arquivo .otmod (Metadados)**

```yaml
# game_interface/interface.otmod
Module
  name: game_interface
  description: Gerencia a interface principal do jogo
  author: OTClient Team
  website: https://github.com/mehah/otclient
  version: 1.0
  autoload: true
  autoload-priority: 1000
  
  dependencies:
    - game_battle
    - game_inventory
    - game_minimap
  
  load-later:
    - game_hotkeys
```

### 🎨 **Arquivo .otui (Interface)**

```yaml
# gameinterface.otui
MainInterface < Interface
  id: gameInterface
  anchors.fill: parent
  
  UIGameMap
    id: gameMapPanel
    anchors.left: parent.left
    anchors.top: parent.top
    anchors.bottom: bottomPanel.top
    anchors.right: rightPanel.left
    
  Panel
    id: rightPanel
    anchors.top: parent.top
    anchors.right: parent.right
    anchors.bottom: bottomPanel.top
    width: 200
    
    UIInventory
      id: inventoryPanel
      anchors.top: parent.top
      anchors.left: parent.left
      anchors.right: parent.right
      height: 180
```

### 💻 **Arquivo .lua (Lógica)**

```lua
-- gameinterface.lua
    --  gameinterface.lua (traduzido)
gameInterface = {}

local gameRootPanel
local gameMapPanel
local gameRightPanel

function gameInterface.init()
    -- Função: gameInterface
    connect(g_game, { 
        onGameStart = gameInterface.show,
        onGameEnd = gameInterface.hide 
    })
    
    gameRootPanel = g_ui.displayUI('gameinterface')
    gameMapPanel = gameRootPanel:getChildById('gameMapPanel')
    gameRightPanel = gameRootPanel:getChildById('rightPanel')
    
    gameRootPanel:hide()
end

function gameInterface.terminate()
    -- Função: gameInterface
    disconnect(g_game, { 
        onGameStart = gameInterface.show,
        onGameEnd = gameInterface.hide 
    })
    
    gameRootPanel:destroy()
end

function gameInterface.show()
    -- Função: gameInterface
    gameRootPanel:show()
    gameRootPanel:focus()
    gameMapPanel:followCreature(g_game.getLocalPlayer())
end

function gameInterface.hide()
    -- Função: gameInterface
    gameRootPanel:hide()
end
```

## 🔧 Conceitos Fundamentais

### 🎛️ **Sistema de Eventos**

```lua
-- Conectar a eventos globais
    --  Conectar a eventos globais (traduzido)
connect(g_game, {
    onGameStart = function()
        print("Jogo iniciado!")
    end,
    onCreatureAppear = function(creature)
        print("Criatura apareceu:", creature:getName())
    end,
    onTextMessage = function(mode, text)
        print("Mensagem:", text)
    end
})

-- Eventos de UI
    --  Eventos de UI (traduzido)
local button = g_ui.getRootWidget():getChildById('myButton')
button.onClick = function(widget)
    print("Botão clicado!")
end
```

### 🔗 **Links Automáticos**

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

## 🔗 **APIs Principais**

```lua
-- API do Jogo
    --  API do Jogo (traduzido)
local player = g_game.getLocalPlayer()
local position = player:getPosition()
local health = player:getHealth()

-- API do Mapa
    --  API do Mapa (traduzido)
local tile = g_map.getTile(position)
local creatures = g_map.getSpectators(position, false)

-- API de UI
    --  API de UI (traduzido)
local rootWidget = g_ui.getRootWidget()
local window = g_ui.createWidget('MainWindow', rootWidget)

-- API de Configuração
g_settings.set('my.setting', 'value')
local value = g_settings.getString('my.setting')

-- API de Recursos
    --  API de Recursos (traduzido)
local image = g_textures.getTexture('/images/myimage.png')
local sound = g_sounds.getSound('/sounds/mysound.ogg')
```

### 📦 **Gerenciamento de Recursos**

```lua
-- Carregar imagem
    --  Carregar imagem (traduzido)
local texture = g_textures.getTexture('/images/icons/sword.png')

-- Tocar som
    --  Tocar som (traduzido)
g_sounds.playSoundFile('/sounds/effects/sword_hit.ogg')

-- Ler arquivo
    --  Ler arquivo (traduzido)
local content = g_resources.readFileContents('/data/myfile.txt')

-- Verificar existência
if g_resources.fileExists('/images/custom.png') then
    -- Verificação condicional
    -- arquivo existe
    --  arquivo existe (traduzido)
end
```

## 🎨 Primeiro Módulo

### 📝 **Criando um Módulo Simples**

Vamos criar um módulo "Hello World":

1. **Criar diretório**:
```bash
mkdir modules/tutorial_helloworld
```

2. **Criar arquivo .otmod**:
```yaml
# modules/tutorial_helloworld/helloworld.otmod
Module
  name: tutorial_helloworld  
  description: Primeiro módulo tutorial
  author: Seu Nome
  version: 1.0
  autoload: true
  autoload-priority: 100
```

3. **Criar interface .otui**:
```yaml
# modules/tutorial_helloworld/helloworld.otui
HelloWorldWindow < MainWindow
  id: helloWorldWindow
  !text: tr('Hello World')
  size: 300 200
  @onEscape: HelloWorld.hide()
  
  Label
    id: messageLabel
    !text: tr('Olá, OTClient!')
    text-align: center
    anchors.centerIn: parent
    
  Button
    id: closeButton
    !text: tr('Fechar')
    size: 80 24
    anchors.bottom: parent.bottom
    anchors.right: parent.right
    margin-right: 10
    margin-bottom: 10
    @onClick: HelloWorld.hide()
```

4. **Criar lógica .lua**:
```lua
-- modules/tutorial_helloworld/helloworld.lua
    --  modules/tutorial_helloworld/helloworld.lua (traduzido)
HelloWorld = {}

local helloWorldWindow

function HelloWorld.init()
    -- Função: HelloWorld
    -- Carregar interface
    --  Carregar interface (traduzido)
    helloWorldWindow = g_ui.loadUI('helloworld', rootWidget)
    helloWorldWindow:hide()
    
    -- Adicionar botão no menu superior
    local topMenu = modules.client_topmenu.getTopMenu()
    local button = topMenu:addLeftButton('helloWorldButton', 
        tr('Hello World'), '/images/topbuttons/logout')
    button.onClick = HelloWorld.toggle
    
    print("Módulo Hello World carregado!")
end

function HelloWorld.terminate()
    -- Função: HelloWorld
    helloWorldWindow:destroy()
    print("Módulo Hello World finalizado!")
end

function HelloWorld.show()
    -- Função: HelloWorld
    helloWorldWindow:show()
    helloWorldWindow:raise()
    helloWorldWindow:focus()
end

function HelloWorld.hide()
    -- Função: HelloWorld
    helloWorldWindow:hide()
end

function HelloWorld.toggle()
    -- Função: HelloWorld
    if helloWorldWindow:isVisible() then
    -- Verificação condicional
        HelloWorld.hide()
    else
        HelloWorld.show()
    end
end
```

5. **Reiniciar o cliente**:
```bash
./otclient
```

Seu módulo será carregado automaticamente e um botão "Hello World" aparecerá no menu superior!

## ⚙️ Customização Básica

### 🎨 **Modificar Aparência**

```lua
-- Alterar tema de cores
    --  Alterar tema de cores (traduzido)
g_ui.setStyleSheet([[
  MainWindow {
    background-color: #2c3e50;
    border: 1px solid #34495e;
  }
  
  Button {
    background-color: #3498db;
    color: white;
    border-radius: 3px;
  }
  
  Button:hover {
    background-color: #2980b9;
  }
]])

-- Customizar fonte
    --  Customizar fonte (traduzido)
local widget = g_ui.createWidget('Label')
widget:setFont('verdana-11px-antialised')
widget:setForegroundColor('#ecf0f1')
```

### 🔊 **Adicionar Sons Customizados**

```lua
-- Tocar som quando conectar
    --  Tocar som quando conectar (traduzido)
connect(g_game, {
    onGameStart = function()
        g_sounds.playSoundFile('/sounds/custom/login.ogg')
    end,
    
    onCreatureAppear = function(creature)
        if creature:isPlayer() then
    -- Verificação condicional
            g_sounds.playSoundFile('/sounds/custom/player_appear.ogg')
        end
    end
})
```

### ⚡ **Adicionar Hotkeys Customizados**

```lua
-- Registrar hotkey personalizada
    --  Registrar hotkey personalizada (traduzido)
g_keyboard.bindKeyDown('Ctrl+H', function()
    HelloWorld.toggle()
end)

-- Hotkey para comando rápido
g_keyboard.bindKeyDown('F9', function()
    local player = g_game.getLocalPlayer()
    if player then
    -- Verificação condicional
        g_game.talk('exura gran')  -- Cura
    end
end)
```

## 🔨 Desenvolvimento Local

### 📁 **Estrutura de Desenvolvimento**

```
Seu Projeto/
├── custom_modules/          # Seus módulos personalizados
│   ├── my_inventory/
│   ├── my_minimap/
│   └── my_ui_theme/
├── custom_data/            # Seus assets personalizados
│   ├── images/
│   ├── sounds/
│   └── configs/
└── development_notes.md    # Suas anotações
```

### 🔄 **Workflow de Desenvolvimento**

#### Nível Basic
```lua
-- 1. Desenvolvimento iterativo
-- Modificar código Lua não requer recompilação
-- Use Ctrl+R para recarregar módulos
-- 2. Debug rápido
function debugInfo(info)
    print("[DEBUG]", os.date(), info)
    -- Adicionar mais logs conforme necessário
end
-- 3. Teste em tempo real
local function testFeature()
    local success, result = pcall(function()
        -- Seu código experimental aqui
    end)
    if success then
        print("Teste passou:", result)
        print("Teste falhou:", result)
    end
end
```

#### Nível Intermediate
```lua
-- 1. Desenvolvimento iterativo
-- Modificar código Lua não requer recompilação
-- Use Ctrl+R para recarregar módulos

-- 2. Debug rápido
function debugInfo(info)
    print("[DEBUG]", os.date(), info)
    -- Adicionar mais logs conforme necessário
end

-- 3. Teste em tempo real
local function testFeature()
        -- Seu código experimental aqui
        return "success"
    end)
    
    if success then
        print("Teste passou:", result)
    else
        print("Teste falhou:", result)
    end
end
```

#### Nível Advanced
```lua
-- 1. Desenvolvimento iterativo
-- Modificar código Lua não requer recompilação
-- Use Ctrl+R para recarregar módulos

-- 2. Debug rápido
function debugInfo(info)
    print("[DEBUG]", os.date(), info)
    -- Adicionar mais logs conforme necessário
end

-- 3. Teste em tempo real
local function testFeature()
    local success, result = pcall(function()
        -- Seu código experimental aqui
        return "success"
    end)
    
    if success then
        print("Teste passou:", result)
    else
        print("Teste falhou:", result)
    end
end
```

### 🔧 **Hot Reload de Módulos**

```lua
-- Função para recarregar módulo específico
function reloadModule(moduleName)
    -- Função: reloadModule
    local module = g_modules.getModule(moduleName)
    if module then
    -- Verificação condicional
        module:unload()
        module:load()
        print("Módulo recarregado:", moduleName)
    end
end

-- Uso:
    --  Uso: (traduzido)
-- reloadModule('tutorial_helloworld')
    --  reloadModule('tutorial_helloworld') (traduzido)
```

## 🐛 Debugging e Ferramentas

### 🔍 **Console Lua Integrado**

#### Nível Basic
```lua
-- Abrir console: Ctrl+T
-- Comandos úteis no console:
-- Listar módulos carregados
for k,v in pairs(g_modules.getModules()) do print(k, v:getName()) end
-- Inspecionar objeto
local player = g_game.getLocalPlayer()
for k,v in pairs(getmetatable(player)) do print(k,v) end
-- Executar função
-- Modificar configuração
```

#### Nível Intermediate
```lua
-- Abrir console: Ctrl+T
-- Comandos úteis no console:

-- Listar módulos carregados
for k,v in pairs(g_modules.getModules()) do print(k, v:getName()) end

-- Inspecionar objeto
local player = g_game.getLocalPlayer()

-- Executar função
HelloWorld.show()

-- Modificar configuração
g_settings.set('debug.enabled', true)
```

#### Nível Advanced
```lua
-- Abrir console: Ctrl+T
-- Comandos úteis no console:

-- Listar módulos carregados
for k,v in pairs(g_modules.getModules()) do print(k, v:getName()) end

-- Inspecionar objeto
local player = g_game.getLocalPlayer()
for k,v in pairs(getmetatable(player)) do print(k,v) end

-- Executar função
HelloWorld.show()

-- Modificar configuração
g_settings.set('debug.enabled', true)
```

### 📊 **Debug de Performance**

```lua
-- Medir tempo de execução
local function measureTime(func, name)
    local startTime = g_clock.millis()
    func()
    local endTime = g_clock.millis()
    print(name .. " levou " .. (endTime - startTime) .. "ms")
end

-- Uso
    --  Uso (traduzido)
measureTime(function()
    -- código a ser medido
    local spectators = g_map.getSpectators(g_game.getLocalPlayer():getPosition(), false)
end, "Get Spectators")

-- Monitor de FPS
    --  Monitor de FPS (traduzido)
local function showFPS()
    local fpsLabel = g_ui.getRootWidget():getChildById('fpsLabel')
    if not fpsLabel then
    -- Verificação condicional
        fpsLabel = g_ui.createWidget('Label', g_ui.getRootWidget())
        fpsLabel:setId('fpsLabel')
        fpsLabel:setPosition({x = 10, y = 10})
        fpsLabel:setForegroundColor('#00ff00')
    end
    
    scheduleEvent(function()
        fpsLabel:setText('FPS: ' .. g_app.getFps())
        showFPS()  -- Repetir
    end, 1000)
end
```

### 🔧 **Ferramentas de Desenvolvimento**

#### Nível Basic
```lua
-- 1. Inspector de UI (módulo game_ui_inspector)
-- Permite inspecionar hierarquia de widgets em tempo real
-- 2. Terminal Lua avançado
-- Histórico de comandos, autocomplete
-- 3. Monitor de recursos
function showResourceUsage()
    print("Texturas carregadas:", g_textures.getLoadedTextureCount())
    print("Memória Lua:", collectgarbage("count") .. "KB")
    print("Uptime:", g_clock.seconds() .. "s")
end
-- 4. Log customizado
local function setupCustomLogging()
    local logFile = io.open("debug.log", "a")
    local originalPrint = print
    print = function(...)
        local args = {...}
        local line = table.concat(args, "\t")
        if logFile then
        end
    end
end
```

#### Nível Intermediate
```lua
-- 1. Inspector de UI (módulo game_ui_inspector)
-- Permite inspecionar hierarquia de widgets em tempo real

-- 2. Terminal Lua avançado
-- Histórico de comandos, autocomplete

-- 3. Monitor de recursos
function showResourceUsage()
    print("Texturas carregadas:", g_textures.getLoadedTextureCount())
    print("Memória Lua:", collectgarbage("count") .. "KB")
    print("Uptime:", g_clock.seconds() .. "s")
end

-- 4. Log customizado
local function setupCustomLogging()
    local logFile = io.open("debug.log", "a")
    
    local originalPrint = print
    print = function(...)
        local args = {...}
        local line = table.concat(args, "\t")
        originalPrint(line)
        
        if logFile then
            logFile:write(os.date() .. "\t" .. line .. "\n")
            logFile:flush()
        end
    end
end
```

#### Nível Advanced
```lua
-- 1. Inspector de UI (módulo game_ui_inspector)
-- Permite inspecionar hierarquia de widgets em tempo real

-- 2. Terminal Lua avançado
-- Histórico de comandos, autocomplete

-- 3. Monitor de recursos
function showResourceUsage()
    print("Texturas carregadas:", g_textures.getLoadedTextureCount())
    print("Memória Lua:", collectgarbage("count") .. "KB")
    print("Uptime:", g_clock.seconds() .. "s")
end

-- 4. Log customizado
local function setupCustomLogging()
    local logFile = io.open("debug.log", "a")
    
    local originalPrint = print
    print = function(...)
        local args = {...}
        local line = table.concat(args, "\t")
        originalPrint(line)
        
        if logFile then
            logFile:write(os.date() .. "\t" .. line .. "\n")
            logFile:flush()
        end
    end
end
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

## 🚀 Próximos Passos

### 📚 **Documentação Recomendada**

1. **[Sistema de Módulos](ModuleSystem.md)** - Entenda como criar módulos avançados
2. **[Sistema de Configuração](Configuration.md)** - Aprenda sobre configs e settings
3. **[UIWidget Reference](UIWidget_Reference.md)** - Guia completo de widgets
4. **[Protocolo de Comunicação](Protocol.md)** - Como funciona a rede
5. **[Sistema de Mundo e Mapas](WorldSystem.md)** - Manipulação de mapas e tiles

### 🎯 **Projetos Sugeridos para Iniciantes**

1. **Modificador de Interface**:
   - Alterar cores e layout
   - Adicionar botões customizados
   - Criar janelas personalizadas

2. **Sistema de Notificações**:
   - Notificações de eventos do jogo
   - Sistema de alertas
   - Log de atividades

3. **Automação Básica**:
   - Hotkeys para ações comuns
   - Macros simples
   - Shortcuts de navegação

4. **Customização Visual**:
   - Temas personalizados
   - Efeitos visuais
   - Animações customizadas

### 🌟 **Recursos da Comunidade**

- **Discord**: [Comunidade OTClient](https://discord.gg/tUjTBZzMCy)
- **GitHub**: [Repositório Principal](https://github.com/mehah/otclient)
- **Wiki**: Documentação detalhada e exemplos
- **Fórum**: Discussões e suporte técnico

### 🔄 **Fluxo de Contribuição**

```bash
# 1. Fork do repositório
git fork https://github.com/mehah/otclient

# 2. Criar branch para sua feature
git checkout -b feature/minha-feature

# 3. Desenvolver e testar
# ... fazer modificações ...

# 4. Commit das mudanças
git add .
git commit -m "Adicionar nova feature: descrição"

# 5. Push e pull request
git push origin feature/minha-feature
# Criar PR no GitHub
```

Parabéns! 🎉 Você agora tem uma base sólida para começar a desenvolver com o OTClient - Redemption. Lembre-se: a maior parte do desenvolvimento envolve scripting Lua, que não requer recompilação. Explore, experimente e divirta-se criando!

---

> [!success] Navegação
> - [[Getting_Started_Guide]] - Comece aqui
> - [[Module_System_Guide]] - Desenvolvimento de módulos
> - [[UI_System_Guide]] - Interface do usuário
> - [[Lua_API_Reference]] - Referência completa da API

