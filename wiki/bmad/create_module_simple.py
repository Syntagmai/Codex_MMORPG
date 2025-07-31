#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 Script simplificado para criar módulo do zero
"""
import os
import sys
import json
from pathlib import Path

# Adicionar o diretório de agentes ao path
current_dir = os.path.dirname(os.path.abspath(__file__))
agents_dir = os.path.join(current_dir, "agents")
sys.path.insert(0, agents_dir)

from module_creator import ModuleCreatorAgent

def main():
    print("🚀 Criando módulo do zero baseado na wiki...")
    print("=" * 60)
    
    # Criar módulo do zero
    creator = ModuleCreatorAgent()
    creation_result = creator.create_module_from_scratch()
    
    if not creation_result["success"]:
        print("❌ Falha na criação do módulo")
        return
    
    print(f"✅ Módulo criado com sucesso: {creation_result['module_name']}")
    print(f"📁 Localização: {creation_result['module_path']}")
    print(f"📄 Arquivos criados: {list(creation_result['files_created'].keys())}")
    
    # Verificar se o módulo está na pasta modules
    if os.path.exists(creation_result["module_path"]):
        print(f"✅ Módulo encontrado na pasta modules/")
        print(f"📂 Caminho completo: {os.path.abspath(creation_result['module_path'])}")
        
        # Listar arquivos criados
        print("\n📋 Arquivos do módulo:")
        for file_type, file_path in creation_result["files_created"].items():
            if os.path.exists(file_path):
                file_size = os.path.getsize(file_path)
                print(f"  • {file_type}: {os.path.basename(file_path)} ({file_size} bytes)")
            else:
                print(f"  • {file_type}: {os.path.basename(file_path)} (NÃO ENCONTRADO)")
    else:
        print("❌ Módulo não encontrado na pasta modules/")
    
    print("\n🎉 Módulo criado com sucesso!")
    print("=" * 60)

if __name__ == "__main__":
    main() 