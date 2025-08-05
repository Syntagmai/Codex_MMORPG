# Documentação Técnica - auto_update_all_maps

## Análise Estática

### Métricas de Código
- **Linhas de código**: 276
- **Complexidade ciclomática**: 23.00
- **Funções**: 11
- **Classes**: 1
- **Imports**: 10

### Análise de Complexidade
- **Nível**: Alto (Código complexo, considere refatoração)\n
### Estrutura de Dependências

#### Imports Externos
os, sys, json, subprocess, time, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

#### Hierarquia de Classes
- AutoMapUpdater (sem herança)\n
### Análise de Funções

#### Funções Principais
**__init__**
- Parâmetros: 1
- Linhas: 21
- Documentação: Não

**load_context_data**
- Parâmetros: 1
- Linhas: 14
- Documentação: Sim

**get_context_scripts**
- Parâmetros: 1
- Linhas: 36
- Documentação: Sim

**get_context_maps**
- Parâmetros: 1
- Linhas: 30
- Documentação: Sim

**log**
- Parâmetros: 3
- Linhas: 3
- Documentação: Sim

**execute_script**
- Parâmetros: 2
- Linhas: 38
- Documentação: Sim

**validate_map**
- Parâmetros: 2
- Linhas: 23
- Documentação: Sim

**update_all_maps**
- Parâmetros: 1
- Linhas: 20
- Documentação: Sim

**generate_report**
- Parâmetros: 1
- Linhas: 22
- Documentação: Sim

**save_report**
- Parâmetros: 2
- Linhas: 7
- Documentação: Sim

**print_summary**
- Parâmetros: 1
- Linhas: 20
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

