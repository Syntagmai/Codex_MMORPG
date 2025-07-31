---
title: Soundsystem
tags: [otclient, system, guide, documentation]
status: completed
aliases: [Soundsystem]
---

# Sistema de Som - OTClient Redemption

Documentação completa do sistema de áudio do OTClient, incluindo reprodução de sons, canais de áudio, efeitos sonoros e controle de volume.

## 📋 Índice

1. [Visão Geral](#-visão-geral)
2. [Sistema de Áudio](#-sistema-de-áudio)
3. [Canais de Som](#-canais-de-som)
4. [Reprodução de Sons](#-reprodução-de-sons)
5. [Controle de Volume](#-controle-de-volume)
6. [Efeitos Sonoros](#-efeitos-sonoros)
7. [Sons Ambientais](#-sons-ambientais)
8. [Integração com Jogo](#-integração-com-jogo)
9. [Configurações de Áudio](#-configurações-de-áudio)
10. [Exemplos Práticos](#-exemplos-práticos)

## 🎯 Visão Geral

O sistema de som do OTClient fornece uma API completa para reprodução de áudio, incluindo efeitos sonoros, música de fundo, sons ambientais e controle granular de volume através de múltiplos canais.

### Arquitetura do Sistema

```lua
-- Hierarquia do sistema de som
Audio Engine
├── g_sounds (Interface principal)
├── SoundChannels (Canais de áudio)
├── SoundEffects (Efeitos sonoros)
├── Audio Files (Arquivos de som)
└── Volume Control (Controle de volume)
```

### Canais de Áudio Predefinidos

```lua
-- Constantes de canais de som
SoundChannels = {
    Master = 0,        -- Canal principal
    Music = 1,         -- Música de fundo
    Effects = 2,       -- Efeitos sonoros
    Interface = 3,     -- Sons da interface
    Environment = 4,   -- Sons ambientais
    Voice = 5,         -- Voz/narração
    Bot = 6           -- Sons de bots/automação
}
```

## 🔊 Sistema de Áudio

### g_sounds - Interface Principal

```lua
-- Controle geral do áudio
g_sounds.enableAudio()                  -- Habilita sistema de áudio
g_sounds.disableAudio()                 -- Desabilita sistema de áudio
local enabled = g_sounds.isAudioEnabled() -- Verifica se áudio está habilitado

-- Parar todos os sons
g_sounds.stopAll()                      -- Para todos os sons imediatamente

-- Informações do sistema
local eaxEnabled = g_sounds.isEaxEnabled() -- Verifica suporte EAX

-- Posição 3D do ouvinte
g_sounds.setPosition(position)          -- Define posição do ouvinte
```

### Inicialização do Sistema

```lua
-- Inicializar sistema de áudio
function initializeAudioSystem()
    if not g_sounds.isAudioEnabled() then
        g_sounds.enableAudio()
        print("Sistema de áudio habilitado")
    end
    
    -- Carregar arquivos de som do cliente
    g_sounds.loadClientFiles('sounds/')
    
    -- Configurar canais de volume
    setupVolumeChannels()
    
    print("Sistema de áudio inicializado")
end

-- Verificar compatibilidade
function checkAudioCompatibility()
    local compatible = g_sounds.isAudioEnabled()
    local eax = g_sounds.isEaxEnabled()
    
    print("Áudio suportado:", compatible)
    print("EAX suportado:", eax)
    
    return compatible
end
```

## 📻 Canais de Som

### SoundChannel - Interface de Canal

```lua
-- Obter canal específico
local musicChannel = g_sounds.getChannel(SoundChannels.Music)
local effectsChannel = g_sounds.getChannel(SoundChannels.Effects)
local interfaceChannel = g_sounds.getChannel(SoundChannels.Interface)

-- Controle do canal
musicChannel:enable()                   -- Habilita canal
musicChannel:disable()                  -- Desabilita canal
local enabled = musicChannel:isEnabled() -- Verifica se habilitado

-- Controle de volume do canal
musicChannel:setGain(0.8)               -- Define volume (0.0 - 1.0)
local gain = musicChannel:getGain()     -- Obtém volume atual

-- Reprodução no canal
musicChannel:play(fileName, fadeTime, gain, pitch)
musicChannel:stop(fadeTime)             -- Para reprodução
musicChannel:enqueue(fileName, fadeTime, gain, pitch) -- Adiciona à fila

-- Estados do canal
local playing = musicChannel:isPlaying() -- Está reproduzindo
local buffering = musicChannel:isBuffering() -- Está carregando
```

### Gerenciamento de Canais

```lua
-- Configurar todos os canais
function setupVolumeChannels()
    local channels = {
        {id = SoundChannels.Music, gain = 0.7, name = "Music"},
        {id = SoundChannels.Effects, gain = 0.9, name = "Effects"},
        {id = SoundChannels.Interface, gain = 0.8, name = "Interface"},
        {id = SoundChannels.Environment, gain = 0.6, name = "Environment"},
        {id = SoundChannels.Voice, gain = 1.0, name = "Voice"}
    }
    
    for _, channelInfo in ipairs(channels) do
        local channel = g_sounds.getChannel(channelInfo.id)
        if channel then
            channel:enable()
            channel:setGain(channelInfo.gain)
            print("Canal configurado:", channelInfo.name, "Volume:", channelInfo.gain)
        end
    end
end

-- Silenciar todos os canais
function muteAllChannels()
    for channelId = SoundChannels.Master, SoundChannels.Bot do
        local channel = g_sounds.getChannel(channelId)
        if channel then
            channel:setGain(0.0)
        end
    end
end

-- Restaurar volumes dos canais
function restoreChannelVolumes()
    local volumes = {
        [SoundChannels.Music] = 0.7,
        [SoundChannels.Effects] = 0.9,
        [SoundChannels.Interface] = 0.8,
        [SoundChannels.Environment] = 0.6,
        [SoundChannels.Voice] = 1.0
    }
    
    for channelId, volume in pairs(volumes) do
        local channel = g_sounds.getChannel(channelId)
        if channel then
            channel:setGain(volume)
        end
    end
end
```

## 🎵 Reprodução de Sons

### Reprodução Básica

```lua
-- Reprodução simples
g_sounds.play("sounds/click.ogg")       -- Som simples
g_sounds.play("sounds/music.ogg", 1000) -- Com fade in de 1 segundo

-- Reprodução com parâmetros
g_sounds.play(fileName, fadeTime, gain, pitch)
-- fileName: caminho do arquivo
-- fadeTime: tempo de fade in/out em ms
-- gain: volume (0.0 - 1.0)
-- pitch: pitch/velocidade (0.5 - 2.0)

-- Pré-carregar som
g_sounds.preload("sounds/explosion.ogg") -- Carrega na memória

-- Reprodução em canal específico
local effectsChannel = g_sounds.getChannel(SoundChannels.Effects)
effectsChannel:play("sounds/sword_hit.ogg", 0, 1.0, 1.0)
```

### Fila de Reprodução

```lua
-- Enfileirar sons para reprodução sequencial
local musicChannel = g_sounds.getChannel(SoundChannels.Music)

musicChannel:enqueue("sounds/intro.ogg", 1000, 0.8, 1.0)
musicChannel:enqueue("sounds/main_theme.ogg", 2000, 0.8, 1.0)
musicChannel:enqueue("sounds/outro.ogg", 1000, 0.8, 1.0)

-- Playlist de música
function playMusicPlaylist(playlist)
    local musicChannel = g_sounds.getChannel(SoundChannels.Music)
    musicChannel:stop(1000) -- Para música atual com fade out
    
    for i, track in ipairs(playlist) do
        local fadeTime = i == 1 and 2000 or 0 -- Fade in apenas na primeira
        musicChannel:enqueue(track.file, fadeTime, track.volume or 0.8, track.pitch or 1.0)
    end
end

-- Exemplo de playlist
local gameplayPlaylist = {
    {file = "sounds/music/ambient1.ogg", volume = 0.6},
    {file = "sounds/music/ambient2.ogg", volume = 0.7},
    {file = "sounds/music/combat.ogg", volume = 0.8, pitch = 1.1}
}

playMusicPlaylist(gameplayPlaylist)
```

## 🔈 Controle de Volume

### Volume Global

```lua
-- Controle do volume master
function setMasterVolume(volume)
    local masterChannel = g_sounds.getChannel(SoundChannels.Master)
    if masterChannel then
        masterChannel:setGain(volume)
    end
end

function getMasterVolume()
    local masterChannel = g_sounds.getChannel(SoundChannels.Master)
    return masterChannel and masterChannel:getGain() or 0.0
end

-- Fade global
function fadeToVolume(targetVolume, duration)
    local masterChannel = g_sounds.getChannel(SoundChannels.Master)
    if not masterChannel then return end
    
    local startVolume = masterChannel:getGain()
    local startTime = g_clock.millis()
    local updateEvent
    
    local function updateFade()
        local elapsed = g_clock.millis() - startTime
        local progress = math.min(elapsed / duration, 1.0)
        
        local currentVolume = startVolume + (targetVolume - startVolume) * progress
        masterChannel:setGain(currentVolume)
        
        if progress < 1.0 then
            updateEvent = scheduleEvent(updateFade, 50)
        end
    end
    
    updateEvent = scheduleEvent(updateFade, 50)
    return updateEvent
end
```

### Volume por Canal

```lua
-- Configurações de volume por categoria
local VolumeSettings = {
    master = 1.0,
    music = 0.7,
    effects = 0.9,
    interface = 0.8,
    environment = 0.6,
    voice = 1.0
}

-- Aplicar configurações de volume
function applyVolumeSettings(settings)
    settings = settings or VolumeSettings
    
    local channels = {
        [SoundChannels.Master] = settings.master,
        [SoundChannels.Music] = settings.music,
        [SoundChannels.Effects] = settings.effects,
        [SoundChannels.Interface] = settings.interface,
        [SoundChannels.Environment] = settings.environment,
        [SoundChannels.Voice] = settings.voice
    }
    
    for channelId, volume in pairs(channels) do
        local channel = g_sounds.getChannel(channelId)
        if channel then
            channel:setGain(volume)
        end
    end
end

-- Salvar configurações de volume
function saveVolumeSettings()
    local settings = {}
    
    local channels = {
        master = SoundChannels.Master,
        music = SoundChannels.Music,
        effects = SoundChannels.Effects,
        interface = SoundChannels.Interface,
        environment = SoundChannels.Environment,
        voice = SoundChannels.Voice
    }
    
    for name, channelId in pairs(channels) do
        local channel = g_sounds.getChannel(channelId)
        settings[name] = channel and channel:getGain() or 0.0
    end
    
    g_settings.setNode('audio.volumes', settings)
    g_settings.save()
end

-- Carregar configurações de volume
function loadVolumeSettings()
    local settings = g_settings.getNode('audio.volumes') or VolumeSettings
    applyVolumeSettings(settings)
end
```

## ✨ Efeitos Sonoros

### Sons de Interface

```lua
-- Sons de UI comuns
local InterfaceSounds = {
    click = "sounds/ui/click.ogg",
    hover = "sounds/ui/hover.ogg",
    open = "sounds/ui/window_open.ogg",
    close = "sounds/ui/window_close.ogg",
    error = "sounds/ui/error.ogg",
    success = "sounds/ui/success.ogg",
    notification = "sounds/ui/notification.ogg"
}

-- Reproduzir som de interface
function playInterfaceSound(soundType)
    local soundFile = InterfaceSounds[soundType]
    if not soundFile then return end
    
    local interfaceChannel = g_sounds.getChannel(SoundChannels.Interface)
    if interfaceChannel then
        interfaceChannel:play(soundFile, 0, 1.0, 1.0)
    end
end

-- Conectar sons à interface
function setupInterfaceSounds()
    -- Som de clique para todos os botões
    connect(UIButton, {
        onClick = function()
            playInterfaceSound('click')
        end
    })
    
    -- Som de hover
    connect(UIButton, {
        onHoverChange = function(widget, hovered)
            if hovered then
                playInterfaceSound('hover')
            end
        end
    })
    
    -- Sons de janela
    connect(UIWindow, {
        onVisibilityChange = function(window, visible)
            if visible then
                playInterfaceSound('open')
            else
                playInterfaceSound('close')
            end
        end
    })
end
```

### Sons de Jogo

```lua
-- Sons de combate
local CombatSounds = {
    sword_hit = "sounds/combat/sword_hit.ogg",
    magic_missile = "sounds/combat/magic_missile.ogg",
    explosion = "sounds/combat/explosion.ogg",
    heal = "sounds/combat/heal.ogg",
    death = "sounds/combat/death.ogg"
}

-- Sons de movimento
local MovementSounds = {
    walk_grass = "sounds/movement/walk_grass.ogg",
    walk_stone = "sounds/movement/walk_stone.ogg",
    walk_water = "sounds/movement/walk_water.ogg",
    teleport = "sounds/movement/teleport.ogg"
}

-- Reproduzir som de combate
function playCombatSound(soundType, position)
    local soundFile = CombatSounds[soundType]
    if not soundFile then return end
    
    local effectsChannel = g_sounds.getChannel(SoundChannels.Effects)
    if effectsChannel then
        -- Som com posição 3D se fornecida
        if position then
            g_sounds.setPosition(position)
        end
        effectsChannel:play(soundFile, 0, 1.0, 1.0)
    end
end

-- Integração com eventos do jogo
function setupGameSounds()
    connect(g_game, {
        onCreatureMove = function(creature, newPos, oldPos)
            if creature:isLocalPlayer() then
                -- Determinar tipo de terreno e tocar som apropriado
                local tile = g_map.getTile(newPos)
                if tile then
                    local ground = tile:getGround()
                    if ground then
                        local terrainType = getTerrainType(ground:getId())
                        playMovementSound(terrainType)
                    end
                end
            end
        end,
        
        onMissileAppear = function(missile)
            -- Som baseado no tipo de míssil
            local missileType = getMissileType(missile:getId())
            playCombatSound(missileType)
        end,
        
        onAnimatedTextAppear = function(animatedText)
            -- Sons para diferentes tipos de texto animado
            local textType = animatedText:getType()
            if textType == AnimatedTextType.Damage then
                playCombatSound('sword_hit')
            elseif textType == AnimatedTextType.Heal then
                playCombatSound('heal')
            end
        end
    })
end
```

## 🌍 Sons Ambientais

### Sistema de Som Ambiental

```lua
-- Sons ambientais por localização
local AmbientSounds = {
    forest = {
        file = "sounds/ambient/forest.ogg",
        volume = 0.4,
        loop = true
    },
    city = {
        file = "sounds/ambient/city.ogg",
        volume = 0.3,
        loop = true
    },
    dungeon = {
        file = "sounds/ambient/dungeon.ogg",
        volume = 0.5,
        loop = true
    },
    cave = {
        file = "sounds/ambient/cave.ogg",
        volume = 0.6,
        loop = true
    }
}

-- Gerenciador de som ambiental
local AmbientManager = {
    currentAmbient = nil,
    environmentChannel = nil
}

function AmbientManager.init()
    AmbientManager.environmentChannel = g_sounds.getChannel(SoundChannels.Environment)
    
    connect(g_game, {
        onLocalPlayerPositionChange = AmbientManager.onPositionChange
    })
end

function AmbientManager.onPositionChange(localPlayer, newPos, oldPos)
    local newAmbient = AmbientManager.detectAmbientZone(newPos)
    
    if newAmbient ~= AmbientManager.currentAmbient then
        AmbientManager.changeAmbient(newAmbient)
        AmbientManager.currentAmbient = newAmbient
    end
end

function AmbientManager.detectAmbientZone(position)
    -- Detectar zona baseada na posição
    -- Esta seria uma lógica específica do jogo
    if position.z <= 6 then
        return 'city'
    elseif position.z == 7 then
        return 'forest'
    elseif position.z >= 8 then
        return 'dungeon'
    end
    
    return nil
end

function AmbientManager.changeAmbient(ambientType)
    if not AmbientManager.environmentChannel then return end
    
    -- Fade out som atual
    AmbientManager.environmentChannel:stop(2000)
    
    if ambientType and AmbientSounds[ambientType] then
        local ambient = AmbientSounds[ambientType]
        
        scheduleEvent(function()
            AmbientManager.environmentChannel:play(
                ambient.file,
                2000, -- Fade in
                ambient.volume,
                1.0
            )
        end, 1000) -- Delay para fade out completar
        
        print("Som ambiental alterado para:", ambientType)
    end
end
```

## 🎮 Integração com Jogo

### Sistema de Notificações Sonoras

```lua
-- Sons de notificação
local NotificationSounds = {
    message = "sounds/notifications/message.ogg",
    trade = "sounds/notifications/trade.ogg",
    party_invite = "sounds/notifications/party.ogg",
    level_up = "sounds/notifications/levelup.ogg",
    death = "sounds/notifications/death.ogg",
    login = "sounds/notifications/login.ogg",
    logout = "sounds/notifications/logout.ogg"
}

-- Reproduzir notificação
function playNotificationSound(type)
    local soundFile = NotificationSounds[type]
    if not soundFile then return end
    
    local interfaceChannel = g_sounds.getChannel(SoundChannels.Interface)
    if interfaceChannel then
        interfaceChannel:play(soundFile, 0, 1.0, 1.0)
    end
end

-- Integrar com eventos do jogo
function setupGameNotifications()
    connect(g_game, {
        onTalk = function(name, level, mode, message, channelId, pos)
            if mode == TalkType.PrivateFrom then
                playNotificationSound('message')
            end
        end,
        
        onTradeRequest = function()
            playNotificationSound('trade')
        end,
        
        onPartyInvite = function()
            playNotificationSound('party_invite')
        end,
        
        onLocalPlayerLevelChange = function(localPlayer, level)
            playNotificationSound('level_up')
        end,
        
        onLocalPlayerDeath = function()
            playNotificationSound('death')
        end,
        
        onGameStart = function()
            playNotificationSound('login')
        end,
        
        onGameEnd = function()
            playNotificationSound('logout')
        end
    })
end
```

### Sistema de Feedback Sonoro

```lua
-- Feedback sonoro para ações
local ActionSounds = {
    spell_cast = "sounds/actions/spell_cast.ogg",
    item_use = "sounds/actions/item_use.ogg",
    door_open = "sounds/actions/door_open.ogg",
    chest_open = "sounds/actions/chest_open.ogg",
    buy_item = "sounds/actions/buy.ogg",
    sell_item = "sounds/actions/sell.ogg"
}

-- Reproduzir feedback sonoro
function playActionFeedback(action, success)
    local soundFile = ActionSounds[action]
    if not soundFile then return end
    
    local effectsChannel = g_sounds.getChannel(SoundChannels.Effects)
    if effectsChannel then
        local pitch = success and 1.0 or 0.8 -- Pitch mais baixo para falha
        effectsChannel:play(soundFile, 0, 1.0, pitch)
    end
end

-- Integrar com protocolo
function setupActionFeedback()
    -- Esta seria uma integração com o sistema de protocolo
    -- para detectar ações e seu resultado
    
    connect(g_game, {
        onSpellCast = function(spell, success)
            playActionFeedback('spell_cast', success)
        end,
        
        onItemUse = function(item, success)
            playActionFeedback('item_use', success)
        end,
        
        onContainerOpen = function(container)
            if container:getItem():getId() == 1740 then -- chest
                playActionFeedback('chest_open', true)
            end
        end
    })
end
```

## ⚙️ Configurações de Áudio

### Interface de Configurações

```lua
-- Sistema de configurações de áudio
local AudioSettings = {
    enabled = true,
    masterVolume = 1.0,
    musicVolume = 0.7,
    effectsVolume = 0.9,
    interfaceVolume = 0.8,
    environmentVolume = 0.6,
    voiceVolume = 1.0,
    enableAmbient = true,
    enableNotifications = true,
    enableFeedback = true
}

-- Aplicar todas as configurações
function applyAudioSettings(settings)
    settings = settings or AudioSettings
    
    -- Habilitar/desabilitar áudio
    if settings.enabled then
        g_sounds.enableAudio()
    else
        g_sounds.disableAudio()
        return
    end
    
    -- Aplicar volumes
    local volumes = {
        [SoundChannels.Master] = settings.masterVolume,
        [SoundChannels.Music] = settings.musicVolume,
        [SoundChannels.Effects] = settings.effectsVolume,
        [SoundChannels.Interface] = settings.interfaceVolume,
        [SoundChannels.Environment] = settings.environmentVolume,
        [SoundChannels.Voice] = settings.voiceVolume
    }
    
    for channelId, volume in pairs(volumes) do
        local channel = g_sounds.getChannel(channelId)
        if channel then
            channel:setGain(volume)
        end
    end
    
    -- Configurações específicas
    if not settings.enableAmbient then
        local envChannel = g_sounds.getChannel(SoundChannels.Environment)
        if envChannel then
            envChannel:stop()
        end
    end
end

-- Salvar configurações
function saveAudioSettings(settings)
    g_settings.setNode('audio', settings or AudioSettings)
    g_settings.save()
end

-- Carregar configurações
function loadAudioSettings()
    local settings = g_settings.getNode('audio') or AudioSettings
    applyAudioSettings(settings)
    return settings
end

-- Configurações predefinidas
local AudioPresets = {
    silent = {
        enabled = false,
        masterVolume = 0.0
    },
    
    minimal = {
        enabled = true,
        masterVolume = 0.3,
        musicVolume = 0.1,
        effectsVolume = 0.5,
        interfaceVolume = 0.7,
        environmentVolume = 0.0,
        enableAmbient = false
    },
    
    balanced = {
        enabled = true,
        masterVolume = 0.8,
        musicVolume = 0.6,
        effectsVolume = 0.8,
        interfaceVolume = 0.7,
        environmentVolume = 0.4,
        enableAmbient = true
    },
    
    immersive = {
        enabled = true,
        masterVolume = 1.0,
        musicVolume = 0.8,
        effectsVolume = 1.0,
        interfaceVolume = 0.6,
        environmentVolume = 0.8,
        enableAmbient = true
    }
}

-- Aplicar preset
function applyAudioPreset(presetName)
    local preset = AudioPresets[presetName]
    if preset then
        applyAudioSettings(preset)
        saveAudioSettings(preset)
        print("Preset de áudio aplicado:", presetName)
    end
end
```

## 💡 Exemplos Práticos

### Exemplo 1: Gerenciador de Áudio

```lua
-- modules/audio_manager/audio_manager.lua
audioManager = {}

function audioManager.init()
    audioManager.settings = {}
    audioManager.window = g_ui.displayUI('audio_manager')
    audioManager.setupInterface()
    audioManager.loadSettings()
    
    -- Inicializar sistema de áudio
    if not g_sounds.isAudioEnabled() then
        g_sounds.enableAudio()
    end
    
    audioManager.setupChannels()
    audioManager.setupGameIntegration()
end

function audioManager.setupInterface()
    -- Sliders de volume
    audioManager.masterSlider = audioManager.window:getChildById('masterSlider')
    audioManager.musicSlider = audioManager.window:getChildById('musicSlider')
    audioManager.effectsSlider = audioManager.window:getChildById('effectsSlider')
    audioManager.interfaceSlider = audioManager.window:getChildById('interfaceSlider')
    audioManager.environmentSlider = audioManager.window:getChildById('environmentSlider')
    
    -- Checkboxes
    audioManager.enabledBox = audioManager.window:getChildById('enabledBox')
    audioManager.ambientBox = audioManager.window:getChildById('ambientBox')
    audioManager.notificationsBox = audioManager.window:getChildById('notificationsBox')
    
    -- Botões
    audioManager.testButton = audioManager.window:getChildById('testButton')
    audioManager.muteButton = audioManager.window:getChildById('muteButton')
    audioManager.presetCombo = audioManager.window:getChildById('presetCombo')
    
    -- Eventos
    audioManager.masterSlider.onValueChange = audioManager.onMasterVolumeChange
    audioManager.musicSlider.onValueChange = audioManager.onMusicVolumeChange
    audioManager.effectsSlider.onValueChange = audioManager.onEffectsVolumeChange
    audioManager.interfaceSlider.onValueChange = audioManager.onInterfaceVolumeChange
    audioManager.environmentSlider.onValueChange = audioManager.onEnvironmentVolumeChange
    
    audioManager.enabledBox.onCheckChange = audioManager.onEnabledChange
    audioManager.ambientBox.onCheckChange = audioManager.onAmbientChange
    audioManager.notificationsBox.onCheckChange = audioManager.onNotificationsChange
    
    audioManager.testButton.onClick = audioManager.playTestSounds
    audioManager.muteButton.onClick = audioManager.toggleMute
    audioManager.presetCombo.onOptionChange = audioManager.onPresetChange
    
    -- Configurar presets
    audioManager.presetCombo:addOption('Personalizado', 'custom')
    audioManager.presetCombo:addOption('Silencioso', 'silent')
    audioManager.presetCombo:addOption('Mínimo', 'minimal')
    audioManager.presetCombo:addOption('Balanceado', 'balanced')
    audioManager.presetCombo:addOption('Imersivo', 'immersive')
end

function audioManager.onMasterVolumeChange(slider, value)
    local volume = value / 100.0
    audioManager.settings.masterVolume = volume
    
    local masterChannel = g_sounds.getChannel(SoundChannels.Master)
    if masterChannel then
        masterChannel:setGain(volume)
    end
    
    audioManager.updateVolumeLabel('masterLabel', volume)
end

function audioManager.onMusicVolumeChange(slider, value)
    local volume = value / 100.0
    audioManager.settings.musicVolume = volume
    
    local musicChannel = g_sounds.getChannel(SoundChannels.Music)
    if musicChannel then
        musicChannel:setGain(volume)
    end
    
    audioManager.updateVolumeLabel('musicLabel', volume)
end

function audioManager.onEffectsVolumeChange(slider, value)
    local volume = value / 100.0
    audioManager.settings.effectsVolume = volume
    
    local effectsChannel = g_sounds.getChannel(SoundChannels.Effects)
    if effectsChannel then
        effectsChannel:setGain(volume)
    end
    
    audioManager.updateVolumeLabel('effectsLabel', volume)
end

function audioManager.updateVolumeLabel(labelId, volume)
    local label = audioManager.window:getChildById(labelId)
    if label then
        label:setText(string.format('%d%%', math.floor(volume * 100)))
    end
end

function audioManager.onEnabledChange(checkbox, checked)
    audioManager.settings.enabled = checked
    
    if checked then
        g_sounds.enableAudio()
        audioManager.applyAllSettings()
    else
        g_sounds.disableAudio()
    end
    
    audioManager.updateInterfaceState()
end

function audioManager.updateInterfaceState()
    local enabled = audioManager.settings.enabled
    
    -- Habilitar/desabilitar controles baseado no estado do áudio
    audioManager.masterSlider:setEnabled(enabled)
    audioManager.musicSlider:setEnabled(enabled)
    audioManager.effectsSlider:setEnabled(enabled)
    audioManager.interfaceSlider:setEnabled(enabled)
    audioManager.environmentSlider:setEnabled(enabled)
    audioManager.testButton:setEnabled(enabled)
end

function audioManager.playTestSounds()
    -- Tocar sons de teste para cada canal
    local testSounds = {
        {channel = SoundChannels.Music, file = "sounds/test/music_test.ogg"},
        {channel = SoundChannels.Effects, file = "sounds/test/effect_test.ogg"},
        {channel = SoundChannels.Interface, file = "sounds/test/interface_test.ogg"},
        {channel = SoundChannels.Environment, file = "sounds/test/ambient_test.ogg"}
    }
    
    for i, test in ipairs(testSounds) do
        scheduleEvent(function()
            local channel = g_sounds.getChannel(test.channel)
            if channel and g_resources.fileExists(test.file) then
                channel:play(test.file, 0, 1.0, 1.0)
            end
        end, i * 1000) -- 1 segundo entre cada teste
    end
end

function audioManager.toggleMute()
    local currentVolume = audioManager.settings.masterVolume
    
    if currentVolume > 0 then
        -- Salvar volume atual e mutar
        audioManager.previousVolume = currentVolume
        audioManager.onMasterVolumeChange(audioManager.masterSlider, 0)
        audioManager.masterSlider:setValue(0)
        audioManager.muteButton:setText('Unmute')
    else
        -- Restaurar volume anterior
        local restoreVolume = audioManager.previousVolume or 80
        audioManager.onMasterVolumeChange(audioManager.masterSlider, restoreVolume)
        audioManager.masterSlider:setValue(restoreVolume)
        audioManager.muteButton:setText('Mute')
    end
end

function audioManager.onPresetChange(combo, option)
    local presetName = option.data
    if presetName ~= 'custom' then
        audioManager.applyPreset(presetName)
    end
end

function audioManager.applyPreset(presetName)
    local presets = {
        silent = {enabled = false, masterVolume = 0.0},
        minimal = {
            enabled = true,
            masterVolume = 0.3,
            musicVolume = 0.1,
            effectsVolume = 0.5,
            interfaceVolume = 0.7,
            environmentVolume = 0.0
        },
        balanced = {
            enabled = true,
            masterVolume = 0.8,
            musicVolume = 0.6,
            effectsVolume = 0.8,
            interfaceVolume = 0.7,
            environmentVolume = 0.4
        },
        immersive = {
            enabled = true,
            masterVolume = 1.0,
            musicVolume = 0.8,
            effectsVolume = 1.0,
            interfaceVolume = 0.6,
            environmentVolume = 0.8
        }
    }
    
    local preset = presets[presetName]
    if preset then
        -- Aplicar preset
        for key, value in pairs(preset) do
            audioManager.settings[key] = value
        end
        
        audioManager.applyAllSettings()
        audioManager.updateInterface()
        audioManager.saveSettings()
        
        modules.game_textmessage.displayGameMessage('Preset aplicado: ' .. presetName)
    end
end

function audioManager.applyAllSettings()
    if not audioManager.settings.enabled then
        g_sounds.disableAudio()
        return
    end
    
    g_sounds.enableAudio()
    
    -- Aplicar volumes
    local channels = {
        [SoundChannels.Master] = audioManager.settings.masterVolume,
        [SoundChannels.Music] = audioManager.settings.musicVolume,
        [SoundChannels.Effects] = audioManager.settings.effectsVolume,
        [SoundChannels.Interface] = audioManager.settings.interfaceVolume,
        [SoundChannels.Environment] = audioManager.settings.environmentVolume
    }
    
    for channelId, volume in pairs(channels) do
        local channel = g_sounds.getChannel(channelId)
        if channel then
            channel:setGain(volume or 0.0)
        end
    end
end

function audioManager.updateInterface()
    -- Atualizar sliders
    audioManager.masterSlider:setValue((audioManager.settings.masterVolume or 0) * 100)
    audioManager.musicSlider:setValue((audioManager.settings.musicVolume or 0) * 100)
    audioManager.effectsSlider:setValue((audioManager.settings.effectsVolume or 0) * 100)
    audioManager.interfaceSlider:setValue((audioManager.settings.interfaceVolume or 0) * 100)
    audioManager.environmentSlider:setValue((audioManager.settings.environmentVolume or 0) * 100)
    
    -- Atualizar checkboxes
    audioManager.enabledBox:setChecked(audioManager.settings.enabled or false)
    audioManager.ambientBox:setChecked(audioManager.settings.enableAmbient or false)
    audioManager.notificationsBox:setChecked(audioManager.settings.enableNotifications or false)
    
    audioManager.updateInterfaceState()
end

function audioManager.setupChannels()
    -- Configurar todos os canais
    local channels = {
        SoundChannels.Master,
        SoundChannels.Music,
        SoundChannels.Effects,
        SoundChannels.Interface,
        SoundChannels.Environment,
        SoundChannels.Voice
    }
    
    for _, channelId in ipairs(channels) do
        local channel = g_sounds.getChannel(channelId)
        if channel then
            channel:enable()
        end
    end
end

function audioManager.setupGameIntegration()
    -- Integrar com eventos do jogo
    connect(g_game, {
        onGameStart = function()
            audioManager.playNotification('login')
        end,
        
        onGameEnd = function()
            audioManager.playNotification('logout')
        end,
        
        onTalk = function(name, level, mode, message, channelId, pos)
            if mode == TalkType.PrivateFrom and audioManager.settings.enableNotifications then
                audioManager.playNotification('message')
            end
        end
    })
end

function audioManager.playNotification(type)
    if not audioManager.settings.enableNotifications then return end
    
    local sounds = {
        login = "sounds/notifications/login.ogg",
        logout = "sounds/notifications/logout.ogg",
        message = "sounds/notifications/message.ogg"
    }
    
    local soundFile = sounds[type]
    if soundFile and g_resources.fileExists(soundFile) then
        local interfaceChannel = g_sounds.getChannel(SoundChannels.Interface)
        if interfaceChannel then
            interfaceChannel:play(soundFile, 0, 1.0, 1.0)
        end
    end
end

function audioManager.loadSettings()
    audioManager.settings = g_settings.getNode('audioManager') or {
        enabled = true,
        masterVolume = 0.8,
        musicVolume = 0.6,
        effectsVolume = 0.8,
        interfaceVolume = 0.7,
        environmentVolume = 0.4,
        enableAmbient = true,
        enableNotifications = true
    }
    
    audioManager.applyAllSettings()
    audioManager.updateInterface()
end

function audioManager.saveSettings()
    g_settings.setNode('audioManager', audioManager.settings)
    g_settings.save()
end

function audioManager.terminate()
    audioManager.saveSettings()
    g_sounds.stopAll()
end
```

### Exemplo 2: Sistema de Música Dinâmica

```lua
-- modules/dynamic_music/dynamic_music.lua
dynamicMusic = {}

function dynamicMusic.init()
    dynamicMusic.currentTrack = nil
    dynamicMusic.musicLibrary = {}
    dynamicMusic.fadeEvents = {}
    
    dynamicMusic.loadMusicLibrary()
    dynamicMusic.setupGameIntegration()
end

function dynamicMusic.loadMusicLibrary()
    dynamicMusic.musicLibrary = {
        ambient = {
            files = {
                "sounds/music/ambient1.ogg",
                "sounds/music/ambient2.ogg",
                "sounds/music/ambient3.ogg"
            },
            volume = 0.6,
            fadeTime = 3000
        },
        
        combat = {
            files = {
                "sounds/music/combat1.ogg",
                "sounds/music/combat2.ogg"
            },
            volume = 0.8,
            fadeTime = 1500
        },
        
        city = {
            files = {
                "sounds/music/city1.ogg",
                "sounds/music/city2.ogg"
            },
            volume = 0.5,
            fadeTime = 2000
        },
        
        dungeon = {
            files = {
                "sounds/music/dungeon1.ogg",
                "sounds/music/dungeon2.ogg"
            },
            volume = 0.7,
            fadeTime = 2500
        }
    }
end

function dynamicMusic.setupGameIntegration()
    connect(g_game, {
        onGameStart = dynamicMusic.onGameStart,
        onGameEnd = dynamicMusic.onGameEnd,
        onAttackingCreatureChange = dynamicMusic.onCombatChange,
        onLocalPlayerPositionChange = dynamicMusic.onPositionChange
    })
end

function dynamicMusic.onGameStart()
    dynamicMusic.startAmbientMusic()
end

function dynamicMusic.onGameEnd()
    dynamicMusic.stopAllMusic()
end

function dynamicMusic.onCombatChange(creature, oldCreature)
    if creature then
        -- Entrou em combate
        dynamicMusic.switchToMusic('combat')
    else
        -- Saiu de combate
        dynamicMusic.switchToAmbientMusic()
    end
end

function dynamicMusic.onPositionChange(localPlayer, newPos, oldPos)
    local musicType = dynamicMusic.getMusicTypeForPosition(newPos)
    
    if musicType ~= dynamicMusic.currentTrack then
        dynamicMusic.switchToMusic(musicType)
    end
end

function dynamicMusic.getMusicTypeForPosition(position)
    -- Determinar tipo de música baseado na posição
    if position.z <= 6 then
        return 'city'
    elseif position.z == 7 then
        return 'ambient'
    elseif position.z >= 8 then
        return 'dungeon'
    end
    
    return 'ambient'
end

function dynamicMusic.switchToMusic(musicType)
    if musicType == dynamicMusic.currentTrack then return end
    
    local musicChannel = g_sounds.getChannel(SoundChannels.Music)
    if not musicChannel then return end
    
    local musicData = dynamicMusic.musicLibrary[musicType]
    if not musicData then return end
    
    -- Fade out música atual
    if dynamicMusic.currentTrack then
        musicChannel:stop(musicData.fadeTime)
    end
    
    -- Selecionar arquivo aleatório
    local files = musicData.files
    local selectedFile = files[math.random(1, #files)]
    
    -- Verificar se arquivo existe
    if not g_resources.fileExists(selectedFile) then
        print("Arquivo de música não encontrado:", selectedFile)
        return
    end
    
    -- Fade in nova música
    scheduleEvent(function()
        musicChannel:play(
            selectedFile,
            musicData.fadeTime,
            musicData.volume,
            1.0
        )
        dynamicMusic.currentTrack = musicType
        print("Música alterada para:", musicType, "-", selectedFile)
    end, musicData.fadeTime / 2)
end

function dynamicMusic.switchToAmbientMusic()
    local player = g_game.getLocalPlayer()
    if player then
        local musicType = dynamicMusic.getMusicTypeForPosition(player:getPosition())
        dynamicMusic.switchToMusic(musicType)
    else
        dynamicMusic.switchToMusic('ambient')
    end
end

function dynamicMusic.startAmbientMusic()
    dynamicMusic.switchToAmbientMusic()
end

function dynamicMusic.stopAllMusic()
    local musicChannel = g_sounds.getChannel(SoundChannels.Music)
    if musicChannel then
        musicChannel:stop(2000)
    end
    
    dynamicMusic.currentTrack = nil
end

function dynamicMusic.setMusicVolume(volume)
    local musicChannel = g_sounds.getChannel(SoundChannels.Music)
    if musicChannel then
        musicChannel:setGain(volume)
    end
    
    -- Atualizar volumes na biblioteca
    for _, musicData in pairs(dynamicMusic.musicLibrary) do
        musicData.volume = volume
    end
end

function dynamicMusic.addMusicTrack(category, file, volume)
    if not dynamicMusic.musicLibrary[category] then
        dynamicMusic.musicLibrary[category] = {
            files = {},
            volume = volume or 0.6,
            fadeTime = 2000
        }
    end
    
    table.insert(dynamicMusic.musicLibrary[category].files, file)
    print("Música adicionada:", category, file)
end

function dynamicMusic.terminate()
    dynamicMusic.stopAllMusic()
    
    -- Limpar eventos de fade
    for _, event in ipairs(dynamicMusic.fadeEvents) do
        removeEvent(event)
    end
    dynamicMusic.fadeEvents = {}
end
```

### Exemplo 3: Sistema de Efeitos Sonoros 3D

```lua
-- modules/spatial_audio/spatial_audio.lua
spatialAudio = {}

function spatialAudio.init()
    spatialAudio.soundSources = {}
    spatialAudio.maxDistance = 15 -- Distância máxima para sons
    spatialAudio.setupGameIntegration()
end

function spatialAudio.setupGameIntegration()
    connect(g_game, {
        onMissileAppear = spatialAudio.onMissileAppear,
        onAnimatedTextAppear = spatialAudio.onAnimatedTextAppear,
        onEffectAppear = spatialAudio.onEffectAppear,
        onCreatureMove = spatialAudio.onCreatureMove,
        onLocalPlayerPositionChange = spatialAudio.updateListenerPosition
    })
end

function spatialAudio.onMissileAppear(missile)
    local position = missile:getPosition()
    local missileId = missile:getId()
    
    -- Sons baseados no tipo de míssil
    local missileSounds = {
        [1] = "sounds/missiles/spear.ogg",      -- Spear
        [2] = "sounds/missiles/bolt.ogg",       -- Bolt
        [3] = "sounds/missiles/arrow.ogg",      -- Arrow
        [4] = "sounds/missiles/fire.ogg",       -- Fire
        [5] = "sounds/missiles/energy.ogg",     -- Energy
        [6] = "sounds/missiles/poison.ogg",     -- Poison
        [7] = "sounds/missiles/ice.ogg",        -- Ice
        [8] = "sounds/missiles/holy.ogg",       -- Holy
        [9] = "sounds/missiles/death.ogg"       -- Death
    }
    
    local soundFile = missileSounds[missileId]
    if soundFile then
        spatialAudio.playPositionalSound(soundFile, position, 1.0, 1.0)
    end
end

function spatialAudio.onAnimatedTextAppear(animatedText)
    local position = animatedText:getPosition()
    local textType = animatedText:getType()
    
    -- Sons baseados no tipo de texto animado
    if textType == AnimatedTextType.Damage then
        spatialAudio.playPositionalSound("sounds/combat/hit.ogg", position, 0.8, 1.0)
    elseif textType == AnimatedTextType.Heal then
        spatialAudio.playPositionalSound("sounds/combat/heal.ogg", position, 0.6, 1.2)
    elseif textType == AnimatedTextType.Mana then
        spatialAudio.playPositionalSound("sounds/combat/mana.ogg", position, 0.5, 1.1)
    end
end

function spatialAudio.onEffectAppear(effect)
    local position = effect:getPosition()
    local effectId = effect:getId()
    
    -- Sons baseados no tipo de efeito
    local effectSounds = {
        [1] = "sounds/effects/teleport.ogg",    -- Teleport
        [2] = "sounds/effects/magic.ogg",       -- Magic effect
        [3] = "sounds/effects/explosion.ogg",   -- Explosion
        [4] = "sounds/effects/fire.ogg",        -- Fire
        [5] = "sounds/effects/poison.ogg",      -- Poison
        [10] = "sounds/effects/heal.ogg",       -- Heal
        [11] = "sounds/effects/spark.ogg",      -- Spark
        [12] = "sounds/effects/fire_hit.ogg"    -- Fire hit
    }
    
    local soundFile = effectSounds[effectId]
    if soundFile then
        spatialAudio.playPositionalSound(soundFile, position, 1.0, 1.0)
    end
end

function spatialAudio.playPositionalSound(soundFile, position, volume, pitch)
    if not g_resources.fileExists(soundFile) then
        return
    end
    
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    local playerPos = player:getPosition()
    local distance = spatialAudio.calculateDistance(playerPos, position)
    
    -- Não tocar som se muito distante
    if distance > spatialAudio.maxDistance then
        return
    end
    
    -- Calcular volume baseado na distância
    local distanceVolume = 1.0 - (distance / spatialAudio.maxDistance)
    local finalVolume = volume * distanceVolume
    
    -- Calcular pan estéreo baseado na posição relativa
    local pan = spatialAudio.calculateSterePan(playerPos, position)
    
    -- Reproduzir som
    local effectsChannel = g_sounds.getChannel(SoundChannels.Effects)
    if effectsChannel then
        -- Nota: Esta API de pan estéreo seria hipotética
        -- effectsChannel:playWithPan(soundFile, 0, finalVolume, pitch, pan)
        effectsChannel:play(soundFile, 0, finalVolume, pitch)
    end
    
    -- Registrar fonte sonora
    local sourceId = spatialAudio.generateSourceId()
    spatialAudio.soundSources[sourceId] = {
        file = soundFile,
        position = position,
        volume = finalVolume,
        pitch = pitch,
        startTime = g_clock.millis()
    }
    
    -- Remover fonte após um tempo
    scheduleEvent(function()
        spatialAudio.soundSources[sourceId] = nil
    end, 5000)
end

function spatialAudio.calculateDistance(pos1, pos2)
    local dx = pos1.x - pos2.x
    local dy = pos1.y - pos2.y
    local dz = (pos1.z - pos2.z) * 4 -- Z tem peso maior
    
    return math.sqrt(dx * dx + dy * dy + dz * dz)
end

function spatialAudio.calculateSterePan(listenerPos, sourcePos)
    local dx = sourcePos.x - listenerPos.x
    
    -- Pan de -1.0 (esquerda) a 1.0 (direita)
    local pan = math.max(-1.0, math.min(1.0, dx / 10.0))
    return pan
end

function spatialAudio.updateListenerPosition(localPlayer, newPos, oldPos)
    -- Atualizar posição do ouvinte para cálculos 3D
    g_sounds.setPosition(newPos)
    
    -- Atualizar volume de todas as fontes ativas baseado na nova posição
    for sourceId, source in pairs(spatialAudio.soundSources) do
        local distance = spatialAudio.calculateDistance(newPos, source.position)
        
        if distance > spatialAudio.maxDistance then
            -- Som muito distante, remover
            spatialAudio.soundSources[sourceId] = nil
        else
            -- Atualizar volume baseado na nova distância
            local distanceVolume = 1.0 - (distance / spatialAudio.maxDistance)
            source.volume = source.originalVolume * distanceVolume
        end
    end
end

function spatialAudio.onCreatureMove(creature, newPos, oldPos)
    -- Tocar som de movimento baseado no terreno
    if creature:isLocalPlayer() then
        local tile = g_map.getTile(newPos)
        if tile then
            local ground = tile:getGround()
            if ground then
                local terrainSound = spatialAudio.getTerrainSound(ground:getId())
                if terrainSound then
                    spatialAudio.playPositionalSound(terrainSound, newPos, 0.3, 1.0)
                end
            end
        end
    end
end

function spatialAudio.getTerrainSound(groundId)
    -- Mapeamento de IDs de terreno para sons
    local terrainSounds = {
        -- Grama
        [4526] = "sounds/terrain/grass.ogg",
        [4527] = "sounds/terrain/grass.ogg",
        
        -- Pedra
        [4608] = "sounds/terrain/stone.ogg",
        [4609] = "sounds/terrain/stone.ogg",
        
        -- Água
        [4608] = "sounds/terrain/water.ogg",
        [4609] = "sounds/terrain/water.ogg",
        
        -- Areia
        [5406] = "sounds/terrain/sand.ogg",
        [5407] = "sounds/terrain/sand.ogg"
    }
    
    return terrainSounds[groundId]
end

function spatialAudio.generateSourceId()
    return string.format("source_%d_%d", g_clock.millis(), math.random(1000, 9999))
end

function spatialAudio.setMaxDistance(distance)
    spatialAudio.maxDistance = distance
end

function spatialAudio.getActiveSources()
    local count = 0
    for _ in pairs(spatialAudio.soundSources) do
        count = count + 1
    end
    return count
end

function spatialAudio.terminate()
    spatialAudio.soundSources = {}
end
```

---

Esta documentação cobre completamente o sistema de som do OTClient, fornecendo exemplos práticos e detalhados para trabalhar com áudio, canais de som, efeitos sonoros e integração com o jogo. Use estes exemplos como base para criar sistemas avançados de áudio e feedback sonoro em seus módulos.

---

> [!success] Navegação
> - [[Getting_Started_Guide]] - Comece aqui
> - [[Module_System_Guide]] - Desenvolvimento de módulos
> - [[UI_System_Guide]] - Interface do usuário
> - [[Lua_API_Reference]] - Referência completa da API

