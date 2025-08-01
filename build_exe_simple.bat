@echo off
echo ========================================
echo BMAD System GUI - Gerador de Executavel
echo ========================================
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python nao encontrado!
    echo Instale Python primeiro: https://python.org
    pause
    exit /b 1
)

echo ✅ Python encontrado
echo.

REM Instalar PyInstaller se necessário
echo 📦 Verificando PyInstaller...
python -c "import PyInstaller" >nul 2>&1
if errorlevel 1 (
    echo Instalando PyInstaller...
    pip install pyinstaller
    if errorlevel 1 (
        echo ❌ Erro ao instalar PyInstaller
        pause
        exit /b 1
    )
) else (
    echo ✅ PyInstaller ja instalado
)

echo.

REM Verificar se os arquivos necessários existem
if not exist "bmad_system_gui_integrated.py" (
    echo ❌ Arquivo bmad_system_gui_integrated.py nao encontrado
    pause
    exit /b 1
)

if not exist "gui_modules" (
    echo ❌ Pasta gui_modules nao encontrada
    pause
    exit /b 1
)

if not exist "wiki\bmad\agents" (
    echo ❌ Pasta wiki\bmad\agents nao encontrada
    pause
    exit /b 1
)

echo ✅ Todos os arquivos necessarios encontrados
echo.

REM Limpar builds anteriores
if exist "build" (
    echo Limpando builds anteriores...
    rmdir /s /q build
)

if exist "dist" (
    echo Limpando dist anteriores...
    rmdir /s /q dist
)

if exist "*.spec" (
    echo Removendo arquivos .spec anteriores...
    del *.spec
)

echo.

REM Criar executável
echo 🔨 Criando executavel...
echo Isso pode demorar alguns minutos...
echo.

pyinstaller --onefile --windowed --name="BMAD_System_GUI" --add-data="gui_modules;gui_modules" --add-data="wiki;wiki" bmad_system_gui_integrated.py

if errorlevel 1 (
    echo ❌ Erro ao criar executavel
    pause
    exit /b 1
)

echo.
echo ✅ Executavel criado com sucesso!
echo.

REM Verificar se o executável foi criado
if exist "dist\BMAD_System_GUI.exe" (
    echo 📁 Executavel criado em: dist\BMAD_System_GUI.exe
    echo.
    echo 🎯 Para testar:
    echo   1. Vá para a pasta dist
    echo   2. Execute BMAD_System_GUI.exe
    echo.
    
    REM Perguntar se quer testar
    set /p testar="Deseja testar o executavel agora? (s/n): "
    if /i "%testar%"=="s" (
        echo.
        echo 🚀 Iniciando teste...
        start "" "dist\BMAD_System_GUI.exe"
    )
) else (
    echo ❌ Executavel nao foi criado corretamente
)

echo.
echo ========================================
echo Processo concluido!
echo ========================================
pause 