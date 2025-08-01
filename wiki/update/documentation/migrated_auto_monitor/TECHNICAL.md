# Documentação Técnica - migrated_auto_monitor

## Análise Estática

### Métricas de Código
- **Linhas de código**: 589
- **Complexidade ciclomática**: 69.00
- **Funções**: 24
- **Classes**: 1
- **Imports**: 11

### Análise de Complexidade
- **Nível**: Alto (Código complexo, considere refatoração)\n
### Estrutura de Dependências

#### Imports Externos
.AgentmonitorModule, json, time, os, subprocess, sys, datetime.datetime, datetime.timedelta, threading, logging, psutil

#### Hierarquia de Classes
- AutoMonitor (sem herança)\n
### Análise de Funções

#### Funções Principais
**main**
- Parâmetros: 0
- Linhas: 24
- Documentação: Sim

**integrate_with_module**
- Parâmetros: 0
- Linhas: 3
- Documentação: Sim

**__init__**
- Parâmetros: 1
- Linhas: 28
- Documentação: Não

**setup_logging**
- Parâmetros: 1
- Linhas: 13
- Documentação: Sim

**start_monitoring**
- Parâmetros: 1
- Linhas: 28
- Documentação: Sim

**check_system_health**
- Parâmetros: 1
- Linhas: 20
- Documentação: Sim

**check_maps_integrity**
- Parâmetros: 1
- Linhas: 27
- Documentação: Sim

**check_rules_consistency**
- Parâmetros: 1
- Linhas: 26
- Documentação: Sim

**check_scripts_functionality**
- Parâmetros: 1
- Linhas: 34
- Documentação: Sim

**check_file_permissions**
- Parâmetros: 1
- Linhas: 21
- Documentação: Sim

**check_json_validity**
- Parâmetros: 1
- Linhas: 18
- Documentação: Sim

**detect_changes**
- Parâmetros: 1
- Linhas: 38
- Documentação: Sim

**analyze_performance**
- Parâmetros: 1
- Linhas: 19
- Documentação: Sim

**measure_response_time**
- Parâmetros: 1
- Linhas: 23
- Documentação: Sim

**measure_memory_usage**
- Parâmetros: 1
- Linhas: 21
- Documentação: Sim

**measure_file_access_speed**
- Parâmetros: 1
- Linhas: 31
- Documentação: Sim

**measure_script_execution_time**
- Parâmetros: 1
- Linhas: 31
- Documentação: Sim

**check_and_trigger_actions**
- Parâmetros: 1
- Linhas: 27
- Documentação: Sim

**trigger_health_correction**
- Parâmetros: 1
- Linhas: 9
- Documentação: Sim

**trigger_performance_optimization**
- Parâmetros: 1
- Linhas: 9
- Documentação: Sim

**trigger_auto_update**
- Parâmetros: 1
- Linhas: 9
- Documentação: Sim

**trigger_emergency_mode**
- Parâmetros: 1
- Linhas: 14
- Documentação: Sim

**save_system_state**
- Parâmetros: 1
- Linhas: 10
- Documentação: Sim

**get_system_status**
- Parâmetros: 1
- Linhas: 9
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

