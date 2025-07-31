# Regras do Sistema BMAD - Better Model-Assisted Development

## 🎯 **Objetivo**

Definir regras para integração e uso do sistema BMAD (Better Model-Assisted Development) com o ecossistema OTClient + Canary, mantendo `cursor.md` como orquestrador principal e preservando toda a funcionalidade existente.

---

## 📋 **Princípios Fundamentais**

### 🔄 **Integração Hierárquica**

1. **`cursor.md` permanece** como orquestrador principal
2. **Sistema BMAD** funciona como extensão especializada
3. **Contexto inteligente** detectado automaticamente
4. **Compatibilidade total** com regras existentes
5. **Evolução contínua** do sistema

### 🎮 **Especialização Contextual**

- **Agentes especializados** para diferentes aspectos do desenvolvimento
- **Workflows estruturados** para processos padronizados
- **Templates adaptados** para documentação consistente
- **Orquestração inteligente** entre especialistas

---

## 🎭 **Regras de Agentes**

### 📋 **Ativação de Agentes**

#### **Comando de Ativação**
```bash
@agent_name "comando específico"
@game_designer "Criar sistema de combate"
@engine_developer "Otimizar performance"
```

#### **Regras de Ativação**
- **SEMPRE use @** para ativar agentes especializados
- **SEMPRE forneça contexto** claro no comando
- **SEMPRE mantenha contexto** entre transições
- **SEMPRE documente decisões** importantes

### 🎯 **Agentes Disponíveis**

#### **🎯 Game Designer (Luna)**
- **Uso**: Design de features, balanceamento, experiência do jogador
- **Expertise**: Mecânicas de jogo, sistemas de progressão, psicologia do jogador
- **Comandos**: `@game_designer "comando específico"`

#### **⚙️ Engine Developer (Zara)**
- **Uso**: Desenvolvimento C++, otimização, arquitetura
- **Expertise**: Performance, memória, rede, sistemas
- **Comandos**: `@engine_developer "comando específico"`

#### **📝 Content Creator (Maya)**
- **Uso**: Lua scripting, conteúdo, narrativa
- **Expertise**: Quests, NPCs, itens, storytelling
- **Comandos**: `@content_creator "comando específico"`

#### **🗺️ Level Designer (River)**
- **Uso**: Design de mapas, fluxo de jogador, storytelling ambiental
- **Expertise**: Áreas, dungeons, cidades, gameplay espacial
- **Comandos**: `@level_designer "comando específico"`

#### **🧪 QA Tester (Alex)**
- **Uso**: Testes, validação, qualidade
- **Expertise**: Testes de features, balanceamento, performance
- **Comandos**: `@qa_tester "comando específico"`

#### **🔧 DevOps Engineer (Jordan)**
- **Uso**: Infraestrutura, deploy, operações
- **Expertise**: Servidores, monitoramento, automação
- **Comandos**: `@devops_engineer "comando específico"`

#### **🎮 Game Team Orchestrator**
- **Uso**: Coordenação, planejamento, handoffs
- **Expertise**: Gestão de projetos, orquestração, qualidade
- **Comandos**: `@game_team_orchestrator "comando específico"`

### 🔄 **Transições entre Agentes**

#### **Protocolos de Handoff**
1. **Clear Context Transfer**: Decisões e restrições comunicadas
2. **Deliverable Specification**: Outputs e padrões definidos
3. **Timeline Coordination**: Dependências identificadas
4. **Review Checkpoints**: Gates de qualidade estabelecidos

#### **Regras de Transição**
- **SEMPRE documente contexto** antes de handoff
- **SEMPRE especifique entregáveis** esperados
- **SEMPRE identifique dependências** e bloqueios
- **SEMPRE estabeleça checkpoints** de qualidade

---

## 🔄 **Regras de Workflows**

### 📋 **Workflows Disponíveis**

#### **🚀 Feature Development**
- **Descrição**: Processo completo de desenvolvimento de features
- **Fases**: Concept & Design → Implementation → Integration & Testing → Deployment
- **Duração**: 2-4 semanas
- **Ativação**: `workflow feature-development "nome da feature"`

#### **📝 Content Pipeline**
- **Descrição**: Criação e integração de conteúdo
- **Fases**: Planning → Development → Integration → Deployment
- **Duração**: 1-2 semanas
- **Ativação**: `workflow content-pipeline "tipo de conteúdo"`

