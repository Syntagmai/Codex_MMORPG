# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
TIMEOUT_SECONDS = 60

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: example_integration.py
Módulo de Destino: tools.git_automation
Data de Migração: 2025-08-01 12:21:44

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import GitautomationModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de Integração: Auto-Aprendizado com Sistema de Regras
Demonstra como o sistema aprende e melhora regras automaticamente
"""

from datetime import datetime

def exemplo_integracao_regras():
    """Exemplo de como o sistema integra auto-aprendizado com regras"""
    
    # Inicializar sistema
    print("🚀 Inicializando Sistema de Auto-Aprendizado com Integração de Regras...")
    auto_learning = AutoLearningSystem()
    
    # Simular interações que usam regras
    interacoes_exemplo = [
        {
            "user_request": "Criar documentação para módulo Lua",
            "context_detected": {
                "technologies": ["Lua", "OTClient"],
                "task_type": "documentation",
                "complexity": "medium"
            },
            "agents_selected": ["Content Creator", "Lua Agent"],
            "workflow_executed": "documentation_workflow",
            "execution_time": 45.2,
            "success_score": 0.85,
            "rules_used": ["documentation-rules.md", "wiki-rules.md"]
        },
        {
            "user_request": "Otimizar código C++ do cliente",
            "context_detected": {
                "technologies": ["C++", "OTClient"],
                "task_type": "optimization",
                "complexity": "high"
            },
            "agents_selected": ["Engine Developer", "Python Agent"],
            "workflow_executed": "optimization_workflow",
            "execution_time": 120.5,
            "success_score": 0.92,
            "rules_used": ["bmad-system-rules.md", "intelligent-orchestration-rules.md"]
        },
        {
            "user_request": "Criar nova regra para indexação",
            "context_detected": {
                "technologies": ["Python", "JSON"],
                "task_type": "rule_creation",
                "complexity": "low"
            },
            "agents_selected": ["Python Agent"],
            "workflow_executed": "rule_creation_workflow",
            "execution_time": 25.8,
            "success_score": 0.78,
            "rules_used": ["template.md", "system-rules.md"]
        }
    ]
    
    # Registrar interações
    print("📝 Registrando interações de exemplo...")
    for i, dados in enumerate(interacoes_exemplo):
        interacao = InteractionData(
            timestamp=datetime.now().isoformat(),
            user_request=dados["user_request"],
            context_detected=dados["context_detected"],
            agents_selected=dados["agents_selected"],
            workflow_executed=dados["workflow_executed"],
            execution_time=dados["execution_time"],
            success_score=dados["success_score"],
            rules_used=dados["rules_used"]
        )
        
        auto_learning.record_interaction(interacao)
        print(f"  ✅ Interação {i+1} registrada")
    
    # Aguardar processamento
    print("⏳ Aguardando processamento de aprendizado...")
    import time
    time.sleep(5)
    
    # Analisar padrões de regras
    print("🔍 Analisando padrões de uso das regras...")
    padroes_regras = auto_learning.analyze_rule_patterns()
    print(f"  📊 {len(padroes_regras)} padrões de regras identificados")
    
    # Obter recomendações de regras
    print("💡 Obtendo recomendações de regras...")
    contexto_exemplo = {
        "technologies": ["Lua", "OTClient"],
        "task_type": "documentation",
        "complexity": "medium"
    }
    
    recomendacoes = auto_learning.get_rule_recommendations(contexto_exemplo)
    print(f"  🎯 {len(recomendacoes)} recomendações encontradas")
    
    for rec in recomendacoes:
        print(f"    📋 {rec['rule_file']} - Relevância: {rec['relevance_score']:.2f}")
    
    # Gerar relatório completo
    print("📊 Gerando relatório completo...")
    relatorio = auto_learning.generate_learning_report()
    
    print("\n" + "="*60)
    print("📋 RELATÓRIO DE APRENDIZADO COM INTEGRAÇÃO DE REGRAS")
    print("="*60)
    
    # Estatísticas gerais
    stats = relatorio['stats']
    print(f"📈 Total de Interações: {stats['total_interactions']}")
    print(f"🧠 Padrões Aprendidos: {stats['patterns_learned']}")
    print(f"⚡ Otimizações Aplicadas: {stats['optimizations_applied']}")
    
    # Análise de regras
    if 'rules_learning' in relatorio:
        rules_data = relatorio['rules_learning']
        print(f"\n📚 ANÁLISE DE REGRAS:")
        print(f"  📖 Regras Analisadas: {rules_data.get('total_rules_analyzed', 0)}")
        print(f"  🔧 Otimizações Geradas: {rules_data.get('optimizations_generated', 0)}")
        
        usage_stats = rules_data.get('usage_statistics', {})
        print(f"  📊 Total de Usos: {usage_stats.get('total_usage_events', 0)}")
        print(f"  🎯 Taxa de Sucesso Média: {usage_stats.get('avg_success_rate', 0):.2f}")
    
    # Recomendações
    print(f"\n💡 RECOMENDAÇÕES:")
    for rec in relatorio['recommendations']:
        print(f"  • {rec}")
    
    print("\n" + "="*60)
    print("✅ Exemplo de integração concluído!")
    print("="*60)
    
    return auto_learning

def exemplo_otimizacao_automatica_regras():
    """Exemplo de otimização automática de regras"""
    
    print("\n🔧 EXEMPLO DE OTIMIZAÇÃO AUTOMÁTICA DE REGRAS")
    print("="*60)
    
    auto_learning = AutoLearningSystem()
    
    # Simular mais interações para gerar padrões
    print("📝 Simulando interações adicionais...")
    for i in range(10):
        interacao = InteractionData(
            timestamp=datetime.now().isoformat(),
            user_request=f"Tarefa de exemplo {i+1}",
            context_detected={
                "technologies": ["Python", "Lua"] if i % 2 == 0 else ["C++", "OTClient"],
                "task_type": "development" if i % 3 == 0 else "documentation",
                "complexity": "medium"
            },
            agents_selected=["Python Agent", "Content Creator"],
            workflow_executed="standard_workflow",
            execution_time=30.0 + i * 5,
            success_score=0.7 + (i * 0.02),
            rules_used=["bmad-system-rules.md", "auto-learning-rules.md"]
        )
        
        auto_learning.record_interaction(interacao)
    
    # Aguardar processamento
    import time
    time.sleep(3)
    
    # Aplicar otimizações de regras
    print("⚡ Aplicando otimizações automáticas de regras...")
    otimizacoes = auto_learning.apply_rule_optimizations()
    
    if otimizacoes:
        print(f"  ✅ {len(otimizacoes)} otimizações aplicadas:")
        for opt in otimizacoes:
            print(f"    🔧 Regra {opt['rule_id']} - Confiança: {opt['confidence']:.2f}")
    else:
        print("  ℹ️ Nenhuma otimização aplicada (threshold de confiança não atingido)")
    
    print("✅ Exemplo de otimização concluído!")

if __name__ == "__main__":
    # Executar exemplos
    auto_learning = exemplo_integracao_regras()
    exemplo_otimizacao_automatica_regras()
    
    print("\n🎉 Todos os exemplos executados com sucesso!")
    print("O sistema de auto-aprendizado está integrado com o sistema de regras!") 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = GitautomationModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script example_integration.py executado com sucesso via módulo tools.git_automation")
    else:
        print(f"❌ Erro na execução do script example_integration.py via módulo tools.git_automation")
