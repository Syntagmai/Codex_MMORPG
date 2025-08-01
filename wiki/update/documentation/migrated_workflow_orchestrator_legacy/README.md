# migrated_workflow_orchestrator_legacy

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_workflow_orchestrator_legacy
- **Caminho**: wiki\update\modules\agents\agent_orchestrator\migrated_workflow_orchestrator_legacy.py
- **Linhas de código**: 461
- **Complexidade**: 34.00
- **Funções**: 14
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Função principal para teste do orquestrador

### integrate_with_module

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Integra o script com o módulo de destino.

### __init__

**Parâmetros**: self, workspace_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Sem documentação.

### execute_workflow

**Parâmetros**: self, module_name, config
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 83

Executa o workflow completo para um módulo

Args:
    module_name: Nome do módulo OTClient a processar
    config: Configurações opcionais do workflow
    
Returns:
    Resultados completos do workflow

### execute_analysis_phase

**Parâmetros**: self, module_name
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Executa fase de análise

### execute_generation_phase

**Parâmetros**: self, analysis_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 35

Executa fase de geração

### execute_testing_phase

**Parâmetros**: self, generation_results, analysis_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Executa fase de teste

### execute_learning_phase

**Parâmetros**: self, analysis_results, generation_results, test_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Executa fase de aprendizado

### generate_workflow_summary

**Parâmetros**: self, workflow_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 42

Gera resumo do workflow

### save_workflow_results

**Parâmetros**: self, workflow_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Salva resultados do workflow

### log_phase

**Parâmetros**: self, phase_name, module_name, status, duration, error
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Registra log de uma fase do workflow

### get_available_modules

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 2

Retorna lista de módulos disponíveis

### get_workflow_status

**Parâmetros**: self, workflow_id
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Obtém status de um workflow específico

### list_workflows

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Lista todos os workflows executados

## Classes

### WorkflowOrchestrator

**Herança**: Nenhuma
**Atributos**: workflow_results, start_time, start_time, start_time, start_time, summary, total_duration, phases_completed, workflow_id, module_name, results_file, log_file, log_entry, log_dir, workflows, log_dir, analysis_results, generation_results, test_results, available_modules, analysis_results, duration, variation_count, variations, generation_results, duration, variations, test_results, duration, learning_data, duration, gen_results, test_results, test_summary, learning_results, error_msg, duration, duration, duration, duration, file_path, file_path, workflow_data
**Métodos**: 12
**Linhas**: 369

Orquestrador principal do workflow de módulos OTClient

#### __init__

**Parâmetros**: self, workspace_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Sem documentação.

#### execute_workflow

**Parâmetros**: self, module_name, config
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 83

Executa o workflow completo para um módulo

Args:
    module_name: Nome do módulo OTClient a processar
    config: Configurações opcionais do workflow
    
Returns:
    Resultados completos do workflow

#### execute_analysis_phase

**Parâmetros**: self, module_name
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Executa fase de análise

#### execute_generation_phase

**Parâmetros**: self, analysis_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 35

Executa fase de geração

#### execute_testing_phase

**Parâmetros**: self, generation_results, analysis_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Executa fase de teste

#### execute_learning_phase

**Parâmetros**: self, analysis_results, generation_results, test_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Executa fase de aprendizado

#### generate_workflow_summary

**Parâmetros**: self, workflow_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 42

Gera resumo do workflow

#### save_workflow_results

**Parâmetros**: self, workflow_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Salva resultados do workflow

#### log_phase

**Parâmetros**: self, phase_name, module_name, status, duration, error
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Registra log de uma fase do workflow

#### get_available_modules

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 2

Retorna lista de módulos disponíveis

#### get_workflow_status

**Parâmetros**: self, workflow_id
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Obtém status de um workflow específico

#### list_workflows

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Lista todos os workflows executados

## Imports

.AgentorchestratorModule, os, sys, json, time, datetime.datetime

## Uso

```python
# Exemplo de uso do módulo migrated_workflow_orchestrator_legacy
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:59
