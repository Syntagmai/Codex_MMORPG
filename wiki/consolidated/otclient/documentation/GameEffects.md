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

#### Nível Basic
```cpp
// Criação de efeito de partículas
EffectPtr effect = EffectManager::createEffect("fire");
effect->setPosition(position);
effect->start();
```

#### Nível Intermediate
```cpp
// Criação de efeito de partículas
EffectPtr effect = EffectManager::createEffect("fire");
effect->setPosition(position);
effect->start();
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
// Criação de efeito de partículas
EffectPtr effect = EffectManager::createEffect("fire");
effect->setPosition(position);
effect->start();
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

#### Nível Basic
```lua
-- Efeito de explosão
local effect = g_effects.createEffect("explosion")
effect:setPosition(player:getPosition())
effect:start()
```

#### Nível Intermediate
```lua
-- Efeito de explosão
local effect = g_effects.createEffect("explosion")
effect:setPosition(player:getPosition())
effect:start()
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```lua
-- Efeito de explosão
local effect = g_effects.createEffect("explosion")
effect:setPosition(player:getPosition())
effect:start()
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

## 💡 Exemplos

```lua
-- Sistema de efeitos completo
    --  Sistema de efeitos completo (traduzido)
function onSpellCast(spell)
    -- Função: onSpellCast
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

