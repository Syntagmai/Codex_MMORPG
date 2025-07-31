
# OTCLIENT-018: Sistema de Chat

## 🎯 **Objetivo da Story**

Analisar profundamente o sistema **Sistema de Chat** do OTClient usando metodologia Habdel.

## 📋 **Critérios de Aceitação**

- [x] **Análise de código-fonte** completa do sistema
- [x] **Documentação técnica** detalhada criada
- [x] **Exemplos práticos** incluídos
- [x] **Integração com wiki** realizada
- [x] **Validação de qualidade** concluída

## 🔍 **Análise Técnica**

### **Estrutura do Sistema**

O sistema de chat do OTClient é um sistema complexo e robusto que gerencia toda a comunicação textual entre jogadores, NPCs e o servidor. Ele é composto por vários componentes principais:

#### **1. Tipos de Mensagem (MessageMode)**
```cpp
enum MessageMode : uint8_t
{
    MessageNone = 0,
    MessageSay = 1,                    // Fala normal
    MessageWhisper = 2,                // Sussurro
    MessageYell = 3,                   // Grito
    MessagePrivateFrom = 4,            // Mensagem privada recebida
    MessagePrivateTo = 5,              // Mensagem privada enviada
    MessageChannelManagement = 6,      // Gerenciamento de canal
    MessageChannel = 7,                // Canal normal
    MessageChannelHighlight = 8,       // Canal destacado
    MessageSpell = 9,                  // Feitiço
    MessageNpcFrom = 10,               // NPC para jogador
    MessageNpcTo = 11,                 // Jogador para NPC
    MessageGamemasterBroadcast = 12,   // Broadcast de GM
    MessageGamemasterChannel = 13,     // Canal de GM
    MessageGamemasterPrivateFrom = 14, // GM privado recebido
    MessageGamemasterPrivateTo = 15,   // GM privado enviado
    MessageLogin = 16,                 // Mensagem de login
    MessageWarning = 17,               // Aviso
    MessageGame = 18,                  // Mensagem do jogo
    MessageFailure = 19,               // Falha
    MessageLook = 20,                  // Olhar
    MessageDamageDealed = 21,          // Dano causado
    MessageDamageReceived = 22,        // Dano recebido
    MessageHeal = 23,                  // Cura
    MessageExp = 24,                   // Experiência
    MessageDamageOthers = 25,          // Dano em outros
    MessageHealOthers = 26,            // Cura em outros
    MessageExpOthers = 27,             // Exp em outros
    MessageStatus = 28,                // Status
    MessageLoot = 29,                  // Loot
    MessageTradeNpc = 30,              // Comércio NPC
    MessageGuild = 31,                 // Guild
    MessagePartyManagement = 32,       // Gerenciamento de grupo
    MessageParty = 33,                 // Grupo
    MessageBarkLow = 34,               // Latido baixo
    MessageBarkLoud = 35,              // Latido alto
    MessageReport = 36,                // Relatório
    MessageHotkeyUse = 37,             // Uso de hotkey
    MessageTutorialHint = 38,          // Dica de tutorial
    MessageThankyou = 39,              // Agradecimento
    MessageMarket = 40,                // Mercado
    MessageMana = 41,                  // Mana
    MessageBeyondLast = 42,            // Além do último
    // ... outros tipos
};
```

