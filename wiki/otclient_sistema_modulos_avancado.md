---
tags: [otclient, modules, advanced, .otmod, module_system, wiki, canary_otclient]
type: wiki_page
status: active
priority: medium
created: 2025-08-05
updated: 2025-08-05
aliases: [Módulos Avançado OTClient, Sistema de Módulos, .otmod Files]
---

# 📦 **Sistema de Módulos Avançado - OTClient**

> [!info] **Baseado na Pesquisa Habdel**
> Esta página é baseada na pesquisa detalhada da **[OTCLIENT-017: Sistema de Guilds](../../habdel/OTCLIENT-017.md)** realizada pelo sistema Habdel.

---

## 🎯 **Visão Geral**

O **Sistema de Módulos Avançado** do OTClient permite a criação, carregamento e gerenciamento de módulos complexos através de arquivos `.otmod`, oferecendo funcionalidades avançadas como **dependências dinâmicas**, **carregamento condicional**, **hooks de sistema** e **gerenciamento de recursos**.

### **Características Principais**
- **Arquivos .otmod** para definição de módulos
- **Sistema de dependências** automático
- **Carregamento condicional** baseado em contexto
- **Hooks de sistema** para integração
- **Gerenciamento de recursos** automático
- **Hot-reloading** de módulos

---

## 🏗️ **Arquitetura do Sistema**

### **Estrutura de Módulos**
```
📁 otclient/modules/
├── 📁 [module_name]/
│   ├── 📄 init.lua          # Ponto de entrada do módulo
│   ├── 📄 module.otmod      # Definição do módulo
│   ├── 📁 lib/              # Bibliotecas do módulo
│   ├── 📁 resources/        # Recursos (imagens, sons, etc.)
│   ├── 📁 styles/           # Estilos OTUI
│   └── 📁 scripts/          # Scripts Lua
└── 📁 modulelib/            # Sistema de carregamento
```

### **Componentes Principais**

#### **1. Module Loader (modulelib/)**
```lua
-- Sistema principal de carregamento de módulos
local ModuleLoader = {}
ModuleLoader.__index = ModuleLoader

function ModuleLoader.new()
    local loader = {
        loadedModules = {},
        moduleCache = {},
        dependencies = {},
        hooks = {}
    }
    setmetatable(loader, ModuleLoader)
    return loader
end

function ModuleLoader:loadModule(moduleName)
    if self.moduleCache[moduleName] then
        return self.moduleCache[moduleName]
    end
    
    local modulePath = "modules/" .. moduleName
    local otmodFile = modulePath .. "/module.otmod"
    local initFile = modulePath .. "/init.lua"
    
    -- Carregar definição do módulo
    local moduleDef = self:loadOtmodFile(otmodFile)
    
    -- Verificar dependências
    self:checkDependencies(moduleDef.dependencies)
    
    -- Carregar módulo
    local success, module = pcall(dofile, initFile)
    if success then
        self.moduleCache[moduleName] = module
        self.loadedModules[moduleName] = moduleDef
        self:setupHooks(module, moduleDef)
        return module
    else
        error("Failed to load module: " .. moduleName .. " - " .. tostring(module))
    end
end
```

#### **2. Otmod Parser**
```lua
-- Parser para arquivos .otmod
function ModuleLoader:loadOtmodFile(otmodPath)
    local file = io.open(otmodPath, "r")
    if not file then
        error("Otmod file not found: " .. otmodPath)
    end
    
    local content = file:read("*all")
    file:close()
    
    local moduleDef = {
        name = "",
        version = "",
        author = "",
        description = "",
        dependencies = {},
        hooks = {},
        resources = {},
        permissions = {}
    }
    
    -- Parse do conteúdo do arquivo
    for line in content:gmatch("[^\r\n]+") do
        local key, value = line:match("^([^:]+):%s*(.+)$")
        if key and value then
            key = key:trim()
            value = value:trim()
            
            if key == "dependencies" then
                moduleDef.dependencies = self:parseDependencies(value)
            elseif key == "hooks" then
                moduleDef.hooks = self:parseHooks(value)
            elseif key == "resources" then
                moduleDef.resources = self:parseResources(value)
            else
                moduleDef[key] = value
            end
        end
    end
    
    return moduleDef
end
```

