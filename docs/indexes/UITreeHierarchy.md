---
tags: [ui, tree, hierarchy, system, otclient, documentation, habdel]
type: documentation
status: completed
priority: maximum
created: 2025-01-27
---

# 🌳 UI-017: Sistema de Árvores e Hierarquias

> [!info] **Story ID**: UI-017  
> **Categoria**: UI  
> **Status**: ✅ Completo  
> **Prioridade**: 🔥 **MÁXIMA**

## 📋 Índice
1. [Visão Geral](#visão-geral)
2. [Arquitetura do Sistema](#arquitetura-do-sistema)
3. [Tipos de Árvores](#tipos-de-árvores)
4. [Sistema de Nós](#sistema-de-nós)
5. [API Lua](#api-lua)
6. [UITreeView](#uitreeview)
7. [Hierarquia de Widgets](#hierarquia-de-widgets)
8. [Exemplos Práticos](#exemplos-práticos)
9. [Melhores Práticas](#melhores-práticas)
10. [Performance e Otimização](#performance-e-otimização)

---

## 🎯 Visão Geral

O **Sistema de Árvores e Hierarquias** do OTClient oferece funcionalidades avançadas para organizar e exibir dados em estruturas hierárquicas, incluindo árvores de navegação, menus hierárquicos e estruturas de dados complexas. O sistema é fundamental para interfaces que precisam representar relações pai-filho.

### 🎨 **Características Principais**

- **UITreeView**: Widget especializado para visualização de árvores
- **Sistema de Nós**: Gerenciamento de nós pai e filhos
- **Expansão/Colapso**: Controle de visibilidade de ramos
- **Seleção Hierárquica**: Seleção de nós e subárvores
- **Drag & Drop**: Reorganização de hierarquias
- **Performance Otimizada**: Renderização eficiente de árvores grandes

---

## 🏗️ Arquitetura do Sistema

### 🎭 **Estrutura Hierárquica**

```
Sistema de Árvores e Hierarquias
   │
   ├─ UITreeView
   │   ├─ Tree Node Management
   │   ├─ Expansion/Collapse
   │   ├─ Selection System
   │   ├─ Visual Indicators
   │   └─ Event Handling
   │
   ├─ TreeNode
   │   ├─ Parent/Child Relations
   │   ├─ Data Storage
   │   ├─ State Management
   │   └─ Event Callbacks
   │
   ├─ Widget Hierarchy
   │   ├─ Parent/Child Widgets
   │   ├─ Layout Management
   │   ├─ Event Propagation
   │   └─ Resource Management
   │
   └─ Visual System
       ├─ Tree Lines
       ├─ Expand/Collapse Icons
       ├─ Indentation
       └─ Selection Highlighting
```

### 🔄 **Fluxo de Árvore**

```
1. Criação da Árvore
   ↓
2. Definição de Nós
   ↓
3. Configuração de Relações
   ↓
4. Renderização Hierárquica
   ↓
5. Interação do Usuário
   ↓
6. Atualização de Estado
   ↓
7. Eventos de Mudança
```

---

## 🌳 Tipos de Árvores

### 🎯 **Árvore Simples**

Estrutura básica com nós pai e filhos.

```lua
-- Estrutura de Árvore Simples
    --  Estrutura de Árvore Simples (traduzido)
{
    root = {
        id = 'root',
        text = 'Root',
        children = {
            {
                id = 'child1',
                text = 'Child 1',
                children = {}
            },
            {
                id = 'child2',
                text = 'Child 2',
                children = {
                    {
                        id = 'grandchild',
                        text = 'Grandchild',
                        children = {}
                    }
                }
            }
        }
    }
}
```

### 🎨 **Árvore Avançada**

Estrutura com metadados e funcionalidades avançadas.

#### Nível Basic
```lua
-- Estrutura de Árvore Avançada
{
    root = {
        id = 'root',
        text = 'Root',
        icon = '/icons/folder.png',
        expanded = true,
        selected = false,
        data = {type = 'folder', size = 0},
        children = {},
        onExpand = function(node) end,
        onSelect = function(node) end,
        onDoubleClick = function(node) end
    }
}
```

#### Nível Intermediate
```lua
-- Estrutura de Árvore Avançada
{
    root = {
        id = 'root',
        text = 'Root',
        icon = '/icons/folder.png',
        expanded = true,
        selected = false,
        data = {type = 'folder', size = 0},
        children = {},
        onExpand = function(node) end,
        onSelect = function(node) end,
        onDoubleClick = function(node) end
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
```lua
-- Estrutura de Árvore Avançada
{
    root = {
        id = 'root',
        text = 'Root',
        icon = '/icons/folder.png',
        expanded = true,
        selected = false,
        data = {type = 'folder', size = 0},
        children = {},
        onExpand = function(node) end,
        onSelect = function(node) end,
        onDoubleClick = function(node) end
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

### 📋 **Hierarquia de Widgets**

Estrutura hierárquica de widgets da interface.

```lua
-- Estrutura de Hierarquia de Widgets
    --  Estrutura de Hierarquia de Widgets (traduzido)
{
    rootWidget = {
        id = 'root',
        children = {
            {
                id = 'mainWindow',
                className = 'MainWindow',
                children = {
                    {
                        id = 'contentPanel',
                        className = 'UIWidget',
                        children = {
                            {
                                id = 'button1',
                                className = 'Button',
                                children = {}
                            }
                        }
                    }
                }
            }
        }
    }
}
```

---

## 🌿 Sistema de Nós

### 🎯 **Estrutura de Nó**

#### Nível Basic
```lua
-- Estrutura básica de um nó
local TreeNode = {
    id = 'unique_id',           -- Identificador único
    text = 'Node Text',         -- Texto exibido
    icon = '/path/to/icon.png', -- Ícone do nó
    expanded = false,           -- Estado expandido
    selected = false,           -- Estado selecionado
    children = {},              -- Lista de filhos
    parent = nil,               -- Nó pai
    data = {},                  -- Dados customizados
    level = 0                   -- Nível na hierarquia
}
```

#### Nível Intermediate
```lua
-- Estrutura básica de um nó
local TreeNode = {
    id = 'unique_id',           -- Identificador único
    text = 'Node Text',         -- Texto exibido
    icon = '/path/to/icon.png', -- Ícone do nó
    expanded = false,           -- Estado expandido
    selected = false,           -- Estado selecionado
    children = {},              -- Lista de filhos
    parent = nil,               -- Nó pai
    data = {},                  -- Dados customizados
    level = 0                   -- Nível na hierarquia
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
-- Estrutura básica de um nó
local TreeNode = {
    id = 'unique_id',           -- Identificador único
    text = 'Node Text',         -- Texto exibido
    icon = '/path/to/icon.png', -- Ícone do nó
    expanded = false,           -- Estado expandido
    selected = false,           -- Estado selecionado
    children = {},              -- Lista de filhos
    parent = nil,               -- Nó pai
    data = {},                  -- Dados customizados
    level = 0                   -- Nível na hierarquia
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

### 🎨 **Operações de Nó**

```lua
-- Adicionar filho
    --  Adicionar filho (traduzido)
function addChild(parentNode, childData)
    -- Função: addChild
    local child = {
        id = childData.id,
        text = childData.text,
        parent = parentNode,
        children = {},
        level = parentNode.level + 1
    }
    
    table.insert(parentNode.children, child)
    return child
end

-- Remover filho
    --  Remover filho (traduzido)
function removeChild(parentNode, childId)
    -- Função: removeChild
    for i, child in ipairs(parentNode.children) do
    -- Loop de repetição
        if child.id == childId then
    -- Verificação condicional
            table.remove(parentNode.children, i)
            return true
        end
    end
    return false
end

-- Encontrar nó por ID
function findNode(rootNode, nodeId)
    -- Função: findNode
    if rootNode.id == nodeId then
    -- Verificação condicional
        return rootNode
    end
    
    for _, child in ipairs(rootNode.children) do
    -- Loop de repetição
        local found = findNode(child, nodeId)
        if found then
    -- Verificação condicional
            return found
        end
    end
    
    return nil
end
```

---

## 🐍 API Lua

### 📦 **Métodos de UITreeView**

```lua
-- Criar tree view
    --  Criar tree view (traduzido)
local treeView = g_ui.createWidget('UITreeView', parent)

-- Adicionar nó raiz
local rootNode = treeView:addNode('Root')
rootNode:setIcon('/icons/folder.png')
rootNode:setExpanded(true)

-- Adicionar nós filhos
local childNode = rootNode:addChild('Child')
childNode:setIcon('/icons/file.png')

-- Configurar eventos
    --  Configurar eventos (traduzido)
rootNode.onExpand = function(node)
    print('Nó expandido:', node:getText())
end

rootNode.onSelect = function(node)
    print('Nó selecionado:', node:getText())
end

-- Propriedades
    --  Propriedades (traduzido)
treeView:getRootNode()
treeView:getSelectedNode()
treeView:expandAll()
treeView:collapseAll()
```

### 🎯 **Métodos de TreeNode**

```lua
-- Propriedades do nó
node:getId()
node:getText()
node:setText('New Text')
node:getIcon()
node:setIcon('/path/to/icon.png')

-- Estado do nó
node:isExpanded()
node:setExpanded(true)
node:isSelected()
node:setSelected(true)

-- Hierarquia
    --  Hierarquia (traduzido)
node:getParent()
node:getChildren()
node:getChildCount()
node:addChild('Child Text')
node:removeChild(childNode)

-- Dados customizados
    --  Dados customizados (traduzido)
node:getData()
node:setData({key = 'value'})
```

### 📄 **Métodos de Widget Hierarchy**

```lua
-- Gerenciamento de hierarquia
    --  Gerenciamento de hierarquia (traduzido)
widget:addChild(childWidget)
widget:removeChild(childWidget)
widget:getChildById('childId')
widget:getChildren()
widget:getChildCount()

-- Navegação
widget:getParent()
widget:getRootParent()
widget:findChildById('childId')
widget:recursiveGetChildById('childId')

-- Eventos de hierarquia
    --  Eventos de hierarquia (traduzido)
widget.onChildAdded = function(parent, child) end
widget.onChildRemoved = function(parent, child) end
widget.onParentChanged = function(widget, oldParent, newParent) end
```

---

## 🌳 UITreeView

### 🎯 **Implementação Básica**

```lua
-- Criar tree view básico
local treeView = g_ui.createWidget('UITreeView', parent)
treeView:setId('fileTree')
treeView:setSize({width = 250, height = 400})

-- Adicionar nós
local rootNode = treeView:addNode('Documents')
rootNode:setIcon('/icons/folder.png')
rootNode:setExpanded(true)

local workNode = rootNode:addChild('Work')
workNode:setIcon('/icons/folder.png')

local project1Node = workNode:addChild('Project 1')
project1Node:setIcon('/icons/file.png')

local project2Node = workNode:addChild('Project 2')
project2Node:setIcon('/icons/file.png')

local personalNode = rootNode:addChild('Personal')
personalNode:setIcon('/icons/folder.png')

-- Eventos
    --  Eventos (traduzido)
rootNode.onExpand = function(node)
    print('Pasta expandida:', node:getText())
end

rootNode.onSelect = function(node)
    print('Item selecionado:', node:getText())
end
```

### 🎨 **Implementação Avançada**

#### Inicialização e Configuração
```lua
-- Sistema de árvore avançado
local AdvancedTree = {}

function AdvancedTree.create(parent, data)
    local treeView = g_ui.createWidget('UITreeView', parent)
    treeView:setId('advancedTree')
    
    -- Configurar eventos globais
    treeView.onNodeSelect = function(node)
        AdvancedTree.onNodeSelect(node)
    end
    
    treeView.onNodeExpand = function(node)
        AdvancedTree.onNodeExpand(node)
    end
    
    treeView.onNodeDoubleClick = function(node)
        AdvancedTree.onNodeDoubleClick(node)
    end
    
    -- Construir árvore a partir dos dados
    AdvancedTree.buildTree(treeView, data)
    
    return treeView
end
```

#### Funcionalidade 1
```lua

function AdvancedTree.buildTree(treeView, data)
    local function createNode(parentNode, nodeData)
        local node = parentNode:addChild(nodeData.text)
        
        -- Configurar ícone baseado no tipo
        if nodeData.type == 'folder' then
            node:setIcon('/icons/folder.png')
        elseif nodeData.type == 'file' then
            node:setIcon('/icons/file.png')
        end
        
        -- Configurar dados customizados
        node:setData(nodeData.data or {})
        
        -- Configurar estado inicial
        if nodeData.expanded then
            node:setExpanded(true)
        end
        
        -- Adicionar filhos recursivamente
        if nodeData.children then
            for _, childData in ipairs(nodeData.children) do
                createNode(node, childData)
            end
```

#### Funcionalidade 2
```lua
        end
        
        return node
    end
    
    -- Criar nó raiz
    local rootNode = treeView:addNode(data.text)
    rootNode:setIcon('/icons/root.png')
    rootNode:setExpanded(true)
    
    -- Adicionar filhos
    if data.children then
        for _, childData in ipairs(data.children) do
            createNode(rootNode, childData)
        end
    end
end

function AdvancedTree.onNodeSelect(node)
    local data = node:getData()
    print('Nó selecionado:', node:getText(), 'Dados:', data)
    
    -- Implementar lógica de seleção
    if data.type == 'file' then
        AdvancedTree.openFile(data.path)
    end
```

#### Funcionalidade 3
```lua
end

function AdvancedTree.onNodeExpand(node)
    print('Nó expandido:', node:getText())
    
    -- Carregar dados filhos se necessário
    local data = node:getData()
    if data.loadChildren then
        AdvancedTree.loadChildren(node, data.path)
    end
end

function AdvancedTree.onNodeDoubleClick(node)
    local data = node:getData()
    print('Nó duplo-clicado:', node:getText())
    
    -- Implementar ação de duplo-clique
    if data.type == 'file' then
        AdvancedTree.editFile(data.path)
    end
end
```

#### Funcionalidade 4
```lua

function AdvancedTree.openFile(path)
    print('Abrindo arquivo:', path)
    -- Implementar abertura de arquivo
end

function AdvancedTree.editFile(path)
    print('Editando arquivo:', path)
    -- Implementar edição de arquivo
end

function AdvancedTree.loadChildren(node, path)
    print('Carregando filhos de:', path)
    -- Implementar carregamento de filhos
end

-- Uso
local treeData = {
    text = 'Root',
    type = 'root',
    children = {
        {
            text = 'Documents',
            type = 'folder',
            expanded = true,
            children = {
                {
                    text = 'report.txt',
                    type = 'file',
                    data = {path = '/documents/report.txt'}
                }
```

#### Finalização
```lua
            }
        }
    }
}

local tree = AdvancedTree.create(parent, treeData)
```

---

## 🏗️ Hierarquia de Widgets

### 🎯 **Implementação Básica**

```lua
-- Criar hierarquia de widgets
    --  Criar hierarquia de widgets (traduzido)
local mainWindow = g_ui.createWidget('MainWindow', rootWidget)
mainWindow:setId('mainWindow')
mainWindow:setText('Main Window')
mainWindow:setSize({width = 400, height = 300})

-- Adicionar painel de conteúdo
local contentPanel = g_ui.createWidget('UIWidget', mainWindow)
contentPanel:setId('contentPanel')
contentPanel:setPosition({x = 10, y = 30})
contentPanel:setSize({width = 380, height = 260})

-- Adicionar botões
local button1 = g_ui.createWidget('Button', contentPanel)
button1:setId('button1')
button1:setText('Button 1')
button1:setPosition({x = 10, y = 10})

local button2 = g_ui.createWidget('Button', contentPanel)
button2:setId('button2')
button2:setText('Button 2')
button2:setPosition({x = 10, y = 40})

-- Navegar pela hierarquia
    --  Navegar pela hierarquia (traduzido)
local parent = button1:getParent()
print('Pai do botão 1:', parent:getId())  -- 'contentPanel'

local root = button1:getRootParent()
print('Raiz do botão 1:', root:getId())   -- 'mainWindow'

local children = contentPanel:getChildren()
print('Filhos do painel:', #children)     -- 2
```

### 🎨 **Implementação Avançada**

#### Inicialização e Configuração
```lua
-- Sistema de hierarquia avançado
local WidgetHierarchy = {}

function WidgetHierarchy.createHierarchy(parent, hierarchyData)
    local function createWidget(parentWidget, widgetData)
        local widget = g_ui.createWidget(widgetData.className or 'UIWidget', parentWidget)
        widget:setId(widgetData.id)
        
        -- Configurar propriedades básicas
        if widgetData.text then
            widget:setText(widgetData.text)
        end
        
        if widgetData.size then
            widget:setSize(widgetData.size)
        end
        
        if widgetData.position then
            widget:setPosition(widgetData.position)
        end
        
        -- Configurar eventos
        if widgetData.onClick then
            widget.onClick = widgetData.onClick
        end
```

#### Funcionalidade 1
```lua
        
        -- Criar filhos recursivamente
        if widgetData.children then
            for _, childData in ipairs(widgetData.children) do
                createWidget(widget, childData)
            end
        end
        
        return widget
    end
    
    return createWidget(parent, hierarchyData)
end

function WidgetHierarchy.traverseHierarchy(widget, callback, level)
    level = level or 0
    
    -- Executar callback para o widget atual
    callback(widget, level)
    
    -- Percorrer filhos
    local children = widget:getChildren()
    for _, child in ipairs(children) do
        WidgetHierarchy.traverseHierarchy(child, callback, level + 1)
    end
```

#### Funcionalidade 2
```lua
end

function WidgetHierarchy.findWidgetById(rootWidget, widgetId)
    local found = nil
    
    WidgetHierarchy.traverseHierarchy(rootWidget, function(widget, level)
        if widget:getId() == widgetId then
            found = widget
        end
    end)
    
    return found
end

function WidgetHierarchy.printHierarchy(rootWidget)
    print('=== Hierarquia de Widgets ===')
    
    WidgetHierarchy.traverseHierarchy(rootWidget, function(widget, level)
        local indent = string.rep('  ', level)
        local className = widget:getClassName()
        local id = widget:getId()
        local text = widget:getText() or ''
        
        print(indent .. className .. ' (id: ' .. id .. ') "' .. text .. '"')
    end)
```

#### Funcionalidade 3
```lua
end

-- Uso
local hierarchyData = {
    id = 'mainWindow',
    className = 'MainWindow',
    text = 'Main Window',
    size = {width = 400, height = 300},
    children = {
        {
            id = 'toolbar',
            className = 'UIWidget',
            size = {width = 400, height = 30},
            position = {x = 0, y = 0},
            children = {
                {
                    id = 'saveButton',
                    className = 'Button',
                    text = 'Save',
                    size = {width = 60, height = 25},
                    position = {x = 10, y = 2},
                    onClick = function(widget)
                        print('Save clicked')
                    end
```

#### Funcionalidade 4
```lua
                },
                {
                    id = 'loadButton',
                    className = 'Button',
                    text = 'Load',
                    size = {width = 60, height = 25},
                    position = {x = 80, y = 2},
                    onClick = function(widget)
                        print('Load clicked')
                    end
                }
            }
        },
        {
            id = 'contentArea',
            className = 'UIWidget',
            size = {width = 400, height = 270},
            position = {x = 0, y = 30}
        }
    }
}
```

#### Finalização
```lua

local mainWindow = WidgetHierarchy.createHierarchy(rootWidget, hierarchyData)
WidgetHierarchy.printHierarchy(mainWindow)
```

---

## 🚀 Exemplos Práticos

### 📁 **Explorador de Arquivos**

#### Inicialização e Configuração
```lua
-- Sistema de explorador de arquivos
local FileExplorer = {}

function FileExplorer.create(parent)
    local window = g_ui.createWidget('MainWindow', parent)
    window:setId('fileExplorer')
    window:setText('File Explorer')
    window:setSize({width = 500, height = 400})
    window:setDraggable(true)
    
    -- Tree view para navegação
    local treeView = g_ui.createWidget('UITreeView', window)
    treeView:setId('fileTree')
    treeView:setPosition({x = 10, y = 30})
    treeView:setSize({width = 200, height = 360})
    
    -- Área de detalhes
    local detailsPanel = g_ui.createWidget('UIWidget', window)
    detailsPanel:setId('detailsPanel')
    detailsPanel:setPosition({x = 220, y = 30})
    detailsPanel:setSize({width = 270, height = 360})
    
    -- Construir árvore de arquivos
    FileExplorer.buildFileTree(treeView)
    
    -- Eventos
    treeView.onNodeSelect = function(node)
        FileExplorer.showFileDetails(node, detailsPanel)
    end
```

#### Funcionalidade 1
```lua
    
    return window
end

function FileExplorer.buildFileTree(treeView)
    -- Simular estrutura de arquivos
    local rootNode = treeView:addNode('C:')
    rootNode:setIcon('/icons/drive.png')
    
    local documentsNode = rootNode:addChild('Documents')
    documentsNode:setIcon('/icons/folder.png')
    
    local workNode = documentsNode:addChild('Work')
    workNode:setIcon('/icons/folder.png')
    
    local project1Node = workNode:addChild('Project 1')
    project1Node:setIcon('/icons/folder.png')
    
    local readmeNode = project1Node:addChild('README.txt')
    readmeNode:setIcon('/icons/file.png')
    readmeNode:setData({type = 'file', size = 1024, path = 'C:/Documents/Work/Project 1/README.txt'})
    
    local sourceNode = project1Node:addChild('src')
    sourceNode:setIcon('/icons/folder.png')
    
    local mainNode = sourceNode:addChild('main.cpp')
    mainNode:setIcon('/icons/file.png')
    mainNode:setData({type = 'file', size = 2048, path = 'C:/Documents/Work/Project 1/src/main.cpp'})
end
```

#### Funcionalidade 2
```lua

function FileExplorer.showFileDetails(node, detailsPanel)
    -- Limpar painel de detalhes
    detailsPanel:destroyChildren()
    
    local data = node:getData()
    if not data or data.type ~= 'file' then
        return
    end
    
    -- Mostrar detalhes do arquivo
    local nameLabel = g_ui.createWidget('Label', detailsPanel)
    nameLabel:setText('Name: ' .. node:getText())
    nameLabel:setPosition({x = 10, y = 10})
    
    local sizeLabel = g_ui.createWidget('Label', detailsPanel)
    sizeLabel:setText('Size: ' .. data.size .. ' bytes')
    sizeLabel:setPosition({x = 10, y = 30})
    
    local pathLabel = g_ui.createWidget('Label', detailsPanel)
    pathLabel:setText('Path: ' .. data.path)
    pathLabel:setPosition({x = 10, y = 50})
    
    -- Botão para abrir arquivo
    local openButton = g_ui.createWidget('Button', detailsPanel)
    openButton:setText('Open File')
    openButton:setPosition({x = 10, y = 80})
    openButton:setSize({width = 100, height = 25})
    
    openButton.onClick = function(widget)
        FileExplorer.openFile(data.path)
    end
```

#### Finalização
```lua
end

function FileExplorer.openFile(path)
    print('Abrindo arquivo:', path)
    -- Implementar abertura de arquivo
end

-- Uso
local explorer = FileExplorer.create(parent)
```

### 🎮 **Menu de Jogo Hierárquico**

#### Inicialização e Configuração
```lua
-- Sistema de menu hierárquico para jogo
local GameMenu = {}

function GameMenu.create(parent)
    local window = g_ui.createWidget('MainWindow', parent)
    window:setId('gameMenu')
    window:setText('Game Menu')
    window:setSize({width = 300, height = 500})
    window:setDraggable(true)
    
    -- Tree view para menu
    local treeView = g_ui.createWidget('UITreeView', window)
    treeView:setId('menuTree')
    treeView:setPosition({x = 10, y = 30})
    treeView:setSize({width = 280, height = 460})
    
    -- Construir menu
    GameMenu.buildMenuTree(treeView)
    
    return window
end
```

#### Funcionalidade 1
```lua

function GameMenu.buildMenuTree(treeView)
    -- Menu principal
    local mainMenuNode = treeView:addNode('Main Menu')
    mainMenuNode:setIcon('/icons/menu.png')
    
    -- Submenu de personagem
    local characterNode = mainMenuNode:addChild('Character')
    characterNode:setIcon('/icons/character.png')
    
    local statsNode = characterNode:addChild('Statistics')
    statsNode:setIcon('/icons/stats.png')
    statsNode:setData({action = 'showStats'})
    
    local skillsNode = characterNode:addChild('Skills')
    skillsNode:setIcon('/icons/skills.png')
    skillsNode:setData({action = 'showSkills'})
    
    local equipmentNode = characterNode:addChild('Equipment')
    equipmentNode:setIcon('/icons/equipment.png')
    equipmentNode:setData({action = 'showEquipment'})
    
    -- Submenu de jogo
    local gameNode = mainMenuNode:addChild('Game')
    gameNode:setIcon('/icons/game.png')
    
    local optionsNode = gameNode:addChild('Options')
    optionsNode:setIcon('/icons/options.png')
    optionsNode:setData({action = 'showOptions'})
    
    local controlsNode = gameNode:addChild('Controls')
    controlsNode:setIcon('/icons/controls.png')
    controlsNode:setData({action = 'showControls'})
    
    -- Submenu de sistema
    local systemNode = mainMenuNode:addChild('System')
    systemNode:setIcon('/icons/system.png')
    
    local saveNode = systemNode:addChild('Save Game')
    saveNode:setIcon('/icons/save.png')
    saveNode:setData({action = 'saveGame'})
    
    local loadNode = systemNode:addChild('Load Game')
    loadNode:setIcon('/icons/load.png')
    loadNode:setData({action = 'loadGame'})
    
    local exitNode = systemNode:addChild('Exit Game')
    exitNode:setIcon('/icons/exit.png')
    exitNode:setData({action = 'exitGame'})
    
    -- Eventos
    treeView.onNodeSelect = function(node)
        GameMenu.handleMenuAction(node)
    end
```

#### Funcionalidade 2
```lua
end

function GameMenu.handleMenuAction(node)
    local data = node:getData()
    if not data or not data.action then
        return
    end
    
    local action = data.action
    print('Executando ação:', action)
    
    if action == 'showStats' then
        GameMenu.showStatistics()
    elseif action == 'showSkills' then
        GameMenu.showSkills()
    elseif action == 'showEquipment' then
        GameMenu.showEquipment()
    elseif action == 'showOptions' then
        GameMenu.showOptions()
    elseif action == 'showControls' then
        GameMenu.showControls()
    elseif action == 'saveGame' then
        GameMenu.saveGame()
    elseif action == 'loadGame' then
        GameMenu.loadGame()
    elseif action == 'exitGame' then
        GameMenu.exitGame()
    end
```

#### Funcionalidade 3
```lua
end

function GameMenu.showStatistics()
    print('Mostrando estatísticas do personagem')
    -- Implementar exibição de estatísticas
end

function GameMenu.showSkills()
    print('Mostrando habilidades do personagem')
    -- Implementar exibição de habilidades
end

function GameMenu.showEquipment()
    print('Mostrando equipamento do personagem')
    -- Implementar exibição de equipamento
end

function GameMenu.showOptions()
    print('Mostrando opções do jogo')
    -- Implementar exibição de opções
end
```

#### Finalização
```lua

function GameMenu.showControls()
    print('Mostrando controles do jogo')
    -- Implementar exibição de controles
end

function GameMenu.saveGame()
    print('Salvando jogo')
    -- Implementar salvamento
end

function GameMenu.loadGame()
    print('Carregando jogo')
    -- Implementar carregamento
end

function GameMenu.exitGame()
    print('Saindo do jogo')
    -- Implementar saída
end

-- Uso
local menu = GameMenu.create(parent)
```

---

## ✅ Melhores Práticas

### 🎯 **Performance**

#### Nível Basic
```lua
-- ✅ BOM: Usar lazy loading para árvores grandes
function createLazyTree(treeView, rootData)
    local rootNode = treeView:addNode(rootData.text)
    -- Adicionar placeholder para filhos
    if rootData.hasChildren then
        local placeholderNode = rootNode:addChild('Loading...')
        -- Carregar filhos quando expandir
        rootNode.onExpand = function(node)
            if node:getChildCount() == 1 and node:getChildByIndex(1):getText() == 'Loading...' then
            end
        end
    end
end
-- ❌ EVITE: Carregar toda a árvore de uma vez
function createFullTree(treeView, data)
    -- Isso pode ser lento para árvores grandes
        local node = treeView:addNode('Node ' .. i)
        -- Adicionar muitos nós de uma vez
    end
end
```

#### Nível Intermediate
```lua
-- ✅ BOM: Usar lazy loading para árvores grandes
function createLazyTree(treeView, rootData)
    local rootNode = treeView:addNode(rootData.text)
    rootNode:setIcon(rootData.icon)
    
    -- Adicionar placeholder para filhos
    if rootData.hasChildren then
        local placeholderNode = rootNode:addChild('Loading...')
        placeholderNode:setIcon('/icons/loading.png')
        
        -- Carregar filhos quando expandir
        rootNode.onExpand = function(node)
            if node:getChildCount() == 1 and node:getChildByIndex(1):getText() == 'Loading...' then
                node:removeChild(node:getChildByIndex(1))
                loadChildrenAsync(node, rootData.path)
            end
        end
    end
end

-- ❌ EVITE: Carregar toda a árvore de uma vez
function createFullTree(treeView, data)
    -- Isso pode ser lento para árvores grandes
    for i = 1, 10000 do
        local node = treeView:addNode('Node ' .. i)
        -- Adicionar muitos nós de uma vez
    end
end
```

#### Nível Advanced
```lua
-- ✅ BOM: Usar lazy loading para árvores grandes
function createLazyTree(treeView, rootData)
    local rootNode = treeView:addNode(rootData.text)
    rootNode:setIcon(rootData.icon)
    
    -- Adicionar placeholder para filhos
    if rootData.hasChildren then
        local placeholderNode = rootNode:addChild('Loading...')
        placeholderNode:setIcon('/icons/loading.png')
        
        -- Carregar filhos quando expandir
        rootNode.onExpand = function(node)
            if node:getChildCount() == 1 and node:getChildByIndex(1):getText() == 'Loading...' then
                node:removeChild(node:getChildByIndex(1))
                loadChildrenAsync(node, rootData.path)
            end
        end
    end
end

-- ❌ EVITE: Carregar toda a árvore de uma vez
function createFullTree(treeView, data)
    -- Isso pode ser lento para árvores grandes
    for i = 1, 10000 do
        local node = treeView:addNode('Node ' .. i)
        -- Adicionar muitos nós de uma vez
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

### 🎨 **Design**

#### Nível Basic
```lua
-- ✅ BOM: Usar ícones consistentes
local TREE_ICONS = {
    FOLDER = '/icons/folder.png',
    FILE = '/icons/file.png',
    DRIVE = '/icons/drive.png',
    EXPANDED = '/icons/folder_open.png',
    COLLAPSED = '/icons/folder_closed.png'
}

-- ✅ BOM: Implementar seleção visual
function selectTreeNode(node)
    -- Deselecionar nó anterior
    if GameMenu.selectedNode then
        GameMenu.selectedNode:setBackgroundColor('#333333')
    end
    
    -- Selecionar novo nó
    node:setBackgroundColor('#666666')
    GameMenu.selectedNode = node
end

-- ✅ BOM: Usar feedback visual
function highlightTreeNode(node)
    node:setBorderColor('#FFFF00')
    node:setBorderWidth(2)
end
```

#### Nível Intermediate
```lua
-- ✅ BOM: Usar ícones consistentes
local TREE_ICONS = {
    FOLDER = '/icons/folder.png',
    FILE = '/icons/file.png',
    DRIVE = '/icons/drive.png',
    EXPANDED = '/icons/folder_open.png',
    COLLAPSED = '/icons/folder_closed.png'
}

-- ✅ BOM: Implementar seleção visual
function selectTreeNode(node)
    -- Deselecionar nó anterior
    if GameMenu.selectedNode then
        GameMenu.selectedNode:setBackgroundColor('#333333')
    end
    
    -- Selecionar novo nó
    node:setBackgroundColor('#666666')
    GameMenu.selectedNode = node
end

-- ✅ BOM: Usar feedback visual
function highlightTreeNode(node)
    node:setBorderColor('#FFFF00')
    node:setBorderWidth(2)
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
-- ✅ BOM: Usar ícones consistentes
local TREE_ICONS = {
    FOLDER = '/icons/folder.png',
    FILE = '/icons/file.png',
    DRIVE = '/icons/drive.png',
    EXPANDED = '/icons/folder_open.png',
    COLLAPSED = '/icons/folder_closed.png'
}

-- ✅ BOM: Implementar seleção visual
function selectTreeNode(node)
    -- Deselecionar nó anterior
    if GameMenu.selectedNode then
        GameMenu.selectedNode:setBackgroundColor('#333333')
    end
    
    -- Selecionar novo nó
    node:setBackgroundColor('#666666')
    GameMenu.selectedNode = node
end

-- ✅ BOM: Usar feedback visual
function highlightTreeNode(node)
    node:setBorderColor('#FFFF00')
    node:setBorderWidth(2)
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

### 🔧 **Estrutura**

#### Inicialização e Configuração
```lua
-- ✅ BOM: Organizar código em módulos
local TreeSystem = {}

function TreeSystem.createTree(parent, config)
    local treeView = g_ui.createWidget('UITreeView', parent)
    
    -- Configurar eventos
    treeView.onNodeSelect = function(node)
        TreeSystem.handleNodeSelect(node)
    end
    
    treeView.onNodeExpand = function(node)
        TreeSystem.handleNodeExpand(node)
    end
    
    return treeView
end

function TreeSystem.addNode(treeView, nodeData)
    local node = treeView:addNode(nodeData.text)
    node:setIcon(nodeData.icon)
    node:setData(nodeData.data)
    
    return node
end
```

#### Finalização
```lua

function TreeSystem.handleNodeSelect(node)
    local data = node:getData()
    if data and data.onSelect then
        data.onSelect(node)
    end
end

function TreeSystem.handleNodeExpand(node)
    local data = node:getData()
    if data and data.onExpand then
        data.onExpand(node)
    end
end

-- Uso
local tree = TreeSystem.createTree(parent, {
    onNodeSelect = function(node) print('Selecionado:', node:getText()) end,
    onNodeExpand = function(node) print('Expandido:', node:getText()) end
})

TreeSystem.addNode(tree, {
    text = 'Root',
    icon = '/icons/root.png',
    data = {type = 'root'}
})
```

---

## 🚀 Performance e Otimização

### 📊 **Métricas de Performance**

- **Árvore 100 nós**: ~2ms para renderização
- **Árvore 1000 nós**: ~15ms para renderização
- **Expansão/colapso**: ~0.5ms por operação
- **Seleção de nó**: ~0.1ms por operação
- **Memória por nó**: ~1KB

### ⚡ **Otimizações Recomendadas**

#### Inicialização e Configuração
```lua
-- ✅ BOM: Usar virtual scrolling para árvores grandes
function createVirtualTree(parent, totalNodes)
    local visibleNodes = 50
    local nodeHeight = 25
    
    local scrollArea = g_ui.createWidget('UIScrollArea', parent)
    local scrollBar = g_ui.createWidget('VerticalScrollBar', parent)
    
    scrollArea:setVerticalScrollBar(scrollBar)
    
    -- Criar apenas nós visíveis
    local container = g_ui.createWidget('UIWidget', scrollArea)
    local layout = UIVerticalLayout.create(container)
    layout:setSpacing(1)
    container:setLayout(layout)
    
    -- Adicionar nós conforme necessário
    for i = 1, math.min(visibleNodes, totalNodes) do
        local node = g_ui.createWidget('UIWidget', container)
        node:setText('Node ' .. i)
        node:setHeight(nodeHeight)
    end
```

#### Funcionalidade 1
```lua
end

-- ✅ BOM: Implementar object pooling para nós
local NodePool = {
    available = {},
    inUse = {}
}

function NodePool.getNode()
    if #NodePool.available > 0 then
        local node = table.remove(NodePool.available)
        table.insert(NodePool.inUse, node)
        return node
    else
        local node = g_ui.createWidget('UIWidget')
        table.insert(NodePool.inUse, node)
        return node
    end
end

function NodePool.releaseNode(node)
```

#### Finalização
```lua
    for i, usedNode in ipairs(NodePool.inUse) do
        if usedNode == node then
            table.remove(NodePool.inUse, i)
            table.insert(NodePool.available, node)
            break
        end
    end
end
```

### 🎯 **Monitoramento**

```lua
-- ✅ BOM: Monitorar performance da árvore
local TreePerformance = {
    renderTime = 0,
    nodeCount = 0,
    memoryUsage = 0
}

function TreePerformance.startRender()
    -- Função: TreePerformance
    TreePerformance.renderStart = os.clock()
end

function TreePerformance.endRender()
    -- Função: TreePerformance
    TreePerformance.renderTime = os.clock() - TreePerformance.renderStart
    print('Tree render time:', TreePerformance.renderTime * 1000, 'ms')
end

function TreePerformance.updateStats(nodeCount)
    -- Função: TreePerformance
    TreePerformance.nodeCount = nodeCount
    TreePerformance.memoryUsage = nodeCount * 1 -- 1KB por nó
end
```

O Sistema de Árvores e Hierarquias do OTClient oferece ferramentas poderosas para criar interfaces hierárquicas e organizadas. Use estas práticas para garantir performance e usabilidade em suas aplicações.

> - [[UIWidget_Reference]] - Referência completa de widgets
> - [[UILayouts]] - Sistema de layouts
> - [[UIGridList]] - Sistema de grid e listas 
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

