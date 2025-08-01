"""
knowledge_consolidation_system

Sistema de Consolidação Automática de Conhecimento
==================================================

Este script integra 53 documentos + 23 mapas JSON em wiki unificada
com navegação inteligente e estrutura hierárquica.

Autor: Sistema BMAD - Knowledge Manager
Data: 2025-08-01

Módulo: knowledge_consolidation_system
Caminho: wiki\update\knowledge_consolidation_system.py
Linhas de código: 384
Complexidade: 44.00

Funções (8):
- main(): Função principal do script....\n- __init__(self, wiki_dir): Inicializa o sistema de consolidação.

Args:
    w...\n- scan_documents(self): Escaneia todos os documentos disponíveis.

Returns...\n- categorize_documents(self, documents): Categoriza documentos por tipo de conteúdo.

Args:...\n- create_consolidation_structure(self, categorized_docs): Cria estrutura de consolidação organizada.

Args:
...\n- create_navigation_index(self): Cria índice de navegação para a wiki consolidada....\n- create_consolidation_report(self, documents, navigation_data): Cria relatório de consolidação.

Args:
    documen...\n- consolidate_knowledge(self): Executa consolidação completa do conhecimento.

Re...\n
Classes (1):
- KnowledgeConsolidationSystem: Sistema de consolidação automática de conhecimento...\n  - __init__(self, wiki_dir): Inicializa o sistema de consol...\n  - scan_documents(self): Escaneia todos os documentos d...\n  - categorize_documents(self, documents): Categoriza documentos por tipo...\n  - create_consolidation_structure(self, categorized_docs): Cria estrutura de consolidação...\n  - create_navigation_index(self): Cria índice de navegação para ...\n  - create_consolidation_report(self, documents, navigation_data): Cria relatório de consolidação...\n  - consolidate_knowledge(self): Executa consolidação completa ...\n
Imports (10):
json, os, shutil, pathlib.Path, typing.Dict, typing.List, typing.Any, typing.Optional, datetime.datetime, logging

Autor: Documentation Agent
Data: 2025-08-01 15:05:51
"""
