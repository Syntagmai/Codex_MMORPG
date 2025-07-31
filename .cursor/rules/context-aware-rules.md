# Regras de Contexto Inteligente - Detecção Automática de Repositório

## 🎯 **Objetivo**

Criar um sistema que detecte automaticamente em qual repositório estamos trabalhando (OTClient, Canary, ou futuro repositório unificado) e adapte o comportamento da IA de acordo com o contexto.

---

## 🔍 **Sistema de Detecção de Contexto**

### 📊 **Detecção Automática de Repositório**

#### **1. Análise de Estrutura de Pastas**
```python
def detect_repository_context():
    """
    Detecta automaticamente o contexto do repositório atual
    Retorna: 'otclient', 'canary', 'unified', ou 'unknown'
    """
    indicators = {
        'otclient': [
            'src/client/', 'modules/', 'data/', 'CMakeLists.txt',
            'otclient_source_index.json', 'README.md (OTClient)'
        ],
        'canary': [
            'src/game/', 'src/account/', 'src/creatures/',
            'canary_source_index.json', 'README.md (Canary)'
        ],
        'unified': [
            'wiki/otclient/', 'wiki/canary/', 'wiki/integration/',
            'unified_wiki_index.json'
        ]
    }
    
    # Verificar estrutura atual
    current_structure = analyze_current_structure()
    
    # Determinar contexto
    for repo_type, markers in indicators.items():
        if all_markers_present(markers, current_structure):
            return repo_type
    
    return 'unknown'
```

#### **2. Análise de Conteúdo**
```python
def analyze_content_context():
    """
    Analisa o conteúdo para determinar o contexto
    """
    content_indicators = {
        'otclient': [
            'OTClient', 'client', 'UI', 'widgets', 'rendering',
            'g_ui', 'UIWidget', 'modules'
        ],
        'canary': [
            'Canary', 'server', 'game logic', 'database',
            'creatures', 'items', 'world management'
        ],
        'unified': [
            'integration', 'cross-project', 'OTClient + Canary',
            'ecosystem', 'protocol layer'
        ]
    }
    
    # Analisar arquivos principais
    main_files = ['README.md', 'CMakeLists.txt', 'cursor.md']
    content_analysis = {}
    
    for file in main_files:
        if file_exists(file):
            content = read_file_content(file)
            content_analysis[file] = content
    
    return determine_context_from_content(content_analysis)
```

### 🎯 **Contextos Identificados**

#### **📱 Contexto OTClient**
- **Detecção**: Presença de `src/client/`, `modules/`, `data/`
- **Foco**: Cliente, UI, rendering, módulos
- **Wiki**: `wiki/otclient/` (documentação do cliente)
- **Integração**: `wiki/integration/` (pontos de integração)

#### **🖥️ Contexto Canary**
- **Detecção**: Presença de `src/game/`, `src/account/`, `src/creatures/`
- **Foco**: Servidor, lógica de jogo, banco de dados
- **Wiki**: `wiki/canary/` (documentação do servidor)
- **Integração**: `wiki/integration/` (pontos de integração)

#### **🌐 Contexto Unificado**
- **Detecção**: Presença de `wiki/otclient/` E `wiki/canary/`
- **Foco**: Ecossistema completo, integração
- **Wiki**: `wiki/` (documentação completa)
- **Integração**: `wiki/integration/` (documentação compartilhada)

---

## 🔧 **Adaptação Automática do Sistema**

### 📁 **Estrutura de Pastas Contextual**

#### **Para Contexto OTClient:**
```
wiki/
├── otclient/          # Documentação específica do cliente
├── integration/       # Pontos de integração com Canary
├── update/           # Scripts de atualização
├── maps/             # Mapas JSON
└── habdel/           # Documentação original
```

#### **Para Contexto Canary:**
```
wiki/
├── canary/           # Documentação específica do servidor
├── integration/      # Pontos de integração com OTClient
├── update/           # Scripts de atualização
├── maps/             # Mapas JSON
└── habdel/           # Documentação original
```

#### **Para Contexto Unificado:**
```
wiki/
├── otclient/         # Documentação do cliente
├── canary/           # Documentação do servidor
├── integration/      # Documentação compartilhada
├── update/           # Scripts de atualização
├── maps/             # Mapas JSON unificados
└── habdel/           # Documentação original
```

### 🗺️ **Mapas JSON Contextuais**

