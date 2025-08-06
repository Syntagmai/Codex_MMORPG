---
tags: [projects, practical, integration, chat, communication, educational, intermediate, lua_scripting, modification]
aliases: [sistema_chat_completo, complete_chat_system, chat_integration_project, chat_modification]
type: practical_project
status: active
priority: high
level: intermediate
created: 2025-08-05
updated: 2025-08-05
project: 03
course: integration
prerequisites: [4.1_comunicacao_protocolo, 4.2_sincronizacao_dados, 01_servidor_basico_npcs, 02_cliente_interface_simples]
next_project: 04_mmorpg_basico_funcional
---

# 💬 **Projeto 3: Modificando o Sistema de Chat Existente**

## 🎯 **Visão Geral**

Este projeto prático ensina como **modificar e estender** o sistema de chat existente no Canary e OTClient, focando em Lua scripting para adicionar funcionalidades personalizadas. Você aprenderá como trabalhar com a base Open Tibia existente para criar um sistema de comunicação robusto.

## 📚 **Objetivos do Projeto**

### **🎯 Ao final deste projeto, você será capaz de:**
- ✅ Entender como o Canary e OTClient gerenciam chat
- ✅ Modificar canais de chat existentes via Lua
- ✅ Criar novos canais e funcionalidades de chat
- ✅ Implementar filtros e moderação personalizados
- ✅ Trabalhar com eventos de chat existentes
- ✅ Adicionar funcionalidades avançadas sem alterar C++

## 🏗️ **Estrutura do Projeto**

### **📁 Organização dos Arquivos (Baseado no Canary e OTClient Reais)**
```
canary/data/
├── scripts/
│   ├── revscripts/
│   │   ├── custom_chat.lua           # Sistema de chat personalizado
│   │   ├── chat_filters.lua          # Filtros de chat
│   │   └── chat_moderation.lua       # Sistema de moderação
│   └── moveevents/
│       └── chat_triggers.lua         # Gatilhos de chat
├── chatchannels/
│   ├── custom_channels.xml           # Canais personalizados
│   └── channel_config.lua            # Configuração de canais
└── config.lua.dist                   # Configuração do servidor

otclient/data/
├── otui/
│   └── custom/
│       ├── chat_window.otui          # Interface de chat personalizada
│       └── chat_settings.otui        # Configurações de chat
└── modules/
    └── custom_ui/
        ├── chat_manager.lua          # Gerenciador de chat do cliente
        └── chat_filters.lua          # Filtros do lado cliente
```

## 🔧 **Implementação**

### **📖 1. Entendendo o Sistema de Chat Existente**

#### **🏗️ Como o Canary Gerencia Chat**
O Canary usa um sistema de canais de chat integrado. Vamos entender como funciona:

```lua
-- Estrutura básica de um canal de chat no Canary
local channel = {
    id = 1,
    name = "Local",
    description = "Canal local",
    public = true,
    muted = false
}

-- O Canary carrega canais de canary/data/chatchannels/
-- Cada canal pode ter configurações específicas
```

#### **🔍 Localização dos Arquivos no Canary**
```bash
# Canais de chat
canary/data/chatchannels/
canary/data/chatchannels/custom_channels.xml

# Scripts de chat
canary/data/scripts/revscripts/
canary/data/scripts/moveevents/

# Configurações
canary/config.lua.dist
```

### **📖 2. Modificando Canais de Chat Existentes**

#### **🛠️ Exemplo: Personalizando o Canal Local**
Vamos modificar o canal local existente para adicionar funcionalidades:

