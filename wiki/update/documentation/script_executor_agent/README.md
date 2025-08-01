# script_executor_agent

## Descrição

Script Executor Agent - Sistema Inteligente de Execução de Scripts Python

Este agente implementa um sistema inteligente para execução automática de scripts Python
com análise de dependências, validação, monitoramento e tratamento de erros.

## Informações Técnicas

- **Módulo**: script_executor_agent
- **Caminho**: wiki\update\script_executor_agent.py
- **Linhas de código**: 431
- **Complexidade**: 36.00
- **Funções**: 16
- **Classes**: 5

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Função principal

### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 1

Sem documentação.

### analyze_script

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 61

Analisa um script Python e retorna suas informações

### _calculate_complexity

**Parâmetros**: self, tree
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Calcula complexidade ciclomática simples

### _validate_script

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Valida se um script Python é sintaticamente correto

### __init__

**Parâmetros**: self, base_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 4

Sem documentação.

### execute_script

**Parâmetros**: self, script_path, args, timeout, capture_output
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 57

Executa um script Python com análise e monitoramento

### _run_script

**Parâmetros**: self, script_path, args, timeout, capture_output
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 51

Executa um script Python usando subprocess

### _check_dependencies

**Parâmetros**: self, dependencies
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Verifica se as dependências estão disponíveis

### execute_batch

**Parâmetros**: self, scripts, parallel, max_workers
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Executa múltiplos scripts em lote

### _execute_parallel

**Parâmetros**: self, scripts, max_workers
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Executa scripts em paralelo

### get_execution_history

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 2

Retorna o histórico de execuções

### get_statistics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Retorna estatísticas das execuções

### __init__

**Parâmetros**: self, base_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Sem documentação.

### execute_task_12_8

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 39

Executa a Task 12.8: Implementar executor inteligente de scripts

### _find_test_scripts

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Encontra scripts para testar o executor

## Classes

### ExecutionResult

**Herança**: Nenhuma
**Atributos**: Nenhum
**Métodos**: 0
**Linhas**: 11

Resultado da execução de um script

### ScriptInfo

**Herança**: Nenhuma
**Atributos**: Nenhum
**Métodos**: 0
**Linhas**: 11

Informações sobre um script Python

### DependencyAnalyzer

**Herança**: Nenhuma
**Atributos**: complexity, tree, imports, functions, classes, complexity, is_valid, stat, last_modified, content, content, module
**Métodos**: 4
**Linhas**: 85

Analisador de dependências de scripts Python

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 1

Sem documentação.

#### analyze_script

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 61

Analisa um script Python e retorna suas informações

#### _calculate_complexity

**Parâmetros**: self, tree
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Calcula complexidade ciclomática simples

#### _validate_script

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Valida se um script Python é sintaticamente correto

### ScriptExecutor

**Herança**: Nenhuma
**Atributos**: script_path, script_info, missing_deps, start_time, result, execution_time, execution_result, cmd, missing, results, total_executions, successful_executions, failed_executions, total_time, avg_time, results, future_to_script, process, process, module_name, module_name, result, result
**Métodos**: 8
**Linhas**: 192

Executor inteligente de scripts Python

#### __init__

**Parâmetros**: self, base_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 4

Sem documentação.

#### execute_script

**Parâmetros**: self, script_path, args, timeout, capture_output
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 57

Executa um script Python com análise e monitoramento

#### _run_script

**Parâmetros**: self, script_path, args, timeout, capture_output
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 51

Executa um script Python usando subprocess

#### _check_dependencies

**Parâmetros**: self, dependencies
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Verifica se as dependências estão disponíveis

#### execute_batch

**Parâmetros**: self, scripts, parallel, max_workers
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Executa múltiplos scripts em lote

#### _execute_parallel

**Parâmetros**: self, scripts, max_workers
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Executa scripts em paralelo

#### get_execution_history

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 2

Retorna o histórico de execuções

#### get_statistics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Retorna estatísticas das execuções

### ScriptExecutorAgent

**Herança**: Nenhuma
**Atributos**: test_scripts, results, stats, report, report_path, test_scripts, search_paths, result, path
**Métodos**: 3
**Linhas**: 70

Agente principal para execução inteligente de scripts

#### __init__

**Parâmetros**: self, base_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Sem documentação.

#### execute_task_12_8

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 39

Executa a Task 12.8: Implementar executor inteligente de scripts

#### _find_test_scripts

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Encontra scripts para testar o executor

## Imports

os, sys, subprocess, importlib, ast, logging, json, time, threading, pathlib.Path, typing.Dict, typing.List, typing.Optional, typing.Tuple, typing.Any, dataclasses.dataclass, dataclasses.asdict, datetime.datetime, traceback, concurrent.futures

## Uso

```python
# Exemplo de uso do módulo script_executor_agent
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:52
