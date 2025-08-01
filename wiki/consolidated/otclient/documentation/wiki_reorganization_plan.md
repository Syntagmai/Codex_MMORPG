---
tags: [wiki_reorganization, obsidian_vault, structure_plan, documentation]
type: reorganization_plan
status: active
priority: critical
created: 2025-01-27
updated: 2025-01-27
---

# 📁 Plano de Reorganização da Wiki - Transformar docs/ em Cofre Obsidian

## 🎯 **Objetivo da Reorganização**

Transformar a pasta `wiki/docs/` em um **cofre Obsidian completo** que contenha toda a documentação organizada de forma lógica, incluindo:
- **OTClient**: Documentação completa do cliente
- **Canary**: Documentação completa do servidor  
- **Cursos e Lições**: Material educacional
- **Laboratório**: Testes e experimentos
- **Templates**: Modelos reutilizáveis

## 📊 **Estrutura Atual vs Estrutura Proposta**

### **📁 Estrutura Atual (Problemática):**
```
wiki/
├── otclient/ (documentação OTClient)
├── canary/ (documentação Canary)
├── docs/ (cursos e lições)
├── teste/ (laboratório)
├── habdel/ (stories de pesquisa)
├── dashboard/ (sistema de tarefas)
├── bmad/ (sistema de agentes)
├── integration/ (integração)
├── tools/ (ferramentas)
├── maps/ (mapas JSON)
├── log/ (logs)
└── update/ (scripts)
```

### **📁 Estrutura Proposta (Cofre Obsidian):**
```
wiki/docs/ (COFRE OBSIDIAN)
├── 📚 otclient/
│   ├── 📖 guides/ (guias práticos)
│   ├── 📋 api/ (referência da API)
│   ├── 🎨 ui/ (sistema de interface)
│   ├── 🔧 development/ (desenvolvimento)
│   ├── 📊 performance/ (otimização)
│   └── 🐛 debugging/ (depuração)
├── 🗄️ canary/
│   ├── 📖 guides/ (guias práticos)
│   ├── 📋 api/ (referência da API)
│   ├── 🏗️ architecture/ (arquitetura)
│   ├── 🔧 development/ (desenvolvimento)
│   ├── 📊 performance/ (otimização)
│   └── 🐛 debugging/ (depuração)
├── 🎓 courses/
│   ├── 📚 beginner/ (iniciante)
│   ├── 📚 intermediate/ (intermediário)
│   ├── 📚 advanced/ (avançado)
│   └── 📚 expert/ (especialista)
├── 📝 lessons/
│   ├── 🎯 practical/ (práticas)
│   ├── 🧠 theoretical/ (teóricas)
│   └── 🔬 experimental/ (experimentais)
├── 🧪 laboratory/
│   ├── 🔬 experiments/ (experimentos)
│   ├── 🧪 tests/ (testes)
│   ├── 📊 analysis/ (análises)
│   └── 📈 results/ (resultados)
├── 📋 templates/
│   ├── 📄 documentation/ (documentação)
│   ├── 🎯 guides/ (guias)
│   ├── 📊 reports/ (relatórios)
│   └── 🔧 development/ (desenvolvimento)
├── 🔗 integration/
│   ├── 📋 protocols/ (protocolos)
│   ├── 🔄 workflows/ (fluxos de trabalho)
│   ├── 📊 comparisons/ (comparações)
│   └── 🎯 best_practices/ (melhores práticas)
├── 📊 research/
│   ├── 📋 habdel/ (stories de pesquisa)
│   ├── 📈 analysis/ (análises)
│   └── 📊 reports/ (relatórios)
└── 🎯 dashboard/
    ├── 📋 tasks/ (tarefas)
    ├── 📊 metrics/ (métricas)
    └── 📈 progress/ (progresso)
```

## 🔄 **Plano de Migração**

### **📋 Fase 1: Preparação (Imediato)**
1. **Criar estrutura base** em `wiki/docs/`
2. **Mover documentação OTClient** para `wiki/docs/otclient/`
3. **Mover documentação Canary** para `wiki/docs/canary/`
4. **Mover cursos e lições** para `wiki/docs/courses/` e `wiki/docs/lessons/`
5. **Mover laboratório** para `wiki/docs/laboratory/`

### **📋 Fase 2: Organização (Curto Prazo)**
1. **Categorizar arquivos** por tipo e função
2. **Criar índices** de navegação
3. **Estabelecer links** entre documentos
4. **Padronizar nomenclatura** de arquivos

### **📋 Fase 3: Integração (Médio Prazo)**
1. **Configurar Obsidian** para a pasta `wiki/docs/`
2. **Implementar plugins** necessários
3. **Configurar templates** automáticos
4. **Estabelecer workflows** de documentação

### **📋 Fase 4: Otimização (Longo Prazo)**
1. **Implementar automação** de documentação
2. **Criar sistema de busca** avançado
3. **Estabelecer versionamento** de documentação
4. **Implementar colaboração** em tempo real

## 📁 **Detalhamento da Nova Estrutura**

### **📚 OTClient Documentation (`wiki/docs/otclient/`)**

#### **📖 Guides/ (Guias Práticos)**
- `getting_started.md` - Guia de início rápido
- `installation.md` - Guia de instalação
- `configuration.md` - Guia de configuração
- `module_development.md` - Desenvolvimento de módulos
- `ui_development.md` - Desenvolvimento de interface
- `performance_optimization.md` - Otimização de performance
- `debugging_guide.md` - Guia de depuração

