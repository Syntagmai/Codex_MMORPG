#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Auditor Agent
Responsável por auditar todos os agentes BMAD e scripts Python
"""

import os
import json
import ast
import importlib.util
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set, Tuple
import argparse

class PythonAuditor:
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root).resolve()
        self.audit_results = {
            "timestamp": datetime.now().isoformat(),
            "project_root": str(self.project_root),
            "total_python_files": 0,
            "bmad_agents": [],
            "issues": [],
            "import_errors": [],
            "syntax_errors": [],
            "obsolete_imports": [],
            "missing_dependencies": [],
            "recommendations": []
        }
        
    def scan_python_files(self) -> Dict:
        """Escaneia todos os arquivos Python do projeto"""
        print("🔍 Iniciando auditoria de arquivos Python...")
        
        # Encontra todos os arquivos Python
        python_files = list(self.project_root.rglob("*.py"))
        self.audit_results["total_python_files"] = len(python_files)
        
        print(f"📄 Encontrados {len(python_files)} arquivos Python")
        
        # Analisa cada arquivo
        for py_file in python_files:
            self._analyze_python_file(py_file)
        
        # Gera recomendações
        self._generate_recommendations()
        
        return self.audit_results
    
    def _analyze_python_file(self, file_path: Path):
        """Analisa um arquivo Python específico"""
        relative_path = file_path.relative_to(self.project_root)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Verifica se é um agente BMAD
            if "wiki/bmad/agents" in str(file_path):
                self.audit_results["bmad_agents"].append({
                    "file": str(relative_path),
                    "size": len(content),
                    "lines": len(content.splitlines())
                })
            
            # Analisa sintaxe
            try:
                ast.parse(content)
            except SyntaxError as e:
                self.audit_results["syntax_errors"].append({
                    "file": str(relative_path),
                    "line": e.lineno,
                    "error": str(e),
                    "severity": "high"
                })
            
            # Analisa imports
            self._analyze_imports(content, relative_path)
            
            # Verifica imports problemáticos
            self._check_problematic_imports(content, relative_path)
            
        except Exception as e:
            self.audit_results["issues"].append({
                "file": str(relative_path),
                "type": "file_read_error",
                "error": str(e),
                "severity": "medium"
            })
    
    def _analyze_imports(self, content: str, file_path: Path):
        """Analisa imports do arquivo"""
        lines = content.splitlines()
        
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            
            # Verifica imports
            if line.startswith(('import ', 'from ')):
                try:
                    # Tenta analisar o import
                    if line.startswith('import '):
                        module_name = line[7:].split()[0]
                    else:  # from ... import
                        parts = line[5:].split(' import ')
                        if len(parts) == 2:
                            module_name = parts[0].strip()
                        else:
                            continue
                    
                    # Verifica se o módulo existe
                    if not self._module_exists(module_name):
                        self.audit_results["missing_dependencies"].append({
                            "file": str(file_path),
                            "line": line_num,
                            "import": line,
                            "module": module_name,
                            "severity": "medium"
                        })
                        
                except Exception as e:
                    self.audit_results["import_errors"].append({
                        "file": str(file_path),
                        "line": line_num,
                        "import": line,
                        "error": str(e),
                        "severity": "medium"
                    })
    
    def _check_problematic_imports(self, content: str, file_path: Path):
        """Verifica imports problemáticos conhecidos"""
        problematic_imports = [
            "unicode_aliases",
            "from unicode_aliases import",
            "import unicode_aliases"
        ]
        
        lines = content.splitlines()
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            for problematic in problematic_imports:
                if problematic in line:
                    self.audit_results["obsolete_imports"].append({
                        "file": str(file_path),
                        "line": line_num,
                        "import": line,
                        "problematic": problematic,
                        "severity": "high"
                    })
                    break
    
    def _module_exists(self, module_name: str) -> bool:
        """Verifica se um módulo existe"""
        try:
            # Remove submodules
            base_module = module_name.split('.')[0]
            
            # Lista de módulos padrão do Python
            stdlib_modules = {
                'os', 'sys', 'json', 'datetime', 'pathlib', 'typing', 
                'argparse', 'ast', 'importlib', 'hashlib', 're', 'collections',
                'itertools', 'functools', 'logging', 'subprocess', 'shutil',
                'tempfile', 'urllib', 'http', 'socket', 'threading', 'multiprocessing',
                'tkinter', 'sqlite3', 'pickle', 'copy', 'math', 'random', 'time',
                'traceback', 'warnings', 'weakref', 'abc', 'enum', 'dataclasses'
            }
            
            if base_module in stdlib_modules:
                return True
            
            # Tenta importar
            importlib.import_module(base_module)
            return True
            
        except ImportError:
            return False
    
    def _generate_recommendations(self):
        """Gera recomendações baseadas na análise"""
        recommendations = []
        
        # Recomendações baseadas em problemas encontrados
        if self.audit_results["obsolete_imports"]:
            recommendations.append({
                "category": "Limpeza",
                "action": "Remover imports de unicode_aliases",
                "priority": "high",
                "description": f"Encontrados {len(self.audit_results['obsolete_imports'])} imports obsoletos"
            })
        
        if self.audit_results["syntax_errors"]:
            recommendations.append({
                "category": "Correção",
                "action": "Corrigir erros de sintaxe",
                "priority": "high",
                "description": f"Encontrados {len(self.audit_results['syntax_errors'])} erros de sintaxe"
            })
        
        if self.audit_results["missing_dependencies"]:
            recommendations.append({
                "category": "Dependências",
                "action": "Instalar dependências faltantes",
                "priority": "medium",
                "description": f"Encontradas {len(self.audit_results['missing_dependencies'])} dependências faltantes"
            })
        
        # Recomendações gerais
        recommendations.extend([
            {
                "category": "Qualidade",
                "action": "Implementar testes unitários",
                "priority": "medium",
                "description": "Para todos os agentes BMAD"
            },
            {
                "category": "Documentação",
                "action": "Adicionar docstrings",
                "priority": "low",
                "description": "Para melhor documentação do código"
            },
            {
                "category": "Padronização",
                "action": "Aplicar PEP 8",
                "priority": "low",
                "description": "Para padronização do código"
            }
        ])
        
        self.audit_results["recommendations"] = recommendations
    
    def save_report(self, output_file: str = "python_audit_report.json"):
        """Salva o relatório em arquivo JSON"""
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.audit_results, f, indent=2, ensure_ascii=False)
        
        print(f"📄 Relatório salvo em: {output_path}")
        return output_path
    
    def print_summary(self):
        """Imprime resumo da auditoria"""
        print("\n" + "="*60)
        print("📊 RESUMO DA AUDITORIA PYTHON")
        print("="*60)
        
        print(f"📄 Total de arquivos Python: {self.audit_results['total_python_files']}")
        print(f"🤖 Agentes BMAD: {len(self.audit_results['bmad_agents'])}")
        print(f"⚠️  Problemas encontrados: {len(self.audit_results['issues'])}")
        print(f"🚨 Erros de sintaxe: {len(self.audit_results['syntax_errors'])}")
        print(f"📦 Imports obsoletos: {len(self.audit_results['obsolete_imports'])}")
        print(f"❌ Dependências faltantes: {len(self.audit_results['missing_dependencies'])}")
        print(f"💡 Recomendações: {len(self.audit_results['recommendations'])}")
        
        # Mostra agentes BMAD
        if self.audit_results['bmad_agents']:
            print(f"\n🤖 AGENTES BMAD ({len(self.audit_results['bmad_agents'])}):")
            for agent in self.audit_results['bmad_agents'][:10]:
                print(f"  • {agent['file']} ({agent['lines']} linhas)")
        
        # Mostra erros críticos
        critical_errors = [error for error in self.audit_results['syntax_errors'] if error.get('severity') == 'high']
        if critical_errors:
            print(f"\n🚨 ERROS CRÍTICOS ({len(critical_errors)}):")
            for error in critical_errors[:5]:
                print(f"  • {error['file']}:{error['line']} - {error['error']}")
        
        # Mostra imports obsoletos
        if self.audit_results['obsolete_imports']:
            print(f"\n📦 IMPORTS OBSOLETOS ({len(self.audit_results['obsolete_imports'])}):")
            for imp in self.audit_results['obsolete_imports'][:5]:
                print(f"  • {imp['file']}:{imp['line']} - {imp['import']}")
        
        print("\n" + "="*60)

def main():
    parser = argparse.ArgumentParser(description="Python Auditor Agent")
    parser.add_argument("--project-root", default=".", help="Raiz do projeto para auditar")
    parser.add_argument("--output", default="python_audit_report.json", help="Arquivo de saída")
    parser.add_argument("--scan", action="store_true", help="Executar escaneamento completo")
    
    args = parser.parse_args()
    
    if args.scan:
        auditor = PythonAuditor(args.project_root)
        results = auditor.scan_python_files()
        auditor.save_report(args.output)
        auditor.print_summary()
        
        return results
    
    print("🔍 Python Auditor Agent")
    print("Use --scan para executar a auditoria completa")

if __name__ == "__main__":
    main() 