"""
intelligent_navigation_system

Sistema de Navegação Inteligente Otimizada
==========================================

Este script implementa navegação inteligente otimizada entre documentos consolidados
com busca semântica e links contextuais.

Autor: Sistema BMAD - Navigation Agent
Data: 2025-08-01

Módulo: intelligent_navigation_system
Caminho: wiki\update\intelligent_navigation_system.py
Linhas de código: 496
Complexidade: 55.00

Funções (14):
- main(): Função principal do script....\n- __init__(self, consolidated_dir): Inicializa o sistema de navegação inteligente.

Ar...\n- load_navigation_index(self): Carrega o índice de navegação existente.

Returns:...\n- analyze_document_content(self, file_path): Analisa o conteúdo de um documento para extrair in...\n- build_navigation_graph(self): Constrói grafo de navegação entre documentos....\n- create_semantic_links(self): Cria links semânticos entre documentos relacionado...\n- create_contextual_paths(self): Cria caminhos contextuais entre documentos....\n- create_quick_access(self): Cria sistema de acesso rápido....\n- create_search_index(self): Cria índice de busca para navegação rápida....\n- create_breadcrumbs(self): Cria sistema de breadcrumbs para navegação hierárq...\n- create_related_documents(self): Cria sistema de documentos relacionados....\n- generate_navigation_report(self): Gera relatório de navegação inteligente.

Returns:...\n- save_intelligent_navigation(self): Salva o sistema de navegação inteligente....\n- optimize_navigation(self): Executa otimização completa da navegação.

Returns...\n
Classes (1):
- IntelligentNavigationSystem: Sistema de navegação inteligente otimizada...\n  - __init__(self, consolidated_dir): Inicializa o sistema de navega...\n  - load_navigation_index(self): Carrega o índice de navegação ...\n  - analyze_document_content(self, file_path): Analisa o conteúdo de um docum...\n  - build_navigation_graph(self): Constrói grafo de navegação en...\n  - create_semantic_links(self): Cria links semânticos entre do...\n  - create_contextual_paths(self): Cria caminhos contextuais entr...\n  - create_quick_access(self): Cria sistema de acesso rápido....\n  - create_search_index(self): Cria índice de busca para nave...\n  - create_breadcrumbs(self): Cria sistema de breadcrumbs pa...\n  - create_related_documents(self): Cria sistema de documentos rel...\n  - generate_navigation_report(self): Gera relatório de navegação in...\n  - save_intelligent_navigation(self): Salva o sistema de navegação i...\n  - optimize_navigation(self): Executa otimização completa da...\n
Imports (11):
json, os, re, pathlib.Path, typing.Dict, typing.List, typing.Any, typing.Optional, typing.Tuple, datetime.datetime...

Autor: Documentation Agent
Data: 2025-08-01 15:05:51
"""

## 🔗 **Links Automáticos - Scripts**

> [!info] **Script de Automação**
> Este script faz parte do sistema de automação da wiki

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]

### **🔧 Links de Scripts**
- [[../update/README|Documentação de Scripts]]
- [[../maps/scripts_index|Índice de Scripts]]
- [[../templates/README|Templates de Scripts]]

### **📊 Scripts Relacionados**
- [[../update/automatic_linkage_system.py|automatic_linkage_system.py]]
- [[../update/create_automatic_link_templates.py|create_automatic_link_templates.py]]
- [[../update/orphan_files_analyzer.py|orphan_files_analyzer.py]]
- [[../update/update_json_maps.py|update_json_maps.py]]

### **📈 Métricas do Script**
- **Nome**: docstring
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

