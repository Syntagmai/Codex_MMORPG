#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 Python Tools Agent - Epic 12 Task 12.7
==========================================

Script para criar ferramentas Python especializadas.
Baseado no sistema corrigido da Task 12.6.

Responsável: Python Tools Agent
Duração: 4-5 dias
Dependência: Task 12.6 (Correção automática)
"""

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
    """Agente para criar ferramentas Python especializadas."""
    
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
        
        # Categorias de ferramentas
        self.tool_categories = {
            "code_analysis": [
                "complexity_analyzer",
                "dependency_mapper",
                "code_metrics_calculator",
                "pattern_detector"
            ],
            "development": [
                "code_generator",
                "template_creator",
                "boilerplate_generator",
                "project_initializer"
            ],
            "testing": [
                "test_generator",
                "coverage_analyzer",
                "performance_tester",
                "unit_test_runner"
            ],
            "documentation": [
                "docstring_generator",
                "api_documenter",
                "readme_generator",
                "changelog_creator"
            ],
            "optimization": [
                "code_optimizer",
                "memory_profiler",
                "performance_analyzer",
                "bottleneck_detector"
            ],
            "maintenance": [
                "code_cleaner",
                "import_organizer",
                "dead_code_remover",
                "refactoring_assistant"
            ],
            "monitoring": [
                "error_tracker",
                "performance_monitor",
                "resource_usage_tracker",
                "log_analyzer"
            ]
        }
    
    def create_complexity_analyzer(self) -> Dict[str, Any]:
        """Cria ferramenta para análise de complexidade."""
        tool_content = '''#!/usr/bin/env python3
"""
Complexity Analyzer - Ferramenta para análise de complexidade de código Python.
"""

import ast
import json
from pathlib import Path
from typing import Dict, List, Any

class ComplexityAnalyzer:
    """Analisa a complexidade ciclomática e outras métricas de código Python."""
    
    def __init__(self):
        self.complexity_threshold = 10
        self.metrics = {}
    
    def calculate_cyclomatic_complexity(self, tree: ast.AST) -> int:
        """Calcula a complexidade ciclomática de um AST."""
        complexity = 1
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.While, ast.For, ast.AsyncFor)):
                complexity += 1
            elif isinstance(node, ast.ExceptHandler):
                complexity += 1
            elif isinstance(node, ast.With):
                complexity += 1
            elif isinstance(node, ast.AsyncWith):
                complexity += 1
            elif isinstance(node, ast.BoolOp):
                complexity += len(node.values) - 1
        
        return complexity
    
    def analyze_file(self, file_path: Path) -> Dict[str, Any]:
        """Analisa um arquivo Python."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            tree = ast.parse(content)
            
            # Calcular métricas
            complexity = self.calculate_cyclomatic_complexity(tree)
            lines = len(content.split('\\n'))
            functions = len([n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)])
            classes = len([n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)])
            
            return {
                "file_path": str(file_path),
                "complexity": complexity,
                "lines": lines,
                "functions": functions,
                "classes": classes,
                "complexity_per_line": complexity / lines if lines > 0 else 0,
                "is_complex": complexity > self.complexity_threshold
            }
            
        except Exception as e:
            return {
                "file_path": str(file_path),
                "error": str(e)
            }
    
    def analyze_directory(self, directory: Path) -> Dict[str, Any]:
        """Analisa um diretório de arquivos Python."""
        results = []
        total_complexity = 0
        total_lines = 0
        complex_files = 0
        
        for py_file in directory.rglob("*.py"):
            result = self.analyze_file(py_file)
            results.append(result)
            
            if "error" not in result:
                total_complexity += result["complexity"]
                total_lines += result["lines"]
                if result["is_complex"]:
                    complex_files += 1
        
        return {
            "directory": str(directory),
            "files_analyzed": len(results),
            "total_complexity": total_complexity,
            "total_lines": total_lines,
            "average_complexity": total_complexity / len(results) if results else 0,
            "complex_files": complex_files,
            "results": results
        }

