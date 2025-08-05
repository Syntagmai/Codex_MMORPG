"""
migrated_advanced_search_system



Módulo: migrated_advanced_search_system
Caminho: wiki\update\modules\analysis\advanced_searcher\migrated_advanced_search_system.py
Linhas de código: 699
Complexidade: 62.00

Funções (21):
- main(): Função principal do script....\n- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self, consolidated_dir): Inicializa o sistema de busca avançada.

Args:
   ...\n- load_intelligent_navigation(self): Carrega dados de navegação inteligente.

Returns:
...\n- extract_document_content(self, file_path): Extrai conteúdo completo de um documento.

Args:
 ...\n- build_content_index(self): Constrói índice de conteúdo para busca textual....\n- build_semantic_index(self): Constrói índice semântico baseado em similaridade ...\n- build_category_index(self): Constrói índice por categorias....\n- build_tag_index(self): Constrói índice por tags....\n- build_keyword_index(self): Constrói índice por palavras-chave....\n- build_metadata_index(self): Constrói índice por metadados....\n- build_similarity_matrix(self): Constrói matriz de similaridade entre documentos....\n- calculate_similarity(self, doc1, doc2): Calcula similaridade entre dois documentos.

Args:...\n- search_by_text(self, query, limit): Busca por texto nos documentos.

Args:
    query: ...\n- search_by_tags(self, tags, limit): Busca por tags.

Args:
    tags: Lista de tags par...\n- search_by_category(self, category, subcategory, limit): Busca por categoria.

Args:
    category: Categori...\n- search_similar(self, doc_path, limit): Busca documentos similares.

Args:
    doc_path: C...\n- extract_snippet(self, content, query, max_length): Extrai snippet do conteúdo com a query destacada.
...\n- save_search_index(self): Salva o índice de busca avançada....\n- generate_search_report(self): Gera relatório do sistema de busca.

Returns:
    ...\n- build_advanced_search(self): Constrói sistema completo de busca avançada.

Retu...\n
Classes (1):
- AdvancedSearchSystem: Sistema de busca avançada semântica...\n  - __init__(self, consolidated_dir): Inicializa o sistema de busca ...\n  - load_intelligent_navigation(self): Carrega dados de navegação int...\n  - extract_document_content(self, file_path): Extrai conteúdo completo de um...\n  - build_content_index(self): Constrói índice de conteúdo pa...\n  - build_semantic_index(self): Constrói índice semântico base...\n  - build_category_index(self): Constrói índice por categorias...\n  - build_tag_index(self): Constrói índice por tags....\n  - build_keyword_index(self): Constrói índice por palavras-c...\n  - build_metadata_index(self): Constrói índice por metadados....\n  - build_similarity_matrix(self): Constrói matriz de similaridad...\n  - calculate_similarity(self, doc1, doc2): Calcula similaridade entre doi...\n  - search_by_text(self, query, limit): Busca por texto nos documentos...\n  - search_by_tags(self, tags, limit): Busca por tags.

Args:
    tag...\n  - search_by_category(self, category, subcategory, limit): Busca por categoria.

Args:
  ...\n  - search_similar(self, doc_path, limit): Busca documentos similares.

A...\n  - extract_snippet(self, content, query, max_length): Extrai snippet do conteúdo com...\n  - save_search_index(self): Salva o índice de busca avança...\n  - generate_search_report(self): Gera relatório do sistema de b...\n  - build_advanced_search(self): Constrói sistema completo de b...\n
Imports (5):
.AdvancedsearcherModule, json, re, datetime.datetime, logging

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

