# Regras de Prompt Engineering - Técnicas Básicas

## 📋 **Objetivo**
Definir regras para **otimização básica de prompts** usando técnicas fundamentais de engenharia de prompt, garantindo respostas mais precisas e eficazes.

---

## 🎯 **Regras Principais (BÁSICAS)**

### **1. Análise Obrigatória de Prompts**
**SEMPRE analise prompts recebidos e aplique técnicas de engenharia de prompt antes de executar.** Identifique oportunidades de melhoria e otimize automaticamente.

### **2. Role Prompting Obrigatório**
**Use Role Prompting para atribuir contexto específico à IA quando apropriado.** Defina claramente o papel da IA para melhorar consistência e qualidade das respostas.

**Exemplo de aplicação:**
- **Antes**: "Explica isso aqui"
- **Depois**: "Você é um professor de programação experiente. Explique este conceito de forma didática: ..."

### **3. Refatoração de Prompts Ambíguos**
**Refatore prompts ambíguos perguntando por contexto adicional quando necessário.** Reescreva como pergunta clara e sugira alternativas de interpretação.

**Exemplo de aplicação:**
- **Antes**: "Faz um código pra mim que resolva isso aqui"
- **Depois**: "Você é um programador especializado. Gere um código eficiente que resolva o seguinte problema. Explique cada parte com comentários. Problema: ..."

### **4. Structured Output para Organização**
**Estruture a saída quando o usuário precisa de respostas organizadas.** Force a IA a responder com estrutura clara e previsível.

**Exemplo de aplicação:**
```
Responda usando o seguinte formato:

- Introdução
- Explicação Técnica  
- Conclusão Resumida
```

---

## 🔄 **Processo de Aplicação (BÁSICO)**

### **📋 Checklist de Otimização Básica**

Para cada prompt recebido, verifique e aplique:

- [ ] **Role Prompting** - Atribuir papel específico à IA
- [ ] **Refatoração** - Clarificar ambiguidades (se existirem)
- [ ] **Structured Output** - Definir formato de resposta (se apropriado)

### **🎯 Prioridade de Aplicação**

1. **Primeiro**: Role Prompting (sempre aplicável)
2. **Segundo**: Refatoração (se necessário)
3. **Terceiro**: Structured Output (se organização for importante)

---

## ⚠️ **Regras de Exceção**

### **1. Prompts Já Otimizados**
Se o prompt já estiver bem estruturado e claro, aplique apenas Role Prompting básico.

### **2. Prompts Específicos**
Para prompts que já especificam formato ou papel, respeite a estrutura original.

### **3. Contexto de Emergência**
Em situações urgentes, priorize velocidade sobre otimização completa.

---

## 📚 **Exemplos de Transformação Básica**

### **Exemplo 1: Role Prompting**
```
ANTES:
"Analisa este código"

DEPOIS:
"Você é um analista de código experiente especializado em Python. 
Analise este código identificando possíveis melhorias, bugs e 
oportunidades de otimização: [código]"
```

### **Exemplo 2: Refatoração**
```
ANTES:
"Faz um script que funcione"

DEPOIS:
"Você é um desenvolvedor Python. Crie um script funcional que 
resolva o seguinte problema. Inclua comentários explicativos e 
tratamento de erros. Problema: [descrição]"
```

### **Exemplo 3: Structured Output**
```
ANTES:
"Explica como funciona"

DEPOIS:
"Você é um professor. Explique como funciona [conceito] usando 
o seguinte formato:

1. **Definição**: O que é
2. **Como Funciona**: Explicação técnica
3. **Exemplo Prático**: Caso de uso real
4. **Resumo**: Pontos principais"
```

---

## 🔗 **Referências para Técnicas Avançadas**

Para técnicas mais avançadas de prompt engineering, consulte:
- **Chain-of-Thought**: `enhanced-prompt-engineering-rules.md`
- **Few-shot Prompting**: `enhanced-prompt-engineering-rules.md`
- **Meta-Prompting**: `enhanced-prompt-engineering-rules.md`
- **Tree-of-Thoughts**: `enhanced-prompt-engineering-rules.md`

---

## 📊 **Aplicação no Contexto de Integração**

### **Para Preparação de Integração Canary:**
- **Role**: "Você é um especialista em integração de sistemas"
- **Contexto**: "Preparando integração OTClient + Canary"
- **Estrutura**: "Análise → Preparação → Implementação → Validação"

### **Para Otimização de Regras:**
- **Role**: "Você é um arquiteto de sistemas especializado em consolidação"
- **Contexto**: "Consolidando regras duplicadas para integração"
- **Estrutura**: "Identificação → Consolidação → Validação → Documentação"

---

**Regras Básicas**: 2025-01-27  
**Status**: Ativo e Funcional  
**Próxima Revisão**: 2025-02-03  
**Relacionado**: `enhanced-prompt-engineering-rules.md` (técnicas avançadas) 