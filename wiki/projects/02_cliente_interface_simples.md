---
tags: [projects, practical, otclient, client, interface, educational, beginner, otui, lua_scripting, modification]
aliases: [cliente_interface_simples, simple_client_interface, otclient_interface_project, otui_modification]
type: practical_project
status: active
priority: high
level: beginner
created: 2025-08-05
updated: 2025-08-05
project: 02
course: otclient
prerequisites: [3.1_otclient_introduction, 3.2_interface_system, 3.3_otui_framework]
next_project: 03_sistema_chat_completo
---

# 🎮 **Projeto 2: Modificando Interfaces no OTClient**

## 🎯 **Visão Geral**

Este projeto prático ensina como **modificar e estender** interfaces do OTClient existente, focando em OTUI (Open Tibia User Interface) e Lua scripting para criar interfaces personalizadas. Você aprenderá como trabalhar com a base Open Tibia existente para customizar a experiência do usuário.

## 📚 **Objetivos do Projeto**

### **🎯 Ao final deste projeto, você será capaz de:**
- ✅ Entender como o OTClient organiza interfaces e OTUI
- ✅ Criar interfaces personalizadas usando OTUI
- ✅ Modificar interfaces existentes sem alterar o código C++
- ✅ Implementar funcionalidades via Lua scripting
- ✅ Trabalhar com eventos e callbacks do OTClient
- ✅ Criar widgets e componentes reutilizáveis

## 🏗️ **Estrutura do Projeto**

### **📁 Organização dos Arquivos (Baseado no OTClient Real)**
```
otclient/data/
├── otui/
│   ├── login.otui              # Interface de login (modificada)
│   ├── game.otui               # Interface principal do jogo (modificada)
│   └── custom/
│       ├── inventory_panel.otui    # Painel de inventário personalizado
│       ├── chat_window.otui        # Janela de chat personalizada
│       └── status_bar.otui         # Barra de status personalizada
├── modules/
│   ├── game_interface/
│   │   ├── gameinterface.lua       # Módulo principal da interface
│   │   └── custom_widgets.lua      # Widgets personalizados
│   └── custom_ui/
│       ├── inventory_manager.lua   # Gerenciador de inventário
│       └── chat_manager.lua        # Gerenciador de chat
└── config.otml                   # Configuração do cliente
```

## 🔧 **Implementação**

### **📖 1. Entendendo a Estrutura Existente do OTClient**

#### **🏗️ Como o OTClient Organiza Interfaces**
O OTClient usa OTUI (Open Tibia User Interface) para definir interfaces. Vamos entender como funciona:

```lua
-- Estrutura básica de uma interface OTUI
MainWindow
  id: main_window
  size: 800 600
  @onEscape: self:close()
  
  Label
    id: title_label
    text: "Título da Interface"
    font: verdana-11px-antialised
    color: white
```

#### **🔍 Localização dos Arquivos no OTClient**
```bash
# Interfaces principais
otclient/data/otui/login.otui
otclient/data/otui/game.otui
otclient/data/otui/characterlist.otui

# Módulos Lua
otclient/modules/game_interface/
otclient/modules/game_interface/gameinterface.lua

# Configurações
otclient/data/otui/config.otml
```

### **📖 2. Modificando Interfaces Existentes**

#### **🛠️ Exemplo: Personalizando a Interface de Login**
Vamos modificar a interface de login existente para adicionar funcionalidades:

```otui
-- otclient/data/otui/login.otui (modificado)
MainWindow
  id: login_window
  size: 400 300
  @onEscape: self:close()
  
  Label
    id: title_label
    text: "Login do Jogo"
    font: verdana-11px-antialised
    color: white
    pos: 150 20
    size: 100 20
  
  -- Campos de entrada originais
  TextEdit
    id: account
    pos: 100 60
    size: 200 20
    font: verdana-11px-antialised
    color: white
    background-color: alpha
    
  TextEdit
    id: password
    pos: 100 90
    size: 200 20
    font: verdana-11px-antialised
    color: white
    background-color: alpha
    password: true
    
  -- NOVA FUNCIONALIDADE: Checkbox "Lembrar Conta"
  CheckBox
    id: remember_account
    text: "Lembrar conta"
    font: verdana-11px-antialised
    color: white
    pos: 100 120
    size: 100 20
    @onCheckChange: self:onRememberAccountChange()
    
  -- NOVA FUNCIONALIDADE: Botão "Configurações"
  Button
    id: settings_button
    text: "Configurações"
    font: verdana-11px-antialised
    color: white
    pos: 100 150
    size: 80 20
    @onClick: self:onSettingsClick()
    
  -- Botões originais
  Button
    id: login
    text: "Login"
    font: verdana-11px-antialised
    color: white
    pos: 100 180
    size: 80 20
    @onClick: self:onLoginClick()
    
  Button
    id: exit
    text: "Sair"
    font: verdana-11px-antialised
    color: white
    pos: 200 180
    size: 80 20
    @onClick: self:onExitClick()
```

