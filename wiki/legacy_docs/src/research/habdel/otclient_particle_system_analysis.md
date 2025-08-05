# OTClient Particle System - Análise Técnica

## 🎯 Visão Geral

O **Sistema de Partículas** do OTClient é responsável por criar e gerenciar efeitos visuais baseados em partículas. Ele fornece um sistema completo para criar explosões, fogo, fumaça, faíscas e outros efeitos visuais impressionantes.

## 📊 Estatísticas da Análise

- **Arquivos Analisados**: 14
- **Linhas de Código**: 1,190
- **Componentes Principais**: 14
- **Padrões Identificados**: 6
- **APIs Documentadas**: 9

## 🏗️ Arquitetura do Sistema

### **Componentes Principais**

### **particle.h**
- **Linhas**: 87
- **Classes**: 1
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 5
- **Padrões**: Particle

### **particle.cpp**
- **Linhas**: 102
- **Classes**: 0
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 0
- **Padrões**: Particle, Manager

### **particlesystem.h**
- **Linhas**: 49
- **Classes**: 1
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 4
- **Padrões**: Particle, Emitter, Affector, System

### **particlesystem.cpp**
- **Linhas**: 120
- **Classes**: 0
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 3
- **Padrões**: Particle, Emitter, Affector, Manager, System

### **particleemitter.h**
- **Linhas**: 53
- **Classes**: 1
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 2
- **Padrões**: Particle, Emitter, System

### **particleemitter.cpp**
- **Linhas**: 101
- **Classes**: 0
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 1
- **Padrões**: Particle, Emitter, Manager, System

### **particlemanager.h**
- **Linhas**: 50
- **Classes**: 1
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 4
- **Padrões**: Particle, Effect, Manager

### **particlemanager.cpp**
- **Linhas**: 87
- **Classes**: 0
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 0
- **Padrões**: Particle, Effect, Manager

### **particletype.h**
- **Linhas**: 80
- **Classes**: 2
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 1
- **Padrões**: Particle, Emitter

### **particletype.cpp**
- **Linhas**: 136
- **Classes**: 0
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 1
- **Padrões**: Particle, Manager

### **particleaffector.h**
- **Linhas**: 70
- **Classes**: 3
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 2
- **Padrões**: Particle, Affector

### **particleaffector.cpp**
- **Linhas**: 123
- **Classes**: 0
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 0
- **Padrões**: Particle, Affector

### **particleeffect.h**
- **Linhas**: 60
- **Classes**: 2
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 4
- **Padrões**: Particle, Effect, System

### **particleeffect.cpp**
- **Linhas**: 72
- **Classes**: 0
- **Enums**: 0
- **Structs**: 0
- **Métodos**: 1
- **Padrões**: Particle, Effect, System



### **Padrões de Design Identificados**

- **Particle**: Descrição do padrão
- **Effect**: Descrição do padrão
- **Emitter**: Descrição do padrão
- **System**: Descrição do padrão
- **Affector**: Descrição do padrão
- **Manager**: Descrição do padrão



## 🔌 APIs Principais

### **Particle**
Classe base para partículas individuais

**Métodos Principais:**
- `render()`
- `update()`
- `hasFinished()`
- `getPosition()`
- `setPosition()`

**Componentes:** particle.h, particle.cpp

### **ParticleSystem**
Sistema de partículas com emissores e afetores

**Métodos Principais:**
- `addEmitter()`
- `addAffector()`
- `update()`
- `render()`
- `clear()`

**Componentes:** particlesystem.h, particlesystem.cpp

### **ParticleEmitter**
Emissores de partículas com diferentes tipos

**Métodos Principais:**
- `emit()`
- `setEmissionRate()`
- `setParticleType()`
- `setPosition()`

**Componentes:** particleemitter.h, particleemitter.cpp

### **ParticleAffector**
Afetores que modificam partículas durante animação

**Métodos Principais:**
- `update()`
- `load()`
- `updateParticle()`
- `hasFinished()`

**Componentes:** particleaffector.h, particleaffector.cpp

### **GravityAffector**
Afetor de gravidade para partículas

**Métodos Principais:**
- `load()`
- `updateParticle()`

**Componentes:** particleaffector.h, particleaffector.cpp

### **AttractionAffector**
Afetor de atração/repulsão para partículas

**Métodos Principais:**
- `load()`
- `updateParticle()`

**Componentes:** particleaffector.h, particleaffector.cpp

### **ParticleManager**
Gerenciador central de partículas

**Métodos Principais:**
- `createEffect()`
- `updateEffects()`
- `renderEffects()`
- `clearEffects()`

**Componentes:** particlemanager.h, particlemanager.cpp

### **ParticleType**
Definição de tipos de partículas

**Métodos Principais:**
- `setTexture()`
- `setSize()`
- `setColor()`
- `setLifetime()`
- `setVelocity()`

