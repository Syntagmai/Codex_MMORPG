# Contexto: Navegação e Estrutura do Sistema

Este arquivo serve como um mapa geral do projeto, ajudando a localizar arquivos, entender a estrutura das pastas e os principais fluxos de navegação.

---

## 📁 ESTRUTURA ATUALIZADA DO PROJETO

-   **`wiki/`** - Conteúdo educacional (Obsidian)
-   **`habdel/`** - Metodologia de pesquisa e stories
-   **`docs/`** - Documentação interna do sistema
-   **`logs/`** - Relatórios, monitoramento e alertas
-   **`data/`** - Dados do sistema (incluindo mapas JSON)
-   **`scripts/`** - Scripts e ferramentas
-   **`backup/`** - Sistema de backup
-   **`temp/`** - Arquivos temporários
-   **`.cursor/`** - Regras e contextos do assistente

---

## 🗺️ Mapa Visual da Estrutura

```
📁 Codex_MMORPG/
├── 📋 cursor.md (ORQUESTRADOR PRINCIPAL)
├── 📂 .cursor/
│   ├── 📂 rules/ (30+ regras)
│   └── 📂 context/ (Contextos Modulares)
├── 📂 logs/
│   └── 📂 reports/
│       └── 📋 task_master.md (SISTEMA DE TAREFAS PRINCIPAL)
├── 📂 docs/
│   └── 📂 dashboard/
│       └── 🎯 integrated_task_manager.md (SISTEMA DE INTEGRAÇÃO)
├── 📚 wiki/ (documentação educacional)
├── 🔬 habdel/ (metodologia de pesquisa)
├── 💾 data/ (dados e mapas JSON)
├── 🔧 scripts/ (scripts e ferramentas)
│
├── 🔧 otclient/ (SUBMÓDULO - CLIENTE)
├── 🖥️ canary/ (SUBMÓDULO - SERVIDOR)
└── 🗺️ forgottenmapeditor/ (SUBMÓDULO - EDITOR DE MAPA)
```

---

## 🧭 Padrões de Navegação Principais

-   **Dashboard Central**: `cursor.md` → `docs/dashboard/integrated_task_manager.md`
-   **Task Master**: `cursor.md` → `logs/reports/task_master.md`
-   **Análise de código OTClient**: `data/maps/otclient_source_index.json` → `otclient/src/`
-   **Busca de documentação**: `data/maps/tags_index.json` → `data/maps/wiki_map.json` → `wiki/`
-   **Consulta de regras**: `cursor.md` → `.cursor/rules/` ou `.cursor/context/`
-   **Execução de scripts**: `cursor.md` → `scripts/script_execution_manager.py`

---

## 📁 Referências Rápidas de Pastas

-   `wiki/`: Documentação educacional.
-   `habdel/`: Metodologia de pesquisa.
-   `docs/`: Documentação técnica interna.
-   `logs/`: Relatórios e monitoramento.
-   `data/`: Dados e mapas JSON.
-   `scripts/`: Ferramentas e automação.
-   `.cursor/rules/`: Regras detalhadas do assistente.
-   `.cursor/context/`: Contextos modulares para workflows.
-   `otclient/`, `canary/`, `forgottenmapeditor/`: Submódulos de código-fonte.
