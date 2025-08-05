# update_wiki_maps

## Descrição

Script para atualização automática dos mapas JSON da wiki do OTClient
Atualiza: maps/tags_index.json, maps/wiki_map.json, maps/relationships.json
Usa contexto detectado automaticamente

## Informações Técnicas

- **Módulo**: update_wiki_maps
- **Caminho**: wiki\update\update_wiki_maps.py
- **Linhas de código**: 284
- **Complexidade**: 35.00
- **Funções**: 9
- **Classes**: 1

## Funções

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
**Linhas**: 26

Atualiza todos os arquivos JSON

## Classes

### WikiJSONUpdater

**Herança**: Nenhuma
**Atributos**: context_file, md_files, docs_dir, frontmatter, tags_index, all_tags, wiki_map, file_lower, tags_lower, relationships, md_files, docs_dir, frontmatter, frontmatter, category, frontmatter, content, parts, frontmatter_text, tags_match, status_match, aliases_match, title_match, tags_str, aliases_str
**Métodos**: 9
**Linhas**: 266

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
**Linhas**: 26

Atualiza todos os arquivos JSON

## Imports

os, json, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

## Uso

```python
# Exemplo de uso do módulo update_wiki_maps
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

