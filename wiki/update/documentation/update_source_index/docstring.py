"""
update_source_index

Script para indexação automática do código-fonte do OTClient e Canary (submódulos)
Gera otclient_source_index.json com informações sobre arquivos C++ e Lua
Adaptado para estrutura com submódulos otclient/ e canary/

Módulo: update_source_index
Caminho: wiki\update\update_source_index.py
Linhas de código: 272
Complexidade: 53.00

Funções (10):
- main(): Função principal...\n- __init__(self): ...\n- scan_source_files(self): Escaneia arquivos de código-fonte nos submódulos...\n- categorize_file(self, file_path): Categoriza um arquivo baseado em seu caminho e con...\n- extract_functions(self, file_path): Extrai funções de um arquivo...\n- extract_classes(self, file_path): Extrai classes de um arquivo...\n- generate_source_index(self): Gera o índice completo do código-fonte...\n- generate_statistics(self): Gera estatísticas do código-fonte...\n- generate_search_index(self): Gera índice de busca...\n- save_index(self, source_index, output_file): Salva o índice em arquivo JSON...\n
Classes (1):
- SourceIndexer: ...\n  - __init__(self): ...\n  - scan_source_files(self): Escaneia arquivos de código-fo...\n  - categorize_file(self, file_path): Categoriza um arquivo baseado ...\n  - extract_functions(self, file_path): Extrai funções de um arquivo...\n  - extract_classes(self, file_path): Extrai classes de um arquivo...\n  - generate_source_index(self): Gera o índice completo do códi...\n  - generate_statistics(self): Gera estatísticas do código-fo...\n  - generate_search_index(self): Gera índice de busca...\n  - save_index(self, source_index, output_file): Salva o índice em arquivo JSON...\n
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

