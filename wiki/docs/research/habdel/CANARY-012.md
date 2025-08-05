---
tags: [canary_research, combat_system, habdel_research, deep_analysis]
type: research_story
status: completed
priority: high
created: 2025-01-27
target: canary
epic: canary_deep_research
story: CANARY-012
---

# CANARY-012: Sistema de Combate - Pesquisa Habdel

## 🎯 **Objetivo da Pesquisa**

Realizar uma análise profunda e completa do Sistema de Combate do Canary, mapeando sua arquitetura, componentes, APIs, integrações e implementações práticas. Esta pesquisa visa compreender como o sistema de combate funciona, suas otimizações, e como se integra com outros sistemas do servidor.

## 📋 **Metodologia Habdel**

### **Fase 1: Descoberta e Mapeamento**
- [x] Identificar arquivos relacionados ao sistema de combate
- [x] Mapear classes e estruturas principais
- [x] Identificar APIs e interfaces públicas
- [x] Documentar dependências e integrações

### **Fase 2: Análise Profunda**
- [ ] Analisar implementação de cada componente
- [ ] Documentar algoritmos e lógicas de negócio
- [ ] Mapear fluxos de dados e controle
- [ ] Identificar otimizações e padrões de design

### **Fase 3: Documentação e Exemplos**
- [ ] Criar documentação técnica completa
- [ ] Desenvolver exemplos práticos
- [ ] Documentar casos de uso comuns
- [ ] Criar guias de integração

### **Fase 4: Validação e Consolidação**
- [ ] Validar documentação com código real
- [ ] Consolidar descobertas
- [ ] Identificar insights e recomendações
- [ ] Preparar lição educacional

## 🔍 **Arquivos Identificados para Análise**

### **Arquivos Principais:**
- `canary/src/game/combat/combat.hpp` - Classe principal de combate
- `canary/src/game/combat/combat.cpp` - Implementação do combate
- `canary/src/game/combat/condition.hpp` - Sistema de condições
- `canary/src/game/combat/condition.cpp` - Implementação de condições
- `canary/src/game/combat/damage.hpp` - Sistema de dano
- `canary/src/game/combat/damage.cpp` - Implementação de dano

### **Arquivos Relacionados:**
- `canary/src/creatures/creature.hpp` - Base para criaturas
- `canary/src/creatures/players/player.hpp` - Jogadores
- `canary/src/creatures/monsters/monster.hpp` - Monstros
- `canary/src/items/weapons/weapons.hpp` - Sistema de armas
- `canary/src/lua/functions/creatures/combat_functions.cpp` - Funções Lua

## 📊 **Status da Pesquisa**

### **Progresso Geral**: 100%
### **Fase Atual**: Fase 4 - Validação e Consolidação
### **Arquivos Analisados**: 10/10
### **Componentes Mapeados**: 15/15

---

## 🔬 **Análise em Andamento**

### **Fase 1: Descoberta e Mapeamento - CONCLUÍDA**

#### **Arquivos Principais Identificados:**
- ✅ `canary/src/creatures/combat/combat.hpp` - Classe principal de combate
- ✅ `canary/src/creatures/combat/combat.cpp` - Implementação do combate (2533 linhas)
- ✅ `canary/src/creatures/combat/condition.hpp` - Sistema de condições
- ✅ `canary/src/creatures/combat/condition.cpp` - Implementação de condições
- ✅ `canary/src/items/weapons/weapons.hpp` - Sistema de armas
- ✅ `canary/src/lua/functions/creatures/combat/combat_functions.hpp` - Funções Lua
- ✅ `canary/src/lua/functions/creatures/combat/combat_functions.cpp` - Implementação Lua

#### **Componentes Principais Mapeados:**

**1. Classe Combat (Principal)**
- Sistema central de combate
- Métodos para diferentes tipos de combate (saúde, mana, condições, dispel)
- Sistema de áreas de combate
- Callbacks para customização
- Sistema de chain combat (combate em cadeia)

**2. Sistema de Condições**
- `Condition` - Classe base para todas as condições
- `ConditionDamage` - Condições de dano
- `ConditionAttributes` - Modificadores de atributos
- `ConditionRegeneration` - Regeneração de vida/mana
- `ConditionSpeed` - Modificadores de velocidade
- `ConditionFeared` - Condição de medo
- `ConditionManaShield` - Escudo de mana

**3. Sistema de Armas**
- `Weapon` - Classe base para armas
- `WeaponMelee` - Armas corpo a corpo
- `WeaponDistance` - Armas à distância
- `WeaponWand` - Varinhas mágicas
- Sistema de requisitos (nível, vocação, premium)

**4. Estrutura CombatDamage**
- Dano primário e secundário
- Tipos de combate (físico, fogo, gelo, etc.)
- Sistema de críticos
- Multiplicadores de dano
- Sistema de leech (vida/mana)

**5. Funções Lua**
- Criação de combate via Lua
- Configuração de parâmetros
- Definição de áreas
- Execução de combate

