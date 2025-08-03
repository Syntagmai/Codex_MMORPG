from unicode_aliases import *
# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
TIMEOUT_SECONDS = 60

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: agents_orchestrator.py
Módulo de Destino: agents.agent_orchestrator
Data de Migração: 2025-08-01 12:21:42

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import AgentorchestratorModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agents Orchestrator - Sistema de Coordenação de Agentes

Este agente é responsável por:
- Coordenar todos os agentes BMAD
- Orquestrar workflows entre agentes
- Gerenciar dependências entre tarefas
- Executar commits automáticos
- Monitorar performance dos agentes
"""

import json
import logging
import subprocess
import time
from datetime import datetime
import threading
import queue

class AgentsOrchestrator:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent.parent.parent
        self.dashboard_path = self.base_path / "wiki" / "dashboard"
        self.log_path = self.base_path / "wiki" / "log"
        self.agents_path = self.base_path / "wiki" / "bmad" / "agents"
        
        # Debug: verificar caminhos
        self.logger = logging.getLogger('AgentsOrchestrator')
        self.logger.info(f"🔍 Caminho base: {self.base_path}")
        self.logger.info(f"🔍 Caminho dashboard: {self.dashboard_path}")
        self.logger.info(f"🔍 Caminho agents: {self.agents_path}")
        
        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        # Carregar configurações
        self.load_configuration()
        
        # Fila de tarefas
        self.task_queue = queue.Queue()
        self.running_agents = {}
        self.agent_results = {}
        
    def load_configuration(self):
        """Carrega configurações do sistema"""
        self.logger.info("🔧 Carregando configurações do Agents Orchestrator...")
        
        # Configurações padrão
        self.config = {
            "max_concurrent_agents": 3,
            "agent_timeout": 1800,  # 30 minutos
            "commit_after_task": True,
            "auto_retry_failed": True,
            "max_retries": 3,
            "agents": {
                "task_master": {
                    "file": "task_master_agent.py",
                    "priority": "high",
                    "dependencies": [],
                    "auto_commit": True
                },
                "progress_tracker": {
                    "file": "progress_tracker_agent.py",
                    "priority": "medium",
                    "dependencies": ["task_master"],
                    "auto_commit": True
                },
                "documentation_completer": {
                    "file": "documentation_completer_agent.py",
                    "priority": "medium",
                    "dependencies": [],
                    "auto_commit": True
                },
                "path_validator": {
                    "file": "path_validator_agent.py",
                    "priority": "low",
                    "dependencies": [],
                    "auto_commit": False
                },
                "deep_source_analyzer": {
                    "file": "deep_source_analyzer_agent.py",
                    "priority": "medium",
                    "dependencies": [],
                    "auto_commit": True
                },
                "habdel_organizer": {
                    "file": "habdel_organizer_agent.py",
                    "priority": "high",
                    "dependencies": [],
                    "auto_commit": True
                }
            }
        }
        
        self.logger.info("✅ Configurações carregadas com sucesso")
    
    def analyze_dashboard(self) -> Dict:
        """Analisa o dashboard para identificar tarefas pendentes"""
        self.logger.info("📊 Analisando dashboard para tarefas pendentes...")
        
        dashboard_file = self.dashboard_path / "integrated_task_manager.md"
        
        if not dashboard_file.exists():
            self.logger.error(f"❌ Dashboard não encontrado: {dashboard_file}")
            return {}
        
        try:
            with open(dashboard_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extrair tarefas pendentes
            pending_tasks = self.extract_pending_tasks(content)
            
            self.logger.info(f"✅ Dashboard analisado: {len(pending_tasks)} tarefas pendentes")
            return {"pending_tasks": pending_tasks}
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao analisar dashboard: {e}")
            return {}
    
    def extract_pending_tasks(self, content: str) -> List[Dict]:
        """Extrai tarefas pendentes do dashboard"""
        pending_tasks = []
        
        # Padrões para diferentes tipos de tarefas pendentes
        patterns = [
            (r'- \[ \] \*\*(\d+\.\d+)\*\* (.+?) \((\d+)% → (\d+)%\)', "subtask"),
            (r'- \[ \] \*\*(.+?)\*\* (.+?)$', "story"),
            (r'- \[ \] \*\*(.+?)\*\* 🔄 Em desenvolvimento', "agent"),
            (r'- \[ \] \*\*(.+?)\*\* 📋 Planejado', "agent"),
            (r'- \[ \] \*\*(.+?)\*\* 📋 Pendente', "roadmap"),
            (r'- \[ \] \*\*(.+?)\*\* 📋 Pendente', "planejamento")
        ]
        
        for pattern, task_type in patterns:
            matches = re.finditer(pattern, content, re.MULTILINE)
            for match in matches:
                if task_type == "subtask":
                    task_id = match.group(1)
                    title = match.group(2)
                    current_progress = int(match.group(3))
                    target_progress = int(match.group(4))
                    
                    pending_tasks.append({
                        "id": task_id,
                        "title": title,
                        "type": task_type,
                        "current_progress": current_progress,
                        "target_progress": target_progress,
                        "priority": self.determine_priority(task_id, task_type)
                    })
                else:
                    task_id = match.group(1)
                    title = match.group(2) if len(match.groups()) > 1 else ""
                    
                    pending_tasks.append({
                        "id": task_id,
                        "title": title,
                        "type": task_type,
                        "priority": self.determine_priority(task_id, task_type)
                    })
        
        return pending_tasks
    
    def determine_priority(self, task_id: str, task_type: str) -> str:
        """Determina prioridade da tarefa"""
        if task_type == "subtask":
            # Prioridade baseada no ID da epic
            epic_id = task_id.split('.')[0]
            if epic_id in ['1', '2']:  # Epics críticas
                return "high"
            elif epic_id == '4':  # Epic de agentes
                return "high"
            else:
                return "medium"
        elif task_type == "agent":
            return "high"  # Agentes sempre têm prioridade alta
        elif task_type == "story":
            # Prioridade baseada na categoria da story
            if task_id.startswith(('UI-', 'GAME-')):
                return "medium"
            else:
                return "low"
        else:
            return "low"
    
    def assign_task_to_agent(self, task: Dict) -> Optional[str]:
        """Atribui tarefa ao agente apropriado"""
        task_type = task.get('type', '')
        
        # Mapeamento de tipos de tarefa para agentes
        agent_mapping = {
            'subtask': 'task_master',
            'story': 'documentation_completer',
            'agent': 'task_master',
            'roadmap': 'task_master',
            'planejamento': 'task_master'
        }
        
        assigned_agent = agent_mapping.get(task_type, 'task_master')
        
        # Verificar se agente está disponível
        if assigned_agent in self.running_agents:
            self.logger.warning(f"⚠️ Agente {assigned_agent} já está em execução")
            return None
        
        return assigned_agent
    
    def execute_agent(self, agent_name: str, task: Dict) -> bool:
        """Executa um agente específico"""
        self.logger.info(f"🚀 Executando agente: {agent_name}")
        
        agent_config = self.config["agents"].get(agent_name)
        if not agent_config:
            self.logger.error(f"❌ Configuração não encontrada para agente: {agent_name}")
            return False
        
        agent_file = self.agents_path / agent_config["file"]
        
        if not agent_file.exists():
            self.logger.error(f"❌ Arquivo do agente não encontrado: {agent_file}")
            return False
        
        try:
            # Marcar agente como em execução
            self.running_agents[agent_name] = {
                "start_time": datetime.now(),
                "task": task,
                "status": "running"
            }
            
            # Executar agente em thread separada
            thread = threading.Thread(
                target=self._run_agent_thread,
                args=(agent_file, agent_name, task)
            )
            thread.start()
            
            self.logger.info(f"✅ Agente {agent_name} iniciado em thread separada")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao executar agente {agent_name}: {e}")
            if agent_name in self.running_agents:
                del self.running_agents[agent_name]
            return False
    
    def _run_agent_thread(self, agent_file: Path, agent_name: str, task: Dict):
        """Executa agente em thread separada"""
        try:
            # Executar agente
            result = subprocess.run(
                ['python', str(agent_file)],
                capture_output=True,
                text=True,
                timeout=self.config["agent_timeout"]
            )
            
            # Processar resultado
            success = result.returncode == 0
            output = result.stdout
            error = result.stderr
            
            # Salvar resultado
            self.agent_results[agent_name] = {
                "success": success,
                "output": output,
                "error": error,
                "task": task,
                "completion_time": datetime.now()
            }
            
            # Marcar agente como concluído
            if agent_name in self.running_agents:
                self.running_agents[agent_name]["status"] = "completed"
                self.running_agents[agent_name]["completion_time"] = datetime.now()
            
            self.logger.info(f"✅ Agente {agent_name} concluído: {'sucesso' if success else 'falha'}")
            
            # Fazer commit automático se configurado
            if self.config["agents"][agent_name].get("auto_commit", False) and success:
                self.execute_auto_commit(agent_name, task)
            
        except subprocess.TimeoutExpired:
            self.logger.error(f"❌ Agente {agent_name} atingiu timeout")
            self.agent_results[agent_name] = {
                "success": False,
                "output": "",
                "error": "Timeout",
                "task": task,
                "completion_time": datetime.now()
            }
            
            if agent_name in self.running_agents:
                self.running_agents[agent_name]["status"] = "timeout"
        
        except Exception as e:
            self.logger.error(f"❌ Erro na execução do agente {agent_name}: {e}")
            self.agent_results[agent_name] = {
                "success": False,
                "output": "",
                "error": str(e),
                "task": task,
                "completion_time": datetime.now()
            }
    
    def execute_auto_commit(self, agent_name: str, task: Dict):
        """Executa commit automático após tarefa concluída"""
        self.logger.info(f"📝 Executando commit automático para {agent_name}")
        
        try:
            # Gerar mensagem de commit
            commit_message = self.generate_commit_message(agent_name, task)
            
            # Adicionar arquivos modificados
            subprocess.run(['git', 'add', '.'], check=True)
            
            # Fazer commit
            result = subprocess.run(
                ['git', 'commit', '-m', commit_message],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                # Extrair hash do commit
                commit_hash = result.stdout.strip().split()[-1]
                self.logger.info(f"✅ Commit realizado: {commit_hash}")
                
                # Atualizar dashboard com hash do commit
                self.update_dashboard_with_commit(commit_hash, agent_name, task)
            else:
                self.logger.error(f"❌ Erro no commit: {result.stderr}")
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao executar commit automático: {e}")
    
    def generate_commit_message(self, agent_name: str, task: Dict) -> str:
        """Gera mensagem de commit contextual"""
        task_type = task.get('type', '')
        task_id = task.get('id', '')
        task_title = task.get('title', '')
        
        # Determinar categoria baseada no tipo de tarefa
        category_mapping = {
            'subtask': 'Epic',
            'story': 'Story',
            'agent': 'Agent',
            'roadmap': 'Roadmap',
            'planejamento': 'Planejamento'
        }
        
        category = category_mapping.get(task_type, 'Task')
        
        # Calcular progresso se disponível
        progress_info = ""
        if 'current_progress' in task and 'target_progress' in task:
            current = task['current_progress']
            target = task['target_progress']
            progress = target - current
            progress_info = f"\n📊 Progresso: {current}% → {target}% (+{progress}%)"
        
        commit_message = f"""feat(task-manager): {category} - {task_title}

