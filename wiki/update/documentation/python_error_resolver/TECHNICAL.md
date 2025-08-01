# Documentação Técnica - python_error_resolver

## Análise Estática

### Métricas de Código
- **Linhas de código**: 539
- **Complexidade ciclomática**: 62.00
- **Funções**: 16
- **Classes**: 1
- **Imports**: 11

### Análise de Complexidade
- **Nível**: Alto (Código complexo, considere refatoração)\n
### Estrutura de Dependências

#### Imports Externos
json, subprocess, sys, traceback, time, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any, typing.Optional

#### Hierarquia de Classes
- PythonErrorResolver (sem herança)\n
### Análise de Funções

#### Funções Principais
**main**
- Parâmetros: 0
- Linhas: 21
- Documentação: Sim

**__init__**
- Parâmetros: 1
- Linhas: 9
- Documentação: Não

**load_error_patterns**
- Parâmetros: 1
- Linhas: 92
- Documentação: Sim

**detect_error_type**
- Parâmetros: 2
- Linhas: 9
- Documentação: Sim

**check_python_path**
- Parâmetros: 2
- Linhas: 7
- Documentação: Sim

**install_missing_dependencies**
- Parâmetros: 2
- Linhas: 21
- Documentação: Sim

**fix_import_statement**
- Parâmetros: 2
- Linhas: 49
- Documentação: Sim

**fix_syntax_error**
- Parâmetros: 2
- Linhas: 36
- Documentação: Sim

**validate_json_syntax**
- Parâmetros: 2
- Linhas: 42
- Documentação: Sim

**check_file_path**
- Parâmetros: 2
- Linhas: 19
- Documentação: Sim

**fix_encoding_declaration**
- Parâmetros: 2
- Linhas: 29
- Documentação: Sim

**increase_timeout**
- Parâmetros: 2
- Linhas: 22
- Documentação: Sim

**resolve_error**
- Parâmetros: 3
- Linhas: 70
- Documentação: Sim

**test_script**
- Parâmetros: 2
- Linhas: 16
- Documentação: Sim

**auto_resolve_script_errors**
- Parâmetros: 2
- Linhas: 25
- Documentação: Sim

**log_resolution**
- Parâmetros: 2
- Linhas: 21
- Documentação: Sim

### Recomendações

1. **Documentação**: Adicione docstrings para todas as funções e classes
2. **Complexidade**: Considere refatorar funções muito complexas
3. **Testes**: Implemente testes unitários para todas as funções
4. **Type Hints**: Adicione type hints para melhorar a legibilidade

### Histórico de Versões

- **v1.0**: Documentação inicial gerada automaticamente
- **Data**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Agente**: Documentation Agent

