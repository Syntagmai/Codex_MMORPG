BUY = 1
SELL = 2
CURRENCY = 'gold'
CURRENCY_DECIMAL = false
WEIGHT_UNIT = 'oz'
LAST_INVENTORY = 10

npcWindow = nil
itemsPanel = nil
radioTabs = nil
radioItems = nil
searchText = nil
setupPanel = nil
quantity = nil
quantityScroll = nil
nameLabel = nil
priceLabel = nil
moneyLabel = nil
weightDesc = nil
weightLabel = nil
capacityDesc = nil
capacityLabel = nil
tradeButton = nil
buyTab = nil
sellTab = nil
initialized = false

showWeight = true
buyWithBackpack = nil
ignoreCapacity = nil
ignoreEquipped = nil
showAllItems = nil
sellAllButton = nil

playerFreeCapacity = 0
playerMoney = 0
tradeItems = {}
playerItems = {}
selectedItem = nil

cancelNextRelease = nil

function init()
    npcWindow = g_ui.displayUI('npctrade')
    npcWindow:setVisible(false)

    itemsPanel = npcWindow:recursiveGetChildById('itemsPanel')
    searchText = npcWindow:recursiveGetChildById('searchText')

    setupPanel = npcWindow:recursiveGetChildById('setupPanel')
    quantityScroll = setupPanel:getChildById('quantityScroll')
    nameLabel = setupPanel:getChildById('name')
    priceLabel = setupPanel:getChildById('price')
    moneyLabel = setupPanel:getChildById('money')
    weightDesc = setupPanel:getChildById('weightDesc')
    weightLabel = setupPanel:getChildById('weight')
    capacityDesc = setupPanel:getChildById('capacityDesc')
    capacityLabel = setupPanel:getChildById('capacity')
    tradeButton = npcWindow:recursiveGetChildById('tradeButton')

    buyWithBackpack = npcWindow:recursiveGetChildById('buyWithBackpack')
    ignoreCapacity = npcWindow:recursiveGetChildById('ignoreCapacity')
    ignoreEquipped = npcWindow:recursiveGetChildById('ignoreEquipped')
    showAllItems = npcWindow:recursiveGetChildById('showAllItems')
    sellAllButton = npcWindow:recursiveGetChildById('sellAllButton')

    buyTab = npcWindow:getChildById('buyTab')
    sellTab = npcWindow:getChildById('sellTab')

    radioTabs = UIRadioGroup.create()
    radioTabs:addWidget(buyTab)
    radioTabs:addWidget(sellTab)
    radioTabs:selectWidget(buyTab)
    radioTabs.onSelectionChange = onTradeTypeChange

    cancelNextRelease = false

    if g_game.isOnline() then
        playerFreeCapacity = g_game.getLocalPlayer():getFreeCapacity()
    end

    connect(g_game, {
        onGameEnd = hide,
        onOpenNpcTrade = onOpenNpcTrade,
        onCloseNpcTrade = onCloseNpcTrade,
        onPlayerGoods = onPlayerGoods
    })

    connect(LocalPlayer, {
        onFreeCapacityChange = onFreeCapacityChange,
        onInventoryChange = onInventoryChange
    })

    initialized = true
end

function terminate()
    initialized = false
    npcWindow:destroy()

    disconnect(g_game, {
        onGameEnd = hide,
        onOpenNpcTrade = onOpenNpcTrade,
        onCloseNpcTrade = onCloseNpcTrade,
        onPlayerGoods = onPlayerGoods
    })

    disconnect(LocalPlayer, {
        onFreeCapacityChange = onFreeCapacityChange,
        onInventoryChange = onInventoryChange
    })
end

function show()
    if g_game.isOnline() then
        if #tradeItems[BUY] > 0 then
            radioTabs:selectWidget(buyTab)
        else
            radioTabs:selectWidget(sellTab)
        end

        npcWindow:show()
        npcWindow:raise()
        npcWindow:focus()
    end
end

function hide()
    npcWindow:hide()
end

function onItemBoxChecked(widget)
    if widget:isChecked() then
        local item = widget.item
        selectedItem = item
        refreshItem(item)
        tradeButton:enable()

        if getCurrentTradeType() == SELL then
            quantityScroll:setValue(quantityScroll:getMaximum())
        end
    end
end

function onQuantityValueChange(quantity)
    if selectedItem then
        weightLabel:setText(string.format('%.2f', selectedItem.weight * quantity) .. ' ' .. WEIGHT_UNIT)
        priceLabel:setText(formatCurrency(getItemPrice(selectedItem)))
    end
