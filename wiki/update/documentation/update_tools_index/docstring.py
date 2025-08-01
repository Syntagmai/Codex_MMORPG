"""
update_tools_index

Script para indexação das ferramentas do OTClient
Atualiza: wiki/maps/tools_index.json

Módulo: update_tools_index
Caminho: wiki\update\update_tools_index.py
Linhas de código: 362
Complexidade: 49.00

Funções (17):
- main(): Função principal...\n- __init__(self, project_root): ...\n- scan_tools(self): Escaneia todas as ferramentas...\n- analyze_tool(self, tool_path): Analisa uma ferramenta...\n- categorize_tool(self, file_path): Categoriza uma ferramenta...\n- extract_tool_info(self, file_path): Extrai informações da ferramenta...\n- extract_description(self, content): Extrai descrição do conteúdo...\n- get_language(self, file_ext): Determina a linguagem do arquivo...\n- extract_functions(self, content, file_ext): Extrai funções do arquivo...\n- extract_dependencies(self, content): Extrai dependências do arquivo...\n- count_lines(self, file_path): Conta linhas de um arquivo...\n- categorize_tools(self): Categoriza todas as ferramentas...\n- generate_statistics(self): Gera estatísticas das ferramentas...\n- generate_search_index(self): Gera índice de busca...\n- generate_tools_index(self): Gera o índice completo das ferramentas...\n- save_index(self, tools_index, output_file): Salva o índice em arquivo JSON...\n- update_index(self): Atualiza o índice das ferramentas...\n
Classes (1):
- ToolsIndexer: ...\n  - __init__(self, project_root): ...\n  - scan_tools(self): Escaneia todas as ferramentas...\n  - analyze_tool(self, tool_path): Analisa uma ferramenta...\n  - categorize_tool(self, file_path): Categoriza uma ferramenta...\n  - extract_tool_info(self, file_path): Extrai informações da ferramen...\n  - extract_description(self, content): Extrai descrição do conteúdo...\n  - get_language(self, file_ext): Determina a linguagem do arqui...\n  - extract_functions(self, content, file_ext): Extrai funções do arquivo...\n  - extract_dependencies(self, content): Extrai dependências do arquivo...\n  - count_lines(self, file_path): Conta linhas de um arquivo...\n  - categorize_tools(self): Categoriza todas as ferramenta...\n  - generate_statistics(self): Gera estatísticas das ferramen...\n  - generate_search_index(self): Gera índice de busca...\n  - generate_tools_index(self): Gera o índice completo das fer...\n  - save_index(self, tools_index, output_file): Salva o índice em arquivo JSON...\n  - update_index(self): Atualiza o índice das ferramen...\n
Imports (8):
os, json, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

Autor: Documentation Agent
Data: 2025-08-01 15:05:52
"""
