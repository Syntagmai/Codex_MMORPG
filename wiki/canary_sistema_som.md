---
tags: [canary, som, audio, efeitos, soundeffect, servidor, mmorpg, c++, habdel]
type: course
level: intermediate
created: 2025-08-05
updated: 2025-08-05
aliases: [canary_som, canary_audio, canary_sound, canary_soundeffect]
---

# 🔊 Sistema de Som - Canary

## 📋 **Visão Geral**
O Sistema de Som do Canary gerencia todos os efeitos sonoros do servidor, incluindo sons de combate, magias, ambiente, ações e itens. Ele utiliza enums para categorizar efeitos e integra o envio de sons via protocolo para os clientes.

## 🏗️ **Arquitetura do Sistema**
- **Definições**: `canary/src/creatures/creatures_definitions.hpp` (SoundEffect_t, SourceEffect_t)
- **Gerenciamento**: `canary/src/game/game.cpp` (sendSingleSoundEffect, sendDoubleSoundEffect)
- **Protocolo**: `canary/src/server/network/protocol/protocolgame.cpp`
- **Funções Lua**: `canary/src/lua/functions/map/position_functions.cpp`

## 🔧 **Componentes Principais**
### SoundEffect_t e SourceEffect_t
```cpp
enum SoundEffect_t : uint16_t {
    SILENCE = 0,
    HUMAN_CLOSE_ATK_FIST = 1,
    SPELL_LIGHT_HEALING = 1001,
    ENV_WIND_1 = 2652,
    ACTION_OPEN_DOOR = 2674,
    ITEM_MOVE_BACKPACK = 2786,
    // ... outros efeitos
};

enum class SourceEffect_t : uint8_t {
    GLOBAL = 0, OWN = 1, OTHERS = 2, CREATURES = 3
};
```

### Funções Principais
```cpp
// Envio de som único
game.sendSingleSoundEffect(pos, SoundEffect_t::MELEE_ATK_SWORD, player);
// Envio de dois sons
game.sendDoubleSoundEffect(pos, SoundEffect_t::SPELL_FIREBALL_RUNE, SoundEffect_t::SPELL_EXPLOSION_RUNE, player);
// Protocolo
gameProtocol.sendSingleSoundEffect(pos, id, source);
```

## 📝 **Exemplo Prático em Lua**
```lua
local pos = Position(100, 100, 7)
pos:sendSingleSoundEffect(SoundEffect_t.SPELL_LIGHT_HEALING)
pos:sendDoubleSoundEffect(SoundEffect_t.MELEE_ATK_SWORD, SoundEffect_t.MELEE_ATK_CLUB)
player:sendSingleSoundEffect(SoundEffect_t.ACTION_NOTIFICATION, true)
```

## 🎮 **Categorias de Som**
- **Combate**: Ataques, magias, monstros
- **Ambiente**: Natureza, clima
- **Ações**: Portas, notificações
- **Itens**: Movimento, uso

## 🔄 **Fluxo de Dados**
1. Game chama sendSingleSoundEffect/sendDoubleSoundEffect
2. Protocolo envia pacote para cliente
3. Cliente reproduz som conforme categoria e fonte

## 🔧 **Troubleshooting**
- Verifique se o protocolo do cliente suporta sons
- Use SILENCE para não enviar som
- Categorize corretamente o SourceEffect_t

## 🚀 **Comparação com OTClient**
- Ambos suportam efeitos sonoros, mas o Canary centraliza o controle e categorização no servidor.

## 📈 **Benefícios**
- Flexibilidade e controle total dos sons
- Suporte a múltiplas categorias e fontes
- Integração fácil com scripts Lua

---
**Baseado na pesquisa Habdel**: [[../habdel/CANARY-009|CANARY-009: Sistema de Som]]