---

## 📄 **Arquivos .otmod**

### **Estrutura do Arquivo .otmod**
```ini
# Exemplo de arquivo module.otmod
name: MyAdvancedModule
version: 1.0.0
author: Developer Name
description: Advanced module with custom features

dependencies: corelib, gamelib, ui_framework
hooks: onGameStart, onPlayerLogin, onInventoryChange
resources: images/icons, sounds/effects, styles/custom.otui
permissions: file_access, network_access, ui_modification

# Configurações específicas do módulo
settings:
  debug_mode: false
  auto_reload: true
  cache_enabled: true

# Eventos customizados
events:
  custom_event_1: function_name_1
  custom_event_2: function_name_2
```

### **Campos Principais**

#### **Informações Básicas**
- **name**: Nome único do módulo
- **version**: Versão do módulo (semantic versioning)
- **author**: Autor do módulo
- **description**: Descrição detalhada

#### **Dependências**
```ini
dependencies: corelib, gamelib, ui_framework, database_module
```

#### **Hooks do Sistema**
```ini
hooks: onGameStart, onPlayerLogin, onInventoryChange, onChatMessage
```

#### **Recursos**
```ini
resources: images/icons, sounds/effects, styles/custom.otui, data/config.json
```

---

## 🔗 **Sistema de Dependências**

### **Dependências Simples**
```lua
-- Exemplo: Dependência básica
local function checkSimpleDependency(moduleName)
    if not package.loaded[moduleName] then
        error("Required module not loaded: " .. moduleName)
    end
end
```

### **Dependências com Versão**
```lua
-- Exemplo: Dependência com verificação de versão
function ModuleLoader:checkVersionedDependency(moduleName, requiredVersion)
    local module = package.loaded[moduleName]
    if not module then
        error("Required module not loaded: " .. moduleName)
    end
    
    if module.version then
        if not self:compareVersions(module.version, requiredVersion) then
            error("Module version mismatch: " .. moduleName .. 
                  " (required: " .. requiredVersion .. 
                  ", found: " .. module.version .. ")")
        end
    end
end

function ModuleLoader:compareVersions(v1, v2)
    local function parseVersion(v)
        local major, minor, patch = v:match("(%d+)%.(%d+)%.(%d+)")
        return tonumber(major), tonumber(minor), tonumber(patch)
    end
    
    local major1, minor1, patch1 = parseVersion(v1)
    local major2, minor2, patch2 = parseVersion(v2)
    
    if major1 ~= major2 then return major1 >= major2 end
    if minor1 ~= minor2 then return minor1 >= minor2 end
    return patch1 >= patch2
end
```

### **Dependências Circulares**
```lua
-- Exemplo: Detecção de dependências circulares
function ModuleLoader:detectCircularDependencies(moduleName, visited)
    visited = visited or {}
    
    if visited[moduleName] then
        error("Circular dependency detected: " .. moduleName)
    end
    
    visited[moduleName] = true
    
    local moduleDef = self.loadedModules[moduleName]
    if moduleDef and moduleDef.dependencies then
        for _, dep in ipairs(moduleDef.dependencies) do
            self:detectCircularDependencies(dep, visited)
        end
    end
    
    visited[moduleName] = nil
end
```

---

## 🪝 **Sistema de Hooks**