#### **🐛 Bug Fix Workflow**
- **Descrição**: Identificação e correção de bugs
- **Fases**: Identification → Analysis → Fix → Validation
- **Duração**: 1-3 dias
- **Ativação**: `workflow bug-fix "descrição do bug"`

#### **⚡ Performance Optimization**
- **Descrição**: Análise e otimização de performance
- **Fases**: Analysis → Identification → Optimization → Validation
- **Duração**: 3-7 dias
- **Ativação**: `workflow performance-optimization "área de otimização"`

### 🎯 **Regras de Workflows**

#### **Ativação de Workflows**
- **SEMPRE use `workflow`** para iniciar processos estruturados
- **SEMPRE forneça contexto** claro no comando
- **SEMPRE siga fases** estabelecidas
- **SEMPRE documente progresso** em cada fase

#### **Execução de Workflows**
- **SEMPRE use agentes apropriados** para cada fase
- **SEMPRE mantenha rastreabilidade** de decisões
- **SEMPRE valide qualidade** em cada checkpoint
- **SEMPRE documente entregáveis** de cada fase

---

## 📄 **Regras de Templates**

### 🎨 **Templates Disponíveis**

#### **Game Design Document (GDD)**
- **Uso**: Documentação de design de features
- **Formato**: Markdown com formatação Obsidian
- **Integração**: Compatível com mapas JSON
- **Validação**: Checklist de qualidade integrado

#### **Technical Specification**
- **Uso**: Especificação técnica de sistemas
- **Formato**: Markdown com diagramas
- **Integração**: Compatível com contexto detectado
- **Validação**: Review técnico obrigatório

#### **Content Creation Template**
- **Uso**: Criação de conteúdo e scripts
- **Formato**: Lua + Markdown
- **Integração**: Compatível com workflows
- **Validação**: Testes de integração

### 📋 **Regras de Templates**

#### **Uso de Templates**
- **SEMPRE use templates** apropriados para cada tipo de documento
- **SEMPRE siga formatação** Obsidian estabelecida
- **SEMPRE integre com** mapas JSON existentes
- **SEMPRE valide qualidade** antes de finalizar

#### **Criação de Templates**
- **SEMPRE baseie em** workflows estabelecidos
- **SEMPRE mantenha consistência** com padrões existentes
- **SEMPRE integre com** sistema de contexto
- **SEMPRE documente uso** e exemplos

---

## 🔗 **Regras de Integração**

### 📱 **Integração com Contexto OTClient**

#### **Adaptação de Agentes**
- **Game Designer**: Foco em features de cliente
- **Engine Developer**: Otimização de rendering e UI
- **Content Creator**: Scripts de módulos e UI
- **Level Designer**: Design de interfaces
- **QA Tester**: Testes de interface e usabilidade
- **DevOps Engineer**: Deploy de cliente

#### **Workflows Adaptados**
- **Feature Development**: Features de cliente
- **Content Pipeline**: Módulos e UI
- **Bug Fix Workflow**: Bugs de cliente
- **Performance Optimization**: Performance de cliente

### 🖥️ **Integração com Contexto Canary**

#### **Adaptação de Agentes**
- **Game Designer**: Foco em mecânicas de servidor
- **Engine Developer**: Otimização de servidor
- **Content Creator**: Scripts de servidor
- **Level Designer**: Design de mundo
- **QA Tester**: Testes de servidor
- **DevOps Engineer**: Infraestrutura de servidor

#### **Workflows Adaptados**
- **Feature Development**: Features de servidor
- **Content Pipeline**: Conteúdo de servidor
- **Bug Fix Workflow**: Bugs de servidor
- **Performance Optimization**: Performance de servidor

### 🌐 **Integração com Contexto Unificado**

#### **Coordenação Completa**
- **Game Team Orchestrator**: Coordenação entre cliente e servidor
- **Agentes Especializados**: Foco em integração
- **Workflows Unificados**: Processos completos
- **Templates Integrados**: Documentação unificada

---

## 🎯 **Regras de Comandos**

### 📋 **Comandos Principais**

#### **Comandos de Sistema**
```bash
*help                    # Mostrar comandos disponíveis
*agents                  # Listar agentes disponíveis
*workflows               # Mostrar workflows disponíveis
*status                  # Status atual do projeto
*handoff                 # Coordenar handoff entre fases
```

#### **Comandos de Agentes**
```bash
@agent_name "comando específico"
@game_designer "Criar sistema de combate"
@engine_developer "Otimizar performance"
```

