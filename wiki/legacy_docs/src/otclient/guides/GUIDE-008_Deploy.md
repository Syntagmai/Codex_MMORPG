
# 🚀 Guia de Deploy - OTClient

## 🎯 **Visão Geral**

Este guia fornece informações detalhadas sobre o processo de deploy do OTClient, incluindo build, distribuição, release management e automação para desenvolvedores e agentes de IA.

## 📚 **Pré-requisitos**

- ✅ Conhecimento básico do OTClient
- ✅ Familiaridade com CMake
- ✅ Compreensão de sistemas de build
- ✅ Conhecimento de distribuição de software

---

## 🔨 **1. Sistema de Build**

### **1.1 Build Manager**

#### Inicialização e Configuração
```lua
-- Gerenciador de build
local BuildManager = {
    platforms = {
        windows = "win32",
        linux = "linux",
        macos = "darwin",
        android = "android"
    },
    configurations = {
        debug = "Debug",
        release = "Release",
        relwithdebinfo = "RelWithDebInfo",
        minsizerel = "MinSizeRel"
    },
    targets = {
        client = "otclient",
        server = "otserver",
        tools = "tools"
    }
}

function BuildManager:build(platform, configuration, target)
```

#### Funcionalidade 1
```lua
    local buildDir = self:getBuildDirectory(platform, configuration)
    local sourceDir = self:getSourceDirectory()
    
    -- Criar diretório de build se não existir
    if not self:directoryExists(buildDir) then
        self:createDirectory(buildDir)
    end
    
    -- Configurar CMake
    local cmakeCommand = self:generateCMakeCommand(platform, configuration, sourceDir, buildDir)
    local success = self:executeCommand(cmakeCommand)
    
    if not success then
        return false, "Falha na configuração CMake"
    end
    
    -- Compilar
    local makeCommand = self:generateMakeCommand(platform, target, buildDir)
    success = self:executeCommand(makeCommand)
    
    if not success then
        return false, "Falha na compilação"
    end
```

#### Funcionalidade 2
```lua
    
    return true
end

function BuildManager:getBuildDirectory(platform, configuration)
    return string.format("build/%s/%s", platform, configuration:lower())
end

function BuildManager:getSourceDirectory()
    return "."
end

function BuildManager:generateCMakeCommand(platform, configuration, sourceDir, buildDir)
    local cmakeArgs = {
        "-S", sourceDir,
        "-B", buildDir,
        "-DCMAKE_BUILD_TYPE=" .. configuration,
        "-DCMAKE_TOOLCHAIN_FILE=" .. self:getToolchainFile(platform)
    }
    
    -- Adicionar flags específicas da plataforma
    if platform == "windows" then
        table.insert(cmakeArgs, "-G")
        table.insert(cmakeArgs, "Visual Studio 17 2022")
        table.insert(cmakeArgs, "-A")
        table.insert(cmakeArgs, "x64")
    elseif platform == "android" then
        table.insert(cmakeArgs, "-DANDROID_ABI=arm64-v8a")
        table.insert(cmakeArgs, "-DANDROID_PLATFORM=android-21")
    end
```

#### Funcionalidade 3
```lua
    
    return "cmake " .. table.concat(cmakeArgs, " ")
end

function BuildManager:generateMakeCommand(platform, target, buildDir)
    if platform == "windows" then
        return string.format("cmake --build %s --target %s --config Release", buildDir, target)
    else
        return string.format("make -C %s %s", buildDir, target)
    end
end

function BuildManager:getToolchainFile(platform)
    local toolchainFiles = {
        android = "cmake/android.toolchain.cmake",
        windows = "cmake/windows.toolchain.cmake",
        linux = "cmake/linux.toolchain.cmake",
        macos = "cmake/macos.toolchain.cmake"
    }
    
    return toolchainFiles[platform] or ""
end
```

#### Finalização
```lua

function BuildManager:executeCommand(command)
    -- Implementar execução de comando
    local result = os.execute(command)
    return result == 0
end

function BuildManager:directoryExists(path)
    local file = io.open(path .. "/.exists", "r")
    if file then
        file:close()
        return true
    end
    return false
end

function BuildManager:createDirectory(path)
    os.execute("mkdir -p " .. path)
end
```

### **1.2 Build Configuration**

#### Inicialização e Configuração
```lua
-- Configuração de build
local BuildConfig = {
    default = {
        cmake_minimum_required = "3.16",
        project_name = "OTClient",
        cpp_standard = "17",
        build_type = "Release",
        enable_tests = true,
        enable_docs = true
    },
    
    platforms = {
        windows = {
            compiler = "MSVC",
            arch = "x64",
            sdk_version = "10.0.19041.0",
            vcpkg_toolchain = true
        },
        
        linux = {
            compiler = "GCC",
            arch = "x64",
            pkg_config = true,
            system_libs = {"SDL2", "OpenGL", "ALSA"}
        },
```

