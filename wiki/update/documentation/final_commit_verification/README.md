# final_commit_verification

## Descrição

Sistema de Verificação Final de Commits
=======================================

Sistema que garante que todos os commits sejam feitos corretamente,
incluindo o relatório final, e sempre faz pull para evitar perda de dados.

Autor: Sistema BMAD - OTClient Documentation
Data: 2025-01-28
Versão: 1.0

## Informações Técnicas

- **Módulo**: final_commit_verification
- **Caminho**: wiki\update\final_commit_verification.py
- **Linhas de código**: 473
- **Complexidade**: 37.00
- **Funções**: 10
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 41

Função principal.

### __init__

**Parâmetros**: self, base_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 4

Sem documentação.

### pull_latest_changes

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Faz pull das últimas mudanças para evitar perda de dados.

Returns:
    True se pull foi bem-sucedido

### check_git_status

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 44

Verifica status do Git.

Returns:
    Dicionário com informações do status

### add_all_changes

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Adiciona todas as mudanças ao staging.

Returns:
    True se adição foi bem-sucedida

### commit_changes

**Parâmetros**: self, message
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Faz commit das mudanças.

Args:
    message: Mensagem do commit
    
Returns:
    True se commit foi bem-sucedido

### push_changes

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Faz push das mudanças.

Returns:
    True se push foi bem-sucedido

### verify_clean_working_tree

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Verifica se o working tree está limpo.

Returns:
    True se working tree está limpo

### generate_final_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 131

Gera relatório final da verificação.

Returns:
    Conteúdo do relatório

### run_final_verification

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 78

Executa verificação final completa.

Returns:
    Resultados da verificação

## Classes

### FinalCommitVerification

**Herança**: Nenhuma
**Atributos**: report, results, result, result, status_info, result, result, result, result, status_info, report_content, report_path, lines, commit_message, status, file_path
**Métodos**: 9
**Linhas**: 390

Sistema de verificação final de commits

#### __init__

**Parâmetros**: self, base_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 4

Sem documentação.

#### pull_latest_changes

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Faz pull das últimas mudanças para evitar perda de dados.

Returns:
    True se pull foi bem-sucedido

#### check_git_status

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 44

Verifica status do Git.

Returns:
    Dicionário com informações do status

#### add_all_changes

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Adiciona todas as mudanças ao staging.

Returns:
    True se adição foi bem-sucedida

#### commit_changes

**Parâmetros**: self, message
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Faz commit das mudanças.

Args:
    message: Mensagem do commit
    
Returns:
    True se commit foi bem-sucedido

#### push_changes

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Faz push das mudanças.

Returns:
    True se push foi bem-sucedido

#### verify_clean_working_tree

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Verifica se o working tree está limpo.

Returns:
    True se working tree está limpo

#### generate_final_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 131

Gera relatório final da verificação.

Returns:
    Conteúdo do relatório

#### run_final_verification

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 78

Executa verificação final completa.

Returns:
    Resultados da verificação

## Imports

os, sys, subprocess, logging, pathlib.Path, typing.Dict, typing.Any, typing.List, datetime.datetime, argparse

## Uso

```python
# Exemplo de uso do módulo final_commit_verification
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:51

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

