"""
intelligent_orchestrator

Sistema de Orquestração Inteligente para Agentes BMAD
Detecta automaticamente o contexto e coordena agentes sem comandos manuais

Módulo: intelligent_orchestrator
Caminho: wiki\update\intelligent_orchestrator.py
Linhas de código: 517
Complexidade: 31.00

Funções (13):
- main(): Função principal para teste do sistema...\n- __init__(self): ...\n- analyze_context(self, user_request): Analisa o contexto do pedido do usuário...\n- analyze_complexity(self, text, keywords): Analisa a complexidade baseada no contexto...\n- identify_primary_workflow(self, keywords, workflows): Identifica o workflow principal baseado nas palavr...\n- select_agents(self, context): Seleciona agentes baseado no contexto...\n- get_agent_role(self, agent_id, workflow_type): Define o papel específico do agente no workflow...\n- execute_workflow(self, agent_workflow): Executa o workflow coordenado...\n- get_agents_for_phase(self, phase, agents): Identifica agentes responsáveis por cada fase...\n- report_phase_progress(self, phase, agents, progress): Reporta progresso da fase...\n- generate_progress_report(self, execution_results): Gera relatório de progresso em tempo real...\n- orchestrate_request(self, user_request): Orquestra automaticamente o pedido do usuário...\n- save_execution_results(self, execution_results): Salva resultados da execução...\n
Classes (1):
- IntelligentOrchestrator: Sistema de orquestração inteligente para agentes B...\n  - __init__(self): ...\n  - analyze_context(self, user_request): Analisa o contexto do pedido d...\n  - analyze_complexity(self, text, keywords): Analisa a complexidade baseada...\n  - identify_primary_workflow(self, keywords, workflows): Identifica o workflow principa...\n  - select_agents(self, context): Seleciona agentes baseado no c...\n  - get_agent_role(self, agent_id, workflow_type): Define o papel específico do a...\n  - execute_workflow(self, agent_workflow): Executa o workflow coordenado...\n  - get_agents_for_phase(self, phase, agents): Identifica agentes responsávei...\n  - report_phase_progress(self, phase, agents, progress): Reporta progresso da fase...\n  - generate_progress_report(self, execution_results): Gera relatório de progresso em...\n  - orchestrate_request(self, user_request): Orquestra automaticamente o pe...\n  - save_execution_results(self, execution_results): Salva resultados da execução...\n
Imports (8):
json, re, time, datetime.datetime, typing.Dict, typing.List, typing.Any, typing.Optional

Autor: Documentation Agent
Data: 2025-08-01 15:05:51
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

