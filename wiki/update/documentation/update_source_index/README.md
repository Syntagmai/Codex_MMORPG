# update_source_index

## Descrição

Script para indexação automática do código-fonte do OTClient e Canary (submódulos)
Gera otclient_source_index.json com informações sobre arquivos C++ e Lua
Adaptado para estrutura com submódulos otclient/ e canary/

## Informações Técnicas

- **Módulo**: update_source_index
- **Caminho**: wiki\update\update_source_index.py
- **Linhas de código**: 272
- **Complexidade**: 53.00
- **Funções**: 10
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Função principal

### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Sem documentação.

### scan_source_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Escaneia arquivos de código-fonte nos submódulos

### categorize_file

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 32

Categoriza um arquivo baseado em seu caminho e conteúdo

### extract_functions

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Extrai funções de um arquivo

### extract_classes

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Extrai classes de um arquivo

### generate_source_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 44

Gera o índice completo do código-fonte

### generate_statistics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Gera estatísticas do código-fonte

### generate_search_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Gera índice de busca

### save_index

**Parâmetros**: self, source_index, output_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Salva o índice em arquivo JSON

## Classes

### SourceIndexer

**Herança**: Nenhuma
**Atributos**: source_extensions, source_files, otclient_src_dir, otclient_modules_dir, canary_src_dir, canary_modules_dir, path_lower, functions, classes, source_files, statistics, search_index, source_index, stats, search_index, category, functions, classes, file_info, output_path, content, lua_functions, cpp_functions, content, cpp_classes, ext, file_name
**Métodos**: 9
**Linhas**: 238

Sem documentação.

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Sem documentação.

#### scan_source_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Escaneia arquivos de código-fonte nos submódulos

#### categorize_file

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 32

Categoriza um arquivo baseado em seu caminho e conteúdo

#### extract_functions

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Extrai funções de um arquivo

#### extract_classes

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Extrai classes de um arquivo

#### generate_source_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 44

Gera o índice completo do código-fonte

#### generate_statistics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Gera estatísticas do código-fonte

#### generate_search_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Gera índice de busca

#### save_index

**Parâmetros**: self, source_index, output_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Salva o índice em arquivo JSON

## Imports

os, json, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

## Uso

```python
# Exemplo de uso do módulo update_source_index
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:52