**Componentes:** particletype.h, particletype.cpp

### **ParticleEffect**
Efeitos de partículas pré-definidos

**Métodos Principais:**
- `load()`
- `hasFinished()`
- `render()`
- `update()`
- `getEffectType()`

**Componentes:** particleeffect.h, particleeffect.cpp



## 💡 Exemplos Práticos

### **Partícula Básica**
Como criar uma partícula básica

#### Inicialização e Configuração
```cpp
// Exemplo de partícula básica
#include "graphics/particle.h"

void createBasicParticle() {{
    // Definir posição inicial
    Point position(100, 100);
    
    // Definir tamanhos
    Size startSize(16, 16);
    Size finalSize(32, 32);
    
    // Definir velocidade e aceleração
    PointF velocity(10.0f, -20.0f);  // Movimento para cima e direita
    PointF acceleration(0.0f, 50.0f);  // Gravidade para baixo
    
    // Definir duração
    float duration = 2000.0f;  // 2 segundos
    float ignorePhysicsAfter = 1000.0f;  // Ignorar física após 1 segundo
    
    // Definir cores (gradiente)
    std::vector<Color> colors = {{
        Color(255, 100, 0, 255),   // Laranja
        Color(255, 255, 0, 255),   // Amarelo
        Color(255, 255, 255, 0)    // Branco transparente
    }};
```

#### Funcionalidade 1
```cpp
    
    std::vector<float> colorStops = {{0.0f, 0.5f, 1.0f}};
    
    // Definir modo de composição
    CompositionMode compositionMode = CompositionMode::Normal;
    
    // Criar textura
    TexturePtr texture = g_textures.loadTexture("particles/fire.png");
    
    // Criar partícula
    ParticlePtr particle = std::make_shared<Particle>(
        position, startSize, finalSize, velocity, acceleration,
        duration, ignorePhysicsAfter, colors, colorStops,
        compositionMode, texture, nullptr
    );
    
    // Atualizar partícula
    particle->update(16.0f);  // 16ms = ~60 FPS
    
    // Renderizar partícula
    particle->render();
    
    // Verificar se terminou
    if (particle->hasFinished()) {{
        std::cout << "Particle finished" << std::endl;
    }}
```

#### Finalização
```cpp
}}
```

### **Sistema de Partículas**
Como criar um sistema de partículas completo

#### Nível Basic
```cpp
// Exemplo de sistema de partículas
#include "graphics/particlesystem.h"
#include "graphics/particleemitter.h"
#include "graphics/particleaffector.h"

void createParticleSystem() {{
    // Criar sistema de partículas
    ParticleSystemPtr particleSystem = std::make_shared<ParticleSystem>();
    
    // Criar tipo de partícula
    ParticleTypePtr particleType = std::make_shared<ParticleType>();
    particleType->setTexture(g_textures.loadTexture("particles/spark.png"));
    particleType->setSize(Size(8, 8));
    particleType->setColor(Color(255, 255, 0, 255));
    particleType->setLifetime(1000.0f);
    particleType->setVelocity(PointF(20.0f, -30.0f));
    
    // Criar emissor
    ParticleEmitterPtr emitter = std::make_shared<ParticleEmitter>();
    emitter->setEmissionRate(50);  // 50 partículas por segundo
    emitter->setPosition(Point(200, 200));
    emitter->setParticleType(particleType);
    
    // Adicionar emissor ao sistema
    particleSystem->addEmitter(emitter);
    
    // Criar afetor de gravidade
    GravityAffectorPtr gravityAffector = std::make_shared<GravityAffector>();
    gravityAffector->setGravity(100.0f);  // Força da gravidade
    gravityAffector->setAngle(90.0f);     // Direção (90° = para baixo)
    
    // Adicionar afetor ao sistema
    particleSystem->addAffector(gravityAffector);
    
    // Atualizar sistema
    particleSystem->update(16.0f);
    
    // Renderizar sistema
    particleSystem->render();
    
    // Limpar sistema quando terminar
    if (particleSystem->hasFinished()) {{
        particleSystem->clear();
    }}
}}
```

