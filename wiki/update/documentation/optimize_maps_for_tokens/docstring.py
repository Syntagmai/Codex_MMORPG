"""
optimize_maps_for_tokens

Script para otimização de tokens nos mapas JSON
Converte descrições para inglês (IA) mantendo tags em português (usuário)

Módulo: optimize_maps_for_tokens
Caminho: wiki\update\optimize_maps_for_tokens.py
Linhas de código: 559
Complexidade: 12.00

Funções (8):
- main(): Função principal...\n- __init__(self, wiki_dir): ...\n- translate_text(self, text): Traduz texto para inglês para otimizar tokens...\n- optimize_metadata(self, metadata): Otimiza metadados convertendo para inglês...\n- optimize_tags_index(self, tags_data): Otimiza tags_index.json...\n- optimize_wiki_map(self, wiki_data): Otimiza wiki_map.json...\n- optimize_relationships(self, rel_data): Otimiza relationships.json...\n- optimize_all_maps(self): Otimiza todos os mapas JSON...\n
Classes (1):
- TokenOptimizer: ...\n  - __init__(self, wiki_dir): ...\n  - translate_text(self, text): Traduz texto para inglês para ...\n  - optimize_metadata(self, metadata): Otimiza metadados convertendo ...\n  - optimize_tags_index(self, tags_data): Otimiza tags_index.json...\n  - optimize_wiki_map(self, wiki_data): Otimiza wiki_map.json...\n  - optimize_relationships(self, rel_data): Otimiza relationships.json...\n  - optimize_all_maps(self): Otimiza todos os mapas JSON...\n
Imports (7):
json, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

Autor: Documentation Agent
Data: 2025-08-01 15:05:51
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

