# migrated_progress_tracker_agent

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_progress_tracker_agent
- **Caminho**: wiki\update\modules\agents\agent_orchestrator\migrated_progress_tracker_agent.py
- **Linhas de código**: 537
- **Complexidade**: 38.00
- **Funções**: 17
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
**Linhas**: 20

Sem documentação.

### load_configuration

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Carrega configurações do sistema

### calculate_current_metrics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Calcula métricas atuais do sistema

### calculate_general_progress

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Calcula progresso geral do sistema

### calculate_epics_progress

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Calcula progresso das epics

### calculate_stories_progress

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Calcula progresso das stories

### calculate_agents_progress

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Calcula progresso dos agentes

### calculate_tasks_progress

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Calcula progresso das tasks

### calculate_roadmaps_progress

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Calcula progresso dos roadmaps

### calculate_planejamentos_progress

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Calcula progresso dos planejamentos

### calculate_velocity

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 40

Calcula velocidade de progresso

### calculate_trends

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 52

Calcula tendências de progresso

### generate_alerts

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Gera alertas baseados no conteúdo atual

### save_metrics

**Parâmetros**: self, metrics
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Salva métricas atuais

### generate_dashboard_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 63

Gera relatório de dashboard

### run

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 40

Executa o Progress Tracker Agent

## Classes

### ProgressTrackerAgent

**Herança**: Nenhuma
**Atributos**: dashboard_file, epics_progress, stories_progress, agentes_progress, tasks_progress, weights, general_progress, pattern, matches, total_progress, average_progress, completed_pattern, total_pattern, completed_matches, total_matches, completed_count, total_count, progress, active_pattern, total_pattern, active_matches, total_matches, active_count, total_count, progress, completed_pattern, pending_pattern, completed_matches, pending_matches, completed_count, total_count, progress, implemented_pattern, total_pattern, implemented_matches, total_matches, implemented_count, total_count, progress, active_pattern, total_pattern, active_matches, total_matches, active_count, total_count, progress, current_metrics, previous_metrics, current_time, previous_time, time_diff, progress_diff, current_velocity, recent_metrics, progress_values, alerts, blocked_pattern, blocked_matches, critical_pattern, critical_matches, current_metrics, report, metrics, recent_metrics, total_progress_diff, total_time_diff, average_velocity, average_velocity, trend, first_half, second_half, first_avg, second_avg, direction, variance, strength, last_value, prediction, recent_progress, metrics_file, history_file, current_metrics, report, report_file, content, trend, trend, direction, strength, prediction, prediction, direction, direction, strength, strength
**Métodos**: 16
**Linhas**: 474

Sem documentação.

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Sem documentação.

#### load_configuration

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Carrega configurações do sistema

#### calculate_current_metrics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Calcula métricas atuais do sistema

#### calculate_general_progress

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Calcula progresso geral do sistema

#### calculate_epics_progress

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Calcula progresso das epics

#### calculate_stories_progress

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Calcula progresso das stories

#### calculate_agents_progress

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Calcula progresso dos agentes

#### calculate_tasks_progress

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Calcula progresso das tasks

#### calculate_roadmaps_progress

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Calcula progresso dos roadmaps

#### calculate_planejamentos_progress

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Calcula progresso dos planejamentos

#### calculate_velocity

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 40

Calcula velocidade de progresso

#### calculate_trends

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 52

Calcula tendências de progresso

#### generate_alerts

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Gera alertas baseados no conteúdo atual

#### save_metrics

**Parâmetros**: self, metrics
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Salva métricas atuais

#### generate_dashboard_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 63

Gera relatório de dashboard

#### run

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 40

Executa o Progress Tracker Agent

## Imports

.AgentorchestratorModule, json, logging, re

## Uso

```python
# Exemplo de uso do módulo migrated_progress_tracker_agent
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:59

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

