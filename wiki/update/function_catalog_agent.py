from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import ast
import inspect
import json
import logging
import os

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 Function Catalog Agent - Epic 12 Task 12.4
=============================================

Script para criar catálogo automático de todas as funções Python.
Baseado nos módulos migrados da Task 12.3.

Responsável: Function Catalog Agent
Duração: 2-3 dias
Dependência: Task 12.3 (Migração de scripts)
"""


# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class FunctionCatalogAgent:
    """Agente para criação de catálogo automático de funções Python."""
    
    def __init__(self):
        self.project_root = Path(__file__).parent.parent.parent
        self.modules_path = self.project_root / "wiki/update/modules"
        self.catalog_path = self.project_root / "wiki/update/function_catalog"
        
        # Criar diretório do catálogo
        self.catalog_path.mkdir(exist_ok=True)
        
        # Estatísticas do catálogo
        self.catalog_stats = {
            "total_functions": 0,
            "total_classes": 0,
            "total_modules": 0,
            "total_categories": 0,
            "functions_cataloged": 0,
            "classes_cataloged": 0,
            "errors": [],
            "warnings": []
        }
        
        # Catálogo principal
        self.function_catalog = {
            "metadata": {
                "created": datetime.now().isoformat(),
                "version": "1.0.0",
                "description": "Catálogo automático de funções Python",
                "total_functions": 0,
                "total_classes": 0,
                "total_modules": 0
            },
            "categories": {},
            "functions": {},
            "classes": {},
            "modules": {},
            "search_index": {}
        }
    
    def discover_python_files(self) -> List[Path]:
        """Descobre todos os arquivos Python nos módulos."""
        logger.info("🔍 Descobrindo arquivos Python nos módulos...")
        
        python_files = []
        
        if self.modules_path.exists():
            for py_file in self.modules_path.rglob("*.py"):
                # Excluir arquivos de teste e cache
                if not any(exclude in str(py_file) for exclude in ["__pycache__", "test_", "_test"]):
                    python_files.append(py_file)
        
        logger.info(f"📊 Encontrados {len(python_files)} arquivos Python")
        return python_files
    
    def analyze_python_file(self, file_path: Path) -> Dict[str, Any]:
        """Analisa um arquivo Python para extrair funções e classes."""
        try:
            # Tentar diferentes encodings
            content = None
            for encoding in ['utf-8', 'latin-1', 'cp1252']:
                try:
                    with open(file_path, 'r', encoding=encoding) as f:
                        content = f.read()
                    break
                except UnicodeDecodeError:
                    continue
            
            if content is None:
                logger.error(f"❌ Não foi possível ler {file_path} com nenhum encoding")
                return {"file_path": str(file_path), "error": "encoding_error"}
            
            # Análise AST
            tree = ast.parse(content)
            
            analysis = {
                "file_path": str(file_path),
                "file_name": file_path.name,
                "module_path": str(file_path.relative_to(self.modules_path)),
                "size": file_path.stat().st_size,
                "lines": len(content.split('\n')),
                "functions": [],
                "classes": [],
                "imports": [],
                "docstring": self.extract_module_docstring(content),
                "complexity": "low"
            }
            
            # Extrair funções e classes
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    function_info = self.extract_function_info(node, content)
                    analysis["functions"].append(function_info)
                elif isinstance(node, ast.ClassDef):
                    class_info = self.extract_class_info(node, content)
                    analysis["classes"].append(class_info)
                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        analysis["imports"].append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        analysis["imports"].append(node.module)
            
            # Determinar complexidade
            total_elements = len(analysis["functions"]) + len(analysis["classes"])
            if total_elements > 20:
                analysis["complexity"] = "high"
            elif total_elements > 10:
                analysis["complexity"] = "medium"
            
            return analysis
            
        except Exception as e:
            logger.error(f"❌ Erro ao analisar {file_path}: {e}")
            return {"file_path": str(file_path), "error": str(e)}
    
    def extract_function_info(self, node: ast.FunctionDef, content: str) -> Dict[str, Any]:
        """Extrai informações de uma função."""
        # Obter linhas da função
        start_line = node.lineno
        end_line = node.end_lineno if hasattr(node, 'end_lineno') else start_line + 10
        
        # Extrair docstring
        docstring = ast.get_docstring(node) or ""
        
        # Extrair argumentos
        args = []
        for arg in node.args.args:
            args.append({
                "name": arg.arg,
                "annotation": ast.unparse(arg.annotation) if arg.annotation else None
            })
        
        # Extrair decoradores
        decorators = []
        for decorator in node.decorator_list:
            decorators.append(ast.unparse(decorator))
        
        # Determinar tipo de função
        function_type = "function"
        if node.name.startswith("__") and node.name.endswith("__"):
            function_type = "magic_method"
        elif node.name.startswith("_"):
            function_type = "private_method"
        elif any(decorator.startswith("@classmethod") for decorator in decorators):
            function_type = "class_method"
        elif any(decorator.startswith("@staticmethod") for decorator in decorators):
            function_type = "static_method"
        
        return {
            "name": node.name,
            "type": function_type,
            "docstring": docstring,
            "args": args,
            "decorators": decorators,
            "start_line": start_line,
            "end_line": end_line,
            "returns": ast.unparse(node.returns) if node.returns else None,
            "async": isinstance(node, ast.AsyncFunctionDef)
        }
    
    def extract_class_info(self, node: ast.ClassDef, content: str) -> Dict[str, Any]:
        """Extrai informações de uma classe."""
        # Obter linhas da classe
        start_line = node.lineno
        end_line = node.end_lineno if hasattr(node, 'end_lineno') else start_line + 20
        
        # Extrair docstring
        docstring = ast.get_docstring(node) or ""
        
        # Extrair métodos
        methods = []
        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                method_info = self.extract_function_info(item, content)
                methods.append(method_info)
        
        # Extrair decoradores
        decorators = []
        for decorator in node.decorator_list:
            decorators.append(ast.unparse(decorator))
        
        # Extrair bases
        bases = []
        for base in node.bases:
            bases.append(ast.unparse(base))
        
        return {
            "name": node.name,
            "docstring": docstring,
            "methods": methods,
            "decorators": decorators,
            "bases": bases,
            "start_line": start_line,
            "end_line": end_line
        }
    
    def extract_module_docstring(self, content: str) -> str:
        """Extrai docstring do módulo."""
        try:
            tree = ast.parse(content)
            return ast.get_docstring(tree) or ""
        except:
            return ""
    
    def categorize_function(self, function_info: Dict[str, Any], module_path: str) -> str:
        """Categoriza uma função baseada em seu contexto."""
        # Extrair categoria do caminho do módulo
        parts = module_path.split('/')
        if len(parts) >= 2:
            return parts[0]  # Primeira parte é a categoria
        
        # Fallback baseado no nome da função
        function_name = function_info["name"].lower()
        
        if any(keyword in function_name for keyword in ["map", "index", "update"]):
            return "maps"
        elif any(keyword in function_name for keyword in ["agent", "orchestrator", "workflow"]):
            return "agents"
        elif any(keyword in function_name for keyword in ["metric", "monitor", "dashboard"]):
            return "metrics"
        elif any(keyword in function_name for keyword in ["analyze", "search", "context"]):
            return "analysis"
        elif any(keyword in function_name for keyword in ["python", "script", "error"]):
            return "python"
        elif any(keyword in function_name for keyword in ["tool", "file", "backup"]):
            return "tools"
        elif any(keyword in function_name for keyword in ["wiki", "documentation", "markdown"]):
            return "documentation"
        else:
            return "python"  # Fallback
    
    def build_function_catalog(self) -> bool:
        """Constrói o catálogo completo de funções."""
        logger.info("🚀 Iniciando construção do catálogo de funções...")
        
        # Descobrir arquivos Python
        python_files = self.discover_python_files()
        
        if not python_files:
            logger.warning("⚠️ Nenhum arquivo Python encontrado")
            return False
        
        # Analisar cada arquivo
        for file_path in python_files:
            logger.info(f"📋 Analisando: {file_path.name}")
            
            analysis = self.analyze_python_file(file_path)
            
            if "error" in analysis:
                self.catalog_stats["errors"].append(f"{file_path}: {analysis['error']}")
                continue
            
            # Adicionar ao catálogo
            self.add_to_catalog(analysis)
        
        # Construir índices de busca
        self.build_search_index()
        
        # Atualizar estatísticas
        self.update_catalog_stats()
        
        logger.info("✅ Catálogo de funções construído com sucesso!")
        return True
    
    def add_to_catalog(self, analysis: Dict[str, Any]):
        """Adiciona análise de arquivo ao catálogo."""
        module_path = analysis["module_path"]
        file_name = analysis["file_name"]
        
        # Adicionar módulo ao catálogo
        self.function_catalog["modules"][module_path] = {
            "file_name": file_name,
            "size": analysis["size"],
            "lines": analysis["lines"],
            "complexity": analysis["complexity"],
            "docstring": analysis["docstring"],
            "imports": analysis["imports"],
            "function_count": len(analysis["functions"]),
            "class_count": len(analysis["classes"])
        }
        
        # Processar funções
        for function_info in analysis["functions"]:
            category = self.categorize_function(function_info, module_path)
            
            # Criar ID único para a função
            function_id = f"{module_path}.{function_info['name']}"
            
            # Adicionar função ao catálogo
            self.function_catalog["functions"][function_id] = {
                **function_info,
                "module_path": module_path,
                "category": category,
                "file_name": file_name
            }
            
            # Adicionar à categoria
            if category not in self.function_catalog["categories"]:
                self.function_catalog["categories"][category] = {
                    "functions": [],
                    "classes": [],
                    "total_functions": 0,
                    "total_classes": 0
                }
            
            self.function_catalog["categories"][category]["functions"].append(function_id)
            self.function_catalog["categories"][category]["total_functions"] += 1
            
            self.catalog_stats["functions_cataloged"] += 1
        
        # Processar classes
        for class_info in analysis["classes"]:
            category = self.categorize_function({"name": class_info["name"]}, module_path)
            
            # Criar ID único para a classe
            class_id = f"{module_path}.{class_info['name']}"
            
            # Adicionar classe ao catálogo
            self.function_catalog["classes"][class_id] = {
                **class_info,
                "module_path": module_path,
                "category": category,
                "file_name": file_name
            }
            
            # Adicionar à categoria
            if category not in self.function_catalog["categories"]:
                self.function_catalog["categories"][category] = {
                    "functions": [],
                    "classes": [],
                    "total_functions": 0,
                    "total_classes": 0
                }
            
            self.function_catalog["categories"][category]["classes"].append(class_id)
            self.function_catalog["categories"][category]["total_classes"] += 1
            
            self.catalog_stats["classes_cataloged"] += 1
    
    def build_search_index(self):
        """Constrói índice de busca para o catálogo."""
        logger.info("🔍 Construindo índice de busca...")
        
        search_index = {
            "by_name": {},
            "by_category": {},
            "by_type": {},
            "by_module": {},
            "by_keyword": {}
        }
        
        # Índice por nome
        for function_id, function_info in self.function_catalog["functions"].items():
            name = function_info["name"].lower()
            if name not in search_index["by_name"]:
                search_index["by_name"][name] = []
            search_index["by_name"][name].append(function_id)
        
        # Índice por categoria
        for category, category_info in self.function_catalog["categories"].items():
            search_index["by_category"][category] = {
                "functions": category_info["functions"],
                "classes": category_info["classes"]
            }
        
        # Índice por tipo
        for function_id, function_info in self.function_catalog["functions"].items():
            func_type = function_info["type"]
            if func_type not in search_index["by_type"]:
                search_index["by_type"][func_type] = []
            search_index["by_type"][func_type].append(function_id)
        
        # Índice por módulo
        for function_id, function_info in self.function_catalog["functions"].items():
            module_path = function_info["module_path"]
            if module_path not in search_index["by_module"]:
                search_index["by_module"][module_path] = []
            search_index["by_module"][module_path].append(function_id)
        
        # Índice por palavra-chave (docstring)
        for function_id, function_info in self.function_catalog["functions"].items():
            docstring = function_info["docstring"].lower()
            if docstring:
                words = docstring.split()
                for word in words:
                    if len(word) > 3:  # Ignorar palavras muito curtas
                        if word not in search_index["by_keyword"]:
                            search_index["by_keyword"][word] = []
                        if function_id not in search_index["by_keyword"][word]:
                            search_index["by_keyword"][word].append(function_id)
        
        self.function_catalog["search_index"] = search_index
    
    def update_catalog_stats(self):
        """Atualiza estatísticas do catálogo."""
        self.function_catalog["metadata"]["total_functions"] = len(self.function_catalog["functions"])
        self.function_catalog["metadata"]["total_classes"] = len(self.function_catalog["classes"])
        self.function_catalog["metadata"]["total_modules"] = len(self.function_catalog["modules"])
        
        self.catalog_stats["total_functions"] = len(self.function_catalog["functions"])
        self.catalog_stats["total_classes"] = len(self.function_catalog["classes"])
        self.catalog_stats["total_modules"] = len(self.function_catalog["modules"])
        self.catalog_stats["total_categories"] = len(self.function_catalog["categories"])
    
    def save_catalog(self):
        """Salva o catálogo em arquivos JSON."""
        logger.info("💾 Salvando catálogo...")
        
        # Salvar catálogo principal
        catalog_file = self.catalog_path / "function_catalog.json"
        with open(catalog_file, 'w', encoding='utf-8') as f:
            json.dump(self.function_catalog, f, indent=2, ensure_ascii=False)
        
        # Salvar catálogo por categoria
        for category, category_info in self.function_catalog["categories"].items():
            category_file = self.catalog_path / f"catalog_{category}.json"
            category_data = {
                "category": category,
                "metadata": {
                    "total_functions": category_info["total_functions"],
                    "total_classes": category_info["total_classes"],
                    "created": datetime.now().isoformat()
                },
                "functions": {
                    func_id: self.function_catalog["functions"][func_id]
                    for func_id in category_info["functions"]
                },
                "classes": {
                    class_id: self.function_catalog["classes"][class_id]
                    for class_id in category_info["classes"]
                }
            }
            
            with open(category_file, 'w', encoding='utf-8') as f:
                json.dump(category_data, f, indent=2, ensure_ascii=False)
        
        # Salvar índice de busca
        search_index_file = self.catalog_path / "search_index.json"
        with open(search_index_file, 'w', encoding='utf-8') as f:
            json.dump(self.function_catalog["search_index"], f, indent=2, ensure_ascii=False)
        
        logger.info(f"📄 Catálogo salvo em: {self.catalog_path}")
    
    def generate_catalog_report(self) -> Dict[str, Any]:
        """Gera relatório do catálogo."""
        return {
            "task": "12.4",
            "description": "Implementar sistema de catálogo de funções",
            "status": "completed",
            "timestamp": datetime.now().isoformat(),
            "catalog_stats": self.catalog_stats,
            "catalog_info": {
                "total_functions": len(self.function_catalog["functions"]),
                "total_classes": len(self.function_catalog["classes"]),
                "total_modules": len(self.function_catalog["modules"]),
                "total_categories": len(self.function_catalog["categories"]),
                "catalog_path": str(self.catalog_path)
            },
            "next_task": "12.5 - Criar validador automático de scripts Python"
        }
    
    def save_catalog_report(self, report: Dict[str, Any]):
        """Salva relatório do catálogo."""
        report_file = self.project_root / "wiki/log/task_12_4_function_catalog_report.json"
        report_file.parent.mkdir(exist_ok=True)
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        logger.info(f"📄 Relatório salvo em: {report_file}")

def main():
    """Função principal do script."""
    print("🚀 Function Catalog Agent - Epic 12 Task 12.4")
    print("=" * 60)
    
    agent = FunctionCatalogAgent()
    
    # Construir catálogo
    success = agent.build_function_catalog()
    
    if success:
        # Salvar catálogo
        agent.save_catalog()
        
        # Gerar relatório
        report = agent.generate_catalog_report()
        agent.save_catalog_report(report)
        
        stats = report["catalog_stats"]
        catalog_info = report["catalog_info"]
        
        print("\n✅ Catálogo de funções criado com sucesso!")
        print(f"📊 Funções catalogadas: {stats['functions_cataloged']}")
        print(f"🏗️ Classes catalogadas: {stats['classes_cataloged']}")
        print(f"📁 Módulos processados: {stats['total_modules']}")
        print(f"🗂️ Categorias criadas: {stats['total_categories']}")
        print(f"📄 Catálogo salvo em: {catalog_info['catalog_path']}")
        print(f"📋 Próxima task: {report['next_task']}")
        
        if stats['errors']:
            print(f"\n❌ Erros: {len(stats['errors'])}")
            for error in stats['errors'][:3]:  # Mostrar apenas os primeiros 3
                print(f"  - {error}")
        
        if stats['warnings']:
            print(f"\n⚠️ Avisos: {len(stats['warnings'])}")
            for warning in stats['warnings'][:3]:  # Mostrar apenas os primeiros 3
                print(f"  - {warning}")
        
    else:
        print("❌ Erro na criação do catálogo de funções")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 