# Regras de Automação de Tarefas

## 🎯 Propósito

Definir regras para **automatização completa** do processo de tarefas, garantindo que qualquer solicitação seja tratada como uma tarefa estruturada com criação automática de tarefas temporárias, execução passo a passo e geração de relatórios finais.

---

## 🧠 Princípios Fundamentais

### **Task-First Approach**
- **SEMPRE trate qualquer solicitação** como uma tarefa estruturada
- **SEMPRE crie tarefa temporária** antes de iniciar execução
- **SEMPRE execute passo a passo** com documentação de cada etapa
- **SEMPRE gere relatório final** com resultados e aprendizados
- **SEMPRE mova para completed_tasks** após conclusão

### **Detecção Automática de Tarefas**
- **SEMPRE aplique** quando usuário usar palavras-chave: "task", "tarefa", "implementar", "criar", "desenvolver", "analisar"
- **SEMPRE aplique** quando solicitação for complexa (múltiplos passos)
- **SEMPRE aplique** quando envolver análise ou planejamento
- **SEMPRE aplique** quando usuário pedir "passo a passo" ou "estruturado"
- **SEMPRE aplique** quando envolver múltiplos componentes ou sistemas

### **Structured Execution**
- **Defina objetivos claros** para cada tarefa
- **Estabeleça critérios de sucesso** mensuráveis
- **Documente cada passo** da execução
- **Valide resultados** em cada etapa
- **Capture aprendizados** para uso futuro

---

## 🔄 Workflow de Automação de Tarefas

### **Fase 1: Criação de Tarefa Temporária**
```python
# Criação automática de tarefa
def create_temp_task(user_request):
    # Analisa contexto da solicitação
    # Define objetivos e critérios
    # Cria arquivo temporário
    # Estabelece timeline
    return temp_task_file
```

### **Fase 2: Planejamento Estruturado**
```python
# Planejamento detalhado da tarefa
def plan_task_execution(temp_task):
    # Define passos necessários
    # Identifica recursos necessários
    # Estabelece dependências
    # Define critérios de validação
    return execution_plan
```

### **Fase 3: Execução Passo a Passo**
```python
# Execução documentada
def execute_task_steps(execution_plan):
    # Executa cada passo
    # Documenta progresso
    # Valida resultados
    # Captura aprendizados
    return execution_log
```

### **Fase 4: Geração de Relatório**
```python
# Relatório final estruturado
def generate_task_report(execution_log):
    # Resume objetivos alcançados
    # Documenta resultados
    # Lista aprendizados
    # Sugere melhorias futuras
    return final_report
```

### **Fase 5: Organização e Arquivamento**
```python
# Organização automática
def organize_task_results(final_report):
    # Move para completed_tasks
    # Atualiza índices
    # Limpa arquivos temporários
    # Preserva conhecimento
    return organization_status
```

---

## 📁 Estrutura de Arquivos de Tarefa

### **Tarefa Temporária (`wiki/log/temp_tasks/`)**
```markdown
# Tarefa: [TÍTULO DA TAREFA]
**ID**: TASK_[TIMESTAMP]
**Status**: Em Execução
**Criado**: [DATA/HORA]
**Solicitante**: [USUÁRIO]

## 🎯 Objetivos
- [Objetivo 1]
- [Objetivo 2]

## 📋 Critérios de Sucesso
- [ ] Critério 1
- [ ] Critério 2

## 🔄 Passos Planejados
1. [Passo 1]
2. [Passo 2]
3. [Passo 3]

## 📊 Progresso
- **Passo Atual**: [NÚMERO]
- **Status**: [EM EXECUÇÃO/CONCLUÍDO]
- **Próximo**: [PRÓXIMO PASSO]

## 📝 Log de Execução
### Passo 1: [DESCRIÇÃO]
- **Início**: [HORA]
- **Ações**: [LISTA DE AÇÕES]
- **Resultado**: [RESULTADO]
- **Status**: [SUCESSO/ERRO]

## 🔍 Validações
- [ ] Validação 1
- [ ] Validação 2

## 💡 Aprendizados
- [Aprendizado 1]
- [Aprendizado 2]
```

