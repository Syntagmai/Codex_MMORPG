# migrated_navigation_validation_agent

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_navigation_validation_agent
- **Caminho**: wiki\update\modules\agents\agent_orchestrator\migrated_navigation_validation_agent.py
- **Linhas de código**: 461
- **Complexidade**: 38.00
- **Funções**: 10
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
**Linhas**: 6

Sem documentação.

### log_message

**Parâmetros**: self, message, level
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Sem documentação.

### validate_file_references

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 102

Valida referências a arquivos em documentos e scripts

### validate_import_statements

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 68

Valida statements de import em arquivos Python

### validate_json_references

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 60

Valida referências em arquivos JSON

### update_json_references

**Parâmetros**: self, data, old_name, new_name
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Atualiza referências em estrutura JSON

### validate_execution_paths

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 48

Valida caminhos de execução em scripts

### generate_navigation_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 50

Gera relatório completo de validação de navegação

### execute

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 45

Executa a validação completa de navegação

## Classes

### NavigationValidationAgent

**Herança**: Nenhuma
**Atributos**: timestamp, log_entry, log_file, validation_results, file_changes, archived_files, deleted_files, config_files, import_validation, json_validation, json_files, execution_validation, main_scripts, file_refs, import_refs, json_refs, exec_paths, navigation_report, report_file, script_path, file_refs, import_refs, json_refs, exec_paths, navigation_report, final_report, report_file, import_lines, broken_imports, updated_content, broken_refs, updated_content, content, module_path, json_str, broken_refs, updated_data, file_changes, result, content, potential_paths, data, updated_content, updated_content, updated_content, old_to_new, updated_data, updated_content
**Métodos**: 9
**Linhas**: 412

Sem documentação.

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Sem documentação.

#### log_message

**Parâmetros**: self, message, level
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Sem documentação.

#### validate_file_references

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 102

Valida referências a arquivos em documentos e scripts

#### validate_import_statements

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 68

Valida statements de import em arquivos Python

#### validate_json_references

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 60

Valida referências em arquivos JSON

#### update_json_references

**Parâmetros**: self, data, old_name, new_name
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Atualiza referências em estrutura JSON

#### validate_execution_paths

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 48

Valida caminhos de execução em scripts

#### generate_navigation_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 50

Gera relatório completo de validação de navegação

#### execute

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 45

Executa a validação completa de navegação

## Imports

.AgentorchestratorModule, json, re, datetime.datetime, subprocess

## Uso

```python
# Exemplo de uso do módulo migrated_navigation_validation_agent
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

