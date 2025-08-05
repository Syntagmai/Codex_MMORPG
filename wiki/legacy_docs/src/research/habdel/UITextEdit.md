# UITextEdit

O `UITextEdit` é um widget avançado que estende `UIWidget` para fornecer funcionalidades de edição de texto. Ele oferece recursos como posicionamento de cursor, seleção de texto, validação de entrada, modo senha, suporte a múltiplas linhas e integração com barras de rolagem.

## Herança

`UITextEdit` herda de `UIWidget`, tendo acesso a todas as propriedades e métodos do widget base.

## API C++ (`src/framework/ui/uitextedit.h`)

### Métodos Principais

#### Controle de Cursor

* `setCursorPos(int pos)`: Define a posição do cursor no texto
* `getCursorPos()`: Retorna a posição atual do cursor
* `setCursorVisible(bool enable)`: Define se o cursor deve ser visível
* `isCursorVisible()`: Retorna se o cursor está visível
* `setChangeCursorImage(bool enable)`: Define se a imagem do cursor deve mudar
* `isChangingCursorImage()`: Retorna se a imagem do cursor está mudando
* `blinkCursor()`: Faz o cursor piscar
* `moveCursorHorizontally(bool right)`: Move o cursor horizontalmente
* `moveCursorVertically(bool up)`: Move o cursor verticalmente

#### Seleção de Texto

* `setSelection(int start, int end)`: Define uma seleção de texto
* `getSelection()`: Retorna o texto selecionado
* `getSelectionStart()`: Retorna o índice inicial da seleção
* `getSelectionEnd()`: Retorna o índice final da seleção
* `hasSelection()`: Retorna se há texto selecionado
* `selectAll()`: Seleciona todo o texto
* `clearSelection()`: Limpa a seleção
* `deleteSelection()`: Remove o texto selecionado
* `setSelectionColor(Color color)`: Define a cor do texto selecionado
* `setSelectionBackgroundColor(Color color)`: Define a cor de fundo da seleção
* `getSelectionColor()`: Retorna a cor do texto selecionado
* `getSelectionBackgroundColor()`: Retorna a cor de fundo da seleção

#### Manipulação de Texto

* `appendText(std::string_view text)`: Adiciona texto ao final
* `appendCharacter(char c)`: Adiciona um caractere
* `removeCharacter(bool right)`: Remove um caractere (direita ou esquerda)
* `del(bool right)`: Remove caractere ou seleção
* `paste(std::string_view text)`: Cola texto na posição do cursor
* `copy()`: Copia a seleção para a área de transferência
* `cut()`: Corta a seleção para a área de transferência
* `wrapText()`: Ajusta quebra de texto

#### Propriedades de Edição

* `setEditable(bool editable)`: Define se o texto pode ser editado
* `isEditable()`: Retorna se o texto pode ser editado
* `setSelectable(bool selectable)`: Define se o texto pode ser selecionado
* `isSelectable()`: Retorna se o texto pode ser selecionado
* `setTextHidden(bool hidden)`: Define modo senha (oculta o texto)
* `isTextHidden()`: Retorna se o texto está oculto
* `setValidCharacters(std::string_view chars)`: Define caracteres válidos para entrada
* `setMaxLength(uint32_t maxLength)`: Define comprimento máximo do texto
* `getMaxLength()`: Retorna o comprimento máximo permitido

#### Navegação e Layout

* `setShiftNavigation(bool enable)`: Define navegação com Shift para seleção
* `isShiftNavigation()`: Retorna se navegação com Shift está ativa
* `setMultiline(bool enable)`: Define se suporta múltiplas linhas
* `isMultiline()`: Retorna se suporta múltiplas linhas
* `setAutoScroll(bool autoScroll)`: Define rolagem automática
* `isAutoScrolling()`: Retorna se rolagem automática está ativa

#### Área Virtual e Rolagem

