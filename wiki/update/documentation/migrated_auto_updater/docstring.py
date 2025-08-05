"""
migrated_auto_updater



Módulo: migrated_auto_updater
Caminho: wiki\update\modules\maps\map_updater\migrated_auto_updater.py
Linhas de código: 753
Complexidade: 84.00

Funções (26):
- main(): Função principal...\n- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self): ...\n- setup_logging(self): Configura sistema de logging...\n- trigger_auto_update(self, change_type, details): Dispara atualização automática baseada no tipo de ...\n- update_maps(self, details): Atualiza mapas JSON automaticamente...\n- update_rules(self, details): Atualiza regras automaticamente...\n- update_scripts(self, details): Atualiza scripts automaticamente...\n- update_context(self, details): Atualiza contexto automaticamente...\n- update_performance(self, details): Atualiza performance automaticamente...\n- validate_maps(self): Valida mapas após atualização...\n- scan_rules_consistency(self): Escaneia consistência das regras...\n- resolve_rule_conflicts(self, issues): Resolve conflitos de regras...\n- optimize_rule_structure(self): Otimiza estrutura de regras...\n- optimize_script_performance(self): Otimiza performance dos scripts...\n- fix_script_errors(self): Corrige erros nos scripts...\n- update_script_dependencies(self): Atualiza dependências dos scripts...\n- detect_context_changes(self): Detecta mudanças de contexto...\n- update_context_maps(self, changes): Atualiza mapas de contexto...\n- optimize_navigation_patterns(self): Otimiza padrões de navegação...\n- apply_performance_optimizations(self): Aplica otimizações de performance baseadas na anál...\n- apply_cache_optimizations(self): Aplica otimizações de cache...\n- apply_search_optimizations(self): Aplica otimizações de busca...\n- apply_structure_optimizations(self): Aplica otimizações de estrutura...\n- save_update_history(self): Salva histórico de atualizações...\n- get_update_stats(self): Retorna estatísticas de atualização...\n
Classes (1):
- AutoUpdater: ...\n  - __init__(self): ...\n  - setup_logging(self): Configura sistema de logging...\n  - trigger_auto_update(self, change_type, details): Dispara atualização automática...\n  - update_maps(self, details): Atualiza mapas JSON automatica...\n  - update_rules(self, details): Atualiza regras automaticament...\n  - update_scripts(self, details): Atualiza scripts automaticamen...\n  - update_context(self, details): Atualiza contexto automaticame...\n  - update_performance(self, details): Atualiza performance automatic...\n  - validate_maps(self): Valida mapas após atualização...\n  - scan_rules_consistency(self): Escaneia consistência das regr...\n  - resolve_rule_conflicts(self, issues): Resolve conflitos de regras...\n  - optimize_rule_structure(self): Otimiza estrutura de regras...\n  - optimize_script_performance(self): Otimiza performance dos script...\n  - fix_script_errors(self): Corrige erros nos scripts...\n  - update_script_dependencies(self): Atualiza dependências dos scri...\n  - detect_context_changes(self): Detecta mudanças de contexto...\n  - update_context_maps(self, changes): Atualiza mapas de contexto...\n  - optimize_navigation_patterns(self): Otimiza padrões de navegação...\n  - apply_performance_optimizations(self): Aplica otimizações de performa...\n  - apply_cache_optimizations(self): Aplica otimizações de cache...\n  - apply_search_optimizations(self): Aplica otimizações de busca...\n  - apply_structure_optimizations(self): Aplica otimizações de estrutur...\n  - save_update_history(self): Salva histórico de atualizaçõe...\n  - get_update_stats(self): Retorna estatísticas de atuali...\n
Imports (7):
.MapupdaterModule, json, time, subprocess, sys, datetime.datetime, logging

Autor: Documentation Agent
Data: 2025-08-01 15:05:54
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

