---
tags: [projects, practical, canary, server, npcs, educational, beginner, lua_scripting, modification]
aliases: [servidor_basico_npcs, basic_server_npcs, canary_server_project, lua_modification]
type: practical_project
status: active
priority: high
level: beginner
created: 2025-08-05
updated: 2025-08-05
project: 01
course: canary
prerequisites: [2.1_canary_introduction, 2.2_core_architecture, 2.3_scripting_system]
next_project: 02_cliente_interface_simples
---

# 🎮 **Projeto 1: Modificando NPCs e Comportamentos no Canary**

## 🎯 **Visão Geral**

Este projeto prático ensina como **modificar e estender** um servidor Canary existente, focando em Lua scripting para criar NPCs personalizados e comportamentos de jogo. Você aprenderá como trabalhar com a base Open Tibia existente para transformá-la no seu MMORPG desejado.

## 📚 **Objetivos do Projeto**

### **🎯 Ao final deste projeto, você será capaz de:**
- ✅ Entender como o Canary organiza NPCs e scripts
- ✅ Criar NPCs personalizados usando Lua scripting
- ✅ Modificar comportamentos existentes sem alterar o código C++
- ✅ Implementar sistemas de diálogo e interação
- ✅ Adicionar novas funcionalidades via moveevents e revscripts
- ✅ Trabalhar com a estrutura de dados existente do Canary

## 🏗️ **Estrutura do Projeto**

### **📁 Organização dos Arquivos (Baseado no Canary Real)**
```
canary/data/
├── npc/
│   ├── merchant.lua          # NPC comerciante (modificado)
│   ├── guard.lua             # NPC guarda (modificado)
│   └── custom/
│       ├── quest_giver.lua   # NPC de missões (novo)
│       └── trainer.lua       # NPC treinador (novo)
├── scripts/
│   ├── moveevents/
│   │   ├── custom_teleport.lua    # Teleporte personalizado
│   │   └── magic_door.lua         # Porta mágica
│   └── revscripts/
│       ├── custom_spells.lua      # Magias personalizadas
│       └── special_items.lua      # Itens especiais
└── config.lua.dist              # Configuração do servidor
```

## 🔧 **Implementação**

### **📖 1. Entendendo a Estrutura Existente do Canary**

#### **🏗️ Como o Canary Organiza NPCs**
O Canary usa uma estrutura específica para NPCs. Vamos entender como funciona:

```lua
-- Estrutura básica de um NPC no Canary
local npc = {
    name = "Merchant",
    type = "merchant",
    script = "merchant.lua"
}

-- O Canary carrega NPCs de canary/data/npc/
-- Cada NPC tem seu próprio script Lua
```

#### **🔍 Localização dos Arquivos no Canary**
```bash
# NPCs principais
canary/data/npc/merchant.lua
canary/data/npc/guard.lua
canary/data/npc/priest.lua

# Scripts de eventos
canary/data/scripts/moveevents/
canary/data/scripts/revscripts/

# Configurações
canary/config.lua.dist
```

### **📖 2. Modificando NPCs Existentes**

#### **🛠️ Exemplo: Personalizando o Merchant NPC**
Vamos modificar o NPC comerciante existente para adicionar funcionalidades:

```lua
-- canary/data/npc/merchant.lua (modificado)
local npc = {
    name = "Merchant",
    type = "merchant",
    script = "merchant.lua"
}

-- Adicionando funcionalidades personalizadas
function npc:onInteract(player)
    -- Comportamento original do merchant
    local dialog = self.dialogs.greet
    player:sendTextMessage(dialog)
    
    -- NOVA FUNCIONALIDADE: Sistema de reputação
    local reputation = player:getStorageValue("merchant_reputation") or 0
    if reputation > 100 then
        player:sendTextMessage("Você tem desconto especial por ser um cliente VIP!")
        -- Aplicar desconto de 10%
        self.discount = 0.10
    end
    
    player:openShop(self.items)
end

-- NOVA FUNCIONALIDADE: Evento de compra
function npc:onPlayerBuy(player, itemId, count)
    -- Aumentar reputação do jogador
    local currentRep = player:getStorageValue("merchant_reputation") or 0
    player:setStorageValue("merchant_reputation", currentRep + 1)
    
    -- Log da transação
    print(string.format("Player %s bought %d of item %d", 
          player:getName(), count, itemId))
end

return npc
```

