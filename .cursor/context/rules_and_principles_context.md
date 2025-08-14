# Contexto: Regras e Princípios Gerais do Sistema

Este arquivo consolida as regras de alto nível, os princípios de funcionamento e as diretrizes de performance que governam o comportamento do assistente.

---

## 🎯 Hierarquia de Prioridades

**Nível 1 - CRÍTICO (Sempre aplicar):**
1.  **Task Master**: Consultar `logs/reports/task_master.md` primeiro para qualquer tarefa.
2.  **Simplificação**: Evitar loops infinitos e complexidade desnecessária.
3.  **Contexto**: Detectar o contexto da tarefa antes de agir.
4.  **Permissões**: Respeitar restrições de modificação (código-fonte é apenas leitura).

**Nível 2 - IMPORTANTE (Aplicar quando relevante):**
5.  **Token Optimization**: Economizar tokens sempre que possível.
6.  **JSON Navigation**: Usar mapas (`data/maps/`) para consultas em vez de varrer arquivos.
7.  **File Organization**: Manter a estrutura de arquivos limpa e organizada.

**Nível 3 - OPCIONAL (Aplicar se necessário):**
8.  **BMAD Agents**: Usar agentes para tarefas complexas.
9.  **Auto-Learning**: Permitir que o sistema aprenda com as interações.
10. **Cross-Project Integration**: Focar na preparação para a integração com o Canary.

---

## 📋 Regras de Resolução de Conflitos

-   **Hierarquia**: Se regras conflitam, a de nível superior (Crítico > Importante) prevalece.
-   **Especificidade**: Se as regras são do mesmo nível, a mais específica para a tarefa se aplica.
-   **Padrão**: Em caso de dúvida ou conflito persistente, a **simplificação** é a regra padrão.
-   **Tarefas**: A consulta ao **Task Master é sempre o primeiro passo** para qualquer tarefa.

---

## ⚠️ Regras Principais (Extraído de `rules.md`)

-   **Escopo de Modificação**: **Nunca modifique** arquivos fora das pastas `wiki/`, `.cursor/`, `docs/`, `logs/`, `habdel/`.
-   **Código-Fonte**: O código dos submódulos (`otclient/`, etc.) é **imutável**.
-   **Criação de Tarefas**: Tarefas só podem ser criadas com base no `task_master.md`.

---

## ⚡ Regras de Performance e Simplificação

-   **Performance**:
    *   Limite a análise a no máximo 3 níveis de profundidade.
    *   Use cache para consultas repetidas.
    *   Implemente timeouts de 30 segundos para análises complexas.
    *   Otimize consultas usando índices JSON.
-   **Simplificação**:
    *   Execute solicitações simples diretamente, sem criar tarefas formais.
    *   Evite loops com limites de tentativas.
    *   Priorize a solução imediata sobre a documentação excessiva para problemas simples.
