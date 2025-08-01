"""
update_json_maps

Script para atualização automática dos mapas JSON da wiki do OTClient
Atualiza: maps/tags_index.json, maps/wiki_map.json, maps/relationships.json

Módulo: update_json_maps
Caminho: wiki\update\update_json_maps.py
Linhas de código: 482
Complexidade: 82.00

Funções (17):
- main(): Função principal...\n- __init__(self, wiki_dir): ...\n- scan_markdown_files(self): Escaneia todos os arquivos markdown na pasta wiki...\n- extract_frontmatter(self, file_path): Extrai frontmatter de um arquivo markdown...\n- generate_tags_index(self): Gera o índice de tags...\n- generate_search_aliases(self, files_by_tag): Gera aliases de busca para tags...\n- generate_wiki_map(self): Gera o mapa completo da wiki...\n- categorize_document(self, file, frontmatter): Categoriza um documento baseado em seu conteúdo...\n- get_priority(self, file, frontmatter): Determina a prioridade de um documento...\n- get_description(self, file, frontmatter): Extrai descrição do documento...\n- generate_statistics(self, categories): Gera estatísticas da wiki...\n- generate_navigation_paths(self, categories): Gera caminhos de navegação...\n- generate_relationships(self): Gera relacionamentos entre documentos...\n- generate_learning_paths(self): Gera caminhos de aprendizado...\n- generate_dependency_graph(self, relationships): Gera grafo de dependências...\n- generate_topic_clusters(self): Gera clusters de tópicos...\n- update_all_json_files(self): Atualiza todos os arquivos JSON...\n
Classes (1):
- WikiJSONUpdater: ...\n  - __init__(self, wiki_dir): ...\n  - scan_markdown_files(self): Escaneia todos os arquivos mar...\n  - extract_frontmatter(self, file_path): Extrai frontmatter de um arqui...\n  - generate_tags_index(self): Gera o índice de tags...\n  - generate_search_aliases(self, files_by_tag): Gera aliases de busca para tag...\n  - generate_wiki_map(self): Gera o mapa completo da wiki...\n  - categorize_document(self, file, frontmatter): Categoriza um documento basead...\n  - get_priority(self, file, frontmatter): Determina a prioridade de um d...\n  - get_description(self, file, frontmatter): Extrai descrição do documento...\n  - generate_statistics(self, categories): Gera estatísticas da wiki...\n  - generate_navigation_paths(self, categories): Gera caminhos de navegação...\n  - generate_relationships(self): Gera relacionamentos entre doc...\n  - generate_learning_paths(self): Gera caminhos de aprendizado...\n  - generate_dependency_graph(self, relationships): Gera grafo de dependências...\n  - generate_topic_clusters(self): Gera clusters de tópicos...\n  - update_all_json_files(self): Atualiza todos os arquivos JSO...\n
Imports (8):
os, json, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

Autor: Documentation Agent
Data: 2025-08-01 15:05:52
"""
