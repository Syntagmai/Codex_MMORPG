"""
migrated_prompt_learning_integration



Módulo: migrated_prompt_learning_integration
Caminho: wiki\update\modules\tools\git_automation\migrated_prompt_learning_integration.py
Linhas de código: 487
Complexidade: 50.00

Funções (22):
- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self, base_path): ...\n- load_prompt_patterns(self): Carrega padrões de prompt aprendidos...\n- load_optimization_history(self): Carrega histórico de otimizações...\n- load_learning_log(self): Carrega log de aprendizado...\n- save_prompt_patterns(self): Salva padrões de prompt aprendidos...\n- save_optimization_history(self): Salva histórico de otimizações...\n- save_learning_log(self): Salva log de aprendizado...\n- record_prompt_optimization(self, result): Registra resultado de otimização de prompt...\n- _update_prompt_patterns(self, result): Atualiza padrões de prompt baseado em resultado be...\n- _detect_prompt_type(self, prompt): Detecta tipo de prompt...\n- get_optimization_recommendation(self, prompt, context): Obtém recomendação de otimização baseada em padrõe...\n- _calculate_context_relevance(self, pattern, context): Calcula relevância de contexto para um padrão...\n- analyze_optimization_effectiveness(self): Analisa efetividade das otimizações...\n- get_learning_recommendations(self): Gera recomendações baseadas no aprendizado...\n- generate_learning_report(self): Gera relatório de aprendizado...\n- _get_top_patterns(self): Retorna padrões mais bem-sucedidos...\n- apply_learned_optimizations(self, prompt, context): Aplica otimizações aprendidas a um prompt...\n- _apply_role_prompting(self, prompt, context): Aplica role prompting baseado em contexto...\n- _apply_chain_of_thought(self, prompt): Aplica chain-of-thought...\n- _apply_specificity_improvement(self, prompt, context): Aplica melhoria de especificidade...\n- _apply_clarity_enhancement(self, prompt): Aplica melhoria de clareza...\n
Classes (3):
- PromptLearningPattern: Padrão aprendido sobre prompts...\n- PromptOptimizationResult: Resultado de otimização de prompt...\n- PromptLearningIntegration: Integração entre prompt engineering e auto-aprendi...\n  - __init__(self, base_path): ...\n  - load_prompt_patterns(self): Carrega padrões de prompt apre...\n  - load_optimization_history(self): Carrega histórico de otimizaçõ...\n  - load_learning_log(self): Carrega log de aprendizado...\n  - save_prompt_patterns(self): Salva padrões de prompt aprend...\n  - save_optimization_history(self): Salva histórico de otimizações...\n  - save_learning_log(self): Salva log de aprendizado...\n  - record_prompt_optimization(self, result): Registra resultado de otimizaç...\n  - _update_prompt_patterns(self, result): Atualiza padrões de prompt bas...\n  - _detect_prompt_type(self, prompt): Detecta tipo de prompt...\n  - get_optimization_recommendation(self, prompt, context): Obtém recomendação de otimizaç...\n  - _calculate_context_relevance(self, pattern, context): Calcula relevância de contexto...\n  - analyze_optimization_effectiveness(self): Analisa efetividade das otimiz...\n  - get_learning_recommendations(self): Gera recomendações baseadas no...\n  - generate_learning_report(self): Gera relatório de aprendizado...\n  - _get_top_patterns(self): Retorna padrões mais bem-suced...\n  - apply_learned_optimizations(self, prompt, context): Aplica otimizações aprendidas ...\n  - _apply_role_prompting(self, prompt, context): Aplica role prompting baseado ...\n  - _apply_chain_of_thought(self, prompt): Aplica chain-of-thought...\n  - _apply_specificity_improvement(self, prompt, context): Aplica melhoria de especificid...\n  - _apply_clarity_enhancement(self, prompt): Aplica melhoria de clareza...\n
Imports (6):
.GitautomationModule, json, hashlib, datetime.datetime, datetime.timedelta, statistics

Autor: Documentation Agent
Data: 2025-08-01 15:05:53
"""

## 🔗 **Links Automáticos - Scripts**

> [!info] **Script de Automação**
> Este script faz parte do sistema de automação da wiki

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]

### **🔧 Links de Scripts**
- [[../update/README|Documentação de Scripts]]
- [[../maps/scripts_index|Índice de Scripts]]
- [[../templates/README|Templates de Scripts]]

### **📊 Scripts Relacionados**
- [[../update/automatic_linkage_system.py|automatic_linkage_system.py]]
- [[../update/create_automatic_link_templates.py|create_automatic_link_templates.py]]
- [[../update/orphan_files_analyzer.py|orphan_files_analyzer.py]]
- [[../update/update_json_maps.py|update_json_maps.py]]

### **📈 Métricas do Script**
- **Nome**: docstring
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

