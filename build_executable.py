#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gerar executável do BMAD System GUI Integrado
Usa PyInstaller para criar um arquivo .exe standalone

Autor: Sistema BMAD - Codex MMORPG
Versão: 1.0.0
Data: 2025-08-01
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
from datetime import datetime

def check_pyinstaller():
    """Verifica se PyInstaller está instalado"""
    try:
        import PyInstaller
        print("✅ PyInstaller encontrado")
        return True
    except ImportError:
        print("❌ PyInstaller não encontrado")
        print("📦 Instalando PyInstaller...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            print("✅ PyInstaller instalado com sucesso")
            return True
        except subprocess.CalledProcessError:
            print("❌ Erro ao instalar PyInstaller")
            return False

def create_spec_file():
    """Cria arquivo .spec para PyInstaller"""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['bmad_system_gui_integrated.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('gui_modules', 'gui_modules'),
        ('wiki/bmad/agents', 'wiki/bmad/agents'),
        ('wiki', 'wiki'),
    ],
    hiddenimports=[
        'tkinter',
        'tkinter.ttk',
        'tkinter.scrolledtext',
        'tkinter.messagebox',
        'pathlib',
        'threading',
        'subprocess',
        'json',
        'datetime',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='BMAD_System_GUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico' if os.path.exists('icon.ico') else None,
)
'''
    
    with open('bmad_system_gui_integrated.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    
    print("✅ Arquivo .spec criado")

def create_icon():
    """Cria um ícone simples para o executável"""
    try:
        # Verificar se já existe um ícone
        if Path("icon.ico").exists():
            print("✅ Ícone já existe")
            return True
        
        # Tentar criar um ícone simples usando PIL
        try:
            from PIL import Image, ImageDraw
            
            # Criar imagem 256x256
            img = Image.new('RGBA', (256, 256), (37, 99, 235, 255))  # Azul BMAD
            draw = ImageDraw.Draw(img)
            
            # Desenhar círculo central
            draw.ellipse([64, 64, 192, 192], fill=(255, 255, 255, 255))
            
            # Salvar como ICO
            img.save('icon.ico', format='ICO')
            print("✅ Ícone criado")
            return True
            
        except ImportError:
            print("⚠️ PIL não disponível, executável será criado sem ícone")
            return False
            
    except Exception as e:
        print(f"⚠️ Erro ao criar ícone: {e}")
        return False

def build_executable():
    """Constrói o executável"""
    print("🔨 Iniciando construção do executável...")
    
    # Verificar se o arquivo principal existe
    if not Path("bmad_system_gui_integrated.py").exists():
        print("❌ Arquivo bmad_system_gui_integrated.py não encontrado")
        return False
    
    # Verificar se os módulos existem
    if not Path("gui_modules").exists():
        print("❌ Pasta gui_modules não encontrada")
        return False
    
    # Verificar se os agentes existem
    if not Path("wiki/bmad/agents").exists():
        print("❌ Pasta wiki/bmad/agents não encontrada")
        return False
    
    try:
        # Criar arquivo .spec
        create_spec_file()
        
        # Criar ícone
        create_icon()
        
        # Executar PyInstaller
        print("🔨 Executando PyInstaller...")
        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--clean",
            "--noconfirm",
            "bmad_system_gui_integrated.spec"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Executável criado com sucesso!")
            return True
        else:
            print("❌ Erro ao criar executável:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Erro durante a construção: {e}")
        return False

def create_installer_script():
    """Cria script de instalação simples"""
    installer_content = '''@echo off
echo ========================================
echo BMAD System GUI - Instalador
echo ========================================
echo.

REM Criar diretório de instalação
set INSTALL_DIR=%USERPROFILE%\\BMAD_System_GUI
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

echo Instalando BMAD System GUI...
echo Diretório: %INSTALL_DIR%

REM Copiar executável
copy "dist\\BMAD_System_GUI.exe" "%INSTALL_DIR%\\"

REM Criar atalho na área de trabalho
echo Criando atalho na área de trabalho...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\\Desktop\\BMAD System GUI.lnk'); $Shortcut.TargetPath = '%INSTALL_DIR%\\BMAD_System_GUI.exe'; $Shortcut.Save()"

echo.
echo ========================================
echo Instalação concluída!
echo ========================================
echo.
echo O BMAD System GUI foi instalado em:
echo %INSTALL_DIR%
echo.
echo Um atalho foi criado na área de trabalho.
echo.
pause
'''
    
    with open('installer.bat', 'w', encoding='utf-8') as f:
        f.write(installer_content)
    
    print("✅ Script de instalação criado")

def create_readme_executable():
    """Cria README para o executável"""
    readme_content = '''# BMAD System GUI - Executável

## 🎯 **Sobre o Executável**

Este é o **BMAD System GUI** compilado como executável standalone, permitindo execução sem necessidade de Python instalado.

## 🚀 **Como Usar**

### **Execução Direta**
1. Execute o arquivo `BMAD_System_GUI.exe`
2. O sistema será iniciado automaticamente
3. Todos os agentes BMAD estarão disponíveis

### **Instalação (Opcional)**
1. Execute `installer.bat` para instalação completa
2. O sistema será instalado em `%USERPROFILE%\\BMAD_System_GUI`
3. Um atalho será criado na área de trabalho

## 📁 **Estrutura do Executável**

O executável contém:
- ✅ Interface gráfica completa
- ✅ Todos os módulos GUI
- ✅ Agentes BMAD integrados
- ✅ Sistema de logs
- ✅ Configurações

## 🔧 **Requisitos**

- ✅ **Windows 10/11** (testado)
- ✅ **Sem necessidade de Python** instalado
- ✅ **Sem dependências** externas

## 📊 **Funcionalidades**

### **Controle de Sistema**
- Iniciar/Parar Sistema
- Atualizar lista de agentes

### **Controle de Agentes**
- Execução individual de agentes
- Execução em lote
- Parar todos os agentes

### **Sistema de Logs**
- Logs em tempo real
- Salvar logs em arquivo
- Limpar logs

## 🎨 **Interface**

- Interface moderna e intuitiva
- Tema claro e acessível
- Navegação simplificada
- Detecção automática de agentes

## 📝 **Logs**

Os logs são salvos em:
- `%USERPROFILE%\\BMAD_System_GUI\\logs\\`

## 🔄 **Atualizações**

Para atualizar o sistema:
1. Baixe a nova versão
2. Substitua o executável antigo
3. Execute a nova versão

---

**Versão**: 4.0.0 (Executável)  
**Data**: 2025-08-01  
**Status**: ✅ Funcional e Operacional
'''
    
    with open('README_EXECUTABLE.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("✅ README do executável criado")

def main():
    """Função principal"""
    print("🚀 BMAD System GUI - Gerador de Executável")
    print("=" * 50)
    
    # Verificar PyInstaller
    if not check_pyinstaller():
        print("❌ Não foi possível instalar PyInstaller")
        return
    
    # Construir executável
    if build_executable():
        print("\n✅ Executável criado com sucesso!")
        
        # Criar arquivos adicionais
        create_installer_script()
        create_readme_executable()
        
        print("\n📁 Arquivos criados:")
        print("  - dist/BMAD_System_GUI.exe (executável)")
        print("  - installer.bat (script de instalação)")
        print("  - README_EXECUTABLE.md (documentação)")
        
        print("\n🎯 Como usar:")
        print("  1. Execute dist/BMAD_System_GUI.exe")
        print("  2. Ou execute installer.bat para instalação completa")
        
    else:
        print("\n❌ Falha ao criar executável")

if __name__ == "__main__":
    main() 