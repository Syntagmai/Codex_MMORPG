# migrated_integrated_navigation_agent

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_integrated_navigation_agent
- **Caminho**: wiki\update\modules\agents\agent_orchestrator\migrated_integrated_navigation_agent.py
- **Linhas de código**: 468
- **Complexidade**: 43.00
- **Funções**: 12
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 33

Função principal para teste do agente integrado

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
**Linhas**: 18

Sem documentação.

### navigate

**Parâmetros**: self, query, context, strategy
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 54

Navegação integrada com múltiplas estratégias

Estratégias:
- 'json': Navegação JSON tradicional
- 'graph': Navegação por grafos
- 'hybrid': Combinação inteligente

### json_navigation

**Parâmetros**: self, query, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 41

Navegação JSON tradicional

### graph_navigation

**Parâmetros**: self, query, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Navegação por grafos

### hybrid_navigation

**Parâmetros**: self, query, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Navegação híbrida - combina JSON e grafos

### integrate_results

**Parâmetros**: self, json_results, graph_results, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 54

Integra resultados de JSON e grafos

### calculate_confidence_scores

**Parâmetros**: self, integrated_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Calcula scores de confiança para os resultados

### generate_suggestions

**Parâmetros**: self, query, context, results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 49

Gera sugestões de navegação

### get_performance_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Gera relatório de performance

### optimize_navigation

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Otimiza a navegação integrada

## Classes

### IntegratedNavigationAgent

**Herança**: Nenhuma
**Atributos**: start_time, cache_key, result, execution_time, results, tags_file, wiki_map_file, results, related_nodes, results, json_results, graph_results, integrated, integrated, json_files, graph_nodes, scores, total_confidence, json_results, graph_results, hybrid_results, suggestions, total_queries, cache_hit_rate, optimization_result, json_opt, graph_opt, node_data, target_node, optimal_path, node_id, confidence, old_cache, tags_data, wiki_data, path, graph_info, path, file_name, file_name, cache_time
**Métodos**: 10
**Linhas**: 382

Agente que integra navegação JSON e grafos

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 18

Sem documentação.

#### navigate

**Parâmetros**: self, query, context, strategy
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 54

Navegação integrada com múltiplas estratégias

Estratégias:
- 'json': Navegação JSON tradicional
- 'graph': Navegação por grafos
- 'hybrid': Combinação inteligente

#### json_navigation

**Parâmetros**: self, query, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 41

Navegação JSON tradicional

#### graph_navigation

**Parâmetros**: self, query, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Navegação por grafos

#### hybrid_navigation

**Parâmetros**: self, query, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Navegação híbrida - combina JSON e grafos

#### integrate_results

**Parâmetros**: self, json_results, graph_results, context
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 54

Integra resultados de JSON e grafos

#### calculate_confidence_scores

**Parâmetros**: self, integrated_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Calcula scores de confiança para os resultados

#### generate_suggestions

**Parâmetros**: self, query, context, results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 49

Gera sugestões de navegação

#### get_performance_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Gera relatório de performance

#### optimize_navigation

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Otimiza a navegação integrada

## Imports

.AgentorchestratorModule, json, time, datetime.datetime

## Uso

```python
# Exemplo de uso do módulo migrated_integrated_navigation_agent
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