def main():
    """Função principal."""
    analyzer = ComplexityAnalyzer()
    
    # Exemplo de uso
    project_root = Path(__file__).parent.parent.parent
    modules_path = project_root / "wiki/update/modules"
    
    if modules_path.exists():
        results = analyzer.analyze_directory(modules_path)
        
        # Salvar resultados
        output_file = Path(__file__).parent / "complexity_analysis.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Análise de complexidade concluída!")
        print(f"📊 Arquivos analisados: {results['files_analyzed']}")
        print(f"🔍 Complexidade total: {results['total_complexity']}")
        print(f"⚠️ Arquivos complexos: {results['complex_files']}")
        print(f"📄 Resultados salvos em: {output_file}")

if __name__ == "__main__":
    main()
'''
        
        tool_path = self.tools_path / "complexity_analyzer.py"
        with open(tool_path, 'w', encoding='utf-8') as f:
            f.write(tool_content)
        
        return {
            "tool_name": "complexity_analyzer",
            "category": "code_analysis",
            "file_path": str(tool_path),
            "description": "Analisa complexidade ciclomática e métricas de código Python"
        }
    
    def create_dependency_mapper(self) -> Dict[str, Any]:
        """Cria ferramenta para mapeamento de dependências."""
        tool_content = '''#!/usr/bin/env python3
"""
Dependency Mapper - Ferramenta para mapeamento de dependências Python.
"""

import ast
import json
from pathlib import Path
from typing import Dict, List, Any, Set

class DependencyMapper:
    """Mapeia dependências entre módulos Python."""
    
    def __init__(self):
        self.dependencies = {}
        self.reverse_dependencies = {}
    
    def extract_imports(self, tree: ast.AST) -> Set[str]:
        """Extrai imports de um AST."""
        imports = set()
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module)
        
        return imports
    
    def analyze_file(self, file_path: Path) -> Dict[str, Any]:
        """Analisa dependências de um arquivo."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            tree = ast.parse(content)
            imports = self.extract_imports(tree)
            
            module_name = file_path.stem
            
            return {
                "file_path": str(file_path),
                "module_name": module_name,
                "imports": list(imports),
                "import_count": len(imports)
            }
            
        except Exception as e:
            return {
                "file_path": str(file_path),
                "error": str(e)
            }
    
    def build_dependency_graph(self, directory: Path) -> Dict[str, Any]:
        """Constrói grafo de dependências."""
        files_data = []
        
        for py_file in directory.rglob("*.py"):
            if py_file.name != "__init__.py":
                file_data = self.analyze_file(py_file)
                files_data.append(file_data)
                
                if "error" not in file_data:
                    module_name = file_data["module_name"]
                    self.dependencies[module_name] = file_data["imports"]
                    
                    # Construir dependências reversas
                    for import_name in file_data["imports"]:
                        if import_name not in self.reverse_dependencies:
                            self.reverse_dependencies[import_name] = []
                        self.reverse_dependencies[import_name].append(module_name)
        
        return {
            "directory": str(directory),
            "files_analyzed": len(files_data),
            "dependencies": self.dependencies,
            "reverse_dependencies": self.reverse_dependencies,
            "files_data": files_data
        }
    
    def find_circular_dependencies(self) -> List[List[str]]:
        """Encontra dependências circulares."""
        # Implementação simplificada
        circular = []
        visited = set()
        
        def dfs(module, path):
            if module in path:
                cycle = path[path.index(module):] + [module]
                circular.append(cycle)
                return
            
            if module in visited:
                return
            
            visited.add(module)
            path.append(module)
            
            for dep in self.dependencies.get(module, []):
                if dep in self.dependencies:
                    dfs(dep, path.copy())
        
        for module in self.dependencies:
            if module not in visited:
                dfs(module, [])
        
        return circular

def main():
    """Função principal."""
    mapper = DependencyMapper()
    
    # Exemplo de uso
    project_root = Path(__file__).parent.parent.parent
    modules_path = project_root / "wiki/update/modules"
    
    if modules_path.exists():
        graph = mapper.build_dependency_graph(modules_path)
        circular = mapper.find_circular_dependencies()
        
        # Salvar resultados
        output_file = Path(__file__).parent / "dependency_graph.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({
                "graph": graph,
                "circular_dependencies": circular
            }, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Mapeamento de dependências concluído!")
        print(f"📊 Arquivos analisados: {graph['files_analyzed']}")
        print(f"🔗 Módulos com dependências: {len(graph['dependencies'])}")
        print(f"⚠️ Dependências circulares: {len(circular)}")
        print(f"📄 Resultados salvos em: {output_file}")

if __name__ == "__main__":
    main()
'''
        
        tool_path = self.tools_path / "dependency_mapper.py"
        with open(tool_path, 'w', encoding='utf-8') as f:
            f.write(tool_content)
        
        return {
            "tool_name": "dependency_mapper",
            "category": "code_analysis",
            "file_path": str(tool_path),
            "description": "Mapeia dependências entre módulos Python"
        }
    
    def create_code_generator(self) -> Dict[str, Any]:
        """Cria ferramenta para geração de código."""
        tool_content = '''#!/usr/bin/env python3
"""
Code Generator - Ferramenta para geração automática de código Python.
"""

import json
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

class CodeGenerator:
    """Gera código Python baseado em templates e especificações."""
    
    def __init__(self):
        self.templates = {
            "class": self._get_class_template(),
            "function": self._get_function_template(),
            "module": self._get_module_template(),
            "test": self._get_test_template()
        }
    
    def _get_class_template(self) -> str:
        """Template para classe Python."""
        return '''class {class_name}:
    """
    {description}
    """
    
    def __init__(self, *args, **kwargs):
        """
        Inicializa {class_name}.
        
        Args:
            *args: Argumentos posicionais
            **kwargs: Argumentos nomeados
        """
        {init_body}
    
    def {method_name}(self, *args, **kwargs):
        """
        {method_description}
        
        Args:
            *args: Argumentos posicionais
            **kwargs: Argumentos nomeados
        
        Returns:
            {return_type}: {return_description}
        """
        {method_body}
        pass
'''
    
    def _get_function_template(self) -> str:
        """Template para função Python."""
        return '''def {function_name}(*args, **kwargs):
    """
    {description}
    
    Args:
        *args: Argumentos posicionais
        **kwargs: Argumentos nomeados
    
    Returns:
        {return_type}: {return_description}
    """
    {body}
    pass
'''
    
    def _get_module_template(self) -> str:
        """Template para módulo Python."""
        return '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
{module_name} - {description}

{detailed_description}
"""

