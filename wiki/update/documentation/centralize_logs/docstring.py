"""
centralize_logs

Sistema de Logs Centralizado
============================

Este script centraliza e organiza logs espalhados em sistema centralizado
com categorização automática e estrutura hierárquica.

Autor: Sistema BMAD - Log Organizer
Data: 2025-08-01

Módulo: centralize_logs
Caminho: wiki\update\centralize_logs.py
Linhas de código: 417
Complexidade: 38.00

Funções (10):
- main(): Função principal...\n- __init__(self, log_dir): Inicializa o centralizador de logs.

Args:
    log...\n- create_centralized_structure(self): Cria estrutura centralizada de logs...\n- categorize_file(self, filename): Categoriza um arquivo de log...\n- matches_pattern(self, filename, pattern): Verifica se arquivo corresponde ao padrão...\n- backup_existing_files(self): Faz backup dos arquivos existentes...\n- move_file_to_category(self, file_path, category, subcategory): Move arquivo para categoria apropriada...\n- centralize_logs(self): Centraliza todos os logs...\n- create_centralized_index(self, results): Cria índice centralizado dos logs...\n- generate_centralization_report(self, results): Gera relatório de centralização...\n
Classes (1):
- LogCentralizer: Centralizador de logs BMAD...\n  - __init__(self, log_dir): Inicializa o centralizador de ...\n  - create_centralized_structure(self): Cria estrutura centralizada de...\n  - categorize_file(self, filename): Categoriza um arquivo de log...\n  - matches_pattern(self, filename, pattern): Verifica se arquivo correspond...\n  - backup_existing_files(self): Faz backup dos arquivos existe...\n  - move_file_to_category(self, file_path, category, subcategory): Move arquivo para categoria ap...\n  - centralize_logs(self): Centraliza todos os logs...\n  - create_centralized_index(self, results): Cria índice centralizado dos l...\n  - generate_centralization_report(self, results): Gera relatório de centralizaçã...\n
Imports (11):
json, os, shutil, pathlib.Path, typing.Dict, typing.List, typing.Any, typing.Optional, datetime.datetime, logging...

Autor: Documentation Agent
Data: 2025-08-01 15:05:50
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

