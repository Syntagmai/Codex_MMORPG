# git_atomic_commits

## Descrição

Script para fazer commits atômicos organizados por categoria
Seguindo as regras de automação Git do sistema BMAD

## Informações Técnicas

- **Módulo**: git_atomic_commits
- **Caminho**: wiki\update\git_atomic_commits.py
- **Linhas de código**: 135
- **Complexidade**: 21.00
- **Funções**: 5
- **Classes**: 0

## Funções

### run_command

**Parâmetros**: command, capture_output
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Executa comando e retorna resultado

### get_untracked_files

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Obtém lista de arquivos não rastreados

### categorize_files

**Parâmetros**: files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Categoriza arquivos por tipo

### make_commit

**Parâmetros**: files, category, description
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Faz commit de uma categoria de arquivos

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 43

Função principal

## Classes

## Imports

subprocess, os, sys, pathlib.Path

## Uso

```python
# Exemplo de uso do módulo git_atomic_commits
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

