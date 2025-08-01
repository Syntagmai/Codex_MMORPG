# Documentação Técnica - migrated_prompt_evaluator

## Análise Estática

### Métricas de Código
- **Linhas de código**: 531
- **Complexidade ciclomática**: 46.00
- **Funções**: 18
- **Classes**: 3
- **Imports**: 5

### Análise de Complexidade
- **Nível**: Alto (Código complexo, considere refatoração)\n
### Estrutura de Dependências

#### Imports Externos
.GitautomationModule, re, statistics, datetime.datetime, hashlib

#### Hierarquia de Classes
- PromptMetrics (sem herança)\n- EvaluationResult (sem herança)\n- PromptEvaluator (sem herança)\n
### Análise de Funções

#### Funções Principais
**integrate_with_module**
- Parâmetros: 0
- Linhas: 3
- Documentação: Sim

**__init__**
- Parâmetros: 1
- Linhas: 14
- Documentação: Não

**_load_evaluation_patterns**
- Parâmetros: 1
- Linhas: 49
- Documentação: Sim

**evaluate_prompt**
- Parâmetros: 3
- Linhas: 64
- Documentação: Sim

**_calculate_clarity_score**
- Parâmetros: 2
- Linhas: 27
- Documentação: Sim

**_calculate_specificity_score**
- Parâmetros: 3
- Linhas: 26
- Documentação: Sim

**_calculate_completeness_score**
- Parâmetros: 2
- Linhas: 26
- Documentação: Sim

**_calculate_structure_score**
- Parâmetros: 2
- Linhas: 23
- Documentação: Sim

**_calculate_context_score**
- Parâmetros: 3
- Linhas: 28
- Documentação: Sim

**_calculate_overall_score**
- Parâmetros: 2
- Linhas: 7
- Documentação: Sim

**_generate_suggestions**
- Parâmetros: 2
- Linhas: 23
- Documentação: Sim

**_create_detailed_analysis**
- Parâmetros: 3
- Linhas: 37
- Documentação: Sim

**_generate_recommendations**
- Parâmetros: 3
- Linhas: 30
- Documentação: Sim

**_calculate_evaluation_confidence**
- Parâmetros: 2
- Linhas: 16
- Documentação: Sim

**_generate_prompt_id**
- Parâmetros: 2
- Linhas: 4
- Documentação: Sim

**batch_evaluate**
- Parâmetros: 3
- Linhas: 8
- Documentação: Sim

**get_evaluation_stats**
- Parâmetros: 1
- Linhas: 26
- Documentação: Sim

**_calculate_improvement_trend**
- Parâmetros: 1
- Linhas: 21
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

