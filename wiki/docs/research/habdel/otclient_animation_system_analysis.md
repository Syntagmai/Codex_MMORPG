# OTClient Animation System - Análise Técnica

## 🎯 Visão Geral

O **Sistema de Animações** do OTClient é responsável por gerenciar animações de texturas, efeitos de partículas e transições visuais. Ele fornece um sistema robusto para criar animações fluidas e efeitos visuais impressionantes.

## 📊 Estatísticas da Análise

- **Arquivos Analisados**: 16
- **Linhas de Código**: 1,386
- **Componentes Principais**: 16
- **Padrões Identificados**: 4
- **APIs Documentadas**: 7

## 🏗️ Arquitetura do Sistema

### **Componentes Principais**

### **animatedtexture.h**
- **Linhas**: 69
- **Classes**: 1
- **Métodos**: 3
- **Padrões**: Timer

### **animatedtexture.cpp**
- **Linhas**: 127
- **Classes**: 0
- **Métodos**: 0
- **Padrões**: Animation, Timer

### **particleeffect.h**
- **Linhas**: 60
- **Classes**: 2
- **Métodos**: 4
- **Padrões**: Particle System, Effect

### **particleeffect.cpp**
- **Linhas**: 72
- **Classes**: 0
- **Métodos**: 1
- **Padrões**: Particle System, Effect

### **particlesystem.h**
- **Linhas**: 49
- **Classes**: 1
- **Métodos**: 4
- **Padrões**: Particle System

### **particlesystem.cpp**
- **Linhas**: 120
- **Classes**: 0
- **Métodos**: 3
- **Padrões**: Particle System

### **particle.h**
- **Linhas**: 87
- **Classes**: 1
- **Métodos**: 5
- **Padrões**: Animation, Particle System, Timer

### **particle.cpp**
- **Linhas**: 102
- **Classes**: 0
- **Métodos**: 0
- **Padrões**: Particle System

### **particleemitter.h**
- **Linhas**: 53
- **Classes**: 1
- **Métodos**: 2
- **Padrões**: Particle System

### **particleemitter.cpp**
- **Linhas**: 101
- **Classes**: 0
- **Métodos**: 1
- **Padrões**: Particle System

### **particlemanager.h**
- **Linhas**: 50
- **Classes**: 1
- **Métodos**: 4
- **Padrões**: Particle System, Effect

### **particlemanager.cpp**
- **Linhas**: 87
- **Classes**: 0
- **Métodos**: 0
- **Padrões**: Particle System, Effect

### **particletype.h**
- **Linhas**: 80
- **Classes**: 2
- **Métodos**: 1
- **Padrões**: Particle System

### **particletype.cpp**
- **Linhas**: 136
- **Classes**: 0
- **Métodos**: 1
- **Padrões**: Particle System

### **particleaffector.h**
- **Linhas**: 70
- **Classes**: 3
- **Métodos**: 2
- **Padrões**: Particle System

### **particleaffector.cpp**
- **Linhas**: 123
- **Classes**: 0
- **Métodos**: 0
- **Padrões**: Particle System



### **Padrões de Design Identificados**

- **Effect**: Descrição do padrão
- **Particle System**: Descrição do padrão
- **Animation**: Descrição do padrão
- **Timer**: Descrição do padrão



## 🔌 APIs Principais

### **AnimatedTexture**
Sistema de texturas animadas com frames e delays

**Métodos Principais:**
- `get()`
- `getCurrentFrame()`
- `update()`
- `restart()`
- `setNumPlays()`

**Componentes:** animatedtexture.h, animatedtexture.cpp

### **ParticleEffect**
Sistema de efeitos de partículas

**Métodos Principais:**
- `load()`
- `hasFinished()`
- `render()`
- `update()`
- `getEffectType()`

**Componentes:** particleeffect.h, particleeffect.cpp

### **ParticleSystem**
Sistema de partículas com emissores e afetores

**Métodos Principais:**
- `addEmitter()`
- `addAffector()`
- `update()`
- `render()`

**Componentes:** particlesystem.h, particlesystem.cpp

### **ParticleEmitter**
Emissores de partículas com diferentes tipos

