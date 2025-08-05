"""
migrated_workflow_orchestrator_legacy



Módulo: migrated_workflow_orchestrator_legacy
Caminho: wiki\update\modules\agents\agent_orchestrator\migrated_workflow_orchestrator_legacy.py
Linhas de código: 461
Complexidade: 34.00

Funções (14):
- main(): Função principal para teste do orquestrador...\n- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self, workspace_path): ...\n- execute_workflow(self, module_name, config): Executa o workflow completo para um módulo

Args:
...\n- execute_analysis_phase(self, module_name): Executa fase de análise...\n- execute_generation_phase(self, analysis_results): Executa fase de geração...\n- execute_testing_phase(self, generation_results, analysis_results): Executa fase de teste...\n- execute_learning_phase(self, analysis_results, generation_results, test_results): Executa fase de aprendizado...\n- generate_workflow_summary(self, workflow_results): Gera resumo do workflow...\n- save_workflow_results(self, workflow_results): Salva resultados do workflow...\n- log_phase(self, phase_name, module_name, status, duration, error): Registra log de uma fase do workflow...\n- get_available_modules(self): Retorna lista de módulos disponíveis...\n- get_workflow_status(self, workflow_id): Obtém status de um workflow específico...\n- list_workflows(self): Lista todos os workflows executados...\n
Classes (1):
- WorkflowOrchestrator: Orquestrador principal do workflow de módulos OTCl...\n  - __init__(self, workspace_path): ...\n  - execute_workflow(self, module_name, config): Executa o workflow completo pa...\n  - execute_analysis_phase(self, module_name): Executa fase de análise...\n  - execute_generation_phase(self, analysis_results): Executa fase de geração...\n  - execute_testing_phase(self, generation_results, analysis_results): Executa fase de teste...\n  - execute_learning_phase(self, analysis_results, generation_results, test_results): Executa fase de aprendizado...\n  - generate_workflow_summary(self, workflow_results): Gera resumo do workflow...\n  - save_workflow_results(self, workflow_results): Salva resultados do workflow...\n  - log_phase(self, phase_name, module_name, status, duration, error): Registra log de uma fase do wo...\n  - get_available_modules(self): Retorna lista de módulos dispo...\n  - get_workflow_status(self, workflow_id): Obtém status de um workflow es...\n  - list_workflows(self): Lista todos os workflows execu...\n
Imports (6):
.AgentorchestratorModule, os, sys, json, time, datetime.datetime

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

