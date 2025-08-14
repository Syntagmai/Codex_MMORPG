# Guia de Otimização Avançada: Contextos Modulares

## 🎯 Objetivo

Reestruturar o sistema de contexto, abandonando um `cursor.md` monolítico em favor de múltiplos **arquivos de contexto modulares e específicos para cada workflow**. Esta abordagem equilibra a riqueza do contexto com a eficiência no uso de tokens.

## 🧐 O Problema: O Dilema entre Contexto Rico e Custo de Tokens

-   **`cursor_backup.md`**: Rico em detalhes, mas extremamente caro para usar como contexto em todas as interações (758 linhas).
-   **`cursor.md` (versão otimizada anterior)**: Leve e barato, mas perdeu nuances e informações contextuais importantes, tornando-se um "roteador" pouco informativo.

A solução não é escolher entre um e outro, mas sim combinar o melhor dos dois mundos.

## ✨ A Solução: Micro-Contextos por Workflow

A estratégia é criar uma pasta dedicada, como `.cursor/context/`, que conterá arquivos `.md` menores, cada um sendo um "micro-contexto" extraído do `cursor_backup.md` original. Cada arquivo será focado em um único workflow.

O novo `cursor.md` se tornará um índice inteligente, apontando para esses micro-contextos.

---

## 📋 Plano de Ação: Criando os Contextos Modulares

### Passo 1: Criar a Estrutura de Pastas

Crie uma nova pasta para armazenar os contextos modulares:
`mkdir .cursor/context`

### Passo 2: Criar os Arquivos de Contexto Específicos

Crie os seguintes arquivos dentro de `.cursor/context/` e popule-os com as seções correspondentes do `cursor_backup.md`.

---

#### 1. **`task_management_context.md`**
*   **Propósito**: Para planejar, criar e executar tarefas.
*   **Conteúdo a ser extraído do `cursor_backup.md`**:
    *   Seção `⚠️ SISTEMA DE TAREFAS - REGRAS CRÍTICAS` (Linhas 99-160)
    *   Hierarquia de Prioridades (focada em tarefas)
    *   Referências ao `task_master.md` e `integrated_task_manager.md`
*   **Exemplo de Prompt**: `@.cursor/context/task_management_context.md @logs/reports/task_master.md Planeje o Epic 2.`

---

#### 2. **`code_analysis_context.md`**
*   **Propósito**: Para analisar, entender e gerar código relacionado aos submódulos.
*   **Conteúdo a ser extraído do `cursor_backup.md`**:
    *   Seção `ESTRUTURA DE SUBMÓDULOS` (Linhas 227-232 e 458-464)
    *   Padrões de Navegação para `Análise de código OTClient` e `Análise de código Canary` (Linhas 89-90)
    *   Regras de Indexação do Código-Fonte (Linhas 518-525)
    *   Permissões de modificação de código (apenas leitura para submódulos).
*   **Exemplo de Prompt**: `@.cursor/context/code_analysis_context.md @data/maps/otclient_source_index.json Explique a classe `Game`.'

---

#### 3. **`documentation_context.md`**
*   **Propósito**: Para criar ou modificar a documentação na `wiki/` ou `docs/`.
*   **Conteúdo a ser extraído do `cursor_backup.md`**:
    *   Seção `Regras de Documentação` (Linhas 467-473)
    *   Seção `Regras da Wiki` (Linhas 476-483)
    *   Seção `Regras para Wiki Abrangente` (Linhas 564-579)
    *   Referências de Pastas (`wiki/`, `docs/`, `habdel/`).
*   **Exemplo de Prompt**: `@.cursor/context/documentation_context.md Crie um documento na wiki sobre o sistema de `networking`.`

---

#### 4. **`system_navigation_context.md`**
*   **Propósito**: Para perguntas gerais sobre a estrutura, navegação e onde encontrar arquivos.
*   **Conteúdo a ser extraído do `cursor_backup.md`**:
    *   Seção `NOVA ESTRUTURA DO PROJETO` (Linhas 4-60)
    *   Mapa Visual da Estrutura (Linhas 233-280)
    *   Padrões de Navegação (gerais) (Linhas 86-96)
    *   Referências de Pastas (Linhas 437-457)
*   **Exemplo de Prompt**: `@.cursor/context/system_navigation_context.md Onde ficam os mapas de dados?`

---

#### 5. **`rules_and_principles_context.md`**
*   **Propósito**: Para entender os princípios gerais, prioridades e regras de alto nível do sistema.
*   **Conteúdo a ser extraído do `cursor_backup.md`**:
    *   Hierarquia de Prioridades (NOVA) (Linhas 319-339)
    *   Regras de Resolução de Conflitos (Linhas 340-346)
    *   Regras Principais (`rules.md`) (Linhas 424-436)
    *   Regras de Performance e Simplificação (Linhas 672-694)
*   **Exemplo de Prompt**: `@.cursor/context/rules_and_principles_context.md Qual a prioridade ao lidar com uma tarefa de otimização?`

---

### Passo 3: Atualizar o `cursor.md` para ser o Novo Roteador

Substitua o conteúdo do `cursor.md` principal pelo seguinte, que agora aponta para os novos contextos modulares.

```markdown
# 🎯 Codex Assistente - Roteador de Contexto Modular

