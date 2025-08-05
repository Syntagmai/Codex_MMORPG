--[[
    Inventory Windows System - Sistema de Inventário com Windows Comum
    =================================================================
    
    Módulo de inventário que mantém 100% da funcionalidade do original,
    mas usa interface de janela comum em vez de mini windows.
    
    DIFERENÇAS DO ORIGINAL:
    - ❌ Mini windows (PhantomMiniWindow) → ✅ MainWindow comum
    - ❌ Interface compacta → ✅ Interface expandida e organizada
    - ❌ Layout minimalista → ✅ Layout com painéis organizados
    - ❌ Tamanho fixo pequeno → ✅ Tamanho ajustável
    
    MANTIDO DO ORIGINAL:
    - ✅ Todos os slots de equipamento
    - ✅ Sistema de duração de itens
    - ✅ Controles de postura (Stand/Follow)
    - ✅ Modos PvP (White/Yellow/Red)
    - ✅ Sistema de bênçãos
    - ✅ Acesso à bolsa
    - ✅ Todas as funcionalidades de jogo
    - ✅ Eventos e atualizações em tempo real
    - ✅ Integração com sistema de opções
    - ✅ Compatibilidade com outros módulos
    - ✅ Configurações e estados salvos
    - ✅ Eventos do jogo (walk, fight, etc.)
    
    Autor: Sistema BMAD
    Versão: 1.0.0
    Data: 2025-01-27
]]

local iconTopMenu = nil

local inventoryShrink = false
local itemSlotsWithDuration = {}
local updateSlotsDurationEvent = nil
local DURATION_UPDATE_INTERVAL = 1000
local pvpModeRadioGroup = nil

-- Mapeamento de slots para elementos da UI (MANTIDO DO ORIGINAL)
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

-- Função para formatar duração (MANTIDO DO ORIGINAL)
local function formatDuration(duration)
    return string.format("%dm%02d", duration / 60, duration % 60)
end

-- Função para parar evento de atualização (MANTIDO DO ORIGINAL)
local function stopEvent()
    if updateSlotsDurationEvent then
        removeEvent(updateSlotsDurationEvent)
        updateSlotsDurationEvent = nil
    end
end

-- Função para atualizar duração dos slots (MANTIDO DO ORIGINAL)
local function updateSlotsDuration()
    if not g_game.isOnline() or next(itemSlotsWithDuration) == nil then
        stopEvent()
        return
    end

    if not modules.client_options.getOption('showExpiryInInvetory') then
        stopEvent()
        local ui = getInventoryUi()
        for slot, itemDurationReg in pairs(itemSlotsWithDuration) do
            local getSlotInfo = getSlotPanelBySlot[slot]
            if getSlotInfo then
                local slotPanel = getSlotInfo(ui)
                if slotPanel and slotPanel.item then
                    slotPanel.item.duration:setText("")
                end
            end
        end
        return
    end

    local currTime = g_clock.seconds()
    local ui = getInventoryUi()
    local hasItemsWithDuration = false

    for slot, itemDurationReg in pairs(itemSlotsWithDuration) do
        local item = itemDurationReg.item
        if item and item:getDurationTime() > 0 then
            hasItemsWithDuration = true
            local durationTimeLeft = math.max(0, itemDurationReg.timeEnd - currTime)
            local getSlotInfo = getSlotPanelBySlot[slot]
            if getSlotInfo then
                local slotPanel = getSlotInfo(ui)
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

-- Função para obter UI do inventário (MANTIDO DO ORIGINAL)
local function getInventoryUi()
    if inventoryShrink then
        return inventoryController.ui.offPanel
    end
    return inventoryController.ui.onPanel
end

-- Função para walk event (MANTIDO DO ORIGINAL)
local function walkEvent()
    if modules.client_options.getOption('autoChaseOverride') then
        if g_game.isAttacking() and g_game.getChaseMode() == ChaseOpponent then
            selectPosture('stand', false)
        end
    end
end

-- Função para combat event (MANTIDO DO ORIGINAL)
local function combatEvent()
    if g_game.getChaseMode() == ChaseOpponent then
        selectPosture('follow', true)
    else
        selectPosture('stand', true)
    end
    
    if g_game.getFightMode() == FightOffensive then
        selectCombat('attack', true)
    elseif g_game.getFightMode() == FightBalanced then
        selectCombat('balanced', true)
    elseif g_game.getFightMode() == FightDefensive then
        selectCombat('defense', true)
    end
