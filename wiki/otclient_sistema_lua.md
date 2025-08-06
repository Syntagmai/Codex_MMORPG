---
tags: [otclient, lua, scripting, sistema, wikipedia, habdel]
type: wikipedia
status: active
priority: alta
created: 2025-08-05
updated: 2025-08-05
aliases: [Sistema Lua OTClient, Lua Scripting OTClient, OTClient Lua System]
---

# 🐍 **Sistema de Lua - OTClient**

> [!info] **Baseado na pesquisa Habdel**
> Esta página é baseada na pesquisa detalhada da **OTCLIENT-006** realizada pelo sistema Habdel.

---

## 🎯 **Visão Geral**

O **Sistema de Lua** do OTClient é o coração da programabilidade do cliente, permitindo que desenvolvedores criem módulos, interfaces e funcionalidades personalizadas usando a linguagem Lua. Este sistema integra-se profundamente com o framework C++ do OTClient, fornecendo uma interface poderosa e flexível para desenvolvimento.

### **Características Principais**
- **Integração C++/Lua**: Ponte bidirecional entre C++ e Lua
- **Sistema de Módulos**: Carregamento dinâmico de módulos Lua
- **APIs Completas**: Acesso a todos os sistemas do cliente
- **Performance Otimizada**: Bindings diretos para máxima eficiência
- **Debugging Avançado**: Ferramentas de desenvolvimento integradas

---

## 🏗️ **Arquitetura do Sistema**

### **Estrutura Hierárquica**
```
OTClient Framework (C++)
├── LuaEngine (Interface C++/Lua)
├── LuaInterface (Bindings e APIs)
├── LuaObject (Objetos Lua)
├── LuaFunctions (Funções Globais)
└── Modules (Módulos Lua)
    ├── gamelib/ (Biblioteca de Jogo)
    ├── corelib/ (Biblioteca Core)
    └── game_*/ (Módulos Específicos)
```

### **Componentes Principais**

#### **1. LuaEngine (`src/framework/luaengine/`)**
```cpp
// Interface principal entre C++ e Lua
class LuaInterface {
    // Bindings de funções C++ para Lua
    // Gerenciamento de objetos Lua
    // Sistema de eventos e callbacks
};
```

#### **2. LuaFunctions (`src/framework/luafunctions.cpp`)**
```cpp
// Funções globais disponíveis em Lua
void Application::registerLuaFunctions() {
    // Conversões de tipos
    g_lua.bindGlobalFunction("torect", [](const std::string_view v) { 
        return stdext::from_string<Rect>(v); 
    });
    
    // Funções utilitárias
    g_lua.bindGlobalFunction("ucwords", [](std::string s) { 
        return stdext::ucwords(s); 
    });
}
```

#### **3. Sistema de Módulos**
```lua
-- Estrutura de um módulo OTClient
-- modules/gamelib/gamelib.otmod
{
    name = "gamelib",
    description = "Game library for OTClient",
    author = "OTClient Team",
    autoload = true,
    autoloadPriority = 1000,
    script = "gamelib.lua"
}
```

---

## 🔧 **APIs e Interfaces**

### **Funções Globais Disponíveis**

#### **Conversões de Tipos**
```lua
-- Conversão de strings para tipos C++
local rect = torect("10,20,100,200")
local point = topoint("50,50")
local color = tocolor("255,0,0,255")
local size = tosize("200,150")

-- Conversão de tipos C++ para strings
local rectStr = recttostring(rect)
local pointStr = pointtostring(point)
local colorStr = colortostring(color)
local sizeStr = sizetostring(size)
```

#### **Funções de Rede**
```lua
-- Conversão de IPs
local ipStr = iptostring(ip)
local ip = stringtoip("127.0.0.1")

-- Listagem de endereços de sub-rede
local addresses = listSubnetAddresses(ip, subnetMask)
```

#### **Funções de Texto**
```lua
-- Capitalização de palavras
local capitalized = ucwords("hello world") -- "Hello World"

-- Expressões regulares
local matches = regexMatch(text, pattern)
```

