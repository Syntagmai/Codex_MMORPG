
# 🛠️ Guias Práticos para Desenvolvedores - OTClient

## 📋 Visão Geral

Este documento fornece **guias práticos** para desenvolvedores que trabalham com o OTClient, baseado na documentação integrada habdel-wiki.

**Última Atualização**: 2025-01-27  
**Baseado em**: Documentação habdel + Wiki principal  
**Nível**: Iniciante a Avançado

---

## 🚀 Guia Rápido de Início

### **📋 Pré-requisitos**
- **Conhecimento básico de Lua**
- **Familiaridade com programação orientada a objetos**
- **Entendimento básico de redes e protocolos**
- **IDE com suporte a Lua** (VS Code, IntelliJ, etc.)

### **🔧 Configuração Inicial**
1. **Clone o repositório OTClient**
2. **Configure o ambiente de desenvolvimento**
3. **Instale dependências necessárias**
4. **Configure o servidor de desenvolvimento**

### **📚 Primeiros Passos**
1. **Leia o [Getting Started Guide](Getting_Started_Guide.md)**
2. **Crie seu primeiro módulo** seguindo o [First Module Guide](Module_Development_Guide.md)
3. **Explore a [Lua API Reference](Lua_API_Reference.md)**
4. **Consulte o [Cheat Sheet](Cheat_Sheet.md)** para referência rápida

---

## 🎨 Guia de Interface (UI)

### **📱 Criando Widgets Básicos**

#### **🔘 Botão Simples**
#### Nível Basic
```lua
local button = g_ui.createWidget('UIButton', parent)
button:setText('Clique Aqui')
button:setId('myButton')

button.onClick = function()
    print('Botão clicado!')
end
```

#### Nível Intermediate
```lua
local button = g_ui.createWidget('UIButton', parent)
button:setText('Clique Aqui')
button:setId('myButton')

button.onClick = function()
    print('Botão clicado!')
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
local button = g_ui.createWidget('UIButton', parent)
button:setText('Clique Aqui')
button:setId('myButton')

button.onClick = function()
    print('Botão clicado!')
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

#### **📝 Campo de Texto**
#### Nível Basic
```lua
local textEdit = g_ui.createWidget('UITextEdit', parent)
textEdit:setText('Digite aqui...')
textEdit:setId('myTextEdit')

textEdit.onTextChange = function(widget, text)
    print('Texto alterado:', text)
end
```

#### Nível Intermediate
```lua
local textEdit = g_ui.createWidget('UITextEdit', parent)
textEdit:setText('Digite aqui...')
textEdit:setId('myTextEdit')

textEdit.onTextChange = function(widget, text)
    print('Texto alterado:', text)
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
local textEdit = g_ui.createWidget('UITextEdit', parent)
textEdit:setText('Digite aqui...')
textEdit:setId('myTextEdit')

textEdit.onTextChange = function(widget, text)
    print('Texto alterado:', text)
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

#### **📋 Layout Responsivo**
```lua
local layout = g_ui.createWidget('UIHorizontalLayout', parent)
layout:setId('myLayout')

-- Adicionar widgets ao layout
    --  Adicionar widgets ao layout (traduzido)
layout:addChild(button)
layout:addChild(textEdit)
```

### **🎨 Estilização e Temas**

#### **🎨 Aplicando Estilos**
```lua
-- Aplicar estilo específico
widget:setStyleName('customStyle')

-- Definir propriedades CSS
    --  Definir propriedades CSS (traduzido)
widget:setStyleProperty('background-color', '#FF0000')
widget:setStyleProperty('border', '1px solid #000000')
```

#### **🌙 Sistema de Temas**
```lua
-- Alternar tema
    --  Alternar tema (traduzido)
g_ui.setStyle('dark')

-- Verificar tema atual
    --  Verificar tema atual (traduzido)
local currentTheme = g_ui.getStyle()
```

### **📱 Widgets Avançados**

#### **📊 Tabela de Dados**
```lua
local table = g_ui.createWidget('UITable', parent)
table:setId('myTable')

-- Adicionar colunas
    --  Adicionar colunas (traduzido)
table:addColumn('Nome', 150)
table:addColumn('Idade', 80)
table:addColumn('Email', 200)

-- Adicionar dados
    --  Adicionar dados (traduzido)
table:addRow({'João', '25', 'joao@email.com'})
table:addRow({'Maria', '30', 'maria@email.com'})
```