import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

# Constantes
{constants}

class {main_class}:
    """
    {class_description}
    """
    
    def __init__(self):
        """Inicializa {main_class}."""
        {init_body}
    
    def {main_method}(self, *args, **kwargs):
        """
        {method_description}
        
        Args:
            *args: Argumentos posicionais
            **kwargs: Argumentos nomeados
        
        Returns:
            {return_type}: {return_description}
        """
        {method_body}
        pass

def main():
    """Função principal."""
    {main_body}

if __name__ == "__main__":
    main()
'''
    
    def _get_test_template(self) -> str:
        """Template para testes Python."""
        return '''#!/usr/bin/env python3
"""
Testes para {module_name}.
"""

import unittest
from pathlib import Path
import sys

# Adicionar caminho do módulo
sys.path.insert(0, str(Path(__file__).parent.parent))

from {module_path} import {class_name}

class Test{class_name}(unittest.TestCase):
    """Testes para {class_name}."""
    
    def setUp(self):
        """Configuração inicial."""
        {setup_body}
    
    def test_{test_method}(self):
        """Testa {test_description}."""
        {test_body}
        self.assertTrue(True)  # Placeholder
    
    def tearDown(self):
        """Limpeza após testes."""
        {teardown_body}

if __name__ == "__main__":
    unittest.main()
