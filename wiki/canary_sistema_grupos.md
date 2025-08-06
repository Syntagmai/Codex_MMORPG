---
tags: [canary, sistema_grupos, party, guild, permissions, habdel_research]
type: wiki_page
status: active
priority: high
created: 2025-08-05
updated: 2025-08-05
aliases: [grupos_canary, party_system, guild_system, permissions_system]
level: intermediate
category: sistemas_avancados
dependencies: [canary_fundamentos, canary_arquitetura_core]
related: [canary_sistema_combate, canary_sistema_magias, canary_sistema_monstros]
---

# 🎯 **Sistema de Grupos - Canary**

> [!info] **Baseado na Pesquisa Habdel**
> Esta página é baseada na pesquisa detalhada **[CANARY-016: Sistema de Grupos](habdel/CANARY-016.md)** do Habdel, que analisou profundamente a arquitetura e implementação do sistema de grupos no Canary.

---

## 📋 **Visão Geral**

O **Sistema de Grupos** do Canary é um componente fundamental que gerencia permissões, organizações sociais e funcionalidades colaborativas no servidor. Ele inclui grupos de usuário, parties temporárias, guildas permanentes e familiars de combate.

### **🎯 Objetivos do Sistema**
- **Controle de Permissões**: Gerenciar capacidades e acesso dos jogadores
- **Organização Social**: Facilitar colaboração e interação entre jogadores
- **Experiência Compartilhada**: Distribuir experiência e loot em grupos
- **Hierarquia**: Estabelecer estruturas organizacionais (grupos, guildas, parties)

---

## 🏗️ **Arquitetura do Sistema**

### **📁 Estrutura de Arquivos**

```
canary/src/creatures/players/grouping/
├── groups.hpp          # Definição da classe Groups e estrutura Group
├── groups.cpp          # Implementação do sistema de grupos
├── party.hpp           # Sistema de party/grupo de jogadores
├── party.cpp           # Implementação do sistema de party
├── guild.hpp           # Sistema de guildas
├── guild.cpp           # Implementação de guildas
├── team_finder.hpp     # Sistema de busca de equipes
└── familiars.hpp       # Sistema de familiars
```

### **🔧 Componentes Principais**

#### **1. Estrutura Group**
```cpp
struct Group {
    std::string name;                    // Nome do grupo
    std::array<bool, magic_enum::enum_integer(PlayerFlags_t::FlagLast)> flags { false }; // Flags do jogador
    uint32_t maxDepotItems;              // Máximo de itens no depósito
    uint32_t maxVipEntries;              // Máximo de entradas VIP
    uint16_t id;                         // ID único do grupo
    bool access;                         // Permissão de acesso
};
```

#### **2. Classe Groups**
```cpp
class Groups {
public:
    static uint8_t getFlagNumber(PlayerFlags_t playerFlags);
    static PlayerFlags_t getFlagFromNumber(uint8_t value);
    static bool reload();
    bool load();
    [[nodiscard]] std::shared_ptr<Group> getGroup(uint16_t id) const;
    std::vector<std::shared_ptr<Group>> &getGroups();

private:
    std::vector<std::shared_ptr<Group>> groups_vector;
};
```

#### **3. Sistema de Party**
```cpp
class Party final : public SharedObject {
public:
    static std::shared_ptr<Party> create(const std::shared_ptr<Player> &leader);
    
    // Gerenciamento de membros
    std::shared_ptr<Player> getLeader() const;
    std::vector<std::shared_ptr<Player>> getPlayers() const;
    std::vector<std::shared_ptr<Player>> getMembers();
    std::vector<std::shared_ptr<Player>> getInvitees();
    
    // Operações de party
    void disband();
    bool invitePlayer(const std::shared_ptr<Player> &player);
    bool joinParty(const std::shared_ptr<Player> &player);
    void revokeInvitation(const std::shared_ptr<Player> &player);
    bool passPartyLeadership(const std::shared_ptr<Player> &player);
    bool leaveParty(const std::shared_ptr<Player> &player, bool forceRemove = false);
    
    // Sistema de experiência compartilhada
    void shareExperience(uint64_t experience, const std::shared_ptr<Creature> &target = nullptr);
    bool setSharedExperience(const std::shared_ptr<Player> &player, bool sharedExpActive, bool silent = false);
    bool isSharedExperienceActive() const;
    bool isSharedExperienceEnabled() const;
};
```

