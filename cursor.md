# Comportamento do Assistente

## 🚀 **ÍNDICE DE NAVEGAÇÃO RÁPIDA**

### **🎯 Contextos Principais:**
- **@otclient** → Desenvolvimento do cliente OTClient
- **@bmad** → Sistema de agentes BMAD  
- **@wiki** → Documentação da wiki
- **@integration** → Integração entre projetos

### **⚡ Ações Rápidas:**
- **🎯 Dashboard** → `wiki/dashboard/integrated_task_manager.md` (Sistema Central)
- **📋 Regras** → `.cursor/rules/` (26 arquivos)
- **🗺️ Mapas** → `wiki/maps/` (15 arquivos JSON)
- **📚 Wiki** → `wiki/` (documentação estruturada)
- **🔧 Código** → `src/` (código-fonte - somente leitura)
- **🐍 Scripts** → `wiki/update/` (scripts Python com resolução automática)

### **🎯 Hierarquia de Prioridades:**
1. **CRÍTICO**: Dashboard Central, Simplificação, Contexto, Permissões, Resolução de Erros
2. **IMPORTANTE**: Task Management, Token Optimization, JSON Navigation, File Organization
3. **OPCIONAL**: BMAD Agents, Auto-Learning, Cross-Project Integration

### **🧭 Padrões de Navegação:**
- **Dashboard Central**: `cursor.md` → `integrated_task_manager.md` → Sistema Completo
- **Análise de código**: `otclient_source_index.json` → `src/` → `modules/` → `wiki/otclient/`
- **Busca de documentação**: `tags_index.json` → `wiki_map.json` → `wiki/` → `relationships.json`
- **Navegação por grafos**: `navigation_graph.json` → Caminhos ótimos → Cache inteligente → Sugestões contextuais
- **Consulta de regras**: `cursor.md` → `.cursor/rules/` → `enhanced_context_system.json`
- **Workflow BMAD**: `bmad_agents.json` → `bmad_workflows.json` → `wiki/bmad/` → `bmad_rules.md`
- **Execução de scripts**: `cursor.md` → `script_execution_manager.py` → `python_error_resolver.py` → script.py

---

## ⚠️ **LIMITAÇÕES CRÍTICAS DO SISTEMA**

### 🚨 **CONTEXTO IMPORTANTE - SUBMÓDULOS COMO FONTES DE VERDADE**

**Este repositório (`otclient_doc`) contém:**
- ✅ **Submódulos Git**: `otclient/` e `canary/` (fontes de verdade imutáveis)
- ✅ **Documentação e automação**: `wiki/`, `.cursor/`, `bmad/` (editáveis)
- ✅ **Sistema de agentes**: BMAD para orquestração e automação

**IMPORTANTE:**
- ❌ **NUNCA editar** arquivos dentro de `otclient/` ou `canary/` por este repositório
- ❌ **NUNCA modificar** código-fonte dos submódulos
- ✅ **APENAS documentação, automação e orquestração** são editáveis

### 📁 **Estrutura Real dos Repositórios**

```
📁 otclient_doc/ (REPOSITÓRIO PRINCIPAL - BMAD Agent)
├── 📚 wiki/ (documentação e automação - editável)
├── 🤖 bmad/ (sistema de agentes - editável)
├── 📘 .cursor/ (regras e configurações - editável)
├── 📦 otclient/ (SUBMÓDULO - fonte de verdade imutável)
│   ├── 🔧 src/ (código OTClient)
│   ├── 📦 modules/ (módulos Lua OTClient)
│   └── 📁 data/ (recursos OTClient)
└── 🗄️ canary/ (SUBMÓDULO - fonte de verdade imutável)
    ├── 🔧 src/ (código Canary)
    ├── 📦 modules/ (módulos Canary)
    └── 📁 data/ (recursos Canary)
```

### 🎯 **O que É Possível Fazer**

