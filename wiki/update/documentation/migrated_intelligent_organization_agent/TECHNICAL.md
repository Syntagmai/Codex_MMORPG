# Documentação Técnica - migrated_intelligent_organization_agent

## Análise Estática

### Métricas de Código
- **Linhas de código**: 984
- **Complexidade ciclomática**: 101.00
- **Funções**: 32
- **Classes**: 1
- **Imports**: 7

### Análise de Complexidade
- **Nível**: Alto (Código complexo, considere refatoração)\n
### Estrutura de Dependências

#### Imports Externos
.AgentorchestratorModule, shutil, re, datetime.datetime, datetime.timedelta, logging, argparse

#### Hierarquia de Classes
- IntelligentOrganizationAgent (sem herança)\n
### Análise de Funções

#### Funções Principais
**main**
- Parâmetros: 0
- Linhas: 45
- Documentação: Sim

**integrate_with_module**
- Parâmetros: 0
- Linhas: 3
- Documentação: Sim

**__init__**
- Parâmetros: 2
- Linhas: 91
- Documentação: Não

**detect_organization_issues**
- Parâmetros: 1
- Linhas: 39
- Documentação: Sim

**_detect_canary_integration_issues**
- Parâmetros: 1
- Linhas: 16
- Documentação: Sim

**_detect_missing_integration_structure**
- Parâmetros: 1
- Linhas: 23
- Documentação: Sim

**_is_canary_integration_file**
- Parâmetros: 2
- Linhas: 11
- Documentação: Sim

**_is_in_correct_canary_location**
- Parâmetros: 2
- Linhas: 16
- Documentação: Sim

**organize_canary_integration_files**
- Parâmetros: 1
- Linhas: 38
- Documentação: Sim

**_create_canary_integration_structure**
- Parâmetros: 1
- Linhas: 25
- Documentação: Sim

**_organize_canary_file**
- Parâmetros: 2
- Linhas: 36
- Documentação: Sim

**validate_canary_integration_structure**
- Parâmetros: 1
- Linhas: 54
- Documentação: Sim

**is_in_wrong_location**
- Parâmetros: 2
- Linhas: 13
- Documentação: Sim

**is_obsolete**
- Parâmetros: 2
- Linhas: 13
- Documentação: Sim

**is_temp_file**
- Parâmetros: 2
- Linhas: 5
- Documentação: Sim

**has_category**
- Parâmetros: 2
- Linhas: 3
- Documentação: Sim

**find_duplicates**
- Parâmetros: 2
- Linhas: 16
- Documentação: Sim

**find_unorganized_reports**
- Parâmetros: 1
- Linhas: 10
- Documentação: Sim

**detect_file_context**
- Parâmetros: 2
- Linhas: 6
- Documentação: Sim

**is_in_reports_folder**
- Parâmetros: 2
- Linhas: 2
- Documentação: Sim

**is_in_tasks_folder**
- Parâmetros: 2
- Linhas: 2
- Documentação: Sim

**is_in_recipes_folder**
- Parâmetros: 2
- Linhas: 2
- Documentação: Sim

**is_in_archives_folder**
- Parâmetros: 2
- Linhas: 2
- Documentação: Sim

**organize_by_category**
- Parâmetros: 1
- Linhas: 41
- Documentação: Sim

**organize_by_date**
- Parâmetros: 1
- Linhas: 47
- Documentação: Sim

**extract_date_from_file**
- Parâmetros: 2
- Linhas: 23
- Documentação: Sim

**cleanup_temp_files**
- Parâmetros: 1
- Linhas: 22
- Documentação: Sim

**remove_duplicates**
- Parâmetros: 1
- Linhas: 24
- Documentação: Sim

**create_organization_structure**
- Parâmetros: 1
- Linhas: 50
- Documentação: Sim

**generate_organization_report**
- Parâmetros: 2
- Linhas: 82
- Documentação: Sim

**run_full_organization**
- Parâmetros: 1
- Linhas: 55
- Documentação: Sim

**_is_ignored**
- Parâmetros: 2
- Linhas: 37
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

