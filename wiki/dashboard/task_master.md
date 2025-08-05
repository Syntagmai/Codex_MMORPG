---
tags: [task_master, system_control, project_management, bmad, wiki_optimization]
type: task_master
status: active
priority: critical
created: 2025-08-04
updated: 2025-08-05
---

# 🎯 **TASK MASTER - EPIC 22 ATIVA**

> [!info] **EPIC ATIVA**
> Este arquivo contém apenas a **Epic 22 ativa** para foco total.
> Para histórico completo das Epics 1-21, consulte: **[📚 Epics Arquivadas](task_master_archived.md)**

---

## 🎯 **PRIORIDADE ATUAL**

### **🔄 EPIC 22: REORGANIZAÇÃO COMPLETA DE DIRETÓRIOS E ESTRUTURA DO PROJETO**
**Status**: 0% | **Prioridade**: Crítica | **Foco**: Reorganização Estrutural

**Objetivo**: Reorganizar completamente a estrutura de diretórios do projeto, limpar a pasta wiki, separar conteúdo educacional de sistemas internos e criar estrutura organizada e escalável.

**Contexto**: Análise do arquivo `diretorios.md` revelou problemas críticos de organização: 2.178 arquivos .md espalhados, pasta wiki bagunçada, relatórios misturados com documentação, scripts na raiz e estrutura inconsistente.

---

## 📋 **REGRAS DE EXECUÇÃO**

### **⚡ REGRAS PRINCIPAIS**
1. **Foco Total**: Apenas Epic 22 - Reorganização Completa de Diretórios
2. **Ordem de Prioridade**: Seguir sequência das tasks (22.1 → 22.5)
3. **Backup Obrigatório**: Fazer backup completo antes de qualquer mudança
4. **Validação Contínua**: Testar cada fase antes de prosseguir
5. **Atualização de Sistemas**: Manter todos os sistemas funcionando

### **🔍 CRITÉRIOS DE QUALIDADE**
- **Organização**: Estrutura clara e lógica
- **Separação**: Conteúdo educacional separado de sistemas internos
- **Navegabilidade**: Fácil localização de arquivos
- **Escalabilidade**: Estrutura preparada para crescimento
- **Compatibilidade**: Manter funcionamento de todos os sistemas

---

## 📊 **STATUS ATUAL**

### **Task Master Atualizado**: 2025-08-05
### **Status**: 🔄 EPIC 22 EM ANDAMENTO
### **Foco**: Reorganização Completa de Diretórios

---

## 🎯 **EPIC 22: REORGANIZAÇÃO COMPLETA DE DIRETÓRIOS E ESTRUTURA DO PROJETO**

### **Status**: 0%
### **Prioridade**: Crítica
### **Objetivo**: Reorganizar completamente a estrutura de diretórios do projeto, limpar a pasta wiki, separar conteúdo educacional de sistemas internos e criar estrutura organizada e escalável

### **Contexto**: Análise do arquivo `diretorios.md` revelou problemas críticos de organização: 2.178 arquivos .md espalhados, pasta wiki bagunçada, relatórios misturados com documentação, scripts na raiz e estrutura inconsistente.

### **Tasks da Epic 22:**

- [ ] **22.1** Limpeza da Raiz e Arquivos Soltos (0%)
  - **Descrição**: Mover todos os arquivos soltos da raiz para suas pastas apropriadas
  - **Prioridade**: Crítica
  - **Tempo Estimado**: 8 horas
  - **Dependências**: Nenhuma
  - **Sub-tarefas**:
    - [ ] Mover relatórios da raiz para `logs/reports/` (charm_error.md, RELATORIO_COMPARATIVO_INVENTARIOS.md)
    - [ ] Mover documentação da raiz para `docs/guides/` (README_LEARNING_WORKFLOW.md, COMO_USAR_SISTEMA_INTELIGENTE.md, README_GUI_SYSTEM.md)
    - [ ] Mover scripts da raiz para `scripts/` (audit_file_structure.py, activate_complete_system.sh, learn_command.py, build_exe_simple.bat, quick_unicode_fix.py, bmad_system_gui_integrated.py, unicode_aliases.py, unicode_fix.py, chat_learning_integration.py)
    - [ ] Mover backup da raiz para `backup/` (README.md.backup)
    - [ ] Validar que raiz está limpa e organizada
  - **Resultado Esperado**: Raiz do projeto limpa com apenas arquivos essenciais

