# migrated_data_collector

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_data_collector
- **Caminho**: wiki\update\modules\tools\git_automation\migrated_data_collector.py
- **Linhas de código**: 467
- **Complexidade**: 28.00
- **Funções**: 15
- **Classes**: 2

## Funções

### integrate_with_module

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Integra o script com o módulo de destino.

### __init__

**Parâmetros**: self, data_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Sem documentação.

### init_database

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 62

Inicializa banco de dados SQLite

### generate_interaction_id

**Parâmetros**: self, user_request, timestamp
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Gera ID único para uma interação

### save_interaction

**Parâmetros**: self, interaction_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 53

Salva uma nova interação no sistema

### _calculate_complexity

**Parâmetros**: self, interaction_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Calcula score de complexidade da interação

### _save_json_backup

**Parâmetros**: self, record
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Salva backup em formato JSON

### get_interaction

**Parâmetros**: self, interaction_id
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Recupera uma interação específica

### get_interactions

**Parâmetros**: self, limit, offset, filters
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 39

Recupera múltiplas interações com filtros

### _row_to_dict

**Parâmetros**: self, row, description
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Converte linha do banco em dicionário

### get_total_interactions

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Retorna total de interações no sistema

### get_interaction_stats

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 65

Retorna estatísticas das interações

### add_feedback

**Parâmetros**: self, interaction_id, feedback_text, feedback_score
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Adiciona feedback a uma interação

### cleanup_old_data

**Parâmetros**: self, days_to_keep
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Remove dados antigos do sistema

### _cleanup_old_json_files

**Parâmetros**: self, days_to_keep
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Remove arquivos JSON antigos

## Classes

### InteractionRecord

**Herança**: Nenhuma
**Atributos**: Nenhum
**Métodos**: 0
**Linhas**: 13

Registro de uma interação no banco de dados

### DataCollector

**Herança**: Nenhuma
**Atributos**: content, interaction_id, record, complexity, context_size, request_length, date_str, json_file, query, params, result, feedback_id, cutoff_date, cutoff_date, cursor, data, conditions, value, cursor, data, cursor, row, cursor, rows, cursor, cursor, total_interactions, avg_success, avg_execution_time, optimized_interactions, workflow_stats, daily_stats, stats, cursor, cursor, date_str, file_date
**Métodos**: 14
**Linhas**: 402

Sistema de coleta e armazenamento de dados de interações

#### __init__

**Parâmetros**: self, data_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Sem documentação.

#### init_database

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 62

Inicializa banco de dados SQLite

#### generate_interaction_id

**Parâmetros**: self, user_request, timestamp
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Gera ID único para uma interação

#### save_interaction

**Parâmetros**: self, interaction_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 53

Salva uma nova interação no sistema

#### _calculate_complexity

**Parâmetros**: self, interaction_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Calcula score de complexidade da interação

#### _save_json_backup

**Parâmetros**: self, record
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Salva backup em formato JSON

#### get_interaction

**Parâmetros**: self, interaction_id
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Recupera uma interação específica

#### get_interactions

**Parâmetros**: self, limit, offset, filters
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 39

Recupera múltiplas interações com filtros

#### _row_to_dict

**Parâmetros**: self, row, description
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Converte linha do banco em dicionário

#### get_total_interactions

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Retorna total de interações no sistema

#### get_interaction_stats

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 65

Retorna estatísticas das interações

#### add_feedback

**Parâmetros**: self, interaction_id, feedback_text, feedback_score
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Adiciona feedback a uma interação

#### cleanup_old_data

**Parâmetros**: self, days_to_keep
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Remove dados antigos do sistema

#### _cleanup_old_json_files

**Parâmetros**: self, days_to_keep
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Remove arquivos JSON antigos

## Imports

.GitautomationModule, json, sqlite3, hashlib, datetime.datetime, datetime.timedelta, threading

## Uso

```python
# Exemplo de uso do módulo migrated_data_collector
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:52

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

