
# CANARY-001: Configurar Ambiente de Pesquisa Canary

## 🎯 **Objetivo da Story**

Configurar o ambiente de pesquisa para análise profunda do sistema Canary usando metodologia Habdel, incluindo análise das tasks do Epic 4 para identificar oportunidades de integração com OTClient.

## 📋 **Critérios de Aceitação**

- [x] **Ambiente configurado** para pesquisa Canary
- [x] **Estrutura do sistema** mapeada
- [x] **Análise do Epic 4** realizada
- [x] **Oportunidades de integração** identificadas
- [x] **Metodologia Habdel** aplicada

## 🔍 **Análise do Sistema Canary**

### **📊 Visão Geral**

O **Canary** é um servidor MMORPG open-source desenvolvido em C++ que funciona como um fork do projeto OTServBR-Global. É um servidor robusto e modular que oferece uma arquitetura completa para jogos MMORPG baseados em Tibia.

### **🏗️ Arquitetura do Sistema**

```
Canary System Architecture
   │
   ├─ Core Systems
   │   ├─ CanaryServer (Main Server)
   │   ├─ ServiceManager
   │   ├─ Logger
   │   └─ RSA Security
   │
   ├─ Game Systems
   │   ├─ Game Engine
   │   ├─ Combat System
   │   ├─ Movement System
   │   ├─ Scheduling
   │   └─ Zones
   │
   ├─ Creature Systems
   │   ├─ Players
   │   ├─ NPCs
   │   ├─ Monsters
   │   ├─ Combat
   │   └─ Interactions
   │
   ├─ Data Systems
   │   ├─ Database
   │   ├─ Items
   │   ├─ Map
   │   └─ Config
   │
   ├─ Network Systems
   │   ├─ IO Management
   │   ├─ Protocol Handling
   │   └─ Connection Management
   │
   └─ Scripting Systems
       ├─ Lua Engine
       ├─ Scripts
       ├─ Modules
       └─ Functions
```

### **📁 Estrutura de Diretórios**

#### **Diretórios Principais**

| Diretório | Propósito | Status |
|-----------|-----------|--------|
| `src/` | Código-fonte principal | ✅ Disponível |
| `src/game/` | Sistemas de jogo | ✅ Disponível |
| `src/creatures/` | Sistema de criaturas | ✅ Disponível |
| `src/lua/` | Sistema de scripting | ✅ Disponível |
| `src/database/` | Sistema de banco de dados | ✅ Disponível |
| `src/io/` | Sistema de I/O | ✅ Disponível |
| `src/map/` | Sistema de mapas | ✅ Disponível |
| `src/items/` | Sistema de itens | ✅ Disponível |
| `data/` | Dados do servidor | ✅ Disponível |
| `config.lua.dist` | Configuração padrão | ✅ Disponível |

#### **Arquivos de Configuração**

**config.lua.dist** - Configuração principal do servidor:
```lua
-- Core settings
    --  Core settings (traduzido)
useAnyDatapackFolder = false
dataPackDirectory = "data-otservbr-global"
coreDirectory = "data"

-- Log level
    --  Log level (traduzido)
logLevel = "info"

-- Combat settings
    --  Combat settings (traduzido)
worldType = "pvp"
protectionLevel = 7
pzLocked = 60 * 1000

-- Connection Config
    --  Connection Config (traduzido)
ip = "127.0.0.1"
loginProtocolPort = 7171
gameProtocolPort = 7172
statusProtocolPort = 7171
maxPlayers = 0
serverName = "OTServBR-Global"

-- Packet Compression
    --  Packet Compression (traduzido)
packetCompressionLevel = 6

-- Item and containers limit
    --  Item and containers limit (traduzido)
maxItem = 5000
maxContainer = 500
maxContainerDepth = 200
```

### **🔧 Componentes Principais**

#### **1. CanaryServer (Main Server)**
```cpp
class CanaryServer {
    -- Classe: CanaryServer
public:
    explicit CanaryServer(
        Logger &logger,
        RSA &rsa,
        ServiceManager &serviceManager
    );

    int run();

private:
    void loadConfigLua();
    void validateDatapack();
    void initializeDatabase();
    void loadModules();
    void setWorldType();
    void loadMaps() const;
    void setupHousesRent();
};
```

#### **2. Game Engine**
- **Localização**: `src/game/`
- **Arquivos Principais**: `game.hpp`, `game.cpp`
- **Funcionalidades**: Lógica principal do jogo, combate, movimento

#### **3. Creature System**
- **Localização**: `src/creatures/`
- **Subsistemas**:
  - `players/` - Sistema de jogadores
  - `npcs/` - Sistema de NPCs
  - `monsters/` - Sistema de monstros
  - `combat/` - Sistema de combate
  - `interactions/` - Sistema de interações

