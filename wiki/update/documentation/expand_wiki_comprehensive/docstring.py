"""
expand_wiki_comprehensive

Script para expansão abrangente da wiki do OTClient
Integra conteúdo do habdel e cria documentação completa

Módulo: expand_wiki_comprehensive
Caminho: wiki\update\expand_wiki_comprehensive.py
Linhas de código: 447
Complexidade: 24.00

Funções (13):
- main(): Função principal...\n- __init__(self, wiki_dir): ...\n- load_context_data(self): Carrega dados de contexto detectado...\n- extract_section_content(self, file_path, section_title): Extrai conteúdo de uma seção específica...\n- extract_examples(self, file_path): Extrai exemplos práticos do arquivo...\n- create_comprehensive_ui_guide(self): Cria guia completo de UI integrando conteúdo do ha...\n- create_lua_api_reference(self): Cria referência completa da API Lua...\n- create_system_guides(self): Cria guias completos para cada sistema...\n- process_habdel_content(self, content, original_file): Processa conteúdo do habdel para formato da wiki...\n- create_development_guides(self): Cria guias de desenvolvimento expandidos...\n- create_reference_documents(self): Cria documentos de referência...\n- update_wiki_index(self): Atualiza o índice principal da wiki...\n- expand_wiki_comprehensive(self): Expande a wiki de forma abrangente...\n
Classes (1):
- WikiExpander: ...\n  - __init__(self, wiki_dir): ...\n  - load_context_data(self): Carrega dados de contexto dete...\n  - extract_section_content(self, file_path, section_title): Extrai conteúdo de uma seção e...\n  - extract_examples(self, file_path): Extrai exemplos práticos do ar...\n  - create_comprehensive_ui_guide(self): Cria guia completo de UI integ...\n  - create_lua_api_reference(self): Cria referência completa da AP...\n  - create_system_guides(self): Cria guias completos para cada...\n  - process_habdel_content(self, content, original_file): Processa conteúdo do habdel pa...\n  - create_development_guides(self): Cria guias de desenvolvimento ...\n  - create_reference_documents(self): Cria documentos de referência...\n  - update_wiki_index(self): Atualiza o índice principal da...\n  - expand_wiki_comprehensive(self): Expande a wiki de forma abrang...\n
Imports (8):
os, json, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

Autor: Documentation Agent
Data: 2025-08-01 15:05:51
"""
