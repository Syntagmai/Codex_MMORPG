---
tags: [supervision, task_management, bmad]
type: supervision_report
status: active
created: 2025-08-01T02:41:38.524466
---

# 📊 Relatório de Supervisão - Task Supervisor Agent

## 🎯 **Status Atual**

### **Monitoramento:**
- **Ativo**: False
- **Último comando**: Nunca
- **Cooldown**: 300s
- **Timeout de resposta**: 60s

        ### **Análise do Contexto:**
        - **Tarefa atual**: N/A - N/A
        - **Conclusão detectada**: True
        - **Espera detectada**: False
        - **Erros detectados**: True
        - **Pode enviar comando**: True

## 📋 **Padrões de Detecção**

### **Conclusão:**
- concluído|concluída|completo|completa
- feito|feita|finalizado|finalizada
- terminado|terminada|pronto|pronta
- sucesso|success|completado|completada
- ✅|🟢|🎯|🏆
- task.*concluída|task.*completa
- epic.*concluída|epic.*completa

### **Espera por Instruções:**
- próxima.*tarefa|next.*task
- aguardando.*instrução|waiting.*instruction
- próximo.*passo|next.*step
- o que.*fazer|what.*to.*do
- próxima.*ação|next.*action
- continuar|continue

### **Erros:**
- erro|error|falha|failure
- problema|problem|issue
- ❌|🔴|⚠️|🚨
- não.*funciona|doesn't.*work
- falhou|failed|broke

## 🚀 **Próximas Ações**

### **Se conclusão detectada:**
- Continuar automaticamente para próxima tarefa
- Gerar comando: `@cursor.md continue para a próxima tarefa pfv`

### **Se espera detectada:**
- Continuar automaticamente para próxima tarefa
- Gerar comando: `@cursor.md continue para a próxima tarefa pfv`

### **Se erros detectados:**
- Não continuar automaticamente
- Aguardar intervenção manual

## 📈 **Estatísticas**

- **Ciclos executados**: False
- **Comandos enviados**: 0
- **Tempo desde último comando**: N/As

---

**Relatório Gerado**: 2025-08-01T02:41:38.524516  
**Responsável**: Task Supervisor Agent  
**Status**: 🔴 Inativo

## 🔗 **Links Automáticos**

> [!info] **Links Gerados Automaticamente**
> Estes links foram criados automaticamente pelo sistema de linkagem da categoria **Tools**

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]
- [[../maps/tools_index|Índice de Ferramentas]]
- [[../update/README|Scripts de Atualização]]

### **🧭 Navegação**
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]
- [[../maps/category_indices|Índices por Categoria]]
- [[../maps/relationships|Relacionamentos]]

### **📊 Métricas da Categoria**
- **Categoria**: Tools
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