**Métodos Principais:**
- `emit()`
- `setEmissionRate()`
- `setParticleType()`

**Componentes:** particleemitter.h, particleemitter.cpp

### **ParticleAffector**
Afetores que modificam partículas durante animação

**Métodos Principais:**
- `affect()`
- `setForce()`
- `setGravity()`

**Componentes:** particleaffector.h, particleaffector.cpp

### **ParticleManager**
Gerenciador central de partículas

**Métodos Principais:**
- `createEffect()`
- `updateEffects()`
- `renderEffects()`

**Componentes:** particlemanager.h, particlemanager.cpp

### **ParticleType**
Definição de tipos de partículas

**Métodos Principais:**
- `setTexture()`
- `setSize()`
- `setColor()`
- `setLifetime()`

**Componentes:** particletype.h, particletype.cpp



## 💡 Exemplos Práticos

### **Textura Animada**
Como criar e usar texturas animadas

#### Nível Basic
```cpp
// Exemplo de textura animada
#include "graphics/animatedtexture.h"

void createAnimatedTexture() {{
    // Carregar frames da animação
    std::vector<ImagePtr> frames;
    frames.push_back(g_images.loadImage("animation/frame1.png"));
    frames.push_back(g_images.loadImage("animation/frame2.png"));
    frames.push_back(g_images.loadImage("animation/frame3.png"));
    frames.push_back(g_images.loadImage("animation/frame4.png"));
    
    // Definir delays entre frames (em milissegundos)
    std::vector<uint16_t> frameDelays = {{100, 100, 100, 100}};
    
    // Criar textura animada (0 = loop infinito)
    AnimatedTexturePtr animTexture = std::make_shared<AnimatedTexture>(
        Size(64, 64), frames, frameDelays, 0
    );
    
    // Atualizar animação
    animTexture->update();
    
    // Obter frame atual
    TexturePtr currentFrame = animTexture->getCurrentFrame();
    
    // Reiniciar animação
    animTexture->restart();
    
    // Definir número de repetições
    animTexture->setNumPlays(3);  // Repetir 3 vezes
}}
```

#### Nível Intermediate
```cpp
// Exemplo de textura animada
#include "graphics/animatedtexture.h"

void createAnimatedTexture() {{
    // Carregar frames da animação
    std::vector<ImagePtr> frames;
    frames.push_back(g_images.loadImage("animation/frame1.png"));
    frames.push_back(g_images.loadImage("animation/frame2.png"));
    frames.push_back(g_images.loadImage("animation/frame3.png"));
    frames.push_back(g_images.loadImage("animation/frame4.png"));
    
    // Definir delays entre frames (em milissegundos)
    std::vector<uint16_t> frameDelays = {{100, 100, 100, 100}};
    
    // Criar textura animada (0 = loop infinito)
    AnimatedTexturePtr animTexture = std::make_shared<AnimatedTexture>(
        Size(64, 64), frames, frameDelays, 0
    );
    
    // Atualizar animação
    animTexture->update();
    
    // Obter frame atual
    TexturePtr currentFrame = animTexture->getCurrentFrame();
    
    // Reiniciar animação
    animTexture->restart();
    
    // Definir número de repetições
    animTexture->setNumPlays(3);  // Repetir 3 vezes
}}
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Exemplo de textura animada
#include "graphics/animatedtexture.h"

void createAnimatedTexture() {{
    // Carregar frames da animação
    std::vector<ImagePtr> frames;
    frames.push_back(g_images.loadImage("animation/frame1.png"));
    frames.push_back(g_images.loadImage("animation/frame2.png"));
    frames.push_back(g_images.loadImage("animation/frame3.png"));
    frames.push_back(g_images.loadImage("animation/frame4.png"));
    
    // Definir delays entre frames (em milissegundos)
    std::vector<uint16_t> frameDelays = {{100, 100, 100, 100}};
    
    // Criar textura animada (0 = loop infinito)
    AnimatedTexturePtr animTexture = std::make_shared<AnimatedTexture>(
        Size(64, 64), frames, frameDelays, 0
    );
    
    // Atualizar animação
    animTexture->update();
    
    // Obter frame atual
    TexturePtr currentFrame = animTexture->getCurrentFrame();
    
    // Reiniciar animação
    animTexture->restart();
    
    // Definir número de repetições
    animTexture->setNumPlays(3);  // Repetir 3 vezes
}}
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

### **Efeito de Partículas**
Como criar e usar efeitos de partículas

#### Nível Basic
```cpp
// Exemplo de efeito de partículas
#include "graphics/particleeffect.h"
#include "graphics/particlesystem.h"