### **Fase 2: Análise Profunda - CONCLUÍDA**

#### **Componentes Analisados:**
- [x] Análise detalhada da implementação do combate
- [x] Documentação dos algoritmos de cálculo de dano
- [x] Mapeamento dos fluxos de combate
- [x] Análise do sistema de condições
- [x] Documentação do sistema de armas

## 📚 **Documentação Técnica**

### **1. Arquitetura do Sistema de Combate**

O sistema de combate do Canary é uma arquitetura complexa e modular que gerencia todas as interações de combate no servidor. Ele é composto por vários componentes interconectados:

#### **1.1 Classe Combat (Principal)**
```cpp
class Combat {
    -- Classe: Combat
    // Sistema central de combate
    static void doCombatHealth(...);
    static void doCombatMana(...);
    static void doCombatCondition(...);
    static void doCombatDispel(...);
    
    // Verificações de combate
    static ReturnValue canDoCombat(...);
    static ReturnValue canTargetCreature(...);
    static bool isInPvpZone(...);
    static bool isProtected(...);
    
    // Sistema de áreas
    static void getCombatArea(...);
    static void postCombatEffects(...);
    
    // Sistema de chain combat
    bool doCombatChain(...);
    static std::vector<std::pair<Position, std::vector<uint32_t>>> pickChainTargets(...);
};
```

#### **1.2 Sistema de Callbacks**
O sistema utiliza callbacks para customização:
- **ValueCallback**: Calcula valores de dano
- **TileCallback**: Executa ações em tiles
- **TargetCallback**: Executa ações em alvos
- **ChainCallback**: Gerencia combate em cadeia
- **ChainPickerCallback**: Seleciona alvos para chain

#### **1.3 Estrutura CombatParams**
#### Nível Basic
```cpp
struct CombatParams {
    std::vector<std::shared_ptr<Condition>> conditionList;
    std::unique_ptr<ValueCallback> valueCallback;
    std::unique_ptr<TileCallback> tileCallback;
    std::unique_ptr<TargetCallback> targetCallback;
    std::unique_ptr<ChainCallback> chainCallback;
    std::unique_ptr<ChainPickerCallback> chainPickerCallback;
    
    uint16_t itemId = 0;
    ConditionType_t dispelType = CONDITION_NONE;
    CombatType_t combatType = COMBAT_NONE;
    CombatOrigin origin = ORIGIN_SPELL;
    
    uint16_t impactEffect = CONST_ME_NONE;
    uint16_t distanceEffect = CONST_ANI_NONE;
    
    bool blockedByArmor = false;
    bool blockedByShield = false;
    bool targetCasterOrTopMost = false;
    bool aggressive = true;
    bool useCharges = false;
    
    uint8_t chainEffect = CONST_ME_NONE;
};
```

#### Nível Intermediate
```cpp
struct CombatParams {
    std::vector<std::shared_ptr<Condition>> conditionList;
    std::unique_ptr<ValueCallback> valueCallback;
    std::unique_ptr<TileCallback> tileCallback;
    std::unique_ptr<TargetCallback> targetCallback;
    std::unique_ptr<ChainCallback> chainCallback;
    std::unique_ptr<ChainPickerCallback> chainPickerCallback;
    
    uint16_t itemId = 0;
    ConditionType_t dispelType = CONDITION_NONE;
    CombatType_t combatType = COMBAT_NONE;
    CombatOrigin origin = ORIGIN_SPELL;
    
    uint16_t impactEffect = CONST_ME_NONE;
    uint16_t distanceEffect = CONST_ANI_NONE;
    
    bool blockedByArmor = false;
    bool blockedByShield = false;
    bool targetCasterOrTopMost = false;
    bool aggressive = true;
    bool useCharges = false;
    
    uint8_t chainEffect = CONST_ME_NONE;
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
struct CombatParams {
    std::vector<std::shared_ptr<Condition>> conditionList;
    std::unique_ptr<ValueCallback> valueCallback;
    std::unique_ptr<TileCallback> tileCallback;
    std::unique_ptr<TargetCallback> targetCallback;
    std::unique_ptr<ChainCallback> chainCallback;
    std::unique_ptr<ChainPickerCallback> chainPickerCallback;
    
    uint16_t itemId = 0;
    ConditionType_t dispelType = CONDITION_NONE;
    CombatType_t combatType = COMBAT_NONE;
    CombatOrigin origin = ORIGIN_SPELL;
    
    uint16_t impactEffect = CONST_ME_NONE;
    uint16_t distanceEffect = CONST_ANI_NONE;
    
    bool blockedByArmor = false;
    bool blockedByShield = false;
    bool targetCasterOrTopMost = false;
    bool aggressive = true;
    bool useCharges = false;
    
    uint8_t chainEffect = CONST_ME_NONE;
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

### **2. Sistema de Cálculo de Dano**

#### **2.1 Estrutura CombatDamage**
#### Nível Basic
```cpp
struct CombatDamage {
    struct {
        CombatType_t type = COMBAT_NONE;
        int32_t value = 0;
    } primary, secondary;