#### **Comandos de Workflows**
```bash
workflow feature-development "nome da feature"
workflow content-pipeline "tipo de conteúdo"
workflow bug-fix "descrição do bug"
workflow performance-optimization "área de otimização"
```

### 🎮 **Regras de Comandos**

#### **Uso de Comandos**
- **SEMPRE use @** para ativar agentes especializados
- **SEMPRE use workflow** para processos estruturados
- **SEMPRE forneça contexto** claro nos comandos
- **SEMPRE mantenha consistência** de uso

#### **Validação de Comandos**
- **SEMPRE valide sintaxe** dos comandos
- **SEMPRE confirme contexto** antes de executar
- **SEMPRE documente resultados** de comandos
- **SEMPRE mantenha rastreabilidade** de execução

---

## 📊 **Regras de Qualidade**

### 🎯 **Padrões de Qualidade**

#### **Code Quality**
- **SEMPRE siga padrões** de código estabelecidos
- **SEMPRE use ferramentas** de qualidade (cppcheck, luacheck)
- **SEMPRE faça reviews** de código
- **SEMPRE teste funcionalidade** antes de deploy

#### **Content Quality**
- **SEMPRE teste scripts** Lua antes de integração
- **SEMPRE valide balanceamento** de features
- **SEMPRE documente conteúdo** criado
- **SEMPRE faça reviews** de conteúdo

#### **Documentation Quality**
- **SEMPRE use templates** apropriados
- **SEMPRE siga formatação** Obsidian
- **SEMPRE integre com** mapas JSON
- **SEMPRE valide links** e referências

### 🧪 **Processos de Validação**

#### **Checklists de Qualidade**
- **SEMPRE use checklists** apropriados para cada tipo de trabalho
- **SEMPRE valide entregáveis** antes de handoff
- **SEMPRE faça reviews** cross-funcionais
- **SEMPRE documente validações** realizadas

#### **Gates de Qualidade**
- **SEMPRE estabeleça gates** de qualidade em cada fase
- **SEMPRE valide critérios** antes de prosseguir
- **SEMPRE documente decisões** de qualidade
- **SEMPRE mantenha rastreabilidade** de validações

---

## 🔄 **Regras de Atualização**

### 📋 **Atualização Automática**

#### **Mapas JSON BMAD**
- **SEMPRE atualize** mapas JSON quando criar novos agentes
- **SEMPRE mantenha** integração com mapas existentes
- **SEMPRE valide** consistência de dados
- **SEMPRE documente** mudanças realizadas

#### **Templates e Workflows**
- **SEMPRE atualize** templates quando evoluir workflows
- **SEMPRE mantenha** compatibilidade com sistema existente
- **SEMPRE documente** mudanças em templates
- **SEMPRE valide** uso de templates atualizados

### 🎯 **Evolução do Sistema**

#### **Novos Agentes**
- **SEMPRE documente** novo agente completamente
- **SEMPRE integre** com sistema existente
- **SEMPRE atualize** mapas JSON
- **SEMPRE teste** funcionalidade do novo agente

#### **Novos Workflows**
- **SEMPRE documente** workflow completamente
- **SEMPRE integre** com agentes existentes
- **SEMPRE crie templates** apropriados
- **SEMPRE teste** execução do workflow

---

## ⚠️ **Regras de Exceção**

### 🚫 **O que NÃO Fazer**
- **NÃO ignore contexto** detectado automaticamente
- **NÃO use agentes** para tarefas fora de sua expertise
- **NÃO pule fases** de workflows estabelecidos
- **NÃO ignore validações** de qualidade

### ✅ **O que SEMPRE Fazer**
- **SEMPRE detecte contexto** antes de usar agentes
- **SEMPRE use expertise** apropriada para cada tarefa
- **SEMPRE siga workflows** estabelecidos
- **SEMPRE valide qualidade** em cada fase

---

## 🎉 **Conclusão**

Estas regras garantem que o sistema BMAD funcione perfeitamente integrado ao ecossistema OTClient + Canary, mantendo toda a funcionalidade existente e adicionando capacidades especializadas para desenvolvimento de MMORPG.

### 🚀 **Benefícios Esperados**
- **Especialização** sem perda de contexto
- **Eficiência** sem comprometer qualidade
- **Escalabilidade** sem complexidade
- **Flexibilidade** sem instabilidade

**O sistema BMAD agora está totalmente integrado e pronto para uso!** 🎮 