#### **🛠️ Exemplo: Criando um Painel de Inventário Personalizado**
```otui
-- otclient/data/otui/custom/inventory_panel.otui (novo)
Panel
  id: custom_inventory_panel
  pos: 10 10
  size: 200 300
  background-color: alpha
  border-color: white
  
  Label
    id: inventory_title
    text: "Inventário Personalizado"
    font: verdana-11px-antialised
    color: white
    pos: 5 5
    size: 190 20
    
  -- Grid de slots de inventário
  GridLayout
    id: inventory_grid
    pos: 5 30
    size: 190 200
    margin: 2
    flow: left-to-right
    
    -- Slots serão criados dinamicamente via Lua
    -- Slot 1
    Item
      id: slot_1
      size: 32 32
      margin: 1
      @onDrop: self:onItemDrop()
      @onClick: self:onItemClick()
      
    -- Slot 2
    Item
      id: slot_2
      size: 32 32
      margin: 1
      @onDrop: self:onItemDrop()
      @onClick: self:onItemClick()
      
    -- Continua para todos os slots...
    
  -- Barra de informações
  Label
    id: weight_label
    text: "Peso: 0/100"
    font: verdana-10px-antialised
    color: yellow
    pos: 5 240
    size: 190 15
    
  Label
    id: capacity_label
    text: "Capacidade: 0/100"
    font: verdana-10px-antialised
    color: yellow
    pos: 5 255
    size: 190 15
    
  -- Botões de ação
  Button
    id: sort_button
    text: "Organizar"
    font: verdana-10px-antialised
    color: white
    pos: 5 275
    size: 60 20
    @onClick: self:onSortClick()
    
  Button
    id: search_button
    text: "Buscar"
    font: verdana-10px-antialised
    color: white
    pos: 70 275
    size: 60 20
    @onClick: self:onSearchClick()
```

### **📖 3. Criando Módulos Lua para Funcionalidades**

