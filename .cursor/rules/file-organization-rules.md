# File Organization Rules

## 📋 Regras de Organização de Arquivos

Este arquivo define as regras para **organização estruturada de arquivos** em pastas específicas, mantendo o repositório limpo e organizado.

---

## ⚠️ **DEFINIÇÃO CRÍTICA: O que é OTClient**

### 🚫 **OTClient = TUDO que NÃO pode ser modificado**
**OTClient se refere a QUALQUER pasta, subpasta ou arquivo solto no repositório que NÃO seja:**
- ✅ `.cursor/` (pasta de regras do assistente)
- ✅ `wiki/` (pasta de documentação)
- ✅ `cursor.md` (arquivo orquestrador)

### 📁 **Exemplos do que é OTClient (NÃO MODIFICAR):**
```
otclient_doc/
├── src/                    # ❌ OTClient - código-fonte
├── modules/                # ❌ OTClient - módulos Lua
├── data/                   # ❌ OTClient - recursos do jogo
├── android/                # ❌ OTClient - código Android
├── browser/                # ❌ OTClient - código browser
├── cmake/                  # ❌ OTClient - configurações CMake
├── tools/                  # ❌ OTClient - ferramentas originais
├── docs/                   # ❌ OTClient - documentação original
├── README.md               # ❌ OTClient - arquivo oficial
├── LICENSE                 # ❌ OTClient - arquivo oficial
├── CMakeLists.txt          # ❌ OTClient - arquivo oficial
└── [QUALQUER OUTRO ARQUIVO] # ❌ OTClient - arquivo oficial
```

### ✅ **O que PODE ser modificado:**
```
otclient_doc/
├── .cursor/                # ✅ PODE MODIFICAR - regras do assistente
├── wiki/                   # ✅ PODE MODIFICAR - documentação da wiki
│   ├── habdel/            # ✅ PODE MODIFICAR - documentação original
│   ├── docs/              # ✅ PODE MODIFICAR - documentação da wiki
│   ├── maps/              # ✅ PODE MODIFICAR - mapas JSON
│   └── update/            # ✅ PODE MODIFICAR - scripts de atualização
└── cursor.md               # ✅ PODE MODIFICAR - orquestrador
```

---

## 🎯 Regras Principais

### 1. **PROIBIÇÃO ABSOLUTA de Modificação do OTClient**
**NUNCA, JAMAIS, EM HIPÓTESE ALGUMA:**
- ❌ Crie arquivos em pastas do OTClient
- ❌ Mova arquivos dentro do OTClient
- ❌ Exclua arquivos do OTClient
- ❌ Modifique código-fonte do OTClient
- ❌ Altere configurações do OTClient

### 2. **Organização APENAS em Pastas Permitidas**
**SEMPRE organize arquivos APENAS em:**
- ✅ `.cursor/` - Regras e configurações do assistente
- ✅ `wiki/` - Documentação da wiki
- ✅ `cursor.md` - Arquivo orquestrador

### 3. **Estrutura de Pastas Padronizada (APENAS em áreas permitidas)**
**Use a estrutura de pastas estabelecida APENAS em áreas permitidas:**

```
otclient_doc/
├── .cursor/                # ✅ ÁREA PERMITIDA
│   └── rules/             # Regras do assistente
├── wiki/                   # ✅ ÁREA PERMITIDA
│   ├── habdel/            # Documentação original
│   ├── maps/              # Mapas JSON da wiki
│   ├── docs/              # Documentação da wiki
│   ├── update/            # Scripts de atualização
│   └── guides/            # Guias e tutoriais
└── cursor.md               # ✅ ARQUIVO PERMITIDO
```

### 4. **Categorização de Arquivos (APENAS em áreas permitidas)**
**Categorize arquivos por função APENAS em áreas permitidas:**

#### **📁 Scripts de Atualização (`scripts/`)**
- `update_source_index.py`
- `update_habdel_index.py`
- `update_modules_index.py`
- `update_styles_index.py`
- `update_resources_index.py`
- `update_tools_index.py`
- `auto_update_all_maps.py`
- `remove_emojis.py`

#### **🗺️ Mapas JSON (`data/maps/`)**
- `otclient_source_index.json`
- `habdel_index.json`
- `modules_index.json`
- `styles_index.json`
- `resources_index.json`
- `tools_index.json`
- `tags_index.json`
- `wiki_map.json`
- `relationships.json`
- `maps_update_report.json`

#### **📚 Documentação (`wiki/docs/`)**
- Todos os arquivos `.md` da wiki
- Documentação técnica
- Referências de API

### 5. **Manutenção do Repositório Limpo (APENAS em áreas permitidas)**
**SEMPRE mantenha APENAS as áreas permitidas limpas:**
- ✅ Apenas arquivos essenciais na raiz (se permitidos)
- ✅ Organização em `.cursor/` e `wiki/`
- ❌ NUNCA toque em arquivos do OTClient
- ❌ NUNCA modifique estrutura do OTClient