✅ **Análise completa do código** dos submódulos (somente leitura)
✅ **Documentação da wiki** baseada nos submódulos
✅ **Desenvolvimento de agentes BMAD** para automação
✅ **Orquestração e integração** entre OTClient e Canary
✅ **Criação de templates** e workflows
✅ **Análise e documentação** cruzada

### ❌ **O que NÃO É Possível Fazer**

❌ **Modificar código-fonte** dos submódulos
❌ **Editar arquivos** dentro de `otclient/` ou `canary/`
❌ **Alterar estrutura** dos submódulos
❌ **Commits diretos** nos submódulos

### 🔄 **Estratégia de Integração Total**

1. **Foco Principal**: Documentação, automação e orquestração
2. **Submódulos**: Fontes de verdade imutáveis
3. **Agentes BMAD**: Análise e documentação automática
4. **Workflows**: Integração e validação cruzada
5. **Templates**: Para documentação e automação
6. **Protocolos**: Documentação de interfaces compartilhadas

---

## 📋 Orquestrador de Regras

Este arquivo atua como **orquestrador** que referencia a **coletânea de regras** definidas na pasta:

📘 `.cursor/rules/`

---

## 🎯 Estrutura de Regras

### 📘 **Arquivos de Regras Disponíveis**

| Arquivo | Propósito | Status |
|---------|-----------|--------|
| `rules.md` | **Regras principais** de escopo e modificação | ✅ Ativo |
| `template.md` | **Template** para criar novas regras | ✅ Ativo |
| `documentation-rules.md` | **Regras de documentação** e formatação | ✅ Ativo |
| `wiki-rules.md` | **Regras específicas** para pasta wiki | ✅ Ativo |
| `prompt-engineering-rules.md` | **Regras de otimização automática** de prompts | ✅ Ativo |
| `enhanced-prompt-engineering-rules.md` | **Regras avançadas de engenharia** de prompts | ✅ Ativo |
| `wiki-json-navigation-rules.md` | **Regras de navegação JSON** para wiki | ✅ Ativo |
| `otclient-source-index-rules.md` | **Regras de indexação** do código-fonte | ✅ Ativo |
| `system-rules.md` | **Regras do sistema** de regras | ✅ Ativo |
| `auto-update-maps-rules.md` | **Regras de atualização automática** de mapas | ✅ Ativo |
| `file-organization-rules.md` | **Regras de organização** de arquivos | ✅ Ativo |
| `token-optimization-rules.md` | **Regras de otimização** de tokens | ✅ Ativo |
| `wiki-comprehensive-rules.md` | **Regras para wiki abrangente** e completa | ✅ Ativo |
| `cross-project-integration-rules.md` | **Regras de integração** entre OTClient e Canary | ✅ Ativo |
| `context-aware-rules.md` | **Regras de contexto inteligente** e detecção automática | ✅ Ativo |
| `bmad-system-rules.md` | **Regras do sistema BMAD** e agentes especializados | ✅ Ativo |
| `intelligent-orchestration-rules.md` | **Regras de orquestração inteligente** automática | ✅ Ativo |
| `report-cleanup-rules.md` | **Regras de limpeza** e organização de relatórios | ✅ Ativo |
| `task-automation-rules.md` | **Regras de automação** de tarefas e execução passo a passo | ✅ Ativo |
| `python-agent-rules.md` | **Regras do agente Python** especializado em desenvolvimento e qualidade | ✅ Ativo |
| `agent-organization-rules.md` | **Regras de organização automática** de agentes na estrutura BMAD | ✅ Ativo |
| `auto-learning-rules.md` | **Regras do sistema de auto aprendizado** BMAD | ✅ Ativo |
| `git-automation-rules.md` | **Regras de automação Git** e boas práticas | ✅ Ativo |
| `simplification-rules.md` | **Regras de simplificação** para evitar loops e travamentos | ✅ Ativo |
| `performance-rules.md` | **Regras de performance** e otimização do sistema | ✅ Ativo |
| `aaa-agent-specialization-rules.md` | **Regras de agentes especializados** de nível AAA | ✅ Ativo |
| `code-cleanup-rules.md` | **Regras de code cleanup** e organização automática | ✅ Ativo |
| `enhanced-context-system.json` | **Sistema de contexto avançado** e navegação inteligente | ✅ Ativo |
| `intelligent-navigation.json` | **Navegação inteligente** e padrões de acesso | ✅ Ativo |
| `integrated-task-management-rules.md` | **Regras do sistema integrado** de task management | ✅ Ativo |
| `git-task-manager-integration-rules.md` | **Regras de integração** Git-Task Manager | ✅ Ativo |
| `log-organization-rules.md` | **Regras de organização** de logs e arquivos de log | ✅ Ativo |
| `wiki-log-organization-rules.md` | **Regras de organização** da pasta wiki/log/ | ✅ Ativo |