#### Funcionalidade 1
```lua
        
        macos = {
            compiler = "Clang",
            arch = "x64",
            sdk_version = "10.15",
            frameworks = {"Cocoa", "OpenGL", "CoreAudio"}
        },
        
        android = {
            compiler = "Clang",
            arch = "arm64-v8a",
            api_level = 21,
            ndk_version = "25.1.8937393"
        }
    }
}

function BuildConfig:generateCMakeLists(platform, config)
    local cmakeContent = string.format([
cmake_minimum_required(VERSION %s)
project(%s)

set(CMAKE_CXX_STANDARD %s)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_BUILD_TYPE %s)
set(BUILD_TESTS %s)
set(BUILD_DOCS %s)

](
cmake_minimum_required(VERSION %s)
project(%s)

set(CMAKE_CXX_STANDARD %s)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_BUILD_TYPE %s)
set(BUILD_TESTS %s)
set(BUILD_DOCS %s)

.md), 
        config.cmake_minimum_required,
        config.project_name,
        config.cpp_standard,
        config.build_type,
        config.enable_tests and "ON" or "OFF",
        config.enable_docs and "ON" or "OFF"
    )
    
    -- Adicionar configurações específicas da plataforma
    local platformConfig = self.platforms[platform]
    if platformConfig then
        cmakeContent = cmakeContent .. self:generatePlatformConfig(platformConfig)
    end
```

#### Funcionalidade 2
```lua
    
    -- Adicionar targets
    cmakeContent = cmakeContent .. self:generateTargets()
    
    return cmakeContent
end

function BuildConfig:generatePlatformConfig(platformConfig)
    local config = ""
    
    if platformConfig.compiler then
        config = config .. string.format("set(CMAKE_CXX_COMPILER %s)\n", platformConfig.compiler)
    end
    
    if platformConfig.arch then
        config = config .. string.format("set(CMAKE_SYSTEM_PROCESSOR %s)\n", platformConfig.arch)
    end
    
    if platformConfig.system_libs then
        for _, lib in ipairs(platformConfig.system_libs) do
            config = config .. string.format("find_package(%s REQUIRED)\n", lib)
        end
```

#### Funcionalidade 3
```lua
    end
    
    return config
end

function BuildConfig:generateTargets()
    return [
# Targets
add_executable(otclient src/main.cpp)
target_link_libraries(otclient ${LIBS})

if(BUILD_TESTS)
    enable_testing()
    add_subdirectory(tests)
endif()

if(BUILD_DOCS)
    add_subdirectory(docs)
endif()
](
# Targets
add_executable(otclient src/main.cpp)
target_link_libraries(otclient ${LIBS})

if(BUILD_TESTS)
    enable_testing()
    add_subdirectory(tests)
endif()
```

#### Finalização
```lua

if(BUILD_DOCS)
    add_subdirectory(docs)
endif()
.md)
end
```

---

## 📦 **2. Sistema de Packaging**

### **2.1 Package Manager**

#### Inicialização e Configuração
```lua
-- Gerenciador de pacotes
local PackageManager = {
    formats = {
        windows = {"exe", "msi", "zip"},
        linux = {"deb", "rpm", "tar.gz", "AppImage"},
        macos = {"dmg", "pkg", "tar.gz"},
        android = {"apk", "aab"}
    },
    dependencies = {
        windows = {"vcredist", "directx", "opengl"},
        linux = {"libsdl2", "libopengl", "libasound"},
        macos = {"sdl2", "opengl", "coreaudio"},
        android = {"android-sdk", "android-ndk"}
    }
}

function PackageManager:createPackage(platform, format, buildDir)
    local packageDir = self:getPackageDirectory(platform, format)
    
    -- Criar diretório de pacote
    self:createDirectory(packageDir)
    
    -- Copiar arquivos do build
    self:copyBuildFiles(buildDir, packageDir)
    
    -- Adicionar dependências
    self:addDependencies(platform, packageDir)
    
    -- Adicionar recursos
    self:addResources(packageDir)
    
    -- Criar pacote final
    return self:createFinalPackage(platform, format, packageDir)
end
```

#### Funcionalidade 1
```lua

function PackageManager:getPackageDirectory(platform, format)
    return string.format("packages/%s/%s", platform, format)
end

function PackageManager:copyBuildFiles(buildDir, packageDir)
    local files = {
        "otclient.exe",
        "otclient",
        "*.dll",
        "*.so",
        "*.dylib"
    }
    
    for _, file in ipairs(files) do
        local command = string.format("cp %s/%s %s/", buildDir, file, packageDir)
        self:executeCommand(command)
    end
end

function PackageManager:addDependencies(platform, packageDir)
```

#### Funcionalidade 2
```lua
    local deps = self.dependencies[platform]
    if not deps then return end
    
    for _, dep in ipairs(deps) do
        local depPath = self:findDependency(dep)
        if depPath then
            local command = string.format("cp -r %s %s/", depPath, packageDir)
            self:executeCommand(command)
        end
    end
end

function PackageManager:addResources(packageDir)
    local resources = {
        "data/",
        "modules/",
        "docs/",
        "README.md",
        "LICENSE"
    }
    
    for _, resource in ipairs(resources) do
        if self:fileExists(resource) then
            local command = string.format("cp -r %s %s/", resource, packageDir)
            self:executeCommand(command)
        end
```

