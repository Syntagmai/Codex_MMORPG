---
tags: [otclient, sistema, combate, battle, criaturas, ataques, defesa, wiki]
type: wiki_page
status: published
priority: high
created: 2025-08-05
updated: 2025-08-05
---

# ⚔️ **Sistema de Combate - OTClient**

> [!info] **Sistema de Combate e Battle List**
> O sistema de combate do OTClient gerencia ataques, defesa, lista de batalha e interações com criaturas, fornecendo APIs para automação e controle de combate.

---

## 📋 **Visão Geral**

O **Sistema de Combate** do OTClient é responsável por:

- **Battle List**: Lista de criaturas visíveis e interativas
- **Sistema de Ataque**: Gerenciamento de ataques e alvos
- **Sistema de Defesa**: Proteção e esquiva
- **Estados de Combate**: Modos de luta e PvP
- **Automação**: Scripts de combate automático

---

## 🏗️ **Arquitetura do Sistema**

### **Componentes Principais**

```cpp
// Estrutura principal do sistema de combate
class BattleSystem {
    std::map<uint32_t, CreaturePtr> m_battleList;    // Lista de criaturas
    CreaturePtr m_attackingCreature;                 // Criatura sendo atacada
    CreaturePtr m_followingCreature;                 // Criatura sendo seguida
    Otc::FightModes m_fightMode;                     // Modo de luta
    Otc::ChaseModes m_chaseMode;                     // Modo de perseguição
    bool m_safeFight;                                // Luta segura
};
```

### **Hierarquia de Combate**

```
BattleSystem
├── BattleList (Lista de Batalha)
│   ├── Creature (Criatura)
│   │   ├── Health (Vida)
│   │   ├── Skull (Caveira)
│   │   └── Shield (Escudo)
│   └── Filters (Filtros)
├── CombatModes (Modos de Combate)
│   ├── FightMode (Modo de Luta)
│   ├── ChaseMode (Modo de Perseguição)
│   └── PvPMode (Modo PvP)
└── AutoCombat (Combate Automático)
    ├── TargetSelection (Seleção de Alvo)
    ├── AttackLogic (Lógica de Ataque)
    └── DefenseLogic (Lógica de Defesa)
```

---

## 🔧 **APIs e Interfaces**

### **Gerenciamento da Battle List**

```lua
-- Obter criatura da battle list
local creature = g_map.getCreatureById(creatureId)

-- Adicionar criatura à battle list
g_map.addThing(creature, position, stackPos)

-- Remover criatura da battle list
g_map.removeCreatureById(creatureId)

-- Obter todas as criaturas em área
local creatures = g_map.getSpectatorsInRangeEx(centerPos, multiFloor, minX, maxX, minY, maxY)
```

### **Sistema de Ataque**

```lua
-- Atacar criatura
g_game.attack(creature)

-- Seguir criatura
g_game.follow(creature)

-- Cancelar ataque
g_game.cancelAttack()

-- Verificar se está atacando
local isAttacking = g_game.isAttacking()

-- Obter criatura sendo atacada
local target = g_game.getAttackingCreature()
```

### **Modos de Combate**

```lua
-- Configurar modo de luta
g_game.setFightMode(fightMode)
-- fightMode: Otc.FightOffensive, Otc.FightBalanced, Otc.FightDefensive

-- Configurar modo de perseguição
g_game.setChaseMode(chaseMode)
-- chaseMode: Otc.DontChase, Otc.ChaseOpponent

-- Configurar luta segura
g_game.setSafeFight(enabled)

-- Configurar modo PvP
g_game.setPVPMode(pvpMode)
-- pvpMode: Otc.WhiteDove, Otc.WhiteHand, Otc.YellowHand, Otc.RedFist
```

---

## 📚 **Exemplos Práticos**

### **Exemplo 1: Sistema de Auto-Ataque**

