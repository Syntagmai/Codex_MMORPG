# Contexto: Performance e Navegação JSON

Este arquivo contém as regras e otimizações para navegação eficiente, cache inteligente, uso de mapas JSON e diretrizes de performance do sistema.

---

## 🗺️ Navegação JSON

### **Estrutura de Navegação Padronizada:**
- **Busca de documentação**: `data/maps/tags_index.json` → `data/maps/wiki_map.json` → `docs/` → `data/maps/relationships.json`
- **Navegação por grafos**: `data/maps/navigation_graph.json` → Caminhos ótimos → Cache inteligente → Sugestões contextuais

### **Regras de Navegação JSON:**
- **Use arquivos JSON como meio principal de navegação** durante consultas da wiki e regras
- **Mantenha `wiki/tags_index.json` atualizado** com todas as tags da wiki organizadas por arquivo
- **Consulte os mapas JSON antes de acessar arquivos markdown diretamente**
- **Atualize os arquivos JSON** quando criar, modificar ou remover documentos
- **Use a estrutura de consulta padronizada**: tags_index.json → wiki_map.json → relationships.json → markdown

---

## ⚡ Otimizações de Performance

### **🎯 Cache Inteligente:**
- **Arquivos frequentes** (30 min): `cursor.md`, `tags_index.json`, `wiki_map.json`
- **Contexto** (15 min): `enhanced_context_system.json`, `context_data.json`
- **Datasets grandes** (60 min): `otclient_source_index.json`, `modules_index.json`

### **🚀 Limites de Performance:**
- **Máximo 3 níveis** de análise para evitar loops
- **Timeout 30 segundos** para operações complexas
- **Máximo 10 arquivos** lidos por consulta
- **Máximo 50 resultados** por busca

### **🧠 Lazy Loading:**
- **Regras**: Carregadas apenas quando necessárias
- **Mapas JSON**: Carregados sob demanda
- **Documentação**: Carregada sempre (acesso direto)

### **📊 Métricas de Performance:**
- **Tarefas simples**: < 2 segundos
- **Tarefas complexas**: < 10 segundos
- **Análises grandes**: < 30 segundos

---

## 🔄 Regras de Atualização Automática

- **Execute scripts de atualização** antes de qualquer tarefa
- **Use ordem padronizada**: código-fonte → habdel → módulos → estilos → recursos → ferramentas → wiki
- **Valide integridade** de todos os mapas após atualização
- **Mantenha mapas sincronizados** com arquivos reais
- **Reporte status** de atualização automaticamente

---

## 🧭 Recuperação de Erros

- **Arquivo não encontrado**: Buscar similar → Usar índice
- **Permissão negada**: Trocar contexto → Modo somente leitura
- **Timeout**: Reduzir escopo → Modo simples

---

## 📚 Referências Completas

Para detalhes completos sobre navegação e performance, consulte:
- `@.cursor/rules/wiki-json-navigation-rules.md`
- `@.cursor/rules/performance-rules.md`
- `@.cursor/rules/auto-update-maps-rules.md`
- `@.cursor/rules/token-optimization-rules.md`