- [ ] **22.2** Limpeza e Reorganização da Pasta Wiki (0%)
  - **Descrição**: Reorganizar completamente a pasta wiki, removendo conteúdo não educacional
  - **Prioridade**: Crítica
  - **Tempo Estimado**: 16 horas
  - **Dependências**: 22.1
  - **Sub-tarefas**:
    - [ ] Remover pasta redundante `wiki/wiki/`
    - [ ] Mover relatórios de `wiki/log/` para `logs/`
    - [ ] Mover backups de `wiki/backup/` para `backup/`
    - [ ] Mover scripts de `wiki/update/` e `wiki/tools/` para `scripts/`
    - [ ] Mover monitoramento de `wiki/monitoring/` para `logs/monitoring/`
    - [ ] Mover ML de `wiki/ml/` para `docs/ml/`
    - [ ] Mover alertas de `wiki/alerts/` para `logs/alerts/`
    - [ ] Mover métricas de `wiki/metrics/` para `logs/metrics/`
    - [ ] Mover dados consolidados de `wiki/consolidated/` para `data/consolidated/`
    - [ ] Mover cursor core de `wiki/cursor_core/` para `docs/game-development/`
    - [ ] Mover dashboard de `wiki/dashboard/` para `docs/dashboard/`
    - [ ] Mover templates de `wiki/templates/` para `docs/templates/`
    - [ ] Mover BMAD de `wiki/bmad/` para `docs/bmad/`
    - [ ] Mover maps de `wiki/maps/` para `data/maps/`
    - [ ] Mover workflows de `wiki/workflows/` para `docs/workflows/`
    - [ ] Mover habdel de `wiki/habdel/` para `habdel/` (pasta própria)
    - [ ] Manter apenas `wiki/educational/`, `wiki/integration/` e conteúdo educacional
  - **Resultado Esperado**: Pasta wiki limpa com apenas conteúdo educacional para Obsidian

- [ ] **22.3** Classificação e Organização dos Arquivos .md (0%)
  - **Descrição**: Classificar todos os 2.178 arquivos .md e organizá-los por categoria
  - **Prioridade**: Alta
  - **Tempo Estimado**: 20 horas
  - **Dependências**: 22.2
  - **Sub-tarefas**:
    - [ ] Criar sistema de classificação automática de arquivos .md
    - [ ] Separar relatórios (~50 arquivos) para `logs/reports/`
    - [ ] Separar índices (~15 arquivos) para `docs/indexes/`
    - [ ] Separar guias internos (~10 arquivos) para `docs/guides/`
    - [ ] Separar glossários (~5 arquivos) para `docs/glossary/`
    - [ ] Separar sistemas internos (~20 arquivos) para `docs/systems/`
    - [ ] Separar metodologia Habdel (~100 arquivos) para `habdel/`
    - [ ] Manter documentação final (~100 arquivos) na `wiki/`
    - [ ] Analisar e organizar arquivos órfãos (~1.800 arquivos)
    - [ ] Criar índices de navegação para cada categoria
  - **Resultado Esperado**: Todos os arquivos .md organizados por categoria e função

- [ ] **22.4** Criação da Estrutura Final Organizada (0%)
  - **Descrição**: Criar estrutura final organizada com pastas bem definidas
  - **Prioridade**: Alta
  - **Tempo Estimado**: 12 horas
  - **Dependências**: 22.3
  - **Sub-tarefas**:
    - [ ] Criar estrutura `wiki/` = Apenas conteúdo educacional (Obsidian)
    - [ ] Criar estrutura `habdel/` = Metodologia de pesquisa e stories
    - [ ] Criar estrutura `docs/` = Documentação interna do sistema
      - [ ] `docs/bmad/` = Sistema BMAD (organização e documentação)
      - [ ] `docs/game-development/` = Sistema de desenvolvimento de jogos
      - [ ] `docs/dashboard/` = Sistema de tarefas
      - [ ] `docs/templates/` = Templates e padrões
      - [ ] `docs/workflows/` = Workflows de desenvolvimento
    - [ ] Organizar `logs/` = Todos os relatórios e logs
    - [ ] Organizar `scripts/` = Todos os scripts e ferramentas
    - [ ] Organizar `config/` = Configurações e certificados
    - [ ] Organizar `backup/` = Todos os backups
    - [ ] Organizar `temp/` = Arquivos temporários
    - [ ] Organizar `data/` = Dados consolidados e mapas
    - [ ] Organizar `assets/` = Recursos estáticos
  - **Resultado Esperado**: Estrutura final organizada e escalável

- [ ] **22.5** Atualização de Sistemas e Validação (0%)
  - **Descrição**: Atualizar todos os sistemas para funcionar com nova estrutura
  - **Prioridade**: Alta
  - **Tempo Estimado**: 16 horas
  - **Dependências**: 22.4
  - **Sub-tarefas**:
    - [ ] Atualizar scripts (todos os .py, .sh, .bat) com novos caminhos
    - [ ] Atualizar regras do sistema sobre diretórios (`.cursor/rules/`)
    - [ ] Atualizar orquestrador principal (`cursor.md`)
    - [ ] Atualizar mapas JSON para navegação fluida
    - [ ] Atualizar README.md explicando nova estrutura
    - [ ] Validar funcionamento de todos os sistemas
    - [ ] Criar documentação da nova organização
    - [ ] Testar navegação e acesso a todos os arquivos
    - [ ] Validar que nenhum sistema quebrou
    - [ ] Criar relatório final de reorganização
  - **Resultado Esperado**: Todos os sistemas funcionando com nova estrutura

