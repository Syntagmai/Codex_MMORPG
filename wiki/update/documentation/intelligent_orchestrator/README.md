# intelligent_orchestrator

## Descrição

Sistema de Orquestração Inteligente para Agentes BMAD
Detecta automaticamente o contexto e coordena agentes sem comandos manuais

## Informações Técnicas

- **Módulo**: intelligent_orchestrator
- **Caminho**: wiki\update\intelligent_orchestrator.py
- **Linhas de código**: 517
- **Complexidade**: 31.00
- **Funções**: 13
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Função principal para teste do sistema

### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 161

Sem documentação.

### analyze_context

**Parâmetros**: self, user_request
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 41

Analisa o contexto do pedido do usuário

### analyze_complexity

**Parâmetros**: self, text, keywords
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Analisa a complexidade baseada no contexto

### identify_primary_workflow

**Parâmetros**: self, keywords, workflows
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Identifica o workflow principal baseado nas palavras-chave

### select_agents

**Parâmetros**: self, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Seleciona agentes baseado no contexto

### get_agent_role

**Parâmetros**: self, agent_id, workflow_type
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Define o papel específico do agente no workflow

### execute_workflow

**Parâmetros**: self, agent_workflow
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 47

Executa o workflow coordenado

### get_agents_for_phase

**Parâmetros**: self, phase, agents
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Identifica agentes responsáveis por cada fase

### report_phase_progress

**Parâmetros**: self, phase, agents, progress
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 4

Reporta progresso da fase

### generate_progress_report

**Parâmetros**: self, execution_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Gera relatório de progresso em tempo real

### orchestrate_request

**Parâmetros**: self, user_request
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Orquestra automaticamente o pedido do usuário

### save_execution_results

**Parâmetros**: self, execution_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Salva resultados da execução

## Classes

### IntelligentOrchestrator

**Herança**: Nenhuma
**Atributos**: text, detected_keywords, detected_agents, detected_workflows, complexity, primary_workflow, context_analysis, performance_keywords, performance_count, feature_keywords, feature_count, bug_keywords, bug_count, primary_workflow, workflow_config, selected_agents, agent_workflow, roles, start_time, execution_results, phase_agent_mapping, agent_names, workflow, report, context, agent_workflow, execution_results, progress_report, agent_info, phase_agents, phase_result, progress, agent_names, history_file, execution_record, history, history
**Métodos**: 12
**Linhas**: 472

Sistema de orquestração inteligente para agentes BMAD

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 161

Sem documentação.

#### analyze_context

**Parâmetros**: self, user_request
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 41

Analisa o contexto do pedido do usuário

#### analyze_complexity

**Parâmetros**: self, text, keywords
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Analisa a complexidade baseada no contexto

#### identify_primary_workflow

**Parâmetros**: self, keywords, workflows
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Identifica o workflow principal baseado nas palavras-chave

#### select_agents

**Parâmetros**: self, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Seleciona agentes baseado no contexto

#### get_agent_role

**Parâmetros**: self, agent_id, workflow_type
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Define o papel específico do agente no workflow

#### execute_workflow

**Parâmetros**: self, agent_workflow
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 47

Executa o workflow coordenado

#### get_agents_for_phase

**Parâmetros**: self, phase, agents
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Identifica agentes responsáveis por cada fase

#### report_phase_progress

**Parâmetros**: self, phase, agents, progress
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 4

Reporta progresso da fase

#### generate_progress_report

**Parâmetros**: self, execution_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Gera relatório de progresso em tempo real

#### orchestrate_request

**Parâmetros**: self, user_request
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Orquestra automaticamente o pedido do usuário

#### save_execution_results

**Parâmetros**: self, execution_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Salva resultados da execução

## Imports

json, re, time, datetime.datetime, typing.Dict, typing.List, typing.Any, typing.Optional

## Uso

```python
# Exemplo de uso do módulo intelligent_orchestrator
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:51
