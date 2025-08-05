# migrated_git_automation_agent

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_git_automation_agent
- **Caminho**: wiki\update\modules\agents\agent_orchestrator\migrated_git_automation_agent.py
- **Linhas de código**: 1200
- **Complexidade**: 156.00
- **Funções**: 27
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 127

Função principal do agente.

### integrate_with_module

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Integra o script com o módulo de destino.

### __init__

**Parâmetros**: self, project_root
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 45

Inicializa o agente de automação Git.

Args:
    project_root: Caminho raiz do projeto

### validate_file_exists

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Valida se um arquivo existe antes de tentar adicioná-lo.

Args:
    file_path: Caminho do arquivo
    
Returns:
    True se o arquivo existe

### safe_add_file

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 33

Adiciona um arquivo de forma segura, validando sua existência.

Args:
    file_path: Caminho do arquivo
    
Returns:
    True se adicionado com sucesso

### analyze_changes

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 70

Analisa mudanças no repositório Git.

Returns:
    Dicionário com informações das mudanças

### _detect_task_context

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Detecta contexto de tarefa atual.

Returns:
    Informações do contexto de tarefa

### _detect_open_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Detecta arquivos abertos no IDE.

Returns:
    Lista de arquivos abertos

### _analyze_commit_groups

**Parâmetros**: self, changes
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 52

Analisa e agrupa mudanças para commits separados.

Args:
    changes: Dicionário com informações das mudanças
    
Returns:
    Lista de grupos de commit

### _group_by_directory

**Parâmetros**: self, files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Agrupa arquivos por diretório.

Args:
    files: Lista de arquivos
    
Returns:
    Lista de grupos por diretório

### _group_by_file_type

**Parâmetros**: self, files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Agrupa arquivos por tipo.

Args:
    files: Lista de arquivos
    
Returns:
    Lista de grupos por tipo

### _group_by_context

**Parâmetros**: self, files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Agrupa arquivos por contexto (análise de diff).

Args:
    files: Lista de arquivos
    
Returns:
    Lista de grupos por contexto

### _get_file_diff

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Obtém diff de um arquivo.

Args:
    file_path: Caminho do arquivo
    
Returns:
    Conteúdo do diff

### _extract_context_from_diff

**Parâmetros**: self, diff_content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Extrai contexto de um diff.

Args:
    diff_content: Conteúdo do diff
    
Returns:
    Contexto extraído

### _is_similar_context

**Parâmetros**: self, context1, context2
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Verifica se dois contextos são similares.

Args:
    context1: Primeiro contexto
    context2: Segundo contexto
    
Returns:
    True se similares

### _consolidate_groups

**Parâmetros**: self, groups
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Consolida grupos sobrepostos.

Args:
    groups: Lista de grupos
    
Returns:
    Lista consolidada

### _ensure_unique_files

**Parâmetros**: self, groups, all_files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Garante que cada arquivo está em apenas um grupo.

Args:
    groups: Lista de grupos
    all_files: Lista de todos os arquivos
    
Returns:
    Lista de grupos com arquivos únicos

### _get_file_type

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Determina o tipo de um arquivo.

Args:
    file_path: Caminho do arquivo
    
Returns:
    Tipo do arquivo

### _determine_type_from_files

**Parâmetros**: self, files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Determina o tipo de commit baseado em uma lista de arquivos.

Args:
    files: Lista de arquivos
    
Returns:
    Tipo de commit

### _generate_group_message

**Parâmetros**: self, files, commit_type
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 32

Gera mensagem para um grupo de arquivos.

Args:
    files: Lista de arquivos
    commit_type: Tipo de commit
    
Returns:
    Mensagem gerada

### _determine_commit_type

**Parâmetros**: self, changes
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Determina o tipo de commit baseado nas mudanças.

Args:
    changes: Dicionário com informações das mudanças
    
Returns:
    Tipo de commit convencional

### _generate_change_summary

**Parâmetros**: self, changes
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Gera resumo das mudanças em português.