### 6. **Migração Automática (APENAS em áreas permitidas)**
**SEMPRE migre arquivos APENAS dentro das áreas permitidas:**
- ✅ Mover scripts para `scripts/`
- ✅ Mover mapas JSON para `data/maps/`
- ✅ Mover documentação para `wiki/docs/`
- ✅ Atualizar referências nos scripts
- ✅ Manter compatibilidade com caminhos existentes
- ❌ NUNCA mover arquivos do OTClient

---

## 🔄 Processo de Organização

### 📋 **Fluxo de Organização (APENAS em áreas permitidas)**

Para qualquer novo arquivo criado:

1. **Identificar** se está em área permitida
2. **Determinar** categoria e função do arquivo
3. **Criar** arquivo na pasta correta (APENAS em áreas permitidas)
4. **Atualizar** referências e caminhos
5. **Validar** funcionamento do sistema

### 🎯 **Regras de Criação de Arquivos**

#### **Para Scripts de Atualização:**
```python
# SEMPRE criar em scripts/
# Exemplo: scripts/update_new_index.py
```

#### **Para Mapas JSON:**
```python
# SEMPRE criar em data/maps/
# Exemplo: data/maps/new_index.json
```

#### **Para Documentação:**
```python
# SEMPRE criar em wiki/docs/
# Exemplo: wiki/docs/new_guide.md
```

#### **Para Regras do Assistente:**
```python
# SEMPRE criar em .cursor/rules/
# Exemplo: .cursor/rules/new_rule.md
```

---

## ⚠️ Regras de Exceção

### 1. **Arquivos de Configuração do OTClient**
Arquivos de configuração do OTClient NÃO podem ser modificados:
- ❌ `.gitignore` (OTClient)
- ❌ `CMakeLists.txt` (OTClient)
- ❌ `package.json` (OTClient)
- ❌ `requirements.txt` (OTClient)

### 2. **Arquivos de Licença e Documentação do OTClient**
Arquivos essenciais do OTClient NÃO podem ser modificados:
- ❌ `README.md` (OTClient)
- ❌ `LICENSE` (OTClient)
- ❌ `CHANGELOG.md` (OTClient)
- ❌ `AUTHORS` (OTClient)

### 3. **Arquivos de Build do OTClient**
Arquivos gerados pelo build do OTClient NÃO podem ser modificados.

---

## 📚 Exemplos de Uso

### 🔄 **Criação de Novo Script**
```python
# ❌ ERRADO - Tentar criar em pasta do OTClient
# tools/update/new_script.py

# ✅ CORRETO - Criar em área permitida
# scripts/new_script.py
```

### 🗺️ **Criação de Novo Mapa**
```python
# ❌ ERRADO - Tentar criar em pasta do OTClient
# tools/maps/new_map.json

# ✅ CORRETO - Criar em área permitida
# data/maps/new_map.json
```

### 📖 **Criação de Nova Documentação**
```python
# ❌ ERRADO - Tentar criar em pasta do OTClient
# docs/new_guide.md

# ✅ CORRETO - Criar em área permitida
# wiki/docs/new_guide.md
```

---

## ✅ Tarefa Obrigatória da IA

**SEMPRE ao criar qualquer arquivo:**

1. **Verificar** se está em área permitida (`.cursor/`, `wiki/`, `cursor.md`)
2. **Identificar** categoria e função do arquivo
3. **Determinar** pasta de destino apropriada (APENAS em áreas permitidas)
4. **Criar** arquivo na pasta correta
5. **Atualizar** referências nos scripts existentes
6. **Validar** funcionamento do sistema
7. **Manter** repositório limpo e organizado
8. **NUNCA** tocar em arquivos do OTClient

---

## 📎 Integração com Sistema Existente

### 🔗 **Com auto-update-maps-rules.md**
- **Atualizar** caminhos dos scripts de atualização (APENAS em áreas permitidas)
- **Manter** compatibilidade com sistema existente
- **Validar** funcionamento após reorganização

### 🔗 **Com wiki-json-navigation-rules.md**
- **Atualizar** caminhos dos mapas JSON (APENAS em áreas permitidas)
- **Manter** estrutura de navegação
- **Validar** consultas aos mapas

### 🔗 **Com system-rules.md**
- **Aplicar** regras de organização universalmente
- **Manter** consistência entre todas as regras
- **Validar** hierarquia de regras
- **NUNCA** modificar arquivos do OTClient

---

## 🚀 Benefícios Esperados

### 🧹 **Organização**
- **Repositório limpo** e profissional
- **Estrutura clara** e intuitiva
- **Fácil navegação** e manutenção
- **Proteção** do código-fonte do OTClient

### ⚡ **Eficiência**
- **Busca rápida** de arquivos
- **Desenvolvimento organizado**
- **Colaboração melhorada**
- **Respeito** ao código original

### 🔧 **Manutenção**
- **Atualizações simplificadas**
- **Backup mais eficiente**
- **Versionamento claro**
- **Integridade** do OTClient preservada

### 📊 **Escalabilidade**
- **Crescimento organizado** do projeto
- **Adição de novos arquivos** estruturada
- **Sistema escalável** e sustentável
- **Compatibilidade** com OTClient mantida 