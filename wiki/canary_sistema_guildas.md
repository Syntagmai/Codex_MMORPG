---
tags: [canary, sistema_guildas, guild, ranks, hierarchy, habdel_research]
type: wiki_page
status: active
priority: high
created: 2025-08-05
updated: 2025-08-05
aliases: [guildas_canary, guild_system, ranks_system, hierarchy_system]
level: intermediate
category: sistemas_avancados
dependencies: [canary_fundamentos, canary_sistema_grupos]
related: [canary_sistema_grupos, canary_sistema_raids, canary_sistema_eventos]
---

# 🏰 **Sistema de Guildas - Canary**

> [!info] **Baseado na Pesquisa Habdel**
> Esta página é baseada na pesquisa detalhada **[CANARY-017: Sistema de Guildas](habdel/CANARY-017.md)** do Habdel, que analisou profundamente a arquitetura e implementação do sistema de guildas no Canary.

---

## 📋 **Visão Geral**

O **Sistema de Guildas** do Canary gerencia organizações permanentes de jogadores, incluindo hierarquias de ranks, permissões específicas, eventos de guilda e funcionalidades sociais avançadas. É um sistema complexo que permite aos jogadores se organizarem em estruturas hierárquicas permanentes.

### **🎯 Objetivos do Sistema**
- **Organização Permanente**: Criar estruturas hierárquicas duradouras
- **Hierarquia de Ranks**: Gerenciar diferentes níveis de autoridade
- **Funcionalidades Sociais**: Facilitar comunicação e colaboração
- **Eventos de Guilda**: Organizar atividades específicas da guilda

---

## 🏗️ **Arquitetura do Sistema**

### **📁 Estrutura de Arquivos**

```
canary/src/creatures/players/grouping/
├── guild.hpp          # Definição da classe Guild e estrutura GuildRank
├── guild.cpp          # Implementação do sistema de guildas
├── groups.hpp         # Sistema de grupos (relacionado)
├── party.hpp          # Sistema de party (relacionado)
└── team_finder.hpp    # Sistema de busca de equipes

canary/src/io/
├── ioguild.hpp        # Interface de I/O para guildas

canary/src/lua/functions/creatures/player/
├── guild_functions.hpp # Funções Lua para guildas
└── guild_functions.cpp # Implementação das funções Lua
```

### **🔧 Componentes Principais**

#### **1. Estrutura GuildRank**
```cpp
struct GuildRank {
    uint32_t id;        // ID único do rank
    std::string name;   // Nome do rank
    uint8_t level;      // Nível hierárquico

    GuildRank(uint32_t initId, std::string initName, uint8_t initLevel) :
        id(initId), name(std::move(initName)), level(initLevel) { }
};

using GuildRank_ptr = std::shared_ptr<GuildRank>;
```

#### **2. Classe Guild**
```cpp
class Guild {
public:
    // Criação e gerenciamento
    static std::shared_ptr<Guild> create(uint32_t id, const std::string &name);
    
    // Informações básicas
    uint32_t getId() const;
    std::string getName() const;
    std::string getMotto() const;
    
    // Gerenciamento de ranks
    void addRank(uint32_t id, const std::string &name, uint8_t level);
    std::vector<GuildRank_ptr> getRanks() const;
    GuildRank_ptr getRankById(uint32_t id) const;
    
    // Gerenciamento de membros
    void addMember(uint32_t playerId, uint32_t rankId);
    void removeMember(uint32_t playerId);
    std::vector<GuildMember> getMembers() const;
    
    // Funcionalidades de guilda
    void setMotto(const std::string &motto);
    void setDescription(const std::string &description);
    void setLogo(uint32_t logoId);
};
```

#### **3. Interface IOGuild**
```cpp
class IOGuild {
public:
    // Operações de banco de dados
    static bool loadGuilds();
    static bool saveGuild(const std::shared_ptr<Guild> &guild);
    static bool deleteGuild(uint32_t guildId);
    
    // Consultas
    static std::shared_ptr<Guild> loadGuildById(uint32_t guildId);
    static std::shared_ptr<Guild> loadGuildByName(const std::string &name);
    static std::vector<std::shared_ptr<Guild>> loadAllGuilds();
    
    // Operações de membros
    static bool addMemberToGuild(uint32_t guildId, uint32_t playerId, uint32_t rankId);
    static bool removeMemberFromGuild(uint32_t guildId, uint32_t playerId);
    static bool updateMemberRank(uint32_t guildId, uint32_t playerId, uint32_t newRankId);
};
```

---