```lua
-- canary/data/scripts/revscripts/custom_chat.lua
local customChat = {}

-- Configurações do chat personalizado
customChat.config = {
    enableFilters = true,
    enableModeration = true,
    maxMessageLength = 200,
    spamProtection = true,
    cooldownTime = 3000 -- 3 segundos
}

-- Estado do chat
customChat.state = {
    lastMessages = {},
    mutedPlayers = {},
    spamCount = {}
}

-- Modificar o canal local existente
function customChat:modifyLocalChannel()
    local localChannel = g_game.getLocalChannel()
    if localChannel then
        -- Adicionar funcionalidades personalizadas
        localChannel.onPlayerMessage = function(player, message)
            return self:handlePlayerMessage(player, message, localChannel)
        end
        
        -- Adicionar sistema de moderação
        localChannel.onPlayerJoin = function(player)
            self:handlePlayerJoin(player, localChannel)
        end
        
        localChannel.onPlayerLeave = function(player)
            self:handlePlayerLeave(player, localChannel)
        end
    end
end

-- Manipular mensagem do jogador
function customChat:handlePlayerMessage(player, message, channel)
    -- Verificar filtros
    if self.config.enableFilters and self:shouldFilterMessage(player, message) then
        player:sendTextMessage("Mensagem bloqueada por filtro.")
        return false
    end
    
    -- Verificar spam
    if self.config.spamProtection and self:isSpam(player, message) then
        player:sendTextMessage("Você está enviando mensagens muito rápido.")
        return false
    end
    
    -- Verificar comprimento
    if string.len(message) > self.config.maxMessageLength then
        player:sendTextMessage("Mensagem muito longa.")
        return false
    end
    
    -- Verificar se o jogador está mutado
    if self.state.mutedPlayers[player:getId()] then
        player:sendTextMessage("Você está mutado.")
        return false
    end
    
    -- Registrar mensagem para spam protection
    self:registerMessage(player, message)
    
    -- Aplicar formatação personalizada
    local formattedMessage = self:formatMessage(player, message)
    
    -- Enviar mensagem formatada
    channel:sendMessage(player, formattedMessage)
    
    return true
end

-- Verificar se deve filtrar mensagem
function customChat:shouldFilterMessage(player, message)
    local filters = {
        "palavrão1", "palavrão2", "spam", "link"
    }
    
    local lowerMessage = string.lower(message)
    for _, filter in ipairs(filters) do
        if string.find(lowerMessage, filter) then
            return true
        end
    end
    
    return false
end

-- Verificar spam
function customChat:isSpam(player, message)
    local playerId = player:getId()
    local currentTime = os.time()
    
    if not self.state.spamCount[playerId] then
        self.state.spamCount[playerId] = {
            count = 0,
            lastTime = currentTime
        }
    end
    
    local spamData = self.state.spamCount[playerId]
    
    -- Resetar contador se passou muito tempo
    if currentTime - spamData.lastTime > 60 then
        spamData.count = 0
    end
    
    -- Incrementar contador
    spamData.count = spamData.count + 1
    spamData.lastTime = currentTime
    
    -- Verificar se é spam (mais de 5 mensagens por minuto)
    return spamData.count > 5
end

-- Registrar mensagem
function customChat:registerMessage(player, message)
    local playerId = player:getId()
    local currentTime = os.time()
    
    if not self.state.lastMessages[playerId] then
        self.state.lastMessages[playerId] = {}
    end
    
    table.insert(self.state.lastMessages[playerId], {
        message = message,
        time = currentTime
    })
    
    -- Manter apenas as últimas 10 mensagens
    if #self.state.lastMessages[playerId] > 10 then
        table.remove(self.state.lastMessages[playerId], 1)
    end
end

-- Formatar mensagem
function customChat:formatMessage(player, message)
    local playerName = player:getName()
    local playerLevel = player:getLevel()
    local playerVocation = player:getVocation():getName()
    
    -- Formatação personalizada baseada no nível
    local prefix = ""
    if playerLevel >= 100 then
        prefix = "[VIP] "
    elseif playerLevel >= 50 then
        prefix = "[EXP] "
    end
    
    return string.format("%s%s [%s %s]: %s", 
                        prefix, playerName, playerLevel, playerVocation, message)
end

-- Manipular jogador entrando no canal
function customChat:handlePlayerJoin(player, channel)
    local playerName = player:getName()
    local welcomeMessage = string.format("Bem-vindo ao canal %s, %s!", 
                                        channel:getName(), playerName)
    
    channel:sendMessage(nil, welcomeMessage)
    
    -- Verificar se o jogador é VIP
    if player:getLevel() >= 100 then
        channel:sendMessage(nil, string.format("%s é um jogador VIP!", playerName))
    end
end

-- Manipular jogador saindo do canal
function customChat:handlePlayerLeave(player, channel)
    local playerName = player:getName()
    local goodbyeMessage = string.format("%s saiu do canal.", playerName)
    
    channel:sendMessage(nil, goodbyeMessage)
end

-- Comandos de moderação
function customChat:addModerationCommands()
    -- Comando para mutar jogador
    local muteCommand = TalkAction("/mute")
    muteCommand.onSay = function(player, words, param)
        if player:getGroup():getAccess() then
            local targetName = param
            local targetPlayer = Player(targetName)
            
            if targetPlayer then
                self.state.mutedPlayers[targetPlayer:getId()] = true
                player:sendTextMessage(string.format("Jogador %s foi mutado.", targetName))
                targetPlayer:sendTextMessage("Você foi mutado por um administrador.")
            else
                player:sendTextMessage("Jogador não encontrado.")
            end
        end
        return true
    end
    muteCommand:register()
    
    -- Comando para desmutar jogador
    local unmuteCommand = TalkAction("/unmute")
    unmuteCommand.onSay = function(player, words, param)
        if player:getGroup():getAccess() then
            local targetName = param
            local targetPlayer = Player(targetName)
            
            if targetPlayer then
                self.state.mutedPlayers[targetPlayer:getId()] = nil
                player:sendTextMessage(string.format("Jogador %s foi desmutado.", targetName))
                targetPlayer:sendTextMessage("Você foi desmutado por um administrador.")
            else
                player:sendTextMessage("Jogador não encontrado.")
            end
        end
        return true
    end
    unmuteCommand:register()
end

-- Inicializar sistema
function customChat:init()
    self:modifyLocalChannel()
    self:addModerationCommands()
    print("Sistema de chat personalizado inicializado!")
end

-- Executar inicialização
customChat:init()
```

