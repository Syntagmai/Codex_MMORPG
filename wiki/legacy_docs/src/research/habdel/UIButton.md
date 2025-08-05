# UIButton

O `UIButton` é um widget simples que estende `UIWidget`. É usado para criar botões clicáveis na interface.

## Herança

`UIButton` herda de `UIWidget`. Isso significa que possui todas as mesmas propriedades e métodos de um `UIWidget`.

## API Lua (`modules/corelib/ui/uibutton.lua`)

O `UIButton` é definido no arquivo `modules/corelib/ui/uibutton.lua`.

### `create()`

Esta função cria um novo widget `UIButton`. Define a propriedade `focusable` como `false` por padrão.

### `onMouseRelease(pos, button)`

Esta função é chamada quando um botão do mouse é liberado sobre o botão. Retorna `true` se o botão estiver no estado pressionado, o que significa que o evento `onClick` será disparado.

## Exemplo

Aqui está um exemplo de como criar um `UIButton` e manipular seu evento `onClick`:

#### Nível Basic
```lua
local button = g_ui.createWidget('Button', parent)
button:setText('Clique em Mim')
button:setPosition({x = 100, y = 100})
button:setSize({width = 100, height = 30})

button.onClick = function()
  print('Botão clicado!')
end
```

#### Nível Intermediate
```lua
local button = g_ui.createWidget('Button', parent)
button:setText('Clique em Mim')
button:setPosition({x = 100, y = 100})
button:setSize({width = 100, height = 30})

button.onClick = function()
  print('Botão clicado!')
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
local button = g_ui.createWidget('Button', parent)
button:setText('Clique em Mim')
button:setPosition({x = 100, y = 100})
button:setSize({width = 100, height = 30})

button.onClick = function()
  print('Botão clicado!')
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

## 🔗 **Links Automáticos**

> [!info] **Links Gerados Automaticamente**
> Estes links foram criados automaticamente pelo sistema de linkagem da categoria **Legacy**

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]
- [[../maps/search_index|Busca em Arquivos Legados]]
- [[../legacy_docs/README|Documentação Legada]]

### **🧭 Navegação**
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]
- [[../maps/category_indices|Índices por Categoria]]
- [[../maps/relationships|Relacionamentos]]

### **📊 Métricas da Categoria**
- **Categoria**: Legacy
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