### 📁 **Contexto das Pastas do Projeto**

| Pasta/Arquivo | Propósito | Permissões |
|---------------|-----------|------------|
| `wiki/` | **Documentação estruturada** da wiki do OTClient | ✅ Modificação permitida |
| `.cursor/` | **Regras e configurações** do assistente | ✅ Modificação permitida |
| `.cursor/rules/` | **Regras específicas** e templates do assistente | ✅ Modificação permitida |
| `cursor.md` | **Arquivo orquestrador** das regras | ✅ Modificação permitida |
| `git-task-manager-integration-rules.md` | **Regras de integração** Git-Task Manager | ✅ Modificação permitida |
| **TODOS OS OUTROS** | **Código-fonte, recursos e configurações** do OTClient | ❌ Apenas leitura |

> [!warning] **LIMITAÇÃO IMPORTANTE**
> Este repositório contém **APENAS** o código-fonte do OTClient. O código-fonte do Canary **NÃO está disponível** para análise ou modificação.

### 🗺️ **Mapa Visual da Estrutura**

```
📁 otclient_doc/
├── 📋 cursor.md (ORQUESTRADOR PRINCIPAL)
├── 📘 .cursor/rules/ (25 regras)
│   ├── 🎯 rules.md (regras principais)
│   ├── 🧠 prompt-engineering-rules.md
│   ├── 🗺️ wiki-json-navigation-rules.md
│   ├── 🔍 otclient-source-index-rules.md
│   ├── 🤖 bmad-system-rules.md
│   └── ... (22 outras regras)
├── 📚 wiki/ (documentação)
│   ├── 🗺️ maps/ (15 arquivos JSON)
│   │   ├── tags_index.json
│   │   ├── wiki_map.json
│   │   ├── enhanced_context_system.json
│   │   └── intelligent_navigation.json
│   ├── 🤖 bmad/ (sistema de agentes)
│   ├── 📖 otclient/ (documentação do cliente)
│   └── 🔗 integration/ (integração - preparação)
├── 🔧 src/ (código-fonte OTClient - somente leitura)
├── 📦 modules/ (módulos Lua - somente leitura)
└── 📁 data/ (recursos - somente leitura)

❌ canary_repository/ (FUTURO - SERÁ COPIADO)
   ├── 🔧 src/ (código Canary - futuro)
   └── 📚 wiki/ (documentação Canary - futuro)
```

### 🎯 **Fluxo de Navegação Otimizado**

```
1. 📋 cursor.md (ENTRADA)
   ↓
2. 🎯 Dashboard Central (integrated_task_manager.md)
   ↓
3. 🎯 Detectar contexto (@otclient, @bmad, @wiki, @integration)
   ↓
4. 🗺️ Consultar mapas JSON relevantes
   ↓
5. 📚 Acessar documentação específica
   ↓
6. 🔧 Consultar código-fonte OTClient (se necessário)
   ↓
7. ✅ Executar tarefa com regras apropriadas
   ↓
8. 📈 Atualizar dashboard central
```

> [!info] **CONTEXTO DE NAVEGAÇÃO**
> - **OTClient**: Análise completa disponível (código + documentação)
> - **Canary**: Preparação para integração total (futuro)
> - **BMAD**: Sistema de agentes disponível para desenvolvimento
> - **Wiki**: Documentação OTClient disponível para modificação

