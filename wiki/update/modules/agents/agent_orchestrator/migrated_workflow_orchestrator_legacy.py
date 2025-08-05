from unicode_aliases import *
# Constantes
MAX_RETRIES = 8

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: workflow_orchestrator_legacy.py
Módulo de Destino: agents.agent_orchestrator
Data de Migração: 2025-08-01 12:21:44

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import AgentorchestratorModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎯 Workflow Orchestrator
Orquestrador principal que coordena todos os agentes do workflow de módulos OTClient
"""

import os
import sys
import json
import time
from datetime import datetime

# Adicionar diretório dos agentes ao path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)


class WorkflowOrchestrator:
    """Orquestrador principal do workflow de módulos OTClient"""
    
    def __init__(self, workspace_path: str = None):
        self.workspace_path = workspace_path or os.getcwd()
        self.results_path = os.path.join(self.workspace_path, "wiki/bmad/results")
        
        # Criar diretórios se não existirem
        os.makedirs(self.results_path, exist_ok=True)
        os.makedirs(os.path.join(self.results_path, "workflow_logs"), exist_ok=True)
        
        # Inicializar agentes
        self.analyzer = ModuleAnalyzerAgent(workspace_path)
        self.generator = ModuleGeneratorAgent(workspace_path)
        self.tester = ModuleTesterAgent(workspace_path)
        self.knowledge_manager = KnowledgeManagerAgent(workspace_path)
        
        # Configurações do workflow
        self.workflow_config = {
            "variation_count": 3,
            "test_all_variations": True,
            "save_physical_files": False,
            "enable_learning": True,
            "log_level": "INFO"
        }
        
        # Log do workflow
        self.workflow_log = []
    
    def execute_workflow(self, module_name: str, config: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Executa o workflow completo para um módulo
        
        Args:
            module_name: Nome do módulo OTClient a processar
            config: Configurações opcionais do workflow
            
        Returns:
            Resultados completos do workflow
        """
        print(f"🚀 Iniciando workflow para módulo: {module_name}")
        
        # Atualizar configurações se fornecidas
        if config:
            self.workflow_config.update(config)
        
        # Inicializar resultados
        workflow_results = {
            "workflow_id": f"workflow_{module_name}_{int(time.time())}",
            "module_name": module_name,
            "start_time": datetime.now().isoformat(),
            "config": self.workflow_config,
            "phases": {},
            "summary": {},
            "errors": [],
            "warnings": []
        }
        
        try:
            # Fase 1: Análise do módulo
            print("📖 Fase 1: Analisando módulo...")
            analysis_results = self.execute_analysis_phase(module_name)
            workflow_results["phases"]["analysis"] = {
                "status": "completed",
                "results": analysis_results,
                "duration": analysis_results.get("duration", 0)
            }
            
            # Fase 2: Geração de variações
            print("🎨 Fase 2: Gerando variações...")
            generation_results = self.execute_generation_phase(analysis_results)
            workflow_results["phases"]["generation"] = {
                "status": "completed",
                "results": generation_results,
                "duration": generation_results.get("duration", 0)
            }
            
            # Fase 3: Teste das variações
            print("🧪 Fase 3: Testando variações...")
            test_results = self.execute_testing_phase(generation_results, analysis_results)
            workflow_results["phases"]["testing"] = {
                "status": "completed",
                "results": test_results,
                "duration": test_results.get("duration", 0)
            }
            
            # Fase 4: Processamento de conhecimento
            if self.workflow_config["enable_learning"]:
                print("📚 Fase 4: Processando conhecimento...")
                learning_results = self.execute_learning_phase(analysis_results, generation_results, test_results)
                workflow_results["phases"]["learning"] = {
                    "status": "completed",
                    "results": learning_results,
                    "duration": learning_results.get("duration", 0)
                }
            
            # Gerar resumo
            workflow_results["summary"] = self.generate_workflow_summary(workflow_results)
            workflow_results["end_time"] = datetime.now().isoformat()
            
            # Salvar resultados
            self.save_workflow_results(workflow_results)
            
            print(f"✅ Workflow concluído com sucesso para {module_name}")
            
        except Exception as e:
            error_msg = f"Erro no workflow: {str(e)}"
            print(f"❌ {error_msg}")
            workflow_results["errors"].append(error_msg)
            workflow_results["status"] = "failed"
            workflow_results["end_time"] = datetime.now().isoformat()
        
        return workflow_results
    
    def execute_analysis_phase(self, module_name: str) -> Dict[str, Any]:
        """Executa fase de análise"""
        start_time = time.time()
        
        try:
            # Verificar se módulo existe
            available_modules = self.analyzer.get_available_modules()
            if module_name not in available_modules:
                raise ValueError(f"Módulo '{module_name}' não encontrado. Módulos disponíveis: {available_modules}")
            
            # Executar análise
            analysis_results = self.analyzer.analyze_module(module_name)
            
            # Adicionar métricas de tempo
            duration = time.time() - start_time
            analysis_results["duration"] = duration
            analysis_results["status"] = "success"
            
            self.log_phase("analysis", module_name, "success", duration)
            
            return analysis_results
            
        except Exception as e:
            duration = time.time() - start_time
            self.log_phase("analysis", module_name, "failed", duration, str(e))
            raise
    
    def execute_generation_phase(self, analysis_results: Dict[str, Any]) -> Dict[str, Any]:
        """Executa fase de geração"""
        start_time = time.time()
        
        try:
            # Gerar variações
            variation_count = self.workflow_config["variation_count"]
            variations = self.generator.generate_module_variations(analysis_results, variation_count)
            
            # Criar arquivos físicos se configurado
            if self.workflow_config["save_physical_files"]:
                for variation in variations:
                    self.generator.create_physical_files(variation)
            
            # Preparar resultados
            generation_results = {
                "variations": variations,
                "total_variations": len(variations),
                "successful_variations": len([v for v in variations if v.get("compatibility_score", 0) > 0.7]),
                "average_compatibility_score": sum(v.get("compatibility_score",
    0) for v in variations) / len(variations) if variations else 0,
                "status": "success"
            }
            
            # Adicionar métricas de tempo
            duration = time.time() - start_time
            generation_results["duration"] = duration
            
            self.log_phase("generation", analysis_results.get("module_name", "unknown"), "success", duration)
            
            return generation_results
            
        except Exception as e:
            duration = time.time() - start_time
            self.log_phase("generation", analysis_results.get("module_name", "unknown"), "failed", duration, str(e))
            raise
    
    def execute_testing_phase(self, generation_results: Dict[str, Any], 
                            analysis_results: Dict[str, Any]) -> Dict[str, Any]:
        """Executa fase de teste"""
        start_time = time.time()
        
        try:
            # Testar variações
            variations = generation_results.get("variations", [])
            test_results = self.tester.test_module_variations(variations, analysis_results)
            
            # Adicionar métricas de tempo
            duration = time.time() - start_time
            test_results["duration"] = duration
            test_results["status"] = "success"
            
            self.log_phase("testing", analysis_results.get("module_name", "unknown"), "success", duration)
            
            return test_results
            
        except Exception as e:
            duration = time.time() - start_time
            self.log_phase("testing", analysis_results.get("module_name", "unknown"), "failed", duration, str(e))
            raise
    
    def execute_learning_phase(self, analysis_results: Dict[str, Any], 
                             generation_results: Dict[str, Any], 
                             test_results: Dict[str, Any]) -> Dict[str, Any]:
        """Executa fase de aprendizado"""
        start_time = time.time()
        
        try:
            # Processar resultados e extrair insights
            learning_data = self.knowledge_manager.process_workflow_results(
                analysis_results, 
                generation_results.get("variations", []), 
                test_results
            )
            
            # Adicionar métricas de tempo
            duration = time.time() - start_time
            learning_data["duration"] = duration
            learning_data["status"] = "success"
            
            self.log_phase("learning", analysis_results.get("module_name", "unknown"), "success", duration)
            
            return learning_data
            
        except Exception as e:
            duration = time.time() - start_time
            self.log_phase("learning", analysis_results.get("module_name", "unknown"), "failed", duration, str(e))
            raise
    
    def generate_workflow_summary(self, workflow_results: Dict[str, Any]) -> Dict[str, Any]:
        """Gera resumo do workflow"""
        summary = {
            "total_duration": 0,
            "phases_completed": 0,
            "total_phases": len(workflow_results["phases"]),
            "overall_status": "success",
            "key_metrics": {}
        }
        
        # Calcular duração total
        total_duration = 0
        phases_completed = 0
        
        for phase_name, phase_data in workflow_results["phases"].items():
            if phase_data.get("status") == "completed":
                phases_completed += 1
                total_duration += phase_data.get("duration", 0)
        
        summary["total_duration"] = total_duration
        summary["phases_completed"] = phases_completed
        
        # Determinar status geral
        if phases_completed < len(workflow_results["phases"]):
            summary["overall_status"] = "partial"
        if workflow_results.get("errors"):
            summary["overall_status"] = "failed"
        
        # Métricas chave
        if "generation" in workflow_results["phases"]:
            gen_results = workflow_results["phases"]["generation"]["results"]
            summary["key_metrics"]["variations_generated"] = gen_results.get("total_variations", 0)
            summary["key_metrics"]["success_rate"] = gen_results.get("successful_variations",
    0) / max(gen_results.get("total_variations", 1), 1)
        
        if "testing" in workflow_results["phases"]:
            test_results = workflow_results["phases"]["testing"]["results"]
            test_summary = test_results.get("summary", {})
            summary["key_metrics"]["test_pass_rate"] = test_summary.get("passed_variations",
    0) / max(test_summary.get("total_variations", 1), 1)
            summary["key_metrics"]["average_quality_score"] = test_summary.get("average_quality_score", 0)
        
        return summary
    
    def save_workflow_results(self, workflow_results: Dict[str, Any]):
        """Salva resultados do workflow"""
        workflow_id = workflow_results["workflow_id"]
        module_name = workflow_results["module_name"]
        
        # Salvar resultados principais
        results_file = os.path.join(
            self.results_path, 
            "workflow_logs", 
            f"{workflow_id}_{module_name}_results.json"
        )
        
        try:
            with open(results_file, 'w', encoding='utf-8') as f:
                json.dump(workflow_results, f, indent=2, ensure_ascii=False)
            print(f"✅ Resultados do workflow salvos em: {results_file}")
        except Exception as e:
            print(f"⚠️ Erro ao salvar resultados do workflow: {e}")
        
        # Salvar log do workflow
        log_file = os.path.join(
            self.results_path, 
            "workflow_logs", 
            f"{workflow_id}_{module_name}_log.json"
        )
        
        try:
            with open(log_file, 'w', encoding='utf-8') as f:
                json.dump(self.workflow_log, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️ Erro ao salvar log do workflow: {e}")
    
    def log_phase(self, phase_name: str, module_name: str, status: str, 
                 duration: float, error: str = None):
        """Registra log de uma fase do workflow"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "phase": phase_name,
            "module": module_name,
            "status": status,
            "duration": duration,
            "error": error
        }
        
        self.workflow_log.append(log_entry)
        
        # Log no console
        if status == "success":
            print(f"✅ {phase_name.capitalize()} concluída em {duration:.2f}s")
        else:
            print(f"❌ {phase_name.capitalize()} falhou em {duration:.2f}s: {error}")
    
    def get_available_modules(self) -> List[str]:
        """Retorna lista de módulos disponíveis"""
        return self.analyzer.get_available_modules()
    
    def get_workflow_status(self, workflow_id: str) -> Dict[str, Any]:
        """Obtém status de um workflow específico"""
        log_dir = os.path.join(self.results_path, "workflow_logs")
        
        for file_name in os.listdir(log_dir):
            if file_name.startswith(workflow_id) and file_name.endswith("_results.json"):
                file_path = os.path.join(log_dir, file_name)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        return json.load(f)
                except Exception as e:
                    print(f"⚠️ Erro ao carregar status do workflow: {e}")
        
        return {"error": "Workflow não encontrado"}
    
    def list_workflows(self) -> List[Dict[str, Any]]:
        """Lista todos os workflows executados"""
        workflows = []
        log_dir = os.path.join(self.results_path, "workflow_logs")
        
        if not os.path.exists(log_dir):
            return workflows
        
        for file_name in os.listdir(log_dir):
            if file_name.endswith("_results.json"):
                file_path = os.path.join(log_dir, file_name)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        workflow_data = json.load(f)
                        workflows.append({
                            "workflow_id": workflow_data.get("workflow_id"),
                            "module_name": workflow_data.get("module_name"),
                            "start_time": workflow_data.get("start_time"),
                            "end_time": workflow_data.get("end_time"),
                            "status": workflow_data.get("summary", {}).get("overall_status", "unknown")
                        })
                except Exception as e:
                    print(f"⚠️ Erro ao carregar workflow {file_name}: {e}")
        
        return sorted(workflows, key=lambda x: x.get("start_time", ""), reverse=True)

def main():
    """Função principal para teste do orquestrador"""
    orchestrator = WorkflowOrchestrator()
    
    # Listar módulos disponíveis
    modules = orchestrator.get_available_modules()
    print(f"📋 Módulos disponíveis: {len(modules)}")
    
    if not modules:
        print("❌ Nenhum módulo encontrado")
        return
    
    # Executar workflow para o primeiro módulo
    example_module = modules[0]
    print(f"🚀 Executando workflow para módulo: {example_module}")
    
    # Configurações de teste
    test_config = {
        "variation_count": 2,
        "test_all_variations": True,
        "save_physical_files": False,
        "enable_learning": True,
        "log_level": "INFO"
    }
    
    try:
        results = orchestrator.execute_workflow(example_module, test_config)
        
        print(f"✅ Workflow concluído")
        print(f"📊 Resumo: {results['summary']}")
        
        # Listar workflows
        workflows = orchestrator.list_workflows()
        print(f"📋 Total de workflows executados: {len(workflows)}")
        
    except Exception as e:
        print(f"❌ Erro no workflow: {e}")

if __name__ == "__main__":
    main() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = AgentorchestratorModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script workflow_orchestrator_legacy.py executado com sucesso via módulo agents.agent_orchestrator")
    else:
        print(f"❌ Erro na execução do script workflow_orchestrator_legacy.py via módulo agents.agent_orchestrator")

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
- **Nome**: migrated_workflow_orchestrator_legacy
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