### **Hooks do Sistema**
```lua
-- Exemplo: Sistema de hooks
local HookSystem = {}
HookSystem.__index = HookSystem

function HookSystem.new()
    local system = {
        hooks = {},
        registeredModules = {}
    }
    setmetatable(system, HookSystem)
    return system
end

function HookSystem:registerHook(hookName, moduleName, callback)
    if not self.hooks[hookName] then
        self.hooks[hookName] = {}
    end
    
    table.insert(self.hooks[hookName], {
        module = moduleName,
        callback = callback
    })
end

function HookSystem:triggerHook(hookName, ...)
    if self.hooks[hookName] then
        for _, hook in ipairs(self.hooks[hookName]) do
            local success, result = pcall(hook.callback, ...)
            if not success then
                print("Hook error in " .. hook.module .. ": " .. tostring(result))
            end
        end
    end
end
```

### **Hooks Comuns**
```lua
-- Exemplos de hooks comuns
local commonHooks = {
    "onGameStart",           -- Quando o jogo inicia
    "onGameEnd",             -- Quando o jogo termina
    "onPlayerLogin",         -- Quando um jogador faz login
    "onPlayerLogout",        -- Quando um jogador faz logout
    "onInventoryChange",     -- Quando o inventário muda
    "onChatMessage",         -- Quando uma mensagem é enviada
    "onCreatureMove",        -- Quando uma criatura se move
    "onCombatStart",         -- Quando um combate inicia
    "onCombatEnd",           -- Quando um combate termina
    "onItemUse",             -- Quando um item é usado
    "onSpellCast",           -- Quando uma magia é lançada
    "onUIEvent"              -- Quando um evento de UI ocorre
}
```

---

## 🔄 **Carregamento Condicional**

### **Carregamento Baseado em Contexto**
```lua
-- Exemplo: Carregamento condicional
function ModuleLoader:loadConditionalModule(moduleName, conditions)
    local shouldLoad = true
    
    for condition, value in pairs(conditions) do
        if condition == "game_version" then
            shouldLoad = shouldLoad and self:checkGameVersion(value)
        elseif condition == "feature_enabled" then
            shouldLoad = shouldLoad and self:isFeatureEnabled(value)
        elseif condition == "user_permission" then
            shouldLoad = shouldLoad and self:hasUserPermission(value)
        elseif condition == "system_requirement" then
            shouldLoad = shouldLoad and self:checkSystemRequirement(value)
        end
    end
    
    if shouldLoad then
        return self:loadModule(moduleName)
    else
        print("Module " .. moduleName .. " not loaded due to conditions")
        return nil
    end
end
```

### **Carregamento Lazy**
```lua
-- Exemplo: Carregamento lazy (sob demanda)
function ModuleLoader:loadLazyModule(moduleName, triggerEvent)
    local lazyModule = {
        name = moduleName,
        loaded = false,
        module = nil
    }
    
    -- Registrar para carregamento quando o evento ocorrer
    self:registerHook(triggerEvent, "lazy_loader", function()
        if not lazyModule.loaded then
            lazyModule.module = self:loadModule(moduleName)
            lazyModule.loaded = true
        end
    end)
    
    return lazyModule
end
```

---

## 🎨 **Gerenciamento de Recursos**

### **Carregamento de Recursos**
```lua
-- Exemplo: Sistema de gerenciamento de recursos
local ResourceManager = {}
ResourceManager.__index = ResourceManager

function ResourceManager.new()
    local manager = {
        resources = {},
        loadedResources = {}
    }
    setmetatable(manager, ResourceManager)
    return manager
end

function ResourceManager:loadResources(moduleName, resourceList)
    for _, resource in ipairs(resourceList) do
        local resourcePath = "modules/" .. moduleName .. "/" .. resource
        local resourceType = self:getResourceType(resource)
        
        if resourceType == "image" then
            self:loadImage(resourcePath)
        elseif resourceType == "sound" then
            self:loadSound(resourcePath)
        elseif resourceType == "style" then
            self:loadStyle(resourcePath)
        elseif resourceType == "data" then
            self:loadData(resourcePath)
        end
    end
end

function ResourceManager:getResourceType(resourcePath)
    local extension = resourcePath:match("%.([^%.]+)$")
    if extension == "png" or extension == "jpg" or extension == "gif" then
        return "image"
    elseif extension == "wav" or extension == "mp3" or extension == "ogg" then
        return "sound"
    elseif extension == "otui" then
        return "style"
    elseif extension == "json" or extension == "lua" then
        return "data"
    else
        return "unknown"
    end
end
```

