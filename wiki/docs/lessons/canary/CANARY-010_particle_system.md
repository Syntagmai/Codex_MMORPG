---
tags: [canary_lesson, particle_system, magic_effects, visual_effects, game_development]
type: lesson
status: published
priority: high
created: 2025-01-27
target: canary
---

# CANARY-010: Sistema de Partículas - Lição Educacional

## 🎯 **Objetivo da Lição**
Compreender o sistema de partículas (magic effects) do Canary, sua arquitetura, implementação e uso prático no desenvolvimento de servidores MMORPG.

## 📚 **Teoria**

### **O que é o Sistema de Partículas?**
O Sistema de Partículas do Canary é responsável por gerenciar todos os efeitos visuais que aparecem no jogo, desde efeitos de combate até animações ambientais. Ele utiliza o conceito de "Magic Effects" para criar uma experiência visual rica e imersiva.

### **Conceitos Fundamentais**

#### **1. Magic Effects**
- **Definição**: Efeitos visuais pré-definidos com IDs únicos
- **Propósito**: Criar feedback visual para ações do jogador
- **Categorias**: Combate, Magia, Ambiente, Criaturas, Especiais

#### **2. Sistema de Coordenadas**
- **Position**: Localização 3D (x, y, z) onde o efeito aparece
- **Espectadores**: Jogadores que podem ver o efeito
- **Visibilidade**: Controle de quem vê cada efeito

#### **3. Protocolo de Rede**
- **Transmissão**: Dados enviados do servidor para o cliente
- **Compatibilidade**: Suporte a protocolos antigos e novos
- **Otimização**: Dados compactos para eficiência

### **Arquitetura do Sistema**

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Game Layer    │    │  Protocol Layer │    │  Client Layer   │
│                 │    │                 │    │                 │
│ addMagicEffect  │───▶│ sendMagicEffect │───▶│   Render Effect │
│ removeMagicEffect│   │ removeMagicEffect│   │                 │
│ addDistanceEffect│   │ sendDistanceShoot│   │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Lua Layer     │    │  Network Layer  │    │  Visual Layer   │
│                 │    │                 │    │                 │
│ position:send   │    │ NetworkMessage  │    │   Animation     │
│ position:remove │    │ Protocol Control│    │   Synchronization│
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 💻 **Exemplos Práticos**

### **1. Efeitos Básicos de Combate**

```cpp
// Exemplo 1: Dano com sangue
void Player::takeDamage(int32_t damage) {
    if (damage > 0) {
        // Efeito visual de sangue
        g_game().addMagicEffect(getPosition(), CONST_ME_DRAWBLOOD);
    }
}

// Exemplo 2: Bloqueio de ataque
void Player::blockAttack() {
    // Efeito visual de bloqueio
    g_game().addMagicEffect(getPosition(), CONST_ME_BLOCKHIT);
}

// Exemplo 3: Esquiva de ataque
void Player::dodgeAttack() {
    // Efeito visual de esquiva
    g_game().addMagicEffect(getPosition(), CONST_ME_DODGE);
}
```

### **2. Efeitos de Magia**

```cpp
// Exemplo 1: Magia de cura
void Player::castHealSpell() {
    // Efeito azul para magias de cura
    g_game().addMagicEffect(getPosition(), CONST_ME_MAGIC_BLUE);
}

// Exemplo 2: Magia de ataque
void Player::castAttackSpell() {
    // Efeito vermelho para magias de ataque
    g_game().addMagicEffect(getPosition(), CONST_ME_MAGIC_RED);
}

// Exemplo 3: Magia de proteção
void Player::castProtectionSpell() {
    // Efeito verde para magias de proteção
    g_game().addMagicEffect(getPosition(), CONST_ME_MAGIC_GREEN);
}
```

### **3. Efeitos de Teleporte**

