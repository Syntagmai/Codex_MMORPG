---
tags: [organização, estrutura, diretórios, reorganização, limpeza]
type: organização
status: em_planejamento
priority: crítica
created: 2025-01-27
---

# 📁 **MAPEAMENTO COMPLETO DE DIRETÓRIOS - PLANO DE REORGANIZAÇÃO**

## 🎯 **OBJETIVO**

Este documento mapeia **TODA** a estrutura de diretórios do projeto para planejar uma reorganização completa. O objetivo é:

1. **Identificar** o que cada pasta contém
2. **Classificar** por tipo de conteúdo
3. **Planejar** migração para estrutura organizada
4. **Manter** apenas conteúdo educacional na pasta `wiki/` (para Obsidian)

---

## ⚠️ **PASTAS IMUTÁVEIS (NÃO MEXER)**

### 🔒 **Código-Fonte Principal**
- **`otclient/`** - Código-fonte do OTClient (somente leitura)
- **`canary/`** - Código-fonte do Canary (somente leitura)
- **`forgottenmapeditor/`** - Editor de mapa integrado (somente leitura)

---

## 📊 **ESTRUTURA ATUAL - MAPEAMENTO COMPLETO**

### 🏠 **RAIZ DO PROJETO**

#### **📁 Pastas Principais (Criadas pelo BMAD)**
| Pasta | Status | Conteúdo | Propósito |
|-------|--------|----------|-----------|
| **`src/`** | ✅ Vazia | `.gitkeep` | Código fonte principal |
| **`tests/`** | ✅ Vazia | `.gitkeep` | Testes unitários |
| **`docs/`** | ✅ Ativa | `gui_system/`, `src/`, `index.html`, `book.toml` | Documentação técnica |
| **`config/`** | ✅ Vazia | `.gitkeep` | Arquivos de configuração |
| **`logs/`** | ✅ Vazia | `.gitkeep` | Arquivos de log |
| **`temp/`** | ✅ Vazia | `.gitkeep` | Arquivos temporários |
| **`backup/`** | ✅ Vazia | `.gitkeep` | Backups automáticos |
| **`assets/`** | ✅ Vazia | `.gitkeep` | Recursos estáticos |
| **`data/`** | ✅ Vazia | `.gitkeep` | Dados do projeto |
| **`scripts/`** | ✅ Vazia | `.gitkeep` | Scripts utilitários |

#### **📁 Pastas Específicas**
| Pasta | Status | Conteúdo | Propósito |
|-------|--------|----------|-----------|
| **`wiki/`** | 🔥 **BAGUNÇADA** | 2.178 arquivos .md + subpastas | **CONTEÚDO EDUCACIONAL** (deveria ser limpa) |
| **`generated/`** | ✅ Ativa | 8 arquivos de ferramentas | Ferramentas geradas automaticamente |
| **`gui_modules/`** | ✅ Ativa | 8 arquivos Python | Módulos GUI do sistema |
| **`free_lance/`** | ✅ Ativa | `cliente_1332_espanhol/` | Projetos freelance |
| **`.cursor/`** | ✅ Ativa | `rules/` (30 regras) | Regras do assistente |
| **`.venv/`** | ✅ Ativa | Ambiente virtual Python | Dependências Python |
| **`.github/`** | ✅ Ativa | Configurações GitHub | CI/CD e workflows |

#### **📄 Arquivos na Raiz (PROBLEMA)**
| Arquivo | Tipo | Deveria ir para |
|---------|------|----------------|
| `charm_error.md` | Relatório | `logs/reports/` |
| `RELATORIO_COMPARATIVO_INVENTARIOS.md` | Relatório | `logs/reports/` |
| `README_LEARNING_WORKFLOW.md` | Documentação | `docs/guides/` |
| `COMO_USAR_SISTEMA_INTELIGENTE.md` | Documentação | `docs/guides/` |
| `README_GUI_SYSTEM.md` | Documentação | `docs/guides/` |
| `audit_file_structure.py` | Script | `scripts/` |
| `activate_complete_system.sh` | Script | `scripts/` |
| `learn_command.py` | Script | `scripts/` |
| `build_exe_simple.bat` | Script | `scripts/` |
| `quick_unicode_fix.py` | Script | `scripts/` |
| `bmad_system_gui_integrated.py` | Script | `scripts/` |
| `unicode_aliases.py` | Script | `scripts/` |
| `unicode_fix.py` | Script | `scripts/` |
| `chat_learning_integration.py` | Script | `scripts/` |
| `README.md.backup` | Backup | `backup/` |

