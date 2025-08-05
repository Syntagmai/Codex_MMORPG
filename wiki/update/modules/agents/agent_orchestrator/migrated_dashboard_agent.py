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
Script Migrado: dashboard_agent.py
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
Dashboard Agent - Interface de Visualização de Métricas

Este agente é responsável por:
- Criar interface visual para métricas do sistema
- Gerar dashboards interativos
- Visualizar tendências e padrões
- Fornecer insights visuais
- Criar relatórios gráficos
"""

import json
import logging

class DashboardAgent:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent.parent
        self.metrics_path = self.base_path / "wiki" / "log" / "metrics"
        self.dashboard_path = self.base_path / "wiki" / "dashboard"
        self.output_path = self.base_path / "wiki" / "dashboard" / "metrics_dashboard"
        
        # Criar pasta de dashboard se não existir
        self.output_path.mkdir(parents=True, exist_ok=True)
        
        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('DashboardAgent')
        
        # Carregar configurações
        self.load_configuration()
        
    def load_configuration(self):
        """Carrega configurações do sistema de dashboard"""
        self.logger.info("🔧 Carregando configurações do Dashboard Agent...")
        
        # Configurações padrão
        self.config = {
            "metrics_file": "system_metrics.json",
            "kpis_file": "metrics_dashboard.json",
            "history_file": "metrics_history.json",
            "dashboard_html": "metrics_dashboard.html",
            "dashboard_md": "metrics_dashboard.md",
            "update_interval": 300,  # 5 minutos
            "chart_types": ["line", "bar", "pie", "gauge"],
            "refresh_rate": 60,  # 1 minuto
            "max_data_points": 100,
            "color_scheme": {
                "success": "#28a745",
                "warning": "#ffc107",
                "danger": "#dc3545",
                "info": "#17a2b8",
                "primary": "#007bff"
            }
        }
        
        self.logger.info("✅ Configurações carregadas com sucesso")
    
    def load_metrics_data(self) -> Dict[str, Any]:
        """Carrega dados de métricas"""
        self.logger.info("📊 Carregando dados de métricas...")
        
        try:
            data = {
                "system_metrics": {},
                "kpis": {},
                "history": []
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
            
            # Carregar histórico
            history_file = self.metrics_path / self.config["history_file"]
            if history_file.exists():
                with open(history_file, 'r', encoding='utf-8') as f:
                    data["history"] = json.load(f)
            
            self.logger.info("✅ Dados de métricas carregados com sucesso")
            return data
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao carregar dados de métricas: {e}")
            return {}
    
    def generate_html_dashboard(self, data: Dict) -> str:
        """Gera dashboard HTML interativo"""
        self.logger.info("🌐 Gerando dashboard HTML...")
        
        try:
            system_metrics = data.get("system_metrics", {})
            kpis = data.get("kpis", {})
            
            # Extrair valores
            cpu_usage = system_metrics.get('cpu', {}).get('usage_percent', 0)
            memory_usage = system_metrics.get('memory', {}).get('usage_percent', 0)
            disk_usage = system_metrics.get('disk', {}).get('usage_percent', 0)
            overall_score = kpis.get('overall_score', 0)
            
            # Determinar status
            def get_status_color(value, thresholds):
                if value >= thresholds['success']:
                    return self.config['color_scheme']['success']
                elif value >= thresholds['warning']:
                    return self.config['color_scheme']['warning']
                else:
                    return self.config['color_scheme']['danger']
            
            cpu_color = get_status_color(cpu_usage, {'success': 30, 'warning': 60})
            memory_color = get_status_color(memory_usage, {'success': 50, 'warning': 75})
            disk_color = get_status_color(disk_usage, {'success': 60, 'warning': 80})
            score_color = get_status_color(overall_score, {'success': 80, 'warning': 60})
            
            # Gerar HTML sem f-strings para evitar conflitos
            html = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📊 Dashboard de Métricas - Codex MMORPG</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}
        
        .header {{
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            text-align: center;
        }}
        
        .header h1 {{
            color: #333;
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .header p {{
            color: #666;
            font-size: 1.2em;
        }}
        
        .metrics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            margin-bottom: 30px;
        }}
        
        .metric-card {{
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }}
        
        .metric-card:hover {{
            transform: translateY(-5px);
        }}
        
        .metric-title {{
            font-size: 1.3em;
            font-weight: bold;
            color: #333;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
        }}
        
        .metric-value {{
            font-size: 2.5em;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        
        .metric-unit {{
            font-size: 0.8em;
            color: #666;
        }}
        
        .progress-bar {{
            width: 100%;
            height: 20px;
            background: #f0f0f0;
            border-radius: 10px;
            overflow: hidden;
            margin-top: 15px;
        }}
        
        .progress-fill {{
            height: 100%;
            border-radius: 10px;
            transition: width 0.3s ease;
        }}
        
        .status-indicator {{
            display: inline-block;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            margin-right: 10px;
        }}
        
        .alerts-section {{
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }}
        
        .alert-item {{
            padding: 15px;
            margin: 10px 0;
            border-radius: 10px;
            border-left: 5px solid;
        }}
        
        .alert-warning {{
            background: #fff3cd;
            border-color: #ffc107;
            color: #856404;
        }}
        
        .alert-danger {{
            background: #f8d7da;
            border-color: #dc3545;
            color: #721c24;
        }}
        
        .alert-success {{
            background: #d4edda;
            border-color: #28a745;
            color: #155724;
        }}
        
        .footer {{
            text-align: center;
            margin-top: 30px;
            color: rgba(255, 255, 255, 0.8);
        }}
        
        @media (max-width: 768px) {{
            .metrics-grid {{
                grid-template-columns: 1fr;
            }}
            
            .header h1 {{
                font-size: 2em;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Dashboard de Métricas</h1>
            <p>Codex MMORPG - Sistema de Monitoramento em Tempo Real</p>
            <p><strong>Última Atualização:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
        
        <div class="metrics-grid">
            <div class="metric-card">
                <div class="metric-title">
                    <span class="status-indicator" style="background-color: {score_color};"></span>
                    Score Geral do Sistema
                </div>
                <div class="metric-value" style="color: {score_color};">{overall_score:.1f}</div>
                <div class="metric-unit">/ 100</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {overall_score}%; background-color: {score_color};"></div>
                </div>
            </div>
            
            <div class="metric-card">
                <div class="metric-title">
                    <span class="status-indicator" style="background-color: {cpu_color};"></span>
                    Uso de CPU
                </div>
                <div class="metric-value" style="color: {cpu_color};">{cpu_usage:.1f}</div>
                <div class="metric-unit">%</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {cpu_usage}%; background-color: {cpu_color};"></div>
                </div>
            </div>
            
            <div class="metric-card">
                <div class="metric-title">
                    <span class="status-indicator" style="background-color: {memory_color};"></span>
                    Uso de Memória
                </div>
                <div class="metric-value" style="color: {memory_color};">{memory_usage:.1f}</div>
                <div class="metric-unit">%</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {memory_usage}%; background-color: {memory_color};"></div>
                </div>
            </div>
            
            <div class="metric-card">
                <div class="metric-title">
                    <span class="status-indicator" style="background-color: {disk_color};"></span>
                    Uso de Disco
                </div>
                <div class="metric-value" style="color: {disk_color};">{disk_usage:.1f}</div>
                <div class="metric-unit">%</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {disk_usage}%; background-color: {disk_color};"></div>
                </div>
            </div>
        </div>
        
        <div class="alerts-section">
            <h2 style="margin-bottom: 20px; color: #333;">🚨 Alertas do Sistema</h2>
"""
            
            # Adicionar alertas
            alerts = kpis.get('alerts', [])
            if alerts:
                for alert in alerts:
                    alert_class = f"alert-{alert['type']}"
                    html += f"""
            <div class="alert-item {alert_class}">
                <strong>{alert['type'].upper()}</strong>: {alert['message']}
            </div>
"""
            else:
                html += """
            <div class="alert-item alert-success">
                <strong>✅ SUCESSO</strong>: Nenhum alerta ativo - Sistema funcionando normalmente
            </div>
"""
            
            # Adicionar footer e JavaScript
            html += f"""
        </div>
        
        <div class="footer">
            <p>🔄 Atualização automática a cada {self.config['refresh_rate']} segundos</p>
            <p>📊 Gerado pelo Dashboard Agent - Codex MMORPG</p>
        </div>
    </div>
    
    <script>
        // Auto-refresh
        setTimeout(function() {{
            location.reload();
        }}, {self.config['refresh_rate'] * 1000});
        
        // Animações
        document.addEventListener('DOMContentLoaded', function() {{
            const cards = document.querySelectorAll('.metric-card');
            cards.forEach((card, index) => {{
                setTimeout(() => {{
                    card.style.opacity = '1';
                    card.style.transform = 'translateY(0)';
                }}, index * 100);
            }});
        }});
    </script>
</body>
</html>
"""
            
            self.logger.info("✅ Dashboard HTML gerado com sucesso")
            return html
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao gerar dashboard HTML: {e}")
            return f"<html><body><h1>Erro ao gerar dashboard: {e}</h1></body></html>"
    
    def generate_markdown_dashboard(self, data: Dict) -> str:
        """Gera dashboard em Markdown"""
        self.logger.info("📝 Gerando dashboard Markdown...")
        
        try:
            system_metrics = data.get("system_metrics", {})
            kpis = data.get("kpis", {})
            
            # Extrair valores
            cpu_usage = system_metrics.get('cpu', {}).get('usage_percent', 0)
            memory_usage = system_metrics.get('memory', {}).get('usage_percent', 0)
            disk_usage = system_metrics.get('disk', {}).get('usage_percent', 0)
            overall_score = kpis.get('overall_score', 0)
            
            # Determinar status
            def get_status_emoji(value, thresholds):
                if value >= thresholds['success']:
                    return "🟢"
                elif value >= thresholds['warning']:
                    return "🟡"
                else:
                    return "🔴"
            
            cpu_status = get_status_emoji(cpu_usage, {'success': 30, 'warning': 60})
            memory_status = get_status_emoji(memory_usage, {'success': 50, 'warning': 75})
            disk_status = get_status_emoji(disk_usage, {'success': 60, 'warning': 80})
            score_status = get_status_emoji(overall_score, {'success': 80, 'warning': 60})
            
            markdown = f"""
# 📊 Dashboard de Métricas - Codex MMORPG

**Data/Hora**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 🎯 Visão Geral

| Métrica | Valor | Status |
|---------|-------|--------|
| **Score Geral** | {overall_score:.1f}/100 | {score_status} |
| **CPU** | {cpu_usage:.1f}% | {cpu_status} |
| **Memória** | {memory_usage:.1f}% | {memory_status} |
| **Disco** | {disk_usage:.1f}% | {disk_status} |

## 📈 Métricas Detalhadas

### 🖥️ Sistema

#### CPU
- **Uso**: {cpu_usage:.1f}%
- **Núcleos**: {system_metrics.get('cpu', {}).get('count', 0)}
- **Frequência**: {system_metrics.get('cpu', {}).get('frequency_mhz', 0):.0f} MHz

#### Memória
- **Total**: {system_metrics.get('memory', {}).get('total_gb', 0):.1f} GB
- **Usado**: {system_metrics.get('memory', {}).get('used_gb', 0):.1f} GB
- **Uso**: {memory_usage:.1f}%

#### Disco
- **Total**: {system_metrics.get('disk', {}).get('total_gb', 0):.1f} GB
- **Usado**: {system_metrics.get('disk', {}).get('used_gb', 0):.1f} GB
- **Uso**: {disk_usage:.1f}%

### 📊 KPIs da Aplicação

| KPI | Valor | Meta |
|-----|-------|------|
| **Taxa de Conclusão de Tarefas** | {kpis.get('application_kpis', {}).get('task_completion_rate', 0):.1f}% | ≥95% |
| **Disponibilidade de Agentes** | {kpis.get('application_kpis', {}).get('agent_availability', 0):.1f}% | ≥98% |
| **Tempo de Resposta** | {kpis.get('application_kpis', {}).get('response_time_seconds', 0):.2f}s | ≤2s |
| **Taxa de Erro** | {kpis.get('application_kpis', {}).get('error_rate_percent', 0):.1f}% | ≤2% |
| **Taxa de Cache Hit** | {kpis.get('application_kpis', {}).get('cache_hit_rate_percent', 0):.1f}% | ≥90% |

## 🚨 Alertas

"""
            
            # Adicionar alertas
            alerts = kpis.get('alerts', [])
            if alerts:
                for alert in alerts:
                    emoji = "🔴" if alert['type'] == 'critical' else "🟡" if alert['type'] == 'warning' else "🔵"
                    markdown += f"- {emoji} **{alert['type'].upper()}**: {alert['message']}\n"
            else:
                markdown += "- ✅ **SUCCESS**: Nenhum alerta ativo - Sistema funcionando normalmente\n"
            
            markdown += f"""
## 📋 Status do Sistema

- **Status Geral**: {'🟢 Saudável' if overall_score >= 80 else '🟡 Atenção' if overall_score >= 60 else '🔴 Crítico'}
- **Última Atualização**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Próxima Atualização**: {(datetime.now() + timedelta(seconds=self.config['update_interval'])).strftime('%Y-%m-%d %H:%M:%S')}

## 🔄 Histórico de Atualizações

- **Dashboard HTML**: `{self.output_path / self.config['dashboard_html']}`
- **Dashboard Markdown**: `{self.output_path / self.config['dashboard_md']}`
- **Dados JSON**: `{self.metrics_path / self.config['kpis_file']}`

---

*Dashboard gerado automaticamente pelo Dashboard Agent*
"""
            
            self.logger.info("✅ Dashboard Markdown gerado com sucesso")
            return markdown
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao gerar dashboard Markdown: {e}")
            return f"# Erro ao gerar dashboard: {e}"
    
    def save_dashboard(self, html_content: str, markdown_content: str) -> bool:
        """Salva dashboards em arquivos"""
        try:
            # Salvar HTML
            html_file = self.output_path / self.config["dashboard_html"]
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            # Salvar Markdown
            md_file = self.output_path / self.config["dashboard_md"]
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            self.logger.info(f"✅ Dashboards salvos em: {self.output_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao salvar dashboards: {e}")
            return False
    
    def run(self):
        """Executa o agente de dashboard"""
        self.logger.info("🚀 Iniciando Dashboard Agent...")
        
        try:
            # Carregar dados
            data = self.load_metrics_data()
            
            if not data:
                self.logger.error("❌ Nenhum dado de métricas encontrado")
                return False
            
            # Gerar dashboards
            html_dashboard = self.generate_html_dashboard(data)
            markdown_dashboard = self.generate_markdown_dashboard(data)
            
            # Salvar dashboards
            success = self.save_dashboard(html_dashboard, markdown_dashboard)
            
            if success:
                self.logger.info("✅ Dashboard Agent executado com sucesso")
                return True
            else:
                self.logger.error("❌ Erro ao salvar dashboards")
                return False
                
        except Exception as e:
            self.logger.error(f"❌ Erro na execução do Dashboard Agent: {e}")
            return False

def main():
    """Função principal"""
    agent = DashboardAgent()
    success = agent.run()
    
    if success:
        print("✅ Dashboard Agent executado com sucesso")
        return 0
    else:
        print("❌ Erro na execução do Dashboard Agent")
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
        print(f"✅ Script dashboard_agent.py executado com sucesso via módulo agents.agent_orchestrator")
    else:
        print(f"❌ Erro na execução do script dashboard_agent.py via módulo agents.agent_orchestrator")

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
- **Nome**: migrated_dashboard_agent
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

