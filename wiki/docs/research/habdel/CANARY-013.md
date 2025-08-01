---
tags: [canary_research, inventory_system, habdel_research, deep_analysis]
type: research_story
status: completed
priority: high
created: 2025-01-27
target: canary
epic: canary_deep_research
story: CANARY-013
---

# CANARY-013: Sistema de Inventário - Pesquisa Habdel

## 🎯 **Objetivo da Pesquisa**

Realizar uma análise profunda e completa do Sistema de Inventário do Canary, mapeando sua arquitetura, componentes, APIs, integrações e implementações práticas. Esta pesquisa visa compreender como o sistema de inventário funciona, suas otimizações, e como se integra com outros sistemas do servidor.

## 📋 **Metodologia Habdel**

### **Fase 1: Descoberta e Mapeamento**
- [x] Identificar arquivos relacionados ao sistema de inventário
- [x] Mapear classes e estruturas principais
- [x] Identificar APIs e interfaces públicas
- [x] Documentar dependências e integrações

### **Fase 2: Análise Profunda**
- [x] Analisar implementação de cada componente
- [x] Documentar algoritmos e lógicas de negócio
- [x] Mapear fluxos de dados e controle
- [x] Identificar otimizações e padrões de design

### **Fase 3: Documentação e Exemplos**
- [x] Criar documentação técnica completa
- [x] Desenvolver exemplos práticos
- [x] Documentar casos de uso comuns
- [x] Criar guias de integração

### **Fase 4: Validação e Consolidação**
- [x] Validar documentação com código real
- [x] Consolidar descobertas
- [x] Identificar insights e recomendações
- [x] Preparar lição educacional

## 🔍 **Arquivos Identificados para Análise**

### **Arquivos Principais:**
- `canary/src/creatures/players/player.hpp` - Classe Player com sistema de inventário
- `canary/src/items/containers/container.hpp` - Sistema de containers
- `canary/src/items/containers/container.cpp` - Implementação de containers
- `canary/src/creatures/creatures_definitions.hpp` - Definições de slots
- `canary/src/items/cylinder.hpp` - Sistema de cilindros (base para containers)

### **Arquivos Relacionados:**
- `canary/src/items/item.hpp` - Sistema de itens
- `canary/src/items/items.hpp` - Gerenciamento de itens
- `canary/src/lua/functions/creatures/player/player_functions.hpp` - Funções Lua
- `canary/src/server/network/protocol/protocolgame.hpp` - Protocolo de rede

## 📊 **Status da Pesquisa**

### **Progresso Geral**: 100%
### **Fase Atual**: Fase 4 - Validação e Consolidação
### **Arquivos Analisados**: 8/8
### **Componentes Mapeados**: 12/12

---

## 🔬 **Análise Completa**

### **Fase 1: Descoberta e Mapeamento - CONCLUÍDA**

#### **Arquivos Principais Identificados:**
- ✅ `canary/src/creatures/players/player.hpp` - Classe Player com inventário
- ✅ `canary/src/items/containers/container.hpp` - Sistema de containers
- ✅ `canary/src/items/containers/container.cpp` - Implementação de containers
- ✅ `canary/src/creatures/creatures_definitions.hpp` - Definições de slots
- ✅ `canary/src/items/cylinder.hpp` - Sistema de cilindros
- ✅ `canary/src/items/item.hpp` - Sistema de itens
- ✅ `canary/src/items/items.hpp` - Gerenciamento de itens
- ✅ `canary/src/lua/functions/creatures/player/player_functions.hpp` - Funções Lua

#### **Componentes Principais Mapeados:**

**1. Sistema de Slots do Inventário**
- **CONST_SLOT_HEAD**: Slot da cabeça (1)
- **CONST_SLOT_NECKLACE**: Slot do colar (2)
- **CONST_SLOT_BACKPACK**: Slot da mochila (3)
- **CONST_SLOT_ARMOR**: Slot da armadura (4)
- **CONST_SLOT_RIGHT**: Slot da mão direita (5)
- **CONST_SLOT_LEFT**: Slot da mão esquerda (6)
- **CONST_SLOT_LEGS**: Slot das pernas (7)
- **CONST_SLOT_FEET**: Slot dos pés (8)
- **CONST_SLOT_RING**: Slot do anel (9)
- **CONST_SLOT_AMMO**: Slot da munição (10)
- **CONST_SLOT_STORE_INBOX**: Slot da caixa de entrada da loja (11)

