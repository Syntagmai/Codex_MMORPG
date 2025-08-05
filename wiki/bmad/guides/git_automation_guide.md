---
tags: [bmad, guide, git, automation, commit, best-practices, portuguese]
type: guide
aliases: [Git Automation Guide, Guia de Automação Git, Guia Git]
status: active
---

# Guia de Automação Git - Sistema BMAD

## 📋 Visão Geral

Este guia apresenta o **Sistema de Automação Git** integrado ao BMAD, que permite commits automáticos com boas práticas em português durante o desenvolvimento.

### 🎯 **Funcionalidades Principais**
- ✅ **Commits automáticos** com validação de qualidade
- ✅ **Mensagens em português** seguindo Conventional Commits
- ✅ **Integração com tarefas** BMAD
- ✅ **Validação automática** de boas práticas
- ✅ **Atalhos de teclado** no Cursor IDE
- ✅ **Hooks de pre-commit** configurados

---

## 🚀 **Como Usar**

### **1. Commit Automático Básico**

```bash
# Commit automático simples
python wiki/bmad/agents/git_automation_agent.py --auto-commit

# Saída esperada:
# ✅ Commit realizado com sucesso!
# 📝 Mensagem: feat: modificados 3 arquivos
# 📊 Score: 95/100
```

### **2. Commit com Push Automático**

```bash
# Commit + Push automático
python wiki/bmad/agents/git_automation_agent.py --auto-commit --push

# Saída esperada:
# ✅ Commit realizado com sucesso!
# 🚀 Push realizado!
```

### **3. Integração com Tarefas**

```bash
# Commit com contexto de tarefa
python wiki/update/git_task_integration.py --auto-commit

# Saída esperada:
# ✅ Commit realizado com sucesso!
# 🎯 Tarefa: TASK-003
# 📋 Título: Sistema de Automação Git Inteligente
```

### **4. Análise de Mudanças**

```bash
# Apenas analisar mudanças
python wiki/bmad/agents/git_automation_agent.py --analyze

# Saída esperada:
# 📋 Tipo: feat
# 📝 Resumo: modificados 2 arquivos, adicionados 1 arquivo
# 🎯 Tarefa Ativa: TASK-003
```

### **5. Validação Manual**

```bash
# Validar mensagem específica
python wiki/bmad/agents/git_automation_agent.py --validate "feat: nova funcionalidade"

# Saída esperada:
# 📊 Score: 85/100
# ✅ Válido: True
# ⚠️ Avisos: Primeira linha muito longa
```

---

## ⌨️ **Atalhos de Teclado**

### **Atalhos Principais**
- **`Ctrl+Shift+G`**: Commit automático básico
- **`Ctrl+Shift+P`**: Commit + Push automático
- **`Ctrl+Shift+T`**: Commit com contexto de tarefa
- **`Ctrl+Shift+R`**: Relatório da tarefa ativa
- **`Ctrl+Shift+S`**: Estatísticas da tarefa
- **`Ctrl+Shift+A`**: Análise de mudanças

### **Como Usar**
1. Abra o terminal integrado no Cursor IDE
2. Pressione o atalho desejado
3. O comando será executado automaticamente
4. Veja o resultado no terminal

---

## 📊 **Relatórios e Estatísticas**

### **Relatório de Tarefa**

```bash
# Gerar relatório da tarefa ativa
python wiki/update/git_task_integration.py --report

# Saída esperada:
# 📊 Relatório de Commits da Tarefa:
# ==================================================
# ## 📝 **Commits Automáticos**
# 
# ### Commit: 2024-12-19T15:45:30
# - **Mensagem**: feat: implementar agente de automação Git - TASK-003
# - **Tipo**: feat
# - **Score**: 95/100
# - **Status**: ✅ Sucesso
# - **Push**: ❌ Não
```

### **Estatísticas da Tarefa**

```bash
# Mostrar estatísticas
python wiki/update/git_task_integration.py --stats

# Saída esperada:
# 📈 Estatísticas da Tarefa:
# ==============================
# 📝 Total de commits: 5
# ✅ Commits bem-sucedidos: 5
# ❌ Commits com erro: 0
# 📊 Taxa de sucesso: 100.0%
# 🎯 Score médio: 92.5/100
```

---

## 🎯 **Padrões de Mensagens**

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

### **Tipos de Commit Disponíveis**
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

## 🔧 **Configuração**

### **Configurações do Cursor IDE**

O sistema já está configurado automaticamente com as seguintes configurações:

#### Nível Basic
```json
{
  "git.automation.enabled": true,
  "git.automation.language": "portuguese",
  "git.automation.conventionalCommits": true,
  "git.automation.autoCommit": true,
  "git.automation.autoPush": false,
  "git.automation.validation": true,
  "git.automation.taskIntegration": true
}
```

#### Nível Intermediate
```json
{
  "git.automation.enabled": true,
  "git.automation.language": "portuguese",
  "git.automation.conventionalCommits": true,
  "git.automation.autoCommit": true,
  "git.automation.autoPush": false,
  "git.automation.validation": true,
  "git.automation.taskIntegration": true
}
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```json
{
  "git.automation.enabled": true,
  "git.automation.language": "portuguese",
  "git.automation.conventionalCommits": true,
  "git.automation.autoCommit": true,
  "git.automation.autoPush": false,
  "git.automation.validation": true,
  "git.automation.taskIntegration": true
}
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

### **Variáveis de Ambiente (Opcional)**

