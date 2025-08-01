# migrated_migrated_knowledge_consolidation_system

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_migrated_knowledge_consolidation_system
- **Caminho**: wiki\update\modules\maps\map_updater\migrated_migrated_knowledge_consolidation_system.py
- **Linhas de código**: 448
- **Complexidade**: 48.00
- **Funções**: 10
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Função principal do script.

### integrate_with_module

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Integra o script com o módulo de destino.

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
**Linhas**: 54

Inicializa o sistema de consolidação.

Args:
    wiki_dir: Diretório da wiki

### scan_documents

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 53

Escaneia todos os documentos disponíveis.

Returns:
    Dicionário com documentos organizados por categoria

### categorize_documents

**Parâmetros**: self, documents
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 52

Categoriza documentos por tipo de conteúdo.

Args:
    documents: Documentos escaneados
    
Returns:
    Documentos categorizados

### create_consolidation_structure

**Parâmetros**: self, categorized_docs
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 45

Cria estrutura de consolidação organizada.

Args:
    categorized_docs: Documentos categorizados

### create_navigation_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 48

Cria índice de navegação para a wiki consolidada.

### create_consolidation_report

**Parâmetros**: self, documents, navigation_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Cria relatório de consolidação.

Args:
    documents: Documentos originais
    navigation_data: Dados de navegação
    
Returns:
    Caminho do relatório

### consolidate_knowledge

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Executa consolidação completa do conhecimento.

Returns:
    Resultados da consolidação

## Classes

### KnowledgeConsolidationSystem

**Herança**: Nenhuma
**Atributos**: documents, categorized, mapping, navigation_data, navigation_file, report, report_file, documents, categorized_docs, navigation_data, report_path, results, path, filename, path, category_dir, category_dir, subcategory_dir, target_dir, source_path, target_path, subcategory_dir, files
**Métodos**: 7
**Linhas**: 341

Sistema de consolidação automática de conhecimento

#### __init__

**Parâmetros**: self, wiki_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 54

Inicializa o sistema de consolidação.

Args:
    wiki_dir: Diretório da wiki

#### scan_documents

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 53

Escaneia todos os documentos disponíveis.

Returns:
    Dicionário com documentos organizados por categoria

#### categorize_documents

**Parâmetros**: self, documents
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 52

Categoriza documentos por tipo de conteúdo.

Args:
    documents: Documentos escaneados
    
Returns:
    Documentos categorizados

#### create_consolidation_structure

**Parâmetros**: self, categorized_docs
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 45

Cria estrutura de consolidação organizada.

Args:
    categorized_docs: Documentos categorizados

#### create_navigation_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 48

Cria índice de navegação para a wiki consolidada.

#### create_consolidation_report

**Parâmetros**: self, documents, navigation_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Cria relatório de consolidação.

Args:
    documents: Documentos originais
    navigation_data: Dados de navegação
    
Returns:
    Caminho do relatório

#### consolidate_knowledge

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Executa consolidação completa do conhecimento.

Returns:
    Resultados da consolidação

## Imports

.MapupdaterModule, .KnowledgeconsolidatorModule, json, shutil, datetime.datetime, logging

## Uso

```python
# Exemplo de uso do módulo migrated_migrated_knowledge_consolidation_system
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:55
