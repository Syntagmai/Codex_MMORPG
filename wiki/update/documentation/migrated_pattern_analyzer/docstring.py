"""
migrated_pattern_analyzer



Módulo: migrated_pattern_analyzer
Caminho: wiki\update\modules\analysis\source_analyzer\migrated_pattern_analyzer.py
Linhas de código: 614
Complexidade: 62.00

Funções (25):
- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self, models_path): ...\n- load_patterns(self): Carrega padrões aprendidos do arquivo...\n- load_clusters(self): Carrega clusters de padrões do arquivo...\n- save_patterns(self): Salva padrões aprendidos no arquivo...\n- save_clusters(self): Salva clusters de padrões no arquivo...\n- analyze_patterns(self, interactions): Analisa interações e identifica padrões...\n- _extract_features(self, interactions): Extrai características das interações...\n- _identify_success_patterns(self, interactions, features): Identifica padrões de sucesso...\n- _identify_failure_patterns(self, interactions, features): Identifica padrões de falha...\n- _identify_optimization_patterns(self, interactions, features): Identifica padrões de otimização...\n- _analyze_context_patterns(self, interactions): Analisa padrões de contexto...\n- _analyze_agent_patterns(self, interactions): Analisa padrões de combinação de agentes...\n- _analyze_workflow_patterns(self, interactions): Analisa padrões de workflow...\n- _analyze_error_patterns(self, interactions): Analisa padrões de erro...\n- _extract_error_type(self, error_message): Extrai tipo de erro da mensagem...\n- _create_pattern_clusters(self, patterns): Cria clusters de padrões similares...\n- _calculate_cluster_center(self, patterns): Calcula o centro de um cluster de padrões...\n- _calculate_pattern_scores(self, patterns, clusters): Calcula scores de confiança para padrões...\n- _generate_pattern_id(self, pattern_type): Gera ID único para um padrão...\n- _save_learned_patterns(self, patterns): Salva padrões aprendidos...\n- _limit_patterns_per_type(self): Limita número de padrões por tipo...\n- find_similar_patterns(self, context, pattern_type): Encontra padrões similares ao contexto atual...\n- _calculate_pattern_similarity(self, context, pattern): Calcula similaridade entre contexto e padrão...\n- _get_matched_features(self, context, pattern): Retorna características que deram match...\n
Classes (3):
- PatternMatch: Match de um padrão em uma interação...\n- PatternCluster: Cluster de padrões similares...\n- PatternAnalyzer: Analisador de padrões para identificação de aprend...\n  - __init__(self, models_path): ...\n  - load_patterns(self): Carrega padrões aprendidos do ...\n  - load_clusters(self): Carrega clusters de padrões do...\n  - save_patterns(self): Salva padrões aprendidos no ar...\n  - save_clusters(self): Salva clusters de padrões no a...\n  - analyze_patterns(self, interactions): Analisa interações e identific...\n  - _extract_features(self, interactions): Extrai características das int...\n  - _identify_success_patterns(self, interactions, features): Identifica padrões de sucesso...\n  - _identify_failure_patterns(self, interactions, features): Identifica padrões de falha...\n  - _identify_optimization_patterns(self, interactions, features): Identifica padrões de otimizaç...\n  - _analyze_context_patterns(self, interactions): Analisa padrões de contexto...\n  - _analyze_agent_patterns(self, interactions): Analisa padrões de combinação ...\n  - _analyze_workflow_patterns(self, interactions): Analisa padrões de workflow...\n  - _analyze_error_patterns(self, interactions): Analisa padrões de erro...\n  - _extract_error_type(self, error_message): Extrai tipo de erro da mensage...\n  - _create_pattern_clusters(self, patterns): Cria clusters de padrões simil...\n  - _calculate_cluster_center(self, patterns): Calcula o centro de um cluster...\n  - _calculate_pattern_scores(self, patterns, clusters): Calcula scores de confiança pa...\n  - _generate_pattern_id(self, pattern_type): Gera ID único para um padrão...\n  - _save_learned_patterns(self, patterns): Salva padrões aprendidos...\n  - _limit_patterns_per_type(self): Limita número de padrões por t...\n  - find_similar_patterns(self, context, pattern_type): Encontra padrões similares ao ...\n  - _calculate_pattern_similarity(self, context, pattern): Calcula similaridade entre con...\n  - _get_matched_features(self, context, pattern): Retorna características que de...\n
Imports (6):
.SourceanalyzerModule, json, hashlib, datetime.datetime, datetime.timedelta, statistics

Autor: Documentation Agent
Data: 2025-08-01 15:05:58
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

