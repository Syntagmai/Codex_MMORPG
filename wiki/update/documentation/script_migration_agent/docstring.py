"""
script_migration_agent

🚀 Script Migration Agent - Epic 12 Task 12.3
=============================================

Script para migrar 172 scripts Python existentes para 50 módulos organizados.
Baseado na estrutura modular unificada criada na Task 12.2.

Responsável: Migration Agent
Duração: 5-7 dias
Dependência: Task 12.2 (Estrutura modular unificada)

Módulo: script_migration_agent
Caminho: wiki\update\script_migration_agent.py
Linhas de código: 451
Complexidade: 49.00

Funções (14):
- main(): Função principal do script....\n- __init__(self): ...\n- load_structure_config(self): Carrega configuração da estrutura modular....\n- load_script_mapping(self): Carrega mapeamento de scripts para módulos....\n- discover_python_scripts(self): Descobre todos os scripts Python no projeto....\n- analyze_script(self, script_path): Analisa um script Python para extrair informações....\n- determine_target_module(self, script_analysis): Determina o módulo de destino para um script....\n- migrate_script_to_module(self, script_path, target_module): Migra um script para o módulo de destino....\n- create_migrated_script(self, original_content, script_name, target_module): Cria versão migrada do script....\n- update_module_init(self, module_path, script_name, target_module): Atualiza __init__.py do módulo para incluir script...\n- update_module_config(self, module_path, script_name, target_module): Atualiza configuração do módulo....\n- migrate_all_scripts(self): Migra todos os scripts descobertos....\n- generate_migration_report(self): Gera relatório da migração....\n- save_migration_report(self, report): Salva relatório da migração....\n
Classes (1):
- ScriptMigrationAgent: Agente para migração de scripts Python para módulo...\n  - __init__(self): ...\n  - load_structure_config(self): Carrega configuração da estrut...\n  - load_script_mapping(self): Carrega mapeamento de scripts ...\n  - discover_python_scripts(self): Descobre todos os scripts Pyth...\n  - analyze_script(self, script_path): Analisa um script Python para ...\n  - determine_target_module(self, script_analysis): Determina o módulo de destino ...\n  - migrate_script_to_module(self, script_path, target_module): Migra um script para o módulo ...\n  - create_migrated_script(self, original_content, script_name, target_module): Cria versão migrada do script....\n  - update_module_init(self, module_path, script_name, target_module): Atualiza __init__.py do módulo...\n  - update_module_config(self, module_path, script_name, target_module): Atualiza configuração do módul...\n  - migrate_all_scripts(self): Migra todos os scripts descobe...\n  - generate_migration_report(self): Gera relatório da migração....\n  - save_migration_report(self, report): Salva relatório da migração....\n
Imports (13):
os, json, shutil, ast, re, pathlib.Path, typing.Dict, typing.List, typing.Any, typing.Optional...

Autor: Documentation Agent
Data: 2025-08-01 15:05:52
"""
