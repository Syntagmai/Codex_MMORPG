
# CORE-010: Sistema de Backup

<div class="info"> **Sistema Completo de Backup e Recuperação**
> Documentação completa do sistema de backup do OTClient, incluindo backup automático, recuperação de dados, versionamento, sincronização e proteção contra perda de dados.

## 📋 Índice
- [#Visão Geral](#Visão Geral.md)
- [#Sistema de Backup](#Sistema de Backup.md)
- [#Tipos de Backup](#Tipos de Backup.md)
- [#Versionamento](#Versionamento.md)
- [#Sincronização](#Sincronização.md)
- [#Recuperação](#Recuperação.md)
- [#Monitoramento](#Monitoramento.md)
- [#Exemplos Práticos](#Exemplos Práticos.md)
- [#Melhores Práticas](#Melhores Práticas.md)

---

## 🎯 Visão Geral

O sistema de backup do OTClient oferece proteção completa contra perda de dados:

### **💾 Componentes Principais:**
- **Backup Automático**: Backup programado e automático
- **Múltiplos Tipos**: Completo, incremental, diferencial
- **Versionamento**: Controle de versões dos backups
- **Sincronização**: Sincronização entre dispositivos
- **Recuperação**: Recuperação rápida e confiável
- **Monitoramento**: Acompanhamento de status e integridade

### 🏗️ **Arquitetura do Sistema**

```
Sistema de Backup
   │
   ├─ Backup Engine
   │   ├─ Automatic Backup
   │   ├─ Manual Backup
   │   ├─ Scheduled Backup
   │   └─ Backup Validation
   │
   ├─ Storage Management
   │   ├─ Local Storage
   │   ├─ Cloud Storage
   │   ├─ Compression
   │   └─ Encryption
   │
   ├─ Version Control
   │   ├─ Version History
   │   ├─ Rollback System
   │   ├─ Conflict Resolution
   │   └─ Change Tracking
   │
   └─ Recovery System
       ├─ Data Recovery
       ├─ Configuration Recovery
       ├─ System Recovery
       └─ Disaster Recovery
```

---

## 💾 Sistema de Backup

### 🎯 **Configuração Principal**

#### Inicialização e Configuração
```lua
-- Sistema de backup principal
local BackupSystem = {}

-- Configuração global
BackupSystem.config = {
    -- Configuração geral
    enabled = true,
    autoBackup = true,
    backupInterval = 3600000,  -- 1 hora
    maxBackups = 10,
    
    -- Configuração de armazenamento
    storage = {
        local = {
            enabled = true,
            path = "backups/",
            maxSize = 1024 * 1024 * 1024,  -- 1GB
            compress = true,
            encrypt = false
        },
        cloud = {
            enabled = false,
            provider = "local",  -- local, dropbox, google, etc.
            path = "otclient_backups/",
            sync = true
        }
```

#### Funcionalidade 1
```lua
    },
    
    -- Configuração de dados
    data = {
        settings = true,
        characters = true,
        modules = true,
        logs = false,
        cache = false
    },
    
    -- Configuração de validação
    validation = {
        enabled = true,
        checksum = true,
        integrity = true,
        testRestore = false
    }
}

-- Inicializar sistema de backup
function BackupSystem.init()
```

#### Funcionalidade 2
```lua
    BackupSystem.loadConfiguration()
    BackupSystem.setupDirectories()
    BackupSystem.setupScheduler()
    BackupSystem.setupValidation()
    
    print("Sistema de backup inicializado")
end

function BackupSystem.loadConfiguration()
    -- Carregar configuração das settings
    BackupSystem.config.enabled = g_settings.getBoolean("backup.enabled", true)
    BackupSystem.config.autoBackup = g_settings.getBoolean("backup.autoBackup", true)
    BackupSystem.config.backupInterval = g_settings.getNumber("backup.interval", 3600000)
    BackupSystem.config.maxBackups = g_settings.getNumber("backup.maxBackups", 10)
    
    -- Configurar armazenamento local
    BackupSystem.config.storage.local.enabled = g_settings.getBoolean("backup.storage.local.enabled", true)
    BackupSystem.config.storage.local.path = g_settings.getString("backup.storage.local.path", "backups/")
    BackupSystem.config.storage.local.compress = g_settings.getBoolean("backup.storage.local.compress", true)
    
    -- Configurar dados para backup
    BackupSystem.config.data.settings = g_settings.getBoolean("backup.data.settings", true)
    BackupSystem.config.data.characters = g_settings.getBoolean("backup.data.characters", true)
    BackupSystem.config.data.modules = g_settings.getBoolean("backup.data.modules", true)
end
```

#### Finalização
```lua

function BackupSystem.setupDirectories()
    -- Criar diretório de backup se não existir
    if BackupSystem.config.storage.local.enabled then
        local path = BackupSystem.config.storage.local.path
        if not io.open(path, "r") then
            os.execute("mkdir -p " .. path)
        end
        
        -- Criar subdiretórios
        local subdirs = {"settings", "characters", "modules", "logs", "temp"}
        for _, subdir in ipairs(subdirs) do
            local subpath = path .. subdir .. "/"
            if not io.open(subpath, "r") then
                os.execute("mkdir -p " .. subpath)
            end
        end
    end
end
```

### 🔧 **Sistema de Agendamento**

#### Inicialização e Configuração
```lua
-- Sistema de agendamento de backups
BackupSystem.scheduler = {}

function BackupSystem.setupScheduler()
    BackupSystem.scheduler.enabled = BackupSystem.config.autoBackup
    BackupSystem.scheduler.interval = BackupSystem.config.backupInterval
    BackupSystem.scheduler.lastBackup = 0
    BackupSystem.scheduler.nextBackup = g_clock.millis() + BackupSystem.scheduler.interval
    
    if BackupSystem.scheduler.enabled then
        BackupSystem.startScheduler()
    end
end

function BackupSystem.startScheduler()
    -- Iniciar agendador em background
    connect(g_app, 'onRun', function()
        BackupSystem.updateScheduler()
    end)
end

function BackupSystem.updateScheduler()
```

#### Funcionalidade 1
```lua
    if not BackupSystem.scheduler.enabled then
        return
    end
    
    local currentTime = g_clock.millis()
    
    -- Verificar se é hora de fazer backup
    if currentTime >= BackupSystem.scheduler.nextBackup then
        BackupSystem.performAutomaticBackup()
        BackupSystem.scheduler.lastBackup = currentTime
        BackupSystem.scheduler.nextBackup = currentTime + BackupSystem.scheduler.interval
    end
end

function BackupSystem.performAutomaticBackup()
    if not BackupSystem.config.enabled then
        return
    end
    
    print("Iniciando backup automático...")
    
    -- Verificar espaço disponível
    if not BackupSystem.checkStorageSpace() then
        BackupSystem.cleanupOldBackups()
        if not BackupSystem.checkStorageSpace() then
            print("ERRO: Espaço insuficiente para backup")
            return
        end
```

#### Funcionalidade 2
```lua
    end
    
    -- Executar backup
    local success = BackupSystem.createBackup("auto")
    
    if success then
        print("Backup automático concluído com sucesso")
        BackupSystem.logBackup("auto", true)
    else
        print("ERRO: Falha no backup automático")
        BackupSystem.logBackup("auto", false)
    end
end

function BackupSystem.checkStorageSpace()
    if not BackupSystem.config.storage.local.enabled then
        return true
    end
    
    local path = BackupSystem.config.storage.local.path
    local requiredSpace = 100 * 1024 * 1024  -- 100MB estimado
    
    -- Verificar espaço disponível (implementação simplificada)
    local availableSpace = BackupSystem.getAvailableSpace(path)
    
    return availableSpace >= requiredSpace
end
```

#### Finalização
```lua

function BackupSystem.getAvailableSpace(path)
    -- Implementação simplificada - em produção usar APIs do sistema
    return 1024 * 1024 * 1024  -- 1GB (simulado)
end
```

---

## 📦 Tipos de Backup

### 🎯 **Backup Completo**

#### Inicialização e Configuração
```lua
-- Sistema de backup completo
BackupSystem.full = {}

function BackupSystem.createFullBackup(name)
    name = name or "full_" .. os.date("%Y%m%d_%H%M%S")
    
    print("Criando backup completo: " .. name)
    
    local backupPath = BackupSystem.config.storage.local.path .. name .. "/"
    local success = true
    
    -- Criar diretório do backup
    os.execute("mkdir -p " .. backupPath)
    
    -- Backup de configurações
    if BackupSystem.config.data.settings then
        success = success and BackupSystem.backupSettings(backupPath)
    end
    
    -- Backup de personagens
    if BackupSystem.config.data.characters then
        success = success and BackupSystem.backupCharacters(backupPath)
    end
```

#### Funcionalidade 1
```lua
    
    -- Backup de módulos
    if BackupSystem.config.data.modules then
        success = success and BackupSystem.backupModules(backupPath)
    end
    
    -- Backup de logs (opcional)
    if BackupSystem.config.data.logs then
        success = success and BackupSystem.backupLogs(backupPath)
    end
    
    -- Criar metadados do backup
    if success then
        BackupSystem.createBackupMetadata(backupPath, "full", name)
    end
    
    return success
end

function BackupSystem.backupSettings(backupPath)
    local settingsPath = backupPath .. "settings/"
    os.execute("mkdir -p " .. settingsPath)
    
    -- Copiar arquivos de configuração
    local settingsFiles = {
        "otclient.otml",
        "modules.otml",
        "keybind.otml"
    }
```

#### Funcionalidade 2
```lua
    
    for _, file in ipairs(settingsFiles) do
        local source = file
        local destination = settingsPath .. file
        
        if io.open(source, "r") then
            local success = BackupSystem.copyFile(source, destination)
            if not success then
                print("ERRO: Falha ao copiar " .. file)
                return false
            end
        end
    end
    
    return true
end

function BackupSystem.backupCharacters(backupPath)
    local charactersPath = backupPath .. "characters/"
    os.execute("mkdir -p " .. charactersPath)
    
    -- Backup de dados de personagens
    if g_game and g_game.isOnline() then
        local character = g_game.getLocalPlayer()
        if character then
            local characterData = {
                name = character:getName(),
                level = character:getLevel(),
                vocation = character:getVocation(),
                position = character:getPosition(),
                health = character:getHealth(),
                maxHealth = character:getMaxHealth(),
                mana = character:getMana(),
                maxMana = character:getMaxMana(),
                experience = character:getExperience(),
                timestamp = os.date("%Y-%m-%d %H:%M:%S")
            }
```

#### Funcionalidade 3
```lua
            
            local file = io.open(charactersPath .. "current_character.json", "w")
            if file then
                file:write(BackupSystem.encodeJSON(characterData))
                file:close()
            end
        end
    end
    
    return true
end

function BackupSystem.backupModules(backupPath)
    local modulesPath = backupPath .. "modules/"
    os.execute("mkdir -p " .. modulesPath)
    
    -- Backup de módulos personalizados
    local modulesDir = "modules/"
    if io.open(modulesDir, "r") then
        local success = BackupSystem.copyDirectory(modulesDir, modulesPath)
        if not success then
            print("ERRO: Falha ao copiar módulos")
            return false
        end
```

#### Finalização
```lua
    end
    
    return true
end

function BackupSystem.backupLogs(backupPath)
    local logsPath = backupPath .. "logs/"
    os.execute("mkdir -p " .. logsPath)
    
    -- Backup de logs recentes
    local logsDir = "logs/"
    if io.open(logsDir, "r") then
        local success = BackupSystem.copyDirectory(logsDir, logsPath)
        if not success then
            print("ERRO: Falha ao copiar logs")
            return false
        end
    end
    
    return true
end
```

### 🔄 **Backup Incremental**

#### Inicialização e Configuração
```lua
-- Sistema de backup incremental
BackupSystem.incremental = {}

function BackupSystem.createIncrementalBackup(name)
    name = name or "incremental_" .. os.date("%Y%m%d_%H%M%S")
    
    print("Criando backup incremental: " .. name)
    
    -- Encontrar último backup completo
    local lastFullBackup = BackupSystem.findLastFullBackup()
    if not lastFullBackup then
        print("ERRO: Nenhum backup completo encontrado")
        return false
    end
    
    local backupPath = BackupSystem.config.storage.local.path .. name .. "/"
    local success = true
    
    -- Criar diretório do backup
    os.execute("mkdir -p " .. backupPath)
    
    -- Backup apenas de arquivos modificados
    success = success and BackupSystem.backupModifiedFiles(lastFullBackup, backupPath)
    
    -- Criar metadados do backup
    if success then
        BackupSystem.createBackupMetadata(backupPath, "incremental", name, lastFullBackup)
    end
```

#### Funcionalidade 1
```lua
    
    return success
end

function BackupSystem.findLastFullBackup()
    local backupPath = BackupSystem.config.storage.local.path
    local backups = {}
    
    -- Listar backups
    for file in io.popen("ls -t " .. backupPath):lines() do
        if file:match("^full_") then
            table.insert(backups, file)
        end
    end
    
    if #backups > 0 then
        return backups[1]  -- Mais recente
    end
    
    return nil
end
```

#### Funcionalidade 2
```lua

function BackupSystem.backupModifiedFiles(lastBackup, backupPath)
    local lastBackupPath = BackupSystem.config.storage.local.path .. lastBackup .. "/"
    
    -- Verificar arquivos modificados desde o último backup
    local modifiedFiles = BackupSystem.getModifiedFiles(lastBackupPath)
    
    for _, file in ipairs(modifiedFiles) do
        local source = file
        local destination = backupPath .. file
        
        -- Criar diretório de destino se necessário
        local destDir = destination:match("(.+)/[^/]+$")
        if destDir then
            os.execute("mkdir -p " .. destDir)
        end
        
        local success = BackupSystem.copyFile(source, destination)
        if not success then
            print("ERRO: Falha ao copiar " .. file)
            return false
        end
```

#### Funcionalidade 3
```lua
    end
    
    return true
end

function BackupSystem.getModifiedFiles(lastBackupPath)
    local modifiedFiles = {}
    
    -- Implementação simplificada - em produção usar APIs do sistema
    -- para verificar timestamps e hashes dos arquivos
    
    -- Verificar configurações modificadas
    if BackupSystem.isFileModified("otclient.otml", lastBackupPath .. "settings/otclient.otml") then
        table.insert(modifiedFiles, "otclient.otml")
    end
    
    -- Verificar módulos modificados
    if BackupSystem.isDirectoryModified("modules/", lastBackupPath .. "modules/") then
        table.insert(modifiedFiles, "modules/")
    end
    
    return modifiedFiles
end
```

#### Finalização
```lua

function BackupSystem.isFileModified(source, backup)
    -- Verificar se arquivo foi modificado
    local sourceFile = io.open(source, "r")
    local backupFile = io.open(backup, "r")
    
    if not sourceFile or not backupFile then
        return true  -- Considerar modificado se não existir
    end
    
    sourceFile:close()
    backupFile:close()
    
    -- Em produção, comparar timestamps e hashes
    return false  -- Simplificado
end

function BackupSystem.isDirectoryModified(source, backup)
    -- Verificar se diretório foi modificado
    return true  -- Simplificado
end
```

---

## 🔄 Versionamento

### 🎯 **Sistema de Versões**

#### Inicialização e Configuração
```lua
-- Sistema de versionamento de backups
BackupSystem.versioning = {}

function BackupSystem.createBackupMetadata(backupPath, type, name, parent)
    local metadata = {
        name = name,
        type = type,
        timestamp = os.date("%Y-%m-%d %H:%M:%S"),
        version = BackupSystem.generateVersion(),
        parent = parent,
        size = BackupSystem.calculateBackupSize(backupPath),
        checksum = BackupSystem.calculateChecksum(backupPath),
        files = BackupSystem.listBackupFiles(backupPath)
    }
    
    local file = io.open(backupPath .. "metadata.json", "w")
    if file then
        file:write(BackupSystem.encodeJSON(metadata))
        file:close()
    end
end
```

#### Funcionalidade 1
```lua

function BackupSystem.generateVersion()
    -- Gerar versão baseada em timestamp
    return os.date("%Y%m%d.%H%M%S")
end

function BackupSystem.calculateBackupSize(backupPath)
    -- Calcular tamanho total do backup
    local size = 0
    
    local function calculateDirSize(path)
        for file in io.popen("find " .. path .. " -type f"):lines() do
            local f = io.open(file, "r")
            if f then
                f:seek("end")
                size = size + f:seek("cur")
                f:close()
            end
        end
    end
    
    calculateDirSize(backupPath)
    return size
end
```

#### Funcionalidade 2
```lua

function BackupSystem.calculateChecksum(backupPath)
    -- Calcular checksum do backup (simplificado)
    return "checksum_" .. os.time()
end

function BackupSystem.listBackupFiles(backupPath)
    local files = {}
    
    for file in io.popen("find " .. backupPath .. " -type f"):lines() do
        local relativePath = file:gsub(backupPath, "")
        table.insert(files, relativePath)
    end
    
    return files
end

function BackupSystem.getBackupHistory()
    local backupPath = BackupSystem.config.storage.local.path
    local history = {}
    
    for backup in io.popen("ls -t " .. backupPath):lines() do
        local metadataFile = backupPath .. backup .. "/metadata.json"
        local file = io.open(metadataFile, "r")
        
        if file then
            local content = file:read("*all")
            file:close()
            
            local metadata = BackupSystem.decodeJSON(content)
            if metadata then
                table.insert(history, metadata)
            end
```

#### Funcionalidade 3
```lua
        end
    end
    
    return history
end

function BackupSystem.rollbackToVersion(version)
    print("Executando rollback para versão: " .. version)
    
    -- Encontrar backup da versão
    local backup = BackupSystem.findBackupByVersion(version)
    if not backup then
        print("ERRO: Backup da versão não encontrado")
        return false
    end
    
    -- Validar integridade do backup
    if not BackupSystem.validateBackup(backup.path) then
        print("ERRO: Backup corrompido")
        return false
    end
```

#### Funcionalidade 4
```lua
    
    -- Executar restauração
    local success = BackupSystem.restoreFromBackup(backup.path)
    
    if success then
        print("Rollback concluído com sucesso")
        BackupSystem.logRollback(version, true)
    else
        print("ERRO: Falha no rollback")
        BackupSystem.logRollback(version, false)
    end
    
    return success
end

function BackupSystem.findBackupByVersion(version)
    local history = BackupSystem.getBackupHistory()
    
    for _, backup in ipairs(history) do
        if backup.version == version then
            return backup
        end
```

#### Finalização
```lua
    end
    
    return nil
end
```

---

## 🔄 Sincronização

### 🎯 **Sistema de Sincronização**

#### Inicialização e Configuração
```lua
-- Sistema de sincronização de backups
BackupSystem.sync = {}

function BackupSystem.setupSync()
    BackupSystem.sync.enabled = BackupSystem.config.storage.cloud.enabled
    BackupSystem.sync.provider = BackupSystem.config.storage.cloud.provider
    BackupSystem.sync.path = BackupSystem.config.storage.cloud.path
    BackupSystem.sync.interval = 300000  -- 5 minutos
    
    if BackupSystem.sync.enabled then
        BackupSystem.startSync()
    end
end

function BackupSystem.startSync()
    -- Iniciar sincronização em background
    connect(g_app, 'onRun', function()
        BackupSystem.updateSync()
    end)
end

function BackupSystem.updateSync()
```

#### Funcionalidade 1
```lua
    if not BackupSystem.sync.enabled then
        return
    end
    
    local currentTime = g_clock.millis()
    
    -- Verificar se é hora de sincronizar
    if not BackupSystem.sync.lastSync then
        BackupSystem.sync.lastSync = 0
    end
    
    if currentTime - BackupSystem.sync.lastSync >= BackupSystem.sync.interval then
        BackupSystem.performSync()
        BackupSystem.sync.lastSync = currentTime
    end
end

function BackupSystem.performSync()
    print("Iniciando sincronização de backups...")
    
    -- Sincronizar backups locais com nuvem
    local success = BackupSystem.syncToCloud()
    
    if success then
        print("Sincronização concluída com sucesso")
        BackupSystem.logSync(true)
    else
        print("ERRO: Falha na sincronização")
        BackupSystem.logSync(false)
    end
```

#### Funcionalidade 2
```lua
end

function BackupSystem.syncToCloud()
    local localPath = BackupSystem.config.storage.local.path
    local cloudPath = BackupSystem.sync.path
    
    -- Implementação específica por provedor
    if BackupSystem.sync.provider == "local" then
        return BackupSystem.syncToLocalCloud(localPath, cloudPath)
    elseif BackupSystem.sync.provider == "dropbox" then
        return BackupSystem.syncToDropbox(localPath, cloudPath)
    elseif BackupSystem.sync.provider == "google" then
        return BackupSystem.syncToGoogle(localPath, cloudPath)
    end
    
    return false
end

function BackupSystem.syncToLocalCloud(localPath, cloudPath)
    -- Sincronização para nuvem local (outro diretório)
    local command = string.format("rsync -av --delete %s %s", localPath, cloudPath)
    local result = os.execute(command)
    
    return result == 0
end
```

#### Finalização
```lua

function BackupSystem.syncToDropbox(localPath, cloudPath)
    -- Sincronização para Dropbox (implementação específica)
    print("Sincronização para Dropbox não implementada")
    return false
end

function BackupSystem.syncToGoogle(localPath, cloudPath)
    -- Sincronização para Google Drive (implementação específica)
    print("Sincronização para Google Drive não implementada")
    return false
end
```

---

## 🔧 Recuperação

### 🎯 **Sistema de Recuperação**

#### Inicialização e Configuração
```lua
-- Sistema de recuperação de backups
BackupSystem.recovery = {}

function BackupSystem.restoreFromBackup(backupPath)
    print("Iniciando restauração do backup: " .. backupPath)
    
    -- Validar backup antes da restauração
    if not BackupSystem.validateBackup(backupPath) then
        print("ERRO: Backup inválido")
        return false
    end
    
    -- Criar backup de segurança antes da restauração
    local safetyBackup = BackupSystem.createSafetyBackup()
    
    local success = true
    
    -- Restaurar configurações
    if BackupSystem.config.data.settings then
        success = success and BackupSystem.restoreSettings(backupPath)
    end
```

#### Funcionalidade 1
```lua
    
    -- Restaurar personagens
    if BackupSystem.config.data.characters then
        success = success and BackupSystem.restoreCharacters(backupPath)
    end
    
    -- Restaurar módulos
    if BackupSystem.config.data.modules then
        success = success and BackupSystem.restoreModules(backupPath)
    end
    
    -- Restaurar logs (opcional)
    if BackupSystem.config.data.logs then
        success = success and BackupSystem.restoreLogs(backupPath)
    end
    
    if success then
        print("Restauração concluída com sucesso")
        BackupSystem.logRestore(backupPath, true)
        
        -- Remover backup de segurança se restauração foi bem-sucedida
        BackupSystem.removeSafetyBackup(safetyBackup)
    else
        print("ERRO: Falha na restauração")
        BackupSystem.logRestore(backupPath, false)
        
        -- Restaurar backup de segurança
        BackupSystem.restoreFromSafetyBackup(safetyBackup)
    end
```

#### Funcionalidade 2
```lua
    
    return success
end

function BackupSystem.validateBackup(backupPath)
    -- Verificar se backup existe
    if not io.open(backupPath, "r") then
        return false
    end
    
    -- Verificar metadados
    local metadataFile = backupPath .. "metadata.json"
    local file = io.open(metadataFile, "r")
    if not file then
        return false
    end
    
    local content = file:read("*all")
    file:close()
    
    local metadata = BackupSystem.decodeJSON(content)
    if not metadata then
        return false
    end
```

#### Funcionalidade 3
```lua
    
    -- Verificar checksum se habilitado
    if BackupSystem.config.validation.checksum then
        local currentChecksum = BackupSystem.calculateChecksum(backupPath)
        if currentChecksum ~= metadata.checksum then
            print("ERRO: Checksum não confere")
            return false
        end
    end
    
    return true
end

function BackupSystem.createSafetyBackup()
    local safetyName = "safety_" .. os.date("%Y%m%d_%H%M%S")
    print("Criando backup de segurança: " .. safetyName)
    
    local success = BackupSystem.createFullBackup(safetyName)
    return success and safetyName or nil
end

function BackupSystem.removeSafetyBackup(safetyBackup)
```

#### Funcionalidade 4
```lua
    if safetyBackup then
        local safetyPath = BackupSystem.config.storage.local.path .. safetyBackup
        os.execute("rm -rf " .. safetyPath)
        print("Backup de segurança removido: " .. safetyBackup)
    end
end

function BackupSystem.restoreFromSafetyBackup(safetyBackup)
    if safetyBackup then
        local safetyPath = BackupSystem.config.storage.local.path .. safetyBackup
        print("Restaurando backup de segurança: " .. safetyBackup)
        return BackupSystem.restoreFromBackup(safetyPath)
    end
    return false
end

function BackupSystem.restoreSettings(backupPath)
    local settingsPath = backupPath .. "settings/"
    
    -- Restaurar arquivos de configuração
    local settingsFiles = {
        "otclient.otml",
        "modules.otml",
        "keybind.otml"
    }
```

#### Funcionalidade 5
```lua
    
    for _, file in ipairs(settingsFiles) do
        local source = settingsPath .. file
        local destination = file
        
        if io.open(source, "r") then
            local success = BackupSystem.copyFile(source, destination)
            if not success then
                print("ERRO: Falha ao restaurar " .. file)
                return false
            end
        end
    end
    
    return true
end

function BackupSystem.restoreCharacters(backupPath)
    local charactersPath = backupPath .. "characters/"
    local characterFile = charactersPath .. "current_character.json"
    
    local file = io.open(characterFile, "r")
    if file then
        local content = file:read("*all")
        file:close()
        
        local characterData = BackupSystem.decodeJSON(content)
        if characterData then
            print("Dados do personagem restaurados: " .. characterData.name)
        end
```

#### Funcionalidade 6
```lua
    end
    
    return true
end

function BackupSystem.restoreModules(backupPath)
    local modulesPath = backupPath .. "modules/"
    
    -- Restaurar módulos
    if io.open(modulesPath, "r") then
        local success = BackupSystem.copyDirectory(modulesPath, "modules/")
        if not success then
            print("ERRO: Falha ao restaurar módulos")
            return false
        end
    end
    
    return true
end

function BackupSystem.restoreLogs(backupPath)
```

#### Finalização
```lua
    local logsPath = backupPath .. "logs/"
    
    -- Restaurar logs
    if io.open(logsPath, "r") then
        local success = BackupSystem.copyDirectory(logsPath, "logs/")
        if not success then
            print("ERRO: Falha ao restaurar logs")
            return false
        end
    end
    
    return true
end
```

---

## 📊 Monitoramento

### 🎯 **Sistema de Monitoramento**

#### Inicialização e Configuração
```lua
-- Sistema de monitoramento de backups
BackupSystem.monitoring = {}

function BackupSystem.setupMonitoring()
    BackupSystem.monitoring.enabled = true
    BackupSystem.monitoring.interval = 60000  -- 1 minuto
    BackupSystem.monitoring.lastCheck = 0
    BackupSystem.monitoring.metrics = {
        totalBackups = 0,
        successfulBackups = 0,
        failedBackups = 0,
        lastBackup = nil,
        storageUsed = 0,
        syncStatus = "unknown"
    }
    
    if BackupSystem.monitoring.enabled then
        BackupSystem.startMonitoring()
    end
end

function BackupSystem.startMonitoring()
```

#### Funcionalidade 1
```lua
    -- Iniciar monitoramento em background
    connect(g_app, 'onRun', function()
        BackupSystem.updateMonitoring()
    end)
end

function BackupSystem.updateMonitoring()
    if not BackupSystem.monitoring.enabled then
        return
    end
    
    local currentTime = g_clock.millis()
    if currentTime - BackupSystem.monitoring.lastCheck >= BackupSystem.monitoring.interval then
        BackupSystem.checkBackupMetrics()
        BackupSystem.monitoring.lastCheck = currentTime
    end
end

function BackupSystem.checkBackupMetrics()
    local metrics = BackupSystem.monitoring.metrics
    
    -- Verificar espaço de armazenamento
    metrics.storageUsed = BackupSystem.calculateStorageUsed()
    
    -- Verificar status de sincronização
    if BackupSystem.sync.enabled then
        metrics.syncStatus = BackupSystem.checkSyncStatus()
    end
```

#### Funcionalidade 2
```lua
    
    -- Verificar integridade dos backups
    BackupSystem.checkBackupIntegrity()
    
    -- Gerar relatório de métricas
    BackupSystem.generateMonitoringReport()
end

function BackupSystem.calculateStorageUsed()
    local backupPath = BackupSystem.config.storage.local.path
    local totalSize = 0
    
    if io.open(backupPath, "r") then
        for file in io.popen("find " .. backupPath .. " -type f"):lines() do
            local f = io.open(file, "r")
            if f then
                f:seek("end")
                totalSize = totalSize + f:seek("cur")
                f:close()
            end
        end
```

#### Funcionalidade 3
```lua
    end
    
    return totalSize
end

function BackupSystem.checkSyncStatus()
    -- Verificar status da sincronização
    if BackupSystem.sync.lastSync then
        local timeSinceLastSync = g_clock.millis() - BackupSystem.sync.lastSync
        if timeSinceLastSync < 600000 then  -- 10 minutos
            return "synced"
        else
            return "outdated"
        end
    end
    
    return "unknown"
end

function BackupSystem.checkBackupIntegrity()
    local backupPath = BackupSystem.config.storage.local.path
    local corruptedBackups = {}
    
    for backup in io.popen("ls " .. backupPath):lines() do
        local backupFullPath = backupPath .. backup
        if not BackupSystem.validateBackup(backupFullPath) then
            table.insert(corruptedBackups, backup)
        end
```

#### Funcionalidade 4
```lua
    end
    
    if #corruptedBackups > 0 then
        print("ALERTA: Backups corrompidos encontrados:")
        for _, backup in ipairs(corruptedBackups) do
            print("  - " .. backup)
        end
    end
end

function BackupSystem.generateMonitoringReport()
    local metrics = BackupSystem.monitoring.metrics
    local report = {
        timestamp = os.date("%Y-%m-%d %H:%M:%S"),
        totalBackups = metrics.totalBackups,
        successfulBackups = metrics.successfulBackups,
        failedBackups = metrics.failedBackups,
        successRate = metrics.totalBackups > 0 and (metrics.successfulBackups / metrics.totalBackups) * 100 or 0,
        storageUsed = metrics.storageUsed,
        syncStatus = metrics.syncStatus
    }
```

#### Finalização
```lua
    
    -- Salvar relatório
    local reportFile = io.open(BackupSystem.config.storage.local.path .. "monitoring.log", "a")
    if reportFile then
        reportFile:write(BackupSystem.encodeJSON(report) .. "\n")
        reportFile:close()
    end
end
```

---

## 💡 Exemplos Práticos

### 🎯 **Exemplo de Uso Completo**

#### Inicialização e Configuração
```lua
-- Exemplo completo de uso do sistema de backup
function setupBackupSystem()
    -- Inicializar sistema de backup
    BackupSystem.init()
    
    -- Configurar sincronização
    BackupSystem.setupSync()
    
    -- Configurar monitoramento
    BackupSystem.setupMonitoring()
    
    -- Log de inicialização
    print("Sistema de backup inicializado com sucesso")
end

-- Exemplo de backup manual
function manualBackupExample()
    print("Iniciando backup manual...")
    
    -- Criar backup completo
    local success = BackupSystem.createFullBackup("manual_backup")
    
    if success then
        print("Backup manual concluído com sucesso")
        
        -- Listar histórico de backups
        local history = BackupSystem.getBackupHistory()
        print("Histórico de backups:")
        for i, backup in ipairs(history) do
            print(string.format("  %d. %s (%s) - %s", i, backup.name, backup.type, backup.timestamp))
        end
```

#### Funcionalidade 1
```lua
    else
        print("ERRO: Falha no backup manual")
    end
end

-- Exemplo de restauração
function restoreExample()
    print("Iniciando restauração...")
    
    -- Listar backups disponíveis
    local history = BackupSystem.getBackupHistory()
    if #history == 0 then
        print("Nenhum backup disponível")
        return
    end
    
    -- Usar o backup mais recente
    local latestBackup = history[1]
    local backupPath = BackupSystem.config.storage.local.path .. latestBackup.name
    
    local success = BackupSystem.restoreFromBackup(backupPath)
    
    if success then
        print("Restauração concluída com sucesso")
        print("Backup restaurado: " .. latestBackup.name)
    else
        print("ERRO: Falha na restauração")
    end
```

#### Funcionalidade 2
```lua
end

-- Exemplo de rollback
function rollbackExample()
    print("Iniciando rollback...")
    
    -- Listar versões disponíveis
    local history = BackupSystem.getBackupHistory()
    if #history == 0 then
        print("Nenhuma versão disponível")
        return
    end
    
    -- Usar a versão anterior
    local previousVersion = history[2]  -- Segunda mais recente
    if previousVersion then
        local success = BackupSystem.rollbackToVersion(previousVersion.version)
        
        if success then
            print("Rollback concluído com sucesso")
            print("Versão restaurada: " .. previousVersion.version)
        else
            print("ERRO: Falha no rollback")
        end
```

#### Finalização
```lua
    else
        print("Nenhuma versão anterior disponível")
    end
end

-- Exemplo de limpeza
function cleanupExample()
    print("Iniciando limpeza de backups...")
    
    -- Limpar backups antigos
    BackupSystem.cleanupOldBackups()
    
    -- Verificar espaço usado
    local storageUsed = BackupSystem.calculateStorageUsed()
    print(string.format("Espaço usado: %.2f MB", storageUsed / (1024 * 1024)))
end
```

---

## ✅ Melhores Práticas

### 🎯 **Recomendações de Backup**

1. **Frequência de Backup**
   - Backup automático a cada hora
   - Backup manual antes de mudanças importantes
   - Backup completo semanal
   - Backup incremental diário

2. **Armazenamento**
   - Use múltiplos locais de armazenamento
   - Configure compressão para economizar espaço
   - Implemente rotação de backups
   - Monitore espaço disponível

3. **Validação**
   - Valide integridade dos backups
   - Teste restauração regularmente
   - Verifique checksums
   - Monitore logs de backup

4. **Segurança**
   - Use criptografia para dados sensíveis
   - Configure permissões adequadas
   - Mantenha backups offline
   - Implemente controle de acesso

### 🚨 **Considerações Importantes**

- **Espaço**: Monitore uso de espaço em disco
- **Performance**: Evite backup durante uso intensivo
- **Confiabilidade**: Teste restauração regularmente
- **Segurança**: Proteja backups contra acesso não autorizado

---

## 📊 Métricas e KPIs

### 📈 **Indicadores de Backup**

- **Backup Success Rate**: Taxa de sucesso dos backups (%)
- **Recovery Time**: Tempo de recuperação (minutos)
- **Storage Efficiency**: Eficiência de armazenamento (%)
- **Data Loss Risk**: Risco de perda de dados (baixo/médio/alto)
- **Backup Frequency**: Frequência de backups (por hora/dia)

### 🔍 **Relatórios de Backup**

#### Nível Basic
```json
{
  "timestamp": "2025-01-27T10:30:00Z",
  "metrics": {
    "totalBackups": 150,
    "successfulBackups": 145,
    "failedBackups": 5,
    "successRate": 96.7,
    "storageUsed": "2.5GB",
    "lastBackup": "2025-01-27T09:30:00Z"
  },
  "backups": [
    {
      "name": "full_20250127_093000",
      "type": "full",
      "size": "150MB",
      "status": "valid"
    }
  ],
  "sync": {
    "status": "synced",
    "lastSync": "2025-01-27T10:25:00Z"
  }
}
```

#### Nível Intermediate
```json
{
  "timestamp": "2025-01-27T10:30:00Z",
  "metrics": {
    "totalBackups": 150,
    "successfulBackups": 145,
    "failedBackups": 5,
    "successRate": 96.7,
    "storageUsed": "2.5GB",
    "lastBackup": "2025-01-27T09:30:00Z"
  },
  "backups": [
    {
      "name": "full_20250127_093000",
      "type": "full",
      "size": "150MB",
      "status": "valid"
    }
  ],
  "sync": {
    "status": "synced",
    "lastSync": "2025-01-27T10:25:00Z"
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
```json
{
  "timestamp": "2025-01-27T10:30:00Z",
  "metrics": {
    "totalBackups": 150,
    "successfulBackups": 145,
    "failedBackups": 5,
    "successRate": 96.7,
    "storageUsed": "2.5GB",
    "lastBackup": "2025-01-27T09:30:00Z"
  },
  "backups": [
    {
      "name": "full_20250127_093000",
      "type": "full",
      "size": "150MB",
      "status": "valid"
    }
  ],
  "sync": {
    "status": "synced",
    "lastSync": "2025-01-27T10:25:00Z"
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

---

**Story ID**: CORE-010  
**Categoria**: CORE  
**Status**: ✅ Completo  
**Última Atualização**: 2025-01-27 
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

