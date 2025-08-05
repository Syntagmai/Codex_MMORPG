"""
update_resources_index

Script para indexação dos recursos do OTClient
Atualiza: wiki/maps/resources_index.json

Módulo: update_resources_index
Caminho: wiki\update\update_resources_index.py
Linhas de código: 337
Complexidade: 41.00

Funções (16):
- main(): Função principal...\n- __init__(self, project_root): ...\n- scan_resources(self): Escaneia todos os recursos...\n- analyze_resource(self, resource_path): Analisa um recurso...\n- categorize_resource(self, file_path): Categoriza um recurso...\n- extract_metadata(self, file_path): Extrai metadados do arquivo...\n- extract_font_metadata(self, file_path): Extrai metadados de fonte...\n- extract_locale_metadata(self, file_path): Extrai metadados de localização...\n- extract_particle_metadata(self, file_path): Extrai metadados de partículas...\n- count_lines(self, file_path): Conta linhas de um arquivo...\n- categorize_resources(self): Categoriza todos os recursos...\n- generate_statistics(self): Gera estatísticas dos recursos...\n- generate_search_index(self): Gera índice de busca...\n- generate_resources_index(self): Gera o índice completo dos recursos...\n- save_index(self, resources_index, output_file): Salva o índice em arquivo JSON...\n- update_index(self): Atualiza o índice dos recursos...\n
Classes (1):
- ResourcesIndexer: ...\n  - __init__(self, project_root): ...\n  - scan_resources(self): Escaneia todos os recursos...\n  - analyze_resource(self, resource_path): Analisa um recurso...\n  - categorize_resource(self, file_path): Categoriza um recurso...\n  - extract_metadata(self, file_path): Extrai metadados do arquivo...\n  - extract_font_metadata(self, file_path): Extrai metadados de fonte...\n  - extract_locale_metadata(self, file_path): Extrai metadados de localizaçã...\n  - extract_particle_metadata(self, file_path): Extrai metadados de partículas...\n  - count_lines(self, file_path): Conta linhas de um arquivo...\n  - categorize_resources(self): Categoriza todos os recursos...\n  - generate_statistics(self): Gera estatísticas dos recursos...\n  - generate_search_index(self): Gera índice de busca...\n  - generate_resources_index(self): Gera o índice completo dos rec...\n  - save_index(self, resources_index, output_file): Salva o índice em arquivo JSON...\n  - update_index(self): Atualiza o índice dos recursos...\n
Imports (8):
os, json, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

Autor: Documentation Agent
Data: 2025-08-01 15:05:52
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

