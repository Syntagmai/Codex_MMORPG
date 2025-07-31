# Regras de Limpeza e Organização de Relatórios

## 🎯 Propósito

Definir regras para **limpeza automática** de arquivos temporários e **organização estruturada** de relatórios de conclusão na pasta `wiki/log/`, incluindo receitas para reproduzir resultados.

---

## 🧹 Princípios de Limpeza

### **Arquivos Temporários**
- **SEMPRE identifique** arquivos temporários após conclusão de tarefas
- **SEMPRE mova** relatórios de conclusão para `wiki/log/`
- **SEMPRE mantenha** apenas arquivos essenciais no sistema
- **SEMPRE organize** relatórios com estrutura padronizada
- **SEMPRE inclua** receitas para reproduzir resultados

### **Arquivos de Tarefas**
- **SEMPRE arquive** arquivos de tarefas concluídas
- **SEMPRE mantenha** histórico de execução
- **SEMPRE documente** aprendizados e melhorias
- **SEMPRE preserve** conhecimento para uso futuro

---

## 📁 Estrutura de Organização

### **Pasta `wiki/log/`**
```
wiki/log/
├── completed_tasks/           # Tarefas concluídas
│   ├── integration_tasks.md   # Tarefas de integração (arquivado)
│   ├── system_updates.md      # Atualizações do sistema
│   └── feature_implementations.md # Implementações de features
├── reports/                   # Relatórios de conclusão
│   ├── integration_status_report.md
│   ├── system_performance_report.md
│   └── feature_completion_report.md
├── recipes/                   # Receitas para reproduzir resultados
│   ├── intelligent_orchestration_recipe.md
│   ├── bmad_integration_recipe.md
│   └── system_optimization_recipe.md
└── archives/                  # Arquivos arquivados
    ├── obsolete_files/        # Arquivos obsoletos
    └── historical_data/       # Dados históricos
```

---

## 📋 Regras de Limpeza Automática

### **🔄 Após Conclusão de Tarefas**
- **SEMPRE identifique** arquivos temporários criados durante a execução
- **SEMPRE mova** relatórios de conclusão para `wiki/log/reports/`
- **SEMPRE crie** receita na pasta `wiki/log/recipes/`
- **SEMPRE arquive** arquivos de tarefas em `wiki/log/completed_tasks/`
- **SEMPRE remova** arquivos temporários desnecessários

### **📊 Após Relatórios de Status**
- **SEMPRE consolide** informações em relatório final
- **SEMPRE mova** para pasta `wiki/log/reports/`
- **SEMPRE crie** receita correspondente
- **SEMPRE remova** arquivos temporários de status

### **🎯 Após Implementações de Features**
- **SEMPRE documente** processo completo
- **SEMPRE crie** receita de implementação
- **SEMPRE arquive** arquivos de planejamento
- **SEMPRE mantenha** apenas arquivos essenciais

---

## 📝 Estrutura de Relatórios de Conclusão

### **Template Padrão para Relatórios**
```markdown
# [Nome do Relatório] - Relatório de Conclusão

## 🎯 **Resumo Executivo**
- **Objetivo**: [Descrição do objetivo]
- **Status**: [COMPLETO/EM ANDAMENTO/CANCELADO]
- **Data de Conclusão**: [Data]
- **Duração**: [Tempo total]

## 📊 **Resultados Alcançados**
- [Lista de resultados]

## 🔄 **O que se tornou Obsoleto**
- [Lista de itens obsoletos]

## 🚀 **Benefícios Alcançados**
- [Lista de benefícios]

## 📈 **Métricas de Sucesso**
- [Métricas quantificáveis]

## 🎉 **Conclusão**
- [Resumo final]

## 📋 **Próximos Passos**
- [Passos futuros opcionais]

## 🔗 **Receita Correspondente**
- [Link para receita em `wiki/log/recipes/`]
```

---

## 🍳 Estrutura de Receitas

### **Template Padrão para Receitas**
```markdown
# [Nome da Receita] - Como Reproduzir o Resultado

## 🎯 **Objetivo**
[Descrição do que a receita permite reproduzir]

## 📋 **Pré-requisitos**
- [Lista de pré-requisitos]
- [Dependências necessárias]
- [Configurações prévias]

## 🛠️ **Ingredientes (Arquivos Necessários)**
- [Lista de arquivos necessários]
- [Estrutura de pastas]
- [Configurações]

## 📝 **Passo a Passo**

### **Passo 1: Preparação**
```bash
# Comandos de preparação
```

### **Passo 2: Implementação**
```bash
# Comandos de implementação
```

### **Passo 3: Validação**
```bash
# Comandos de validação
```

### **Passo 4: Teste**
```bash
# Comandos de teste
```

## ✅ **Resultado Esperado**
[Descrição do resultado esperado]

## 🔧 **Solução de Problemas**
- [Problemas comuns e soluções]

## 📚 **Referências**
- [Links para documentação relevante]
```