end


-- ========================================
-- MODIFICAÇÃO: Remover opção Buy with Backpack
-- ========================================

function onTradeTypeChange(radioTabs, selected, deselected)
    tradeButton:setText(selected:getText())
    selected:setOn(true)
    deselected:setOn(false)

    local currentTradeType = getCurrentTradeType()
    -- SEMPRE ocultar buyWithBackpack (modificação)
    buyWithBackpack:setVisible(false)
    ignoreCapacity:setVisible(currentTradeType == BUY)
    ignoreEquipped:setVisible(currentTradeType == SELL)
    showAllItems:setVisible(currentTradeType == SELL)
    sellAllButton:setVisible(currentTradeType == SELL)

    refreshTradeItems()
    refreshPlayerGoods()
end

-- Interceptar função de compra para sempre usar false
local originalBuyItem = g_game.buyItem
g_game.buyItem = function(item, amount, ignoreCapacity, buyWithBackpack)
    -- Sempre usar false para buyWithBackpack
    return originalBuyItem(item, amount, ignoreCapacity, false)
end


    tradeItems[SELL] = {}

    for key, item in pairs(items) do
        if item[4] > 0 then
            local newItem = {}
            newItem.ptr = item[1]
            newItem.name = item[2]
            newItem.weight = item[3] / 100
            newItem.price = item[4]
            table.insert(tradeItems[BUY], newItem)
        end

        if item[5] > 0 then
            local newItem = {}
            newItem.ptr = item[1]
            newItem.name = item[2]
            newItem.weight = item[3] / 100
            newItem.price = item[5]
            table.insert(tradeItems[SELL], newItem)
        end
    end

    refreshTradeItems()
    addEvent(show) -- player goods has not been parsed yet
end

function closeNpcTrade()
    g_game.closeNpcTrade()
    hide()
end

function onCloseNpcTrade()
    hide()
end

function onPlayerGoods(money, items)
    playerMoney = money

    playerItems = {}
    for key, item in pairs(items) do
        local id = item[1]:getId()
        if not playerItems[id] then
            playerItems[id] = item[2]
        else
            playerItems[id] = playerItems[id] + item[2]
        end
    end

    refreshPlayerGoods()
end

function onFreeCapacityChange(localPlayer, freeCapacity, oldFreeCapacity)
    playerFreeCapacity = freeCapacity

    if npcWindow:isVisible() then
        refreshPlayerGoods()
    end
end

function onInventoryChange(inventory, item, oldItem)
    refreshPlayerGoods()
end

function getTradeItemData(id, type)
    if table.empty(tradeItems[type]) then
        return false
    end

    if type then
        for key, item in pairs(tradeItems[type]) do
            if item.ptr and item.ptr:getId() == id then
                return item
            end
        end
    else
        for _, items in pairs(tradeItems) do
            for key, item in pairs(items) do
                if item.ptr and item.ptr:getId() == id then
                    return item
                end
            end
        end
    end
    return false
end

function checkSellAllTooltip()
    sellAllButton:setEnabled(true)
    sellAllButton:removeTooltip()

    local total = 0
    local info = ''
    local first = true

    for key, amount in pairs(playerItems) do
        local data = getTradeItemData(key, SELL)
        if data then
            amount = getSellQuantity(data.ptr)
            if amount > 0 then
                if data and amount > 0 then
                    info = info .. (not first and '\n' or '') .. amount .. ' ' .. data.name .. ' (' .. data.price *
                               amount .. ' gold)'

                    total = total + (data.price * amount)
                    if first then
                        first = false
                    end
                end
            end
        end
    end
    if info ~= '' then
        info = info .. '\nTotal: ' .. total .. ' gold'
        sellAllButton:setTooltip(info)
    else
        sellAllButton:setEnabled(false)
    end
end

function formatCurrency(amount)
    if CURRENCY_DECIMAL then
        return string.format('%.02f', amount / 100.0) .. ' ' .. CURRENCY
    else
        return amount .. ' ' .. CURRENCY
    end
end

function getMaxAmount()
    if getCurrentTradeType() == SELL and g_game.getFeature(GameDoubleShopSellAmount) then
        return 10000
    end
    return 100
end

function sellAll()
    for itemid, item in pairs(playerItems) do
        local item = Item.create(itemid)
        local amount = getSellQuantity(item)
        if amount > 0 then
            g_game.sellItem(item, amount, ignoreEquipped:isChecked())
        end
    end
end
