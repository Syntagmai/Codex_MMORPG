# migrated_knowledge_manager

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_knowledge_manager
- **Caminho**: wiki\update\modules\agents\agent_orchestrator\migrated_knowledge_manager.py
- **Linhas de código**: 682
- **Complexidade**: 59.00
- **Funções**: 23
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 35

Função principal para teste do agente

### integrate_with_module

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Integra o script com o módulo de destino.

### __init__

**Parâmetros**: self, workspace_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Sem documentação.

### load_navigation_maps

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Carrega mapas de navegação da wiki

### process_workflow_results

**Parâmetros**: self, analysis_results, generation_results, test_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 53

Processa resultados do workflow completo e extrai insights

Args:
    analysis_results: Resultados do Module Analyzer
    generation_results: Resultados do Module Generator
    test_results: Resultados do Module Tester
    
Returns:
    Insights e aprendizados extraídos

### extract_analysis_insights

**Parâmetros**: self, analysis_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 44

Extrai insights dos resultados de análise

### extract_generation_insights

**Parâmetros**: self, generation_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 53

Extrai insights dos resultados de geração

### extract_test_insights

**Parâmetros**: self, test_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Extrai insights dos resultados de teste

### identify_patterns

**Parâmetros**: self, analysis_results, generation_results, test_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Identifica padrões nos resultados

### analyze_success_patterns

**Parâmetros**: self, successful_variations
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Analisa padrões de sucesso

### analyze_failure_patterns

**Parâmetros**: self, failed_variations
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Analisa padrões de falha

### analyze_code_patterns

**Parâmetros**: self, analysis_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Analisa padrões de código

### analyze_structural_patterns

**Parâmetros**: self, analysis_results, generation_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Analisa padrões estruturais

### generate_rules

**Parâmetros**: self, insights, patterns
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Gera regras baseadas nos insights e padrões

### generate_recommendations

**Parâmetros**: self, learning_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Gera recomendações baseadas nos dados de aprendizado

### update_knowledge_base

**Parâmetros**: self, learning_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 33

Atualiza base de conhecimento com novos dados

### save_knowledge_base

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Salva base de conhecimento em arquivo

### save_learning_data

**Parâmetros**: self, module_name, learning_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Salva dados de aprendizado

### analyze_file_types

**Parâmetros**: self, files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Analisa tipos de arquivo

### analyze_score_distribution

**Parâmetros**: self, scores
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Analisa distribuição de scores

### get_common_patterns

**Parâmetros**: self, patterns, top_n
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Obtém padrões mais comuns

### get_wiki_knowledge

**Parâmetros**: self, topic
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Obtém conhecimento da wiki sobre um tópico específico

### update_navigation_maps

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Atualiza mapas de navegação com novos dados

## Classes

### KnowledgeManagerAgent

**Herança**: Nenhuma
**Atributos**: learning_data, analysis_insights, generation_insights, test_insights, insights, metrics, patterns, dependencies, structure, insights, total_variations, successful_variations, variation_patterns, modification_patterns, compatibility_scores, insights, summary, error_patterns, patterns, successful_variations, failed_variations, patterns, mod_counts, naming_patterns, patterns, error_types, patterns, lua_patterns, patterns, files, file_types, rules, generation_insights, success_rate, test_insights, pass_rate, quality_insights, avg_quality, recommendations, insights, patterns, generation_insights, success_rate, test_insights, pass_rate, updates, new_patterns, new_rules, new_insights, knowledge_file, learning_file, file_types, distribution, pattern_counts, sorted_patterns, knowledge, tags_file, wiki_map_file, relationships_file, variation_name, modifications, modifications, name, ext, ext
**Métodos**: 21
**Linhas**: 597

Agente especializado em gerenciamento de conhecimento e navegação da wiki

#### __init__

**Parâmetros**: self, workspace_path
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Sem documentação.

#### load_navigation_maps

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 31

Carrega mapas de navegação da wiki

#### process_workflow_results

**Parâmetros**: self, analysis_results, generation_results, test_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 53

Processa resultados do workflow completo e extrai insights

Args:
    analysis_results: Resultados do Module Analyzer
    generation_results: Resultados do Module Generator
    test_results: Resultados do Module Tester
    
Returns:
    Insights e aprendizados extraídos

#### extract_analysis_insights

**Parâmetros**: self, analysis_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 44

Extrai insights dos resultados de análise

#### extract_generation_insights

**Parâmetros**: self, generation_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 53

Extrai insights dos resultados de geração

#### extract_test_insights

**Parâmetros**: self, test_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Extrai insights dos resultados de teste

#### identify_patterns

**Parâmetros**: self, analysis_results, generation_results, test_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Identifica padrões nos resultados

#### analyze_success_patterns

**Parâmetros**: self, successful_variations
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Analisa padrões de sucesso

#### analyze_failure_patterns

**Parâmetros**: self, failed_variations
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Analisa padrões de falha

#### analyze_code_patterns

**Parâmetros**: self, analysis_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 28

Analisa padrões de código

#### analyze_structural_patterns

**Parâmetros**: self, analysis_results, generation_results
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 26

Analisa padrões estruturais

#### generate_rules

**Parâmetros**: self, insights, patterns
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 36

Gera regras baseadas nos insights e padrões

#### generate_recommendations

**Parâmetros**: self, learning_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Gera recomendações baseadas nos dados de aprendizado

#### update_knowledge_base

**Parâmetros**: self, learning_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 33

Atualiza base de conhecimento com novos dados

#### save_knowledge_base

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 9

Salva base de conhecimento em arquivo

#### save_learning_data

**Parâmetros**: self, module_name, learning_data
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 13

Salva dados de aprendizado

#### analyze_file_types

**Parâmetros**: self, files
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 6

Analisa tipos de arquivo

#### analyze_score_distribution

**Parâmetros**: self, scores
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 19

Analisa distribuição de scores

#### get_common_patterns

**Parâmetros**: self, patterns, top_n
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 8

Obtém padrões mais comuns

#### get_wiki_knowledge

**Parâmetros**: self, topic
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 21

Obtém conhecimento da wiki sobre um tópico específico

#### update_navigation_maps

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 5

Atualiza mapas de navegação com novos dados

## Imports

.AgentorchestratorModule, os, json, datetime.datetime

## Uso

```python
# Exemplo de uso do módulo migrated_knowledge_manager
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:59
