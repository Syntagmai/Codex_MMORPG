# Contexto: Documentação (Wiki e Docs)

Este arquivo define as regras e padrões para a criação e manutenção de toda a documentação do projeto, seja na `wiki/` (educacional) ou na `docs/` (técnica).

---

## 📝 Regras Gerais de Documentação

-   **Formatação**: Use formatação Obsidian (callouts, wikilinks, frontmatter).
-   **Consistência**: Mantenha um estilo consistente com os documentos existentes.
-   **Foco Prático**: Priorize exemplos práticos e código funcional.
-   **Linguagem**: Use uma linguagem clara e acessível.

---

## 📚 Regras Específicas da Wiki (`wiki/`)

-   **Extensão**: Use `.md` para todos os arquivos.
-   **Frontmatter**: É obrigatório o uso de frontmatter com `tags`, `status` e `aliases`.
-   **Estrutura**: Mantenha uma estrutura hierárquica com índices e seções bem definidas.
-   **Proteção**: **NUNCA** modifique arquivos na pasta `wiki/.obsidian/` sem autorização.

---

## 📖 Regras para uma Wiki Abrangente

-   **Integração de Conteúdo**: Integre **TODO** o conteúdo da pasta `habdel/` na wiki.
-   **Completude**: Crie uma documentação 100% completa, sem lacunas.
-   **Navegação**: Organize uma navegação lógica entre os documentos, com referências cruzadas atualizadas.

### 🔄 Atualização Obrigatória

-   **Índice Principal**: Ao criar um novo documento, atualize `wiki/otclient_wiki.md`.
-   **Referência**: Adicione uma referência ao novo documento na seção "Documentação Criada".
-   **Estatísticas**: Atualize os contadores e estatísticas de progresso.
-   **Links**: Mantenha os links internos funcionando e verifique a consistência com os padrões.

---

## 📁 Referências de Pastas de Documentação

-   `wiki/`: Contém conteúdo educacional para Obsidian.
-   `docs/`: Contém documentação interna do sistema (guias, sistemas, etc.).
-   `habdel/`: Contém a metodologia de pesquisa e stories, que deve ser migrada para a wiki.
