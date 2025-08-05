# migrated_prompt_optimizer

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_prompt_optimizer
- **Caminho**: wiki\update\modules\tools\git_automation\migrated_prompt_optimizer.py
- **Linhas de código**: 448
- **Complexidade**: 34.00
- **Funções**: 22
- **Classes**: 2

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
**Linhas**: 5

Sem documentação.

### _load_optimization_templates

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 51

Carrega templates de otimização

### _load_detection_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Carrega padrões de detecção

### optimize_prompt

**Parâmetros**: self, prompt, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 58

Otimiza um prompt usando múltiplas técnicas

### _detect_task_type

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Detecta tipo de tarefa do prompt

### _needs_role_prompting

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Verifica se prompt precisa de role prompting

### _needs_clarity_improvement

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Verifica se prompt precisa de melhoria de clareza

### _needs_chain_of_thought

**Parâmetros**: self, prompt, task_type
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Verifica se prompt precisa de chain-of-thought

### _needs_specificity_improvement

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Verifica se prompt precisa de melhoria de especificidade

### _needs_structured_output

**Parâmetros**: self, prompt, task_type
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Verifica se prompt precisa de saída estruturada

### _apply_role_prompting

**Parâmetros**: self, prompt, task_type, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Aplica role prompting

### _improve_clarity

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Melhora clareza do prompt

### _apply_chain_of_thought

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Aplica chain-of-thought

### _improve_specificity

**Parâmetros**: self, prompt, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Melhora especificidade do prompt

### _add_structured_output

**Parâmetros**: self, prompt, task_type
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Adiciona estrutura de saída

### _extract_technology

**Parâmetros**: self, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Extrai tecnologia do contexto

### _extract_subject

**Parâmetros**: self, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Extrai assunto do contexto

### _extract_domain

**Parâmetros**: self, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Extrai domínio do contexto

### _calculate_improvement_score

**Parâmetros**: self, original, optimized
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Calcula score de melhoria

### batch_optimize

**Parâmetros**: self, prompts, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Otimiza múltiplos prompts

### get_optimization_stats

**Parâmetros**: self, results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Retorna estatísticas de otimização

## Classes

### OptimizationResult

**Herança**: Nenhuma
**Atributos**: Nenhum
**Métodos**: 0
**Linhas**: 7

Resultado de uma otimização de prompt

### PromptOptimizer

**Herança**: Nenhuma
**Atributos**: original_prompt, optimized_prompt, applied_techniques, changes_made, reasoning, task_type, improvement_score, prompt_lower, role_indicators, has_role, has_ambiguous, sentences, long_sentences, complex_keywords, has_complex, generic_phrases, is_generic, has_context, structured_tasks, replacements, improved, improved, context_info, improved, original_words, optimized_words, word_ratio, has_structure, structure_bonus, has_specific, specific_bonus, base_score, total_score, results, techniques_used, optimized_prompt, optimized_prompt, optimized_prompt, optimized_prompt, optimized_prompt, technology, years, template, improved, format_structure, result, subject, template, format_structure, format_structure, domain, template, template
**Métodos**: 21
**Linhas**: 395

Otimizador especializado de prompts

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Sem documentação.

#### _load_optimization_templates

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 51

Carrega templates de otimização

#### _load_detection_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Carrega padrões de detecção

#### optimize_prompt

**Parâmetros**: self, prompt, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 58

Otimiza um prompt usando múltiplas técnicas

#### _detect_task_type

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Detecta tipo de tarefa do prompt

#### _needs_role_prompting

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Verifica se prompt precisa de role prompting

#### _needs_clarity_improvement

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Verifica se prompt precisa de melhoria de clareza

#### _needs_chain_of_thought

**Parâmetros**: self, prompt, task_type
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Verifica se prompt precisa de chain-of-thought

#### _needs_specificity_improvement

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Verifica se prompt precisa de melhoria de especificidade

#### _needs_structured_output

**Parâmetros**: self, prompt, task_type
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Verifica se prompt precisa de saída estruturada

#### _apply_role_prompting

**Parâmetros**: self, prompt, task_type, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Aplica role prompting

#### _improve_clarity

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Melhora clareza do prompt

#### _apply_chain_of_thought

**Parâmetros**: self, prompt
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Aplica chain-of-thought

#### _improve_specificity

**Parâmetros**: self, prompt, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Melhora especificidade do prompt

#### _add_structured_output

**Parâmetros**: self, prompt, task_type
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Adiciona estrutura de saída

#### _extract_technology

**Parâmetros**: self, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Extrai tecnologia do contexto

#### _extract_subject

**Parâmetros**: self, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Extrai assunto do contexto

#### _extract_domain

**Parâmetros**: self, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Extrai domínio do contexto

#### _calculate_improvement_score

**Parâmetros**: self, original, optimized
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Calcula score de melhoria

#### batch_optimize

**Parâmetros**: self, prompts, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Otimiza múltiplos prompts

#### get_optimization_stats

**Parâmetros**: self, results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Retorna estatísticas de otimização

## Imports

.GitautomationModule, re

## Uso

```python
# Exemplo de uso do módulo migrated_prompt_optimizer
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

