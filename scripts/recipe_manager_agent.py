#!/usr/bin/env python3
"""
Recipe Manager Agent - Sistema de Receitas Python

Este agente implementa um sistema de receitas para tarefas Python comuns,
permitindo criar, gerenciar e executar receitas reutilizáveis.
"""

import os
import sys
import json
import logging
import subprocess
import time
from pathlib import Path
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, asdict
from datetime import datetime
import traceback
import shutil
import re

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class RecipeStep:
    """Passo de uma receita"""
    name: str
    description: str
    command: str
    args: List[str]
    timeout: int = 300
    retry_count: int = 3
    required: bool = True
    condition: Optional[str] = None

@dataclass
class Recipe:
    """Receita Python"""
    name: str
    description: str
    version: str
    author: str
    category: str
    tags: List[str]
    steps: List[RecipeStep]
    dependencies: List[str]
    created_at: str
    updated_at: str
    success_rate: float = 0.0
    execution_count: int = 0

@dataclass
class RecipeExecution:
    """Resultado da execução de uma receita"""
    recipe_name: str
    success: bool
    execution_time: float
    steps_executed: int
    steps_failed: int
    output: str
    error: Optional[str]
    timestamp: str
    environment: Dict[str, str]

class RecipeManager:
    """Gerenciador de receitas Python"""
    
    def __init__(self, recipes_path: str = "wiki/update/recipes"):
        self.recipes_path = Path(recipes_path)
        self.recipes_path.mkdir(exist_ok=True)
        self.recipes = {}
        self.execution_history = []
        self.load_recipes()
    
    def load_recipes(self):
        """Carrega todas as receitas do diretório"""
        for recipe_file in self.recipes_path.glob("*.json"):
            try:
                with open(recipe_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    recipe = self._dict_to_recipe(data)
                    self.recipes[recipe.name] = recipe
                    logger.info(f"Receita carregada: {recipe.name}")
            except Exception as e:
                logger.error(f"Erro ao carregar receita {recipe_file}: {e}")
    
    def _dict_to_recipe(self, data: Dict) -> Recipe:
        """Converte dicionário para objeto Recipe"""
        steps = []
        for step_data in data.get('steps', []):
            step = RecipeStep(
                name=step_data['name'],
                description=step_data['description'],
                command=step_data['command'],
                args=step_data.get('args', []),
                timeout=step_data.get('timeout', 300),
                retry_count=step_data.get('retry_count', 3),
                required=step_data.get('required', True),
                condition=step_data.get('condition')
            )
            steps.append(step)
        
        return Recipe(
            name=data['name'],
            description=data['description'],
            version=data['version'],
            author=data['author'],
            category=data['category'],
            tags=data.get('tags', []),
            steps=steps,
            dependencies=data.get('dependencies', []),
            created_at=data['created_at'],
            updated_at=data['updated_at'],
            success_rate=data.get('success_rate', 0.0),
            execution_count=data.get('execution_count', 0)
        )
    
    def _recipe_to_dict(self, recipe: Recipe) -> Dict:
        """Converte objeto Recipe para dicionário"""
        return {
            'name': recipe.name,
            'description': recipe.description,
            'version': recipe.version,
            'author': recipe.author,
            'category': recipe.category,
            'tags': recipe.tags,
            'steps': [asdict(step) for step in recipe.steps],
            'dependencies': recipe.dependencies,
            'created_at': recipe.created_at,
            'updated_at': recipe.updated_at,
            'success_rate': recipe.success_rate,
            'execution_count': recipe.execution_count
        }
    
    def create_recipe(self, recipe: Recipe) -> bool:
        """Cria uma nova receita"""
        try:
            recipe_file = self.recipes_path / f"{recipe.name}.json"
            with open(recipe_file, 'w', encoding='utf-8') as f:
                json.dump(self._recipe_to_dict(recipe), f, indent=2, ensure_ascii=False)
            
            self.recipes[recipe.name] = recipe
            logger.info(f"Receita criada: {recipe.name}")
            return True
        except Exception as e:
            logger.error(f"Erro ao criar receita {recipe.name}: {e}")
            return False
    
    def get_recipe(self, name: str) -> Optional[Recipe]:
        """Obtém uma receita pelo nome"""
        return self.recipes.get(name)
    
    def list_recipes(self, category: Optional[str] = None) -> List[Recipe]:
        """Lista todas as receitas, opcionalmente filtradas por categoria"""
        if category:
            return [r for r in self.recipes.values() if r.category == category]
        return list(self.recipes.values())
    
    def execute_recipe(self, name: str, args: Dict[str, Any] = None) -> RecipeExecution:
        """Executa uma receita"""
        recipe = self.get_recipe(name)
        if not recipe:
            return RecipeExecution(
                recipe_name=name,
                success=False,
                execution_time=0.0,
                steps_executed=0,
                steps_failed=1,
                output="",
                error=f"Receita não encontrada: {name}",
                timestamp=datetime.now().isoformat(),
                environment={}
            )
        
        start_time = time.time()
        steps_executed = 0
        steps_failed = 0
        output_lines = []
        error_lines = []
        
        # Verificar dependências
        missing_deps = self._check_dependencies(recipe.dependencies)
        if missing_deps:
            error_lines.append(f"Dependências faltando: {missing_deps}")
            steps_failed += 1
        
        # Executar passos
        for step in recipe.steps:
            if step.condition and not self._evaluate_condition(step.condition, args):
                continue
            
            step_success = False
            for attempt in range(step.retry_count):
                try:
                    step_output = self._execute_step(step, args)
                    output_lines.append(f"[{step.name}] {step_output}")
                    step_success = True
                    steps_executed += 1
                    break
                except Exception as e:
                    if attempt == step.retry_count - 1:
                        error_lines.append(f"[{step.name}] Erro: {e}")
                        steps_failed += 1
                        if step.required:
                            break
                    else:
                        time.sleep(1)  # Aguardar antes de tentar novamente
        
        execution_time = time.time() - start_time
        success = steps_failed == 0
        
        # Criar resultado
        execution = RecipeExecution(
            recipe_name=name,
            success=success,
            execution_time=execution_time,
            steps_executed=steps_executed,
            steps_failed=steps_failed,
            output="\n".join(output_lines),
            error="\n".join(error_lines) if error_lines else None,
            timestamp=datetime.now().isoformat(),
            environment=dict(os.environ)
        )
        
        # Atualizar estatísticas da receita
        recipe.execution_count += 1
        if success:
            recipe.success_rate = ((recipe.success_rate * (recipe.execution_count - 1)) + 1.0) / recipe.execution_count
        else:
            recipe.success_rate = (recipe.success_rate * (recipe.execution_count - 1)) / recipe.execution_count
        
        recipe.updated_at = datetime.now().isoformat()
        self._save_recipe(recipe)
        
        # Adicionar ao histórico
        self.execution_history.append(execution)
        
        return execution
    
    def _execute_step(self, step: RecipeStep, args: Dict[str, Any] = None) -> str:
        """Executa um passo da receita"""
        if step.command == "python":
            return self._execute_python_script(step.args, args)
        elif step.command == "shell":
            return self._execute_shell_command(step.args, args)
        elif step.command == "copy":
            return self._execute_copy_operation(step.args, args)
        elif step.command == "create":
            return self._execute_create_operation(step.args, args)
        else:
            raise ValueError(f"Comando não suportado: {step.command}")
    
    def _execute_python_script(self, script_args: List[str], recipe_args: Dict[str, Any] = None) -> str:
        """Executa um script Python"""
        if not script_args:
            raise ValueError("Script não especificado")
        
        script_path = script_args[0]
        script_args = script_args[1:] if len(script_args) > 1 else []
        
        # Substituir variáveis da receita
        script_args = [self._substitute_variables(arg, recipe_args) for arg in script_args]
        
        cmd = [sys.executable, script_path] + script_args
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        
        if result.returncode != 0:
            raise RuntimeError(f"Script falhou: {result.stderr}")
        
        return result.stdout
    
    def _execute_shell_command(self, command_args: List[str], recipe_args: Dict[str, Any] = None) -> str:
        """Executa um comando shell"""
        if not command_args:
            raise ValueError("Comando não especificado")
        
        command = " ".join(command_args)
        command = self._substitute_variables(command, recipe_args)
        
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=300)
        
        if result.returncode != 0:
            raise RuntimeError(f"Comando falhou: {result.stderr}")
        
        return result.stdout
    
    def _execute_copy_operation(self, copy_args: List[str], recipe_args: Dict[str, Any] = None) -> str:
        """Executa operação de cópia"""
        if len(copy_args) < 2:
            raise ValueError("Origem e destino devem ser especificados")
        
        source = self._substitute_variables(copy_args[0], recipe_args)
        destination = self._substitute_variables(copy_args[1], recipe_args)
        
        if os.path.isfile(source):
            shutil.copy2(source, destination)
        elif os.path.isdir(source):
            shutil.copytree(source, destination, dirs_exist_ok=True)
        else:
            raise FileNotFoundError(f"Arquivo/diretório não encontrado: {source}")
        
        return f"Copiado: {source} -> {destination}"
    
    def _execute_create_operation(self, create_args: List[str], recipe_args: Dict[str, Any] = None) -> str:
        """Executa operação de criação"""
        if not create_args:
            raise ValueError("Caminho não especificado")
        
        path = self._substitute_variables(create_args[0], recipe_args)
        path_obj = Path(path)
        
        if path_obj.suffix:  # É um arquivo
            path_obj.parent.mkdir(parents=True, exist_ok=True)
            path_obj.touch()
            return f"Arquivo criado: {path}"
        else:  # É um diretório
            path_obj.mkdir(parents=True, exist_ok=True)
            return f"Diretório criado: {path}"
    
    def _substitute_variables(self, text: str, args: Dict[str, Any] = None) -> str:
        """Substitui variáveis no texto"""
        if not args:
            return text
        
        for key, value in args.items():
            placeholder = f"${{{key}}}"
            text = text.replace(placeholder, str(value))
        
        return text
    
    def _evaluate_condition(self, condition: str, args: Dict[str, Any] = None) -> bool:
        """Avalia uma condição"""
        try:
            # Substituir variáveis na condição
            condition = self._substitute_variables(condition, args)
            
            # Avaliar condição simples
            if condition.startswith("exists:"):
                path = condition[7:]
                return Path(path).exists()
            elif condition.startswith("not_exists:"):
                path = condition[11:]
                return not Path(path).exists()
            else:
                # Avaliar expressão Python simples
                return eval(condition)
        except:
            return False
    
    def _check_dependencies(self, dependencies: List[str]) -> List[str]:
        """Verifica se as dependências estão disponíveis"""
        missing = []
        for dep in dependencies:
            try:
                __import__(dep)
            except ImportError:
                missing.append(dep)
        return missing
    
    def _save_recipe(self, recipe: Recipe):
        """Salva uma receita no arquivo"""
        try:
            recipe_file = self.recipes_path / f"{recipe.name}.json"
            with open(recipe_file, 'w', encoding='utf-8') as f:
                json.dump(self._recipe_to_dict(recipe), f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Erro ao salvar receita {recipe.name}: {e}")
    
    def get_execution_history(self) -> List[RecipeExecution]:
        """Retorna o histórico de execuções"""
        return self.execution_history
    
    def get_statistics(self) -> Dict[str, Any]:
        """Retorna estatísticas das receitas"""
        if not self.recipes:
            return {}
        
        total_recipes = len(self.recipes)
        total_executions = sum(r.execution_count for r in self.recipes.values())
        avg_success_rate = sum(r.success_rate for r in self.recipes.values()) / total_recipes if total_recipes > 0 else 0
        
        categories = {}
        for recipe in self.recipes.values():
            categories[recipe.category] = categories.get(recipe.category, 0) + 1
        
        return {
            'total_recipes': total_recipes,
            'total_executions': total_executions,
            'average_success_rate': avg_success_rate,
            'categories': categories,
            'most_used_recipe': max(self.recipes.values(), key=lambda r: r.execution_count).name if self.recipes else None
        }

class RecipeManagerAgent:
    """Agente principal para gerenciamento de receitas"""
    
    def __init__(self):
        self.manager = RecipeManager()
        self.reports_path = Path("wiki/update/recipe_reports")
        self.reports_path.mkdir(exist_ok=True)
    
    def execute_task_12_9(self) -> Dict[str, Any]:
        """Executa a Task 12.9: Criar sistema de receitas Python"""
        
        logger.info("Iniciando Task 12.9: Criar sistema de receitas Python")
        
        # Criar receitas de exemplo
        recipes_created = self._create_sample_recipes()
        
        # Executar algumas receitas de teste
        executions = []
        for recipe_name in ["python_script_validator", "code_analyzer", "backup_creator"]:
            if recipe_name in self.manager.recipes:
                logger.info(f"Executando receita: {recipe_name}")
                execution = self.manager.execute_recipe(recipe_name)
                executions.append(execution)
        
        # Gerar estatísticas
        stats = self.manager.get_statistics()
        
        # Salvar relatório
        report = {
            'task': '12.9',
            'epic': '12',
            'title': 'Criar sistema de receitas Python',
            'status': 'completed',
            'timestamp': datetime.now().isoformat(),
            'recipes_created': recipes_created,
            'total_recipes': stats.get('total_recipes', 0),
            'total_executions': stats.get('total_executions', 0),
            'average_success_rate': stats.get('average_success_rate', 0),
            'categories': stats.get('categories', {}),
            'executions': [asdict(e) for e in executions]
        }
        
        report_path = self.reports_path / "recipe_manager_report.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Task 12.9 concluída. Relatório salvo em: {report_path}")
        
        return report
    
    def _create_sample_recipes(self) -> int:
        """Cria receitas de exemplo"""
        recipes = []
        
        # Receita para validar scripts Python
        validator_recipe = Recipe(
            name="python_script_validator",
            description="Valida scripts Python usando ast.parse",
            version="1.0.0",
            author="Recipe Manager Agent",
            category="validation",
            tags=["python", "validation", "syntax"],
            steps=[
                RecipeStep(
                    name="validate_syntax",
                    description="Valida sintaxe do script Python",
                    command="python",
                    args=["wiki/update/python_tools/complexity_analyzer.py"],
                    timeout=60,
                    required=True
                )
            ],
            dependencies=["ast"],
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )
        recipes.append(validator_recipe)
        
        # Receita para análise de código
        analyzer_recipe = Recipe(
            name="code_analyzer",
            description="Analisa complexidade e dependências de código Python",
            version="1.0.0",
            author="Recipe Manager Agent",
            category="analysis",
            tags=["python", "analysis", "complexity"],
            steps=[
                RecipeStep(
                    name="analyze_complexity",
                    description="Analisa complexidade do código",
                    command="python",
                    args=["wiki/update/python_tools/complexity_analyzer.py"],
                    timeout=120,
                    required=True
                ),
                RecipeStep(
                    name="map_dependencies",
                    description="Mapeia dependências do código",
                    command="python",
                    args=["wiki/update/python_tools/dependency_mapper.py"],
                    timeout=180,
                    required=False
                )
            ],
            dependencies=["ast", "json"],
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )
        recipes.append(analyzer_recipe)
        
        # Receita para backup
        backup_recipe = Recipe(
            name="backup_creator",
            description="Cria backup dos scripts Python",
            version="1.0.0",
            author="Recipe Manager Agent",
            category="backup",
            tags=["python", "backup", "files"],
            steps=[
                RecipeStep(
                    name="create_backup_dir",
                    description="Cria diretório de backup",
                    command="create",
                    args=["wiki/backup/python_scripts"],
                    timeout=30,
                    required=True
                ),
                RecipeStep(
                    name="copy_scripts",
                    description="Copia scripts Python para backup",
                    command="copy",
                    args=["wiki/update/python_tools", "wiki/backup/python_scripts"],
                    timeout=300,
                    required=True
                )
            ],
            dependencies=[],
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )
        recipes.append(backup_recipe)
        
        # Salvar receitas
        created_count = 0
        for recipe in recipes:
            if self.manager.create_recipe(recipe):
                created_count += 1
        
        return created_count

def main():
    """Função principal"""
    agent = RecipeManagerAgent()
    
    try:
        report = agent.execute_task_12_9()
        print(f"Task 12.9 concluída com sucesso!")
        print(f"Receitas criadas: {report['recipes_created']}")
        print(f"Total de receitas: {report['total_recipes']}")
        print(f"Taxa média de sucesso: {report['average_success_rate']:.1f}%")
        print(f"Categorias: {list(report['categories'].keys())}")
        
    except Exception as e:
        logger.error(f"Erro na execução da Task 12.9: {e}")
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 
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
- **Nome**: recipe_manager_agent
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

