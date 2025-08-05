# OTClient Source Index Rules

## 📋 Regras de Indexação do Código-Fonte OTClient

Este arquivo define as regras para **indexação e consulta do código-fonte** do OTClient, garantindo acesso rápido e preciso à verdade da implementação antes de consultar a wiki.

---

## 🎯 Regras Principais

### 1. **Código-Fonte como Fonte da Verdade**
**SEMPRE consulte o código-fonte do OTClient antes da wiki.** O código-fonte é a implementação real e deve ser a referência primária para qualquer consulta técnica.

### 2. **Índice JSON Obrigatório**
**Mantenha um arquivo `otclient_source_index.json` sempre atualizado** com todos os arquivos do código-fonte organizados por categoria, funcionalidade e localização.

### 3. **Hierarquia de Consulta**
**Use a hierarquia de consulta estabelecida:**
1. **Primeiro**: Consultar `otclient_source_index.json` para localizar arquivos relevantes
2. **Segundo**: Acessar código-fonte específico para implementação real
3. **Terceiro**: Consultar wiki para documentação e exemplos
4. **Quarto**: Usar regras e templates para formatação

### 4. **Indexação Automática**
**SEMPRE atualize o índice quando o código-fonte for modificado.** Execute scripts de indexação automática após qualquer mudança no código.

### 5. **Categorização Inteligente**
**Organize o código-fonte por categorias funcionais:**
- **Core Systems**: Engine, framework, bibliotecas fundamentais
- **UI Systems**: Interface, widgets, layouts, eventos
- **Game Systems**: Mapas, criaturas, combate, efeitos
- **Network Systems**: Protocolos, comunicação, serialização
- **Resource Systems**: Imagens, sons, fontes, dados
- **Module Systems**: Sistema de módulos, carregamento, sandboxing

---

## 📁 Estrutura do Índice

### 🗂️ **Arquivo Principal**
`otclient_source_index.json` - Índice completo do código-fonte

### 📋 **Estrutura do Índice**
```json
{
  "metadata": {
    "version": "1.0",
    "last_updated": "2025-01-27T10:00:00Z",
    "total_files": 1500,
    "total_lines": 250000,
    "description": "Índice completo do código-fonte do OTClient"
  },
  "categories": {
    "core_systems": {
      "name": "Sistemas Core",
      "description": "Engine, framework e bibliotecas fundamentais",
      "files": [
        {
          "path": "src/client/client.cpp",
          "name": "client.cpp",
          "type": "cpp",
          "size": 15420,
          "lines": 450,
          "functions": ["init", "terminate", "processEvents"],
          "classes": ["Client"],
          "description": "Cliente principal do OTClient"
        }
      ]
    }
  },
  "search_index": {
    "by_function": {
      "init": ["src/client/client.cpp", "src/framework/core.cpp"],
      "g_ui": ["src/client/ui.cpp", "modules/corelib/ui/"],
      "g_map": ["src/client/map.cpp", "modules/gamelib/"]
    },
    "by_class": {
      "UIWidget": ["src/client/ui.cpp", "modules/corelib/ui/"],
      "Map": ["src/client/map.cpp"],
      "Creature": ["src/client/creature.cpp"]
    },
    "by_file_type": {
      "cpp": 800,
      "h": 400,
      "lua": 200,
      "otui": 100
    }
  }
}
```

---

## 🔄 Processo de Consulta

### 📋 **Fluxo de Consulta Padrão**

Para qualquer consulta técnica:

1. **Consultar `otclient_source_index.json`** para localizar arquivos relevantes
2. **Acessar código-fonte específico** para implementação real
3. **Analisar funções e classes** relacionadas ao assunto
4. **Consultar wiki** para documentação e exemplos
5. **Usar regras** para formatação e estrutura

### 🎯 **Exemplos de Consulta**

#### **Busca por Função**
```bash
# Buscar implementação de g_ui
curl -s otclient_source_index.json | jq '.search_index.by_function.g_ui'
```

#### **Busca por Classe**
```bash
# Buscar implementação de UIWidget
curl -s otclient_source_index.json | jq '.search_index.by_class.UIWidget'
```

#### **Busca por Categoria**
```bash
# Buscar todos os arquivos de UI
curl -s otclient_source_index.json | jq '.categories.ui_systems.files'
```

---

## ⚡ Indexação Automática