end

-- Função para selecionar postura (MANTIDO DO ORIGINAL)
local function selectPosture(posture, chase)
    if not g_game.isOnline() then
        return
    end

    local player = g_game.getLocalPlayer()
    if not player then
        return
    end

    if posture == 'stand' then
        player:setChaseMode(DontChase)
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

-- Função para selecionar combate (MANTIDO DO ORIGINAL)
local function selectCombat(combat, chase)
    if not g_game.isOnline() then
        return
    end

    local player = g_game.getLocalPlayer()
    if not player then
        return
    end

    if combat == 'attack' then
        player:setFightMode(FightOffensive)
    elseif combat == 'balanced' then
        player:setFightMode(FightBalanced)
    elseif combat == 'defense' then
        player:setFightMode(FightDefensive)
    end
end

-- Função para evento de inventário (MANTIDO DO ORIGINAL)
local function inventoryEvent(player, slot, item, oldItem)
    if inventoryShrink then
        return
    end

    local ui = getInventoryUi()
    local getSlotInfo = getSlotPanelBySlot[slot]
    if not getSlotInfo then
        return
    end

    local slotPanel, toggler = getSlotInfo(ui)

    slotPanel.item:setItem(item)
    toggler:setEnabled(not item)
    slotPanel.item:setWidth(34)
    slotPanel.item:setHeight(34)
    slotPanel.item.duration:setText("")
    slotPanel.item.charges:setText("")
    
    if g_game.getFeature(GameThingClock) then
        if item and item:getDurationTime() > 0 then
            if not itemSlotsWithDuration[slot] or itemSlotsWithDuration[slot].item ~= item then
                itemSlotsWithDuration[slot] = {
                    item = item,
                    timeEnd = g_clock.seconds() + item:getDurationTime()
                }
            end
            if modules.client_options.getOption('showExpiryInInvetory') then
                if not updateSlotsDurationEvent then
                    updateSlotsDuration()
                end
            end
        else
            itemSlotsWithDuration[slot] = nil
        end
    end
    
    if modules.client_options.getOption('showExpiryInInvetory') then
        ItemsDatabase.setCharges(slotPanel.item, item)
    end
    ItemsDatabase.setTier(slotPanel.item, item)
end

-- Função para mudança de soul (MANTIDO DO ORIGINAL)
local function onSoulChange(localPlayer, soul)
    local ui = getInventoryUi()
    if not localPlayer then
        return
    end
    if not soul then
        return
    end

    if ui.soulPanel and ui.soulPanel.soul then
        ui.soulPanel.soul:setText(soul)
    end

    if ui.soulAndCapacity and ui.soulAndCapacity.soul then
        ui.soulAndCapacity.soul:setText(soul)
    end
end

-- Função para mudança de capacidade (MANTIDO DO ORIGINAL)
local function onFreeCapacityChange(player, freeCapacity)
    if not player then
        return
    end

    if not freeCapacity then
        return
    end
    if freeCapacity > 99999 then
        freeCapacity = math.min(9999, math.floor(freeCapacity / 1000)) .. "k"
    elseif freeCapacity > 999 then
        freeCapacity = math.floor(freeCapacity)
    elseif freeCapacity > 99 then
        freeCapacity = math.floor(freeCapacity * 10) / 10
    end
    local ui = getInventoryUi()
    if ui.capacityPanel and ui.capacityPanel.capacity then
        ui.capacityPanel.capacity:setText(freeCapacity)
    end
    if ui.soulAndCapacity and ui.soulAndCapacity.capacity then
        ui.soulAndCapacity.capacity:setText(freeCapacity)
    end
end

-- Função para obter painel de ícones ligado (MANTIDO DO ORIGINAL)
function getIconsPanelOn()
    return inventoryController.ui.onPanel.icons
end

-- Função para obter painel de ícones desligado (MANTIDO DO ORIGINAL)
function getIconsPanelOff()
    return inventoryController.ui.offPanel.icons
end

-- Função para atualizar painel do inventário (MANTIDO DO ORIGINAL)
local function refreshInventory_panel()
    local player = g_game.getLocalPlayer()
    if player then
        onSoulChange(player, player:getSoul())
        onFreeCapacityChange(player, player:getFreeCapacity())
    end
    if inventoryShrink then
        return
    end

    for i = InventorySlotFirst, InventorySlotPurse do
        if g_game.isOnline() then
            inventoryEvent(player, i, player:getInventoryItem(i))
        else
            inventoryEvent(player, i, nil)
        end
    end