#### **🛠️ Exemplo: Criando um NPC de Missões Personalizado**
```lua
-- canary/data/npc/custom/quest_giver.lua (novo)
local npc = {
    name = "Quest Master",
    type = "quest_giver",
    script = "custom/quest_giver.lua"
}

-- Sistema de missões personalizado
local quests = {
    {
        id = 1,
        name = "Primeira Missão",
        description = "Mate 5 ratos",
        target = {monster = "rat", count = 5},
        reward = {item = 2160, count = 10} -- 10 gold coins
    }
}

function npc:onInteract(player)
    local playerQuests = player:getStorageValue("active_quests") or {}
    
    -- Verificar se o jogador tem missões ativas
    for _, quest in ipairs(quests) do
        if not playerQuests[quest.id] then
            -- Oferecer nova missão
            player:sendTextMessage(string.format(
                "Missão disponível: %s - %s", 
                quest.name, quest.description
            ))
            player:sendTextMessage("Digite 'accept' para aceitar a missão.")
            return
        end
    end
    
    player:sendTextMessage("Você completou todas as missões disponíveis!")
end

return npc
```

### **📖 3. Criando MoveEvents Personalizados**

#### **🛠️ Exemplo: Teleporte Personalizado**
```lua
-- canary/data/scripts/moveevents/custom_teleport.lua
local teleport = MoveEvent()

function teleport.onStepIn(creature, item, position, fromPosition)
    if not creature:isPlayer() then
        return true
    end
    
    local player = creature
    local destination = Position(1000, 1000, 7) -- Coordenadas de destino
    
    -- Verificar se o jogador tem permissão
    if player:getLevel() < 10 then
        player:sendTextMessage("Você precisa ser nível 10 para usar este teleporte.")
        player:teleportTo(fromPosition)
        return false
    end
    
    -- Efeito visual
    player:getPosition():sendMagicEffect(CONST_ME_TELEPORT)
    
    -- Teleportar
    player:teleportTo(destination)
    
    -- Efeito no destino
    destination:sendMagicEffect(CONST_ME_TELEPORT)
    
    return true
end

teleport:aid(4001) -- Action ID do teleporte
teleport:register()
```

#### **🛠️ Exemplo: Porta Mágica com Senha**
```lua
-- canary/data/scripts/moveevents/magic_door.lua
local magicDoor = MoveEvent()

function magicDoor.onStepIn(creature, item, position, fromPosition)
    if not creature:isPlayer() then
        return true
    end
    
    local player = creature
    local password = "abracadabra"
    
    -- Verificar se o jogador tem a senha
    if player:getStorageValue("magic_door_password") == 1 then
        -- Abrir porta
        item:transform(item:getId() + 1) -- Transformar em porta aberta
        player:sendTextMessage("A porta mágica se abre!")
        return true
    else
        -- Pedir senha
        player:sendTextMessage("Esta porta requer uma senha mágica.")
        player:teleportTo(fromPosition)
        return false
    end
end

magicDoor:aid(4002) -- Action ID da porta
magicDoor:register()
```

### **📖 4. Criando RevScripts para Funcionalidades Avançadas**

#### **🛠️ Exemplo: Sistema de Magias Personalizadas**
```lua
-- canary/data/scripts/revscripts/custom_spells.lua
local customSpells = {}

-- Magia personalizada: Raio de Energia
customSpells.energyBeam = {
    name = "Energy Beam",
    words = "exevo vis lux",
    level = 8,
    mana = 40,
    cooldown = 2000, -- 2 segundos
    
    cast = function(player, target)
        if not target then
            player:sendTextMessage("Você precisa mirar em um alvo.")
            return false
        end
        
        -- Calcular dano baseado no nível do jogador
        local damage = math.floor(player:getLevel() * 1.5)
        
        -- Efeito visual
        player:getPosition():sendMagicEffect(CONST_ME_ENERGYAREA)
        
        -- Aplicar dano
        target:addHealth(-damage)
        
        -- Mensagem de combate
        player:sendTextMessage(string.format(
            "Você causou %d de dano com Energy Beam!", damage
        ))
        
        return true
    end
}

-- Registrar a magia no sistema
for spellName, spellData in pairs(customSpells) do
    -- Aqui você integraria com o sistema de magias do Canary
    -- Esta é uma implementação conceitual
    print(string.format("Magia registrada: %s", spellName))
end
```

