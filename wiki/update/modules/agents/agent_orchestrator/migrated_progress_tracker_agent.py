# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
MAX_ITEMS = 100
MAX_SIZE = 1000
TIMEOUT_SECONDS = 60

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: progress_tracker_agent.py
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
Progress Tracker Agent - Sistema de Monitoramento em Tempo Real

Este agente é responsável por:
- Monitorar progresso em tempo real de todas as tarefas
- Gerar métricas e relatórios automáticos
- Alertar sobre mudanças de status
- Atualizar métricas de progresso
- Gerar dashboards de performance
"""

import json
import logging
import re

class ProgressTrackerAgent:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent.parent
        self.dashboard_path = self.base_path / "wiki" / "dashboard"
        self.log_path = self.base_path / "wiki" / "log"
        self.metrics_path = self.base_path / "wiki" / "log" / "metrics"
        
        # Criar pasta de métricas se não existir
        self.metrics_path.mkdir(exist_ok=True)
        
        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('ProgressTrackerAgent')
        
        # Carregar configurações
        self.load_configuration()
        
        # Histórico de métricas
        self.metrics_history = []
        
    def load_configuration(self):
        """Carrega configurações do sistema"""
        self.logger.info("🔧 Carregando configurações do Progress Tracker Agent...")
        
        # Configurações padrão
        self.config = {
            "dashboard_file": "integrated_task_manager.md",
            "metrics_file": "progress_metrics.json",
            "history_file": "metrics_history.json",
            "update_interval": 300,  # 5 minutos
            "alert_threshold": 0.1,  # 10% de mudança
            "max_history_size": 1000,
            "kpi_targets": {
                "progresso_geral": 100.0,
                "epics": 100.0,
                "stories": 100.0,
                "agentes": 100.0,
                "tasks": 100.0
            }
        }
        
        self.logger.info("✅ Configurações carregadas com sucesso")
    
    def calculate_current_metrics(self) -> Dict:
        """Calcula métricas atuais do sistema"""
        self.logger.info("📊 Calculando métricas atuais...")
        
        dashboard_file = self.dashboard_path / self.config["dashboard_file"]
        
        if not dashboard_file.exists():
            self.logger.error(f"❌ Dashboard não encontrado: {dashboard_file}")
            return {}
        
        try:
            with open(dashboard_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Calcular métricas
            metrics = {
                "timestamp": datetime.now().isoformat(),
                "progresso_geral": self.calculate_general_progress(content),
                "epics": self.calculate_epics_progress(content),
                "stories": self.calculate_stories_progress(content),
                "agentes": self.calculate_agents_progress(content),
                "tasks": self.calculate_tasks_progress(content),
                "roadmaps": self.calculate_roadmaps_progress(content),
                "planejamentos": self.calculate_planejamentos_progress(content),
                "velocity": self.calculate_velocity(),
                "trends": self.calculate_trends(),
                "alerts": self.generate_alerts(content)
            }
            
            self.logger.info(f"✅ Métricas calculadas: {metrics['progresso_geral']:.1f}% geral")
            return metrics
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao calcular métricas: {e}")
            return {}
    
    def calculate_general_progress(self, content: str) -> float:
        """Calcula progresso geral do sistema"""
        # Extrair métricas individuais
        epics_progress = self.calculate_epics_progress(content)
        stories_progress = self.calculate_stories_progress(content)
        agentes_progress = self.calculate_agents_progress(content)
        tasks_progress = self.calculate_tasks_progress(content)
        
        # Peso das categorias
        weights = {
            "epics": 0.3,
            "stories": 0.4,
            "agentes": 0.2,
            "tasks": 0.1
        }
        
        # Calcular progresso ponderado
        general_progress = (
            epics_progress * weights["epics"] +
            stories_progress * weights["stories"] +
            agentes_progress * weights["agentes"] +
            tasks_progress * weights["tasks"]
        )
        
        return round(general_progress, 1)
    
    def calculate_epics_progress(self, content: str) -> float:
        """Calcula progresso das epics"""
        # Padrão para encontrar status das epics
        pattern = r'\*\*Status\*\*: ([\d.]+)%'
        matches = re.findall(pattern, content)
        
        if not matches:
            return 0.0
        
        # Calcular média dos status
        total_progress = sum(float(match) for match in matches)
        average_progress = total_progress / len(matches)
        
        return round(average_progress, 1)
    
    def calculate_stories_progress(self, content: str) -> float:
        """Calcula progresso das stories"""
        # Contar stories completas e totais
        completed_pattern = r'- \[x\] \*\*(.+?)\*\* (.+?) ✅'
        total_pattern = r'- \[([x ])\] \*\*(.+?)\*\*'
        
        completed_matches = re.findall(completed_pattern, content)
        total_matches = re.findall(total_pattern, content)
        
        if not total_matches:
            return 0.0
        
        completed_count = len(completed_matches)
        total_count = len(total_matches)
        
        progress = (completed_count / total_count * 100) if total_count > 0 else 0
        return round(progress, 1)
    
    def calculate_agents_progress(self, content: str) -> float:
        """Calcula progresso dos agentes"""
        # Contar agentes ativos e totais
        active_pattern = r'- \[x\] \*\*(.+?)\*\* ✅ Ativo'
        total_pattern = r'- \[([x ])\] \*\*(.+?)\*\*'
        
        active_matches = re.findall(active_pattern, content)
        total_matches = re.findall(total_pattern, content)
        
        if not total_matches:
            return 0.0
        
        active_count = len(active_matches)
        total_count = len(total_matches)
        
        progress = (active_count / total_count * 100) if total_count > 0 else 0
        return round(progress, 1)
    
    def calculate_tasks_progress(self, content: str) -> float:
        """Calcula progresso das tasks"""
        # Contar tasks concluídas e totais
        completed_pattern = r'✅ (.+?)(?:\n|$)'
        pending_pattern = r'📋 (.+?)(?:\n|$)'
        
        completed_matches = re.findall(completed_pattern, content)
        pending_matches = re.findall(pending_pattern, content)
        
        completed_count = len(completed_matches)
        total_count = completed_count + len(pending_matches)
        
        progress = (completed_count / total_count * 100) if total_count > 0 else 0
        return round(progress, 1)
    
    def calculate_roadmaps_progress(self, content: str) -> float:
        """Calcula progresso dos roadmaps"""
        # Contar roadmaps implementados e totais
        implemented_pattern = r'- \[x\] \*\*(.+?)\*\* ✅'
        total_pattern = r'- \[([x ])\] \*\*(.+?)\*\*'
        
        implemented_matches = re.findall(implemented_pattern, content)
        total_matches = re.findall(total_pattern, content)
        
        if not total_matches:
            return 0.0
        
        implemented_count = len(implemented_matches)
        total_count = len(total_matches)
        
        progress = (implemented_count / total_count * 100) if total_count > 0 else 0
        return round(progress, 1)
    
    def calculate_planejamentos_progress(self, content: str) -> float:
        """Calcula progresso dos planejamentos"""
        # Contar planejamentos ativos e totais
        active_pattern = r'- \[x\] \*\*(.+?)\*\* ✅'
        total_pattern = r'- \[([x ])\] \*\*(.+?)\*\*'
        
        active_matches = re.findall(active_pattern, content)
        total_matches = re.findall(total_pattern, content)
        
        if not total_matches:
            return 0.0
        
        active_count = len(active_matches)
        total_count = len(total_matches)
        
        progress = (active_count / total_count * 100) if total_count > 0 else 0
        return round(progress, 1)
    
    def calculate_velocity(self) -> Dict:
        """Calcula velocidade de progresso"""
        if len(self.metrics_history) < 2:
            return {"current": 0.0, "average": 0.0, "trend": "stable"}
        
        # Calcular velocidade atual (últimas 2 medições)
        current_metrics = self.metrics_history[-1]
        previous_metrics = self.metrics_history[-2]
        
        current_time = datetime.fromisoformat(current_metrics["timestamp"])
        previous_time = datetime.fromisoformat(previous_metrics["timestamp"])
        
        time_diff = (current_time - previous_time).total_seconds() / 3600  # horas
        progress_diff = current_metrics["progresso_geral"] - previous_metrics["progresso_geral"]
        
        current_velocity = progress_diff / time_diff if time_diff > 0 else 0
        
        # Calcular velocidade média (últimas 10 medições)
        if len(self.metrics_history) >= 10:
            recent_metrics = self.metrics_history[-10:]
            total_progress_diff = recent_metrics[-1]["progresso_geral"] - recent_metrics[0]["progresso_geral"]
            total_time_diff = (datetime.fromisoformat(recent_metrics[-1]["timestamp"]) - 
                             datetime.fromisoformat(recent_metrics[0]["timestamp"])).total_seconds() / 3600
            
            average_velocity = total_progress_diff / total_time_diff if total_time_diff > 0 else 0
        else:
            average_velocity = current_velocity
        
        # Determinar tendência
        if current_velocity > average_velocity * 1.1:
            trend = "accelerating"
        elif current_velocity < average_velocity * 0.9:
            trend = "decelerating"
        else:
            trend = "stable"
        
        return {
            "current": round(current_velocity, 2),
            "average": round(average_velocity, 2),
            "trend": trend
        }
    
    def calculate_trends(self) -> Dict:
        """Calcula tendências de progresso"""
        if len(self.metrics_history) < 5:
            return {"direction": "stable", "strength": "weak", "prediction": "insufficient_data"}
        
        # Analisar tendência dos últimos 5 pontos
        recent_metrics = self.metrics_history[-5:]
        progress_values = [m["progresso_geral"] for m in recent_metrics]
        
        # Calcular direção da tendência
        if len(progress_values) >= 2:
            first_half = progress_values[:len(progress_values)//2]
            second_half = progress_values[len(progress_values)//2:]
            
            first_avg = sum(first_half) / len(first_half)
            second_avg = sum(second_half) / len(second_half)
            
            if second_avg > first_avg * 1.05:
                direction = "up"
            elif second_avg < first_avg * 0.95:
                direction = "down"
            else:
                direction = "stable"
        else:
            direction = "stable"
        
        # Calcular força da tendência
        if len(progress_values) >= 3:
            variance = sum((x - sum(progress_values)/len(progress_values))**2 for x in progress_values) / len(progress_values)
            if variance < 1:
                strength = "strong"
            elif variance < 5:
                strength = "moderate"
            else:
                strength = "weak"
        else:
            strength = "weak"
        
        # Fazer predição simples
        if len(progress_values) >= 3 and direction != "stable":
            last_value = progress_values[-1]
            if direction == "up":
                prediction = min(100, last_value + 5)
            else:
                prediction = max(0, last_value - 5)
        else:
            prediction = "insufficient_data"
        
        return {
            "direction": direction,
            "strength": strength,
            "prediction": prediction
        }
    
    def generate_alerts(self, content: str) -> List[Dict]:
        """Gera alertas baseados no conteúdo atual"""
        alerts = []
        
        # Verificar se há tarefas bloqueadas
        blocked_pattern = r'⚪ \*\*Blocked\*\*'
        blocked_matches = re.findall(blocked_pattern, content)
        if blocked_matches:
            alerts.append({
                "type": "warning",
                "message": f"Encontradas {len(blocked_matches)} tarefas bloqueadas",
                "priority": "medium"
            })
        
        # Verificar se há tarefas críticas atrasadas
        critical_pattern = r'🔥 \*\*Crítica\*\*'
        critical_matches = re.findall(critical_pattern, content)
        if critical_matches:
            alerts.append({
                "type": "critical",
                "message": f"Encontradas {len(critical_matches)} tarefas críticas",
                "priority": "high"
            })
        
        # Verificar se há progresso estagnado
        if len(self.metrics_history) >= 3:
            recent_progress = [m["progresso_geral"] for m in self.metrics_history[-3:]]
            if len(set(recent_progress)) == 1:  # Mesmo valor por 3 medições
                alerts.append({
                    "type": "info",
                    "message": "Progresso estagnado nas últimas 3 medições",
                    "priority": "low"
                })
        
        return alerts
    
    def save_metrics(self, metrics: Dict) -> bool:
        """Salva métricas atuais"""
        try:
            # Salvar métricas atuais
            metrics_file = self.metrics_path / self.config["metrics_file"]
            with open(metrics_file, 'w', encoding='utf-8') as f:
                json.dump(metrics, f, indent=2, ensure_ascii=False)
            
            # Adicionar ao histórico
            self.metrics_history.append(metrics)
            
            # Manter tamanho do histórico
            if len(self.metrics_history) > self.config["max_history_size"]:
                self.metrics_history = self.metrics_history[-self.config["max_history_size"]:]
            
            # Salvar histórico
            history_file = self.metrics_path / self.config["history_file"]
            with open(history_file, 'w', encoding='utf-8') as f:
                json.dump(self.metrics_history, f, indent=2, ensure_ascii=False)
            
            self.logger.info("✅ Métricas salvas com sucesso")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao salvar métricas: {e}")
            return False
    
    def generate_dashboard_report(self) -> str:
        """Gera relatório de dashboard"""
        self.logger.info("📊 Gerando relatório de dashboard...")
        
        current_metrics = self.calculate_current_metrics()
        
        if not current_metrics:
            return "❌ Erro ao calcular métricas"
        
        report = f"""# 📊 Relatório de Progresso - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 🎯 Métricas Principais

