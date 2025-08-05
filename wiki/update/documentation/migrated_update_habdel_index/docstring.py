"""
migrated_update_habdel_index



Módulo: migrated_update_habdel_index
Caminho: wiki\update\modules\maps\habdel_indexer\migrated_update_habdel_index.py
Linhas de código: 358
Complexidade: 64.00

Funções (15):
- main(): Função principal...\n- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self, project_root): ...\n- scan_habdel_files(self): Escaneia todos os arquivos da pasta habdel...\n- extract_story_info(self, file_path): Extrai informações de story de um arquivo...\n- extract_title(self, content, file_stem): Extrai título do conteúdo...\n- extract_description(self, content): Extrai descrição do conteúdo...\n- determine_status(self, content, file_name): Determina status baseado no conteúdo...\n- extract_tags(self, content): Extrai tags do conteúdo...\n- categorize_stories(self): Categoriza as stories...\n- generate_statistics(self): Gera estatísticas da pasta habdel...\n- generate_search_index(self): Gera índice de busca...\n- generate_habdel_index(self): Gera o índice completo da pasta habdel...\n- save_index(self, habdel_index, output_file): Salva o índice em arquivo JSON...\n- update_index(self): Atualiza o índice da pasta habdel...\n
Classes (1):
- HabdelIndexer: ...\n  - __init__(self, project_root): ...\n  - scan_habdel_files(self): Escaneia todos os arquivos da ...\n  - extract_story_info(self, file_path): Extrai informações de story de...\n  - extract_title(self, content, file_stem): Extrai título do conteúdo...\n  - extract_description(self, content): Extrai descrição do conteúdo...\n  - determine_status(self, content, file_name): Determina status baseado no co...\n  - extract_tags(self, content): Extrai tags do conteúdo...\n  - categorize_stories(self): Categoriza as stories...\n  - generate_statistics(self): Gera estatísticas da pasta hab...\n  - generate_search_index(self): Gera índice de busca...\n  - generate_habdel_index(self): Gera o índice completo da past...\n  - save_index(self, habdel_index, output_file): Salva o índice em arquivo JSON...\n  - update_index(self): Atualiza o índice da pasta hab...\n
Imports (4):
.HabdelindexerModule, json, re, datetime.datetime

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