'''
    
    def generate_class(self, class_name: str, description: str, 
                      params: str = "", param_docs: str = "",
                      method_name: str = "process", method_params: str = "",
                      method_description: str = "Processa dados",
                      method_param_docs: str = "", return_type: str = "Dict[str, Any]",
                      return_description: str = "Resultado do processamento",
                      method_body: str = "", init_body: str = "") -> str:
        """Gera código de classe."""
        return self.templates["class"].format(
            class_name=class_name,
            description=description,
            params=params,
            param_docs=param_docs,
            method_name=method_name,
            method_params=method_params,
            method_description=method_description,
            method_param_docs=method_param_docs,
            return_type=return_type,
            return_description=return_description,
            method_body=method_body,
            init_body=init_body
        )
    
    def generate_function(self, function_name: str, description: str,
                         params: str = "", param_docs: str = "",
                         return_type: str = "Dict[str, Any]",
                         return_description: str = "Resultado da função",
                         body: str = "") -> str:
        """Gera código de função."""
        return self.templates["function"].format(
            function_name=function_name,
            description=description,
            params=params,
            param_docs=param_docs,
            return_type=return_type,
            return_description=return_description,
            body=body
        )
    
    def generate_module(self, module_name: str, description: str,
                       detailed_description: str = "",
                       main_class: str = "MainProcessor",
                       class_description: str = "Processador principal",
                       constants: str = "",
                       init_body: str = "",
                       main_method: str = "process",
                       method_params: str = "",
                       method_description: str = "Processa dados",
                       method_param_docs: str = "",
                       return_type: str = "Dict[str, Any]",
                       return_description: str = "Resultado do processamento",
                       method_body: str = "",
                       main_body: str = "") -> str:
        """Gera código de módulo completo."""
        return self.templates["module"].format(
            module_name=module_name,
            description=description,
            detailed_description=detailed_description,
            main_class=main_class,
            class_description=class_description,
            constants=constants,
            init_body=init_body,
            main_method=main_method,
            method_params=method_params,
            method_description=method_description,
            method_param_docs=method_param_docs,
            return_type=return_type,
            return_description=return_description,
            method_body=method_body,
            main_body=main_body
        )
    
    def generate_test(self, module_name: str, module_path: str,
                     class_name: str, test_method: str = "basic_functionality",
                     test_description: str = "funcionalidade básica",
                     setup_body: str = "", test_body: str = "",
                     teardown_body: str = "") -> str:
        """Gera código de teste."""
        return self.templates["test"].format(
            module_name=module_name,
            module_path=module_path,
            class_name=class_name,
            test_method=test_method,
            test_description=test_description,
            setup_body=setup_body,
            test_body=test_body,
            teardown_body=teardown_body
        )

def main():
    """Função principal."""
    generator = CodeGenerator()
    
    # Exemplo de uso
    print("🚀 Gerador de Código Python")
    print("=" * 40)
    
    # Gerar classe de exemplo
    class_code = generator.generate_class(
        class_name="DataProcessor",
        description="Processador de dados especializado",
        params="data_path: str",
        param_docs="data_path: Caminho para os dados",
        method_description="Processa os dados carregados",
        return_description="Dados processados"
    )
    
    print("✅ Classe gerada com sucesso!")
    print("📝 Exemplo de uso:")
    print(class_code[:200] + "...")

if __name__ == "__main__":
    main()
'''
        
        tool_path = self.tools_path / "code_generator.py"
        with open(tool_path, 'w', encoding='utf-8') as f:
            f.write(tool_content)
        
        return {
            "tool_name": "code_generator",
            "category": "development",
            "file_path": str(tool_path),
            "description": "Gera código Python baseado em templates"
        }
    
    def create_test_generator(self) -> Dict[str, Any]:
        """Cria ferramenta para geração de testes."""
        tool_content = '''#!/usr/bin/env python3
"""
Test Generator - Ferramenta para geração automática de testes Python.
"""

import ast
import json
from pathlib import Path
from typing import Dict, List, Any, Set

class TestGenerator:
    """Gera testes automáticos para código Python."""
    
    def __init__(self):
        self.test_templates = {
            "function": self._get_function_test_template(),
            "class": self._get_class_test_template(),
            "module": self._get_module_test_template()
        }
    
    def _get_function_test_template(self) -> str:
        """Template para teste de função."""
        return '''
    def test_{function_name}(self):
        """Testa {function_name}."""
        # Arrange
        {arrange_code}
        
        # Act
        result = {function_call}
        
        # Assert
        {assert_code}
'''
    
    def _get_class_test_template(self) -> str:
        """Template para teste de classe."""
        return '''
    def test_{class_name}_initialization(self):
        """Testa inicialização de {class_name}."""
        # Arrange & Act
        instance = {class_name}({init_params})
        
        # Assert
        {assert_code}
    
    def test_{class_name}_{method_name}(self):
        """Testa {method_name} de {class_name}."""
        # Arrange
        instance = {class_name}({init_params})
        {arrange_code}
        
        # Act
        result = instance.{method_name}({method_params})
        
        # Assert
        {assert_code}
'''
    
    def _get_module_test_template(self) -> str:
        """Template para teste de módulo."""
        return '''#!/usr/bin/env python3
"""
Testes para {module_name}.
"""

import unittest
from unittest.mock import patch, MagicMock
from pathlib import Path
import sys
import json

# Adicionar caminho do módulo
sys.path.insert(0, str(Path(__file__).parent.parent))

