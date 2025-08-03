from unicode_aliases import *
# Constantes
MAX_RETRIES = 8

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: migrated_centralize_logs.py
Módulo de Destino: maps.map_updater
Data de Migração: 2025-08-01 12:21:36

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import MapupdaterModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: centralize_logs.py
Módulo de Destino: tools.log_manager
Data de Migração: 2025-08-01 12:21:34

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import LogmanagerModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Logs Centralizado
============================

Este script centraliza e organiza logs espalhados em sistema centralizado
com categorização automática e estrutura hierárquica.

Autor: Sistema BMAD - Log Organizer
Data: 2025-08-01
"""

import json
import shutil
from datetime import datetime
import logging

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class LogCentralizer:
    """Centralizador de logs BMAD"""
    
    def __init__(self, log_dir: str = "wiki/log"):
        """
        Inicializa o centralizador de logs.
        
        Args:
            log_dir: Diretório principal de logs
        """
        self.log_dir = Path(log_dir)
        self.backup_dir = self.log_dir / "backup_centralization"
        self.backup_dir.mkdir(exist_ok=True)
        
        # Estrutura de categorização
        self.log_categories = {
            "agents": {
                "description": "Logs de agentes BMAD",
                "patterns": ["*_agent.log", "*_agent_*.log"],
                "subcategories": {
                    "core_agents": ["professor_agent.log", "task_supervisor_agent.log", "quality_assurance_agent.log"],
                    "navigation_agents": ["json_navigation_agent.log", "graph_navigation_agent.log",
    "integrated_navigation_agent.log"],
                    "documentation_agents": ["documentation_agent.log", "documentation_completer.log"],
                    "module_agents": ["module_creator.log", "module_generator.log", "module_analyzer.log",
    "module_tester.log"],
                    "git_agents": ["git_automation.log", "git_automation_fixed.log"],
                    "research_agents": ["researcher_agent.log", "canary_researcher.log"],
                    "integration_agents": ["integration_agent.log", "integration_system.log"],
                    "validation_agents": ["path_validator_agent.log", "comprehensive_path_validator.log"],
                    "organization_agents": ["intelligent_organization.log", "habdel_organization.log"],
                    "analysis_agents": ["deep_source_analyzer.log", "dashboard_creation.log"]
                }
            },
            "reports": {
                "description": "Relatórios de execução",
                "patterns": ["*_report.md", "*_report.json", "*_report_*.md", "*_report_*.json"],
                "subcategories": {
                    "task_reports": ["*task*", "*Task*"],
                    "workflow_reports": ["*workflow*", "*Workflow*"],
                    "validation_reports": ["*validation*", "*Validation*"],
                    "education_reports": ["*education*", "*Education*", "*professor*", "*Professor*"],
                    "integration_reports": ["*integration*", "*Integration*"],
                    "organization_reports": ["*organization*", "*Organization*"],
                    "progress_reports": ["*progress*", "*Progress*"],
                    "analysis_reports": ["*analysis*", "*Analysis*", "*analise*", "*Analise*"]
                }
            },
            "system": {
                "description": "Logs do sistema",
                "patterns": ["auto_*.log", "auto_*.json", "script_*.json", "python_*.json"],
                "subcategories": {
                    "optimization": ["auto_optimizer.log", "auto_optimization_history.json"],
                    "script_executions": ["script_executions.json", "python_error_resolutions.json"],
                    "system_status": ["readme_status_report.json", "orchestration_report_*.json"]
                }
            },
            "archives": {
                "description": "Arquivos arquivados",
                "patterns": ["*.md", "*.json"],
                "subcategories": {
                    "plans": ["*plano*", "*Plano*", "*plan*", "*Plan*"],
                    "final_reports": ["*final*", "*Final*"],
                    "corrections": ["*correcao*", "*Correcao*", "*correction*", "*Correction*"],
                    "improvements": ["*improvement*", "*Improvement*", "*melhoria*", "*Melhoria*"]
                }
            }
        }
        
        # Estrutura de diretórios centralizada
        self.centralized_structure = {
            "agents": self.log_dir / "agents",
            "reports": self.log_dir / "reports",
            "system": self.log_dir / "system",
            "archives": self.log_dir / "archives",
            "temp": self.log_dir / "temp",
            "backup": self.log_dir / "backup"
        }
        
    def create_centralized_structure(self) -> bool:
        """Cria estrutura centralizada de logs"""
        logger.info("📁 Criando estrutura centralizada...")
        
        try:
            # Criar diretórios principais
            for category, path in self.centralized_structure.items():
                path.mkdir(exist_ok=True)
                logger.info(f"✅ Diretório criado: {path}")
            
            # Criar subcategorias
            for category_name, category_config in self.log_categories.items():
                category_path = self.centralized_structure[category_name]
                
                for subcategory in category_config.get("subcategories", {}).keys():
                    subcategory_path = category_path / subcategory
                    subcategory_path.mkdir(exist_ok=True)
                    logger.info(f"✅ Subcategoria criada: {subcategory_path}")
            
            return True
            
        except Exception as e:
            logger.error(f"Erro ao criar estrutura: {e}")
            return False
    
    def categorize_file(self, filename: str) -> Dict[str, str]:
        """Categoriza um arquivo de log"""
        filename_lower = filename.lower()
        
        for category_name, category_config in self.log_categories.items():
            # Verificar padrões da categoria
            for pattern in category_config["patterns"]:
                if self.matches_pattern(filename, pattern):
                    # Encontrar subcategoria
                    subcategory = "general"
                    for subcat_name, subcat_patterns in category_config.get("subcategories", {}).items():
                        for pattern in subcat_patterns:
                            if self.matches_pattern(filename, pattern):
                                subcategory = subcat_name
                                break
                        if subcategory != "general":
                            break
                    
                    return {
                        "category": category_name,
                        "subcategory": subcategory,
                        "description": category_config["description"]
                    }
        
        # Arquivo não categorizado
        return {
            "category": "archives",
            "subcategory": "uncategorized",
            "description": "Arquivo não categorizado"
        }
    
    def matches_pattern(self, filename: str, pattern: str) -> bool:
        """Verifica se arquivo corresponde ao padrão"""
        import fnmatch
        
        # Converter padrões simples para fnmatch
        if "*" in pattern:
            return fnmatch.fnmatch(filename, pattern)
        else:
            return filename == pattern
    
    def backup_existing_files(self) -> bool:
        """Faz backup dos arquivos existentes"""
        logger.info("💾 Fazendo backup dos arquivos existentes...")
        
        try:
            # Fazer backup de todos os arquivos no diretório de logs
            for file_path in self.log_dir.rglob("*"):
                if file_path.is_file() and file_path.parent != self.backup_dir:
                    # Criar estrutura de backup
                    relative_path = file_path.relative_to(self.log_dir)
                    backup_path = self.backup_dir / relative_path
                    backup_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    # Copiar arquivo
                    shutil.copy2(file_path, backup_path)
            
            logger.info("✅ Backup concluído")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao fazer backup: {e}")
            return False
    
    def move_file_to_category(self, file_path: Path, category: str, subcategory: str) -> bool:
        """Move arquivo para categoria apropriada"""
        try:
            # Determinar destino
            if category in self.centralized_structure:
                dest_dir = self.centralized_structure[category] / subcategory
                dest_dir.mkdir(parents=True, exist_ok=True)
                
                dest_file = dest_dir / file_path.name
                
                # Se arquivo já existe, adicionar timestamp
                if dest_file.exists():
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    name_parts = file_path.stem, timestamp, file_path.suffix
                    dest_file = dest_dir / f"{name_parts[0]}_{name_parts[1]}{name_parts[2]}"
                
                # Mover arquivo
                shutil.move(str(file_path), str(dest_file))
                logger.info(f"📁 Movido: {file_path.name} → {category}/{subcategory}/")
                return True
            else:
                logger.warning(f"Categoria não encontrada: {category}")
                return False
                
        except Exception as e:
            logger.error(f"Erro ao mover {file_path}: {e}")
            return False
    
    def centralize_logs(self) -> Dict[str, Any]:
        """Centraliza todos os logs"""
        logger.info("🚀 Iniciando centralização de logs...")
        
        # Fazer backup primeiro
        if not self.backup_existing_files():
            return {"error": "Falha no backup"}
        
        # Criar estrutura centralizada
        if not self.create_centralized_structure():
            return {"error": "Falha na criação da estrutura"}
        
        results = {
            "timestamp": datetime.now().isoformat(),
            "files_processed": 0,
            "files_categorized": 0,
            "files_moved": 0,
            "errors": [],
            "categories": {}
        }
        
        # Processar todos os arquivos
        for file_path in self.log_dir.rglob("*"):
            if file_path.is_file() and file_path.parent != self.backup_dir:
                results["files_processed"] += 1
                
                try:
                    # Categorizar arquivo
                    categorization = self.categorize_file(file_path.name)
                    category = categorization["category"]
                    subcategory = categorization["subcategory"]
                    
                    # Registrar categoria
                    if category not in results["categories"]:
                        results["categories"][category] = {}
                    if subcategory not in results["categories"][category]:
                        results["categories"][category][subcategory] = []
                    
                    results["categories"][category][subcategory].append(file_path.name)
                    results["files_categorized"] += 1
                    
                    # Mover arquivo
                    if self.move_file_to_category(file_path, category, subcategory):
                        results["files_moved"] += 1
                    else:
                        results["errors"].append(f"Falha ao mover: {file_path.name}")
                
                except Exception as e:
                    error_msg = f"Erro ao processar {file_path.name}: {e}"
                    results["errors"].append(error_msg)
                    logger.error(error_msg)
        
        # Criar índice centralizado
        self.create_centralized_index(results)
        
        logger.info(f"✅ Centralização concluída!")
        logger.info(f"📊 Arquivos processados: {results['files_processed']}")
        logger.info(f"📊 Arquivos categorizados: {results['files_categorized']}")
        logger.info(f"📊 Arquivos movidos: {results['files_moved']}")
        
        return results
    
    def create_centralized_index(self, results: Dict[str, Any]) -> bool:
        """Cria índice centralizado dos logs"""
        try:
            index_data = {
                "timestamp": datetime.now().isoformat(),
                "total_files": results["files_processed"],
                "categories": results["categories"],
                "structure": {
                    "agents": "Logs de agentes BMAD",
                    "reports": "Relatórios de execução",
                    "system": "Logs do sistema",
                    "archives": "Arquivos arquivados",
                    "temp": "Arquivos temporários",
                    "backup": "Backups"
                }
            }
            
            # Salvar índice
            index_file = self.log_dir / "centralized_logs_index.json"
            with open(index_file, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
            
            logger.info(f"📋 Índice centralizado criado: {index_file}")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao criar índice: {e}")
            return False
    
    def generate_centralization_report(self, results: Dict[str, Any]) -> str:
        """Gera relatório de centralização"""
        report = f"""# Relatório de Centralização de Logs

