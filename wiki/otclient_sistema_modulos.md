---
tags: [otclient, sistema_modulos, fundamentos, habdel_research]
type: wiki_page
status: active
priority: high
created: 2025-08-05
updated: 2025-08-05
aliases: [modulos_otclient, module_system, otmod_files]
level: intermediate
category: fundamentos
dependencies: [otclient_arquitetura_core]
related: [otclient_arquitetura_core, otclient_sistema_rede, otclient_sistema_ui, otclient_sistema_graficos]
---

# 📦 **Sistema de Módulos do OTClient**

> [!info] **Baseado no Código-Fonte Real**
> Esta página é baseada na análise direta do código-fonte do OTClient, especificamente os arquivos em `otclient/modules/` e `otclient/src/framework/luaengine/`.

## 📋 **Visão Geral**

O **Sistema de Módulos** do OTClient permite extensibilidade e customização através de módulos Lua independentes. Cada módulo pode adicionar funcionalidades específicas ao cliente, desde interfaces customizadas até integrações com sistemas externos.

### **🎯 Objetivos do Sistema**
- **Modularidade**: Módulos independentes e reutilizáveis
- **Extensibilidade**: Fácil adição de novas funcionalidades
- **Isolamento**: Módulos não interferem entre si
- **Performance**: Carregamento sob demanda

---

## 📁 **Estrutura de Arquivos**

```
otclient/modules/
├── corelib/                    # Biblioteca core Lua
│   ├── init.lua               # Inicialização da biblioteca
│   └── ...                    # Funções utilitárias
├── gamelib/                    # Biblioteca de jogo Lua
│   ├── init.lua               # Inicialização da biblioteca
│   └── ...                    # APIs de jogo
├── client/                     # Módulos do cliente
│   ├── client/                # Módulo principal do cliente
│   ├── client_background/     # Módulo de fundo
│   ├── client_bottommenu/     # Módulo de menu inferior
│   └── ...                    # Outros módulos cliente
├── game_*/                     # Módulos de funcionalidades do jogo
│   ├── game_interface/        # Interface principal do jogo
│   ├── game_inventory/        # Sistema de inventário
│   ├── game_containers/       # Sistema de containers
│   └── ...                    # Outros módulos de jogo
└── [modulo_customizado]/      # Módulos personalizados
    ├── init.lua               # Script de inicialização
    ├── module.otmod           # Configuração do módulo
    └── ...                    # Arquivos do módulo
```

---

## 🔧 **Componentes Principais**

### **1. Estrutura de Módulo (.otmod)**
```xml
<!-- Exemplo de arquivo module.otmod -->
<module name="exemplo_modulo" version="1.0" author="Desenvolvedor">
    <description>Módulo de exemplo para demonstração</description>
    <dependencies>
        <dependency name="corelib" />
        <dependency name="gamelib" />
    </dependencies>
    <scripts>
        <script file="init.lua" />
        <script file="functions.lua" />
    </scripts>
    <files>
        <file path="data/interface.otui" />
        <file path="data/sprites.png" />
    </files>
</module>
```

### **2. Script de Inicialização (init.lua)**
```lua
-- Exemplo de init.lua para módulo
local module = {}

-- Variáveis do módulo
local window
local button

-- Função de inicialização (obrigatória)
function init()
    print("Módulo exemplo inicializado!")
    
    -- Carrega interface
    window = g_ui.createWidget('Window')
    window:setText('Módulo Exemplo')
    
    -- Cria botão
    button = g_ui.createWidget('Button', window)
    button:setText('Clique Aqui')
    button:onClick(function()
        print("Botão clicado!")
    end)
    
    window:show()
end

-- Função de finalização (obrigatória)
function terminate()
    print("Módulo exemplo finalizado!")
    
    if window then
        window:destroy()
    end
end

-- Funções públicas do módulo
function module.showWindow()
    if window then
        window:show()
    end
end

function module.hideWindow()
    if window then
        window:hide()
    end
end

return module
```

