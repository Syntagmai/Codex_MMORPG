"""
migrated_update_tools_index



Módulo: migrated_update_tools_index
Caminho: wiki\update\modules\maps\tools_indexer\migrated_update_tools_index.py
Linhas de código: 392
Complexidade: 51.00

Funções (18):
- main(): Função principal...\n- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self, project_root): ...\n- scan_tools(self): Escaneia todas as ferramentas...\n- analyze_tool(self, tool_path): Analisa uma ferramenta...\n- categorize_tool(self, file_path): Categoriza uma ferramenta...\n- extract_tool_info(self, file_path): Extrai informações da ferramenta...\n- extract_description(self, content): Extrai descrição do conteúdo...\n- get_language(self, file_ext): Determina a linguagem do arquivo...\n- extract_functions(self, content, file_ext): Extrai funções do arquivo...\n- extract_dependencies(self, content): Extrai dependências do arquivo...\n- count_lines(self, file_path): Conta linhas de um arquivo...\n- categorize_tools(self): Categoriza todas as ferramentas...\n- generate_statistics(self): Gera estatísticas das ferramentas...\n- generate_search_index(self): Gera índice de busca...\n- generate_tools_index(self): Gera o índice completo das ferramentas...\n- save_index(self, tools_index, output_file): Salva o índice em arquivo JSON...\n- update_index(self): Atualiza o índice das ferramentas...\n
Classes (1):
- ToolsIndexer: ...\n  - __init__(self, project_root): ...\n  - scan_tools(self): Escaneia todas as ferramentas...\n  - analyze_tool(self, tool_path): Analisa uma ferramenta...\n  - categorize_tool(self, file_path): Categoriza uma ferramenta...\n  - extract_tool_info(self, file_path): Extrai informações da ferramen...\n  - extract_description(self, content): Extrai descrição do conteúdo...\n  - get_language(self, file_ext): Determina a linguagem do arqui...\n  - extract_functions(self, content, file_ext): Extrai funções do arquivo...\n  - extract_dependencies(self, content): Extrai dependências do arquivo...\n  - count_lines(self, file_path): Conta linhas de um arquivo...\n  - categorize_tools(self): Categoriza todas as ferramenta...\n  - generate_statistics(self): Gera estatísticas das ferramen...\n  - generate_search_index(self): Gera índice de busca...\n  - generate_tools_index(self): Gera o índice completo das fer...\n  - save_index(self, tools_index, output_file): Salva o índice em arquivo JSON...\n  - update_index(self): Atualiza o índice das ferramen...\n
Imports (4):
.ToolsindexerModule, json, re, datetime.datetime

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

