---
tags: [ui, upload, download, system, otclient, documentation, habdel]
type: documentation
status: completed
priority: maximum
created: 2025-01-27
---

# 📤📥 UI-020: Sistema de Upload/Download

> [!info] **Story ID**: UI-020  
> **Categoria**: UI  
> **Status**: ✅ Completo  
> **Prioridade**: 🔥 **MÁXIMA**

## 📋 Índice
1. [Visão Geral](#visão-geral)
2. [Arquitetura do Sistema](#arquitetura-do-sistema)
3. [Tipos de Upload/Download](#tipos-de-uploaddownload)
4. [API Lua](#api-lua)
5. [Exemplos Práticos](#exemplos-práticos)
6. [Melhores Práticas](#melhores-práticas)

---

## 🎯 Visão Geral

O **Sistema de Upload/Download** do OTClient oferece funcionalidades para transferir arquivos entre cliente e servidor, incluindo upload de imagens, download de recursos e sincronização de dados. O sistema é fundamental para interfaces que precisam gerenciar arquivos.

### 🎨 **Características Principais**

- **UIUploadWidget**: Widget para upload de arquivos
- **UIDownloadWidget**: Widget para download de arquivos
- **Progress Tracking**: Acompanhamento de progresso
- **File Validation**: Validação de tipos e tamanhos
- **Drag & Drop**: Suporte a arrastar e soltar
- **Multiple Files**: Upload/download múltiplo

---

## 🏗️ Arquitetura do Sistema

### 🎭 **Estrutura Hierárquica**

```
Sistema de Upload/Download
   │
   ├─ UIUploadWidget
   │   ├─ File Selection
   │   ├─ Drag & Drop Area
   │   ├─ Progress Bar
   │   ├─ File Validation
   │   └─ Upload Queue
   │
   ├─ UIDownloadWidget
   │   ├─ Download List
   │   ├─ Progress Tracking
   │   ├─ File Management
   │   ├─ Resume Support
   │   └─ Download Queue
   │
   ├─ File Management
   │   ├─ File Storage
   │   ├─ File Validation
   │   ├─ File Compression
   │   └─ File Security
   │
   └─ Network Layer
       ├─ HTTP Requests
       ├─ FTP Support
       ├─ WebSocket
       └─ Error Handling
```

---

## 📤📥 Tipos de Upload/Download

### 🎯 **UIUploadWidget**

```lua
-- Estrutura do UIUploadWidget
    --  Estrutura do UIUploadWidget (traduzido)
{
    allowedTypes = {'.jpg', '.png', '.gif'},
    maxFileSize = 1024 * 1024,  -- 1MB
    multipleFiles = true,
    dragDropEnabled = true,
    autoUpload = false
}
```

### 📥 **UIDownloadWidget**

```lua
-- Estrutura do UIDownloadWidget
    --  Estrutura do UIDownloadWidget (traduzido)
{
    downloadPath = '/downloads/',
    resumeDownloads = true,
    maxConcurrent = 3,
    showProgress = true
}
```

---

## 🐍 API Lua

### 📦 **Métodos de UIUploadWidget**

```lua
-- Criar widget de upload
    --  Criar widget de upload (traduzido)
local uploadWidget = g_ui.createWidget('UIUploadWidget', parent)

-- Configurar tipos permitidos
    --  Configurar tipos permitidos (traduzido)
uploadWidget:setAllowedTypes({'.jpg', '.png', '.gif'})

-- Configurar tamanho máximo
uploadWidget:setMaxFileSize(1024 * 1024)

-- Habilitar múltiplos arquivos
uploadWidget:setMultipleFiles(true)

-- Eventos
    --  Eventos (traduzido)
uploadWidget.onFileSelected = function(widget, files)
    print('Arquivos selecionados:', #files)
end

uploadWidget.onUploadProgress = function(widget, file, progress)
    print('Progresso:', progress .. '%')
end

uploadWidget.onUploadComplete = function(widget, file, response)
    print('Upload completo:', file.name)
end
```

### 🎯 **Métodos de UIDownloadWidget**

```lua
-- Criar widget de download
    --  Criar widget de download (traduzido)
local downloadWidget = g_ui.createWidget('UIDownloadWidget', parent)

-- Adicionar arquivo para download
    --  Adicionar arquivo para download (traduzido)
downloadWidget:addDownload(url, filename)

-- Pausar download
    --  Pausar download (traduzido)
downloadWidget:pauseDownload(downloadId)

-- Retomar download
    --  Retomar download (traduzido)
downloadWidget:resumeDownload(downloadId)

-- Eventos
    --  Eventos (traduzido)
downloadWidget.onDownloadProgress = function(widget, downloadId, progress)
    print('Download progresso:', progress .. '%')
end

downloadWidget.onDownloadComplete = function(widget, downloadId, filePath)
    print('Download completo:', filePath)
end
```

---

## 🚀 Exemplos Práticos

### 📤 **Sistema de Upload de Imagens**

#### Inicialização e Configuração
```lua
-- Sistema de upload de imagens
local ImageUploader = {}

function ImageUploader.create(parent)
    local window = g_ui.createWidget('MainWindow', parent)
    window:setId('imageUploader')
    window:setText('Upload de Imagens')
    window:setSize({width = 400, height = 300})
    
    -- Widget de upload
    local uploadWidget = g_ui.createWidget('UIUploadWidget', window)
    uploadWidget:setPosition({x = 10, y = 30})
    uploadWidget:setSize({width = 380, height = 200})
    
    -- Configurar upload
    uploadWidget:setAllowedTypes({'.jpg', '.jpeg', '.png', '.gif'})
    uploadWidget:setMaxFileSize(5 * 1024 * 1024)  -- 5MB
    uploadWidget:setMultipleFiles(true)
    uploadWidget:setDragDropEnabled(true)
    
    -- Eventos
    uploadWidget.onFileSelected = function(widget, files)
        ImageUploader.handleFileSelection(files)
    end
```

#### Funcionalidade 1
```lua
    
    uploadWidget.onUploadProgress = function(widget, file, progress)
        ImageUploader.updateProgress(file, progress)
    end
    
    uploadWidget.onUploadComplete = function(widget, file, response)
        ImageUploader.handleUploadComplete(file, response)
    end
    
    return window
end

function ImageUploader.handleFileSelection(files)
    print('Arquivos selecionados:', #files)
    for _, file in ipairs(files) do
        print('Arquivo:', file.name, 'Tamanho:', file.size)
    end
end

function ImageUploader.updateProgress(file, progress)
    print('Progresso de', file.name, ':', progress .. '%')
end
```

#### Finalização
```lua

function ImageUploader.handleUploadComplete(file, response)
    print('Upload completo:', file.name)
    if response.success then
        print('URL da imagem:', response.url)
    else
        print('Erro no upload:', response.error)
    end
end

-- Uso
local uploader = ImageUploader.create(parent)
```

### 📥 **Sistema de Download de Recursos**

#### Inicialização e Configuração
```lua
-- Sistema de download de recursos
local ResourceDownloader = {}

function ResourceDownloader.create(parent)
    local window = g_ui.createWidget('MainWindow', parent)
    window:setId('resourceDownloader')
    window:setText('Download de Recursos')
    window:setSize({width = 500, height = 400})
    
    -- Widget de download
    local downloadWidget = g_ui.createWidget('UIDownloadWidget', window)
    downloadWidget:setPosition({x = 10, y = 30})
    downloadWidget:setSize({width = 480, height = 360})
    
    -- Configurar download
    downloadWidget:setDownloadPath('/resources/')
    downloadWidget:setResumeDownloads(true)
    downloadWidget:setMaxConcurrent(3)
    downloadWidget:setShowProgress(true)
    
    -- Eventos
    downloadWidget.onDownloadProgress = function(widget, downloadId, progress)
        ResourceDownloader.updateProgress(downloadId, progress)
    end
```

#### Funcionalidade 1
```lua
    
    downloadWidget.onDownloadComplete = function(widget, downloadId, filePath)
        ResourceDownloader.handleDownloadComplete(downloadId, filePath)
    end
    
    downloadWidget.onDownloadError = function(widget, downloadId, error)
        ResourceDownloader.handleDownloadError(downloadId, error)
    end
    
    return window
end

function ResourceDownloader.addResource(url, filename)
    downloadWidget:addDownload(url, filename)
end

function ResourceDownloader.updateProgress(downloadId, progress)
    print('Download', downloadId, 'progresso:', progress .. '%')
end

function ResourceDownloader.handleDownloadComplete(downloadId, filePath)
```

#### Finalização
```lua
    print('Download completo:', downloadId, '->', filePath)
end

function ResourceDownloader.handleDownloadError(downloadId, error)
    print('Erro no download:', downloadId, '->', error)
end

-- Uso
local downloader = ResourceDownloader.create(parent)
ResourceDownloader.addResource('https://example.com/texture.png', 'texture.png')
ResourceDownloader.addResource('https://example.com/sound.mp3', 'sound.mp3')
```

---

## ✅ Melhores Práticas

### 🎯 **Performance**

```lua
-- ✅ BOM: Usar chunks para arquivos grandes
    --  ✅ BOM: Usar chunks para arquivos grandes (traduzido)
function uploadLargeFile(file, chunkSize)
    -- Função: uploadLargeFile
    chunkSize = chunkSize or 1024 * 1024  -- 1MB chunks
    
    for i = 1, math.ceil(file.size / chunkSize) do
    -- Loop de repetição
        local start = (i - 1) * chunkSize + 1
        local end_pos = math.min(i * chunkSize, file.size)
        local chunk = file:read(start, end_pos)
        
        uploadChunk(file.name, i, chunk)
    end
end

-- ✅ BOM: Implementar retry automático
function downloadWithRetry(url, filename, maxRetries)
    -- Função: downloadWithRetry
    maxRetries = maxRetries or 3
    
    local function attemptDownload(attempt)
        downloadWidget:addDownload(url, filename)
        
        downloadWidget.onDownloadError = function(widget, downloadId, error)
            if attempt < maxRetries then
    -- Verificação condicional
                print('Tentativa', attempt, 'falhou, tentando novamente...')
                scheduleEvent(function() attemptDownload(attempt + 1) end, 1000)
            else
                print('Download falhou após', maxRetries, 'tentativas')
            end
        end
    end
    
    attemptDownload(1)
end
```

### 🎨 **Design**

```lua
-- ✅ BOM: Usar constantes para configuração
local UPLOAD_CONFIG = {
    MAX_FILE_SIZE = 10 * 1024 * 1024,  -- 10MB
    ALLOWED_TYPES = {'.jpg', '.png', '.gif', '.pdf'},
    CHUNK_SIZE = 1024 * 1024,  -- 1MB
    MAX_RETRIES = 3
}

-- ✅ BOM: Implementar validação robusta
function validateFile(file)
    -- Função: validateFile
    -- Verificar tipo
    --  Verificar tipo (traduzido)
    local isValidType = false
    for _, allowedType in ipairs(UPLOAD_CONFIG.ALLOWED_TYPES) do
    -- Loop de repetição
        if string.lower(file.name):endsWith(allowedType) then
    -- Verificação condicional
            isValidType = true
            break
        end
    end
    
    if not isValidType then
    -- Verificação condicional
        return false, 'Tipo de arquivo não permitido'
    end
    
    -- Verificar tamanho
    --  Verificar tamanho (traduzido)
    if file.size > UPLOAD_CONFIG.MAX_FILE_SIZE then
    -- Verificação condicional
        return false, 'Arquivo muito grande'
    end
    
    return true, 'Arquivo válido'
end
```

O Sistema de Upload/Download do OTClient oferece ferramentas completas para transferir arquivos de forma segura e eficiente. Use estas práticas para garantir performance e confiabilidade.

> - [[UIWidget_Reference]] - Referência completa de widgets
> - [[UIDragDrop]] - Sistema de drag & drop
> - [[UIEvents]] - Sistema de eventos 
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

