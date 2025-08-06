---
tags: [concept, canary, scripting_system, modules, lua, recvbyte, delays]
type: concept
status: active
priority: high
created: 2025-08-05
level: intermediate
duration: 40 minutos
prerequisites: [canary_server_overview, canary_core_architecture]
aliases: [Canary Scripting System, Module System, Lua Integration, Recvbyte System]
---

# 🔧 Sistema de Scripting do Canary

## Explicação Clara e Objetiva

O sistema de scripting do Canary é um mecanismo poderoso que permite criar extensões customizadas do servidor através de módulos Lua. Ele intercepta mensagens de rede (recvbyte) e permite que desenvolvedores implementem funcionalidades específicas de forma dinâmica e flexível.

## 🎯 Componentes Principais

### **1. Module Class (Classe de Módulo)**
- **Função**: Representa um módulo Lua individual
- **Responsabilidades**: Configuração, execução de scripts, gerenciamento de recvbyte
- **Localização**: `src/lua/modules/modules.hpp`

### **2. Modules Manager (Gerenciador de Módulos)**
- **Função**: Gerencia todos os módulos do sistema
- **Responsabilidades**: Execução de eventos, registro de módulos, interface Lua
- **Localização**: `src/lua/modules/modules.hpp`

### **3. Module Types (Tipos de Módulo)**
- **RECVBYTE**: Módulos que interceptam mensagens de rede
- **NONE**: Tipo padrão para módulos não especificados
- **Localização**: `src/lua/lua_definitions.hpp`

### **4. Player Module Management (Gerenciamento de Módulos do Jogador)**
- **Função**: Controla delays e execução de módulos por jogador
- **Responsabilidades**: Controle de delays, verificação de execução
- **Localização**: `src/creatures/players/player.hpp`

## 🔄 Sistema de Recvbyte

O sistema de recvbyte permite interceptar mensagens de rede específicas:

- **Mapeamento por Byte**: Cada módulo é associado a um byte específico
- **Execução Dinâmica**: Módulos são executados quando o byte é recebido
- **Busca Inteligente**: Sistema pode buscar módulos de forma forçada ou normal
- **Lista de Módulos**: Gerenciamento eficiente de múltiplos módulos

## ⏱️ Sistema de Delays

O sistema de delays controla a frequência de execução dos módulos:

- **Configuração por Módulo**: Cada módulo pode ter seu próprio delay
- **Verificação de Execução**: Sistema verifica se o módulo pode executar
- **Mapeamento Temporal**: Associação de delays com timestamps
- **Controle por Jogador**: Delays são controlados individualmente por jogador

## 🔧 Funcionalidades Principais

### **Extensibilidade**
- Criação de módulos customizados em Lua
- Interceptação de mensagens de rede
- Implementação de funcionalidades específicas

### **Flexibilidade**
- Configuração dinâmica via XML
- Recarregamento de módulos em tempo real
- Controle granular de execução

### **Performance**
- Sistema de delays para controle de frequência
- Execução eficiente de módulos
- Gerenciamento otimizado de recursos

## 🔗 Links Relacionados

- **Análise Técnica Completa**: [[habdel/CANARY-006|CANARY-006: Sistema de Módulos]]
- **Exemplo Prático**: [[examples/canary_scripting_setup|Configuração do Sistema de Scripting]]
- **Exercício Prático**: [[exercises/build_scripting_system|Construindo o Sistema de Scripting]]
- **Módulo Educacional**: [[modules/02_canary/03_scripting_system|Módulo: Sistema de Scripting]]

## 📚 Recursos Adicionais

- **Tópico Canary**: [[topics/canary|Índice Canary]]
- **Arquitetura Core**: [[concepts/canary_core_architecture|Arquitetura Core do Canary]]
- **Templates**: [[templates/concept_template|Template de Conceito]] 