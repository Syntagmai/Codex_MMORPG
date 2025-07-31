# Regras de Automação Git - Sistema Automático, Atômico e Integrado

## 📋 Regras do Agente de Automação Git

Este arquivo define as regras para o **agente de automação Git especializado** que gerencia commits, validação de boas práticas e integração com o sistema de tarefas BMAD.

---

## 🚨 **REGRAS CRÍTICAS - SEMPRE AUTOMÁTICO**

### 1. **NUNCA FAÇA COMMITS MANUAIS**
**SEMPRE use o agente Git para qualquer operação de commit.** Commits manuais são PROIBIDOS. O agente Git é especializado em automação, validação de boas práticas e integração com o sistema de tarefas.

### 2. **Commits Automáticos Obrigatórios**
**SEMPRE execute commits automaticamente** quando detectar mudanças. Não aguarde confirmação manual. O agente deve analisar, validar e commitar automaticamente.

### 3. **Commits Atômicos Obrigatórios**
**SEMPRE faça commits atômicos** - um commit por mudança lógica. Separe automaticamente mudanças diferentes em commits separados.

### 4. **Resolução Automática de Erros**
**SEMPRE resolva erros automaticamente** sem intervenção manual. O agente deve detectar e corrigir problemas de Git automaticamente.

### 5. **Análise Inteligente de Mudanças**
**SEMPRE analise arquivos mudados** e categorize automaticamente. Separe mudanças por contexto e tipo para commits atômicos.

### 6. **Integração com Task Manager**
**SEMPRE integre com o sistema de tarefas** para commits contextuais. Cada tarefa concluída deve gerar um commit automático com mensagem explicativa.

---

## 🎯 Regras Principais

### 1. **Agente Git Obrigatório**
**SEMPRE use o agente Git para qualquer operação de commit.** O agente Git é especializado em automação, validação de boas práticas e integração com o sistema de tarefas.

### 2. **Commits em Português Obrigatórios**
**SEMPRE use português para mensagens de commit.** Todas as mensagens, validações e relatórios devem estar em português para manter consistência com o sistema.

### 3. **Conventional Commits Obrigatórios**
**SEMPRE use formato Conventional Commits.** Todas as mensagens devem seguir o padrão: `tipo: descrição` com tipos padronizados.

### 4. **Validação Automática Obrigatória**
**SEMPRE valide commits antes de executar.** O agente deve verificar qualidade, formato e boas práticas automaticamente.

### 5. **Integração com Sistema de Tarefas**
**SEMPRE integre com sistema de tarefas.** O agente deve detectar contexto de tarefa ativa e incluir informações relevantes nos commits.

### 6. **Mensagens Contextuais Obrigatórias**
**SEMPRE use mensagens contextuais** explicando o que foi feito, incluindo referências ao dashboard central e impacto da mudança.

---

## 🔧 Funcionalidades Obrigatórias

### 📊 **Análise Automática de Mudanças**
- **Detecção de arquivos modificados** usando Git status
- **Categorização por tipo** baseada em extensões e padrões
- **Identificação de contexto** de tarefa ativa
- **Geração de resumo** das mudanças em português
- **Separação automática** de mudanças por contexto

### 🎯 **Geração Inteligente de Mensagens**
- **Formato Conventional Commits** obrigatório
- **Inclusão de contexto** de tarefa quando disponível
- **Descrição detalhada** em português
- **Timestamp automático** de geração
- **Mensagens atômicas** por mudança específica
- **Template padronizado** para mensagens contextuais

### ✅ **Validação de Boas Práticas**
- **Verificação de formato** Conventional Commits
- **Validação de tamanho** da mensagem
- **Checagem de caracteres** especiais
- **Score de qualidade** (0-100)
- **Sugestões de melhoria** automáticas

### 🔄 **Execução Automática**
- **Commit automático** com validação
- **Push opcional** configurável
- **Logs detalhados** de operações
- **Relatórios de sucesso** ou erro
- **Resolução automática** de problemas

