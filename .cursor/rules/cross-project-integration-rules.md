# Regras para Integração entre Projetos (OTClient + Canary)

## 🚀 **PREPARAÇÃO PARA INTEGRAÇÃO FUTURA**

### 🎯 **CONTEXTO DE INTEGRAÇÃO**

**Este repositório (`otclient_doc`) está sendo preparado para integração total com o Canary.**

**O código-fonte do Canary será copiado e integrado neste repositório.**

### 📁 **Estrutura Futura dos Repositórios**

```
📁 otclient_doc/ (REPOSITÓRIO ATUAL - SERÁ INTEGRADO)
├── 📚 wiki/ (documentação OTClient)
├── 🔧 src/ (código OTClient)
├── 📦 modules/ (módulos Lua OTClient)
└── 🔄 PREPARADO PARA INTEGRAÇÃO CANARY

📁 canary_repository/ (REPOSITÓRIO FUTURO - SERÁ COPIADO)
├── 🔧 src/ (código Canary - será copiado)
├── 📚 wiki/ (documentação Canary - será copiado)
└── 📦 modules/ (módulos Canary - serão copiados)

📁 REPOSITÓRIO FINAL INTEGRADO
├── 📚 wiki/ (OTClient + Canary integradas)
├── 🔧 src/ (OTClient + Canary)
├── 📦 modules/ (OTClient + Canary)
└── 🔗 integration/ (integração completa)
```

### 🎯 **O que Estamos Preparando (INTEGRAÇÃO FUTURA)**

✅ **Criar estrutura de integração** para receber código Canary
✅ **Documentar protocolos compartilhados** (OpenCode, ExtendedOpen)
✅ **Preparar templates** para documentação integrada
✅ **Estabelecer padrões** de comunicação cliente-servidor
✅ **Criar referências** para documentação integrada
✅ **Preparar agentes** para integração automática

### 🔮 **O que Será Possível Após Integração**

🔮 **Analisar código-fonte completo** (OTClient + Canary)
🔮 **Criar documentação técnica integrada** (cliente + servidor)
🔮 **Comparar implementações** (ambos os lados disponíveis)
🔮 **Validar integração completa** (ecossistema completo)
🔮 **Executar testes de integração** (sistema completo)

### 🔄 **Estratégia de Integração**

1. **Foco em Integração**: Estruturar para receber código Canary
2. **Documentar Interfaces**: Protocolos e pontos de comunicação
3. **Criar Templates**: Para documentação integrada
4. **Estabelecer Padrões**: Formato de documentação unificada
5. **Preparar Agentes**: Para integração automática
6. **Criar Workflows**: Para processo de integração

---

## 🎯 **Objetivo (ATUALIZADO)**

Preparar a wiki do OTClient para **integração total** com o Canary, criando **estrutura, templates e agentes** para um ecossistema de documentação unificado do jogo MMORPG completo.

**NOTA**: Esta preparação está sendo feita para receber o código-fonte do Canary que será copiado e integrado.

---

## 📋 **Princípios Fundamentais**

### 🔄 **Estratégia de Integração**

1. **Documentação Modular**: Cada projeto mantém sua wiki específica
2. **Pontos de Integração**: Áreas onde OTClient e Canary se comunicam
3. **Protocolo Unificado**: Documentação compartilhada de protocolos
4. **Referências Cruzadas**: Links entre wikis quando relevante
5. **Evolução Independente**: Cada projeto pode evoluir separadamente

### 🏗️ **Arquitetura de Integração**

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   OTClient Wiki │    │  Shared Protocol│    │   Canary Wiki   │
│                 │    │   Documentation │    │                 │
│ • UI System     │◄──►│ • OpenCode      │◄──►│ • Game Logic    │
│ • Client Logic  │    │ • ExtendedOpen  │    │ • Server Logic  │
│ • Rendering     │    │ • Protocol Spec │    │ • Database      │
│ • Modules       │    │ • Message Types │    │ • World Mgmt    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

---

## 🎮 **Áreas de Integração Identificadas**

### 🔐 **Protocolo de Comunicação**

#### **OpenCode (Protocolo Base)**
- **Descrição**: Protocolo base para comunicação cliente-servidor
- **Versões Suportadas**: 7.72 até 14.12
- **Implementação**: OTClient (cliente) ↔ Canary (servidor)
- **Documentação**: Compartilhada entre projetos

#### **ExtendedOpen (Extensões)**
- **Descrição**: Extensões customizadas do protocolo base
- **Funcionalidades**: Features avançadas não presentes no protocolo original
- **Implementação**: Módulos OTClient ↔ Scripts Canary
- **Documentação**: Específica de cada projeto + interface compartilhada

### 🌐 **Sistema de Rede**

#### **Conexão e Autenticação**
- **Login Protocol**: Handshake inicial cliente-servidor
- **Session Management**: Gerenciamento de sessões
- **Reconnection**: Reconexão automática
- **Security**: Criptografia XTEA, RSA

