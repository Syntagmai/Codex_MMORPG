"""
optimize_wiki_structure

Script para otimização da estrutura da wiki
Remove duplicações e melhora organização sem perder informação

Módulo: optimize_wiki_structure
Caminho: wiki\update\optimize_wiki_structure.py
Linhas de código: 384
Complexidade: 36.00

Funções (13):
- main(): Função principal...\n- __init__(self, wiki_dir): ...\n- analyze_content_overlap(self, file1, file2): Analisa sobreposição de conteúdo entre dois arquiv...\n- extract_sections(self, content): Extrai seções do conteúdo...\n- merge_network_documents(self): Mescla documentos de rede em um só...\n- optimize_ui_documents(self): Otimiza documentos de UI...\n- extract_widget_sections(self, content): Extrai seções de widgets do conteúdo...\n- remove_repetitive_sections(self): Remove seções repetitivas desnecessárias...\n- get_section_content(self, lines, start_index): Obtém conteúdo de uma seção...\n- standardize_navigation(self): Padroniza seções de navegação...\n- generate_standard_navigation(self, filename): Gera navegação padronizada baseada no tipo de docu...\n- update_wiki_index(self): Atualiza o índice da wiki com a nova estrutura...\n- optimize_wiki_structure(self): Otimiza a estrutura completa da wiki...\n
Classes (1):
- WikiOptimizer: ...\n  - __init__(self, wiki_dir): ...\n  - analyze_content_overlap(self, file1, file2): Analisa sobreposição de conteú...\n  - extract_sections(self, content): Extrai seções do conteúdo...\n  - merge_network_documents(self): Mescla documentos de rede em u...\n  - optimize_ui_documents(self): Otimiza documentos de UI...\n  - extract_widget_sections(self, content): Extrai seções de widgets do co...\n  - remove_repetitive_sections(self): Remove seções repetitivas desn...\n  - get_section_content(self, lines, start_index): Obtém conteúdo de uma seção...\n  - standardize_navigation(self): Padroniza seções de navegação...\n  - generate_standard_navigation(self, filename): Gera navegação padronizada bas...\n  - update_wiki_index(self): Atualiza o índice da wiki com ...\n  - optimize_wiki_structure(self): Otimiza a estrutura completa d...\n
Imports (8):
os, json, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

Autor: Documentation Agent
Data: 2025-08-01 15:05:51
"""
