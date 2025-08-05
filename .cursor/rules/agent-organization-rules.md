# Agent Organization Rules

## 📋 Regras de Organização Automática de Agentes

Este arquivo define as regras para **organização automática** de agentes durante implementação, garantindo que todos os agentes sejam integrados corretamente ao sistema BMAD e mantenham estrutura consistente.

---

## 🎯 Regras Principais

### 1. **Estrutura BMAD Obrigatória**
**SEMPRE organize agentes dentro da estrutura BMAD.** Todos os agentes devem ser integrados ao sistema BMAD para manter consistência e organização.

### 2. **Detecção Automática de Agentes**
**SEMPRE detecte automaticamente** quando um novo agente está sendo implementado e organize a estrutura de pastas adequadamente.

### 3. **Migração Automática**
**SEMPRE migre agentes existentes** para a estrutura BMAD quando detectados fora da organização padrão.

### 4. **Estrutura Padrão Obrigatória**
**SEMPRE mantenha estrutura padrão** para todos os agentes dentro do sistema BMAD.

### 5. **Integração Completa**
**SEMPRE integre completamente** o agente ao sistema BMAD, incluindo documentação, workflows e templates.

---

## 📁 Estrutura Padrão de Agentes

### **🗂️ Estrutura BMAD para Agentes**
```
docs/bmad/
├── agents/                          # Todos os agentes especializados
│   ├── python_agent/               # Agente Python
│   │   ├── python_agent.py         # Implementação principal
│   │   ├── patterns/               # Padrões específicos
│   │   │   ├── error_patterns.json # Padrões de erro
│   │   │   └── quality_patterns.json # Padrões de qualidade
│   │   ├── scripts/                # Scripts auxiliares
│   │   │   ├── analyzer.py         # Analisador de código
│   │   │   └── optimizer.py        # Otimizador
│   │   ├── knowledge/              # Base de conhecimento
│   │   │   ├── best_practices.md   # Melhores práticas
│   │   │   └── common_errors.md    # Erros comuns
│   │   └── README.md               # Documentação do agente
│   ├── lua_agent/                  # Agente Lua (futuro)
│   ├── cpp_agent/                  # Agente C++ (futuro)
│   └── BMAD_Agents_Guide.md        # Guia geral dos agentes
├── workflows/                       # Workflows dos agentes
│   ├── python_development.md       # Workflow Python
│   ├── python_optimization.md      # Workflow otimização
│   └── python_bug_fix.md           # Workflow correção
├── templates/                       # Templates dos agentes
│   ├── python_file_template.py     # Template arquivo Python
│   └── agent_report_template.md    # Template relatório
└── guides/                         # Guias específicos
    └── python_agent_guide.md       # Guia do agente Python
```

### **📋 Estrutura Individual do Agente**
```
docs/bmad/agents/{agent_name}/
├── {agent_name}.py                 # Implementação principal
├── patterns/                       # Padrões específicos
│   ├── error_patterns.json         # Padrões de erro
│   ├── quality_patterns.json       # Padrões de qualidade
│   └── context_patterns.json       # Padrões de contexto
├── scripts/                        # Scripts auxiliares
│   ├── analyzer.py                 # Analisador
│   ├── optimizer.py                # Otimizador
│   └── validator.py                # Validador
├── knowledge/                      # Base de conhecimento
│   ├── best_practices.md           # Melhores práticas
│   ├── common_errors.md            # Erros comuns
│   ├── optimization_tips.md        # Dicas de otimização
│   └── integration_guide.md        # Guia de integração
├── logs/                           # Logs específicos do agente
│   ├── error_log.json              # Log de erros
│   ├── improvement_log.json        # Log de melhorias
│   └── performance_log.json        # Log de performance
├── tests/                          # Testes do agente
│   ├── test_integration.py         # Teste de integração
│   ├── test_functionality.py       # Teste de funcionalidade
│   └── test_performance.py         # Teste de performance
├── docs/                           # Documentação
│   ├── README.md                   # Documentação principal
│   ├── API.md                      # Documentação da API
│   └── examples.md                 # Exemplos de uso
└── config/                         # Configurações
    ├── agent_config.json           # Configuração do agente
    └── integration_config.json     # Configuração de integração
```

---

## 🔄 Processo de Organização Automática

### **1. Detecção de Agente**
**SEMPRE detecte quando um agente está sendo implementado:**
- ✅ Menção de "agente" + linguagem/tecnologia
- ✅ Criação de arquivos de agente
- ✅ Pastas com nome "agente_*" ou "*_agent"
- ✅ Implementação de funcionalidades de agente

### **2. Criação de Estrutura**
**SEMPRE crie estrutura padrão automaticamente:**
```python
def create_agent_structure(agent_name: str, agent_type: str):
    """Cria estrutura padrão para novo agente"""
    
    # 1. Criar pasta principal do agente
    agent_path = f"docs/bmad/agents/{agent_name}_agent"
    
    # 2. Criar subpastas padrão
    subfolders = [
        "patterns", "scripts", "knowledge", 
        "logs", "tests", "docs", "config"
    ]
    
    # 3. Criar arquivos padrão
    standard_files = [
        f"{agent_name}_agent.py",
        "patterns/error_patterns.json",
        "patterns/quality_patterns.json",
        "knowledge/best_practices.md",
        "knowledge/common_errors.md",
        "docs/README.md",
        "config/agent_config.json"
    ]
    
    # 4. Integrar ao sistema BMAD
    update_bmad_agents_guide(agent_name, agent_type)
    create_agent_workflows(agent_name, agent_type)
    create_agent_templates(agent_name, agent_type)
```