Este arquivo é o ponto de entrada principal. Ele direciona para **contextos modulares** específicos para cada tipo de tarefa, garantindo o equilíbrio perfeito entre detalhes e custo de tokens.

---

## 🚀 Workflows e Contextos Modulares

**Para cada tarefa, use `@` para carregar o contexto modular relevante.**

### 1. 📋 **Gerenciamento de Tarefas**
-   **Contexto Principal**: `@.cursor/context/task_management_context.md`
-   **Arquivos-Chave**: `@logs/reports/task_master.md`, `@docs/dashboard/integrated_task_manager.md`
-   **Uso**: Para planejar, criar, executar e atualizar tarefas.

### 2. 💻 **Análise e Desenvolvimento de Código**
-   **Contexto Principal**: `@.cursor/context/code_analysis_context.md`
-   **Arquivos-Chave**: `@data/maps/otclient_source_index.json`, `@data/maps/canary_source_index.json`
-   **Uso**: Para analisar código-fonte, entender a arquitetura dos submódulos e seguir as regras de desenvolvimento.

### 3. 📚 **Criação e Edição de Documentação**
-   **Contexto Principal**: `@.cursor/context/documentation_context.md`
-   **Arquivos-Chave**: Use os índices em `data/maps/` para navegar na `wiki/` e `docs/`.
-   **Uso**: Para criar novos guias, tutoriais ou documentação técnica seguindo os padrões do projeto.

### 4. 🧭 **Navegação e Estrutura do Projeto**
-   **Contexto Principal**: `@.cursor/context/system_navigation_context.md`
-   **Uso**: Para fazer perguntas gerais sobre a localização de arquivos, a estrutura de pastas e como os sistemas se conectam.

### 5. ⚙️ **Regras Gerais e Princípios do Sistema**
-   **Contexto Principal**: `@.cursor/context/rules_and_principles_context.md`
-   **Uso**: Para entender a hierarquia de prioridades, as regras de resolução de conflitos e as diretrizes de performance e simplificação.

> **Lembrete**: Combine contextos conforme necessário. Para uma tarefa complexa que envolve código e documentação, você pode carregar múltiplos contextos: `@.cursor/context/code_analysis_context.md @.cursor/context/documentation_context.md ...`
```

## ✅ Benefícios Desta Nova Abordagem

1.  **Contexto Rico e Focado**: Cada workflow recebe exatamente as informações de que precisa, sem excessos.
2.  **Economia de Tokens Inteligente**: O custo é proporcional à complexidade da tarefa. Uma pergunta simples de navegação é muito mais barata que uma análise de código.
3.  **Manutenção e Escalabilidade**: É fácil adicionar novos workflows ou atualizar os existentes, modificando apenas os arquivos de contexto modulares, sem tocar no sistema inteiro.
4.  **Clareza e Usabilidade**: Fica muito mais claro para você (e para a IA) qual conjunto de regras e informações se aplica a cada situação.
