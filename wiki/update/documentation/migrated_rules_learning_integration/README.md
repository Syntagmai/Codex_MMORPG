# migrated_rules_learning_integration

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_rules_learning_integration
- **Caminho**: wiki\update\modules\tools\git_automation\migrated_rules_learning_integration.py
- **Linhas de código**: 468
- **Complexidade**: 48.00
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
**Linhas**: 27

Sem documentação.

### load_rule_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Carrega padrões de regras aprendidos

### load_rule_optimizations

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Carrega otimizações de regras

### load_rule_usage_log

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Carrega log de uso de regras

### save_rule_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Salva padrões de regras aprendidos

### save_rule_optimizations

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Salva otimizações de regras

### save_rule_usage_log

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Salva log de uso de regras

### get_all_rules

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Obtém todas as regras do sistema

### parse_rule_content

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Analisa conteúdo de uma regra

### record_rule_usage

**Parâmetros**: self, rule_file, context, success_score, feedback
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Registra uso de uma regra

### analyze_rule_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 37

Analisa padrões de uso das regras

### _analyze_context_applicability

**Parâmetros**: self, usages
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Analisa aplicabilidade da regra em diferentes contextos

### _extract_context_keywords

**Parâmetros**: self, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Extrai palavras-chave do contexto

### _generate_rule_improvements

**Parâmetros**: self, rule_file, usages
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Gera sugestões de melhoria para uma regra

### generate_rule_optimizations

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Gera otimizações para regras baseado em padrões aprendidos

### _create_rule_optimization

**Parâmetros**: self, pattern
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Cria otimização para uma regra específica

### _generate_improved_content

**Parâmetros**: self, current_content, suggestions
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Gera conteúdo melhorado baseado em sugestões

### apply_rule_optimization

**Parâmetros**: self, optimization
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 39

Aplica uma otimização de regra

### get_rule_recommendations

**Parâmetros**: self, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Obtém recomendações de regras baseado no contexto

### _calculate_context_relevance

**Parâmetros**: self, pattern, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Calcula relevância de uma regra para o contexto atual

### generate_rules_learning_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Gera relatório de aprendizado das regras

## Classes

### RuleLearningPattern

**Herança**: Nenhuma
**Atributos**: Nenhum
**Métodos**: 0
**Linhas**: 10

Padrão aprendido sobre regras

### RuleOptimization

**Herança**: Nenhuma
**Atributos**: Nenhum
**Métodos**: 0
**Linhas**: 8

Otimização sugerida para uma regra

### RulesLearningIntegration

**Herança**: Nenhuma
**Atributos**: rules, sections, current_section, current_content, usage_entry, patterns, rule_usage, context_scores, applicability, keywords, suggestions, negative_feedback, context_applicability, low_applicability, optimizations, patterns, improved_content, recommendations, patterns, context_keywords, overlap_score, patterns, report, success_scores, avg_success, context_applicability, suggestions, pattern, context, score, keywords, request_words, rule_content, sections, suggestions, optimization, rule_file_path, backup_path, relevance_score, current_section, current_content, optimization, current_content, recommendation, content, rule_file_path
**Métodos**: 21
**Linhas**: 395

Sistema de integração entre auto-aprendizado e regras

#### __init__

**Parâmetros**: self, base_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Sem documentação.

#### load_rule_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Carrega padrões de regras aprendidos

#### load_rule_optimizations

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Carrega otimizações de regras

#### load_rule_usage_log

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Carrega log de uso de regras

#### save_rule_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Salva padrões de regras aprendidos

#### save_rule_optimizations

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Salva otimizações de regras

#### save_rule_usage_log

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Salva log de uso de regras

#### get_all_rules

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Obtém todas as regras do sistema

#### parse_rule_content

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Analisa conteúdo de uma regra

#### record_rule_usage

**Parâmetros**: self, rule_file, context, success_score, feedback
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Registra uso de uma regra

#### analyze_rule_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 37

Analisa padrões de uso das regras

#### _analyze_context_applicability

**Parâmetros**: self, usages
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Analisa aplicabilidade da regra em diferentes contextos

#### _extract_context_keywords

**Parâmetros**: self, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Extrai palavras-chave do contexto

#### _generate_rule_improvements

**Parâmetros**: self, rule_file, usages
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Gera sugestões de melhoria para uma regra

#### generate_rule_optimizations

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Gera otimizações para regras baseado em padrões aprendidos

#### _create_rule_optimization

**Parâmetros**: self, pattern
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Cria otimização para uma regra específica

#### _generate_improved_content

**Parâmetros**: self, current_content, suggestions
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Gera conteúdo melhorado baseado em sugestões

#### apply_rule_optimization

**Parâmetros**: self, optimization
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 39

Aplica uma otimização de regra

#### get_rule_recommendations

**Parâmetros**: self, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Obtém recomendações de regras baseado no contexto

#### _calculate_context_relevance

**Parâmetros**: self, pattern, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Calcula relevância de uma regra para o contexto atual

#### generate_rules_learning_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Gera relatório de aprendizado das regras

## Imports

.GitautomationModule, json, re, hashlib, datetime.datetime, datetime.timedelta, statistics

## Uso

```python
# Exemplo de uso do módulo migrated_rules_learning_integration
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