> [!warning] **DEFINIÇÃO CRÍTICA de "otclient"**: OTClient se refere a QUALQUER pasta, subpasta ou arquivo solto no repositório que NÃO seja `.cursor/`, `wiki/` e `cursor.md`. Isso inclui `src/`, `modules/`, `data/`, `tools/`, `docs/`, `README.md`, `LICENSE`, `CMakeLists.txt` e QUALQUER OUTRO ARQUIVO do repositório oficial.

---

## 🔄 Como Funciona

### 🎯 **Hierarquia de Prioridades (NOVA)**

**Nível 1 - CRÍTICO (Sempre aplicar):**
1. **Simplificação** - Evitar loops infinitos
2. **Contexto** - Detectar repositório atual (OTClient apenas)
3. **Permissões** - Respeitar restrições de modificação

**Nível 2 - IMPORTANTE (Aplicar quando relevante):**
4. **Token Optimization** - Economizar tokens
5. **JSON Navigation** - Usar mapas para consultas
6. **File Organization** - Manter estrutura limpa

**Nível 3 - OPCIONAL (Aplicar se necessário):**
7. **BMAD Agents** - Para tarefas complexas
8. **Auto-Learning** - Para melhorias futuras
9. **Cross-Project Integration** - Preparação para integração total (Canary como futuro)

> [!info] **PRIORIDADE ATUALIZADA**
> Integração com Canary é considerada **futuro** para integração total, não limitação.

### 📋 **Regras de Resolução de Conflitos**

- **Se regras conflitam**: Aplicar regra de nível superior
- **Se múltiplas regras do mesmo nível**: Aplicar a mais específica
- **Se ainda houver conflito**: Usar simplificação como padrão

### 🧠 **Sistema de Contexto Avançado**

#### **Contextos Disponíveis:**
- **@otclient** - Foco no desenvolvimento do cliente (código disponível)
- **@bmad** - Foco no sistema de agentes BMAD (desenvolvimento permitido)
- **@wiki** - Foco na documentação da wiki OTClient (modificação permitida)
- **@integration** - Foco na preparação para integração total (Canary como futuro)

> [!info] **CONTEXTOS ATIVOS**
> - **@otclient**: Análise completa disponível
> - **@bmad**: Desenvolvimento de agentes permitido
> - **@wiki**: Documentação OTClient disponível
> - **@integration**: Preparação para integração total (Canary como futuro)

#### **Navegação Inteligente:**
- **Mapas JSON otimizados** para consultas rápidas
- **Cache inteligente** para arquivos frequentemente acessados
- **Detecção automática** de contexto baseada no pedido
- **Fallback automático** para modo simples em caso de problemas

> [!info] **NAVEGAÇÃO DISPONÍVEL**
> - **OTClient**: Análise completa (código + documentação)
> - **BMAD**: Desenvolvimento de agentes
> - **Wiki**: Documentação OTClient
> - **Canary**: Preparação para integração total (futuro)
> - **Git**: Automação de controle de versão

#### **Performance Otimizada:**
- **Limite de 3 níveis** de análise para evitar loops
- **Timeout de 30 segundos** para operações complexas
- **Lazy loading** de regras e mapas
- **Cache de 5 minutos** para consultas repetidas

#### **Resolução Automática de Erros:**
- **Detecção automática** de tipos de erro em scripts Python
- **Correção automática** de imports, sintaxe e encoding
- **Modo fallback** para scripts que falham
- **Log detalhado** de resoluções e estatísticas

---