#### Funcionalidade 3
```lua
    end
end

function PackageManager:createFinalPackage(platform, format, packageDir)
    local outputFile = string.format("otclient-%s-%s.%s", 
        self:getVersion(), platform, format)
    
    if format == "zip" then
        return self:createZipPackage(packageDir, outputFile)
    elseif format == "tar.gz" then
        return self:createTarGzPackage(packageDir, outputFile)
    elseif format == "deb" then
        return self:createDebPackage(packageDir, outputFile)
    elseif format == "rpm" then
        return self:createRpmPackage(packageDir, outputFile)
    elseif format == "msi" then
        return self:createMsiPackage(packageDir, outputFile)
    elseif format == "dmg" then
        return self:createDmgPackage(packageDir, outputFile)
    elseif format == "apk" then
        return self:createApkPackage(packageDir, outputFile)
    end
```

#### Funcionalidade 4
```lua
    
    return false, "Formato de pacote não suportado"
end

function PackageManager:createZipPackage(packageDir, outputFile)
    local command = string.format("cd %s && zip -r ../%s .", packageDir, outputFile)
    return self:executeCommand(command)
end

function PackageManager:createTarGzPackage(packageDir, outputFile)
    local command = string.format("cd %s && tar -czf ../%s .", packageDir, outputFile)
    return self:executeCommand(command)
end

function PackageManager:createDebPackage(packageDir, outputFile)
    -- Implementar criação de pacote DEB
    local controlFile = self:generateDebControl()
    local command = string.format("dpkg-deb --build %s %s", packageDir, outputFile)
    return self:executeCommand(command)
end

function PackageManager:generateDebControl()
```

#### Funcionalidade 5
```lua
    return [
Package: otclient
Version: ](
Package: otclient
Version: .md) .. self:getVersion() .. [
Architecture: amd64
Maintainer: OTClient Team <team@otclient.org>
Description: Open Tibia Client
 A modern, feature-rich client for Open Tibia servers.
](
Architecture: amd64
Maintainer: OTClient Team <team@otclient.org>
Description: Open Tibia Client
 A modern, feature-rich client for Open Tibia servers.
.md)
end

function PackageManager:getVersion()
    -- Ler versão do arquivo de configuração
    local versionFile = io.open("VERSION", "r")
    if versionFile then
        local version = versionFile:read("*line")
        versionFile:close()
        return version or "1.0.0"
    end
```

#### Funcionalidade 6
```lua
    return "1.0.0"
end

function PackageManager:findDependency(depName)
    -- Implementar busca de dependências
    local searchPaths = {
        "/usr/lib",
        "/usr/local/lib",
        "/opt",
        "deps"
    }
    
    for _, path in ipairs(searchPaths) do
        local depPath = path .. "/" .. depName
        if self:fileExists(depPath) then
            return depPath
        end
    end
    
    return nil
end
```

#### Finalização
```lua

function PackageManager:fileExists(path)
    local file = io.open(path, "r")
    if file then
        file:close()
        return true
    end
    return false
end

function PackageManager:executeCommand(command)
    local result = os.execute(command)
    return result == 0
end
```

### **2.2 Installer Generator**

#### Inicialização e Configuração
```lua
-- Gerador de instaladores
local InstallerGenerator = {
    installers = {
        windows = "nsis",
        linux = "makeself",
        macos = "pkgbuild",
        android = "gradle"
    }
}

function InstallerGenerator:createInstaller(platform, packageDir, outputFile)
    local installerType = self.installers[platform]
    
    if installerType == "nsis" then
        return self:createNsisInstaller(packageDir, outputFile)
    elseif installerType == "makeself" then
        return self:createMakeselfInstaller(packageDir, outputFile)
    elseif installerType == "pkgbuild" then
        return self:createPkgbuildInstaller(packageDir, outputFile)
    elseif installerType == "gradle" then
        return self:createGradleInstaller(packageDir, outputFile)
    end
```

#### Funcionalidade 1
```lua
    
    return false, "Tipo de instalador não suportado"
end

function InstallerGenerator:createNsisInstaller(packageDir, outputFile)
    local nsisScript = self:generateNsisScript(packageDir)
    local scriptFile = "installer.nsi"
    
    -- Salvar script NSIS
    local file = io.open(scriptFile, "w")
    if file then
        file:write(nsisScript)
        file:close()
    end
    
    -- Compilar instalador
    local command = string.format("makensis %s", scriptFile)
    return self:executeCommand(command)
end

function InstallerGenerator:generateNsisScript(packageDir)
```

