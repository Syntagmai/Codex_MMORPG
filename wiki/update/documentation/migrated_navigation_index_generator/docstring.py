"""
migrated_navigation_index_generator



Módulo: migrated_navigation_index_generator
Caminho: wiki\update\modules\analysis\research_manager\migrated_navigation_index_generator.py
Linhas de código: 692
Complexidade: 64.00

Funções (16):
- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self): ...\n- scan_all_documents(self): Escaneia todos os documentos para criar índice com...\n- extract_document_info(self, file_path, source): Extrai informações do documento...\n- extract_frontmatter(self, content): Extrai frontmatter do conteúdo...\n- extract_title(self, content): Extrai título do conteúdo...\n- extract_story_id(self, content, filename): Extrai ID da story...\n- categorize_document(self, doc_info): Categoriza o documento...\n- categorize_size(self, size): Categoriza o tamanho do documento...\n- extract_keywords(self, content): Extrai palavras-chave do conteúdo...\n- create_alphabetical_index(self, documents): Cria índice alfabético...\n- create_categorical_index(self, documents): Cria índice por categorias...\n- create_story_based_index(self, documents): Cria índice baseado em stories...\n- create_search_index(self, documents): Cria índice de busca...\n- save_indexes(self, documents): Salva todos os índices...\n- run(self): Executa a geração de índices...\n
Classes (1):
- NavigationIndexGenerator: ...\n  - __init__(self): ...\n  - scan_all_documents(self): Escaneia todos os documentos p...\n  - extract_document_info(self, file_path, source): Extrai informações do document...\n  - extract_frontmatter(self, content): Extrai frontmatter do conteúdo...\n  - extract_title(self, content): Extrai título do conteúdo...\n  - extract_story_id(self, content, filename): Extrai ID da story...\n  - categorize_document(self, doc_info): Categoriza o documento...\n  - categorize_size(self, size): Categoriza o tamanho do docume...\n  - extract_keywords(self, content): Extrai palavras-chave do conte...\n  - create_alphabetical_index(self, documents): Cria índice alfabético...\n  - create_categorical_index(self, documents): Cria índice por categorias...\n  - create_story_based_index(self, documents): Cria índice baseado em stories...\n  - create_search_index(self, documents): Cria índice de busca...\n  - save_indexes(self, documents): Salva todos os índices...\n  - run(self): Executa a geração de índices...\n
Imports (4):
.ResearchmanagerModule, logging, re, datetime.datetime

Autor: Documentation Agent
Data: 2025-08-01 15:05:58
"""
