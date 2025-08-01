# migrated_python_error_resolver

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_python_error_resolver
- **Caminho**: wiki\update\modules\python\error_resolver\migrated_python_error_resolver.py
- **Linhas de código**: 568
- **Complexidade**: 64.00
- **Funções**: 17
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Função principal para resolução automática

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
**Linhas**: 9

Sem documentação.

### load_error_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 92

Carrega padrões de erro conhecidos e suas soluções

### detect_error_type

**Parâmetros**: self, error_message
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Detecta o tipo de erro baseado na mensagem

### check_python_path

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Verifica se o Python está no PATH

### install_missing_dependencies

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Instala dependências faltantes

### fix_import_statement

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 49

Corrige declarações de import problemáticas

### fix_syntax_error

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Corrige erros de sintaxe básicos

### validate_json_syntax

**Parâmetros**: self, json_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 42

Valida e corrige sintaxe JSON

### check_file_path

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Verifica se o arquivo existe e cria se necessário

### fix_encoding_declaration

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Corrige declaração de encoding

### increase_timeout

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Aumenta timeout para scripts que demoram muito

### resolve_error

**Parâmetros**: self, script_path, error_message
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 70

Resolve erro específico em um script Python

### test_script

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Testa se o script funciona após correções

### auto_resolve_script_errors

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Resolve automaticamente erros em um script Python

### log_resolution

**Parâmetros**: self, resolution_result
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Registra resultado da resolução

## Classes

### PythonErrorResolver

**Herança**: Nenhuma
**Atributos**: error_message_lower, path, error_type, resolution_result, solutions, log_file, resolutions, result, dependencies, common_imports, lines, import_section, other_lines, essential_imports, new_content, backup_path, lines, fixed_lines, new_content, backup_path, backup_path, result, result, error_message, content, content, content, content, content, content, content, content, line, lines, cleaned_lines, cleaned_content, backup_path, lines, content, content, resolutions, resolutions, line
**Métodos**: 15
**Linhas**: 496

Sem documentação.

#### __init__

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Sem documentação.

#### load_error_patterns

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 92

Carrega padrões de erro conhecidos e suas soluções

#### detect_error_type

**Parâmetros**: self, error_message
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Detecta o tipo de erro baseado na mensagem

#### check_python_path

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Verifica se o Python está no PATH

#### install_missing_dependencies

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Instala dependências faltantes

#### fix_import_statement

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 49

Corrige declarações de import problemáticas

#### fix_syntax_error

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Corrige erros de sintaxe básicos

#### validate_json_syntax

**Parâmetros**: self, json_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 42

Valida e corrige sintaxe JSON

#### check_file_path

**Parâmetros**: self, file_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Verifica se o arquivo existe e cria se necessário

#### fix_encoding_declaration

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Corrige declaração de encoding

#### increase_timeout

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Aumenta timeout para scripts que demoram muito

#### resolve_error

**Parâmetros**: self, script_path, error_message
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 70

Resolve erro específico em um script Python

#### test_script

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Testa se o script funciona após correções

#### auto_resolve_script_errors

**Parâmetros**: self, script_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 25

Resolve automaticamente erros em um script Python

#### log_resolution

**Parâmetros**: self, resolution_result
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Registra resultado da resolução

## Imports

.ErrorresolverModule, json, subprocess, sys

## Uso

```python
# Exemplo de uso do módulo migrated_python_error_resolver
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:53