#### Funcionalidade 2
```lua
    return string.format([
!include "MUI2.nsh"

Name "OTClient"
OutFile "otclient-installer.exe"
InstallDir "$PROGRAMFILES\\OTClient"

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_LANGUAGE "Portuguese"

Section "Install"
    SetOutPath "$INSTDIR"
    File /r "%s\\*.*"
    
    WriteUninstaller "$INSTDIR\\uninstall.exe"
    
    CreateDirectory "$SMPROGRAMS\\OTClient"
    CreateShortCut "$SMPROGRAMS\\OTClient\\OTClient.lnk" "$INSTDIR\\otclient.exe"
    CreateShortCut "$DESKTOP\\OTClient.lnk" "$INSTDIR\\otclient.exe"
    
    WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\OTClient" \
                     "DisplayName" "OTClient"
    WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\OTClient" \
                     "UninstallString" "$INSTDIR\\uninstall.exe"
SectionEnd

Section "Uninstall"
    Delete "$INSTDIR\\uninstall.exe"
    RMDir /r "$INSTDIR"
    
    Delete "$SMPROGRAMS\\OTClient\\OTClient.lnk"
    RMDir "$SMPROGRAMS\\OTClient"
    Delete "$DESKTOP\\OTClient.lnk"
    
    DeleteRegKey HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\OTClient"
SectionEnd
](
!include "MUI2.nsh"

Name "OTClient"
OutFile "otclient-installer.exe"
InstallDir "$PROGRAMFILES\\OTClient"

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_LANGUAGE "Portuguese"

Section "Install"
    SetOutPath "$INSTDIR"
    File /r "%s\\*.*"
    
    WriteUninstaller "$INSTDIR\\uninstall.exe"
    
    CreateDirectory "$SMPROGRAMS\\OTClient"
    CreateShortCut "$SMPROGRAMS\\OTClient\\OTClient.lnk" "$INSTDIR\\otclient.exe"
    CreateShortCut "$DESKTOP\\OTClient.lnk" "$INSTDIR\\otclient.exe"
    
    WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\OTClient" \
                     "DisplayName" "OTClient"
    WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\OTClient" \
                     "UninstallString" "$INSTDIR\\uninstall.exe"
SectionEnd

Section "Uninstall"
    Delete "$INSTDIR\\uninstall.exe"
    RMDir /r "$INSTDIR"
    
    Delete "$SMPROGRAMS\\OTClient\\OTClient.lnk"
    RMDir "$SMPROGRAMS\\OTClient"
    Delete "$DESKTOP\\OTClient.lnk"
    
    DeleteRegKey HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\OTClient"
SectionEnd
.md), packageDir)
end
```

#### Funcionalidade 3
```lua

function InstallerGenerator:createMakeselfInstaller(packageDir, outputFile)
    local command = string.format("makeself %s %s 'OTClient Installer' ./install.sh", 
        packageDir, outputFile)
    return self:executeCommand(command)
end

function InstallerGenerator:createPkgbuildInstaller(packageDir, outputFile)
    local pkgScript = self:generatePkgbuildScript(packageDir)
    local command = string.format("pkgbuild --root %s --identifier org.otclient.client --version %s %s", 
        packageDir, self:getVersion(), outputFile)
    return self:executeCommand(command)
end

function InstallerGenerator:generatePkgbuildScript(packageDir)
    return string.format([
#!/bin/bash
# OTClient Package Builder

PACKAGE_NAME="OTClient"
PACKAGE_VERSION="%s"
PACKAGE_ID="org.otclient.client"
INSTALL_DIR="/Applications/OTClient"

# Criar estrutura de diretórios
mkdir -p "$INSTALL_DIR"

# Copiar arquivos
cp -r %s/* "$INSTDIR/"

# Definir permissões
chmod +x "$INSTDIR/otclient"

echo "Package created successfully"
](
#!/bin/bash
# OTClient Package Builder

PACKAGE_NAME="OTClient"
PACKAGE_VERSION="%s"
PACKAGE_ID="org.otclient.client"
INSTALL_DIR="/Applications/OTClient"

# Criar estrutura de diretórios
mkdir -p "$INSTALL_DIR"

# Copiar arquivos
cp -r %s/* "$INSTDIR/"

# Definir permissões
chmod +x "$INSTDIR/otclient"

echo "Package created successfully"
.md), self:getVersion(), packageDir)
end
```

#### Finalização
```lua

function InstallerGenerator:executeCommand(command)
    local result = os.execute(command)
    return result == 0
end

function InstallerGenerator:getVersion()
    local versionFile = io.open("VERSION", "r")
    if versionFile then
        local version = versionFile:read("*line")
        versionFile:close()
        return version or "1.0.0"
    end
    return "1.0.0"
end
```

---

## 🚀 **3. Sistema de Release**

### **3.1 Release Manager**

#### Inicialização e Configuração
```lua
-- Gerenciador de releases
local ReleaseManager = {
    releases = {},
    channels = {
        stable = "stable",
        beta = "beta",
        alpha = "alpha",
        nightly = "nightly"
    }
}

function ReleaseManager:createRelease(version, channel, packages)
    local release = {
        version = version,
        channel = channel,
        packages = packages,
        timestamp = os.time(),
        changelog = self:generateChangelog(version),
        checksums = self:calculateChecksums(packages)
    }
    
    table.insert(self.releases, release)
    
    -- Salvar release
    self:saveRelease(release)
    
    -- Notificar sobre novo release
    self:notifyRelease(release)
    
    return release
end
```

