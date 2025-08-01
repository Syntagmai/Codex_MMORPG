"""
update_styles_index

Script para indexação dos estilos OTUI do OTClient
Atualiza: wiki/maps/styles_index.json

Módulo: update_styles_index
Caminho: wiki\update\update_styles_index.py
Linhas de código: 323
Complexidade: 44.00

Funções (16):
- main(): Função principal...\n- __init__(self, project_root): ...\n- scan_style_files(self): Escaneia todos os arquivos de estilo OTUI...\n- analyze_style_file(self, file_path): Analisa um arquivo de estilo OTUI...\n- extract_widgets(self, content): Extrai widgets do arquivo de estilo...\n- extract_widget_properties(self, widget_content): Extrai propriedades de um widget...\n- guess_property_type(self, value): Tenta adivinhar o tipo da propriedade...\n- extract_properties(self, content): Extrai todas as propriedades do arquivo...\n- extract_dependencies(self, content): Extrai dependências do arquivo de estilo...\n- categorize_style(self, file_name, content): Categoriza um arquivo de estilo...\n- categorize_styles(self): Categoriza todos os estilos...\n- generate_statistics(self): Gera estatísticas dos estilos...\n- generate_search_index(self): Gera índice de busca...\n- generate_styles_index(self): Gera o índice completo dos estilos...\n- save_index(self, styles_index, output_file): Salva o índice em arquivo JSON...\n- update_index(self): Atualiza o índice dos estilos...\n
Classes (1):
- StylesIndexer: ...\n  - __init__(self, project_root): ...\n  - scan_style_files(self): Escaneia todos os arquivos de ...\n  - analyze_style_file(self, file_path): Analisa um arquivo de estilo O...\n  - extract_widgets(self, content): Extrai widgets do arquivo de e...\n  - extract_widget_properties(self, widget_content): Extrai propriedades de um widg...\n  - guess_property_type(self, value): Tenta adivinhar o tipo da prop...\n  - extract_properties(self, content): Extrai todas as propriedades d...\n  - extract_dependencies(self, content): Extrai dependências do arquivo...\n  - categorize_style(self, file_name, content): Categoriza um arquivo de estil...\n  - categorize_styles(self): Categoriza todos os estilos...\n  - generate_statistics(self): Gera estatísticas dos estilos...\n  - generate_search_index(self): Gera índice de busca...\n  - generate_styles_index(self): Gera o índice completo dos est...\n  - save_index(self, styles_index, output_file): Salva o índice em arquivo JSON...\n  - update_index(self): Atualiza o índice dos estilos...\n
Imports (8):
os, json, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

Autor: Documentation Agent
Data: 2025-08-01 15:05:52
"""
