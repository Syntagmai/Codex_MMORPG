# update_habdel_index

## Descrição

Script para indexação da pasta habdel - Documentação Original e Planejamento
Atualiza: wiki/maps/habdel_index.json

## Informações Técnicas

- **Módulo**: update_habdel_index
- **Caminho**: wiki\update\update_habdel_index.py
- **Linhas de código**: 328
- **Complexidade**: 62.00
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

os, json, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

## Uso

```python
# Exemplo de uso do módulo update_habdel_index
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:52

## 🔗 **Links Automáticos**

> [!info] **Links Gerados Automaticamente**
> Estes links foram criados automaticamente pelo sistema de linkagem da categoria **Tools**

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]
- [[../maps/tools_index|Índice de Ferramentas]]
- [[../update/README|Scripts de Atualização]]

### **🧭 Navegação**
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]
- [[../maps/category_indices|Índices por Categoria]]
- [[../maps/relationships|Relacionamentos]]

### **📊 Métricas da Categoria**
- **Categoria**: Tools
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

