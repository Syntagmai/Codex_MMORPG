"""
script_execution_manager

Gerenciador de Execução de Scripts Python
Gerencia a execução de scripts Python com resolução automática de erros

Módulo: script_execution_manager
Caminho: wiki\update\script_execution_manager.py
Linhas de código: 341
Complexidade: 28.00

Funções (11):
- main(): Função principal...\n- __init__(self): ...\n- execute_script_with_error_resolution(self, script_path, args): Executa script Python com resolução automática de ...\n- resolve_script_error(self, script_path, error_message): Resolve erro em script usando o resolver automátic...\n- execute_script_safely(self, script_path, args): Executa script de forma segura com fallback...\n- execute_fallback_mode(self, script_path, args): Executa script em modo fallback (simplificado)...\n- create_basic_map_update(self, script_path): Cria atualização básica de mapas...\n- create_basic_analysis_report(self, script_path): Cria relatório básico de análise...\n- create_basic_report(self, script_path): Cria relatório básico genérico...\n- log_execution(self, execution_result): Registra resultado da execução...\n- get_execution_stats(self): Obtém estatísticas de execução...\n
Classes (1):
- ScriptExecutionManager: ...\n  - __init__(self): ...\n  - execute_script_with_error_resolution(self, script_path, args): Executa script Python com reso...\n  - resolve_script_error(self, script_path, error_message): Resolve erro em script usando ...\n  - execute_script_safely(self, script_path, args): Executa script de forma segura...\n  - execute_fallback_mode(self, script_path, args): Executa script em modo fallbac...\n  - create_basic_map_update(self, script_path): Cria atualização básica de map...\n  - create_basic_analysis_report(self, script_path): Cria relatório básico de análi...\n  - create_basic_report(self, script_path): Cria relatório básico genérico...\n  - log_execution(self, execution_result): Registra resultado da execução...\n  - get_execution_stats(self): Obtém estatísticas de execução...\n
Imports (10):
json, subprocess, sys, time, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any, typing.Optional

Autor: Documentation Agent
Data: 2025-08-01 15:05:52
"""
