"""
update_source_index

Script para indexação automática do código-fonte do OTClient e Canary (submódulos)
Gera otclient_source_index.json com informações sobre arquivos C++ e Lua
Adaptado para estrutura com submódulos otclient/ e canary/

Módulo: update_source_index
Caminho: wiki\update\update_source_index.py
Linhas de código: 272
Complexidade: 53.00

Funções (10):
- main(): Função principal...\n- __init__(self): ...\n- scan_source_files(self): Escaneia arquivos de código-fonte nos submódulos...\n- categorize_file(self, file_path): Categoriza um arquivo baseado em seu caminho e con...\n- extract_functions(self, file_path): Extrai funções de um arquivo...\n- extract_classes(self, file_path): Extrai classes de um arquivo...\n- generate_source_index(self): Gera o índice completo do código-fonte...\n- generate_statistics(self): Gera estatísticas do código-fonte...\n- generate_search_index(self): Gera índice de busca...\n- save_index(self, source_index, output_file): Salva o índice em arquivo JSON...\n
Classes (1):
- SourceIndexer: ...\n  - __init__(self): ...\n  - scan_source_files(self): Escaneia arquivos de código-fo...\n  - categorize_file(self, file_path): Categoriza um arquivo baseado ...\n  - extract_functions(self, file_path): Extrai funções de um arquivo...\n  - extract_classes(self, file_path): Extrai classes de um arquivo...\n  - generate_source_index(self): Gera o índice completo do códi...\n  - generate_statistics(self): Gera estatísticas do código-fo...\n  - generate_search_index(self): Gera índice de busca...\n  - save_index(self, source_index, output_file): Salva o índice em arquivo JSON...\n
Imports (8):
os, json, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

Autor: Documentation Agent
Data: 2025-08-01 15:05:52
"""
