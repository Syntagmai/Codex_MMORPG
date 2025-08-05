# migrated_dashboard_agent

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_dashboard_agent
- **Caminho**: wiki\update\modules\agents\agent_orchestrator\migrated_dashboard_agent.py
- **Linhas de código**: 610
- **Complexidade**: 23.00
- **Funções**: 11
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Função principal

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
**Linhas**: 17

Sem documentação.

### load_configuration

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Carrega configurações do sistema de dashboard

### load_metrics_data

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Carrega dados de métricas

### generate_html_dashboard

**Parâmetros**: self, data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 301

Gera dashboard HTML interativo

### generate_markdown_dashboard

**Parâmetros**: self, data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 107

Gera dashboard em Markdown

### save_dashboard

**Parâmetros**: self, html_content, markdown_content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Salva dashboards em arquivos

### run

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Executa o agente de dashboard

### get_status_color

**Parâmetros**: value, thresholds
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Sem documentação.

### get_status_emoji

**Parâmetros**: value, thresholds
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Sem documentação.

## Classes

### DashboardAgent

**Herança**: Nenhuma
**Atributos**: data, system_metrics_file, kpis_file, history_file, system_metrics, kpis, cpu_usage, memory_usage, disk_usage, overall_score, cpu_color, memory_color, disk_color, score_color, html, alerts, system_metrics, kpis, cpu_usage, memory_usage, disk_usage, overall_score, cpu_status, memory_status, disk_status, score_status, markdown, alerts, html_file, md_file, data, html_dashboard, markdown_dashboard, success, alert_class, emoji
**Métodos**: 9
**Linhas**: 542

Sem documentação.

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Sem documentação.

#### load_configuration

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Carrega configurações do sistema de dashboard

#### load_metrics_data

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Carrega dados de métricas

#### generate_html_dashboard

**Parâmetros**: self, data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 301

Gera dashboard HTML interativo

#### generate_markdown_dashboard

**Parâmetros**: self, data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 107

Gera dashboard em Markdown

#### save_dashboard

**Parâmetros**: self, html_content, markdown_content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Salva dashboards em arquivos

#### run

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Executa o agente de dashboard

#### get_status_color

**Parâmetros**: value, thresholds
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Sem documentação.

#### get_status_emoji

**Parâmetros**: value, thresholds
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Sem documentação.

## Imports

.AgentorchestratorModule, json, logging

## Uso

```python
# Exemplo de uso do módulo migrated_dashboard_agent
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

