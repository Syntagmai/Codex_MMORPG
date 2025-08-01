# migrated_advanced_search_system

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_advanced_search_system
- **Caminho**: wiki\update\modules\analysis\advanced_searcher\migrated_advanced_search_system.py
- **Linhas de código**: 699
- **Complexidade**: 62.00
- **Funções**: 21
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Função principal do script.

### integrate_with_module

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Integra o script com o módulo de destino.

### __init__

**Parâmetros**: self, consolidated_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Inicializa o sistema de busca avançada.

Args:
    consolidated_dir: Diretório dos documentos consolidados

### load_intelligent_navigation

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Carrega dados de navegação inteligente.

Returns:
    Dados de navegação inteligente

### extract_document_content

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 56

Extrai conteúdo completo de um documento.

Args:
    file_path: Caminho para o documento
    
Returns:
    Conteúdo extraído do documento

### build_content_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Constrói índice de conteúdo para busca textual.

### build_semantic_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 32

Constrói índice semântico baseado em similaridade de conteúdo.

### build_category_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Constrói índice por categorias.

### build_tag_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Constrói índice por tags.

### build_keyword_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Constrói índice por palavras-chave.

### build_metadata_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 45

Constrói índice por metadados.

### build_similarity_matrix

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Constrói matriz de similaridade entre documentos.

### calculate_similarity

**Parâmetros**: self, doc1, doc2
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Calcula similaridade entre dois documentos.

Args:
    doc1: Dados do primeiro documento
    doc2: Dados do segundo documento
    
Returns:
    Score de similaridade (0-1)

### search_by_text

**Parâmetros**: self, query, limit
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 50

Busca por texto nos documentos.

Args:
    query: Query de busca
    limit: Limite de resultados
    
Returns:
    Lista de resultados

### search_by_tags

**Parâmetros**: self, tags, limit
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 32

Busca por tags.

Args:
    tags: Lista de tags para buscar
    limit: Limite de resultados
    
Returns:
    Lista de resultados

### search_by_category

**Parâmetros**: self, category, subcategory, limit
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Busca por categoria.

Args:
    category: Categoria principal
    subcategory: Subcategoria (opcional)
    limit: Limite de resultados
    
Returns:
    Lista de resultados

### search_similar

**Parâmetros**: self, doc_path, limit
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Busca documentos similares.

Args:
    doc_path: Caminho do documento de referência
    limit: Limite de resultados
    
Returns:
    Lista de documentos similares

### extract_snippet

**Parâmetros**: self, content, query, max_length
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 41

Extrai snippet do conteúdo com a query destacada.

Args:
    content: Conteúdo do documento
    query: Query de busca
    max_length: Tamanho máximo do snippet
    
Returns:
    Snippet extraído

### save_search_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Salva o índice de busca avançada.

### generate_search_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Gera relatório do sistema de busca.

Returns:
    Caminho do relatório

### build_advanced_search

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 35

Constrói sistema completo de busca avançada.

Returns:
    Resultados da construção

## Classes

### AdvancedSearchSystem

**Herança**: Nenhuma
**Atributos**: content_index, nav_graph, semantic_index, content_index, category_index, content_index, tag_index, content_index, keyword_index, semantic_index, metadata_index, content_index, similarity_matrix, semantic_index, doc_paths, keywords1, keywords2, keyword_similarity, tags1, tags2, tag_similarity, type_similarity, total_similarity, query_lower, results, content_index, results, tag_index, seen, unique_results, results, category_index, results, similarity_matrix, content_lower, query_lower, pos, start, end, snippet, report, report_file, report_path, results, metadata, title_match, tags_match, type_match, status_match, sections, links, code_blocks, content, words, word_freq, sorted_words, tags, keywords, metadata, doc_type, status, size, size_category, word_count, word_category, tag_similarity, content, title, score, content_matches, query_words, similarities, sorted_similarities, words, snippet, snippet, content, doc_path, full_path, similarity, word_matches, results, content_data, pos, content_data
**Métodos**: 19
**Linhas**: 619

Sistema de busca avançada semântica

#### __init__

**Parâmetros**: self, consolidated_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Inicializa o sistema de busca avançada.

Args:
    consolidated_dir: Diretório dos documentos consolidados

#### load_intelligent_navigation

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Carrega dados de navegação inteligente.

Returns:
    Dados de navegação inteligente

#### extract_document_content

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 56

Extrai conteúdo completo de um documento.

Args:
    file_path: Caminho para o documento
    
Returns:
    Conteúdo extraído do documento

#### build_content_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Constrói índice de conteúdo para busca textual.

#### build_semantic_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 32

Constrói índice semântico baseado em similaridade de conteúdo.

#### build_category_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Constrói índice por categorias.

#### build_tag_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Constrói índice por tags.

#### build_keyword_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Constrói índice por palavras-chave.

#### build_metadata_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 45

Constrói índice por metadados.

#### build_similarity_matrix

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Constrói matriz de similaridade entre documentos.

#### calculate_similarity

**Parâmetros**: self, doc1, doc2
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Calcula similaridade entre dois documentos.

Args:
    doc1: Dados do primeiro documento
    doc2: Dados do segundo documento
    
Returns:
    Score de similaridade (0-1)

#### search_by_text

**Parâmetros**: self, query, limit
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 50

Busca por texto nos documentos.

Args:
    query: Query de busca
    limit: Limite de resultados
    
Returns:
    Lista de resultados

#### search_by_tags

**Parâmetros**: self, tags, limit
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 32

Busca por tags.

Args:
    tags: Lista de tags para buscar
    limit: Limite de resultados
    
Returns:
    Lista de resultados

#### search_by_category

**Parâmetros**: self, category, subcategory, limit
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Busca por categoria.

Args:
    category: Categoria principal
    subcategory: Subcategoria (opcional)
    limit: Limite de resultados
    
Returns:
    Lista de resultados

#### search_similar

**Parâmetros**: self, doc_path, limit
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Busca documentos similares.

Args:
    doc_path: Caminho do documento de referência
    limit: Limite de resultados
    
Returns:
    Lista de documentos similares

#### extract_snippet

**Parâmetros**: self, content, query, max_length
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 41

Extrai snippet do conteúdo com a query destacada.

Args:
    content: Conteúdo do documento
    query: Query de busca
    max_length: Tamanho máximo do snippet
    
Returns:
    Snippet extraído

#### save_search_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Salva o índice de busca avançada.

#### generate_search_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Gera relatório do sistema de busca.

Returns:
    Caminho do relatório

#### build_advanced_search

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 35

Constrói sistema completo de busca avançada.

Returns:
    Resultados da construção

## Imports

.AdvancedsearcherModule, json, re, datetime.datetime, logging

## Uso

```python
# Exemplo de uso do módulo migrated_advanced_search_system
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:57
