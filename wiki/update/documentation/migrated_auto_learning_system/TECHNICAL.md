# Documentação Técnica - migrated_auto_learning_system

## Análise Estática

### Métricas de Código
- **Linhas de código**: 456
- **Complexidade ciclomática**: 31.00
- **Funções**: 25
- **Classes**: 3
- **Imports**: 7

### Análise de Complexidade
- **Nível**: Alto (Código complexo, considere refatoração)\n
### Estrutura de Dependências

#### Imports Externos
.GitautomationModule, json, time, threading, datetime.datetime, datetime.timedelta, statistics

#### Hierarquia de Classes
- InteractionData (sem herança)\n- LearningPattern (sem herança)\n- AutoLearningSystem (sem herança)\n
### Análise de Funções

#### Funções Principais
**integrate_with_module**
- Parâmetros: 0
- Linhas: 3
- Documentação: Sim

**__init__**
- Parâmetros: 2
- Linhas: 32
- Documentação: Não

**create_directory_structure**
- Parâmetros: 1
- Linhas: 11
- Documentação: Sim

**load_config**
- Parâmetros: 1
- Linhas: 18
- Documentação: Sim

**save_config**
- Parâmetros: 2
- Linhas: 4
- Documentação: Sim

**start_learning_background**
- Parâmetros: 1
- Linhas: 6
- Documentação: Sim

**stop_learning_background**
- Parâmetros: 1
- Linhas: 5
- Documentação: Sim

**_learning_loop**
- Parâmetros: 1
- Linhas: 13
- Documentação: Sim

**_perform_learning_cycle**
- Parâmetros: 1
- Linhas: 22
- Documentação: Sim

**_save_learning_results**
- Parâmetros: 3
- Linhas: 19
- Documentação: Sim

**record_interaction**
- Parâmetros: 2
- Linhas: 20
- Documentação: Sim

**_check_immediate_optimizations**
- Parâmetros: 2
- Linhas: 10
- Documentação: Sim

**_find_similar_patterns**
- Parâmetros: 2
- Linhas: 15
- Documentação: Sim

**_calculate_context_similarity**
- Parâmetros: 3
- Linhas: 17
- Documentação: Sim

**get_learning_stats**
- Parâmetros: 1
- Linhas: 9
- Documentação: Sim

**get_recommendations**
- Parâmetros: 2
- Linhas: 26
- Documentação: Sim

**update_feedback**
- Parâmetros: 4
- Linhas: 6
- Documentação: Sim

**_trigger_relearning**
- Parâmetros: 1
- Linhas: 6
- Documentação: Sim

**generate_learning_report**
- Parâmetros: 1
- Linhas: 30
- Documentação: Sim

**_generate_system_recommendations**
- Parâmetros: 1
- Linhas: 16
- Documentação: Sim

**shutdown**
- Parâmetros: 1
- Linhas: 10
- Documentação: Sim

**_save_current_state**
- Parâmetros: 1
- Linhas: 11
- Documentação: Sim

**get_rule_recommendations**
- Parâmetros: 2
- Linhas: 2
- Documentação: Sim

**apply_rule_optimizations**
- Parâmetros: 1
- Linhas: 16
- Documentação: Sim

**analyze_rule_patterns**
- Parâmetros: 1
- Linhas: 2
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

