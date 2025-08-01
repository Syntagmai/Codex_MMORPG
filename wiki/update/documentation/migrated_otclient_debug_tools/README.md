# migrated_otclient_debug_tools

## Descrição

Módulo Python sem descrição.

## Informações Técnicas

- **Módulo**: migrated_otclient_debug_tools
- **Caminho**: wiki\update\modules\analysis\source_analyzer\migrated_otclient_debug_tools.py
- **Linhas de código**: 604
- **Complexidade**: 59.00
- **Funções**: 16
- **Classes**: 1

## Funções

### main

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 29

Função principal

### integrate_with_module

**Parâmetros**: Nenhum
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 3

Integra o script com o módulo de destino.

### __init__

**Parâmetros**: self, work_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Sem documentação.

### check_debug_environment

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 51

Verifica ambiente de debug

### check_tool_available

**Parâmetros**: self, tool_name
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Verifica se ferramenta está disponível

### check_lua_debugger

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Verifica debugger Lua

### analyze_crash_dump

**Parâmetros**: self, crash_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 43

Analisa dump de crash

### identify_crash_type

**Parâmetros**: self, crash_content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Identifica tipo de crash

### extract_stack_trace

**Parâmetros**: self, crash_content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Extrai stack trace do crash

### extract_memory_info

**Parâmetros**: self, crash_content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Extrai informações de memória

### extract_system_info

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Extrai informações do sistema

### generate_crash_recommendations

**Parâmetros**: self, crash_analysis
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 60

Gera recomendações baseadas na análise de crash

### analyze_performance

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 90

Analisa performance do sistema

### generate_performance_recommendations

**Parâmetros**: self, performance_analysis
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Gera recomendações de performance

### generate_debug_report

**Parâmetros**: self, environment, crash_analysis, performance_analysis
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 76

Gera relatório completo de debug

### save_debug_report

**Parâmetros**: self, report, output_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Salva relatório de debug

## Classes

### OTClientDebugTools

**Herança**: Nenhuma
**Atributos**: environment, debug_files, cmake_file, lua_debugger, crash_analysis, crash_path, content_lower, stack_trace, patterns, lines, memory_info, memory_patterns, content_lower, system_info, recommendations, crash_type, performance_analysis, recommendations, memory_usage, memory_percent, cpu_usage, cpu_percent, disk_usage, disk_percent, report, debug_files, build_config, debug_tools, file_path, result, result, match, memory, cpu_percent, disk, network, status, size, recommendations, memory_usage, cpu_usage, disk_usage, recommendations, output_path, cmake_content, crash_content, match, status, status, tool_type
**Métodos**: 14
**Linhas**: 521

Ferramentas de debug especializadas para OTClient

#### __init__

**Parâmetros**: self, work_dir
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 16

Sem documentação.

#### check_debug_environment

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 51

Verifica ambiente de debug

#### check_tool_available

**Parâmetros**: self, tool_name
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 7

Verifica se ferramenta está disponível

#### check_lua_debugger

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 22

Verifica debugger Lua

#### analyze_crash_dump

**Parâmetros**: self, crash_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 43

Analisa dump de crash

#### identify_crash_type

**Parâmetros**: self, crash_content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Identifica tipo de crash

#### extract_stack_trace

**Parâmetros**: self, crash_content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 20

Extrai stack trace do crash

#### extract_memory_info

**Parâmetros**: self, crash_content
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 27

Extrai informações de memória

#### extract_system_info

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 17

Extrai informações do sistema

#### generate_crash_recommendations

**Parâmetros**: self, crash_analysis
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 60

Gera recomendações baseadas na análise de crash

#### analyze_performance

**Parâmetros**: self
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 90

Analisa performance do sistema

#### generate_performance_recommendations

**Parâmetros**: self, performance_analysis
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 34

Gera recomendações de performance

#### generate_debug_report

**Parâmetros**: self, environment, crash_analysis, performance_analysis
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 76

Gera relatório completo de debug

#### save_debug_report

**Parâmetros**: self, report, output_file
**Retorna**: Any
**Complexidade**: Low
**Linhas**: 12

Salva relatório de debug

## Imports

.SourceanalyzerModule, subprocess, sys, os, re, datetime.datetime, platform, re, psutil, psutil, psutil, psutil, psutil

## Uso

```python
# Exemplo de uso do módulo migrated_otclient_debug_tools
# Adicione exemplos específicos aqui
```

## Autor

Documentation Agent - 2025-08-01 15:05:58
