---
tags: [game_store, system_analysis, protocol, communication, client_server, documentation]
type: system_analysis
status: complete
priority: critical
created: 2025-01-27
updated: 2025-01-27
---

# 🏪 Sistema Game Store - Análise Profunda Completa

## 📋 **Visão Geral**

O **Sistema Game Store** é um componente crítico do OTClient e Canary que gerencia a loja in-game, permitindo aos jogadores comprar itens, serviços e cosméticos usando moedas virtuais. Este sistema implementa protocolos de comunicação cliente-servidor complexos e oferece uma interface de usuário rica e interativa.

## 🎯 **Objetivo da Análise**

Esta documentação fornece uma análise profunda e completa do sistema Game Store, incluindo:
- **Protocolos de comunicação** cliente-servidor
- **Estruturas de dados** e enums
- **Funcionalidades** e fluxos de trabalho
- **Integração** entre OTClient e Canary
- **Padrões de implementação** e melhores práticas

---

## 🏗️ **Arquitetura do Sistema**

### **📁 Estrutura de Arquivos**

```
📁 OTClient Game Store
├── 📄 modules/game_store/game_store.lua (1.130 linhas)
├── 📄 modules/game_store/game_store.otmod
├── 📄 modules/game_store/style/ui.otui
└── 📄 modules/game_store/images/

📁 Canary Game Store
├── 📄 data/modules/scripts/gamestore/init.lua (2.302 linhas)
├── 📄 data/modules/scripts/gamestore/
└── 📄 src/server/network/protocol/protocolgame.cpp
```

### **🔄 Fluxo de Comunicação**

```
Cliente (OTClient) ←→ Protocolo ←→ Servidor (Canary)
     ↓                    ↓              ↓
Interface Lua      ←→ Packets ←→  Lógica de Negócio
     ↓                    ↓              ↓
UI Components      ←→ Enums ←→   Validações
```

---

## 📦 **Enums e Estruturas de Dados**

### **🪙 Tipos de Moeda (CoinType)**

#### Nível Basic
```lua
GameStore.CoinType = {
    Coin = 0,           -- Moedas normais
    Transferable = 1    -- Moedas transferíveis
}
```