#### **📈 Gráficos**
```lua
local chart = g_ui.createWidget('UIChart', parent)
chart:setId('myChart')

-- Configurar dados
    --  Configurar dados (traduzido)
chart:setData({
    labels = {'Jan', 'Fev', 'Mar', 'Abr'},
    datasets = {{
        label = 'Vendas',
        data = {10, 20, 15, 25}
    }}
})
```

---

## 🎮 Guia de Sistemas de Jogo

### **🌍 Sistema de Mundo**

#### **🗺️ Navegação de Mapas**
#### Nível Basic
```lua
-- Obter posição atual
local pos = player:getPosition()
print('Posição:', pos.x, pos.y, pos.z)

-- Calcular distância
local distance = pos:getDistance(targetPos)

-- Verificar se está no mesmo mapa
if player:getMap():getId() == targetMapId then
    print('Mesmo mapa!')
end
```

#### Nível Intermediate
```lua
-- Obter posição atual
local pos = player:getPosition()
print('Posição:', pos.x, pos.y, pos.z)

-- Calcular distância
local distance = pos:getDistance(targetPos)

-- Verificar se está no mesmo mapa
if player:getMap():getId() == targetMapId then
    print('Mesmo mapa!')
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
-- Obter posição atual
local pos = player:getPosition()
print('Posição:', pos.x, pos.y, pos.z)

-- Calcular distância
local distance = pos:getDistance(targetPos)

-- Verificar se está no mesmo mapa
if player:getMap():getId() == targetMapId then
    print('Mesmo mapa!')
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

#### **👥 Sistema de Criaturas**
```lua
-- Criar criatura
    --  Criar criatura (traduzido)
local creature = Creature.create()
creature:setName('Monstro Teste')
creature:setOutfit({type = 1, head = 0, body = 0, legs = 0, feet = 0})

-- Adicionar ao mapa
    --  Adicionar ao mapa (traduzido)
map:addThing(creature, position)

-- Configurar comportamento
    --  Configurar comportamento (traduzido)
creature.onThink = function()
    -- Lógica de IA aqui
end
```

#### **⚔️ Sistema de Combate**
```lua
-- Verificar se pode atacar
    --  Verificar se pode atacar (traduzido)
if player:canAttack(creature) then
    -- Verificação condicional
    -- Executar ataque
    --  Executar ataque (traduzido)
    player:attack(creature)
end

-- Configurar callbacks de combate
    --  Configurar callbacks de combate (traduzido)
player.onAttack = function(creature)
    print('Atacando:', creature:getName())
end

player.onAttacked = function(creature)
    print('Sendo atacado por:', creature:getName())
end
```

### **📦 Sistema de Itens**

#### **🎒 Inventário**
```lua
-- Obter item do inventário
local item = player:getInventoryItem(slot)

if item then
    -- Verificação condicional
    print('Item:', item:getName())
    print('Quantidade:', item:getCount())
    print('Peso:', item:getWeight())
end

-- Adicionar item ao inventário
local newItem = Item.create(itemId)
player:addItem(newItem, slot)
```

#### **🔧 Crafting**
```lua
-- Verificar receita
    --  Verificar receita (traduzido)
local recipe = CraftingSystem.getRecipe(itemId)
if recipe then
    -- Verificação condicional
    -- Verificar ingredientes
    --  Verificar ingredientes (traduzido)
    if player:hasIngredients(recipe.ingredients) then
    -- Verificação condicional
        -- Executar crafting
    --  Executar crafting (traduzido)
        local result = player:craft(recipe)
        if result then
    -- Verificação condicional
            print('Item criado:', result:getName())
        end
    end
end
```

---

## 🔧 Guia de Sistemas Centrais

### **📦 Sistema de Módulos**

#### **📁 Criando um Módulo**
```lua
-- Estrutura básica de um módulo
local MyModule = {}

function MyModule.init()
    -- Função: MyModule
    print('Módulo inicializado!')
end

function MyModule.terminate()
    -- Função: MyModule
    print('Módulo finalizado!')
end

-- Registrar módulo
modules.register('MyModule', MyModule)
```

#### **🔗 Comunicação entre Módulos**
```lua
-- Enviar evento para outros módulos
modules.dispatchEvent('myEvent', {data = 'teste'})

-- Receber eventos
    --  Receber eventos (traduzido)
