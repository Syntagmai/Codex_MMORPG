#!/usr/bin/env python3
"""
Python Correction Agent - Epic 18 Task 18.2
Corrige erros de sintaxe Python e imports obsoletos identificados na Epic 17
"""
import os
import json
import re
import shutil
import ast
from datetime import datetime
from pathlib import Path

class PythonCorrectionAgent:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.audit_reports_dir = self.project_root / "wiki" / "docs" / "audit_reports"
        self.python_report = self.audit_reports_dir / "python_audit_report.json"
        self.correction_report = {
            "timestamp": datetime.now().isoformat(),
            "syntax_errors_fixed": [],
            "imports_fixed": [],
            "unicode_aliases_fixed": [],
            "files_modified": [],
            "backups_created": [],
            "errors_encountered": [],
            "total_fixes": 0
        }
    
    def load_python_audit(self):
        """Carrega o relatório de auditoria Python"""
        try:
            with open(self.python_report, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Erro ao carregar relatório Python: {e}")
            return None
    
    def backup_file(self, file_path):
        """Cria backup de um arquivo antes de modificá-lo"""
        try:
            backup_path = str(file_path) + ".backup"
            shutil.copy2(file_path, backup_path)
            self.correction_report["backups_created"].append(backup_path)
            return True
        except Exception as e:
            print(f"Erro ao criar backup de {file_path}: {e}")
            return False
    
    def fix_unicode_aliases_imports(self, file_path):
        """Corrige imports obsoletos de unicode_aliases"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Remove imports obsoletos de unicode_aliases
            content = re.sub(r'from\s+unicodedata\s+import\s+unicode_aliases\s*\n?', '', content)
            content = re.sub(r'import\s+unicodedata\s*\n?', '', content)
            
            # Remove linhas vazias duplicadas
            content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
            
            # Remove imports vazios
            content = re.sub(r'^\s*import\s*\n', '', content, flags=re.MULTILINE)
            
            if content != original_content:
                self.backup_file(file_path)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                self.correction_report["unicode_aliases_fixed"].append({
                    "file": file_path,
                    "fix_type": "unicode_aliases_removal",
                    "description": "Removido import obsoleto unicode_aliases"
                })
                
                self.correction_report["files_modified"].append(file_path)
                return True
            
            return False
            
        except Exception as e:
            self.correction_report["errors_encountered"].append({
                "file": file_path,
                "error": str(e),
                "fix_type": "unicode_aliases"
            })
            return False
    
    def fix_syntax_errors(self, file_path, syntax_errors):
        """Corrige erros de sintaxe específicos"""
        fixes_applied = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            for error in syntax_errors:
                error_type = error.get('error_type', '')
                line_number = error.get('line_number', 0)
                description = error.get('description', '')
                
                # Correções específicas por tipo de erro
                if "IndentationError" in error_type:
                    # Corrige problemas de indentação
                    lines = content.split('\n')
                    if line_number <= len(lines):
                        # Ajusta indentação para 4 espaços
                        line = lines[line_number - 1]
                        if line.strip():  # Se a linha não está vazia
                            # Remove espaços/tabs e adiciona indentação correta
                            stripped = line.lstrip()
                            if stripped:
                                # Calcula indentação baseada no contexto
                                indent_level = (line_number - 1) // 4  # Aproximação
                                new_indent = '    ' * indent_level
                                lines[line_number - 1] = new_indent + stripped
                        
                        content = '\n'.join(lines)
                
                elif "SyntaxError" in error_type:
                    # Corrige erros de sintaxe comuns
                    if "invalid syntax" in description.lower():
                        # Remove caracteres inválidos
                        content = re.sub(r'[^\x00-\x7F]+', '', content)  # Remove caracteres não-ASCII
                        content = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', content)  # Remove caracteres de controle
                
                elif "ImportError" in error_type:
                    # Corrige imports quebrados
                    if "No module named" in description:
                        # Remove imports quebrados
                        module_name = re.search(r"No module named '([^']+)'", description)
                        if module_name:
                            module = module_name.group(1)
                            content = re.sub(rf'import\s+{module}\s*\n?', '', content)
                            content = re.sub(rf'from\s+{module}\s+import.*\n?', '', content)
                
                elif "NameError" in error_type:
                    # Corrige variáveis não definidas
                    if "name" in description and "is not defined" in description:
                        # Adiciona imports básicos se necessário
                        if "os" not in content and "import os" not in content:
                            content = "import os\n" + content
                        if "json" not in content and "import json" not in content:
                            content = "import json\n" + content
                
                elif "AttributeError" in error_type:
                    # Corrige erros de atributo
                    if "pathlib" in description and "WindowsPath" in description:
                        # Corrige problemas específicos do pathlib
                        content = re.sub(r'pathlib\._local\.WindowsPath', 'pathlib.WindowsPath', content)
                        content = re.sub(r'\._str_normcase_cached', '', content)
                        content = re.sub(r'\._str', '', content)
            
            if content != original_content:
                self.backup_file(file_path)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                fixes_applied.append({
                    "file": file_path,
                    "error_type": error_type,
                    "description": description,
                    "fix_applied": "Syntax error corrected"
                })
                
                self.correction_report["files_modified"].append(file_path)
            
        except Exception as e:
            self.correction_report["errors_encountered"].append({
                "file": file_path,
                "error": str(e),
                "fix_type": "syntax_error"
            })
        
        self.correction_report["syntax_errors_fixed"].extend(fixes_applied)
        return fixes_applied
    
    def fix_common_python_issues(self, file_path):
        """Corrige problemas comuns de Python"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Corrige encoding
            if not content.startswith('#!'):
                content = '#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n' + content
            
            # Corrige imports duplicados
            lines = content.split('\n')
            import_lines = []
            other_lines = []
            
            for line in lines:
                if line.strip().startswith(('import ', 'from ')):
                    if line.strip() not in [l.strip() for l in import_lines]:
                        import_lines.append(line)
                else:
                    other_lines.append(line)
            
            # Reorganiza imports
            content = '\n'.join(import_lines) + '\n\n' + '\n'.join(other_lines)
            
            # Remove linhas vazias duplicadas
            content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
            
            # Corrige problemas de encoding
            content = content.replace('\r\n', '\n')  # Normaliza line endings
            
            if content != original_content:
                self.backup_file(file_path)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                self.correction_report["files_modified"].append(file_path)
                return True
            
            return False
            
        except Exception as e:
            self.correction_report["errors_encountered"].append({
                "file": file_path,
                "error": str(e),
                "fix_type": "common_issues"
            })
            return False
    
    def validate_python_file(self, file_path):
        """Valida se o arquivo Python está sintaticamente correto"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Tenta compilar o código
            ast.parse(content)
            return True
        except SyntaxError as e:
            return False
        except Exception as e:
            return False
    
    def create_python_guidelines(self):
        """Cria diretrizes de Python"""
        guidelines = '''# Diretrizes de Python - Codex MMORPG

## 1. Imports e Dependências
- Sempre usar imports absolutos quando possível
- Evitar imports circulares
- Usar imports específicos: `from module import function`
- Remover imports não utilizados
- Não usar imports obsoletos (unicode_aliases, etc.)

## 2. Sintaxe e Estrutura
- Usar indentação de 4 espaços (não tabs)
- Seguir PEP 8 para estilo de código
- Usar docstrings para funções e classes
- Manter linhas com máximo de 79 caracteres
- Usar nomes descritivos para variáveis e funções

## 3. Tratamento de Erros
- Usar try/except para tratamento de exceções
- Especificar tipos de exceção quando possível
- Evitar except genérico sem especificar exceção
- Usar logging para registrar erros

## 4. Performance
- Evitar loops desnecessários
- Usar list comprehensions quando apropriado
- Otimizar imports e dependências
- Usar geradores para grandes conjuntos de dados

## 5. Segurança
- Validar todas as entradas de usuário
- Usar prepared statements para SQL
- Evitar eval() e exec() com entrada do usuário
- Sanitizar dados antes de processar

## 6. Compatibilidade
- Usar Python 3.6+ features
- Evitar código específico de versão
- Testar em múltiplas versões do Python
- Usar type hints quando possível

## 7. Documentação
- Documentar funções e classes
- Usar docstrings no formato Google ou NumPy
- Manter README atualizado
- Documentar APIs e interfaces

## 8. Testes
- Escrever testes unitários
- Usar pytest para testes
- Manter cobertura de código alta
- Testar casos de erro e edge cases
'''
        
        guidelines_file = self.project_root / "wiki" / "docs" / "python_guidelines.md"
        with open(guidelines_file, 'w', encoding='utf-8') as f:
            f.write(guidelines)
        
        self.correction_report["files_modified"].append(str(guidelines_file))
        return str(guidelines_file)
    
    def create_correction_report(self):
        """Cria relatório de correção"""
        report_file = self.audit_reports_dir / "python_correction_report.json"
        
        # Calcula estatísticas
        total_syntax_fixes = len(self.correction_report["syntax_errors_fixed"])
        total_import_fixes = len(self.correction_report["unicode_aliases_fixed"])
        total_files_modified = len(set(self.correction_report["files_modified"]))
        total_errors = len(self.correction_report["errors_encountered"])
        
        self.correction_report["total_fixes"] = total_syntax_fixes + total_import_fixes
        self.correction_report["statistics"] = {
            "syntax_errors_fixed": total_syntax_fixes,
            "imports_fixed": total_import_fixes,
            "files_modified": total_files_modified,
            "errors_encountered": total_errors
        }
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(self.correction_report, f, indent=2, ensure_ascii=False)
        
        return str(report_file)
    
    def run_python_correction(self):
        """Executa correção Python completa"""
        print("🐍 Iniciando correção de erros de sintaxe Python...")
        
        # Carrega relatório Python
        python_data = self.load_python_audit()
        if not python_data:
            print("❌ Não foi possível carregar relatório Python")
            return False
        
        print(f"📊 Erros de sintaxe identificados: {len(python_data.get('syntax_errors', []))}")
        print(f"📊 Imports obsoletos identificados: {len(python_data.get('obsolete_imports', []))}")
        
        # Corrige imports obsoletos
        print("🔧 Corrigindo imports obsoletos...")
        obsolete_imports = python_data.get('obsolete_imports', [])
        for import_info in obsolete_imports:
            file_path = import_info.get('file_path', '')
            if file_path and os.path.exists(file_path):
                self.fix_unicode_aliases_imports(file_path)
        
        # Corrige erros de sintaxe
        print("🔧 Corrigindo erros de sintaxe...")
        syntax_errors = python_data.get('syntax_errors', [])
        for error in syntax_errors:
            file_path = error.get('file_path', '')
            if file_path and os.path.exists(file_path):
                self.fix_syntax_errors(file_path, [error])
        
        # Corrige problemas comuns
        print("🔧 Aplicando correções comuns...")
        python_files = python_data.get('python_files', [])
        for file_info in python_files:
            file_path = file_info.get('file_path', '')
            if file_path and os.path.exists(file_path):
                self.fix_common_python_issues(file_path)
        
        # Valida arquivos corrigidos
        print("✅ Validando arquivos corrigidos...")
        valid_files = 0
        total_files = 0
        
        for file_path in set(self.correction_report["files_modified"]):
            if file_path.endswith('.py'):
                total_files += 1
                if self.validate_python_file(file_path):
                    valid_files += 1
        
        # Cria diretrizes
        print("📋 Criando diretrizes de Python...")
        guidelines_file = self.create_python_guidelines()
        
        # Cria relatório
        report_file = self.create_correction_report()
        
        # Estatísticas finais
        print(f"\n✅ Correção Python concluída!")
        print(f"📊 Arquivos modificados: {len(set(self.correction_report['files_modified']))}")
        print(f"🔧 Erros de sintaxe corrigidos: {len(self.correction_report['syntax_errors_fixed'])}")
        print(f"🔧 Imports obsoletos corrigidos: {len(self.correction_report['unicode_aliases_fixed'])}")
        print(f"✅ Arquivos válidos: {valid_files}/{total_files}")
        print(f"❌ Erros encontrados: {len(self.correction_report['errors_encountered'])}")
        print(f"📄 Relatório salvo em: {report_file}")
        print(f"📋 Diretrizes: {guidelines_file}")
        
        return True

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        project_root = sys.argv[1]
    else:
        project_root = "."
    
    agent = PythonCorrectionAgent(project_root)
    result = agent.run_python_correction() 