**2. Classe Player (Sistema de Inventário)**
- Array de itens do inventário: `std::shared_ptr<Item> inventory[CONST_SLOT_LAST + 1]`
- Sistema de peso: `uint32_t inventoryWeight`
- Sistema de capacidade: `uint32_t capacity`, `uint32_t bonusCapacity`
- Sistema de containers abertos: `std::map<uint8_t, OpenContainer> openContainers`

**3. Classe Container**
- Sistema de itens: `ItemDeque itemlist`
- Capacidade máxima: `uint32_t m_maxItems`
- Sistema de peso: `uint32_t totalWeight`
- Sistema de travamento: `bool unlocked`
- Sistema de paginação: `bool pagination`

**4. Sistema de Cylinder**
- Base para containers e inventário
- Sistema de consultas: `queryAdd`, `queryRemove`, `queryMaxCount`
- Sistema de destino: `queryDestination`

### **Fase 2: Análise Profunda - CONCLUÍDA**

#### **Componentes Analisados:**
- [x] Análise detalhada do sistema de slots
- [x] Documentação do sistema de containers
- [x] Mapeamento do sistema de peso e capacidade
- [x] Análise do sistema de containers abertos
- [x] Documentação do sistema de consultas

## 📚 **Documentação Técnica**

### **1. Arquitetura do Sistema de Inventário**

O sistema de inventário do Canary é uma arquitetura complexa e modular que gerencia todos os itens que um jogador pode carregar. Ele é composto por vários componentes interconectados:

#### **1.1 Sistema de Slots**
```cpp
enum Slots_t : uint8_t {
    CONST_SLOT_WHEREEVER = 0,
    CONST_SLOT_HEAD = 1,
    CONST_SLOT_NECKLACE = 2,
    CONST_SLOT_BACKPACK = 3,
    CONST_SLOT_ARMOR = 4,
    CONST_SLOT_RIGHT = 5,
    CONST_SLOT_LEFT = 6,
    CONST_SLOT_LEGS = 7,
    CONST_SLOT_FEET = 8,
    CONST_SLOT_RING = 9,
    CONST_SLOT_AMMO = 10,
    CONST_SLOT_STORE_INBOX = 11,

    CONST_SLOT_FIRST = CONST_SLOT_HEAD,
    CONST_SLOT_LAST = CONST_SLOT_STORE_INBOX,
};
```

#### **1.2 Estrutura do Inventário do Player**
```cpp
class Player : public Creature, public Cylinder, public Bankable {
private:
    // Array de itens do inventário
    std::shared_ptr<Item> inventory[CONST_SLOT_LAST + 1] = {};
    
    // Sistema de peso
    uint32_t inventoryWeight = 0;
    uint32_t capacity = 40000;
    uint32_t bonusCapacity = 0;
    
    // Containers abertos
    std::map<uint8_t, OpenContainer> openContainers;
    
    // Habilidades de itens
    bool inventoryAbilities[CONST_SLOT_LAST + 1] = {};
};
```

#### **1.3 Estrutura OpenContainer**
```cpp
struct OpenContainer {
    std::shared_ptr<Container> container;
    uint16_t index;
};
```

### **2. Sistema de Containers**

#### **2.1 Classe Container**
```cpp
class Container : public Item, public Cylinder {
private:
    uint32_t m_maxItems {};
    uint32_t maxSize {};
    uint32_t totalWeight {};
    ItemDeque itemlist;
    uint32_t serializationCount = {};
    bool unlocked {};
    bool pagination {};

public:
    // Construtores
    explicit Container(uint16_t type);
    Container(uint16_t type, uint16_t size, bool unlocked = true, bool pagination = false);
    
    // Métodos principais
    uint32_t getMaxCapacity() const;
    size_t size() const;
    bool empty() const;
    uint32_t capacity() const;
    uint16_t getFreeSlots() const;
    uint32_t getWeight() const final;
    
    // Sistema de itens
    void addItem(const std::shared_ptr<Item> &item);
    std::shared_ptr<Item> getItemByIndex(size_t index) const;
    void removeItem(const std::shared_ptr<Thing> &thing, bool sendUpdateToClient = false);
    
    // Sistema de consultas
    ReturnValue queryAdd(int32_t index, const std::shared_ptr<Thing> &thing, uint32_t count, uint32_t flags, const std::shared_ptr<Creature> &actor = nullptr) override;
    ReturnValue queryMaxCount(int32_t index, const std::shared_ptr<Thing> &thing, uint32_t count, uint32_t &maxQueryCount, uint32_t flags) final;
    ReturnValue queryRemove(const std::shared_ptr<Thing> &thing, uint32_t count, uint32_t flags, const std::shared_ptr<Creature> &actor = nullptr) override;
    std::shared_ptr<Cylinder> queryDestination(int32_t &index, const std::shared_ptr<Thing> &thing, std::shared_ptr<Item> &destItem, uint32_t &flags) final;
};
```

