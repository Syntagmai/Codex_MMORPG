# Documentação Técnica - migrated_script_execution_manager

## Análise Estática

### Métricas de Código
- **Linhas de código**: 374
- **Complexidade ciclomática**: 30.00
- **Funções**: 12
- **Classes**: 1
- **Imports**: 6

### Análise de Complexidade
- **Nível**: Alto (Código complexo, considere refatoração)\n
### Estrutura de Dependências

#### Imports Externos
.ScriptexecutorModule, json, subprocess, sys, time, datetime.datetime

#### Hierarquia de Classes
- ScriptExecutionManager (sem herança)\n
### Análise de Funções

#### Funções Principais
**main**
- Parâmetros: 0
- Linhas: 27
- Documentação: Sim

**integrate_with_module**
- Parâmetros: 0
- Linhas: 3
- Documentação: Sim

**__init__**
- Parâmetros: 1
- Linhas: 11
- Documentação: Não

**execute_script_with_error_resolution**
- Parâmetros: 3
- Linhas: 64
- Documentação: Sim

**resolve_script_error**
- Parâmetros: 3
- Linhas: 20
- Documentação: Sim

**execute_script_safely**
- Parâmetros: 3
- Linhas: 11
- Documentação: Sim

**execute_fallback_mode**
- Parâmetros: 3
- Linhas: 21
- Documentação: Sim

**create_basic_map_update**
- Parâmetros: 2
- Linhas: 48
- Documentação: Sim

**create_basic_analysis_report**
- Parâmetros: 2
- Linhas: 28
- Documentação: Sim

**create_basic_report**
- Parâmetros: 2
- Linhas: 22
- Documentação: Sim

**log_execution**
- Parâmetros: 2
- Linhas: 25
- Documentação: Sim

**get_execution_stats**
- Parâmetros: 1
- Linhas: 24
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