```lua
-- Sistema básico de auto-ataque
local function autoAttack()
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    -- Verificar se já está atacando
    if g_game.isAttacking() then
        return
    end
    
    -- Procurar monstros próximos
    local creatures = g_map.getSpectatorsInRangeEx(
        player:getPosition(),
        true,  -- multiFloor
        -5, 5, -5, 5  -- range 5x5
    )
    
    for _, creature in ipairs(creatures) do
        if creature:isMonster() and creature:getHealthPercent() > 0 then
            -- Verificar se é um monstro válido para ataque
            local distance = player:getPosition():getDistanceFrom(creature:getPosition())
            if distance <= 4 then
                g_game.attack(creature)
                print("Atacando: " .. creature:getName())
                break
            end
        end
    end
end

-- Executar auto-ataque a cada 1 segundo
scheduleEvent(autoAttack, 1000)
```

### **Exemplo 2: Sistema de Auto-Heal**

```lua
-- Sistema de auto-heal baseado na vida
local function autoHeal()
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    local healthPercent = player:getHealthPercent()
    
    if healthPercent <= 50 then
        -- Usar potion de vida
        local healthPotion = g_game.findPlayerItem(7618, -1) -- Health Potion
        if healthPotion then
            g_game.useInventoryItem(7618)
            print("Usando Health Potion - Vida: " .. healthPercent .. "%")
        end
    end
    
    if healthPercent <= 30 then
        -- Usar potion de vida forte
        local strongHealthPotion = g_game.findPlayerItem(7588, -1) -- Strong Health Potion
        if strongHealthPotion then
            g_game.useInventoryItem(7588)
            print("Usando Strong Health Potion - Vida: " .. healthPercent .. "%")
        end
    end
end

-- Executar auto-heal a cada 500ms
scheduleEvent(autoHeal, 500)
```

### **Exemplo 3: Sistema de Auto-Follow**

```lua
-- Sistema de auto-follow para party
local function autoFollowParty()
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    -- Verificar se já está seguindo alguém
    if g_game.getChaseMode() == Otc.ChaseOpponent then
        return
    end
    
    -- Procurar membros do party
    local creatures = g_map.getSpectatorsInRangeEx(
        player:getPosition(),
        true,  -- multiFloor
        -10, 10, -10, 10  -- range 10x10
    )
    
    for _, creature in ipairs(creatures) do
        if creature:isPlayer() and creature:isPartyMember() then
            local distance = player:getPosition():getDistanceFrom(creature:getPosition())
            if distance > 3 then
                g_game.follow(creature)
                print("Seguindo: " .. creature:getName())
                break
            end
        end
    end
end

-- Executar auto-follow a cada 2 segundos
scheduleEvent(autoFollowParty, 2000)
```

---

## 🎮 **Sistema de Battle List**

### **Gerenciamento da Interface**

```lua
-- Controle da janela de battle list
local function setupBattleList()
    -- Mostrar/ocultar battle list
    modules.game_battle.toggle()
    
    -- Configurar filtros
    modules.game_battle.setFilter("hidePlayers", false)
    modules.game_battle.setFilter("hideNPCs", true)
    modules.game_battle.setFilter("hideMonsters", false)
    modules.game_battle.setFilter("hideSkulls", false)
    modules.game_battle.setFilter("hideParty", false)
end

-- Adicionar criatura à battle list
local function addToBattleList(creature)
    if creature and creature:isMonster() then
        -- Criatura já é adicionada automaticamente pelo OTClient
        print("Criatura adicionada à battle list: " .. creature:getName())
    end
end
```

### **Exemplo: Sistema de Priorização de Alvos**

