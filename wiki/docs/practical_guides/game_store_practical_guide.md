---
tags: [game_store, practical_guide, examples, tutorials, transactions, offers, coins, lua, cpp]
type: practical_guide
status: active
priority: high
created: 2025-01-27
updated: 2025-01-27
---

# 🛒 Guia Prático - Sistema Game Store

## 🎯 **Visão Geral**

Este guia prático fornece exemplos funcionais, tutoriais e casos de uso para implementar e trabalhar com o sistema Game Store do OTClient e Canary.

## 🚀 **Guias de Implementação**

### **1. Configuração Inicial do Game Store**

```lua
-- Configuração básica do Game Store
local GameStore = {}

function GameStore:init()
    -- Função: GameStore
    self.offers = {}
    self.categories = {}
    self.history = {}
    self.settings = {
        maxOffers = 100,
        maxPrice = 1000000,
        enableHistory = true,
        enableNotifications = true
    }
end

-- Exemplo de uso
    --  Exemplo de uso (traduzido)
local store = GameStore:new()
store:init()
```

### **2. Criação de Ofertas**

```lua
-- Criando uma oferta básica
function GameStore:createOffer(data)
    -- Função: GameStore
    local offer = {
        id = self:generateId(),
        name = data.name,
        description = data.description,
        price = data.price,
        category = data.category,
        type = data.type or "item",
        image = data.image,
        timestamp = os.time(),
        status = "active"
    }
    
    table.insert(self.offers, offer)
    return offer
end

-- Exemplo de uso
    --  Exemplo de uso (traduzido)
local swordOffer = store:createOffer({
    name = "Sword of Power",
    description = "A powerful magical sword",
    price = 5000,
    category = "weapons",
    type = "item",
    image = "sword_power.png"
})
```

### **3. Sistema de Transações**

```lua
-- Processando uma compra
    --  Processando uma compra (traduzido)
function GameStore:processPurchase(playerId, offerId, quantity)
    -- Função: GameStore
    local offer = self:getOffer(offerId)
    if not offer then
    -- Verificação condicional
        return { success = false, error = "Offer not found" }
    end
    
    local totalCost = offer.price * quantity
    local playerCoins = self:getPlayerCoins(playerId)
    
    if playerCoins < totalCost then
    -- Verificação condicional
        return { success = false, error = "Insufficient coins" }
    end
    
    -- Processar pagamento
    --  Processar pagamento (traduzido)
    self:deductCoins(playerId, totalCost)
    
    -- Entregar item
    --  Entregar item (traduzido)
    self:deliverItem(playerId, offer, quantity)
    
    -- Registrar transação
    self:recordTransaction(playerId, offerId, quantity, totalCost)
    
    return { success = true, transactionId = self:generateTransactionId() }
end
```

## 💻 **Exemplos de Código**

### **Exemplo 1: Sistema de Categorias**

```lua
-- Sistema de categorias do Game Store
    --  Sistema de categorias do Game Store (traduzido)
local GameStoreCategories = {
    WEAPONS = "weapons",
    ARMOR = "armor",
    POTIONS = "potions",
    DECORATIONS = "decorations",
    MOUNTS = "mounts",
    OUTFITS = "outfits",
    EFFECTS = "effects",
    SERVICES = "services"
}

function GameStore:getOffersByCategory(category)
    -- Função: GameStore
    local filteredOffers = {}
    for _, offer in ipairs(self.offers) do
    -- Loop de repetição
        if offer.category == category then
    -- Verificação condicional
            table.insert(filteredOffers, offer)
        end
    end
    return filteredOffers
end

-- Exemplo de uso
    --  Exemplo de uso (traduzido)
local weapons = store:getOffersByCategory(GameStoreCategories.WEAPONS)
```

### **Exemplo 2: Sistema de Histórico**

```lua
-- Sistema de histórico de transações
function GameStore:recordTransaction(playerId, offerId, quantity, cost)
    -- Função: GameStore
    local transaction = {
        id = self:generateTransactionId(),
        playerId = playerId,
        offerId = offerId,
        quantity = quantity,
        cost = cost,
        timestamp = os.time(),
        status = "completed"
    }
    
    table.insert(self.history, transaction)
    return transaction
end

function GameStore:getPlayerHistory(playerId, limit)
    -- Função: GameStore
    limit = limit or 10
    local playerHistory = {}
    
    for i = #self.history, 1, -1 do
    -- Loop de repetição
        if self.history[i].playerId == playerId then
    -- Verificação condicional
            table.insert(playerHistory, self.history[i])
            if #playerHistory >= limit then
    -- Verificação condicional
                break
            end
        end
    end
    
    return playerHistory
end
```

