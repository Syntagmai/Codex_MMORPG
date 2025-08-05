"""
migrated_progress_tracker_agent



Módulo: migrated_progress_tracker_agent
Caminho: wiki\update\modules\agents\agent_orchestrator\migrated_progress_tracker_agent.py
Linhas de código: 537
Complexidade: 38.00

Funções (17):
- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self): ...\n- load_configuration(self): Carrega configurações do sistema...\n- calculate_current_metrics(self): Calcula métricas atuais do sistema...\n- calculate_general_progress(self, content): Calcula progresso geral do sistema...\n- calculate_epics_progress(self, content): Calcula progresso das epics...\n- calculate_stories_progress(self, content): Calcula progresso das stories...\n- calculate_agents_progress(self, content): Calcula progresso dos agentes...\n- calculate_tasks_progress(self, content): Calcula progresso das tasks...\n- calculate_roadmaps_progress(self, content): Calcula progresso dos roadmaps...\n- calculate_planejamentos_progress(self, content): Calcula progresso dos planejamentos...\n- calculate_velocity(self): Calcula velocidade de progresso...\n- calculate_trends(self): Calcula tendências de progresso...\n- generate_alerts(self, content): Gera alertas baseados no conteúdo atual...\n- save_metrics(self, metrics): Salva métricas atuais...\n- generate_dashboard_report(self): Gera relatório de dashboard...\n- run(self): Executa o Progress Tracker Agent...\n
Classes (1):
- ProgressTrackerAgent: ...\n  - __init__(self): ...\n  - load_configuration(self): Carrega configurações do siste...\n  - calculate_current_metrics(self): Calcula métricas atuais do sis...\n  - calculate_general_progress(self, content): Calcula progresso geral do sis...\n  - calculate_epics_progress(self, content): Calcula progresso das epics...\n  - calculate_stories_progress(self, content): Calcula progresso das stories...\n  - calculate_agents_progress(self, content): Calcula progresso dos agentes...\n  - calculate_tasks_progress(self, content): Calcula progresso das tasks...\n  - calculate_roadmaps_progress(self, content): Calcula progresso dos roadmaps...\n  - calculate_planejamentos_progress(self, content): Calcula progresso dos planejam...\n  - calculate_velocity(self): Calcula velocidade de progress...\n  - calculate_trends(self): Calcula tendências de progress...\n  - generate_alerts(self, content): Gera alertas baseados no conte...\n  - save_metrics(self, metrics): Salva métricas atuais...\n  - generate_dashboard_report(self): Gera relatório de dashboard...\n  - run(self): Executa o Progress Tracker Age...\n
Imports (4):
.AgentorchestratorModule, json, logging, re

Autor: Documentation Agent
Data: 2025-08-01 15:05:59
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

