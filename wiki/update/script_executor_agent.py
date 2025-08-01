#!/usr/bin/env python3
"""
Script Executor Agent - Sistema Inteligente de Execução de Scripts Python

Este agente implementa um sistema inteligente para execução automática de scripts Python
com análise de dependências, validação, monitoramento e tratamento de erros.
"""

import os
import sys
import subprocess
import importlib
import ast
import logging
import json
import time
import threading
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, asdict
from datetime import datetime
import traceback

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class ExecutionResult:
    """Resultado da execução de um script"""
    script_path: str
    success: bool
    execution_time: float
    output: str
    error: Optional[str]
    return_code: int
    dependencies: List[str]
    timestamp: str
    memory_usage: Optional[float] = None
    cpu_usage: Optional[float] = None

@dataclass
class ScriptInfo:
    """Informações sobre um script Python"""
    path: str
    name: str
    dependencies: List[str]
    imports: List[str]
    functions: List[str]
    classes: List[str]
    complexity: int
    lines: int
    is_valid: bool
    last_modified: str

class DependencyAnalyzer:
    """Analisador de dependências de scripts Python"""
    
    def __init__(self):
        self.import_cache = {}
    
    def analyze_script(self, script_path: str) -> ScriptInfo:
        """Analisa um script Python e retorna suas informações"""
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            tree = ast.parse(content)
            
            imports = []
            functions = []
            classes = []
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    module = node.module or ''
                    for alias in node.names:
                        imports.append(f"{module}.{alias.name}")
                elif isinstance(node, ast.FunctionDef):
                    functions.append(node.name)
                elif isinstance(node, ast.ClassDef):
                    classes.append(node.name)
            
            # Calcular complexidade ciclomática simples
            complexity = self._calculate_complexity(tree)
            
            # Verificar se o script é válido
            is_valid = self._validate_script(script_path)
            
            # Obter data de modificação
            stat = os.stat(script_path)
            last_modified = datetime.fromtimestamp(stat.st_mtime).isoformat()
            
            return ScriptInfo(
                path=script_path,
                name=os.path.basename(script_path),
                dependencies=imports,
                imports=imports,
                functions=functions,
                classes=classes,
                complexity=complexity,
                lines=len(content.splitlines()),
                is_valid=is_valid,
                last_modified=last_modified
            )
            
        except Exception as e:
            logger.error(f"Erro ao analisar script {script_path}: {e}")
            return ScriptInfo(
                path=script_path,
                name=os.path.basename(script_path),
                dependencies=[],
                imports=[],
                functions=[],
                classes=[],
                complexity=0,
                lines=0,
                is_valid=False,
                last_modified=datetime.now().isoformat()
            )
    
    def _calculate_complexity(self, tree: ast.AST) -> int:
        """Calcula complexidade ciclomática simples"""
        complexity = 1
        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.While, ast.For, ast.ExceptHandler)):
                complexity += 1
        return complexity
    
    def _validate_script(self, script_path: str) -> bool:
        """Valida se um script Python é sintaticamente correto"""
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                content = f.read()
            ast.parse(content)
            return True
        except:
            return False