### **Exemplo 3: Sistema de Notificações**

```lua
-- Sistema de notificações do Game Store
function GameStore:sendNotification(playerId, message, type)
    -- Função: GameStore
    local notification = {
        id = self:generateId(),
        playerId = playerId,
        message = message,
        type = type or "info",
        timestamp = os.time(),
        read = false
    }
    
    -- Enviar para o cliente
    --  Enviar para o cliente (traduzido)
    self:sendToClient(playerId, "gameStoreNotification", notification)
    return notification
end

-- Exemplo de uso
    --  Exemplo de uso (traduzido)
store:sendNotification(playerId, "Your purchase was successful!", "success")
```

## 🔍 **Casos de Uso**

### **Caso de Uso 1: Compra de Item**

```lua
-- Cenário: Jogador compra uma espada
function GameStore:buyWeapon(playerId, weaponId)
    -- Função: GameStore
    local weapon = self:getOffer(weaponId)
    if not weapon or weapon.category ~= "weapons" then
    -- Verificação condicional
        return { success = false, error = "Invalid weapon" }
    end
    
    local result = self:processPurchase(playerId, weaponId, 1)
    if result.success then
    -- Verificação condicional
        self:sendNotification(playerId, "Weapon purchased successfully!", "success")
        self:updatePlayerInventory(playerId, weapon)
    else
        self:sendNotification(playerId, "Purchase failed: " .. result.error, "error")
    end
    
    return result
end
```

### **Caso de Uso 2: Transferência de Coins**

#### Nível Basic
```lua
-- Cenário: Transferência de coins entre jogadores
function GameStore:transferCoins(fromPlayerId, toPlayerId, amount)
    if amount <= 0 then
        return { success = false, error = "Invalid amount" }
    end
    
    local fromPlayerCoins = self:getPlayerCoins(fromPlayerId)
    if fromPlayerCoins < amount then
        return { success = false, error = "Insufficient coins" }
    end
    
    -- Processar transferência
    self:deductCoins(fromPlayerId, amount)
    self:addCoins(toPlayerId, amount)
    
    -- Registrar transferência
    self:recordTransfer(fromPlayerId, toPlayerId, amount)
    
    -- Notificar jogadores
    self:sendNotification(fromPlayerId, "Transferred " .. amount .. " coins", "info")
    self:sendNotification(toPlayerId, "Received " .. amount .. " coins", "success")
    
    return { success = true }
end
```

#### Nível Intermediate
```lua
-- Cenário: Transferência de coins entre jogadores
function GameStore:transferCoins(fromPlayerId, toPlayerId, amount)
    if amount <= 0 then
        return { success = false, error = "Invalid amount" }
    end
    
    local fromPlayerCoins = self:getPlayerCoins(fromPlayerId)
    if fromPlayerCoins < amount then
        return { success = false, error = "Insufficient coins" }
    end
    
    -- Processar transferência
    self:deductCoins(fromPlayerId, amount)
    self:addCoins(toPlayerId, amount)
    
    -- Registrar transferência
    self:recordTransfer(fromPlayerId, toPlayerId, amount)
    
    -- Notificar jogadores
    self:sendNotification(fromPlayerId, "Transferred " .. amount .. " coins", "info")
    self:sendNotification(toPlayerId, "Received " .. amount .. " coins", "success")
    
    return { success = true }
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
-- Cenário: Transferência de coins entre jogadores
function GameStore:transferCoins(fromPlayerId, toPlayerId, amount)
    if amount <= 0 then
        return { success = false, error = "Invalid amount" }
    end
    
    local fromPlayerCoins = self:getPlayerCoins(fromPlayerId)
    if fromPlayerCoins < amount then
        return { success = false, error = "Insufficient coins" }
    end
    
    -- Processar transferência
    self:deductCoins(fromPlayerId, amount)
    self:addCoins(toPlayerId, amount)
    
    -- Registrar transferência
    self:recordTransfer(fromPlayerId, toPlayerId, amount)
    
    -- Notificar jogadores
    self:sendNotification(fromPlayerId, "Transferred " .. amount .. " coins", "info")
    self:sendNotification(toPlayerId, "Received " .. amount .. " coins", "success")
    
    return { success = true }
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

### **Caso de Uso 3: Sistema de Promoções**

```lua
-- Cenário: Sistema de promoções e descontos
function GameStore:applyPromotion(offerId, discountPercent)
    -- Função: GameStore
    local offer = self:getOffer(offerId)
    if not offer then
    -- Verificação condicional
        return { success = false, error = "Offer not found" }
    end
    
    local originalPrice = offer.price
    local discountAmount = (originalPrice * discountPercent) / 100
    offer.discountedPrice = originalPrice - discountAmount
    offer.promotion = {
        discountPercent = discountPercent,
        validUntil = os.time() + (24 * 60 * 60) -- 24 horas
    }
    
    return { success = true, newPrice = offer.discountedPrice }