#### **🛠️ Exemplo: Itens Especiais com Efeitos**
```lua
-- canary/data/scripts/revscripts/special_items.lua
local specialItems = {}

-- Item: Anel de Regeneração
specialItems.ringOfRegeneration = {
    itemId = 3001,
    name = "Ring of Regeneration",
    
    onEquip = function(player, item)
        -- Adicionar efeito de regeneração
        player:setStorageValue("regen_effect", 1)
        player:sendTextMessage("Você sente uma energia curativa fluindo através do anel.")
    end,
    
    onUnequip = function(player, item)
        -- Remover efeito
        player:setStorageValue("regen_effect", 0)
        player:sendTextMessage("A energia curativa do anel se dissipa.")
    end,
    
    onUse = function(player, item)
        -- Efeito especial quando usado
        local health = player:getHealth()
        local maxHealth = player:getMaxHealth()
        
        if health < maxHealth then
            local heal = math.floor(maxHealth * 0.3) -- Curar 30%
            player:addHealth(heal)
            player:sendTextMessage(string.format("O anel cura %d pontos de vida!", heal))
            
            -- Efeito visual
            player:getPosition():sendMagicEffect(CONST_ME_MAGIC_BLUE)
        else
            player:sendTextMessage("Você já está com vida cheia.")
        end
    end
}

-- Sistema de regeneração automática
local function checkRegeneration()
    for _, player in pairs(Game.getPlayers()) do
        if player:getStorageValue("regen_effect") == 1 then
            local health = player:getHealth()
            local maxHealth = player:getMaxHealth()
            
            if health < maxHealth then
                -- Regenerar 1 HP a cada 10 segundos
                player:addHealth(1)
            end
        end
    end
end

-- Executar verificação a cada 10 segundos
addEvent(checkRegeneration, 10000)
```

### **📖 5. Configuração do Servidor**

#### **⚙️ Modificando config.lua.dist**
```lua
-- canary/config.lua.dist (modificações)
-- Configurações para NPCs personalizados
npcEnabled = true
npcPath = "data/npc/"
customNpcPath = "data/npc/custom/"

-- Configurações para scripts personalizados
moveEventsEnabled = true
moveEventsPath = "data/scripts/moveevents/"

revScriptsEnabled = true
revScriptsPath = "data/scripts/revscripts/"

-- Configurações de debug para desenvolvimento
debugMode = true
logLevel = "info"
```

## 🎯 **Exercícios Práticos**

### **📝 Exercício 1: NPC Comerciante Personalizado**
**Objetivo**: Modificar o NPC comerciante existente para incluir um sistema de lealdade.

**Tarefas**:
1. Abra `canary/data/npc/merchant.lua`
2. Adicione um sistema de pontos de lealdade
3. Implemente descontos baseados na lealdade
4. Crie um comando para verificar pontos de lealdade

**Código Base**:
```lua
-- Adicione ao merchant.lua existente
function npc:onPlayerBuy(player, itemId, count)
    -- Implementar sistema de lealdade
    local loyalty = player:getStorageValue("merchant_loyalty") or 0
    player:setStorageValue("merchant_loyalty", loyalty + count)
    
    -- Aplicar desconto baseado na lealdade
    if loyalty > 1000 then
        -- Desconto de 15%
        player:sendTextMessage("Desconto VIP aplicado: 15%")
    elseif loyalty > 500 then
        -- Desconto de 10%
        player:sendTextMessage("Desconto aplicado: 10%")
    end
end
```

### **📝 Exercício 2: Sistema de Teleportes Personalizado**
**Objetivo**: Criar um sistema de teleportes que requer itens específicos.

**Tarefas**:
1. Crie um novo moveevent em `canary/data/scripts/moveevents/`
2. Implemente verificação de itens necessários
3. Adicione efeitos visuais personalizados
4. Crie um sistema de cooldown

**Código Base**:
```lua
-- Novo arquivo: canary/data/scripts/moveevents/item_teleport.lua
local itemTeleport = MoveEvent()

function itemTeleport.onStepIn(creature, item, position, fromPosition)
    if not creature:isPlayer() then
        return true
    end
    
    local player = creature
    local requiredItem = 2160 -- Gold coin
    local requiredCount = 5
    
    -- Verificar se o jogador tem o item necessário
    if player:getItemCount(requiredItem) >= requiredCount then
        -- Remover itens
        player:removeItem(requiredItem, requiredCount)
        
        -- Teleportar
        local destination = Position(1000, 1000, 7)
        player:teleportTo(destination)
        
        -- Efeitos visuais
        fromPosition:sendMagicEffect(CONST_ME_TELEPORT)
        destination:sendMagicEffect(CONST_ME_TELEPORT)
        
        player:sendTextMessage("Teleporte realizado com sucesso!")
    else
        player:sendTextMessage(string.format(
            "Você precisa de %d gold coins para usar este teleporte.", 
            requiredCount
        ))
        player:teleportTo(fromPosition)
    end
    
    return true
end

itemTeleport:aid(4003)
itemTeleport:register()
```

