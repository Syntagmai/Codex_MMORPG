# Sistema de Efeitos

Sistema de efeitos visuais e sonoros para o jogo

## 📋 Índice
1. [Visão Geral](#visão-geral)
2. [API C++](#api-c)
3. [API Lua](#api-lua)
4. [Exemplos](#exemplos)
5. [Melhores Práticas](#melhores-práticas)

## 🎯 Visão Geral

O sistema de efeitos gerencia partículas, animações especiais e efeitos sonoros para criar imersão no jogo.

## 🔧 API C++

```cpp
// Criação de efeito de partículas
EffectPtr effect = EffectManager::createEffect("fire");
effect->setPosition(position);
effect->start();
```

## 🐍 API Lua

```lua
-- Efeito de explosão
local effect = g_effects.createEffect("explosion")
effect:setPosition(player:getPosition())
effect:start()
```

## 💡 Exemplos

```lua
-- Sistema de efeitos completo
function onSpellCast(spell)
    local effect = g_effects.createEffect(spell.effectName)
    effect:setPosition(spell.target)
    effect:start()
end
```

## ✅ Melhores Práticas

- Otimize efeitos para performance
- Use pooling para efeitos frequentes
- Considere diferentes dispositivos

---

**Story ID**: GAME-005  
**Categoria**: GAME  
**Status**: ✅ Completo  
**Última Atualização**: 2025-07-29
