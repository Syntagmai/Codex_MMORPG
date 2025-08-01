# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
MAX_ITEMS = 100
TIMEOUT_SECONDS = 60

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: migrated_intelligent_orchestrator.py
Módulo de Destino: maps.map_updater
Data de Migração: 2025-08-01 12:21:42

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import MapupdaterModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: intelligent_orchestrator.py
Módulo de Destino: agents.workflow_manager
Data de Migração: 2025-08-01 12:21:34

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import WorkflowmanagerModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Orquestração Inteligente para Agentes BMAD
Detecta automaticamente o contexto e coordena agentes sem comandos manuais
"""

import json
import time
from datetime import datetime

class IntelligentOrchestrator:
    """Sistema de orquestração inteligente para agentes BMAD"""
    
    def __init__(self):
        self.context_keywords = {
            # Engine Development (C++)
            "performance": ["engine_developer", "performance_optimization"],
            "otimização": ["engine_developer", "performance_optimization"],
            "memory": ["engine_developer", "memory_management"],
            "C++": ["engine_developer", "core_development"],
            "OpenGL": ["engine_developer", "graphics_optimization"],
            "ASIO": ["engine_developer", "network_optimization"],
            "VCPKG": ["engine_developer", "dependency_management"],
            "renderização": ["engine_developer", "graphics_optimization"],
            "compilação": ["engine_developer", "build_optimization"],
            
            # Content Creation (Lua)
            "Lua": ["content_creator", "module_development"],
            "módulo": ["content_creator", "module_development"],
            "OTUI": ["content_creator", "ui_development"],
            "scripts": ["content_creator", "scripting"],
            "interface": ["content_creator", "ui_development"],
            "conteúdo": ["content_creator", "content_creation"],
            "quest": ["content_creator", "quest_development"],
            "NPC": ["content_creator", "npc_development"],
            
            # Game Design
            "sistema": ["game_designer", "feature_development"],
            "feature": ["game_designer", "feature_development"],
            "mecânica": ["game_designer", "gameplay_design"],
            "gameplay": ["game_designer", "gameplay_design"],
            "design": ["game_designer", "system_design"],
            "jogo": ["game_designer", "game_design"],
            
            # Quality Assurance
            "teste": ["qa_tester", "quality_assurance"],
            "bug": ["qa_tester", "bug_fix"],
            "erro": ["qa_tester", "bug_fix"],
            "validação": ["qa_tester", "quality_assurance"],
            "qualidade": ["qa_tester", "quality_assurance"],
            "problema": ["qa_tester", "issue_resolution"],
            
            # DevOps
            "deploy": ["devops_engineer", "deployment"],
            "build": ["devops_engineer", "build_management"],
            "CI/CD": ["devops_engineer", "ci_cd"],
            "infraestrutura": ["devops_engineer", "infrastructure"],
            "produção": ["devops_engineer", "production"],
            "servidor": ["devops_engineer", "server_management"],
            
            # Level Design (UI/UX)
            "UX": ["level_designer", "ux_design"],
            "UI": ["level_designer", "ui_design"],
            "layout": ["level_designer", "layout_design"],
            "experiência": ["level_designer", "user_experience"],
            "usabilidade": ["level_designer", "usability"],
            
            # Project Management
            "coordenar": ["game_team_orchestrator", "project_management"],
            "gerenciar": ["game_team_orchestrator", "project_management"],
            "workflow": ["game_team_orchestrator", "workflow_management"],
            "projeto": ["game_team_orchestrator", "project_management"],
            "equipe": ["game_team_orchestrator", "team_management"],
            
            # OTClient specific
            "OTClient": ["engine_developer", "content_creator", "game_designer"],
            "cliente": ["engine_developer", "content_creator"],
            "servidor": ["devops_engineer", "engine_developer"],
            "protocolo": ["engine_developer", "content_creator"],
            "opcode": ["engine_developer", "content_creator"],
            "network": ["engine_developer", "content_creator"]
        }
        
        self.workflows = {
            "performance_optimization": {
                "agents": ["engine_developer", "content_creator", "qa_tester"],
                "phases": [
                    "analysis",      # Engine Developer analisa código
                    "optimization",  # Engine Developer otimiza C++
                    "integration",   # Content Creator cria módulos Lua
                    "testing"        # QA Tester valida melhorias
                ],
                "estimated_duration": "2-3 hours",
                "description": "Otimização de performance do OTClient"
            },
            "feature_development": {
                "agents": ["game_designer", "engine_developer", "content_creator", "qa_tester"],
                "phases": [
                    "design",        # Game Designer cria design
                    "implementation", # Engine Developer implementa core
                    "content",       # Content Creator cria conteúdo
                    "testing"        # QA Tester testa feature
                ],
                "estimated_duration": "4-6 hours",
                "description": "Desenvolvimento de nova feature"
            },
            "bug_fix": {
                "agents": ["qa_tester", "engine_developer", "content_creator"],
                "phases": [
                    "identification", # QA Tester identifica bug
                    "fix",           # Engine Developer/Content Creator corrige
                    "validation"     # QA Tester valida correção
                ],
                "estimated_duration": "1-2 hours",
                "description": "Correção de bug"
            },
            "module_development": {
                "agents": ["content_creator", "qa_tester"],
                "phases": [
                    "design",        # Content Creator designa módulo
                    "implementation", # Content Creator implementa Lua
                    "testing"        # QA Tester testa módulo
                ],
                "estimated_duration": "1-3 hours",
                "description": "Desenvolvimento de módulo Lua"
            },
            "ui_development": {
                "agents": ["level_designer", "content_creator", "qa_tester"],
                "phases": [
                    "design",        # Level Designer cria design UI
                    "implementation", # Content Creator implementa OTUI
                    "testing"        # QA Tester testa interface
                ],
                "estimated_duration": "2-4 hours",
                "description": "Desenvolvimento de interface"
            }
        }
        
        self.agent_personalities = {
            "engine_developer": {
                "name": "Zara",
                "expertise": "C++ Development, Performance Optimization, Memory Management",
                "personality": "Analytical, performance-focused, technical expert"
            },
            "content_creator": {
                "name": "Maya",
                "expertise": "Lua Scripting, Module Development, UI Scripting",
                "personality": "Creative, detail-oriented, user-focused"
            },
            "game_designer": {
                "name": "Alex",
                "expertise": "Game Systems, Feature Design, Gameplay Mechanics",
                "personality": "Innovative, player-focused, systems thinker"
            },
            "qa_tester": {
                "name": "Sam",
                "expertise": "Quality Assurance, Bug Detection, Testing Strategies",
                "personality": "Thorough, methodical, quality-focused"
            },
            "devops_engineer": {
                "name": "Jordan",
                "expertise": "Deployment, CI/CD, Infrastructure Management",
                "personality": "Efficient, automation-focused, reliability-driven"
            },
            "level_designer": {
                "name": "Casey",
                "expertise": "UI/UX Design, User Experience, Interface Design",
                "personality": "User-centric, aesthetic-focused, experience-driven"
            },
            "game_team_orchestrator": {
                "name": "Riley",
                "expertise": "Project Management, Team Coordination, Workflow Optimization",
                "personality": "Organized, leadership-focused, coordination expert"
            }
        }
    
    def analyze_context(self, user_request: str) -> Dict[str, Any]:
        """Analisa o contexto do pedido do usuário"""
        print(f"🤖 Analisando contexto: '{user_request}'")
        
        # Normaliza o texto
        text = user_request.lower()
        
        # Detecta palavras-chave
        detected_keywords = []
        detected_agents = set()
        detected_workflows = set()
        
        for keyword, agent_workflows in self.context_keywords.items():
            if keyword.lower() in text:
                detected_keywords.append(keyword)
                for agent_workflow in agent_workflows:
                    detected_agents.add(agent_workflow)
                    if "_" in agent_workflow:
                        detected_workflows.add(agent_workflow)
        
        # Determina complexidade
        complexity = self.analyze_complexity(text, detected_keywords)
        
        # Identifica workflow principal
        primary_workflow = self.identify_primary_workflow(detected_keywords, detected_workflows)
        
        context_analysis = {
            "original_request": user_request,
            "detected_keywords": detected_keywords,
            "detected_agents": list(detected_agents),
            "detected_workflows": list(detected_workflows),
            "complexity": complexity,
            "primary_workflow": primary_workflow,
            "estimated_duration": self.workflows.get(primary_workflow, {}).get("estimated_duration", "1-2 hours"),
            "description": self.workflows.get(primary_workflow, {}).get("description", "Tarefa personalizada")
        }
        
        print(f"🎯 Contexto detectado: {context_analysis['description']}")
        print(f"👥 Agentes necessários: {', '.join(context_analysis['detected_agents'])}")
        print(f"📊 Complexidade: {context_analysis['complexity']}")
        
        return context_analysis
    
    def analyze_complexity(self, text: str, keywords: List[str]) -> str:
        """Analisa a complexidade baseada no contexto"""
        # Conta palavras-chave relacionadas a performance
        performance_keywords = ["performance", "otimização", "memory", "renderização"]
        performance_count = sum(1 for kw in keywords if kw in performance_keywords)
        
        # Conta palavras-chave relacionadas a features
        feature_keywords = ["sistema", "feature", "mecânica", "gameplay"]
        feature_count = sum(1 for kw in keywords if kw in feature_keywords)
        
        # Conta palavras-chave relacionadas a bugs
        bug_keywords = ["bug", "erro", "problema"]
        bug_count = sum(1 for kw in keywords if kw in bug_keywords)
        
        if performance_count >= 2 or feature_count >= 2:
            return "high"
        elif bug_count >= 1 or performance_count == 1 or feature_count == 1:
            return "medium"
        else:
            return "low"
    
    def identify_primary_workflow(self, keywords: List[str], workflows: set) -> str:
        """Identifica o workflow principal baseado nas palavras-chave"""
        # Prioriza workflows específicos
        if "performance" in keywords or "otimização" in keywords:
            return "performance_optimization"
        elif "sistema" in keywords or "feature" in keywords:
            return "feature_development"
        elif "bug" in keywords or "erro" in keywords:
            return "bug_fix"
        elif "módulo" in keywords or "Lua" in keywords:
            return "module_development"
        elif "interface" in keywords or "UI" in keywords or "UX" in keywords:
            return "ui_development"
        else:
            return "feature_development"  # Default
    
    def select_agents(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Seleciona agentes baseado no contexto"""
        print(f"👥 Selecionando agentes para: {context['description']}")
        
        primary_workflow = context['primary_workflow']
        workflow_config = self.workflows.get(primary_workflow, {})
        
        selected_agents = []
        for agent_id in workflow_config.get('agents', []):
            agent_info = self.agent_personalities.get(agent_id, {})
            selected_agents.append({
                "id": agent_id,
                "name": agent_info.get('name', agent_id),
                "expertise": agent_info.get('expertise', ''),
                "personality": agent_info.get('personality', ''),
                "role": self.get_agent_role(agent_id, primary_workflow)
            })
        
        agent_workflow = {
            "workflow_type": primary_workflow,
            "agents": selected_agents,
            "phases": workflow_config.get('phases', []),
            "estimated_duration": workflow_config.get('estimated_duration', '1-2 hours'),
            "description": workflow_config.get('description', 'Tarefa personalizada')
        }
        
        print(f"✅ Agentes selecionados: {len(selected_agents)}")
        for agent in selected_agents:
            print(f"   - {agent['name']} ({agent['role']})")
        
        return agent_workflow
    
    def get_agent_role(self, agent_id: str, workflow_type: str) -> str:
        """Define o papel específico do agente no workflow"""
        roles = {
            "performance_optimization": {
                "engine_developer": "Analisa e otimiza código C++",
                "content_creator": "Cria módulos Lua de monitoramento",
                "qa_tester": "Valida melhorias de performance"
            },
            "feature_development": {
                "game_designer": "Designa sistema e mecânicas",
                "engine_developer": "Implementa core em C++",
                "content_creator": "Cria conteúdo Lua e OTUI",
                "qa_tester": "Testa feature completa"
            },
            "bug_fix": {
                "qa_tester": "Identifica e documenta bug",
                "engine_developer": "Corrige código C++ se necessário",
                "content_creator": "Corrige scripts Lua se necessário"
            },
            "module_development": {
                "content_creator": "Designa e implementa módulo Lua",
                "qa_tester": "Testa funcionalidade do módulo"
            },
            "ui_development": {
                "level_designer": "Designa interface e UX",
                "content_creator": "Implementa OTUI",
                "qa_tester": "Testa usabilidade"
            }
        }
        
        return roles.get(workflow_type, {}).get(agent_id, "Executa tarefas específicas")
    
    def execute_workflow(self, agent_workflow: Dict[str, Any]) -> Dict[str, Any]:
        """Executa o workflow coordenado"""
        print(f"🚀 Iniciando workflow: {agent_workflow['description']}")
        print(f"⏰ Duração estimada: {agent_workflow['estimated_duration']}")
        
        start_time = time.time()
        execution_results = {
            "workflow": agent_workflow,
            "start_time": datetime.now().isoformat(),
            "phases": [],
            "agents_results": {},
            "overall_status": "in_progress"
        }
        
        # Executa cada fase
        for i, phase in enumerate(agent_workflow['phases'], 1):
            print(f"\n📋 Fase {i}: {phase}")
            
            # Identifica agentes para esta fase
            phase_agents = self.get_agents_for_phase(phase, agent_workflow['agents'])
            
            phase_result = {
                "phase": phase,
                "phase_number": i,
                "agents": phase_agents,
                "status": "completed",
                "start_time": datetime.now().isoformat(),
                "end_time": None,
                "output": f"Fase {phase} executada com sucesso"
            }
            
            # Simula execução da fase
            time.sleep(1)  # Simula tempo de processamento
            
            phase_result["end_time"] = datetime.now().isoformat()
            execution_results["phases"].append(phase_result)
            
            # Reporta progresso
            progress = (i / len(agent_workflow['phases'])) * 100
            self.report_phase_progress(phase, phase_agents, progress)
        
        execution_results["end_time"] = datetime.now().isoformat()
        execution_results["overall_status"] = "completed"
        execution_results["total_duration"] = time.time() - start_time
        
        print(f"\n✅ Workflow concluído em {execution_results['total_duration']:.2f}s")
        
        return execution_results
    
    def get_agents_for_phase(self, phase: str, agents: List[Dict]) -> List[Dict]:
        """Identifica agentes responsáveis por cada fase"""
        phase_agent_mapping = {
            "analysis": [agent for agent in agents if agent['id'] == 'engine_developer'],
            "optimization": [agent for agent in agents if agent['id'] == 'engine_developer'],
            "design": [agent for agent in agents if agent['id'] in ['game_designer', 'level_designer']],
            "implementation": [agent for agent in agents if agent['id'] in ['engine_developer', 'content_creator']],
            "integration": [agent for agent in agents if agent['id'] == 'content_creator'],
            "content": [agent for agent in agents if agent['id'] == 'content_creator'],
            "identification": [agent for agent in agents if agent['id'] == 'qa_tester'],
            "fix": [agent for agent in agents if agent['id'] in ['engine_developer', 'content_creator']],
            "testing": [agent for agent in agents if agent['id'] == 'qa_tester'],
            "validation": [agent for agent in agents if agent['id'] == 'qa_tester']
        }
        
        return phase_agent_mapping.get(phase, agents)
    
    def report_phase_progress(self, phase: str, agents: List[Dict], progress: float):
        """Reporta progresso da fase"""
        agent_names = [agent['name'] for agent in agents]
        print(f"   👥 {', '.join(agent_names)}: {phase}")
        print(f"   📊 Progresso: {progress:.1f}%")
    
    def generate_progress_report(self, execution_results: Dict[str, Any]) -> str:
        """Gera relatório de progresso em tempo real"""
        workflow = execution_results['workflow']
        
        report = f"""
🤖 **Orquestração Inteligente Ativa**
🎯 **Tarefa**: {workflow['description']}
⏱️ **Status**: {execution_results['overall_status']}
👥 **Agentes**: {len(workflow['agents'])} agentes coordenados
📋 **Fases**: {len(workflow['phases'])} fases executadas
⏰ **Duração**: {execution_results.get('total_duration', 0):.2f}s

📊 **Progresso por Fase:**
"""
        
        for phase_result in execution_results['phases']:
            agent_names = [agent['name'] for agent in phase_result['agents']]
            report += f"   ✅ {phase_result['phase']} - {', '.join(agent_names)}\n"
        
        report += f"""
🎉 **Resultado Final:**
   - Workflow: {workflow['workflow_type']}
   - Status: {execution_results['overall_status']}
   - Duração Total: {execution_results.get('total_duration', 0):.2f}s
   - Agentes Utilizados: {len(workflow['agents'])}
"""
        
        return report
    
    def orchestrate_request(self, user_request: str) -> Dict[str, Any]:
        """Orquestra automaticamente o pedido do usuário"""
        print("🎯 Iniciando Orquestração Inteligente")
        print("=" * 50)
        
        # 1. Analisa contexto
        context = self.analyze_context(user_request)
        
        # 2. Seleciona agentes
        agent_workflow = self.select_agents(context)
        
        # 3. Executa workflow
        execution_results = self.execute_workflow(agent_workflow)
        
        # 4. Gera relatório
        progress_report = self.generate_progress_report(execution_results)
        
        # 5. Salva resultados
        self.save_execution_results(execution_results)
        
        return {
            "context": context,
            "workflow": agent_workflow,
            "execution": execution_results,
            "report": progress_report
        }
    
    def save_execution_results(self, execution_results: Dict[str, Any]):
        """Salva resultados da execução"""
        try:
            # Carrega histórico existente
            history_file = "wiki/maps/orchestration_history.json"
            try:
                with open(history_file, 'r', encoding='utf-8') as f:
                    history = json.load(f)
            except FileNotFoundError:
                history = {"executions": []}
            
            # Adiciona nova execução
            execution_record = {
                "timestamp": datetime.now().isoformat(),
                "workflow_type": execution_results['workflow']['workflow_type'],
                "description": execution_results['workflow']['description'],
                "agents_used": len(execution_results['workflow']['agents']),
                "duration": execution_results.get('total_duration', 0),
                "status": execution_results['overall_status']
            }
            
            history["executions"].append(execution_record)
            
            # Mantém apenas as últimas 50 execuções
            if len(history["executions"]) > 50:
                history["executions"] = history["executions"][-50:]
            
            # Salva histórico
            with open(history_file, 'w', encoding='utf-8') as f:
                json.dump(history, f, indent=2, ensure_ascii=False)
            
            print(f"💾 Histórico salvo em: {history_file}")
            
        except Exception as e:
            print(f"⚠️ Erro ao salvar histórico: {e}")