### **📖 3. Criando Novos Canais de Chat**

#### **🛠️ Exemplo: Canal de Trade Personalizado**
```lua
-- canary/data/scripts/revscripts/trade_channel.lua
local tradeChannel = {}

-- Configurações do canal de trade
tradeChannel.config = {
    minLevel = 10,
    maxMessageLength = 150,
    priceFormat = true,
    itemLinks = true
}

-- Criar canal de trade personalizado
function tradeChannel:createTradeChannel()
    local channel = g_game.createChannel("Trade", "Canal de comércio")
    
    -- Configurar canal
    channel:setPublic(true)
    channel:setMuted(false)
    
    -- Adicionar handlers personalizados
    channel.onPlayerMessage = function(player, message)
        return self:handleTradeMessage(player, message, channel)
    end
    
    channel.onPlayerJoin = function(player)
        self:handleTradeJoin(player, channel)
    end
    
    return channel
end

-- Manipular mensagem de trade
function tradeChannel:handleTradeMessage(player, message, channel)
    -- Verificar nível mínimo
    if player:getLevel() < self.config.minLevel then
        player:sendTextMessage("Você precisa ser nível " .. self.config.minLevel .. " para usar este canal.")
        return false
    end
    
    -- Verificar formato de preço
    if self.config.priceFormat and not self:isValidTradeMessage(message) then
        player:sendTextMessage("Use o formato: [ITEM] - [PREÇO] - [DESCRIÇÃO]")
        return false
    end
    
    -- Processar links de itens
    if self.config.itemLinks then
        message = self:processItemLinks(message)
    end
    
    -- Enviar mensagem
    channel:sendMessage(player, message)
    return true
end

-- Verificar se é mensagem de trade válida
function tradeChannel:isValidTradeMessage(message)
    -- Padrão básico: [ITEM] - [PREÇO] - [DESCRIÇÃO]
    local pattern = "%[([^%]]+)%]%s*-%s*([0-9,]+)%s*-%s*(.+)"
    return string.match(message, pattern) ~= nil
end

-- Processar links de itens
function tradeChannel:processItemLinks(message)
    -- Converter [ITEM] em links clicáveis
    message = string.gsub(message, "%[([^%]]+)%]", function(itemName)
        local itemId = self:getItemIdByName(itemName)
        if itemId then
            return string.format("[%s](item:%d)", itemName, itemId)
        else
            return string.format("[%s]", itemName)
        end
    end)
    
    return message
end

-- Obter ID do item por nome
function tradeChannel:getItemIdByName(itemName)
    -- Implementação simplificada
    local itemIds = {
        ["sword"] = 2400,
        ["shield"] = 2516,
        ["helmet"] = 2457,
        ["armor"] = 2487
    }
    
    return itemIds[string.lower(itemName)]
end

-- Manipular jogador entrando no canal de trade
function tradeChannel:handleTradeJoin(player, channel)
    local welcomeMessage = string.format(
        "Bem-vindo ao canal de Trade, %s! Use o formato: [ITEM] - [PREÇO] - [DESCRIÇÃO]",
        player:getName()
    )
    
    channel:sendMessage(nil, welcomeMessage)
end

-- Inicializar canal de trade
function tradeChannel:init()
    self:createTradeChannel()
    print("Canal de Trade personalizado criado!")
end

-- Executar inicialização
tradeChannel:init()
```