#### **2.2 ContainerIterator**
```cpp
class ContainerIterator {
public:
    ContainerIterator(const std::shared_ptr<Container> &container, size_t maxDepth);
    
    bool hasNext() const;
    void advance();
    std::shared_ptr<Item> operator*() const;
    bool hasReachedMaxDepth() const;
    std::shared_ptr<Container> getCurrentContainer() const;
    size_t getCurrentIndex() const;

private:
    struct IteratorState {
        std::weak_ptr<Container> container;
        size_t index;
        size_t depth;
        
        IteratorState(std::shared_ptr<Container> c, size_t i, size_t d) :
            container(c), index(i), depth(d) { }
    };
    
    std::vector<IteratorState> states;
    std::unordered_set<std::shared_ptr<Container>> visitedContainers;
    size_t maxTraversalDepth = 0;
    bool m_maxDepthReached = false;
    bool m_cycleDetected = false;
};
```

### **3. Sistema de Peso e Capacidade**

#### **3.1 Cálculo de Capacidade**
```cpp
class Player {
public:
    uint32_t getBaseCapacity() const;
    uint32_t getCapacity() const;
    uint32_t getBonusCapacity() const;
    uint32_t getFreeCapacity() const;
    
private:
    void updateInventoryWeight();
};
```

#### **3.2 Sistema de Peso**
```cpp
// Cálculo do peso total do inventário
uint32_t inventoryWeight = 0;

// Capacidade base e bônus
uint32_t capacity = 40000;
uint32_t bonusCapacity = 0;

// Capacidade total = base + bônus
uint32_t getCapacity() const {
    return capacity + bonusCapacity;
}

// Capacidade livre = total - peso atual
uint32_t getFreeCapacity() const {
    return getCapacity() - inventoryWeight;
}
```

### **4. Sistema de Containers Abertos**

#### **4.1 Gerenciamento de Containers**
```cpp
class Player {
public:
    void addContainer(uint8_t cid, const std::shared_ptr<Container> &container);
    void closeContainer(uint8_t cid);
    void setContainerIndex(uint8_t cid, uint16_t index);
    std::shared_ptr<Container> getContainerByID(uint8_t cid);
    int8_t getContainerID(const std::shared_ptr<Container> &container) const;
    uint16_t getContainerIndex(uint8_t cid) const;

private:
    std::map<uint8_t, OpenContainer> openContainers;
};
```

#### **4.2 Operações de Container**
```cpp
// Adicionar container
void Player::addContainer(uint8_t cid, const std::shared_ptr<Container> &container) {
    openContainers[cid] = { container, 0 };
}

// Fechar container
void Player::closeContainer(uint8_t cid) {
    openContainers.erase(cid);
}

// Obter container por ID
std::shared_ptr<Container> Player::getContainerByID(uint8_t cid) {
    auto it = openContainers.find(cid);
    return it != openContainers.end() ? it->second.container : nullptr;
}
```

### **5. Sistema de Consultas (Cylinder)**

#### **5.1 Interface Cylinder**
```cpp
class Cylinder {
public:
    virtual ReturnValue queryAdd(int32_t index, const std::shared_ptr<Thing> &thing, uint32_t count, uint32_t flags, const std::shared_ptr<Creature> &actor = nullptr) = 0;
    virtual ReturnValue queryMaxCount(int32_t index, const std::shared_ptr<Thing> &thing, uint32_t count, uint32_t &maxQueryCount, uint32_t flags) = 0;
    virtual ReturnValue queryRemove(const std::shared_ptr<Thing> &thing, uint32_t count, uint32_t flags, const std::shared_ptr<Creature> &actor = nullptr) = 0;
    virtual std::shared_ptr<Cylinder> queryDestination(int32_t &index, const std::shared_ptr<Thing> &thing, std::shared_ptr<Item> &destItem, uint32_t &flags) = 0;
    
    virtual void addThing(const std::shared_ptr<Thing> &thing) = 0;
    virtual void addThing(int32_t index, const std::shared_ptr<Thing> &thing) = 0;
    virtual void updateThing(const std::shared_ptr<Thing> &thing, uint16_t itemId, uint32_t count) = 0;
    virtual void replaceThing(uint32_t index, const std::shared_ptr<Thing> &thing) = 0;
    virtual void removeThing(const std::shared_ptr<Thing> &thing, uint32_t count) = 0;
    
    virtual int32_t getThingIndex(const std::shared_ptr<Thing> &thing) const = 0;
    virtual size_t getFirstIndex() const = 0;
    virtual size_t getLastIndex() const = 0;
    virtual uint32_t getItemTypeCount(uint16_t itemId, int32_t subType = -1) const = 0;
    virtual std::shared_ptr<Thing> getThing(size_t index) const = 0;
};
```