#### **Comunicação em Tempo Real**
- **Game Protocol**: Dados do jogo em tempo real
- **Chat System**: Sistema de comunicação
- **World Updates**: Atualizações do mundo
- **Player Actions**: Ações do jogador

### 🎯 **Pontos de Sincronização**

#### **Game State**
- **Player Position**: Posição do jogador
- **Inventory**: Inventário e itens
- **Skills**: Habilidades e progressão
- **Combat**: Sistema de combate

#### **World State**
- **Map Data**: Dados do mapa
- **Creatures**: Criaturas e NPCs
- **Items**: Itens no mundo
- **Effects**: Efeitos visuais

---

## 📝 **Regras de Documentação**

### 🏷️ **Tags de Integração**

#### **Tags Obrigatórias para Áreas de Integração**
```markdown
---
tags: [otclient, canary, protocol, integration, opencode, extendedopen]
cross_project: true
integration_areas: [protocol, network, game_state]
related_projects: [canary-wiki]
---
```

#### **Tags Específicas por Área**
- `protocol-opencode`: Documentação do protocolo base
- `protocol-extendedopen`: Extensões do protocolo
- `network-communication`: Comunicação de rede
- `game-state-sync`: Sincronização de estado do jogo
- `client-server-interface`: Interface cliente-servidor

### 🔗 **Referências Cruzadas**

#### **Formato Padrão para Links entre Projetos**
```markdown
> [!info] **Integração com Canary**
> Este sistema se integra com o servidor Canary. Para detalhes do lado servidor:
> - **Canary Wiki**: [Protocol Implementation](canary-wiki-url)
> - **Shared Spec**: [OpenCode Protocol](shared-spec-url)
> - **Testing**: [Integration Tests](test-url)
```

#### **Seção de Integração em Documentos**
```markdown
## 🔗 **Integração com Canary**

### **Lado Cliente (OTClient)**
- Implementação do protocolo
- Gerenciamento de conexão
- Processamento de mensagens

### **Lado Servidor (Canary)**
- [Ver documentação no Canary Wiki](canary-wiki-url)
- Implementação do servidor
- Gerenciamento de sessões

### **Protocolo Compartilhado**
- [Especificação OpenCode](opencode-spec-url)
- [Extensões ExtendedOpen](extendedopen-spec-url)
- [Testes de Integração](integration-tests-url)
```

### 📊 **Estrutura de Documentação Compartilhada**

#### **Documentos de Interface**
```markdown
# Interface Cliente-Servidor: [Nome do Sistema]

## 📋 **Visão Geral**
Descrição do sistema e como OTClient e Canary interagem.

## 🔧 **Implementação OTClient**
- Código Lua/C++ do cliente
- APIs e interfaces
- Exemplos de uso

## 🖥️ **Implementação Canary**
- Referência para documentação do Canary
- Pontos de integração
- APIs do servidor

## 📡 **Protocolo de Comunicação**
- Mensagens trocadas
- Formato dos dados
- Sequência de operações

## 🧪 **Testes de Integração**
- Como testar a integração
- Ferramentas de debug
- Cenários de teste
```

---

## 🛠️ **Implementação Prática**

### 📁 **Estrutura de Arquivos**

#### **Documentos de Integração**
```
wiki/docs/integration/
├── protocol/
│   ├── OpenCode_Protocol.md
│   ├── ExtendedOpen_Protocol.md
│   └── Message_Types.md
├── network/
│   ├── Client_Server_Communication.md
│   ├── Authentication_System.md
│   └── Session_Management.md
├── game_state/
│   ├── Player_Synchronization.md
│   ├── World_State_Sync.md
│   └── Combat_System_Integration.md
└── testing/
    ├── Integration_Testing.md
    └── Debug_Protocol.md
```

#### **Mapas JSON de Integração**
```json
{
  "integration_areas": {
    "protocol": {
      "opencode": ["OpenCode_Protocol.md", "Message_Types.md"],
      "extendedopen": ["ExtendedOpen_Protocol.md"]
    },
    "network": {
      "communication": ["Client_Server_Communication.md"],
      "auth": ["Authentication_System.md"]
    }
  },
  "cross_project_links": {
    "canary_wiki": "https://canary-wiki-url",
    "shared_specs": "https://shared-specs-url"
  }
}
```

### 🔄 **Processo de Atualização**

#### **Quando Criar Documentos de Integração**
1. **Novo Sistema de Protocolo**: Sempre documentar interface
2. **Modificação de Protocolo**: Atualizar documentação compartilhada
3. **Nova Funcionalidade**: Verificar se afeta comunicação cliente-servidor
4. **Bug Fix**: Documentar mudanças que afetam integração

#### **Validação de Integração**
```markdown
## ✅ **Checklist de Integração**

- [ ] Documentação criada em `wiki/docs/integration/`
- [ ] Tags de integração adicionadas
- [ ] Referências cruzadas implementadas
- [ ] Exemplos de código incluídos
- [ ] Testes de integração documentados
- [ ] Mapas JSON atualizados
- [ ] Links para Canary Wiki verificados
```

