# Documentação Técnica - script_migration_agent

## Análise Estática

### Métricas de Código
- **Linhas de código**: 451
- **Complexidade ciclomática**: 49.00
- **Funções**: 14
- **Classes**: 1
- **Imports**: 13

### Análise de Complexidade
- **Nível**: Alto (Código complexo, considere refatoração)\n
### Estrutura de Dependências

#### Imports Externos
os, json, shutil, ast, re, pathlib.Path, typing.Dict, typing.List, typing.Any, typing.Optional, typing.Tuple, datetime.datetime, logging

#### Hierarquia de Classes
- ScriptMigrationAgent (sem herança)\n
### Análise de Funções

#### Funções Principais
**main**
- Parâmetros: 0
- Linhas: 39
- Documentação: Sim

**__init__**
- Parâmetros: 1
- Linhas: 17
- Documentação: Não

**load_structure_config**
- Parâmetros: 1
- Linhas: 8
- Documentação: Sim

**load_script_mapping**
- Parâmetros: 1
- Linhas: 8
- Documentação: Sim

**discover_python_scripts**
- Parâmetros: 1
- Linhas: 19
- Documentação: Sim

**analyze_script**
- Parâmetros: 2
- Linhas: 68
- Documentação: Sim

**determine_target_module**
- Parâmetros: 2
- Linhas: 49
- Documentação: Sim

**migrate_script_to_module**
- Parâmetros: 3
- Linhas: 35
- Documentação: Sim

**create_migrated_script**
- Parâmetros: 4
- Linhas: 35
- Documentação: Sim

**update_module_init**
- Parâmetros: 4
- Linhas: 23
- Documentação: Sim

**update_module_config**
- Parâmetros: 4
- Linhas: 23
- Documentação: Sim

**migrate_all_scripts**
- Parâmetros: 1
- Linhas: 41
- Documentação: Sim

**generate_migration_report**
- Parâmetros: 1
- Linhas: 14
- Documentação: Sim

**save_migration_report**
- Parâmetros: 2
- Linhas: 8
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