* `setTextVirtualOffset(Point offset)`: Define offset virtual do texto
* `getTextVirtualOffset()`: Retorna o offset virtual atual
* `getTextVirtualSize()`: Retorna o tamanho virtual visível
* `getTextTotalSize()`: Retorna o tamanho total do texto
* `getTextPos(Point pos)`: Retorna posição do texto baseada em coordenadas
* `getDisplayedText()`: Retorna o texto exibido (pode diferir do texto real em modo senha)

#### Placeholder

* `setPlaceholder(std::string placeholder)`: Define texto de placeholder
* `setPlaceholderColor(Color color)`: Define cor do placeholder
* `setPlaceholderAlign(Fw::AlignmentFlag align)`: Define alinhamento do placeholder
* `setPlaceholderFont(std::string_view fontName)`: Define fonte do placeholder

## API Lua (`modules/corelib/ui/uitextedit.lua`)

### Integração com Barras de Rolagem

#### `setVerticalScrollBar(scrollbar)`

Conecta uma barra de rolagem vertical ao TextEdit. A barra será atualizada automaticamente conforme o conteúdo muda.

#### Nível Basic
```lua
local textEdit = g_ui.createWidget('MultilineTextEdit', parent)
local vScrollBar = g_ui.createWidget('VerticalScrollBar', parent)
textEdit:setVerticalScrollBar(vScrollBar)
```

#### Nível Intermediate
```lua
local textEdit = g_ui.createWidget('MultilineTextEdit', parent)
local vScrollBar = g_ui.createWidget('VerticalScrollBar', parent)
textEdit:setVerticalScrollBar(vScrollBar)
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
local textEdit = g_ui.createWidget('MultilineTextEdit', parent)
local vScrollBar = g_ui.createWidget('VerticalScrollBar', parent)
textEdit:setVerticalScrollBar(vScrollBar)
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

#### `setHorizontalScrollBar(scrollbar)`

Conecta uma barra de rolagem horizontal ao TextEdit.

#### Nível Basic
```lua
local textEdit = g_ui.createWidget('TextEdit', parent)
local hScrollBar = g_ui.createWidget('HorizontalScrollBar', parent)
textEdit:setHorizontalScrollBar(hScrollBar)
```

#### Nível Intermediate
```lua
local textEdit = g_ui.createWidget('TextEdit', parent)
local hScrollBar = g_ui.createWidget('HorizontalScrollBar', parent)
textEdit:setHorizontalScrollBar(hScrollBar)
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
local textEdit = g_ui.createWidget('TextEdit', parent)
local hScrollBar = g_ui.createWidget('HorizontalScrollBar', parent)
textEdit:setHorizontalScrollBar(hScrollBar)
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

#### `updateScrollBars()`

Atualiza as barras de rolagem baseado no conteúdo atual do texto.

### Eventos

#### `onMouseWheel(mousePos, mouseWheel)`

Gerencia rolagem com roda do mouse, integrando com as barras de rolagem conectadas.

#### `onTextAreaUpdate(virtualOffset, virtualSize, totalSize)`

Chamado quando a área de texto é atualizada, automaticamente atualiza as barras de rolagem.

## Estilos Predefinidos (`data/styles/10-textedits.otui`)

### `TextEdit`

Estilo básico para edição de texto de uma linha:

```otui
TextEdit < UITextEdit
  font: verdana-11px-antialised
  color: #f4f4f4ff
  size: 86 22
  text-offset: 0 4
  padding: 4
  image-source: /images/ui/textedit
  image-border: 1
  selection-color: #ffffffff
  selection-background-color: #808080ff
```

### `PasswordTextEdit`

Estilo para campos de senha:

```otui
PasswordTextEdit < TextEdit
  text-hidden: true
```

### `MultilineTextEdit`

Estilo para texto de múltiplas linhas:

```otui
MultilineTextEdit < TextEdit
  multiline: true
```

### `TextQtEdit`

Estilo alternativo com visual mais simples:

```otui
TextQtEdit < UITextEdit
  background-color: #363636ff
  change-cursor-image: false
```

## Exemplos de Uso