---

## 🎯 **Benefícios Esperados**

### 📈 **Para Desenvolvedores**
- **Visão Completa**: Entendimento do ecossistema completo
- **Debugging Facilitado**: Documentação de ambos os lados
- **Desenvolvimento Coordenado**: Sincronização entre projetos
- **Testes Integrados**: Validação de funcionalidades completas

### 🏗️ **Para o Projeto**
- **Documentação Unificada**: Coerência entre cliente e servidor
- **Manutenção Simplificada**: Mudanças documentadas em ambos os lados
- **Onboarding Melhorado**: Novos desenvolvedores entendem o todo
- **Qualidade Garantida**: Validação de integração documentada

### 🔄 **Para Futuras Integrações**
- **Padrão Estabelecido**: Processo definido para novas integrações
- **Escalabilidade**: Fácil adição de novos sistemas
- **Consistência**: Formato padronizado para documentação
- **Automação**: Possibilidade de geração automática de documentação

---

## ⚠️ **Regras de Exceção**

### 🚫 **O que NÃO Fazer**
- **Duplicar Documentação**: Não copiar documentação do Canary
- **Criar Dependências**: OTClient deve funcionar independentemente
- **Misturar Contextos**: Manter separação clara entre cliente e servidor
- **Sobrescrever Especificações**: Respeitar especificações oficiais

### ✅ **O que SEMPRE Fazer**
- **Referenciar Canary**: Sempre linkar para documentação do Canary
- **Documentar Interface**: Sempre documentar pontos de integração
- **Manter Atualizado**: Atualizar documentação quando protocolo mudar
- **Validar Links**: Verificar se links para Canary Wiki funcionam

---

## 🔄 **Sistema de Atualização**

### 📋 **Tarefa Obrigatória da IA**

**SEMPRE que criar ou modificar documentação relacionada a:**
- Protocolo de comunicação
- Sistema de rede
- Sincronização de estado
- Interface cliente-servidor

**DEVE:**
1. **Adicionar tags de integração** apropriadas
2. **Criar seção de integração** com referências ao Canary
3. **Atualizar mapas JSON** de integração
4. **Validar links cruzados** entre projetos
5. **Documentar pontos de interface** claramente

### 📊 **Métricas de Qualidade**

#### **Quantitativas**
- **Documentos de Integração**: Número de documentos com tags de integração
- **Links Cruzados**: Número de referências válidas para Canary
- **Cobertura de Protocolo**: % de protocolos documentados
- **Testes de Integração**: Número de cenários de teste documentados

#### **Qualitativas**
- **Clareza de Interface**: Facilidade de entender pontos de integração
- **Consistência**: Padrão seguido em todos os documentos
- **Atualização**: Documentação sempre sincronizada com código
- **Usabilidade**: Facilidade de encontrar informações de integração

---

## 🚀 **PREPARAÇÃO PARA INTEGRAÇÃO TOTAL**

### 📋 **Tasks de Preparação**

#### **Task 1.1: Estrutura de Recepção**
- [ ] Criar pasta `wiki/canary/` para documentação Canary
- [ ] Criar pasta `wiki/integration/` para documentação integrada
- [ ] Preparar templates para documentação Canary
- [ ] Criar mapas de integração

#### **Task 1.2: Agentes de Integração**
- [ ] Criar `integration_agent.py` para integração automática
- [ ] Atualizar `intelligent_organization_agent.py` para suporte Canary
- [ ] Criar `integration_workflow.py` para processo automatizado
- [ ] Preparar validação de integração

#### **Task 1.3: Documentação de Preparação**
- [ ] Criar guias de integração
- [ ] Documentar processo de cópia de pastas
- [ ] Preparar templates de documentação integrada
- [ ] Criar checklists de validação

### 🎯 **Cronograma de Integração**

#### **Fase 1: Preparação (Esta Semana)**
- [ ] Estrutura de pastas criada
- [ ] Agentes de integração funcionais
- [ ] Templates de documentação prontos
- [ ] Sistema de validação implementado

#### **Fase 2: Integração (Próxima Semana)**
- [ ] Cópia de pastas Canary realizada
- [ ] Documentação integrada criada
- [ ] Agentes treinados para novo contexto
- [ ] Sistema de validação executado

#### **Fase 3: Validação (Terceira Semana)**
- [ ] Testes de integração executados
- [ ] Documentação validada
- [ ] Agentes otimizados
- [ ] Sistema estabilizado

## 🎉 **Conclusão**

Esta estratégia de integração prepara a wiki do OTClient para **integração total** com o Canary, criando um ecossistema de documentação completo e coerente para o jogo MMORPG.

### 🚀 **Próximos Passos**
1. **Implementar estrutura de recepção** para código Canary
2. **Criar agentes de integração** automatizados
3. **Preparar templates** para documentação integrada
4. **Estabelecer workflows** de integração
5. **Executar processo** de cópia e integração

**A wiki agora está preparada para receber e integrar o código Canary!** 🎮 