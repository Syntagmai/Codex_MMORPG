# Documentação Técnica - migrated_migrated_performance_monitor

## Análise Estática

### Métricas de Código
- **Linhas de código**: 529
- **Complexidade ciclomática**: 47.00
- **Funções**: 15
- **Classes**: 1
- **Imports**: 10

### Análise de Complexidade
- **Nível**: Alto (Código complexo, considere refatoração)\n
### Estrutura de Dependências

#### Imports Externos
.MapupdaterModule, .PerformancemonitorModule, json, time, psutil, threading, datetime.datetime, datetime.timedelta, logging, argparse

#### Hierarquia de Classes
- PerformanceMonitor (sem herança)\n
### Análise de Funções

#### Funções Principais
**main**
- Parâmetros: 0
- Linhas: 66
- Documentação: Sim

**integrate_with_module**
- Parâmetros: 0
- Linhas: 3
- Documentação: Sim

**integrate_with_module**
- Parâmetros: 0
- Linhas: 3
- Documentação: Sim

**__init__**
- Parâmetros: 3
- Linhas: 30
- Documentação: Sim

**load_metrics**
- Parâmetros: 1
- Linhas: 23
- Documentação: Sim

**save_metrics**
- Parâmetros: 1
- Linhas: 6
- Documentação: Sim

**collect_system_metrics**
- Parâmetros: 1
- Linhas: 47
- Documentação: Sim

**collect_project_metrics**
- Parâmetros: 1
- Linhas: 59
- Documentação: Sim

**check_performance_thresholds**
- Parâmetros: 3
- Linhas: 56
- Documentação: Sim

**record_metrics**
- Parâmetros: 4
- Linhas: 21
- Documentação: Sim

**_cleanup_old_metrics**
- Parâmetros: 1
- Linhas: 14
- Documentação: Sim

**start_monitoring**
- Parâmetros: 1
- Linhas: 9
- Documentação: Sim

**stop_monitoring**
- Parâmetros: 1
- Linhas: 5
- Documentação: Sim

**_monitoring_loop**
- Parâmetros: 1
- Linhas: 26
- Documentação: Sim

**get_performance_report**
- Parâmetros: 1
- Linhas: 45
- Documentação: Sim

### Recomendações

1. **Documentação**: Adicione docstrings para todas as funções e classes
2. **Complexidade**: Considere refatorar funções muito complexas
3. **Testes**: Implemente testes unitários para todas as funções
4. **Type Hints**: Adicione type hints para melhorar a legibilidade

### Histórico de Versões

- **v1.0**: Documentação inicial gerada automaticamente
- **Data**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Agente**: Documentation Agent

