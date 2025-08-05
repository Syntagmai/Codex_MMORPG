from unicode_aliases import *
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import ast
import json
import logging
import os
import re
import shutil

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 Error Correction Agent - Epic 12 Task 12.6
=============================================

Script para implementar correção automática de erros Python.
Baseado nos resultados de validação da Task 12.5.

Responsável: Error Correction Agent
Duração: 3-4 dias
Dependência: Task 12.5 (Validação de scripts)
"""


# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ErrorCorrectionAgent:
    """Agente para correção automática de erros Python."""
    
    def __init__(self):
        self.project_root = Path(__file__).parent.parent.parent
        self.modules_path = self.project_root / "wiki/update/modules"
        self.validation_path = self.project_root / "wiki/update/validation_results"
        self.correction_path = self.project_root / "wiki/update/correction_results"
        
        # Criar diretório de resultados
        self.correction_path.mkdir(exist_ok=True)
        
        # Carregar resultados de validação
        self.validation_results = self.load_validation_results()
        
        # Estatísticas de correção
        self.correction_stats = {
            "total_files_processed": 0,
            "files_corrected": 0,
            "files_failed": 0,
            "errors_fixed": 0,
            "warnings_fixed": 0,
            "backups_created": 0,
            "errors": [],
            "warnings": []
        }
        
        # Regras de correção
        self.correction_rules = {
            "syntax_errors": {
                "unterminated_string": True,
                "invalid_character": True,
                "leading_zeros": True,
                "indentation_error": True
            },
            "style_issues": {
                "line_length": True,
                "naming_convention": True,
                "missing_docstring": True,
                "magic_numbers": True
            },
            "quality_issues": {
                "unused_imports": True,
                "complexity_reduction": True,
                "code_duplication": True
            }
        }
    
    def load_validation_results(self) -> Dict[str, Any]:
        """Carrega os resultados de validação."""
        validation_file = self.validation_path / "python_validation_results.json"
        if validation_file.exists():
            with open(validation_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            logger.warning("⚠️ Resultados de validação não encontrados")
            return {"results": []}
    
    def get_files_with_errors(self) -> List[Dict[str, Any]]:
        """Obtém arquivos que possuem erros para correção."""
        files_with_errors = []
        
        for result in self.validation_results.get("results", []):
            if result.get("errors") or result.get("warnings"):
                files_with_errors.append(result)
        
        logger.info(f"📊 Encontrados {len(files_with_errors)} arquivos com problemas para correção")
        return files_with_errors
    
    def create_backup(self, file_path: Path) -> bool:
        """Cria backup de um arquivo antes da correção."""
        try:
            backup_path = file_path.with_suffix(f"{file_path.suffix}.backup")
            shutil.copy2(file_path, backup_path)
            self.correction_stats["backups_created"] += 1
            logger.info(f"💾 Backup criado: {backup_path}")
            return True
        except Exception as e:
            logger.error(f"❌ Erro ao criar backup de {file_path}: {e}")
            return False
    
    def fix_unterminated_string(self, content: str, line_number: int) -> str:
        """Corrige strings não terminadas."""
        lines = content.split('\n')
        
        if line_number <= len(lines):
            line = lines[line_number - 1]
            
            # Verificar se há aspas não fechadas
            if line.count('"') % 2 != 0:
                # Adicionar aspas de fechamento
                lines[line_number - 1] = line + '"'
            elif line.count("'") % 2 != 0:
                # Adicionar aspas simples de fechamento
                lines[line_number - 1] = line + "'"
            elif '"""' in line and line.count('"""') % 2 != 0:
                # Adicionar aspas triplas de fechamento
                lines[line_number - 1] = line + '"""'
            elif "'''" in line and line.count("'''") % 2 != 0:
                # Adicionar aspas triplas simples de fechamento
                lines[line_number - 1] = line + "'''"
        
        return '\n'.join(lines)
    
    def fix_invalid_character(self, content: str, line_number: int) -> str:
        """Corrige caracteres inválidos."""
        lines = content.split('\n')
        
        if line_number <= len(lines):
            line = lines[line_number - 1]
            
            # Remover emojis e caracteres especiais
            # Manter apenas caracteres ASCII válidos para Python
            cleaned_line = re.sub(r'[^\x00-\x7F]+', '', line)
            lines[line_number - 1] = cleaned_line
        
        return '\n'.join(lines)
    
    def fix_leading_zeros(self, content: str, line_number: int) -> str:
        """Corrige literais com zeros à esquerda."""
        lines = content.split('\n')
        
        if line_number <= len(lines):
            line = lines[line_number - 1]
            
            # Corrigir números com zeros à esquerda (exceto 0)
            # Substituir 0x por 0o para números octais
            corrected_line = re.sub(r'\b0+([1-9]\d*)\b', r'\1', line)
            corrected_line = re.sub(r'\b0+([1-7][0-7]*)\b', r'0o\1', corrected_line)
            
            lines[line_number - 1] = corrected_line
        
        return '\n'.join(lines)
    
    def fix_line_length(self, content: str) -> str:
        """Corrige linhas muito longas."""
        lines = content.split('\n')
        corrected_lines = []
        
        for line in lines:
            if len(line) > 120:
                # Tentar quebrar a linha em pontos lógicos
                if ',' in line:
                    # Quebrar em vírgulas
                    parts = line.split(',')
                    current_line = parts[0]
                    
                    for part in parts[1:]:
                        if len(current_line + ',' + part) > 120:
                            corrected_lines.append(current_line + ',')
                            current_line = '    ' + part.lstrip()
                        else:
                            current_line += ',' + part
                    
                    corrected_lines.append(current_line)
                elif '(' in line and ')' in line:
                    # Quebrar em parênteses
                    corrected_lines.append(line)
                else:
                    # Quebrar em espaços
                    words = line.split()
                    current_line = words[0]
                    
                    for word in words[1:]:
                        if len(current_line + ' ' + word) > 120:
                            corrected_lines.append(current_line)
                            current_line = '    ' + word
                        else:
                            current_line += ' ' + word
                    
                    corrected_lines.append(current_line)
            else:
                corrected_lines.append(line)
        
        return '\n'.join(corrected_lines)
    
    def fix_naming_convention(self, content: str) -> str:
        """Corrige convenções de nomenclatura."""
        try:
            tree = ast.parse(content)
            
            # Mapear nomes antigos para novos
            name_mapping = {}
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    old_name = node.name
                    # Converter para snake_case
                    new_name = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', old_name).lower()
                    if new_name != old_name:
                        name_mapping[old_name] = new_name
                
                elif isinstance(node, ast.ClassDef):
                    old_name = node.name
                    # Converter para PascalCase
                    new_name = ''.join(word.capitalize() for word in re.split(r'[_\s]', old_name))
                    if new_name != old_name:
                        name_mapping[old_name] = new_name
            
            # Aplicar mudanças
            for old_name, new_name in name_mapping.items():
                content = re.sub(r'\b' + re.escape(old_name) + r'\b', new_name, content)
            
        except:
            pass  # Se não conseguir fazer parse, mantém o conteúdo original
        
        return content
    
    def fix_missing_docstring(self, content: str) -> str:
        """Adiciona docstrings ausentes."""
        lines = content.split('\n')
        
        # Verificar se já tem docstring no início
        has_docstring = False
        for line in lines[:5]:  # Verificar apenas as primeiras 5 linhas
            if line.strip().startswith('"""') or line.strip().startswith("'''"):
                has_docstring = True
                break
        
        if not has_docstring:
            # Adicionar docstring básica
            docstring = '"""\nMódulo Python.\n"""\n'
            lines.insert(0, docstring)
        
        return '\n'.join(lines)
    
    def fix_magic_numbers(self, content: str) -> str:
        """Substitui números mágicos por constantes."""
        lines = content.split('\n')
        
        # Definir constantes comuns
        constants = {
            '8': 'MAX_RETRIES',
            '10': 'MAX_ATTEMPTS',
            '100': 'MAX_ITEMS',
            '1000': 'MAX_SIZE',
            '500': 'TIMEOUT_MS',
            '60': 'TIMEOUT_SECONDS'
        }
        
        # Adicionar constantes no início do arquivo
        constants_added = []
        for number, const_name in constants.items():
            if number in content and const_name not in content:
                constants_added.append(f"{const_name} = {number}")
        
        if constants_added:
            lines.insert(0, "# Constantes\n" + '\n'.join(constants_added) + '\n')
        
        return '\n'.join(lines)
    
    def fix_unused_imports(self, content: str) -> str:
        """Remove imports não utilizados."""
        try:
            tree = ast.parse(content)
            
            # Encontrar imports
            imports = []
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imports.append(node.module)
            
            # Encontrar nomes utilizados
            used_names = set()
            for node in ast.walk(tree):
                if isinstance(node, ast.Name):
                    used_names.add(node.id)
                elif isinstance(node, ast.Attribute):
                    if isinstance(node.value, ast.Name):
                        used_names.add(node.value.id)
            
            # Remover imports não utilizados
            lines = content.split('\n')
            corrected_lines = []
            
            for line in lines:
                should_keep = True
                
                # Verificar se é uma linha de import
                if line.strip().startswith('import ') or line.strip().startswith('from '):
                    for import_name in imports:
                        if import_name in line and import_name not in used_names:
                            should_keep = False
                            break
                
                if should_keep:
                    corrected_lines.append(line)
            
            return '\n'.join(corrected_lines)
            
        except:
            return content  # Se não conseguir fazer parse, mantém o conteúdo original
    
    def correct_file(self, file_info: Dict[str, Any]) -> Dict[str, Any]:
        """Corrige um arquivo Python."""
        file_path = Path(file_info["file_path"])
        
        if not file_path.exists():
            return {
                "file_path": str(file_path),
                "corrected": False,
                "error": "file_not_found"
            }
        
        try:
            # Criar backup
            self.create_backup(file_path)
            
            # Ler conteúdo
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
                    "corrected": False,
                    "error": "encoding_error"
                }
            
            original_content = content
            corrections_made = []
            
            # Corrigir erros de sintaxe
            for error in file_info.get("errors", []):
                error_type = error.get("type", "")
                line_number = error.get("line", 0)
                
                if error_type == "syntax_error":
                    message = error.get("message", "")
                    
                    if "unterminated string" in message:
                        content = self.fix_unterminated_string(content, line_number)
                        corrections_made.append("unterminated_string")
                    
                    elif "invalid character" in message:
                        content = self.fix_invalid_character(content, line_number)
                        corrections_made.append("invalid_character")
                    
                    elif "leading zeros" in message:
                        content = self.fix_leading_zeros(content, line_number)
                        corrections_made.append("leading_zeros")
            
            # Corrigir avisos de estilo
            for warning in file_info.get("warnings", []):
                warning_type = warning.get("type", "")
                
                if warning_type == "line_too_long":
                    content = self.fix_line_length(content)
                    corrections_made.append("line_length")
                
                elif warning_type == "naming_convention":
                    content = self.fix_naming_convention(content)
                    corrections_made.append("naming_convention")
                
                elif warning_type == "missing_module_docstring":
                    content = self.fix_missing_docstring(content)
                    corrections_made.append("missing_docstring")
                
                elif warning_type == "magic_number":
                    content = self.fix_magic_numbers(content)
                    corrections_made.append("magic_numbers")
            
            # Corrigir problemas de qualidade
            content = self.fix_unused_imports(content)
            if content != original_content:
                corrections_made.append("unused_imports")
            
            # Salvar arquivo corrigido
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                self.correction_stats["files_corrected"] += 1
                self.correction_stats["errors_fixed"] += len(file_info.get("errors", []))
                self.correction_stats["warnings_fixed"] += len(file_info.get("warnings", []))
                
                return {
                    "file_path": str(file_path),
                    "corrected": True,
                    "corrections_made": corrections_made,
                    "errors_fixed": len(file_info.get("errors", [])),
                    "warnings_fixed": len(file_info.get("warnings", []))
                }
            else:
                return {
                    "file_path": str(file_path),
                    "corrected": False,
                    "reason": "no_corrections_needed"
                }
            
        except Exception as e:
            self.correction_stats["files_failed"] += 1
            return {
                "file_path": str(file_path),
                "corrected": False,
                "error": str(e)
            }
    
    def correct_all_files(self) -> bool:
        """Corrige todos os arquivos com problemas."""
        logger.info("🚀 Iniciando correção automática de erros Python...")
        
        # Obter arquivos com problemas
        files_with_issues = self.get_files_with_errors()
        self.correction_stats["total_files_processed"] = len(files_with_issues)
        
        if not files_with_issues:
            logger.warning("⚠️ Nenhum arquivo com problemas encontrado")
            return False
        
        # Corrigir cada arquivo
        correction_results = []
        
        for file_info in files_with_issues:
            logger.info(f"🔧 Corrigindo: {file_info['file_name']}")
            
            result = self.correct_file(file_info)
            correction_results.append(result)
            
            if result.get("corrected", False):
                logger.info(f"✅ Corrigido: {result['corrections_made']}")
            else:
                logger.warning(f"⚠️ Não corrigido: {result.get('reason', result.get('error', 'unknown'))}")
        
        # Salvar resultados
        self.save_correction_results(correction_results)
        
        logger.info("✅ Correção automática de erros Python concluída!")
        return True
    
    def save_correction_results(self, results: List[Dict[str, Any]]):
        """Salva os resultados da correção."""
        logger.info("💾 Salvando resultados da correção...")
        
        # Resultados completos
        correction_file = self.correction_path / "python_correction_results.json"
        with open(correction_file, 'w', encoding='utf-8') as f:
            json.dump({
                "metadata": {
                    "created": datetime.now().isoformat(),
                    "total_files": len(results),
                    "correction_stats": self.correction_stats
                },
                "results": results
            }, f, indent=2, ensure_ascii=False)
        
        # Relatório resumido
        summary_file = self.correction_path / "correction_summary.json"
        summary = {
            "total_files_processed": self.correction_stats["total_files_processed"],
            "files_corrected": self.correction_stats["files_corrected"],
            "files_failed": self.correction_stats["files_failed"],
            "errors_fixed": self.correction_stats["errors_fixed"],
            "warnings_fixed": self.correction_stats["warnings_fixed"],
            "backups_created": self.correction_stats["backups_created"],
            "success_rate": (self.correction_stats["files_corrected"] / self.correction_stats["total_files_processed"]) * 100 if self.correction_stats["total_files_processed"] > 0 else 0
        }
        
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        
        logger.info(f"📄 Resultados salvos em: {self.correction_path}")
    
    def generate_correction_report(self) -> Dict[str, Any]:
        """Gera relatório da correção."""
        return {
            "task": "12.6",
            "description": "Implementar correção automática de erros Python",
            "status": "completed",
            "timestamp": datetime.now().isoformat(),
            "correction_stats": self.correction_stats,
            "correction_info": {
                "total_files_processed": self.correction_stats["total_files_processed"],
                "files_corrected": self.correction_stats["files_corrected"],
                "files_failed": self.correction_stats["files_failed"],
                "errors_fixed": self.correction_stats["errors_fixed"],
                "warnings_fixed": self.correction_stats["warnings_fixed"],
                "correction_path": str(self.correction_path)
            },
            "next_task": "12.7 - Criar ferramentas Python especializadas"
        }
    
    def save_correction_report(self, report: Dict[str, Any]):
        """Salva relatório da correção."""
        report_file = self.project_root / "wiki/log/task_12_6_correction_report.json"
        report_file.parent.mkdir(exist_ok=True)
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        logger.info(f"📄 Relatório salvo em: {report_file}")