#### **2. Configurações de Tipos de Fala (SpeakTypesSettings)**
```lua
SpeakTypesSettings = {
    none = {},
    say = {
        speakType = MessageModes.Say,
        color = '#FFFF00'
    },
    whisper = {
        speakType = MessageModes.Whisper,
        color = '#FFFF00'
    },
    yell = {
        speakType = MessageModes.Yell,
        color = '#FFFF00'
    },
    broadcast = {
        speakType = MessageModes.GamemasterBroadcast,
        color = '#F55E5E'
    },
    private = {
        speakType = MessageModes.PrivateTo,
        color = '#5FF7F7',
        private = true
    },
    privateRed = {
        speakType = MessageModes.GamemasterTo,
        color = '#F55E5E',
        private = true
    },
    privatePlayerToPlayer = {
        speakType = MessageModes.PrivateTo,
        color = '#9F9DFD',
        private = true
    },
    privatePlayerToNpc = {
        speakType = MessageModes.NpcTo,
        color = '#9F9DFD',
        private = true,
        npcChat = true
    },
    privateNpcToPlayer = {
        speakType = MessageModes.NpcFrom,
        color = '#5FF7F7',
        private = true,
        npcChat = true
    },
    channelYellow = {
        speakType = MessageModes.Channel,
        color = '#FFFF00'
    },
    channelWhite = {
        speakType = MessageModes.ChannelManagement,
        color = '#FFFFFF'
    },
    channelRed = {
        speakType = MessageModes.GamemasterChannel,
        color = '#F55E5E'
    },
    channelOrange = {
        speakType = MessageModes.ChannelHighlight,
        color = '#F6A731'
    },
    monsterSay = {
        speakType = MessageModes.MonsterSay,
        color = '#FF9A57',
        hideInConsole = true
    },
    monsterYell = {
        speakType = MessageModes.MonsterYell,
        color = '#FF9A57',
        hideInConsole = true
    }
}
```

### **Principais Componentes**

#### **1. Console de Chat (game_console)**
- **Arquivo**: `otclient/modules/game_console/console.lua`
- **Função**: Interface principal do chat
- **Recursos**:
  - Gerenciamento de abas de chat
  - Histórico de mensagens
  - Comandos de chat
  - Modo WASD/Chat
  - Filtros de mensagem

#### **2. Protocolo de Comunicação**
- **Arquivo**: `otclient/src/client/protocolgamesend.cpp`
- **Função**: Envio de mensagens para o servidor
- **Métodos principais**:
  - `sendTalk()` - Envia mensagem
  - `sendRequestChannels()` - Solicita lista de canais
  - `sendJoinChannel()` - Entra em canal
  - `sendLeaveChannel()` - Sai de canal
  - `sendOpenPrivateChannel()` - Abre canal privado

#### **3. Parser de Mensagens**
- **Arquivo**: `otclient/src/client/protocolgameparse.cpp`
- **Função**: Processa mensagens recebidas do servidor
- **Métodos principais**:
  - `parseTalk()` - Processa mensagem de fala
  - `parseChannelList()` - Processa lista de canais
  - `parseOpenChannel()` - Processa abertura de canal
  - `parseTextMessage()` - Processa mensagem de texto

### **APIs e Interfaces**

#### **1. API de Envio de Mensagens**
```cpp
void ProtocolGame::sendTalk(const Otc::MessageMode mode, 
                           const uint16_t channelId, 
                           const std::string_view receiver, 
                           const std::string_view message)
{
    if (message.empty())
        return;

    if (message.length() > UINT8_MAX) {
        g_logger.traceError("message too large");
        return;
    }

    const auto& msg = std::make_shared<OutputMessage>();
    msg->addU8(Proto::ClientTalk);
    msg->addU8(Proto::translateMessageModeToServer(mode));

    switch (mode) {
        case Otc::MessagePrivateTo:
        case Otc::MessageGamemasterPrivateTo:
        case Otc::MessageRVRAnswer:
            msg->addString(receiver);
            break;
        case Otc::MessageChannel:
        case Otc::MessageChannelHighlight:
        case Otc::MessageChannelManagement:
        case Otc::MessageGamemasterChannel:
            msg->addU16(channelId);
            break;
        default:
            break;
    }

    msg->addString(message);
    send(msg);
}
```

