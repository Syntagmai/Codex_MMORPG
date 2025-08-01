"""
optimize_maps_for_tokens

Script para otimização de tokens nos mapas JSON
Converte descrições para inglês (IA) mantendo tags em português (usuário)

Módulo: optimize_maps_for_tokens
Caminho: wiki\update\optimize_maps_for_tokens.py
Linhas de código: 559
Complexidade: 12.00

Funções (8):
- main(): Função principal...\n- __init__(self, wiki_dir): ...\n- translate_text(self, text): Traduz texto para inglês para otimizar tokens...\n- optimize_metadata(self, metadata): Otimiza metadados convertendo para inglês...\n- optimize_tags_index(self, tags_data): Otimiza tags_index.json...\n- optimize_wiki_map(self, wiki_data): Otimiza wiki_map.json...\n- optimize_relationships(self, rel_data): Otimiza relationships.json...\n- optimize_all_maps(self): Otimiza todos os mapas JSON...\n
Classes (1):
- TokenOptimizer: ...\n  - __init__(self, wiki_dir): ...\n  - translate_text(self, text): Traduz texto para inglês para ...\n  - optimize_metadata(self, metadata): Otimiza metadados convertendo ...\n  - optimize_tags_index(self, tags_data): Otimiza tags_index.json...\n  - optimize_wiki_map(self, wiki_data): Otimiza wiki_map.json...\n  - optimize_relationships(self, rel_data): Otimiza relationships.json...\n  - optimize_all_maps(self): Otimiza todos os mapas JSON...\n
Imports (7):
json, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

Autor: Documentation Agent
Data: 2025-08-01 15:05:51
"""
