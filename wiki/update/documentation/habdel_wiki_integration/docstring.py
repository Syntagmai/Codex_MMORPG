"""
habdel_wiki_integration

Habdel Wiki Integration Script

Este script integra a documentação habdel com a wiki principal do OTClient,
criando links, índices e navegação unificada.

Módulo: habdel_wiki_integration
Caminho: wiki\update\habdel_wiki_integration.py
Linhas de código: 499
Complexidade: 61.00

Funções (15):
- __init__(self): ...\n- analyze_habdel_structure(self): Analisa a estrutura da documentação habdel...\n- determine_category(self, filename): Determina a categoria do arquivo baseado no nome...\n- extract_story_info(self, file_path): Extrai informações da story do arquivo...\n- extract_title(self, content): Extrai título do conteúdo...\n- extract_status(self, content): Extrai status do conteúdo...\n- analyze_wiki_structure(self): Analisa a estrutura da wiki principal...\n- determine_wiki_category(self, filename): Determina a categoria do arquivo da wiki...\n- create_integration_index(self, habdel_structure, wiki_structure): Cria índice de integração entre habdel e wiki...\n- get_category_emoji(self, category): Retorna emoji para categoria...\n- get_category_name(self, category): Retorna nome completo da categoria...\n- get_status_emoji(self, status): Retorna emoji para status...\n- create_navigation_links(self, habdel_structure): Cria links de navegação para arquivos habdel...\n- save_integration_files(self, habdel_structure, wiki_structure): Salva arquivos de integração...\n- run(self): Executa a integração habdel-wiki...\n
Classes (1):
- HabdelWikiIntegration: ...\n  - __init__(self): ...\n  - analyze_habdel_structure(self): Analisa a estrutura da documen...\n  - determine_category(self, filename): Determina a categoria do arqui...\n  - extract_story_info(self, file_path): Extrai informações da story do...\n  - extract_title(self, content): Extrai título do conteúdo...\n  - extract_status(self, content): Extrai status do conteúdo...\n  - analyze_wiki_structure(self): Analisa a estrutura da wiki pr...\n  - determine_wiki_category(self, filename): Determina a categoria do arqui...\n  - create_integration_index(self, habdel_structure, wiki_structure): Cria índice de integração entr...\n  - get_category_emoji(self, category): Retorna emoji para categoria...\n  - get_category_name(self, category): Retorna nome completo da categ...\n  - get_status_emoji(self, status): Retorna emoji para status...\n  - create_navigation_links(self, habdel_structure): Cria links de navegação para a...\n  - save_integration_files(self, habdel_structure, wiki_structure): Salva arquivos de integração...\n  - run(self): Executa a integração habdel-wi...\n
Imports (9):
json, logging, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Optional, typing.Tuple

Autor: Documentation Agent
Data: 2025-08-01 15:05:51
"""
