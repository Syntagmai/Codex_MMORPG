---
tags: [canary_lesson, combat_system, weapons, conditions, chain_combat, game_development]
type: lesson
status: published
priority: high
created: 2025-01-27
target: canary
---

# CANARY-012: Sistema de Combate - Lição Educacional

## 🎯 **Objetivo da Lição**
Compreender o sistema de combate do Canary, sua arquitetura complexa, implementação e uso prático no desenvolvimento de servidores MMORPG.

## 📚 **Teoria**

### **O que é o Sistema de Combate?**
O Sistema de Combate do Canary é responsável por gerenciar todas as interações de combate no servidor, desde ataques básicos até magias complexas, incluindo sistema de condições, armas e áreas de efeito.

### **Conceitos Fundamentais**

#### **1. Combate Centralizado**
- Todas as ações de combate passam pelo sistema central
- Validação unificada de regras e permissões
- Controle consistente de mecânicas

#### **2. Sistema de Callbacks**
- Permite customização extensiva via Lua
- Callbacks para cálculo de dano, áreas e alvos
- Flexibilidade para implementações customizadas

#### **3. Cálculo de Dano**
- Múltiplas fórmulas para diferentes tipos de combate
- Sistema de dano primário e secundário
- Suporte a críticos e multiplicadores

#### **4. Condições**
- Sistema temporal para efeitos contínuos
- Hierarquia flexível de condições
- Execução baseada em ticks

#### **5. Áreas de Efeito**
- Sistema para combate em área
- Matrizes de área configuráveis
- Suporte a diferentes formatos

#### **6. Chain Combat**
- Combate em cadeia entre múltiplos alvos
- Algoritmo de seleção de alvos inteligente
- Sistema de delay configurável

### **Arquitetura do Sistema**

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Combat Class  │    │  Condition      │    ┌  Weapon System  │
│                 │    │  System         │    │                 │
│ doCombatHealth()│    │                 │    │ WeaponMelee     │
│ doCombatMana()  │    │ ConditionDamage │    │ WeaponDistance  │
│ doCombatChain() │    │ ConditionSpeed  │    │ WeaponWand      │
│ canDoCombat()   │    │ ConditionFeared │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  AreaCombat     │    │  Callbacks      │    ┌  Lua Functions  │
│                 │    │                 │    │                 │
│ getList()       │    │ ValueCallback   │    │ Combat()        │
│ setupArea()     │    │ TileCallback    │    │ setParameter()  │
│ MatrixArea      │    │ TargetCallback  │    │ setFormula()    │
│                 │    │ ChainCallback   │    │ execute()       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 💻 **Exemplos Práticos**

### **1. Criando um Combate Básico**

```lua
-- Criar combate de fogo
    --  Criar combate de fogo (traduzido)
local combat = Combat()
combat:setParameter(COMBAT_PARAM_TYPE, COMBAT_FIREDAMAGE)
combat:setParameter(COMBAT_PARAM_EFFECT, CONST_ME_FIREAREA)
combat:setParameter(COMBAT_PARAM_DISTANCEEFFECT, CONST_ANI_FIRE)

-- Configurar fórmula de dano
combat:setFormula(COMBAT_FORMULA_LEVELMAGIC, 5, 5, 10, 10)

-- Executar combate
    --  Executar combate (traduzido)
combat:execute(caster, target)
```

### **2. Combate com Condições**

```lua
-- Criar combate de veneno
    --  Criar combate de veneno (traduzido)
local combat = Combat()
combat:setParameter(COMBAT_PARAM_TYPE, COMBAT_EARTHDAMAGE)
combat:setParameter(COMBAT_PARAM_EFFECT, CONST_ME_GREEN_RINGS)

-- Adicionar condição de veneno
local condition = Condition(CONDITION_POISON)
condition:setParameter(CONDITION_PARAM_DELAYED, 1)
condition:setParameter(CONDITION_PARAM_MINVALUE, 50)
condition:setParameter(CONDITION_PARAM_MAXVALUE, 100)
condition:setParameter(CONDITION_PARAM_STARTVALUE, 50)
condition:setParameter(CONDITION_PARAM_TICKINTERVAL, 4000)
condition:setParameter(CONDITION_PARAM_FORCEUPDATE, true)

combat:addCondition(condition)
combat:execute(caster, target)
```

### **3. Combate em Área**