### **📖 4. Sistema de Filtros Avançados**

#### **🛠️ Exemplo: Filtros de Chat Personalizados**
```lua
-- canary/data/scripts/revscripts/chat_filters.lua
local chatFilters = {}

-- Configurações dos filtros
chatFilters.config = {
    enableWordFilter = true,
    enableLinkFilter = true,
    enableCapsFilter = true,
    enableSpamFilter = true,
    maxCapsPercentage = 70,
    maxMessageLength = 200
}

-- Lista de palavras filtradas
chatFilters.bannedWords = {
    "palavrão1", "palavrão2", "spam", "hack", "cheat"
}

-- Lista de domínios permitidos
chatFilters.allowedDomains = {
    "tibia.com", "wikipedia.org", "youtube.com"
}

-- Aplicar filtros à mensagem
function chatFilters:applyFilters(player, message, channel)
    local originalMessage = message
    
    -- Filtro de palavras
    if self.config.enableWordFilter then
        message = self:filterWords(message)
    end
    
    -- Filtro de links
    if self.config.enableLinkFilter then
        message = self:filterLinks(message)
    end
    
    -- Filtro de caps
    if self.config.enableCapsFilter then
        message = self:filterCaps(message)
    end
    
    -- Verificar se a mensagem foi modificada
    if message ~= originalMessage then
        player:sendTextMessage("Sua mensagem foi filtrada.")
        return message
    end
    
    return originalMessage
end

-- Filtrar palavras proibidas
function chatFilters:filterWords(message)
    local filteredMessage = message
    
    for _, word in ipairs(self.bannedWords) do
        local pattern = string.format("(%s)", word)
        filteredMessage = string.gsub(filteredMessage, pattern, "***")
    end
    
    return filteredMessage
end

-- Filtrar links não permitidos
function chatFilters:filterLinks(message)
    local filteredMessage = message
    
    -- Padrão para detectar URLs
    local urlPattern = "https?://([%w%.%-]+)"
    
    filteredMessage = string.gsub(filteredMessage, urlPattern, function(domain)
        if self:isAllowedDomain(domain) then
            return string.format("http://%s", domain)
        else
            return "[LINK BLOQUEADO]"
        end
    end)
    
    return filteredMessage
end

-- Verificar se domínio é permitido
function chatFilters:isAllowedDomain(domain)
    for _, allowedDomain in ipairs(self.allowedDomains) do
        if string.find(domain, allowedDomain) then
            return true
        end
    end
    return false
end

-- Filtrar excesso de caps
function chatFilters:filterCaps(message)
    local capsCount = 0
    local totalChars = 0
    
    for i = 1, string.len(message) do
        local char = string.sub(message, i, i)
        if string.match(char, "%u") then
            capsCount = capsCount + 1
        end
        if string.match(char, "%w") then
            totalChars = totalChars + 1
        end
    end
    
    if totalChars > 0 then
        local capsPercentage = (capsCount / totalChars) * 100
        
        if capsPercentage > self.config.maxCapsPercentage then
            -- Converter para minúsculas
            return string.lower(message)
        end
    end
    
    return message
end

-- Detectar spam
function chatFilters:detectSpam(player, message)
    local playerId = player:getId()
    local currentTime = os.time()
    
    if not self.spamData then
        self.spamData = {}
    end
    
    if not self.spamData[playerId] then
        self.spamData[playerId] = {
            messages = {},
            lastWarning = 0
        }
    end
    
    local data = self.spamData[playerId]
    
    -- Adicionar mensagem atual
    table.insert(data.messages, {
        message = message,
        time = currentTime
    })
    
    -- Remover mensagens antigas (últimos 60 segundos)
    for i = #data.messages, 1, -1 do
        if currentTime - data.messages[i].time > 60 then
            table.remove(data.messages, i)
        end
    end
    
    -- Verificar spam (mais de 5 mensagens por minuto)
    if #data.messages > 5 then
        if currentTime - data.lastWarning > 30 then
            player:sendTextMessage("Você está enviando mensagens muito rápido. Aguarde um pouco.")
            data.lastWarning = currentTime
        end
        return true
    end
    
    return false
end

-- Inicializar filtros
function chatFilters:init()
    print("Sistema de filtros de chat inicializado!")
end

-- Executar inicialização
chatFilters:init()
```