### **📝 Exercício 3: Sistema de Missões Simples**
**Objetivo**: Implementar um sistema básico de missões usando storage values.

**Tarefas**:
1. Crie um NPC de missões personalizado
2. Implemente sistema de progresso de missão
3. Adicione sistema de recompensas
4. Crie verificação de conclusão de missão

**Código Base**:
```lua
-- Novo arquivo: canary/data/npc/custom/mission_npc.lua
local missionNPC = {
    name = "Mission Master",
    type = "mission_giver",
    script = "custom/mission_npc.lua"
}

local missions = {
    {
        id = 1,
        name = "Caçador de Ratos",
        description = "Mate 10 ratos",
        target = {monster = "rat", count = 10},
        reward = {item = 2160, count = 50}
    }
}

function missionNPC:onInteract(player)
    local activeMission = player:getStorageValue("active_mission_id")
    local missionProgress = player:getStorageValue("mission_progress") or 0
    
    if activeMission == 0 then
        -- Oferecer missão
        player:sendTextMessage("Missão disponível: Caçador de Ratos")
        player:sendTextMessage("Digite 'accept' para aceitar.")
    else
        -- Verificar progresso
        if missionProgress >= missions[activeMission].target.count then
            -- Completar missão
            local reward = missions[activeMission].reward
            player:addItem(reward.item, reward.count)
            player:setStorageValue("active_mission_id", 0)
            player:setStorageValue("mission_progress", 0)
            player:sendTextMessage("Missão completada! Recompensa recebida.")
        else
            player:sendTextMessage(string.format(
                "Progresso: %d/%d ratos mortos", 
                missionProgress, 
                missions[activeMission].target.count
            ))
        end
    end
end

return missionNPC
```

## 🔍 **Conceitos-Chave Aprendidos**

### **🎯 Modificação vs Re-implementação**
- **✅ Correto**: Modificar comportamentos existentes via Lua
- **❌ Incorreto**: Re-escrever sistemas completos em C++

### **🎯 Lua Scripting para Game Logic**
- **MoveEvents**: Para eventos de movimento e interação
- **RevScripts**: Para funcionalidades avançadas e personalizadas
- **NPC Scripts**: Para comportamentos de NPCs
- **Storage Values**: Para persistência de dados do jogador

### **🎯 C++ Apenas para Mudanças Estruturais**
- **Sistema de Combate**: Modificações no core do jogo
- **Novas Vocações**: Adições estruturais
- **Novas Condições**: Mecânicas fundamentais
- **Protocolo de Rede**: Mudanças na comunicação

### **🎯 Trabalhando com a Base Existente**
- **Entender a estrutura**: Como o Canary organiza arquivos
- **Respeitar convenções**: Seguir padrões existentes
- **Extensão gradual**: Adicionar funcionalidades sem quebrar o existente
- **Debugging**: Usar ferramentas existentes do Canary

## 🚀 **Próximos Passos**

### **📚 Módulos Relacionados**
- [[2.3_scripting_system|Sistema de Scripting Lua]]
- [[2.4_game_mechanics|Mecânicas do Jogo]]
- [[4.1_comunicacao_protocolo|Comunicação e Protocolo]]

### **🎮 Projetos Relacionados**
- [[02_cliente_interface_simples|Projeto 2: Interface do Cliente]]
- [[03_sistema_chat_completo|Projeto 3: Sistema de Chat]]

### **🔧 Ferramentas Úteis**
- **Canary Documentation**: `canary/docs/`
- **Lua Scripting Guide**: `canary/data/libs/`
- **Debug Tools**: `canary/tools/`

---

> [!success] **Projeto Concluído**
> ✅ **Objetivo**: Aprender a modificar e estender um servidor Canary existente
> ✅ **Foco**: Lua scripting para game logic, C++ apenas para mudanças estruturais
> ✅ **Resultado**: Capacidade de trabalhar com a base Open Tibia existente
> 🎯 **Próximo**: [[02_cliente_interface_simples|Projeto 2: Interface do Cliente]] 