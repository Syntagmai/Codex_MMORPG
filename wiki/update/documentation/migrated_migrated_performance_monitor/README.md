# migrated_migrated_performance_monitor

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_migrated_performance_monitor
- **Caminho**: wiki\update\modules\maps\map_updater\migrated_migrated_performance_monitor.py
- **Linhas de código**: 529
- **Complexidade**: 47.00
- **Funções**: 15
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 66

Função principal do script.

### integrate_with_module

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Integra o script com o módulo de destino.

### integrate_with_module

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Integra o script com o módulo de destino.

### __init__

**Parâmetros**: self, project_root, monitor_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Inicializa o monitor de performance.

Args:
    project_root: Diretório raiz do projeto
    monitor_dir: Diretório para armazenar dados de monitoramento

### load_metrics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Carrega métricas de performance existentes.

### save_metrics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Salva métricas de performance.

### collect_system_metrics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 47

Coleta métricas do sistema.

### collect_project_metrics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 59

Coleta métricas específicas do projeto.

### check_performance_thresholds

**Parâmetros**: self, system_metrics, project_metrics
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 56

Verifica se as métricas excedem os limites definidos.

### record_metrics

**Parâmetros**: self, system_metrics, project_metrics, alerts
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Registra métricas coletadas.

### _cleanup_old_metrics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Remove métricas antigas para economizar espaço.

### start_monitoring

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Inicia o monitoramento contínuo.

### stop_monitoring

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Para o monitoramento contínuo.

### _monitoring_loop

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Loop principal de monitoramento.

### get_performance_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 45

Gera relatório de performance.

## Classes

### PerformanceMonitor

**Herança**: Nenhuma
**Atributos**: alerts, combined_metrics, cutoff_date, latest_metrics, cutoff_time, recent_metrics, recent_alerts, cpu_percent, cpu_count, memory, memory_percent, memory_available, disk, disk_percent, disk_free, python_processes, metrics, cutoff_time, maps_dir, avg_cpu, avg_memory, avg_disk, avg_cpu, avg_memory, avg_disk, system_metrics, project_metrics, alerts, file_size_mb, mtime, file_size_mb
**Métodos**: 12
**Linhas**: 366

Sistema de monitoramento de performance.

#### __init__

**Parâmetros**: self, project_root, monitor_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Inicializa o monitor de performance.

Args:
    project_root: Diretório raiz do projeto
    monitor_dir: Diretório para armazenar dados de monitoramento

#### load_metrics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Carrega métricas de performance existentes.

#### save_metrics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Salva métricas de performance.

#### collect_system_metrics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 47

Coleta métricas do sistema.

#### collect_project_metrics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 59

Coleta métricas específicas do projeto.

#### check_performance_thresholds

**Parâmetros**: self, system_metrics, project_metrics
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 56

Verifica se as métricas excedem os limites definidos.

#### record_metrics

**Parâmetros**: self, system_metrics, project_metrics, alerts
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Registra métricas coletadas.

#### _cleanup_old_metrics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Remove métricas antigas para economizar espaço.

#### start_monitoring

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Inicia o monitoramento contínuo.

#### stop_monitoring

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Para o monitoramento contínuo.

#### _monitoring_loop

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Loop principal de monitoramento.

#### get_performance_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 45

Gera relatório de performance.

## Imports

.MapupdaterModule, .PerformancemonitorModule, json, time, psutil, threading, datetime.datetime, datetime.timedelta, logging, argparse

## Uso

```python
# Exemplo de uso do módulo migrated_migrated_performance_monitor
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:56

## 🔗 **Links Automáticos**

> [!info] **Links Gerados Automaticamente**
> Estes links foram criados automaticamente pelo sistema de linkagem da categoria **Tools**

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]
- [[../maps/tools_index|Índice de Ferramentas]]
- [[../update/README|Scripts de Atualização]]

### **🧭 Navegação**
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]
- [[../maps/category_indices|Índices por Categoria]]
- [[../maps/relationships|Relacionamentos]]

### **📊 Métricas da Categoria**
- **Categoria**: Tools
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

