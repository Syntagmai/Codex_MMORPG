"""
migrated_git_automation_agent



Módulo: migrated_git_automation_agent
Caminho: wiki\update\modules\agents\agent_orchestrator\migrated_git_automation_agent.py
Linhas de código: 1200
Complexidade: 156.00

Funções (27):
- main(): Função principal do agente....\n- integrate_with_module(): Integra o script com o módulo de destino....\n- __init__(self, project_root): Inicializa o agente de automação Git.

Args:
    p...\n- validate_file_exists(self, file_path): Valida se um arquivo existe antes de tentar adicio...\n- safe_add_file(self, file_path): Adiciona um arquivo de forma segura, validando sua...\n- analyze_changes(self): Analisa mudanças no repositório Git.

Returns:
   ...\n- _detect_task_context(self): Detecta contexto de tarefa atual.

Returns:
    In...\n- _detect_open_files(self): Detecta arquivos abertos no IDE.

Returns:
    Lis...\n- _analyze_commit_groups(self, changes): Analisa e agrupa mudanças para commits separados.
...\n- _group_by_directory(self, files): Agrupa arquivos por diretório.

Args:
    files: L...\n- _group_by_file_type(self, files): Agrupa arquivos por tipo.

Args:
    files: Lista ...\n- _group_by_context(self, files): Agrupa arquivos por contexto (análise de diff).

A...\n- _get_file_diff(self, file_path): Obtém diff de um arquivo.

Args:
    file_path: Ca...\n- _extract_context_from_diff(self, diff_content): Extrai contexto de um diff.

Args:
    diff_conten...\n- _is_similar_context(self, context1, context2): Verifica se dois contextos são similares.

Args:
 ...\n- _consolidate_groups(self, groups): Consolida grupos sobrepostos.

Args:
    groups: L...\n- _ensure_unique_files(self, groups, all_files): Garante que cada arquivo está em apenas um grupo.
...\n- _get_file_type(self, file_path): Determina o tipo de um arquivo.

Args:
    file_pa...\n- _determine_type_from_files(self, files): Determina o tipo de commit baseado em uma lista de...\n- _generate_group_message(self, files, commit_type): Gera mensagem para um grupo de arquivos.

Args:
  ...\n- _determine_commit_type(self, changes): Determina o tipo de commit baseado nas mudanças.

...\n- _generate_change_summary(self, changes): Gera resumo das mudanças em português.

Args:
    ...\n- generate_commit_message(self, changes): Gera mensagem de commit inteligente em português.
...\n- validate_commit_message(self, message): Valida mensagem de commit seguindo boas práticas.
...\n- execute_commit(self, message, auto_push): Executa commit com validação.

Args:
    message: ...\n- auto_commit(self, auto_push): Executa commit automático completo.

Args:
    aut...\n- execute_multiple_commits(self, commit_groups, auto_push): Executa múltiplos commits baseado nos grupos.

Arg...\n
Classes (1):
- GitAutomationAgentFixed: Agente de automação Git com boas práticas em portu...\n  - __init__(self, project_root): Inicializa o agente de automaç...\n  - validate_file_exists(self, file_path): Valida se um arquivo existe an...\n  - safe_add_file(self, file_path): Adiciona um arquivo de forma s...\n  - analyze_changes(self): Analisa mudanças no repositóri...\n  - _detect_task_context(self): Detecta contexto de tarefa atu...\n  - _detect_open_files(self): Detecta arquivos abertos no ID...\n  - _analyze_commit_groups(self, changes): Analisa e agrupa mudanças para...\n  - _group_by_directory(self, files): Agrupa arquivos por diretório....\n  - _group_by_file_type(self, files): Agrupa arquivos por tipo.

Arg...\n  - _group_by_context(self, files): Agrupa arquivos por contexto (...\n  - _get_file_diff(self, file_path): Obtém diff de um arquivo.

Arg...\n  - _extract_context_from_diff(self, diff_content): Extrai contexto de um diff.

A...\n  - _is_similar_context(self, context1, context2): Verifica se dois contextos são...\n  - _consolidate_groups(self, groups): Consolida grupos sobrepostos.
...\n  - _ensure_unique_files(self, groups, all_files): Garante que cada arquivo está ...\n  - _get_file_type(self, file_path): Determina o tipo de um arquivo...\n  - _determine_type_from_files(self, files): Determina o tipo de commit bas...\n  - _generate_group_message(self, files, commit_type): Gera mensagem para um grupo de...\n  - _determine_commit_type(self, changes): Determina o tipo de commit bas...\n  - _generate_change_summary(self, changes): Gera resumo das mudanças em po...\n  - generate_commit_message(self, changes): Gera mensagem de commit inteli...\n  - validate_commit_message(self, message): Valida mensagem de commit segu...\n  - execute_commit(self, message, auto_push): Executa commit com validação.
...\n  - auto_commit(self, auto_push): Executa commit automático comp...\n  - execute_multiple_commits(self, commit_groups, auto_push): Executa múltiplos commits base...\n
Imports (8):
.AgentorchestratorModule, subprocess, re, logging, datetime.datetime, sys, argparse, difflib

Autor: Documentation Agent
Data: 2025-08-01 15:05:58
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

