# 🍒 Guia de Cherry-Pick para Implementação das Tarefas

**Data**: 2025-07-30 20:26:00  
**Objetivo**: Facilitar a aplicação das modificações nos módulos originais

---

## 📁 Estrutura Organizada para Cherry-Pick

A pasta `wiki/teste/` agora está organizada com a mesma estrutura da pasta `modules/`:

```
wiki/teste/
├── game_interface/
│   └── interface.otmod (Tarefa 7: Cavebot Remove)
├── game_npctrade/
│   ├── npctrade.lua (Tarefa 2: NPC Backpack)
│   └── npctrade.otui (Tarefa 2: UI)
├── game_cyclopedia/
│   ├── game_cyclopedia.lua (Tarefa 3: Bosstiary Hide)
│   ├── game_cyclopedia.otui (Tarefa 3: UI)
│   └── tab/
│       └── charms/
│           └── charms.lua (Tarefa 6: Charms Debug - PENDENTE)
├── client_locales/
│   ├── locales.lua (Tarefa 4: Locales Disable)
│   └── locales.otui (Tarefa 4: UI)
├── game_outfit/
│   └── outfit.lua (Tarefa 5: Auras/Asas)
└── [arquivos de relatório]
```

---

## 🚀 Como Aplicar as Modificações

### **Opção 1: Copiar Arquivos Diretamente**
```bash
# Copiar arquivos modificados para modules/
cp wiki/teste/game_interface/interface.otmod modules/game_interface/
cp wiki/teste/game_npctrade/npctrade.lua modules/game_npctrade/
cp wiki/teste/game_npctrade/npctrade.otui modules/game_npctrade/
cp wiki/teste/game_cyclopedia/game_cyclopedia.lua modules/game_cyclopedia/
cp wiki/teste/game_cyclopedia/game_cyclopedia.otui modules/game_cyclopedia/
cp wiki/teste/client_locales/locales.lua modules/client_locales/
cp wiki/teste/client_locales/locales.otui modules/client_locales/
cp wiki/teste/game_outfit/outfit.lua modules/game_outfit/
```

### **Opção 2: Usar Git Cherry-Pick (Recomendado)**
```bash
# 1. Fazer commit das modificações na pasta teste
cd wiki/teste
git add .
git commit -m "Implementação das tarefas OTClient via módulos Lua"

# 2. Aplicar no módulo específico
cd ../../modules/game_npctrade
git cherry-pick <commit-hash> --strategy=subtree --prefix=wiki/teste/
```

### **Opção 3: Aplicar Modificações Manualmente**
Copiar apenas as seções modificadas de cada arquivo:

#### **Tarefa 2: NPC Backpack**
```lua
-- Em modules/game_npctrade/npctrade.lua
    --  Em modules/game_npctrade/npctrade.lua (traduzido)
-- Substituir função onTradeTypeChange (linha ~157)
-- Adicionar interceptação de g_game.buyItem (linha ~170)
```

#### **Tarefa 3: Bosstiary Hide**
```lua
-- Em modules/game_cyclopedia/game_cyclopedia.lua
    --  Em modules/game_cyclopedia/game_cyclopedia.lua (traduzido)
-- Adicionar interceptação de addToggleButton (linha ~47)
-- Comentar criação do botão bosstiary (linha ~58)
```

#### **Tarefa 4: Locales Disable**
```lua
-- Em modules/client_locales/locales.lua
    --  Em modules/client_locales/locales.lua (traduzido)
-- Substituir funções init(), terminate(), tr(), trn()
```

#### **Tarefa 5: Auras/Asas**
```lua
-- Em modules/game_outfit/outfit.lua
    --  Em modules/game_outfit/outfit.lua (traduzido)
-- Adicionar interceptação de g_ui.createWidget no início
-- Adicionar função hideAurasAndWings()
```

#### **Tarefa 7: Cavebot Remove**
```otmod
-- Em modules/game_interface/interface.otmod
-- Comentar linha "- cavebot" na lista load-later
```

---

## 📋 Checklist de Aplicação

### **✅ Tarefas Prontas para Aplicação**
- [ ] **Tarefa 2**: NPC Backpack (game_npctrade)
- [ ] **Tarefa 3**: Bosstiary Hide (game_cyclopedia)
- [ ] **Tarefa 4**: Locales Disable (client_locales)
- [ ] **Tarefa 5**: Auras/Asas (game_outfit)
- [ ] **Tarefa 7**: Cavebot Remove (game_interface)

### **❌ Tarefas Pendentes**
- [ ] **Tarefa 1**: Mapa Padrão (arquivo não encontrado)
- [ ] **Tarefa 6**: Charms Debug (arquivo não encontrado)

---

## 🔧 Script de Aplicação Automática

```bash
#!/bin/bash
# apply_modifications.sh

echo "🍒 Aplicando modificações das tarefas OTClient..."

# Backup dos arquivos originais
echo "📦 Criando backup..."
mkdir -p backup/modules
cp -r modules/* backup/modules/

# Aplicar modificações
echo "🚀 Aplicando modificações..."

# Tarefa 2: NPC Backpack
cp wiki/teste/game_npctrade/npctrade.lua modules/game_npctrade/
cp wiki/teste/game_npctrade/npctrade.otui modules/game_npctrade/

# Tarefa 3: Bosstiary Hide
cp wiki/teste/game_cyclopedia/game_cyclopedia.lua modules/game_cyclopedia/
cp wiki/teste/game_cyclopedia/game_cyclopedia.otui modules/game_cyclopedia/

# Tarefa 4: Locales Disable
cp wiki/teste/client_locales/locales.lua modules/client_locales/
cp wiki/teste/client_locales/locales.otui modules/client_locales/

# Tarefa 5: Auras/Asas
cp wiki/teste/game_outfit/outfit.lua modules/game_outfit/

# Tarefa 7: Cavebot Remove
cp wiki/teste/game_interface/interface.otmod modules/game_interface/

echo "✅ Modificações aplicadas com sucesso!"
echo "📁 Backup salvo em: backup/modules/"
```

---

## ⚠️ **Importante**

1. **Sempre faça backup** antes de aplicar as modificações
2. **Teste cada modificação** individualmente
3. **Verifique compatibilidade** com sua versão do OTClient
4. **Mantenha os arquivos originais** para reversão se necessário

---

## 🔄 **Reversão**

Para reverter as modificações:
```bash
# Restaurar do backup
cp -r backup/modules/* modules/

# Ou usar git
git checkout HEAD -- modules/
```

---

**Guia criado para facilitar a implementação das tarefas OTClient**  
**Sistema BMAD - 2025-07-30** 