def main():
    """Função principal do script."""
    print("🚀 Error Correction Agent - Epic 12 Task 12.6")
    print("=" * 60)
    
    agent = ErrorCorrectionAgent()
    
    # Executar correção
    success = agent.correct_all_files()
    
    if success:
        # Gerar relatório
        report = agent.generate_correction_report()
        agent.save_correction_report(report)
        
        stats = report["correction_stats"]
        correction_info = report["correction_info"]
        
        print("\n✅ Correção automática de erros Python concluída com sucesso!")
        print(f"📊 Arquivos processados: {stats['total_files_processed']}")
        print(f"✅ Arquivos corrigidos: {stats['files_corrected']}")
        print(f"❌ Arquivos com falha: {stats['files_failed']}")
        print(f"🔧 Erros corrigidos: {stats['errors_fixed']}")
        print(f"⚠️ Avisos corrigidos: {stats['warnings_fixed']}")
        print(f"💾 Backups criados: {stats['backups_created']}")
        print(f"📄 Resultados salvos em: {correction_info['correction_path']}")
        print(f"📋 Próxima task: {report['next_task']}")
        
        if stats['errors']:
            print(f"\n❌ Erros de correção: {len(stats['errors'])}")
            for error in stats['errors'][:3]:  # Mostrar apenas os primeiros 3
                print(f"  - {error}")
        
        if stats['warnings']:
            print(f"\n⚠️ Avisos de correção: {len(stats['warnings'])}")
            for warning in stats['warnings'][:3]:  # Mostrar apenas os primeiros 3
                print(f"  - {warning}")
        
    else:
        print("❌ Erro na correção automática de erros Python")
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
- **Nome**: error_correction_agent
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