#### **4. Lua Scripting**
- **Localização**: `src/lua/`
- **Subsistemas**:
  - `scripts/` - Scripts Lua
  - `modules/` - Módulos Lua
  - `functions/` - Funções Lua
  - `callbacks/` - Callbacks Lua

## 🔗 **Links Automáticos**

> [!info] **Links Gerados Automaticamente**
> Estes links foram criados automaticamente pelo sistema de linkagem da categoria **Legacy**

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]
- [[../maps/search_index|Busca em Arquivos Legados]]
- [[../legacy_docs/README|Documentação Legada]]

### **🧭 Navegação**
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]
- [[../maps/category_indices|Índices por Categoria]]
- [[../maps/relationships|Relacionamentos]]

### **📊 Métricas da Categoria**
- **Categoria**: Legacy
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

## 🔗 **Análise do Epic 4 - Integração e Comparação**

### **📋 Tasks Existentes do Epic 4**

| Task | Descrição | Status | Análise |
|------|-----------|--------|---------|
| **4.1** | INTEGRATION-001: Comparação de Arquiteturas | ⏳ Pendente | 🔍 **Revisar** |
| **4.2** | INTEGRATION-002: Análise de Protocolos | ⏳ Pendente | 🔍 **Revisar** |
| **4.3** | INTEGRATION-003: Comparação de UI | ⏳ Pendente | 🔍 **Revisar** |
| **4.4** | INTEGRATION-004: Análise de Performance | ⏳ Pendente | 🔍 **Revisar** |
| **4.5** | INTEGRATION-005: Comparação de Funcionalidades | ⏳ Pendente | 🔍 **Revisar** |
| **4.6** | INTEGRATION-006: Guias de Migração | ⏳ Pendente | 🔍 **Revisar** |
| **4.7** | INTEGRATION-007: Padrões Comuns | ⏳ Pendente | 🔍 **Revisar** |
| **4.8** | INTEGRATION-008: APIs Unificadas | ⏳ Pendente | 🔍 **Revisar** |
| **4.9** | INTEGRATION-009: Validação de Integração | ⏳ Pendente | 🔍 **Revisar** |
| **4.10** | INTEGRATION-010: Documentação Final | ⏳ Pendente | 🔍 **Revisar** |

### **🎯 Oportunidades de Integração Identificadas**

#### **1. Comparação de Arquiteturas (INTEGRATION-001)**

**Análise Inicial**:
- **OTClient**: Cliente C++ com Lua, foco em UI e comunicação
- **Canary**: Servidor C++ com Lua, foco em lógica de jogo e dados
- **Oportunidade**: Mapear pontos de integração cliente-servidor

**Nova Task Proposta**:
```
INTEGRATION-001.1: Mapear APIs Cliente-Servidor
- Identificar APIs OTClient que se comunicam com Canary
- Documentar protocolos de comunicação
- Mapear pontos de integração
```

#### **2. Análise de Protocolos (INTEGRATION-002)**

**Análise Inicial**:
- **OTClient**: Protocolo de comunicação cliente
- **Canary**: Protocolo de comunicação servidor
- **Oportunidade**: Documentar protocolos compartilhados

**Nova Task Proposta**:
```
INTEGRATION-002.1: Documentar Protocolos Compartilhados
- Protocolo de login/autenticação
- Protocolo de comunicação em tempo real
- Protocolo de sincronização de dados
```

#### **3. Comparação de Funcionalidades (INTEGRATION-005)**

**Análise Inicial**:
- **OTClient**: 21 sistemas (Core, UI, Game, Social, Support)
- **Canary**: Sistemas de servidor (Game, Creatures, Data, Network)
- **Oportunidade**: Mapear correspondências entre sistemas

**Nova Task Proposta**:
```
INTEGRATION-005.1: Mapear Correspondências de Sistemas
- OTClient Chat ↔ Canary Communication
- OTClient Configuration ↔ Canary Config
- OTClient Logs ↔ Canary Logger
- OTClient Game Systems ↔ Canary Game Engine
```

#### **4. APIs Unificadas (INTEGRATION-008)**

**Análise Inicial**:
- **OTClient**: APIs Lua para client-side
- **Canary**: APIs Lua para server-side
- **Oportunidade**: Criar APIs unificadas

**Nova Task Proposta**:
```
INTEGRATION-008.1: Design de APIs Unificadas
- APIs Lua compartilhadas
- Padrões de comunicação
- Interfaces unificadas
```

## 📊 **Métricas de Configuração**

### **Cobertura de Análise**

