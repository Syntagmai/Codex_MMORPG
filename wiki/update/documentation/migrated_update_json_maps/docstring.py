"""
migrated_update_json_maps



Módulo: migrated_update_json_maps
Caminho: wiki\update\modules\documentation\content_validator\migrated_update_json_maps.py
Linhas de código: 511
Complexidade: 84.00

Funções (18):
- main(): Função principal...\n- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self, wiki_dir): ...\n- scan_markdown_files(self): Escaneia todos os arquivos markdown na pasta wiki...\n- extract_frontmatter(self, file_path): Extrai frontmatter de um arquivo markdown...\n- generate_tags_index(self): Gera o índice de tags...\n- generate_search_aliases(self, files_by_tag): Gera aliases de busca para tags...\n- generate_wiki_map(self): Gera o mapa completo da wiki...\n- categorize_document(self, file, frontmatter): Categoriza um documento baseado em seu conteúdo...\n- get_priority(self, file, frontmatter): Determina a prioridade de um documento...\n- get_description(self, file, frontmatter): Extrai descrição do documento...\n- generate_statistics(self, categories): Gera estatísticas da wiki...\n- generate_navigation_paths(self, categories): Gera caminhos de navegação...\n- generate_relationships(self): Gera relacionamentos entre documentos...\n- generate_learning_paths(self): Gera caminhos de aprendizado...\n- generate_dependency_graph(self, relationships): Gera grafo de dependências...\n- generate_topic_clusters(self): Gera clusters de tópicos...\n- update_all_json_files(self): Atualiza todos os arquivos JSON...\n
Classes (1):
- WikiJSONUpdater: ...\n  - __init__(self, wiki_dir): ...\n  - scan_markdown_files(self): Escaneia todos os arquivos mar...\n  - extract_frontmatter(self, file_path): Extrai frontmatter de um arqui...\n  - generate_tags_index(self): Gera o índice de tags...\n  - generate_search_aliases(self, files_by_tag): Gera aliases de busca para tag...\n  - generate_wiki_map(self): Gera o mapa completo da wiki...\n  - categorize_document(self, file, frontmatter): Categoriza um documento basead...\n  - get_priority(self, file, frontmatter): Determina a prioridade de um d...\n  - get_description(self, file, frontmatter): Extrai descrição do documento...\n  - generate_statistics(self, categories): Gera estatísticas da wiki...\n  - generate_navigation_paths(self, categories): Gera caminhos de navegação...\n  - generate_relationships(self): Gera relacionamentos entre doc...\n  - generate_learning_paths(self): Gera caminhos de aprendizado...\n  - generate_dependency_graph(self, relationships): Gera grafo de dependências...\n  - generate_topic_clusters(self): Gera clusters de tópicos...\n  - update_all_json_files(self): Atualiza todos os arquivos JSO...\n
Imports (4):
.ContentvalidatorModule, json, re, datetime.datetime

Autor: Documentation Agent
Data: 2025-08-01 15:05:56
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

