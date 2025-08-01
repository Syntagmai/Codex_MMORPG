# Documentação Técnica - migrated_file_mover

## Análise Estática

### Métricas de Código
- **Linhas de código**: 342
- **Complexidade ciclomática**: 41.00
- **Funções**: 10
- **Classes**: 1
- **Imports**: 8

### Análise de Complexidade
- **Nível**: Alto (Código complexo, considere refatoração)\n
### Estrutura de Dependências

#### Imports Externos
.FilemoverModule, os, sys, json, shutil, argparse, logging, datetime.datetime

#### Hierarquia de Classes
- FileMover (sem herança)\n
### Análise de Funções

#### Funções Principais
**load_config**
- Parâmetros: 1
- Linhas: 7
- Documentação: Sim

**save_config**
- Parâmetros: 2
- Linhas: 7
- Documentação: Sim

**interactive_mode**
- Parâmetros: 0
- Linhas: 55
- Documentação: Sim

**main**
- Parâmetros: 0
- Linhas: 66
- Documentação: Sim

**integrate_with_module**
- Parâmetros: 0
- Linhas: 3
- Documentação: Sim

**__init__**
- Parâmetros: 3
- Linhas: 5
- Documentação: Não

**setup_backup_directory**
- Parâmetros: 2
- Linhas: 10
- Documentação: Sim

**validate_paths**
- Parâmetros: 4
- Linhas: 28
- Documentação: Sim

**move_file**
- Parâmetros: 3
- Linhas: 20
- Documentação: Sim

**move_files**
- Parâmetros: 4
- Linhas: 42
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