#### **🛠️ Exemplo: Gerenciador de Inventário Personalizado**
```lua
-- otclient/modules/custom_ui/inventory_manager.lua
local inventoryManager = {}

-- Configurações do inventário
inventoryManager.config = {
    maxSlots = 30,
    maxWeight = 100,
    autoSort = false,
    showTooltips = true
}

-- Estado do inventário
inventoryManager.state = {
    items = {},
    weight = 0,
    capacity = 0,
    selectedSlot = nil
}

-- Inicializar o gerenciador
function inventoryManager:init()
    self.panel = g_ui.displayUI('custom/inventory_panel')
    self:setupEventHandlers()
    self:loadSettings()
    self:updateDisplay()
end

-- Configurar handlers de eventos
function inventoryManager:setupEventHandlers()
    -- Handler para drop de itens
    self.panel.onItemDrop = function(widget, item)
        self:handleItemDrop(widget, item)
    end
    
    -- Handler para clique em itens
    self.panel.onItemClick = function(widget)
        self:handleItemClick(widget)
    end
    
    -- Handler para botão organizar
    self.panel.sort_button.onClick = function()
        self:sortInventory()
    end
    
    -- Handler para botão buscar
    self.panel.search_button.onClick = function()
        self:showSearchDialog()
    end
end

-- Manipular drop de item
function inventoryManager:handleItemDrop(widget, item)
    local slotId = widget:getId():gsub("slot_", "")
    local slotIndex = tonumber(slotId)
    
    if slotIndex and slotIndex <= self.config.maxSlots then
        -- Verificar se o slot está vazio
        if not self.state.items[slotIndex] then
            -- Adicionar item ao slot
            self.state.items[slotIndex] = {
                id = item:getId(),
                count = item:getCount(),
                name = item:getName()
            }
            
            -- Atualizar peso
            self:updateWeight()
            
            -- Atualizar display
            self:updateDisplay()
            
            -- Enviar para o servidor
            self:sendToServer(slotIndex, item:getId(), item:getCount())
        else
            -- Slot ocupado, mostrar mensagem
            g_ui.displayInfoBox("Slot ocupado!")
        end
    end
end

-- Manipular clique em item
function inventoryManager:handleItemClick(widget)
    local slotId = widget:getId():gsub("slot_", "")
    local slotIndex = tonumber(slotId)
    
    if slotIndex and self.state.items[slotIndex] then
        local item = self.state.items[slotIndex]
        
        -- Mostrar tooltip se habilitado
        if self.config.showTooltips then
            self:showItemTooltip(widget, item)
        end
        
        -- Selecionar slot
        self.state.selectedSlot = slotIndex
        self:updateSelection()
    end
end

-- Organizar inventário
function inventoryManager:sortInventory()
    -- Implementar lógica de organização
    local sortedItems = {}
    
    -- Remover slots vazios
    for slotIndex, item in pairs(self.state.items) do
        if item then
            table.insert(sortedItems, item)
        end
    end
    
    -- Ordenar por tipo de item
    table.sort(sortedItems, function(a, b)
        return a.id < b.id
    end)
    
    -- Reorganizar slots
    self.state.items = {}
    for i, item in ipairs(sortedItems) do
        self.state.items[i] = item
    end
    
    -- Atualizar display
    self:updateDisplay()
    
    -- Enviar reorganização para o servidor
    self:sendReorganizationToServer()
end

-- Mostrar diálogo de busca
function inventoryManager:showSearchDialog()
    local dialog = g_ui.createWidget('TextEdit')
    dialog:setText("Digite o nome do item...")
    dialog:focus()
    
    dialog.onTextChange = function(widget, text)
        self:searchItems(text)
    end
end

-- Buscar itens
function inventoryManager:searchItems(searchText)
    if searchText and searchText ~= "" then
        local foundItems = {}
        
        for slotIndex, item in pairs(self.state.items) do
            if item and string.find(string.lower(item.name), 
                                   string.lower(searchText)) then
                table.insert(foundItems, {
                    slot = slotIndex,
                    item = item
                })
            end
        end
        
        -- Destacar itens encontrados
        self:highlightItems(foundItems)
    else
        -- Remover destaque
        self:clearHighlights()
    end
end

-- Atualizar display
function inventoryManager:updateDisplay()
    -- Atualizar slots
    for i = 1, self.config.maxSlots do
        local slotWidget = self.panel:recursiveGetChildById("slot_" .. i)
        if slotWidget then
            local item = self.state.items[i]
            if item then
                -- Mostrar item no slot
                slotWidget:setItemId(item.id)
                slotWidget:setItemCount(item.count)
            else
                -- Slot vazio
                slotWidget:setItemId(0)
                slotWidget:setItemCount(0)
            end
        end
    end
    
    -- Atualizar informações
    self.panel.weight_label:setText(string.format("Peso: %d/%d", 
                                                  self.state.weight, 
                                                  self.config.maxWeight))
    self.panel.capacity_label:setText(string.format("Capacidade: %d/%d", 
                                                    self.state.capacity, 
                                                    self.config.maxSlots))
end

-- Carregar configurações
function inventoryManager:loadSettings()
    local settings = g_settings.getNode('inventory')
    if settings then
        self.config.autoSort = settings:get('autoSort') or false
        self.config.showTooltips = settings:get('showTooltips') or true
    end
end

-- Salvar configurações
function inventoryManager:saveSettings()
    local settings = g_settings.getNode('inventory')
    if not settings then
        settings = g_settings.createNode('inventory')
    end
    
    settings:set('autoSort', self.config.autoSort)
    settings:set('showTooltips', self.config.showTooltips)
    g_settings.save()
end

-- Enviar dados para o servidor
function inventoryManager:sendToServer(slot, itemId, count)
    -- Implementar comunicação com o servidor
    -- Esta é uma implementação conceitual
    print(string.format("Enviando para servidor: slot=%d, item=%d, count=%d", 
                        slot, itemId, count))
end

return inventoryManager
```

