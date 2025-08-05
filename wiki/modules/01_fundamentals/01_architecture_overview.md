---
tags: [fundamentals, architecture, mmorpg, canary, otclient, beginner, education]
type: module
status: active
priority: high
created: 2025-08-05
level: beginner
duration: 1 semana
prerequisites: []
aliases: [Visão Geral da Arquitetura, Arquitetura MMORPG, Overview Arquitetura]
---

# 🏗️ Visão Geral da Arquitetura MMORPG
## Canary + OTClient - Fundamentos Arquiteturais

> [!info] **Sobre Este Módulo**
> Este módulo apresenta os conceitos fundamentais da arquitetura de MMORPGs, explicando como Canary (servidor) e OTClient (cliente) trabalham juntos para criar jogos online massivos.

## 🎯 **Objetivos de Aprendizado**

- ✅ Entender a arquitetura cliente-servidor em MMORPGs
- ✅ Compreender o papel do Canary como servidor
- ✅ Entender o papel do OTClient como cliente
- ✅ Aprender sobre comunicação em rede
- ✅ Conhecer os componentes principais de cada sistema

## 🏛️ **Arquitetura Cliente-Servidor**

### **Visão Geral do Sistema**
```
┌─────────────────┐    TCP/IP    ┌─────────────────┐
│                 │◄────────────►│                 │
│   OTClient      │              │    Canary       │
│   (Cliente)     │              │   (Servidor)    │
│                 │              │                 │
└─────────────────┘              └─────────────────┘
```

### **Responsabilidades do Cliente (OTClient)**
- **Renderização**: Exibir gráficos e interface
- **Entrada do Usuário**: Capturar cliques, teclas, etc.
- **Interface**: Menus, inventário, chat
- **Cache Local**: Armazenar dados temporários
- **Validação Local**: Verificar dados antes de enviar

### **Responsabilidades do Servidor (Canary)**
- **Lógica do Jogo**: Regras, mecânicas, validações
- **Persistência**: Banco de dados, salvamento
- **Sincronização**: Coordenar todos os jogadores
- **Segurança**: Prevenir trapaças e exploits
- **Escalabilidade**: Suportar muitos jogadores

## 🖥️ **Arquitetura do Servidor Canary**

### **Componentes Principais**
```
Canary Server
├── Core Systems
│   ├── Game Engine
│   ├── Network Manager
│   ├── Database Manager
│   └── Script Engine (Lua)
├── Game Systems
│   ├── Combat System
│   ├── Inventory System
│   ├── NPC System
│   └── Quest System
└── Support Systems
    ├── Logging System
    ├── Configuration
    └── Monitoring
```

### **Sistema de Logs (Baseado em [[habdel/CANARY-020]])**
O Canary possui um sistema de logs robusto para monitoramento e debug:

```cpp
// Exemplo de uso do sistema de logs
Logger logger;
logger.info("Player {} connected", playerName);
logger.warn("High memory usage detected");
logger.error("Database connection failed");
logger.critical("Server crash imminent");
```

### **Arquitetura Core**
- **Framework Core**: Base do sistema
- **Application Manager**: Gerencia o ciclo de vida da aplicação
- **Event System**: Sistema de eventos assíncronos
- **Resource Manager**: Gerencia recursos (memória, arquivos)
- **Platform Abstraction**: Abstração de plataforma

## 🎮 **Arquitetura do Cliente OTClient**

### **Componentes Principais**
```
OTClient
├── Core Systems
│   ├── Application Manager
│   ├── Event System
│   ├── Resource Manager
│   └── Platform Abstraction
├── Graphics Systems
│   ├── Graphics Engine
│   ├── Animation System
│   ├── Particle System
│   └── Sound System
├── Game Systems
│   ├── Map System
│   ├── Combat System
│   ├── Inventory System
│   └── Chat System
└── UI Systems
    ├── UI Framework
    ├── Module System
    └── Lua Integration
```

### **Sistema de Módulos (Baseado em [[habdel/OTCLIENT-021]])**
O OTClient usa um sistema modular para organizar funcionalidades:

