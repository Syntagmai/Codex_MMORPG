# Documentação Técnica - migrated_pattern_analyzer

## Análise Estática

### Métricas de Código
- **Linhas de código**: 614
- **Complexidade ciclomática**: 62.00
- **Funções**: 25
- **Classes**: 3
- **Imports**: 6

### Análise de Complexidade
- **Nível**: Alto (Código complexo, considere refatoração)\n
### Estrutura de Dependências

#### Imports Externos
.SourceanalyzerModule, json, hashlib, datetime.datetime, datetime.timedelta, statistics

#### Hierarquia de Classes
- PatternMatch (sem herança)\n- PatternCluster (sem herança)\n- PatternAnalyzer (sem herança)\n
### Análise de Funções

#### Funções Principais
**integrate_with_module**
- Parâmetros: 0
- Linhas: 3
- Documentação: Sim

**__init__**
- Parâmetros: 2
- Linhas: 25
- Documentação: Não

**load_patterns**
- Parâmetros: 1
- Linhas: 5
- Documentação: Sim

**load_clusters**
- Parâmetros: 1
- Linhas: 5
- Documentação: Sim

**save_patterns**
- Parâmetros: 1
- Linhas: 3
- Documentação: Sim

**save_clusters**
- Parâmetros: 1
- Linhas: 3
- Documentação: Sim

**analyze_patterns**
- Parâmetros: 2
- Linhas: 36
- Documentação: Sim

**_extract_features**
- Parâmetros: 2
- Linhas: 34
- Documentação: Sim

**_identify_success_patterns**
- Parâmetros: 3
- Linhas: 40
- Documentação: Sim

**_identify_failure_patterns**
- Parâmetros: 3
- Linhas: 35
- Documentação: Sim

**_identify_optimization_patterns**
- Parâmetros: 3
- Linhas: 31
- Documentação: Sim

**_analyze_context_patterns**
- Parâmetros: 2
- Linhas: 26
- Documentação: Sim

**_analyze_agent_patterns**
- Parâmetros: 2
- Linhas: 23
- Documentação: Sim

**_analyze_workflow_patterns**
- Parâmetros: 2
- Linhas: 22
- Documentação: Sim

**_analyze_error_patterns**
- Parâmetros: 2
- Linhas: 23
- Documentação: Sim

**_extract_error_type**
- Parâmetros: 2
- Linhas: 15
- Documentação: Sim

**_create_pattern_clusters**
- Parâmetros: 2
- Linhas: 53
- Documentação: Sim

**_calculate_cluster_center**
- Parâmetros: 2
- Linhas: 24
- Documentação: Sim

**_calculate_pattern_scores**
- Parâmetros: 3
- Linhas: 19
- Documentação: Sim

**_generate_pattern_id**
- Parâmetros: 2
- Linhas: 5
- Documentação: Sim

**_save_learned_patterns**
- Parâmetros: 2
- Linhas: 19
- Documentação: Sim

**_limit_patterns_per_type**
- Parâmetros: 1
- Linhas: 14
- Documentação: Sim

**find_similar_patterns**
- Parâmetros: 3
- Linhas: 23
- Documentação: Sim

**_calculate_pattern_similarity**
- Parâmetros: 3
- Linhas: 11
- Documentação: Sim

**_get_matched_features**
- Parâmetros: 3
- Linhas: 5
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

