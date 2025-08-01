"""
migrated_migrated_performance_monitor



Módulo: migrated_migrated_performance_monitor
Caminho: wiki\update\modules\maps\map_updater\migrated_migrated_performance_monitor.py
Linhas de código: 529
Complexidade: 47.00

Funções (15):
- main(): Função principal do script....\n- integrate_with_module(): Integra o script com o módulo de destino....\n- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self, project_root, monitor_dir): Inicializa o monitor de performance.

Args:
    pr...\n- load_metrics(self): Carrega métricas de performance existentes....\n- save_metrics(self): Salva métricas de performance....\n- collect_system_metrics(self): Coleta métricas do sistema....\n- collect_project_metrics(self): Coleta métricas específicas do projeto....\n- check_performance_thresholds(self, system_metrics, project_metrics): Verifica se as métricas excedem os limites definid...\n- record_metrics(self, system_metrics, project_metrics, alerts): Registra métricas coletadas....\n- _cleanup_old_metrics(self): Remove métricas antigas para economizar espaço....\n- start_monitoring(self): Inicia o monitoramento contínuo....\n- stop_monitoring(self): Para o monitoramento contínuo....\n- _monitoring_loop(self): Loop principal de monitoramento....\n- get_performance_report(self): Gera relatório de performance....\n
Classes (1):
- PerformanceMonitor: Sistema de monitoramento de performance....\n  - __init__(self, project_root, monitor_dir): Inicializa o monitor de perfor...\n  - load_metrics(self): Carrega métricas de performanc...\n  - save_metrics(self): Salva métricas de performance....\n  - collect_system_metrics(self): Coleta métricas do sistema....\n  - collect_project_metrics(self): Coleta métricas específicas do...\n  - check_performance_thresholds(self, system_metrics, project_metrics): Verifica se as métricas excede...\n  - record_metrics(self, system_metrics, project_metrics, alerts): Registra métricas coletadas....\n  - _cleanup_old_metrics(self): Remove métricas antigas para e...\n  - start_monitoring(self): Inicia o monitoramento contínu...\n  - stop_monitoring(self): Para o monitoramento contínuo....\n  - _monitoring_loop(self): Loop principal de monitorament...\n  - get_performance_report(self): Gera relatório de performance....\n
Imports (10):
.MapupdaterModule, .PerformancemonitorModule, json, time, psutil, threading, datetime.datetime, datetime.timedelta, logging, argparse

Autor: Documentation Agent
Data: 2025-08-01 15:05:56
"""
