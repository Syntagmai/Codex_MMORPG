#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from unicode_aliases import *
"""
Folder Restructure Agent
========================

Agente para reestruturação de pastas do projeto Codex MMORPG.
Remove resquícios de sistemas antigos e organiza tudo no sistema unificado.

Autor: Sistema BMAD - Codex MMORPG
Versão: 1.0.0
Data: 2025-08-01
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime
import logging

class FolderRestructureAgent:
    """Agente para reestruturação de pastas"""
    
    def __init__(self):
        self.project_root = Path.cwd()
        self.wiki_update = self.project_root / "wiki" / "update"
        self.legacy_tools = self.wiki_update / "legacy_tools"
        self.restructure_log = []
        
        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
    def log_action(self, action: str, details: str):
        """Registra uma ação no log de reestruturação"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "details": details
        }
        self.restructure_log.append(entry)
        self.logger.info(f"{action}: {details}")
        
    def analyze_legacy_folders(self):
        """Analisa pastas legadas que precisam ser reorganizadas"""
        self.logger.info("🔍 Analisando pastas legadas...")
        
        legacy_analysis = {
            "generated": {
                "path": self.project_root / "generated",
                "status": "obsolete",
                "description": "Ferramentas antigas não integradas ao sistema atual",
                "files": [],
                "action": "migrate_useful_content"
            },
            "scripts": {
                "path": self.project_root / "scripts",
                "status": "obsolete",
                "description": "Scripts antigos migrados para wiki/update",
                "files": [],
                "action": "migrate_useful_content"
            },
            "modules": {
                "path": self.project_root / "modules",
                "status": "obsolete",
                "description": "Módulos de jogo antigos não integrados",
                "files": [],
                "action": "remove"
            },
            "docs": {
                "path": self.project_root / "docs",
                "status": "duplicate",
                "description": "Documentação duplicada da wiki principal",
                "files": [],
                "action": "consolidate"
            }
        }
        
        # Analisar conteúdo de cada pasta
        for folder_name, folder_info in legacy_analysis.items():
            folder_path = folder_info["path"]
            if folder_path.exists():
                folder_info["files"] = [f.name for f in folder_path.rglob("*") if f.is_file()]
                self.logger.info(f"📁 {folder_name}: {len(folder_info['files'])} arquivos encontrados")
            else:
                self.logger.info(f"📁 {folder_name}: Pasta não encontrada")
                
        return legacy_analysis
        
    def migrate_useful_content(self, source_path: Path, target_path: Path):
        """Migra conteúdo útil para o sistema unificado"""
        if not source_path.exists():
            return
            
        self.logger.info(f"📦 Migrando conteúdo útil de {source_path.name}...")
        
        # Criar pasta de destino se não existir
        target_path.mkdir(parents=True, exist_ok=True)
        
        # Migrar arquivos úteis
        for file_path in source_path.rglob("*"):
            if file_path.is_file():
                # Determinar se o arquivo é útil
                if self.is_useful_file(file_path):
                    relative_path = file_path.relative_to(source_path)
                    target_file = target_path / relative_path
                    
                    # Criar diretório de destino se necessário
                    target_file.parent.mkdir(parents=True, exist_ok=True)
                    
                    # Copiar arquivo
                    shutil.copy2(file_path, target_file)
                    self.log_action("migrate", f"Migrado: {file_path} -> {target_file}")
                    
    def is_useful_file(self, file_path: Path) -> bool:
        """Determina se um arquivo é útil para migração"""
        useful_extensions = {'.py', '.md', '.json', '.txt', '.yml', '.yaml'}
        useful_names = {'README', 'LICENSE', 'requirements', 'setup'}
        
        # Verificar extensão
        if file_path.suffix.lower() in useful_extensions:
            return True
            
        # Verificar nome do arquivo
        if any(name in file_path.stem.lower() for name in useful_names):
            return True
            
        return False
        
    def remove_obsolete_folders(self, folders_to_remove: list):
        """Remove pastas obsoletas"""
        for folder_name in folders_to_remove:
            folder_path = self.project_root / folder_name
            if folder_path.exists():
                self.logger.info(f"🗑️ Removendo pasta obsoleta: {folder_name}")
                shutil.rmtree(folder_path)
                self.log_action("remove", f"Removida pasta: {folder_name}")
                
    def consolidate_documentation(self):
        """Consolida documentação duplicada"""
        docs_path = self.project_root / "docs"
        wiki_path = self.project_root / "wiki"
        
        if docs_path.exists():
            self.logger.info("📚 Consolidando documentação...")
            
            # Mover conteúdo útil para wiki
            for file_path in docs_path.rglob("*"):
                if file_path.is_file() and file_path.suffix == '.md':
                    relative_path = file_path.relative_to(docs_path)
                    target_file = wiki_path / "legacy_docs" / relative_path
                    
                    # Criar diretório de destino
                    target_file.parent.mkdir(parents=True, exist_ok=True)
                    
                    # Copiar arquivo
                    shutil.copy2(file_path, target_file)
                    self.log_action("consolidate", f"Consolidado: {file_path} -> {target_file}")
                    
    def create_clean_structure(self):
        """Cria estrutura limpa e organizada"""
        self.logger.info("🏗️ Criando estrutura limpa...")
        
        # Estrutura ideal
        clean_structure = {
            "wiki": {
                "description": "Sistema unificado principal",
                "subfolders": ["update", "bmad", "dashboard", "maps", "docs"]
            },
            ".cursor": {
                "description": "Regras e configurações do assistente",
                "subfolders": ["rules"]
            },
            "canary": {
                "description": "Código-fonte Canary",
                "subfolders": []
            },
            "otclient": {
                "description": "Código-fonte OTClient",
                "subfolders": []
            }
        }
        
        # Criar estrutura
        for folder_name, folder_info in clean_structure.items():
            folder_path = self.project_root / folder_name
            if not folder_path.exists():
                folder_path.mkdir(exist_ok=True)
                self.log_action("create", f"Criada pasta: {folder_name}")
                
    def generate_restructure_report(self):
        """Gera relatório da reestruturação"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "agent": "FolderRestructureAgent",
            "version": "1.0.0",
            "actions": self.restructure_log,
            "summary": {
                "total_actions": len(self.restructure_log),
                "migrations": len([a for a in self.restructure_log if a["action"] == "migrate"]),
                "removals": len([a for a in self.restructure_log if a["action"] == "remove"]),
                "consolidations": len([a for a in self.restructure_log if a["action"] == "consolidate"])
            }
        }
        
        # Salvar relatório
        report_path = self.wiki_update / "restructure_report.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
            
        self.logger.info(f"📊 Relatório salvo em: {report_path}")
        return report
        
    def execute_restructure(self):
        """Executa a reestruturação completa"""
        self.logger.info("🚀 Iniciando reestruturação de pastas...")
        
        try:
            # 1. Analisar pastas legadas
            legacy_analysis = self.analyze_legacy_folders()
            
            # 2. Migrar conteúdo útil
            self.migrate_useful_content(
                self.project_root / "generated",
                self.legacy_tools
            )
            
            self.migrate_useful_content(
                self.project_root / "scripts",
                self.wiki_update
            )
            
            # 3. Consolidar documentação
            self.consolidate_documentation()
            
            # 4. Remover pastas obsoletas
            folders_to_remove = ["generated", "scripts", "modules"]
            self.remove_obsolete_folders(folders_to_remove)
            
            # 5. Criar estrutura limpa
            self.create_clean_structure()
            
            # 6. Gerar relatório
            report = self.generate_restructure_report()
            
            self.logger.info("✅ Reestruturação concluída com sucesso!")
            return report
            
        except Exception as e:
            self.logger.error(f"❌ Erro durante reestruturação: {e}")
            raise

def main():
    """Função principal"""
    agent = FolderRestructureAgent()
    report = agent.execute_restructure()
    
    print("\n" + "="*60)
    print("📊 RELATÓRIO DE REESTRUTURAÇÃO")
    print("="*60)
    print(f"📅 Data: {report['timestamp']}")
    print(f"🤖 Agente: {report['agent']} v{report['version']}")
    print(f"📈 Total de ações: {report['summary']['total_actions']}")
    print(f"📦 Migrações: {report['summary']['migrations']}")
    print(f"🗑️ Remoções: {report['summary']['removals']}")
    print(f"📚 Consolidações: {report['summary']['consolidations']}")
    print("="*60)

if __name__ == "__main__":
    main() 