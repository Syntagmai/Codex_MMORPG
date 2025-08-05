"""
migrated_expand_wiki_comprehensive



Módulo: migrated_expand_wiki_comprehensive
Caminho: wiki\update\modules\documentation\wiki_expander\migrated_expand_wiki_comprehensive.py
Linhas de código: 478
Complexidade: 26.00

Funções (14):
- main(): Função principal...\n- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self, wiki_dir): ...\n- load_context_data(self): Carrega dados de contexto detectado...\n- extract_section_content(self, file_path, section_title): Extrai conteúdo de uma seção específica...\n- extract_examples(self, file_path): Extrai exemplos práticos do arquivo...\n- create_comprehensive_ui_guide(self): Cria guia completo de UI integrando conteúdo do ha...\n- create_lua_api_reference(self): Cria referência completa da API Lua...\n- create_system_guides(self): Cria guias completos para cada sistema...\n- process_habdel_content(self, content, original_file): Processa conteúdo do habdel para formato da wiki...\n- create_development_guides(self): Cria guias de desenvolvimento expandidos...\n- create_reference_documents(self): Cria documentos de referência...\n- update_wiki_index(self): Atualiza o índice principal da wiki...\n- expand_wiki_comprehensive(self): Expande a wiki de forma abrangente...\n
Classes (1):
- WikiExpander: ...\n  - __init__(self, wiki_dir): ...\n  - load_context_data(self): Carrega dados de contexto dete...\n  - extract_section_content(self, file_path, section_title): Extrai conteúdo de uma seção e...\n  - extract_examples(self, file_path): Extrai exemplos práticos do ar...\n  - create_comprehensive_ui_guide(self): Cria guia completo de UI integ...\n  - create_lua_api_reference(self): Cria referência completa da AP...\n  - create_system_guides(self): Cria guias completos para cada...\n  - process_habdel_content(self, content, original_file): Processa conteúdo do habdel pa...\n  - create_development_guides(self): Cria guias de desenvolvimento ...\n  - create_reference_documents(self): Cria documentos de referência...\n  - update_wiki_index(self): Atualiza o índice principal da...\n  - expand_wiki_comprehensive(self): Expande a wiki de forma abrang...\n
Imports (3):
.WikiexpanderModule, json, re

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

