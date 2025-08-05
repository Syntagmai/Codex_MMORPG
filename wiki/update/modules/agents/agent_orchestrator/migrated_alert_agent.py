from unicode_aliases import *
# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
MAX_ITEMS = 100
MAX_SIZE = 1000
TIMEOUT_SECONDS = 60

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: alert_agent.py
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
Alert Agent - Sistema de Alertas Automáticos

Este agente é responsável por:
- Monitorar métricas em tempo real
- Gerar alertas automáticos para problemas
- Notificar sobre mudanças críticas
- Gerenciar níveis de alerta
- Fornecer recomendações de ação
"""

import json
import logging
import time
from datetime import datetime, timedelta

class AlertAgent:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent.parent
        self.metrics_path = self.base_path / "wiki" / "log" / "metrics"
        self.alerts_path = self.base_path / "wiki" / "log" / "alerts"
        
        # Criar pasta de alertas se não existir
        self.alerts_path.mkdir(parents=True, exist_ok=True)
        
        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('AlertAgent')
        
        # Carregar configurações
        self.load_configuration()
        
        # Histórico de alertas
        self.alert_history = []
        
    def load_configuration(self):
        """Carrega configurações do sistema de alertas"""
        self.logger.info("🔧 Carregando configurações do Alert Agent...")
        
        # Configurações padrão
        self.config = {
            "metrics_file": "system_metrics.json",
            "kpis_file": "metrics_dashboard.json",
            "alerts_file": "active_alerts.json",
            "history_file": "alert_history.json",
            "check_interval": 60,  # 1 minuto
            "alert_thresholds": {
                "critical": {
                    "cpu_usage": 85.0,
                    "memory_usage": 90.0,
                    "disk_usage": 95.0,
                    "response_time": 5.0,
                    "error_rate": 5.0,
                    "task_completion": 70.0
                },
                "warning": {
                    "cpu_usage": 70.0,
                    "memory_usage": 80.0,
                    "disk_usage": 85.0,
                    "response_time": 3.0,
                    "error_rate": 2.0,
                    "task_completion": 85.0
                },
                "info": {
                    "cpu_usage": 50.0,
                    "memory_usage": 60.0,
                    "disk_usage": 70.0,
                    "response_time": 2.0,
                    "error_rate": 1.0,
                    "task_completion": 90.0
                }
            },
            "notification_channels": ["log", "file", "console"],
            "alert_cooldown": 300,  # 5 minutos
            "max_alerts_per_hour": 10
        }
        
        self.logger.info("✅ Configurações carregadas com sucesso")
    
    def load_metrics_data(self) -> Dict[str, Any]:
        """Carrega dados de métricas"""
        self.logger.info("📊 Carregando dados de métricas...")
        
        try:
            data = {
                "system_metrics": {},
                "kpis": {}
            }
            
            # Carregar métricas do sistema
            system_metrics_file = self.metrics_path / self.config["metrics_file"]
            if system_metrics_file.exists():
                with open(system_metrics_file, 'r', encoding='utf-8') as f:
                    data["system_metrics"] = json.load(f)
            
            # Carregar KPIs
            kpis_file = self.metrics_path / self.config["kpis_file"]
            if kpis_file.exists():
                with open(kpis_file, 'r', encoding='utf-8') as f:
                    data["kpis"] = json.load(f)
            
            self.logger.info("✅ Dados de métricas carregados com sucesso")
            return data
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao carregar dados de métricas: {e}")
            return {}
    
    def check_system_alerts(self, data: Dict) -> List[Dict]:
        """Verifica alertas do sistema"""
        self.logger.info("🔍 Verificando alertas do sistema...")
        
        alerts = []
        system_metrics = data.get("system_metrics", {})
        
        try:
            # Verificar CPU
            cpu_usage = system_metrics.get('cpu', {}).get('usage_percent', 0)
            if cpu_usage >= self.config["alert_thresholds"]["critical"]["cpu_usage"]:
                alerts.append({
                    "id": f"cpu_critical_{int(time.time())}",
                    "type": "critical",
                    "component": "system",
                    "metric": "cpu_usage",
                    "value": cpu_usage,
                    "threshold": self.config["alert_thresholds"]["critical"]["cpu_usage"],
                    "message": f"Uso de CPU crítico: {cpu_usage:.1f}%",
                    "recommendation": "Considere fechar aplicações desnecessárias ou reiniciar o sistema",
                    "timestamp": datetime.now().isoformat()
                })
            elif cpu_usage >= self.config["alert_thresholds"]["warning"]["cpu_usage"]:
                alerts.append({
                    "id": f"cpu_warning_{int(time.time())}",
                    "type": "warning",
                    "component": "system",
                    "metric": "cpu_usage",
                    "value": cpu_usage,
                    "threshold": self.config["alert_thresholds"]["warning"]["cpu_usage"],
                    "message": f"Uso de CPU alto: {cpu_usage:.1f}%",
                    "recommendation": "Monitore o uso de CPU e feche aplicações não essenciais",
                    "timestamp": datetime.now().isoformat()
                })
            
            # Verificar memória
            memory_usage = system_metrics.get('memory', {}).get('usage_percent', 0)
            if memory_usage >= self.config["alert_thresholds"]["critical"]["memory_usage"]:
                alerts.append({
                    "id": f"memory_critical_{int(time.time())}",
                    "type": "critical",
                    "component": "system",
                    "metric": "memory_usage",
                    "value": memory_usage,
                    "threshold": self.config["alert_thresholds"]["critical"]["memory_usage"],
                    "message": f"Uso de memória crítico: {memory_usage:.1f}%",
                    "recommendation": "Reinicie aplicações ou o sistema para liberar memória",
                    "timestamp": datetime.now().isoformat()
                })
            elif memory_usage >= self.config["alert_thresholds"]["warning"]["memory_usage"]:
                alerts.append({
                    "id": f"memory_warning_{int(time.time())}",
                    "message": f"Uso de memória alto: {memory_usage:.1f}%",
                    "recommendation": "Feche aplicações desnecessárias para liberar memória",
                    "timestamp": datetime.now().isoformat()
                })
            
            # Verificar disco
            disk_usage = system_metrics.get('disk', {}).get('usage_percent', 0)
            if disk_usage >= self.config["alert_thresholds"]["critical"]["disk_usage"]:
                alerts.append({
                    "id": f"disk_critical_{int(time.time())}",
                    "type": "critical",
                    "component": "system",
                    "metric": "disk_usage",
                    "value": disk_usage,
                    "threshold": self.config["alert_thresholds"]["critical"]["disk_usage"],
                    "message": f"Uso de disco crítico: {disk_usage:.1f}%",
                    "recommendation": "Libere espaço em disco removendo arquivos desnecessários",
                    "timestamp": datetime.now().isoformat()
                })
            elif disk_usage >= self.config["alert_thresholds"]["warning"]["disk_usage"]:
                alerts.append({
                    "id": f"disk_warning_{int(time.time())}",
                    "type": "warning",
                    "component": "system",
                    "metric": "disk_usage",
                    "value": disk_usage,
                    "threshold": self.config["alert_thresholds"]["warning"]["disk_usage"],
                    "message": f"Uso de disco alto: {disk_usage:.1f}%",
                    "recommendation": "Considere limpar arquivos temporários e logs antigos",
                    "timestamp": datetime.now().isoformat()
                })
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao verificar alertas do sistema: {e}")
        
        return alerts
    
    def check_application_alerts(self, data: Dict) -> List[Dict]:
        """Verifica alertas da aplicação"""
        self.logger.info("🔍 Verificando alertas da aplicação...")
        
        alerts = []
        kpis = data.get("kpis", {})
        app_kpis = kpis.get("application_kpis", {})
        
        try:
            # Verificar taxa de conclusão de tarefas
            task_completion = app_kpis.get("task_completion_rate", 0)
            if task_completion < self.config["alert_thresholds"]["critical"]["task_completion"]:
                alerts.append({
                    "id": f"task_completion_critical_{int(time.time())}",
                    "type": "critical",
                    "component": "application",
                    "metric": "task_completion_rate",
                    "value": task_completion,
                    "threshold": self.config["alert_thresholds"]["critical"]["task_completion"],
                    "message": f"Taxa de conclusão de tarefas crítica: {task_completion:.1f}%",
                    "recommendation": "Verifique se há tarefas travadas ou agentes inativos",
                    "timestamp": datetime.now().isoformat()
                })
            elif task_completion < self.config["alert_thresholds"]["warning"]["task_completion"]:
                alerts.append({
                    "id": f"task_completion_warning_{int(time.time())}",
                    "type": "warning",
                    "component": "application",
                    "metric": "task_completion_rate",
                    "value": task_completion,
                    "threshold": self.config["alert_thresholds"]["warning"]["task_completion"],
                    "message": f"Taxa de conclusão de tarefas baixa: {task_completion:.1f}%",
                    "recommendation": "Monitore o progresso das tarefas e verifique agentes",
                    "timestamp": datetime.now().isoformat()
                })
            
            # Verificar tempo de resposta
            response_time = app_kpis.get("response_time_seconds", 0)
            if response_time >= self.config["alert_thresholds"]["critical"]["response_time"]:
                alerts.append({
                    "id": f"response_time_critical_{int(time.time())}",
                    "type": "critical",
                    "component": "application",
                    "metric": "response_time",
                    "value": response_time,
                    "threshold": self.config["alert_thresholds"]["critical"]["response_time"],
                    "message": f"Tempo de resposta crítico: {response_time:.2f}s",
                    "recommendation": "Verifique gargalos no sistema ou reinicie agentes",
                    "timestamp": datetime.now().isoformat()
                })
            elif response_time >= self.config["alert_thresholds"]["warning"]["response_time"]:
                alerts.append({
                    "id": f"response_time_warning_{int(time.time())}",
                    "type": "warning",
                    "component": "application",
                    "metric": "response_time",
                    "value": response_time,
                    "threshold": self.config["alert_thresholds"]["warning"]["response_time"],
                    "message": f"Tempo de resposta alto: {response_time:.2f}s",
                    "recommendation": "Monitore performance e otimize operações",
                    "timestamp": datetime.now().isoformat()
                })
            
            # Verificar taxa de erro
            error_rate = app_kpis.get("error_rate_percent", 0)
            if error_rate >= self.config["alert_thresholds"]["critical"]["error_rate"]:
                alerts.append({
                    "id": f"error_rate_critical_{int(time.time())}",
                    "type": "critical",
                    "component": "application",
                    "metric": "error_rate",
                    "value": error_rate,
                    "threshold": self.config["alert_thresholds"]["critical"]["error_rate"],
                    "message": f"Taxa de erro crítica: {error_rate:.1f}%",
                    "recommendation": "Verifique logs de erro e reinicie componentes problemáticos",
                    "timestamp": datetime.now().isoformat()
                })
            elif error_rate >= self.config["alert_thresholds"]["warning"]["error_rate"]:
                alerts.append({
                    "id": f"error_rate_warning_{int(time.time())}",
                    "type": "warning",
                    "component": "application",
                    "metric": "error_rate",
                    "value": error_rate,
                    "threshold": self.config["alert_thresholds"]["warning"]["error_rate"],
                    "message": f"Taxa de erro alta: {error_rate:.1f}%",
                    "recommendation": "Monitore logs e verifique configurações",
                    "timestamp": datetime.now().isoformat()
                })
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao verificar alertas da aplicação: {e}")
        
        return alerts
    
    def check_trend_alerts(self, data: Dict) -> List[Dict]:
        """Verifica alertas baseados em tendências"""
        self.logger.info("📈 Verificando alertas de tendências...")
        
        alerts = []
        
        try:
            # Carregar histórico de alertas
            history_file = self.alerts_path / self.config["history_file"]
            if history_file.exists():
                with open(history_file, 'r', encoding='utf-8') as f:
                    history = json.load(f)
                
                # Verificar se há muitas ocorrências do mesmo alerta
                recent_alerts = [alert for alert in history if 
                               (datetime.now() - datetime.fromisoformat(alert.get('timestamp',
    '2025-01-01'))).seconds < 3600]
                
                if len(recent_alerts) >= self.config["max_alerts_per_hour"]:
                    alerts.append({
                        "id": f"alert_flood_{int(time.time())}",
                        "type": "warning",
                        "component": "system",
                        "metric": "alert_frequency",
                        "value": len(recent_alerts),
                        "threshold": self.config["max_alerts_per_hour"],
                        "message": f"Muitos alertas gerados: {len(recent_alerts)} na última hora",
                        "recommendation": "Verifique se há problemas sistêmicos ou ajuste thresholds",
                        "timestamp": datetime.now().isoformat()
                    })
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao verificar alertas de tendências: {e}")
        
        return alerts
    
    def generate_alert_summary(self, alerts: List[Dict]) -> str:
        """Gera resumo dos alertas"""
        if not alerts:
            return "✅ Nenhum alerta ativo - Sistema funcionando normalmente"
        
        summary = f"🚨 **Resumo de Alertas** - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        # Agrupar por tipo
        critical_alerts = [a for a in alerts if a['type'] == 'critical']
        warning_alerts = [a for a in alerts if a['type'] == 'warning']
        info_alerts = [a for a in alerts if a['type'] == 'info']
        
        if critical_alerts:
            summary += f"🔴 **Críticos ({len(critical_alerts)})**:\n"
            for alert in critical_alerts:
                summary += f"- {alert['message']}\n"
            summary += "\n"
        
        if warning_alerts:
            summary += f"🟡 **Avisos ({len(warning_alerts)})**:\n"
            for alert in warning_alerts:
                summary += f"- {alert['message']}\n"
            summary += "\n"
        
        if info_alerts:
            summary += f"🔵 **Informações ({len(info_alerts)})**:\n"
            for alert in info_alerts:
                summary += f"- {alert['message']}\n"
            summary += "\n"
        
        summary += f"📊 **Total**: {len(alerts)} alertas ativos"
        
        return summary
    
    def save_alerts(self, alerts: List[Dict]) -> bool:
        """Salva alertas em arquivo"""
        try:
            # Salvar alertas ativos
            active_alerts_file = self.alerts_path / self.config["alerts_file"]
            with open(active_alerts_file, 'w', encoding='utf-8') as f:
                json.dump(alerts, f, indent=2, ensure_ascii=False)
            
            # Adicionar ao histórico
            history_file = self.alerts_path / self.config["history_file"]
            history = []
            
            if history_file.exists():
                with open(history_file, 'r', encoding='utf-8') as f:
                    history = json.load(f)
            
            # Adicionar novos alertas
            history.extend(alerts)
            
            # Manter apenas últimos 1000 alertas
            if len(history) > 1000:
                history = history[-1000:]
            
            with open(history_file, 'w', encoding='utf-8') as f:
                json.dump(history, f, indent=2, ensure_ascii=False)
            
            self.logger.info(f"✅ Alertas salvos: {len(alerts)} ativos")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao salvar alertas: {e}")
            return False
    
    def generate_alert_report(self, alerts: List[Dict]) -> str:
        """Gera relatório detalhado de alertas"""
        self.logger.info("📋 Gerando relatório de alertas...")
        
        try:
            report = f"""
