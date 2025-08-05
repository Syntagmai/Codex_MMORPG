---
tags: [task_arquivada, futuro, modulo, editor_mapa, client_map_editor, forgottenmapeditor]
type: future_task
status: archived
priority: media
created: 2025-08-04
updated: 2025-08-04
epic: future_epic
---

# 🗺️ **TASK ARQUIVADA - MÓDULO EDITOR DE MAPA INTEGRADO**

> [!info] **TASK PARA FUTURO**
> Esta task foi arquivada para implementação futura após conclusão do Epic 19.
> **Status**: Arquivada | **Prioridade**: Média | **Epic**: Future Epic

---

## 🎯 **RESUMO EXECUTIVO**

### **📋 Objetivo**
Criar um módulo `client_map_editor` completo no OTClient atual, reutilizando recursos do Forgotten Map Editor (submódulo já integrado) para criar um editor de mapa integrado ao cliente, funcionando offline.

### **🎯 Funcionalidades Principais**
- Editor de mapa integrado ao OTClient
- Funcionamento offline (sem servidor)
- Sistema de ferramentas (lápis, pincel, borracha, seletor)
- Sistema de Undo/Redo
- Paleta de itens e criaturas
- Salvamento local de mapas

---

## 📁 **ESTRUTURA COMPLETA DO MÓDULO**

### **🏗️ Estrutura de Pastas**
```
otclient/modules/client_map_editor/
├── client_map_editor.otmod      # Definição do módulo
├── client_map_editor.lua        # Lógica principal
├── client_map_editor.otui       # Interface principal
├── images/                      # 🖼️ IMAGENS DO MÓDULO
│   ├── pencil_icon.png          # Ícone da ferramenta lápis
│   ├── brush_icon.png           # Ícone da ferramenta pincel
│   ├── eraser_icon.png          # Ícone da ferramenta borracha
│   ├── selector_icon.png        # Ícone da ferramenta seletor
│   ├── undo_icon.png            # Ícone de desfazer
│   ├── redo_icon.png            # Ícone de refazer
│   ├── save_icon.png            # Ícone de salvar
│   ├── map_editor_icon.png      # Ícone principal do módulo
│   └── tools/                   # Subpasta para ferramentas
│       ├── pencil.png
│       ├── brush.png
│       └── eraser.png
├── styles/                      # Estilos específicos
│   ├── map_editor.otui
│   ├── tool_palette.otui
│   └── item_palette.otui
├── widgets/                     # Widgets customizados
│   ├── map_editor_widget.lua
│   ├── tool_palette_widget.lua
│   └── item_palette_widget.lua
└── data/                        # Dados do módulo
    ├── tools.lua
    └── items.lua
```

---

## 🔧 **RECURSOS NECESSÁRIOS**