---

### 📚 **PASTA WIKI (PROBLEMA PRINCIPAL)**

#### **📁 Subpastas da Wiki**
| Pasta | Status | Conteúdo | Propósito |
|-------|--------|----------|-----------|
| **`wiki/wiki/`** | ❌ **REDUNDANTE** | `bmad/`, `docs.backup/`, `log/`, `dashboard/` | Pasta duplicada |
| **`wiki/log/`** | ❌ **PROBLEMA** | 100+ arquivos de relatório | Deveria estar em `logs/` |
| **`wiki/backup/`** | ❌ **PROBLEMA** | Backups | Deveria estar em `backup/` |
| **`wiki/config.backup/`** | ❌ **PROBLEMA** | Backup de config | Deveria estar em `config/backup/` |
| **`wiki/certificates.backup/`** | ❌ **PROBLEMA** | Certificados | Deveria estar em `config/certificates/` |
| **`wiki/teste/`** | ❌ **PROBLEMA** | Testes | Deveria estar em `temp/test/` |
| **`wiki/legacy_docs/`** | ❌ **PROBLEMA** | Docs antigas | Deveria estar em `docs/legacy/` |
| **`wiki/templates/`** | ❌ **PROBLEMA** | Templates | Deveria estar em `docs/templates/` |
| **`wiki/dashboard/`** | ❌ **PROBLEMA** | Sistema de tarefas | Deveria estar em `docs/dashboard/` |
| **`wiki/bmad/`** | ❌ **PROBLEMA** | Sistema BMAD | Deveria estar em `docs/bmad/` |
| **`wiki/integration/`** | ✅ **OK** | Integração OTClient-Canary | Pode ficar na wiki (conhecimento cruzado) |
| **`wiki/maps/`** | ❌ **PROBLEMA** | Mapas JSON | Deveria estar em `data/maps/` |
| **`wiki/update/`** | ❌ **PROBLEMA** | Scripts de atualização | Deveria estar em `scripts/` |
| **`wiki/tools/`** | ❌ **PROBLEMA** | Ferramentas | Deveria estar em `scripts/` |
| **`wiki/monitoring/`** | ❌ **PROBLEMA** | Monitoramento | Deveria estar em `logs/monitoring/` |
| **`wiki/ml/`** | ❌ **PROBLEMA** | Machine Learning | Deveria estar em `docs/ml/` |
| **`wiki/educational/`** | ✅ **OK** | Sistema educacional | Pode ficar na wiki |
| **`wiki/alerts/`** | ❌ **PROBLEMA** | Alertas | Deveria estar em `logs/alerts/` |
| **`wiki/metrics/`** | ❌ **PROBLEMA** | Métricas | Deveria estar em `logs/metrics/` |
| **`wiki/consolidated/`** | ❌ **PROBLEMA** | Dados consolidados | Deveria estar em `data/consolidated/` |
| **`wiki/workflows/`** | ❌ **PROBLEMA** | Workflows BMAD | Deveria estar em `docs/workflows/` |
| **`wiki/habdel/`** | ❌ **PROBLEMA** | Sistema Habdel | Deveria estar em `habdel/` |
| **`wiki/cursor_core/`** | ❌ **PROBLEMA** | Sistema de desenvolvimento de jogos | Deveria estar em `docs/game-development/` |