#### **Estrutura de Mapas por Contexto**
```json
{
  "context": "otclient|canary|unified",
  "detected_at": "2025-01-27T02:10:00Z",
  "repository_type": "client|server|ecosystem",
  "integration_enabled": true|false,
  "maps": {
    "otclient": {
      "source_index": "wiki/maps/otclient_source_index.json",
      "wiki_map": "wiki/maps/otclient_wiki_map.json",
      "tags_index": "wiki/maps/otclient_tags_index.json"
    },
    "canary": {
      "source_index": "wiki/maps/canary_source_index.json", 
      "wiki_map": "wiki/maps/canary_wiki_map.json",
      "tags_index": "wiki/maps/canary_tags_index.json"
    },
    "integration": {
      "cross_project_map": "wiki/maps/integration_map.json",
      "protocol_map": "wiki/maps/protocol_map.json",
      "relationship_map": "wiki/maps/cross_project_relationships.json"
    }
  }
}
```

### 🔄 **Scripts de Atualização Contextuais**

#### **Scripts Baseados no Contexto**
```python
class ContextAwareUpdater:
    def __init__(self):
        self.context = self.detect_context()
        self.scripts = self.get_context_scripts()
    
    def get_context_scripts(self):
        if self.context == "otclient":
            return [
                "wiki/update/update_otclient_source_index.py",
                "wiki/update/update_otclient_wiki_maps.py",
                "wiki/update/update_integration_maps.py"
            ]
        elif self.context == "canary":
            return [
                "wiki/update/update_canary_source_index.py",
                "wiki/update/update_canary_wiki_maps.py", 
                "wiki/update/update_integration_maps.py"
            ]
        elif self.context == "unified":
            return [
                "wiki/update/update_unified_source_index.py",
                "wiki/update/update_unified_wiki_maps.py",
                "wiki/update/update_integration_maps.py",
                "wiki/update/update_cross_project_maps.py"
            ]
```

---

## 📝 **Regras de Comportamento Contextual**

### 🎯 **Para Contexto OTClient**

#### **Criação de Documentos:**
- **Localização**: `wiki/otclient/`
- **Foco**: Cliente, UI, módulos, rendering
- **Integração**: Sempre incluir seções de integração com Canary
- **Tags**: `otclient`, `client`, `ui`, `modules` + tags de integração

#### **Mapas JSON:**
- **Prefixo**: `otclient_` para mapas específicos
- **Integração**: Incluir mapas de integração
- **Referências**: Links para Canary Wiki (quando disponível)

#### **Scripts de Atualização:**
- **Foco**: Código-fonte do OTClient
- **Integração**: Atualizar mapas de integração
- **Contexto**: Sempre considerar integração com servidor

### 🖥️ **Para Contexto Canary**

#### **Criação de Documentos:**
- **Localização**: `wiki/canary/`
- **Foco**: Servidor, lógica de jogo, banco de dados
- **Integração**: Sempre incluir seções de integração com OTClient
- **Tags**: `canary`, `server`, `game-logic`, `database` + tags de integração

#### **Mapas JSON:**
- **Prefixo**: `canary_` para mapas específicos
- **Integração**: Incluir mapas de integração
- **Referências**: Links para OTClient Wiki

#### **Scripts de Atualização:**
- **Foco**: Código-fonte do Canary
- **Integração**: Atualizar mapas de integração
- **Contexto**: Sempre considerar integração com cliente

### 🌐 **Para Contexto Unificado**

#### **Criação de Documentos:**
- **Localização**: `wiki/otclient/` ou `wiki/canary/` conforme o foco
- **Foco**: Ecossistema completo, integração total
- **Integração**: Documentação unificada e compartilhada
- **Tags**: `unified`, `ecosystem`, `integration` + tags específicas

#### **Mapas JSON:**
- **Estrutura**: Mapas unificados com seções por projeto
- **Integração**: Mapas de relacionamento cruzado
- **Contexto**: Visão completa do ecossistema

#### **Scripts de Atualização:**
- **Foco**: Ambos os projetos simultaneamente
- **Integração**: Sincronização completa entre projetos
- **Contexto**: Manutenção do ecossistema unificado

---

## 🔄 **Sistema de Atualização Automática**

### 📋 **Tarefa Obrigatória da IA**

**SEMPRE que iniciar qualquer tarefa:**

1. **Detectar contexto** automaticamente
2. **Adaptar comportamento** baseado no contexto
3. **Usar estrutura correta** de pastas e arquivos
4. **Aplicar regras específicas** do contexto
5. **Manter integração** quando relevante

