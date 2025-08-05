---
tags: [otclient, modules, otui, development, completed, guide]
priority: 1
status: completed
aliases: [Module Development, OTUI Guide, Module Creation]
---

# Guia de Desenvolvimento de Módulos OTUI

> [!info] Módulos OTClient
> Este guia ensina como criar módulos completos para o OTClient usando arquivos `.otui` e Lua, seguindo a estrutura padrão do projeto.

> [!tip] Pré-requisitos
> Recomendamos ler [[UI_System_Guide]] antes deste guia para entender os conceitos básicos de widgets.

## 📋 Índice
- [[#Visão Geral da Estrutura]]
- [[#Arquivos .otui - Interface Visual]]
- [[#Arquivos .otmod - Configuração do Módulo]]
- [[#Arquivos .lua - Lógica do Módulo]]
- [[#Funções Principais]]
- [[#Estrutura de Pastas]]
- [[#Exemplos Práticos]]
- [[#Melhores Práticas]]

---

## Visão Geral da Estrutura

Um módulo completo do OTClient é composto por três tipos principais de arquivos:

```
modules/meu_modulo/
├── meu_modulo.otmod    # Configuração do módulo
├── meu_modulo.lua      # Lógica em Lua
├── meu_modulo.otui     # Interface visual
└── images/             # Recursos visuais (opcional)
    └── icon.png
```

### Fluxo de Funcionamento
1. **`.otmod`** - Define como o módulo é carregado
2. **`.otui`** - Define a aparência da interface
3. **`.lua`** - Implementa a funcionalidade
4. **`g_ui.displayUI()`** - Carrega a interface

---

## Arquivos .otui - Interface Visual

> [!note] Linguagem de Marcação
> Arquivos `.otui` são linguagens de marcação para definir interfaces visuais. Eles usam uma sintaxe específica do OTClient.

### Sintaxe Básica

```otui
# Definir um widget personalizado
MeuWidget < UIWidget
  id: meuWidget
  size: 200 100
  anchors.top: parent.top
  anchors.left: parent.left
  
  # Adicionar um label filho
  Label
    id: titulo
    text: "Meu Título"
    text-align: center
    color: #ffffff
    margin: 5
```

### Elementos Principais

#### Herança de Widgets
```otui
# Criar widget baseado em outro
MeuBotao < Button
  size: 80 30
  text: "Clique Aqui"
  color: #ff0000
```

#### Âncoras (Anchors)
```otui
# Posicionamento responsivo
Widget
  anchors.top: parent.top
  anchors.left: parent.left
  anchors.right: parent.right
  anchors.bottom: parent.bottom
```

#### Margens e Padding
```otui
Widget
  margin: 10          # Todas as margens
  margin: 10 20       # Vertical Horizontal
  margin: 10 20 15 5  # Top Right Bottom Left
  
  padding: 5          # Preenchimento interno
```

#### Cores e Estilos
```otui
Widget
  color: #ffffff       # Cor do texto
  background-color: #000000  # Cor de fundo
  border: 2 #ff0000   # Borda: largura cor
  opacity: 0.8         # Transparência
```

#### Texto e Fontes
```otui
Label
  text: "Texto simples"
  text-align: center   # left, center, right
  font: verdana-11px-antialised
  text-wrap: true      # Quebra de linha
```

### Exemplo Completo de Interface

```otui
# Janela principal do módulo
ImbuingWindow < MainWindow
  id: imbuingWindow
  size: 800 600
  text: "Sistema de Imbuing"
  draggable: true
  
  # Painel de informações do item
  ItemInformation < Panel
    height: 100
    border: 1 black
    padding: 5
    anchors.top: parent.top
    anchors.left: parent.left
    anchors.right: parent.right
    
    Label
      id: title
      text: "Informações do Item"
      text-align: center
      anchors.top: parent.top
      anchors.left: parent.left
      anchors.right: parent.right
    
    UIItem
      id: item
      size: 64 64
      anchors.left: parent.left
      anchors.verticalCenter: parent.verticalCenter
      margin-left: 10
    
    Panel
      id: slots
      size: 240 66
      anchors.right: parent.right
      anchors.verticalCenter: parent.verticalCenter
      
      Slot
        id: slot0
        text: "Slot 1"
        anchors.left: parent.left
      
      Slot
        id: slot1
        text: "Slot 2"
        anchors.left: prev.right
        margin-left: 10
      
      Slot
        id: slot2
        text: "Slot 3"
        anchors.left: prev.right
        margin-left: 10
  
  # Painel de imbuing vazio
  EmptyImbue < Panel
    height: 240
    border: 1 black
    padding: 5
    anchors.top: prev.bottom
    anchors.left: parent.left
    anchors.right: parent.right
    margin-top: 10
    
    Label
      id: title
      text: "Imbuing de Slot Vazio"
      text-align: center
      anchors.top: parent.top
      anchors.left: parent.left
      anchors.right: parent.right
    
    ComboBox
      id: groups
      anchors.top: prev.bottom
      anchors.left: parent.left
      anchors.right: parent.right
      margin-top: 10
    
    ComboBox
      id: imbuement
      anchors.top: prev.bottom
      anchors.left: parent.left
      anchors.right: parent.right
      margin-top: 5
```

---

## Arquivos .otmod - Configuração do Módulo

> [!info] Metadados do Módulo
> Arquivos `.otmod` definem metadados e configuração do módulo.

### Estrutura Básica

```otmod
Module
  name: meu_modulo
  description: Descrição do módulo
  author: Seu Nome
  website: https://github.com/seu-usuario
  sandboxed: true
  scripts: [ meu_modulo ]
  @onLoad: init()
  @onUnload: terminate()
```

### Propriedades Principais

#### Informações Básicas
```otmod
Module
  name: game_imbuing          # Nome único do módulo
  description: Sistema de imbuing  # Descrição
  author: Seu Nome
  website: https://github.com/seu-usuario
```

#### Configurações de Segurança
```otmod
Module
  sandboxed: true             # Executa em sandbox
  reloadable: true            # Pode ser recarregado
  autoload: true              # Carrega automaticamente
```

#### Scripts e Eventos
```otmod
Module
  scripts: [ imbuing ]        # Arquivo Lua principal
  @onLoad: init()             # Função chamada ao carregar
  @onUnload: terminate()      # Função chamada ao descarregar
```

#### Dependências
```otmod
Module
  # Carregar outros módulos primeiro
  load-later:
    - client_styles
    - client_locales
    - game_interface
```

### Exemplo Completo

```otmod
Module
  name: game_imbuing
  description: Sistema de imbuing para itens
  author: Vincent#1766 on discord
  website: http://otclient.ovh
  sandboxed: true
  scripts: [ imbuing ]
  @onLoad: init()
  @onUnload: terminate()
```

---

## Arquivos .lua - Lógica do Módulo

> [!info] Funcionalidade
> Arquivos `.lua` contêm toda a lógica e funcionalidade do módulo.

### Estrutura Básica

#### Nível Basic
```lua
-- Namespace do módulo
MeuModulo = {}

-- Variáveis globais do módulo
local minhaJanela
local dados = {}

-- Função de inicialização
function init()
    -- Conectar eventos do jogo
    connect(g_game, {
        onGameEnd = hide,
        onImbuementWindow = MeuModulo.onImbuementWindow
    })
    
    -- Carregar interface
    minhaJanela = g_ui.displayUI('meu_modulo')
    minhaJanela:hide()
end

-- Função de finalização
function terminate()
    -- Limpar recursos
    if minhaJanela then
        minhaJanela:destroy()
    end
end

-- Funções do módulo
function MeuModulo.show()
    if minhaJanela then
        minhaJanela:show()
        minhaJanela:focus()
    end
end

function MeuModulo.hide()
    if minhaJanela then
        minhaJanela:hide()
    end
end
```

#### Nível Intermediate
```lua
-- Namespace do módulo
MeuModulo = {}

-- Variáveis globais do módulo
local minhaJanela
local dados = {}

-- Função de inicialização
function init()
    -- Conectar eventos do jogo
    connect(g_game, {
        onGameEnd = hide,
        onImbuementWindow = MeuModulo.onImbuementWindow
    })
    
    -- Carregar interface
    minhaJanela = g_ui.displayUI('meu_modulo')
    minhaJanela:hide()
end

-- Função de finalização
function terminate()
    -- Limpar recursos
    if minhaJanela then
        minhaJanela:destroy()
    end
end

-- Funções do módulo
function MeuModulo.show()
    if minhaJanela then
        minhaJanela:show()
        minhaJanela:focus()
    end
end

function MeuModulo.hide()
    if minhaJanela then
        minhaJanela:hide()
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
-- Namespace do módulo
MeuModulo = {}

-- Variáveis globais do módulo
local minhaJanela
local dados = {}

-- Função de inicialização
function init()
    -- Conectar eventos do jogo
    connect(g_game, {
        onGameEnd = hide,
        onImbuementWindow = MeuModulo.onImbuementWindow
    })
    
    -- Carregar interface
    minhaJanela = g_ui.displayUI('meu_modulo')
    minhaJanela:hide()
end

-- Função de finalização
function terminate()
    -- Limpar recursos
    if minhaJanela then
        minhaJanela:destroy()
    end
end

-- Funções do módulo
function MeuModulo.show()
    if minhaJanela then
        minhaJanela:show()
        minhaJanela:focus()
    end
end

function MeuModulo.hide()
    if minhaJanela then
        minhaJanela:hide()
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

### Carregando Interface

```lua
-- Carregar interface do arquivo .otui
    --  Carregar interface do arquivo .otui (traduzido)
minhaJanela = g_ui.displayUI('nome_do_arquivo')

-- Carregar em um widget específico
minhaJanela = g_ui.displayUI('nome_do_arquivo', parentWidget)
```

### Acessando Elementos da Interface

```lua
-- Após carregar a interface
minhaJanela = g_ui.displayUI('meu_modulo')

-- Acessar elementos por ID
    --  Acessar elementos por ID (traduzido)
local botao = minhaJanela.botaoId
local label = minhaJanela.titulo
local combo = minhaJanela.comboBox

-- Configurar elementos
    --  Configurar elementos (traduzido)
botao.onClick = function()
    print("Botão clicado!")
end

combo.onOptionChange = function(widget)
    local opcao = widget:getCurrentOption()
    print("Opção selecionada:", opcao.text)
end
```

---

## Funções Principais

### g_ui.displayUI()
Carrega uma interface do arquivo `.otui`.

```lua
-- Carregar interface
    --  Carregar interface (traduzido)
local window = g_ui.displayUI('nome_do_arquivo')

-- Carregar em widget específico
local window = g_ui.displayUI('nome_do_arquivo', parentWidget)
```

### connect()
Conecta eventos do jogo.

#### Nível Basic
```lua
connect(g_game, {
    onGameEnd = hide,
    onImbuementWindow = MeuModulo.onImbuementWindow,
    onCloseImbuementWindow = MeuModulo.onCloseImbuementWindow
})
```

#### Nível Intermediate
```lua
connect(g_game, {
    onGameEnd = hide,
    onImbuementWindow = MeuModulo.onImbuementWindow,
    onCloseImbuementWindow = MeuModulo.onCloseImbuementWindow
})
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
connect(g_game, {
    onGameEnd = hide,
    onImbuementWindow = MeuModulo.onImbuementWindow,
    onCloseImbuementWindow = MeuModulo.onCloseImbuementWindow
})
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

### g_ui.createWidget()
Cria widgets dinamicamente.

#### Nível Basic
```lua
-- Criar widget básico
local widget = g_ui.createWidget('UIWidget', parent)

-- Criar widget específico
local button = g_ui.createWidget('Button', parent)
local label = g_ui.createWidget('Label', parent)
```

#### Nível Intermediate
```lua
-- Criar widget básico
local widget = g_ui.createWidget('UIWidget', parent)

-- Criar widget específico
local button = g_ui.createWidget('Button', parent)
local label = g_ui.createWidget('Label', parent)
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
-- Criar widget básico
local widget = g_ui.createWidget('UIWidget', parent)

-- Criar widget específico
local button = g_ui.createWidget('Button', parent)
local label = g_ui.createWidget('Label', parent)
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

### Eventos de Widget
```lua
-- Eventos de mouse
    --  Eventos de mouse (traduzido)
widget.onClick = function()
    print("Clicado!")
end

widget.onDoubleClick = function()
    print("Duplo clique!")
end

-- Eventos de teclado
    --  Eventos de teclado (traduzido)
widget.onKeyDown = function(keyCode, keyboardModifiers)
    if keyCode == KeyEscape then
    -- Verificação condicional
        hide()
    end
end
```

---

## Estrutura de Pastas

### Estrutura Recomendada

```
modules/meu_modulo/
├── meu_modulo.otmod          # Configuração
├── meu_modulo.lua            # Lógica principal
├── meu_modulo.otui           # Interface principal
├── styles/                   # Estilos adicionais
│   ├── style1.otui
│   └── style2.otui
├── images/                   # Recursos visuais
│   ├── icon.png
│   └── background.png
└── README.md                 # Documentação
```

### Organização de Módulos

```
modules/
├── client/                   # Módulos do cliente
│   ├── client.otmod
│   ├── client.lua
│   └── client.otui
├── game_meu_modulo/          # Módulos do jogo
│   ├── meu_modulo.otmod
│   ├── meu_modulo.lua
│   └── meu_modulo.otui
└── corelib/                  # Bibliotecas core
    ├── corelib.otmod
    └── ui/
        └── uiwidget.lua
```

---

## Exemplos Práticos

### Exemplo 1: Módulo Simples

> [!example] Módulo Básico
> Este exemplo mostra a estrutura mínima para um módulo funcional.

#### `modules/exemplo_simples/exemplo_simples.otmod`
```otmod
Module
  name: exemplo_simples
  description: Módulo de exemplo
  author: Seu Nome
  sandboxed: true
  scripts: [ exemplo_simples ]
  @onLoad: init()
  @onUnload: terminate()
```

#### `modules/exemplo_simples/exemplo_simples.otui`
```otui
ExemploWindow < MainWindow
  id: exemploWindow
  size: 300 200
  text: "Exemplo Simples"
  draggable: true
  
  Label
    id: titulo
    text: "Olá Mundo!"
    text-align: center
    anchors.top: parent.top
    anchors.left: parent.left
    anchors.right: parent.right
    margin: 20
  
  Button
    id: botao
    text: "Clique Aqui"
    anchors.bottom: parent.bottom
    anchors.left: parent.left
    anchors.right: parent.right
    margin: 20
```

#### `modules/exemplo_simples/exemplo_simples.lua`
```lua
ExemploSimples = {}

local exemploWindow

function init()
    -- Função: init
    exemploWindow = g_ui.displayUI('exemplo_simples')
    exemploWindow:hide()
    
    -- Configurar evento do botão
    exemploWindow.botao.onClick = function()
        exemploWindow.titulo:setText("Botão clicado!")
    end
end

function terminate()
    -- Função: terminate
    if exemploWindow then
    -- Verificação condicional
        exemploWindow:destroy()
    end
end

function ExemploSimples.show()
    -- Função: ExemploSimples
    if exemploWindow then
    -- Verificação condicional
        exemploWindow:show()
        exemploWindow:focus()
    end
end

function ExemploSimples.hide()
    -- Função: ExemploSimples
    if exemploWindow then
    -- Verificação condicional
        exemploWindow:hide()
    end
end
```

### Exemplo 2: Módulo com Interface Complexa

> [!example] Módulo Avançado
> Este exemplo mostra uma interface mais complexa com múltiplos painéis.

#### `modules/game_meu_sistema/meu_sistema.otui`
```otui
MeuSistemaWindow < MainWindow
  id: meuSistemaWindow
  size: 600 400
  text: "Meu Sistema"
  draggable: true
  
  # Painel superior
  Panel
    id: topPanel
    height: 50
    anchors.top: parent.top
    anchors.left: parent.left
    anchors.right: parent.right
    background-color: #2a2a2a
    
    Label
      id: title
      text: "Meu Sistema"
      text-align: center
      anchors.centerIn: parent
      color: #ffffff
  
  # Painel principal
  Panel
    id: mainPanel
    anchors.top: prev.bottom
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.bottom: parent.bottom
    margin: 10
    
    # Lista de itens
    UIWidget
      id: itemList
      anchors.top: parent.top
      anchors.left: parent.left
      anchors.right: parent.right
      height: 200
      border: 1 #666666
    
    # Botões de ação
    Panel
      id: buttonPanel
      height: 40
      anchors.bottom: parent.bottom
      anchors.left: parent.left
      anchors.right: parent.right
      
      Button
        id: addButton
        text: "Adicionar"
        anchors.left: parent.left
        size: 80 30
      
      Button
        id: removeButton
        text: "Remover"
        anchors.left: prev.right
        anchors.top: prev.top
        size: 80 30
        margin-left: 10
      
      Button
        id: closeButton
        text: "Fechar"
        anchors.right: parent.right
        anchors.top: parent.top
        size: 80 30
```

#### `modules/game_meu_sistema/meu_sistema.lua`
#### Inicialização e Configuração
```lua
MeuSistema = {}

local meuSistemaWindow
local itens = {}

function init()
    -- Conectar eventos
    connect(g_game, {
        onGameEnd = hide
    })
    
    -- Carregar interface
    meuSistemaWindow = g_ui.displayUI('meu_sistema')
    meuSistemaWindow:hide()
    
    -- Configurar eventos dos botões
    meuSistemaWindow.addButton.onClick = function()
        adicionarItem()
    end
    
    meuSistemaWindow.removeButton.onClick = function()
        removerItem()
    end
```

#### Funcionalidade 1
```lua
    
    meuSistemaWindow.closeButton.onClick = function()
        hide()
    end
end

function terminate()
    if meuSistemaWindow then
        meuSistemaWindow:destroy()
    end
end

function adicionarItem()
    local item = g_ui.createWidget('UIWidget', meuSistemaWindow.itemList)
    item:setText("Item " .. #itens + 1)
    table.insert(itens, item)
end

function removerItem()
    if #itens > 0 then
        local item = table.remove(itens)
        item:destroy()
    end
```

#### Finalização
```lua
end

function MeuSistema.show()
    if meuSistemaWindow then
        meuSistemaWindow:show()
        meuSistemaWindow:focus()
    end
end

function MeuSistema.hide()
    if meuSistemaWindow then
        meuSistemaWindow:hide()
    end
end
```

---

## Melhores Práticas

> [!tip] Dicas de Desenvolvimento
> Siga estas práticas para criar módulos eficientes e mantíveis.

### Organização de Código
#### Nível Basic
```lua
-- Sempre use namespace para seu módulo
MeuModulo = {}

-- Variáveis locais para o módulo
local minhaJanela
local dados = {}

-- Funções públicas do módulo
function MeuModulo.show()
    -- implementação
end

-- Funções privadas (locais)
local function processarDados()
    -- implementação
end
```

#### Nível Intermediate
```lua
-- Sempre use namespace para seu módulo
MeuModulo = {}

-- Variáveis locais para o módulo
local minhaJanela
local dados = {}

-- Funções públicas do módulo
function MeuModulo.show()
    -- implementação
end

-- Funções privadas (locais)
local function processarDados()
    -- implementação
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
-- Sempre use namespace para seu módulo
MeuModulo = {}

-- Variáveis locais para o módulo
local minhaJanela
local dados = {}

-- Funções públicas do módulo
function MeuModulo.show()
    -- implementação
end

-- Funções privadas (locais)
local function processarDados()
    -- implementação
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

### Gerenciamento de Recursos
```lua
function init()
    -- Função: init
    -- Carregar recursos
    --  Carregar recursos (traduzido)
    minhaJanela = g_ui.displayUI('meu_modulo')
end

function terminate()
    -- Função: terminate
    -- Limpar recursos
    --  Limpar recursos (traduzido)
    if minhaJanela then
    -- Verificação condicional
        minhaJanela:destroy()
        minhaJanela = nil
    end
end
```

### Tratamento de Erros
```lua
function MeuModulo.show()
    -- Função: MeuModulo
    if not minhaJanela then
    -- Verificação condicional
        print("Erro: Janela não inicializada")
        return
    end
    
    minhaJanela:show()
    minhaJanela:focus()
end
```

### Documentação
```lua
--[[
    -- [[ (traduzido)
    Módulo: Meu Modulo
    Descrição: Sistema de exemplo
    Autor: Seu Nome
    Versão: 1.0
]]

MeuModulo = {}

-- Função para mostrar a interface
-- @return void
    --  @return void (traduzido)
function MeuModulo.show()
    -- Função: MeuModulo
    -- implementação
end
```

### Nomenclatura
- **Arquivos**: `meu_modulo.lua`, `meu_modulo.otui`, `meu_modulo.otmod`
- **Namespaces**: `MeuModulo` (PascalCase)
- **Variáveis**: `minhaJanela` (camelCase)
- **IDs**: `meuWidget` (camelCase)

---

## 🔗 Relacionamentos

### Dependências
- Baseado em [[UI_System_Guide]]
- Utilizado por todos os módulos de interface

### Próximos Passos
- Leia [[Lua_Programming_Guide]] para funcionalidades avançadas
- Explore [[Network_Protocol_Guide]] para comunicação com servidor
- Consulte [[API_Reference_Guide]] para referência completa
> - [[Getting_Started_Guide]] - Primeiros passos
> - [[UI_System_Guide]] - Interface do usuário
> - [[Lua_API_Reference]] - Referência da API
> - [[Configuration_Guide]] - Configuração

---

> [!success] **Navegação**
> **📚 Documentos Relacionados:**
> - [[Getting_Started_Guide]] - Comece aqui
> - [[Module_System_Guide]] - Sistema de módulos
> - [[UI_System_Guide]] - Interface do usuário
> - [[Lua_API_Reference]] - API completa
> 
> **🔗 Navegação Rápida:**
> - [[Wiki_Index]] - Voltar ao índice
> - [[Cheat_Sheet]] - Referência rápida
> - [[Debug_System_Guide]] - Debugging

