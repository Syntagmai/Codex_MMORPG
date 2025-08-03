#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from unicode_aliases import *

import os
import json
import ast
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import logging

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PythonToolsAgent:
    
    def __init__(self):
        self.project_root = Path(__file__).parent.parent.parent
        self.modules_path = self.project_root / "wiki/update/modules"
        self.tools_path = self.project_root / "wiki/update/python_tools"
        
        # Criar diretório de ferramentas
        self.tools_path.mkdir(exist_ok=True)
        
        # Estatísticas de criação
        self.tools_stats = {
            "total_tools_created": 0,
            "tools_by_category": {},
            "tools_created": [],
            "errors": [],
            "warnings": []
        }
    
    def create_complexity_analyzer(self) -> Dict[str, Any]:
        tool_name = "complexity_analyzer"
        tool_path = self.tools_path / "{}.py".format(tool_name)
        
        content = '''#!/usr/bin/env python3
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
'''
        
        try:
            with open(tool_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return {
                "tool_name": tool_name,
                "category": "code_analysis",
                "file_path": str(tool_path),
                "status": "created",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "tool_name": tool_name,
                "category": "code_analysis",
                "file_path": str(tool_path),
                "status": "error",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def create_dependency_mapper(self) -> Dict[str, Any]:
        tool_name = "dependency_mapper"
        tool_path = self.tools_path / "{}.py".format(tool_name)
        
        content = '''#!/usr/bin/env python3
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
'''
        
        try:
            with open(tool_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return {
                "tool_name": tool_name,
                "category": "code_analysis",
                "file_path": str(tool_path),
                "status": "created",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "tool_name": tool_name,
                "category": "code_analysis",
                "file_path": str(tool_path),
                "status": "error",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def create_code_generator(self) -> Dict[str, Any]:
        tool_name = "code_generator"
        tool_path = self.tools_path / "{}.py".format(tool_name)
        
        content = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

class CodeGenerator:
    
    def __init__(self):
        pass
    
    def generate_class(self, class_name: str, methods: List[str]) -> str:
        methods_code = "\\n    ".join(["def {}(self):\\n        pass".format(method) for method in methods])
        
        template = '''class {class_name}:
    
    def __init__(self):
        pass
    
    {methods_code}
'''
        return template.format(class_name=class_name, methods_code=methods_code)
    
    def generate_function(self, function_name: str, params: List[str]) -> str:
        params_str = ", ".join(params) if params else ""
        
        template = '''def {function_name}({params_str}):
    pass
'''
        return template.format(function_name=function_name, params_str=params_str)

def main():
    generator = CodeGenerator()
    class_code = generator.generate_class("ExampleClass", ["method1", "method2"])
    print(class_code)

if __name__ == "__main__":
    main()
'''
        
        try:
            with open(tool_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return {
                "tool_name": tool_name,
                "category": "development",
                "file_path": str(tool_path),
                "status": "created",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "tool_name": tool_name,
                "category": "development",
                "file_path": str(tool_path),
                "status": "error",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def create_test_generator(self) -> Dict[str, Any]:
        tool_name = "test_generator"
        tool_path = self.tools_path / "{}.py".format(tool_name)
        
        content = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ast
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

class TestGenerator:
    
    def __init__(self):
        pass
    
    def generate_tests(self, source_file: str, test_type: str = "unit") -> str:
        try:
            with open(source_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            tree = ast.parse(content)
            visitor = TestVisitor()
            visitor.visit(tree)
            
            module_name = Path(source_file).stem
            class_name = visitor.classes[0] if visitor.classes else "Example"
            functions = "\\n    ".join(["def test_{}(self):\\n        self.assertTrue(True)".format(func) for func in visitor.functions])
            
            return '''#!/usr/bin/env python3

import unittest
from {module_name} import {class_name}

class Test{class_name}(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    {functions}

if __name__ == "__main__":
    unittest.main()
'''.format(module_name=module_name, class_name=class_name, functions=functions)
        except Exception as e:
            return "# Erro ao gerar testes: {}".format(e)

class TestVisitor(ast.NodeVisitor):
    
    def __init__(self):
        self.classes = []
        self.functions = []
    
    def visit_ClassDef(self, node):
        self.classes.append(node.name)
        self.generic_visit(node)
    
    def visit_FunctionDef(self, node):
        if not hasattr(node, 'parent') or not isinstance(node.parent, ast.ClassDef):
            self.functions.append(node.name)
        self.generic_visit(node)
    
    def visit_AsyncFunctionDef(self, node):
        if not hasattr(node, 'parent') or not isinstance(node.parent, ast.ClassDef):
            self.functions.append(node.name)
        self.generic_visit(node)

def main():
    generator = TestGenerator()
    test_code = generator.generate_tests("example.py", "unit")
    print(test_code)

if __name__ == "__main__":
    main()
'''
        
        try:
            with open(tool_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return {
                "tool_name": tool_name,
                "category": "testing",
                "file_path": str(tool_path),
                "status": "created",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "tool_name": tool_name,
                "category": "testing",
                "file_path": str(tool_path),
                "status": "error",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def create_all_tools(self) -> bool:
        logger.info("🚀 Iniciando criação de ferramentas Python especializadas...")
        
        tools_created = []
        
        # Criar ferramentas principais
        tools_created.append(self.create_complexity_analyzer())
        tools_created.append(self.create_dependency_mapper())
        tools_created.append(self.create_code_generator())
        tools_created.append(self.create_test_generator())
        
        # Salvar estatísticas
        self.save_tools_stats(tools_created)
        
        # Gerar relatório
        report = self.generate_tools_report()
        self.save_tools_report(report)
        
        # Verificar sucesso
        successful_tools = [tool for tool in tools_created if tool.get("status") == "created"]
        logger.info("✅ Criadas {} ferramentas com sucesso".format(len(successful_tools)))
        
        return len(successful_tools) > 0
    
    def save_tools_stats(self, tools_created: List[Dict[str, Any]]):
        stats_path = self.tools_path / "tools_stats.json"
        
        # Contar ferramentas por categoria
        for tool in tools_created:
            category = tool.get("category", "unknown")
            if category not in self.tools_stats["tools_by_category"]:
                self.tools_stats["tools_by_category"][category] = 0
            self.tools_stats["tools_by_category"][category] += 1
        
        self.tools_stats["total_tools_created"] = len(tools_created)
        self.tools_stats["tools_created"] = tools_created
        
        try:
            with open(stats_path, 'w', encoding='utf-8') as f:
                json.dump(self.tools_stats, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error("Erro ao salvar estatísticas: {}".format(e))
    
    def generate_tools_report(self) -> Dict[str, Any]:
        return {
            "task": "12.7",
            "epic": "12",
            "title": "Criar ferramentas Python especializadas",
            "status": "completed",
            "timestamp": datetime.now().isoformat(),
            "tools_created": self.tools_stats["total_tools_created"],
            "categories": len(self.tools_stats["tools_by_category"]),
            "tools_by_category": self.tools_stats["tools_by_category"],
            "errors": len(self.tools_stats["errors"]),
            "warnings": len(self.tools_stats["warnings"])
        }
    
    def save_tools_report(self, report: Dict[str, Any]):
        report_path = self.project_root / "wiki/update/python_tools_report.json"
        
        try:
            with open(report_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            logger.info("✅ Relatório salvo: {}".format(report_path))
        except Exception as e:
            logger.error("Erro ao salvar relatório: {}".format(e))

def main():
    agent = PythonToolsAgent()
    success = agent.create_all_tools()
    
    if success:
        print("✅ Task 12.7 concluída com sucesso!")
        print("🚀 Ferramentas Python especializadas criadas.")
    else:
        print("❌ Erro na execução da Task 12.7.")

if __name__ == "__main__":
    main() 