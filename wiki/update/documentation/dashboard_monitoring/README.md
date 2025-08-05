# dashboard_monitoring

## Descrição

Dashboard de Monitoramento
=========================

Este script cria interface para visualizar métricas do sistema BMAD
com gráficos, alertas e visualizações em tempo real.

Autor: Sistema BMAD - Dashboard Agent
Data: 2025-08-01

## Informações Técnicas

- **Módulo**: dashboard_monitoring
- **Caminho**: wiki\update\dashboard_monitoring.py
- **Linhas de código**: 608
- **Complexidade**: 45.00
- **Funções**: 14
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Função principal do script.

### __init__

**Parâmetros**: self, metrics_dir, dashboard_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Inicializa o dashboard de monitoramento.

Args:
    metrics_dir: Diretório das métricas
    dashboard_dir: Diretório do dashboard

### load_metrics_data

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Carrega dados das métricas.

Returns:
    Dados das métricas

### calculate_system_status

**Parâmetros**: self, metrics_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 114

Calcula status geral do sistema.

Args:
    metrics_data: Dados das métricas
    
Returns:
    Status do sistema

### generate_alerts

**Parâmetros**: self, status
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 78

Gera alertas baseados no status do sistema.

Args:
    status: Status do sistema
    
Returns:
    Lista de alertas

### create_dashboard_data

**Parâmetros**: self, metrics_data, status, alerts
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 79

Cria dados do dashboard.

Args:
    metrics_data: Dados das métricas
    status: Status do sistema
    alerts: Alertas gerados
    
Returns:
    Dados do dashboard

### extract_performance_history

**Parâmetros**: self, performance_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Extrai histórico de performance para gráficos.

Args:
    performance_data: Dados de performance
    
Returns:
    Dados para gráficos

### extract_usage_history

**Parâmetros**: self, usage_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Extrai histórico de uso para gráficos.

Args:
    usage_data: Dados de uso
    
Returns:
    Dados para gráficos

### extract_quality_history

**Parâmetros**: self, quality_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Extrai histórico de qualidade para gráficos.

Args:
    quality_data: Dados de qualidade
    
Returns:
    Dados para gráficos

### save_dashboard_data

**Parâmetros**: self, dashboard_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Salva dados do dashboard.

Args:
    dashboard_data: Dados do dashboard

### save_alerts

**Parâmetros**: self, alerts
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Salva alertas do sistema.

Args:
    alerts: Lista de alertas

### save_system_status

**Parâmetros**: self, status
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Salva status do sistema.

Args:
    status: Status do sistema

### generate_dashboard_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 48

Gera relatório do dashboard.

Returns:
    Caminho do relatório

### create_monitoring_dashboard

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Cria dashboard completo de monitoramento.

Returns:
    Resultados da criação

## Classes

### DashboardMonitoring

**Herança**: Nenhuma
**Atributos**: metrics_data, status, alerts, dashboard_data, history, history, history, metrics_data, status, alerts, dashboard_data, report, report_file, report_path, files_created, results, critical_count, warning_count, latest_perf, total_files, total_size, latest_usage, total_docs, indexed_docs, latest_quality, quality_score, trends, recommendations, quality_data, usage_data, latest_perf, latest_usage, latest_quality, coverage, quality_status, quality_status, quality_status
**Métodos**: 13
**Linhas**: 560

Dashboard de monitoramento do sistema

#### __init__

**Parâmetros**: self, metrics_dir, dashboard_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Inicializa o dashboard de monitoramento.

Args:
    metrics_dir: Diretório das métricas
    dashboard_dir: Diretório do dashboard

#### load_metrics_data

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Carrega dados das métricas.

Returns:
    Dados das métricas

#### calculate_system_status

**Parâmetros**: self, metrics_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 114

Calcula status geral do sistema.

Args:
    metrics_data: Dados das métricas
    
Returns:
    Status do sistema

#### generate_alerts

**Parâmetros**: self, status
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 78

Gera alertas baseados no status do sistema.

Args:
    status: Status do sistema
    
Returns:
    Lista de alertas

#### create_dashboard_data

**Parâmetros**: self, metrics_data, status, alerts
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 79

Cria dados do dashboard.

Args:
    metrics_data: Dados das métricas
    status: Status do sistema
    alerts: Alertas gerados
    
Returns:
    Dados do dashboard

#### extract_performance_history

**Parâmetros**: self, performance_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Extrai histórico de performance para gráficos.

Args:
    performance_data: Dados de performance
    
Returns:
    Dados para gráficos

#### extract_usage_history

**Parâmetros**: self, usage_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Extrai histórico de uso para gráficos.

Args:
    usage_data: Dados de uso
    
Returns:
    Dados para gráficos

#### extract_quality_history

**Parâmetros**: self, quality_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Extrai histórico de qualidade para gráficos.

Args:
    quality_data: Dados de qualidade
    
Returns:
    Dados para gráficos

#### save_dashboard_data

**Parâmetros**: self, dashboard_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Salva dados do dashboard.

Args:
    dashboard_data: Dados do dashboard

#### save_alerts

**Parâmetros**: self, alerts
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Salva alertas do sistema.

Args:
    alerts: Lista de alertas

#### save_system_status

**Parâmetros**: self, status
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Salva status do sistema.

Args:
    status: Status do sistema

#### generate_dashboard_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 48

Gera relatório do dashboard.

Returns:
    Caminho do relatório

#### create_monitoring_dashboard

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Cria dashboard completo de monitoramento.

Returns:
    Resultados da criação

## Imports

json, os, pathlib.Path, typing.Dict, typing.List, typing.Any, typing.Optional, datetime.datetime, datetime.timedelta, logging

## Uso

```python
# Exemplo de uso do módulo dashboard_monitoring
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:50

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