### Campo de Texto Simples

#### Nível Basic
```lua
local textEdit = g_ui.createWidget('TextEdit', parent)
textEdit:setPosition({x = 100, y = 100})
textEdit:setSize({width = 200, height = 22})
textEdit:setText('Digite aqui...')
textEdit:setMaxLength(50)

textEdit.onTextChange = function(widget, newText)
  print('Texto alterado para:', newText)
end
```

#### Nível Intermediate
```lua
local textEdit = g_ui.createWidget('TextEdit', parent)
textEdit:setPosition({x = 100, y = 100})
textEdit:setSize({width = 200, height = 22})
textEdit:setText('Digite aqui...')
textEdit:setMaxLength(50)

textEdit.onTextChange = function(widget, newText)
  print('Texto alterado para:', newText)
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
local textEdit = g_ui.createWidget('TextEdit', parent)
textEdit:setPosition({x = 100, y = 100})
textEdit:setSize({width = 200, height = 22})
textEdit:setText('Digite aqui...')
textEdit:setMaxLength(50)

textEdit.onTextChange = function(widget, newText)
  print('Texto alterado para:', newText)
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

### Campo de Senha

#### Nível Basic
```lua
local passwordEdit = g_ui.createWidget('PasswordTextEdit', parent)
passwordEdit:setPosition({x = 100, y = 130})
passwordEdit:setSize({width = 200, height = 22})
passwordEdit:setPlaceholder('Senha')
passwordEdit:setMaxLength(32)
```

#### Nível Intermediate
```lua
local passwordEdit = g_ui.createWidget('PasswordTextEdit', parent)
passwordEdit:setPosition({x = 100, y = 130})
passwordEdit:setSize({width = 200, height = 22})
passwordEdit:setPlaceholder('Senha')
passwordEdit:setMaxLength(32)
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
local passwordEdit = g_ui.createWidget('PasswordTextEdit', parent)
passwordEdit:setPosition({x = 100, y = 130})
passwordEdit:setSize({width = 200, height = 22})
passwordEdit:setPlaceholder('Senha')
passwordEdit:setMaxLength(32)
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

### Editor de Texto Multilinha com Rolagem

```lua
-- Criar editor multilinha
    --  Criar editor multilinha (traduzido)
local textEditor = g_ui.createWidget('MultilineTextEdit', parent)
textEditor:setPosition({x = 50, y = 50})
textEditor:setSize({width = 300, height = 200})

-- Criar barra de rolagem vertical
    --  Criar barra de rolagem vertical (traduzido)
local vScrollBar = g_ui.createWidget('VerticalScrollBar', parent)
vScrollBar:setPosition({x = 355, y = 50})
vScrollBar:setSize({width = 20, height = 200})

-- Conectar barra de rolagem
    --  Conectar barra de rolagem (traduzido)
textEditor:setVerticalScrollBar(vScrollBar)

-- Configurar propriedades
    --  Configurar propriedades (traduzido)
textEditor:setEditable(true)
textEditor:setSelectable(true)
textEditor:setAutoScroll(true)
```

### Validação de Entrada

```lua
-- Campo que aceita apenas números
local numberEdit = g_ui.createWidget('TextEdit', parent)
numberEdit:setValidCharacters('0123456789')
numberEdit:setMaxLength(10)

-- Campo que aceita apenas letras
    --  Campo que aceita apenas letras (traduzido)
local nameEdit = g_ui.createWidget('TextEdit', parent)
nameEdit:setValidCharacters('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ')
```

### Manipulação Programática

#### Nível Basic
```lua
local textEdit = g_ui.createWidget('TextEdit', parent)

-- Definir texto e posicionar cursor
textEdit:setText('Olá Mundo')
textEdit:setCursorPos(5) -- Posiciona cursor após "Olá "

-- Selecionar parte do texto
textEdit:setSelection(0, 4) -- Seleciona "Olá "

-- Manipular seleção
local selectedText = textEdit:getSelection()
textEdit:deleteSelection()
textEdit:appendText('Novo texto')

-- Operações de clipboard
textEdit:selectAll()
local copiedText = textEdit:copy()
textEdit:clearSelection()
textEdit:paste(' - Colado!')
```

