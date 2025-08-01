# Documentação Técnica - migrated_advanced_prompt_system

## Análise Estática

### Métricas de Código
- **Linhas de código**: 761
- **Complexidade ciclomática**: 77.00
- **Funções**: 37
- **Classes**: 4
- **Imports**: 7

### Análise de Complexidade
- **Nível**: Alto (Código complexo, considere refatoração)\n
### Estrutura de Dependências

#### Imports Externos
.GitautomationModule, json, re, hashlib, datetime.datetime, datetime.timedelta, statistics

#### Hierarquia de Classes
- PromptOptimization (sem herança)\n- ThoughtNode (sem herança)\n- PromptEvaluation (sem herança)\n- AdvancedPromptSystem (sem herança)\n
### Análise de Funções

#### Funções Principais
**integrate_with_module**
- Parâmetros: 0
- Linhas: 3
- Documentação: Sim

**__init__**
- Parâmetros: 2
- Linhas: 20
- Documentação: Não

**create_directory_structure**
- Parâmetros: 1
- Linhas: 10
- Documentação: Sim

**load_config**
- Parâmetros: 1
- Linhas: 21
- Documentação: Sim

**save_config**
- Parâmetros: 2
- Linhas: 4
- Documentação: Sim

**optimize_prompt**
- Parâmetros: 3
- Linhas: 41
- Documentação: Sim

**evaluate_prompt**
- Parâmetros: 2
- Linhas: 34
- Documentação: Sim

**apply_tree_of_thought**
- Parâmetros: 3
- Linhas: 35
- Documentação: Sim

**apply_self_consistency**
- Parâmetros: 3
- Linhas: 20
- Documentação: Sim

**apply_generated_knowledge**
- Parâmetros: 3
- Linhas: 9
- Documentação: Sim

**_select_optimization_technique**
- Parâmetros: 3
- Linhas: 14
- Documentação: Sim

**_apply_optimization_technique**
- Parâmetros: 4
- Linhas: 16
- Documentação: Sim

**_comprehensive_rewrite**
- Parâmetros: 3
- Linhas: 14
- Documentação: Sim

**_enhance_clarity**
- Parâmetros: 2
- Linhas: 16
- Documentação: Sim

**_improve_specificity**
- Parâmetros: 3
- Linhas: 17
- Documentação: Sim

**_enhance_completeness**
- Parâmetros: 3
- Linhas: 15
- Documentação: Sim

**_apply_tot_to_prompt**
- Parâmetros: 3
- Linhas: 17
- Documentação: Sim

**_apply_role_prompting**
- Parâmetros: 3
- Linhas: 12
- Documentação: Sim

**_detect_task_type**
- Parâmetros: 2
- Linhas: 12
- Documentação: Sim

**_determine_appropriate_role**
- Parâmetros: 2
- Linhas: 20
- Documentação: Sim

**_calculate_clarity_score**
- Parâmetros: 2
- Linhas: 23
- Documentação: Sim

**_calculate_specificity_score**
- Parâmetros: 2
- Linhas: 16
- Documentação: Sim

**_calculate_completeness_score**
- Parâmetros: 2
- Linhas: 17
- Documentação: Sim

**_generate_evaluation_suggestions**
- Parâmetros: 4
- Linhas: 17
- Documentação: Sim

**_calculate_optimization_confidence**
- Parâmetros: 2
- Linhas: 9
- Documentação: Sim

**_generate_optimization_reasoning**
- Parâmetros: 3
- Linhas: 14
- Documentação: Sim

**_estimate_improvement**
- Parâmetros: 2
- Linhas: 9
- Documentação: Sim

**_generate_child_thoughts**
- Parâmetros: 3
- Linhas: 23
- Documentação: Sim

**_evaluate_thought**
- Parâmetros: 2
- Linhas: 13
- Documentação: Sim

**_calculate_thought_confidence**
- Parâmetros: 2
- Linhas: 11
- Documentação: Sim

**_generate_thought_chain**
- Parâmetros: 2
- Linhas: 12
- Documentação: Sim

**_analyze_consistency**
- Parâmetros: 2
- Linhas: 22
- Documentação: Sim

**_select_most_consistent_response**
- Parâmetros: 3
- Linhas: 15
- Documentação: Sim

**_generate_relevant_knowledge**
- Parâmetros: 3
- Linhas: 28
- Documentação: Sim

**_integrate_knowledge_into_prompt**
- Parâmetros: 3
- Linhas: 12
- Documentação: Sim

**get_optimization_stats**
- Parâmetros: 1
- Linhas: 10
- Documentação: Sim

**_get_most_used_technique**
- Parâmetros: 1
- Linhas: 9
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

