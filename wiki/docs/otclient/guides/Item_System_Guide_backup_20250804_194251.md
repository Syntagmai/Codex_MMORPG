---
title: Itemsystem
tags: [otclient, system, guide, documentation]
status: completed
aliases: [Itemsystem]
---

# Sistema de Itens - OTClient Redemption

Documentação completa do sistema de itens do OTClient, incluindo criação, manipulação, inventário, containers e market.

## 📋 Índice

1. [Visão Geral](#-visão-geral)
2. [Item Base](#-item-base)
3. [Tipos de Itens](#-tipos-de-itens)
4. [Sistema de Inventário](#-sistema-de-inventário)
5. [Sistema de Containers](#-sistema-de-containers)
6. [UIItem Widget](#-uiitem-widget)
7. [Market System](#-market-system)
8. [Drag & Drop](#-drag--drop)
9. [Durabilidade e Cargas](#-durabilidade-e-cargas)
10. [Exemplos Práticos](#-exemplos-práticos)

## 🎯 Visão Geral

O sistema de itens do OTClient gerencia todos os objetos do jogo, desde equipamentos e consumíveis até containers e itens especiais. Cada item possui propriedades específicas como ID, contagem, subtipo e atributos especiais.

### Slots de Inventário

#### Nível Basic
```lua
-- Constantes de slots do inventário
InventorySlotHead = 1      -- Capacete
InventorySlotNeck = 2      -- Amuleto
InventorySlotBack = 3      -- Backpack
InventorySlotBody = 4      -- Armadura
InventorySlotRight = 5     -- Mão direita (escudo/weapon)
InventorySlotLeft = 6      -- Mão esquerda (weapon/escudo)
InventorySlotLeg = 7       -- Calças
InventorySlotFeet = 8      -- Botas
InventorySlotFinger = 9    -- Anel
InventorySlotAmmo = 10     -- Munição/Tools

-- Verificar se é slot válido
function isValidSlot(slot)
    return slot >= InventorySlotHead and slot <= InventorySlotAmmo
end
```

#### Nível Intermediate
```lua
-- Constantes de slots do inventário
InventorySlotHead = 1      -- Capacete
InventorySlotNeck = 2      -- Amuleto
InventorySlotBack = 3      -- Backpack
InventorySlotBody = 4      -- Armadura
InventorySlotRight = 5     -- Mão direita (escudo/weapon)
InventorySlotLeft = 6      -- Mão esquerda (weapon/escudo)
InventorySlotLeg = 7       -- Calças
InventorySlotFeet = 8      -- Botas
InventorySlotFinger = 9    -- Anel
InventorySlotAmmo = 10     -- Munição/Tools

-- Verificar se é slot válido
function isValidSlot(slot)
    return slot >= InventorySlotHead and slot <= InventorySlotAmmo
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
-- Constantes de slots do inventário
InventorySlotHead = 1      -- Capacete
InventorySlotNeck = 2      -- Amuleto
InventorySlotBack = 3      -- Backpack
InventorySlotBody = 4      -- Armadura
InventorySlotRight = 5     -- Mão direita (escudo/weapon)
InventorySlotLeft = 6      -- Mão esquerda (weapon/escudo)
InventorySlotLeg = 7       -- Calças
InventorySlotFeet = 8      -- Botas
InventorySlotFinger = 9    -- Anel
InventorySlotAmmo = 10     -- Munição/Tools

-- Verificar se é slot válido
function isValidSlot(slot)
    return slot >= InventorySlotHead and slot <= InventorySlotAmmo
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

### IDs de Itens Comuns

```lua
-- Moedas
    --  Moedas (traduzido)
local GOLD_COIN = 2160
local PLATINUM_COIN = 2157
local CRYSTAL_COIN = 2159

-- Containers
    --  Containers (traduzido)
local BACKPACK = 1988
local BAG = 1987
local DEPOT_CHEST = 2594

-- Runas
    --  Runas (traduzido)
local UH_RUNE = 2273        -- Ultimate Healing
local IH_RUNE = 2265        -- Intense Healing
local SD_RUNE = 2268        -- Sudden Death

-- Potions
    --  Potions (traduzido)
local HEALTH_POTION = 7618
local MANA_POTION = 7620
local STRONG_HEALTH = 7588
local STRONG_MANA = 7589
local GREAT_HEALTH = 7591
local GREAT_MANA = 7590
local ULTIMATE_HEALTH = 8473
local GREAT_SPIRIT = 8472

-- Foods
    --  Foods (traduzido)
local BREAD = 2689
local CHEESE = 2696
local HAM = 2671
local MEAT = 2666
```

## 🧬 Item Base

### Criação e Propriedades Básicas

#### Nível Basic
```lua
-- Criar item
local item = Item.create(2160)         -- Gold coin
local item2 = Item.create(2160, 100)   -- 100 gold coins

-- Propriedades básicas
local id = item:getId()                 -- ID do item (2160)
local count = item:getCount()           -- Quantidade
local subType = item:getSubType()       -- Subtipo
local description = item:getDescription() -- Descrição

-- Definir propriedades
item:setCount(50)                       -- Define quantidade
item:setSubType(5)                      -- Define subtipo

-- Posição e localização
local pos = item:getPosition()          -- Posição no mapa
local tile = item:getTile()             -- Tile onde está
local container = item:getContainer()   -- Container onde está
local containerSlot = item:getContainerSlot() -- Slot no container

-- Verificações de estado
local exists = item:isValid()           -- Item existe/é válido
local nil_item = item:isNull()          -- É item nulo
```

#### Nível Intermediate
```lua
-- Criar item
local item = Item.create(2160)         -- Gold coin
local item2 = Item.create(2160, 100)   -- 100 gold coins

-- Propriedades básicas
local id = item:getId()                 -- ID do item (2160)
local count = item:getCount()           -- Quantidade
local subType = item:getSubType()       -- Subtipo
local description = item:getDescription() -- Descrição

-- Definir propriedades
item:setCount(50)                       -- Define quantidade
item:setSubType(5)                      -- Define subtipo

-- Posição e localização
local pos = item:getPosition()          -- Posição no mapa
local tile = item:getTile()             -- Tile onde está
local container = item:getContainer()   -- Container onde está
local containerSlot = item:getContainerSlot() -- Slot no container

-- Verificações de estado
local exists = item:isValid()           -- Item existe/é válido
local nil_item = item:isNull()          -- É item nulo
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
-- Criar item
local item = Item.create(2160)         -- Gold coin
local item2 = Item.create(2160, 100)   -- 100 gold coins

-- Propriedades básicas
local id = item:getId()                 -- ID do item (2160)
local count = item:getCount()           -- Quantidade
local subType = item:getSubType()       -- Subtipo
local description = item:getDescription() -- Descrição

-- Definir propriedades
item:setCount(50)                       -- Define quantidade
item:setSubType(5)                      -- Define subtipo

-- Posição e localização
local pos = item:getPosition()          -- Posição no mapa
local tile = item:getTile()             -- Tile onde está
local container = item:getContainer()   -- Container onde está
local containerSlot = item:getContainerSlot() -- Slot no container

-- Verificações de estado
local exists = item:isValid()           -- Item existe/é válido
local nil_item = item:isNull()          -- É item nulo
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

### Propriedades Avançadas

#### Nível Basic
```lua
-- Características físicas
local stackable = item:isStackable()    -- É empilhável
local moveable = item:isMoveable()      -- É movível
local pickupable = item:isPickupable()  -- Pode ser pego
local rotatable = item:isRotatable()    -- Pode ser rotacionado
local hangable = item:isHangable()      -- Pode ser pendurado
-- Interação
local readable = item:isReadable()      -- Pode ser lido
local writable = item:isWritable()      -- Pode ser escrito
local useable = item:isUseable()        -- Pode ser usado
local multiUse = item:isMultiUse()      -- Uso múltiplo (ex: rope)
-- Características especiais
local blocking = item:isBlocking()      -- Bloqueia passagem
local blockProjectile = item:isBlockProjectile() -- Bloqueia projéteis
local notWalkable = item:isNotWalkable() -- Não é caminhável
local notMoveable = item:isNotMoveable() -- Não é movível
-- Propriedades do tile
local ground = item:isGround()          -- É chão
local topOrder = item:getTopOrder()     -- Ordem de renderização
```

#### Nível Intermediate
```lua
-- Características físicas
local stackable = item:isStackable()    -- É empilhável
local moveable = item:isMoveable()      -- É movível
local pickupable = item:isPickupable()  -- Pode ser pego
local rotatable = item:isRotatable()    -- Pode ser rotacionado
local hangable = item:isHangable()      -- Pode ser pendurado

-- Interação
local readable = item:isReadable()      -- Pode ser lido
local writable = item:isWritable()      -- Pode ser escrito
local useable = item:isUseable()        -- Pode ser usado
local multiUse = item:isMultiUse()      -- Uso múltiplo (ex: rope)

-- Características especiais
local blocking = item:isBlocking()      -- Bloqueia passagem
local blockProjectile = item:isBlockProjectile() -- Bloqueia projéteis
local notWalkable = item:isNotWalkable() -- Não é caminhável
local notMoveable = item:isNotMoveable() -- Não é movível

-- Propriedades do tile
local ground = item:isGround()          -- É chão
local topOrder = item:getTopOrder()     -- Ordem de renderização
```

#### Nível Advanced
```lua
-- Características físicas
local stackable = item:isStackable()    -- É empilhável
local moveable = item:isMoveable()      -- É movível
local pickupable = item:isPickupable()  -- Pode ser pego
local rotatable = item:isRotatable()    -- Pode ser rotacionado
local hangable = item:isHangable()      -- Pode ser pendurado

-- Interação
local readable = item:isReadable()      -- Pode ser lido
local writable = item:isWritable()      -- Pode ser escrito
local useable = item:isUseable()        -- Pode ser usado
local multiUse = item:isMultiUse()      -- Uso múltiplo (ex: rope)

-- Características especiais
local blocking = item:isBlocking()      -- Bloqueia passagem
local blockProjectile = item:isBlockProjectile() -- Bloqueia projéteis
local notWalkable = item:isNotWalkable() -- Não é caminhável
local notMoveable = item:isNotMoveable() -- Não é movível

-- Propriedades do tile
local ground = item:isGround()          -- É chão
local topOrder = item:getTopOrder()     -- Ordem de renderização
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

## 🎲 Tipos de Itens

### Equipamentos

#### Nível Basic
```lua
-- Verificar tipo de equipamento
local weapon = item:isWeapon()          -- É arma
local armor = item:isArmor()            -- É armadura
local ammo = item:isAmmo()              -- É munição
local shield = item:isShield()          -- É escudo
-- Informações de arma
if item:isWeapon() then
    local weaponType = item:getWeaponType() -- Tipo da arma
    local attackValue = item:getAttackValue() -- Valor de ataque
    local defenseValue = item:getDefenseValue() -- Valor de defesa
    local range = item:getRange()         -- Alcance
    local skillType = item:getSkillType() -- Skill necessária
end
-- Informações de armadura
if item:isArmor() then
    local armorValue = item:getArmorValue() -- Valor de armadura
    local weight = item:getWeight()       -- Peso
end
```

#### Nível Intermediate
```lua
-- Verificar tipo de equipamento
local weapon = item:isWeapon()          -- É arma
local armor = item:isArmor()            -- É armadura
local ammo = item:isAmmo()              -- É munição
local shield = item:isShield()          -- É escudo

-- Informações de arma
if item:isWeapon() then
    local weaponType = item:getWeaponType() -- Tipo da arma
    local attackValue = item:getAttackValue() -- Valor de ataque
    local defenseValue = item:getDefenseValue() -- Valor de defesa
    local range = item:getRange()         -- Alcance
    local skillType = item:getSkillType() -- Skill necessária
end

-- Informações de armadura
if item:isArmor() then
    local armorValue = item:getArmorValue() -- Valor de armadura
    local weight = item:getWeight()       -- Peso
end
```

#### Nível Advanced
```lua
-- Verificar tipo de equipamento
local weapon = item:isWeapon()          -- É arma
local armor = item:isArmor()            -- É armadura
local ammo = item:isAmmo()              -- É munição
local shield = item:isShield()          -- É escudo

-- Informações de arma
if item:isWeapon() then
    local weaponType = item:getWeaponType() -- Tipo da arma
    local attackValue = item:getAttackValue() -- Valor de ataque
    local defenseValue = item:getDefenseValue() -- Valor de defesa
    local range = item:getRange()         -- Alcance
    local skillType = item:getSkillType() -- Skill necessária
end

-- Informações de armadura
if item:isArmor() then
    local armorValue = item:getArmorValue() -- Valor de armadura
    local weight = item:getWeight()       -- Peso
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

### Containers

#### Nível Basic
```lua
-- Verificar se é container
if item:isContainer() then
    local capacity = item:getCapacity()  -- Capacidade máxima
    local size = item:getSize()          -- Itens dentro
    local hasParent = item:hasParent()   -- Tem container pai
    
    -- Obter itens dentro
    local items = item:getItems()        -- Lista de itens
    local itemAt = item:getItem(slot)    -- Item no slot específico
    
    -- Verificações
    local empty = item:isEmpty()         -- Está vazio
    local full = item:isFull()           -- Está cheio
end
```

#### Nível Intermediate
```lua
-- Verificar se é container
if item:isContainer() then
    local capacity = item:getCapacity()  -- Capacidade máxima
    local size = item:getSize()          -- Itens dentro
    local hasParent = item:hasParent()   -- Tem container pai
    
    -- Obter itens dentro
    local items = item:getItems()        -- Lista de itens
    local itemAt = item:getItem(slot)    -- Item no slot específico
    
    -- Verificações
    local empty = item:isEmpty()         -- Está vazio
    local full = item:isFull()           -- Está cheio
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
-- Verificar se é container
if item:isContainer() then
    local capacity = item:getCapacity()  -- Capacidade máxima
    local size = item:getSize()          -- Itens dentro
    local hasParent = item:hasParent()   -- Tem container pai
    
    -- Obter itens dentro
    local items = item:getItems()        -- Lista de itens
    local itemAt = item:getItem(slot)    -- Item no slot específico
    
    -- Verificações
    local empty = item:isEmpty()         -- Está vazio
    local full = item:isFull()           -- Está cheio
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

### Fluidos

```lua
-- Containers de fluido
    --  Containers de fluido (traduzido)
if item:isFluidContainer() then
    -- Verificação condicional
    local fluidType = item:getFluidType() -- Tipo do fluido
    item:setFluidType(FluidType.Water)   -- Define tipo do fluido
    
    -- Tipos de fluido comuns
    --  Tipos de fluido comuns (traduzido)
    -- FluidType.None, FluidType.Water, FluidType.Wine, 
    --  FluidType.None, FluidType.Water, FluidType.Wine, (traduzido)
    -- FluidType.Beer, FluidType.Mud, FluidType.Blood, etc.
    --  FluidType.Beer, FluidType.Mud, FluidType.Blood, etc. (traduzido)
end

-- Splash items (poções, etc.)
if item:isSplash() then
    -- Verificação condicional
    local splashType = item:getSplashType()
end
```

### Runes e Consumíveis

#### Nível Basic
```lua
-- Runes
if item:isRune() then
    local charges = item:getCharges()    -- Cargas restantes
    local maxCharges = item:getMaxCharges() -- Cargas máximas
    local runeSpell = item:getRuneSpell() -- Spell da runa
end

-- Itens com cargas
if item:isCharged() then
    local charges = item:getCharges()
    item:setCharges(5)                   -- Define cargas
end

-- Consumíveis (food, potions)
if item:isConsumable() then
    local nutrition = item:getNutrition() -- Valor nutricional (food)
    local regeneration = item:getRegeneration() -- Regeneração
end
```

#### Nível Intermediate
```lua
-- Runes
if item:isRune() then
    local charges = item:getCharges()    -- Cargas restantes
    local maxCharges = item:getMaxCharges() -- Cargas máximas
    local runeSpell = item:getRuneSpell() -- Spell da runa
end

-- Itens com cargas
if item:isCharged() then
    local charges = item:getCharges()
    item:setCharges(5)                   -- Define cargas
end

-- Consumíveis (food, potions)
if item:isConsumable() then
    local nutrition = item:getNutrition() -- Valor nutricional (food)
    local regeneration = item:getRegeneration() -- Regeneração
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
-- Runes
if item:isRune() then
    local charges = item:getCharges()    -- Cargas restantes
    local maxCharges = item:getMaxCharges() -- Cargas máximas
    local runeSpell = item:getRuneSpell() -- Spell da runa
end

-- Itens com cargas
if item:isCharged() then
    local charges = item:getCharges()
    item:setCharges(5)                   -- Define cargas
end

-- Consumíveis (food, potions)
if item:isConsumable() then
    local nutrition = item:getNutrition() -- Valor nutricional (food)
    local regeneration = item:getRegeneration() -- Regeneração
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

### Itens com Texto

```lua
-- Itens que podem ter texto (books, signs, etc.)
    --  Itens que podem ter texto (books, signs, etc.) (traduzido)
if item:isReadable() or item:isWritable() then
    -- Verificação condicional
    local text = item:getText()          -- Texto atual
    item:setText("Novo texto")           -- Define texto (se writeable)
    
    local maxLength = item:getMaxTextLength() -- Tamanho máximo
end

-- Writable items (pergaminhos, livros)
    --  Writable items (pergaminhos, livros) (traduzido)
if item:isWritable() then
    -- Verificação condicional
    local writer = item:getWriter()      -- Quem escreveu
    local date = item:getDate()          -- Data de escrita
end
```

## 🎒 Sistema de Inventário

### Gerenciamento de Slots

#### Nível Basic
```lua
-- Obter itens do inventário
local player = g_game.getLocalPlayer()
if player then
    -- Item em slot específico
    local helmet = player:getInventoryItem(InventorySlotHead)
    local backpack = player:getInventoryItem(InventorySlotBack)
    local weapon = player:getInventoryItem(InventorySlotRight)
    
    -- Todos os itens do inventário
    local allItems = player:getInventoryItems()
    
    -- Verificar se slot está vazio
    if not helmet then
        print("Não está usando capacete")
    end
    
    -- Procurar item específico
    local goldCoin = g_game.findPlayerItem(2160, -1) -- -1 = qualquer quantidade
    if goldCoin then
        print("Encontrou gold coin:", goldCoin:getCount())
    end
end
```

#### Nível Intermediate
```lua
-- Obter itens do inventário
local player = g_game.getLocalPlayer()
if player then
    -- Item em slot específico
    local helmet = player:getInventoryItem(InventorySlotHead)
    local backpack = player:getInventoryItem(InventorySlotBack)
    local weapon = player:getInventoryItem(InventorySlotRight)
    
    -- Todos os itens do inventário
    local allItems = player:getInventoryItems()
    
    -- Verificar se slot está vazio
    if not helmet then
        print("Não está usando capacete")
    end
    
    -- Procurar item específico
    local goldCoin = g_game.findPlayerItem(2160, -1) -- -1 = qualquer quantidade
    if goldCoin then
        print("Encontrou gold coin:", goldCoin:getCount())
    end
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
-- Obter itens do inventário
local player = g_game.getLocalPlayer()
if player then
    -- Item em slot específico
    local helmet = player:getInventoryItem(InventorySlotHead)
    local backpack = player:getInventoryItem(InventorySlotBack)
    local weapon = player:getInventoryItem(InventorySlotRight)
    
    -- Todos os itens do inventário
    local allItems = player:getInventoryItems()
    
    -- Verificar se slot está vazio
    if not helmet then
        print("Não está usando capacete")
    end
    
    -- Procurar item específico
    local goldCoin = g_game.findPlayerItem(2160, -1) -- -1 = qualquer quantidade
    if goldCoin then
        print("Encontrou gold coin:", goldCoin:getCount())
    end
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

### Uso de Itens do Inventário

```lua
-- Usar item por ID
    --  Usar item por ID (traduzido)
g_game.useInventoryItem(2160)           -- Usar gold coin

-- Usar item com alvo
    --  Usar item com alvo (traduzido)
g_game.useInventoryItemWith(2160, creature) -- Usar item em criatura
g_game.useInventoryItemWith(2160, tile)     -- Usar item em tile

-- Usar item do slot
    --  Usar item do slot (traduzido)
local item = player:getInventoryItem(InventorySlotRight)
if item then
    -- Verificação condicional
    g_game.use(item)                    -- Usar item
    g_game.useWith(item, target)        -- Usar item em alvo
end
```

### Cálculos de Inventário

#### Inicialização e Configuração
```lua
-- Peso e capacidade
local capacity = player:getCapacity()    -- Capacidade total
local freeCapacity = player:getFreeCapacity() -- Capacidade livre

-- Calcular peso de um item
function getItemWeight(item)
    local weight = item:getWeight()
    local count = item:getCount()
    return weight * count / 100  -- Weight em centenas de gramas
end

-- Verificar se pode carregar item
function canCarryItem(item)
    local itemWeight = getItemWeight(item)
    return player:getFreeCapacity() >= itemWeight
end

-- Contar itens específicos no inventário
function countItemsInInventory(itemId)
    local total = 0
    local allItems = player:getInventoryItems()
    
    for _, item in ipairs(allItems) do
        if item:getId() == itemId then
            total = total + item:getCount()
        end
```

#### Funcionalidade 1
```lua
        
        -- Verificar dentro de containers também
        if item:isContainer() then
            total = total + countItemsInContainer(item, itemId)
        end
    end
    
    return total
end

function countItemsInContainer(container, itemId)
    local total = 0
    local items = container:getItems()
    
    for _, item in ipairs(items) do
        if item:getId() == itemId then
            total = total + item:getCount()
        end
        
        if item:isContainer() then
            total = total + countItemsInContainer(item, itemId)
        end
```

#### Finalização
```lua
    end
    
    return total
end
```

## 📦 Sistema de Containers

### Gerenciamento de Containers

#### Nível Basic
```lua
-- Abrir container
-- Informações do container
local name = container:getName()         -- Nome do container
local capacity = container:getCapacity() -- Capacidade
local size = container:getSize()         -- Itens dentro
local items = container:getItems()       -- Lista de itens
local empty = container:isEmpty()        -- Está vazio
local full = container:isFull()         -- Está cheio
-- Hierarquia de containers
local hasParent = container:hasParent()  -- Tem container pai
local parent = container:getParentContainer() -- Container pai
local isChild = container:isChild()      -- É container filho
-- Obter item em slot específico
local item = container:getItem(slot)     -- Item no slot (0-based)
local firstItem = container:getItem(0)   -- Primeiro item
```

#### Nível Intermediate
```lua
-- Abrir container
g_game.open(item, container)            -- Abre item como container
g_game.openParent(container)            -- Abre container pai
g_game.close(container)                 -- Fecha container

-- Informações do container
local name = container:getName()         -- Nome do container
local capacity = container:getCapacity() -- Capacidade
local size = container:getSize()         -- Itens dentro
local items = container:getItems()       -- Lista de itens
local empty = container:isEmpty()        -- Está vazio
local full = container:isFull()         -- Está cheio

-- Hierarquia de containers
local hasParent = container:hasParent()  -- Tem container pai
local parent = container:getParentContainer() -- Container pai
local isChild = container:isChild()      -- É container filho

-- Obter item em slot específico
local item = container:getItem(slot)     -- Item no slot (0-based)
local firstItem = container:getItem(0)   -- Primeiro item
```

#### Nível Advanced
```lua
-- Abrir container
g_game.open(item, container)            -- Abre item como container
g_game.openParent(container)            -- Abre container pai
g_game.close(container)                 -- Fecha container

-- Informações do container
local name = container:getName()         -- Nome do container
local capacity = container:getCapacity() -- Capacidade
local size = container:getSize()         -- Itens dentro
local items = container:getItems()       -- Lista de itens
local empty = container:isEmpty()        -- Está vazio
local full = container:isFull()         -- Está cheio

-- Hierarquia de containers
local hasParent = container:hasParent()  -- Tem container pai
local parent = container:getParentContainer() -- Container pai
local isChild = container:isChild()      -- É container filho

-- Obter item em slot específico
local item = container:getItem(slot)     -- Item no slot (0-based)
local firstItem = container:getItem(0)   -- Primeiro item
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

### Manipulação de Itens em Containers

```lua
-- Mover item para container
    --  Mover item para container (traduzido)
g_game.move(item, containerPosition, count)

-- Posição em container
local containerPos = {
    x = 0xFFFF,           -- Container ID
    y = containerId,      -- ID do container
    z = slot             -- Slot no container
}

-- Exemplo: mover 50 gold coins para slot 0 do container ID 100
    --  Exemplo: mover 50 gold coins para slot 0 do container ID 100 (traduzido)
g_game.move(goldCoin, {x = 0xFFFF, y = 100, z = 0}, 50)

-- Usar item do container
    --  Usar item do container (traduzido)
local containerItem = container:getItem(0)
if containerItem then
    -- Verificação condicional
    g_game.use(containerItem)
    g_game.useWith(containerItem, target)
end
```

### Busca em Containers

#### Inicialização e Configuração
```lua
-- Procurar item em todos os containers
function findItemInContainers(itemId, minCount)
    minCount = minCount or 1
    local player = g_game.getLocalPlayer()
    if not player then return nil end
    
    -- Verificar inventário primeiro
    local item = g_game.findPlayerItem(itemId, minCount)
    if item then return item end
    
    -- Buscar em todos os containers abertos
    for _, container in pairs(g_game.getContainers()) do
        local found = findItemInContainer(container, itemId, minCount)
        if found then return found end
    end
    
    return nil
end

function findItemInContainer(container, itemId, minCount)
    local items = container:getItems()
    
    for _, item in ipairs(items) do
        if item:getId() == itemId and item:getCount() >= minCount then
            return item
        end
```

#### Funcionalidade 1
```lua
        
        -- Busca recursiva em sub-containers
        if item:isContainer() then
            local found = findItemInContainer(item, itemId, minCount)
            if found then return found end
        end
    end
    
    return nil
end

-- Listar todos os itens em containers
function listAllContainerItems()
    local allItems = {}
    
    for _, container in pairs(g_game.getContainers()) do
        local containerItems = listContainerItems(container)
        for _, item in ipairs(containerItems) do
            table.insert(allItems, item)
        end
    end
```

#### Funcionalidade 2
```lua
    
    return allItems
end

function listContainerItems(container)
    local items = {}
    local containerItems = container:getItems()
    
    for _, item in ipairs(containerItems) do
        table.insert(items, {
            item = item,
            container = container,
            path = getContainerPath(container)
        })
        
        if item:isContainer() then
            local subItems = listContainerItems(item)
            for _, subItem in ipairs(subItems) do
                table.insert(items, subItem)
            end
        end
```

#### Finalização
```lua
    end
    
    return items
end
```

## 🎨 UIItem Widget

### Criação e Configuração

#### Nível Basic
```lua
-- Criar UIItem widget
local itemWidget = g_ui.createWidget('UIItem', parent)
-- Configurar item
-- Obter informações
local item = itemWidget:getItem()       -- Objeto Item
local itemId = itemWidget:getItemId()   -- ID do item
local count = itemWidget:getItemCount() -- Quantidade
local subType = itemWidget:getItemSubType() -- Subtipo
-- Estados especiais
local virtual = itemWidget:isVirtual()  -- Verifica se virtual
-- Posição (para itens no mapa)
local pos = itemWidget:getPosition()    -- Obtém posição
```

#### Nível Intermediate
```lua
-- Criar UIItem widget
local itemWidget = g_ui.createWidget('UIItem', parent)

-- Configurar item
itemWidget:setItemId(2160)              -- ID do item
itemWidget:setItemCount(100)            -- Quantidade
itemWidget:setItemSubType(5)            -- Subtipo
itemWidget:setItem(item)                -- Objeto Item completo

-- Obter informações
local item = itemWidget:getItem()       -- Objeto Item
local itemId = itemWidget:getItemId()   -- ID do item
local count = itemWidget:getItemCount() -- Quantidade
local subType = itemWidget:getItemSubType() -- Subtipo

-- Estados especiais
itemWidget:setVirtual(true)             -- Item virtual (não real)
local virtual = itemWidget:isVirtual()  -- Verifica se virtual

-- Posição (para itens no mapa)
itemWidget:setPosition(position)        -- Define posição
local pos = itemWidget:getPosition()    -- Obtém posição
```

#### Nível Advanced
```lua
-- Criar UIItem widget
local itemWidget = g_ui.createWidget('UIItem', parent)

-- Configurar item
itemWidget:setItemId(2160)              -- ID do item
itemWidget:setItemCount(100)            -- Quantidade
itemWidget:setItemSubType(5)            -- Subtipo
itemWidget:setItem(item)                -- Objeto Item completo

-- Obter informações
local item = itemWidget:getItem()       -- Objeto Item
local itemId = itemWidget:getItemId()   -- ID do item
local count = itemWidget:getItemCount() -- Quantidade
local subType = itemWidget:getItemSubType() -- Subtipo

-- Estados especiais
itemWidget:setVirtual(true)             -- Item virtual (não real)
local virtual = itemWidget:isVirtual()  -- Verifica se virtual

-- Posição (para itens no mapa)
itemWidget:setPosition(position)        -- Define posição
local pos = itemWidget:getPosition()    -- Obtém posição
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

### Eventos de UIItem

```lua
-- Eventos de interação
itemWidget.onClick = function(widget)
    local item = widget:getItem()
    if item then
    -- Verificação condicional
        print("Clicou no item:", item:getId())
    end
end

itemWidget.onDoubleClick = function(widget)
    local item = widget:getItem()
    if item then
    -- Verificação condicional
        g_game.use(item)  -- Usar item no duplo clique
    end
end

itemWidget.onMousePress = function(widget, mousePos, button)
    if button == MouseRightButton then
    -- Verificação condicional
        local item = widget:getItem()
        if item then
    -- Verificação condicional
            g_game.look(item)  -- Examinar item
        end
    end
end

-- Eventos de drag & drop
    --  Eventos de drag & drop (traduzido)
itemWidget.onDragEnter = function(widget, mousePos)
    widget:setBorderWidth(1)
    widget:setBorderColor('#FFFF00')
    return true
end

itemWidget.onDragLeave = function(widget, droppedWidget, mousePos)
    widget:setBorderWidth(0)
    return true
end

itemWidget.onDrop = function(widget, droppedWidget, mousePos)
    local draggedItem = droppedWidget:getItem()
    local targetItem = widget:getItem()
    
    if draggedItem and targetItem then
    -- Verificação condicional
        -- Lógica de drop customizada
        print("Dropou", draggedItem:getId(), "em", targetItem:getId())
    end
    
    widget:setBorderWidth(0)
    return true
end
```

## 💰 Market System

### Market Data

#### Nível Basic
```lua
-- Obter dados de market
local marketData = item:getMarketData()
if marketData then
    local category = marketData.category     -- Categoria
    local name = marketData.name            -- Nome no market
    local requiredLevel = marketData.requiredLevel -- Level necessário
    local restrictVocation = marketData.restrictVocation -- Vocação restrita
    local showAs = marketData.showAs        -- Como mostrar
    local tradeAs = marketData.tradeAs      -- Como negociar
end
-- Verificações de market
local marketable = item:isMarketable()    -- Pode ser vendido no market
local stackable = item:isStackable()      -- É empilhável no market
```

#### Nível Intermediate
```lua
-- Obter dados de market
local marketData = item:getMarketData()
if marketData then
    local category = marketData.category     -- Categoria
    local name = marketData.name            -- Nome no market
    local requiredLevel = marketData.requiredLevel -- Level necessário
    local restrictVocation = marketData.restrictVocation -- Vocação restrita
    local showAs = marketData.showAs        -- Como mostrar
    local tradeAs = marketData.tradeAs      -- Como negociar
end

-- Verificações de market
local marketable = item:isMarketable()    -- Pode ser vendido no market
local stackable = item:isStackable()      -- É empilhável no market
```

#### Nível Advanced
```lua
-- Obter dados de market
local marketData = item:getMarketData()
if marketData then
    local category = marketData.category     -- Categoria
    local name = marketData.name            -- Nome no market
    local requiredLevel = marketData.requiredLevel -- Level necessário
    local restrictVocation = marketData.restrictVocation -- Vocação restrita
    local showAs = marketData.showAs        -- Como mostrar
    local tradeAs = marketData.tradeAs      -- Como negociar
end

-- Verificações de market
local marketable = item:isMarketable()    -- Pode ser vendido no market
local stackable = item:isStackable()      -- É empilhável no market
```

### Market Operations

#### Nível Basic
```lua
-- Criar oferta de venda
function createSellOffer(itemId, amount, price)
    local protocolGame = g_game.getProtocolGame()
    if protocolGame then
        protocolGame:sendMarketCreateOffer(
            MarketOfferType.Sell,  -- Tipo: venda
            itemId,                -- ID do item
            amount,                -- Quantidade
            price,                 -- Preço por item
            false                  -- Anônimo
        )
    end
end

-- Criar oferta de compra
function createBuyOffer(itemId, amount, price)
    local protocolGame = g_game.getProtocolGame()
    if protocolGame then
        protocolGame:sendMarketCreateOffer(
            MarketOfferType.Buy,   -- Tipo: compra
            itemId,                -- ID do item
            amount,                -- Quantidade
            price,                 -- Preço por item
            false                  -- Anônimo
        )
    end
end

-- Aceitar oferta
function acceptMarketOffer(offerId, amount)
    local protocolGame = g_game.getProtocolGame()
    if protocolGame then
        protocolGame:sendMarketAcceptOffer(offerId, amount)
    end
end

-- Cancelar oferta
function cancelMarketOffer(offerId)
    local protocolGame = g_game.getProtocolGame()
    if protocolGame then
        protocolGame:sendMarketCancelOffer(offerId)
    end
end
```

#### Nível Intermediate
```lua
-- Criar oferta de venda
function createSellOffer(itemId, amount, price)
    local protocolGame = g_game.getProtocolGame()
    if protocolGame then
        protocolGame:sendMarketCreateOffer(
            MarketOfferType.Sell,  -- Tipo: venda
            itemId,                -- ID do item
            amount,                -- Quantidade
            price,                 -- Preço por item
            false                  -- Anônimo
        )
    end
end

-- Criar oferta de compra
function createBuyOffer(itemId, amount, price)
    local protocolGame = g_game.getProtocolGame()
    if protocolGame then
        protocolGame:sendMarketCreateOffer(
            MarketOfferType.Buy,   -- Tipo: compra
            itemId,                -- ID do item
            amount,                -- Quantidade
            price,                 -- Preço por item
            false                  -- Anônimo
        )
    end
end

-- Aceitar oferta
function acceptMarketOffer(offerId, amount)
    local protocolGame = g_game.getProtocolGame()
    if protocolGame then
        protocolGame:sendMarketAcceptOffer(offerId, amount)
    end
end

-- Cancelar oferta
function cancelMarketOffer(offerId)
    local protocolGame = g_game.getProtocolGame()
    if protocolGame then
        protocolGame:sendMarketCancelOffer(offerId)
    end
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
-- Criar oferta de venda
function createSellOffer(itemId, amount, price)
    local protocolGame = g_game.getProtocolGame()
    if protocolGame then
        protocolGame:sendMarketCreateOffer(
            MarketOfferType.Sell,  -- Tipo: venda
            itemId,                -- ID do item
            amount,                -- Quantidade
            price,                 -- Preço por item
            false                  -- Anônimo
        )
    end
end

-- Criar oferta de compra
function createBuyOffer(itemId, amount, price)
    local protocolGame = g_game.getProtocolGame()
    if protocolGame then
        protocolGame:sendMarketCreateOffer(
            MarketOfferType.Buy,   -- Tipo: compra
            itemId,                -- ID do item
            amount,                -- Quantidade
            price,                 -- Preço por item
            false                  -- Anônimo
        )
    end
end

-- Aceitar oferta
function acceptMarketOffer(offerId, amount)
    local protocolGame = g_game.getProtocolGame()
    if protocolGame then
        protocolGame:sendMarketAcceptOffer(offerId, amount)
    end
end

-- Cancelar oferta
function cancelMarketOffer(offerId)
    local protocolGame = g_game.getProtocolGame()
    if protocolGame then
        protocolGame:sendMarketCancelOffer(offerId)
    end
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

## 🔄 Drag & Drop

### Sistema de Drag & Drop

```lua
-- Implementar drag & drop customizado
    --  Implementar drag & drop customizado (traduzido)
function setupItemDragDrop(itemWidget)
    -- Função: setupItemDragDrop
    itemWidget:setDraggable(true)
    
    itemWidget.onDragEnter = function(widget, mousePos)
        if widget:isVirtual() then return false end
    -- Verificação condicional
        
        local item = widget:getItem()
        if not item then return false end
    -- Verificação condicional
        
        widget:setBorderWidth(1)
        widget:setBorderColor('#00FF00')
        widget.currentDragThing = item
        g_mouse.pushCursor('target')
        return true
    end
    
    itemWidget.onDragLeave = function(widget, droppedWidget, mousePos)
        if widget:isVirtual() then return false end
    -- Verificação condicional
        
        widget.currentDragThing = nil
        g_mouse.popCursor('target')
        widget:setBorderWidth(0)
        return true
    end
    
    itemWidget.onDrop = function(widget, droppedWidget, mousePos)
        local draggedItem = droppedWidget.currentDragThing
        if not draggedItem or not draggedItem:isItem() then return false end
    -- Verificação condicional
        
        local toPos = widget:getPosition()
        local fromPos = draggedItem:getPosition()
        
        if fromPos.x == toPos.x and fromPos.y == toPos.y and fromPos.z == toPos.z then
    -- Verificação condicional
            return false
        end
        
        -- Mover item
    --  Mover item (traduzido)
        if draggedItem:getCount() > 1 then
    -- Verificação condicional
            modules.game_interface.moveStackableItem(draggedItem, toPos)
        else
            g_game.move(draggedItem, toPos, 1)
        end
        
        widget:setBorderWidth(0)
        return true
    end
end
```

### Drag & Drop para Containers

```lua
-- Setup para container slots
    --  Setup para container slots (traduzido)
function setupContainerSlot(slotWidget, containerId, slotIndex)
    -- Função: setupContainerSlot
    slotWidget:setAcceptDrops(true)
    
    slotWidget.onDrop = function(widget, droppedWidget, mousePos)
        local draggedItem = droppedWidget:getItem()
        if not draggedItem then return false end
    -- Verificação condicional
        
        local targetPos = {
            x = 0xFFFF,
            y = containerId,
            z = slotIndex
        }
        
        -- Verificar se pode mover para este slot
    --  Verificar se pode mover para este slot (traduzido)
        if draggedItem:getCount() > 1 then
    -- Verificação condicional
            modules.game_interface.moveStackableItem(draggedItem, targetPos)
        else
            g_game.move(draggedItem, targetPos, 1)
        end
        
        return true
    end
end
```

## ⏱️ Durabilidade e Cargas

### Sistema de Durabilidade

#### Inicialização e Configuração
```lua
-- Itens com duração
if item:hasDuration() then
    local duration = item:getDurationTime()  -- Tempo em segundos
    local maxDuration = item:getMaxDuration() -- Duração máxima
    local durationPercent = (duration / maxDuration) * 100
    
    print(string.format("Duração: %d/%d (%d%%)", 
                       duration, maxDuration, durationPercent))
end

-- Formatação de tempo
function formatDuration(seconds)
    local hours = math.floor(seconds / 3600)
    local minutes = math.floor((seconds % 3600) / 60)
    local secs = seconds % 60
    
    if hours > 0 then
        return string.format("%dh%02dm%02ds", hours, minutes, secs)
    elseif minutes > 0 then
        return string.format("%dm%02ds", minutes, secs)
    else
        return string.format("%ds", secs)
    end
```

#### Funcionalidade 1
```lua
end

-- Monitor de duração
function startDurationMonitor()
    local updateEvent
    
    local function updateDurations()
        local player = g_game.getLocalPlayer()
        if not player then return end
        
        -- Verificar itens do inventário
        for slot = InventorySlotHead, InventorySlotAmmo do
            local item = player:getInventoryItem(slot)
            if item and item:hasDuration() then
                local duration = item:getDurationTime()
                if duration > 0 then
                    updateDurationDisplay(slot, duration)
                else
                    removeDurationDisplay(slot)
                end
            end
```

#### Finalização
```lua
        end
        
        updateEvent = scheduleEvent(updateDurations, 1000)
    end
    
    updateEvent = scheduleEvent(updateDurations, 1000)
    return updateEvent
end
```

### Sistema de Cargas

```lua
-- Itens com cargas (runes, tools)
    --  Itens com cargas (runes, tools) (traduzido)
if item:isCharged() then
    -- Verificação condicional
    local charges = item:getCharges()    -- Cargas atuais
    local maxCharges = item:getMaxCharges() -- Cargas máximas
    
    print(string.format("Cargas: %d/%d", charges, maxCharges))
    
    -- Verificar se ainda tem cargas
    --  Verificar se ainda tem cargas (traduzido)
    if charges > 0 then
    -- Verificação condicional
        print("Item ainda utilizável")
    else
        print("Item sem cargas")
    end
end

-- Monitor de cargas para runes
    --  Monitor de cargas para runes (traduzido)
function monitorRuneCharges()
    -- Função: monitorRuneCharges
    local player = g_game.getLocalPlayer()
    if not player then return end
    -- Verificação condicional
    
    local allItems = listAllContainerItems()
    
    for _, itemInfo in ipairs(allItems) do
    -- Loop de repetição
        local item = itemInfo.item
        if item:isRune() and item:isCharged() then
    -- Verificação condicional
            local charges = item:getCharges()
            if charges <= 5 then  -- Aviso quando restam poucas cargas
    -- Verificação condicional
                print(string.format("AVISO: %s com apenas %d cargas!", 
                                   item:getDescription(), charges))
            end
        end
    end
end
```

## 💡 Exemplos Práticos

### Exemplo 1: Sistema de Auto-Loot

#### Inicialização e Configuração
```lua
-- modules/auto_loot/auto_loot.lua
autoLoot = {}

function autoLoot.init()
    autoLoot.enabled = false
    autoLoot.lootList = {}
    autoLoot.window = g_ui.displayUI('auto_loot')
    autoLoot.setupInterface()
    autoLoot.loadConfiguration()
    
    connect(Container, {
        onOpen = autoLoot.onContainerOpen,
        onAddItem = autoLoot.onContainerAddItem,
        onUpdateItem = autoLoot.onContainerUpdateItem
    })
end

function autoLoot.setupInterface()
    autoLoot.enabledBox = autoLoot.window:getChildById('enabledBox')
    autoLoot.itemList = autoLoot.window:getChildById('itemList')
    autoLoot.addButton = autoLoot.window:getChildById('addButton')
    autoLoot.removeButton = autoLoot.window:getChildById('removeButton')
    
    autoLoot.enabledBox.onCheckChange = function(widget, checked)
        autoLoot.enabled = checked
        autoLoot.saveConfiguration()
    end
```

#### Funcionalidade 1
```lua
    
    autoLoot.addButton.onClick = autoLoot.addCurrentItem
    autoLoot.removeButton.onClick = autoLoot.removeSelectedItem
end

function autoLoot.addCurrentItem()
    local mouseGrabber = g_ui.createWidget('UIWidget')
    mouseGrabber:setVisible(false)
    mouseGrabber:setFocusable(false)
    mouseGrabber:grabMouse()
    g_mouse.pushCursor('target')
    
    mouseGrabber.onMouseRelease = function(widget, mousePos, button)
        if button == MouseLeftButton then
            local clickedWidget = modules.game_interface.getRootPanel():recursiveGetChildByPos(mousePos, false)
            if clickedWidget and clickedWidget:getClassName() == 'UIItem' then
                local item = clickedWidget:getItem()
                if item then
                    autoLoot.addItemToList(item:getId(), item:getDescription())
                end
            end
```

#### Funcionalidade 2
```lua
        end
        
        g_mouse.popCursor('target')
        widget:ungrabMouse()
        widget:destroy()
    end
end

function autoLoot.addItemToList(itemId, description)
    if not autoLoot.lootList[itemId] then
        autoLoot.lootList[itemId] = {
            id = itemId,
            description = description,
            priority = 1
        }
        
        autoLoot.updateItemList()
        autoLoot.saveConfiguration()
        modules.game_textmessage.displayGameMessage('Item adicionado ao loot: ' .. description)
    end
end
```

#### Funcionalidade 3
```lua

function autoLoot.updateItemList()
    autoLoot.itemList:destroyChildren()
    
    for itemId, itemData in pairs(autoLoot.lootList) do
        local item = g_ui.createWidget('UILabel', autoLoot.itemList)
        item:setText(itemData.description)
        item.itemId = itemId
        
        item.onDoubleClick = function()
            autoLoot.editItemPriority(itemId)
        end
    end
end

function autoLoot.onContainerOpen(container)
    if not autoLoot.enabled then return end
    
    -- Verificar se é corpo de criatura
    local containerItem = container:getContainerItem()
    if containerItem and containerItem:getId() == 3058 then  -- Dead body
        scheduleEvent(function()
            autoLoot.lootContainer(container)
        end, 500)
```

#### Funcionalidade 4
```lua
    end
end

function autoLoot.lootContainer(container)
    local items = container:getItems()
    local lootedItems = {}
    
    -- Ordenar por prioridade
    for _, item in ipairs(items) do
        local itemId = item:getId()
        local lootData = autoLoot.lootList[itemId]
        
        if lootData then
            table.insert(lootedItems, {
                item = item,
                priority = lootData.priority
            })
        end
    end
    
    table.sort(lootedItems, function(a, b)
        return a.priority > b.priority
    end)
```

#### Funcionalidade 5
```lua
    
    -- Pegar itens
    for _, lootItem in ipairs(lootedItems) do
        local item = lootItem.item
        if item and item:isPickupable() then
            scheduleEvent(function()
                g_game.move(item, {x = 65535, y = SlotType.Inventory, z = 0}, item:getCount())
            end, 200)
        end
    end
end

function autoLoot.loadConfiguration()
    local config = g_settings.getNode('autoLoot') or {}
    autoLoot.enabled = config.enabled or false
    autoLoot.lootList = config.lootList or {}
    
    autoLoot.enabledBox:setChecked(autoLoot.enabled)
    autoLoot.updateItemList()
end

function autoLoot.saveConfiguration()
```

#### Finalização
```lua
    g_settings.setNode('autoLoot', {
        enabled = autoLoot.enabled,
        lootList = autoLoot.lootList
    })
    g_settings.save()
end
```

### Exemplo 2: Item Manager

#### Inicialização e Configuração
```lua
-- modules/item_manager/item_manager.lua
itemManager = {}

function itemManager.init()
    itemManager.window = g_ui.displayUI('item_manager')
    itemManager.setupInterface()
    itemManager.updateItemDatabase()
    
    connect(g_game, {
        onGameStart = itemManager.onGameStart,
        onGameEnd = itemManager.onGameEnd
    })
end

function itemManager.setupInterface()
    itemManager.itemList = itemManager.window:getChildById('itemList')
    itemManager.searchEdit = itemManager.window:getChildById('searchEdit')
    itemManager.categoryCombo = itemManager.window:getChildById('categoryCombo')
    itemManager.detailsPanel = itemManager.window:getChildById('detailsPanel')
    
    -- Configurar categorias
    itemManager.categoryCombo:addOption('Todos', 'all')
    itemManager.categoryCombo:addOption('Armas', 'weapons')
    itemManager.categoryCombo:addOption('Armaduras', 'armor')
    itemManager.categoryCombo:addOption('Escudos', 'shields')
    itemManager.categoryCombo:addOption('Containers', 'containers')
    itemManager.categoryCombo:addOption('Consumíveis', 'consumables')
    
    -- Eventos
    itemManager.searchEdit.onTextChange = itemManager.filterItems
    itemManager.categoryCombo.onOptionChange = itemManager.filterItems
    itemManager.itemList.onChildFocusChange = itemManager.onItemSelect
end
```

#### Funcionalidade 1
```lua

function itemManager.updateItemDatabase()
    itemManager.itemDatabase = {}
    
    -- Scan de itens conhecidos
    for itemId = 100, 10000 do
        local item = Item.create(itemId)
        if item and not item:isNull() then
            local itemInfo = {
                id = itemId,
                description = item:getDescription(),
                category = itemManager.categorizeItem(item),
                weight = item:getWeight(),
                stackable = item:isStackable(),
                moveable = item:isMoveable(),
                useable = item:isUseable(),
                readable = item:isReadable(),
                writable = item:isWritable(),
                container = item:isContainer(),
                weapon = item:isWeapon(),
                armor = item:isArmor(),
                marketable = item:isMarketable()
            }
```

#### Funcionalidade 2
```lua
            
            if item:isContainer() then
                itemInfo.capacity = item:getCapacity()
            end
            
            if item:isWeapon() then
                itemInfo.attack = item:getAttackValue()
                itemInfo.defense = item:getDefenseValue()
                itemInfo.range = item:getRange()
            end
            
            if item:isArmor() then
                itemInfo.armorValue = item:getArmorValue()
            end
            
            itemManager.itemDatabase[itemId] = itemInfo
        end
    end
    
    print("Item database atualizada:", table.size(itemManager.itemDatabase), "itens")
end
```

#### Funcionalidade 3
```lua

function itemManager.categorizeItem(item)
    if item:isWeapon() then
        return 'weapons'
    elseif item:isArmor() then
        return 'armor'
    elseif item:isShield() then
        return 'shields'
    elseif item:isContainer() then
        return 'containers'
    elseif item:isConsumable() or item:isRune() then
        return 'consumables'
    else
        return 'misc'
    end
end

function itemManager.filterItems()
    local searchText = itemManager.searchEdit:getText():lower()
    local category = itemManager.categoryCombo:getCurrentOption().data
    
    itemManager.itemList:destroyChildren()
    
    for itemId, itemInfo in pairs(itemManager.itemDatabase) do
        local matches = true
        
        -- Filtro de texto
        if #searchText > 0 then
            if not itemInfo.description:lower():find(searchText) then
                matches = false
            end
```

#### Funcionalidade 4
```lua
        end
        
        -- Filtro de categoria
        if category ~= 'all' and itemInfo.category ~= category then
            matches = false
        end
        
        if matches then
            local item = g_ui.createWidget('UILabel', itemManager.itemList)
            item:setText(string.format("%d - %s", itemId, itemInfo.description))
            item.itemId = itemId
            item.itemInfo = itemInfo
            
            -- Cor baseada na categoria
            local colors = {
                weapons = '#FF6666',
                armor = '#66FF66',
                shields = '#6666FF',
                containers = '#FFFF66',
                consumables = '#FF66FF',
                misc = '#FFFFFF'
            }
```

#### Funcionalidade 5
```lua
            item:setColor(colors[itemInfo.category] or '#FFFFFF')
        end
    end
end

function itemManager.onItemSelect(itemList, focusedChild)
    if not focusedChild then return end
    
    local itemInfo = focusedChild.itemInfo
    if not itemInfo then return end
    
    itemManager.showItemDetails(itemInfo)
end

function itemManager.showItemDetails(itemInfo)
    itemManager.detailsPanel:destroyChildren()
    
    -- Ícone do item
    local itemIcon = g_ui.createWidget('UIItem', itemManager.detailsPanel)
    itemIcon:setItemId(itemInfo.id)
    itemIcon:setSize({width = 32, height = 32})
    itemIcon:addAnchor(AnchorTop, 'parent', AnchorTop)
    itemIcon:addAnchor(AnchorLeft, 'parent', AnchorLeft)
    itemIcon:setMargin(10)
    
    -- Informações
    local infoText = string.format([[
ID: %d
Descrição: %s
Categoria: %s
Peso: %.2f oz
Empilhável: %s
Movível: %s
Usável: %s
Market: %s]], 
        itemInfo.id,
        itemInfo.description,
        itemInfo.category,
        itemInfo.weight / 100,
        itemInfo.stackable and 'Sim' or 'Não',
        itemInfo.moveable and 'Sim' or 'Não',
        itemInfo.useable and 'Sim' or 'Não',
        itemInfo.marketable and 'Sim' or 'Não'
    )
    
    -- Informações específicas
    if itemInfo.weapon then
        infoText = infoText .. string.format("\nAtaque: %d\nDefesa: %d\nAlcance: %d",
                                           itemInfo.attack or 0,
                                           itemInfo.defense or 0,
                                           itemInfo.range or 0)
    end
```

#### Funcionalidade 6
```lua
    
    if itemInfo.armor then
        infoText = infoText .. string.format("\nArmadura: %d", itemInfo.armorValue or 0)
    end
    
    if itemInfo.container then
        infoText = infoText .. string.format("\nCapacidade: %d", itemInfo.capacity or 0)
    end
    
    local infoLabel = g_ui.createWidget('UILabel', itemManager.detailsPanel)
    infoLabel:setText(infoText)
    infoLabel:setTextWrap(true)
    infoLabel:addAnchor(AnchorTop, 'parent', AnchorTop)
    infoLabel:addAnchor(AnchorLeft, itemIcon, AnchorRight)
    infoLabel:addAnchor(AnchorRight, 'parent', AnchorRight)
    infoLabel:addAnchor(AnchorBottom, 'parent', AnchorBottom)
    infoLabel:setMargin(10)
end

function itemManager.onGameStart()
    -- Atualizar base quando conectar
    scheduleEvent(itemManager.updateItemDatabase, 2000)
end
```

#### Finalização
```lua

function itemManager.onGameEnd()
    -- Limpar ao desconectar
end
```

### Exemplo 3: Smart Container Organizer

#### Inicialização e Configuração
```lua
-- modules/container_organizer/container_organizer.lua
containerOrganizer = {}

function containerOrganizer.init()
    containerOrganizer.rules = {}
    containerOrganizer.window = g_ui.displayUI('container_organizer')
    containerOrganizer.setupInterface()
    containerOrganizer.loadConfiguration()
    
    connect(Container, {
        onOpen = containerOrganizer.onContainerOpen,
        onAddItem = containerOrganizer.onContainerAddItem
    })
end

function containerOrganizer.setupInterface()
    containerOrganizer.rulesList = containerOrganizer.window:getChildById('rulesList')
    containerOrganizer.addRuleButton = containerOrganizer.window:getChildById('addRuleButton')
    containerOrganizer.removeRuleButton = containerOrganizer.window:getChildById('removeRuleButton')
    containerOrganizer.organizeButton = containerOrganizer.window:getChildById('organizeButton')
    
    containerOrganizer.addRuleButton.onClick = containerOrganizer.addRule
    containerOrganizer.removeRuleButton.onClick = containerOrganizer.removeRule
    containerOrganizer.organizeButton.onClick = containerOrganizer.organizeAllContainers
end
```

#### Funcionalidade 1
```lua

function containerOrganizer.addRule()
    local dialog = g_ui.createWidget('UIInputDialog', rootWidget)
    dialog:setText('Nova Regra')
    dialog:setTitle('Adicionar Regra de Organização')
    
    dialog.onOk = function(dialog, text)
        -- Parse da regra: "itemId:containerId" ou "category:containerId"
        local parts = text:split(':')
        if #parts == 2 then
            local rule = {
                condition = parts[1],
                targetContainer = tonumber(parts[2])
            }
            
            table.insert(containerOrganizer.rules, rule)
            containerOrganizer.updateRulesList()
            containerOrganizer.saveConfiguration()
        end
    end
end
```

#### Funcionalidade 2
```lua

function containerOrganizer.organizeAllContainers()
    local containers = g_game.getContainers()
    
    for _, container in pairs(containers) do
        containerOrganizer.organizeContainer(container)
    end
end

function containerOrganizer.organizeContainer(container)
    local items = container:getItems()
    local moves = {}
    
    for slot, item in ipairs(items) do
        local targetContainer = containerOrganizer.findTargetContainer(item)
        
        if targetContainer and targetContainer ~= container then
            table.insert(moves, {
                item = item,
                fromContainer = container,
                toContainer = targetContainer
            })
```

#### Funcionalidade 3
```lua
        end
    end
    
    -- Executar movimentos com delay
    for i, move in ipairs(moves) do
        scheduleEvent(function()
            containerOrganizer.moveItemToContainer(move.item, move.toContainer)
        end, i * 200)
    end
end

function containerOrganizer.findTargetContainer(item)
    for _, rule in ipairs(containerOrganizer.rules) do
        if containerOrganizer.itemMatchesRule(item, rule) then
            local targetContainer = g_game.getContainer(rule.targetContainer)
            if targetContainer and not targetContainer:isFull() then
                return targetContainer
            end
        end
    end
    
    return nil
end
```

#### Funcionalidade 4
```lua

function containerOrganizer.itemMatchesRule(item, rule)
    local condition = rule.condition
    
    -- Regra por ID específico
    if tonumber(condition) then
        return item:getId() == tonumber(condition)
    end
    
    -- Regra por categoria
    if condition == 'weapons' and item:isWeapon() then
        return true
    elseif condition == 'armor' and item:isArmor() then
        return true
    elseif condition == 'containers' and item:isContainer() then
        return true
    elseif condition == 'runes' and item:isRune() then
        return true
    elseif condition == 'potions' and containerOrganizer.isPotion(item) then
        return true
    end
```

#### Funcionalidade 5
```lua
    
    return false
end

function containerOrganizer.isPotion(item)
    local potionIds = {7618, 7620, 7588, 7589, 7591, 7590, 8473, 8472}
    for _, potionId in ipairs(potionIds) do
        if item:getId() == potionId then
            return true
        end
    end
    return false
end

function containerOrganizer.moveItemToContainer(item, targetContainer)
    if not item or not targetContainer then return end
    
    local targetPos = {
        x = 0xFFFF,
        y = targetContainer:getId(),
        z = targetContainer:getFirstEmptySlot() or 0
    }
```

#### Funcionalidade 6
```lua
    
    g_game.move(item, targetPos, item:getCount())
end

function containerOrganizer.onContainerOpen(container)
    -- Auto-organizar quando abrir container (opcional)
    if containerOrganizer.autoOrganize then
        scheduleEvent(function()
            containerOrganizer.organizeContainer(container)
        end, 1000)
    end
end

function containerOrganizer.onContainerAddItem(container, slot, item)
    -- Auto-organizar item adicionado (opcional)
    if containerOrganizer.autoOrganize then
        scheduleEvent(function()
            local targetContainer = containerOrganizer.findTargetContainer(item)
            if targetContainer and targetContainer ~= container then
                containerOrganizer.moveItemToContainer(item, targetContainer)
            end
```

#### Funcionalidade 7
```lua
        end, 500)
    end
end

function containerOrganizer.updateRulesList()
    containerOrganizer.rulesList:destroyChildren()
    
    for i, rule in ipairs(containerOrganizer.rules) do
        local ruleLabel = g_ui.createWidget('UILabel', containerOrganizer.rulesList)
        ruleLabel:setText(string.format("%s → Container %d", rule.condition, rule.targetContainer))
        ruleLabel.ruleIndex = i
    end
end

function containerOrganizer.loadConfiguration()
    local config = g_settings.getNode('containerOrganizer') or {}
    containerOrganizer.rules = config.rules or {}
    containerOrganizer.autoOrganize = config.autoOrganize or false
    
    containerOrganizer.updateRulesList()
end
```

#### Finalização
```lua

function containerOrganizer.saveConfiguration()
    g_settings.setNode('containerOrganizer', {
        rules = containerOrganizer.rules,
        autoOrganize = containerOrganizer.autoOrganize
    })
    g_settings.save()
end
```

---

Esta documentação cobre completamente o sistema de itens do OTClient, desde conceitos básicos até sistemas avançados de gerenciamento, organização e market. Use estes exemplos como base para criar sistemas sofisticados de manipulação de itens em seus módulos.

---

> [!success] Navegação
> - [[Getting_Started_Guide]] - Comece aqui
> - [[Module_System_Guide]] - Desenvolvimento de módulos
> - [[UI_System_Guide]] - Interface do usuário
> - [[Lua_API_Reference]] - Referência completa da API