#### **5.2 Implementação no Container**
```cpp
ReturnValue Container::queryAdd(int32_t index, const std::shared_ptr<Thing> &thing, uint32_t count, uint32_t flags, const std::shared_ptr<Creature> &actor) {
    if (!unlocked) {
        return RETURNVALUE_NOTPOSSIBLE;
    }
    
    if (thing == nullptr) {
        return RETURNVALUE_NOTPOSSIBLE;
    }
    
    if (index == INDEX_WHEREEVER && size() >= capacity()) {
        return RETURNVALUE_CONTAINERNOTENOUGHROOM;
    }
    
    // Verificar se o item pode ser adicionado
    const std::shared_ptr<Item> &item = thing->getItem();
    if (!item) {
        return RETURNVALUE_NOTPOSSIBLE;
    }
    
    // Verificar capacidade
    if (item->isStackable() && count != item->getItemCount()) {
        return RETURNVALUE_NOTPOSSIBLE;
    }
    
    return RETURNVALUE_NOERROR;
}
```

### **6. Sistema de Itens do Inventário**

#### **6.1 Métodos do Player para Inventário**
```cpp
class Player {
public:
    // Obter item do inventário
    std::shared_ptr<Item> getInventoryItem(Slots_t slot) const;
    
    // Verificar habilidades de itens
    bool isItemAbilityEnabled(Slots_t slot) const;
    void setItemAbility(Slots_t slot, bool enabled);
    
    // Obter todos os itens do inventário
    std::vector<std::shared_ptr<Item>> getAllInventoryItems(bool ignoreEquiped = false, bool ignoreItemWithTier = false) const;
    
    // Obter itens por ID
    std::vector<std::shared_ptr<Item>> getInventoryItemsFromId(uint16_t itemId, bool ignore = true) const;
    
    // Obter itens equipados
    std::vector<std::shared_ptr<Item>> getEquippedItems() const;
    
    // Sistema de stash
    ReturnValue addItemFromStash(uint16_t itemId, uint32_t itemCount);
    void stowItem(const std::shared_ptr<Item> &item, uint32_t count, bool allItems);
    uint32_t getStashItemCount(uint16_t itemId) const;
    bool withdrawItem(uint16_t itemId, uint32_t amount);
    StashItemList getStashItems() const;
};
```

#### **6.2 Sistema de Stash**
```cpp
// Adicionar item do stash
ReturnValue Player::addItemFromStash(uint16_t itemId, uint32_t itemCount) {
    auto stashCount = getStashItemCount(itemId);
    if (stashCount < itemCount) {
        return RETURNVALUE_NOTPOSSIBLE;
    }
    
    // Criar item e adicionar ao inventário
    auto item = Item::CreateItem(itemId, itemCount);
    if (!item) {
        return RETURNVALUE_NOTPOSSIBLE;
    }
    
    ReturnValue ret = addItem(item);
    if (ret == RETURNVALUE_NOERROR) {
        // Remover do stash
        withdrawItem(itemId, itemCount);
    }
    
    return ret;
}

// Guardar item no stash
void Player::stowItem(const std::shared_ptr<Item> &item, uint32_t count, bool allItems) {
    if (!item) {
        return;
    }
    
    uint32_t itemCount = allItems ? item->getItemCount() : count;
    if (itemCount > item->getItemCount()) {
        itemCount = item->getItemCount();
    }
    
    // Adicionar ao stash
    addItemOnStash(item->getID(), itemCount);
    
    // Remover do inventário
    removeItem(item, itemCount);
}
```

### **7. Sistema de Containers Especializados**

#### **7.1 DepotChest**
```cpp
class DepotChest : public Container {
public:
    explicit DepotChest(uint16_t type);
    
    std::shared_ptr<DepotLocker> getDepotLocker() override;
    bool isDepotChest() const override;
    
private:
    uint32_t depotId;
};
```

#### **7.2 Inbox**
```cpp
class Inbox : public Container {
public:
    explicit Inbox(uint16_t type);
    
    bool isInbox() const override;
};
```