### 🎯 **Integração com Tarefas**
- **Detecção automática** de tarefa ativa
- **Inclusão de ID da tarefa** na mensagem
- **Contexto de desenvolvimento** preservado
- **Rastreabilidade** completa de mudanças
- **Atualização automática** do dashboard central

---

## 🔄 Workflow de Integração Git-Task Manager

### **Fase 1: Conclusão de Tarefa**
```python
def complete_task(task_info):
    # 1. Marcar tarefa como concluída no dashboard
    # 2. Atualizar métricas de progresso
    # 3. Gerar relatório de conclusão
    # 4. Preparar commit automático
    return task_completion_data
```

### **Fase 2: Preparação do Commit**
```python
def prepare_git_commit(task_completion_data):
    # 1. Analisar mudanças realizadas
    # 2. Gerar mensagem contextual
    # 3. Incluir métricas de progresso
    # 4. Referenciar dashboard central
    return commit_message
```

### **Fase 3: Execução do Commit**
```python
def execute_git_commit(commit_message):
    # 1. Adicionar arquivos modificados
    # 2. Fazer commit com mensagem contextual
    # 3. Atualizar dashboard com hash do commit
    # 4. Gerar relatório de commit
    return commit_hash
```

---

## 📋 Formato de Mensagens de Commit

### **🎯 Template Padrão:**
```
feat(task-manager): [CATEGORIA] - [TÍTULO DA TAREFA]

📊 Progresso: [X]% → [Y]% ([+/-]Z%)
🎯 Categoria: [Epic/Story/Agent/Roadmap/Planejamento]
📋 Dashboard: integrated_task_manager.md

🔧 Mudanças Realizadas:
- [Lista de mudanças específicas]
- [Funcionalidades implementadas]
- [Arquivos modificados]

📈 Impacto no Sistema:
- [Benefícios da mudança]
- [Melhorias no progresso]
- [Próximos passos habilitados]

🔗 Referências:
- Epic: [ID da Epic] (se aplicável)
- Story: [ID da Story] (se aplicável)
- Agent: [Nome do Agent] (se aplicável)

📊 Métricas Atualizadas:
- Progresso Geral: [X]%
- [Categoria]: [Y]%
- Tasks Concluídas: [Z]/[Total]

---
Commit automático gerado pelo Task Manager Agent
```

### **🎨 Exemplos de Mensagens:**

#### **Epic Commit:**
```
feat(epic): Epic 1 - Wiki OTClient Completa - 100% CONCLUÍDA

📊 Progresso: 75% → 100% (+25%)
🎯 Categoria: Epic
📋 Dashboard: integrated_task_manager.md

🔧 Mudanças Realizadas:
- Completadas todas as 60 stories do habdel
- Integração completa habdel-wiki principal
- Validação de qualidade da documentação
- Criação de índices de navegação

📈 Impacto no Sistema:
- Wiki OTClient agora tem 100% de cobertura
- Documentação completa e navegável
- Base sólida para integração Canary

🔗 Referências:
- Epic: Epic 1 - Wiki OTClient Completa
- Stories: UI-001 a REF-005 (60 total)

📊 Métricas Atualizadas:
- Progresso Geral: 100%
- Documentação: 100%
- Tasks Concluídas: 20/20

---
Commit automático gerado pelo Task Manager Agent
```

#### **Story Commit:**
```
feat(story): UI-015 - Sistema de Scroll e Paginação

📊 Progresso: 45% → 50% (+5%)
🎯 Categoria: Story
📋 Dashboard: integrated_task_manager.md

🔧 Mudanças Realizadas:
- Documentação completa do sistema de scroll
- Guias práticos de implementação
- Exemplos de código e configuração
- Integração com wiki principal

📈 Impacto no Sistema:
- UI Stories: 15/20 completas (75%)
- Documentação de scroll e paginação disponível
- Próximo: UI-016 Sistema de Grid e Listas

🔗 Referências:
- Story: UI-015
- Epic: Epic 1 - Wiki OTClient Completa

📊 Métricas Atualizadas:
- UI Stories: 75%
- Progresso Geral: 50%
- Tasks Concluídas: 30/60

---
Commit automático gerado pelo Task Manager Agent
```

