"""
git_atomic_commits

Script para fazer commits atômicos organizados por categoria
Seguindo as regras de automação Git do sistema BMAD

Módulo: git_atomic_commits
Caminho: wiki\update\git_atomic_commits.py
Linhas de código: 135
Complexidade: 21.00

Funções (5):
- run_command(command, capture_output): Executa comando e retorna resultado...\n- get_untracked_files(): Obtém lista de arquivos não rastreados...\n- categorize_files(files): Categoriza arquivos por tipo...\n- make_commit(files, category, description): Faz commit de uma categoria de arquivos...\n- main(): Função principal...\n
Classes (0):

Imports (4):
subprocess, os, sys, pathlib.Path

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

