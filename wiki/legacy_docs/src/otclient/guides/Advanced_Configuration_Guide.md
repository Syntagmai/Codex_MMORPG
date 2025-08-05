
# Sistema de Configuração Avançada

Sistema de configuração com suporte a múltiplos tipos de dados, validação e callbacks personalizados.

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [API C++](#api-c)
3. [API Lua](#api-lua)
4. [Tipos de Configuração](#tipos-de-configuração)
5. [Sistema de Opções](#sistema-de-opções)
6. [Exemplos Práticos](#exemplos-práticos)
7. [Melhores Práticas](#melhores-práticas)

## 🎯 Visão Geral

O sistema de configuração avançada do OTClient permite gerenciar configurações complexas com:

- **Tipos de dados múltiplos**: Boolean, number, string, table
- **Validação automática**: Verificação de tipos e ranges
- **Callbacks dinâmicos**: Ações personalizadas quando valores mudam
- **Interface integrada**: UI automática para configurações
- **Persistência**: Salvamento automático em g_settings

### 🔧 Fluxo de Configuração

```
Definição de Opção → Validação → Callback (se definido) → Atualização UI → Persistência
```

## 🔧 API C++

### ConfigManager
```cpp
class ConfigManager {
    -- Classe: ConfigManager
public:
    // Definir configuração
    static void defineOption(const std::string& key, 
                           const ConfigValue& defaultValue,
                           const std::string& description = "",
                           ConfigValidator validator = nullptr);
    
    // Obter/definir valores
    static ConfigValue getValue(const std::string& key);
    static bool setValue(const std::string& key, const ConfigValue& value);
    
    // Callbacks
    static void setCallback(const std::string& key, ConfigCallback callback);
    
    // Validação
    static bool isValid(const std::string& key, const ConfigValue& value);
    
    // Persistência
    static void save();
    static void load();
};

// Tipos de dados suportados
enum ConfigType {
    CONFIG_BOOLEAN,
    CONFIG_NUMBER,
    CONFIG_STRING,
    CONFIG_TABLE
};

// Estrutura de valor
struct ConfigValue {
    ConfigType type;
    union {
        bool boolValue;
        double numberValue;
        std::string* stringValue;
        ConfigTable* tableValue;
    };
};
```

### Validadores Predefinidos
#### Nível Basic
```cpp
// Validadores comuns
ConfigValidator rangeValidator(double min, double max);
ConfigValidator enumValidator(std::vector<std::string> options);
ConfigValidator regexValidator(const std::string& pattern);
ConfigValidator compositeValidator(std::vector<ConfigValidator> validators);
```

#### Nível Intermediate
```cpp
// Validadores comuns
ConfigValidator rangeValidator(double min, double max);
ConfigValidator enumValidator(std::vector<std::string> options);
ConfigValidator regexValidator(const std::string& pattern);
ConfigValidator compositeValidator(std::vector<ConfigValidator> validators);
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Validadores comuns
ConfigValidator rangeValidator(double min, double max);
ConfigValidator enumValidator(std::vector<std::string> options);
ConfigValidator regexValidator(const std::string& pattern);
ConfigValidator compositeValidator(std::vector<ConfigValidator> validators);
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

## 🐍 API Lua

### Funções Principais

#### `setOption(key, value, force)`
Define valor de uma opção com validação automática.

```lua
-- Definir valor
    --  Definir valor (traduzido)
setOption('masterVolume', 0.8)
setOption('enableVSync', true)
setOption('preferredLanguage', 'pt-BR')

-- Forçar sem validação (cuidado!)
setOption('debugMode', true, true)
```

#### `getOption(key)`
Obtém valor atual de uma opção.

#### Nível Basic
```lua
local volume = getOption('masterVolume')
local isFullscreen = getOption('fullscreen')
```

#### Nível Intermediate
```lua
local volume = getOption('masterVolume')
local isFullscreen = getOption('fullscreen')
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
local volume = getOption('masterVolume')
local isFullscreen = getOption('fullscreen')
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

#### `defineOption(key, defaultValue, options)`
Define nova opção com configurações avançadas.

#### Nível Basic
```lua
-- Opção simples
defineOption('autoSave', true)

-- Opção com validação
defineOption('maxFPS', 60, {
    min = 30,
    max = 240,
    description = "Maximum frames per second",
    category = "Graphics"
})

-- Opção com callback
defineOption('theme', 'default', {
    options = {'default', 'dark', 'light'},
    callback = function(value)
        g_ui.setTheme(value)
    end
})
```

#### Nível Intermediate
```lua
-- Opção simples
defineOption('autoSave', true)

-- Opção com validação
defineOption('maxFPS', 60, {
    min = 30,
    max = 240,
    description = "Maximum frames per second",
    category = "Graphics"
})

-- Opção com callback
defineOption('theme', 'default', {
    options = {'default', 'dark', 'light'},
    callback = function(value)
        g_ui.setTheme(value)
    end
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
-- Opção simples
defineOption('autoSave', true)

-- Opção com validação
defineOption('maxFPS', 60, {
    min = 30,
    max = 240,
    description = "Maximum frames per second",
    category = "Graphics"
})

-- Opção com callback
defineOption('theme', 'default', {
    options = {'default', 'dark', 'light'},
    callback = function(value)
        g_ui.setTheme(value)
    end
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

#### `registerOptionCallback(key, callback)`
Registra callback para mudanças de opção.

#### Nível Basic
```lua
registerOptionCallback('language', function(newValue, oldValue)
    tr.setLanguage(newValue)
    g_ui.reloadAll()
end)
```

#### Nível Intermediate
```lua
registerOptionCallback('language', function(newValue, oldValue)
    tr.setLanguage(newValue)
    g_ui.reloadAll()
end)
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
registerOptionCallback('language', function(newValue, oldValue)
    tr.setLanguage(newValue)
    g_ui.reloadAll()
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

### Sistema de Categorias

#### `createOptionCategory(name, options)`
Cria categoria de opções para organização.

#### Nível Basic
```lua
createOptionCategory('Graphics', {
    icon = '/images/icons/graphics',
    priority = 100,
    description = 'Graphics and rendering options'
})
```

#### Nível Intermediate
```lua
createOptionCategory('Graphics', {
    icon = '/images/icons/graphics',
    priority = 100,
    description = 'Graphics and rendering options'
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
createOptionCategory('Graphics', {
    icon = '/images/icons/graphics',
    priority = 100,
    description = 'Graphics and rendering options'
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

#### `addOptionToCategory(category, optionKey)`
Adiciona opção a uma categoria.

#### Nível Basic
```lua
addOptionToCategory('Graphics', 'fullscreen')
addOptionToCategory('Graphics', 'vsync')
addOptionToCategory('Graphics', 'maxFPS')
```

#### Nível Intermediate
```lua
addOptionToCategory('Graphics', 'fullscreen')
addOptionToCategory('Graphics', 'vsync')
addOptionToCategory('Graphics', 'maxFPS')
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
addOptionToCategory('Graphics', 'fullscreen')
addOptionToCategory('Graphics', 'vsync')
addOptionToCategory('Graphics', 'maxFPS')
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

## 🎛️ Tipos de Configuração

### 1. Boolean (Checkbox)
#### Nível Basic
```lua
defineOption('enableShadows', true, {
    description = "Enable dynamic shadows",
    category = "Graphics",
    widget = "checkbox"
})
```

#### Nível Intermediate
```lua
defineOption('enableShadows', true, {
    description = "Enable dynamic shadows",
    category = "Graphics",
    widget = "checkbox"
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
defineOption('enableShadows', true, {
    description = "Enable dynamic shadows",
    category = "Graphics",
    widget = "checkbox"
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

### 2. Number (Slider/SpinBox)
#### Nível Basic
```lua
defineOption('masterVolume', 1.0, {
    min = 0.0,
    max = 1.0,
    step = 0.1,
    widget = "slider",
    description = "Master audio volume"
})

defineOption('maxConnections', 100, {
    min = 1,
    max = 1000,
    widget = "spinbox",
    description = "Maximum concurrent connections"
})
```

#### Nível Intermediate
```lua
defineOption('masterVolume', 1.0, {
    min = 0.0,
    max = 1.0,
    step = 0.1,
    widget = "slider",
    description = "Master audio volume"
})

defineOption('maxConnections', 100, {
    min = 1,
    max = 1000,
    widget = "spinbox",
    description = "Maximum concurrent connections"
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
defineOption('masterVolume', 1.0, {
    min = 0.0,
    max = 1.0,
    step = 0.1,
    widget = "slider",
    description = "Master audio volume"
})

defineOption('maxConnections', 100, {
    min = 1,
    max = 1000,
    widget = "spinbox",
    description = "Maximum concurrent connections"
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

### 3. String (LineEdit/ComboBox)
```lua
-- Texto livre
    --  Texto livre (traduzido)
defineOption('playerName', '', {
    maxLength = 32,
    pattern = '^[a-zA-Z ]+$',
    widget = "lineedit"
})

-- Lista de opções
defineOption('resolution', '1920x1080', {
    options = {'1024x768', '1280x720', '1920x1080', '2560x1440'},
    widget = "combobox"
})
```

### 4. Table (Estruturas Complexas)
#### Nível Basic
```lua
defineOption('hotkeys', {}, {
    structure = {
        key = 'string',
        action = 'string',
        modifier = 'string'
    },
    widget = "custom"
})
```

#### Nível Intermediate
```lua
defineOption('hotkeys', {}, {
    structure = {
        key = 'string',
        action = 'string',
        modifier = 'string'
    },
    widget = "custom"
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
defineOption('hotkeys', {}, {
    structure = {
        key = 'string',
        action = 'string',
        modifier = 'string'
    },
    widget = "custom"
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

## ⚙️ Sistema de Opções

### Estrutura de Opção
#### Nível Basic
```lua
local optionStructure = {
    value = defaultValue,      -- Valor atual
    defaultValue = default,    -- Valor padrão
    type = 'boolean',         -- Tipo da opção
    description = 'desc',     -- Descrição
    category = 'General',     -- Categoria
    validator = function(),   -- Função de validação
    callback = function(),    -- Callback de mudança
    widget = 'checkbox',      -- Tipo de widget UI
    min = 0,                 -- Valor mínimo (números)
    max = 100,               -- Valor máximo (números)
    step = 1,                -- Incremento (números)
    options = {},            -- Lista de opções (string)
    pattern = '^[a-z]+$',    -- Padrão regex (string)
    maxLength = 255          -- Comprimento máximo (string)
}
```

#### Nível Intermediate
```lua
local optionStructure = {
    value = defaultValue,      -- Valor atual
    defaultValue = default,    -- Valor padrão
    type = 'boolean',         -- Tipo da opção
    description = 'desc',     -- Descrição
    category = 'General',     -- Categoria
    validator = function(),   -- Função de validação
    callback = function(),    -- Callback de mudança
    widget = 'checkbox',      -- Tipo de widget UI
    min = 0,                 -- Valor mínimo (números)
    max = 100,               -- Valor máximo (números)
    step = 1,                -- Incremento (números)
    options = {},            -- Lista de opções (string)
    pattern = '^[a-z]+$',    -- Padrão regex (string)
    maxLength = 255          -- Comprimento máximo (string)
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
local optionStructure = {
    value = defaultValue,      -- Valor atual
    defaultValue = default,    -- Valor padrão
    type = 'boolean',         -- Tipo da opção
    description = 'desc',     -- Descrição
    category = 'General',     -- Categoria
    validator = function(),   -- Função de validação
    callback = function(),    -- Callback de mudança
    widget = 'checkbox',      -- Tipo de widget UI
    min = 0,                 -- Valor mínimo (números)
    max = 100,               -- Valor máximo (números)
    step = 1,                -- Incremento (números)
    options = {},            -- Lista de opções (string)
    pattern = '^[a-z]+$',    -- Padrão regex (string)
    maxLength = 255          -- Comprimento máximo (string)
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

### Integração com Interface

#### Criação Automática de Widgets
```lua
-- O sistema cria automaticamente widgets baseado no tipo
    --  O sistema cria automaticamente widgets baseado no tipo (traduzido)
function createWidgetForOption(optionKey, option)
    -- Função: createWidgetForOption
    local widget
    
    if option.type == 'boolean' then
    -- Verificação condicional
        widget = g_ui.createWidget('UICheckBox', parent)
        widget:setChecked(option.value)
        
    elseif option.type == 'number' then
        if option.widget == 'slider' then
    -- Verificação condicional
            widget = g_ui.createWidget('UIScrollBar', parent)
            widget:setRange(option.min or 0, option.max or 100)
            widget:setValue(option.value)
        else
            widget = g_ui.createWidget('UISpinBox', parent)
        end
        
    elseif option.type == 'string' then
        if option.options then
    -- Verificação condicional
            widget = g_ui.createWidget('UIComboBox', parent)
            for _, opt in ipairs(option.options) do
    -- Loop de repetição
                widget:addOption(opt, opt)
            end
        else
            widget = g_ui.createWidget('UITextEdit', parent)
        end
    end
    
    return widget
end
```

### Validação Avançada

#### Validadores Compostos
```lua
-- Validador para porta de rede
    --  Validador para porta de rede (traduzido)
defineOption('serverPort', 7171, {
    validators = {
        rangeValidator(1024, 65535),
        function(value)
            return not isPortInUse(value), "Port already in use"
        end
    }
})

-- Validador para caminho de arquivo
    --  Validador para caminho de arquivo (traduzido)
defineOption('logPath', '/var/log/otclient.log', {
    validators = {
        function(value)
            local dir = dirname(value)
            return g_resources.directoryExists(dir), "Directory does not exist"
        end,
        function(value)
            return hasWritePermission(value), "No write permission"
        end
    }
})
```

## 💡 Exemplos Práticos

### 1. Sistema de Configuração de Gráficos
```lua
-- Definir opções de gráficos
local graphicsOptions = {
    {
        key = 'fullscreen',
        default = false,
        description = 'Enable fullscreen mode',
        callback = function(value)
            g_window.setFullscreen(value)
        end
    },
    {
        key = 'vsync',
        default = true,
        description = 'Enable vertical synchronization',
        callback = function(value)
            g_graphics.setVSync(value)
        end
    },
    {
        key = 'antialiasing',
        default = 'none',
        options = {'none', '2x', '4x', '8x'},
        description = 'Antialiasing level',
        callback = function(value)
            local samples = value == 'none' and 0 or tonumber(value:sub(1, 1))
            g_graphics.setMultisampling(samples)
        end
    },
    {
        key = 'renderScale',
        default = 1.0,
        min = 0.5,
        max = 2.0,
        step = 0.1,
        widget = 'slider',
        description = 'Render scale multiplier',
        callback = function(value)
            g_graphics.setRenderScale(value)
        end
    }
}

-- Registrar todas as opções
for _, option in ipairs(graphicsOptions) do
    -- Loop de repetição
    defineOption(option.key, option.default, option)
    addOptionToCategory('Graphics', option.key)
end
```

### 2. Sistema de Configuração de Audio
#### Inicialização e Configuração
```lua
-- Configuração avançada de audio
local audioConfig = {
    channels = {
        master = { volume = 1.0, enabled = true },
        music = { volume = 0.8, enabled = true },
        effects = { volume = 1.0, enabled = true },
        interface = { volume = 0.6, enabled = true }
    },
    device = 'default',
    sampleRate = 44100,
    bufferSize = 1024
}

-- Definir configuração complexa
defineOption('audioConfig', audioConfig, {
    description = 'Advanced audio configuration',
    category = 'Audio',
    validator = function(config)
        -- Validar estrutura
        if type(config.channels) ~= 'table' then
            return false, "Invalid channels configuration"
        end
```

#### Funcionalidade 1
```lua
        
        for name, channel in pairs(config.channels) do
            if type(channel.volume) ~= 'number' or 
               channel.volume < 0 or channel.volume > 1 then
                return false, "Invalid volume for channel " .. name
            end
        end
        
        return true
    end,
    callback = function(config)
        -- Aplicar configuração
        for name, channel in pairs(config.channels) do
            local soundChannel = g_sounds.getChannel(name)
            if soundChannel then
                soundChannel:setVolume(channel.volume)
                soundChannel:setEnabled(channel.enabled)
            end
        end
        
        g_sounds.setDevice(config.device)
        g_sounds.setSampleRate(config.sampleRate)
    end
```

#### Finalização
```lua
})

-- Funções auxiliares para audio
function setChannelVolume(channelName, volume)
    local config = getOption('audioConfig')
    if config.channels[channelName] then
        config.channels[channelName].volume = volume
        setOption('audioConfig', config)
    end
end

function toggleChannel(channelName)
    local config = getOption('audioConfig')
    if config.channels[channelName] then
        config.channels[channelName].enabled = not config.channels[channelName].enabled
        setOption('audioConfig', config)
    end
end
```

### 3. Sistema de Perfis de Configuração
#### Inicialização e Configuração
```lua
local ConfigProfiles = {}

-- Carregar perfil
function ConfigProfiles.load(profileName)
    local profilePath = 'profiles/' .. profileName .. '.json'
    if g_resources.fileExists(profilePath) then
        local data = g_resources.readFileContents(profilePath)
        local profile = json.decode(data)
        
        for key, value in pairs(profile.options) do
            setOption(key, value, true) -- Forçar aplicação
        end
        
        setOption('currentProfile', profileName)
        print("Profile '" .. profileName .. "' loaded successfully")
        return true
    end
    return false
end

-- Salvar perfil
function ConfigProfiles.save(profileName)
```

#### Funcionalidade 1
```lua
    local profile = {
        name = profileName,
        created = os.time(),
        options = {}
    }
    
    -- Coletar todas as opções
    for key, option in pairs(options) do
        profile.options[key] = option.value
    end
    
    local profilePath = 'profiles/' .. profileName .. '.json'
    local data = json.encode(profile, { indent = true })
    g_resources.writeFileContents(profilePath, data)
    
    print("Profile '" .. profileName .. "' saved successfully")
end

-- Listar perfis disponíveis
function ConfigProfiles.list()
    local profiles = {}
    local files = g_resources.listDirectoryFiles('profiles')
    
    for _, file in ipairs(files) do
        if file:match('%.json$') then
            local name = file:gsub('%.json$', '')
            table.insert(profiles, name)
        end
```

#### Funcionalidade 2
```lua
    end
    
    return profiles
end

-- UI para gerenciamento de perfis
function createProfileManager()
    local profileWindow = g_ui.createWidget('MainWindow')
    profileWindow:setTitle('Configuration Profiles')
    
    local profileList = g_ui.createWidget('UIList', profileWindow)
    local profiles = ConfigProfiles.list()
    
    for _, profile in ipairs(profiles) do
        local item = g_ui.createWidget('UILabel', profileList)
        item:setText(profile)
        item:setPhantom(false)
        
        item.onDoubleClick = function()
            ConfigProfiles.load(profile)
            profileWindow:destroy()
        end
```

#### Finalização
```lua
    end
    
    return profileWindow
end
```

## ✅ Melhores Práticas

### 1. Definição de Opções
- **Use nomes descritivos**: `enableShadows` em vez de `shadows`
- **Defina valores padrão sensatos**: Que funcionem na maioria dos casos
- **Adicione descrições**: Para documentar o propósito da opção
- **Agrupe em categorias**: Para melhor organização

### 2. Validação
- **Sempre valide entradas**: Especialmente valores críticos
- **Mensagens de erro claras**: Explique o que está errado
- **Validação em múltiplas camadas**: Interface + backend
- **Teste valores extremos**: Min/max, strings vazias, etc.

### 3. Callbacks
- **Mantenha callbacks leves**: Evite operações custosas
- **Trate erros gracefully**: Não quebrar por mudança de configuração
- **Atualize interface**: Reflita mudanças visualmente
- **Considere debouncing**: Para mudanças rápidas

### 4. Performance
- **Cache valores frequentes**: Evite getOption() excessivo
- **Batch mudanças**: Agrupe múltiplas alterações
- **Lazy loading**: Carregue configurações sob demanda
- **Minimize persistência**: Salve apenas quando necessário

### 5. Compatibilidade
- **Versionamento**: Mantenha compatibilidade com versões antigas
- **Migração automática**: Para mudanças de estrutura
- **Valores padrão seguros**: Se configuração não existir
- **Fallbacks**: Para quando algo der errado

### 6. Segurança
- **Validação de tipos**: Nunca assuma tipos corretos
- **Sanitização**: Para strings e caminhos de arquivo
- **Limitação de recursos**: Evite configurações que quebrem o sistema
- **Auditoria**: Log mudanças importantes

### 7. Organização
```lua
-- Estrutura recomendada para configurações
local configs = {
    graphics = {
        fullscreen = false,
        vsync = true,
        renderScale = 1.0
    },
    audio = {
        masterVolume = 1.0,
        enableAudio = true
    },
    gameplay = {
        autoWalk = true,
        showFPS = false
    }
}

-- Registrar com prefixos
    --  Registrar com prefixos (traduzido)
for category, options in pairs(configs) do
    -- Loop de repetição
    for key, value in pairs(options) do
    -- Loop de repetição
        defineOption(category .. '.' .. key, value, {
            category = category:gsub("^%l", string.upper)
        })
    end
end
```

## 📊 Métricas e Monitoramento

### Tracking de Mudanças
#### Nível Basic
```lua
local configMetrics = {
-- Interceptar mudanças
local originalSetOption = setOption
setOption = function(key, value, force)
    -- Registrar mudança
end
-- Relatório de uso
function generateConfigReport()
    local report = {
    -- Contar mudanças por chave
    local changeCounts = {}
    end
    -- Ordenar por frequência
    local sortedChanges = {}
    end
    table.sort(sortedChanges, function(a, b) return a.count > b.count end)
end
```

#### Nível Intermediate
```lua
local configMetrics = {
    changes = {},
    accessCount = {},
    lastAccess = {}
}

-- Interceptar mudanças
local originalSetOption = setOption
setOption = function(key, value, force)
    -- Registrar mudança
    table.insert(configMetrics.changes, {
        key = key,
        oldValue = getOption(key),
        newValue = value,
        timestamp = os.time(),
        forced = force or false
    })
    
    return originalSetOption(key, value, force)
end

-- Relatório de uso
function generateConfigReport()
    local report = {
        totalChanges = #configMetrics.changes,
        mostChanged = {},
        recentChanges = {}
    }
    
    -- Contar mudanças por chave
    local changeCounts = {}
    for _, change in ipairs(configMetrics.changes) do
        changeCounts[change.key] = (changeCounts[change.key] or 0) + 1
    end
    
    -- Ordenar por frequência
    local sortedChanges = {}
    for key, count in pairs(changeCounts) do
        table.insert(sortedChanges, {key = key, count = count})
    end
    table.sort(sortedChanges, function(a, b) return a.count > b.count end)
    
    report.mostChanged = sortedChanges
    return report
end
```

#### Nível Advanced
```lua
local configMetrics = {
    changes = {},
    accessCount = {},
    lastAccess = {}
}

-- Interceptar mudanças
local originalSetOption = setOption
setOption = function(key, value, force)
    -- Registrar mudança
    table.insert(configMetrics.changes, {
        key = key,
        oldValue = getOption(key),
        newValue = value,
        timestamp = os.time(),
        forced = force or false
    })
    
    return originalSetOption(key, value, force)
end

-- Relatório de uso
function generateConfigReport()
    local report = {
        totalChanges = #configMetrics.changes,
        mostChanged = {},
        recentChanges = {}
    }
    
    -- Contar mudanças por chave
    local changeCounts = {}
    for _, change in ipairs(configMetrics.changes) do
        changeCounts[change.key] = (changeCounts[change.key] or 0) + 1
    end
    
    -- Ordenar por frequência
    local sortedChanges = {}
    for key, count in pairs(changeCounts) do
        table.insert(sortedChanges, {key = key, count = count})
    end
    table.sort(sortedChanges, function(a, b) return a.count > b.count end)
    
    report.mostChanged = sortedChanges
    return report
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

*Documentação gerada para OTClient - Redemption | Sistema de Configuração Avançada*

---

<div class="success"> Navegação
> - [Getting_Started_Guide](Getting_Started_Guide.md) - Comece aqui
> - [Module_System_Guide](Module_System_Guide.md) - Desenvolvimento de módulos
> - [UI_System_Guide](UI_System_Guide.md) - Interface do usuário
> - [Lua_API_Reference](Lua_API_Reference.md) - Referência completa da API

