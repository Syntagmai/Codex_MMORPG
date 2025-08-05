"""
migrated_prompt_optimizer



Módulo: migrated_prompt_optimizer
Caminho: wiki\update\modules\tools\git_automation\migrated_prompt_optimizer.py
Linhas de código: 448
Complexidade: 34.00

Funções (22):
- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self): ...\n- _load_optimization_templates(self): Carrega templates de otimização...\n- _load_detection_patterns(self): Carrega padrões de detecção...\n- optimize_prompt(self, prompt, context): Otimiza um prompt usando múltiplas técnicas...\n- _detect_task_type(self, prompt): Detecta tipo de tarefa do prompt...\n- _needs_role_prompting(self, prompt): Verifica se prompt precisa de role prompting...\n- _needs_clarity_improvement(self, prompt): Verifica se prompt precisa de melhoria de clareza...\n- _needs_chain_of_thought(self, prompt, task_type): Verifica se prompt precisa de chain-of-thought...\n- _needs_specificity_improvement(self, prompt): Verifica se prompt precisa de melhoria de especifi...\n- _needs_structured_output(self, prompt, task_type): Verifica se prompt precisa de saída estruturada...\n- _apply_role_prompting(self, prompt, task_type, context): Aplica role prompting...\n- _improve_clarity(self, prompt): Melhora clareza do prompt...\n- _apply_chain_of_thought(self, prompt): Aplica chain-of-thought...\n- _improve_specificity(self, prompt, context): Melhora especificidade do prompt...\n- _add_structured_output(self, prompt, task_type): Adiciona estrutura de saída...\n- _extract_technology(self, context): Extrai tecnologia do contexto...\n- _extract_subject(self, context): Extrai assunto do contexto...\n- _extract_domain(self, context): Extrai domínio do contexto...\n- _calculate_improvement_score(self, original, optimized): Calcula score de melhoria...\n- batch_optimize(self, prompts, context): Otimiza múltiplos prompts...\n- get_optimization_stats(self, results): Retorna estatísticas de otimização...\n
Classes (2):
- OptimizationResult: Resultado de uma otimização de prompt...\n- PromptOptimizer: Otimizador especializado de prompts...\n  - __init__(self): ...\n  - _load_optimization_templates(self): Carrega templates de otimizaçã...\n  - _load_detection_patterns(self): Carrega padrões de detecção...\n  - optimize_prompt(self, prompt, context): Otimiza um prompt usando múlti...\n  - _detect_task_type(self, prompt): Detecta tipo de tarefa do prom...\n  - _needs_role_prompting(self, prompt): Verifica se prompt precisa de ...\n  - _needs_clarity_improvement(self, prompt): Verifica se prompt precisa de ...\n  - _needs_chain_of_thought(self, prompt, task_type): Verifica se prompt precisa de ...\n  - _needs_specificity_improvement(self, prompt): Verifica se prompt precisa de ...\n  - _needs_structured_output(self, prompt, task_type): Verifica se prompt precisa de ...\n  - _apply_role_prompting(self, prompt, task_type, context): Aplica role prompting...\n  - _improve_clarity(self, prompt): Melhora clareza do prompt...\n  - _apply_chain_of_thought(self, prompt): Aplica chain-of-thought...\n  - _improve_specificity(self, prompt, context): Melhora especificidade do prom...\n  - _add_structured_output(self, prompt, task_type): Adiciona estrutura de saída...\n  - _extract_technology(self, context): Extrai tecnologia do contexto...\n  - _extract_subject(self, context): Extrai assunto do contexto...\n  - _extract_domain(self, context): Extrai domínio do contexto...\n  - _calculate_improvement_score(self, original, optimized): Calcula score de melhoria...\n  - batch_optimize(self, prompts, context): Otimiza múltiplos prompts...\n  - get_optimization_stats(self, results): Retorna estatísticas de otimiz...\n
Imports (2):
.GitautomationModule, re

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