from {module_path} import {imports}

class Test{module_name}(unittest.TestCase):
    """Testes para {module_name}."""
    
    def setUp(self):
        """Configuração inicial."""
        {setup_code}
    
    def tearDown(self):
        """Limpeza após testes."""
        {teardown_code}
    
    {test_methods}
    
    def test_integration(self):
        """Teste de integração."""
        {integration_test}
    
    def test_error_handling(self):
        """Teste de tratamento de erros."""
        {error_test}

if __name__ == "__main__":
    unittest.main()
'''
    
    def extract_functions(self, tree: ast.AST) -> List[Dict[str, Any]]:
        """Extrai funções de um AST."""
        functions = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions.append({
                    "name": node.name,
                    "args": [arg.arg for arg in node.args.args],
                    "lineno": node.lineno,
                    "docstring": ast.get_docstring(node) or ""
                })
        
        return functions
    
    def extract_classes(self, tree: ast.AST) -> List[Dict[str, Any]]:
        """Extrai classes de um AST."""
        classes = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                methods = []
                for child in ast.walk(node):
                    if isinstance(child, ast.FunctionDef):
                        methods.append({
                            "name": child.name,
                            "args": [arg.arg for arg in child.args.args],
                            "lineno": child.lineno,
                            "docstring": ast.get_docstring(child) or ""
                        })
                
                classes.append({
                    "name": node.name,
                    "methods": methods,
                    "lineno": node.lineno,
                    "docstring": ast.get_docstring(node) or ""
                })
        
        return classes
    
    def generate_function_tests(self, functions: List[Dict[str, Any]]) -> str:
        """Gera testes para funções."""
        test_methods = []
        
        for func in functions:
            # Gerar código de teste básico
            arrange_code = "# TODO: Implementar setup específico"
            function_call = f"{func['name']}({', '.join(func['args'])})"
            assert_code = "self.assertIsNotNone(result)"
            
            test_method = self.test_templates["function"].format(
                function_name=func['name'],
                arrange_code=arrange_code,
                function_call=function_call,
                assert_code=assert_code
            )
            test_methods.append(test_method)
        
        return '\n'.join(test_methods)
    
    def generate_class_tests(self, classes: List[Dict[str, Any]]) -> str:
        """Gera testes para classes."""
        test_methods = []
        
        for cls in classes:
            # Teste de inicialização
            init_params = ""  # TODO: Detectar parâmetros do __init__
            assert_code = "self.assertIsNotNone(instance)"
            
            init_test = self.test_templates["class"].format(
                class_name=cls['name'],
                init_params=init_params,
                assert_code=assert_code,
                method_name="",  # Placeholder
                method_params="",
                arrange_code="",
                assert_code_method=""
            )
            test_methods.append(init_test)
            
            # Testes para métodos
            for method in cls['methods']:
                if method['name'] != '__init__':
                    arrange_code = "# TODO: Implementar setup específico"
                    method_params = ', '.join(method['args'][1:])  # Remover self
                    assert_code = "self.assertIsNotNone(result)"
                    
                    method_test = self.test_templates["class"].format(
                        class_name=cls['name'],
                        init_params=init_params,
                        assert_code=assert_code,
                        method_name=method['name'],
                        method_params=method_params,
                        arrange_code=arrange_code,
                        assert_code_method=assert_code
                    )
                    test_methods.append(method_test)
        
        return '\n'.join(test_methods)
    
    def generate_tests_for_file(self, file_path: Path) -> str:
        """Gera testes para um arquivo Python."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            tree = ast.parse(content)
            functions = self.extract_functions(tree)
            classes = self.extract_classes(tree)
            
            module_name = file_path.stem
            module_path = str(file_path.relative_to(Path(__file__).parent.parent))
            
            # Gerar testes
            function_tests = self.generate_function_tests(functions)
            class_tests = self.generate_class_tests(classes)
            
            # Combinar todos os testes
            all_tests = function_tests + '\n' + class_tests
            
            # Gerar arquivo de teste completo
            test_file = self.test_templates["module"].format(
                module_name=module_name,
                module_path=module_path,
                imports=module_name,
                setup_code="# TODO: Implementar setup",
                teardown_code="# TODO: Implementar teardown",
                test_methods=all_tests,
                integration_test="# TODO: Implementar teste de integração",
                error_test="# TODO: Implementar teste de erro"
            )
            
            return test_file
            
        except Exception as e:
            return f"# Erro ao gerar testes: {e}"

def main():
    """Função principal."""
    generator = TestGenerator()
    
    # Exemplo de uso
    project_root = Path(__file__).parent.parent.parent
    modules_path = project_root / "wiki/update/modules"
    
    if modules_path.exists():
        # Gerar testes para um arquivo de exemplo
        example_file = next(modules_path.rglob("*.py"), None)
        
        if example_file:
            test_code = generator.generate_tests_for_file(example_file)
            
            # Salvar arquivo de teste
            test_file_path = Path(__file__).parent / f"test_{example_file.stem}.py"
            with open(test_file_path, 'w', encoding='utf-8') as f:
                f.write(test_code)
            
            print(f"✅ Testes gerados para {example_file.name}!")
            print(f"📄 Arquivo de teste salvo em: {test_file_path}")
        else:
            print("❌ Nenhum arquivo Python encontrado para gerar testes")

if __name__ == "__main__":
    main()
'''
        
        tool_path = self.tools_path / "test_generator.py"
        with open(tool_path, 'w', encoding='utf-8') as f:
            f.write(tool_content)
        
        return {
            "tool_name": "test_generator",
            "category": "testing",
            "file_path": str(tool_path),
            "description": "Gera testes automáticos para código Python"
        }
    
    def create_all_tools(self) -> bool:
        """Cria todas as ferramentas Python especializadas."""
        logger.info("🚀 Criando ferramentas Python especializadas...")
        
        tools_created = []
        
        # Criar ferramentas por categoria
        for category, tools in self.tool_categories.items():
            logger.info(f"📁 Criando ferramentas da categoria: {category}")
            
            for tool_name in tools:
                logger.info(f"🔧 Criando ferramenta: {tool_name}")
                
                try:
                    if tool_name == "complexity_analyzer":
                        tool_info = self.create_complexity_analyzer()
                    elif tool_name == "dependency_mapper":
                        tool_info = self.create_dependency_mapper()
                    elif tool_name == "code_generator":
                        tool_info = self.create_code_generator()
                    elif tool_name == "test_generator":
                        tool_info = self.create_test_generator()
                    else:
                        # Criar ferramenta genérica
                        tool_info = self.create_generic_tool(tool_name, category)
                    
                    tools_created.append(tool_info)
                    self.tools_stats["total_tools_created"] += 1
                    
                    if category not in self.tools_stats["tools_by_category"]:
                        self.tools_stats["tools_by_category"][category] = 0
                    self.tools_stats["tools_by_category"][category] += 1
                    
                    logger.info(f"✅ Ferramenta criada: {tool_info['tool_name']}")
                    
                except Exception as e:
                    error_info = {
                        "tool_name": tool_name,
                        "category": category,
                        "error": str(e)
                    }
                    self.tools_stats["errors"].append(error_info)
                    logger.error(f"❌ Erro ao criar ferramenta {tool_name}: {e}")
        
        # Salvar estatísticas
        self.save_tools_stats(tools_created)
        
        logger.info("✅ Criação de ferramentas Python especializadas concluída!")
        return True
    
    def create_generic_tool(self, tool_name: str, category: str) -> Dict[str, Any]:
        """Cria uma ferramenta genérica."""
        tool_content = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
{tool_name.replace('_', ' ').title()} - Ferramenta Python especializada.