## 📊 Resumo da Centralização

- **Data**: {results['timestamp']}
- **Arquivos Processados**: {results['files_processed']}
- **Arquivos Categorizados**: {results['files_categorized']}
- **Arquivos Movidos**: {results['files_moved']}

## 📁 Estrutura Centralizada

### Agents
Logs de agentes BMAD organizados por especialização.

### Reports
Relatórios de execução categorizados por tipo.

### System
Logs do sistema e automações.

### Archives
Arquivos arquivados e históricos.

### Temp
Arquivos temporários.

### Backup
Backups de segurança.

## 📋 Categorização Detalhada

"""
        
        for category, subcategories in results["categories"].items():
            report += f"### {category.title()}\n\n"
            for subcategory, files in subcategories.items():
                report += f"#### {subcategory.replace('_', ' ').title()}\n"
                report += f"- Arquivos: {len(files)}\n"
                for file in files[:5]:  # Mostrar apenas os primeiros 5
                    report += f"  - {file}\n"
                if len(files) > 5:
                    report += f"  - ... e mais {len(files) - 5} arquivos\n"
                report += "\n"
        
        if results["errors"]:
            report += "## ❌ Erros\n\n"
            for error in results["errors"]:
                report += f"- {error}\n"
        
        report += f"""
## 📁 Backup

