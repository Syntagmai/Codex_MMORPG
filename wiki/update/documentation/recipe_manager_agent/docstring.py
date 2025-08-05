"""
recipe_manager_agent

Recipe Manager Agent - Sistema de Receitas Python

Este agente implementa um sistema de receitas para tarefas Python comuns,
permitindo criar, gerenciar e executar receitas reutilizáveis.

Módulo: recipe_manager_agent
Caminho: wiki\update\recipe_manager_agent.py
Linhas de código: 570
Complexidade: 45.00

Funções (23):
- main(): Função principal...\n- __init__(self, recipes_path): ...\n- load_recipes(self): Carrega todas as receitas do diretório...\n- _dict_to_recipe(self, data): Converte dicionário para objeto Recipe...\n- _recipe_to_dict(self, recipe): Converte objeto Recipe para dicionário...\n- create_recipe(self, recipe): Cria uma nova receita...\n- get_recipe(self, name): Obtém uma receita pelo nome...\n- list_recipes(self, category): Lista todas as receitas, opcionalmente filtradas p...\n- execute_recipe(self, name, args): Executa uma receita...\n- _execute_step(self, step, args): Executa um passo da receita...\n- _execute_python_script(self, script_args, recipe_args): Executa um script Python...\n- _execute_shell_command(self, command_args, recipe_args): Executa um comando shell...\n- _execute_copy_operation(self, copy_args, recipe_args): Executa operação de cópia...\n- _execute_create_operation(self, create_args, recipe_args): Executa operação de criação...\n- _substitute_variables(self, text, args): Substitui variáveis no texto...\n- _evaluate_condition(self, condition, args): Avalia uma condição...\n- _check_dependencies(self, dependencies): Verifica se as dependências estão disponíveis...\n- _save_recipe(self, recipe): Salva uma receita no arquivo...\n- get_execution_history(self): Retorna o histórico de execuções...\n- get_statistics(self): Retorna estatísticas das receitas...\n- __init__(self): ...\n- execute_task_12_9(self): Executa a Task 12.9: Criar sistema de receitas Pyt...\n- _create_sample_recipes(self): Cria receitas de exemplo...\n
Classes (5):
- RecipeStep: Passo de uma receita...\n- Recipe: Receita Python...\n- RecipeExecution: Resultado da execução de uma receita...\n- RecipeManager: Gerenciador de receitas Python...\n  - __init__(self, recipes_path): ...\n  - load_recipes(self): Carrega todas as receitas do d...\n  - _dict_to_recipe(self, data): Converte dicionário para objet...\n  - _recipe_to_dict(self, recipe): Converte objeto Recipe para di...\n  - create_recipe(self, recipe): Cria uma nova receita...\n  - get_recipe(self, name): Obtém uma receita pelo nome...\n  - list_recipes(self, category): Lista todas as receitas, opcio...\n  - execute_recipe(self, name, args): Executa uma receita...\n  - _execute_step(self, step, args): Executa um passo da receita...\n  - _execute_python_script(self, script_args, recipe_args): Executa um script Python...\n  - _execute_shell_command(self, command_args, recipe_args): Executa um comando shell...\n  - _execute_copy_operation(self, copy_args, recipe_args): Executa operação de cópia...\n  - _execute_create_operation(self, create_args, recipe_args): Executa operação de criação...\n  - _substitute_variables(self, text, args): Substitui variáveis no texto...\n  - _evaluate_condition(self, condition, args): Avalia uma condição...\n  - _check_dependencies(self, dependencies): Verifica se as dependências es...\n  - _save_recipe(self, recipe): Salva uma receita no arquivo...\n  - get_execution_history(self): Retorna o histórico de execuçõ...\n  - get_statistics(self): Retorna estatísticas das recei...\n- RecipeManagerAgent: Agente principal para gerenciamento de receitas...\n  - __init__(self): ...\n  - execute_task_12_9(self): Executa a Task 12.9: Criar sis...\n  - _create_sample_recipes(self): Cria receitas de exemplo...\n
Imports (18):
os, sys, json, logging, subprocess, time, pathlib.Path, typing.Dict, typing.List, typing.Optional...

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