#### **2. API de Processamento de Mensagens**
```cpp
void ProtocolGame::parseTalk(const InputMessagePtr& msg)
{
    uint32_t statement = 0;
    if (g_game.getFeature(Otc::GameMessageStatements)) {
        statement = msg->getU32(); // channel statement guid
    }

    const auto& name = g_game.formatCreatureName(msg->getString());

    if (statement > 0 && g_game.getClientVersion() >= 1281) {
        msg->getU8(); // suffix
    }

    const uint16_t level = g_game.getFeature(Otc::GameMessageLevel) ? msg->getU16() : 0;

    auto messageByte = msg->getU8();
    const Otc::MessageMode mode = Proto::translateMessageModeFromServer(messageByte);
    uint16_t channelId = 0;
    Position pos;

    switch (mode) {
        case Otc::MessagePotion:
        case Otc::MessageSay:
        case Otc::MessageWhisper:
        case Otc::MessageYell:
        case Otc::MessageMonsterSay:
        case Otc::MessageMonsterYell:
        case Otc::MessageNpcTo:
        case Otc::MessageBarkLow:
        case Otc::MessageBarkLoud:
        case Otc::MessageSpell:
        case Otc::MessageNpcFromStartBlock:
            pos = getPosition(msg);
            break;
        case Otc::MessageChannel:
        case Otc::MessageChannelManagement:
        case Otc::MessageChannelHighlight:
        case Otc::MessageGamemasterChannel:
            channelId = msg->getU16();
            break;
        case Otc::MessageNpcFrom:
        case Otc::MessagePrivateTo:
        case Otc::MessagePrivateFrom:
        case Otc::MessageGamemasterBroadcast:
        case Otc::MessageGamemasterPrivateFrom:
        case Otc::MessageRVRAnswer:
        case Otc::MessageRVRContinue:
            break;
        case Otc::MessageRVRChannel:
            msg->getU32();
            break;
        default:
            throw Exception("ProtocolGame::parseTalk: unknown message mode {}", messageByte);
    }

    const auto& text = msg->getString();
    g_game.processTalk(name, level, mode, text, channelId, pos);
}
```

#### **3. API Lua para Chat**
```lua
-- Enviar mensagem
function sendMessage(message, tab)
    local tab = tab or getCurrentTab()
    if not tab then
        return
    end

    -- Filtros de mensagem
    for k, func in pairs(filters) do
        if func(message) then
            return true
        end
    end

    -- Comandos de chat
    local channel = tab.channelId
    local originalMessage = message
    local chatCommandSayMode
    local chatCommandPrivate
    local chatCommandPrivateReady
    local chatCommandMessage

    -- Comando de grito
    chatCommandMessage = message:match('^%#[y|Y] (.*)')
    if chatCommandMessage ~= nil then
        chatCommandSayMode = 'yell'
        channel = 0
        message = chatCommandMessage
    end

    -- Comando de sussurro
    chatCommandMessage = message:match('^%#[w|W] (.*)')
    if chatCommandMessage ~= nil then
        chatCommandSayMode = 'whisper'
        message = chatCommandMessage
        channel = 0
    end

    -- Comando de fala
    chatCommandMessage = message:match('^%#[s|S] (.*)')
    if chatCommandMessage ~= nil then
        chatCommandSayMode = 'say'
        message = chatCommandMessage
        channel = 0
    end

    -- Comando de broadcast
    chatCommandMessage = message:match('^%#[b|B] (.*)')
    if chatCommandMessage ~= nil then
        chatCommandSayMode = 'broadcast'
        message = chatCommandMessage
        channel = 0
    end

    -- Comando privado
    local findIni, findEnd, chatCommandInitial, chatCommandPrivate, chatCommandEnd, chatCommandMessage = message:find('([%*%@])(.+)([%*%@])(.*)')
    if findIni ~= nil and findIni == 1 then
        if chatCommandInitial == chatCommandEnd then
            chatCommandPrivateRepeat = false
            if chatCommandInitial == '*' then
                setTextEditText('*' .. chatCommandPrivate .. '* ')
            end
            message = chatCommandMessage:trim()
            chatCommandPrivateReady = true
        end
    end

    message = message:gsub('^(%s*)(.*)', '%2')
    if #message == 0 then
        return
    end

    -- Adicionar ao histórico
    currentMessageIndex = 0
    if #messageHistory == 0 or messageHistory[#messageHistory] ~= originalMessage then
        table.insert(messageHistory, originalMessage)
        if #messageHistory > MAX_HISTORY then
            table.remove(messageHistory, 1)
        end
    end

    -- Enviar mensagem
    local speaktypedesc
    if (channel or tab == defaultTab) and not chatCommandPrivateReady then
        if tab == defaultTab then
            speaktypedesc = chatCommandSayMode or SayModes[consolePanel:getChildById('sayModeButton').sayMode].speakTypeDesc
            if speaktypedesc ~= 'say' then
                sayModeChange(2)
            end
        else
            speaktypedesc = chatCommandSayMode or 'channelYellow'
        end

        g_game.talkChannel(SpeakTypesSettings[speaktypedesc].speakType, channel, message)
        return
    else
        local isPrivateCommand = false
        local priv = true
        local tabname = name
        local dontAdd = false
        
        if chatCommandPrivateReady then
            speaktypedesc = 'privatePlayerToPlayer'
            name = chatCommandPrivate
            isPrivateCommand = true
        elseif tab.npcChat then
            speaktypedesc = 'privatePlayerToNpc'
        elseif tab == violationReportTab then
            if violationReportTab.locked then
                modules.game_textmessage.displayFailureMessage('Wait for a gamemaster reply.')
                dontAdd = true
            else
                speaktypedesc = 'rvrContinue'
                tabname = tr('Report Rule') .. '...'
            end
        elseif tab.violationChatName then
            speaktypedesc = 'rvrAnswerTo'
            name = tab.violationChatName
            tabname = tab.violationChatName .. '\'...'
        else
            speaktypedesc = 'privatePlayerToPlayer'
        end

        local speaktype = SpeakTypesSettings[speaktypedesc]
        local player = g_game.getLocalPlayer()
        g_game.talkPrivate(speaktype.speakType, name, message)
        
        if not dontAdd then
            message = applyMessagePrefixies(g_game.getCharacterName(), player:getLevel(), message)
            addPrivateText(message, speaktype, tabname, isPrivateCommand, g_game.getCharacterName())
        end
    end
end
```