---

## 🧹 Regras de Limpeza Específicas

### **📁 Arquivos de Tarefas Temporárias**
- **SEMPRE mova** `integration_tasks.md` para `wiki/log/completed_tasks/` após conclusão
- **SEMPRE mova** `DEPENDENCY_INTEGRATION_PLAN.md` para `wiki/log/archives/` se obsoleto
- **SEMPRE mantenha** apenas tarefas ativas na pasta raiz
- **SEMPRE arquive** tarefas concluídas com data de conclusão

### **📊 Relatórios de Status**
- **SEMPRE consolide** múltiplos relatórios em um relatório final
- **SEMPRE mova** para `wiki/log/reports/` com nome descritivo
- **SEMPRE crie** receita correspondente
- **SEMPRE remova** relatórios temporários

### **🔄 Arquivos de Sistema**
- **SEMPRE mantenha** apenas arquivos essenciais do sistema
- **SEMPRE arquive** versões antigas em `wiki/log/archives/`
- **SEMPRE documente** mudanças significativas
- **SEMPRE preserve** histórico de evolução

---

## 🔄 Processo de Limpeza Automática

### **📋 Checklist de Limpeza**
```python
def cleanup_after_completion():
    # 1. Identificar arquivos temporários
    temp_files = identify_temp_files()
    
    # 2. Mover relatórios para pasta log
    move_reports_to_log()
    
    # 3. Criar receitas
    create_recipes()
    
    # 4. Arquivar tarefas concluídas
    archive_completed_tasks()
    
    # 5. Remover arquivos temporários
    remove_temp_files()
    
    # 6. Atualizar documentação
    update_documentation()
```

### **🎯 Triggers de Limpeza**
- **Após conclusão de tarefas** com status 100%
- **Após criação de relatórios** de status
- **Após implementação de features** completas
- **Após identificação de arquivos** obsoletos

---

## 📊 Manutenção de Histórico

### **📁 Estrutura de Arquivos**
- **SEMPRE mantenha** histórico de evolução
- **SEMPRE preserve** conhecimento para uso futuro
- **SEMPRE organize** por data e categoria
- **SEMPRE facilite** busca e recuperação

### **🔍 Sistema de Busca**
- **SEMPRE use** tags e categorias
- **SEMPRE mantenha** índices atualizados
- **SEMPRE facilite** localização de informações
- **SEMPRE preserve** contexto histórico

---

## 🎯 Regras de Execução

### **🔄 Execução Automática**
- **SEMPRE execute** limpeza após conclusão de tarefas
- **SEMPRE valide** arquivos antes de remover
- **SEMPRE mantenha** backup de arquivos importantes
- **SEMPRE documente** processo de limpeza

### **📋 Validação**
- **SEMPRE verifique** se arquivos foram movidos corretamente
- **SEMPRE confirme** se receitas foram criadas
- **SEMPRE teste** se sistema continua funcionando
- **SEMPRE valide** se documentação está atualizada

---

## 🔄 Atualização Automática

### **📝 Para Novos Relatórios**
Quando novos relatórios forem criados:
- ✅ Mover para pasta `wiki/log/reports/`
- ✅ Criar receita correspondente
- ✅ Atualizar índices de documentação
- ✅ Remover arquivos temporários

### **🧹 Para Limpeza de Sistema**
Quando limpeza for necessária:
- ✅ Identificar arquivos temporários
- ✅ Mover para pastas apropriadas
- ✅ Criar documentação de mudanças
- ✅ Validar funcionamento do sistema

---

## 🎉 Benefícios Esperados

### **🧹 Organização**
- **Sistema limpo** e organizado
- **Arquivos bem estruturados** e fáceis de encontrar
- **Histórico preservado** para referência futura
- **Conhecimento documentado** para reprodução

### **📊 Eficiência**
- **Busca rápida** de informações
- **Reprodução fácil** de resultados
- **Manutenção simplificada** do sistema
- **Colaboração melhorada** entre equipes

### **🔄 Sustentabilidade**
- **Sistema escalável** e organizado
- **Processos replicáveis** e documentados
- **Conhecimento preservado** para futuro
- **Evolução contínua** do sistema 