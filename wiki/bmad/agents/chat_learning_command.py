#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unicode_aliases
"""
Chat Learning Command - Comando de Aprendizado para Chat
=======================================================

Comando simples que pode ser executado diretamente do chat para:
1. Executar workflow de aprendizado completo
2. Gerar relatórios de aprendizado
3. Consultar estatísticas de aprendizado

Uso no chat:
@learn_create "module_name" "language" "purpose" [reference_source]
@learn_report
@learn_stats

Autor: Sistema BMAD
Versão: 1.0.0
Data: 2025-01-27
"""

import sys
import json
from pathlib import Path

# Importar o orquestrador
try:
    from learning_workflow_orchestrator import LearningWorkflowOrchestrator
except ImportError:
    print("❌ Erro: Learning Workflow Orchestrator não encontrado")
    sys.exit(1)

def learn_create(module_name: str, language: str, purpose: str, reference_source: str = "otclient"):
    """
    Comando para criar módulo com aprendizado.
    
    Args:
        module_name: Nome do módulo
        language: Linguagem de programação
        purpose: Propósito do módulo
        reference_source: Fonte de referência
    """
    print(f"🚀 Iniciando criação de módulo com aprendizado...")
    print(f"📦 Módulo: {module_name}")
    print(f"🐍 Linguagem: {language}")
    print(f"🎯 Propósito: {purpose}")
    print(f"📚 Referência: {reference_source}")
    print("-" * 50)
    
    orchestrator = LearningWorkflowOrchestrator()
    
    success = orchestrator.run_learning_workflow(
        module_name, language, purpose, reference_source
    )
    
    if success:
        print("✅ Módulo criado com sucesso e aprendizado registrado!")
        print("📝 Relatório de aprendizado gerado")
        print("🔄 Memória de aprendizado atualizada")
    else:
        print("❌ Falha na criação do módulo")
        print("📋 Verifique os logs para mais detalhes")

def learn_report():
    """Comando para gerar relatório de aprendizado."""
    print("📊 Gerando relatório de aprendizado...")
    
    orchestrator = LearningWorkflowOrchestrator()
    report = orchestrator.generate_learning_report()
    
    print(report)

def learn_stats():
    """Comando para mostrar estatísticas de aprendizado."""
    print("📈 Estatísticas de Aprendizado")
    print("-" * 30)
    
    orchestrator = LearningWorkflowOrchestrator()
    stats = orchestrator.get_learning_statistics()
    
    print(f"📦 Total de módulos criados: {stats['total_modules_created']}")
    print(f"✅ Padrões de sucesso: {stats['successful_patterns']}")
    print(f"❌ Erros comuns: {stats['common_errors']}")
    print(f"🔄 Estratégias de melhoria: {stats['improvement_strategies']}")
    print(f"📝 Entradas de feedback: {stats['feedback_entries']}")
    print(f"🧠 Tamanho da memória: {stats['learning_memory_size']}")

def show_help():
    """Mostra ajuda dos comandos disponíveis."""
    help_text = """
🎓 Comandos de Aprendizado - Sistema BMAD

📖 COMANDOS DISPONÍVEIS:

1. @learn_create "module_name" "language" "purpose" [reference_source]
   Cria um módulo com aprendizado contínuo
   
   Exemplos:
   @learn_create "network_handler" "C++" "Gerenciamento de conexões"
   @learn_create "ui_component" "Lua" "Interface de usuário" "otclient"
   @learn_create "game_logic" "C++" "Lógica de jogo" "canary"

2. @learn_report
   Gera relatório completo de aprendizado
   
3. @learn_stats
   Mostra estatísticas de aprendizado

4. @learn_help
   Mostra esta ajuda

🔄 WORKFLOW DE APRENDIZADO:

1. 🔍 Análise do código de referência (OTClient/Canary)
2. 🏗️ Geração do módulo baseado no aprendizado
3. 🧠 Análise educacional e comentários
4. 📊 Avaliação de qualidade
5. 📝 Documentação e feedback
6. 🔄 Atualização da memória de aprendizado

📚 FONTES DE REFERÊNCIA:
- otclient: Código-fonte do OTClient
- canary: Código-fonte do Canary (quando disponível)

🎯 OBJETIVO:
Evoluir para agentes criadores de código sem erros através de aprendizado contínuo!
"""
    print(help_text)

def main():
    """Função principal para execução dos comandos."""
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == "create" and len(sys.argv) >= 5:
        module_name = sys.argv[2]
        language = sys.argv[3]
        purpose = sys.argv[4]
        reference_source = sys.argv[5] if len(sys.argv) > 5 else "otclient"
        
        learn_create(module_name, language, purpose, reference_source)
        
    elif command == "report":
        learn_report()
        
    elif command == "stats":
        learn_stats()
        
    elif command == "help":
        show_help()
        
    else:
        print("❌ Comando inválido ou parâmetros incorretos")
        print("💡 Use @learn_help para ver os comandos disponíveis")

if __name__ == "__main__":
    main() 