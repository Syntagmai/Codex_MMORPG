from unicode_aliases import *
# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
MAX_ITEMS = 100

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: python_agent_system.py
Módulo de Destino: python.python_agent
Data de Migração: 2025-08-01 12:21:35

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import PythonagentModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Agent System
Agente especializado em desenvolvimento Python com verificação de erros e otimização automática
Integra arquivos base da pasta agente_python_base
"""

import os
import json
import re
import ast
from datetime import datetime

class PythonAgent:
    """Agente especializado em desenvolvimento Python"""
    
    def __init__(self, name: str = "Python", base_path: str = "wiki"):
        self.name = name
        self.base_path = Path(base_path)
        self.log_path = self.base_path / "log" / "python_agent"
        self.log_path.mkdir(parents=True, exist_ok=True)
        
        # Log de erros e melhorias
        self.error_log_file = self.log_path / "python_errors.json"
        self.improvement_log_file = self.log_path / "python_improvements.json"
        
        # Carrega logs existentes
        self.error_log = self.load_error_log()
        self.improvement_log = self.load_improvement_log()
        
        # Carrega padrões base da pasta agente_python_base
        self.base_patterns = self.load_base_patterns()
        
        # Padrões específicos do projeto
        self.project_patterns = {
            "file_header": {
                "template": """#!/usr/bin/env python3
