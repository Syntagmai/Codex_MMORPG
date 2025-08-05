# Regras de Organização de Logs

## 📋 **Objetivo**
Garantir que todos os logs sejam organizados na pasta `wiki/log/` e que scripts futuros sigam o padrão correto, mantendo a estrutura organizada e limpa.

## 🎯 **Regras Principais**

### **1. Localização de Logs**
- **✅ Local Correto**: `wiki/log/` - Única pasta para todos os logs
- **❌ Local Incorreto**: Raiz do projeto (`*.log`)
- **❌ Local Incorreto**: Qualquer outra pasta fora de `wiki/log/`

### **2. Estrutura de Logs**
```
wiki/log/
├── 📄 *.log (logs de scripts - NÃO MOVER)
├── 📄 *.md (relatórios - ORGANIZAR)
├── 📁 reports/ (relatórios organizados)
│   ├── 📁 current/ (relatórios atuais)
│   └── 📁 YYYY-MM/ (relatórios por mês/ano)
├── 📁 archives/ (arquivos antigos)
│   ├── 📁 old_reports/
│   ├── 📁 historical_data/
│   └── 📁 obsolete_files/
├── 📁 completed_tasks/ (tarefas concluídas)
│   ├── 📁 bug_fixes/
│   ├── 📁 feature_implementations/
│   └── 📁 system_updates/
├── 📁 temp_tasks/ (tarefas temporárias)
├── 📁 aaa_validation/ (validações AAA)
├── 📁 aaa_fixes/ (correções AAA)
├── 📁 learning/ (materiais de aprendizado)
├── 📁 python_agent/ (logs do agente Python)
└── 📁 recipes/ (receitas de execução)
```

### **3. Categorização de Arquivos**

#### **📄 Logs de Scripts (NÃO MOVER)**
- **Localização**: Raiz da pasta `wiki/log/`
- **Padrão**: `*.log`
- **Exemplos**: `git_automation.log`, `intelligent_organization.log`
- **Regra**: Logs de scripts devem permanecer na raiz para fácil acesso

#### **📄 Relatórios (ORGANIZAR)**
- **Padrão**: `*_report.md`, `Relatório_*.md`, `RELATORIO_*.md`
- **Destino**: `reports/YYYY-MM/`
- **Organização**: Por data de criação/modificação

#### **📄 Tarefas (ORGANIZAR)**
- **Padrão**: `TASK_*.md`, `*_task.md`, `*_TASK.md`
- **Destino**: `completed_tasks/` ou `temp_tasks/`
- **Critério**: Status da tarefa (concluída vs. temporária)

#### **📄 Receitas (ORGANIZAR)**
- **Padrão**: `*_RECIPE.md`, `*_recipe.md`
- **Destino**: `recipes/`

#### **📄 Arquivos Temporários (LIMPAR)**
- **Padrão**: `*_temp.md`, `*_tmp.md`, `temp_*`, `tmp_*`
- **Ação**: Mover para `temp_tasks/` ou remover se antigos

#### **📄 Arquivos Obsoletos (ARQUIVAR)**
- **Padrão**: `*_obsolete.md`, `*_archive.md`, `*_deprecated.md`
- **Destino**: `archives/obsolete_files/`

### **4. Limites de Arquivos na Raiz**
- **Máximo**: 50 arquivos na raiz da pasta `wiki/log/`
- **Ação**: Se exceder, executar organização imediata
- **Exceção**: Logs de scripts não contam no limite

### **5. Verificação de Qualidade**
- **✅ Sem arquivos duplicados**
- **✅ Nomes de arquivo padronizados**
- **✅ Estrutura de pastas respeitada**
- **✅ Logs de scripts na raiz**
- **✅ Relatórios organizados por data**

## 🔧 **Padrão de Configuração de Logging**

### **Para Scripts Python:**
```python
# Configuração de logging
log_dir = Path.cwd() / 'wiki' / 'log'
log_dir.mkdir(parents=True, exist_ok=True)
log_file = log_dir / 'nome_do_script.log'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
```

### **Para Agentes BMAD:**
```python
# Configurar logging
log_dir = self.base_path / 'wiki' / 'log'
log_dir.mkdir(parents=True, exist_ok=True)
log_file = log_dir / 'nome_do_agente.log'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
```

### **4. Nomenclatura de Logs**
- **Formato**: `nome_do_script.log` ou `nome_do_agente.log`
- **Encoding**: UTF-8 para suporte a caracteres especiais
- **Timestamp**: Incluído automaticamente pelo logging

### **5. Verificação Obrigatória**
Antes de criar qualquer script:
1. ✅ Verificar se pasta `wiki/log/` existe
2. ✅ Criar pasta se não existir
3. ✅ Usar caminho relativo correto
4. ✅ Testar geração de log

## 🔧 **Scripts Corrigidos**

### **Scripts de Update:**
- ✅ `git_task_integration.py` → `wiki/log/git_task_integration.log`
- ✅ `final_commit_verification.py` → `wiki/log/final_commit_verification.log`

### **Agentes BMAD:**
- ✅ `intelligent_organization_agent.py` → `wiki/log/intelligent_organization.log`
- ✅ `git_automation_agent.py` → `wiki/log/git_automation.log`
- ✅ `researcher_agent.py` → `wiki/log/researcher_agent.log`
- ✅ `path_validator_agent.py` → `wiki/log/path_validator.log`

### **Ferramentas:**
- ✅ `file_mover.py` → `wiki/log/file_mover.log`

## 📝 **Template para Novos Scripts**

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nome do Script
Descrição do que o script faz
"""

import logging
import sys
from pathlib import Path

# Configuração de logging
log_dir = Path.cwd() / 'wiki' / 'log'
log_dir.mkdir(parents=True, exist_ok=True)
log_file = log_dir / 'nome_do_script.log'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

# Seu código aqui...
```

## 🔄 **Comandos de Organização**

### **Organização Completa**
```bash
python wiki/bmad/agents/intelligent_organization_agent.py --full
```

### **Apenas Detecção de Problemas**
```bash
python wiki/bmad/agents/intelligent_organization_agent.py --detect
```

### **Apenas Limpeza de Temporários**
```bash
python wiki/bmad/agents/intelligent_organization_agent.py --cleanup
```

### **Apenas Organização por Categoria**
```bash
python wiki/bmad/agents/intelligent_organization_agent.py --organize
```

## ⚠️ **Problemas Conhecidos e Soluções**

### **Erro de Permissão no Windows**
- **Problema**: `[WinError 5] Access denied: 'wiki\\log\\temp_tasks'`
- **Solução**: Executar PowerShell como administrador ou verificar permissões da pasta
- **Workaround**: O agente continua a execução mesmo com este erro

### **Arquivos Temporários Não Removidos**
- **Problema**: Arquivos em `temp_tasks/` não são removidos automaticamente
- **Solução**: Limpeza manual periódica ou ajuste de permissões
- **Prevenção**: Verificar permissões antes da execução

## 📊 **Execução Obrigatória**

### **Frequência**: Semanal (toda sexta-feira)
### **Comando**: `python wiki/bmad/agents/intelligent_organization_agent.py --full`
### **Verificação**: Após cada execução, verificar se não há erros
### **Relatório**: Gerar relatório de organização após execução

---

**Regras Consolidadas**: 2025-01-27  
**Status**: Ativo e Funcional  
**Próxima Revisão**: 2025-02-03 