Todos os arquivos originais foram salvos em: `wiki/log/backup_centralization/`

## 🎯 Resultado

A centralização organizou **{results['files_processed']}** arquivos em estrutura hierárquica,
facilitando navegação e manutenção dos logs do sistema BMAD.
"""
        
        return report

def main():
    """Função principal"""
    print("🚀 Sistema de Logs Centralizado")
    print("=" * 50)
    
    centralizer = LogCentralizer()
    
    # Centralizar logs
    results = centralizer.centralize_logs()
    
    if "error" in results:
        print(f"❌ Erro: {results['error']}")
        return
    
    # Gerar relatório
    report = centralizer.generate_centralization_report(results)
    
    # Salvar relatório
    report_file = centralizer.log_dir / "centralization_report.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    # Salvar resultados JSON
    results_file = centralizer.log_dir / "centralization_results.json"
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n📋 Relatório salvo em: {report_file}")
    print(f"📊 Resultados salvos em: {results_file}")
    
    print(f"\n📊 Resumo:")
    print(f"   Arquivos processados: {results['files_processed']}")
    print(f"   Arquivos categorizados: {results['files_categorized']}")
    print(f"   Arquivos movidos: {results['files_moved']}")
    print(f"   Categorias criadas: {len(results['categories'])}")
    
    print("✅ Sistema de logs centralizado implementado!")

if __name__ == "__main__":
    main() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = LogmanagerModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script centralize_logs.py executado com sucesso via módulo tools.log_manager")
    else:
        print(f"❌ Erro na execução do script centralize_logs.py via módulo tools.log_manager")


# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = MapupdaterModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script migrated_centralize_logs.py executado com sucesso via módulo maps.map_updater")
    else:
        print(f"❌ Erro na execução do script migrated_centralize_logs.py via módulo maps.map_updater")
