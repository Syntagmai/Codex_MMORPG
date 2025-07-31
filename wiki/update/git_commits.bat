@echo off
chcp 65001 >nul
echo 🚀 Iniciando commits atômicos organizados...

REM Verifica se estamos em um repositório Git
git rev-parse --git-dir >nul 2>&1
if errorlevel 1 (
    echo ❌ Não estamos em um repositório Git válido
    exit /b 1
)

REM Obtém arquivos não rastreados
echo 📁 Verificando arquivos não rastreados...
git status --porcelain | findstr "^??" > temp_untracked.txt

REM Verifica se há arquivos
if not exist temp_untracked.txt (
    echo ✅ Nenhum arquivo não rastreado encontrado
    exit /b 0
)

REM Commit 1: Documentação Core
echo.
echo 🔄 Commit 1: Documentação Core
git add "wiki/otclient/CORE-010_Backup_System.md"
git commit -m "docs: adiciona sistema de backup avançado para OTClient (CORE-010)"
if errorlevel 1 (
    echo ❌ Erro no commit core
    exit /b 1
)
echo ✅ Commit core realizado

REM Commit 2: Guias Avançados
echo.
echo 🔄 Commit 2: Guias Avançados
git add "wiki/otclient/GUIDE-004_Debugging_Avancado.md"
git add "wiki/otclient/GUIDE-005_Performance_Otimizacao.md"
git add "wiki/otclient/GUIDE-006_UI_Avancada.md"
git add "wiki/otclient/GUIDE-007_Game_Systems.md"
git add "wiki/otclient/GUIDE-008_Deploy.md"
git add "wiki/otclient/GUIDE-009_Contribuicao.md"
git add "wiki/otclient/GUIDE-010_Troubleshooting.md"
git commit -m "docs: adiciona guias avançados de desenvolvimento e troubleshooting"
if errorlevel 1 (
    echo ❌ Erro no commit guides
    exit /b 1
)
echo ✅ Commit guides realizado

REM Commit 3: Sistemas de UI
echo.
echo 🔄 Commit 3: Sistemas de UI
git add "wiki/otclient/UI_Modals_System_Guide.md"
git commit -m "docs: adiciona documentação de sistemas de interface do usuário"
if errorlevel 1 (
    echo ❌ Erro no commit UI
    exit /b 1
)
echo ✅ Commit UI realizado

REM Commit 4: Integração e Relatórios
echo.
echo 🔄 Commit 4: Integração e Relatórios
git add "wiki/otclient/Habdel_Wiki_Integration_Report.md"
git add "wiki/otclient/Wiki_Completion_Plan.md"
git commit -m "docs: adiciona documentação de integração e relatórios"
if errorlevel 1 (
    echo ❌ Erro no commit integration
    exit /b 1
)
echo ✅ Commit integration realizado

REM Commit 5: Tarefas e Planos
echo.
echo 🔄 Commit 5: Tarefas e Planos
git add "wiki/update/epic_2_canary_integration_task.md"
git commit -m "docs: adiciona tarefas e planos de desenvolvimento"
if errorlevel 1 (
    echo ❌ Erro no commit tasks
    exit /b 1
)
echo ✅ Commit tasks realizado

REM Limpa arquivo temporário
if exist temp_untracked.txt del temp_untracked.txt

echo.
echo 🎉 Processo concluído! 5 commits realizados
echo.
echo 📊 Status final:
git status

echo.
echo 🚀 Fazendo pull do repositório remoto...
git pull origin doc
if errorlevel 1 (
    echo ⚠️ Aviso: Erro no pull, mas commits foram realizados
) else (
    echo ✅ Pull realizado com sucesso
)

echo.
echo ✅ Processo completo finalizado! 