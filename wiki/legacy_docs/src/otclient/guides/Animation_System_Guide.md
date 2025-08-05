
# Animation System Guide

<div class="info"> Este guia documenta o sistema completo de animações e transições do OTClient, incluindo tweening, easing functions, animações de UI e controle de timing para criar interfaces fluidas e responsivas.

## 📋 Índice
- [#Visão Geral](#Visão Geral.md)
- [#Sistema de Tweening](#Sistema de Tweening.md)
- [#Funções de Easing](#Funções de Easing.md)
- [#Animações de UI](#Animações de UI.md)
- [#Transições de Tela](#Transições de Tela.md)
- [#Animações de Widgets](#Animações de Widgets.md)
- [#Controle de Timing](#Controle de Timing.md)
- [#Performance e Otimização](#Performance e Otimização.md)
- [#Exemplos Práticos](#Exemplos Práticos.md)
- [#Melhores Práticas](#Melhores Práticas.md)

---

## 🎯 Visão Geral

O sistema de animações do OTClient oferece:

- **Tweening Avançado**: Animações suaves entre valores
- **Funções de Easing**: Curvas de animação naturais
- **Animações de UI**: Transições de widgets e interfaces
- **Controle de Timing**: Precisão temporal nas animações
- **Performance Otimizada**: Animações eficientes e responsivas

### 🏗️ **Arquitetura do Sistema**

```
Sistema de Animações
   │
   ├─ Tween Engine
   │   ├─ Interpolação de valores
   │   ├─ Controle de timing
   │   └─ Callbacks de eventos
   │
   ├─ Easing Functions
   │   ├─ Linear
   │   ├─ Ease In/Out
   │   ├─ Bounce
   │   └─ Elastic
   │
   ├─ UI Animations
   │   ├─ Transições de widgets
   │   ├─ Animações de entrada/saída
   │   └─ Feedback visual
   │
   └─ Animation Manager
       ├─ Pool de animações
       ├─ Controle de performance
       └─ Limpeza automática
```

---

## ⚡ Sistema de Tweening

### 🎯 **Criando Tweens Básicos**

#### Nível Basic
```lua
-- Tween simples de posição
local widget = g_ui.createWidget('UIWidget', parent)
local tween = widget:addAnchoredTween(easeInOut, 1000)  -- 1 segundo
tween:setPosition({x = 100, y = 100})

-- Tween de escala
local scaleTween = widget:addAnchoredTween(easeOutBack, 500)
scaleTween:setScale(1.5)

-- Tween de rotação
local rotationTween = widget:addAnchoredTween(easeInOut, 800)
rotationTween:setRotation(360)  -- Rotação completa

-- Tween de opacidade
local opacityTween = widget:addAnchoredTween(easeInOut, 600)
opacityTween:setOpacity(0.5)
```

#### Nível Intermediate
```lua
-- Tween simples de posição
local widget = g_ui.createWidget('UIWidget', parent)
local tween = widget:addAnchoredTween(easeInOut, 1000)  -- 1 segundo
tween:setPosition({x = 100, y = 100})

-- Tween de escala
local scaleTween = widget:addAnchoredTween(easeOutBack, 500)
scaleTween:setScale(1.5)

-- Tween de rotação
local rotationTween = widget:addAnchoredTween(easeInOut, 800)
rotationTween:setRotation(360)  -- Rotação completa

-- Tween de opacidade
local opacityTween = widget:addAnchoredTween(easeInOut, 600)
opacityTween:setOpacity(0.5)
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
-- Tween simples de posição
local widget = g_ui.createWidget('UIWidget', parent)
local tween = widget:addAnchoredTween(easeInOut, 1000)  -- 1 segundo
tween:setPosition({x = 100, y = 100})

-- Tween de escala
local scaleTween = widget:addAnchoredTween(easeOutBack, 500)
scaleTween:setScale(1.5)

-- Tween de rotação
local rotationTween = widget:addAnchoredTween(easeInOut, 800)
rotationTween:setRotation(360)  -- Rotação completa

-- Tween de opacidade
local opacityTween = widget:addAnchoredTween(easeInOut, 600)
opacityTween:setOpacity(0.5)
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

### 🔄 **Tweens Múltiplos**

#### Nível Basic
```lua
-- Animar múltiplas propriedades simultaneamente
function animateWidget(widget, targetPos, targetScale, duration)
    duration = duration or 1000
    
    -- Tween de posição
    local posTween = widget:addAnchoredTween(easeOutBack, duration)
    posTween:setPosition(targetPos)
    
    -- Tween de escala
    local scaleTween = widget:addAnchoredTween(easeOutBack, duration)
    scaleTween:setScale(targetScale)
    
    -- Tween de rotação
    local rotationTween = widget:addAnchoredTween(easeInOut, duration)
    rotationTween:setRotation(180)
end

-- Sequência de tweens
function animateSequence(widget)
    -- Primeiro: mover
    local moveTween = widget:addAnchoredTween(easeInOut, 500)
    moveTween:setPosition({x = 200, y = 200})
    
    -- Segundo: escalar (após mover)
    scheduleEvent(function()
        local scaleTween = widget:addAnchoredTween(easeOutBack, 300)
        scaleTween:setScale(1.2)
    end, 500)
    
    -- Terceiro: rotacionar (após escalar)
    scheduleEvent(function()
        local rotationTween = widget:addAnchoredTween(easeInOut, 400)
        rotationTween:setRotation(360)
    end, 800)
end
```

#### Nível Intermediate
```lua
-- Animar múltiplas propriedades simultaneamente
function animateWidget(widget, targetPos, targetScale, duration)
    duration = duration or 1000
    
    -- Tween de posição
    local posTween = widget:addAnchoredTween(easeOutBack, duration)
    posTween:setPosition(targetPos)
    
    -- Tween de escala
    local scaleTween = widget:addAnchoredTween(easeOutBack, duration)
    scaleTween:setScale(targetScale)
    
    -- Tween de rotação
    local rotationTween = widget:addAnchoredTween(easeInOut, duration)
    rotationTween:setRotation(180)
end

-- Sequência de tweens
function animateSequence(widget)
    -- Primeiro: mover
    local moveTween = widget:addAnchoredTween(easeInOut, 500)
    moveTween:setPosition({x = 200, y = 200})
    
    -- Segundo: escalar (após mover)
    scheduleEvent(function()
        local scaleTween = widget:addAnchoredTween(easeOutBack, 300)
        scaleTween:setScale(1.2)
    end, 500)
    
    -- Terceiro: rotacionar (após escalar)
    scheduleEvent(function()
        local rotationTween = widget:addAnchoredTween(easeInOut, 400)
        rotationTween:setRotation(360)
    end, 800)
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
-- Animar múltiplas propriedades simultaneamente
function animateWidget(widget, targetPos, targetScale, duration)
    duration = duration or 1000
    
    -- Tween de posição
    local posTween = widget:addAnchoredTween(easeOutBack, duration)
    posTween:setPosition(targetPos)
    
    -- Tween de escala
    local scaleTween = widget:addAnchoredTween(easeOutBack, duration)
    scaleTween:setScale(targetScale)
    
    -- Tween de rotação
    local rotationTween = widget:addAnchoredTween(easeInOut, duration)
    rotationTween:setRotation(180)
end

-- Sequência de tweens
function animateSequence(widget)
    -- Primeiro: mover
    local moveTween = widget:addAnchoredTween(easeInOut, 500)
    moveTween:setPosition({x = 200, y = 200})
    
    -- Segundo: escalar (após mover)
    scheduleEvent(function()
        local scaleTween = widget:addAnchoredTween(easeOutBack, 300)
        scaleTween:setScale(1.2)
    end, 500)
    
    -- Terceiro: rotacionar (após escalar)
    scheduleEvent(function()
        local rotationTween = widget:addAnchoredTween(easeInOut, 400)
        rotationTween:setRotation(360)
    end, 800)
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

### 🎭 **Callbacks de Tween**

```lua
-- Tween com callback de início
local tween = widget:addAnchoredTween(easeInOut, 1000)
tween:setPosition({x = 100, y = 100})
tween.onStart = function()
    print("Animação iniciada!")
end

-- Tween com callback de progresso
    --  Tween com callback de progresso (traduzido)
local progressTween = widget:addAnchoredTween(easeInOut, 2000)
progressTween:setScale(2.0)
progressTween.onUpdate = function(progress)
    print("Progresso da animação:", progress * 100 .. "%")
end

-- Tween com callback de conclusão
local completeTween = widget:addAnchoredTween(easeInOut, 1500)
completeTween:setOpacity(0)
completeTween.onComplete = function()
    print("Animação concluída!")
    widget:hide()
end
```

---

## 📈 Funções de Easing

### 📊 **Tipos de Easing Disponíveis**

#### Nível Basic
```lua
-- Easing Linear (sem aceleração)
local linearTween = widget:addAnchoredTween(linear, 1000)

-- Easing In (aceleração)
local easeInTween = widget:addAnchoredTween(easeIn, 1000)

-- Easing Out (desaceleração)
local easeOutTween = widget:addAnchoredTween(easeOut, 1000)

-- Easing In-Out (aceleração + desaceleração)
local easeInOutTween = widget:addAnchoredTween(easeInOut, 1000)

-- Easing Back (efeito de "volta")
local easeOutBackTween = widget:addAnchoredTween(easeOutBack, 1000)

-- Easing Bounce (efeito de "quicar")
local easeOutBounceTween = widget:addAnchoredTween(easeOutBounce, 1000)

-- Easing Elastic (efeito elástico)
local easeOutElasticTween = widget:addAnchoredTween(easeOutElastic, 1000)
```

#### Nível Intermediate
```lua
-- Easing Linear (sem aceleração)
local linearTween = widget:addAnchoredTween(linear, 1000)

-- Easing In (aceleração)
local easeInTween = widget:addAnchoredTween(easeIn, 1000)

-- Easing Out (desaceleração)
local easeOutTween = widget:addAnchoredTween(easeOut, 1000)

-- Easing In-Out (aceleração + desaceleração)
local easeInOutTween = widget:addAnchoredTween(easeInOut, 1000)

-- Easing Back (efeito de "volta")
local easeOutBackTween = widget:addAnchoredTween(easeOutBack, 1000)

-- Easing Bounce (efeito de "quicar")
local easeOutBounceTween = widget:addAnchoredTween(easeOutBounce, 1000)

-- Easing Elastic (efeito elástico)
local easeOutElasticTween = widget:addAnchoredTween(easeOutElastic, 1000)
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
-- Easing Linear (sem aceleração)
local linearTween = widget:addAnchoredTween(linear, 1000)

-- Easing In (aceleração)
local easeInTween = widget:addAnchoredTween(easeIn, 1000)

-- Easing Out (desaceleração)
local easeOutTween = widget:addAnchoredTween(easeOut, 1000)

-- Easing In-Out (aceleração + desaceleração)
local easeInOutTween = widget:addAnchoredTween(easeInOut, 1000)

-- Easing Back (efeito de "volta")
local easeOutBackTween = widget:addAnchoredTween(easeOutBack, 1000)

-- Easing Bounce (efeito de "quicar")
local easeOutBounceTween = widget:addAnchoredTween(easeOutBounce, 1000)

-- Easing Elastic (efeito elástico)
local easeOutElasticTween = widget:addAnchoredTween(easeOutElastic, 1000)
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

### 🎨 **Aplicações Específicas**

```lua
-- Entrada suave (easeOut)
    --  Entrada suave (easeOut) (traduzido)
function animateEntry(widget)
    -- Função: animateEntry
    widget:setScale(0.0)
    widget:setOpacity(0.0)
    
    local tween = widget:addAnchoredTween(easeOutBack, 600)
    tween:setScale(1.0)
    tween:setOpacity(1.0)
end

-- Saída suave (easeIn)
function animateExit(widget)
    -- Função: animateExit
    local tween = widget:addAnchoredTween(easeInOut, 400)
    tween:setScale(0.8)
    tween:setOpacity(0.0)
end

-- Bounce para feedback (easeOutBounce)
    --  Bounce para feedback (easeOutBounce) (traduzido)
function animateBounce(widget)
    -- Função: animateBounce
    local tween = widget:addAnchoredTween(easeOutBounce, 800)
    tween:setScale(1.1)
    
    scheduleEvent(function()
        local returnTween = widget:addAnchoredTween(easeInOut, 400)
        returnTween:setScale(1.0)
    end, 800)
end

-- Elastic para destaque (easeOutElastic)
    --  Elastic para destaque (easeOutElastic) (traduzido)
function animateElastic(widget)
    -- Função: animateElastic
    local tween = widget:addAnchoredTween(easeOutElastic, 1200)
    tween:setScale(1.3)
    
    scheduleEvent(function()
        local returnTween = widget:addAnchoredTween(easeInOut, 600)
        returnTween:setScale(1.0)
    end, 1200)
end
```

---

## 🖥️ Animações de UI

### 🎭 **Transições de Widgets**

#### Inicialização e Configuração
```lua
-- Fade in/out
function fadeWidget(widget, fadeIn, duration)
    duration = duration or 300
    
    if fadeIn then
        widget:setOpacity(0.0)
        widget:show()
        
        local tween = widget:addAnchoredTween(easeInOut, duration)
        tween:setOpacity(1.0)
    else
        local tween = widget:addAnchoredTween(easeInOut, duration)
        tween:setOpacity(0.0)
        
        scheduleEvent(function()
            widget:hide()
        end, duration)
    end
end

-- Slide in/out
function slideWidget(widget, direction, slideIn, duration)
```

#### Funcionalidade 1
```lua
    duration = duration or 400
    
    local startPos = widget:getPosition()
    local offset = {x = 0, y = 0}
    
    if direction == 'left' then
        offset.x = -300
    elseif direction == 'right' then
        offset.x = 300
    elseif direction == 'up' then
        offset.y = -200
    elseif direction == 'down' then
        offset.y = 200
    end
    
    if slideIn then
        widget:setPosition({x = startPos.x + offset.x, y = startPos.y + offset.y})
        widget:show()
        
        local tween = widget:addAnchoredTween(easeOutBack, duration)
        tween:setPosition(startPos)
    else
        local tween = widget:addAnchoredTween(easeInOut, duration)
        tween:setPosition({x = startPos.x + offset.x, y = startPos.y + offset.y})
        
        scheduleEvent(function()
            widget:hide()
        end, duration)
```

#### Funcionalidade 2
```lua
    end
end

-- Scale in/out
function scaleWidget(widget, scaleIn, duration)
    duration = duration or 300
    
    if scaleIn then
        widget:setScale(0.0)
        widget:show()
        
        local tween = widget:addAnchoredTween(easeOutBack, duration)
        tween:setScale(1.0)
    else
        local tween = widget:addAnchoredTween(easeInOut, duration)
        tween:setScale(0.0)
        
        scheduleEvent(function()
            widget:hide()
        end, duration)
    end
```

#### Finalização
```lua
end
```

### 🎨 **Animações de Hover**

```lua
-- Setup hover animations
    --  Setup hover animations (traduzido)
function setupHoverAnimations(widget)
    -- Função: setupHoverAnimations
    widget.onHoverChange = function(widget, hovered)
        if hovered then
    -- Verificação condicional
            -- Hover in
    --  Hover in (traduzido)
            local tween = widget:addAnchoredTween(easeOutBack, 200)
            tween:setScale(1.05)
            tween:setOpacity(0.9)
        else
            -- Hover out
    --  Hover out (traduzido)
            local tween = widget:addAnchoredTween(easeInOut, 200)
            tween:setScale(1.0)
            tween:setOpacity(1.0)
        end
    end
end

-- Setup click animations
    --  Setup click animations (traduzido)
function setupClickAnimations(widget)
    -- Função: setupClickAnimations
    widget.onClick = function(widget)
        -- Click feedback
    --  Click feedback (traduzido)
        local tween = widget:addAnchoredTween(easeOutBack, 150)
        tween:setScale(0.95)
        
        scheduleEvent(function()
            local returnTween = widget:addAnchoredTween(easeInOut, 150)
            returnTween:setScale(1.0)
        end, 150)
    end
end
```

---

## 🎬 Transições de Tela

### 🔄 **Transições Entre Telas**

#### Inicialização e Configuração
```lua
-- Fade transition
function fadeTransition(fromWidget, toWidget, duration)
    duration = duration or 500
    
    -- Fade out current screen
    local fadeOutTween = fromWidget:addAnchoredTween(easeInOut, duration)
    fadeOutTween:setOpacity(0)
    
    -- Fade in new screen
    scheduleEvent(function()
        toWidget:show()
        toWidget:setOpacity(0)
        
        local fadeInTween = toWidget:addAnchoredTween(easeInOut, duration)
        fadeInTween:setOpacity(1)
        
        scheduleEvent(function()
            fromWidget:hide()
        end, duration)
    end, duration)
end
```

#### Funcionalidade 1
```lua

-- Slide transition
function slideTransition(fromWidget, toWidget, direction, duration)
    duration = duration or 400
    
    local distance = 400
    local fromOffset = {x = 0, y = 0}
    local toOffset = {x = 0, y = 0}
    
    if direction == 'left' then
        fromOffset.x = distance
        toOffset.x = -distance
    elseif direction == 'right' then
        fromOffset.x = -distance
        toOffset.x = distance
    elseif direction == 'up' then
        fromOffset.y = distance
        toOffset.y = -distance
    elseif direction == 'down' then
        fromOffset.y = -distance
        toOffset.y = distance
    end
```

#### Funcionalidade 2
```lua
    
    -- Slide out current screen
    local slideOutTween = fromWidget:addAnchoredTween(easeInOut, duration)
    slideOutTween:setMarginLeft(fromOffset.x)
    slideOutTween:setMarginTop(fromOffset.y)
    
    -- Slide in new screen
    scheduleEvent(function()
        toWidget:show()
        toWidget:setMarginLeft(toOffset.x)
        toWidget:setMarginTop(toOffset.y)
        
        local slideInTween = toWidget:addAnchoredTween(easeInOut, duration)
        slideInTween:setMarginLeft(0)
        slideInTween:setMarginTop(0)
        
        scheduleEvent(function()
            fromWidget:hide()
        end, duration)
    end, duration)
end
```

#### Funcionalidade 3
```lua

-- Scale transition
function scaleTransition(fromWidget, toWidget, duration)
    duration = duration or 300
    
    -- Scale out current screen
    local scaleOutTween = fromWidget:addAnchoredTween(easeInOut, duration)
    scaleOutTween:setScale(0.8)
    scaleOutTween:setOpacity(0)
    
    -- Scale in new screen
    scheduleEvent(function()
        toWidget:show()
        toWidget:setScale(0.8)
        toWidget:setOpacity(0)
        
        local scaleInTween = toWidget:addAnchoredTween(easeOutBack, duration)
        scaleInTween:setScale(1.0)
        scaleInTween:setOpacity(1)
        
        scheduleEvent(function()
            fromWidget:hide()
        end, duration)
```

#### Finalização
```lua
    end, duration)
end
```

---

## 🎨 Animações de Widgets

### 🎯 **Animações de Loading**

#### Inicialização e Configuração
```lua
-- Spinning loader
function createSpinner(parent)
    local spinner = g_ui.createWidget('UIWidget', parent)
    spinner:setSize({width = 32, height = 32})
    spinner:setImageSource('/images/ui/spinner')
    
    local function rotate()
        local currentRotation = spinner:getRotation()
        spinner:setRotation(currentRotation + 30)
        scheduleEvent(rotate, 100)
    end
    
    rotate()
    return spinner
end

-- Pulsing loader
function createPulsingLoader(parent)
    local loader = g_ui.createWidget('UIWidget', parent)
    loader:setSize({width = 40, height = 40})
    loader:setImageSource('/images/ui/loader')
    
    local function pulse()
        local tween = loader:addAnchoredTween(easeInOut, 1000)
        tween:setScale(1.2)
        tween:setOpacity(0.5)
        
        scheduleEvent(function()
            local returnTween = loader:addAnchoredTween(easeInOut, 1000)
            returnTween:setScale(1.0)
            returnTween:setOpacity(1.0)
            
            scheduleEvent(pulse, 1000)
        end, 1000)
```

#### Finalização
```lua
    end
    
    pulse()
    return loader
end

-- Progress bar animation
function animateProgressBar(progressBar, targetValue, duration)
    duration = duration or 1000
    
    local startValue = progressBar:getValue()
    local valueDiff = targetValue - startValue
    
    local function updateProgress(progress)
        local currentValue = startValue + (valueDiff * progress)
        progressBar:setValue(currentValue)
    end
    
    local tween = progressBar:addAnchoredTween(easeInOut, duration)
    tween.onUpdate = updateProgress
end
```

### 🎭 **Animações de Feedback**

#### Inicialização e Configuração
```lua
-- Shake animation
function shakeWidget(widget, intensity, duration)
    intensity = intensity or 10
    duration = duration or 500
    
    local originalPos = widget:getPosition()
    local steps = math.floor(duration / 50)
    
    for i = 1, steps do
        scheduleEvent(function()
            local offset = math.sin(i * 0.5) * intensity
            widget:setPosition({x = originalPos.x + offset, y = originalPos.y})
        end, i * 50)
    end
    
    scheduleEvent(function()
        widget:setPosition(originalPos)
    end, duration)
end

-- Bounce animation
function bounceWidget(widget, height, duration)
```

#### Funcionalidade 1
```lua
    height = height or 20
    duration = duration or 600
    
    local originalPos = widget:getPosition()
    
    -- Bounce up
    local upTween = widget:addAnchoredTween(easeOutBack, duration / 2)
    upTween:setPosition({x = originalPos.x, y = originalPos.y - height})
    
    -- Bounce down
    scheduleEvent(function()
        local downTween = widget:addAnchoredTween(easeInOut, duration / 2)
        downTween:setPosition(originalPos)
    end, duration / 2)
end

-- Pulse animation
function pulseWidget(widget, scale, duration)
    scale = scale or 1.1
    duration = duration or 400
    
    local tween = widget:addAnchoredTween(easeInOut, duration)
    tween:setScale(scale)
    
    scheduleEvent(function()
        local returnTween = widget:addAnchoredTween(easeInOut, duration)
        returnTween:setScale(1.0)
    end, duration)
```

#### Finalização
```lua
end
```

---

## ⏱️ Controle de Timing

### 🎯 **Timing Preciso**

```lua
-- Animações com timing específico
function timedAnimation(widget, sequence)
    -- Função: timedAnimation
    local currentTime = 0
    
    for _, step in ipairs(sequence) do
    -- Loop de repetição
        scheduleEvent(function()
            local tween = widget:addAnchoredTween(step.easing, step.duration)
            
            if step.property == 'position' then
    -- Verificação condicional
                tween:setPosition(step.value)
            elseif step.property == 'scale' then
                tween:setScale(step.value)
            elseif step.property == 'rotation' then
                tween:setRotation(step.value)
            elseif step.property == 'opacity' then
                tween:setOpacity(step.value)
            end
        end, currentTime)
        
        currentTime = currentTime + step.delay
    end
end

-- Exemplo de uso
    --  Exemplo de uso (traduzido)
local animationSequence = {
    {property = 'position', value = {x = 100, y = 100}, easing = easeOutBack, duration = 500, delay = 0},
    {property = 'scale', value = 1.2, easing = easeInOut, duration = 300, delay = 200},
    {property = 'rotation', value = 180, easing = easeInOut, duration = 400, delay = 100},
    {property = 'opacity', value = 0.8, easing = easeInOut, duration = 200, delay = 300}
}

timedAnimation(myWidget, animationSequence)
```

### 🔄 **Loops e Repetições**

```lua
-- Animation loop
    --  Animation loop (traduzido)
function createAnimationLoop(widget, animation, interval)
    -- Função: createAnimationLoop
    interval = interval or 2000
    
    local function loop()
        animation(widget)
        scheduleEvent(loop, interval)
    end
    
    loop()
end

-- Breathe animation
    --  Breathe animation (traduzido)
function breatheAnimation(widget)
    -- Função: breatheAnimation
    local tween = widget:addAnchoredTween(easeInOut, 2000)
    tween:setScale(1.05)
    tween:setOpacity(0.8)
    
    scheduleEvent(function()
        local returnTween = widget:addAnchoredTween(easeInOut, 2000)
        returnTween:setScale(1.0)
        returnTween:setOpacity(1.0)
    end, 2000)
end

-- Start breathing loop
    --  Start breathing loop (traduzido)
createAnimationLoop(myWidget, breatheAnimation, 4000)
```

---

## ⚡ Performance e Otimização

### 🚀 **Otimizações de Performance**

```lua
-- Animation pool
    --  Animation pool (traduzido)
local AnimationPool = {}
AnimationPool.tweens = {}

function AnimationPool.getTween()
    -- Função: AnimationPool
    if #AnimationPool.tweens > 0 then
    -- Verificação condicional
        return table.remove(AnimationPool.tweens)
    else
        return nil  -- Create new tween
    end
end

function AnimationPool.releaseTween(tween)
    -- Função: AnimationPool
    tween:stop()
    table.insert(AnimationPool.tweens, tween)
end

-- Limit concurrent animations
    --  Limit concurrent animations (traduzido)
local MAX_CONCURRENT_ANIMATIONS = 20
local currentAnimations = 0

function canStartAnimation()
    -- Função: canStartAnimation
    return currentAnimations < MAX_CONCURRENT_ANIMATIONS
end

function startAnimation(widget, animation)
    -- Função: startAnimation
    if canStartAnimation() then
    -- Verificação condicional
        currentAnimations = currentAnimations + 1
        animation(widget)
        
        scheduleEvent(function()
            currentAnimations = currentAnimations - 1
        end, 1000)  -- Assume 1 second duration
        
        return true
    end
    return false
end
```

### 🎯 **Configurações de Performance**

```lua
-- Disable animations on low-end devices
    --  Disable animations on low-end devices (traduzido)
function shouldAnimate()
    -- Função: shouldAnimate
    local fps = g_app.getFps()
    local quality = g_settings.getString("graphics.quality")
    
    return fps > 30 and quality ~= "low"
end

-- Conditional animation
    --  Conditional animation (traduzido)
function conditionalAnimate(widget, animation)
    -- Função: conditionalAnimate
    if shouldAnimate() then
    -- Verificação condicional
        animation(widget)
    else
        -- Apply final state immediately
    --  Apply final state immediately (traduzido)
        widget:setPosition({x = 100, y = 100})
        widget:setScale(1.0)
    end
end
```

---

### 🎮 **Sistema de Menu Animado**

```lua
-- Animated menu system
    --  Animated menu system (traduzido)
local AnimatedMenu = {}

function AnimatedMenu.create()
    -- Função: AnimatedMenu
    local menu = g_ui.createWidget('Panel', rootWidget)
    menu:setSize({width = 200, height = 300})
    menu:setPosition({x = 10, y = 10})
    
    -- Add menu items with animations
    --  Add menu items with animations (traduzido)
    local items = {'Item 1', 'Item 2', 'Item 3', 'Item 4'}
    
    for i, itemText in ipairs(items) do
    -- Loop de repetição
        local item = g_ui.createWidget('Button', menu)
        item:setText(itemText)
        item:setPosition({x = 10, y = 10 + (i-1) * 40})
        
        -- Staggered entry animation
    --  Staggered entry animation (traduzido)
        scheduleEvent(function()
            item:setOpacity(0)
            item:setMarginLeft(-50)
            
            local tween = item:addAnchoredTween(easeOutBack, 400)
            tween:setOpacity(1)
            tween:setMarginLeft(0)
        end, i * 100)
        
        -- Hover animation
    --  Hover animation (traduzido)
        item.onHoverChange = function(widget, hovered)
            if hovered then
    -- Verificação condicional
                local tween = widget:addAnchoredTween(easeOutBack, 200)
                tween:setMarginLeft(10)
                tween:setScale(1.05)
            else
                local tween = widget:addAnchoredTween(easeInOut, 200)
                tween:setMarginLeft(0)
                tween:setScale(1.0)
            end
        end
    end
    
    return menu
end
```

### 🎨 **Sistema de Notificações Animadas**

```lua
-- Animated notification system
    --  Animated notification system (traduzido)
local NotificationSystem = {}

function NotificationSystem.show(message, type, duration)
    -- Função: NotificationSystem
    duration = duration or 3000
    
    local notification = g_ui.createWidget('Panel', rootWidget)
    notification:setSize({width = 300, height = 60})
    notification:setPosition({x = g_window.getWidth() - 320, y = 20})
    
    local label = g_ui.createWidget('Label', notification)
    label:setText(message)
    label:setPosition({x = 10, y = 20})
    
    -- Set background color based on type
    --  Set background color based on type (traduzido)
    if type == 'success' then
    -- Verificação condicional
        notification:setBackgroundColor('#00FF00')
    elseif type == 'error' then
        notification:setBackgroundColor('#FF0000')
    elseif type == 'warning' then
        notification:setBackgroundColor('#FFFF00')
    end
    
    -- Entry animation
    --  Entry animation (traduzido)
    notification:setOpacity(0)
    notification:setMarginTop(-60)
    
    local entryTween = notification:addAnchoredTween(easeOutBack, 400)
    entryTween:setOpacity(1)
    entryTween:setMarginTop(0)
    
    -- Exit animation
    --  Exit animation (traduzido)
    scheduleEvent(function()
        local exitTween = notification:addAnchoredTween(easeInOut, 300)
        exitTween:setOpacity(0)
        exitTween:setMarginTop(-60)
        
        scheduleEvent(function()
            notification:destroy()
        end, 300)
    end, duration)
end
```

### 🎭 **Sistema de Loading Animado**

```lua
-- Animated loading system
    --  Animated loading system (traduzido)
local LoadingSystem = {}

function LoadingSystem.create(parent)
    -- Função: LoadingSystem
    local loading = g_ui.createWidget('Panel', parent)
    loading:setSize({width = 200, height = 100})
    loading:setPosition({x = 50, y = 50})
    loading:setBackgroundColor('#000000')
    loading:setOpacity(0.8)
    
    local spinner = g_ui.createWidget('UIWidget', loading)
    spinner:setSize({width = 32, height = 32})
    spinner:setPosition({x = 84, y = 20})
    spinner:setImageSource('/images/ui/spinner')
    
    local text = g_ui.createWidget('Label', loading)
    text:setText('Carregando...')
    text:setPosition({x = 70, y = 60})
    text:setColor('#FFFFFF')
    
    -- Rotate spinner
    --  Rotate spinner (traduzido)
    local function rotate()
        local currentRotation = spinner:getRotation()
        spinner:setRotation(currentRotation + 30)
        scheduleEvent(rotate, 100)
    end
    
    rotate()
    
    -- Pulse text
    --  Pulse text (traduzido)
    local function pulseText()
        local tween = text:addAnchoredTween(easeInOut, 1000)
        tween:setOpacity(0.5)
        
        scheduleEvent(function()
            local returnTween = text:addAnchoredTween(easeInOut, 1000)
            returnTween:setOpacity(1.0)
            scheduleEvent(pulseText, 1000)
        end, 1000)
    end
    
    pulseText()
    
    return loading
end
```

---

## ✅ Melhores Práticas

### 🎯 **Uso Eficiente de Animações**

#### Nível Basic
```lua
-- ✅ BOM: Usar durações apropriadas
local SHORT_ANIMATION = 200   -- Feedback rápido
local MEDIUM_ANIMATION = 500  -- Transições normais
local LONG_ANIMATION = 1000   -- Animações complexas
-- ✅ BOM: Usar easing apropriado
function animateEntry(widget)
    local tween = widget:addAnchoredTween(easeOutBack, MEDIUM_ANIMATION)
end
function animateExit(widget)
    local tween = widget:addAnchoredTween(easeInOut, SHORT_ANIMATION)
end
-- ✅ BOM: Limpar animações automaticamente
function safeAnimate(widget, animation)
    if widget:isDestroyed() then return end
end
-- ❌ EVITE: Animações muito longas
local tween = widget:addAnchoredTween(easeInOut, 5000)  -- 5s é muito
-- ❌ EVITE: Muitas animações simultâneas
    local tween = widget:addAnchoredTween(easeInOut, 1000)
end
```

#### Nível Intermediate
```lua
-- ✅ BOM: Usar durações apropriadas
local SHORT_ANIMATION = 200   -- Feedback rápido
local MEDIUM_ANIMATION = 500  -- Transições normais
local LONG_ANIMATION = 1000   -- Animações complexas

-- ✅ BOM: Usar easing apropriado
function animateEntry(widget)
    local tween = widget:addAnchoredTween(easeOutBack, MEDIUM_ANIMATION)
    tween:setScale(1.0)
end

function animateExit(widget)
    local tween = widget:addAnchoredTween(easeInOut, SHORT_ANIMATION)
    tween:setOpacity(0)
end

-- ✅ BOM: Limpar animações automaticamente
function safeAnimate(widget, animation)
    if widget:isDestroyed() then return end
    
    animation(widget)
end

-- ❌ EVITE: Animações muito longas
local tween = widget:addAnchoredTween(easeInOut, 5000)  -- 5s é muito

-- ❌ EVITE: Muitas animações simultâneas
for i = 1, 100 do
    local tween = widget:addAnchoredTween(easeInOut, 1000)
end
```

#### Nível Advanced
```lua
-- ✅ BOM: Usar durações apropriadas
local SHORT_ANIMATION = 200   -- Feedback rápido
local MEDIUM_ANIMATION = 500  -- Transições normais
local LONG_ANIMATION = 1000   -- Animações complexas

-- ✅ BOM: Usar easing apropriado
function animateEntry(widget)
    local tween = widget:addAnchoredTween(easeOutBack, MEDIUM_ANIMATION)
    tween:setScale(1.0)
end

function animateExit(widget)
    local tween = widget:addAnchoredTween(easeInOut, SHORT_ANIMATION)
    tween:setOpacity(0)
end

-- ✅ BOM: Limpar animações automaticamente
function safeAnimate(widget, animation)
    if widget:isDestroyed() then return end
    
    animation(widget)
end

-- ❌ EVITE: Animações muito longas
local tween = widget:addAnchoredTween(easeInOut, 5000)  -- 5s é muito

-- ❌ EVITE: Muitas animações simultâneas
for i = 1, 100 do
    local tween = widget:addAnchoredTween(easeInOut, 1000)
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

### 🔧 **Configuração Adequada**

```lua
-- ✅ BOM: Verificar performance
    --  ✅ BOM: Verificar performance (traduzido)
if shouldAnimate() then
    -- Verificação condicional
    startAnimation(widget, myAnimation)
else
    applyFinalState(widget)
end

-- ✅ BOM: Usar callbacks apropriados
    --  ✅ BOM: Usar callbacks apropriados (traduzido)
local tween = widget:addAnchoredTween(easeInOut, 1000)
tween.onComplete = function()
    widget:hide()
    cleanup()
end

-- ✅ BOM: Cancelar animações quando necessário
function cancelWidgetAnimations(widget)
    -- Função: cancelWidgetAnimations
    widget:stopAllTweens()
end
```

### 🎨 **Design Consistente**

```lua
-- ✅ BOM: Usar constantes para animações
local ANIMATION_CONFIG = {
    ENTRY_DURATION = 400,
    EXIT_DURATION = 300,
    HOVER_DURATION = 200,
    FEEDBACK_DURATION = 150
}

-- ✅ BOM: Usar easing consistente
    --  ✅ BOM: Usar easing consistente (traduzido)
local ANIMATION_EASING = {
    ENTRY = easeOutBack,
    EXIT = easeInOut,
    HOVER = easeOutBack,
    FEEDBACK = easeInOut
}

-- ✅ BOM: Funções de animação padronizadas
function animateWidgetEntry(widget)
    -- Função: animateWidgetEntry
    local tween = widget:addAnchoredTween(ANIMATION_EASING.ENTRY, ANIMATION_CONFIG.ENTRY_DURATION)
    tween:setScale(1.0)
    tween:setOpacity(1.0)
end

function animateWidgetExit(widget)
    -- Função: animateWidgetExit
    local tween = widget:addAnchoredTween(ANIMATION_EASING.EXIT, ANIMATION_CONFIG.EXIT_DURATION)
    tween:setScale(0.8)
    tween:setOpacity(0)
end
```

O sistema de animações do OTClient oferece ferramentas poderosas para criar interfaces fluidas e responsivas. Use estas práticas para garantir performance e consistência em suas aplicações. 
> - [Getting_Started_Guide](Getting_Started_Guide.md) - Comece aqui
> - [Module_System_Guide](Module_System_Guide.md) - Sistema de módulos
> - [UI_System_Guide](UI_System_Guide.md) - Interface do usuário
> - [Lua_API_Reference](Lua_API_Reference.md) - Referência da API

---

<div class="success"> **Navegação**
> **📚 Documentos Relacionados:**
> - [Getting_Started_Guide](Getting_Started_Guide.md) - Comece aqui
> - [Module_System_Guide](Module_System_Guide.md) - Sistema de módulos
> - [UI_System_Guide](UI_System_Guide.md) - Interface do usuário
> - [Lua_API_Reference](Lua_API_Reference.md) - API completa
> 
> **🔗 Navegação Rápida:**
> - [Wiki_Index](Wiki_Index.md) - Voltar ao índice
> - [Cheat_Sheet](Cheat_Sheet.md) - Referência rápida
> - [Debug_System_Guide](Debug_System_Guide.md) - Debugging


## 🔗 **Links Automáticos**

> [!info] **Links Gerados Automaticamente**
> Estes links foram criados automaticamente pelo sistema de linkagem da categoria **Legacy**

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]
- [[../maps/search_index|Busca em Arquivos Legados]]
- [[../legacy_docs/README|Documentação Legada]]

### **🧭 Navegação**
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]
- [[../maps/category_indices|Índices por Categoria]]
- [[../maps/relationships|Relacionamentos]]

### **📊 Métricas da Categoria**
- **Categoria**: Legacy
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

