# migrated_update_habdel_index

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_update_habdel_index
- **Caminho**: wiki\update\modules\maps\habdel_indexer\migrated_update_habdel_index.py
- **Linhas de código**: 358
- **Complexidade**: 64.00
- **Funções**: 15
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Função principal

### integrate_with_module

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Integra o script com o módulo de destino.

### __init__

**Parâmetros**: self, project_root
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Sem documentação.

### scan_habdel_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Escaneia todos os arquivos da pasta habdel

### extract_story_info

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 78

Extrai informações de story de um arquivo

### extract_title

**Parâmetros**: self, content, file_stem
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Extrai título do conteúdo

### extract_description

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Extrai descrição do conteúdo

### determine_status

**Parâmetros**: self, content, file_name
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Determina status baseado no conteúdo

### extract_tags

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Extrai tags do conteúdo

### categorize_stories

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Categoriza as stories

### generate_statistics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Gera estatísticas da pasta habdel

### generate_search_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Gera índice de busca

### generate_habdel_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Gera o índice completo da pasta habdel

### save_index

**Parâmetros**: self, habdel_index, output_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Salva o índice em arquivo JSON

### update_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Atualiza o índice da pasta habdel

## Classes

### HabdelIndexer

**Herança**: Nenhuma
**Atributos**: habdel_files, lines, lines, content_lower, tags, tag_patterns, stats, status_counts, search_index, habdel_files, statistics, search_index, habdel_index, habdel_index, file_name, file_stem, story_id, story_category, patterns, title, description, status, tags, lines, size, story_info, line, line, matches, category, status, title, status, category, story_info, output_path, content, match, tag_lower, story_id, story_category, story_category, story_category, story_category, story_category, story_category, story_category
**Métodos**: 13
**Linhas**: 295

Sem documentação.

#### __init__

**Parâmetros**: self, project_root
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Sem documentação.

#### scan_habdel_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Escaneia todos os arquivos da pasta habdel

#### extract_story_info

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 78

Extrai informações de story de um arquivo

#### extract_title

**Parâmetros**: self, content, file_stem
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Extrai título do conteúdo

#### extract_description

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Extrai descrição do conteúdo

#### determine_status

**Parâmetros**: self, content, file_name
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Determina status baseado no conteúdo

#### extract_tags

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Extrai tags do conteúdo

#### categorize_stories

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Categoriza as stories

#### generate_statistics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Gera estatísticas da pasta habdel

#### generate_search_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Gera índice de busca

#### generate_habdel_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Gera o índice completo da pasta habdel

#### save_index

**Parâmetros**: self, habdel_index, output_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Salva o índice em arquivo JSON

#### update_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Atualiza o índice da pasta habdel

## Imports

.HabdelindexerModule, json, re, datetime.datetime

## Uso

```python
# Exemplo de uso do módulo migrated_update_habdel_index
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:54
