# Regras de Code Cleanup e Organização Automática

## 🎯 Propósito

Definir regras para **limpeza automática de código** e **organização inteligente** de arquivos, pastas e relatórios, garantindo um sistema sempre limpo, organizado e eficiente.

---

## 🧹 Princípios de Code Cleanup

### **Organização Automática**
- **SEMPRE mantenha** estrutura de pastas organizada
- **SEMPRE categorize** arquivos por tipo e função
- **SEMPRE remova** arquivos temporários automaticamente
- **SEMPRE organize** relatórios em pastas específicas
- **SEMPRE mantenha** histórico limpo e rastreável

### **Limpeza Inteligente**
- **SEMPRE identifique** arquivos obsoletos automaticamente
- **SEMPRE mova** arquivos para pastas apropriadas
- **SEMPRE mantenha** apenas arquivos essenciais
- **SEMPRE preserve** conhecimento importante
- **SEMPRE documente** mudanças de organização

---

## 📁 Estrutura de Organização Padrão

### **Pasta `wiki/log/` - Estrutura Limpa**
```
wiki/log/
├── reports/                    # Relatórios organizados por data
│   ├── 2025-01/               # Relatórios de janeiro 2025
│   ├── 2025-02/               # Relatórios de fevereiro 2025
│   └── current/                # Relatórios atuais
├── completed_tasks/            # Tarefas concluídas
│   ├── system_updates/         # Atualizações do sistema
│   ├── feature_implementations/ # Implementações de features
│   └── bug_fixes/              # Correções de bugs
├── archives/                   # Arquivos arquivados
│   ├── obsolete_files/         # Arquivos obsoletos
│   ├── historical_data/        # Dados históricos
│   └── old_reports/            # Relatórios antigos
├── recipes/                    # Receitas para reproduzir resultados
├── learning/                   # Dados de aprendizado
├── python_agent/               # Logs do agente Python
├── aaa_validation/             # Validações AAA
├── aaa_fixes/                  # Correções AAA
└── temp_tasks/                 # Tarefas temporárias
```

### **Pasta `wiki/update/` - Scripts Organizados**
```
wiki/update/
├── core/                       # Scripts principais
│   ├── auto_update_all_maps.py
│   ├── cleanup_system.py
│   └── git_task_integration.py
├── agents/                     # Scripts de agentes
│   ├── agent_organizer.py
│   └── python_agent_system.py
├── maintenance/                # Scripts de manutenção
│   ├── optimize_json_maps.py
│   └── system_cleanup.py
└── specialized/                # Scripts especializados
    ├── aaa_agent_specialization_system.py
    └── enhanced_intelligent_orchestrator.py
```

---

## 🤖 Agente de Organização Automática

### **Funcionalidades Obrigatórias**

#### **1. Detecção Automática de Desorganização**
```python
def detect_organization_issues():
    """Detecta problemas de organização automaticamente"""
    
    issues = {
        "files_in_wrong_location": [],
        "duplicate_files": [],
        "obsolete_files": [],
        "unorganized_reports": [],
        "temp_files_not_cleaned": []
    }
    
    # Verificar arquivos na pasta log
    log_files = scan_log_directory()
    for file in log_files:
        if is_in_wrong_location(file):
            issues["files_in_wrong_location"].append(file)
        
        if is_obsolete(file):
            issues["obsolete_files"].append(file)
    
    return issues
```

#### **2. Organização Automática por Categoria**
```python
def organize_by_category():
    """Organiza arquivos por categoria automaticamente"""
    
    categories = {
        "reports": {
            "patterns": ["*_REPORT.md", "*_report.md", "Relatório_*.md"],
            "destination": "wiki/log/reports/current/"
        },
        "completed_tasks": {
            "patterns": ["TASK_*.md", "*_task.md"],
            "destination": "wiki/log/completed_tasks/"
        },
        "recipes": {
            "patterns": ["*_recipe.md", "*_RECIPE.md"],
            "destination": "wiki/log/recipes/"
        },
        "archives": {
            "patterns": ["*_old.md", "*_obsolete.md", "*_archive.md"],
            "destination": "wiki/log/archives/"
        }
    }
    
    for category, config in categories.items():
        organize_files_by_pattern(config["patterns"], config["destination"])
```