#### Funcionalidade 1
```lua

function ReleaseManager:generateChangelog(version)
    local changelog = ""
    
    -- Ler changelog do arquivo
    local changelogFile = io.open("CHANGELOG.md", "r")
    if changelogFile then
        local content = changelogFile:read("*all")
        changelogFile:close()
        
        -- Extrair seção da versão
        local pattern = string.format("## %s[^#]*", version)
        local match = string.match(content, pattern)
        if match then
            changelog = match
        end
    end
    
    return changelog
end

function ReleaseManager:calculateChecksums(packages)
```

#### Funcionalidade 2
```lua
    local checksums = {}
    
    for _, package in ipairs(packages) do
        local checksum = self:calculateFileChecksum(package)
        checksums[package] = checksum
    end
    
    return checksums
end

function ReleaseManager:calculateFileChecksum(filePath)
    -- Implementar cálculo de checksum (SHA256)
    local command = string.format("sha256sum %s", filePath)
    local handle = io.popen(command)
    if handle then
        local result = handle:read("*line")
        handle:close()
        return result and string.match(result, "([%x]+)") or ""
    end
    return ""
end
```

#### Funcionalidade 3
```lua

function ReleaseManager:saveRelease(release)
    local releaseFile = string.format("releases/release-%s.json", release.version)
    
    local file = io.open(releaseFile, "w")
    if file then
        file:write(self:serializeRelease(release))
        file:close()
    end
end

function ReleaseManager:serializeRelease(release)
    local json = {
        version = release.version,
        channel = release.channel,
        timestamp = release.timestamp,
        packages = release.packages,
        changelog = release.changelog,
        checksums = release.checksums
    }
    
    -- Converter para JSON (implementação simplificada)
    return string.format([
{
    "version": "%s",
    "channel": "%s",
    "timestamp": %d,
    "packages": %s,
    "changelog": "%s",
    "checksums": %s
}
```

#### Funcionalidade 4
```lua
](
{
    "version": "%s",
    "channel": "%s",
    "timestamp": %d,
    "packages": %s,
    "changelog": "%s",
    "checksums": %s
}
.md), 
        json.version,
        json.channel,
        json.timestamp,
        self:serializeTable(json.packages),
        json.changelog:gsub('"', '\\"'),
        self:serializeTable(json.checksums)
    )
end

function ReleaseManager:serializeTable(tbl)
    local items = {}
    for k, v in pairs(tbl) do
        table.insert(items, string.format('"%s": "%s"', k, v))
    end
```

#### Funcionalidade 5
```lua
    return "{" .. table.concat(items, ", ") .. "}"
end

function ReleaseManager:notifyRelease(release)
    -- Notificar sobre novo release
    local message = string.format("Novo release disponível: %s (%s)", 
        release.version, release.channel)
    
    -- Enviar notificação (implementação específica)
    self:sendNotification(message, release)
end

function ReleaseManager:sendNotification(message, release)
    -- Implementar envio de notificação
    -- Pode ser email, webhook, etc.
    print("NOTIFICATION: " .. message)
end

function ReleaseManager:getLatestRelease(channel)
    local latest = nil
    
    for _, release in ipairs(self.releases) do
        if release.channel == channel then
            if not latest or self:compareVersions(release.version, latest.version) > 0 then
                latest = release
            end
```

#### Funcionalidade 6
```lua
        end
    end
    
    return latest
end

function ReleaseManager:compareVersions(version1, version2)
    local v1Parts = self:parseVersion(version1)
    local v2Parts = self:parseVersion(version2)
    
    for i = 1, math.max(#v1Parts, #v2Parts) do
        local v1 = v1Parts[i] or 0
        local v2 = v2Parts[i] or 0
        
        if v1 > v2 then
            return 1
        elseif v1 < v2 then
            return -1
        end
    end
    
    return 0
end
```

#### Finalização
```lua

function ReleaseManager:parseVersion(version)
    local parts = {}
    for part in string.gmatch(version, "(%d+)") do
        table.insert(parts, tonumber(part))
    end
    return parts
end
```

### **3.2 Update Manager**

#### Inicialização e Configuração
```lua
-- Gerenciador de atualizações
local UpdateManager = {
    updateUrl = "https://releases.otclient.org",
    currentVersion = "1.0.0",
    updateChannel = "stable"
}

function UpdateManager:checkForUpdates()
    local latestRelease = self:getLatestRelease()
    
    if not latestRelease then
        return false, "Não foi possível verificar atualizações"
    end
    
    if self:compareVersions(latestRelease.version, self.currentVersion) > 0 then
        return true, latestRelease
    end
    
    return false, "Já está na versão mais recente"
end

function UpdateManager:getLatestRelease()
```

#### Funcionalidade 1
```lua
    local url = string.format("%s/latest-%s.json", self.updateUrl, self.updateChannel)
    
    -- Fazer requisição HTTP (implementação simplificada)
    local response = self:httpGet(url)
    if response then
        return self:parseReleaseJson(response)
    end
    
    return nil
end

function UpdateManager:httpGet(url)
    -- Implementar requisição HTTP
    local command = string.format("curl -s %s", url)
    local handle = io.popen(command)
    if handle then
        local response = handle:read("*all")
        handle:close()
        return response
    end
    return nil
end
```

