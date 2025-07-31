#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste de Integração do Agente Python
Testa se o agente Python é selecionado corretamente
"""

from enhanced_intelligent_orchestrator import EnhancedIntelligentOrchestrator

def test_python_agent_integration():
    """Testa integração do agente Python"""
    
    print("🐍 TESTE DE INTEGRAÇÃO DO AGENTE PYTHON")
    print("=" * 50)
    
    orchestrator = EnhancedIntelligentOrchestrator()
    
    # Cenários de teste para Python
    test_scenarios = [
        {
            "name": "Cenário 1: Edição de Arquivo Python",
            "request": "Vou editar um arquivo Python para criar um script de automação",
            "expected_agents": ["python_agent"],
            "expected_workflow": "python_development"
        },
        {
            "name": "Cenário 2: Otimização de Código Python",
            "request": "Preciso otimizar um script Python para melhorar a performance",
            "expected_agents": ["python_agent"],
            "expected_workflow": "python_optimization"
        },
        {
            "name": "Cenário 3: Correção de Bug em Python",
            "request": "Há um bug no script Python que precisa ser corrigido",
            "expected_agents": ["python_agent", "qa_tester"],
            "expected_workflow": "python_bug_fix"
        }
    ]
    
    results = []
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"\n🔍 {scenario['name']}")
        print(f"📝 Pedido: {scenario['request']}")
        print("-" * 50)
        
        try:
            # Executa orquestração
            result = orchestrator.orchestrate_request(scenario['request'])
            
            # Extrai informações do resultado
            detected_agents = [agent['id'] for agent in result['workflow']['agents']]
            detected_workflow = result['workflow']['workflow_type']
            
            # Verifica se o resultado está correto
            agent_match = set(detected_agents) == set(scenario['expected_agents'])
            workflow_match = detected_workflow == scenario['expected_workflow']
            
            print(f"✅ Agentes detectados: {detected_agents}")
            print(f"✅ Workflow detectado: {detected_workflow}")
            print(f"✅ Agentes corretos: {'SIM' if agent_match else 'NÃO'}")
            print(f"✅ Workflow correto: {'SIM' if workflow_match else 'NÃO'}")
            
            # Mostra detalhes dos agentes selecionados
            print("\n👥 Agentes Selecionados:")
            for agent in result['workflow']['agents']:
                print(f"   - {agent['name']} ({agent['role']})")
            
            results.append({
                "scenario": i,
                "name": scenario['name'],
                "success": agent_match and workflow_match,
                "detected_agents": detected_agents,
                "expected_agents": scenario['expected_agents'],
                "detected_workflow": detected_workflow,
                "expected_workflow": scenario['expected_workflow']
            })
            
        except Exception as e:
            print(f"❌ ERRO no cenário {i}: {e}")
            results.append({
                "scenario": i,
                "name": scenario['name'],
                "success": False,
                "error": str(e)
            })
    
    # Relatório final
    print("\n" + "=" * 50)
    print("📋 RELATÓRIO FINAL DOS CENÁRIOS PYTHON")
    print("=" * 50)
    
    successful_scenarios = sum(1 for r in results if r.get('success', False))
    total_scenarios = len(results)
    
    print(f"✅ Cenários bem-sucedidos: {successful_scenarios}/{total_scenarios}")
    print(f"📊 Taxa de sucesso: {(successful_scenarios/total_scenarios)*100:.1f}%")
    
    if successful_scenarios == total_scenarios:
        print("🎉 TODOS OS CENÁRIOS PYTHON PASSARAM! Agente Python integrado com sucesso!")
    else:
        print("⚠️ Alguns cenários falharam. Verifique a integração.")
    
    return results

if __name__ == "__main__":
    test_python_agent_integration()