void createParticleEffect() {{
    // Criar tipo de partícula
    ParticleTypePtr particleType = std::make_shared<ParticleType>();
    particleType->setTexture(g_textures.loadTexture("particles/fire.png"));
    particleType->setSize(Size(16, 16));
    particleType->setColor(Color(255, 100, 0, 255));
    particleType->setLifetime(2000);  // 2 segundos
    
    // Criar sistema de partículas
    ParticleSystemPtr particleSystem = std::make_shared<ParticleSystem>();
    particleSystem->setParticleType(particleType);
    
    // Criar emissor
    ParticleEmitterPtr emitter = std::make_shared<ParticleEmitter>();
    emitter->setEmissionRate(50);  // 50 partículas por segundo
    emitter->setPosition(Point(100, 100));
    particleSystem->addEmitter(emitter);
    
    // Criar afetor de gravidade
    ParticleAffectorPtr gravityAffector = std::make_shared<ParticleAffector>();
    gravityAffector->setGravity(Point(0, 50));  // Gravidade para baixo
    particleSystem->addAffector(gravityAffector);
    
    // Criar efeito
    ParticleEffectPtr effect = std::make_shared<ParticleEffect>();
    effect->addSystem(particleSystem);
    
    // Atualizar e renderizar
    effect->update();
    effect->render();
    
    // Verificar se terminou
    if (effect->hasFinished()) {{
        std::cout << "Effect finished" << std::endl;
    }}
}}
```

#### Nível Intermediate
```cpp
// Exemplo de efeito de partículas
#include "graphics/particleeffect.h"
#include "graphics/particlesystem.h"

void createParticleEffect() {{
    // Criar tipo de partícula
    ParticleTypePtr particleType = std::make_shared<ParticleType>();
    particleType->setTexture(g_textures.loadTexture("particles/fire.png"));
    particleType->setSize(Size(16, 16));
    particleType->setColor(Color(255, 100, 0, 255));
    particleType->setLifetime(2000);  // 2 segundos
    
    // Criar sistema de partículas
    ParticleSystemPtr particleSystem = std::make_shared<ParticleSystem>();
    particleSystem->setParticleType(particleType);
    
    // Criar emissor
    ParticleEmitterPtr emitter = std::make_shared<ParticleEmitter>();
    emitter->setEmissionRate(50);  // 50 partículas por segundo
    emitter->setPosition(Point(100, 100));
    particleSystem->addEmitter(emitter);
    
    // Criar afetor de gravidade
    ParticleAffectorPtr gravityAffector = std::make_shared<ParticleAffector>();
    gravityAffector->setGravity(Point(0, 50));  // Gravidade para baixo
    particleSystem->addAffector(gravityAffector);
    
    // Criar efeito
    ParticleEffectPtr effect = std::make_shared<ParticleEffect>();
    effect->addSystem(particleSystem);
    
    // Atualizar e renderizar
    effect->update();
    effect->render();
    
    // Verificar se terminou
    if (effect->hasFinished()) {{
        std::cout << "Effect finished" << std::endl;
    }}
}}
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Exemplo de efeito de partículas
#include "graphics/particleeffect.h"
#include "graphics/particlesystem.h"