#### **7.3 RewardChest**
```cpp
class RewardChest : public Container {
public:
    explicit RewardChest(uint16_t type);
    
    std::shared_ptr<Reward> getReward() override;
};
```

### **8. Sistema de Redes (Protocolo)**

#### **8.1 Envio de Dados do Inventário**
```cpp
class ProtocolGame {
public:
    // Enviar item do inventário
    void sendInventoryItem(Slots_t slot, const std::shared_ptr<Item> &item);
    
    // Enviar IDs do inventário
    void sendInventoryIds();
    
    // Enviar imbuements do inventário
    void sendInventoryImbuements(const std::map<Slots_t, std::shared_ptr<Item>> &items);
    
    // Enviar lista de venda
    void sendSaleItemList(const std::vector<ShopBlock> &shopVector, const std::map<uint16_t, uint16_t> &inventoryMap);
};
```

#### **8.2 Recebimento de Dados**
```cpp
class ProtocolGame {
public:
    // Processar imbuements do inventário
    void parseInventoryImbuements(NetworkMessage &msg);
};
```

### **9. Sistema de Containers Gerenciados**

#### **9.1 Managed Containers**
```cpp
class Player {
public:
    std::shared_ptr<Container> refreshManagedContainer(ObjectCategory_t category, const std::shared_ptr<Container> &container, bool isLootContainer, bool loading = false);
    std::shared_ptr<Container> getManagedContainer(ObjectCategory_t category, bool isLootContainer) const;
    void setMainBackpackUnassigned(const std::shared_ptr<Container> &container);

private:
    std::map<ObjectCategory_t, std::pair<std::shared_ptr<Container>, std::shared_ptr<Container>>> m_managedContainers;
};
```

#### **9.2 ObjectCategory_t**
```cpp
enum ObjectCategory_t : uint8_t {
    OBJECTCATEGORY_NONE = 0,
    OBJECTCATEGORY_ARMORS = 1,
    OBJECTCATEGORY_AMULETS = 2,
    OBJECTCATEGORY_BOOTS = 3,
    OBJECTCATEGORY_CONTAINERS = 4,
    OBJECTCATEGORY_DECORATION = 5,
    OBJECTCATEGORY_FOOD = 6,
    OBJECTCATEGORY_HELMETS = 7,
    OBJECTCATEGORY_LEGS = 8,
    OBJECTCATEGORY_OTHERS = 9,
    OBJECTCATEGORY_POTIONS = 10,
    OBJECTCATEGORY_RINGS = 11,
    OBJECTCATEGORY_RUNES = 12,
    OBJECTCATEGORY_SHIELDS = 13,
    OBJECTCATEGORY_TOOLS = 14,
    OBJECTCATEGORY_VALUABLES = 15,
    OBJECTCATEGORY_AMMO = 16,
    OBJECTCATEGORY_AXES = 17,
    OBJECTCATEGORY_CLUBS = 18,
    OBJECTCATEGORY_DISTANCEWEAPONS = 19,
    OBJECTCATEGORY_SWORDS = 20,
    OBJECTCATEGORY_WANDS = 21,
    OBJECTCATEGORY_CREATUREPRODUCTS = 22,
    OBJECTCATEGORY_RETRIEVAL = 23,
    OBJECTCATEGORY_GOLD = 24,
    OBJECTCATEGORY_DEFAULT = 25,
    OBJECTCATEGORY_UNASSIGNED = 26,
};
```

### **10. Sistema de Loot e Recompensas**

#### **10.1 Loot Pouch**
```cpp
class Player {
public:
    std::shared_ptr<Container> getLootPouch();
    
private:
    std::shared_ptr<Container> lootPouch;
};
```

#### **10.2 Sistema de Recompensas**
```cpp
class Player {
public:
    std::shared_ptr<Reward> getReward(uint64_t rewardId, bool autoCreate);
    void removeReward(uint64_t rewardId);
    void getRewardList(std::vector<uint64_t> &rewards) const;
    std::shared_ptr<RewardChest> getRewardChest();
    std::vector<std::shared_ptr<Item>> getRewardsFromContainer(const std::shared_ptr<Container> &container) const;

private:
    std::map<uint64_t, std::shared_ptr<Reward>> rewardMap;
    std::shared_ptr<RewardChest> rewardChest = nullptr;
};
```

### **11. Sistema de Depot**

