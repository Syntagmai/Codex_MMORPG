# expand_wiki_comprehensive

## Descrição

Script para expansão abrangente da wiki do OTClient
Integra conteúdo do habdel e cria documentação completa

## Informações Técnicas

- **Módulo**: expand_wiki_comprehensive
- **Caminho**: wiki\update\expand_wiki_comprehensive.py
- **Linhas de código**: 447
- **Complexidade**: 24.00
- **Funções**: 13
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
**Linhas**: 89

Sem documentação.

### load_context_data

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Carrega dados de contexto detectado

### extract_section_content

**Parâmetros**: self, file_path, section_title
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Extrai conteúdo de uma seção específica

### extract_examples

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Extrai exemplos práticos do arquivo

### create_comprehensive_ui_guide

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Cria guia completo de UI integrando conteúdo do habdel

### create_lua_api_reference

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 53

Cria referência completa da API Lua

### create_system_guides

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Cria guias completos para cada sistema

### process_habdel_content

**Parâmetros**: self, content, original_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Processa conteúdo do habdel para formato da wiki

### create_development_guides

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Cria guias de desenvolvimento expandidos

### create_reference_documents

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Cria documentos de referência

### update_wiki_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 72

Atualiza o índice principal da wiki

### expand_wiki_comprehensive

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Expande a wiki de forma abrangente

## Classes

### WikiExpander

**Herança**: Nenhuma
**Atributos**: context_file, target_file, current_content, expanded_content, target_file, content, lua_api_file, best_practices_file, content, frontmatter, content, navigation, index_file, content, pattern, match, examples, code_pattern, code_matches, example_pattern, example_matches, habdel_path, sections, habdel_path, target_path, habdel_path, target_path, habdel_path, target_path, content, content, current_content, sections, lua_content, section_content, practices_content, processed_content, processed_content, processed_content, habdel_content, section_content, habdel_content, habdel_content, habdel_content
**Métodos**: 12
**Linhas**: 426

Sem documentação.

#### __init__

**Parâmetros**: self, wiki_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 89

Sem documentação.

#### load_context_data

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Carrega dados de contexto detectado

#### extract_section_content

**Parâmetros**: self, file_path, section_title
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Extrai conteúdo de uma seção específica

#### extract_examples

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Extrai exemplos práticos do arquivo

#### create_comprehensive_ui_guide

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Cria guia completo de UI integrando conteúdo do habdel

#### create_lua_api_reference

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 53

Cria referência completa da API Lua

#### create_system_guides

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Cria guias completos para cada sistema

#### process_habdel_content

**Parâmetros**: self, content, original_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Processa conteúdo do habdel para formato da wiki

#### create_development_guides

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Cria guias de desenvolvimento expandidos

#### create_reference_documents

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Cria documentos de referência

#### update_wiki_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 72

Atualiza o índice principal da wiki

#### expand_wiki_comprehensive

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Expande a wiki de forma abrangente

## Imports

os, json, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

## Uso

```python
# Exemplo de uso do módulo expand_wiki_comprehensive
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