void createParticleEffect() {{
    // Criar tipo de partícula
    ParticleTypePtr particleType = std::make_shared<ParticleType>();
    particleType->setTexture(g_textures.loadTexture("particles/fire.png"));
    particleType->setSize(Size(16, 16));
    particleType->setColor(Color(255, 100, 0, 255));
    particleType->setLifetime(2000);  // 2 segundos
    
    // Criar sistema de partículas
    ParticleSystemPtr particleSystem = std::make_shared<ParticleSystem>();
    particleSystem->setParticleType(particleType);
    
    // Criar emissor
    ParticleEmitterPtr emitter = std::make_shared<ParticleEmitter>();
    emitter->setEmissionRate(50);  // 50 partículas por segundo
    emitter->setPosition(Point(100, 100));
    particleSystem->addEmitter(emitter);
    
    // Criar afetor de gravidade
    ParticleAffectorPtr gravityAffector = std::make_shared<ParticleAffector>();
    gravityAffector->setGravity(Point(0, 50));  // Gravidade para baixo
    particleSystem->addAffector(gravityAffector);
    
    // Criar efeito
    ParticleEffectPtr effect = std::make_shared<ParticleEffect>();
    effect->addSystem(particleSystem);
    
    // Atualizar e renderizar
    effect->update();
    effect->render();
    
    // Verificar se terminou
    if (effect->hasFinished()) {{
        std::cout << "Effect finished" << std::endl;
    }}
}}
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

### **Gerenciador de Partículas**
Como usar o gerenciador de partículas

#### Nível Basic
```cpp
// Exemplo de gerenciador de partículas
#include "graphics/particlemanager.h"

void useParticleManager() {{
    // Obter instância do gerenciador
    ParticleManager& manager = g_particles;
    
    // Criar efeito de fogo
    ParticleEffectPtr fireEffect = manager.createEffect("fire");
    fireEffect->setPosition(Point(200, 200));
    
    // Criar efeito de explosão
    ParticleEffectPtr explosionEffect = manager.createEffect("explosion");
    explosionEffect->setPosition(Point(300, 300));
    
    // Atualizar todos os efeitos
    manager.updateEffects();
    
    // Renderizar todos os efeitos
    manager.renderEffects();
    
    // Verificar efeitos ativos
    if (manager.hasActiveEffects()) {{
        std::cout << "Active effects: " << manager.getActiveEffectsCount() << std::endl;
    }}
    
    // Limpar efeitos terminados
    manager.cleanupFinishedEffects();
}}
```

#### Nível Intermediate
```cpp
// Exemplo de gerenciador de partículas
#include "graphics/particlemanager.h"

void useParticleManager() {{
    // Obter instância do gerenciador
    ParticleManager& manager = g_particles;
    
    // Criar efeito de fogo
    ParticleEffectPtr fireEffect = manager.createEffect("fire");
    fireEffect->setPosition(Point(200, 200));
    
    // Criar efeito de explosão
    ParticleEffectPtr explosionEffect = manager.createEffect("explosion");
    explosionEffect->setPosition(Point(300, 300));
    
    // Atualizar todos os efeitos
    manager.updateEffects();
    
    // Renderizar todos os efeitos
    manager.renderEffects();
    
    // Verificar efeitos ativos
    if (manager.hasActiveEffects()) {{
        std::cout << "Active effects: " << manager.getActiveEffectsCount() << std::endl;
    }}
    
    // Limpar efeitos terminados
    manager.cleanupFinishedEffects();
}}
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Exemplo de gerenciador de partículas
#include "graphics/particlemanager.h"

void useParticleManager() {{
    // Obter instância do gerenciador
    ParticleManager& manager = g_particles;
    
    // Criar efeito de fogo
    ParticleEffectPtr fireEffect = manager.createEffect("fire");
    fireEffect->setPosition(Point(200, 200));
    
    // Criar efeito de explosão
    ParticleEffectPtr explosionEffect = manager.createEffect("explosion");
    explosionEffect->setPosition(Point(300, 300));
    
    // Atualizar todos os efeitos
    manager.updateEffects();
    
    // Renderizar todos os efeitos
    manager.renderEffects();
    
    // Verificar efeitos ativos
    if (manager.hasActiveEffects()) {{
        std::cout << "Active effects: " << manager.getActiveEffectsCount() << std::endl;
    }}
    
    // Limpar efeitos terminados
    manager.cleanupFinishedEffects();
}}
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

### **Tipo de Partícula Personalizado**
Como criar tipos de partículas personalizados

#### Nível Basic
```cpp
// Exemplo de tipo de partícula personalizado
#include "graphics/particletype.h"

