"""
navigation_index_generator

Navigation Index Generator

Este script gera índices de navegação para facilitar a busca e navegação
na documentação integrada habdel-wiki.

Módulo: navigation_index_generator
Caminho: wiki\update\navigation_index_generator.py
Linhas de código: 657
Complexidade: 62.00

Funções (15):
- __init__(self): ...\n- scan_all_documents(self): Escaneia todos os documentos para criar índice com...\n- extract_document_info(self, file_path, source): Extrai informações do documento...\n- extract_frontmatter(self, content): Extrai frontmatter do conteúdo...\n- extract_title(self, content): Extrai título do conteúdo...\n- extract_story_id(self, content, filename): Extrai ID da story...\n- categorize_document(self, doc_info): Categoriza o documento...\n- categorize_size(self, size): Categoriza o tamanho do documento...\n- extract_keywords(self, content): Extrai palavras-chave do conteúdo...\n- create_alphabetical_index(self, documents): Cria índice alfabético...\n- create_categorical_index(self, documents): Cria índice por categorias...\n- create_story_based_index(self, documents): Cria índice baseado em stories...\n- create_search_index(self, documents): Cria índice de busca...\n- save_indexes(self, documents): Salva todos os índices...\n- run(self): Executa a geração de índices...\n
Classes (1):
- NavigationIndexGenerator: ...\n  - __init__(self): ...\n  - scan_all_documents(self): Escaneia todos os documentos p...\n  - extract_document_info(self, file_path, source): Extrai informações do document...\n  - extract_frontmatter(self, content): Extrai frontmatter do conteúdo...\n  - extract_title(self, content): Extrai título do conteúdo...\n  - extract_story_id(self, content, filename): Extrai ID da story...\n  - categorize_document(self, doc_info): Categoriza o documento...\n  - categorize_size(self, size): Categoriza o tamanho do docume...\n  - extract_keywords(self, content): Extrai palavras-chave do conte...\n  - create_alphabetical_index(self, documents): Cria índice alfabético...\n  - create_categorical_index(self, documents): Cria índice por categorias...\n  - create_story_based_index(self, documents): Cria índice baseado em stories...\n  - create_search_index(self, documents): Cria índice de busca...\n  - save_indexes(self, documents): Salva todos os índices...\n  - run(self): Executa a geração de índices...\n
Imports (9):
json, logging, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Optional, typing.Tuple

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

