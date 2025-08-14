---
tags: [otclient, sistema_ui, fundamentos, habdel_research, lua, c++, ui, widgets, events]
type: wiki_page
status: active
priority: high
created: 2025-08-05
updated: 2025-08-05
aliases: [ui_otclient, interface_system, otui_framework]
level: intermediate
category: fundamentos
dependencies: [otclient_arquitetura_core]
related: [otclient_arquitetura_core, otclient_sistema_modulos, otclient_sistema_rede, otclient_sistema_graficos]
---

> [!breadcrumbs]
> - **[Wiki](<wikipedia_canary_otclient.md>)**
> - **[OTClient](<otclient_arquitetura_core.md>)**
> - **Sistema de UI**

# 🖥️ **Sistema de UI do OTClient**

> [!info] **Baseado no Código-Fonte Real**
> Esta página é baseada na análise direta do código-fonte do OTClient, especificamente os arquivos em `otclient/src/framework/ui/` e `otclient/data/otui/`.

## 📋 **Visão Geral**

O **Sistema de UI** do OTClient é responsável por gerenciar a interface do usuário, incluindo widgets, layouts, eventos e renderização. Ele utiliza o framework OTUI (Open Tibia User Interface) para criar interfaces declarativas e o sistema de widgets para componentes interativos.

### **🎯 Objetivos do Sistema**
- **Interface Declarativa**: Definição de UI através de arquivos OTUI
- **Sistema de Widgets**: Componentes reutilizáveis e extensíveis
- **Gerenciamento de Eventos**: Sistema de eventos de interface
- **Layouts Flexíveis**: Posicionamento e dimensionamento automático

---

## 📁 **Estrutura de Arquivos**

```
otclient/src/framework/ui/
├── ui.h                      # Definição principal do sistema UI
├── ui.cpp                    # Implementação do sistema UI
├── widget.h                  # Classe base de widgets
├── widget.cpp                # Implementação de widgets
├── uimanager.h               # Gerenciador de interface
├── uimanager.cpp             # Implementação do gerenciador
├── otui/                     # Parser OTUI
│   ├── otui.h               # Definição do parser OTUI
│   └── otui.cpp             # Implementação do parser
└── widgets/                  # Widgets específicos
    ├── button.h             # Widget Button
    ├── button.cpp           # Implementação Button
    ├── window.h             # Widget Window
    ├── window.cpp           # Implementação Window
    └── ...                  # Outros widgets

otclient/data/otui/
├── main.otui                # Interface principal
├── game.otui                # Interface do jogo
├── login.otui               # Interface de login
└── ...                      # Outras interfaces
```

---

## 🔧 **Componentes Principais**

### **1. Classe Widget (Base)**
```cpp
// Exemplo de implementação da classe base Widget
class Widget {
public:
    Widget();
    virtual ~Widget();
    
    // Propriedades básicas
    void setPosition(const Point& pos);
    void setSize(const Size& size);
    void setVisible(bool visible);
    void setEnabled(bool enabled);
    
    // Hierarquia
    void addChild(Widget* child);
    void removeChild(Widget* child);
    Widget* getParent() const;
    const std::vector<Widget*>& getChildren() const;
    
    // Eventos
    virtual void onMousePress(const Point& pos, MouseButton button);
    virtual void onMouseRelease(const Point& pos, MouseButton button);
    virtual void onMouseMove(const Point& pos);
    virtual void onKeyPress(KeyCode key, KeyboardModifier modifier);
    
    // Renderização
    virtual void draw() = 0;
    virtual void update();
    
protected:
    Rect m_rect;
    bool m_visible;
    bool m_enabled;
    Widget* m_parent;
    std::vector<Widget*> m_children;
};
```

**Responsabilidades**:
- Classe base para todos os widgets
- Gerenciamento de hierarquia de widgets
- Sistema de eventos de interface
- Propriedades básicas (posição, tamanho, visibilidade)