---

## 🔧 **APIs e Interfaces**

### **1. Funções Lua para Grupos**
```cpp
class GroupFunctions {
public:
    static void init(lua_State* L);

private:
    static int luaGroupCreate(lua_State* L);
    static int luaGroupGetId(lua_State* L);
    static int luaGroupGetName(lua_State* L);
    static int luaGroupGetFlags(lua_State* L);
    static int luaGroupGetAccess(lua_State* L);
    static int luaGroupGetMaxDepotItems(lua_State* L);
    static int luaGroupGetMaxVipEntries(lua_State* L);
    static int luaGroupHasFlag(lua_State* L);
};
```

### **2. Funções Lua para Players**
```cpp
// Funções relacionadas a grupos
static int luaPlayerGetGroup(lua_State* L);
static int luaPlayerSetGroup(lua_State* L);
static int luaPlayerHasGroupFlag(lua_State* L);
static int luaPlayerSetGroupFlag(lua_State* L);
static int luaPlayerRemoveGroupFlag(lua_State* L);
```

### **3. Funções do Game**
```cpp
// Gerenciamento de party
void Game::playerInviteToParty(uint32_t playerId, uint32_t invitedId);
void Game::playerJoinParty(uint32_t playerId, uint32_t leaderId);
void Game::playerRevokePartyInvitation(uint32_t playerId, uint32_t invitedId);
void Game::playerPassPartyLeadership(uint32_t playerId, uint32_t newLeaderId);
void Game::playerLeaveParty(uint32_t playerId);
void Game::playerEnableSharedPartyExperience(uint32_t playerId, bool sharedExpActive);
```

---

## 📊 **Fluxo de Dados**

### **1. Carregamento de Grupos**
```
1. Groups::load() → Carrega XML/groups.xml
2. parseGroupFlags() → Processa flags do grupo
3. groups_vector.emplace_back() → Adiciona grupo ao vetor
4. getGroup(id) → Retorna grupo por ID
```

### **2. Criação de Party**
```
1. Party::create(leader) → Cria nova party
2. party->invitePlayer(player) → Convida jogador
3. player->isInviting(leader) → Verifica convite
4. party->joinParty(player) → Jogador entra na party
```

### **3. Experiência Compartilhada**
```
1. setSharedExperience(player, true) → Ativa exp compartilhada
2. shareExperience(exp, target) → Distribui experiência
3. updateSharedExperience() → Atualiza status
4. getMemberSharedExperienceStatus() → Verifica status
```

---

## 💡 **Exemplos Práticos**

### **1. Criando um Grupo Personalizado**

#### **Nível Básico**
```lua
-- Exemplo de criação de grupo via Lua
local group = Group.create()
group:setId(10)
group:setName("Vip Premium")
group:setAccess(true)
group:setMaxDepotItems(2000)
group:setMaxVipEntries(100)
group:setFlag(PlayerFlag_CanReportBugs, true)
group:setFlag(PlayerFlag_CanSeeSpecialDescription, true)
```

#### **Nível Intermediário**
```lua
-- Exemplo com tratamento de erros
local function createPremiumGroup()
    local success, group = pcall(function()
        local g = Group.create()
        g:setId(10)
        g:setName("Vip Premium")
        g:setAccess(true)
        g:setMaxDepotItems(2000)
        g:setMaxVipEntries(100)
        g:setFlag(PlayerFlag_CanReportBugs, true)
        g:setFlag(PlayerFlag_CanSeeSpecialDescription, true)
        return g
    end)
    
    if not success then
        print("Erro ao criar grupo:", group)
        return nil
    end
    
    return group
end
```

