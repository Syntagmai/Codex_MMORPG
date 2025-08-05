# python_validator_agent

## Descrição

🚀 Python Validator Agent - Epic 12 Task 12.5
=============================================

Script para criar validador automático de scripts Python.
Baseado no catálogo de funções da Task 12.4.

Responsável: Python Validator Agent
Duração: 3-4 dias
Dependência: Task 12.4 (Catálogo de funções)

## Informações Técnicas

- **Módulo**: python_validator_agent
- **Caminho**: wiki\update\python_validator_agent.py
- **Linhas de código**: 553
- **Complexidade**: 63.00
- **Funções**: 16
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 41

Função principal do script.

### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 45

Sem documentação.

### load_function_catalog

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Carrega o catálogo de funções.

### discover_python_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Descobre todos os arquivos Python para validação.

### validate_syntax

**Parâmetros**: self, file_path, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 33

Valida a sintaxe de um arquivo Python.

### validate_style

**Parâmetros**: self, file_path, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 52

Valida o estilo de código Python.

### validate_quality

**Parâmetros**: self, file_path, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 44

Valida a qualidade do código Python.

### calculate_cyclomatic_complexity

**Parâmetros**: self, tree
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Calcula a complexidade ciclomática de um AST.

### find_unused_imports

**Parâmetros**: self, tree, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Encontra imports não utilizados.

### find_magic_numbers

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Encontra números mágicos no código.

### validate_file

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 57

Valida um arquivo Python completo.

### validate_all_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 47

Valida todos os arquivos Python descobertos.

### save_validation_results

**Parâmetros**: self, results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 39

Salva os resultados da validação.

### generate_category_report

**Parâmetros**: self, results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Gera relatório de validação por categoria.

### generate_validation_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Gera relatório da validação.

### save_validation_report

**Parâmetros**: self, report
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Salva relatório da validação.

## Classes

### PythonValidatorAgent

**Herança**: Nenhuma
**Atributos**: catalog_file, python_files, validation_result, validation_result, lines, validation_result, complexity, imports, used_names, magic_numbers, lines, python_files, validation_results, validation_file, summary_file, summary, category_report, category_file, category_stats, report_file, tree, tree, tree, complexity, unused_imports, magic_numbers, numbers, content, syntax_result, style_result, quality_result, validation_result, result, module_path, category, content
**Métodos**: 15
**Linhas**: 474

Agente para validação automática de scripts Python.

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 45

Sem documentação.

#### load_function_catalog

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Carrega o catálogo de funções.

#### discover_python_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Descobre todos os arquivos Python para validação.

#### validate_syntax

**Parâmetros**: self, file_path, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 33

Valida a sintaxe de um arquivo Python.

#### validate_style

**Parâmetros**: self, file_path, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 52

Valida o estilo de código Python.

#### validate_quality

**Parâmetros**: self, file_path, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 44

Valida a qualidade do código Python.

#### calculate_cyclomatic_complexity

**Parâmetros**: self, tree
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Calcula a complexidade ciclomática de um AST.

#### find_unused_imports

**Parâmetros**: self, tree, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Encontra imports não utilizados.

#### find_magic_numbers

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Encontra números mágicos no código.

#### validate_file

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 57

Valida um arquivo Python completo.

#### validate_all_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 47

Valida todos os arquivos Python descobertos.

#### save_validation_results

**Parâmetros**: self, results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 39

Salva os resultados da validação.

#### generate_category_report

**Parâmetros**: self, results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Gera relatório de validação por categoria.

#### generate_validation_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Gera relatório da validação.

#### save_validation_report

**Parâmetros**: self, report
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Salva relatório da validação.

## Imports

os, json, ast, re, subprocess, sys, pathlib.Path, typing.Dict, typing.List, typing.Any, typing.Optional, typing.Tuple, datetime.datetime, logging

## Uso

```python
# Exemplo de uso do módulo python_validator_agent
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:51

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