### **APIs de Sistema**

#### **Gerenciamento de Módulos**
```lua
-- Carregar módulo
g_modules.loadModule("gamelib")

-- Verificar se módulo está carregado
if g_modules.isModuleLoaded("gamelib") then
    print("Módulo gamelib carregado")
end

-- Descarregar módulo
g_modules.unloadModule("gamelib")
```

#### **Sistema de Eventos**
```lua
-- Conectar a evento
connect(g_game, { onGameStart = function()
    print("Jogo iniciado!")
end })

-- Desconectar de evento
disconnect(g_game, { onGameStart = nil })

-- Emitir evento customizado
signalcall('onCustomEvent', data)
```

---

## 📚 **Exemplos Práticos**

### **Exemplo 1: Criando um Módulo Básico**
```lua
-- modules/meu_modulo/meu_modulo.otmod
{
    name = "meu_modulo",
    description = "Meu módulo personalizado",
    author = "Seu Nome",
    autoload = true,
    autoloadPriority = 1000,
    script = "meu_modulo.lua"
}

-- modules/meu_modulo/meu_modulo.lua
local meuModulo = {}

function meuModulo.init()
    print("Meu módulo inicializado!")
    
    -- Conectar a eventos do jogo
    connect(g_game, { onGameStart = meuModulo.onGameStart })
end

function meuModulo.onGameStart()
    print("Jogo iniciado - meu módulo ativo!")
end

function meuModulo.terminate()
    disconnect(g_game, { onGameStart = meuModulo.onGameStart })
    print("Meu módulo finalizado!")
end

return meuModulo
```

### **Exemplo 2: Interface Personalizada**
```lua
-- Criar janela personalizada
local janela = g_ui.createWidget('UIWindow')
janela:setText('Minha Janela')
janela:setSize({ width = 300, height = 200 })

-- Adicionar botão
local botao = g_ui.createWidget('UIButton', janela)
botao:setText('Clique Aqui')
botao:setPosition({ x = 10, y = 10 })

-- Conectar evento de clique
connect(botao, { onClick = function()
    print("Botão clicado!")
end })

-- Mostrar janela
janela:show()
```

### **Exemplo 3: Sistema de Animações**
```lua
-- Criar animação personalizada
local animacao = {}
animacao.duration = 1000 -- 1 segundo
animacao.startValue = 0
animacao.endValue = 100

function animacao.start(widget)
    local startTime = g_clock.millis()
    
    local function update()
        local elapsed = g_clock.millis() - startTime
        local progress = math.min(elapsed / animacao.duration, 1.0)
        
        local currentValue = animacao.startValue + 
            (animacao.endValue - animacao.startValue) * progress
        
        widget:setOpacity(currentValue / 100)
        
        if progress < 1.0 then
            scheduleEvent(update, 16) -- ~60 FPS
        end
    end
    
    update()
end
```

---

## 🔗 **Dependências e Integração**

### **Dependências Internas**
- **LuaEngine**: Interface C++/Lua
- **LuaInterface**: Bindings de funções
- **LuaObject**: Gerenciamento de objetos
- **ModuleManager**: Sistema de módulos
- **EventDispatcher**: Sistema de eventos

### **Integração com Outros Sistemas**
- **Sistema de UI**: Criação de interfaces
- **Sistema de Rede**: Comunicação com servidor
- **Sistema de Gráficos**: Renderização
- **Sistema de Som**: Reprodução de áudio
- **Sistema de Eventos**: Gerenciamento de eventos

### **APIs Relacionadas**
```lua
-- Sistema de UI
g_ui.createWidget()
g_ui.getRootWidget()
g_ui.getWidgetById()

-- Sistema de Rede
g_game.connect()
g_game.disconnect()
g_game.send()

-- Sistema de Gráficos
g_graphics.createTexture()
g_graphics.drawText()
g_graphics.drawRect()
```

