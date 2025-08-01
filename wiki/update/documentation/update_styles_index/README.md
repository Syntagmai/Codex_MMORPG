# update_styles_index

## Descrição

Script para indexação dos estilos OTUI do OTClient
Atualiza: wiki/maps/styles_index.json

## Informações Técnicas

- **Módulo**: update_styles_index
- **Caminho**: wiki\update\update_styles_index.py
- **Linhas de código**: 323
- **Complexidade**: 44.00
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
**Linhas**: 10

Sem documentação.

### scan_style_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Escaneia todos os arquivos de estilo OTUI

### analyze_style_file

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 39

Analisa um arquivo de estilo OTUI

### extract_widgets

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Extrai widgets do arquivo de estilo

### extract_widget_properties

**Parâmetros**: self, widget_content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Extrai propriedades de um widget

### guess_property_type

**Parâmetros**: self, value
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Tenta adivinhar o tipo da propriedade

### extract_properties

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Extrai todas as propriedades do arquivo

### extract_dependencies

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Extrai dependências do arquivo de estilo

### categorize_style

**Parâmetros**: self, file_name, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Categoriza um arquivo de estilo

### categorize_styles

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Categoriza todos os estilos

### generate_statistics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Gera estatísticas dos estilos

### generate_search_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Gera índice de busca

### generate_styles_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Gera o índice completo dos estilos

### save_index

**Parâmetros**: self, styles_index, output_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Salva o índice em arquivo JSON

### update_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Atualiza o índice dos estilos

## Classes

### StylesIndexer

**Herança**: Nenhuma
**Atributos**: style_files, widgets, widget_pattern, matches, properties, prop_pattern, matches, value, properties, prop_pattern, matches, dependencies, import_pattern, imports, include_pattern, includes, name_lower, content_lower, stats, search_index, style_files, statistics, search_index, styles_index, styles_index, file_name, file_stem, widgets, properties, dependencies, category, style_info, widget_info, prop_info, prop_info, category, name, style_info, output_path, content, widget_name, prop_name
**Métodos**: 15
**Linhas**: 290

Sem documentação.

#### __init__

**Parâmetros**: self, project_root
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Sem documentação.

#### scan_style_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Escaneia todos os arquivos de estilo OTUI

#### analyze_style_file

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 39

Analisa um arquivo de estilo OTUI

#### extract_widgets

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Extrai widgets do arquivo de estilo

#### extract_widget_properties

**Parâmetros**: self, widget_content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Extrai propriedades de um widget

#### guess_property_type

**Parâmetros**: self, value
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Tenta adivinhar o tipo da propriedade

#### extract_properties

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Extrai todas as propriedades do arquivo

#### extract_dependencies

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Extrai dependências do arquivo de estilo

#### categorize_style

**Parâmetros**: self, file_name, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Categoriza um arquivo de estilo

#### categorize_styles

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Categoriza todos os estilos

#### generate_statistics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Gera estatísticas dos estilos

#### generate_search_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Gera índice de busca

#### generate_styles_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Gera o índice completo dos estilos

#### save_index

**Parâmetros**: self, styles_index, output_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Salva o índice em arquivo JSON

#### update_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Atualiza o índice dos estilos

## Imports

os, json, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

## Uso

```python
# Exemplo de uso do módulo update_styles_index
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:52
