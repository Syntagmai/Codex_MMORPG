#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Task Master Agent - Sistema de Coordenação Geral de Tasks

Este agente é responsável por:
- Coordenar todas as tarefas do sistema integrado
- Atribuir tarefas aos agentes apropriados
- Monitorar progresso em tempo real
- Atualizar o dashboard central
- Gerenciar dependências entre tarefas
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import re

class TaskMasterAgent:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent.parent
        self.dashboard_path = self.base_path / "wiki" / "dashboard"
        self.log_path = self.base_path / "wiki" / "log"
        self.rules_path = self.base_path / ".cursor" / "rules"
        
        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('TaskMasterAgent')
        
        # Carregar configurações
        self.load_configuration()
        
    def load_configuration(self):
        """Carrega configurações do sistema"""
        self.logger.info("🔧 Carregando configurações do Task Master Agent...")
        
        # Configurações padrão
        self.config = {
            "dashboard_file": "integrated_task_manager.md",
            "log_file": "task_master_agent.log",
            "max_concurrent_tasks": 5,
            "task_timeout": 3600,  # 1 hora
            "update_interval": 300,  # 5 minutos
            "priority_levels": ["crítica", "alta", "média", "baixa"],
            "task_categories": ["epic", "story", "agent", "roadmap", "planejamento"]
        }
        
        # Debug: verificar caminhos
        self.logger.info(f"🔍 Caminho base: {self.base_path}")
        self.logger.info(f"🔍 Caminho dashboard: {self.dashboard_path}")
        self.logger.info(f"🔍 Arquivo dashboard: {self.dashboard_path / self.config['dashboard_file']}")
        
        self.logger.info("✅ Configurações carregadas com sucesso")
    
    def analyze_dashboard(self) -> Dict:
        """Analisa o dashboard central e extrai informações"""
        self.logger.info("📊 Analisando dashboard central...")
        
        dashboard_file = self.dashboard_path / self.config["dashboard_file"]
        
        if not dashboard_file.exists():
            self.logger.error(f"❌ Dashboard não encontrado: {dashboard_file}")
            return {}
        
        try:
            with open(dashboard_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extrair informações do dashboard
            analysis = {
                "epics": self.extract_epics(content),
                "stories": self.extract_stories(content),
                "agents": self.extract_agents(content),
                "roadmaps": self.extract_roadmaps(content),
                "planejamentos": self.extract_planejamentos(content),
                "progress": self.extract_progress(content),
                "tasks_in_progress": self.extract_tasks_in_progress(content),
                "tasks_pending": self.extract_tasks_pending(content)
            }
            
            self.logger.info(f"✅ Dashboard analisado: {len(analysis['epics'])} epics, {len(analysis['stories'])} stories")
            return analysis
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao analisar dashboard: {e}")
            return {}
    
    def extract_epics(self, content: str) -> List[Dict]:
        """Extrai informações das epics do dashboard"""
        epics = []
        
        # Padrão para encontrar epics
        epic_pattern = r'### \*\*🔥 Epic (\d+): (.+?)\*\*\s*\*\*Status\*\*: ([\d.]+)%'
        
        matches = re.finditer(epic_pattern, content, re.DOTALL)
        
        for match in matches:
            epic_id = match.group(1)
            title = match.group(2)
            status = float(match.group(3))
            
            # Extrair subtasks
            subtasks = self.extract_subtasks(content, epic_id)
            
            epics.append({
                "id": f"Epic {epic_id}",
                "title": title,
                "status": status,
                "subtasks": subtasks,
                "category": "epic"
            })
        
        return epics
    
    def extract_stories(self, content: str) -> List[Dict]:
        """Extrai informações das stories habdel"""
        stories = []
        
        # Padrões para diferentes categorias de stories
        story_patterns = [
            (r'### \*\*🎨 UI Stories \((\d+) stories\)\*\*', "UI"),
            (r'### \*\*🎮 Game Stories \((\d+) stories\)\*\*', "GAME"),
            (r'### \*\*🔧 Core Stories \((\d+) stories\)\*\*', "CORE"),
            (r'### \*\*📚 Guide Stories \((\d+) stories\)\*\*', "GUIDE"),
            (r'### \*\*🔍 Reference Stories \((\d+) stories\)\*\*', "REF")
        ]
        
        for pattern, category in story_patterns:
            matches = re.finditer(pattern, content)
            for match in matches:
                count = int(match.group(1))
                
                # Extrair stories completas e pendentes
                section_start = match.start()
                section_end = content.find('###', section_start + 1)
                if section_end == -1:
                    section_end = len(content)
                
                section_content = content[section_start:section_end]
                
                completed = self.extract_completed_stories(section_content, category)
                pending = self.extract_pending_stories(section_content, category)
                
                stories.extend(completed)
                stories.extend(pending)
        
        return stories
    
    def extract_agents(self, content: str) -> List[Dict]:
        """Extrai informações dos agentes BMAD"""
        agents = []
        
        # Padrões para diferentes status de agentes
        agent_patterns = [
            (r'- \[x\] \*\*(.+?)\*\* ✅ Ativo', "ativo"),
            (r'- \[ \] \*\*(.+?)\*\* 🔄 Em desenvolvimento', "desenvolvimento"),
            (r'- \[ \] \*\*(.+?)\*\* 📋 Planejado', "planejado")
        ]
        
        for pattern, status in agent_patterns:
            matches = re.finditer(pattern, content)
            for match in matches:
                agent_name = match.group(1)
                agents.append({
                    "name": agent_name,
                    "status": status,
                    "category": "agent"
                })
        
        return agents
    
    def extract_roadmaps(self, content: str) -> List[Dict]:
        """Extrai informações dos roadmaps"""
        roadmaps = []
        
        roadmap_pattern = r'- \[([x ])\] \*\*(.+?)\*\* ([✅📋])'
        matches = re.finditer(roadmap_pattern, content)
        
        for match in matches:
            completed = match.group(1) == 'x'
            title = match.group(2)
            status_icon = match.group(3)
            
            roadmaps.append({
                "title": title,
                "completed": completed,
                "status": "implementado" if completed else "pendente",
                "category": "roadmap"
            })
        
        return roadmaps
    
    def extract_planejamentos(self, content: str) -> List[Dict]:
        """Extrai informações dos planejamentos"""
        planejamentos = []
        
        planejamento_pattern = r'- \[([x ])\] \*\*(.+?)\*\* ([✅📋])'
        matches = re.finditer(planejamento_pattern, content)
        
        for match in matches:
            completed = match.group(1) == 'x'
            title = match.group(2)
            status_icon = match.group(3)
            
            planejamentos.append({
                "title": title,
                "completed": completed,
                "status": "ativo" if completed else "pendente",
                "category": "planejamento"
            })
        
        return planejamentos
    
    def extract_progress(self, content: str) -> Dict:
        """Extrai métricas de progresso"""
        progress = {}
        
        # Padrões para métricas
        progress_patterns = [
            (r'\*\*Progresso Geral\*\*: ([\d.]+)%', "geral"),
            (r'\*\*Epics\*\*: ([\d.]+)%', "epics"),
            (r'\*\*Stories Habdel\*\*: ([\d.]+)%', "stories"),
            (r'\*\*Agentes BMAD\*\*: ([\d.]+)%', "agentes"),
            (r'\*\*Tasks Concluídas\*\*: ([\d.]+)%', "tasks")
        ]
        
        for pattern, key in progress_patterns:
            match = re.search(pattern, content)
            if match:
                progress[key] = float(match.group(1))
        
        return progress
    
    def extract_tasks_in_progress(self, content: str) -> List[str]:
        """Extrai tarefas em progresso"""
        tasks = []
        
        # Padrão para tarefas em progresso
        pattern = r'🔄 (.+?)(?:\n|$)'
        matches = re.finditer(pattern, content)
        
        for match in matches:
            task = match.group(1).strip()
            if task:
                tasks.append(task)
        
        return tasks
    
    def extract_tasks_pending(self, content: str) -> List[str]:
        """Extrai tarefas pendentes"""
        tasks = []
        
        # Padrão para tarefas pendentes
        pattern = r'📋 (.+?)(?:\n|$)'
        matches = re.finditer(pattern, content)
        
        for match in matches:
            task = match.group(1).strip()
            if task:
                tasks.append(task)
        
        return tasks
    
    def extract_subtasks(self, content: str, epic_id: str) -> List[Dict]:
        """Extrai subtasks de uma epic específica"""
        subtasks = []
        
        # Padrão para subtasks
        pattern = rf'- \[([x ])\] \*\*{epic_id}\.(\d+)\*\* (.+?) \((\d+)% → (\d+)%\)'
        matches = re.finditer(pattern, content)
        
        for match in matches:
            completed = match.group(1) == 'x'
            subtask_id = match.group(2)
            title = match.group(3)
            current_progress = int(match.group(4))
            target_progress = int(match.group(5))
            
            subtasks.append({
                "id": f"{epic_id}.{subtask_id}",
                "title": title,
                "completed": completed,
                "current_progress": current_progress,
                "target_progress": target_progress
            })
        
        return subtasks
    
    def extract_completed_stories(self, content: str, category: str) -> List[Dict]:
        """Extrai stories completas"""
        stories = []
        
        pattern = r'- \[x\] \*\*(.+?)\*\* (.+?) ✅'
        matches = re.finditer(pattern, content)
        
        for match in matches:
            story_id = match.group(1)
            title = match.group(2)
            
            stories.append({
                "id": story_id,
                "title": title,
                "category": category,
                "completed": True,
                "status": "completa"
            })
        
        return stories
    
    def extract_pending_stories(self, content: str, category: str) -> List[Dict]:
        """Extrai stories pendentes"""
        stories = []
        
        pattern = r'- \[ \] \*\*(.+?)\*\* (.+?)$'
        matches = re.finditer(pattern, content, re.MULTILINE)
        
        for match in matches:
            story_id = match.group(1)
            title = match.group(2)
            
            stories.append({
                "id": story_id,
                "title": title,
                "category": category,
                "completed": False,
                "status": "pendente"
            })
        
        return stories
    
    def assign_task(self, task_info: Dict) -> Dict:
        """Atribui uma tarefa ao agente apropriado"""
        self.logger.info(f"📋 Atribuindo tarefa: {task_info.get('title', 'N/A')}")
        
        # Determinar agente apropriado baseado na categoria
        category = task_info.get('category', '')
        priority = task_info.get('priority', 'média')
        
        agent_mapping = {
            'epic': 'Task Master Agent',
            'story': 'Documentation Agent',
            'agent': 'Development Agent',
            'roadmap': 'Planning Agent',
            'planejamento': 'Strategy Agent'
        }
        
        assigned_agent = agent_mapping.get(category, 'Task Master Agent')
        
        assignment = {
            "task_id": task_info.get('id', ''),
            "task_title": task_info.get('title', ''),
            "assigned_agent": assigned_agent,
            "priority": priority,
            "assigned_at": datetime.now().isoformat(),
            "estimated_duration": self.estimate_duration(task_info),
            "dependencies": task_info.get('dependencies', []),
            "status": "assigned"
        }
        
        self.logger.info(f"✅ Tarefa atribuída a: {assigned_agent}")
        return assignment
    
    def estimate_duration(self, task_info: Dict) -> int:
        """Estima a duração de uma tarefa em minutos"""
        category = task_info.get('category', '')
        priority = task_info.get('priority', 'média')
        
        # Estimativas base por categoria (em minutos)
        base_estimates = {
            'epic': 480,  # 8 horas
            'story': 120,  # 2 horas
            'agent': 240,  # 4 horas
            'roadmap': 180,  # 3 horas
            'planejamento': 120   # 2 horas
        }
        
        base_duration = base_estimates.get(category, 120)
        
        # Ajustar por prioridade
        priority_multipliers = {
            'crítica': 0.8,  # Mais rápido
            'alta': 1.0,     # Normal
            'média': 1.2,    # Um pouco mais lento
            'baixa': 1.5     # Mais lento
        }
        
        multiplier = priority_multipliers.get(priority, 1.0)
        
        return int(base_duration * multiplier)
    
    def update_dashboard(self, task_updates: List[Dict]) -> bool:
        """Atualiza o dashboard central com mudanças de tarefas"""
        self.logger.info("📊 Atualizando dashboard central...")
        
        try:
            dashboard_file = self.dashboard_path / self.config["dashboard_file"]
            
            if not dashboard_file.exists():
                self.logger.error("❌ Dashboard não encontrado")
                return False
            
            # Ler conteúdo atual
            with open(dashboard_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Aplicar atualizações
            updated_content = content
            for update in task_updates:
                updated_content = self.apply_task_update(updated_content, update)
            
            # Salvar conteúdo atualizado
            with open(dashboard_file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            self.logger.info("✅ Dashboard atualizado com sucesso")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao atualizar dashboard: {e}")
            return False
    
    def apply_task_update(self, content: str, update: Dict) -> str:
        """Aplica uma atualização específica ao conteúdo do dashboard"""
        task_id = update.get('task_id', '')
        new_status = update.get('status', '')
        progress = update.get('progress', 0)
        
        # Padrões para diferentes tipos de atualização
        if task_id.startswith('Epic'):
            # Atualizar epic
            pattern = rf'(\*\*Epic {task_id[5:]}: .+?\*\*)\s*\*\*Status\*\*: ([\d.]+)%'
            replacement = rf'\1\n**Status**: {progress}%'
            content = re.sub(pattern, replacement, content)
            
        elif task_id.startswith(('UI-', 'GAME-', 'CORE-', 'GUIDE-', 'REF-')):
            # Atualizar story
            if new_status == 'completed':
                pattern = rf'- \[ \] \*\*({task_id})\*\* (.+?)$'
                replacement = rf'- [x] **\1** \2 ✅'
                content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
        
        return content
    
    def generate_progress_report(self) -> Dict:
        """Gera relatório de progresso do sistema"""
        self.logger.info("📈 Gerando relatório de progresso...")
        
        # Analisar dashboard
        analysis = self.analyze_dashboard()
        
        # Calcular métricas
        total_tasks = len(analysis.get('epics', [])) + len(analysis.get('stories', []))
        completed_tasks = sum(1 for epic in analysis.get('epics', []) if epic.get('status', 0) == 100)
        completed_tasks += sum(1 for story in analysis.get('stories', []) if story.get('completed', False))
        
        progress_percentage = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "progress_percentage": progress_percentage,
            "epics": analysis.get('epics', []),
            "stories": analysis.get('stories', []),
            "agents": analysis.get('agents', []),
            "roadmaps": analysis.get('roadmaps', []),
            "planejamentos": analysis.get('planejamentos', []),
            "tasks_in_progress": analysis.get('tasks_in_progress', []),
            "tasks_pending": analysis.get('tasks_pending', []),
            "next_priorities": self.identify_next_priorities(analysis)
        }
        
        self.logger.info(f"✅ Relatório gerado: {progress_percentage:.1f}% de progresso")
        return report
    
    def identify_next_priorities(self, analysis: Dict) -> List[str]:
        """Identifica próximas prioridades baseado na análise"""
        priorities = []
        
        # Verificar epics com menor progresso
        epics = analysis.get('epics', [])
        if epics:
            lowest_progress_epic = min(epics, key=lambda x: x.get('status', 0))
            if lowest_progress_epic.get('status', 0) < 100:
                priorities.append(f"Completar {lowest_progress_epic['id']}: {lowest_progress_epic['title']}")
        
        # Verificar stories pendentes por categoria
        stories = analysis.get('stories', [])
        pending_stories = [s for s in stories if not s.get('completed', False)]
        
        if pending_stories:
            # Agrupar por categoria
            categories = {}
            for story in pending_stories:
                category = story.get('category', '')
                if category not in categories:
                    categories[category] = []
                categories[category].append(story)
            
            # Adicionar prioridades por categoria
            for category, category_stories in categories.items():
                if len(category_stories) > 0:
                    priorities.append(f"Completar {len(category_stories)} stories {category}")
        
        return priorities[:5]  # Limitar a 5 prioridades
    
    def run(self):
        """Executa o Task Master Agent"""
        self.logger.info("🚀 Iniciando Task Master Agent...")
        
        try:
            # Analisar dashboard
            analysis = self.analyze_dashboard()
            
            if not analysis:
                self.logger.error("❌ Falha ao analisar dashboard")
                return False
            
            # Gerar relatório de progresso
            report = self.generate_progress_report()
            
            # Salvar relatório
            report_file = self.log_path / f"task_master_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(report_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            
            self.logger.info(f"✅ Relatório salvo: {report_file}")
            
            # Log de resumo
            self.logger.info(f"📊 Resumo do Sistema:")
            self.logger.info(f"   - Progresso Geral: {report['progress_percentage']:.1f}%")
            self.logger.info(f"   - Total de Tarefas: {report['total_tasks']}")
            self.logger.info(f"   - Tarefas Concluídas: {report['completed_tasks']}")
            self.logger.info(f"   - Tarefas em Progresso: {len(report['tasks_in_progress'])}")
            self.logger.info(f"   - Tarefas Pendentes: {len(report['tasks_pending'])}")
            
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro na execução do Task Master Agent: {e}")
            return False

if __name__ == "__main__":
    agent = TaskMasterAgent()
    success = agent.run()
    
    if success:
        print("✅ Task Master Agent executado com sucesso!")
    else:
        print("❌ Task Master Agent falhou na execução!") 