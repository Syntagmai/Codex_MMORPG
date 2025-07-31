# Regras de Orquestração Inteligente

## 🎯 Propósito

Definir regras para **orquestração automática** de agentes BMAD, eliminando a necessidade de comandos manuais e permitindo que o sistema detecte automaticamente o contexto e coordene os agentes necessários.

---

## 🧠 Princípios Fundamentais

### **Context-Aware Intelligence**
- **SEMPRE analise o contexto** do pedido do usuário automaticamente
- **SEMPRE identifique agentes necessários** baseado no contexto
- **SEMPRE coordene workflow completo** sem intervenção manual
- **SEMPRE reporte progresso** em tempo real
- **SEMPRE sugira próximos passos** automaticamente

### **Automatic Agent Selection**
- **Detecte tecnologias** mencionadas (C++, Lua, OTClient, Canary)
- **Identifique tipo de tarefa** (otimização, nova feature, bug fix, documentação)
- **Determine complexidade** e duração estimada
- **Selecione agentes apropriados** automaticamente
- **Crie workflow otimizado** para a tarefa

---

## 🔄 Workflow de Orquestração Inteligente

### **Fase 1: Análise de Contexto**
```python
# Análise automática do pedido
def analyze_context(user_request):
    # Detecta palavras-chave
    # Identifica tecnologias
    # Determina tipo de tarefa
    # Avalia complexidade
    return context_analysis
```

### **Fase 2: Seleção de Agentes**
```python
# Seleção automática de agentes
def select_agents(context):
    # Mapeia contexto para agentes
    # Determina ordem de execução
    # Define responsabilidades
    return agent_workflow
```

### **Fase 3: Execução Coordenada**
```python
# Execução automática do workflow
def execute_workflow(agent_workflow):
    # Executa agentes em sequência
    # Coordena transferências
    # Monitora progresso
    return execution_results
```

### **Fase 4: Relatório Inteligente**
```python
# Relatório automático de progresso
def report_progress(execution_results):
    # Mostra progresso em tempo real
    # Indica próximos passos
    # Reporta conclusões
    return progress_report
```

---

## 🎯 Mapeamento de Contexto para Agentes

### **🛠️ Tecnologias C++ (Engine Development)**
- **Palavras-chave**: C++, performance, memory, renderização, OpenGL, ASIO, VCPKG
- **Agentes**: Engine Developer (Zara)
- **Workflow**: Performance Optimization, Core Development

### **📝 Tecnologias Lua (Content Creation)**
- **Palavras-chave**: Lua, módulos, OTUI, scripts, interface, conteúdo
- **Agentes**: Content Creator (Maya)
- **Workflow**: Content Pipeline, Module Development

### **🎮 Game Design (Sistemas de Jogo)**
- **Palavras-chave**: sistema, feature, mecânica, gameplay, design
- **Agentes**: Game Designer (Alex)
- **Workflow**: Feature Development

### **🧪 Quality Assurance (Testes)**
- **Palavras-chave**: teste, bug, erro, validação, qualidade
- **Agentes**: QA Tester (Sam)
- **Workflow**: Bug Fix, Quality Assurance

### **🚀 DevOps (Deploy e Infraestrutura)**
- **Palavras-chave**: deploy, build, CI/CD, infraestrutura, produção
- **Agentes**: DevOps Engineer (Jordan)
- **Workflow**: Deployment, Infrastructure

### **🎨 Level Design (Interface e UX)**
- **Palavras-chave**: interface, UX, UI, design, layout, experiência
- **Agentes**: Level Designer (Riley)
- **Workflow**: Interface Design, UX Optimization

### **🔧 Operações Git (Controle de Versão)**
- **Palavras-chave**: git, commit, push, arrumar, fix, automatizar, "arrumar commits", "fix commits"
- **Agentes**: Git Automation Agent
- **Workflow**: Git Operations, Commit Automation, Version Control
- **Agentes**: Level Designer (Casey)
- **Workflow**: UI/UX Design

### **🎯 Orquestração Geral**
- **Palavras-chave**: coordenar, gerenciar, workflow, projeto, equipe
- **Agentes**: Game Team Orchestrator (Riley)
- **Workflow**: Project Management

---

## 🔍 Detecção Automática de Contexto

### **📊 Análise de Palavras-Chave**
```python
# Mapeamento de palavras-chave para contextos
CONTEXT_KEYWORDS = {
    "performance": ["engine_developer", "performance_optimization"],
    "otimização": ["engine_developer", "performance_optimization"],
    "memory": ["engine_developer", "memory_management"],
    "C++": ["engine_developer", "core_development"],
    "Lua": ["content_creator", "module_development"],
    "módulo": ["content_creator", "module_development"],
    "OTUI": ["content_creator", "ui_development"],
    "sistema": ["game_designer", "feature_development"],
    "feature": ["game_designer", "feature_development"],
    "teste": ["qa_tester", "quality_assurance"],
    "bug": ["qa_tester", "bug_fix"],
    "deploy": ["devops_engineer", "deployment"],
    "interface": ["level_designer", "ui_design"],
    "UX": ["level_designer", "ux_design"],
    "coordenar": ["game_team_orchestrator", "project_management"]
}
```

