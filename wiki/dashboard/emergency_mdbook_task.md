---
tags: [emergency_task, mdbook, obsidian, documentation, github_pages]
type: emergency_task
status: active
priority: critical
created: 2025-01-27
updated: 2025-01-27
---

# 🚨 Task Emergencial: Sistema mdBook + Obsidian

## 🎯 **Objetivo da Task**

Implementar um **sistema duplo de documentação** que combine:
- **📚 Obsidian** (uso pessoal/desenvolvimento)
- **📖 mdBook** (publicação/GitHub Pages)

## 📋 **Estrutura a Ser Criada**

```
📁 wiki/docs/ (COFRE OBSIDIAN)
├── 📖 otclient/
├── 🗄️ canary/
├── 🎓 courses/
├── 🧪 laboratory/
└── 📊 research/

📁 docs/ (SISTEMA MDBOOK)
├── 📋 book.toml
├── 📖 SUMMARY.md
├── 📖 src/
│   ├── 📖 otclient/
│   ├── 🗄️ canary/
│   ├── 🎓 courses/
│   └── 🧪 laboratory/
└── 📊 book/ (gerado automaticamente)

📁 scripts/
├── 🔄 obsidian_to_mdbook.py
├── 🔄 mdbook_builder.py
└── 🔄 link_converter.py

📁 .github/workflows/
└── 📋 deploy-book.yml
```

## 🚀 **Plano de Execução**

### **📋 Fase 1: Estrutura Base (Imediato)**
1. **Criar pasta `docs/`** na raiz do projeto
2. **Configurar `book.toml`** para mdBook
3. **Criar `SUMMARY.md`** com estrutura completa
4. **Organizar pastas** em `docs/src/`

### **📋 Fase 2: Scripts de Conversão (Curto Prazo)**
1. **Desenvolver `obsidian_to_mdbook.py`**
2. **Implementar conversão de links** `[[...]]` → `[...]()`
3. **Converter callouts** do Obsidian para HTML
4. **Manter estrutura hierárquica**

### **📋 Fase 3: Automação GitHub (Médio Prazo)**
1. **Configurar GitHub Actions**
2. **Implementar deploy automático**
3. **Configurar GitHub Pages**
4. **Testar workflow completo**

## 🎯 **Critérios de Sucesso**

### **✅ Estrutura Completa**
- [ ] Pasta `docs/` criada e configurada
- [ ] `book.toml` configurado corretamente
- [ ] `SUMMARY.md` com estrutura completa
- [ ] Pastas organizadas em `docs/src/`

### **✅ Scripts Funcionais**
- [ ] `obsidian_to_mdbook.py` converte arquivos
- [ ] Links internos convertidos corretamente
- [ ] Callouts convertidos para HTML
- [ ] Estrutura hierárquica mantida

### **✅ Automação GitHub**
- [ ] GitHub Actions configurado
- [ ] Deploy automático funcionando
- [ ] GitHub Pages ativo
- [ ] Workflow testado e validado

## 📊 **Métricas de Progresso**

- **Estrutura**: 0% → 100%
- **Scripts**: 0% → 100%
- **Automação**: 0% → 100%
- **Testes**: 0% → 100%

## 🎯 **Status Atual**

**Status**: 🚨 **EMERGÊNCIA ATIVA**  
**Próximo**: 🎯 **Criar estrutura base do mdBook** 