def main():
    """Função principal para teste do sistema"""
    orchestrator = IntelligentOrchestrator()
    
    # Exemplos de teste
    test_requests = [
        "Otimize a performance do OTClient",
        "Crie um sistema de guilds para o OTClient",
        "Corrija o bug no módulo de inventário",
        "Desenvolva uma nova interface para configurações",
        "Implemente memory compression LZ4 no OTClient"
    ]
    
    print("🧪 Testando Sistema de Orquestração Inteligente")
    print("=" * 60)
    
    for i, request in enumerate(test_requests, 1):
        print(f"\n🔍 Teste {i}: {request}")
        print("-" * 40)
        
        try:
            result = orchestrator.orchestrate_request(request)
            print(result['report'])
        except Exception as e:
            print(f"❌ Erro no teste {i}: {e}")
        
        print("\n" + "=" * 60)

if __name__ == "__main__":
    main() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = WorkflowmanagerModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script intelligent_orchestrator.py executado com sucesso via módulo agents.workflow_manager")
    else:
        print(f"❌ Erro na execução do script intelligent_orchestrator.py via módulo agents.workflow_manager")


# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = MapupdaterModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script migrated_intelligent_orchestrator.py executado com sucesso via módulo maps.map_updater")
    else:
        print(f"❌ Erro na execução do script migrated_intelligent_orchestrator.py via módulo maps.map_updater")
