# migrated_migrated_centralize_logs

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_migrated_centralize_logs
- **Caminho**: wiki\update\modules\maps\map_updater\migrated_migrated_centralize_logs.py
- **Linhas de código**: 477
- **Complexidade**: 42.00
- **Funções**: 12
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Função principal

### integrate_with_module

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Integra o script com o módulo de destino.

### integrate_with_module

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Integra o script com o módulo de destino.

### __init__

**Parâmetros**: self, log_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 74

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
**Linhas**: 349

Centralizador de logs BMAD

#### __init__

**Parâmetros**: self, log_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 74

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

.MapupdaterModule, .LogmanagerModule, json, shutil, datetime.datetime, logging, fnmatch

## Uso

```python
# Exemplo de uso do módulo migrated_migrated_centralize_logs
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:55