```cpp
// Exemplo de módulo OTClient
class Module {
public:
    virtual void init() = 0;
    virtual void terminate() = 0;
    virtual void update() = 0;
};
```

## 🔄 **Comunicação Cliente-Servidor**

### **Protocolo de Comunicação**
```
Cliente → Servidor: Ações do jogador
Servidor → Cliente: Atualizações do mundo
Servidor → Cliente: Respostas às ações
Cliente → Servidor: Heartbeat/Keep-alive
```

### **Tipos de Mensagens**
1. **Ações do Jogador**: Movimento, ataque, uso de item
2. **Atualizações do Mundo**: Posições, estados, eventos
3. **Sistema**: Login, logout, configurações
4. **Chat**: Mensagens entre jogadores

### **Otimizações de Rede**
- **Compressão**: Reduzir tamanho das mensagens
- **Delta Updates**: Enviar apenas mudanças
- **Prediction**: Prever ações no cliente
- **Interpolation**: Suavizar movimentos

## 📊 **Fluxo de Dados Típico**

### **Exemplo: Jogador Move-se**
```
1. Usuário pressiona tecla → OTClient
2. OTClient valida movimento local
3. OTClient envia para Canary
4. Canary valida no servidor
5. Canary atualiza posição no banco
6. Canary notifica outros jogadores
7. OTClient recebe confirmação
8. OTClient atualiza interface
```

## 🛠️ **Integração Lua**

### **Lua no Canary (Servidor)**
```lua
-- Exemplo de script de NPC no Canary
function onCreatureSay(cid, type, msg)
    if msg == "hello" then
        doCreatureSay(cid, "Hello, traveler!", TALKTYPE_SAY)
    end
end
```

### **Lua no OTClient (Cliente)**
```lua
-- Exemplo de módulo UI no OTClient
function init()
    local window = g_ui.createWidget('MainWindow')
    window:setText('Hello World')
end
```

## 🎯 **Exercícios Práticos**

### **Exercício 1: Análise de Arquitetura**
1. Abra o código do Canary em `canary/src/`
2. Identifique os componentes principais
3. Mapeie as dependências entre sistemas
4. Documente sua descoberta

### **Exercício 2: Análise do OTClient**
1. Explore o código do OTClient em `otclient/src/`
2. Identifique o sistema de módulos
3. Analise a integração Lua
4. Compare com a documentação em [[habdel/OTCLIENT-021]]

### **Exercício 3: Comunicação de Rede**
1. Use ferramentas como Wireshark
2. Capture tráfego entre cliente e servidor
3. Analise os tipos de mensagens
4. Documente o protocolo observado

## 📚 **Recursos Adicionais**

### **Documentação Técnica**
- [[habdel/CANARY-020|Sistema de Logs Canary]]
- [[habdel/OTCLIENT-021|Documentação Consolidada OTClient]]
- [[habdel/METHODOLOGY-001|Metodologia de Pesquisa]]

### **Código-Fonte**
- `canary/src/` - Código do servidor
- `otclient/src/` - Código do cliente
- `canary/data/` - Dados do servidor
- `otclient/modules/` - Módulos do cliente

### **Próximos Passos**
- [[wiki/modules/01_fundamentals/02_development_environment|Ambiente de Desenvolvimento]]
- [[wiki/modules/01_fundamentals/03_basic_concepts|Conceitos Básicos]]
- [[wiki/modules/01_fundamentals/04_project_structure|Estrutura do Projeto]]

## ✅ **Checklist de Conclusão**

- [ ] Entendi a arquitetura cliente-servidor
- [ ] Compreendi o papel do Canary
- [ ] Compreendi o papel do OTClient
- [ ] Analisei o código-fonte básico
- [ ] Completei os exercícios práticos
- [ ] Li a documentação recomendada

---

> [!tip] **Dica de Estudo**
> Use o Obsidian para criar links entre conceitos relacionados. Isso ajudará a construir uma rede de conhecimento interconectada.

**Próximo Módulo**: [[wiki/modules/01_fundamentals/02_development_environment|Ambiente de Desenvolvimento]]  
**Nível**: Beginner  
**Duração**: 1 semana 