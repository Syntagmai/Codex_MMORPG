--[[
    Modular Inventory System - Sistema de Inventário Modal
    =====================================================
    
    Módulo de inventário com interface modal similar ao market,
    substituindo a interface de mini windows do inventário original.
    
    Características:
    - Interface modal com janela principal
    - Slots de equipamento organizados
    - Informações de status do jogador
    - Botões de ação e controle
    - Sistema de duração de itens
    - Integração com sistema de bênçãos
    
    Autor: Sistema BMAD
    Versão: 1.0.0
    Data: 2025-01-27
]]

ModularInventory = {}

-- Variáveis globais
local inventoryWindow = nil
local itemSlotsWithDuration = {}
local updateSlotsDurationEvent = nil
local DURATION_UPDATE_INTERVAL = 1000
local pvpModeRadioGroup = nil

-- Mapeamento de slots para elementos da UI
local getSlotPanelBySlot = {
    [InventorySlotHead] = function(ui) return ui.helmet, ui.helmet.helmet end,
    [InventorySlotNeck] = function(ui) return ui.amulet, ui.amulet.amulet end,
    [InventorySlotBack] = function(ui) return ui.backpack, ui.backpack.backpack end,
    [InventorySlotBody] = function(ui) return ui.armor, ui.armor.armor end,
    [InventorySlotRight] = function(ui) return ui.shield, ui.shield.shield end,
    [InventorySlotLeft] = function(ui) return ui.sword, ui.sword.sword end,
    [InventorySlotLeg] = function(ui) return ui.legs, ui.legs.legs end,
    [InventorySlotFeet] = function(ui) return ui.boots, ui.boots.boots end,
    [InventorySlotFinger] = function(ui) return ui.ring, ui.ring.ring end,
    [InventorySlotAmmo] = function(ui) return ui.tools, ui.tools.tools end
}

-- Função para formatar duração
local function formatDuration(duration)
    return string.format("%dm%02d", duration / 60, duration % 60)
end

-- Função para parar evento de atualização
local function stopEvent()
    if updateSlotsDurationEvent then
        removeEvent(updateSlotsDurationEvent)
        updateSlotsDurationEvent = nil
    end
end

-- Função para atualizar duração dos slots
local function updateSlotsDuration()
    if not g_game.isOnline() or next(itemSlotsWithDuration) == nil then
        stopEvent()
        return
    end

    if not modules.client_options.getOption('showExpiryInInvetory') then
        stopEvent()
        for slot, itemDurationReg in pairs(itemSlotsWithDuration) do
            local getSlotInfo = getSlotPanelBySlot[slot]
            if getSlotInfo then
                local slotPanel = getSlotInfo(inventoryWindow)
                if slotPanel and slotPanel.item then
                    slotPanel.item.duration:setText("")
                end
            end
        end
        return
    end

    local currTime = g_clock.seconds()
    local hasItemsWithDuration = false

    for slot, itemDurationReg in pairs(itemSlotsWithDuration) do
        local item = itemDurationReg.item
        if item and item:getDurationTime() > 0 then
            hasItemsWithDuration = true
            local durationTimeLeft = math.max(0, itemDurationReg.timeEnd - currTime)
            local getSlotInfo = getSlotPanelBySlot[slot]
            if getSlotInfo then
                local slotPanel = getSlotInfo(inventoryWindow)
                if slotPanel and slotPanel.item then
                    slotPanel.item.duration:setText(formatDuration(durationTimeLeft))
                end
            end
        end
    end

    if hasItemsWithDuration then
        updateSlotsDurationEvent = scheduleEvent(updateSlotsDuration, DURATION_UPDATE_INTERVAL)
    else
        stopEvent()
    end
end

-- Função para selecionar postura
local function selectPosture(posture, chase)
    if not g_game.isOnline() then
        return
    end

    local player = g_game.getLocalPlayer()
    if not player then
        return
    end

    if posture == 'stand' then
        player:setChaseMode(ChaseOpponent)
        if chase then
            player:setFollowCreature(nil)
        end
    elseif posture == 'follow' then
        player:setChaseMode(ChaseOpponent)
        if chase then
            player:setFollowCreature(nil)
        end
    end
end

-- Função para alternar modo PvP
local function togglePvpMode(mode)
    if not g_game.isOnline() then
        return
    end

    local player = g_game.getLocalPlayer()
    if not player then
        return
    end

    if mode == 'white' then
        player:setFightMode(FightOffensive)
    elseif mode == 'yellow' then
        player:setFightMode(FightBalanced)
    elseif mode == 'red' then
        player:setFightMode(FightDefensive)
    end
end

-- Função para abrir bolsa
local function openPurse()
    local player = g_game.getLocalPlayer()
    if not player then
        return
    end

    local purse = player:getInventoryItem(InventorySlotPurse)
    if purse then
        g_game.use(purse)
    end
end