### **Resultado Esperado**: Projeto completamente reorganizado com estrutura clara, wiki limpa apenas com conteúdo educacional, sistemas internos separados e navegação otimizada

---

## 📈 **PROGRESSO DAS EPICS**

### **📊 Status Geral**
- **Epic 19**: ✅ **ARQUIVADA** (8/8 tasks - 100%) - Melhoria Completa da Qualidade da Wiki
- **Epic 20**: ✅ **ARQUIVADA** (8/8 tasks - 100%) - Sistema Centralizado de Linkagem e Organização
- **Epic 21**: ✅ **ARQUIVADA** (5/5 tasks - 100%) - Sistema Avançado de Integração e Otimização
- **Epic 22**: 🔄 **EM ANDAMENTO** (5/5 tasks - 0%) - Reorganização Completa de Diretórios
- **Tasks Concluídas**: 21/26 (80.8%)
- **Tasks Pendentes**: 5/26 (19.2%)
- **Tempo Estimado Restante**: 72 horas
- **Status**: 🔄 **EPIC 22 EM ANDAMENTO**

### **🎯 Próximos Passos**
1. **✅ Epics 19-21 Arquivadas**: Todas as melhorias anteriores concluídas com sucesso
2. **🔄 Epic 22 Ativa**: Foco total na reorganização de diretórios
3. **📋 Task 22.1**: Limpeza da Raiz e Arquivos Soltos
4. **📋 Task 22.2**: Limpeza e Reorganização da Pasta Wiki
5. **📋 Task 22.3**: Classificação e Organização dos Arquivos .md
6. **📋 Task 22.4**: Criação da Estrutura Final Organizada
7. **📋 Task 22.5**: Atualização de Sistemas e Validação

---

## 🔧 **FERRAMENTAS DISPONÍVEIS**

### **🔍 Scripts Criados**
- **Análise de Diretórios**: `wiki/update/directory_analysis.py`
- **Classificação de Arquivos**: `wiki/update/file_classification_system.py`
- **Migração Automática**: `wiki/update/automatic_migration_system.py`
- **Validação de Estrutura**: `wiki/update/structure_validation.py`
- **Atualização de Caminhos**: `wiki/update/path_updater.py`
- **Backup Automático**: `wiki/update/backup_system.py`

### **📊 Relatórios Disponíveis**
- **Mapeamento de Diretórios**: `wiki/diretorios.md` - Análise completa da estrutura atual
- **Problemas Identificados**: 2.178 arquivos .md espalhados, pasta wiki bagunçada
- **Plano de Reorganização**: 5 fases estruturadas para limpeza completa
- **Estrutura Final**: Definição clara de propósito de cada pasta

---

> [!success] **EPIC 22 ATIVA**
> 🔄 **Status**: Epic 22 em andamento (5/5 tasks - 0%)
> 🎯 **Foco**: Reorganização Completa de Diretórios e Estrutura do Projeto
> 📚 **Histórico**: Epics 19-21 arquivadas com sucesso

> [!info] **REORGANIZAÇÃO ESTRUTURAL**
> ✅ **Objetivo**: Limpar e organizar toda a estrutura do projeto
> ✅ **Foco**: Separar conteúdo educacional de sistemas internos
> ✅ **Resultado**: Estrutura clara, navegável e escalável
> 🎯 **Status**: Epic 22 em execução

---

## 🔗 **Links Automáticos**

> [!info] **Links Gerados Automaticamente**
> Estes links foram criados automaticamente pelo sistema de linkagem da categoria **Task_Management**

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]
- [[../diretorios|Plano de Reorganização de Diretórios]]

### **🧭 Navegação**
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]
- [[../maps/category_indices|Índices por Categoria]]
- [[../maps/relationships|Relacionamentos]]

### **📊 Métricas da Categoria**
- **Categoria**: Task_Management
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

## 🔗 **Integração com Sistemas**

> [!tip] **Hub Central**
> - [[../README|Hub Central da Wiki]]

> [!important] **Sistemas de Automação**
> - [[../bmad/README|Sistema BMAD]]
> - [[../habdel/README|Sistema Habdel]]

> [!example] **Guias e Documentação**
> - [[../Sistema_Orquestracao_Inteligente_Guia|Guia de Orquestração]]
> - [[../GLOSSARIO_TERMINOLOGIA_TECNICA|Glossário Técnico]]

> [!info] **Relatórios**
> - [[../Sistema_OTClient_BMAD_Relatorio_Geral|Relatório Geral]]
> - [[../Relatorio_Qualidade_Linkagem|Relatório de Qualidade]]

---
