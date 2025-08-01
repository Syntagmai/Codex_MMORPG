#!/bin/bash

# 🧠 Script de Ativação Completa do Sistema de Aprendizado dos Agentes
# =================================================================
# Este script ativa efetivamente todo o sistema de agentes para que
# eles comecem a aprender, criar módulos e melhorar continuamente.
#
# Autor: Sistema BMAD - Codex MMORPG
# Versão: 1.0.0
# Data: 2025-08-01
# =================================================================

echo "🧠 ATIVAÇÃO COMPLETA DO SISTEMA DE APRENDIZADO DOS AGENTES"
echo "=========================================================="
echo ""

# Configurações
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="wiki/log/activation_${TIMESTAMP}.log"
SUCCESS_COUNT=0
TOTAL_TASKS=8

# Função para log
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Função para verificar sucesso
check_success() {
    if [ $? -eq 0 ]; then
        log_message "✅ $1 - SUCESSO"
        ((SUCCESS_COUNT++))
    else
        log_message "❌ $1 - FALHA"
    fi
}

# Criar diretório de log se não existir
mkdir -p wiki/log

log_message "🚀 Iniciando ativação do sistema de aprendizado..."
log_message "📁 Log salvo em: $LOG_FILE"
echo ""

# =================================================================
# TASK 14.1: ATIVAR SISTEMA EDUCACIONAL COMPLETO
# =================================================================
echo "📚 TASK 14.1: Ativando Sistema Educacional Completo"
echo "---------------------------------------------------"

log_message "🎓 Ativando sistema de aprendizado automático..."
python wiki/bmad/agents/workflow_orchestrator_agent.py --activate-learning
check_success "Sistema de aprendizado automático"

log_message "🏆 Ativando sistema de certificação..."
python wiki/bmad/agents/workflow_orchestrator_agent.py --activate-certification
check_success "Sistema de certificação"

log_message "📖 Criando cursos funcionais..."
python wiki/bmad/agents/professor_agent.py --create-courses
check_success "Criação de cursos funcionais"

log_message "📝 Gerando lições estruturadas..."
python wiki/bmad/agents/professor_agent.py --generate-lessons
check_success "Geração de lições estruturadas"

echo ""

# =================================================================
# TASK 14.2: EXECUTAR GERAÇÃO DE CÓDIGO E MÓDULOS
# =================================================================
echo "🤖 TASK 14.2: Executando Geração de Código e Módulos"
echo "---------------------------------------------------"

log_message "🔧 Executando projetos práticos..."
python wiki/bmad/agents/code_generator_agent.py --execute-projects
check_success "Execução de projetos práticos"

log_message "📦 Analisando módulos OTClient..."
python wiki/bmad/run_module_workflow.py --module client --variations 5
check_success "Análise de módulos OTClient"

log_message "📋 Listando módulos disponíveis..."
python wiki/bmad/run_module_workflow.py --list-modules
check_success "Listagem de módulos"

echo ""

# =================================================================
# TASK 14.3: ATIVAR SISTEMA DE TREINAMENTO CONTÍNUO
# =================================================================
echo "🔄 TASK 14.3: Ativando Sistema de Treinamento Contínuo"
echo "-----------------------------------------------------"

log_message "🎯 Ativando orquestrador de agentes..."
python wiki/bmad/agents/agents_orchestrator.py
check_success "Orquestrador de agentes"

log_message "📊 Ativando sistema de métricas..."
python wiki/bmad/agents/metrics_agent.py
check_success "Sistema de métricas"

log_message "✅ Ativando validação contínua..."
python wiki/bmad/agents/unified_validation_agent.py
check_success "Validação contínua"

echo ""

# =================================================================
# TASK 14.4: IMPLEMENTAR ANÁLISE DE INSIGHTS AUTOMÁTICA
# =================================================================
echo "🔍 TASK 14.4: Implementando Análise de Insights Automática"
echo "----------------------------------------------------------"

