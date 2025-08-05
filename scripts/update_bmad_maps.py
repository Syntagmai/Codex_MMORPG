#!/usr/bin/env python3
"""
Script para atualização automática dos mapas JSON do sistema BMAD
Atualiza: maps/bmad_agents_index.json, maps/bmad_workflows_index.json, maps/bmad_templates_index.json
"""
import os
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any

class BMADMapUpdater:
    def __init__(self, wiki_dir: str = "wiki"):
        self.wiki_dir = Path(wiki_dir)
        self.bmad_dir = self.wiki_dir / "bmad"
        
        # Detectar contexto
        self.context_data = self.load_context_data()
        
        # Dados dos agentes BMAD
        self.agents_data = {
            "game_designer": {
                "name": "Game Designer (Luna)",
                "personality": "Criativa, focada em experiência do jogador",
                "expertise": ["Game Mechanics", "Player Experience", "Balance Design", "Progression Systems"],
                "commands": ["@game_designer"],
                "workflows": ["feature-design", "balance-analysis", "player-journey"],
                "templates": ["Game Design Document", "Feature Specification", "Balance Analysis Report"]
            },
            "engine_developer": {
                "name": "Engine Developer (Zara)",
                "personality": "Técnica, focada em performance e arquitetura",
                "expertise": ["C++ Development", "Performance Optimization", "Memory Management", "System Architecture"],
                "commands": ["@engine_developer"],
                "workflows": ["performance-optimization", "system-architecture", "code-optimization"],
                "templates": ["Technical Specification", "Performance Analysis Report", "Architecture Design Document"]
            },
            "content_creator": {
                "name": "Content Creator (Maya)",
                "personality": "Criativa, focada em narrativa e conteúdo",
                "expertise": ["Lua Scripting", "Quest Design", "NPC Systems", "Narrative Design"],
                "commands": ["@content_creator"],
                "workflows": ["content-pipeline", "quest-design", "npc-development"],
                "templates": ["Quest Design Document", "NPC Specification", "Content Integration Guide"]
            },
            "level_designer": {
                "name": "Level Designer (River)",
                "personality": "Visual, focada em experiência espacial",
                "expertise": ["Map Design", "Player Flow", "Environmental Storytelling", "Spatial Gameplay"],
                "commands": ["@level_designer"],
                "workflows": ["area-design", "flow-optimization", "environmental-design"],
                "templates": ["Level Design Document", "Area Specification", "Flow Analysis Report"]
            },
            "qa_tester": {
                "name": "QA Tester (Alex)",
                "personality": "Analítica, focada em qualidade",
                "expertise": ["Game Testing", "Balance Validation", "Bug Tracking", "Performance Testing"],
                "commands": ["@qa_tester"],
                "workflows": ["feature-testing", "balance-validation", "bug-analysis"],
                "templates": ["Test Plan", "Bug Report", "Performance Analysis"]
            },
            "devops_engineer": {
                "name": "DevOps Engineer (Jordan)",
                "personality": "Organizada, focada em infraestrutura",
                "expertise": ["Infrastructure Management", "Deployment Automation", "Monitoring Systems", "Server Administration"],
                "commands": ["@devops_engineer"],
                "workflows": ["environment-setup", "deployment-management", "monitoring-setup"],
                "templates": ["Deployment Guide", "Infrastructure Specification", "Monitoring Setup Guide"]
            },
            "game_team_orchestrator": {
                "name": "Game Team Orchestrator",
                "personality": "Estratégica, focada em coordenação",
                "expertise": ["Team Coordination", "Project Management", "Workflow Orchestration", "Quality Assurance"],
                "commands": ["@game_team_orchestrator"],
                "workflows": ["sprint-planning", "feature-review", "deployment-coordination"],
                "templates": ["Sprint Plan", "Feature Review Report", "Deployment Checklist"]
            }
        }
        
        # Dados dos workflows BMAD
        self.workflows_data = {
            "feature-development": {
                "name": "Feature Development Workflow",
                "description": "Processo completo de desenvolvimento de features",
                "phases": ["Concept & Design", "Implementation", "Integration & Testing", "Deployment"],
                "duration": "2-4 weeks",
                "agents": ["game_designer", "engine_developer", "content_creator", "level_designer", "qa_tester", "devops_engineer"],
                "templates": ["Game Design Document", "Technical Specification", "Test Plan", "Deployment Guide"]
            },
            "content-pipeline": {
                "name": "Content Pipeline Workflow",
                "description": "Criação e integração de conteúdo",
                "phases": ["Planning", "Development", "Integration", "Deployment"],
                "duration": "1-2 weeks",
                "agents": ["content_creator", "level_designer", "qa_tester"],
                "templates": ["Content Planning Document", "Content Integration Guide", "Test Plan"]
            },
            "bug-fix": {
                "name": "Bug Fix Workflow",
                "description": "Identificação e correção de bugs",
                "phases": ["Identification", "Analysis", "Fix", "Validation"],
                "duration": "1-3 days",
                "agents": ["qa_tester", "engine_developer", "content_creator"],
                "templates": ["Bug Report", "Fix Specification", "Validation Report"]
            },
            "performance-optimization": {
                "name": "Performance Optimization Workflow",
                "description": "Análise e otimização de performance",
                "phases": ["Analysis", "Identification", "Optimization", "Validation"],
                "duration": "3-7 days",
                "agents": ["engine_developer", "qa_tester", "devops_engineer"],
                "templates": ["Performance Analysis Report", "Optimization Plan", "Validation Report"]
            }
        }
        
        # Dados dos templates BMAD
        self.templates_data = {
            "Game Design Document": {
                "name": "Game Design Document (GDD)",
                "description": "Documentação de design de features",
                "format": "Markdown with Obsidian formatting",
                "sections": ["Overview", "Gameplay Mechanics", "Balance", "Progression", "Technical Requirements"],
                "agents": ["game_designer"],
                "workflows": ["feature-development"]
            },
            "Technical Specification": {
                "name": "Technical Specification",
                "description": "Especificação técnica de sistemas",
                "format": "Markdown with diagrams",
                "sections": ["Architecture", "Implementation", "Performance", "Testing", "Deployment"],
                "agents": ["engine_developer"],
                "workflows": ["feature-development", "performance-optimization"]
            },
            "Quest Design Document": {
                "name": "Quest Design Document",
                "description": "Documentação de design de quests",
                "format": "Markdown with Lua scripts",
                "sections": ["Quest Overview", "Objectives", "Rewards", "Scripts", "Testing"],
                "agents": ["content_creator"],
                "workflows": ["content-pipeline"]
            },
            "Level Design Document": {
                "name": "Level Design Document",
                "description": "Documentação de design de níveis",
                "format": "Markdown with maps",
                "sections": ["Area Overview", "Layout", "Flow", "Assets", "Performance"],
                "agents": ["level_designer"],
                "workflows": ["content-pipeline"]
            },
            "Test Plan": {
                "name": "Test Plan",
                "description": "Plano de testes para features",
                "format": "Markdown with checklists",
                "sections": ["Test Scope", "Test Cases", "Test Environment", "Test Execution", "Results"],
                "agents": ["qa_tester"],
                "workflows": ["feature-development", "content-pipeline", "bug-fix"]
            },
            "Deployment Guide": {
                "name": "Deployment Guide",
                "description": "Guia de deploy de features",
                "format": "Markdown with scripts",
                "sections": ["Prerequisites", "Deployment Steps", "Verification", "Rollback", "Monitoring"],
                "agents": ["devops_engineer"],
                "workflows": ["feature-development", "content-pipeline"]
            }
        }
    
    def load_context_data(self) -> Dict[str, Any]:
        """Carrega dados de contexto detectado"""
        context_file = Path("wiki/maps/context_data.json")
        if context_file.exists():
            with open(context_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            return {
                'context': 'otclient',
                'paths': {
                    'docs': 'wiki/otclient/',
                    'maps': 'wiki/maps/'
                }
            }
    
    def generate_agents_index(self) -> Dict[str, Any]:
        """Gera índice de agentes BMAD"""
        agents_index = {
            "metadata": {
                "version": "1.0",
                "last_updated": datetime.now().isoformat(),
                "context": self.context_data['context'],
                "total_agents": len(self.agents_data),
                "description": f"BMAD agents index for {self.context_data['context'].upper()} context"
            },
            "agents": {}
        }
        
        for agent_id, agent_data in self.agents_data.items():
            agents_index["agents"][agent_id] = {
                "name": agent_data["name"],
                "personality": agent_data["personality"],
                "expertise": agent_data["expertise"],
                "commands": agent_data["commands"],
                "workflows": agent_data["workflows"],
                "templates": agent_data["templates"],
                "context_adaptation": self.get_context_adaptation(agent_id)
            }
        
        return agents_index
    
    def generate_workflows_index(self) -> Dict[str, Any]:
        """Gera índice de workflows BMAD"""
        workflows_index = {
            "metadata": {
                "version": "1.0",
                "last_updated": datetime.now().isoformat(),
                "context": self.context_data['context'],
                "total_workflows": len(self.workflows_data),
                "description": f"BMAD workflows index for {self.context_data['context'].upper()} context"
            },
            "workflows": {}
        }
        
        for workflow_id, workflow_data in self.workflows_data.items():
            workflows_index["workflows"][workflow_id] = {
                "name": workflow_data["name"],
                "description": workflow_data["description"],
                "phases": workflow_data["phases"],
                "duration": workflow_data["duration"],
                "agents": workflow_data["agents"],
                "templates": workflow_data["templates"],
                "context_adaptation": self.get_workflow_context_adaptation(workflow_id)
            }
        
        return workflows_index
    
    def generate_templates_index(self) -> Dict[str, Any]:
        """Gera índice de templates BMAD"""
        templates_index = {
            "metadata": {
                "version": "1.0",
                "last_updated": datetime.now().isoformat(),
                "context": self.context_data['context'],
                "total_templates": len(self.templates_data),
                "description": f"BMAD templates index for {self.context_data['context'].upper()} context"
            },
            "templates": {}
        }
        
        for template_id, template_data in self.templates_data.items():
            templates_index["templates"][template_id] = {
                "name": template_data["name"],
                "description": template_data["description"],
                "format": template_data["format"],
                "sections": template_data["sections"],
                "agents": template_data["agents"],
                "workflows": template_data["workflows"],
                "context_adaptation": self.get_template_context_adaptation(template_id)
            }
        
        return templates_index
    
    def get_context_adaptation(self, agent_id: str) -> Dict[str, str]:
        """Retorna adaptação do agente para o contexto atual"""
        context = self.context_data['context']
        
        adaptations = {
            "otclient": {
                "game_designer": "Foco em features de cliente e UI",
                "engine_developer": "Otimização de rendering e performance de cliente",
                "content_creator": "Scripts de módulos e interface",
                "level_designer": "Design de interfaces e layouts",
                "qa_tester": "Testes de interface e usabilidade",
                "devops_engineer": "Deploy e distribuição de cliente",
                "game_team_orchestrator": "Coordenação de desenvolvimento de cliente"
            },
            "canary": {
                "game_designer": "Foco em mecânicas de servidor e balanceamento",
                "engine_developer": "Otimização de servidor e performance",
                "content_creator": "Scripts de servidor e conteúdo",
                "level_designer": "Design de mundo e áreas",
                "qa_tester": "Testes de servidor e balanceamento",
                "devops_engineer": "Infraestrutura e operações de servidor",
                "game_team_orchestrator": "Coordenação de desenvolvimento de servidor"
            },
            "unified": {
                "game_designer": "Design de ecossistema completo",
                "engine_developer": "Arquitetura cliente-servidor",
                "content_creator": "Conteúdo integrado",
                "level_designer": "Design de mundo unificado",
                "qa_tester": "Testes de integração",
                "devops_engineer": "Infraestrutura completa",
                "game_team_orchestrator": "Coordenação de ecossistema completo"
            }
        }
        
        return {
            "focus": adaptations.get(context, {}).get(agent_id, "Adaptação padrão"),
            "context": context
        }
    
    def get_workflow_context_adaptation(self, workflow_id: str) -> Dict[str, str]:
        """Retorna adaptação do workflow para o contexto atual"""
        context = self.context_data['context']
        
        adaptations = {
            "otclient": {
                "feature-development": "Desenvolvimento de features de cliente",
                "content-pipeline": "Criação de módulos e UI",
                "bug-fix": "Correção de bugs de cliente",
                "performance-optimization": "Otimização de performance de cliente"
            },
            "canary": {
                "feature-development": "Desenvolvimento de features de servidor",
                "content-pipeline": "Criação de conteúdo de servidor",
                "bug-fix": "Correção de bugs de servidor",
                "performance-optimization": "Otimização de performance de servidor"
            },
            "unified": {
                "feature-development": "Desenvolvimento de features integradas",
                "content-pipeline": "Criação de conteúdo unificado",
                "bug-fix": "Correção de bugs integrados",
                "performance-optimization": "Otimização de performance completa"
            }
        }
        
        return {
            "focus": adaptations.get(context, {}).get(workflow_id, "Adaptação padrão"),
            "context": context
        }
    
    def get_template_context_adaptation(self, template_id: str) -> Dict[str, str]:
        """Retorna adaptação do template para o contexto atual"""
        context = self.context_data['context']
        
        adaptations = {
            "otclient": {
                "Game Design Document": "Design de features de cliente",
                "Technical Specification": "Especificação técnica de cliente",
                "Quest Design Document": "Design de módulos e UI",
                "Level Design Document": "Design de interfaces",
                "Test Plan": "Testes de cliente",
                "Deployment Guide": "Deploy de cliente"
            },
            "canary": {
                "Game Design Document": "Design de features de servidor",
                "Technical Specification": "Especificação técnica de servidor",
                "Quest Design Document": "Design de conteúdo de servidor",
                "Level Design Document": "Design de mundo",
                "Test Plan": "Testes de servidor",
                "Deployment Guide": "Deploy de servidor"
            },
            "unified": {
                "Game Design Document": "Design de ecossistema completo",
                "Technical Specification": "Especificação técnica unificada",
                "Quest Design Document": "Design de conteúdo integrado",
                "Level Design Document": "Design de mundo unificado",
                "Test Plan": "Testes de integração",
                "Deployment Guide": "Deploy unificado"
            }
        }
        
        return {
            "focus": adaptations.get(context, {}).get(template_id, "Adaptação padrão"),
            "context": context
        }
    
    def update_all_bmad_maps(self):
        """Atualiza todos os mapas BMAD"""
        print(f"Atualizando mapas BMAD ({self.context_data['context'].upper()})...")
        
        # Gerar agentes index
        print("Gerando bmad_agents_index.json...")
        agents_index = self.generate_agents_index()
        with open(self.wiki_dir / "maps" / "bmad_agents_index.json", 'w', encoding='utf-8') as f:
            json.dump(agents_index, f, indent=2, ensure_ascii=False)
        
        # Gerar workflows index
        print("Gerando bmad_workflows_index.json...")
        workflows_index = self.generate_workflows_index()
        with open(self.wiki_dir / "maps" / "bmad_workflows_index.json", 'w', encoding='utf-8') as f:
            json.dump(workflows_index, f, indent=2, ensure_ascii=False)
        
        # Gerar templates index
        print("Gerando bmad_templates_index.json...")
        templates_index = self.generate_templates_index()
        with open(self.wiki_dir / "maps" / "bmad_templates_index.json", 'w', encoding='utf-8') as f:
            json.dump(templates_index, f, indent=2, ensure_ascii=False)
        
        print("Todos os mapas BMAD foram atualizados!")

if __name__ == "__main__":
    updater = BMADMapUpdater()
    updater.update_all_bmad_maps() 
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
- **Nome**: update_bmad_maps
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