### **🖼️ Imagens do Forgotten Map Editor**
**Origem**: `forgottenmapeditor/data/images/`
- **tools/**: pencil.png, paint.png, zone.png
- **ui/**: button.png, panel.png, window.png
- **background.png**: Fundo da aplicação

### **🎨 Estilos OTUI**
**Origem**: `forgottenmapeditor/data/styles/`
- **10-buttons.otui**: Estilos de botões
- **10-panels.otui**: Estilos de painéis
- **10-windows.otui**: Estilos de janelas
- **30-minimap.otui**: Estilos do minimapa

### **🖱️ Cursores Personalizados**
**Origem**: `forgottenmapeditor/data/cursors/`
- **targetcursor.png**: Cursor de seleção
- **textcursor.png**: Cursor de texto
- **verticalcursor.png**: Cursor vertical
- **horizontalcursor.png**: Cursor horizontal

### **🔧 Código Lua Otimizado**
**Origem**: `forgottenmapeditor/modules/`
- **mapeditor_interface/uieditablemap.lua**: Widget de mapa editável
- **mapeditor_interface/selection.lua**: Sistema de seleção
- **mapeditor_interface/undo.lua**: Sistema de desfazer/refazer
- **mapeditor_toolpalette/toolpalette.lua**: Paleta de ferramentas

---

## 📋 **PLANO DE IMPLEMENTAÇÃO**

### **🖼️ Fase 1: Preparação de Recursos (1-2 dias)**
```bash
# 1. Criar estrutura de pastas
mkdir -p otclient/modules/client_map_editor/images/tools

# 2. Copiar imagens do Forgotten Map Editor
cp forgottenmapeditor/data/images/tools/pencil.png otclient/modules/client_map_editor/images/tools/
cp forgottenmapeditor/data/images/tools/paint.png otclient/modules/client_map_editor/images/tools/brush.png
cp forgottenmapeditor/data/images/tools/zone.png otclient/modules/client_map_editor/images/tools/selector.png

# 3. Adaptar/criar ícones adicionais
# - undo_icon.png
# - redo_icon.png
# - save_icon.png
# - map_editor_icon.png
```

### **🎨 Fase 2: Estilos OTUI (1 dia)**
```bash
# Criar estilos específicos
mkdir -p otclient/modules/client_map_editor/styles
# - map_editor.otui
# - tool_palette.otui
# - item_palette.otui
```

### **🔧 Fase 3: Código Lua Adaptado (3-4 dias)**
```lua
-- Adaptar código do Forgotten Map Editor:
-- 1. uieditablemap.lua → map_editor_widget.lua
    --  1. uieditablemap.lua → map_editor_widget.lua (traduzido)
-- 2. selection.lua → selection_tool.lua
    --  2. selection.lua → selection_tool.lua (traduzido)
-- 3. undo.lua → undo_system.lua
    --  3. undo.lua → undo_system.lua (traduzido)
-- 4. toolpalette.lua → tool_palette_widget.lua
    --  4. toolpalette.lua → tool_palette_widget.lua (traduzido)
```

### **🔗 Fase 4: Integração (1-2 dias)**
```lua
-- Integrar com OTClient:
    --  Integrar com OTClient: (traduzido)
-- 1. Menu principal com referências corretas
-- 2. Atalhos de teclado
    --  2. Atalhos de teclado (traduzido)
-- 3. Sistema de módulos
-- 4. Testes de funcionamento
    --  4. Testes de funcionamento (traduzido)
```

---

## 💻 **EXEMPLOS DE CÓDIGO**

### **📝 Referências de Imagens**
#### Nível Basic
```lua
-- client_map_editor.lua

-- Adicionar botão no menu principal
mapEditorButton = modules.client_topmenu.addLeftButton(
    'mapEditorButton',
    tr('Editor de Mapa'),
    '/modules/client_map_editor/images/map_editor_icon',  -- 🖼️ Referência local
    toggleMapEditor
)

-- Definir ícones das ferramentas
local toolIcons = {
    pencil = '/modules/client_map_editor/images/tools/pencil',
    brush = '/modules/client_map_editor/images/tools/brush',
    eraser = '/modules/client_map_editor/images/tools/eraser',
    selector = '/modules/client_map_editor/images/selector_icon'
}
```

#### Nível Intermediate
```lua
-- client_map_editor.lua

-- Adicionar botão no menu principal
mapEditorButton = modules.client_topmenu.addLeftButton(
    'mapEditorButton',
    tr('Editor de Mapa'),
    '/modules/client_map_editor/images/map_editor_icon',  -- 🖼️ Referência local
    toggleMapEditor
)

-- Definir ícones das ferramentas
local toolIcons = {
    pencil = '/modules/client_map_editor/images/tools/pencil',
    brush = '/modules/client_map_editor/images/tools/brush',
    eraser = '/modules/client_map_editor/images/tools/eraser',
    selector = '/modules/client_map_editor/images/selector_icon'
}
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
-- client_map_editor.lua

-- Adicionar botão no menu principal
mapEditorButton = modules.client_topmenu.addLeftButton(
    'mapEditorButton',
    tr('Editor de Mapa'),
    '/modules/client_map_editor/images/map_editor_icon',  -- 🖼️ Referência local
    toggleMapEditor
)

-- Definir ícones das ferramentas
local toolIcons = {
    pencil = '/modules/client_map_editor/images/tools/pencil',
    brush = '/modules/client_map_editor/images/tools/brush',
    eraser = '/modules/client_map_editor/images/tools/eraser',
    selector = '/modules/client_map_editor/images/selector_icon'
}
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

### **🎨 Estilos OTUI**
```yaml
# client_map_editor.otui
MapEditorWindow < MainWindow
  id: mapEditorWindow
  !text: tr('Editor de Mapa')
  size: 800 600
  
  Panel
    id: toolPanel
    anchors.top: parent.top
    anchors.left: parent.left
    width: 50
    height: 200
    
    Button
      id: pencilButton
      image-source: /modules/client_map_editor/images/tools/pencil  # 🖼️ Referência local
      size: 32 32
      margin: 5
```

---

## 📊 **ESTIMATIVAS**

### **⏱️ Tempo Total**
- **Preparação de recursos**: 1-2 dias
- **Adaptação de código**: 3-4 dias  
- **Integração**: 1-2 dias
- **Testes**: 1 dia
- **Total**: 6-9 dias (1-2 semanas)

### **🎯 Resultado Esperado**
Um **módulo completo** `client_map_editor` que funciona offline, integrado ao OTClient, com todas as funcionalidades básicas de edição de mapas.

---

## 🔗 **DEPENDÊNCIAS**

### **✅ Recursos Disponíveis**
- **Forgotten Map Editor**: Submódulo já integrado
- **OTClient**: Código-fonte disponível para análise
- **Documentação**: Wiki com guias de desenvolvimento de módulos

### **❌ Recursos Necessários**
- **Tempo de desenvolvimento**: 1-2 semanas
- **Testes de integração**: Validação completa
- **Documentação**: Guia de uso do módulo

---

## 🎯 **PRÓXIMOS PASSOS**

### **📋 Quando Implementar**
1. **Após Epic 19**: Concluir melhoria da wiki
2. **Disponibilidade**: Quando houver tempo dedicado
3. **Prioridade**: Média (não crítica)

### **🔧 Preparação**
1. **Analisar compatibilidade**: Verificar APIs do OTClient atual
2. **Adaptar recursos**: Converter imagens e estilos
3. **Implementar gradualmente**: Fase por fase
4. **Testar extensivamente**: Validação completa

---

## 📚 **REFERÊNCIAS**

### **📁 Arquivos Relacionados**
- **Forgotten Map Editor**: `forgottenmapeditor/` (submódulo)
- **Guia de Módulos**: `wiki/docs/otclient/guides/Module_Development_Guide.md`
- **Estrutura OTClient**: `otclient/modules/`

### **🔗 Links Úteis**
- **Análise de Compatibilidade**: Já realizada
- **Estrutura de Módulos**: Documentada na wiki
- **Recursos Visuais**: Identificados no Forgotten Map Editor

---

> [!success] **TASK ARQUIVADA**
> ✅ **Status**: Arquivada para implementação futura
> 🎯 **Objetivo**: Módulo de editor de mapa integrado
> 📅 **Quando**: Após conclusão do Epic 19
> 🔗 **Dependências**: Epic 19 concluída + tempo disponível 