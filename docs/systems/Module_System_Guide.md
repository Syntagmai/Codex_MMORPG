
# Sistema de Módulos OTClient

O OTClient utiliza um sistema modular robusto que permite carregar, gerenciar e estender funcionalidades através de módulos Lua organizados hierarquicamente com controle de dependências e carregamento automático.

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Estrutura de Módulos](#estrutura-de-módulos)
3. [Arquivos .otmod](#arquivos-otmod)
4. [Sistema de Prioridades](#sistema-de-prioridades)
5. [Carregamento de Módulos](#carregamento-de-módulos)
6. [Dependências e Load-Later](#dependências-e-load-later)
7. [Gerenciamento de Módulos](#gerenciamento-de-módulos)
8. [Criando Módulos](#criando-módulos)
9. [Melhores Práticas](#melhores-práticas)
10. [Exemplos Práticos](#exemplos-práticos)

## 🎯 Visão Geral

O sistema modular do OTClient oferece:

- **Carregamento Hierárquico**: Módulos carregam por ordem de prioridade (0-9999)
- **Gestão de Dependências**: Sistema load-later para carregar módulos quando dependências estão prontas
- **Isolamento**: Módulos podem ser sandboxed para segurança
- **Hot Reload**: Capacidade de recarregar módulos durante desenvolvimento
- **Extensibilidade**: Fácil adição de novas funcionalidades

### 🏗️ **Arquitetura do Sistema**

```
init.lua (ponto de entrada)
    ↓
g_modules.discoverModules()     # Descobre todos os módulos
    ↓
g_modules.autoLoadModules()     # Carrega por prioridade
    ↓
Módulos específicos via ensureModuleLoaded()
```

## 📁 Estrutura de Módulos

### 🗂️ **Organização de Diretórios**

```
modules/
├── corelib/               # 0-99: Bibliotecas core
│   ├── corelib.otmod
│   ├── math.lua
│   ├── string.lua
│   └── ui/
├── gamelib/               # 0-99: Classes de jogo
│   ├── gamelib.otmod
│   ├── game.lua
│   └── protocol.lua
├── client/                # 100-499: Módulos do cliente
│   ├── client.otmod
│   └── client.lua
├── client_*/              # 100-499: UI do cliente
├── game_*/                # 500-999: Módulos do jogo
└── mods/                  # 1000-9999: Modificações
```

### 🏷️ **Categorias por Prioridade**

| Prioridade | Categoria | Descrição | Exemplos |
|-----------|-----------|-----------|----------|
| **0-99** | **Core Libraries** | Bibliotecas fundamentais | corelib, gamelib, modulelib |
| **100-499** | **Client Modules** | Interface do cliente | client_*, UI básica |
| **500-999** | **Game Modules** | Funcionalidades do jogo | game_*, jogabilidade |
| **1000-9999** | **Mods** | Modificações e extensões | Customizações, plugins |

## 📄 Arquivos .otmod

Cada módulo possui um arquivo `.otmod` que define suas propriedades e comportamento.

### 🔧 **Estrutura Básica**

```otmod
Module
  name: module_name
  description: Descrição do módulo
  author: Nome do Autor
  website: https://site.com
  version: 1.0
  
  # Configurações de carregamento
  autoload: true
  reloadable: true
  sandboxed: false
  
  # Scripts para carregar
  scripts: [ script1, script2 ]
  
  # Dependências
  dependencies: [ module1, module2 ]
  
  # Módulos para carregar depois
  load-later:
    - dependent_module1
    - dependent_module2
  
  # Callbacks de ciclo de vida
  @onLoad: init()
  @onUnload: terminate()
```

### 📝 **Exemplo Detalhado**

```otmod
Module
  name: game_inventory
  description: Manages player inventory interface
  author: OTClient Team
  website: https://github.com/mehah/otclient
  version: 2.0
  
  # Este módulo pode ser recarregado durante desenvolvimento
  reloadable: true
  
  # Executar em sandbox por segurança
  sandboxed: true
  
  # Scripts principais
  scripts: [ inventory, inventory_slots ]
  
  # Depende destes módulos estarem carregados primeiro
  dependencies: [ gamelib, game_interface ]
  
  # Estes módulos podem usar nossos recursos
  load-later:
    - game_containers
    - game_market
    - game_npctrade
  
  # Função chamada quando módulo carrega
  @onLoad: |
    Inventory.init()
    g_keyboard.bindKeyDown('Ctrl+I', Inventory.toggle)
  
  # Função chamada quando módulo descarrega
  @onUnload: |
    Inventory.terminate()
    g_keyboard.unbindKeyDown('Ctrl+I')
```

## 🔢 Sistema de Prioridades

O carregamento ocorre em fases baseadas na prioridade numérica definida no nome ou configuração.

### 📊 **Fases de Carregamento**

```lua
-- No init.lua

-- Fase 1: Core Libraries (0-99)
g_modules.autoLoadModules(99)
g_modules.ensureModuleLoaded('corelib')     -- Prioridade 0
g_modules.ensureModuleLoaded('gamelib')     -- Prioridade 0
g_modules.ensureModuleLoaded('modulelib')   -- Prioridade 0

-- Fase 2: Preparação (pré-999)
g_modules.autoLoadModules(999)
g_modules.ensureModuleLoaded('game_shaders') -- Pré-carregamento

-- Fase 3: Client Modules (100-499)
g_modules.autoLoadModules(499)
g_modules.ensureModuleLoaded('client')

-- Fase 4: Game Modules (500-999)  
g_modules.autoLoadModules(999)
g_modules.ensureModuleLoaded('game_interface')

-- Fase 5: Mods (1000-9999)
g_modules.autoLoadModules(9999)
g_modules.ensureModuleLoaded('client_mods')
```

### 🎯 **Definindo Prioridades**

```otmod
# Método 1: Via nome do diretório
# modules/100_client_base/     -> Prioridade 100
# modules/500_game_core/       -> Prioridade 500

# Método 2: Via configuração no .otmod
Module
  name: my_module
  priority: 150              # Carrega na prioridade 150
  
# Método 3: Prioridade implícita por categoria
# client_* -> 100-499 automaticamente
# game_*   -> 500-999 automaticamente
```

## 🔄 Carregamento de Módulos

### 🚀 **Processo de Inicialização**

```lua
-- 1. Descoberta de módulos
g_modules.discoverModules()
-- Varre diretórios procurando por arquivos .otmod

-- 2. Carregamento automático por prioridade
g_modules.autoLoadModules(999)
-- Carrega todos os módulos com prioridade <= 999

-- 3. Carregamento específico
g_modules.ensureModuleLoaded('module_name')
-- Força o carregamento de um módulo específico

-- 4. Verificação de dependências
-- Automaticamente carrega dependências necessárias
```

### 🔍 **Estados de Módulo**

```lua
-- Verificar estado de um módulo
local module = g_modules.getModule('game_inventory')

if module then
    print('Estado:', module:isLoaded())      -- true/false
    print('Sandbox:', module:isSandboxed()) -- true/false
    print('Reloadable:', module:isReloadable()) -- true/false
    print('Autor:', module:getAuthor())
    print('Versão:', module:getVersion())
end

-- Listar todos os módulos
local allModules = g_modules.getModules()
for _, mod in ipairs(allModules) do
    print(mod:getName(), mod:isLoaded())
end
```

## 🔗 Dependências e Load-Later

### 📦 **Sistema de Dependências**

```otmod
# Módulo que depende de outros
Module
  name: game_containers
  dependencies: [ gamelib, game_interface, game_inventory ]
  
  @onLoad: |
    -- Quando este módulo carregar, as dependências já estarão disponíveis
    if not Inventory then
        error('Inventory dependency not loaded!')
    end
    Containers.init()
```

### ⏱️ **Load-Later (Carregamento Tardio)**

```otmod
# Módulo principal
Module
  name: game_interface
  
  load-later:
    - game_inventory      # Carregará após game_interface
    - game_minimap        # Carregará após game_interface
    - game_skills         # Carregará após game_interface
  
  @onLoad: |
    GameInterface.init()
    -- Neste ponto, módulos load-later ainda NÃO estão carregados
    
    -- Callback para quando load-later completar
    GameInterface.onAllModulesLoaded = function()
        print('Todos os módulos dependentes carregados!')
        -- Agora Inventory, Minimap, Skills estão disponíveis
    end
```

### 🎯 **Carregamento Condicional**

```lua
-- Carregar módulo apenas se condição for atendida
local function loadOptionalModules()
    -- Só carrega se o jogo suporta versão 13+
    if g_game.getClientVersion() >= 1300 then
        g_modules.ensureModuleLoaded('game_cyclopedia')
        g_modules.ensureModuleLoaded('game_store')
    end
    
    -- Só carrega se configuração permitir
    if g_settings.getBoolean('enableAdvancedFeatures') then
        g_modules.ensureModuleLoaded('game_advanced_ui')
    end
end
```

## 🛠️ Gerenciamento de Módulos

### 🔄 **Hot Reload durante Desenvolvimento**

```lua
-- Habilitar auto-reload (apenas desenvolvimento)
g_modules.enableAutoReload()

-- Recarregar módulo específico
g_modules.reloadModule('game_inventory')

-- Descarregar módulo
g_modules.unloadModule('game_inventory')

-- Carregar módulo
g_modules.loadModule('game_inventory')
```

### 📊 **Informações de Debug**

```lua
-- Função de debug para módulos
local function debugModules()
    print('=== STATUS DOS MÓDULOS ===')
    
    local modules = g_modules.getModules()
    table.sort(modules, function(a, b) 
        return a:getName() < b:getName() 
    end)
    
    for _, module in ipairs(modules) do
        local status = module:isLoaded() and 'LOADED' or 'NOT_LOADED'
        local sandbox = module:isSandboxed() and '[SANDBOX]' or ''
        local reloadable = module:isReloadable() and '[RELOADABLE]' or ''
        
        print(string.format('%s: %s %s %s', 
            module:getName(), status, sandbox, reloadable))
    end
end

-- Usar durante desenvolvimento
debugModules()
```

### 🔧 **Utilitários de Módulo**

```lua
-- ModuleManager - Classe helper
local ModuleManager = {}

function ModuleManager.waitForModule(moduleName, callback, timeout)
    timeout = timeout or 5000  -- 5 segundos
    
    local startTime = g_clock.millis()
    
    local function check()
        if g_modules.getModule(moduleName) and 
           g_modules.getModule(moduleName):isLoaded() then
            callback()
        elseif g_clock.millis() - startTime < timeout then
            scheduleEvent(check, 100)  -- Verificar a cada 100ms
        else
            error('Timeout waiting for module: ' .. moduleName)
        end
    end
    
    check()
end

-- Uso
ModuleManager.waitForModule('game_inventory', function()
    print('Inventory carregado, pode usar!')
    Inventory.open()
end)
```

## 🏗️ Criando Módulos

### 📝 **Módulo Básico**

```lua
-- modules/my_custom_module/my_custom_module.otmod
Module
  name: my_custom_module
  description: Meu módulo personalizado
  author: Meu Nome
  version: 1.0
  reloadable: true
  
  @onLoad: MyModule.init()
  @onUnload: MyModule.terminate()
```

```lua
-- modules/my_custom_module/my_custom_module.lua
MyModule = {}

function MyModule.init()
    print('MyModule inicialized!')
    
    -- Criar UI
    MyModule.window = g_ui.displayUI('my_module_window')
    
    -- Bind teclas
    g_keyboard.bindKeyDown('Ctrl+M', MyModule.toggle)
    
    -- Conectar eventos
    connect(g_game, {
        onGameStart = MyModule.onGameStart,
        onGameEnd = MyModule.onGameEnd
    })
end

function MyModule.terminate()
    print('MyModule terminated!')
    
    -- Cleanup
    if MyModule.window then
        MyModule.window:destroy()
        MyModule.window = nil
    end
    
    -- Unbind teclas
    g_keyboard.unbindKeyDown('Ctrl+M')
    
    -- Desconectar eventos
    disconnect(g_game, {
        onGameStart = MyModule.onGameStart,
        onGameEnd = MyModule.onGameEnd
    })
end

function MyModule.toggle()
    if MyModule.window:isVisible() then
        MyModule.window:hide()
    else
        MyModule.window:show()
    end
end

function MyModule.onGameStart()
    print('Game started, MyModule ready!')
end

function MyModule.onGameEnd()
    print('Game ended, MyModule cleanup!')
end
```

### 🎮 **Módulo de Jogo Avançado**

```lua
-- modules/game_my_feature/game_my_feature.otmod
Module
  name: game_my_feature
  description: Advanced game feature module
  author: Developer
  version: 2.0
  
  dependencies: [ gamelib, game_interface ]
  sandboxed: true
  reloadable: true
  
  load-later:
    - game_inventory
    - game_skills
  
  @onLoad: |
    MyGameFeature.init()
    
    -- Registrar protocolo customizado
    MyGameFeature.registerProtocol()
  
  @onUnload: |
    MyGameFeature.terminate()
    MyGameFeature.unregisterProtocol()
```

```lua
-- modules/game_my_feature/game_my_feature.lua
MyGameFeature = {}

-- Configurações do módulo
MyGameFeature.config = {
    enabled = true,
    autoStart = false,
    debugMode = false
}

function MyGameFeature.init()
    -- Carregar configurações
    MyGameFeature.loadConfig()
    
    -- Criar interface
    MyGameFeature.setupUI()
    
    -- Registrar eventos
    MyGameFeature.registerEvents()
    
    print('MyGameFeature initialized')
end

function MyGameFeature.terminate()
    -- Salvar configurações
    MyGameFeature.saveConfig()
    
    -- Limpar interface
    MyGameFeature.cleanupUI()
    
    -- Desregistrar eventos
    MyGameFeature.unregisterEvents()
    
    print('MyGameFeature terminated')
end

function MyGameFeature.loadConfig()
    local config = g_settings.getNode('MyGameFeature')
    if config then
        MyGameFeature.config = table.merge(MyGameFeature.config, config)
    end
end

function MyGameFeature.saveConfig()
    g_settings.setNode('MyGameFeature', MyGameFeature.config)
end

function MyGameFeature.registerProtocol()
    -- Registrar opcode customizado
    ProtocolGame.registerExtendedOpcode(100, MyGameFeature.onExtendedOpcode)
end

function MyGameFeature.onExtendedOpcode(protocol, opcode, buffer)
    local data = json.decode(buffer)
    
    if data.action == 'update' then
        MyGameFeature.updateData(data.payload)
    elseif data.action == 'notify' then
        MyGameFeature.showNotification(data.message)
    end
end

function MyGameFeature.setupUI()
    MyGameFeature.window = g_ui.loadUI('game_my_feature', modules.game_interface.getRightPanel())
    MyGameFeature.window:hide()
end
```

### 🔌 **Módulo Plugin System**

```lua
-- Sistema de plugins para módulos
local PluginSystem = {}
PluginSystem.plugins = {}

function PluginSystem.registerPlugin(name, plugin)
    PluginSystem.plugins[name] = plugin
    
    if plugin.init then
        plugin.init()
    end
    
    print('Plugin registered:', name)
end

function PluginSystem.getPlugin(name)
    return PluginSystem.plugins[name]
end

function PluginSystem.callPlugins(method, ...)
    for name, plugin in pairs(PluginSystem.plugins) do
        if plugin[method] then
            plugin[method](...)
        end
    end
end

-- Uso em módulos
-- modules/plugin_example/plugin_example.lua
local MyPlugin = {
    name = 'MyPlugin',
    version = '1.0'
}

function MyPlugin.init()
    print('MyPlugin initialized')
end

function MyPlugin.onPlayerLogin()
    print('Player logged in - MyPlugin')
end

function MyPlugin.onPlayerLogout()
    print('Player logged out - MyPlugin')
end

-- Registrar plugin
PluginSystem.registerPlugin('MyPlugin', MyPlugin)
```

## ✅ Melhores Práticas

### 🎯 **Estrutura de Módulo**

```lua
-- ✅ BOM: Estrutura organizada
MyModule = {}

-- Configurações
MyModule.config = {}

-- Estado interno
MyModule.data = {}

-- Funções de ciclo de vida
function MyModule.init() end
function MyModule.terminate() end

-- Funções públicas
function MyModule.publicFunction() end

-- Funções privadas (locais)
local function privateFunction() end
```

### 🔄 **Gerenciamento de Estado**

```lua
-- ✅ BOM: Limpar estado adequadamente
function MyModule.terminate()
    -- 1. Desconectar eventos
    disconnect(g_game, {...})
    
    -- 2. Destruir UI
    if MyModule.window then
        MyModule.window:destroy()
        MyModule.window = nil
    end
    
    -- 3. Cancelar timers/schedules
    if MyModule.timer then
        removeEvent(MyModule.timer)
        MyModule.timer = nil
    end
    
    -- 4. Limpar dados
    MyModule.data = {}
end
```

### 📦 **Dependências**

```lua
-- ✅ BOM: Verificar dependências
function MyModule.init()
    -- Verificar se dependências estão disponíveis
    if not Inventory then
        error('MyModule requires game_inventory to be loaded')
    end
    
    if not g_game.isOnline() then
        -- Aguardar jogo iniciar
        connect(g_game, {onGameStart = MyModule.onGameStart})
        return
    end
    
    MyModule.doInit()
end
```

### 🔧 **Configuração**

```lua
-- ✅ BOM: Sistema de configuração robusto
MyModule.defaultConfig = {
    enabled = true,
    hotkey = 'Ctrl+M',
    position = {x = 100, y = 100}
}

function MyModule.loadConfig()
    local saved = g_settings.getNode('MyModule') or {}
    MyModule.config = table.merge(MyModule.defaultConfig, saved)
end

function MyModule.saveConfig()
    g_settings.setNode('MyModule', MyModule.config)
end
```

### 🐛 **Debug e Logging**

```lua
-- Sistema de debug para módulos
MyModule.debug = false

function MyModule.log(...)
    if MyModule.debug then
        print('[MyModule]', ...)
    end
end

function MyModule.error(msg)
    error('[MyModule] ' .. msg)
end

-- Usar
MyModule.log('Initialized successfully')
MyModule.error('Failed to load configuration')
```

O sistema de módulos do OTClient oferece flexibilidade máxima para criar funcionalidades extensíveis e bem organizadas. Use as práticas recomendadas para manter código limpo e módulos reutilizáveis.

---

<div class="success"> Navegação
> - [Getting_Started_Guide](Getting_Started_Guide.md) - Comece aqui
> - [Module_System_Guide](Module_System_Guide.md) - Desenvolvimento de módulos
> - [UI_System_Guide](UI_System_Guide.md) - Interface do usuário
> - [Lua_API_Reference](Lua_API_Reference.md) - Referência completa da API