## 🔧 **APIs e Interfaces**

### **1. Funções Lua para Guildas**
```cpp
class GuildFunctions {
public:
    static void init(lua_State* L);

private:
    static int luaGuildCreate(lua_State* L);
    static int luaGuildGetId(lua_State* L);
    static int luaGuildGetName(lua_State* L);
    static int luaGuildGetMotto(lua_State* L);
    static int luaGuildGetDescription(lua_State* L);
    static int luaGuildGetLogo(lua_State* L);
    static int luaGuildGetRanks(lua_State* L);
    static int luaGuildGetMembers(lua_State* L);
    static int luaGuildAddRank(lua_State* L);
    static int luaGuildAddMember(lua_State* L);
    static int luaGuildRemoveMember(lua_State* L);
    static int luaGuildSetMotto(lua_State* L);
    static int luaGuildSetDescription(lua_State* L);
    static int luaGuildSetLogo(lua_State* L);
};
```

### **2. Funções Lua para Players**
```cpp
// Funções relacionadas a guildas
static int luaPlayerGetGuild(lua_State* L);
static int luaPlayerSetGuild(lua_State* L);
static int luaPlayerGetGuildRank(lua_State* L);
static int luaPlayerSetGuildRank(lua_State* L);
static int luaPlayerIsGuildLeader(lua_State* L);
static int luaPlayerCanInviteToGuild(lua_State* L);
static int luaPlayerCanKickFromGuild(lua_State* L);
```

### **3. Funções do Game**
```cpp
// Gerenciamento de guildas
void Game::playerCreateGuild(uint32_t playerId, const std::string &name);
void Game::playerJoinGuild(uint32_t playerId, uint32_t guildId);
void Game::playerLeaveGuild(uint32_t playerId);
void Game::playerInviteToGuild(uint32_t playerId, uint32_t targetId);
void Game::playerKickFromGuild(uint32_t playerId, uint32_t targetId);
void Game::playerSetGuildRank(uint32_t playerId, uint32_t targetId, uint32_t rankId);
void Game::playerSetGuildMotto(uint32_t playerId, const std::string &motto);
```

---

## 📊 **Fluxo de Dados**

### **1. Criação de Guilda**
```
1. Game::playerCreateGuild() → Valida jogador e nome
2. Guild::create() → Cria nova guilda
3. IOGuild::saveGuild() → Salva no banco de dados
4. addMember() → Adiciona criador como líder
5. updateGuildInfo() → Atualiza informações
```

### **2. Gerenciamento de Membros**
```
1. playerInviteToGuild() → Envia convite
2. playerJoinGuild() → Aceita convite
3. IOGuild::addMemberToGuild() → Adiciona ao banco
4. updateGuildMembers() → Atualiza lista
5. notifyGuildMembers() → Notifica membros
```

### **3. Hierarquia de Ranks**
```
1. addRank() → Adiciona novo rank
2. setMemberRank() → Define rank do membro
3. checkPermissions() → Verifica permissões
4. updateMemberList() → Atualiza interface
```

---

## 💡 **Exemplos Práticos**

### **1. Criando uma Guilda**

#### **Nível Básico**
```lua
-- Exemplo de criação de guilda via Lua
local function createGuild(playerName, guildName)
    local player = Player(playerName)
    if not player then
        return false, "Jogador não encontrado"
    end
    
    local guild = Guild.create(0, guildName) -- ID 0 = auto-increment
    if not guild then
        return false, "Erro ao criar guilda"
    end
    
    -- Adicionar ranks padrão
    guild:addRank(1, "Leader", 3)
    guild:addRank(2, "Vice-Leader", 2)
    guild:addRank(3, "Member", 1)
    
    -- Adicionar criador como líder
    guild:addMember(player:getId(), 1)
    
    -- Salvar guilda
    if IOGuild.saveGuild(guild) then
        return true, "Guilda criada com sucesso"
    else
        return false, "Erro ao salvar guilda"
    end
end
```

