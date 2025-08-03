from unicode_aliases import *
from datetime import datetime
from typing import Dict, List, Any, Set
import json
import os
import re

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enhanced Intelligent Orchestrator
Versão melhorada com detecção de extensões de arquivo e contextos mais específicos
"""


class EnhancedContextAnalyzer:
    """Analisador de contexto melhorado com detecção de extensões de arquivo"""
    
    def __init__(self):
        # Detecção de extensões de arquivo
        self.file_extensions = {
            ".lua": ["content_creator", "module_development"],
            ".cpp": ["engine_developer", "core_development"],
            ".hpp": ["engine_developer", "core_development"],
            ".h": ["engine_developer", "core_development"],
            ".otui": ["content_creator", "ui_development"],
            ".otmod": ["content_creator", "module_development"],
            ".md": ["content_creator", "documentation"],
            ".json": ["content_creator", "data_management"],
            ".py": ["python_agent", "python_development"],
            ".cmake": ["engine_developer", "build_management"],
            ".txt": ["content_creator", "documentation"],
            ".html": ["content_creator", "ui_development"],
            ".css": ["content_creator", "ui_development"],
            ".js": ["content_creator", "ui_development"]
        }
        
        # Padrões de contexto específico
        self.context_patterns = {
            "lua_file_edit": {
                "keywords": ["editar", "arquivo", "lua", ".lua", "módulo", "script"],
                "agents": ["content_creator"],
                "workflow": "module_development"
            },
            "cpp_file_edit": {
                "keywords": ["editar", "arquivo", "c++", ".cpp", ".hpp", ".h", "código", "core"],
                "agents": ["engine_developer"],
                "workflow": "core_development"
            },
            "bug_fix_lua": {
                "keywords": ["bug", "lua", "módulo", "corrigir", "erro", "problema"],
                "agents": ["qa_tester", "content_creator"],
                "workflow": "bug_fix"
            },
            "bug_fix_cpp": {
                "keywords": ["bug", "c++", "core", "corrigir", "erro", "problema"],
                "agents": ["qa_tester", "engine_developer"],
                "workflow": "bug_fix"
            },
            "performance_optimization": {
                "keywords": ["lento", "performance", "otimizar", "velocidade", "memória"],
                "agents": ["engine_developer", "content_creator", "qa_tester"],
                "workflow": "performance_optimization"
            },
            "new_feature": {
                "keywords": ["nova", "feature", "sistema", "mecânica", "funcionalidade"],
                "agents": ["game_designer", "engine_developer", "content_creator", "qa_tester"],
                "workflow": "feature_development"
            },
            "ui_development": {
                "keywords": ["interface", "ui", "ux", "design", "layout", "usabilidade"],
                "agents": ["level_designer", "content_creator", "qa_tester"],
                "workflow": "ui_development"
            },
            "documentation": {
                "keywords": ["documentar", "wiki", "manual", "guia", "explicar"],
                "agents": ["content_creator", "game_designer"],
                "workflow": "documentation"
            }
        }
        
        # Palavras-chave específicas por tecnologia
        self.technology_keywords = {
            "C++": {
                "keywords": ["C++", "cpp", "hpp", "h", "OpenGL", "ASIO", "VCPKG", "CMake", "compilação"],
                "agents": ["engine_developer"],
                "workflows": ["core_development", "performance_optimization", "bug_fix"]
            },
            "python_file_edit": {
                "keywords": ["editar", "arquivo", "python", ".py", "script", "automação"],
                "agents": ["python_agent"],
                "workflow": "python_development"
            },
            "python_optimization": {
                "keywords": ["otimizar", "python", "qualidade", "refatorar", "melhorar"],
                "agents": ["python_agent"],
                "workflow": "python_optimization"
            },
            "python_bug_fix": {
                "keywords": ["bug", "python", "erro", "corrigir", "problema"],
                "agents": ["python_agent", "qa_tester"],
                "workflow": "python_bug_fix"
            },

            "Lua": {
                "keywords": ["Lua", "lua", "otui", "otmod", "script", "módulo"],
                "agents": ["content_creator"],
                "workflows": ["module_development", "ui_development", "bug_fix"]
            },
            "Python": {
                "keywords": ["Python", "python", "py", "script", "automação", "scripting"],
                "agents": ["python_agent"],
                "workflows": ["python_development", "python_optimization", "python_bug_fix"]
            },

            "OTClient": {
                "keywords": ["OTClient", "cliente", "client", "protocolo", "opcode"],
                "agents": ["engine_developer", "content_creator"],
                "workflows": ["core_development", "module_development"]
            },
            "Canary": {
                "keywords": ["Canary", "servidor", "server", "protocolo", "opcode"],
                "agents": ["engine_developer", "devops_engineer"],
                "workflows": ["core_development", "deployment"]
            }
        }
    
    def analyze_request(self, user_request: str) -> Dict[str, Any]:
        """Análise completa do pedido do usuário"""
        print(f"🔍 Analisando pedido: '{user_request}'")
        
        # Normaliza o texto
        text = user_request.lower()
        
        # Detecta extensões de arquivo
        file_extensions = self.detect_file_extensions(text)
        
        # Detecta padrões de contexto
        context_patterns = self.detect_context_patterns(text)
        
        # Detecta tecnologias
        technologies = self.detect_technologies(text)
        
        # Combina todas as detecções
        combined_analysis = self.combine_analysis(file_extensions, context_patterns, technologies)
        
        # Determina complexidade
        complexity = self.analyze_complexity(text, combined_analysis)
        
        # Identifica workflow principal
        primary_workflow = self.identify_primary_workflow(combined_analysis)
        
        analysis_result = {
            "original_request": user_request,
            "file_extensions": file_extensions,
            "context_patterns": context_patterns,
            "technologies": technologies,
            "detected_agents": list(combined_analysis["agents"]),
            "detected_workflows": list(combined_analysis["workflows"]),
            "complexity": complexity,
            "primary_workflow": primary_workflow,
            "confidence_score": self.calculate_confidence(combined_analysis)
        }
        
        print(f"📁 Extensões detectadas: {file_extensions}")
        print(f"🎯 Padrões detectados: {list(context_patterns.keys())}")
        print(f"🔧 Tecnologias detectadas: {list(technologies.keys())}")
        print(f"👥 Agentes necessários: {', '.join(analysis_result['detected_agents'])}")
        print(f"📊 Complexidade: {complexity}")
        print(f"🎯 Workflow principal: {primary_workflow}")
        print(f"📈 Confiança: {analysis_result['confidence_score']:.1f}%")
        
        return analysis_result
    
    def detect_file_extensions(self, text: str) -> List[str]:
        """Detecta extensões de arquivo no texto"""
        extensions = []
        for ext in self.file_extensions.keys():
            if ext in text or ext.replace(".", "") in text:
                extensions.append(ext)
        return extensions
    
    def detect_context_patterns(self, text: str) -> Dict[str, Any]:
        """Detecta padrões de contexto específicos"""
        detected_patterns = {}
        for pattern_name, pattern_config in self.context_patterns.items():
            keyword_matches = sum(1 for kw in pattern_config["keywords"] if kw in text)
            if keyword_matches >= 2:  # Pelo menos 2 palavras-chave
                detected_patterns[pattern_name] = {
                    "agents": pattern_config["agents"],
                    "workflow": pattern_config["workflow"],
                    "confidence": keyword_matches / len(pattern_config["keywords"])
                }
        return detected_patterns
    
    def detect_technologies(self, text: str) -> Dict[str, Any]:
        """Detecta tecnologias mencionadas"""
        detected_technologies = {}
        for tech_name, tech_config in self.technology_keywords.items():
            keyword_matches = sum(1 for kw in tech_config["keywords"] if kw.lower() in text)
            if keyword_matches > 0:
                detected_technologies[tech_name] = {
                    "agents": tech_config["agents"],
                    "workflows": tech_config["workflows"],
                    "confidence": keyword_matches / len(tech_config["keywords"])
                }
        return detected_technologies
    
    def combine_analysis(self, file_extensions: List[str], context_patterns: Dict, technologies: Dict) -> Dict[str, Any]:
        """Combina todas as análises"""
        all_agents = set()
        all_workflows = set()
        
        # Adiciona agentes de extensões de arquivo
        for ext in file_extensions:
            if ext in self.file_extensions:
                all_agents.update(self.file_extensions[ext])
        
        # Adiciona agentes de padrões de contexto
        for pattern_data in context_patterns.values():
            all_agents.update(pattern_data["agents"])
            all_workflows.add(pattern_data["workflow"])
        
        # Adiciona agentes de tecnologias
        for tech_data in technologies.values():
            all_agents.update(tech_data["agents"])
            all_workflows.update(tech_data["workflows"])
        
        return {
            "agents": all_agents,
            "workflows": all_workflows
        }
    
    def analyze_complexity(self, text: str, analysis: Dict[str, Any]) -> str:
        """Analisa complexidade baseada no contexto"""
        agent_count = len(analysis["agents"])
        workflow_count = len(analysis["workflows"])
        
        # Palavras-chave de complexidade
        high_complexity_keywords = ["sistema", "feature", "otimização", "performance", "mecânica"]
        medium_complexity_keywords = ["módulo", "bug", "corrigir", "interface"]
        
        high_count = sum(1 for kw in high_complexity_keywords if kw in text)
        medium_count = sum(1 for kw in medium_complexity_keywords if kw in text)
        
        if agent_count >= 3 or workflow_count >= 2 or high_count >= 2:
            return "high"
        elif agent_count >= 2 or medium_count >= 1:
            return "medium"
        else:
            return "low"
    
    def identify_primary_workflow(self, analysis: Dict[str, Any]) -> str:
        """Identifica o workflow principal"""
        workflows = analysis["workflows"]
        
        # Prioriza workflows específicos
        if "performance_optimization" in workflows:
            return "performance_optimization"
        elif "bug_fix" in workflows:
            return "bug_fix"
        elif "feature_development" in workflows:
            return "feature_development"
        elif "module_development" in workflows:
            return "module_development"
        elif "ui_development" in workflows:
            return "ui_development"
        elif "core_development" in workflows:
            return "core_development"
        else:
            return "feature_development"  # Default
    
    def calculate_confidence(self, analysis: Dict[str, Any]) -> float:
        """Calcula score de confiança da análise"""
        agent_count = len(analysis["agents"])
        workflow_count = len(analysis["workflows"])
        
        # Base score
        base_score = 50.0
        
        # Bônus por múltiplos indicadores
        if agent_count > 0:
            base_score += 20.0
        if workflow_count > 0:
            base_score += 20.0
        if agent_count >= 2:
            base_score += 10.0
        
        return min(base_score, 100.0)

class EnhancedIntelligentOrchestrator:
    """Orquestrador inteligente melhorado"""
    
    def __init__(self):
        self.analyzer = EnhancedContextAnalyzer()
        
        # Workflows específicos para edição de arquivos
        self.file_edit_workflows = {
            "lua_edit": {
                "agents": ["content_creator"],
                "phases": ["analysis", "implementation", "testing"],
                "description": "Edição de arquivo Lua",
                "estimated_duration": "1-2 hours"
            },
            "python_development": {
                "agents": ["python_agent"],
                "phases": ["analysis", "implementation", "optimization", "testing"],
                "description": "Desenvolvimento de scripts Python",
                "estimated_duration": "1-2 hours"
            },
            "python_optimization": {
                "agents": ["python_agent"],
                "phases": ["analysis", "optimization", "validation"],
                "description": "Otimização de código Python existente",
                "estimated_duration": "30min-1h"
            },
            "python_bug_fix": {
                "agents": ["python_agent", "qa_tester"],
                "phases": ["identification", "fix", "validation"],
                "description": "Correção de bugs em código Python",
                "estimated_duration": "1-2 hours"
            },
            "cpp_edit": {
                "agents": ["engine_developer"],
                "phases": ["analysis", "implementation", "testing"],
                "description": "Edição de arquivo C++",
                "estimated_duration": "2-3 hours"
            },
            "bug_fix_lua": {
                "agents": ["qa_tester", "content_creator"],
                "phases": ["identification", "fix", "validation"],
                "description": "Correção de bug em Lua",
                "estimated_duration": "1-2 hours"
            },
            "bug_fix_cpp": {
                "agents": ["qa_tester", "engine_developer"],
                "phases": ["identification", "fix", "validation"],
                "description": "Correção de bug em C++",
                "estimated_duration": "2-3 hours"
            },
            "performance_optimization": {
                "agents": ["engine_developer", "content_creator", "qa_tester"],
                "phases": ["analysis", "optimization", "integration", "testing"],
                "description": "Otimização de performance",
                "estimated_duration": "3-4 hours"
            },
            "feature_development": {
                "agents": ["game_designer", "engine_developer", "content_creator", "qa_tester"],
                "phases": ["design", "implementation", "content", "testing"],
                "description": "Desenvolvimento de nova feature",
                "estimated_duration": "4-6 hours"
            },
            "ui_development": {
                "agents": ["level_designer", "content_creator", "qa_tester"],
                "phases": ["design", "implementation", "testing"],
                "description": "Desenvolvimento de interface",
                "estimated_duration": "2-4 hours"
            },
            "documentation": {
                "agents": ["content_creator", "game_designer"],
                "phases": ["research", "writing", "review"],
                "description": "Criação de documentação",
                "estimated_duration": "1-3 hours"
            }
        }
        
        # Personalidades dos agentes
        self.agent_personalities = {
            "engine_developer": {
                "name": "Zara",
                "expertise": "C++ Development, Performance Optimization, Memory Management",
                "personality": "Analytical, performance-focused, technical expert",
                "specializations": ["C++", "OpenGL", "ASIO", "VCPKG", "CMake"]
            },
            "python_agent": {
                "name": "Py",
                "expertise": "Python Development, Code Quality, Automation Scripts",
                "personality": "Analytical, quality-focused, continuous optimizer",
                "specializations": ["Python", "Code Quality", "Automation", "Scripting"]
            },
            "content_creator": {
                "name": "Maya",
                "expertise": "Lua Scripting, Module Development, UI Scripting",
                "personality": "Creative, detail-oriented, user-focused",
                "specializations": ["Lua", "OTUI", "OTMod", "Scripting"]
            },
            "game_designer": {
                "name": "Alex",
                "expertise": "Game Systems, Feature Design, Gameplay Mechanics",
                "personality": "Innovative, player-focused, systems thinker",
                "specializations": ["Game Design", "Systems", "Mechanics"]
            },
            "qa_tester": {
                "name": "Sam",
                "expertise": "Quality Assurance, Bug Detection, Testing Strategies",
                "personality": "Thorough, methodical, quality-focused",
                "specializations": ["Testing", "Bug Fix", "Quality"]
            },
            "devops_engineer": {
                "name": "Jordan",
                "expertise": "Deployment, CI/CD, Infrastructure Management",
                "personality": "Efficient, automation-focused, reliability-driven",
                "specializations": ["Deployment", "CI/CD", "Infrastructure"]
            },
            "level_designer": {
                "name": "Casey",
                "expertise": "UI/UX Design, User Experience, Interface Design",
                "personality": "User-centric, aesthetic-focused, experience-driven",
                "specializations": ["UI/UX", "Design", "Experience"]
            },
            "game_team_orchestrator": {
                "name": "Riley",
                "expertise": "Project Management, Team Coordination, Workflow Optimization",
                "personality": "Organized, leadership-focused, coordination expert",
                "specializations": ["Management", "Coordination", "Workflow"]
            }
        }
    
    def orchestrate_request(self, user_request: str) -> Dict[str, Any]:
        """Orquestra o pedido do usuário com análise melhorada"""
        print(f"🤖 Iniciando orquestração inteligente melhorada")
        print(f"📝 Pedido: '{user_request}'")
        print("=" * 60)
        
        # Análise de contexto melhorada
        context_analysis = self.analyzer.analyze_request(user_request)
        
        # Seleção de agentes
        agent_workflow = self.select_agents(context_analysis)
        
        # Execução do workflow
        execution_results = self.execute_workflow(agent_workflow)
        
        # Geração de relatório
        progress_report = self.generate_progress_report(execution_results)
        
        # Salva resultados
        self.save_execution_results(execution_results)
        
        return {
            "context_analysis": context_analysis,
            "agent_workflow": agent_workflow,
            "execution_results": execution_results,
            "progress_report": progress_report
        }
    
    def select_agents(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Seleciona agentes baseado no contexto melhorado"""
        print(f"👥 Selecionando agentes para: {context['primary_workflow']}")
        
        primary_workflow = context['primary_workflow']
        workflow_config = self.file_edit_workflows.get(primary_workflow, {})
        
        selected_agents = []
        for agent_id in workflow_config.get('agents', []):
            agent_info = self.agent_personalities.get(agent_id, {})
            selected_agents.append({
                "id": agent_id,
                "name": agent_info.get('name', agent_id),
                "expertise": agent_info.get('expertise', ''),
                "personality": agent_info.get('personality', ''),
                "specializations": agent_info.get('specializations', []),
                "role": self.get_agent_role(agent_id, primary_workflow)
            })
        
        agent_workflow = {
            "workflow_type": primary_workflow,
            "agents": selected_agents,
            "phases": workflow_config.get('phases', []),
            "estimated_duration": workflow_config.get('estimated_duration', '1-2 hours'),
            "description": workflow_config.get('description', 'Tarefa personalizada'),
            "confidence_score": context.get('confidence_score', 0.0)
        }
        
        print(f"✅ Agentes selecionados: {len(selected_agents)}")
        for agent in selected_agents:
            print(f"   - {agent['name']} ({agent['role']})")
            print(f"     Especializações: {', '.join(agent['specializations'])}")
        
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
                "qa_tester": "Testa módulo implementado"
            },
            "ui_development": {
                "level_designer": "Cria design de interface",
                "content_creator": "Implementa OTUI",
                "qa_tester": "Testa interface"
            },
            "core_development": {
                "engine_developer": "Implementa funcionalidades core em C++",
                "qa_tester": "Testa implementações"
            },
            "documentation": {
                "content_creator": "Escreve documentação técnica",
                "game_designer": "Revisa conteúdo e estrutura"
            },
            "python_development": {
                "python_agent": "Analisa, implementa e otimiza scripts Python"
            },
            "python_optimization": {
                "python_agent": "Otimiza código Python existente e melhora qualidade"
            },
            "python_bug_fix": {
                "python_agent": "Identifica e corrige bugs em código Python",
                "qa_tester": "Valida correções e testa funcionalidade"
            },

        }
        
        return roles.get(workflow_type, {}).get(agent_id, "Contribui para a tarefa")
    
    def execute_workflow(self, agent_workflow: Dict[str, Any]) -> Dict[str, Any]:
        """Executa o workflow com os agentes selecionados"""
        print(f"\n🚀 Executando workflow: {agent_workflow['description']}")
        print(f"⏱️ Duração estimada: {agent_workflow['estimated_duration']}")
        print(f"📊 Confiança: {agent_workflow['confidence_score']:.1f}%")
        
        execution_results = {
            "workflow_type": agent_workflow['workflow_type'],
            "description": agent_workflow['description'],
            "agents": agent_workflow['agents'],
            "phases": agent_workflow['phases'],
            "execution_log": [],
            "start_time": datetime.now().isoformat(),
            "status": "completed"
        }
        
        total_phases = len(agent_workflow['phases'])
        
        for i, phase in enumerate(agent_workflow['phases'], 1):
            print(f"\n📋 Fase {i}/{total_phases}: {phase}")
            
            # Identifica agentes para esta fase
            phase_agents = self.get_agents_for_phase(phase, agent_workflow['agents'])
            
            # Simula execução da fase
            phase_result = self.simulate_phase_execution(phase, phase_agents)
            
            execution_results['execution_log'].append(phase_result)
            
            # Reporta progresso
            progress = (i / total_phases) * 100
            self.report_phase_progress(phase, phase_agents, progress)
        
        execution_results['end_time'] = datetime.now().isoformat()
        execution_results['total_duration'] = "2h 15min"  # Simulado
        
        print(f"\n✅ Workflow concluído com sucesso!")
        print(f"📊 Resultado: {execution_results['description']}")
        
        return execution_results
    
    def get_agents_for_phase(self, phase: str, agents: List[Dict]) -> List[Dict]:
        """Identifica agentes responsáveis por cada fase"""
        phase_agent_mapping = {
            "analysis": [a for a in agents if a['id'] in ['engine_developer', 'content_creator']],
            "design": [a for a in agents if a['id'] in ['game_designer', 'level_designer']],
            "implementation": [a for a in agents if a['id'] in ['engine_developer', 'content_creator']],
            "content": [a for a in agents if a['id'] in ['content_creator']],
            "testing": [a for a in agents if a['id'] in ['qa_tester']],
            "optimization": [a for a in agents if a['id'] in ['engine_developer']],
            "integration": [a for a in agents if a['id'] in ['content_creator']],
            "identification": [a for a in agents if a['id'] in ['qa_tester']],
            "fix": [a for a in agents if a['id'] in ['engine_developer', 'content_creator']],
            "validation": [a for a in agents if a['id'] in ['qa_tester']],
            "research": [a for a in agents if a['id'] in ['content_creator']],
            "writing": [a for a in agents if a['id'] in ['content_creator']],
            "review": [a for a in agents if a['id'] in ['game_designer']]
        }
        
        return phase_agent_mapping.get(phase, agents)
    
    def simulate_phase_execution(self, phase: str, agents: List[Dict]) -> Dict[str, Any]:
        """Simula execução de uma fase"""
        agent_names = [agent['name'] for agent in agents]
        
        phase_actions = {
            "analysis": f"Análise técnica realizada por {', '.join(agent_names)}",
            "design": f"Design criado por {', '.join(agent_names)}",
            "implementation": f"Implementação realizada por {', '.join(agent_names)}",
            "content": f"Conteúdo criado por {', '.join(agent_names)}",
            "testing": f"Testes executados por {', '.join(agent_names)}",
            "optimization": f"Otimização realizada por {', '.join(agent_names)}",
            "integration": f"Integração realizada por {', '.join(agent_names)}",
            "identification": f"Identificação realizada por {', '.join(agent_names)}",
            "fix": f"Correção realizada por {', '.join(agent_names)}",
            "validation": f"Validação realizada por {', '.join(agent_names)}",
            "research": f"Pesquisa realizada por {', '.join(agent_names)}",
            "writing": f"Escrita realizada por {', '.join(agent_names)}",
            "review": f"Revisão realizada por {', '.join(agent_names)}"
        }
        
        return {
            "phase": phase,
            "agents": [agent['name'] for agent in agents],
            "action": phase_actions.get(phase, f"Fase {phase} executada"),
            "status": "completed",
            "duration": "15-30 min"
        }
    
    def report_phase_progress(self, phase: str, agents: List[Dict], progress: float):
        """Reporta progresso da fase"""
        agent_names = [agent['name'] for agent in agents]
        print(f"   👥 Agentes: {', '.join(agent_names)}")
        print(f"   📈 Progresso: {progress:.1f}%")
        print(f"   ✅ Status: Concluído")
    
    def generate_progress_report(self, execution_results: Dict[str, Any]) -> str:
        """Gera relatório de progresso"""
        print(f"\n📋 GERANDO RELATÓRIO DE PROGRESSO")
        print("=" * 50)
        
        report = f"""
# Relatório de Orquestração Inteligente

## 🎯 Workflow Executado
- **Tipo**: {execution_results['workflow_type']}
- **Descrição**: {execution_results['description']}
- **Duração**: {execution_results['total_duration']}
- **Status**: {execution_results['status']}

## 👥 Agentes Participantes
"""
        
        for agent in execution_results['agents']:
            report += f"- **{agent['name']}** ({agent['role']})\n"
        
        report += f"""
## 📋 Fases Executadas
"""
        
        for phase_log in execution_results['execution_log']:
            report += f"- **{phase_log['phase']}**: {phase_log['action']} ({phase_log['duration']})\n"
        
        report += f"""
## 📊 Resultados
- ✅ Workflow executado com sucesso
- ✅ Todos os agentes participaram ativamente
- ✅ Fases concluídas conforme planejado
- ✅ Objetivos alcançados

## 🚀 Próximos Passos
1. Implementar as melhorias identificadas
2. Validar resultados com testes
3. Documentar aprendizados
4. Preparar para próxima iteração
"""
        
        print("✅ Relatório gerado com sucesso!")
        return report
    
    def save_execution_results(self, execution_results: Dict[str, Any]):
        """Salva resultados da execução"""
        try:
            # Cria diretório se não existir
            maps_dir = os.path.join(os.path.dirname(__file__), '..', 'maps')
            os.makedirs(maps_dir, exist_ok=True)
            
            # Salva resultados
            results_file = os.path.join(maps_dir, 'enhanced_orchestration_results.json')
            
            # Adiciona timestamp
            execution_results['saved_at'] = datetime.now().isoformat()
            
            with open(results_file, 'w', encoding='utf-8') as f:
                json.dump(execution_results, f, indent=2, ensure_ascii=False)
            
            print(f"💾 Resultados salvos em: {results_file}")
            
        except Exception as e:
            print(f"❌ Erro ao salvar resultados: {e}")

def main():
    """Função principal para teste"""
    orchestrator = EnhancedIntelligentOrchestrator()
    
    # Teste com diferentes cenários
    test_scenarios = [
        "Vou editar um arquivo Lua para criar um módulo de inventário",
        "Vou editar um arquivo C++ para otimizar a performance do sistema de renderização",
        "Preciso corrigir um bug no módulo Lua de inventário",
        "Vou criar uma nova feature de guilds que precisa de C++ e Lua",
        "O sistema está lento, preciso otimizar a performance do OTClient"
    ]
    
    print("🧪 TESTE DO ORQUESTRADOR MELHORADO")
    print("=" * 60)
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"\n🔍 CENÁRIO {i}: {scenario}")
        print("-" * 50)
        
        try:
            result = orchestrator.orchestrate_request(scenario)
            print(f"✅ Cenário {i} executado com sucesso!")
        except Exception as e:
            print(f"❌ Erro no cenário {i}: {e}")
        
        print("\n" + "=" * 60)

if __name__ == "__main__":
    main() 