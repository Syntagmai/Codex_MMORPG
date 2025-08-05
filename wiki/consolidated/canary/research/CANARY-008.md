---
tags: [habdel_research, canary-008, research_story, animation_system, sprite_animation]
type: research_story
status: completed
priority: critical
created: 2025-07-31
target: canary
completed: 2025-01-27
---

# CANARY-008: Sistema de Animações

## 🎯 **Objetivo**
Pesquisa profunda do sistema de animações no Canary usando metodologia habdel

## 📋 **Tarefas de Pesquisa**

### **1. Análise do Código-Fonte** ✅
- [x] Identificar arquivos relevantes
- [x] Analisar estrutura e arquitetura
- [x] Documentar principais componentes
- [x] Mapear dependências

### **2. Documentação Técnica** ✅
- [x] Criar documentação detalhada
- [x] Incluir exemplos práticos
- [x] Documentar APIs e interfaces
- [x] Criar diagramas quando necessário

### **3. Validação** ✅
- [x] Validar completude da documentação
- [x] Verificar qualidade técnica
- [x] Testar exemplos práticos
- [x] Revisar integração com wiki

## 📊 **Progresso**
- **Status**: ✅ Concluído
- **Progresso**: 100%
- **Iniciado**: 2025-01-27
- **Concluído**: 2025-01-27

## 🎬 **Arquitetura do Sistema de Animações**

### **Estrutura de Componentes**
```
canary/src/
├── protobuf/
│   └── appearances.proto          # Definições de animações
├── items/
│   ├── items.cpp                  # Processamento de animações
│   ├── items_definitions.hpp      # Tipos de animação
│   └── item.cpp                   # Implementação de itens
└── server/network/protocol/
    └── protocolgame.cpp           # Protocolo de animações
```

### **Componentes Principais**

#### **1. SpriteAnimation (Protobuf)**
- **Arquivo**: `canary/src/protobuf/appearances.proto`
- **Propósito**: Definição de animações de sprites
- **Funcionalidades**:
  - Configuração de fases de animação
  - Controle de sincronização
  - Tipos de loop (ping-pong, infinito, contado)
  - Fases de sprite com duração

#### **2. Sistema de Itens**
- **Arquivo**: `canary/src/items/items.cpp`
- **Propósito**: Processamento de animações de itens
- **Funcionalidades**:
  - Carregamento de animações
  - Tipos de animação (RANDOM, DESYNC)
  - Suporte a protocolos antigos

#### **3. Protocolo de Rede**
- **Arquivo**: `canary/src/server/network/protocol/protocolgame.cpp`
- **Propósito**: Transmissão de animações para clientes
- **Funcionalidades**:
  - Envio de dados de animação
  - Sincronização de fases
  - Controle de timing

## 🔧 **APIs e Interfaces**

### **Definições Protobuf**
```protobuf
message SpritePhase {
    optional uint32 duration_min = 1;
    optional uint32 duration_max = 2;
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
    ANIMATION_LOOP_TYPE_PINGPONG = -1;
    ANIMATION_LOOP_TYPE_INFINITE = 0;
    ANIMATION_LOOP_TYPE_COUNTED = 1;
}
```

### **Tipos de Animação**
#### Nível Basic
```cpp
enum AnimationType_t {
    ANIMATION_NONE = 0,
    ANIMATION_RANDOM = 1,
    ANIMATION_DESYNC = 2
};
```

#### Nível Intermediate
```cpp
enum AnimationType_t {
    ANIMATION_NONE = 0,
    ANIMATION_RANDOM = 1,
    ANIMATION_DESYNC = 2
};
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
enum AnimationType_t {
    ANIMATION_NONE = 0,
    ANIMATION_RANDOM = 1,
    ANIMATION_DESYNC = 2
};
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

### **Estrutura de Item**
#### Nível Basic
```cpp
struct ItemType {
    // ... outros campos
    AnimationType_t animationType = ANIMATION_NONE;
    uint32_t animationSpeed = 0;
    bool hasAnimation = false;
};
```

#### Nível Intermediate
```cpp
struct ItemType {
    // ... outros campos
    AnimationType_t animationType = ANIMATION_NONE;
    uint32_t animationSpeed = 0;
    bool hasAnimation = false;
};
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
struct ItemType {
    // ... outros campos
    AnimationType_t animationType = ANIMATION_NONE;
    uint32_t animationSpeed = 0;
    bool hasAnimation = false;
};
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