#### **Nível Avançado**
```lua
-- Exemplo com metatable e funcionalidade avançada
local GroupManager = {}
GroupManager.__index = GroupManager

function GroupManager.new()
    local self = setmetatable({}, GroupManager)
    self.groups = {}
    return self
end

function GroupManager:createGroup(config)
    local group = Group.create()
    for key, value in pairs(config) do
        if type(value) == "function" then
            value(group)
        else
            group["set" .. key](group, value)
        end
    end
    self.groups[group:getId()] = group
    return group
end

-- Uso
local manager = GroupManager.new()
local premiumGroup = manager:createGroup({
    Id = 10,
    Name = "Vip Premium",
    Access = true,
    MaxDepotItems = 2000,
    MaxVipEntries = 100,
    Flags = function(group)
        group:setFlag(PlayerFlag_CanReportBugs, true)
        group:setFlag(PlayerFlag_CanSeeSpecialDescription, true)
    end
})
```

### **2. Gerenciando Party**

#### **Nível Básico**
```lua
-- Exemplo de gerenciamento de party
local player = Player("Leader")
local party = Party.create(player)

-- Convitar jogador
local member = Player("Member")
party:invitePlayer(member)

-- Ativar experiência compartilhada
party:setSharedExperience(player, true)

-- Compartilhar experiência
party:shareExperience(1000, monster)

-- Passar liderança
party:passPartyLeadership(player, member)
```

#### **Nível Intermediário**
```lua
-- Exemplo com sistema de convites
local function inviteToParty(leader, targetName)
    local target = Player(targetName)
    if not target then
        return false, "Jogador não encontrado"
    end
    
    local party = leader:getParty()
    if not party then
        party = Party.create(leader)
    end
    
    if party:invitePlayer(target) then
        return true, "Convite enviado com sucesso"
    else
        return false, "Erro ao enviar convite"
    end
end
```

#### **Nível Avançado**
```lua
-- Exemplo com sistema de party avançado
local AdvancedParty = {}
AdvancedParty.__index = AdvancedParty

function AdvancedParty.new(leader)
    local self = setmetatable({}, AdvancedParty)
    self.party = Party.create(leader)
    self.invites = {}
    self.rules = {
        autoLoot = false,
        expSharing = true,
        maxMembers = 4
    }
    return self
end

function AdvancedParty:inviteWithRules(player, rules)
    if #self.party:getMembers() >= self.rules.maxMembers then
        return false, "Party cheia"
    end
    
    if self.party:invitePlayer(player) then
        self.invites[player:getId()] = {
            timestamp = os.time(),
            rules = rules or {}
        }
        return true, "Convite enviado"
    end
    
    return false, "Erro ao convidar"
end

function AdvancedParty:applyRules()
    if self.rules.expSharing then
        for _, member in ipairs(self.party:getMembers()) do
            self.party:setSharedExperience(member, true)
        end
    end
end
```

### **3. Verificando Permissões de Grupo**
```lua
-- Exemplo de verificação de permissões
local function checkPlayerPermissions(playerName)
    local player = Player(playerName)
    if not player then
        return false, "Jogador não encontrado"
    end
    
    local group = player:getGroup()
    local permissions = {}
    
    -- Verificar flags específicas
    if group:hasFlag(PlayerFlag_CanReportBugs) then
        permissions.canReportBugs = true
    end
    
    if group:hasFlag(PlayerFlag_CanSeeSpecialDescription) then
        permissions.canSeeSpecialDescription = true
    end
    
    if group:hasFlag(PlayerFlag_CanAccessPlayerManager) then
        permissions.canAccessPlayerManager = true
    end
    
    return true, permissions
end

-- Uso
local success, perms = checkPlayerPermissions("TestPlayer")
if success then
    print("Permissões:", json.encode(perms))
end
```

---

## 🎓 **Lição Educacional: Sistema de Grupos em MMORPGs**

### **Conceitos Fundamentais**

#### **1. Hierarquia de Grupos**
- **Grupos de Usuário**: Definem permissões e capacidades
- **Parties**: Grupos temporários para aventuras
- **Guildas**: Organizações permanentes de jogadores
- **Familiars**: Companheiros de combate

#### **2. Sistema de Permissões**
- **Flags**: Controle granular de capacidades
- **Access**: Controle de acesso a áreas
- **Limites**: Restrições de recursos (depósito, VIP)

#### **3. Experiência Compartilhada**
- **Distribuição**: Baseada em nível e distância
- **Condições**: Membros ativos e próximos
- **Análise**: Tracking de contribuição

### **Padrões de Design**

#### **1. Factory Pattern**
```cpp
static std::shared_ptr<Party> create(const std::shared_ptr<Player> &leader);
```