```lua
-- Criar área de combate
local area = {
    {0, 1, 0},
    {1, 3, 1},
    {0, 1, 0}
}

-- Configurar combate
    --  Configurar combate (traduzido)
local combat = Combat()
combat:setParameter(COMBAT_PARAM_TYPE, COMBAT_ICEDAMAGE)
combat:setParameter(COMBAT_PARAM_EFFECT, CONST_ME_ICEAREA)
combat:setArea(createCombatArea(area))

-- Executar combate
    --  Executar combate (traduzido)
combat:execute(caster, position)
```

### **4. Chain Combat**

```lua
-- Configurar chain combat
    --  Configurar chain combat (traduzido)
local combat = Combat()
combat:setParameter(COMBAT_PARAM_TYPE, COMBAT_ENERGYDAMAGE)
combat:setParameter(COMBAT_PARAM_EFFECT, CONST_ME_ENERGYAREA)

-- Configurar chain
    --  Configurar chain (traduzido)
combat:setChainCallback(3, 3, true) -- 3 alvos, distância 3, backtracking

combat:execute(caster, target)
```

### **5. Combate com Callback Customizado**

```lua
-- Criar callback para cálculo de dano
function onGetPlayerMinMaxValues(player, level, maglevel)
    -- Função: onGetPlayerMinMaxValues
    local min = level * 2 + maglevel * 3
    local max = level * 3 + maglevel * 4
    return min, max
end

-- Configurar combate
    --  Configurar combate (traduzido)
local combat = Combat()
combat:setParameter(COMBAT_PARAM_TYPE, COMBAT_HOLYDAMAGE)
combat:setCallback(CALLBACK_PARAM_LEVELMAGICVALUE, "onGetPlayerMinMaxValues")

combat:execute(caster, target)
```

### **6. Sistema de Armas**

```cpp
// Exemplo 1: Arma corpo a corpo
class WeaponMelee : public Weapon {
    -- Classe: WeaponMelee
    int32_t getWeaponDamage(const std::shared_ptr<Player> &player, 
                           const std::shared_ptr<Creature> &target, 
                           const std::shared_ptr<Item> &item, 
                           bool maxDamage = false) const override {
        // Cálculo de dano baseado em habilidades
        int32_t attackSkill = player->getSkillLevel(SKILL_SWORD);
        int32_t attackValue = item->getAttack();
        return normal_random(attackValue, attackValue + attackSkill);
    }
};

// Exemplo 2: Arma à distância
class WeaponDistance : public Weapon {
    -- Classe: WeaponDistance
    bool interruptSwing() const override { return true; }
    
    int32_t getWeaponDamage(const std::shared_ptr<Player> &player, 
                           const std::shared_ptr<Creature> &target, 
                           const std::shared_ptr<Item> &item, 
                           bool maxDamage = false) const override {
        // Cálculo de dano à distância
        int32_t distanceSkill = player->getSkillLevel(SKILL_DISTANCE);
        int32_t attackValue = item->getAttack();
        return normal_random(attackValue, attackValue + distanceSkill);
    }
};
```

### **7. Sistema de Condições**

```cpp
// Exemplo 1: Condição de dano
class ConditionDamage : public Condition {
    -- Classe: ConditionDamage
    bool addDamage(int32_t rounds, int32_t time, int32_t value) {
        IntervalInfo info;
        info.timeLeft = time;
        info.value = value;
        info.interval = rounds;
        damageList.push_back(info);
        return true;
    }
    
    int32_t getTotalDamage() const {
        int32_t total = 0;
        for (const auto &info : damageList) {
            total += info.value;
        }
        return total;
    }
};

// Exemplo 2: Condição de velocidade
class ConditionSpeed : public Condition {
    -- Classe: ConditionSpeed
    bool startCondition(std::shared_ptr<Creature> creature) override {
        creature->setSpeed(creature->getSpeed() + speedDelta);
        return true;
    }
    
    void endCondition(std::shared_ptr<Creature> creature) override {
        creature->setSpeed(creature->getSpeed() - speedDelta);
    }
};
```

### **8. Verificações de Combate**

