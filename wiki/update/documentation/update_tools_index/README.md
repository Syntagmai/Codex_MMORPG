# update_tools_index

## Descrição

Script para indexação das ferramentas do OTClient
Atualiza: wiki/maps/tools_index.json

## Informações Técnicas

- **Módulo**: update_tools_index
- **Caminho**: wiki\update\update_tools_index.py
- **Linhas de código**: 362
- **Complexidade**: 49.00
- **Funções**: 17
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Função principal

### __init__

**Parâmetros**: self, project_root
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Sem documentação.

### scan_tools

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Escaneia todas as ferramentas

### analyze_tool

**Parâmetros**: self, tool_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Analisa uma ferramenta

### categorize_tool

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Categoriza uma ferramenta

### extract_tool_info

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Extrai informações da ferramenta

### extract_description

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Extrai descrição do conteúdo

### get_language

**Parâmetros**: self, file_ext
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Determina a linguagem do arquivo

### extract_functions

**Parâmetros**: self, content, file_ext
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Extrai funções do arquivo

### extract_dependencies

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Extrai dependências do arquivo

### count_lines

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Conta linhas de um arquivo

### categorize_tools

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Categoriza todas as ferramentas

### generate_statistics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 32

Gera estatísticas das ferramentas

### generate_search_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Gera índice de busca

### generate_tools_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Gera o índice completo das ferramentas

### save_index

**Parâmetros**: self, tools_index, output_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Salva o índice em arquivo JSON

### update_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Atualiza o índice das ferramentas

## Classes

### ToolsIndexer

**Herança**: Nenhuma
**Atributos**: tools, file_name, file_ext, info, lines, language_map, functions, dependencies, stats, type_counts, language_counts, search_index, tool_paths, statistics, search_index, tools_index, tools_index, item_path, item_name, is_file, is_dir, category, tool_info, stat, tool_data, line, patterns, category, tool_type, language, name, category, language, tool_info, output_path, file_ext, files, info, info, pattern, functions, matches, info, info, pattern, functions, content, pattern, functions
**Métodos**: 16
**Linhas**: 329

Sem documentação.

#### __init__

**Parâmetros**: self, project_root
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Sem documentação.

#### scan_tools

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Escaneia todas as ferramentas

#### analyze_tool

**Parâmetros**: self, tool_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Analisa uma ferramenta

#### categorize_tool

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Categoriza uma ferramenta

#### extract_tool_info

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Extrai informações da ferramenta

#### extract_description

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Extrai descrição do conteúdo

#### get_language

**Parâmetros**: self, file_ext
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Determina a linguagem do arquivo

#### extract_functions

**Parâmetros**: self, content, file_ext
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Extrai funções do arquivo

#### extract_dependencies

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Extrai dependências do arquivo

#### count_lines

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Conta linhas de um arquivo

#### categorize_tools

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Categoriza todas as ferramentas

#### generate_statistics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 32

Gera estatísticas das ferramentas

#### generate_search_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Gera índice de busca

#### generate_tools_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Gera o índice completo das ferramentas

#### save_index

**Parâmetros**: self, tools_index, output_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Salva o índice em arquivo JSON

#### update_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Atualiza o índice das ferramentas

## Imports

os, json, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

## Uso

```python
# Exemplo de uso do módulo update_tools_index
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

