"""
migrated_prompt_evaluator



Módulo: migrated_prompt_evaluator
Caminho: wiki\update\modules\tools\git_automation\migrated_prompt_evaluator.py
Linhas de código: 531
Complexidade: 46.00

Funções (18):
- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self): ...\n- _load_evaluation_patterns(self): Carrega padrões de avaliação...\n- evaluate_prompt(self, prompt, context): Avalia um prompt completo...\n- _calculate_clarity_score(self, prompt): Calcula score de clareza...\n- _calculate_specificity_score(self, prompt, context): Calcula score de especificidade...\n- _calculate_completeness_score(self, prompt): Calcula score de completude...\n- _calculate_structure_score(self, prompt): Calcula score de estrutura...\n- _calculate_context_score(self, prompt, context): Calcula score de contexto...\n- _calculate_overall_score(self, scores): Calcula score geral ponderado...\n- _generate_suggestions(self, scores): Gera sugestões baseadas nos scores...\n- _create_detailed_analysis(self, prompt, metrics): Cria análise detalhada do prompt...\n- _generate_recommendations(self, metrics, context): Gera recomendações específicas...\n- _calculate_evaluation_confidence(self, metrics): Calcula confiança da avaliação...\n- _generate_prompt_id(self, prompt): Gera ID único para o prompt...\n- batch_evaluate(self, prompts, context): Avalia múltiplos prompts...\n- get_evaluation_stats(self): Retorna estatísticas de avaliação...\n- _calculate_improvement_trend(self): Calcula tendência de melhoria...\n
Classes (3):
- PromptMetrics: Métricas de avaliação de prompt...\n- EvaluationResult: Resultado completo de avaliação...\n- PromptEvaluator: Avaliador especializado de prompts...\n  - __init__(self): ...\n  - _load_evaluation_patterns(self): Carrega padrões de avaliação...\n  - evaluate_prompt(self, prompt, context): Avalia um prompt completo...\n  - _calculate_clarity_score(self, prompt): Calcula score de clareza...\n  - _calculate_specificity_score(self, prompt, context): Calcula score de especificidad...\n  - _calculate_completeness_score(self, prompt): Calcula score de completude...\n  - _calculate_structure_score(self, prompt): Calcula score de estrutura...\n  - _calculate_context_score(self, prompt, context): Calcula score de contexto...\n  - _calculate_overall_score(self, scores): Calcula score geral ponderado...\n  - _generate_suggestions(self, scores): Gera sugestões baseadas nos sc...\n  - _create_detailed_analysis(self, prompt, metrics): Cria análise detalhada do prom...\n  - _generate_recommendations(self, metrics, context): Gera recomendações específicas...\n  - _calculate_evaluation_confidence(self, metrics): Calcula confiança da avaliação...\n  - _generate_prompt_id(self, prompt): Gera ID único para o prompt...\n  - batch_evaluate(self, prompts, context): Avalia múltiplos prompts...\n  - get_evaluation_stats(self): Retorna estatísticas de avalia...\n  - _calculate_improvement_trend(self): Calcula tendência de melhoria...\n
Imports (5):
.GitautomationModule, re, statistics, datetime.datetime, hashlib

Autor: Documentation Agent
Data: 2025-08-01 15:05:52
"""
