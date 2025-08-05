from unicode_aliases import *
# Constantes
MAX_RETRIES = 8

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: file_organization_agent.py
Módulo de Destino: agents.agent_orchestrator
Data de Migração: 2025-08-01 12:21:43

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import AgentorchestratorModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File Organization Agent - Padronização e Limpeza de Arquivos
Padroniza nomenclatura de arquivos e identifica arquivos obsoletos
"""

import os
import json
import shutil
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Tuple

class FileOrganizationAgent:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent.parent.parent
        self.wiki_path = self.project_root / "wiki"
        self.bmad_path = self.wiki_path / "bmad"
        self.agents_path = self.bmad_path / "agents"
        self.log_path = self.wiki_path / "log" / "file_organization"
        self.log_path.mkdir(parents=True, exist_ok=True)
        
    def log_message(self, message, level="INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        print(log_entry)
        
        log_file = self.log_path / "file_organization.log"
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")
    
    def analyze_naming_patterns(self) -> Dict[str, Any]:
        """Analisa padrões de nomenclatura atuais"""
        self.log_message("Analisando padrões de nomenclatura...")
        
        naming_analysis = {
            "inconsistent_patterns": [],
            "obsolete_files": [],
            "duplicate_files": [],
            "recommendations": []
        }
        
        # Padrões identificados
        patterns_found = {
            "snake_case": [],      # arquivo_nome.py
            "camel_case": [],      # arquivoNome.py
            "kebab_case": [],      # arquivo-nome.py
            "mixed_case": [],      # Arquivo_Nome.py
            "uppercase": [],       # ARQUIVO.py
            "lowercase": [],       # arquivo.py
            "with_numbers": [],    # arquivo_001.py
            "with_extensions": []  # arquivo.py, arquivo.md, arquivo.json
        }
        
        # Analisar arquivos na pasta agents
        for file_path in self.agents_path.rglob("*"):
            if file_path.is_file():
                filename = file_path.name
                relative_path = file_path.relative_to(self.agents_path)
                
                # Classificar padrão
                if re.match(r'^[a-z][a-z0-9_]*$', filename):
                    patterns_found["snake_case"].append(str(relative_path))
                elif re.match(r'^[a-z][a-zA-Z0-9]*$', filename):
                    patterns_found["camel_case"].append(str(relative_path))
                elif re.match(r'^[a-z][a-z0-9-]*$', filename):
                    patterns_found["kebab_case"].append(str(relative_path))
                elif re.match(r'^[A-Z][a-zA-Z0-9_]*$', filename):
                    patterns_found["mixed_case"].append(str(relative_path))
                elif re.match(r'^[A-Z_]+$', filename):
                    patterns_found["uppercase"].append(str(relative_path))
                elif re.match(r'^[a-z]+$', filename):
                    patterns_found["lowercase"].append(str(relative_path))
                elif re.match(r'.*\d+.*', filename):
                    patterns_found["with_numbers"].append(str(relative_path))
                
                # Verificar extensões
                if file_path.suffix:
                    patterns_found["with_extensions"].append(str(relative_path))
        
        naming_analysis["patterns_found"] = patterns_found
        self.log_message(f"Padrões analisados: {len(patterns_found)} categorias")
        
        return naming_analysis
    
    def identify_obsolete_files(self) -> List[Dict[str, Any]]:
        """Identifica arquivos obsoletos"""
        self.log_message("Identificando arquivos obsoletos...")
        
        obsolete_files = []
        
        # Arquivos que podem ser obsoletos
        potential_obsolete = [
            # Arquivos .md que podem ser consolidados
            "consolidation_report.md",
            "epic_2_1_canary_analysis_task.md",
            "game_stories_priority_task.md", 
            "ui_stories_priority_task.md",
            "epic_4_4_autonomy_complete_task.md",
            "dashboard_completion_task.md",
            "task_researcher_agent.md",
            "researcher_agent.md",
            "git_automation_agent.md",
            "BMAD_Agents_Guide.md",
            
            # Arquivos .log que podem ser limpos
            "path_validator.log",
            "researcher_agent.log",
            
            # Arquivos .json que podem ser consolidados
            "consolidation_results.json",
            
            # Arquivos Python que podem ser duplicados
            "workflow_orchestrator.py",  # vs workflow_orchestrator_agent.py
            "git_automation_agent_fixed.py",  # vs git_automation_agent.py
            "python_agent.py",  # arquivo pequeno (501B)
            "start_task_supervisor.py",  # arquivo pequeno (2.9KB)
            "absolute_path_utility.py",  # pode ser integrado
            "update_orchestrator_with_python_agent.py"  # específico demais
        ]
        
        for filename in potential_obsolete:
            file_path = self.agents_path / filename
            if file_path.exists():
                file_info = {
                    "filename": filename,
                    "path": str(file_path),
                    "size": file_path.stat().st_size,
                    "modified": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat(),
                    "reason": self.get_obsolete_reason(filename),
                    "action": self.get_recommended_action(filename)
                }
                obsolete_files.append(file_info)
        
        self.log_message(f"Arquivos obsoletos identificados: {len(obsolete_files)}")
        return obsolete_files
    
    def get_obsolete_reason(self, filename: str) -> str:
        """Retorna razão para arquivo ser considerado obsoleto"""
        reasons = {
            "consolidation_report.md": "Consolidado no sistema principal",
            "epic_2_1_canary_analysis_task.md": "Task já concluída",
            "game_stories_priority_task.md": "Task já concluída",
            "ui_stories_priority_task.md": "Task já concluída",
            "epic_4_4_autonomy_complete_task.md": "Task já concluída",
            "dashboard_completion_task.md": "Task já concluída",
            "task_researcher_agent.md": "Agente já implementado",
            "researcher_agent.md": "Agente já implementado",
            "git_automation_agent.md": "Agente já implementado",
            "BMAD_Agents_Guide.md": "Documentação consolidada",
            "path_validator.log": "Log temporário",
            "researcher_agent.log": "Log temporário",
            "consolidation_results.json": "Resultados consolidados",
            "workflow_orchestrator.py": "Versão antiga do agente",
            "git_automation_agent_fixed.py": "Versão corrigida do agente original",
            "python_agent.py": "Arquivo muito pequeno (501B)",
            "start_task_supervisor.py": "Arquivo pequeno, pode ser integrado",
            "absolute_path_utility.py": "Pode ser integrado em outro agente",
            "update_orchestrator_with_python_agent.py": "Script específico demais"
        }
        return reasons.get(filename, "Arquivo não essencial")
    
    def get_recommended_action(self, filename: str) -> str:
        """Retorna ação recomendada para arquivo obsoleto"""
        actions = {
            "consolidation_report.md": "MOVER para wiki/log/archives/",
            "epic_2_1_canary_analysis_task.md": "MOVER para wiki/log/archives/",
            "game_stories_priority_task.md": "MOVER para wiki/log/archives/",
            "ui_stories_priority_task.md": "MOVER para wiki/log/archives/",
            "epic_4_4_autonomy_complete_task.md": "MOVER para wiki/log/archives/",
            "dashboard_completion_task.md": "MOVER para wiki/log/archives/",
            "task_researcher_agent.md": "MOVER para wiki/log/archives/",
            "researcher_agent.md": "MOVER para wiki/log/archives/",
            "git_automation_agent.md": "MOVER para wiki/log/archives/",
            "BMAD_Agents_Guide.md": "MOVER para wiki/docs/",
            "path_validator.log": "DELETAR",
            "researcher_agent.log": "DELETAR",
            "consolidation_results.json": "MOVER para wiki/log/archives/",
            "workflow_orchestrator.py": "DELETAR (versão antiga)",
            "git_automation_agent_fixed.py": "RENOMEAR para git_automation_agent.py",
            "python_agent.py": "DELETAR (arquivo muito pequeno)",
            "start_task_supervisor.py": "INTEGRAR em task_supervisor_agent.py",
            "absolute_path_utility.py": "INTEGRAR em comprehensive_path_validator.py",
            "update_orchestrator_with_python_agent.py": "DELETAR (script específico)"
        }
        return actions.get(filename, "REVISAR")
    
    def standardize_file_names(self) -> Dict[str, Any]:
        """Padroniza nomes de arquivos para snake_case"""
        self.log_message("Padronizando nomes de arquivos...")
        
        standardization_results = {
            "renamed_files": [],
            "failed_renames": [],
            "recommendations": []
        }
        
        # Mapeamento de renomeações
        rename_mapping = {
            "BMAD_Agents_Guide.md": "bmad_agents_guide.md",
            "git_automation_agent_fixed.py": "git_automation_agent.py",
            "workflow_orchestrator.py": "workflow_orchestrator_legacy.py"  # Marcar como legacy
        }
        
        for old_name, new_name in rename_mapping.items():
            old_path = self.agents_path / old_name
            new_path = self.agents_path / new_name
            
            if old_path.exists():
                try:
                    # Verificar se arquivo de destino já existe
                    if new_path.exists():
                        # Criar backup
                        backup_path = self.agents_path / f"{new_name}.backup"
                        shutil.move(str(new_path), str(backup_path))
                        self.log_message(f"Backup criado: {backup_path}")
                    
                    # Renomear arquivo
                    shutil.move(str(old_path), str(new_path))
                    
                    rename_info = {
                        "old_name": old_name,
                        "new_name": new_name,
                        "status": "SUCCESS"
                    }
                    standardization_results["renamed_files"].append(rename_info)
                    self.log_message(f"Arquivo renomeado: {old_name} → {new_name}")
                    
                except Exception as e:
                    rename_info = {
                        "old_name": old_name,
                        "new_name": new_name,
                        "error": str(e),
                        "status": "FAILED"
                    }
                    standardization_results["failed_renames"].append(rename_info)
                    self.log_message(f"Erro ao renomear {old_name}: {str(e)}", "ERROR")
        
        self.log_message(f"Arquivos padronizados: {len(standardization_results['renamed_files'])} renomeados")
        return standardization_results
    
    def clean_obsolete_files(self) -> Dict[str, Any]:
        """Remove arquivos obsoletos identificados"""
        self.log_message("Limpando arquivos obsoletos...")
        
        cleanup_results = {
            "deleted_files": [],
            "moved_files": [],
            "failed_operations": []
        }
        
        # Arquivos para deletar
        files_to_delete = [
            "path_validator.log",
            "researcher_agent.log",
            "python_agent.py",
            "update_orchestrator_with_python_agent.py"
        ]
        
        # Arquivos para mover para archives
        files_to_archive = [
            "consolidation_report.md",
            "epic_2_1_canary_analysis_task.md",
            "game_stories_priority_task.md",
            "ui_stories_priority_task.md",
            "epic_4_4_autonomy_complete_task.md",
            "dashboard_completion_task.md",
            "task_researcher_agent.md",
            "researcher_agent.md",
            "git_automation_agent.md",
            "consolidation_results.json"
        ]
        
        # Criar pasta de arquivos
        archives_path = self.wiki_path / "log" / "archives"
        archives_path.mkdir(parents=True, exist_ok=True)
        
        # Deletar arquivos
        for filename in files_to_delete:
            file_path = self.agents_path / filename
            if file_path.exists():
                try:
                    file_path.unlink()
                    cleanup_results["deleted_files"].append(filename)
                    self.log_message(f"Arquivo deletado: {filename}")
                except Exception as e:
                    cleanup_results["failed_operations"].append({
                        "filename": filename,
                        "operation": "DELETE",
                        "error": str(e)
                    })
                    self.log_message(f"Erro ao deletar {filename}: {str(e)}", "ERROR")
        
        # Mover arquivos para archives
        for filename in files_to_archive:
            source_path = self.agents_path / filename
            dest_path = archives_path / filename
            
            if source_path.exists():
                try:
                    shutil.move(str(source_path), str(dest_path))
                    cleanup_results["moved_files"].append(filename)
                    self.log_message(f"Arquivo movido para archives: {filename}")
                except Exception as e:
                    cleanup_results["failed_operations"].append({
                        "filename": filename,
                        "operation": "MOVE",
                        "error": str(e)
                    })
                    self.log_message(f"Erro ao mover {filename}: {str(e)}", "ERROR")
        
        self.log_message(f"Limpeza concluída: {len(cleanup_results['deleted_files'])} deletados,
    {len(cleanup_results['moved_files'])} movidos")
        return cleanup_results
    
    def validate_navigation_paths(self) -> Dict[str, Any]:
        """Valida caminhos de navegação após mudanças"""
        self.log_message("Validando caminhos de navegação...")
        
        validation_results = {
            "valid_paths": [],
            "broken_paths": [],
            "updated_references": []
        }
        
        # Verificar arquivos de configuração e regras
        config_files = [
            self.project_root / "cursor.md",
            self.wiki_path / "dashboard" / "task_master.md",
            self.wiki_path / "maps" / "wiki_map.json",
            self.wiki_path / "maps" / "tags_index.json"
        ]
        
        for config_file in config_files:
            if config_file.exists():
                try:
                    with open(config_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Verificar referências a arquivos renomeados/movidos
                    broken_references = []
                    updated_content = content
                    
                    # Verificar referências específicas
                    old_references = [
                        "git_automation_agent_fixed.py",
                        "BMAD_Agents_Guide.md",
                        "consolidation_report.md"
                    ]
                    
                    for old_ref in old_references:
                        if old_ref in content:
                            broken_references.append(old_ref)
                            # Atualizar referência
                            if old_ref == "git_automation_agent_fixed.py":
                                updated_content = updated_content.replace(old_ref, "git_automation_agent.py")
                            elif old_ref == "BMAD_Agents_Guide.md":
                                updated_content = updated_content.replace(old_ref, "bmad_agents_guide.md")
                    
                    if broken_references:
                        validation_results["broken_paths"].append({
                            "file": str(config_file),
                            "broken_references": broken_references
                        })
                        
                        # Atualizar arquivo se necessário
                        if updated_content != content:
                            with open(config_file, 'w', encoding='utf-8') as f:
                                f.write(updated_content)
                            validation_results["updated_references"].append(str(config_file))
                            self.log_message(f"Referências atualizadas em: {config_file}")
                    else:
                        validation_results["valid_paths"].append(str(config_file))
                        
                except Exception as e:
                    self.log_message(f"Erro ao validar {config_file}: {str(e)}", "ERROR")
        
        self.log_message(f"Validação concluída: {len(validation_results['valid_paths'])} caminhos válidos")
        return validation_results
    
    def generate_organization_report(self) -> Dict[str, Any]:
        """Gera relatório completo da organização"""
        self.log_message("Gerando relatório de organização...")
        
        # Coletar todos os resultados
        naming_analysis = self.analyze_naming_patterns()
        obsolete_files = self.identify_obsolete_files()
        standardization_results = self.standardize_file_names()
        cleanup_results = self.clean_obsolete_files()
        validation_results = self.validate_navigation_paths()
        
        # Relatório consolidado
        organization_report = {
            "data_geracao": datetime.now().isoformat(),
            "naming_analysis": naming_analysis,
            "obsolete_files": obsolete_files,
            "standardization_results": standardization_results,
            "cleanup_results": cleanup_results,
            "validation_results": validation_results,
            "summary": {
                "files_renamed": len(standardization_results["renamed_files"]),
                "files_deleted": len(cleanup_results["deleted_files"]),
                "files_moved": len(cleanup_results["moved_files"]),
                "paths_validated": len(validation_results["valid_paths"]),
                "references_updated": len(validation_results["updated_references"]),
                "overall_status": "ORGANIZADO"
            }
        }
        
        report_file = self.wiki_path / "bmad" / "agents" / "file_organization_report.json" # Corrected path
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(organization_report, f, indent=2, ensure_ascii=False)
        
        self.log_message(f"Relatório de organização salvo: {report_file}")
        return organization_report
    
    def execute(self):
        """Executa a organização completa de arquivos"""
        self.log_message("=== INICIANDO ORGANIZAÇÃO DE ARQUIVOS ===")
        
        try:
            # 1. Analisar padrões de nomenclatura
            naming_analysis = self.analyze_naming_patterns()
            
            # 2. Identificar arquivos obsoletos
            obsolete_files = self.identify_obsolete_files()
            
            # 3. Padronizar nomes de arquivos
            standardization_results = self.standardize_file_names()
            
            # 4. Limpar arquivos obsoletos
            cleanup_results = self.clean_obsolete_files()
            
            # 5. Validar caminhos de navegação
            validation_results = self.validate_navigation_paths()
            
            # 6. Gerar relatório completo
            organization_report = self.generate_organization_report()
            
            # Relatório final
            final_report = {
                "task": "Organização de Arquivos",
                "status": "CONCLUÍDA",
                "data_conclusao": datetime.now().isoformat(),
                "resultados": {
                    "naming_analysis": naming_analysis,
                    "obsolete_files": obsolete_files,
                    "standardization_results": standardization_results,
                    "cleanup_results": cleanup_results,
                    "validation_results": validation_results,
                    "organization_report": organization_report
                }
            }
            
            report_file = self.log_path / "file_organization_complete.json"
            with open(report_file, "w", encoding="utf-8") as f:
                json.dump(final_report, f, indent=2, ensure_ascii=False)
            
            self.log_message("=== ORGANIZAÇÃO DE ARQUIVOS CONCLUÍDA COM SUCESSO ===")
            self.log_message(f"Relatório salvo: {report_file}")
            
            return final_report
            
        except Exception as e:
            self.log_message(f"ERRO na execução: {str(e)}", "ERROR")
            return {"status": "ERRO", "erro": str(e)}

if __name__ == "__main__":
    agent = FileOrganizationAgent()
    result = agent.execute()
    print(json.dumps(result, indent=2, ensure_ascii=False)) 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = AgentorchestratorModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script file_organization_agent.py executado com sucesso via módulo agents.agent_orchestrator")
    else:
        print(f"❌ Erro na execução do script file_organization_agent.py via módulo agents.agent_orchestrator")

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
- **Nome**: migrated_file_organization_agent
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