```bash
# Configurações básicas
GIT_AUTO_COMMIT=true
GIT_LANGUAGE=portuguese
GIT_CONVENTIONAL_COMMITS=true

# Configurações avançadas
GIT_AUTO_PUSH=false
GIT_VALIDATION_LEVEL=strict
GIT_INCLUDE_TASK_CONTEXT=true
```

---

## 📋 **Workflow de Desenvolvimento**

### **Fluxo Recomendado**

1. **Iniciar Tarefa**
   ```bash
   # Criar nova tarefa no sistema BMAD
   # O sistema detecta automaticamente
   ```

2. **Desenvolver**
   ```bash
   # Fazer mudanças no código
   # O sistema monitora automaticamente
   ```

3. **Commit Automático**
   ```bash
   # Pressionar Ctrl+Shift+T
   # Ou executar manualmente:
   python wiki/update/git_task_integration.py --auto-commit
   ```

4. **Verificar Progresso**
   ```bash
   # Pressionar Ctrl+Shift+S
   # Ou executar manualmente:
   python wiki/update/git_task_integration.py --stats
   ```

5. **Finalizar Tarefa**
   ```bash
   # O sistema registra todos os commits
   # Relatório automático gerado
   ```

---

## 🚨 **Tratamento de Erros**

### **Erros Comuns e Soluções**

#### **1. Agente Git não encontrado**
```bash
❌ Erro: Agente Git não encontrado

# Solução: Verificar se o arquivo existe
ls wiki/bmad/agents/git_automation_agent.py
```

#### **2. Git não inicializado**
```bash
❌ Erro: Git não inicializado

# Solução: Inicializar repositório
git init
```

#### **3. Conflitos de merge**
```bash
❌ Erro: Conflitos de merge

# Solução: Resolver manualmente
git status
git add .
git commit -m "fix: resolver conflitos de merge"
```

#### **4. Permissões insuficientes**
```bash
❌ Erro: Permissões insuficientes

# Solução: Verificar permissões
# No Windows: Executar como administrador
# No Linux/Mac: chmod +x script.py
```

---

## 📈 **Métricas de Qualidade**

### **Indicadores de Sucesso**
- **Taxa de commits válidos**: > 95%
- **Tempo de criação de commit**: < 30 segundos
- **Conformidade com boas práticas**: > 98%
- **Integração com tarefas**: 100% funcional

### **Score de Qualidade**
- **90-100**: Excelente - Commit perfeito
- **80-89**: Bom - Pequenos ajustes necessários
- **70-79**: Regular - Melhorias recomendadas
- **< 70**: Ruim - Revisão obrigatória

---

## 🔗 **Links Automáticos**

> [!info] **Links Gerados Automaticamente**
> Estes links foram criados automaticamente pelo sistema de linkagem da categoria **BMAD_System**

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]
- [[../bmad/README|Sistema BMAD]]
- [[../maps/bmad_agents_index|Índice de Agentes]]

### **🧭 Navegação**
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]
- [[../maps/category_indices|Índices por Categoria]]
- [[../maps/relationships|Relacionamentos]]

### **📊 Métricas da Categoria**
- **Categoria**: BMAD_System
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

## 🔗 **Integração com Sistema BMAD**

### **Agentes Relacionados**
- **Task Automation Agent**: Coordenação de tarefas
- **Documentation Agent**: Commits de documentação
- **Quality Agent**: Validação de qualidade

### **Workflows Integrados**
- **Git Auto Commit**: Commit automático básico
- **Git Validation**: Validação de mensagens
- **Git Integration**: Integração com tarefas

---

## 💡 **Dicas e Melhores Práticas**

### **1. Use Atalhos de Teclado**
- Mais rápido que comandos manuais
- Menos propenso a erros
- Integração perfeita com IDE

### **2. Monitore Estatísticas**
- Verifique regularmente o score médio
- Identifique padrões de qualidade
- Melhore continuamente

### **3. Mantenha Tarefas Ativas**
- O sistema detecta automaticamente
- Contexto preservado nos commits
- Rastreabilidade completa

### **4. Valide Antes de Commitar**
- Use `--validate` para mensagens manuais
- Verifique score antes de prosseguir
- Corrija problemas identificados

---

## 🆘 **Suporte e Troubleshooting**

### **Comandos de Diagnóstico**

```bash
# Verificar saúde do sistema
python wiki/bmad/agents/git_automation_agent.py --analyze

# Verificar integração com tarefas
python wiki/update/git_task_integration.py --stats

# Validar configurações
python wiki/bmad/agents/git_automation_agent.py --validate "teste"
```

### **Logs do Sistema**
- **Agente Git**: `git_automation.log`
- **Integração**: `git_task_integration.log`
- **Pre-commit**: Terminal do Git

### **Contatos de Suporte**
- **Documentação**: Este guia
- **Logs**: Arquivos de log mencionados
- **Sistema BMAD**: Agentes especializados

---

## 🔄 **Atualizações**

### **Histórico de Versões**
- **v1.0**: Versão inicial com automação básica
- **v1.1**: Adicionado Conventional Commits
- **v1.2**: Integração com sistema de tarefas
- **v1.3**: Atalhos de teclado e hooks

### **Próximas Melhorias**
- IA para geração de mensagens mais inteligentes
- Integração com sistemas de review
- Dashboard de métricas de commits
- Automação de branch management

---

*Guia criado pelo Sistema BMAD - OTClient Documentation* 