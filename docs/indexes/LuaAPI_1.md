# Lua API Reference - OTClient Redemption

Referência completa da API Lua do OTClient, incluindo todas as funções globais, módulos e sistemas disponíveis para desenvolvimento.

## 📋 Índice

1. [Globais Core](#-globais-core)
2. [Sistema de Interface](#-sistema-de-interface)
3. [Sistema de Jogo](#-sistema-de-jogo)
4. [Sistema de Rede](#-sistema-de-rede)
5. [Sistema de Gráficos](#-sistema-de-gráficos)
6. [Sistema de Som](#-sistema-de-som)
7. [Sistema de Configuração](#-sistema-de-configuração)
8. [Utilitários](#-utilitários)
9. [Callbacks e Eventos](#-callbacks-e-eventos)
10. [Exemplos Práticos](#-exemplos-práticos)

## 🌐 Globais Core

### g_app (Application)

**Descrição**: Interface principal da aplicação.

#### Nível Basic
```lua
-- Informações da aplicação
local name = g_app.getName()              -- "OTClient - Redemption"
local version = g_app.getVersion()        -- "1.0.0"
local revision = g_app.getBuildRevision() -- Revisão do build
local commit = g_app.getBuildCommit()     -- Hash do commit
local date = g_app.getBuildDate()         -- Data do build
local arch = g_app.getBuildArch()         -- Arquitetura (x64, x86)
-- Configuração da aplicação
-- Controle da aplicação
```

#### Nível Intermediate
```lua
-- Informações da aplicação
local name = g_app.getName()              -- "OTClient - Redemption"
local version = g_app.getVersion()        -- "1.0.0"
local revision = g_app.getBuildRevision() -- Revisão do build
local commit = g_app.getBuildCommit()     -- Hash do commit
local date = g_app.getBuildDate()         -- Data do build
local arch = g_app.getBuildArch()         -- Arquitetura (x64, x86)

-- Configuração da aplicação
g_app.setName("Meu Cliente")
g_app.setCompactName("meuclient")
g_app.setOrganizationName("minhaorg")

-- Controle da aplicação
g_app.exit()                              -- Fecha a aplicação
g_app.restart()                           -- Reinicia a aplicação
g_app.minimize()                          -- Minimiza a janela
g_app.maximize()                          -- Maximiza a janela
```

#### Nível Advanced
```lua
-- Informações da aplicação
local name = g_app.getName()              -- "OTClient - Redemption"
local version = g_app.getVersion()        -- "1.0.0"
local revision = g_app.getBuildRevision() -- Revisão do build
local commit = g_app.getBuildCommit()     -- Hash do commit
local date = g_app.getBuildDate()         -- Data do build
local arch = g_app.getBuildArch()         -- Arquitetura (x64, x86)

-- Configuração da aplicação
g_app.setName("Meu Cliente")
g_app.setCompactName("meuclient")
g_app.setOrganizationName("minhaorg")

-- Controle da aplicação
g_app.exit()                              -- Fecha a aplicação
g_app.restart()                           -- Reinicia a aplicação
g_app.minimize()                          -- Minimiza a janela
g_app.maximize()                          -- Maximiza a janela
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

### g_platform (Platform)

**Descrição**: Funções específicas da plataforma.

#### Nível Basic
```lua
-- Informações do sistema
local osName = g_platform.getOSName()     -- "Windows", "Linux", "Mac"
local cpuName = g_platform.getCPUName()   -- Nome do processador
local totalMem = g_platform.getTotalSystemMemory() -- Memória total
-- Clipboard
local text = g_platform.getClipboardText() -- Obtém texto do clipboard
-- Diretórios especiais
local home = g_platform.getHomeDir()      -- Diretório home
local desktop = g_platform.getDesktopDir() -- Área de trabalho
local temp = g_platform.getTempDir()      -- Diretório temporário
-- Processamento
local cores = g_platform.getProcessorCount() -- Número de cores
```

#### Nível Intermediate
```lua
-- Informações do sistema
local osName = g_platform.getOSName()     -- "Windows", "Linux", "Mac"
local cpuName = g_platform.getCPUName()   -- Nome do processador
local totalMem = g_platform.getTotalSystemMemory() -- Memória total

-- Clipboard
g_platform.setClipboardText("Texto")     -- Define texto do clipboard
local text = g_platform.getClipboardText() -- Obtém texto do clipboard

-- Diretórios especiais
local home = g_platform.getHomeDir()      -- Diretório home
local desktop = g_platform.getDesktopDir() -- Área de trabalho
local temp = g_platform.getTempDir()      -- Diretório temporário

-- Processamento
local cores = g_platform.getProcessorCount() -- Número de cores
```

#### Nível Advanced
```lua
-- Informações do sistema
local osName = g_platform.getOSName()     -- "Windows", "Linux", "Mac"
local cpuName = g_platform.getCPUName()   -- Nome do processador
local totalMem = g_platform.getTotalSystemMemory() -- Memória total

-- Clipboard
g_platform.setClipboardText("Texto")     -- Define texto do clipboard
local text = g_platform.getClipboardText() -- Obtém texto do clipboard

-- Diretórios especiais
local home = g_platform.getHomeDir()      -- Diretório home
local desktop = g_platform.getDesktopDir() -- Área de trabalho
local temp = g_platform.getTempDir()      -- Diretório temporário

-- Processamento
local cores = g_platform.getProcessorCount() -- Número de cores
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

### g_logger (Logger)

**Descrição**: Sistema de logging.

#### Nível Basic
```lua
-- Configuração
-- Logging
-- Funções auxiliares
g_logger.onLog = function(level, message, time)
    -- Callback personalizado para logs
end
```

#### Nível Intermediate
```lua
-- Configuração
g_logger.setLogFile("meulog.log")         -- Define arquivo de log
g_logger.setLevel(LogLevel.Debug)         -- Define nível de log

-- Logging
g_logger.debug("Mensagem de debug")       -- Nível DEBUG
g_logger.info("Informação importante")    -- Nível INFO
g_logger.warning("Aviso importante")      -- Nível WARNING
g_logger.error("Erro encontrado")         -- Nível ERROR
g_logger.fatal("Erro fatal!")             -- Nível FATAL

-- Funções auxiliares
g_logger.fireOldMessages()                -- Dispara mensagens antigas
g_logger.onLog = function(level, message, time)
    -- Callback personalizado para logs
end
```

#### Nível Advanced
```lua
-- Configuração
g_logger.setLogFile("meulog.log")         -- Define arquivo de log
g_logger.setLevel(LogLevel.Debug)         -- Define nível de log

-- Logging
g_logger.debug("Mensagem de debug")       -- Nível DEBUG
g_logger.info("Informação importante")    -- Nível INFO
g_logger.warning("Aviso importante")      -- Nível WARNING
g_logger.error("Erro encontrado")         -- Nível ERROR
g_logger.fatal("Erro fatal!")             -- Nível FATAL

-- Funções auxiliares
g_logger.fireOldMessages()                -- Dispara mensagens antigas
g_logger.onLog = function(level, message, time)
    -- Callback personalizado para logs
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

### g_resources (Resources)

**Descrição**: Gerenciamento de recursos e arquivos.

#### Nível Basic
```lua
-- Configuração de diretórios
g_resources.setupUserWriteDir("otclient/") -- Define diretório de escrita
local workDir = g_resources.getWorkDir()   -- Diretório de trabalho
local writeDir = g_resources.getWriteDir() -- Diretório de escrita

-- Caminhos de busca
g_resources.addSearchPath("/data", true)   -- Adiciona caminho de busca
g_resources.removeSearchPath("/data")      -- Remove caminho

-- Busca de pacotes
g_resources.searchAndAddPackages("/", ".otpkg", true) -- Busca pacotes

-- Verificação de arquivos
local exists = g_resources.fileExists("arquivo.lua") -- Verifica se existe
local size = g_resources.getFileSize("arquivo.lua")  -- Tamanho do arquivo
local time = g_resources.getFileTime("arquivo.lua")  -- Timestamp do arquivo

-- Operações de arquivo
local content = g_resources.readFileContents("arquivo.txt") -- Lê conteúdo
g_resources.writeFileContents("arquivo.txt", "conteúdo")    -- Escreve conteúdo

-- Diretórios
local files = g_resources.listDirectoryFiles("/data")       -- Lista arquivos
g_resources.makeDir("novapasta")                            -- Cria diretório

-- URLs e downloads
g_resources.downloadFile("http://exemplo.com/arquivo.zip", "local.zip")
```

#### Nível Intermediate
```lua
-- Configuração de diretórios
g_resources.setupUserWriteDir("otclient/") -- Define diretório de escrita
local workDir = g_resources.getWorkDir()   -- Diretório de trabalho
local writeDir = g_resources.getWriteDir() -- Diretório de escrita

-- Caminhos de busca
g_resources.addSearchPath("/data", true)   -- Adiciona caminho de busca
g_resources.removeSearchPath("/data")      -- Remove caminho

-- Busca de pacotes
g_resources.searchAndAddPackages("/", ".otpkg", true) -- Busca pacotes

-- Verificação de arquivos
local exists = g_resources.fileExists("arquivo.lua") -- Verifica se existe
local size = g_resources.getFileSize("arquivo.lua")  -- Tamanho do arquivo
local time = g_resources.getFileTime("arquivo.lua")  -- Timestamp do arquivo

-- Operações de arquivo
local content = g_resources.readFileContents("arquivo.txt") -- Lê conteúdo
g_resources.writeFileContents("arquivo.txt", "conteúdo")    -- Escreve conteúdo

-- Diretórios
local files = g_resources.listDirectoryFiles("/data")       -- Lista arquivos
g_resources.makeDir("novapasta")                            -- Cria diretório

-- URLs e downloads
g_resources.downloadFile("http://exemplo.com/arquivo.zip", "local.zip")
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
-- Configuração de diretórios
g_resources.setupUserWriteDir("otclient/") -- Define diretório de escrita
local workDir = g_resources.getWorkDir()   -- Diretório de trabalho
local writeDir = g_resources.getWriteDir() -- Diretório de escrita

-- Caminhos de busca
g_resources.addSearchPath("/data", true)   -- Adiciona caminho de busca
g_resources.removeSearchPath("/data")      -- Remove caminho

-- Busca de pacotes
g_resources.searchAndAddPackages("/", ".otpkg", true) -- Busca pacotes

-- Verificação de arquivos
local exists = g_resources.fileExists("arquivo.lua") -- Verifica se existe
local size = g_resources.getFileSize("arquivo.lua")  -- Tamanho do arquivo
local time = g_resources.getFileTime("arquivo.lua")  -- Timestamp do arquivo

-- Operações de arquivo
local content = g_resources.readFileContents("arquivo.txt") -- Lê conteúdo
g_resources.writeFileContents("arquivo.txt", "conteúdo")    -- Escreve conteúdo

-- Diretórios
local files = g_resources.listDirectoryFiles("/data")       -- Lista arquivos
g_resources.makeDir("novapasta")                            -- Cria diretório

-- URLs e downloads
g_resources.downloadFile("http://exemplo.com/arquivo.zip", "local.zip")
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

### g_modules (Modules)

**Descrição**: Sistema de módulos do cliente.

#### Nível Basic
```lua
-- Descoberta e carregamento
-- Controle de módulos
-- Informações de módulos
local module = g_modules.getModule("meu_modulo") -- Obtém instância do módulo
local loaded = g_modules.isModuleLoaded("meu_modulo") -- Verifica se carregado
local modules = g_modules.getModules()    -- Lista todos os módulos
-- Propriedades do módulo
if module then
    local name = module:getName()         -- Nome do módulo
    local desc = module:getDescription()  -- Descrição
    local author = module:getAuthor()     -- Autor
    local version = module:getVersion()   -- Versão
    local deps = module:getDependencies() -- Dependências
    local loaded = module:isLoaded()      -- Status de carregamento
    local sandboxed = module:isSandboxed() -- Executando em sandbox
end
```

#### Nível Intermediate
```lua
-- Descoberta e carregamento
g_modules.discoverModules()               -- Descobre módulos disponíveis
g_modules.autoLoadModules(999)            -- Carrega módulos até prioridade 999
g_modules.ensureModuleLoaded("game_interface") -- Garante que módulo está carregado

-- Controle de módulos
g_modules.reloadModule("meu_modulo")      -- Recarrega módulo específico
g_modules.unloadModule("meu_modulo")      -- Descarrega módulo
g_modules.enableAutoReload()             -- Habilita recarga automática

-- Informações de módulos
local module = g_modules.getModule("meu_modulo") -- Obtém instância do módulo
local loaded = g_modules.isModuleLoaded("meu_modulo") -- Verifica se carregado
local modules = g_modules.getModules()    -- Lista todos os módulos

-- Propriedades do módulo
if module then
    local name = module:getName()         -- Nome do módulo
    local desc = module:getDescription()  -- Descrição
    local author = module:getAuthor()     -- Autor
    local version = module:getVersion()   -- Versão
    local deps = module:getDependencies() -- Dependências
    local loaded = module:isLoaded()      -- Status de carregamento
    local sandboxed = module:isSandboxed() -- Executando em sandbox
end
```

#### Nível Advanced
```lua
-- Descoberta e carregamento
g_modules.discoverModules()               -- Descobre módulos disponíveis
g_modules.autoLoadModules(999)            -- Carrega módulos até prioridade 999
g_modules.ensureModuleLoaded("game_interface") -- Garante que módulo está carregado

-- Controle de módulos
g_modules.reloadModule("meu_modulo")      -- Recarrega módulo específico
g_modules.unloadModule("meu_modulo")      -- Descarrega módulo
g_modules.enableAutoReload()             -- Habilita recarga automática

-- Informações de módulos
local module = g_modules.getModule("meu_modulo") -- Obtém instância do módulo
local loaded = g_modules.isModuleLoaded("meu_modulo") -- Verifica se carregado
local modules = g_modules.getModules()    -- Lista todos os módulos

-- Propriedades do módulo
if module then
    local name = module:getName()         -- Nome do módulo
    local desc = module:getDescription()  -- Descrição
    local author = module:getAuthor()     -- Autor
    local version = module:getVersion()   -- Versão
    local deps = module:getDependencies() -- Dependências
    local loaded = module:isLoaded()      -- Status de carregamento
    local sandboxed = module:isSandboxed() -- Executando em sandbox
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

### g_clock (Clock)

**Descrição**: Funções de tempo e temporização.

```lua
-- Tempo atual
    --  Tempo atual (traduzido)
local millis = g_clock.millis()           -- Tempo em milissegundos
local micros = g_clock.micros()           -- Tempo em microssegundos
local seconds = g_clock.seconds()         -- Tempo em segundos

-- Conversões
local realTime = g_clock.millisToString(millis) -- Converte para string legível
```

### g_crypt (Cryptography)

**Descrição**: Funções criptográficas.

```lua
-- RSA
    --  RSA (traduzido)
local rsa = g_crypt.genRSAKey(1024)       -- Gera chave RSA
g_crypt.setRSAPublicKey(key, exponent)    -- Define chave pública

-- Hashing
    --  Hashing (traduzido)
local md5 = g_crypt.md5Encode("texto")    -- Hash MD5
local sha1 = g_crypt.sha1Encode("texto")  -- Hash SHA1
local sha256 = g_crypt.sha256Encode("texto") -- Hash SHA256

-- Codificação
local base64 = g_crypt.base64Encode("texto") -- Codifica em Base64
local decoded = g_crypt.base64Decode(base64)  -- Decodifica Base64
```

## 🎨 Sistema de Interface

### g_ui (User Interface)

**Descrição**: Gerenciamento de interface gráfica.

#### Nível Basic
```lua
-- Carregamento de UI
local window = g_ui.loadUI("janela.otui", rootWidget) -- Carrega UI de arquivo
local widget = g_ui.createWidget("UIPushButton")      -- Cria widget específico
local display = g_ui.displayUI("janela.otui")         -- Exibe UI como janela

-- Widgets especiais
local tooltip = g_ui.createTooltip()     -- Cria tooltip
local messagebox = g_ui.createMessageBox("Título", "Mensagem", MessageBoxOk)

-- Estados
local focused = g_ui.getFocusedChild()   -- Widget com foco
g_ui.setRootWidget(widget)               -- Define widget raiz

-- Mouse
local grabbing = g_ui.isMouseGrabbed()   -- Verifica se mouse está capturado
local position = g_ui.getMousePosition() -- Posição do mouse

-- Teclado
g_ui.setKeyboardReceiver(widget)         -- Define receptor de teclado

-- Importação de estilos
g_ui.importStyle("styles.otui")          -- Importa estilos
```

#### Nível Intermediate
```lua
-- Carregamento de UI
local window = g_ui.loadUI("janela.otui", rootWidget) -- Carrega UI de arquivo
local widget = g_ui.createWidget("UIPushButton")      -- Cria widget específico
local display = g_ui.displayUI("janela.otui")         -- Exibe UI como janela

-- Widgets especiais
local tooltip = g_ui.createTooltip()     -- Cria tooltip
local messagebox = g_ui.createMessageBox("Título", "Mensagem", MessageBoxOk)

-- Estados
local focused = g_ui.getFocusedChild()   -- Widget com foco
g_ui.setRootWidget(widget)               -- Define widget raiz

-- Mouse
local grabbing = g_ui.isMouseGrabbed()   -- Verifica se mouse está capturado
local position = g_ui.getMousePosition() -- Posição do mouse

-- Teclado
g_ui.setKeyboardReceiver(widget)         -- Define receptor de teclado

-- Importação de estilos
g_ui.importStyle("styles.otui")          -- Importa estilos
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
-- Carregamento de UI
local window = g_ui.loadUI("janela.otui", rootWidget) -- Carrega UI de arquivo
local widget = g_ui.createWidget("UIPushButton")      -- Cria widget específico
local display = g_ui.displayUI("janela.otui")         -- Exibe UI como janela

-- Widgets especiais
local tooltip = g_ui.createTooltip()     -- Cria tooltip
local messagebox = g_ui.createMessageBox("Título", "Mensagem", MessageBoxOk)

-- Estados
local focused = g_ui.getFocusedChild()   -- Widget com foco
g_ui.setRootWidget(widget)               -- Define widget raiz

-- Mouse
local grabbing = g_ui.isMouseGrabbed()   -- Verifica se mouse está capturado
local position = g_ui.getMousePosition() -- Posição do mouse

-- Teclado
g_ui.setKeyboardReceiver(widget)         -- Define receptor de teclado

-- Importação de estilos
g_ui.importStyle("styles.otui")          -- Importa estilos
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

### Widget Base

**Descrição**: Funcionalidades básicas de todos os widgets.

#### Inicialização e Configuração
```lua
-- Hierarquia
local parent = widget:getParent()        -- Widget pai
local children = widget:getChildren()    -- Widgets filhos
local child = widget:getChildById("id")  -- Filho por ID
widget:addChild(childWidget)             -- Adiciona filho
widget:removeChild(childWidget)          -- Remove filho
widget:destroyChildren()                 -- Destroi todos os filhos

-- Propriedades básicas
widget:setId("meuWidget")                -- Define ID
local id = widget:getId()                -- Obtém ID
widget:setVisible(true)                  -- Define visibilidade
local visible = widget:isVisible()       -- Verifica visibilidade
widget:setEnabled(true)                  -- Define se habilitado
local enabled = widget:isEnabled()       -- Verifica se habilitado

-- Posicionamento e tamanho
widget:setPosition({x = 100, y = 50})    -- Define posição
local pos = widget:getPosition()         -- Obtém posição
widget:setSize({width = 200, height = 100}) -- Define tamanho
local size = widget:getSize()            -- Obtém tamanho
widget:setRect({x = 0, y = 0, width = 100, height = 50}) -- Define retângulo completo

-- Margem e padding
widget:setMargin(10)                     -- Define margem uniforme
widget:setMarginTop(5)                   -- Margem superior
widget:setPadding(5)                     -- Define padding uniforme

-- Estilo visual
widget:setBackgroundColor("#FF0000")     -- Cor de fundo
widget:setBorderWidth(2)                 -- Largura da borda
widget:setBorderColor("#000000")         -- Cor da borda
widget:setOpacity(0.8)                   -- Opacidade (0.0 - 1.0)

-- Texto
widget:setText("Meu Texto")              -- Define texto
local text = widget:getText()            -- Obtém texto
widget:setTextColor("#FFFFFF")           -- Cor do texto
widget:setFont("verdana-11px-rounded")   -- Fonte do texto

-- Foco e seleção
widget:focus()                           -- Da foco ao widget
widget:clearFocus()                      -- Remove foco
local focused = widget:isFocused()       -- Verifica se tem foco

-- Eventos
widget.onClick = function(widget)
    print("Widget clicado!")
end
```

#### Finalização
```lua

widget.onDoubleClick = function(widget)
    print("Widget duplo-clicado!")
end

widget.onHoverChange = function(widget, hovered)
    if hovered then
        widget:setBackgroundColor("#FFFF00")
    else
        widget:setBackgroundColor("#FFFFFF")
    end
end

-- Destruição
widget:destroy()                         -- Destroi o widget
```

### UIWindow

**Descrição**: Janelas da interface.

#### Nível Basic
```lua
local window = g_ui.createWidget("UIWindow", rootWidget)

-- Configuração da janela
window:setTitle("Minha Janela")          -- Título da janela
local title = window:getTitle()          -- Obtém título

-- Controles da janela
window:setResizable(true)                -- Permite redimensionamento
window:setMoveable(true)                 -- Permite movimento
window:setCloseable(true)                -- Permite fechar

-- Estados
window:show()                            -- Exibe janela
window:hide()                            -- Oculta janela
window:raise()                           -- Traz para frente
window:minimize()                        -- Minimiza
window:maximize()                        -- Maximiza

-- Eventos específicos
window.onClose = function(window)
    print("Janela fechada!")
end

window.onMinimize = function(window)
    print("Janela minimizada!")
end
```

#### Nível Intermediate
```lua
local window = g_ui.createWidget("UIWindow", rootWidget)

-- Configuração da janela
window:setTitle("Minha Janela")          -- Título da janela
local title = window:getTitle()          -- Obtém título

-- Controles da janela
window:setResizable(true)                -- Permite redimensionamento
window:setMoveable(true)                 -- Permite movimento
window:setCloseable(true)                -- Permite fechar

-- Estados
window:show()                            -- Exibe janela
window:hide()                            -- Oculta janela
window:raise()                           -- Traz para frente
window:minimize()                        -- Minimiza
window:maximize()                        -- Maximiza

-- Eventos específicos
window.onClose = function(window)
    print("Janela fechada!")
end

window.onMinimize = function(window)
    print("Janela minimizada!")
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
local window = g_ui.createWidget("UIWindow", rootWidget)

-- Configuração da janela
window:setTitle("Minha Janela")          -- Título da janela
local title = window:getTitle()          -- Obtém título

-- Controles da janela
window:setResizable(true)                -- Permite redimensionamento
window:setMoveable(true)                 -- Permite movimento
window:setCloseable(true)                -- Permite fechar

-- Estados
window:show()                            -- Exibe janela
window:hide()                            -- Oculta janela
window:raise()                           -- Traz para frente
window:minimize()                        -- Minimiza
window:maximize()                        -- Maximiza

-- Eventos específicos
window.onClose = function(window)
    print("Janela fechada!")
end

window.onMinimize = function(window)
    print("Janela minimizada!")
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

### UIButton

**Descrição**: Botões clicáveis.

#### Nível Basic
```lua
local button = g_ui.createWidget("UIButton", parent)

-- Configuração
button:setText("Clique Aqui")            -- Texto do botão
button:setIcon("/icons/button.png")      -- Ícone do botão

-- Estados
button:setCheckable(true)                -- Permite ser checkable
button:setChecked(true)                  -- Define como checked
local checked = button:isChecked()       -- Verifica se checked
button:setPressed(true)                  -- Estado pressionado

-- Eventos
button.onClick = function(button)
    print("Botão clicado: " .. button:getText())
end

button.onCheckChange = function(button, checked)
    print("Estado alterado: " .. tostring(checked))
end
```

#### Nível Intermediate
```lua
local button = g_ui.createWidget("UIButton", parent)

-- Configuração
button:setText("Clique Aqui")            -- Texto do botão
button:setIcon("/icons/button.png")      -- Ícone do botão

-- Estados
button:setCheckable(true)                -- Permite ser checkable
button:setChecked(true)                  -- Define como checked
local checked = button:isChecked()       -- Verifica se checked
button:setPressed(true)                  -- Estado pressionado

-- Eventos
button.onClick = function(button)
    print("Botão clicado: " .. button:getText())
end

button.onCheckChange = function(button, checked)
    print("Estado alterado: " .. tostring(checked))
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
local button = g_ui.createWidget("UIButton", parent)

-- Configuração
button:setText("Clique Aqui")            -- Texto do botão
button:setIcon("/icons/button.png")      -- Ícone do botão

-- Estados
button:setCheckable(true)                -- Permite ser checkable
button:setChecked(true)                  -- Define como checked
local checked = button:isChecked()       -- Verifica se checked
button:setPressed(true)                  -- Estado pressionado

-- Eventos
button.onClick = function(button)
    print("Botão clicado: " .. button:getText())
end

button.onCheckChange = function(button, checked)
    print("Estado alterado: " .. tostring(checked))
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

### UITextEdit

**Descrição**: Campos de entrada de texto.

#### Nível Basic
```lua
local textEdit = g_ui.createWidget("UITextEdit", parent)
-- Configuração de texto
local text = textEdit:getText()          -- Obtém texto
textEdit:appendText(" mais texto")       -- Adiciona texto
-- Cursor e seleção
local pos = textEdit:getCursorPos()      -- Obtém posição do cursor
-- Configurações
-- Eventos
textEdit.onTextChange = function(textEdit, text, oldText)
    print("Texto alterado de '" .. oldText .. "' para '" .. text .. "'")
end
textEdit.onEnterPressed = function(textEdit)
    print("Enter pressionado com texto: " .. textEdit:getText())
end
```

#### Nível Intermediate
```lua
local textEdit = g_ui.createWidget("UITextEdit", parent)

-- Configuração de texto
textEdit:setText("Texto inicial")        -- Define texto
local text = textEdit:getText()          -- Obtém texto
textEdit:clearText()                     -- Limpa texto
textEdit:appendText(" mais texto")       -- Adiciona texto

-- Cursor e seleção
textEdit:setCursorPos(5)                 -- Posição do cursor
local pos = textEdit:getCursorPos()      -- Obtém posição do cursor
textEdit:setSelection(0, 10)             -- Seleciona texto
textEdit:selectAll()                     -- Seleciona tudo

-- Configurações
textEdit:setMaxLength(100)               -- Tamanho máximo
textEdit:setEditable(true)               -- Permite edição
textEdit:setMultiline(true)              -- Permite múltiplas linhas
textEdit:setPasswordMode(true)           -- Modo senha

-- Eventos
textEdit.onTextChange = function(textEdit, text, oldText)
    print("Texto alterado de '" .. oldText .. "' para '" .. text .. "'")
end

textEdit.onEnterPressed = function(textEdit)
    print("Enter pressionado com texto: " .. textEdit:getText())
end
```

#### Nível Advanced
```lua
local textEdit = g_ui.createWidget("UITextEdit", parent)

-- Configuração de texto
textEdit:setText("Texto inicial")        -- Define texto
local text = textEdit:getText()          -- Obtém texto
textEdit:clearText()                     -- Limpa texto
textEdit:appendText(" mais texto")       -- Adiciona texto

-- Cursor e seleção
textEdit:setCursorPos(5)                 -- Posição do cursor
local pos = textEdit:getCursorPos()      -- Obtém posição do cursor
textEdit:setSelection(0, 10)             -- Seleciona texto
textEdit:selectAll()                     -- Seleciona tudo

-- Configurações
textEdit:setMaxLength(100)               -- Tamanho máximo
textEdit:setEditable(true)               -- Permite edição
textEdit:setMultiline(true)              -- Permite múltiplas linhas
textEdit:setPasswordMode(true)           -- Modo senha

-- Eventos
textEdit.onTextChange = function(textEdit, text, oldText)
    print("Texto alterado de '" .. oldText .. "' para '" .. text .. "'")
end

textEdit.onEnterPressed = function(textEdit)
    print("Enter pressionado com texto: " .. textEdit:getText())
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

### UILabel

**Descrição**: Labels para exibição de texto.

#### Nível Basic
```lua
local label = g_ui.createWidget("UILabel", parent)

-- Configuração
label:setText("Meu Label")               -- Define texto
label:setTextAlign(AlignCenter)          -- Alinhamento do texto
label:setTextWrap(true)                  -- Quebra de linha automática
label:setAutoResize(true)                -- Redimensiona automaticamente

-- Colorização
label:setTextColor("#FF0000")            -- Cor do texto
label:setColoredText("Texto {#FF0000}vermelho{#FFFFFF} e branco")
```

#### Nível Intermediate
```lua
local label = g_ui.createWidget("UILabel", parent)

-- Configuração
label:setText("Meu Label")               -- Define texto
label:setTextAlign(AlignCenter)          -- Alinhamento do texto
label:setTextWrap(true)                  -- Quebra de linha automática
label:setAutoResize(true)                -- Redimensiona automaticamente

-- Colorização
label:setTextColor("#FF0000")            -- Cor do texto
label:setColoredText("Texto {#FF0000}vermelho{#FFFFFF} e branco")
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
local label = g_ui.createWidget("UILabel", parent)

-- Configuração
label:setText("Meu Label")               -- Define texto
label:setTextAlign(AlignCenter)          -- Alinhamento do texto
label:setTextWrap(true)                  -- Quebra de linha automática
label:setAutoResize(true)                -- Redimensiona automaticamente

-- Colorização
label:setTextColor("#FF0000")            -- Cor do texto
label:setColoredText("Texto {#FF0000}vermelho{#FFFFFF} e branco")
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

### UIProgressBar

**Descrição**: Barras de progresso.

#### Nível Basic
```lua
local progressBar = g_ui.createWidget("UIProgressBar", parent)

-- Configuração
progressBar:setMinimum(0)                -- Valor mínimo
progressBar:setMaximum(100)              -- Valor máximo
progressBar:setValue(50)                 -- Valor atual (50%)
local value = progressBar:getValue()     -- Obtém valor atual
local percent = progressBar:getPercent() -- Percentual (0.0 - 1.0)

-- Visual
progressBar:setBackgroundColor("#808080") -- Cor de fundo
progressBar:setForegroundColor("#00FF00") -- Cor do progresso
```

#### Nível Intermediate
```lua
local progressBar = g_ui.createWidget("UIProgressBar", parent)

-- Configuração
progressBar:setMinimum(0)                -- Valor mínimo
progressBar:setMaximum(100)              -- Valor máximo
progressBar:setValue(50)                 -- Valor atual (50%)
local value = progressBar:getValue()     -- Obtém valor atual
local percent = progressBar:getPercent() -- Percentual (0.0 - 1.0)

-- Visual
progressBar:setBackgroundColor("#808080") -- Cor de fundo
progressBar:setForegroundColor("#00FF00") -- Cor do progresso
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
local progressBar = g_ui.createWidget("UIProgressBar", parent)

-- Configuração
progressBar:setMinimum(0)                -- Valor mínimo
progressBar:setMaximum(100)              -- Valor máximo
progressBar:setValue(50)                 -- Valor atual (50%)
local value = progressBar:getValue()     -- Obtém valor atual
local percent = progressBar:getPercent() -- Percentual (0.0 - 1.0)

-- Visual
progressBar:setBackgroundColor("#808080") -- Cor de fundo
progressBar:setForegroundColor("#00FF00") -- Cor do progresso
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

### UIComboBox

**Descrição**: Caixas de seleção dropdown.

#### Nível Basic
```lua
local comboBox = g_ui.createWidget("UIComboBox", parent)

-- Gerenciamento de opções
comboBox:addOption("Opção 1", "valor1")  -- Adiciona opção
comboBox:addOption("Opção 2", "valor2")
comboBox:removeOption("Opção 1")         -- Remove opção
comboBox:clearOptions()                  -- Limpa todas as opções

-- Seleção
comboBox:setCurrentIndex(0)              -- Seleciona por índice
comboBox:setCurrentOption("Opção 1")     -- Seleciona por texto
comboBox:setCurrentOptionByData("valor1") -- Seleciona por data
local selected = comboBox:getCurrentOption() -- Opção selecionada
local index = comboBox:getCurrentIndex() -- Índice selecionado

-- Eventos
comboBox.onOptionChange = function(comboBox, optionText, optionData)
    print("Selecionado: " .. optionText .. " (data: " .. optionData .. ")")
end
```

#### Nível Intermediate
```lua
local comboBox = g_ui.createWidget("UIComboBox", parent)

-- Gerenciamento de opções
comboBox:addOption("Opção 1", "valor1")  -- Adiciona opção
comboBox:addOption("Opção 2", "valor2")
comboBox:removeOption("Opção 1")         -- Remove opção
comboBox:clearOptions()                  -- Limpa todas as opções

-- Seleção
comboBox:setCurrentIndex(0)              -- Seleciona por índice
comboBox:setCurrentOption("Opção 1")     -- Seleciona por texto
comboBox:setCurrentOptionByData("valor1") -- Seleciona por data
local selected = comboBox:getCurrentOption() -- Opção selecionada
local index = comboBox:getCurrentIndex() -- Índice selecionado

-- Eventos
comboBox.onOptionChange = function(comboBox, optionText, optionData)
    print("Selecionado: " .. optionText .. " (data: " .. optionData .. ")")
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
local comboBox = g_ui.createWidget("UIComboBox", parent)

-- Gerenciamento de opções
comboBox:addOption("Opção 1", "valor1")  -- Adiciona opção
comboBox:addOption("Opção 2", "valor2")
comboBox:removeOption("Opção 1")         -- Remove opção
comboBox:clearOptions()                  -- Limpa todas as opções

-- Seleção
comboBox:setCurrentIndex(0)              -- Seleciona por índice
comboBox:setCurrentOption("Opção 1")     -- Seleciona por texto
comboBox:setCurrentOptionByData("valor1") -- Seleciona por data
local selected = comboBox:getCurrentOption() -- Opção selecionada
local index = comboBox:getCurrentIndex() -- Índice selecionado

-- Eventos
comboBox.onOptionChange = function(comboBox, optionText, optionData)
    print("Selecionado: " .. optionText .. " (data: " .. optionData .. ")")
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

### UIListWidget

**Descrição**: Listas de itens.

#### Nível Basic
```lua
local listWidget = g_ui.createWidget("UIListWidget", parent)

-- Adição de itens
local item1 = g_ui.createWidget("UIListItem")
item1:setText("Item 1")
listWidget:addChild(item1)

-- Seleção
listWidget:focusChild(item1)             -- Foca item
local focused = listWidget:getFocusedChild() -- Item focado
listWidget:selectAll()                   -- Seleciona tudo
listWidget:clearSelection()              -- Limpa seleção

-- Navegação
listWidget:focusNextChild()              -- Próximo item
listWidget:focusPreviousChild()          -- Item anterior

-- Eventos
listWidget.onChildFocusChange = function(listWidget, focusedChild)
    if focusedChild then
        print("Item focado: " .. focusedChild:getText())
    end
end
```

#### Nível Intermediate
```lua
local listWidget = g_ui.createWidget("UIListWidget", parent)

-- Adição de itens
local item1 = g_ui.createWidget("UIListItem")
item1:setText("Item 1")
listWidget:addChild(item1)

-- Seleção
listWidget:focusChild(item1)             -- Foca item
local focused = listWidget:getFocusedChild() -- Item focado
listWidget:selectAll()                   -- Seleciona tudo
listWidget:clearSelection()              -- Limpa seleção

-- Navegação
listWidget:focusNextChild()              -- Próximo item
listWidget:focusPreviousChild()          -- Item anterior

-- Eventos
listWidget.onChildFocusChange = function(listWidget, focusedChild)
    if focusedChild then
        print("Item focado: " .. focusedChild:getText())
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
local listWidget = g_ui.createWidget("UIListWidget", parent)

-- Adição de itens
local item1 = g_ui.createWidget("UIListItem")
item1:setText("Item 1")
listWidget:addChild(item1)

-- Seleção
listWidget:focusChild(item1)             -- Foca item
local focused = listWidget:getFocusedChild() -- Item focado
listWidget:selectAll()                   -- Seleciona tudo
listWidget:clearSelection()              -- Limpa seleção

-- Navegação
listWidget:focusNextChild()              -- Próximo item
listWidget:focusPreviousChild()          -- Item anterior

-- Eventos
listWidget.onChildFocusChange = function(listWidget, focusedChild)
    if focusedChild then
        print("Item focado: " .. focusedChild:getText())
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

### UIItem

**Descrição**: Widgets para exibição de itens do jogo.

```lua
local itemWidget = g_ui.createWidget("UIItem", parent)

-- Configuração do item
itemWidget:setItemId(2160)               -- ID do item (gold coin)
itemWidget:setItemCount(100)             -- Quantidade
itemWidget:setItemSubType(5)             -- Subtipo (para fluidos)
local item = itemWidget:getItem()        -- Objeto Item

-- Estados
    --  Estados (traduzido)
itemWidget:setVirtual(true)              -- Item virtual (não real)
local virtual = itemWidget:isVirtual()   -- Verifica se virtual

-- Eventos
    --  Eventos (traduzido)
itemWidget.onDrop = function(itemWidget, mousePos, item)
    print("Item dropado: " .. item:getId())
end

itemWidget.onDoubleClick = function(itemWidget)
    local item = itemWidget:getItem()
    if item then
    -- Verificação condicional
        g_game.use(item)
    end
end
```

### UIScrollArea

**Descrição**: Áreas com rolagem.

```lua
local scrollArea = g_ui.createWidget("UIScrollArea", parent)

-- Configuração
scrollArea:setVerticalScrollBar(scrollBar) -- Barra de rolagem vertical
scrollArea:setHorizontalScrollBar(scrollBar) -- Barra de rolagem horizontal

-- Controle de rolagem
    --  Controle de rolagem (traduzido)
scrollArea:setVerticalScrollStep(10)     -- Passo da rolagem vertical
scrollArea:setHorizontalScrollStep(10)   -- Passo da rolagem horizontal
scrollArea:scrollToTop()                 -- Rola para o topo
scrollArea:scrollToBottom()              -- Rola para baixo

-- Estado
    --  Estado (traduzido)
local offset = scrollArea:getScrollOffset() -- Offset atual
scrollArea:setScrollOffset(offset)       -- Define offset
```

## 🎮 Sistema de Jogo

### g_game (Game)

**Descrição**: Interface principal do jogo.

#### Inicialização e Configuração
```lua
-- Estado da conexão
local online = g_game.isOnline()         -- Verifica se está online
local connecting = g_game.isConnecting() -- Verifica se conectando
local version = g_game.getClientVersion() -- Versão do protocolo

-- Personagem
local player = g_game.getLocalPlayer()   -- Jogador local
local name = g_game.getCharacterName()   -- Nome do personagem

-- Mundo
local worldName = g_game.getWorldName()  -- Nome do mundo
local worldId = g_game.getWorldId()      -- ID do mundo

-- Comunicação
g_game.talk("Olá mundo!")               -- Fala normal
g_game.talkChannel(ChannelType.Say, 0, "Mensagem") -- Fala em canal
g_game.talkPrivate(ChannelType.Private, "Player", "Mensagem privada")

-- Movimento
g_game.walk(North)                      -- Anda para direção
g_game.autoWalk({                       -- Caminhada automática
    {x = 100, y = 100, z = 7},
    {x = 101, y = 100, z = 7}
})
```

#### Funcionalidade 1
```lua
g_game.stop()                           -- Para movimento

-- Combate
g_game.attack(creature)                 -- Ataca criatura
g_game.follow(creature)                 -- Segue criatura
g_game.setChaseMode(ChaseOpponent)      -- Define modo de perseguição
g_game.setFightMode(FightBalanced)      -- Define modo de luta

-- Itens
g_game.use(item)                        -- Usa item
g_game.useWith(item, target)            -- Usa item em alvo
g_game.useInventoryItem(itemId)         -- Usa item do inventário
g_game.move(item, toPos, count)         -- Move item

-- Container
g_game.open(item, container)            -- Abre container
g_game.openParent(container)            -- Abre container pai
g_game.close(container)                 -- Fecha container

-- NPC
g_game.talkChannel(ChannelType.NpcTo, 0, "hi") -- Fala com NPC
g_game.closeNpcTrade()                  -- Fecha trade com NPC

-- Party
g_game.partyInvite(playerId)            -- Convida para party
g_game.partyJoin(leaderId)              -- Entra na party
g_game.partyRevokeInvitation(playerId)  -- Revoga convite
g_game.partyPassLeadership(playerId)    -- Passa liderança

-- Guild
g_game.joinGuild()                      -- Entra na guild
g_game.leaveGuild()                     -- Sai da guild

-- Configurações do jogo
g_game.setProtocolVersion(version)      -- Define versão do protocolo
g_game.setClientVersion(version)        -- Define versão do cliente

-- Eventos de conexão
connect(g_game, {
    onGameStart = function()
        print("Jogo iniciado!")
    end,
```

#### Finalização
```lua
    onGameEnd = function()
        print("Jogo finalizado!")
    end,
    onLoginError = function(message)
        print("Erro de login: " .. message)
    end,
    onConnectionError = function(message, code)
        print("Erro de conexão: " .. message .. " (código: " .. code .. ")")
    end
})

-- Eventos de personagem
connect(g_game, {
    onLocalPlayerPositionChange = function(newPos, oldPos)
        print("Posição alterada de " .. oldPos.x .. "," .. oldPos.y .. "," .. oldPos.z ..
              " para " .. newPos.x .. "," .. newPos.y .. "," .. newPos.z)
    end,
    onLocalPlayerStatsChange = function(localPlayer)
        print("Stats alteradas - HP: " .. localPlayer:getHealth())
    end
})
```

### g_map (Map)

**Descrição**: Sistema de mapa e tiles.

#### Nível Basic
```lua
-- Informações do mapa
local centerPos = g_map.getCentralPosition() -- Posição central
local cameraPos = g_map.getCameraPosition() -- Posição da câmera
-- Tiles
local tile = g_map.getTile(position)     -- Obtém tile na posição
local tiles = g_map.getTiles(fromPos, toPos) -- Tiles em área
-- Criaturas
local creatures = g_map.getCreatures()   -- Todas as criaturas
local spectators = g_map.getSpectators(centerPos, multifloor, xRange, yRange)
-- Path finding
local path = g_map.findPath(fromPos, toPos, maxDistance)
local reachable = g_map.canReach(fromPos, toPos, maxDistance)
-- Informações de tile
if tile then
    local walkable = tile:isWalkable()   -- Verificar se é caminhável
    local ground = tile:getGround()      -- Item do chão
    local items = tile:getItems()        -- Itens no tile
    local creature = tile:getTopCreature() -- Criatura no topo
    local moveThing = tile:getTopMoveThing() -- Coisa movível no topo
    -- Verificações
    local hasCreature = tile:hasCreature() -- Tem criatura
    local isEmpty = tile:isEmpty()        -- Está vazio
    local isBlocking = tile:isBlocking()  -- Está bloqueando
end
-- Eventos do mapa
    onTileUpdate = function(tile)
        print("Tile atualizado: " .. tile:getPosition().x .. "," .. tile:getPosition().y)
    end
```

#### Nível Intermediate
```lua
-- Informações do mapa
local centerPos = g_map.getCentralPosition() -- Posição central
g_map.setCentralPosition(position)       -- Define posição central
local cameraPos = g_map.getCameraPosition() -- Posição da câmera

-- Tiles
local tile = g_map.getTile(position)     -- Obtém tile na posição
local tiles = g_map.getTiles(fromPos, toPos) -- Tiles em área
g_map.cleanTile(position)                -- Limpa tile

-- Criaturas
local creatures = g_map.getCreatures()   -- Todas as criaturas
local spectators = g_map.getSpectators(centerPos, multifloor, xRange, yRange)
g_map.addCreature(creature)              -- Adiciona criatura
g_map.removeCreature(creature)           -- Remove criatura

-- Path finding
local path = g_map.findPath(fromPos, toPos, maxDistance)
local reachable = g_map.canReach(fromPos, toPos, maxDistance)

-- Informações de tile
if tile then
    local walkable = tile:isWalkable()   -- Verificar se é caminhável
    local ground = tile:getGround()      -- Item do chão
    local items = tile:getItems()        -- Itens no tile
    local creature = tile:getTopCreature() -- Criatura no topo
    local moveThing = tile:getTopMoveThing() -- Coisa movível no topo
    
    -- Verificações
    local hasCreature = tile:hasCreature() -- Tem criatura
    local isEmpty = tile:isEmpty()        -- Está vazio
    local isBlocking = tile:isBlocking()  -- Está bloqueando
end

-- Eventos do mapa
connect(g_map, {
    onTileUpdate = function(tile)
        print("Tile atualizado: " .. tile:getPosition().x .. "," .. tile:getPosition().y)
    end
})
```

#### Nível Advanced
```lua
-- Informações do mapa
local centerPos = g_map.getCentralPosition() -- Posição central
g_map.setCentralPosition(position)       -- Define posição central
local cameraPos = g_map.getCameraPosition() -- Posição da câmera

-- Tiles
local tile = g_map.getTile(position)     -- Obtém tile na posição
local tiles = g_map.getTiles(fromPos, toPos) -- Tiles em área
g_map.cleanTile(position)                -- Limpa tile

-- Criaturas
local creatures = g_map.getCreatures()   -- Todas as criaturas
local spectators = g_map.getSpectators(centerPos, multifloor, xRange, yRange)
g_map.addCreature(creature)              -- Adiciona criatura
g_map.removeCreature(creature)           -- Remove criatura

-- Path finding
local path = g_map.findPath(fromPos, toPos, maxDistance)
local reachable = g_map.canReach(fromPos, toPos, maxDistance)

-- Informações de tile
if tile then
    local walkable = tile:isWalkable()   -- Verificar se é caminhável
    local ground = tile:getGround()      -- Item do chão
    local items = tile:getItems()        -- Itens no tile
    local creature = tile:getTopCreature() -- Criatura no topo
    local moveThing = tile:getTopMoveThing() -- Coisa movível no topo
    
    -- Verificações
    local hasCreature = tile:hasCreature() -- Tem criatura
    local isEmpty = tile:isEmpty()        -- Está vazio
    local isBlocking = tile:isBlocking()  -- Está bloqueando
end

-- Eventos do mapa
connect(g_map, {
    onTileUpdate = function(tile)
        print("Tile atualizado: " .. tile:getPosition().x .. "," .. tile:getPosition().y)
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

### Creature

**Descrição**: Entidades do jogo (jogadores, NPCs, monstros).

#### Nível Basic
```lua
local creature = g_game.getLocalPlayer() -- Exemplo: jogador local
-- Informações básicas
local id = creature:getId()              -- ID único da criatura
local name = creature:getName()          -- Nome
local pos = creature:getPosition()       -- Posição atual
local direction = creature:getDirection() -- Direção que está olhando
-- Estados
local health = creature:getHealth()      -- HP atual
local maxHealth = creature:getMaxHealth() -- HP máximo
local healthPercent = creature:getHealthPercent() -- Percentual de HP
local mana = creature:getMana()          -- Mana atual (se jogador)
local maxMana = creature:getMaxMana()    -- Mana máxima
-- Visual
local outfit = creature:getOutfit()      -- Outfit atual
local light = creature:getLight()        -- Luz da criatura
local speed = creature:getSpeed()        -- Velocidade
local skull = creature:getSkull()        -- Skull (PK)
local shield = creature:getShield()      -- Shield (guild)
local emblem = creature:getEmblem()      -- Emblem (guild)
-- Verificações de tipo
local isPlayer = creature:isPlayer()     -- É jogador
local isNpc = creature:isNpc()           -- É NPC  
local isMonster = creature:isMonster()   -- É monstro
local isLocalPlayer = creature:isLocalPlayer() -- É o jogador local
-- Estados especiais
local dead = creature:isDead()           -- Está morto
local walking = creature:isWalking()     -- Está andando
local invisible = creature:isInvisible() -- Está invisível
-- Tile relacionado
local tile = creature:getTile()          -- Tile onde está
-- Para jogadores específicos
if creature:isPlayer() then
    local vocation = creature:getVocation() -- Vocação
    local level = creature:getLevel()     -- Nível
    local experience = creature:getExperience() -- Experiência
    local soul = creature:getSoul()       -- Soul points
    local capacity = creature:getCapacity() -- Capacidade
    local freeCapacity = creature:getFreeCapacity() -- Capacidade livre
    -- Skills
    local skillLevel = creature:getSkillLevel(Otc.Skill.Fist) -- Nível de skill
    local skillPercent = creature:getSkillLevelPercent(Otc.Skill.Fist) -- %
    -- Estados
    local stamina = creature:getStamina()  -- Stamina
    local food = creature:getFood()        -- Food time
    local blessings = creature:getBlessings() -- Blessings count
end
```

#### Nível Intermediate
```lua
local creature = g_game.getLocalPlayer() -- Exemplo: jogador local

-- Informações básicas
local id = creature:getId()              -- ID único da criatura
local name = creature:getName()          -- Nome
local pos = creature:getPosition()       -- Posição atual
local direction = creature:getDirection() -- Direção que está olhando

-- Estados
local health = creature:getHealth()      -- HP atual
local maxHealth = creature:getMaxHealth() -- HP máximo
local healthPercent = creature:getHealthPercent() -- Percentual de HP
local mana = creature:getMana()          -- Mana atual (se jogador)
local maxMana = creature:getMaxMana()    -- Mana máxima

-- Visual
local outfit = creature:getOutfit()      -- Outfit atual
creature:setOutfit(outfit)               -- Define outfit
local light = creature:getLight()        -- Luz da criatura
local speed = creature:getSpeed()        -- Velocidade
local skull = creature:getSkull()        -- Skull (PK)
local shield = creature:getShield()      -- Shield (guild)
local emblem = creature:getEmblem()      -- Emblem (guild)

-- Verificações de tipo
local isPlayer = creature:isPlayer()     -- É jogador
local isNpc = creature:isNpc()           -- É NPC  
local isMonster = creature:isMonster()   -- É monstro
local isLocalPlayer = creature:isLocalPlayer() -- É o jogador local

-- Estados especiais
local dead = creature:isDead()           -- Está morto
local walking = creature:isWalking()     -- Está andando
local invisible = creature:isInvisible() -- Está invisível

-- Tile relacionado
local tile = creature:getTile()          -- Tile onde está
creature:setPosition(newPosition)        -- Define nova posição

-- Para jogadores específicos
if creature:isPlayer() then
    local vocation = creature:getVocation() -- Vocação
    local level = creature:getLevel()     -- Nível
    local experience = creature:getExperience() -- Experiência
    local soul = creature:getSoul()       -- Soul points
    local capacity = creature:getCapacity() -- Capacidade
    local freeCapacity = creature:getFreeCapacity() -- Capacidade livre
    
    -- Skills
    local skillLevel = creature:getSkillLevel(Otc.Skill.Fist) -- Nível de skill
    local skillPercent = creature:getSkillLevelPercent(Otc.Skill.Fist) -- %
    
    -- Estados
    local stamina = creature:getStamina()  -- Stamina
    local food = creature:getFood()        -- Food time
    local blessings = creature:getBlessings() -- Blessings count
end
```

#### Nível Advanced
```lua
local creature = g_game.getLocalPlayer() -- Exemplo: jogador local

-- Informações básicas
local id = creature:getId()              -- ID único da criatura
local name = creature:getName()          -- Nome
local pos = creature:getPosition()       -- Posição atual
local direction = creature:getDirection() -- Direção que está olhando

-- Estados
local health = creature:getHealth()      -- HP atual
local maxHealth = creature:getMaxHealth() -- HP máximo
local healthPercent = creature:getHealthPercent() -- Percentual de HP
local mana = creature:getMana()          -- Mana atual (se jogador)
local maxMana = creature:getMaxMana()    -- Mana máxima

-- Visual
local outfit = creature:getOutfit()      -- Outfit atual
creature:setOutfit(outfit)               -- Define outfit
local light = creature:getLight()        -- Luz da criatura
local speed = creature:getSpeed()        -- Velocidade
local skull = creature:getSkull()        -- Skull (PK)
local shield = creature:getShield()      -- Shield (guild)
local emblem = creature:getEmblem()      -- Emblem (guild)

-- Verificações de tipo
local isPlayer = creature:isPlayer()     -- É jogador
local isNpc = creature:isNpc()           -- É NPC  
local isMonster = creature:isMonster()   -- É monstro
local isLocalPlayer = creature:isLocalPlayer() -- É o jogador local

-- Estados especiais
local dead = creature:isDead()           -- Está morto
local walking = creature:isWalking()     -- Está andando
local invisible = creature:isInvisible() -- Está invisível

-- Tile relacionado
local tile = creature:getTile()          -- Tile onde está
creature:setPosition(newPosition)        -- Define nova posição

-- Para jogadores específicos
if creature:isPlayer() then
    local vocation = creature:getVocation() -- Vocação
    local level = creature:getLevel()     -- Nível
    local experience = creature:getExperience() -- Experiência
    local soul = creature:getSoul()       -- Soul points
    local capacity = creature:getCapacity() -- Capacidade
    local freeCapacity = creature:getFreeCapacity() -- Capacidade livre
    
    -- Skills
    local skillLevel = creature:getSkillLevel(Otc.Skill.Fist) -- Nível de skill
    local skillPercent = creature:getSkillLevelPercent(Otc.Skill.Fist) -- %
    
    -- Estados
    local stamina = creature:getStamina()  -- Stamina
    local food = creature:getFood()        -- Food time
    local blessings = creature:getBlessings() -- Blessings count
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

### Item

**Descrição**: Itens do jogo.

#### Nível Basic
```lua
local item = Item.create(2160) -- Cria item (gold coin)
-- Informações básicas
local id = item:getId()                  -- ID do item
local count = item:getCount()            -- Quantidade
local subType = item:getSubType()        -- Subtipo
local description = item:getDescription() -- Descrição
-- Propriedades
local stackable = item:isStackable()     -- É empilhável
local moveable = item:isMoveable()       -- É movível
local pickupable = item:isPickupable()   -- Pode ser pego
local rotatable = item:isRotatable()     -- Pode ser rotacionado
local readable = item:isReadable()       -- Pode ser lido
local writable = item:isWritable()       -- Pode ser escrito
-- Propriedades especiais
local multiUse = item:isMultiUse()       -- Uso múltiplo
local fluidContainer = item:isFluidContainer() -- Container de fluido
local container = item:isContainer()     -- É container
local weapon = item:isWeapon()           -- É arma
local ammo = item:isAmmo()               -- É munição
local armor = item:isArmor()             -- É armadura
local charged = item:isCharged()         -- Tem cargas
-- Container específico
if item:isContainer() then
    local capacity = item:getCapacity()  -- Capacidade
    local size = item:getSize()          -- Itens dentro
    local items = item:getItems()        -- Lista de itens
    local hasParent = item:hasParent()   -- Tem container pai
end
-- Posição e localização
local pos = item:getPosition()           -- Posição no mapa
local tile = item:getTile()              -- Tile onde está
local container = item:getContainer()    -- Container onde está
-- Texto (para itens com texto)
local text = item:getText()              -- Texto do item
-- Eventos
    onPositionChange = function(item, newPos, oldPos)
        print("Item movido para: " .. newPos.x .. "," .. newPos.y .. "," .. newPos.z)
    end
```

#### Nível Intermediate
```lua
local item = Item.create(2160) -- Cria item (gold coin)

-- Informações básicas
local id = item:getId()                  -- ID do item
local count = item:getCount()            -- Quantidade
item:setCount(100)                       -- Define quantidade
local subType = item:getSubType()        -- Subtipo
local description = item:getDescription() -- Descrição

-- Propriedades
local stackable = item:isStackable()     -- É empilhável
local moveable = item:isMoveable()       -- É movível
local pickupable = item:isPickupable()   -- Pode ser pego
local rotatable = item:isRotatable()     -- Pode ser rotacionado
local readable = item:isReadable()       -- Pode ser lido
local writable = item:isWritable()       -- Pode ser escrito

-- Propriedades especiais
local multiUse = item:isMultiUse()       -- Uso múltiplo
local fluidContainer = item:isFluidContainer() -- Container de fluido
local container = item:isContainer()     -- É container
local weapon = item:isWeapon()           -- É arma
local ammo = item:isAmmo()               -- É munição
local armor = item:isArmor()             -- É armadura
local charged = item:isCharged()         -- Tem cargas

-- Container específico
if item:isContainer() then
    local capacity = item:getCapacity()  -- Capacidade
    local size = item:getSize()          -- Itens dentro
    local items = item:getItems()        -- Lista de itens
    local hasParent = item:hasParent()   -- Tem container pai
end

-- Posição e localização
local pos = item:getPosition()           -- Posição no mapa
local tile = item:getTile()              -- Tile onde está
local container = item:getContainer()    -- Container onde está

-- Texto (para itens com texto)
local text = item:getText()              -- Texto do item
item:setText("Novo texto")               -- Define texto

-- Eventos
connect(item, {
    onPositionChange = function(item, newPos, oldPos)
        print("Item movido para: " .. newPos.x .. "," .. newPos.y .. "," .. newPos.z)
    end
})
```

#### Nível Advanced
```lua
local item = Item.create(2160) -- Cria item (gold coin)

-- Informações básicas
local id = item:getId()                  -- ID do item
local count = item:getCount()            -- Quantidade
item:setCount(100)                       -- Define quantidade
local subType = item:getSubType()        -- Subtipo
local description = item:getDescription() -- Descrição

-- Propriedades
local stackable = item:isStackable()     -- É empilhável
local moveable = item:isMoveable()       -- É movível
local pickupable = item:isPickupable()   -- Pode ser pego
local rotatable = item:isRotatable()     -- Pode ser rotacionado
local readable = item:isReadable()       -- Pode ser lido
local writable = item:isWritable()       -- Pode ser escrito

-- Propriedades especiais
local multiUse = item:isMultiUse()       -- Uso múltiplo
local fluidContainer = item:isFluidContainer() -- Container de fluido
local container = item:isContainer()     -- É container
local weapon = item:isWeapon()           -- É arma
local ammo = item:isAmmo()               -- É munição
local armor = item:isArmor()             -- É armadura
local charged = item:isCharged()         -- Tem cargas

-- Container específico
if item:isContainer() then
    local capacity = item:getCapacity()  -- Capacidade
    local size = item:getSize()          -- Itens dentro
    local items = item:getItems()        -- Lista de itens
    local hasParent = item:hasParent()   -- Tem container pai
end

-- Posição e localização
local pos = item:getPosition()           -- Posição no mapa
local tile = item:getTile()              -- Tile onde está
local container = item:getContainer()    -- Container onde está

-- Texto (para itens com texto)
local text = item:getText()              -- Texto do item
item:setText("Novo texto")               -- Define texto

-- Eventos
connect(item, {
    onPositionChange = function(item, newPos, oldPos)
        print("Item movido para: " .. newPos.x .. "," .. newPos.y .. "," .. newPos.z)
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

## 🌐 Sistema de Rede

### g_game (Network functions)

**Descrição**: Funções de rede do jogo.

#### Nível Basic
```lua
-- Conexão
-- Informações da conexão
local host = g_game.getWorldHost()       -- Host do mundo
local port = g_game.getWorldPort()       -- Porta do mundo
local ping = g_game.getPing()            -- Ping atual
-- Configurações de protocolo
-- Pacotes customizados
g_game.sendExtendedOpcode(opcode, buffer) -- Envia opcode estendido
-- Callbacks de rede
    onPingUpdate = function(ping)
        print("Ping atualizado: " .. ping .. "ms")
    end,
    onConnectionError = function(message, code)
        print("Erro de conexão: " .. message)
    end,
    onProtocolError = function(message, code)
        print("Erro de protocolo: " .. message)
    end
```

#### Nível Intermediate
```lua
-- Conexão
g_game.loginWorld("account", "password", "world", "127.0.0.1", 7171, "character")
g_game.cancelLogin()                     -- Cancela login
g_game.forceLogout()                     -- Força logout
g_game.safeLogout()                      -- Logout seguro

-- Informações da conexão
local host = g_game.getWorldHost()       -- Host do mundo
local port = g_game.getWorldPort()       -- Porta do mundo
local ping = g_game.getPing()            -- Ping atual

-- Configurações de protocolo
g_game.setProtocolVersion(1412)          -- Versão do protocolo
g_game.setClientVersion(1412)            -- Versão do cliente
g_game.enableFeature(GameFeature.Feature) -- Habilita feature

-- Pacotes customizados
g_game.sendExtendedOpcode(opcode, buffer) -- Envia opcode estendido

-- Callbacks de rede
connect(g_game, {
    onPingUpdate = function(ping)
        print("Ping atualizado: " .. ping .. "ms")
    end,
    onConnectionError = function(message, code)
        print("Erro de conexão: " .. message)
    end,
    onProtocolError = function(message, code)
        print("Erro de protocolo: " .. message)
    end
})
```

#### Nível Advanced
```lua
-- Conexão
g_game.loginWorld("account", "password", "world", "127.0.0.1", 7171, "character")
g_game.cancelLogin()                     -- Cancela login
g_game.forceLogout()                     -- Força logout
g_game.safeLogout()                      -- Logout seguro

-- Informações da conexão
local host = g_game.getWorldHost()       -- Host do mundo
local port = g_game.getWorldPort()       -- Porta do mundo
local ping = g_game.getPing()            -- Ping atual

-- Configurações de protocolo
g_game.setProtocolVersion(1412)          -- Versão do protocolo
g_game.setClientVersion(1412)            -- Versão do cliente
g_game.enableFeature(GameFeature.Feature) -- Habilita feature

-- Pacotes customizados
g_game.sendExtendedOpcode(opcode, buffer) -- Envia opcode estendido

-- Callbacks de rede
connect(g_game, {
    onPingUpdate = function(ping)
        print("Ping atualizado: " .. ping .. "ms")
    end,
    onConnectionError = function(message, code)
        print("Erro de conexão: " .. message)
    end,
    onProtocolError = function(message, code)
        print("Erro de protocolo: " .. message)
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

### HTTP Requests

**Descrição**: Requisições HTTP (se módulo HTTP estiver disponível).

#### Nível Basic
```lua
-- Requisição GET simples
HTTP.get("http://api.exemplo.com/data", function(data, err)
    if err then
        print("Erro: " .. err)
        return
    end
    print("Dados recebidos: " .. data)
end)

-- Requisição POST
HTTP.post("http://api.exemplo.com/submit", {
    name = "João",
    level = 50
}, function(response, err)
    if not err then
        print("Resposta: " .. response)
    end
end)

-- Requisição com headers customizados
HTTP.request({
    url = "http://api.exemplo.com/protected",
    method = "GET",
    headers = {
        ["Authorization"] = "Bearer token123",
        ["Content-Type"] = "application/json"
    }
}, function(response, err)
    -- Processar resposta
end)
```

#### Nível Intermediate
```lua
-- Requisição GET simples
HTTP.get("http://api.exemplo.com/data", function(data, err)
    if err then
        print("Erro: " .. err)
        return
    end
    print("Dados recebidos: " .. data)
end)

-- Requisição POST
HTTP.post("http://api.exemplo.com/submit", {
    name = "João",
    level = 50
}, function(response, err)
    if not err then
        print("Resposta: " .. response)
    end
end)

-- Requisição com headers customizados
HTTP.request({
    url = "http://api.exemplo.com/protected",
    method = "GET",
    headers = {
        ["Authorization"] = "Bearer token123",
        ["Content-Type"] = "application/json"
    }
}, function(response, err)
    -- Processar resposta
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
-- Requisição GET simples
HTTP.get("http://api.exemplo.com/data", function(data, err)
    if err then
        print("Erro: " .. err)
        return
    end
    print("Dados recebidos: " .. data)
end)

-- Requisição POST
HTTP.post("http://api.exemplo.com/submit", {
    name = "João",
    level = 50
}, function(response, err)
    if not err then
        print("Resposta: " .. response)
    end
end)

-- Requisição com headers customizados
HTTP.request({
    url = "http://api.exemplo.com/protected",
    method = "GET",
    headers = {
        ["Authorization"] = "Bearer token123",
        ["Content-Type"] = "application/json"
    }
}, function(response, err)
    -- Processar resposta
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

## 🎨 Sistema de Gráficos

### g_graphics (Graphics)

**Descrição**: Controle de gráficos e renderização.

#### Nível Basic
```lua
-- Informações gráficas
local vendor = g_graphics.getVendor()    -- Fabricante da GPU
local renderer = g_graphics.getRenderer() -- Renderizador
local version = g_graphics.getVersion()  -- Versão OpenGL
-- Configurações
local vsync = g_graphics.isVSyncEnabled() -- Verifica VSync
-- Resolução
local size = g_graphics.getViewportSize() -- Tamanho da viewport
-- Screenshots
-- Performance
local fps = g_graphics.getAverageFPS()   -- FPS médio
local maxFps = g_graphics.getMaxFPS()    -- FPS máximo
```

#### Nível Intermediate
```lua
-- Informações gráficas
local vendor = g_graphics.getVendor()    -- Fabricante da GPU
local renderer = g_graphics.getRenderer() -- Renderizador
local version = g_graphics.getVersion()  -- Versão OpenGL

-- Configurações
g_graphics.setVSync(true)                -- Ativa VSync
local vsync = g_graphics.isVSyncEnabled() -- Verifica VSync

-- Resolução
local size = g_graphics.getViewportSize() -- Tamanho da viewport
g_graphics.resize(1920, 1080)            -- Redimensiona

-- Screenshots
g_graphics.screenshot("screenshot.png")   -- Captura tela

-- Performance
local fps = g_graphics.getAverageFPS()   -- FPS médio
local maxFps = g_graphics.getMaxFPS()    -- FPS máximo
g_graphics.setMaxFPS(60)                 -- Define FPS máximo
```

#### Nível Advanced
```lua
-- Informações gráficas
local vendor = g_graphics.getVendor()    -- Fabricante da GPU
local renderer = g_graphics.getRenderer() -- Renderizador
local version = g_graphics.getVersion()  -- Versão OpenGL

-- Configurações
g_graphics.setVSync(true)                -- Ativa VSync
local vsync = g_graphics.isVSyncEnabled() -- Verifica VSync

-- Resolução
local size = g_graphics.getViewportSize() -- Tamanho da viewport
g_graphics.resize(1920, 1080)            -- Redimensiona

-- Screenshots
g_graphics.screenshot("screenshot.png")   -- Captura tela

-- Performance
local fps = g_graphics.getAverageFPS()   -- FPS médio
local maxFps = g_graphics.getMaxFPS()    -- FPS máximo
g_graphics.setMaxFPS(60)                 -- Define FPS máximo
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

### g_shaders (Shaders)

**Descrição**: Sistema de shaders (se disponível).

```lua
-- Carregamento de shaders
    --  Carregamento de shaders (traduzido)
local shader = g_shaders.createShader("vertex.glsl", "fragment.glsl")
g_shaders.setShader(shader)              -- Ativa shader
g_shaders.clearShader()                  -- Remove shader ativo

-- Uniforms
    --  Uniforms (traduzido)
g_shaders.setUniform("time", g_clock.seconds())
g_shaders.setUniform("resolution", {1920, 1080})
g_shaders.setUniform("color", {1.0, 0.0, 0.0, 1.0})

-- Texturas
    --  Texturas (traduzido)
g_shaders.bindTexture(texture, 0)        -- Bind texture na unidade 0
```

## 🔊 Sistema de Som

### g_sounds (Sounds)

**Descrição**: Sistema de áudio e sons.

#### Nível Basic
```lua
-- Configurações gerais
local enabled = g_sounds.isAudioEnabled() -- Verifica se habilitado
-- Volume
local volume = g_sounds.getMasterVolume() -- Obtém volume master
-- Canais de volume
-- Reprodução de sons
local soundId = g_sounds.playSoundFile("sound.ogg") -- Reproduz arquivo
-- Sons com configurações
local soundId = g_sounds.playSoundFile("music.ogg", {
-- Efeitos sonoros simples
-- Informações
local playing = g_sounds.isSoundPlaying(soundId) -- Verifica se tocando
local duration = g_sounds.getSoundDuration(soundId) -- Duração do som
```

#### Nível Intermediate
```lua
-- Configurações gerais
g_sounds.setAudioEnabled(true)           -- Habilita áudio
local enabled = g_sounds.isAudioEnabled() -- Verifica se habilitado

-- Volume
g_sounds.setMasterVolume(0.8)            -- Volume master (0.0 - 1.0)
local volume = g_sounds.getMasterVolume() -- Obtém volume master

-- Canais de volume
g_sounds.setChannelVolume(SoundChannel.Music, 0.7)    -- Volume música
g_sounds.setChannelVolume(SoundChannel.Effects, 0.9)  -- Volume efeitos

-- Reprodução de sons
local soundId = g_sounds.playSoundFile("sound.ogg") -- Reproduz arquivo
g_sounds.stopSound(soundId)              -- Para som específico
g_sounds.stopAll()                       -- Para todos os sons

-- Sons com configurações
local soundId = g_sounds.playSoundFile("music.ogg", {
    volume = 0.5,
    loop = true,
    channel = SoundChannel.Music
})

-- Efeitos sonoros simples
g_sounds.playEffect("click.wav")         -- Efeito simples
g_sounds.playMusic("background.ogg", true) -- Música em loop

-- Informações
local playing = g_sounds.isSoundPlaying(soundId) -- Verifica se tocando
local duration = g_sounds.getSoundDuration(soundId) -- Duração do som
```

#### Nível Advanced
```lua
-- Configurações gerais
g_sounds.setAudioEnabled(true)           -- Habilita áudio
local enabled = g_sounds.isAudioEnabled() -- Verifica se habilitado

-- Volume
g_sounds.setMasterVolume(0.8)            -- Volume master (0.0 - 1.0)
local volume = g_sounds.getMasterVolume() -- Obtém volume master

-- Canais de volume
g_sounds.setChannelVolume(SoundChannel.Music, 0.7)    -- Volume música
g_sounds.setChannelVolume(SoundChannel.Effects, 0.9)  -- Volume efeitos

-- Reprodução de sons
local soundId = g_sounds.playSoundFile("sound.ogg") -- Reproduz arquivo
g_sounds.stopSound(soundId)              -- Para som específico
g_sounds.stopAll()                       -- Para todos os sons

-- Sons com configurações
local soundId = g_sounds.playSoundFile("music.ogg", {
    volume = 0.5,
    loop = true,
    channel = SoundChannel.Music
})

-- Efeitos sonoros simples
g_sounds.playEffect("click.wav")         -- Efeito simples
g_sounds.playMusic("background.ogg", true) -- Música em loop

-- Informações
local playing = g_sounds.isSoundPlaying(soundId) -- Verifica se tocando
local duration = g_sounds.getSoundDuration(soundId) -- Duração do som
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

## ⚙️ Sistema de Configuração

### g_settings (Settings)

**Descrição**: Configurações persistentes da aplicação.

#### Nível Basic
```lua
-- Configurações simples
g_settings.set("graphics.fullscreen", true) -- Define configuração
local fullscreen = g_settings.getBoolean("graphics.fullscreen", false) -- Obtém boolean
local volume = g_settings.getNumber("audio.volume", 1.0) -- Obtém número
local username = g_settings.getString("login.username", "") -- Obtém string

-- Configurações de lista
g_settings.setList("hotkeys.f1", {"exura", "auto"}) -- Define lista
local hotkey = g_settings.getList("hotkeys.f1") -- Obtém lista

-- Nós complexos
g_settings.setNode("ui.windows", {
    inventory = {x = 100, y = 50, visible = true},
    minimap = {x = 200, y = 100, visible = false}
})
local windows = g_settings.getNode("ui.windows") -- Obtém nó completo

-- Operações de arquivo
g_settings.save()                        -- Salva configurações
g_settings.load()                        -- Recarrega configurações
g_settings.clear()                       -- Limpa todas as configurações

-- Eventos
connect(g_settings, {
    onSettingChange = function(key, value)
        print("Configuração alterada: " .. key .. " = " .. tostring(value))
    end
})
```

#### Nível Intermediate
```lua
-- Configurações simples
g_settings.set("graphics.fullscreen", true) -- Define configuração
local fullscreen = g_settings.getBoolean("graphics.fullscreen", false) -- Obtém boolean
local volume = g_settings.getNumber("audio.volume", 1.0) -- Obtém número
local username = g_settings.getString("login.username", "") -- Obtém string

-- Configurações de lista
g_settings.setList("hotkeys.f1", {"exura", "auto"}) -- Define lista
local hotkey = g_settings.getList("hotkeys.f1") -- Obtém lista

-- Nós complexos
g_settings.setNode("ui.windows", {
    inventory = {x = 100, y = 50, visible = true},
    minimap = {x = 200, y = 100, visible = false}
})
local windows = g_settings.getNode("ui.windows") -- Obtém nó completo

-- Operações de arquivo
g_settings.save()                        -- Salva configurações
g_settings.load()                        -- Recarrega configurações
g_settings.clear()                       -- Limpa todas as configurações

-- Eventos
connect(g_settings, {
    onSettingChange = function(key, value)
        print("Configuração alterada: " .. key .. " = " .. tostring(value))
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
-- Configurações simples
g_settings.set("graphics.fullscreen", true) -- Define configuração
local fullscreen = g_settings.getBoolean("graphics.fullscreen", false) -- Obtém boolean
local volume = g_settings.getNumber("audio.volume", 1.0) -- Obtém número
local username = g_settings.getString("login.username", "") -- Obtém string

-- Configurações de lista
g_settings.setList("hotkeys.f1", {"exura", "auto"}) -- Define lista
local hotkey = g_settings.getList("hotkeys.f1") -- Obtém lista

-- Nós complexos
g_settings.setNode("ui.windows", {
    inventory = {x = 100, y = 50, visible = true},
    minimap = {x = 200, y = 100, visible = false}
})
local windows = g_settings.getNode("ui.windows") -- Obtém nó completo

-- Operações de arquivo
g_settings.save()                        -- Salva configurações
g_settings.load()                        -- Recarrega configurações
g_settings.clear()                       -- Limpa todas as configurações

-- Eventos
connect(g_settings, {
    onSettingChange = function(key, value)
        print("Configuração alterada: " .. key .. " = " .. tostring(value))
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

### g_configs (Configs)

**Descrição**: Configurações específicas do jogo.

#### Nível Basic
```lua
-- Carregamento
g_configs.loadSettings("/config.otml")   -- Carrega configurações

-- Acesso a configurações
local autoChase = g_configs.getBoolean("autoChase", false)
local moveSpeed = g_configs.getNumber("moveSpeed", 1000)
local serverList = g_configs.getList("servers")

-- Configurações de jogo
g_configs.set("game.autoLogin", true)
g_configs.set("game.defaultServer", "localhost")
g_configs.set("game.rememberPassword", false)

-- Salvar
g_configs.save()                         -- Salva configurações
```

#### Nível Intermediate
```lua
-- Carregamento
g_configs.loadSettings("/config.otml")   -- Carrega configurações

-- Acesso a configurações
local autoChase = g_configs.getBoolean("autoChase", false)
local moveSpeed = g_configs.getNumber("moveSpeed", 1000)
local serverList = g_configs.getList("servers")

-- Configurações de jogo
g_configs.set("game.autoLogin", true)
g_configs.set("game.defaultServer", "localhost")
g_configs.set("game.rememberPassword", false)

-- Salvar
g_configs.save()                         -- Salva configurações
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
-- Carregamento
g_configs.loadSettings("/config.otml")   -- Carrega configurações

-- Acesso a configurações
local autoChase = g_configs.getBoolean("autoChase", false)
local moveSpeed = g_configs.getNumber("moveSpeed", 1000)
local serverList = g_configs.getList("servers")

-- Configurações de jogo
g_configs.set("game.autoLogin", true)
g_configs.set("game.defaultServer", "localhost")
g_configs.set("game.rememberPassword", false)

-- Salvar
g_configs.save()                         -- Salva configurações
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

## 🛠️ Utilitários

### g_keyboard (Keyboard)

**Descrição**: Gerenciamento de teclado e teclas.

#### Nível Basic
```lua
-- Bind de teclas
g_keyboard.bindKeyDown("Ctrl+S", function()
    print("Ctrl+S pressionado!")
end)

g_keyboard.bindKeyPress("F1", function()
    print("F1 pressionado!")
end, widget)  -- Bind específico para widget

g_keyboard.bindKeyUp("Space", function()
    print("Space liberado!")
end)

-- Unbind
g_keyboard.unbindKeyDown("Ctrl+S")       -- Remove bind específico
g_keyboard.clearKeyboardBindings()       -- Remove todos os binds

-- Estado das teclas
local ctrlPressed = g_keyboard.isCtrlPressed() -- Ctrl pressionado
local shiftPressed = g_keyboard.isShiftPressed() -- Shift pressionado
local altPressed = g_keyboard.isAltPressed() -- Alt pressionado

-- Modificadores
local modifiers = g_keyboard.getModifiers() -- Todos os modificadores

-- Conversão de teclas
local keyText = g_keyboard.getKeyText(KeyCode.F1) -- "F1"
local keyCode = g_keyboard.getKeyCode("F1")   -- KeyCode.F1
```

#### Nível Intermediate
```lua
-- Bind de teclas
g_keyboard.bindKeyDown("Ctrl+S", function()
    print("Ctrl+S pressionado!")
end)

g_keyboard.bindKeyPress("F1", function()
    print("F1 pressionado!")
end, widget)  -- Bind específico para widget

g_keyboard.bindKeyUp("Space", function()
    print("Space liberado!")
end)

-- Unbind
g_keyboard.unbindKeyDown("Ctrl+S")       -- Remove bind específico
g_keyboard.clearKeyboardBindings()       -- Remove todos os binds

-- Estado das teclas
local ctrlPressed = g_keyboard.isCtrlPressed() -- Ctrl pressionado
local shiftPressed = g_keyboard.isShiftPressed() -- Shift pressionado
local altPressed = g_keyboard.isAltPressed() -- Alt pressionado

-- Modificadores
local modifiers = g_keyboard.getModifiers() -- Todos os modificadores

-- Conversão de teclas
local keyText = g_keyboard.getKeyText(KeyCode.F1) -- "F1"
local keyCode = g_keyboard.getKeyCode("F1")   -- KeyCode.F1
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
-- Bind de teclas
g_keyboard.bindKeyDown("Ctrl+S", function()
    print("Ctrl+S pressionado!")
end)

g_keyboard.bindKeyPress("F1", function()
    print("F1 pressionado!")
end, widget)  -- Bind específico para widget

g_keyboard.bindKeyUp("Space", function()
    print("Space liberado!")
end)

-- Unbind
g_keyboard.unbindKeyDown("Ctrl+S")       -- Remove bind específico
g_keyboard.clearKeyboardBindings()       -- Remove todos os binds

-- Estado das teclas
local ctrlPressed = g_keyboard.isCtrlPressed() -- Ctrl pressionado
local shiftPressed = g_keyboard.isShiftPressed() -- Shift pressionado
local altPressed = g_keyboard.isAltPressed() -- Alt pressionado

-- Modificadores
local modifiers = g_keyboard.getModifiers() -- Todos os modificadores

-- Conversão de teclas
local keyText = g_keyboard.getKeyText(KeyCode.F1) -- "F1"
local keyCode = g_keyboard.getKeyCode("F1")   -- KeyCode.F1
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

### g_mouse (Mouse)

**Descrição**: Gerenciamento do mouse.

#### Nível Basic
```lua
-- Posição
local pos = g_mouse.getPosition()        -- Posição atual
g_mouse.setPosition(100, 200)            -- Define posição

-- Cursor
g_mouse.pushCursor("target")             -- Empilha cursor
g_mouse.popCursor()                      -- Remove cursor do topo
g_mouse.setCursor("hand")                -- Define cursor direto

-- Estados
local leftPressed = g_mouse.isPressed(MouseLeftButton)   -- Botão esquerdo
local rightPressed = g_mouse.isPressed(MouseRightButton) -- Botão direito
local middlePressed = g_mouse.isPressed(MouseMiddleButton) -- Botão do meio

-- Bind de eventos globais
g_mouse.bindMousePress(MouseLeftButton, function(mousePos)
    print("Clique esquerdo em: " .. mousePos.x .. "," .. mousePos.y)
end)

g_mouse.bindMouseRelease(MouseRightButton, function(mousePos)
    print("Botão direito liberado")
end)

-- Unbind
g_mouse.unbindMousePress(MouseLeftButton)
```

#### Nível Intermediate
```lua
-- Posição
local pos = g_mouse.getPosition()        -- Posição atual
g_mouse.setPosition(100, 200)            -- Define posição

-- Cursor
g_mouse.pushCursor("target")             -- Empilha cursor
g_mouse.popCursor()                      -- Remove cursor do topo
g_mouse.setCursor("hand")                -- Define cursor direto

-- Estados
local leftPressed = g_mouse.isPressed(MouseLeftButton)   -- Botão esquerdo
local rightPressed = g_mouse.isPressed(MouseRightButton) -- Botão direito
local middlePressed = g_mouse.isPressed(MouseMiddleButton) -- Botão do meio

-- Bind de eventos globais
g_mouse.bindMousePress(MouseLeftButton, function(mousePos)
    print("Clique esquerdo em: " .. mousePos.x .. "," .. mousePos.y)
end)

g_mouse.bindMouseRelease(MouseRightButton, function(mousePos)
    print("Botão direito liberado")
end)

-- Unbind
g_mouse.unbindMousePress(MouseLeftButton)
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
-- Posição
local pos = g_mouse.getPosition()        -- Posição atual
g_mouse.setPosition(100, 200)            -- Define posição

-- Cursor
g_mouse.pushCursor("target")             -- Empilha cursor
g_mouse.popCursor()                      -- Remove cursor do topo
g_mouse.setCursor("hand")                -- Define cursor direto

-- Estados
local leftPressed = g_mouse.isPressed(MouseLeftButton)   -- Botão esquerdo
local rightPressed = g_mouse.isPressed(MouseRightButton) -- Botão direito
local middlePressed = g_mouse.isPressed(MouseMiddleButton) -- Botão do meio

-- Bind de eventos globais
g_mouse.bindMousePress(MouseLeftButton, function(mousePos)
    print("Clique esquerdo em: " .. mousePos.x .. "," .. mousePos.y)
end)

g_mouse.bindMouseRelease(MouseRightButton, function(mousePos)
    print("Botão direito liberado")
end)

-- Unbind
g_mouse.unbindMousePress(MouseLeftButton)
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

### g_textures (Textures)

**Descrição**: Gerenciamento de texturas.

#### Nível Basic
```lua
-- Carregamento
local texture = g_textures.getTexture("/images/icon.png") -- Carrega textura
-- Informações
local size = texture:getSize()           -- Tamanho da textura
local width = texture:getWidth()         -- Largura
local height = texture:getHeight()       -- Altura
-- Estados
local loaded = texture:isLoaded()        -- Está carregada
local smooth = texture:isSmooth()        -- Suavização ativa
```

#### Nível Intermediate
```lua
-- Carregamento
local texture = g_textures.getTexture("/images/icon.png") -- Carrega textura
g_textures.preload("/images/")           -- Pré-carrega diretório

-- Informações
local size = texture:getSize()           -- Tamanho da textura
local width = texture:getWidth()         -- Largura
local height = texture:getHeight()       -- Altura

-- Estados
local loaded = texture:isLoaded()        -- Está carregada
local smooth = texture:isSmooth()        -- Suavização ativa
texture:setSmooth(true)                  -- Ativa suavização
```

#### Nível Advanced
```lua
-- Carregamento
local texture = g_textures.getTexture("/images/icon.png") -- Carrega textura
g_textures.preload("/images/")           -- Pré-carrega diretório

-- Informações
local size = texture:getSize()           -- Tamanho da textura
local width = texture:getWidth()         -- Largura
local height = texture:getHeight()       -- Altura

-- Estados
local loaded = texture:isLoaded()        -- Está carregada
local smooth = texture:isSmooth()        -- Suavização ativa
texture:setSmooth(true)                  -- Ativa suavização
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

### g_fonts (Fonts)

**Descrição**: Gerenciamento de fontes.

#### Nível Basic
```lua
-- Carregamento
local font = g_fonts.getFont("verdana-11px-rounded") -- Obtém fonte
-- Informações
local glyphHeight = font:getGlyphHeight() -- Altura dos glyphs
local textSize = font:calculateTextRectSize("Meu texto") -- Tamanho do texto
local spacing = font:getGlyphSpacing()    -- Espaçamento entre glyphs
-- Renderização de texto
font:renderText("Texto", {x = 100, y = 50}, "#FFFFFF") -- Renderiza texto
```

#### Nível Intermediate
```lua
-- Carregamento
local font = g_fonts.getFont("verdana-11px-rounded") -- Obtém fonte
g_fonts.importFont("/fonts/myfont.otfont") -- Importa fonte personalizada

-- Informações
local glyphHeight = font:getGlyphHeight() -- Altura dos glyphs
local textSize = font:calculateTextRectSize("Meu texto") -- Tamanho do texto
local spacing = font:getGlyphSpacing()    -- Espaçamento entre glyphs

-- Renderização de texto
font:renderText("Texto", {x = 100, y = 50}, "#FFFFFF") -- Renderiza texto
```

#### Nível Advanced
```lua
-- Carregamento
local font = g_fonts.getFont("verdana-11px-rounded") -- Obtém fonte
g_fonts.importFont("/fonts/myfont.otfont") -- Importa fonte personalizada

-- Informações
local glyphHeight = font:getGlyphHeight() -- Altura dos glyphs
local textSize = font:calculateTextRectSize("Meu texto") -- Tamanho do texto
local spacing = font:getGlyphSpacing()    -- Espaçamento entre glyphs

-- Renderização de texto
font:renderText("Texto", {x = 100, y = 50}, "#FFFFFF") -- Renderiza texto
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

## 📞 Callbacks e Eventos

### Sistema de Conexão de Eventos

**Descrição**: Como conectar e desconectar eventos.

#### Nível Basic
```lua
-- Conexão básica
connect(g_game, {
    onGameStart = function()
        print("Jogo iniciado!")
    end,
    onGameEnd = function()
        print("Jogo finalizado!")
    end
})

-- Conexão individual
local callback = function(player)
    print("Player criado: " .. player:getName())
end
connect(g_game, "onCreatureAppear", callback)

-- Desconexão
disconnect(g_game, {
    onGameStart = onGameStartCallback,
    onGameEnd = onGameEndCallback
})

-- Desconexão individual
disconnect(g_game, "onCreatureAppear", callback)

-- Eventos únicos (executam apenas uma vez)
connectOnce(g_game, "onGameStart", function()
    print("Primeira vez que o jogo inicia!")
end)
```

#### Nível Intermediate
```lua
-- Conexão básica
connect(g_game, {
    onGameStart = function()
        print("Jogo iniciado!")
    end,
    onGameEnd = function()
        print("Jogo finalizado!")
    end
})

-- Conexão individual
local callback = function(player)
    print("Player criado: " .. player:getName())
end
connect(g_game, "onCreatureAppear", callback)

-- Desconexão
disconnect(g_game, {
    onGameStart = onGameStartCallback,
    onGameEnd = onGameEndCallback
})

-- Desconexão individual
disconnect(g_game, "onCreatureAppear", callback)

-- Eventos únicos (executam apenas uma vez)
connectOnce(g_game, "onGameStart", function()
    print("Primeira vez que o jogo inicia!")
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
-- Conexão básica
connect(g_game, {
    onGameStart = function()
        print("Jogo iniciado!")
    end,
    onGameEnd = function()
        print("Jogo finalizado!")
    end
})

-- Conexão individual
local callback = function(player)
    print("Player criado: " .. player:getName())
end
connect(g_game, "onCreatureAppear", callback)

-- Desconexão
disconnect(g_game, {
    onGameStart = onGameStartCallback,
    onGameEnd = onGameEndCallback
})

-- Desconexão individual
disconnect(g_game, "onCreatureAppear", callback)

-- Eventos únicos (executam apenas uma vez)
connectOnce(g_game, "onGameStart", function()
    print("Primeira vez que o jogo inicia!")
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

### Principais Eventos do Jogo

#### Inicialização e Configuração
```lua
-- Eventos de conexão
connect(g_game, {
    onGameStart = function()
        -- Chamado quando conecta ao jogo
    end,
    onGameEnd = function()
        -- Chamado quando desconecta
    end,
    onLoginError = function(message)
        -- Erro de login
    end,
    onConnectionError = function(message, code)
        -- Erro de conexão
    end
})

-- Eventos de criatura
connect(g_game, {
    onCreatureAppear = function(creature)
        -- Nova criatura apareceu
    end,
```

#### Funcionalidade 1
```lua
    onCreatureDisappear = function(creature)
        -- Criatura desapareceu
    end,
    onCreatureMove = function(creature, oldPos, newPos)
        -- Criatura se moveu
    end,
    onCreatureHealthChange = function(creature, health, maxHealth)
        -- HP da criatura mudou
    end
})

-- Eventos do jogador local
connect(g_game, {
    onLocalPlayerPositionChange = function(newPos, oldPos)
        -- Posição do jogador mudou
    end,
    onLocalPlayerStatsChange = function(localPlayer)
        -- Stats do jogador mudaram (HP, mana, etc)
    end,
    onLocalPlayerSkillChange = function(skillId, level, levelPercent)
        -- Skill do jogador mudou
    end,
```

#### Funcionalidade 2
```lua
    onLocalPlayerVocationChange = function(vocation)
        -- Vocação mudou
    end
})

-- Eventos de mapa
connect(g_map, {
    onTileUpdate = function(tile)
        -- Tile foi atualizado
    end
})

-- Eventos de chat
connect(g_game, {
    onTalk = function(name, level, mode, message, channelId, pos)
        -- Mensagem recebida no chat
    end,
    onChannelList = function(channels)
        -- Lista de canais recebida
    end,
    onOpenChannel = function(channelId, channelName)
        -- Canal aberto
    end
```

#### Funcionalidade 3
```lua
})

-- Eventos de container
connect(g_game, {
    onContainerOpen = function(container, previousContainer)
        -- Container aberto
    end,
    onContainerClose = function(container)
        -- Container fechado
    end,
    onContainerAddItem = function(container, slot, item)
        -- Item adicionado ao container
    end,
    onContainerUpdateItem = function(container, slot, item, oldItem)
        -- Item atualizado no container
    end,
    onContainerRemoveItem = function(container, slot, lastItem)
        -- Item removido do container
    end
})

-- Eventos de trade
connect(g_game, {
    onOpenNpcTrade = function(items)
        -- Trade com NPC aberto
    end,
```

#### Finalização
```lua
    onCloseNpcTrade = function()
        -- Trade com NPC fechado
    end,
    onPlayerTradeRequest = function(traderName, items)
        -- Pedido de trade de jogador
    end,
    onOwnTradeRequest = function(items)
        -- Seu pedido de trade
    end,
    onTradeClose = function()
        -- Trade fechado
    end
})
```

### Eventos de Interface

#### Inicialização e Configuração
```lua
-- Eventos de widget
widget.onClick = function(widget)
    -- Widget clicado
end

widget.onDoubleClick = function(widget)
    -- Widget duplo-clicado
end

widget.onMousePress = function(widget, mousePos, button)
    -- Botão do mouse pressionado
end

widget.onMouseRelease = function(widget, mousePos, button)
    -- Botão do mouse liberado
end

widget.onHoverChange = function(widget, hovered)
    -- Estado de hover mudou
end

widget.onFocusChange = function(widget, focused)
    -- Estado de foco mudou
end
```

#### Funcionalidade 1
```lua

widget.onStyleApply = function(widget, styleName, styleNode)
    -- Estilo aplicado
end

widget.onGeometryChange = function(widget, oldRect, newRect)
    -- Geometria (posição/tamanho) mudou
end

widget.onVisibilityChange = function(widget, visible)
    -- Visibilidade mudou
end

-- Eventos de texto
textEdit.onTextChange = function(textEdit, text, oldText)
    -- Texto mudou
end

textEdit.onEnterPressed = function(textEdit)
    -- Enter pressionado
end
```

#### Finalização
```lua

textEdit.onEscapePressed = function(textEdit)
    -- Escape pressionado
end

-- Eventos de seleção
comboBox.onOptionChange = function(comboBox, optionText, optionData)
    -- Opção do combo box mudou
end

listWidget.onChildFocusChange = function(listWidget, focusedChild)
    -- Item da lista ganhou foco
end
```

## 🎯 Exemplos Práticos

### Exemplo 1: Sistema de Auto-Login

#### Inicialização e Configuração
```lua
-- modules/auto_login/auto_login.lua
autoLogin = {}

function autoLogin.init()
    -- Interface de configuração
    autoLogin.window = g_ui.displayUI('auto_login')
    autoLogin.window:hide()
    
    -- Campos da interface
    autoLogin.accountEdit = autoLogin.window:getChildById('accountEdit')
    autoLogin.passwordEdit = autoLogin.window:getChildById('passwordEdit')
    autoLogin.serverCombo = autoLogin.window:getChildById('serverCombo')
    autoLogin.enabledBox = autoLogin.window:getChildById('enabledBox')
    
    -- Carrega configurações
    autoLogin.loadSettings()
    
    -- Conecta eventos
    connect(g_game, {
        onLoginError = autoLogin.onLoginError,
        onGameStart = autoLogin.onGameStart
    })
```

#### Funcionalidade 1
```lua
    
    -- Menu
    autoLogin.button = modules.client_topmenu.addLeftButton(
        'autoLoginButton', 
        'Auto Login', 
        '/icons/auto_login', 
        autoLogin.toggle
    )
end

function autoLogin.terminate()
    disconnect(g_game, {
        onLoginError = autoLogin.onLoginError,
        onGameStart = autoLogin.onGameStart
    })
    
    autoLogin.saveSettings()
    autoLogin.window:destroy()
    autoLogin.button:destroy()
end

function autoLogin.toggle()
```

#### Funcionalidade 2
```lua
    if autoLogin.window:isVisible() then
        autoLogin.window:hide()
    else
        autoLogin.window:show()
        autoLogin.window:raise()
        autoLogin.accountEdit:focus()
    end
end

function autoLogin.loadSettings()
    local account = g_settings.getString('autoLogin.account', '')
    local password = g_settings.getString('autoLogin.password', '')
    local server = g_settings.getString('autoLogin.server', '')
    local enabled = g_settings.getBoolean('autoLogin.enabled', false)
    
    autoLogin.accountEdit:setText(account)
    autoLogin.passwordEdit:setText(password)
    autoLogin.serverCombo:setCurrentOption(server)
    autoLogin.enabledBox:setChecked(enabled)
end

function autoLogin.saveSettings()
```

#### Funcionalidade 3
```lua
    g_settings.set('autoLogin.account', autoLogin.accountEdit:getText())
    g_settings.set('autoLogin.password', autoLogin.passwordEdit:getText())
    g_settings.set('autoLogin.server', autoLogin.serverCombo:getCurrentOption().text)
    g_settings.set('autoLogin.enabled', autoLogin.enabledBox:isChecked())
    g_settings.save()
end

function autoLogin.performLogin()
    if not autoLogin.enabledBox:isChecked() then
        return
    end
    
    local account = autoLogin.accountEdit:getText()
    local password = autoLogin.passwordEdit:getText()
    local server = autoLogin.serverCombo:getCurrentOption()
    
    if #account > 0 and #password > 0 and server then
        modules.game_login.doLogin(account, password, server.data)
    end
end

function autoLogin.onLoginError(message)
```

#### Finalização
```lua
    print("Auto-login falhou: " .. message)
    -- Tentar novamente em 5 segundos
    scheduleEvent(autoLogin.performLogin, 5000)
end

function autoLogin.onGameStart()
    autoLogin.window:hide()
end
```

### Exemplo 2: Monitor de Status

#### Inicialização e Configuração
```lua
-- modules/status_monitor/status_monitor.lua
statusMonitor = {}

function statusMonitor.init()
    statusMonitor.window = g_ui.createWidget('UIWindow', rootWidget)
    statusMonitor.window:setTitle('Status Monitor')
    statusMonitor.window:setSize({width = 300, height = 200})
    statusMonitor.window:addAnchor(AnchorTop, 'parent', AnchorTop)
    statusMonitor.window:addAnchor(AnchorRight, 'parent', AnchorRight)
    
    -- Labels de status
    statusMonitor.hpLabel = g_ui.createWidget('UILabel', statusMonitor.window)
    statusMonitor.manaLabel = g_ui.createWidget('UILabel', statusMonitor.window)
    statusMonitor.levelLabel = g_ui.createWidget('UILabel', statusMonitor.window)
    statusMonitor.expLabel = g_ui.createWidget('UILabel', statusMonitor.window)
    
    -- Layout vertical
    local layout = g_ui.createWidget('UIVerticalLayout', statusMonitor.window)
    layout:addChild(statusMonitor.hpLabel)
    layout:addChild(statusMonitor.manaLabel)
    layout:addChild(statusMonitor.levelLabel)
    layout:addChild(statusMonitor.expLabel)
    
    -- Eventos
    connect(g_game, {
        onGameStart = statusMonitor.onGameStart,
        onGameEnd = statusMonitor.onGameEnd,
        onLocalPlayerStatsChange = statusMonitor.updateStats
    })
```

#### Funcionalidade 1
```lua
    
    -- Timer para atualização
    statusMonitor.updateEvent = nil
    
    statusMonitor.window:hide()
end

function statusMonitor.onGameStart()
    statusMonitor.window:show()
    statusMonitor.startUpdating()
end

function statusMonitor.onGameEnd()
    statusMonitor.window:hide()
    statusMonitor.stopUpdating()
end

function statusMonitor.startUpdating()
    statusMonitor.updateStats()
    statusMonitor.updateEvent = scheduleEvent(statusMonitor.startUpdating, 1000)
end
```

#### Funcionalidade 2
```lua

function statusMonitor.stopUpdating()
    if statusMonitor.updateEvent then
        removeEvent(statusMonitor.updateEvent)
        statusMonitor.updateEvent = nil
    end
end

function statusMonitor.updateStats()
    local player = g_game.getLocalPlayer()
    if not player then
        return
    end
    
    -- HP
    local hp = player:getHealth()
    local maxHp = player:getMaxHealth()
    local hpPercent = math.floor((hp / maxHp) * 100)
    statusMonitor.hpLabel:setText(string.format("HP: %d/%d (%d%%)", hp, maxHp, hpPercent))
    statusMonitor.hpLabel:setColor(statusMonitor.getHealthColor(hpPercent))
    
    -- Mana
    local mana = player:getMana()
    local maxMana = player:getMaxMana()
    local manaPercent = math.floor((mana / maxMana) * 100)
    statusMonitor.manaLabel:setText(string.format("Mana: %d/%d (%d%%)", mana, maxMana, manaPercent))
    statusMonitor.manaLabel:setColor(statusMonitor.getManaColor(manaPercent))
    
    -- Level
    local level = player:getLevel()
    statusMonitor.levelLabel:setText(string.format("Level: %d", level))
    
    -- Experience
    local exp = player:getExperience()
    statusMonitor.expLabel:setText(string.format("Exp: %s", statusMonitor.formatNumber(exp)))
end
```

#### Funcionalidade 3
```lua

function statusMonitor.getHealthColor(percent)
    if percent >= 80 then
        return "#00FF00"  -- Verde
    elseif percent >= 50 then
        return "#FFFF00"  -- Amarelo
    elseif percent >= 30 then
        return "#FF8000"  -- Laranja
    else
        return "#FF0000"  -- Vermelho
    end
end

function statusMonitor.getManaColor(percent)
    if percent >= 50 then
        return "#0080FF"  -- Azul
    elseif percent >= 30 then
        return "#8040FF"  -- Roxo
    else
        return "#FF0080"  -- Rosa
    end
```

#### Finalização
```lua
end

function statusMonitor.formatNumber(num)
    -- Formata números grandes (1000000 -> 1.00M)
    if num >= 1000000 then
        return string.format("%.2fM", num / 1000000)
    elseif num >= 1000 then
        return string.format("%.2fK", num / 1000)
    else
        return tostring(num)
    end
end
```

### Exemplo 3: Sistema de Hotkeys Customizado

#### Inicialização e Configuração
```lua
-- modules/custom_hotkeys/custom_hotkeys.lua
customHotkeys = {}

function customHotkeys.init()
    customHotkeys.bindings = {}
    customHotkeys.loadBindings()
    
    -- Interface de configuração
    customHotkeys.setupInterface()
    
    -- Comando para abrir interface
    modules.game_console.addCommand('hotkeys', customHotkeys.toggle, 'Abre configuração de hotkeys')
end

function customHotkeys.setupInterface()
    customHotkeys.window = g_ui.displayUI('custom_hotkeys')
    customHotkeys.window:hide()
    
    customHotkeys.keyEdit = customHotkeys.window:getChildById('keyEdit')
    customHotkeys.actionCombo = customHotkeys.window:getChildById('actionCombo')
    customHotkeys.valueEdit = customHotkeys.window:getChildById('valueEdit')
    customHotkeys.bindingsList = customHotkeys.window:getChildById('bindingsList')
    
    -- Ações disponíveis
    customHotkeys.actionCombo:addOption('Falar', 'say')
    customHotkeys.actionCombo:addOption('Usar Spell', 'spell')
    customHotkeys.actionCombo:addOption('Usar Item', 'item')
    customHotkeys.actionCombo:addOption('Executar Comando', 'command')
    
    -- Eventos da interface
    customHotkeys.window:getChildById('addButton').onClick = customHotkeys.addBinding
    customHotkeys.window:getChildById('removeButton').onClick = customHotkeys.removeBinding
    customHotkeys.window:getChildById('saveButton').onClick = customHotkeys.saveBindings
    
    customHotkeys.updateBindingsList()
end
```

#### Funcionalidade 1
```lua

function customHotkeys.toggle()
    if customHotkeys.window:isVisible() then
        customHotkeys.window:hide()
    else
        customHotkeys.window:show()
        customHotkeys.window:raise()
    end
end

function customHotkeys.addBinding()
    local key = customHotkeys.keyEdit:getText()
    local action = customHotkeys.actionCombo:getCurrentOption().data
    local value = customHotkeys.valueEdit:getText()
    
    if #key == 0 or #value == 0 then
        modules.game_textmessage.displayGameMessage('Preencha todos os campos!')
        return
    end
    
    -- Remove binding anterior se existir
    customHotkeys.removeKeyBinding(key)
    
    -- Cria novo binding
    local binding = {
        key = key,
        action = action,
        value = value
    }
```

#### Funcionalidade 2
```lua
    
    customHotkeys.bindings[key] = binding
    
    -- Registra no sistema
    g_keyboard.bindKeyPress(key, function()
        customHotkeys.executeBinding(binding)
    end)
    
    customHotkeys.updateBindingsList()
    customHotkeys.clearFields()
end

function customHotkeys.removeBinding()
    local selected = customHotkeys.bindingsList:getFocusedChild()
    if not selected then
        return
    end
    
    local key = selected.bindingKey
    customHotkeys.removeKeyBinding(key)
    customHotkeys.updateBindingsList()
end
```

#### Funcionalidade 3
```lua

function customHotkeys.removeKeyBinding(key)
    if customHotkeys.bindings[key] then
        g_keyboard.unbindKeyPress(key)
        customHotkeys.bindings[key] = nil
    end
end

function customHotkeys.executeBinding(binding)
    if not g_game.isOnline() then
        return
    end
    
    if binding.action == 'say' then
        g_game.talk(binding.value)
    elseif binding.action == 'spell' then
        modules.game_console.sendMessage('exura "' .. binding.value .. '"')
    elseif binding.action == 'item' then
        local itemId = tonumber(binding.value)
        if itemId then
            g_game.useInventoryItem(itemId)
        end
```

#### Funcionalidade 4
```lua
    elseif binding.action == 'command' then
        modules.game_console.sendMessage(binding.value)
    end
end

function customHotkeys.updateBindingsList()
    customHotkeys.bindingsList:destroyChildren()
    
    for key, binding in pairs(customHotkeys.bindings) do
        local label = g_ui.createWidget('UILabel', customHotkeys.bindingsList)
        label:setText(string.format("%s: %s (%s)", key, binding.value, binding.action))
        label.bindingKey = key
        
        -- Cor baseada na ação
        if binding.action == 'say' then
            label:setColor('#FFFF00')
        elseif binding.action == 'spell' then
            label:setColor('#00FF00')
        elseif binding.action == 'item' then
            label:setColor('#FF8000')
        elseif binding.action == 'command' then
            label:setColor('#FF0080')
        end
```

#### Funcionalidade 5
```lua
    end
end

function customHotkeys.clearFields()
    customHotkeys.keyEdit:clearText()
    customHotkeys.valueEdit:clearText()
    customHotkeys.actionCombo:setCurrentIndex(0)
end

function customHotkeys.saveBindings()
    g_settings.setNode('customHotkeys.bindings', customHotkeys.bindings)
    g_settings.save()
    modules.game_textmessage.displayGameMessage('Hotkeys salvos!')
end

function customHotkeys.loadBindings()
    local saved = g_settings.getNode('customHotkeys.bindings')
    if saved then
        for key, binding in pairs(saved) do
            customHotkeys.bindings[key] = binding
            g_keyboard.bindKeyPress(key, function()
                customHotkeys.executeBinding(binding)
            end)
```

#### Finalização
```lua
        end
    end
end
```

### Exemplo 4: Sistema de Notificações

#### Inicialização e Configuração
```lua
-- modules/notifications/notifications.lua
notifications = {}

function notifications.init()
    notifications.queue = {}
    notifications.container = g_ui.createWidget('UIWidget', rootWidget)
    notifications.container:setId('notificationsContainer')
    notifications.container:addAnchor(AnchorTop, 'parent', AnchorTop)
    notifications.container:addAnchor(AnchorRight, 'parent', AnchorRight)
    notifications.container:setMarginTop(50)
    notifications.container:setMarginRight(20)
    notifications.container:setFocusable(false)
    
    -- Layout vertical para as notificações
    notifications.layout = g_ui.createWidget('UIVerticalLayout', notifications.container)
    notifications.layout:setSpacing(5)
end

function notifications.show(title, message, type, duration)
    type = type or 'info'
    duration = duration or 3000
    
    local notification = g_ui.createWidget('UIWidget', notifications.container)
    notification:setHeight(60)
    notification:setWidth(300)
    notification:setBackgroundColor('#000000')
    notification:setOpacity(0.9)
    notification:setBorderWidth(2)
    notification:setPadding(10)
    
    -- Cor da borda baseada no tipo
    local borderColor = '#FFFFFF'
    if type == 'success' then
        borderColor = '#00FF00'
    elseif type == 'warning' then
        borderColor = '#FFFF00'
    elseif type == 'error' then
        borderColor = '#FF0000'
    elseif type == 'info' then
        borderColor = '#0080FF'
    end
```

#### Funcionalidade 1
```lua
    notification:setBorderColor(borderColor)
    
    -- Título
    local titleLabel = g_ui.createWidget('UILabel', notification)
    titleLabel:setText(title)
    titleLabel:setFont('verdana-11px-rounded')
    titleLabel:setTextColor('#FFFFFF')
    titleLabel:addAnchor(AnchorTop, 'parent', AnchorTop)
    titleLabel:addAnchor(AnchorLeft, 'parent', AnchorLeft)
    titleLabel:addAnchor(AnchorRight, 'parent', AnchorRight)
    titleLabel:setHeight(20)
    
    -- Mensagem
    local messageLabel = g_ui.createWidget('UILabel', notification)
    messageLabel:setText(message)
    messageLabel:setFont('verdana-9px-rounded')
    messageLabel:setTextColor('#CCCCCC')
    messageLabel:addAnchor(AnchorTop, 'titleLabel', AnchorBottom)
    messageLabel:addAnchor(AnchorLeft, 'parent', AnchorLeft)
    messageLabel:addAnchor(AnchorRight, 'parent', AnchorRight)
    messageLabel:addAnchor(AnchorBottom, 'parent', AnchorBottom)
    messageLabel:setTextWrap(true)
    
    -- Efeito de entrada
    notification:setOpacity(0)
    notification:setMarginRight(-320)
    
    -- Animação de entrada
    g_effects.fadeIn(notification, 200)
    g_effects.slideIn(notification, 'right', 200)
    
    -- Auto-remoção
    scheduleEvent(function()
        notifications.remove(notification)
    end, duration)
```

#### Funcionalidade 2
```lua
    
    -- Clique para remover
    notification.onClick = function()
        notifications.remove(notification)
    end
    
    -- Som baseado no tipo
    if type == 'error' then
        g_sounds.playEffect('error.wav')
    elseif type == 'success' then
        g_sounds.playEffect('success.wav')
    end
    
    return notification
end

function notifications.remove(notification)
    if not notification or notification:isDestroyed() then
        return
    end
    
    -- Animação de saída
    g_effects.fadeOut(notification, 200, function()
        notification:destroy()
    end)
```

#### Funcionalidade 3
```lua
end

-- Funções de conveniência
function notifications.success(title, message, duration)
    return notifications.show(title, message, 'success', duration)
end

function notifications.warning(title, message, duration)
    return notifications.show(title, message, 'warning', duration)
end

function notifications.error(title, message, duration)
    return notifications.show(title, message, 'error', duration)
end

function notifications.info(title, message, duration)
    return notifications.show(title, message, 'info', duration)
end

-- Integração com eventos do jogo
connect(g_game, {
    onGameStart = function()
        notifications.success('Conectado', 'Conectado ao servidor com sucesso!')
    end,
```

#### Finalização
```lua
    onGameEnd = function()
        notifications.info('Desconectado', 'Desconectado do servidor')
    end,
    onLoginError = function(message)
        notifications.error('Erro de Login', message)
    end,
    onConnectionError = function(message)
        notifications.error('Erro de Conexão', message)
    end
})

-- API pública para outros módulos
_G.notify = notifications
```

---

## 🔗 Referências Rápidas

### Códigos de Tecla Comuns

```lua
-- Teclas especiais
    --  Teclas especiais (traduzido)
KeyCode.Escape, KeyCode.Tab, KeyCode.Return, KeyCode.Space
KeyCode.Shift, KeyCode.Ctrl, KeyCode.Alt
KeyCode.Insert, KeyCode.Delete, KeyCode.Home, KeyCode.End
KeyCode.PageUp, KeyCode.PageDown
KeyCode.Up, KeyCode.Down, KeyCode.Left, KeyCode.Right

-- Teclas de função
KeyCode.F1, KeyCode.F2, ..., KeyCode.F12

-- Números
KeyCode.Key0, KeyCode.Key1, ..., KeyCode.Key9

-- Letras
    --  Letras (traduzido)
KeyCode.A, KeyCode.B, ..., KeyCode.Z
```

### Cores Comuns

```lua
-- Cores básicas
"#FFFFFF" -- Branco
"#000000" -- Preto  
"#FF0000" -- Vermelho
"#00FF00" -- Verde
"#0000FF" -- Azul
"#FFFF00" -- Amarelo
"#FF00FF" -- Magenta
"#00FFFF" -- Ciano

-- Cores do chat
    --  Cores do chat (traduzido)
"#FFFF00" -- Amarelo (say)
"#A5F1FF" -- Azul claro (whisper) 
"#FF6060" -- Vermelho claro (yell)
"#C0C0C0" -- Cinza (private)
```

### Enums Importantes

#### Nível Basic
```lua
-- Direções
North, South, East, West, Northeast, Northwest, Southeast, Southwest

-- Modos de luta  
FightOffensive, FightBalanced, FightDefensive

-- Modos de perseguição
DontChase, ChaseOpponent

-- Tipos de canal
ChannelType.Say, ChannelType.Whisper, ChannelType.Yell
ChannelType.Private, ChannelType.NpcTo, ChannelType.Party

-- Skills
Otc.Skill.Fist, Otc.Skill.Club, Otc.Skill.Sword, Otc.Skill.Axe
Otc.Skill.Distance, Otc.Skill.Shielding, Otc.Skill.Fishing

-- Slots de inventário  
InventorySlotHead, InventorySlotNecklace, InventorySlotBack
InventorySlotBody, InventorySlotRight, InventorySlotLeft
InventorySlotLegs, InventorySlotFeet, InventorySlotFinger
InventorySlotAmmo
```

#### Nível Intermediate
```lua
-- Direções
North, South, East, West, Northeast, Northwest, Southeast, Southwest

-- Modos de luta  
FightOffensive, FightBalanced, FightDefensive

-- Modos de perseguição
DontChase, ChaseOpponent

-- Tipos de canal
ChannelType.Say, ChannelType.Whisper, ChannelType.Yell
ChannelType.Private, ChannelType.NpcTo, ChannelType.Party

-- Skills
Otc.Skill.Fist, Otc.Skill.Club, Otc.Skill.Sword, Otc.Skill.Axe
Otc.Skill.Distance, Otc.Skill.Shielding, Otc.Skill.Fishing

-- Slots de inventário  
InventorySlotHead, InventorySlotNecklace, InventorySlotBack
InventorySlotBody, InventorySlotRight, InventorySlotLeft
InventorySlotLegs, InventorySlotFeet, InventorySlotFinger
InventorySlotAmmo
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
-- Direções
North, South, East, West, Northeast, Northwest, Southeast, Southwest

-- Modos de luta  
FightOffensive, FightBalanced, FightDefensive

-- Modos de perseguição
DontChase, ChaseOpponent

-- Tipos de canal
ChannelType.Say, ChannelType.Whisper, ChannelType.Yell
ChannelType.Private, ChannelType.NpcTo, ChannelType.Party

-- Skills
Otc.Skill.Fist, Otc.Skill.Club, Otc.Skill.Sword, Otc.Skill.Axe
Otc.Skill.Distance, Otc.Skill.Shielding, Otc.Skill.Fishing

-- Slots de inventário  
InventorySlotHead, InventorySlotNecklace, InventorySlotBack
InventorySlotBody, InventorySlotRight, InventorySlotLeft
InventorySlotLegs, InventorySlotFeet, InventorySlotFinger
InventorySlotAmmo
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

Esta referência da API Lua cobre as principais funcionalidades disponíveis no OTClient. Para casos específicos ou funcionalidades avançadas, consulte também a documentação dos módulos individuais e os exemplos práticos fornecidos.

---

## 🔗 **Links Automáticos - Documentação Legacy**

> [!info] **Documentação Legacy**
> Este arquivo faz parte da documentação legacy do projeto

### **📚 Links Obrigatórios**
- [[../../README|Hub Central da Wiki]]
- [[../../dashboard/task_master|Task Master]]
- [[../../dashboard/integrated_task_manager|Dashboard Central]]

### **🔧 Links de Documentação**
- [[../../legacy_docs/README|Documentação Legacy]]
- [[../../docs/README|Documentação Principal]]
- [[../../research/README|Pesquisa Principal]]

### **📊 Documentação Relacionada**
- [[../../legacy_docs/src/README|Código-Fonte Legacy]]
- [[../../legacy_docs/research/README|Pesquisa Legacy]]
- [[../../legacy_docs/docs/README|Documentação Legacy]]

### **📈 Métricas do Arquivo**
- **Nome**: LuaAPI.md
- **Categoria**: Documentação Legacy
- **Função**: Referência Lua API legacy
- **Status**: Arquivado

---