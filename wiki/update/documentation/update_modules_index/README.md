# update_modules_index

## Descrição

Script para indexação dos módulos Lua do OTClient
Atualiza: wiki/maps/modules_index.json

## Informações Técnicas

- **Módulo**: update_modules_index
- **Caminho**: wiki\update\update_modules_index.py
- **Linhas de código**: 319
- **Complexidade**: 44.00
- **Funções**: 14
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
**Linhas**: 10

Sem documentação.

### scan_modules

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Escaneia todos os módulos Lua

### analyze_module

**Parâmetros**: self, module_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 57

Analisa um módulo Lua

### extract_description

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Extrai descrição do módulo

### extract_lua_apis

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 32

Extrai APIs Lua do arquivo

### extract_dependencies

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Extrai dependências do módulo

### categorize_module

**Parâmetros**: self, module_name
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Categoriza um módulo

### categorize_modules

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Categoriza todos os módulos

### generate_statistics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Gera estatísticas dos módulos

### generate_search_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Gera índice de busca

### generate_modules_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Gera o índice completo dos módulos

### save_index

**Parâmetros**: self, modules_index, output_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Salva o índice em arquivo JSON

### update_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Atualiza o índice dos módulos

## Classes

### ModulesIndexer

**Herança**: Nenhuma
**Atributos**: modules, lines, apis, dependencies, require_pattern, requires, import_pattern, imports, name_lower, stats, search_index, modules_paths, statistics, search_index, modules_index, modules_index, module_dir, module_name, lua_files, otmod_files, otui_files, main_lua, module_info, line, function_pattern, functions, class_pattern, classes, category, name, module_info, output_path, main_lua, content, api_name, dep_lower, main_lua, content
**Métodos**: 13
**Linhas**: 286

Sem documentação.

#### __init__

**Parâmetros**: self, project_root
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Sem documentação.

#### scan_modules

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Escaneia todos os módulos Lua

#### analyze_module

**Parâmetros**: self, module_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 57

Analisa um módulo Lua

#### extract_description

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Extrai descrição do módulo

#### extract_lua_apis

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 32

Extrai APIs Lua do arquivo

#### extract_dependencies

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Extrai dependências do módulo

#### categorize_module

**Parâmetros**: self, module_name
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Categoriza um módulo

#### categorize_modules

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Categoriza todos os módulos

#### generate_statistics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Gera estatísticas dos módulos

#### generate_search_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Gera índice de busca

#### generate_modules_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Gera o índice completo dos módulos

#### save_index

**Parâmetros**: self, modules_index, output_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Salva o índice em arquivo JSON

#### update_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Atualiza o índice dos módulos

## Imports

os, json, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

## Uso

```python
# Exemplo de uso do módulo update_modules_index
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:52