# -*- coding: utf-8 -*-
\"\"\"
{description}
\"\"\"
""",
                "required": True
            },
            "imports": {
                "standard_order": [
                    "os", "sys", "json", "re", "datetime", "pathlib", "typing"
                ],
                "project_specific": [
                    "ast", "subprocess", "shutil", "tempfile"
                ]
            },
            "class_structure": {
                "docstring": True,
                "type_hints": True,
                "error_handling": True
            },
            "function_structure": {
                "docstring": True,
                "type_hints": True,
                "error_handling": True
            }
        }
        
        # Erros comuns detectados (expandindo os padrões base)
        self.common_errors = {
            "missing_encoding": {
                "pattern": r'open\([^)]*\)',
                "fix": "Adicionar encoding='utf-8'",
                "severity": "medium"
            },
            "missing_type_hints": {
                "pattern": r'def\s+\w+\s*\([^)]*\)\s*:',
                "fix": "Adicionar type hints",
                "severity": "low"
            },
            "hardcoded_paths": {
                "pattern": r'["\']/[^"\']*["\']',
                "fix": "Usar pathlib.Path",
                "severity": "medium"
            },
            "print_statements": {
                "pattern": r'print\s*\(',
                "fix": "Usar logging ou logger",
                "severity": "low"
            },
            "bare_except": {
                "pattern": r'except\s*:',
                "fix": "Especificar exceção",
                "severity": "high"
            },
            "unused_imports": {
                "pattern": r'import\s+\w+',
                "fix": "Remover imports não utilizados",
                "severity": "low"
            },
            "missing_import": {
                "pattern": r'NameError: name \'(\w+)\' is not defined',
                "fix": "Adicionar import necessário",
                "severity": "high"
            },
            "type_coercion": {
                "pattern": r'TypeError: expected str, got int',
                "fix": "Usar str() para conversão",
                "severity": "medium"
            }
        }
    
    def load_base_patterns(self) -> List[Dict[str, Any]]:
        """Carrega padrões base da pasta agente_python_base"""
        base_patterns_file = self.base_path / "agente_python_base" / "knowledge" / "py_patterns.json"
        
        if base_patterns_file.exists():
            try:
                with open(base_patterns_file, 'r', encoding='utf-8') as f:
                    patterns = json.load(f)
                print(f"✅ Carregados {len(patterns)} padrões base do agente Python")
                return patterns
            except Exception as e:
                print(f"⚠️ Erro ao carregar padrões base: {e}")
        
        return []
    
    def load_error_log(self) -> Dict[str, Any]:
        """Carrega log de erros"""
        if self.error_log_file.exists():
            try:
                with open(self.error_log_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        return {
            "errors": [],
            "statistics": {
                "total_errors": 0,
                "errors_by_type": {},
                "files_analyzed": 0
            },
            "last_updated": datetime.now().isoformat()
        }
    
    def load_improvement_log(self) -> Dict[str, Any]:
        """Carrega log de melhorias"""
        if self.improvement_log_file.exists():
            try:
                with open(self.improvement_log_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        return {
            "improvements": [],
            "statistics": {
                "total_improvements": 0,
                "improvements_by_type": {},
                "files_improved": 0
            },
            "last_updated": datetime.now().isoformat()
        }
    
    def save_error_log(self):
        """Salva log de erros"""
        self.error_log["last_updated"] = datetime.now().isoformat()
        with open(self.error_log_file, 'w', encoding='utf-8') as f:
            json.dump(self.error_log, f, indent=2, ensure_ascii=False)
    
    def save_improvement_log(self):
        """Salva log de melhorias"""
        self.improvement_log["last_updated"] = datetime.now().isoformat()
        with open(self.improvement_log_file, 'w', encoding='utf-8') as f:
            json.dump(self.improvement_log, f, indent=2, ensure_ascii=False)
    
    def analyze_python_file(self, file_path: str) -> Dict[str, Any]:
        """Analisa arquivo Python e detecta problemas"""
        print(f"🔍 Analisando arquivo Python: {file_path}")
        
        analysis_result = {
            "file_path": file_path,
            "timestamp": datetime.now().isoformat(),
            "errors": [],
            "warnings": [],
            "suggestions": [],
            "score": 100,
            "structure_analysis": {},
            "syntax_valid": True
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Análise sintática
            try:
                ast.parse(content)
                analysis_result["syntax_valid"] = True
            except SyntaxError as e:
                analysis_result["syntax_valid"] = False
                analysis_result["errors"].append({
                    "type": "syntax_error",
                    "line": e.lineno,
                    "message": str(e),
                    "severity": "high"
                })
                analysis_result["score"] -= 20
            
            # Verificar erros comuns
            for error_type, error_config in self.common_errors.items():
                matches = re.finditer(error_config["pattern"], content)
                for match in matches:
                    line_num = content[:match.start()].count('\n') + 1
                    analysis_result["errors"].append({
                        "type": error_type,
                        "line": line_num,
                        "message": error_config["fix"],
                        "severity": error_config["severity"],
                        "match": match.group()
                    })
                    
                    # Reduzir score baseado na severidade
                    if error_config["severity"] == "high":
                        analysis_result["score"] -= 10
                    elif error_config["severity"] == "medium":
                        analysis_result["score"] -= 5
                    else:
                        analysis_result["score"] -= 2
            
            # Verificar padrões base
            base_errors = self.check_base_patterns(content)
            analysis_result["errors"].extend(base_errors)
            
            # Análise de estrutura
            analysis_result["structure_analysis"] = self.analyze_structure(content)
            
            # Verificar padrões do projeto
            project_issues = self.check_project_patterns(content, file_path)
            analysis_result["warnings"].extend(project_issues)
            
            # Atualizar logs
            self.update_error_log(analysis_result)
            
        except Exception as e:
            analysis_result["errors"].append({
                "type": "analysis_error",
                "message": f"Erro ao analisar arquivo: {str(e)}",
                "severity": "high"
            })
            analysis_result["score"] -= 30
        
        return analysis_result
    
    def check_base_patterns(self, content: str) -> List[Dict[str, Any]]:
        """Verifica padrões base carregados da pasta agente_python_base"""
        errors = []
        
        for pattern in self.base_patterns:
            error_pattern = pattern.get("erro", "")
            if error_pattern and error_pattern in content:
                errors.append({
                    "type": "base_pattern",
                    "pattern": pattern.get("padrão", ""),
                    "message": pattern.get("correcao", ""),
                    "severity": "medium",
                    "tag": pattern.get("tag", "")
                })
        
        return errors
    
    def analyze_structure(self, content: str) -> Dict[str, Any]:
        """Analisa estrutura do código Python"""
        structure = {
            "classes": [],
            "functions": [],
            "imports": [],
            "lines_of_code": len(content.split('\n')),
            "has_main": False,
            "has_docstrings": False
        }
        
        try:
            tree = ast.parse(content)
            
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    structure["classes"].append({
                        "name": node.name,
                        "has_docstring": ast.get_docstring(node) is not None,
                        "methods": len([n for n in node.body if isinstance(n, ast.FunctionDef)])
                    })
                elif isinstance(node, ast.FunctionDef):
                    structure["functions"].append({
                        "name": node.name,
                        "has_docstring": ast.get_docstring(node) is not None,
                        "has_type_hints": self.has_type_hints(node)
                    })
                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        structure["imports"].append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        structure["imports"].append(node.module)
            
            # Verificar se tem main
            structure["has_main"] = "if __name__ == '__main__':" in content
            structure["has_docstrings"] = any(cls["has_docstring"] for cls in structure["classes"]) or \
                                        any(func["has_docstring"] for func in structure["functions"])
            
        except:
            pass
        
        return structure
    
    def has_type_hints(self, node: ast.FunctionDef) -> bool:
        """Verifica se função tem type hints"""
        return node.returns is not None or \
               any(arg.annotation is not None for arg in node.args.args)
    
    def check_project_patterns(self, content: str, file_path: str) -> List[Dict[str, Any]]:
        """Verifica padrões específicos do projeto"""
        warnings = []
        
        # Verificar header do arquivo
        if not content.startswith("#!/usr/bin/env python3"):
            warnings.append({
                "type": "missing_header",
                "message": "Arquivo deve começar com shebang Python",
                "severity": "medium"
            })
        
        # Verificar encoding
        if "# -*- coding: utf-8 -*-" not in content:
            warnings.append({
                "type": "missing_encoding",
                "message": "Adicionar encoding UTF-8",
                "severity": "medium"
            })
        
        # Verificar docstring do módulo
        if not re.search(r'"""[^"]*"""', content, re.DOTALL):
            warnings.append({
                "type": "missing_module_docstring",
                "message": "Adicionar docstring do módulo",
                "severity": "low"
            })
        
        return warnings
    
    def update_error_log(self, analysis_result: Dict[str, Any]):
        """Atualiza log de erros"""
        file_path = analysis_result["file_path"]
        
        # Adicionar erros ao log
        for error in analysis_result["errors"]:
            self.error_log["errors"].append({
                "file": file_path,
                "timestamp": analysis_result["timestamp"],
                "type": error["type"],
                "line": error.get("line", 0),
                "message": error["message"],
                "severity": error["severity"]
            })
            
            # Atualizar estatísticas
            error_type = error["type"]
            if error_type not in self.error_log["statistics"]["errors_by_type"]:
                self.error_log["statistics"]["errors_by_type"][error_type] = 0
            self.error_log["statistics"]["errors_by_type"][error_type] += 1
        
        self.error_log["statistics"]["total_errors"] += len(analysis_result["errors"])
        self.error_log["statistics"]["files_analyzed"] += 1
        
        self.save_error_log()
    
    def create_python_file(self, file_path: str, description: str, content: str = "") -> Dict[str, Any]:
        """Cria arquivo Python com estrutura otimizada"""
        print(f"🐍 Criando arquivo Python: {file_path}")
        
        # Gerar estrutura base
        file_structure = self.generate_file_structure(description, content)
        
        # Verificar se arquivo já existe
        if os.path.exists(file_path):
            return {
                "status": "error",
                "message": f"Arquivo já existe: {file_path}",
                "file_path": file_path
            }
        
        # Criar diretório se necessário
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Salvar arquivo
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(file_structure)
        
        # Analisar arquivo criado
        analysis = self.analyze_python_file(file_path)
        
        # Registrar melhoria
        self.improvement_log["improvements"].append({
            "file": file_path,
            "timestamp": datetime.now().isoformat(),
            "type": "file_created",
            "description": f"Arquivo Python criado com estrutura otimizada",
            "score": analysis["score"]
        })
        
        self.improvement_log["statistics"]["total_improvements"] += 1
        self.improvement_log["statistics"]["files_improved"] += 1
        self.save_improvement_log()
        
        return {
            "status": "success",
            "file_path": file_path,
            "analysis": analysis,
            "structure": file_structure
        }
    
    def generate_file_structure(self, description: str, content: str = "") -> str:
        """Gera estrutura de arquivo Python"""
        # Header padrão
        header = self.project_patterns["file_header"]["template"].format(
            description=description
        )
        
        # Imports padrão
        imports = []
        for module in self.project_patterns["imports"]["standard_order"]:
            imports.append(f"import {module}")
        
        imports_section = "\n".join(imports) + "\n\n"
        
        # Conteúdo principal
        if content:
            main_content = content
        else:
            main_content = """def main():
    \"\"\"
    Função principal
    \"\"\"
    print("Hello, World!")


if __name__ == "__main__":
    main()
"""
        
        return header + imports_section + main_content
    
    def optimize_python_file(self, file_path: str) -> Dict[str, Any]:
        """Otimiza arquivo Python existente"""
        print(f"⚡ Otimizando arquivo Python: {file_path}")
        
        # Analisar arquivo atual
        analysis = self.analyze_python_file(file_path)
        
        if not analysis["syntax_valid"]:
            return {
                "status": "error",
                "message": "Arquivo tem erros de sintaxe",
                "analysis": analysis
            }
        
        # Ler conteúdo atual
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Aplicar otimizações
        optimized_content = self.apply_optimizations(content)
        
        # Salvar versão otimizada
        backup_path = file_path + ".backup"
        os.rename(file_path, backup_path)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(optimized_content)
        
        # Analisar versão otimizada
        new_analysis = self.analyze_python_file(file_path)
        
        # Registrar melhoria
        improvement = {
            "file": file_path,
            "timestamp": datetime.now().isoformat(),
            "type": "file_optimized",
            "description": f"Arquivo otimizado - Score melhorou de {analysis['score']} para {new_analysis['score']}",
            "score_improvement": new_analysis["score"] - analysis["score"]
        }
        
        self.improvement_log["improvements"].append(improvement)
        self.improvement_log["statistics"]["total_improvements"] += 1
        self.save_improvement_log()
        
        return {
            "status": "success",
            "file_path": file_path,
            "backup_path": backup_path,
            "original_analysis": analysis,
            "optimized_analysis": new_analysis,
            "improvement": improvement
        }
    
    def apply_optimizations(self, content: str) -> str:
        """Aplica otimizações no código Python"""
        optimized = content
        
        # Adicionar encoding se não existir
        if "# -*- coding: utf-8 -*-" not in optimized:
            optimized = optimized.replace("#!/usr/bin/env python3", 
                                        "#!/usr/bin/env python3\n# -*- coding: utf-8 -*-")
        
        # Corrigir imports
        optimized = self.optimize_imports(optimized)
        
        # Adicionar type hints básicos
        optimized = self.add_basic_type_hints(optimized)
        
        # Corrigir encoding em open()
        optimized = re.sub(r'open\(([^)]+)\)', r'open(\1, encoding="utf-8")', optimized)
        
        return optimized
    
    def optimize_imports(self, content: str) -> str:
        """Otimiza imports do arquivo"""
        # Extrair imports existentes
        import_lines = []
        other_lines = []
        
        lines = content.split('\n')
        in_imports = True
        
        for line in lines:
            if line.strip().startswith(('import ', 'from ')):
                import_lines.append(line)
            elif line.strip() == '' and in_imports:
                continue
            else:
                in_imports = False
                other_lines.append(line)
        
        # Organizar imports
        standard_imports = []
        project_imports = []
        other_imports = []
        
        for line in import_lines:
            if any(module in line for module in self.project_patterns["imports"]["standard_order"]):
                standard_imports.append(line)
            elif any(module in line for module in self.project_patterns["imports"]["project_specific"]):
                project_imports.append(line)
            else:
                other_imports.append(line)
        
        # Reconstruir conteúdo
        optimized_imports = standard_imports + project_imports + other_imports
        return '\n'.join(optimized_imports + [''] + other_lines)
    
    def add_basic_type_hints(self, content: str) -> str:
        """Adiciona type hints básicos"""
        # Adicionar typing import se necessário
        if "from typing import" not in content and "import typing" not in content:
            content = content.replace("import json", "import json\nfrom typing import Dict, List, Any")
        
        return content
    
    def scan_project_python_files(self) -> Dict[str, Any]:
        """Escaneia todos os arquivos Python do projeto"""
        print(f"🔍 Escaneando arquivos Python do projeto")
        
        python_files = []
        for root, dirs, files in os.walk(self.base_path):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    python_files.append(file_path)
        
        scan_result = {
            "total_files": len(python_files),
            "files_analyzed": 0,
            "total_errors": 0,
            "total_warnings": 0,
            "average_score": 0,
            "files_by_score": {
                "excellent": [],  # 90-100
                "good": [],      # 70-89
                "fair": [],      # 50-69
                "poor": []       # 0-49
            },
            "analysis_results": []
        }
        
        total_score = 0
        
        for file_path in python_files:
            analysis = self.analyze_python_file(file_path)
            scan_result["analysis_results"].append(analysis)
            scan_result["files_analyzed"] += 1
            scan_result["total_errors"] += len(analysis["errors"])
            scan_result["total_warnings"] += len(analysis["warnings"])
            
            total_score += analysis["score"]
            
            # Categorizar por score
            if analysis["score"] >= 90:
                scan_result["files_by_score"]["excellent"].append(file_path)
            elif analysis["score"] >= 70:
                scan_result["files_by_score"]["good"].append(file_path)
            elif analysis["score"] >= 50:
                scan_result["files_by_score"]["fair"].append(file_path)
            else:
                scan_result["files_by_score"]["poor"].append(file_path)
        
        if scan_result["files_analyzed"] > 0:
            scan_result["average_score"] = total_score / scan_result["files_analyzed"]
        
        return scan_result
    
    def generate_report(self) -> str:
        """Gera relatório completo do agente Python"""
        print(f"📋 Gerando relatório do agente Python")
        
        # Escanear arquivos do projeto
        scan_result = self.scan_project_python_files()
        
        report = f"""# Relatório do Agente Python - {self.name}

**Gerado**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Arquivos Python no Projeto**: {scan_result['total_files']}

## 📊 Estatísticas Gerais

- **Arquivos Analisados**: {scan_result['files_analyzed']}
- **Score Médio**: {scan_result['average_score']:.1f}/100
- **Total de Erros**: {scan_result['total_errors']}
- **Total de Avisos**: {scan_result['total_warnings']}

## 📈 Distribuição por Score

- **Excelente (90-100)**: {len(scan_result['files_by_score']['excellent'])} arquivos
- **Bom (70-89)**: {len(scan_result['files_by_score']['good'])} arquivos
- **Regular (50-69)**: {len(scan_result['files_by_score']['fair'])} arquivos
- **Ruim (0-49)**: {len(scan_result['files_by_score']['poor'])} arquivos

## 🐛 Erros Mais Comuns

"""
        
        # Estatísticas de erros
        error_stats = self.error_log["statistics"]["errors_by_type"]
        for error_type, count in sorted(error_stats.items(), key=lambda x: x[1], reverse=True):
            report += f"- **{error_type}**: {count} ocorrências\n"
        
        report += f"""
## 🚀 Melhorias Implementadas

- **Total de Melhorias**: {self.improvement_log['statistics']['total_improvements']}
- **Arquivos Melhorados**: {self.improvement_log['statistics']['files_improved']}

## 📁 Arquivos que Precisam de Atenção

"""
        
        # Listar arquivos com problemas
        for analysis in scan_result["analysis_results"]:
            if analysis["score"] < 70:
                report += f"- **{analysis['file_path']}** (Score: {analysis['score']})\n"
                for error in analysis["errors"][:3]:  # Mostrar apenas 3 primeiros erros
                    report += f"  - {error['message']}\n"
        
        report += f"""
## 💡 Recomendações

1. **Corrigir erros de sintaxe** em arquivos com score baixo
2. **Adicionar type hints** para melhorar legibilidade
3. **Padronizar imports** seguindo ordem estabelecida
4. **Adicionar docstrings** em classes e funções
5. **Usar encoding UTF-8** em todas as operações de arquivo

## 🔧 Funcionalidades do Agente

- ✅ **Análise automática** de arquivos Python
- ✅ **Detecção de erros** comuns
- ✅ **Criação de arquivos** com estrutura otimizada
- ✅ **Otimização automática** de código existente
- ✅ **Log de erros** e melhorias
- ✅ **Relatórios detalhados** de qualidade
- ✅ **Integração com padrões base** da pasta agente_python_base

## 📚 Padrões Base Integrados

- **Padrões carregados**: {len(self.base_patterns)}
- **Fonte**: wiki/agente_python_base/knowledge/py_patterns.json
- **Funcionalidade**: Detecção automática de erros comuns

---
*Relatório gerado automaticamente pelo Agente Python*
"""
        
        return report

def main():
    """Função principal para teste"""
    print("🐍 TESTE DO AGENTE PYTHON")
    print("=" * 50)
    
    # Inicializar agente
    agent = PythonAgent("Python Agent")
    
    # Testar análise de arquivo
    test_file = "task_automation_system.py"
    if os.path.exists(test_file):
        print(f"\n🔍 Analisando arquivo de teste: {test_file}")
        analysis = agent.analyze_python_file(test_file)
        print(f"✅ Score: {analysis['score']}/100")
        print(f"✅ Erros: {len(analysis['errors'])}")
        print(f"✅ Avisos: {len(analysis['warnings'])}")
    
    # Gerar relatório
    print(f"\n📋 Gerando relatório completo...")
    report = agent.generate_report()
    
    # Salvar relatório
    report_file = agent.log_path / "python_agent_report.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"✅ Relatório salvo em: {report_file}")
    print(f"✅ Logs salvos em: {agent.log_path}")

if __name__ == "__main__":
    main() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = PythonagentModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script python_agent_system.py executado com sucesso via módulo python.python_agent")
    else:
        print(f"❌ Erro na execução do script python_agent_system.py via módulo python.python_agent")
