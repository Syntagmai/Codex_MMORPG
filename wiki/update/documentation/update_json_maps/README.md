# update_json_maps

## Descrição

Script para atualização automática dos mapas JSON da wiki do OTClient
Atualiza: maps/tags_index.json, maps/wiki_map.json, maps/relationships.json

## Informações Técnicas

- **Módulo**: update_json_maps
- **Caminho**: wiki\update\update_json_maps.py
- **Linhas de código**: 482
- **Complexidade**: 82.00
- **Funções**: 17
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Função principal

### __init__

**Parâmetros**: self, wiki_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Sem documentação.

### scan_markdown_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Escaneia todos os arquivos markdown na pasta wiki

### extract_frontmatter

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 45

Extrai frontmatter de um arquivo markdown

### generate_tags_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Gera o índice de tags

### generate_search_aliases

**Parâmetros**: self, files_by_tag
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Gera aliases de busca para tags

### generate_wiki_map

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 53

Gera o mapa completo da wiki

### categorize_document

**Parâmetros**: self, file, frontmatter
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 33

Categoriza um documento baseado em seu conteúdo

### get_priority

**Parâmetros**: self, file, frontmatter
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Determina a prioridade de um documento

### get_description

**Parâmetros**: self, file, frontmatter
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Extrai descrição do documento

### generate_statistics

**Parâmetros**: self, categories
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Gera estatísticas da wiki

### generate_navigation_paths

**Parâmetros**: self, categories
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Gera caminhos de navegação

### generate_relationships

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Gera relacionamentos entre documentos

### generate_learning_paths

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 33

Gera caminhos de aprendizado

### generate_dependency_graph

**Parâmetros**: self, relationships
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Gera grafo de dependências

### generate_topic_clusters

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Gera clusters de tópicos

### update_all_json_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Atualiza todos os arquivos JSON

## Classes

### WikiJSONUpdater

**Herança**: Nenhuma
**Atributos**: md_files, frontmatter, files_by_tag, tags_by_file, all_tags, search_aliases, tags_index, aliases, common_aliases, categories, statistics, navigation, wiki_map, tags, title, title, stats, status_counts, priority_counts, paths, relationships, learning_paths, dependency_graph, topic_clusters, relationships_data, paths, graph, clusters, ui_files, game_files, api_files, md_files, frontmatter, tags, frontmatter, category, priority, description, doc_info, frontmatter, frontmatter, frontmatter, frontmatter, frontmatter, frontmatter, tags, frontmatter, frontmatter, frontmatter, content, parts, status, priority, frontmatter_text, tags_match, status_match, aliases_match, title_match, other_frontmatter, other_tags, common_tags, tags_str, aliases_str
**Métodos**: 16
**Linhas**: 460

Sem documentação.

#### __init__

**Parâmetros**: self, wiki_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Sem documentação.

#### scan_markdown_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Escaneia todos os arquivos markdown na pasta wiki

#### extract_frontmatter

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 45

Extrai frontmatter de um arquivo markdown

#### generate_tags_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Gera o índice de tags

#### generate_search_aliases

**Parâmetros**: self, files_by_tag
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Gera aliases de busca para tags

#### generate_wiki_map

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 53

Gera o mapa completo da wiki

#### categorize_document

**Parâmetros**: self, file, frontmatter
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 33

Categoriza um documento baseado em seu conteúdo

#### get_priority

**Parâmetros**: self, file, frontmatter
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Determina a prioridade de um documento

#### get_description

**Parâmetros**: self, file, frontmatter
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Extrai descrição do documento

#### generate_statistics

**Parâmetros**: self, categories
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Gera estatísticas da wiki

#### generate_navigation_paths

**Parâmetros**: self, categories
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Gera caminhos de navegação

#### generate_relationships

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Gera relacionamentos entre documentos

#### generate_learning_paths

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 33

Gera caminhos de aprendizado

#### generate_dependency_graph

**Parâmetros**: self, relationships
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Gera grafo de dependências

#### generate_topic_clusters

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Gera clusters de tópicos

#### update_all_json_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Atualiza todos os arquivos JSON

## Imports

os, json, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

## Uso

```python
# Exemplo de uso do módulo update_json_maps
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:52