### **Cache de Recursos**
```lua
-- Exemplo: Sistema de cache de recursos
function ResourceManager:cacheResource(resourcePath, resourceData)
    self.loadedResources[resourcePath] = {
        data = resourceData,
        lastAccess = os.time(),
        accessCount = 0
    }
end

function ResourceManager:getCachedResource(resourcePath)
    local resource = self.loadedResources[resourcePath]
    if resource then
        resource.lastAccess = os.time()
        resource.accessCount = resource.accessCount + 1
        return resource.data
    end
    return nil
end
```

---

## 🔄 **Hot-Reloading**

### **Sistema de Hot-Reload**
```lua
-- Exemplo: Sistema de hot-reload
function ModuleLoader:enableHotReload(moduleName)
    local modulePath = "modules/" .. moduleName
    local lastModified = {}
    
    -- Monitorar arquivos do módulo
    local function checkForChanges()
        local files = self:getModuleFiles(modulePath)
        
        for _, file in ipairs(files) do
            local currentModified = self:getFileModifiedTime(file)
            local lastMod = lastModified[file]
            
            if lastMod and currentModified > lastMod then
                print("File changed: " .. file .. ", reloading module: " .. moduleName)
                self:reloadModule(moduleName)
                break
            end
            
            lastModified[file] = currentModified
        end
    end
    
    -- Iniciar monitoramento
    self:startFileWatcher(modulePath, checkForChanges)
end

function ModuleLoader:reloadModule(moduleName)
    -- Descarregar módulo atual
    self:unloadModule(moduleName)
    
    -- Limpar cache
    collectgarbage("collect")
    
    -- Recarregar módulo
    return self:loadModule(moduleName)
end
```

---

## 🛠️ **Exemplos Práticos**

### **Exemplo 1: Módulo de Interface Avançada**
```lua
-- modules/advanced_ui/module.otmod
name: AdvancedUI
version: 2.1.0
author: UI Developer
description: Advanced UI components and widgets

dependencies: corelib, gamelib, ui_framework
hooks: onGameStart, onUIEvent, onPlayerLogin
resources: styles/advanced.otui, images/icons, scripts/widgets.lua
permissions: ui_modification, file_access

settings:
  theme: dark
  animations: true
  custom_widgets: true
```

```lua
-- modules/advanced_ui/init.lua
local AdvancedUI = {}

function AdvancedUI:init()
    -- Carregar recursos
    self:loadResources()
    
    -- Registrar widgets customizados
    self:registerCustomWidgets()
    
    -- Configurar hooks
    self:setupHooks()
    
    print("AdvancedUI module loaded successfully")
end

function AdvancedUI:loadResources()
    -- Carregar estilos OTUI
    g_ui.loadStyle("modules/advanced_ui/styles/advanced.otui")
    
    -- Carregar imagens
    g_ui.loadImage("modules/advanced_ui/images/icons")
end

function AdvancedUI:registerCustomWidgets()
    -- Registrar widgets customizados
    g_ui.registerWidget("AdvancedButton", AdvancedButton)
    g_ui.registerWidget("AdvancedPanel", AdvancedPanel)
    g_ui.registerWidget("AdvancedList", AdvancedList)
end

function AdvancedUI:setupHooks()
    -- Hook para inicialização
    connect(g_game, { onGameStart = self.onGameStart })
    
    -- Hook para eventos de UI
    connect(g_ui, { onUIEvent = self.onUIEvent })
end

function AdvancedUI:onGameStart()
    -- Inicializar interface avançada
    self:createMainInterface()
end

function AdvancedUI:onUIEvent(eventType, ...)
    -- Processar eventos de UI
    if eventType == "widget_created" then
        self:setupWidget(...)
    end
end

return AdvancedUI
```

