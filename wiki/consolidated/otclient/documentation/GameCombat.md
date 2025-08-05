# Sistema de Combate

Sistema completo de combate e mecânicas de luta

## 📋 Índice
1. [Visão Geral](#visão-geral)
2. [API C++](#api-c)
3. [API Lua](#api-lua)
4. [Exemplos](#exemplos)
5. [Melhores Práticas](#melhores-práticas)

## 🎯 Visão Geral

O sistema de combate gerencia ataques, defesas, dano e mecânicas de luta entre criaturas.

## 🔧 API C++

#### Nível Basic
```cpp
// Processamento de ataque
void Game::processAttack(Creature* attacker, Creature* target) {
    int damage = calculateDamage(attacker, target);
    target->takeDamage(damage);
}
```

#### Nível Intermediate
```cpp
// Processamento de ataque
void Game::processAttack(Creature* attacker, Creature* target) {
    int damage = calculateDamage(attacker, target);
    target->takeDamage(damage);
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
// Processamento de ataque
void Game::processAttack(Creature* attacker, Creature* target) {
    int damage = calculateDamage(attacker, target);
    target->takeDamage(damage);
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

## 🐍 API Lua

```lua
-- Função de ataque
function attack(target)
    -- Função: attack
    local damage = calculateDamage(player, target)
    target:takeDamage(damage)
    showDamageEffect(target, damage)
end
```

## 💡 Exemplos

```lua
-- Sistema de combate completo
    --  Sistema de combate completo (traduzido)
function onCombatStart(attacker, target)
    -- Função: onCombatStart
    startCombatAnimation(attacker)
    processAttack(attacker, target)
    updateCombatUI()
end
```

## ✅ Melhores Práticas

- Mantenha combate responsivo
- Use animações para feedback visual
- Implemente sistema de cooldowns

---

**Story ID**: GAME-006  
**Categoria**: GAME  
**Status**: ✅ Completo  
**Última Atualização**: 2025-07-29