### **3. Sistema de Carregamento**
```cpp
// Exemplo de carregamento de módulos em C++
class ModuleManager {
public:
    void loadModule(const std::string& path);
    void unloadModule(const std::string& name);
    void reloadModule(const std::string& name);
    
private:
    std::map<std::string, Module*> m_modules;
    LuaEngine* m_lua;
};
```

---

## 🔌 **APIs e Interfaces**

### **APIs Lua para Módulos**
```lua
-- APIs principais disponíveis para módulos
g_ui = require('ui')                    -- Sistema de interface
g_graphics = require('graphics')        -- Sistema de gráficos
g_network = require('network')          -- Sistema de rede
g_sound = require('sound')              -- Sistema de áudio
g_game = require('game')                -- Sistema de jogo
g_map = require('map')                  -- Sistema de mapa
g_creatures = require('creatures')      -- Sistema de criaturas
g_items = require('items')              -- Sistema de itens

-- Exemplo de uso das APIs
function createCustomInterface()
    local window = g_ui.createWidget('Window')
    window:setText('Interface Customizada')
    window:setSize({300, 200})
    
    local button = g_ui.createWidget('Button', window)
    button:setText('Ação Customizada')
    button:onClick(function()
        g_sound.play('click.wav')
        g_game.send('custom_action')
    end)
    
    return window
end
```

### **Sistema de Eventos**
```lua
-- Exemplo de sistema de eventos
function onGameStart()
    print("Jogo iniciado!")
    -- Inicializa funcionalidades do módulo
end

function onGameEnd()
    print("Jogo finalizado!")
    -- Limpa recursos do módulo
end

-- Registra eventos
connect(g_game, { onGameStart = onGameStart, onGameEnd = onGameEnd })
```

---

## 🔄 **Fluxo de Dados**

### **1. Carregamento de Módulo**
```
ModuleManager::loadModule() →
├── Parse module.otmod
├── Check dependencies
├── Load scripts (init.lua, etc.)
├── Execute init() function
└── Register module
```

### **2. Execução de Módulo**
```
Game Loop →
├── Module::update() → Atualiza lógica do módulo
├── Module::draw() → Renderiza elementos do módulo
└── Module::handleEvent() → Processa eventos
```

### **3. Finalização de Módulo**
```
ModuleManager::unloadModule() →
├── Execute terminate() function
├── Cleanup resources
├── Unregister events
└── Remove module
```

---

## 💡 **Exemplos Práticos**

### **Nível Básico: Módulo de Informações**
```lua
-- modules/info_display/init.lua
local infoWindow

function init()
    -- Cria janela de informações
    infoWindow = g_ui.createWidget('Window')
    infoWindow:setText('Informações do Jogo')
    infoWindow:setSize({250, 150})
    infoWindow:setPosition({10, 10})
    
    -- Adiciona informações básicas
    local label = g_ui.createWidget('Label', infoWindow)
    label:setText('Versão: 1.0\nStatus: Online')
    
    infoWindow:show()
end

function terminate()
    if infoWindow then
        infoWindow:destroy()
    end
end
```

### **Nível Intermediário: Módulo de Estatísticas**
```lua
-- modules/statistics/init.lua
local statsWindow
local stats = {}

function init()
    -- Cria janela de estatísticas
    statsWindow = g_ui.createWidget('Window')
    statsWindow:setText('Estatísticas')
    statsWindow:setSize({300, 200})
    
    -- Cria tabela de estatísticas
    local table = g_ui.createWidget('Table', statsWindow)
    table:addColumn('Métrica', 150)
    table:addColumn('Valor', 100)
    
    -- Adiciona dados
    updateStats()
    
    -- Registra eventos para atualização
    connect(g_game, { onGameStart = updateStats })
    
    statsWindow:show()
end

function updateStats()
    stats = {
        { 'Tempo Online', os.date('%H:%M:%S') },
        { 'FPS', g_graphics.getFPS() },
        { 'Ping', g_network.getPing() }
    }
    
    -- Atualiza tabela
    local table = statsWindow:getChildById('statsTable')
    table:clearData()
    for _, row in ipairs(stats) do
        table:addRow(row)
    end
end

function terminate()
    if statsWindow then
        statsWindow:destroy()
    end
end
```