| Métrica | Valor Atual | Meta | Status |
|---------|-------------|------|--------|
| **Progresso Geral** | {current_metrics['progresso_geral']}% | 100% | {'🟢' if current_metrics['progresso_geral'] >= 80
    else '🟡' if current_metrics['progresso_geral'] >= 50 else '🔴'} |
| **Epics** | {current_metrics['epics']}% | 100% | {'🟢' if current_metrics['epics'] >= 80 else '🟡' if
    current_metrics['epics'] >= 50 else '🔴'} |
| **Stories** | {current_metrics['stories']}% | 100% | {'🟢' if current_metrics['stories'] >= 80 else '🟡' if
    current_metrics['stories'] >= 50 else '🔴'} |
| **Agentes** | {current_metrics['agentes']}% | 100% | {'🟢' if current_metrics['agentes'] >= 80 else '🟡' if
    current_metrics['agentes'] >= 50 else '🔴'} |
| **Tasks** | {current_metrics['tasks']}% | 100% | {'🟢' if current_metrics['tasks'] >= 80 else '🟡' if
    current_metrics['tasks'] >= 50 else '🔴'} |

## 📈 Velocidade e Tendências

### 🚀 Velocidade
- **Atual**: {current_metrics['velocity']['current']}%/hora
- **Média**: {current_metrics['velocity']['average']}%/hora
- **Tendência**: {current_metrics['velocity']['trend']}

