"""
migrated_dashboard_monitoring



Módulo: migrated_dashboard_monitoring
Caminho: wiki\update\modules\metrics\dashboard_monitor\migrated_dashboard_monitoring.py
Linhas de código: 640
Complexidade: 47.00

Funções (15):
- main(): Função principal do script....\n- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self, metrics_dir, dashboard_dir): Inicializa o dashboard de monitoramento.

Args:
  ...\n- load_metrics_data(self): Carrega dados das métricas.

Returns:
    Dados da...\n- calculate_system_status(self, metrics_data): Calcula status geral do sistema.

Args:
    metric...\n- generate_alerts(self, status): Gera alertas baseados no status do sistema.

Args:...\n- create_dashboard_data(self, metrics_data, status, alerts): Cria dados do dashboard.

Args:
    metrics_data: ...\n- extract_performance_history(self, performance_data): Extrai histórico de performance para gráficos.

Ar...\n- extract_usage_history(self, usage_data): Extrai histórico de uso para gráficos.

Args:
    ...\n- extract_quality_history(self, quality_data): Extrai histórico de qualidade para gráficos.

Args...\n- save_dashboard_data(self, dashboard_data): Salva dados do dashboard.

Args:
    dashboard_dat...\n- save_alerts(self, alerts): Salva alertas do sistema.

Args:
    alerts: Lista...\n- save_system_status(self, status): Salva status do sistema.

Args:
    status: Status...\n- generate_dashboard_report(self): Gera relatório do dashboard.

Returns:
    Caminho...\n- create_monitoring_dashboard(self): Cria dashboard completo de monitoramento.

Returns...\n
Classes (1):
- DashboardMonitoring: Dashboard de monitoramento do sistema...\n  - __init__(self, metrics_dir, dashboard_dir): Inicializa o dashboard de moni...\n  - load_metrics_data(self): Carrega dados das métricas.

R...\n  - calculate_system_status(self, metrics_data): Calcula status geral do sistem...\n  - generate_alerts(self, status): Gera alertas baseados no statu...\n  - create_dashboard_data(self, metrics_data, status, alerts): Cria dados do dashboard.

Args...\n  - extract_performance_history(self, performance_data): Extrai histórico de performanc...\n  - extract_usage_history(self, usage_data): Extrai histórico de uso para g...\n  - extract_quality_history(self, quality_data): Extrai histórico de qualidade ...\n  - save_dashboard_data(self, dashboard_data): Salva dados do dashboard.

Arg...\n  - save_alerts(self, alerts): Salva alertas do sistema.

Arg...\n  - save_system_status(self, status): Salva status do sistema.

Args...\n  - generate_dashboard_report(self): Gera relatório do dashboard.

...\n  - create_monitoring_dashboard(self): Cria dashboard completo de mon...\n
Imports (5):
.DashboardmonitorModule, json, datetime.datetime, datetime.timedelta, logging

Autor: Documentation Agent
Data: 2025-08-01 15:05:53
"""

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
- **Nome**: docstring
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