end

-- Função para atualizar tamanhos do inventário (MANTIDO DO ORIGINAL)
local function refreshInventorySizes()
    if inventoryShrink then
        inventoryController.ui:setOn(false)
        inventoryController.ui.onPanel:hide()
        inventoryController.ui.offPanel:show()
    else
        inventoryController.ui:setOn(true)
        inventoryController.ui.onPanel:show()
        inventoryController.ui.offPanel:hide()
        refreshInventory_panel()
    end
    combatEvent()
    walkEvent()
    modules.game_mainpanel.reloadMainPanelSizes()
end

-- Função para definir modo de perseguição (MANTIDO DO ORIGINAL)
function onSetChaseMode(self, selectedChaseModeButton)
    if selectedChaseModeButton == nil then
        return
    end
    
    local buttonId = selectedChaseModeButton:getId()
    local chaseMode
    if buttonId == 'followPosture' then
        chaseMode = ChaseOpponent
    else
        chaseMode = DontChase
    end
    g_game.setChaseMode(chaseMode)
end

-- Função para definir modo PvP (MANTIDO DO ORIGINAL)
function onSetPVPMode(self, selectedPVPModeButton)
    if selectedPVPModeButton == nil then
        return
    end
    
    local buttonId = selectedPVPModeButton:getId()
    local pvpMode
    if buttonId == 'whiteDoveBox' then
        pvpMode = WhiteDove
    elseif buttonId == 'whiteHandBox' then
        pvpMode = WhiteHand
    elseif buttonId == 'yellowHandBox' then
        pvpMode = YellowHand
    elseif buttonId == 'redFistBox' then
        pvpMode = RedFist
    end
    g_game.setPVPMode(pvpMode)
end

-- Função para definir luta segura (MANTIDO DO ORIGINAL)
function onSetSafeFight(self, checked)
    g_game.setSafeFight(checked)
end

-- Função para modo expert (MANTIDO DO ORIGINAL)
function expertMode(self, checked)
    g_game.setExpertPvpMode(checked)
end

-- Função para alternar tamanho do inventário (MANTIDO DO ORIGINAL)
function changeInventorySize()
    inventoryShrink = not inventoryShrink
    refreshInventorySizes()
end

-- Função para estendida view (MANTIDO DO ORIGINAL)
function extendedView(extendedView)
    if extendedView then
        if not iconTopMenu then
            iconTopMenu = modules.client_topmenu.addTopRightToggleButton('inventory', tr('Show inventory'),
                '/images/topbuttons/inventory', toggle)
            iconTopMenu:setOn(inventoryController.ui:isVisible())
            inventoryController.ui:setBorderColor('black')
            inventoryController.ui:setBorderWidth(2)
        end
    else
        if iconTopMenu then
            iconTopMenu:destroy()
            iconTopMenu = nil
        end
        inventoryController.ui:setBorderColor('alpha')
        inventoryController.ui:setBorderWidth(0)
        local mainRightPanel = modules.game_interface.getMainRightPanel()
        if not mainRightPanel:hasChild(inventoryController.ui) then
            mainRightPanel:insertChild(3, inventoryController.ui)
        end
        inventoryController.ui:show()
    end
    inventoryController.ui.moveOnlyToMain = not extendedView
end

-- Função para alternar visibilidade (MANTIDO DO ORIGINAL)
function toggle()
    if iconTopMenu:isOn() then
        inventoryController.ui:hide()
        iconTopMenu:setOn(false)
    else
        inventoryController.ui:show()
        iconTopMenu:setOn(true)
    end
end

-- Controller do inventário (CORRIGIDO PARA 100% COMPATIBILIDADE)
inventoryController = Controller:new()
inventoryController:setUI('inventory', modules.game_interface.getMainRightPanel())

