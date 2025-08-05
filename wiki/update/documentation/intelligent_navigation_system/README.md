# intelligent_navigation_system

## Descrição

Sistema de Navegação Inteligente Otimizada
==========================================

Este script implementa navegação inteligente otimizada entre documentos consolidados
com busca semântica e links contextuais.

Autor: Sistema BMAD - Navigation Agent
Data: 2025-08-01

## Informações Técnicas

- **Módulo**: intelligent_navigation_system
- **Caminho**: wiki\update\intelligent_navigation_system.py
- **Linhas de código**: 496
- **Complexidade**: 55.00
- **Funções**: 14
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Função principal do script.

### __init__

**Parâmetros**: self, consolidated_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Inicializa o sistema de navegação inteligente.

Args:
    consolidated_dir: Diretório dos documentos consolidados

### load_navigation_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Carrega o índice de navegação existente.

Returns:
    Dados do índice de navegação

### analyze_document_content

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 42

Analisa o conteúdo de um documento para extrair informações de navegação.

Args:
    file_path: Caminho para o documento
    
Returns:
    Informações extraídas do documento

### build_navigation_graph

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Constrói grafo de navegação entre documentos.

### create_semantic_links

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 32

Cria links semânticos entre documentos relacionados.

### create_contextual_paths

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 49

Cria caminhos contextuais entre documentos.

### create_quick_access

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 41

Cria sistema de acesso rápido.

### create_search_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 40

Cria índice de busca para navegação rápida.

### create_breadcrumbs

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Cria sistema de breadcrumbs para navegação hierárquica.

### create_related_documents

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Cria sistema de documentos relacionados.

### generate_navigation_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 40

Gera relatório de navegação inteligente.

Returns:
    Caminho do relatório

### save_intelligent_navigation

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Salva o sistema de navegação inteligente.

### optimize_navigation

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 47

Executa otimização completa da navegação.

Returns:
    Resultados da otimização

## Classes

### IntelligentNavigationSystem

**Herança**: Nenhuma
**Atributos**: graph, semantic_links, tag_groups, keyword_groups, contextual_paths, common_paths, quick_access, all_docs, popular_docs, essential_keywords, search_index, breadcrumbs, related_docs, report, report_file, report_path, results, title_match, title, tags_match, tags, internal_links, keywords, keywords, category_dir, existing_docs, title_lower, content, tags, full_path, subcategory_dir, title, doc_path, doc_tags, doc_info, other_doc_path, other_tags
**Métodos**: 13
**Linhas**: 447

Sistema de navegação inteligente otimizada

#### __init__

**Parâmetros**: self, consolidated_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Inicializa o sistema de navegação inteligente.

Args:
    consolidated_dir: Diretório dos documentos consolidados

#### load_navigation_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Carrega o índice de navegação existente.

Returns:
    Dados do índice de navegação

#### analyze_document_content

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 42

Analisa o conteúdo de um documento para extrair informações de navegação.

Args:
    file_path: Caminho para o documento
    
Returns:
    Informações extraídas do documento

#### build_navigation_graph

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Constrói grafo de navegação entre documentos.

#### create_semantic_links

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 32

Cria links semânticos entre documentos relacionados.

#### create_contextual_paths

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 49

Cria caminhos contextuais entre documentos.

#### create_quick_access

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 41

Cria sistema de acesso rápido.

#### create_search_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 40

Cria índice de busca para navegação rápida.

#### create_breadcrumbs

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Cria sistema de breadcrumbs para navegação hierárquica.

#### create_related_documents

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Cria sistema de documentos relacionados.

#### generate_navigation_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 40

Gera relatório de navegação inteligente.

Returns:
    Caminho do relatório

#### save_intelligent_navigation

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Salva o sistema de navegação inteligente.

#### optimize_navigation

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 47

Executa otimização completa da navegação.

Returns:
    Resultados da otimização

## Imports

json, os, re, pathlib.Path, typing.Dict, typing.List, typing.Any, typing.Optional, typing.Tuple, datetime.datetime, logging

## Uso

```python
# Exemplo de uso do módulo intelligent_navigation_system
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

