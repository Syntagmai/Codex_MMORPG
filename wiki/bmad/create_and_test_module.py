#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 Script para criar módulo do zero e testá-lo automaticamente
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
from module_tester import ModuleTesterAgent
from workflow_orchestrator import WorkflowOrchestrator

def main():
    print("🚀 Iniciando criação e teste de módulo do zero...")
    print("=" * 60)
    
    # 1. Criar módulo do zero
    print("🤖 Fase 1: Criando módulo do zero...")
    creator = ModuleCreatorAgent()
    creation_result = creator.create_module_from_scratch()
    
    if not creation_result["success"]:
        print("❌ Falha na criação do módulo")
        return
    
    print(f"✅ Módulo criado: {creation_result['module_name']}")
    print(f"📁 Localização: {creation_result['module_path']}")
    
    # 2. Testar o módulo criado
    print("\n🧪 Fase 2: Testando módulo criado...")
    tester = ModuleTesterAgent()
    
    # Preparar dados para teste (formato esperado pelo tester)
    test_variation = {
        "name": creation_result["module_name"],
        "variation_name": creation_result["module_name"],
        "variation_id": creation_result["module_name"],
        "path": creation_result["module_path"],
        "files": creation_result["files_created"],
        "concept": creation_result.get("concept", {})
    }
    
    # Executar testes
    test_result = tester.test_single_variation(test_variation, "created_module")
    
    print(f"✅ Testes concluídos para: {creation_result['module_name']}")
    
    # 3. Gerar relatório final
    print("\n📊 Fase 3: Gerando relatório final...")
    
    final_report = {
        "creation": creation_result,
        "testing": test_result,
        "summary": {
            "module_name": creation_result["module_name"],
            "module_path": creation_result["module_path"],
            "creation_success": creation_result["success"],
            "test_score": test_result.get("overall_score", 0.0),
            "test_status": test_result.get("status", "unknown")
        }
    }
    
    # Salvar relatório
    report_file = os.path.join(creator.results_path, "created_modules", f"{creation_result['module_name']}_final_report.json")
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(final_report, f, indent=2, ensure_ascii=False)
    
    # 4. Exibir resultados
    print("\n" + "=" * 60)
    print("📋 RELATÓRIO FINAL")
    print("=" * 60)
    print(f"🎯 Módulo: {creation_result['module_name']}")
    print(f"📁 Localização: {creation_result['module_path']}")
    print(f"✅ Criação: {'Sucesso' if creation_result['success'] else 'Falha'}")
    print(f"🧪 Score de Teste: {test_result.get('overall_score', 0.0):.2f}/10.0")
    print(f"📊 Status: {test_result.get('status', 'Desconhecido')}")
    print(f"📄 Arquivos criados: {list(creation_result['files_created'].keys())}")
    print(f"📋 Relatório salvo em: {report_file}")
    
    # Verificar se o módulo está na pasta modules
    if os.path.exists(creation_result["module_path"]):
        print(f"✅ Módulo encontrado na pasta modules/")
        print(f"📂 Caminho completo: {os.path.abspath(creation_result['module_path'])}")
    else:
        print("❌ Módulo não encontrado na pasta modules/")
    
    print("\n🎉 Processo concluído com sucesso!")
    print("=" * 60)

if __name__ == "__main__":
    main() 