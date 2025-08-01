# migrated_consolidate_agents

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_consolidate_agents
- **Caminho**: wiki\update\modules\maps\map_updater\migrated_consolidate_agents.py
- **Linhas de código**: 474
- **Complexidade**: 35.00
- **Funções**: 8
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Função principal

### integrate_with_module

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Integra o script com o módulo de destino.

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

.MapupdaterModule, json, shutil, datetime.datetime, logging

## Uso

```python
# Exemplo de uso do módulo migrated_consolidate_agents
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:54