1. **Este arquivo** (`cursor.md`) = Orquestrador/Referência
2. **Dashboard Central** (`integrated_task_manager.md`) = Sistema de Controle de Tasks
3. **Pasta `.cursor/rules/`** = Coletânea de regras e templates
4. **Antes de qualquer tarefa**, consulte o dashboard central e siga todas as regras relevantes
5. **Para cada prompt recebido**, aplique automaticamente as técnicas de engenharia de prompt
6. **Para consultas da wiki**, use navegação JSON: `tags_index.json` → `wiki_map.json` → `relationships.json` → markdown
7. **Para consultas do código-fonte**, use indexação JSON: `otclient_source_index.json` → código-fonte → wiki
8. **Para qualquer interação**, aplique sistema de regras: `cursor.md` → dashboard central → regras específicas → execução
9. **Atualize mapas JSON** automaticamente antes de qualquer tarefa
10. **Organize arquivos** em pastas estruturadas
11. **Otimize tokens** usando inglês para IA e português para usuário
12. **Crie wiki abrangente** integrando TODO o conteúdo do habdel
13. **Prepare integração total** com Canary para ecossistema completo do jogo
14. **Detecte contexto** automaticamente e adapte comportamento
15. **Use agentes BMAD** para especialização quando apropriado
16. **Orquestre inteligentemente** agentes automaticamente baseado no contexto do pedido
17. **Limpe e organize** arquivos temporários e relatórios na pasta log
18. **Automatize tarefas** criando tarefas temporárias, executando passo a passo e gerando relatórios finais
19. **Aprenda automaticamente** com interações passadas para melhorar detecção de contexto e otimizar workflows
20. **Aplique simplificação** para solicitações simples, evitando loops infinitos e travamentos
21. **Use resolução automática de erros** para scripts Python que falham na execução
22. **Mantenha sistema sempre limpo** usando agente de organização inteligente
23. **Organize arquivos automaticamente** por categoria e data
24. **Remova arquivos temporários** e duplicatas automaticamente
25. **Preserve conhecimento importante** em estrutura organizada
26. **Atualize dashboard central** após cada tarefa concluída
27. **Mantenha 100% de cobertura** de todas as tarefas do sistema

---

## ⚠️ Regras Principais (rules.md)

- **Nunca modifique** arquivos fora das pastas `wiki/`, `.cursor/` e `cursor.md`
- **Código-fonte** do OTClient é **imutável** sem autorização explícita
- **Sugestões** são permitidas via comentários (sem alterar código)
- **Quando mencionar "otclient"**: Refere-se a TODAS as pastas e arquivos que NÃO têm ✅ Modificação permitida
- **Canary**: Preparação para integração total (código não disponível)

> [!info] **CONTEXTO ATUALIZADO**
> O código-fonte do Canary será integrado no futuro para **integração total**. Tarefas relacionadas ao Canary focam na preparação e estrutura.

### 📁 **Referências de Pastas**

- **Quando mencionar "wiki"**: Refere-se à pasta `wiki/` do projeto
- **Quando mencionar "rules"**: Refere-se à pasta `.cursor/rules/` do projeto
- **Quando mencionar "otclient"**: Refere-se a TODAS as pastas e arquivos que NÃO têm ✅ Modificação permitida
- **Pasta wiki**: Contém documentação estruturada da wiki do OTClient
- **Pasta rules**: Contém regras e templates do assistente
- **Pastas/arquivos otclient**: Contém código-fonte, recursos e configurações do OTClient (apenas leitura)

> [!warning] **LIMITAÇÃO IMPORTANTE**
> - **OTClient**: Código-fonte disponível para análise (somente leitura)
> - **Canary**: Código-fonte será integrado no futuro
> - **Integração**: Apenas preparação e estrutura para futuro

---

## 📝 Regras de Documentação (documentation-rules.md)

- **Use formatação Obsidian** (callouts, wikilinks, frontmatter)
- **Mantenha consistência de estilo** com documentos existentes
- **Priorize exemplos práticos** e código funcional
- **Use linguagem clara e acessível**

---

## 📚 Regras da Wiki (wiki-rules.md)

- **Use extensão .md** para arquivos na pasta wiki
- **Use frontmatter obrigatório** com tags, status e aliases
- **Siga formatação Obsidian** (callouts, wikilinks, separadores)
- **Mantenha estrutura hierárquica** com índices e seções bem definidas
- **Proteção da pasta .obsidian** - NUNCA modifique arquivos em `wiki/.obsidian/` sem autorização prévia

