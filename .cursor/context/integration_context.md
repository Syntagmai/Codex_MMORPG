# Contexto: Integração Cross-Project

Este arquivo contém as regras e diretrizes para a integração entre projetos, especialmente a preparação para integração total entre OTClient e Canary.

---

## 🔗 Integração Cross-Project

### **Foco Principal:**
- **@integration** - Foco na preparação para integração total (Canary como futuro)
- Preparação para integração total com ecossistema completo do jogo
- Análise completa disponível para ambos os projetos (OTClient e Canary)

### **Status Atual:**
- **OTClient**: Análise completa (código + documentação) - submódulo ativo
- **Canary**: Análise completa (código + documentação) - submódulo ativo  
- **Integração**: Ativa e disponível para desenvolvimento

---

## 🎯 Regras de Integração

- **Prepare estrutura** para integração total com Canary
- **Documente protocolos** compartilhados (OpenCode, ExtendedOpen)
- **Crie templates** para documentação futura do Canary
- **Estabeleça padrões** de comunicação cliente-servidor
- **Referencie** documentação externa do Canary quando disponível

### **Análise de Compatibilidade:**
- **Análise de código OTClient**: `data/maps/otclient_source_index.json` → `otclient/src/` → `otclient/modules/` → `docs/systems/`
- **Análise de código Canary**: `data/maps/canary_source_index.json` → `canary/src/` → `canary/data/` → `docs/systems/`

---

## 📋 Sistema de Tarefas de Integração

### **Integrated Task Manager:**
- **Sistema de integração** OTClient-Canary em `docs/dashboard/integrated_task_manager.md`
- **15 tasks de integração** (86.7% completas)
- **Foco em preparação** para integração total

### **Fases de Integração:**
- ✅ **Fase 1**: Preparação (100% completa)
- ✅ **Fase 2**: Otimização (100% completa)  
- ✅ **Fase 3**: Agentes (100% completa)
- ✅ **Fase 4**: Documentação (100% completa)
- 🔄 **Fase 5**: Testes (0% - pendente)

---

## 🏛️ Estrutura de Submódulos para Integração

```
🔧 otclient/ (SUBMÓDULO - CLIENTE)
├── 🔧 src/ (código-fonte do cliente)
├── 📦 modules/ (módulos Lua)
├── 📁 data/ (recursos do cliente)
└── 📚 docs/ (documentação do cliente)

🖥️ canary/ (SUBMÓDULO - SERVIDOR) 
├── 🔧 src/ (código-fonte do servidor)
├── 📁 data/ (dados do servidor)
├── 🗄️ schema.sql (esquema do banco)
└── 📚 docs/ (documentação do servidor)

🗺️ forgottenmapeditor/ (SUBMÓDULO - EDITOR DE MAPA)
├── 🔧 modules/ (módulos do editor)
├── 📁 data/ (dados do editor)  
└── 📚 docs/ (documentação do editor)
```

---

## 📚 Referências Completas

Para detalhes completos sobre integração, consulte:
- `@.cursor/rules/cross-project-integration-rules.md`
- `@docs/dashboard/integrated_task_manager.md`
- `@data/maps/otclient_source_index.json`
- `@data/maps/canary_source_index.json`