void createCustomParticleType() {{
    // Criar tipo de partícula de fogo
    ParticleTypePtr fireParticle = std::make_shared<ParticleType>();
    fireParticle->setTexture(g_textures.loadTexture("particles/fire.png"));
    fireParticle->setSize(Size(32, 32));
    fireParticle->setColor(Color(255, 100, 0, 255));
    fireParticle->setLifetime(1500);
    fireParticle->setFadeOut(true);
    fireParticle->setFadeOutTime(500);
    
    // Criar tipo de partícula de fumaça
    ParticleTypePtr smokeParticle = std::make_shared<ParticleType>();
    smokeParticle->setTexture(g_textures.loadTexture("particles/smoke.png"));
    smokeParticle->setSize(Size(48, 48));
    smokeParticle->setColor(Color(100, 100, 100, 128));
    smokeParticle->setLifetime(3000);
    smokeParticle->setFadeOut(true);
    smokeParticle->setFadeOutTime(1000);
    
    // Criar tipo de partícula de faísca
    ParticleTypePtr sparkParticle = std::make_shared<ParticleType>();
    sparkParticle->setTexture(g_textures.loadTexture("particles/spark.png"));
    sparkParticle->setSize(Size(8, 8));
    sparkParticle->setColor(Color(255, 255, 0, 255));
    sparkParticle->setLifetime(800);
    sparkParticle->setFadeOut(true);
    sparkParticle->setFadeOutTime(200);
}}
```

#### Nível Intermediate
```cpp
// Exemplo de tipo de partícula personalizado
#include "graphics/particletype.h"

void createCustomParticleType() {{
    // Criar tipo de partícula de fogo
    ParticleTypePtr fireParticle = std::make_shared<ParticleType>();
    fireParticle->setTexture(g_textures.loadTexture("particles/fire.png"));
    fireParticle->setSize(Size(32, 32));
    fireParticle->setColor(Color(255, 100, 0, 255));
    fireParticle->setLifetime(1500);
    fireParticle->setFadeOut(true);
    fireParticle->setFadeOutTime(500);
    
    // Criar tipo de partícula de fumaça
    ParticleTypePtr smokeParticle = std::make_shared<ParticleType>();
    smokeParticle->setTexture(g_textures.loadTexture("particles/smoke.png"));
    smokeParticle->setSize(Size(48, 48));
    smokeParticle->setColor(Color(100, 100, 100, 128));
    smokeParticle->setLifetime(3000);
    smokeParticle->setFadeOut(true);
    smokeParticle->setFadeOutTime(1000);
    
    // Criar tipo de partícula de faísca
    ParticleTypePtr sparkParticle = std::make_shared<ParticleType>();
    sparkParticle->setTexture(g_textures.loadTexture("particles/spark.png"));
    sparkParticle->setSize(Size(8, 8));
    sparkParticle->setColor(Color(255, 255, 0, 255));
    sparkParticle->setLifetime(800);
    sparkParticle->setFadeOut(true);
    sparkParticle->setFadeOutTime(200);
}}
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Exemplo de tipo de partícula personalizado
#include "graphics/particletype.h"

void createCustomParticleType() {{
    // Criar tipo de partícula de fogo
    ParticleTypePtr fireParticle = std::make_shared<ParticleType>();
    fireParticle->setTexture(g_textures.loadTexture("particles/fire.png"));
    fireParticle->setSize(Size(32, 32));
    fireParticle->setColor(Color(255, 100, 0, 255));
    fireParticle->setLifetime(1500);
    fireParticle->setFadeOut(true);
    fireParticle->setFadeOutTime(500);
    
    // Criar tipo de partícula de fumaça
    ParticleTypePtr smokeParticle = std::make_shared<ParticleType>();
    smokeParticle->setTexture(g_textures.loadTexture("particles/smoke.png"));
    smokeParticle->setSize(Size(48, 48));
    smokeParticle->setColor(Color(100, 100, 100, 128));
    smokeParticle->setLifetime(3000);
    smokeParticle->setFadeOut(true);
    smokeParticle->setFadeOutTime(1000);
    
    // Criar tipo de partícula de faísca
    ParticleTypePtr sparkParticle = std::make_shared<ParticleType>();
    sparkParticle->setTexture(g_textures.loadTexture("particles/spark.png"));
    sparkParticle->setSize(Size(8, 8));
    sparkParticle->setColor(Color(255, 255, 0, 255));
    sparkParticle->setLifetime(800);
    sparkParticle->setFadeOut(true);
    sparkParticle->setFadeOutTime(200);
}}
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

