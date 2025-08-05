"""
analyze_navigation_optimization

Script de Análise de Otimização de Navegação
Analisa se todos os caminhos referenciados no cursor.md estão otimizados

Módulo: analyze_navigation_optimization
Caminho: wiki\update\analyze_navigation_optimization.py
Linhas de código: 451
Complexidade: 60.00

Funções (12):
- main(): Função principal...\n- __init__(self): ...\n- analyze_tags_index_optimization(self): Analisa otimização do tags_index.json...\n- analyze_wiki_map_optimization(self): Analisa otimização do wiki_map.json...\n- analyze_rules_optimization(self): Analisa otimização das regras...\n- analyze_enhanced_context_system(self): Analisa otimização do sistema de contexto avançado...\n- analyze_intelligent_navigation(self): Analisa otimização da navegação inteligente...\n- analyze_performance_metrics(self): Analisa métricas de performance dos caminhos...\n- calculate_path_optimization_score(self, path, access_time): Calcula score de otimização para um caminho...\n- generate_optimization_report(self): Gera relatório completo de otimização...\n- get_grade(self, score): Converte score em nota...\n- generate_optimization_recommendations(self, score): Gera recomendações baseadas no score...\n
Classes (1):
- NavigationOptimizationAnalyzer: ...\n  - __init__(self): ...\n  - analyze_tags_index_optimization(self): Analisa otimização do tags_ind...\n  - analyze_wiki_map_optimization(self): Analisa otimização do wiki_map...\n  - analyze_rules_optimization(self): Analisa otimização das regras...\n  - analyze_enhanced_context_system(self): Analisa otimização do sistema ...\n  - analyze_intelligent_navigation(self): Analisa otimização da navegaçã...\n  - analyze_performance_metrics(self): Analisa métricas de performanc...\n  - calculate_path_optimization_score(self, path, access_time): Calcula score de otimização pa...\n  - generate_optimization_report(self): Gera relatório completo de oti...\n  - get_grade(self, score): Converte score em nota...\n  - generate_optimization_recommendations(self, score): Gera recomendações baseadas no...\n
Imports (4):
json, time, datetime.datetime, pathlib.Path

Autor: Documentation Agent
Data: 2025-08-01 15:05:50
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