---

## 🧠 Regras de Prompt Engineering (prompt-engineering-rules.md)

- **Analise prompts recebidos** e aplique técnicas de engenharia de prompt antes de executar
- **Use Role Prompting** para atribuir contexto específico à IA quando apropriado
- **Aplique Chain-of-Thought** para problemas complexos que requerem raciocínio passo-a-passo
- **Utilize Few-shot Prompting** quando exemplos podem melhorar a compreensão
- **Estruture a saída** quando o usuário precisa de respostas organizadas
- **Refatore prompts ambíguos** perguntando por contexto adicional quando necessário

---

## 🚀 Regras Avançadas de Prompt Engineering (enhanced-prompt-engineering-rules.md)

- **Aplique técnicas avançadas** de engenharia de prompt para otimizar interações
- **Use Meta-Prompting** para criar prompts que geram outros prompts
- **Aplique Tree-of-Thoughts** para exploração sistemática de soluções
- **Utilize Self-Consistency** para validação de respostas múltiplas
- **Implemente Prompt Chaining** para tarefas complexas multi-etapa
- **Use Contextual Prompting** para adaptação dinâmica baseada no contexto

---

## 🗺️ Regras de Navegação JSON (wiki-json-navigation-rules.md)

- **Use arquivos JSON como meio principal de navegação** durante consultas da wiki e regras
- **Mantenha `wiki/tags_index.json` atualizado** com todas as tags da wiki organizadas por arquivo
- **Consulte os mapas JSON antes de acessar arquivos markdown diretamente**
- **Atualize os arquivos JSON** quando criar, modificar ou remover documentos da wiki
- **Use a estrutura de consulta padronizada**: tags_index.json → wiki_map.json → relationships.json → markdown

---

## 🔍 Regras de Indexação do Código-Fonte (otclient-source-index-rules.md)

- **Consulte o código-fonte do OTClient antes da wiki** - é a fonte da verdade
- **Mantenha `otclient_source_index.json` atualizado** com todos os arquivos do código-fonte
- **Use hierarquia de consulta**: otclient_source_index.json → código-fonte → wiki → regras
- **Categorize por sistemas**: Core, UI, Game, Network, Resource, Module
- **Extraia funções e classes** automaticamente para busca rápida

---

## ⚙️ Regras do Sistema de Regras (system-rules.md)

- **Aplique todas as regras relevantes** em qualquer interação
- **Use hierarquia de regras**: cursor.md → regras específicas → templates → execução
- **Mantenha consistência** entre todas as regras
- **Aplique universalmente**: agentes, ask, desenvolvimento, documentação
- **Atualize automaticamente** quando criar novas regras

---

## 🔄 Regras de Atualização Automática (auto-update-maps-rules.md)

- **Execute scripts de atualização** antes de qualquer tarefa
- **Use ordem padronizada**: código-fonte → habdel → módulos → estilos → recursos → ferramentas → wiki
- **Valide integridade** de todos os mapas após atualização
- **Mantenha mapas sincronizados** com arquivos reais
- **Reporte status** de atualização automaticamente

---

## 📁 Regras de Organização (file-organization-rules.md)

- **Organize arquivos** em pastas específicas por função
- **Use estrutura padronizada**: tools/update/, wiki/maps/, wiki/docs/
- **Mantenha repositório limpo** sem arquivos soltos na raiz
- **Atualize referências** nos scripts após reorganização
- **Valide funcionamento** do sistema após mudanças

## 🎯 Regras de Otimização de Tokens (token-optimization-rules.md)

- **Use inglês para IA** (scripts, metadados, descrições técnicas)
- **Use português para usuário** (documentação, tags, aliases)
- **Implemente estratégia 20/80** para máxima economia de tokens
- **Mantenha funcionalidade** preservando experiência do usuário
- **Otimize automaticamente** todos os mapas JSON