#### **Nível Intermediário**
```lua
-- Exemplo com validações e configurações
local GuildManager = {}
GuildManager.__index = GuildManager

function GuildManager.new()
    local self = setmetatable({}, GuildManager)
    self.defaultRanks = {
        {id = 1, name = "Leader", level = 3},
        {id = 2, name = "Vice-Leader", level = 2},
        {id = 3, name = "Officer", level = 2},
        {id = 4, name = "Member", level = 1},
        {id = 5, name = "Recruit", level = 0}
    }
    return self
end

function GuildManager:createGuildWithConfig(playerName, config)
    local player = Player(playerName)
    if not player then
        return false, "Jogador não encontrado"
    end
    
    -- Validar configuração
    if not config.name or #config.name < 3 then
        return false, "Nome da guilda muito curto"
    end
    
    if config.name:match("[^%w%s]") then
        return false, "Nome da guilda contém caracteres inválidos"
    end
    
    -- Criar guilda
    local guild = Guild.create(0, config.name)
    if not guild then
        return false, "Erro ao criar guilda"
    end
    
    -- Configurar ranks personalizados ou usar padrão
    local ranks = config.ranks or self.defaultRanks
    for _, rank in ipairs(ranks) do
        guild:addRank(rank.id, rank.name, rank.level)
    end
    
    -- Configurar informações adicionais
    if config.motto then
        guild:setMotto(config.motto)
    end
    
    if config.description then
        guild:setDescription(config.description)
    end
    
    -- Adicionar criador como líder
    guild:addMember(player:getId(), 1)
    
    -- Salvar
    if IOGuild.saveGuild(guild) then
        return true, guild:getId()
    else
        return false, "Erro ao salvar guilda"
    end
end
```

#### **Nível Avançado**
```lua
-- Exemplo com sistema completo de gerenciamento
local AdvancedGuildSystem = {}
AdvancedGuildSystem.__index = AdvancedGuildSystem

function AdvancedGuildSystem.new()
    local self = setmetatable({}, AdvancedGuildSystem)
    self.guilds = {}
    self.invites = {}
    self.events = {}
    return self
end

function AdvancedGuildSystem:createGuildWithAdvancedFeatures(playerName, config)
    local player = Player(playerName)
    if not player then
        return false, "Jogador não encontrado"
    end
    
    -- Verificar se jogador já está em uma guilda
    if player:getGuild() then
        return false, "Jogador já está em uma guilda"
    end
    
    -- Verificar se nome já existe
    local existingGuild = IOGuild.loadGuildByName(config.name)
    if existingGuild then
        return false, "Nome de guilda já existe"
    end
    
    -- Criar guilda com validações avançadas
    local success, guildId = self:createGuildWithConfig(playerName, config)
    if not success then
        return false, guildId -- guildId contém a mensagem de erro
    end
    
    -- Configurar funcionalidades avançadas
    local guild = IOGuild.loadGuildById(guildId)
    if guild then
        -- Configurar sistema de eventos
        if config.events then
            self:setupGuildEvents(guild, config.events)
        end
        
        -- Configurar sistema de convites
        if config.inviteSettings then
            self:setupInviteSystem(guild, config.inviteSettings)
        end
        
        -- Configurar sistema de logs
        if config.logging then
            self:setupLoggingSystem(guild, config.logging)
        end
        
        -- Notificar criação
        self:notifyGuildCreation(guild, player)
        
        return true, guildId
    end
    
    return false, "Erro ao carregar guilda criada"
end

function AdvancedGuildSystem:setupGuildEvents(guild, eventConfig)
    -- Configurar eventos automáticos da guilda
    for eventType, settings in pairs(eventConfig) do
        self.events[guild:getId()] = self.events[guild:getId()] or {}
        self.events[guild:getId()][eventType] = settings
    end
end

function AdvancedGuildSystem:setupInviteSystem(guild, inviteConfig)
    -- Configurar sistema de convites
    self.invites[guild:getId()] = {
        autoAccept = inviteConfig.autoAccept or false,
        requireApproval = inviteConfig.requireApproval or true,
        maxInvites = inviteConfig.maxInvites or 5,
        inviteExpiry = inviteConfig.inviteExpiry or 24 * 60 * 60 -- 24 horas
    }
end

function AdvancedGuildSystem:setupLoggingSystem(guild, loggingConfig)
    -- Configurar sistema de logs
    if loggingConfig.enabled then
        -- Implementar sistema de logs para ações da guilda
        print("Sistema de logs configurado para guilda:", guild:getName())
    end
end

function AdvancedGuildSystem:notifyGuildCreation(guild, creator)
    -- Notificar criação da guilda
    print(string.format("Guilda '%s' criada por %s", guild:getName(), creator:getName()))
    
    -- Enviar mensagem para o criador
    creator:sendTextMessage(MESSAGE_INFO_DESCR, 
        string.format("Guilda '%s' criada com sucesso!", guild:getName()))
end
```

### **2. Gerenciando Membros da Guilda**