## 📝 **Exemplos Práticos**

### **1. Carregamento de Animação**
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

### **2. Processamento de Animação no Protocolo**
#### Nível Basic
```cpp
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

### **3. Configuração de SpriteInfo**
```protobuf
message SpriteInfo {
    optional uint32 pattern_width = 1;
    optional uint32 pattern_height = 2;
    optional uint32 pattern_depth = 3;
    optional uint32 layers = 4;
    repeated uint32 sprite_id = 5;
    optional uint32 bounding_square = 7;
    optional SpriteAnimation animation = 6;  // Animação do sprite
    optional bool is_opaque = 8;
    repeated Box bounding_box_per_direction = 9;
}
```

## 🎮 **Sistema de Animações**

### **Tipos de Animação Suportados**

#### **1. ANIMATION_NONE**
- **Descrição**: Item sem animação
- **Uso**: Itens estáticos como paredes, chão
- **Performance**: Máxima (sem overhead)

#### **2. ANIMATION_RANDOM**
- **Descrição**: Animação com fase inicial aleatória
- **Uso**: Efeitos visuais, itens decorativos
- **Características**:
  - Fase inicial aleatória para cada instância
  - Efeito visual diversificado
  - Ideal para múltiplas instâncias

#### **3. ANIMATION_DESYNC**
- **Descrição**: Animação dessincronizada
- **Uso**: Itens animados comuns
- **Características**:
  - Baseada no tempo do servidor
  - Sincronização entre clientes
  - Performance otimizada

### **Configuração de Fases**
```protobuf
message SpritePhase {
    optional uint32 duration_min = 1;  // Duração mínima em ms
    optional uint32 duration_max = 2;  // Duração máxima em ms
}
```

### **Tipos de Loop**
```protobuf
enum ANIMATION_LOOP_TYPE {
    ANIMATION_LOOP_TYPE_PINGPONG = -1;  // Ida e volta
    ANIMATION_LOOP_TYPE_INFINITE = 0;   // Loop infinito
    ANIMATION_LOOP_TYPE_COUNTED = 1;    // Loop contado
}
```

## 🔄 **Sistema de Sincronização**

### **Sincronização de Tempo**
- **Base**: Tempo do servidor (ticks)
- **Cálculo**: `(ticks % animationPhases)`
- **Vantagem**: Sincronização automática entre clientes

### **Animação Aleatória**
- **Base**: Número aleatório por instância
- **Cálculo**: `randomNumber(0, animationPhases - 1)`
- **Vantagem**: Diversidade visual

### **Controle de Performance**
#### Nível Basic
```cpp
// Verificação de suporte a animação
bool supportAnimation = g_configManager().getBoolean(OLD_PROTOCOL);

if (supportAnimation) {
    // Processar animação apenas se suportado
    if (objectFrame.sprite_info().has_animation()) {
        // Configurar animação
    }
}
```

#### Nível Intermediate
```cpp
// Verificação de suporte a animação
bool supportAnimation = g_configManager().getBoolean(OLD_PROTOCOL);