#### **📄 Arquivos .md na Wiki (PROBLEMA)**
| Tipo de Arquivo | Quantidade | Deveria ir para |
|-----------------|------------|----------------|
| **Relatórios** | ~50 arquivos | `logs/reports/` |
| **Índices** | ~15 arquivos | `docs/indexes/` |
| **Guias internos** | ~10 arquivos | `docs/guides/` |
| **Glossários** | ~5 arquivos | `docs/glossary/` |
| **Sistemas internos** | ~20 arquivos | `docs/systems/` |
| **Metodologia Habdel** | ~100 arquivos | `habdel/` |
| **Documentação final** | ~100 arquivos | `wiki/` (manter) |
| **Arquivos órfãos** | ~1.800 arquivos | **ANALISAR E ORGANIZAR** |

---

## 🎯 **PLANO DE REORGANIZAÇÃO**

### **📋 FASE 1: LIMPEZA DA RAIZ**
1. **Mover relatórios** da raiz para `logs/reports/`
2. **Mover scripts** da raiz para `scripts/`
3. **Mover documentação** da raiz para `docs/`
4. **Mover backups** da raiz para `backup/`

### **📋 FASE 2: LIMPEZA DA WIKI**
1. **Remover pasta redundante** `wiki/wiki/`
2. **Mover relatórios** de `wiki/log/` para `logs/`
3. **Mover backups** de `wiki/backup/` para `backup/`
4. **Mover scripts** de `wiki/update/` e `wiki/tools/` para `scripts/`
5. **Mover monitoramento** de `wiki/monitoring/` para `logs/monitoring/`
6. **Mover ML** de `wiki/ml/` para `docs/ml/`
7. **Mover alertas** de `wiki/alerts/` para `logs/alerts/`
8. **Mover métricas** de `wiki/metrics/` para `logs/metrics/`
9. **Mover dados consolidados** de `wiki/consolidated/` para `data/consolidated/`
10. **Mover cursor core** de `wiki/cursor_core/` para `docs/game-development/`
11. **Mover dashboard** de `wiki/dashboard/` para `docs/dashboard/`
12. **Mover templates** de `wiki/templates/` para `docs/templates/`
13. **Mover BMAD** de `wiki/bmad/` para `docs/bmad/`
14. **Manter integration** em `wiki/integration/` (conhecimento cruzado OTClient-Canary)
15. **Mover maps** de `wiki/maps/` para `data/maps/`
16. **Mover workflows** de `wiki/workflows/` para `docs/workflows/`
17. **Mover habdel** de `wiki/habdel/` para `habdel/` (pasta própria)
18. **Manter apenas** `wiki/educational/`, `wiki/integration/` e conteúdo educacional

### **📋 FASE 3: ORGANIZAÇÃO DOS ARQUIVOS .md**
1. **Classificar** todos os 2.178 arquivos .md
2. **Separar** relatórios de documentação
3. **Organizar** por categorias
4. **Manter** apenas documentação final na wiki

#### **📚 DISTINÇÃO CLARA DE CONTEÚDO:**

##### **📁 Pasta `habdel/` (METODOLOGIA DE PESQUISA)**
- **Stories** de pesquisa profunda
- **Metodologia** de extração de informações
- **Técnicas** de análise de código-fonte
- **Processos** de documentação estruturada
- **Guias** de como fazer pesquisa eficiente

##### **📚 Pasta `wiki/` (PRODUTO FINAL - APENAS WIKI EDUCACIONAL)**
- **Guias** de uso do OTClient/Canary (educacionais)
- **Cursos** e lições estruturadas
- **Material de estudo** do Canary, OTClient
- **Integração** OTClient-Canary (conhecimento cruzado)
- **Protocolos** OpenCode e Extended OpenCode (explicados)
- **Documentação** de banco de dados a interface (para aprendizado)
- **Conteúdo educacional** gerado por agentes professores
- **Apenas arquivos .md** para Obsidian
- **Nada de sistemas, relatórios ou ferramentas**

##### **📖 Pasta `docs/` (DOCUMENTAÇÃO INTERNA)**
- **Guias** do sistema BMAD
- **Manuais** dos agentes
- **Documentação técnica** interna
- **Workflows** de desenvolvimento
- **Templates** e padrões
- **Sistema de desenvolvimento de jogos** (game-development)