#### **📋 API/ (Referência da API)**
- `lua_api_reference.md` - Referência da API Lua
- `cpp_api_reference.md` - Referência da API C++
- `protocol_reference.md` - Referência de protocolos
- `network_api.md` - API de rede

#### **🎨 UI/ (Sistema de Interface)**
- `ui_system_guide.md` - Guia do sistema de UI
- `otui_development.md` - Desenvolvimento OTUI
- `animation_system.md` - Sistema de animações
- `effects_system.md` - Sistema de efeitos
- `sound_system.md` - Sistema de som

#### **🔧 Development/ (Desenvolvimento)**
- `module_system.md` - Sistema de módulos
- `protocol_system.md` - Sistema de protocolos
- `network_system.md` - Sistema de rede
- `graphics_system.md` - Sistema de gráficos
- `world_system.md` - Sistema de mundo

### **🗄️ Canary Documentation (`wiki/docs/canary/`)**

#### **📖 Guides/ (Guias Práticos)**
- `getting_started.md` - Guia de início rápido
- `installation.md` - Guia de instalação
- `configuration.md` - Guia de configuração
- `server_development.md` - Desenvolvimento de servidor
- `database_management.md` - Gerenciamento de banco de dados
- `performance_optimization.md` - Otimização de performance

#### **📋 API/ (Referência da API)**
- `lua_api_reference.md` - Referência da API Lua
- `cpp_api_reference.md` - Referência da API C++
- `database_api.md` - API de banco de dados
- `network_api.md` - API de rede

#### **🏗️ Architecture/ (Arquitetura)**
- `architecture_overview.md` - Visão geral da arquitetura
- `core_systems.md` - Sistemas principais
- `data_flow.md` - Fluxo de dados
- `security_model.md` - Modelo de segurança

### **🎓 Courses/ (Cursos)**

#### **📚 Beginner/ (Iniciante)**
- `introduction_to_mmorpg.md` - Introdução a MMORPGs
- `basic_concepts.md` - Conceitos básicos
- `first_steps.md` - Primeiros passos

#### **📚 Intermediate/ (Intermediário)**
- `advanced_concepts.md` - Conceitos avançados
- `development_practices.md` - Práticas de desenvolvimento
- `optimization_techniques.md` - Técnicas de otimização

#### **📚 Advanced/ (Avançado)**
- `expert_techniques.md` - Técnicas especializadas
- `architecture_design.md` - Design de arquitetura
- `performance_tuning.md` - Ajuste de performance

### **🧪 Laboratory/ (Laboratório)**

#### **🔬 Experiments/ (Experimentos)**
- `performance_tests.md` - Testes de performance
- `integration_tests.md` - Testes de integração
- `stress_tests.md` - Testes de estresse

#### **🧪 Tests/ (Testes)**
- `unit_tests.md` - Testes unitários
- `integration_tests.md` - Testes de integração
- `end_to_end_tests.md` - Testes end-to-end

## 🔧 **Configuração do Obsidian**

### **📋 Plugins Recomendados:**
- **Graph View**: Visualização de relacionamentos
- **Calendar**: Controle de datas
- **Templates**: Templates automáticos
- **Tag Wrangler**: Gerenciamento de tags
- **Advanced Tables**: Tabelas avançadas
- **Code Block Enhancer**: Melhorias em blocos de código
- **Git**: Integração com Git
- **Obsidian Git**: Sincronização Git

### **🎨 Temas Recomendados:**
- **Minimal**: Tema limpo e minimalista
- **Obsidianite**: Tema escuro profissional
- **ITS Theme**: Tema com foco em produtividade

### **📋 Configurações Específicas:**
- **Vault Name**: "Codex MMORPG Documentation"
- **Default Location**: `wiki/docs/`
- **Attachment Folder**: `attachments/`
- **Template Folder**: `templates/`
- **Daily Note Folder**: `daily_notes/`

## 📊 **Benefícios da Reorganização**

### **✅ Para Desenvolvimento:**
- **Navegação intuitiva** entre documentação
- **Busca eficiente** em todo o cofre
- **Links automáticos** entre documentos relacionados
- **Versionamento** integrado com Git

### **✅ Para Aprendizado:**
- **Cursos estruturados** por nível
- **Lições práticas** com exemplos
- **Laboratório** para experimentos
- **Templates** para padronização

### **✅ Para Colaboração:**
- **Documentação centralizada** em um local
- **Padrões consistentes** de documentação
- **Workflows** automatizados
- **Controle de versão** integrado

## 🎯 **Próximos Passos**

### **Imediato (Hoje):**
1. ✅ **Criar plano** de reorganização
2. **Aprovar estrutura** proposta
3. **Iniciar migração** dos arquivos

### **Curto Prazo (Esta Semana):**
1. **Migrar documentação** OTClient e Canary
2. **Organizar cursos** e lições
3. **Configurar laboratório**
4. **Estabelecer templates**

### **Médio Prazo (Próximo Mês):**
1. **Configurar Obsidian** completamente
2. **Implementar automação**
3. **Criar workflows** de documentação
4. **Estabelecer padrões** de colaboração

---

**Plano de Reorganização**: ✅ **CRIADO**  
**Status**: 🟡 **AGUARDANDO APROVAÇÃO**  
**Próximo**: 🎯 **Iniciar migração dos arquivos** 