#### **2. Observer Pattern**
```cpp
void updateAllPartyIcons();
void updatePlayerStatus(const std::shared_ptr<Player> &player);
```

#### **3. State Pattern**
```cpp
enum SharedExpStatus_t : uint8_t {
    SHAREDEXP_OK,
    SHAREDEXP_TOOFARAWAY,
    SHAREDEXP_LEVELDIFFTOOLARGE,
    SHAREDEXP_MEMBERINACTIVE,
    SHAREDEXP_EMPTYPARTY
};
```

---

## 🔍 **Insights Técnicos**

### **1. Otimizações Implementadas**

#### **Memory Management**
- **Shared Pointers**: Uso consistente de `std::shared_ptr`
- **Vector Optimization**: `shrink_to_fit()` após carregamento
- **Lazy Loading**: Grupos carregados sob demanda

#### **Performance**
- **Magic Enum**: Uso de `magic_enum` para conversões eficientes
- **Flat Hash Map**: `phmap::flat_hash_map` para parsing de flags
- **Range-based Loops**: Uso de `std::ranges` para iterações

#### **Thread Safety**
- **SharedObject**: Herança de `SharedObject` para thread safety
- **Weak Pointers**: `std::weak_ptr` para referências circulares
- **Atomic Operations**: Operações atômicas para contadores

### **2. Integrações com Outros Sistemas**

#### **Sistema de Players**
- **Group Assignment**: Jogadores associados a grupos
- **Permission Checking**: Verificação de flags em tempo real
- **Status Updates**: Atualização de status baseada em grupo

#### **Sistema de Combat**
- **Experience Sharing**: Integração com sistema de experiência
- **Loot Distribution**: Distribuição de loot em party
- **Damage Tracking**: Rastreamento de dano por membro

#### **Sistema de Communication**
- **Party Messages**: Mensagens específicas de party
- **Status Broadcasting**: Broadcast de status para membros
- **Invitation System**: Sistema de convites integrado

### **3. Configuração e Customização**

#### **XML Configuration**
```xml
<groups>
    <group id="1" name="Player" access="0" maxdepotitems="1000" maxvipentries="100" flags="0">
        <flags>
            <flag name="canreportbugs" value="1"/>
            <flag name="canseespecialdescription" value="1"/>
        </flags>
    </group>
</groups>
```

#### **Lua Scripting**
- **Dynamic Group Creation**: Criação dinâmica via Lua
- **Flag Management**: Gerenciamento de flags via scripts
- **Permission Checking**: Verificação de permissões em scripts

---

## 🚀 **Recomendações e Melhorias**

### **1. Otimizações Sugeridas**

#### **Cache System**
```cpp
// Implementar cache para grupos frequentemente acessados
class GroupCache {
    std::unordered_map<uint16_t, std::shared_ptr<Group>> cache;
    std::mutex cacheMutex;
public:
    std::shared_ptr<Group> getGroup(uint16_t id);
    void invalidateCache();
};
```

#### **Async Loading**
```cpp
// Carregamento assíncrono de grupos
std::future<bool> Groups::loadAsync() {
    return std::async(std::launch::async, [this]() {
        return this->load();
    });
}
```

#### **Batch Operations**
```cpp
// Operações em lote para múltiplos grupos
void Groups::updateMultipleGroups(const std::vector<GroupUpdate>& updates);
```

### **2. Funcionalidades Avançadas**

#### **Dynamic Permissions**
```cpp
// Sistema de permissões dinâmicas
class DynamicPermission {
    std::function<bool(const Player&)> condition;
    std::string permission;
public:
    bool check(const Player& player) const;
};
```

#### **Group Hierarchies**
```cpp
// Hierarquia de grupos
class GroupHierarchy {
    std::map<uint16_t, std::vector<uint16_t>> inheritance;
public:
    bool inheritsFrom(uint16_t child, uint16_t parent);
    std::vector<uint16_t> getAllPermissions(uint16_t groupId);
};
```

#### **Advanced Party Features**
```cpp
// Funcionalidades avançadas de party
class AdvancedParty : public Party {
public:
    void setPartyRoles(const std::map<Player*, PartyRole>& roles);
    void setPartyRules(const PartyRules& rules);
    void enableAutoLoot(const LootRules& rules);
};
```

