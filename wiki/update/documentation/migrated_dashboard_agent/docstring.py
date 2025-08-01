"""
migrated_dashboard_agent



Módulo: migrated_dashboard_agent
Caminho: wiki\update\modules\agents\agent_orchestrator\migrated_dashboard_agent.py
Linhas de código: 610
Complexidade: 23.00

Funções (11):
- main(): Função principal...\n- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self): ...\n- load_configuration(self): Carrega configurações do sistema de dashboard...\n- load_metrics_data(self): Carrega dados de métricas...\n- generate_html_dashboard(self, data): Gera dashboard HTML interativo...\n- generate_markdown_dashboard(self, data): Gera dashboard em Markdown...\n- save_dashboard(self, html_content, markdown_content): Salva dashboards em arquivos...\n- run(self): Executa o agente de dashboard...\n- get_status_color(value, thresholds): ...\n- get_status_emoji(value, thresholds): ...\n
Classes (1):
- DashboardAgent: ...\n  - __init__(self): ...\n  - load_configuration(self): Carrega configurações do siste...\n  - load_metrics_data(self): Carrega dados de métricas...\n  - generate_html_dashboard(self, data): Gera dashboard HTML interativo...\n  - generate_markdown_dashboard(self, data): Gera dashboard em Markdown...\n  - save_dashboard(self, html_content, markdown_content): Salva dashboards em arquivos...\n  - run(self): Executa o agente de dashboard...\n  - get_status_color(value, thresholds): ...\n  - get_status_emoji(value, thresholds): ...\n
Imports (3):
.AgentorchestratorModule, json, logging

Autor: Documentation Agent
Data: 2025-08-01 15:05:58
"""
