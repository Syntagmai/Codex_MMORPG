# migrated_update_wiki_maps

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_update_wiki_maps
- **Caminho**: wiki\update\modules\maps\wiki_indexer\migrated_update_wiki_maps.py
- **Linhas de código**: 314
- **Complexidade**: 37.00
- **Funções**: 10
- **Classes**: 1

## Funções

### integrate_with_module

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Integra o script com o módulo de destino.

### __init__

**Parâmetros**: self, wiki_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Sem documentação.

### load_context_data

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Carrega dados de contexto detectado

### scan_markdown_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Escaneia todos os arquivos markdown na pasta de documentação

### extract_frontmatter

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 46

Extrai frontmatter de um arquivo markdown

### generate_tags_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Gera índice de tags

### generate_wiki_map

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 53

Gera mapa da wiki

### categorize_document

**Parâmetros**: self, file_name, frontmatter
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Categoriza documento baseado no nome e tags

### generate_relationships

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Gera relacionamentos entre documentos

### update_all_json_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Atualiza todos os arquivos JSON

## Classes

### WikiJSONUpdater

**Herança**: Nenhuma
**Atributos**: context_file, md_files, docs_dir, frontmatter, tags_index, all_tags, wiki_map, file_lower, tags_lower, relationships, md_files, docs_dir, frontmatter, frontmatter, category, frontmatter, content, parts, frontmatter_text, tags_match, status_match, aliases_match, title_match, tags_str, aliases_str
**Métodos**: 9
**Linhas**: 267

Sem documentação.

#### __init__

**Parâmetros**: self, wiki_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Sem documentação.

#### load_context_data

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Carrega dados de contexto detectado

#### scan_markdown_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Escaneia todos os arquivos markdown na pasta de documentação

#### extract_frontmatter

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 46

Extrai frontmatter de um arquivo markdown

#### generate_tags_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Gera índice de tags

#### generate_wiki_map

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 53

Gera mapa da wiki

#### categorize_document

**Parâmetros**: self, file_name, frontmatter
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Categoriza documento baseado no nome e tags

#### generate_relationships

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Gera relacionamentos entre documentos

#### update_all_json_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Atualiza todos os arquivos JSON

## Imports

.WikiindexerModule, json, re, datetime.datetime

## Uso

```python
# Exemplo de uso do módulo migrated_update_wiki_maps
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:56
