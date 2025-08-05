# 📋 Regras de Manutenção do README.md

> **Manutenção automática e atualização do README.md principal do repositório**

## 🎯 **Propósito**

Manter o `README.md` sempre atualizado como um **retrato fiel** do repositório, refletindo:

- ✅ **Estrutura atual** de arquivos e pastas
- ✅ **Funcionalidades ativas** e em desenvolvimento
- ✅ **Status real** de cada componente
- ✅ **Métricas atualizadas** do sistema
- ✅ **Navegação funcional** e contextos disponíveis

## 📋 **Regras Principais**

### 🎯 **Atualização Obrigatória**

#### **1. Estrutura de Arquivos**
- **Atualizar** tabelas de arquivos e pastas sempre que houver mudanças
- **Verificar** status de cada componente (✅ Ativo, 🚧 Em desenvolvimento, ❌ Inativo)
- **Manter** contadores precisos (30 regras, 23 mapas JSON, etc.)

#### **2. Funcionalidades**
- **Listar** apenas funcionalidades realmente implementadas
- **Marcar** funcionalidades em desenvolvimento com 🚧
- **Remover** funcionalidades descontinuadas
- **Adicionar** novas funcionalidades implementadas

#### **3. Status do Projeto**
- **Atualizar** progresso de cada componente (0-100%)
- **Refletir** status real baseado em testes e validação
- **Manter** métricas precisas e atualizadas

#### **4. Navegação**
- **Verificar** se todos os contextos (@otclient, @bmad, @wiki, @integration) funcionam
- **Testar** padrões de navegação descritos
- **Atualizar** comandos e exemplos conforme necessário

### 🔄 **Processo de Atualização**

#### **1. Verificação Automática**
```bash
# Antes de qualquer atualização do README.md
1. Verificar estrutura atual do repositório
2. Validar funcionalidades descritas
3. Testar navegação e contextos
4. Atualizar métricas e status
```

#### **2. Validação de Conteúdo**
- **Estrutura**: Verificar se todas as pastas e arquivos estão listados
- **Regras**: Confirmar se todas as 30 regras estão ativas
- **Mapas**: Validar se todos os 23 mapas JSON existem e funcionam
- **Contextos**: Testar se os 4 contextos automáticos funcionam

#### **3. Atualização de Métricas**
- **Contadores**: Atualizar números de arquivos, regras, mapas
- **Progresso**: Recalcular progresso de cada componente
- **Status**: Verificar status real de cada funcionalidade

### 📊 **Métricas a Manter Atualizadas**

#### **Sistema de Regras**
- **Total de regras**: 30 (verificar se todas existem)
- **Regras ativas**: Contar apenas as que funcionam
- **Regras em desenvolvimento**: Marcar com 🚧

#### **Mapas de Navegação**
- **Total de mapas JSON**: 15 (verificar se todos existem)
- **Mapas funcionais**: Testar se todos carregam corretamente
- **Mapas em cache**: Verificar cache inteligente

#### **Documentação**
- **Pastas da wiki**: Listar todas as pastas existentes
- **Documentos criados**: Contar documentos ativos
- **Cobertura**: Calcular % de cobertura da documentação

#### **Sistema BMAD**
- **Agentes ativos**: Contar agentes funcionais
- **Workflows**: Listar workflows implementados
- **Templates**: Contar templates disponíveis

### 🧪 **Testes de Validação**

#### **1. Teste de Navegação**
```bash
# Testar cada contexto
@otclient → Deve navegar para código OTClient
@bmad → Deve navegar para sistema BMAD
@wiki → Deve navegar para documentação
@integration → Deve navegar para integração
```

#### **2. Teste de Estrutura**
```bash
# Verificar se todos os arquivos/pastas existem
- .cursor/rules/ (26 arquivos)
- data/maps/ (15 arquivos JSON)
- docs/bmad/ (sistema de agentes)
- otclient/ (submódulo)
- canary/ (submódulo)
```

#### **3. Teste de Funcionalidades**
```bash
# Verificar se funcionalidades descritas funcionam
- Sistema de regras
- Navegação inteligente
- Mapas JSON
- Agentes BMAD
- Documentação
```

### 📝 **Formato e Padrões**

#### **1. Estrutura do README**
- **Manter** índice completo e funcional
- **Usar** emojis consistentes para categorização
- **Seguir** formatação markdown padrão
- **Incluir** exemplos práticos de uso

#### **2. Tabelas de Status**
- **✅ Ativo**: Funcionalidade implementada e funcionando
- **🚧 Em desenvolvimento**: Funcionalidade em implementação
- **❌ Inativo**: Funcionalidade descontinuada ou não implementada

