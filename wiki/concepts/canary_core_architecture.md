---
tags: [concept, canary, core_architecture, server_components, initialization, service_management]
type: concept
status: active
priority: high
created: 2025-08-05
level: intermediate
duration: 45 minutos
prerequisites: [canary_server_overview]
aliases: [Canary Core Architecture, Server Core, Main Components, Service Management]
---

# 🏗️ Arquitetura Core do Canary

## Explicação Clara e Objetiva

A arquitetura core do Canary é o coração do servidor MMORPG, responsável por coordenar todos os subsistemas e garantir o funcionamento estável do jogo. Ela é baseada em C++ moderno com gerenciamento de serviços, configuração dinâmica e inicialização estruturada.

## 🎯 Componentes Principais

### **1. CanaryServer (Servidor Principal)**
- **Função**: Coordenador central de todos os subsistemas
- **Responsabilidades**: Inicialização, gerenciamento de ciclo de vida, tratamento de erros
- **Localização**: `src/canary_server.hpp`, `src/canary_server.cpp`

### **2. ServiceManager (Gerenciador de Serviços)**
- **Função**: Gerencia portas e serviços de rede
- **Responsabilidades**: Aceitação de conexões, roteamento de protocolos
- **Localização**: `src/server/server.hpp`

### **3. ConfigManager (Gerenciador de Configuração)**
- **Função**: Gerencia todas as configurações do servidor
- **Responsabilidades**: Carregamento, validação, recarregamento dinâmico
- **Localização**: `src/config/configmanager.hpp`

### **4. DatabaseManager (Gerenciador de Banco de Dados)**
- **Função**: Gerencia conexões e operações de banco de dados
- **Responsabilidades**: Migrações, otimizações, configuração
- **Localização**: `src/database/databasemanager.hpp`

## 🔄 Fluxo de Inicialização

O servidor segue uma sequência específica de inicialização:

1. **Carregar Configuração** → `loadConfigLua()`
2. **Validar Datapack** → `validateDatapack()`
3. **Inicializar Banco** → `initializeDatabase()`
4. **Carregar Módulos** → `loadModules()`
5. **Configurar Mundo** → `setWorldType()`
6. **Carregar Mapas** → `loadMaps()`
7. **Configurar Casas** → `setupHousesRent()`
8. **Iniciar Jogo** → `g_game().start()`

## 🔗 Links Relacionados

- **Análise Técnica Completa**: [[habdel/CANARY-002|CANARY-002: Análise da Arquitetura Core]]
- **Exemplo Prático**: [[examples/canary_core_setup|Configuração da Arquitetura Core]]
- **Exercício Prático**: [[exercises/build_core_architecture|Construindo a Arquitetura Core]]
- **Módulo Educacional**: [[modules/02_canary/02_core_architecture|Módulo: Arquitetura Core]]

## 📚 Recursos Adicionais

- **Tópico Canary**: [[topics/canary|Índice Canary]]
- **Arquitetura Geral**: [[concepts/architecture_overview|Visão Geral da Arquitetura]]
- **Templates**: [[templates/concept_template|Template de Conceito]] 