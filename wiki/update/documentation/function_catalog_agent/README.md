# function_catalog_agent

## Descrição

🚀 Function Catalog Agent - Epic 12 Task 12.4
=============================================

Script para criar catálogo automático de todas as funções Python.
Baseado nos módulos migrados da Task 12.3.

Responsável: Function Catalog Agent
Duração: 2-3 dias
Dependência: Task 12.3 (Migração de scripts)

## Informações Técnicas

- **Módulo**: function_catalog_agent
- **Caminho**: wiki\update\function_catalog_agent.py
- **Linhas de código**: 549
- **Complexidade**: 67.00
- **Funções**: 15
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 43

Função principal do script.

### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 35

Sem documentação.

### discover_python_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Descobre todos os arquivos Python nos módulos.

### analyze_python_file

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 59

Analisa um arquivo Python para extrair funções e classes.

### extract_function_info

**Parâmetros**: self, node, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 43

Extrai informações de uma função.

### extract_class_info

**Parâmetros**: self, node, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Extrai informações de uma classe.

### extract_module_docstring

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Extrai docstring do módulo.

### categorize_function

**Parâmetros**: self, function_info, module_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Categoriza uma função baseada em seu contexto.

### build_function_catalog

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Constrói o catálogo completo de funções.

### add_to_catalog

**Parâmetros**: self, analysis
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 73

Adiciona análise de arquivo ao catálogo.

### build_search_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 52

Constrói índice de busca para o catálogo.

### update_catalog_stats

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Atualiza estatísticas do catálogo.

### save_catalog

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 37

Salva o catálogo em arquivos JSON.

### generate_catalog_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Gera relatório do catálogo.

### save_catalog_report

**Parâmetros**: self, report
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Salva relatório do catálogo.

## Classes

### FunctionCatalogAgent

**Herança**: Nenhuma
**Atributos**: python_files, start_line, end_line, docstring, args, decorators, function_type, start_line, end_line, docstring, methods, decorators, bases, parts, function_name, python_files, module_path, file_name, search_index, catalog_file, search_index_file, report_file, content, tree, analysis, total_elements, function_type, tree, analysis, category, function_id, category, class_id, name, func_type, module_path, docstring, category_file, category_data, function_type, method_info, words, function_info, function_type, content, class_info, function_type
**Métodos**: 14
**Linhas**: 470

Agente para criação de catálogo automático de funções Python.

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 35

Sem documentação.

#### discover_python_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Descobre todos os arquivos Python nos módulos.

#### analyze_python_file

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 59

Analisa um arquivo Python para extrair funções e classes.

#### extract_function_info

**Parâmetros**: self, node, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 43

Extrai informações de uma função.

#### extract_class_info

**Parâmetros**: self, node, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Extrai informações de uma classe.

#### extract_module_docstring

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Extrai docstring do módulo.

#### categorize_function

**Parâmetros**: self, function_info, module_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Categoriza uma função baseada em seu contexto.

#### build_function_catalog

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Constrói o catálogo completo de funções.

#### add_to_catalog

**Parâmetros**: self, analysis
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 73

Adiciona análise de arquivo ao catálogo.

#### build_search_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 52

Constrói índice de busca para o catálogo.

#### update_catalog_stats

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Atualiza estatísticas do catálogo.

#### save_catalog

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 37

Salva o catálogo em arquivos JSON.

#### generate_catalog_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Gera relatório do catálogo.

#### save_catalog_report

**Parâmetros**: self, report
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Salva relatório do catálogo.

## Imports

os, json, ast, inspect, pathlib.Path, typing.Dict, typing.List, typing.Any, typing.Optional, typing.Tuple, datetime.datetime, logging

## Uso

```python
# Exemplo de uso do módulo function_catalog_agent
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