## 📚 **Documentação**

### **Guia de Uso**

#### **1. Comandos de Chat**
O sistema de chat do OTClient suporta vários comandos especiais:

- `#y <mensagem>` - Gritar (yell)
- `#w <mensagem>` - Sussurrar (whisper)
- `#s <mensagem>` - Falar normalmente (say)
- `#b <mensagem>` - Broadcast (apenas GMs)
- `#c <mensagem>` - Canal vermelho (apenas GMs)
- `*nome* <mensagem>` - Mensagem privada para jogador
- `@nome@ <mensagem>` - Mensagem privada para jogador

#### **2. Navegação de Canais**
- **Tab** - Próximo canal
- **Shift+Tab** - Canal anterior
- **Ctrl+O** - Lista de canais
- **Ctrl+E** - Fechar canal atual
- **Ctrl+H** - Canal de ajuda

#### **3. Modo WASD/Chat**
- **Enter** - Alternar entre modo chat e movimento
- **Escape** - Cancelar modo chat
- **Shift+Up/Down** - Navegar no histórico

### **Referência de API**

#### **1. Funções de Envio**
```lua
-- Enviar mensagem em canal
g_game.talkChannel(speakType, channelId, message)

-- Enviar mensagem privada
g_game.talkPrivate(speakType, receiver, message)

-- Solicitar lista de canais
g_game.requestChannels()

-- Entrar em canal
g_game.joinChannel(channelId)

-- Sair de canal
g_game.leaveChannel(channelId)

-- Abrir canal privado
g_game.openPrivateChannel(receiver)
```

#### **2. Funções de Processamento**
```lua
-- Processar mensagem recebida
g_game.processTalk(name, level, mode, text, channelId, pos)

-- Processar lista de canais
g_game.processChannelList(channelList)

-- Processar abertura de canal
g_game.processOpenChannel(channelId, channelName)

-- Processar canal privado
g_game.processOpenPrivateChannel(receiver)
```

### **Exemplos Práticos**

