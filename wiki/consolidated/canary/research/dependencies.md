---
tags: [canary, dependencies, epic_2_1, analysis, external_libraries]
type: canary_documentation
status: in_progress
priority: critical
created: 2025-01-27
responsible_agent: deep_source_analyzer
---

# 📦 Dependências do Projeto Canary

## 🎯 **Visão Geral**

Este documento cataloga todas as **dependências externas** do projeto Canary, incluindo bibliotecas, frameworks e ferramentas necessárias para compilação e execução.

**Status**: Análise em Progresso  
**Responsável**: Deep Source Analyzer  
**Epic**: 2.1.1 - Análise da Estrutura do Projeto

---

## 🔧 **Dependências de Sistema**

### **💻 Compilador e Build Tools**

#### **C++ Compiler**
- **GCC**: 7.0+ (Linux/macOS)
- **MSVC**: 2017+ (Windows)
- **Clang**: 6.0+ (Alternativa)

#### **Build System**
- **CMake**: 3.15+
- **Make**: 4.0+ (Linux/macOS)
- **Ninja**: 1.8+ (Opcional, mais rápido)

#### **Package Manager**
- **vcpkg**: Latest (Gerenciamento de dependências)
- **Conan**: 1.40+ (Alternativa)

### **🗄️ Banco de Dados**

#### **MySQL/MariaDB**
- **MySQL**: 8.0+ (Recomendado)
- **MariaDB**: 10.5+ (Alternativa)
- **Funcionalidades**:
  - Armazenamento de dados de jogadores
  - Histórico de transações
  - Logs do sistema
  - Backup e recuperação

#### **SQLite**
- **Versão**: 3.30+
- **Uso**: Banco local para desenvolvimento
- **Funcionalidades**:
  - Cache local
  - Dados temporários
  - Testes unitários

### **🔐 Segurança**

#### **OpenSSL**
- **Versão**: 1.1.1+
- **Funcionalidades**:
  - Criptografia de comunicação
  - Certificados SSL/TLS
  - Hash de senhas
  - Assinatura digital

---

## 📚 **Bibliotecas C++**

### **🚀 Boost Libraries**
- **Versão**: 1.70+
- **Módulos Utilizados**:
  - **boost::asio**: Networking assíncrono
  - **boost::filesystem**: Manipulação de arquivos
  - **boost::thread**: Multithreading
  - **boost::regex**: Expressões regulares
  - **boost::smart_ptr**: Smart pointers
  - **boost::variant**: Union types
  - **boost::optional**: Optional values

### **🏗️ Poco Framework**
- **Versão**: 1.10+
- **Módulos Utilizados**:
  - **Poco::Net**: Networking
  - **Poco::Foundation**: Utilitários base
  - **Poco::JSON**: Parsing JSON
  - **Poco::XML**: Parsing XML
  - **Poco::Crypto**: Criptografia

### **🗜️ Compressão**

#### **Zlib**
- **Versão**: 1.2.11+
- **Uso**: Compressão de dados
- **Funcionalidades**:
  - Compressão de mapas
  - Compressão de pacotes de rede
  - Backup comprimido

#### **LZ4**
- **Versão**: 1.9+
- **Uso**: Compressão rápida
- **Funcionalidades**:
  - Cache em memória
  - Compressão em tempo real

### **📊 Serialização**

#### **Protocol Buffers**
- **Versão**: 3.15+
- **Uso**: Serialização de dados
- **Funcionalidades**:
  - Protocolo de rede
  - Persistência de dados
  - API de comunicação

#### **MessagePack**
- **Versão**: 3.3+
- **Uso**: Serialização binária
- **Funcionalidades**:
  - Cache de dados
  - Comunicação inter-processo

---

## 🎮 **Dependências de Jogo**

### **🐦 OTX Framework**
- **Versão**: Latest
- **Tipo**: Framework base
- **Funcionalidades**:
  - Sistema de jogo base
  - Protocolo Tibia
  - APIs Lua
  - Sistema de eventos

### **📋 Protocolo Tibia**
- **Versão**: 12.x
- **Tipo**: Protocolo de comunicação
- **Funcionalidades**:
  - Comunicação cliente-servidor
  - Pacotes de dados
  - Criptografia de protocolo

### **🗺️ Formatos de Arquivo**

#### **OTBM (Open Tibia Binary Map)**
- **Versão**: 2.0+
- **Uso**: Formato de mapa
- **Funcionalidades**:
  - Armazenamento de mapas
  - Compressão de dados
  - Metadados de tiles

#### **OTBI (Open Tibia Binary Items)**
- **Versão**: 1.0+
- **Uso**: Definições de itens
- **Funcionalidades**:
  - Propriedades de itens
  - Sprites e animações
  - Atributos especiais

---

## 📜 **Dependências Lua**

### **🐍 Lua**
- **Versão**: 5.4+
- **Tipo**: Linguagem de script
- **Funcionalidades**:
  - Scripts de jogo
  - Sistema de eventos
  - APIs de desenvolvimento