```lua
-- Sistema de priorização de alvos baseado em tipo e vida
local function getPriorityTarget()
    local player = g_game.getLocalPlayer()
    if not player then return nil end
    
    local creatures = g_map.getSpectatorsInRangeEx(
        player:getPosition(),
        true,  -- multiFloor
        -6, 6, -6, 6  -- range 6x6
    )
    
    local priorityTargets = {}
    
    for _, creature in ipairs(creatures) do
        if creature:isMonster() and creature:getHealthPercent() > 0 then
            local priority = 0
            local distance = player:getPosition():getDistanceFrom(creature:getPosition())
            
            -- Priorizar criaturas mais próximas
            priority = priority + (10 - distance)
            
            -- Priorizar criaturas com menos vida
            priority = priority + (100 - creature:getHealthPercent())
            
            -- Priorizar criaturas específicas (ex: dragões)
            if creature:getName():lower():find("dragon") then
                priority = priority + 50
            end
            
            table.insert(priorityTargets, {
                creature = creature,
                priority = priority
            })
        end
    end
    
    -- Ordenar por prioridade
    table.sort(priorityTargets, function(a, b)
        return a.priority > b.priority
    end)
    
    if #priorityTargets > 0 then
        return priorityTargets[1].creature
    end
    
    return nil
end

-- Uso no auto-ataque
local function smartAutoAttack()
    local target = getPriorityTarget()
    if target then
        g_game.attack(target)
        print("Atacando alvo prioritário: " .. target:getName())
    end
end
```

---

## 🛡️ **Sistema de Defesa**

### **Auto-Defesa**

```lua
-- Sistema de auto-defesa
local function autoDefense()
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    local healthPercent = player:getHealthPercent()
    local manaPercent = player:getManaPercent()
    
    -- Auto-escape quando vida baixa
    if healthPercent <= 20 then
        -- Usar haste para fugir
        local hasteSpell = g_game.findPlayerItem(3155, -1) -- Haste Spell
        if hasteSpell then
            g_game.useInventoryItem(3155)
            print("Usando Haste para fugir - Vida: " .. healthPercent .. "%")
        end
        
        -- Cancelar ataque e fugir
        g_game.cancelAttack()
        g_game.setChaseMode(Otc.DontChase)
    end
    
    -- Auto-cura quando mana disponível
    if manaPercent >= 30 and healthPercent <= 70 then
        -- Usar spell de cura
        g_game.talk("exura")
        print("Usando Exura - Vida: " .. healthPercent .. "%")
    end
end

-- Executar auto-defesa a cada 300ms
scheduleEvent(autoDefense, 300)
```

### **Sistema de Anti-PK**

```lua
-- Sistema anti-PK (Player Killer)
local function antiPK()
    local player = g_game.getLocalPlayer()
    if not player then return end
    
    local creatures = g_map.getSpectatorsInRangeEx(
        player:getPosition(),
        true,  -- multiFloor
        -8, 8, -8, 8  -- range 8x8
    )
    
    for _, creature in ipairs(creatures) do
        if creature:isPlayer() then
            local skull = creature:getSkull()
            
            -- Verificar se é um PK
            if skull == SkullRed or skull == SkullBlack then
                local distance = player:getPosition():getDistanceFrom(creature:getPosition())
                
                if distance <= 3 then
                    -- PK detectado próximo!
                    print("PK detectado: " .. creature:getName())
                    
                    -- Fugir imediatamente
                    g_game.cancelAttack()
                    g_game.setChaseMode(Otc.DontChase)
                    
                    -- Usar haste para fugir
                    local hasteSpell = g_game.findPlayerItem(3155, -1)
                    if hasteSpell then
                        g_game.useInventoryItem(3155)
                    end
                    
                    -- Tentar teleportar se possível
                    local teleportSpell = g_game.findPlayerItem(3160, -1) -- Teleport Spell
                    if teleportSpell then
                        g_game.useInventoryItem(3160)
                    end
                    
                    break
                end
            end
        end
    end
end

-- Executar anti-PK a cada 500ms
scheduleEvent(antiPK, 500)
```

---

## 🔍 **Monitoramento e Logs**

