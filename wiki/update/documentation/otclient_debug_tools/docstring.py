"""
otclient_debug_tools

OTClient Debug Tools
Ferramentas especializadas para debug do OTClient

Módulo: otclient_debug_tools
Caminho: wiki\update\otclient_debug_tools.py
Linhas de código: 574
Complexidade: 57.00

Funções (15):
- main(): Função principal...\n- __init__(self, work_dir): ...\n- check_debug_environment(self): Verifica ambiente de debug...\n- check_tool_available(self, tool_name): Verifica se ferramenta está disponível...\n- check_lua_debugger(self): Verifica debugger Lua...\n- analyze_crash_dump(self, crash_file): Analisa dump de crash...\n- identify_crash_type(self, crash_content): Identifica tipo de crash...\n- extract_stack_trace(self, crash_content): Extrai stack trace do crash...\n- extract_memory_info(self, crash_content): Extrai informações de memória...\n- extract_system_info(self): Extrai informações do sistema...\n- generate_crash_recommendations(self, crash_analysis): Gera recomendações baseadas na análise de crash...\n- analyze_performance(self): Analisa performance do sistema...\n- generate_performance_recommendations(self, performance_analysis): Gera recomendações de performance...\n- generate_debug_report(self, environment, crash_analysis, performance_analysis): Gera relatório completo de debug...\n- save_debug_report(self, report, output_file): Salva relatório de debug...\n
Classes (1):
- OTClientDebugTools: Ferramentas de debug especializadas para OTClient...\n  - __init__(self, work_dir): ...\n  - check_debug_environment(self): Verifica ambiente de debug...\n  - check_tool_available(self, tool_name): Verifica se ferramenta está di...\n  - check_lua_debugger(self): Verifica debugger Lua...\n  - analyze_crash_dump(self, crash_file): Analisa dump de crash...\n  - identify_crash_type(self, crash_content): Identifica tipo de crash...\n  - extract_stack_trace(self, crash_content): Extrai stack trace do crash...\n  - extract_memory_info(self, crash_content): Extrai informações de memória...\n  - extract_system_info(self): Extrai informações do sistema...\n  - generate_crash_recommendations(self, crash_analysis): Gera recomendações baseadas na...\n  - analyze_performance(self): Analisa performance do sistema...\n  - generate_performance_recommendations(self, performance_analysis): Gera recomendações de performa...\n  - generate_debug_report(self, environment, crash_analysis, performance_analysis): Gera relatório completo de deb...\n  - save_debug_report(self, report, output_file): Salva relatório de debug...\n
Imports (18):
json, subprocess, sys, os, re, datetime.datetime, pathlib.Path, typing.Dict, typing.List, typing.Any...

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

