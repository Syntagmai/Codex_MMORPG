"""
fix_wiki_issues

Script para correção completa da wiki - Deixar 10/10
Corrige links quebrados, melhora navegação e otimiza para IA e usuários brasileiros

Módulo: fix_wiki_issues
Caminho: wiki\update\fix_wiki_issues.py
Linhas de código: 449
Complexidade: 20.00

Funções (8):
- __init__(self, wiki_dir): ...\n- fix_broken_links(self): Corrige links quebrados em todos os documentos...\n- improve_wiki_index(self): Melhora o índice principal da wiki...\n- improve_document_aliases(self): Melhora aliases dos documentos para melhor busca...\n- improve_navigation_sections(self): Melhora seções de navegação em todos os documentos...\n- optimize_maps_for_ai(self): Otimiza mapas JSON para melhor consulta da IA...\n- create_quick_search_guide(self): Cria guia de busca rápida para brasileiros...\n- fix_all_issues(self): Executa todas as correções...\n
Classes (1):
- WikiFixer: ...\n  - __init__(self, wiki_dir): ...\n  - fix_broken_links(self): Corrige links quebrados em tod...\n  - improve_wiki_index(self): Melhora o índice principal da ...\n  - improve_document_aliases(self): Melhora aliases dos documentos...\n  - improve_navigation_sections(self): Melhora seções de navegação em...\n  - optimize_maps_for_ai(self): Otimiza mapas JSON para melhor...\n  - create_quick_search_guide(self): Cria guia de busca rápida para...\n  - fix_all_issues(self): Executa todas as correções...\n
Imports (8):
os, json, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any

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

