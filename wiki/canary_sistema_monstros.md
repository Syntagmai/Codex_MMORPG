---
tags: [canary, sistema_monstros, monsters, AI, drops, comportamento, habdel_research]
type: wiki_page
status: active
priority: high
created: 2025-08-05
updated: 2025-08-05
aliases: [monstros, monsters, AI, drops, loot, comportamento, behavior]
---

# 🐉 Sistema de Monstros - Canary

> [!info] **Baseado na Pesquisa Habdel**
> Esta página é baseada na pesquisa detalhada **[CANARY-013: Sistema de Inventário](habdel/CANARY-013.md)** realizada com metodologia Habdel.

## 🎯 **Visão Geral**

O Sistema de Monstros do Canary gerencia criaturas não-jogador (NPCs hostis), incluindo AI, comportamento, drops, spawns e interações. É um sistema complexo que cria desafios dinâmicos para os jogadores.

## 🏗️ **Arquitetura do Sistema**

### **Estrutura de Arquivos**
```
canary/src/creatures/monsters/
├── monster.hpp                    # Classe principal Monster
├── monster.cpp                    # Implementação do Monster
├── monster_type.hpp               # Definições de tipos
├── monster_type.cpp               # Implementação de tipos
└── spawns/
    ├── spawn_monster.hpp          # Sistema de spawns
    └── spawn_monster.cpp          # Implementação de spawns
```

### **Componentes Principais**

#### **1. Classe Monster**
- **Arquivo**: `canary/src/creatures/monsters/monster.hpp`
- **Propósito**: Gerenciamento de monstros individuais
- **Funcionalidades**:
  - AI e comportamento
  - Sistema de combate
  - Drops e loot
  - Spawn e respawn

#### **2. Classe MonsterType**
- **Arquivo**: `canary/src/creatures/monsters/monster_type.hpp`
- **Propósito**: Definição de tipos de monstros
- **Configurações**:
  - Estatísticas base
  - Comportamento padrão
  - Drops configurados
  - Resistências

#### **3. Sistema de Spawns**
- **Arquivo**: `canary/src/creatures/monsters/spawns/spawn_monster.hpp`
- **Propósito**: Gerenciamento de spawns
- **Funcionalidades**:
  - Spawn automático
  - Respawn configurável
  - Limites de população

## 🔧 **Implementação Prática**

### **Exemplo 1: Definição de Monstro**
```cpp
// Exemplo: Definir tipo de monstro
class MonsterType {
public:
    std::string name;
    uint32_t health;
    uint32_t maxHealth;
    uint32_t experience;
    uint32_t defense;
    uint32_t armor;
    
    // Configurações de comportamento
    bool canPushItems;
    bool canPushCreatures;
    bool canWalkOnEnergy;
    bool canWalkOnFire;
    bool canWalkOnPoison;
    
    // Sistema de drops
    std::vector<LootBlock> lootList;
};
```

### **Exemplo 2: AI de Monstro**
```cpp
// Exemplo: Comportamento básico de monstro
void Monster::onThink() {
    if (isDead()) {
        return;
    }
    
    // Verificar alvos próximos
    auto target = getTarget();
    if (!target) {
        target = findTarget();
        if (target) {
            setTarget(target);
        }
    }
    
    // Executar ações baseadas no estado
    if (target) {
        if (canAttack(target)) {
            attack(target);
        } else {
            moveToTarget(target);
        }
    } else {
        // Comportamento passivo
        wanderAround();
    }
}
```

### **Exemplo 3: Sistema de Drops**
```cpp
// Exemplo: Sistema de loot configurável
void Monster::dropLoot(Container* corpse) {
    if (!corpse) {
        return;
    }
    
    for (const auto& lootBlock : monsterType->lootList) {
        if (random(1, 100) <= lootBlock.chance) {
            uint32_t count = random(lootBlock.countMin, lootBlock.countMax);
            
            auto item = Item::CreateItem(lootBlock.id, count);
            if (item) {
                corpse->addItem(item);
            }
        }
    }
}
```

## 🎮 **Exemplos Práticos em Lua**

### **Exemplo 1: Monstro Customizado**
```lua
-- Exemplo: Criar monstro customizado
local monster = MonsterType("Dragon")
monster:health(5000)
monster:maxHealth(5000)
monster:experience(2000)
monster:defense(50)
monster:armor(30)

-- Configurar comportamento
monster:canPushItems(false)
monster:canPushCreatures(true)
monster:canWalkOnFire(true)

-- Configurar drops
monster:addLoot(2160, 1, 10, 100) -- Gold coins
monster:addLoot(2393, 1, 1, 50)   -- Dragon scale mail
monster:addLoot(2392, 1, 1, 30)   -- Dragon shield
```

