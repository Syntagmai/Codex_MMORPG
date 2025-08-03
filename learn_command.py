#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comando de Aprendizado - Sistema BMAD
=====================================

Script para executar comandos de aprendizado diretamente do chat.
Integra com o Learning Workflow Orchestrator para criar módulos com aprendizado contínuo.

Uso:
python learn_command.py create "module_name" "language" "purpose" [reference_source]
python learn_command.py report
python learn_command.py stats
python learn_command.py help

Autor: Sistema BMAD
Versão: 1.0.0
Data: 2025-01-27
"""

import sys
import os
from pathlib import Path

# Adicionar pasta de agentes ao path
current_dir = Path(__file__).parent
agents_dir = current_dir / "wiki" / "bmad" / "agents"
sys.path.insert(0, str(agents_dir))

try:
    from chat_learning_command import learn_create, learn_report, learn_stats, show_help
except ImportError as e:
    print(f"❌ Erro ao importar módulos: {e}")
    print("💡 Certifique-se de que os arquivos estão na pasta correta")
    sys.exit(1)

def main():
    """Função principal."""
    if len(sys.argv) < 2:
        print("🎓 Sistema de Aprendizado BMAD")
        print("=" * 40)
        show_help()
        return
    
    command = sys.argv[1].lower()
    
    try:
        if command == "create" and len(sys.argv) >= 5:
            module_name = sys.argv[2]
            language = sys.argv[3]
            purpose = sys.argv[4]
            reference_source = sys.argv[5] if len(sys.argv) > 5 else "otclient"
            
            print("🎓 Executando comando de aprendizado...")
            learn_create(module_name, language, purpose, reference_source)
            
        elif command == "report":
            learn_report()
            
        elif command == "stats":
            learn_stats()
            
        elif command == "help":
            show_help()
            
        else:
            print("❌ Comando inválido ou parâmetros incorretos")
            print("💡 Use 'python learn_command.py help' para ver os comandos disponíveis")
            
    except Exception as e:
        print(f"❌ Erro durante execução: {e}")
        print("📋 Verifique os logs para mais detalhes")

if __name__ == "__main__":
    main() 