# update_bmad_maps

## Descrição

Script para atualização automática dos mapas JSON do sistema BMAD
Atualiza: maps/bmad_agents_index.json, maps/bmad_workflows_index.json, maps/bmad_templates_index.json

## Informações Técnicas

- **Módulo**: update_bmad_maps
- **Caminho**: wiki\update\update_bmad_maps.py
- **Linhas de código**: 392
- **Complexidade**: 6.00
- **Funções**: 9
- **Classes**: 1

## Funções

### __init__

**Parâmetros**: self, wiki_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 153

Sem documentação.

### load_context_data

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Carrega dados de contexto detectado

### generate_agents_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Gera índice de agentes BMAD

### generate_workflows_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Gera índice de workflows BMAD

### generate_templates_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Gera índice de templates BMAD

### get_context_adaptation

**Parâmetros**: self, agent_id
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 37

Retorna adaptação do agente para o contexto atual

### get_workflow_context_adaptation

**Parâmetros**: self, workflow_id
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Retorna adaptação do workflow para o contexto atual

### get_template_context_adaptation

**Parâmetros**: self, template_id
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Retorna adaptação do template para o contexto atual

### update_all_bmad_maps

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Atualiza todos os mapas BMAD

## Classes

### BMADMapUpdater

**Herança**: Nenhuma
**Atributos**: context_file, agents_index, workflows_index, templates_index, context, adaptations, context, adaptations, context, adaptations, agents_index, workflows_index, templates_index
**Métodos**: 9
**Linhas**: 376

Sem documentação.

#### __init__

**Parâmetros**: self, wiki_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 153

Sem documentação.

#### load_context_data

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Carrega dados de contexto detectado

#### generate_agents_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Gera índice de agentes BMAD

#### generate_workflows_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Gera índice de workflows BMAD

#### generate_templates_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Gera índice de templates BMAD

#### get_context_adaptation

**Parâmetros**: self, agent_id
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 37

Retorna adaptação do agente para o contexto atual

#### get_workflow_context_adaptation

**Parâmetros**: self, workflow_id
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Retorna adaptação do workflow para o contexto atual

#### get_template_context_adaptation

**Parâmetros**: self, template_id
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Retorna adaptação do template para o contexto atual

#### update_all_bmad_maps

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Atualiza todos os mapas BMAD

## Imports

os, json, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

## Uso

```python
# Exemplo de uso do módulo update_bmad_maps
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

