#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ast
import json
from pathlib import Path
from typing import Dict, List, Any, Optional, Set
from datetime import datetime

class DependencyMapper:
    
    def __init__(self):
        self.dependencies = {}
        self.circular_deps = []
    
    def map_dependencies(self, directory: str) -> Dict[str, Any]:
        try:
            dir_path = Path(directory)
            python_files = list(dir_path.rglob("*.py"))
            
            for file_path in python_files:
                self._analyze_file_dependencies(file_path)
            
            return {
                "dependencies": self.dependencies,
                "circular_dependencies": self.circular_deps,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {"error": str(e)}
    
    def _analyze_file_dependencies(self, file_path: Path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            tree = ast.parse(content)
            visitor = ImportVisitor()
            visitor.visit(tree)
            
            self.dependencies[str(file_path)] = visitor.imports
        except Exception as e:
            self.dependencies[str(file_path)] = {"error": str(e)}

class ImportVisitor(ast.NodeVisitor):
    
    def __init__(self):
        self.imports = []
    
    def visit_Import(self, node):
        for alias in node.names:
            self.imports.append(alias.name)
        self.generic_visit(node)
    
    def visit_ImportFrom(self, node):
        if node.module:
            self.imports.append(node.module)
        self.generic_visit(node)

def main():
    mapper = DependencyMapper()
    result = mapper.map_dependencies(".")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()

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
- **Nome**: dependency_mapper
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

