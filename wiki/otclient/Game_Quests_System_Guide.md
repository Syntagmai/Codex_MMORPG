---
tags: [otclient, game, quests, missions, system, guide, documentation]
status: completed
aliases: [Sistema de Quests, Quest Log, Quest Tracker, Missões]
---

# 🎯 Sistema de Quest e Missões

> [!info] O Sistema de Quest e Missões do OTClient oferece funcionalidades completas para gerenciar quests, missões e tracking de progresso do jogador.

## 📋 Índice
- [[#Visão Geral]]
- [[#Componentes do Sistema]]
- [[#Implementação Prática]]
- [[#Exemplos Práticos]]
- [[#Melhores Práticas]]

---

## 🎯 Visão Geral

O **Sistema de Quest e Missões** do OTClient oferece funcionalidades completas para gerenciar quests, missões e tracking de progresso do jogador. O sistema inclui interface de quest log, tracker de missões e gerenciamento de estado das quests.

### 🎨 **Características Principais**

- **Quest Log**: Interface completa para visualizar todas as quests
- **Quest Tracker**: Sistema de tracking de missões específicas
- **Progress Tracking**: Acompanhamento automático de progresso
- **Filtros Avançados**: Busca, ordenação e filtros por status
- **Persistência**: Salvamento automático de configurações
- **Integração com Jogo**: Comunicação direta com servidor

---

## 🔧 Componentes do Sistema

### 🏗️ **Arquitetura do Sistema**

```
Sistema de Quests
   │
   ├─ Quest Log Controller
   │   ├─ Interface Principal
   │   ├─ Lista de Quests
   │   ├─ Detalhes de Missões
   │   └─ Filtros e Busca
   │
   ├─ Quest Tracker
   │   ├─ Mini Window
   │   ├─ Missões Ativas
   │   ├─ Progresso Visual
   │   └─ Configurações
   │
   ├─ Quest Cache
   │   ├─ Items de Quest
   │   ├─ Contadores
   │   ├─ Estados
   │   └─ Configurações
   │
   └─ Sistema de Persistência
       ├─ Settings JSON
       ├─ Quest Tracking
       └─ Preferências
```

### 🎭 **Estrutura de Dados**

#### 📋 **Quest Data**

```lua
-- Estrutura de uma quest
{
    id = questId,           -- ID único da quest
    name = questName,       -- Nome da quest
    completed = false,      -- Status de conclusão
    missions = {},          -- Lista de missões
    description = "",       -- Descrição detalhada
    icon = "/path/to/icon"  -- Ícone da quest
}
```

#### 🎯 **Mission Data**

```lua
-- Estrutura de uma missão
{
    id = missionId,         -- ID da missão
    name = missionName,     -- Nome da missão
    description = "",       -- Descrição detalhada
    questId = questId,      -- ID da quest pai
    completed = false,      -- Status de conclusão
    progress = 0           -- Progresso atual
}
```

#### 📊 **Quest Cache**

```lua
-- Cache de quests
questLogCache = {
    items = {},            -- Lista de items de quest
    completed = 0,         -- Contador de quests completas
    hidden = 0,           -- Contador de quests ocultas
    visible = 0           -- Contador de quests visíveis
}
```

---

## 💡 Implementação Prática

### 🐍 **API Lua**

#### 📦 **Métodos de Quest Log**

```lua
-- Solicitar lista de quests
g_game.requestQuestLog()

-- Solicitar detalhes de uma quest
g_game.requestQuestLine(questId)

-- Enviar configurações de tracking
g_game.sendRequestTrackerQuestLog(trackingMap)
```

#### 🎯 **Métodos de Controller**

```lua
-- Mostrar quest log
questLogController:show()

-- Ocultar quest log
questLogController:hide()

-- Alternar visibilidade
questLogController:toggle()

-- Filtrar quests
questLogController:filterQuestList(searchText)

-- Ordenar quests
questLogController:sortQuestList(sortOrder)
```

#### 🎨 **Métodos de Tracking**

```lua
-- Mostrar quest tracker
questLogController:showQuestTracker()

-- Alternar tracker
questLogController:toggleMiniWindowsTracker()

-- Adicionar quest ao tracker
questLogController:addQuestToTracker(questId, questName)

-- Remover quest do tracker
questLogController:removeQuestFromTracker(questId)
```

### 🎮 **Implementação Completa do Controller**

```lua
-- Controller principal do Quest Log
questLogController = Controller:new()

-- Variáveis de controle
local trackerMiniWindow = nil
local questLogButton = nil
local buttonQuestLogTrackerButton = nil

-- Cache de quests
local questLogCache = {
    items = {},
    completed = 0,
    hidden = 0,
    visible = 0
}

-- Configurações
local settings = {}
local namePlayer = ""

-- Constantes de cores
local COLORS = {
    BASE_1 = "#484848",
    BASE_2 = "#414141",
    SELECTED = "#585858"
}

-- Funções de ordenação
local sortFunctions = {
    ["Alphabetically (A-Z)"] = function(a, b)
        return a:getText() < b:getText()
    end,
    ["Alphabetically (Z-A)"] = function(a, b)
        return a:getText() > b:getText()
    end,
    ["Completed on Top"] = function(a, b)
        local aCompleted = a.isComplete or false
        local bCompleted = b.isComplete or false
        
        if aCompleted and not bCompleted then
            return true
        elseif not aCompleted and bCompleted then
            return false
        else
            return a:getText() < b:getText()
        end
    end,
    ["Completed on Bottom"] = function(a, b)
        local aCompleted = a.isComplete or false
        local bCompleted = b.isComplete or false
        
        if aCompleted and not bCompleted then
            return false
        elseif not aCompleted and bCompleted then
            return true
        else
            return a:getText() < b:getText()
        end
    end
}

-- Criar item de quest
local function createQuestItem(parent, id, text, color, icon)
    local item = g_ui.createWidget("QuestLogLabel", parent)
    item:setId(id)
    item:setText(text)
    item:setBackgroundColor(color)
    item:setPhantom(false)
    item:setFocusable(true)
    item.BaseColor = color
    item.isPinned = false
    item.isComplete = false
    
    if icon then
        item:setIcon(icon)
    end
    
    if parent == UITextList.questLogList then
        table.insert(questLogCache.items, item)
        if icon ~= "" then
            item.isComplete = true
            questLogCache.completed = questLogCache.completed + 1
        end
    end
    
    return item
end

-- Configurar handlers de clique
local function setupQuestItemClickHandler(item, isQuestList)
    function item:onClick()
        local list = isQuestList and UITextList.questLogList or UITextList.questLogLine
        resetItemCategorySelection(list)
        self:setChecked(true)
        self:setBackgroundColor(COLORS.SELECTED)
        
        if isQuestList then
            g_game.requestQuestLine(self:getId())
            self.iconShow:setVisible(true)
            self.iconPin:setVisible(true)
            questLogController.ui.panelQuestLineSelected:setText(self:getText())
        else
            UITextList.questLogInfo:setText(self.description)
        end
        
        UICheckBox.showInQuestTracker:setChecked(
            isIdInTracker(g_game.getCharacterName():lower(), tonumber(self:getId())))
    end
end

-- Ordenar lista de quests
local function sortQuestList(questList, sortOrder)
    questLogController.currentSortOrder = sortOrder
    local pinnedItems = {}
    local regularItems = {}
    
    for _, child in pairs(questLogCache.items) do
        if child.isPinned then
            table.insert(pinnedItems, child)
        else
            table.insert(regularItems, child)
        end
    end
    
    local sortFunc = sortFunctions[sortOrder]
    if sortFunc then
        table.sort(regularItems, sortFunc)
    end
    
    questLogCache.items = {}
    local index = 1
    
    for _, item in ipairs(pinnedItems) do
        questList:moveChildToIndex(item, index)
        table.insert(questLogCache.items, item)
        index = index + 1
    end
    
    for _, item in ipairs(regularItems) do
        questList:moveChildToIndex(item, index)
        table.insert(questLogCache.items, item)
        index = index + 1
    end
    
    recolorVisibleItems()
    updateQuestCounter()
end

-- Filtrar lista de quests
local function filterQuestList(searchText)
    local showComplete = UICheckBox.showComplete:isChecked()
    local showHidden = UICheckBox.showShidden:isChecked()
    local searchPattern = searchText and string.lower(searchText) or nil
    
    questLogCache.visible = 0
    
    for _, child in pairs(questLogCache.items) do
        local isCompleted = child.isComplete
        local isHidden = child.isHiddenQuestLog
        local text = child:getText()
        local visible = true
        
        if searchPattern and text then
            visible = string.find(string.lower(text), searchPattern) ~= nil
        end
        
        if not showComplete and isCompleted then
            visible = false
        end
        
        if showHidden then
            visible = visible and isHidden
        else
            visible = visible and not isHidden
        end
        
        child:setVisible(visible)
        if visible then
            questLogCache.visible = questLogCache.visible + 1
        end
    end
    
    recolorVisibleItems()
end
```

### 🎨 **Estilo OTUI para Quest Log**

```otui
QuestLogWindow < MainWindow
  size: 800 600
  &minimumSize: 600 400

  Panel
    id: panelQuestLog
    anchors.fill: parent
    layout: horizontalBox

    Panel
      id: areaPanelQuestList
      size: 300 0
      layout: verticalBox

      TextEdit
        id: textEditSearchQuest
        size: 0 25
        margin: 2

      Panel
        id: filterPanel
        size: 0 30
        layout: horizontalBox

        Label
          text: "Complete:"
          size: 60 0

        Label
          id: lblCompleteNumber
          text: "0"
          size: 30 0

        Label
          text: "Hidden:"
          size: 60 0

        Label
          id: lblHiddenNumber
          text: "0"
          size: 30 0

        CheckBox
          id: checkboxShowComplete
          text: "Show Complete"
          size: 100 0

        CheckBox
          id: checkboxShowShidden
          text: "Show Hidden"
          size: 100 0

      TextList
        id: questList
        size: 0 0
        vertical-scrollbar: true

  Panel
    id: panelQuestLineSelected
    size: 0 0
    layout: verticalBox

    Label
      text: "Quest Details"
      size: 0 25
      text-align: center

    Panel
      size: 0 0
      layout: horizontalBox

      ScrollArea
        id: ScrollAreaQuestList
        size: 200 0
        vertical-scrollbar: true

        TextList
          id: questList
          size: 0 0

      Panel
        id: panelQuestInfo
        size: 0 0
        layout: verticalBox

        TextList
          id: questList
          size: 0 0
          text-wrap: true

        CheckBox
          id: checkboxShowInQuestTracker
          text: "Show in Quest Tracker"
          size: 0 25

QuestLogLabel < Label
  size: 0 25
  text-offset: 5 0
  focusable: true

  $hover:
    background-color: #585858

  $checked:
    background-color: #585858

QuestLogTracker < MiniWindow
  size: 250 200
  &minimumSize: 200 150

  Panel
    id: contentsPanel
    anchors.fill: parent
    layout: verticalBox

    TextList
      id: list
      size: 0 0
      vertical-scrollbar: true

QuestTrackerLabel < Label
  size: 0 0
  text-wrap: true
  margin: 2

  Label
    id: description
    size: 0 0
    text-wrap: true
    margin-top: 5
```

---

## 💡 Exemplos Práticos

### 🎯 **Exemplo 1: Sistema de Quest Básico**

```lua
local QuestSystem = {}

function QuestSystem.createBasicQuestSystem()
    -- Criar interface de quest log
    local questWindow = g_ui.createWidget('QuestLogWindow', rootWidget)
    questWindow:hide()
    
    -- Configurar lista de quests
    local questList = questWindow:getChildById('questList')
    
    -- Adicionar quests de exemplo
    local quests = {
        {id = 1, name = "The Lost Sword", completed = false},
        {id = 2, name = "Dragon Slayer", completed = true},
        {id = 3, name = "Ancient Ruins", completed = false}
    }
    
    for _, questData in ipairs(quests) do
        local questItem = g_ui.createWidget('QuestLogLabel', questList)
        questItem:setId(questData.id)
        questItem:setText(questData.name)
        
        if questData.completed then
            questItem:setIcon('/images/checkmark-icon')
            questItem.isComplete = true
        end
        
        questItem.onClick = function()
            QuestSystem.showQuestDetails(questData.id)
        end
    end
    
    return questWindow
end

function QuestSystem.showQuestDetails(questId)
    -- Solicitar detalhes da quest ao servidor
    g_game.requestQuestLine(questId)
end

-- Uso
local questSystem = QuestSystem.createBasicQuestSystem()
```

### 🎨 **Exemplo 2: Sistema de Quest Tracker**

```lua
local QuestTrackerSystem = {}

function QuestTrackerSystem.createQuestTracker()
    local trackerWindow = g_ui.createWidget('QuestLogTracker', rootWidget)
    trackerWindow:hide()
    
    local trackerList = trackerWindow:getChildById('list')
    
    -- Configurar tracking de quests
    local trackedQuests = {
        {id = 1, name = "The Lost Sword", progress = 50},
        {id = 2, name = "Ancient Ruins", progress = 25}
    }
    
    for _, questData in ipairs(trackedQuests) do
        local trackerItem = g_ui.createWidget('QuestTrackerLabel', trackerList)
        trackerItem:setId(questData.id)
        trackerItem:setText(questData.name)
        
        local progressBar = g_ui.createWidget('UIProgressBar', trackerItem)
        progressBar:setPercent(questData.progress)
        progressBar:setSize({width = 200, height = 15})
        progressBar:setPosition({x = 5, y = 25})
    end
    
    return trackerWindow
end

function QuestTrackerSystem.addQuestToTracker(questId, questName)
    local trackerWindow = g_ui.getWidgetById('questTracker')
    if not trackerWindow then
        return
    end
    
    local trackerList = trackerWindow:getChildById('list')
    local trackerItem = g_ui.createWidget('QuestTrackerLabel', trackerList)
    trackerItem:setId(questId)
    trackerItem:setText(questName)
    
    -- Salvar configuração
    QuestTrackerSystem.saveTrackingConfig(questId, questName)
end

function QuestTrackerSystem.saveTrackingConfig(questId, questName)
    local settings = QuestTrackerSystem.loadSettings()
    if not settings.trackedQuests then
        settings.trackedQuests = {}
    end
    
    table.insert(settings.trackedQuests, {
        id = questId,
        name = questName,
        added = os.time()
    })
    
    QuestTrackerSystem.saveSettings(settings)
end

-- Uso
local questTracker = QuestTrackerSystem.createQuestTracker()
```

### 🪟 **Exemplo 3: Sistema de Quest Avançado**

```lua
local AdvancedQuestSystem = {}

function AdvancedQuestSystem.createAdvancedQuestSystem()
    local questSystem = {
        window = nil,
        questList = {},
        tracker = nil,
        filters = {},
        sortOrder = "Alphabetically (A-Z)"
    }
    
    -- Criar janela principal
    questSystem.window = g_ui.createWidget('QuestLogWindow', rootWidget)
    questSystem.window:hide()
    
    -- Configurar filtros
    questSystem.filters = {
        showComplete = true,
        showHidden = false,
        searchText = ""
    }
    
    -- Configurar eventos
    questSystem:setupEvents()
    
    return questSystem
end

function AdvancedQuestSystem:setupEvents()
    -- Evento de recebimento de quest log
    connect(g_game, {
        onQuestLog = function(questList)
            self:onQuestLogReceived(questList)
        end,
        
        onQuestLine = function(questId, questMissions)
            self:onQuestLineReceived(questId, questMissions)
        end,
        
        onQuestTracker = function(remainingQuests, missions)
            self:onQuestTrackerReceived(remainingQuests, missions)
        end
    })
end

function AdvancedQuestSystem:onQuestLogReceived(questList)
    local questListWidget = self.window:getChildById('questList')
    questListWidget:destroyChildren()
    
    self.questList = {}
    
    for _, questData in ipairs(questList) do
        local id, questName, questCompleted = unpack(questData)
        
        local questItem = g_ui.createWidget('QuestLogLabel', questListWidget)
        questItem:setId(id)
        questItem:setText(questName)
        
        if questCompleted then
            questItem:setIcon('/images/checkmark-icon')
            questItem.isComplete = true
        end
        
        questItem.onClick = function()
            self:selectQuest(id, questName)
        end
        
        table.insert(self.questList, questItem)
    end
    
    self:applyFilters()
    self:sortQuestList()
end

function AdvancedQuestSystem:selectQuest(questId, questName)
    -- Solicitar detalhes da quest
    g_game.requestQuestLine(questId)
    
    -- Atualizar interface
    local selectedPanel = self.window:getChildById('panelQuestLineSelected')
    selectedPanel:getChildById('questTitle'):setText(questName)
end

function AdvancedQuestSystem:applyFilters()
    for _, questItem in ipairs(self.questList) do
        local visible = true
        
        -- Filtro de busca
        if self.filters.searchText and self.filters.searchText ~= "" then
            local questName = questItem:getText():lower()
            local searchText = self.filters.searchText:lower()
            visible = string.find(questName, searchText) ~= nil
        end
        
        -- Filtro de quests completas
        if not self.filters.showComplete and questItem.isComplete then
            visible = false
        end
        
        -- Filtro de quests ocultas
        if self.filters.showHidden and not questItem.isHidden then
            visible = false
        end
        
        questItem:setVisible(visible)
    end
end

function AdvancedQuestSystem:sortQuestList()
    local questListWidget = self.window:getChildById('questList')
    local items = questListWidget:getChildren()
    
    local sortFunctions = {
        ["Alphabetically (A-Z)"] = function(a, b)
            return a:getText() < b:getText()
        end,
        ["Alphabetically (Z-A)"] = function(a, b)
            return a:getText() > b:getText()
        end,
        ["Completed on Top"] = function(a, b)
            if a.isComplete and not b.isComplete then
                return true
            elseif not a.isComplete and b.isComplete then
                return false
            else
                return a:getText() < b:getText()
            end
        end
    }
    
    local sortFunc = sortFunctions[self.sortOrder]
    if sortFunc then
        table.sort(items, sortFunc)
        
        -- Reorganizar widgets
        for i, item in ipairs(items) do
            questListWidget:moveChildToIndex(item, i)
        end
    end
end

-- Uso
local advancedQuestSystem = AdvancedQuestSystem.createAdvancedQuestSystem()
```

---

## ✅ Melhores Práticas

### 🎯 **Uso Eficiente**

```lua
-- ✅ BOM: Sempre verificar se a janela existe
function showQuestLog()
    if not questLogController.ui then
        return
    end
    
    questLogController.ui:show()
    questLogController.ui:raise()
    questLogController.ui:focus()
end

-- ✅ BOM: Gerenciar cache de quests
function updateQuestCache(questList)
    questLogCache = {
        items = {},
        completed = 0,
        hidden = 0,
        visible = #questList
    }
    
    for _, questData in ipairs(questList) do
        local id, questName, questCompleted = unpack(questData)
        local questItem = createQuestItem(questList, id, questName, color, icon)
        
        if questCompleted then
            questLogCache.completed = questLogCache.completed + 1
        end
    end
end

-- ✅ BOM: Validar dados de quest
function validateQuestData(questData)
    if not questData or type(questData) ~= 'table' then
        return false
    end
    
    if not questData.id or not questData.name then
        return false
    end
    
    return true
end

-- ❌ EVITE: Não verificar existência de widgets
function badShowQuestLog()
    questLogController.ui:show()  -- Pode falhar se ui não existir
end

-- ❌ EVITE: Não gerenciar cache
function badUpdateQuests(questList)
    -- Sem gerenciamento de cache - pode causar vazamentos
    for _, quest in ipairs(questList) do
        createQuestItem(questList, quest.id, quest.name)
    end
end
```

### 🎨 **Organização de Código**

```lua
-- ✅ BOM: Separar responsabilidades
local QuestDataManager = {
    cache = {},
    settings = {}
}

function QuestDataManager:addQuest(questData)
    if not validateQuestData(questData) then
        return false
    end
    
    self.cache[questData.id] = questData
    return true
end

function QuestDataManager:getQuest(questId)
    return self.cache[questId]
end

function QuestDataManager:saveSettings()
    local settingsData = {
        trackedQuests = self.settings.trackedQuests,
        filters = self.settings.filters,
        sortOrder = self.settings.sortOrder
    }
    
    g_resources.writeFileContents('/settings/quests.json', json.encode(settingsData))
end

-- ✅ BOM: Usar callbacks para flexibilidade
function createQuestWithCallbacks(questData, callbacks)
    local questItem = g_ui.createWidget('QuestLogLabel', parent)
    questItem:setId(questData.id)
    questItem:setText(questData.name)
    
    if callbacks.onCreate then
        callbacks.onCreate(questItem)
    end
    
    if callbacks.onSelect then
        questItem.onClick = function()
            callbacks.onSelect(questItem)
        end
    end
    
    return questItem
end

-- ✅ BOM: Sistema de eventos
local QuestEventSystem = {
    listeners = {}
}

function QuestEventSystem:addEventListener(event, callback)
    if not self.listeners[event] then
        self.listeners[event] = {}
    end
    
    table.insert(self.listeners[event], callback)
end

function QuestEventSystem:triggerEvent(event, data)
    if self.listeners[event] then
        for _, callback in ipairs(self.listeners[event]) do
            callback(data)
        end
    end
end
```

### 🔧 **Performance e Otimização**

```lua
-- ✅ BOM: Lazy loading de quests
local QuestLazyLoader = {
    loadedQuests = {},
    questCache = {}
}

function QuestLazyLoader:loadQuest(questId)
    if self.loadedQuests[questId] then
        return self.loadedQuests[questId]
    end
    
    -- Carregar quest do servidor
    g_game.requestQuestLine(questId)
    
    -- Criar placeholder
    local placeholder = g_ui.createWidget('Label')
    placeholder:setText('Loading...')
    
    self.loadedQuests[questId] = placeholder
    return placeholder
end

-- ✅ BOM: Debounce para busca
local searchDebounce = nil

function debouncedSearch(searchText)
    if searchDebounce then
        removeEvent(searchDebounce)
    end
    
    searchDebounce = scheduleEvent(function()
        filterQuestList(searchText)
        searchDebounce = nil
    end, 300)  -- 300ms delay
end

-- ✅ BOM: Pool de widgets para quests
local QuestWidgetPool = {
    available = {},
    inUse = {}
}

function QuestWidgetPool:getWidget()
    if #self.available > 0 then
        local widget = table.remove(self.available)
        table.insert(self.inUse, widget)
        return widget
    end
    
    local widget = g_ui.createWidget('QuestLogLabel')
    table.insert(self.inUse, widget)
    return widget
end

function QuestWidgetPool:returnWidget(widget)
    widget:hide()
    widget:setText("")
    widget:setId("")
    
    table.removevalue(self.inUse, widget)
    table.insert(self.available, widget)
end
```

### 🎨 **Estilização e Temas**

```lua
-- ✅ BOM: Sistema de temas para quests
local questThemes = {
    default = {
        backgroundColor = '#2c2c2c',
        textColor = '#ffffff',
        selectedColor = '#4a90e2',
        completedColor = '#27ae60',
        hiddenColor = '#7f8c8d'
    },
    
    dark = {
        backgroundColor = '#1a1a1a',
        textColor = '#e0e0e0',
        selectedColor = '#007acc',
        completedColor = '#2ecc71',
        hiddenColor = '#95a5a6'
    },
    
    light = {
        backgroundColor = '#f5f5f5',
        textColor = '#333333',
        selectedColor = '#2196f3',
        completedColor = '#4caf50',
        hiddenColor = '#9e9e9e'
    }
}

function applyQuestTheme(themeName)
    local theme = questThemes[themeName] or questThemes.default
    
    for _, questItem in ipairs(questLogCache.items) do
        questItem:setBackgroundColor(theme.backgroundColor)
        questItem:setColor(theme.textColor)
        
        if questItem.isComplete then
            questItem:setColor(theme.completedColor)
        end
        
        if questItem.isHidden then
            questItem:setColor(theme.hiddenColor)
        end
    end
end

-- ✅ BOM: Animações suaves
function createAnimatedQuestSystem()
    local questSystem = createBasicQuestSystem()
    
    -- Animação de entrada
    questSystem.window:setOpacity(0)
    questSystem.window:show()
    
    local animation = questSystem.window:createAnimation()
    animation:setDuration(200)
    animation:setOpacity(1)
    animation:start()
    
    return questSystem
end
```

O sistema de quest e missões oferece ferramentas poderosas para gerenciar o progresso do jogador no OTClient. Seguindo as melhores práticas e utilizando os exemplos fornecidos, você pode criar sistemas de quest robustos e eficientes que melhoram significativamente a experiência do usuário.

---

> [!success] **Navegação**
> **📚 Documentos Relacionados:**
> - [[Game_Systems_Guide]] - Sistemas de jogo
> - [[Creature_System_Guide]] - Sistema de criaturas
> - [[Item_System_Guide]] - Sistema de itens
> - [[Game_Trading_System_Guide]] - Sistema de trade
> 
> **🔗 Navegação Rápida:**
> - [[Wiki_Index]] - Voltar ao índice
> - [[Cheat_Sheet]] - Referência rápida
> - [[Getting_Started_Guide]] - Comece aqui 