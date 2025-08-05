# habdel_wiki_integration

## Descrição

Habdel Wiki Integration Script

Este script integra a documentação habdel com a wiki principal do OTClient,
criando links, índices e navegação unificada.

## Informações Técnicas

- **Módulo**: habdel_wiki_integration
- **Caminho**: wiki\update\habdel_wiki_integration.py
- **Linhas de código**: 499
- **Complexidade**: 61.00
- **Funções**: 15
- **Classes**: 1

## Funções

### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 50

Sem documentação.

### analyze_habdel_structure

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Analisa a estrutura da documentação habdel

### determine_category

**Parâmetros**: self, filename
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Determina a categoria do arquivo baseado no nome

### extract_story_info

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Extrai informações da story do arquivo

### extract_title

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Extrai título do conteúdo

### extract_status

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Extrai status do conteúdo

### analyze_wiki_structure

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Analisa a estrutura da wiki principal

### determine_wiki_category

**Parâmetros**: self, filename
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Determina a categoria do arquivo da wiki

### create_integration_index

**Parâmetros**: self, habdel_structure, wiki_structure
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 122

Cria índice de integração entre habdel e wiki

### get_category_emoji

**Parâmetros**: self, category
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Retorna emoji para categoria

### get_category_name

**Parâmetros**: self, category
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Retorna nome completo da categoria

### get_status_emoji

**Parâmetros**: self, status
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Retorna emoji para status

### create_navigation_links

**Parâmetros**: self, habdel_structure
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 71

Cria links de navegação para arquivos habdel

### save_integration_files

**Parâmetros**: self, habdel_structure, wiki_structure
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Salva arquivos de integração

### run

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Executa a integração habdel-wiki

## Classes

### HabdelWikiIntegration

**Herança**: Nenhuma
**Atributos**: structure, lines, structure, index_content, emojis, names, emojis, navigation_content, story_ids, saved_files, integration_index, integration_file, navigation_guide, navigation_file, story_patterns, file, story_info, status_emoji, habdel_structure, wiki_structure, saved_files, category, story_info, content, match, category, story_info, status_emoji, wiki_file, story_info, status_emoji
**Métodos**: 15
**Linhas**: 473

Sem documentação.

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 50

Sem documentação.

#### analyze_habdel_structure

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Analisa a estrutura da documentação habdel

#### determine_category

**Parâmetros**: self, filename
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Determina a categoria do arquivo baseado no nome

#### extract_story_info

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Extrai informações da story do arquivo

#### extract_title

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Extrai título do conteúdo

#### extract_status

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Extrai status do conteúdo

#### analyze_wiki_structure

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Analisa a estrutura da wiki principal

#### determine_wiki_category

**Parâmetros**: self, filename
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Determina a categoria do arquivo da wiki

#### create_integration_index

**Parâmetros**: self, habdel_structure, wiki_structure
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 122

Cria índice de integração entre habdel e wiki

#### get_category_emoji

**Parâmetros**: self, category
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Retorna emoji para categoria

#### get_category_name

**Parâmetros**: self, category
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Retorna nome completo da categoria

#### get_status_emoji

**Parâmetros**: self, status
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Retorna emoji para status

#### create_navigation_links

**Parâmetros**: self, habdel_structure
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 71

Cria links de navegação para arquivos habdel

#### save_integration_files

**Parâmetros**: self, habdel_structure, wiki_structure
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Salva arquivos de integração

#### run

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Executa a integração habdel-wiki

## Imports

json, logging, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Optional, typing.Tuple

## Uso

```python
# Exemplo de uso do módulo habdel_wiki_integration
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:51

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

