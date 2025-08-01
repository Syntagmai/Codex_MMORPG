# error_correction_agent

## Descrição

🚀 Error Correction Agent - Epic 12 Task 12.6
=============================================

Script para implementar correção automática de erros Python.
Baseado nos resultados de validação da Task 12.5.

Responsável: Error Correction Agent
Duração: 3-4 dias
Dependência: Task 12.5 (Validação de scripts)

## Informações Técnicas

- **Módulo**: error_correction_agent
- **Caminho**: wiki\update\error_correction_agent.py
- **Linhas de código**: 579
- **Complexidade**: 82.00
- **Funções**: 18
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 42

Função principal do script.

### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 43

Sem documentação.

### load_validation_results

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Carrega os resultados de validação.

### get_files_with_errors

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Obtém arquivos que possuem erros para correção.

### create_backup

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Cria backup de um arquivo antes da correção.

### fix_unterminated_string

**Parâmetros**: self, content, line_number
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Corrige strings não terminadas.

### fix_invalid_character

**Parâmetros**: self, content, line_number
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Corrige caracteres inválidos.

### fix_leading_zeros

**Parâmetros**: self, content, line_number
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Corrige literais com zeros à esquerda.

### fix_line_length

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 40

Corrige linhas muito longas.

### fix_naming_convention

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Corrige convenções de nomenclatura.

### fix_missing_docstring

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Adiciona docstrings ausentes.

### fix_magic_numbers

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Substitui números mágicos por constantes.

### fix_unused_imports

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 44

Remove imports não utilizados.

### correct_file

**Parâmetros**: self, file_info
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 109

Corrige um arquivo Python.

### correct_all_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Corrige todos os arquivos com problemas.

### save_correction_results

**Parâmetros**: self, results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Salva os resultados da correção.

### generate_correction_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Gera relatório da correção.

### save_correction_report

**Parâmetros**: self, report
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Salva relatório da correção.

## Classes

### ErrorCorrectionAgent

**Herança**: Nenhuma
**Atributos**: validation_file, files_with_errors, lines, lines, lines, lines, corrected_lines, lines, has_docstring, lines, constants, constants_added, file_path, files_with_issues, correction_results, correction_file, summary_file, summary, report_file, backup_path, line, line, cleaned_line, line, corrected_line, corrected_line, tree, name_mapping, docstring, tree, imports, used_names, lines, corrected_lines, content, original_content, corrections_made, content, result, content, has_docstring, should_keep, error_type, line_number, warning_type, parts, current_line, old_name, new_name, message, content, words, current_line, old_name, new_name, content, content, content, current_line, should_keep, content, content, current_line, content, content
**Métodos**: 17
**Linhas**: 500

Agente para correção automática de erros Python.

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 43

Sem documentação.

#### load_validation_results

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Carrega os resultados de validação.

#### get_files_with_errors

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Obtém arquivos que possuem erros para correção.

#### create_backup

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 10

Cria backup de um arquivo antes da correção.

#### fix_unterminated_string

**Parâmetros**: self, content, line_number
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Corrige strings não terminadas.

#### fix_invalid_character

**Parâmetros**: self, content, line_number
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Corrige caracteres inválidos.

#### fix_leading_zeros

**Parâmetros**: self, content, line_number
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 14

Corrige literais com zeros à esquerda.

#### fix_line_length

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 40

Corrige linhas muito longas.

#### fix_naming_convention

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Corrige convenções de nomenclatura.

#### fix_missing_docstring

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Adiciona docstrings ausentes.

#### fix_magic_numbers

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 23

Substitui números mágicos por constantes.

#### fix_unused_imports

**Parâmetros**: self, content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 44

Remove imports não utilizados.

#### correct_file

**Parâmetros**: self, file_info
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 109

Corrige um arquivo Python.

#### correct_all_files

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 30

Corrige todos os arquivos com problemas.

#### save_correction_results

**Parâmetros**: self, results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Salva os resultados da correção.

#### generate_correction_report

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Gera relatório da correção.

#### save_correction_report

**Parâmetros**: self, report
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Salva relatório da correção.

## Imports

os, json, ast, re, shutil, pathlib.Path, typing.Dict, typing.List, typing.Any, typing.Optional, typing.Tuple, datetime.datetime, logging

## Uso

```python
# Exemplo de uso do módulo error_correction_agent
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:51
