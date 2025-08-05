"""
migrated_update_modules_index



Módulo: migrated_update_modules_index
Caminho: wiki\update\modules\maps\modules_indexer\migrated_update_modules_index.py
Linhas de código: 348
Complexidade: 46.00

Funções (15):
- main(): Função principal...\n- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self, project_root): ...\n- scan_modules(self): Escaneia todos os módulos Lua...\n- analyze_module(self, module_path): Analisa um módulo Lua...\n- extract_description(self, content): Extrai descrição do módulo...\n- extract_lua_apis(self, file_path): Extrai APIs Lua do arquivo...\n- extract_dependencies(self, content): Extrai dependências do módulo...\n- categorize_module(self, module_name): Categoriza um módulo...\n- categorize_modules(self): Categoriza todos os módulos...\n- generate_statistics(self): Gera estatísticas dos módulos...\n- generate_search_index(self): Gera índice de busca...\n- generate_modules_index(self): Gera o índice completo dos módulos...\n- save_index(self, modules_index, output_file): Salva o índice em arquivo JSON...\n- update_index(self): Atualiza o índice dos módulos...\n
Classes (1):
- ModulesIndexer: ...\n  - __init__(self, project_root): ...\n  - scan_modules(self): Escaneia todos os módulos Lua...\n  - analyze_module(self, module_path): Analisa um módulo Lua...\n  - extract_description(self, content): Extrai descrição do módulo...\n  - extract_lua_apis(self, file_path): Extrai APIs Lua do arquivo...\n  - extract_dependencies(self, content): Extrai dependências do módulo...\n  - categorize_module(self, module_name): Categoriza um módulo...\n  - categorize_modules(self): Categoriza todos os módulos...\n  - generate_statistics(self): Gera estatísticas dos módulos...\n  - generate_search_index(self): Gera índice de busca...\n  - generate_modules_index(self): Gera o índice completo dos mód...\n  - save_index(self, modules_index, output_file): Salva o índice em arquivo JSON...\n  - update_index(self): Atualiza o índice dos módulos...\n
Imports (4):
.ModulesindexerModule, json, re, datetime.datetime

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