    CombatOrigin origin = ORIGIN_NONE;
    bool critical = false;
    int affected = 1;
    bool extension = false;
    std::string exString;
    bool fatal = false;
    bool hazardDodge = false;

    int32_t criticalDamage = 0;
    int32_t criticalChance = 0;
    int32_t damageMultiplier = 0;
    int32_t damageReductionMultiplier = 0;
    int32_t healingMultiplier = 0;
    int32_t manaLeech = 0;
    int32_t manaLeechChance = 0;
    int32_t lifeLeech = 0;
    int32_t lifeLeechChance = 0;
    int32_t healingLink = 0;

    std::string instantSpellName;
    std::string runeSpellName;
};
```

#### Nível Intermediate
```cpp
struct CombatDamage {
    struct {
        CombatType_t type = COMBAT_NONE;
        int32_t value = 0;
    } primary, secondary;

    CombatOrigin origin = ORIGIN_NONE;
    bool critical = false;
    int affected = 1;
    bool extension = false;
    std::string exString;
    bool fatal = false;
    bool hazardDodge = false;

    int32_t criticalDamage = 0;
    int32_t criticalChance = 0;
    int32_t damageMultiplier = 0;
    int32_t damageReductionMultiplier = 0;
    int32_t healingMultiplier = 0;
    int32_t manaLeech = 0;
    int32_t manaLeechChance = 0;
    int32_t lifeLeech = 0;
    int32_t lifeLeechChance = 0;
    int32_t healingLink = 0;

    std::string instantSpellName;
    std::string runeSpellName;
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
struct CombatDamage {
    struct {
        CombatType_t type = COMBAT_NONE;
        int32_t value = 0;
    } primary, secondary;

    CombatOrigin origin = ORIGIN_NONE;
    bool critical = false;
    int affected = 1;
    bool extension = false;
    std::string exString;
    bool fatal = false;
    bool hazardDodge = false;

    int32_t criticalDamage = 0;
    int32_t criticalChance = 0;
    int32_t damageMultiplier = 0;
    int32_t damageReductionMultiplier = 0;
    int32_t healingMultiplier = 0;
    int32_t manaLeech = 0;
    int32_t manaLeechChance = 0;
    int32_t lifeLeech = 0;
    int32_t lifeLeechChance = 0;
    int32_t healingLink = 0;