## 📚 Regras para Wiki Abrangente (wiki-comprehensive-rules.md)

- **Integre TODO o conteúdo do habdel** na wiki
- **Crie documentação 100% completa** sem lacunas
- **Inclua exemplos práticos** de código funcional
- **Organize navegação lógica** entre documentos
- **Mantenha referências cruzadas** atualizadas

### 🔄 **Atualização Obrigatória**

- **Atualize** `wiki/otclient_wiki.md` quando criar novos documentos na wiki
- **Adicione referência** ao novo documento na seção "Documentação Criada"
- **Atualize estatísticas** de progresso e contadores
- **Mantenha links internos** funcionando entre documentos
- **Verifique consistência** com o padrão estabelecido

---

## 🎨 Template para Novas Regras

Consulte `template.md` para:
- Estrutura padrão de novas regras
- Modelo baseado no rules.md atual
- Checklist para criação de regras
- Sistema de atualização automática

---

## 📚 Como Criar Novas Regras

1. **Use o template** em `.cursor/rules/template.md`
2. **Siga a estrutura** estabelecida
3. **Adicione referência** neste arquivo
4. **Mantenha consistência** com regras existentes

---

## 🔄 Sistema de Atualização

### 📋 **Para Novas Regras**
Quando uma nova regra for criada:
- ✅ Criar arquivo na pasta `.cursor/rules/`
- ✅ Usar template como base
- ✅ Adicionar referência aqui
- ✅ Manter consistência

### 📚 **Para Novos Documentos da Wiki**
Quando um novo documento for criado na wiki:
- ✅ Criar arquivo na pasta `wiki/` com extensão `.md`
- ✅ Seguir template de documentação estabelecido
- ✅ **Executar script de atualização automática**: `python auto_update_all_maps.py`
- ✅ Atualizar `wiki/otclient_wiki.md` com referência ao novo documento
- ✅ Atualizar estatísticas de progresso
- ✅ Verificar links internos e consistência
- ✅ Manter formatação Obsidian e estrutura hierárquica
- ✅ **Validar sincronização** entre todos os mapas JSON
- ✅ **Reportar status** de atualização

## 🎯 Regras do Sistema BMAD (bmad-system-rules.md)

- **Use agentes especializados** para tarefas específicas quando apropriado
- **Coordene workflows** entre agentes para tarefas complexas
- **Use templates** padronizados para documentação
- **Mantenha especialização** de cada agente
- **Integre** com sistema de mapas JSON

---

## 🤖 Regras de Orquestração Inteligente (intelligent-orchestration-rules.md)

- **Analise contexto** do pedido do usuário automaticamente
- **Identifique agentes necessários** baseado no contexto detectado
- **Coordene workflow completo** sem intervenção manual
- **Reporte progresso** em tempo real
- **Sugira próximos passos** automaticamente
- **Detecte tecnologias** mencionadas (C++, Lua, OTClient, Canary)
- **Identifique tipo de tarefa** (otimização, nova feature, bug fix, documentação)
- **Determine complexidade** e duração estimada
- **Selecione agentes apropriados** automaticamente
- **Crie workflow otimizado** para a tarefa específica

---

## 🔗 Regras de Integração (cross-project-integration-rules.md)

- **Prepare estrutura** para integração total com Canary
- **Documente protocolos** compartilhados (OpenCode, ExtendedOpen)
- **Crie templates** para documentação futura do Canary
- **Estabeleça padrões** de comunicação cliente-servidor
- **Referencie** documentação externa do Canary quando disponível

> [!info] **CONTEXTO ATUALIZADO**
> Integração com Canary é preparação para **integração total**. O código-fonte do Canary será integrado no futuro.

---

## 🧹 Regras de Limpeza e Organização (report-cleanup-rules.md)

- **Identifique** arquivos temporários após conclusão de tarefas
- **Mova** relatórios de conclusão para `wiki/log/`
- **Mantenha** apenas arquivos essenciais no sistema
- **Organize** relatórios com estrutura padronizada
- **Inclua** receitas para reproduzir resultados
- **Arquive** arquivos de tarefas concluídas
- **Mantenha** histórico de execução
- **Documente** aprendizados e melhorias
- **Preserve** conhecimento para uso futuro