### **📖 5. Interface de Chat Personalizada no OTClient**

#### **🛠️ Exemplo: Interface de Chat Avançada**
```otui
-- otclient/data/otui/custom/chat_window.otui
MainWindow
  id: custom_chat_window
  size: 400 300
  @onEscape: self:close()
  
  Label
    id: chat_title
    text: "Chat Personalizado"
    font: verdana-11px-antialised
    color: white
    pos: 5 5
    size: 390 20
    
  -- Lista de mensagens
  TextList
    id: message_list
    pos: 5 30
    size: 390 200
    font: verdana-10px-antialised
    color: white
    background-color: alpha
    vertical-scrollbar: true
    @onDoubleClick: self:onMessageDoubleClick()
    
  -- Campo de entrada
  TextEdit
    id: message_input
    pos: 5 240
    size: 320 25
    font: verdana-10px-antialised
    color: white
    background-color: alpha
    @onTextSubmit: self:onSendMessage()
    
  -- Botão enviar
  Button
    id: send_button
    text: "Enviar"
    font: verdana-10px-antialised
    color: white
    pos: 330 240
    size: 60 25
    @onClick: self:onSendMessage()
    
  -- Lista de canais
  ComboBox
    id: channel_list
    pos: 5 270
    size: 150 20
    font: verdana-10px-antialised
    color: white
    @onSelectionChange: self:onChannelChange()
    
  -- Botão configurações
  Button
    id: settings_button
    text: "Config"
    font: verdana-10px-antialised
    color: white
    pos: 160 270
    size: 60 20
    @onClick: self:onSettingsClick()
    
  -- Botão filtros
  Button
    id: filter_button
    text: "Filtros"
    font: verdana-10px-antialised
    color: white
    pos: 225 270
    size: 60 20
    @onClick: self:onFilterClick()
```

