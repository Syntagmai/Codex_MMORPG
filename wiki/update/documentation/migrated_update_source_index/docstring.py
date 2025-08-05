"""
migrated_update_source_index



Módulo: migrated_update_source_index
Caminho: wiki\update\modules\maps\source_indexer\migrated_update_source_index.py
Linhas de código: 301
Complexidade: 55.00

Funções (11):
- main(): Função principal...\n- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self): ...\n- scan_source_files(self): Escaneia arquivos de código-fonte nos submódulos...\n- categorize_file(self, file_path): Categoriza um arquivo baseado em seu caminho e con...\n- extract_functions(self, file_path): Extrai funções de um arquivo...\n- extract_classes(self, file_path): Extrai classes de um arquivo...\n- generate_source_index(self): Gera o índice completo do código-fonte...\n- generate_statistics(self): Gera estatísticas do código-fonte...\n- generate_search_index(self): Gera índice de busca...\n- save_index(self, source_index, output_file): Salva o índice em arquivo JSON...\n
Classes (1):
- SourceIndexer: ...\n  - __init__(self): ...\n  - scan_source_files(self): Escaneia arquivos de código-fo...\n  - categorize_file(self, file_path): Categoriza um arquivo baseado ...\n  - extract_functions(self, file_path): Extrai funções de um arquivo...\n  - extract_classes(self, file_path): Extrai classes de um arquivo...\n  - generate_source_index(self): Gera o índice completo do códi...\n  - generate_statistics(self): Gera estatísticas do código-fo...\n  - generate_search_index(self): Gera índice de busca...\n  - save_index(self, source_index, output_file): Salva o índice em arquivo JSON...\n
Imports (4):
.SourceindexerModule, json, re, datetime.datetime

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

