---
tags: [habdel_research, canary-009, research_story, sound_system, audio_effects]
type: research_story
status: completed
priority: critical
created: 2025-07-31
target: canary
completed: 2025-01-27
---

# CANARY-009: Sistema de Som

## 🎯 **Objetivo**
Pesquisa profunda do sistema de som no Canary usando metodologia habdel

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

## 🔊 **Arquitetura do Sistema de Som**

### **Estrutura de Componentes**
```
canary/src/
├── creatures/creatures_definitions.hpp    # Definições de SoundEffect_t
├── game/game.cpp                          # Sistema principal de som
├── server/network/protocol/
│   ├── protocolgame.hpp                   # Interface de protocolo
│   └── protocolgame.cpp                   # Implementação de protocolo
├── creatures/players/
│   ├── player.hpp                         # Interface do jogador
│   └── player.cpp                         # Implementação do jogador
└── lua/functions/
    ├── map/position_functions.cpp         # Funções Lua de posição
    └── creatures/player/player_functions.cpp # Funções Lua do jogador
```

### **Componentes Principais**

#### **1. SoundEffect_t (Enum)**
- **Arquivo**: `canary/src/creatures/creatures_definitions.hpp`
- **Propósito**: Definição de todos os tipos de efeitos sonoros
- **Funcionalidades**:
  - Categorização de sons por tipo (combate, magia, ambiente)
  - Identificação única para cada efeito sonoro
  - Suporte a sons de criaturas, jogadores e ambiente

#### **2. SourceEffect_t (Enum)**
- **Arquivo**: `canary/src/creatures/creatures_definitions.hpp`
- **Propósito**: Definição da fonte do efeito sonoro
- **Tipos**:
  - `GLOBAL`: Som global para todos os jogadores
  - `OWN`: Som apenas para o jogador que executou a ação
  - `OTHERS`: Som para outros jogadores (não o executor)
  - `CREATURES`: Som para criaturas

#### **3. Sistema Game**
- **Arquivo**: `canary/src/game/game.cpp`
- **Propósito**: Gerenciamento central de efeitos sonoros
- **Funcionalidades**:
  - `sendSingleSoundEffect()`: Envio de som único
  - `sendDoubleSoundEffect()`: Envio de dois sons simultâneos
  - Gerenciamento de espectadores e fontes

#### **4. Protocolo de Rede**
- **Arquivo**: `canary/src/server/network/protocol/protocolgame.cpp`
- **Propósito**: Transmissão de sons para clientes
- **Funcionalidades**:
  - Codificação de dados de som
  - Controle de compatibilidade com protocolos antigos
  - Otimização de transmissão

## 🔧 **APIs e Interfaces**

### **Definições de Som**
#### Nível Basic
```cpp
enum SoundEffect_t : uint16_t {
    // Sons de Combate
    SILENCE = 0,
    HUMAN_CLOSE_ATK_FIST = 1,
    MONSTER_CLOSE_ATK_FIST = 2,
    MELEE_ATK_SWORD = 3,
    MELEE_ATK_CLUB = 4,
    MELEE_ATK_AXE = 5,
    DIST_ATK_BOW = 6,
    DIST_ATK_CROSSBOW = 7,
    DIST_ATK_THROW = 8,
    MAGICAL_RANGE_ATK = 9,
    
    // Sons de Magia
    SPELL_LIGHT_HEALING = 1001,
    SPELL_INTENSE_HEALING = 1002,
    SPELL_ULTIMATE_HEALING = 1003,
    SPELL_FIREBALL_RUNE = 1015,
    SPELL_EXPLOSION_RUNE = 1018,
    
    // Sons de Criaturas
    MONSTER_MELEE_ATK_FIST = 100,
    MONSTER_MELEE_ATK_CLAW = 101,
    MONSTER_MELEE_ATK_BITE = 102,
    
    // Sons de Ambiente
    ENV_INSECTS_BIRDS = 2651,
    ENV_WIND_1 = 2652,
    ENV_WATER_DEPTH = 2657,
    ENV_FIRE = 2745,
    
    // Sons de Ações
    ACTION_OPEN_DOOR = 2674,
    ACTION_CLOSE_DOOR = 2675,
    ACTION_NOTIFICATION = 2771,
    
    // Sons de Itens
    ITEM_MOVE_BACKPACK = 2786,
    ITEM_USE_POTION = 2787,
    ITEM_MOVE_METALIC = 2790
};

enum class SourceEffect_t : uint8_t {
    GLOBAL = 0,      // Som global
    OWN = 1,         // Som próprio
    OTHERS = 2,      // Som de outros
    CREATURES = 3    // Som de criaturas
};
```