### **Exemplo 2: Módulo de Sistema de Combate**
```lua
-- modules/combat_system/module.otmod
name: CombatSystem
version: 1.5.0
author: Combat Developer
description: Advanced combat system with custom mechanics

dependencies: corelib, gamelib, battle_module
hooks: onCombatStart, onCombatEnd, onCreatureMove, onSpellCast
resources: scripts/combat.lua, data/spells.json, sounds/combat
permissions: game_modification, network_access

settings:
  damage_calculation: advanced
  spell_effects: true
  combat_log: true
```

```lua
-- modules/combat_system/init.lua
local CombatSystem = {}

function CombatSystem:init()
    -- Carregar dados de combate
    self:loadCombatData()
    
    -- Configurar sistema de dano
    self:setupDamageSystem()
    
    -- Registrar hooks
    self:registerHooks()
    
    print("CombatSystem module loaded successfully")
end

function CombatSystem:loadCombatData()
    -- Carregar dados de magias
    local spellsFile = "modules/combat_system/data/spells.json"
    self.spells = json.decode(io.readfile(spellsFile))
    
    -- Carregar sons de combate
    self:loadCombatSounds()
end

function CombatSystem:setupDamageSystem()
    -- Configurar cálculo de dano avançado
    self.damageCalculator = AdvancedDamageCalculator.new()
    
    -- Configurar efeitos de magia
    self.spellEffects = SpellEffectManager.new()
end

function CombatSystem:registerHooks()
    connect(g_game, {
        onCombatStart = self.onCombatStart,
        onCombatEnd = self.onCombatEnd,
        onSpellCast = self.onSpellCast
    })
end

function CombatSystem:onCombatStart(attacker, target)
    -- Inicializar combate
    self:startCombat(attacker, target)
    
    -- Aplicar efeitos de combate
    self:applyCombatEffects(attacker, target)
end

function CombatSystem:onSpellCast(caster, spell, target)
    -- Processar magia
    local spellData = self.spells[spell]
    if spellData then
        self:castSpell(caster, spellData, target)
    end
end

return CombatSystem
```

---

## 🔗 **Dependências e Integração**

### **Dependências Internas**
- **[[otclient_sistema_modulos|Sistema de Módulos]]** - Sistema base de módulos
- **[[otclient_sistema_lua_avancado|Sistema de Lua Avançado]]** - Recursos Lua avançados
- **[[otclient_sistema_eventos|Sistema de Eventos]]** - Sistema de eventos

### **Dependências Externas**
- **OTClient Core** - Sistema core do cliente
- **Lua 5.1+** - Linguagem base
- **File System** - Sistema de arquivos

### **Integração com Outros Sistemas**
```lua
-- Exemplo: Integração com sistema de eventos
local ModuleSystem = require("modules/modulelib/module_system")
local EventSystem = require("modules/corelib/event_system")

-- Registrar eventos de módulos
EventSystem:addListener("module_loaded", function(moduleName, module)
    ModuleSystem:setupModuleHooks(moduleName, module)
end)

EventSystem:addListener("module_unloaded", function(moduleName)
    ModuleSystem:cleanupModuleHooks(moduleName)
end)
```

---

## 📚 **Referência de API**

### **Funções Principais**

#### **Carregamento de Módulos**
- `ModuleLoader:loadModule(name)` - Carrega um módulo
- `ModuleLoader:unloadModule(name)` - Descarrega um módulo
- `ModuleLoader:reloadModule(name)` - Recarrega um módulo
- `ModuleLoader:getLoadedModules()` - Lista módulos carregados

#### **Gerenciamento de Dependências**
- `ModuleLoader:checkDependencies(deps)` - Verifica dependências
- `ModuleLoader:resolveDependencies(module)` - Resolve dependências
- `ModuleLoader:detectCircularDependencies(module)` - Detecta dependências circulares

#### **Sistema de Hooks**
- `HookSystem:registerHook(name, module, callback)` - Registra um hook
- `HookSystem:triggerHook(name, ...)` - Dispara um hook
- `HookSystem:unregisterHook(name, module)` - Remove um hook