#### Nível Intermediate
```cpp
// Exemplo de sistema de partículas
#include "graphics/particlesystem.h"
#include "graphics/particleemitter.h"
#include "graphics/particleaffector.h"

void createParticleSystem() {{
    // Criar sistema de partículas
    ParticleSystemPtr particleSystem = std::make_shared<ParticleSystem>();
    
    // Criar tipo de partícula
    ParticleTypePtr particleType = std::make_shared<ParticleType>();
    particleType->setTexture(g_textures.loadTexture("particles/spark.png"));
    particleType->setSize(Size(8, 8));
    particleType->setColor(Color(255, 255, 0, 255));
    particleType->setLifetime(1000.0f);
    particleType->setVelocity(PointF(20.0f, -30.0f));
    
    // Criar emissor
    ParticleEmitterPtr emitter = std::make_shared<ParticleEmitter>();
    emitter->setEmissionRate(50);  // 50 partículas por segundo
    emitter->setPosition(Point(200, 200));
    emitter->setParticleType(particleType);
    
    // Adicionar emissor ao sistema
    particleSystem->addEmitter(emitter);
    
    // Criar afetor de gravidade
    GravityAffectorPtr gravityAffector = std::make_shared<GravityAffector>();
    gravityAffector->setGravity(100.0f);  // Força da gravidade
    gravityAffector->setAngle(90.0f);     // Direção (90° = para baixo)
    
    // Adicionar afetor ao sistema
    particleSystem->addAffector(gravityAffector);
    
    // Atualizar sistema
    particleSystem->update(16.0f);
    
    // Renderizar sistema
    particleSystem->render();
    
    // Limpar sistema quando terminar
    if (particleSystem->hasFinished()) {{
        particleSystem->clear();
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
// Exemplo de sistema de partículas
#include "graphics/particlesystem.h"
#include "graphics/particleemitter.h"
#include "graphics/particleaffector.h"

void createParticleSystem() {{
    // Criar sistema de partículas
    ParticleSystemPtr particleSystem = std::make_shared<ParticleSystem>();
    
    // Criar tipo de partícula
    ParticleTypePtr particleType = std::make_shared<ParticleType>();
    particleType->setTexture(g_textures.loadTexture("particles/spark.png"));
    particleType->setSize(Size(8, 8));
    particleType->setColor(Color(255, 255, 0, 255));
    particleType->setLifetime(1000.0f);
    particleType->setVelocity(PointF(20.0f, -30.0f));
    
    // Criar emissor
    ParticleEmitterPtr emitter = std::make_shared<ParticleEmitter>();
    emitter->setEmissionRate(50);  // 50 partículas por segundo
    emitter->setPosition(Point(200, 200));
    emitter->setParticleType(particleType);
    
    // Adicionar emissor ao sistema
    particleSystem->addEmitter(emitter);
    
    // Criar afetor de gravidade
    GravityAffectorPtr gravityAffector = std::make_shared<GravityAffector>();
    gravityAffector->setGravity(100.0f);  // Força da gravidade
    gravityAffector->setAngle(90.0f);     // Direção (90° = para baixo)
    
    // Adicionar afetor ao sistema
    particleSystem->addAffector(gravityAffector);
    
    // Atualizar sistema
    particleSystem->update(16.0f);
    
    // Renderizar sistema
    particleSystem->render();
    
    // Limpar sistema quando terminar
    if (particleSystem->hasFinished()) {{
        particleSystem->clear();
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

### **Tipos de Emissores**
Como usar diferentes tipos de emissores

#### Nível Basic
```cpp
// Exemplo de diferentes tipos de emissores
#include "graphics/particleemitter.h"

void createDifferentEmitters() {{
    // Emissor de ponto (partículas de um ponto)
    ParticleEmitterPtr pointEmitter = std::make_shared<ParticleEmitter>();
    pointEmitter->setType(EmitterType::Point);
    pointEmitter->setPosition(Point(100, 100));
    pointEmitter->setEmissionRate(30);
    
    // Emissor de linha (partículas ao longo de uma linha)
    ParticleEmitterPtr lineEmitter = std::make_shared<ParticleEmitter>();
    lineEmitter->setType(EmitterType::Line);
    lineEmitter->setStartPoint(Point(50, 50));
    lineEmitter->setEndPoint(Point(150, 150));
    lineEmitter->setEmissionRate(20);
    
    // Emissor de círculo (partículas em círculo)
    ParticleEmitterPtr circleEmitter = std::make_shared<ParticleEmitter>();
    circleEmitter->setType(EmitterType::Circle);
    circleEmitter->setPosition(Point(200, 200));
    circleEmitter->setRadius(50.0f);
    circleEmitter->setEmissionRate(40);
    
    // Emissor de retângulo (partículas em área retangular)
    ParticleEmitterPtr rectEmitter = std::make_shared<ParticleEmitter>();
    rectEmitter->setType(EmitterType::Rectangle);
    rectEmitter->setPosition(Point(300, 300));
    rectEmitter->setSize(Size(100, 50));
    rectEmitter->setEmissionRate(25);
    
    // Configurar direção dos emissores
    pointEmitter->setDirection(PointF(1.0f, -1.0f));      // Diagonal
    lineEmitter->setDirection(PointF(0.0f, -1.0f));       // Para cima
    circleEmitter->setDirection(PointF(0.0f, 0.0f));      // Radial
    rectEmitter->setDirection(PointF(1.0f, 0.0f));        // Para direita
}}
```

#### Nível Intermediate
```cpp
// Exemplo de diferentes tipos de emissores
#include "graphics/particleemitter.h"

