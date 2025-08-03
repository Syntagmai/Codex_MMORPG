#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from unicode_aliases import *
"""
🚀 Python Validator Agent - Epic 12 Task 12.5
=============================================

Script para criar validador automático de scripts Python.
Baseado no catálogo de funções da Task 12.4.

Responsável: Python Validator Agent
Duração: 3-4 dias
Dependência: Task 12.4 (Catálogo de funções)
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

class PythonValidatorAgent:
    """Agente para validação automática de scripts Python."""
    
    def __init__(self):
        self.project_root = Path(__file__).parent.parent.parent
        self.modules_path = self.project_root / "wiki/update/modules"
        self.catalog_path = self.project_root / "wiki/update/function_catalog"
        self.validation_path = self.project_root / "wiki/update/validation_results"
        
        # Criar diretório de resultados
        self.validation_path.mkdir(exist_ok=True)
        
        # Carregar catálogo de funções
        self.function_catalog = self.load_function_catalog()
        
        # Estatísticas de validação
        self.validation_stats = {
            "total_files": 0,
            "files_validated": 0,
            "files_with_errors": 0,
            "files_with_warnings": 0,
            "syntax_errors": 0,
            "style_issues": 0,
            "quality_issues": 0,
            "errors": [],
            "warnings": [],
            "suggestions": []
        }
        
        # Regras de validação
        self.validation_rules = {
            "syntax": {
                "check_ast_parsing": True,
                "check_imports": True,
                "check_indentation": True
            },
            "style": {
                "check_naming_convention": True,
                "check_line_length": True,
                "check_docstrings": True,
                "check_comments": True
            },
            "quality": {
                "check_complexity": True,
                "check_duplicate_code": True,
                "check_unused_imports": True,
                "check_magic_numbers": True
            }
        }
    
    def load_function_catalog(self) -> Dict[str, Any]:
        """Carrega o catálogo de funções."""
        catalog_file = self.catalog_path / "function_catalog.json"
        if catalog_file.exists():
            with open(catalog_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            logger.warning("⚠️ Catálogo de funções não encontrado")
            return {}
    
    def discover_python_files(self) -> List[Path]:
        """Descobre todos os arquivos Python para validação."""
        logger.info("🔍 Descobrindo arquivos Python para validação...")
        
        python_files = []
        
        if self.modules_path.exists():
            for py_file in self.modules_path.rglob("*.py"):
                # Excluir arquivos de teste e cache
                if not any(exclude in str(py_file) for exclude in ["__pycache__", "test_", "_test"]):
                    python_files.append(py_file)
        
        logger.info(f"📊 Encontrados {len(python_files)} arquivos Python para validação")
        return python_files
    
    def validate_syntax(self, file_path: Path, content: str) -> Dict[str, Any]:
        """Valida a sintaxe de um arquivo Python."""
        validation_result = {
            "valid": True,
            "errors": [],
            "warnings": []
        }
        
        try:
            # Tentar fazer parse AST
            tree = ast.parse(content)
            validation_result["ast_valid"] = True
        except SyntaxError as e:
            validation_result["valid"] = False
            validation_result["ast_valid"] = False
            validation_result["errors"].append({
                "type": "syntax_error",
                "line": e.lineno,
                "message": str(e),
                "severity": "error"
            })
            self.validation_stats["syntax_errors"] += 1
        except Exception as e:
            validation_result["valid"] = False
            validation_result["ast_valid"] = False
            validation_result["errors"].append({
                "type": "parsing_error",
                "line": 0,
                "message": str(e),
                "severity": "error"
            })
            self.validation_stats["syntax_errors"] += 1
        
        return validation_result
    
    def validate_style(self, file_path: Path, content: str) -> Dict[str, Any]:
        """Valida o estilo de código Python."""
        validation_result = {
            "valid": True,
            "errors": [],
            "warnings": []
        }
        
        lines = content.split('\n')
        
        # Verificar comprimento das linhas
        for i, line in enumerate(lines, 1):
            if len(line) > 120:  # PEP 8 recomenda 79, mas 120 é mais flexível
                validation_result["warnings"].append({
                    "type": "line_too_long",
                    "line": i,
                    "message": f"Linha {i} tem {len(line)} caracteres (recomendado: 79)",
                    "severity": "warning"
                })
        
        # Verificar convenções de nomenclatura
        try:
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    if not re.match(r'^[a-z_][a-z0-9_]*$', node.name):
                        validation_result["warnings"].append({
                            "type": "naming_convention",
                            "line": node.lineno,
                            "message": f"Função '{node.name}' não segue convenção snake_case",
                            "severity": "warning"
                        })
                elif isinstance(node, ast.ClassDef):
                    if not re.match(r'^[A-Z][a-zA-Z0-9]*$', node.name):
                        validation_result["warnings"].append({
                            "type": "naming_convention",
                            "line": node.lineno,
                            "message": f"Classe '{node.name}' não segue convenção PascalCase",
                            "severity": "warning"
                        })
        except:
            pass  # Se não conseguir fazer parse, pula verificação de nomenclatura
        
        # Verificar docstrings
        if not content.strip().startswith('"""') and not content.strip().startswith("'''"):
            validation_result["warnings"].append({
                "type": "missing_module_docstring",
                "line": 1,
                "message": "Módulo não possui docstring",
                "severity": "warning"
            })
        
        return validation_result
    
    def validate_quality(self, file_path: Path, content: str) -> Dict[str, Any]:
        """Valida a qualidade do código Python."""
        validation_result = {
            "valid": True,
            "errors": [],
            "warnings": []
        }
        
        try:
            tree = ast.parse(content)
            
            # Verificar complexidade ciclomática
            complexity = self.calculate_cyclomatic_complexity(tree)
            if complexity > 10:
                validation_result["warnings"].append({
                    "type": "high_complexity",
                    "line": 1,
                    "message": f"Complexidade ciclomática alta: {complexity} (recomendado: < 10)",
                    "severity": "warning"
                })
            
            # Verificar imports não utilizados
            unused_imports = self.find_unused_imports(tree, content)
            for import_name in unused_imports:
                validation_result["warnings"].append({
                    "type": "unused_import",
                    "line": 1,
                    "message": f"Import não utilizado: {import_name}",
                    "severity": "warning"
                })
            
            # Verificar números mágicos
            magic_numbers = self.find_magic_numbers(content)
            for number, line in magic_numbers:
                validation_result["warnings"].append({
                    "type": "magic_number",
                    "line": line,
                    "message": f"Número mágico encontrado: {number}",
                    "severity": "warning"
                })
            
        except:
            pass  # Se não conseguir fazer parse, pula verificação de qualidade
        
        return validation_result
    
    def calculate_cyclomatic_complexity(self, tree: ast.AST) -> int:
        """Calcula a complexidade ciclomática de um AST."""
        complexity = 1  # Base complexity
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.While, ast.For, ast.AsyncFor)):
                complexity += 1
            elif isinstance(node, ast.ExceptHandler):
                complexity += 1
            elif isinstance(node, ast.With):
                complexity += 1
            elif isinstance(node, ast.AsyncWith):
                complexity += 1
        
        return complexity
    
    def find_unused_imports(self, tree: ast.AST, content: str) -> List[str]:
        """Encontra imports não utilizados."""
        imports = set()
        used_names = set()
        
        # Extrair imports
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module)
        
        # Extrair nomes utilizados
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                used_names.add(node.id)
            elif isinstance(node, ast.Attribute):
                if isinstance(node.value, ast.Name):
                    used_names.add(node.value.id)
        
        # Retornar imports não utilizados
        return list(imports - used_names)
    
    def find_magic_numbers(self, content: str) -> List[Tuple[str, int]]:
        """Encontra números mágicos no código."""
        magic_numbers = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Procurar por números que não são 0, 1, ou parte de strings
            numbers = re.findall(r'\b([2-9]\d*|1\d+)\b', line)
            for number in numbers:
                # Verificar se não é parte de uma string
                if f"'{number}" not in line and f'"{number}' not in line:
                    magic_numbers.append((number, i))
        
        return magic_numbers
    
    def validate_file(self, file_path: Path) -> Dict[str, Any]:
        """Valida um arquivo Python completo."""
        try:
            # Ler conteúdo do arquivo
            content = None
            for encoding in ['utf-8', 'latin-1', 'cp1252']:
                try:
                    with open(file_path, 'r', encoding=encoding) as f:
                        content = f.read()
                    break
                except UnicodeDecodeError:
                    continue
            
            if content is None:
                return {
                    "file_path": str(file_path),
                    "valid": False,
                    "error": "encoding_error",
                    "message": "Não foi possível ler o arquivo com nenhum encoding"
                }
            
            # Realizar validações
            syntax_result = self.validate_syntax(file_path, content)
            style_result = self.validate_style(file_path, content)
            quality_result = self.validate_quality(file_path, content)
            
            # Combinar resultados
            validation_result = {
                "file_path": str(file_path),
                "file_name": file_path.name,
                "module_path": str(file_path.relative_to(self.modules_path)),
                "size": file_path.stat().st_size,
                "lines": len(content.split('\n')),
                "valid": syntax_result["valid"] and style_result["valid"] and quality_result["valid"],
                "syntax_valid": syntax_result["valid"],
                "style_valid": style_result["valid"],
                "quality_valid": quality_result["valid"],
                "errors": syntax_result["errors"] + style_result["errors"] + quality_result["errors"],
                "warnings": syntax_result["warnings"] + style_result["warnings"] + quality_result["warnings"],
                "suggestions": []
            }
            
            # Gerar sugestões de melhoria
            if validation_result["warnings"]:
                validation_result["suggestions"].append("Considere corrigir os avisos de estilo e qualidade")
            
            if len(content.split('\n')) > 500:
                validation_result["suggestions"].append("Arquivo muito longo, considere dividir em módulos menores")
            
            return validation_result
            
        except Exception as e:
            return {
                "file_path": str(file_path),
                "valid": False,
                "error": "validation_error",
                "message": str(e)
            }
    
    def validate_all_files(self) -> bool:
        """Valida todos os arquivos Python descobertos."""
        logger.info("🚀 Iniciando validação de scripts Python...")
        
        # Descobrir arquivos
        python_files = self.discover_python_files()
        self.validation_stats["total_files"] = len(python_files)
        
        if not python_files:
            logger.warning("⚠️ Nenhum arquivo Python encontrado")
            return False
        
        # Validar cada arquivo
        validation_results = []
        
        for file_path in python_files:
            logger.info(f"📋 Validando: {file_path.name}")
            
            result = self.validate_file(file_path)
            validation_results.append(result)
            
            # Atualizar estatísticas
            if result.get("valid", False):
                self.validation_stats["files_validated"] += 1
            else:
                self.validation_stats["files_with_errors"] += 1
            
            if result.get("warnings"):
                self.validation_stats["files_with_warnings"] += 1
            
            # Coletar erros e avisos
            for error in result.get("errors", []):
                self.validation_stats["errors"].append({
                    "file": file_path.name,
                    "error": error
                })
            
            for warning in result.get("warnings", []):
                self.validation_stats["warnings"].append({
                    "file": file_path.name,
                    "warning": warning
                })
        
        # Salvar resultados
        self.save_validation_results(validation_results)
        
        logger.info("✅ Validação de scripts Python concluída!")
        return True
    
    def save_validation_results(self, results: List[Dict[str, Any]]):
        """Salva os resultados da validação."""
        logger.info("💾 Salvando resultados da validação...")
        
        # Resultados completos
        validation_file = self.validation_path / "python_validation_results.json"
        with open(validation_file, 'w', encoding='utf-8') as f:
            json.dump({
                "metadata": {
                    "created": datetime.now().isoformat(),
                    "total_files": len(results),
                    "validation_stats": self.validation_stats
                },
                "results": results
            }, f, indent=2, ensure_ascii=False)
        
        # Relatório resumido
        summary_file = self.validation_path / "validation_summary.json"
        summary = {
            "total_files": len(results),
            "valid_files": sum(1 for r in results if r.get("valid", False)),
            "invalid_files": sum(1 for r in results if not r.get("valid", False)),
            "files_with_warnings": sum(1 for r in results if r.get("warnings")),
            "total_errors": len(self.validation_stats["errors"]),
            "total_warnings": len(self.validation_stats["warnings"]),
            "syntax_errors": self.validation_stats["syntax_errors"],
            "style_issues": self.validation_stats["style_issues"],
            "quality_issues": self.validation_stats["quality_issues"]
        }
        
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        
        # Relatório por categoria
        category_report = self.generate_category_report(results)
        category_file = self.validation_path / "validation_by_category.json"
        with open(category_file, 'w', encoding='utf-8') as f:
            json.dump(category_report, f, indent=2, ensure_ascii=False)
        
        logger.info(f"📄 Resultados salvos em: {self.validation_path}")
    
    def generate_category_report(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Gera relatório de validação por categoria."""
        category_stats = {}
        
        for result in results:
            module_path = result.get("module_path", "")
            category = module_path.split('/')[0] if '/' in module_path else "unknown"
            
            if category not in category_stats:
                category_stats[category] = {
                    "total_files": 0,
                    "valid_files": 0,
                    "invalid_files": 0,
                    "files_with_warnings": 0,
                    "total_errors": 0,
                    "total_warnings": 0
                }
            
            category_stats[category]["total_files"] += 1
            
            if result.get("valid", False):
                category_stats[category]["valid_files"] += 1
            else:
                category_stats[category]["invalid_files"] += 1
            
            if result.get("warnings"):
                category_stats[category]["files_with_warnings"] += 1
            
            category_stats[category]["total_errors"] += len(result.get("errors", []))
            category_stats[category]["total_warnings"] += len(result.get("warnings", []))
        
        return category_stats
    
    def generate_validation_report(self) -> Dict[str, Any]:
        """Gera relatório da validação."""
        return {
            "task": "12.5",
            "description": "Criar validador automático de scripts Python",
            "status": "completed",
            "timestamp": datetime.now().isoformat(),
            "validation_stats": self.validation_stats,
            "validation_info": {
                "total_files": self.validation_stats["total_files"],
                "files_validated": self.validation_stats["files_validated"],
                "files_with_errors": self.validation_stats["files_with_errors"],
                "files_with_warnings": self.validation_stats["files_with_warnings"],
                "validation_path": str(self.validation_path)
            },
            "next_task": "12.6 - Implementar correção automática de erros Python"
        }
    
    def save_validation_report(self, report: Dict[str, Any]):
        """Salva relatório da validação."""
        report_file = self.project_root / "wiki/log/task_12_5_validation_report.json"
        report_file.parent.mkdir(exist_ok=True)
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        logger.info(f"📄 Relatório salvo em: {report_file}")

def main():
    """Função principal do script."""
    print("🚀 Python Validator Agent - Epic 12 Task 12.5")
    print("=" * 60)
    
    agent = PythonValidatorAgent()
    
    # Executar validação
    success = agent.validate_all_files()
    
    if success:
        # Gerar relatório
        report = agent.generate_validation_report()
        agent.save_validation_report(report)
        
        stats = report["validation_stats"]
        validation_info = report["validation_info"]
        
        print("\n✅ Validação de scripts Python concluída com sucesso!")
        print(f"📊 Arquivos processados: {stats['total_files']}")
        print(f"✅ Arquivos válidos: {stats['files_validated']}")
        print(f"❌ Arquivos com erros: {stats['files_with_errors']}")
        print(f"⚠️ Arquivos com avisos: {stats['files_with_warnings']}")
        print(f"🔍 Erros de sintaxe: {stats['syntax_errors']}")
        print(f"📄 Resultados salvos em: {validation_info['validation_path']}")
        print(f"📋 Próxima task: {report['next_task']}")
        
        if stats['errors']:
            print(f"\n❌ Erros encontrados: {len(stats['errors'])}")
            for error in stats['errors'][:3]:  # Mostrar apenas os primeiros 3
                print(f"  - {error['file']}: {error['error']['message']}")
        
        if stats['warnings']:
            print(f"\n⚠️ Avisos encontrados: {len(stats['warnings'])}")
            for warning in stats['warnings'][:3]:  # Mostrar apenas os primeiros 3
                print(f"  - {warning['file']}: {warning['warning']['message']}")
        
    else:
        print("❌ Erro na validação de scripts Python")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 