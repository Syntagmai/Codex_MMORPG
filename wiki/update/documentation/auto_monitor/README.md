# auto_monitor

## Descrição

Sistema de Auto-Monitoramento Contínuo BMAD
Monitora continuamente o estado do sistema e dispara ações automáticas

## Informações Técnicas

- **Módulo**: auto_monitor
- **Caminho**: wiki\update\auto_monitor.py
- **Linhas de código**: 556
- **Complexidade**: 67.00
- **Funções**: 23
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Função principal

### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Sem documentação.

### setup_logging

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Configura sistema de logging

### start_monitoring

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Inicia monitoramento contínuo

### check_system_health

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Verifica saúde geral do sistema

### check_maps_integrity

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Verifica integridade dos mapas JSON

### check_rules_consistency

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Verifica consistência das regras

### check_scripts_functionality

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Verifica funcionalidade dos scripts Python

### check_file_permissions

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Verifica permissões de arquivos

### check_json_validity

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Verifica validade de arquivos JSON

### detect_changes

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Detecta mudanças no sistema

### analyze_performance

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Analisa performance do sistema

### measure_response_time

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Mede tempo de resposta do sistema

### measure_memory_usage

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Mede uso de memória

### measure_file_access_speed

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Mede velocidade de acesso a arquivos

### measure_script_execution_time

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Mede tempo de execução de scripts

### check_and_trigger_actions

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Verifica se ações automáticas são necessárias

### trigger_health_correction

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Dispara correção de saúde do sistema

### trigger_performance_optimization

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Dispara otimização de performance

### trigger_auto_update

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Dispara atualização automática

### trigger_emergency_mode

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Ativa modo de emergência

### save_system_state

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Salva estado atual do sistema

### get_system_status

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Retorna status atual do sistema

## Classes

### AutoMonitor

**Herança**: Nenhuma
**Atributos**: log_file, health_checks, health_score, current_time, changes, performance_metrics, performance_score, actions_triggered, emergency_state, emergency_file, maps_to_check, valid_maps, rules_to_check, valid_rules, scripts_to_check, valid_scripts, critical_paths, accessible_paths, json_files, valid_jsons, start_time, response_time, memory_percent, start_time, test_files, access_time, start_time, test_script, correction_script, optimization_script, update_script, state_file, map_path, rule_path, script_path, result, execution_time, file_key, current_mtime, result
**Métodos**: 22
**Linhas**: 508

Sem documentação.

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Sem documentação.

#### setup_logging

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Configura sistema de logging

#### start_monitoring

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Inicia monitoramento contínuo

#### check_system_health

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Verifica saúde geral do sistema

#### check_maps_integrity

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Verifica integridade dos mapas JSON

#### check_rules_consistency

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Verifica consistência das regras

#### check_scripts_functionality

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Verifica funcionalidade dos scripts Python

#### check_file_permissions

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Verifica permissões de arquivos

#### check_json_validity

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Verifica validade de arquivos JSON

#### detect_changes

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Detecta mudanças no sistema

#### analyze_performance

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Analisa performance do sistema

#### measure_response_time

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Mede tempo de resposta do sistema

#### measure_memory_usage

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Mede uso de memória

#### measure_file_access_speed

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Mede velocidade de acesso a arquivos

#### measure_script_execution_time

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Mede tempo de execução de scripts

#### check_and_trigger_actions

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Verifica se ações automáticas são necessárias

#### trigger_health_correction

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Dispara correção de saúde do sistema

#### trigger_performance_optimization

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Dispara otimização de performance

#### trigger_auto_update

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Dispara atualização automática

#### trigger_emergency_mode

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Ativa modo de emergência

#### save_system_state

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Salva estado atual do sistema

#### get_system_status

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Retorna status atual do sistema

## Imports

json, time, os, subprocess, sys, datetime.datetime, datetime.timedelta, pathlib.Path, typing.Dict, typing.List, typing.Any, typing.Optional, threading, logging, psutil

## Uso

```python
# Exemplo de uso do módulo auto_monitor
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:50