# 🚨 Relatório de Alertas - Codex MMORPG

**Data/Hora**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 📊 Resumo Executivo

- **Total de Alertas**: {len(alerts)}
- **Críticos**: {len([a for a in alerts if a['type'] == 'critical'])}
- **Avisos**: {len([a for a in alerts if a['type'] == 'warning'])}
- **Informações**: {len([a for a in alerts if a['type'] == 'info'])}

## 🔍 Alertas Detalhados

"""
            
            if alerts:
                for i, alert in enumerate(alerts, 1):
                    emoji = "🔴" if alert['type'] == 'critical' else "🟡" if alert['type'] == 'warning' else "🔵"
                    report += f"""
### {emoji} Alerta {i}: {alert['type'].upper()}

- **Componente**: {alert.get('component', 'N/A')}
- **Métrica**: {alert.get('metric', 'N/A')}
- **Valor**: {alert.get('value', 'N/A')}
- **Threshold**: {alert.get('threshold', 'N/A')}
- **Mensagem**: {alert['message']}
- **Recomendação**: {alert.get('recommendation', 'N/A')}
- **Timestamp**: {alert['timestamp']}

---
"""
            else:
                report += """
### ✅ Status do Sistema

Nenhum alerta ativo - Sistema funcionando normalmente.

---
"""
            
            report += f"""
