"""
migrated_navigation_validation_agent



Módulo: migrated_navigation_validation_agent
Caminho: wiki\update\modules\agents\agent_orchestrator\migrated_navigation_validation_agent.py
Linhas de código: 461
Complexidade: 38.00

Funções (10):
- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self): ...\n- log_message(self, message, level): ...\n- validate_file_references(self): Valida referências a arquivos em documentos e scri...\n- validate_import_statements(self): Valida statements de import em arquivos Python...\n- validate_json_references(self): Valida referências em arquivos JSON...\n- update_json_references(self, data, old_name, new_name): Atualiza referências em estrutura JSON...\n- validate_execution_paths(self): Valida caminhos de execução em scripts...\n- generate_navigation_report(self): Gera relatório completo de validação de navegação...\n- execute(self): Executa a validação completa de navegação...\n
Classes (1):
- NavigationValidationAgent: ...\n  - __init__(self): ...\n  - log_message(self, message, level): ...\n  - validate_file_references(self): Valida referências a arquivos ...\n  - validate_import_statements(self): Valida statements de import em...\n  - validate_json_references(self): Valida referências em arquivos...\n  - update_json_references(self, data, old_name, new_name): Atualiza referências em estrut...\n  - validate_execution_paths(self): Valida caminhos de execução em...\n  - generate_navigation_report(self): Gera relatório completo de val...\n  - execute(self): Executa a validação completa d...\n
Imports (5):
.AgentorchestratorModule, json, re, datetime.datetime, subprocess

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