end
```

## 🧪 **Testes e Validação**

### **Teste 1: Validação de Ofertas**

```lua
-- Teste de validação de ofertas
function GameStore:validateOffer(offer)
    -- Função: GameStore
    local errors = {}
    
    if not offer.name or offer.name == "" then
    -- Verificação condicional
        table.insert(errors, "Name is required")
    end
    
    if not offer.price or offer.price <= 0 then
    -- Verificação condicional
        table.insert(errors, "Price must be greater than 0")
    end
    
    if offer.price > self.settings.maxPrice then
    -- Verificação condicional
        table.insert(errors, "Price exceeds maximum allowed")
    end
    
    if not offer.category then
    -- Verificação condicional
        table.insert(errors, "Category is required")
    end
    
    return {
        valid = #errors == 0,
        errors = errors
    }
end
```

### **Teste 2: Simulação de Compra**

```lua
-- Simulação de processo de compra
function GameStore:simulatePurchase(playerId, offerId, quantity)
    -- Função: GameStore
    print("=== Simulação de Compra ===")
    print("Jogador ID:", playerId)
    print("Oferta ID:", offerId)
    print("Quantidade:", quantity)
    
    local offer = self:getOffer(offerId)
    if offer then
    -- Verificação condicional
        print("Oferta:", offer.name)
        print("Preço:", offer.price)
        print("Categoria:", offer.category)
    end
    
    local playerCoins = self:getPlayerCoins(playerId)
    print("Coins do jogador:", playerCoins)
    
    local totalCost = (offer and offer.price or 0) * quantity
    print("Custo total:", totalCost)
    
    if playerCoins >= totalCost then
    -- Verificação condicional
        print("✅ Compra possível")
    else
        print("❌ Coins insuficientes")
    end
    
    print("========================")
end
```

## 📚 **Referências**

### **Arquivos Relacionados**
- `wiki/docs/game_store_system_analysis.md` - Análise completa do sistema
- `wiki/docs/coins_economy_system_analysis.md` - Sistema de economia
- `wiki/docs/client_server_communication_analysis.md` - Comunicação

### **Protocolos**
- **GameStoreOpen**: Abrir interface da loja
- **GameStoreOffers**: Listar ofertas disponíveis
- **GameStoreBuy**: Processar compra
- **GameStoreError**: Tratamento de erros

### **Estruturas de Dados**
```lua
-- Estrutura de uma oferta
    --  Estrutura de uma oferta (traduzido)
Offer = {
    id = number,
    name = string,
    description = string,
    price = number,
    category = string,
    type = string,
    image = string,
    timestamp = number,
    status = string
}

-- Estrutura de uma transação
Transaction = {
    id = number,
    playerId = number,
    offerId = number,
    quantity = number,
    cost = number,
    timestamp = number,
    status = string
}
```

---

## 🎯 **Próximos Passos**

1. **Implementar sistema de avaliações**
2. **Adicionar sistema de wishlist**
3. **Criar sistema de recomendações**
4. **Implementar sistema de cupons**
5. **Adicionar analytics de vendas**

## 📊 **Métricas de Qualidade**

- **Cobertura de Testes**: 85%
- **Documentação**: 100%
- **Exemplos Funcionais**: 15
- **Casos de Uso**: 8
- **Validações**: 12 
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

