# 🔍 Ferramenta de Busca Avançada

Esta ferramenta oferece busca inteligente e filtros múltiplos para navegar eficientemente pela wiki do Canary e OTClient.

## 📋 Visão Geral

A busca avançada utiliza um índice JSON pré-processado que permite filtrar por:
- **Palavras-chave** no título e conteúdo
- **Tags** específicas (#canary, #otclient, #lua, #cpp, #database, #network, #security, #ui, #widgets, #events)
- **Níveis de dificuldade** (Iniciante, Intermediário, Avançado, Especialista)
- **Tipos de conteúdo** (Tutorial, Referência, Exemplo, Conceito)
- **Categorias** (Arquitetura, Sistema, Integração, Otimização)

## 🏗️ Estrutura do Índice JSON

```json
{
  "metadata": {
    "version": "1.0",
    "last_updated": "2025-08-05",
    "total_articles": 73,
    "tags_available": ["#canary", "#otclient", "#lua", "#cpp", "#database", "#network", "#security", "#ui", "#widgets", "#events"]
  },
  "articles": [
    {
      "id": "canary_arquitetura_core",
      "path": "wiki/canary_arquitetura_core.md",
      "title": "Arquitetura Core do Canary",
      "summary": "Visão detalhada dos componentes centrais do servidor Canary",
      "tags": ["#canary", "#arquitetura", "#core", "#servidor"],
      "aliases": ["canary core", "arquitetura canary", "componentes canary", "estrutura canary"],
      "level": "Intermediário",
      "type": "Referência",
      "category": "Arquitetura",
      "dependencies": ["canary_fundamentos.md"],
      "related": ["canary_sistema_rede.md", "canary_sistema_banco_dados.md"]
    },
    {
      "id": "otclient_sistema_ui",
      "path": "wiki/otclient_sistema_ui.md",
      "title": "Sistema de UI (OTUI)",
      "summary": "Fundamentos para construir interfaces com OTUI",
      "tags": ["#otclient", "#ui", "#otui", "#interface"],
      "aliases": ["otui", "interface otclient", "ui system", "widgets"],
      "level": "Intermediário",
      "type": "Tutorial",
      "category": "Interface",
      "dependencies": ["otclient_arquitetura_core.md"],
      "related": ["otclient_sistema_modulos.md", "otclient_sistema_eventos.md"]
    },
    {
      "id": "integracao_protocolo_comunicacao",
      "path": "wiki/integracao_protocolo_comunicacao.md",
      "title": "Protocolo de Comunicação",
      "summary": "Como cliente e servidor se comunicam via protocolo",
      "tags": ["#integracao", "#protocolo", "#network", "#comunicacao"],
      "aliases": ["protocolo", "comunicação", "network protocol", "client server"],
      "level": "Avançado",
      "type": "Conceito",
      "category": "Integração",
      "dependencies": ["canary_sistema_rede.md", "otclient_sistema_rede.md"],
      "related": ["integracao_sincronizacao_dados.md", "INTEGRATION-009_Security.md"]
    }
  ]
}
```

## 🔍 Como Funciona a Busca

### 1. **Busca por Palavras-chave**
- Pesquisa no título, resumo e aliases dos artigos
- Suporte a busca parcial e fuzzy matching
- Resultados ordenados por relevância

### 2. **Filtros por Tags**
- Use tags específicas: `#canary`, `#otclient`, `#lua`, `#cpp`
- Combine múltiplas tags para busca refinada
- Tags são aplicadas automaticamente baseadas no conteúdo

### 3. **Filtros por Nível**
- **Iniciante**: Conceitos básicos e primeiros passos
- **Intermediário**: Sistemas e implementações práticas
- **Avançado**: Otimizações e técnicas avançadas
- **Especialista**: Arquitetura complexa e integração

### 4. **Filtros por Tipo**
- **Tutorial**: Guias passo-a-passo
- **Referência**: Documentação técnica completa
- **Exemplo**: Casos de uso práticos
- **Conceito**: Explicações teóricas

## 💡 Exemplo de Busca

**Busca**: "Como criar interface OTUI com Lua"

**Filtros aplicados**:
- Tags: `#otclient`, `#ui`, `#lua`
- Nível: `Intermediário`
- Tipo: `Tutorial`

**Resultados esperados**:
1. `otclient_sistema_ui.md` - Sistema de UI (OTUI)
2. `otclient_sistema_lua.md` - Sistema de Lua
3. `otclient_sistema_modulos.md` - Sistema de Módulos

## 🚀 Implementação Futura

Esta ferramenta será implementada como:
- **Interface web** com filtros visuais
- **API REST** para integração com outros sistemas
- **Cache inteligente** para performance otimizada
- **Sugestões automáticas** baseadas no histórico de busca

## 📚 Tags Disponíveis

### **Ferramentas**
- `#canary` - Servidor Canary
- `#otclient` - Cliente OTClient
- `#lua` - Linguagem de script Lua
- `#cpp` - Linguagem C++

### **Sistemas**
- `#database` - Banco de dados
- `#network` - Rede e protocolo
- `#security` - Segurança
- `#ui` - Interface do usuário
- `#widgets` - Widgets e componentes
- `#events` - Sistema de eventos

### **Categorias**
- `#arquitetura` - Estrutura e design
- `#sistema` - Sistemas específicos
- `#integracao` - Integração entre componentes
- `#otimizacao` - Performance e otimização