### **Sistema de Logs de Combate**

```lua
-- Sistema de logs de combate
local combatLog = {}

local function logCombatEvent(event, data)
    local timestamp = os.date("%H:%M:%S")
    local logEntry = {
        timestamp = timestamp,
        event = event,
        data = data
    }
    
    table.insert(combatLog, logEntry)
    
    -- Manter apenas os últimos 100 logs
    if #combatLog > 100 then
        table.remove(combatLog, 1)
    end
    
    print("[" .. timestamp .. "] " .. event .. ": " .. (data or ""))
end

-- Conectar eventos de combate
connect(g_game, {
    onAttack = function(creature)
        logCombatEvent("Attack", creature:getName())
    end,
    
    onFollow = function(creature)
        logCombatEvent("Follow", creature:getName())
    end,
    
    onCancelAttack = function()
        logCombatEvent("CancelAttack", "")
    end
})

-- Função para salvar logs
local function saveCombatLog()
    local file = io.open("combat_log.txt", "w")
    if file then
        for _, entry in ipairs(combatLog) do
            file:write(string.format("[%s] %s: %s\n", 
                entry.timestamp, entry.event, entry.data))
        end
        file:close()
        print("Log de combate salvo em combat_log.txt")
    end
end
```

### **Estatísticas de Combate**

```lua
-- Estatísticas de combate
local combatStats = {
    attacks = 0,
    kills = 0,
    damageDealt = 0,
    damageReceived = 0,
    startTime = os.time()
}

local function updateCombatStats(event, data)
    if event == "Attack" then
        combatStats.attacks = combatStats.attacks + 1
    elseif event == "Kill" then
        combatStats.kills = combatStats.kills + 1
    elseif event == "DamageDealt" then
        combatStats.damageDealt = combatStats.damageDealt + (data or 0)
    elseif event == "DamageReceived" then
        combatStats.damageReceived = combatStats.damageReceived + (data or 0)
    end
end

local function showCombatStats()
    local sessionTime = os.time() - combatStats.startTime
    local hours = math.floor(sessionTime / 3600)
    local minutes = math.floor((sessionTime % 3600) / 60)
    
    print("=== Estatísticas de Combate ===")
    print("Tempo de sessão: " .. hours .. "h " .. minutes .. "m")
    print("Ataques: " .. combatStats.attacks)
    print("Kills: " .. combatStats.kills)
    print("Dano causado: " .. combatStats.damageDealt)
    print("Dano recebido: " .. combatStats.damageReceived)
    print("K/D Ratio: " .. (combatStats.kills / math.max(combatStats.attacks, 1)))
end
```

---

## 🔗 **Integração com Outros Sistemas**

### **Sistema de Eventos**

```lua
-- Conectar eventos de combate
connect(g_game, {
    onAttack = function(creature)
        print("Atacando: " .. creature:getName())
    end,
    
    onFollow = function(creature)
        print("Seguindo: " .. creature:getName())
    end,
    
    onCancelAttack = function()
        print("Ataque cancelado")
    end
})

connect(LocalPlayer, {
    onHealthPercentChange = function(healthPercent)
        if healthPercent <= 30 then
            print("Vida baixa: " .. healthPercent .. "%")
        end
    end,
    
    onManaPercentChange = function(manaPercent)
        if manaPercent <= 20 then
            print("Mana baixa: " .. manaPercent .. "%")
        end
    end
})
```

### **Sistema de UI**