| Componente | Status | Complexidade | Prioridade |
|------------|--------|--------------|------------|
| **Core Systems** | ✅ Mapeado | Alta | 🔥 Crítica |
| **Game Systems** | ✅ Mapeado | Alta | 🔥 Crítica |
| **Creature Systems** | ✅ Mapeado | Média | ⚡ Alta |
| **Data Systems** | ✅ Mapeado | Média | ⚡ Alta |
| **Network Systems** | ✅ Mapeado | Alta | 🔥 Crítica |
| **Scripting Systems** | ✅ Mapeado | Média | ⚡ Alta |

### **Análise do Epic 4**

| Aspecto | Status | Impacto | Ação |
|---------|--------|---------|------|
| **Tasks Existentes** | ✅ Identificadas | Alto | Revisar e expandir |
| **Oportunidades** | ✅ Identificadas | Alto | Criar novas tasks |
| **Integração** | 🔍 Em análise | Crítico | Mapear pontos |
| **Protocolos** | 🔍 Em análise | Crítico | Documentar |

## 🎯 **Recomendações para Epic 4**

### **Tasks Adicionais Propostas**

#### **INTEGRATION-001.1: Mapear APIs Cliente-Servidor**
- **Objetivo**: Identificar pontos de integração entre OTClient e Canary
- **Entregáveis**: Documentação de APIs, protocolos de comunicação
- **Prioridade**: 🔥 Crítica

#### **INTEGRATION-002.1: Documentar Protocolos Compartilhados**
- **Objetivo**: Documentar protocolos de comunicação cliente-servidor
- **Entregáveis**: Especificação de protocolos, exemplos de implementação
- **Prioridade**: 🔥 Crítica

#### **INTEGRATION-005.1: Mapear Correspondências de Sistemas**
- **Objetivo**: Mapear correspondências entre sistemas OTClient e Canary
- **Entregáveis**: Matriz de correspondências, análise de gaps
- **Prioridade**: ⚡ Alta

#### **INTEGRATION-008.1: Design de APIs Unificadas**
- **Objetivo**: Projetar APIs unificadas para o ecossistema completo
- **Entregáveis**: Design de APIs, protótipos, documentação
- **Prioridade**: ⚡ Alta

### **Estratégia de Integração**

#### **Fase 1: Análise (Epic 2)**
1. **Completar pesquisa Canary**: Entender completamente o sistema
2. **Mapear correspondências**: Identificar pontos de integração
3. **Documentar protocolos**: Especificar comunicação

#### **Fase 2: Design (Epic 4)**
1. **Projetar APIs unificadas**: Criar interfaces compartilhadas
2. **Definir padrões**: Estabelecer convenções
3. **Criar protótipos**: Validar conceitos

#### **Fase 3: Implementação (Epic 4)**
1. **Implementar integração**: Desenvolver soluções
2. **Testar funcionalidade**: Validar integração
3. **Documentar resultados**: Criar guias finais

## 🚀 **Próximos Passos**

### **Imediato**

1. **Continuar Epic 2**: Executar CANARY-002 a CANARY-023
2. **Aplicar metodologia Habdel**: Usar padrões validados do OTClient
3. **Documentar descobertas**: Registrar insights para Epic 4

### **Curto Prazo**

1. **Revisar Epic 4**: Expandir tasks baseado em descobertas
2. **Criar novas tasks**: Adicionar tasks de integração específicas
3. **Preparar comparação**: Coletar dados para análise comparativa

### **Longo Prazo**

1. **Implementar integração**: Desenvolver soluções unificadas
2. **Validar ecossistema**: Testar integração completa
3. **Documentar resultados**: Criar documentação final

## 🎯 **Conclusão**

A **configuração do ambiente de pesquisa Canary** estabelece:

### **✅ Conquistas Principais**

1. **Ambiente Configurado**: Estrutura do sistema mapeada
2. **Análise Inicial**: Componentes principais identificados
3. **Epic 4 Revisado**: Oportunidades de integração identificadas
4. **Metodologia Aplicada**: Habdel validada do OTClient

### **🔍 Insights para Integração**

1. **Arquitetura Complementar**: OTClient (cliente) + Canary (servidor)
2. **Protocolos Compartilhados**: Comunicação cliente-servidor
3. **APIs Unificadas**: Possibilidade de interfaces compartilhadas
4. **Sistemas Correspondentes**: Mapeamento entre funcionalidades

### **📊 Impacto no Projeto**

- **Epic 2 Preparado**: Base para pesquisa Canary
- **Epic 4 Expandido**: Novas tasks de integração identificadas
- **Visão Unificada**: Ecossistema OTClient-Canary mapeado
- **Metodologia Validada**: Habdel pronta para aplicação

A configuração estabelece uma base sólida para a pesquisa Canary e identifica oportunidades significativas para integração com OTClient, preparando o terreno para o Epic 4 expandido.

---

**Status**: ✅ **COMPLETA**  
**Próximo**: 🎯 **CANARY-002: Análise da Arquitetura Core** 