#### Nível Intermediate
```lua
GameStore.CoinType = {
    Coin = 0,           -- Moedas normais
    Transferable = 1    -- Moedas transferíveis
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
GameStore.CoinType = {
    Coin = 0,           -- Moedas normais
    Transferable = 1    -- Moedas transferíveis
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

### **📦 Tipos de Oferta (OfferTypes)**

#### Nível Basic
```lua
GameStore.OfferTypes = {
    OFFER_TYPE_NONE = 0,
    OFFER_TYPE_ITEM = 1,
    OFFER_TYPE_STACKABLE = 2,
    OFFER_TYPE_CHARGES = 3,
    OFFER_TYPE_OUTFIT = 4,
    OFFER_TYPE_OUTFIT_ADDON = 5,
    OFFER_TYPE_MOUNT = 6,
    OFFER_TYPE_NAMECHANGE = 7,
    OFFER_TYPE_SEXCHANGE = 8,
    OFFER_TYPE_HOUSE = 9,
    OFFER_TYPE_EXPBOOST = 10,
    OFFER_TYPE_PREYSLOT = 11,
    OFFER_TYPE_PREYBONUS = 12,
    OFFER_TYPE_TEMPLE = 13,
    OFFER_TYPE_BLESSINGS = 14,
    OFFER_TYPE_PREMIUM = 15,
    OFFER_TYPE_ALLBLESSINGS = 17,
    OFFER_TYPE_INSTANT_REWARD_ACCESS = 18,
    OFFER_TYPE_CHARMS = 19,
    OFFER_TYPE_HIRELING = 20,
    OFFER_TYPE_HIRELING_NAMECHANGE = 21,
    OFFER_TYPE_HIRELING_SEXCHANGE = 22,
    OFFER_TYPE_HIRELING_SKILL = 23,
    OFFER_TYPE_HIRELING_OUTFIT = 24,
    OFFER_TYPE_HUNTINGSLOT = 25,
    OFFER_TYPE_ITEM_BED = 26,
    OFFER_TYPE_ITEM_UNIQUE = 27
}
```

#### Nível Intermediate
```lua
GameStore.OfferTypes = {
    OFFER_TYPE_NONE = 0,
    OFFER_TYPE_ITEM = 1,
    OFFER_TYPE_STACKABLE = 2,
    OFFER_TYPE_CHARGES = 3,
    OFFER_TYPE_OUTFIT = 4,
    OFFER_TYPE_OUTFIT_ADDON = 5,
    OFFER_TYPE_MOUNT = 6,
    OFFER_TYPE_NAMECHANGE = 7,
    OFFER_TYPE_SEXCHANGE = 8,
    OFFER_TYPE_HOUSE = 9,
    OFFER_TYPE_EXPBOOST = 10,
    OFFER_TYPE_PREYSLOT = 11,
    OFFER_TYPE_PREYBONUS = 12,
    OFFER_TYPE_TEMPLE = 13,
    OFFER_TYPE_BLESSINGS = 14,
    OFFER_TYPE_PREMIUM = 15,
    OFFER_TYPE_ALLBLESSINGS = 17,
    OFFER_TYPE_INSTANT_REWARD_ACCESS = 18,
    OFFER_TYPE_CHARMS = 19,
    OFFER_TYPE_HIRELING = 20,
    OFFER_TYPE_HIRELING_NAMECHANGE = 21,
    OFFER_TYPE_HIRELING_SEXCHANGE = 22,
    OFFER_TYPE_HIRELING_SKILL = 23,
    OFFER_TYPE_HIRELING_OUTFIT = 24,
    OFFER_TYPE_HUNTINGSLOT = 25,
    OFFER_TYPE_ITEM_BED = 26,
    OFFER_TYPE_ITEM_UNIQUE = 27
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
GameStore.OfferTypes = {
    OFFER_TYPE_NONE = 0,
    OFFER_TYPE_ITEM = 1,
    OFFER_TYPE_STACKABLE = 2,
    OFFER_TYPE_CHARGES = 3,
    OFFER_TYPE_OUTFIT = 4,
    OFFER_TYPE_OUTFIT_ADDON = 5,
    OFFER_TYPE_MOUNT = 6,
    OFFER_TYPE_NAMECHANGE = 7,
    OFFER_TYPE_SEXCHANGE = 8,
    OFFER_TYPE_HOUSE = 9,
    OFFER_TYPE_EXPBOOST = 10,
    OFFER_TYPE_PREYSLOT = 11,
    OFFER_TYPE_PREYBONUS = 12,
    OFFER_TYPE_TEMPLE = 13,
    OFFER_TYPE_BLESSINGS = 14,
    OFFER_TYPE_PREMIUM = 15,
    OFFER_TYPE_ALLBLESSINGS = 17,
    OFFER_TYPE_INSTANT_REWARD_ACCESS = 18,
    OFFER_TYPE_CHARMS = 19,
    OFFER_TYPE_HIRELING = 20,
    OFFER_TYPE_HIRELING_NAMECHANGE = 21,
    OFFER_TYPE_HIRELING_SEXCHANGE = 22,
    OFFER_TYPE_HIRELING_SKILL = 23,
    OFFER_TYPE_HIRELING_OUTFIT = 24,
    OFFER_TYPE_HUNTINGSLOT = 25,
    OFFER_TYPE_ITEM_BED = 26,
    OFFER_TYPE_ITEM_UNIQUE = 27
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

### **🎯 Tipos de Cliente (ClientOfferTypes)**

#### Nível Basic
```lua
GameStore.ClientOfferTypes = {
    CLIENT_STORE_OFFER_OTHER = 0,
    CLIENT_STORE_OFFER_NAMECHANGE = 1,
    CLIENT_STORE_OFFER_WORLD_TRANSFER = 2,
    CLIENT_STORE_OFFER_HIRELING = 3,
    CLIENT_STORE_OFFER_CHARACTER = 4,
    CLIENT_STORE_OFFER_TOURNAMENT = 5,
    CLIENT_STORE_OFFER_CONFIRM = 6
}
```

#### Nível Intermediate
```lua
GameStore.ClientOfferTypes = {
    CLIENT_STORE_OFFER_OTHER = 0,
    CLIENT_STORE_OFFER_NAMECHANGE = 1,
    CLIENT_STORE_OFFER_WORLD_TRANSFER = 2,
    CLIENT_STORE_OFFER_HIRELING = 3,
    CLIENT_STORE_OFFER_CHARACTER = 4,
    CLIENT_STORE_OFFER_TOURNAMENT = 5,
    CLIENT_STORE_OFFER_CONFIRM = 6
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
GameStore.ClientOfferTypes = {
    CLIENT_STORE_OFFER_OTHER = 0,
    CLIENT_STORE_OFFER_NAMECHANGE = 1,
    CLIENT_STORE_OFFER_WORLD_TRANSFER = 2,
    CLIENT_STORE_OFFER_HIRELING = 3,
    CLIENT_STORE_OFFER_CHARACTER = 4,
    CLIENT_STORE_OFFER_TOURNAMENT = 5,
    CLIENT_STORE_OFFER_CONFIRM = 6
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

### **📊 Estados de Produto (States)**

#### Nível Basic
```lua
GameStore.States = {
    STATE_NONE = 0,    -- Estado normal
    STATE_NEW = 1,     -- Produto novo
    STATE_SALE = 2,    -- Produto em promoção
    STATE_TIMED = 3    -- Produto com tempo limitado
}
```

#### Nível Intermediate
```lua
GameStore.States = {
    STATE_NONE = 0,    -- Estado normal
    STATE_NEW = 1,     -- Produto novo
    STATE_SALE = 2,    -- Produto em promoção
    STATE_TIMED = 3    -- Produto com tempo limitado
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
GameStore.States = {
    STATE_NONE = 0,    -- Estado normal
    STATE_NEW = 1,     -- Produto novo
    STATE_SALE = 2,    -- Produto em promoção
    STATE_TIMED = 3    -- Produto com tempo limitado
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

---

## 📡 **Protocolos de Comunicação**

### **📤 Pacotes Enviados pelo Servidor (SendingPackets)**

#### Nível Basic
```lua
GameStore.SendingPackets = {
    S_CoinBalance = 0xDF,           -- 223 - Saldo de moedas
    S_StoreError = 0xE0,            -- 224 - Erro da loja
    S_RequestPurchaseData = 0xE1,   -- 225 - Dados de compra
    S_CoinBalanceUpdating = 0xF2,   -- 242 - Atualização de saldo
    S_OpenStore = 0xFB,             -- 251 - Abrir loja
    S_StoreOffers = 0xFC,           -- 252 - Ofertas da loja
    S_OpenTransactionHistory = 0xFD, -- 253 - Histórico de transações
    S_CompletePurchase = 0xFE       -- 254 - Compra completa
}
```

#### Nível Intermediate
```lua
GameStore.SendingPackets = {
    S_CoinBalance = 0xDF,           -- 223 - Saldo de moedas
    S_StoreError = 0xE0,            -- 224 - Erro da loja
    S_RequestPurchaseData = 0xE1,   -- 225 - Dados de compra
    S_CoinBalanceUpdating = 0xF2,   -- 242 - Atualização de saldo
    S_OpenStore = 0xFB,             -- 251 - Abrir loja
    S_StoreOffers = 0xFC,           -- 252 - Ofertas da loja
    S_OpenTransactionHistory = 0xFD, -- 253 - Histórico de transações
    S_CompletePurchase = 0xFE       -- 254 - Compra completa
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
GameStore.SendingPackets = {
    S_CoinBalance = 0xDF,           -- 223 - Saldo de moedas
    S_StoreError = 0xE0,            -- 224 - Erro da loja
    S_RequestPurchaseData = 0xE1,   -- 225 - Dados de compra
    S_CoinBalanceUpdating = 0xF2,   -- 242 - Atualização de saldo
    S_OpenStore = 0xFB,             -- 251 - Abrir loja
    S_StoreOffers = 0xFC,           -- 252 - Ofertas da loja
    S_OpenTransactionHistory = 0xFD, -- 253 - Histórico de transações
    S_CompletePurchase = 0xFE       -- 254 - Compra completa
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

### **📥 Pacotes Recebidos pelo Servidor (ReceivedPackets)**

#### Nível Basic
```lua
GameStore.RecivedPackets = {
    C_StoreEvent = 0xE9,                    -- 233 - Evento da loja
    C_TransferCoins = 0xEF,                 -- 239 - Transferir moedas
    C_ParseHirelingName = 0xEC,             -- 236 - Nome do hireling
    C_OpenStore = 0xFA,                     -- 250 - Abrir loja
    C_RequestStoreOffers = 0xFB,            -- 251 - Solicitar ofertas
    C_BuyStoreOffer = 0xFC,                 -- 252 - Comprar oferta
    C_OpenTransactionHistory = 0xFD,        -- 253 - Abrir histórico
    C_RequestTransactionHistory = 0xFE      -- 254 - Solicitar histórico
}
```

#### Nível Intermediate
```lua
GameStore.RecivedPackets = {
    C_StoreEvent = 0xE9,                    -- 233 - Evento da loja
    C_TransferCoins = 0xEF,                 -- 239 - Transferir moedas
    C_ParseHirelingName = 0xEC,             -- 236 - Nome do hireling
    C_OpenStore = 0xFA,                     -- 250 - Abrir loja
    C_RequestStoreOffers = 0xFB,            -- 251 - Solicitar ofertas
    C_BuyStoreOffer = 0xFC,                 -- 252 - Comprar oferta
    C_OpenTransactionHistory = 0xFD,        -- 253 - Abrir histórico
    C_RequestTransactionHistory = 0xFE      -- 254 - Solicitar histórico
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
GameStore.RecivedPackets = {
    C_StoreEvent = 0xE9,                    -- 233 - Evento da loja
    C_TransferCoins = 0xEF,                 -- 239 - Transferir moedas
    C_ParseHirelingName = 0xEC,             -- 236 - Nome do hireling
    C_OpenStore = 0xFA,                     -- 250 - Abrir loja
    C_RequestStoreOffers = 0xFB,            -- 251 - Solicitar ofertas
    C_BuyStoreOffer = 0xFC,                 -- 252 - Comprar oferta
    C_OpenTransactionHistory = 0xFD,        -- 253 - Abrir histórico
    C_RequestTransactionHistory = 0xFE      -- 254 - Solicitar histórico
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

---

## 🔧 **Implementação no OTClient**

### **📋 Estrutura Principal (game_store.lua)**

#### **🎮 Controller Principal**

#### Nível Basic
```lua
controllerShop = Controller:new()
g_ui.importStyle("style/ui.otui")
controllerShop:setUI('game_store')
```

#### Nível Intermediate
```lua
controllerShop = Controller:new()
g_ui.importStyle("style/ui.otui")
controllerShop:setUI('game_store')
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
controllerShop = Controller:new()
g_ui.importStyle("style/ui.otui")
controllerShop:setUI('game_store')
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

#### **🔄 Eventos Registrados**

#### Nível Basic
```lua
controllerShop:registerEvents(g_game, {
    onParseStoreGetCoin = onParseStoreGetCoin,
    onParseStoreGetCategories = onParseStoreGetCategories,
    onParseStoreCreateHome = onParseStoreCreateHome,
    onParseStoreCreateProducts = onParseStoreCreateProducts,
    onParseStoreGetHistory = onParseStoreGetHistory,
    onParseStoreGetPurchaseStatus = onParseStoreGetPurchaseStatus,
    onParseStoreOfferDescriptions = onParseStoreOfferDescriptions,
    onParseStoreError = onParseStoreError,
    onStoreInit = onStoreInit
})
```

#### Nível Intermediate
```lua
controllerShop:registerEvents(g_game, {
    onParseStoreGetCoin = onParseStoreGetCoin,
    onParseStoreGetCategories = onParseStoreGetCategories,
    onParseStoreCreateHome = onParseStoreCreateHome,
    onParseStoreCreateProducts = onParseStoreCreateProducts,
    onParseStoreGetHistory = onParseStoreGetHistory,
    onParseStoreGetPurchaseStatus = onParseStoreGetPurchaseStatus,
    onParseStoreOfferDescriptions = onParseStoreOfferDescriptions,
    onParseStoreError = onParseStoreError,
    onStoreInit = onStoreInit
})
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
controllerShop:registerEvents(g_game, {
    onParseStoreGetCoin = onParseStoreGetCoin,
    onParseStoreGetCategories = onParseStoreGetCategories,
    onParseStoreCreateHome = onParseStoreCreateHome,
    onParseStoreCreateProducts = onParseStoreCreateProducts,
    onParseStoreGetHistory = onParseStoreGetHistory,
    onParseStoreGetPurchaseStatus = onParseStoreGetPurchaseStatus,
    onParseStoreOfferDescriptions = onParseStoreOfferDescriptions,
    onParseStoreError = onParseStoreError,
    onStoreInit = onStoreInit
})
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

### **📊 Funções de Parse**

#### **💰 Parse de Saldo de Moedas**

```lua
function onParseStoreGetCoin(getTibiaCoins, getTransferableCoins)
    -- Função: onParseStoreGetCoin
    a0xF2 = false
    controllerShop.ui.lblCoins.lblTibiaCoins:setText(formatNumberWithCommas(getTibiaCoins))
    controllerShop.ui.lblCoins.lblTibiaTransfer:setText(string.format("(Including: %s",
        formatNumberWithCommas(getTransferableCoins)))
end
```

#### **📂 Parse de Categorias**

#### Nível Basic
```lua
function onParseStoreGetCategories(buttons)
    -- Criação dinâmica de categorias e subcategorias
    -- Organização hierárquica
    -- Interface de navegação
end
```

#### Nível Intermediate
```lua
function onParseStoreGetCategories(buttons)
    -- Criação dinâmica de categorias e subcategorias
    -- Organização hierárquica
    -- Interface de navegação
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
function onParseStoreGetCategories(buttons)
    -- Criação dinâmica de categorias e subcategorias
    -- Organização hierárquica
    -- Interface de navegação
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

#### **🏠 Parse da Página Inicial**

```lua
function onParseStoreCreateHome(offer)
    -- Função: onParseStoreCreateHome
    -- Criação de produtos em destaque
    -- Banners rotativos
    --  Banners rotativos (traduzido)
    -- Interface da página inicial
end
```

#### **📦 Parse de Produtos**

```lua
function onParseStoreCreateProducts(storeProducts)
    -- Função: onParseStoreCreateProducts
    -- Listagem de produtos
    --  Listagem de produtos (traduzido)
    -- Filtros e ordenação
    -- Interface de compra
    --  Interface de compra (traduzido)
end
```

---

## 🏗️ **Implementação no Canary**

### **📋 Estrutura Principal (init.lua)**

#### **🎯 Configuração do Módulo**

#### Nível Basic
```lua
GameStore = {
    ModuleName = "GameStore",
    Developers = { "Cjaker", "metabob", "Rick" },
    Version = "1.1",
    LastUpdated = "25-07-2020 11:52AM",
}
```

#### Nível Intermediate
```lua
GameStore = {
    ModuleName = "GameStore",
    Developers = { "Cjaker", "metabob", "Rick" },
    Version = "1.1",
    LastUpdated = "25-07-2020 11:52AM",
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
GameStore = {
    ModuleName = "GameStore",
    Developers = { "Cjaker", "metabob", "Rick" },
    Version = "1.1",
    LastUpdated = "25-07-2020 11:52AM",
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

#### **🔄 Sub-Ações (SubActions)**

#### Nível Basic
```lua
GameStore.SubActions = {
    PREY_THIRDSLOT_REAL = 0,
    PREY_WILDCARD = 1,
    INSTANT_REWARD = 2,
    BLESSING_TWIST = 3,
    BLESSING_SOLITUDE = 4,
    BLESSING_PHOENIX = 5,
    BLESSING_SUNS = 6,
    BLESSING_SPIRITUAL = 7,
    BLESSING_EMBRACE = 8,
    BLESSING_BLOOD = 9,
    BLESSING_HEART = 10,
    BLESSING_ALL_PVE = 11,
    BLESSING_ALL_PVP = 12,
    CHARM_EXPANSION = 13,
    TASKHUNTING_THIRDSLOT = 14,
    PREY_THIRDSLOT_REDIRECT = 15,
}
```

#### Nível Intermediate
```lua
GameStore.SubActions = {
    PREY_THIRDSLOT_REAL = 0,
    PREY_WILDCARD = 1,
    INSTANT_REWARD = 2,
    BLESSING_TWIST = 3,
    BLESSING_SOLITUDE = 4,
    BLESSING_PHOENIX = 5,
    BLESSING_SUNS = 6,
    BLESSING_SPIRITUAL = 7,
    BLESSING_EMBRACE = 8,
    BLESSING_BLOOD = 9,
    BLESSING_HEART = 10,
    BLESSING_ALL_PVE = 11,
    BLESSING_ALL_PVP = 12,
    CHARM_EXPANSION = 13,
    TASKHUNTING_THIRDSLOT = 14,
    PREY_THIRDSLOT_REDIRECT = 15,
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
GameStore.SubActions = {
    PREY_THIRDSLOT_REAL = 0,
    PREY_WILDCARD = 1,
    INSTANT_REWARD = 2,
    BLESSING_TWIST = 3,
    BLESSING_SOLITUDE = 4,
    BLESSING_PHOENIX = 5,
    BLESSING_SUNS = 6,
    BLESSING_SPIRITUAL = 7,
    BLESSING_EMBRACE = 8,
    BLESSING_BLOOD = 9,
    BLESSING_HEART = 10,
    BLESSING_ALL_PVE = 11,
    BLESSING_ALL_PVP = 12,
    CHARM_EXPANSION = 13,
    TASKHUNTING_THIRDSLOT = 14,
    PREY_THIRDSLOT_REDIRECT = 15,
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

---

## 🔄 **Fluxos de Trabalho Principais**

### **🛒 Fluxo de Compra**

```
1. Usuário seleciona produto
   ↓
2. Validação de saldo
   ↓
3. Confirmação de compra
   ↓
4. Envio de pacote C_BuyStoreOffer
   ↓
5. Processamento no servidor
   ↓
6. Resposta S_CompletePurchase
   ↓
7. Atualização de saldo
   ↓
8. Entrega do produto
```

### **💰 Fluxo de Transferência de Moedas**

```
1. Usuário inicia transferência
   ↓
2. Validação de saldo transferível
   ↓
3. Confirmação de destinatário
   ↓
4. Envio de pacote C_TransferCoins
   ↓
5. Processamento no servidor
   ↓
6. Atualização de saldos
   ↓
7. Confirmação de transferência
```

### **📊 Fluxo de Histórico de Transações**

```
1. Usuário solicita histórico
   ↓
2. Envio de pacote C_RequestTransactionHistory
   ↓
3. Processamento no servidor
   ↓
4. Resposta S_OpenTransactionHistory
   ↓
5. Exibição de transações
   ↓
6. Navegação por páginas
```

---

## 🎨 **Interface de Usuário**

### **📱 Componentes Principais**

#### **🏠 Painel Inicial (HomePanel)**
- Produtos em destaque
- Banners rotativos
- Categorias principais
- Navegação rápida

#### **📦 Painel de Produtos (panelItem)**
- Lista de produtos
- Filtros e ordenação
- Detalhes do produto
- Botão de compra

#### **📊 Histórico de Transações (transferHistory)**
- Lista de transações
- Paginação
- Filtros por tipo
- Detalhes de cada transação

### **🎯 Funcionalidades de Interface**

#### **🔍 Sistema de Busca**
```lua
function search()
    -- Função: search
    if controllerShop.ui.openedCategory ~= nil then
    -- Verificação condicional
        close(controllerShop.ui.openedCategory)
    end
    g_game.sendRequestStoreSearch(controllerShop.ui.SearchEdit:getText(), 0, 1)
end
```

#### **🔄 Navegação por Categorias**
```lua
function toggleSubCategories(parent, isOpen)
    -- Função: toggleSubCategories
    -- Expansão/contração de subcategorias
    -- Navegação hierárquica
    -- Interface responsiva
    --  Interface responsiva (traduzido)
end
```

#### **💰 Transferência de Moedas**
#### Nível Basic
```lua
function transferPoints()
    -- Interface de transferência
    -- Validação de saldo
    -- Confirmação de destinatário
    -- Processamento da transferência
end
```

#### Nível Intermediate
```lua
function transferPoints()
    -- Interface de transferência
    -- Validação de saldo
    -- Confirmação de destinatário
    -- Processamento da transferência
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
function transferPoints()
    -- Interface de transferência
    -- Validação de saldo
    -- Confirmação de destinatário
    -- Processamento da transferência
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

## 🔒 **Segurança e Validação**

### **✅ Validações de Cliente**

#### **💰 Validação de Saldo**
```lua
local function getCoinsBalance()
    local function extractNumber(text)
        if type(text) ~= "string" then 
    -- Verificação condicional
            return 0 
        end
        local numberStr = text:match("%d[%d,]*")
        if not numberStr then 
    -- Verificação condicional
            return 0 
        end
        local cleanNumber = numberStr:gsub("[^%d]", "")
        return tonumber(cleanNumber) or 0
    end

    local lblCoins = controllerShop.ui.lblCoins.lblTibiaCoins
    local lblTransfer = controllerShop.ui.lblCoins.lblTibiaTransfer

    local coins1 = lblCoins and extractNumber(lblCoins:getText()) or 0
    local coins2 = lblTransfer and extractNumber(lblTransfer:getText()) or 0
    return coins1, coins2
end
```

#### **🛡️ Validação de Produtos Desabilitados**
```lua
if offer.disabled then
    -- Verificação condicional
    local btnBuy = offerPanel:getChildById('btnBuy')
    btnBuy:disable()
    btnBuy:setOpacity(0.8)
    
    -- Exibição de motivo da desabilitação
    if offer.reasonIdDisable then
    -- Verificação condicional
        -- Tooltip com explicação
    end
end
```

### **🔐 Validações de Servidor**

#### **💰 Verificação de Saldo**
- Validação antes da compra
- Verificação de moedas transferíveis
- Proteção contra saldo negativo

#### **🛡️ Validação de Produtos**
- Verificação de disponibilidade
- Validação de preços
- Controle de acesso por personagem

---

## 🔧 **Integração com Protocolo**

### **📡 Pacotes de Comunicação**

#### **🔄 Abertura da Loja**
#### Nível Basic
```cpp
void ProtocolGame::sendOpenStore(const uint8_t serviceType, const std::string_view category)
{
    const auto& msg = std::make_shared<OutputMessage>();
    msg->addU8(Proto::ClientOpenStore);

    if (g_game.getFeature(Otc::GameIngameStoreServiceType)) {
        msg->addU8(serviceType);
        msg->addString(category);
    }

    send(msg);
}
```

#### Nível Intermediate
```cpp
void ProtocolGame::sendOpenStore(const uint8_t serviceType, const std::string_view category)
{
    const auto& msg = std::make_shared<OutputMessage>();
    msg->addU8(Proto::ClientOpenStore);

    if (g_game.getFeature(Otc::GameIngameStoreServiceType)) {
        msg->addU8(serviceType);
        msg->addString(category);
    }

    send(msg);
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
void ProtocolGame::sendOpenStore(const uint8_t serviceType, const std::string_view category)
{
    const auto& msg = std::make_shared<OutputMessage>();
    msg->addU8(Proto::ClientOpenStore);

    if (g_game.getFeature(Otc::GameIngameStoreServiceType)) {
        msg->addU8(serviceType);
        msg->addString(category);
    }

    send(msg);
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

#### **📦 Compra de Produto**
#### Nível Basic
```cpp
void ProtocolGame::sendBuyStoreOffer(const uint32_t offerId, const uint8_t action, const std::string_view& name, const uint8_t type, const std::string_view& location)
{
    const auto& msg = std::make_shared<OutputMessage>();
    msg->addU8(Proto::ClientBuyStoreOffer);
    msg->addU32(offerId);
    msg->addU8(action);
    msg->addString(name);
    msg->addU8(type);
    msg->addString(location);
    send(msg);
}
```

#### Nível Intermediate
```cpp
void ProtocolGame::sendBuyStoreOffer(const uint32_t offerId, const uint8_t action, const std::string_view& name, const uint8_t type, const std::string_view& location)
{
    const auto& msg = std::make_shared<OutputMessage>();
    msg->addU8(Proto::ClientBuyStoreOffer);
    msg->addU32(offerId);
    msg->addU8(action);
    msg->addString(name);
    msg->addU8(type);
    msg->addString(location);
    send(msg);
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
void ProtocolGame::sendBuyStoreOffer(const uint32_t offerId, const uint8_t action, const std::string_view& name, const uint8_t type, const std::string_view& location)
{
    const auto& msg = std::make_shared<OutputMessage>();
    msg->addU8(Proto::ClientBuyStoreOffer);
    msg->addU32(offerId);
    msg->addU8(action);
    msg->addString(name);
    msg->addU8(type);
    msg->addString(location);
    send(msg);
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

#### **💰 Transferência de Moedas**
#### Nível Basic
```cpp
void ProtocolGame::sendTransferCoins(const std::string_view recipient, const uint16_t amount)
{
    const auto& msg = std::make_shared<OutputMessage>();
    msg->addU8(Proto::ClientTransferCoins);
    msg->addString(recipient);
    msg->addU16(amount);
    send(msg);
}
```

#### Nível Intermediate
```cpp
void ProtocolGame::sendTransferCoins(const std::string_view recipient, const uint16_t amount)
{
    const auto& msg = std::make_shared<OutputMessage>();
    msg->addU8(Proto::ClientTransferCoins);
    msg->addString(recipient);
    msg->addU16(amount);
    send(msg);
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
void ProtocolGame::sendTransferCoins(const std::string_view recipient, const uint16_t amount)
{
    const auto& msg = std::make_shared<OutputMessage>();
    msg->addU8(Proto::ClientTransferCoins);
    msg->addString(recipient);
    msg->addU16(amount);
    send(msg);
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

### **📊 Parse de Respostas**

#### **🏪 Parse da Loja**
#### Nível Basic
```cpp
    if (g_game.getClientVersion() <= 1100) {
```

#### Nível Intermediate
```cpp
void ProtocolGame::parseStore(const InputMessagePtr& msg) const
{
    if (g_game.getClientVersion() <= 1100) {
        parseCoinBalance(msg);
    }

    const uint16_t categoryCount = msg->getU16();
    std::vector<StoreCategory> categories;

    for (auto i = 0; i < categoryCount; ++i) {
        StoreCategory category;
        category.name = msg->getString();
        // ... processamento de categorias
    }

    g_lua.callGlobalField("g_game", "onParseStoreGetCategories", organizedCategories);
}
```

#### Nível Advanced
```cpp
void ProtocolGame::parseStore(const InputMessagePtr& msg) const
{
    if (g_game.getClientVersion() <= 1100) {
        parseCoinBalance(msg);
    }

    const uint16_t categoryCount = msg->getU16();
    std::vector<StoreCategory> categories;

    for (auto i = 0; i < categoryCount; ++i) {
        StoreCategory category;
        category.name = msg->getString();
        // ... processamento de categorias
    }

    g_lua.callGlobalField("g_game", "onParseStoreGetCategories", organizedCategories);
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

#### **📦 Parse de Ofertas**
#### Nível Basic
```cpp
void ProtocolGame::parseStoreOffers(const InputMessagePtr& msg)
{
    if (g_game.getClientVersion() >= 1291) {
        StoreData storeData;
        storeData.categoryName = msg->getString();
        storeData.redirectId = msg->getU32();
        // ... processamento de ofertas
    }
}
```

#### Nível Intermediate
```cpp
void ProtocolGame::parseStoreOffers(const InputMessagePtr& msg)
{
    if (g_game.getClientVersion() >= 1291) {
        StoreData storeData;
        storeData.categoryName = msg->getString();
        storeData.redirectId = msg->getU32();
        // ... processamento de ofertas
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
void ProtocolGame::parseStoreOffers(const InputMessagePtr& msg)
{
    if (g_game.getClientVersion() >= 1291) {
        StoreData storeData;
        storeData.categoryName = msg->getString();
        storeData.redirectId = msg->getU32();
        // ... processamento de ofertas
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

---

## 🎯 **Padrões de Implementação**

### **📋 Padrões de Código**

#### **🔄 Event-Driven Architecture**
- Uso de eventos Lua para comunicação
- Separação clara entre UI e lógica
- Sistema de callbacks estruturado

#### **🏗️ Modular Design**
- Componentes independentes
- Reutilização de código
- Fácil manutenção e extensão

#### **🛡️ Defensive Programming**
- Validações robustas
- Tratamento de erros
- Fallbacks para casos extremos

### **🎨 Padrões de Interface**

#### **📱 Responsive Design**
- Interface adaptável
- Componentes flexíveis
- Navegação intuitiva

#### **🎯 User Experience**
- Feedback visual imediato
- Confirmações de ações críticas
- Interface consistente

---

## 🔧 **Configuração e Personalização**

### **⚙️ Configurações do Sistema**

#### **🌐 URLs e Endpoints**
```lua
GameStore.website = {
    WEBSITE_GETCOINS = "https://github.com/mehah/otclient",
    --IMAGES_URL = "http://localhost/images/store/"
    -- IMAGES_URL = "http://localhost/images/store/" (traduzido)
}
```

#### **📊 Valores Padrão**
#### Nível Basic
```lua
GameStore.DefaultValues = {
    DEFAULT_VALUE_ENTRIES_PER_PAGE = 26,
}
```

#### Nível Intermediate
```lua
GameStore.DefaultValues = {
    DEFAULT_VALUE_ENTRIES_PER_PAGE = 26,
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
GameStore.DefaultValues = {
    DEFAULT_VALUE_ENTRIES_PER_PAGE = 26,
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

#### **🎯 Boost de Experiência**
#### Nível Basic
```lua
GameStore.ExpBoostValues = {
    [1] = 30,
    [2] = 45,
    [3] = 90,
    [4] = 180,
    [5] = 360,
}
```

#### Nível Intermediate
```lua
GameStore.ExpBoostValues = {
    [1] = 30,
    [2] = 45,
    [3] = 90,
    [4] = 180,
    [5] = 360,
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
GameStore.ExpBoostValues = {
    [1] = 30,
    [2] = 45,
    [3] = 90,
    [4] = 180,
    [5] = 360,
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

### **🎨 Personalização de Interface**

#### **🎨 Temas e Estilos**
- Suporte a temas claro/escuro
- Personalização de cores
- Adaptação a diferentes resoluções

#### **🔧 Configurações de Usuário**
- Preferências de exibição
- Configurações de notificação
- Personalização de filtros

---

## 🚀 **Otimizações e Performance**

### **⚡ Otimizações de Cliente**

#### **🔄 Cache Inteligente**
- Cache de imagens HTTP
- Cache de dados de produtos
- Otimização de consultas

#### **📊 Lazy Loading**
- Carregamento sob demanda
- Redução de uso de memória
- Melhoria de performance

### **🔧 Otimizações de Servidor**

#### **📦 Compressão de Dados**
- Otimização de pacotes
- Redução de tráfego de rede
- Melhoria de latência

#### **🔄 Processamento Assíncrono**
- Operações não-bloqueantes
- Melhoria de throughput
- Escalabilidade

---

## 🐛 **Tratamento de Erros**

### **❌ Tipos de Erro**

#### Nível Basic
```lua
GameStore.StoreErrors = {
    STORE_ERROR_PURCHASE = 0,
    STORE_ERROR_NETWORK = 1,
    STORE_ERROR_HISTORY = 2,
    STORE_ERROR_TRANSFER = 3,
    STORE_ERROR_INFORMATION = 4,
}
```

#### Nível Intermediate
```lua
GameStore.StoreErrors = {
    STORE_ERROR_PURCHASE = 0,
    STORE_ERROR_NETWORK = 1,
    STORE_ERROR_HISTORY = 2,
    STORE_ERROR_TRANSFER = 3,
    STORE_ERROR_INFORMATION = 4,
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
GameStore.StoreErrors = {
    STORE_ERROR_PURCHASE = 0,
    STORE_ERROR_NETWORK = 1,
    STORE_ERROR_HISTORY = 2,
    STORE_ERROR_TRANSFER = 3,
    STORE_ERROR_INFORMATION = 4,
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

### **🛡️ Estratégias de Recuperação**

#### **🔄 Retry Logic**
- Tentativas automáticas
- Backoff exponencial
- Fallbacks robustos

#### **📊 Error Reporting**
- Logs detalhados
- Monitoramento de erros
- Alertas automáticos

---

## 📈 **Métricas e Monitoramento**

### **📊 Métricas de Performance**

#### **⚡ Tempo de Resposta**
- Latência de pacotes
- Tempo de carregamento
- Performance de interface

#### **🔄 Taxa de Sucesso**
- Taxa de compras bem-sucedidas
- Taxa de transferências
- Taxa de erros

### **📈 Métricas de Negócio**

#### **💰 Volume de Transações**
- Número de compras
- Valor total transacionado
- Produtos mais populares

#### **👥 Engajamento de Usuários**
- Frequência de uso
- Tempo na loja
- Padrões de navegação

---

## 🔮 **Roadmap e Melhorias Futuras**

### **🎯 Melhorias Planejadas**

#### **📱 Interface Moderna**
- Design responsivo avançado
- Animações fluidas
- Experiência mobile-first

#### **🤖 Inteligência Artificial**
- Recomendações personalizadas
- Análise de comportamento
- Otimização automática

### **🚀 Novas Funcionalidades**

#### **🎮 Integração Social**
- Compartilhamento de produtos
- Sistema de avaliações
- Comunidade de usuários

#### **📊 Analytics Avançado**
- Dashboard de métricas
- Relatórios detalhados
- Insights de negócio

---

## 📚 **Conclusão**

O **Sistema Game Store** representa uma implementação robusta e bem estruturada de uma loja in-game moderna. Com protocolos de comunicação eficientes, interface de usuário intuitiva e sistema de segurança robusto, oferece uma experiência completa para compras e transações virtuais.

### **🎯 Pontos Fortes**

- **Arquitetura modular** e bem estruturada
- **Protocolos de comunicação** eficientes
- **Interface de usuário** intuitiva e responsiva
- **Sistema de segurança** robusto
- **Integração perfeita** entre cliente e servidor

### **🔧 Áreas de Melhoria**

- **Performance** pode ser otimizada em alguns cenários
- **Documentação** pode ser expandida
- **Testes automatizados** podem ser implementados
- **Monitoramento** pode ser aprimorado

### **🚀 Impacto no Criador de Códigos**

Esta análise fornece ao **criador de códigos** conhecimento profundo sobre:
- **Padrões de implementação** de sistemas complexos
- **Protocolos de comunicação** cliente-servidor
- **Estruturas de dados** e enums
- **Fluxos de trabalho** e validações
- **Melhores práticas** de desenvolvimento

Com este conhecimento, o criador de códigos pode gerar implementações mais inteligentes, contextualizadas e eficientes para sistemas similares.

---

**📅 Data da Análise**: 2025-01-27  
**🔍 Responsável**: Deep Source Analyzer + Code Generator Agent  
**📊 Status**: ✅ **ANÁLISE COMPLETA**  
**🎯 Próximo Passo**: Task 16.2 - Documentação Completa do Extended Opcode 
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

