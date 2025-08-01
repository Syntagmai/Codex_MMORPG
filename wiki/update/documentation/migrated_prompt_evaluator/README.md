# migrated_prompt_evaluator

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_prompt_evaluator
- **Caminho**: wiki\update\modules\tools\git_automation\migrated_prompt_evaluator.py
- **Linhas de código**: 531
- **Complexidade**: 46.00
- **Funções**: 18
- **Classes**: 3

## Funções

### integrate_with_module

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Integra o script com o módulo de destino.

### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Sem documentação.

### _load_evaluation_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 49

Carrega padrões de avaliação

### evaluate_prompt

**Parâmetros**: self, prompt, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 64

Avalia um prompt completo

### _calculate_clarity_score

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Calcula score de clareza

### _calculate_specificity_score

**Parâmetros**: self, prompt, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Calcula score de especificidade

### _calculate_completeness_score

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Calcula score de completude

### _calculate_structure_score

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Calcula score de estrutura

### _calculate_context_score

**Parâmetros**: self, prompt, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Calcula score de contexto

### _calculate_overall_score

**Parâmetros**: self, scores
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Calcula score geral ponderado

### _generate_suggestions

**Parâmetros**: self, scores
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Gera sugestões baseadas nos scores

### _create_detailed_analysis

**Parâmetros**: self, prompt, metrics
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 37

Cria análise detalhada do prompt

### _generate_recommendations

**Parâmetros**: self, metrics, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Gera recomendações específicas

### _calculate_evaluation_confidence

**Parâmetros**: self, metrics
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Calcula confiança da avaliação

### _generate_prompt_id

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 4

Gera ID único para o prompt

### batch_evaluate

**Parâmetros**: self, prompts, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Avalia múltiplos prompts

### get_evaluation_stats

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Retorna estatísticas de avaliação

### _calculate_improvement_trend

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Calcula tendência de melhoria

## Classes

### PromptMetrics

**Herança**: Nenhuma
**Atributos**: Nenhum
**Métodos**: 0
**Linhas**: 10

Métricas de avaliação de prompt

### EvaluationResult

**Herança**: Nenhuma
**Atributos**: Nenhum
**Métodos**: 0
**Linhas**: 5

Resultado completo de avaliação

### PromptEvaluator

**Herança**: Nenhuma
**Atributos**: clarity_score, specificity_score, completeness_score, structure_score, context_score, overall_score, suggestions, prompt_id, metrics, detailed_analysis, recommendations, confidence, score, sentences, avg_sentence_length, positive_count, negative_count, score, specific_count, generic_count, score, complete_count, incomplete_count, instruction_count, score, structure_count, no_structure_count, score, context_count, no_context_count, overall, suggestions, recommendations, scores, variance, confidence, results, recent_evaluations, scores, recent_scores, first_half, second_half, avg_first, avg_second, context_mentions, tech_list, result, tech_mentions
**Métodos**: 17
**Linhas**: 464

Avaliador especializado de prompts

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Sem documentação.

#### _load_evaluation_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 49

Carrega padrões de avaliação

#### evaluate_prompt

**Parâmetros**: self, prompt, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 64

Avalia um prompt completo

#### _calculate_clarity_score

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Calcula score de clareza

#### _calculate_specificity_score

**Parâmetros**: self, prompt, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Calcula score de especificidade

#### _calculate_completeness_score

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Calcula score de completude

#### _calculate_structure_score

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Calcula score de estrutura

#### _calculate_context_score

**Parâmetros**: self, prompt, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Calcula score de contexto

#### _calculate_overall_score

**Parâmetros**: self, scores
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Calcula score geral ponderado

#### _generate_suggestions

**Parâmetros**: self, scores
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Gera sugestões baseadas nos scores

#### _create_detailed_analysis

**Parâmetros**: self, prompt, metrics
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 37

Cria análise detalhada do prompt

#### _generate_recommendations

**Parâmetros**: self, metrics, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Gera recomendações específicas

#### _calculate_evaluation_confidence

**Parâmetros**: self, metrics
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Calcula confiança da avaliação

#### _generate_prompt_id

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 4

Gera ID único para o prompt

#### batch_evaluate

**Parâmetros**: self, prompts, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Avalia múltiplos prompts

#### get_evaluation_stats

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Retorna estatísticas de avaliação

#### _calculate_improvement_trend

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Calcula tendência de melhoria

## Imports

.GitautomationModule, re, statistics, datetime.datetime, hashlib

## Uso

```python
# Exemplo de uso do módulo migrated_prompt_evaluator
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:52
