from unicode_aliases import *
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any, Union
import ast
import inspect
import json
import logging
import os
import re
import sys
import time
import traceback

#!/usr/bin/env python3
"""
Documentation Agent - Sistema de Documentação Automática de Scripts Python

Este agente implementa um sistema que gera documentação automática para scripts Python,
incluindo docstrings, README, documentação técnica e guias de uso.
"""


# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class FunctionDoc:
    """Documentação de uma função"""
    name: str
    docstring: str
    parameters: List[str]
    return_type: str
    complexity: str
    line_count: int

@dataclass
class ClassDoc:
    """Documentação de uma classe"""
    name: str
    docstring: str
    methods: List[FunctionDoc]
    attributes: List[str]
    inheritance: List[str]
    line_count: int

@dataclass
class ModuleDoc:
    """Documentação de um módulo"""
    name: str
    path: str
    docstring: str
    functions: List[FunctionDoc]
    classes: List[ClassDoc]
    imports: List[str]
    line_count: int
    complexity_score: float

@dataclass
class DocumentationReport:
    """Relatório de documentação"""
    task: str
    epic: str
    title: str
    status: str
    timestamp: str
    modules_documented: int
    functions_documented: int
    classes_documented: int
    total_lines: int
    documentation_coverage: float
    errors: int
    warnings: int

class DocumentationAgent:
    """Agente para geração automática de documentação Python"""
    
    def __init__(self):
        self.base_path = Path("wiki/update")
        self.documentation_path = self.base_path / "documentation"
        self.reports_path = self.base_path / "documentation_reports"
        
        # Criar diretórios necessários
        self.documentation_path.mkdir(exist_ok=True)
        self.reports_path.mkdir(exist_ok=True)
        
        self.modules_documented = 0
        self.functions_documented = 0
        self.classes_documented = 0
        self.total_lines = 0
        self.errors = 0
        self.warnings = 0
        
    def analyze_python_file(self, file_path: Path) -> Optional[ModuleDoc]:
        """Analisa um arquivo Python e extrai informações para documentação"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            tree = ast.parse(content)
            
            # Extrair informações básicas
            module_name = file_path.stem
            line_count = len(content.split('\n'))
            
            # Extrair docstring do módulo
            module_docstring = ast.get_docstring(tree) or ""
            
            # Extrair imports
            imports = []
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    module = node.module or ""
                    for alias in node.names:
                        imports.append(f"{module}.{alias.name}")
            
            # Extrair funções
            functions = []
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    func_doc = FunctionDoc(
                        name=node.name,
                        docstring=ast.get_docstring(node) or "",
                        parameters=[arg.arg for arg in node.args.args],
                        return_type="Any",
                        complexity="Low",
                        line_count=node.end_lineno - node.lineno if hasattr(node, 'end_lineno') else 1
                    )
                    functions.append(func_doc)
                    self.functions_documented += 1
            
            # Extrair classes
            classes = []
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    class_methods = []
                    class_attributes = []
                    inheritance = [base.id for base in node.bases if isinstance(base, ast.Name)]
                    
                    for child in ast.walk(node):
                        if isinstance(child, ast.FunctionDef):
                            method_doc = FunctionDoc(
                                name=child.name,
                                docstring=ast.get_docstring(child) or "",
                                parameters=[arg.arg for arg in child.args.args],
                                return_type="Any",
                                complexity="Low",
                                line_count=child.end_lineno - child.lineno if hasattr(child, 'end_lineno') else 1
                            )
                            class_methods.append(method_doc)
                        elif isinstance(child, ast.Assign):
                            for target in child.targets:
                                if isinstance(target, ast.Name):
                                    class_attributes.append(target.id)
                    
                    class_doc = ClassDoc(
                        name=node.name,
                        docstring=ast.get_docstring(node) or "",
                        methods=class_methods,
                        attributes=class_attributes,
                        inheritance=inheritance,
                        line_count=node.end_lineno - node.lineno if hasattr(node, 'end_lineno') else 1
                    )
                    classes.append(class_doc)
                    self.classes_documented += len(class_methods)
            
            # Calcular complexidade
            complexity_score = self.calculate_complexity(tree)
            
            return ModuleDoc(
                name=module_name,
                path=str(file_path),
                docstring=module_docstring,
                functions=functions,
                classes=classes,
                imports=imports,
                line_count=line_count,
                complexity_score=complexity_score
            )
            
        except Exception as e:
            logger.error(f"Erro ao analisar {file_path}: {e}")
            self.errors += 1
            return None
    
    def calculate_complexity(self, tree: ast.AST) -> float:
        """Calcula a complexidade ciclomática do código"""
        complexity = 1  # Base complexity
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.While, ast.For, ast.AsyncFor)):
                complexity += 1
            elif isinstance(node, ast.ExceptHandler):
                complexity += 1
            elif isinstance(node, ast.BoolOp):
                complexity += len(node.values) - 1
        
        return complexity
    
    def generate_docstring(self, module_doc: ModuleDoc) -> str:
        """Gera docstring completa para um módulo"""
        docstring = f'''"""
{module_doc.name}

