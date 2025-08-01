# aaa_integration_validator

## Descrição

Sistema de Validação de Integridade AAA
Valida compatibilidade entre sistema AAA e sistema existente

## Informações Técnicas

- **Módulo**: aaa_integration_validator
- **Caminho**: wiki\update\aaa_integration_validator.py
- **Linhas de código**: 641
- **Complexidade**: 74.00
- **Funções**: 12
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Função principal para teste do sistema de validação

### __init__

**Parâmetros**: self, base_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Sem documentação.

### validate_system_integrity

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 59

Valida integridade completa do sistema

### validate_agents

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 67

Valida agentes especializados

### validate_workflows

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 68

Valida workflows AAA

### validate_compatibility

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 67

Valida compatibilidade com sistema existente

### validate_performance

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 66

Valida performance do sistema

### validate_json_maps

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 63

Valida mapas JSON

### validate_rules

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 61

Valida regras do sistema

### calculate_overall_status

**Parâmetros**: self, validations
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Calcula status geral baseado em todas as validações

### save_validation_results

**Parâmetros**: self, results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Salva resultados da validação

### generate_validation_report

**Parâmetros**: self, results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 69

Gera relatório de validação em formato legível

## Classes

### AAAIntegrationValidator

**Herança**: Nenhuma
**Atributos**: start_time, validation_results, agent_validation, workflow_validation, compatibility_validation, performance_validation, json_validation, rules_validation, overall_status, total_time, agent_validation, agents_file, workflow_validation, agents_file, compatibility_validation, rules_path, maps_path, bmad_path, performance_validation, test_scenarios, total_score, total_scenarios, performance_score, json_validation, maps_path, json_files, rules_validation, rules_path, rule_files, status_scores, total_score, total_validations, average_score, timestamp, filename, filepath, report, validations, agents, aaa_workflows, existing_rules, aaa_rules, json_files, bmad_agents_file, bmad_files, start_time, execution_time, target_time, file_detail, rule_detail, status, score, status, status_emoji, issues, agents_data, agent_detail, required_fields, workflows, agents_data, workflow_detail, required_fields, agents, phases, data, content
**Métodos**: 11
**Linhas**: 594

Sistema de validação de integridade para sistema AAA

#### __init__

**Parâmetros**: self, base_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Sem documentação.

#### validate_system_integrity

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 59

Valida integridade completa do sistema

#### validate_agents

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 67

Valida agentes especializados

#### validate_workflows

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 68

Valida workflows AAA

#### validate_compatibility

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 67

Valida compatibilidade com sistema existente

#### validate_performance

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 66

Valida performance do sistema

#### validate_json_maps

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 63

Valida mapas JSON

#### validate_rules

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 61

Valida regras do sistema

#### calculate_overall_status

**Parâmetros**: self, validations
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Calcula status geral baseado em todas as validações

#### save_validation_results

**Parâmetros**: self, results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Salva resultados da validação

#### generate_validation_report

**Parâmetros**: self, results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 69

Gera relatório de validação em formato legível

## Imports

os, json, time, datetime.datetime, typing.Dict, typing.List, typing.Any, typing.Optional, typing.Tuple, pathlib.Path

## Uso

```python
# Exemplo de uso do módulo aaa_integration_validator
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:50
