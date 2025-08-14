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

### 6. 🤖 **Sistema de Agentes BMAD**
-   **Contexto Principal**: `@.cursor/context/bmad_agents_context.md`
-   **Uso**: Para usar agentes especializados, orquestração inteligente e coordenação de workflows complexos.

### 7. ⚡ **Performance e Navegação JSON**
-   **Contexto Principal**: `@.cursor/context/performance_navigation_context.md`
-   **Uso**: Para otimização de performance, navegação eficiente por mapas JSON e cache inteligente.

### 8. 🔗 **Integração Cross-Project**
-   **Contexto Principal**: `@.cursor/context/integration_context.md`
-   **Uso**: Para trabalhar na integração entre OTClient e Canary, protocolos compartilhados e preparação para integração total.

### 9. 🔧 **Automação (Git e Python)**
-   **Contexto Principal**: `@.cursor/context/automation_context.md`
-   **Uso**: Para automação de scripts Python, controle de versão Git, resolução automática de erros e organização de arquivos.

### 10. 🧠 **Prompt Engineering e Otimização**
-   **Contexto Principal**: `@.cursor/context/prompt_engineering_context.md`
-   **Uso**: Para aplicar técnicas de prompt engineering, otimização de tokens, simplificação inteligente e uso de templates.

> **Lembrete**: Combine contextos conforme necessário. Para uma tarefa complexa que envolve código e documentação, você pode carregar múltiplos contextos: `@.cursor/context/code_analysis_context.md @.cursor/context/documentation_context.md ...`
