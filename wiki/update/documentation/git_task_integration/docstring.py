"""
git_task_integration

Integração Git + Sistema de Tarefas - Sistema Automático e Atômico
==================================================================

Script que integra o agente de automação Git com o sistema de tarefas BMAD,
permitindo commits automáticos durante o desenvolvimento com contexto de tarefa.
IMPLEMENTAÇÃO AUTOMÁTICA E ATÔMICA - NUNCA MANUAL!

Autor: Sistema BMAD - OTClient Documentation
Data: 2024-12-19
Versão: 2.0 - Automático e Atômico

Módulo: git_task_integration
Caminho: wiki\update\git_task_integration.py
Linhas de código: 655
Complexidade: 82.00

Funções (23):
- main(): Função principal....\n- __init__(self): Inicializa a integração....\n- resolve_git_errors_automatically(self): Resolve erros Git automaticamente sem intervenção ...\n- is_git_repo(self): Verifica se é um repositório Git....\n- initialize_git_repo(self): Inicializa repositório Git automaticamente....\n- get_untracked_files(self): Obtém lista de arquivos não rastreados....\n- get_modified_files(self): Obtém lista de arquivos modificados....\n- get_deleted_files(self): Obtém lista de arquivos deletados....\n- add_untracked_files_automatically(self, files): Adiciona arquivos não rastreados automaticamente....\n- add_modified_files_automatically(self, files): Adiciona arquivos modificados automaticamente....\n- remove_deleted_files_automatically(self, files): Remove arquivos deletados automaticamente....\n- has_merge_conflicts(self): Verifica se há conflitos de merge....\n- resolve_merge_conflicts_automatically(self): Resolve conflitos de merge automaticamente....\n- is_staging_area_empty(self): Verifica se a staging area está vazia....\n- add_changed_files_automatically(self): Adiciona todas as mudanças automaticamente....\n- analyze_changes_by_context(self): Analisa mudanças e as separa por contexto para com...\n- create_atomic_commits(self, changes_by_context, task_info): Cria commits atômicos baseados no contexto das mud...\n- generate_contextual_commit_message(self, context, files, task_info): Gera mensagem de commit contextual em português.

...\n- extract_commit_hash(self, git_output): Extrai hash do commit da saída do Git....\n- get_active_task(self): Obtém informações da tarefa ativa.

Returns:
    I...\n- auto_commit_atomic(self, auto_push): Executa commit automático e atômico com resolução ...\n- auto_push(self): Executa push automático....\n- generate_commit_report(self, commit_results, task_info, push_result): Gera relatório detalhado dos commits....\n
Classes (1):
- GitTaskIntegration: Integração entre agente Git e sistema de tarefas -...\n  - __init__(self): Inicializa a integração....\n  - resolve_git_errors_automatically(self): Resolve erros Git automaticame...\n  - is_git_repo(self): Verifica se é um repositório G...\n  - initialize_git_repo(self): Inicializa repositório Git aut...\n  - get_untracked_files(self): Obtém lista de arquivos não ra...\n  - get_modified_files(self): Obtém lista de arquivos modifi...\n  - get_deleted_files(self): Obtém lista de arquivos deleta...\n  - add_untracked_files_automatically(self, files): Adiciona arquivos não rastread...\n  - add_modified_files_automatically(self, files): Adiciona arquivos modificados ...\n  - remove_deleted_files_automatically(self, files): Remove arquivos deletados auto...\n  - has_merge_conflicts(self): Verifica se há conflitos de me...\n  - resolve_merge_conflicts_automatically(self): Resolve conflitos de merge aut...\n  - is_staging_area_empty(self): Verifica se a staging area est...\n  - add_changed_files_automatically(self): Adiciona todas as mudanças aut...\n  - analyze_changes_by_context(self): Analisa mudanças e as separa p...\n  - create_atomic_commits(self, changes_by_context, task_info): Cria commits atômicos baseados...\n  - generate_contextual_commit_message(self, context, files, task_info): Gera mensagem de commit contex...\n  - extract_commit_hash(self, git_output): Extrai hash do commit da saída...\n  - get_active_task(self): Obtém informações da tarefa at...\n  - auto_commit_atomic(self, auto_push): Executa commit automático e at...\n  - auto_push(self): Executa push automático....\n  - generate_commit_report(self, commit_results, task_info, push_result): Gera relatório detalhado dos c...\n
Imports (14):
os, sys, json, logging, subprocess, re, pathlib.Path, typing.Dict, typing.Any, typing.Optional...

Autor: Documentation Agent
Data: 2025-08-01 15:05:51
"""