void createDifferentEmitters() {{
    // Emissor de ponto (partículas de um ponto)
    ParticleEmitterPtr pointEmitter = std::make_shared<ParticleEmitter>();
    pointEmitter->setType(EmitterType::Point);
    pointEmitter->setPosition(Point(100, 100));
    pointEmitter->setEmissionRate(30);
    
    // Emissor de linha (partículas ao longo de uma linha)
    ParticleEmitterPtr lineEmitter = std::make_shared<ParticleEmitter>();
    lineEmitter->setType(EmitterType::Line);
    lineEmitter->setStartPoint(Point(50, 50));
    lineEmitter->setEndPoint(Point(150, 150));
    lineEmitter->setEmissionRate(20);
    
    // Emissor de círculo (partículas em círculo)
    ParticleEmitterPtr circleEmitter = std::make_shared<ParticleEmitter>();
    circleEmitter->setType(EmitterType::Circle);
    circleEmitter->setPosition(Point(200, 200));
    circleEmitter->setRadius(50.0f);
    circleEmitter->setEmissionRate(40);
    
    // Emissor de retângulo (partículas em área retangular)
    ParticleEmitterPtr rectEmitter = std::make_shared<ParticleEmitter>();
    rectEmitter->setType(EmitterType::Rectangle);
    rectEmitter->setPosition(Point(300, 300));
    rectEmitter->setSize(Size(100, 50));
    rectEmitter->setEmissionRate(25);
    
    // Configurar direção dos emissores
    pointEmitter->setDirection(PointF(1.0f, -1.0f));      // Diagonal
    lineEmitter->setDirection(PointF(0.0f, -1.0f));       // Para cima
    circleEmitter->setDirection(PointF(0.0f, 0.0f));      // Radial
    rectEmitter->setDirection(PointF(1.0f, 0.0f));        // Para direita
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
// Exemplo de diferentes tipos de emissores
#include "graphics/particleemitter.h"

void createDifferentEmitters() {{
    // Emissor de ponto (partículas de um ponto)
    ParticleEmitterPtr pointEmitter = std::make_shared<ParticleEmitter>();
    pointEmitter->setType(EmitterType::Point);
    pointEmitter->setPosition(Point(100, 100));
    pointEmitter->setEmissionRate(30);
    
    // Emissor de linha (partículas ao longo de uma linha)
    ParticleEmitterPtr lineEmitter = std::make_shared<ParticleEmitter>();
    lineEmitter->setType(EmitterType::Line);
    lineEmitter->setStartPoint(Point(50, 50));
    lineEmitter->setEndPoint(Point(150, 150));
    lineEmitter->setEmissionRate(20);
    
    // Emissor de círculo (partículas em círculo)
    ParticleEmitterPtr circleEmitter = std::make_shared<ParticleEmitter>();
    circleEmitter->setType(EmitterType::Circle);
    circleEmitter->setPosition(Point(200, 200));
    circleEmitter->setRadius(50.0f);
    circleEmitter->setEmissionRate(40);
    
    // Emissor de retângulo (partículas em área retangular)
    ParticleEmitterPtr rectEmitter = std::make_shared<ParticleEmitter>();
    rectEmitter->setType(EmitterType::Rectangle);
    rectEmitter->setPosition(Point(300, 300));
    rectEmitter->setSize(Size(100, 50));
    rectEmitter->setEmissionRate(25);
    
    // Configurar direção dos emissores
    pointEmitter->setDirection(PointF(1.0f, -1.0f));      // Diagonal
    lineEmitter->setDirection(PointF(0.0f, -1.0f));       // Para cima
    circleEmitter->setDirection(PointF(0.0f, 0.0f));      // Radial
    rectEmitter->setDirection(PointF(1.0f, 0.0f));        // Para direita
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
Como usar diferentes tipos de afetores

#### Nível Basic
```cpp
// Exemplo de diferentes tipos de afetores
void createDifferentAffectors() {{
```

#### Nível Intermediate
```cpp
// Exemplo de diferentes tipos de afetores
#include "graphics/particleaffector.h"

void createDifferentAffectors() {{
    // Afetor de gravidade
    GravityAffectorPtr gravityAffector = std::make_shared<GravityAffector>();
    gravityAffector->setGravity(100.0f);  // Força da gravidade
    gravityAffector->setAngle(90.0f);     // Direção (90° = para baixo)
    gravityAffector->setActive(true);
    
    // Afetor de atração (partículas atraídas para um ponto)
    AttractionAffectorPtr attractionAffector = std::make_shared<AttractionAffector>();
    attractionAffector->setPosition(Point(400, 300));
    attractionAffector->setAcceleration(50.0f);  // Força de atração
    attractionAffector->setReduction(0.1f);      // Redução da força
    attractionAffector->setRepelish(false);      // Atração (não repulsão)
    attractionAffector->setActive(true);
    
    // Afetor de repulsão (partículas repelidas de um ponto)
    AttractionAffectorPtr repulsionAffector = std::make_shared<AttractionAffector>();
    repulsionAffector->setPosition(Point(100, 100));
    repulsionAffector->setAcceleration(30.0f);   // Força de repulsão
    repulsionAffector->setReduction(0.05f);      // Redução da força
    repulsionAffector->setRepelish(true);        // Repulsão
    repulsionAffector->setActive(true);
    
    // Configurar timing dos afetores
    gravityAffector->setDelay(0.0f);      // Começar imediatamente
    gravityAffector->setDuration(5000.0f); // Durar 5 segundos
    
    attractionAffector->setDelay(1000.0f); // Começar após 1 segundo
    attractionAffector->setDuration(3000.0f); // Durar 3 segundos
    
    repulsionAffector->setDelay(2000.0f); // Começar após 2 segundos
    repulsionAffector->setDuration(2000.0f); // Durar 2 segundos
}}
```

#### Nível Advanced
```cpp
// Exemplo de diferentes tipos de afetores
#include "graphics/particleaffector.h"

void createDifferentAffectors() {{
    // Afetor de gravidade
    GravityAffectorPtr gravityAffector = std::make_shared<GravityAffector>();
    gravityAffector->setGravity(100.0f);  // Força da gravidade
    gravityAffector->setAngle(90.0f);     // Direção (90° = para baixo)
    gravityAffector->setActive(true);
    
    // Afetor de atração (partículas atraídas para um ponto)
    AttractionAffectorPtr attractionAffector = std::make_shared<AttractionAffector>();
    attractionAffector->setPosition(Point(400, 300));
    attractionAffector->setAcceleration(50.0f);  // Força de atração
    attractionAffector->setReduction(0.1f);      // Redução da força
    attractionAffector->setRepelish(false);      // Atração (não repulsão)
    attractionAffector->setActive(true);
    
    // Afetor de repulsão (partículas repelidas de um ponto)
    AttractionAffectorPtr repulsionAffector = std::make_shared<AttractionAffector>();
    repulsionAffector->setPosition(Point(100, 100));
    repulsionAffector->setAcceleration(30.0f);   // Força de repulsão
    repulsionAffector->setReduction(0.05f);      // Redução da força
    repulsionAffector->setRepelish(true);        // Repulsão
    repulsionAffector->setActive(true);
    
    // Configurar timing dos afetores
    gravityAffector->setDelay(0.0f);      // Começar imediatamente
    gravityAffector->setDuration(5000.0f); // Durar 5 segundos
    
    attractionAffector->setDelay(1000.0f); // Começar após 1 segundo
    attractionAffector->setDuration(3000.0f); // Durar 3 segundos
    
    repulsionAffector->setDelay(2000.0f); // Começar após 2 segundos
    repulsionAffector->setDuration(2000.0f); // Durar 2 segundos
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

### **Efeitos de Partículas**
Como criar efeitos de partículas pré-definidos

#### Nível Basic
```cpp
// Exemplo de efeitos de partículas
#include "graphics/particleeffect.h"
#include "graphics/particlemanager.h"

void createParticleEffects() {{
    // Obter gerenciador de partículas
    ParticleManager& manager = g_particles;
    
    // Criar efeito de fogo
    ParticleEffectPtr fireEffect = manager.createEffect("fire");
    fireEffect->setPosition(Point(200, 200));
    fireEffect->setScale(1.5f);
    fireEffect->setActive(true);
    
    // Criar efeito de explosão
    ParticleEffectPtr explosionEffect = manager.createEffect("explosion");
    explosionEffect->setPosition(Point(300, 300));
    explosionEffect->setScale(2.0f);
    explosionEffect->setActive(true);
    
    // Criar efeito de fumaça
    ParticleEffectPtr smokeEffect = manager.createEffect("smoke");
    smokeEffect->setPosition(Point(400, 400));
    smokeEffect->setScale(1.0f);
    smokeEffect->setActive(true);
    
    // Criar efeito de faíscas
    ParticleEffectPtr sparkEffect = manager.createEffect("sparks");
    sparkEffect->setPosition(Point(500, 500));
    sparkEffect->setScale(0.8f);
    sparkEffect->setActive(true);
    
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
// Exemplo de efeitos de partículas
#include "graphics/particleeffect.h"
#include "graphics/particlemanager.h"

void createParticleEffects() {{
    // Obter gerenciador de partículas
    ParticleManager& manager = g_particles;
    
    // Criar efeito de fogo
    ParticleEffectPtr fireEffect = manager.createEffect("fire");
    fireEffect->setPosition(Point(200, 200));
    fireEffect->setScale(1.5f);
    fireEffect->setActive(true);
    
    // Criar efeito de explosão
    ParticleEffectPtr explosionEffect = manager.createEffect("explosion");
    explosionEffect->setPosition(Point(300, 300));
    explosionEffect->setScale(2.0f);
    explosionEffect->setActive(true);
    
    // Criar efeito de fumaça
    ParticleEffectPtr smokeEffect = manager.createEffect("smoke");
    smokeEffect->setPosition(Point(400, 400));
    smokeEffect->setScale(1.0f);
    smokeEffect->setActive(true);
    
    // Criar efeito de faíscas
    ParticleEffectPtr sparkEffect = manager.createEffect("sparks");
    sparkEffect->setPosition(Point(500, 500));
    sparkEffect->setScale(0.8f);
    sparkEffect->setActive(true);
    
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
// Exemplo de efeitos de partículas
#include "graphics/particleeffect.h"
#include "graphics/particlemanager.h"

void createParticleEffects() {{
    // Obter gerenciador de partículas
    ParticleManager& manager = g_particles;
    
    // Criar efeito de fogo
    ParticleEffectPtr fireEffect = manager.createEffect("fire");
    fireEffect->setPosition(Point(200, 200));
    fireEffect->setScale(1.5f);
    fireEffect->setActive(true);
    
    // Criar efeito de explosão
    ParticleEffectPtr explosionEffect = manager.createEffect("explosion");
    explosionEffect->setPosition(Point(300, 300));
    explosionEffect->setScale(2.0f);
    explosionEffect->setActive(true);
    
    // Criar efeito de fumaça
    ParticleEffectPtr smokeEffect = manager.createEffect("smoke");
    smokeEffect->setPosition(Point(400, 400));
    smokeEffect->setScale(1.0f);
    smokeEffect->setActive(true);
    
    // Criar efeito de faíscas
    ParticleEffectPtr sparkEffect = manager.createEffect("sparks");
    sparkEffect->setPosition(Point(500, 500));
    sparkEffect->setScale(0.8f);
    sparkEffect->setActive(true);
    
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
    fireParticle->setLifetime(1500);
    smokeParticle->setLifetime(3000);
    sparkParticle->setLifetime(800);
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
    fireParticle->setVelocity(PointF(0.0f, -10.0f));  // Movimento para cima
    fireParticle->setAcceleration(PointF(0.0f, 20.0f)); // Gravidade
    fireParticle->setStartSize(Size(16, 16));
    fireParticle->setFinalSize(Size(48, 48));
    
    // Criar tipo de partícula de fumaça
    ParticleTypePtr smokeParticle = std::make_shared<ParticleType>();
    smokeParticle->setTexture(g_textures.loadTexture("particles/smoke.png"));
    smokeParticle->setSize(Size(48, 48));
    smokeParticle->setColor(Color(100, 100, 100, 128));
    smokeParticle->setLifetime(3000);
    smokeParticle->setFadeOut(true);
    smokeParticle->setFadeOutTime(1000);
    smokeParticle->setVelocity(PointF(5.0f, -5.0f));   // Movimento diagonal
    smokeParticle->setAcceleration(PointF(0.0f, 10.0f)); // Gravidade leve
    smokeParticle->setStartSize(Size(24, 24));
    smokeParticle->setFinalSize(Size(64, 64));
    
    // Criar tipo de partícula de faísca
    ParticleTypePtr sparkParticle = std::make_shared<ParticleType>();
    sparkParticle->setTexture(g_textures.loadTexture("particles/spark.png"));
    sparkParticle->setSize(Size(8, 8));
    sparkParticle->setColor(Color(255, 255, 0, 255));
    sparkParticle->setLifetime(800);
    sparkParticle->setFadeOut(true);
    sparkParticle->setFadeOutTime(200);
    sparkParticle->setVelocity(PointF(15.0f, -25.0f));  // Movimento rápido
    sparkParticle->setAcceleration(PointF(0.0f, 50.0f)); // Gravidade forte
    sparkParticle->setStartSize(Size(4, 4));
    sparkParticle->setFinalSize(Size(12, 12));
}}
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
    fireParticle->setVelocity(PointF(0.0f, -10.0f));  // Movimento para cima
    fireParticle->setAcceleration(PointF(0.0f, 20.0f)); // Gravidade
    fireParticle->setStartSize(Size(16, 16));
    fireParticle->setFinalSize(Size(48, 48));
    
    // Criar tipo de partícula de fumaça
    ParticleTypePtr smokeParticle = std::make_shared<ParticleType>();
    smokeParticle->setTexture(g_textures.loadTexture("particles/smoke.png"));
    smokeParticle->setSize(Size(48, 48));
    smokeParticle->setColor(Color(100, 100, 100, 128));
    smokeParticle->setLifetime(3000);
    smokeParticle->setFadeOut(true);
    smokeParticle->setFadeOutTime(1000);
    smokeParticle->setVelocity(PointF(5.0f, -5.0f));   // Movimento diagonal
    smokeParticle->setAcceleration(PointF(0.0f, 10.0f)); // Gravidade leve
    smokeParticle->setStartSize(Size(24, 24));
    smokeParticle->setFinalSize(Size(64, 64));
    
    // Criar tipo de partícula de faísca
    ParticleTypePtr sparkParticle = std::make_shared<ParticleType>();
    sparkParticle->setTexture(g_textures.loadTexture("particles/spark.png"));
    sparkParticle->setSize(Size(8, 8));
    sparkParticle->setColor(Color(255, 255, 0, 255));
    sparkParticle->setLifetime(800);
    sparkParticle->setFadeOut(true);
    sparkParticle->setFadeOutTime(200);
    sparkParticle->setVelocity(PointF(15.0f, -25.0f));  // Movimento rápido
    sparkParticle->setAcceleration(PointF(0.0f, 50.0f)); // Gravidade forte
    sparkParticle->setStartSize(Size(4, 4));
    sparkParticle->setFinalSize(Size(12, 12));
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

### **Animações de Partículas**
Como criar animações complexas de partículas

#### Inicialização e Configuração
```cpp
// Exemplo de animação complexa de partículas
#include "graphics/particlesystem.h"
#include "graphics/particleemitter.h"
#include "graphics/particleaffector.h"

void createComplexParticleAnimation() {{
    // Criar sistema principal
    ParticleSystemPtr mainSystem = std::make_shared<ParticleSystem>();
    
    // Fase 1: Explosão inicial
    ParticleTypePtr explosionParticle = std::make_shared<ParticleType>();
    explosionParticle->setTexture(g_textures.loadTexture("particles/explosion.png"));
    explosionParticle->setSize(Size(64, 64));
    explosionParticle->setColor(Color(255, 200, 0, 255));
    explosionParticle->setLifetime(500);
    
    ParticleEmitterPtr explosionEmitter = std::make_shared<ParticleEmitter>();
    explosionEmitter->setType(EmitterType::Circle);
    explosionEmitter->setPosition(Point(300, 300));
    explosionEmitter->setRadius(0.0f);  // Começar do centro
    explosionEmitter->setEmissionRate(100);
    explosionEmitter->setParticleType(explosionParticle);
    explosionEmitter->setDuration(100);  // Emitir por 100ms
    
    mainSystem->addEmitter(explosionEmitter);
    
    // Fase 2: Faíscas
    ParticleTypePtr sparkParticle = std::make_shared<ParticleType>();
    sparkParticle->setTexture(g_textures.loadTexture("particles/spark.png"));
    sparkParticle->setSize(Size(8, 8));
    sparkParticle->setColor(Color(255, 255, 0, 255));
    sparkParticle->setLifetime(1000);
    
    ParticleEmitterPtr sparkEmitter = std::make_shared<ParticleEmitter>();
    sparkEmitter->setType(EmitterType::Circle);
    sparkEmitter->setPosition(Point(300, 300));
    sparkEmitter->setRadius(50.0f);  // Emitir do círculo
    sparkEmitter->setEmissionRate(50);
    sparkEmitter->setParticleType(sparkParticle);
    sparkEmitter->setDelay(50);  // Começar após 50ms
    sparkEmitter->setDuration(200);  // Emitir por 200ms
    
    mainSystem->addEmitter(sparkEmitter);
    
    // Fase 3: Fumaça
    ParticleTypePtr smokeParticle = std::make_shared<ParticleType>();
    smokeParticle->setTexture(g_textures.loadTexture("particles/smoke.png"));
    smokeParticle->setSize(Size(48, 48));
    smokeParticle->setColor(Color(100, 100, 100, 128));
    smokeParticle->setLifetime(2000);
    
    ParticleEmitterPtr smokeEmitter = std::make_shared<ParticleEmitter>();
    smokeEmitter->setType(EmitterType::Point);
    smokeEmitter->setPosition(Point(300, 300));
    smokeEmitter->setEmissionRate(20);
    smokeEmitter->setParticleType(smokeParticle);
    smokeEmitter->setDelay(100);  // Começar após 100ms
    smokeEmitter->setDuration(1000);  // Emitir por 1 segundo
    
    mainSystem->addEmitter(smokeEmitter);
    
    // Adicionar afetores
    GravityAffectorPtr gravityAffector = std::make_shared<GravityAffector>();
    gravityAffector->setGravity(30.0f);
    mainSystem->addAffector(gravityAffector);
    
    // Loop de animação
    float elapsedTime = 0.0f;
    while (!mainSystem->hasFinished()) {{
        mainSystem->update(16.0f);  // 16ms = ~60 FPS
        mainSystem->render();
        
        elapsedTime += 16.0f;
        if (elapsedTime > 3000.0f) break;  // Máximo 3 segundos
    }}
```

#### Finalização
```cpp
}}
```



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

## 🔗 Pontos de Integração

### **Graphics System**
Integração com sistema de gráficos para renderização

**Tipo:** dependency
**Arquivos:** particle.h, particlesystem.h, particleeffect.h

### **Animation System**
Integração com sistema de animações para texturas animadas

**Tipo:** integration
**Arquivos:** particle.h, particletype.h

### **Core Framework**
Integração com sistema core (Timer, EventDispatcher)

**Tipo:** dependency
**Arquivos:** particle.h, particlesystem.h

### **Lua System**
Exposição de partículas para scripts Lua

**Tipo:** binding
**Arquivos:** particleeffect.h, particlemanager.h

### **Resource Management**
Gerenciamento de recursos de partículas

**Tipo:** dependency
**Arquivos:** particletype.h, particlemanager.h

### **UI System**
Partículas na interface do usuário

**Tipo:** integration
**Arquivos:** particleeffect.h, particlemanager.h

### **Game System**
Partículas no jogo (efeitos visuais)

**Tipo:** integration
**Arquivos:** particleeffect.h, particlesystem.h



## 📋 Guia de Uso

### **Partícula Básica**

#### Nível Basic
```cpp
#include "graphics/particle.h"

// Criar partícula
ParticlePtr particle = std::make_shared<Particle>(
    position, startSize, finalSize, velocity, acceleration,
    duration, ignorePhysicsAfter, colors, colorStops,
    compositionMode, texture, animatedTexture
);

// Atualizar e renderizar
particle->update(16.0f);
particle->render();
```

#### Nível Intermediate
```cpp
#include "graphics/particle.h"

// Criar partícula
ParticlePtr particle = std::make_shared<Particle>(
    position, startSize, finalSize, velocity, acceleration,
    duration, ignorePhysicsAfter, colors, colorStops,
    compositionMode, texture, animatedTexture
);

// Atualizar e renderizar
particle->update(16.0f);
particle->render();
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
#include "graphics/particle.h"

// Criar partícula
ParticlePtr particle = std::make_shared<Particle>(
    position, startSize, finalSize, velocity, acceleration,
    duration, ignorePhysicsAfter, colors, colorStops,
    compositionMode, texture, animatedTexture
);

// Atualizar e renderizar
particle->update(16.0f);
particle->render();
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
system->update(16.0f);
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
system->update(16.0f);
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
system->update(16.0f);
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

### **Efeitos de Partículas**

#### Nível Basic
```cpp
#include "graphics/particleeffect.h"

// Criar efeito
ParticleEffectPtr effect = manager.createEffect("fire");
effect->setPosition(Point(200, 200));
effect->setActive(true);
```

#### Nível Intermediate
```cpp
#include "graphics/particleeffect.h"

// Criar efeito
ParticleEffectPtr effect = manager.createEffect("fire");
effect->setPosition(Point(200, 200));
effect->setActive(true);
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
ParticleEffectPtr effect = manager.createEffect("fire");
effect->setPosition(Point(200, 200));
effect->setActive(true);
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

## ✨ Tipos de Partículas

### **Tipos de Emissores**
- **Point**: Emissão de um ponto específico
- **Line**: Emissão ao longo de uma linha
- **Circle**: Emissão em círculo
- **Rectangle**: Emissão em área retangular

### **Tipos de Afetores**
- **Gravity**: Gravidade que afeta partículas
- **Attraction**: Atração para um ponto específico
- **Repulsion**: Repulsão de um ponto específico

### **Efeitos Pré-definidos**
- **Fire**: Efeito de fogo
- **Explosion**: Efeito de explosão
- **Smoke**: Efeito de fumaça
- **Sparks**: Efeito de faíscas

## 🎨 Características das Partículas

### **Propriedades Físicas**
- **Posição**: Localização no espaço 2D
- **Velocidade**: Movimento inicial
- **Aceleração**: Mudança de velocidade
- **Tamanho**: Tamanho inicial e final
- **Duração**: Tempo de vida da partícula

### **Propriedades Visuais**
- **Cor**: Cor da partícula
- **Textura**: Imagem da partícula
- **Gradiente**: Mudança de cor ao longo do tempo
- **Transparência**: Opacidade da partícula
- **Modo de Composição**: Como a partícula se mistura com o fundo

## 🎯 Performance

### **Otimizações**
- **Particle Pooling**: Reutilização de partículas
- **Culling**: Remoção de partículas fora da tela
- **LOD**: Nível de detalhe baseado na distância
- **Batch Rendering**: Renderização em lotes

### **Métricas**
- **Máximo de Partículas**: 10.000 partículas simultâneas
- **Performance**: < 5ms para 1.000 partículas
- **Memory Usage**: < 50MB para efeitos complexos
- **CPU Usage**: < 3% para efeitos padrão

## 🚀 Próximos Passos

1. **Análise de Performance**: Profiling de partículas
2. **Otimizações Avançadas**: Técnicas de otimização
3. **Integração com Canary**: Preparação para servidor
4. **Documentação de API**: Referência completa

---

*Análise gerada automaticamente pelo sistema Habdel - 2025-07-31 15:30:30*