#### Funcionalidade 2
```lua

function UpdateManager:parseReleaseJson(json)
    -- Implementar parsing de JSON (simplificado)
    local release = {}
    
    -- Extrair informações básicas
    release.version = string.match(json, '"version":%s*"([^"]+)"')
    release.channel = string.match(json, '"channel":%s*"([^"]+)"')
    release.timestamp = tonumber(string.match(json, '"timestamp":%s*(%d+)'))
    
    return release
end

function UpdateManager:downloadUpdate(release)
    local platform = self:getCurrentPlatform()
    local package = release.packages[platform]
    
    if not package then
        return false, "Pacote não disponível para esta plataforma"
    end
    
    local downloadUrl = string.format("%s/%s", self.updateUrl, package)
    local localPath = string.format("downloads/%s", package)
    
    -- Criar diretório de downloads
    self:createDirectory("downloads")
    
    -- Download do arquivo
    local success = self:downloadFile(downloadUrl, localPath)
    
    if success then
        -- Verificar checksum
        local expectedChecksum = release.checksums[package]
        local actualChecksum = self:calculateFileChecksum(localPath)
        
        if expectedChecksum == actualChecksum then
            return true, localPath
        else
            return false, "Checksum inválido"
        end
```

#### Funcionalidade 3
```lua
    end
    
    return false, "Falha no download"
end

function UpdateManager:downloadFile(url, localPath)
    local command = string.format("curl -L -o %s %s", localPath, url)
    local result = os.execute(command)
    return result == 0
end

function UpdateManager:installUpdate(packagePath)
    local platform = self:getCurrentPlatform()
    
    if platform == "windows" then
        return self:installWindowsUpdate(packagePath)
    elseif platform == "linux" then
        return self:installLinuxUpdate(packagePath)
    elseif platform == "macos" then
        return self:installMacosUpdate(packagePath)
    end
```

#### Funcionalidade 4
```lua
    
    return false, "Plataforma não suportada"
end

function UpdateManager:installWindowsUpdate(packagePath)
    -- Implementar instalação no Windows
    local command = string.format("msiexec /i %s /quiet", packagePath)
    return os.execute(command) == 0
end

function UpdateManager:installLinuxUpdate(packagePath)
    -- Implementar instalação no Linux
    if string.match(packagePath, "%.deb$") then
        local command = string.format("sudo dpkg -i %s", packagePath)
        return os.execute(command) == 0
    elseif string.match(packagePath, "%.rpm$") then
        local command = string.format("sudo rpm -i %s", packagePath)
        return os.execute(command) == 0
    end
    
    return false, "Formato de pacote não suportado"
end
```

#### Funcionalidade 5
```lua

function UpdateManager:installMacosUpdate(packagePath)
    -- Implementar instalação no macOS
    if string.match(packagePath, "%.pkg$") then
        local command = string.format("sudo installer -pkg %s -target /", packagePath)
        return os.execute(command) == 0
    end
    
    return false, "Formato de pacote não suportado"
end

function UpdateManager:getCurrentPlatform()
    local platform = os.getenv("OS")
    if platform == "Windows_NT" then
        return "windows"
    elseif os.getenv("OSTYPE") == "darwin" then
        return "macos"
    else
        return "linux"
    end
end
```

#### Funcionalidade 6
```lua

function UpdateManager:createDirectory(path)
    os.execute("mkdir -p " .. path)
end

function UpdateManager:calculateFileChecksum(filePath)
    local command = string.format("sha256sum %s", filePath)
    local handle = io.popen(command)
    if handle then
        local result = handle:read("*line")
        handle:close()
        return result and string.match(result, "([%x]+)") or ""
    end
    return ""
end

function UpdateManager:compareVersions(version1, version2)
    local v1Parts = self:parseVersion(version1)
    local v2Parts = self:parseVersion(version2)
    
    for i = 1, math.max(#v1Parts, #v2Parts) do
        local v1 = v1Parts[i] or 0
        local v2 = v2Parts[i] or 0
        
        if v1 > v2 then
            return 1
        elseif v1 < v2 then
            return -1
        end
```

#### Finalização
```lua
    end
    
    return 0
end

function UpdateManager:parseVersion(version)
    local parts = {}
    for part in string.gmatch(version, "(%d+)") do
        table.insert(parts, tonumber(part))
    end
    return parts
end
```

---

## 🤖 **4. Automação de Deploy**

### **4.1 CI/CD Pipeline**

#### Inicialização e Configuração
```lua
-- Pipeline de CI/CD
local CICDPipeline = {
    stages = {
        build = "build",
        test = "test",
        package = "package",
        deploy = "deploy"
    },
    triggers = {
        push = "push",
        pull_request = "pull_request",
        tag = "tag",
        manual = "manual"
    }
}

function CICDPipeline:runPipeline(trigger, branch, commit)
    local pipeline = {
        trigger = trigger,
        branch = branch,
        commit = commit,
        stages = {},
        status = "running",
        startTime = os.time()
    }
```