-- Função para atualizar informações do jogador
local function updatePlayerInfo()
    if not g_game.isOnline() then
        return
    end

    local player = g_game.getLocalPlayer()
    if not player then
        return
    end

    -- Atualizar informações de status
    if inventoryWindow.healthLabel then
        inventoryWindow.healthLabel:setText(string.format("HP: %d/%d", player:getHealth(), player:getMaxHealth()))
    end

    if inventoryWindow.manaLabel then
        inventoryWindow.manaLabel:setText(string.format("MP: %d/%d", player:getMana(), player:getMaxMana()))
    end

    if inventoryWindow.capacityLabel then
        inventoryWindow.capacityLabel:setText(string.format("Cap: %d/%d", player:getCapacity(), player:getMaxCapacity()))
    end

    if inventoryWindow.soulLabel then
        inventoryWindow.soulLabel:setText(string.format("Soul: %d", player:getSoul()))
    end

    if inventoryWindow.staminaLabel then
        inventoryWindow.staminaLabel:setText(string.format("Stamina: %d", player:getStamina()))
    end
end

-- Função para inicializar interface
local function initInterface()
    -- Criar janela principal
    inventoryWindow = g_ui.createWidget('ModularInventoryWindow', rootWidget)
    inventoryWindow:hide()

    -- Conectar eventos
    connect(g_game, {
        onGameStart = ModularInventory.show,
        onGameEnd = ModularInventory.hide,
        onInventoryChange = ModularInventory.onInventoryChange,
        onPlayerHealthChange = updatePlayerInfo,
        onPlayerManaChange = updatePlayerInfo,
        onPlayerCapacityChange = updatePlayerInfo,
        onPlayerSoulChange = updatePlayerInfo,
        onPlayerStaminaChange = updatePlayerInfo
    })

    -- Configurar botões
    if inventoryWindow.purseButton then
        inventoryWindow.purseButton.onClick = openPurse
    end

    if inventoryWindow.blessingsButton then
        inventoryWindow.blessingsButton.onClick = function()
            modules.game_blessing.toggle()
        end
    end

    if inventoryWindow.closeButton then
        inventoryWindow.closeButton.onClick = ModularInventory.close
    end

    -- Configurar botões de postura
    if inventoryWindow.standButton then
        inventoryWindow.standButton.onClick = function()
            selectPosture('stand', true)
        end
    end

    if inventoryWindow.followButton then
        inventoryWindow.followButton.onClick = function()
            selectPosture('follow', true)
        end
    end

    -- Configurar botões de modo PvP
    if inventoryWindow.whiteModeButton then
        inventoryWindow.whiteModeButton.onClick = function()
            togglePvpMode('white')
        end
    end

    if inventoryWindow.yellowModeButton then
        inventoryWindow.yellowModeButton.onClick = function()
            togglePvpMode('yellow')
        end
    end

    if inventoryWindow.redModeButton then
        inventoryWindow.redModeButton.onClick = function()
            togglePvpMode('red')
        end
    end

    -- Inicializar informações do jogador
    updatePlayerInfo()
end

-- Função para mostrar inventário
function ModularInventory.show()
    if inventoryWindow then
        inventoryWindow:show()
        inventoryWindow:raise()
        inventoryWindow:focus()
        updatePlayerInfo()
    end
end

-- Função para esconder inventário
function ModularInventory.hide()
    if inventoryWindow then
        inventoryWindow:hide()
    end
end

-- Função para alternar visibilidade
function ModularInventory.toggle()
    if inventoryWindow and inventoryWindow:isVisible() then
        ModularInventory.hide()
    else
        ModularInventory.show()
    end
end

-- Função para fechar inventário
function ModularInventory.close()
    ModularInventory.hide()
end

-- Função para lidar com mudanças no inventário
function ModularInventory.onInventoryChange(player, slot, item, oldItem)
    if not inventoryWindow then
        return
    end

    local getSlotInfo = getSlotPanelBySlot[slot]
    if not getSlotInfo then
        return
    end

    local slotPanel = getSlotInfo(inventoryWindow)
    if not slotPanel then
        return
    end

    -- Atualizar item no slot
    if item then
        slotPanel:setItem(item)
        
        -- Configurar duração se necessário
        if item:getDurationTime() > 0 then
            itemSlotsWithDuration[slot] = {
                item = item,
                timeEnd = g_clock.seconds() + item:getDurationTime()
            }
            updateSlotsDuration()
        end
    else
        slotPanel:setItem(nil)
        itemSlotsWithDuration[slot] = nil
    end
end

-- Função de inicialização
function ModularInventory.init()
    initInterface()
end

-- Função de finalização
function ModularInventory.terminate()
    stopEvent()
    
    if inventoryWindow then
        inventoryWindow:destroy()
        inventoryWindow = nil
    end

    disconnect(g_game, {
        onGameStart = ModularInventory.show,
        onGameEnd = ModularInventory.hide,
        onInventoryChange = ModularInventory.onInventoryChange,
        onPlayerHealthChange = updatePlayerInfo,
        onPlayerManaChange = updatePlayerInfo,
        onPlayerCapacityChange = updatePlayerInfo,
        onPlayerSoulChange = updatePlayerInfo,
        onPlayerStaminaChange = updatePlayerInfo
    })
end

-- Exportar módulo
return ModularInventory 