Args:
    changes: Dicionário com informações das mudanças
    
Returns:
    Resumo das mudanças

### generate_commit_message

**Parâmetros**: self, changes
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 67

Gera mensagem de commit inteligente em português.

Args:
    changes: Dicionário com informações das mudanças
    
Returns:
    Mensagem de commit formatada

### validate_commit_message

**Parâmetros**: self, message
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 74

Valida mensagem de commit seguindo boas práticas.

Args:
    message: Mensagem de commit a ser validada
    
Returns:
    Resultado da validação

### execute_commit

**Parâmetros**: self, message, auto_push
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 94

Executa commit com validação.

Args:
    message: Mensagem de commit
    auto_push: Se deve fazer push automático
    
Returns:
    Resultado da execução

### auto_commit

**Parâmetros**: self, auto_push
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Executa commit automático completo.

Args:
    auto_push: Se deve fazer push automático
    
Returns:
    Resultado da execução

### execute_multiple_commits

**Parâmetros**: self, commit_groups, auto_push
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 41

Executa múltiplos commits baseado nos grupos.

Args:
    commit_groups: Lista de grupos de commit
    auto_push: Se deve fazer push automático
    
Returns:
    Lista de resultados dos commits

## Classes

### GitAutomationAgentFixed

**Herança**: Nenhuma
**Atributos**: groups, groups, groups, consolidated, used_files, final_groups, unused_files, changes, message, result, results, full_path, result, result, changes, task_files, open_files, cursor_temp_dir, all_files, valid_files, groups, consolidated_groups, final_groups, directory, file_type, result, lines, context_lines, similarity, merged, unique_files, file_path_lower, ext, type_counts, file_types, type_counts, descriptions, all_files, parts, commit_type, summary, task_context, body_parts, timestamp, message, validation, lines, title, conventional_pattern, validation, result, commit_result, message, result, latest_task, task_content, task_id_match, task_title_match, dir_groups, type_groups, context_groups, common_files, file_type, task_id, title, title, modified_files, added_files, deleted_files, untracked_files, push_result, error_msg, error_msg, push_result, status, file_path, merged, content
**Métodos**: 25
**Linhas**: 983

Agente de automação Git com boas práticas em português - VERSÃO CORRIGIDA.

#### __init__

**Parâmetros**: self, project_root
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 45

Inicializa o agente de automação Git.

Args:
    project_root: Caminho raiz do projeto

#### validate_file_exists

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Valida se um arquivo existe antes de tentar adicioná-lo.

Args:
    file_path: Caminho do arquivo
    
Returns:
    True se o arquivo existe

#### safe_add_file

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 33

Adiciona um arquivo de forma segura, validando sua existência.

Args:
    file_path: Caminho do arquivo
    
Returns:
    True se adicionado com sucesso

#### analyze_changes

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 70

Analisa mudanças no repositório Git.

Returns:
    Dicionário com informações das mudanças

#### _detect_task_context

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Detecta contexto de tarefa atual.

Returns:
    Informações do contexto de tarefa

#### _detect_open_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Detecta arquivos abertos no IDE.

Returns:
    Lista de arquivos abertos

#### _analyze_commit_groups

**Parâmetros**: self, changes
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 52

Analisa e agrupa mudanças para commits separados.

Args:
    changes: Dicionário com informações das mudanças
    
Returns:
    Lista de grupos de commit

#### _group_by_directory

**Parâmetros**: self, files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Agrupa arquivos por diretório.

Args:
    files: Lista de arquivos
    
Returns:
    Lista de grupos por diretório

#### _group_by_file_type

**Parâmetros**: self, files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Agrupa arquivos por tipo.

Args:
    files: Lista de arquivos
    
Returns:
    Lista de grupos por tipo

#### _group_by_context

**Parâmetros**: self, files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Agrupa arquivos por contexto (análise de diff).

Args:
    files: Lista de arquivos
    
Returns:
    Lista de grupos por contexto