#### **Nível Básico**
```lua
-- Exemplo de gerenciamento de membros
local function manageGuildMembers(guildId)
    local guild = IOGuild.loadGuildById(guildId)
    if not guild then
        return false, "Guilda não encontrada"
    end
    
    local members = guild:getMembers()
    print("Membros da guilda:", guild:getName())
    
    for _, member in ipairs(members) do
        local player = Player(member.playerId)
        local rank = guild:getRankById(member.rankId)
        
        if player and rank then
            print(string.format("- %s (%s)", player:getName(), rank.name))
        end
    end
    
    return true, #members
end
```

#### **Nível Intermediário**
```lua
-- Exemplo com sistema de convites e aprovações
local function invitePlayerToGuild(guildId, inviterName, targetName)
    local inviter = Player(inviterName)
    local target = Player(targetName)
    
    if not inviter or not target then
        return false, "Jogador não encontrado"
    end
    
    local guild = inviter:getGuild()
    if not guild or guild:getId() ~= guildId then
        return false, "Você não pertence a esta guilda"
    end
    
    -- Verificar permissões
    local inviterRank = guild:getRankById(inviter:getGuildRank())
    if not inviterRank or inviterRank.level < 2 then
        return false, "Você não tem permissão para convidar"
    end
    
    -- Verificar se alvo já está em uma guilda
    if target:getGuild() then
        return false, "Jogador já está em uma guilda"
    end
    
    -- Enviar convite
    target:sendTextMessage(MESSAGE_INFO_DESCR, 
        string.format("Você foi convidado para a guilda '%s'", guild:getName()))
    
    return true, "Convite enviado"
end
```

#### **Nível Avançado**
```lua
-- Exemplo com sistema completo de gerenciamento
local GuildMemberManager = {}
GuildMemberManager.__index = GuildMemberManager

function GuildMemberManager.new(guildId)
    local self = setmetatable({}, GuildMemberManager)
    self.guildId = guildId
    self.guild = IOGuild.loadGuildById(guildId)
    self.pendingInvites = {}
    self.memberActivity = {}
    return self
end

function GuildMemberManager:invitePlayer(inviterId, targetId, rankId)
    local inviter = Player(inviterId)
    local target = Player(targetId)
    
    if not inviter or not target then
        return false, "Jogador não encontrado"
    end
    
    -- Verificar permissões
    if not self:canInvite(inviterId) then
        return false, "Sem permissão para convidar"
    end
    
    -- Verificar se já foi convidado
    if self.pendingInvites[targetId] then
        return false, "Jogador já foi convidado"
    end
    
    -- Criar convite
    self.pendingInvites[targetId] = {
        inviterId = inviterId,
        rankId = rankId,
        timestamp = os.time(),
        expiresAt = os.time() + (24 * 60 * 60) -- 24 horas
    }
    
    -- Notificar jogador
    target:sendTextMessage(MESSAGE_INFO_DESCR, 
        string.format("Convite para guilda '%s' enviado", self.guild:getName()))
    
    return true, "Convite enviado"
end

function GuildMemberManager:acceptInvite(playerId)
    local invite = self.pendingInvites[playerId]
    if not invite then
        return false, "Convite não encontrado"
    end
    
    -- Verificar se expirou
    if os.time() > invite.expiresAt then
        self.pendingInvites[playerId] = nil
        return false, "Convite expirado"
    end
    
    -- Adicionar à guilda
    if IOGuild.addMemberToGuild(self.guildId, playerId, invite.rankId) then
        self.pendingInvites[playerId] = nil
        self:trackMemberActivity(playerId, "joined")
        return true, "Jogador adicionado à guilda"
    else
        return false, "Erro ao adicionar jogador"
    end
end

function GuildMemberManager:kickMember(kickerId, targetId, reason)
    local kicker = Player(kickerId)
    local target = Player(targetId)
    
    if not kicker or not target then
        return false, "Jogador não encontrado"
    end
    
    -- Verificar permissões
    if not self:canKick(kickerId, targetId) then
        return false, "Sem permissão para expulsar"
    end
    
    -- Remover da guilda
    if IOGuild.removeMemberFromGuild(self.guildId, targetId) then
        self:trackMemberActivity(targetId, "kicked", reason)
        
        -- Notificar jogador
        target:sendTextMessage(MESSAGE_INFO_DESCR, 
            string.format("Você foi expulso da guilda '%s'. Motivo: %s", 
                self.guild:getName(), reason or "Não especificado"))
        
        return true, "Jogador expulso"
    else
        return false, "Erro ao expulsar jogador"
    end
end

function GuildMemberManager:canInvite(playerId)
    local player = Player(playerId)
    if not player then return false end
    
    local rank = self.guild:getRankById(player:getGuildRank())
    return rank and rank.level >= 2 -- Vice-leader ou superior
end

function GuildMemberManager:canKick(kickerId, targetId)
    local kicker = Player(kickerId)
    local target = Player(targetId)
    
    if not kicker or not target then return false end
    
    local kickerRank = self.guild:getRankById(kicker:getGuildRank())
    local targetRank = self.guild:getRankById(target:getGuildRank())
    
    -- Só pode expulsar membros de rank inferior
    return kickerRank and targetRank and kickerRank.level > targetRank.level
end

function GuildMemberManager:trackMemberActivity(playerId, action, data)
    self.memberActivity[playerId] = self.memberActivity[playerId] or {}
    table.insert(self.memberActivity[playerId], {
        action = action,
        data = data,
        timestamp = os.time()
    })
end
```