#### **🛠️ Exemplo: Gerenciador de Chat Personalizado**
```lua
-- otclient/modules/custom_ui/chat_manager.lua
local chatManager = {}

-- Configurações do chat
chatManager.config = {
    maxMessages = 100,
    autoScroll = true,
    showTimestamps = true,
    filterSpam = true
}

-- Estado do chat
chatManager.state = {
    messages = {},
    channels = {},
    activeChannel = "Local",
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
    self.window.input.onTextSubmit = function(widget, text)
        self:sendMessage(text)
    end
    
    -- Handler para mudança de canal
    self.window.channel_list.onSelectionChange = function(widget, selected)
        self:changeChannel(selected)
    end
    
    -- Handler para filtros
    self.window.filter_button.onClick = function()
        self:showFilterDialog()
    end
end

-- Enviar mensagem
function chatManager:sendMessage(text)
    if text and text ~= "" then
        local message = {
            text = text,
            channel = self.state.activeChannel,
            timestamp = os.time(),
            sender = "Você"
        }
        
        -- Adicionar à lista de mensagens
        table.insert(self.state.messages, message)
        
        -- Limitar número de mensagens
        if #self.state.messages > self.config.maxMessages then
            table.remove(self.state.messages, 1)
        end
        
        -- Atualizar display
        self:updateDisplay()
        
        -- Enviar para o servidor
        self:sendToServer(message)
        
        -- Limpar input
        self.window.input:setText("")
    end
end

-- Receber mensagem
function chatManager:receiveMessage(message)
    -- Aplicar filtros
    if self:shouldFilterMessage(message) then
        return
    end
    
    -- Adicionar à lista
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

-- Filtrar mensagem
function chatManager:shouldFilterMessage(message)
    if not self.config.filterSpam then
        return false
    end
    
    -- Verificar se é spam (mensagem repetida)
    local lastMessage = self.state.messages[#self.state.messages]
    if lastMessage and lastMessage.text == message.text and
       lastMessage.sender == message.sender and
       (os.time() - lastMessage.timestamp) < 5 then
        return true
    end
    
    -- Verificar filtros personalizados
    for _, filter in pairs(self.state.filters) do
        if string.find(string.lower(message.text), 
                      string.lower(filter)) then
            return true
        end
    end
    
    return false
end

-- Mudar canal
function chatManager:changeChannel(channelName)
    if channelName and self.state.channels[channelName] then
        self.state.activeChannel = channelName
        self:updateDisplay()
        
        -- Atualizar interface
        self.window.channel_label:setText("Canal: " .. channelName)
    end
end

-- Configurar canais
function chatManager:setupChannels()
    self.state.channels = {
        ["Local"] = {color = "white", enabled = true},
        ["Trade"] = {color = "yellow", enabled = true},
        ["Help"] = {color = "blue", enabled = true},
        ["Private"] = {color = "green", enabled = true}
    }
    
    -- Atualizar lista de canais
    for channelName, channelData in pairs(self.state.channels) do
        local item = self.window.channel_list:addOption(channelName)
        item:setColor(channelData.color)
    end
end

-- Atualizar display
function chatManager:updateDisplay()
    -- Limpar mensagens
    self.window.message_list:clearChildren()
    
    -- Adicionar mensagens filtradas por canal
    for _, message in ipairs(self.state.messages) do
        if message.channel == self.state.activeChannel then
            local messageWidget = g_ui.createWidget('Label', self.window.message_list)
            
            local displayText = message.text
            if self.config.showTimestamps then
                local timeStr = os.date("%H:%M", message.timestamp)
                displayText = "[" .. timeStr .. "] " .. displayText
            end
            
            messageWidget:setText(displayText)
            messageWidget:setColor(self.state.channels[message.channel].color)
        end
    end
    
    -- Auto-scroll se habilitado
    if self.config.autoScroll then
        self:scrollToBottom()
    end
end

-- Rolar para baixo
function chatManager:scrollToBottom()
    local scrollbar = self.window.message_list:getVerticalScrollBar()
    if scrollbar then
        scrollbar:setValue(scrollbar:getMaximum())
    end
end

-- Mostrar diálogo de filtros
function chatManager:showFilterDialog()
    local dialog = g_ui.createWidget('TextEdit')
    dialog:setText("Digite palavras para filtrar...")
    dialog:focus()
    
    dialog.onTextSubmit = function(widget, text)
        if text and text ~= "" then
            table.insert(self.state.filters, text)
            self:saveSettings()
        end
        widget:destroy()
    end
end

-- Carregar configurações
function chatManager:loadSettings()
    local settings = g_settings.getNode('chat')
    if settings then
        self.config.autoScroll = settings:get('autoScroll') or true
        self.config.showTimestamps = settings:get('showTimestamps') or true
        self.config.filterSpam = settings:get('filterSpam') or true
        
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
    settings:set('filterSpam', self.config.filterSpam)
    settings:set('filters', self.state.filters)
    g_settings.save()
end

-- Enviar dados para o servidor
function chatManager:sendToServer(message)
    -- Implementar comunicação com o servidor
    -- Esta é uma implementação conceitual
    print(string.format("Enviando mensagem: %s (canal: %s)", 
                        message.text, message.channel))
end

return chatManager
```