```cpp
// Exemplo 1: Teleporte normal
void Player::teleport(const Position &newPos) {
    // Efeito no local de origem
    g_game().addMagicEffect(getPosition(), CONST_ME_TELEPORT);
    
    // Lógica de teleporte
    setPosition(newPos);
    
    // Efeito no local de destino
    g_game().addMagicEffect(newPos, CONST_ME_TELEPORT);
}

// Exemplo 2: Teleporte especial
void Player::specialTeleport(const Position &newPos) {
    // Efeito roxo para teleporte especial
    g_game().addMagicEffect(getPosition(), CONST_ME_PURPLETELEPORT);
    
    setPosition(newPos);
    g_game().addMagicEffect(newPos, CONST_ME_PURPLETELEPORT);
}
```

### **4. Projéteis (Distance Effects)**

```cpp
// Exemplo 1: Tiro de arco
void Player::shootArrow(const Position &target) {
    // Efeito de projétil de arco
    g_game().addDistanceEffect(getPosition(), target, CONST_ANI_ARROW);
}

// Exemplo 2: Magia de distância
void Player::castDistanceSpell(const Position &target) {
    // Efeito de energia mágica
    g_game().addDistanceEffect(getPosition(), target, CONST_ANI_ENERGY);
}

// Exemplo 3: Tiro de crossbow
void Player::shootBolt(const Position &target) {
    // Efeito de projétil de crossbow
    g_game().addDistanceEffect(getPosition(), target, CONST_ANI_BOLT);
}
```

### **5. Uso via Lua**

```lua
-- Exemplo 1: Efeito básico
local pos = Position(100, 100, 7)
pos:sendMagicEffect(CONST_ME_MAGIC_BLUE)

-- Exemplo 2: Remoção de efeito
pos:removeMagicEffect(CONST_ME_MAGIC_BLUE)

-- Exemplo 3: Efeito para jogador específico
local player = Player("TestPlayer")
pos:sendMagicEffect(CONST_ME_TELEPORT, player)

-- Exemplo 4: Projétil
pos:sendDistanceEffect(Position(105, 105, 7), CONST_ANI_ARROW)

-- Exemplo 5: Efeito de área
pos:sendMagicEffect(CONST_ME_FIREAREA)
```

## 🎮 **Categorias de Efeitos**

### **Efeitos de Combate**
| Efeito | ID | Descrição | Uso |
|--------|----|-----------|-----|
| `CONST_ME_DRAWBLOOD` | 1 | Sangue | Dano físico |
| `CONST_ME_BLOCKHIT` | 4 | Bloqueio | Defesa bem-sucedida |
| `CONST_ME_DODGE` | 231 | Esquiva | Esquiva de ataque |
| `CONST_ME_CRITICAL_DAMAGE` | 173 | Dano crítico | Golpe crítico |
| `CONST_ME_FATAL` | 230 | Dano fatal | Morte |

### **Efeitos de Magia**
| Efeito | ID | Descrição | Uso |
|--------|----|-----------|-----|
| `CONST_ME_MAGIC_BLUE` | 13 | Magia azul | Cura/proteção |
| `CONST_ME_MAGIC_RED` | 14 | Magia vermelha | Ataque |
| `CONST_ME_MAGIC_GREEN` | 15 | Magia verde | Suporte |
| `CONST_ME_PURPLEENERGY` | 48 | Energia roxa | Magia especial |
| `CONST_ME_MAGIC_POWDER` | 182 | Pó mágico | Transformação |

### **Efeitos de Teleporte**
| Efeito | ID | Descrição | Uso |
|--------|----|-----------|-----|
| `CONST_ME_TELEPORT` | 11 | Teleporte | Teleporte normal |
| `CONST_ME_PURPLETELEPORT` | 222 | Teleporte roxo | Teleporte especial |
| `CONST_ME_REDTELEPORT` | 223 | Teleporte vermelho | Teleporte de emergência |
| `CONST_ME_ORANGETELEPORT` | 224 | Teleporte laranja | Teleporte VIP |

### **Efeitos de Ambiente**
| Efeito | ID | Descrição | Uso |
|--------|----|-----------|-----|
| `CONST_ME_SMOKE` | 68 | Fumaça | Ambiente |
| `CONST_ME_FIREAREA` | 7 | Área de fogo | Campo de fogo |
| `CONST_ME_ICEAREA` | 42 | Área de gelo | Campo de gelo |
| `CONST_ME_POISONAREA` | 21 | Área de veneno | Campo de veneno |
| `CONST_ME_WATER_DROP` | 243 | Gota d'água | Chuva |

