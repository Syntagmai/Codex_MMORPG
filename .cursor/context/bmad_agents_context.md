# Contexto: Sistema de Agentes BMAD

Este arquivo contém as regras e informações sobre o sistema de agentes BMAD (Behavior-Modular Agent Development), orquestração inteligente e especialização de agentes para tarefas complexas.

---

## 🤖 Sistema de Agentes BMAD

### **Contextos de Agentes Disponíveis:**
- **@bmad** - Sistema de agentes BMAD (desenvolvimento permitido)
- Agentes especializados disponíveis para desenvolvimento
- Orquestração automática baseada no contexto do pedido

### **Workflow BMAD:**
`data/maps/bmad_agents.json` → `data/maps/bmad_workflows.json` → `docs/bmad/` → `docs/bmad/bmad_rules.md`

---

## 🎯 Regras do Sistema BMAD

- **Use agentes especializados** para tarefas específicas quando apropriado
- **Coordene workflows** entre agentes para tarefas complexas
- **Use templates** padronizados para documentação
- **Mantenha especialização** de cada agente
- **Integre** com sistema de mapas JSON

---

## 🤖 Orquestração Inteligente Automática

- **Analise contexto** do pedido do usuário automaticamente
- **Identifique agentes necessários** baseado no contexto detectado
- **Coordene workflow completo** sem intervenção manual
- **Reporte progresso** em tempo real
- **Sugira próximos passos** automaticamente

### **Detecção Automática:**
- **Detecte tecnologias** mencionadas (C++, Lua, OTClient, Canary)
- **Identifique tipo de tarefa** (otimização, nova feature, bug fix, documentação)
- **Determine complexidade** e duração estimada
- **Selecione agentes apropriados** automaticamente
- **Crie workflow otimizado** para a tarefa específica

---

## 🔧 Agentes Especializados Disponíveis

### **Python Agent**
- Especializado em desenvolvimento e qualidade Python
- Resolução automática de erros em scripts
- Execução de scripts com fallback automático

### **Agentes AAA (Nível Especialização Máxima)**
- Agentes de nível AAA para tarefas críticas
- Especialização em diferentes áreas do desenvolvimento

### **Agent Organization**
- Organização automática de agentes na estrutura BMAD
- Coordenação entre múltiplos agentes

---

## 📚 Referências Completas

Para detalhes completos sobre agentes BMAD, consulte:
- `@.cursor/rules/bmad-system-rules.md`
- `@.cursor/rules/intelligent-orchestration-rules.md`
- `@.cursor/rules/python-agent-rules.md`
- `@.cursor/rules/aaa-agent-specialization-rules.md`
- `@.cursor/rules/agent-organization-rules.md`
- `@.cursor/rules/auto-learning-rules.md`
