"""
final_commit_verification

Sistema de Verificação Final de Commits
=======================================

Sistema que garante que todos os commits sejam feitos corretamente,
incluindo o relatório final, e sempre faz pull para evitar perda de dados.

Autor: Sistema BMAD - OTClient Documentation
Data: 2025-01-28
Versão: 1.0

Módulo: final_commit_verification
Caminho: wiki\update\final_commit_verification.py
Linhas de código: 473
Complexidade: 37.00

Funções (10):
- main(): Função principal....\n- __init__(self, base_path): ...\n- pull_latest_changes(self): Faz pull das últimas mudanças para evitar perda de...\n- check_git_status(self): Verifica status do Git.

Returns:
    Dicionário c...\n- add_all_changes(self): Adiciona todas as mudanças ao staging.

Returns:
 ...\n- commit_changes(self, message): Faz commit das mudanças.

Args:
    message: Mensa...\n- push_changes(self): Faz push das mudanças.

Returns:
    True se push ...\n- verify_clean_working_tree(self): Verifica se o working tree está limpo.

Returns:
 ...\n- generate_final_report(self): Gera relatório final da verificação.

Returns:
   ...\n- run_final_verification(self): Executa verificação final completa.

Returns:
    ...\n
Classes (1):
- FinalCommitVerification: Sistema de verificação final de commits...\n  - __init__(self, base_path): ...\n  - pull_latest_changes(self): Faz pull das últimas mudanças ...\n  - check_git_status(self): Verifica status do Git.

Retur...\n  - add_all_changes(self): Adiciona todas as mudanças ao ...\n  - commit_changes(self, message): Faz commit das mudanças.

Args...\n  - push_changes(self): Faz push das mudanças.

Return...\n  - verify_clean_working_tree(self): Verifica se o working tree est...\n  - generate_final_report(self): Gera relatório final da verifi...\n  - run_final_verification(self): Executa verificação final comp...\n
Imports (10):
os, sys, subprocess, logging, pathlib.Path, typing.Dict, typing.Any, typing.List, datetime.datetime, argparse

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