#### Nível Intermediate
```lua
local textEdit = g_ui.createWidget('TextEdit', parent)

-- Definir texto e posicionar cursor
textEdit:setText('Olá Mundo')
textEdit:setCursorPos(5) -- Posiciona cursor após "Olá "

-- Selecionar parte do texto
textEdit:setSelection(0, 4) -- Seleciona "Olá "

-- Manipular seleção
local selectedText = textEdit:getSelection()
textEdit:deleteSelection()
textEdit:appendText('Novo texto')

-- Operações de clipboard
textEdit:selectAll()
local copiedText = textEdit:copy()
textEdit:clearSelection()
textEdit:paste(' - Colado!')
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
local textEdit = g_ui.createWidget('TextEdit', parent)

-- Definir texto e posicionar cursor
textEdit:setText('Olá Mundo')
textEdit:setCursorPos(5) -- Posiciona cursor após "Olá "

-- Selecionar parte do texto
textEdit:setSelection(0, 4) -- Seleciona "Olá "

-- Manipular seleção
local selectedText = textEdit:getSelection()
textEdit:deleteSelection()
textEdit:appendText('Novo texto')

-- Operações de clipboard
textEdit:selectAll()
local copiedText = textEdit:copy()
textEdit:clearSelection()
textEdit:paste(' - Colado!')
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

### Personalização de Aparência

```lua
local customEdit = g_ui.createWidget('TextEdit', parent)

-- Personalizar cores de seleção
customEdit:setSelectionColor('#ffff00') -- Texto amarelo
customEdit:setSelectionBackgroundColor('#0000ff') -- Fundo azul

-- Configurar placeholder
    --  Configurar placeholder (traduzido)
customEdit:setPlaceholder('Digite seu nome...')
customEdit:setPlaceholderColor('#888888')
customEdit:setPlaceholderAlign(AlignCenter)

-- Configurar fonte específica para placeholder
customEdit:setPlaceholderFont('verdana-9px-antialised')
```

## Eventos Comuns

```lua
local textEdit = g_ui.createWidget('TextEdit', parent)

-- Evento de mudança de texto
textEdit.onTextChange = function(widget, newText, oldText)
  print('Texto mudou de "' .. oldText .. '" para "' .. newText .. '"')
end

-- Evento de foco
    --  Evento de foco (traduzido)
textEdit.onFocusChange = function(widget, focused)
  if focused then
    -- Verificação condicional
    print('TextEdit ganhou foco')
  else
    print('TextEdit perdeu foco')
  end
end

-- Evento de tecla pressionada
    --  Evento de tecla pressionada (traduzido)
textEdit.onKeyPress = function(widget, keyCode, keyModifiers)
  if keyCode == KeyEnter then
    -- Verificação condicional
    print('Enter pressionado, texto:', widget:getText())
    return true -- Consumir evento
  end
  return false
end
```

## Melhores Práticas

1. **Use estilos apropriados** - Escolha `TextEdit`, `PasswordTextEdit` ou `MultilineTextEdit` conforme necessário
2. **Defina limites** - Use `setMaxLength()` para controlar o tamanho da entrada
3. **Valide entrada** - Use `setValidCharacters()` para restringir caracteres permitidos
4. **Configure placeholders** - Ajude o usuário com texto de orientação
5. **Implemente rolagem** - Para textos longos, conecte barras de rolagem
6. **Gerencie foco** - Configure adequadamente a navegação com Tab
7. **Personalize seleção** - Ajuste cores de seleção para melhor legibilidade
8. **Trate eventos** - Implemente callbacks apropriados para interação do usuário

O `UITextEdit` fornece uma base sólida para qualquer interface que necessite de entrada de texto, desde campos simples até editores complexos com múltiplas linhas e recursos avançados.
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

