# Documentação Técnica - git_task_integration

## Análise Estática

### Métricas de Código
- **Linhas de código**: 655
- **Complexidade ciclomática**: 82.00
- **Funções**: 23
- **Classes**: 1
- **Imports**: 14

### Análise de Complexidade
- **Nível**: Alto (Código complexo, considere refatoração)\n
### Estrutura de Dependências

#### Imports Externos
os, sys, json, logging, subprocess, re, pathlib.Path, typing.Dict, typing.Any, typing.Optional, typing.List, datetime.datetime, git_automation_agent.GitAutomationAgent, argparse

#### Hierarquia de Classes
- GitTaskIntegration (sem herança)\n
### Análise de Funções

#### Funções Principais
**main**
- Parâmetros: 0
- Linhas: 43
- Documentação: Sim

**__init__**
- Parâmetros: 1
- Linhas: 7
- Documentação: Sim

**resolve_git_errors_automatically**
- Parâmetros: 1
- Linhas: 48
- Documentação: Sim

**is_git_repo**
- Parâmetros: 1
- Linhas: 7
- Documentação: Sim

**initialize_git_repo**
- Parâmetros: 1
- Linhas: 8
- Documentação: Sim

**get_untracked_files**
- Parâmetros: 1
- Linhas: 12
- Documentação: Sim

**get_modified_files**
- Parâmetros: 1
- Linhas: 12
- Documentação: Sim

**get_deleted_files**
- Parâmetros: 1
- Linhas: 12
- Documentação: Sim

**add_untracked_files_automatically**
- Parâmetros: 2
- Linhas: 9
- Documentação: Sim

**add_modified_files_automatically**
- Parâmetros: 2
- Linhas: 9
- Documentação: Sim

**remove_deleted_files_automatically**
- Parâmetros: 2
- Linhas: 9
- Documentação: Sim

**has_merge_conflicts**
- Parâmetros: 1
- Linhas: 7
- Documentação: Sim

**resolve_merge_conflicts_automatically**
- Parâmetros: 1
- Linhas: 10
- Documentação: Sim

**is_staging_area_empty**
- Parâmetros: 1
- Linhas: 7
- Documentação: Sim

**add_changed_files_automatically**
- Parâmetros: 1
- Linhas: 8
- Documentação: Sim

**analyze_changes_by_context**
- Parâmetros: 1
- Linhas: 48
- Documentação: Sim

**create_atomic_commits**
- Parâmetros: 3
- Linhas: 62
- Documentação: Sim

**generate_contextual_commit_message**
- Parâmetros: 4
- Linhas: 46
- Documentação: Sim

**extract_commit_hash**
- Parâmetros: 2
- Linhas: 11
- Documentação: Sim

**get_active_task**
- Parâmetros: 1
- Linhas: 51
- Documentação: Sim

**auto_commit_atomic**
- Parâmetros: 2
- Linhas: 60
- Documentação: Sim

**auto_push**
- Parâmetros: 1
- Linhas: 24
- Documentação: Sim

**generate_commit_report**
- Parâmetros: 4
- Linhas: 46
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

