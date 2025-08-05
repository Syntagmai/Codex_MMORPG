# migrated_update_source_index

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_update_source_index
- **Caminho**: wiki\update\modules\maps\source_indexer\migrated_update_source_index.py
- **Linhas de código**: 301
- **Complexidade**: 55.00
- **Funções**: 11
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Função principal

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
**Linhas**: 11

Sem documentação.

### scan_source_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Escaneia arquivos de código-fonte nos submódulos

### categorize_file

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 32

Categoriza um arquivo baseado em seu caminho e conteúdo

### extract_functions

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Extrai funções de um arquivo

### extract_classes

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Extrai classes de um arquivo

### generate_source_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 44

Gera o índice completo do código-fonte

### generate_statistics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Gera estatísticas do código-fonte

### generate_search_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Gera índice de busca

### save_index

**Parâmetros**: self, source_index, output_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Salva o índice em arquivo JSON

## Classes

### SourceIndexer

**Herança**: Nenhuma
**Atributos**: source_extensions, source_files, otclient_src_dir, otclient_modules_dir, canary_src_dir, canary_modules_dir, path_lower, functions, classes, source_files, statistics, search_index, source_index, stats, search_index, category, functions, classes, file_info, output_path, content, lua_functions, cpp_functions, content, cpp_classes, ext, file_name
**Métodos**: 9
**Linhas**: 238

Sem documentação.

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Sem documentação.

#### scan_source_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Escaneia arquivos de código-fonte nos submódulos

#### categorize_file

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 32

Categoriza um arquivo baseado em seu caminho e conteúdo

#### extract_functions

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Extrai funções de um arquivo

#### extract_classes

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 15

Extrai classes de um arquivo

#### generate_source_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 44

Gera o índice completo do código-fonte

#### generate_statistics

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Gera estatísticas do código-fonte

#### generate_search_index

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Gera índice de busca

#### save_index

**Parâmetros**: self, source_index, output_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Salva o índice em arquivo JSON

## Imports

.SourceindexerModule, json, re, datetime.datetime

## Uso

```python
# Exemplo de uso do módulo migrated_update_source_index
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:56

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