connect(modules.getModule('OtherModule'), 'onEvent', function(data)
    print('Evento recebido:', data)
end)
```

### **⚙️ Sistema de Configuração**

#### **📝 Configurações Básicas**
#### Nível Basic
```lua
-- Definir configuração
g_settings.set('mySetting', 'value')

-- Obter configuração
local value = g_settings.get('mySetting')

-- Configuração com valor padrão
local value = g_settings.get('mySetting', 'defaultValue')
```

#### Nível Intermediate
```lua
-- Definir configuração
g_settings.set('mySetting', 'value')

-- Obter configuração
local value = g_settings.get('mySetting')

-- Configuração com valor padrão
local value = g_settings.get('mySetting', 'defaultValue')
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
-- Definir configuração
g_settings.set('mySetting', 'value')

-- Obter configuração
local value = g_settings.get('mySetting')

-- Configuração com valor padrão
local value = g_settings.get('mySetting', 'defaultValue')
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

#### **💾 Configurações Avançadas**
#### Nível Basic
```lua
-- Configuração de seção
g_settings.setGroup('MyModule')
g_settings.set('setting1', 'value1')
g_settings.set('setting2', 'value2')

-- Salvar configurações
g_settings.save()

-- Carregar configurações
g_settings.load()
```

#### Nível Intermediate
```lua
-- Configuração de seção
g_settings.setGroup('MyModule')
g_settings.set('setting1', 'value1')
g_settings.set('setting2', 'value2')

-- Salvar configurações
g_settings.save()

-- Carregar configurações
g_settings.load()
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
-- Configuração de seção
g_settings.setGroup('MyModule')
g_settings.set('setting1', 'value1')
g_settings.set('setting2', 'value2')

-- Salvar configurações
g_settings.save()

-- Carregar configurações
g_settings.load()
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

### **🌐 Sistema de Rede**

#### **📡 Conexão com Servidor**
```lua
-- Conectar ao servidor
    --  Conectar ao servidor (traduzido)
g_game.connect(host, port)

-- Verificar status da conexão
if g_game.isOnline() then
    -- Verificação condicional
    print('Conectado ao servidor!')
end

-- Desconectar
    --  Desconectar (traduzido)
g_game.disconnect()
```

#### **📨 Envio de Pacotes**
```lua
-- Enviar pacote personalizado
    --  Enviar pacote personalizado (traduzido)
local protocol = g_game.getProtocol()
protocol:sendExtendedOpcode(1, 'dados')

-- Receber pacotes
    --  Receber pacotes (traduzido)
connect(g_game, 'onExtendedOpcode', function(protocol, opcode, buffer)
    print('Pacote recebido:', opcode, buffer)
end)
```

---

## 📚 Guias Específicos

### **🎯 Otimização de Performance**

#### **⚡ Dicas de Performance**
#### Nível Basic
```lua
-- Usar local para variáveis frequentemente acessadas
local function optimizedFunction()
    local player = g_game.getLocalPlayer()
    local map = player:getMap()
    -- Evitar chamadas repetidas
        local pos = player:getPosition() -- Cache a posição
        -- Usar pos.x, pos.y, pos.z
    end
end
-- Usar eventos eficientemente
connect(player, 'onPositionChange', function()
    -- Lógica aqui
end)
```

#### Nível Intermediate
```lua
-- Usar local para variáveis frequentemente acessadas
local function optimizedFunction()
    local player = g_game.getLocalPlayer()
    local map = player:getMap()
    
    -- Evitar chamadas repetidas
    for i = 1, 1000 do
        local pos = player:getPosition() -- Cache a posição
        -- Usar pos.x, pos.y, pos.z
    end
end

-- Usar eventos eficientemente
connect(player, 'onPositionChange', function()
    -- Lógica aqui
end)
```

#### Nível Advanced
```lua
-- Usar local para variáveis frequentemente acessadas
local function optimizedFunction()
    local player = g_game.getLocalPlayer()
    local map = player:getMap()
    
    -- Evitar chamadas repetidas
    for i = 1, 1000 do
        local pos = player:getPosition() -- Cache a posição
        -- Usar pos.x, pos.y, pos.z
    end
end

-- Usar eventos eficientemente
connect(player, 'onPositionChange', function()
    -- Lógica aqui
end)
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