class ScriptExecutor:
    """Executor inteligente de scripts Python"""
    
    def __init__(self, base_path: str = None):
        self.base_path = Path(base_path) if base_path else Path.cwd()
        self.dependency_analyzer = DependencyAnalyzer()
        self.execution_history = []
        self.running_processes = {}
        
    def execute_script(self, script_path: str, args: List[str] = None, 
                      timeout: int = 300, capture_output: bool = True) -> ExecutionResult:
        """Executa um script Python com análise e monitoramento"""
        
        script_path = Path(script_path)
        if not script_path.exists():
            return ExecutionResult(
                script_path=str(script_path),
                success=False,
                execution_time=0.0,
                output="",
                error=f"Script não encontrado: {script_path}",
                return_code=-1,
                dependencies=[],
                timestamp=datetime.now().isoformat()
            )
        
        # Analisar dependências
        script_info = self.dependency_analyzer.analyze_script(str(script_path))
        
        if not script_info.is_valid:
            return ExecutionResult(
                script_path=str(script_path),
                success=False,
                execution_time=0.0,
                output="",
                error="Script contém erros de sintaxe",
                return_code=-1,
                dependencies=script_info.dependencies,
                timestamp=datetime.now().isoformat()
            )
        
        # Verificar dependências
        missing_deps = self._check_dependencies(script_info.dependencies)
        if missing_deps:
            logger.warning(f"Dependências faltando para {script_path}: {missing_deps}")
        
        # Executar script
        start_time = time.time()
        result = self._run_script(script_path, args, timeout, capture_output)
        execution_time = time.time() - start_time
        
        # Criar resultado
        execution_result = ExecutionResult(
            script_path=str(script_path),
            success=result['success'],
            execution_time=execution_time,
            output=result['output'],
            error=result['error'],
            return_code=result['return_code'],
            dependencies=script_info.dependencies,
            timestamp=datetime.now().isoformat()
        )
        
        # Adicionar ao histórico
        self.execution_history.append(execution_result)
        
        return execution_result
    
    def _run_script(self, script_path: Path, args: List[str], 
                   timeout: int, capture_output: bool) -> Dict[str, Any]:
        """Executa um script Python usando subprocess"""
        
        cmd = [sys.executable, str(script_path)]
        if args:
            cmd.extend(args)
        
        try:
            if capture_output:
                process = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                    cwd=self.base_path
                )
                
                return {
                    'success': process.returncode == 0,
                    'output': process.stdout,
                    'error': process.stderr if process.stderr else None,
                    'return_code': process.returncode
                }
            else:
                process = subprocess.run(
                    cmd,
                    timeout=timeout,
                    cwd=self.base_path
                )
                
                return {
                    'success': process.returncode == 0,
                    'output': '',
                    'error': None,
                    'return_code': process.returncode
                }
                
        except subprocess.TimeoutExpired:
            return {
                'success': False,
                'output': '',
                'error': f'Timeout após {timeout} segundos',
                'return_code': -1
            }
        except Exception as e:
            return {
                'success': False,
                'output': '',
                'error': str(e),
                'return_code': -1
            }
    
    def _check_dependencies(self, dependencies: List[str]) -> List[str]:
        """Verifica se as dependências estão disponíveis"""
        missing = []
        for dep in dependencies:
            if '.' in dep:
                # Import relativo
                module_name = dep.split('.')[0]
            else:
                module_name = dep
            
            try:
                importlib.import_module(module_name)
            except ImportError:
                missing.append(dep)
        
        return missing
    
    def execute_batch(self, scripts: List[str], parallel: bool = False, 
                     max_workers: int = 4) -> List[ExecutionResult]:
        """Executa múltiplos scripts em lote"""
        
        if parallel:
            return self._execute_parallel(scripts, max_workers)
        else:
            results = []
            for script in scripts:
                result = self.execute_script(script)
                results.append(result)
            return results
    
    def _execute_parallel(self, scripts: List[str], max_workers: int) -> List[ExecutionResult]:
        """Executa scripts em paralelo"""
        import concurrent.futures
        
        results = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_script = {
                executor.submit(self.execute_script, script): script 
                for script in scripts
            }
            
            for future in concurrent.futures.as_completed(future_to_script):
                result = future.result()
                results.append(result)
        
        return results
    
    def get_execution_history(self) -> List[ExecutionResult]:
        """Retorna o histórico de execuções"""
        return self.execution_history
    
    def get_statistics(self) -> Dict[str, Any]:
        """Retorna estatísticas das execuções"""
        if not self.execution_history:
            return {}
        
        total_executions = len(self.execution_history)
        successful_executions = sum(1 for r in self.execution_history if r.success)
        failed_executions = total_executions - successful_executions
        
        total_time = sum(r.execution_time for r in self.execution_history)
        avg_time = total_time / total_executions if total_executions > 0 else 0
        
        return {
            'total_executions': total_executions,
            'successful_executions': successful_executions,
            'failed_executions': failed_executions,
            'success_rate': (successful_executions / total_executions) * 100 if total_executions > 0 else 0,
            'total_execution_time': total_time,
            'average_execution_time': avg_time,
            'last_execution': self.execution_history[-1].timestamp if self.execution_history else None
        }

class ScriptExecutorAgent:
    """Agente principal para execução inteligente de scripts"""
    
    def __init__(self, base_path: str = None):
        self.executor = ScriptExecutor(base_path)
        self.reports_path = Path("wiki/update/executor_reports")
        self.reports_path.mkdir(exist_ok=True)
    
    def execute_task_12_8(self) -> Dict[str, Any]:
        """Executa a Task 12.8: Implementar executor inteligente de scripts"""
        
        logger.info("Iniciando Task 12.8: Implementar executor inteligente de scripts")
        
        # Testar o executor com alguns scripts existentes
        test_scripts = self._find_test_scripts()
        
        results = []
        for script in test_scripts:
            logger.info(f"Executando script de teste: {script}")
            result = self.executor.execute_script(script)
            results.append(result)
        
        # Gerar estatísticas
        stats = self.executor.get_statistics()
        
        # Salvar relatório
        report = {
            'task': '12.8',
            'epic': '12',
            'title': 'Implementar executor inteligente de scripts',
            'status': 'completed',
            'timestamp': datetime.now().isoformat(),
            'scripts_tested': len(test_scripts),
            'successful_executions': stats.get('successful_executions', 0),
            'failed_executions': stats.get('failed_executions', 0),
            'success_rate': stats.get('success_rate', 0),
            'average_execution_time': stats.get('average_execution_time', 0),
            'test_scripts': test_scripts,
            'results': [asdict(r) for r in results]
        }
        
        report_path = self.reports_path / "script_executor_report.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Task 12.8 concluída. Relatório salvo em: {report_path}")
        
        return report
    
    def _find_test_scripts(self) -> List[str]:
        """Encontra scripts para testar o executor"""
        test_scripts = []
        
        # Procurar scripts Python em diretórios específicos
        search_paths = [
            "wiki/update/python_tools",
            "wiki/update",
            "scripts",
            "tools"
        ]
        
        for search_path in search_paths:
            path = Path(search_path)
            if path.exists():
                for py_file in path.rglob("*.py"):
                    if py_file.name != "__init__.py" and py_file.name != "script_executor_agent.py":
                        test_scripts.append(str(py_file))
                        if len(test_scripts) >= 5:  # Limitar a 5 scripts para teste
                            break
        
        return test_scripts[:5]  # Retornar no máximo 5 scripts

def main():
    """Função principal"""
    agent = ScriptExecutorAgent()
    
    try:
        report = agent.execute_task_12_8()
        print(f"Task 12.8 concluída com sucesso!")
        print(f"Scripts testados: {report['scripts_tested']}")
        print(f"Taxa de sucesso: {report['success_rate']:.1f}%")
        print(f"Tempo médio de execução: {report['average_execution_time']:.2f}s")
        
    except Exception as e:
        logger.error(f"Erro na execução da Task 12.8: {e}")
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 