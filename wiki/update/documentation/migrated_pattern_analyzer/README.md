# migrated_pattern_analyzer

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_pattern_analyzer
- **Caminho**: wiki\update\modules\analysis\source_analyzer\migrated_pattern_analyzer.py
- **Linhas de código**: 614
- **Complexidade**: 62.00
- **Funções**: 25
- **Classes**: 3

## Funções

### integrate_with_module

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Integra o script com o módulo de destino.

### __init__

**Parâmetros**: self, models_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Sem documentação.

### load_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Carrega padrões aprendidos do arquivo

### load_clusters

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Carrega clusters de padrões do arquivo

### save_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Salva padrões aprendidos no arquivo

### save_clusters

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Salva clusters de padrões no arquivo

### analyze_patterns

**Parâmetros**: self, interactions
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Analisa interações e identifica padrões

### _extract_features

**Parâmetros**: self, interactions
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Extrai características das interações

### _identify_success_patterns

**Parâmetros**: self, interactions, features
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 40

Identifica padrões de sucesso

### _identify_failure_patterns

**Parâmetros**: self, interactions, features
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 35

Identifica padrões de falha

### _identify_optimization_patterns

**Parâmetros**: self, interactions, features
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Identifica padrões de otimização

### _analyze_context_patterns

**Parâmetros**: self, interactions
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Analisa padrões de contexto

### _analyze_agent_patterns

**Parâmetros**: self, interactions
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Analisa padrões de combinação de agentes

### _analyze_workflow_patterns

**Parâmetros**: self, interactions
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Analisa padrões de workflow

### _analyze_error_patterns

**Parâmetros**: self, interactions
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Analisa padrões de erro

### _extract_error_type

**Parâmetros**: self, error_message
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Extrai tipo de erro da mensagem

### _create_pattern_clusters

**Parâmetros**: self, patterns
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 53

Cria clusters de padrões similares

### _calculate_cluster_center

**Parâmetros**: self, patterns
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Calcula o centro de um cluster de padrões

### _calculate_pattern_scores

**Parâmetros**: self, patterns, clusters
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Calcula scores de confiança para padrões

### _generate_pattern_id

**Parâmetros**: self, pattern_type
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Gera ID único para um padrão

### _save_learned_patterns

**Parâmetros**: self, patterns
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Salva padrões aprendidos

### _limit_patterns_per_type

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Limita número de padrões por tipo

### find_similar_patterns

**Parâmetros**: self, context, pattern_type
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Encontra padrões similares ao contexto atual

### _calculate_pattern_similarity

**Parâmetros**: self, context, pattern
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Calcula similaridade entre contexto e padrão

### _get_matched_features

**Parâmetros**: self, context, pattern
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Retorna características que deram match

## Classes

### PatternMatch

**Herança**: Nenhuma
**Atributos**: Nenhum
**Métodos**: 0
**Linhas**: 5

Match de um padrão em uma interação

### PatternCluster

**Herança**: Nenhuma
**Atributos**: Nenhum
**Métodos**: 0
**Linhas**: 7

Cluster de padrões similares

### PatternAnalyzer

**Herança**: Nenhuma
**Atributos**: features, success_patterns, failure_patterns, optimization_patterns, all_patterns, clusters, patterns_with_scores, filtered_patterns, features, success_patterns, successful_interactions, context_patterns, agent_patterns, workflow_patterns, failure_patterns, failed_interactions, error_patterns, failure_context_patterns, optimization_patterns, optimized_interactions, optimization_context_patterns, context_patterns, context_groups, agent_patterns, agent_combinations, workflow_patterns, workflow_groups, error_patterns, error_groups, error_message, pattern_texts, avg_success_rate, avg_execution_time, all_keywords, pattern_types, most_common_type, content, matches, pattern_keywords, context_keys, intersection, union, pattern_keywords, context_keys, text, context_keys, perf_features, pattern, context_keys, agent_combo, text, tfidf_matrix, clustering, clusters, success_score, usage_score, cluster_score, pattern_id, type_patterns, similarity, pattern, success_scores, execution_times, pattern, success_scores, pattern, success_scores, pattern, error_type, pattern, cluster_indices, cluster_patterns, clusters, existing, patterns_to_remove, match, pattern, center_pattern, cluster, cluster_score
**Métodos**: 24
**Linhas**: 548

Analisador de padrões para identificação de aprendizados

#### __init__

**Parâmetros**: self, models_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Sem documentação.

#### load_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Carrega padrões aprendidos do arquivo

#### load_clusters

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Carrega clusters de padrões do arquivo

#### save_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Salva padrões aprendidos no arquivo

#### save_clusters

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Salva clusters de padrões no arquivo

#### analyze_patterns

**Parâmetros**: self, interactions
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Analisa interações e identifica padrões

#### _extract_features

**Parâmetros**: self, interactions
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Extrai características das interações

#### _identify_success_patterns

**Parâmetros**: self, interactions, features
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 40

Identifica padrões de sucesso

#### _identify_failure_patterns

**Parâmetros**: self, interactions, features
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 35

Identifica padrões de falha

#### _identify_optimization_patterns

**Parâmetros**: self, interactions, features
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Identifica padrões de otimização

#### _analyze_context_patterns

**Parâmetros**: self, interactions
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Analisa padrões de contexto

#### _analyze_agent_patterns

**Parâmetros**: self, interactions
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Analisa padrões de combinação de agentes

#### _analyze_workflow_patterns

**Parâmetros**: self, interactions
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Analisa padrões de workflow

#### _analyze_error_patterns

**Parâmetros**: self, interactions
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Analisa padrões de erro

#### _extract_error_type

**Parâmetros**: self, error_message
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Extrai tipo de erro da mensagem

#### _create_pattern_clusters

**Parâmetros**: self, patterns
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 53

Cria clusters de padrões similares

#### _calculate_cluster_center

**Parâmetros**: self, patterns
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Calcula o centro de um cluster de padrões

#### _calculate_pattern_scores

**Parâmetros**: self, patterns, clusters
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Calcula scores de confiança para padrões

#### _generate_pattern_id

**Parâmetros**: self, pattern_type
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Gera ID único para um padrão

#### _save_learned_patterns

**Parâmetros**: self, patterns
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Salva padrões aprendidos

#### _limit_patterns_per_type

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Limita número de padrões por tipo

#### find_similar_patterns

**Parâmetros**: self, context, pattern_type
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Encontra padrões similares ao contexto atual

#### _calculate_pattern_similarity

**Parâmetros**: self, context, pattern
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Calcula similaridade entre contexto e padrão

#### _get_matched_features

**Parâmetros**: self, context, pattern
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Retorna características que deram match

## Imports

.SourceanalyzerModule, json, hashlib, datetime.datetime, datetime.timedelta, statistics

## Uso

```python
# Exemplo de uso do módulo migrated_pattern_analyzer
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:58
