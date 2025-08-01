# Documentação Técnica - recipe_manager_agent

## Análise Estática

### Métricas de Código
- **Linhas de código**: 570
- **Complexidade ciclomática**: 45.00
- **Funções**: 23
- **Classes**: 5
- **Imports**: 18

### Análise de Complexidade
- **Nível**: Alto (Código complexo, considere refatoração)\n
### Estrutura de Dependências

#### Imports Externos
os, sys, json, logging, subprocess, time, pathlib.Path, typing.Dict, typing.List, typing.Optional, typing.Any, typing.Union, dataclasses.dataclass, dataclasses.asdict, datetime.datetime, traceback, shutil, re

#### Hierarquia de Classes
- RecipeStep (sem herança)\n- Recipe (sem herança)\n- RecipeExecution (sem herança)\n- RecipeManager (sem herança)\n- RecipeManagerAgent (sem herança)\n
### Análise de Funções

#### Funções Principais
**main**
- Parâmetros: 0
- Linhas: 17
- Documentação: Sim

**__init__**
- Parâmetros: 2
- Linhas: 5
- Documentação: Não

**load_recipes**
- Parâmetros: 1
- Linhas: 10
- Documentação: Sim

**_dict_to_recipe**
- Parâmetros: 2
- Linhas: 29
- Documentação: Sim

**_recipe_to_dict**
- Parâmetros: 2
- Linhas: 15
- Documentação: Sim

**create_recipe**
- Parâmetros: 2
- Linhas: 12
- Documentação: Sim

**get_recipe**
- Parâmetros: 2
- Linhas: 2
- Documentação: Sim

**list_recipes**
- Parâmetros: 2
- Linhas: 4
- Documentação: Sim

**execute_recipe**
- Parâmetros: 3
- Linhas: 79
- Documentação: Sim

**_execute_step**
- Parâmetros: 3
- Linhas: 11
- Documentação: Sim

**_execute_python_script**
- Parâmetros: 3
- Linhas: 17
- Documentação: Sim

**_execute_shell_command**
- Parâmetros: 3
- Linhas: 13
- Documentação: Sim

**_execute_copy_operation**
- Parâmetros: 3
- Linhas: 15
- Documentação: Sim

**_execute_create_operation**
- Parâmetros: 3
- Linhas: 14
- Documentação: Sim

**_substitute_variables**
- Parâmetros: 3
- Linhas: 9
- Documentação: Sim

**_evaluate_condition**
- Parâmetros: 3
- Linhas: 17
- Documentação: Sim

**_check_dependencies**
- Parâmetros: 2
- Linhas: 8
- Documentação: Sim

**_save_recipe**
- Parâmetros: 2
- Linhas: 7
- Documentação: Sim

**get_execution_history**
- Parâmetros: 1
- Linhas: 2
- Documentação: Sim

**get_statistics**
- Parâmetros: 1
- Linhas: 19
- Documentação: Sim

**__init__**
- Parâmetros: 1
- Linhas: 3
- Documentação: Não

**execute_task_12_9**
- Parâmetros: 1
- Linhas: 40
- Documentação: Sim

**_create_sample_recipes**
- Parâmetros: 1
- Linhas: 98
- Documentação: Sim

### Recomendações

1. **Documentação**: Adicione docstrings para todas as funções e classes
2. **Complexidade**: Considere refatorar funções muito complexas
3. **Testes**: Implemente testes unitários para todas as funções
4. **Type Hints**: Adicione type hints para melhorar a legibilidade

### Histórico de Versões

- **v1.0**: Documentação inicial gerada automaticamente
- **Data**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Agente**: Documentation Agent

