# Python Agent Rules

## 📋 Regras do Agente Python Especializado

Este arquivo define as regras para o **agente Python especializado** que gerencia desenvolvimento, qualidade e otimização de código Python no projeto OTClient.

---

## 🎯 Regras Principais

### 1. **Agente Python Obrigatório**
**SEMPRE use o agente Python para qualquer tarefa relacionada a arquivos .py.** O agente Python é especializado em desenvolvimento, qualidade e otimização de código Python.

### 2. **Análise Automática Obrigatória**
**SEMPRE analise arquivos Python antes de qualquer modificação.** O agente deve verificar qualidade, detectar erros e sugerir melhorias automaticamente.

### 3. **Padrões de Qualidade**
**SEMPRE mantenha padrões de qualidade Python estabelecidos:**
- ✅ Shebang Python obrigatório
- ✅ Encoding UTF-8 obrigatório
- ✅ Docstrings em módulos, classes e funções
- ✅ Type hints quando apropriado
- ✅ Imports organizados (padrão → projeto → outros)
- ✅ Tratamento de exceções específico

### 4. **Log de Melhorias**
**SEMPRE mantenha log de erros e melhorias.** O agente deve registrar todas as melhorias aplicadas para evolução contínua.

### 5. **Integração com Arquivos Base**
**SEMPRE reutilize padrões da pasta `wiki/agente_python_base/`.** Os arquivos base contêm conhecimento valioso que deve ser integrado.

---

## 🔧 Funcionalidades Obrigatórias

### 📊 **Análise de Arquivos Python**
- **Análise sintática** usando AST
- **Detecção de 24 tipos** de erros comuns
- **Verificação de padrões** do projeto
- **Score de qualidade** (0-100)
- **Análise de estrutura** (classes, funções, imports)

### 🐍 **Criação de Arquivos Python**
- **Estrutura padrão** otimizada
- **Imports organizados** automaticamente
- **Docstrings** obrigatórias
- **Type hints** básicos
- **Tratamento de erros** adequado

### ⚡ **Otimização Automática**
- **Reorganização de imports**
- **Adição de encoding UTF-8**
- **Correção de type hints**
- **Backup automático** antes de otimizar
- **Relatório de melhorias**

### 📋 **Relatórios e Logs**
- **Log de erros** (`python_errors.json`)
- **Log de melhorias** (`python_improvements.json`)
- **Relatórios de qualidade** (`python_agent_report.md`)
- **Estatísticas** de evolução

---

## 🎯 Contextos de Ativação

### **Detecção Automática**
O agente Python é ativado automaticamente quando:

#### **Extensões de Arquivo**
- `.py` - Qualquer arquivo Python

#### **Palavras-chave**
- "python", "py", "script", "automação"
- "editar arquivo python", "criar script"
- "otimizar python", "melhorar código"
- "bug python", "erro script"

#### **Padrões de Contexto**
```python
"python_file_edit": {
    "keywords": ["editar", "arquivo", "python", ".py", "script", "automação"],
    "agents": ["python_agent"],
    "workflow": "python_development"
},
"python_optimization": {
    "keywords": ["otimizar", "python", "qualidade", "refatorar", "melhorar"],
    "agents": ["python_agent"],
    "workflow": "python_optimization"
},
"python_bug_fix": {
    "keywords": ["bug", "python", "erro", "corrigir", "problema"],
    "agents": ["python_agent", "qa_tester"],
    "workflow": "python_bug_fix"
}
```

---

## 🔄 Workflows Especializados

### **1. Python Development**
- **Agentes**: Python Agent
- **Fases**: analysis → implementation → optimization → testing
- **Duração**: 1-2 hours
- **Descrição**: Desenvolvimento de scripts Python

### **2. Python Optimization**
- **Agentes**: Python Agent
- **Fases**: analysis → optimization → validation
- **Duração**: 30min-1h
- **Descrição**: Otimização de código Python existente

### **3. Python Bug Fix**
- **Agentes**: Python Agent, QA Tester
- **Fases**: identification → fix → validation
- **Duração**: 1-2 hours
- **Descrição**: Correção de bugs em código Python

---

## 📁 Estrutura de Arquivos

### **Arquivos do Agente**
```
wiki/update/python_agent/
├── python_agent_system.py              # Sistema principal
├── update_orchestrator_with_python_agent.py  # Integração
└── PYTHON_AGENT_IMPLEMENTATION_REPORT.md     # Relatório

wiki/log/python_agent/
├── python_errors.json                  # Log de erros
├── python_improvements.json            # Log de melhorias
└── python_agent_report.md              # Relatório de qualidade
```

### **Arquivos Base Reutilizados**
```
wiki/agente_python_base/
├── agents/python_agent.py              # Agente base
├── scripts/analisador_erros.py         # Analisador de erros
└── knowledge/py_patterns.json          # Padrões de erro
```

---

## 🎨 Padrões de Qualidade

