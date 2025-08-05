---
tags: [lesson, canary, CANARY, CANARY-008, animation_system, sprite_animation]
type: lesson
status: completed
priority: high
created: 2025-07-29T01:04:09.668291
lesson_id: CANARY-008
course_id: CANARY
duration: 3 horas
difficulty: medium
aliases: [Animation System, Sistema de Animações, Lição CANARY-008]
---

# Sistema de Animações

Sistema de animações de sprites no Canary

## 🎯 Objetivos da Lição

- Compreender a arquitetura do sistema de animações no Canary
- Aplicar conceitos de animação de sprites em prática
- Desenvolver habilidades de configuração de animações
- Preparar-se para próximas lições

## 📚 Conteúdo

## Teoria

### Sistema de Animações
O sistema de animações no Canary é responsável por gerenciar animações de sprites de itens, oferecendo:

- **Tipos de Animação**: NONE, RANDOM, DESYNC
- **Sincronização**: Baseada no tempo do servidor
- **Performance**: Otimizada para servidores MMORPG
- **Compatibilidade**: Suporte a protocolos antigos e novos

### Conceitos Fundamentais

#### 1. SpriteAnimation (Protobuf)
- **Propósito**: Definição de animações de sprites
- **Funcionalidades**:
  - Configuração de fases de animação
  - Controle de sincronização
  - Tipos de loop (ping-pong, infinito, contado)
  - Fases de sprite com duração

#### 2. Sistema de Itens
- **Propósito**: Processamento de animações de itens
- **Funcionalidades**:
  - Carregamento de animações
  - Tipos de animação (RANDOM, DESYNC)
  - Suporte a protocolos antigos

#### 3. Protocolo de Rede
- **Propósito**: Transmissão de animações para clientes
- **Funcionalidades**:
  - Envio de dados de animação
  - Sincronização de fases
  - Controle de timing

## Prática

### Exemplo Básico - Definição de Animação
```protobuf
message SpritePhase {
    optional uint32 duration_min = 1;  // Duração mínima em ms
    optional uint32 duration_max = 2;  // Duração máxima em ms
}

message SpriteAnimation {
    optional uint32 default_start_phase = 1;
    optional bool synchronized = 2;
    optional bool random_start_phase = 3;
    optional ANIMATION_LOOP_TYPE loop_type = 4;
    optional uint32 loop_count = 5;
    repeated SpritePhase sprite_phase = 6;
}

enum ANIMATION_LOOP_TYPE {
    ANIMATION_LOOP_TYPE_PINGPONG = -1;  // Ida e volta
    ANIMATION_LOOP_TYPE_INFINITE = 0;   // Loop infinito
    ANIMATION_LOOP_TYPE_COUNTED = 1;    // Loop contado
}
```

### Exemplo Avançado - Carregamento de Animação
#### Nível Basic
```cpp
// Carregamento de animação de item
bool Items::parseItemNode(const pugi::xml_node& itemNode, uint16_t id) {
    // ... código existente
    
    if (objectFrame.sprite_info().has_animation()) {
        const auto& animation = objectFrame.sprite_info().animation();
        
        if (animation.random_start_phase()) {
            iType.animationType = ANIMATION_RANDOM;
        } else {
            iType.animationType = ANIMATION_DESYNC;
        }
        
        iType.hasAnimation = true;
        iType.animationSpeed = animation.sprite_phase(0).duration_min();
    }
    
    return true;
}

// Envio de animação para cliente
void ProtocolGame::sendAddItem(const Position& pos, uint32_t stackpos, const Item* item) {
    // ... código existente
    
    if (it.animationType == ANIMATION_RANDOM) {
        // Animação com fase inicial aleatória
        msg.add<uint8_t>(randomNumber(0, it.animationPhases - 1));
    } else if (it.animationType == ANIMATION_DESYNC) {
        // Animação dessincronizada
        msg.add<uint8_t>((ticks % it.animationPhases));
    }
    
    // ... resto do código
}
```

