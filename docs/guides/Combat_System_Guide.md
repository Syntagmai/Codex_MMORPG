
# Combat System Guide

<div class="info"> Este guia documenta o sistema completo de combate do OTClient, incluindo cálculos de dano, tipos de ataque, defesa, efeitos visuais e integração com o sistema de criaturas e itens.

## 📋 Índice
- [#Visão Geral](#Visão Geral.md)
- [#Tipos de Ataque](#Tipos de Ataque.md)
- [#Sistema de Dano](#Sistema de Dano.md)
- [#Sistema de Defesa](#Sistema de Defesa.md)
- [#Efeitos de Combate](#Efeitos de Combate.md)
- [#Sistema de Crítico](#Sistema de Crítico.md)
- [#Integração com Criaturas](#Integração com Criaturas.md)
- [#Performance e Otimização](#Performance e Otimização.md)
- [#Exemplos Práticos](#Exemplos Práticos.md)
- [#Melhores Práticas](#Melhores Práticas.md)

---

## 🎯 Visão Geral

O sistema de combate do OTClient oferece:

- **Cálculos Precisos**: Dano baseado em atributos e equipamentos
- **Tipos de Ataque**: Físico, mágico, distância e habilidades
- **Sistema de Defesa**: Armadura, escudos e resistências
- **Efeitos Visuais**: Animações e partículas de combate
- **Sistema de Crítico**: Golpes críticos e multiplicadores
- **Integração Completa**: Criaturas, itens e magias

### 🏗️ **Arquitetura do Sistema**

```
Sistema de Combate
   │
   ├─ Attack Engine
   │   ├─ Cálculo de dano
   │   ├─ Tipos de ataque
   │   └─ Modificadores
   │
   ├─ Defense System
   │   ├─ Armadura
   │   ├─ Resistências
   │   └─ Escudos
   │
   ├─ Visual Effects
   │   ├─ Animações de ataque
   │   ├─ Efeitos de dano
   │   └─ Partículas
   │
   └─ Integration
       ├─ Criaturas
       ├─ Itens
       └─ Magias
```

---

## ⚔️ Tipos de Ataque

### 🗡️ **Ataque Físico**

```lua
-- Ataque físico básico
function performPhysicalAttack(attacker, target, weapon)
    local baseDamage = calculateBaseDamage(attacker, weapon)
    local finalDamage = applyModifiers(baseDamage, attacker, target)
    
    -- Aplicar dano
    applyDamage(target, finalDamage, 'physical')
    
    -- Efeitos visuais
    showAttackAnimation(attacker, target)
    showDamageEffect(target, finalDamage, 'physical')
end

-- Calcular dano base
function calculateBaseDamage(attacker, weapon)
    local strength = attacker:getSkillLevel(SkillType.Fist)
    local weaponDamage = weapon:getAttack()
    
    return strength + weaponDamage
end

-- Aplicar modificadores
function applyModifiers(baseDamage, attacker, target)
    local modifiedDamage = baseDamage
    
    -- Modificador de força
    local strength = attacker:getSkillLevel(SkillType.Fist)
    modifiedDamage = modifiedDamage * (1 + strength * 0.01)
    
    -- Modificador de equipamento
    local equipmentBonus = getEquipmentAttackBonus(attacker)
    modifiedDamage = modifiedDamage + equipmentBonus
    
    -- Modificador de buffs
    local buffBonus = getAttackBuffBonus(attacker)
    modifiedDamage = modifiedDamage * (1 + buffBonus)
    
    return math.floor(modifiedDamage)
end
```

### 🔮 **Ataque Mágico**

```lua
-- Ataque mágico
function performMagicAttack(caster, target, spell)
    local baseDamage = calculateMagicDamage(caster, spell)
    local finalDamage = applyMagicModifiers(baseDamage, caster, target)
    
    -- Aplicar dano mágico
    applyDamage(target, finalDamage, 'magic')
    
    -- Efeitos mágicos
    showSpellAnimation(caster, target, spell)
    showMagicEffect(target, finalDamage, spell:getElement())
end

-- Calcular dano mágico
function calculateMagicDamage(caster, spell)
    local magicLevel = caster:getSkillLevel(SkillType.Magic)
    local spellPower = spell:getPower()
    
    return magicLevel * spellPower
end

-- Aplicar modificadores mágicos
function applyMagicModifiers(baseDamage, caster, target)
    local modifiedDamage = baseDamage
    
    -- Modificador de magic level
    local magicLevel = caster:getSkillLevel(SkillType.Magic)
    modifiedDamage = modifiedDamage * (1 + magicLevel * 0.02)
    
    -- Modificador de equipamento mágico
    local magicBonus = getMagicEquipmentBonus(caster)
    modifiedDamage = modifiedDamage + magicBonus
    
    -- Resistência mágica do alvo
    local magicResistance = target:getMagicResistance()
    modifiedDamage = modifiedDamage * (1 - magicResistance)
    
    return math.floor(modifiedDamage)
end
```

### 🏹 **Ataque à Distância**

```lua
-- Ataque à distância
function performRangedAttack(attacker, target, weapon)
    local baseDamage = calculateRangedDamage(attacker, weapon)
    local finalDamage = applyRangedModifiers(baseDamage, attacker, target)
    
    -- Verificar se está no range
    if isInRange(attacker, target, weapon:getRange()) then
        applyDamage(target, finalDamage, 'ranged')
        showRangedAttackAnimation(attacker, target, weapon)
        showRangedDamageEffect(target, finalDamage)
    else
        showOutOfRangeMessage(attacker)
    end
end

-- Calcular dano à distância
function calculateRangedDamage(attacker, weapon)
    local distance = attacker:getSkillLevel(SkillType.Distance)
    local weaponDamage = weapon:getAttack()
    
    return distance + weaponDamage
end

-- Aplicar modificadores de distância
function applyRangedModifiers(baseDamage, attacker, target)
    local modifiedDamage = baseDamage
    
    -- Modificador de distância
    local distance = attacker:getSkillLevel(SkillType.Distance)
    modifiedDamage = modifiedDamage * (1 + distance * 0.01)
    
    -- Modificador de munição
    local ammoBonus = getAmmoBonus(attacker)
    modifiedDamage = modifiedDamage + ammoBonus
    
    -- Modificador de range
    local rangeModifier = getRangeModifier(attacker, target)
    modifiedDamage = modifiedDamage * rangeModifier
    
    return math.floor(modifiedDamage)
end
```

---

## 🛡️ Sistema de Dano

### 💥 **Aplicação de Dano**

```lua
-- Aplicar dano a uma criatura
function applyDamage(target, damage, damageType)
    if not target or target:isDead() then
        return
    end
    
    -- Verificar imunidades
    if target:isImmuneTo(damageType) then
        showImmuneEffect(target)
        return
    end
    
    -- Calcular dano final
    local finalDamage = calculateFinalDamage(target, damage, damageType)
    
    -- Aplicar dano
    local currentHealth = target:getHealth()
    local newHealth = math.max(0, currentHealth - finalDamage)
    target:setHealth(newHealth)
    
    -- Efeitos visuais
    showDamageEffect(target, finalDamage, damageType)
    
    -- Verificar morte
    if newHealth <= 0 then
        handleCreatureDeath(target)
    end
    
    -- Eventos
    triggerDamageEvent(target, finalDamage, damageType)
end

-- Calcular dano final
function calculateFinalDamage(target, damage, damageType)
    local finalDamage = damage
    
    -- Redução por armadura
    local armorReduction = getArmorReduction(target, damageType)
    finalDamage = finalDamage * (1 - armorReduction)
    
    -- Redução por escudo
    local shieldReduction = getShieldReduction(target, damageType)
    finalDamage = finalDamage * (1 - shieldReduction)
    
    -- Redução por resistências
    local resistanceReduction = getResistanceReduction(target, damageType)
    finalDamage = finalDamage * (1 - resistanceReduction)
    
    -- Dano mínimo
    finalDamage = math.max(1, finalDamage)
    
    return math.floor(finalDamage)
end
```

### 🎯 **Tipos de Dano**

```lua
-- Tipos de dano disponíveis
local DAMAGE_TYPES = {
    PHYSICAL = 'physical',
    MAGIC = 'magic',
    FIRE = 'fire',
    ICE = 'ice',
    EARTH = 'earth',
    ENERGY = 'energy',
    DEATH = 'death',
    HOLY = 'holy',
    RANGED = 'ranged'
}

-- Configurações de dano por tipo
local DAMAGE_CONFIG = {
    [DAMAGE_TYPES.PHYSICAL] = {
        armorReduction = 0.3,
        shieldReduction = 0.2,
        resistanceReduction = 0.1
    },
    [DAMAGE_TYPES.MAGIC] = {
        armorReduction = 0.1,
        shieldReduction = 0.3,
        resistanceReduction = 0.4
    },
    [DAMAGE_TYPES.FIRE] = {
        armorReduction = 0.2,
        shieldReduction = 0.1,
        resistanceReduction = 0.5
    },
    [DAMAGE_TYPES.ICE] = {
        armorReduction = 0.2,
        shieldReduction = 0.1,
        resistanceReduction = 0.5
    },
    [DAMAGE_TYPES.EARTH] = {
        armorReduction = 0.3,
        shieldReduction = 0.2,
        resistanceReduction = 0.3
    },
    [DAMAGE_TYPES.ENERGY] = {
        armorReduction = 0.1,
        shieldReduction = 0.4,
        resistanceReduction = 0.4
    },
    [DAMAGE_TYPES.DEATH] = {
        armorReduction = 0.0,
        shieldReduction = 0.0,
        resistanceReduction = 0.6
    },
    [DAMAGE_TYPES.HOLY] = {
        armorReduction = 0.1,
        shieldReduction = 0.2,
        resistanceReduction = 0.5
    },
    [DAMAGE_TYPES.RANGED] = {
        armorReduction = 0.2,
        shieldReduction = 0.3,
        resistanceReduction = 0.1
    }
}
```

---

## 🛡️ Sistema de Defesa

### 🛡️ **Armadura**

```lua
-- Obter redução de armadura
function getArmorReduction(target, damageType)
    local armor = target:getArmor()
    local config = DAMAGE_CONFIG[damageType]
    
    if not config then
        return 0
    end
    
    local baseReduction = config.armorReduction
    local armorModifier = armor / 100  -- Armadura de 0-100
    
    return baseReduction * armorModifier
end

-- Calcular armadura total
function calculateTotalArmor(creature)
    local baseArmor = creature:getBaseArmor()
    local equipmentArmor = getEquipmentArmor(creature)
    local buffArmor = getBuffArmor(creature)
    
    return baseArmor + equipmentArmor + buffArmor
end

-- Obter armadura do equipamento
function getEquipmentArmor(creature)
    local totalArmor = 0
    
    local equipment = creature:getEquipment()
    for slot, item in pairs(equipment) do
        if item and item:isArmor() then
            totalArmor = totalArmor + item:getArmor()
        end
    end
    
    return totalArmor
end
```

### 🛡️ **Escudos**

```lua
-- Obter redução de escudo
function getShieldReduction(target, damageType)
    local shield = target:getShield()
    local config = DAMAGE_CONFIG[damageType]
    
    if not config then
        return 0
    end
    
    local baseReduction = config.shieldReduction
    local shieldModifier = shield / 100  -- Escudo de 0-100
    
    return baseReduction * shieldModifier
end

-- Calcular escudo total
function calculateTotalShield(creature)
    local baseShield = creature:getBaseShield()
    local equipmentShield = getEquipmentShield(creature)
    local buffShield = getBuffShield(creature)
    
    return baseShield + equipmentShield + buffShield
end

-- Obter escudo do equipamento
function getEquipmentShield(creature)
    local totalShield = 0
    
    local equipment = creature:getEquipment()
    for slot, item in pairs(equipment) do
        if item and item:isShield() then
            totalShield = totalShield + item:getShield()
        end
    end
    
    return totalShield
end
```

### 🛡️ **Resistências**

```lua
-- Obter redução de resistência
function getResistanceReduction(target, damageType)
    local resistance = target:getResistance(damageType)
    local config = DAMAGE_CONFIG[damageType]
    
    if not config then
        return 0
    end
    
    local baseReduction = config.resistanceReduction
    local resistanceModifier = resistance / 100  -- Resistência de 0-100
    
    return baseReduction * resistanceModifier
end

-- Obter resistência específica
function getResistance(creature, damageType)
    local baseResistance = creature:getBaseResistance(damageType)
    local equipmentResistance = getEquipmentResistance(creature, damageType)
    local buffResistance = getBuffResistance(creature, damageType)
    
    return baseResistance + equipmentResistance + buffResistance
end

-- Obter resistência do equipamento
function getEquipmentResistance(creature, damageType)
    local totalResistance = 0
    
    local equipment = creature:getEquipment()
    for slot, item in pairs(equipment) do
        if item then
            local itemResistance = item:getResistance(damageType)
            totalResistance = totalResistance + itemResistance
        end
    end
    
    return totalResistance
end
```

---

## ⚡ Efeitos de Combate

### 🎭 **Animações de Ataque**

```lua
-- Mostrar animação de ataque
function showAttackAnimation(attacker, target)
    -- Animação do atacante
    attacker:setAnimation(AnimationType.Attack)
    
    -- Efeito de movimento
    local attackEffect = Effect.create()
    attackEffect:setId(1)  -- ID do efeito de ataque
    attackEffect:setPosition(attacker:getPosition())
    g_map.addThing(attackEffect, attacker:getPosition())
    
    -- Remover efeito após animação
    scheduleEvent(function()
        g_map.removeThing(attackEffect)
    end, 1000)
end

-- Mostrar animação de spell
function showSpellAnimation(caster, target, spell)
    -- Animação do caster
    caster:setAnimation(AnimationType.Spell)
    
    -- Efeito de spell
    local spellEffect = Effect.create()
    spellEffect:setId(spell:getEffectId())
    spellEffect:setPosition(caster:getPosition())
    g_map.addThing(spellEffect, caster:getPosition())
    
    -- Efeito no alvo
    scheduleEvent(function()
        local targetEffect = Effect.create()
        targetEffect:setId(spell:getTargetEffectId())
        targetEffect:setPosition(target:getPosition())
        g_map.addThing(targetEffect, target:getPosition())
        
        scheduleEvent(function()
            g_map.removeThing(targetEffect)
        end, 2000)
    end, 500)
    
    -- Remover efeito do caster
    scheduleEvent(function()
        g_map.removeThing(spellEffect)
    end, 1000)
end

-- Mostrar animação de ataque à distância
function showRangedAttackAnimation(attacker, target, weapon)
    -- Animação do atacante
    attacker:setAnimation(AnimationType.RangedAttack)
    
    -- Projétil
    local projectile = Missile.create()
    projectile:setId(weapon:getProjectileId())
    projectile:setPosition(attacker:getPosition())
    projectile:setTarget(target:getPosition())
    
    g_map.addThing(projectile, attacker:getPosition())
    
    -- Remover projétil ao atingir
    scheduleEvent(function()
        g_map.removeThing(projectile)
    end, 1000)
end
```

### 💥 **Efeitos de Dano**

```lua
-- Mostrar efeito de dano
function showDamageEffect(target, damage, damageType)
    -- Texto animado de dano
    local damageText = AnimatedText.create()
    damageText:setText(tostring(damage))
    
    -- Cor baseada no tipo de dano
    local color = getDamageColor(damageType)
    damageText:setColor(color)
    
    -- Posição
    local targetPos = target:getPosition()
    damageText:setOffset({x = 0, y = -30})
    
    g_map.addAnimatedText(damageText, targetPos)
    
    -- Efeito visual baseado no tipo
    local damageEffect = Effect.create()
    damageEffect:setId(getDamageEffectId(damageType))
    damageEffect:setPosition(targetPos)
    g_map.addThing(damageEffect, targetPos)
    
    -- Remover efeito
    scheduleEvent(function()
        g_map.removeThing(damageEffect)
    end, 2000)
end

-- Obter cor do dano
function getDamageColor(damageType)
    local colors = {
        [DAMAGE_TYPES.PHYSICAL] = '#FFFFFF',
        [DAMAGE_TYPES.MAGIC] = '#FF00FF',
        [DAMAGE_TYPES.FIRE] = '#FF0000',
        [DAMAGE_TYPES.ICE] = '#00FFFF',
        [DAMAGE_TYPES.EARTH] = '#8B4513',
        [DAMAGE_TYPES.ENERGY] = '#FFFF00',
        [DAMAGE_TYPES.DEATH] = '#800080',
        [DAMAGE_TYPES.HOLY] = '#FFD700',
        [DAMAGE_TYPES.RANGED] = '#FFA500'
    }
    
    return colors[damageType] or '#FFFFFF'
end

-- Obter ID do efeito de dano
function getDamageEffectId(damageType)
    local effectIds = {
        [DAMAGE_TYPES.PHYSICAL] = 1,
        [DAMAGE_TYPES.MAGIC] = 2,
        [DAMAGE_TYPES.FIRE] = 3,
        [DAMAGE_TYPES.ICE] = 4,
        [DAMAGE_TYPES.EARTH] = 5,
        [DAMAGE_TYPES.ENERGY] = 6,
        [DAMAGE_TYPES.DEATH] = 7,
        [DAMAGE_TYPES.HOLY] = 8,
        [DAMAGE_TYPES.RANGED] = 9
    }
    
    return effectIds[damageType] or 1
end
```

---

## ⚡ Sistema de Crítico

### 🎯 **Cálculo de Crítico**

```lua
-- Verificar se é crítico
function isCriticalHit(attacker, target)
    local criticalChance = calculateCriticalChance(attacker)
    local random = math.random(1, 100)
    
    return random <= criticalChance
end

-- Calcular chance de crítico
function calculateCriticalChance(attacker)
    local baseChance = 5  -- 5% base
    
    -- Modificador de equipamento
    local equipmentBonus = getCriticalEquipmentBonus(attacker)
    baseChance = baseChance + equipmentBonus
    
    -- Modificador de buffs
    local buffBonus = getCriticalBuffBonus(attacker)
    baseChance = baseChance + buffBonus
    
    -- Modificador de skills
    local skillBonus = getCriticalSkillBonus(attacker)
    baseChance = baseChance + skillBonus
    
    return math.min(50, baseChance)  -- Máximo 50%
end

-- Calcular multiplicador de crítico
function calculateCriticalMultiplier(attacker)
    local baseMultiplier = 1.5  -- 50% extra
    
    -- Modificador de equipamento
    local equipmentBonus = getCriticalMultiplierBonus(attacker)
    baseMultiplier = baseMultiplier + equipmentBonus
    
    -- Modificador de buffs
    local buffBonus = getCriticalMultiplierBuffBonus(attacker)
    baseMultiplier = baseMultiplier + buffBonus
    
    return math.min(3.0, baseMultiplier)  -- Máximo 300%
end
```

### 💥 **Aplicação de Crítico**

```lua
-- Aplicar dano com verificação de crítico
function applyDamageWithCritical(attacker, target, damage, damageType)
    local finalDamage = damage
    
    -- Verificar crítico
    if isCriticalHit(attacker, target) then
        local criticalMultiplier = calculateCriticalMultiplier(attacker)
        finalDamage = math.floor(damage * criticalMultiplier)
        
        -- Efeitos de crítico
        showCriticalEffect(target, finalDamage, damageType)
        playCriticalSound()
    else
        -- Dano normal
        showDamageEffect(target, finalDamage, damageType)
    end
    
    -- Aplicar dano
    applyDamage(target, finalDamage, damageType)
end

-- Mostrar efeito de crítico
function showCriticalEffect(target, damage, damageType)
    -- Texto de crítico
    local criticalText = AnimatedText.create()
    criticalText:setText(tostring(damage) .. '!')
    criticalText:setColor('#FF0000')
    criticalText:setFont('verdana-16px-bold')
    criticalText:setOffset({x = 0, y = -40})
    
    local targetPos = target:getPosition()
    g_map.addAnimatedText(criticalText, targetPos)
    
    -- Efeito visual de crítico
    local criticalEffect = Effect.create()
    criticalEffect:setId(10)  -- ID do efeito de crítico
    criticalEffect:setPosition(targetPos)
    g_map.addThing(criticalEffect, targetPos)
    
    -- Remover efeito
    scheduleEvent(function()
        g_map.removeThing(criticalEffect)
    end, 3000)
end

-- Tocar som de crítico
function playCriticalSound()
    g_sounds.playSoundFile('/sounds/combat/critical.ogg')
end
```

---

## 👥 Integração com Criaturas

### 🎯 **Sistema de Combate de Criaturas**

```lua
-- Setup de combate para criatura
function setupCreatureCombat(creature)
    -- Configurar eventos de combate
    creature.onAttack = function(attacker, target)
        performCreatureAttack(attacker, target)
    end
    
    creature.onDamaged = function(creature, damage, damageType)
        handleCreatureDamage(creature, damage, damageType)
    end
    
    creature.onDeath = function(creature)
        handleCreatureDeath(creature)
    end
end

-- Ataque de criatura
function performCreatureAttack(attacker, target)
    local weapon = attacker:getWeapon()
    local damage = calculateCreatureDamage(attacker, weapon)
    
    -- Verificar se é crítico
    if isCriticalHit(attacker, target) then
        local criticalMultiplier = calculateCriticalMultiplier(attacker)
        damage = math.floor(damage * criticalMultiplier)
        showCriticalEffect(target, damage, 'physical')
    else
        showDamageEffect(target, damage, 'physical')
    end
    
    applyDamage(target, damage, 'physical')
end

-- Calcular dano de criatura
function calculateCreatureDamage(creature, weapon)
    local baseDamage = creature:getAttack()
    local weaponDamage = weapon and weapon:getAttack() or 0
    
    return baseDamage + weaponDamage
end

-- Lidar com dano de criatura
function handleCreatureDamage(creature, damage, damageType)
    -- Efeitos visuais
    showDamageEffect(creature, damage, damageType)
    
    -- Sons de dano
    playDamageSound(creature, damageType)
    
    -- Verificar status
    if creature:getHealth() <= creature:getMaxHealth() * 0.2 then
        creature:setStatus(CreatureStatus.Blood)
    end
end

-- Lidar com morte de criatura
function handleCreatureDeath(creature)
    -- Efeito de morte
    showDeathEffect(creature)
    
    -- Som de morte
    playDeathSound(creature)
    
    -- Loot
    generateLoot(creature)
    
    -- Experiência
    giveExperience(creature)
    
    -- Remover criatura
    scheduleEvent(function()
        g_map.removeCreature(creature)
    end, 2000)
end
```

---

## ⚡ Performance e Otimização

### 🚀 **Otimizações de Combate**

```lua
-- Cache de cálculos de dano
local DamageCache = {}
DamageCache.calculations = {}

function getCachedDamage(attacker, target, damageType)
    local key = attacker:getId() .. '_' .. target:getId() .. '_' .. damageType
    
    if DamageCache.calculations[key] then
        local cached = DamageCache.calculations[key]
        if g_clock.millis() - cached.timestamp < 1000 then
            return cached.damage
        end
    end
    
    local damage = calculateDamage(attacker, target, damageType)
    
    DamageCache.calculations[key] = {
        damage = damage,
        timestamp = g_clock.millis()
    }
    
    return damage
end

-- Limpar cache periodicamente
scheduleEvent(function()
    local currentTime = g_clock.millis()
    for key, cached in pairs(DamageCache.calculations) do
        if currentTime - cached.timestamp > 5000 then
            DamageCache.calculations[key] = nil
        end
    end
end, 5000)

-- Pool de efeitos de combate
local CombatEffectPool = {}
CombatEffectPool.effects = {}

function getCombatEffect()
    if #CombatEffectPool.effects > 0 then
        return table.remove(CombatEffectPool.effects)
    else
        return Effect.create()
    end
end

function releaseCombatEffect(effect)
    effect:setId(0)
    effect:setPosition({x = 0, y = 0, z = 0})
    table.insert(CombatEffectPool.effects, effect)
end
```

### 🎯 **Configurações de Performance**

```lua
-- Desabilitar efeitos em configurações baixas
function shouldShowCombatEffects()
    local quality = g_settings.getString("graphics.quality")
    local fps = g_app.getFps()
    
    return quality ~= "low" and fps > 30
end

-- Configurar efeitos condicionalmente
function showConditionalCombatEffect(target, damage, damageType)
    if shouldShowCombatEffects() then
        showDamageEffect(target, damage, damageType)
    else
        -- Apenas texto simples
        local text = AnimatedText.create()
        text:setText(tostring(damage))
        text:setColor('#FFFFFF')
        g_map.addAnimatedText(text, target:getPosition())
    end
end
```

---

### 🎮 **Sistema de Combate Completo**

```lua
-- Sistema de combate principal
local CombatSystem = {}

function CombatSystem.init()
    -- Conectar eventos de combate
    connect(g_game, {
        onCreatureAttack = CombatSystem.handleAttack,
        onCreatureDamaged = CombatSystem.handleDamage,
        onCreatureDeath = CombatSystem.handleDeath
    })
    
    -- Setup de criaturas existentes
    local creatures = g_map.getCreatures()
    for _, creature in ipairs(creatures) do
        setupCreatureCombat(creature)
    end
end

function CombatSystem.handleAttack(attacker, target)
    local weapon = attacker:getWeapon()
    local damageType = getDamageType(weapon)
    
    local damage = getCachedDamage(attacker, target, damageType)
    
    if isCriticalHit(attacker, target) then
        local criticalMultiplier = calculateCriticalMultiplier(attacker)
        damage = math.floor(damage * criticalMultiplier)
        showCriticalEffect(target, damage, damageType)
    else
        showConditionalCombatEffect(target, damage, damageType)
    end
    
    applyDamage(target, damage, damageType)
end

function CombatSystem.handleDamage(creature, damage, damageType)
    showConditionalCombatEffect(creature, damage, damageType)
    
    -- Verificar status de sangue
    if creature:getHealth() <= creature:getMaxHealth() * 0.2 then
        creature:setStatus(CreatureStatus.Blood)
    end
end

function CombatSystem.handleDeath(creature)
    showDeathEffect(creature)
    playDeathSound(creature)
    
    -- Gerar loot
    generateLoot(creature)
    
    -- Dar experiência
    giveExperience(creature)
    
    -- Remover criatura
    scheduleEvent(function()
        g_map.removeCreature(creature)
    end, 2000)
end

-- Obter tipo de dano da arma
function getDamageType(weapon)
    if not weapon then
        return DAMAGE_TYPES.PHYSICAL
    end
    
    local weaponType = weapon:getType()
    
    if weaponType == 'sword' or weaponType == 'axe' or weaponType == 'club' then
        return DAMAGE_TYPES.PHYSICAL
    elseif weaponType == 'wand' or weaponType == 'rod' then
        return DAMAGE_TYPES.MAGIC
    elseif weaponType == 'bow' or weaponType == 'crossbow' then
        return DAMAGE_TYPES.RANGED
    else
        return DAMAGE_TYPES.PHYSICAL
    end
end
```

### 🎨 **Sistema de Efeitos de Combate**

```lua
-- Sistema de efeitos de combate
local CombatEffects = {}

function CombatEffects.showAttackEffect(attacker, target)
    -- Efeito de movimento do atacante
    local attackEffect = getCombatEffect()
    attackEffect:setId(1)
    attackEffect:setPosition(attacker:getPosition())
    g_map.addThing(attackEffect, attacker:getPosition())
    
    -- Efeito de impacto no alvo
    scheduleEvent(function()
        local impactEffect = getCombatEffect()
        impactEffect:setId(2)
        impactEffect:setPosition(target:getPosition())
        g_map.addThing(impactEffect, target:getPosition())
        
        scheduleEvent(function()
            releaseCombatEffect(impactEffect)
        end, 1000)
    end, 500)
    
    -- Remover efeito do atacante
    scheduleEvent(function()
        releaseCombatEffect(attackEffect)
    end, 1000)
end

function CombatEffects.showSpellEffect(caster, target, spell)
    -- Efeito de casting
    local castEffect = getCombatEffect()
    castEffect:setId(spell:getCastEffectId())
    castEffect:setPosition(caster:getPosition())
    g_map.addThing(castEffect, caster:getPosition())
    
    -- Efeito de projétil
    scheduleEvent(function()
        local projectile = Missile.create()
        projectile:setId(spell:getProjectileId())
        projectile:setPosition(caster:getPosition())
        projectile:setTarget(target:getPosition())
        g_map.addThing(projectile, caster:getPosition())
        
        scheduleEvent(function()
            g_map.removeThing(projectile)
        end, 1000)
    end, 300)
    
    -- Efeito de impacto
    scheduleEvent(function()
        local impactEffect = getCombatEffect()
        impactEffect:setId(spell:getImpactEffectId())
        impactEffect:setPosition(target:getPosition())
        g_map.addThing(impactEffect, target:getPosition())
        
        scheduleEvent(function()
            releaseCombatEffect(impactEffect)
        end, 2000)
    end, 800)
    
    -- Remover efeito de casting
    scheduleEvent(function()
        releaseCombatEffect(castEffect)
    end, 1000)
end

function CombatEffects.showDeathEffect(creature)
    -- Efeito de morte
    local deathEffect = getCombatEffect()
    deathEffect:setId(3)
    deathEffect:setPosition(creature:getPosition())
    g_map.addThing(deathEffect, creature:getPosition())
    
    -- Remover efeito
    scheduleEvent(function()
        releaseCombatEffect(deathEffect)
    end, 3000)
end
```

---

## ✅ Melhores Práticas

### 🎯 **Uso Eficiente do Sistema**

```lua
-- ✅ BOM: Usar cache de cálculos
local damage = getCachedDamage(attacker, target, damageType)

-- ✅ BOM: Usar pool de efeitos
local effect = getCombatEffect()
-- ... usar efeito ...
releaseCombatEffect(effect)

-- ✅ BOM: Verificar performance
if shouldShowCombatEffects() then
    showDamageEffect(target, damage, damageType)
end

-- ❌ EVITE: Calcular dano constantemente
function onAttack(attacker, target)
    local damage = calculateDamage(attacker, target)  -- Sem cache
end

-- ❌ EVITE: Criar muitos efeitos
for i = 1, 100 do
    local effect = Effect.create()  -- Muito custoso
end
```

### 🔧 **Configuração Adequada**

```lua
-- ✅ BOM: Usar constantes para configurações
local COMBAT_CONFIG = {
    CRITICAL_BASE_CHANCE = 5,
    CRITICAL_BASE_MULTIPLIER = 1.5,
    MAX_CRITICAL_CHANCE = 50,
    MAX_CRITICAL_MULTIPLIER = 3.0,
    DAMAGE_MIN = 1
}

-- ✅ BOM: Validar dados adequadamente
function applyDamage(target, damage, damageType)
    if not target or target:isDead() then
        return
    end
    
    if not DAMAGE_CONFIG[damageType] then
        damageType = DAMAGE_TYPES.PHYSICAL
    end
    
    local finalDamage = math.max(COMBAT_CONFIG.DAMAGE_MIN, damage)
    -- ... aplicar dano ...
end

-- ✅ BOM: Limpar recursos adequadamente
function cleanupCombatSystem()
    -- Limpar cache
    DamageCache.calculations = {}
    
    -- Limpar pool de efeitos
    for _, effect in ipairs(CombatEffectPool.effects) do
        effect:destroy()
    end
    CombatEffectPool.effects = {}
end
```

### 🎨 **Design Consistente**

```lua
-- ✅ BOM: Usar tipos de dano padronizados
local DAMAGE_TYPES = {
    PHYSICAL = 'physical',
    MAGIC = 'magic',
    FIRE = 'fire',
    ICE = 'ice',
    EARTH = 'earth',
    ENERGY = 'energy',
    DEATH = 'death',
    HOLY = 'holy',
    RANGED = 'ranged'
}

-- ✅ BOM: Usar configurações consistentes
local DAMAGE_CONFIG = {
    [DAMAGE_TYPES.PHYSICAL] = {
        armorReduction = 0.3,
        shieldReduction = 0.2,
        resistanceReduction = 0.1
    }
    -- ... outras configurações ...
}

-- ✅ BOM: Funções padronizadas
function calculateStandardDamage(attacker, target, damageType)
    local baseDamage = getBaseDamage(attacker)
    local modifiers = getDamageModifiers(attacker, target, damageType)
    return math.floor(baseDamage * modifiers)
end

function applyStandardDamage(target, damage, damageType)
    local finalDamage = calculateFinalDamage(target, damage, damageType)
    applyDamage(target, finalDamage, damageType)
end
```

O sistema de combate do OTClient oferece ferramentas poderosas para criar experiências de combate ricas e responsivas. Use estas práticas para garantir performance e consistência em suas aplicações. 
> - [Getting_Started_Guide](Getting_Started_Guide.md) - Comece aqui
> - [Module_System_Guide](Module_System_Guide.md) - Sistema de módulos
> - [UI_System_Guide](UI_System_Guide.md) - Interface do usuário
> - [Lua_API_Reference](Lua_API_Reference.md) - Referência da API

---

## 🔗 **Integração com Canary**

### **Lado Cliente (OTClient)**
- Renderização e interface do usuário
- Processamento de entrada do jogador
- Sincronização de estado local

### **Lado Servidor (Canary)**
- [Ver lógica de jogo no Canary Wiki](https://canary-wiki-url/game-logic)
- Validação de ações do jogador
- Gerenciamento de estado do mundo

### **Sincronização Compartilhada**
- [Protocolo de sincronização](https://shared-specs-url/sync)
- [Validação de estado](https://shared-specs-url/validation)
- [Testes de sincronização](https://canary-wiki-url/sync-tests)

<div class="info"> **Nota de Integração**
> Este sistema sincroniza o estado do jogo entre cliente e servidor.
> Para desenvolvimento, consulte a lógica de jogo do Canary.

---

<div class="success"> **Navegação**
> **📚 Documentos Relacionados:**
> - [Getting_Started_Guide](Getting_Started_Guide.md) - Comece aqui
> - [Module_System_Guide](Module_System_Guide.md) - Sistema de módulos
> - [UI_System_Guide](UI_System_Guide.md) - Interface do usuário
> - [Lua_API_Reference](Lua_API_Reference.md) - API completa
> 
> **🔗 Navegação Rápida:**
> - [Wiki_Index](Wiki_Index.md) - Voltar ao índice
> - [Cheat_Sheet](Cheat_Sheet.md) - Referência rápida
> - [Debug_System_Guide](Debug_System_Guide.md) - Debugging

