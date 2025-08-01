"""
complexity_analyzer



Módulo: complexity_analyzer
Caminho: wiki\update\python_tools\complexity_analyzer.py
Linhas de código: 93
Complexidade: 4.00

Funções (11):
- main(): ...\n- __init__(self): ...\n- analyze_file(self, file_path): ...\n- _analyze_ast(self, tree, file_path): ...\n- __init__(self): ...\n- visit_FunctionDef(self, node): ...\n- visit_ClassDef(self, node): ...\n- visit_If(self, node): ...\n- visit_While(self, node): ...\n- visit_For(self, node): ...\n- visit_ExceptHandler(self, node): ...\n
Classes (2):
- ComplexityAnalyzer: ...\n  - __init__(self): ...\n  - analyze_file(self, file_path): ...\n  - _analyze_ast(self, tree, file_path): ...\n- ComplexityVisitor: ...\n  - __init__(self): ...\n  - visit_FunctionDef(self, node): ...\n  - visit_ClassDef(self, node): ...\n  - visit_If(self, node): ...\n  - visit_While(self, node): ...\n  - visit_For(self, node): ...\n  - visit_ExceptHandler(self, node): ...\n
Imports (8):
ast, json, pathlib.Path, typing.Dict, typing.List, typing.Any, typing.Optional, datetime.datetime

Autor: Documentation Agent
Data: 2025-08-01 15:05:52
"""