### **📖 4. Configuração do Cliente**

#### **⚙️ Modificando config.otml**
```otml
<!-- otclient/data/otui/config.otml (modificações) -->
<Config>
  <!-- Configurações de interface personalizada -->
  <Interface>
    <CustomUI enabled="true" />
    <InventoryPanel enabled="true" />
    <ChatWindow enabled="true" />
    <StatusBar enabled="true" />
  </Interface>
  
  <!-- Configurações de módulos personalizados -->
  <Modules>
    <CustomUI path="modules/custom_ui/" />
    <InventoryManager enabled="true" />
    <ChatManager enabled="true" />
  </Modules>
  
  <!-- Configurações de debug para desenvolvimento -->
  <Debug>
    <ShowWidgetBounds enabled="false" />
    <ShowWidgetNames enabled="false" />
    <LogLevel value="info" />
  </Debug>
</Config>
```

## 🎯 **Exercícios Práticos**

### **📝 Exercício 1: Interface de Login Personalizada**
**Objetivo**: Modificar a interface de login para incluir funcionalidades avançadas.

**Tarefas**:
1. Abra `otclient/data/otui/login.otui`
2. Adicione um campo para "Servidor Personalizado"
3. Implemente sistema de "Lembrar Conta"
4. Crie um botão "Configurações Avançadas"

**Código Base**:
```otui
-- Adicione ao login.otui existente
TextEdit
  id: custom_server
  text: "Servidor Personalizado"
  font: verdana-11px-antialised
  color: white
  background-color: alpha
  pos: 100 120
  size: 200 20
  @onTextChange: self:onServerChange()

CheckBox
  id: remember_account
  text: "Lembrar conta"
  font: verdana-11px-antialised
  color: white
  pos: 100 150
  size: 100 20
  @onCheckChange: self:onRememberAccountChange()

Button
  id: advanced_settings
  text: "Configurações Avançadas"
  font: verdana-11px-antialised
  color: white
  pos: 100 180
  size: 120 20
  @onClick: self:onAdvancedSettingsClick()
```

### **📝 Exercício 2: Painel de Status Personalizado**
**Objetivo**: Criar um painel de status que mostra informações do jogador.

**Tarefas**:
1. Crie um novo arquivo `otclient/data/otui/custom/status_panel.otui`
2. Implemente barras de vida, mana e stamina
3. Adicione informações de nível e experiência
4. Crie sistema de notificações