### **Estrutura de Arquivo Padrão**
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
{description}
"""
import os
import json
import re
from datetime import datetime
from typing import Dict, List, Any

class {ClassName}:
    """{class_description}"""
    
    def __init__(self):
        pass
    
    def main(self):
        """Função principal"""
        pass

if __name__ == "__main__":
    main()
```

### **Organização de Imports**
1. **Imports padrão**: os, sys, json, re, datetime, pathlib, typing
2. **Imports específicos do projeto**: ast, subprocess, shutil, tempfile
3. **Outros imports**: Qualquer outro módulo

### **Tratamento de Erros**
```python
try:
    # Operação que pode falhar
    pass
except SpecificError as e:
    # Tratamento específico
    pass
except Exception as e:
    # Log do erro
    print(f"Erro inesperado: {e}")
```

---

## 📊 Métricas de Qualidade

### **Score de Qualidade (0-100)**
- **90-100**: Excelente - Código de produção
- **70-89**: Bom - Código funcional com pequenas melhorias
- **50-69**: Regular - Precisa de otimizações
- **0-49**: Ruim - Precisa de refatoração

### **Fatores de Pontuação**
- **Sintaxe válida**: +20 pontos
- **Encoding UTF-8**: +10 pontos
- **Docstrings**: +10 pontos
- **Type hints**: +10 pontos
- **Imports organizados**: +10 pontos
- **Tratamento de erros**: +10 pontos
- **Estrutura padrão**: +10 pontos
- **Sem erros detectados**: +20 pontos

---

## 🔍 Detecção de Erros

### **24 Tipos de Erros Identificados**
1. **missing_encoding** - Falta encoding UTF-8
2. **missing_type_hints** - Falta type hints
3. **hardcoded_paths** - Caminhos hardcoded
4. **print_statements** - Print statements (deveria usar logging)
5. **bare_except** - Exceções genéricas
6. **unused_imports** - Imports não utilizados
7. **missing_import** - Imports faltando
8. **type_coercion** - Conversão de tipos inadequada
9. **syntax_error** - Erro de sintaxe
10. **missing_header** - Falta shebang Python
11. **missing_module_docstring** - Falta docstring do módulo
12. **base_pattern** - Padrões base da pasta agente_python_base

### **Padrões Base Integrados**
- **NameError**: name 'request' is not defined → import requests
- **TypeError**: expected str, got int → usar str() para conversão
- **SyntaxError**: unexpected indent → verificar espaços e tabulações

---

## 🚀 Otimizações Automáticas

### **Correções Aplicadas**
1. **Adicionar encoding UTF-8** se não existir
2. **Reorganizar imports** na ordem padrão
3. **Adicionar type hints** básicos
4. **Corrigir open()** com encoding
5. **Aplicar padrões base** conhecidos

### **Backup Automático**
- **Arquivo original** salvo como `.backup`
- **Versão otimizada** substitui original
- **Relatório de mudanças** gerado

---

## 📋 Integração com Sistema

### **Orquestrador Inteligente**
- **Detecção automática** de contextos Python
- **Seleção inteligente** do agente Python
- **Workflows especializados** para Python
- **Logs de execução** detalhados

### **Sistema de Automação de Tarefas**
- **Criação de tarefas** para operações Python
- **Execução passo a passo** com logs
- **Relatórios finais** com métricas
- **Organização** em pastas específicas

### **Sistema de Limpeza**
- **Logs organizados** em `wiki/log/python_agent/`
- **Relatórios arquivados** automaticamente
- **Receitas** para reproduzir resultados

---

## ⚡ Aplicação Automática

### **Triggers de Ativação**
- ✅ Qualquer arquivo `.py` mencionado
- ✅ Palavras-chave Python detectadas
- ✅ Contexto de desenvolvimento Python
- ✅ Otimização de código Python
- ✅ Correção de bugs Python

### **Execução Obrigatória**
1. **Análise automática** do arquivo Python
2. **Detecção de problemas** e sugestões
3. **Aplicação de otimizações** quando apropriado
4. **Geração de relatórios** de qualidade
5. **Atualização de logs** de melhorias

---

## 🎯 Benefícios Esperados

### **Qualidade do Código**
- **Detecção automática** de problemas
- **Padronização** de estrutura
- **Melhoria contínua** da qualidade

### **Produtividade**
- **Criação rápida** de scripts Python
- **Otimização automática** de código existente
- **Redução de erros** comuns

### **Manutenibilidade**
- **Log de melhorias** para evolução
- **Padrões consistentes** em todo o projeto
- **Documentação automática** de mudanças

---

## 📚 Referências

### **Arquivos Base**
- `wiki/agente_python_base/agents/python_agent.py`
- `wiki/agente_python_base/scripts/analisador_erros.py`
- `wiki/agente_python_base/knowledge/py_patterns.json`

### **Sistema Principal**
- `wiki/update/python_agent/python_agent_system.py`
- `wiki/update/enhanced_intelligent_orchestrator.py`
- `wiki/update/task_automation_system.py`

### **Relatórios**
- `wiki/update/python_agent/PYTHON_AGENT_IMPLEMENTATION_REPORT.md`
- `wiki/log/python_agent/python_agent_report.md`

---

*Regras do Agente Python - Especializado em desenvolvimento e qualidade de código Python* 