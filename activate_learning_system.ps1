# �� Script de Ativação Completa do Sistema de Aprendizado dos Agentes (Windows)
# =================================================================
# Este script ativa efetivamente todo o sistema de agentes para que
# eles comecem a aprender, criar módulos e melhorar continuamente.
#
# Autor: Sistema BMAD - Codex MMORPG
# Versão: 1.0.0
# Data: 2025-08-01
# Sistema: Windows PowerShell
# =================================================================

Write-Host "🧠 ATIVAÇÃO COMPLETA DO SISTEMA DE APRENDIZADO DOS AGENTES" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host ""

# Configurações
$Timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$LogFile = "wiki\log\activation_$Timestamp.log"
$SuccessCount = 0
$TotalTasks = 8

# Função para log
function Write-LogMessage {
    param($Message)
    $LogEntry = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $Message"
    Write-Host $LogEntry
    Add-Content -Path $LogFile -Value $LogEntry
}

# Função para verificar sucesso
function Test-Success {
    param($TaskName)
    if ($LASTEXITCODE -eq 0) {
        Write-LogMessage "✅ $TaskName - SUCESSO"
        $script:SuccessCount++
    } else {
        Write-LogMessage "❌ $TaskName - FALHA"
    }
}

# Criar diretório de log se não existir
if (!(Test-Path "wiki\log")) {
    New-Item -ItemType Directory -Path "wiki\log" -Force | Out-Null
}

Write-LogMessage "�� Iniciando ativação do sistema de aprendizado..."
Write-LogMessage "�� Log salvo em: $LogFile"
Write-Host ""

# =================================================================
# TASK 14.1: ATIVAR SISTEMA EDUCACIONAL COMPLETO
# =================================================================
Write-Host "📚 TASK 14.1: Ativando Sistema Educacional Completo" -ForegroundColor Yellow
Write-Host "---------------------------------------------------" -ForegroundColor Yellow

Write-LogMessage "🎓 Ativando sistema de aprendizado automático..."
python wiki\bmad\agents\workflow_orchestrator_agent.py --activate-learning
Test-Success "Sistema de aprendizado automático"

Write-LogMessage "🏆 Ativando sistema de certificação..."
python wiki\bmad\agents\workflow_orchestrator_agent.py --activate-certification
Test-Success "Sistema de certificação"

Write-LogMessage "📖 Criando cursos funcionais..."
python wiki\bmad\agents\professor_agent.py --create-courses
Test-Success "Criação de cursos funcionais"

Write-LogMessage "📝 Gerando lições estruturadas..."
python wiki\bmad\agents\professor_agent.py --generate-lessons
Test-Success "Geração de lições estruturadas"

Write-Host ""

# =================================================================
# TASK 14.2: EXECUTAR GERAÇÃO DE CÓDIGO E MÓDULOS
# =================================================================
Write-Host "🤖 TASK 14.2: Executando Geração de Código e Módulos" -ForegroundColor Yellow
Write-Host "---------------------------------------------------" -ForegroundColor Yellow

Write-LogMessage "🔧 Executando projetos práticos..."
python wiki\bmad\agents\code_generator_agent.py --execute-projects
Test-Success "Execução de projetos práticos"

Write-LogMessage "�� Analisando módulos OTClient..."
python wiki\bmad\run_module_workflow.py --module client --variations 5
Test-Success "Análise de módulos OTClient"

Write-LogMessage "📋 Listando módulos disponíveis..."
python wiki\bmad\run_module_workflow.py --list-modules
Test-Success "Listagem de módulos"

Write-Host ""

# =================================================================
# TASK 14.3: ATIVAR SISTEMA DE TREINAMENTO CONTÍNUO
# =================================================================
Write-Host "🔄 TASK 14.3: Ativando Sistema de Treinamento Contínuo" -ForegroundColor Yellow
Write-Host "-----------------------------------------------------" -ForegroundColor Yellow

Write-LogMessage "🎯 Ativando orquestrador de agentes..."
python wiki\bmad\agents\agents_orchestrator.py
Test-Success "Orquestrador de agentes"

Write-LogMessage "📊 Ativando sistema de métricas..."
python wiki\bmad\agents\metrics_agent.py
Test-Success "Sistema de métricas"

Write-LogMessage "✅ Ativando validação contínua..."
python wiki\bmad\agents\unified_validation_agent.py
Test-Success "Validação contínua"

Write-Host ""

# =================================================================
# TASK 14.4: IMPLEMENTAR ANÁLISE DE INSIGHTS AUTOMÁTICA
# =================================================================
Write-Host "🔍 TASK 14.4: Implementando Análise de Insights Automática" -ForegroundColor Yellow
Write-Host "----------------------------------------------------------" -ForegroundColor Yellow

Write-LogMessage "🔬 Ativando análise profunda de código..."
python wiki\bmad\agents\deep_source_analyzer.py
Test-Success "Análise profunda de código"

