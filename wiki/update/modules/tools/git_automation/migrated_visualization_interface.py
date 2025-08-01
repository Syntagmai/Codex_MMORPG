# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
MAX_ITEMS = 100
TIMEOUT_SECONDS = 60

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: visualization_interface.py
Módulo de Destino: tools.git_automation
Data de Migração: 2025-08-01 12:21:45

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import GitautomationModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interface de Visualização para Auto-Aprendizado
Mostra métricas, aprendizados e insights do sistema de auto aprendizado
"""

import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from collections import defaultdict
import statistics

class VisualizationInterface:
    """Interface de visualização para o sistema de auto aprendizado"""
    
    def __init__(self, auto_learning_path: Path):
        self.auto_learning_path = auto_learning_path
        self.visualizations_path = auto_learning_path / "visualizations"
        self.reports_path = auto_learning_path / "reports"
        
        # Criar pastas necessárias
        self.visualizations_path.mkdir(parents=True, exist_ok=True)
        self.reports_path.mkdir(parents=True, exist_ok=True)
        
        # Configurações de visualização
        plt.style.use('seaborn-v0_8')
        self.colors = {
            'success': '#2ecc71',
            'failure': '#e74c3c',
            'optimization': '#3498db',
            'neutral': '#95a5a6'
        }
    
    def generate_learning_dashboard(self, learning_stats: Dict[str, Any], 
                                  feedback_stats: Dict[str, Any],
                                  optimization_stats: Dict[str, Any]) -> str:
        """Gera dashboard completo de aprendizado"""
        dashboard_html = self._create_dashboard_html(learning_stats, feedback_stats, optimization_stats)
        
        # Salvar dashboard
        dashboard_file = self.visualizations_path / "learning_dashboard.html"
        with open(dashboard_file, 'w', encoding='utf-8') as f:
            f.write(dashboard_html)
        
        return str(dashboard_file)
    
    def _create_dashboard_html(self, learning_stats: Dict[str, Any], 
                             feedback_stats: Dict[str, Any],
                             optimization_stats: Dict[str, Any]) -> str:
        """Cria HTML do dashboard"""
        html = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Auto-Aprendizado BMAD - Dashboard</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.5em;
        }}
        .header p {{
            margin: 10px 0 0 0;
            opacity: 0.9;
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .stat-card {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s;
        }}
        .stat-card:hover {{
            transform: translateY(-5px);
        }}
        .stat-card h3 {{
            margin: 0 0 15px 0;
            color: #333;
            font-size: 1.2em;
        }}
        .stat-value {{
            font-size: 2.5em;
            font-weight: bold;
            margin: 10px 0;
        }}
        .stat-success {{ color: #2ecc71; }}
        .stat-warning {{ color: #f39c12; }}
        .stat-danger {{ color: #e74c3c; }}
        .stat-info {{ color: #3498db; }}
        .stat-description {{
            color: #666;
            font-size: 0.9em;
        }}
        .chart-container {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }}
        .chart-container h3 {{
            margin: 0 0 20px 0;
            color: #333;
        }}
        .progress-bar {{
            width: 100%;
            height: 20px;
            background-color: #ecf0f1;
            border-radius: 10px;
            overflow: hidden;
            margin: 10px 0;
        }}
        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #2ecc71, #27ae60);
            transition: width 0.3s ease;
        }}
        .recommendations {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        .recommendation-item {{
            background: #f8f9fa;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
            border-left: 4px solid #3498db;
        }}
        .recommendation-item h4 {{
            margin: 0 0 10px 0;
            color: #333;
        }}
        .recommendation-item p {{
            margin: 0;
            color: #666;
        }}
        .timestamp {{
            text-align: center;
            color: #666;
            font-size: 0.9em;
            margin-top: 30px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🧠 Sistema de Auto-Aprendizado BMAD</h1>
            <p>Dashboard de Métricas e Aprendizados</p>
        </div>
        
        <div class="stats-grid">
            <div class="stat-card">
                <h3>📊 Interações Totais</h3>
                <div class="stat-value stat-info">{learning_stats.get('total_interactions', 0)}</div>
                <div class="stat-description">Total de interações analisadas pelo sistema</div>
            </div>
            
            <div class="stat-card">
                <h3>🎯 Padrões Aprendidos</h3>
                <div class="stat-value stat-success">{learning_stats.get('patterns_learned', 0)}</div>
                <div class="stat-description">Padrões identificados e armazenados</div>
            </div>
            
            <div class="stat-card">
                <h3>⚡ Otimizações Aplicadas</h3>
                <div class="stat-value stat-warning">{learning_stats.get('optimizations_applied', 0)}</div>
                <div class="stat-description">Otimizações aplicadas automaticamente</div>
            </div>
            
            <div class="stat-card">
                <h3>📈 Score Médio de Feedback</h3>
                <div class="stat-value stat-success">{feedback_stats.get('avg_score', 0):.2f}</div>
                <div class="stat-description">Score médio das avaliações dos usuários</div>
            </div>
        </div>
        
        <div class="chart-container">
            <h3>📊 Distribuição de Sentimento</h3>
            <div style="display: flex; gap: 20px; align-items: center;">
                <div style="flex: 1;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                        <span>Positivo</span>
                        <span>{feedback_stats.get('sentiment_distribution', {}).get('positive', 0)}</span>
                    </div>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {self._calculate_percentage(feedback_stats.get('sentiment_distribution',
    
    
    
    
    
    
    
    {}).get('positive', 0), feedback_stats.get('total_feedback', 1))}%"></div>
                    </div>
                </div>
                <div style="flex: 1;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                        <span>Neutro</span>
                        <span>{feedback_stats.get('sentiment_distribution', {}).get('neutral', 0)}</span>
                    </div>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {self._calculate_percentage(feedback_stats.get('sentiment_distribution',
    
    
    
    
    
    
    
    {}).get('neutral', 0), feedback_stats.get('total_feedback', 1))}%"></div>
                    </div>
                </div>
                <div style="flex: 1;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                        <span>Negativo</span>
                        <span>{feedback_stats.get('sentiment_distribution', {}).get('negative', 0)}</span>
                    </div>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {self._calculate_percentage(feedback_stats.get('sentiment_distribution',
    
    
    
    
    
    
    
    {}).get('negative', 0), feedback_stats.get('total_feedback', 1))}%"></div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="chart-container">
            <h3>🔧 Regras de Otimização</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px;">
                {self._generate_optimization_rules_html(optimization_stats)}
            </div>
        </div>
        
        <div class="recommendations">
            <h3>💡 Recomendações de Melhoria</h3>
            {self._generate_recommendations_html(learning_stats, feedback_stats, optimization_stats)}
        </div>
        
        <div class="timestamp">
            Dashboard gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
        </div>
    </div>
</body>
</html>
        """
        return html
    
    def _calculate_percentage(self, value: int, total: int) -> float:
        """Calcula porcentagem"""
        if total == 0:
            return 0
        return (value / total) * 100
    
    def _generate_optimization_rules_html(self, optimization_stats: Dict[str, Any]) -> str:
        """Gera HTML para regras de otimização"""
        html = ""
        rules_by_type = optimization_stats.get('rules_by_type', {})
        
        for rule_type, count in rules_by_type.items():
            html += f"""
            <div style="background: #f8f9fa; padding: 15px; border-radius: 5px; text-align: center;">
                <div style="font-size: 1.5em; font-weight: bold; color: #3498db;">{count}</div>
                <div style="color: #666; font-size: 0.9em;">{rule_type.replace('_', ' ').title()}</div>
            </div>
            """
        
        return html
    
    def _generate_recommendations_html(self, learning_stats: Dict[str, Any], 
                                     feedback_stats: Dict[str, Any],
                                     optimization_stats: Dict[str, Any]) -> str:
        """Gera HTML para recomendações"""
        recommendations = []
        
        # Recomendação baseada no número de interações
        if learning_stats.get('total_interactions', 0) < 50:
            recommendations.append({
                'title': 'Coletar Mais Dados',
                'description': 'O sistema precisa de mais interações para aprender padrões eficazes.'
            })
        
        # Recomendação baseada no score de feedback
        avg_score = feedback_stats.get('avg_score', 0)
        if avg_score < 0.6:
            recommendations.append({
                'title': 'Melhorar Qualidade',
                'description': f'Score médio baixo ({avg_score:.2f}) - revisar workflows problemáticos.'
            })
        
        # Recomendação baseada em otimizações
        success_rate = optimization_stats.get('success_rate', 0)
        if success_rate < 0.5:
            recommendations.append({
                'title': 'Otimizar Regras',
                'description': f'Taxa de sucesso das otimizações baixa ({success_rate:.2f}) - revisar regras.'
            })
        
        # Recomendação baseada em padrões
        patterns_learned = learning_stats.get('patterns_learned', 0)
        if patterns_learned < 10:
            recommendations.append({
                'title': 'Identificar Padrões',
                'description': 'Poucos padrões identificados - analisar mais interações.'
            })
        
        if not recommendations:
            recommendations.append({
                'title': 'Sistema Funcionando Bem',
                'description': 'O sistema está aprendendo adequadamente e aplicando otimizações.'
            })
        
        html = ""
        for rec in recommendations:
            html += f"""
            <div class="recommendation-item">
                <h4>{rec['title']}</h4>
                <p>{rec['description']}</p>
            </div>
            """
        
        return html
    
    def generate_learning_report(self, learning_stats: Dict[str, Any], 
                               feedback_stats: Dict[str, Any],
                               optimization_stats: Dict[str, Any]) -> str:
        """Gera relatório detalhado de aprendizado"""
        report_content = self._create_learning_report(learning_stats, feedback_stats, optimization_stats)
        
        # Salvar relatório
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_file = self.reports_path / f"learning_report_{timestamp}.md"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        return str(report_file)
    
    def _create_learning_report(self, learning_stats: Dict[str, Any], 
                              feedback_stats: Dict[str, Any],
                              optimization_stats: Dict[str, Any]) -> str:
        """Cria conteúdo do relatório de aprendizado"""
        report = f"""# Relatório de Aprendizado - Sistema BMAD

**Data**: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}  
**Período**: Últimos 30 dias

---

## 📊 Resumo Executivo

O sistema de auto aprendizado BMAD demonstrou **{'excelente' if learning_stats.get('patterns_learned',
    0) > 20 else 'bom' if learning_stats.get('patterns_learned',
    0) > 10 else 'moderado'}** desempenho no período analisado.

### Principais Métricas:
- **Interações Analisadas**: {learning_stats.get('total_interactions', 0)}
- **Padrões Aprendidos**: {learning_stats.get('patterns_learned', 0)}
- **Otimizações Aplicadas**: {learning_stats.get('optimizations_applied', 0)}
- **Score Médio de Feedback**: {feedback_stats.get('avg_score', 0):.2f}

---

## 🧠 Análise de Aprendizado

### Padrões Identificados
O sistema identificou **{learning_stats.get('patterns_learned', 0)}** padrões distintos, distribuídos da seguinte forma:

- **Padrões de Sucesso**: {learning_stats.get('success_patterns', 0)}
- **Padrões de Falha**: {learning_stats.get('failure_patterns', 0)}
- **Padrões de Otimização**: {learning_stats.get('optimization_patterns', 0)}

### Confiança dos Padrões
- **Confiança Média**: {learning_stats.get('avg_confidence', 0):.2f}
- **Padrões de Alta Confiança** (>0.8): {learning_stats.get('high_confidence_patterns', 0)}
- **Padrões de Baixa Confiança** (<0.5): {learning_stats.get('low_confidence_patterns', 0)}

---

## 📈 Análise de Feedback

### Distribuição de Sentimento
- **Positivo**: {feedback_stats.get('sentiment_distribution', {}).get('positive',
    0)} ({self._calculate_percentage(feedback_stats.get('sentiment_distribution', {}).get('positive', 0),
    feedback_stats.get('total_feedback', 1)):.1f}%)
- **Neutro**: {feedback_stats.get('sentiment_distribution', {}).get('neutral',
    0)} ({self._calculate_percentage(feedback_stats.get('sentiment_distribution', {}).get('neutral', 0),
    feedback_stats.get('total_feedback', 1)):.1f}%)
- **Negativo**: {feedback_stats.get('sentiment_distribution', {}).get('negative',
    0)} ({self._calculate_percentage(feedback_stats.get('sentiment_distribution', {}).get('negative', 0),
    feedback_stats.get('total_feedback', 1)):.1f}%)

### Sugestões de Melhoria
{self._format_improvement_suggestions(feedback_stats)}

---

## ⚡ Análise de Otimização

### Regras de Otimização
- **Total de Regras**: {optimization_stats.get('total_rules', 0)}
- **Taxa de Sucesso**: {optimization_stats.get('success_rate', 0):.2f}
- **Otimizações Aplicadas**: {optimization_stats.get('total_optimizations', 0)}

### Regras por Tipo
{self._format_optimization_rules(optimization_stats)}

### Regras Mais Efetivas
{self._format_most_effective_rules(optimization_stats)}

---

## 💡 Recomendações

### Ações Imediatas
{self._generate_immediate_actions(learning_stats, feedback_stats, optimization_stats)}

### Ações de Médio Prazo
{self._generate_medium_term_actions(learning_stats, feedback_stats, optimization_stats)}

### Ações de Longo Prazo
{self._generate_long_term_actions(learning_stats, feedback_stats, optimization_stats)}

---

## 📋 Próximos Passos

1. **Monitorar** aplicação das recomendações
2. **Coletar** feedback adicional sobre otimizações
3. **Ajustar** parâmetros baseado em resultados
4. **Expandir** análise para novos tipos de interação

---

*Relatório gerado automaticamente pelo Sistema de Auto-Aprendizado BMAD*
"""
        return report
    
    def _format_improvement_suggestions(self, feedback_stats: Dict[str, Any]) -> str:
        """Formata sugestões de melhoria"""
        suggestions = feedback_stats.get('improvement_suggestions', [])
        
        if not suggestions:
            return "Nenhuma sugestão específica identificada no período."
        
        formatted = ""
        for i, suggestion in enumerate(suggestions[:5], 1):
            formatted += f"{i}. **{suggestion['suggestion']}** (mencionado {suggestion['count']} vezes)\n"
        
        return formatted
    
    def _format_optimization_rules(self, optimization_stats: Dict[str, Any]) -> str:
        """Formata regras de otimização"""
        rules_by_type = optimization_stats.get('rules_by_type', {})
        
        if not rules_by_type:
            return "Nenhuma regra de otimização ativa."
        
        formatted = ""
        for rule_type, count in rules_by_type.items():
            formatted += f"- **{rule_type.replace('_', ' ').title()}**: {count} regras\n"
        
        return formatted
    
    def _format_most_effective_rules(self, optimization_stats: Dict[str, Any]) -> str:
        """Formata regras mais efetivas"""
        most_used_rules = optimization_stats.get('most_used_rules', [])
        
        if not most_used_rules:
            return "Dados insuficientes para análise."
        
        formatted = ""
        for i, rule in enumerate(most_used_rules[:5], 1):
            formatted += f"{i}. **{rule['rule_type']}** - Uso: {rule['usage_count']},
    Sucesso: {rule['success_rate']:.2f}\n"
        
        return formatted
    
    def _generate_immediate_actions(self, learning_stats: Dict[str, Any], 
                                  feedback_stats: Dict[str, Any],
                                  optimization_stats: Dict[str, Any]) -> str:
        """Gera ações imediatas"""
        actions = []
        
        if feedback_stats.get('avg_score', 0) < 0.6:
            actions.append("Revisar workflows com baixo score de feedback")
        
        if optimization_stats.get('success_rate', 0) < 0.5:
            actions.append("Ajustar regras de otimização com baixa taxa de sucesso")
        
        if learning_stats.get('patterns_learned', 0) < 10:
            actions.append("Aumentar coleta de dados para melhor aprendizado")
        
        if not actions:
            actions.append("Manter configurações atuais - sistema funcionando adequadamente")
        
        return "\n".join([f"- {action}" for action in actions])
    
    def _generate_medium_term_actions(self, learning_stats: Dict[str, Any], 
                                    feedback_stats: Dict[str, Any],
                                    optimization_stats: Dict[str, Any]) -> str:
        """Gera ações de médio prazo"""
        actions = []
        
        actions.append("Implementar análise de tendências temporais")
        actions.append("Desenvolver novos tipos de padrões de aprendizado")
        actions.append("Otimizar algoritmos de clustering de padrões")
        
        return "\n".join([f"- {action}" for action in actions])
    
    def _generate_long_term_actions(self, learning_stats: Dict[str, Any], 
                                  feedback_stats: Dict[str, Any],
                                  optimization_stats: Dict[str, Any]) -> str:
        """Gera ações de longo prazo"""
        actions = []
        
        actions.append("Integrar aprendizado com outros sistemas BMAD")
        actions.append("Implementar predição de performance")
        actions.append("Desenvolver interface de configuração avançada")
        
        return "\n".join([f"- {action}" for action in actions])
    
    def create_performance_chart(self, performance_data: List[Dict[str, Any]]) -> str:
        """Cria gráfico de performance"""
        if not performance_data:
            return ""
        
        # Preparar dados
        dates = [datetime.fromisoformat(d['timestamp']) for d in performance_data]
        scores = [d['success_score'] for d in performance_data]
        
        # Criar gráfico
        plt.figure(figsize=(12, 6))
        plt.plot(dates, scores, marker='o', linewidth=2, markersize=4)
        plt.title('Evolução do Score de Sucesso', fontsize=14, fontweight='bold')
        plt.xlabel('Data')
        plt.ylabel('Score de Sucesso')
        plt.grid(True, alpha=0.3)
        
        # Formatar eixo X
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
        plt.xticks(rotation=45)
        
        # Salvar gráfico
        chart_file = self.visualizations_path / "performance_chart.png"
        plt.tight_layout()
        plt.savefig(chart_file, dpi=300, bbox_inches='tight')
        plt.close()
        
        return str(chart_file) 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = GitautomationModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script visualization_interface.py executado com sucesso via módulo tools.git_automation")
    else:
        print(f"❌ Erro na execução do script visualization_interface.py via módulo tools.git_automation")
