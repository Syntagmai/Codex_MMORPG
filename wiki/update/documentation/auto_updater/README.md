# auto_updater

## Descrição

Sistema de Auto-Atualização Inteligente BMAD
Atualiza automaticamente o sistema baseado em mudanças detectadas

## Informações Técnicas

- **Módulo**: auto_updater
- **Caminho**: wiki\update\auto_updater.py
- **Linhas de código**: 720
- **Complexidade**: 82.00
- **Funções**: 25
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Função principal

### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Sem documentação.

### setup_logging

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Configura sistema de logging

### trigger_auto_update

**Parâmetros**: self, change_type, details
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 37

Dispara atualização automática baseada no tipo de mudança

### update_maps

**Parâmetros**: self, details
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 49

Atualiza mapas JSON automaticamente

### update_rules

**Parâmetros**: self, details
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Atualiza regras automaticamente

### update_scripts

**Parâmetros**: self, details
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Atualiza scripts automaticamente

### update_context

**Parâmetros**: self, details
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Atualiza contexto automaticamente

### update_performance

**Parâmetros**: self, details
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Atualiza performance automaticamente

### validate_maps

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 35

Valida mapas após atualização

### scan_rules_consistency

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 32

Escaneia consistência das regras

### resolve_rule_conflicts

**Parâmetros**: self, issues
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Resolve conflitos de regras

### optimize_rule_structure

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 52

Otimiza estrutura de regras

### optimize_script_performance

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Otimiza performance dos scripts

### fix_script_errors

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Corrige erros nos scripts

### update_script_dependencies

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 57

Atualiza dependências dos scripts

### detect_context_changes

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Detecta mudanças de contexto

### update_context_maps

**Parâmetros**: self, changes
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Atualiza mapas de contexto

### optimize_navigation_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Otimiza padrões de navegação

### apply_performance_optimizations

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Aplica otimizações de performance baseadas na análise

### apply_cache_optimizations

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Aplica otimizações de cache

### apply_search_optimizations

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Aplica otimizações de busca

### apply_structure_optimizations

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Aplica otimizações de estrutura

### save_update_history

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Salva histórico de atualizações

### get_update_stats

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Retorna estatísticas de atualização

## Classes

### AutoUpdater

**Herança**: Nenhuma
**Atributos**: log_file, issues, resolved_count, improvements, fixes, updates, changes, optimizations, map_update_scripts, success_count, validation_success, success_rate, consistency_issues, performance_improvements, error_fixes, dependency_updates, context_changes, performance_script, maps_to_validate, valid_maps, validation_rate, cursor_file, rules_optimized, total_rules, common_imports, context_files, context_script, nav_script, report_file, history_file, total_updates, successful_updates, success_rate, start_time, success, execution_time, update_record, script_path, resolved_issues, optimization_success, context_update_success, navigation_optimization, result, map_path, rule_references, context_path, result, result, score, optimizations_applied, content, rule_name, rule_path, result, missing_imports, mtime, report, result, rule_name, rule_path, basic_rule_content, content, expanded_content, content, content, lines, import_section, other_lines, new_content, data, improved_content, improved_content
**Métodos**: 24
**Linhas**: 677

Sem documentação.

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Sem documentação.

#### setup_logging

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Configura sistema de logging

#### trigger_auto_update

**Parâmetros**: self, change_type, details
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 37

Dispara atualização automática baseada no tipo de mudança

#### update_maps

**Parâmetros**: self, details
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 49

Atualiza mapas JSON automaticamente

#### update_rules

**Parâmetros**: self, details
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Atualiza regras automaticamente

#### update_scripts

**Parâmetros**: self, details
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Atualiza scripts automaticamente

#### update_context

**Parâmetros**: self, details
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Atualiza contexto automaticamente

#### update_performance

**Parâmetros**: self, details
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Atualiza performance automaticamente

#### validate_maps

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 35

Valida mapas após atualização

#### scan_rules_consistency

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 32

Escaneia consistência das regras

#### resolve_rule_conflicts

**Parâmetros**: self, issues
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Resolve conflitos de regras

#### optimize_rule_structure

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 52

Otimiza estrutura de regras

#### optimize_script_performance

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Otimiza performance dos scripts

#### fix_script_errors

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Corrige erros nos scripts

#### update_script_dependencies

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 57

Atualiza dependências dos scripts

#### detect_context_changes

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Detecta mudanças de contexto

#### update_context_maps

**Parâmetros**: self, changes
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Atualiza mapas de contexto

#### optimize_navigation_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Otimiza padrões de navegação

#### apply_performance_optimizations

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Aplica otimizações de performance baseadas na análise

#### apply_cache_optimizations

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Aplica otimizações de cache

#### apply_search_optimizations

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Aplica otimizações de busca

#### apply_structure_optimizations

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Aplica otimizações de estrutura

#### save_update_history

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Salva histórico de atualizações

#### get_update_stats

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Retorna estatísticas de atualização

## Imports

json, time, subprocess, sys, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any, typing.Optional, logging

## Uso

```python
# Exemplo de uso do módulo auto_updater
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:50
