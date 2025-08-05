# migrated_otclient_log_analyzer

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_otclient_log_analyzer
- **Caminho**: wiki\update\modules\maps\map_updater\migrated_otclient_log_analyzer.py
- **Linhas de código**: 565
- **Complexidade**: 66.00
- **Funções**: 18
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Função principal

### integrate_with_module

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Integra o script com o módulo de destino.

### __init__

**Parâmetros**: self, work_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 67

Sem documentação.

### analyze_logs

**Parâmetros**: self, log_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Analisa logs do OTClient

### parse_log_entries

**Parâmetros**: self, log_content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Parseia entradas de log

### parse_log_line

**Parâmetros**: self, line
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 35

Parseia uma linha de log

### get_time_range

**Parâmetros**: self, entries
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Obtém o intervalo de tempo dos logs

### analyze_level_distribution

**Parâmetros**: self, entries
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Analisa distribuição de níveis de log

### analyze_category_distribution

**Parâmetros**: self, entries
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Analisa distribuição de categorias

### analyze_errors

**Parâmetros**: self, entries
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Analisa erros nos logs

### classify_error

**Parâmetros**: self, message
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Classifica o tipo de erro

### analyze_performance

**Parâmetros**: self, entries
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 48

Analisa métricas de performance

### analyze_crashes

**Parâmetros**: self, entries
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Analisa crashes do cliente

### identify_crash_pattern

**Parâmetros**: self, message
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Identifica padrão de crash

### analyze_patterns

**Parâmetros**: self, entries
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 32

Analisa padrões nos logs

### generate_recommendations

**Parâmetros**: self, entries
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Gera recomendações baseadas na análise

### generate_report

**Parâmetros**: self, analysis
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 66

Gera relatório de análise

### save_analysis

**Parâmetros**: self, analysis, output_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Salva análise em arquivo JSON

## Classes

### OTClientLogAnalyzer

**Herança**: Nenhuma
**Atributos**: log_path, entries, lines, timestamps, level_counts, category_counts, error_entries, error_analysis, message_lower, performance_analysis, crash_entries, crash_analysis, message_lower, pattern_analysis, error_messages, error_counts, error_sequence, recommendations, level_dist, error_count, fatal_count, performance_analysis, pattern_analysis, report, level_dist, category_dist, error_analysis, performance_analysis, crash_analysis, recommendations, log_entries, analysis, entry, pattern, match, pattern2, match2, message, category, error_type, error_key, message, category, message, crash_pattern, output_path, log_content, fps_match, memory_match, latency_match, fps_value, memory_value, latency_value
**Métodos**: 16
**Linhas**: 478

Analisador especializado de logs do OTClient

#### __init__

**Parâmetros**: self, work_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 67

Sem documentação.

#### analyze_logs

**Parâmetros**: self, log_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Analisa logs do OTClient

#### parse_log_entries

**Parâmetros**: self, log_content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Parseia entradas de log

#### parse_log_line

**Parâmetros**: self, line
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 35

Parseia uma linha de log

#### get_time_range

**Parâmetros**: self, entries
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Obtém o intervalo de tempo dos logs

#### analyze_level_distribution

**Parâmetros**: self, entries
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Analisa distribuição de níveis de log

#### analyze_category_distribution

**Parâmetros**: self, entries
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Analisa distribuição de categorias

#### analyze_errors

**Parâmetros**: self, entries
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Analisa erros nos logs

#### classify_error

**Parâmetros**: self, message
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Classifica o tipo de erro

#### analyze_performance

**Parâmetros**: self, entries
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 48

Analisa métricas de performance

#### analyze_crashes

**Parâmetros**: self, entries
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Analisa crashes do cliente

#### identify_crash_pattern

**Parâmetros**: self, message
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Identifica padrão de crash

#### analyze_patterns

**Parâmetros**: self, entries
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 32

Analisa padrões nos logs

#### generate_recommendations

**Parâmetros**: self, entries
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Gera recomendações baseadas na análise

#### generate_report

**Parâmetros**: self, analysis
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 66

Gera relatório de análise

#### save_analysis

**Parâmetros**: self, analysis, output_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Salva análise em arquivo JSON

## Imports

.MapupdaterModule, json, re, argparse

## Uso

```python
# Exemplo de uso do módulo migrated_otclient_log_analyzer
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:56

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