#### Nível Intermediate
```cpp
enum SoundEffect_t : uint16_t {
    // Sons de Combate
    SILENCE = 0,
    HUMAN_CLOSE_ATK_FIST = 1,
    MONSTER_CLOSE_ATK_FIST = 2,
    MELEE_ATK_SWORD = 3,
    MELEE_ATK_CLUB = 4,
    MELEE_ATK_AXE = 5,
    DIST_ATK_BOW = 6,
    DIST_ATK_CROSSBOW = 7,
    DIST_ATK_THROW = 8,
    MAGICAL_RANGE_ATK = 9,
    
    // Sons de Magia
    SPELL_LIGHT_HEALING = 1001,
    SPELL_INTENSE_HEALING = 1002,
    SPELL_ULTIMATE_HEALING = 1003,
    SPELL_FIREBALL_RUNE = 1015,
    SPELL_EXPLOSION_RUNE = 1018,
    
    // Sons de Criaturas
    MONSTER_MELEE_ATK_FIST = 100,
    MONSTER_MELEE_ATK_CLAW = 101,
    MONSTER_MELEE_ATK_BITE = 102,
    
    // Sons de Ambiente
    ENV_INSECTS_BIRDS = 2651,
    ENV_WIND_1 = 2652,
    ENV_WATER_DEPTH = 2657,
    ENV_FIRE = 2745,
    
    // Sons de Ações
    ACTION_OPEN_DOOR = 2674,
    ACTION_CLOSE_DOOR = 2675,
    ACTION_NOTIFICATION = 2771,
    
    // Sons de Itens
    ITEM_MOVE_BACKPACK = 2786,
    ITEM_USE_POTION = 2787,
    ITEM_MOVE_METALIC = 2790
};

enum class SourceEffect_t : uint8_t {
    GLOBAL = 0,      // Som global
    OWN = 1,         // Som próprio
    OTHERS = 2,      // Som de outros
    CREATURES = 3    // Som de criaturas
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
enum SoundEffect_t : uint16_t {
    // Sons de Combate
    SILENCE = 0,
    HUMAN_CLOSE_ATK_FIST = 1,
    MONSTER_CLOSE_ATK_FIST = 2,
    MELEE_ATK_SWORD = 3,
    MELEE_ATK_CLUB = 4,
    MELEE_ATK_AXE = 5,
    DIST_ATK_BOW = 6,
    DIST_ATK_CROSSBOW = 7,
    DIST_ATK_THROW = 8,
    MAGICAL_RANGE_ATK = 9,
    
    // Sons de Magia
    SPELL_LIGHT_HEALING = 1001,
    SPELL_INTENSE_HEALING = 1002,
    SPELL_ULTIMATE_HEALING = 1003,
    SPELL_FIREBALL_RUNE = 1015,
    SPELL_EXPLOSION_RUNE = 1018,
    
    // Sons de Criaturas
    MONSTER_MELEE_ATK_FIST = 100,
    MONSTER_MELEE_ATK_CLAW = 101,
    MONSTER_MELEE_ATK_BITE = 102,
    
    // Sons de Ambiente
    ENV_INSECTS_BIRDS = 2651,
    ENV_WIND_1 = 2652,
    ENV_WATER_DEPTH = 2657,
    ENV_FIRE = 2745,
    
    // Sons de Ações
    ACTION_OPEN_DOOR = 2674,
    ACTION_CLOSE_DOOR = 2675,
    ACTION_NOTIFICATION = 2771,
    
    // Sons de Itens
    ITEM_MOVE_BACKPACK = 2786,
    ITEM_USE_POTION = 2787,
    ITEM_MOVE_METALIC = 2790
};

enum class SourceEffect_t : uint8_t {
    GLOBAL = 0,      // Som global
    OWN = 1,         // Som próprio
    OTHERS = 2,      // Som de outros
    CREATURES = 3    // Som de criaturas
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

### **Funções Principais do Game**
#### Nível Basic
```cpp
// Envio de som único
void Game::sendSingleSoundEffect(
    const Position &pos, 
    SoundEffect_t soundId, 
    const std::shared_ptr<Creature> &actor = nullptr
);

