# Wiki JSON Navigation Rules

## 📋 Regras de Navegação JSON para Wiki

Este arquivo define as regras para **navegação baseada em JSON** da wiki do OTClient, garantindo consultas rápidas, atualizações eficientes e produtividade máxima.

---

## 🎯 Regras Principais

### 1. **JSON como Padrão de Navegação**
**SEMPRE use arquivos JSON como meio principal de navegação durante consultas da wiki e regras.** Priorize consultas via JSON sobre busca direta em arquivos markdown.

### 2. **Índice Centralizado de Tags**
**Mantenha um arquivo `wiki/tags_index.json` sempre atualizado** com todas as tags da wiki organizadas por arquivo. Este é o ponto de entrada principal para consultas.

### 3. **Mapas de Navegação Obrigatórios**
**SEMPRE consulte os mapas JSON antes de acessar arquivos markdown diretamente.** Use a hierarquia: `tags_index.json` → `wiki_map.json` → `relationships.json` → arquivo markdown.

### 4. **Atualização Automática de Índices**
**SEMPRE atualize os arquivos JSON quando criar, modificar ou remover documentos da wiki.** Execute scripts de atualização automática após qualquer mudança.

### 5. **Estrutura de Consulta Padronizada**
**Use a estrutura de consulta estabelecida:**
1. **Primeiro**: Consultar `wiki/tags_index.json` para localizar arquivos
2. **Segundo**: Usar `wiki/maps/wiki_map.json` para metadados e status
3. **Terceiro**: Consultar `wiki/relationships.json` para dependências
4. **Quarto**: Acessar arquivo markdown apenas se necessário

---

## 📁 Estrutura de Arquivos JSON

### 🗂️ **Arquivos Obrigatórios**

| Arquivo | Propósito | Atualização |
|---------|-----------|-------------|
| `wiki/tags_index.json` | **Índice principal** de tags e arquivos | Automática |
| `wiki/maps/wiki_map.json` | **Mapa completo** da wiki com metadados | Automática |
| `wiki/relationships.json` | **Relacionamentos** entre documentos | Automática |
| `wiki/search_index.json` | **Índice de busca** otimizado | Automática |

### 📋 **Estrutura do tags_index.json**
```json
{
  "metadata": {
    "version": "1.0",
    "last_updated": "2025-01-27T10:00:00Z",
    "total_files": 16,
    "total_tags": 45
  },
  "files_by_tag": {
    "ui": [
      "UI_System_Guide.md",
      "UIWidget_Reference (1).md",
      "OTUI_Module_Development_Guide.md"
    ],
    "game": [
      "Combat_System_Guide.md",
      "Map_System_Guide.md",
      "Effects_System_Guide.md"
    ]
  },
  "tags_by_file": {
    "Getting_Started_Guide.md": ["otclient", "getting-started", "tutorial", "beginner"],
    "Module_System_Guide.md": ["otclient", "modules", "system", "development"]
  }
}
```

### 📋 **Estrutura do wiki_map.json**
```json
{
  "metadata": {
    "version": "1.0",
    "last_updated": "2025-01-27T10:00:00Z",
    "total_documents": 16,
    "categories": 4
  },
  "categories": {
    "core_systems": {
      "name": "Sistemas Core",
      "description": "Sistemas fundamentais do OTClient",
      "documents": [
        {
          "id": "module_system",
          "title": "Module System Guide",
          "file": "Module_System_Guide.md",
          "status": "completed",
          "priority": 1,
          "tags": ["modules", "system", "development"],
          "dependencies": [],
          "related": ["otui_development", "ui_system"]
        }
      ]
    }
  }
}
```

---

## 🔄 Processo de Consulta

### 📋 **Fluxo de Consulta Padrão**

Para qualquer consulta da wiki:

1. **Consultar `tags_index.json`** para localizar arquivos relevantes
2. **Usar `wiki_map.json`** para obter metadados e status
3. **Verificar `relationships.json`** para dependências e relacionamentos
4. **Acessar arquivo markdown** apenas se necessário para conteúdo detalhado

### 🎯 **Exemplos de Consulta**

#### **Busca por Tag**
```bash
# Buscar todos os documentos sobre UI
curl -s wiki/tags_index.json | jq '.files_by_tag.ui'
```

#### **Busca por Status**
```bash
# Verificar documentos completos
curl -s wiki/maps/wiki_map.json | jq '.categories[].documents[] | select(.status == "completed")'
```

#### **Busca por Relacionamentos**
```bash
# Encontrar dependências de um documento
curl -s wiki/relationships.json | jq '.Getting_Started_Guide.md.dependencies'
```

---

## ⚡ Atualização Automática

### 🔧 **Scripts Obrigatórios**