#### **Agent Commit:**
```
feat(agent): Git Automation Agent - Implementação Completa

📊 Progresso: 80% → 85% (+5%)
🎯 Categoria: Agent
📋 Dashboard: integrated_task_manager.md

🔧 Mudanças Realizadas:
- Implementação completa do Git Automation Agent
- Sistema de commits automáticos
- Validação de boas práticas
- Integração com Task Manager

📈 Impacto no Sistema:
- Automação completa de commits
- Qualidade garantida de mensagens
- Integração perfeita com tarefas

🔗 Referências:
- Agent: Git Automation Agent
- Epic: Epic 4 - Agentes Autônomos

📊 Métricas Atualizadas:
- Agentes BMAD: 85%
- Progresso Geral: 85%
- Tasks Concluídas: 17/20

---
Commit automático gerado pelo Task Manager Agent
```

---

## 📊 Categorias de Commit

### **🎯 Epic Commits:**
- **Trigger**: Conclusão de epic completa
- **Escopo**: Todas as subtasks da epic
- **Impacto**: Alto (mudança significativa no progresso)
- **Frequência**: Baixa (4 epics no total)

### **📚 Story Commits:**
- **Trigger**: Conclusão de story individual
- **Escopo**: Funcionalidade específica
- **Impacto**: Médio (progresso incremental)
- **Frequência**: Média (60 stories no total)

### **🤖 Agent Commits:**
- **Trigger**: Implementação de agente
- **Escopo**: Sistema de automação
- **Impacto**: Alto (capacidade de automação)
- **Frequência**: Baixa (12 agentes no total)

### **🗺️ Roadmap Commits:**
- **Trigger**: Implementação de roadmap
- **Escopo**: Planejamento estratégico
- **Impacto**: Médio (visão de longo prazo)
- **Frequência**: Baixa (3 roadmaps no total)

### **📋 Planejamento Commits:**
- **Trigger**: Ativação de planejamento
- **Escopo**: Estratégia específica
- **Impacto**: Médio (metodologia)
- **Frequência**: Baixa (5 planejamentos no total)

---

## 🚨 **SISTEMA DE RESOLUÇÃO AUTOMÁTICA DE ERROS**

### **Erros Críticos - Resolução Automática**
```python
def resolve_git_errors_automatically():
    """Resolve erros Git automaticamente sem intervenção manual."""
    
    # 1. Verificar se é repositório Git
    if not is_git_repo():
        initialize_git_repo()
    
    # 2. Verificar conflitos de merge
    if has_merge_conflicts():
        resolve_merge_conflicts_automatically()
    
    # 3. Verificar permissões
    if has_permission_issues():
        fix_permissions_automatically()
    
    # 4. Verificar arquivos não rastreados
    if has_untracked_files():
        add_untracked_files_automatically()
    
    # 5. Verificar staging vazio
    if is_staging_empty():
        add_changed_files_automatically()
    
    # 6. Verificar validação de mensagem
    if has_validation_errors():
        fix_validation_automatically()
```

### **Tratamento de Erros Específicos**
- **Git não inicializado**: Inicializar automaticamente
- **Conflitos de merge**: Resolver automaticamente
- **Permissões insuficientes**: Corrigir automaticamente
- **Arquivos não rastreados**: Adicionar automaticamente
- **Staging vazio**: Adicionar mudanças automaticamente
- **Mensagem muito longa**: Encurtar automaticamente
- **Caracteres especiais**: Remover automaticamente
- **Sem descrição**: Gerar automaticamente
- **Formato incorreto**: Corrigir automaticamente

---

## 📋 Padrões de Mensagens

### **Conventional Commits em Português**
```bash
# Formato padrão
tipo: descrição em português

# Exemplos válidos
feat: adicionar nova funcionalidade de automação
fix: corrigir bug na validação de commits
docs: atualizar documentação do sistema
style: formatar código seguindo padrões
refactor: refatorar sistema de validação
test: adicionar testes para agente Git
chore: atualizar dependências do projeto
```

