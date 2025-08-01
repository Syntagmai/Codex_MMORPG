# update_resources_index

## Descrição

Script para indexação dos recursos do OTClient
Atualiza: wiki/maps/resources_index.json

## Informações Técnicas

- **Módulo**: update_resources_index
- **Caminho**: wiki\update\update_resources_index.py
- **Linhas de código**: 337
- **Complexidade**: 41.00
- **Funções**: 16
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Função principal

### __init__

**Parâmetros**: self, project_root
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Sem documentação.

### scan_resources

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Escaneia todos os recursos

### analyze_resource

**Parâmetros**: self, resource_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 33

Analisa um recurso

### categorize_resource

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Categoriza um recurso

### extract_metadata

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Extrai metadados do arquivo

### extract_font_metadata

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Extrai metadados de fonte

### extract_locale_metadata

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Extrai metadados de localização

### extract_particle_metadata

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Extrai metadados de partículas

### count_lines

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Conta linhas de um arquivo

### categorize_resources

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Categoriza todos os recursos

### generate_statistics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Gera estatísticas dos recursos

### generate_search_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Gera índice de busca

### generate_resources_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Gera o índice completo dos recursos

### save_index

**Parâmetros**: self, resources_index, output_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Salva o índice em arquivo JSON

### update_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Atualiza o índice dos recursos

## Classes

### ResourcesIndexer

**Herança**: Nenhuma
**Atributos**: resources, resource_paths, file_ext, parent_dir, metadata, file_ext, stats, ext_counts, search_index, resource_files, statistics, search_index, resources_index, resources_index, category_path, file_path, file_name, file_stem, file_ext, category, metadata, stat, resource_info, metadata, language, metadata, metadata, category, ext, name, category, ext, resource_info, output_path, metadata, content, content, content, metadata, metadata, metadata
**Métodos**: 15
**Linhas**: 304

Sem documentação.

#### __init__

**Parâmetros**: self, project_root
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Sem documentação.

#### scan_resources

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Escaneia todos os recursos

#### analyze_resource

**Parâmetros**: self, resource_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 33

Analisa um recurso

#### categorize_resource

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Categoriza um recurso

#### extract_metadata

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Extrai metadados do arquivo

#### extract_font_metadata

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Extrai metadados de fonte

#### extract_locale_metadata

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Extrai metadados de localização

#### extract_particle_metadata

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Extrai metadados de partículas

#### count_lines

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Conta linhas de um arquivo

#### categorize_resources

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Categoriza todos os recursos

#### generate_statistics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Gera estatísticas dos recursos

#### generate_search_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Gera índice de busca

#### generate_resources_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Gera o índice completo dos recursos

#### save_index

**Parâmetros**: self, resources_index, output_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Salva o índice em arquivo JSON

#### update_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Atualiza o índice dos recursos

## Imports

os, json, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

## Uso

```python
# Exemplo de uso do módulo update_resources_index
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:52
