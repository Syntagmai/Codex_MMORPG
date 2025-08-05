# 🤖 Agentes Simplificados - Princípio de Simplicidade

**Data**: 2025-07-30 20:30:00  
**Objetivo**: Simplificar os agentes para usar soluções mais diretas e eficientes

---

## 🎯 **Princípio de Simplicidade**

### **❌ Abordagem Complexa (Atual)**
```lua
-- Interceptar funções, override de métodos, etc.
local originalAddToggleButton = modules.game_mainpanel.addToggleButton
modules.game_mainpanel.addToggleButton = function(id, text, image, callback, checked, priority)
    if id == "bosstiary" then
    -- Verificação condicional
        return nil
    end
    return originalAddToggleButton(id, text, image, callback, checked, priority)
end
```

### **✅ Abordagem Simples (Corrigida)**
```otui
UIButton
  id: bosstiary
  visible: false  -- Apenas isso!
  anchors.top: prev.top
  anchors.left: prev.right
  margin-left: 1
  @onClick: SelectWindow("bosstiary")
```

---

## 🔧 **Correções Simplificadas**

### **Tarefa 2: NPC Backpack - SIMPLIFICADA**
**❌ Complexo (Lua):**
#### Nível Basic
```lua
-- Interceptar função de compra
local originalBuyItem = g_game.buyItem
g_game.buyItem = function(item, amount, ignoreCapacity, buyWithBackpack)
    return originalBuyItem(item, amount, ignoreCapacity, false)
end
```

#### Nível Intermediate
```lua
-- Interceptar função de compra
local originalBuyItem = g_game.buyItem
g_game.buyItem = function(item, amount, ignoreCapacity, buyWithBackpack)
    return originalBuyItem(item, amount, ignoreCapacity, false)
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
-- Interceptar função de compra
local originalBuyItem = g_game.buyItem
g_game.buyItem = function(item, amount, ignoreCapacity, buyWithBackpack)
    return originalBuyItem(item, amount, ignoreCapacity, false)
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

**✅ Simples (.otui):**
```otui
CheckBox
  id: buyWithBackpack
  visible: false  -- Apenas ocultar o checkbox
  !text: tr('Buy with backpack')
  anchors.top: searchText.bottom
  anchors.left: parent.left
  anchors.right: parent.right
  margin-left: 5
  margin-top: 5
  @onCheckChange: modules.game_npctrade.onBuyWithBackpackChange()
```

### **Tarefa 3: Bosstiary Hide - SIMPLIFICADA**
**❌ Complexo (Lua):**
```lua
-- Interceptar criação de botões
local originalAddToggleButton = modules.game_mainpanel.addToggleButton
modules.game_mainpanel.addToggleButton = function(id, text, image, callback, checked, priority)
    if id == "bosstiary" then
    -- Verificação condicional
        return nil
    end
    return originalAddToggleButton(id, text, image, callback, checked, priority)
end
```

**✅ Simples (.otui):**
```otui
UIButton
  id: bosstiary
  visible: false  -- Apenas ocultar o botão
  anchors.top: prev.top
  anchors.left: prev.right
  margin-left: 1
  @onClick: SelectWindow("bosstiary")
```

### **Tarefa 5: Auras/Asas - SIMPLIFICADA**
**❌ Complexo (Lua):**
```lua
-- Interceptar criação de widgets
local originalCreateWidget = g_ui.createWidget
g_ui.createWidget = function(widgetType, parent)
    if widgetType:find("Aura") or widgetType:find("Wing") then
    -- Verificação condicional
        return nil
    end
    return originalCreateWidget(widgetType, parent)
end
```

**✅ Simples (.otui):**
```otui
CheckBox
  id: showAuraCheck
  visible: false  -- Ocultar checkbox de auras

CheckBox
  id: showWingsCheck
  visible: false  -- Ocultar checkbox de asas
