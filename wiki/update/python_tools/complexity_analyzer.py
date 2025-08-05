#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ast
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

class ComplexityAnalyzer:
    
    def __init__(self):
        self.metrics = {
            'cyclomatic_complexity': 0,
            'nesting_depth': 0,
            'function_count': 0,
            'class_count': 0,
            'line_count': 0,
            'comment_count': 0
        }
    
    def analyze_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            tree = ast.parse(content)
            return self._analyze_ast(tree, file_path)
        except Exception as e:
            return {'error': str(e)}
    
    def _analyze_ast(self, tree, file_path):
        visitor = ComplexityVisitor()
        visitor.visit(tree)
        return {
            'file_path': file_path,
            'metrics': visitor.metrics,
            'timestamp': datetime.now().isoformat()
        }

class ComplexityVisitor(ast.NodeVisitor):
    def __init__(self):
        self.metrics = {
            'cyclomatic_complexity': 1,
            'nesting_depth': 0,
            'function_count': 0,
            'class_count': 0,
            'line_count': 0,
            'comment_count': 0
        }
        self.current_depth = 0
    
    def visit_FunctionDef(self, node):
        self.metrics['function_count'] += 1
        self.current_depth += 1
        self.metrics['nesting_depth'] = max(self.metrics['nesting_depth'], self.current_depth)
        self.generic_visit(node)
        self.current_depth -= 1
    
    def visit_ClassDef(self, node):
        self.metrics['class_count'] += 1
        self.current_depth += 1
        self.metrics['nesting_depth'] = max(self.metrics['nesting_depth'], self.current_depth)
        self.generic_visit(node)
        self.current_depth -= 1
    
    def visit_If(self, node):
        self.metrics['cyclomatic_complexity'] += 1
        self.generic_visit(node)
    
    def visit_While(self, node):
        self.metrics['cyclomatic_complexity'] += 1
        self.generic_visit(node)
    
    def visit_For(self, node):
        self.metrics['cyclomatic_complexity'] += 1
        self.generic_visit(node)
    
    def visit_ExceptHandler(self, node):
        self.metrics['cyclomatic_complexity'] += 1
        self.generic_visit(node)

def main():
    analyzer = ComplexityAnalyzer()
    test_file = 'test_file.py'
    if Path(test_file).exists():
        result = analyzer.analyze_file(test_file)
        print(json.dumps(result, indent=2))
    else:
        print('Arquivo {} não encontrado.'.format(test_file))

if __name__ == '__main__':
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
- **Nome**: complexity_analyzer
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