### **Tipos de Commit Padrão**
- **feat**: Nova funcionalidade
- **fix**: Correção de bug
- **docs**: Documentação
- **style**: Formatação
- **refactor**: Refatoração
- **test**: Testes
- **chore**: Manutenção
- **perf**: Melhoria de performance
- **ci**: Integração contínua
- **build**: Build do sistema

### **Inclusão de Contexto de Tarefa**
```bash
# Com tarefa ativa
feat: implementar agente de automação Git - TASK-003

# Sem tarefa ativa
feat: implementar agente de automação Git
```

---

## 🔧 Configuração do Sistema

### **Parâmetros Obrigatórios**
```json
{
  "git_automation": {
    "enabled": true,
    "language": "portuguese",
    "conventional_commits": true,
    "auto_commit": true,
    "auto_push": false,
    "validation_strict": true,
    "include_task_context": true,
    "max_commit_size": 10,
    "require_description": true,
    "atomic_commits": true,
    "auto_error_resolution": true,
    "never_manual": true,
    "task_manager_integration": true,
    "dashboard_updates": true,
    "contextual_messages": true
  }
}
```

### **Variáveis de Ambiente**
```bash
# Configurações obrigatórias
GIT_AUTO_COMMIT=true
GIT_LANGUAGE=portuguese
GIT_CONVENTIONAL_COMMITS=true
GIT_VALIDATION_LEVEL=strict
GIT_INCLUDE_TASK_CONTEXT=true
GIT_ATOMIC_COMMITS=true
GIT_AUTO_ERROR_RESOLUTION=true
GIT_NEVER_MANUAL=true
GIT_TASK_MANAGER_INTEGRATION=true
GIT_DASHBOARD_UPDATES=true
GIT_CONTEXTUAL_MESSAGES=true

# Configurações opcionais
GIT_AUTO_PUSH=false
GIT_MAX_COMMIT_SIZE=10
GIT_REQUIRE_DESCRIPTION=true
```

---

## 📊 Métricas de Qualidade

### **Indicadores Obrigatórios**
- **Taxa de commits válidos**: > 95%
- **Tempo de criação de commit**: < 30 segundos
- **Conformidade com boas práticas**: > 98%
- **Integração com tarefas**: 100% funcional
- **Detecção de contexto**: > 90%
- **Resolução automática de erros**: > 95%
- **Mensagens contextuais**: 100%
- **Atualização do dashboard**: 100%

### **Validação de Qualidade**
- **Formato Conventional Commits**: Obrigatório
- **Tamanho da primeira linha**: < 72 caracteres
- **Descrição em português**: Obrigatório
- **Contexto de tarefa**: Quando disponível
- **Timestamp automático**: Obrigatório
- **Commits atômicos**: Obrigatório
- **Mensagens contextuais**: Obrigatório
- **Integração com dashboard**: Obrigatório

---

## 🔗 Integração com Dashboard

### **📋 Atualização Automática:**
```python
def update_dashboard_with_commit(commit_hash, task_data):
    # 1. Adicionar hash do commit ao dashboard
    # 2. Atualizar métricas de progresso
    # 3. Marcar tarefa como concluída
    # 4. Gerar relatório de impacto
    return dashboard_update
```

### **📊 Rastreabilidade:**
- **Hash do Commit**: Sempre incluído no dashboard
- **Data/Hora**: Timestamp de conclusão
- **Agente Responsável**: Identificação do agente
- **Impacto**: Métricas antes/depois
- **Contexto**: Referência à tarefa específica

---

## 🚨 Regras de Emergência

### **🔥 Commit de Emergência:**
- **Trigger**: Problema crítico detectado
- **Formato**: `fix(emergency): [DESCRIÇÃO RÁPIDA]`
- **Prioridade**: Máxima
- **Validação**: Automática

### **🔄 Rollback Automático:**
- **Trigger**: Falha na execução de tarefa
- **Ação**: Reverter commit anterior
- **Notificação**: Alerta imediato
- **Documentação**: Relatório de falha

