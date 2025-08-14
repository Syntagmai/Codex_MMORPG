# Contexto: Prompt Engineering

Este arquivo contém as técnicas e regras de engenharia de prompts para otimizar as interações com a IA, melhorar a qualidade das respostas e economizar tokens.

---

## 🧠 Regras Básicas de Prompt Engineering

### **Aplicação Automática:**
- **Analise prompts recebidos** e aplique técnicas de engenharia de prompt antes de executar
- **Para cada prompt recebido**, aplique automaticamente as técnicas apropriadas

### **Técnicas Fundamentais:**
- **Role Prompting**: Atribuir contexto específico à IA quando apropriado
- **Chain-of-Thought**: Para problemas complexos que requerem raciocínio passo-a-passo
- **Few-shot Prompting**: Quando exemplos podem melhorar a compreensão
- **Estruturação de Saída**: Quando o usuário precisa de respostas organizadas
- **Refatoração**: Reformular prompts ambíguos perguntando por contexto adicional

---

## 🚀 Técnicas Avançadas de Prompt Engineering

### **Técnicas Especializadas:**
- **Meta-Prompting**: Criar prompts que geram outros prompts
- **Tree-of-Thoughts**: Exploração sistemática de soluções
- **Self-Consistency**: Validação de respostas múltiplas
- **Prompt Chaining**: Para tarefas complexas multi-etapa
- **Contextual Prompting**: Adaptação dinâmica baseada no contexto

### **Otimização de Interações:**
- Aplique técnicas avançadas para otimizar interações
- Use técnicas apropriadas baseadas na complexidade da tarefa
- Combine múltiplas técnicas quando necessário

---

## 🎯 Otimização de Tokens

### **Estratégia 20/80:**
- **Use inglês para IA** (scripts, metadados, descrições técnicas)
- **Use português para usuário** (documentação, tags, aliases)
- **Implemente estratégia 20/80** para máxima economia de tokens
- **Mantenha funcionalidade** preservando experiência do usuário
- **Otimize automaticamente** todos os mapas JSON

### **Princípios de Economia:**
- Economizar tokens sempre que possível
- Usar contextos específicos em vez de contextos gerais
- Aplicar lazy loading para carregar apenas o necessário
- Priorizar velocidade sobre completude para tarefas simples

---

## 📋 Templates e Padrões

### **Sistema de Templates:**
- **Template para Novas Regras**: Usar `.cursor/rules/template.md` como base
- **Templates Padronizados**: Para documentação e regras
- **Estrutura Padrão**: Seguir padrões estabelecidos
- **Checklist**: Para criação e validação de prompts

### **Padrões de Prompt:**
- Estruturar prompts para máxima clareza
- Incluir contexto necessário sem redundância
- Usar formatação consistente
- Aplicar princípios de hierarquia de informação

---

## 🔄 Simplificação Inteligente

### **Detecção de Complexidade:**
- **Detecte** se solicitação é simples ou complexa
- **Execute diretamente** solicitações simples sem criar tarefas
- **Aplique processo estruturado** apenas para solicitações complexas

### **Prevenção de Loops:**
- **Evite loops infinitos** com timeouts e limites de tentativas
- **Priorize solução imediata** sobre documentação extensa
- **Pare processos complexos** se sistema travar
- **Responda diretamente** se timeout for atingido

---

## 📚 Referências Completas

Para detalhes completos sobre prompt engineering, consulte:
- `@.cursor/rules/prompt-engineering-rules.md`
- `@.cursor/rules/enhanced-prompt-engineering-rules.md`
- `@.cursor/rules/token-optimization-rules.md`
- `@.cursor/rules/simplification-rules.md`
- `@.cursor/rules/template.md`