**Código Base**:
```otui
-- Novo arquivo: otclient/data/otui/custom/status_panel.otui
Panel
  id: status_panel
  pos: 10 10
  size: 250 150
  background-color: alpha
  border-color: white
  
  Label
    id: player_name
    text: "Nome do Jogador"
    font: verdana-11px-antialised
    color: white
    pos: 5 5
    size: 240 20
    
  -- Barra de vida
  ProgressBar
    id: health_bar
    pos: 5 30
    size: 240 15
    color: red
    background-color: darkred
    @onValueChange: self:onHealthChange()
    
  Label
    id: health_label
    text: "Vida: 100/100"
    font: verdana-10px-antialised
    color: red
    pos: 5 50
    size: 240 15
    
  -- Barra de mana
  ProgressBar
    id: mana_bar
    pos: 5 70
    size: 240 15
    color: blue
    background-color: darkblue
    @onValueChange: self:onManaChange()
    
  Label
    id: mana_label
    text: "Mana: 50/50"
    font: verdana-10px-antialised
    color: blue
    pos: 5 90
    size: 240 15
    
  -- Informações de nível
  Label
    id: level_label
    text: "Nível: 1"
    font: verdana-10px-antialised
    color: yellow
    pos: 5 110
    size: 120 15
    
  Label
    id: exp_label
    text: "Exp: 0/100"
    font: verdana-10px-antialised
    color: yellow
    pos: 130 110
    size: 120 15
    
  -- Notificações
  Label
    id: notification
    text: ""
    font: verdana-10px-antialised
    color: green
    pos: 5 130
    size: 240 15
```

### **📝 Exercício 3: Sistema de Atalhos Personalizado**
**Objetivo**: Implementar um sistema de atalhos de teclado personalizado.

**Tarefas**:
1. Crie um módulo Lua para gerenciar atalhos
2. Implemente atalhos para inventário, chat e status
3. Adicione sistema de configuração de atalhos
4. Crie interface para editar atalhos

**Código Base**:
```lua
-- Novo arquivo: otclient/modules/custom_ui/hotkey_manager.lua
local hotkeyManager = {}

-- Configurações de atalhos
hotkeyManager.config = {
    enabled = true,
    showHints = true
}

-- Atalhos padrão
hotkeyManager.defaultHotkeys = {
    ["F1"] = "toggle_inventory",
    ["F2"] = "toggle_chat",
    ["F3"] = "toggle_status",
    ["F4"] = "toggle_map",
    ["Ctrl+I"] = "open_inventory",
    ["Ctrl+C"] = "open_chat",
    ["Ctrl+S"] = "open_status"
}

-- Estado dos atalhos
hotkeyManager.state = {
    hotkeys = {},
    active = true
}

-- Inicializar o gerenciador
function hotkeyManager:init()
    self:loadSettings()
    self:setupEventHandlers()
    self:registerDefaultHotkeys()
end

-- Configurar handlers de eventos
function hotkeyManager:setupEventHandlers()
    -- Handler para teclas pressionadas
    g_keyboard.bindKeyDown(function(key, keyboardModifiers)
        self:handleKeyPress(key, keyboardModifiers)
    end)
end

-- Manipular tecla pressionada
function hotkeyManager:handleKeyPress(key, modifiers)
    if not self.state.active then
        return
    end
    
    local keyCombo = self:getKeyCombo(key, modifiers)
    local action = self.state.hotkeys[keyCombo]
    
    if action then
        self:executeAction(action)
    end
end

-- Obter combinação de teclas
function hotkeyManager:getKeyCombo(key, modifiers)
    local combo = ""
    
    if modifiers.ctrl then
        combo = combo .. "Ctrl+"
    end
    if modifiers.alt then
        combo = combo .. "Alt+"
    end
    if modifiers.shift then
        combo = combo .. "Shift+"
    end
    
    combo = combo .. key
    return combo
end

-- Executar ação
function hotkeyManager:executeAction(action)
    if action == "toggle_inventory" then
        self:toggleInventory()
    elseif action == "toggle_chat" then
        self:toggleChat()
    elseif action == "toggle_status" then
        self:toggleStatus()
    elseif action == "toggle_map" then
        self:toggleMap()
    elseif action == "open_inventory" then
        self:openInventory()
    elseif action == "open_chat" then
        self:openChat()
    elseif action == "open_status" then
        self:openStatus()
    end
end

-- Ações de interface
function hotkeyManager:toggleInventory()
    local inventory = g_ui.getWidget('custom_inventory_panel')
    if inventory then
        inventory:setVisible(not inventory:isVisible())
    end
end

function hotkeyManager:toggleChat()
    local chat = g_ui.getWidget('custom_chat_window')
    if chat then
        chat:setVisible(not chat:isVisible())
    end
end

function hotkeyManager:toggleStatus()
    local status = g_ui.getWidget('status_panel')
    if status then
        status:setVisible(not status:isVisible())
    end
end

function hotkeyManager:toggleMap()
    local map = g_ui.getWidget('gameMapPanel')
    if map then
        map:setVisible(not map:isVisible())
    end
end

-- Registrar atalhos padrão
function hotkeyManager:registerDefaultHotkeys()
    for keyCombo, action in pairs(self.defaultHotkeys) do
        self.state.hotkeys[keyCombo] = action
    end
end

-- Carregar configurações
function hotkeyManager:loadSettings()
    local settings = g_settings.getNode('hotkeys')
    if settings then
        self.state.active = settings:get('enabled') or true
        self.config.showHints = settings:get('showHints') or true
        
        -- Carregar atalhos personalizados
        local customHotkeys = settings:get('customHotkeys')
        if customHotkeys then
            for keyCombo, action in pairs(customHotkeys) do
                self.state.hotkeys[keyCombo] = action
            end
        end
    end
end

-- Salvar configurações
function hotkeyManager:saveSettings()
    local settings = g_settings.getNode('hotkeys')
    if not settings then
        settings = g_settings.createNode('hotkeys')
    end
    
    settings:set('enabled', self.state.active)
    settings:set('showHints', self.config.showHints)
    
    -- Salvar atalhos personalizados
    local customHotkeys = {}
    for keyCombo, action in pairs(self.state.hotkeys) do
        if not self.defaultHotkeys[keyCombo] then
            customHotkeys[keyCombo] = action
        end
    end
    settings:set('customHotkeys', customHotkeys)
    
    g_settings.save()
end

return hotkeyManager
```