---

## 🎯 **Melhores Práticas**

### **1. Estrutura de Módulos**
```lua
-- ✅ Bom: Estrutura organizada
modules/my_module/
├── init.lua          # Ponto de entrada
├── module.otmod      # Definição do módulo
├── lib/              # Bibliotecas
├── resources/        # Recursos
└── styles/           # Estilos

-- ❌ Ruim: Estrutura desorganizada
modules/my_module/
├── main.lua          # Nome não padrão
├── config.txt        # Formato não padrão
└── files/            # Estrutura genérica
```

### **2. Gerenciamento de Dependências**
```lua
-- ✅ Bom: Dependências claras
dependencies: corelib, gamelib, ui_framework

-- ❌ Ruim: Dependências implícitas
-- Módulo depende de outros sem declarar
```

### **3. Tratamento de Erros**
```lua
-- ✅ Bom: Tratamento adequado
local success, module = pcall(dofile, initFile)
if not success then
    print("Module load error: " .. tostring(module))
    return nil
end

-- ❌ Ruim: Sem tratamento
local module = dofile(initFile) -- Pode quebrar
```

---

## 🔍 **Debugging e Troubleshooting**

### **Debug de Módulos**
```lua
-- Função para debug de módulos
function ModuleLoader:debugModule(moduleName)
    local module = self.moduleCache[moduleName]
    local moduleDef = self.loadedModules[moduleName]
    
    print("=== Module Debug: " .. moduleName .. " ===")
    print("Loaded: " .. tostring(module ~= nil))
    print("Definition: " .. tostring(moduleDef ~= nil))
    
    if moduleDef then
        print("Version: " .. moduleDef.version)
        print("Dependencies: " .. table.concat(moduleDef.dependencies, ", "))
        print("Hooks: " .. table.concat(moduleDef.hooks, ", "))
    end
end
```

### **Verificação de Integridade**
```lua
-- Função para verificar integridade de módulos
function ModuleLoader:verifyModuleIntegrity(moduleName)
    local modulePath = "modules/" .. moduleName
    local requiredFiles = {"init.lua", "module.otmod"}
    
    for _, file in ipairs(requiredFiles) do
        local filePath = modulePath .. "/" .. file
        if not io.exists(filePath) then
            print("Missing required file: " .. filePath)
            return false
        end
    end
    
    return true
end
```

---

## 📖 **Recursos Adicionais**

### **Documentação Relacionada**
- **[[otclient_sistema_modulos|Sistema de Módulos]]** - Sistema base de módulos
- **[[otclient_sistema_lua_avancado|Sistema de Lua Avançado]]** - Recursos Lua avançados
- **[[otclient_sistema_eventos|Sistema de Eventos]]** - Sistema de eventos

### **Exemplos de Código**
- **[[otclient_exemplos_modulos_avancado|Exemplos Módulos Avançado]]** - Exemplos práticos
- **[[otclient_padroes_modulos|Padrões de Módulos]]** - Padrões de design para módulos

### **Ferramentas de Desenvolvimento**
- **[[otclient_ferramentas_modulos|Ferramentas de Módulos]]** - Ferramentas para desenvolvimento
- **[[otclient_debug_modulos|Debug de Módulos]]** - Ferramentas de debug

---

## 🎯 **Próximos Passos**

1. **Crie um Módulo Simples** - Comece com estrutura básica
2. **Adicione Dependências** - Configure dependências entre módulos
3. **Implemente Hooks** - Conecte com eventos do sistema
4. **Gerencie Recursos** - Adicione imagens, sons e estilos
5. **Teste Hot-Reload** - Configure recarregamento automático

---

> [!success] **Conclusão**
> O Sistema de Módulos Avançado do OTClient oferece uma plataforma robusta e flexível para desenvolvimento de módulos complexos, com recursos avançados como dependências dinâmicas, hooks de sistema e gerenciamento automático de recursos. 