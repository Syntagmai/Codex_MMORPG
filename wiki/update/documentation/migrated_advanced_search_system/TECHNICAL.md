# Documentação Técnica - migrated_advanced_search_system

## Análise Estática

### Métricas de Código
- **Linhas de código**: 699
- **Complexidade ciclomática**: 62.00
- **Funções**: 21
- **Classes**: 1
- **Imports**: 5

### Análise de Complexidade
- **Nível**: Alto (Código complexo, considere refatoração)\n
### Estrutura de Dependências

#### Imports Externos
.AdvancedsearcherModule, json, re, datetime.datetime, logging

#### Hierarquia de Classes
- AdvancedSearchSystem (sem herança)\n
### Análise de Funções

#### Funções Principais
**main**
- Parâmetros: 0
- Linhas: 15
- Documentação: Sim

**integrate_with_module**
- Parâmetros: 0
- Linhas: 3
- Documentação: Sim

**__init__**
- Parâmetros: 2
- Linhas: 23
- Documentação: Sim

**load_intelligent_navigation**
- Parâmetros: 1
- Linhas: 14
- Documentação: Sim

**extract_document_content**
- Parâmetros: 2
- Linhas: 56
- Documentação: Sim

**build_content_index**
- Parâmetros: 1
- Linhas: 22
- Documentação: Sim

**build_semantic_index**
- Parâmetros: 1
- Linhas: 32
- Documentação: Sim

**build_category_index**
- Parâmetros: 1
- Linhas: 26
- Documentação: Sim

**build_tag_index**
- Parâmetros: 1
- Linhas: 23
- Documentação: Sim

**build_keyword_index**
- Parâmetros: 1
- Linhas: 27
- Documentação: Sim

**build_metadata_index**
- Parâmetros: 1
- Linhas: 45
- Documentação: Sim

**build_similarity_matrix**
- Parâmetros: 1
- Linhas: 22
- Documentação: Sim

**calculate_similarity**
- Parâmetros: 3
- Linhas: 34
- Documentação: Sim

**search_by_text**
- Parâmetros: 3
- Linhas: 50
- Documentação: Sim

**search_by_tags**
- Parâmetros: 3
- Linhas: 32
- Documentação: Sim

**search_by_category**
- Parâmetros: 4
- Linhas: 23
- Documentação: Sim

**search_similar**
- Parâmetros: 3
- Linhas: 28
- Documentação: Sim

**extract_snippet**
- Parâmetros: 4
- Linhas: 41
- Documentação: Sim

**save_search_index**
- Parâmetros: 1
- Linhas: 9
- Documentação: Sim

**generate_search_report**
- Parâmetros: 1
- Linhas: 38
- Documentação: Sim

**build_advanced_search**
- Parâmetros: 1
- Linhas: 35
- Documentação: Sim

### Recomendações

1. **Documentação**: Adicione docstrings para todas as funções e classes
2. **Complexidade**: Considere refatorar funções muito complexas
3. **Testes**: Implemente testes unitários para todas as funções
4. **Type Hints**: Adicione type hints para melhorar a legibilidade

### Histórico de Versões

- **v1.0**: Documentação inicial gerada automaticamente
- **Data**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Agente**: Documentation Agent

