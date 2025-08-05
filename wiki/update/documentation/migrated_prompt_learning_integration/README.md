# migrated_prompt_learning_integration

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_prompt_learning_integration
- **Caminho**: wiki\update\modules\tools\git_automation\migrated_prompt_learning_integration.py
- **Linhas de código**: 487
- **Complexidade**: 50.00
- **Funções**: 22
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
**Linhas**: 21

Sem documentação.

### load_prompt_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Carrega padrões de prompt aprendidos

### load_optimization_history

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Carrega histórico de otimizações

### load_learning_log

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Carrega log de aprendizado

### save_prompt_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Salva padrões de prompt aprendidos

### save_optimization_history

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Salva histórico de otimizações

### save_learning_log

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Salva log de aprendizado

### record_prompt_optimization

**Parâmetros**: self, result
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Registra resultado de otimização de prompt

### _update_prompt_patterns

**Parâmetros**: self, result
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 43

Atualiza padrões de prompt baseado em resultado bem-sucedido

### _detect_prompt_type

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Detecta tipo de prompt

### get_optimization_recommendation

**Parâmetros**: self, prompt, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 39

Obtém recomendação de otimização baseada em padrões aprendidos

### _calculate_context_relevance

**Parâmetros**: self, pattern, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Calcula relevância de contexto para um padrão

### analyze_optimization_effectiveness

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 42

Analisa efetividade das otimizações

### get_learning_recommendations

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Gera recomendações baseadas no aprendizado

### generate_learning_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Gera relatório de aprendizado

### _get_top_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Retorna padrões mais bem-sucedidos

### apply_learned_optimizations

**Parâmetros**: self, prompt, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Aplica otimizações aprendidas a um prompt

### _apply_role_prompting

**Parâmetros**: self, prompt, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Aplica role prompting baseado em contexto

### _apply_chain_of_thought

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Aplica chain-of-thought

### _apply_specificity_improvement

**Parâmetros**: self, prompt, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Aplica melhoria de especificidade

### _apply_clarity_enhancement

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Aplica melhoria de clareza

## Classes

### PromptLearningPattern

**Herança**: Nenhuma
**Atributos**: Nenhum
**Métodos**: 0
**Linhas**: 9

Padrão aprendido sobre prompts

### PromptOptimizationResult

**Herança**: Nenhuma
**Atributos**: Nenhum
**Métodos**: 0
**Linhas**: 7

Resultado de otimização de prompt

### PromptLearningIntegration

**Herança**: Nenhuma
**Atributos**: optimization_id, prompt_type, pattern_id, prompt_lower, prompt_type, relevant_patterns, relevance_scores, technique_stats, technique_analysis, recent_optimizations, recommendations, analysis, best_technique, most_used, recent_avg, analysis, recommendations, patterns_list, recommendation, technique, role, context_info, pattern, context_applicability, best_pattern, technique, recent_avg, recent_avg, techs, context_relevance, role, role, role
**Métodos**: 21
**Linhas**: 417

Integração entre prompt engineering e auto-aprendizado

#### __init__

**Parâmetros**: self, base_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Sem documentação.

#### load_prompt_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Carrega padrões de prompt aprendidos

#### load_optimization_history

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Carrega histórico de otimizações

#### load_learning_log

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Carrega log de aprendizado

#### save_prompt_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Salva padrões de prompt aprendidos

#### save_optimization_history

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Salva histórico de otimizações

#### save_learning_log

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Salva log de aprendizado

#### record_prompt_optimization

**Parâmetros**: self, result
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Registra resultado de otimização de prompt

#### _update_prompt_patterns

**Parâmetros**: self, result
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 43

Atualiza padrões de prompt baseado em resultado bem-sucedido

#### _detect_prompt_type

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Detecta tipo de prompt

#### get_optimization_recommendation

**Parâmetros**: self, prompt, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 39

Obtém recomendação de otimização baseada em padrões aprendidos

#### _calculate_context_relevance

**Parâmetros**: self, pattern, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Calcula relevância de contexto para um padrão

#### analyze_optimization_effectiveness

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 42

Analisa efetividade das otimizações

#### get_learning_recommendations

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Gera recomendações baseadas no aprendizado

#### generate_learning_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Gera relatório de aprendizado

#### _get_top_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Retorna padrões mais bem-sucedidos

#### apply_learned_optimizations

**Parâmetros**: self, prompt, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Aplica otimizações aprendidas a um prompt

#### _apply_role_prompting

**Parâmetros**: self, prompt, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Aplica role prompting baseado em contexto

#### _apply_chain_of_thought

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Aplica chain-of-thought

#### _apply_specificity_improvement

**Parâmetros**: self, prompt, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Aplica melhoria de especificidade

#### _apply_clarity_enhancement

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Aplica melhoria de clareza

## Imports

.GitautomationModule, json, hashlib, datetime.datetime, datetime.timedelta, statistics

## Uso

```python
# Exemplo de uso do módulo migrated_prompt_learning_integration
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:53

## 🔗 **Links Automáticos**

> [!info] **Links Gerados Automaticamente**
> Estes links foram criados automaticamente pelo sistema de linkagem da categoria **Tools**

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]
- [[../maps/tools_index|Índice de Ferramentas]]
- [[../update/README|Scripts de Atualização]]

### **🧭 Navegação**
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]
- [[../maps/category_indices|Índices por Categoria]]
- [[../maps/relationships|Relacionamentos]]

### **📊 Métricas da Categoria**
- **Categoria**: Tools
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

