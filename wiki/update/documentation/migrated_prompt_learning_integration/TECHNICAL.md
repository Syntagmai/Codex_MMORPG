# Documentação Técnica - migrated_prompt_learning_integration

## Análise Estática

### Métricas de Código
- **Linhas de código**: 487
- **Complexidade ciclomática**: 50.00
- **Funções**: 22
- **Classes**: 3
- **Imports**: 6

### Análise de Complexidade
- **Nível**: Alto (Código complexo, considere refatoração)\n
### Estrutura de Dependências

#### Imports Externos
.GitautomationModule, json, hashlib, datetime.datetime, datetime.timedelta, statistics

#### Hierarquia de Classes
- PromptLearningPattern (sem herança)\n- PromptOptimizationResult (sem herança)\n- PromptLearningIntegration (sem herança)\n
### Análise de Funções

#### Funções Principais
**integrate_with_module**
- Parâmetros: 0
- Linhas: 3
- Documentação: Sim

**__init__**
- Parâmetros: 2
- Linhas: 21
- Documentação: Não

**load_prompt_patterns**
- Parâmetros: 1
- Linhas: 5
- Documentação: Sim

**load_optimization_history**
- Parâmetros: 1
- Linhas: 5
- Documentação: Sim

**load_learning_log**
- Parâmetros: 1
- Linhas: 5
- Documentação: Sim

**save_prompt_patterns**
- Parâmetros: 1
- Linhas: 3
- Documentação: Sim

**save_optimization_history**
- Parâmetros: 1
- Linhas: 3
- Documentação: Sim

**save_learning_log**
- Parâmetros: 1
- Linhas: 3
- Documentação: Sim

**record_prompt_optimization**
- Parâmetros: 2
- Linhas: 34
- Documentação: Sim

**_update_prompt_patterns**
- Parâmetros: 2
- Linhas: 43
- Documentação: Sim

**_detect_prompt_type**
- Parâmetros: 2
- Linhas: 14
- Documentação: Sim

**get_optimization_recommendation**
- Parâmetros: 3
- Linhas: 39
- Documentação: Sim

**_calculate_context_relevance**
- Parâmetros: 3
- Linhas: 15
- Documentação: Sim

**analyze_optimization_effectiveness**
- Parâmetros: 1
- Linhas: 42
- Documentação: Sim

**get_learning_recommendations**
- Parâmetros: 1
- Linhas: 28
- Documentação: Sim

**generate_learning_report**
- Parâmetros: 1
- Linhas: 20
- Documentação: Sim

**_get_top_patterns**
- Parâmetros: 1
- Linhas: 19
- Documentação: Sim

**apply_learned_optimizations**
- Parâmetros: 3
- Linhas: 18
- Documentação: Sim

**_apply_role_prompting**
- Parâmetros: 3
- Linhas: 18
- Documentação: Sim

**_apply_chain_of_thought**
- Parâmetros: 2
- Linhas: 14
- Documentação: Sim

**_apply_specificity_improvement**
- Parâmetros: 3
- Linhas: 12
- Documentação: Sim

**_apply_clarity_enhancement**
- Parâmetros: 2
- Linhas: 13
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

