"""
update_bmad_maps

Script para atualização automática dos mapas JSON do sistema BMAD
Atualiza: maps/bmad_agents_index.json, maps/bmad_workflows_index.json, maps/bmad_templates_index.json

Módulo: update_bmad_maps
Caminho: wiki\update\update_bmad_maps.py
Linhas de código: 392
Complexidade: 6.00

Funções (9):
- __init__(self, wiki_dir): ...\n- load_context_data(self): Carrega dados de contexto detectado...\n- generate_agents_index(self): Gera índice de agentes BMAD...\n- generate_workflows_index(self): Gera índice de workflows BMAD...\n- generate_templates_index(self): Gera índice de templates BMAD...\n- get_context_adaptation(self, agent_id): Retorna adaptação do agente para o contexto atual...\n- get_workflow_context_adaptation(self, workflow_id): Retorna adaptação do workflow para o contexto atua...\n- get_template_context_adaptation(self, template_id): Retorna adaptação do template para o contexto atua...\n- update_all_bmad_maps(self): Atualiza todos os mapas BMAD...\n
Classes (1):
- BMADMapUpdater: ...\n  - __init__(self, wiki_dir): ...\n  - load_context_data(self): Carrega dados de contexto dete...\n  - generate_agents_index(self): Gera índice de agentes BMAD...\n  - generate_workflows_index(self): Gera índice de workflows BMAD...\n  - generate_templates_index(self): Gera índice de templates BMAD...\n  - get_context_adaptation(self, agent_id): Retorna adaptação do agente pa...\n  - get_workflow_context_adaptation(self, workflow_id): Retorna adaptação do workflow ...\n  - get_template_context_adaptation(self, template_id): Retorna adaptação do template ...\n  - update_all_bmad_maps(self): Atualiza todos os mapas BMAD...\n
Imports (7):
os, json, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

Autor: Documentation Agent
Data: 2025-08-01 15:05:52
"""
