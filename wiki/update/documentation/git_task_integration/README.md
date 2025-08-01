# git_task_integration

## Descrição

Integração Git + Sistema de Tarefas - Sistema Automático e Atômico
==================================================================

Script que integra o agente de automação Git com o sistema de tarefas BMAD,
permitindo commits automáticos durante o desenvolvimento com contexto de tarefa.
IMPLEMENTAÇÃO AUTOMÁTICA E ATÔMICA - NUNCA MANUAL!

Autor: Sistema BMAD - OTClient Documentation
Data: 2024-12-19
Versão: 2.0 - Automático e Atômico

## Informações Técnicas

- **Módulo**: git_task_integration
- **Caminho**: wiki\update\git_task_integration.py
- **Linhas de código**: 655
- **Complexidade**: 82.00
- **Funções**: 23
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 43

Função principal.

### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Inicializa a integração.

### resolve_git_errors_automatically

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 48

Resolve erros Git automaticamente sem intervenção manual.

Returns:
    True se todos os erros foram resolvidos

### is_git_repo

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Verifica se é um repositório Git.

### initialize_git_repo

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Inicializa repositório Git automaticamente.

### get_untracked_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Obtém lista de arquivos não rastreados.

### get_modified_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Obtém lista de arquivos modificados.

### get_deleted_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Obtém lista de arquivos deletados.

### add_untracked_files_automatically

**Parâmetros**: self, files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Adiciona arquivos não rastreados automaticamente.

### add_modified_files_automatically

**Parâmetros**: self, files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Adiciona arquivos modificados automaticamente.

### remove_deleted_files_automatically

**Parâmetros**: self, files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Remove arquivos deletados automaticamente.

### has_merge_conflicts

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Verifica se há conflitos de merge.

### resolve_merge_conflicts_automatically

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Resolve conflitos de merge automaticamente.

### is_staging_area_empty

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Verifica se a staging area está vazia.

### add_changed_files_automatically

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Adiciona todas as mudanças automaticamente.

### analyze_changes_by_context

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 48

Analisa mudanças e as separa por contexto para commits atômicos.

Returns:
    Dicionário com mudanças separadas por contexto

### create_atomic_commits

**Parâmetros**: self, changes_by_context, task_info
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 62

Cria commits atômicos baseados no contexto das mudanças.

Args:
    changes_by_context: Mudanças separadas por contexto
    task_info: Informações da tarefa ativa
    
Returns:
    Lista de resultados dos commits

### generate_contextual_commit_message

**Parâmetros**: self, context, files, task_info
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 46

Gera mensagem de commit contextual em português.

Args:
    context: Contexto das mudanças
    files: Lista de arquivos modificados
    task_info: Informações da tarefa ativa
    
Returns:
    Mensagem de commit em formato Conventional Commits

### extract_commit_hash

**Parâmetros**: self, git_output
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Extrai hash do commit da saída do Git.

### get_active_task

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 51

Obtém informações da tarefa ativa.

Returns:
    Informações da tarefa ativa ou None

### auto_commit_atomic

**Parâmetros**: self, auto_push
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 60

Executa commit automático e atômico com resolução de erros.

Args:
    auto_push: Se deve fazer push automático
    
Returns:
    Resultado da operação

### auto_push

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Executa push automático.

### generate_commit_report

**Parâmetros**: self, commit_results, task_info, push_result
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 46

Gera relatório detalhado dos commits.

## Classes

### GitTaskIntegration

**Herança**: Nenhuma
**Atributos**: commit_results, context_to_type, commit_type, context_descriptions, description, match, match, report, successful_commits, failed_commits, untracked_files, modified_files, deleted_files, result, result, untracked, result, modified, result, deleted, result, result, result, changes_by_context, temp_tasks_dir, task_files, latest_task, task_content, task_info, task_id_match, title_match, status_match, task_info, changes_by_context, commit_results, push_result, report, result, file_path, commit_message, result, push_result, file_path, file_path, file_path, commit_hash, commit_result, commit_result
**Métodos**: 22
**Linhas**: 558

Integração entre agente Git e sistema de tarefas - AUTOMÁTICO E ATÔMICO.

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Inicializa a integração.

#### resolve_git_errors_automatically

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 48

Resolve erros Git automaticamente sem intervenção manual.

Returns:
    True se todos os erros foram resolvidos

#### is_git_repo

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Verifica se é um repositório Git.

#### initialize_git_repo

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Inicializa repositório Git automaticamente.

#### get_untracked_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Obtém lista de arquivos não rastreados.

#### get_modified_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Obtém lista de arquivos modificados.

#### get_deleted_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Obtém lista de arquivos deletados.

#### add_untracked_files_automatically

**Parâmetros**: self, files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Adiciona arquivos não rastreados automaticamente.

#### add_modified_files_automatically

**Parâmetros**: self, files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Adiciona arquivos modificados automaticamente.

#### remove_deleted_files_automatically

**Parâmetros**: self, files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Remove arquivos deletados automaticamente.

#### has_merge_conflicts

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Verifica se há conflitos de merge.

#### resolve_merge_conflicts_automatically

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Resolve conflitos de merge automaticamente.

#### is_staging_area_empty

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Verifica se a staging area está vazia.

#### add_changed_files_automatically

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Adiciona todas as mudanças automaticamente.

#### analyze_changes_by_context

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 48

Analisa mudanças e as separa por contexto para commits atômicos.

Returns:
    Dicionário com mudanças separadas por contexto

#### create_atomic_commits

**Parâmetros**: self, changes_by_context, task_info
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 62

Cria commits atômicos baseados no contexto das mudanças.

Args:
    changes_by_context: Mudanças separadas por contexto
    task_info: Informações da tarefa ativa
    
Returns:
    Lista de resultados dos commits

#### generate_contextual_commit_message

**Parâmetros**: self, context, files, task_info
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 46

Gera mensagem de commit contextual em português.

Args:
    context: Contexto das mudanças
    files: Lista de arquivos modificados
    task_info: Informações da tarefa ativa
    
Returns:
    Mensagem de commit em formato Conventional Commits

#### extract_commit_hash

**Parâmetros**: self, git_output
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Extrai hash do commit da saída do Git.

#### get_active_task

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 51

Obtém informações da tarefa ativa.

Returns:
    Informações da tarefa ativa ou None

#### auto_commit_atomic

**Parâmetros**: self, auto_push
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 60

Executa commit automático e atômico com resolução de erros.

Args:
    auto_push: Se deve fazer push automático
    
Returns:
    Resultado da operação

#### auto_push

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Executa push automático.

#### generate_commit_report

**Parâmetros**: self, commit_results, task_info, push_result
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 46

Gera relatório detalhado dos commits.

## Imports

os, sys, json, logging, subprocess, re, pathlib.Path, typing.Dict, typing.Any, typing.Optional, typing.List, datetime.datetime, git_automation_agent.GitAutomationAgent, argparse

## Uso

```python
# Exemplo de uso do módulo git_task_integration
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:51
