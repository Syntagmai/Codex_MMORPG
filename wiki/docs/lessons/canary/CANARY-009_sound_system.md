---
tags: [lesson, canary, sound_system, audio_effects, habdel_research]
type: lesson
status: published
priority: high
created: 2025-01-27
target: canary
---

# CANARY-009: Sistema de Som - Lição Educacional

## 🎯 **Objetivo da Lição**
Compreender a arquitetura e implementação do sistema de som no Canary, incluindo tipos de sons, transmissão de dados e integração com outros sistemas.

## 📚 **Teoria**

### **Conceitos Fundamentais**

#### **1. SoundEffect_t (Enum)**
O `SoundEffect_t` é um enum que define todos os tipos de efeitos sonoros disponíveis no Canary. Ele é organizado em categorias:

#### Nível Basic
```cpp
enum SoundEffect_t : uint16_t {
    // Sons de Combate (1-99)
    SILENCE = 0,
    HUMAN_CLOSE_ATK_FIST = 1,
    MELEE_ATK_SWORD = 3,
    
    // Sons de Monstros (100-999)
    MONSTER_MELEE_ATK_FIST = 100,
    MONSTER_MELEE_ATK_CLAW = 101,
    
    // Sons de Magia (1000-1999)
    SPELL_LIGHT_HEALING = 1001,
    SPELL_FIREBALL_RUNE = 1015,
    
    // Sons de Ambiente (2000-2999)
    ENV_WIND_1 = 2652,
    ENV_FIRE = 2745,
    
    // Sons de Ações (2600-2799)
    ACTION_OPEN_DOOR = 2674,
    ACTION_NOTIFICATION = 2771,
    
    // Sons de Itens (2780-2999)
    ITEM_MOVE_BACKPACK = 2786,
    ITEM_USE_POTION = 2787
};
```