#### **11.1 DepotChest e DepotLocker**
```cpp
class Player {
public:
    std::shared_ptr<DepotChest> getDepotChest(uint32_t depotId, bool autoCreate);
    std::shared_ptr<DepotLocker> getDepotLocker(uint32_t depotId);
    void onReceiveMail();
    bool isNearDepotBox();

private:
    std::map<uint32_t, std::shared_ptr<DepotLocker>> depotLockerMap;
    std::map<uint32_t, std::shared_ptr<DepotChest>> depotChests;
    std::shared_ptr<Inbox> inbox;
};
```

### **12. Sistema de Market**

#### **12.1 Store Inbox**
```cpp
class Player {
public:
    std::shared_ptr<Container> getStoreInbox() const;
    ItemsTierCountList getStoreInboxItemsId() const;

private:
    std::shared_ptr<Container> storeInbox;
};
```

## 💡 **Insights e Descobertas**

### **1. Arquitetura Modular e Hierárquica**

#### **1.1 Hierarquia de Classes**
O sistema de inventário utiliza uma hierarquia bem definida:
- **Cylinder**: Interface base para containers
- **Container**: Implementação base de container
- **DepotChest**: Container especializado para depósito
- **Inbox**: Container especializado para caixa de entrada
- **RewardChest**: Container especializado para recompensas

#### **1.2 Sistema de Slots Fixos**
O inventário utiliza um sistema de slots fixos com IDs específicos:
- Slots de equipamento (1-10): Cabeça, colar, mochila, armadura, etc.
- Slot especial (11): Store inbox para market
- Sistema flexível para containers abertos

### **2. Sistema de Peso e Capacidade Sofisticado**

#### **2.1 Cálculo Dinâmico**
```cpp
// Capacidade total = base + bônus
uint32_t getCapacity() const {
    return capacity + bonusCapacity;
}

// Capacidade livre = total - peso atual
uint32_t getFreeCapacity() const {
    return getCapacity() - inventoryWeight;
}
```

#### **2.2 Sistema de Bônus**
- Capacidade base: 40000
- Bônus de capacidade: Modificável via itens/efeitos
- Peso dinâmico: Atualizado automaticamente

### **3. Sistema de Containers Avançado**

#### **3.1 ContainerIterator Inteligente**
```cpp
class ContainerIterator {
    // Suporte a profundidade máxima
    // Detecção de ciclos
    // Navegação hierárquica
    // Estado de iteração persistente
};
```

#### **3.2 Sistema de Consultas Robusto**
```cpp
// Verificações antes de adicionar itens
ReturnValue queryAdd(...);
// Verificações antes de remover itens
ReturnValue queryRemove(...);
// Verificações de capacidade máxima
ReturnValue queryMaxCount(...);
// Determinação de destino
std::shared_ptr<Cylinder> queryDestination(...);
```

### **4. Sistema de Stash Inovador**

#### **4.1 Funcionalidades Avançadas**
- **Adição automática**: `addItemFromStash()`
- **Armazenamento**: `stowItem()`
- **Contagem**: `getStashItemCount()`
- **Retirada**: `withdrawItem()`
- **Listagem**: `getStashItems()`

#### **4.2 Integração com Inventário**
```cpp
// Adicionar do stash para inventário
ReturnValue addItemFromStash(uint16_t itemId, uint32_t itemCount);

// Mover do inventário para stash
void stowItem(const std::shared_ptr<Item> &item, uint32_t count, bool allItems);
```

### **5. Sistema de Containers Gerenciados**

#### **5.1 Categorização Automática**
```cpp
enum ObjectCategory_t : uint8_t {
    OBJECTCATEGORY_ARMORS = 1,
    OBJECTCATEGORY_AMULETS = 2,
    OBJECTCATEGORY_BOOTS = 3,
    // ... 26 categorias diferentes
};
```

#### **5.2 Gerenciamento Automático**
```cpp
// Container principal e secundário por categoria
std::map<ObjectCategory_t, std::pair<std::shared_ptr<Container>, std::shared_ptr<Container>>> m_managedContainers;
```

### **6. Sistema de Redes Otimizado**

#### **6.1 Protocolo Eficiente**
- Envio seletivo de dados
- Atualizações incrementais
- Suporte a imbuements
- Integração com market

#### **6.2 Sincronização Bidirecional**
```cpp
// Servidor → Cliente
void sendInventoryItem(Slots_t slot, const std::shared_ptr<Item> &item);
void sendInventoryIds();

// Cliente → Servidor
void parseInventoryImbuements(NetworkMessage &msg);
```

### **7. Sistema de Loot e Recompensas**

#### **7.1 Loot Pouch**
- Container especializado para loot
- Integração com sistema de monstros
- Gerenciamento automático

