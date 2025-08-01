# Documentação Técnica - navigation_index_generator

## Análise Estática

### Métricas de Código
- **Linhas de código**: 657
- **Complexidade ciclomática**: 62.00
- **Funções**: 15
- **Classes**: 1
- **Imports**: 9

### Análise de Complexidade
- **Nível**: Alto (Código complexo, considere refatoração)\n
### Estrutura de Dependências

#### Imports Externos
json, logging, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Optional, typing.Tuple

#### Hierarquia de Classes
- NavigationIndexGenerator (sem herança)\n
### Análise de Funções

#### Funções Principais
**__init__**
- Parâmetros: 1
- Linhas: 18
- Documentação: Não

**scan_all_documents**
- Parâmetros: 1
- Linhas: 56
- Documentação: Sim

**extract_document_info**
- Parâmetros: 3
- Linhas: 61
- Documentação: Sim

**extract_frontmatter**
- Parâmetros: 2
- Linhas: 26
- Documentação: Sim

**extract_title**
- Parâmetros: 2
- Linhas: 6
- Documentação: Sim

**extract_story_id**
- Parâmetros: 3
- Linhas: 16
- Documentação: Sim

**categorize_document**
- Parâmetros: 2
- Linhas: 15
- Documentação: Sim

**categorize_size**
- Parâmetros: 2
- Linhas: 9
- Documentação: Sim

**extract_keywords**
- Parâmetros: 2
- Linhas: 21
- Documentação: Sim

**create_alphabetical_index**
- Parâmetros: 2
- Linhas: 74
- Documentação: Sim

**create_categorical_index**
- Parâmetros: 2
- Linhas: 87
- Documentação: Sim

**create_story_based_index**
- Parâmetros: 2
- Linhas: 91
- Documentação: Sim

**create_search_index**
- Parâmetros: 2
- Linhas: 71
- Documentação: Sim

**save_indexes**
- Parâmetros: 2
- Linhas: 28
- Documentação: Sim

**run**
- Parâmetros: 1
- Linhas: 23
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