#### _get_file_diff

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Obtém diff de um arquivo.

Args:
    file_path: Caminho do arquivo
    
Returns:
    Conteúdo do diff

#### _extract_context_from_diff

**Parâmetros**: self, diff_content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Extrai contexto de um diff.

Args:
    diff_content: Conteúdo do diff
    
Returns:
    Contexto extraído

#### _is_similar_context

**Parâmetros**: self, context1, context2
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Verifica se dois contextos são similares.

Args:
    context1: Primeiro contexto
    context2: Segundo contexto
    
Returns:
    True se similares

#### _consolidate_groups

**Parâmetros**: self, groups
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Consolida grupos sobrepostos.

Args:
    groups: Lista de grupos
    
Returns:
    Lista consolidada

#### _ensure_unique_files

**Parâmetros**: self, groups, all_files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Garante que cada arquivo está em apenas um grupo.

Args:
    groups: Lista de grupos
    all_files: Lista de todos os arquivos
    
Returns:
    Lista de grupos com arquivos únicos

#### _get_file_type

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Determina o tipo de um arquivo.

Args:
    file_path: Caminho do arquivo
    
Returns:
    Tipo do arquivo

#### _determine_type_from_files

**Parâmetros**: self, files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Determina o tipo de commit baseado em uma lista de arquivos.

Args:
    files: Lista de arquivos
    
Returns:
    Tipo de commit

#### _generate_group_message

**Parâmetros**: self, files, commit_type
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 32

Gera mensagem para um grupo de arquivos.

Args:
    files: Lista de arquivos
    commit_type: Tipo de commit
    
Returns:
    Mensagem gerada

#### _determine_commit_type

**Parâmetros**: self, changes
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Determina o tipo de commit baseado nas mudanças.

Args:
    changes: Dicionário com informações das mudanças
    
Returns:
    Tipo de commit convencional

#### _generate_change_summary

**Parâmetros**: self, changes
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Gera resumo das mudanças em português.

Args:
    changes: Dicionário com informações das mudanças
    
Returns:
    Resumo das mudanças

#### generate_commit_message

**Parâmetros**: self, changes
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 67

Gera mensagem de commit inteligente em português.

Args:
    changes: Dicionário com informações das mudanças
    
Returns:
    Mensagem de commit formatada

#### validate_commit_message

**Parâmetros**: self, message
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 74

Valida mensagem de commit seguindo boas práticas.

Args:
    message: Mensagem de commit a ser validada
    
Returns:
    Resultado da validação

#### execute_commit

**Parâmetros**: self, message, auto_push
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 94

Executa commit com validação.

Args:
    message: Mensagem de commit
    auto_push: Se deve fazer push automático
    
Returns:
    Resultado da execução

#### auto_commit

**Parâmetros**: self, auto_push
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Executa commit automático completo.

Args:
    auto_push: Se deve fazer push automático
    
Returns:
    Resultado da execução

#### execute_multiple_commits

**Parâmetros**: self, commit_groups, auto_push
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 41

Executa múltiplos commits baseado nos grupos.

Args:
    commit_groups: Lista de grupos de commit
    auto_push: Se deve fazer push automático
    
Returns:
    Lista de resultados dos commits

## Imports

.AgentorchestratorModule, subprocess, re, logging, datetime.datetime, sys, argparse, difflib

## Uso

```python
# Exemplo de uso do módulo migrated_git_automation_agent
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:58

## 🔗 **Links Automáticos**

> [!info] **Links Gerados Automaticamente**
> Estes links foram criados automaticamente pelo sistema de linkagem da categoria **Tools**

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]
- [[../maps/tools_index|Índice de Ferramentas]]
- [[../update/README|Scripts de Atualização]]

### **🧭 Navegação**
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]
- [[../maps/category_indices|Índices por Categoria]]
- [[../maps/relationships|Relacionamentos]]

### **📊 Métricas da Categoria**
- **Categoria**: Tools
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

