---
title: Guia de Início Rápido
tags: [inicio, rapido, tutorial, basico, primeiro_passo]
type: guide
status: active
priority: alta
created: 2025-08-04
updated: 2025-08-04
---

# 🚀 **GUIA DE INÍCIO RÁPIDO - OTClient**

> [!info] **BEM-VINDO AO OTClient!**
> Este guia te ajudará a começar rapidamente com o desenvolvimento usando OTClient. Em apenas 5 minutos, você estará pronto para criar seu primeiro módulo!

---

## 📋 **ÍNDICE DETALHADO**

### **🎯 Navegação Rápida**
1. [O que é OTClient?](#-o-que-é-otclient)
2. [Primeiros Passos](#-primeiros-passos)
3. [Criando seu Primeiro Módulo](#-criando-seu-primeiro-módulo)
4. [Conceitos Básicos](#-conceitos-básicos)
5. [Próximos Passos](#-próximos-passos)

### **📚 Seções Principais**

| Seção | Descrição |
|-------|-----------|
| O que é OTClient? | Introdução e visão geral do sistema |
| Primeiros Passos | Configuração inicial e ambiente |
| Criando seu Primeiro Módulo | Tutorial prático passo a passo |
| Conceitos Básicos | Fundamentos essenciais para entender |
| Próximos Passos | Onde ir depois do básico |

---

## 🎯 **O QUE É OTCLIENT?**

### **📖 Visão Geral**
OTClient é um framework de desenvolvimento para jogos MMORPG baseado em Lua e C++. Ele fornece uma arquitetura modular e extensível para criar interfaces de usuário, sistemas de jogo e funcionalidades personalizadas.

### **🔧 Principais Características**
- **Linguagem Lua**: Scripting simples e poderoso
- **Interface OTUI**: Sistema de widgets moderno
- **Arquitetura Modular**: Componentes reutilizáveis
- **Performance Otimizada**: C++ para operações críticas
- **Documentação Completa**: Guias e exemplos detalhados

---

## 🚀 **PRIMEIROS PASSOS**

### **📋 Pré-requisitos**
- **Sistema Operacional**: Windows, Linux ou macOS
- **Conhecimento Básico**: Lua (opcional, mas recomendado)
- **Editor de Código**: VS Code, Sublime Text ou similar
- **Tempo**: 5 minutos para começar

### **⚙️ Configuração Inicial**

1. **Baixar OTClient**
   ```bash
   git clone https://github.com/otclient/otclient.git
   cd otclient
   ```

2. **Compilar o Projeto**
   ```bash
   mkdir build && cd build
   cmake ..
   make
   ```

3. **Executar pela Primeira Vez**
   ```bash
   ./otclient
   ```

### **✅ Verificação de Instalação**
- [ ] OTClient compila sem erros
- [ ] Interface gráfica abre corretamente
- [ ] Logs mostram "Sistema inicializado"
- [ ] Pasta `modules/` está presente

---

## 💻 **CRIANDO SEU PRIMEIRO MÓDULO**

### **🎯 Objetivo**
Criar um módulo simples que exibe "Olá, Mundo!" na tela.

### **📁 Estrutura do Módulo**
```
modules/meu_primeiro_modulo/
├── meu_primeiro_modulo.otmod
├── meu_primeiro_modulo.lua
└── meu_primeiro_modulo.otui
```

### **🔧 Passo 1: Criar Arquivo do Módulo**

**`meu_primeiro_modulo.otmod`**
#### Nível Basic
```xml
<?xml version="1.0" encoding="UTF-8"?>
<module>
    <name>Meu Primeiro Módulo</name>
    <description>Um módulo simples para começar</description>
    <author>Seu Nome</author>
    <version>1.0.0</version>
    <entry>meu_primeiro_modulo.lua</entry>
    <dependencies>
        <dependency>corelib</dependency>
    </dependencies>
</module>
```

#### Nível Intermediate
```xml
<?xml version="1.0" encoding="UTF-8"?>
<module>
    <name>Meu Primeiro Módulo</name>
    <description>Um módulo simples para começar</description>
    <author>Seu Nome</author>
    <version>1.0.0</version>
    <entry>meu_primeiro_modulo.lua</entry>
    <dependencies>
        <dependency>corelib</dependency>
    </dependencies>
</module>
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```xml
<?xml version="1.0" encoding="UTF-8"?>
<module>
    <name>Meu Primeiro Módulo</name>
    <description>Um módulo simples para começar</description>
    <author>Seu Nome</author>
    <version>1.0.0</version>
    <entry>meu_primeiro_modulo.lua</entry>
    <dependencies>
        <dependency>corelib</dependency>
    </dependencies>
</module>
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

### **🔧 Passo 2: Criar Lógica Lua**

**`meu_primeiro_modulo.lua`**
#### Nível Basic
```lua
-- Meu Primeiro Módulo
-- Um exemplo simples para começar

meuModulo = {}

function meuModulo.init()
    print("🎉 Meu primeiro módulo foi carregado!")
    
    -- Criar janela
    meuModulo.window = g_ui.displayUI('meu_primeiro_modulo')
    meuModulo.window:show()
    
    -- Conectar botão
    local botao = meuModulo.window:getChildById('botaoClicar')
    botao.onClick = meuModulo.onBotaoClicar
end

function meuModulo.onBotaoClicar()
    print("👋 Olá, Mundo! Botão clicado!")
    
    -- Mostrar mensagem na tela
    local label = meuModulo.window:getChildById('mensagem')
    label:setText("Olá, Mundo! 🎉")
end

function meuModulo.terminate()
    if meuModulo.window then
        meuModulo.window:destroy()
    end
end
```

#### Nível Intermediate
```lua
-- Meu Primeiro Módulo
-- Um exemplo simples para começar

meuModulo = {}

function meuModulo.init()
    print("🎉 Meu primeiro módulo foi carregado!")
    
    -- Criar janela
    meuModulo.window = g_ui.displayUI('meu_primeiro_modulo')
    meuModulo.window:show()
    
    -- Conectar botão
    local botao = meuModulo.window:getChildById('botaoClicar')
    botao.onClick = meuModulo.onBotaoClicar
end

function meuModulo.onBotaoClicar()
    print("👋 Olá, Mundo! Botão clicado!")
    
    -- Mostrar mensagem na tela
    local label = meuModulo.window:getChildById('mensagem')
    label:setText("Olá, Mundo! 🎉")
end

function meuModulo.terminate()
    if meuModulo.window then
        meuModulo.window:destroy()
    end
end
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```lua
-- Meu Primeiro Módulo
-- Um exemplo simples para começar

meuModulo = {}

function meuModulo.init()
    print("🎉 Meu primeiro módulo foi carregado!")
    
    -- Criar janela
    meuModulo.window = g_ui.displayUI('meu_primeiro_modulo')
    meuModulo.window:show()
    
    -- Conectar botão
    local botao = meuModulo.window:getChildById('botaoClicar')
    botao.onClick = meuModulo.onBotaoClicar
end

function meuModulo.onBotaoClicar()
    print("👋 Olá, Mundo! Botão clicado!")
    
    -- Mostrar mensagem na tela
    local label = meuModulo.window:getChildById('mensagem')
    label:setText("Olá, Mundo! 🎉")
end

function meuModulo.terminate()
    if meuModulo.window then
        meuModulo.window:destroy()
    end
end
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

### **🔧 Passo 3: Criar Interface OTUI**

**`meu_primeiro_modulo.otui`**
#### Nível Basic
```xml
<?xml version="1.0" encoding="UTF-8"?>
<MainWindow id="meu_primeiro_modulo" size="300 200" text="Meu Primeiro Módulo">
    <Label id="titulo" pos="10 10" size="280 30" text="Bem-vindo ao OTClient!" font="verdana-11px-antialised" text-align="center" />
    <Button id="botaoClicar" pos="100 60" size="100 30" text="Clique Aqui!" />
    <Label id="mensagem" pos="10 100" size="280 30" text="Clique no botão acima!" font="verdana-11px-antialised" text-align="center" />
</MainWindow>
```

#### Nível Intermediate
```xml
<?xml version="1.0" encoding="UTF-8"?>
<MainWindow id="meu_primeiro_modulo" size="300 200" text="Meu Primeiro Módulo">
    <Label id="titulo" pos="10 10" size="280 30" text="Bem-vindo ao OTClient!" font="verdana-11px-antialised" text-align="center" />
    <Button id="botaoClicar" pos="100 60" size="100 30" text="Clique Aqui!" />
    <Label id="mensagem" pos="10 100" size="280 30" text="Clique no botão acima!" font="verdana-11px-antialised" text-align="center" />
</MainWindow>
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```xml
<?xml version="1.0" encoding="UTF-8"?>
<MainWindow id="meu_primeiro_modulo" size="300 200" text="Meu Primeiro Módulo">
    <Label id="titulo" pos="10 10" size="280 30" text="Bem-vindo ao OTClient!" font="verdana-11px-antialised" text-align="center" />
    <Button id="botaoClicar" pos="100 60" size="100 30" text="Clique Aqui!" />
    <Label id="mensagem" pos="10 100" size="280 30" text="Clique no botão acima!" font="verdana-11px-antialised" text-align="center" />
</MainWindow>
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

### **🎮 Testando o Módulo**

1. **Copiar arquivos** para `modules/meu_primeiro_modulo/`
2. **Reiniciar OTClient**
3. **Verificar logs** para confirmação de carregamento
4. **Clicar no botão** para ver a mensagem

### **✅ Resultado Esperado**
- Módulo carrega sem erros
- Janela aparece na tela
- Botão responde ao clique
- Mensagem "Olá, Mundo!" é exibida

---

## 🧠 **CONCEITOS BÁSICOS**

### **📚 Fundamentos Essenciais**

#### **1. Módulos**
- **O que é**: Unidades de funcionalidade independentes
- **Como usar**: Carregados automaticamente pelo sistema
- **Estrutura**: Arquivo `.otmod` + `.lua` + `.otui`

#### **2. Interface OTUI**
- **O que é**: Sistema de widgets para criar interfaces
- **Componentes**: Janelas, botões, labels, inputs
- **Layout**: Posicionamento e dimensionamento automático

#### **3. Eventos e Callbacks**
- **O que é**: Sistema de comunicação entre componentes
- **Exemplos**: `onClick`, `onTextChange`, `onVisibilityChange`
- **Como usar**: Conectar funções a eventos

#### **4. Sistema de Arquivos**
- **Estrutura**: Organização hierárquica de módulos
- **Recursos**: Imagens, sons, dados
- **Acesso**: Via `g_resources` e `g_ui`

### **🔧 Ferramentas Importantes**

#### **Debug e Logs**
```lua
-- Logs básicos
print("Mensagem de debug")

-- Logs com contexto
    --  Logs com contexto (traduzido)
g_logger.info("Informação importante")
g_logger.warning("Aviso do sistema")
g_logger.error("Erro encontrado")
```

#### **Acesso a Recursos**
```lua
-- Verificar se arquivo existe
    --  Verificar se arquivo existe (traduzido)
if g_resources.fileExists("images/icon.png") then
    -- Verificação condicional
    -- Usar recurso
    --  Usar recurso (traduzido)
end

-- Carregar arquivo
    --  Carregar arquivo (traduzido)
local content = g_resources.readFileContents("data/config.txt")
```

---

## 🔍 **TROUBLESHOOTING COMUM**

### **❌ Problemas Frequentes**

#### **1. Módulo não carrega**
**Sintomas**: Erro no log, janela não aparece
**Soluções**:
- Verificar sintaxe Lua
- Confirmar estrutura de arquivos
- Verificar dependências no `.otmod`

#### **2. Interface não aparece**
**Sintomas**: Módulo carrega mas janela não mostra
**Soluções**:
- Verificar se `g_ui.displayUI()` foi chamado
- Confirmar se `window:show()` foi executado
- Verificar sintaxe OTUI

#### **3. Botões não respondem**
**Sintomas**: Interface aparece mas botões não funcionam
**Soluções**:
- Verificar se `onClick` foi conectado
- Confirmar se função existe
- Verificar logs de erro

#### **4. Erros de compilação**
**Sintomas**: OTClient não inicia
**Soluções**:
- Verificar dependências do sistema
- Limpar e recompilar
- Verificar versão do CMake

### **🔧 Ferramentas de Debug**

#### **Console de Desenvolvimento**
```lua
-- Abrir console
    --  Abrir console (traduzido)
g_ui.displayUI('console')

-- Executar comandos
    --  Executar comandos (traduzido)
g_console.executeCommand('help')
```

#### **Inspetor de Interface**
#### Nível Basic
```lua
-- Mostrar informações de widget
local widget = g_ui.getRootWidget():getChildById('meuBotao')
print("Posição:", widget:getPosition())
print("Tamanho:", widget:getSize())
```

#### Nível Intermediate
```lua
-- Mostrar informações de widget
local widget = g_ui.getRootWidget():getChildById('meuBotao')
print("Posição:", widget:getPosition())
print("Tamanho:", widget:getSize())
```

#### Nível Advanced
```lua
-- Mostrar informações de widget
local widget = g_ui.getRootWidget():getChildById('meuBotao')
print("Posição:", widget:getPosition())
print("Tamanho:", widget:getSize())
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

---

## 🚀 **PRÓXIMOS PASSOS**

### **📚 Aprendizado Progressivo**

#### **Nível Básico (1-2 semanas)**
- [ ] Dominar sintaxe Lua básica
- [ ] Criar interfaces simples
- [ ] Entender sistema de eventos
- [ ] Trabalhar com recursos

#### **Nível Intermediário (1-2 meses)**
- [ ] Criar módulos complexos
- [ ] Implementar sistemas de dados
- [ ] Trabalhar com networking
- [ ] Otimizar performance

#### **Nível Avançado (3+ meses)**
- [ ] Desenvolver sistemas completos
- [ ] Contribuir para o projeto
- [ ] Criar documentação
- [ ] Mentorear outros desenvolvedores

### **📖 Recursos Recomendados**

#### **Documentação Essencial**
- [Guia de Configuração](../docs/otclient/guides/Configuration_Guide.md)
- [Guia de Desenvolvimento de Módulos](../docs/otclient/guides/Module_Development_Guide.md)
- [Referência da API Lua](../docs/otclient/guides/Lua_API_Reference.md)

#### **Exemplos Práticos**
- [Exemplos de Código](../docs/otclient/guides/CodeExamples.md)
- [Melhores Práticas](../docs/otclient/guides/BestPractices.md)
- [Troubleshooting](../docs/otclient/guides/Troubleshooting.md)

#### **Comunidade**
- [Fórum de Desenvolvedores](https://otland.net)
- [GitHub do Projeto](https://github.com/otclient/otclient)
- [Canal de Discord](https://discord.gg/otclient)

---

## 🎯 **RESUMO RÁPIDO**

### **✅ O que você aprendeu**
1. **Configuração**: Como instalar e configurar OTClient
2. **Primeiro Módulo**: Criou um módulo funcional do zero
3. **Conceitos Básicos**: Entendeu fundamentos do sistema
4. **Troubleshooting**: Aprendeu a resolver problemas comuns
5. **Próximos Passos**: Tem um roteiro de aprendizado

### **🚀 Pronto para Começar**
- ✅ Ambiente configurado
- ✅ Primeiro módulo funcionando
- ✅ Conceitos básicos compreendidos
- ✅ Ferramentas de debug conhecidas
- ✅ Roteiro de aprendizado definido

---

## 🧭 **NAVEGAÇÃO**

### **📖 Guias Relacionados**
- [Guia de Configuração](../docs/otclient/guides/Configuration_Guide.md)
- [Guia de Desenvolvimento de Módulos](../docs/otclient/guides/Module_Development_Guide.md)
- [Guia de Troubleshooting](../docs/otclient/guides/Troubleshooting.md)

### **🔗 Links Úteis**
- [Documentação Principal](../README.md)
- [Índice da Wiki](../Wiki_Index.md)
- [Sistema de Busca](../Navigation_Index_Search.md)

### **📞 Suporte**
Para dúvidas ou problemas:
- Consulte a seção [Troubleshooting](#troubleshooting-comum)
- Verifique os [Exemplos Práticos](#criando-seu-primeiro-módulo)
- Consulte a [Referência da API](../docs/otclient/guides/Lua_API_Reference.md)

---

> [!success] **PARABÉNS!**
> Você completou o Guia de Início Rápido e está pronto para começar sua jornada no desenvolvimento com OTClient! 🎉 