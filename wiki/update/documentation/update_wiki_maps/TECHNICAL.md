# Documentação Técnica - update_wiki_maps

## Análise Estática

### Métricas de Código
- **Linhas de código**: 284
- **Complexidade ciclomática**: 35.00
- **Funções**: 9
- **Classes**: 1
- **Imports**: 8

### Análise de Complexidade
- **Nível**: Alto (Código complexo, considere refatoração)\n
### Estrutura de Dependências

#### Imports Externos
os, json, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

#### Hierarquia de Classes
- WikiJSONUpdater (sem herança)\n
### Análise de Funções

#### Funções Principais
**__init__**
- Parâmetros: 2
- Linhas: 10
- Documentação: Não

**load_context_data**
- Parâmetros: 1
- Linhas: 14
- Documentação: Sim

**scan_markdown_files**
- Parâmetros: 1
- Linhas: 11
- Documentação: Sim

**extract_frontmatter**
- Parâmetros: 2
- Linhas: 46
- Documentação: Sim

**generate_tags_index**
- Parâmetros: 1
- Linhas: 25
- Documentação: Sim

**generate_wiki_map**
- Parâmetros: 1
- Linhas: 53
- Documentação: Sim

**categorize_document**
- Parâmetros: 3
- Linhas: 36
- Documentação: Sim

**generate_relationships**
- Parâmetros: 1
- Linhas: 28
- Documentação: Sim

**update_all_json_files**
- Parâmetros: 1
- Linhas: 26
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