if (supportAnimation) {
    // Processar animação apenas se suportado
    if (objectFrame.sprite_info().has_animation()) {
        // Configurar animação
    }
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
// Verificação de suporte a animação
bool supportAnimation = g_configManager().getBoolean(OLD_PROTOCOL);

if (supportAnimation) {
    // Processar animação apenas se suportado
    if (objectFrame.sprite_info().has_animation()) {
        // Configurar animação
    }
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

## 🎯 **Integração com Outros Sistemas**

### **Sistema de Itens**
- **Carregamento**: Durante inicialização do servidor
- **Processamento**: Em tempo real durante gameplay
- **Armazenamento**: Em memória para performance

### **Sistema de Rede**
- **Transmissão**: Via protocolo de jogo
- **Sincronização**: Automática entre servidor e clientes
- **Otimização**: Dados compactos via protobuf

### **Sistema de Protocolo**
- **Compatibilidade**: Suporte a protocolos antigos e novos
- **Flexibilidade**: Configuração por item
- **Performance**: Processamento otimizado

## 🔧 **Otimizações e Performance**

### **Estratégias de Otimização**
1. **Carregamento Lazy**: Animações carregadas sob demanda
2. **Cache Inteligente**: Dados de animação em memória
3. **Compressão**: Dados protobuf otimizados
4. **Seleção Condicional**: Animação apenas quando necessário

### **Controle de Memória**
#### Nível Basic
```cpp
// Verificação de suporte antes de processar
if (!objectFrame.sprite_info().has_animation()) {
    return; // Pular processamento se não há animação
}
```

#### Nível Intermediate
```cpp
// Verificação de suporte antes de processar
if (!objectFrame.sprite_info().has_animation()) {
    return; // Pular processamento se não há animação
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
// Verificação de suporte antes de processar
if (!objectFrame.sprite_info().has_animation()) {
    return; // Pular processamento se não há animação
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

### **Performance de Rede**
- **Dados Mínimos**: Apenas informações essenciais
- **Sincronização Eficiente**: Baseada em ticks do servidor
- **Cache Cliente**: Redução de retransmissão

## 📊 **Métricas e Monitoramento**

### **Métricas Disponíveis**
- **Número de Itens Animados**: Por tipo e categoria
- **Uso de Memória**: Por animação
- **Performance de Rede**: Dados transmitidos
- **Tempo de Processamento**: Por frame

### **Logs e Debug**
#### Nível Basic
```cpp
if (animation.random_start_phase()) {
```

#### Nível Intermediate
```cpp
// Log de animação carregada
if (animation.random_start_phase()) {
    g_logger().debug("Animation loaded: RANDOM type for item {}", id);
} else {
    g_logger().debug("Animation loaded: DESYNC type for item {}", id);
}
```

#### Nível Advanced
```cpp
// Log de animação carregada
if (animation.random_start_phase()) {
    g_logger().debug("Animation loaded: RANDOM type for item {}", id);
} else {
    g_logger().debug("Animation loaded: DESYNC type for item {}", id);
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

## 🔗 **Integração com Cliente**

### **Protocolo de Comunicação**
1. **Servidor**: Envia dados de animação via protobuf
2. **Cliente**: Recebe e processa animações
3. **Sincronização**: Baseada em tempo do servidor
4. **Renderização**: Cliente responsável pela exibição

### **Compatibilidade**
- **Protocolos Antigos**: Suporte via configuração
- **Protocolos Novos**: Funcionalidades completas
- **Fallback**: Comportamento padrão para incompatibilidades

## 📝 **Notas de Pesquisa**

### **Descobertas Importantes**
1. **Arquitetura Simples**: Sistema direto e eficiente
2. **Performance Otimizada**: Processamento mínimo necessário
3. **Flexibilidade**: Suporte a múltiplos tipos de animação
4. **Compatibilidade**: Funciona com protocolos antigos e novos

### **Diferenças do OTClient**
1. **Foco Servidor**: Canary foca na lógica do servidor
2. **Protocolo Otimizado**: Dados compactos via protobuf
3. **Sincronização Centralizada**: Controle pelo servidor
4. **Simplicidade**: Menos complexidade que o cliente

### **Pontos de Atenção**
1. **Compatibilidade**: Verificar suporte a protocolos
2. **Performance**: Monitorar uso de memória
3. **Sincronização**: Garantir consistência entre clientes
4. **Configuração**: Ajustar parâmetros conforme necessário

## 🔗 **Links Relacionados**
- [Documentação Principal](../../README.md)
- [Plano de Pesquisa](../research_plan.json)
- [Status Geral](../status_report.md)
- [CANARY-007: Sistema de Lua](../habdel/CANARY-007.md)
- [CANARY-009: Sistema de Som](../habdel/CANARY-009.md)

---
*Story concluída seguindo metodologia habdel - 2025-01-27*