#### Funcionalidade 1
```lua
    
    -- Executar estágios
    for _, stage in ipairs(self.stages) do
        local stageResult = self:runStage(stage, pipeline)
        
        pipeline.stages[stage] = {
            status = stageResult.success and "success" or "failed",
            output = stageResult.output,
            duration = stageResult.duration
        }
        
        if not stageResult.success then
            pipeline.status = "failed"
            break
        end
    end
    
    if pipeline.status == "running" then
        pipeline.status = "success"
    end
    
    pipeline.endTime = os.time()
    pipeline.duration = pipeline.endTime - pipeline.startTime
    
    -- Salvar resultado
    self:savePipelineResult(pipeline)
    
    return pipeline
end
```

#### Funcionalidade 2
```lua

function CICDPipeline:runStage(stage, pipeline)
    local startTime = os.time()
    local success = false
    local output = ""
    
    if stage == "build" then
        success, output = self:runBuildStage(pipeline)
    elseif stage == "test" then
        success, output = self:runTestStage(pipeline)
    elseif stage == "package" then
        success, output = self:runPackageStage(pipeline)
    elseif stage == "deploy" then
        success, output = self:runDeployStage(pipeline)
    end
    
    local endTime = os.time()
    local duration = endTime - startTime
    
    return {
        success = success,
        output = output,
        duration = duration
    }
```

#### Funcionalidade 3
```lua
end

function CICDPipeline:runBuildStage(pipeline)
    local platforms = {"windows", "linux", "macos"}
    local success = true
    local output = ""
    
    for _, platform in ipairs(platforms) do
        local buildResult = BuildManager:build(platform, "Release", "otclient")
        if not buildResult then
            success = false
            output = output .. string.format("Build failed for %s\n", platform)
        else
            output = output .. string.format("Build successful for %s\n", platform)
        end
    end
    
    return success, output
end

function CICDPipeline:runTestStage(pipeline)
```

#### Funcionalidade 4
```lua
    local testCommand = "ctest --output-on-failure"
    local result = os.execute(testCommand)
    
    if result == 0 then
        return true, "All tests passed"
    else
        return false, "Some tests failed"
    end
end

function CICDPipeline:runPackageStage(pipeline)
    local platforms = {"windows", "linux", "macos"}
    local packages = {}
    local success = true
    local output = ""
    
    for _, platform in ipairs(platforms) do
        local buildDir = string.format("build/%s/release", platform)
        local packageResult = PackageManager:createPackage(platform, "zip", buildDir)
        
        if packageResult then
            table.insert(packages, packageResult)
            output = output .. string.format("Package created for %s\n", platform)
        else
            success = false
            output = output .. string.format("Package failed for %s\n", platform)
        end
```

#### Funcionalidade 5
```lua
    end
    
    pipeline.packages = packages
    return success, output
end

function CICDPipeline:runDeployStage(pipeline)
    -- Só fazer deploy se for tag ou branch principal
    if pipeline.trigger == "tag" or pipeline.branch == "main" then
        local version = self:extractVersion(pipeline.commit)
        local release = ReleaseManager:createRelease(version, "stable", pipeline.packages)
        
        if release then
            return true, "Release deployed successfully"
        else
            return false, "Release deployment failed"
        end
    else
        return true, "Skipped deployment (not main branch or tag)"
    end
end
```

#### Funcionalidade 6
```lua

function CICDPipeline:extractVersion(commit)
    -- Extrair versão do commit ou tag
    local versionFile = io.open("VERSION", "r")
    if versionFile then
        local version = versionFile:read("*line")
        versionFile:close()
        return version or "1.0.0"
    end
    return "1.0.0"
end

function CICDPipeline:savePipelineResult(pipeline)
    local resultFile = string.format("ci-results/pipeline-%s.json", pipeline.commit)
    
    local file = io.open(resultFile, "w")
    if file then
        file:write(self:serializePipeline(pipeline))
        file:close()
    end
end
```

#### Funcionalidade 7
```lua

function CICDPipeline:serializePipeline(pipeline)
    -- Implementar serialização do pipeline
    return string.format([
{
    "trigger": "%s",
    "branch": "%s",
    "commit": "%s",
    "status": "%s",
    "startTime": %d,
    "endTime": %d,
    "duration": %d,
    "stages": %s
}
](
{
    "trigger": "%s",
    "branch": "%s",
    "commit": "%s",
    "status": "%s",
    "startTime": %d,
    "endTime": %d,
    "duration": %d,
    "stages": %s
}
```

#### Finalização
```lua
.md), 
        pipeline.trigger,
        pipeline.branch,
        pipeline.commit,
        pipeline.status,
        pipeline.startTime,
        pipeline.endTime,
        pipeline.duration,
        self:serializeStages(pipeline.stages)
    )
end

function CICDPipeline:serializeStages(stages)
    local stageItems = {}
    for stageName, stageData in pairs(stages) do
        table.insert(stageItems, string.format('"%s": {"status": "%s", "duration": %d}', 
            stageName, stageData.status, stageData.duration))
    end
    return "{" .. table.concat(stageItems, ", ") .. "}"
end
```

---

## 🎯 **5. Melhores Práticas de Deploy**

### **5.1 Princípios de Deploy**