#### **1. Atualizar tags_index.json**
```python
def update_tags_index():
    """Atualiza o índice de tags da wiki"""
    # Ler todos os arquivos markdown
    # Extrair tags do frontmatter
    # Gerar estrutura JSON
    # Salvar tags_index.json
```

#### **2. Atualizar wiki_map.json**
```python
def update_wiki_map():
    """Atualiza o mapa principal da wiki"""
    # Ler metadados dos documentos
    # Organizar por categorias
    # Gerar estrutura hierárquica
    # Salvar wiki_map.json
```

#### **3. Atualizar relationships.json**
```python
def update_relationships():
    """Atualiza relacionamentos entre documentos"""
    # Analisar links internos
    # Identificar dependências
    # Gerar grafo de relacionamentos
    # Salvar relationships.json
```

### 📋 **Trigger de Atualização**

**SEMPRE execute scripts de atualização quando:**
- ✅ Criar novo documento na wiki
- ✅ Modificar documento existente
- ✅ Remover documento da wiki
- ✅ Alterar tags ou frontmatter
- ✅ Modificar relacionamentos

---

## 🎯 Regras de Performance

### ⚡ **Otimização de Consultas**

1. **Cache de JSON**: Mantenha JSONs em memória durante sessão
2. **Consulta Indexada**: Use índices para busca rápida
3. **Lazy Loading**: Carregue conteúdo markdown apenas quando necessário
4. **Compressão**: Use JSON compactado para arquivos grandes

### 📊 **Métricas de Performance**

| Operação | Tempo Máximo | Método |
|----------|--------------|--------|
| **Busca por tag** | < 100ms | JSON indexado |
| **Busca por status** | < 100ms | JSON indexado |
| **Busca por relacionamento** | < 100ms | JSON indexado |
| **Leitura de conteúdo** | < 500ms | Markdown direto |

---

## ⚠️ Regras de Exceção

### 1. **Conteúdo Detalhado**
Para conteúdo detalhado ou exemplos de código, acesse arquivo markdown diretamente.

### 2. **Busca de Texto Completo**
Para busca de texto dentro dos documentos, use ferramentas de busca específicas.

### 3. **Edição de Documentos**
Para edição, sempre acesse arquivo markdown original.

---

## 📚 Exemplos de Uso

### 🔍 **Consulta de Documentos por Categoria**
```python
# Buscar todos os documentos de UI
with open('wiki/tags_index.json', 'r') as f:
    data = json.load(f)
    ui_docs = data['files_by_tag']['ui']
    print(f"Documentos de UI: {ui_docs}")
```

### 📊 **Análise de Progresso**
```python
# Verificar progresso da documentação
with open('wiki/maps/wiki_map.json', 'r') as f:
    data = json.load(f)
    completed = sum(1 for cat in data['categories'].values() 
                   for doc in cat['documents'] 
                   if doc['status'] == 'completed')
    total = data['metadata']['total_documents']
    print(f"Progresso: {completed}/{total} ({completed/total*100:.1f}%)")
```

### 🔗 **Navegação por Relacionamentos**
```python
# Encontrar próximos passos
with open('wiki/relationships.json', 'r') as f:
    data = json.load(f)
    next_steps = data['Getting_Started_Guide.md']['next_steps']
    print(f"Próximos passos: {next_steps}")
```

---

## ✅ Tarefa Obrigatória da IA

**SEMPRE que uma consulta da wiki for solicitada:**

1. **Consultar primeiro** `wiki/tags_index.json`
2. **Usar metadados** de `wiki/maps/wiki_map.json`
3. **Verificar relacionamentos** em `wiki/relationships.json`
4. **Acessar markdown** apenas se necessário
5. **Atualizar JSONs** após qualquer modificação

---

## 📎 Integração com Sistema Existente

### 🔗 **Com cursor.md**
- **Consultar JSONs** antes de acessar regras
- **Usar índices** para navegação rápida
- **Manter sincronização** entre regras e wiki

### 🔗 **Com prompt-engineering-rules.md**
- **Otimizar consultas** usando estrutura JSON
- **Melhorar velocidade** de resposta
- **Reduzir custo** de processamento

---

## 🚀 Benefícios Esperados

### ⚡ **Performance**
- **Consultas 10x mais rápidas** via JSON indexado
- **Redução de 90%** no tempo de busca
- **Cache eficiente** de metadados

### 🔄 **Produtividade**
- **Navegação intuitiva** por relacionamentos
- **Atualizações automáticas** de índices
- **Consistência garantida** entre documentos

### 💰 **Eficiência**
- **Menor uso de recursos** computacionais
- **Consultas otimizadas** e direcionadas
- **Redução de processamento** desnecessário 