# consolidate_agents

## Descrição

Consolidação de Agentes BMAD
============================

Este script consolida 35 agentes em 25 especializados,
identificando agentes similares e consolidando suas funcionalidades.

Autor: Sistema BMAD - Agent Organizer
Data: 2025-08-01

## Informações Técnicas

- **Módulo**: consolidate_agents
- **Caminho**: wiki\update\consolidate_agents.py
- **Linhas de código**: 443
- **Complexidade**: 33.00
- **Funções**: 7
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Função principal

### __init__

**Parâmetros**: self, agents_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 122

Inicializa o consolidador de agentes.

Args:
    agents_dir: Diretório contendo os agentes

### analyze_agents

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 53

Analisa todos os agentes existentes

### backup_agents

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Faz backup de todos os agentes antes da consolidação

### consolidate_group

**Parâmetros**: self, group_name, group_config
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 83

Consolida um grupo de agentes

### consolidate_all_agents

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 43

Consolida todos os agentes

### generate_consolidation_report

**Parâmetros**: self, results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 40

Gera relatório de consolidação

## Classes

### AgentConsolidator

**Herança**: Nenhuma
**Atributos**: analysis, agent_files, analysis, results, final_agents, report, filename, categorized, agent_files, agents_to_merge, new_name, description, existing_agents, consolidated_agent_path, main_agent, main_agent_path, agents_in_group, backup_file, agent_path, consolidation_header, lines, header_end, new_content, success, categorized, content, header_end, agent_path
**Métodos**: 6
**Linhas**: 371

Consolidador de agentes BMAD

#### __init__

**Parâmetros**: self, agents_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 122

Inicializa o consolidador de agentes.

Args:
    agents_dir: Diretório contendo os agentes

#### analyze_agents

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 53

Analisa todos os agentes existentes

#### backup_agents

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Faz backup de todos os agentes antes da consolidação

#### consolidate_group

**Parâmetros**: self, group_name, group_config
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 83

Consolida um grupo de agentes

#### consolidate_all_agents

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 43

Consolida todos os agentes

#### generate_consolidation_report

**Parâmetros**: self, results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 40

Gera relatório de consolidação

## Imports

json, os, shutil, pathlib.Path, typing.Dict, typing.List, typing.Any, typing.Optional, datetime.datetime, logging

## Uso

```python
# Exemplo de uso do módulo consolidate_agents
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

