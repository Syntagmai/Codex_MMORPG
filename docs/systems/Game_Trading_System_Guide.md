---
tags: [otclient, game, trade, economy, shop, market, system, guide, documentation]
status: completed
aliases: [Sistema de Trade, Sistema de Economia, Game Store, Market System]
---

# 💰 Sistema de Trade e Economia

> [!info] O Sistema de Trade e Economia do OTClient oferece funcionalidades completas para gerenciar a loja do jogo, transações, histórico de compras e sistema de moedas.

## 📋 Índice
- [[#Visão Geral]]
- [[#Componentes do Sistema]]
- [[#Implementação Prática]]
- [[#Exemplos Práticos]]
- [[#Melhores Práticas]]

---

## 🎯 Visão Geral

O **Sistema de Trade e Economia** do OTClient oferece funcionalidades completas para gerenciar a loja do jogo, transações, histórico de compras e sistema de moedas. O sistema inclui interface de loja, gerenciamento de moedas, histórico de transações e sistema de ofertas.

### 🎨 **Características Principais**

- **Game Store**: Interface completa da loja do jogo
- **Sistema de Moedas**: Gerenciamento de Tibia Coins e Transferable Coins
- **Histórico de Transações**: Rastreamento completo de compras
- **Sistema de Ofertas**: Produtos configuráveis e personalizáveis
- **Filtros Avançados**: Busca e categorização de produtos
- **Integração com Servidor**: Comunicação direta com o servidor

---

## 🔧 Componentes do Sistema

### 🏗️ **Arquitetura do Sistema**

```
Sistema de Trade e Economia
   │
   ├─ Game Store Controller
   │   ├─ Interface Principal
   │   ├─ Categorias de Produtos
   │   ├─ Sistema de Ofertas
   │   └─ Gerenciamento de Estado
   │
   ├─ Sistema de Moedas
   │   ├─ Tibia Coins
   │   ├─ Transferable Coins
   │   ├─ Balance Management
   │   └─ Transfer System
   │
   ├─ Sistema de Transações
   │   ├─ Histórico de Compras
   │   ├─ Status de Transações
   │   ├─ Confirmações
   │   └─ Processamento
   │
   └─ Sistema de Produtos
       ├─ Categorias
       ├─ Subcategorias
       ├─ Filtros
       └─ Configurações
```

### 🎭 **Estrutura de Dados**

#### 💰 **Sistema de Moedas**

```lua
-- Tipos de moedas
    --  Tipos de moedas (traduzido)
GameStore.CoinType = {
    Coin = 0,           -- Tibia Coins regulares
    Transferable = 1    -- Tibia Coins transferíveis
}

-- Estados dos produtos
    --  Estados dos produtos (traduzido)
GameStore.States = {
    STATE_NONE = 0,     -- Estado normal
    STATE_NEW = 1,      -- Produto novo
    STATE_SALE = 2,     -- Produto em promoção
    STATE_TIMED = 3     -- Produto com tempo limitado
}
```

#### 🛍️ **Estrutura de Produto**

#### Nível Basic
```lua
-- Estrutura de um produto da loja
{
    id = productId,           -- ID único do produto
    name = productName,       -- Nome do produto
    description = "",         -- Descrição detalhada
    price = 100,             -- Preço em moedas
    coinType = 0,            -- Tipo de moeda (0 = regular, 1 = transferível)
    count = 1,               -- Quantidade do produto
    configurable = false,    -- Se é configurável
    disabled = false,        -- Se está desabilitado
    subOffers = {},          -- Subofertas do produto
    reasonIdDisable = nil    -- Razão da desabilitação
}
```

#### Nível Intermediate
```lua
-- Estrutura de um produto da loja
{
    id = productId,           -- ID único do produto
    name = productName,       -- Nome do produto
    description = "",         -- Descrição detalhada
    price = 100,             -- Preço em moedas
    coinType = 0,            -- Tipo de moeda (0 = regular, 1 = transferível)
    count = 1,               -- Quantidade do produto
    configurable = false,    -- Se é configurável
    disabled = false,        -- Se está desabilitado
    subOffers = {},          -- Subofertas do produto
    reasonIdDisable = nil    -- Razão da desabilitação
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
```lua
-- Estrutura de um produto da loja
{
    id = productId,           -- ID único do produto
    name = productName,       -- Nome do produto
    description = "",         -- Descrição detalhada
    price = 100,             -- Preço em moedas
    coinType = 0,            -- Tipo de moeda (0 = regular, 1 = transferível)
    count = 1,               -- Quantidade do produto
    configurable = false,    -- Se é configurável
    disabled = false,        -- Se está desabilitado
    subOffers = {},          -- Subofertas do produto
    reasonIdDisable = nil    -- Razão da desabilitação
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

#### 📦 **Estrutura de Categoria**

```lua
-- Estrutura de uma categoria
    --  Estrutura de uma categoria (traduzido)
{
    id = categoryId,         -- ID da categoria
    name = categoryName,     -- Nome da categoria
    description = "",        -- Descrição da categoria
    parent = nil,           -- Categoria pai (se houver)
    subcategories = {},     -- Subcategorias
    products = {}           -- Produtos da categoria
}
```

---

## 💡 Implementação Prática

### 🐍 **API Lua**

#### 📦 **Métodos de Game Store**

```lua
-- Abrir loja
    --  Abrir loja (traduzido)
g_game.openStore()

-- Solicitar página inicial da loja
g_game.sendRequestStoreHome()

-- Solicitar ofertas da loja
    --  Solicitar ofertas da loja (traduzido)
g_game.requestStoreOffers(category, subcategory, page)

-- Comprar oferta da loja
    --  Comprar oferta da loja (traduzido)
g_game.buyStoreOffer(offerId, offerType)

-- Solicitar histórico de transações
g_game.requestTransactionHistory(page)

-- Transferir moedas
    --  Transferir moedas (traduzido)
g_game.transferCoins(amount, characterName)
```

#### 🎯 **Métodos de Controller**

```lua
-- Mostrar loja
    --  Mostrar loja (traduzido)
controllerShop:show()

-- Ocultar loja
    --  Ocultar loja (traduzido)
controllerShop:hide()

-- Alternar visibilidade
    --  Alternar visibilidade (traduzido)
controllerShop:toggle()

-- Mostrar painel específico
showPanel("HomePanel")      -- Painel inicial
showPanel("panelItem")      -- Painel de produtos
showPanel("transferHistory") -- Histórico de transferências
```

#### 💰 **Métodos de Moedas**

```lua
-- Obter saldo de moedas
    --  Obter saldo de moedas (traduzido)
local regularCoins, transferableCoins = getCoinsBalance()

-- Formatar número com vírgulas
local formattedNumber = formatNumberWithCommas(1000000)

-- Verificar se tem moedas suficientes
    --  Verificar se tem moedas suficientes (traduzido)
function hasEnoughCoins(price, coinType)
    -- Função: hasEnoughCoins
    local regular, transferable = getCoinsBalance()
    local balance = (coinType == GameStore.CoinType.Transferable) 
        and transferable or regular
    return balance >= price
end
```

### 🎮 **Implementação Completa do Controller**

#### Inicialização e Configuração
```lua
-- Controller principal da Game Store
controllerShop = Controller:new()

-- Variáveis de controle
local acceptWindow = nil
local changeNameWindow = nil
local transferPointsWindow = nil
local processingWindow = nil
local messageBox = nil

-- Configurações
local oldProtocol = false
local a0xF2 = true

-- Cache de dados
local offerDescriptions = {}
local reasonCategory = {}
local bannersHome = {}

-- Enums do sistema
GameStore = {}

GameStore.CoinType = {
    Coin = 0,
    Transferable = 1
}
```

#### Funcionalidade 1
```lua

GameStore.States = {
    STATE_NONE = 0,
    STATE_NEW = 1,
    STATE_SALE = 2,
    STATE_TIMED = 3
}

GameStore.ClientOfferTypes = {
    CLIENT_STORE_OFFER_OTHER = 0,
    CLIENT_STORE_OFFER_NAMECHANGE = 1,
    CLIENT_STORE_OFFER_WORLD_TRANSFER = 2,
    CLIENT_STORE_OFFER_HIRELING = 3,
    CLIENT_STORE_OFFER_CHARACTER = 4,
    CLIENT_STORE_OFFER_TOURNAMENT = 5,
    CLIENT_STORE_OFFER_CONFIRM = 6
}

-- Função para mostrar painel específico
local function showPanel(panel)
    if panel == "HomePanel" then
        controllerShop.ui.HomePanel:setVisible(true)
        controllerShop.ui.panelItem:setVisible(false)
        controllerShop.ui.transferHistory:setVisible(false)
    elseif panel == "transferHistory" then
        controllerShop.ui.HomePanel:setVisible(false)
        controllerShop.ui.panelItem:setVisible(false)
        controllerShop.ui.transferHistory:setVisible(true)
    elseif panel == "panelItem" then
        controllerShop.ui.HomePanel:setVisible(false)
        controllerShop.ui.panelItem:setVisible(true)
        controllerShop.ui.transferHistory:setVisible(false)
    end
```

#### Funcionalidade 2
```lua
end

-- Função para destruir janelas
local function destroyWindow(windows)
    if type(windows) == "table" then
        for _, window in ipairs(windows) do
            if window and not window:isDestroyed() then
                window:destroy()
            end
        end
    else
        if windows and not windows:isDestroyed() then
            windows:destroy()
        end
    end
    return nil
end

-- Função para obter saldo de moedas
function getCoinsBalance()
    local lblCoins = controllerShop.ui.lblCoins.lblTibiaCoins
    local lblTransfer = controllerShop.ui.lblCoins.lblTibiaTransfer
    
    local regularCoins = tonumber(lblCoins:getText():gsub(",", "")) or 0
    local transferableCoins = tonumber(lblTransfer:getText():match("(%d+)") or "0")
    
    return regularCoins, transferableCoins
end
```

#### Funcionalidade 3
```lua

-- Função para formatar números
function formatNumberWithCommas(number)
    local formatted = tostring(number)
    local k
    while true do
        formatted, k = string.gsub(formatted, "^(-?%d+)(%d%d%d)", '%1,%2')
        if k == 0 then break end
    end
    return formatted
end

-- Função para escolher oferta
function chooseOffert(self, focusedChild)
    if not focusedChild then
        return
    end

    local product = focusedChild.product
    local panel = controllerShop.ui.panelItem
    
    -- Atualizar informações do produto
    panel:getChildById('lblName'):setText(product.name)
    
    local description = product.description or ""
    local subOffers = product.subOffers or {}
    
    if not table.empty(subOffers) then
        local descriptionInfo = offerDescriptions[subOffers[1].id] or { id = 0xFFFF, description = "" }
        description = descriptionInfo.description
    end
```

#### Funcionalidade 4
```lua

    panel:getChildById('lblDescription'):setText(description)

    -- Atualizar imagem do produto
    local data = getProductData(product)
    local imagePanel = panel:getChildById('image')
    imagePanel:destroyChildren()
    if data then
        createProductImage(imagePanel, data)
    end

    -- Atualizar ofertas
    local coinsBalance2, coinsBalance1 = getCoinsBalance()
    local offerStackPanel = panel:getChildById('StackOffers')
    offerStackPanel:destroyChildren()

    local offers = not table.empty(subOffers) and subOffers or { product }
    
    for _, offer in ipairs(offers) do
        local offerPanel = g_ui.createWidget('OfferPanel2', offerStackPanel)

        local priceLabel = offerPanel:getChildById('lblPrice')
        priceLabel:setText(offer.price)

        if offer.count and offer.count > 0 then
            offerPanel:getChildById('btnBuy'):setText("Buy " .. offer.count .. "x")
        end
```

#### Funcionalidade 5
```lua

        if product.configurable then
            offerPanel:getChildById('btnBuy'):setText("Configurable")
        end

        local isTransferable = offer.coinType == GameStore.CoinType.Transferable
        local currentBalance = isTransferable and coinsBalance1 or coinsBalance2

        -- Configurar ícone da moeda
        if isTransferable then
            priceLabel:setIcon("/game_store/images/icon-tibiacointransferable")
        else
            priceLabel:setIcon("images/ui/tibiaCoin")
        end

        -- Verificar se tem moedas suficientes
        if currentBalance < offer.price then
            priceLabel:setColor("#d33c3c")
            offerPanel:getChildById('btnBuy'):disable()
        else
            priceLabel:setColor("white")
            offerPanel:getChildById('btnBuy'):enable()
        end
```

#### Funcionalidade 6
```lua

        -- Configurar botão de compra
        offerPanel:getChildById('btnBuy').onClick = function(widget)
            if acceptWindow then
                destroyWindow(acceptWindow)
            end

            if product.configurable or product.name == "Character Name Change" then
                return displayChangeName(offer)
            end

            local function acceptFunc()
                local latestBalance2, latestBalance1 = getCoinsBalance()
                local latestCurrentBalance = isTransferable and latestBalance1 or latestBalance2
                
                if latestCurrentBalance >= offer.price then
                    g_game.buyStoreOffer(offer.id, GameStore.ClientOfferTypes.CLIENT_STORE_OFFER_OTHER)
                    
                    local closeWindow = function()
                        destroyWindow(processingWindow)
                    end
```

#### Funcionalidade 7
```lua
                    
                    controllerShop.ui:hide()
                    processingWindow = displayGeneralBox('Processing purchase.', 'Your purchase is being processed',
                    {
                        { text = tr('ok'), callback = closeWindow },
                        anchor = 50
                    }, closeWindow, closeWindow)
                else
                    displayErrorBox(controllerShop.ui:getText(), tr("You don't have enough coins"))
                end
                destroyWindow(acceptWindow)
            end
            
            local function cancelFunc()
                destroyWindow(acceptWindow)
            end
            
            local coinType = isTransferable and "transferable coins" or "regular coins"
            local confirmationMessage = string.format("Do you want to buy %s for %d %s?", 
                product.name, offer.price, coinType)
            
            acceptWindow = displayGeneralBox('Confirm Purchase', confirmationMessage,
            {
                { text = tr('Accept'), callback = acceptFunc },
                { text = tr('Cancel'), callback = cancelFunc },
                anchor = 50
            }, cancelFunc, cancelFunc)
```

#### Finalização
```lua
        end
    end
end
```

### 🎨 **Estilo OTUI para Game Store**

```otui
GameStoreWindow < MainWindow
  size: 900 700
  &minimumSize: 800 600

  Panel
    id: HomePanel
    anchors.fill: parent
    layout: verticalBox

    Panel
      id: HomeImagen
      size: 0 200
      image-source: /game_store/images/banner

    Panel
      id: HomeRecentlyAdded
      size: 0 0
      layout: verticalBox

      Label
        text: "Recently Added"
        size: 0 25
        text-align: center

      TextList
        id: HomeProductos
        size: 0 0
        vertical-scrollbar: true

  Panel
    id: panelItem
    anchors.fill: parent
    layout: horizontalBox

    Panel
      id: listCategory
      size: 200 0
      layout: verticalBox

    Panel
      id: panelItemContent
      size: 0 0
      layout: verticalBox

      Panel
        id: productInfo
        size: 0 100
        layout: horizontalBox

        Label
          id: lblName
          text: "Product Name"
          size: 0 25

        Label
          id: lblDescription
          text: "Product Description"
          size: 0 0
          text-wrap: true

      Panel
        id: image
        size: 0 200

      Panel
        id: StackOffers
        size: 0 0
        layout: verticalBox

  Panel
    id: transferHistory
    anchors.fill: parent
    layout: verticalBox

    Panel
      id: historyPanel
      size: 0 0
      layout: verticalBox

    Panel
      id: paginationPanel
      size: 0 30
      layout: horizontalBox

      Button
        id: btnPrevPage
        text: "Previous"
        size: 80 0

      Label
        id: lblPage
        text: "Page 1/1"
        size: 0 0

      Button
        id: btnNextPage
        text: "Next"
        size: 80 0

OfferPanel2 < Panel
  size: 0 50
  layout: horizontalBox

  Label
    id: lblPrice
    text: "100"
    size: 100 0

  Button
    id: btnBuy
    text: "Buy"
    size: 80 0

StoreCategory < Panel
  size: 0 30
  layout: horizontalBox

  Label
    text: "Category Name"
    size: 0 0
```

---

## 💡 Exemplos Práticos

### 🎯 **Exemplo 1: Sistema de Loja Básico**

```lua
local BasicStoreSystem = {}

function BasicStoreSystem.createBasicStore()
    -- Função: BasicStoreSystem
    -- Criar interface da loja
    --  Criar interface da loja (traduzido)
    local storeWindow = g_ui.createWidget('GameStoreWindow', rootWidget)
    storeWindow:hide()
    
    -- Configurar categorias
    --  Configurar categorias (traduzido)
    local categoryList = storeWindow:getChildById('listCategory')
    
    local categories = {
        {id = "outfits", name = "Outfits"},
        {id = "mounts", name = "Mounts"},
        {id = "potions", name = "Potions"},
        {id = "runes", name = "Runes"}
    }
    
    for _, categoryData in ipairs(categories) do
    -- Loop de repetição
        local categoryWidget = g_ui.createWidget('StoreCategory', categoryList)
        categoryWidget:setId(categoryData.id)
        categoryWidget:getChildById('lblName'):setText(categoryData.name)
        
        categoryWidget.onClick = function()
            BasicStoreSystem.loadCategory(categoryData.id)
        end
    end
    
    return storeWindow
end

function BasicStoreSystem.loadCategory(categoryId)
    -- Função: BasicStoreSystem
    -- Solicitar produtos da categoria
    --  Solicitar produtos da categoria (traduzido)
    g_game.requestStoreOffers(categoryId, "", 0)
end

function BasicStoreSystem.showStore()
    -- Função: BasicStoreSystem
    local storeWindow = g_ui.getWidgetById('gameStore')
    if storeWindow then
    -- Verificação condicional
        storeWindow:show()
        g_game.openStore()
    end
end

-- Uso
    --  Uso (traduzido)
local storeSystem = BasicStoreSystem.createBasicStore()
```

### 🎨 **Exemplo 2: Sistema de Moedas Avançado**

#### Inicialização e Configuração
```lua
local AdvancedCoinSystem = {}

function AdvancedCoinSystem.createCoinManager()
    local coinManager = {
        regularCoins = 0,
        transferableCoins = 0,
        listeners = {}
    }
    
    -- Função para atualizar saldo
    function coinManager:updateBalance(regular, transferable)
        self.regularCoins = regular
        self.transferableCoins = transferable
        
        -- Notificar listeners
        for _, listener in ipairs(self.listeners) do
            listener(regular, transferable)
        end
    end
    
    -- Função para verificar se pode comprar
    function coinManager:canAfford(price, coinType)
```

#### Funcionalidade 1
```lua
        local balance = (coinType == GameStore.CoinType.Transferable) 
            and self.transferableCoins or self.regularCoins
        return balance >= price
    end
    
    -- Função para formatar saldo
    function coinManager:formatBalance(coinType)
        local balance = (coinType == GameStore.CoinType.Transferable) 
            and self.transferableCoins or self.regularCoins
        return formatNumberWithCommas(balance)
    end
    
    -- Função para adicionar listener
    function coinManager:addBalanceListener(listener)
        table.insert(self.listeners, listener)
    end
    
    return coinManager
end

function AdvancedCoinSystem.createTransferSystem()
```

#### Funcionalidade 2
```lua
    local transferSystem = {
        history = {},
        maxHistory = 100
    }
    
    -- Função para transferir moedas
    function transferSystem:transferCoins(amount, characterName)
        if amount <= 0 then
            return false, "Invalid amount"
        end
        
        local coinManager = AdvancedCoinSystem.createCoinManager()
        if not coinManager:canAfford(amount, GameStore.CoinType.Transferable) then
            return false, "Insufficient transferable coins"
        end
        
        -- Executar transferência
        g_game.transferCoins(amount, characterName)
        
        -- Adicionar ao histórico
        table.insert(self.history, {
            amount = amount,
            character = characterName,
            timestamp = os.time(),
            status = "pending"
        })
```

#### Finalização
```lua
        
        -- Manter histórico limitado
        if #self.history > self.maxHistory then
            table.remove(self.history, 1)
        end
        
        return true, "Transfer initiated"
    end
    
    -- Função para obter histórico
    function transferSystem:getHistory()
        return self.history
    end
    
    return transferSystem
end

-- Uso
local coinManager = AdvancedCoinSystem.createCoinManager()
local transferSystem = AdvancedCoinSystem.createTransferSystem()
```

### 🪟 **Exemplo 3: Sistema de Produtos Configuráveis**

#### Inicialização e Configuração
```lua
local ConfigurableProductSystem = {}

function ConfigurableProductSystem.createConfigurableProduct(productData)
    local product = {
        id = productData.id,
        name = productData.name,
        configurable = true,
        options = productData.options or {},
        currentConfig = {}
    }
    
    -- Função para configurar produto
    function product:configure(optionId, value)
        self.currentConfig[optionId] = value
    end
    
    -- Função para obter configuração
    function product:getConfiguration()
        return self.currentConfig
    end
    
    -- Função para validar configuração
    function product:isValidConfiguration()
```

#### Funcionalidade 1
```lua
        for _, option in ipairs(self.options) do
            if option.required and not self.currentConfig[option.id] then
                return false
            end
        end
        return true
    end
    
    -- Função para calcular preço
    function product:calculatePrice()
        local basePrice = productData.basePrice or 0
        local totalPrice = basePrice
        
        for optionId, value in pairs(self.currentConfig) do
            local option = self:findOption(optionId)
            if option and option.priceModifier then
                totalPrice = totalPrice + option.priceModifier
            end
        end
        
        return totalPrice
    end
```

#### Funcionalidade 2
```lua
    
    -- Função para encontrar opção
    function product:findOption(optionId)
        for _, option in ipairs(self.options) do
            if option.id == optionId then
                return option
            end
        end
        return nil
    end
    
    return product
end

function ConfigurableProductSystem.createProductConfigurator(product)
    local configurator = {
        product = product,
        ui = nil
    }
    
    -- Função para criar interface
    function configurator:createUI(parent)
```

#### Funcionalidade 3
```lua
        self.ui = g_ui.createWidget('Panel', parent)
        self.ui:setLayout('verticalBox')
        
        -- Criar opções de configuração
        for _, option in ipairs(self.product.options) do
            local optionWidget = self:createOptionWidget(option)
            self.ui:addChild(optionWidget)
        end
        
        -- Botão de confirmação
        local confirmButton = g_ui.createWidget('Button', self.ui)
        confirmButton:setText('Confirm Configuration')
        confirmButton.onClick = function()
            self:confirmConfiguration()
        end
        
        return self.ui
    end
    
    -- Função para criar widget de opção
    function configurator:createOptionWidget(option)
```

#### Funcionalidade 4
```lua
        local optionPanel = g_ui.createWidget('Panel')
        optionPanel:setLayout('horizontalBox')
        
        local label = g_ui.createWidget('Label', optionPanel)
        label:setText(option.name)
        
        if option.type == 'text' then
            local textEdit = g_ui.createWidget('TextEdit', optionPanel)
            textEdit.onTextChange = function(widget, text)
                self.product:configure(option.id, text)
            end
        elseif option.type == 'select' then
            local comboBox = g_ui.createWidget('ComboBox', optionPanel)
            for _, choice in ipairs(option.choices) do
                comboBox:addOption(choice.name, choice.value)
            end
            comboBox.onOptionChange = function(widget, option)
                self.product:configure(option.id, option)
            end
        end
        
        return optionPanel
    end
```

#### Funcionalidade 5
```lua
    
    -- Função para confirmar configuração
    function configurator:confirmConfiguration()
        if not self.product:isValidConfiguration() then
            displayErrorBox("Configuration Error", "Please fill all required fields")
            return
        end
        
        local price = self.product:calculatePrice()
        local config = self.product:getConfiguration()
        
        -- Criar oferta configurada
        local configuredOffer = {
            id = self.product.id,
            price = price,
            configuration = config
        }
        
        -- Processar compra
        self:processPurchase(configuredOffer)
    end
```

#### Funcionalidade 6
```lua
    
    -- Função para processar compra
    function configurator:processPurchase(offer)
        local coinManager = AdvancedCoinSystem.createCoinManager()
        
        if not coinManager:canAfford(offer.price, GameStore.CoinType.Coin) then
            displayErrorBox("Purchase Error", "Insufficient coins")
            return
        end
        
        -- Enviar oferta configurada para o servidor
        g_game.buyStoreOffer(offer.id, GameStore.ClientOfferTypes.CLIENT_STORE_OFFER_CONFIRM)
    end
    
    return configurator
end

-- Exemplo de uso
local productData = {
    id = "character_name_change",
    name = "Character Name Change",
    basePrice = 250,
    configurable = true,
    options = {
        {
            id = "new_name",
            name = "New Character Name",
            type = "text",
            required = true
        },
```

#### Finalização
```lua
        {
            id = "name_type",
            name = "Name Type",
            type = "select",
            required = true,
            choices = {
                {name = "Regular", value = "regular"},
                {name = "Premium", value = "premium"}
            }
        }
    }
}

local product = ConfigurableProductSystem.createConfigurableProduct(productData)
local configurator = ConfigurableProductSystem.createProductConfigurator(product)
```

---

## ✅ Melhores Práticas

### 🎯 **Uso Eficiente**

#### Inicialização e Configuração
```lua
-- ✅ BOM: Sempre verificar se a loja existe
function showStore()
    if not controllerShop.ui then
        return
    end
    
    controllerShop.ui:show()
    controllerShop.ui:raise()
    controllerShop.ui:focus()
end

-- ✅ BOM: Gerenciar saldo de moedas
function updateCoinBalance(regular, transferable)
    if not controllerShop.ui then
        return
    end
    
    controllerShop.ui.lblCoins.lblTibiaCoins:setText(formatNumberWithCommas(regular))
    controllerShop.ui.lblCoins.lblTibiaTransfer:setText(
        string.format("(Including: %s)", formatNumberWithCommas(transferable)))
end
```

#### Funcionalidade 1
```lua

-- ✅ BOM: Validar produtos antes da compra
function validateProductPurchase(product, coinType)
    if not product or not product.id then
        return false, "Invalid product"
    end
    
    if product.disabled then
        return false, "Product is disabled"
    end
    
    local regularCoins, transferableCoins = getCoinsBalance()
    local balance = (coinType == GameStore.CoinType.Transferable) 
        and transferableCoins or regularCoins
    
    if balance < product.price then
        return false, "Insufficient coins"
    end
    
    return true, "Valid purchase"
end
```

#### Finalização
```lua

-- ❌ EVITE: Não verificar existência de widgets
function badShowStore()
    controllerShop.ui:show()  -- Pode falhar se ui não existir
end

-- ❌ EVITE: Não validar saldo
function badPurchase(product)
    g_game.buyStoreOffer(product.id, 0)  -- Sem validação
end
```

### 🎨 **Organização de Código**

#### Inicialização e Configuração
```lua
-- ✅ BOM: Separar responsabilidades
local StoreDataManager = {
    products = {},
    categories = {},
    history = {}
}

function StoreDataManager:addProduct(productData)
    if not productData or not productData.id then
        return false
    end
    
    self.products[productData.id] = productData
    return true
end

function StoreDataManager:getProduct(productId)
    return self.products[productId]
end

function StoreDataManager:addTransaction(transaction)
```

#### Funcionalidade 1
```lua
    table.insert(self.history, {
        id = transaction.id,
        product = transaction.product,
        price = transaction.price,
        timestamp = os.time(),
        status = transaction.status
    })
end

-- ✅ BOM: Usar callbacks para flexibilidade
function createStoreWithCallbacks(storeData, callbacks)
    local store = g_ui.createWidget('GameStoreWindow', parent)
    
    if callbacks.onCreate then
        callbacks.onCreate(store)
    end
    
    if callbacks.onProductSelect then
        store.onProductSelect = callbacks.onProductSelect
    end
    
    if callbacks.onPurchase then
        store.onPurchase = callbacks.onPurchase
    end
```

#### Funcionalidade 2
```lua
    
    return store
end

-- ✅ BOM: Sistema de eventos
local StoreEventSystem = {
    listeners = {}
}

function StoreEventSystem:addEventListener(event, callback)
    if not self.listeners[event] then
        self.listeners[event] = {}
    end
    
    table.insert(self.listeners[event], callback)
end

function StoreEventSystem:triggerEvent(event, data)
    if self.listeners[event] then
        for _, callback in ipairs(self.listeners[event]) do
            callback(data)
        end
```

#### Finalização
```lua
    end
end
```

### 🔧 **Performance e Otimização**

#### Inicialização e Configuração
```lua
-- ✅ BOM: Cache de produtos
local ProductCache = {
    cache = {},
    maxSize = 100
}

function ProductCache:getProduct(productId)
    if self.cache[productId] then
        return self.cache[productId]
    end
    
    -- Carregar produto do servidor
    g_game.requestStoreOffers(productId, "", 0)
    
    -- Criar placeholder
    local placeholder = {
        id = productId,
        name = "Loading...",
        price = 0,
        loading = true
    }
```

#### Funcionalidade 1
```lua
    
    self.cache[productId] = placeholder
    return placeholder
end

function ProductCache:updateProduct(productId, productData)
    self.cache[productId] = productData
    
    -- Manter cache limitado
    local cacheSize = 0
    for _ in pairs(self.cache) do
        cacheSize = cacheSize + 1
    end
    
    if cacheSize > self.maxSize then
        -- Remover item mais antigo
        local oldestKey = nil
        for key in pairs(self.cache) do
            oldestKey = key
            break
        end
```

#### Funcionalidade 2
```lua
        if oldestKey then
            self.cache[oldestKey] = nil
        end
    end
end

-- ✅ BOM: Debounce para busca
local searchDebounce = nil

function debouncedSearch(searchText)
    if searchDebounce then
        removeEvent(searchDebounce)
    end
    
    searchDebounce = scheduleEvent(function()
        g_game.sendRequestStoreSearch(searchText, 0, 1)
        searchDebounce = nil
    end, 300)  -- 300ms delay
end

-- ✅ BOM: Pool de widgets para produtos
local ProductWidgetPool = {
    available = {},
    inUse = {}
}
```

#### Finalização
```lua

function ProductWidgetPool:getWidget()
    if #self.available > 0 then
        local widget = table.remove(self.available)
        table.insert(self.inUse, widget)
        return widget
    end
    
    local widget = g_ui.createWidget('OfferPanel2')
    table.insert(self.inUse, widget)
    return widget
end

function ProductWidgetPool:returnWidget(widget)
    widget:hide()
    widget:setText("")
    widget:setId("")
    
    table.removevalue(self.inUse, widget)
    table.insert(self.available, widget)
end
```

### 🎨 **Estilização e Temas**

#### Inicialização e Configuração
```lua
-- ✅ BOM: Sistema de temas para loja
local storeThemes = {
    default = {
        backgroundColor = '#2c2c2c',
        textColor = '#ffffff',
        accentColor = '#4a90e2',
        errorColor = '#d33c3c',
        successColor = '#27ae60'
    },
    
    dark = {
        backgroundColor = '#1a1a1a',
        textColor = '#e0e0e0',
        accentColor = '#007acc',
        errorColor = '#ff4444',
        successColor = '#2ecc71'
    },
    
    light = {
        backgroundColor = '#f5f5f5',
        textColor = '#333333',
        accentColor = '#2196f3',
        errorColor = '#f44336',
        successColor = '#4caf50'
    }
```

#### Funcionalidade 1
```lua
}

function applyStoreTheme(themeName)
    local theme = storeThemes[themeName] or storeThemes.default
    
    if not controllerShop.ui then
        return
    end
    
    -- Aplicar tema aos widgets
    controllerShop.ui:setBackgroundColor(theme.backgroundColor)
    
    local nameLabel = controllerShop.ui:getChildById('lblName')
    if nameLabel then
        nameLabel:setColor(theme.textColor)
    end
    
    local descriptionLabel = controllerShop.ui:getChildById('lblDescription')
    if descriptionLabel then
        descriptionLabel:setColor(theme.textColor)
    end
```

#### Funcionalidade 2
```lua
end

-- ✅ BOM: Animações suaves
function createAnimatedStore()
    local store = createBasicStore()
    
    -- Animação de entrada
    store:setOpacity(0)
    store:show()
    
    local animation = store:createAnimation()
    animation:setDuration(200)
    animation:setOpacity(1)
    animation:start()
    
    return store
end

-- ✅ BOM: Feedback visual
function showPurchaseFeedback(success, message)
    local feedbackWindow = g_ui.createWidget('MessageBox', rootWidget)
    
    if success then
        feedbackWindow:setText("Purchase Successful")
        feedbackWindow:setColor(storeThemes.default.successColor)
    else
        feedbackWindow:setText("Purchase Failed")
        feedbackWindow:setColor(storeThemes.default.errorColor)
    end
```

#### Finalização
```lua
    
    feedbackWindow:setDescription(message)
    
    -- Auto-destroy após 3 segundos
    scheduleEvent(function()
        if feedbackWindow and not feedbackWindow:isDestroyed() then
            feedbackWindow:destroy()
        end
    end, 3000)
end
```

O sistema de trade e economia oferece ferramentas poderosas para gerenciar a loja do jogo no OTClient. Seguindo as melhores práticas e utilizando os exemplos fornecidos, você pode criar sistemas de loja robustos e eficientes que melhoram significativamente a experiência do usuário.

---

> [!success] **Navegação**
> **📚 Documentos Relacionados:**
> - [[Game_Systems_Guide]] - Sistemas de jogo
> - [[Item_System_Guide]] - Sistema de itens
> - [[Game_Quests_System_Guide]] - Sistema de quest e missões
> - [[UI_System_Guide]] - Sistema de interface
> 
> **🔗 Navegação Rápida:**
> - [[Wiki_Index]] - Voltar ao índice
> - [[Cheat_Sheet]] - Referência rápida
> - [[Getting_Started_Guide]] - Comece aqui 
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