#### **🛠️ Exemplo: Gerenciador de Chat do Cliente**
```lua
-- otclient/modules/custom_ui/chat_manager.lua
local chatManager = {}

-- Configurações do chat
chatManager.config = {
    maxMessages = 100,
    autoScroll = true,
    showTimestamps = true,
    enableFilters = true,
    customChannels = {}
}

-- Estado do chat
chatManager.state = {
    messages = {},
    currentChannel = "Local",
    channels = {},
    filters = {}
}

-- Inicializar o gerenciador
function chatManager:init()
    self.window = g_ui.displayUI('custom/chat_window')
    self:setupEventHandlers()
    self:loadSettings()
    self:setupChannels()
end

-- Configurar handlers de eventos
function chatManager:setupEventHandlers()
    -- Handler para envio de mensagem
    self.window.message_input.onTextSubmit = function(widget, text)
        self:sendMessage(text)
    end
    
    -- Handler para botão enviar
    self.window.send_button.onClick = function()
        local text = self.window.message_input:getText()
        self:sendMessage(text)
    end
    
    -- Handler para mudança de canal
    self.window.channel_list.onSelectionChange = function(widget, selected)
        self:changeChannel(selected)
    end
    
    -- Handler para configurações
    self.window.settings_button.onClick = function()
        self:showSettingsDialog()
    end
    
    -- Handler para filtros
    self.window.filter_button.onClick = function()
        self:showFilterDialog()
    end
end

-- Enviar mensagem
function chatManager:sendMessage(text)
    if text and text ~= "" then
        -- Aplicar filtros locais
        if self.config.enableFilters then
            text = self:applyLocalFilters(text)
        end
        
        -- Enviar para o servidor
        self:sendToServer(text)
        
        -- Limpar input
        self.window.message_input:setText("")
    end
end

-- Aplicar filtros locais
function chatManager:applyLocalFilters(text)
    local filteredText = text
    
    -- Filtro de caps
    if self:isExcessiveCaps(text) then
        filteredText = string.lower(text)
    end
    
    -- Filtro de comprimento
    if string.len(filteredText) > 200 then
        filteredText = string.sub(filteredText, 1, 200)
    end
    
    return filteredText
end

-- Verificar excesso de caps
function chatManager:isExcessiveCaps(text)
    local capsCount = 0
    local totalChars = 0
    
    for i = 1, string.len(text) do
        local char = string.sub(text, i, i)
        if string.match(char, "%u") then
            capsCount = capsCount + 1
        end
        if string.match(char, "%w") then
            totalChars = totalChars + 1
        end
    end
    
    if totalChars > 0 then
        local capsPercentage = (capsCount / totalChars) * 100
        return capsPercentage > 70
    end
    
    return false
end

-- Receber mensagem do servidor
function chatManager:receiveMessage(message)
    -- Adicionar timestamp se habilitado
    if self.config.showTimestamps then
        local timeStr = os.date("%H:%M")
        message.text = "[" .. timeStr .. "] " .. message.text
    end
    
    -- Adicionar à lista de mensagens
    table.insert(self.state.messages, message)
    
    -- Limitar número de mensagens
    if #self.state.messages > self.config.maxMessages then
        table.remove(self.state.messages, 1)
    end
    
    -- Atualizar display
    self:updateDisplay()
    
    -- Auto-scroll se habilitado
    if self.config.autoScroll then
        self:scrollToBottom()
    end
end

-- Atualizar display
function chatManager:updateDisplay()
    -- Limpar lista
    self.window.message_list:clearChildren()
    
    -- Adicionar mensagens do canal atual
    for _, message in ipairs(self.state.messages) do
        if message.channel == self.state.currentChannel then
            local messageWidget = g_ui.createWidget('Label', self.window.message_list)
            messageWidget:setText(message.text)
            messageWidget:setColor(message.color or "white")
        end
    end
end

-- Mudar canal
function chatManager:changeChannel(channelName)
    if channelName then
        self.state.currentChannel = channelName
        self:updateDisplay()
        
        -- Atualizar título
        self.window.chat_title:setText("Chat - " .. channelName)
    end
end

-- Configurar canais
function chatManager:setupChannels()
    self.state.channels = {
        "Local", "Trade", "Help", "Private"
    }
    
    -- Adicionar canais à lista
    for _, channelName in ipairs(self.state.channels) do
        self.window.channel_list:addOption(channelName)
    end
    
    -- Selecionar canal padrão
    self.window.channel_list:setCurrentOption("Local")
end

-- Mostrar diálogo de configurações
function chatManager:showSettingsDialog()
    local dialog = g_ui.createWidget('Window')
    dialog:setText("Configurações do Chat")
    dialog:setSize(300, 200)
    
    -- Checkbox para auto-scroll
    local autoScrollCheck = g_ui.createWidget('CheckBox', dialog)
    autoScrollCheck:setText("Auto-scroll")
    autoScrollCheck:setChecked(self.config.autoScroll)
    autoScrollCheck:setPosition(10, 30)
    
    -- Checkbox para timestamps
    local timestampCheck = g_ui.createWidget('CheckBox', dialog)
    timestampCheck:setText("Mostrar timestamps")
    timestampCheck:setChecked(self.config.showTimestamps)
    timestampCheck:setPosition(10, 50)
    
    -- Botão salvar
    local saveButton = g_ui.createWidget('Button', dialog)
    saveButton:setText("Salvar")
    saveButton:setPosition(10, 150)
    saveButton.onClick = function()
        self.config.autoScroll = autoScrollCheck:isChecked()
        self.config.showTimestamps = timestampCheck:isChecked()
        self:saveSettings()
        dialog:destroy()
    end
end

-- Mostrar diálogo de filtros
function chatManager:showFilterDialog()
    local dialog = g_ui.createWidget('Window')
    dialog:setText("Filtros do Chat")
    dialog:setSize(300, 200)
    
    -- Lista de filtros
    local filterList = g_ui.createWidget('TextList', dialog)
    filterList:setPosition(10, 30)
    filterList:setSize(280, 120)
    
    -- Adicionar filtros existentes
    for _, filter in ipairs(self.state.filters) do
        filterList:addOption(filter)
    end
    
    -- Campo para novo filtro
    local newFilterInput = g_ui.createWidget('TextEdit', dialog)
    newFilterInput:setPosition(10, 160)
    newFilterInput:setSize(200, 20)
    newFilterInput:setText("Novo filtro...")
    
    -- Botão adicionar
    local addButton = g_ui.createWidget('Button', dialog)
    addButton:setText("Adicionar")
    addButton:setPosition(220, 160)
    addButton.onClick = function()
        local newFilter = newFilterInput:getText()
        if newFilter and newFilter ~= "" then
            table.insert(self.state.filters, newFilter)
            filterList:addOption(newFilter)
            newFilterInput:setText("")
            self:saveSettings()
        end
    end
end

-- Carregar configurações
function chatManager:loadSettings()
    local settings = g_settings.getNode('chat')
    if settings then
        self.config.autoScroll = settings:get('autoScroll') or true
        self.config.showTimestamps = settings:get('showTimestamps') or true
        self.config.enableFilters = settings:get('enableFilters') or true
        
        -- Carregar filtros
        local filters = settings:get('filters')
        if filters then
            self.state.filters = filters
        end
    end
end

-- Salvar configurações
function chatManager:saveSettings()
    local settings = g_settings.getNode('chat')
    if not settings then
        settings = g_settings.createNode('chat')
    end
    
    settings:set('autoScroll', self.config.autoScroll)
    settings:set('showTimestamps', self.config.showTimestamps)
    settings:set('enableFilters', self.config.enableFilters)
    settings:set('filters', self.state.filters)
    g_settings.save()
end

-- Enviar dados para o servidor
function chatManager:sendToServer(text)
    -- Implementar comunicação com o servidor
    -- Esta é uma implementação conceitual
    print(string.format("Enviando mensagem: %s (canal: %s)", 
                        text, self.state.currentChannel))
end

return chatManager
```

