# Documentação Técnica - migrated_agents_orchestrator

## Análise Estática

### Métricas de Código
- **Linhas de código**: 618
- **Complexidade ciclomática**: 55.00
- **Funções**: 16
- **Classes**: 1
- **Imports**: 9

### Análise de Complexidade
- **Nível**: Alto (Código complexo, considere refatoração)\n
### Estrutura de Dependências

#### Imports Externos
.AgentorchestratorModule, json, logging, subprocess, time, datetime.datetime, threading, queue, re

#### Hierarquia de Classes
- AgentsOrchestrator (sem herança)\n
### Análise de Funções

#### Funções Principais
**integrate_with_module**
- Parâmetros: 0
- Linhas: 3
- Documentação: Sim

**__init__**
- Parâmetros: 1
- Linhas: 24
- Documentação: Não

**load_configuration**
- Parâmetros: 1
- Linhas: 51
- Documentação: Sim

**analyze_dashboard**
- Parâmetros: 1
- Linhas: 22
- Documentação: Sim

**extract_pending_tasks**
- Parâmetros: 2
- Linhas: 42
- Documentação: Sim

**determine_priority**
- Parâmetros: 3
- Linhas: 20
- Documentação: Sim

**assign_task_to_agent**
- Parâmetros: 2
- Linhas: 20
- Documentação: Sim

**execute_agent**
- Parâmetros: 3
- Linhas: 37
- Documentação: Sim

**_run_agent_thread**
- Parâmetros: 4
- Linhas: 57
- Documentação: Sim

**execute_auto_commit**
- Parâmetros: 3
- Linhas: 29
- Documentação: Sim

**generate_commit_message**
- Parâmetros: 3
- Linhas: 49
- Documentação: Sim

**update_dashboard_with_commit**
- Parâmetros: 4
- Linhas: 33
- Documentação: Sim

**orchestrate_workflow**
- Parâmetros: 1
- Linhas: 54
- Documentação: Sim

**wait_for_agents_completion**
- Parâmetros: 2
- Linhas: 21
- Documentação: Sim

**generate_orchestration_report**
- Parâmetros: 1
- Linhas: 46
- Documentação: Sim

**run**
- Parâmetros: 1
- Linhas: 17
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