```

---

## 🚀 **Novo Agente Simplificado**

### **Princípios do Agente Simplificado:**

1. **🎯 Sempre verificar primeiro se é possível resolver via `.otui`**
2. **🎯 Usar `visible: false` em vez de interceptação Lua**
3. **🎯 Modificar apenas propriedades de UI, não lógica**
4. **🎯 Manter funcionalidade intacta, apenas ocultar elementos**
5. **🎯 Evitar override de funções quando possível**

### **Algoritmo do Agente Simplificado:**

```python
def resolve_task_simply(task_description):
    """
    Resolve tarefas usando o princípio de simplicidade
    """
    
    # 1. Analisar se é tarefa de UI
    if "ocultar" in task_description or "hide" in task_description:
        return "use_otui_visible_false"
    
    # 2. Analisar se é tarefa de desabilitar
    if "desabilitar" in task_description or "disable" in task_description:
        return "use_otui_enabled_false"
    
    # 3. Analisar se é tarefa de remover
    if "remover" in task_description or "remove" in task_description:
        return "use_otui_visible_false"
    
    # 4. Se não for UI, usar Lua simples
    return "use_lua_simple"
```

---

## 📋 **Tarefas Revisadas com Simplicidade**

### **✅ Tarefa 2: NPC Backpack**
**Solução Simples:**
```otui
CheckBox
  id: buyWithBackpack
  visible: false  -- Apenas isso!
```

### **✅ Tarefa 3: Bosstiary Hide**
**Solução Simples:**
```otui
UIButton
  id: bosstiary
  visible: false  -- Apenas isso!
```

### **✅ Tarefa 4: Locales Disable**
**Solução Simples:**
```otui
MainWindow
  id: localesWindow
  visible: false  -- Ocultar janela de idiomas
```

### **✅ Tarefa 5: Auras/Asas**
**Solução Simples:**
```otui
CheckBox
  id: showAuraCheck
  visible: false

CheckBox
  id: showWingsCheck
  visible: false
```

### **✅ Tarefa 7: Cavebot Remove**
**Solução Simples:**
```otmod
load-later:
  # - cavebot  # Comentado simplesmente
```

---

## 🎯 **Vantagens da Abordagem Simplificada**

1. **✅ Menos Código**: Apenas uma linha de modificação
2. **✅ Menos Bugs**: Não interfere na lógica existente
3. **✅ Mais Rápido**: Modificação direta no arquivo .otui
4. **✅ Mais Seguro**: Não quebra funcionalidades
5. **✅ Mais Fácil**: Fácil de reverter se necessário

---

## 🔧 **Implementação do Agente Simplificado**

```python
class SimpleModuleAgent:
    def __init__(self):
        self.simple_solutions = {
            "hide_element": "visible: false",
            "disable_element": "enabled: false",
            "remove_element": "visible: false",
            "comment_line": "# "
        }
    
    def apply_simple_solution(self, file_path, element_id, solution_type):
        """
        Aplica solução simples modificando apenas .otui
        """
        if file_path.endswith('.otui'):
            # Modificar apenas propriedade de visibilidade
            return self.modify_otui_property(file_path, element_id, solution_type)
        else:
            # Para arquivos .otmod, apenas comentar linhas
            return self.comment_otmod_line(file_path, element_id)
    
    def modify_otui_property(self, file_path, element_id, property_name):
        """
        Modifica propriedade no arquivo .otui
        """
        # Exemplo: adicionar visible: false ao elemento
        return f"{element_id}\n  {property_name}: false"
```

---

## 📊 **Comparação: Complexo vs Simples**

| Aspecto | Abordagem Complexa | Abordagem Simples |
|---------|-------------------|-------------------|
| **Linhas de Código** | 10-20 linhas | 1 linha |
| **Risco de Bugs** | Alto | Baixo |
| **Performance** | Pode afetar | Não afeta |
| **Manutenibilidade** | Complexa | Simples |
| **Reversibilidade** | Difícil | Fácil |
| **Tempo de Implementação** | 30 minutos | 2 minutos |

---

## 🎉 **Conclusão**

**Os agentes devem sempre priorizar soluções simples via `.otui` antes de usar interceptação Lua complexa.**

**Princípio**: "Se pode ser resolvido com `visible: false`, não use override de funções!"

---

**Agentes Simplificados - Sistema BMAD**  
**Data**: 2025-07-30 20:30:00 