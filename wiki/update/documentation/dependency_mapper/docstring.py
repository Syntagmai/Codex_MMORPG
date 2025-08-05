"""
dependency_mapper



Módulo: dependency_mapper
Caminho: wiki\update\python_tools\dependency_mapper.py
Linhas de código: 67
Complexidade: 7.00

Funções (7):
- main(): ...\n- __init__(self): ...\n- map_dependencies(self, directory): ...\n- _analyze_file_dependencies(self, file_path): ...\n- __init__(self): ...\n- visit_Import(self, node): ...\n- visit_ImportFrom(self, node): ...\n
Classes (2):
- DependencyMapper: ...\n  - __init__(self): ...\n  - map_dependencies(self, directory): ...\n  - _analyze_file_dependencies(self, file_path): ...\n- ImportVisitor: ...\n  - __init__(self): ...\n  - visit_Import(self, node): ...\n  - visit_ImportFrom(self, node): ...\n
Imports (9):
ast, json, pathlib.Path, typing.Dict, typing.List, typing.Any, typing.Optional, typing.Set, datetime.datetime

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

