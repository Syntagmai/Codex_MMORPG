# Documentação Técnica - migrated_git_automation_agent

## Análise Estática

### Métricas de Código
- **Linhas de código**: 1200
- **Complexidade ciclomática**: 156.00
- **Funções**: 27
- **Classes**: 1
- **Imports**: 8

### Análise de Complexidade
- **Nível**: Alto (Código complexo, considere refatoração)\n
### Estrutura de Dependências

#### Imports Externos
.AgentorchestratorModule, subprocess, re, logging, datetime.datetime, sys, argparse, difflib

#### Hierarquia de Classes
- GitAutomationAgentFixed (sem herança)\n
### Análise de Funções

#### Funções Principais
**main**
- Parâmetros: 0
- Linhas: 127
- Documentação: Sim

**integrate_with_module**
- Parâmetros: 0
- Linhas: 3
- Documentação: Sim

**__init__**
- Parâmetros: 2
- Linhas: 45
- Documentação: Sim

**validate_file_exists**
- Parâmetros: 2
- Linhas: 15
- Documentação: Sim

**safe_add_file**
- Parâmetros: 2
- Linhas: 33
- Documentação: Sim

**analyze_changes**
- Parâmetros: 1
- Linhas: 70
- Documentação: Sim

**_detect_task_context**
- Parâmetros: 1
- Linhas: 30
- Documentação: Sim

**_detect_open_files**
- Parâmetros: 1
- Linhas: 25
- Documentação: Sim

**_analyze_commit_groups**
- Parâmetros: 2
- Linhas: 52
- Documentação: Sim

**_group_by_directory**
- Parâmetros: 2
- Linhas: 24
- Documentação: Sim

**_group_by_file_type**
- Parâmetros: 2
- Linhas: 24
- Documentação: Sim

**_group_by_context**
- Parâmetros: 2
- Linhas: 30
- Documentação: Sim

**_get_file_diff**
- Parâmetros: 2
- Linhas: 18
- Documentação: Sim

**_extract_context_from_diff**
- Parâmetros: 2
- Linhas: 24
- Documentação: Sim

**_is_similar_context**
- Parâmetros: 3
- Linhas: 16
- Documentação: Sim

**_consolidate_groups**
- Parâmetros: 2
- Linhas: 30
- Documentação: Sim

**_ensure_unique_files**
- Parâmetros: 3
- Linhas: 31
- Documentação: Sim

**_get_file_type**
- Parâmetros: 2
- Linhas: 36
- Documentação: Sim

**_determine_type_from_files**
- Parâmetros: 2
- Linhas: 24
- Documentação: Sim

**_generate_group_message**
- Parâmetros: 3
- Linhas: 32
- Documentação: Sim

**_determine_commit_type**
- Parâmetros: 2
- Linhas: 38
- Documentação: Sim

**_generate_change_summary**
- Parâmetros: 2
- Linhas: 30
- Documentação: Sim

**generate_commit_message**
- Parâmetros: 2
- Linhas: 67
- Documentação: Sim

**validate_commit_message**
- Parâmetros: 2
- Linhas: 74
- Documentação: Sim

**execute_commit**
- Parâmetros: 3
- Linhas: 94
- Documentação: Sim

**auto_commit**
- Parâmetros: 2
- Linhas: 29
- Documentação: Sim

**execute_multiple_commits**
- Parâmetros: 3
- Linhas: 41
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

