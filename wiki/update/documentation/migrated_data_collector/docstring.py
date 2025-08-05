"""
migrated_data_collector



Módulo: migrated_data_collector
Caminho: wiki\update\modules\tools\git_automation\migrated_data_collector.py
Linhas de código: 467
Complexidade: 28.00

Funções (15):
- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self, data_path): ...\n- init_database(self): Inicializa banco de dados SQLite...\n- generate_interaction_id(self, user_request, timestamp): Gera ID único para uma interação...\n- save_interaction(self, interaction_data): Salva uma nova interação no sistema...\n- _calculate_complexity(self, interaction_data): Calcula score de complexidade da interação...\n- _save_json_backup(self, record): Salva backup em formato JSON...\n- get_interaction(self, interaction_id): Recupera uma interação específica...\n- get_interactions(self, limit, offset, filters): Recupera múltiplas interações com filtros...\n- _row_to_dict(self, row, description): Converte linha do banco em dicionário...\n- get_total_interactions(self): Retorna total de interações no sistema...\n- get_interaction_stats(self): Retorna estatísticas das interações...\n- add_feedback(self, interaction_id, feedback_text, feedback_score): Adiciona feedback a uma interação...\n- cleanup_old_data(self, days_to_keep): Remove dados antigos do sistema...\n- _cleanup_old_json_files(self, days_to_keep): Remove arquivos JSON antigos...\n
Classes (2):
- InteractionRecord: Registro de uma interação no banco de dados...\n- DataCollector: Sistema de coleta e armazenamento de dados de inte...\n  - __init__(self, data_path): ...\n  - init_database(self): Inicializa banco de dados SQLi...\n  - generate_interaction_id(self, user_request, timestamp): Gera ID único para uma interaç...\n  - save_interaction(self, interaction_data): Salva uma nova interação no si...\n  - _calculate_complexity(self, interaction_data): Calcula score de complexidade ...\n  - _save_json_backup(self, record): Salva backup em formato JSON...\n  - get_interaction(self, interaction_id): Recupera uma interação específ...\n  - get_interactions(self, limit, offset, filters): Recupera múltiplas interações ...\n  - _row_to_dict(self, row, description): Converte linha do banco em dic...\n  - get_total_interactions(self): Retorna total de interações no...\n  - get_interaction_stats(self): Retorna estatísticas das inter...\n  - add_feedback(self, interaction_id, feedback_text, feedback_score): Adiciona feedback a uma intera...\n  - cleanup_old_data(self, days_to_keep): Remove dados antigos do sistem...\n  - _cleanup_old_json_files(self, days_to_keep): Remove arquivos JSON antigos...\n
Imports (7):
.GitautomationModule, json, sqlite3, hashlib, datetime.datetime, datetime.timedelta, threading

Autor: Documentation Agent
Data: 2025-08-01 15:05:52
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

