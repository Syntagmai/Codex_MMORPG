#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para atualizar o orquestrador inteligente com o novo agente Python
"""

import re
import os
from pathlib import Path

def update_orchestrator_with_python_agent():
    """Atualiza o orquestrador com o novo agente Python"""
    
    orchestrator_file = Path("enhanced_intelligent_orchestrator.py")
    
    if not orchestrator_file.exists():
        print("❌ Arquivo do orquestrador não encontrado")
        return False
    
    # Ler conteúdo atual
    with open(orchestrator_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Atualizar extensões de arquivo para usar python_agent
    content = re.sub(
        r'\.py": \["content_creator", "scripting"\]',
        '.py": ["python_agent", "python_development"]',
        content
    )
    
    # 2. Adicionar padrões de contexto Python
    python_patterns = '''            "python_file_edit": {
                "keywords": ["editar", "arquivo", "python", ".py", "script", "automação"],
                "agents": ["python_agent"],
                "workflow": "python_development"
            },
            "python_optimization": {
                "keywords": ["otimizar", "python", "qualidade", "refatorar", "melhorar"],
                "agents": ["python_agent"],
                "workflow": "python_optimization"
            },
            "python_bug_fix": {
                "keywords": ["bug", "python", "erro", "corrigir", "problema"],
                "agents": ["python_agent", "qa_tester"],
                "workflow": "python_bug_fix"
            },
'''
    
    # Inserir após o padrão "documentation"
    content = re.sub(
        r'("documentation": \{[\s\S]*?\},)',
        r'\1\n' + python_patterns,
        content
    )
    
    # 3. Adicionar tecnologia Python
    python_technology = '''            "Python": {
                "keywords": ["Python", "python", "py", "script", "automação", "scripting"],
                "agents": ["python_agent"],
                "workflows": ["python_development", "python_optimization", "python_bug_fix"]
            },
'''
    
    # Inserir após a tecnologia "Lua"
    content = re.sub(
        r'("Lua": \{[\s\S]*?\},)',
        r'\1\n' + python_technology,
        content
    )
    
    # 4. Adicionar workflows Python
    python_workflows = '''            "python_development": {
                "agents": ["python_agent"],
                "phases": ["analysis", "implementation", "optimization", "testing"],
                "description": "Desenvolvimento de scripts Python",
                "estimated_duration": "1-2 hours"
            },
            "python_optimization": {
                "agents": ["python_agent"],
                "phases": ["analysis", "optimization", "validation"],
                "description": "Otimização de código Python existente",
                "estimated_duration": "30min-1h"
            },
            "python_bug_fix": {
                "agents": ["python_agent", "qa_tester"],
                "phases": ["identification", "fix", "validation"],
                "description": "Correção de bugs em código Python",
                "estimated_duration": "1-2 hours"
            },
'''
    
    # Encontrar onde inserir os workflows (após o último workflow existente)
    workflow_pattern = r'("documentation": \{[\s\S]*?"estimated_duration": "[^"]*"\s*\})'
    match = re.search(workflow_pattern, content)
    if match:
        insert_pos = match.end()
        content = content[:insert_pos] + ',\n' + python_workflows + content[insert_pos:]
    
    # 5. Adicionar personalidade do agente Python
    python_personality = '''            "python_agent": {
                "name": "Py",
                "expertise": "Python Development, Code Quality, Automation Scripts",
                "personality": "Analytical, quality-focused, continuous optimizer",
                "specializations": ["Python", "Code Quality", "Automation", "Scripting"]
            },
'''
    
    # Encontrar onde inserir a personalidade (após o último agente existente)
    personality_pattern = r'("game_team_orchestrator": \{[\s\S]*?"specializations": \[[^\]]*\]\s*\})'
    match = re.search(personality_pattern, content)
    if match:
        insert_pos = match.end()
        content = content[:insert_pos] + ',\n' + python_personality + content[insert_pos:]
    
    # 6. Adicionar roles do agente Python
    python_roles = '''            "python_development": {
                "python_agent": "Analisa, implementa e otimiza scripts Python"
            },
            "python_optimization": {
                "python_agent": "Otimiza código Python existente e melhora qualidade"
            },
            "python_bug_fix": {
                "python_agent": "Identifica e corrige bugs em código Python",
                "qa_tester": "Valida correções e testa funcionalidade"
            },
'''
    
    # Encontrar onde inserir os roles (após o último role existente)
    role_pattern = r'("documentation": \{[\s\S]*?"content_creator": "[^"]*",\s*"game_designer": "[^"]*"\s*\})'
    match = re.search(role_pattern, content)
    if match:
        insert_pos = match.end()
        content = content[:insert_pos] + ',\n' + python_roles + content[insert_pos:]
    
    # 7. Atualizar get_agents_for_phase para incluir fases Python
    python_phases = '''            "analysis": [a for a in agents if a['id'] in ['python_agent', 'engine_developer', 'content_creator']],
            "implementation": [a for a in agents if a['id'] in ['python_agent', 'engine_developer', 'content_creator']],
            "optimization": [a for a in agents if a['id'] in ['python_agent', 'engine_developer']],
            "validation": [a for a in agents if a['id'] in ['python_agent', 'qa_tester']],
'''
    
    # Encontrar onde inserir as fases (após a fase "review")
    phase_pattern = r'("review": \[a for a in agents if a\[\'id\'\] in \[\'game_designer\'\]\})'
    match = re.search(phase_pattern, content)
    if match:
        insert_pos = match.end()
        content = content[:insert_pos] + ',\n' + python_phases + content[insert_pos:]
    
    # Salvar arquivo atualizado
    with open(orchestrator_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Orquestrador atualizado com sucesso!")
    print("✅ Agente Python integrado ao sistema")
    
    return True

def create_python_agent_integration_test():
    """Cria teste de integração do agente Python"""
    
    test_content = '''#!/usr/bin/env python3
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
        print(f"\\n🔍 {scenario['name']}")
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
            print("\\n👥 Agentes Selecionados:")
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
    print("\\n" + "=" * 50)
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
    # Atualizar orquestrador
    success = update_orchestrator_with_python_agent()
    
    if success:
        # Criar teste de integração
        test_file = "python_agent_integration_test.py"
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write(test_content)
        
        print(f"✅ Teste de integração criado: {test_file}")
        print("\\n🚀 Para testar a integração, execute:")
        print(f"python {test_file}")
    else:
        print("❌ Falha ao atualizar orquestrador")
'''
    
    return test_content

def main():
    """Função principal"""
    print("🔧 ATUALIZANDO ORQUESTRADOR COM AGENTE PYTHON")
    print("=" * 50)
    
    # Atualizar orquestrador
    success = update_orchestrator_with_python_agent()
    
    if success:
        # Criar teste de integração
        test_content = create_python_agent_integration_test()
        test_file = "python_agent_integration_test.py"
        
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write(test_content)
        
        print(f"✅ Teste de integração criado: {test_file}")
        print("\n🚀 Para testar a integração, execute:")
        print(f"python {test_file}")
        
        print("\n📋 PRÓXIMOS PASSOS:")
        print("1. ✅ Agente Python criado")
        print("2. ✅ Orquestrador atualizado")
        print("3. ✅ Teste de integração criado")
        print("4. 🔄 Execute o teste para validar integração")
        print("5. 🔄 Teste com cenários reais de Python")
    else:
        print("❌ Falha ao atualizar orquestrador")

if __name__ == "__main__":
    main() 