Write-LogMessage "📚 Ativando gerenciamento de conhecimento..."
python wiki\bmad\agents\knowledge_manager.py
Test-Success "Gerenciamento de conhecimento"

Write-LogMessage "🔍 Ativando pesquisa unificada..."
python wiki\bmad\agents\unified_research_agent.py
Test-Success "Pesquisa unificada"

Write-Host ""

# =================================================================
# TASK 14.5: CONFIGURAR MONITORAMENTO DE APRENDIZADO
# =================================================================
Write-Host "📈 TASK 14.5: Configurando Monitoramento de Aprendizado" -ForegroundColor Yellow
Write-Host "-------------------------------------------------------" -ForegroundColor Yellow

Write-LogMessage "🚨 Ativando sistema de alertas..."
python wiki\bmad\agents\alert_agent.py
Test-Success "Sistema de alertas"

Write-LogMessage "�� Ativando dashboard de aprendizado..."
python wiki\bmad\agents\dashboard_agent.py
Test-Success "Dashboard de aprendizado"

Write-Host ""

# =================================================================
# TASK 14.6: VALIDAR SISTEMA DE APRENDIZADO
# =================================================================
Write-Host "✅ TASK 14.6: Validando Sistema de Aprendizado" -ForegroundColor Yellow
Write-Host "----------------------------------------------" -ForegroundColor Yellow

Write-LogMessage "🔍 Executando validação de qualidade..."
python wiki\bmad\agents\quality_assurance_agent.py
Test-Success "Validação de qualidade"

Write-LogMessage "✅ Executando validação unificada..."
python wiki\bmad\agents\unified_validation_agent.py
Test-Success "Validação unificada"

Write-Host ""

# =================================================================
# TASK 14.7: DOCUMENTAR PROCESSO DE ATIVAÇÃO
# =================================================================
Write-Host "📝 TASK 14.7: Documentando Processo de Ativação" -ForegroundColor Yellow
Write-Host "-----------------------------------------------" -ForegroundColor Yellow

Write-LogMessage "📚 Gerando documentação..."
python wiki\bmad\agents\documentation_agent.py
Test-Success "Geração de documentação"

Write-LogMessage "📖 Gerando documentação abrangente..."
python wiki\bmad\agents\comprehensive_documentation_agent.py
Test-Success "Documentação abrangente"

Write-Host ""

# =================================================================
# TASK 14.8: CRIAR SCRIPT DE ATIVAÇÃO COMPLETA
# =================================================================
Write-Host "🛠️ TASK 14.8: Criando Script de Ativação Completa" -ForegroundColor Yellow
Write-Host "-------------------------------------------------" -ForegroundColor Yellow

Write-LogMessage "�� Integrando sistema..."
python wiki\bmad\agents\integration_agent.py
Test-Success "Integração do sistema"

Write-LogMessage "📋 Atualizando task master..."
python wiki\bmad\agents\task_master_agent.py
Test-Success "Atualização do task master"

Write-Host ""

# =================================================================
# RELATÓRIO FINAL
# =================================================================
Write-Host "�� RELATÓRIO FINAL DA ATIVAÇÃO" -ForegroundColor Green
Write-Host "==============================" -ForegroundColor Green

$SuccessRate = [math]::Round(($SuccessCount * 100) / $TotalTasks)

Write-LogMessage "�� Taxa de sucesso: $SuccessCount/$TotalTasks ($SuccessRate%)"

if ($SuccessRate -ge 80) {
    Write-LogMessage "�� ATIVAÇÃO BEM-SUCEDIDA! Sistema de aprendizado ativo."
    Write-Host ""
    Write-Host "🎯 PRÓXIMOS PASSOS:" -ForegroundColor Green
    Write-Host "1. Monitorar logs em: $LogFile" -ForegroundColor White
    Write-Host "2. Verificar dashboard em: wiki\dashboard\" -ForegroundColor White
    Write-Host "3. Acompanhar progresso em: wiki\log\" -ForegroundColor White
    Write-Host "4. Executar comandos especializados quando necessário" -ForegroundColor White
    Write-Host ""
    Write-Host "🚀 O sistema está aprendendo e melhorando continuamente!" -ForegroundColor Green
    exit 0
} else {
    Write-LogMessage "⚠️ ATIVAÇÃO PARCIAL. Verificar logs para detalhes."
    Write-Host ""
    Write-Host "�� AÇÕES RECOMENDADAS:" -ForegroundColor Yellow
    Write-Host "1. Verificar logs em: $LogFile" -ForegroundColor White
    Write-Host "2. Executar tarefas falhadas manualmente" -ForegroundColor White
    Write-Host "3. Verificar dependências e configurações" -ForegroundColor White
    Write-Host "4. Tentar ativação novamente após correções" -ForegroundColor White
    exit 1
}