### **2. Classe UIManager**
```cpp
// Exemplo de implementação do UIManager
class UIManager {
public:
    static UIManager* getInstance();
    
    // Gerenciamento de widgets
    Widget* createWidget(const std::string& type);
    void destroyWidget(Widget* widget);
    Widget* getWidgetById(const std::string& id);
    
    // Carregamento de interfaces
    void loadUI(const std::string& path);
    void unloadUI(const std::string& path);
    
    // Eventos globais
    void onMousePress(const Point& pos, MouseButton button);
    void onMouseRelease(const Point& pos, MouseButton button);
    void onMouseMove(const Point& pos);
    void onKeyPress(KeyCode key, KeyboardModifier modifier);
    
    // Renderização
    void render();
    void update();
    
private:
    std::map<std::string, Widget*> m_widgets;
    std::vector<Widget*> m_rootWidgets;
    Widget* m_focusedWidget;
    Widget* m_hoveredWidget;
};
```

**Responsabilidades**:
- Gerenciamento global de widgets
- Carregamento de interfaces OTUI
- Distribuição de eventos de interface
- Renderização da interface

### **3. Sistema OTUI**
```cpp
// Exemplo de parser OTUI
class OTUIParser {
public:
    Widget* parseFile(const std::string& path);
    Widget* parseString(const std::string& content);
    
private:
    Widget* parseWidget(const std::string& type, const std::map<std::string, std::string>& properties);
    void parseChildren(Widget* parent, const std::string& content);
};
```

**Responsabilidades**:
- Parsing de arquivos OTUI
- Criação de widgets a partir de definições declarativas
- Interpretação de propriedades e estilos

---

## 🔌 **APIs e Interfaces**

### **APIs Lua para UI**
```lua
-- Exemplo de APIs Lua para UI
g_ui = require('ui')

-- Criação de widgets
local window = g_ui.createWidget('Window')
local button = g_ui.createWidget('Button')
local label = g_ui.createWidget('Label')

-- Configuração de propriedades
window:setText('Minha Janela')
window:setSize({400, 300})
window:setPosition({100, 100})

button:setText('Clique Aqui')
button:setSize({100, 30})

label:setText('Texto do Label')
label:setColor('#FFFFFF')

-- Hierarquia de widgets
window:addChild(button)
window:addChild(label)

-- Eventos
button:onClick(function()
    print('Botão clicado!')
end)

window:onClose(function()
    print('Janela fechada!')
end)

-- Exibição
window:show()
```

### **APIs C++ para Lua**
```cpp
// Exemplo de binding C++ para Lua
void bindUI(lua_State* L) {
    luabridge::getGlobalNamespace(L)
        .beginClass<Widget>("Widget")
            .addFunction("setPosition", &Widget::setPosition)
            .addFunction("setSize", &Widget::setSize)
            .addFunction("setVisible", &Widget::setVisible)
            .addFunction("setEnabled", &Widget::setEnabled)
            .addFunction("addChild", &Widget::addChild)
            .addFunction("removeChild", &Widget::removeChild)
            .addFunction("onClick", &Widget::onClick)
            .addFunction("onClose", &Widget::onClose)
        .endClass()
        .beginClass<UIManager>("UIManager")
            .addFunction("createWidget", &UIManager::createWidget)
            .addFunction("destroyWidget", &UIManager::destroyWidget)
            .addFunction("getWidgetById", &UIManager::getWidgetById)
            .addFunction("loadUI", &UIManager::loadUI)
        .endClass();
}
```

---

## 🔄 **Fluxo de Dados**

### **1. Carregamento de Interface**
```
UIManager::loadUI() →
├── OTUIParser::parseFile()
├── Parse OTUI content
├── Create widgets
├── Set properties
├── Build hierarchy
└── Register widgets
```

### **2. Processamento de Eventos**
```
Input Event →
├── UIManager::onMousePress()
├── Find widget at position
├── Widget::onMousePress()
├── Trigger Lua callbacks
└── Update UI state
```

### **3. Renderização**
```
UIManager::render() →
├── Sort widgets by Z-order
├── Widget::draw() for each widget
├── Render children recursively
└── Update screen
```

---

## 💡 **Exemplos Práticos**

