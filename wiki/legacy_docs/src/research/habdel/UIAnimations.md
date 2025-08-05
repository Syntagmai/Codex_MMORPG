
# 🎬 UI-010: Sistema de Animações

<div class="info"> **Story ID**: UI-010  
> **Categoria**: UI  
> **Status**: ✅ Completo  
> **Prioridade**: 🔥 **MÁXIMA**

## 📋 Índice
1. [Visão Geral](#visão-geral)
2. [Arquitetura do Sistema](#arquitetura-do-sistema)
3. [Sistema de Tweening](#sistema-de-tweening)
4. [Funções de Easing](#funções-de-easing)
5. [API Lua](#api-lua)
6. [Animações de UI](#animações-de-ui)
7. [Exemplos Práticos](#exemplos-práticos)
8. [Performance e Otimização](#performance-e-otimização)
9. [Melhores Práticas](#melhores-práticas)

---

## 🎯 Visão Geral

O **Sistema de Animações** do OTClient oferece um framework completo para criar transições suaves, efeitos visuais dinâmicos e animações responsivas nos widgets da interface. O sistema é baseado em **tweening** e **easing functions** para proporcionar animações naturais e fluidas.

### 🎨 **Características Principais**

- **Tweening Avançado**: Animações suaves entre valores
- **Funções de Easing**: Curvas de animação naturais e realistas
- **Animações de UI**: Transições de widgets e interfaces
- **Controle de Timing**: Precisão temporal nas animações
- **Performance Otimizada**: Animações eficientes e responsivas
- **Callbacks de Eventos**: Controle completo do ciclo de vida das animações

---

## 🏗️ Arquitetura do Sistema

### 🎭 **Estrutura Hierárquica**

```
Sistema de Animações
   │
   ├─ Tween Engine
   │   ├─ Interpolação de valores
   │   ├─ Controle de timing
   │   ├─ Callbacks de eventos
   │   └─ Gerenciamento de estado
   │
   ├─ Easing Functions
   │   ├─ Linear (sem aceleração)
   │   ├─ Ease In (aceleração)
   │   ├─ Ease Out (desaceleração)
   │   ├─ Ease In-Out (aceleração + desaceleração)
   │   ├─ Ease Back (efeito de "volta")
   │   ├─ Ease Bounce (efeito de "quicar")
   │   └─ Ease Elastic (efeito elástico)
   │
   ├─ UI Animations
   │   ├─ Transições de widgets
   │   ├─ Animações de entrada/saída
   │   ├─ Feedback visual
   │   └─ Loading animations
   │
   └─ Animation Manager
       ├─ Pool de animações
       ├─ Controle de performance
       ├─ Limpeza automática
       └─ Gerenciamento de memória
```

### 🔄 **Fluxo de Animação**

```
1. Criação do Tween
   ↓
2. Configuração de Propriedades
   ↓
3. Aplicação de Easing
   ↓
4. Execução da Animação
   ↓
5. Callbacks de Progresso
   ↓
6. Callback de Conclusão
   ↓
7. Limpeza Automática
```

---

## ⚡ Sistema de Tweening

### 🎯 **Criando Tweens Básicos**

O sistema de tweening permite animar propriedades de widgets de forma suave e controlada.

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

As funções de easing controlam como a animação progride ao longo do tempo, criando curvas de animação naturais.

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

## 🐍 API Lua

### 📦 **Métodos de Animação**

#### Nível Basic
```lua
-- Criar tween básico
local tween = widget:addAnchoredTween(easing, duration)

-- Propriedades animáveis
tween:setPosition({x = 100, y = 100})
tween:setScale(1.5)
tween:setRotation(180)
tween:setOpacity(0.8)

-- Callbacks
tween.onStart = function() end
tween.onUpdate = function(progress) end
tween.onComplete = function() end

-- Controle de animação
widget:stopAllTweens()  -- Parar todas as animações
widget:stopTween(tween) -- Parar animação específica
```

#### Nível Intermediate
```lua
-- Criar tween básico
local tween = widget:addAnchoredTween(easing, duration)

-- Propriedades animáveis
tween:setPosition({x = 100, y = 100})
tween:setScale(1.5)
tween:setRotation(180)
tween:setOpacity(0.8)

-- Callbacks
tween.onStart = function() end
tween.onUpdate = function(progress) end
tween.onComplete = function() end

-- Controle de animação
widget:stopAllTweens()  -- Parar todas as animações
widget:stopTween(tween) -- Parar animação específica
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
-- Criar tween básico
local tween = widget:addAnchoredTween(easing, duration)

-- Propriedades animáveis
tween:setPosition({x = 100, y = 100})
tween:setScale(1.5)
tween:setRotation(180)
tween:setOpacity(0.8)

-- Callbacks
tween.onStart = function() end
tween.onUpdate = function(progress) end
tween.onComplete = function() end

-- Controle de animação
widget:stopAllTweens()  -- Parar todas as animações
widget:stopTween(tween) -- Parar animação específica
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

### 🎯 **Animações Especializadas**

#### Inicialização e Configuração
```lua
-- Animação de fade in/out
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

-- Animação de slide
function slideWidget(widget, direction, slideIn, duration)
```

#### Funcionalidade 1
```lua
    duration = duration or 400
    
    local startPos = widget:getPosition()
    local targetPos = {x = startPos.x, y = startPos.y}
    
    if direction == 'left' then
        targetPos.x = slideIn and 0 or -widget:getWidth()
    elseif direction == 'right' then
        targetPos.x = slideIn and 0 or widget:getParent():getWidth()
    elseif direction == 'up' then
        targetPos.y = slideIn and 0 or -widget:getHeight()
    elseif direction == 'down' then
        targetPos.y = slideIn and 0 or widget:getParent():getHeight()
    end
    
    if slideIn then
        widget:setPosition(targetPos)
        widget:show()
        
        local tween = widget:addAnchoredTween(easeOutBack, duration)
        tween:setPosition(startPos)
    else
        local tween = widget:addAnchoredTween(easeInOut, duration)
        tween:setPosition(targetPos)
        
        scheduleEvent(function()
            widget:hide()
        end, duration)
```

#### Finalização
```lua
    end
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
    local targetPos = {x = startPos.x, y = startPos.y}
    
    if direction == 'left' then
        targetPos.x = slideIn and 0 or -widget:getWidth()
    elseif direction == 'right' then
        targetPos.x = slideIn and 0 or widget:getParent():getWidth()
    elseif direction == 'up' then
        targetPos.y = slideIn and 0 or -widget:getHeight()
    elseif direction == 'down' then
        targetPos.y = slideIn and 0 or widget:getParent():getHeight()
    end
    
    if slideIn then
        widget:setPosition(targetPos)
        widget:show()
        
        local tween = widget:addAnchoredTween(easeOutBack, duration)
        tween:setPosition(startPos)
    else
        local tween = widget:addAnchoredTween(easeInOut, duration)
        tween:setPosition(targetPos)
        
        scheduleEvent(function()
            widget:hide()
        end, duration)
```

#### Funcionalidade 2
```lua
    end
end

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

### 🎨 **Animações de Loading**

```lua
-- Spinning loader
    --  Spinning loader (traduzido)
function createSpinner(parent)
    -- Função: createSpinner
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
    --  Pulsing loader (traduzido)
function createPulsingLoader(parent)
    -- Função: createPulsingLoader
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
    end
    
    pulse()
    return loader
end

-- Progress bar animation
    --  Progress bar animation (traduzido)
function animateProgressBar(progressBar, targetValue, duration)
    -- Função: animateProgressBar
    duration = duration or 1000
    
    local currentValue = progressBar:getValue() or 0
    local tween = progressBar:addAnchoredTween(easeInOut, duration)
    tween:setValue(targetValue)
end
```

---

## 💡 Exemplos Práticos

### 🎯 **Exemplo 1: Sistema de Notificações Animadas**

#### Nível Basic
```lua
local NotificationSystem = {}

function NotificationSystem.show(text, type, duration)
    duration = duration or 3000
    
    -- Criar notificação
    local notification = g_ui.createWidget('Panel')
    notification:setSize({width = 300, height = 60})
    notification:setPosition({x = 50, y = 50})
    notification:setBackgroundColor('#2C3E50')
    notification:setOpacity(0)
    
    -- Adicionar texto
    local textWidget = g_ui.createWidget('Label', notification)
    textWidget:setText(text)
    textWidget:setPosition({x = 10, y = 20})
    textWidget:setColor('#FFFFFF')
    
    -- Animação de entrada
    local entryTween = notification:addAnchoredTween(easeOutBack, 500)
    entryTween:setOpacity(1.0)
    entryTween:setPosition({x = 50, y = 100})
    
    -- Animação de saída
    scheduleEvent(function()
        local exitTween = notification:addAnchoredTween(easeInOut, 300)
        exitTween:setOpacity(0)
        exitTween:setPosition({x = 50, y = 50})
        
        exitTween.onComplete = function()
            notification:destroy()
        end
    end, duration)
    
    return notification
end

-- Uso
NotificationSystem.show('Mensagem de sucesso!', 'success', 3000)
```

#### Nível Intermediate
```lua
local NotificationSystem = {}

function NotificationSystem.show(text, type, duration)
    duration = duration or 3000
    
    -- Criar notificação
    local notification = g_ui.createWidget('Panel')
    notification:setSize({width = 300, height = 60})
    notification:setPosition({x = 50, y = 50})
    notification:setBackgroundColor('#2C3E50')
    notification:setOpacity(0)
    
    -- Adicionar texto
    local textWidget = g_ui.createWidget('Label', notification)
    textWidget:setText(text)
    textWidget:setPosition({x = 10, y = 20})
    textWidget:setColor('#FFFFFF')
    
    -- Animação de entrada
    local entryTween = notification:addAnchoredTween(easeOutBack, 500)
    entryTween:setOpacity(1.0)
    entryTween:setPosition({x = 50, y = 100})
    
    -- Animação de saída
    scheduleEvent(function()
        local exitTween = notification:addAnchoredTween(easeInOut, 300)
        exitTween:setOpacity(0)
        exitTween:setPosition({x = 50, y = 50})
        
        exitTween.onComplete = function()
            notification:destroy()
        end
    end, duration)
    
    return notification
end

-- Uso
NotificationSystem.show('Mensagem de sucesso!', 'success', 3000)
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
local NotificationSystem = {}

function NotificationSystem.show(text, type, duration)
    duration = duration or 3000
    
    -- Criar notificação
    local notification = g_ui.createWidget('Panel')
    notification:setSize({width = 300, height = 60})
    notification:setPosition({x = 50, y = 50})
    notification:setBackgroundColor('#2C3E50')
    notification:setOpacity(0)
    
    -- Adicionar texto
    local textWidget = g_ui.createWidget('Label', notification)
    textWidget:setText(text)
    textWidget:setPosition({x = 10, y = 20})
    textWidget:setColor('#FFFFFF')
    
    -- Animação de entrada
    local entryTween = notification:addAnchoredTween(easeOutBack, 500)
    entryTween:setOpacity(1.0)
    entryTween:setPosition({x = 50, y = 100})
    
    -- Animação de saída
    scheduleEvent(function()
        local exitTween = notification:addAnchoredTween(easeInOut, 300)
        exitTween:setOpacity(0)
        exitTween:setPosition({x = 50, y = 50})
        
        exitTween.onComplete = function()
            notification:destroy()
        end
    end, duration)
    
    return notification
end

-- Uso
NotificationSystem.show('Mensagem de sucesso!', 'success', 3000)
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

### 🎨 **Exemplo 2: Menu Animado**

```lua
local AnimatedMenu = {}

function AnimatedMenu.create(parent)
    -- Função: AnimatedMenu
    local menu = g_ui.createWidget('Panel', parent)
    menu:setSize({width = 200, height = 300})
    menu:setPosition({x = 0, y = 0})
    menu:setBackgroundColor('#34495E')
    menu:setOpacity(0)
    menu:setScale(0.8)
    
    -- Adicionar itens do menu
    --  Adicionar itens do menu (traduzido)
    local menuItems = {'Início', 'Perfil', 'Configurações', 'Sair'}
    
    for i, itemText in ipairs(menuItems) do
    -- Loop de repetição
        local item = g_ui.createWidget('Button', menu)
        item:setText(itemText)
        item:setPosition({x = 10, y = (i-1) * 50 + 20})
        item:setSize({width = 180, height = 40})
        item:setOpacity(0)
        item:setScale(0.5)
        
        -- Animação de entrada escalonada
        scheduleEvent(function()
            local itemTween = item:addAnchoredTween(easeOutBack, 400)
            itemTween:setOpacity(1.0)
            itemTween:setScale(1.0)
        end, i * 100)
    end
    
    -- Animação de entrada do menu
    local menuTween = menu:addAnchoredTween(easeOutBack, 600)
    menuTween:setOpacity(1.0)
    menuTween:setScale(1.0)
    
    return menu
end

function AnimatedMenu.hide(menu)
    -- Função: AnimatedMenu
    local menuTween = menu:addAnchoredTween(easeInOut, 400)
    menuTween:setOpacity(0)
    menuTween:setScale(0.8)
    
    menuTween.onComplete = function()
        menu:destroy()
    end
end
```

### 🎭 **Exemplo 3: Sistema de Loading Completo**

```lua
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

## 🚀 Performance e Otimização

### 📊 **Métricas de Performance**

1. **Tempo de Criação de Tween**: < 0.1ms
2. **Tempo de Execução por Frame**: < 0.5ms
3. **Uso de Memória por Animação**: < 0.5KB
4. **Limite de Animações Simultâneas**: 50 por widget

### 🎯 **Técnicas de Otimização**

```lua
-- Object pooling para animações
local AnimationPool = {}

function AnimationPool.get()
    -- Função: AnimationPool
    if #AnimationPool > 0 then
    -- Verificação condicional
        return table.remove(AnimationPool)
    else
        return {}
    end
end

function AnimationPool.release(animation)
    -- Função: AnimationPool
    animation:reset()
    table.insert(AnimationPool, animation)
end

-- Lazy loading de animações
local function createAnimationOnDemand(widget, animationType)
    if not widget.animations then
    -- Verificação condicional
        widget.animations = {}
    end
    
    if not widget.animations[animationType] then
    -- Verificação condicional
        widget.animations[animationType] = createAnimation(animationType)
    end
    
    return widget.animations[animationType]
end

-- Controle de performance
    --  Controle de performance (traduzido)
local function shouldAnimate()
    return g_clock.millis() - lastAnimationTime > 16  -- 60 FPS
end
```

### 🔧 **Monitoramento de Performance**

```lua
-- Função para medir performance de animações
local function measureAnimationPerformance(animationCount)
    local startTime = g_clock.millis()
    
    local widgets = {}
    for i = 1, animationCount do
    -- Loop de repetição
        widgets[i] = g_ui.createWidget('UIWidget')
        local tween = widgets[i]:addAnchoredTween(easeInOut, 1000)
        tween:setPosition({x = math.random(100), y = math.random(100)})
    end
    
    local creationTime = g_clock.millis() - startTime
    
    -- Medir tempo de execução
    startTime = g_clock.millis()
    for _, widget in ipairs(widgets) do
    -- Loop de repetição
        widget:stopAllTweens()
    end
    local executionTime = g_clock.millis() - startTime
    
    -- Limpeza
    --  Limpeza (traduzido)
    for _, widget in ipairs(widgets) do
    -- Loop de repetição
        widget:destroy()
    end
    
    print(string.format('Criação: %dms, Execução: %dms', creationTime, executionTime))
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

---

## 📚 Referências

### 🔗 **Links Automáticos**

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

## 🔗 Links Relacionados
- [UIAdvancedWidgets](UIAdvancedWidgets.md) - Widgets Avançados
- [UI_System_Guide](UI_System_Guide.md) - Guia do sistema de UI
- [Animation_System_Guide](Animation_System_Guide.md) - Guia completo do sistema de animações
- [EffectsSystem](EffectsSystem.md) - Sistema de efeitos visuais

### 📖 Documentação Técnica
- **Sistema de Tweening**: Framework interno de animações
- **Funções de Easing**: Curvas de animação disponíveis
- **Performance**: Otimizações e métricas

---

**Última Atualização**: 2025-01-27  
**Versão**: 1.0  
**Status**: ✅ **Completo**  
**Prioridade**: 🔥 **MÁXIMA**
