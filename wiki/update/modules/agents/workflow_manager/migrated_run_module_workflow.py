# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
TIMEOUT_SECONDS = 60

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: run_module_workflow.py
Módulo de Destino: agents.workflow_manager
Data de Migração: 2025-08-01 12:21:42

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import WorkflowmanagerModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 Script Principal - Workflow de Módulos OTClient
Script para executar o workflow completo de análise, geração e teste de módulos OTClient
"""

import os
import sys
import argparse
import json
from pathlib import Path

# Adicionar diretório dos agentes ao path
current_dir = os.path.dirname(os.path.abspath(__file__))
agents_dir = os.path.join(current_dir, "agents")
sys.path.append(agents_dir)

from agents.workflow_orchestrator import WorkflowOrchestrator

def main():
    """Função principal do script"""
    parser = argparse.ArgumentParser(
        description="Workflow de Análise, Geração e Teste de Módulos OTClient",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python run_module_workflow.py --list-modules
  python run_module_workflow.py --module client --variations 3
  python run_module_workflow.py --module game_inventory --config config.json
  python run_module_workflow.py --list-workflows
  python run_module_workflow.py --status workflow_client_1234567890
        """
    )
    
    # Argumentos principais
    parser.add_argument(
        "--module", "-m",
        type=str,
        help="Nome do módulo OTClient a processar"
    )
    
    parser.add_argument(
        "--list-modules", "-l",
        action="store_true",
        help="Listar todos os módulos disponíveis"
    )
    
    parser.add_argument(
        "--list-workflows", "-w",
        action="store_true",
        help="Listar todos os workflows executados"
    )
    
    parser.add_argument(
        "--status", "-s",
        type=str,
        help="Verificar status de um workflow específico (ID do workflow)"
    )
    
    # Configurações do workflow
    parser.add_argument(
        "--variations", "-v",
        type=int,
        default=3,
        help="Número de variações a gerar (padrão: 3)"
    )
    
    parser.add_argument(
        "--save-files",
        action="store_true",
        help="Salvar arquivos físicos das variações geradas"
    )
    
    parser.add_argument(
        "--no-learning",
        action="store_true",
        help="Desabilitar fase de aprendizado"
    )
    
    parser.add_argument(
        "--config", "-c",
        type=str,
        help="Arquivo de configuração JSON"
    )
    
    parser.add_argument(
        "--workspace", "-p",
        type=str,
        help="Caminho do workspace (padrão: diretório atual)"
    )
    
    # Argumentos de debug
    parser.add_argument(
        "--verbose", "-V",
        action="store_true",
        help="Modo verboso com mais informações"
    )
    
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Executar em modo de teste (não salvar arquivos)"
    )
    
    args = parser.parse_args()
    
    # Configurar workspace
    workspace_path = args.workspace or os.getcwd()
    
    # Inicializar orquestrador
    try:
        orchestrator = WorkflowOrchestrator(workspace_path)
    except Exception as e:
        print(f"❌ Erro ao inicializar orquestrador: {e}")
        return 1
    
    # Comando: Listar módulos
    if args.list_modules:
        print("📋 Módulos OTClient disponíveis:")
        print("=" * 50)
        
        modules = orchestrator.get_available_modules()
        if not modules:
            print("❌ Nenhum módulo encontrado")
            return 1
        
        for i, module in enumerate(modules, 1):
            print(f"{i:3d}. {module}")
        
        print(f"\nTotal: {len(modules)} módulos")
        return 0
    
    # Comando: Listar workflows
    if args.list_workflows:
        print("📋 Workflows executados:")
        print("=" * 60)
        
        workflows = orchestrator.list_workflows()
        if not workflows:
            print("❌ Nenhum workflow encontrado")
            return 0
        
        for i, workflow in enumerate(workflows, 1):
            workflow_id = workflow.get("workflow_id", "N/A")
            module_name = workflow.get("module_name", "N/A")
            start_time = workflow.get("start_time", "N/A")
            status = workflow.get("status", "N/A")
            
            print(f"{i:3d}. {workflow_id}")
            print(f"     Módulo: {module_name}")
            print(f"     Início: {start_time}")
            print(f"     Status: {status}")
            print()
        
        print(f"Total: {len(workflows)} workflows")
        return 0
    
    # Comando: Verificar status
    if args.status:
        print(f"📊 Status do workflow: {args.status}")
        print("=" * 50)
        
        status = orchestrator.get_workflow_status(args.status)
        if "error" in status:
            print(f"❌ {status['error']}")
            return 1
        
        # Exibir informações do workflow
        print(f"ID: {status.get('workflow_id', 'N/A')}")
        print(f"Módulo: {status.get('module_name', 'N/A')}")
        print(f"Início: {status.get('start_time', 'N/A')}")
        print(f"Fim: {status.get('end_time', 'N/A')}")
        
        summary = status.get("summary", {})
        print(f"Status: {summary.get('overall_status', 'N/A')}")
        print(f"Duração: {summary.get('total_duration', 0):.2f}s")
        print(f"Fases completadas: {summary.get('phases_completed', 0)}/{summary.get('total_phases', 0)}")
        
        key_metrics = summary.get("key_metrics", {})
        if key_metrics:
            print("\nMétricas chave:")
            for metric, value in key_metrics.items():
                if isinstance(value, float):
                    print(f"  {metric}: {value:.2f}")
                else:
                    print(f"  {metric}: {value}")
        
        return 0
    
    # Comando: Executar workflow
    if args.module:
        print(f"🚀 Executando workflow para módulo: {args.module}")
        print("=" * 60)
        
        # Verificar se módulo existe
        available_modules = orchestrator.get_available_modules()
        if args.module not in available_modules:
            print(f"❌ Módulo '{args.module}' não encontrado")
            print(f"📋 Módulos disponíveis: {',
    '.join(available_modules[:10])}{'...' if len(available_modules) > 10 else ''}")
            return 1
        
        # Carregar configuração
        config = {}
        if args.config:
            try:
                with open(args.config, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                print(f"✅ Configuração carregada de: {args.config}")
            except Exception as e:
                print(f"⚠️ Erro ao carregar configuração: {e}")
                print("Usando configurações padrão")
        
        # Configurar parâmetros
        workflow_config = {
            "variation_count": args.variations,
            "test_all_variations": True,
            "save_physical_files": args.save_files,
            "enable_learning": not args.no_learning,
            "log_level": "DEBUG" if args.verbose else "INFO"
        }
        
        # Atualizar com configuração do arquivo
        config.update(workflow_config)
        
        # Modo dry-run
        if args.dry_run:
            print("🧪 Modo dry-run ativado - não serão salvos arquivos")
            config["save_physical_files"] = False
        
        # Exibir configuração
        if args.verbose:
            print("\nConfiguração do workflow:")
            for key, value in config.items():
                print(f"  {key}: {value}")
            print()
        
        try:
            # Executar workflow
            results = orchestrator.execute_workflow(args.module, config)
            
            # Exibir resultados
            print("\n" + "=" * 60)
            print("📊 RESULTADOS DO WORKFLOW")
            print("=" * 60)
            
            summary = results.get("summary", {})
            print(f"Status: {summary.get('overall_status', 'N/A')}")
            print(f"Duração total: {summary.get('total_duration', 0):.2f}s")
            print(f"Fases completadas: {summary.get('phases_completed', 0)}/{summary.get('total_phases', 0)}")
            
            key_metrics = summary.get("key_metrics", {})
            if key_metrics:
                print("\nMétricas chave:")
                for metric, value in key_metrics.items():
                    if isinstance(value, float):
                        print(f"  {metric}: {value:.2f}")
                    else:
                        print(f"  {metric}: {value}")
            
            # Exibir erros se houver
            errors = results.get("errors", [])
            if errors:
                print(f"\n❌ Erros encontrados ({len(errors)}):")
                for error in errors:
                    print(f"  - {error}")
            
            # Exibir avisos se houver
            warnings = results.get("warnings", [])
            if warnings:
                print(f"\n⚠️ Avisos ({len(warnings)}):")
                for warning in warnings:
                    print(f"  - {warning}")
            
            print(f"\n✅ Workflow concluído!")
            print(f"📁 Resultados salvos em: wiki/bmad/results/")
            
            return 0
            
        except Exception as e:
            print(f"❌ Erro durante execução do workflow: {e}")
            if args.verbose:
                import traceback
                traceback.print_exc()
            return 1
    
    # Se nenhum comando foi especificado
    if not any([args.list_modules, args.list_workflows, args.status, args.module]):
        parser.print_help()
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code) 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = WorkflowmanagerModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script run_module_workflow.py executado com sucesso via módulo agents.workflow_manager")
    else:
        print(f"❌ Erro na execução do script run_module_workflow.py via módulo agents.workflow_manager")
