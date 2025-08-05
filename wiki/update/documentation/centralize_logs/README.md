# centralize_logs

## Descrição

Sistema de Logs Centralizado
============================

Este script centraliza e organiza logs espalhados em sistema centralizado
com categorização automática e estrutura hierárquica.

Autor: Sistema BMAD - Log Organizer
Data: 2025-08-01

## Informações Técnicas

- **Módulo**: centralize_logs
- **Caminho**: wiki\update\centralize_logs.py
- **Linhas de código**: 417
- **Complexidade**: 38.00
- **Funções**: 10
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Função principal

### __init__

**Parâmetros**: self, log_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 72

Inicializa o centralizador de logs.

Args:
    log_dir: Diretório principal de logs

### create_centralized_structure

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Cria estrutura centralizada de logs

### categorize_file

**Parâmetros**: self, filename
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Categoriza um arquivo de log

### matches_pattern

**Parâmetros**: self, filename, pattern
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Verifica se arquivo corresponde ao padrão

### backup_existing_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Faz backup dos arquivos existentes

### move_file_to_category

**Parâmetros**: self, file_path, category, subcategory
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Move arquivo para categoria apropriada

### centralize_logs

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 60

Centraliza todos os logs

### create_centralized_index

**Parâmetros**: self, results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Cria índice centralizado dos logs

### generate_centralization_report

**Parâmetros**: self, results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 62

Gera relatório de centralização

## Classes

### LogCentralizer

**Herança**: Nenhuma
**Atributos**: filename_lower, results, report, index_data, index_file, category_path, dest_dir, dest_file, subcategory_path, subcategory, relative_path, backup_path, timestamp, name_parts, dest_file, categorization, category, subcategory, error_msg, subcategory
**Métodos**: 9
**Linhas**: 347

Centralizador de logs BMAD

#### __init__

**Parâmetros**: self, log_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 72

Inicializa o centralizador de logs.

Args:
    log_dir: Diretório principal de logs

#### create_centralized_structure

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Cria estrutura centralizada de logs

#### categorize_file

**Parâmetros**: self, filename
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Categoriza um arquivo de log

#### matches_pattern

**Parâmetros**: self, filename, pattern
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Verifica se arquivo corresponde ao padrão

#### backup_existing_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Faz backup dos arquivos existentes

#### move_file_to_category

**Parâmetros**: self, file_path, category, subcategory
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Move arquivo para categoria apropriada

#### centralize_logs

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 60

Centraliza todos os logs

#### create_centralized_index

**Parâmetros**: self, results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Cria índice centralizado dos logs

#### generate_centralization_report

**Parâmetros**: self, results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 62

Gera relatório de centralização

## Imports

json, os, shutil, pathlib.Path, typing.Dict, typing.List, typing.Any, typing.Optional, datetime.datetime, logging, fnmatch

## Uso

```python
# Exemplo de uso do módulo centralize_logs
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:50

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

