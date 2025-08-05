# auto_update_all_maps

## Descrição

Script principal para atualização automática de todos os mapas JSON
Executa todos os scripts de indexação na ordem estabelecida
Usa contexto detectado automaticamente

## Informações Técnicas

- **Módulo**: auto_update_all_maps
- **Caminho**: wiki\update\auto_update_all_maps.py
- **Linhas de código**: 276
- **Complexidade**: 23.00
- **Funções**: 11
- **Classes**: 1

## Funções

### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Sem documentação.

### load_context_data

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Carrega dados de contexto detectado

### get_context_scripts

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Retorna scripts baseados no contexto

### get_context_maps

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Retorna mapas baseados no contexto

### log

**Parâmetros**: self, message, level
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Log com timestamp

### execute_script

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Executa um script específico

### validate_map

**Parâmetros**: self, map_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Valida um mapa JSON

### update_all_maps

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Executa atualização de todos os mapas

### generate_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Gera relatório de atualização

### save_report

**Parâmetros**: self, report_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Salva relatório de atualização

### print_summary

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Imprime resumo da atualização

## Classes

### AutoMapUpdater

**Herança**: Nenhuma
**Atributos**: context_file, base_maps, timestamp, total_scripts, success_rate, total_files, total_scripts, executed_scripts, failed_scripts, success_rate, start_time, result, end_time, execution_time, data, data
**Métodos**: 11
**Linhas**: 255

Sem documentação.

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Sem documentação.

#### load_context_data

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Carrega dados de contexto detectado

#### get_context_scripts

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Retorna scripts baseados no contexto

#### get_context_maps

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Retorna mapas baseados no contexto

#### log

**Parâmetros**: self, message, level
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Log com timestamp

#### execute_script

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Executa um script específico

#### validate_map

**Parâmetros**: self, map_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Valida um mapa JSON

#### update_all_maps

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Executa atualização de todos os mapas

#### generate_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Gera relatório de atualização

#### save_report

**Parâmetros**: self, report_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Salva relatório de atualização

#### print_summary

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Imprime resumo da atualização

## Imports

os, sys, json, subprocess, time, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

## Uso

```python
# Exemplo de uso do módulo auto_update_all_maps
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:50

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