#### Nível Intermediate
```cpp
enum SoundEffect_t : uint16_t {
    // Sons de Combate (1-99)
    SILENCE = 0,
    HUMAN_CLOSE_ATK_FIST = 1,
    MELEE_ATK_SWORD = 3,
    
    // Sons de Monstros (100-999)
    MONSTER_MELEE_ATK_FIST = 100,
    MONSTER_MELEE_ATK_CLAW = 101,
    
    // Sons de Magia (1000-1999)
    SPELL_LIGHT_HEALING = 1001,
    SPELL_FIREBALL_RUNE = 1015,
    
    // Sons de Ambiente (2000-2999)
    ENV_WIND_1 = 2652,
    ENV_FIRE = 2745,
    
    // Sons de Ações (2600-2799)
    ACTION_OPEN_DOOR = 2674,
    ACTION_NOTIFICATION = 2771,
    
    // Sons de Itens (2780-2999)
    ITEM_MOVE_BACKPACK = 2786,
    ITEM_USE_POTION = 2787
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
    // Sons de Combate (1-99)
    SILENCE = 0,
    HUMAN_CLOSE_ATK_FIST = 1,
    MELEE_ATK_SWORD = 3,
    
    // Sons de Monstros (100-999)
    MONSTER_MELEE_ATK_FIST = 100,
    MONSTER_MELEE_ATK_CLAW = 101,
    
    // Sons de Magia (1000-1999)
    SPELL_LIGHT_HEALING = 1001,
    SPELL_FIREBALL_RUNE = 1015,
    
    // Sons de Ambiente (2000-2999)
    ENV_WIND_1 = 2652,
    ENV_FIRE = 2745,
    
    // Sons de Ações (2600-2799)
    ACTION_OPEN_DOOR = 2674,
    ACTION_NOTIFICATION = 2771,
    
    // Sons de Itens (2780-2999)
    ITEM_MOVE_BACKPACK = 2786,
    ITEM_USE_POTION = 2787
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

#### **2. SourceEffect_t (Enum)**
Define a fonte do efeito sonoro, controlando quem deve ouvir o som:

#### Nível Basic
```cpp
enum class SourceEffect_t : uint8_t {
    GLOBAL = 0,      // Todos os jogadores na área
    OWN = 1,         // Apenas o jogador que executou a ação
    OTHERS = 2,      // Outros jogadores (não o executor)
    CREATURES = 3    // Criaturas (NPCs e monstros)
};
```

#### Nível Intermediate
```cpp
enum class SourceEffect_t : uint8_t {
    GLOBAL = 0,      // Todos os jogadores na área
    OWN = 1,         // Apenas o jogador que executou a ação
    OTHERS = 2,      // Outros jogadores (não o executor)
    CREATURES = 3    // Criaturas (NPCs e monstros)
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
enum class SourceEffect_t : uint8_t {
    GLOBAL = 0,      // Todos os jogadores na área
    OWN = 1,         // Apenas o jogador que executou a ação
    OTHERS = 2,      // Outros jogadores (não o executor)
    CREATURES = 3    // Criaturas (NPCs e monstros)
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

#### **3. Arquitetura do Sistema**
O sistema de som segue uma arquitetura em camadas:

```
┌─────────────────┐
│   Game Layer    │ ← sendSingleSoundEffect()
├─────────────────┤
│  Player Layer   │ ← sendSingleSoundEffect()
├─────────────────┤
│ Protocol Layer  │ ← sendSingleSoundEffect()
├─────────────────┤
│  Network Layer  │ ← NetworkMessage
└─────────────────┘
```

### **Fluxo de Dados**
1. **Game Layer**: Recebe solicitação de som
2. **Player Layer**: Determina espectadores e fontes
3. **Protocol Layer**: Codifica dados para transmissão
4. **Network Layer**: Envia para clientes

## 🔧 **Exemplos Práticos**

### **Exemplo 1: Som de Combate**
#### Nível Basic
```cpp
// Implementação de ataque com espada
void Player::attackWithSword() {
    // Enviar som de ataque
    g_game().sendSingleSoundEffect(
        getPosition(),           // Posição do jogador
        SoundEffect_t::MELEE_ATK_SWORD,  // Som de espada
        getPlayer()              // Ator (jogador)
    );
    
    // Lógica de combate...
}
```

#### Nível Intermediate
```cpp
// Implementação de ataque com espada
void Player::attackWithSword() {
    // Enviar som de ataque
    g_game().sendSingleSoundEffect(
        getPosition(),           // Posição do jogador
        SoundEffect_t::MELEE_ATK_SWORD,  // Som de espada
        getPlayer()              // Ator (jogador)
    );
    
    // Lógica de combate...
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
// Implementação de ataque com espada
void Player::attackWithSword() {
    // Enviar som de ataque
    g_game().sendSingleSoundEffect(
        getPosition(),           // Posição do jogador
        SoundEffect_t::MELEE_ATK_SWORD,  // Som de espada
        getPlayer()              // Ator (jogador)
    );
    
    // Lógica de combate...
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

### **Exemplo 2: Som de Magia**
#### Nível Basic
```cpp
// Implementação de magia de cura
void Player::castHealingSpell() {
    // Enviar som de magia
    g_game().sendSingleSoundEffect(
        getPosition(),
        SoundEffect_t::SPELL_LIGHT_HEALING,
        getPlayer()
    );
    
    // Aplicar efeito de cura...
}
```

#### Nível Intermediate
```cpp
// Implementação de magia de cura
void Player::castHealingSpell() {
    // Enviar som de magia
    g_game().sendSingleSoundEffect(
        getPosition(),
        SoundEffect_t::SPELL_LIGHT_HEALING,
        getPlayer()
    );
    
    // Aplicar efeito de cura...
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
// Implementação de magia de cura
void Player::castHealingSpell() {
    // Enviar som de magia
    g_game().sendSingleSoundEffect(
        getPosition(),
        SoundEffect_t::SPELL_LIGHT_HEALING,
        getPlayer()
    );
    
    // Aplicar efeito de cura...
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

### **Exemplo 3: Dois Sons Simultâneos**
#### Nível Basic
```cpp
// Combate com som de ataque e impacto
void Player::meleeCombat() {
    g_game().sendDoubleSoundEffect(
        getPosition(),
        getAttackSoundEffect(),    // Som de ataque
        getHitSoundEffect(),       // Som de impacto
        getPlayer()
    );
}
```

#### Nível Intermediate
```cpp
// Combate com som de ataque e impacto
void Player::meleeCombat() {
    g_game().sendDoubleSoundEffect(
        getPosition(),
        getAttackSoundEffect(),    // Som de ataque
        getHitSoundEffect(),       // Som de impacto
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
void Player::meleeCombat() {
    g_game().sendDoubleSoundEffect(
        getPosition(),
        getAttackSoundEffect(),    // Som de ataque
        getHitSoundEffect(),       // Som de impacto
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

### **Exemplo 4: Som de Ambiente**
#### Nível Basic
```cpp
// Som de ambiente (vento)
void Game::addWindSound(const Position &pos) {
    g_game().sendSingleSoundEffect(
        pos,
        SoundEffect_t::ENV_WIND_1,
        nullptr  // Sem ator específico (som global)
    );
}
```

#### Nível Intermediate
```cpp
// Som de ambiente (vento)
void Game::addWindSound(const Position &pos) {
    g_game().sendSingleSoundEffect(
        pos,
        SoundEffect_t::ENV_WIND_1,
        nullptr  // Sem ator específico (som global)
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
void Game::addWindSound(const Position &pos) {
    g_game().sendSingleSoundEffect(
        pos,
        SoundEffect_t::ENV_WIND_1,
        nullptr  // Sem ator específico (som global)
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

### **Exemplo 5: Funções Lua**
```lua
-- Envio de som via Lua
    --  Envio de som via Lua (traduzido)
function onPlayerAttack(player, target)
    -- Função: onPlayerAttack
    -- Som de ataque
    --  Som de ataque (traduzido)
    player:sendSingleSoundEffect(SoundEffect_t.MELEE_ATK_SWORD, true)
    
    -- Som de impacto se acertar
    --  Som de impacto se acertar (traduzido)
    if target then
    -- Verificação condicional
        target:getPosition():sendSingleSoundEffect(SoundEffect_t.MELEE_ATK_SWORD)
    end
end

-- Som de ambiente via posição
function addAmbientSound(pos)
    -- Função: addAmbientSound
    pos:sendSingleSoundEffect(SoundEffect_t.ENV_WIND_1)
end
```

## 🎮 **Categorias de Som**

### **Sons de Combate**
- **Ataques Corpo a Corpo**: Espada, clava, machado, punho
- **Ataques à Distância**: Arco, besta, arremesso
- **Ataques Mágicos**: Magias de ataque
- **Monstros**: Sons específicos por tipo de criatura

### **Sons de Magia**
- **Cura**: Magias de regeneração
- **Ataque**: Magias ofensivas
- **Suporte**: Buffs e debuffs
- **Runas**: Magias em forma de runas

### **Sons de Ambiente**
- **Natureza**: Vento, água, insetos
- **Elementos**: Fogo, gelo, energia
- **Animais**: Sons de criaturas selvagens
- **Clima**: Chuva, tempestade, trovão

### **Sons de Ações**
- **Interação**: Portas, baús, alavancas
- **Interface**: Cliques, notificações
- **Combate**: Impactos, bloqueios

### **Sons de Itens**
- **Movimento**: Baseado no tipo de item
- **Uso**: Poções, runas, ferramentas
- **Equipamento**: Armaduras, armas

## 📝 **Exercícios Práticos**

### **Exercício 1: Implementar Som de Porta**
#### Nível Basic
```cpp
// Implemente uma função que reproduz som ao abrir uma porta
void Door::open() {
    // TODO: Adicione o som de abertura da porta
    // Dica: Use ACTION_OPEN_DOOR
    
    // Lógica de abertura da porta...
}
```

#### Nível Intermediate
```cpp
// Implemente uma função que reproduz som ao abrir uma porta
void Door::open() {
    // TODO: Adicione o som de abertura da porta
    // Dica: Use ACTION_OPEN_DOOR
    
    // Lógica de abertura da porta...
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
// Implemente uma função que reproduz som ao abrir uma porta
void Door::open() {
    // TODO: Adicione o som de abertura da porta
    // Dica: Use ACTION_OPEN_DOOR
    
    // Lógica de abertura da porta...
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

**Solução:**
#### Nível Basic
```cpp
void Door::open() {
    // Som de abertura da porta
    g_game().sendSingleSoundEffect(
        getPosition(),
        SoundEffect_t::ACTION_OPEN_DOOR,
        nullptr  // Som global
    );
    
    // Lógica de abertura da porta...
}
```

#### Nível Intermediate
```cpp
void Door::open() {
    // Som de abertura da porta
    g_game().sendSingleSoundEffect(
        getPosition(),
        SoundEffect_t::ACTION_OPEN_DOOR,
        nullptr  // Som global
    );
    
    // Lógica de abertura da porta...
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
void Door::open() {
    // Som de abertura da porta
    g_game().sendSingleSoundEffect(
        getPosition(),
        SoundEffect_t::ACTION_OPEN_DOOR,
        nullptr  // Som global
    );
    
    // Lógica de abertura da porta...
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

### **Exercício 2: Som de Poção**
#### Nível Basic
```cpp
// Implemente som ao usar uma poção
void Player::usePotion() {
    // TODO: Adicione o som de uso de poção
    // Dica: Use ITEM_USE_POTION
    
    // Lógica de uso da poção...
}
```

#### Nível Intermediate
```cpp
// Implemente som ao usar uma poção
void Player::usePotion() {
    // TODO: Adicione o som de uso de poção
    // Dica: Use ITEM_USE_POTION
    
    // Lógica de uso da poção...
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
// Implemente som ao usar uma poção
void Player::usePotion() {
    // TODO: Adicione o som de uso de poção
    // Dica: Use ITEM_USE_POTION
    
    // Lógica de uso da poção...
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

**Solução:**
#### Nível Basic
```cpp
void Player::usePotion() {
    // Som de uso de poção
    g_game().sendSingleSoundEffect(
        getPosition(),
        SoundEffect_t::ITEM_USE_POTION,
        getPlayer()
    );
    
    // Lógica de uso da poção...
}
```

#### Nível Intermediate
```cpp
void Player::usePotion() {
    // Som de uso de poção
    g_game().sendSingleSoundEffect(
        getPosition(),
        SoundEffect_t::ITEM_USE_POTION,
        getPlayer()
    );
    
    // Lógica de uso da poção...
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
void Player::usePotion() {
    // Som de uso de poção
    g_game().sendSingleSoundEffect(
        getPosition(),
        SoundEffect_t::ITEM_USE_POTION,
        getPlayer()
    );
    
    // Lógica de uso da poção...
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

### **Exercício 3: Combate com Dois Sons**
#### Nível Basic
```cpp
// Implemente combate com som de ataque e impacto
void Player::attack() {
    // TODO: Adicione som de ataque e impacto
    // Dica: Use sendDoubleSoundEffect
    
    // Lógica de combate...
}
```

#### Nível Intermediate
```cpp
// Implemente combate com som de ataque e impacto
void Player::attack() {
    // TODO: Adicione som de ataque e impacto
    // Dica: Use sendDoubleSoundEffect
    
    // Lógica de combate...
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
// Implemente combate com som de ataque e impacto
void Player::attack() {
    // TODO: Adicione som de ataque e impacto
    // Dica: Use sendDoubleSoundEffect
    
    // Lógica de combate...
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

**Solução:**
#### Nível Basic
```cpp
void Player::attack() {
    // Som de ataque e impacto
    g_game().sendDoubleSoundEffect(
        getPosition(),
        getAttackSoundEffect(),    // Som de ataque
        getHitSoundEffect(),       // Som de impacto
        getPlayer()
    );
    
    // Lógica de combate...
}
```

#### Nível Intermediate
```cpp
void Player::attack() {
    // Som de ataque e impacto
    g_game().sendDoubleSoundEffect(
        getPosition(),
        getAttackSoundEffect(),    // Som de ataque
        getHitSoundEffect(),       // Som de impacto
        getPlayer()
    );
    
    // Lógica de combate...
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
void Player::attack() {
    // Som de ataque e impacto
    g_game().sendDoubleSoundEffect(
        getPosition(),
        getAttackSoundEffect(),    // Som de ataque
        getHitSoundEffect(),       // Som de impacto
        getPlayer()
    );
    
    // Lógica de combate...
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

### **Exercício 4: Lua - Som de Notificação**
```lua
-- Implemente função Lua que envia som de notificação
function sendNotification(player, message)
    -- Função: sendNotification
    -- TODO: Adicione som de notificação
    -- Dica: Use ACTION_NOTIFICATION
    --  Dica: Use ACTION_NOTIFICATION (traduzido)
    
    player:sendTextMessage(MESSAGE_INFO_DESCR, message)
end
```

**Solução:**
```lua
function sendNotification(player, message)
    -- Função: sendNotification
    -- Som de notificação
    player:sendSingleSoundEffect(SoundEffect_t.ACTION_NOTIFICATION, true)
    
    player:sendTextMessage(MESSAGE_INFO_DESCR, message)
end
```

## 🔍 **Conceitos-Chave**

### **1. Controle de Espectadores**
O sistema automaticamente determina quem deve ouvir cada som:

#### Nível Basic
```cpp
    if (!actor || actor->getNpc()) {
    } else if (actor == spectator) {
    } else if (actor->getPlayer()) {
    spectator->getPlayer()->sendSingleSoundEffect(pos, soundId, source);
```

#### Nível Intermediate
```cpp
for (const auto &spectator : Spectators().find<Player>(pos)) {
    SourceEffect_t source = CREATURES;
    
    if (!actor || actor->getNpc()) {
        source = GLOBAL;           // Som global
    } else if (actor == spectator) {
        source = OWN;              // Som próprio
    } else if (actor->getPlayer()) {
        source = OTHERS;           // Som de outros
    }
    
    spectator->getPlayer()->sendSingleSoundEffect(pos, soundId, source);
}
```

#### Nível Advanced
```cpp
for (const auto &spectator : Spectators().find<Player>(pos)) {
    SourceEffect_t source = CREATURES;
    
    if (!actor || actor->getNpc()) {
        source = GLOBAL;           // Som global
    } else if (actor == spectator) {
        source = OWN;              // Som próprio
    } else if (actor->getPlayer()) {
        source = OTHERS;           // Som de outros
    }
    
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

### **2. Compatibilidade com Protocolos**
O sistema verifica se o cliente suporta sons:

#### Nível Basic
```cpp
if (oldProtocol) {
    return; // Não enviar som para protocolos antigos
}
```

#### Nível Intermediate
```cpp
if (oldProtocol) {
    return; // Não enviar som para protocolos antigos
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
if (oldProtocol) {
    return; // Não enviar som para protocolos antigos
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

### **3. Otimização de Performance**
- Verificação de som silencioso
- Busca otimizada de espectadores
- Dados compactos de transmissão

### **4. Integração com Lua**
O sistema expõe funções Lua para facilitar o uso:

```lua
-- Via posição
pos:sendSingleSoundEffect(soundId)
pos:sendDoubleSoundEffect(mainSound, secondarySound)

-- Via jogador
    --  Via jogador (traduzido)
player:sendSingleSoundEffect(soundId, isOwn)
player:sendDoubleSoundEffect(mainSound, secondarySound, isOwn)
```

## 🎯 **Aplicações Práticas**

### **1. Sistema de Combate**
- Sons automáticos baseados no tipo de arma
- Feedback sonoro para ataques e defesas
- Sons de magias e runas

### **2. Sistema de Interação**
- Sons de portas, baús e alavancas
- Feedback para ações do jogador
- Sons de interface

### **3. Sistema de Ambiente**
- Sons baseados na localização
- Atmosfera sonora dinâmica
- Sons de clima e natureza

### **4. Sistema de Itens**
- Sons baseados no tipo de item
- Feedback para movimentação
- Sons de uso de itens

## 📊 **Boas Práticas**

### **1. Escolha de Sons**
- Use sons apropriados para cada ação
- Considere o contexto e ambiente
- Mantenha consistência sonora

### **2. Performance**
- Evite enviar sons desnecessários
- Use `SILENCE` quando apropriado
- Otimize a frequência de sons

### **3. Compatibilidade**
- Sempre verifique suporte a protocolos
- Forneça fallbacks quando necessário
- Teste com diferentes clientes

### **4. Integração**
- Integre sons com outros sistemas
- Mantenha sincronização adequada
- Considere a experiência do usuário

## 🔗 **Links Relacionados**
- [[CANARY-008_animation_system]] - Sistema de Animações
- [[CANARY-010_particle_system]] - Sistema de Partículas
- [Documentação Principal](../../README.md)

---

*Lição criada seguindo metodologia habdel - 2025-01-27* 