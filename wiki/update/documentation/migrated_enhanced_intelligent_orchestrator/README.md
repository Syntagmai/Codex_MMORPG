# migrated_enhanced_intelligent_orchestrator

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_enhanced_intelligent_orchestrator
- **Caminho**: wiki\update\modules\agents\agent_orchestrator\migrated_enhanced_intelligent_orchestrator.py
- **Linhas de código**: 755
- **Complexidade**: 37.00
- **Funções**: 21
- **Classes**: 2

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Função principal para teste

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
**Linhas**: 107

Sem documentação.

### analyze_request

**Parâmetros**: self, user_request
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 45

Análise completa do pedido do usuário

### detect_file_extensions

**Parâmetros**: self, text
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Detecta extensões de arquivo no texto

### detect_context_patterns

**Parâmetros**: self, text
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Detecta padrões de contexto específicos

### detect_technologies

**Parâmetros**: self, text
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Detecta tecnologias mencionadas

### combine_analysis

**Parâmetros**: self, file_extensions, context_patterns, technologies
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Combina todas as análises

### analyze_complexity

**Parâmetros**: self, text, analysis
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Analisa complexidade baseada no contexto

### identify_primary_workflow

**Parâmetros**: self, analysis
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Identifica o workflow principal

### calculate_confidence

**Parâmetros**: self, analysis
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Calcula score de confiança da análise

### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 123

Sem documentação.

### orchestrate_request

**Parâmetros**: self, user_request
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Orquestra o pedido do usuário com análise melhorada

### select_agents

**Parâmetros**: self, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 33

Seleciona agentes baseado no contexto melhorado

### get_agent_role

**Parâmetros**: self, agent_id, workflow_type
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 49

Define o papel específico do agente no workflow

### execute_workflow

**Parâmetros**: self, agent_workflow
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 39

Executa o workflow com os agentes selecionados

### get_agents_for_phase

**Parâmetros**: self, phase, agents
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Identifica agentes responsáveis por cada fase

### simulate_phase_execution

**Parâmetros**: self, phase, agents
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Simula execução de uma fase

### report_phase_progress

**Parâmetros**: self, phase, agents, progress
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Reporta progresso da fase

### generate_progress_report

**Parâmetros**: self, execution_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 42

Gera relatório de progresso

### save_execution_results

**Parâmetros**: self, execution_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Salva resultados da execução

## Classes

### EnhancedContextAnalyzer

**Herança**: Nenhuma
**Atributos**: text, file_extensions, context_patterns, technologies, combined_analysis, complexity, primary_workflow, analysis_result, extensions, detected_patterns, detected_technologies, all_agents, all_workflows, agent_count, workflow_count, high_complexity_keywords, medium_complexity_keywords, high_count, medium_count, workflows, agent_count, workflow_count, base_score, keyword_matches, keyword_matches
**Métodos**: 9
**Linhas**: 274

Analisador de contexto melhorado com detecção de extensões de arquivo

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 107

Sem documentação.

#### analyze_request

**Parâmetros**: self, user_request
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 45

Análise completa do pedido do usuário

#### detect_file_extensions

**Parâmetros**: self, text
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Detecta extensões de arquivo no texto

#### detect_context_patterns

**Parâmetros**: self, text
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Detecta padrões de contexto específicos

#### detect_technologies

**Parâmetros**: self, text
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Detecta tecnologias mencionadas

#### combine_analysis

**Parâmetros**: self, file_extensions, context_patterns, technologies
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Combina todas as análises

#### analyze_complexity

**Parâmetros**: self, text, analysis
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Analisa complexidade baseada no contexto

#### identify_primary_workflow

**Parâmetros**: self, analysis
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Identifica o workflow principal

#### calculate_confidence

**Parâmetros**: self, analysis
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Calcula score de confiança da análise

### EnhancedIntelligentOrchestrator

**Herança**: Nenhuma
**Atributos**: context_analysis, agent_workflow, execution_results, progress_report, primary_workflow, workflow_config, selected_agents, agent_workflow, roles, execution_results, total_phases, phase_agent_mapping, agent_names, phase_actions, agent_names, report, agent_info, phase_agents, phase_result, progress, maps_dir, results_file
**Métodos**: 10
**Linhas**: 401

Orquestrador inteligente melhorado

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 123

Sem documentação.

#### orchestrate_request

**Parâmetros**: self, user_request
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Orquestra o pedido do usuário com análise melhorada

#### select_agents

**Parâmetros**: self, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 33

Seleciona agentes baseado no contexto melhorado

#### get_agent_role

**Parâmetros**: self, agent_id, workflow_type
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 49

Define o papel específico do agente no workflow

#### execute_workflow

**Parâmetros**: self, agent_workflow
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 39

Executa o workflow com os agentes selecionados

#### get_agents_for_phase

**Parâmetros**: self, phase, agents
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Identifica agentes responsáveis por cada fase

#### simulate_phase_execution

**Parâmetros**: self, phase, agents
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Simula execução de uma fase

#### report_phase_progress

**Parâmetros**: self, phase, agents, progress
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Reporta progresso da fase

#### generate_progress_report

**Parâmetros**: self, execution_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 42

Gera relatório de progresso

#### save_execution_results

**Parâmetros**: self, execution_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Salva resultados da execução

## Imports

.AgentorchestratorModule, os, json, datetime.datetime

## Uso

```python
# Exemplo de uso do módulo migrated_enhanced_intelligent_orchestrator
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:58
