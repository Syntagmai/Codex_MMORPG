# modular_structure_creator

## Descrição

🚀 Module Structure Creator - Epic 12 Task 12.2
===============================================

Script para criar estrutura modular unificada com 50 módulos organizados por funcionalidade.
Baseado na análise de 172 scripts Python existentes no projeto.

Responsável: Module Structure Agent
Duração: 3-5 dias
Dependência: Task 12.1 (Análise completa dos scripts Python)

## Informações Técnicas

- **Módulo**: modular_structure_creator
- **Caminho**: wiki\update\modular_structure_creator.py
- **Linhas de código**: 644
- **Complexidade**: 11.00
- **Funções**: 12
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 33

Função principal do script.

### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 108

Sem documentação.

### create_script_mapping

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 65

Cria mapeamento de scripts existentes para módulos.

### create_module_structure

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 41

Cria a estrutura modular unificada.

### create_init_file

**Parâmetros**: self, path, description
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Cria arquivo __init__.py para categoria.

### create_module_init

**Parâmetros**: self, path, module_name, description
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Cria arquivo __init__.py para módulo.

### create_module_files

**Parâmetros**: self, path, module_name, description
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 162

Cria arquivos base do módulo.

### get_category_for_module

**Parâmetros**: self, module_name
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Retorna a categoria de um módulo.

### create_structure_config

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Cria arquivo de configuração da estrutura.

### create_script_mapping_file

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 4

Cria arquivo de mapeamento de scripts.

### create_structure_documentation

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 76

Cria documentação da estrutura modular.

### generate_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Gera relatório da criação da estrutura.

## Classes

### ModuleStructureCreator

**Herança**: Nenhuma
**Atributos**: init_content, init_file, init_content, init_file, main_file, main_content, config_file, config_content, test_file, test_content, config_file, config_content, mapping_file, doc_file, doc_content, category_path, module_path
**Métodos**: 11
**Linhas**: 576

Criador de estrutura modular unificada para scripts Python.

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 108

Sem documentação.

#### create_script_mapping

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 65

Cria mapeamento de scripts existentes para módulos.

#### create_module_structure

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 41

Cria a estrutura modular unificada.

#### create_init_file

**Parâmetros**: self, path, description
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Cria arquivo __init__.py para categoria.

#### create_module_init

**Parâmetros**: self, path, module_name, description
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Cria arquivo __init__.py para módulo.

#### create_module_files

**Parâmetros**: self, path, module_name, description
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 162

Cria arquivos base do módulo.

#### get_category_for_module

**Parâmetros**: self, module_name
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Retorna a categoria de um módulo.

#### create_structure_config

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Cria arquivo de configuração da estrutura.

#### create_script_mapping_file

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 4

Cria arquivo de mapeamento de scripts.

#### create_structure_documentation

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 76

Cria documentação da estrutura modular.

#### generate_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Gera relatório da criação da estrutura.

## Imports

os, json, shutil, pathlib.Path, typing.Dict, typing.List, typing.Any, typing.Optional, datetime.datetime, logging

## Uso

```python
# Exemplo de uso do módulo modular_structure_creator
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:51
