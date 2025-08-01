# migrated_script_execution_manager

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_script_execution_manager
- **Caminho**: wiki\update\modules\python\script_executor\migrated_script_execution_manager.py
- **Linhas de código**: 374
- **Complexidade**: 30.00
- **Funções**: 12
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Função principal

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
**Linhas**: 11

Sem documentação.

### execute_script_with_error_resolution

**Parâmetros**: self, script_path, args
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 64

Executa script Python com resolução automática de erros

### resolve_script_error

**Parâmetros**: self, script_path, error_message
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Resolve erro em script usando o resolver automático

### execute_script_safely

**Parâmetros**: self, script_path, args
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Executa script de forma segura com fallback

### execute_fallback_mode

**Parâmetros**: self, script_path, args
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Executa script em modo fallback (simplificado)

### create_basic_map_update

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 48

Cria atualização básica de mapas

### create_basic_analysis_report

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Cria relatório básico de análise

### create_basic_report

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Cria relatório básico genérico

### log_execution

**Parâmetros**: self, execution_result
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Registra resultado da execução

### get_execution_stats

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Obtém estatísticas de execução

## Classes

### ScriptExecutionManager

**Herança**: Nenhuma
**Atributos**: execution_result, result, log_file, executions, log_file, args, start_time, cmd, result, script_name, script_name, report_file, basic_report, script_name, report_file, basic_report, executions, total, successful, success_rate, cmd, result, execution_time, map_file, basic_data, executions, map_file, basic_data, map_file, basic_data, executions, executions
**Métodos**: 10
**Linhas**: 293

Sem documentação.

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Sem documentação.

#### execute_script_with_error_resolution

**Parâmetros**: self, script_path, args
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 64

Executa script Python com resolução automática de erros

#### resolve_script_error

**Parâmetros**: self, script_path, error_message
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Resolve erro em script usando o resolver automático

#### execute_script_safely

**Parâmetros**: self, script_path, args
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Executa script de forma segura com fallback

#### execute_fallback_mode

**Parâmetros**: self, script_path, args
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Executa script em modo fallback (simplificado)

#### create_basic_map_update

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 48

Cria atualização básica de mapas

#### create_basic_analysis_report

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Cria relatório básico de análise

#### create_basic_report

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Cria relatório básico genérico

#### log_execution

**Parâmetros**: self, execution_result
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Registra resultado da execução

#### get_execution_stats

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Obtém estatísticas de execução

## Imports

.ScriptexecutorModule, json, subprocess, sys, time, datetime.datetime

## Uso

```python
# Exemplo de uso do módulo migrated_script_execution_manager
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:53
