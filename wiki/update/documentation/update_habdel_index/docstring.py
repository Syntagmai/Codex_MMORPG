"""
update_habdel_index

Script para indexação da pasta habdel - Documentação Original e Planejamento
Atualiza: wiki/maps/habdel_index.json

Módulo: update_habdel_index
Caminho: wiki\update\update_habdel_index.py
Linhas de código: 328
Complexidade: 62.00

Funções (14):
- main(): Função principal...\n- __init__(self, project_root): ...\n- scan_habdel_files(self): Escaneia todos os arquivos da pasta habdel...\n- extract_story_info(self, file_path): Extrai informações de story de um arquivo...\n- extract_title(self, content, file_stem): Extrai título do conteúdo...\n- extract_description(self, content): Extrai descrição do conteúdo...\n- determine_status(self, content, file_name): Determina status baseado no conteúdo...\n- extract_tags(self, content): Extrai tags do conteúdo...\n- categorize_stories(self): Categoriza as stories...\n- generate_statistics(self): Gera estatísticas da pasta habdel...\n- generate_search_index(self): Gera índice de busca...\n- generate_habdel_index(self): Gera o índice completo da pasta habdel...\n- save_index(self, habdel_index, output_file): Salva o índice em arquivo JSON...\n- update_index(self): Atualiza o índice da pasta habdel...\n
Classes (1):
- HabdelIndexer: ...\n  - __init__(self, project_root): ...\n  - scan_habdel_files(self): Escaneia todos os arquivos da ...\n  - extract_story_info(self, file_path): Extrai informações de story de...\n  - extract_title(self, content, file_stem): Extrai título do conteúdo...\n  - extract_description(self, content): Extrai descrição do conteúdo...\n  - determine_status(self, content, file_name): Determina status baseado no co...\n  - extract_tags(self, content): Extrai tags do conteúdo...\n  - categorize_stories(self): Categoriza as stories...\n  - generate_statistics(self): Gera estatísticas da pasta hab...\n  - generate_search_index(self): Gera índice de busca...\n  - generate_habdel_index(self): Gera o índice completo da past...\n  - save_index(self, habdel_index, output_file): Salva o índice em arquivo JSON...\n  - update_index(self): Atualiza o índice da pasta hab...\n
Imports (8):
os, json, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

Autor: Documentation Agent
Data: 2025-08-01 15:05:52
"""
