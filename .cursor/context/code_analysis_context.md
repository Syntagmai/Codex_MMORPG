# Contexto: Análise e Desenvolvimento de Código

Este arquivo fornece o contexto necessário para analisar, entender e interagir com o código-fonte do projeto, especialmente os submódulos Git.

---

## 🏛️ Estrutura de Submódulos

Este repositório contém **TRÊS submódulos Git** como fontes de verdade:
-   **`otclient/`** - Código-fonte do cliente OTClient (submódulo)
-   **`canary/`** - Código-fonte do servidor Canary (submódulo)
-   **`forgottenmapeditor/`** - Editor de mapa integrado (submódulo)

**Definição de "otclient"**: Refere-se ao submódulo `otclient/` que contém o código-fonte oficial. O código está disponível para análise e documentação, mas modificações devem ser feitas no repositório original.

**Permissões**: O código-fonte dos submódulos é **imutável** neste repositório. Sugestões são permitidas via comentários, mas sem alterar o código diretamente.

---

## 🧭 Padrões de Navegação de Código

-   **Análise de código OTClient**: `data/maps/otclient_source_index.json` → `otclient/src/` → `otclient/modules/` → `docs/systems/`
-   **Análise de código Canary**: `data/maps/canary_source_index.json` → `canary/src/` → `canary/data/` → `docs/systems/`

---

## 🔍 Regras de Indexação do Código-Fonte

-   **Fonte da Verdade**: Consulte o código-fonte do OTClient **antes** da wiki.
-   **Índice Principal**: Mantenha `otclient_source_index.json` atualizado com todos os arquivos do código-fonte.
-   **Hierarquia de Consulta**: `otclient_source_index.json` → código-fonte → wiki → regras.
-   **Categorização**: O código é categorizado por sistemas: Core, UI, Game, Network, Resource, Module.
-   **Extração Automática**: Funções e classes são extraídas automaticamente para busca rápida.
