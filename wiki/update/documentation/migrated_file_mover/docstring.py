"""
migrated_file_mover



Módulo: migrated_file_mover
Caminho: wiki\update\modules\tools\file_mover\migrated_file_mover.py
Linhas de código: 342
Complexidade: 41.00

Funções (10):
- load_config(config_file): Load configuration from JSON file....\n- save_config(config, config_file): Save configuration to JSON file....\n- interactive_mode(): Interactive mode for file moving....\n- main(): Main function with command line interface....\n- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self, dry_run, create_backup): ...\n- setup_backup_directory(self, source_dir): Create backup directory for safety....\n- validate_paths(self, source_dir, destination_dir, files): Validate all paths before moving files....\n- move_file(self, source_file, destination_file): Move a single file with error handling....\n- move_files(self, source_dir, destination_dir, files): Move multiple files efficiently....\n
Classes (1):
- FileMover: Efficient file mover with absolute directory suppo...\n  - __init__(self, dry_run, create_backup): ...\n  - setup_backup_directory(self, source_dir): Create backup directory for sa...\n  - validate_paths(self, source_dir, destination_dir, files): Validate all paths before movi...\n  - move_file(self, source_file, destination_file): Move a single file with error ...\n  - move_files(self, source_dir, destination_dir, files): Move multiple files efficientl...\n
Imports (8):
.FilemoverModule, os, sys, json, shutil, argparse, logging, datetime.datetime

Autor: Documentation Agent
Data: 2025-08-01 15:05:52
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

