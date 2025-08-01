from datetime import datetime
from pathlib import Path
import json
import os
import shutil

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Limpeza e Organização do Sistema
Organiza arquivos temporários e relatórios conforme regras de limpeza
"""


class SystemCleanup:
    """Sistema de limpeza e organização automática"""
    
    def __init__(self):
        self.wiki_dir = Path("wiki")
        self.log_dir = self.wiki_dir / "log"
        self.update_dir = self.wiki_dir / "update"
        
        # Estrutura de pastas de log
        self.log_structure = {
            "completed_tasks": self.log_dir / "completed_tasks",
            "reports": self.log_dir / "reports",
            "recipes": self.log_dir / "recipes",
            "archives": {
                "obsolete_files": self.log_dir / "archives" / "obsolete_files",
                "historical_data": self.log_dir / "archives" / "historical_data"
            }
        }
        
        # Arquivos temporários identificados
        self.temp_files = [
            "integration_tasks.md",
            "INTEGRATION_STATUS_REPORT.md",
            "DEPENDENCY_INTEGRATION_PLAN.md"
        ]
        
        # Arquivos de relatório
        self.report_files = [
            "INTEGRATION_STATUS_REPORT.md",
            "Sistema_OTClient_BMAD_Relatorio_Geral.md"
        ]
        
        # Arquivos de tarefas concluídas
        self.completed_task_files = [
            "integration_tasks.md"
        ]
        
        # Arquivos obsoletos
        self.obsolete_files = [
            "DEPENDENCY_INTEGRATION_PLAN.md"
        ]
    
    def create_log_structure(self):
        """Cria estrutura de pastas de log"""
        print("📁 Criando estrutura de pastas de log...")
        
        for folder_path in self.log_structure.values():
            if isinstance(folder_path, dict):
                for subfolder in folder_path.values():
                    subfolder.mkdir(parents=True, exist_ok=True)
            else:
                folder_path.mkdir(parents=True, exist_ok=True)
        
        print("✅ Estrutura de pastas criada com sucesso!")
    
    def identify_temp_files(self):
        """Identifica arquivos temporários no sistema"""
        print("🔍 Identificando arquivos temporários...")
        
        found_files = []
        for file_name in self.temp_files:
            file_path = self.wiki_dir / file_name
            if file_path.exists():
                found_files.append((file_name, file_path))
                print(f"   📄 Encontrado: {file_name}")
        
        return found_files
    
    def move_reports_to_log(self):
        """Move relatórios para pasta de relatórios"""
        print("📊 Movendo relatórios para pasta de log...")
        
        moved_count = 0
        for file_name in self.report_files:
            source_path = self.wiki_dir / file_name
            dest_path = self.log_structure["reports"] / file_name
            
            if source_path.exists():
                try:
                    shutil.move(str(source_path), str(dest_path))
                    print(f"   ✅ Movido: {file_name} → log/reports/")
                    moved_count += 1
                except Exception as e:
                    print(f"   ❌ Erro ao mover {file_name}: {e}")
        
        print(f"✅ {moved_count} relatórios movidos com sucesso!")
    
    def archive_completed_tasks(self):
        """Arquiva tarefas concluídas"""
        print("📋 Arquivando tarefas concluídas...")
        
        archived_count = 0
        for file_name in self.completed_task_files:
            source_path = self.wiki_dir / file_name
            dest_path = self.log_structure["completed_tasks"] / file_name
            
            if source_path.exists():
                try:
                    shutil.move(str(source_path), str(dest_path))
                    print(f"   ✅ Arquivado: {file_name} → log/completed_tasks/")
                    archived_count += 1
                except Exception as e:
                    print(f"   ❌ Erro ao arquivar {file_name}: {e}")
        
        print(f"✅ {archived_count} tarefas arquivadas com sucesso!")
    
    def move_obsolete_files(self):
        """Move arquivos obsoletos para pasta de arquivo"""
        print("🗂️ Movendo arquivos obsoletos...")
        
        moved_count = 0
        for file_name in self.obsolete_files:
            source_path = self.wiki_dir / file_name
            dest_path = self.log_structure["archives"]["obsolete_files"] / file_name
            
            if source_path.exists():
                try:
                    shutil.move(str(source_path), str(dest_path))
                    print(f"   ✅ Movido: {file_name} → log/archives/obsolete_files/")
                    moved_count += 1
                except Exception as e:
                    print(f"   ❌ Erro ao mover {file_name}: {e}")
        
        print(f"✅ {moved_count} arquivos obsoletos movidos com sucesso!")
    
    def create_cleanup_report(self):
        """Cria relatório de limpeza"""
        print("📝 Criando relatório de limpeza...")
        
        cleanup_report = {
            "timestamp": datetime.now().isoformat(),
            "operation": "system_cleanup",
            "files_moved": {
                "reports": [],
                "completed_tasks": [],
                "obsolete_files": []
            },
            "structure_created": True,
            "status": "completed"
        }
        
        # Adiciona arquivos movidos ao relatório
        for file_name in self.report_files:
            if (self.log_structure["reports"] / file_name).exists():
                cleanup_report["files_moved"]["reports"].append(file_name)
        
        for file_name in self.completed_task_files:
            if (self.log_structure["completed_tasks"] / file_name).exists():
                cleanup_report["files_moved"]["completed_tasks"].append(file_name)
        
        for file_name in self.obsolete_files:
            if (self.log_structure["archives"]["obsolete_files"] / file_name).exists():
                cleanup_report["files_moved"]["obsolete_files"].append(file_name)
        
        # Salva relatório
        report_path = self.log_structure["reports"] / "cleanup_report.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(cleanup_report, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Relatório de limpeza salvo em: {report_path}")
        return cleanup_report
    
    def update_system_documentation(self):
        """Atualiza documentação do sistema"""
        print("📚 Atualizando documentação do sistema...")
        
        # Cria índice de arquivos de log
        log_index = {
            "timestamp": datetime.now().isoformat(),
            "structure": {
                "completed_tasks": [],
                "reports": [],
                "recipes": [],
                "archives": {
                    "obsolete_files": [],
                    "historical_data": []
                }
            }
        }
        
        # Lista arquivos em cada pasta
        for category, folder_path in self.log_structure.items():
            if isinstance(folder_path, dict):
                for subcategory, subfolder in folder_path.items():
                    if subfolder.exists():
                        files = [f.name for f in subfolder.iterdir() if f.is_file()]
                        log_index["structure"][category][subcategory] = files
            else:
                if folder_path.exists():
                    files = [f.name for f in folder_path.iterdir() if f.is_file()]
                    log_index["structure"][category] = files
        
        # Salva índice
        index_path = self.log_dir / "log_index.json"
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump(log_index, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Índice de log atualizado em: {index_path}")
    
    def cleanup_system(self):
        """Executa limpeza completa do sistema"""
        print("🧹 Iniciando limpeza do sistema...")
        print("=" * 50)
        
        try:
            # 1. Criar estrutura de pastas
            self.create_log_structure()
            
            # 2. Mover relatórios
            self.move_reports_to_log()
            
            # 3. Arquivar tarefas concluídas
            self.archive_completed_tasks()
            
            # 4. Mover arquivos obsoletos
            self.move_obsolete_files()
            
            # 5. Criar relatório de limpeza
            cleanup_report = self.create_cleanup_report()
            
            # 6. Atualizar documentação
            self.update_system_documentation()
            
            print("=" * 50)
            print("🎉 Limpeza do sistema concluída com sucesso!")
            
            # Resumo final
            print("\n📊 RESUMO DA LIMPEZA:")
            print(f"   📄 Relatórios movidos: {len(cleanup_report['files_moved']['reports'])}")
            print(f"   📋 Tarefas arquivadas: {len(cleanup_report['files_moved']['completed_tasks'])}")
            print(f"   🗂️ Arquivos obsoletos: {len(cleanup_report['files_moved']['obsolete_files'])}")
            print(f"   📁 Estrutura criada: {cleanup_report['structure_created']}")
            
            return True
            
        except Exception as e:
            print(f"❌ Erro durante limpeza: {e}")
            return False

def main():
    """Função principal"""
    print("🧹 Sistema de Limpeza e Organização")
    print("=" * 40)
    
    cleanup = SystemCleanup()
    success = cleanup.cleanup_system()
    
    if success:
        print("\n✅ Sistema limpo e organizado com sucesso!")
        print("📁 Arquivos organizados em: wiki/log/")
        print("📝 Relatórios em: wiki/log/reports/")
        print("📋 Tarefas em: wiki/log/completed_tasks/")
        print("🗂️ Arquivos obsoletos em: wiki/log/archives/obsolete_files/")
    else:
        print("\n❌ Erro durante limpeza do sistema!")

if __name__ == "__main__":
    main() 