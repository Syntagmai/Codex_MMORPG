"""
migrated_intelligent_organization_agent



Módulo: migrated_intelligent_organization_agent
Caminho: wiki\update\modules\agents\agent_orchestrator\migrated_intelligent_organization_agent.py
Linhas de código: 984
Complexidade: 101.00

Funções (32):
- main(): Função principal....\n- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self, base_path): ...\n- detect_organization_issues(self): Detecta problemas de organização automaticamente.
...\n- _detect_canary_integration_issues(self): Detecta problemas específicos relacionados à integ...\n- _detect_missing_integration_structure(self): Detecta estrutura de integração faltante.

Returns...\n- _is_canary_integration_file(self, file_path): Verifica se um arquivo é relacionado à integração ...\n- _is_in_correct_canary_location(self, file_path): Verifica se um arquivo de integração Canary está n...\n- organize_canary_integration_files(self): Organiza arquivos relacionados à integração Canary...\n- _create_canary_integration_structure(self): Cria estrutura de integração Canary se não existir...\n- _organize_canary_file(self, file_path): Organiza um arquivo específico de integração Canar...\n- validate_canary_integration_structure(self): Valida a estrutura de integração Canary.

Returns:...\n- is_in_wrong_location(self, file_path): Verifica se arquivo está no local errado....\n- is_obsolete(self, file_path): Verifica se arquivo é obsoleto....\n- is_temp_file(self, file_path): Verifica se arquivo é temporário....\n- has_category(self, file_path): Verifica se arquivo tem categoria definida....\n- find_duplicates(self, files): Encontra arquivos duplicados....\n- find_unorganized_reports(self): Encontra relatórios não organizados....\n- detect_file_context(self, file_path): Detecta contexto do arquivo automaticamente....\n- is_in_reports_folder(self, file_path): Verifica se arquivo está na pasta de relatórios....\n- is_in_tasks_folder(self, file_path): Verifica se arquivo está na pasta de tarefas....\n- is_in_recipes_folder(self, file_path): Verifica se arquivo está na pasta de receitas....\n- is_in_archives_folder(self, file_path): Verifica se arquivo está na pasta de arquivos....\n- organize_by_category(self): Organiza arquivos por categoria automaticamente.

...\n- organize_by_date(self): Organiza relatórios por data automaticamente.

Ret...\n- extract_date_from_file(self, file_path): Extrai data do arquivo ou usa data de modificação....\n- cleanup_temp_files(self): Remove arquivos temporários automaticamente.

Retu...\n- remove_duplicates(self): Remove arquivos duplicados.

Returns:
    Número d...\n- create_organization_structure(self): Cria estrutura de organização padrão.

Returns:
  ...\n- generate_organization_report(self, results): Gera relatório de organização.

Args:
    results:...\n- run_full_organization(self): Executa organização completa do sistema.

Returns:...\n- _is_ignored(self, file_path): Verifica se um arquivo deve ser ignorado pela orga...\n
Classes (1):
- IntelligentOrganizationAgent: Agente de organização inteligente para code cleanu...\n  - __init__(self, base_path): ...\n  - detect_organization_issues(self): Detecta problemas de organizaç...\n  - _detect_canary_integration_issues(self): Detecta problemas específicos ...\n  - _detect_missing_integration_structure(self): Detecta estrutura de integraçã...\n  - _is_canary_integration_file(self, file_path): Verifica se um arquivo é relac...\n  - _is_in_correct_canary_location(self, file_path): Verifica se um arquivo de inte...\n  - organize_canary_integration_files(self): Organiza arquivos relacionados...\n  - _create_canary_integration_structure(self): Cria estrutura de integração C...\n  - _organize_canary_file(self, file_path): Organiza um arquivo específico...\n  - validate_canary_integration_structure(self): Valida a estrutura de integraç...\n  - is_in_wrong_location(self, file_path): Verifica se arquivo está no lo...\n  - is_obsolete(self, file_path): Verifica se arquivo é obsoleto...\n  - is_temp_file(self, file_path): Verifica se arquivo é temporár...\n  - has_category(self, file_path): Verifica se arquivo tem catego...\n  - find_duplicates(self, files): Encontra arquivos duplicados....\n  - find_unorganized_reports(self): Encontra relatórios não organi...\n  - detect_file_context(self, file_path): Detecta contexto do arquivo au...\n  - is_in_reports_folder(self, file_path): Verifica se arquivo está na pa...\n  - is_in_tasks_folder(self, file_path): Verifica se arquivo está na pa...\n  - is_in_recipes_folder(self, file_path): Verifica se arquivo está na pa...\n  - is_in_archives_folder(self, file_path): Verifica se arquivo está na pa...\n  - organize_by_category(self): Organiza arquivos por categori...\n  - organize_by_date(self): Organiza relatórios por data a...\n  - extract_date_from_file(self, file_path): Extrai data do arquivo ou usa ...\n  - cleanup_temp_files(self): Remove arquivos temporários au...\n  - remove_duplicates(self): Remove arquivos duplicados.

R...\n  - create_organization_structure(self): Cria estrutura de organização ...\n  - generate_organization_report(self, results): Gera relatório de organização....\n  - run_full_organization(self): Executa organização completa d...\n  - _is_ignored(self, file_path): Verifica se um arquivo deve se...\n
Imports (7):
.AgentorchestratorModule, shutil, re, datetime.datetime, datetime.timedelta, logging, argparse

Autor: Documentation Agent
Data: 2025-08-01 15:05:59
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

