# migrated_auto_learning_system

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_auto_learning_system
- **Caminho**: wiki\update\modules\tools\git_automation\migrated_auto_learning_system.py
- **Linhas de código**: 456
- **Complexidade**: 31.00
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

**Parâmetros**: self, base_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 32

Sem documentação.

### create_directory_structure

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Cria estrutura de pastas necessária

### load_config

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Carrega configuração do sistema

### save_config

**Parâmetros**: self, config
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 4

Salva configuração do sistema

### start_learning_background

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Inicia thread de aprendizado em background

### stop_learning_background

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Para thread de aprendizado

### _learning_loop

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Loop principal de aprendizado em background

### _perform_learning_cycle

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Executa um ciclo completo de aprendizado

### _save_learning_results

**Parâmetros**: self, patterns, optimizations
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Salva resultados do aprendizado

### record_interaction

**Parâmetros**: self, interaction_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Registra uma nova interação no sistema

### _check_immediate_optimizations

**Parâmetros**: self, interaction_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Verifica otimizações que podem ser aplicadas imediatamente

### _find_similar_patterns

**Parâmetros**: self, interaction_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Encontra padrões similares à interação atual

### _calculate_context_similarity

**Parâmetros**: self, context, keywords
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Calcula similaridade entre contexto e palavras-chave

### get_learning_stats

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Retorna estatísticas do sistema de aprendizado

### get_recommendations

**Parâmetros**: self, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Retorna recomendações baseadas no contexto atual

### update_feedback

**Parâmetros**: self, interaction_id, feedback, score
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Atualiza feedback de uma interação

### _trigger_relearning

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Dispara relearning baseado em feedback negativo

### generate_learning_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Gera relatório completo do sistema de aprendizado

### _generate_system_recommendations

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Gera recomendações para melhorar o sistema

### shutdown

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Desliga o sistema de aprendizado

### _save_current_state

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Salva estado atual do sistema

### get_rule_recommendations

**Parâmetros**: self, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 2

Obtém recomendações de regras baseado no contexto

### apply_rule_optimizations

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Aplica otimizações de regras aprendidas

### analyze_rule_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 2

Analisa padrões de uso das regras

## Classes

### InteractionData

**Herança**: Nenhuma
**Atributos**: Nenhum
**Métodos**: 0
**Linhas**: 12

Dados de uma interação do sistema

### LearningPattern

**Herança**: Nenhuma
**Atributos**: Nenhum
**Métodos**: 0
**Linhas**: 11

Padrão aprendido pelo sistema

### AutoLearningSystem

**Herança**: Nenhuma
**Atributos**: directories, config_file, config_file, interactions, patterns, optimizations, timestamp, patterns_file, optimizations_file, similar_patterns, similar_patterns, context_text, context_words, keyword_set, intersection, union, recommendations, relevant_patterns, stats, pattern_analysis, performance_analysis, recommendations, avg_confidence, state, state_file, optimizations, applied_optimizations, default_config, context_similarity, recent_optimizations, optimization, success
**Métodos**: 24
**Linhas**: 375

Sistema principal de auto aprendizado BMAD

#### __init__

**Parâmetros**: self, base_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 32

Sem documentação.

#### create_directory_structure

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Cria estrutura de pastas necessária

#### load_config

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Carrega configuração do sistema

#### save_config

**Parâmetros**: self, config
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 4

Salva configuração do sistema

#### start_learning_background

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Inicia thread de aprendizado em background

#### stop_learning_background

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Para thread de aprendizado

#### _learning_loop

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Loop principal de aprendizado em background

#### _perform_learning_cycle

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Executa um ciclo completo de aprendizado

#### _save_learning_results

**Parâmetros**: self, patterns, optimizations
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Salva resultados do aprendizado

#### record_interaction

**Parâmetros**: self, interaction_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Registra uma nova interação no sistema

#### _check_immediate_optimizations

**Parâmetros**: self, interaction_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Verifica otimizações que podem ser aplicadas imediatamente

#### _find_similar_patterns

**Parâmetros**: self, interaction_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Encontra padrões similares à interação atual

#### _calculate_context_similarity

**Parâmetros**: self, context, keywords
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Calcula similaridade entre contexto e palavras-chave

#### get_learning_stats

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Retorna estatísticas do sistema de aprendizado

#### get_recommendations

**Parâmetros**: self, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Retorna recomendações baseadas no contexto atual

#### update_feedback

**Parâmetros**: self, interaction_id, feedback, score
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Atualiza feedback de uma interação

#### _trigger_relearning

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Dispara relearning baseado em feedback negativo

#### generate_learning_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Gera relatório completo do sistema de aprendizado

#### _generate_system_recommendations

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Gera recomendações para melhorar o sistema

#### shutdown

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Desliga o sistema de aprendizado

#### _save_current_state

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Salva estado atual do sistema

#### get_rule_recommendations

**Parâmetros**: self, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 2

Obtém recomendações de regras baseado no contexto

#### apply_rule_optimizations

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Aplica otimizações de regras aprendidas

#### analyze_rule_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 2

Analisa padrões de uso das regras

## Imports

.GitautomationModule, json, time, threading, datetime.datetime, datetime.timedelta, statistics

## Uso

```python
# Exemplo de uso do módulo migrated_auto_learning_system
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:52
