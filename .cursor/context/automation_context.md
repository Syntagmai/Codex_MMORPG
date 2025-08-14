# Contexto: Automação (Git e Python)

Este arquivo contém as regras e diretrizes para automação de scripts Python, controle de versão Git e resolução automática de erros.

---

## 🐍 Automação Python

### **Execução de Scripts:**
- **Fluxo padrão**: `cursor.md` → `scripts/script_execution_manager.py` → `scripts/python_error_resolver.py` → script.py
- Scripts Python com resolução automática de erros
- Modo fallback para scripts que falham

### **Resolução Automática de Erros:**
- **Detecção automática** de tipos de erro em scripts Python
- **Correção automática** de imports, sintaxe e encoding
- **Modo fallback** para scripts que falham
- **Log detalhado** de resoluções e estatísticas

### **Python Agent Especializado:**
- Agente Python especializado em desenvolvimento e qualidade
- Resolução automática para scripts Python que falham na execução
- Integração com sistema de agentes BMAD

---

## 🔧 Automação Git

### **Controle de Versão:**
- **@git** - Operações de controle de versão (automação Git)
- Automação de controle de versão integrada ao sistema
- Boas práticas de Git aplicadas automaticamente

### **Integração Git-Task Manager:**
- Sistema integrado entre Git e Task Manager
- Automação de commits baseada em conclusão de tarefas
- Controle de versão sincronizado com progresso de tarefas

### **Submódulos Git:**
- Gerenciamento automático dos três submódulos:
  - `otclient/` - Cliente OTClient
  - `canary/` - Servidor Canary  
  - `forgottenmapeditor/` - Editor de mapa
- Sincronização automática entre repositórios

---

## 📁 Organização Automática de Arquivos

### **Limpeza e Organização:**
- **Identifique** arquivos temporários após conclusão de tarefas
- **Mova** relatórios de conclusão para `logs/`
- **Mantenha** apenas arquivos essenciais no sistema
- **Organize** relatórios com estrutura padronizada
- **Inclua** receitas para reproduzir resultados

### **Manutenção Automática:**
- **Organize arquivos automaticamente** por categoria e data
- **Remova arquivos temporários** e duplicatas automaticamente
- **Preserve conhecimento importante** em estrutura organizada
- **Mantenha sistema sempre limpo** usando agente de organização inteligente

---

## 🔄 Automação de Tarefas

### **Execução Passo a Passo:**
- **Automatize tarefas** criando tarefas temporárias
- **Execute passo a passo** com relatórios de progresso
- **Gere relatórios finais** automaticamente
- **Atualize Task Master** após cada tarefa concluída

### **Workflow Automatizado:**
1. Criar tarefas temporárias baseadas no pedido
2. Executar cada passo com validação
3. Gerar relatório de conclusão
4. Atualizar sistemas de tarefa apropriados
5. Limpar arquivos temporários

---

## 📚 Referências Completas

Para detalhes completos sobre automação, consulte:
- `@.cursor/rules/git-automation-rules.md`
- `@.cursor/rules/python-agent-rules.md`  
- `@.cursor/rules/task-automation-rules.md`
- `@.cursor/rules/git-task-manager-integration-rules.md`
- `@.cursor/rules/report-cleanup-rules.md`
- `@scripts/script_execution_manager.py`
- `@scripts/python_error_resolver.py`
