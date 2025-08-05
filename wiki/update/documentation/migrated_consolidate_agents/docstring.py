"""
migrated_consolidate_agents



Módulo: migrated_consolidate_agents
Caminho: wiki\update\modules\maps\map_updater\migrated_consolidate_agents.py
Linhas de código: 474
Complexidade: 35.00

Funções (8):
- main(): Função principal...\n- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self, agents_dir): Inicializa o consolidador de agentes.

Args:
    a...\n- analyze_agents(self): Analisa todos os agentes existentes...\n- backup_agents(self): Faz backup de todos os agentes antes da consolidaç...\n- consolidate_group(self, group_name, group_config): Consolida um grupo de agentes...\n- consolidate_all_agents(self): Consolida todos os agentes...\n- generate_consolidation_report(self, results): Gera relatório de consolidação...\n
Classes (1):
- AgentConsolidator: Consolidador de agentes BMAD...\n  - __init__(self, agents_dir): Inicializa o consolidador de a...\n  - analyze_agents(self): Analisa todos os agentes exist...\n  - backup_agents(self): Faz backup de todos os agentes...\n  - consolidate_group(self, group_name, group_config): Consolida um grupo de agentes...\n  - consolidate_all_agents(self): Consolida todos os agentes...\n  - generate_consolidation_report(self, results): Gera relatório de consolidação...\n
Imports (5):
.MapupdaterModule, json, shutil, datetime.datetime, logging

Autor: Documentation Agent
Data: 2025-08-01 15:05:54
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