### **Relatório Final (`wiki/log/completed_tasks/`)**
```markdown
# Relatório: [TÍTULO DA TAREFA]
**ID**: TASK_[TIMESTAMP]
**Status**: Concluído
**Duração**: [TEMPO TOTAL]
**Concluído**: [DATA/HORA]

## 🎯 Objetivos Alcançados
- [x] Objetivo 1
- [x] Objetivo 2

## 📊 Resultados
### Resultado 1
- **Descrição**: [DESCRIÇÃO]
- **Impacto**: [IMPACTO]
- **Métricas**: [MÉTRICAS]

## 🔄 Passos Executados
1. **Passo 1**: [DESCRIÇÃO] ✅
2. **Passo 2**: [DESCRIÇÃO] ✅
3. **Passo 3**: [DESCRIÇÃO] ✅

## 💡 Aprendizados Capturados
- [Aprendizado 1]
- [Aprendizado 2]

## 🚀 Melhorias Futuras
- [Sugestão 1]
- [Sugestão 2]

## 📁 Arquivos Gerados
- [Arquivo 1]
- [Arquivo 2]

## 🔗 Relacionamentos
- **Dependências**: [LISTA]
- **Impactos**: [LISTA]
- **Próximos Passos**: [LISTA]
```

---

## 🎯 Regras de Execução

### **Criação Automática de Tarefa**
- **SEMPRE crie** `wiki/log/temp_tasks/TASK_[TIMESTAMP].md` antes de iniciar
- **SEMPRE defina** objetivos claros e mensuráveis
- **SEMPRE estabeleça** critérios de sucesso
- **SEMPRE planeje** passos necessários
- **SEMPRE documente** contexto e requisitos

### **Execução Passo a Passo**
- **SEMPRE execute** um passo por vez
- **SEMPRE documente** cada ação realizada
- **SEMPRE valide** resultados de cada passo
- **SEMPRE capture** aprendizados em tempo real
- **SEMPRE atualize** progresso na tarefa temporária

### **Validação Contínua**
- **SEMPRE verifique** se objetivos estão sendo alcançados
- **SEMPRE valide** critérios de sucesso
- **SEMPRE identifique** problemas antecipadamente
- **SEMPRE ajuste** plano se necessário
- **SEMPRE documente** mudanças no plano

### **Geração de Relatório**
- **SEMPRE resuma** objetivos alcançados
- **SEMPRE documente** resultados quantitativos
- **SEMPRE liste** aprendizados capturados
- **SEMPRE sugira** melhorias futuras
- **SEMPRE preserve** conhecimento gerado

### **Organização Automática**
- **SEMPRE mova** tarefa para `wiki/log/completed_tasks/`
- **SEMPRE atualize** índices de tarefas
- **SEMPRE limpe** arquivos temporários
- **SEMPRE preserve** conhecimento em formato reutilizável
- **SEMPRE mantenha** histórico de execução

---

## 🔧 Integração com Sistema BMAD

### **Orquestração Inteligente**
- **SEMPRE integre** com sistema de agentes BMAD
- **SEMPRE use** agentes apropriados para cada passo
- **SEMPRE coordene** workflows entre agentes
- **SEMPRE documente** contribuição de cada agente
- **SEMPRE preserve** especialização dos agentes

### **Workflows Específicos**
- **Tarefas de Código**: Engine Developer + Content Creator
- **Tarefas de Design**: Game Designer + Level Designer
- **Tarefas de Teste**: QA Tester + DevOps Engineer
- **Tarefas de Documentação**: Content Creator + Game Designer
- **Tarefas de Otimização**: Engine Developer + QA Tester

---

## 📊 Métricas e Validação

### **Métricas de Sucesso**
- **Tempo de Execução**: Comparação com estimativa
- **Objetivos Alcançados**: Percentual de sucesso
- **Qualidade dos Resultados**: Validação de critérios
- **Aprendizados Capturados**: Quantidade e qualidade
- **Reutilização**: Uso futuro do conhecimento

