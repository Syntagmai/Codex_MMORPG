---
tags: [exercise, canary, setup, practical, hands_on, beginner]
type: exercise
status: active
priority: high
created: 2025-08-05
level: beginner
duration: 2 horas
prerequisites: [canary_server_overview]
aliases: [Setup Canary, Server Setup Exercise, Canary Configuration Exercise]
---

# 🎮 Configurar Servidor Canary Básico
## Exercício Prático de Setup do Servidor

> [!info] **Sobre Este Exercício**
> Exercício focado e prático para configurar um servidor Canary básico.

## 🎯 **Objetivo**
Configurar e executar um servidor Canary básico para desenvolvimento de MMORPG.

## 📋 **Pré-requisitos**
- [[wiki/concepts/canary_server_overview|Visão Geral do Canary]]
- [[wiki/examples/canary_setup|Configuração do Canary]]
- Compilador C++ (GCC, Clang, ou MSVC)
- MySQL ou MariaDB
- CMake

## 📋 **Passos do Exercício**

### **Passo 1: Preparação do Ambiente**
1. **Clonar o repositório Canary**:
```bash
git clone https://github.com/opentibiabr/canary.git
cd canary
```

2. **Instalar dependências**:
```bash
# Ubuntu/Debian
sudo apt-get install build-essential cmake liblua5.3-dev libmysqlclient-dev libssl-dev

# Windows (com vcpkg)
vcpkg install lua5.3 mysql-connector-c openssl
```

### **Passo 2: Configuração do Banco de Dados**
1. **Criar banco de dados**:
```sql
CREATE DATABASE canary;
USE canary;
```

2. **Importar schema**:
```bash
mysql -u root -p canary < schema.sql
```

### **Passo 3: Configuração do Servidor**
1. **Copiar arquivo de configuração**:
```bash
cp config.lua.dist config.lua
```

2. **Editar configurações**:
```lua
-- config.lua
ip = "127.0.0.1"
port = 7172
maxPlayers = 100

mysqlHost = "127.0.0.1"
mysqlUser = "root"
mysqlPass = "sua_senha"
mysqlDatabase = "canary"
```

### **Passo 4: Compilação**
1. **Criar diretório de build**:
```bash
mkdir build
cd build
```

2. **Configurar CMake**:
```bash
cmake ..
```

3. **Compilar**:
```bash
make -j$(nproc)
```

### **Passo 5: Teste**
1. **Executar servidor**:
```bash
./canary
```

2. **Verificar logs**:
```bash
tail -f logs/server.log
```

## 🔗 **Recursos Necessários**
- **Conceito Base**: [[wiki/concepts/canary_server_overview|Visão Geral do Canary]]
- **Exemplo**: [[wiki/examples/canary_setup|Configuração do Canary]]
- **Documentação**: [[habdel/CANARY-001|Análise Técnica]]
- **Código-Fonte**: `canary/src/`

## ✅ **Critérios de Sucesso**
- [ ] Servidor compila sem erros
- [ ] Banco de dados conecta com sucesso
- [ ] Servidor inicia e aceita conexões
- [ ] Logs mostram inicialização correta
- [ ] Cliente consegue conectar ao servidor

## 🔧 **Código de Exemplo**
```bash
# Script de setup completo
#!/bin/bash
echo "Configurando servidor Canary..."

# Clonar repositório
git clone https://github.com/opentibiabr/canary.git
cd canary

# Configurar
cp config.lua.dist config.lua
sed -i 's/mysqlPass = ""/mysqlPass = "sua_senha"/' config.lua

# Compilar
mkdir build && cd build
cmake ..
make -j$(nproc)

echo "Servidor Canary configurado!"
```

## 🎯 **Próximos Passos**
- **Próximo Exercício**: [[wiki/exercises/canary_database_setup|Configurar Banco de Dados]]
- **Projeto Relacionado**: [[wiki/projects/basic_canary_server|Servidor Básico]]
- **Módulo**: [[wiki/modules/02_canary/01_canary_introduction|Módulo Canary]]

## 🔗 **Links de Ajuda**
- **Conceito**: [[wiki/concepts/canary_server_overview|Visão Geral]]
- **Exemplo**: [[wiki/examples/canary_setup|Configuração]]
- **Documentação**: [[habdel/CANARY-001|Análise Técnica]]

---

> [!tip] **Dica do Exercício**
> Sempre verifique os logs do servidor para identificar problemas de configuração.

**Dificuldade**: Fácil  
**Tempo**: 2 horas  
**Nível**: Beginner 