#### Nível Basic
```cpp
// Exemplo 1: Verificar se pode fazer combate
ReturnValue Combat::canDoCombat(const std::shared_ptr<Creature> &caster, 
                               const std::shared_ptr<Creature> &target, 
                               bool aggressive) {
    if (!aggressive) {
        return RETURNVALUE_NOERROR;
    }
    
    // Verificar zona de proteção
    if (target->getTile()->hasFlag(TILESTATE_PROTECTIONZONE)) {
        return RETURNVALUE_ACTIONNOTPERMITTEDINPROTECTIONZONE;
    }
    
    // Verificar se pode atacar
    if (!target->isAttackable()) {
        return RETURNVALUE_YOUMAYNOTATTACKTHISCREATURE;
    }
    
    return RETURNVALUE_NOERROR;
}

// Exemplo 2: Verificar alvo válido
ReturnValue Combat::canTargetCreature(const std::shared_ptr<Player> &player, 
                                     const std::shared_ptr<Creature> &target) {
    // Verificar auto-ataque
    if (player == target) {
        return RETURNVALUE_YOUMAYNOTATTACKTHISPLAYER;
    }
    
    // Verificar proteção
    if (isProtected(player, target->getPlayer())) {
        return RETURNVALUE_YOUMAYNOTATTACKTHISPLAYER;
    }
    
    return RETURNVALUE_NOERROR;
}
```

