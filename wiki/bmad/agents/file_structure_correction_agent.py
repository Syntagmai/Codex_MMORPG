#!/usr/bin/env python3
"""
File Structure Correction Agent - Epic 18 Task 18.5
Limpa estrutura de arquivos, remove itens obsoletos e corrige problemas de nomenclatura
"""
import os
import json
import re
import shutil
from datetime import datetime
from pathlib import Path

class FileStructureCorrectionAgent:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.audit_reports_dir = self.project_root / "wiki" / "docs" / "audit_reports"
        self.file_structure_report = self.audit_reports_dir / "file_structure_audit_report.json"
        self.correction_report = {
            "timestamp": datetime.now().isoformat(),
            "obsolete_items_removed": [],
            "empty_directories_removed": [],
            "naming_issues_fixed": [],
            "duplicate_files_removed": [],
            "backup_files_cleaned": [],
            "temp_files_removed": [],
            "files_modified": [],
            "directories_created": [],
            "total_cleanup_items": 0
        }
    
    def load_file_structure_audit(self):
        """Carrega o relatório de auditoria de estrutura de arquivos"""
        try:
            with open(self.file_structure_report, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Erro ao carregar relatório de estrutura de arquivos: {e}")
            return None
    
    def remove_obsolete_items(self, obsolete_items):
        """Remove itens obsoletos"""
        removed_items = []
        
        for item in obsolete_items:
            item_path = item.get('file_path', '')
            item_type = item.get('item_type', '')
            description = item.get('description', '')
            
            if not item_path or not os.path.exists(item_path):
                continue
            
            try:
                # Cria backup antes de remover
                backup_path = str(item_path) + ".backup"
                if os.path.isfile(item_path):
                    shutil.copy2(item_path, backup_path)
                elif os.path.isdir(item_path):
                    shutil.copytree(item_path, backup_path)
                
                # Remove o item
                if os.path.isfile(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                
                removed_items.append({
                    "path": item_path,
                    "type": item_type,
                    "description": description,
                    "backup_created": backup_path
                })
                
                self.correction_report["files_modified"].append(item_path)
                
            except Exception as e:
                print(f"Erro ao remover item obsoleto {item_path}: {e}")
        
        self.correction_report["obsolete_items_removed"] = removed_items
        return removed_items
    
    def remove_empty_directories(self, empty_dirs):
        """Remove diretórios vazios"""
        removed_dirs = []
        
        for dir_path in empty_dirs:
            if not dir_path or not os.path.exists(dir_path):
                continue
            
            try:
                # Verifica se o diretório está realmente vazio
                if os.path.isdir(dir_path) and not os.listdir(dir_path):
                    # Cria backup
                    backup_path = str(dir_path) + ".backup"
                    shutil.copytree(dir_path, backup_path)
                    
                    # Remove diretório
                    os.rmdir(dir_path)
                    
                    removed_dirs.append({
                        "path": dir_path,
                        "description": "Empty directory removed",
                        "backup_created": backup_path
                    })
                    
                    self.correction_report["files_modified"].append(dir_path)
                
            except Exception as e:
                print(f"Erro ao remover diretório vazio {dir_path}: {e}")
        
        self.correction_report["empty_directories_removed"] = removed_dirs
        return removed_dirs
    
    def fix_naming_issues(self, naming_issues):
        """Corrige problemas de nomenclatura"""
        fixed_issues = []
        
        for issue in naming_issues:
            file_path = issue.get('file_path', '')
            issue_type = issue.get('issue_type', '')
            description = issue.get('description', '')
            
            if not file_path or not os.path.exists(file_path):
                continue
            
            try:
                # Cria backup
                backup_path = str(file_path) + ".backup"
                shutil.copy2(file_path, backup_path)
                
                # Corrige nomenclatura baseada no tipo de problema
                if "spaces" in issue_type.lower():
                    new_path = self.fix_spaces_in_filename(file_path)
                elif "special_chars" in issue_type.lower():
                    new_path = self.fix_special_characters(file_path)
                elif "case" in issue_type.lower():
                    new_path = self.fix_case_issues(file_path)
                elif "length" in issue_type.lower():
                    new_path = self.fix_filename_length(file_path)
                else:
                    new_path = file_path
                
                # Renomeia se houve mudança
                if new_path != file_path:
                    os.rename(file_path, new_path)
                    
                    fixed_issues.append({
                        "old_path": file_path,
                        "new_path": new_path,
                        "issue_type": issue_type,
                        "description": description,
                        "backup_created": backup_path
                    })
                    
                    self.correction_report["files_modified"].append(new_path)
                
            except Exception as e:
                print(f"Erro ao corrigir nomenclatura em {file_path}: {e}")
        
        self.correction_report["naming_issues_fixed"] = fixed_issues
        return fixed_issues
    
    def fix_spaces_in_filename(self, file_path):
        """Corrige espaços em nomes de arquivo"""
        path_obj = Path(file_path)
        parent = path_obj.parent
        name = path_obj.name
        
        # Substitui espaços por underscores
        new_name = name.replace(' ', '_')
        
        return str(parent / new_name)
    
    def fix_special_characters(self, file_path):
        """Corrige caracteres especiais em nomes de arquivo"""
        path_obj = Path(file_path)
        parent = path_obj.parent
        name = path_obj.name
        
        # Remove caracteres especiais problemáticos
        special_chars = ['<', '>', ':', '"', '|', '?', '*', '\\', '/']
        for char in special_chars:
            name = name.replace(char, '_')
        
        # Remove caracteres de controle
        name = ''.join(char for char in name if ord(char) >= 32)
        
        return str(parent / name)
    
    def fix_case_issues(self, file_path):
        """Corrige problemas de case em nomes de arquivo"""
        path_obj = Path(file_path)
        parent = path_obj.parent
        name = path_obj.name
        
        # Converte para lowercase para consistência
        new_name = name.lower()
        
        return str(parent / new_name)
    
    def fix_filename_length(self, file_path):
        """Corrige nomes de arquivo muito longos"""
        path_obj = Path(file_path)
        parent = path_obj.parent
        name = path_obj.name
        
        # Limita o tamanho do nome (máximo 255 caracteres)
        if len(name) > 255:
            # Mantém extensão
            name_parts = name.rsplit('.', 1)
            if len(name_parts) > 1:
                base_name = name_parts[0]
                extension = '.' + name_parts[1]
                # Trunca o nome base
                max_base_length = 255 - len(extension)
                new_name = base_name[:max_base_length] + extension
            else:
                new_name = name[:255]
        else:
            new_name = name
        
        return str(parent / new_name)
    
    def remove_duplicate_files(self, duplicate_files):
        """Remove arquivos duplicados"""
        removed_duplicates = []
        
        for duplicate_group in duplicate_files:
            files = duplicate_group.get('files', [])
            if len(files) <= 1:
                continue
            
            # Mantém o primeiro arquivo, remove os outros
            keep_file = files[0]
            remove_files = files[1:]
            
            for file_path in remove_files:
                if os.path.exists(file_path):
                    try:
                        # Cria backup
                        backup_path = str(file_path) + ".backup"
                        shutil.copy2(file_path, backup_path)
                        
                        # Remove arquivo
                        os.remove(file_path)
                        
                        removed_duplicates.append({
                            "removed_file": file_path,
                            "kept_file": keep_file,
                            "backup_created": backup_path
                        })
                        
                        self.correction_report["files_modified"].append(file_path)
                        
                    except Exception as e:
                        print(f"Erro ao remover arquivo duplicado {file_path}: {e}")
        
        self.correction_report["duplicate_files_removed"] = removed_duplicates
        return removed_duplicates
    
    def clean_backup_files(self):
        """Remove arquivos de backup antigos"""
        backup_files = []
        
        # Procura por arquivos .backup antigos (mais de 30 dias)
        for root, dirs, files in os.walk(self.project_root):
            for file in files:
                if file.endswith('.backup'):
                    file_path = os.path.join(root, file)
                    try:
                        # Verifica se o arquivo é antigo
                        file_time = os.path.getmtime(file_path)
                        current_time = datetime.now().timestamp()
                        days_old = (current_time - file_time) / (24 * 3600)
                        
                        if days_old > 30:
                            os.remove(file_path)
                            backup_files.append({
                                "file": file_path,
                                "days_old": int(days_old)
                            })
                            
                    except Exception as e:
                        print(f"Erro ao remover backup antigo {file_path}: {e}")
        
        self.correction_report["backup_files_cleaned"] = backup_files
        return backup_files
    
    def remove_temp_files(self):
        """Remove arquivos temporários"""
        temp_files = []
        
        # Padrões de arquivos temporários
        temp_patterns = [
            '*.tmp', '*.temp', '*.swp', '*.swo', '*.bak',
            '*~', '.#*', '.DS_Store', 'Thumbs.db',
            '*.log', '*.out', '*.pid'
        ]
        
        for pattern in temp_patterns:
            for root, dirs, files in os.walk(self.project_root):
                for file in files:
                    if self.matches_pattern(file, pattern):
                        file_path = os.path.join(root, file)
                        try:
                            os.remove(file_path)
                            temp_files.append({
                                "file": file_path,
                                "pattern": pattern
                            })
                            
                        except Exception as e:
                            print(f"Erro ao remover arquivo temporário {file_path}: {e}")
        
        self.correction_report["temp_files_removed"] = temp_files
        return temp_files
    
    def matches_pattern(self, filename, pattern):
        """Verifica se o arquivo corresponde ao padrão"""
        import fnmatch
        return fnmatch.fnmatch(filename, pattern)
    
    def create_organized_structure(self):
        """Cria estrutura organizada de diretórios"""
        organized_dirs = []
        
        # Diretórios padrão para organização
        standard_dirs = [
            "src",
            "tests",
            "docs",
            "config",
            "logs",
            "temp",
            "backup",
            "assets",
            "data",
            "scripts"
        ]
        
        for dir_name in standard_dirs:
            dir_path = self.project_root / dir_name
            if not dir_path.exists():
                try:
                    dir_path.mkdir(parents=True, exist_ok=True)
                    organized_dirs.append(str(dir_path))
                    
                    # Cria arquivo .gitkeep para manter diretório no git
                    gitkeep_file = dir_path / ".gitkeep"
                    gitkeep_file.touch()
                    
                except Exception as e:
                    print(f"Erro ao criar diretório {dir_path}: {e}")
        
        self.correction_report["directories_created"] = organized_dirs
        return organized_dirs
    
    def create_file_structure_guidelines(self):
        """Cria diretrizes de estrutura de arquivos"""
        guidelines = '''# Diretrizes de Estrutura de Arquivos - Codex MMORPG

## 1. Organização de Diretórios
- **src/**: Código fonte principal
- **tests/**: Testes unitários e de integração
- **docs/**: Documentação do projeto
- **config/**: Arquivos de configuração
- **logs/**: Arquivos de log
- **temp/**: Arquivos temporários
- **backup/**: Backups automáticos
- **assets/**: Recursos estáticos (imagens, fontes, etc.)
- **data/**: Dados do projeto
- **scripts/**: Scripts utilitários

## 2. Nomenclatura de Arquivos
- Usar nomes descritivos e em inglês
- Evitar espaços (usar underscores ou hífens)
- Usar lowercase para nomes de arquivos
- Evitar caracteres especiais
- Manter nomes com menos de 255 caracteres
- Usar extensões apropriadas

## 3. Estrutura de Código
- Organizar por funcionalidade
- Separar interfaces de implementações
- Agrupar arquivos relacionados
- Usar namespaces/packages adequadamente
- Manter hierarquia lógica

## 4. Versionamento
- Não versionar arquivos temporários
- Usar .gitignore adequadamente
- Manter histórico de mudanças
- Fazer backups regulares
- Documentar mudanças estruturais

## 5. Limpeza Regular
- Remover arquivos obsoletos
- Limpar diretórios vazios
- Remover arquivos temporários
- Consolidar arquivos duplicados
- Manter estrutura organizada

## 6. Padrões de Arquivo
- **Código**: .py, .js, .cpp, .h, etc.
- **Configuração**: .json, .yaml, .ini, .conf
- **Documentação**: .md, .txt, .pdf
- **Dados**: .csv, .xml, .json
- **Recursos**: .png, .jpg, .svg, .mp3, .mp4

## 7. Segurança
- Não versionar dados sensíveis
- Usar variáveis de ambiente
- Proteger arquivos de configuração
- Validar entrada de dados
- Manter permissões adequadas

## 8. Performance
- Otimizar tamanho de arquivos
- Usar compressão quando apropriado
- Evitar arquivos muito grandes
- Implementar cache adequadamente
- Monitorar uso de espaço
'''
        
        guidelines_file = self.project_root / "wiki" / "docs" / "file_structure_guidelines.md"
        with open(guidelines_file, 'w', encoding='utf-8') as f:
            f.write(guidelines)
        
        self.correction_report["files_modified"].append(str(guidelines_file))
        return str(guidelines_file)
    
    def create_correction_report(self):
        """Cria relatório de correção"""
        report_file = self.audit_reports_dir / "file_structure_correction_report.json"
        
        # Calcula estatísticas
        total_obsolete = len(self.correction_report["obsolete_items_removed"])
        total_empty_dirs = len(self.correction_report["empty_directories_removed"])
        total_naming_fixes = len(self.correction_report["naming_issues_fixed"])
        total_duplicates = len(self.correction_report["duplicate_files_removed"])
        total_backups_cleaned = len(self.correction_report["backup_files_cleaned"])
        total_temp_files = len(self.correction_report["temp_files_removed"])
        total_dirs_created = len(self.correction_report["directories_created"])
        
        self.correction_report["total_cleanup_items"] = (
            total_obsolete + total_empty_dirs + total_naming_fixes + 
            total_duplicates + total_backups_cleaned + total_temp_files
        )
        
        self.correction_report["statistics"] = {
            "obsolete_items_removed": total_obsolete,
            "empty_directories_removed": total_empty_dirs,
            "naming_issues_fixed": total_naming_fixes,
            "duplicate_files_removed": total_duplicates,
            "backup_files_cleaned": total_backups_cleaned,
            "temp_files_removed": total_temp_files,
            "directories_created": total_dirs_created,
            "files_modified": len(set(self.correction_report["files_modified"]))
        }
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(self.correction_report, f, indent=2, ensure_ascii=False)
        
        return str(report_file)
    
    def run_file_structure_correction(self):
        """Executa correção de estrutura de arquivos completa"""
        print("🗂️ Iniciando limpeza de estrutura de arquivos...")
        
        # Carrega relatório de estrutura de arquivos
        structure_data = self.load_file_structure_audit()
        if not structure_data:
            print("❌ Não foi possível carregar relatório de estrutura de arquivos")
            return False
        
        print(f"📊 Itens obsoletos identificados: {len(structure_data.get('obsolete_items', []))}")
        print(f"📊 Diretórios vazios identificados: {len(structure_data.get('empty_directories', []))}")
        print(f"📊 Problemas de nomenclatura identificados: {len(structure_data.get('naming_issues', []))}")
        
        # Remove itens obsoletos
        print("🗑️ Removendo itens obsoletos...")
        obsolete_removed = self.remove_obsolete_items(structure_data.get('obsolete_items', []))
        
        # Remove diretórios vazios
        print("📁 Removendo diretórios vazios...")
        empty_dirs_removed = self.remove_empty_directories(structure_data.get('empty_directories', []))
        
        # Corrige problemas de nomenclatura
        print("✏️ Corrigindo problemas de nomenclatura...")
        naming_fixed = self.fix_naming_issues(structure_data.get('naming_issues', []))
        
        # Remove arquivos duplicados (se existirem)
        print("🔄 Verificando arquivos duplicados...")
        duplicate_files = structure_data.get('duplicate_files', [])
        if duplicate_files:
            duplicates_removed = self.remove_duplicate_files(duplicate_files)
        else:
            duplicates_removed = []
        
        # Limpa arquivos de backup antigos
        print("🧹 Limpando arquivos de backup antigos...")
        backups_cleaned = self.clean_backup_files()
        
        # Remove arquivos temporários
        print("🗑️ Removendo arquivos temporários...")
        temp_files_removed = self.remove_temp_files()
        
        # Cria estrutura organizada
        print("📂 Criando estrutura organizada...")
        organized_dirs = self.create_organized_structure()
        
        # Cria diretrizes
        print("📋 Criando diretrizes de estrutura de arquivos...")
        guidelines_file = self.create_file_structure_guidelines()
        
        # Cria relatório
        report_file = self.create_correction_report()
        
        # Estatísticas finais
        total_cleanup = (
            len(obsolete_removed) + len(empty_dirs_removed) + 
            len(naming_fixed) + len(duplicates_removed) + 
            len(backups_cleaned) + len(temp_files_removed)
        )
        
        print(f"\n✅ Limpeza de estrutura de arquivos concluída!")
        print(f"📊 Itens obsoletos removidos: {len(obsolete_removed)}")
        print(f"📁 Diretórios vazios removidos: {len(empty_dirs_removed)}")
        print(f"✏️ Problemas de nomenclatura corrigidos: {len(naming_fixed)}")
        print(f"🔄 Arquivos duplicados removidos: {len(duplicates_removed)}")
        print(f"🧹 Backups antigos limpos: {len(backups_cleaned)}")
        print(f"🗑️ Arquivos temporários removidos: {len(temp_files_removed)}")
        print(f"📂 Diretórios organizados criados: {len(organized_dirs)}")
        print(f"📄 Relatório salvo em: {report_file}")
        print(f"📋 Diretrizes: {guidelines_file}")
        
        return True

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        project_root = sys.argv[1]
    else:
        project_root = "."
    
    agent = FileStructureCorrectionAgent(project_root)
    result = agent.run_file_structure_correction() 