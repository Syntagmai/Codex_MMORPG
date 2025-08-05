#!/bin/bash

# 🧠 Script de Ativação Completa do Sistema de Aprendizado BMAD
# Epic 14: Ativação do Sistema de Aprendizado dos Agentes
# Versão: 1.0.0
# Data: 2025-01-27

echo "🚀 INICIANDO ATIVAÇÃO COMPLETA DO SISTEMA DE APRENDIZADO BMAD"
echo "================================================================"
echo ""

# Configurações
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENTS_DIR="$BASE_DIR/wiki/bmad/agents"
LOG_DIR="$BASE_DIR/wiki/log"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Criar diretório de logs
mkdir -p "$LOG_DIR"

echo "📁 Diretório base: $BASE_DIR"
echo "🤖 Diretório de agentes: $AGENTS_DIR"
echo "📊 Diretório de logs: $LOG_DIR"
echo ""

# Função para executar comando e verificar resultado
execute_command() {
    local command="$1"
    local description="$2"
    
    echo "🔄 Executando: $description"
    echo "   Comando: $command"
    
    if eval "$command" > "$LOG_DIR/${description// /_}_${TIMESTAMP}.log" 2>&1; then
        echo "   ✅ Sucesso: $description"
        return 0
    else
        echo "   ❌ Erro: $description"
        return 1
    fi
}

# Contador de sucessos e falhas
SUCCESS_COUNT=0
FAILURE_COUNT=0

echo "🎯 TASK 14.1: ATIVAR SISTEMA EDUCACIONAL COMPLETO"
echo "------------------------------------------------"

# Ativar Workflow Orchestrator
if execute_command "cd $BASE_DIR && python $AGENTS_DIR/workflow_orchestrator_agent.py --activate-learning" "Workflow Orchestrator - Learning"; then
    ((SUCCESS_COUNT++))
else
    ((FAILURE_COUNT++))
fi

# Ativar sistema de certificação
if execute_command "cd $BASE_DIR && python $AGENTS_DIR/workflow_orchestrator_agent.py --activate-certification" "Workflow Orchestrator - Certification"; then
    ((SUCCESS_COUNT++))
else
    ((FAILURE_COUNT++))
fi

echo ""
echo "🎯 TASK 14.2: EXECUTAR GERAÇÃO DE CÓDIGO E MÓDULOS"
echo "------------------------------------------------"

# Executar Code Generator Agent
if execute_command "cd $BASE_DIR && python $AGENTS_DIR/code_generator_agent.py --execute-projects" "Code Generator Agent"; then
    ((SUCCESS_COUNT++))
else
    ((FAILURE_COUNT++))
fi

echo ""
echo "🎯 TASK 14.3: ATIVAR SISTEMA DE TREINAMENTO CONTÍNUO"
echo "----------------------------------------------------"

# Ativar Agents Orchestrator
if execute_command "cd $BASE_DIR && python $AGENTS_DIR/agents_orchestrator.py" "Agents Orchestrator"; then
    ((SUCCESS_COUNT++))
else
    ((FAILURE_COUNT++))
fi

# Ativar Metrics Agent
if execute_command "cd $BASE_DIR && python $AGENTS_DIR/metrics_agent.py" "Metrics Agent"; then
    ((SUCCESS_COUNT++))
else
    ((FAILURE_COUNT++))
fi

echo ""
echo "🎯 TASK 14.4: IMPLEMENTAR ANÁLISE DE INSIGHTS AUTOMÁTICA"
echo "--------------------------------------------------------"

# Ativar Deep Source Analyzer
if execute_command "cd $BASE_DIR && python $AGENTS_DIR/deep_source_analyzer.py" "Deep Source Analyzer"; then
    ((SUCCESS_COUNT++))
else
    ((FAILURE_COUNT++))
fi

# Ativar Knowledge Manager
if execute_command "cd $BASE_DIR && python $AGENTS_DIR/knowledge_manager.py" "Knowledge Manager"; then
    ((SUCCESS_COUNT++))
else
    ((FAILURE_COUNT++))
fi

echo ""
echo "🎯 TASK 14.5: CONFIGURAR MONITORAMENTO DE APRENDIZADO"
echo "----------------------------------------------------"

# Ativar Alert Agent
if execute_command "cd $BASE_DIR && python $AGENTS_DIR/alert_agent.py" "Alert Agent"; then
    ((SUCCESS_COUNT++))
else
    ((FAILURE_COUNT++))
fi

# Ativar Dashboard Agent
if execute_command "cd $BASE_DIR && python $AGENTS_DIR/dashboard_agent.py" "Dashboard Agent"; then
    ((SUCCESS_COUNT++))
else
    ((FAILURE_COUNT++))
fi

echo ""
echo "🎯 TASK 14.6: VALIDAR SISTEMA DE APRENDIZADO"
echo "--------------------------------------------"

# Executar Quality Assurance Agent
if execute_command "cd $BASE_DIR && python $AGENTS_DIR/quality_assurance_agent.py" "Quality Assurance Agent"; then
    ((SUCCESS_COUNT++))
else
    ((FAILURE_COUNT++))
fi

echo ""
echo "🎯 TASK 14.7: DOCUMENTAR PROCESSO DE ATIVAÇÃO"
echo "---------------------------------------------"

# Executar Documentation Agent
if execute_command "cd $BASE_DIR && python $AGENTS_DIR/documentation_agent.py" "Documentation Agent"; then
    ((SUCCESS_COUNT++))
else
    ((FAILURE_COUNT++))
fi

echo ""
echo "================================================================"
echo "📊 RELATÓRIO FINAL DE ATIVAÇÃO"
echo "================================================================"
echo ""

# Calcular taxa de sucesso
TOTAL_TASKS=$((SUCCESS_COUNT + FAILURE_COUNT))
SUCCESS_RATE=$(echo "scale=2; $SUCCESS_COUNT * 100 / $TOTAL_TASKS" | bc)

echo "✅ Sucessos: $SUCCESS_COUNT"
echo "❌ Falhas: $FAILURE_COUNT"
echo "📊 Total de tarefas: $TOTAL_TASKS"
echo "🎯 Taxa de sucesso: ${SUCCESS_RATE}%"
echo ""

# Determinar status final
if [ $SUCCESS_RATE -ge 80 ]; then
    echo "🎉 SISTEMA DE APRENDIZADO ATIVADO COM SUCESSO!"
    echo "   Status: OPERACIONAL"
    echo "   Qualidade: EXCELENTE"
elif [ $SUCCESS_RATE -ge 60 ]; then
    echo "⚠️  SISTEMA DE APRENDIZADO ATIVADO PARCIALMENTE"
    echo "   Status: PARCIALMENTE OPERACIONAL"
    echo "   Qualidade: BOM"
else
    echo "❌ SISTEMA DE APRENDIZADO COM PROBLEMAS"
    echo "   Status: COM PROBLEMAS"
    echo "   Qualidade: NECESSITA ATENÇÃO"
fi

echo ""
echo "📁 Logs salvos em: $LOG_DIR"
echo "📋 Documentação: $BASE_DIR/wiki/docs/epic_14_activation_documentation.md"
echo ""

# Verificar se interface gráfica está disponível
if [ -f "$BASE_DIR/bmad_system_gui_integrated.py" ]; then
    echo "🖥️  Interface gráfica disponível!"
    echo "   Para iniciar: python bmad_system_gui_integrated.py"
    echo ""
fi

echo "🚀 Ativação concluída em: $(date)"
echo "================================================================" 