# Documentação Técnica - migrated_progress_tracker_agent

## Análise Estática

### Métricas de Código
- **Linhas de código**: 537
- **Complexidade ciclomática**: 38.00
- **Funções**: 17
- **Classes**: 1
- **Imports**: 4

### Análise de Complexidade
- **Nível**: Alto (Código complexo, considere refatoração)\n
### Estrutura de Dependências

#### Imports Externos
.AgentorchestratorModule, json, logging, re

#### Hierarquia de Classes
- ProgressTrackerAgent (sem herança)\n
### Análise de Funções

#### Funções Principais
**integrate_with_module**
- Parâmetros: 0
- Linhas: 3
- Documentação: Sim

**__init__**
- Parâmetros: 1
- Linhas: 20
- Documentação: Não

**load_configuration**
- Parâmetros: 1
- Linhas: 21
- Documentação: Sim

**calculate_current_metrics**
- Parâmetros: 1
- Linhas: 34
- Documentação: Sim

**calculate_general_progress**
- Parâmetros: 2
- Linhas: 24
- Documentação: Sim

**calculate_epics_progress**
- Parâmetros: 2
- Linhas: 13
- Documentação: Sim

**calculate_stories_progress**
- Parâmetros: 2
- Linhas: 16
- Documentação: Sim

**calculate_agents_progress**
- Parâmetros: 2
- Linhas: 16
- Documentação: Sim

**calculate_tasks_progress**
- Parâmetros: 2
- Linhas: 13
- Documentação: Sim

**calculate_roadmaps_progress**
- Parâmetros: 2
- Linhas: 16
- Documentação: Sim

**calculate_planejamentos_progress**
- Parâmetros: 2
- Linhas: 16
- Documentação: Sim

**calculate_velocity**
- Parâmetros: 1
- Linhas: 40
- Documentação: Sim

**calculate_trends**
- Parâmetros: 1
- Linhas: 52
- Documentação: Sim

**generate_alerts**
- Parâmetros: 2
- Linhas: 34
- Documentação: Sim

**save_metrics**
- Parâmetros: 2
- Linhas: 25
- Documentação: Sim

**generate_dashboard_report**
- Parâmetros: 1
- Linhas: 63
- Documentação: Sim

**run**
- Parâmetros: 1
- Linhas: 40
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