### 📊 Tendências
- **Direção**: {current_metrics['trends']['direction']}
- **Força**: {current_metrics['trends']['strength']}
- **Predição**: {current_metrics['trends']['prediction']}

## 🚨 Alertas

"""
        
        if current_metrics['alerts']:
            for alert in current_metrics['alerts']:
                report += f"- **{alert['type'].upper()}**: {alert['message']}\n"
        else:
            report += "- ✅ Nenhum alerta ativo\n"
        
        report += f"""
## 📋 Próximas Ações

Baseado nas métricas atuais, recomenda-se:

1. **Focar em epics** com menor progresso
2. **Acelerar stories** pendentes
3. **Ativar agentes** em desenvolvimento
4. **Completar tasks** críticas

---
**Relatório gerado**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Responsável**: Progress Tracker Agent
"""
        
        return report
    
    def run(self):
        """Executa o Progress Tracker Agent"""
        self.logger.info("🚀 Iniciando Progress Tracker Agent...")
        
        try:
            # Calcular métricas atuais
            current_metrics = self.calculate_current_metrics()
            
            if not current_metrics:
                self.logger.error("❌ Falha ao calcular métricas")
                return False
            
            # Salvar métricas
            if not self.save_metrics(current_metrics):
                self.logger.error("❌ Falha ao salvar métricas")
                return False
            
            # Gerar relatório
            report = self.generate_dashboard_report()
            
            # Salvar relatório
            report_file = self.log_path / f"progress_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write(report)
            
            self.logger.info(f"✅ Relatório salvo: {report_file}")
            
            # Log de resumo
            self.logger.info(f"📊 Resumo do Progresso:")
            self.logger.info(f"   - Progresso Geral: {current_metrics['progresso_geral']}%")
            self.logger.info(f"   - Epics: {current_metrics['epics']}%")
            self.logger.info(f"   - Stories: {current_metrics['stories']}%")
            self.logger.info(f"   - Agentes: {current_metrics['agentes']}%")
            self.logger.info(f"   - Tasks: {current_metrics['tasks']}%")
            self.logger.info(f"   - Alertas: {len(current_metrics['alerts'])}")
            
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro na execução do Progress Tracker Agent: {e}")
            return False

if __name__ == "__main__":
    agent = ProgressTrackerAgent()
    success = agent.run()
    
    if success:
        print("✅ Progress Tracker Agent executado com sucesso!")
    else:
        print("❌ Progress Tracker Agent falhou na execução!") 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = AgentorchestratorModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script progress_tracker_agent.py executado com sucesso via módulo agents.agent_orchestrator")
    else:
        print(f"❌ Erro na execução do script progress_tracker_agent.py via módulo agents.agent_orchestrator")