### **3. Gerenciando Ranks e Hierarquia**

#### **Nível Básico**
```lua
-- Exemplo de gerenciamento de ranks
local function manageGuildRanks(guildId)
    local guild = IOGuild.loadGuildById(guildId)
    if not guild then
        return false, "Guilda não encontrada"
    end
    
    local ranks = guild:getRanks()
    print("Ranks da guilda:", guild:getName())
    
    for _, rank in ipairs(ranks) do
        print(string.format("- %s (Nível %d)", rank.name, rank.level))
    end
    
    return true, #ranks
end
```

#### **Nível Intermediário**
```lua
-- Exemplo com sistema de promoções
local function promoteMember(guildId, promoterId, targetId)
    local promoter = Player(promoterId)
    local target = Player(targetId)
    
    if not promoter or not target then
        return false, "Jogador não encontrado"
    end
    
    local guild = promoter:getGuild()
    if not guild or guild:getId() ~= guildId then
        return false, "Você não pertence a esta guilda"
    end
    
    -- Verificar permissões
    local promoterRank = guild:getRankById(promoter:getGuildRank())
    local targetRank = guild:getRankById(target:getGuildRank())
    
    if not promoterRank or not targetRank then
        return false, "Rank não encontrado"
    end
    
    if promoterRank.level <= targetRank.level then
        return false, "Você não pode promover alguém de rank igual ou superior"
    end
    
    -- Encontrar próximo rank
    local ranks = guild:getRanks()
    local nextRank = nil
    
    for _, rank in ipairs(ranks) do
        if rank.level > targetRank.level and (not nextRank or rank.level < nextRank.level) then
            nextRank = rank
        end
    end
    
    if not nextRank then
        return false, "Não há rank superior disponível"
    end
    
    -- Promover
    if IOGuild.updateMemberRank(guildId, targetId, nextRank.id) then
        target:sendTextMessage(MESSAGE_INFO_DESCR, 
            string.format("Você foi promovido para %s na guilda '%s'", 
                nextRank.name, guild:getName()))
        
        return true, "Jogador promovido"
    else
        return false, "Erro ao promover jogador"
    end
end
```

