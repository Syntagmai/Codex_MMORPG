"""
auto_update_all_maps

Script principal para atualização automática de todos os mapas JSON
Executa todos os scripts de indexação na ordem estabelecida
Usa contexto detectado automaticamente

Módulo: auto_update_all_maps
Caminho: wiki\update\auto_update_all_maps.py
Linhas de código: 276
Complexidade: 23.00

Funções (11):
- __init__(self): ...\n- load_context_data(self): Carrega dados de contexto detectado...\n- get_context_scripts(self): Retorna scripts baseados no contexto...\n- get_context_maps(self): Retorna mapas baseados no contexto...\n- log(self, message, level): Log com timestamp...\n- execute_script(self, script_path): Executa um script específico...\n- validate_map(self, map_path): Valida um mapa JSON...\n- update_all_maps(self): Executa atualização de todos os mapas...\n- generate_report(self): Gera relatório de atualização...\n- save_report(self, report_path): Salva relatório de atualização...\n- print_summary(self): Imprime resumo da atualização...\n
Classes (1):
- AutoMapUpdater: ...\n  - __init__(self): ...\n  - load_context_data(self): Carrega dados de contexto dete...\n  - get_context_scripts(self): Retorna scripts baseados no co...\n  - get_context_maps(self): Retorna mapas baseados no cont...\n  - log(self, message, level): Log com timestamp...\n  - execute_script(self, script_path): Executa um script específico...\n  - validate_map(self, map_path): Valida um mapa JSON...\n  - update_all_maps(self): Executa atualização de todos o...\n  - generate_report(self): Gera relatório de atualização...\n  - save_report(self, report_path): Salva relatório de atualização...\n  - print_summary(self): Imprime resumo da atualização...\n
Imports (10):
os, sys, json, subprocess, time, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

Autor: Documentation Agent
Data: 2025-08-01 15:05:50
"""