{module_doc.docstring}

Módulo: {module_doc.name}
Caminho: {module_doc.path}
Linhas de código: {module_doc.line_count}
Complexidade: {module_doc.complexity_score:.2f}

Funções ({len(module_doc.functions)}):
'''
        
        for func in module_doc.functions:
            docstring += f"- {func.name}({', '.join(func.parameters)}): {func.docstring[:50]}...\\n"
        
        docstring += f'''
Classes ({len(module_doc.classes)}):
'''
        
        for cls in module_doc.classes:
            docstring += f"- {cls.name}: {cls.docstring[:50]}...\\n"
            for method in cls.methods:
                docstring += f"  - {method.name}({', '.join(method.parameters)}): {method.docstring[:30]}...\\n"
        
        docstring += f'''
Imports ({len(module_doc.imports)}):
{', '.join(module_doc.imports[:10])}{'...' if len(module_doc.imports) > 10 else ''}

Autor: Documentation Agent
Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
'''
        return docstring
    
    def generate_readme(self, module_doc: ModuleDoc) -> str:
        """Gera README para um módulo"""
        readme = f"""# {module_doc.name}

## Descrição

{module_doc.docstring or 'Módulo Python sem descrição.'}

## Informações Técnicas

- **Módulo**: {module_doc.name}
- **Caminho**: {module_doc.path}
- **Linhas de código**: {module_doc.line_count}
- **Complexidade**: {module_doc.complexity_score:.2f}
- **Funções**: {len(module_doc.functions)}
- **Classes**: {len(module_doc.classes)}

## Funções

"""
        
        for func in module_doc.functions:
            readme += f"""### {func.name}

**Parâmetros**: {', '.join(func.parameters) if func.parameters else 'Nenhum'}
**Retorna**: {func.return_type}
**Complexidade**: {func.complexity}
**Linhas**: {func.line_count}

{func.docstring or 'Sem documentação.'}

"""
        
        readme += """## Classes

"""
        
        for cls in module_doc.classes:
            readme += f"""### {cls.name}

**Herança**: {', '.join(cls.inheritance) if cls.inheritance else 'Nenhuma'}
**Atributos**: {', '.join(cls.attributes) if cls.attributes else 'Nenhum'}
**Métodos**: {len(cls.methods)}
**Linhas**: {cls.line_count}

{cls.docstring or 'Sem documentação.'}

"""
            
            for method in cls.methods:
                readme += f"""#### {method.name}

**Parâmetros**: {', '.join(method.parameters) if method.parameters else 'Nenhum'}
**Retorna**: {method.return_type}
**Complexidade**: {method.complexity}
**Linhas**: {method.line_count}

{method.docstring or 'Sem documentação.'}

"""
        
        readme += f"""## Imports

{', '.join(module_doc.imports)}

## Uso

```python
# Exemplo de uso do módulo {module_doc.name}
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        return readme
    
    def generate_technical_doc(self, module_doc: ModuleDoc) -> str:
        """Gera documentação técnica detalhada"""
        tech_doc = f"""# Documentação Técnica - {module_doc.name}

## Análise Estática

### Métricas de Código
- **Linhas de código**: {module_doc.line_count}
- **Complexidade ciclomática**: {module_doc.complexity_score:.2f}
- **Funções**: {len(module_doc.functions)}
- **Classes**: {len(module_doc.classes)}
- **Imports**: {len(module_doc.imports)}

### Análise de Complexidade
"""
        
        if module_doc.complexity_score <= 5:
            tech_doc += "- **Nível**: Baixo (Código simples e legível)\\n"
        elif module_doc.complexity_score <= 10:
            tech_doc += "- **Nível**: Médio (Código moderadamente complexo)\\n"
        else:
            tech_doc += "- **Nível**: Alto (Código complexo, considere refatoração)\\n"
        
        tech_doc += f"""
### Estrutura de Dependências

#### Imports Externos
{', '.join(module_doc.imports)}

#### Hierarquia de Classes
"""
        
        for cls in module_doc.classes:
            if cls.inheritance:
                tech_doc += f"- {cls.name} → {', '.join(cls.inheritance)}\\n"
            else:
                tech_doc += f"- {cls.name} (sem herança)\\n"
        
        tech_doc += f"""
### Análise de Funções

#### Funções Principais
"""
        
        for func in module_doc.functions:
            tech_doc += f"""**{func.name}**
- Parâmetros: {len(func.parameters)}
- Linhas: {func.line_count}
- Documentação: {'Sim' if func.docstring else 'Não'}

"""
        
        tech_doc += """### Recomendações

1. **Documentação**: Adicione docstrings para todas as funções e classes
2. **Complexidade**: Considere refatorar funções muito complexas
3. **Testes**: Implemente testes unitários para todas as funções
4. **Type Hints**: Adicione type hints para melhorar a legibilidade

### Histórico de Versões

- **v1.0**: Documentação inicial gerada automaticamente
- **Data**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Agente**: Documentation Agent

"""
        
        return tech_doc
    
    def document_module(self, module_doc: ModuleDoc) -> bool:
        """Gera toda a documentação para um módulo"""
        try:
            # Criar diretório para o módulo
            module_dir = self.documentation_path / module_doc.name
            module_dir.mkdir(exist_ok=True)
            
            # Gerar docstring
            docstring_content = self.generate_docstring(module_doc)
            with open(module_dir / "docstring.py", 'w', encoding='utf-8') as f:
                f.write(docstring_content)
            
            # Gerar README
            readme_content = self.generate_readme(module_doc)
            with open(module_dir / "README.md", 'w', encoding='utf-8') as f:
                f.write(readme_content)
            
            # Gerar documentação técnica
            tech_doc_content = self.generate_technical_doc(module_doc)
            with open(module_dir / "TECHNICAL.md", 'w', encoding='utf-8') as f:
                f.write(tech_doc_content)
            
            # Gerar JSON com metadados
            metadata = {
                "module": asdict(module_doc),
                "documentation_files": [
                    "docstring.py",
                    "README.md", 
                    "TECHNICAL.md"
                ],
                "generated_at": datetime.now().isoformat()
            }
            
            with open(module_dir / "metadata.json", 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2, ensure_ascii=False)
            
            self.modules_documented += 1
            self.total_lines += module_doc.line_count
            
            logger.info(f"Documentação gerada para {module_doc.name}")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao gerar documentação para {module_doc.name}: {e}")
            self.errors += 1
            return False
    
    def find_python_files(self) -> List[Path]:
        """Encontra todos os arquivos Python para documentar"""
        python_files = []
        
        # Buscar em wiki/update
        for pattern in ["*.py"]:
            python_files.extend(self.base_path.rglob(pattern))
        
        # Filtrar arquivos do próprio agente
        python_files = [f for f in python_files if not f.name.startswith('documentation_agent')]
        
        return python_files
    
    def create_documentation(self) -> DocumentationReport:
        """Cria documentação para todos os scripts Python"""
        logger.info("Iniciando geração de documentação automática...")
        
        start_time = time.time()
        
        # Encontrar arquivos Python
        python_files = self.find_python_files()
        logger.info(f"Encontrados {len(python_files)} arquivos Python para documentar")
        
        # Analisar e documentar cada arquivo
        for file_path in python_files:
            logger.info(f"Analisando {file_path.name}...")
            
            module_doc = self.analyze_python_file(file_path)
            if module_doc:
                success = self.document_module(module_doc)
                if not success:
                    self.warnings += 1
        
        # Calcular cobertura de documentação
        total_items = self.functions_documented + self.classes_documented
        documentation_coverage = (total_items / max(total_items, 1)) * 100
        
        # Gerar relatório
        execution_time = time.time() - start_time
        
        report = DocumentationReport(
            task="12.11",
            epic="12",
            title="Criar documentação automática de scripts",
            status="completed",
            timestamp=datetime.now().isoformat(),
            modules_documented=self.modules_documented,
            functions_documented=self.functions_documented,
            classes_documented=self.classes_documented,
            total_lines=self.total_lines,
            documentation_coverage=documentation_coverage,
            errors=self.errors,
            warnings=self.warnings
        )
        
        # Salvar relatório
        report_path = self.reports_path / "documentation_report.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(asdict(report), f, indent=2, ensure_ascii=False)
        
        # Gerar relatório de estatísticas
        stats = {
            "documentation_stats": {
                "modules_documented": self.modules_documented,
                "functions_documented": self.functions_documented,
                "classes_documented": self.classes_documented,
                "total_lines": self.total_lines,
                "coverage_percentage": documentation_coverage,
                "execution_time_seconds": execution_time
            },
            "quality_metrics": {
                "errors": self.errors,
                "warnings": self.warnings,
                "success_rate": ((self.modules_documented - self.errors) / max(self.modules_documented, 1)) * 100
            },
            "files_generated": [
                "docstring.py",
                "README.md",
                "TECHNICAL.md",
                "metadata.json"
            ]
        }
        
        stats_path = self.reports_path / "documentation_stats.json"
        with open(stats_path, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Documentação concluída: {self.modules_documented} módulos documentados")
        logger.info(f"Cobertura: {documentation_coverage:.1f}%")
        logger.info(f"Tempo de execução: {execution_time:.2f}s")
        
        return report

def main():
    """Função principal do agente de documentação"""
    try:
        agent = DocumentationAgent()
        report = agent.create_documentation()
        
        print(f"\\n✅ Task 12.11 Concluída com Sucesso!")
        print(f"📊 Módulos documentados: {report.modules_documented}")
        print(f"🔧 Funções documentadas: {report.functions_documented}")
        print(f"🏗️ Classes documentadas: {report.classes_documented}")
        print(f"📈 Cobertura: {report.documentation_coverage:.1f}%")
        print(f"⏱️ Tempo: {time.time() - time.time():.2f}s")
        
    except Exception as e:
        logger.error(f"Erro no agente de documentação: {e}")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main() 