### 🔍 **Detecção de Contexto**
```python
def get_context_rules():
    """
    Retorna regras específicas baseadas no contexto detectado
    """
    context = detect_repository_context()
    
    rules = {
        'otclient': {
            'docs_path': 'wiki/otclient/',
            'integration_path': 'wiki/integration/',
            'focus': 'client_side',
            'integration_enabled': True
        },
        'canary': {
            'docs_path': 'wiki/canary/',
            'integration_path': 'wiki/integration/',
            'focus': 'server_side',
            'integration_enabled': True
        },
        'unified': {
            'docs_path': 'wiki/',
            'integration_path': 'wiki/integration/',
            'focus': 'ecosystem',
            'integration_enabled': True
        }
    }
    
    return rules.get(context, rules['unknown'])
```

### 📊 **Validação de Contexto**
```python
def validate_context_consistency():
    """
    Valida se a estrutura está consistente com o contexto
    """
    context = detect_repository_context()
    expected_structure = get_expected_structure(context)
    current_structure = analyze_current_structure()
    
    inconsistencies = []
    
    for expected_path in expected_structure:
        if not path_exists(expected_path):
            inconsistencies.append(f"Missing: {expected_path}")
    
    if inconsistencies:
        print(f"⚠️ Context inconsistencies detected:")
        for issue in inconsistencies:
            print(f"  - {issue}")
        
        return False
    
    return True
```

---

## 🎯 **Benefícios do Sistema Contextual**

### 📈 **Para Desenvolvimento**
- **Adaptação Automática**: Sistema se adapta ao contexto
- **Consistência**: Estrutura padronizada por contexto
- **Escalabilidade**: Fácil expansão para novos contextos
- **Manutenção**: Regras específicas por contexto

### 🏗️ **Para o Projeto**
- **Flexibilidade**: Funciona em qualquer repositório
- **Integração**: Mantém pontos de integração sempre
- **Evolução**: Suporta evolução para repositório unificado
- **Qualidade**: Validação automática de consistência

### 🔄 **Para Futuras Expansões**
- **Novos Projetos**: Fácil adição de novos contextos
- **Migração**: Transição suave entre contextos
- **Automação**: Detecção e adaptação automática
- **Padrão**: Estrutura replicável para outros projetos

---

## ⚠️ **Regras de Exceção**

### 🚫 **O que NÃO Fazer**
- **Ignorar Contexto**: Sempre detectar e adaptar
- **Misturar Contextos**: Manter separação clara
- **Quebrar Integração**: Sempre manter pontos de integração
- **Assumir Contexto**: Sempre verificar automaticamente

### ✅ **O que SEMPRE Fazer**
- **Detectar Contexto**: Antes de qualquer operação
- **Adaptar Comportamento**: Baseado no contexto detectado
- **Manter Integração**: Quando relevante
- **Validar Consistência**: Verificar estrutura correta

---

## 🔄 **Sistema de Migração**

### 📋 **Migração entre Contextos**
```python
def migrate_context(from_context, to_context):
    """
    Migra de um contexto para outro
    """
    # 1. Validar contexto atual
    validate_current_context(from_context)
    
    # 2. Preparar estrutura de destino
    prepare_target_structure(to_context)
    
    # 3. Migrar documentos
    migrate_documents(from_context, to_context)
    
    # 4. Atualizar mapas
    update_maps_for_context(to_context)
    
    # 5. Validar nova estrutura
    validate_context_consistency()
```

### 🎯 **Migração para Unificado**
```python
def prepare_for_unified_migration():
    """
    Prepara migração para repositório unificado
    """
    # 1. Criar estrutura unificada
    create_unified_structure()
    
    # 2. Migrar documentos OTClient
    migrate_otclient_docs()
    
    # 3. Preparar para Canary
    prepare_canary_structure()
    
    # 4. Configurar integração
    setup_unified_integration()
    
    # 5. Atualizar regras
    update_context_rules()
```

---

## 🎉 **Conclusão**

Este sistema de contexto inteligente permite que a IA trabalhe eficientemente em qualquer repositório (OTClient, Canary, ou futuro unificado), adaptando automaticamente seu comportamento e mantendo sempre a integração entre projetos.

### 🚀 **Próximos Passos**
1. **Implementar detecção automática** em todos os scripts
2. **Criar scripts contextuais** para cada tipo de repositório
3. **Preparar estrutura para Canary** quando disponível
4. **Estabelecer processo de migração** para repositório unificado

**O sistema agora é totalmente contextual e preparado para evolução!** 🎮 