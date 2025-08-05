# migrated_intelligent_organization_agent

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_intelligent_organization_agent
- **Caminho**: wiki\update\modules\agents\agent_orchestrator\migrated_intelligent_organization_agent.py
- **Linhas de código**: 984
- **Complexidade**: 101.00
- **Funções**: 32
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 45

Função principal.

### integrate_with_module

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Integra o script com o módulo de destino.

### __init__

**Parâmetros**: self, base_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 91

Sem documentação.

### detect_organization_issues

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 39

Detecta problemas de organização automaticamente.
Inclui detecção específica para arquivos de integração Canary.

Returns:
    Dicionário com problemas encontrados

### _detect_canary_integration_issues

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Detecta problemas específicos relacionados à integração Canary.

Returns:
    Lista de arquivos com problemas de integração

### _detect_missing_integration_structure

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Detecta estrutura de integração faltante.

Returns:
    Lista de diretórios/arquivos faltantes

### _is_canary_integration_file

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Verifica se um arquivo é relacionado à integração Canary.

Args:
    file_path: Caminho do arquivo
    
Returns:
    True se for arquivo de integração Canary

### _is_in_correct_canary_location

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Verifica se um arquivo de integração Canary está no local correto.

Args:
    file_path: Caminho do arquivo
    
Returns:
    True se estiver no local correto

### organize_canary_integration_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Organiza arquivos relacionados à integração Canary.

Returns:
    Dicionário com estatísticas de organização

### _create_canary_integration_structure

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Cria estrutura de integração Canary se não existir.

Returns:
    True se estrutura foi criada ou já existia

### _organize_canary_file

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Organiza um arquivo específico de integração Canary.

Args:
    file_path: Caminho do arquivo
    
Returns:
    True se arquivo foi organizado com sucesso

### validate_canary_integration_structure

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 54

Valida a estrutura de integração Canary.

Returns:
    Dicionário com resultados da validação

### is_in_wrong_location

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Verifica se arquivo está no local errado.

### is_obsolete

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Verifica se arquivo é obsoleto.

### is_temp_file

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Verifica se arquivo é temporário.

### has_category

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Verifica se arquivo tem categoria definida.

### find_duplicates

**Parâmetros**: self, files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Encontra arquivos duplicados.

### find_unorganized_reports

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Encontra relatórios não organizados.

### detect_file_context

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Detecta contexto do arquivo automaticamente.

### is_in_reports_folder

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 2

Verifica se arquivo está na pasta de relatórios.

### is_in_tasks_folder

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 2

Verifica se arquivo está na pasta de tarefas.

### is_in_recipes_folder

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 2

Verifica se arquivo está na pasta de receitas.

### is_in_archives_folder

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 2

Verifica se arquivo está na pasta de arquivos.

### organize_by_category

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 41

Organiza arquivos por categoria automaticamente.

Returns:
    Dicionário com número de arquivos organizados por categoria

### organize_by_date

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 47

Organiza relatórios por data automaticamente.

Returns:
    Dicionário com número de relatórios organizados por mês

### extract_date_from_file

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Extrai data do arquivo ou usa data de modificação.

### cleanup_temp_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Remove arquivos temporários automaticamente.

Returns:
    Número de arquivos removidos

### remove_duplicates

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Remove arquivos duplicados.

Returns:
    Número de duplicatas removidas

### create_organization_structure

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 50

Cria estrutura de organização padrão.

Returns:
    True se estrutura foi criada com sucesso

### generate_organization_report

**Parâmetros**: self, results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 82

Gera relatório de organização.

Args:
    results: Resultados da organização
    
Returns:
    Relatório em formato markdown

### run_full_organization

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 55

Executa organização completa do sistema.

Returns:
    Resultados da organização

### _is_ignored

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 37

Verifica se um arquivo deve ser ignorado pela organização.

Args:
    file_path: Caminho do arquivo
    
Returns:
    True se o arquivo deve ser ignorado

## Classes

### IntelligentOrganizationAgent

