"""
migrated_update_wiki_maps



Módulo: migrated_update_wiki_maps
Caminho: wiki\update\modules\maps\wiki_indexer\migrated_update_wiki_maps.py
Linhas de código: 314
Complexidade: 37.00

Funções (10):
- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self, wiki_dir): ...\n- load_context_data(self): Carrega dados de contexto detectado...\n- scan_markdown_files(self): Escaneia todos os arquivos markdown na pasta de do...\n- extract_frontmatter(self, file_path): Extrai frontmatter de um arquivo markdown...\n- generate_tags_index(self): Gera índice de tags...\n- generate_wiki_map(self): Gera mapa da wiki...\n- categorize_document(self, file_name, frontmatter): Categoriza documento baseado no nome e tags...\n- generate_relationships(self): Gera relacionamentos entre documentos...\n- update_all_json_files(self): Atualiza todos os arquivos JSON...\n
Classes (1):
- WikiJSONUpdater: ...\n  - __init__(self, wiki_dir): ...\n  - load_context_data(self): Carrega dados de contexto dete...\n  - scan_markdown_files(self): Escaneia todos os arquivos mar...\n  - extract_frontmatter(self, file_path): Extrai frontmatter de um arqui...\n  - generate_tags_index(self): Gera índice de tags...\n  - generate_wiki_map(self): Gera mapa da wiki...\n  - categorize_document(self, file_name, frontmatter): Categoriza documento baseado n...\n  - generate_relationships(self): Gera relacionamentos entre doc...\n  - update_all_json_files(self): Atualiza todos os arquivos JSO...\n
Imports (4):
.WikiindexerModule, json, re, datetime.datetime

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