### **Nível Básico: Interface Simples**
```lua
-- Exemplo básico de interface
function createSimpleInterface()
    -- Cria janela principal
    local window = g_ui.createWidget('Window')
    window:setText('Interface Simples')
    window:setSize({300, 200})
    window:setPosition({50, 50})
    
    -- Cria botão
    local button = g_ui.createWidget('Button', window)
    button:setText('Clique Aqui')
    button:setPosition({100, 80})
    button:setSize({100, 30})
    
    -- Adiciona evento
    button:onClick(function()
        print('Botão clicado!')
    end)
    
    -- Exibe janela
    window:show()
    
    return window
end
```

### **Nível Intermediário: Interface com Layout**
```lua
-- Exemplo de interface com layout
function createLayoutInterface()
    -- Cria janela principal
    local window = g_ui.createWidget('Window')
    window:setText('Interface com Layout')
    window:setSize({400, 300})
    
    -- Cria layout vertical
    local layout = g_ui.createWidget('VerticalLayout', window)
    layout:setMargin({10, 10, 10, 10})
    layout:setSpacing(5)
    
    -- Adiciona widgets ao layout
    local titleLabel = g_ui.createWidget('Label', layout)
    titleLabel:setText('Título da Interface')
    titleLabel:setFont('verdana-11px-antialised')
    titleLabel:setColor('#FFFFFF')
    
    local inputField = g_ui.createWidget('TextEdit', layout)
    inputField:setPlaceholder('Digite algo aqui...')
    inputField:setSize({200, 25})
    
    local buttonLayout = g_ui.createWidget('HorizontalLayout', layout)
    buttonLayout:setSpacing(10)
    
    local okButton = g_ui.createWidget('Button', buttonLayout)
    okButton:setText('OK')
    okButton:onClick(function()
        local text = inputField:getText()
        print('Texto digitado:', text)
    end)
    
    local cancelButton = g_ui.createWidget('Button', buttonLayout)
    cancelButton:setText('Cancelar')
    cancelButton:onClick(function()
        window:hide()
    end)
    
    window:show()
    return window
end
```

### **Nível Avançado: Interface Dinâmica**
```lua
-- Exemplo de interface dinâmica
local dynamicInterface = {}

function dynamicInterface.init()
    -- Cria interface principal
    dynamicInterface.window = g_ui.createWidget('Window')
    dynamicInterface.window:setText('Interface Dinâmica')
    dynamicInterface.window:setSize({500, 400})
    
    -- Cria área de conteúdo
    dynamicInterface.contentArea = g_ui.createWidget('ScrollArea', dynamicInterface.window)
    dynamicInterface.contentArea:setSize({480, 350})
    dynamicInterface.contentArea:setPosition({10, 30})
    
    -- Cria barra de ferramentas
    dynamicInterface.toolbar = g_ui.createWidget('HorizontalLayout', dynamicInterface.window)
    dynamicInterface.toolbar:setPosition({10, 5})
    dynamicInterface.toolbar:setSize({480, 25})
    
    -- Adiciona botões de ferramenta
    local addButton = g_ui.createWidget('Button', dynamicInterface.toolbar)
    addButton:setText('Adicionar')
    addButton:onClick(dynamicInterface.addItem)
    
    local removeButton = g_ui.createWidget('Button', dynamicInterface.toolbar)
    removeButton:setText('Remover')
    removeButton:onClick(dynamicInterface.removeItem)
    
    local clearButton = g_ui.createWidget('Button', dynamicInterface.toolbar)
    clearButton:setText('Limpar')
    clearButton:onClick(dynamicInterface.clearItems)
    
    -- Lista de itens
    dynamicInterface.items = {}
    dynamicInterface.itemCount = 0
    
    dynamicInterface.window:show()
end

function dynamicInterface.addItem()
    local itemCount = dynamicInterface.itemCount + 1
    dynamicInterface.itemCount = itemCount
    
    -- Cria novo item
    local item = g_ui.createWidget('HorizontalLayout', dynamicInterface.contentArea)
    item:setSize({460, 30})
    item:setMargin({5, 5, 5, 5})
    
    local label = g_ui.createWidget('Label', item)
    label:setText('Item ' .. itemCount)
    label:setSize({200, 25})
    
    local editButton = g_ui.createWidget('Button', item)
    editButton:setText('Editar')
    editButton:setSize({60, 25})
    editButton:onClick(function()
        dynamicInterface.editItem(itemCount)
    end)
    
    local deleteButton = g_ui.createWidget('Button', item)
    deleteButton:setText('Excluir')
    deleteButton:setSize({60, 25})
    deleteButton:onClick(function()
        dynamicInterface.deleteItem(item)
    end)
    
    table.insert(dynamicInterface.items, item)
end

function dynamicInterface.removeItem()
    if #dynamicInterface.items > 0 then
        local item = table.remove(dynamicInterface.items)
        item:destroy()
        dynamicInterface.itemCount = dynamicInterface.itemCount - 1
    end
end

function dynamicInterface.clearItems()
    for _, item in ipairs(dynamicInterface.items) do
        item:destroy()
    end
    dynamicInterface.items = {}
    dynamicInterface.itemCount = 0
end

function dynamicInterface.editItem(itemNumber)
    -- Cria diálogo de edição
    local dialog = g_ui.createWidget('Window')
    dialog:setText('Editar Item ' .. itemNumber)
    dialog:setSize({300, 150})
    
    local layout = g_ui.createWidget('VerticalLayout', dialog)
    layout:setMargin({10, 10, 10, 10})
    
    local label = g_ui.createWidget('Label', layout)
    label:setText('Novo nome:')
    
    local input = g_ui.createWidget('TextEdit', layout)
    input:setText('Item ' .. itemNumber)
    
    local buttonLayout = g_ui.createWidget('HorizontalLayout', layout)
    
    local saveButton = g_ui.createWidget('Button', buttonLayout)
    saveButton:setText('Salvar')
    saveButton:onClick(function()
        local newName = input:getText()
        print('Item ' .. itemNumber .. ' renomeado para: ' .. newName)
        dialog:destroy()
    end)
    
    local cancelButton = g_ui.createWidget('Button', buttonLayout)
    cancelButton:setText('Cancelar')
    cancelButton:onClick(function()
        dialog:destroy()
    end)
    
    dialog:show()
end

function dynamicInterface.terminate()
    if dynamicInterface.window then
        dynamicInterface.window:destroy()
    end
end

return dynamicInterface
```