#### **Nível Avançado**
```lua
-- Exemplo com sistema completo de hierarquia
local GuildHierarchyManager = {}
GuildHierarchyManager.__index = GuildHierarchyManager

function GuildHierarchyManager.new(guildId)
    local self = setmetatable({}, GuildHierarchyManager)
    self.guildId = guildId
    self.guild = IOGuild.loadGuildById(guildId)
    self.rankPermissions = {}
    self.rankHistory = {}
    return self
end

function GuildHierarchyManager:setupRankPermissions()
    -- Configurar permissões por rank
    self.rankPermissions = {
        [3] = { -- Leader
            canInvite = true,
            canKick = true,
            canPromote = true,
            canDemote = true,
            canChangeMotto = true,
            canChangeDescription = true,
            canManageRanks = true,
            canStartEvents = true
        },
        [2] = { -- Vice-Leader/Officer
            canInvite = true,
            canKick = true,
            canPromote = true,
            canDemote = false,
            canChangeMotto = false,
            canChangeDescription = false,
            canManageRanks = false,
            canStartEvents = true
        },
        [1] = { -- Member
            canInvite = false,
            canKick = false,
            canPromote = false,
            canDemote = false,
            canChangeMotto = false,
            canChangeDescription = false,
            canManageRanks = false,
            canStartEvents = false
        }
    }
end

function GuildHierarchyManager:checkPermission(playerId, permission)
    local player = Player(playerId)
    if not player then return false end
    
    local rank = self.guild:getRankById(player:getGuildRank())
    if not rank then return false end
    
    local permissions = self.rankPermissions[rank.level]
    return permissions and permissions[permission] or false
end

function GuildHierarchyManager:promoteMember(promoterId, targetId)
    if not self:checkPermission(promoterId, "canPromote") then
        return false, "Sem permissão para promover"
    end
    
    local target = Player(targetId)
    if not target then
        return false, "Jogador não encontrado"
    end
    
    local currentRank = self.guild:getRankById(target:getGuildRank())
    local nextRank = self:getNextRank(currentRank.level)
    
    if not nextRank then
        return false, "Não há rank superior disponível"
    end
    
    -- Registrar histórico
    self:logRankChange(targetId, currentRank.id, nextRank.id, "promotion", promoterId)
    
    -- Aplicar promoção
    if IOGuild.updateMemberRank(self.guildId, targetId, nextRank.id) then
        target:sendTextMessage(MESSAGE_INFO_DESCR, 
            string.format("Promovido para %s", nextRank.name))
        
        return true, "Promoção realizada"
    else
        return false, "Erro ao promover"
    end
end

function GuildHierarchyManager:demoteMember(demoterId, targetId)
    if not self:checkPermission(demoterId, "canDemote") then
        return false, "Sem permissão para rebaixar"
    end
    
    local target = Player(targetId)
    if not target then
        return false, "Jogador não encontrado"
    end
    
    local currentRank = self.guild:getRankById(target:getGuildRank())
    local previousRank = self:getPreviousRank(currentRank.level)
    
    if not previousRank then
        return false, "Não há rank inferior disponível"
    end
    
    -- Registrar histórico
    self:logRankChange(targetId, currentRank.id, previousRank.id, "demotion", demoterId)
    
    -- Aplicar rebaixamento
    if IOGuild.updateMemberRank(self.guildId, targetId, previousRank.id) then
        target:sendTextMessage(MESSAGE_INFO_DESCR, 
            string.format("Rebaixado para %s", previousRank.name))
        
        return true, "Rebaixamento realizado"
    else
        return false, "Erro ao rebaixar"
    end
end

function GuildHierarchyManager:getNextRank(currentLevel)
    local ranks = self.guild:getRanks()
    local nextRank = nil
    
    for _, rank in ipairs(ranks) do
        if rank.level > currentLevel and (not nextRank or rank.level < nextRank.level) then
            nextRank = rank
        end
    end
    
    return nextRank
end

function GuildHierarchyManager:getPreviousRank(currentLevel)
    local ranks = self.guild:getRanks()
    local previousRank = nil
    
    for _, rank in ipairs(ranks) do
        if rank.level < currentLevel and (not previousRank or rank.level > previousRank.level) then
            previousRank = rank
        end
    end
    
    return previousRank
end

function GuildHierarchyManager:logRankChange(playerId, oldRankId, newRankId, action, actorId)
    self.rankHistory[playerId] = self.rankHistory[playerId] or {}
    table.insert(self.rankHistory[playerId], {
        oldRankId = oldRankId,
        newRankId = newRankId,
        action = action,
        actorId = actorId,
        timestamp = os.time()
    })
end
```

---

## 🎓 **Lição Educacional: Sistema de Guildas em MMORPGs**

### **Conceitos Fundamentais**

#### **1. Hierarquia Organizacional**
- **Ranks**: Níveis de autoridade dentro da guilda
- **Permissões**: Capacidades específicas por rank
- **Responsabilidades**: Funções e deveres de cada nível

#### **2. Gestão de Membros**
- **Recrutamento**: Processo de adicionar novos membros
- **Promoções**: Avanço na hierarquia
- **Expulsões**: Remoção de membros problemáticos

#### **3. Funcionalidades Sociais**
- **Comunicação**: Chat específico da guilda
- **Eventos**: Atividades organizadas pela guilda
- **Colaboração**: Trabalho em equipe

### **Padrões de Design**

#### **1. Hierarchical Pattern**
```cpp
struct GuildRank {
    uint32_t id;
    std::string name;
    uint8_t level;  // Hierarquia numérica
};
```

#### **2. Permission Pattern**
```cpp
class GuildPermissions {
    std::map<uint8_t, std::set<std::string>> rankPermissions;
public:
    bool hasPermission(uint8_t rankLevel, const std::string &permission);
};
```

#### **3. Observer Pattern**
```cpp
class GuildObserver {
public:
    virtual void onMemberJoined(uint32_t playerId) = 0;
    virtual void onMemberLeft(uint32_t playerId) = 0;
    virtual void onRankChanged(uint32_t playerId, uint32_t newRankId) = 0;
};
```