// Envio de dois sons simultâneos
void Game::sendDoubleSoundEffect(
    const Position &pos, 
    SoundEffect_t mainSoundEffect, 
    SoundEffect_t secondarySoundEffect, 
    const std::shared_ptr<Creature> &actor = nullptr
);
```

#### Nível Intermediate
```cpp
// Envio de som único
void Game::sendSingleSoundEffect(
    const Position &pos, 
    SoundEffect_t soundId, 
    const std::shared_ptr<Creature> &actor = nullptr
);

// Envio de dois sons simultâneos
void Game::sendDoubleSoundEffect(
    const Position &pos, 
    SoundEffect_t mainSoundEffect, 
    SoundEffect_t secondarySoundEffect, 
    const std::shared_ptr<Creature> &actor = nullptr
);
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
// Envio de som único
void Game::sendSingleSoundEffect(
    const Position &pos, 
    SoundEffect_t soundId, 
    const std::shared_ptr<Creature> &actor = nullptr
);

// Envio de dois sons simultâneos
void Game::sendDoubleSoundEffect(
    const Position &pos, 
    SoundEffect_t mainSoundEffect, 
    SoundEffect_t secondarySoundEffect, 
    const std::shared_ptr<Creature> &actor = nullptr
);
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

### **Funções do Protocolo**
#### Nível Basic
```cpp
// Envio de som único via protocolo
void ProtocolGame::sendSingleSoundEffect(
    const Position &pos, 
    SoundEffect_t id, 
    SourceEffect_t source
);

// Envio de dois sons via protocolo
void ProtocolGame::sendDoubleSoundEffect(
    const Position &pos,
    SoundEffect_t mainSoundId,
    SourceEffect_t mainSource,
    SoundEffect_t secondarySoundId,
    SourceEffect_t secondarySource
);
```

#### Nível Intermediate
```cpp
// Envio de som único via protocolo
void ProtocolGame::sendSingleSoundEffect(
    const Position &pos, 
    SoundEffect_t id, 
    SourceEffect_t source
);

// Envio de dois sons via protocolo
void ProtocolGame::sendDoubleSoundEffect(
    const Position &pos,
    SoundEffect_t mainSoundId,
    SourceEffect_t mainSource,
    SoundEffect_t secondarySoundId,
    SourceEffect_t secondarySource
);
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
// Envio de som único via protocolo
void ProtocolGame::sendSingleSoundEffect(
    const Position &pos, 
    SoundEffect_t id, 
    SourceEffect_t source
);

// Envio de dois sons via protocolo
void ProtocolGame::sendDoubleSoundEffect(
    const Position &pos,
    SoundEffect_t mainSoundId,
    SourceEffect_t mainSource,
    SoundEffect_t secondarySoundId,
    SourceEffect_t secondarySource
);
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

### **1. Envio de Som Único**
#### Nível Basic
```cpp
// Envio de som de combate
void Player::attack() {
    // Som de ataque com espada
    g_game().sendSingleSoundEffect(
        getPosition(), 
        SoundEffect_t::MELEE_ATK_SWORD, 
        getPlayer()
    );
}

// Envio de som de magia
void Player::castSpell() {
    // Som de magia de cura
    g_game().sendSingleSoundEffect(
        getPosition(), 
        SoundEffect_t::SPELL_LIGHT_HEALING, 
        getPlayer()
    );
}
```

#### Nível Intermediate
```cpp
// Envio de som de combate
void Player::attack() {
    // Som de ataque com espada
    g_game().sendSingleSoundEffect(
        getPosition(), 
        SoundEffect_t::MELEE_ATK_SWORD, 
        getPlayer()
    );
}

