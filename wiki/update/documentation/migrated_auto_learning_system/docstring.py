"""
migrated_auto_learning_system



Módulo: migrated_auto_learning_system
Caminho: wiki\update\modules\tools\git_automation\migrated_auto_learning_system.py
Linhas de código: 456
Complexidade: 31.00

Funções (25):
- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self, base_path): ...\n- create_directory_structure(self): Cria estrutura de pastas necessária...\n- load_config(self): Carrega configuração do sistema...\n- save_config(self, config): Salva configuração do sistema...\n- start_learning_background(self): Inicia thread de aprendizado em background...\n- stop_learning_background(self): Para thread de aprendizado...\n- _learning_loop(self): Loop principal de aprendizado em background...\n- _perform_learning_cycle(self): Executa um ciclo completo de aprendizado...\n- _save_learning_results(self, patterns, optimizations): Salva resultados do aprendizado...\n- record_interaction(self, interaction_data): Registra uma nova interação no sistema...\n- _check_immediate_optimizations(self, interaction_data): Verifica otimizações que podem ser aplicadas imedi...\n- _find_similar_patterns(self, interaction_data): Encontra padrões similares à interação atual...\n- _calculate_context_similarity(self, context, keywords): Calcula similaridade entre contexto e palavras-cha...\n- get_learning_stats(self): Retorna estatísticas do sistema de aprendizado...\n- get_recommendations(self, context): Retorna recomendações baseadas no contexto atual...\n- update_feedback(self, interaction_id, feedback, score): Atualiza feedback de uma interação...\n- _trigger_relearning(self): Dispara relearning baseado em feedback negativo...\n- generate_learning_report(self): Gera relatório completo do sistema de aprendizado...\n- _generate_system_recommendations(self): Gera recomendações para melhorar o sistema...\n- shutdown(self): Desliga o sistema de aprendizado...\n- _save_current_state(self): Salva estado atual do sistema...\n- get_rule_recommendations(self, context): Obtém recomendações de regras baseado no contexto...\n- apply_rule_optimizations(self): Aplica otimizações de regras aprendidas...\n- analyze_rule_patterns(self): Analisa padrões de uso das regras...\n
Classes (3):
- InteractionData: Dados de uma interação do sistema...\n- LearningPattern: Padrão aprendido pelo sistema...\n- AutoLearningSystem: Sistema principal de auto aprendizado BMAD...\n  - __init__(self, base_path): ...\n  - create_directory_structure(self): Cria estrutura de pastas neces...\n  - load_config(self): Carrega configuração do sistem...\n  - save_config(self, config): Salva configuração do sistema...\n  - start_learning_background(self): Inicia thread de aprendizado e...\n  - stop_learning_background(self): Para thread de aprendizado...\n  - _learning_loop(self): Loop principal de aprendizado ...\n  - _perform_learning_cycle(self): Executa um ciclo completo de a...\n  - _save_learning_results(self, patterns, optimizations): Salva resultados do aprendizad...\n  - record_interaction(self, interaction_data): Registra uma nova interação no...\n  - _check_immediate_optimizations(self, interaction_data): Verifica otimizações que podem...\n  - _find_similar_patterns(self, interaction_data): Encontra padrões similares à i...\n  - _calculate_context_similarity(self, context, keywords): Calcula similaridade entre con...\n  - get_learning_stats(self): Retorna estatísticas do sistem...\n  - get_recommendations(self, context): Retorna recomendações baseadas...\n  - update_feedback(self, interaction_id, feedback, score): Atualiza feedback de uma inter...\n  - _trigger_relearning(self): Dispara relearning baseado em ...\n  - generate_learning_report(self): Gera relatório completo do sis...\n  - _generate_system_recommendations(self): Gera recomendações para melhor...\n  - shutdown(self): Desliga o sistema de aprendiza...\n  - _save_current_state(self): Salva estado atual do sistema...\n  - get_rule_recommendations(self, context): Obtém recomendações de regras ...\n  - apply_rule_optimizations(self): Aplica otimizações de regras a...\n  - analyze_rule_patterns(self): Analisa padrões de uso das reg...\n
Imports (7):
.GitautomationModule, json, time, threading, datetime.datetime, datetime.timedelta, statistics

Autor: Documentation Agent
Data: 2025-08-01 15:05:52
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

