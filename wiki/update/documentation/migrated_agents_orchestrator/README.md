# migrated_agents_orchestrator

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_agents_orchestrator
- **Caminho**: wiki\update\modules\agents\agent_orchestrator\migrated_agents_orchestrator.py
- **Linhas de código**: 618
- **Complexidade**: 55.00
- **Funções**: 16
- **Classes**: 1

## Funções

### integrate_with_module

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Integra o script com o módulo de destino.

### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Sem documentação.

### load_configuration

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 51

Carrega configurações do sistema

### analyze_dashboard

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Analisa o dashboard para identificar tarefas pendentes

### extract_pending_tasks

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 42

Extrai tarefas pendentes do dashboard

### determine_priority

**Parâmetros**: self, task_id, task_type
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Determina prioridade da tarefa

### assign_task_to_agent

**Parâmetros**: self, task
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Atribui tarefa ao agente apropriado

### execute_agent

**Parâmetros**: self, agent_name, task
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 37

Executa um agente específico

### _run_agent_thread

**Parâmetros**: self, agent_file, agent_name, task
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 57

Executa agente em thread separada

### execute_auto_commit

**Parâmetros**: self, agent_name, task
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Executa commit automático após tarefa concluída

### generate_commit_message

**Parâmetros**: self, agent_name, task
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 49

Gera mensagem de commit contextual

### update_dashboard_with_commit

**Parâmetros**: self, commit_hash, agent_name, task
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 33

Atualiza dashboard com hash do commit

### orchestrate_workflow

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 54

Orquestra workflow completo de agentes

### wait_for_agents_completion

**Parâmetros**: self, timeout
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Aguarda conclusão de todos os agentes

### generate_orchestration_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 46

Gera relatório de orquestração

### run

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Executa o Agents Orchestrator

## Classes

### AgentsOrchestrator

**Herança**: Nenhuma
**Atributos**: dashboard_file, pending_tasks, patterns, task_type, agent_mapping, assigned_agent, agent_config, agent_file, task_type, task_id, task_title, category_mapping, category, progress_info, commit_message, start_time, serializable_agent_results, serializable_running_agents, report, report_file, pending_tasks, matches, epic_id, thread, result, success, output, error, commit_message, result, current, target, progress, progress_info, dashboard_file, commit_info, updated_content, analysis, pending_tasks, priority_order, sorted_tasks, completed_agents, serializable_result, serializable_agent_info, success, content, commit_hash, content, agent_name, task_id, title, current_progress, target_progress, task_id, title
**Métodos**: 15
**Linhas**: 551

Sem documentação.

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Sem documentação.

#### load_configuration

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 51

Carrega configurações do sistema

#### analyze_dashboard

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Analisa o dashboard para identificar tarefas pendentes

#### extract_pending_tasks

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 42

Extrai tarefas pendentes do dashboard

#### determine_priority

**Parâmetros**: self, task_id, task_type
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Determina prioridade da tarefa

#### assign_task_to_agent

**Parâmetros**: self, task
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Atribui tarefa ao agente apropriado

#### execute_agent

**Parâmetros**: self, agent_name, task
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 37

Executa um agente específico

#### _run_agent_thread

**Parâmetros**: self, agent_file, agent_name, task
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 57

Executa agente em thread separada

#### execute_auto_commit

**Parâmetros**: self, agent_name, task
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Executa commit automático após tarefa concluída

#### generate_commit_message

**Parâmetros**: self, agent_name, task
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 49

Gera mensagem de commit contextual

#### update_dashboard_with_commit

**Parâmetros**: self, commit_hash, agent_name, task
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 33

Atualiza dashboard com hash do commit

#### orchestrate_workflow

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 54

Orquestra workflow completo de agentes

#### wait_for_agents_completion

**Parâmetros**: self, timeout
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Aguarda conclusão de todos os agentes

#### generate_orchestration_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 46

Gera relatório de orquestração

#### run

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Executa o Agents Orchestrator

## Imports

.AgentorchestratorModule, json, logging, subprocess, time, datetime.datetime, threading, queue, re

## Uso

```python
# Exemplo de uso do módulo migrated_agents_orchestrator
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:58

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