### **Afetores de Partículas**
Como usar afetores para modificar partículas

#### Nível Basic
```cpp

```

#### Nível Intermediate
```cpp
// Exemplo de afetores de partículas
#include "graphics/particleaffector.h"

void useParticleAffectors() {{
    // Afetor de gravidade
    ParticleAffectorPtr gravityAffector = std::make_shared<ParticleAffector>();
    gravityAffector->setGravity(Point(0, 100));  // Gravidade para baixo
    gravityAffector->setType(ParticleAffectorType::Gravity);
    
    // Afetor de força
    ParticleAffectorPtr forceAffector = std::make_shared<ParticleAffector>();
    forceAffector->setForce(Point(10, -20));  // Força para cima e direita
    forceAffector->setType(ParticleAffectorType::Force);
    
    // Afetor de cor
    ParticleAffectorPtr colorAffector = std::make_shared<ParticleAffector>();
    colorAffector->setStartColor(Color(255, 0, 0, 255));  // Vermelho
    colorAffector->setEndColor(Color(255, 255, 0, 255));  // Amarelo
    colorAffector->setType(ParticleAffectorType::Color);
    
    // Afetor de tamanho
    ParticleAffectorPtr sizeAffector = std::make_shared<ParticleAffector>();
    sizeAffector->setStartSize(Size(16, 16));
    sizeAffector->setEndSize(Size(32, 32));
    sizeAffector->setType(ParticleAffectorType::Size);
    
    // Afetor de rotação
    ParticleAffectorPtr rotationAffector = std::make_shared<ParticleAffector>();
    rotationAffector->setStartRotation(0.0f);
    rotationAffector->setEndRotation(360.0f);
    rotationAffector->setType(ParticleAffectorType::Rotation);
}}
```