```lua
-- Interface de controle de combate
local function createCombatControlUI()
    local window = g_ui.createWidget('MainWindow')
    window:setText('Controle de Combate')
    window:setSize({width = 300, height = 200})
    
    -- Botão de auto-ataque
    local autoAttackButton = g_ui.createWidget('Button', window)
    autoAttackButton:setText('Auto-Ataque')
    autoAttackButton:setPosition({x = 10, y = 10})
    autoAttackButton.onClick = function()
        smartAutoAttack()
    end
    
    -- Botão de auto-heal
    local autoHealButton = g_ui.createWidget('Button', window)
    autoHealButton:setText('Auto-Heal')
    autoHealButton:setPosition({x = 10, y = 40})
    autoHealButton.onClick = function()
        autoHeal()
    end
    
    -- Botão de estatísticas
    local statsButton = g_ui.createWidget('Button', window)
    statsButton:setText('Estatísticas')
    statsButton:setPosition({x = 10, y = 70})
    statsButton.onClick = function()
        showCombatStats()
    end
    
    return window
end
```

---

## 📊 **Dependências e Relacionamentos**

### **Dependências Principais**
- **Sistema de Mapas**: Posicionamento de criaturas
- **Sistema de Eventos**: Comunicação entre componentes
- **Sistema de Inventário**: Uso de itens de combate
- **Sistema de Protocolo**: Comunicação com servidor

### **Sistemas Dependentes**
- **Sistema de Quests**: Combate para completar missões
- **Sistema de NPCs**: Interação com NPCs de combate
- **Sistema de Interface**: Battle list e controles

---

## 🚀 **Melhores Práticas**

### **Otimização de Combate**

1. **Use Filtros Inteligentes**: Configure filtros da battle list adequadamente
2. **Priorize Alvos**: Implemente sistema de priorização de alvos
3. **Monitore Recursos**: Verifique vida e mana antes de ações
4. **Evite Spam**: Use delays entre ações para evitar spam

### **Padrões de Design**

```lua
-- Padrão Strategy para diferentes modos de combate
local CombatStrategy = {
    strategies = {},
    
    addStrategy = function(name, strategy)
        CombatStrategy.strategies[name] = strategy
    end,
    
    executeStrategy = function(name, context)
        local strategy = CombatStrategy.strategies[name]
        if strategy then
            strategy(context)
        end
    end
}

-- Estratégias de combate
CombatStrategy.addStrategy("aggressive", function(context)
    g_game.setFightMode(Otc.FightOffensive)
    g_game.setChaseMode(Otc.ChaseOpponent)
end)

CombatStrategy.addStrategy("defensive", function(context)
    g_game.setFightMode(Otc.FightDefensive)
    g_game.setChaseMode(Otc.DontChase)
end)

CombatStrategy.addStrategy("balanced", function(context)
    g_game.setFightMode(Otc.FightBalanced)
    g_game.setChaseMode(Otc.ChaseOpponent)
end)
```

---

## 📚 **Referências e Links**

### **Arquivos Relacionados**
- [[otclient_sistema_mapas|Sistema de Mapas]]
- [[otclient_sistema_criaturas|Sistema de Criaturas]]
- [[otclient_sistema_inventario|Sistema de Inventário]]

### **APIs Principais**
- `g_game`: API principal do sistema de jogo
- `g_map`: API do sistema de mapas
- `LocalPlayer`: Classe do jogador local
- `Creature`: Classe base para criaturas

### **Constantes Importantes**
```lua
-- Modos de luta
Otc.FightOffensive = 0
Otc.FightBalanced = 1
Otc.FightDefensive = 2

-- Modos de perseguição
Otc.DontChase = 0
Otc.ChaseOpponent = 1

-- Tipos de caveira
SkullYellow = 1
SkullGreen = 2
SkullWhite = 3
SkullRed = 4
SkullBlack = 5
SkullOrange = 6
```

---

> [!success] **Conclusão**
> O Sistema de Combate do OTClient fornece ferramentas poderosas para automação de combate, gerenciamento de alvos e estratégias de luta, permitindo criar sistemas sofisticados de auto-combate.

---

**📖 Próximo**: [[otclient_sistema_inventario|Sistema de Inventário]] | **🔙 Anterior**: [[otclient_sistema_mapas|Sistema de Mapas]] 