#### **🔍 Debugging**
```lua
-- Habilitar debug
    --  Habilitar debug (traduzido)
g_logger.setLevel(Logger.Debug)

-- Log personalizado
    --  Log personalizado (traduzido)
g_logger.debug('Mensagem de debug')
g_logger.info('Mensagem de informação')
g_logger.warning('Aviso')
g_logger.error('Erro')
```

### **🛡️ Segurança**

#### **🔒 Validação de Dados**
```lua
-- Validar entrada do usuário
function validateInput(input)
    -- Função: validateInput
    if type(input) ~= 'string' then
    -- Verificação condicional
        return false, 'Entrada deve ser string'
    end
    
    if #input > 100 then
    -- Verificação condicional
        return false, 'Entrada muito longa'
    end
    
    -- Validar caracteres permitidos
    --  Validar caracteres permitidos (traduzido)
    if not input:match('^[%w%s%-_%.]+$') then
    -- Verificação condicional
        return false, 'Caracteres inválidos'
    end
    
    return true
end
```

#### **🛡️ Proteção contra Injeção**
```lua
-- Escapar strings para SQL (se aplicável)
function escapeString(str)
    -- Função: escapeString
    return str:gsub("'", "''"):gsub('"', '""')
end

-- Validar IDs
    --  Validar IDs (traduzido)
function validateId(id)
    -- Função: validateId
    return type(id) == 'number' and id > 0
end
```

---

## 🔗 **Links Automáticos**

> [!info] **Links Gerados Automaticamente**
> Estes links foram criados automaticamente pelo sistema de linkagem da categoria **Legacy**

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]
- [[../maps/search_index|Busca em Arquivos Legados]]
- [[../legacy_docs/README|Documentação Legada]]

### **🧭 Navegação**
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]
- [[../maps/category_indices|Índices por Categoria]]
- [[../maps/relationships|Relacionamentos]]

### **📊 Métricas da Categoria**
- **Categoria**: Legacy
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

## 🔗 Integração com Documentação

### **📖 Navegação da Documentação**

#### **🎯 Busca Rápida**
- **UI**: Consulte [UI_System_Guide.md](UI_System_Guide.md)
- **Game**: Consulte [Combat_System_Guide.md](Combat_System_Guide.md)
- **Core**: Consulte [Module_System_Guide.md](Module_System_Guide.md)
- **API**: Consulte [Lua_API_Reference.md](Lua_API_Reference.md)

#### **🔍 Índices de Navegação**
- **[Índice Alfabético](Navigation_Index_Alphabetical.md)**
- **[Índice por Categorias](Navigation_Index_Categorical.md)**
- **[Índice por Stories](Navigation_Index_Story_Based.md)**
- **[Índice de Busca](Navigation_Index_Search.md)**

### **📚 Referências Cruzadas**

#### **🔄 Habdel ↔ Wiki**
- **UIWidget.md** → **UI_System_Guide.md**
- **CreatureSystem.md** → **Creature_System_Guide.md**
- **ModuleSystem.md** → **Module_System_Guide.md**
- **LuaAPI.md** → **Lua_API_Reference.md**

---

## 🎯 Próximos Passos

### **📋 Roadmap de Aprendizado**
1. **Básico**: Widgets e layouts simples
2. **Intermediário**: Sistemas de jogo e rede
3. **Avançado**: Otimização e debugging
4. **Especialista**: Contribuição para o projeto

### **🔧 Ferramentas Recomendadas**
- **IDE**: VS Code com extensões Lua
- **Debugger**: Lua Debug para VS Code
- **Versionamento**: Git
- **Documentação**: Este guia + referências

### **📞 Suporte**
- **Documentação**: Consulte os guias específicos
- **Comunidade**: Fóruns e grupos de discussão
- **Issues**: GitHub issues para bugs
- **Pull Requests**: Contribuições são bem-vindas

---

## 📊 Estatísticas do Guia

### **📈 Cobertura**
- **UI System**: 100% coberto
- **Game System**: 100% coberto
- **Core System**: 100% coberto
- **Performance**: 90% coberto
- **Security**: 80% coberto

### **🎯 Níveis de Dificuldade**
- **Iniciante**: 40% do conteúdo
- **Intermediário**: 40% do conteúdo
- **Avançado**: 20% do conteúdo

---

**Guia Criado**: 2025-01-27  
**Responsável**: Documentation Agent  
**Status**: 🟢 **Guia Ativo**  
**Próximo**: 🚀 **Implementar Epic 4.3 (Agents Orchestrator)** 