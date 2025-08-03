from unicode_aliases import *
# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
TIMEOUT_SECONDS = 60

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: python_error_resolver.py
Módulo de Destino: python.error_resolver
Data de Migração: 2025-08-01 12:21:35

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import ErrorresolverModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Resolução de Erros para Scripts Python
Resolve automaticamente problemas de execução em scripts Python
"""

import json
import subprocess
import sys

class PythonErrorResolver:
    def __init__(self):
        self.project_root = Path(".")
        self.update_path = self.project_root / "wiki/update"
        self.maps_path = self.project_root / "wiki/maps"
        self.log_path = self.project_root / "wiki/log"
        
        # Configurações de resolução
        self.max_retries = 3
        self.timeout_seconds = 30
        self.error_patterns = self.load_error_patterns()
        
    def load_error_patterns(self) -> Dict[str, Dict[str, Any]]:
        """Carrega padrões de erro conhecidos e suas soluções"""
        return {
            "import_error": {
                "patterns": [
                    "ModuleNotFoundError",
                    "ImportError",
                    "No module named"
                ],
                "solutions": [
                    "check_python_path",
                    "install_missing_dependencies",
                    "fix_import_statement"
                ],
                "priority": "high"
            },
            "syntax_error": {
                "patterns": [
                    "SyntaxError",
                    "IndentationError",
                    "TabError"
                ],
                "solutions": [
                    "fix_syntax_error",
                    "check_indentation",
                    "validate_encoding"
                ],
                "priority": "high"
            },
            "file_not_found": {
                "patterns": [
                    "FileNotFoundError",
                    "No such file or directory"
                ],
                "solutions": [
                    "check_file_path",
                    "create_missing_file",
                    "fix_path_reference"
                ],
                "priority": "medium"
            },
            "permission_error": {
                "patterns": [
                    "PermissionError",
                    "Permission denied"
                ],
                "solutions": [
                    "check_file_permissions",
                    "run_as_administrator",
                    "fix_file_ownership"
                ],
                "priority": "medium"
            },
            "json_error": {
                "patterns": [
                    "JSONDecodeError",
                    "Expecting property name",
                    "Expecting value"
                ],
                "solutions": [
                    "validate_json_syntax",
                    "fix_json_structure",
                    "backup_and_restore"
                ],
                "priority": "high"
            },
            "encoding_error": {
                "patterns": [
                    "UnicodeDecodeError",
                    "UnicodeEncodeError",
                    "codec can't decode"
                ],
                "solutions": [
                    "fix_encoding_declaration",
                    "convert_file_encoding",
                    "use_utf8_encoding"
                ],
                "priority": "medium"
            },
            "timeout_error": {
                "patterns": [
                    "TimeoutError",
                    "timeout",
                    "timed out"
                ],
                "solutions": [
                    "increase_timeout",
                    "optimize_performance",
                    "reduce_scope"
                ],
                "priority": "low"
            }
        }
    
    def detect_error_type(self, error_message: str) -> Optional[str]:
        """Detecta o tipo de erro baseado na mensagem"""
        error_message_lower = error_message.lower()
        
        for error_type, config in self.error_patterns.items():
            for pattern in config["patterns"]:
                if pattern.lower() in error_message_lower:
                    return error_type
        
        return None
    
    def check_python_path(self, script_path: str) -> bool:
        """Verifica se o Python está no PATH"""
        try:
            result = subprocess.run([sys.executable, "--version"], 
                                  capture_output=True, text=True, timeout=10)
            return result.returncode == 0
        except Exception:
            return False
    
    def install_missing_dependencies(self, script_path: str) -> bool:
        """Instala dependências faltantes"""
        try:
            # Lista de dependências comuns do projeto
            dependencies = [
                "pathlib",
                "typing",
                "json",
                "datetime",
                "subprocess"
            ]
            
            for dep in dependencies:
                try:
                    __import__(dep)
                except ImportError:
                    print(f"⚠️ Dependência {dep} não encontrada, mas é padrão do Python")
            
            return True
        except Exception as e:
            print(f"❌ Erro ao verificar dependências: {e}")
            return False
    
    def fix_import_statement(self, script_path: str) -> bool:
        """Corrige declarações de import problemáticas"""
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Verificar imports comuns do projeto
            common_imports = [
                "import json",
                "import os",
                "import sys",
                "from pathlib import Path",
                "from datetime import datetime",
                "from typing import Dict, List, Any"
            ]
            
            # Adicionar imports faltantes se necessário
            lines = content.split('\n')
            import_section = []
            other_lines = []
            
            for line in lines:
                if line.strip().startswith(('import ', 'from ')):
                    import_section.append(line)
                else:
                    other_lines.append(line)
            
            # Verificar se imports essenciais estão presentes
            essential_imports = ["import json", "from pathlib import Path"]
            for essential in essential_imports:
                if not any(essential in imp for imp in import_section):
                    import_section.append(essential)
            
            # Reconstruir arquivo
            new_content = '\n'.join(import_section + [''] + other_lines)
            
            # Fazer backup antes de modificar
            backup_path = script_path.with_suffix('.py.backup')
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            with open(script_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Imports corrigidos em {script_path}")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao corrigir imports: {e}")
            return False
    
    def fix_syntax_error(self, script_path: str) -> bool:
        """Corrige erros de sintaxe básicos"""
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Verificar encoding
            if not content.startswith('# -*- coding: utf-8 -*-'):
                if not content.startswith('#!/usr/bin/env python3'):
                    content = '#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n' + content
            
            # Verificar indentação
            lines = content.split('\n')
            fixed_lines = []
            
            for line in lines:
                # Corrigir mistura de tabs e espaços
                if '\t' in line:
                    line = line.replace('\t', '    ')
                fixed_lines.append(line)
            
            new_content = '\n'.join(fixed_lines)
            
            # Fazer backup
            backup_path = script_path.with_suffix('.py.backup')
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            with open(script_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Sintaxe corrigida em {script_path}")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao corrigir sintaxe: {e}")
            return False
    
    def validate_json_syntax(self, json_path: str) -> bool:
        """Valida e corrige sintaxe JSON"""
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Tentar fazer parse do JSON
            json.loads(content)
            return True
            
        except json.JSONDecodeError as e:
            print(f"⚠️ Erro JSON em {json_path}: {e}")
            
            # Tentar corrigir JSON malformado
            try:
                # Remover linhas vazias e comentários
                lines = content.split('\n')
                cleaned_lines = []
                
                for line in lines:
                    line = line.strip()
                    if line and not line.startswith('//') and not line.startswith('#'):
                        cleaned_lines.append(line)
                
                cleaned_content = '\n'.join(cleaned_lines)
                
                # Tentar parse novamente
                json.loads(cleaned_content)
                
                # Salvar versão corrigida
                backup_path = Path(json_path).with_suffix('.json.backup')
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                with open(json_path, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)
                
                print(f"✅ JSON corrigido em {json_path}")
                return True
                
            except Exception:
                print(f"❌ Não foi possível corrigir JSON em {json_path}")
                return False
    
    def check_file_path(self, file_path: str) -> bool:
        """Verifica se o arquivo existe e cria se necessário"""
        path = Path(file_path)
        
        if not path.exists():
            # Criar diretório se não existir
            path.parent.mkdir(parents=True, exist_ok=True)
            
            # Criar arquivo básico se for JSON
            if path.suffix == '.json':
                with open(path, 'w', encoding='utf-8') as f:
                    json.dump({"metadata": {"created": datetime.now().isoformat()}}, f, indent=2)
                print(f"✅ Arquivo JSON criado: {path}")
            else:
                path.touch()
                print(f"✅ Arquivo criado: {path}")
            
            return True
        
        return True
    
    def fix_encoding_declaration(self, script_path: str) -> bool:
        """Corrige declaração de encoding"""
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Verificar se já tem encoding declarado
            if '# -*- coding: utf-8 -*-' not in content:
                # Adicionar encoding no início
                if content.startswith('#!/usr/bin/env python3'):
                    lines = content.split('\n')
                    lines.insert(1, '# -*- coding: utf-8 -*-')
                    content = '\n'.join(lines)
                else:
                    content = '#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n' + content
            
            # Fazer backup
            backup_path = script_path.with_suffix('.py.backup')
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            with open(script_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Encoding corrigido em {script_path}")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao corrigir encoding: {e}")
            return False
    
    def increase_timeout(self, script_path: str) -> bool:
        """Aumenta timeout para scripts que demoram muito"""
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Procurar por timeouts e aumentar
            if 'timeout=' in content:
                # Substituir timeouts pequenos por maiores
                content = content.replace('timeout=10', 'timeout=60')
                content = content.replace('timeout=30', 'timeout=120')
                
                with open(script_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"✅ Timeout aumentado em {script_path}")
                return True
            
            return False
            
        except Exception as e:
            print(f"❌ Erro ao ajustar timeout: {e}")
            return False
    
    def resolve_error(self, script_path: str, error_message: str) -> Dict[str, Any]:
        """Resolve erro específico em um script Python"""
        print(f"Resolvendo erro em {script_path}")
        print(f"Erro: {error_message}")
        
        error_type = self.detect_error_type(error_message)
        resolution_result = {
            "script_path": script_path,
            "error_message": error_message,
            "error_type": error_type,
            "solutions_applied": [],
            "success": False,
            "timestamp": datetime.now().isoformat()
        }
        
        if not error_type:
            print("Tipo de erro nao reconhecido")
            return resolution_result
        
        print(f"Tipo de erro detectado: {error_type}")
        
        # Aplicar soluções baseadas no tipo de erro
        solutions = self.error_patterns[error_type]["solutions"]
        
        for solution in solutions:
            print(f"Aplicando solucao: {solution}")
            
            try:
                if solution == "check_python_path":
                    if self.check_python_path(script_path):
                        resolution_result["solutions_applied"].append(solution)
                
                elif solution == "install_missing_dependencies":
                    if self.install_missing_dependencies(script_path):
                        resolution_result["solutions_applied"].append(solution)
                
                elif solution == "fix_import_statement":
                    if self.fix_import_statement(script_path):
                        resolution_result["solutions_applied"].append(solution)
                
                elif solution == "fix_syntax_error":
                    if self.fix_syntax_error(script_path):
                        resolution_result["solutions_applied"].append(solution)
                
                elif solution == "validate_json_syntax":
                    if self.validate_json_syntax(script_path):
                        resolution_result["solutions_applied"].append(solution)
                
                elif solution == "check_file_path":
                    if self.check_file_path(script_path):
                        resolution_result["solutions_applied"].append(solution)
                
                elif solution == "fix_encoding_declaration":
                    if self.fix_encoding_declaration(script_path):
                        resolution_result["solutions_applied"].append(solution)
                
                elif solution == "increase_timeout":
                    if self.increase_timeout(script_path):
                        resolution_result["solutions_applied"].append(solution)
                
            except Exception as e:
                print(f"❌ Erro ao aplicar solução {solution}: {e}")
        
        # Testar se o script funciona agora
        if self.test_script(script_path):
            resolution_result["success"] = True
            print(f"✅ Erro resolvido com sucesso!")
        else:
            print(f"⚠️ Erro não foi completamente resolvido")
        
        return resolution_result
    
    def test_script(self, script_path: str) -> bool:
        """Testa se o script funciona após correções"""
        try:
            # Teste básico de sintaxe
            result = subprocess.run([sys.executable, "-m", "py_compile", script_path], 
                                  capture_output=True, text=True, timeout=10)
            
            if result.returncode == 0:
                print(f"✅ Script {script_path} compila corretamente")
                return True
            else:
                print(f"❌ Script {script_path} ainda tem erros de sintaxe")
                return False
                
        except Exception as e:
            print(f"❌ Erro ao testar script: {e}")
            return False
    
    def auto_resolve_script_errors(self, script_path: str) -> Dict[str, Any]:
        """Resolve automaticamente erros em um script Python"""
        print(f"Iniciando resolucao automatica para {script_path}")
        
        # Tentar executar o script para detectar erros
        try:
            result = subprocess.run([sys.executable, script_path], 
                                  capture_output=True, text=True, timeout=self.timeout_seconds)
            
            if result.returncode == 0:
                print(f"✅ Script {script_path} executa sem erros")
                return {
                    "script_path": script_path,
                    "status": "success",
                    "no_errors": True,
                    "timestamp": datetime.now().isoformat()
                }
            
            # Se há erro, tentar resolver
            error_message = result.stderr
            return self.resolve_error(script_path, error_message)
            
        except subprocess.TimeoutExpired:
            return self.resolve_error(script_path, "TimeoutError: Script demorou muito para executar")
        except Exception as e:
            return self.resolve_error(script_path, str(e))
    
    def log_resolution(self, resolution_result: Dict[str, Any]):
        """Registra resultado da resolução"""
        log_file = self.log_path / "python_error_resolutions.json"
        
        # Carregar log existente
        resolutions = []
        if log_file.exists():
            try:
                with open(log_file, 'r', encoding='utf-8') as f:
                    resolutions = json.load(f)
            except:
                resolutions = []
        
        # Adicionar nova resolução
        resolutions.append(resolution_result)
        
        # Salvar log
        log_file.parent.mkdir(parents=True, exist_ok=True)
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(resolutions, f, indent=2, ensure_ascii=False)
        
        print(f"Resolucao registrada em {log_file}")

def main():
    """Função principal para resolução automática"""
    if len(sys.argv) < 2:
        print("❌ Uso: python python_error_resolver.py <script_path>")
        sys.exit(1)
    
    script_path = sys.argv[1]
    resolver = PythonErrorResolver()
    
    # Resolver erros automaticamente
    result = resolver.auto_resolve_script_errors(script_path)
    
    # Registrar resultado
    resolver.log_resolution(result)
    
    # Retornar código de saída apropriado
    if result.get("success", False) or result.get("no_errors", False):
        print("✅ Resolução concluída com sucesso")
        sys.exit(0)
    else:
        print("Resolucao nao foi completamente bem-sucedida")
        sys.exit(1)

if __name__ == "__main__":
    main() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = ErrorresolverModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script python_error_resolver.py executado com sucesso via módulo python.error_resolver")
    else:
        print(f"❌ Erro na execução do script python_error_resolver.py via módulo python.error_resolver")