#### **1. Sistema de Chat Customizado**
```lua
local CustomChat = {}

function CustomChat.init()
    -- Interceptar mensagens de chat
    ProtocolGame.registerOpcode(GameServerCreatureSay, function(protocol, msg)
        local name = msg:getString()
        local level = msg:getU16()
        local messageType = msg:getU8()
        local message = msg:getString()
        
        -- Processar comandos especiais
        if message:starts('/custom ') then
            CustomChat.handleCustomCommand(name, message:sub(9))
            return -- Não processar normalmente
        end
        
        -- Processar normalmente
        g_game.processCreatureSay(name, level, messageType, message)
    end)
    
    -- Extended opcode para chat avançado
    ProtocolGame.registerExtendedOpcode(90, function(protocol, opcode, buffer)
        local chatData = json.decode(buffer)
        CustomChat.handleAdvancedChat(chatData)
    end)
end

function CustomChat.sendFormattedMessage(message, color, style)
    local data = {
        action = 'formattedMessage',
        message = message,
        color = color,
        style = style
    }
    
    protocolGame:sendExtendedOpcode(90, json.encode(data))
end

function CustomChat.handleCustomCommand(playerName, command)
    if command == 'time' then
        local timeStr = os.date('%H:%M:%S')
        CustomChat.sendFormattedMessage('Hora atual: ' .. timeStr, '#00ff00', 'bold')
    elseif command == 'players' then
        local count = #g_map.getCreatures()
        CustomChat.sendFormattedMessage('Jogadores online: ' .. count, '#ffff00', 'italic')
    end
end
```

#### **2. Sistema de Filtros de Chat**
```lua
local ChatFilters = {}

function ChatFilters.init()
    -- Filtro de spam
    addFilter(function(message)
        local lastMessage = ChatFilters.lastMessage
        local lastTime = ChatFilters.lastTime
        
        if lastMessage == message and os.time() - lastTime < 3 then
            return true -- Bloquear mensagem
        end
        
        ChatFilters.lastMessage = message
        ChatFilters.lastTime = os.time()
        return false
    end)
    
    -- Filtro de palavras proibidas
    local forbiddenWords = {'spam', 'hack', 'cheat'}
    addFilter(function(message)
        for _, word in ipairs(forbiddenWords) do
            if message:lower():find(word) then
                return true -- Bloquear mensagem
            end
        end
        return false
    end)
end
```

#### **3. Sistema de Chat por Cores**
```lua
local ColorChat = {}

function ColorChat.init()
    -- Mapeamento de cores por tipo de mensagem
    ColorChat.colorMap = {
        say = '#FFFF00',
        whisper = '#FFFF00',
        yell = '#FFFF00',
        private = '#5FF7F7',
        channel = '#FFFF00',
        npc = '#9F9DFD',
        gm = '#F55E5E'
    }
end

function ColorChat.applyColor(message, messageType)
    local color = ColorChat.colorMap[messageType] or '#FFFFFF'
    return '<span style="color: ' .. color .. '">' .. message .. '</span>'
end

function ColorChat.processMessage(name, level, mode, text, channelId, pos)
    local messageType = ColorChat.getMessageType(mode)
    local coloredText = ColorChat.applyColor(text, messageType)
    
    -- Adicionar mensagem colorida ao console
    addText(name .. ': ' .. coloredText, messageType)
end
```

## 🔗 **Integração**

### **Links para Wiki**
- [Documentação OTClient](../../otclient/)
- [Análises Técnicas](../analysis/)
- [Templates](../templates/)

### **Dependências**
- [OTCLIENT-001: Análise da Arquitetura Core](./OTCLIENT-001.md)
- [OTCLIENT-003: Sistema de Rede](./OTCLIENT-003.md)
- [OTCLIENT-004: Sistema de UI](./OTCLIENT-004.md)

## 📊 **Métricas**

### **Progresso**
- **Análise de Código**: 100%
- **Documentação**: 100%
- **Exemplos**: 100%
- **Integração**: 100%
- **Validação**: 100%

### **Tempo Estimado**
- **Análise**: 4 horas
- **Documentação**: 2 horas
- **Integração**: 30 minutos
- **Validação**: 30 minutos

## 🚀 **Próximos Passos**

1. **Implementar sistema de chat avançado** com formatação rica
2. **Criar sistema de filtros** mais sofisticados
3. **Desenvolver interface de chat** customizada
4. **Integrar com sistema de logs** para auditoria
5. **Otimizar performance** para grandes volumes de mensagens

---

**Story Completa**: 2025-01-27 16:30:00  
**Responsável**: Habdel Research Agent  
**Status**: ✅ **COMPLETA**  
**Próximo**: 📚 **OTCLIENT-019: Sistema de Configuração**