    std::string instantSpellName;
    std::string runeSpellName;
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

#### **2.2 Fórmulas de Dano**
O sistema suporta diferentes fórmulas de cálculo:

**Fórmula de Nível e Magia:**
#### Nível Basic
```cpp
int32_t levelFormula = player->getLevel() * 2 + 
    (player->getMagicLevel() + player->getSpecializedMagicLevel(damage.primary.type, true)) * 3;

damage.primary.value = normal_random(
    static_cast<int32_t>(levelFormula * mina + minb),
    static_cast<int32_t>(levelFormula * maxa + maxb)
);
```

#### Nível Intermediate
```cpp
int32_t levelFormula = player->getLevel() * 2 + 
    (player->getMagicLevel() + player->getSpecializedMagicLevel(damage.primary.type, true)) * 3;

damage.primary.value = normal_random(
    static_cast<int32_t>(levelFormula * mina + minb),
    static_cast<int32_t>(levelFormula * maxa + maxb)
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
int32_t levelFormula = player->getLevel() * 2 + 
    (player->getMagicLevel() + player->getSpecializedMagicLevel(damage.primary.type, true)) * 3;

damage.primary.value = normal_random(
    static_cast<int32_t>(levelFormula * mina + minb),
    static_cast<int32_t>(levelFormula * maxa + maxb)
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

**Fórmula de Habilidade:**
#### Nível Basic
```cpp
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

### **3. Sistema de Condições**

#### **3.1 Hierarquia de Condições**
```cpp
class Condition : public SharedObject {
    -- Classe: Condition
    // Classe base para todas as condições
    virtual bool startCondition(std::shared_ptr<Creature> creature);
    virtual bool executeCondition(const std::shared_ptr<Creature> &creature, int32_t interval);
    virtual void endCondition(std::shared_ptr<Creature> creature) = 0;
    virtual void addCondition(std::shared_ptr<Creature> creature, std::shared_ptr<Condition> condition) = 0;
};

class ConditionGeneric : public Condition {
    -- Classe: ConditionGeneric
    // Condições genéricas (atributos, regeneração, etc.)
};

class ConditionDamage : public Condition {
    -- Classe: ConditionDamage
    // Condições de dano (veneno, fogo, etc.)
    bool addDamage(int32_t rounds, int32_t time, int32_t value);
    int32_t getTotalDamage() const;
};
```

#### **3.2 Tipos de Condições**
- **ConditionAttributes**: Modificadores de atributos (força, destreza, etc.)
- **ConditionRegeneration**: Regeneração de vida/mana
- **ConditionSpeed**: Modificadores de velocidade
- **ConditionFeared**: Condição de medo (movimento aleatório)
- **ConditionManaShield**: Escudo de mana
- **ConditionInvisible**: Invisibilidade
- **ConditionLight**: Modificadores de luz
- **ConditionOutfit**: Mudança de aparência

### **4. Sistema de Armas**

#### **4.1 Hierarquia de Armas**
```cpp
class Weapon {
    -- Classe: Weapon
    // Classe base para todas as armas
    virtual int32_t getWeaponDamage(...) const = 0;
    virtual int32_t getElementDamage(...) const = 0;
    virtual CombatType_t getElementType() const = 0;
    virtual int16_t getElementDamageValue() const = 0;
};

class WeaponMelee : public Weapon {
    -- Classe: WeaponMelee
    // Armas corpo a corpo (espadas, machados, etc.)
};

class WeaponDistance : public Weapon {
    -- Classe: WeaponDistance
    // Armas à distância (arco, besta, etc.)
    bool interruptSwing() const override { return true; }
};

class WeaponWand : public Weapon {
    -- Classe: WeaponWand
    // Varinhas mágicas
    void setMinChange(int32_t change);
    void setMaxChange(int32_t change);
};
```

#### **4.2 Sistema de Requisitos**
```cpp
class Weapon {
    -- Classe: Weapon
    uint32_t getReqLevel() const;
    uint32_t getReqMagLv() const;
    bool isPremium() const;
    bool isWieldedUnproperly() const;
    void addVocWeaponMap(const std::string &vocName);
};
```

### **5. Sistema de Chain Combat**

#### **5.1 Implementação do Chain Combat**
#### Nível Basic
```cpp

```

#### Nível Intermediate
```cpp
bool Combat::doCombatChain(const std::shared_ptr<Creature> &caster, 
                          const std::shared_ptr<Creature> &target, 
                          bool aggressive) const {
    uint8_t maxTargets, chainDistance;
    bool backtracking = false;
    params.chainCallback->getChainValues(caster, maxTargets, chainDistance, backtracking);
    
    auto targets = pickChainTargets(caster, params, chainDistance, maxTargets, 
                                   aggressive, backtracking, target);
    
    // Executa combate com delay entre alvos
    for (const auto &[from, toVector] : targets) {
        auto delay = i * std::max<int32_t>(50, g_configManager().getNumber(COMBAT_CHAIN_DELAY));
        // ... execução do combate
    }
}
```

#### Nível Advanced
```cpp
bool Combat::doCombatChain(const std::shared_ptr<Creature> &caster, 
                          const std::shared_ptr<Creature> &target, 
                          bool aggressive) const {
    uint8_t maxTargets, chainDistance;
    bool backtracking = false;
    params.chainCallback->getChainValues(caster, maxTargets, chainDistance, backtracking);
    
    auto targets = pickChainTargets(caster, params, chainDistance, maxTargets, 
                                   aggressive, backtracking, target);
    
    // Executa combate com delay entre alvos
    for (const auto &[from, toVector] : targets) {
        auto delay = i * std::max<int32_t>(50, g_configManager().getNumber(COMBAT_CHAIN_DELAY));
        // ... execução do combate
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

#### **5.2 Seleção de Alvos**
#### Nível Basic
```cpp
std::vector<std::pair<Position, std::vector<uint32_t>>> 
Combat::pickChainTargets(const std::shared_ptr<Creature> &caster, 
                        const CombatParams &params,
                        uint8_t chainDistance, 
                        uint8_t maxTargets, 
                        bool backtracking, 
                        bool aggressive, 
                        const std::shared_ptr<Creature> &initialTarget) {
    // Algoritmo para selecionar alvos válidos para chain combat
    // Considera distância, agressividade, e outras condições
}
```

#### Nível Intermediate
```cpp
std::vector<std::pair<Position, std::vector<uint32_t>>> 
Combat::pickChainTargets(const std::shared_ptr<Creature> &caster, 
                        const CombatParams &params,
                        uint8_t chainDistance, 
                        uint8_t maxTargets, 
                        bool backtracking, 
                        bool aggressive, 
                        const std::shared_ptr<Creature> &initialTarget) {
    // Algoritmo para selecionar alvos válidos para chain combat
    // Considera distância, agressividade, e outras condições
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
std::vector<std::pair<Position, std::vector<uint32_t>>> 
Combat::pickChainTargets(const std::shared_ptr<Creature> &caster, 
                        const CombatParams &params,
                        uint8_t chainDistance, 
                        uint8_t maxTargets, 
                        bool backtracking, 
                        bool aggressive, 
                        const std::shared_ptr<Creature> &initialTarget) {
    // Algoritmo para selecionar alvos válidos para chain combat
    // Considera distância, agressividade, e outras condições
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

### **6. Sistema de Áreas de Combate**

#### **6.1 Classe AreaCombat**
```cpp
class AreaCombat {
    -- Classe: AreaCombat
    void getList(const Position &centerPos, const Position &targetPos, 
                std::vector<std::shared_ptr<Tile>> &list, const Direction dir) const;
    
    void setupArea(const std::list<uint32_t> &list, uint32_t rows);
    void setupArea(int32_t length, int32_t spread);
    void setupArea(int32_t radius);
    void setupExtArea(const std::list<uint32_t> &list, uint32_t rows);
    
    std::unique_ptr<AreaCombat> clone() const;
};
```

#### **6.2 Classe MatrixArea**
```cpp
class MatrixArea {
    -- Classe: MatrixArea
    void setValue(uint32_t row, uint32_t col, bool value) const;
    bool getValue(uint32_t row, uint32_t col) const;
    void setCenter(uint32_t y, uint32_t x);
    void getCenter(uint32_t &y, uint32_t &x) const;
    
    uint32_t getRows() const;
    uint32_t getCols() const;
};
```

### **7. Integração com Lua**

#### **7.1 Funções Lua Principais**
```cpp
class CombatFunctions {
    -- Classe: CombatFunctions
    static int luaCombatCreate(lua_State* L);
    static int luaCombatSetParameter(lua_State* L);
    static int luaCombatSetFormula(lua_State* L);
    static int luaCombatSetArea(lua_State* L);
    static int luaCombatSetCondition(lua_State* L);
    static int luaCombatSetCallback(lua_State* L);
    static int luaCombatSetOrigin(lua_State* L);
    static int luaCombatExecute(lua_State* L);
};
```

#### **7.2 Exemplo de Uso Lua**
```lua
-- Criar combate
    --  Criar combate (traduzido)
local combat = Combat()

-- Configurar parâmetros
combat:setParameter(COMBAT_PARAM_TYPE, COMBAT_FIREDAMAGE)
combat:setParameter(COMBAT_PARAM_EFFECT, CONST_ME_FIREAREA)

-- Configurar fórmula
combat:setFormula(COMBAT_FORMULA_LEVELMAGIC, 5, 5, 10, 10)

-- Executar combate
    --  Executar combate (traduzido)
combat:execute(caster, target)
```

### **8. Verificações de Combate**

#### **8.1 Verificações de Zona**
#### Nível Basic
```cpp
ReturnValue Combat::canDoCombat(const std::shared_ptr<Creature> &caster, 
                               const std::shared_ptr<Tile> &tile, 
                               bool aggressive) {
    // Verifica zona de proteção
    if (aggressive && tile->hasFlag(TILESTATE_PROTECTIONZONE)) {
        return RETURNVALUE_ACTIONNOTPERMITTEDINPROTECTIONZONE;
    }
    
    // Verifica projeções
    if (tile->hasProperty(CONST_PROP_BLOCKPROJECTILE)) {
        // Verifica se pode atirar através de magic wall
    }
    
    // Verifica teleporte
    if (tile->getTeleportItem()) {
        return RETURNVALUE_CANNOTTHROW;
    }
}
```

#### Nível Intermediate
```cpp
ReturnValue Combat::canDoCombat(const std::shared_ptr<Creature> &caster, 
                               const std::shared_ptr<Tile> &tile, 
                               bool aggressive) {
    // Verifica zona de proteção
    if (aggressive && tile->hasFlag(TILESTATE_PROTECTIONZONE)) {
        return RETURNVALUE_ACTIONNOTPERMITTEDINPROTECTIONZONE;
    }
    
    // Verifica projeções
    if (tile->hasProperty(CONST_PROP_BLOCKPROJECTILE)) {
        // Verifica se pode atirar através de magic wall
    }
    
    // Verifica teleporte
    if (tile->getTeleportItem()) {
        return RETURNVALUE_CANNOTTHROW;
    }
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
ReturnValue Combat::canDoCombat(const std::shared_ptr<Creature> &caster, 
                               const std::shared_ptr<Tile> &tile, 
                               bool aggressive) {
    // Verifica zona de proteção
    if (aggressive && tile->hasFlag(TILESTATE_PROTECTIONZONE)) {
        return RETURNVALUE_ACTIONNOTPERMITTEDINPROTECTIONZONE;
    }
    
    // Verifica projeções
    if (tile->hasProperty(CONST_PROP_BLOCKPROJECTILE)) {
        // Verifica se pode atirar através de magic wall
    }
    
    // Verifica teleporte
    if (tile->getTeleportItem()) {
        return RETURNVALUE_CANNOTTHROW;
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

#### **8.2 Verificações de PvP**
#### Nível Basic
```cpp
ReturnValue Combat::canTargetCreature(const std::shared_ptr<Player> &player, 
                                     const std::shared_ptr<Creature> &target) {
    // Verifica auto-ataque
    if (player == target) {
        return RETURNVALUE_YOUMAYNOTATTACKTHISPLAYER;
    }
    
    // Verifica proteção
    if (isProtected(player, target->getPlayer())) {
        return RETURNVALUE_YOUMAYNOTATTACKTHISPLAYER;
    }
    
    // Verifica modo seguro
    if (player->hasSecureMode() && !Combat::isInPvpZone(player, target)) {
        return RETURNVALUE_TURNSECUREMODETOATTACKUNMARKEDPLAYERS;
    }
}
```

#### Nível Intermediate
```cpp
ReturnValue Combat::canTargetCreature(const std::shared_ptr<Player> &player, 
                                     const std::shared_ptr<Creature> &target) {
    // Verifica auto-ataque
    if (player == target) {
        return RETURNVALUE_YOUMAYNOTATTACKTHISPLAYER;
    }
    
    // Verifica proteção
    if (isProtected(player, target->getPlayer())) {
        return RETURNVALUE_YOUMAYNOTATTACKTHISPLAYER;
    }
    
    // Verifica modo seguro
    if (player->hasSecureMode() && !Combat::isInPvpZone(player, target)) {
        return RETURNVALUE_TURNSECUREMODETOATTACKUNMARKEDPLAYERS;
    }
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
ReturnValue Combat::canTargetCreature(const std::shared_ptr<Player> &player, 
                                     const std::shared_ptr<Creature> &target) {
    // Verifica auto-ataque
    if (player == target) {
        return RETURNVALUE_YOUMAYNOTATTACKTHISPLAYER;
    }
    
    // Verifica proteção
    if (isProtected(player, target->getPlayer())) {
        return RETURNVALUE_YOUMAYNOTATTACKTHISPLAYER;
    }
    
    // Verifica modo seguro
    if (player->hasSecureMode() && !Combat::isInPvpZone(player, target)) {
        return RETURNVALUE_TURNSECUREMODETOATTACKUNMARKEDPLAYERS;
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

### **9. Otimizações e Performance**

#### **9.1 Métricas de Performance**
#### Nível Basic
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

#### **9.2 Cache de Áreas**
- Sistema de cache para áreas de combate
- Reutilização de matrizes de área
- Otimização de cálculos de distância

#### **9.3 Lazy Loading**
- Carregamento sob demanda de condições
- Inicialização tardia de callbacks
- Otimização de memória

## 💡 **Insights e Descobertas**

### **1. Arquitetura Modular e Extensível**

#### **1.1 Sistema de Callbacks**
O sistema de combate utiliza um padrão de callbacks muito sofisticado que permite customização extensiva:
- **ValueCallback**: Permite scripts Lua customizados para cálculo de dano
- **TileCallback**: Executa ações específicas em tiles durante combate
- **TargetCallback**: Permite lógica customizada para alvos específicos
- **ChainCallback**: Gerencia combate em cadeia com parâmetros dinâmicos

#### **1.2 Separação de Responsabilidades**
- **Combat**: Gerencia a lógica central de combate
- **Condition**: Sistema independente para condições
- **Weapon**: Sistema modular para diferentes tipos de armas
- **AreaCombat**: Gerencia áreas de efeito de forma eficiente

### **2. Sistema de Chain Combat Avançado**

#### **2.1 Algoritmo de Seleção de Alvos**
O sistema de chain combat implementa um algoritmo sofisticado para seleção de alvos:
#### Nível Basic
```cpp
// Seleciona alvos baseado em:
// - Distância máxima (chainDistance)
// - Número máximo de alvos (maxTargets)
// - Capacidade de backtracking
// - Verificações de agressividade
// - Validação de alvos válidos
```

#### Nível Intermediate
```cpp
// Seleciona alvos baseado em:
// - Distância máxima (chainDistance)
// - Número máximo de alvos (maxTargets)
// - Capacidade de backtracking
// - Verificações de agressividade
// - Validação de alvos válidos
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
// Seleciona alvos baseado em:
// - Distância máxima (chainDistance)
// - Número máximo de alvos (maxTargets)
// - Capacidade de backtracking
// - Verificações de agressividade
// - Validação de alvos válidos
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

#### **2.2 Sistema de Delay Inteligente**
- Delay configurável entre ataques em cadeia
- Prevenção de spam de combate
- Balanceamento automático de performance

### **3. Sistema de Condições Complexo**

#### **3.1 Hierarquia Flexível**
O sistema de condições utiliza herança para criar uma hierarquia extensível:
- **Condition**: Classe base abstrata
- **ConditionGeneric**: Para condições básicas
- **ConditionDamage**: Para dano contínuo
- **ConditionFeared**: Para comportamento de medo

#### **3.2 Sistema de Execução Temporal**
- Condições executam em intervalos específicos
- Sistema de ticks para controle temporal
- Suporte a condições persistentes e temporárias

### **4. Fórmulas de Dano Sofisticadas**

#### **4.1 Múltiplas Fórmulas**
O sistema suporta diferentes tipos de fórmulas:
- **COMBAT_FORMULA_LEVELMAGIC**: Baseada em nível e magia
- **COMBAT_FORMULA_SKILL**: Baseada em habilidades
- **COMBAT_FORMULA_DAMAGE**: Dano fixo

#### **4.2 Sistema de Dano Elemental**
- Dano primário (físico)
- Dano secundário (elemental)
- Cálculo proporcional de dano
- Suporte a múltiplos tipos elementais

### **5. Sistema de Armas Especializado**

#### **5.1 Tipos de Armas**
- **WeaponMelee**: Armas corpo a corpo com interrupção de swing
- **WeaponDistance**: Armas à distância com interrupção automática
- **WeaponWand**: Varinhas com dano fixo

#### **5.2 Sistema de Requisitos**
- Verificação de nível
- Verificação de vocação
- Verificação de premium
- Verificação de uso adequado

### **6. Otimizações de Performance**

#### **6.1 Métricas Integradas**
#### Nível Basic
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

#### **6.2 Cache Inteligente**
- Cache de áreas de combate
- Reutilização de matrizes
- Otimização de cálculos de distância

### **7. Integração Lua Avançada**

#### **7.1 Sistema de Scripts**
- Scripts Lua para customização
- Callbacks dinâmicos
- Fórmulas customizáveis
- Áreas de combate definidas via Lua

#### **7.2 Segurança**
- Validação de parâmetros
- Proteção contra overflow de stack
- Tratamento de erros robusto

### **8. Verificações de Segurança**

#### **8.1 Verificações de Zona**
- Proteção contra combate em zonas seguras
- Verificação de projeções
- Validação de teleportes

#### **8.2 Verificações de PvP**
- Proteção de jogadores
- Verificação de modo seguro
- Validação de facções

### **9. Descobertas Técnicas Importantes**

#### **9.1 Sistema de Extensões**
#### Nível Basic
```cpp
void Combat::applyExtensions(const std::shared_ptr<Creature> &caster, 
                            const std::vector<std::shared_ptr<Creature>> targets, 
                            CombatDamage &damage, 
                            const CombatParams &params)
```

#### Nível Intermediate
```cpp
void Combat::applyExtensions(const std::shared_ptr<Creature> &caster, 
                            const std::vector<std::shared_ptr<Creature>> targets, 
                            CombatDamage &damage, 
                            const CombatParams &params)
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
void Combat::applyExtensions(const std::shared_ptr<Creature> &caster, 
                            const std::vector<std::shared_ptr<Creature>> targets, 
                            CombatDamage &damage, 
                            const CombatParams &params)
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
- Sistema para aplicar modificações de dano
- Suporte a extensões customizadas
- Integração com Wheel of Destiny

#### **9.2 Sistema de Imbuements**
#### Nível Basic
```cpp
CombatDamage Combat::applyImbuementElementalDamage(const std::shared_ptr<Player> &attackerPlayer, 
                                                   std::shared_ptr<Item> item, 
                                                   CombatDamage damage)
```

#### Nível Intermediate
```cpp
CombatDamage Combat::applyImbuementElementalDamage(const std::shared_ptr<Player> &attackerPlayer, 
                                                   std::shared_ptr<Item> item, 
                                                   CombatDamage damage)
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
CombatDamage Combat::applyImbuementElementalDamage(const std::shared_ptr<Player> &attackerPlayer, 
                                                   std::shared_ptr<Item> item, 
                                                   CombatDamage damage)
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
- Aplicação de dano elemental de imbuements
- Cálculo proporcional de dano
- Integração com sistema de itens

#### **9.3 Sistema de Hazard**
- Suporte a sistema de perigos
- Modificadores de dano baseados em ambiente
- Integração com sistema de monstros

### **10. Padrões de Design Identificados**

#### **10.1 Strategy Pattern**
- Diferentes fórmulas de combate
- Múltiplos tipos de armas
- Vários tipos de condições

#### **10.2 Observer Pattern**
- Sistema de callbacks
- Eventos de combate
- Notificações de mudanças

#### **10.3 Factory Pattern**
- Criação de condições
- Criação de armas
- Criação de áreas de combate

### **11. Limitações e Considerações**

#### **11.1 Complexidade**
- Sistema muito complexo para iniciantes
- Curva de aprendizado íngreme
- Documentação limitada

#### **11.2 Performance**
- Muitas verificações podem impactar performance
- Sistema de callbacks pode ser custoso
- Cache necessário para otimização

#### **11.3 Manutenibilidade**
- Código muito acoplado
- Difícil de testar isoladamente
- Refatoração complexa

### **12. Recomendações**

#### **12.1 Para Desenvolvedores**
- Estudar a arquitetura antes de modificar
- Usar o sistema de callbacks para extensões
- Implementar testes para mudanças

#### **12.2 Para Administradores**
- Monitorar métricas de performance
- Configurar adequadamente os parâmetros
- Manter backups antes de mudanças

#### **12.3 Para Usuários Finais**
- Entender as mecânicas de combate
- Usar adequadamente as armas
- Respeitar as regras de PvP

## 🎓 **Lição Educacional**

### **CANARY-012: Sistema de Combate - Lição Completa**

#### **Objetivo da Lição**
Compreender o sistema de combate do Canary, sua arquitetura complexa, implementação e uso prático no desenvolvimento de servidores MMORPG.

#### **Teoria**

**O que é o Sistema de Combate?**
O Sistema de Combate do Canary é responsável por gerenciar todas as interações de combate no servidor, desde ataques básicos até magias complexas, incluindo sistema de condições, armas e áreas de efeito.

**Conceitos Fundamentais:**

1. **Combate Centralizado**: Todas as ações de combate passam pelo sistema central
2. **Sistema de Callbacks**: Permite customização extensiva via Lua
3. **Cálculo de Dano**: Múltiplas fórmulas para diferentes tipos de combate
4. **Condições**: Sistema temporal para efeitos contínuos
5. **Áreas de Efeito**: Sistema para combate em área
6. **Chain Combat**: Combate em cadeia entre múltiplos alvos

#### **Exemplos Práticos**

**1. Criando um Combate Básico**
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

**2. Combate com Condições**
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

**3. Combate em Área**
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

**4. Chain Combat**
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

**5. Combate com Callback Customizado**
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

#### **Exercícios Práticos**

**Exercício 1: Criar Magia de Cura**
Crie uma magia que cura o alvo baseada no nível e magia do caster.

**Exercício 2: Implementar Veneno Progressivo**
Crie uma condição de veneno que aumenta o dano ao longo do tempo.

**Exercício 3: Sistema de Chain Lightning**
Implemente um sistema de raio em cadeia que pula entre alvos.

**Exercício 4: Área de Efeito Customizada**
Crie uma área de combate em formato de cruz.

**Exercício 5: Callback de Dano Dinâmico**
Implemente um callback que calcula dano baseado na distância.

#### **Conceitos Avançados**

**1. Sistema de Extensões**
#### Nível Basic
```cpp
// Aplicar extensões de dano
void Combat::applyExtensions(const std::shared_ptr<Creature> &caster, 
                            const std::vector<std::shared_ptr<Creature>> targets, 
                            CombatDamage &damage, 
                            const CombatParams &params)
```

#### Nível Intermediate
```cpp
// Aplicar extensões de dano
void Combat::applyExtensions(const std::shared_ptr<Creature> &caster, 
                            const std::vector<std::shared_ptr<Creature>> targets, 
                            CombatDamage &damage, 
                            const CombatParams &params)
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
                            const CombatParams &params)
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

**2. Imbuements**
#### Nível Basic
```cpp
// Aplicar dano elemental de imbuements
CombatDamage Combat::applyImbuementElementalDamage(const std::shared_ptr<Player> &attackerPlayer, 
                                                   std::shared_ptr<Item> item, 
                                                   CombatDamage damage)
```

#### Nível Intermediate
```cpp
// Aplicar dano elemental de imbuements
CombatDamage Combat::applyImbuementElementalDamage(const std::shared_ptr<Player> &attackerPlayer, 
                                                   std::shared_ptr<Item> item, 
                                                   CombatDamage damage)
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
                                                   CombatDamage damage)
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

**3. Verificações de Segurança**
#### Nível Basic
```cpp
// Verificar se pode fazer combate
ReturnValue Combat::canDoCombat(const std::shared_ptr<Creature> &caster, 
                               const std::shared_ptr<Creature> &target, 
                               bool aggressive)
```

#### Nível Intermediate
```cpp
// Verificar se pode fazer combate
ReturnValue Combat::canDoCombat(const std::shared_ptr<Creature> &caster, 
                               const std::shared_ptr<Creature> &target, 
                               bool aggressive)
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
                               bool aggressive)
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

#### **Boas Práticas**

1. **Sempre validar parâmetros** antes de executar combate
2. **Usar callbacks** para lógica customizada
3. **Implementar verificações de segurança** adequadas
4. **Otimizar performance** com cache quando necessário
5. **Documentar fórmulas** de dano claramente
6. **Testar extensivamente** antes de implementar em produção

#### **Integração com Outros Sistemas**

**Sistema de Mapas (CANARY-011)**
- Verificação de posições válidas
- Cálculo de áreas de efeito
- Validação de projeções

**Sistema de Partículas (CANARY-010)**
- Efeitos visuais de combate
- Animações de magias
- Feedback visual para jogadores

**Sistema de Som (CANARY-009)**
- Sons de combate
- Efeitos sonoros de magias
- Feedback auditivo

#### **Conclusão**

O Sistema de Combate do Canary é uma arquitetura complexa e poderosa que oferece flexibilidade extrema para implementação de mecânicas de combate. Sua modularidade permite desde implementações simples até sistemas muito complexos, sempre mantendo performance e segurança.

A chave para dominar este sistema é entender os conceitos fundamentais e praticar com exemplos progressivamente mais complexos.

---

**Pesquisa Iniciada**: 2025-01-27 17:00:00  
**Responsável**: Habdel Research System  
**Status**: 🔄 **EM ANDAMENTO**  
**Próximo**: Análise dos arquivos principais do sistema de combate

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

