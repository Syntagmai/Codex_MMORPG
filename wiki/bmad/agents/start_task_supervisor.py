#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Start Task Supervisor - Script de Inicialização
==============================================

Script para iniciar o Task Supervisor Agent em modo de monitoramento contínuo.

Autor: Sistema BMAD
Versão: 1.0.0
Data: 2025-08-01
"""

import sys
import time
import subprocess
from pathlib import Path

def main():
    """
    Função principal para iniciar o Task Supervisor Agent.
    """
    print("🎯 Iniciando Task Supervisor Agent...")
    print("=" * 50)
    
    # Verificar se o agente existe
    agent_path = Path("wiki/bmad/agents/task_supervisor_agent.py")
    if not agent_path.exists():
        print("❌ Task Supervisor Agent não encontrado!")
        print(f"Procurando em: {agent_path.absolute()}")
        sys.exit(1)
    
    print("✅ Task Supervisor Agent encontrado")
    print("🔄 Iniciando monitoramento contínuo...")
    print("📋 Configurações:")
    print("   - Intervalo: 30 segundos")
    print("   - Cooldown: 5 minutos")
    print("   - Timeout: 60 segundos")
    print("")
    print("🎯 O supervisor irá:")
    print("   - Monitorar conclusão de tarefas")
    print("   - Detectar espera por instruções")
    print("   - Continuar automaticamente para próxima tarefa")
    print("   - Respeitar cooldown de 5 minutos")
    print("")
    print("🛑 Pressione Ctrl+C para parar")
    print("=" * 50)
    
    try:
        # Iniciar o agente em modo de monitoramento
        cmd = [
            sys.executable,
            str(agent_path),
            "--monitor",
            "--interval", "30"
        ]
        
        print(f"🚀 Executando: {' '.join(cmd)}")
        print("")
        
        # Executar o agente
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True
        )
        
        # Monitorar saída
        while True:
            output = process.stdout.readline()
            if output:
                print(output.strip())
            
            # Verificar se o processo ainda está rodando
            if process.poll() is not None:
                break
            
            time.sleep(0.1)
        
        # Verificar se houve erro
        if process.returncode != 0:
            stderr = process.stderr.read()
            if stderr:
                print(f"❌ Erro no Task Supervisor Agent:")
                print(stderr)
                sys.exit(1)
    
    except KeyboardInterrupt:
        print("\n🛑 Interrompido pelo usuário")
        if 'process' in locals():
            process.terminate()
            print("✅ Processo finalizado")
    
    except Exception as e:
        print(f"❌ Erro ao iniciar Task Supervisor Agent: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 