### **📋 FASE 4: ESTRUTURA FINAL**
1. **`wiki/`** = Apenas conteúdo educacional (Obsidian)
2. **`habdel/`** = Metodologia de pesquisa e stories
3. **`docs/`** = Documentação interna do sistema
   - **`docs/bmad/`** = Sistema BMAD (organização e documentação)
   - **`docs/game-development/`** = Sistema de desenvolvimento de jogos
   - **`docs/dashboard/`** = Sistema de tarefas
   - **`docs/templates/`** = Templates e padrões
   - **`docs/workflows/`** = Workflows de desenvolvimento
4. **`logs/`** = Todos os relatórios e logs
5. **`scripts/`** = Todos os scripts e ferramentas
6. **`config/`** = Configurações e certificados
7. **`backup/`** = Todos os backups
8. **`temp/`** = Arquivos temporários
9. **`data/`** = Dados consolidados e mapas
10. **`assets/`** = Recursos estáticos
11. **`src/`** = Código fonte (quando necessário)
12. **`tests/`** = Testes (quando necessário)

### **📋 FASE 5: ATUALIZAÇÃO DE SISTEMAS**
1. **Atualizar scripts** (todos os .py, .sh, .bat) com novos caminhos
2. **Atualizar regras** do sistema sobre diretórios
3. **Atualizar mapas JSON** para navegação fluida
4. **Atualizar README.md** explicando nova estrutura
5. **Validar** funcionamento de todos os sistemas

---

## 🚨 **PROBLEMAS IDENTIFICADOS**

### **❌ Problemas Críticos:**
1. **Pasta `wiki/wiki/`** redundante
2. **2.178 arquivos .md** espalhados
3. **Relatórios misturados** com documentação
4. **Scripts na raiz** em vez de `scripts/`
5. **Backups espalhados** em vez de `backup/`
6. **Logs na wiki** em vez de `logs/`

### **⚠️ Problemas Médios:**
1. **Arquivos .md** não categorizados
2. **Estrutura inconsistente** entre pastas
3. **Nomenclatura** não padronizada
4. **Conteúdo duplicado** em várias pastas

### **✅ Pontos Positivos:**
1. **Pastas organizacionais** criadas pelo BMAD
2. **Sistema de tarefas** bem estruturado
3. **Sistema BMAD** funcionando
4. **Documentação técnica** em `docs/`

---

## 📝 **PRÓXIMOS PASSOS**

1. **Aprovar** este mapeamento
2. **Definir** prioridades de reorganização
3. **Criar** script de migração automática
4. **Executar** limpeza fase por fase
5. **Validar** estrutura final
6. **Atualizar** todos os sistemas (scripts, regras, mapas)
7. **Documentar** nova organização no README.md

## 🔧 **DETALHAMENTO DA FASE 5 - ATUALIZAÇÃO DE SISTEMAS**

### **📝 Scripts a Atualizar:**
- **Todos os .py** em `scripts/`, `wiki/update/`, `wiki/tools/`
- **Todos os .sh** na raiz e em `scripts/`
- **Todos os .bat** na raiz e em `scripts/`
- **Scripts BMAD** em `wiki/bmad/agents/`
- **Scripts Game Development** em `wiki/cursor_core/.bmad-game-core/`

### **📋 Regras a Atualizar:**
- **`.cursor/rules/`** - Todas as regras sobre diretórios
- **`cursor.md`** - Orquestrador principal
- **Regras específicas** de organização

### **🗺️ Mapas JSON a Atualizar:**
- **`wiki/maps/`** - Todos os mapas de navegação
- **Índices** de arquivos e pastas
- **Relacionamentos** entre documentos

### **📖 README.md a Atualizar:**
- **Estrutura** do projeto
- **Propósito** de cada pasta
- **Como navegar** no projeto
- **Sistemas** disponíveis

---

> [!info] **NOTA IMPORTANTE**
> Este documento será atualizado conforme a reorganização avança. Cada fase deve ser executada e validada antes de prosseguir para a próxima.

> [!warning] **BACKUP OBRIGATÓRIO**
> Antes de qualquer reorganização, fazer backup completo do projeto para evitar perda de dados. 