## 📈 Estatísticas

- **Última Verificação**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Próxima Verificação**: {(datetime.now() + timedelta(seconds=self.config['check_interval'])).strftime('%Y-%m-%d %H:%M:%S')}
- **Intervalo de Verificação**: {self.config['check_interval']} segundos
- **Limite de Alertas por Hora**: {self.config['max_alerts_per_hour']}

## 🔧 Configurações de Threshold

### Críticos
- CPU: ≥{self.config['alert_thresholds']['critical']['cpu_usage']}%
- Memória: ≥{self.config['alert_thresholds']['critical']['memory_usage']}%
- Disco: ≥{self.config['alert_thresholds']['critical']['disk_usage']}%
- Tempo de Resposta: ≥{self.config['alert_thresholds']['critical']['response_time']}s
- Taxa de Erro: ≥{self.config['alert_thresholds']['critical']['error_rate']}%
- Conclusão de Tarefas: <{self.config['alert_thresholds']['critical']['task_completion']}%

### Avisos
- CPU: ≥{self.config['alert_thresholds']['warning']['cpu_usage']}%
- Memória: ≥{self.config['alert_thresholds']['warning']['memory_usage']}%
- Disco: ≥{self.config['alert_thresholds']['warning']['disk_usage']}%
- Tempo de Resposta: ≥{self.config['alert_thresholds']['warning']['response_time']}s
- Taxa de Erro: ≥{self.config['alert_thresholds']['warning']['error_rate']}%
- Conclusão de Tarefas: <{self.config['alert_thresholds']['warning']['task_completion']}%

