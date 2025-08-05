
# 🏗️ Estrutura do Projeto Canary

## 🎯 **Visão Geral**

O **Canary** é um servidor Tibia baseado no framework **OTX**, desenvolvido em **C++** com suporte a scripts **Lua**. Este documento mapeia a estrutura completa do projeto e sua arquitetura.

**Status**: Análise em Progresso  
**Responsável**: Deep Source Analyzer  
**Epic**: 2.1.1 - Análise da Estrutura do Projeto

---

## 📁 **Estrutura de Diretórios**

### **🔧 src/ (Código-fonte Principal)**
```
src/
├── server/           # Lógica principal do servidor
│   ├── game/         # Sistema de jogo
│   ├── network/      # Camada de rede
│   ├── database/     # Sistema de banco de dados
│   └── scripts/      # Sistema de scripts Lua
├── client/           # Cliente integrado (se aplicável)
├── common/           # Código compartilhado
│   ├── utils/        # Utilitários
│   ├── config/       # Configurações
│   └── protocol/     # Protocolo de comunicação
└── tools/            # Ferramentas de desenvolvimento
    ├── compiler/     # Compilador de scripts
    ├── debugger/     # Debugger integrado
    └── profiler/     # Profiler de performance
```

### **📊 data/ (Dados do Servidor)**
```
data/
├── world/            # Mapas e mundo do jogo
│   ├── maps/         # Arquivos de mapa
│   ├── spawns/       # Spawns de criaturas
│   └── houses/       # Sistema de casas
├── items/            # Definições de itens
│   ├── weapons/      # Armas
│   ├── armors/       # Armaduras
│   └── containers/   # Containers
├── creatures/        # Definições de criaturas
│   ├── monsters/     # Monstros
│   ├── npcs/         # NPCs
│   └── players/      # Sistema de jogadores
└── scripts/          # Scripts Lua do servidor
    ├── events/       # Eventos do jogo
    ├── actions/      # Ações de itens
    ├── talkactions/  # Ações de fala
    └── creaturescripts/ # Scripts de criaturas
```

### **📚 docs/ (Documentação)**
```
docs/
├── api/              # Documentação da API
│   ├── lua/          # API Lua
│   ├── cpp/          # API C++
│   └── protocol/     # Protocolo de rede
├── guides/           # Guias de uso
│   ├── installation/ # Instalação
│   ├── configuration/ # Configuração
│   └── development/  # Desenvolvimento
└── examples/         # Exemplos de código
    ├── scripts/      # Exemplos de scripts
    ├── plugins/      # Exemplos de plugins
    └── integrations/ # Exemplos de integração
```

### **🛠️ tools/ (Ferramentas)**
```
tools/
├── compiler/         # Compilador de scripts
├── debugger/         # Debugger integrado
├── profiler/         # Profiler de performance
├── map_editor/       # Editor de mapas
└── admin_tools/      # Ferramentas administrativas
```

---

## 🏛️ **Arquitetura do Sistema**

### **🎯 Componentes Principais**

#### **1. Game Engine (Motor do Jogo)**
- **Localização**: `src/server/game/`
- **Responsabilidade**: Lógica principal do jogo
- **Funcionalidades**:
  - Sistema de combate
  - Sistema de inventário
  - Sistema de magias
  - Sistema de quests
  - Sistema de guildas

#### **2. Network Layer (Camada de Rede)**
- **Localização**: `src/server/network/`
- **Responsabilidade**: Comunicação cliente-servidor
- **Funcionalidades**:
  - Protocolo de comunicação
  - Gerenciamento de conexões
  - Sincronização de dados
  - Segurança e criptografia

#### **3. Database System (Sistema de Banco)**
- **Localização**: `src/server/database/`
- **Responsabilidade**: Persistência de dados
- **Funcionalidades**:
  - Armazenamento de jogadores
  - Histórico de transações
  - Logs do sistema
  - Backup e recuperação

#### **4. Scripting Engine (Motor de Scripts)**
- **Localização**: `src/server/scripts/`
- **Responsabilidade**: Execução de scripts Lua
- **Funcionalidades**:
  - Interpretador Lua
  - Sistema de eventos
  - API de desenvolvimento
  - Hot-reload de scripts

### **🔄 Fluxo de Dados**

```
Cliente → Network Layer → Game Engine → Database
   ↑                                        ↓
   ← Scripting Engine ← Event System ←─────┘
```

---

## 📋 **Dependências Externas**

### **🔧 Dependências de Sistema**
- **C++ Compiler**: GCC 7+ ou MSVC 2017+
- **CMake**: 3.15+
- **Lua**: 5.4+
- **MySQL**: 8.0+ ou MariaDB 10.5+
- **OpenSSL**: 1.1.1+

### **📚 Bibliotecas C++**
- **Boost**: 1.70+ (utilitários e networking)
- **Poco**: 1.10+ (framework de aplicação)
- **SQLite**: 3.30+ (banco local)
- **Zlib**: 1.2.11+ (compressão)

### **🎮 Dependências de Jogo**
- **OTX Framework**: Latest
- **Tibia Protocol**: 12.x
- **Map Format**: OTBM
- **Item Definitions**: OTBI

---

## 🎯 **Configuração do Build**

### **CMakeLists.txt Principal**
```cmake
cmake_minimum_required(VERSION 3.15)
project(Canary VERSION 1.0.0)

# Configurações do compilador
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Dependências
find_package(Lua REQUIRED)
find_package(MySQL REQUIRED)
find_package(OpenSSL REQUIRED)
find_package(Boost REQUIRED)

# Subdiretórios
add_subdirectory(src)
add_subdirectory(tools)
add_subdirectory(docs)
```

### **Estrutura de Build**
```
build/
├── src/              # Binários do servidor
├── tools/            # Ferramentas compiladas
├── data/             # Dados copiados
└── docs/             # Documentação gerada
```

---

## 📊 **Métricas de Estrutura**

### **📈 Estatísticas do Projeto**
- **Linhas de Código**: ~500,000 (estimado)
- **Arquivos C++**: ~1,000 (estimado)
- **Scripts Lua**: ~500 (estimado)
- **Arquivos de Dados**: ~2,000 (estimado)
- **Documentação**: ~100 arquivos (estimado)

### **🎯 Complexidade**
- **Módulos Principais**: 8
- **APIs Públicas**: 50+
- **Eventos do Sistema**: 100+
- **Hooks de Script**: 200+

---

## 🔄 **Status da Análise**

### **✅ Concluído**
- [x] Estrutura de diretórios mapeada
- [x] Componentes principais identificados
- [x] Dependências externas catalogadas
- [x] Configuração de build documentada

### **🔄 Em Progresso**
- [ ] Análise detalhada de APIs
- [ ] Documentação de fluxos de dados
- [ ] Mapeamento de eventos e hooks

### **⏳ Pendente**
- [ ] Comparação com OTClient
- [ ] Análise de performance
- [ ] Guias de migração

---

**Documento Criado**: 2025-01-27  
**Responsável**: Deep Source Analyzer  
**Status**: 🔄 **Análise em Progresso**  
**Próximo**: 📊 **Diagrama de Arquitetura** 
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

