---
title: Configuration
tags: [otclient, system, guide, documentation]
status: completed
aliases: [Configuration]
---

# Sistema de Configuração OTClient

O OTClient implementa um sistema robusto de configuração baseado em arquivos OTML (OTClient Markup Language) que permite personalizar todos os aspectos do cliente, desde configurações gráficas até controles de jogo.

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Arquitetura do Sistema](#arquitetura-do-sistema)
3. [ConfigManager (g_configs)](#configmanager-g_configs)
4. [GameConfig (g_gameConfig)](#gameconfig-g_gameconfig)
5. [Settings (g_settings)](#settings-g_settings)
6. [Formato OTML](#formato-otml)
7. [Configurações de Jogo](#configurações-de-jogo)
8. [Sistema de Opções](#sistema-de-opções)
9. [Configurações de Controle](#configurações-de-controle)
10. [Implementação Prática](#implementação-prática)
11. [Melhores Práticas](#melhores-práticas)

## 🎯 Visão Geral

O sistema de configuração do OTClient oferece:

- **Configuração Centralizada**: ConfigManager gerencia todos os arquivos de configuração
- **Persistência Automática**: Configurações salvas automaticamente em OTML
- **Hierarquia de Configs**: Settings globais + configs específicos por contexto
- **Hot Reload**: Recarregamento dinâmico de configurações
- **Validação**: Sistema de tipos e validação de valores
- **Múltiplos Perfis**: Suporte a presets e perfis de usuário

### 🏗️ **Arquitetura de Configuração**

```
Sistema de Configuração
   │
   ├─ ConfigManager (g_configs)
   │   │
   │   ├─ Settings (config principal)
   │   │   └─ settings.otml
   │   │
   │   ├─ Configs específicos
   │   │   ├─ keybinds/*.otml
   │   │   ├─ hotkeys/*.otml
   │   │   └─ profiles/*.otml
   │   │
   │   └─ GameConfig (g_gameConfig)
   │       └─ setup.otml
   │
   └─ Sistema de Opções UI
       ├─ Interface de configuração
       ├─ Validação em tempo real
       └─ Persistência automática
```

## ⚙️ ConfigManager (g_configs)

### 📁 **Gerenciamento Central de Configs**

#### Nível Basic
```lua
-- ConfigManager é um singleton global disponível como g_configs
-- Gerencia carregamento, salvamento e ciclo de vida dos configs

-- Obter configuração principal (settings)
local settings = g_configs.getSettings()

-- Carregar config específico
local myConfig = g_configs.get("myconfig.otml")

-- Criar novo config
local newConfig = g_configs.create("data/myapp.otml")

-- Carregar config como settings
local customSettings = g_configs.loadSettings("mysettings.otml")

-- Descarregar config da memória
g_configs.unload("myconfig.otml")
```

#### Nível Intermediate
```lua
-- ConfigManager é um singleton global disponível como g_configs
-- Gerencia carregamento, salvamento e ciclo de vida dos configs

-- Obter configuração principal (settings)
local settings = g_configs.getSettings()

-- Carregar config específico
local myConfig = g_configs.get("myconfig.otml")

-- Criar novo config
local newConfig = g_configs.create("data/myapp.otml")

-- Carregar config como settings
local customSettings = g_configs.loadSettings("mysettings.otml")

-- Descarregar config da memória
g_configs.unload("myconfig.otml")
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
-- ConfigManager é um singleton global disponível como g_configs
-- Gerencia carregamento, salvamento e ciclo de vida dos configs

-- Obter configuração principal (settings)
local settings = g_configs.getSettings()

-- Carregar config específico
local myConfig = g_configs.get("myconfig.otml")

-- Criar novo config
local newConfig = g_configs.create("data/myapp.otml")

-- Carregar config como settings
local customSettings = g_configs.loadSettings("mysettings.otml")

-- Descarregar config da memória
g_configs.unload("myconfig.otml")
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

### 🔧 **Operações com Configs**

```lua
-- Criar um config personalizado
    --  Criar um config personalizado (traduzido)
local function createCustomConfig()
    local config = g_configs.create("data/custom.otml")
    
    -- Definir valores
    --  Definir valores (traduzido)
    config:setValue("window.width", 1024)
    config:setValue("window.height", 768)
    config:setValue("graphics.vsync", true)
    config:setValue("audio.volume", 0.8)
    
    -- Definir lista
    --  Definir lista (traduzido)
    config:setList("recent.servers", {
        "server1.com",
        "server2.com", 
        "localhost"
    })
    
    -- Salvar no disco
    --  Salvar no disco (traduzido)
    config:save()
    
    return config
end

-- Ler valores do config
    --  Ler valores do config (traduzido)
local function readConfigValues(config)
    local width = config:getValue("window.width")
    local height = config:getValue("window.height")
    local vsync = config:getValue("graphics.vsync") == "true"
    local volume = tonumber(config:getValue("audio.volume"))
    
    local servers = config:getList("recent.servers")
    
    print("Resolução:", width .. "x" .. height)
    print("VSync:", vsync)
    print("Volume:", volume)
    print("Servidores:")
    for _, server in ipairs(servers) do
    -- Loop de repetição
        print("- " .. server)
    end
end
```

### 📊 **Gerenciamento de Nodes OTML**

```lua
-- Trabalhar com nodes OTML complexos
    --  Trabalhar com nodes OTML complexos (traduzido)
local config = g_configs.create("complex.otml")

-- Criar node estruturado
    --  Criar node estruturado (traduzido)
local windowNode = {
    size = "1024 768",
    position = "center",
    fullscreen = false,
    decorations = true
}

config:setNode("window", windowNode)

-- Obter node
    --  Obter node (traduzido)
local retrievedNode = config:getNode("window")
if retrievedNode then
    -- Verificação condicional
    print("Tamanho da janela:", retrievedNode.size)
    print("Posição:", retrievedNode.position)
end

-- Mesclar nodes
    --  Mesclar nodes (traduzido)
local updateNode = {
    maximized = true,
    opacity = 0.95
}

config:mergeNode("window", updateNode)

-- Verificar tamanho do node
    --  Verificar tamanho do node (traduzido)
local nodeSize = config:getNodeSize("window")
print("Node possui " .. nodeSize .. " elementos")

-- Obter ou criar node
    --  Obter ou criar node (traduzido)
local audioNode = config:getOrCreateNode("audio", {
    volume = 1.0,
    muted = false
})
```

## 🎮 GameConfig (g_gameConfig)

### 🔧 **Configuração Global do Jogo**

#### Nível Basic
```lua
-- GameConfig contém configurações fixas do jogo carregadas de setup.otml
-- Não são editáveis pelo usuário em runtime
-- Configurações de sprite
local spriteSize = g_gameConfig.getSpriteSize()  -- 32
print("Tamanho do sprite:", spriteSize .. "x" .. spriteSize)
-- Versão suportada
local lastVersion = g_gameConfig.getLastSupportedVersion()  -- 1412
print("Última versão suportada:", lastVersion)
-- Configurações de mapa
local mapViewPort = g_gameConfig.getMapViewPort()  -- {width=8, height=6}
local mapMaxZ = g_gameConfig.getMapMaxZ()  -- 15
local seaFloor = g_gameConfig.getMapSeaFloor()  -- 7
print("Viewport do mapa:", mapViewPort.width .. "x" .. mapViewPort.height)
print("Máximo Z:", mapMaxZ)
print("Andar do mar:", seaFloor)
-- Configurações de tile
local maxElevation = g_gameConfig.getTileMaxElevation()  -- 24
local maxThings = g_gameConfig.getTileMaxThings()  -- 10
local transparentRange = g_gameConfig.getTileTransparentFloorViewRange()  -- 2
-- Configurações de criatura
local drawByWidget = g_gameConfig.isDrawingInformationByWidget()
local forceWalkFormula = g_gameConfig.isForcingNewWalkingFormula()
local shieldBlinkTicks = g_gameConfig.getShieldBlinkTicks()  -- 500
-- Configurações de renderização
local drawCovered = g_gameConfig.isDrawingCoveredThings()
local itemTicksPerFrame = g_gameConfig.getItemTicksPerFrame()  -- 500
local effectTicksPerFrame = g_gameConfig.getEffectTicksPerFrame()  -- 75
-- Configurações de fonte
local creatureFont = g_gameConfig.getCreatureNameFont()
local animatedFont = g_gameConfig.getAnimatedTextFont()
local staticFont = g_gameConfig.getStaticTextFont()
local widgetFont = g_gameConfig.getWidgetTextFont()
print("Fonte de criaturas:", g_gameConfig.getCreatureNameFontName())
print("Fonte de texto animado:", g_gameConfig.getAnimatedTextFontName())
```

#### Nível Intermediate
```lua
-- GameConfig contém configurações fixas do jogo carregadas de setup.otml
-- Não são editáveis pelo usuário em runtime

-- Configurações de sprite
local spriteSize = g_gameConfig.getSpriteSize()  -- 32
print("Tamanho do sprite:", spriteSize .. "x" .. spriteSize)

-- Versão suportada
local lastVersion = g_gameConfig.getLastSupportedVersion()  -- 1412
print("Última versão suportada:", lastVersion)

-- Configurações de mapa
local mapViewPort = g_gameConfig.getMapViewPort()  -- {width=8, height=6}
local mapMaxZ = g_gameConfig.getMapMaxZ()  -- 15
local seaFloor = g_gameConfig.getMapSeaFloor()  -- 7

print("Viewport do mapa:", mapViewPort.width .. "x" .. mapViewPort.height)
print("Máximo Z:", mapMaxZ)
print("Andar do mar:", seaFloor)

-- Configurações de tile
local maxElevation = g_gameConfig.getTileMaxElevation()  -- 24
local maxThings = g_gameConfig.getTileMaxThings()  -- 10
local transparentRange = g_gameConfig.getTileTransparentFloorViewRange()  -- 2

-- Configurações de criatura
local drawByWidget = g_gameConfig.isDrawingInformationByWidget()
local forceWalkFormula = g_gameConfig.isForcingNewWalkingFormula()
local shieldBlinkTicks = g_gameConfig.getShieldBlinkTicks()  -- 500

-- Configurações de renderização
local drawCovered = g_gameConfig.isDrawingCoveredThings()
local itemTicksPerFrame = g_gameConfig.getItemTicksPerFrame()  -- 500
local effectTicksPerFrame = g_gameConfig.getEffectTicksPerFrame()  -- 75

-- Configurações de fonte
local creatureFont = g_gameConfig.getCreatureNameFont()
local animatedFont = g_gameConfig.getAnimatedTextFont()
local staticFont = g_gameConfig.getStaticTextFont()
local widgetFont = g_gameConfig.getWidgetTextFont()

print("Fonte de criaturas:", g_gameConfig.getCreatureNameFontName())
print("Fonte de texto animado:", g_gameConfig.getAnimatedTextFontName())
```

#### Nível Advanced
```lua
-- GameConfig contém configurações fixas do jogo carregadas de setup.otml
-- Não são editáveis pelo usuário em runtime

-- Configurações de sprite
local spriteSize = g_gameConfig.getSpriteSize()  -- 32
print("Tamanho do sprite:", spriteSize .. "x" .. spriteSize)

-- Versão suportada
local lastVersion = g_gameConfig.getLastSupportedVersion()  -- 1412
print("Última versão suportada:", lastVersion)

-- Configurações de mapa
local mapViewPort = g_gameConfig.getMapViewPort()  -- {width=8, height=6}
local mapMaxZ = g_gameConfig.getMapMaxZ()  -- 15
local seaFloor = g_gameConfig.getMapSeaFloor()  -- 7

print("Viewport do mapa:", mapViewPort.width .. "x" .. mapViewPort.height)
print("Máximo Z:", mapMaxZ)
print("Andar do mar:", seaFloor)

-- Configurações de tile
local maxElevation = g_gameConfig.getTileMaxElevation()  -- 24
local maxThings = g_gameConfig.getTileMaxThings()  -- 10
local transparentRange = g_gameConfig.getTileTransparentFloorViewRange()  -- 2

-- Configurações de criatura
local drawByWidget = g_gameConfig.isDrawingInformationByWidget()
local forceWalkFormula = g_gameConfig.isForcingNewWalkingFormula()
local shieldBlinkTicks = g_gameConfig.getShieldBlinkTicks()  -- 500

-- Configurações de renderização
local drawCovered = g_gameConfig.isDrawingCoveredThings()
local itemTicksPerFrame = g_gameConfig.getItemTicksPerFrame()  -- 500
local effectTicksPerFrame = g_gameConfig.getEffectTicksPerFrame()  -- 75

-- Configurações de fonte
local creatureFont = g_gameConfig.getCreatureNameFont()
local animatedFont = g_gameConfig.getAnimatedTextFont()
local staticFont = g_gameConfig.getStaticTextFont()
local widgetFont = g_gameConfig.getWidgetTextFont()

print("Fonte de criaturas:", g_gameConfig.getCreatureNameFontName())
print("Fonte de texto animado:", g_gameConfig.getAnimatedTextFontName())
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

### ⚡ **Configurações de Performance**

#### Nível Basic
```lua
-- Velocidade de movimento
local playerDiagSpeed = g_gameConfig.getPlayerDiagonalWalkSpeed()  -- 3
local creatureDiagSpeed = g_gameConfig.getCreatureDiagonalWalkSpeed()  -- 3

-- Timings de animação
local invisibleTicks = g_gameConfig.getInvisibleTicksPerFrame()  -- 500
local missileTicks = g_gameConfig.getMissileTicksPerFrame()  -- 75
local animatedTextDuration = g_gameConfig.getAnimatedTextDuration()  -- 1000

-- Duração de texto estático
local staticDurationPerChar = g_gameConfig.getStaticDurationPerCharacter()  -- 60
local minStaticDuration = g_gameConfig.getMinStatictextDuration()  -- 3000

-- Configurações visuais
local volatileSquareDuration = g_gameConfig.getVolatileSquareDuration()  -- 1000

-- Typing indicator
local drawTyping = g_gameConfig.drawTyping()
local typingIcon = g_gameConfig.getTypingIcon()

print("Mostrar digitação:", drawTyping)
print("Ícone de digitação:", typingIcon)
```

#### Nível Intermediate
```lua
-- Velocidade de movimento
local playerDiagSpeed = g_gameConfig.getPlayerDiagonalWalkSpeed()  -- 3
local creatureDiagSpeed = g_gameConfig.getCreatureDiagonalWalkSpeed()  -- 3

-- Timings de animação
local invisibleTicks = g_gameConfig.getInvisibleTicksPerFrame()  -- 500
local missileTicks = g_gameConfig.getMissileTicksPerFrame()  -- 75
local animatedTextDuration = g_gameConfig.getAnimatedTextDuration()  -- 1000

-- Duração de texto estático
local staticDurationPerChar = g_gameConfig.getStaticDurationPerCharacter()  -- 60
local minStaticDuration = g_gameConfig.getMinStatictextDuration()  -- 3000

-- Configurações visuais
local volatileSquareDuration = g_gameConfig.getVolatileSquareDuration()  -- 1000

-- Typing indicator
local drawTyping = g_gameConfig.drawTyping()
local typingIcon = g_gameConfig.getTypingIcon()

print("Mostrar digitação:", drawTyping)
print("Ícone de digitação:", typingIcon)
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
-- Velocidade de movimento
local playerDiagSpeed = g_gameConfig.getPlayerDiagonalWalkSpeed()  -- 3
local creatureDiagSpeed = g_gameConfig.getCreatureDiagonalWalkSpeed()  -- 3

-- Timings de animação
local invisibleTicks = g_gameConfig.getInvisibleTicksPerFrame()  -- 500
local missileTicks = g_gameConfig.getMissileTicksPerFrame()  -- 75
local animatedTextDuration = g_gameConfig.getAnimatedTextDuration()  -- 1000

-- Duração de texto estático
local staticDurationPerChar = g_gameConfig.getStaticDurationPerCharacter()  -- 60
local minStaticDuration = g_gameConfig.getMinStatictextDuration()  -- 3000

-- Configurações visuais
local volatileSquareDuration = g_gameConfig.getVolatileSquareDuration()  -- 1000

-- Typing indicator
local drawTyping = g_gameConfig.drawTyping()
local typingIcon = g_gameConfig.getTypingIcon()

print("Mostrar digitação:", drawTyping)
print("Ícone de digitação:", typingIcon)
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

## ⚙️ Settings (g_settings)

### 💾 **Configurações Persistentes do Usuário**

#### Nível Basic
```lua
-- g_settings é o config principal para configurações do usuário
-- Automaticamente persistido em settings.otml

-- Definir valores
g_settings.set("graphics.fullscreen", true)
g_settings.set("audio.masterVolume", 0.8)
g_settings.set("game.autoLogin", false)
g_settings.set("interface.theme", "dark")

-- Obter valores com tipos específicos
local fullscreen = g_settings.getBoolean("graphics.fullscreen")
local volume = g_settings.getNumber("audio.masterVolume")
local theme = g_settings.getString("interface.theme")

-- Verificar existência
if g_settings.exists("user.nickname") then
    local nickname = g_settings.getString("user.nickname")
    print("Usuário:", nickname)
end

-- Definir valores padrão
g_settings.setDefault("graphics.antialiasing", true)
g_settings.setDefault("controls.mouseSensitivity", 1.0)

-- Remover configuração
g_settings.remove("temporary.setting")

-- Salvar configurações
g_settings.save()
```

#### Nível Intermediate
```lua
-- g_settings é o config principal para configurações do usuário
-- Automaticamente persistido em settings.otml

-- Definir valores
g_settings.set("graphics.fullscreen", true)
g_settings.set("audio.masterVolume", 0.8)
g_settings.set("game.autoLogin", false)
g_settings.set("interface.theme", "dark")

-- Obter valores com tipos específicos
local fullscreen = g_settings.getBoolean("graphics.fullscreen")
local volume = g_settings.getNumber("audio.masterVolume")
local theme = g_settings.getString("interface.theme")

-- Verificar existência
if g_settings.exists("user.nickname") then
    local nickname = g_settings.getString("user.nickname")
    print("Usuário:", nickname)
end

-- Definir valores padrão
g_settings.setDefault("graphics.antialiasing", true)
g_settings.setDefault("controls.mouseSensitivity", 1.0)

-- Remover configuração
g_settings.remove("temporary.setting")

-- Salvar configurações
g_settings.save()
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
-- g_settings é o config principal para configurações do usuário
-- Automaticamente persistido em settings.otml

-- Definir valores
g_settings.set("graphics.fullscreen", true)
g_settings.set("audio.masterVolume", 0.8)
g_settings.set("game.autoLogin", false)
g_settings.set("interface.theme", "dark")

-- Obter valores com tipos específicos
local fullscreen = g_settings.getBoolean("graphics.fullscreen")
local volume = g_settings.getNumber("audio.masterVolume")
local theme = g_settings.getString("interface.theme")

-- Verificar existência
if g_settings.exists("user.nickname") then
    local nickname = g_settings.getString("user.nickname")
    print("Usuário:", nickname)
end

-- Definir valores padrão
g_settings.setDefault("graphics.antialiasing", true)
g_settings.setDefault("controls.mouseSensitivity", 1.0)

-- Remover configuração
g_settings.remove("temporary.setting")

-- Salvar configurações
g_settings.save()
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

### 📋 **Listas e Arrays**

```lua
-- Trabalhar com listas
    --  Trabalhar com listas (traduzido)
local serverList = {
    "server1.otserv.com:7171",
    "server2.otserv.com:7172",
    "localhost:7171"
}

g_settings.setList("recent.servers", serverList)

-- Obter lista
    --  Obter lista (traduzido)
local servers = g_settings.getList("recent.servers")
for i, server in ipairs(servers) do
    -- Loop de repetição
    print("Servidor " .. i .. ":", server)
end

-- Adicionar item à lista
table.insert(servers, "newserver.com:7171")
g_settings.setList("recent.servers", servers)

-- Controles presets
    --  Controles presets (traduzido)
local presets = g_settings.getList("controls-presets")
if #presets == 0 then
    -- Verificação condicional
    presets = {"Druid", "Knight", "Paladin", "Sorcerer"}
    g_settings.setList("controls-presets", presets)
end

local currentPreset = g_settings.getString("controls-preset-current") or "Druid"
```

## 📝 Formato OTML

### 🔤 **Sintaxe OTML Básica**

```otml
// Arquivo: example.otml
// Comentários com // ou #

// Valores simples
window-width: 1024
window-height: 768
fullscreen: false
title: "OTClient - Redemption"

// Números
volume: 0.8
fps-limit: 60

// Listas
recent-servers:
  - server1.com:7171
  - server2.com:7172
  - localhost:7171

// Objects/Nodes aninhados
graphics:
  antialiasing: true
  vsync: true
  texture-filtering: bilinear
  
  effects:
    particles: true
    bloom: false
    shadows: true

audio:
  master-volume: 0.8
  music-volume: 0.6
  sfx-volume: 1.0
  
  devices:
    output: "default"
    input: "none"

// Arrays complexos
hotkeys:
  - key: "F1"
    action: "cast spell"
    spell: "exura"
    
  - key: "F2" 
    action: "use item"
    item-id: 266
    target: "self"
```

### 🔧 **Estruturas Avançadas**

```otml
// Arquivo: gameconfig.otml
game:
  sprite-size: 32
  last-supported-version: 1412
  draw-typing: false
  typing-icon: "/images/game/console/typing"
  
  map:
    viewport: 8 6
    max-z: 15
    sea-floor: 7
    underground-floor: 8
    aware-underground-floor-range: 2

  tile:
    max-elevation: 24
    max-things: 10
    transparent-floor-view-range: 2

  creature:
    draw-information-by-widget-beta: false
    force-new-walking-formula: false
    shield-blink-ticks: 500
    volatile-square-duration: 1000
    adjust-creature-information-based-crop-size: false
    diagonal-walk-speed: 3

  player:
    diagonal-walk-speed: 3

  render:
    draw-covered-things: false
    invisible-ticks-per-frame: 75
    item-ticks-per-frame: 75
    effect-ticks-per-frame: 75
    missile-ticks-per-frame: 75
    animated-text-duration: 1000
    static-duration-per-character: 60
    min-static-text-duration: 3000

font:
  widget: "verdana-11px-antialised"
  static-text: "verdana-11px-rounded"
  animated-text: "verdana-11px-rounded"
  creature-text: "verdana-11px-rounded"
```

## 🎯 Configurações de Jogo

### 🎮 **Sistema de Opções Integrado**

#### Nível Basic
```lua
-- Sistema de opções do cliente (modules/client_options)
-- Integra com g_settings para persistência
-- Definir uma opção
function setOption(key, value, force)
    if not options[key] or (not force and options[key].value == value) then
    end
    -- Executar ação associada
    if options[key].action then
    end
    -- Atualizar UI
    -- Salvar em settings
end
-- Obter valor de opção
function getOption(key)
end
-- Exemplos de uso
local fullscreen = getOption("graphics.fullscreen")
local volume = getOption("audio.masterVolume")
```

#### Nível Intermediate
```lua
-- Sistema de opções do cliente (modules/client_options)
-- Integra com g_settings para persistência

-- Definir uma opção
function setOption(key, value, force)
    if not options[key] or (not force and options[key].value == value) then
        return
    end
    
    -- Executar ação associada
    if options[key].action then
        options[key].action(value)
    end
    
    -- Atualizar UI
    updateOptionWidget(key, value)
    
    -- Salvar em settings
    options[key].value = value
    g_settings.set(key, value)
end

-- Obter valor de opção
function getOption(key)
    return options[key].value
end

-- Exemplos de uso
setOption("graphics.fullscreen", true)
setOption("audio.masterVolume", 0.8)
setOption("interface.showFPS", false)

local fullscreen = getOption("graphics.fullscreen")
local volume = getOption("audio.masterVolume")
```

#### Nível Advanced
```lua
-- Sistema de opções do cliente (modules/client_options)
-- Integra com g_settings para persistência

-- Definir uma opção
function setOption(key, value, force)
    if not options[key] or (not force and options[key].value == value) then
        return
    end
    
    -- Executar ação associada
    if options[key].action then
        options[key].action(value)
    end
    
    -- Atualizar UI
    updateOptionWidget(key, value)
    
    -- Salvar em settings
    options[key].value = value
    g_settings.set(key, value)
end

-- Obter valor de opção
function getOption(key)
    return options[key].value
end

-- Exemplos de uso
setOption("graphics.fullscreen", true)
setOption("audio.masterVolume", 0.8)
setOption("interface.showFPS", false)

local fullscreen = getOption("graphics.fullscreen")
local volume = getOption("audio.masterVolume")
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

### 🔧 **Configurações Gráficas**

```lua
-- Configurações de gráficos
local graphicsOptions = {
    fullscreen = g_settings.getBoolean("graphics.fullscreen"),
    vsync = g_settings.getBoolean("graphics.vsync"), 
    antialiasing = g_settings.getString("graphics.antialiasing"),
    textureFiltering = g_settings.getString("graphics.textureFiltering"),
    frameRate = g_settings.getNumber("graphics.frameRate"),
    
    -- Efeitos
    --  Efeitos (traduzido)
    particles = g_settings.getBoolean("effects.particles"),
    bloom = g_settings.getBoolean("effects.bloom"),
    shadows = g_settings.getBoolean("effects.shadows")
}

-- Aplicar configurações gráficas
function applyGraphicsSettings()
    -- Função: applyGraphicsSettings
    if graphicsOptions.fullscreen then
    -- Verificação condicional
        g_window.setFullscreen(true)
    end
    
    g_graphics.setVSync(graphicsOptions.vsync)
    
    if graphicsOptions.frameRate > 0 then
    -- Verificação condicional
        g_app.setMaxFps(graphicsOptions.frameRate)
    end
    
    -- Configurar antialiasing
    --  Configurar antialiasing (traduzido)
    if graphicsOptions.antialiasing ~= "none" then
    -- Verificação condicional
        g_graphics.setAntialiasing(graphicsOptions.antialiasing)
    end
end
```

### 🔊 **Configurações de Áudio**

#### Nível Basic
```lua
-- Sistema de áudio
local audioOptions = {
    masterVolume = g_settings.getNumber("audio.masterVolume"),
    musicVolume = g_settings.getNumber("audio.musicVolume"),
    sfxVolume = g_settings.getNumber("audio.sfxVolume"),
    
    -- Dispositivos
    outputDevice = g_settings.getString("audio.outputDevice"),
    inputDevice = g_settings.getString("audio.inputDevice"),
    
    -- Configurações avançadas
    sampleRate = g_settings.getNumber("audio.sampleRate"),
    bufferSize = g_settings.getNumber("audio.bufferSize")
}

-- Aplicar configurações de áudio
function applyAudioSettings()
    g_sounds.setVolume(audioOptions.masterVolume)
    g_music.setVolume(audioOptions.musicVolume)
    
    -- Configurar dispositivos se suportado
    if g_audio.setOutputDevice then
        g_audio.setOutputDevice(audioOptions.outputDevice)
    end
end
```

#### Nível Intermediate
```lua
-- Sistema de áudio
local audioOptions = {
    masterVolume = g_settings.getNumber("audio.masterVolume"),
    musicVolume = g_settings.getNumber("audio.musicVolume"),
    sfxVolume = g_settings.getNumber("audio.sfxVolume"),
    
    -- Dispositivos
    outputDevice = g_settings.getString("audio.outputDevice"),
    inputDevice = g_settings.getString("audio.inputDevice"),
    
    -- Configurações avançadas
    sampleRate = g_settings.getNumber("audio.sampleRate"),
    bufferSize = g_settings.getNumber("audio.bufferSize")
}

-- Aplicar configurações de áudio
function applyAudioSettings()
    g_sounds.setVolume(audioOptions.masterVolume)
    g_music.setVolume(audioOptions.musicVolume)
    
    -- Configurar dispositivos se suportado
    if g_audio.setOutputDevice then
        g_audio.setOutputDevice(audioOptions.outputDevice)
    end
end
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
-- Sistema de áudio
local audioOptions = {
    masterVolume = g_settings.getNumber("audio.masterVolume"),
    musicVolume = g_settings.getNumber("audio.musicVolume"),
    sfxVolume = g_settings.getNumber("audio.sfxVolume"),
    
    -- Dispositivos
    outputDevice = g_settings.getString("audio.outputDevice"),
    inputDevice = g_settings.getString("audio.inputDevice"),
    
    -- Configurações avançadas
    sampleRate = g_settings.getNumber("audio.sampleRate"),
    bufferSize = g_settings.getNumber("audio.bufferSize")
}

-- Aplicar configurações de áudio
function applyAudioSettings()
    g_sounds.setVolume(audioOptions.masterVolume)
    g_music.setVolume(audioOptions.musicVolume)
    
    -- Configurar dispositivos se suportado
    if g_audio.setOutputDevice then
        g_audio.setOutputDevice(audioOptions.outputDevice)
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

## 🎛️ Configurações de Controle

### ⌨️ **Sistema de Keybinds**

#### Nível Basic
```lua
-- Sistema de controles com múltiplos presets
-- Cada preset tem keybinds e hotkeys separados
-- Configuração de keybinds
local function setupKeybinds()
    local preset = Keybind.currentPreset or "Druid"
    -- Carregar configs do preset
    local keybindsConfig = g_configs.create("/controls/keybinds/" .. preset .. ".otml")
    local hotkeysConfig = g_configs.create("/controls/hotkeys/" .. preset .. ".otml")
    -- Definir keybinds padrão
    -- Salvar configurações
end
-- Gerenciar presets
local function createControlsPreset(presetName)
    -- Adicionar à lista de presets
    local presets = g_settings.getList("controls-presets")
    -- Criar arquivos de configuração
    local keybindsConfig = g_configs.create("/controls/keybinds/" .. presetName .. ".otml")
    local hotkeysConfig = g_configs.create("/controls/hotkeys/" .. presetName .. ".otml")
    -- Configurações padrão para novo preset
end
```

#### Nível Intermediate
```lua
-- Sistema de controles com múltiplos presets
-- Cada preset tem keybinds e hotkeys separados

-- Configuração de keybinds
local function setupKeybinds()
    local preset = Keybind.currentPreset or "Druid"
    
    -- Carregar configs do preset
    local keybindsConfig = g_configs.create("/controls/keybinds/" .. preset .. ".otml")
    local hotkeysConfig = g_configs.create("/controls/hotkeys/" .. preset .. ".otml")
    
    -- Definir keybinds padrão
    keybindsConfig:setValue("movement.north", "Up")
    keybindsConfig:setValue("movement.south", "Down") 
    keybindsConfig:setValue("movement.east", "Right")
    keybindsConfig:setValue("movement.west", "Left")
    
    keybindsConfig:setValue("interface.inventory", "Ctrl+I")
    keybindsConfig:setValue("interface.spells", "Ctrl+S")
    keybindsConfig:setValue("interface.skills", "Ctrl+K")
    
    -- Salvar configurações
    keybindsConfig:save()
    hotkeysConfig:save()
end

-- Gerenciar presets
local function createControlsPreset(presetName)
    -- Adicionar à lista de presets
    local presets = g_settings.getList("controls-presets")
    table.insert(presets, presetName)
    g_settings.setList("controls-presets", presets)
    
    -- Criar arquivos de configuração
    local keybindsConfig = g_configs.create("/controls/keybinds/" .. presetName .. ".otml")
    local hotkeysConfig = g_configs.create("/controls/hotkeys/" .. presetName .. ".otml")
    
    -- Configurações padrão para novo preset
    setupDefaultKeybinds(keybindsConfig)
    setupDefaultHotkeys(hotkeysConfig)
    
    return presetName
end
```

#### Nível Advanced
```lua
-- Sistema de controles com múltiplos presets
-- Cada preset tem keybinds e hotkeys separados

-- Configuração de keybinds
local function setupKeybinds()
    local preset = Keybind.currentPreset or "Druid"
    
    -- Carregar configs do preset
    local keybindsConfig = g_configs.create("/controls/keybinds/" .. preset .. ".otml")
    local hotkeysConfig = g_configs.create("/controls/hotkeys/" .. preset .. ".otml")
    
    -- Definir keybinds padrão
    keybindsConfig:setValue("movement.north", "Up")
    keybindsConfig:setValue("movement.south", "Down") 
    keybindsConfig:setValue("movement.east", "Right")
    keybindsConfig:setValue("movement.west", "Left")
    
    keybindsConfig:setValue("interface.inventory", "Ctrl+I")
    keybindsConfig:setValue("interface.spells", "Ctrl+S")
    keybindsConfig:setValue("interface.skills", "Ctrl+K")
    
    -- Salvar configurações
    keybindsConfig:save()
    hotkeysConfig:save()
end

-- Gerenciar presets
local function createControlsPreset(presetName)
    -- Adicionar à lista de presets
    local presets = g_settings.getList("controls-presets")
    table.insert(presets, presetName)
    g_settings.setList("controls-presets", presets)
    
    -- Criar arquivos de configuração
    local keybindsConfig = g_configs.create("/controls/keybinds/" .. presetName .. ".otml")
    local hotkeysConfig = g_configs.create("/controls/hotkeys/" .. presetName .. ".otml")
    
    -- Configurações padrão para novo preset
    setupDefaultKeybinds(keybindsConfig)
    setupDefaultHotkeys(hotkeysConfig)
    
    return presetName
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

### 🔥 **Sistema de Hotkeys**

#### Inicialização e Configuração
```lua
-- Configuração de hotkeys
local function setupHotkeys(config)
    -- Hotkey para cura
    config:setNode("hotkey1", {
        key = "F1",
        action = HOTKEY_ACTION.SPELL,
        spell = "exura",
        text = "",
        parameter = ""
    })
    
    -- Hotkey para usar item em si mesmo
    config:setNode("hotkey2", {
        key = "F2", 
        action = HOTKEY_ACTION.USE_YOURSELF,
        itemId = 266,  -- health potion
        text = "",
        parameter = ""
    })
    
    -- Hotkey para texto automático
    config:setNode("hotkey3", {
        key = "F3",
        action = HOTKEY_ACTION.TEXT_AUTO,
        text = "utani hur",
        parameter = ""
    })
```

#### Funcionalidade 1
```lua
    
    -- Hotkey para usar item com crosshair
    config:setNode("hotkey4", {
        key = "F4",
        action = HOTKEY_ACTION.USE_CROSSHAIR,
        itemId = 3147,  -- blank rune
        text = "",
        parameter = ""
    })
    
    config:save()
end

-- Carregar hotkeys do preset atual
local function loadHotkeys()
    local preset = g_settings.getString("controls-preset-current") or "Druid"
    local config = g_configs.get("/controls/hotkeys/" .. preset .. ".otml")
    
    if not config:isLoaded() then
        return
    end
```

#### Finalização
```lua
    
    -- Processar cada hotkey
    for i = 1, 36 do  -- F1-F12, Shift+F1-F12, Ctrl+F1-F12
        local hotkeyNode = config:getNode("hotkey" .. i)
        if hotkeyNode then
            registerHotkey(hotkeyNode.key, hotkeyNode)
        end
    end
end
```

## 💡 Implementação Prática

### 🛠️ **Sistema de Profiles Personalizado**

#### Inicialização e Configuração
```lua
-- Sistema de perfis de usuário
local ProfileManager = {}

function ProfileManager.init()
    if not g_resources.directoryExists("/profiles") then
        g_resources.makeDir("/profiles")
    end
end

function ProfileManager.createProfile(profileName, baseSettings)
    local profilePath = "/profiles/" .. profileName .. ".otml"
    local config = g_configs.create(profilePath)
    
    -- Configurações padrão
    local defaultSettings = {
        graphics = {
            fullscreen = false,
            vsync = true,
            antialiasing = "2x",
            frameRate = 60
        },
```

#### Funcionalidade 1
```lua
        audio = {
            masterVolume = 0.8,
            musicVolume = 0.6,
            sfxVolume = 1.0
        },
        interface = {
            theme = "default",
            showFPS = false,
            showPing = true,
            language = "en"
        },
        game = {
            autoLogin = false,
            rememberAccount = true,
            classicControls = false
        }
    }
    
    -- Mesclar com configurações base se fornecidas
    if baseSettings then
        for category, settings in pairs(baseSettings) do
            if defaultSettings[category] then
                for key, value in pairs(settings) do
                    defaultSettings[category][key] = value
                end
```

#### Funcionalidade 2
```lua
            else
                defaultSettings[category] = settings
            end
        end
    end
    
    -- Salvar configurações no config
    for category, settings in pairs(defaultSettings) do
        config:setNode(category, settings)
    end
    
    config:save()
    return config
end

function ProfileManager.loadProfile(profileName)
    local profilePath = "/profiles/" .. profileName .. ".otml"
    local config = g_configs.get(profilePath)
    
    if not config or not config:isLoaded() then
        print("Perfil não encontrado:", profileName)
        return false
    end
```

#### Funcionalidade 3
```lua
    
    -- Aplicar configurações do perfil
    local graphics = config:getNode("graphics")
    if graphics then
        for key, value in pairs(graphics) do
            setOption("graphics." .. key, value)
        end
    end
    
    local audio = config:getNode("audio") 
    if audio then
        for key, value in pairs(audio) do
            setOption("audio." .. key, value)
        end
    end
    
    local interface = config:getNode("interface")
    if interface then
        for key, value in pairs(interface) do
            setOption("interface." .. key, value)
        end
```

#### Finalização
```lua
    end
    
    -- Marcar como perfil ativo
    g_settings.set("current.profile", profileName)
    
    return true
end

function ProfileManager.exportProfile(profileName, exportPath)
    local profilePath = "/profiles/" .. profileName .. ".otml"
    local config = g_configs.get(profilePath)
    
    if config and config:isLoaded() then
        -- Copiar arquivo de configuração
        local content = g_resources.readFileContents(profilePath)
        g_resources.writeFileContents(exportPath, content)
        return true
    end
    
    return false
end
```

### 🔧 **Sistema de Configuração Avançada**

#### Inicialização e Configuração
```lua
-- Configuração avançada com validação
local AdvancedConfig = {}

function AdvancedConfig.validateConfig(config, schema)
    for key, rules in pairs(schema) do
        if config:exists(key) then
            local value = config:getValue(key)
            
            -- Validar tipo
            if rules.type then
                local actualType = type(value)
                if rules.type == "number" then
                    value = tonumber(value)
                    if not value then
                        error("Valor inválido para " .. key .. ": deve ser número")
                    end
                elseif rules.type == "boolean" then
                    if value ~= "true" and value ~= "false" then
                        error("Valor inválido para " .. key .. ": deve ser true/false")
                    end
                end
```

#### Funcionalidade 1
```lua
            end
            
            -- Validar range para números
            if rules.min and tonumber(value) < rules.min then
                error("Valor muito baixo para " .. key .. ": mínimo " .. rules.min)
            end
            
            if rules.max and tonumber(value) > rules.max then
                error("Valor muito alto para " .. key .. ": máximo " .. rules.max)
            end
            
            -- Validar opções permitidas
            if rules.options then
                local found = false
                for _, option in ipairs(rules.options) do
                    if value == option then
                        found = true
                        break
                    end
                end
                if not found then
                    error("Valor inválido para " .. key .. ": deve ser um de " .. table.concat(rules.options, ", "))
                end
```

#### Funcionalidade 2
```lua
            end
        elseif rules.required then
            error("Configuração obrigatória ausente: " .. key)
        end
    end
end

-- Schema de validação
local configSchema = {
    ["graphics.frameRate"] = {
        type = "number",
        min = 30,
        max = 200,
        required = false
    },
    ["graphics.antialiasing"] = {
        type = "string",
        options = {"none", "2x", "4x", "8x"},
        required = false
    },
    ["audio.masterVolume"] = {
        type = "number", 
        min = 0.0,
        max = 1.0,
        required = false
    },
```

#### Funcionalidade 3
```lua
    ["interface.theme"] = {
        type = "string",
        options = {"default", "dark", "light", "classic"},
        required = false
    }
}

-- Aplicar validação
function AdvancedConfig.loadWithValidation(configPath)
    local config = g_configs.get(configPath)
    
    if config and config:isLoaded() then
        local success, error = pcall(AdvancedConfig.validateConfig, config, configSchema)
        
        if not success then
            print("Erro de validação:", error)
            return nil
        end
        
        return config
    end
```

#### Finalização
```lua
    
    return nil
end
```

## ✅ Melhores Práticas

### 🛡️ **Configuração Segura**

```lua
-- ✅ BOM: Sempre validar valores
    --  ✅ BOM: Sempre validar valores (traduzido)
local function setSafeOption(key, value, validator)
    if validator and not validator(value) then
    -- Verificação condicional
        print("Valor inválido para " .. key .. ":", value)
        return false
    end
    
    setOption(key, value)
    return true
end

-- ✅ BOM: Usar valores padrão
local function getOptionWithDefault(key, defaultValue)
    if g_settings.exists(key) then
    -- Verificação condicional
        return getOption(key)
    else
        setOption(key, defaultValue)
        return defaultValue
    end
end

-- ✅ BOM: Validadores específicos
local validators = {
    volume = function(value)
        local num = tonumber(value)
        return num and num >= 0 and num <= 1
    end,
    
    frameRate = function(value)
        local num = tonumber(value)
        return num and num >= 30 and num <= 200
    end,
    
    resolution = function(value)
        return value:match("^%d+x%d+$") ~= nil
    end
}

-- Uso seguro
    --  Uso seguro (traduzido)
setSafeOption("audio.volume", 0.8, validators.volume)
setSafeOption("graphics.frameRate", 60, validators.frameRate)
```

### ⚡ **Performance e Organização**

#### Nível Basic
```lua
-- ✅ BOM: Cache de configurações frequentes
local configCache = {}
local function getCachedOption(key)
    if not configCache[key] then
    end
end
local function setCachedOption(key, value)
end
-- ✅ BOM: Batch de configurações
local function applyConfigBatch(configs)
    end
    -- Salvar uma vez no final
end
-- ✅ BOM: Organização hierárquica
local function organizeConfigs()
    local gameConfigs = {
    local graphicsConfigs = {
end
```

#### Nível Intermediate
```lua
-- ✅ BOM: Cache de configurações frequentes
local configCache = {}

local function getCachedOption(key)
    if not configCache[key] then
        configCache[key] = getOption(key)
    end
    return configCache[key]
end

local function setCachedOption(key, value)
    configCache[key] = value
    setOption(key, value)
end

-- ✅ BOM: Batch de configurações
local function applyConfigBatch(configs)
    for key, value in pairs(configs) do
        setOption(key, value)
    end
    
    -- Salvar uma vez no final
    g_settings.save()
end

-- ✅ BOM: Organização hierárquica
local function organizeConfigs()
    local gameConfigs = {
        ["game.autoLogin"] = false,
        ["game.rememberAccount"] = true,
        ["game.classicControls"] = false
    }
    
    local graphicsConfigs = {
        ["graphics.fullscreen"] = false,
        ["graphics.vsync"] = true,
        ["graphics.antialiasing"] = "2x"
    }
    
    applyConfigBatch(gameConfigs)
    applyConfigBatch(graphicsConfigs)
end
```

#### Nível Advanced
```lua
-- ✅ BOM: Cache de configurações frequentes
local configCache = {}

local function getCachedOption(key)
    if not configCache[key] then
        configCache[key] = getOption(key)
    end
    return configCache[key]
end

local function setCachedOption(key, value)
    configCache[key] = value
    setOption(key, value)
end

-- ✅ BOM: Batch de configurações
local function applyConfigBatch(configs)
    for key, value in pairs(configs) do
        setOption(key, value)
    end
    
    -- Salvar uma vez no final
    g_settings.save()
end

-- ✅ BOM: Organização hierárquica
local function organizeConfigs()
    local gameConfigs = {
        ["game.autoLogin"] = false,
        ["game.rememberAccount"] = true,
        ["game.classicControls"] = false
    }
    
    local graphicsConfigs = {
        ["graphics.fullscreen"] = false,
        ["graphics.vsync"] = true,
        ["graphics.antialiasing"] = "2x"
    }
    
    applyConfigBatch(gameConfigs)
    applyConfigBatch(graphicsConfigs)
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

### 🔄 **Backup e Restauração**

```lua
-- ✅ BOM: Sistema de backup
    --  ✅ BOM: Sistema de backup (traduzido)
local function backupConfigs()
    local timestamp = os.date("%Y%m%d_%H%M%S")
    local backupDir = "/backups/" .. timestamp
    
    g_resources.makeDir(backupDir)
    
    -- Backup do settings principal
    --  Backup do settings principal (traduzido)
    local settingsContent = g_resources.readFileContents("/settings.otml")
    g_resources.writeFileContents(backupDir .. "/settings.otml", settingsContent)
    
    -- Backup dos controles
    --  Backup dos controles (traduzido)
    if g_resources.directoryExists("/controls") then
    -- Verificação condicional
        g_resources.copyDir("/controls", backupDir .. "/controls")
    end
    
    print("Backup criado em:", backupDir)
    return backupDir
end

-- ✅ BOM: Restauração de backup
local function restoreBackup(backupDir)
    if not g_resources.directoryExists(backupDir) then
    -- Verificação condicional
        print("Backup não encontrado:", backupDir)
        return false
    end
    
    -- Restaurar settings
    --  Restaurar settings (traduzido)
    local settingsContent = g_resources.readFileContents(backupDir .. "/settings.otml")
    if settingsContent then
    -- Verificação condicional
        g_resources.writeFileContents("/settings.otml", settingsContent)
        
        -- Recarregar configurações
        g_configs.unload("/settings.otml")
        g_configs.loadSettings("/settings.otml")
    end
    
    -- Restaurar controles
    --  Restaurar controles (traduzido)
    if g_resources.directoryExists(backupDir .. "/controls") then
    -- Verificação condicional
        g_resources.copyDir(backupDir .. "/controls", "/controls")
    end
    
    print("Backup restaurado de:", backupDir)
    return true
end
```

O sistema de configuração do OTClient oferece flexibilidade máxima para personalização e persistência de configurações, com suporte robusto para validação, backup e múltiplos perfis de usuário.

---

> [!success] Navegação
> - [[Getting_Started_Guide]] - Comece aqui
> - [[Module_System_Guide]] - Desenvolvimento de módulos
> - [[UI_System_Guide]] - Interface do usuário
> - [[Lua_API_Reference]] - Referência completa da API

