
# Sistema de Efeitos

Sistema completo de efeitos visuais incluindo efeitos animados, anexados e UI com suporte a shaders e transformações.

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [API C++](#api-c)
3. [API Lua](#api-lua)
4. [Efeitos Básicos](#efeitos-básicos)
5. [Efeitos Anexados](#efeitos-anexados)
6. [Efeitos de UI](#efeitos-de-ui)
7. [Exemplos Práticos](#exemplos-práticos)
8. [Melhores Práticas](#melhores-práticas)

## 🎯 Visão Geral

O sistema de efeitos do OTClient oferece múltiplas camadas de efeitos visuais:

- **Efeitos Básicos**: Animações temporárias no mapa
- **Efeitos Anexados**: Ligados a criaturas/objetos
- **Efeitos de UI**: Transições e animações de interface
- **Shaders**: Efeitos de pós-processamento
- **Transformações**: Mudanças visuais temporárias

### 🔧 Tipos de Efeitos

```
Efeito Básico → Posição fixa no mapa, temporário
Efeito Anexado → Segue objeto/criatura, configurável
Efeito UI → Interface do usuário, interativo
Shader → Pós-processamento, global/local
```

## 🔧 API C++

### Effect Class
```cpp
class Effect : public Thing {
    -- Classe: Effect
public:
    // Renderização
    void draw(const Point& dest, bool drawThings = true, 
             const LightViewPtr& lightView = nullptr) override;
    
    // Configuração
    void setId(uint32_t id) override;
    void setPosition(const Position& position, uint8_t stackPos = 0, 
                    bool hasElevation = false) override;
    
    // Estado
    bool isEffect() override { return true; }
    bool waitFor(const EffectPtr& effect);
    
    // Conversão
    EffectPtr asEffect() { return static_self_cast<Effect>(); }

protected:
    void onAppear() override;
    ThingType* getThingType() const override;

private:
    Timer m_animationTimer;      // Timer de animação
    uint16_t m_duration;         // Duração total
    uint16_t m_timeToStartDrawing; // Delay inicial
};
```

### AttachedEffect Class
```cpp
class AttachedEffect {
    -- Classe: AttachedEffect
public:
    // Criação
    static AttachedEffectPtr create(uint16_t thingId, ThingCategory category);
    
    // Configuração básica
    void setId(uint16_t id);
    void setSpeed(float speed);
    void setDuration(uint32_t duration);
    void setLoop(uint16_t loop);
    void setPermanent(bool permanent);
    
    // Posicionamento
    void setOffset(int16_t x, int16_t y);
    void setDirOffset(uint8_t dir, int16_t x, int16_t y, bool onTop = false);
    void setOnTop(bool onTop);
    void setOnTopByDir(uint8_t dir, bool onTop);
    
    // Visual
    void setOpacity(float opacity);
    void setShader(const std::string& name);
    void setSize(const Size& size);
    void setTransform(bool transform);
    void setHideOwner(bool hide);
    
    // Animações
    void setBounce(int16_t minHeight, int16_t height, uint32_t speed);
    void setPulse(int16_t minScale, int16_t scale, uint32_t speed);
    void setFade(int16_t start, int16_t end, uint32_t speed);
    
    // Iluminação
    void setLight(const Light& light);
    
    // Movimento
    void move(const Position& fromPos, const Position& toPos);
    
    // Hierarquia
    void attachEffect(const AttachedEffectPtr& effect);
    void detachEffect(const AttachedEffectPtr& effect);
    
    // Estado
    bool isActive() const;
    ThingPtr getOwner() const;
    void setOwner(const ThingPtr& owner);
};
```

### EffectManager
```cpp
class EffectManager {
    -- Classe: EffectManager
public:
    // Registro
    static void registerEffect(uint16_t id, const std::string& name,
                              uint16_t thingId, ThingCategory category);
    static void registerEffectByImage(uint16_t id, const std::string& name,
                                     const std::string& imagePath);
    
    // Obtenção
    static AttachedEffectPtr getById(uint16_t id);
    static std::vector<AttachedEffectPtr> getAll();
    
    // Remoção
    static void removeEffect(uint16_t id);
    static void clear();
    
    // Configuração global
    static void setGlobalSpeed(float speed);
    static void setGlobalOpacity(float opacity);
    static bool isEnabled();
    static void setEnabled(bool enabled);
};
```

## 🐍 API Lua

### Efeitos Básicos

#### `Effect.create()`
Cria um novo efeito básico.

```lua
-- Criar efeito
    --  Criar efeito (traduzido)
local effect = Effect.create()
effect:setId(50)  -- ID do efeito

-- Adicionar ao mapa
    --  Adicionar ao mapa (traduzido)
local tile = g_map.getTile(position)
tile:addThing(effect)

-- Efeito com posição direta
local effect2 = Effect.create()
effect2:setId(12)
effect2:setPosition(player:getPosition())
```

#### Efeitos Predefinidos
```lua
-- Efeitos comuns
    --  Efeitos comuns (traduzido)
local EFFECT_IDS = {
    POFF = 3,
    YELLOW_RINGS = 12,
    RED_RINGS = 13,
    FIRE = 15,
    POISON = 8,
    HOLY = 49,
    BLOOD = 28,
    TELEPORT = 18,
    MAGIC_MISSILE = 35
}

-- Função auxiliar
function createMapEffect(effectId, position)
    -- Função: createMapEffect
    local effect = Effect.create()
    effect:setId(effectId)
    effect:setPosition(position)
    return effect
end

-- Uso
    --  Uso (traduzido)
createMapEffect(EFFECT_IDS.FIRE, player:getPosition())
```

### Efeitos Anexados

#### `g_attachedEffects` Interface
```lua
-- Registrar efeito por sprite
    --  Registrar efeito por sprite (traduzido)
g_attachedEffects.registerByThing(id, name, thingId, category)

-- Registrar efeito por imagem
    --  Registrar efeito por imagem (traduzido)
g_attachedEffects.registerByImage(id, name, imagePath, smooth)

-- Obter efeito
    --  Obter efeito (traduzido)
local effect = g_attachedEffects.getById(id)

-- Remover efeito
    --  Remover efeito (traduzido)
g_attachedEffects.remove(id)

-- Limpar todos
    --  Limpar todos (traduzido)
g_attachedEffects.clear()
```

#### `AttachedEffectManager` Sistema
#### Nível Basic
```lua
-- Registrar efeito com configuração completa
-- Configuração de efeito
local config = {
    -- Animação
    -- Visual
    -- Posicionamento
    -- Animações especiais
    fade = {start, end, speed},           -- Animação de fade
    -- Iluminação
    -- Callbacks
    onAttach = function(effect, owner)
        -- Quando anexado
    end,
    onDetach = function(effect, oldOwner)
        -- Quando desanexado
    end
```

#### Nível Intermediate
```lua
-- Registrar efeito com configuração completa
AttachedEffectManager.register(id, name, thingId, category, config)

-- Configuração de efeito
local config = {
    -- Animação
    speed = 1.0,                    -- Velocidade da animação
    duration = 5000,                -- Duração em ms (0 = infinito)
    loop = 1,                       -- Número de loops (0 = infinito)
    
    -- Visual
    opacity = 1.0,                  -- Opacidade (0.0 - 1.0)
    shader = "OutfitGrayscale",     -- Nome do shader
    size = {width, height},         -- Tamanho personalizado
    hideOwner = false,              -- Esconder dono
    transform = false,              -- Transformar dono
    drawOnUI = true,                -- Desenhar na UI
    
    -- Posicionamento
    offset = {x, y, onTop},         -- Offset padrão
    dirOffset = {                   -- Offset por direção
        [North] = {x, y, onTop},
        [East] = {x, y, onTop},
        [South] = {x, y, onTop},
        [West] = {x, y, onTop}
    },
    
    -- Animações especiais
    bounce = {minHeight, height, speed},  -- Animação de pulo
    pulse = {minScale, scale, speed},     -- Animação de pulso
    fade = {start, end, speed},           -- Animação de fade
    
    -- Iluminação
    light = {
        color = 0xFFFFFF,           -- Cor da luz
        intensity = 5               -- Intensidade
    },
    
    -- Callbacks
    onAttach = function(effect, owner)
        -- Quando anexado
    end,
    onDetach = function(effect, oldOwner)
        -- Quando desanexado
    end
}
```

#### Nível Advanced
```lua
-- Registrar efeito com configuração completa
AttachedEffectManager.register(id, name, thingId, category, config)

-- Configuração de efeito
local config = {
    -- Animação
    speed = 1.0,                    -- Velocidade da animação
    duration = 5000,                -- Duração em ms (0 = infinito)
    loop = 1,                       -- Número de loops (0 = infinito)
    
    -- Visual
    opacity = 1.0,                  -- Opacidade (0.0 - 1.0)
    shader = "OutfitGrayscale",     -- Nome do shader
    size = {width, height},         -- Tamanho personalizado
    hideOwner = false,              -- Esconder dono
    transform = false,              -- Transformar dono
    drawOnUI = true,                -- Desenhar na UI
    
    -- Posicionamento
    offset = {x, y, onTop},         -- Offset padrão
    dirOffset = {                   -- Offset por direção
        [North] = {x, y, onTop},
        [East] = {x, y, onTop},
        [South] = {x, y, onTop},
        [West] = {x, y, onTop}
    },
    
    -- Animações especiais
    bounce = {minHeight, height, speed},  -- Animação de pulo
    pulse = {minScale, scale, speed},     -- Animação de pulso
    fade = {start, end, speed},           -- Animação de fade
    
    -- Iluminação
    light = {
        color = 0xFFFFFF,           -- Cor da luz
        intensity = 5               -- Intensidade
    },
    
    -- Callbacks
    onAttach = function(effect, owner)
        -- Quando anexado
    end,
    onDetach = function(effect, oldOwner)
        -- Quando desanexado
    end
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

#### Anexar/Desanexar Efeitos
```lua
-- Anexar efeito a criatura
    --  Anexar efeito a criatura (traduzido)
local effect = g_attachedEffects.getById(1)
player:attachEffect(effect)

-- Desanexar efeito
    --  Desanexar efeito (traduzido)
player:detachEffect(effect)

-- Desanexar todos os efeitos
    --  Desanexar todos os efeitos (traduzido)
player:detachAllEffects()

-- Verificar se tem efeito
    --  Verificar se tem efeito (traduzido)
local hasEffect = player:hasAttachedEffect(effectId)

-- Obter efeitos anexados
    --  Obter efeitos anexados (traduzido)
local effects = player:getAttachedEffects()
```

### Efeitos de UI

#### `g_effects` Interface para UI
```lua
-- Fade in
    --  Fade in (traduzido)
g_effects.fadeIn(widget, time, elapsed)

-- Fade out  
    --  Fade out (traduzido)
g_effects.fadeOut(widget, time, elapsed)

-- Cancelar fade
    --  Cancelar fade (traduzido)
g_effects.cancelFade(widget)

-- Piscar
    --  Piscar (traduzido)
g_effects.startBlink(widget, duration, interval, clickCancel)

-- Parar de piscar
    --  Parar de piscar (traduzido)
g_effects.stopBlink(widget)
```

#### Exemplos de Uso
```lua
-- Fade in em janela
    --  Fade in em janela (traduzido)
local window = g_ui.createWidget('MainWindow')
window:setOpacity(0)
window:show()
g_effects.fadeIn(window, 500)

-- Fade out e destruir
    --  Fade out e destruir (traduzido)
g_effects.fadeOut(window, 300)
scheduleEvent(function()
    window:destroy()
end, 300)

-- Botão piscando
local button = g_ui.createWidget('UIButton', parent)
g_effects.startBlink(button, 3000, 250)  -- 3 segundos, 250ms intervalo
```

## 🎮 Efeitos Básicos

### Criação e Gerenciamento
#### Inicialização e Configuração
```lua
local EffectHelper = {}

-- Criar efeito no mapa
function EffectHelper.createAt(effectId, position, delay)
    local function create()
        local effect = Effect.create()
        effect:setId(effectId)
        effect:setPosition(position)
        return effect
    end
    
    if delay and delay > 0 then
        scheduleEvent(create, delay)
    else
        return create()
    end
end

-- Criar efeito em área
function EffectHelper.createArea(effectId, centerPos, radius)
    for x = -radius, radius do
        for y = -radius, radius do
            local pos = {
                x = centerPos.x + x,
                y = centerPos.y + y,
                z = centerPos.z
            }
```

#### Funcionalidade 1
```lua
            
            local distance = math.sqrt(x*x + y*y)
            if distance <= radius then
                local delay = distance * 100  -- 100ms por tile
                EffectHelper.createAt(effectId, pos, delay)
            end
        end
    end
end

-- Criar linha de efeitos
function EffectHelper.createLine(effectId, fromPos, toPos, interval)
    local dx = toPos.x - fromPos.x
    local dy = toPos.y - fromPos.y
    local distance = math.max(math.abs(dx), math.abs(dy))
    
    for i = 0, distance do
        local progress = distance > 0 and i / distance or 0
        local pos = {
            x = fromPos.x + math.floor(dx * progress),
            y = fromPos.y + math.floor(dy * progress),
            z = fromPos.z
        }
```

#### Finalização
```lua
        
        EffectHelper.createAt(effectId, pos, i * (interval or 50))
    end
end

-- Uso dos helpers
EffectHelper.createAt(EFFECT_IDS.FIRE, player:getPosition())
EffectHelper.createArea(EFFECT_IDS.POISON, player:getPosition(), 3)
EffectHelper.createLine(EFFECT_IDS.MAGIC_MISSILE, 
                       player:getPosition(), 
                       target:getPosition(), 100)
```

## 🔗 Efeitos Anexados

### Sistema de Registro
#### Nível Basic
```lua
-- Efeito simples
AttachedEffectManager.register(1, 'Glow', 50, ThingCategoryEffect, {
    opacity = 0.8,
    offset = {0, -10}
})

-- Efeito com shader
AttachedEffectManager.register(2, 'Rainbow Aura', 307, ThingCategoryCreature, {
    shader = 'Outfit - Rainbow',
    speed = 2.0,
    offset = {0, 0, true}  -- onTop = true
})

-- Efeito com animações
AttachedEffectManager.register(3, 'Floating', 40, ThingCategoryEffect, {
    bounce = {10, 30, 2000},      -- Flutuar entre 10-30 pixels
    pulse = {80, 120, 1500},      -- Pulsação 80%-120%
    fade = {50, 100, 1000},       -- Fade 50%-100%
    duration = 10000              -- 10 segundos
})

-- Efeito com direções
AttachedEffectManager.register(4, 'Wings', 308, ThingCategoryCreature, {
    disableWalkAnimation = true,
    dirOffset = {
        [North] = {0, -15, true},
        [East] = {10, -10, true},
        [South] = {0, -5, true},
        [West] = {-10, -10, true}
    }
})

-- Efeito por imagem externa
AttachedEffectManager.register(5, 'Custom Aura', '/images/effects/aura', ThingExternalTexture, {
    size = {64, 64},
    offset = {32, 32}
})
```

#### Nível Intermediate
```lua
-- Efeito simples
AttachedEffectManager.register(1, 'Glow', 50, ThingCategoryEffect, {
    opacity = 0.8,
    offset = {0, -10}
})

-- Efeito com shader
AttachedEffectManager.register(2, 'Rainbow Aura', 307, ThingCategoryCreature, {
    shader = 'Outfit - Rainbow',
    speed = 2.0,
    offset = {0, 0, true}  -- onTop = true
})

-- Efeito com animações
AttachedEffectManager.register(3, 'Floating', 40, ThingCategoryEffect, {
    bounce = {10, 30, 2000},      -- Flutuar entre 10-30 pixels
    pulse = {80, 120, 1500},      -- Pulsação 80%-120%
    fade = {50, 100, 1000},       -- Fade 50%-100%
    duration = 10000              -- 10 segundos
})

-- Efeito com direções
AttachedEffectManager.register(4, 'Wings', 308, ThingCategoryCreature, {
    disableWalkAnimation = true,
    dirOffset = {
        [North] = {0, -15, true},
        [East] = {10, -10, true},
        [South] = {0, -5, true},
        [West] = {-10, -10, true}
    }
})

-- Efeito por imagem externa
AttachedEffectManager.register(5, 'Custom Aura', '/images/effects/aura', ThingExternalTexture, {
    size = {64, 64},
    offset = {32, 32}
})
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
-- Efeito simples
AttachedEffectManager.register(1, 'Glow', 50, ThingCategoryEffect, {
    opacity = 0.8,
    offset = {0, -10}
})

-- Efeito com shader
AttachedEffectManager.register(2, 'Rainbow Aura', 307, ThingCategoryCreature, {
    shader = 'Outfit - Rainbow',
    speed = 2.0,
    offset = {0, 0, true}  -- onTop = true
})

-- Efeito com animações
AttachedEffectManager.register(3, 'Floating', 40, ThingCategoryEffect, {
    bounce = {10, 30, 2000},      -- Flutuar entre 10-30 pixels
    pulse = {80, 120, 1500},      -- Pulsação 80%-120%
    fade = {50, 100, 1000},       -- Fade 50%-100%
    duration = 10000              -- 10 segundos
})

-- Efeito com direções
AttachedEffectManager.register(4, 'Wings', 308, ThingCategoryCreature, {
    disableWalkAnimation = true,
    dirOffset = {
        [North] = {0, -15, true},
        [East] = {10, -10, true},
        [South] = {0, -5, true},
        [West] = {-10, -10, true}
    }
})

-- Efeito por imagem externa
AttachedEffectManager.register(5, 'Custom Aura', '/images/effects/aura', ThingExternalTexture, {
    size = {64, 64},
    offset = {32, 32}
})
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

### Efeitos Compostos
```lua
-- Efeito principal que gerencia sub-efeitos
    --  Efeito principal que gerencia sub-efeitos (traduzido)
AttachedEffectManager.register(10, 'Elemental Aura', 0, 0, {
    onAttach = function(effect, owner)
        -- Fogo
    --  Fogo (traduzido)
        local fireEffect = g_attachedEffects.getById(1):clone()
        fireEffect:setOffset(-20, -20, true)
        fireEffect:setShader('Fire')
        effect:attachEffect(fireEffect)
        
        -- Gelo
    --  Gelo (traduzido)
        local iceEffect = g_attachedEffects.getById(2):clone()
        iceEffect:setOffset(20, -20, true)
        iceEffect:setShader('Ice')
        effect:attachEffect(iceEffect)
        
        -- Raio
    --  Raio (traduzido)
        local lightningEffect = g_attachedEffects.getById(3):clone()
        lightningEffect:setOffset(0, -30, true)
        lightningEffect:setShader('Lightning')
        effect:attachEffect(lightningEffect)
    end,
    
    onDetach = function(effect, oldOwner)
        -- Efeito de desaparecimento
    --  Efeito de desaparecimento (traduzido)
        local dispelEffect = Effect.create()
        dispelEffect:setId(20)
        oldOwner:getTile():addThing(dispelEffect)
    end
})
```

### Sistema Dinâmico de Efeitos
#### Inicialização e Configuração
```lua
local DynamicEffects = {}

-- Efeito baseado na vida
function DynamicEffects.healthAura(creature)
    local healthPercent = creature:getHealthPercent()
    local effectId
    
    if healthPercent > 75 then
        effectId = 1  -- Verde
    elseif healthPercent > 50 then
        effectId = 2  -- Amarelo
    elseif healthPercent > 25 then
        effectId = 3  -- Laranja
    else
        effectId = 4  -- Vermelho
    end
    
    -- Remover efeito anterior
    creature:detachAllEffects()
    
    -- Anexar novo efeito
    local effect = g_attachedEffects.getById(effectId)
    if effect then
        creature:attachEffect(effect)
    end
```

#### Funcionalidade 1
```lua
end

-- Efeito baseado no status
function DynamicEffects.statusEffects(creature)
    local conditions = creature:getConditions()
    
    for condition, active in pairs(conditions) do
        local effectId = {
            poison = 5,
            fire = 6,
            energy = 7,
            physical = 8,
            holy = 9,
            death = 10,
            ice = 11,
            earth = 12
        }[condition]
        
        if effectId then
            if active then
                local effect = g_attachedEffects.getById(effectId)
                creature:attachEffect(effect)
            else
                creature:detachEffectById(effectId)
            end
```

#### Finalização
```lua
        end
    end
end

-- Auto-atualização
local function updateDynamicEffects()
    for _, creature in ipairs(g_map.getCreatures()) do
        DynamicEffects.healthAura(creature)
        DynamicEffects.statusEffects(creature)
    end
    
    scheduleEvent(updateDynamicEffects, 1000)  -- A cada segundo
end

updateDynamicEffects()
```

## 🎨 Efeitos de UI

### Sistema de Transições
#### Inicialização e Configuração
```lua
local UIEffects = {}

-- Transição de slide
function UIEffects.slideIn(widget, direction, duration)
    duration = duration or 300
    local originalPos = widget:getPosition()
    local startPos = {x = originalPos.x, y = originalPos.y}
    
    -- Definir posição inicial baseada na direção
    if direction == 'left' then
        startPos.x = startPos.x - widget:getWidth()
    elseif direction == 'right' then
        startPos.x = startPos.x + widget:getWidth()
    elseif direction == 'top' then
        startPos.y = startPos.y - widget:getHeight()
    elseif direction == 'bottom' then
        startPos.y = startPos.y + widget:getHeight()
    end
    
    widget:setPosition(startPos)
    
    -- Animar para posição final
    local startTime = g_clock.millis()
    local function animate()
        local elapsed = g_clock.millis() - startTime
        local progress = math.min(elapsed / duration, 1)
        
        -- Easing out cubic
        progress = 1 - math.pow(1 - progress, 3)
        
        local currentX = startPos.x + (originalPos.x - startPos.x) * progress
        local currentY = startPos.y + (originalPos.y - startPos.y) * progress
        
        widget:setPosition({x = currentX, y = currentY})
        
        if progress < 1 then
            scheduleEvent(animate, 16)  -- ~60fps
        end
```

#### Funcionalidade 1
```lua
    end
    
    animate()
end

-- Transição de escala
function UIEffects.scaleIn(widget, duration)
    duration = duration or 300
    local originalSize = widget:getSize()
    
    widget:setSize({width = 0, height = 0})
    
    local startTime = g_clock.millis()
    local function animate()
        local elapsed = g_clock.millis() - startTime
        local progress = math.min(elapsed / duration, 1)
        
        -- Easing out back
        local c1 = 1.70158
        local c3 = c1 + 1
        progress = 1 + c3 * math.pow(progress - 1, 3) + c1 * math.pow(progress - 1, 2)
        
        local currentWidth = originalSize.width * progress
        local currentHeight = originalSize.height * progress
        
        widget:setSize({width = currentWidth, height = currentHeight})
        
        if progress < 1 then
            scheduleEvent(animate, 16)
        end
```

#### Funcionalidade 2
```lua
    end
    
    animate()
end

-- Transição rotativa
function UIEffects.rotateIn(widget, duration)
    duration = duration or 500
    
    local startTime = g_clock.millis()
    local function animate()
        local elapsed = g_clock.millis() - startTime
        local progress = math.min(elapsed / duration, 1)
        
        local rotation = (1 - progress) * 360  -- De 360 para 0 graus
        widget:setRotation(rotation)
        
        -- Também aplicar escala
        local scale = progress * 0.8 + 0.2  -- De 0.2 para 1.0
        widget:setScale(scale)
        
        if progress < 1 then
            scheduleEvent(animate, 16)
        else
            widget:setRotation(0)
            widget:setScale(1)
        end
```

#### Funcionalidade 3
```lua
    end
    
    animate()
end

-- Sistema de notificações animadas
function UIEffects.showNotification(text, type, duration)
    duration = duration or 3000
    type = type or 'info'
    
    local notification = g_ui.createWidget('UILabel')
    notification:setText(text)
    notification:setTextAlign(AlignCenter)
    notification:setSize({300, 50})
    
    -- Estilo baseado no tipo
    local styles = {
        info = {backgroundColor = '#3498db', textColor = '#ffffff'},
        success = {backgroundColor = '#2ecc71', textColor = '#ffffff'},
        warning = {backgroundColor = '#f39c12', textColor = '#ffffff'},
        error = {backgroundColor = '#e74c3c', textColor = '#ffffff'}
    }
```

#### Funcionalidade 4
```lua
    
    local style = styles[type] or styles.info
    notification:setBackgroundColor(style.backgroundColor)
    notification:setColor(style.textColor)
    
    -- Posicionar no topo da tela
    local screenSize = g_window.getSize()
    notification:setPosition({
        x = (screenSize.width - 300) / 2,
        y = -50  -- Começa fora da tela
    })
    
    -- Animar entrada
    UIEffects.slideIn(notification, 'top', 400)
    
    -- Agendar saída
    scheduleEvent(function()
        UIEffects.slideOut(notification, 'top', 400)
        scheduleEvent(function()
            notification:destroy()
        end, 400)
```

#### Finalização
```lua
    end, duration)
    
    return notification
end

-- Uso das transições
UIEffects.slideIn(window, 'left', 500)
UIEffects.scaleIn(button, 300)
UIEffects.rotateIn(icon, 600)
UIEffects.showNotification('Conectado com sucesso!', 'success')
```

## 💡 Exemplos Práticos

### 1. Sistema de Buff Visual
#### Inicialização e Configuração
```lua
local BuffEffects = {}

-- Definir efeitos de buff
local BUFF_EFFECTS = {
    [CONDITION_HASTE] = {
        effectId = 101,
        name = 'Speed Boost',
        color = '#00ff00'
    },
    [CONDITION_STRONG] = {
        effectId = 102,
        name = 'Strength',
        color = '#ff6600'
    },
    [CONDITION_PROTECTION] = {
        effectId = 103,
        name = 'Protection',
        color = '#0066ff'
    }
}

-- Registrar efeitos de buff
for condition, config in pairs(BUFF_EFFECTS) do
    AttachedEffectManager.register(config.effectId, config.name, 50, ThingCategoryEffect, {
        speed = 1.5,
        opacity = 0.7,
        offset = {0, -20, true},
        light = {
            color = tonumber(config.color:sub(2), 16),
            intensity = 3
        },
```

#### Funcionalidade 1
```lua
        pulse = {90, 110, 1000}
    })
end

function BuffEffects.updatePlayer(player)
    -- Remover todos os efeitos de buff antigos
    for condition, config in pairs(BUFF_EFFECTS) do
        player:detachEffectById(config.effectId)
    end
    
    -- Adicionar efeitos para condições ativas
    for condition, config in pairs(BUFF_EFFECTS) do
        if player:hasCondition(condition) then
            local effect = g_attachedEffects.getById(config.effectId)
            if effect then
                player:attachEffect(effect)
            end
        end
    end
end

-- Conectar aos eventos
connect(LocalPlayer, {
    onConditionAdd = function(localPlayer, condition)
        BuffEffects.updatePlayer(localPlayer)
    end,
```

#### Finalização
```lua
    onConditionRemove = function(localPlayer, condition)
        BuffEffects.updatePlayer(localPlayer)
    end
})
```

### 2. Sistema de Efeitos de Combate
#### Inicialização e Configuração
```lua
local CombatEffects = {}

-- Efeitos de dano
function CombatEffects.showDamage(creature, damage, damageType)
    local colors = {
        [COMBAT_PHYSICAL] = '#ff0000',
        [COMBAT_ENERGY] = '#9966ff',
        [COMBAT_EARTH] = '#00ff00',
        [COMBAT_FIRE] = '#ff6600',
        [COMBAT_ICE] = '#0099ff',
        [COMBAT_HOLY] = '#ffff00',
        [COMBAT_DEATH] = '#990099'
    }
    
    local color = colors[damageType] or '#ffffff'
    
    -- Criar efeito de texto
    local textEffect = g_ui.createWidget('UILabel')
    textEffect:setText(tostring(damage))
    textEffect:setColor(color)
    textEffect:setFont('verdana-11px-outline')
    textEffect:setSize({100, 20})
    
    -- Posicionar sobre a criatura
    local creaturePos = creature:getPosition()
    local screenPos = g_map.toScreenPosition(creaturePos)
    textEffect:setPosition({
        x = screenPos.x - 50,
        y = screenPos.y - 40
    })
```

#### Funcionalidade 1
```lua
    
    -- Animar movimento para cima e fade
    local startTime = g_clock.millis()
    local function animate()
        local elapsed = g_clock.millis() - startTime
        local progress = elapsed / 1500  -- 1.5 segundos
        
        if progress <= 1 then
            local currentY = screenPos.y - 40 - (progress * 60)
            local opacity = 1 - progress
            
            textEffect:setPosition({
                x = screenPos.x - 50,
                y = currentY
            })
            textEffect:setOpacity(opacity)
            
            scheduleEvent(animate, 16)
        else
            textEffect:destroy()
        end
```

#### Funcionalidade 2
```lua
    end
    
    animate()
    
    -- Efeito visual no mapa
    local effectId = {
        [COMBAT_PHYSICAL] = 28,  -- Blood
        [COMBAT_ENERGY] = 40,    -- Energy
        [COMBAT_EARTH] = 35,     -- Poison
        [COMBAT_FIRE] = 15,      -- Fire
        [COMBAT_ICE] = 52,       -- Ice
        [COMBAT_HOLY] = 49,      -- Holy
        [COMBAT_DEATH] = 20      -- Death
    }[damageType]
    
    if effectId then
        local effect = Effect.create()
        effect:setId(effectId)
        effect:setPosition(creature:getPosition())
    end
end
```

#### Funcionalidade 3
```lua

-- Efeitos de spell
function CombatEffects.castSpell(creature, spellId)
    local spellEffects = {
        [1] = {  -- Fireball
            chargeEffect = 15,
            projectileEffect = 35,
            impactEffect = 28
        },
        [2] = {  -- Ice Strike
            chargeEffect = 52,
            projectileEffect = 51,
            impactEffect = 53
        }
    }
    
    local config = spellEffects[spellId]
    if not config then return end
    
    -- Efeito de carregamento
    local chargeEffect = Effect.create()
    chargeEffect:setId(config.chargeEffect)
    chargeEffect:setPosition(creature:getPosition())
    
    -- Som de conjuração
    g_sounds.play('sounds/spells/charge.ogg')
    
    return config  -- Retorna configuração para usar nos próximos efeitos
end
```

#### Finalização
```lua

-- Conectar aos eventos de combate
connect(g_game, {
    onCreatureDamage = function(creature, damage, damageType)
        CombatEffects.showDamage(creature, damage, damageType)
    end,
    
    onSpellCast = function(creature, spellId)
        CombatEffects.castSpell(creature, spellId)
    end
})
```

### 3. Efeitos Ambientais Dinâmicos
#### Inicialização e Configuração
```lua
local EnvironmentalEffects = {}

-- Sistema de clima
function EnvironmentalEffects.setWeather(weatherType, intensity)
    -- Remover efeitos anteriores
    g_shaders.clear()
    
    if weatherType == 'rain' then
        g_shaders.setGlobalShader('Rain')
        g_shaders.setShaderParam('Rain', 'intensity', intensity or 0.5)
        
        -- Som de chuva
        g_sounds.getChannel(SoundChannels.Environment):play('sounds/rain.ogg', 0, intensity)
        
    elseif weatherType == 'snow' then
        g_shaders.setGlobalShader('Snow')
        g_shaders.setShaderParam('Snow', 'intensity', intensity or 0.3)
        
    elseif weatherType == 'fog' then
        g_shaders.setGlobalShader('Fog')
        g_shaders.setShaderParam('Fog', 'density', intensity or 0.4)
        
    elseif weatherType == 'night' then
        g_shaders.setGlobalShader('Darkness')
        g_shaders.setShaderParam('Darkness', 'level', intensity or 0.6)
    end
```

#### Funcionalidade 1
```lua
end

-- Efeitos baseados no horário
function EnvironmentalEffects.updateTimeEffects()
    local gameTime = g_game.getWorldTime()
    local hour = math.floor(gameTime / 60) % 24
    
    if hour >= 6 and hour < 18 then
        -- Dia - sem efeitos especiais
        g_shaders.clear()
    elseif hour >= 18 and hour < 22 then
        -- Entardecer - luz dourada
        g_shaders.setGlobalShader('Sepia')
        g_shaders.setShaderParam('Sepia', 'intensity', 0.3)
    else
        -- Noite - escuridão
        EnvironmentalEffects.setWeather('night', 0.4)
    end
end

-- Efeitos de área especiais
function EnvironmentalEffects.createAreaEffect(centerPos, radius, effectType)
```

#### Funcionalidade 2
```lua
    local function createEffect(pos, delay)
        scheduleEvent(function()
            local effect = Effect.create()
            effect:setId(effectType)
            effect:setPosition(pos)
        end, delay)
    end
    
    -- Ondas concêntricas
    for r = 1, radius do
        for angle = 0, 360, 30 do  -- A cada 30 graus
            local radian = math.rad(angle)
            local x = centerPos.x + math.floor(r * math.cos(radian))
            local y = centerPos.y + math.floor(r * math.sin(radian))
            local pos = {x = x, y = y, z = centerPos.z}
            
            local delay = r * 100  -- 100ms por anel
            createEffect(pos, delay)
        end
    end
end
```

#### Finalização
```lua

-- Atualizar efeitos a cada minuto do jogo
connect(g_game, {
    onWorldTimeChange = function(time)
        EnvironmentalEffects.updateTimeEffects()
    end
})

-- Uso
EnvironmentalEffects.setWeather('rain', 0.7)
EnvironmentalEffects.createAreaEffect(player:getPosition(), 5, 12)
```

## ✅ Melhores Práticas

### 1. Performance
- **Limite efeitos simultâneos**: Máximo 50-100 efeitos ativos
- **Pool de objetos**: Reutilize efeitos em vez de criar novos
- **LOD (Level of Detail)**: Reduza qualidade para efeitos distantes
- **Culling**: Não renderize efeitos fora da tela

```lua
local EffectPool = {
    available = {},
    active = {},
    maxEffects = 100
}

function EffectPool.get()
    -- Função: EffectPool
    if #EffectPool.available > 0 then
    -- Verificação condicional
        return table.remove(EffectPool.available)
    else
        return Effect.create()
    end
end

function EffectPool.release(effect)
    -- Função: EffectPool
    if #EffectPool.active < EffectPool.maxEffects then
    -- Verificação condicional
        effect:setId(0)  -- Reset
        table.insert(EffectPool.available, effect)
    end
end
```

### 2. Organização
- **IDs consistentes**: Use ranges para diferentes tipos
- **Nomes descritivos**: Facilita manutenção
- **Configuração centralizada**: Um lugar para todos os efeitos
- **Documentação**: Comente configurações complexas

```lua
-- IDs organizados por categoria
    --  IDs organizados por categoria (traduzido)
local EFFECT_IDS = {
    -- Efeitos básicos (1-99)
    DAMAGE = {
        PHYSICAL = 1,
        MAGICAL = 2,
        POISON = 3
    },
    
    -- Efeitos anexados (100-199)  
    --  Efeitos anexados (100-199) (traduzido)
    AURAS = {
        HEALTH = 100,
        MANA = 101,
        SPEED = 102
    },
    
    -- Efeitos especiais (200-299)
    --  Efeitos especiais (200-299) (traduzido)
    SPECIAL = {
        TRANSFORMATION = 200,
        INVISIBILITY = 201
    }
}
```

### 3. Configuração
- **Valores padrão sensatos**: Que funcionem na maioria dos casos
- **Validação**: Verifique parâmetros antes de usar
- **Fallbacks**: Para quando recursos não existem
- **Hot-reload**: Permita recarregar configurações

```lua
function validateEffectConfig(config)
    -- Função: validateEffectConfig
    local defaults = {
        speed = 1.0,
        opacity = 1.0,
        duration = 0,
        offset = {0, 0, false}
    }
    
    -- Aplicar padrões
    for key, value in pairs(defaults) do
    -- Loop de repetição
        if config[key] == nil then
    -- Verificação condicional
            config[key] = value
        end
    end
    
    -- Validar ranges
    --  Validar ranges (traduzido)
    config.speed = math.max(0.1, math.min(config.speed, 10.0))
    config.opacity = math.max(0.0, math.min(config.opacity, 1.0))
    
    return config
end
```

### 4. Debugging
- **Sistema de log**: Para rastrear problemas
- **Visualização**: Debug visual de offsets e áreas
- **Profiling**: Monitore performance
- **Hot-keys**: Para testar rapidamente

```lua
local EffectDebug = {
    enabled = false,
    showBounds = false,
    logLevel = 'INFO'
}

function EffectDebug.log(level, message)
    -- Função: EffectDebug
    if EffectDebug.enabled and EffectDebug.logLevel == level then
    -- Verificação condicional
        print('[Effect Debug]', level, ':', message)
    end
end

function EffectDebug.drawBounds(effect)
    -- Função: EffectDebug
    if EffectDebug.showBounds then
    -- Verificação condicional
        -- Desenhar caixa delimitadora do efeito
    --  Desenhar caixa delimitadora do efeito (traduzido)
        local bounds = effect:getBounds()
        g_painter.drawRect(bounds, 'red')
    end
end
```

### 5. Compatibilidade
- **Versioning**: Para mudanças de API
- **Graceful degradation**: Funcione mesmo sem recursos
- **Platform differences**: Mobile vs Desktop
- **Performance tiers**: Diferentes qualidades

```lua
local EffectConfig = {
    qualityLevel = 'high',  -- high, medium, low
    platformOptimizations = true
}

function getEffectQuality()
    -- Função: getEffectQuality
    if g_platform.isMobile() then
    -- Verificação condicional
        return 'low'
    elseif EffectConfig.qualityLevel == 'high' and g_graphics.canUseShaders() then
        return 'high'
    else
        return 'medium'
    end
end

function createEffectForQuality(baseConfig)
    -- Função: createEffectForQuality
    local quality = getEffectQuality()
    local config = table.copy(baseConfig)
    
    if quality == 'low' then
    -- Verificação condicional
        config.shader = nil
        config.opacity = config.opacity * 0.7
    elseif quality == 'medium' then
        config.bounceHeight = config.bounceHeight * 0.5
    end
    
    return config
end
```

---

*Documentação gerada para OTClient - Redemption | Sistema de Efeitos*

---

<div class="success"> Navegação
> - [Getting_Started_Guide](Getting_Started_Guide.md) - Comece aqui
> - [Module_System_Guide](Module_System_Guide.md) - Desenvolvimento de módulos
> - [UI_System_Guide](UI_System_Guide.md) - Interface do usuário
> - [Lua_API_Reference](Lua_API_Reference.md) - Referência completa da API