#### Nível Intermediate
```cpp
// Carregamento de animação de item
bool Items::parseItemNode(const pugi::xml_node& itemNode, uint16_t id) {
    // ... código existente
    
    if (objectFrame.sprite_info().has_animation()) {
        const auto& animation = objectFrame.sprite_info().animation();
        
        if (animation.random_start_phase()) {
            iType.animationType = ANIMATION_RANDOM;
        } else {
            iType.animationType = ANIMATION_DESYNC;
        }
        
        iType.hasAnimation = true;
        iType.animationSpeed = animation.sprite_phase(0).duration_min();
    }
    
    return true;
}

// Envio de animação para cliente
void ProtocolGame::sendAddItem(const Position& pos, uint32_t stackpos, const Item* item) {
    // ... código existente
    
    if (it.animationType == ANIMATION_RANDOM) {
        // Animação com fase inicial aleatória
        msg.add<uint8_t>(randomNumber(0, it.animationPhases - 1));
    } else if (it.animationType == ANIMATION_DESYNC) {
        // Animação dessincronizada
        msg.add<uint8_t>((ticks % it.animationPhases));
    }
    
    // ... resto do código
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
// Carregamento de animação de item
bool Items::parseItemNode(const pugi::xml_node& itemNode, uint16_t id) {
    // ... código existente
    
    if (objectFrame.sprite_info().has_animation()) {
        const auto& animation = objectFrame.sprite_info().animation();
        
        if (animation.random_start_phase()) {
            iType.animationType = ANIMATION_RANDOM;
        } else {
            iType.animationType = ANIMATION_DESYNC;
        }
        
        iType.hasAnimation = true;
        iType.animationSpeed = animation.sprite_phase(0).duration_min();
    }
    
    return true;
}

// Envio de animação para cliente
void ProtocolGame::sendAddItem(const Position& pos, uint32_t stackpos, const Item* item) {
    // ... código existente
    
    if (it.animationType == ANIMATION_RANDOM) {
        // Animação com fase inicial aleatória
        msg.add<uint8_t>(randomNumber(0, it.animationPhases - 1));
    } else if (it.animationType == ANIMATION_DESYNC) {
        // Animação dessincronizada
        msg.add<uint8_t>((ticks % it.animationPhases));
    }
    
    // ... resto do código
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

## 💡 Conceitos-Chave

**SpriteAnimation**: Definição de animações de sprites
**AnimationType**: Tipos de animação (NONE, RANDOM, DESYNC)
**Sincronização**: Controle de tempo baseado no servidor
**Protobuf**: Formato de dados otimizado
**Performance**: Otimizações para servidores MMORPG

## 🧪 Exercícios

### Exercício 1: Básico
Criar uma definição de animação simples para um item decorativo.

```protobuf
message SpriteAnimation {
    optional uint32 default_start_phase = 1;
    optional bool synchronized = true;
    optional bool random_start_phase = false;
    optional ANIMATION_LOOP_TYPE loop_type = ANIMATION_LOOP_TYPE_INFINITE;
    optional uint32 loop_count = 0;
    repeated SpritePhase sprite_phase = {
        { duration_min: 1000, duration_max: 1000 },
        { duration_min: 1000, duration_max: 1000 },
        { duration_min: 1000, duration_max: 1000 }
    };
}
```

### Exercício 2: Intermediário
Implementar carregamento de animação com verificação de suporte.

#### Nível Basic
```cpp
bool Items::loadAnimation(const pugi::xml_node& animationNode, ItemType& itemType) {
    // Verificar suporte a animação
    bool supportAnimation = g_configManager().getBoolean(OLD_PROTOCOL);
    
    if (!supportAnimation) {
        return false;
    }
    
    if (animationNode.attribute("random_start_phase").as_bool()) {
        itemType.animationType = ANIMATION_RANDOM;
    } else {
        itemType.animationType = ANIMATION_DESYNC;
    }
    
    itemType.hasAnimation = true;
    itemType.animationSpeed = animationNode.attribute("speed").as_uint();
    
    return true;
}
```

#### Nível Intermediate
```cpp
bool Items::loadAnimation(const pugi::xml_node& animationNode, ItemType& itemType) {
    // Verificar suporte a animação
    bool supportAnimation = g_configManager().getBoolean(OLD_PROTOCOL);
    
    if (!supportAnimation) {
        return false;
    }
    
    if (animationNode.attribute("random_start_phase").as_bool()) {
        itemType.animationType = ANIMATION_RANDOM;
    } else {
        itemType.animationType = ANIMATION_DESYNC;
    }
    
    itemType.hasAnimation = true;
    itemType.animationSpeed = animationNode.attribute("speed").as_uint();
    
    return true;
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
bool Items::loadAnimation(const pugi::xml_node& animationNode, ItemType& itemType) {
    // Verificar suporte a animação
    bool supportAnimation = g_configManager().getBoolean(OLD_PROTOCOL);
    
    if (!supportAnimation) {
        return false;
    }
    
    if (animationNode.attribute("random_start_phase").as_bool()) {
        itemType.animationType = ANIMATION_RANDOM;
    } else {
        itemType.animationType = ANIMATION_DESYNC;
    }
    
    itemType.hasAnimation = true;
    itemType.animationSpeed = animationNode.attribute("speed").as_uint();
    
    return true;
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

### Exercício 3: Avançado
Criar sistema de animação com múltiplas fases e controle de loop.

```cpp
class AnimationManager {
    -- Classe: AnimationManager
private:
    struct AnimationData {
        AnimationType_t type;
        uint32_t phases;
        uint32_t speed;
        ANIMATION_LOOP_TYPE loopType;
        uint32_t loopCount;
    };
    
    std::unordered_map<uint16_t, AnimationData> animations;
    
public:
    bool registerAnimation(uint16_t itemId, const AnimationData& data) {
        animations[itemId] = data;
        return true;
    }
    
    uint8_t getAnimationPhase(uint16_t itemId, uint32_t ticks) {
        auto it = animations.find(itemId);
        if (it == animations.end()) {
            return 0;
        }
        
        const auto& anim = it->second;
        
        switch (anim.type) {
            case ANIMATION_RANDOM:
                return randomNumber(0, anim.phases - 1);
            case ANIMATION_DESYNC:
                return (ticks % anim.phases);
            default:
                return 0;
        }
    }
};
```

## 📝 Resumo

## Pontos Principais

- **Arquitetura Simples**: Sistema direto e eficiente
- **Performance Otimizada**: Processamento mínimo necessário
- **Flexibilidade**: Suporte a múltiplos tipos de animação
- **Compatibilidade**: Funciona com protocolos antigos e novos
- **Sincronização**: Controle centralizado pelo servidor

## Aplicação
- **Itens Decorativos**: Animações para decoração
- **Efeitos Visuais**: Animações de efeitos especiais
- **Interface**: Animações de elementos da UI
- **Gameplay**: Animações de itens interativos

## Benefícios
- **Performance**: Sistema otimizado para servidores
- **Flexibilidade**: Múltiplos tipos de animação
- **Compatibilidade**: Suporte a diferentes protocolos
- **Manutenibilidade**: Código limpo e bem estruturado

## Próximos Passos
- Estudar sistema de som
- Aprender sobre partículas
- Explorar integração com outros sistemas
- Praticar configuração de animações complexas

## 🔗 **Links Automáticos**

> [!info] **Links Gerados Automaticamente**
> Estes links foram criados automaticamente pelo sistema de linkagem da categoria **Documentation**

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]

### **🧭 Navegação**
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]
- [[../maps/category_indices|Índices por Categoria]]
- [[../maps/relationships|Relacionamentos]]

### **📊 Métricas da Categoria**
- **Categoria**: Documentation
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

## 🔗 Próxima Lição

[[CANARY-009_sound_system]] - Sistema de Som

---

**Duração**: 3 horas  
**Dificuldade**: medium  
**Status**: completed 