#### **3. Limpeza Automática de Arquivos Temporários**
```python
def cleanup_temp_files():
    """Remove arquivos temporários automaticamente"""
    
    temp_patterns = [
        "*.tmp", "*.temp", "*_temp.md", "*_tmp.md",
        "temp_*", "tmp_*", "*_backup.md", "*_old.md"
    ]
    
    for pattern in temp_patterns:
        remove_files_by_pattern(pattern)
```

#### **4. Organização por Data**
```python
def organize_by_date():
    """Organiza relatórios por data automaticamente"""
    
    current_month = datetime.now().strftime("%Y-%m")
    reports_dir = Path("wiki/log/reports")
    
    # Criar pasta do mês se não existir
    month_dir = reports_dir / current_month
    month_dir.mkdir(exist_ok=True)
    
    # Mover relatórios para pasta do mês
    for report_file in reports_dir.glob("*.md"):
        if report_file.parent == reports_dir:  # Não está em subpasta
            shutil.move(str(report_file), str(month_dir / report_file.name))
```

---

## 📋 Regras de Organização Específicas

### **📄 Relatórios**
- **SEMPRE organize** por data (YYYY-MM)
- **SEMPRE use** nomenclatura padronizada
- **SEMPRE mova** para pasta `reports/current/` se ativo
- **SEMPRE arquive** em `reports/YYYY-MM/` se antigo
- **SEMPRE mantenha** apenas relatórios relevantes

### **📋 Tarefas**
- **SEMPRE mova** tarefas concluídas para `completed_tasks/`
- **SEMPRE categorize** por tipo (system_updates, features, bugs)
- **SEMPRE mantenha** apenas tarefas ativas em `temp_tasks/`
- **SEMPRE arquive** tarefas antigas em `archives/`

### **📚 Receitas**
- **SEMPRE mantenha** em `recipes/` organizadas por categoria
- **SEMPRE use** nomenclatura descritiva
- **SEMPRE inclua** ingredientes e passos claros
- **SEMPRE mantenha** atualizadas

### **🗂️ Arquivos Obsoletos**
- **SEMPRE identifique** automaticamente
- **SEMPRE mova** para `archives/obsolete_files/`
- **SEMPRE documente** motivo da obsolescência
- **SEMPRE mantenha** backup antes de remover

---

## 🔄 Processo de Limpeza Automática

### **📋 Checklist de Limpeza Diária**
```python
def daily_cleanup():
    """Executa limpeza diária automática"""
    
    # 1. Detectar problemas de organização
    issues = detect_organization_issues()
    
    # 2. Organizar relatórios por data
    organize_by_date()
    
    # 3. Mover tarefas concluídas
    move_completed_tasks()
    
    # 4. Limpar arquivos temporários
    cleanup_temp_files()
    
    # 5. Organizar por categoria
    organize_by_category()
    
    # 6. Remover duplicatas
    remove_duplicates()
    
    # 7. Atualizar índices
    update_organization_index()
```

### **📋 Checklist de Limpeza Semanal**
```python
def weekly_cleanup():
    """Executa limpeza semanal mais profunda"""
    
    # 1. Limpeza diária
    daily_cleanup()
    
    # 2. Arquivar relatórios antigos
    archive_old_reports()
    
    # 3. Consolidar relatórios similares
    consolidate_similar_reports()
    
    # 4. Otimizar estrutura de pastas
    optimize_folder_structure()
    
    # 5. Validar integridade
    validate_organization_integrity()
    
    # 6. Gerar relatório de limpeza
    generate_cleanup_report()
```

---

## 🎯 Regras de Nomenclatura

### **📄 Relatórios**
```
Formato: [TIPO]_[DESCRIÇÃO]_[DATA]_REPORT.md
Exemplos:
- SYSTEM_CLEANUP_2025-01-28_REPORT.md
- GIT_AUTOMATION_2025-01-28_REPORT.md
- AGENT_ORGANIZATION_2025-01-28_REPORT.md
```