### **Exemplo 2: AI Customizada**
```lua
-- Exemplo: AI personalizada para monstro
function onThink(monster)
    local target = monster:getTarget()
    
    if target then
        local distance = monster:getDistanceTo(target)
        
        if distance <= 1 then
            -- Atacar se próximo
            monster:attack(target)
        elseif distance <= 3 then
            -- Mover em direção ao alvo
            monster:moveToTarget(target)
        else
            -- Perder alvo se muito longe
            monster:setTarget(nil)
        end
    else
        -- Procurar novo alvo
        local creatures = monster:getSpectators()
        for _, creature in pairs(creatures) do
            if creature:isPlayer() and monster:canSeeCreature(creature) then
                monster:setTarget(creature)
                break
            end
        end
    end
end
```

### **Exemplo 3: Sistema de Drops Dinâmico**
```lua
-- Exemplo: Drops baseados em condições
function onDeath(monster, corpse)
    local killer = monster:getKiller()
    
    if killer and killer:isPlayer() then
        local level = killer:getLevel()
        
        -- Drops baseados no nível do jogador
        if level >= 100 then
            corpse:addItem(2160, math.random(100, 500)) -- Mais gold para jogadores de alto nível
        end
        
        -- Drops especiais baseados em vocação
        local vocation = killer:getVocation()
        if vocation:getId() == VOCATION_KNIGHT then
            corpse:addItem(2393, 1) -- Dragon scale mail para cavaleiros
        elseif vocation:getId() == VOCATION_SORCERER then
            corpse:addItem(2392, 1) -- Dragon shield para magos
        end
    end
end
```

## 🔗 **Dependências e Integrações**

### **Dependências Principais**
- **Sistema de Combate**: Para ataques e dano
- **Sistema de Inventário**: Para drops e loot
- **Sistema de Mapas**: Para movimento e posicionamento
- **Sistema de Spawns**: Para criação e respawn

### **Integrações**
- **Sistema de Players**: Alvos de combate
- **Sistema de Items**: Drops e equipamentos
- **Sistema de Experiência**: XP por morte
- **Sistema de Quests**: Objetivos de caça

## 📊 **Otimizações e Performance**

### **Otimizações Implementadas**
- **AI Otimizada**: Comportamento eficiente
- **Spawn Management**: Controle de população
- **Loot Caching**: Cache de drops frequentes
- **Pathfinding**: Algoritmos otimizados

### **Métricas de Performance**
- **AI Update**: < 5ms por monstro
- **Spawn Time**: < 100ms para spawns
- **Memory Usage**: Pool de objetos reduz uso em 40%

## 🎯 **Casos de Uso Comuns**

### **1. Monstros Básicos**
- Criaturas simples com AI básica
- Drops fixos e previsíveis
- Comportamento padrão

### **2. Bosses Complexos**
- AI avançada com múltiplas fases
- Drops especiais e únicos
- Mecânicas de combate complexas

### **3. Monstros Eventuais**
- Spawns temporários
- Drops especiais por evento
- Comportamento único

## 🔧 **Como Implementar**

### **Passo 1: Definir Tipo de Monstro**
```lua
local monsterType = MonsterType("CustomMonster")
monsterType:health(1000)
monsterType:experience(500)
```

### **Passo 2: Configurar Comportamento**
```lua
monsterType:canPushItems(false)
monsterType:canPushCreatures(true)
monsterType:canWalkOnFire(true)
```

### **Passo 3: Configurar Drops**
```lua
monsterType:addLoot(2160, 1, 10, 100) -- Gold coins
monsterType:addLoot(2393, 1, 1, 50)   -- Special item
```

### **Passo 4: Implementar AI Customizada**
```lua
function onThink(monster)
    -- Lógica de AI personalizada
end
```

## 📚 **Referências Relacionadas**

- **[Sistema de Combate](canary_sistema_combate.md)** - AI de combate de monstros
- **[Sistema de Magias](canary_sistema_magias.md)** - Magias de monstros
- **[Sistema de Quests](canary_sistema_quests.md)** - Objetivos de caça
- **[Sistema de Spawns](canary_sistema_spawns.md)** - Criação de monstros

## 🎓 **Lição Educacional**

O Sistema de Monstros demonstra como criar um sistema de AI complexo com:
1. **Modularidade**: Separação entre tipo e instância
2. **Flexibilidade**: AI customizável via Lua
3. **Performance**: Otimizações para muitos monstros
4. **Extensibilidade**: Fácil adição de novos comportamentos

---

> [!tip] **Próximo Passo**
> Continue para **[Sistema de Quests](canary_sistema_quests.md)** para entender como os monstros se integram com o sistema de missões. 