"""
migrated_centralize_logs



Módulo: migrated_centralize_logs
Caminho: wiki\update\modules\tools\log_manager\migrated_centralize_logs.py
Linhas de código: 448
Complexidade: 40.00

Funções (11):
- main(): Função principal...\n- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self, log_dir): Inicializa o centralizador de logs.

Args:
    log...\n- create_centralized_structure(self): Cria estrutura centralizada de logs...\n- categorize_file(self, filename): Categoriza um arquivo de log...\n- matches_pattern(self, filename, pattern): Verifica se arquivo corresponde ao padrão...\n- backup_existing_files(self): Faz backup dos arquivos existentes...\n- move_file_to_category(self, file_path, category, subcategory): Move arquivo para categoria apropriada...\n- centralize_logs(self): Centraliza todos os logs...\n- create_centralized_index(self, results): Cria índice centralizado dos logs...\n- generate_centralization_report(self, results): Gera relatório de centralização...\n
Classes (1):
- LogCentralizer: Centralizador de logs BMAD...\n  - __init__(self, log_dir): Inicializa o centralizador de ...\n  - create_centralized_structure(self): Cria estrutura centralizada de...\n  - categorize_file(self, filename): Categoriza um arquivo de log...\n  - matches_pattern(self, filename, pattern): Verifica se arquivo correspond...\n  - backup_existing_files(self): Faz backup dos arquivos existe...\n  - move_file_to_category(self, file_path, category, subcategory): Move arquivo para categoria ap...\n  - centralize_logs(self): Centraliza todos os logs...\n  - create_centralized_index(self, results): Cria índice centralizado dos l...\n  - generate_centralization_report(self, results): Gera relatório de centralizaçã...\n
Imports (6):
.LogmanagerModule, json, shutil, datetime.datetime, logging, fnmatch

Autor: Documentation Agent
Data: 2025-08-01 15:05:53
"""