### **📋 Tarefas**
```
Formato: TASK_[ID]_[DESCRIÇÃO]_[DATA].md
Exemplos:
- TASK_001_SYSTEM_CLEANUP_2025-01-28.md
- TASK_002_GIT_AUTOMATION_2025-01-28.md
```

### **📚 Receitas**
```
Formato: [CATEGORIA]_[DESCRIÇÃO]_RECIPE.md
Exemplos:
- SYSTEM_CLEANUP_RECIPE.md
- GIT_AUTOMATION_RECIPE.md
- AGENT_ORGANIZATION_RECIPE.md
```

---

## 🤖 Agente de Organização Inteligente

### **Detecção Automática de Contexto**
```python
def detect_file_context(file_path: Path) -> str:
    """Detecta contexto do arquivo automaticamente"""
    
    # Padrões de detecção
    patterns = {
        "report": ["*_REPORT.md", "*_report.md", "Relatório_*.md"],
        "task": ["TASK_*.md", "*_task.md"],
        "recipe": ["*_RECIPE.md", "*_recipe.md"],
        "log": ["*.log", "*_log.md"],
        "config": ["*.json", "*.yaml", "*.yml"],
        "script": ["*.py", "*.sh", "*.bat"]
    }
    
    for context, pattern_list in patterns.items():
        for pattern in pattern_list:
            if file_path.match(pattern):
                return context
    
    return "other"
```

### **Organização Inteligente**
```python
def intelligent_organization():
    """Organização inteligente baseada em contexto"""
    
    # 1. Analisar todos os arquivos
    all_files = scan_all_files()
    
    # 2. Detectar contexto de cada arquivo
    for file_path in all_files:
        context = detect_file_context(file_path)
        
        # 3. Determinar localização ideal
        ideal_location = determine_ideal_location(file_path, context)
        
        # 4. Mover se necessário
        if file_path.parent != ideal_location:
            move_file_safely(file_path, ideal_location)
```

---

## 📊 Métricas de Organização

### **Indicadores de Qualidade**
- **Taxa de arquivos organizados**: > 95%
- **Taxa de limpeza automática**: > 90%
- **Tempo de organização**: < 30 segundos
- **Taxa de detecção de problemas**: > 85%

### **Métricas de Performance**
- **Arquivos processados por minuto**: > 100
- **Tempo de resposta**: < 5 segundos
- **Taxa de erro**: < 1%
- **Eficiência de organização**: > 95%

---

## 🔄 Integração com Sistema Existente

### **Com Sistema de Limpeza**
- **Integração completa** com `cleanup_system.py`
- **Execução automática** após tarefas
- **Relatórios unificados** de limpeza
- **Métricas compartilhadas**

### **Com Sistema de Agentes**
- **Detecção automática** de novos agentes
- **Organização automática** de estrutura
- **Integração com BMAD** completa
- **Workflows coordenados**

### **Com Sistema Git**
- **Commits automáticos** de organização
- **Histórico limpo** de mudanças
- **Rastreabilidade** de organização
- **Backup automático**

---

## 🎯 Regras de Execução

### **🔄 Execução Automática**
- **SEMPRE execute** após conclusão de tarefas
- **SEMPRE execute** diariamente às 00:00
- **SEMPRE execute** semanalmente aos domingos
- **SEMPRE execute** quando detectar desorganização

### **📋 Validação**
- **SEMPRE valide** organização antes de commitar
- **SEMPRE teste** se sistema continua funcionando
- **SEMPRE verifique** se arquivos foram movidos corretamente
- **SEMPRE confirme** se estrutura está limpa

---

## 🎉 Benefícios Esperados

### **🧹 Organização**
- **Sistema sempre limpo** e organizado
- **Arquivos fáceis de encontrar** e acessar
- **Estrutura consistente** e previsível
- **Histórico limpo** e rastreável

### **📊 Eficiência**
- **Busca rápida** de informações
- **Navegação intuitiva** no sistema
- **Manutenção simplificada**
- **Produtividade aumentada**

### **🔄 Sustentabilidade**
- **Sistema escalável** e organizado
- **Processos automatizados** e confiáveis
- **Conhecimento preservado** e acessível
- **Evolução contínua** e organizada

---

*Regras criadas pelo Sistema BMAD - OTClient Documentation* 