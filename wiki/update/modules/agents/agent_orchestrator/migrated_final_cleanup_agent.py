from unicode_aliases import *
# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: final_cleanup_agent.py
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
Final Cleanup Agent - Limpeza Final e Integração
Realiza os últimos passos de organização e integração de arquivos
"""

import os
import json
import shutil
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any

class FinalCleanupAgent:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent.parent.parent
        self.wiki_path = self.project_root / "wiki"
        self.bmad_path = self.wiki_path / "bmad"
        self.agents_path = self.bmad_path / "agents"
        self.log_path = self.wiki_path / "log" / "final_cleanup"
        self.log_path.mkdir(parents=True, exist_ok=True)
        
    def log_message(self, message, level="INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        print(log_entry)
        
        log_file = self.log_path / "final_cleanup.log"
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")
    
    def clean_pycache(self) -> Dict[str, Any]:
        """Remove pastas __pycache__"""
        self.log_message("Limpando pastas __pycache__...")
        
        cleanup_results = {
            "removed_dirs": [],
            "failed_removals": [],
            "space_freed": 0
        }
        
        # Encontrar todas as pastas __pycache__
        pycache_dirs = list(self.agents_path.rglob("__pycache__"))
        
        for pycache_dir in pycache_dirs:
            try:
                # Calcular tamanho antes de remover
                total_size = sum(f.stat().st_size for f in pycache_dir.rglob('*') if f.is_file())
                
                # Remover pasta
                shutil.rmtree(pycache_dir)
                
                cleanup_results["removed_dirs"].append(str(pycache_dir))
                cleanup_results["space_freed"] += total_size
                
                self.log_message(f"Pasta removida: {pycache_dir}")
                
            except Exception as e:
                cleanup_results["failed_removals"].append({
                    "dir": str(pycache_dir),
                    "error": str(e)
                })
                self.log_message(f"Erro ao remover {pycache_dir}: {str(e)}", "ERROR")
        
        # Converter bytes para MB
        space_mb = cleanup_results["space_freed"] / (1024 * 1024)
        self.log_message(f"Limpeza concluída: {len(cleanup_results['removed_dirs'])} pastas removidas,
    {space_mb:.2f} MB liberados")
        
        return cleanup_results
    
    def integrate_start_task_supervisor(self) -> Dict[str, Any]:
        """Integra start_task_supervisor.py em task_supervisor_agent.py"""
        self.log_message("Integrando start_task_supervisor.py em task_supervisor_agent.py...")
        
        integration_results = {
            "integration_success": False,
            "backup_created": False,
            "content_added": False,
            "original_removed": False
        }
        
        start_supervisor_path = self.agents_path / "start_task_supervisor.py"
        task_supervisor_path = self.agents_path / "task_supervisor_agent.py"
        
        if not start_supervisor_path.exists():
            self.log_message("Arquivo start_task_supervisor.py não encontrado", "WARNING")
            return integration_results
        
        try:
            # Ler conteúdo do start_task_supervisor
            with open(start_supervisor_path, 'r', encoding='utf-8') as f:
                start_content = f.read()
            
            # Criar backup do task_supervisor_agent
            backup_path = self.agents_path / "task_supervisor_agent.py.backup"
            shutil.copy2(task_supervisor_path, backup_path)
            integration_results["backup_created"] = True
            self.log_message(f"Backup criado: {backup_path}")
            
            # Ler conteúdo atual do task_supervisor_agent
            with open(task_supervisor_path, 'r', encoding='utf-8') as f:
                task_content = f.read()
            
            # Adicionar funcionalidade do start_task_supervisor
            integration_marker = "# === INTEGRATED FROM start_task_supervisor.py ===\n"
            
            # Extrair funções úteis do start_task_supervisor
            useful_functions = []
            lines = start_content.split('\n')
            in_function = False
            current_function = []
            
            for line in lines:
                if line.strip().startswith('def ') and ':' in line:
                    in_function = True
                    current_function = [line]
                elif in_function:
                    current_function.append(line)
                    if line.strip() == '' or (line.strip() and not line.startswith(' ') and not line.startswith('\t')):
                        # Fim da função
                        useful_functions.append('\n'.join(current_function[:-1]))
                        current_function = []
                        in_function = False
            
            if current_function:
                useful_functions.append('\n'.join(current_function))
            
            # Adicionar funções ao task_supervisor_agent
            if useful_functions:
                new_content = task_content + "\n\n" + integration_marker + "\n".join(useful_functions)
                
                with open(task_supervisor_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                integration_results["content_added"] = True
                self.log_message(f"Funções integradas: {len(useful_functions)} funções adicionadas")
            
            # Remover arquivo original
            start_supervisor_path.unlink()
            integration_results["original_removed"] = True
            integration_results["integration_success"] = True
            
            self.log_message("Integração concluída com sucesso")
            
        except Exception as e:
            self.log_message(f"Erro na integração: {str(e)}", "ERROR")
        
        return integration_results
    
    def integrate_absolute_path_utility(self) -> Dict[str, Any]:
        """Integra absolute_path_utility.py em comprehensive_path_validator.py"""
        self.log_message("Integrando absolute_path_utility.py em comprehensive_path_validator.py...")
        
        integration_results = {
            "integration_success": False,
            "backup_created": False,
            "content_added": False,
            "original_removed": False
        }
        
        utility_path = self.agents_path / "absolute_path_utility.py"
        validator_path = self.agents_path / "comprehensive_path_validator.py"
        
        if not utility_path.exists():
            self.log_message("Arquivo absolute_path_utility.py não encontrado", "WARNING")
            return integration_results
        
        try:
            # Ler conteúdo do utility
            with open(utility_path, 'r', encoding='utf-8') as f:
                utility_content = f.read()
            
            # Criar backup do validator
            backup_path = self.agents_path / "comprehensive_path_validator.py.backup"
            shutil.copy2(validator_path, backup_path)
            integration_results["backup_created"] = True
            self.log_message(f"Backup criado: {backup_path}")
            
            # Ler conteúdo atual do validator
            with open(validator_path, 'r', encoding='utf-8') as f:
                validator_content = f.read()
            
            # Adicionar funcionalidade do utility
            integration_marker = "# === INTEGRATED FROM absolute_path_utility.py ===\n"
            
            # Extrair funções úteis do utility
            useful_functions = []
            lines = utility_content.split('\n')
            in_function = False
            current_function = []
            
            for line in lines:
                if line.strip().startswith('def ') and ':' in line:
                    in_function = True
                    current_function = [line]
                elif in_function:
                    current_function.append(line)
                    if line.strip() == '' or (line.strip() and not line.startswith(' ') and not line.startswith('\t')):
                        # Fim da função
                        useful_functions.append('\n'.join(current_function[:-1]))
                        current_function = []
                        in_function = False
            
            if current_function:
                useful_functions.append('\n'.join(current_function))
            
            # Adicionar funções ao validator
            if useful_functions:
                new_content = validator_content + "\n\n" + integration_marker + "\n".join(useful_functions)
                
                with open(validator_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                integration_results["content_added"] = True
                self.log_message(f"Funções integradas: {len(useful_functions)} funções adicionadas")
            
            # Remover arquivo original
            utility_path.unlink()
            integration_results["original_removed"] = True
            integration_results["integration_success"] = True
            
            self.log_message("Integração concluída com sucesso")
            
        except Exception as e:
            self.log_message(f"Erro na integração: {str(e)}", "ERROR")
        
        return integration_results
    
    def clean_backup_consolidation(self) -> Dict[str, Any]:
        """Limpa pasta backup_consolidation (opcional)"""
        self.log_message("Limpando pasta backup_consolidation...")
        
        cleanup_results = {
            "removed_files": [],
            "failed_removals": [],
            "space_freed": 0,
            "backup_created": False
        }
        
        backup_path = self.agents_path / "backup_consolidation"
        
        if not backup_path.exists():
            self.log_message("Pasta backup_consolidation não encontrada", "WARNING")
            return cleanup_results
        
        try:
            # Criar backup da pasta antes de limpar
            backup_backup_path = self.wiki_path / "log" / "archives" / "backup_consolidation_backup"
            shutil.copytree(backup_path, backup_backup_path)
            cleanup_results["backup_created"] = True
            self.log_message(f"Backup da pasta criado: {backup_backup_path}")
            
            # Calcular tamanho antes de remover
            total_size = sum(f.stat().st_size for f in backup_path.rglob('*') if f.is_file())
            
            # Remover pasta
            shutil.rmtree(backup_path)
            
            cleanup_results["space_freed"] = total_size
            self.log_message(f"Pasta backup_consolidation removida")
            
        except Exception as e:
            cleanup_results["failed_removals"].append({
                "path": str(backup_path),
                "error": str(e)
            })
            self.log_message(f"Erro ao remover backup_consolidation: {str(e)}", "ERROR")
        
        # Converter bytes para MB
        space_mb = cleanup_results["space_freed"] / (1024 * 1024)
        self.log_message(f"Limpeza concluída: {space_mb:.2f} MB liberados")
        
        return cleanup_results
    
    def validate_final_structure(self) -> Dict[str, Any]:
        """Valida estrutura final após limpeza"""
        self.log_message("Validando estrutura final...")
        
        validation_results = {
            "total_files": 0,
            "total_dirs": 0,
            "file_types": {},
            "structure_clean": True,
            "issues_found": []
        }
        
        # Contar arquivos e pastas
        for item in self.agents_path.rglob("*"):
            if item.is_file():
                validation_results["total_files"] += 1
                ext = item.suffix.lower()
                validation_results["file_types"][ext] = validation_results["file_types"].get(ext, 0) + 1
            elif item.is_dir():
                validation_results["total_dirs"] += 1
        
        # Verificar se ainda existem arquivos que deveriam ter sido removidos
        problematic_files = [
            "start_task_supervisor.py",
            "absolute_path_utility.py",
            "python_agent.py",
            "update_orchestrator_with_python_agent.py"
        ]
        
        for file_name in problematic_files:
            file_path = self.agents_path / file_name
            if file_path.exists():
                validation_results["issues_found"].append(f"Arquivo ainda existe: {file_name}")
                validation_results["structure_clean"] = False
        
        # Verificar se __pycache__ ainda existe
        pycache_dirs = list(self.agents_path.rglob("__pycache__"))
        if pycache_dirs:
            validation_results["issues_found"].append(f"Pastas __pycache__ ainda existem: {len(pycache_dirs)}")
            validation_results["structure_clean"] = False
        
        self.log_message(f"Validação concluída: {validation_results['total_files']} arquivos,
    {validation_results['total_dirs']} pastas")
        
        return validation_results
    
    def generate_final_report(self) -> Dict[str, Any]:
        """Gera relatório final da limpeza"""
        self.log_message("Gerando relatório final...")
        
        # Coletar todos os resultados
        pycache_cleanup = self.clean_pycache()
        start_supervisor_integration = self.integrate_start_task_supervisor()
        utility_integration = self.integrate_absolute_path_utility()
        backup_cleanup = self.clean_backup_consolidation()
        final_validation = self.validate_final_structure()
        
        # Relatório consolidado
        final_report = {
            "data_geracao": datetime.now().isoformat(),
            "pycache_cleanup": pycache_cleanup,
            "start_supervisor_integration": start_supervisor_integration,
            "utility_integration": utility_integration,
            "backup_cleanup": backup_cleanup,
            "final_validation": final_validation,
            "summary": {
                "space_freed_mb": (pycache_cleanup["space_freed"] + backup_cleanup["space_freed"]) / (1024 * 1024),
                "files_integrated": 2 if start_supervisor_integration["integration_success"] and utility_integration["integration_success"] else 0,
    
    
    
                "structure_clean": final_validation["structure_clean"],
                "total_files_remaining": final_validation["total_files"],
                "overall_status": "LIMPO" if final_validation["structure_clean"] else "PRECISA_ATENÇÃO"
            }
        }
        
        report_file = self.agents_path / "final_cleanup_report.json"
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(final_report, f, indent=2, ensure_ascii=False)
        
        self.log_message(f"Relatório final salvo: {report_file}")
        return final_report
    
    def execute(self):
        """Executa a limpeza final completa"""
        self.log_message("=== INICIANDO LIMPEZA FINAL ===")
        
        try:
            # 1. Limpar __pycache__
            pycache_cleanup = self.clean_pycache()
            
            # 2. Integrar start_task_supervisor
            start_supervisor_integration = self.integrate_start_task_supervisor()
            
            # 3. Integrar absolute_path_utility
            utility_integration = self.integrate_absolute_path_utility()
            
            # 4. Limpar backup_consolidation
            backup_cleanup = self.clean_backup_consolidation()
            
            # 5. Validar estrutura final
            final_validation = self.validate_final_structure()
            
            # 6. Gerar relatório final
            final_report = self.generate_final_report()
            
            # Relatório final
            complete_report = {
                "task": "Limpeza Final e Integração",
                "status": "CONCLUÍDA",
                "data_conclusao": datetime.now().isoformat(),
                "resultados": {
                    "pycache_cleanup": pycache_cleanup,
                    "start_supervisor_integration": start_supervisor_integration,
                    "utility_integration": utility_integration,
                    "backup_cleanup": backup_cleanup,
                    "final_validation": final_validation,
                    "final_report": final_report
                }
            }
            
            report_file = self.log_path / "final_cleanup_complete.json"
            with open(report_file, "w", encoding="utf-8") as f:
                json.dump(complete_report, f, indent=2, ensure_ascii=False)
            
            self.log_message("=== LIMPEZA FINAL CONCLUÍDA COM SUCESSO ===")
            self.log_message(f"Relatório salvo: {report_file}")
            
            return complete_report
            
        except Exception as e:
            self.log_message(f"ERRO na execução: {str(e)}", "ERROR")
            return {"status": "ERRO", "erro": str(e)}

if __name__ == "__main__":
    agent = FinalCleanupAgent()
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
        print(f"✅ Script final_cleanup_agent.py executado com sucesso via módulo agents.agent_orchestrator")
    else:
        print(f"❌ Erro na execução do script final_cleanup_agent.py via módulo agents.agent_orchestrator")

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
- **Nome**: migrated_final_cleanup_agent
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