## ⚡ Regras de Simplificação (simplification-rules.md)

- **Detecte** se solicitação é simples ou complexa
- **Execute diretamente** solicitações simples sem criar tarefas
- **Aplique processo estruturado** apenas para solicitações complexas
- **Evite loops infinitos** com timeouts e limites de tentativas
- **Priorize solução imediata** sobre documentação extensa
- **Pare processos complexos** se sistema travar
- **Responda diretamente** se timeout for atingido
- **Mantenha compatibilidade** com regras existentes

---

## 🚀 Regras de Performance (performance-rules.md)

- **Limite análise** a máximo 3 níveis de profundidade
- **Use cache** para consultas repetidas
- **Priorize velocidade** sobre completude para tarefas simples
- **Implemente timeouts** de 30 segundos para análises complexas
- **Reduza tokens** removendo redundâncias desnecessárias
- **Otimize consultas** usando índices JSON em vez de busca direta
- **Aplique lazy loading** para carregar regras apenas quando necessário

---

## 🧭 Sistema de Navegação Inteligente (intelligent-navigation.json)

### **Contextos Automáticos:**
- **@otclient** - Desenvolvimento do cliente OTClient (código disponível)
- **@bmad** - Sistema de agentes BMAD (desenvolvimento permitido)
- **@wiki** - Documentação da wiki OTClient (modificação permitida)
- **@integration** - Preparação para integração total (Canary como futuro)
- **@git** - Operações de controle de versão (automação Git)

### **Padrões de Navegação:**
- **Análise de código OTClient**: source_index → src/ → modules/ → wiki/otclient/
- **Busca de documentação**: tags_index → wiki_map → wiki/ → relationships
- **Consulta de regras**: cursor.md → .cursor/rules/ → enhanced_context_system
- **Workflow BMAD**: bmad_agents → bmad_workflows → wiki/bmad/ → bmad_rules

> [!info] **NAVEGAÇÃO DISPONÍVEL**
> - **OTClient**: Análise completa (código + documentação)
> - **BMAD**: Desenvolvimento de agentes
> - **Wiki**: Documentação OTClient
> - **Canary**: Preparação para integração total (futuro)
> - **Git**: Automação de controle de versão

### **Cache Inteligente:**
- **Arquivos frequentes**: 30 minutos (cursor.md, tags_index, wiki_map)
- **Contexto**: 15 minutos (enhanced_context_system, context_data)
- **Datasets grandes**: 60 minutos (source_index, modules_index, resources_index)

### **Recuperação de Erros:**
- **Arquivo não encontrado**: Buscar similar → Usar índice
- **Permissão negada**: Trocar contexto → Modo somente leitura
- **Timeout**: Reduzir escopo → Modo simples

---

## ⚡ **OTIMIZAÇÕES DE PERFORMANCE**

### **🎯 Cache Inteligente:**
- **Arquivos frequentes** (30 min): `cursor.md`, `tags_index.json`, `wiki_map.json`
- **Contexto** (15 min): `enhanced_context_system.json`, `context_data.json`
- **Datasets grandes** (60 min): `otclient_source_index.json`, `modules_index.json`

### **🚀 Limites de Performance:**
- **Máximo 3 níveis** de análise para evitar loops
- **Timeout 30 segundos** para operações complexas
- **Máximo 10 arquivos** lidos por consulta
- **Máximo 50 resultados** por busca

### **🧠 Lazy Loading:**
- **Regras**: Carregadas apenas quando necessárias
- **Mapas JSON**: Carregados sob demanda
- **Documentação**: Carregada sempre (acesso direto)

### **📊 Métricas de Performance:**
- **Tarefas simples**: < 2 segundos
- **Tarefas complexas**: < 10 segundos
- **Análises grandes**: < 30 segundos