---

## 🚀 **Melhores Práticas**

### **1. Estrutura de Módulos**
```lua
-- Sempre use estrutura modular
local meuModulo = {}

function meuModulo.init()
    -- Inicialização
end

function meuModulo.terminate()
    -- Limpeza
end

return meuModulo
```

### **2. Gerenciamento de Eventos**
```lua
-- Sempre desconecte eventos
local connections = {}

function meuModulo.init()
    connections.gameStart = connect(g_game, { 
        onGameStart = meuModulo.onGameStart 
    })
end

function meuModulo.terminate()
    for _, connection in pairs(connections) do
        disconnect(connection)
    end
end
```

### **3. Tratamento de Erros**
```lua
-- Use pcall para operações críticas
local success, result = pcall(function()
    -- Código que pode falhar
    return operacaoCritica()
end)

if not success then
    print("Erro:", result)
end
```

### **4. Performance**
```lua
-- Cache de objetos frequentemente usados
local cachedWidget = g_ui.getWidgetById('meuWidget')

-- Use scheduleEvent para operações não críticas
scheduleEvent(function()
    -- Operação não crítica
end, 100)
```

---

## 🔍 **Debugging e Desenvolvimento**

### **Ferramentas de Debug**
```lua
-- Console de debug
g_logger.debug("Mensagem de debug")
g_logger.info("Mensagem de informação")
g_logger.warning("Aviso")
g_logger.error("Erro")

-- Inspeção de objetos
print(dump(objeto))

-- Profiling
local startTime = g_clock.millis()
-- ... código ...
local endTime = g_clock.millis()
print("Tempo de execução:", endTime - startTime, "ms")
```

### **Desenvolvimento de Módulos**
```lua
-- Recarregar módulo durante desenvolvimento
g_modules.reloadModule("meu_modulo")

-- Verificar dependências
for name, module in pairs(g_modules.getModules()) do
    print("Módulo:", name, "Carregado:", module:isLoaded())
end
```

---

## 📖 **Referência Completa**

### **Funções Globais**
- `torect(string)` → Rect
- `topoint(string)` → Point
- `tocolor(string)` → Color
- `tosize(string)` → Size
- `recttostring(rect)` → string
- `pointtostring(point)` → string
- `colortostring(color)` → string
- `sizetostring(size)` → string
- `iptostring(ip)` → string
- `stringtoip(string)` → number
- `ucwords(string)` → string
- `regexMatch(string, pattern)` → table

### **APIs de Sistema**
- `g_modules.loadModule(name)`
- `g_modules.unloadModule(name)`
- `g_modules.isModuleLoaded(name)`
- `g_modules.reloadModule(name)`
- `g_ui.createWidget(type, parent)`
- `g_ui.getWidgetById(id)`
- `g_game.connect()`
- `g_game.disconnect()`
- `connect(object, events)`
- `disconnect(object, events)`
- `signalcall(event, ...)`
- `scheduleEvent(function, delay)`

---

## 🎯 **Conclusão**

O **Sistema de Lua** do OTClient fornece uma base sólida e flexível para desenvolvimento de módulos e funcionalidades personalizadas. Com sua integração profunda com o framework C++ e APIs completas, permite que desenvolvedores criem experiências ricas e interativas.

### **Próximos Passos**
- Explore os módulos existentes em `modules/`
- Experimente com as APIs de UI e eventos
- Desenvolva módulos personalizados
- Integre com outros sistemas do OTClient

---

## 🔗 **Links Relacionados**

- [[otclient_arquitetura_core|Arquitetura Core do OTClient]]
- [[otclient_sistema_modulos|Sistema de Módulos]]
- [[otclient_sistema_ui|Sistema de UI]]
- [[otclient_sistema_rede|Sistema de Rede]]
- [[otclient_sistema_graficos|Sistema de Gráficos]]

---

*Baseado na pesquisa Habdel: OTCLIENT-006 - Sistema de Lua* 