### **📊 Commit de Métricas:**
- **Trigger**: Atualização de métricas
- **Formato**: `docs(metrics): Atualização de progresso`
- **Frequência**: A cada 5 minutos
- **Escopo**: Apenas métricas

---

## 📈 Métricas de Commit

### **📊 KPIs de Commit:**
- **Frequência**: Commits por hora/dia
- **Qualidade**: Tamanho e clareza das mensagens
- **Impacto**: Progresso gerado por commit
- **Rastreabilidade**: Links para dashboard
- **Contextualização**: % de mensagens contextuais

### **🎯 Metas de Commit:**
- **Mínimo**: 1 commit por tarefa concluída
- **Ideal**: 1 commit por hora de trabalho
- **Máximo**: 1 commit por 15 minutos
- **Qualidade**: 100% de mensagens contextuais
- **Dashboard**: 100% de atualizações automáticas

---

## 🔗 Integração com Sistema Existente

### **Sistema BMAD**
- **Orquestração inteligente** com outros agentes
- **Workflows coordenados** para operações complexas
- **Templates padronizados** para mensagens
- **Logs integrados** com sistema de relatórios

### **Sistema de Tarefas**
- **Detecção automática** de tarefa ativa
- **Inclusão de contexto** nos commits
- **Rastreabilidade** de mudanças por tarefa
- **Relatórios integrados** de progresso
- **Atualização automática** do dashboard

### **Cursor IDE**
- **Atalhos de teclado** para operações rápidas
- **Configurações automáticas** de automação
- **Integração com terminal** integrado
- **Notificações** de status de operações

---

## ✅ Tarefa Obrigatória da IA

**SEMPRE que qualquer operação Git for solicitada:**

1. **Ativar** agente de automação Git automaticamente
2. **Analisar** mudanças no repositório
3. **Detectar** contexto de tarefa ativa
4. **Separar** mudanças por contexto (commits atômicos)
5. **Gerar** mensagem de commit em português
6. **Validar** boas práticas automaticamente
7. **Resolver** erros automaticamente (se houver)
8. **Executar** commit com validação
9. **Atualizar** dashboard central automaticamente
10. **Gerar** relatório de operação
11. **Integrar** com sistema de tarefas

**NUNCA FAÇA COMMITS MANUAIS - SEMPRE USE O AGENTE!**

---

## 🚀 Benefícios Esperados

### **Produtividade**
- **Commits automáticos** durante desenvolvimento
- **Validação instantânea** de qualidade
- **Redução de tempo** em operações Git
- **Padronização** de mensagens
- **Resolução automática** de problemas
- **Integração perfeita** com Task Manager

### **Qualidade**
- **Boas práticas** sempre aplicadas
- **Prevenção** de commits ruins
- **Histórico limpo** de mudanças
- **Documentação automática** de progresso
- **Commits atômicos** sempre
- **Mensagens contextuais** explicativas

### **Integração**
- **Workflow unificado** de desenvolvimento
- **Relatórios automáticos** de progresso
- **Rastreabilidade** completa de mudanças
- **Colaboração melhorada** entre equipes
- **Zero intervenção manual** necessária
- **Dashboard sempre atualizado**

---

## 🎯 Conclusão

### **📊 Objetivos:**
- **100% de commits automáticos** após tarefas
- **100% de mensagens contextuais** explicativas
- **100% de rastreabilidade** no dashboard
- **100% de integração** entre Task Manager e Git
- **100% de automação** sem intervenção manual

### **🚀 Resultado Esperado:**
- **Histórico completo** de todas as mudanças
- **Mensagens explicativas** para cada commit
- **Rastreabilidade total** no dashboard central
- **Automação completa** do processo de commit
- **Integração perfeita** entre Git e Task Manager

---

*Regras consolidadas pelo Sistema BMAD - OTClient Documentation*  
**Consolidação**: git-automation-rules.md + git-task-manager-integration-rules.md  
**Data**: 2025-01-27  
**Status**: 🟢 **Regras Ativas e Consolidadas** 