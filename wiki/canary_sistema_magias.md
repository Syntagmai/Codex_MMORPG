---
tags: [canary, sistema_magias, spells, vocações, vocations, magias, habdel_research]
type: wiki_page
status: active
priority: high
created: 2025-08-05
updated: 2025-08-05
aliases: [magias, spells, vocações, vocations, runas, runes]
---

# 🔮 Sistema de Magias - Canary

> [!info] **Baseado na Pesquisa Habdel**
> Esta página é baseada na pesquisa detalhada **[CANARY-012: Sistema de Combate](habdel/CANARY-012.md)** realizada com metodologia Habdel.

## 🎯 **Visão Geral**

O Sistema de Magias do Canary gerencia spells, vocações, runas e efeitos mágicos. É integrado ao sistema de combate e permite customização completa através de Lua.

## 🏗️ **Arquitetura do Sistema**

### **Estrutura de Arquivos**
```
canary/src/
├── creatures/combat/
│   ├── combat.hpp                 # Sistema de combate mágico
│   └── combat.cpp                 # Implementação
├── lua/functions/creatures/
│   └── combat/combat_functions.cpp # Funções Lua para magias
└── data/
    └── spells/                    # Scripts de magias
```

### **Componentes Principais**

#### **1. Sistema de Vocações**
- **Knight**: Especialista em combate físico
- **Paladin**: Combate à distância e suporte
- **Sorcerer**: Magias ofensivas poderosas
- **Druid**: Magias de cura e suporte

#### **2. Tipos de Magias**
- **Instant Spells**: Magias instantâneas
- **Rune Spells**: Magias através de runas
- **Conjure Spells**: Magias de conjuração
- **Charm Spells**: Magias de encantamento

## 🔧 **Implementação Prática**

### **Exemplo 1: Magia Instantânea**
```lua
-- Exemplo: Magia de fogo instantânea
local combat = Combat()
combat:setParameter(COMBAT_PARAM_TYPE, COMBAT_FIREDAMAGE)
combat:setParameter(COMBAT_PARAM_DAMAGE, 150)
combat:setParameter(COMBAT_PARAM_EFFECT, CONST_ME_FIREAREA)

function onCastSpell(creature, variant)
    return combat:execute(creature, variant)
end
```

### **Exemplo 2: Magia com Vocações**
```lua
-- Exemplo: Magia específica por vocação
function onCastSpell(creature, variant)
    local vocation = creature:getVocation()
    local damage = 100
    
    if vocation:getId() == VOCATION_SORCERER then
        damage = damage * 1.5
    elseif vocation:getId() == VOCATION_DRUID then
        damage = damage * 1.3
    end
    
    local combat = Combat()
    combat:setParameter(COMBAT_PARAM_DAMAGE, damage)
    return combat:execute(creature, variant)
end
```

### **Exemplo 3: Runa Customizada**
```lua
-- Exemplo: Runa de veneno customizada
local rune = Spell("rune")
function rune.onCastSpell(creature, variant)
    local target = variant:getPosition()
    local condition = Condition(CONDITION_POISON)
    condition:setParameter(CONDITION_PARAM_DELAYED, 1)
    condition:setParameter(CONDITION_PARAM_MINVALUE, 50)
    condition:setParameter(CONDITION_PARAM_MAXVALUE, 200)
    
    local tile = Tile(target)
    if tile then
        local creature = tile:getTopCreature()
        if creature then
            creature:addCondition(condition)
        end
    end
    return true
end
```

## 🎮 **Exemplos Práticos**

### **Magia de Cura**
```lua
local combat = Combat()
combat:setParameter(COMBAT_PARAM_TYPE, COMBAT_HEALING)
combat:setParameter(COMBAT_PARAM_EFFECT, CONST_ME_MAGIC_BLUE)
combat:setParameter(COMBAT_PARAM_AGGRESSIVE, 0)

function onCastSpell(creature, variant)
    local target = creature:getTarget()
    if target then
        local health = target:getHealth()
        local maxHealth = target:getMaxHealth()
        local heal = math.min(200, maxHealth - health)
        combat:setParameter(COMBAT_PARAM_DAMAGE, heal)
    end
    return combat:execute(creature, variant)
end
```

### **Magia de Buff**
```lua
function onCastSpell(creature, variant)
    local target = creature:getTarget()
    if target then
        local condition = Condition(CONDITION_ATTRIBUTES)
        condition:setParameter(CONDITION_PARAM_STAT_MAXHITPOINTS, 100)
        condition:setParameter(CONDITION_PARAM_STAT_MAXMANAPOINTS, 50)
        condition:setParameter(CONDITION_PARAM_TICKS, 60000)
        target:addCondition(condition)
    end
    return true
end
```

## 🔗 **Dependências e Integrações**

### **Dependências Principais**
- **Sistema de Combate**: Base para magias ofensivas
- **Sistema de Condições**: Para efeitos mágicos
- **Sistema de Vocações**: Modificadores de dano
- **Sistema de Items**: Runas e equipamentos mágicos

### **Integrações**
- **Sistema de Mana**: Consumo de mana por magia
- **Sistema de Cooldown**: Tempo entre magias
- **Sistema de Experiência**: Progressão de magias

## 📊 **Otimizações**

### **Performance**
- **Cache de Magias**: Resultados frequentes
- **Lazy Loading**: Carregamento sob demanda
- **Pool de Objetos**: Reutilização de objetos mágicos

## 🎯 **Casos de Uso**

### **1. Magias Ofensivas**
- Dano direto
- Dano em área
- Condições de dano

### **2. Magias de Suporte**
- Cura
- Buffs
- Debuffs

### **3. Magias de Utilidade**
- Teleporte
- Invisibilidade
- Proteções

## 🔧 **Como Implementar**

### **Passo 1: Definir Tipo de Magia**
```lua
local spell = Spell("instant")
```

### **Passo 2: Configurar Parâmetros**
```lua
spell:name("Fireball")
spell:words("exevo vis hur")
spell:level(20)
spell:mana(100)
```

### **Passo 3: Implementar Lógica**
```lua
function spell.onCastSpell(creature, variant)
    -- Lógica da magia
    return true
end
```

## 📚 **Referências Relacionadas**

- **[Sistema de Combate](canary_sistema_combate.md)** - Base para magias ofensivas
- **[Sistema de Monstros](canary_sistema_monstros.md)** - Alvos de magias
- **[Sistema de Itens](canary_sistema_itens.md)** - Runas e equipamentos

## 🎓 **Lição Educacional**

O Sistema de Magias demonstra como criar um sistema flexível de spells com:
1. **Modularidade**: Separação clara entre tipos de magia
2. **Extensibilidade**: Fácil adição de novas magias
3. **Performance**: Otimizações para magias frequentes
4. **Integração**: Conexão eficiente com outros sistemas

---

> [!tip] **Próximo Passo**
> Continue para **[Sistema de Monstros](canary_sistema_monstros.md)** para entender como os monstros usam magias e AI. 