log_message "🔬 Ativando análise profunda de código..."
python wiki/bmad/agents/deep_source_analyzer.py
check_success "Análise profunda de código"

log_message "📚 Ativando gerenciamento de conhecimento..."
python wiki/bmad/agents/knowledge_manager.py
check_success "Gerenciamento de conhecimento"

log_message "🔍 Ativando pesquisa unificada..."
python wiki/bmad/agents/unified_research_agent.py
check_success "Pesquisa unificada"

echo ""

# =================================================================
# TASK 14.5: CONFIGURAR MONITORAMENTO DE APRENDIZADO
# =================================================================
echo "📈 TASK 14.5: Configurando Monitoramento de Aprendizado"
echo "-------------------------------------------------------"

log_message "🚨 Ativando sistema de alertas..."
python wiki/bmad/agents/alert_agent.py
check_success "Sistema de alertas"

log_message "📊 Ativando dashboard de aprendizado..."
python wiki/bmad/agents/dashboard_agent.py
check_success "Dashboard de aprendizado"

echo ""

# =================================================================
# TASK 14.6: VALIDAR SISTEMA DE APRENDIZADO
# =================================================================
echo "✅ TASK 14.6: Validando Sistema de Aprendizado"
echo "----------------------------------------------"

log_message "🔍 Executando validação de qualidade..."
python wiki/bmad/agents/quality_assurance_agent.py
check_success "Validação de qualidade"

log_message "✅ Executando validação unificada..."
python wiki/bmad/agents/unified_validation_agent.py
check_success "Validação unificada"

echo ""

# =================================================================
# TASK 14.7: DOCUMENTAR PROCESSO DE ATIVAÇÃO
# =================================================================
echo "📝 TASK 14.7: Documentando Processo de Ativação"
echo "-----------------------------------------------"

log_message "📚 Gerando documentação..."
python wiki/bmad/agents/documentation_agent.py
check_success "Geração de documentação"

log_message "📖 Gerando documentação abrangente..."
python wiki/bmad/agents/comprehensive_documentation_agent.py
check_success "Documentação abrangente"

echo ""

# =================================================================
# TASK 14.8: CRIAR SCRIPT DE ATIVAÇÃO COMPLETA
# =================================================================
echo "🛠️ TASK 14.8: Criando Script de Ativação Completa"
echo "-------------------------------------------------"

log_message "🔧 Integrando sistema..."
python wiki/bmad/agents/integration_agent.py
check_success "Integração do sistema"

log_message "📋 Atualizando task master..."
python wiki/bmad/agents/task_master_agent.py
check_success "Atualização do task master"

echo ""

# =================================================================
# RELATÓRIO FINAL
# =================================================================
echo "📊 RELATÓRIO FINAL DA ATIVAÇÃO"
echo "=============================="

SUCCESS_RATE=$((SUCCESS_COUNT * 100 / TOTAL_TASKS))

log_message "📈 Taxa de sucesso: $SUCCESS_COUNT/$TOTAL_TASKS ($SUCCESS_RATE%)"

if [ $SUCCESS_RATE -ge 80 ]; then
    log_message "🎉 ATIVAÇÃO BEM-SUCEDIDA! Sistema de aprendizado ativo."
    echo ""
    echo "🎯 PRÓXIMOS PASSOS:"
    echo "1. Monitorar logs em: $LOG_FILE"
    echo "2. Verificar dashboard em: wiki/dashboard/"
    echo "3. Acompanhar progresso em: wiki/log/"
    echo "4. Executar comandos especializados quando necessário"
    echo ""
    echo "🚀 O sistema está aprendendo e melhorando continuamente!"
    exit 0
else
    log_message "⚠️ ATIVAÇÃO PARCIAL. Verificar logs para detalhes."
    echo ""
    echo "🔧 AÇÕES RECOMENDADAS:"
    echo "1. Verificar logs em: $LOG_FILE"
    echo "2. Executar tarefas falhadas manualmente"
    echo "3. Verificar dependências e configurações"
    echo "4. Tentar ativação novamente após correções"
    exit 1
fi 