### **3. Migração de Agentes Existentes**
**SEMPRE migre agentes existentes para estrutura BMAD:**
```python
def migrate_existing_agent(source_path: str, agent_name: str):
    """Migra agente existente para estrutura BMAD"""
    
    # 1. Detectar estrutura atual
    current_structure = analyze_current_structure(source_path)
    
    # 2. Criar estrutura BMAD
    bmad_structure = create_agent_structure(agent_name)
    
    # 3. Migrar arquivos
    migrate_files(source_path, bmad_structure)
    
    # 4. Atualizar referências
    update_references(agent_name)
    
    # 5. Remover estrutura antiga
    cleanup_old_structure(source_path)
```

### **4. Integração Completa**
**SEMPRE integre completamente ao sistema:**
- ✅ **Atualizar** `BMAD_Agents_Guide.md`
- ✅ **Criar workflows** específicos
- ✅ **Criar templates** padronizados
- ✅ **Atualizar orquestrador** com novos padrões
- ✅ **Criar documentação** completa

---

## 🎯 Regras de Implementação

### **📋 Antes de Implementar Agente**
1. **Detectar** necessidade de novo agente
2. **Criar** estrutura BMAD padrão
3. **Migrar** arquivos existentes se houver
4. **Integrar** ao sistema BMAD

### **📋 Durante Implementação**
1. **Seguir** estrutura padrão estabelecida
2. **Criar** documentação completa
3. **Implementar** testes de integração
4. **Configurar** logs e relatórios

### **📋 Após Implementação**
1. **Atualizar** guias BMAD
2. **Criar** workflows específicos
3. **Integrar** ao orquestrador
4. **Validar** funcionamento completo

---

## 🔧 Scripts de Automação

### **1. Detector de Agentes**
```python
def detect_agent_implementation():
    """Detecta quando um agente está sendo implementado"""
    
    # Verificar pastas com padrão de agente
    agent_patterns = [
        "agente_*", "*_agent", "agent_*"
    ]
    
    # Verificar arquivos de agente
    agent_files = [
        "*_agent.py", "*agent*.py", "agent_*.py"
    ]
    
    # Verificar conteúdo relacionado a agentes
    agent_keywords = [
        "agente", "agent", "especializado", "specialized"
    ]
```

### **2. Organizador Automático**
```python
def auto_organize_agents():
    """Organiza automaticamente todos os agentes"""
    
    # 1. Detectar agentes existentes
    existing_agents = detect_existing_agents()
    
    # 2. Migrar para estrutura BMAD
    for agent in existing_agents:
        migrate_to_bmad_structure(agent)
    
    # 3. Criar estrutura padrão
    create_standard_structure()
    
    # 4. Atualizar documentação
    update_bmad_documentation()
```

### **3. Validador de Estrutura**
```python
def validate_agent_structure(agent_name: str):
    """Valida se agente está na estrutura correta"""
    
    required_structure = [
        f"docs/bmad/agents/{agent_name}_agent/",
        f"docs/bmad/agents/{agent_name}_agent/patterns/",
        f"docs/bmad/agents/{agent_name}_agent/scripts/",
        f"docs/bmad/agents/{agent_name}_agent/knowledge/",
        f"docs/bmad/agents/{agent_name}_agent/docs/",
        f"docs/bmad/agents/{agent_name}_agent/config/"
    ]
    
    for path in required_structure:
        if not os.path.exists(path):
            create_missing_structure(path)
```

---

## 📊 Monitoramento e Validação

### **✅ Checklist de Organização**
- [ ] **Estrutura BMAD** criada corretamente
- [ ] **Subpastas padrão** implementadas
- [ ] **Arquivos padrão** criados
- [ ] **Documentação** completa
- [ ] **Integração BMAD** realizada
- [ ] **Orquestrador** atualizado
- [ ] **Workflows** criados
- [ ] **Templates** implementados
- [ ] **Testes** funcionando
- [ ] **Logs** configurados

### **📋 Validação Automática**
```python
def validate_agent_organization():
    """Valida organização completa de agentes"""
    
    # Verificar estrutura BMAD
    validate_bmad_structure()
    
    # Verificar agentes individuais
    validate_individual_agents()
    
    # Verificar integração
    validate_integration()
    
    # Verificar documentação
    validate_documentation()
    
    # Gerar relatório
    generate_organization_report()
```

---

## 🚀 Benefícios da Organização

### **✅ Consistência**
- **Estrutura padronizada** para todos os agentes
- **Documentação uniforme** e completa
- **Integração consistente** com sistema BMAD

### **✅ Manutenibilidade**
- **Organização clara** e lógica
- **Fácil localização** de arquivos
- **Manutenção simplificada**

### **✅ Escalabilidade**
- **Estrutura preparada** para novos agentes
- **Integração automática** com sistema
- **Expansão facilitada**

### **✅ Produtividade**
- **Detecção automática** de agentes
- **Organização automática** de estrutura
- **Integração automática** com sistema

---

## 📚 Referências

### **Arquivos BMAD**
- `docs/bmad/BMAD_System_Guide.md`
- `docs/bmad/agents/BMAD_Agents_Guide.md`
- `docs/bmad/workflows/`
- `docs/bmad/templates/`

### **Agentes Existentes**
- `docs/bmad/agents/python_agent/` (após migração)
- `wiki/agente_python_base/` (para migração)

### **Sistema de Orquestração**
- `scripts/enhanced_intelligent_orchestrator.py`
- `cursor.md`

---

*Regras de Organização Automática de Agentes - Garantindo estrutura consistente e integração completa ao sistema BMAD* 