---

*Relatório gerado automaticamente pelo Alert Agent*
"""
            
            self.logger.info("✅ Relatório de alertas gerado com sucesso")
            return report
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao gerar relatório: {e}")
            return f"# Erro ao gerar relatório: {e}"
    
    def run(self):
        """Executa o agente de alertas"""
        self.logger.info("🚀 Iniciando Alert Agent...")
        
        try:
            # Carregar dados
            data = self.load_metrics_data()
            
            if not data:
                self.logger.error("❌ Nenhum dado de métricas encontrado")
                return False
            
            # Verificar alertas
            system_alerts = self.check_system_alerts(data)
            app_alerts = self.check_application_alerts(data)
            trend_alerts = self.check_trend_alerts(data)
            
            # Combinar todos os alertas
            all_alerts = system_alerts + app_alerts + trend_alerts
            
            # Salvar alertas
            success = self.save_alerts(all_alerts)
            
            if success:
                # Gerar resumo
                summary = self.generate_alert_summary(all_alerts)
                self.logger.info(f"📊 {summary}")
                
                # Gerar relatório
                report = self.generate_alert_report(all_alerts)
                
                # Salvar relatório
                report_file = self.alerts_path / "alert_report.md"
                with open(report_file, 'w', encoding='utf-8') as f:
                    f.write(report)
                
                self.logger.info("✅ Alert Agent executado com sucesso")
                return True
            else:
                self.logger.error("❌ Erro ao salvar alertas")
                return False
                
        except Exception as e:
            self.logger.error(f"❌ Erro na execução do Alert Agent: {e}")
            return False

def main():
    """Função principal"""
    agent = AlertAgent()
    success = agent.run()
    
    if success:
        print("✅ Alert Agent executado com sucesso")
        return 0
    else:
        print("❌ Erro na execução do Alert Agent")
        return 1

if __name__ == "__main__":
    exit(main()) 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = AgentorchestratorModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script alert_agent.py executado com sucesso via módulo agents.agent_orchestrator")
    else:
        print(f"❌ Erro na execução do script alert_agent.py via módulo agents.agent_orchestrator")

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
- **Nome**: migrated_alert_agent
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

