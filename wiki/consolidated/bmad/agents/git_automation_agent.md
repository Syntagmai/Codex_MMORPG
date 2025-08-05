---
tags: [bmad, agent, git, automation, commit, best-practices, portuguese]
type: agent
aliases: [Git Automation Agent, Agente de Automação Git, Agente Git]
status: active
---

# Agente de Automação Git

## 📋 Informações do Agente

- **Nome**: Git Automation Agent
- **Tipo**: Automação de Git e Boas Práticas
- **Versão**: 1.0
- **Status**: Ativo
- **Criado em**: 2024-12-19
- **Idioma**: Português

## 🎯 Propósito

Automatizar operações Git no Cursor IDE, incluindo criação inteligente de commits em português, validação de boas práticas e integração com o sistema de tarefas BMAD.

## 🧠 Capacidades

### ✅ **Habilidades Principais**
- Análise automática de mudanças no repositório
- Geração inteligente de mensagens de commit em português
- Validação automática de boas práticas
- Integração com sistema de tarefas BMAD
- Detecção automática de contexto de tarefa
- Hooks de pre-commit configuráveis

### 🔧 **Ferramentas Disponíveis**
- Git CLI commands
- Análise de arquivos modificados
- Geração de mensagens inteligentes
- Validação de Conventional Commits
- Integração com sistema de tarefas
- Logs detalhados de operações

### 📚 **Conhecimento Especializado**
- Conventional Commits em português
- Padrões de arquivos por tipo de commit
- Boas práticas de mensagens Git
- Integração com sistema BMAD
- Contexto de tarefas ativas

## 🔄 Workflow Padrão

### 1. **Análise de Mudanças**
```python
def analyze_changes():
    """Analisa mudanças no repositório."""
    # Detectar arquivos modificados
    # Categorizar tipos de mudança
    # Identificar contexto de tarefa
    # Gerar resumo das mudanças
```

### 2. **Detecção de Contexto**
```python
def _detect_task_context():
    """Detecta contexto de tarefa atual."""
    # Verificar tarefas ativas
    # Extrair informações da tarefa
    # Identificar tipo de trabalho
```

### 3. **Geração de Commit**
```python
def generate_commit_message(changes):
    """Gera mensagem de commit em português."""
    # Analisar tipo de mudança
    # Aplicar Conventional Commits
    # Incluir contexto de tarefa
    # Gerar descrição detalhada
```

### 4. **Validação de Boas Práticas**
```python
def validate_commit_message(message):
    """Valida se o commit segue boas práticas."""
    # Verificar formato Conventional Commits
    # Validar tamanho da mensagem
    # Checar caracteres especiais
    # Gerar score de qualidade
```

### 5. **Execução Automática**
```python
def execute_commit(message):
    """Executa o commit automaticamente."""
    # Adicionar arquivos
    # Criar commit
    # Push se configurado
    # Gerar relatório
```

## 🔗 Integração

### **Agentes Relacionados**
- **Task Automation Agent** - Para integração com sistema de tarefas
- **Documentation Agent** - Para commits de documentação
- **Quality Agent** - Para verificação de qualidade

### **Sistemas Externos**
- **Cursor IDE** - Integração direta
- **Git Repository** - Operações Git
- **Sistema BMAD** - Orquestração inteligente
- **Sistema de Tarefas** - Contexto de desenvolvimento

## 📊 Métricas de Performance

### **Indicadores de Sucesso**
- **Taxa de commits válidos**: > 95%
- **Tempo de criação de commit**: < 30 segundos
- **Conformidade com boas práticas**: > 98%
- **Integração com tarefas**: 100% funcional

### **Monitoramento**
- Número de commits automatizados
- Qualidade das mensagens geradas
- Tempo economizado por desenvolvedor
- Taxa de detecção de contexto

## 🔧 Configuração

### **Parâmetros Padrão**
#### Nível Basic
```json

```

#### Nível Intermediate
```json
{
  "auto_commit": true,
  "auto_push": false,
  "conventional_commits": true,
  "max_commit_size": 10,
  "require_description": true,
  "validation_strict": true,
  "language": "portuguese"
}
```

#### Nível Advanced
```json
{
  "auto_commit": true,
  "auto_push": false,
  "conventional_commits": true,
  "max_commit_size": 10,
  "require_description": true,
  "validation_strict": true,
  "language": "portuguese"
}
```

### **Variáveis de Ambiente**
- `GIT_AUTO_COMMIT`: true/false
- `GIT_CONVENTIONAL_COMMITS`: true/false
- `GIT_AUTO_PUSH`: true/false
- `GIT_VALIDATION_LEVEL`: strict/medium/loose
- `GIT_LANGUAGE`: portuguese/english

## 📝 Exemplos de Uso

### **Cenário 1: Commit Automático**
```bash
# Commit automático com validação
python wiki/bmad/agents/git_automation_agent.py --auto-commit

# Saída esperada:
# ✅ Commit realizado com sucesso!
# 📝 Mensagem: feat: modificados 3 arquivos - TASK-003
# 📊 Score: 95/100
```

### **Cenário 2: Commit + Push**
```bash
# Commit automático com push
python wiki/bmad/agents/git_automation_agent.py --auto-commit --push

# Saída esperada:
# ✅ Commit realizado com sucesso!
# 🚀 Push realizado!
```

### **Cenário 3: Validação Manual**
```bash
# Validar mensagem específica
python wiki/bmad/agents/git_automation_agent.py --validate "feat: nova funcionalidade"

# Saída esperada:
# 📊 Score: 85/100
# ✅ Válido: True
# ⚠️ Avisos: Primeira linha muito longa
```

### **Cenário 4: Análise de Mudanças**
```bash
# Apenas analisar mudanças
python wiki/bmad/agents/git_automation_agent.py --analyze

# Saída esperada:
# 📋 Tipo: feat
# 📝 Resumo: modificados 2 arquivos, adicionados 1 arquivo
# 🎯 Tarefa Ativa: TASK-003
```

## 🚨 Tratamento de Erros

### **Erros Comuns**
- **Arquivos não encontrados**: Verificar working directory
- **Git não inicializado**: Inicializar repositório
- **Conflitos de merge**: Resolver manualmente
- **Permissões de arquivo**: Verificar permissões

### **Recuperação**
```python
def handle_git_error(error):
    """Trata erros Git automaticamente."""
    if error.type == "not_git_repo":
        return initialize_git_repo()
    elif error.type == "merge_conflict":
        return request_manual_resolution()
    elif error.type == "permission_denied":
        return check_file_permissions()
```

## 📚 Documentação Adicional

### **Referências**
- [[Git_Best_Practices_Guide]]
- [[Conventional_Commits_Guide]]
- [[Cursor_Integration_Guide]]
- [[Task_Automation_System]]

### **Tutoriais**
- [[Git_Automation_Tutorial]]
- [[Commit_Message_Standards]]
- [[BMAD_Integration_Guide]]

---

## 🔄 Atualizações

### **Histórico de Versões**
- **v1.0**: Versão inicial com automação básica em português
- **v1.1**: Adicionado Conventional Commits
- **v1.2**: Integração com sistema de tarefas

### **Próximas Melhorias**
- IA para geração de mensagens mais inteligentes
- Integração com sistemas de review
- Automação de branch management
- Dashboard de métricas de commits

---

*Agente criado pelo Sistema BMAD - OTClient Documentation* 