#### **7.2 Sistema de Recompensas**
```cpp
// Múltiplas recompensas por jogador
std::map<uint64_t, std::shared_ptr<Reward>> rewardMap;

// Container especializado
std::shared_ptr<RewardChest> rewardChest;
```

### **8. Sistema de Depot Completo**

#### **8.1 Múltiplos Depósitos**
```cpp
// Múltiplos depósitos por jogador
std::map<uint32_t, std::shared_ptr<DepotLocker>> depotLockerMap;
std::map<uint32_t, std::shared_ptr<DepotChest>> depotChests;
```

#### **8.2 Sistema de Mail**
```cpp
// Caixa de entrada integrada
std::shared_ptr<Inbox> inbox;
void onReceiveMail();
```

### **9. Integração com Market**

#### **9.1 Store Inbox**
- Container especializado para market
- Integração com sistema de vendas
- Sincronização automática

#### **9.2 Sistema de Vendas**
```cpp
// Lista de itens para venda
void sendSaleItemList(const std::vector<ShopBlock> &shopVector, const std::map<uint16_t, uint16_t> &inventoryMap);
```

### **10. Otimizações de Performance**

#### **10.1 Cache Inteligente**
- Containers abertos em memória
- Consultas otimizadas
- Atualizações incrementais

#### **10.2 Sistema de Eventos**
```cpp
// Eventos de inventário
void onUpdateInventoryItem(const std::shared_ptr<Item> &oldItem, const std::shared_ptr<Item> &newItem);
void onRemoveInventoryItem(const std::shared_ptr<Item> &item);
void onEquipInventory();
void onDeEquipInventory();
```

### **11. Padrões de Design Identificados**

#### **11.1 Strategy Pattern**
- Diferentes tipos de containers
- Múltiplas estratégias de consulta
- Vários sistemas de categorização

#### **11.2 Observer Pattern**
- Eventos de inventário
- Notificações de mudanças
- Sincronização automática

#### **11.3 Factory Pattern**
- Criação de containers
- Criação de itens
- Criação de recompensas

### **12. Limitações e Considerações**

#### **12.1 Complexidade**
- Sistema muito complexo para iniciantes
- Muitas dependências entre componentes
- Curva de aprendizado íngreme

#### **12.2 Performance**
- Muitas verificações podem impactar performance
- Sistema de containers pode ser custoso
- Cache necessário para otimização

#### **12.3 Manutenibilidade**
- Código muito acoplado
- Difícil de testar isoladamente
- Refatoração complexa

### **13. Recomendações**

#### **13.1 Para Desenvolvedores**
- Estudar a hierarquia de classes antes de modificar
- Usar o sistema de consultas para validações
- Implementar testes para mudanças

#### **13.2 Para Administradores**
- Monitorar uso de memória dos containers
- Configurar adequadamente as capacidades
- Manter backups antes de mudanças

#### **13.3 Para Usuários Finais**
- Entender as limitações de peso
- Usar adequadamente o sistema de stash
- Organizar containers eficientemente

## 🎓 **Lição Educacional**

### **CANARY-013: Sistema de Inventário - Lição Completa**

#### **Objetivo da Lição**
Compreender o sistema de inventário do Canary, sua arquitetura complexa, implementação e uso prático no desenvolvimento de servidores MMORPG.

#### **Teoria**

**O que é o Sistema de Inventário?**
O Sistema de Inventário do Canary é responsável por gerenciar todos os itens que um jogador pode carregar, incluindo equipamentos, containers, stash, depósitos e recompensas.

**Conceitos Fundamentais:**

1. **Slots Fixos**: Sistema de slots predefinidos para equipamentos
2. **Containers Dinâmicos**: Containers que podem ser abertos e fechados
3. **Sistema de Peso**: Controle de peso e capacidade
4. **Stash**: Sistema de armazenamento temporário
5. **Depósitos**: Sistema de armazenamento permanente
6. **Recompensas**: Sistema de recompensas automáticas

#### **Exemplos Práticos**

**1. Criando um Container Básico**
```cpp
// Criar container simples
auto container = Container::create(ITEM_BAG, 20, true, false);

// Adicionar item ao container
auto item = Item::CreateItem(ITEM_GOLD_COIN, 100);
container->addItem(item);

// Verificar capacidade
uint16_t freeSlots = container->getFreeSlots();
uint32_t weight = container->getWeight();
```