## 🔧 **Implementação Técnica**

### **Funções Principais**

```cpp
// Adicionar magic effect
void Game::addMagicEffect(const Position &pos, uint16_t effect);
void Game::addMagicEffect(const CreatureVector &spectators, const Position &pos, uint16_t effect);

// Remover magic effect
void Game::removeMagicEffect(const Position &pos, uint16_t effect);
void Game::removeMagicEffect(const CreatureVector &spectators, const Position &pos, uint16_t effect);

// Adicionar efeito de distância
void Game::addDistanceEffect(const Position &fromPos, const Position &toPos, uint16_t effect);
void Game::addDistanceEffect(const CreatureVector &spectators, const Position &fromPos, const Position &toPos, uint16_t effect);
```

### **Protocolo de Rede**

```cpp
// Envio de magic effect
void ProtocolGame::sendMagicEffect(const Position &pos, uint16_t type) {
    if (!canSee(pos) || (oldProtocol && type > 0xFF)) {
        return;
    }

    NetworkMessage msg;
    if (oldProtocol) {
        msg.addByte(0x83);
        msg.addPosition(pos);
        msg.addByte(static_cast<uint8_t>(type));
    } else {
        msg.addByte(0x83);
        msg.addPosition(pos);
        msg.addByte(MAGIC_EFFECTS_CREATE_EFFECT);
        msg.add<uint16_t>(type);
        msg.addByte(MAGIC_EFFECTS_END_LOOP);
    }
    writeToOutputBuffer(msg);
}
```

### **Funções Lua**

```cpp
// Envio de magic effect via Lua
int PositionFunctions::luaPositionSendMagicEffect(lua_State* L) {
    // position:sendMagicEffect(magicEffect[, player = nullptr])
    CreatureVector spectators;
    if (lua_gettop(L) >= 3) {
        const auto &player = Lua::getPlayer(L, 3);
        if (!player) {
            Lua::reportErrorFunc(Lua::getErrorDesc(LUA_ERROR_PLAYER_NOT_FOUND));
            return 1;
        }
        spectators.emplace_back(player);
    }

    MagicEffectClasses magicEffect = Lua::getNumber<MagicEffectClasses>(L, 2);
    if (g_configManager().getBoolean(WARN_UNSAFE_SCRIPTS) && 
        !g_game().isMagicEffectRegistered(magicEffect)) {
        g_logger().warn("Unregistered magic effect type '{}' was blocked", 
            fmt::underlying(magicEffect));
        Lua::pushBoolean(L, false);
        return 1;
    }

    const Position &position = Lua::getPosition(L, 1);
    if (!spectators.empty()) {
        Game::addMagicEffect(spectators, position, magicEffect);
    } else {
        g_game().addMagicEffect(position, magicEffect);
    }

    Lua::pushBoolean(L, true);
    return 1;
}
```

## 📝 **Exercícios Práticos**

### **Exercício 1: Sistema de Combate Básico**
Crie um sistema de combate que use diferentes efeitos visuais para diferentes tipos de dano:

```cpp
// Implemente esta função
void Player::takeDamage(CombatType_t combatType, int32_t damage) {
    // TODO: Adicione efeitos visuais baseados no tipo de combate
    // - Físico: CONST_ME_DRAWBLOOD
    // - Fogo: CONST_ME_HITBYFIRE
    // - Gelo: CONST_ME_ICEATTACK
    // - Energia: CONST_ME_ENERGYHIT
    // - Sagrado: CONST_ME_HOLYDAMAGE
    // - Morte: CONST_ME_MORTAREA
}
```

### **Exercício 2: Sistema de Magias**
Crie um sistema de magias com efeitos visuais apropriados:

```cpp
// Implemente esta função
void Player::castSpell(SpellType_t spellType) {
    // TODO: Adicione efeitos visuais baseados no tipo de magia
    // - Cura: CONST_ME_MAGIC_BLUE
    // - Ataque: CONST_ME_MAGIC_RED
    // - Proteção: CONST_ME_MAGIC_GREEN
    // - Energia: CONST_ME_PURPLEENERGY
    // - Transformação: CONST_ME_MAGIC_POWDER
}
```