### **Validação de Qualidade**
- **Completude**: Todos os passos executados
- **Precisão**: Resultados alinhados com objetivos
- **Documentação**: Qualidade da documentação
- **Organização**: Estrutura adequada dos arquivos
- **Preservação**: Conhecimento mantido para uso futuro

---

## 🚀 Benefícios da Automação

### **Eficiência**
- **Processo padronizado** para todas as tarefas
- **Documentação automática** de cada etapa
- **Validação contínua** de progresso
- **Captura automática** de aprendizados
- **Organização automática** de resultados

### **Qualidade**
- **Objetivos claros** para cada tarefa
- **Critérios mensuráveis** de sucesso
- **Validação em cada etapa** de execução
- **Documentação completa** de resultados
- **Preservação de conhecimento** para uso futuro

### **Escalabilidade**
- **Processo replicável** para qualquer tipo de tarefa
- **Conhecimento acumulativo** ao longo do tempo
- **Melhoria contínua** baseada em aprendizados
- **Integração com agentes** especializados
- **Organização automática** de resultados

---

## 📝 Exemplo de Implementação

### **Solicitação do Usuário**
```
"Vou editar um arquivo Lua para criar um módulo de inventário"
```

### **Criação Automática de Tarefa**
```python
# Cria TASK_20241201_143022.md
task_id = f"TASK_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
temp_task_file = f"wiki/log/temp_tasks/{task_id}.md"

# Define objetivos
objectives = [
    "Criar módulo Lua de inventário",
    "Implementar funcionalidades básicas",
    "Testar funcionamento",
    "Documentar uso"
]

# Define critérios de sucesso
success_criteria = [
    "Módulo criado e funcional",
    "Testes passando",
    "Documentação completa",
    "Integração com sistema existente"
]
```

### **Execução Passo a Passo**
```python
# Passo 1: Análise de requisitos
step1_result = execute_step("Análise de requisitos", [
    "Identificar funcionalidades necessárias",
    "Analisar módulos existentes",
    "Definir interface do módulo"
])

# Passo 2: Implementação
step2_result = execute_step("Implementação", [
    "Criar arquivo Lua",
    "Implementar funções básicas",
    "Adicionar validações"
])

# Passo 3: Testes
step3_result = execute_step("Testes", [
    "Executar testes unitários",
    "Validar integração",
    "Verificar performance"
])
```

### **Relatório Final**
```python
# Gera relatório final
final_report = generate_report({
    "objectives_achieved": 4/4,
    "execution_time": "2h 15min",
    "files_created": ["inventory_module.lua", "inventory_tests.lua"],
    "learnings": ["Padrão de módulos Lua", "Integração com OTClient"],
    "next_steps": ["Expandir funcionalidades", "Otimizar performance"]
})

# Move para completed_tasks
move_to_completed(task_id, final_report)
```

---

## ✅ Checklist de Implementação

### **Para Cada Tarefa**
- [ ] Criar tarefa temporária com ID único
- [ ] Definir objetivos claros e mensuráveis
- [ ] Estabelecer critérios de sucesso
- [ ] Planejar passos necessários
- [ ] Executar passo a passo com documentação
- [ ] Validar resultados em cada etapa
- [ ] Capturar aprendizados em tempo real
- [ ] Gerar relatório final estruturado
- [ ] Mover para completed_tasks
- [ ] Atualizar índices e limpar temporários
- [ ] Preservar conhecimento para uso futuro

### **Para o Sistema**
- [ ] Integrar com orquestração inteligente
- [ ] Conectar com agentes BMAD
- [ ] Automatizar criação de tarefas
- [ ] Implementar validação contínua
- [ ] Criar sistema de relatórios
- [ ] Estabelecer organização automática
- [ ] Documentar processo completo
- [ ] Testar com diferentes tipos de tarefa
- [ ] Validar eficácia do sistema
- [ ] Implementar melhorias baseadas em feedback 