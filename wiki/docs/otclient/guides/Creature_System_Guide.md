
# Sistema de Criaturas - OTClient Redemption

Documentação completa do sistema de criaturas do OTClient, incluindo jogadores, NPCs, monstros e sistema de battle.


---

## 📋 Índice 📋

1. [Visão Geral](#-visão-geral)
2. [Creature Base](#-creature-base)
3. [Tipos de Criaturas](#-tipos-de-criaturas)
4. [Sistema Visual](#-sistema-visual)
5. [Estados e Propriedades](#-estados-e-propriedades)
6. [Sistema de Battle](#-sistema-de-battle)
7. [Eventos e Callbacks](#-eventos-e-callbacks)
8. [Pathfinding e Movimento](#-pathfinding-e-movimento)
9. [Sistema de Outfit](#-sistema-de-outfit)
10. [Exemplos Práticos](#-exemplos-práticos)


---

## 🎯 Visão Geral 🎯

O sistema de criaturas do OTClient gerencia todas as entidades vivas do jogo, incluindo jogadores, NPCs, monstros e summons. Cada criatura possui propriedades visuais, estados de combate e comportamentos específicos.

### Hierarquia de Criaturas 📝

#### Nível Basic
```lua
-- Hierarquia básica
Thing
├── Creature (base para todas as criaturas)
    ├── Player (jogadores)
    ├── Npc (NPCs)
    ├── Monster (monstros)
    └── LocalPlayer (jogador local - herda de Player)
```

#### Nível Intermediate
```lua
-- Hierarquia básica
Thing
├── Creature (base para todas as criaturas)
    ├── Player (jogadores)
    ├── Npc (NPCs)
    ├── Monster (monstros)
    └── LocalPlayer (jogador local - herda de Player)
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
-- Hierarquia básica
Thing
├── Creature (base para todas as criaturas)
    ├── Player (jogadores)
    ├── Npc (NPCs)
    ├── Monster (monstros)
    └── LocalPlayer (jogador local - herda de Player)
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

### Constantes de Tipo 📝

#### Nível Basic
```lua
-- Tipos de criatura
CreatureTypePlayer = 0        -- Jogador
CreatureTypeMonster = 1       -- Monstro
CreatureTypeNpc = 2          -- NPC
CreatureTypeSummonOwn = 3    -- Summon próprio
CreatureTypeSummonOther = 4  -- Summon de outro jogador
CreatureTypeHidden = 5       -- Criatura oculta

-- Ícones de NPC
NpcIconNone = 0              -- Sem ícone
NpcIconChat = 1              -- Pode conversar
NpcIconTrade = 2             -- Pode comercializar
NpcIconQuest = 3             -- Tem quest
NpcIconTradeQuest = 4        -- Comércio e quest
```

#### Nível Intermediate
```lua
-- Tipos de criatura
CreatureTypePlayer = 0        -- Jogador
CreatureTypeMonster = 1       -- Monstro
CreatureTypeNpc = 2          -- NPC
CreatureTypeSummonOwn = 3    -- Summon próprio
CreatureTypeSummonOther = 4  -- Summon de outro jogador
CreatureTypeHidden = 5       -- Criatura oculta

-- Ícones de NPC
NpcIconNone = 0              -- Sem ícone
NpcIconChat = 1              -- Pode conversar
NpcIconTrade = 2             -- Pode comercializar
NpcIconQuest = 3             -- Tem quest
NpcIconTradeQuest = 4        -- Comércio e quest
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
-- Tipos de criatura
CreatureTypePlayer = 0        -- Jogador
CreatureTypeMonster = 1       -- Monstro
CreatureTypeNpc = 2          -- NPC
CreatureTypeSummonOwn = 3    -- Summon próprio
CreatureTypeSummonOther = 4  -- Summon de outro jogador
CreatureTypeHidden = 5       -- Criatura oculta

-- Ícones de NPC
NpcIconNone = 0              -- Sem ícone
NpcIconChat = 1              -- Pode conversar
NpcIconTrade = 2             -- Pode comercializar
NpcIconQuest = 3             -- Tem quest
NpcIconTradeQuest = 4        -- Comércio e quest
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


---

## 🧬 Creature Base 📋

### Propriedades Básicas 📝

#### Nível Basic
```lua
-- Obter criatura
local creature = g_map.getCreatureById(id)
local player = g_game.getLocalPlayer()
-- Informações básicas
local id = creature:getId()               -- ID único da criatura
local name = creature:getName()           -- Nome
local pos = creature:getPosition()        -- Posição atual
local direction = creature:getDirection() -- Direção (North, South, etc.)
-- Tile e posicionamento
local tile = creature:getTile()           -- Tile onde está
-- Verificações de tipo
local isPlayer = creature:isPlayer()      -- É jogador
local isNpc = creature:isNpc()           -- É NPC
local isMonster = creature:isMonster()    -- É monstro
local isLocalPlayer = creature:isLocalPlayer() -- É o jogador local
-- Estados básicos
local dead = creature:isDead()            -- Está morto
local walking = creature:isWalking()      -- Está andando
local invisible = creature:isInvisible()  -- Está invisível
local highlighted = creature:isHighlighted() -- Está destacado
```

#### Nível Intermediate
```lua
-- Obter criatura
local creature = g_map.getCreatureById(id)
local player = g_game.getLocalPlayer()

-- Informações básicas
local id = creature:getId()               -- ID único da criatura
local name = creature:getName()           -- Nome
local pos = creature:getPosition()        -- Posição atual
local direction = creature:getDirection() -- Direção (North, South, etc.)

-- Tile e posicionamento
local tile = creature:getTile()           -- Tile onde está
creature:setPosition(newPosition)         -- Define nova posição (apenas visual)

-- Verificações de tipo
local isPlayer = creature:isPlayer()      -- É jogador
local isNpc = creature:isNpc()           -- É NPC
local isMonster = creature:isMonster()    -- É monstro
local isLocalPlayer = creature:isLocalPlayer() -- É o jogador local

-- Estados básicos
local dead = creature:isDead()            -- Está morto
local walking = creature:isWalking()      -- Está andando
local invisible = creature:isInvisible()  -- Está invisível
local highlighted = creature:isHighlighted() -- Está destacado
```

#### Nível Advanced
```lua
-- Obter criatura
local creature = g_map.getCreatureById(id)
local player = g_game.getLocalPlayer()

-- Informações básicas
local id = creature:getId()               -- ID único da criatura
local name = creature:getName()           -- Nome
local pos = creature:getPosition()        -- Posição atual
local direction = creature:getDirection() -- Direção (North, South, etc.)

-- Tile e posicionamento
local tile = creature:getTile()           -- Tile onde está
creature:setPosition(newPosition)         -- Define nova posição (apenas visual)

-- Verificações de tipo
local isPlayer = creature:isPlayer()      -- É jogador
local isNpc = creature:isNpc()           -- É NPC
local isMonster = creature:isMonster()    -- É monstro
local isLocalPlayer = creature:isLocalPlayer() -- É o jogador local

-- Estados básicos
local dead = creature:isDead()            -- Está morto
local walking = creature:isWalking()      -- Está andando
local invisible = creature:isInvisible()  -- Está invisível
local highlighted = creature:isHighlighted() -- Está destacado
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

### Saúde e Estatísticas 📝

#### Nível Basic
```lua
-- Sistema de HP
local health = creature:getHealth()       -- HP atual
local maxHealth = creature:getMaxHealth() -- HP máximo
local healthPercent = creature:getHealthPercent() -- Percentual (0-100)

-- Para jogadores (se aplicável)
if creature:isPlayer() then
    local mana = creature:getMana()       -- Mana atual
    local maxMana = creature:getMaxMana() -- Mana máxima
    local level = creature:getLevel()     -- Nível
    local vocation = creature:getVocation() -- Vocação
    local experience = creature:getExperience() -- Experiência
    
    -- Skills
    local skillLevel = creature:getSkillLevel(Otc.Skill.Sword)
    local skillPercent = creature:getSkillLevelPercent(Otc.Skill.Sword)
    
    -- Outros atributos
    local soul = creature:getSoul()       -- Soul points
    local stamina = creature:getStamina() -- Stamina (minutos)
    local capacity = creature:getCapacity() -- Capacidade
    local food = creature:getFood()       -- Food time
    local blessings = creature:getBlessings() -- Número de blessings
end
```

#### Nível Intermediate
```lua
-- Sistema de HP
local health = creature:getHealth()       -- HP atual
local maxHealth = creature:getMaxHealth() -- HP máximo
local healthPercent = creature:getHealthPercent() -- Percentual (0-100)

-- Para jogadores (se aplicável)
if creature:isPlayer() then
    local mana = creature:getMana()       -- Mana atual
    local maxMana = creature:getMaxMana() -- Mana máxima
    local level = creature:getLevel()     -- Nível
    local vocation = creature:getVocation() -- Vocação
    local experience = creature:getExperience() -- Experiência
    
    -- Skills
    local skillLevel = creature:getSkillLevel(Otc.Skill.Sword)
    local skillPercent = creature:getSkillLevelPercent(Otc.Skill.Sword)
    
    -- Outros atributos
    local soul = creature:getSoul()       -- Soul points
    local stamina = creature:getStamina() -- Stamina (minutos)
    local capacity = creature:getCapacity() -- Capacidade
    local food = creature:getFood()       -- Food time
    local blessings = creature:getBlessings() -- Número de blessings
end
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
-- Sistema de HP
local health = creature:getHealth()       -- HP atual
local maxHealth = creature:getMaxHealth() -- HP máximo
local healthPercent = creature:getHealthPercent() -- Percentual (0-100)

-- Para jogadores (se aplicável)
if creature:isPlayer() then
    local mana = creature:getMana()       -- Mana atual
    local maxMana = creature:getMaxMana() -- Mana máxima
    local level = creature:getLevel()     -- Nível
    local vocation = creature:getVocation() -- Vocação
    local experience = creature:getExperience() -- Experiência
    
    -- Skills
    local skillLevel = creature:getSkillLevel(Otc.Skill.Sword)
    local skillPercent = creature:getSkillLevelPercent(Otc.Skill.Sword)
    
    -- Outros atributos
    local soul = creature:getSoul()       -- Soul points
    local stamina = creature:getStamina() -- Stamina (minutos)
    local capacity = creature:getCapacity() -- Capacidade
    local food = creature:getFood()       -- Food time
    local blessings = creature:getBlessings() -- Número de blessings
end
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


---

## 👥 Tipos de Criaturas 📋

### Player 📝

```lua
-- Verificar se é jogador
if creature:isPlayer() then
    -- Verificação condicional
    -- Propriedades específicas de jogador
    local vocation = creature:getVocation()
    local level = creature:getLevel()
    local experience = creature:getExperience()
    
    -- Guild
    --  Guild (traduzido)
    local guildName = creature:getGuildName()
    local guildRank = creature:getGuildRank()
    
    -- Party
    --  Party (traduzido)
    local inParty = creature:isInParty()
    local partyMember = creature:isPartyMember()
    local partyLeader = creature:isPartyLeader()
    local partySharedExp = creature:isPartySharedExperienceActive()
    
    -- Guerra
    --  Guerra (traduzido)
    local isWar = creature:isWar()
    local enemy = creature:isEnemy()
    
    print("Jogador:", name, "Level:", level, "Vocação:", vocation)
end
```

### NPC 📝

#### Nível Basic
```lua
-- Verificar se é NPC
if creature:isNpc() then
    -- Ícones de NPC
    local iconId = creature:getIcon()
    
    -- Verificar tipo de interação disponível
    if iconId == NpcIconChat then
        print("NPC pode conversar")
    elseif iconId == NpcIconTrade then
        print("NPC pode comercializar")
    elseif iconId == NpcIconQuest then
        print("NPC tem quest")
    elseif iconId == NpcIconTradeQuest then
        print("NPC pode comercializar e tem quest")
    end
    
    -- Interação
    g_game.look(creature)  -- "Olhar" o NPC
    g_game.talkChannel(TalkType.NpcTo, 0, "hi") -- Falar com NPC
end
```

#### Nível Intermediate
```lua
-- Verificar se é NPC
if creature:isNpc() then
    -- Ícones de NPC
    local iconId = creature:getIcon()
    
    -- Verificar tipo de interação disponível
    if iconId == NpcIconChat then
        print("NPC pode conversar")
    elseif iconId == NpcIconTrade then
        print("NPC pode comercializar")
    elseif iconId == NpcIconQuest then
        print("NPC tem quest")
    elseif iconId == NpcIconTradeQuest then
        print("NPC pode comercializar e tem quest")
    end
    
    -- Interação
    g_game.look(creature)  -- "Olhar" o NPC
    g_game.talkChannel(TalkType.NpcTo, 0, "hi") -- Falar com NPC
end
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
-- Verificar se é NPC
if creature:isNpc() then
    -- Ícones de NPC
    local iconId = creature:getIcon()
    
    -- Verificar tipo de interação disponível
    if iconId == NpcIconChat then
        print("NPC pode conversar")
    elseif iconId == NpcIconTrade then
        print("NPC pode comercializar")
    elseif iconId == NpcIconQuest then
        print("NPC tem quest")
    elseif iconId == NpcIconTradeQuest then
        print("NPC pode comercializar e tem quest")
    end
    
    -- Interação
    g_game.look(creature)  -- "Olhar" o NPC
    g_game.talkChannel(TalkType.NpcTo, 0, "hi") -- Falar com NPC
end
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

### Monster 📝

```lua
-- Verificar se é monstro
if creature:isMonster() then
    -- Verificação condicional
    -- Verificar se é summon
    local isSummon = creature:getType() == CreatureTypeSummonOwn or 
                     creature:getType() == CreatureTypeSummonOther
    
    if isSummon then
    -- Verificação condicional
        print("É um summon")
        if creature:getType() == CreatureTypeSummonOwn then
    -- Verificação condicional
            print("É seu summon")
        else
            print("É summon de outro jogador")
        end
    else
        print("Monstro selvagem:", name)
    end
    
    -- Combate
    --  Combate (traduzido)
    g_game.attack(creature)    -- Atacar
    g_game.follow(creature)    -- Seguir
    g_game.look(creature)      -- Examinar
end
```

### LocalPlayer (Jogador Local) 📝

#### Nível Basic
```lua
-- O jogador local é especial
local player = g_game.getLocalPlayer()

if player then
    -- Todas as propriedades de Player, mais:
    
    -- Inventário
    local item = player:getInventoryItem(InventorySlotHead)
    local items = player:getInventoryItems()
    
    -- Containers
    local containers = player:getContainers()
    
    -- Configurações
    local chaseMode = player:getChaseMode()
    local fightMode = player:getFightMode()
    local pvpMode = player:getPvpMode()
    
    -- Estados especiais
    local pz = player:isPzLocked()
    local fighting = player:isFighting()
    local mounted = player:isMounted()
    
    print("Jogador local:", player:getName())
    print("HP:", player:getHealth() .. "/" .. player:getMaxHealth())
    print("Level:", player:getLevel())
end
```

#### Nível Intermediate
```lua
-- O jogador local é especial
local player = g_game.getLocalPlayer()

if player then
    -- Todas as propriedades de Player, mais:
    
    -- Inventário
    local item = player:getInventoryItem(InventorySlotHead)
    local items = player:getInventoryItems()
    
    -- Containers
    local containers = player:getContainers()
    
    -- Configurações
    local chaseMode = player:getChaseMode()
    local fightMode = player:getFightMode()
    local pvpMode = player:getPvpMode()
    
    -- Estados especiais
    local pz = player:isPzLocked()
    local fighting = player:isFighting()
    local mounted = player:isMounted()
    
    print("Jogador local:", player:getName())
    print("HP:", player:getHealth() .. "/" .. player:getMaxHealth())
    print("Level:", player:getLevel())
end
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
-- O jogador local é especial
local player = g_game.getLocalPlayer()

if player then
    -- Todas as propriedades de Player, mais:
    
    -- Inventário
    local item = player:getInventoryItem(InventorySlotHead)
    local items = player:getInventoryItems()
    
    -- Containers
    local containers = player:getContainers()
    
    -- Configurações
    local chaseMode = player:getChaseMode()
    local fightMode = player:getFightMode()
    local pvpMode = player:getPvpMode()
    
    -- Estados especiais
    local pz = player:isPzLocked()
    local fighting = player:isFighting()
    local mounted = player:isMounted()
    
    print("Jogador local:", player:getName())
    print("HP:", player:getHealth() .. "/" .. player:getMaxHealth())
    print("Level:", player:getLevel())
end
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


---

## 🎨 Sistema Visual ⚙️

### Skulls (Caveiras) 📝

```lua
-- Tipos de skull
    --  Tipos de skull (traduzido)
SkullNone = 0        -- Sem skull
SkullYellow = 1      -- Amarela (jogador matou outros)
SkullGreen = 2       -- Verde (pode ser atacado em áreas de PvP)
SkullWhite = 3       -- Branca (ataque injustificado)
SkullRed = 4         -- Vermelha (PK)
SkullBlack = 5       -- Preta (PK extremo)
SkullOrange = 6      -- Laranja (special)

-- Gerenciar skulls
    --  Gerenciar skulls (traduzido)
local skull = creature:getSkull()
creature:setSkull(SkullRed)  -- Define skull (apenas visual)

-- Obter imagem do skull
    --  Obter imagem do skull (traduzido)
function getSkullImagePath(skullId)
    -- Função: getSkullImagePath
    local paths = {
        [SkullYellow] = '/images/game/skulls/skull_yellow',
        [SkullGreen] = '/images/game/skulls/skull_green',
        [SkullWhite] = '/images/game/skulls/skull_white',
        [SkullRed] = '/images/game/skulls/skull_red',
        [SkullBlack] = '/images/game/skulls/skull_black',
        [SkullOrange] = '/images/game/skulls/skull_orange'
    }
    return paths[skullId]
end
```

### Shields (Guild) 📝

#### Nível Basic
```lua
-- Tipos de shield (guild)
ShieldNone = 0
ShieldWhiteYellow = 1       -- Líder da guild
ShieldWhiteBlue = 2         -- Vice-líder
ShieldBlue = 3              -- Membro comum
ShieldYellow = 4            -- Outro tipo de membro
ShieldBlueSharedExp = 5     -- Com exp compartilhada
ShieldYellowSharedExp = 6   -- Líder com exp compartilhada
ShieldGray = 7              -- Membro sem rank

-- Gerenciar shields
local shield = creature:getShield()
creature:setShield(ShieldBlue)

-- Verificar se pisca
function getShieldImagePathAndBlink(shieldId)
    local shieldData = {
        [ShieldWhiteYellow] = {'/images/game/shields/shield_yellow_white', false},
        [ShieldWhiteBlue] = {'/images/game/shields/shield_blue_white', false},
        [ShieldBlue] = {'/images/game/shields/shield_blue', false},
        [ShieldYellow] = {'/images/game/shields/shield_yellow', false},
        [ShieldBlueSharedExp] = {'/images/game/shields/shield_blue_shared', false},
        [ShieldYellowSharedExp] = {'/images/game/shields/shield_yellow_shared', false},
        [ShieldBlueNoSharedExpBlink] = {'/images/game/shields/shield_blue_not_shared', true},
        [ShieldYellowNoSharedExpBlink] = {'/images/game/shields/shield_yellow_not_shared', true},
        [ShieldGray] = {'/images/game/shields/shield_gray', false}
    }
    
    local data = shieldData[shieldId]
    if data then
        return data[1], data[2] -- path, blink
    end
    return nil, false
end
```

#### Nível Intermediate
```lua
-- Tipos de shield (guild)
ShieldNone = 0
ShieldWhiteYellow = 1       -- Líder da guild
ShieldWhiteBlue = 2         -- Vice-líder
ShieldBlue = 3              -- Membro comum
ShieldYellow = 4            -- Outro tipo de membro
ShieldBlueSharedExp = 5     -- Com exp compartilhada
ShieldYellowSharedExp = 6   -- Líder com exp compartilhada
ShieldGray = 7              -- Membro sem rank

-- Gerenciar shields
local shield = creature:getShield()
creature:setShield(ShieldBlue)

-- Verificar se pisca
function getShieldImagePathAndBlink(shieldId)
    local shieldData = {
        [ShieldWhiteYellow] = {'/images/game/shields/shield_yellow_white', false},
        [ShieldWhiteBlue] = {'/images/game/shields/shield_blue_white', false},
        [ShieldBlue] = {'/images/game/shields/shield_blue', false},
        [ShieldYellow] = {'/images/game/shields/shield_yellow', false},
        [ShieldBlueSharedExp] = {'/images/game/shields/shield_blue_shared', false},
        [ShieldYellowSharedExp] = {'/images/game/shields/shield_yellow_shared', false},
        [ShieldBlueNoSharedExpBlink] = {'/images/game/shields/shield_blue_not_shared', true},
        [ShieldYellowNoSharedExpBlink] = {'/images/game/shields/shield_yellow_not_shared', true},
        [ShieldGray] = {'/images/game/shields/shield_gray', false}
    }
    
    local data = shieldData[shieldId]
    if data then
        return data[1], data[2] -- path, blink
    end
    return nil, false
end
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
-- Tipos de shield (guild)
ShieldNone = 0
ShieldWhiteYellow = 1       -- Líder da guild
ShieldWhiteBlue = 2         -- Vice-líder
ShieldBlue = 3              -- Membro comum
ShieldYellow = 4            -- Outro tipo de membro
ShieldBlueSharedExp = 5     -- Com exp compartilhada
ShieldYellowSharedExp = 6   -- Líder com exp compartilhada
ShieldGray = 7              -- Membro sem rank

-- Gerenciar shields
local shield = creature:getShield()
creature:setShield(ShieldBlue)

-- Verificar se pisca
function getShieldImagePathAndBlink(shieldId)
    local shieldData = {
        [ShieldWhiteYellow] = {'/images/game/shields/shield_yellow_white', false},
        [ShieldWhiteBlue] = {'/images/game/shields/shield_blue_white', false},
        [ShieldBlue] = {'/images/game/shields/shield_blue', false},
        [ShieldYellow] = {'/images/game/shields/shield_yellow', false},
        [ShieldBlueSharedExp] = {'/images/game/shields/shield_blue_shared', false},
        [ShieldYellowSharedExp] = {'/images/game/shields/shield_yellow_shared', false},
        [ShieldBlueNoSharedExpBlink] = {'/images/game/shields/shield_blue_not_shared', true},
        [ShieldYellowNoSharedExpBlink] = {'/images/game/shields/shield_yellow_not_shared', true},
        [ShieldGray] = {'/images/game/shields/shield_gray', false}
    }
    
    local data = shieldData[shieldId]
    if data then
        return data[1], data[2] -- path, blink
    end
    return nil, false
end
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

### Emblems (Guerra) 📝

```lua
-- Tipos de emblem
    --  Tipos de emblem (traduzido)
EmblemNone = 0
EmblemGreen = 1      -- Aliado
EmblemRed = 2        -- Inimigo
EmblemBlue = 3       -- Neutro/outro
EmblemMember = 4     -- Membro da guild
EmblemOther = 5      -- Outro tipo

-- Gerenciar emblems
    --  Gerenciar emblems (traduzido)
local emblem = creature:getEmblem()
creature:setEmblem(EmblemRed)

function getEmblemImagePath(emblemId)
    -- Função: getEmblemImagePath
    local paths = {
        [EmblemGreen] = '/images/game/emblems/emblem_green',
        [EmblemRed] = '/images/game/emblems/emblem_red',
        [EmblemBlue] = '/images/game/emblems/emblem_blue',
        [EmblemMember] = '/images/game/emblems/emblem_member',
        [EmblemOther] = '/images/game/emblems/emblem_other'
    }
    return paths[emblemId]
end
```

### Luz e Efeitos 📝

```lua
-- Sistema de luz
    --  Sistema de luz (traduzido)
local light = creature:getLight()
creature:setLight(light)  -- Define luz

-- Efeitos visuais
    --  Efeitos visuais (traduzido)
creature:setHighlighted(true)  -- Destaca criatura
local highlighted = creature:isHighlighted()

-- Marcação personalizada
creature:setMarked(true)   -- Marca criatura
local marked = creature:isMarked()

-- Opacidade
    --  Opacidade (traduzido)
creature:setOpacity(0.5)   -- Semi-transparente
local opacity = creature:getOpacity()
```


---

## 📊 Estados e Propriedades 📋

### Speed e Movimento 📝

#### Nível Basic
```lua
-- Velocidade
local speed = creature:getSpeed()         -- Velocidade atual
creature:setSpeed(speed)                  -- Define velocidade (visual)

-- Direção
local direction = creature:getDirection() -- North, South, East, West
creature:setDirection(North)              -- Define direção

-- Movimento
local walking = creature:isWalking()      -- Está se movendo
local lastStepCost = creature:getLastStepCost() -- Custo do último passo
local stepDuration = creature:getStepDuration() -- Duração do passo
```

#### Nível Intermediate
```lua
-- Velocidade
local speed = creature:getSpeed()         -- Velocidade atual
creature:setSpeed(speed)                  -- Define velocidade (visual)

-- Direção
local direction = creature:getDirection() -- North, South, East, West
creature:setDirection(North)              -- Define direção

-- Movimento
local walking = creature:isWalking()      -- Está se movendo
local lastStepCost = creature:getLastStepCost() -- Custo do último passo
local stepDuration = creature:getStepDuration() -- Duração do passo
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
-- Velocidade
local speed = creature:getSpeed()         -- Velocidade atual
creature:setSpeed(speed)                  -- Define velocidade (visual)

-- Direção
local direction = creature:getDirection() -- North, South, East, West
creature:setDirection(North)              -- Define direção

-- Movimento
local walking = creature:isWalking()      -- Está se movendo
local lastStepCost = creature:getLastStepCost() -- Custo do último passo
local stepDuration = creature:getStepDuration() -- Duração do passo
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

### Informações Avançadas 📝

#### Nível Basic
```lua
-- Distância
local distance = creature:getDistanceFromLocalPlayer() -- Distância do jogador

-- Master (para summons)
local master = creature:getMaster()       -- Dono do summon (se aplicável)
local hasMaster = creature:hasMaster()    -- Tem dono

-- Verificações especiais
local autowalking = creature:isAutoWalking() -- Está em auto-walk
local following = creature:isFollowing()     -- Está seguindo alguém
local blocking = creature:isBlocking()       -- Está bloqueando passagem
```

#### Nível Intermediate
```lua
-- Distância
local distance = creature:getDistanceFromLocalPlayer() -- Distância do jogador

-- Master (para summons)
local master = creature:getMaster()       -- Dono do summon (se aplicável)
local hasMaster = creature:hasMaster()    -- Tem dono

-- Verificações especiais
local autowalking = creature:isAutoWalking() -- Está em auto-walk
local following = creature:isFollowing()     -- Está seguindo alguém
local blocking = creature:isBlocking()       -- Está bloqueando passagem
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
-- Distância
local distance = creature:getDistanceFromLocalPlayer() -- Distância do jogador

-- Master (para summons)
local master = creature:getMaster()       -- Dono do summon (se aplicável)
local hasMaster = creature:hasMaster()    -- Tem dono

-- Verificações especiais
local autowalking = creature:isAutoWalking() -- Está em auto-walk
local following = creature:isFollowing()     -- Está seguindo alguém
local blocking = creature:isBlocking()       -- Está bloqueando passagem
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


---

## ⚔️ Sistema de Battle ⚙️

### Battle List 📝

```lua
-- Obter criaturas na battle list
    --  Obter criaturas na battle list (traduzido)
local battleCreatures = {}

-- Filtrar criaturas na tela
    --  Filtrar criaturas na tela (traduzido)
local spectators = g_map.getSpectators(g_game.getLocalPlayer():getPosition(), false, 7, 7)

for _, creature in ipairs(spectators) do
    -- Loop de repetição
    if not creature:isLocalPlayer() then
    -- Verificação condicional
        table.insert(battleCreatures, creature)
    end
end

-- Ordenar por distância
table.sort(battleCreatures, function(a, b)
    return a:getDistanceFromLocalPlayer() < b:getDistanceFromLocalPlayer()
end)
```

### Combate 📝

```lua
-- Atacar criatura
    --  Atacar criatura (traduzido)
g_game.attack(creature)

-- Seguir criatura
    --  Seguir criatura (traduzido)
g_game.follow(creature)

-- Parar combate
    --  Parar combate (traduzido)
g_game.stop()

-- Verificar combate atual
    --  Verificar combate atual (traduzido)
local attacking = g_game.getAttackingCreature()
local following = g_game.getFollowingCreature()

-- Configurações de combate
g_game.setChaseMode(ChaseOpponent)     -- Perseguir oponente
g_game.setFightMode(FightBalanced)     -- Modo de luta balanceado
g_game.setPvpMode(WhiteDove)           -- Modo PvP

-- Modos disponíveis
-- Chase: DontChase, ChaseOpponent
    --  Chase: DontChase, ChaseOpponent (traduzido)
-- Fight: FightOffensive, FightBalanced, FightDefensive
    --  Fight: FightOffensive, FightBalanced, FightDefensive (traduzido)
-- PvP: WhiteDove, WhiteHand, YellowHand, RedFist
    --  PvP: WhiteDove, WhiteHand, YellowHand, RedFist (traduzido)
```

### Battle Button System 📝

```lua
-- Sistema de botões de battle (como usado no módulo game_battle)
local battleButtons = {}

function createBattleButton(creature)
    -- Função: createBattleButton
    local button = g_ui.createWidget('BattleButton')
    button:setCreature(creature)
    button:setText(creature:getName())
    
    -- Cores baseadas no tipo
    --  Cores baseadas no tipo (traduzido)
    if creature:isPlayer() then
    -- Verificação condicional
        button:setColor('#FFFFFF')
    elseif creature:isNpc() then
        button:setColor('#FFFF00')
    elseif creature:isMonster() then
        button:setColor('#FF6666')
    end
    
    -- Eventos
    --  Eventos (traduzido)
    button.onClick = function()
        g_game.attack(creature)
    end
    
    button.onDoubleClick = function()
        g_game.look(creature)
    end
    
    battleButtons[creature:getId()] = button
    return button
end

function updateBattleButton(creature)
    -- Função: updateBattleButton
    local button = battleButtons[creature:getId()]
    if button then
    -- Verificação condicional
        -- Atualizar HP
    --  Atualizar HP (traduzido)
        local healthPercent = creature:getHealthPercent()
        button:setHealthPercent(healthPercent)
        
        -- Cor baseada no HP
    --  Cor baseada no HP (traduzido)
        if healthPercent < 30 then
    -- Verificação condicional
            button:setHealthColor('#FF0000')
        elseif healthPercent < 70 then
            button:setHealthColor('#FFAA00')
        else
            button:setHealthColor('#00FF00')
        end
    end
end
```


---

## 📡 Eventos e Callbacks 📋

### Eventos Principais 📝

#### Inicialização e Configuração
```lua
-- Conectar eventos de criatura
connect(Creature, {
    onAppear = function(creature)
        print("Criatura apareceu:", creature:getName())
        -- Adicionar à battle list, criar botão, etc.
    end,
    
    onDisappear = function(creature)
        print("Criatura desapareceu:", creature:getName())
        -- Remover da battle list, destruir botão, etc.
    end,
    
    onPositionChange = function(creature, newPos, oldPos)
        print("Criatura moveu:", creature:getName())
        print("De:", oldPos.x, oldPos.y, oldPos.z)
        print("Para:", newPos.x, newPos.y, newPos.z)
    end,
    
    onHealthPercentChange = function(creature, healthPercent)
        print("HP mudou:", creature:getName(), healthPercent .. "%")
        updateBattleButton(creature)
    end,
```

#### Funcionalidade 1
```lua
    
    onSkullChange = function(creature, skull)
        print("Skull mudou:", creature:getName(), skull)
    end,
    
    onShieldChange = function(creature, shield)
        print("Shield mudou:", creature:getName(), shield)
    end,
    
    onEmblemChange = function(creature, emblem)
        print("Emblem mudou:", creature:getName(), emblem)
    end,
    
    onOutfitChange = function(creature, outfit, oldOutfit)
        print("Outfit mudou:", creature:getName())
    end,
    
    onDirectionChange = function(creature, direction, oldDirection)
        print("Direção mudou:", creature:getName(), direction)
    end,
    
    onWalk = function(creature, oldPos, newPos)
        print("Criatura andou:", creature:getName())
    end
```

#### Funcionalidade 2
```lua
})

-- Eventos específicos do jogador local
connect(LocalPlayer, {
    onPositionChange = function(localPlayer, newPos, oldPos)
        print("Jogador moveu para:", newPos.x, newPos.y, newPos.z)
        -- Atualizar lista de criaturas próximas
        updateNearbyCreatures()
    end,
    
    onStatsChange = function(localPlayer)
        print("Stats do jogador mudaram")
        print("HP:", localPlayer:getHealth() .. "/" .. localPlayer:getMaxHealth())
        print("Mana:", localPlayer:getMana() .. "/" .. localPlayer:getMaxMana())
    end,
    
    onLevelChange = function(localPlayer, level, levelPercent)
        print("Level up! Novo level:", level)
    end,
    
    onExperienceChange = function(localPlayer, experience)
        print("Experiência:", experience)
    end,
```

#### Finalização
```lua
    
    onSkillChange = function(localPlayer, skillId, level, levelPercent)
        print("Skill mudou:", skillId, "Level:", level, "Percent:", levelPercent)
    end
})
```

### Eventos de Combate 📝

```lua
connect(g_game, {
    onAttackingCreatureChange = function(creature, oldCreature)
        if creature then
    -- Verificação condicional
            print("Começou a atacar:", creature:getName())
        else
            print("Parou de atacar")
        end
        
        if oldCreature then
    -- Verificação condicional
            print("Parou de atacar:", oldCreature:getName())
        end
    end,
    
    onFollowingCreatureChange = function(creature, oldCreature)
        if creature then
    -- Verificação condicional
            print("Começou a seguir:", creature:getName())
        else
            print("Parou de seguir")
        end
    end,
    
    onChaseModeChange = function(chaseMode)
        print("Modo de perseguição:", chaseMode)
    end,
    
    onFightModeChange = function(fightMode)
        print("Modo de luta:", fightMode)
    end,
    
    onPvpModeChange = function(pvpMode)
        print("Modo PvP:", pvpMode)
    end
})
```


---

## 🧭 Pathfinding e Movimento 📋

### Sistema de Pathfinding 📝

```lua
-- Encontrar caminho para uma criatura
    --  Encontrar caminho para uma criatura (traduzido)
function findPathToCreature(creature)
    -- Função: findPathToCreature
    local localPlayer = g_game.getLocalPlayer()
    if not localPlayer then return nil end
    -- Verificação condicional
    
    local fromPos = localPlayer:getPosition()
    local toPos = creature:getPosition()
    
    -- Buscar caminho
    --  Buscar caminho (traduzido)
    local path = g_map.findPath(fromPos, toPos, 100)
    return path
end

-- Auto-walk para criatura
    --  Auto-walk para criatura (traduzido)
function walkToCreature(creature)
    -- Função: walkToCreature
    local path = findPathToCreature(creature)
    if path and #path > 0 then
    -- Verificação condicional
        g_game.autoWalk(path)
        return true
    end
    return false
end

-- Verificar se pode alcançar criatura
function canReachCreature(creature, maxDistance)
    -- Função: canReachCreature
    maxDistance = maxDistance or 8
    local localPlayer = g_game.getLocalPlayer()
    if not localPlayer then return false end
    -- Verificação condicional
    
    local fromPos = localPlayer:getPosition()
    local toPos = creature:getPosition()
    
    return g_map.canReach(fromPos, toPos, maxDistance)
end
```

### Cálculos de Distância 📝

#### Nível Basic
```lua
-- Distância entre duas posições
function getDistanceBetween(pos1, pos2)
    local dx = math.abs(pos1.x - pos2.x)
    local dy = math.abs(pos1.y - pos2.y)
    local dz = math.abs(pos1.z - pos2.z)
end
-- Ordenar criaturas por distância
function sortCreaturesByDistance(creatures)
    local localPlayer = g_game.getLocalPlayer()
    if not localPlayer then return creatures end
    local playerPos = localPlayer:getPosition()
    table.sort(creatures, function(a, b)
        local distA = getDistanceBetween(playerPos, a:getPosition())
        local distB = getDistanceBetween(playerPos, b:getPosition())
    end)
end
-- Filtrar criaturas por distância máxima
function filterCreaturesByDistance(creatures, maxDistance)
    local localPlayer = g_game.getLocalPlayer()
    if not localPlayer then return {} end
    local playerPos = localPlayer:getPosition()
    local filtered = {}
        local distance = getDistanceBetween(playerPos, creature:getPosition())
        if distance <= maxDistance then
        end
    end
end
```

#### Nível Intermediate
```lua
-- Distância entre duas posições
function getDistanceBetween(pos1, pos2)
    local dx = math.abs(pos1.x - pos2.x)
    local dy = math.abs(pos1.y - pos2.y)
    local dz = math.abs(pos1.z - pos2.z)
    
    return math.max(dx, dy, dz)
end

-- Ordenar criaturas por distância
function sortCreaturesByDistance(creatures)
    local localPlayer = g_game.getLocalPlayer()
    if not localPlayer then return creatures end
    
    local playerPos = localPlayer:getPosition()
    
    table.sort(creatures, function(a, b)
        local distA = getDistanceBetween(playerPos, a:getPosition())
        local distB = getDistanceBetween(playerPos, b:getPosition())
        return distA < distB
    end)
    
    return creatures
end

-- Filtrar criaturas por distância máxima
function filterCreaturesByDistance(creatures, maxDistance)
    local localPlayer = g_game.getLocalPlayer()
    if not localPlayer then return {} end
    
    local playerPos = localPlayer:getPosition()
    local filtered = {}
    
    for _, creature in ipairs(creatures) do
        local distance = getDistanceBetween(playerPos, creature:getPosition())
        if distance <= maxDistance then
            table.insert(filtered, creature)
        end
    end
    
    return filtered
end
```

#### Nível Advanced
```lua
-- Distância entre duas posições
function getDistanceBetween(pos1, pos2)
    local dx = math.abs(pos1.x - pos2.x)
    local dy = math.abs(pos1.y - pos2.y)
    local dz = math.abs(pos1.z - pos2.z)
    
    return math.max(dx, dy, dz)
end

-- Ordenar criaturas por distância
function sortCreaturesByDistance(creatures)
    local localPlayer = g_game.getLocalPlayer()
    if not localPlayer then return creatures end
    
    local playerPos = localPlayer:getPosition()
    
    table.sort(creatures, function(a, b)
        local distA = getDistanceBetween(playerPos, a:getPosition())
        local distB = getDistanceBetween(playerPos, b:getPosition())
        return distA < distB
    end)
    
    return creatures
end

-- Filtrar criaturas por distância máxima
function filterCreaturesByDistance(creatures, maxDistance)
    local localPlayer = g_game.getLocalPlayer()
    if not localPlayer then return {} end
    
    local playerPos = localPlayer:getPosition()
    local filtered = {}
    
    for _, creature in ipairs(creatures) do
        local distance = getDistanceBetween(playerPos, creature:getPosition())
        if distance <= maxDistance then
            table.insert(filtered, creature)
        end
    end
    
    return filtered
end
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


---

## 👕 Sistema de Outfit ⚙️

### Outfit Structure 🏗️

#### Nível Basic
```lua
-- Estrutura básica de outfit
local outfit = {
    type = 128,        -- Tipo do outfit (ID)
    head = 114,        -- Cor da cabeça
    body = 114,        -- Cor do corpo
    legs = 114,        -- Cor das pernas
    feet = 114,        -- Cor dos pés
    addons = 3,        -- Addons (0-3)
    mount = 0,         -- ID da montaria (0 = sem montaria)
    wings = 0,         -- ID das asas (se suportado)
    aura = 0           -- ID da aura (se suportado)
}

-- Gerenciar outfit da criatura
creature:setOutfit(outfit)
local currentOutfit = creature:getOutfit()

-- Verificar montaria
local mounted = creature:isMounted()
local mountId = currentOutfit.mount

-- Cores disponíveis (HSI color system)
-- Cabeça: 0-132
-- Corpo: 0-132  
-- Pernas: 0-132
-- Pés: 0-132
```

#### Nível Intermediate
```lua
-- Estrutura básica de outfit
local outfit = {
    type = 128,        -- Tipo do outfit (ID)
    head = 114,        -- Cor da cabeça
    body = 114,        -- Cor do corpo
    legs = 114,        -- Cor das pernas
    feet = 114,        -- Cor dos pés
    addons = 3,        -- Addons (0-3)
    mount = 0,         -- ID da montaria (0 = sem montaria)
    wings = 0,         -- ID das asas (se suportado)
    aura = 0           -- ID da aura (se suportado)
}

-- Gerenciar outfit da criatura
creature:setOutfit(outfit)
local currentOutfit = creature:getOutfit()

-- Verificar montaria
local mounted = creature:isMounted()
local mountId = currentOutfit.mount

-- Cores disponíveis (HSI color system)
-- Cabeça: 0-132
-- Corpo: 0-132  
-- Pernas: 0-132
-- Pés: 0-132
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
-- Estrutura básica de outfit
local outfit = {
    type = 128,        -- Tipo do outfit (ID)
    head = 114,        -- Cor da cabeça
    body = 114,        -- Cor do corpo
    legs = 114,        -- Cor das pernas
    feet = 114,        -- Cor dos pés
    addons = 3,        -- Addons (0-3)
    mount = 0,         -- ID da montaria (0 = sem montaria)
    wings = 0,         -- ID das asas (se suportado)
    aura = 0           -- ID da aura (se suportado)
}

-- Gerenciar outfit da criatura
creature:setOutfit(outfit)
local currentOutfit = creature:getOutfit()

-- Verificar montaria
local mounted = creature:isMounted()
local mountId = currentOutfit.mount

-- Cores disponíveis (HSI color system)
-- Cabeça: 0-132
-- Corpo: 0-132  
-- Pernas: 0-132
-- Pés: 0-132
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

### Outfit Utils 📝

```lua
-- Gerar outfit aleatório
function generateRandomOutfit(baseType)
    -- Função: generateRandomOutfit
    return {
        type = baseType or 128,
        head = math.random(0, 132),
        body = math.random(0, 132),
        legs = math.random(0, 132),
        feet = math.random(0, 132),
        addons = math.random(0, 3),
        mount = 0,
        wings = 0,
        aura = 0
    }
end

-- Copiar outfit de uma criatura
    --  Copiar outfit de uma criatura (traduzido)
function copyOutfit(creature)
    -- Função: copyOutfit
    return creature:getOutfit()
end

-- Comparar outfits
    --  Comparar outfits (traduzido)
function compareOutfits(outfit1, outfit2)
    -- Função: compareOutfits
    return outfit1.type == outfit2.type and
           outfit1.head == outfit2.head and
           outfit1.body == outfit2.body and
           outfit1.legs == outfit2.legs and
           outfit1.feet == outfit2.feet and
           outfit1.addons == outfit2.addons and
           outfit1.mount == outfit2.mount
end
```


---

## 💡 Exemplos Práticos 💡

### Exemplo 1: Sistema de Radar de Criaturas 🎮

#### Inicialização e Configuração
```lua
-- modules/creature_radar/creature_radar.lua
creatureRadar = {}

function creatureRadar.init()
    creatureRadar.window = g_ui.displayUI('creature_radar')
    creatureRadar.list = creatureRadar.window:getChildById('creatureList')
    creatureRadar.filterCombo = creatureRadar.window:getChildById('filterCombo')
    creatureRadar.rangeEdit = creatureRadar.window:getChildById('rangeEdit')
    
    -- Configurar filtros
    creatureRadar.filterCombo:addOption('Todos', 'all')
    creatureRadar.filterCombo:addOption('Jogadores', 'players')
    creatureRadar.filterCombo:addOption('Monstros', 'monsters')
    creatureRadar.filterCombo:addOption('NPCs', 'npcs')
    
    creatureRadar.filterCombo.onOptionChange = creatureRadar.updateList
    creatureRadar.rangeEdit.onTextChange = creatureRadar.updateList
    
    -- Conectar eventos
    connect(Creature, {
        onAppear = creatureRadar.onCreatureAppear,
        onDisappear = creatureRadar.onCreatureDisappear,
        onPositionChange = creatureRadar.onCreatureMove
    })
```

#### Funcionalidade 1
```lua
    
    -- Timer de atualização
    creatureRadar.updateEvent = scheduleEvent(creatureRadar.updateList, 1000)
end

function creatureRadar.updateList()
    local localPlayer = g_game.getLocalPlayer()
    if not localPlayer then return end
    
    local range = tonumber(creatureRadar.rangeEdit:getText()) or 7
    local filter = creatureRadar.filterCombo:getCurrentOption().data
    
    -- Obter criaturas próximas
    local spectators = g_map.getSpectators(localPlayer:getPosition(), false, range, range)
    local filtered = {}
    
    for _, creature in ipairs(spectators) do
        if not creature:isLocalPlayer() then
            local include = false
            
            if filter == 'all' then
                include = true
            elseif filter == 'players' and creature:isPlayer() then
                include = true
            elseif filter == 'monsters' and creature:isMonster() then
                include = true
            elseif filter == 'npcs' and creature:isNpc() then
                include = true
            end
```

#### Funcionalidade 2
```lua
            
            if include then
                table.insert(filtered, creature)
            end
        end
    end
    
    -- Ordenar por distância
    table.sort(filtered, function(a, b)
        return a:getDistanceFromLocalPlayer() < b:getDistanceFromLocalPlayer()
    end)
    
    -- Atualizar lista
    creatureRadar.list:destroyChildren()
    
    for _, creature in ipairs(filtered) do
        local item = g_ui.createWidget('UILabel', creatureRadar.list)
        local distance = creature:getDistanceFromLocalPlayer()
        local healthPercent = creature:getHealthPercent()
        
        item:setText(string.format("%s (Lv.%d) - %d sqm - %d%% HP", 
                                   creature:getName(),
                                   creature:getLevel() or 0,
                                   distance,
                                   healthPercent))
        
        -- Cor baseada no tipo
        if creature:isPlayer() then
            item:setColor('#FFFFFF')
        elseif creature:isNpc() then
            item:setColor('#FFFF00')
        elseif creature:isMonster() then
            item:setColor('#FF6666')
        end
```

#### Funcionalidade 3
```lua
        
        -- Eventos
        item.onClick = function()
            g_game.look(creature)
        end
        
        item.onDoubleClick = function()
            walkToCreature(creature)
        end
    end
    
    -- Próxima atualização
    creatureRadar.updateEvent = scheduleEvent(creatureRadar.updateList, 1000)
end

function creatureRadar.onCreatureAppear(creature)
    scheduleEvent(creatureRadar.updateList, 100)
end

function creatureRadar.onCreatureDisappear(creature)
    scheduleEvent(creatureRadar.updateList, 100)
end
```

#### Finalização
```lua

function creatureRadar.onCreatureMove(creature, newPos, oldPos)
    scheduleEvent(creatureRadar.updateList, 100)
end
```

### Exemplo 2: Auto-Target System 🎮

#### Inicialização e Configuração
```lua
-- modules/auto_target/auto_target.lua
autoTarget = {}

function autoTarget.init()
    autoTarget.enabled = false
    autoTarget.targets = {}
    autoTarget.currentTarget = nil
    
    autoTarget.setupInterface()
    autoTarget.loadConfiguration()
    
    connect(g_game, {
        onAttackingCreatureChange = autoTarget.onAttackingCreatureChange
    })
    
    connect(Creature, {
        onAppear = autoTarget.onCreatureAppear,
        onDisappear = autoTarget.onCreatureDisappear,
        onHealthPercentChange = autoTarget.onCreatureHealthChange
    })
end
```

#### Funcionalidade 1
```lua

function autoTarget.setupInterface()
    autoTarget.window = g_ui.displayUI('auto_target')
    autoTarget.enabledBox = autoTarget.window:getChildById('enabledBox')
    autoTarget.targetList = autoTarget.window:getChildById('targetList')
    autoTarget.addButton = autoTarget.window:getChildById('addButton')
    autoTarget.removeButton = autoTarget.window:getChildById('removeButton')
    
    autoTarget.enabledBox.onCheckChange = function(widget, checked)
        autoTarget.enabled = checked
        autoTarget.saveConfiguration()
    end
    
    autoTarget.addButton.onClick = autoTarget.addCurrentTarget
    autoTarget.removeButton.onClick = autoTarget.removeSelectedTarget
end

function autoTarget.addCurrentTarget()
    local attacking = g_game.getAttackingCreature()
    if not attacking then
        modules.game_textmessage.displayGameMessage('Nenhuma criatura sendo atacada!')
        return
    end
```

#### Funcionalidade 2
```lua
    
    local name = attacking:getName()
    if not autoTarget.targets[name] then
        autoTarget.targets[name] = {
            name = name,
            priority = 1,
            minHealth = 0,
            maxHealth = 100
        }
        
        autoTarget.updateTargetList()
        autoTarget.saveConfiguration()
        modules.game_textmessage.displayGameMessage('Alvo adicionado: ' .. name)
    else
        modules.game_textmessage.displayGameMessage('Alvo já existe: ' .. name)
    end
end

function autoTarget.removeSelectedTarget()
    local selected = autoTarget.targetList:getFocusedChild()
    if selected then
        local targetName = selected.targetName
        autoTarget.targets[targetName] = nil
        autoTarget.updateTargetList()
        autoTarget.saveConfiguration()
        modules.game_textmessage.displayGameMessage('Alvo removido: ' .. targetName)
    end
```

#### Funcionalidade 3
```lua
end

function autoTarget.updateTargetList()
    autoTarget.targetList:destroyChildren()
    
    for name, target in pairs(autoTarget.targets) do
        local item = g_ui.createWidget('UILabel', autoTarget.targetList)
        item:setText(string.format("%s (Prioridade: %d)", name, target.priority))
        item.targetName = name
        
        item.onDoubleClick = function()
            autoTarget.editTarget(name)
        end
    end
end

function autoTarget.findBestTarget()
    if not autoTarget.enabled then return nil end
    
    local localPlayer = g_game.getLocalPlayer()
    if not localPlayer then return nil end
    
    local spectators = g_map.getSpectators(localPlayer:getPosition(), false, 7, 7)
    local validTargets = {}
    
    for _, creature in ipairs(spectators) do
        if creature:isMonster() and not creature:isDead() then
            local name = creature:getName()
            local target = autoTarget.targets[name]
            
            if target then
                local healthPercent = creature:getHealthPercent()
                if healthPercent >= target.minHealth and healthPercent <= target.maxHealth then
                    table.insert(validTargets, {
                        creature = creature,
                        priority = target.priority,
                        distance = creature:getDistanceFromLocalPlayer()
                    })
```

#### Funcionalidade 4
```lua
                end
            end
        end
    end
    
    if #validTargets == 0 then return nil end
    
    -- Ordenar por prioridade (maior primeiro) e depois por distância (menor primeiro)
    table.sort(validTargets, function(a, b)
        if a.priority ~= b.priority then
            return a.priority > b.priority
        end
        return a.distance < b.distance
    end)
    
    return validTargets[1].creature
end

function autoTarget.onAttackingCreatureChange(creature, oldCreature)
    if not creature and autoTarget.enabled then
        -- Se parou de atacar, procurar novo alvo
        scheduleEvent(function()
            local newTarget = autoTarget.findBestTarget()
            if newTarget then
                g_game.attack(newTarget)
                autoTarget.currentTarget = newTarget
            end
```

#### Funcionalidade 5
```lua
        end, 100)
    end
end

function autoTarget.onCreatureAppear(creature)
    if autoTarget.enabled and creature:isMonster() then
        local attacking = g_game.getAttackingCreature()
        if not attacking then
            local target = autoTarget.findBestTarget()
            if target then
                g_game.attack(target)
                autoTarget.currentTarget = target
            end
        end
    end
end

function autoTarget.onCreatureDisappear(creature)
    if autoTarget.currentTarget == creature then
        autoTarget.currentTarget = nil
    end
```

#### Funcionalidade 6
```lua
end

function autoTarget.onCreatureHealthChange(creature, healthPercent)
    if creature == autoTarget.currentTarget and healthPercent <= 0 then
        -- Alvo morreu, procurar novo
        scheduleEvent(function()
            local newTarget = autoTarget.findBestTarget()
            if newTarget then
                g_game.attack(newTarget)
                autoTarget.currentTarget = newTarget
            end
        end, 500)
    end
end

function autoTarget.loadConfiguration()
    local config = g_settings.getNode('autoTarget') or {}
    autoTarget.enabled = config.enabled or false
    autoTarget.targets = config.targets or {}
    
    autoTarget.enabledBox:setChecked(autoTarget.enabled)
    autoTarget.updateTargetList()
end
```

#### Finalização
```lua

function autoTarget.saveConfiguration()
    g_settings.setNode('autoTarget', {
        enabled = autoTarget.enabled,
        targets = autoTarget.targets
    })
    g_settings.save()
end
```

### Exemplo 3: Creature Info Tracker 🎮

#### Inicialização e Configuração
```lua
-- modules/creature_tracker/creature_tracker.lua
creatureTracker = {}

function creatureTracker.init()
    creatureTracker.creatures = {}
    creatureTracker.window = g_ui.displayUI('creature_tracker')
    creatureTracker.setupInterface()
    
    connect(Creature, {
        onAppear = creatureTracker.onCreatureAppear,
        onDisappear = creatureTracker.onCreatureDisappear,
        onHealthPercentChange = creatureTracker.onHealthChange,
        onPositionChange = creatureTracker.onPositionChange,
        onOutfitChange = creatureTracker.onOutfitChange
    })
end

function creatureTracker.onCreatureAppear(creature)
    if creature:isLocalPlayer() then return end
    
    local id = creature:getId()
    local info = {
        id = id,
        name = creature:getName(),
        type = creature:isPlayer() and 'Player' or 
               creature:isNpc() and 'NPC' or 'Monster',
        level = creature:getLevel() or 0,
        health = creature:getHealthPercent(),
        position = creature:getPosition(),
        firstSeen = os.time(),
        lastSeen = os.time(),
        outfit = creature:getOutfit()
    }
```

#### Funcionalidade 1
```lua
    
    creatureTracker.creatures[id] = info
    creatureTracker.logEvent(creature, 'appeared')
    creatureTracker.updateDisplay()
end

function creatureTracker.onCreatureDisappear(creature)
    local id = creature:getId()
    local info = creatureTracker.creatures[id]
    
    if info then
        info.lastSeen = os.time()
        creatureTracker.logEvent(creature, 'disappeared')
        -- Não remove da lista para manter histórico
    end
    
    creatureTracker.updateDisplay()
end

function creatureTracker.onHealthChange(creature, healthPercent)
    local id = creature:getId()
    local info = creatureTracker.creatures[id]
    
    if info then
        local oldHealth = info.health
        info.health = healthPercent
        info.lastSeen = os.time()
        
        if healthPercent <= 0 then
            creatureTracker.logEvent(creature, 'died')
        elseif oldHealth > healthPercent then
            creatureTracker.logEvent(creature, 'damaged', {
                from = oldHealth,
                to = healthPercent
            })
```

#### Funcionalidade 2
```lua
        elseif oldHealth < healthPercent then
            creatureTracker.logEvent(creature, 'healed', {
                from = oldHealth,
                to = healthPercent
            })
        end
    end
end

function creatureTracker.onPositionChange(creature, newPos, oldPos)
    local id = creature:getId()
    local info = creatureTracker.creatures[id]
    
    if info then
        info.position = newPos
        info.lastSeen = os.time()
        
        local distance = math.max(
            math.abs(newPos.x - oldPos.x),
            math.abs(newPos.y - oldPos.y),
            math.abs(newPos.z - oldPos.z)
        )
        
        if distance > 1 then
            creatureTracker.logEvent(creature, 'teleported', {
                from = oldPos,
                to = newPos
            })
```

#### Funcionalidade 3
```lua
        else
            creatureTracker.logEvent(creature, 'moved', {
                from = oldPos,
                to = newPos
            })
        end
    end
end

function creatureTracker.onOutfitChange(creature, outfit, oldOutfit)
    local id = creature:getId()
    local info = creatureTracker.creatures[id]
    
    if info then
        info.outfit = outfit
        info.lastSeen = os.time()
        creatureTracker.logEvent(creature, 'outfit_changed', {
            from = oldOutfit,
            to = outfit
        })
    end
```

#### Funcionalidade 4
```lua
end

function creatureTracker.logEvent(creature, eventType, data)
    local logEntry = {
        timestamp = os.time(),
        creatureId = creature:getId(),
        creatureName = creature:getName(),
        eventType = eventType,
        data = data or {}
    }
    
    print(string.format("[%s] %s (%d): %s", 
                       os.date('%H:%M:%S'),
                       creature:getName(),
                       creature:getId(),
                       eventType))
    
    -- Salvar no log file se necessário
    creatureTracker.saveToLog(logEntry)
end

function creatureTracker.updateDisplay()
```

#### Funcionalidade 5
```lua
    local list = creatureTracker.window:getChildById('creatureList')
    list:destroyChildren()
    
    local sorted = {}
    for _, info in pairs(creatureTracker.creatures) do
        table.insert(sorted, info)
    end
    
    table.sort(sorted, function(a, b)
        return a.lastSeen > b.lastSeen
    end)
    
    for _, info in ipairs(sorted) do
        local item = g_ui.createWidget('UILabel', list)
        local timeSince = os.time() - info.lastSeen
        local status = timeSince < 5 and 'Online' or string.format('Offline %ds', timeSince)
        
        item:setText(string.format("%s (Lv.%d) - %s - %d%% HP - %s",
                                   info.name,
                                   info.level,
                                   info.type,
                                   info.health,
                                   status))
        
        if timeSince < 5 then
            item:setColor('#00FF00')
        else
            item:setColor('#808080')
        end
```

#### Finalização
```lua
    end
end

function creatureTracker.saveToLog(entry)
    local logFile = g_resources.getWorkDir() .. 'creature_log.txt'
    local line = string.format("[%s] %s\n", 
                               os.date('%Y-%m-%d %H:%M:%S', entry.timestamp),
                               entry.eventType)
    
    -- Implementar salvamento em arquivo se necessário
end
```

---

Esta documentação cobre completamente o sistema de criaturas do OTClient, fornecendo exemplos práticos e detalhados para trabalhar com jogadores, NPCs, monstros e o sistema de combate. Use estes exemplos como base para criar sistemas avançados de gerenciamento de criaturas em seus módulos.

---

> [!success] Navegação
> - [[Getting_Started_Guide]] - Comece aqui
> - [[Module_System_Guide]] - Desenvolvimento de módulos
> - [[UI_System_Guide]] - Interface do usuário
> - [[Lua_API_Reference]] - Referência completa da API