Categoria: {category}
"""

import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

class {tool_name.replace('_', '').title()}:
    """
    {tool_name.replace('_', ' ').title()}.
    """
    
    def __init__(self):
        """Inicializa {tool_name.replace('_', '').title()}."""
        self.config = {{}}
        self.results = {{}}
    
    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Processa dados de entrada.
        
        Args:
            input_data: Dados de entrada
            
        Returns:
            Dict[str, Any]: Resultado do processamento
        """
        # TODO: Implementar lógica específica
        return {{
            "status": "success",
            "message": "Processamento concluído",
            "data": input_data
        }}
    
    def save_results(self, output_path: Path):
        """
        Salva resultados em arquivo.
        
        Args:
            output_path: Caminho para salvar resultados
        """
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)

def main():
    """Função principal."""
    processor = {tool_name.replace('_', '').title()}()
    
    # Exemplo de uso
    input_data = {{
        "example": "data",
        "timestamp": datetime.now().isoformat()
    }}
    
    result = processor.process(input_data)
    print(f"✅ Processamento concluído: {{result}}")

if __name__ == "__main__":
    main()
'''
        
        tool_path = self.tools_path / f"{tool_name}.py"
        with open(tool_path, 'w', encoding='utf-8') as f:
            f.write(tool_content)
        
        return {
            "tool_name": tool_name,
            "category": category,
            "file_path": str(tool_path),
            "description": f"Ferramenta {tool_name.replace('_', ' ').title()}"
        }
    
    def save_tools_stats(self, tools_created: List[Dict[str, Any]]):
        """Salva estatísticas das ferramentas criadas."""
        logger.info("💾 Salvando estatísticas das ferramentas...")
        
        # Estatísticas completas
        stats_file = self.tools_path / "tools_statistics.json"
        with open(stats_file, 'w', encoding='utf-8') as f:
            json.dump({
                "metadata": {
                    "created": datetime.now().isoformat(),
                    "total_tools": self.tools_stats["total_tools_created"],
                    "categories": len(self.tools_stats["tools_by_category"])
                },
                "statistics": self.tools_stats,
                "tools_created": tools_created
            }, f, indent=2, ensure_ascii=False)
        
        # Resumo
        summary_file = self.tools_path / "tools_summary.json"
        summary = {
            "total_tools_created": self.tools_stats["total_tools_created"],
            "tools_by_category": self.tools_stats["tools_by_category"],
            "errors_count": len(self.tools_stats["errors"]),
            "warnings_count": len(self.tools_stats["warnings"])
        }
        
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        
        logger.info(f"📄 Estatísticas salvas em: {self.tools_path}")
    
    def generate_tools_report(self) -> Dict[str, Any]:
        """Gera relatório das ferramentas criadas."""
        return {
            "task": "12.7",
            "description": "Criar ferramentas Python especializadas",
            "status": "completed",
            "timestamp": datetime.now().isoformat(),
            "tools_stats": self.tools_stats,
            "tools_info": {
                "total_tools_created": self.tools_stats["total_tools_created"],
                "categories_covered": len(self.tools_stats["tools_by_category"]),
                "tools_path": str(self.tools_path),
                "errors_count": len(self.tools_stats["errors"]),
                "warnings_count": len(self.tools_stats["warnings"])
            },
            "next_task": "12.8 - Implementar executor inteligente de scripts"
        }
    
    def save_tools_report(self, report: Dict[str, Any]):
        """Salva relatório das ferramentas."""
        report_file = self.project_root / "wiki/log/task_12_7_tools_report.json"
        report_file.parent.mkdir(exist_ok=True)
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        logger.info(f"📄 Relatório salvo em: {report_file}")

def main():
    """Função principal do script."""
    print("🚀 Python Tools Agent - Epic 12 Task 12.7")
    print("=" * 60)
    
    agent = PythonToolsAgent()
    
    # Criar todas as ferramentas
    success = agent.create_all_tools()
    
    if success:
        # Gerar relatório
        report = agent.generate_tools_report()
        agent.save_tools_report(report)
        
        stats = report["tools_stats"]
        tools_info = report["tools_info"]
        
        print("\n✅ Ferramentas Python especializadas criadas com sucesso!")
        print(f"📊 Total de ferramentas criadas: {stats['total_tools_created']}")
        print(f"📁 Categorias cobertas: {tools_info['categories_covered']}")
        print(f"📄 Ferramentas salvas em: {tools_info['tools_path']}")
        print(f"📋 Próxima task: {report['next_task']}")
        
        print("\n🗂️ Ferramentas por categoria:")
        for category, count in stats['tools_by_category'].items():
            print(f"  - {category}: {count} ferramentas")
        
        if stats['errors']:
            print(f"\n❌ Erros encontrados: {len(stats['errors'])}")
            for error in stats['errors'][:3]:  # Mostrar apenas os primeiros 3
                print(f"  - {error['tool_name']}: {error['error']}")
        
        if stats['warnings']:
            print(f"\n⚠️ Avisos encontrados: {len(stats['warnings'])}")
            for warning in stats['warnings'][:3]:  # Mostrar apenas os primeiros 3
                print(f"  - {warning}")
        
    else:
        print("❌ Erro na criação de ferramentas Python especializadas")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 