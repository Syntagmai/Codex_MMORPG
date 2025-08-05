# optimize_maps_for_tokens

## Descrição

Script para otimização de tokens nos mapas JSON
Converte descrições para inglês (IA) mantendo tags em português (usuário)

## Informações Técnicas

- **Módulo**: optimize_maps_for_tokens
- **Caminho**: wiki\update\optimize_maps_for_tokens.py
- **Linhas de código**: 559
- **Complexidade**: 12.00
- **Funções**: 8
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
**Linhas**: 432

Sem documentação.

### translate_text

**Parâmetros**: self, text
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Traduz texto para inglês para otimizar tokens

### optimize_metadata

**Parâmetros**: self, metadata
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Otimiza metadados convertendo para inglês

### optimize_tags_index

**Parâmetros**: self, tags_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Otimiza tags_index.json

### optimize_wiki_map

**Parâmetros**: self, wiki_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Otimiza wiki_map.json

### optimize_relationships

**Parâmetros**: self, rel_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Otimiza relationships.json

### optimize_all_maps

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 40

Otimiza todos os mapas JSON

## Classes

### TokenOptimizer

**Herança**: Nenhuma
**Atributos**: optimized, optimized, optimized, optimized, tags_path, wiki_path, rel_path, text, optimized_tags, optimized_wiki, optimized_rel, tags_data, wiki_data, rel_data
**Métodos**: 7
**Linhas**: 539

Sem documentação.

#### __init__

**Parâmetros**: self, wiki_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 432

Sem documentação.

#### translate_text

**Parâmetros**: self, text
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Traduz texto para inglês para otimizar tokens

#### optimize_metadata

**Parâmetros**: self, metadata
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Otimiza metadados convertendo para inglês

#### optimize_tags_index

**Parâmetros**: self, tags_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Otimiza tags_index.json

#### optimize_wiki_map

**Parâmetros**: self, wiki_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Otimiza wiki_map.json

#### optimize_relationships

**Parâmetros**: self, rel_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Otimiza relationships.json

#### optimize_all_maps

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 40

Otimiza todos os mapas JSON

## Imports

json, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

## Uso

```python
# Exemplo de uso do módulo optimize_maps_for_tokens
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