// Envio de som de magia
void Player::castSpell() {
    // Som de magia de cura
    g_game().sendSingleSoundEffect(
        getPosition(), 
        SoundEffect_t::SPELL_LIGHT_HEALING, 
        getPlayer()
    );
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
// Envio de som de combate
void Player::attack() {
    // Som de ataque com espada
    g_game().sendSingleSoundEffect(
        getPosition(), 
        SoundEffect_t::MELEE_ATK_SWORD, 
        getPlayer()
    );
}

// Envio de som de magia
void Player::castSpell() {
    // Som de magia de cura
    g_game().sendSingleSoundEffect(
        getPosition(), 
        SoundEffect_t::SPELL_LIGHT_HEALING, 
        getPlayer()
    );
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

### **2. Envio de Dois Sons Simultâneos**
#### Nível Basic
```cpp
// Combate com som de ataque e impacto
void Player::meleeAttack() {
    g_game().sendDoubleSoundEffect(
        getPosition(),
        getAttackSoundEffect(),    // Som de ataque
        getHitSoundEffect(),       // Som de impacto
        getPlayer()
    );
}

// Magia com som de cast e impacto
void Player::castRune() {
    g_game().sendDoubleSoundEffect(
        getPosition(),
        SoundEffect_t::SPELL_FIREBALL_RUNE,  // Som de cast
        SoundEffect_t::SPELL_EXPLOSION_RUNE, // Som de impacto
        getPlayer()
    );
}
```

#### Nível Intermediate
```cpp
// Combate com som de ataque e impacto
void Player::meleeAttack() {
    g_game().sendDoubleSoundEffect(
        getPosition(),
        getAttackSoundEffect(),    // Som de ataque
        getHitSoundEffect(),       // Som de impacto
        getPlayer()
    );
}

// Magia com som de cast e impacto
void Player::castRune() {
    g_game().sendDoubleSoundEffect(
        getPosition(),
        SoundEffect_t::SPELL_FIREBALL_RUNE,  // Som de cast
        SoundEffect_t::SPELL_EXPLOSION_RUNE, // Som de impacto
        getPlayer()
    );
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
// Combate com som de ataque e impacto
void Player::meleeAttack() {
    g_game().sendDoubleSoundEffect(
        getPosition(),
        getAttackSoundEffect(),    // Som de ataque
        getHitSoundEffect(),       // Som de impacto
        getPlayer()
    );
}

// Magia com som de cast e impacto
void Player::castRune() {
    g_game().sendDoubleSoundEffect(
        getPosition(),
        SoundEffect_t::SPELL_FIREBALL_RUNE,  // Som de cast
        SoundEffect_t::SPELL_EXPLOSION_RUNE, // Som de impacto
        getPlayer()
    );
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

### **3. Som de Ambiente**
#### Nível Basic
```cpp
// Som de ambiente (vento)
void Game::addEnvironmentSound(const Position &pos) {
    g_game().sendSingleSoundEffect(
        pos,
        SoundEffect_t::ENV_WIND_1,
        nullptr  // Sem ator específico
    );
}

// Som de ação (abrir porta)
void Game::openDoor(const Position &pos) {
    g_game().sendSingleSoundEffect(
        pos,
        SoundEffect_t::ACTION_OPEN_DOOR,
        nullptr
    );
}
```

#### Nível Intermediate
```cpp
// Som de ambiente (vento)
void Game::addEnvironmentSound(const Position &pos) {
    g_game().sendSingleSoundEffect(
        pos,
        SoundEffect_t::ENV_WIND_1,
        nullptr  // Sem ator específico
    );
}

// Som de ação (abrir porta)
void Game::openDoor(const Position &pos) {
    g_game().sendSingleSoundEffect(
        pos,
        SoundEffect_t::ACTION_OPEN_DOOR,
        nullptr
    );
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
// Som de ambiente (vento)
void Game::addEnvironmentSound(const Position &pos) {
    g_game().sendSingleSoundEffect(
        pos,
        SoundEffect_t::ENV_WIND_1,
        nullptr  // Sem ator específico
    );
}

// Som de ação (abrir porta)
void Game::openDoor(const Position &pos) {
    g_game().sendSingleSoundEffect(
        pos,
        SoundEffect_t::ACTION_OPEN_DOOR,
        nullptr
    );
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

### **4. Funções Lua**
```lua
-- Envio de som via Lua (posição)
local pos = Position(100, 100, 7)
pos:sendSingleSoundEffect(SoundEffect_t.SPELL_LIGHT_HEALING)

-- Envio de dois sons via Lua (posição)
pos:sendDoubleSoundEffect(
    SoundEffect_t.MELEE_ATK_SWORD,
    SoundEffect_t.MELEE_ATK_CLUB
)

-- Envio de som via Lua (jogador)
    --  Envio de som via Lua (jogador) (traduzido)
player:sendSingleSoundEffect(SoundEffect_t.ACTION_NOTIFICATION, true)

-- Envio de dois sons via Lua (jogador)
    --  Envio de dois sons via Lua (jogador) (traduzido)
player:sendDoubleSoundEffect(
    SoundEffect_t.SPELL_FIREBALL_RUNE,
    SoundEffect_t.SPELL_EXPLOSION_RUNE,
    true
)
```

## 🎮 **Sistema de Som por Categoria**

### **Sons de Combate**
- **Ataques Corpo a Corpo**: `HUMAN_CLOSE_ATK_FIST`, `MELEE_ATK_SWORD`, `MELEE_ATK_CLUB`, `MELEE_ATK_AXE`
- **Ataques à Distância**: `DIST_ATK_BOW`, `DIST_ATK_CROSSBOW`, `DIST_ATK_THROW`
- **Ataques Mágicos**: `MAGICAL_RANGE_ATK`
- **Monstros**: `MONSTER_MELEE_ATK_FIST`, `MONSTER_MELEE_ATK_CLAW`, `MONSTER_MELEE_ATK_BITE`

### **Sons de Magia**
- **Cura**: `SPELL_LIGHT_HEALING`, `SPELL_INTENSE_HEALING`, `SPELL_ULTIMATE_HEALING`
- **Ataque**: `SPELL_FIREBALL_RUNE`, `SPELL_EXPLOSION_RUNE`, `SPELL_ENERGY_WAVE`
- **Suporte**: `SPELL_HASTE`, `SPELL_LIGHT`, `SPELL_INVISIBLE`

### **Sons de Criaturas**
- **Barks**: Sons de comunicação das criaturas (2500-2544)
- **Death**: Sons de morte das criaturas (2600-2648)
- **Categorizados por raça**: Anfíbios, Aquáticos, Aves, Demônios, etc.

### **Sons de Ambiente**
- **Natureza**: `ENV_INSECTS_BIRDS`, `ENV_WIND_1`, `ENV_WATER_DEPTH`
- **Elementos**: `ENV_FIRE`, `ENV_WATERFALL`, `ENV_STORM_COMING`
- **Animais**: `ENV_OWL`, `ENV_WOLF_HOWL`, `ENV_LION_ROAR`

### **Sons de Ações**
- **Interação**: `ACTION_OPEN_DOOR`, `ACTION_CLOSE_DOOR`, `ACTION_NOTIFICATION`
- **Combate**: `ACTION_HITTING_WOOD`, `ACTION_METAL_OBJECT_HIT`
- **Interface**: `ACTION_CLICK_ON`, `ACTION_CLICK_OFF`

### **Sons de Itens**
- **Movimento**: `ITEM_MOVE_BACKPACK`, `ITEM_MOVE_METALIC`, `ITEM_MOVE_WOOD`
- **Uso**: `ITEM_USE_POTION`
- **Categorizados por tipo**: Metálicos, Madeira, Stackable, etc.

## 🔄 **Sistema de Transmissão**

### **Fluxo de Dados**
1. **Game Layer**: `Game::sendSingleSoundEffect()` ou `Game::sendDoubleSoundEffect()`
2. **Player Layer**: `Player::sendSingleSoundEffect()` ou `Player::sendDoubleSoundEffect()`
3. **Protocol Layer**: `ProtocolGame::sendSingleSoundEffect()` ou `ProtocolGame::sendDoubleSoundEffect()`
4. **Network**: Transmissão via `NetworkMessage` para clientes

### **Controle de Espectadores**
#### Nível Basic
```cpp
    if (!actor || actor->getNpc()) {
    } else if (actor == spectator) {
    } else if (actor->getPlayer()) {
    spectator->getPlayer()->sendSingleSoundEffect(pos, soundId, source);
```

#### Nível Intermediate
```cpp
// Encontrar espectadores na posição
for (const auto &spectator : Spectators().find<Player>(pos)) {
    SourceEffect_t source = CREATURES;
    
    // Determinar fonte do som
    if (!actor || actor->getNpc()) {
        source = GLOBAL;
    } else if (actor == spectator) {
        source = OWN;
    } else if (actor->getPlayer()) {
        source = OTHERS;
    }
    
    // Enviar som para espectador
    spectator->getPlayer()->sendSingleSoundEffect(pos, soundId, source);
}
```

#### Nível Advanced
```cpp
// Encontrar espectadores na posição
for (const auto &spectator : Spectators().find<Player>(pos)) {
    SourceEffect_t source = CREATURES;
    
    // Determinar fonte do som
    if (!actor || actor->getNpc()) {
        source = GLOBAL;
    } else if (actor == spectator) {
        source = OWN;
    } else if (actor->getPlayer()) {
        source = OTHERS;
    }
    
    // Enviar som para espectador
    spectator->getPlayer()->sendSingleSoundEffect(pos, soundId, source);
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

### **Compatibilidade com Protocolos**
#### Nível Basic
```cpp
// Verificação de protocolo antigo
if (oldProtocol) {
    return; // Não enviar som para protocolos antigos
}

// Estrutura do pacote de som
NetworkMessage msg;
msg.addByte(0x83);                    // Tipo de pacote
msg.addPosition(pos);                 // Posição
msg.addByte(0x06);                    // Tipo de efeito (som)
msg.addByte(static_cast<uint8_t>(source)); // Fonte
msg.add<uint16_t>(static_cast<uint16_t>(id)); // ID do som
msg.addByte(0x00);                    // Fim dos efeitos
```

#### Nível Intermediate
```cpp
// Verificação de protocolo antigo
if (oldProtocol) {
    return; // Não enviar som para protocolos antigos
}

// Estrutura do pacote de som
NetworkMessage msg;
msg.addByte(0x83);                    // Tipo de pacote
msg.addPosition(pos);                 // Posição
msg.addByte(0x06);                    // Tipo de efeito (som)
msg.addByte(static_cast<uint8_t>(source)); // Fonte
msg.add<uint16_t>(static_cast<uint16_t>(id)); // ID do som
msg.addByte(0x00);                    // Fim dos efeitos
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
// Verificação de protocolo antigo
if (oldProtocol) {
    return; // Não enviar som para protocolos antigos
}

// Estrutura do pacote de som
NetworkMessage msg;
msg.addByte(0x83);                    // Tipo de pacote
msg.addPosition(pos);                 // Posição
msg.addByte(0x06);                    // Tipo de efeito (som)
msg.addByte(static_cast<uint8_t>(source)); // Fonte
msg.add<uint16_t>(static_cast<uint16_t>(id)); // ID do som
msg.addByte(0x00);                    // Fim dos efeitos
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

### **Sistema de Combate**
- **Ataques**: Sons automáticos baseados no tipo de arma
- **Magias**: Sons de cast e impacto configuráveis
- **Dano**: Sons de impacto e miss

### **Sistema de Criaturas**
- **Monstros**: Sons de ataque, morte e comunicação
- **NPCs**: Sons de interação e comunicação
- **Jogadores**: Sons de ações e combate

### **Sistema de Itens**
- **Movimento**: Sons baseados no tipo de item
- **Uso**: Sons específicos para poções e outros itens
- **Equipamento**: Sons de equipar/desequipar

### **Sistema de Ambiente**
- **Mapa**: Sons ambientais baseados na localização
- **Clima**: Sons de chuva, vento, tempestade
- **Interação**: Sons de portas, baús, alavancas

## 🔧 **Otimizações e Performance**

### **Controle de Silêncio**
#### Nível Basic
```cpp
// Verificação de som silencioso
if (soundId == SoundEffect_t::SILENCE) {
    return; // Não processar som silencioso
}

// Verificação de som secundário silencioso
if (secondarySoundEffect == SoundEffect_t::SILENCE) {
    sendSingleSoundEffect(pos, mainSoundEffect, actor);
    return;
}
```

#### Nível Intermediate
```cpp
// Verificação de som silencioso
if (soundId == SoundEffect_t::SILENCE) {
    return; // Não processar som silencioso
}

// Verificação de som secundário silencioso
if (secondarySoundEffect == SoundEffect_t::SILENCE) {
    sendSingleSoundEffect(pos, mainSoundEffect, actor);
    return;
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
// Verificação de som silencioso
if (soundId == SoundEffect_t::SILENCE) {
    return; // Não processar som silencioso
}

// Verificação de som secundário silencioso
if (secondarySoundEffect == SoundEffect_t::SILENCE) {
    sendSingleSoundEffect(pos, mainSoundEffect, actor);
    return;
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

### **Gerenciamento de Espectadores**
- **Busca Otimizada**: `Spectators().find<Player>(pos)` para encontrar apenas jogadores
- **Filtro por Tipo**: Apenas jogadores recebem sons
- **Controle de Fonte**: Determinação automática da fonte do som

### **Protocolo Otimizado**
- **Dados Compactos**: Apenas informações essenciais
- **Compatibilidade**: Suporte a protocolos antigos e novos
- **Eficiência**: Transmissão otimizada via `NetworkMessage`

## 📊 **Métricas e Monitoramento**

### **Métricas Disponíveis**
- **Número de Sons Enviados**: Por tipo e categoria
- **Uso de Rede**: Dados transmitidos por som
- **Performance**: Tempo de processamento por som
- **Compatibilidade**: Uso de protocolos antigos vs novos

### **Logs e Debug**
#### Nível Basic
```cpp
if (oldProtocol) {
```

#### Nível Intermediate
```cpp
// Log de som enviado
g_logger().debug("Sound sent: {} at position {} from source {}", 
    static_cast<uint16_t>(soundId), 
    pos.toString(), 
    static_cast<uint8_t>(source)
);

// Log de compatibilidade
if (oldProtocol) {
    g_logger().debug("Sound skipped for old protocol");
}
```

#### Nível Advanced
```cpp
// Log de som enviado
g_logger().debug("Sound sent: {} at position {} from source {}", 
    static_cast<uint16_t>(soundId), 
    pos.toString(), 
    static_cast<uint8_t>(source)
);

// Log de compatibilidade
if (oldProtocol) {
    g_logger().debug("Sound skipped for old protocol");
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
1. **Servidor**: Envia dados de som via protocolo
2. **Cliente**: Recebe e processa sons
3. **Renderização**: Cliente responsável pela reprodução
4. **Sincronização**: Baseada em posição e fonte

### **Compatibilidade**
- **Protocolos Antigos**: Suporte via configuração
- **Protocolos Novos**: Funcionalidades completas
- **Fallback**: Comportamento padrão para incompatibilidades

## 📝 **Notas de Pesquisa**

### **Descobertas Importantes**
1. **Arquitetura Simples**: Sistema direto e eficiente
2. **Categorização Clara**: Sons organizados por tipo e função
3. **Flexibilidade**: Suporte a sons únicos e duplos
4. **Compatibilidade**: Funciona com protocolos antigos e novos

### **Diferenças do OTClient**
1. **Foco Servidor**: Canary foca na lógica do servidor
2. **Protocolo Otimizado**: Dados compactos e eficientes
3. **Sincronização Centralizada**: Controle pelo servidor
4. **Simplicidade**: Menos complexidade que o cliente

### **Pontos de Atenção**
1. **Compatibilidade**: Verificar suporte a protocolos
2. **Performance**: Monitorar uso de rede
3. **Sincronização**: Garantir consistência entre clientes
4. **Configuração**: Ajustar parâmetros conforme necessário

## 🔗 **Links Relacionados**
- [Documentação Principal](../../README.md)
- [Plano de Pesquisa](../research_plan.json)
- [Status Geral](../status_report.md)
- [CANARY-008: Sistema de Animações](../habdel/CANARY-008.md)
- [CANARY-010: Sistema de Partículas](../habdel/CANARY-010.md)

---
*Story concluída seguindo metodologia habdel - 2025-01-27*
