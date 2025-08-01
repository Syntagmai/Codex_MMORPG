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