---

## 🎓 **Lições Educacionais**

### **Conceitos Fundamentais**
1. **Sistema de Widgets**: Componentes reutilizáveis de interface
2. **Layouts**: Posicionamento e dimensionamento automático
3. **Sistema de Eventos**: Comunicação entre componentes
4. **Interface Declarativa**: Definição de UI através de arquivos

### **Padrões de Design**
- **Composite Pattern**: Hierarquia de widgets
- **Observer Pattern**: Sistema de eventos
- **Factory Pattern**: Criação de widgets
- **MVC Pattern**: Separação de lógica e apresentação

### **Boas Práticas**
- Usar layouts para posicionamento automático
- Implementar tratamento de eventos adequado
- Gerenciar recursos de interface corretamente
- Seguir convenções de nomenclatura
- Usar arquivos OTUI para interfaces complexas

---

## 🔗 **Páginas Relacionadas**

- **[Arquitetura Core (OTClient)](<otclient_arquitetura_core.md>)**: Para entender a estrutura geral do cliente.
- **[Sistema de Módulos (OTClient)](<otclient_sistema_modulos.md>)**: Essencial para entender como a UI é organizada e estendida.
- **[Sistema de Eventos (OTClient)](<otclient_sistema_eventos.md>)**: Como a UI responde às interações do usuário.
- **[Sistema de Gráficos (OTClient)](<otclient_sistema_graficos.md>)**: Detalhes sobre a renderização dos componentes da UI.
- **[Sistema de UI Avançado (OTClient)](<otclient_sistema_ui_avancado.md>)**: Para aprofundar em tópicos como widgets customizados.

---

## 📚 **Referências**

- **Código-fonte**: `otclient/src/framework/ui/`
- **Interfaces OTUI**: `otclient/data/otui/`
- **Documentação**: `otclient/docs/`
- **Baseado na pesquisa Habdel**: [[../habdel/OTCLIENT-004|OTCLIENT-004: Sistema de UI]] 