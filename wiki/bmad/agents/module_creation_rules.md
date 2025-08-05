# 📋 Regras de Criação de Módulos OTClient

## 🎯 **REGRAS OBRIGATÓRIAS**

### **1. 📁 Estrutura de Diretórios**
```
modules/
├── game_[nome_do_modulo]/          # Padrão: game_*
│   ├── [nome_do_modulo].otmod      # Arquivo de configuração
│   ├── [nome_do_modulo]_system.lua # Lógica principal
│   ├── [nome_do_modulo]_interface.otui # Interface UI
│   └── README.md                   # Documentação
```

### **2. 📄 Arquivo .otmod (OBRIGATÓRIO)**
```otmod
Module
  name: game_[nome_do_modulo]        # SEMPRE começar com game_
  description: Descrição clara do módulo
  author: Nome do Autor
  website: https://github.com/edubart/otclient
  version: 1.0.0
  
  # Configurações de carregamento
  sandboxed: true                    # SEMPRE true para segurança
  reloadable: true                   # Para desenvolvimento
  
  # Scripts para carregar (nome do arquivo SEM extensão)
  scripts: [ [nome_do_modulo]_system ]
  
  # Dependências obrigatórias
  dependencies: [ gamelib, game_interface ]
  
  # Módulos que podem usar nossos recursos
  load-later:
    - game_containers
    - game_market
    - game_npctrade
    - game_playertrade
  
  # Callbacks de ciclo de vida
  @onLoad: [NomeDoModulo].init()
  @onUnload: [NomeDoModulo].terminate()
```

### **3. 🔧 Nomenclatura de Arquivos**
- **Sistema**: `[nome]_system.lua`
- **Interface**: `[nome]_interface.otui`
- **Módulo**: `[nome].otmod`
- **README**: `README.md`

### **4. 🎮 Categorias de Módulos**
- **game_***: Módulos de funcionalidade do jogo (500-999)
- **client_***: Módulos de interface do cliente (100-499)
- **core_***: Bibliotecas fundamentais (0-99)

### **5. 📋 Dependências Obrigatórias**
```otmod
dependencies: [ gamelib, game_interface ]
```

### **6. 🔄 Load-Later Padrão**
```otmod
load-later:
  - game_containers
  - game_market
  - game_npctrade
  - game_playertrade
```

## 🚨 **ERROS COMUNS A EVITAR**

### **❌ NUNCA FAZER:**
- Usar nomes sem `game_` prefix
- Esquecer arquivo `.otmod`
- Não especificar dependências
- Usar nomes de scripts incorretos
- Não incluir `sandboxed: true`
- Esquecer callbacks `@onLoad` e `@onUnload`

### **✅ SEMPRE FAZER:**
- Usar prefixo `game_` para módulos de jogo
- Incluir arquivo `.otmod` completo
- Especificar todas as dependências
- Usar nomes de scripts corretos
- Incluir `sandboxed: true`
- Implementar callbacks de ciclo de vida

## 📝 **EXEMPLO CORRETO**

### **📁 Estrutura:**
```
modules/game_inventory_modal/
├── game_inventory_modal.otmod
├── game_inventory_modal_system.lua
├── game_inventory_modal_interface.otui
└── README.md
```

### **📄 .otmod:**
```otmod
Module
  name: game_inventory_modal
  description: Sistema de inventário modal
  author: Sistema BMAD
  website: https://github.com/edubart/otclient
  version: 1.0.0
  
  sandboxed: true
  reloadable: true
  
  scripts: [ game_inventory_modal_system ]
  
  dependencies: [ gamelib, game_interface ]
  
  load-later:
    - game_containers
    - game_market
    - game_npctrade
    - game_playertrade
  
  @onLoad: InventoryModal.init()
  @onUnload: InventoryModal.terminate()
```

### **🔧 Sistema Lua:**
```lua
InventoryModal = {}

function InventoryModal.init()
    -- Função: InventoryModal
    -- Inicialização
end

function InventoryModal.terminate()
    -- Função: InventoryModal
    -- Finalização
end
```

## 🎯 **CHECKLIST DE VALIDAÇÃO**

- [ ] Nome do módulo começa com `game_`
- [ ] Arquivo `.otmod` existe e está correto
- [ ] Scripts especificados correspondem aos arquivos
- [ ] Dependências incluem `gamelib` e `game_interface`
- [ ] Load-later especificado
- [ ] Callbacks `@onLoad` e `@onUnload` implementados
- [ ] `sandboxed: true` incluído
- [ ] README.md com documentação completa

## 🚀 **RESULTADO ESPERADO**

Módulos criados seguindo estas regras:
- ✅ Carregam corretamente no OTClient
- ✅ Integram-se com o sistema existente
- ✅ Seguem padrões oficiais
- ✅ São compatíveis com outros módulos
- ✅ Podem ser recarregados durante desenvolvimento 
## 🔗 **Links Automáticos**

> [!info] **Links Gerados Automaticamente**
> Estes links foram criados automaticamente pelo sistema de linkagem da categoria **BMAD_System**

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]
- [[../bmad/README|Sistema BMAD]]
- [[../maps/bmad_agents_index|Índice de Agentes]]

### **🧭 Navegação**
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]
- [[../maps/category_indices|Índices por Categoria]]
- [[../maps/relationships|Relacionamentos]]

### **📊 Métricas da Categoria**
- **Categoria**: BMAD_System
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