### 🔧 **Scripts Obrigatórios**

#### **1. Gerar Índice do Código-Fonte**
```python
def generate_source_index():
    """Gera índice completo do código-fonte OTClient"""
    # Escanear todos os arquivos do código-fonte
    # Extrair funções, classes, estruturas
    # Categorizar por funcionalidade
    # Gerar índices de busca
    # Salvar otclient_source_index.json
```

#### **2. Atualizar Índice**
```python
def update_source_index():
    """Atualiza índice quando código for modificado"""
    # Detectar mudanças no código-fonte
    # Reindexar arquivos modificados
    # Atualizar metadados
    # Manter sincronização
```

### 📋 **Trigger de Atualização**

**SEMPRE execute scripts de indexação quando:**
- ✅ Código-fonte for modificado
- ✅ Novos arquivos forem adicionados
- ✅ Estrutura de pastas for alterada
- ✅ Dependências forem atualizadas

---

## 🎯 Regras de Performance

### ⚡ **Otimização de Consultas**

1. **Cache de Índice**: Mantenha índice em memória durante sessão
2. **Busca Indexada**: Use índices para busca rápida
3. **Lazy Loading**: Carregue código apenas quando necessário
4. **Compressão**: Use JSON compactado para arquivos grandes

### 📊 **Métricas de Performance**

| Operação | Tempo Máximo | Método |
|----------|--------------|--------|
| **Busca por função** | < 50ms | JSON indexado |
| **Busca por classe** | < 50ms | JSON indexado |
| **Busca por categoria** | < 100ms | JSON indexado |
| **Leitura de código** | < 200ms | Arquivo direto |

---

## ⚠️ Regras de Exceção

### 1. **Documentação de Alto Nível**
Para conceitos gerais e arquitetura, priorize a wiki.

### 2. **Exemplos Práticos**
Para exemplos de uso, combine código-fonte com wiki.

### 3. **Configurações**
Para configurações e setup, use documentação específica.

---

## 📚 Exemplos de Uso

### 🔍 **Consulta de Implementação**
```python
# Buscar implementação de uma função específica
with open('otclient_source_index.json', 'r') as f:
    data = json.load(f)
    ui_files = data['search_index']['by_function']['g_ui']
    print(f"Implementação de g_ui: {ui_files}")
```

### 📊 **Análise de Código**
```python
# Analisar estrutura do código-fonte
with open('otclient_source_index.json', 'r') as f:
    data = json.load(f)
    total_files = data['metadata']['total_files']
    cpp_files = data['search_index']['by_file_type']['cpp']
    print(f"Total: {total_files}, C++: {cpp_files}")
```

### 🔗 **Navegação por Categoria**
```python
# Navegar por sistemas específicos
with open('otclient_source_index.json', 'r') as f:
    data = json.load(f)
    ui_files = data['categories']['ui_systems']['files']
    for file in ui_files:
        print(f"UI: {file['path']} - {file['description']}")
```

---

## ✅ Tarefa Obrigatória da IA

**SEMPRE que uma consulta técnica for solicitada:**

1. **Consultar primeiro** `otclient_source_index.json`
2. **Localizar arquivos** relevantes no código-fonte
3. **Analisar implementação** real no código
4. **Consultar wiki** para documentação
5. **Atualizar índices** se necessário

---

## 📎 Integração com Sistema Existente

### 🔗 **Com wiki-json-navigation-rules.md**
- **Combinar consultas** de código-fonte e wiki
- **Usar hierarquia** estabelecida
- **Manter sincronização** entre fontes

### 🔗 **Com prompt-engineering-rules.md**
- **Otimizar consultas** usando índices
- **Melhorar precisão** com código real
- **Reduzir tempo** de resposta

---

## 🚀 Benefícios Esperados

### ⚡ **Performance**
- **Consultas 20x mais rápidas** via índice
- **Redução de 95%** no tempo de busca
- **Acesso direto** à implementação real

### 🎯 **Precisão**
- **Informação sempre atualizada** do código
- **Implementação real** vs documentação
- **Detecção de mudanças** automática

### 💰 **Eficiência**
- **Menor uso de recursos** computacionais
- **Consultas direcionadas** e precisas
- **Redução de processamento** desnecessário

### 🔍 **Descoberta**
- **Encontrar funcionalidades** ocultas
- **Entender implementação** real
- **Identificar dependências** não documentadas 