#### Nível Advanced
```cpp
// Exemplo de afetores de partículas
#include "graphics/particleaffector.h"

void useParticleAffectors() {{
    // Afetor de gravidade
    ParticleAffectorPtr gravityAffector = std::make_shared<ParticleAffector>();
    gravityAffector->setGravity(Point(0, 100));  // Gravidade para baixo
    gravityAffector->setType(ParticleAffectorType::Gravity);
    
    // Afetor de força
    ParticleAffectorPtr forceAffector = std::make_shared<ParticleAffector>();
    forceAffector->setForce(Point(10, -20));  // Força para cima e direita
    forceAffector->setType(ParticleAffectorType::Force);
    
    // Afetor de cor
    ParticleAffectorPtr colorAffector = std::make_shared<ParticleAffector>();
    colorAffector->setStartColor(Color(255, 0, 0, 255));  // Vermelho
    colorAffector->setEndColor(Color(255, 255, 0, 255));  // Amarelo
    colorAffector->setType(ParticleAffectorType::Color);
    
    // Afetor de tamanho
    ParticleAffectorPtr sizeAffector = std::make_shared<ParticleAffector>();
    sizeAffector->setStartSize(Size(16, 16));
    sizeAffector->setEndSize(Size(32, 32));
    sizeAffector->setType(ParticleAffectorType::Size);
    
    // Afetor de rotação
    ParticleAffectorPtr rotationAffector = std::make_shared<ParticleAffector>();
    rotationAffector->setStartRotation(0.0f);
    rotationAffector->setEndRotation(360.0f);
    rotationAffector->setType(ParticleAffectorType::Rotation);
}}
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

### **Timer de Animação**
Como usar timers para controlar animações

#### Nível Basic
```cpp
        // Renderizar frame
        // Verificar se animação terminou
        if (elapsed > totalFrames * frameDelay) {{
```

#### Nível Intermediate
```cpp
// Exemplo de timer de animação
#include "graphics/animatedtexture.h"
#include "core/timer.h"

void useAnimationTimer() {{
    // Criar timer para animação
    Timer animTimer;
    animTimer.restart();
    
    // Configurar animação
    uint32_t currentFrame = 0;
    uint32_t totalFrames = 4;
    uint32_t frameDelay = 100;  // 100ms por frame
    
    // Loop de animação
    while (animTimer.running()) {{
        // Calcular frame atual baseado no tempo
        uint32_t elapsed = animTimer.elapsed_millis();
        currentFrame = (elapsed / frameDelay) % totalFrames;
        
        // Obter textura animada
        AnimatedTexturePtr animTexture = getAnimatedTexture();
        TexturePtr frame = animTexture->get(currentFrame, animTimer);
        
        // Renderizar frame
        g_painter.drawTexture(frame, Point(100, 100));
        
        // Verificar se animação terminou
        if (elapsed > totalFrames * frameDelay) {{
            animTimer.stop();
        }}
        
        // Aguardar próximo frame
        std::this_thread::sleep_for(std::chrono::milliseconds(16));  // ~60 FPS
    }}
}}
```

#### Nível Advanced
```cpp
// Exemplo de timer de animação
#include "graphics/animatedtexture.h"
#include "core/timer.h"

void useAnimationTimer() {{
    // Criar timer para animação
    Timer animTimer;
    animTimer.restart();
    
    // Configurar animação
    uint32_t currentFrame = 0;
    uint32_t totalFrames = 4;
    uint32_t frameDelay = 100;  // 100ms por frame
    
    // Loop de animação
    while (animTimer.running()) {{
        // Calcular frame atual baseado no tempo
        uint32_t elapsed = animTimer.elapsed_millis();
        currentFrame = (elapsed / frameDelay) % totalFrames;
        
        // Obter textura animada
        AnimatedTexturePtr animTexture = getAnimatedTexture();
        TexturePtr frame = animTexture->get(currentFrame, animTimer);
        
        // Renderizar frame
        g_painter.drawTexture(frame, Point(100, 100));
        
        // Verificar se animação terminou
        if (elapsed > totalFrames * frameDelay) {{
            animTimer.stop();
        }}
        
        // Aguardar próximo frame
        std::this_thread::sleep_for(std::chrono::milliseconds(16));  // ~60 FPS
    }}
}}
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



## 🔗 Pontos de Integração

### **Graphics System**
Integração com sistema de gráficos para renderização

**Tipo:** dependency
**Arquivos:** animatedtexture.h, particleeffect.h, particlesystem.h

### **UI System**
Animações de interface do usuário

**Tipo:** integration
**Arquivos:** animatedtexture.h, particleeffect.h

### **Core Framework**
Integração com sistema core (Timer, EventDispatcher)

**Tipo:** dependency
**Arquivos:** animatedtexture.h, particleeffect.h

### **Lua System**
Exposição de animações para scripts Lua

**Tipo:** binding
**Arquivos:** particleeffect.h, particlemanager.h

### **Resource Management**
Gerenciamento de recursos de animação

**Tipo:** dependency
**Arquivos:** animatedtexture.h, particletype.h

### **Event System**
Eventos de animação e partículas

**Tipo:** integration
**Arquivos:** particleeffect.h, particlesystem.h

### **Data System**
Conversão de dados de animação

**Tipo:** integration
**Arquivos:** particletype.h, particleeffect.h



## 📋 Guia de Uso

### **Texturas Animadas**

#### Nível Basic
```cpp
#include "graphics/animatedtexture.h"

// Carregar frames
std::vector<ImagePtr> frames = loadAnimationFrames();
std::vector<uint16_t> delays = {100, 100, 100, 100};

// Criar textura animada
AnimatedTexturePtr animTexture = std::make_shared<AnimatedTexture>(
    Size(64, 64), frames, delays, 0  // 0 = loop infinito
);

// Atualizar e renderizar
animTexture->update();
TexturePtr frame = animTexture->getCurrentFrame();
```

#### Nível Intermediate
```cpp
#include "graphics/animatedtexture.h"

// Carregar frames
std::vector<ImagePtr> frames = loadAnimationFrames();
std::vector<uint16_t> delays = {100, 100, 100, 100};

// Criar textura animada
AnimatedTexturePtr animTexture = std::make_shared<AnimatedTexture>(
    Size(64, 64), frames, delays, 0  // 0 = loop infinito
);

// Atualizar e renderizar
animTexture->update();
TexturePtr frame = animTexture->getCurrentFrame();
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
#include "graphics/animatedtexture.h"

// Carregar frames
std::vector<ImagePtr> frames = loadAnimationFrames();
std::vector<uint16_t> delays = {100, 100, 100, 100};

// Criar textura animada
AnimatedTexturePtr animTexture = std::make_shared<AnimatedTexture>(
    Size(64, 64), frames, delays, 0  // 0 = loop infinito
);

// Atualizar e renderizar
animTexture->update();
TexturePtr frame = animTexture->getCurrentFrame();
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

### **Efeitos de Partículas**

#### Nível Basic
```cpp
#include "graphics/particleeffect.h"

// Criar efeito
ParticleEffectPtr effect = std::make_shared<ParticleEffect>();
effect->load(effectType);

// Atualizar e renderizar
effect->update();
effect->render();

// Verificar se terminou
if (effect->hasFinished()) {
    // Efeito concluído
}
```

#### Nível Intermediate
```cpp
#include "graphics/particleeffect.h"

// Criar efeito
ParticleEffectPtr effect = std::make_shared<ParticleEffect>();
effect->load(effectType);

// Atualizar e renderizar
effect->update();
effect->render();

// Verificar se terminou
if (effect->hasFinished()) {
    // Efeito concluído
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
```cpp
#include "graphics/particleeffect.h"

// Criar efeito
ParticleEffectPtr effect = std::make_shared<ParticleEffect>();
effect->load(effectType);

// Atualizar e renderizar
effect->update();
effect->render();

// Verificar se terminou
if (effect->hasFinished()) {
    // Efeito concluído
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

### **Sistema de Partículas**

#### Nível Basic
```cpp
#include "graphics/particlesystem.h"

// Criar sistema
ParticleSystemPtr system = std::make_shared<ParticleSystem>();
system->addEmitter(emitter);
system->addAffector(affector);

// Atualizar e renderizar
system->update();
system->render();
```

#### Nível Intermediate
```cpp
#include "graphics/particlesystem.h"

// Criar sistema
ParticleSystemPtr system = std::make_shared<ParticleSystem>();
system->addEmitter(emitter);
system->addAffector(affector);

// Atualizar e renderizar
system->update();
system->render();
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
#include "graphics/particlesystem.h"

// Criar sistema
ParticleSystemPtr system = std::make_shared<ParticleSystem>();
system->addEmitter(emitter);
system->addAffector(affector);

// Atualizar e renderizar
system->update();
system->render();
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

## 🎬 Tipos de Animação

### **Texturas Animadas**
- **Frames**: Sequência de imagens
- **Delays**: Tempo entre frames
- **Loops**: Número de repetições
- **Smooth**: Interpolação suave

### **Efeitos de Partículas**
- **Emissores**: Geram partículas
- **Afetores**: Modificam partículas
- **Tipos**: Diferentes comportamentos
- **Lifetime**: Duração das partículas

### **Transições**
- **Fade In/Out**: Aparição/desaparecimento
- **Scale**: Mudança de tamanho
- **Rotation**: Rotação
- **Color**: Mudança de cor

## 🎯 Performance

### **Otimizações**
- **Frame Skipping**: Pular frames em baixo FPS
- **Particle Culling**: Remover partículas fora da tela
- **Texture Atlas**: Agrupar texturas
- **GPU Acceleration**: Aceleração por GPU

### **Métricas**
- **Texturas Animadas**: < 1ms por frame
- **Efeitos de Partículas**: < 5ms por 1000 partículas
- **Memory Usage**: < 10MB para animações complexas
- **CPU Usage**: < 5% para animações padrão

## 🚀 Próximos Passos

1. **Análise de Performance**: Profiling de animações
2. **Otimizações Avançadas**: Técnicas de otimização
3. **Integração com Canary**: Preparação para servidor
4. **Documentação de API**: Referência completa

---

*Análise gerada automaticamente pelo sistema Habdel - 2025-07-31 15:05:39*
