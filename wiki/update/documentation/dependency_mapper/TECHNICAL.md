# Documentação Técnica - dependency_mapper

## Análise Estática

### Métricas de Código
- **Linhas de código**: 67
- **Complexidade ciclomática**: 7.00
- **Funções**: 7
- **Classes**: 2
- **Imports**: 9

### Análise de Complexidade
- **Nível**: Médio (Código moderadamente complexo)\n
### Estrutura de Dependências

#### Imports Externos
ast, json, pathlib.Path, typing.Dict, typing.List, typing.Any, typing.Optional, typing.Set, datetime.datetime

#### Hierarquia de Classes
- DependencyMapper (sem herança)\n- ImportVisitor (sem herança)\n
### Análise de Funções

#### Funções Principais
**main**
- Parâmetros: 0
- Linhas: 3
- Documentação: Não

**__init__**
- Parâmetros: 1
- Linhas: 2
- Documentação: Não

**map_dependencies**
- Parâmetros: 2
- Linhas: 14
- Documentação: Não

**_analyze_file_dependencies**
- Parâmetros: 2
- Linhas: 11
- Documentação: Não

**__init__**
- Parâmetros: 1
- Linhas: 1
- Documentação: Não

**visit_Import**
- Parâmetros: 2
- Linhas: 3
- Documentação: Não

**visit_ImportFrom**
- Parâmetros: 2
- Linhas: 3
- Documentação: Não

### Recomendações

1. **Documentação**: Adicione docstrings para todas as funções e classes
2. **Complexidade**: Considere refatorar funções muito complexas
3. **Testes**: Implemente testes unitários para todas as funções
4. **Type Hints**: Adicione type hints para melhorar a legibilidade

### Histórico de Versões

- **v1.0**: Documentação inicial gerada automaticamente
- **Data**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Agente**: Documentation Agent

