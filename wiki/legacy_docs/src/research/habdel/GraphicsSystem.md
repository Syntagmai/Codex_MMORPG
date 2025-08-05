# Sistema de Gráficos - OTClient Redemption

Documentação completa do sistema de gráficos do OTClient, incluindo renderização, shaders, texturas, fontes e efeitos visuais.

## 📋 Índice

1. [Visão Geral](#-visão-geral)
2. [Sistema de Renderização](#-sistema-de-renderização)
3. [Sistema de Shaders](#-sistema-de-shaders)
4. [Gerenciamento de Texturas](#-gerenciamento-de-texturas)
5. [Sistema de Fontes](#-sistema-de-fontes)
6. [Efeitos Visuais](#-efeitos-visuais)
7. [Configurações Gráficas](#-configurações-gráficas)
8. [Performance e Otimização](#-performance-e-otimização)
9. [Screenshots e Gravação](#-screenshots-e-gravação)
10. [Exemplos Práticos](#-exemplos-práticos)

## 🎯 Visão Geral

O sistema de gráficos do OTClient é baseado em OpenGL e fornece renderização acelerada por hardware, suporte a shaders personalizados, gerenciamento de texturas e diversos efeitos visuais para melhorar a experiência do jogo.

### Arquitetura Gráfica

#### Nível Basic
```lua
-- Hierarquia do sistema gráfico
Graphics Engine (OpenGL)
├── Renderer (g_graphics)
├── Shaders (g_shaders)  
├── Textures (g_textures)
├── Fonts (g_fonts)
├── Effects (particles, animations)
└── Painters (drawing operations)
```

#### Nível Intermediate
```lua
-- Hierarquia do sistema gráfico
Graphics Engine (OpenGL)
├── Renderer (g_graphics)
├── Shaders (g_shaders)  
├── Textures (g_textures)
├── Fonts (g_fonts)
├── Effects (particles, animations)
└── Painters (drawing operations)
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
-- Hierarquia do sistema gráfico
Graphics Engine (OpenGL)
├── Renderer (g_graphics)
├── Shaders (g_shaders)  
├── Textures (g_textures)
├── Fonts (g_fonts)
├── Effects (particles, animations)
└── Painters (drawing operations)
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

### Informações do Sistema

#### Nível Basic
```lua
-- Obter informações da placa gráfica
local vendor = g_graphics.getVendor()       -- "NVIDIA Corporation"
local renderer = g_graphics.getRenderer()   -- "GeForce GTX 1060"
local version = g_graphics.getVersion()     -- "4.6.0 NVIDIA 461.92"
-- Verificar compatibilidade
local glslVersion = g_graphics.getGLSLVersion() -- Versão do GLSL
local extensions = g_graphics.getExtensions()   -- Extensões suportadas
print("GPU:", vendor, renderer)
print("OpenGL:", version)
print("GLSL:", glslVersion)
```

#### Nível Intermediate
```lua
-- Obter informações da placa gráfica
local vendor = g_graphics.getVendor()       -- "NVIDIA Corporation"
local renderer = g_graphics.getRenderer()   -- "GeForce GTX 1060"
local version = g_graphics.getVersion()     -- "4.6.0 NVIDIA 461.92"

-- Verificar compatibilidade
local glslVersion = g_graphics.getGLSLVersion() -- Versão do GLSL
local extensions = g_graphics.getExtensions()   -- Extensões suportadas

print("GPU:", vendor, renderer)
print("OpenGL:", version)
print("GLSL:", glslVersion)
```

#### Nível Advanced
```lua
-- Obter informações da placa gráfica
local vendor = g_graphics.getVendor()       -- "NVIDIA Corporation"
local renderer = g_graphics.getRenderer()   -- "GeForce GTX 1060"
local version = g_graphics.getVersion()     -- "4.6.0 NVIDIA 461.92"

-- Verificar compatibilidade
local glslVersion = g_graphics.getGLSLVersion() -- Versão do GLSL
local extensions = g_graphics.getExtensions()   -- Extensões suportadas

print("GPU:", vendor, renderer)
print("OpenGL:", version)
print("GLSL:", glslVersion)
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

## 🎨 Sistema de Renderização

### g_graphics - Interface Principal

#### Nível Basic
```lua
-- Informações da viewport
local viewportSize = g_graphics.getViewportSize() -- {width, height}
local width = viewportSize.width
local height = viewportSize.height
-- Redimensionamento
-- VSync
local vsyncEnabled = g_graphics.isVSyncEnabled() -- Verifica se VSync está ativo
-- FPS
local averageFPS = g_graphics.getAverageFPS() -- FPS médio
local maxFPS = g_graphics.getMaxFPS()     -- FPS máximo configurado
-- Screenshots
```

#### Nível Intermediate
```lua
-- Informações da viewport
local viewportSize = g_graphics.getViewportSize() -- {width, height}
local width = viewportSize.width
local height = viewportSize.height

-- Redimensionamento
g_graphics.resize(1920, 1080)            -- Redimensiona viewport

-- VSync
g_graphics.setVSync(true)                -- Ativa sincronização vertical
local vsyncEnabled = g_graphics.isVSyncEnabled() -- Verifica se VSync está ativo

-- FPS
local averageFPS = g_graphics.getAverageFPS() -- FPS médio
local maxFPS = g_graphics.getMaxFPS()     -- FPS máximo configurado
g_graphics.setMaxFPS(60)                 -- Define limite de FPS

-- Screenshots
g_graphics.screenshot("screenshot.png")   -- Captura tela
g_graphics.screenshotMap("map.png", {x=1000, y=1000, z=7}, 15) -- Screenshot do mapa
```

#### Nível Advanced
```lua
-- Informações da viewport
local viewportSize = g_graphics.getViewportSize() -- {width, height}
local width = viewportSize.width
local height = viewportSize.height

-- Redimensionamento
g_graphics.resize(1920, 1080)            -- Redimensiona viewport

-- VSync
g_graphics.setVSync(true)                -- Ativa sincronização vertical
local vsyncEnabled = g_graphics.isVSyncEnabled() -- Verifica se VSync está ativo

-- FPS
local averageFPS = g_graphics.getAverageFPS() -- FPS médio
local maxFPS = g_graphics.getMaxFPS()     -- FPS máximo configurado
g_graphics.setMaxFPS(60)                 -- Define limite de FPS

-- Screenshots
g_graphics.screenshot("screenshot.png")   -- Captura tela
g_graphics.screenshotMap("map.png", {x=1000, y=1000, z=7}, 15) -- Screenshot do mapa
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

### Configurações de Renderização

```lua
-- Anti-aliasing
    --  Anti-aliasing (traduzido)
g_graphics.setAntialiasingMode(mode)     -- 0=None, 1=AA, 2=Smooth Retro
local aaMode = g_graphics.getAntialiasingMode()

-- Qualidade de textura
    --  Qualidade de textura (traduzido)
g_graphics.setTextureFiltering(enabled)  -- Filtro de textura
local filtering = g_graphics.isTextureFilteringEnabled()

-- Floor view modes
    --  Floor view modes (traduzido)
g_graphics.setFloorViewMode(mode)        -- 0=Normal, 1=Fade, 2=Locked, etc.
local floorMode = g_graphics.getFloorViewMode()

-- Configurações de luz
g_graphics.setDrawLights(enabled)        -- Desenhar luzes
g_graphics.setDrawTexts(enabled)         -- Desenhar textos
g_graphics.setDrawHealthBars(enabled)    -- Desenhar barras de HP
```

### Painters - Sistema de Desenho

#### Nível Basic
```lua
-- Painter para desenho customizado
local painter = g_ui.createPainter()
-- Configurações do painter
-- Desenhar formas básicas
-- Exemplo de uso em widget
widget.onPaint = function(widget, painter, clip)
end
```

#### Nível Intermediate
```lua
-- Painter para desenho customizado
local painter = g_ui.createPainter()

-- Configurações do painter
painter:setColor('#FF0000')              -- Cor vermelha
painter:setOpacity(0.8)                  -- 80% de opacidade
painter:setCompositionMode(mode)         -- Modo de composição

-- Desenhar formas básicas
painter:drawBoundingRect(rect)           -- Retângulo
painter:drawFilledRect(rect)             -- Retângulo preenchido
painter:drawText(text, rect)             -- Texto
painter:drawTexturedRect(rect, texture)  -- Retângulo com textura

-- Exemplo de uso em widget
widget.onPaint = function(widget, painter, clip)
    painter:setColor('#00FF00')
    painter:drawFilledRect(widget:getRect())
    
    painter:setColor('#FFFFFF')
    painter:drawText("Custom Text", widget:getRect())
end
```

#### Nível Advanced
```lua
-- Painter para desenho customizado
local painter = g_ui.createPainter()

-- Configurações do painter
painter:setColor('#FF0000')              -- Cor vermelha
painter:setOpacity(0.8)                  -- 80% de opacidade
painter:setCompositionMode(mode)         -- Modo de composição

-- Desenhar formas básicas
painter:drawBoundingRect(rect)           -- Retângulo
painter:drawFilledRect(rect)             -- Retângulo preenchido
painter:drawText(text, rect)             -- Texto
painter:drawTexturedRect(rect, texture)  -- Retângulo com textura

-- Exemplo de uso em widget
widget.onPaint = function(widget, painter, clip)
    painter:setColor('#00FF00')
    painter:drawFilledRect(widget:getRect())
    
    painter:setColor('#FFFFFF')
    painter:drawText("Custom Text", widget:getRect())
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

## 🌟 Sistema de Shaders

### g_shaders - Interface de Shaders

```lua
-- Criar shader
    --  Criar shader (traduzido)
g_shaders.createShader(name, useFramebuffer)
g_shaders.createFragmentShader(name, fragmentPath, useFramebuffer)
g_shaders.createVertexShader(name, vertexPath)

-- Gerenciar shaders ativos
    --  Gerenciar shaders ativos (traduzido)
g_shaders.setShader(name)                -- Ativa shader
g_shaders.clearShader()                  -- Remove shader ativo
g_shaders.clear()                        -- Limpa todos os shaders

-- Uniforms
    --  Uniforms (traduzido)
g_shaders.setUniform(name, value)        -- Define uniform
g_shaders.setUniformFloat(name, value)   -- Float
g_shaders.setUniformInt(name, value)     -- Integer
g_shaders.setUniformVec2(name, x, y)     -- Vector2
g_shaders.setUniformVec3(name, x, y, z)  -- Vector3
g_shaders.setUniformVec4(name, x, y, z, w) -- Vector4

-- Texturas múltiplas
g_shaders.addMultiTexture(shaderName, texturePath)
g_shaders.bindTexture(texture, unit)     -- Bind texture na unidade

-- Framebuffers
    --  Framebuffers (traduzido)
g_shaders.useFramebuffer(name)           -- Usa framebuffer específico
```

### Shaders Predefinidos

#### Nível Basic
```lua
-- Shaders de mapa disponíveis
local MAP_SHADERS = {
    'Map - Default',        -- Sem shader
    'Map - Fog',           -- Névoa
    'Map - Rain',          -- Chuva
    'Map - Snow',          -- Neve
    'Map - Gray Scale',    -- Escala de cinza
    'Map - Bloom',         -- Efeito bloom
    'Map - Sepia',         -- Sepia
    'Map - Pulse',         -- Pulsação
    'Map - Old Tv',        -- TV antiga
    'Map - Party',         -- Cores vibrantes
    'Map - Radial Blur',   -- Desfoque radial
    'Map - Zomg',          -- Efeito especial
    'Map - Heat',          -- Efeito de calor
    'Map - Noise'          -- Ruído
}

-- Shaders de outfit
local OUTFIT_SHADERS = {
    'Outfit - Default',    -- Padrão
    'Outfit - Rainbow',    -- Arco-íris
    'Outfit - Ghost',      -- Fantasma
    'Outfit - Jelly',      -- Gelatina
    'Outfit - Fragmented', -- Fragmentado
    'Outfit - Outline'     -- Contorno
}

-- Aplicar shader ao mapa
local map = modules.game_interface.getMapPanel()
map:setShader('Map - Fog')

-- Aplicar shader ao jogador
local player = g_game.getLocalPlayer()
if player then
    player:setShader('Outfit - Rainbow')
    player:setMountShader('Mount - Rainbow')
end
```

#### Nível Intermediate
```lua
-- Shaders de mapa disponíveis
local MAP_SHADERS = {
    'Map - Default',        -- Sem shader
    'Map - Fog',           -- Névoa
    'Map - Rain',          -- Chuva
    'Map - Snow',          -- Neve
    'Map - Gray Scale',    -- Escala de cinza
    'Map - Bloom',         -- Efeito bloom
    'Map - Sepia',         -- Sepia
    'Map - Pulse',         -- Pulsação
    'Map - Old Tv',        -- TV antiga
    'Map - Party',         -- Cores vibrantes
    'Map - Radial Blur',   -- Desfoque radial
    'Map - Zomg',          -- Efeito especial
    'Map - Heat',          -- Efeito de calor
    'Map - Noise'          -- Ruído
}

-- Shaders de outfit
local OUTFIT_SHADERS = {
    'Outfit - Default',    -- Padrão
    'Outfit - Rainbow',    -- Arco-íris
    'Outfit - Ghost',      -- Fantasma
    'Outfit - Jelly',      -- Gelatina
    'Outfit - Fragmented', -- Fragmentado
    'Outfit - Outline'     -- Contorno
}

-- Aplicar shader ao mapa
local map = modules.game_interface.getMapPanel()
map:setShader('Map - Fog')

-- Aplicar shader ao jogador
local player = g_game.getLocalPlayer()
if player then
    player:setShader('Outfit - Rainbow')
    player:setMountShader('Mount - Rainbow')
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
-- Shaders de mapa disponíveis
local MAP_SHADERS = {
    'Map - Default',        -- Sem shader
    'Map - Fog',           -- Névoa
    'Map - Rain',          -- Chuva
    'Map - Snow',          -- Neve
    'Map - Gray Scale',    -- Escala de cinza
    'Map - Bloom',         -- Efeito bloom
    'Map - Sepia',         -- Sepia
    'Map - Pulse',         -- Pulsação
    'Map - Old Tv',        -- TV antiga
    'Map - Party',         -- Cores vibrantes
    'Map - Radial Blur',   -- Desfoque radial
    'Map - Zomg',          -- Efeito especial
    'Map - Heat',          -- Efeito de calor
    'Map - Noise'          -- Ruído
}

-- Shaders de outfit
local OUTFIT_SHADERS = {
    'Outfit - Default',    -- Padrão
    'Outfit - Rainbow',    -- Arco-íris
    'Outfit - Ghost',      -- Fantasma
    'Outfit - Jelly',      -- Gelatina
    'Outfit - Fragmented', -- Fragmentado
    'Outfit - Outline'     -- Contorno
}

-- Aplicar shader ao mapa
local map = modules.game_interface.getMapPanel()
map:setShader('Map - Fog')

-- Aplicar shader ao jogador
local player = g_game.getLocalPlayer()
if player then
    player:setShader('Outfit - Rainbow')
    player:setMountShader('Mount - Rainbow')
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

### Criação de Shaders Customizados

#### Inicialização e Configuração
```lua
-- Criar shader customizado
function createCustomShader()
    local fragmentShader = [
        uniform float u_Time;
        uniform vec2 u_Resolution;
        
        void main() {
            vec2 uv = gl_FragCoord.xy / u_Resolution.xy;
            vec3 color = vec3(0.5 + 0.5 * cos(u_Time + uv.xyx + vec3(0, 2, 4)));
            gl_FragColor = vec4(color, 1.0);
        }
    ](
        uniform float u_Time;
        uniform vec2 u_Resolution;
        
        void main() {
            vec2 uv = gl_FragCoord.xy / u_Resolution.xy;
            vec3 color = vec3(0.5 + 0.5 * cos(u_Time + uv.xyx + vec3(0, 2, 4)));
            gl_FragColor = vec4(color, 1.0);
        }
    .md)
    
    -- Salvar shader em arquivo
    local shaderPath = g_resources.getWorkDir() .. 'shaders/fragment/custom.frag'
    g_resources.writeFileContents(shaderPath, fragmentShader)
    
    -- Registrar shader
    g_shaders.createFragmentShader('Custom Shader', 'shaders/fragment/custom.frag', false)
    
    -- Aplicar shader
    local map = modules.game_interface.getMapPanel()
    map:setShader('Custom Shader')
    
    -- Atualizar uniforms
    scheduleEvent(function()
        g_shaders.setUniformFloat('u_Time', g_clock.seconds())
        g_shaders.setUniformVec2('u_Resolution', g_graphics.getViewportSize().width, g_graphics.getViewportSize().height)
    end, 50)
```

#### Finalização
```lua
end

-- Shader animado com timer
function startAnimatedShader()
    local updateEvent
    
    local function updateShader()
        g_shaders.setUniformFloat('u_Time', g_clock.seconds())
        updateEvent = scheduleEvent(updateShader, 16) -- ~60 FPS
    end
    
    updateEvent = scheduleEvent(updateShader, 16)
    return updateEvent
end
```

## 🖼️ Gerenciamento de Texturas

### g_textures - Interface de Texturas

#### Nível Basic
```lua
-- Carregar textura
local texture = g_textures.getTexture(path) -- Carrega/obtém textura
-- Informações da textura
local size = texture:getSize()           -- {width, height}
local width = texture:getWidth()         -- Largura
local height = texture:getHeight()       -- Altura
local glId = texture:getId()             -- ID OpenGL
-- Estados da textura
local loaded = texture:isLoaded()        -- Está carregada
local smooth = texture:isSmooth()        -- Suavização ativa
-- Bind de textura
-- Criar textura em branco
local blankTexture = g_textures.createTexture(width, height)
```

#### Nível Intermediate
```lua
-- Carregar textura
local texture = g_textures.getTexture(path) -- Carrega/obtém textura
g_textures.preload(directory)            -- Pré-carrega diretório

-- Informações da textura
local size = texture:getSize()           -- {width, height}
local width = texture:getWidth()         -- Largura
local height = texture:getHeight()       -- Altura
local glId = texture:getId()             -- ID OpenGL

-- Estados da textura
local loaded = texture:isLoaded()        -- Está carregada
local smooth = texture:isSmooth()        -- Suavização ativa
texture:setSmooth(true)                  -- Ativa suavização

-- Bind de textura
texture:bind()                           -- Bind para uso

-- Criar textura em branco
local blankTexture = g_textures.createTexture(width, height)
```

#### Nível Advanced
```lua
-- Carregar textura
local texture = g_textures.getTexture(path) -- Carrega/obtém textura
g_textures.preload(directory)            -- Pré-carrega diretório

-- Informações da textura
local size = texture:getSize()           -- {width, height}
local width = texture:getWidth()         -- Largura
local height = texture:getHeight()       -- Altura
local glId = texture:getId()             -- ID OpenGL

-- Estados da textura
local loaded = texture:isLoaded()        -- Está carregada
local smooth = texture:isSmooth()        -- Suavização ativa
texture:setSmooth(true)                  -- Ativa suavização

-- Bind de textura
texture:bind()                           -- Bind para uso

-- Criar textura em branco
local blankTexture = g_textures.createTexture(width, height)
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

### Cache de Texturas

#### Nível Basic
```lua
-- Gerenciamento de cache
function preloadGameTextures()
    -- Pré-carregar texturas principais
    g_textures.preload('/images/game/')
    g_textures.preload('/images/ui/')
    g_textures.preload('/images/icons/')
    
    print("Texturas pré-carregadas")
end

-- Verificar uso de memória
function getTextureMemoryUsage()
    local totalMemory = 0
    local textureCount = 0
    
    -- Esta seria uma função hipotética para obter estatísticas
    -- local stats = g_textures.getMemoryStats()
    -- return stats.totalMemory, stats.textureCount
    
    return totalMemory, textureCount
end

-- Limpar cache de texturas não utilizadas
function cleanTextureCache()
    -- g_textures.cleanUnused() -- Função hipotética
    collectgarbage()
end
```

#### Nível Intermediate
```lua
-- Gerenciamento de cache
function preloadGameTextures()
    -- Pré-carregar texturas principais
    g_textures.preload('/images/game/')
    g_textures.preload('/images/ui/')
    g_textures.preload('/images/icons/')
    
    print("Texturas pré-carregadas")
end

-- Verificar uso de memória
function getTextureMemoryUsage()
    local totalMemory = 0
    local textureCount = 0
    
    -- Esta seria uma função hipotética para obter estatísticas
    -- local stats = g_textures.getMemoryStats()
    -- return stats.totalMemory, stats.textureCount
    
    return totalMemory, textureCount
end

-- Limpar cache de texturas não utilizadas
function cleanTextureCache()
    -- g_textures.cleanUnused() -- Função hipotética
    collectgarbage()
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
-- Gerenciamento de cache
function preloadGameTextures()
    -- Pré-carregar texturas principais
    g_textures.preload('/images/game/')
    g_textures.preload('/images/ui/')
    g_textures.preload('/images/icons/')
    
    print("Texturas pré-carregadas")
end

-- Verificar uso de memória
function getTextureMemoryUsage()
    local totalMemory = 0
    local textureCount = 0
    
    -- Esta seria uma função hipotética para obter estatísticas
    -- local stats = g_textures.getMemoryStats()
    -- return stats.totalMemory, stats.textureCount
    
    return totalMemory, textureCount
end

-- Limpar cache de texturas não utilizadas
function cleanTextureCache()
    -- g_textures.cleanUnused() -- Função hipotética
    collectgarbage()
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

## 🔤 Sistema de Fontes

### g_fonts - Interface de Fontes

```lua
-- Carregar fonte
    --  Carregar fonte (traduzido)
local font = g_fonts.getFont(name)       -- "verdana-11px-rounded"
g_fonts.importFont(path)                 -- Importa fonte customizada

-- Informações da fonte
local glyphHeight = font:getGlyphHeight() -- Altura dos glyphs
local glyphSpacing = font:getGlyphSpacing() -- Espaçamento
local textureSize = font:getTextureSize() -- Tamanho da textura

-- Calcular tamanho do texto
    --  Calcular tamanho do texto (traduzido)
local textSize = font:calculateTextRectSize(text, maxWidth)
local width = textSize.width
local height = textSize.height

-- Renderizar texto
    --  Renderizar texto (traduzido)
font:renderText(text, position, color)   -- Renderiza texto
```

### Fontes Disponíveis

```lua
-- Fontes padrão do OTClient
local AVAILABLE_FONTS = {
    'verdana-11px-rounded',
    'verdana-11px-monochrome', 
    'verdana-11px-antialised',
    'terminus-14px-bold',
    'helvetica-12px-bold',
    'sans-bold-16px'
}

-- Usar fonte específica
function setWidgetFont(widget, fontName)
    -- Função: setWidgetFont
    widget:setFont(fontName)
end

-- Exemplo de uso
    --  Exemplo de uso (traduzido)
local label = g_ui.createWidget('UILabel', parent)
label:setText("Texto com fonte customizada")
label:setFont('terminus-14px-bold')
```

### Criação de Fontes Customizadas

```lua
-- Carregar fonte customizada
    --  Carregar fonte customizada (traduzido)
function loadCustomFont()
    -- Função: loadCustomFont
    local fontPath = g_resources.getWorkDir() .. 'fonts/custom.otfont'
    
    if g_resources.fileExists(fontPath) then
    -- Verificação condicional
        g_fonts.importFont(fontPath)
        print("Fonte customizada carregada")
    else
        print("Arquivo de fonte não encontrado")
    end
end

-- Gerar fonte bitmap
    --  Gerar fonte bitmap (traduzido)
function generateBitmapFont(ttfPath, size, outputPath)
    -- Função: generateBitmapFont
    -- Esta seria uma função para gerar fonte bitmap
    -- a partir de fonte TrueType (implementação específica)
    local success = g_fonts.generateBitmapFont(ttfPath, size, outputPath)
    return success
end
```

## ✨ Efeitos Visuais

### Particles e Animações

#### Nível Basic
```lua
-- Sistema de partículas (se disponível)
function createParticleEffect(position, type)
    local effect = g_effects.createEffect(type, position)
    effect:setDuration(2000)             -- 2 segundos
    effect:setIntensity(1.0)             -- Intensidade máxima
    effect:start()
    
    return effect
end

-- Animações de interface
function animateWidget(widget, property, targetValue, duration)
    local startValue = widget[property]
    local startTime = g_clock.millis()
    local updateEvent
    
    local function updateAnimation()
        local elapsed = g_clock.millis() - startTime
        local progress = math.min(elapsed / duration, 1.0)
        
        -- Interpolação linear
        local currentValue = startValue + (targetValue - startValue) * progress
        widget[property] = currentValue
        
        if progress < 1.0 then
            updateEvent = scheduleEvent(updateAnimation, 16)
        end
    end
    
    updateEvent = scheduleEvent(updateAnimation, 16)
    return updateEvent
end

-- Efeitos de fade
function fadeIn(widget, duration)
    widget:setOpacity(0)
    widget:setVisible(true)
    animateWidget(widget, 'opacity', 1.0, duration or 250)
end

function fadeOut(widget, duration, callback)
    animateWidget(widget, 'opacity', 0.0, duration or 250)
    scheduleEvent(function()
        widget:setVisible(false)
        if callback then callback() end
    end, duration or 250)
end
```

#### Nível Intermediate
```lua
-- Sistema de partículas (se disponível)
function createParticleEffect(position, type)
    local effect = g_effects.createEffect(type, position)
    effect:setDuration(2000)             -- 2 segundos
    effect:setIntensity(1.0)             -- Intensidade máxima
    effect:start()
    
    return effect
end

-- Animações de interface
function animateWidget(widget, property, targetValue, duration)
    local startValue = widget[property]
    local startTime = g_clock.millis()
    local updateEvent
    
    local function updateAnimation()
        local elapsed = g_clock.millis() - startTime
        local progress = math.min(elapsed / duration, 1.0)
        
        -- Interpolação linear
        local currentValue = startValue + (targetValue - startValue) * progress
        widget[property] = currentValue
        
        if progress < 1.0 then
            updateEvent = scheduleEvent(updateAnimation, 16)
        end
    end
    
    updateEvent = scheduleEvent(updateAnimation, 16)
    return updateEvent
end

-- Efeitos de fade
function fadeIn(widget, duration)
    widget:setOpacity(0)
    widget:setVisible(true)
    animateWidget(widget, 'opacity', 1.0, duration or 250)
end

function fadeOut(widget, duration, callback)
    animateWidget(widget, 'opacity', 0.0, duration or 250)
    scheduleEvent(function()
        widget:setVisible(false)
        if callback then callback() end
    end, duration or 250)
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
-- Sistema de partículas (se disponível)
function createParticleEffect(position, type)
    local effect = g_effects.createEffect(type, position)
    effect:setDuration(2000)             -- 2 segundos
    effect:setIntensity(1.0)             -- Intensidade máxima
    effect:start()
    
    return effect
end

-- Animações de interface
function animateWidget(widget, property, targetValue, duration)
    local startValue = widget[property]
    local startTime = g_clock.millis()
    local updateEvent
    
    local function updateAnimation()
        local elapsed = g_clock.millis() - startTime
        local progress = math.min(elapsed / duration, 1.0)
        
        -- Interpolação linear
        local currentValue = startValue + (targetValue - startValue) * progress
        widget[property] = currentValue
        
        if progress < 1.0 then
            updateEvent = scheduleEvent(updateAnimation, 16)
        end
    end
    
    updateEvent = scheduleEvent(updateAnimation, 16)
    return updateEvent
end

-- Efeitos de fade
function fadeIn(widget, duration)
    widget:setOpacity(0)
    widget:setVisible(true)
    animateWidget(widget, 'opacity', 1.0, duration or 250)
end

function fadeOut(widget, duration, callback)
    animateWidget(widget, 'opacity', 0.0, duration or 250)
    scheduleEvent(function()
        widget:setVisible(false)
        if callback then callback() end
    end, duration or 250)
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

### Efeitos de Luz

```lua
-- Sistema de luz
    --  Sistema de luz (traduzido)
function setAmbientLight(intensity)
    -- Função: setAmbientLight
    g_graphics.setAmbientLight(intensity) -- 0.0 a 1.0
end

function addDynamicLight(creature, color, intensity)
    -- Função: addDynamicLight
    local light = {
        color = color,         -- {r, g, b}
        intensity = intensity, -- 0-255
        radius = 6            -- Raio da luz
    }
    
    creature:setLight(light)
end

-- Exemplos de luz
    --  Exemplos de luz (traduzido)
function applyTorchLight(creature)
    -- Função: applyTorchLight
    addDynamicLight(creature, {255, 180, 100}, 200) -- Luz alaranjada
end

function applyMagicLight(creature)
    -- Função: applyMagicLight
    addDynamicLight(creature, {100, 100, 255}, 150) -- Luz azul mágica
end
```

## ⚙️ Configurações Gráficas

### Opções de Renderização

```lua
-- Configurações principais
g_graphics.setDrawLights(enabled)        -- Renderizar luzes
g_graphics.setDrawTexts(enabled)         -- Renderizar textos
g_graphics.setDrawHealthBars(enabled)    -- Barras de HP
g_graphics.setDrawNames(enabled)         -- Nomes das criaturas

-- Qualidade visual
    --  Qualidade visual (traduzido)
g_graphics.setAntialiasingMode(mode)     -- Anti-aliasing
g_graphics.setTextureFiltering(enabled)  -- Filtro de textura
g_graphics.setFloorViewMode(mode)        -- Modo de visualização de andares

-- Floor fade out
    --  Floor fade out (traduzido)
g_graphics.setFloorFading(enabled)       -- Fade de andares
g_graphics.setFloorShadowing(enabled)    -- Sombras de andares

-- Performance
    --  Performance (traduzido)
g_graphics.setOptimizeMana(enabled)      -- Otimizar mana
g_graphics.setOptimizeHP(enabled)        -- Otimizar HP
```

### Sistema de Configurações

#### Inicialização e Configuração
```lua
-- Carregar configurações gráficas
function loadGraphicsSettings()
    local settings = g_settings.getNode('graphics') or {}
    
    -- Aplicar configurações
    g_graphics.setVSync(settings.vsync or false)
    g_graphics.setMaxFPS(settings.maxFPS or 60)
    g_graphics.setAntialiasingMode(settings.antialiasing or 0)
    g_graphics.setTextureFiltering(settings.textureFiltering or true)
    g_graphics.setFloorViewMode(settings.floorViewMode or 0)
    
    -- Configurações de desenho
    g_graphics.setDrawLights(settings.drawLights or true)
    g_graphics.setDrawTexts(settings.drawTexts or true)
    g_graphics.setDrawHealthBars(settings.drawHealthBars or true)
    g_graphics.setDrawNames(settings.drawNames or true)
end

-- Salvar configurações
function saveGraphicsSettings()
    local settings = {
        vsync = g_graphics.isVSyncEnabled(),
        maxFPS = g_graphics.getMaxFPS(),
        antialiasing = g_graphics.getAntialiasingMode(),
        textureFiltering = g_graphics.isTextureFilteringEnabled(),
        floorViewMode = g_graphics.getFloorViewMode(),
        drawLights = g_graphics.isDrawingLights(),
        drawTexts = g_graphics.isDrawingTexts(),
        drawHealthBars = g_graphics.isDrawingHealthBars(),
        drawNames = g_graphics.isDrawingNames()
    }
```

#### Funcionalidade 1
```lua
    
    g_settings.setNode('graphics', settings)
    g_settings.save()
end

-- Detectar configurações automáticas
function autoDetectGraphicsSettings()
    local vendor = g_graphics.getVendor():lower()
    local renderer = g_graphics.getRenderer():lower()
    
    -- Configurações baseadas na GPU
    if vendor:find('nvidia') then
        -- Configurações para NVIDIA
        g_graphics.setAntialiasingMode(1)
        g_graphics.setTextureFiltering(true)
        g_graphics.setMaxFPS(0) -- Sem limite
    elseif vendor:find('amd') or vendor:find('ati') then
        -- Configurações para AMD
        g_graphics.setAntialiasingMode(1)
        g_graphics.setTextureFiltering(true)
        g_graphics.setMaxFPS(60)
    elseif vendor:find('intel') then
        -- Configurações para Intel (mais conservadoras)
        g_graphics.setAntialiasingMode(0)
        g_graphics.setTextureFiltering(false)
        g_graphics.setMaxFPS(60)
    else
        -- Configurações padrão para GPUs desconhecidas
        g_graphics.setAntialiasingMode(0)
        g_graphics.setTextureFiltering(true)
        g_graphics.setMaxFPS(60)
    end
```

#### Finalização
```lua
    
    print("Configurações gráficas auto-detectadas para:", vendor, renderer)
end
```

## 🚀 Performance e Otimização

### Monitoramento de Performance

#### Inicialização e Configuração
```lua
-- Monitor de FPS
function createFPSMonitor()
    local window = g_ui.createWidget('UIWindow', rootWidget)
    window:setTitle('FPS Monitor')
    window:setSize({width = 200, height = 100})
    
    local fpsLabel = g_ui.createWidget('UILabel', window)
    fpsLabel:setText('FPS: 0')
    fpsLabel:addAnchor(AnchorTop, 'parent', AnchorTop)
    fpsLabel:addAnchor(AnchorLeft, 'parent', AnchorLeft)
    fpsLabel:setMargin(10)
    
    local avgFpsLabel = g_ui.createWidget('UILabel', window)
    avgFpsLabel:setText('Avg: 0')
    avgFpsLabel:addAnchor(AnchorTop, fpsLabel, AnchorBottom)
    avgFpsLabel:addAnchor(AnchorLeft, 'parent', AnchorLeft)
    avgFpsLabel:setMargin(10)
    
    local updateEvent
    local function updateFPS()
        local currentFPS = g_graphics.getCurrentFPS() or 0
        local averageFPS = g_graphics.getAverageFPS()
        
        fpsLabel:setText(string.format('FPS: %d', currentFPS))
        avgFpsLabel:setText(string.format('Avg: %.1f', averageFPS))
        
        updateEvent = scheduleEvent(updateFPS, 100)
    end
```

#### Funcionalidade 1
```lua
    
    updateEvent = scheduleEvent(updateFPS, 100)
    return window, updateEvent
end

-- Benchmark de performance
function runGraphicsBenchmark()
    local startTime = g_clock.millis()
    local frameCount = 0
    local minFPS = math.huge
    local maxFPS = 0
    
    local updateEvent
    local function benchmarkFrame()
        frameCount = frameCount + 1
        local currentFPS = g_graphics.getCurrentFPS() or 0
        
        minFPS = math.min(minFPS, currentFPS)
        maxFPS = math.max(maxFPS, currentFPS)
        
        if g_clock.millis() - startTime < 10000 then -- 10 segundos
            updateEvent = scheduleEvent(benchmarkFrame, 16)
        else
            local elapsed = g_clock.millis() - startTime
            local avgFPS = frameCount / (elapsed / 1000)
            
            print("Benchmark Results:")
            print("Duration:", elapsed / 1000, "seconds")
            print("Frames:", frameCount)
            print("Average FPS:", avgFPS)
            print("Min FPS:", minFPS)
            print("Max FPS:", maxFPS)
        end
```

#### Finalização
```lua
    end
    
    updateEvent = scheduleEvent(benchmarkFrame, 16)
end
```

### Otimizações

#### Nível Basic
```lua
-- Configurações de performance
function applyPerformanceOptimizations()
    -- Reduzir qualidade visual para melhor performance
    -- Reduzir efeitos visuais
    -- Otimizações específicas
    print("Otimizações de performance aplicadas")
end
-- Configurações de qualidade
function applyQualitySettings()
    -- Máxima qualidade visual
    -- Ativar todos os efeitos
    print("Configurações de qualidade aplicadas")
end
-- Limpeza de recursos gráficos
function cleanGraphicsResources()
    -- Limpar cache de texturas
    -- Limpar shaders não utilizados
    -- Forçar garbage collection
    print("Recursos gráficos limpos")
end
```

#### Nível Intermediate
```lua
-- Configurações de performance
function applyPerformanceOptimizations()
    -- Reduzir qualidade visual para melhor performance
    g_graphics.setAntialiasingMode(0)     -- Desativar anti-aliasing
    g_graphics.setTextureFiltering(false) -- Desativar filtro de textura
    g_graphics.setMaxFPS(60)              -- Limitar FPS
    
    -- Reduzir efeitos visuais
    g_graphics.setDrawLights(false)       -- Desativar luzes
    g_graphics.setFloorFading(false)      -- Desativar fade de andares
    
    -- Otimizações específicas
    setOption('optimizeHP', true)         -- Otimizar barras de HP
    setOption('optimizeMana', true)       -- Otimizar barras de mana
    
    print("Otimizações de performance aplicadas")
end

-- Configurações de qualidade
function applyQualitySettings()
    -- Máxima qualidade visual
    g_graphics.setAntialiasingMode(2)     -- Smooth Retro
    g_graphics.setTextureFiltering(true)  -- Ativar filtro de textura
    g_graphics.setMaxFPS(0)               -- FPS ilimitado
    
    -- Ativar todos os efeitos
    g_graphics.setDrawLights(true)        -- Ativar luzes
    g_graphics.setFloorFading(true)       -- Ativar fade de andares
    g_graphics.setFloorShadowing(true)    -- Ativar sombras
    
    print("Configurações de qualidade aplicadas")
end

-- Limpeza de recursos gráficos
function cleanGraphicsResources()
    -- Limpar cache de texturas
    g_textures.cleanCache()
    
    -- Limpar shaders não utilizados
    g_shaders.cleanUnused()
    
    -- Forçar garbage collection
    collectgarbage('collect')
    
    print("Recursos gráficos limpos")
end
```

#### Nível Advanced
```lua
-- Configurações de performance
function applyPerformanceOptimizations()
    -- Reduzir qualidade visual para melhor performance
    g_graphics.setAntialiasingMode(0)     -- Desativar anti-aliasing
    g_graphics.setTextureFiltering(false) -- Desativar filtro de textura
    g_graphics.setMaxFPS(60)              -- Limitar FPS
    
    -- Reduzir efeitos visuais
    g_graphics.setDrawLights(false)       -- Desativar luzes
    g_graphics.setFloorFading(false)      -- Desativar fade de andares
    
    -- Otimizações específicas
    setOption('optimizeHP', true)         -- Otimizar barras de HP
    setOption('optimizeMana', true)       -- Otimizar barras de mana
    
    print("Otimizações de performance aplicadas")
end

-- Configurações de qualidade
function applyQualitySettings()
    -- Máxima qualidade visual
    g_graphics.setAntialiasingMode(2)     -- Smooth Retro
    g_graphics.setTextureFiltering(true)  -- Ativar filtro de textura
    g_graphics.setMaxFPS(0)               -- FPS ilimitado
    
    -- Ativar todos os efeitos
    g_graphics.setDrawLights(true)        -- Ativar luzes
    g_graphics.setFloorFading(true)       -- Ativar fade de andares
    g_graphics.setFloorShadowing(true)    -- Ativar sombras
    
    print("Configurações de qualidade aplicadas")
end

-- Limpeza de recursos gráficos
function cleanGraphicsResources()
    -- Limpar cache de texturas
    g_textures.cleanCache()
    
    -- Limpar shaders não utilizados
    g_shaders.cleanUnused()
    
    -- Forçar garbage collection
    collectgarbage('collect')
    
    print("Recursos gráficos limpos")
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

## 📸 Screenshots e Gravação

### Sistema de Screenshots

#### Nível Basic
```lua
-- Screenshot básico
function takeScreenshot(filename)
    print("Screenshot salvo:", filename)
end
-- Screenshot do mapa específico
function takeMapScreenshot(position, range, filename)
    print("Screenshot do mapa salvo:", filename)
end
-- Screenshot de widget específico
function takeWidgetScreenshot(widget, filename)
    -- Criar framebuffer para o widget
    local rect = widget:getRect()
    local texture = g_textures.createTexture(rect.width, rect.height)
    -- Renderizar widget para textura
    widget:render(texture)
    -- Salvar textura como imagem
    print("Screenshot do widget salvo:", filename)
end
-- Screenshot automático
function startAutoScreenshot(interval)
    local updateEvent
    local function autoScreenshot()
    end
end
```

#### Nível Intermediate
```lua
-- Screenshot básico
function takeScreenshot(filename)
    filename = filename or string.format("screenshot_%s.png", os.date("%Y%m%d_%H%M%S"))
    g_graphics.screenshot(filename)
    print("Screenshot salvo:", filename)
end

-- Screenshot do mapa específico
function takeMapScreenshot(position, range, filename)
    filename = filename or string.format("map_%d_%d_%d.png", position.x, position.y, position.z)
    g_graphics.screenshotMap(filename, position, range)
    print("Screenshot do mapa salvo:", filename)
end

-- Screenshot de widget específico
function takeWidgetScreenshot(widget, filename)
    filename = filename or "widget_screenshot.png"
    
    -- Criar framebuffer para o widget
    local rect = widget:getRect()
    local texture = g_textures.createTexture(rect.width, rect.height)
    
    -- Renderizar widget para textura
    widget:render(texture)
    
    -- Salvar textura como imagem
    texture:saveToFile(filename)
    
    print("Screenshot do widget salvo:", filename)
end

-- Screenshot automático
function startAutoScreenshot(interval)
    interval = interval or 60000 -- 1 minuto
    
    local updateEvent
    local function autoScreenshot()
        takeScreenshot()
        updateEvent = scheduleEvent(autoScreenshot, interval)
    end
    
    updateEvent = scheduleEvent(autoScreenshot, interval)
    return updateEvent
end
```

#### Nível Advanced
```lua
-- Screenshot básico
function takeScreenshot(filename)
    filename = filename or string.format("screenshot_%s.png", os.date("%Y%m%d_%H%M%S"))
    g_graphics.screenshot(filename)
    print("Screenshot salvo:", filename)
end

-- Screenshot do mapa específico
function takeMapScreenshot(position, range, filename)
    filename = filename or string.format("map_%d_%d_%d.png", position.x, position.y, position.z)
    g_graphics.screenshotMap(filename, position, range)
    print("Screenshot do mapa salvo:", filename)
end

-- Screenshot de widget específico
function takeWidgetScreenshot(widget, filename)
    filename = filename or "widget_screenshot.png"
    
    -- Criar framebuffer para o widget
    local rect = widget:getRect()
    local texture = g_textures.createTexture(rect.width, rect.height)
    
    -- Renderizar widget para textura
    widget:render(texture)
    
    -- Salvar textura como imagem
    texture:saveToFile(filename)
    
    print("Screenshot do widget salvo:", filename)
end

-- Screenshot automático
function startAutoScreenshot(interval)
    interval = interval or 60000 -- 1 minuto
    
    local updateEvent
    local function autoScreenshot()
        takeScreenshot()
        updateEvent = scheduleEvent(autoScreenshot, interval)
    end
    
    updateEvent = scheduleEvent(autoScreenshot, interval)
    return updateEvent
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

## 💡 Exemplos Práticos

### Exemplo 1: Sistema de Configurações Gráficas

#### Inicialização e Configuração
```lua
-- modules/graphics_settings/graphics_settings.lua
graphicsSettings = {}

function graphicsSettings.init()
    graphicsSettings.window = g_ui.displayUI('graphics_settings')
    graphicsSettings.setupInterface()
    graphicsSettings.loadSettings()
end

function graphicsSettings.setupInterface()
    -- Sliders
    graphicsSettings.fpsSlider = graphicsSettings.window:getChildById('fpsSlider')
    graphicsSettings.qualitySlider = graphicsSettings.window:getChildById('qualitySlider')
    
    -- Checkboxes
    graphicsSettings.vsyncBox = graphicsSettings.window:getChildById('vsyncBox')
    graphicsSettings.lightsBox = graphicsSettings.window:getChildById('lightsBox')
    graphicsSettings.texturesBox = graphicsSettings.window:getChildById('texturesBox')
    
    -- Combos
    graphicsSettings.aaCombo = graphicsSettings.window:getChildById('aaCombo')
    graphicsSettings.floorCombo = graphicsSettings.window:getChildById('floorCombo')
    
    -- Botões
    graphicsSettings.autoButton = graphicsSettings.window:getChildById('autoButton')
    graphicsSettings.applyButton = graphicsSettings.window:getChildById('applyButton')
    graphicsSettings.resetButton = graphicsSettings.window:getChildById('resetButton')
    
    -- Configurar combos
    graphicsSettings.aaCombo:addOption('Desabilitado', 0)
    graphicsSettings.aaCombo:addOption('Anti-aliasing', 1)
    graphicsSettings.aaCombo:addOption('Smooth Retro', 2)
    
    graphicsSettings.floorCombo:addOption('Normal', 0)
    graphicsSettings.floorCombo:addOption('Fade', 1)
    graphicsSettings.floorCombo:addOption('Locked', 2)
    graphicsSettings.floorCombo:addOption('Always', 3)
    
    -- Eventos
    graphicsSettings.fpsSlider.onValueChange = graphicsSettings.onFPSChange
    graphicsSettings.vsyncBox.onCheckChange = graphicsSettings.onVSyncChange
    graphicsSettings.lightsBox.onCheckChange = graphicsSettings.onLightsChange
    graphicsSettings.aaCombo.onOptionChange = graphicsSettings.onAAChange
    
    graphicsSettings.autoButton.onClick = graphicsSettings.autoDetect
    graphicsSettings.applyButton.onClick = graphicsSettings.applySettings
    graphicsSettings.resetButton.onClick = graphicsSettings.resetSettings
end
```

#### Funcionalidade 1
```lua

function graphicsSettings.onFPSChange(slider, value)
    local fps = value == 0 and 0 or (30 + value * 2) -- 0 = unlimited, 30-120
    g_graphics.setMaxFPS(fps)
    
    local label = graphicsSettings.window:getChildById('fpsLabel')
    label:setText(fps == 0 and 'Unlimited' or fps .. ' FPS')
end

function graphicsSettings.onVSyncChange(checkbox, checked)
    g_graphics.setVSync(checked)
end

function graphicsSettings.onLightsChange(checkbox, checked)
    g_graphics.setDrawLights(checked)
end

function graphicsSettings.onAAChange(combo, option)
    g_graphics.setAntialiasingMode(option.data)
end

function graphicsSettings.autoDetect()
```

#### Funcionalidade 2
```lua
    local vendor = g_graphics.getVendor():lower()
    
    if vendor:find('nvidia') then
        graphicsSettings.applyProfile('high')
    elseif vendor:find('amd') then
        graphicsSettings.applyProfile('medium')
    else
        graphicsSettings.applyProfile('low')
    end
    
    graphicsSettings.updateInterface()
    modules.game_textmessage.displayGameMessage('Configurações auto-detectadas')
end

function graphicsSettings.applyProfile(profile)
    if profile == 'high' then
        g_graphics.setMaxFPS(0)
        g_graphics.setVSync(true)
        g_graphics.setAntialiasingMode(2)
        g_graphics.setTextureFiltering(true)
        g_graphics.setDrawLights(true)
        g_graphics.setFloorViewMode(1)
    elseif profile == 'medium' then
        g_graphics.setMaxFPS(60)
        g_graphics.setVSync(false)
        g_graphics.setAntialiasingMode(1)
        g_graphics.setTextureFiltering(true)
        g_graphics.setDrawLights(true)
        g_graphics.setFloorViewMode(0)
    else -- low
        g_graphics.setMaxFPS(60)
        g_graphics.setVSync(false)
        g_graphics.setAntialiasingMode(0)
        g_graphics.setTextureFiltering(false)
        g_graphics.setDrawLights(false)
        g_graphics.setFloorViewMode(0)
    end
```

#### Funcionalidade 3
```lua
end

function graphicsSettings.loadSettings()
    local settings = g_settings.getNode('graphics') or {}
    
    -- Aplicar configurações salvas
    g_graphics.setMaxFPS(settings.maxFPS or 60)
    g_graphics.setVSync(settings.vsync or false)
    g_graphics.setAntialiasingMode(settings.antialiasing or 0)
    g_graphics.setTextureFiltering(settings.textureFiltering or true)
    g_graphics.setDrawLights(settings.drawLights or true)
    
    graphicsSettings.updateInterface()
end

function graphicsSettings.saveSettings()
    local settings = {
        maxFPS = g_graphics.getMaxFPS(),
        vsync = g_graphics.isVSyncEnabled(),
        antialiasing = g_graphics.getAntialiasingMode(),
        textureFiltering = g_graphics.isTextureFilteringEnabled(),
        drawLights = g_graphics.isDrawingLights()
    }
```

#### Finalização
```lua
    
    g_settings.setNode('graphics', settings)
    g_settings.save()
end

function graphicsSettings.updateInterface()
    local maxFPS = g_graphics.getMaxFPS()
    graphicsSettings.fpsSlider:setValue(maxFPS == 0 and 0 or (maxFPS - 30) / 2)
    graphicsSettings.vsyncBox:setChecked(g_graphics.isVSyncEnabled())
    graphicsSettings.lightsBox:setChecked(g_graphics.isDrawingLights())
    graphicsSettings.aaCombo:setCurrentOptionByData(g_graphics.getAntialiasingMode())
end
```

### Exemplo 2: Sistema de Shaders Dinâmicos

#### Inicialização e Configuração
```lua
-- modules/dynamic_shaders/dynamic_shaders.lua
dynamicShaders = {}

function dynamicShaders.init()
    dynamicShaders.activeShaders = {}
    dynamicShaders.window = g_ui.displayUI('dynamic_shaders')
    dynamicShaders.setupInterface()
    dynamicShaders.loadShaders()
    
    connect(g_game, {
        onGameStart = dynamicShaders.onGameStart,
        onGameEnd = dynamicShaders.onGameEnd
    })
end

function dynamicShaders.setupInterface()
    dynamicShaders.shaderList = dynamicShaders.window:getChildById('shaderList')
    dynamicShaders.previewArea = dynamicShaders.window:getChildById('previewArea')
    dynamicShaders.applyButton = dynamicShaders.window:getChildById('applyButton')
    dynamicShaders.removeButton = dynamicShaders.window:getChildById('removeButton')
    
    dynamicShaders.shaderList.onChildFocusChange = dynamicShaders.onShaderSelect
    dynamicShaders.applyButton.onClick = dynamicShaders.applySelectedShader
    dynamicShaders.removeButton.onClick = dynamicShaders.removeActiveShader
end
```

#### Funcionalidade 1
```lua

function dynamicShaders.loadShaders()
    -- Carregar shaders do diretório
    local shaderFiles = g_resources.listDirectoryFiles('/shaders/fragment/')
    
    for _, file in ipairs(shaderFiles) do
        if file:ends('.frag') then
            local name = file:sub(1, -6) -- Remove .frag
            dynamicShaders.registerShader(name, '/shaders/fragment/' .. file)
        end
    end
    
    dynamicShaders.updateShaderList()
end

function dynamicShaders.registerShader(name, path)
    g_shaders.createFragmentShader(name, path, false)
    
    local shaderInfo = {
        name = name,
        path = path,
        parameters = dynamicShaders.parseShaderParameters(path)
    }
```

#### Funcionalidade 2
```lua
    
    table.insert(dynamicShaders.activeShaders, shaderInfo)
end

function dynamicShaders.parseShaderParameters(path)
    local content = g_resources.readFileContents(path)
    local parameters = {}
    
    -- Parse uniforms do shader
    for line in content:gmatch('[^\r\n]+') do
        local uniform = line:match('uniform%s+(%w+)%s+(%w+);')
        if uniform then
            local type, name = uniform:match('(%w+)%s+(%w+)')
            table.insert(parameters, {type = type, name = name})
        end
    end
    
    return parameters
end

function dynamicShaders.updateShaderList()
```

#### Funcionalidade 3
```lua
    dynamicShaders.shaderList:destroyChildren()
    
    for _, shader in ipairs(dynamicShaders.activeShaders) do
        local item = g_ui.createWidget('UILabel', dynamicShaders.shaderList)
        item:setText(shader.name)
        item.shaderInfo = shader
    end
end

function dynamicShaders.onShaderSelect(list, focusedChild)
    if not focusedChild then return end
    
    local shader = focusedChild.shaderInfo
    dynamicShaders.showShaderPreview(shader)
end

function dynamicShaders.showShaderPreview(shader)
    dynamicShaders.previewArea:destroyChildren()
    
    -- Criar preview do shader
    local preview = g_ui.createWidget('UIWidget', dynamicShaders.previewArea)
    preview:setSize({width = 200, height = 200})
    preview:setShader(shader.name)
    
    -- Criar controles para parâmetros
    for _, param in ipairs(shader.parameters) do
        local control = dynamicShaders.createParameterControl(param, shader)
        control:addAnchor(AnchorTop, 'prev', AnchorBottom)
        control:addAnchor(AnchorLeft, 'parent', AnchorLeft)
    end
```

#### Funcionalidade 4
```lua
end

function dynamicShaders.createParameterControl(param, shader)
    local container = g_ui.createWidget('UIWidget', dynamicShaders.previewArea)
    container:setHeight(30)
    
    local label = g_ui.createWidget('UILabel', container)
    label:setText(param.name .. ':')
    label:setWidth(80)
    
    if param.type == 'float' then
        local slider = g_ui.createWidget('UISlider', container)
        slider:setMinimum(0)
        slider:setMaximum(100)
        slider:setValue(50)
        slider:addAnchor(AnchorLeft, label, AnchorRight)
        slider:addAnchor(AnchorRight, 'parent', AnchorRight)
        
        slider.onValueChange = function(slider, value)
            g_shaders.setUniformFloat(param.name, value / 100.0)
        end
```

#### Funcionalidade 5
```lua
    elseif param.type == 'vec2' then
        local xSlider = g_ui.createWidget('UISlider', container)
        local ySlider = g_ui.createWidget('UISlider', container)
        -- Configurar sliders para vec2
    end
    
    return container
end

function dynamicShaders.applySelectedShader()
    local selected = dynamicShaders.shaderList:getFocusedChild()
    if not selected then return end
    
    local shader = selected.shaderInfo
    local map = modules.game_interface.getMapPanel()
    map:setShader(shader.name)
    
    modules.game_textmessage.displayGameMessage('Shader aplicado: ' .. shader.name)
end

function dynamicShaders.removeActiveShader()
```

#### Finalização
```lua
    local map = modules.game_interface.getMapPanel()
    map:setShader('Default')
    
    modules.game_textmessage.displayGameMessage('Shader removido')
end

function dynamicShaders.onGameStart()
    -- Aplicar shader padrão quando conectar
    local defaultShader = g_settings.getString('dynamicShaders.default', 'Default')
    local map = modules.game_interface.getMapPanel()
    map:setShader(defaultShader)
end

function dynamicShaders.onGameEnd()
    -- Remover shaders quando desconectar
    dynamicShaders.removeActiveShader()
end
```

### Exemplo 3: Monitor de Performance Gráfica

#### Inicialização e Configuração
```lua
-- modules/graphics_monitor/graphics_monitor.lua
graphicsMonitor = {}

function graphicsMonitor.init()
    graphicsMonitor.window = g_ui.displayUI('graphics_monitor')
    graphicsMonitor.history = {}
    graphicsMonitor.maxHistory = 100
    graphicsMonitor.setupInterface()
    graphicsMonitor.startMonitoring()
end

function graphicsMonitor.setupInterface()
    graphicsMonitor.fpsLabel = graphicsMonitor.window:getChildById('fpsLabel')
    graphicsMonitor.avgLabel = graphicsMonitor.window:getChildById('avgLabel')
    graphicsMonitor.minLabel = graphicsMonitor.window:getChildById('minLabel')
    graphicsMonitor.maxLabel = graphicsMonitor.window:getChildById('maxLabel')
    graphicsMonitor.chartArea = graphicsMonitor.window:getChildById('chartArea')
    
    graphicsMonitor.resetButton = graphicsMonitor.window:getChildById('resetButton')
    graphicsMonitor.resetButton.onClick = graphicsMonitor.resetStats
end
```

#### Funcionalidade 1
```lua

function graphicsMonitor.startMonitoring()
    local updateEvent
    
    local function updateMonitor()
        local currentFPS = g_graphics.getCurrentFPS() or 0
        local averageFPS = g_graphics.getAverageFPS()
        
        -- Adicionar ao histórico
        table.insert(graphicsMonitor.history, {
            time = g_clock.millis(),
            fps = currentFPS
        })
        
        -- Limitar tamanho do histórico
        if #graphicsMonitor.history > graphicsMonitor.maxHistory then
            table.remove(graphicsMonitor.history, 1)
        end
        
        -- Calcular estatísticas
        local minFPS = math.huge
        local maxFPS = 0
        local totalFPS = 0
        
        for _, entry in ipairs(graphicsMonitor.history) do
            minFPS = math.min(minFPS, entry.fps)
            maxFPS = math.max(maxFPS, entry.fps)
            totalFPS = totalFPS + entry.fps
        end
```

#### Funcionalidade 2
```lua
        
        local avgFPS = #graphicsMonitor.history > 0 and (totalFPS / #graphicsMonitor.history) or 0
        
        -- Atualizar interface
        graphicsMonitor.fpsLabel:setText(string.format('FPS: %d', currentFPS))
        graphicsMonitor.avgLabel:setText(string.format('Avg: %.1f', avgFPS))
        graphicsMonitor.minLabel:setText(string.format('Min: %d', minFPS == math.huge and 0 or minFPS))
        graphicsMonitor.maxLabel:setText(string.format('Max: %d', maxFPS))
        
        -- Atualizar gráfico
        graphicsMonitor.updateChart()
        
        updateEvent = scheduleEvent(updateMonitor, 100)
    end
    
    updateEvent = scheduleEvent(updateMonitor, 100)
    graphicsMonitor.updateEvent = updateEvent
end

function graphicsMonitor.updateChart()
    graphicsMonitor.chartArea:destroyChildren()
    
    if #graphicsMonitor.history < 2 then return end
    
    local chartRect = graphicsMonitor.chartArea:getRect()
    local maxFPS = 0
    
    for _, entry in ipairs(graphicsMonitor.history) do
        maxFPS = math.max(maxFPS, entry.fps)
    end
```

#### Funcionalidade 3
```lua
    
    if maxFPS == 0 then return end
    
    -- Desenhar linhas do gráfico
    for i = 2, #graphicsMonitor.history do
        local prev = graphicsMonitor.history[i-1]
        local curr = graphicsMonitor.history[i]
        
        local x1 = (i-2) * (chartRect.width / (graphicsMonitor.maxHistory - 1))
        local y1 = chartRect.height - (prev.fps / maxFPS) * chartRect.height
        local x2 = (i-1) * (chartRect.width / (graphicsMonitor.maxHistory - 1))
        local y2 = chartRect.height - (curr.fps / maxFPS) * chartRect.height
        
        local line = g_ui.createWidget('UIWidget', graphicsMonitor.chartArea)
        line:setSize({width = 2, height = math.abs(y2 - y1)})
        line:setPosition({x = x2, y = math.min(y1, y2)})
        line:setBackgroundColor('#00FF00')
        
        -- Cor baseada no FPS
        if curr.fps < 30 then
            line:setBackgroundColor('#FF0000') -- Vermelho para FPS baixo
        elseif curr.fps < 60 then
            line:setBackgroundColor('#FFFF00') -- Amarelo para FPS médio
        else
            line:setBackgroundColor('#00FF00') -- Verde para FPS alto
        end
```

#### Finalização
```lua
    end
end

function graphicsMonitor.resetStats()
    graphicsMonitor.history = {}
    graphicsMonitor.chartArea:destroyChildren()
end

function graphicsMonitor.terminate()
    if graphicsMonitor.updateEvent then
        removeEvent(graphicsMonitor.updateEvent)
    end
end
```

---

Esta documentação cobre completamente o sistema de gráficos do OTClient, fornecendo exemplos práticos e detalhados para trabalhar com renderização, shaders, texturas e otimização. Use estes exemplos como base para criar sistemas avançados de configuração gráfica e efeitos visuais em seus módulos.
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

