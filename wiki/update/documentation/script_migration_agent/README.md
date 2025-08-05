# script_migration_agent

## Descrição

🚀 Script Migration Agent - Epic 12 Task 12.3
=============================================

Script para migrar 172 scripts Python existentes para 50 módulos organizados.
Baseado na estrutura modular unificada criada na Task 12.2.

Responsável: Migration Agent
Duração: 5-7 dias
Dependência: Task 12.2 (Estrutura modular unificada)

## Informações Técnicas

- **Módulo**: script_migration_agent
- **Caminho**: wiki\update\script_migration_agent.py
- **Linhas de código**: 451
- **Complexidade**: 49.00
- **Funções**: 14
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 39

Função principal do script.

### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Sem documentação.

### load_structure_config

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Carrega configuração da estrutura modular.

### load_script_mapping

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Carrega mapeamento de scripts para módulos.

### discover_python_scripts

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Descobre todos os scripts Python no projeto.

### analyze_script

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 68

Analisa um script Python para extrair informações.

### determine_target_module

**Parâmetros**: self, script_analysis
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 49

Determina o módulo de destino para um script.

### migrate_script_to_module

**Parâmetros**: self, script_path, target_module
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 35

Migra um script para o módulo de destino.

### create_migrated_script

**Parâmetros**: self, original_content, script_name, target_module
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 35

Cria versão migrada do script.

### update_module_init

**Parâmetros**: self, module_path, script_name, target_module
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Atualiza __init__.py do módulo para incluir script migrado.

### update_module_config

**Parâmetros**: self, module_path, script_name, target_module
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Atualiza configuração do módulo.

### migrate_all_scripts

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 41

Migra todos os scripts descobertos.

### generate_migration_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Gera relatório da migração.

### save_migration_report

**Parâmetros**: self, report
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Salva relatório da migração.

## Classes

### ScriptMigrationAgent

**Herança**: Nenhuma
**Atributos**: config_file, mapping_file, scripts, search_paths, script_name, script_path, script_content, keyword_mapping, migrated_content, init_file, config_file, scripts, report_file, content, analysis, module_path, migrated_content, migrated_file, import_line, script_info, analysis, target_module, tree, category_modules, script_content, init_content, lines, insert_index, init_content, config, success, content, insert_index
**Métodos**: 13
**Linhas**: 375

Agente para migração de scripts Python para módulos organizados.

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Sem documentação.

#### load_structure_config

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Carrega configuração da estrutura modular.

#### load_script_mapping

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Carrega mapeamento de scripts para módulos.

#### discover_python_scripts

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Descobre todos os scripts Python no projeto.

#### analyze_script

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 68

Analisa um script Python para extrair informações.

#### determine_target_module

**Parâmetros**: self, script_analysis
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 49

Determina o módulo de destino para um script.

#### migrate_script_to_module

**Parâmetros**: self, script_path, target_module
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 35

Migra um script para o módulo de destino.

#### create_migrated_script

**Parâmetros**: self, original_content, script_name, target_module
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 35

Cria versão migrada do script.

#### update_module_init

**Parâmetros**: self, module_path, script_name, target_module
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Atualiza __init__.py do módulo para incluir script migrado.

#### update_module_config

**Parâmetros**: self, module_path, script_name, target_module
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Atualiza configuração do módulo.

#### migrate_all_scripts

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 41

Migra todos os scripts descobertos.

#### generate_migration_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Gera relatório da migração.

#### save_migration_report

**Parâmetros**: self, report
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Salva relatório da migração.

## Imports

os, json, shutil, ast, re, pathlib.Path, typing.Dict, typing.List, typing.Any, typing.Optional, typing.Tuple, datetime.datetime, logging

## Uso

```python
# Exemplo de uso do módulo script_migration_agent
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

