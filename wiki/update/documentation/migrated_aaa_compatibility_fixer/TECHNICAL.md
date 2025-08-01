# Documentação Técnica - migrated_aaa_compatibility_fixer

## Análise Estática

### Métricas de Código
- **Linhas de código**: 841
- **Complexidade ciclomática**: 58.00
- **Funções**: 19
- **Classes**: 1
- **Imports**: 5

### Análise de Complexidade
- **Nível**: Alto (Código complexo, considere refatoração)\n
### Estrutura de Dependências

#### Imports Externos
.AgentintegratorModule, json, shutil, time, datetime.datetime

#### Hierarquia de Classes
- AAACompatibilityFixer (sem herança)\n
### Análise de Funções

#### Funções Principais
**main**
- Parâmetros: 0
- Linhas: 26
- Documentação: Sim

**integrate_with_module**
- Parâmetros: 0
- Linhas: 3
- Documentação: Sim

**__init__**
- Parâmetros: 2
- Linhas: 16
- Documentação: Não

**fix_all_compatibility_issues**
- Parâmetros: 1
- Linhas: 59
- Documentação: Sim

**fix_rules_folder**
- Parâmetros: 1
- Linhas: 59
- Documentação: Sim

**create_aaa_rules_file**
- Parâmetros: 2
- Linhas: 131
- Documentação: Sim

**create_basic_rule_file**
- Parâmetros: 3
- Linhas: 35
- Documentação: Sim

**optimize_compatibility**
- Parâmetros: 1
- Linhas: 53
- Documentação: Sim

**fix_json_maps**
- Parâmetros: 1
- Linhas: 49
- Documentação: Sim

**create_basic_agents_map**
- Parâmetros: 2
- Linhas: 29
- Documentação: Sim

**fix_agents_map_structure**
- Parâmetros: 3
- Linhas: 13
- Documentação: Sim

**fix_invalid_json**
- Parâmetros: 2
- Linhas: 8
- Documentação: Sim

**fix_agent_integration**
- Parâmetros: 1
- Linhas: 55
- Documentação: Sim

**create_basic_agent_config**
- Parâmetros: 2
- Linhas: 46
- Documentação: Sim

**validate_fixes**
- Parâmetros: 1
- Linhas: 55
- Documentação: Sim

**calculate_final_compatibility_score**
- Parâmetros: 1
- Linhas: 16
- Documentação: Sim

**calculate_overall_fix_status**
- Parâmetros: 2
- Linhas: 32
- Documentação: Sim

**save_fix_results**
- Parâmetros: 2
- Linhas: 9
- Documentação: Sim

**generate_fix_report**
- Parâmetros: 2
- Linhas: 61
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