#### Nível Intermediate
```cpp
// Exemplo 1: Verificar se pode fazer combate
ReturnValue Combat::canDoCombat(const std::shared_ptr<Creature> &caster, 
                               const std::shared_ptr<Creature> &target, 
                               bool aggressive) {
    if (!aggressive) {
        return RETURNVALUE_NOERROR;
    }
    
    // Verificar zona de proteção
    if (target->getTile()->hasFlag(TILESTATE_PROTECTIONZONE)) {
        return RETURNVALUE_ACTIONNOTPERMITTEDINPROTECTIONZONE;
    }
    
    // Verificar se pode atacar
    if (!target->isAttackable()) {
        return RETURNVALUE_YOUMAYNOTATTACKTHISCREATURE;
    }
    
    return RETURNVALUE_NOERROR;
}

// Exemplo 2: Verificar alvo válido
ReturnValue Combat::canTargetCreature(const std::shared_ptr<Player> &player, 
                                     const std::shared_ptr<Creature> &target) {
    // Verificar auto-ataque
    if (player == target) {
        return RETURNVALUE_YOUMAYNOTATTACKTHISPLAYER;
    }
    
    // Verificar proteção
    if (isProtected(player, target->getPlayer())) {
        return RETURNVALUE_YOUMAYNOTATTACKTHISPLAYER;
    }
    
    return RETURNVALUE_NOERROR;
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
// Exemplo 1: Verificar se pode fazer combate
ReturnValue Combat::canDoCombat(const std::shared_ptr<Creature> &caster, 
                               const std::shared_ptr<Creature> &target, 
                               bool aggressive) {
    if (!aggressive) {
        return RETURNVALUE_NOERROR;
    }
    
    // Verificar zona de proteção
    if (target->getTile()->hasFlag(TILESTATE_PROTECTIONZONE)) {
        return RETURNVALUE_ACTIONNOTPERMITTEDINPROTECTIONZONE;
    }
    
    // Verificar se pode atacar
    if (!target->isAttackable()) {
        return RETURNVALUE_YOUMAYNOTATTACKTHISCREATURE;
    }
    
    return RETURNVALUE_NOERROR;
}

// Exemplo 2: Verificar alvo válido
ReturnValue Combat::canTargetCreature(const std::shared_ptr<Player> &player, 
                                     const std::shared_ptr<Creature> &target) {
    // Verificar auto-ataque
    if (player == target) {
        return RETURNVALUE_YOUMAYNOTATTACKTHISPLAYER;
    }
    
    // Verificar proteção
    if (isProtected(player, target->getPlayer())) {
        return RETURNVALUE_YOUMAYNOTATTACKTHISPLAYER;
    }
    
    return RETURNVALUE_NOERROR;
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

### **9. Sistema de Áreas**

#### Nível Basic
```cpp
            if (x * x + y * y <= radius * radius) {
```

#### Nível Intermediate
```cpp
// Exemplo 1: Configurar área circular
void AreaCombat::setupArea(int32_t radius) {
    for (int32_t y = -radius; y <= radius; ++y) {
        for (int32_t x = -radius; x <= radius; ++x) {
            if (x * x + y * y <= radius * radius) {
                // Adicionar posição à área
                setValue(y + radius, x + radius, true);
            }
        }
    }
}

// Exemplo 2: Configurar área customizada
void AreaCombat::setupArea(const std::list<uint32_t> &list, uint32_t rows) {
    auto area = createArea(list, rows);
    for (int32_t i = 0; i < Direction::DIRECTION_LAST + 1; ++i) {
        areas[i] = area->clone();
    }
}
```

#### Nível Advanced
```cpp
// Exemplo 1: Configurar área circular
void AreaCombat::setupArea(int32_t radius) {
    for (int32_t y = -radius; y <= radius; ++y) {
        for (int32_t x = -radius; x <= radius; ++x) {
            if (x * x + y * y <= radius * radius) {
                // Adicionar posição à área
                setValue(y + radius, x + radius, true);
            }
        }
    }
}

// Exemplo 2: Configurar área customizada
void AreaCombat::setupArea(const std::list<uint32_t> &list, uint32_t rows) {
    auto area = createArea(list, rows);
    for (int32_t i = 0; i < Direction::DIRECTION_LAST + 1; ++i) {
        areas[i] = area->clone();
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

### **10. Fórmulas de Dano**

#### Nível Basic
```cpp
// Exemplo 1: Fórmula de nível e magia
int32_t levelFormula = player->getLevel() * 2 + 
    (player->getMagicLevel() + player->getSpecializedMagicLevel(damage.primary.type, true)) * 3;

damage.primary.value = normal_random(
    static_cast<int32_t>(levelFormula * mina + minb),
    static_cast<int32_t>(levelFormula * maxa + maxb)
);

// Exemplo 2: Fórmula de habilidade
const auto &weapon = g_weapons().getWeapon(tool);
if (weapon) {
    damage.primary.value = normal_random(
        static_cast<int32_t>(minb),
        static_cast<int32_t>(weapon->getWeaponDamage(player, target, tool, true) * maxa + maxb)
    );
    
    damage.secondary.type = weapon->getElementType();
    damage.secondary.value = weapon->getElementDamage(player, target, tool);
}
```

#### Nível Intermediate
```cpp
// Exemplo 1: Fórmula de nível e magia
int32_t levelFormula = player->getLevel() * 2 + 
    (player->getMagicLevel() + player->getSpecializedMagicLevel(damage.primary.type, true)) * 3;

damage.primary.value = normal_random(
    static_cast<int32_t>(levelFormula * mina + minb),
    static_cast<int32_t>(levelFormula * maxa + maxb)
);

// Exemplo 2: Fórmula de habilidade
const auto &weapon = g_weapons().getWeapon(tool);
if (weapon) {
    damage.primary.value = normal_random(
        static_cast<int32_t>(minb),
        static_cast<int32_t>(weapon->getWeaponDamage(player, target, tool, true) * maxa + maxb)
    );
    
    damage.secondary.type = weapon->getElementType();
    damage.secondary.value = weapon->getElementDamage(player, target, tool);
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
// Exemplo 1: Fórmula de nível e magia
int32_t levelFormula = player->getLevel() * 2 + 
    (player->getMagicLevel() + player->getSpecializedMagicLevel(damage.primary.type, true)) * 3;

damage.primary.value = normal_random(
    static_cast<int32_t>(levelFormula * mina + minb),
    static_cast<int32_t>(levelFormula * maxa + maxb)
);

// Exemplo 2: Fórmula de habilidade
const auto &weapon = g_weapons().getWeapon(tool);
if (weapon) {
    damage.primary.value = normal_random(
        static_cast<int32_t>(minb),
        static_cast<int32_t>(weapon->getWeaponDamage(player, target, tool, true) * maxa + maxb)
    );
    
    damage.secondary.type = weapon->getElementType();
    damage.secondary.value = weapon->getElementDamage(player, target, tool);
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

## 🎯 **Exercícios Práticos**

### **Exercício 1: Criar Magia de Cura**
Crie uma magia que cura o alvo baseada no nível e magia do caster.

**Solução:**
#### Nível Basic
```lua
local combat = Combat()
combat:setParameter(COMBAT_PARAM_TYPE, COMBAT_HEALING)
combat:setParameter(COMBAT_PARAM_EFFECT, CONST_ME_MAGIC_BLUE)
combat:setFormula(COMBAT_FORMULA_LEVELMAGIC, 10, 10, 20, 20)
combat:execute(caster, target)
```

#### Nível Intermediate
```lua
local combat = Combat()
combat:setParameter(COMBAT_PARAM_TYPE, COMBAT_HEALING)
combat:setParameter(COMBAT_PARAM_EFFECT, CONST_ME_MAGIC_BLUE)
combat:setFormula(COMBAT_FORMULA_LEVELMAGIC, 10, 10, 20, 20)
combat:execute(caster, target)
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
local combat = Combat()
combat:setParameter(COMBAT_PARAM_TYPE, COMBAT_HEALING)
combat:setParameter(COMBAT_PARAM_EFFECT, CONST_ME_MAGIC_BLUE)
combat:setFormula(COMBAT_FORMULA_LEVELMAGIC, 10, 10, 20, 20)
combat:execute(caster, target)
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

### **Exercício 2: Implementar Veneno Progressivo**
Crie uma condição de veneno que aumenta o dano ao longo do tempo.

**Solução:**
#### Nível Basic
```lua
local condition = Condition(CONDITION_POISON)
condition:setParameter(CONDITION_PARAM_DELAYED, 1)
condition:setParameter(CONDITION_PARAM_MINVALUE, 10)
condition:setParameter(CONDITION_PARAM_MAXVALUE, 50)
condition:setParameter(CONDITION_PARAM_STARTVALUE, 10)
condition:setParameter(CONDITION_PARAM_TICKINTERVAL, 2000)
condition:setParameter(CONDITION_PARAM_FORCEUPDATE, true)
```

#### Nível Intermediate
```lua
local condition = Condition(CONDITION_POISON)
condition:setParameter(CONDITION_PARAM_DELAYED, 1)
condition:setParameter(CONDITION_PARAM_MINVALUE, 10)
condition:setParameter(CONDITION_PARAM_MAXVALUE, 50)
condition:setParameter(CONDITION_PARAM_STARTVALUE, 10)
condition:setParameter(CONDITION_PARAM_TICKINTERVAL, 2000)
condition:setParameter(CONDITION_PARAM_FORCEUPDATE, true)
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
local condition = Condition(CONDITION_POISON)
condition:setParameter(CONDITION_PARAM_DELAYED, 1)
condition:setParameter(CONDITION_PARAM_MINVALUE, 10)
condition:setParameter(CONDITION_PARAM_MAXVALUE, 50)
condition:setParameter(CONDITION_PARAM_STARTVALUE, 10)
condition:setParameter(CONDITION_PARAM_TICKINTERVAL, 2000)
condition:setParameter(CONDITION_PARAM_FORCEUPDATE, true)
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

### **Exercício 3: Sistema de Chain Lightning**
Implemente um sistema de raio em cadeia que pula entre alvos.

**Solução:**
#### Nível Basic
```lua
local combat = Combat()
combat:setParameter(COMBAT_PARAM_TYPE, COMBAT_ENERGYDAMAGE)
combat:setParameter(COMBAT_PARAM_EFFECT, CONST_ME_ENERGYAREA)
combat:setChainCallback(5, 2, false) -- 5 alvos, distância 2, sem backtracking
combat:execute(caster, target)
```

#### Nível Intermediate
```lua
local combat = Combat()
combat:setParameter(COMBAT_PARAM_TYPE, COMBAT_ENERGYDAMAGE)
combat:setParameter(COMBAT_PARAM_EFFECT, CONST_ME_ENERGYAREA)
combat:setChainCallback(5, 2, false) -- 5 alvos, distância 2, sem backtracking
combat:execute(caster, target)
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
local combat = Combat()
combat:setParameter(COMBAT_PARAM_TYPE, COMBAT_ENERGYDAMAGE)
combat:setParameter(COMBAT_PARAM_EFFECT, CONST_ME_ENERGYAREA)
combat:setChainCallback(5, 2, false) -- 5 alvos, distância 2, sem backtracking
combat:execute(caster, target)
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

### **Exercício 4: Área de Efeito Customizada**
Crie uma área de combate em formato de cruz.

**Solução:**
#### Nível Basic
```lua
local area = {
    {0, 1, 0},
    {1, 3, 1},
    {0, 1, 0}
}

local combat = Combat()
combat:setParameter(COMBAT_PARAM_TYPE, COMBAT_HOLYDAMAGE)
combat:setArea(createCombatArea(area))
combat:execute(caster, position)
```

#### Nível Intermediate
```lua
local area = {
    {0, 1, 0},
    {1, 3, 1},
    {0, 1, 0}
}

local combat = Combat()
combat:setParameter(COMBAT_PARAM_TYPE, COMBAT_HOLYDAMAGE)
combat:setArea(createCombatArea(area))
combat:execute(caster, position)
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
local area = {
    {0, 1, 0},
    {1, 3, 1},
    {0, 1, 0}
}

local combat = Combat()
combat:setParameter(COMBAT_PARAM_TYPE, COMBAT_HOLYDAMAGE)
combat:setArea(createCombatArea(area))
combat:execute(caster, position)
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

### **Exercício 5: Callback de Dano Dinâmico**
Implemente um callback que calcula dano baseado na distância.

**Solução:**
```lua
function onGetPlayerMinMaxValues(player, level, maglevel)
    -- Função: onGetPlayerMinMaxValues
    local distance = getDistanceBetween(player:getPosition(), target:getPosition())
    local multiplier = math.max(0.5, 1.0 - (distance * 0.1))
    
    local min = (level * 2 + maglevel * 3) * multiplier
    local max = (level * 3 + maglevel * 4) * multiplier
    return min, max
end
```

## 🔧 **Conceitos Avançados**

### **1. Sistema de Extensões**
#### Nível Basic
```cpp
// Aplicar extensões de dano
void Combat::applyExtensions(const std::shared_ptr<Creature> &caster, 
                            const std::vector<std::shared_ptr<Creature>> targets, 
                            CombatDamage &damage, 
                            const CombatParams &params) {
    // Aplicar modificações baseadas em extensões
    // Ex: Wheel of Destiny, imbuements, etc.
}
```

#### Nível Intermediate
```cpp
// Aplicar extensões de dano
void Combat::applyExtensions(const std::shared_ptr<Creature> &caster, 
                            const std::vector<std::shared_ptr<Creature>> targets, 
                            CombatDamage &damage, 
                            const CombatParams &params) {
    // Aplicar modificações baseadas em extensões
    // Ex: Wheel of Destiny, imbuements, etc.
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
// Aplicar extensões de dano
void Combat::applyExtensions(const std::shared_ptr<Creature> &caster, 
                            const std::vector<std::shared_ptr<Creature>> targets, 
                            CombatDamage &damage, 
                            const CombatParams &params) {
    // Aplicar modificações baseadas em extensões
    // Ex: Wheel of Destiny, imbuements, etc.
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

### **2. Imbuements**
#### Nível Basic
```cpp
// Aplicar dano elemental de imbuements
CombatDamage Combat::applyImbuementElementalDamage(const std::shared_ptr<Player> &attackerPlayer, 
                                                   std::shared_ptr<Item> item, 
                                                   CombatDamage damage) {
    // Calcular dano elemental baseado em imbuements
    // Aplicar multiplicadores e modificadores
    return damage;
}
```

#### Nível Intermediate
```cpp
// Aplicar dano elemental de imbuements
CombatDamage Combat::applyImbuementElementalDamage(const std::shared_ptr<Player> &attackerPlayer, 
                                                   std::shared_ptr<Item> item, 
                                                   CombatDamage damage) {
    // Calcular dano elemental baseado em imbuements
    // Aplicar multiplicadores e modificadores
    return damage;
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
// Aplicar dano elemental de imbuements
CombatDamage Combat::applyImbuementElementalDamage(const std::shared_ptr<Player> &attackerPlayer, 
                                                   std::shared_ptr<Item> item, 
                                                   CombatDamage damage) {
    // Calcular dano elemental baseado em imbuements
    // Aplicar multiplicadores e modificadores
    return damage;
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

### **3. Verificações de Segurança**
#### Nível Basic
```cpp
// Verificar se pode fazer combate
ReturnValue Combat::canDoCombat(const std::shared_ptr<Creature> &caster, 
                               const std::shared_ptr<Creature> &target, 
                               bool aggressive) {
    // Verificações de zona, proteção, permissões
    // Validação de parâmetros e condições
}
```

#### Nível Intermediate
```cpp
// Verificar se pode fazer combate
ReturnValue Combat::canDoCombat(const std::shared_ptr<Creature> &caster, 
                               const std::shared_ptr<Creature> &target, 
                               bool aggressive) {
    // Verificações de zona, proteção, permissões
    // Validação de parâmetros e condições
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
// Verificar se pode fazer combate
ReturnValue Combat::canDoCombat(const std::shared_ptr<Creature> &caster, 
                               const std::shared_ptr<Creature> &target, 
                               bool aggressive) {
    // Verificações de zona, proteção, permissões
    // Validação de parâmetros e condições
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

## 📋 **Boas Práticas**

### **1. Validação de Parâmetros**
- Sempre validar parâmetros antes de executar combate
- Verificar se alvos são válidos
- Validar permissões e zonas

### **2. Uso de Callbacks**
- Usar callbacks para lógica customizada
- Implementar callbacks para cálculos complexos
- Manter callbacks simples e eficientes

### **3. Verificações de Segurança**
- Implementar verificações de segurança adequadas
- Validar zonas de proteção
- Verificar permissões de PvP

### **4. Otimização de Performance**
- Otimizar performance com cache quando necessário
- Usar lazy loading para condições
- Minimizar cálculos desnecessários

### **5. Documentação**
- Documentar fórmulas de dano claramente
- Comentar callbacks complexos
- Manter documentação atualizada

### **6. Testes**
- Testar extensivamente antes de implementar em produção
- Implementar testes unitários para componentes
- Validar comportamento em diferentes cenários

## 🔗 **Integração com Outros Sistemas**

### **Sistema de Mapas (CANARY-011)**
- Verificação de posições válidas
- Cálculo de áreas de efeito
- Validação de projeções

### **Sistema de Partículas (CANARY-010)**
- Efeitos visuais de combate
- Animações de magias
- Feedback visual para jogadores

### **Sistema de Som (CANARY-009)**
- Sons de combate
- Efeitos sonoros de magias
- Feedback auditivo

## 📊 **Métricas e Performance**

### **1. Métricas Integradas**
#### Nível Basic
```cpp
metrics::method_latency measure(__METRICS_METHOD_NAME__);
```

#### Nível Intermediate
```cpp
metrics::method_latency measure(__METRICS_METHOD_NAME__);
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
metrics::method_latency measure(__METRICS_METHOD_NAME__);
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
- Monitoramento automático de performance
- Identificação de gargalos
- Otimização contínua

### **2. Cache Inteligente**
- Cache de áreas de combate
- Reutilização de matrizes
- Otimização de cálculos de distância

### **3. Lazy Loading**
- Carregamento sob demanda de condições
- Inicialização tardia de callbacks
- Otimização de memória

## 🎯 **Conclusão**

O Sistema de Combate do Canary é uma arquitetura complexa e poderosa que oferece flexibilidade extrema para implementação de mecânicas de combate. Sua modularidade permite desde implementações simples até sistemas muito complexos, sempre mantendo performance e segurança.

### **Principais Características:**
- ✅ **Arquitetura Modular**: Componentes independentes e reutilizáveis
- ✅ **Sistema de Callbacks**: Flexibilidade para customizações
- ✅ **Múltiplas Fórmulas**: Suporte a diferentes tipos de cálculo
- ✅ **Sistema de Condições**: Efeitos temporais complexos
- ✅ **Chain Combat**: Combate em cadeia avançado
- ✅ **Integração Lua**: Scripts customizáveis
- ✅ **Verificações de Segurança**: Proteção contra exploits
- ✅ **Otimizações**: Performance e cache inteligente

### **Aplicações Práticas:**
- **Magias Customizadas**: Implementação de magias únicas
- **Sistemas de Armas**: Armas com mecânicas especiais
- **Condições Complexas**: Efeitos temporais avançados
- **Combate em Área**: Magias e habilidades em área
- **Chain Combat**: Habilidades que afetam múltiplos alvos
- **Callbacks Dinâmicos**: Lógica customizada de combate

A chave para dominar este sistema é entender os conceitos fundamentais e praticar com exemplos progressivamente mais complexos. O sistema oferece uma base sólida para implementação de mecânicas de combate sofisticadas em servidores MMORPG.

---

**Lição Criada**: 2025-01-27  
**Responsável**: Habdel Research System  
**Status**: ✅ **CONCLUÍDA**  
**Próximo**: 🎯 **CANARY-013: Sistema de Inventário** 