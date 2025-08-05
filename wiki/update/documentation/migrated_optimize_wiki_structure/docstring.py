"""
migrated_optimize_wiki_structure



Módulo: migrated_optimize_wiki_structure
Caminho: wiki\update\modules\documentation\wiki_optimizer\migrated_optimize_wiki_structure.py
Linhas de código: 413
Complexidade: 38.00

Funções (14):
- main(): Função principal...\n- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self, wiki_dir): ...\n- analyze_content_overlap(self, file1, file2): Analisa sobreposição de conteúdo entre dois arquiv...\n- extract_sections(self, content): Extrai seções do conteúdo...\n- merge_network_documents(self): Mescla documentos de rede em um só...\n- optimize_ui_documents(self): Otimiza documentos de UI...\n- extract_widget_sections(self, content): Extrai seções de widgets do conteúdo...\n- remove_repetitive_sections(self): Remove seções repetitivas desnecessárias...\n- get_section_content(self, lines, start_index): Obtém conteúdo de uma seção...\n- standardize_navigation(self): Padroniza seções de navegação...\n- generate_standard_navigation(self, filename): Gera navegação padronizada baseada no tipo de docu...\n- update_wiki_index(self): Atualiza o índice da wiki com a nova estrutura...\n- optimize_wiki_structure(self): Otimiza a estrutura completa da wiki...\n
Classes (1):
- WikiOptimizer: ...\n  - __init__(self, wiki_dir): ...\n  - analyze_content_overlap(self, file1, file2): Analisa sobreposição de conteú...\n  - extract_sections(self, content): Extrai seções do conteúdo...\n  - merge_network_documents(self): Mescla documentos de rede em u...\n  - optimize_ui_documents(self): Otimiza documentos de UI...\n  - extract_widget_sections(self, content): Extrai seções de widgets do co...\n  - remove_repetitive_sections(self): Remove seções repetitivas desn...\n  - get_section_content(self, lines, start_index): Obtém conteúdo de uma seção...\n  - standardize_navigation(self): Padroniza seções de navegação...\n  - generate_standard_navigation(self, filename): Gera navegação padronizada bas...\n  - update_wiki_index(self): Atualiza o índice da wiki com ...\n  - optimize_wiki_structure(self): Otimiza a estrutura completa d...\n
Imports (2):
.WikioptimizerModule, re

Autor: Documentation Agent
Data: 2025-08-01 15:05:57
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