**2. Gerenciando Inventário do Player**
```cpp
// Obter item do inventário
auto item = player->getInventoryItem(CONST_SLOT_BACKPACK);

// Verificar capacidade
uint32_t freeCapacity = player->getFreeCapacity();
uint32_t totalCapacity = player->getCapacity();

// Adicionar item ao inventário
auto newItem = Item::CreateItem(ITEM_GOLD_COIN, 100);
ReturnValue ret = player->addItem(newItem);
```

**3. Sistema de Stash**
```cpp
// Adicionar item ao stash
player->addItemOnStash(ITEM_GOLD_COIN, 1000);

// Verificar quantidade no stash
uint32_t count = player->getStashItemCount(ITEM_GOLD_COIN);

// Retirar do stash
player->withdrawItem(ITEM_GOLD_COIN, 500);

// Mover item do inventário para stash
auto item = player->getInventoryItem(CONST_SLOT_BACKPACK);
player->stowItem(item, 50, false);
```

**4. Sistema de Containers Abertos**
```cpp
// Abrir container
auto container = Container::create(ITEM_BAG, 20);
player->addContainer(0, container);

// Obter container aberto
auto openContainer = player->getContainerByID(0);

// Fechar container
player->closeContainer(0);
```

**5. Sistema de Depot**
```cpp
// Obter depósito
auto depotChest = player->getDepotChest(1, true);
auto depotLocker = player->getDepotLocker(1);

// Verificar se está perto do depósito
bool nearDepot = player->isNearDepotBox();
```

**6. Sistema de Recompensas**
```cpp
// Obter recompensa
auto reward = player->getReward(12345, true);

// Obter lista de recompensas
std::vector<uint64_t> rewards;
player->getRewardList(rewards);

// Obter container de recompensas
auto rewardChest = player->getRewardChest();
```

#### **Exercícios Práticos**

**Exercício 1: Criar Sistema de Loot**
Crie um sistema que adiciona itens automaticamente ao loot pouch do jogador.

**Exercício 2: Implementar Sistema de Stash**
Implemente um sistema que permite ao jogador armazenar itens no stash e retirá-los posteriormente.

**Exercício 3: Sistema de Containers Categorizados**
Crie um sistema que organiza automaticamente itens em containers por categoria.

**Exercício 4: Sistema de Peso Dinâmico**
Implemente um sistema que modifica a capacidade do jogador baseado em itens equipados.

**Exercício 5: Sistema de Recompensas**
Crie um sistema que distribui recompensas automaticamente para jogadores.

#### **Conceitos Avançados**

**1. Sistema de Consultas**
```cpp
// Verificar se pode adicionar item
ReturnValue ret = container->queryAdd(0, item, 1, 0, player);
if (ret == RETURNVALUE_NOERROR) {
    container->addItem(item);
}
```

**2. ContainerIterator**
```cpp
// Iterar sobre todos os itens em um container
auto iterator = container->iterator();
while (iterator.hasNext()) {
    auto item = *iterator;
    // Processar item
    iterator.advance();
}
```

**3. Sistema de Eventos**
```cpp
// Eventos de inventário
void onUpdateInventoryItem(const std::shared_ptr<Item> &oldItem, const std::shared_ptr<Item> &newItem);
void onRemoveInventoryItem(const std::shared_ptr<Item> &item);
void onEquipInventory();
void onDeEquipInventory();
```

#### **Boas Práticas**

1. **Sempre verificar capacidade** antes de adicionar itens
2. **Usar o sistema de consultas** para validações
3. **Implementar verificações de peso** adequadas
4. **Otimizar uso de containers** para performance
5. **Documentar categorias** de itens claramente
6. **Testar extensivamente** antes de implementar em produção

#### **Integração com Outros Sistemas**

**Sistema de Itens (CANARY-007)**
- Gerenciamento de propriedades de itens
- Sistema de peso e atributos
- Integração com equipamentos

**Sistema de Lua (CANARY-006)**
- Scripts para customização
- Eventos de inventário
- Funções de gerenciamento

**Sistema de Rede (CANARY-003)**
- Sincronização com cliente
- Protocolo de inventário
- Atualizações em tempo real

#### **Conclusão**

O Sistema de Inventário do Canary é uma arquitetura complexa e poderosa que oferece flexibilidade extrema para gerenciamento de itens. Sua modularidade permite desde implementações simples até sistemas muito complexos, sempre mantendo performance e segurança.

A chave para dominar este sistema é entender os conceitos fundamentais e praticar com exemplos progressivamente mais complexos.

---

**Pesquisa Iniciada**: 2025-01-27 17:30:00  
**Responsável**: Habdel Research System  
**Status**: ✅ **CONCLUÍDA**  
**Próximo**: CANARY-014: Sistema de NPCs
