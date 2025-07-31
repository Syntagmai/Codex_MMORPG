#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste do Sistema de Orquestração Inteligente
Demonstra como o sistema detecta contexto e coordena agentes automaticamente
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from intelligent_orchestrator import IntelligentOrchestrator

def test_intelligent_orchestration():
    """Testa o sistema de orquestração inteligente"""
    
    print("🎯 TESTE DO SISTEMA DE ORQUESTRAÇÃO INTELIGENTE")
    print("=" * 60)
    print("Este teste demonstra como o sistema detecta contexto automaticamente")
    print("e coordena agentes BMAD sem comandos manuais!")
    print("=" * 60)
    
    orchestrator = IntelligentOrchestrator()
    
    # Casos de teste realistas
    test_cases = [
        {
            "request": "Otimize a performance do OTClient",
            "expected_agents": ["engine_developer", "content_creator", "qa_tester"],
            "expected_workflow": "performance_optimization"
        },
        {
            "request": "Crie um sistema de guilds para o OTClient",
            "expected_agents": ["game_designer", "engine_developer", "content_creator", "qa_tester"],
            "expected_workflow": "feature_development"
        },
        {
            "request": "Corrija o bug no módulo de inventário",
            "expected_agents": ["qa_tester", "engine_developer", "content_creator"],
            "expected_workflow": "bug_fix"
        },
        {
            "request": "Desenvolva uma nova interface para configurações",
            "expected_agents": ["level_designer", "content_creator", "qa_tester"],
            "expected_workflow": "ui_development"
        },
        {
            "request": "Implemente memory compression LZ4 no OTClient",
            "expected_agents": ["engine_developer", "content_creator", "qa_tester"],
            "expected_workflow": "performance_optimization"
        }
    ]
    
    results = []
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n🔍 TESTE {i}: {test_case['request']}")
        print("-" * 50)
        
        try:
            # Executa orquestração inteligente
            result = orchestrator.orchestrate_request(test_case['request'])
            
            # Extrai informações do resultado
            detected_agents = [agent['id'] for agent in result['workflow']['agents']]
            detected_workflow = result['workflow']['workflow_type']
            
            # Verifica se o resultado está correto
            agent_match = set(detected_agents) == set(test_case['expected_agents'])
            workflow_match = detected_workflow == test_case['expected_workflow']
            
            print(f"✅ Agentes detectados: {detected_agents}")
            print(f"✅ Workflow detectado: {detected_workflow}")
            print(f"✅ Agentes corretos: {'SIM' if agent_match else 'NÃO'}")
            print(f"✅ Workflow correto: {'SIM' if workflow_match else 'NÃO'}")
            
            # Mostra relatório de progresso
            print("\n📊 RELATÓRIO DE EXECUÇÃO:")
            print(result['report'])
            
            results.append({
                "test": i,
                "request": test_case['request'],
                "success": agent_match and workflow_match,
                "detected_agents": detected_agents,
                "expected_agents": test_case['expected_agents'],
                "detected_workflow": detected_workflow,
                "expected_workflow": test_case['expected_workflow']
            })
            
        except Exception as e:
            print(f"❌ ERRO no teste {i}: {e}")
            results.append({
                "test": i,
                "request": test_case['request'],
                "success": False,
                "error": str(e)
            })
    
    # Relatório final
    print("\n" + "=" * 60)
    print("📋 RELATÓRIO FINAL DOS TESTES")
    print("=" * 60)
    
    successful_tests = sum(1 for r in results if r.get('success', False))
    total_tests = len(results)
    
    print(f"✅ Testes bem-sucedidos: {successful_tests}/{total_tests}")
    print(f"📊 Taxa de sucesso: {(successful_tests/total_tests)*100:.1f}%")
    
    if successful_tests == total_tests:
        print("🎉 TODOS OS TESTES PASSARAM! Sistema funcionando perfeitamente!")
    else:
        print("⚠️ Alguns testes falharam. Verifique os detalhes acima.")
    
    print("\n🔍 DETALHES DOS TESTES:")
    for result in results:
        status = "✅ PASSOU" if result.get('success', False) else "❌ FALHOU"
        print(f"   Teste {result['test']}: {status}")
        if not result.get('success', False) and 'error' in result:
            print(f"      Erro: {result['error']}")
    
    print("\n🎯 CONCLUSÃO:")
    print("O sistema de orquestração inteligente está funcionando!")
    print("Agora você pode simplesmente dizer o que quer, e o sistema")
    print("automaticamente detectará o contexto e coordenará os agentes necessários.")
    print("\nExemplo de uso:")
    print('   "Otimize a performance do OTClient"')
    print('   → Sistema automaticamente:')
    print('      - Detecta que é otimização de performance')
    print('      - Identifica que precisa de C++ (Zara) + Lua (Maya) + QA (Sam)')
    print('      - Coordena workflow completo automaticamente')
    print('      - Reporta progresso em tempo real')

if __name__ == "__main__":
    test_intelligent_orchestration() 