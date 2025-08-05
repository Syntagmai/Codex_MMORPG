---
tags: [concept, canary, server, overview, beginner, education]
type: concept
status: active
priority: high
created: 2025-08-05
level: beginner
duration: 30 minutos
prerequisites: []
aliases: [Canary Server, Canary Overview, Servidor Canary, Canary Introduction]
---

# 🎯 Visão Geral do Servidor Canary
## Introdução ao Sistema de Servidor MMORPG

> [!info] **Sobre Este Conceito**
> Este conceito apresenta o servidor Canary, um sistema robusto e modular para desenvolvimento de MMORPGs baseados em Tibia.

## 🎯 **Objetivo de Aprendizado**
- ✅ Entender o que é o servidor Canary
- ✅ Compreender sua arquitetura modular
- ✅ Identificar os principais sistemas
- ✅ Conectar com outros conceitos relacionados

## 📚 **Conceito Principal**

### **Definição**
O **Canary** é um servidor MMORPG open-source desenvolvido em C++ que funciona como um fork do projeto OTServBR-Global. É um servidor robusto e modular que oferece uma arquitetura completa para jogos MMORPG baseados em Tibia.

### **Importância**
O Canary é fundamental no desenvolvimento de MMORPGs porque:
- **Fornece base sólida**: Arquitetura testada e robusta
- **Permite customização**: Sistema modular e extensível
- **Suporta Lua scripting**: Facilita desenvolvimento de mecânicas
- **Integra com OTClient**: Comunicação cliente-servidor completa

## 🏗️ **Arquitetura do Sistema**

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

## 🔧 **Exemplo Prático**

### **Estrutura de Diretórios**
```
canary/
├── src/                    # Código-fonte principal
│   ├── game/              # Sistemas de jogo
│   ├── creatures/         # Sistema de criaturas
│   ├── lua/               # Sistema de scripting
│   ├── database/          # Sistema de banco de dados
│   ├── io/                # Sistema de I/O
│   ├── map/               # Sistema de mapas
│   └── items/             # Sistema de itens
├── data/                  # Dados do servidor
└── config.lua.dist        # Configuração padrão
```

### **Configuração Básica**
```lua
-- config.lua - Configuração principal
useAnyDatapackFolder = false
dataPackDirectory = "data-otservbr-global"
coreDirectory = "data"
```

## 🔗 **Links para Aprofundamento**
- **Análise Completa**: [[habdel/CANARY-001|Análise Detalhada do Canary]]
- **Implementação**: [[wiki/examples/canary_setup|Configuração do Canary]]
- **Exercício**: [[wiki/exercises/setup_canary_server|Configurar Servidor Canary]]
- **Projeto**: [[wiki/projects/basic_canary_server|Servidor Básico Canary]]

## ✅ **Checklist de Conclusão**
- [ ] Entendi o que é o servidor Canary
- [ ] Compreendi sua arquitetura modular
- [ ] Identifiquei os principais sistemas
- [ ] Acessei links de aprofundamento
- [ ] Completei exercício relacionado

## 🎯 **Próximos Passos**
- **Próximo Conceito**: [[wiki/concepts/canary_core_systems|Sistemas Core do Canary]]
- **Módulo Relacionado**: [[wiki/modules/02_canary/01_canary_introduction|Módulo Canary]]
- **Tópico**: [[wiki/topics/canary|Índice Canary]]

---

> [!tip] **Dica de Aprendizado**
> O Canary é a base do servidor. Entender sua arquitetura é fundamental para desenvolver MMORPGs robustos.

**Nível**: Beginner  
**Duração**: 30 minutos  
**Status**: Ativo 