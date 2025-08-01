# recipe_manager_agent

## Descrição

Recipe Manager Agent - Sistema de Receitas Python

Este agente implementa um sistema de receitas para tarefas Python comuns,
permitindo criar, gerenciar e executar receitas reutilizáveis.

## Informações Técnicas

- **Módulo**: recipe_manager_agent
- **Caminho**: wiki\update\recipe_manager_agent.py
- **Linhas de código**: 570
- **Complexidade**: 45.00
- **Funções**: 23
- **Classes**: 5

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Função principal

### __init__

**Parâmetros**: self, recipes_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Sem documentação.

### load_recipes

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Carrega todas as receitas do diretório

### _dict_to_recipe

**Parâmetros**: self, data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Converte dicionário para objeto Recipe

### _recipe_to_dict

**Parâmetros**: self, recipe
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Converte objeto Recipe para dicionário

### create_recipe

**Parâmetros**: self, recipe
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Cria uma nova receita

### get_recipe

**Parâmetros**: self, name
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 2

Obtém uma receita pelo nome

### list_recipes

**Parâmetros**: self, category
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 4

Lista todas as receitas, opcionalmente filtradas por categoria

### execute_recipe

**Parâmetros**: self, name, args
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 79

Executa uma receita

### _execute_step

**Parâmetros**: self, step, args
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Executa um passo da receita

### _execute_python_script

**Parâmetros**: self, script_args, recipe_args
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Executa um script Python

### _execute_shell_command

**Parâmetros**: self, command_args, recipe_args
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Executa um comando shell

### _execute_copy_operation

**Parâmetros**: self, copy_args, recipe_args
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Executa operação de cópia

### _execute_create_operation

**Parâmetros**: self, create_args, recipe_args
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Executa operação de criação

### _substitute_variables

**Parâmetros**: self, text, args
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Substitui variáveis no texto

### _evaluate_condition

**Parâmetros**: self, condition, args
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Avalia uma condição

### _check_dependencies

**Parâmetros**: self, dependencies
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Verifica se as dependências estão disponíveis

### _save_recipe

**Parâmetros**: self, recipe
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Salva uma receita no arquivo

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
**Linhas**: 19

Retorna estatísticas das receitas

### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Sem documentação.

### execute_task_12_9

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 40

Executa a Task 12.9: Criar sistema de receitas Python

### _create_sample_recipes

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 98

Cria receitas de exemplo

## Classes

### RecipeStep

**Herança**: Nenhuma
**Atributos**: Nenhum
**Métodos**: 0
**Linhas**: 9

Passo de uma receita

### Recipe

**Herança**: Nenhuma
**Atributos**: Nenhum
**Métodos**: 0
**Linhas**: 13

Receita Python

### RecipeExecution

**Herança**: Nenhuma
**Atributos**: Nenhum
**Métodos**: 0
**Linhas**: 10

Resultado da execução de uma receita

### RecipeManager

**Herança**: Nenhuma
**Atributos**: steps, recipe, start_time, steps_executed, steps_failed, output_lines, error_lines, missing_deps, execution_time, success, execution, script_path, script_args, script_args, cmd, result, command, command, result, source, destination, path, path_obj, missing, total_recipes, total_executions, avg_success_rate, categories, step, recipe_file, step_success, placeholder, text, condition, recipe_file, path, data, recipe, step_output, step_success, path
**Métodos**: 19
**Linhas**: 327

Gerenciador de receitas Python

#### __init__

**Parâmetros**: self, recipes_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Sem documentação.

#### load_recipes

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Carrega todas as receitas do diretório

#### _dict_to_recipe

**Parâmetros**: self, data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Converte dicionário para objeto Recipe

#### _recipe_to_dict

**Parâmetros**: self, recipe
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Converte objeto Recipe para dicionário

#### create_recipe

**Parâmetros**: self, recipe
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Cria uma nova receita

#### get_recipe

**Parâmetros**: self, name
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 2

Obtém uma receita pelo nome

#### list_recipes

**Parâmetros**: self, category
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 4

Lista todas as receitas, opcionalmente filtradas por categoria

#### execute_recipe

**Parâmetros**: self, name, args
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 79

Executa uma receita

#### _execute_step

**Parâmetros**: self, step, args
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Executa um passo da receita

#### _execute_python_script

**Parâmetros**: self, script_args, recipe_args
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Executa um script Python

#### _execute_shell_command

**Parâmetros**: self, command_args, recipe_args
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Executa um comando shell

#### _execute_copy_operation

**Parâmetros**: self, copy_args, recipe_args
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Executa operação de cópia

#### _execute_create_operation

**Parâmetros**: self, create_args, recipe_args
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Executa operação de criação

#### _substitute_variables

**Parâmetros**: self, text, args
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Substitui variáveis no texto

#### _evaluate_condition

**Parâmetros**: self, condition, args
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Avalia uma condição

#### _check_dependencies

**Parâmetros**: self, dependencies
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Verifica se as dependências estão disponíveis

#### _save_recipe

**Parâmetros**: self, recipe
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Salva uma receita no arquivo

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
**Linhas**: 19

Retorna estatísticas das receitas

### RecipeManagerAgent

**Herança**: Nenhuma
**Atributos**: recipes_created, executions, stats, report, report_path, recipes, validator_recipe, analyzer_recipe, backup_recipe, created_count, execution
**Métodos**: 3
**Linhas**: 148

Agente principal para gerenciamento de receitas

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Sem documentação.

#### execute_task_12_9

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 40

Executa a Task 12.9: Criar sistema de receitas Python

#### _create_sample_recipes

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 98

Cria receitas de exemplo

## Imports

os, sys, json, logging, subprocess, time, pathlib.Path, typing.Dict, typing.List, typing.Optional, typing.Any, typing.Union, dataclasses.dataclass, dataclasses.asdict, datetime.datetime, traceback, shutil, re

## Uso

```python
# Exemplo de uso do módulo recipe_manager_agent
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:51