### **Exercício 3: Sistema de Teleporte**
Crie um sistema de teleporte com diferentes efeitos:

```cpp
// Implemente esta função
void Player::teleport(const Position &newPos, TeleportType_t type) {
    // TODO: Adicione efeitos visuais baseados no tipo de teleporte
    // - Normal: CONST_ME_TELEPORT
    // - VIP: CONST_ME_PURPLETELEPORT
    // - Emergência: CONST_ME_REDTELEPORT
    // - Especial: CONST_ME_ORANGETELEPORT
}
```

### **Exercício 4: Sistema de Projéteis**
Crie um sistema de projéteis com diferentes tipos:

```cpp
// Implemente esta função
void Player::shootProjectile(const Position &target, ProjectileType_t type) {
    // TODO: Adicione efeitos de projétil baseados no tipo
    // - Flecha: CONST_ANI_ARROW
    // - Bolt: CONST_ANI_BOLT
    // - Spear: CONST_ANI_SPEAR
    // - Energy: CONST_ANI_ENERGY
    // - Fire: CONST_ANI_FIRE
}
```

### **Exercício 5: Sistema Lua**
Crie scripts Lua que usem o sistema de partículas:

```lua
-- TODO: Implemente estas funções Lua

-- 1. Função para criar efeito de explosão
function createExplosion(position)
    -- Adicione efeito de explosão
end

-- 2. Função para criar efeito de chuva
function createRainEffect(area)
    -- Adicione efeito de chuva na área
end

-- 3. Função para criar efeito de teleporte especial
function specialTeleport(player, targetPosition)
    -- Adicione efeito de teleporte especial
end

-- 4. Função para criar efeito de magia combinada
function combinedMagicEffect(position, spellType1, spellType2)
    -- Adicione dois efeitos mágicos simultâneos
end
```

## 🎯 **Conceitos-Chave**

### **1. Sistema de Espectadores**
- **Definição**: Jogadores que podem ver um efeito
- **Controle**: Apenas espectadores recebem o efeito
- **Otimização**: Reduz tráfego de rede

### **2. Compatibilidade de Protocolo**
- **Protocolos Antigos**: Suporte limitado (8-bit IDs)
- **Protocolos Novos**: Suporte completo (16-bit IDs)
- **Fallback**: Comportamento seguro para incompatibilidades

### **3. Validação de Efeitos**
- **Registro**: Efeitos devem estar registrados
- **Segurança**: Bloqueia efeitos não registrados
- **Logs**: Registra tentativas de uso inválido

### **4. Performance**
- **Otimização**: Dados compactos
- **Eficiência**: Transmissão otimizada
- **Monitoramento**: Métricas de uso

## 🔗 **Integração com Outros Sistemas**

### **Sistema de Combate**
- Efeitos automáticos para dano
- Feedback visual para defesa
- Animações de ataques especiais

### **Sistema de Magias**
- Efeitos específicos por tipo
- Animações de cast
- Efeitos de impacto

### **Sistema de Criaturas**
- Efeitos de spawn/morte
- Animações de ataque
- Efeitos especiais

### **Sistema de Ambiente**
- Efeitos climáticos
- Animações ambientais
- Efeitos de interação

## 📊 **Boas Práticas**

### **1. Uso Consistente**
- Use efeitos apropriados para cada ação
- Mantenha consistência visual
- Evite sobrecarga de efeitos

### **2. Performance**
- Limite efeitos simultâneos
- Use espectadores adequadamente
- Monitore uso de rede

### **3. Compatibilidade**
- Teste com diferentes protocolos
- Implemente fallbacks
- Valide efeitos registrados

### **4. Manutenibilidade**
- Documente uso de efeitos
- Use constantes nomeadas
- Mantenha código limpo

## 🔗 **Links Relacionados**
- [[CANARY-009_sound_system]] - Sistema de Som
- [[CANARY-011_map_system]] - Sistema de Mapas
- [Documentação Principal](../../README.md)
- [Pesquisa CANARY-010](../research/habdel/CANARY-010.md)

---
*Lição criada seguindo metodologia habdel - 2025-01-27* 