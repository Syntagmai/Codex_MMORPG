
# Sistema de Protocolo de Comunicação OTClient

O OTClient implementa um sistema robusto de comunicação com servidores Tibia através de protocolos binários, suportando múltiplas versões (7.72 a 14.12) e extensões customizadas para funcionalidades avançadas.


---

## 📋 Índice 📋

1. [Visão Geral](#visão-geral)
2. [Arquitetura do Protocolo](#arquitetura-do-protocolo)
3. [ProtocolLogin](#protocollogin)
4. [ProtocolGame](#protocolgame)
5. [Sistema de Opcodes](#sistema-de-opcodes)
6. [Extended Opcodes](#extended-opcodes)
7. [Versões e Compatibilidade](#versões-e-compatibilidade)
8. [Mensagens e Serialização](#mensagens-e-serialização)
9. [Implementação Prática](#implementação-prática)
10. [Melhores Práticas](#melhores-práticas)


---

## 🎯 Visão Geral 🎯

O sistema de protocolo do OTClient oferece:

- **Multi-Versão**: Suporte para protocolos 7.72 até 14.12
- **Extensibilidade**: Extended opcodes para funcionalidades customizadas
- **Performance**: Processamento assíncrono e eficiente de mensagens
- **Flexibilidade**: Sistema de callbacks para interceptar e processar dados
- **Compatibilidade**: Funciona com TFS, Canary e servidores customizados

### 🏗️ **Arquitetura de Comunicação** 📝

```
Cliente                           Servidor
   │                                │
   ├─ ProtocolLogin ────────────────→ LoginServer
   │   │                            │
   │   ├─ Enviar credenciais        │
   │   ├─ Receber lista chars ←─────┤
   │   └─ Selecionar personagem     │
   │                                │
   ├─ ProtocolGame ─────────────────→ GameServer
   │   │                            │
   │   ├─ Game opcodes ←────────────→ Game opcodes
   │   ├─ Extended opcodes ←────────→ Extended opcodes
   │   └─ Mensagens binárias        │
   │                                │
```


---

## 🔐 ProtocolLogin 📋

Responsável pela autenticação e seleção de personagem no servidor de login.

### 🚀 **Processo de Login** 📝

```lua
-- Iniciar processo de login
    --  Iniciar processo de login (traduzido)
local protocolLogin = ProtocolLogin.create()

protocolLogin.onLoginError = function(protocol, error)
    print('Erro no login:', error)
end

protocolLogin.onCharacterList = function(protocol, characters, account)
    print('Personagens disponíveis:')
    for _, char in ipairs(characters) do
    -- Loop de repetição
        print('- ' .. char.name .. ' (Level ' .. char.level .. ')')
    end
end

protocolLogin.onUpdateNeeded = function(protocol, signature)
    print('Cliente desatualizado, assinatura:', signature)
end

-- Conectar ao servidor de login
    --  Conectar ao servidor de login (traduzido)
protocolLogin:login(
    'otserver.com',        -- host
    7171,                  -- porta
    'minha_conta',         -- nome da conta
    'minha_senha',         -- senha
    '',                    -- token autenticador
    false                  -- manter logado
)
```

### 📦 **Opcodes de Login** 📝

```lua
-- Opcodes do servidor de login
    --  Opcodes do servidor de login (traduzido)
LoginServerError = 10           -- Erro de login
LoginServerTokenSuccess = 12    -- Token aceito
LoginServerTokenError = 13      -- Token inválido
LoginServerMotd = 20           -- Mensagem do dia
LoginServerUpdateNeeded = 30    -- Cliente desatualizado
LoginServerSessionKey = 40      -- Chave de sessão
LoginServerCharacterList = 100  -- Lista de personagens
```

### 🔧 **Implementação de Login** 💻

#### Nível Basic
```lua
function ProtocolLogin:sendLoginPacket()
    local msg = OutputMessage.create()
    if g_game.getFeature(GameClientVersion) then
    end
    -- Adicionar dados da conta
    -- Token de autenticação (se presente)
    if string.len(self.authenticatorToken) > 0 then
        msg:addString(self.authenticatorToken)
    end
    self:send(msg)
end
function ProtocolLogin:parseCharacterList(msg)
    local characters = {}
    local charactersCount = msg:getU8()
        local character = {
    end
end
```

#### Nível Intermediate
```lua
function ProtocolLogin:sendLoginPacket()
    local msg = OutputMessage.create()
    msg:addU8(ClientOpcodes.ClientEnterAccount)
    msg:addU16(g_game.getOs())                    -- OS
    msg:addU16(g_game.getProtocolVersion())       -- Versão do protocolo
    
    if g_game.getFeature(GameClientVersion) then
        msg:addU32(g_game.getClientVersion())     -- Versão do cliente
    end
    
    -- Adicionar dados da conta
    msg:addString(self.accountName)
    msg:addString(self.accountPassword)
    
    -- Token de autenticação (se presente)
    if string.len(self.authenticatorToken) > 0 then
        msg:addString(self.authenticatorToken)
    end
    
    self:send(msg)
end

function ProtocolLogin:parseCharacterList(msg)
    local characters = {}
    local charactersCount = msg:getU8()
    
    for i = 1, charactersCount do
        local character = {
            name = msg:getString(),
            world = msg:getString(),
            worldPort = msg:getU16(),
            level = msg:getU16(),
            vocation = msg:getU8(),
            lookType = msg:getU16(),
            lookHead = msg:getU8(),
            lookBody = msg:getU8(),
            lookLegs = msg:getU8(),
            lookFeet = msg:getU8(),
            lookAddons = msg:getU8()
        }
        table.insert(characters, character)
    end
    
    signalcall(self.onCharacterList, self, characters)
end
```

#### Nível Advanced
```lua
function ProtocolLogin:sendLoginPacket()
    local msg = OutputMessage.create()
    msg:addU8(ClientOpcodes.ClientEnterAccount)
    msg:addU16(g_game.getOs())                    -- OS
    msg:addU16(g_game.getProtocolVersion())       -- Versão do protocolo
    
    if g_game.getFeature(GameClientVersion) then
        msg:addU32(g_game.getClientVersion())     -- Versão do cliente
    end
    
    -- Adicionar dados da conta
    msg:addString(self.accountName)
    msg:addString(self.accountPassword)
    
    -- Token de autenticação (se presente)
    if string.len(self.authenticatorToken) > 0 then
        msg:addString(self.authenticatorToken)
    end
    
    self:send(msg)
end

function ProtocolLogin:parseCharacterList(msg)
    local characters = {}
    local charactersCount = msg:getU8()
    
    for i = 1, charactersCount do
        local character = {
            name = msg:getString(),
            world = msg:getString(),
            worldPort = msg:getU16(),
            level = msg:getU16(),
            vocation = msg:getU8(),
            lookType = msg:getU16(),
            lookHead = msg:getU8(),
            lookBody = msg:getU8(),
            lookLegs = msg:getU8(),
            lookFeet = msg:getU8(),
            lookAddons = msg:getU8()
        }
        table.insert(characters, character)
    end
    
    signalcall(self.onCharacterList, self, characters)
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

## 🎮 ProtocolGame 📋

Gerencia toda a comunicação durante o jogo, incluindo movimento, chat, ações e eventos.

### 🔄 **Ciclo de Vida do ProtocolGame** 📝

```lua
-- Conectar ao servidor de jogo
    --  Conectar ao servidor de jogo (traduzido)
local protocolGame = ProtocolGame.create()

-- Configurar callbacks
    --  Configurar callbacks (traduzido)
protocolGame.onConnectionError = function(protocol, error, code)
    print('Erro de conexão:', error, code)
end

protocolGame.onGameStart = function(protocol)
    print('Jogo iniciado!')
end

protocolGame.onGameEnd = function(protocol)
    print('Jogo finalizado!')
end

-- Login no servidor de jogo
    --  Login no servidor de jogo (traduzido)
protocolGame:loginWorld(
    'game.otserver.com',   -- host do jogo
    7172,                  -- porta do jogo
    'Meu Char',           -- nome do personagem
    'account_name',        -- conta
    'password',            -- senha
    ''                     -- token
)
```

### 📨 **Enviando Comandos** 📝

```lua
-- Movimento
    --  Movimento (traduzido)
protocolGame:sendWalkNorth()
protocolGame:sendWalkEast()
protocolGame:sendAutoWalk({Otc.North, Otc.East, Otc.South})

-- Chat
    --  Chat (traduzido)
protocolGame:sendTalk(Otc.MessageSay, 0, '', 'Olá mundo!')
protocolGame:sendTalk(Otc.MessageWhisper, 0, '', 'Sussurro')
protocolGame:sendTalk(Otc.MessagePrivateTo, 0, 'Player', 'Mensagem privada')

-- Ações com itens
protocolGame:sendUseItem(position, itemId, stackPos, index)
protocolGame:sendMove(fromPos, itemId, stackPos, toPos, count)
protocolGame:sendLook(position, itemId, stackPos)

-- Combat
    --  Combat (traduzido)
protocolGame:sendAttack(creatureId, seq)
protocolGame:sendFollow(creatureId, seq)
protocolGame:sendCancelAttackAndFollow()

-- Interface
    --  Interface (traduzido)
protocolGame:sendCloseContainer(containerId)
protocolGame:sendOpenOwnChannel()
protocolGame:sendRequestChannels()
```

### 📥 **Processando Respostas** 📝

```lua
-- Registrar callbacks para opcodes específicos
ProtocolGame.registerOpcode(GameServerFullMap, function(protocol, msg)
    local mapDescription = msg:getString()
    g_map.loadMap(mapDescription)
end)

ProtocolGame.registerOpcode(GameServerTextMessage, function(protocol, msg)
    local messageType = msg:getU8()
    local message = msg:getString()
    
    if messageType == MessageTypes.StatusDefault then
    -- Verificação condicional
        g_game.processTextMessage(messageType, message)
    end
end)

ProtocolGame.registerOpcode(GameServerCreatureSay, function(protocol, msg)
    local statementId = msg:getU32()
    local name = msg:getString()
    local level = msg:getU16()
    local messageType = msg:getU8()
    local channelId = 0
    
    if messageType == MessageTypes.ChannelYellow then
    -- Verificação condicional
        channelId = msg:getU16()
    end
    
    local message = msg:getString()
    
    g_game.processCreatureSay(name, level, messageType, message, channelId, statementId)
end)
```


---

## 🔢 Sistema de Opcodes ⚙️

Opcodes são códigos únicos que identificam o tipo de mensagem sendo enviada ou recebida.

### 📤 **Client Opcodes (Enviados pelo Cliente)** 📝

```lua
ClientOpcodes = {
    -- Login
    --  Login (traduzido)
    ClientEnterAccount = 1,
    ClientEnterGame = 10,
    ClientLeaveGame = 20,
    
    -- Movimento
    --  Movimento (traduzido)
    ClientAutoWalk = 100,
    ClientWalkNorth = 101,
    ClientWalkEast = 102,
    ClientWalkSouth = 103,
    ClientWalkWest = 104,
    ClientStop = 105,
    ClientWalkNorthEast = 106,
    ClientWalkSouthEast = 107,
    ClientWalkSouthWest = 108,
    ClientWalkNorthWest = 109,
    ClientTurnNorth = 111,
    ClientTurnEast = 112,
    ClientTurnSouth = 113,
    ClientTurnWest = 114,
    
    -- Ações
    ClientMove = 120,
    ClientInspectNpcTrade = 121,
    ClientBuyItem = 122,
    ClientSellItem = 123,
    ClientCloseNpcTrade = 124,
    ClientRequestTrade = 125,
    ClientLook = 126,
    ClientLookCreature = 127,
    ClientTalk = 150,
    ClientRequestChannels = 151,
    ClientJoinChannel = 152,
    ClientLeaveChannel = 153,
    ClientOpenPrivateChannel = 154,
    ClientOpenOwnChannel = 155,
    ClientCloseOwnChannel = 156,
    
    -- Extended Opcodes
    --  Extended Opcodes (traduzido)
    ClientExtendedOpcode = 50
}
```

### 📥 **Server Opcodes (Recebidos do Servidor)** 📝

```lua
GameServerOpcodes = {
    -- Estados do jogo
    --  Estados do jogo (traduzido)
    GameServerLoginOrPendingState = 10,
    GameServerEnterGame = 15,
    GameServerLoginError = 20,
    GameServerPing = 30,
    GameServerPingBack = 29,
    GameServerChallenge = 31,
    GameServerDeath = 40,
    
    -- Extended Opcodes
    --  Extended Opcodes (traduzido)
    GameServerExtendedOpcode = 50,
    
    -- Mapa
    --  Mapa (traduzido)
    GameServerFullMap = 100,
    GameServerMapTopRow = 101,
    GameServerMapRightRow = 102,
    GameServerMapBottomRow = 103,
    GameServerMapLeftRow = 104,
    GameServerUpdateTile = 105,
    GameServerCreateOnMap = 106,
    GameServerChangeOnMap = 107,
    GameServerDeleteOnMap = 108,
    GameServerMoveCreature = 109,
    
    -- Containers
    --  Containers (traduzido)
    GameServerOpenContainer = 110,
    GameServerCloseContainer = 111,
    GameServerCreateContainer = 112,
    GameServerChangeInContainer = 113,
    GameServerDeleteInContainer = 114,
    
    -- Inventário
    GameServerSetInventory = 120,
    GameServerDeleteInventory = 121,
    
    -- Chat
    --  Chat (traduzido)
    GameServerCreatureSay = 170,
    GameServerChannelList = 171,
    GameServerOpenChannel = 172,
    GameServerTextMessage = 180,
    
    -- Stats
    --  Stats (traduzido)
    GameServerStats = 160,
    GameServerSkills = 161,
    GameServerPlayerConditions = 162,
    GameServerCancelTarget = 163,
    GameServerSpellDelay = 164,
    GameServerSpellGroupDelay = 165,
    GameServerMultiUseDelay = 166
}
```


---

## 🔧 Extended Opcodes 📋

Sistema extensivo para comunicação customizada entre cliente e servidor.

### 📡 **Registrando Extended Opcodes** 📝

```lua
-- No cliente: registrar handler para extended opcode
    --  No cliente: registrar handler para extended opcode (traduzido)
ProtocolGame.registerExtendedOpcode(100, function(protocol, opcode, buffer)
    local data = json.decode(buffer)
    
    if data.action == 'updateHealth' then
    -- Verificação condicional
        local health = data.health
        local maxHealth = data.maxHealth
        g_game.getLocalPlayer():setHealth(health, maxHealth)
        
    elseif data.action == 'showNotification' then
        local message = data.message
        local type = data.type or 'info'
        showNotification(message, type)
        
    elseif data.action == 'openCustomWindow' then
        local windowData = data.windowData
        openCustomWindow(windowData)
    end
end)

-- Enviar extended opcode para o servidor
    --  Enviar extended opcode para o servidor (traduzido)
local function sendCustomData(action, data)
    local payload = {
        action = action,
        data = data,
        timestamp = os.time()
    }
    
    local jsonString = json.encode(payload)
    protocolGame:sendExtendedOpcode(100, jsonString)
end

-- Uso
    --  Uso (traduzido)
sendCustomData('requestPlayerInfo', {playerId = 12345})
sendCustomData('updateSetting', {setting = 'pvpMode', value = true})
```

### 🔄 **Extended Opcodes com JSON** 📝

```lua
-- Sistema robusto para mensagens JSON grandes
    --  Sistema robusto para mensagens JSON grandes (traduzido)
ProtocolGame.registerExtendedJSONOpcode(101, function(protocol, opcode, jsonData)
    -- jsonData já é um objeto Lua (decodificado automaticamente)
    
    if jsonData.type == 'mapData' then
    -- Verificação condicional
        local mapInfo = jsonData.payload
        processMapData(mapInfo)
        
    elseif jsonData.type == 'questUpdate' then
        local questInfo = jsonData.payload
        updateQuestLog(questInfo)
        
    elseif jsonData.type == 'guildInfo' then
        local guildData = jsonData.payload
        updateGuildInterface(guildData)
    end
end)

-- O sistema automaticamente lida com:
    --  O sistema automaticamente lida com: (traduzido)
-- - Mensagens muito grandes (divide em partes)
    --  - Mensagens muito grandes (divide em partes) (traduzido)
-- - Validação JSON
-- - Reagrupamento de mensagens fragmentadas
    --  - Reagrupamento de mensagens fragmentadas (traduzido)
```

### 📦 **Exemplos de Extended Opcodes** 🎮

```lua
-- Opcode 80: Sistema de Quests Customizado
    --  Opcode 80: Sistema de Quests Customizado (traduzido)
ProtocolGame.registerExtendedOpcode(80, function(protocol, opcode, buffer)
    local questData = json.decode(buffer)
    
    if questData.action == 'questStarted' then
    -- Verificação condicional
        QuestSystem.startQuest(questData.questId, questData.questData)
        
    elseif questData.action == 'questCompleted' then
        QuestSystem.completeQuest(questData.questId, questData.reward)
        
    elseif questData.action == 'questProgress' then
        QuestSystem.updateProgress(questData.questId, questData.progress)
    end
end)

-- Opcode 81: Sistema de Loja Customizada
    --  Opcode 81: Sistema de Loja Customizada (traduzido)
ProtocolGame.registerExtendedOpcode(81, function(protocol, opcode, buffer)
    local shopData = json.decode(buffer)
    
    if shopData.action == 'openShop' then
    -- Verificação condicional
        CustomShop.open(shopData.items, shopData.categories)
        
    elseif shopData.action == 'purchaseResult' then
        CustomShop.handlePurchaseResult(shopData.success, shopData.message)
    end
end)

-- Opcode 82: Sistema de Partículas/Efeitos
ProtocolGame.registerExtendedOpcode(82, function(protocol, opcode, buffer)
    local effectData = json.decode(buffer)
    
    if effectData.action == 'playEffect' then
    -- Verificação condicional
        local position = effectData.position
        local effectId = effectData.effectId
        local duration = effectData.duration
        
        EffectSystem.playEffect(position, effectId, duration)
        
    elseif effectData.action == 'stopEffect' then
        EffectSystem.stopEffect(effectData.effectId)
    end
end)
```


---

## 🔖 Versões e Compatibilidade 📋

O OTClient suporta múltiplas versões do protocolo Tibia.

### 📊 **Versões Suportadas** 📝

#### Nível Basic
```lua
-- Versões principais suportadas
local supportedVersions = {
    772,   -- 7.72 (Nostalrius, TFS Downgrade)
    860,   -- 8.60 (TFS 0.4, clássico)
    1098,  -- 10.98 (TFS 1.4.2, estável)
    1300,  -- 13.00 (TFS 1.6, moderna)
    1321,  -- 13.21 (Canary)
    1340,  -- 13.40 (Canary atual)
    1412   -- 14.12 (Mais recente)
}

-- Verificar versão atual
local currentVersion = g_game.getClientVersion()
local protocolVersion = g_game.getProtocolVersion()

print('Versão do cliente:', currentVersion)
print('Versão do protocolo:', protocolVersion)
```

#### Nível Intermediate
```lua
-- Versões principais suportadas
local supportedVersions = {
    772,   -- 7.72 (Nostalrius, TFS Downgrade)
    860,   -- 8.60 (TFS 0.4, clássico)
    1098,  -- 10.98 (TFS 1.4.2, estável)
    1300,  -- 13.00 (TFS 1.6, moderna)
    1321,  -- 13.21 (Canary)
    1340,  -- 13.40 (Canary atual)
    1412   -- 14.12 (Mais recente)
}

-- Verificar versão atual
local currentVersion = g_game.getClientVersion()
local protocolVersion = g_game.getProtocolVersion()

print('Versão do cliente:', currentVersion)
print('Versão do protocolo:', protocolVersion)
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
-- Versões principais suportadas
local supportedVersions = {
    772,   -- 7.72 (Nostalrius, TFS Downgrade)
    860,   -- 8.60 (TFS 0.4, clássico)
    1098,  -- 10.98 (TFS 1.4.2, estável)
    1300,  -- 13.00 (TFS 1.6, moderna)
    1321,  -- 13.21 (Canary)
    1340,  -- 13.40 (Canary atual)
    1412   -- 14.12 (Mais recente)
}

-- Verificar versão atual
local currentVersion = g_game.getClientVersion()
local protocolVersion = g_game.getProtocolVersion()

print('Versão do cliente:', currentVersion)
print('Versão do protocolo:', protocolVersion)
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

### 🔧 **Features por Versão** 📝

#### Nível Basic
```lua
-- Sistema de features baseado na versão
local function checkFeatures()
    if g_game.getFeature(GameProtocolChecksum) then
        print('Suporte a checksum de protocolo')
    end
    
    if g_game.getFeature(GameAccountNames) then
        print('Login com nome de conta')
    end
    
    if g_game.getFeature(GameExtendedOpcode) then
        print('Suporte a extended opcodes')
    end
    
    if g_game.getFeature(GameLoginPending) then
        print('Estado de login pendente')
    end
    
    if g_game.getFeature(GameNewSpeedLaw) then
        print('Nova fórmula de velocidade')
    end
end

-- Adaptação baseada na versão
local function adaptToVersion()
    local version = g_game.getClientVersion()
    
    if version >= 1300 then
        -- Recursos modernos disponíveis
        enableModernFeatures()
    elseif version >= 1000 then
        -- Recursos intermediários
        enableStandardFeatures()
    else
        -- Versão clássica
        enableClassicFeatures()
    end
end
```

#### Nível Intermediate
```lua
-- Sistema de features baseado na versão
local function checkFeatures()
    if g_game.getFeature(GameProtocolChecksum) then
        print('Suporte a checksum de protocolo')
    end
    
    if g_game.getFeature(GameAccountNames) then
        print('Login com nome de conta')
    end
    
    if g_game.getFeature(GameExtendedOpcode) then
        print('Suporte a extended opcodes')
    end
    
    if g_game.getFeature(GameLoginPending) then
        print('Estado de login pendente')
    end
    
    if g_game.getFeature(GameNewSpeedLaw) then
        print('Nova fórmula de velocidade')
    end
end

-- Adaptação baseada na versão
local function adaptToVersion()
    local version = g_game.getClientVersion()
    
    if version >= 1300 then
        -- Recursos modernos disponíveis
        enableModernFeatures()
    elseif version >= 1000 then
        -- Recursos intermediários
        enableStandardFeatures()
    else
        -- Versão clássica
        enableClassicFeatures()
    end
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
-- Sistema de features baseado na versão
local function checkFeatures()
    if g_game.getFeature(GameProtocolChecksum) then
        print('Suporte a checksum de protocolo')
    end
    
    if g_game.getFeature(GameAccountNames) then
        print('Login com nome de conta')
    end
    
    if g_game.getFeature(GameExtendedOpcode) then
        print('Suporte a extended opcodes')
    end
    
    if g_game.getFeature(GameLoginPending) then
        print('Estado de login pendente')
    end
    
    if g_game.getFeature(GameNewSpeedLaw) then
        print('Nova fórmula de velocidade')
    end
end

-- Adaptação baseada na versão
local function adaptToVersion()
    local version = g_game.getClientVersion()
    
    if version >= 1300 then
        -- Recursos modernos disponíveis
        enableModernFeatures()
    elseif version >= 1000 then
        -- Recursos intermediários
        enableStandardFeatures()
    else
        -- Versão clássica
        enableClassicFeatures()
    end
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

## 📨 Mensagens e Serialização 📋

Sistema para construir e ler mensagens binárias do protocolo.

### 📤 **OutputMessage (Enviar Dados)** 📝

```lua
-- Criar mensagem para envio
    --  Criar mensagem para envio (traduzido)
local msg = OutputMessage.create()

-- Adicionar dados básicos
msg:addU8(255)              -- Byte (0-255)
msg:addU16(65535)           -- Short (0-65535)
msg:addU32(4294967295)      -- Int (0-4294967295)
msg:addU64(1234567890)      -- Long

-- Adicionar strings
    --  Adicionar strings (traduzido)
msg:addString('Olá mundo')  -- String com comprimento
msg:addPaddingBytes(4, 0)   -- Padding bytes

-- Adicionar posição
local pos = {x = 1000, y = 1000, z = 7}
msg:addPosition(pos)

-- Adicionar dados customizados
    --  Adicionar dados customizados (traduzido)
msg:addDouble(3.14159)      -- Double precision
msg:addFloat(2.71)          -- Float

-- Enviar mensagem
    --  Enviar mensagem (traduzido)
protocolGame:send(msg)
```

### 📥 **InputMessage (Receber Dados)** 📝

```lua
-- Processar mensagem recebida
    --  Processar mensagem recebida (traduzido)
function parseCustomMessage(protocol, msg)
    -- Função: parseCustomMessage
    -- Ler dados na mesma ordem que foram escritos
    --  Ler dados na mesma ordem que foram escritos (traduzido)
    local opcode = msg:getU8()
    local playerId = msg:getU32()
    local playerName = msg:getString()
    local position = msg:getPosition()
    local health = msg:getU16()
    local maxHealth = msg:getU16()
    
    -- Verificar se ainda há dados
    if not msg:eof() then
    -- Verificação condicional
        local additionalData = msg:getString()
        print('Dados adicionais:', additionalData)
    end
    
    -- Processar dados
    --  Processar dados (traduzido)
    local player = g_game.getCreatureById(playerId)
    if player then
    -- Verificação condicional
        player:setHealthPercent((health / maxHealth) * 100)
    end
end

-- Ler arrays
    --  Ler arrays (traduzido)
function parseItemList(msg)
    -- Função: parseItemList
    local itemCount = msg:getU8()
    local items = {}
    
    for i = 1, itemCount do
    -- Loop de repetição
        local item = {
            id = msg:getU16(),
            count = msg:getU8(),
            name = msg:getString()
        }
        table.insert(items, item)
    end
    
    return items
end
```

### 🔒 **Validação e Segurança** 📝

```lua
-- Validação de mensagens
function safeParseMessage(protocol, msg)
    -- Função: safeParseMessage
    if msg:getMessageSize() < 10 then
    -- Verificação condicional
        error('Mensagem muito pequena')
        return
    end
    
    local messageType = msg:getU8()
    
    -- Verificar tipo válido
    if messageType < 1 or messageType > 100 then
    -- Verificação condicional
        error('Tipo de mensagem inválido: ' .. messageType)
        return
    end
    
    -- Processar conforme o tipo
    --  Processar conforme o tipo (traduzido)
    if messageType == 1 then
    -- Verificação condicional
        parsePlayerUpdate(msg)
    elseif messageType == 2 then
        parseInventoryUpdate(msg)
    else
        print('Tipo de mensagem não implementado:', messageType)
    end
end

-- Rate limiting para extended opcodes
    --  Rate limiting para extended opcodes (traduzido)
local opcodeTimestamps = {}
local OPCODE_COOLDOWN = 100 -- ms

function rateLimitedExtendedOpcode(opcode, callback)
    -- Função: rateLimitedExtendedOpcode
    return function(protocol, opcode, buffer)
        local now = g_clock.millis()
        local lastCall = opcodeTimestamps[opcode] or 0
        
        if now - lastCall < OPCODE_COOLDOWN then
    -- Verificação condicional
            print('Rate limit atingido para opcode:', opcode)
            return
        end
        
        opcodeTimestamps[opcode] = now
        callback(protocol, opcode, buffer)
    end
end

-- Usar
    --  Usar (traduzido)
ProtocolGame.registerExtendedOpcode(100, 
    rateLimitedExtendedOpcode(100, handleCustomOpcode))
```


---

## 💡 Implementação Prática 📋

### 🎮 **Sistema de Chat Customizado** 📝

```lua
local CustomChat = {}

function CustomChat.init()
    -- Função: CustomChat
    -- Interceptar mensagens de chat
    --  Interceptar mensagens de chat (traduzido)
    ProtocolGame.registerOpcode(GameServerCreatureSay, function(protocol, msg)
        local name = msg:getString()
        local level = msg:getU16()
        local messageType = msg:getU8()
        local message = msg:getString()
        
        -- Processar comandos especiais
    --  Processar comandos especiais (traduzido)
        if message:starts('/custom ') then
    -- Verificação condicional
            CustomChat.handleCustomCommand(name, message:sub(9))
            return -- Não processar normalmente
        end
        
        -- Processar normalmente
    --  Processar normalmente (traduzido)
        g_game.processCreatureSay(name, level, messageType, message)
    end)
    
    -- Extended opcode para chat avançado
    ProtocolGame.registerExtendedOpcode(90, function(protocol, opcode, buffer)
        local chatData = json.decode(buffer)
        CustomChat.handleAdvancedChat(chatData)
    end)
end

function CustomChat.sendFormattedMessage(message, color, style)
    -- Função: CustomChat
    local data = {
        action = 'formattedMessage',
        message = message,
        color = color,
        style = style
    }
    
    protocolGame:sendExtendedOpcode(90, json.encode(data))
end

function CustomChat.handleCustomCommand(playerName, command)
    -- Função: CustomChat
    if command == 'time' then
    -- Verificação condicional
        local timeStr = os.date('%H:%M:%S')
        CustomChat.sendFormattedMessage('Hora atual: ' .. timeStr, '#00ff00', 'bold')
    elseif command == 'players' then
        local count = #g_map.getCreatures()
        CustomChat.sendFormattedMessage('Jogadores online: ' .. count, '#ffff00', 'italic')
    end
end
```

### 📊 **Sistema de Estatísticas Avançado** 📝

```lua
local AdvancedStats = {}

function AdvancedStats.init()
    -- Função: AdvancedStats
    -- Interceptar atualizações de stats
    ProtocolGame.registerOpcode(GameServerStats, function(protocol, msg)
        local health = msg:getU16()
        local maxHealth = msg:getU16()
        local freeCapacity = msg:getU32()
        local experience = msg:getU64()
        local level = msg:getU16()
        local levelPercent = msg:getU8()
        local mana = msg:getU16()
        local maxMana = msg:getU16()
        local magicLevel = msg:getU8()
        local magicLevelPercent = msg:getU8()
        local soul = msg:getU8()
        local stamina = msg:getU16()
        
        -- Atualizar interface customizada
    --  Atualizar interface customizada (traduzido)
        AdvancedStats.updateDisplay({
            health = health,
            maxHealth = maxHealth,
            mana = mana,
            maxMana = maxMana,
            level = level,
            experience = experience,
            stamina = stamina
        })
    end)
    
    -- Opcode para stats extras
    --  Opcode para stats extras (traduzido)
    ProtocolGame.registerExtendedOpcode(85, function(protocol, opcode, buffer)
        local extraStats = json.decode(buffer)
        AdvancedStats.updateExtraStats(extraStats)
    end)
end

function AdvancedStats.requestDetailedStats()
    -- Função: AdvancedStats
    protocolGame:sendExtendedOpcode(85, json.encode({
        action = 'requestStats',
        details = {'damage', 'defense', 'speed', 'regeneration'}
    }))
end
```


---

## ✅ Melhores Práticas 📋

### 🛡️ **Segurança** 📝

```lua
-- ✅ BOM: Validar dados recebidos
    --  ✅ BOM: Validar dados recebidos (traduzido)
function safeExtendedOpcode(protocol, opcode, buffer)
    -- Função: safeExtendedOpcode
    if not buffer or buffer:len() == 0 then
    -- Verificação condicional
        return
    end
    
    local success, data = pcall(json.decode, buffer)
    if not success then
    -- Verificação condicional
        print('JSON inválido recebido')
        return
    end
    
    if type(data) ~= 'table' then
    -- Verificação condicional
        print('Dados em formato inválido')
        return
    end
    
    -- Processar dados seguros
    --  Processar dados seguros (traduzido)
    processValidData(data)
end

-- ❌ EVITE: Processar dados sem validação
function unsafeExtendedOpcode(protocol, opcode, buffer)
    -- Função: unsafeExtendedOpcode
    local data = json.decode(buffer) -- Pode falhar
    processData(data.someField)      -- Pode ser nil
end
```

### ⚡ **Performance** 📝

```lua
-- ✅ BOM: Cache para lookups frequentes
    --  ✅ BOM: Cache para lookups frequentes (traduzido)
local opcodeCache = {}

function registerOptimizedOpcode(opcode, callback)
    -- Função: registerOptimizedOpcode
    opcodeCache[opcode] = callback
    ProtocolGame.registerOpcode(opcode, callback)
end

-- ✅ BOM: Batch processing para múltiplas mensagens
local messageQueue = {}
local processingTimer = nil

function queueMessage(message)
    -- Função: queueMessage
    table.insert(messageQueue, message)
    
    if not processingTimer then
    -- Verificação condicional
        processingTimer = scheduleEvent(processMessageQueue, 10)
    end
end

function processMessageQueue()
    -- Função: processMessageQueue
    for _, message in ipairs(messageQueue) do
    -- Loop de repetição
        processMessage(message)
    end
    messageQueue = {}
    processingTimer = nil
end
```

### 🔧 **Debugging** 📝

```lua
-- Sistema de debug para protocolo
    --  Sistema de debug para protocolo (traduzido)
local ProtocolDebugger = {}
ProtocolDebugger.enabled = false
ProtocolDebugger.loggedOpcodes = {}

function ProtocolDebugger.enable()
    -- Função: ProtocolDebugger
    ProtocolDebugger.enabled = true
    
    -- Interceptar todos os opcodes
    --  Interceptar todos os opcodes (traduzido)
    for opcode = 1, 255 do
    -- Loop de repetição
        ProtocolGame.registerOpcode(opcode, function(protocol, msg)
            if ProtocolDebugger.enabled then
    -- Verificação condicional
                ProtocolDebugger.logOpcode(opcode, msg:getMessageSize())
            end
        end)
    end
end

function ProtocolDebugger.logOpcode(opcode, size)
    -- Função: ProtocolDebugger
    local info = {
        opcode = opcode,
        size = size,
        timestamp = os.time()
    }
    
    table.insert(ProtocolDebugger.loggedOpcodes, info)
    print(string.format('[PROTOCOL] Opcode %d, Size: %d bytes', opcode, size))
end

-- Usar durante desenvolvimento
    --  Usar durante desenvolvimento (traduzido)
-- ProtocolDebugger.enable()
    --  ProtocolDebugger.enable() (traduzido)
```

O sistema de protocolo do OTClient oferece flexibilidade máxima para comunicação cliente-servidor robusta e extensível. Use as práticas recomendadas para garantir segurança, performance e compatibilidade.

---

> [!success] Navegação
> - [[Getting_Started_Guide]] - Comece aqui
> - [[Module_System_Guide]] - Desenvolvimento de módulos
> - [[UI_System_Guide]] - Interface do usuário
> - [[Lua_API_Reference]] - Referência completa da API

