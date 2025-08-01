# migrated_feedback_system

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_feedback_system
- **Caminho**: wiki\update\modules\tools\git_automation\migrated_feedback_system.py
- **Linhas de código**: 455
- **Complexidade**: 41.00
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

**Parâmetros**: self, logs_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Sem documentação.

### load_feedback_data

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Carrega dados de feedback do arquivo

### load_feedback_analysis

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Carrega análises de feedback do arquivo

### save_feedback_data

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Salva dados de feedback no arquivo

### save_feedback_analysis

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Salva análises de feedback no arquivo

### record_feedback

**Parâmetros**: self, interaction_id, feedback_text, feedback_score, feedback_type, metadata
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Registra feedback de uma interação

### generate_feedback_id

**Parâmetros**: self, interaction_id, feedback_text, feedback_score
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Gera ID único para feedback

### analyze_feedback

**Parâmetros**: self, feedback_record
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Analisa feedback e extrai insights

### _analyze_sentiment

**Parâmetros**: self, feedback_text
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Analisa sentimento do feedback

### _extract_improvement_suggestions

**Parâmetros**: self, feedback_text
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Extrai sugestões de melhoria do feedback

### _calculate_confidence_level

**Parâmetros**: self, feedback_record
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Calcula nível de confiança do feedback

### get_feedback_stats

**Parâmetros**: self, days
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 56

Retorna estatísticas de feedback

### get_interaction_feedback

**Parâmetros**: self, interaction_id
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Retorna feedback de uma interação específica

### get_low_performing_interactions

**Parâmetros**: self, threshold, days
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Retorna interações com baixo desempenho

### get_improvement_recommendations

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 48

Gera recomendações de melhoria baseadas no feedback

### record_implicit_feedback

**Parâmetros**: self, interaction_id, success_score, execution_time, error_message
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Registra feedback implícito baseado no comportamento

### cleanup_old_feedback

**Parâmetros**: self, days_to_keep
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Remove feedback antigo

## Classes

### FeedbackRecord

**Herança**: Nenhuma
**Atributos**: Nenhum
**Métodos**: 0
**Linhas**: 8

Registro de feedback do usuário

### FeedbackAnalysis

**Herança**: Nenhuma
**Atributos**: Nenhum
**Métodos**: 0
**Linhas**: 6

Análise de feedback

### FeedbackSystem

**Herança**: Nenhuma
**Atributos**: feedback_score, feedback_id, feedback_record, analysis, content, sentiment_score, improvement_suggestions, confidence_level, overall_score, text_lower, positive_count, negative_count, total_words, positive_ratio, negative_ratio, sentiment_score, suggestions, suggestion_keywords, sentences, confidence, cutoff_date, recent_feedback, scores, avg_score, sentiment_scores, sentiment_distribution, feedback_types, all_suggestions, suggestion_counts, top_suggestions, feedback_records, analysis, cutoff_date, low_performing, recommendations, stats, feedback_text, feedback_score, feedback_score, cutoff_date, feedback_to_remove, analysis_to_remove, sentence_lower, top_suggestion, feedback_text, suggestions, suggestion, feedback_info
**Métodos**: 17
**Linhas**: 389

Sistema de coleta e análise de feedback

#### __init__

**Parâmetros**: self, logs_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Sem documentação.

#### load_feedback_data

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Carrega dados de feedback do arquivo

#### load_feedback_analysis

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Carrega análises de feedback do arquivo

#### save_feedback_data

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Salva dados de feedback no arquivo

#### save_feedback_analysis

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Salva análises de feedback no arquivo

#### record_feedback

**Parâmetros**: self, interaction_id, feedback_text, feedback_score, feedback_type, metadata
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Registra feedback de uma interação

#### generate_feedback_id

**Parâmetros**: self, interaction_id, feedback_text, feedback_score
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Gera ID único para feedback

#### analyze_feedback

**Parâmetros**: self, feedback_record
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Analisa feedback e extrai insights

#### _analyze_sentiment

**Parâmetros**: self, feedback_text
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Analisa sentimento do feedback

#### _extract_improvement_suggestions

**Parâmetros**: self, feedback_text
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Extrai sugestões de melhoria do feedback

#### _calculate_confidence_level

**Parâmetros**: self, feedback_record
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Calcula nível de confiança do feedback

#### get_feedback_stats

**Parâmetros**: self, days
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 56

Retorna estatísticas de feedback

#### get_interaction_feedback

**Parâmetros**: self, interaction_id
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Retorna feedback de uma interação específica

#### get_low_performing_interactions

**Parâmetros**: self, threshold, days
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Retorna interações com baixo desempenho

#### get_improvement_recommendations

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 48

Gera recomendações de melhoria baseadas no feedback

#### record_implicit_feedback

**Parâmetros**: self, interaction_id, success_score, execution_time, error_message
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Registra feedback implícito baseado no comportamento

#### cleanup_old_feedback

**Parâmetros**: self, days_to_keep
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Remove feedback antigo

## Imports

.GitautomationModule, json, hashlib, datetime.datetime, datetime.timedelta, statistics

## Uso

```python
# Exemplo de uso do módulo migrated_feedback_system
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:52
