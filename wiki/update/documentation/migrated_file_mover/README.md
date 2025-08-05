# migrated_file_mover

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_file_mover
- **Caminho**: wiki\update\modules\tools\file_mover\migrated_file_mover.py
- **Linhas de código**: 342
- **Complexidade**: 41.00
- **Funções**: 10
- **Classes**: 1

## Funções

### load_config

**Parâmetros**: config_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Load configuration from JSON file.

### save_config

**Parâmetros**: config, config_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Save configuration to JSON file.

### interactive_mode

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 55

Interactive mode for file moving.

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 66

Main function with command line interface.

### integrate_with_module

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Integra o script com o módulo de destino.

### __init__

**Parâmetros**: self, dry_run, create_backup
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Sem documentação.

### setup_backup_directory

**Parâmetros**: self, source_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Create backup directory for safety.

### validate_paths

**Parâmetros**: self, source_dir, destination_dir, files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Validate all paths before moving files.

### move_file

**Parâmetros**: self, source_file, destination_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Move a single file with error handling.

### move_files

**Parâmetros**: self, source_dir, destination_dir, files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 42

Move multiple files efficiently.

## Classes

### FileMover

**Herança**: Nenhuma
**Atributos**: timestamp, backup_dir, errors, file_path, source_file, destination_file, backup_file
**Métodos**: 5
**Linhas**: 116

Efficient file mover with absolute directory support.

#### __init__

**Parâmetros**: self, dry_run, create_backup
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Sem documentação.

#### setup_backup_directory

**Parâmetros**: self, source_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Create backup directory for safety.

#### validate_paths

**Parâmetros**: self, source_dir, destination_dir, files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Validate all paths before moving files.

#### move_file

**Parâmetros**: self, source_file, destination_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Move a single file with error handling.

#### move_files

**Parâmetros**: self, source_dir, destination_dir, files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 42

Move multiple files efficiently.

## Imports

.FilemoverModule, os, sys, json, shutil, argparse, logging, datetime.datetime

## Uso

```python
# Exemplo de uso do módulo migrated_file_mover
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:52

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