**Herança**: Nenhuma
**Atributos**: issues, all_files, duplicates, issues, missing, required_structure, filename, canary_locations, stats, validation, context, context, duplicates, file_contents, unorganized, organized_count, organized_count, reports_dir, date_patterns, removed_count, removed_count, files, duplicates, report, ignored_patterns, submodule_patterns, file_str, structure, filename, required_components, missing, total_components, existing_components, mtime, match, structure, structure_created, issues, organized_by_category, organized_by_date, temp_files_removed, duplicates_removed, results, report_content, report_path, destination, date_str, destination, content, destination, file_date, month_dir, new_path, month_key, date_str, destination, destination, new_path, counter, date_str, counter, name, new_path, name, new_path
**Métodos**: 30
**Linhas**: 865

Agente de organização inteligente para code cleanup e integração Canary

#### __init__

**Parâmetros**: self, base_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 91

Sem documentação.

#### detect_organization_issues

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 39

Detecta problemas de organização automaticamente.
Inclui detecção específica para arquivos de integração Canary.

Returns:
    Dicionário com problemas encontrados

#### _detect_canary_integration_issues

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Detecta problemas específicos relacionados à integração Canary.

Returns:
    Lista de arquivos com problemas de integração

#### _detect_missing_integration_structure

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Detecta estrutura de integração faltante.

Returns:
    Lista de diretórios/arquivos faltantes

#### _is_canary_integration_file

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 11

Verifica se um arquivo é relacionado à integração Canary.

Args:
    file_path: Caminho do arquivo
    
Returns:
    True se for arquivo de integração Canary

#### _is_in_correct_canary_location

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Verifica se um arquivo de integração Canary está no local correto.

Args:
    file_path: Caminho do arquivo
    
Returns:
    True se estiver no local correto

#### organize_canary_integration_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 38

Organiza arquivos relacionados à integração Canary.

Returns:
    Dicionário com estatísticas de organização

#### _create_canary_integration_structure

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Cria estrutura de integração Canary se não existir.

Returns:
    True se estrutura foi criada ou já existia

#### _organize_canary_file

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Organiza um arquivo específico de integração Canary.

Args:
    file_path: Caminho do arquivo
    
Returns:
    True se arquivo foi organizado com sucesso

#### validate_canary_integration_structure

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 54

Valida a estrutura de integração Canary.

Returns:
    Dicionário com resultados da validação

#### is_in_wrong_location

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Verifica se arquivo está no local errado.

#### is_obsolete

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Verifica se arquivo é obsoleto.

#### is_temp_file

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Verifica se arquivo é temporário.

#### has_category

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Verifica se arquivo tem categoria definida.

#### find_duplicates

**Parâmetros**: self, files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Encontra arquivos duplicados.

#### find_unorganized_reports

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Encontra relatórios não organizados.

#### detect_file_context

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Detecta contexto do arquivo automaticamente.

#### is_in_reports_folder

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 2

Verifica se arquivo está na pasta de relatórios.

#### is_in_tasks_folder

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 2

Verifica se arquivo está na pasta de tarefas.

#### is_in_recipes_folder

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 2

Verifica se arquivo está na pasta de receitas.

#### is_in_archives_folder

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 2

Verifica se arquivo está na pasta de arquivos.

#### organize_by_category

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 41

Organiza arquivos por categoria automaticamente.

Returns:
    Dicionário com número de arquivos organizados por categoria

#### organize_by_date

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 47

Organiza relatórios por data automaticamente.

Returns:
    Dicionário com número de relatórios organizados por mês

#### extract_date_from_file

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Extrai data do arquivo ou usa data de modificação.

#### cleanup_temp_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Remove arquivos temporários automaticamente.

Returns:
    Número de arquivos removidos

#### remove_duplicates

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 24

Remove arquivos duplicados.

Returns:
    Número de duplicatas removidas

#### create_organization_structure

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 50

Cria estrutura de organização padrão.

Returns:
    True se estrutura foi criada com sucesso

#### generate_organization_report

**Parâmetros**: self, results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 82

Gera relatório de organização.

Args:
    results: Resultados da organização
    
Returns:
    Relatório em formato markdown

#### run_full_organization

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 55

Executa organização completa do sistema.

Returns:
    Resultados da organização

#### _is_ignored

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 37

Verifica se um arquivo deve ser ignorado pela organização.

Args:
    file_path: Caminho do arquivo
    
Returns:
    True se o arquivo deve ser ignorado

## Imports

.AgentorchestratorModule, shutil, re, datetime.datetime, datetime.timedelta, logging, argparse

## Uso

```python
# Exemplo de uso do módulo migrated_intelligent_organization_agent
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