function inventoryController:onInit()
    refreshInventory_panel()
    local ui = getInventoryUi()

    connect(inventoryController.ui.onPanel.pvp, {
        onCheckChange = onSetSafeFight
    })
    connect(inventoryController.ui.offPanel.pvp, {
        onCheckChange = onSetSafeFight
    })
    connect(inventoryController.ui.onPanel.expert, {
        onCheckChange = expertMode
    })
    
    pvpModeRadioGroup = UIRadioGroup.create()
    pvpModeRadioGroup:addWidget(inventoryController.ui.onPanel.whiteDoveBox)
    pvpModeRadioGroup:addWidget(inventoryController.ui.onPanel.whiteHandBox)
    pvpModeRadioGroup:addWidget(inventoryController.ui.onPanel.yellowHandBox)
    pvpModeRadioGroup:addWidget(inventoryController.ui.onPanel.redFistBox)
    connect(pvpModeRadioGroup, {
        onSelectionChange = onSetPVPMode
    })
end

function inventoryController:onGameStart()
    local player = g_game.getLocalPlayer()
    if player then
        local char = g_game.getCharacterName()
        local lastCombatControls = g_settings.getNode('LastCombatControls')
        if not table.empty(lastCombatControls) then
            if lastCombatControls[char] then
                g_game.setFightMode(lastCombatControls[char].fightMode)
                g_game.setChaseMode(lastCombatControls[char].chaseMode)
                g_game.setSafeFight(lastCombatControls[char].safeFight)
                if lastCombatControls[char].pvpMode then
                    g_game.setPVPMode(lastCombatControls[char].pvpMode)
                end
            end
        end
    end
    
    -- CORREÇÃO: Adicionar :execute() para registrar eventos corretamente
    inventoryController:registerEvents(LocalPlayer, {
        onInventoryChange = inventoryEvent,
        onSoulChange = onSoulChange,
        onFreeCapacityChange = onFreeCapacityChange
    }):execute()

    -- CORREÇÃO: Adicionar eventos do g_game que estavam faltando
    inventoryController:registerEvents(g_game, {
        onWalk = walkEvent,
        onAutoWalk = walkEvent,
        onFightModeChange = combatEvent,
        onChaseModeChange = combatEvent,
        onSafeFightChange = combatEvent,
        onPVPModeChange = combatEvent
    }):execute()

    -- CORREÇÃO: Carregar configurações como no original
    inventoryShrink = g_settings.getBoolean('mainpanel_shrink_inventory')
    refreshInventorySizes()
    refreshInventory_panel()

    -- CORREÇÃO: Mostrar/esconder elementos baseado na versão do cliente
    local elements = {
        {inventoryController.ui.offPanel.blessings, inventoryController.ui.onPanel.blessings},
        {inventoryController.ui.offPanel.expert, inventoryController.ui.onPanel.expert},
        {inventoryController.ui.onPanel.whiteDoveBox},
        {inventoryController.ui.onPanel.whiteHandBox},
        {inventoryController.ui.onPanel.yellowHandBox},
        {inventoryController.ui.onPanel.redFistBox}
    }
    
    local showBlessings = g_game.getClientVersion() >= 1000
    local showPVPMode = g_game.getFeature(GamePVPMode)
    
    for i, elementGroup in ipairs(elements) do
        local show = (i == 1 and showBlessings) or (i > 1 and showPVPMode)
        for _, element in ipairs(elementGroup) do
            if show then
                element:show()
            else
                element:hide()
            end
        end
    end
    inventoryController.ui.onPanel.purseButton:setVisible(g_game.getFeature(GamePurseSlot))
end

function inventoryController:onGameEnd()
    -- CORREÇÃO: Salvar configurações como no original
    local lastCombatControls = g_settings.getNode('LastCombatControls')
    if not lastCombatControls then
        lastCombatControls = {}
    end
    local player = g_game.getLocalPlayer()
    if player then
        local char = g_game.getCharacterName()
        lastCombatControls[char] = {
            fightMode = g_game.getFightMode(),
            chaseMode = g_game.getChaseMode(),
            safeFight = g_game.isSafeFight(),
            pvpMode = g_game.getPVPMode()
        }
        g_settings.setNode('LastCombatControls', lastCombatControls)
    end
    
    inventoryController:unregisterEvents(LocalPlayer)
    inventoryController:unregisterEvents(g_game)
    stopEvent()
end

function inventoryController:onTerminate()
    stopEvent()
    if pvpModeRadioGroup then
        pvpModeRadioGroup:destroy()
        pvpModeRadioGroup = nil
    end
end

-- Exportar funções necessárias
return {
    inventoryController = inventoryController,
    getIconsPanelOn = getIconsPanelOn,
    getIconsPanelOff = getIconsPanelOff,
    changeInventorySize = changeInventorySize,
    extendedView = extendedView,
    toggle = toggle
} 