"""
migrated_integrated_navigation_agent



Módulo: migrated_integrated_navigation_agent
Caminho: wiki\update\modules\agents\agent_orchestrator\migrated_integrated_navigation_agent.py
Linhas de código: 468
Complexidade: 43.00

Funções (12):
- main(): Função principal para teste do agente integrado...\n- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self): ...\n- navigate(self, query, context, strategy): Navegação integrada com múltiplas estratégias

Est...\n- json_navigation(self, query, context): Navegação JSON tradicional...\n- graph_navigation(self, query, context): Navegação por grafos...\n- hybrid_navigation(self, query, context): Navegação híbrida - combina JSON e grafos...\n- integrate_results(self, json_results, graph_results, context): Integra resultados de JSON e grafos...\n- calculate_confidence_scores(self, integrated_results): Calcula scores de confiança para os resultados...\n- generate_suggestions(self, query, context, results): Gera sugestões de navegação...\n- get_performance_report(self): Gera relatório de performance...\n- optimize_navigation(self): Otimiza a navegação integrada...\n
Classes (1):
- IntegratedNavigationAgent: Agente que integra navegação JSON e grafos...\n  - __init__(self): ...\n  - navigate(self, query, context, strategy): Navegação integrada com múltip...\n  - json_navigation(self, query, context): Navegação JSON tradicional...\n  - graph_navigation(self, query, context): Navegação por grafos...\n  - hybrid_navigation(self, query, context): Navegação híbrida - combina JS...\n  - integrate_results(self, json_results, graph_results, context): Integra resultados de JSON e g...\n  - calculate_confidence_scores(self, integrated_results): Calcula scores de confiança pa...\n  - generate_suggestions(self, query, context, results): Gera sugestões de navegação...\n  - get_performance_report(self): Gera relatório de performance...\n  - optimize_navigation(self): Otimiza a navegação integrada...\n
Imports (4):
.AgentorchestratorModule, json, time, datetime.datetime

Autor: Documentation Agent
Data: 2025-08-01 15:05:58
"""

## 🔗 **Links Automáticos - Scripts**

> [!info] **Script de Automação**
> Este script faz parte do sistema de automação da wiki

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]

### **🔧 Links de Scripts**
- [[../update/README|Documentação de Scripts]]
- [[../maps/scripts_index|Índice de Scripts]]
- [[../templates/README|Templates de Scripts]]

### **📊 Scripts Relacionados**
- [[../update/automatic_linkage_system.py|automatic_linkage_system.py]]
- [[../update/create_automatic_link_templates.py|create_automatic_link_templates.py]]
- [[../update/orphan_files_analyzer.py|orphan_files_analyzer.py]]
- [[../update/update_json_maps.py|update_json_maps.py]]

### **📈 Métricas do Script**
- **Nome**: docstring
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