🎯 Categoria: {category}
🤖 Agent: {agent_name}
📋 Dashboard: integrated_task_manager.md{progress_info}

🔧 Mudanças Realizadas:
- Tarefa {task_id} concluída por {agent_name}
- {task_title}
- Atualização automática do dashboard

📈 Impacto no Sistema:
- Progresso atualizado no sistema integrado
- Métricas recalculadas automaticamente
- Próximas prioridades identificadas

🔗 Referências:
- {category}: {task_id}
- Agent: {agent_name}

---
Commit automático gerado pelo Agents Orchestrator
"""
        
        return commit_message
    
    def update_dashboard_with_commit(self, commit_hash: str, agent_name: str, task: Dict):
        """Atualiza dashboard com hash do commit"""
        self.logger.info(f"📊 Atualizando dashboard com commit {commit_hash}")
        
        try:
            dashboard_file = self.dashboard_path / "integrated_task_manager.md"
            
            if not dashboard_file.exists():
                return
            
            # Ler conteúdo atual
            with open(dashboard_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Adicionar informação do commit
            commit_info = f"""
### **📝 Último Commit:**
- **Hash**: {commit_hash}
- **Agent**: {agent_name}
- **Tarefa**: {task.get('id', '')} - {task.get('title', '')}
- **Data**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
            
            # Inserir no final do arquivo
            updated_content = content + commit_info
            
            # Salvar arquivo atualizado
            with open(dashboard_file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            self.logger.info("✅ Dashboard atualizado com hash do commit")
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao atualizar dashboard: {e}")
    
    def orchestrate_workflow(self) -> bool:
        """Orquestra workflow completo de agentes"""
        self.logger.info("🎼 Iniciando orquestração de workflow...")
        
        try:
            # Analisar dashboard
            analysis = self.analyze_dashboard()
            if not analysis:
                return False
            
            pending_tasks = analysis.get('pending_tasks', [])
            
            if not pending_tasks:
                self.logger.info("✅ Nenhuma tarefa pendente encontrada")
                return True
            
            # Ordenar tarefas por prioridade
            priority_order = {"high": 3, "medium": 2, "low": 1}
            sorted_tasks = sorted(
                pending_tasks,
                key=lambda x: priority_order.get(x.get('priority', 'low'), 1),
                reverse=True
            )
            
            self.logger.info(f"📋 {len(sorted_tasks)} tarefas ordenadas por prioridade")
            
            # Executar tarefas
            for task in sorted_tasks[:5]:  # Limitar a 5 tarefas por vez
                agent_name = self.assign_task_to_agent(task)
                
                if agent_name:
                    self.logger.info(f"🎯 Atribuindo tarefa {task['id']} ao agente {agent_name}")
                    
                    # Aguardar slot disponível
                    while len(self.running_agents) >= self.config["max_concurrent_agents"]:
                        time.sleep(5)
                        self.logger.info("⏳ Aguardando slot disponível para agente...")
                    
                    # Executar agente
                    if not self.execute_agent(agent_name, task):
                        self.logger.error(f"❌ Falha ao executar agente {agent_name}")
                else:
                    self.logger.warning(f"⚠️ Nenhum agente disponível para tarefa {task['id']}")
            
            # Aguardar conclusão dos agentes
            self.wait_for_agents_completion()
            
            # Gerar relatório final
            self.generate_orchestration_report()
            
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro na orquestração: {e}")
            return False
    
    def wait_for_agents_completion(self, timeout: int = 3600):
        """Aguarda conclusão de todos os agentes"""
        self.logger.info("⏳ Aguardando conclusão dos agentes...")
        
        start_time = time.time()
        while self.running_agents and (time.time() - start_time) < timeout:
            # Verificar agentes concluídos
            completed_agents = []
            for agent_name, agent_info in self.running_agents.items():
                if agent_info.get('status') in ['completed', 'timeout', 'failed']:
                    completed_agents.append(agent_name)
            
            # Remover agentes concluídos
            for agent_name in completed_agents:
                del self.running_agents[agent_name]
                self.logger.info(f"✅ Agente {agent_name} removido da lista de execução")
            
            if self.running_agents:
                time.sleep(10)
        
        if self.running_agents:
            self.logger.warning("⚠️ Timeout atingido, alguns agentes ainda em execução")
    
    def generate_orchestration_report(self):
        """Gera relatório de orquestração"""
        self.logger.info("📊 Gerando relatório de orquestração...")
        
        # Converter datetime objects para strings
        serializable_agent_results = {}
        for agent_name, result in self.agent_results.items():
            serializable_result = {}
            for key, value in result.items():
                if isinstance(value, datetime):
                    serializable_result[key] = value.isoformat()
                else:
                    serializable_result[key] = value
            serializable_agent_results[agent_name] = serializable_result
        
        serializable_running_agents = {}
        for agent_name, agent_info in self.running_agents.items():
            serializable_agent_info = {}
            for key, value in agent_info.items():
                if isinstance(value, datetime):
                    serializable_agent_info[key] = value.isoformat()
                else:
                    serializable_agent_info[key] = value
            serializable_running_agents[agent_name] = serializable_agent_info
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "total_agents_executed": len(self.agent_results),
            "successful_agents": sum(1 for r in self.agent_results.values() if r.get('success')),
            "failed_agents": sum(1 for r in self.agent_results.values() if not r.get('success')),
            "agent_results": serializable_agent_results,
            "running_agents": serializable_running_agents
        }
        
        # Salvar relatório
        report_file = self.log_path / f"orchestration_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        self.logger.info(f"✅ Relatório salvo: {report_file}")
        
        # Log de resumo
        self.logger.info(f"📊 Resumo da Orquestração:")
        self.logger.info(f"   - Agentes Executados: {report['total_agents_executed']}")
        self.logger.info(f"   - Sucessos: {report['successful_agents']}")
        self.logger.info(f"   - Falhas: {report['failed_agents']}")
        self.logger.info(f"   - Em Execução: {len(self.running_agents)}")
    
    def run(self):
        """Executa o Agents Orchestrator"""
        self.logger.info("🚀 Iniciando Agents Orchestrator...")
        
        try:
            # Executar orquestração
            success = self.orchestrate_workflow()
            
            if success:
                self.logger.info("✅ Orquestração concluída com sucesso")
            else:
                self.logger.error("❌ Orquestração falhou")
            
            return success
            
        except Exception as e:
            self.logger.error(f"❌ Erro na execução do Agents Orchestrator: {e}")
            return False

if __name__ == "__main__":
    import re
    
    orchestrator = AgentsOrchestrator()
    success = orchestrator.run()
    
    if success:
        print("✅ Agents Orchestrator executado com sucesso!")
    else:
        print("❌ Agents Orchestrator falhou na execução!") 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = AgentorchestratorModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script agents_orchestrator.py executado com sucesso via módulo agents.agent_orchestrator")
    else:
        print(f"❌ Erro na execução do script agents_orchestrator.py via módulo agents.agent_orchestrator")