## 🎯 **Exercícios Práticos**

### **📝 Exercício 1: Canal de Eventos Personalizado**
**Objetivo**: Criar um canal de chat específico para eventos do servidor.

**Tarefas**:
1. Crie um novo script Lua para o canal de eventos
2. Implemente sistema de anúncios automáticos
3. Adicione controle de acesso baseado em nível
4. Crie sistema de eventos programados

**Código Base**:
```lua
-- Novo arquivo: canary/data/scripts/revscripts/event_channel.lua
local eventChannel = {}

eventChannel.config = {
    minLevel = 20,
    autoAnnouncements = true,
    eventSchedule = {
        {time = "20:00", message = "Evento noturno começando!"},
        {time = "14:00", message = "Evento diurno ativo!"}
    }
}

function eventChannel:createEventChannel()
    local channel = g_game.createChannel("Events", "Canal de eventos do servidor")
    channel:setPublic(true)
    
    -- Adicionar handlers
    channel.onPlayerMessage = function(player, message)
        return self:handleEventMessage(player, message, channel)
    end
    
    return channel
end

function eventChannel:handleEventMessage(player, message, channel)
    if player:getLevel() < self.config.minLevel then
        player:sendTextMessage("Você precisa ser nível " .. self.config.minLevel .. " para usar este canal.")
        return false
    end
    
    -- Permitir apenas mensagens de eventos
    if not string.find(string.lower(message), "evento") then
        player:sendTextMessage("Este canal é apenas para discussão de eventos.")
        return false
    end
    
    channel:sendMessage(player, message)
    return true
end

-- Inicializar
function eventChannel:init()
    self:createEventChannel()
    print("Canal de Eventos criado!")
end

eventChannel:init()
```

### **📝 Exercício 2: Sistema de Moderação Avançado**
**Objetivo**: Implementar um sistema de moderação com níveis de permissão.

**Tarefas**:
1. Crie comandos de moderação (/warn, /kick, /ban)
2. Implemente sistema de avisos automáticos
3. Adicione log de ações de moderação
4. Crie interface para moderadores

**Código Base**:
```lua
-- Adicione ao custom_chat.lua existente
function customChat:addAdvancedModeration()
    -- Comando de aviso
    local warnCommand = TalkAction("/warn")
    warnCommand.onSay = function(player, words, param)
        if player:getGroup():getAccess() then
            local targetName = param
            local targetPlayer = Player(targetName)
            
            if targetPlayer then
                targetPlayer:sendTextMessage("AVISO: Comporte-se adequadamente!")
                player:sendTextMessage(string.format("Jogador %s foi avisado.", targetName))
                
                -- Registrar no log
                self:logModerationAction(player:getName(), "warn", targetName)
            end
        end
        return true
    end
    warnCommand:register()
end

function customChat:logModerationAction(moderator, action, target)
    local logEntry = string.format("[%s] %s: %s -> %s", 
                                  os.date(), moderator, action, target)
    print("MODERATION LOG: " .. logEntry)
end
```

