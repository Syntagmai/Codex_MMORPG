# navigation_index_generator

## Descrição

Navigation Index Generator

Este script gera índices de navegação para facilitar a busca e navegação
na documentação integrada habdel-wiki.

## Informações Técnicas

- **Módulo**: navigation_index_generator
- **Caminho**: wiki\update\navigation_index_generator.py
- **Linhas de código**: 657
- **Complexidade**: 62.00
- **Funções**: 15
- **Classes**: 1

## Funções

### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Sem documentação.

### scan_all_documents

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 56

Escaneia todos os documentos para criar índice completo

### extract_document_info

**Parâmetros**: self, file_path, source
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 61

Extrai informações do documento

### extract_frontmatter

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Extrai frontmatter do conteúdo

### extract_title

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Extrai título do conteúdo

### extract_story_id

**Parâmetros**: self, content, filename
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Extrai ID da story

### categorize_document

**Parâmetros**: self, doc_info
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Categoriza o documento

### categorize_size

**Parâmetros**: self, size
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Categoriza o tamanho do documento

### extract_keywords

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Extrai palavras-chave do conteúdo

### create_alphabetical_index

**Parâmetros**: self, documents
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 74

Cria índice alfabético

### create_categorical_index

**Parâmetros**: self, documents
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 87

Cria índice por categorias

### create_story_based_index

**Parâmetros**: self, documents
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 91

Cria índice baseado em stories

### create_search_index

**Parâmetros**: self, documents
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 71

Cria índice de busca

### save_indexes

**Parâmetros**: self, documents
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Salva todos os índices

### run

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Executa a geração de índices

## Classes

### NavigationIndexGenerator

**Herança**: Nenhuma
**Atributos**: documents, frontmatter, frontmatter_match, lines, story_patterns, filename, keywords, patterns, all_docs, index_content, current_letter, index_content, category_order, index_content, story_categories, category_order, index_content, all_keywords, keyword_docs, sorted_keywords, saved_files, indexes, frontmatter, title, story_id, tags, status, priority, size, size_category, keywords, frontmatter_text, tags_match, status_match, priority_match, match, matches, first_letter, source_emoji, status_emoji, category, docs, documents, saved_files, doc_info, category, doc_info, category, content, tags_str, tags, current_letter, docs, category_emoji, habdel_docs, wiki_docs, docs, stories, category_name, category_emoji, stories, status_emoji, source_emoji, index_content, index_file, status_emoji, source_emoji, status_emoji, status_emoji
**Métodos**: 15
**Linhas**: 631

Sem documentação.

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Sem documentação.

#### scan_all_documents

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 56

Escaneia todos os documentos para criar índice completo

#### extract_document_info

**Parâmetros**: self, file_path, source
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 61

Extrai informações do documento

#### extract_frontmatter

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Extrai frontmatter do conteúdo

#### extract_title

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Extrai título do conteúdo

#### extract_story_id

**Parâmetros**: self, content, filename
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Extrai ID da story

#### categorize_document

**Parâmetros**: self, doc_info
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Categoriza o documento

#### categorize_size

**Parâmetros**: self, size
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Categoriza o tamanho do documento

#### extract_keywords

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Extrai palavras-chave do conteúdo

#### create_alphabetical_index

**Parâmetros**: self, documents
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 74

Cria índice alfabético

#### create_categorical_index

**Parâmetros**: self, documents
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 87

Cria índice por categorias

#### create_story_based_index

**Parâmetros**: self, documents
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 91

Cria índice baseado em stories

#### create_search_index

**Parâmetros**: self, documents
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 71

Cria índice de busca

#### save_indexes

**Parâmetros**: self, documents
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Salva todos os índices

#### run

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Executa a geração de índices

## Imports

json, logging, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Optional, typing.Tuple

## Uso

```python
# Exemplo de uso do módulo navigation_index_generator
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:51