### **3. Monitoramento e Analytics**

#### **Group Analytics**
```cpp
// Analytics para grupos
class GroupAnalytics {
public:
    void trackGroupActivity(uint16_t groupId, const std::string& action);
    void generateGroupReport(uint16_t groupId);
    void analyzePermissionUsage();
};
```

#### **Performance Monitoring**
```cpp
// Monitoramento de performance
class GroupPerformanceMonitor {
public:
    void trackGroupLoadTime();
    void trackPermissionCheckTime();
    void generatePerformanceReport();
};
```

---

## 📈 **Métricas e Estatísticas**

### **Complexidade do Sistema**
- **Classes Principais**: 4 (Groups, Party, Guild, TeamFinder)
- **Funções Lua**: 8 funções de grupo + 5 funções de player
- **Funções Game**: 6 funções de gerenciamento de party
- **Linhas de Código**: ~1,500 linhas (estimativa)

### **Integrações**
- **Sistemas Integrados**: 6 (Players, Combat, Communication, Inventory, VIP, Lua)
- **APIs Expostas**: 15+ funções públicas
- **Configurações**: XML + Lua scripting

### **Performance**
- **Carregamento**: O(1) para grupos individuais
- **Busca**: O(n) para busca linear, O(log n) com otimizações
- **Memory**: ~1KB por grupo + overhead de flags

---

## 🎯 **Conclusão**

O Sistema de Grupos do Canary demonstra uma arquitetura robusta e bem estruturada, com foco em performance, flexibilidade e integração. O uso de padrões modernos de C++, integração com Lua para scripting, e sistema de configuração XML proporciona uma base sólida para MMORPGs.

### **Pontos Fortes**
- ✅ Arquitetura modular e extensível
- ✅ Sistema de permissões granular
- ✅ Integração completa com outros sistemas
- ✅ Performance otimizada
- ✅ Suporte a scripting Lua

### **Áreas de Melhoria**
- 🔄 Sistema de cache para grupos frequentemente acessados
- 🔄 Carregamento assíncrono de configurações
- 🔄 Analytics e monitoramento avançado
- 🔄 Funcionalidades de party mais avançadas

### **Impacto no Projeto**
Este sistema forma a base para controle de acesso, organização de jogadores e funcionalidades sociais no MMORPG, sendo essencial para a experiência do usuário e administração do servidor.

---

## 🔗 **Dependências**

### **Sistemas Relacionados**
- [[canary_fundamentos|Fundamentos do Canary]] - Base conceitual
- [[canary_arquitetura_core|Arquitetura Core]] - Estrutura base
- [[canary_sistema_combate|Sistema de Combate]] - Experiência compartilhada
- [[canary_sistema_magias|Sistema de Magias]] - Permissões especiais
- [[canary_sistema_monstros|Sistema de Monstros]] - Loot compartilhado

### **Páginas Relacionadas**
- [[canary_sistema_guildas|Sistema de Guildas]] - Organizações permanentes
- [[canary_sistema_raids|Sistema de Raids]] - Grupos para raids
- [[canary_sistema_eventos|Sistema de Eventos]] - Eventos de grupo
- [[canary_sistema_condicoes|Sistema de Condições]] - Condições de grupo

---

## 📚 **Referências**

### **Código-Fonte**
- `canary/src/creatures/players/grouping/groups.hpp` - Definição de grupos
- `canary/src/creatures/players/grouping/party.hpp` - Sistema de party
- `canary/src/creatures/players/grouping/guild.hpp` - Sistema de guildas
- `canary/src/lua/functions/creatures/player/guild_functions.hpp` - Funções Lua

### **Documentação**
- [[habdel/CANARY-016|CANARY-016: Sistema de Grupos - Pesquisa Habdel]] - Pesquisa detalhada
- [[canary_fundamentos|Fundamentos do Canary]] - Conceitos base
- [[canary_arquitetura_core|Arquitetura Core]] - Estrutura do sistema

### **Configuração**
- `canary/data/XML/groups.xml` - Configuração de grupos
- `canary/data/XML/guilds.xml` - Configuração de guildas

---

*Última atualização: 2025-08-05* 