---

## 🔍 **Insights Técnicos**

### **1. Otimizações Implementadas**

#### **Database Optimization**
- **Indexed Queries**: Índices otimizados para consultas frequentes
- **Batch Operations**: Operações em lote para múltiplos membros
- **Caching**: Cache de guildas frequentemente acessadas

#### **Memory Management**
- **Shared Pointers**: Uso consistente de `std::shared_ptr`
- **Weak References**: `std::weak_ptr` para referências circulares
- **Object Pooling**: Pool de objetos para ranks e membros

#### **Performance**
- **Lazy Loading**: Carregamento sob demanda de informações
- **Async Operations**: Operações assíncronas para I/O
- **Connection Pooling**: Pool de conexões de banco de dados

### **2. Integrações com Outros Sistemas**

#### **Sistema de Players**
- **Guild Assignment**: Associação de jogadores a guildas
- **Rank Management**: Gerenciamento de ranks dos jogadores
- **Permission Checking**: Verificação de permissões em tempo real

#### **Sistema de Communication**
- **Guild Chat**: Chat específico da guilda
- **Guild Messages**: Mensagens para todos os membros
- **Private Messages**: Mensagens privadas entre membros

#### **Sistema de Events**
- **Guild Events**: Eventos específicos da guilda
- **Guild Wars**: Guerras entre guildas
- **Guild Quests**: Quests específicas da guilda

### **3. Configuração e Customização**

#### **XML Configuration**
```xml
<guilds>
    <guild id="1" name="Test Guild" motto="Unity is Strength">
        <ranks>
            <rank id="1" name="Leader" level="3"/>
            <rank id="2" name="Vice-Leader" level="2"/>
            <rank id="3" name="Member" level="1"/>
        </ranks>
        <members>
            <member id="1" rank="1" joinDate="2025-01-01"/>
        </members>
    </guild>
</guilds>
```

#### **Lua Scripting**
- **Dynamic Guild Creation**: Criação dinâmica via Lua
- **Custom Ranks**: Ranks personalizados via scripts
- **Guild Events**: Eventos customizados da guilda

---

## 🚀 **Recomendações e Melhorias**

### **1. Otimizações Sugeridas**

#### **Advanced Caching**
```cpp
// Sistema de cache avançado para guildas
class GuildCache {
    std::unordered_map<uint32_t, std::shared_ptr<Guild>> guildCache;
    std::unordered_map<std::string, uint32_t> nameToIdCache;
    std::mutex cacheMutex;
    std::chrono::steady_clock::time_point lastCleanup;
    
public:
    std::shared_ptr<Guild> getGuild(uint32_t id);
    std::shared_ptr<Guild> getGuildByName(const std::string &name);
    void invalidateCache(uint32_t guildId);
    void cleanupExpiredEntries();
};
```

#### **Async Operations**
```cpp
// Operações assíncronas para guildas
class AsyncGuildOperations {
public:
    std::future<bool> createGuildAsync(const GuildConfig &config);
    std::future<bool> addMemberAsync(uint32_t guildId, uint32_t playerId, uint32_t rankId);
    std::future<std::vector<GuildMember>> getMembersAsync(uint32_t guildId);
};
```

#### **Event System**
```cpp
// Sistema de eventos para guildas
class GuildEventSystem {
public:
    void registerEvent(uint32_t guildId, const GuildEvent &event);
    void triggerEvent(uint32_t guildId, const std::string &eventType);
    void notifyMembers(uint32_t guildId, const std::string &message);
};
```

### **2. Funcionalidades Avançadas**

#### **Guild Alliances**
```cpp
// Sistema de alianças entre guildas
class GuildAlliance {
    std::vector<uint32_t> alliedGuilds;
    std::map<uint32_t, AlliancePermissions> permissions;
public:
    bool addAlly(uint32_t guildId);
    bool removeAlly(uint32_t guildId);
    bool hasAlly(uint32_t guildId) const;
};
```

#### **Guild Wars**
```cpp
// Sistema de guerras entre guildas
class GuildWar {
    uint32_t attackerGuildId;
    uint32_t defenderGuildId;
    WarStatus status;
    std::chrono::steady_clock::time_point startTime;
    std::chrono::steady_clock::time_point endTime;
public:
    void startWar();
    void endWar();
    void updateScore(uint32_t guildId, int points);
};
```

