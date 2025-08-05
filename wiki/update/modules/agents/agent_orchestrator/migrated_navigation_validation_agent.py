from unicode_aliases import *
# Constantes
MAX_RETRIES = 8

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: navigation_validation_agent.py
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
Navigation Validation Agent - Validação de Navegação
Valida caminhos de navegação após reorganização de arquivos
"""

import json
import re
from datetime import datetime

class NavigationValidationAgent:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent.parent.parent
        self.wiki_path = self.project_root / "wiki"
        self.bmad_path = self.wiki_path / "bmad"
        self.agents_path = self.bmad_path / "agents"
        self.log_path = self.wiki_path / "log" / "navigation_validation"
        self.log_path.mkdir(parents=True, exist_ok=True)
        
    def log_message(self, message, level="INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        print(log_entry)
        
        log_file = self.log_path / "navigation_validation.log"
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")
    
    def validate_file_references(self) -> Dict[str, Any]:
        """Valida referências a arquivos em documentos e scripts"""
        self.log_message("Validando referências a arquivos...")
        
        validation_results = {
            "valid_references": [],
            "broken_references": [],
            "updated_references": []
        }
        
        # Arquivos que foram renomeados/movidos
        file_changes = {
            "git_automation_agent_fixed.py": "git_automation_agent.py",
            "BMAD_Agents_Guide.md": "bmad_agents_guide.md",
            "workflow_orchestrator.py": "workflow_orchestrator_legacy.py"
        }
        
        # Arquivos que foram movidos para archives
        archived_files = [
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
        
        # Arquivos que foram deletados
        deleted_files = [
            "path_validator.log",
            "researcher_agent.log",
            "python_agent.py",
            "update_orchestrator_with_python_agent.py"
        ]
        
        # Verificar arquivos de configuração
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
                    
                    # Verificar referências quebradas
                    broken_refs = []
                    updated_content = content
                    
                    # Verificar arquivos renomeados
                    for old_name, new_name in file_changes.items():
                        if old_name in content:
                            broken_refs.append(f"{old_name} → {new_name}")
                            updated_content = updated_content.replace(old_name, new_name)
                    
                    # Verificar arquivos movidos para archives
                    for archived_file in archived_files:
                        if archived_file in content:
                            broken_refs.append(f"{archived_file} → archives/{archived_file}")
                            # Atualizar para referência de archives
                            updated_content = updated_content.replace(
                                archived_file, 
                                f"wiki/log/archives/{archived_file}"
                            )
                    
                    # Verificar arquivos deletados
                    for deleted_file in deleted_files:
                        if deleted_file in content:
                            broken_refs.append(f"{deleted_file} → DELETED")
                            # Remover referência ou comentar
                            updated_content = updated_content.replace(
                                deleted_file, 
                                f"# {deleted_file} (DELETED)"
                            )
                    
                    if broken_refs:
                        validation_results["broken_references"].append({
                            "file": str(config_file),
                            "broken_refs": broken_refs
                        })
                        
                        # Atualizar arquivo se necessário
                        if updated_content != content:
                            with open(config_file, 'w', encoding='utf-8') as f:
                                f.write(updated_content)
                            validation_results["updated_references"].append(str(config_file))
                            self.log_message(f"Referências atualizadas em: {config_file}")
                    else:
                        validation_results["valid_references"].append(str(config_file))
                        
                except Exception as e:
                    self.log_message(f"Erro ao validar {config_file}: {str(e)}", "ERROR")
        
        self.log_message(f"Referências validadas: {len(validation_results['valid_references'])} válidas")
        return validation_results
    
    def validate_import_statements(self) -> Dict[str, Any]:
        """Valida statements de import em arquivos Python"""
        self.log_message("Validando statements de import...")
        
        import_validation = {
            "valid_imports": [],
            "broken_imports": [],
            "updated_imports": []
        }
        
        # Verificar imports em todos os arquivos Python
        for py_file in self.agents_path.rglob("*.py"):
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Encontrar imports
                import_lines = re.findall(r'^(?:from|import)\s+([^\s]+)', content, re.MULTILINE)
                
                broken_imports = []
                updated_content = content
                
                for import_line in import_lines:
                    # Verificar se o módulo importado ainda existe
                    module_path = import_line.replace('.', '/')
                    
                    # Verificar se é um import local
                    if not import_line.startswith(('os', 'json', 'sys', 'datetime', 'pathlib', 'typing')):
                        # Verificar se o arquivo existe
                        potential_paths = [
                            self.agents_path / f"{module_path}.py",
                            self.agents_path / module_path / "__init__.py"
                        ]
                        
                        if not any(path.exists() for path in potential_paths):
                            # Verificar se foi renomeado
                            old_to_new = {
                                "git_automation_agent_fixed": "git_automation_agent",
                                "workflow_orchestrator": "workflow_orchestrator_agent"
                            }
                            
                            for old_name, new_name in old_to_new.items():
                                if old_name in import_line:
                                    broken_imports.append(f"{import_line} → {import_line.replace(old_name, new_name)}")
                                    updated_content = updated_content.replace(old_name, new_name)
                                    break
                            else:
                                broken_imports.append(f"{import_line} → NOT_FOUND")
                
                if broken_imports:
                    import_validation["broken_imports"].append({
                        "file": str(py_file),
                        "broken_imports": broken_imports
                    })
                    
                    # Atualizar arquivo se necessário
                    if updated_content != content:
                        with open(py_file, 'w', encoding='utf-8') as f:
                            f.write(updated_content)
                        import_validation["updated_imports"].append(str(py_file))
                        self.log_message(f"Imports atualizados em: {py_file}")
                else:
                    import_validation["valid_imports"].append(str(py_file))
                    
            except Exception as e:
                self.log_message(f"Erro ao validar imports em {py_file}: {str(e)}", "ERROR")
        
        self.log_message(f"Imports validados: {len(import_validation['valid_imports'])} válidos")
        return import_validation
    
    def validate_json_references(self) -> Dict[str, Any]:
        """Valida referências em arquivos JSON"""
        self.log_message("Validando referências em arquivos JSON...")
        
        json_validation = {
            "valid_jsons": [],
            "broken_jsons": [],
            "updated_jsons": []
        }
        
        # Verificar arquivos JSON
        json_files = [
            self.wiki_path / "maps" / "wiki_map.json",
            self.wiki_path / "maps" / "tags_index.json",
            self.agents_path / "file_organization_report.json"
        ]
        
        for json_file in json_files:
            if json_file.exists():
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    # Converter para string para busca
                    json_str = json.dumps(data, ensure_ascii=False)
                    
                    broken_refs = []
                    updated_data = data
                    
                    # Verificar referências a arquivos renomeados/movidos
                    file_changes = {
                        "git_automation_agent_fixed.py": "git_automation_agent.py",
                        "BMAD_Agents_Guide.md": "bmad_agents_guide.md",
                        "workflow_orchestrator.py": "workflow_orchestrator_legacy.py"
                    }
                    
                    for old_name, new_name in file_changes.items():
                        if old_name in json_str:
                            broken_refs.append(f"{old_name} → {new_name}")
                            # Atualizar no JSON
                            updated_data = self.update_json_references(updated_data, old_name, new_name)
                    
                    if broken_refs:
                        json_validation["broken_jsons"].append({
                            "file": str(json_file),
                            "broken_refs": broken_refs
                        })
                        
                        # Salvar JSON atualizado
                        with open(json_file, 'w', encoding='utf-8') as f:
                            json.dump(updated_data, f, indent=2, ensure_ascii=False)
                        json_validation["updated_jsons"].append(str(json_file))
                        self.log_message(f"JSON atualizado: {json_file}")
                    else:
                        json_validation["valid_jsons"].append(str(json_file))
                        
                except Exception as e:
                    self.log_message(f"Erro ao validar JSON {json_file}: {str(e)}", "ERROR")
        
        self.log_message(f"JSONs validados: {len(json_validation['valid_jsons'])} válidos")
        return json_validation
    
    def update_json_references(self, data: Any, old_name: str, new_name: str) -> Any:
        """Atualiza referências em estrutura JSON"""
        if isinstance(data, dict):
            return {k: self.update_json_references(v, old_name, new_name) for k, v in data.items()}
        elif isinstance(data, list):
            return [self.update_json_references(item, old_name, new_name) for item in data]
        elif isinstance(data, str):
            return data.replace(old_name, new_name)
        else:
            return data
    
    def validate_execution_paths(self) -> Dict[str, Any]:
        """Valida caminhos de execução em scripts"""
        self.log_message("Validando caminhos de execução...")
        
        execution_validation = {
            "valid_paths": [],
            "broken_paths": [],
            "updated_paths": []
        }
        
        # Verificar scripts principais
        main_scripts = [
            "workflow_orchestrator_agent.py",
            "task_supervisor_agent.py",
            "professor_agent.py",
            "metrics_agent.py"
        ]
        
        for script_name in main_scripts:
            script_path = self.agents_path / script_name
            if script_path.exists():
                try:
                    # Verificar se o script pode ser executado
                    import subprocess
                    result = subprocess.run(
                        ["python", "-m", "py_compile", str(script_path)],
                        capture_output=True,
                        text=True
                    )
                    
                    if result.returncode == 0:
                        execution_validation["valid_paths"].append(script_name)
                        self.log_message(f"Script válido: {script_name}")
                    else:
                        execution_validation["broken_paths"].append({
                            "script": script_name,
                            "error": result.stderr
                        })
                        self.log_message(f"Script com erro: {script_name}", "ERROR")
                        
                except Exception as e:
                    execution_validation["broken_paths"].append({
                        "script": script_name,
                        "error": str(e)
                    })
                    self.log_message(f"Erro ao validar script {script_name}: {str(e)}", "ERROR")
        
        self.log_message(f"Caminhos de execução validados: {len(execution_validation['valid_paths'])} válidos")
        return execution_validation
    
    def generate_navigation_report(self) -> Dict[str, Any]:
        """Gera relatório completo de validação de navegação"""
        self.log_message("Gerando relatório de validação de navegação...")
        
        # Coletar todos os resultados
        file_refs = self.validate_file_references()
        import_refs = self.validate_import_statements()
        json_refs = self.validate_json_references()
        exec_paths = self.validate_execution_paths()
        
        # Relatório consolidado
        navigation_report = {
            "data_geracao": datetime.now().isoformat(),
            "file_references": file_refs,
            "import_statements": import_refs,
            "json_references": json_refs,
            "execution_paths": exec_paths,
            "summary": {
                "total_valid": (
                    len(file_refs["valid_references"]) +
                    len(import_refs["valid_imports"]) +
                    len(json_refs["valid_jsons"]) +
                    len(exec_paths["valid_paths"])
                ),
                "total_broken": (
                    len(file_refs["broken_references"]) +
                    len(import_refs["broken_imports"]) +
                    len(json_refs["broken_jsons"]) +
                    len(exec_paths["broken_paths"])
                ),
                "total_updated": (
                    len(file_refs["updated_references"]) +
                    len(import_refs["updated_imports"]) +
                    len(json_refs["updated_jsons"]) +
                    len(exec_paths["updated_paths"])
                ),
                "overall_status": "VALIDADO" if (
                    len(file_refs["broken_references"]) +
                    len(import_refs["broken_imports"]) +
                    len(json_refs["broken_jsons"]) +
                    len(exec_paths["broken_paths"])
                ) == 0 else "PRECISA_CORREÇÃO"
            }
        }
        
        report_file = self.wiki_path / "dashboard" / "navigation_validation_report.json"
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(navigation_report, f, indent=2, ensure_ascii=False)
        
        self.log_message(f"Relatório de navegação salvo: {report_file}")
        return navigation_report
    
    def execute(self):
        """Executa a validação completa de navegação"""
        self.log_message("=== INICIANDO VALIDAÇÃO DE NAVEGAÇÃO ===")
        
        try:
            # 1. Validar referências a arquivos
            file_refs = self.validate_file_references()
            
            # 2. Validar statements de import
            import_refs = self.validate_import_statements()
            
            # 3. Validar referências em JSON
            json_refs = self.validate_json_references()
            
            # 4. Validar caminhos de execução
            exec_paths = self.validate_execution_paths()
            
            # 5. Gerar relatório completo
            navigation_report = self.generate_navigation_report()
            
            # Relatório final
            final_report = {
                "task": "Validação de Navegação",
                "status": "CONCLUÍDA",
                "data_conclusao": datetime.now().isoformat(),
                "resultados": {
                    "file_references": file_refs,
                    "import_statements": import_refs,
                    "json_references": json_refs,
                    "execution_paths": exec_paths,
                    "navigation_report": navigation_report
                }
            }
            
            report_file = self.log_path / "navigation_validation_complete.json"
            with open(report_file, "w", encoding="utf-8") as f:
                json.dump(final_report, f, indent=2, ensure_ascii=False)
            
            self.log_message("=== VALIDAÇÃO DE NAVEGAÇÃO CONCLUÍDA COM SUCESSO ===")
            self.log_message(f"Relatório salvo: {report_file}")
            
            return final_report
            
        except Exception as e:
            self.log_message(f"ERRO na execução: {str(e)}", "ERROR")
            return {"status": "ERRO", "erro": str(e)}

if __name__ == "__main__":
    agent = NavigationValidationAgent()
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
        print(f"✅ Script navigation_validation_agent.py executado com sucesso via módulo agents.agent_orchestrator")
    else:
        print(f"❌ Erro na execução do script navigation_validation_agent.py via módulo agents.agent_orchestrator")

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
- **Nome**: migrated_navigation_validation_agent
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

