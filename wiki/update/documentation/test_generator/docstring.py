"""
test_generator



Módulo: test_generator
Caminho: wiki\update\python_tools\test_generator.py
Linhas de código: 60
Complexidade: 7.00

Funções (7):
- main(): ...\n- __init__(self): ...\n- generate_tests(self, source_file, test_type): ...\n- __init__(self): ...\n- visit_ClassDef(self, node): ...\n- visit_FunctionDef(self, node): ...\n- visit_AsyncFunctionDef(self, node): ...\n
Classes (2):
- TestGenerator: ...\n  - __init__(self): ...\n  - generate_tests(self, source_file, test_type): ...\n- TestVisitor: ...\n  - __init__(self): ...\n  - visit_ClassDef(self, node): ...\n  - visit_FunctionDef(self, node): ...\n  - visit_AsyncFunctionDef(self, node): ...\n
Imports (8):
ast, json, pathlib.Path, typing.Dict, typing.List, typing.Any, typing.Optional, datetime.datetime

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