1. **Automação**: Automatizar todo o processo de deploy
2. **Reprodutibilidade**: Garantir que builds sejam idênticos
3. **Segurança**: Verificar integridade dos pacotes
4. **Rollback**: Permitir reversão rápida de releases
5. **Monitoramento**: Acompanhar o status dos deploys

### **5.2 Checklist de Deploy**

#### Nível Basic
```lua
local deployChecklist = {
    "Verificar dependências do sistema",
    "Executar testes automatizados",
    "Validar configurações de build",
    "Verificar assinaturas digitais",
    "Testar instaladores",
    "Validar compatibilidade",
    "Verificar documentação",
    "Testar processo de rollback"
}
```

#### Nível Intermediate
```lua
local deployChecklist = {
    "Verificar dependências do sistema",
    "Executar testes automatizados",
    "Validar configurações de build",
    "Verificar assinaturas digitais",
    "Testar instaladores",
    "Validar compatibilidade",
    "Verificar documentação",
    "Testar processo de rollback"
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
local deployChecklist = {
    "Verificar dependências do sistema",
    "Executar testes automatizados",
    "Validar configurações de build",
    "Verificar assinaturas digitais",
    "Testar instaladores",
    "Validar compatibilidade",
    "Verificar documentação",
    "Testar processo de rollback"
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

### **5.3 Estratégias de Deploy**

#### Nível Basic
```lua
-- Estratégias de deploy
local DeployStrategies = {
    -- Blue-Green Deployment
    blueGreen = function(oldVersion, newVersion)
        -- Manter versão antiga ativa
        -- Deploy nova versão em ambiente paralelo
        -- Testar nova versão
        -- Trocar tráfego para nova versão
        -- Desativar versão antiga
    end,
    
    -- Rolling Deployment
    rolling = function(version, instances)
        -- Deploy em instâncias uma por vez
        -- Verificar saúde de cada instância
        -- Continuar com próxima instância
    end,
    
    -- Canary Deployment
    canary = function(version, percentage)
        -- Deploy para pequena porcentagem de usuários
        -- Monitorar métricas
        -- Expandir gradualmente se tudo OK
    end
}
```

#### Nível Intermediate
```lua
-- Estratégias de deploy
local DeployStrategies = {
    -- Blue-Green Deployment
    blueGreen = function(oldVersion, newVersion)
        -- Manter versão antiga ativa
        -- Deploy nova versão em ambiente paralelo
        -- Testar nova versão
        -- Trocar tráfego para nova versão
        -- Desativar versão antiga
    end,
    
    -- Rolling Deployment
    rolling = function(version, instances)
        -- Deploy em instâncias uma por vez
        -- Verificar saúde de cada instância
        -- Continuar com próxima instância
    end,
    
    -- Canary Deployment
    canary = function(version, percentage)
        -- Deploy para pequena porcentagem de usuários
        -- Monitorar métricas
        -- Expandir gradualmente se tudo OK
    end
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
-- Estratégias de deploy
local DeployStrategies = {
    -- Blue-Green Deployment
    blueGreen = function(oldVersion, newVersion)
        -- Manter versão antiga ativa
        -- Deploy nova versão em ambiente paralelo
        -- Testar nova versão
        -- Trocar tráfego para nova versão
        -- Desativar versão antiga
    end,
    
    -- Rolling Deployment
    rolling = function(version, instances)
        -- Deploy em instâncias uma por vez
        -- Verificar saúde de cada instância
        -- Continuar com próxima instância
    end,
    
    -- Canary Deployment
    canary = function(version, percentage)
        -- Deploy para pequena porcentagem de usuários
        -- Monitorar métricas
        -- Expandir gradualmente se tudo OK
    end
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

## 🔄 **6. Integração com Sistema de Deploy**

### **6.1 Uso com Deploy Stories**

Este guia complementa as Deploy Stories documentadas no sistema, fornecendo:

- ✅ Sistema de build automatizado
- ✅ Gerenciamento de pacotes robusto
- ✅ Pipeline de CI/CD completo
- ✅ Sistema de releases flexível
- ✅ Atualizações automáticas
- ✅ Melhores práticas de deploy

### **6.2 Benefícios para Agentes**

- **Autonomia**: Agentes podem automatizar todo o processo de deploy
- **Confiabilidade**: Sistemas robustos garantem deploys consistentes
- **Eficiência**: Automação reduz tempo e erros humanos
- **Escalabilidade**: Processos padronizados facilitam crescimento

---

## 📊 **Status do Guia**

### **✅ Concluído:**
- ✅ Sistema de build
- ✅ Sistema de packaging
- ✅ Sistema de release
- ✅ Sistema de atualizações
- ✅ Pipeline de CI/CD
- ✅ Melhores práticas
- ✅ Estratégias de deploy
- ✅ Integração com Deploy Stories

### **🎯 Próximo:**
- 🔄 GUIDE-009: Guia de Contribuição

---

**Guia Criado**: 2025-01-27  
**Responsável**: Sistema de Task Manager  
**Status**: ✅ **COMPLETO**  
**Próximo**: 🔥 **GUIDE-009 - Contribuição** 
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