#### **Guild Quests**
```cpp
// Sistema de quests específicas da guilda
class GuildQuest {
    uint32_t questId;
    std::string name;
    std::string description;
    std::vector<QuestObjective> objectives;
    std::vector<QuestReward> rewards;
public:
    bool startQuest(uint32_t guildId);
    bool updateProgress(uint32_t guildId, uint32_t objectiveId, int progress);
    bool completeQuest(uint32_t guildId);
};
```

### **3. Analytics e Monitoramento**

#### **Guild Analytics**
```cpp
// Analytics para guildas
class GuildAnalytics {
public:
    void trackMemberActivity(uint32_t guildId, uint32_t playerId, const std::string &action);
    void generateGuildReport(uint32_t guildId);
    void analyzeGuildGrowth(uint32_t guildId);
    void trackGuildWars(uint32_t guildId);
};
```

#### **Performance Monitoring**
```cpp
// Monitoramento de performance
class GuildPerformanceMonitor {
public:
    void trackGuildLoadTime();
    void trackMemberOperationTime();
    void trackDatabaseQueryTime();
    void generatePerformanceReport();
};
```

---

## 📈 **Métricas e Estatísticas**

### **Complexidade do Sistema**
- **Classes Principais**: 3 (Guild, GuildRank, IOGuild)
- **Funções Lua**: 14 funções de guilda + 7 funções de player
- **Funções Game**: 7 funções de gerenciamento de guilda
- **Linhas de Código**: ~2,000 linhas (estimativa)

### **Integrações**
- **Sistemas Integrados**: 5 (Players, Communication, Events, Database, Lua)
- **APIs Expostas**: 21+ funções públicas
- **Configurações**: XML + Lua scripting

### **Performance**
- **Carregamento**: O(1) para guildas individuais
- **Busca**: O(log n) para busca por nome, O(1) para busca por ID
- **Memory**: ~2KB por guilda + overhead de membros e ranks

---

## 🎯 **Conclusão**

O Sistema de Guildas do Canary oferece uma solução robusta e escalável para organizações permanentes de jogadores. Com sua arquitetura modular, sistema de permissões granular e integração completa com outros sistemas, proporciona uma base sólida para funcionalidades sociais avançadas em MMORPGs.

### **Pontos Fortes**
- ✅ Hierarquia flexível e extensível
- ✅ Sistema de permissões granular
- ✅ Integração completa com outros sistemas
- ✅ Performance otimizada
- ✅ Suporte a scripting Lua

### **Áreas de Melhoria**
- 🔄 Sistema de alianças entre guildas
- 🔄 Guerras de guilda avançadas
- 🔄 Sistema de quests específicas
- 🔄 Analytics e monitoramento avançado

### **Impacto no Projeto**
Este sistema forma a base para organizações sociais permanentes, facilitando a colaboração entre jogadores e criando um senso de comunidade no MMORPG.

---

## 🔗 **Dependências**

### **Sistemas Relacionados**
- [[canary_fundamentos|Fundamentos do Canary]] - Base conceitual
- [[canary_sistema_grupos|Sistema de Grupos]] - Sistema base
- [[canary_sistema_raids|Sistema de Raids]] - Atividades de guilda
- [[canary_sistema_eventos|Sistema de Eventos]] - Eventos de guilda

### **Páginas Relacionadas**
- [[canary_sistema_grupos|Sistema de Grupos]] - Organizações temporárias
- [[canary_sistema_raids|Sistema de Raids]] - Atividades em grupo
- [[canary_sistema_eventos|Sistema de Eventos]] - Eventos organizados
- [[canary_sistema_condicoes|Sistema de Condições]] - Condições de guilda

---

## 📚 **Referências**

### **Código-Fonte**
- `canary/src/creatures/players/grouping/guild.hpp` - Definição de guildas
- `canary/src/creatures/players/grouping/guild.cpp` - Implementação de guildas
- `canary/src/io/ioguild.hpp` - Interface de I/O
- `canary/src/lua/functions/creatures/player/guild_functions.hpp` - Funções Lua

### **Documentação**
- [[habdel/CANARY-017|CANARY-017: Sistema de Guildas - Pesquisa Habdel]] - Pesquisa detalhada
- [[canary_sistema_grupos|Sistema de Grupos]] - Sistema base
- [[canary_fundamentos|Fundamentos do Canary]] - Conceitos base

### **Configuração**
- `canary/data/XML/guilds.xml` - Configuração de guildas
- `canary/data/XML/groups.xml` - Configuração de grupos

---

*Última atualização: 2025-08-05* 