### **📝 Exercício 3: Interface de Chat com Emojis**
**Objetivo**: Adicionar suporte a emojis na interface de chat.

**Tarefas**:
1. Modifique a interface OTUI para suportar emojis
2. Implemente sistema de emojis personalizados
3. Adicione atalhos de teclado para emojis
4. Crie sistema de emojis baseado em itens do jogo

**Código Base**:
```otui
-- Adicione ao chat_window.otui existente
Button
  id: emoji_button
  text: "😊"
  font: verdana-12px-antialised
  color: white
  pos: 290 240
  size: 30 25
  @onClick: self:onEmojiClick()

Panel
  id: emoji_panel
  pos: 290 270
  size: 100 80
  background-color: alpha
  border-color: white
  visible: false

  Button
    id: emoji_1
    text: "😊"
    pos: 5 5
    size: 20 20
    @onClick: self:onEmojiSelect("😊")
    
  Button
    id: emoji_2
    text: "⚔️"
    pos: 30 5
    size: 20 20
    @onClick: self:onEmojiSelect("⚔️")
    
  Button
    id: emoji_3
    text: "🛡️"
    pos: 55 5
    size: 20 20
    @onClick: self:onEmojiSelect("🛡️")
```

## 🔍 **Conceitos-Chave Aprendidos**

### **🎯 Modificação vs Re-implementação**
- **✅ Correto**: Modificar sistema de chat existente via Lua
- **❌ Incorreto**: Re-escrever sistema completo de chat em C++

### **🎯 Lua Scripting para Chat**
- **Canais**: Modificar e criar canais de chat
- **Filtros**: Implementar filtros de conteúdo
- **Moderação**: Sistema de moderação personalizado
- **Eventos**: Responder a eventos de chat

### **🎯 OTUI para Interface de Chat**
- **Widgets**: Componentes de interface reutilizáveis
- **Eventos**: Handlers para interações do usuário
- **Layouts**: Organização da interface
- **Configuração**: Interface de configurações

### **🎯 C++ Apenas para Mudanças Estruturais**
- **Protocolo de Chat**: Modificações na comunicação
- **Sistema de Canais**: Mudanças no core do chat
- **Novos Tipos de Mensagem**: Estruturas fundamentais
- **Integração com Rede**: Mudanças no protocolo

### **🎯 Trabalhando com a Base Existente**
- **Entender o Sistema**: Como Canary/OTClient gerenciam chat
- **Respeitar Convenções**: Seguir padrões existentes
- **Extensão Gradual**: Adicionar funcionalidades sem quebrar
- **Debugging**: Usar ferramentas existentes

## 🚀 **Próximos Passos**

### **📚 Módulos Relacionados**
- [[4.1_comunicacao_protocolo|Comunicação e Protocolo]]
- [[4.2_sincronizacao_dados|Sincronização de Dados]]
- [[4.3_tratamento_erros|Tratamento de Erros]]

### **🎮 Projetos Relacionados**
- [[01_servidor_basico_npcs|Projeto 1: Servidor com NPCs]]
- [[02_cliente_interface_simples|Projeto 2: Interface do Cliente]]
- [[04_mmorpg_basico_funcional|Projeto 4: MMORPG Básico]]

### **🔧 Ferramentas Úteis**
- **Canary Chat System**: `canary/data/chatchannels/`
- **OTClient UI**: `otclient/data/otui/`
- **Lua Scripting**: `canary/data/scripts/`

---

> [!success] **Projeto Concluído**
> ✅ **Objetivo**: Aprender a modificar e estender o sistema de chat existente
> ✅ **Foco**: Lua scripting para funcionalidades, OTUI para interface, C++ apenas para mudanças estruturais
> ✅ **Resultado**: Capacidade de trabalhar com a base Open Tibia existente
> 🎯 **Próximo**: [[04_mmorpg_basico_funcional|Projeto 4: MMORPG Básico]] 