"""
migrated_rules_learning_integration



Módulo: migrated_rules_learning_integration
Caminho: wiki\update\modules\tools\git_automation\migrated_rules_learning_integration.py
Linhas de código: 468
Complexidade: 48.00

Funções (22):
- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self, base_path): ...\n- load_rule_patterns(self): Carrega padrões de regras aprendidos...\n- load_rule_optimizations(self): Carrega otimizações de regras...\n- load_rule_usage_log(self): Carrega log de uso de regras...\n- save_rule_patterns(self): Salva padrões de regras aprendidos...\n- save_rule_optimizations(self): Salva otimizações de regras...\n- save_rule_usage_log(self): Salva log de uso de regras...\n- get_all_rules(self): Obtém todas as regras do sistema...\n- parse_rule_content(self, content): Analisa conteúdo de uma regra...\n- record_rule_usage(self, rule_file, context, success_score, feedback): Registra uso de uma regra...\n- analyze_rule_patterns(self): Analisa padrões de uso das regras...\n- _analyze_context_applicability(self, usages): Analisa aplicabilidade da regra em diferentes cont...\n- _extract_context_keywords(self, context): Extrai palavras-chave do contexto...\n- _generate_rule_improvements(self, rule_file, usages): Gera sugestões de melhoria para uma regra...\n- generate_rule_optimizations(self): Gera otimizações para regras baseado em padrões ap...\n- _create_rule_optimization(self, pattern): Cria otimização para uma regra específica...\n- _generate_improved_content(self, current_content, suggestions): Gera conteúdo melhorado baseado em sugestões...\n- apply_rule_optimization(self, optimization): Aplica uma otimização de regra...\n- get_rule_recommendations(self, context): Obtém recomendações de regras baseado no contexto...\n- _calculate_context_relevance(self, pattern, context): Calcula relevância de uma regra para o contexto at...\n- generate_rules_learning_report(self): Gera relatório de aprendizado das regras...\n
Classes (3):
- RuleLearningPattern: Padrão aprendido sobre regras...\n- RuleOptimization: Otimização sugerida para uma regra...\n- RulesLearningIntegration: Sistema de integração entre auto-aprendizado e reg...\n  - __init__(self, base_path): ...\n  - load_rule_patterns(self): Carrega padrões de regras apre...\n  - load_rule_optimizations(self): Carrega otimizações de regras...\n  - load_rule_usage_log(self): Carrega log de uso de regras...\n  - save_rule_patterns(self): Salva padrões de regras aprend...\n  - save_rule_optimizations(self): Salva otimizações de regras...\n  - save_rule_usage_log(self): Salva log de uso de regras...\n  - get_all_rules(self): Obtém todas as regras do siste...\n  - parse_rule_content(self, content): Analisa conteúdo de uma regra...\n  - record_rule_usage(self, rule_file, context, success_score, feedback): Registra uso de uma regra...\n  - analyze_rule_patterns(self): Analisa padrões de uso das reg...\n  - _analyze_context_applicability(self, usages): Analisa aplicabilidade da regr...\n  - _extract_context_keywords(self, context): Extrai palavras-chave do conte...\n  - _generate_rule_improvements(self, rule_file, usages): Gera sugestões de melhoria par...\n  - generate_rule_optimizations(self): Gera otimizações para regras b...\n  - _create_rule_optimization(self, pattern): Cria otimização para uma regra...\n  - _generate_improved_content(self, current_content, suggestions): Gera conteúdo melhorado basead...\n  - apply_rule_optimization(self, optimization): Aplica uma otimização de regra...\n  - get_rule_recommendations(self, context): Obtém recomendações de regras ...\n  - _calculate_context_relevance(self, pattern, context): Calcula relevância de uma regr...\n  - generate_rules_learning_report(self): Gera relatório de aprendizado ...\n
Imports (7):
.GitautomationModule, json, re, hashlib, datetime.datetime, datetime.timedelta, statistics

Autor: Documentation Agent
Data: 2025-08-01 15:05:53
"""