#### **3. Métricas de Progresso**
- **0-100%**: Progresso real baseado em implementação
- **Atualizar** baseado em testes e validação
- **Manter** precisão nas estimativas

### 🔄 **Atualização Automática**

#### **1. Gatilhos de Atualização**
- **Nova regra** criada em `.cursor/rules/`
- **Novo mapa** criado em `data/maps/`
- **Nova funcionalidade** implementada
- **Mudança** na estrutura de pastas
- **Atualização** de status de componentes

#### **2. Script de Atualização**
```python
# Executar antes de commits importantes
python wiki/tools/update_readme.py
```

#### **3. Validação Pós-Atualização**
- **Verificar** se links funcionam
- **Testar** exemplos de código
- **Validar** métricas e contadores
- **Confirmar** navegação e contextos

### 📋 **Checklist de Manutenção**

#### **Antes de Atualizar README.md**
- [ ] **Verificar** estrutura atual do repositório
- [ ] **Testar** todas as funcionalidades descritas
- [ ] **Validar** navegação e contextos
- [ ] **Contar** arquivos, regras e mapas
- [ ] **Calcular** progresso real de componentes

#### **Durante Atualização**
- [ ] **Manter** formatação consistente
- [ ] **Atualizar** todas as tabelas de status
- [ ] **Verificar** links e referências
- [ ] **Testar** exemplos de código
- [ ] **Validar** métricas e contadores

#### **Após Atualização**
- [ ] **Executar** testes de validação
- [ ] **Verificar** navegação automática
- [ ] **Confirmar** contextos funcionais
- [ ] **Testar** comandos e exemplos
- [ ] **Validar** estrutura geral

### 🎯 **Integração com Outras Regras**

#### **1. Sistema de Regras**
- **Atualizar** contador de regras quando criar/remover
- **Verificar** se todas as regras estão listadas
- **Manter** status de cada regra

#### **2. Mapas de Navegação**
- **Atualizar** contador de mapas JSON
- **Verificar** se todos os mapas funcionam
- **Manter** descrições precisas

#### **3. Sistema BMAD**
- **Atualizar** status de agentes e workflows
- **Verificar** funcionalidade do sistema
- **Manter** métricas de performance

### 📊 **Relatórios de Status**

#### **1. Relatório Mensal**
- **Atualizar** progresso geral do projeto
- **Verificar** funcionalidades implementadas
- **Calcular** métricas de performance
- **Validar** navegação e contextos

#### **2. Relatório de Mudanças**
- **Documentar** mudanças na estrutura
- **Listar** novas funcionalidades
- **Atualizar** status de componentes
- **Verificar** compatibilidade

### 🚨 **Tratamento de Erros**

#### **1. Inconsistências Detectadas**
- **Corrigir** imediatamente discrepâncias
- **Validar** funcionalidades não funcionais
- **Atualizar** status incorretos
- **Remover** referências quebradas

#### **2. Funcionalidades Quebradas**
- **Marcar** como 🚧 Em desenvolvimento
- **Documentar** problemas encontrados
- **Criar** issues para correção
- **Atualizar** progresso real

### 📈 **Melhorias Contínuas**

#### **1. Feedback de Usuários**
- **Coletar** feedback sobre navegação
- **Identificar** problemas de usabilidade
- **Implementar** melhorias sugeridas
- **Atualizar** documentação conforme necessário

#### **2. Novas Funcionalidades**
- **Documentar** novas funcionalidades implementadas
- **Atualizar** exemplos e comandos
- **Verificar** compatibilidade com sistema existente
- **Manter** consistência na documentação

---

## 📋 **Resumo das Regras**

### ✅ **Obrigatório**
1. **Manter README.md sempre atualizado** com estrutura real
2. **Validar funcionalidades** antes de listar como ativas
3. **Atualizar métricas** baseado em testes reais
4. **Testar navegação** e contextos automaticamente
5. **Verificar links** e referências regularmente

### 🎯 **Recomendado**
1. **Atualizar mensalmente** status geral do projeto
2. **Coletar feedback** de usuários sobre navegação
3. **Implementar melhorias** baseadas em uso real
4. **Manter consistência** na formatação e estilo
5. **Documentar mudanças** importantes

### ❌ **Proibido**
1. **Listar funcionalidades** não implementadas como ativas
2. **Manter métricas** desatualizadas ou incorretas
3. **Ignorar problemas** de navegação ou contextos
4. **Usar exemplos** que não funcionam
5. **Manter referências** para arquivos inexistentes

---

**🔄 Última Atualização**: 2025-01-28  
**📊 Versão**: 1.0  
**🎯 Status**: ✅ Ativo 