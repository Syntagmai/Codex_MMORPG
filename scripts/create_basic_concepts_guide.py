#!/usr/bin/env python3
"""
Script para criar guia de conceitos básicos e troubleshooting comum.
Adiciona explicações detalhadas de conceitos fundamentais.
"""

import os
from pathlib import Path
from datetime import datetime

def create_basic_concepts_guide():
    """Cria guia de conceitos básicos com explicações detalhadas."""
    
    guide_file = Path("wiki/Conceitos_Basicos.md")
    
    print("📚 Criando guia de conceitos básicos...")
    
    content = """---
title: Conceitos Básicos
tags: [conceitos, basico, fundamentos, explicacao, tutorial]
type: guide
status: active
priority: alta
created: 2025-08-04
updated: 2025-08-04
---

# 🧠 **CONCEITOS BÁSICOS - OTClient**

> [!info] **FUNDAMENTOS ESSENCIAIS**
> Este guia explica os conceitos básicos necessários para entender e trabalhar com OTClient.

---

## 📋 **ÍNDICE DETALHADO**

### **🎯 Navegação Rápida**
1. [O que é Programação?](#-o-que-é-programação)
2. [Linguagens de Programação](#-linguagens-de-programação)
3. [Conceitos de Interface](#-conceitos-de-interface)
4. [Sistema de Arquivos](#-sistema-de-arquivos)
5. [Debug e Erros](#-debug-e-erros)

---

## 💻 **O QUE É PROGRAMAÇÃO?**

### **📖 Definição Básica**
Programação é o processo de criar instruções para um computador executar tarefas específicas. É como escrever uma receita de bolo - você diz ao computador exatamente o que fazer, passo a passo.

### **🔧 Analogias Simples**

#### **Receita de Bolo**
- **Ingredientes** = Variáveis (dados)
- **Passos** = Instruções (código)
- **Resultado** = Programa funcionando

#### **Lego**
- **Peças** = Funções e componentes
- **Montagem** = Programação
- **Modelo final** = Aplicação completa

### **🎯 Por que Programar?**
- **Automatizar tarefas** repetitivas
- **Resolver problemas** complexos
- **Criar ferramentas** úteis
- **Expressar criatividade** através do código

---

## 🔤 **LINGUAGENS DE PROGRAMAÇÃO**

### **📝 O que são Linguagens?**

#### **Definição**
Linguagens de programação são formas de comunicação entre humanos e computadores. Cada linguagem tem suas regras e sintaxe específicas.

#### **Tipos de Linguagens**

##### **Linguagens Interpretadas (Lua)**
- **Como funciona**: Código é executado linha por linha
- **Vantagens**: Fácil de aprender, desenvolvimento rápido
- **Desvantagens**: Mais lento que linguagens compiladas
- **Exemplo**: Lua, Python, JavaScript

##### **Linguagens Compiladas (C++)**
- **Como funciona**: Código é convertido em linguagem de máquina
- **Vantagens**: Muito rápido, controle total
- **Desvantagens**: Mais complexo, desenvolvimento mais lento
- **Exemplo**: C++, C, Rust

### **🔧 Lua - Linguagem Principal do OTClient**

#### **Características**
- **Sintaxe simples** e intuitiva
- **Tipagem dinâmica** (não precisa declarar tipos)
- **Garbage collection** automático
- **Interpretada** (execução direta)

#### **Exemplo Básico**
```lua
-- Variável simples
local nome = "João"
local idade = 25

-- Função básica
function cumprimentar(pessoa)
    print("Olá, " .. pessoa .. "!")
end

-- Usar a função
cumprimentar(nome)
```

#### **Conceitos Importantes**

##### **Variáveis**
- **O que são**: Espaços para armazenar dados
- **Tipos**: Texto (string), números, booleanos (true/false)
- **Exemplo**: `local contador = 0`

##### **Funções**
- **O que são**: Blocos de código reutilizáveis
- **Função**: Encapsular lógica, evitar repetição
- **Exemplo**: `function somar(a, b) return a + b end`

##### **Tabelas (Arrays)**
- **O que são**: Estruturas para organizar dados
- **Uso**: Listas, dicionários, objetos
- **Exemplo**: `local frutas = {"maçã", "banana", "laranja"}`

---

## 🖥️ **CONCEITOS DE INTERFACE**

### **🎨 O que é Interface do Usuário?**

#### **Definição**
Interface do usuário (UI) é tudo que o usuário vê e com o qual interage no programa. É como a "cara" do programa.

#### **Elementos Básicos**

##### **Janela (Window)**
- **O que é**: Área principal onde o programa aparece
- **Função**: Conter outros elementos
- **Exemplo**: Janela do navegador, janela do Word

##### **Botão (Button)**
- **O que é**: Elemento clicável para ações
- **Função**: Executar comandos quando clicado
- **Exemplo**: Botão "Salvar", "Cancelar", "OK"

##### **Campo de Texto (TextEdit)**
- **O que é**: Área para digitar texto
- **Função**: Coletar informações do usuário
- **Exemplo**: Campo de login, caixa de pesquisa

##### **Lista (List)**
- **O que é**: Lista de itens para seleção
- **Função**: Mostrar opções disponíveis
- **Exemplo**: Lista de arquivos, menu dropdown

### **🎯 Eventos e Interação**

#### **O que são Eventos?**
Eventos são ações que acontecem quando o usuário interage com a interface.

#### **Eventos Comuns**
- **Clique**: Usuário clica em algo
- **Digitação**: Usuário digita texto
- **Movimento do mouse**: Usuário move o cursor
- **Carregamento**: Programa termina de carregar

#### **Como Responder a Eventos**
```lua
-- Quando botão é clicado
botao.onClick = function()
    print("Botão foi clicado!")
end

-- Quando texto muda
campo.onTextChange = function()
    print("Texto foi alterado!")
end
```

---

## 📁 **SISTEMA DE ARQUIVOS**

### **🗂️ O que é Sistema de Arquivos?**

#### **Definição**
Sistema de arquivos é a forma como o computador organiza e armazena arquivos. É como uma biblioteca com prateleiras e livros.

#### **Conceitos Básicos**

##### **Arquivo**
- **O que é**: Unidade básica de informação
- **Tipos**: Texto, imagem, som, programa
- **Exemplo**: `documento.txt`, `foto.jpg`, `musica.mp3`

##### **Pasta (Diretório)**
- **O que é**: Container para organizar arquivos
- **Função**: Agrupar arquivos relacionados
- **Exemplo**: `Documentos/`, `Imagens/`, `Downloads/`

##### **Caminho (Path)**
- **O que é**: Endereço para localizar um arquivo
- **Formato**: `pasta/subpasta/arquivo.extensao`
- **Exemplo**: `Documents/Trabalho/relatorio.pdf`

### **🔧 No Contexto do OTClient**

#### **Estrutura de Pastas**
```
otclient/
├── modules/          # Módulos do sistema
├── data/            # Dados e recursos
├── src/             # Código fonte
└── docs/            # Documentação
```

#### **Acessando Arquivos**
```lua
-- Verificar se arquivo existe
if g_resources.fileExists("config.txt") then
    print("Arquivo encontrado!")
end

-- Ler conteúdo do arquivo
local conteudo = g_resources.readFileContents("dados.txt")
```

---

## 🐛 **DEBUG E ERROS**

### **❌ O que são Erros?**

#### **Definição**
Erros são problemas que impedem o programa de funcionar corretamente. São como "bugs" que precisam ser corrigidos.

#### **Tipos de Erros**

##### **Erro de Sintaxe**
- **O que é**: Erro na escrita do código
- **Causa**: Parênteses não fechados, ponto e vírgula faltando
- **Exemplo**: `print("Olá"` (faltando parêntese)

##### **Erro de Execução**
- **O que é**: Erro que acontece durante a execução
- **Causa**: Tentar dividir por zero, arquivo não encontrado
- **Exemplo**: `local resultado = 10 / 0`

##### **Erro de Lógica**
- **O que é**: Programa funciona, mas resultado está errado
- **Causa**: Algoritmo incorreto, condição mal formulada
- **Exemplo**: Soma que deveria multiplicar

### **🔧 Como Debugar**

#### **Debug Básico**
```lua
-- Imprimir valores para debug
print("Valor da variável:", variavel)

-- Verificar se código está sendo executado
print("Cheguei até aqui!")

-- Verificar tipo de variável
print("Tipo:", type(variavel))
```

#### **Ferramentas de Debug**
- **Console**: Mostra mensagens de debug
- **Logs**: Registra informações do programa
- **Breakpoints**: Pausa execução em pontos específicos

---

## 🎯 **EXEMPLOS PRÁTICOS SIMPLES**

### **💡 Exemplo 1: Calculadora Simples**

```lua
-- Calculadora básica
function calculadora()
    print("=== Calculadora ===")
    print("Digite o primeiro número:")
    local num1 = tonumber(io.read())
    
    print("Digite o segundo número:")
    local num2 = tonumber(io.read())
    
    print("Escolha a operação (+, -, *, /):")
    local operacao = io.read()
    
    local resultado = 0
    
    if operacao == "+" then
        resultado = num1 + num2
    elseif operacao == "-" then
        resultado = num1 - num2
    elseif operacao == "*" then
        resultado = num1 * num2
    elseif operacao == "/" then
        resultado = num1 / num2
    else
        print("Operação inválida!")
        return
    end
    
    print("Resultado:", resultado)
end

-- Executar calculadora
calculadora()
```

### **💡 Exemplo 2: Lista de Tarefas**

```lua
-- Lista de tarefas simples
local tarefas = {}

function adicionarTarefa(descricao)
    table.insert(tarefas, descricao)
    print("Tarefa adicionada:", descricao)
end

function listarTarefas()
    print("=== Lista de Tarefas ===")
    for i, tarefa in ipairs(tarefas) do
        print(i .. ". " .. tarefa)
    end
end

function removerTarefa(indice)
    if tarefas[indice] then
        table.remove(tarefas, indice)
        print("Tarefa removida!")
    else
        print("Tarefa não encontrada!")
    end
end

-- Usar a lista
adicionarTarefa("Estudar Lua")
adicionarTarefa("Fazer exercícios")
adicionarTarefa("Ler documentação")
listarTarefas()
removerTarefa(2)
listarTarefas()
```

---

## 🚀 **PRÓXIMOS PASSOS**

### **📚 Aprendizado Progressivo**

#### **Nível Iniciante**
- [ ] Entender conceitos básicos de programação
- [ ] Aprender sintaxe Lua básica
- [ ] Criar programas simples
- [ ] Entender sistema de arquivos

#### **Nível Básico**
- [ ] Trabalhar com funções e tabelas
- [ ] Criar interfaces simples
- [ ] Entender eventos e callbacks
- [ ] Debug básico

#### **Nível Intermediário**
- [ ] Criar módulos OTClient
- [ ] Trabalhar com OTUI
- [ ] Implementar sistemas complexos
- [ ] Otimizar código

### **📖 Recursos Recomendados**

#### **Para Iniciantes**
- [Guia de Início Rápido](Guia_Inicio_Rapido.md)
- [Tutorial Lua Online](https://www.lua.org/pil/)
- [Exemplos de Código](../docs/otclient/guides/CodeExamples.md)

#### **Para Desenvolvedores**
- [Guia de Desenvolvimento de Módulos](../docs/otclient/guides/Module_Development_Guide.md)
- [Referência da API Lua](../docs/otclient/guides/Lua_API_Reference.md)
- [Melhores Práticas](../docs/otclient/guides/BestPractices.md)

---

## 🧭 **NAVEGAÇÃO**

### **📖 Guias Relacionados**
- [Guia de Início Rápido](Guia_Inicio_Rapido.md)
- [Glossário Técnico](Glossario_Tecnico.md)
- [Troubleshooting Comum](Troubleshooting_Comum.md)

### **🔗 Links Úteis**
- [Documentação Principal](../README.md)
- [Índice da Wiki](../Wiki_Index.md)
- [Sistema de Busca](../Navigation_Index_Search.md)

---

> [!success] **FUNDAMENTOS SÓLIDOS**
> Agora você tem uma base sólida de conceitos básicos para começar sua jornada no desenvolvimento com OTClient! 🚀
"""
    
    # Salvar arquivo
    with open(guide_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Guia de conceitos básicos criado: {guide_file}")
    return True

def create_troubleshooting_common():
    """Cria guia de troubleshooting comum."""
    
    troubleshooting_file = Path("wiki/Troubleshooting_Comum.md")
    
    print("🔧 Criando guia de troubleshooting comum...")
    
    content = """---
title: Troubleshooting Comum
tags: [troubleshooting, problemas, solucoes, debug, ajuda]
type: guide
status: active
priority: alta
created: 2025-08-04
updated: 2025-08-04
---

# 🔧 **TROUBLESHOOTING COMUM - OTClient**

> [!info] **SOLUÇÕES PARA PROBLEMAS FREQUENTES**
> Este guia contém soluções para os problemas mais comuns encontrados ao trabalhar com OTClient.

---

## 📋 **ÍNDICE DETALHADO**

### **🎯 Navegação Rápida**
1. [Problemas de Instalação](#-problemas-de-instalação)
2. [Problemas de Compilação](#-problemas-de-compilação)
3. [Problemas de Módulos](#-problemas-de-módulos)
4. [Problemas de Interface](#-problemas-de-interface)
5. [Problemas de Performance](#-problemas-de-performance)
6. [Problemas de Rede](#-problemas-de-rede)

---

## ⚠️ **PROBLEMAS DE INSTALAÇÃO**

### **❌ OTClient não inicia**

#### **Sintomas**
- Programa não abre
- Erro "Executable not found"
- Tela em branco

#### **Soluções**

##### **1. Verificar Dependências**
```bash
# Windows
# Verificar se Visual Studio Redistributable está instalado

# Linux
sudo apt-get install libgl1-mesa-glx libglu1-mesa
sudo apt-get install libxrandr2 libxinerama1 libxcursor1

# macOS
# Verificar se Xcode Command Line Tools está instalado
xcode-select --install
```

##### **2. Verificar Permissões**
```bash
# Linux/macOS
chmod +x otclient

# Windows
# Executar como administrador
```

##### **3. Verificar Arquivos**
```bash
# Verificar se todos os arquivos estão presentes
ls -la
# Deve mostrar: otclient, data/, modules/, etc.
```

### **❌ Dependências faltando**

#### **Sintomas**
- Erro "Library not found"
- Erro "DLL missing"

#### **Soluções**

##### **Windows**
```bash
# Instalar Visual C++ Redistributable
# Baixar da Microsoft: https://aka.ms/vs/17/release/vc_redist.x64.exe

# Verificar PATH
echo %PATH%
# Deve incluir caminho para bibliotecas
```

##### **Linux**
```bash
# Instalar dependências básicas
sudo apt-get update
sudo apt-get install build-essential cmake
sudo apt-get install libgl1-mesa-dev libglu1-mesa-dev
sudo apt-get install libxrandr-dev libxinerama-dev libxcursor-dev
```

##### **macOS**
```bash
# Instalar Homebrew (se não tiver)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar dependências
brew install cmake
brew install glfw
brew install openal-soft
```

---

## 🔨 **PROBLEMAS DE COMPILAÇÃO**

### **❌ Erro de compilação**

#### **Sintomas**
- `make` falha
- Erro de sintaxe C++
- Erro de linking

#### **Soluções**

##### **1. Limpar e Recompilar**
```bash
# Limpar build anterior
rm -rf build/
mkdir build
cd build

# Reconfigurar
cmake ..

# Compilar
make -j4
```

##### **2. Verificar Versão do CMake**
```bash
cmake --version
# Deve ser 3.10 ou superior
```

##### **3. Verificar Compilador**
```bash
# GCC (Linux)
gcc --version

# Clang (macOS)
clang --version

# MSVC (Windows)
cl
```

##### **4. Erros Específicos**

###### **Erro: "No such file or directory"**
```bash
# Verificar se arquivos de cabeçalho estão presentes
find . -name "*.h" | head -10

# Verificar CMakeLists.txt
cat CMakeLists.txt
```

###### **Erro: "Undefined reference"**
```bash
# Verificar se bibliotecas estão linkadas
# Verificar CMakeLists.txt - target_link_libraries
```

---

## 📦 **PROBLEMAS DE MÓDULOS**

### **❌ Módulo não carrega**

#### **Sintomas**
- Erro no log: "Failed to load module"
- Módulo não aparece na lista
- Funcionalidade não funciona

#### **Soluções**

##### **1. Verificar Estrutura do Módulo**
```
modules/meu_modulo/
├── meu_modulo.otmod    # Arquivo de definição
├── meu_modulo.lua      # Código Lua
└── meu_modulo.otui     # Interface (opcional)
```

##### **2. Verificar Sintaxe Lua**
```lua
-- Verificar se não há erros de sintaxe
-- Usar linter Lua se disponível

-- Exemplo de módulo básico
meuModulo = {}

function meuModulo.init()
    print("Módulo inicializado!")
end

function meuModulo.terminate()
    print("Módulo finalizado!")
end
```

##### **3. Verificar Arquivo .otmod**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<module>
    <name>Meu Módulo</name>
    <description>Descrição do módulo</description>
    <author>Seu Nome</author>
    <version>1.0.0</version>
    <entry>meu_modulo.lua</entry>
    <dependencies>
        <dependency>corelib</dependency>
    </dependencies>
</module>
```

##### **4. Verificar Dependências**
```lua
-- Verificar se dependências estão carregadas
if not g_ui then
    print("ERRO: g_ui não está disponível!")
    return
end
```

### **❌ Módulo carrega mas não funciona**

#### **Sintomas**
- Módulo aparece na lista
- Não há erros no log
- Funcionalidade não responde

#### **Soluções**

##### **1. Verificar Inicialização**
```lua
function meuModulo.init()
    print("DEBUG: Inicializando módulo...")
    
    -- Verificar se recursos estão disponíveis
    if not g_resources.fileExists("meu_modulo.otui") then
        print("ERRO: Arquivo OTUI não encontrado!")
        return
    end
    
    -- Criar interface
    meuModulo.window = g_ui.displayUI('meu_modulo')
    if not meuModulo.window then
        print("ERRO: Falha ao criar interface!")
        return
    end
    
    print("DEBUG: Módulo inicializado com sucesso!")
end
```

##### **2. Verificar Eventos**
```lua
-- Verificar se eventos estão conectados
local button = meuModulo.window:getChildById('meuBotao')
if button then
    button.onClick = function()
        print("DEBUG: Botão clicado!")
        -- Sua lógica aqui
    end
else
    print("ERRO: Botão não encontrado!")
end
```

---

## 🖥️ **PROBLEMAS DE INTERFACE**

### **❌ Interface não aparece**

#### **Sintomas**
- Módulo carrega sem erros
- Janela não aparece na tela
- Interface não responde

#### **Soluções**

##### **1. Verificar Criação da Interface**
```lua
function meuModulo.init()
    -- Criar interface
    meuModulo.window = g_ui.displayUI('meu_modulo')
    
    -- Verificar se foi criada
    if not meuModulo.window then
        print("ERRO: Falha ao criar janela!")
        return
    end
    
    -- Mostrar janela
    meuModulo.window:show()
    
    -- Verificar se está visível
    if not meuModulo.window:isVisible() then
        print("ERRO: Janela não está visível!")
    end
end
```

##### **2. Verificar Arquivo OTUI**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<MainWindow id="meu_modulo" size="300 200" text="Meu Módulo">
    <Label id="titulo" pos="10 10" size="280 30" text="Título" />
    <Button id="botao" pos="100 80" size="100 30" text="Clique Aqui!" />
</MainWindow>
```

##### **3. Verificar Posição da Janela**
```lua
-- Posicionar janela no centro
local screenSize = g_window.getSize()
local windowSize = meuModulo.window:getSize()
local x = (screenSize.width - windowSize.width) / 2
local y = (screenSize.height - windowSize.height) / 2
meuModulo.window:setPosition({x = x, y = y})
```

### **❌ Botões não respondem**

#### **Sintomas**
- Interface aparece corretamente
- Botões não executam ações
- Eventos não são disparados

#### **Soluções**

##### **1. Verificar Conexão de Eventos**
```lua
function meuModulo.init()
    meuModulo.window = g_ui.displayUI('meu_modulo')
    meuModulo.window:show()
    
    -- Conectar eventos
    local button = meuModulo.window:getChildById('meuBotao')
    if button then
        button.onClick = function()
            print("DEBUG: Botão clicado!")
            -- Sua lógica aqui
        end
        print("DEBUG: Evento conectado!")
    else
        print("ERRO: Botão não encontrado!")
    end
end
```

##### **2. Verificar IDs no OTUI**
```xml
<!-- Verificar se ID está correto -->
<Button id="meuBotao" pos="100 80" size="100 30" text="Clique Aqui!" />
```

##### **3. Usar Debug para Verificar**
```lua
-- Listar todos os widgets da janela
function listarWidgets(widget, nivel)
    nivel = nivel or 0
    local indent = string.rep("  ", nivel)
    print(indent .. "- " .. widget:getId() .. " (" .. widget:getClassName() .. ")")
    
    for _, child in ipairs(widget:getChildren()) do
        listarWidgets(child, nivel + 1)
    end
end

-- Usar na inicialização
listarWidgets(meuModulo.window)
```

---

## ⚡ **PROBLEMAS DE PERFORMANCE**

### **❌ Programa lento**

#### **Sintomas**
- Interface responde lentamente
- Uso alto de CPU
- Uso alto de memória

#### **Soluções**

##### **1. Otimizar Loops**
```lua
-- ❌ Ruim: Loop desnecessário
for i = 1, 1000 do
    -- Operação pesada
end

-- ✅ Bom: Evitar loops desnecessários
if condicao then
    -- Operação apenas quando necessário
end
```

##### **2. Gerenciar Memória**
```lua
-- Limpar referências quando não precisar mais
function meuModulo.terminate()
    if meuModulo.window then
        meuModulo.window:destroy()
        meuModulo.window = nil
    end
end
```

##### **3. Usar Timers Eficientemente**
```lua
-- ❌ Ruim: Timer muito frequente
connect(g_timer, { onTimeout = function()
    -- Operação pesada a cada 16ms
end })
g_timer:start(16)

-- ✅ Bom: Timer menos frequente
connect(g_timer, { onTimeout = function()
    -- Operação a cada 100ms
end })
g_timer:start(100)
```

### **❌ Vazamento de Memória**

#### **Sintomas**
- Uso de memória aumenta com o tempo
- Programa fica mais lento
- Crashes após uso prolongado

#### **Soluções**

##### **1. Limpar Event Listeners**
```lua
-- Desconectar eventos quando não precisar mais
function meuModulo.terminate()
    if meuModulo.button then
        disconnect(meuModulo.button, { onClick = meuModulo.onClick })
    end
end
```

##### **2. Limpar Timers**
```lua
-- Parar timers
function meuModulo.terminate()
    if meuModulo.timer then
        meuModulo.timer:stop()
        meuModulo.timer = nil
    end
end
```

##### **3. Verificar Referências Circulares**
```lua
-- Evitar referências circulares
meuModulo.data = {}
meuModulo.data.parent = meuModulo  -- ❌ Referência circular

-- ✅ Bom: Usar weak references se necessário
```

---

## 🌐 **PROBLEMAS DE REDE**

### **❌ Conexão falha**

#### **Sintomas**
- Não consegue conectar ao servidor
- Conexão instável
- Timeout de conexão

#### **Soluções**

##### **1. Verificar Configuração de Rede**
```lua
-- Verificar configurações de conexão
local config = g_settings.getNode('general')
local host = config:getString('host', 'localhost')
local port = config:getInt('port', 7172)

print("Tentando conectar a:", host .. ":" .. port)
```

##### **2. Verificar Firewall**
```bash
# Windows
# Verificar Windows Firewall

# Linux
sudo ufw status
sudo ufw allow 7172

# macOS
# Verificar System Preferences > Security & Privacy > Firewall
```

##### **3. Testar Conexão**
```bash
# Testar conectividade
ping servidor.com
telnet servidor.com 7172
```

### **❌ Dados corrompidos**

#### **Sintomas**
- Informações incorretas recebidas
- Interface mostra dados estranhos
- Crashes ao receber dados

#### **Soluções**

##### **1. Validar Dados Recebidos**
```lua
-- Validar dados antes de usar
function processarDados(dados)
    if not dados then
        print("ERRO: Dados nulos recebidos!")
        return
    end
    
    if type(dados) ~= "table" then
        print("ERRO: Dados não são uma tabela!")
        return
    end
    
    -- Processar dados válidos
    print("Dados válidos:", dados)
end
```

##### **2. Usar Try-Catch**
```lua
-- Capturar erros de processamento
function processarComSeguranca(dados)
    local success, result = pcall(function()
        return processarDados(dados)
    end)
    
    if not success then
        print("ERRO ao processar dados:", result)
    end
end
```

---

## 🔍 **FERRAMENTAS DE DEBUG**

### **📝 Logging Avançado**

#### **Sistema de Logs**
```lua
-- Sistema de logging personalizado
local logger = {}

function logger.debug(message)
    print("[DEBUG] " .. os.date("%H:%M:%S") .. " - " .. message)
end

function logger.info(message)
    print("[INFO] " .. os.date("%H:%M:%S") .. " - " .. message)
end

function logger.error(message)
    print("[ERROR] " .. os.date("%H:%M:%S") .. " - " .. message)
end

-- Usar
logger.debug("Iniciando módulo...")
logger.info("Módulo carregado")
logger.error("Falha ao carregar recurso")
```

#### **Debug de Variáveis**
```lua
-- Função para inspecionar variáveis
function inspect(var, name)
    name = name or "variável"
    print("=== INSPEÇÃO: " .. name .. " ===")
    print("Tipo:", type(var))
    print("Valor:", tostring(var))
    
    if type(var) == "table" then
        print("Conteúdo da tabela:")
        for k, v in pairs(var) do
            print("  " .. tostring(k) .. " = " .. tostring(v))
        end
    end
    print("========================")
end

-- Usar
local dados = {nome = "João", idade = 25}
inspect(dados, "dados")
```

### **🎯 Debug de Interface**

#### **Inspetor de Widgets**
```lua
-- Função para inspecionar widgets
function inspecionarWidget(widget, nivel)
    nivel = nivel or 0
    local indent = string.rep("  ", nivel)
    
    print(indent .. "Widget: " .. widget:getId())
    print(indent .. "  Classe: " .. widget:getClassName())
    print(indent .. "  Posição: " .. tostring(widget:getPosition().x) .. ", " .. tostring(widget:getPosition().y))
    print(indent .. "  Tamanho: " .. tostring(widget:getSize().width) .. "x" .. tostring(widget:getSize().height))
    print(indent .. "  Visível: " .. tostring(widget:isVisible()))
    
    for _, child in ipairs(widget:getChildren()) do
        inspecionarWidget(child, nivel + 1)
    end
end

-- Usar
inspecionarWidget(meuModulo.window)
```

---

## 🚀 **PRÓXIMOS PASSOS**

### **📚 Recursos Adicionais**

#### **Documentação Oficial**
- [Guia de Início Rápido](Guia_Inicio_Rapido.md)
- [Conceitos Básicos](Conceitos_Basicos.md)
- [Glossário Técnico](Glossario_Tecnico.md)

#### **Comunidade**
- [Fórum OTClient](https://otland.net)
- [GitHub Issues](https://github.com/otclient/otclient/issues)
- [Discord Community](https://discord.gg/otclient)

#### **Ferramentas Úteis**
- [Lua Debugger](https://marketplace.visualstudio.com/items?itemName=actboy168.lua-debug)
- [Lua Linter](https://marketplace.visualstudio.com/items?itemName=sumneko.lua)
- [OTClient Tools](../tools/)

---

## 🧭 **NAVEGAÇÃO**

### **📖 Guias Relacionados**
- [Guia de Início Rápido](Guia_Inicio_Rapido.md)
- [Conceitos Básicos](Conceitos_Basicos.md)
- [Glossário Técnico](Glossario_Tecnico.md)

### **🔗 Links Úteis**
- [Documentação Principal](../README.md)
- [Índice da Wiki](../Wiki_Index.md)
- [Sistema de Busca](../Navigation_Index_Search.md)

---

> [!success] **PROBLEMAS RESOLVIDOS**
> Com este guia, você tem soluções para os problemas mais comuns do OTClient. Se não encontrar a solução aqui, consulte a comunidade! 🔧
"""
    
    # Salvar arquivo
    with open(troubleshooting_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Guia de troubleshooting criado: {troubleshooting_file}")
    return True

def main():
    """Função principal."""
    print("🔧 Criando guias de conceitos básicos e troubleshooting...")
    
    # Criar guia de conceitos básicos
    create_basic_concepts_guide()
    
    # Criar guia de troubleshooting
    create_troubleshooting_common()
    
    print("✅ Todos os guias foram criados com sucesso!")

if __name__ == "__main__":
    main() 
## 🔗 **Links Automáticos - Scripts**

> [!info] **Script de Automação**
> Este script faz parte do sistema de automação da wiki

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]

### **🔧 Links de Scripts**
- [[../update/README|Documentação de Scripts]]
- [[../maps/scripts_index|Índice de Scripts]]
- [[../templates/README|Templates de Scripts]]

### **📊 Scripts Relacionados**
- [[../update/automatic_linkage_system.py|automatic_linkage_system.py]]
- [[../update/create_automatic_link_templates.py|create_automatic_link_templates.py]]
- [[../update/orphan_files_analyzer.py|orphan_files_analyzer.py]]
- [[../update/update_json_maps.py|update_json_maps.py]]

### **📈 Métricas do Script**
- **Nome**: create_basic_concepts_guide
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