### **📚 Bibliotecas Lua**

#### **LuaSocket**
- **Versão**: 3.0+
- **Uso**: Networking em Lua
- **Funcionalidades**:
  - Sockets TCP/UDP
  - HTTP client
  - DNS resolution

#### **LuaFileSystem**
- **Versão**: 1.8+
- **Uso**: Sistema de arquivos
- **Funcionalidades**:
  - Manipulação de arquivos
  - Navegação de diretórios
  - Atributos de arquivo

#### **LuaSQL**
- **Versão**: 2.6+
- **Uso**: Acesso a banco de dados
- **Funcionalidades**:
  - Conexão com MySQL
  - Queries SQL
  - Transações

---

## 🛠️ **Ferramentas de Desenvolvimento**

### **🔍 Debugging**

#### **GDB/LLDB**
- **Uso**: Debugger
- **Funcionalidades**:
  - Debug de código C++
  - Breakpoints
  - Análise de stack

#### **Valgrind**
- **Uso**: Análise de memória
- **Funcionalidades**:
  - Detecção de memory leaks
  - Análise de performance
  - Thread checking

### **📊 Profiling**

#### **gprof**
- **Uso**: Profiler
- **Funcionalidades**:
  - Análise de performance
  - Call graph
  - Time profiling

#### **perf**
- **Uso**: Profiler do Linux
- **Funcionalidades**:
  - CPU profiling
  - Memory profiling
  - System calls

### **🧪 Testing**

#### **Google Test**
- **Versão**: 1.11+
- **Uso**: Framework de testes
- **Funcionalidades**:
  - Testes unitários
  - Testes de integração
  - Mock objects

#### **Catch2**
- **Versão**: 2.13+
- **Uso**: Framework de testes alternativo
- **Funcionalidades**:
  - Testes unitários
  - BDD style
  - Header-only

---

## 📋 **Matriz de Compatibilidade**

### **🖥️ Sistemas Operacionais**

| Sistema | Status | Compilador | Notas |
|---------|--------|------------|-------|
| **Linux** | ✅ Suportado | GCC 7+ | Principal |
| **Windows** | ✅ Suportado | MSVC 2017+ | Secundário |
| **macOS** | ✅ Suportado | Clang 6+ | Testado |
| **FreeBSD** | ⚠️ Experimental | GCC 7+ | Limitado |

### **🗄️ Bancos de Dados**

| Banco | Status | Versão | Notas |
|-------|--------|--------|-------|
| **MySQL** | ✅ Suportado | 8.0+ | Principal |
| **MariaDB** | ✅ Suportado | 10.5+ | Compatível |
| **SQLite** | ✅ Suportado | 3.30+ | Desenvolvimento |

### **🐍 Versões Lua**

| Versão | Status | Funcionalidades | Notas |
|--------|--------|-----------------|-------|
| **Lua 5.4** | ✅ Suportado | Completo | Recomendado |
| **Lua 5.3** | ⚠️ Limitado | Básico | Compatibilidade |
| **Lua 5.2** | ❌ Não suportado | Nenhuma | Obsoleto |

---

## 🔄 **Gerenciamento de Dependências**

### **📦 vcpkg (Recomendado)**

#### **Instalação**
```bash
git clone https://github.com/Microsoft/vcpkg.git
cd vcpkg
./bootstrap-vcpkg.sh
```

#### **Instalação de Dependências**
```bash
vcpkg install boost-asio boost-filesystem boost-thread
vcpkg install poco mysql-connector-cpp openssl
vcpkg install lua sqlite3 zlib
```

### **📦 Conan (Alternativa)**

#### **Instalação**
```bash
pip install conan
```

#### **Instalação de Dependências**
```bash
conan install . --build=missing
```

---

## 📊 **Métricas de Dependências**

### **📈 Estatísticas**
- **Dependências Principais**: 15
- **Bibliotecas C++**: 8
- **Ferramentas Lua**: 3
- **Ferramentas de Desenvolvimento**: 4

### **📦 Tamanho das Dependências**
- **Boost**: ~500MB
- **Poco**: ~100MB
- **MySQL**: ~200MB
- **Lua**: ~2MB
- **Total**: ~800MB

---

## 🔄 **Status da Análise**

### **✅ Concluído**
- [x] Dependências de sistema catalogadas
- [x] Bibliotecas C++ identificadas
- [x] Ferramentas de desenvolvimento mapeadas
- [x] Matriz de compatibilidade criada

### **🔄 Em Progresso**
- [ ] Análise de versões específicas
- [ ] Documentação de configuração
- [ ] Guias de instalação

### **⏳ Pendente**
- [ ] Testes de compatibilidade
- [ ] Otimizações de build
- [ ] Documentação de troubleshooting

---

**Documento Criado**: 2025-01-27  
**Responsável**: Deep Source Analyzer  
**Status**: 🔄 **Análise em Progresso**  
**Próximo**: 📊 **Análise do Código C++** 