### **Nível Avançado: Módulo de Automação**
```lua
-- modules/automation/init.lua
local automationWindow
local automationEnabled = false
local tasks = {}

function init()
    -- Cria interface de automação
    automationWindow = g_ui.createWidget('Window')
    automationWindow:setText('Sistema de Automação')
    automationWindow:setSize({400, 300})
    
    -- Cria controles
    local enableButton = g_ui.createWidget('Button', automationWindow)
    enableButton:setText('Ativar Automação')
    enableButton:onClick(toggleAutomation)
    
    -- Cria lista de tarefas
    local taskList = g_ui.createWidget('List', automationWindow)
    taskList:setId('taskList')
    
    -- Registra eventos
    connect(g_game, { onGameStart = startAutomation })
    
    automationWindow:show()
end

function toggleAutomation()
    automationEnabled = not automationEnabled
    local button = automationWindow:getChildById('enableButton')
    button:setText(automationEnabled and 'Desativar' or 'Ativar')
    
    if automationEnabled then
        startAutomation()
    else
        stopAutomation()
    end
end

function startAutomation()
    if not automationEnabled then return end
    
    -- Executa tarefas automáticas
    scheduleEvent(function()
        if automationEnabled then
            executeTasks()
            startAutomation() -- Agenda próxima execução
        end
    end, 1000) -- Executa a cada 1 segundo
end

function executeTasks()
    for _, task in ipairs(tasks) do
        if task.condition() then
            task.action()
        end
    end
end

function stopAutomation()
    automationEnabled = false
end

function terminate()
    stopAutomation()
    if automationWindow then
        automationWindow:destroy()
    end
end
```

---

## 🎓 **Lições Educacionais**

### **Conceitos Fundamentais**
1. **Modularidade**: Separação de funcionalidades em unidades independentes
2. **Inicialização/Finalização**: Ciclo de vida adequado dos módulos
3. **Gerenciamento de Recursos**: Alocação e liberação de recursos
4. **Sistema de Eventos**: Comunicação assíncrona entre módulos

### **Padrões de Design**
- **Module Pattern**: Encapsulamento de funcionalidades
- **Observer Pattern**: Sistema de eventos
- **Factory Pattern**: Criação de widgets e elementos
- **Singleton Pattern**: APIs globais (g_ui, g_game, etc.)

### **Boas Práticas**
- Sempre implementar `init()` e `terminate()`
- Gerenciar recursos adequadamente
- Usar o sistema de eventos para comunicação
- Documentar APIs públicas do módulo
- Seguir convenções de nomenclatura

---

## 🔗 **Páginas Relacionadas**

- [[otclient_arquitetura_core|Arquitetura Core]] - Estrutura geral do OTClient
- [[otclient_sistema_rede|Sistema de Rede]] - Comunicação com servidor
- [[otclient_sistema_ui|Sistema de UI]] - Interface do usuário
- [[otclient_sistema_graficos|Sistema de Gráficos]] - Renderização
- [[wikipedia_canary_otclient|Wikipedia Canary + OTClient]] - Visão geral do projeto

---

## 📚 **Referências**

- **Código-fonte**: `otclient/modules/`
- **Motor Lua**: `otclient/src/framework/luaengine/`
- **Documentação**: `otclient/docs/`
- **Baseado na pesquisa Habdel**: [[../habdel/OTCLIENT-002|OTCLIENT-002: Sistema de Gráficos]] 