### **🎯 Detecção de Complexidade**
```python
# Análise de complexidade baseada no contexto
def analyze_complexity(context):
    if "otimização" in context and "performance" in context:
        return "high"  # Requer múltiplos agentes
    elif "módulo" in context and "Lua" in context:
        return "medium"  # Requer Content Creator
    elif "bug" in context:
        return "low"  # Requer QA Tester
    return "medium"
```

---

## 🚀 Workflows Automáticos

### **⚡ Performance Optimization Workflow**
```python
# Workflow automático para otimização
def performance_optimization_workflow():
    return {
        "agents": ["engine_developer", "content_creator", "qa_tester"],
        "phases": [
            "analysis",      # Engine Developer analisa código
            "optimization",  # Engine Developer otimiza C++
            "integration",   # Content Creator cria módulos Lua
            "testing"        # QA Tester valida melhorias
        ],
        "estimated_duration": "2-3 hours"
    }
```

### **🎮 Feature Development Workflow**
```python
# Workflow automático para novas features
def feature_development_workflow():
    return {
        "agents": ["game_designer", "engine_developer", "content_creator", "qa_tester"],
        "phases": [
            "design",        # Game Designer cria design
            "implementation", # Engine Developer implementa core
            "content",       # Content Creator cria conteúdo
            "testing"        # QA Tester testa feature
        ],
        "estimated_duration": "4-6 hours"
    }
```

### **🐛 Bug Fix Workflow**
```python
# Workflow automático para correção de bugs
def bug_fix_workflow():
    return {
        "agents": ["qa_tester", "engine_developer", "content_creator"],
        "phases": [
            "identification", # QA Tester identifica bug
            "fix",           # Engine Developer/Content Creator corrige
            "validation"     # QA Tester valida correção
        ],
        "estimated_duration": "1-2 hours"
    }
```

---

## 📊 Sistema de Relatórios Inteligentes

### **🔄 Relatório em Tempo Real**
```python
# Template de relatório automático
def generate_progress_report(workflow_status):
    return f"""
🤖 **Orquestração Inteligente Ativa**
🎯 **Tarefa**: {workflow_status.task}
⏱️ **Progresso**: {workflow_status.progress}%
👥 **Agentes Ativos**: {workflow_status.active_agents}
📋 **Próximo Passo**: {workflow_status.next_step}
⏰ **Tempo Estimado**: {workflow_status.estimated_time}
"""
```

### **📈 Métricas de Performance**
```python
# Métricas automáticas de workflow
def track_workflow_metrics(workflow):
    return {
        "execution_time": workflow.duration,
        "agents_used": len(workflow.agents),
        "success_rate": workflow.success_rate,
        "efficiency_score": workflow.efficiency
    }
```

---

## 🎯 Regras de Execução

### **🔄 Execução Automática**
- **SEMPRE execute** workflows automaticamente quando contexto for detectado
- **SEMPRE coordene** transferências entre agentes
- **SEMPRE monitore** progresso em tempo real
- **SEMPRE reporte** status e próximos passos
- **SEMPRE sugira** melhorias e otimizações

### **🧠 Adaptação Inteligente**
- **SEMPRE aprenda** com execuções anteriores
- **SEMPRE otimize** workflows baseado em feedback
- **SEMPRE ajuste** seleção de agentes baseado em resultados
- **SEMPRE melhore** detecção de contexto
- **SEMPRE refine** mapeamento de palavras-chave

### **📊 Validação e Qualidade**
- **SEMPRE valide** resultados de cada agente
- **SEMPRE verifique** qualidade do output
- **SEMPRE confirme** conclusão de cada fase
- **SEMPRE documente** aprendizados e melhorias
- **SEMPRE atualize** workflows baseado em feedback

---

## 🔧 Integração com Sistema Existente

### **📋 Atualização de cursor.md**
- **SEMPRE mantenha** referência a esta regra no cursor.md
- **SEMPRE atualize** seção "Como Funciona" com orquestração inteligente
- **SEMPRE integre** com regras existentes
- **SEMPRE mantenha** compatibilidade com comandos manuais (fallback)

### **🗺️ Integração com Mapas JSON**
- **SEMPRE atualize** mapas BMAD com workflows automáticos
- **SEMPRE registre** execuções bem-sucedidas
- **SEMPRE documente** aprendizados nos mapas
- **SEMPRE mantenha** sincronização com sistema existente

---

## 🎉 Benefícios Esperados

### **⚡ Eficiência**
- **Eliminação** de comandos manuais
- **Automação** completa de workflows
- **Redução** de tempo de execução
- **Otimização** de recursos

### **🧠 Inteligência**
- **Detecção automática** de contexto
- **Seleção inteligente** de agentes
- **Coordenação automática** de workflows
- **Aprendizado contínuo** do sistema

### **📊 Transparência**
- **Relatórios em tempo real** de progresso
- **Visibilidade completa** de workflows
- **Métricas de performance** automáticas
- **Feedback contínuo** para melhorias

---

## 🔄 Atualização Automática

### **📝 Para Novos Contextos**
Quando novos contextos forem identificados:
- ✅ Adicionar palavras-chave ao mapeamento
- ✅ Criar workflow específico
- ✅ Atualizar regras de detecção
- ✅ Testar e validar funcionamento

### **🛠️ Para Novos Agentes**
Quando novos agentes forem adicionados:
- ✅ Integrar ao sistema de seleção
- ✅ Definir especializações
- ✅ Criar workflows específicos
- ✅ Atualizar mapeamento de contexto 