## 🔍 **Conceitos-Chave Aprendidos**

### **🎯 Modificação vs Re-implementação**
- **✅ Correto**: Modificar interfaces existentes via OTUI e Lua
- **❌ Incorreto**: Re-escrever componentes de interface em C++

### **🎯 OTUI para Interface Design**
- **Declarativo**: Definir interfaces de forma declarativa
- **Eventos**: Usar @onClick, @onTextChange, etc.
- **Widgets**: Componentes reutilizáveis
- **Layouts**: GridLayout, HorizontalLayout, etc.

### **🎯 Lua Scripting para Funcionalidades**
- **Módulos**: Organizar código em módulos Lua
- **Eventos**: Responder a eventos da interface
- **Configuração**: Gerenciar configurações do usuário
- **Comunicação**: Enviar dados para o servidor

### **🎯 C++ Apenas para Mudanças Estruturais**
- **Protocolo de Rede**: Modificações na comunicação
- **Sistema de Renderização**: Mudanças no core gráfico
- **Novos Widgets**: Componentes fundamentais
- **Integração com Sistema**: Mudanças no core do cliente

### **🎯 Trabalhando com a Base Existente**
- **Entender OTUI**: Como o OTClient organiza interfaces
- **Respeitar Convenções**: Seguir padrões existentes
- **Extensão Gradual**: Adicionar funcionalidades sem quebrar
- **Debugging**: Usar ferramentas existentes do OTClient

## 🚀 **Próximos Passos**

### **📚 Módulos Relacionados**
- [[3.2_interface_system|Sistema de Interface]]
- [[3.3_otui_framework|Framework OTUI]]
- [[4.1_comunicacao_protocolo|Comunicação e Protocolo]]

### **🎮 Projetos Relacionados**
- [[01_servidor_basico_npcs|Projeto 1: Servidor com NPCs]]
- [[03_sistema_chat_completo|Projeto 3: Sistema de Chat]]

### **🔧 Ferramentas Úteis**
- **OTClient Documentation**: `otclient/docs/`
- **OTUI Reference**: `otclient/data/otui/`
- **Lua Modules**: `otclient/modules/`

---

> [!success] **Projeto Concluído**
> ✅ **Objetivo**: Aprender a modificar e estender interfaces do OTClient existente
> ✅ **Foco**: OTUI para design, Lua para funcionalidades, C++ apenas para mudanças estruturais
> ✅ **Resultado**: Capacidade de trabalhar com a base Open Tibia existente
> 🎯 **Próximo**: [[03_sistema_chat_completo|Projeto 3: Sistema de Chat]] 