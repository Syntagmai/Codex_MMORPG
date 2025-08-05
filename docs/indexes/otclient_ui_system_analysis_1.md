# OTClient UI System - Análise Técnica

## 🎯 Visão Geral

O **Sistema de UI** do OTClient é responsável por toda a interface do usuário, incluindo widgets, layouts, estilos e internacionalização. Ele fornece uma abstração robusta e flexível para criação de interfaces gráficas modernas e responsivas.

## 📊 Estatísticas da Análise

- **Arquivos Analisados**: 29
- **Linhas de Código**: 6,913
- **Componentes Principais**: 28
- **Padrões Identificados**: 1
- **APIs Documentadas**: 14

## 🏗️ Arquitetura do Sistema

### **Componentes Principais**

### **ui.h**
- **Linhas**: 35
- **Classes**: 0
- **Métodos**: 0
- **Padrões**: Nenhum

### **uiwidget.h**
- **Linhas**: 629
- **Classes**: 6
- **Métodos**: 173
- **Padrões**: Nenhum

### **uiwidget.cpp**
- **Linhas**: 2,075
- **Classes**: 0
- **Métodos**: 13
- **Padrões**: Nenhum

### **uimanager.h**
- **Linhas**: 102
- **Classes**: 3
- **Métodos**: 26
- **Padrões**: Singleton

### **uimanager.cpp**
- **Linhas**: 617
- **Classes**: 0
- **Métodos**: 11
- **Padrões**: Nenhum

### **uilayout.h**
- **Linhas**: 66
- **Classes**: 1
- **Métodos**: 2
- **Padrões**: Nenhum

### **uilayout.cpp**
- **Linhas**: 72
- **Classes**: 0
- **Métodos**: 0
- **Padrões**: Nenhum

### **uianchorlayout.h**
- **Linhas**: 91
- **Classes**: 3
- **Métodos**: 9
- **Padrões**: Nenhum

### **uianchorlayout.cpp**
- **Linhas**: 286
- **Classes**: 0
- **Métodos**: 2
- **Padrões**: Nenhum

### **uiverticallayout.h**
- **Linhas**: 47
- **Classes**: 1
- **Métodos**: 0
- **Padrões**: Nenhum

### **uiverticallayout.cpp**
- **Linhas**: 104
- **Classes**: 0
- **Métodos**: 0
- **Padrões**: Nenhum

### **uihorizontallayout.h**
- **Linhas**: 46
- **Classes**: 1
- **Métodos**: 0
- **Padrões**: Nenhum

### **uihorizontallayout.cpp**
- **Linhas**: 102
- **Classes**: 0
- **Métodos**: 0
- **Padrões**: Nenhum

### **uigridlayout.h**
- **Linhas**: 66
- **Classes**: 1
- **Métodos**: 0
- **Padrões**: Nenhum

### **uigridlayout.cpp**
- **Linhas**: 121
- **Classes**: 0
- **Métodos**: 0
- **Padrões**: Nenhum

### **uiboxlayout.h**
- **Linhas**: 46
- **Classes**: 1
- **Métodos**: 0
- **Padrões**: Nenhum

### **uiboxlayout.cpp**
- **Linhas**: 40
- **Classes**: 0
- **Métodos**: 0
- **Padrões**: Nenhum

### **uitextedit.h**
- **Linhas**: 165
- **Classes**: 1
- **Métodos**: 30
- **Padrões**: Nenhum

### **uitextedit.cpp**
- **Linhas**: 955
- **Classes**: 0
- **Métodos**: 11
- **Padrões**: Nenhum

### **uiwidgettext.cpp**
- **Linhas**: 211
- **Classes**: 0
- **Métodos**: 0
- **Padrões**: Nenhum

### **uiwidgetimage.cpp**
- **Linhas**: 230
- **Classes**: 0
- **Métodos**: 0
- **Padrões**: Nenhum

### **uiwidgetbasestyle.cpp**
- **Linhas**: 422
- **Classes**: 0
- **Métodos**: 7
- **Padrões**: Nenhum

### **uiqrcode.h**
- **Linhas**: 44
- **Classes**: 1
- **Métodos**: 1
- **Padrões**: Nenhum

### **uiqrcode.cpp**
- **Linhas**: 62
- **Classes**: 0
- **Métodos**: 0
- **Padrões**: Nenhum

### **uiparticles.h**
- **Linhas**: 43
- **Classes**: 1
- **Métodos**: 1
- **Padrões**: Nenhum

### **uiparticles.cpp**
- **Linhas**: 69
- **Classes**: 0
- **Métodos**: 0
- **Padrões**: Nenhum

### **uitranslator.h**
- **Linhas**: 35
- **Classes**: 0
- **Métodos**: 4
- **Padrões**: Nenhum

### **uitranslator.cpp**
- **Linhas**: 132
- **Classes**: 0
- **Métodos**: 0
- **Padrões**: Nenhum



### **Padrões de Design Identificados**

- **Singleton**: Descrição do padrão



## 🔌 APIs Principais

### **UIWidget**
Widget base para todos os componentes de UI

**Métodos Principais:**
- `create()`
- `destroy()`
- `setVisible()`
- `setEnabled()`
- `setFocus()`

**Componentes:** uiwidget.h, uiwidget.cpp

### **UIManager**
Gerenciador central de widgets e layouts

**Métodos Principais:**
- `createWidget()`
- `destroyWidget()`
- `getWidget()`
- `update()`

**Componentes:** uimanager.h, uimanager.cpp

### **UILayout**
Sistema de layouts para organização de widgets

**Métodos Principais:**
- `addWidget()`
- `removeWidget()`
- `updateLayout()`
- `getSize()`

**Componentes:** uilayout.h, uilayout.cpp

### **UIAnchorLayout**
Layout baseado em âncoras para posicionamento

**Métodos Principais:**
- `setAnchor()`
- `getAnchor()`
- `updateAnchors()`

**Componentes:** uianchorlayout.h, uianchorlayout.cpp

### **UIVerticalLayout**
Layout vertical para organização em coluna

**Métodos Principais:**
- `addWidget()`
- `setSpacing()`
- `setAlignment()`

**Componentes:** uiverticallayout.h, uiverticallayout.cpp

### **UIHorizontalLayout**
Layout horizontal para organização em linha

**Métodos Principais:**
- `addWidget()`
- `setSpacing()`
- `setAlignment()`

**Componentes:** uihorizontallayout.h, uihorizontallayout.cpp

### **UIGridLayout**
Layout em grade para organização tabular

**Métodos Principais:**
- `setGridSize()`
- `addWidget()`
- `setCellSpacing()`

**Componentes:** uigridlayout.h, uigridlayout.cpp

### **UITextEdit**
Widget de edição de texto

**Métodos Principais:**
- `setText()`
- `getText()`
- `setReadOnly()`
- `setMaxLength()`

**Componentes:** uitextedit.h, uitextedit.cpp

### **UIWidgetText**
Widget de exibição de texto

**Métodos Principais:**
- `setText()`
- `getText()`
- `setFont()`
- `setColor()`

**Componentes:** uiwidgettext.h, uiwidgettext.cpp

### **UIWidgetImage**
Widget de exibição de imagens

**Métodos Principais:**
- `setImage()`
- `getImage()`
- `setStretched()`
- `setSmooth()`

**Componentes:** uiwidgetimage.h, uiwidgetimage.cpp

### **UIWidgetBaseStyle**
Sistema de estilos base para widgets

**Métodos Principais:**
- `setStyle()`
- `getStyle()`
- `applyStyle()`
- `resetStyle()`

**Componentes:** uiwidgetbasestyle.h, uiwidgetbasestyle.cpp

### **UIQRCode**
Widget para exibição de códigos QR

**Métodos Principais:**
- `setData()`
- `getData()`
- `setSize()`
- `setErrorCorrection()`

**Componentes:** uiqrcode.h, uiqrcode.cpp

### **UIParticles**
Sistema de partículas para UI

**Métodos Principais:**
- `addParticle()`
- `removeParticle()`
- `update()`
- `clear()`

**Componentes:** uiparticles.h, uiparticles.cpp

### **UITranslator**
Sistema de tradução para internacionalização

**Métodos Principais:**
- `translate()`
- `setLanguage()`
- `getLanguage()`
- `loadFile()`

**Componentes:** uitranslator.h, uitranslator.cpp



## 💡 Exemplos Práticos

### **Criação de Widget Básico**
Como criar e configurar um widget básico

#### Nível Basic
```cpp
    if (auto textWidget = std::dynamic_pointer_cast<UIWidgetText>(widget)) {{
```

#### Nível Intermediate
```cpp
// Exemplo de criação de widget básico
#include "uiwidget.h"
#include "uimanager.h"

void createBasicWidget() {{
    // Criar widget através do gerenciador
    UIWidgetPtr widget = g_ui.createWidget("UIWidget");
    
    // Configurar propriedades básicas
    widget->setVisible(true);
    widget->setEnabled(true);
    widget->setSize(Size(100, 50));
    widget->setPosition(Point(10, 10));
    
    // Definir texto se for um widget de texto
    if (auto textWidget = std::dynamic_pointer_cast<UIWidgetText>(widget)) {{
        textWidget->setText("Hello World!");
        textWidget->setColor(Color::white);
    }}
}}
```

#### Nível Advanced
```cpp
// Exemplo de criação de widget básico
#include "uiwidget.h"
#include "uimanager.h"

void createBasicWidget() {{
    // Criar widget através do gerenciador
    UIWidgetPtr widget = g_ui.createWidget("UIWidget");
    
    // Configurar propriedades básicas
    widget->setVisible(true);
    widget->setEnabled(true);
    widget->setSize(Size(100, 50));
    widget->setPosition(Point(10, 10));
    
    // Definir texto se for um widget de texto
    if (auto textWidget = std::dynamic_pointer_cast<UIWidgetText>(widget)) {{
        textWidget->setText("Hello World!");
        textWidget->setColor(Color::white);
    }}
}}
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

### **Sistema de Layouts**
Como usar diferentes tipos de layouts

#### Nível Basic
```cpp

```

#### Nível Intermediate
```cpp
// Exemplo de uso de layouts
#include "uiverticallayout.h"
#include "uihorizontallayout.h"
#include "uigridlayout.h"

void createLayoutExample() {{
    // Criar layout vertical
    UIVerticalLayoutPtr verticalLayout = UIVerticalLayout::create();
    verticalLayout->setSpacing(5);
    verticalLayout->setAlignment(UIAlign::Center);
    
    // Adicionar widgets ao layout
    UIWidgetPtr button1 = g_ui.createWidget("UIButton");
    UIWidgetPtr button2 = g_ui.createWidget("UIButton");
    UIWidgetPtr textEdit = g_ui.createWidget("UITextEdit");
    
    verticalLayout->addWidget(button1);
    verticalLayout->addWidget(button2);
    verticalLayout->addWidget(textEdit);
    
    // Criar layout horizontal
    UIHorizontalLayoutPtr horizontalLayout = UIHorizontalLayout::create();
    horizontalLayout->setSpacing(10);
    
    // Adicionar widgets ao layout horizontal
    UIWidgetPtr label = g_ui.createWidget("UILabel");
    UIWidgetPtr input = g_ui.createWidget("UITextEdit");
    
    horizontalLayout->addWidget(label);
    horizontalLayout->addWidget(input);
    
    // Criar layout em grade
    UIGridLayoutPtr gridLayout = UIGridLayout::create();
    gridLayout->setGridSize(Size(2, 2));
    gridLayout->setCellSpacing(5);
    
    // Adicionar widgets à grade
    for (int i = 0; i < 4; i++) {{
        UIWidgetPtr cell = g_ui.createWidget("UIWidget");
        gridLayout->addWidget(cell);
    }}
}}
```

#### Nível Advanced
```cpp
// Exemplo de uso de layouts
#include "uiverticallayout.h"
#include "uihorizontallayout.h"
#include "uigridlayout.h"

void createLayoutExample() {{
    // Criar layout vertical
    UIVerticalLayoutPtr verticalLayout = UIVerticalLayout::create();
    verticalLayout->setSpacing(5);
    verticalLayout->setAlignment(UIAlign::Center);
    
    // Adicionar widgets ao layout
    UIWidgetPtr button1 = g_ui.createWidget("UIButton");
    UIWidgetPtr button2 = g_ui.createWidget("UIButton");
    UIWidgetPtr textEdit = g_ui.createWidget("UITextEdit");
    
    verticalLayout->addWidget(button1);
    verticalLayout->addWidget(button2);
    verticalLayout->addWidget(textEdit);
    
    // Criar layout horizontal
    UIHorizontalLayoutPtr horizontalLayout = UIHorizontalLayout::create();
    horizontalLayout->setSpacing(10);
    
    // Adicionar widgets ao layout horizontal
    UIWidgetPtr label = g_ui.createWidget("UILabel");
    UIWidgetPtr input = g_ui.createWidget("UITextEdit");
    
    horizontalLayout->addWidget(label);
    horizontalLayout->addWidget(input);
    
    // Criar layout em grade
    UIGridLayoutPtr gridLayout = UIGridLayout::create();
    gridLayout->setGridSize(Size(2, 2));
    gridLayout->setCellSpacing(5);
    
    // Adicionar widgets à grade
    for (int i = 0; i < 4; i++) {{
        UIWidgetPtr cell = g_ui.createWidget("UIWidget");
        gridLayout->addWidget(cell);
    }}
}}
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

### **Layout com Âncoras**
Como usar layout baseado em âncoras para posicionamento

#### Nível Basic
```cpp
// Exemplo de layout com âncoras
#include "uianchorlayout.h"

void createAnchorLayout() {{
    // Criar layout com âncoras
    UIAnchorLayoutPtr anchorLayout = UIAnchorLayout::create();
    
    // Criar widgets
    UIWidgetPtr topBar = g_ui.createWidget("UIWidget");
    UIWidgetPtr sidePanel = g_ui.createWidget("UIWidget");
    UIWidgetPtr mainContent = g_ui.createWidget("UIWidget");
    UIWidgetPtr statusBar = g_ui.createWidget("UIWidget");
    
    // Configurar âncoras
    // Top bar: ancorado no topo, largura total
    anchorLayout->setAnchor(topBar, UIAnchor::Top | UIAnchor::Left | UIAnchor::Right);
    
    // Side panel: ancorado à esquerda, altura entre top bar e status bar
    anchorLayout->setAnchor(sidePanel, UIAnchor::Left | UIAnchor::Top | UIAnchor::Bottom);
    
    // Main content: preenche o espaço restante
    anchorLayout->setAnchor(mainContent, UIAnchor::Top | UIAnchor::Right | UIAnchor::Bottom);
    
    // Status bar: ancorado na parte inferior, largura total
    anchorLayout->setAnchor(statusBar, UIAnchor::Bottom | UIAnchor::Left | UIAnchor::Right);
    
    // Adicionar widgets ao layout
    anchorLayout->addWidget(topBar);
    anchorLayout->addWidget(sidePanel);
    anchorLayout->addWidget(mainContent);
    anchorLayout->addWidget(statusBar);
}}
```

#### Nível Intermediate
```cpp
// Exemplo de layout com âncoras
#include "uianchorlayout.h"

void createAnchorLayout() {{
    // Criar layout com âncoras
    UIAnchorLayoutPtr anchorLayout = UIAnchorLayout::create();
    
    // Criar widgets
    UIWidgetPtr topBar = g_ui.createWidget("UIWidget");
    UIWidgetPtr sidePanel = g_ui.createWidget("UIWidget");
    UIWidgetPtr mainContent = g_ui.createWidget("UIWidget");
    UIWidgetPtr statusBar = g_ui.createWidget("UIWidget");
    
    // Configurar âncoras
    // Top bar: ancorado no topo, largura total
    anchorLayout->setAnchor(topBar, UIAnchor::Top | UIAnchor::Left | UIAnchor::Right);
    
    // Side panel: ancorado à esquerda, altura entre top bar e status bar
    anchorLayout->setAnchor(sidePanel, UIAnchor::Left | UIAnchor::Top | UIAnchor::Bottom);
    
    // Main content: preenche o espaço restante
    anchorLayout->setAnchor(mainContent, UIAnchor::Top | UIAnchor::Right | UIAnchor::Bottom);
    
    // Status bar: ancorado na parte inferior, largura total
    anchorLayout->setAnchor(statusBar, UIAnchor::Bottom | UIAnchor::Left | UIAnchor::Right);
    
    // Adicionar widgets ao layout
    anchorLayout->addWidget(topBar);
    anchorLayout->addWidget(sidePanel);
    anchorLayout->addWidget(mainContent);
    anchorLayout->addWidget(statusBar);
}}
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Exemplo de layout com âncoras
#include "uianchorlayout.h"

void createAnchorLayout() {{
    // Criar layout com âncoras
    UIAnchorLayoutPtr anchorLayout = UIAnchorLayout::create();
    
    // Criar widgets
    UIWidgetPtr topBar = g_ui.createWidget("UIWidget");
    UIWidgetPtr sidePanel = g_ui.createWidget("UIWidget");
    UIWidgetPtr mainContent = g_ui.createWidget("UIWidget");
    UIWidgetPtr statusBar = g_ui.createWidget("UIWidget");
    
    // Configurar âncoras
    // Top bar: ancorado no topo, largura total
    anchorLayout->setAnchor(topBar, UIAnchor::Top | UIAnchor::Left | UIAnchor::Right);
    
    // Side panel: ancorado à esquerda, altura entre top bar e status bar
    anchorLayout->setAnchor(sidePanel, UIAnchor::Left | UIAnchor::Top | UIAnchor::Bottom);
    
    // Main content: preenche o espaço restante
    anchorLayout->setAnchor(mainContent, UIAnchor::Top | UIAnchor::Right | UIAnchor::Bottom);
    
    // Status bar: ancorado na parte inferior, largura total
    anchorLayout->setAnchor(statusBar, UIAnchor::Bottom | UIAnchor::Left | UIAnchor::Right);
    
    // Adicionar widgets ao layout
    anchorLayout->addWidget(topBar);
    anchorLayout->addWidget(sidePanel);
    anchorLayout->addWidget(mainContent);
    anchorLayout->addWidget(statusBar);
}}
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

### **Edição de Texto**
Como criar e configurar widgets de edição de texto

#### Nível Basic
```cpp
// Exemplo de edição de texto
#include "uitextedit.h"
#include "uiwidgettext.h"

void createTextWidgets() {{
    // Criar widget de edição de texto
    UITextEditPtr textEdit = UITextEdit::create();
    textEdit->setSize(Size(200, 100));
    textEdit->setText("Digite seu texto aqui...");
    textEdit->setMaxLength(1000);
    textEdit->setReadOnly(false);
    
    // Configurar eventos
    textEdit->onTextChange = [](const std::string& text) {{
        std::cout << "Texto alterado: " << text << std::endl;
    }};
    
    textEdit->onEnterPress = [](const std::string& text) {{
        std::cout << "Enter pressionado: " << text << std::endl;
    }};
    
    // Criar widget de exibição de texto
    UIWidgetTextPtr textDisplay = UIWidgetText::create();
    textDisplay->setSize(Size(200, 50));
    textDisplay->setText("Texto de exemplo");
    textDisplay->setColor(Color::white);
    textDisplay->setFont("Arial", 12);
    
    // Configurar alinhamento
    textDisplay->setTextAlign(UIAlign::Center);
    textDisplay->setVerticalAlign(UIAlign::Middle);
}}
```

#### Nível Intermediate
```cpp
// Exemplo de edição de texto
#include "uitextedit.h"
#include "uiwidgettext.h"

void createTextWidgets() {{
    // Criar widget de edição de texto
    UITextEditPtr textEdit = UITextEdit::create();
    textEdit->setSize(Size(200, 100));
    textEdit->setText("Digite seu texto aqui...");
    textEdit->setMaxLength(1000);
    textEdit->setReadOnly(false);
    
    // Configurar eventos
    textEdit->onTextChange = [](const std::string& text) {{
        std::cout << "Texto alterado: " << text << std::endl;
    }};
    
    textEdit->onEnterPress = [](const std::string& text) {{
        std::cout << "Enter pressionado: " << text << std::endl;
    }};
    
    // Criar widget de exibição de texto
    UIWidgetTextPtr textDisplay = UIWidgetText::create();
    textDisplay->setSize(Size(200, 50));
    textDisplay->setText("Texto de exemplo");
    textDisplay->setColor(Color::white);
    textDisplay->setFont("Arial", 12);
    
    // Configurar alinhamento
    textDisplay->setTextAlign(UIAlign::Center);
    textDisplay->setVerticalAlign(UIAlign::Middle);
}}
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Exemplo de edição de texto
#include "uitextedit.h"
#include "uiwidgettext.h"

void createTextWidgets() {{
    // Criar widget de edição de texto
    UITextEditPtr textEdit = UITextEdit::create();
    textEdit->setSize(Size(200, 100));
    textEdit->setText("Digite seu texto aqui...");
    textEdit->setMaxLength(1000);
    textEdit->setReadOnly(false);
    
    // Configurar eventos
    textEdit->onTextChange = [](const std::string& text) {{
        std::cout << "Texto alterado: " << text << std::endl;
    }};
    
    textEdit->onEnterPress = [](const std::string& text) {{
        std::cout << "Enter pressionado: " << text << std::endl;
    }};
    
    // Criar widget de exibição de texto
    UIWidgetTextPtr textDisplay = UIWidgetText::create();
    textDisplay->setSize(Size(200, 50));
    textDisplay->setText("Texto de exemplo");
    textDisplay->setColor(Color::white);
    textDisplay->setFont("Arial", 12);
    
    // Configurar alinhamento
    textDisplay->setTextAlign(UIAlign::Center);
    textDisplay->setVerticalAlign(UIAlign::Middle);
}}
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

### **Widget de Imagem**
Como criar e configurar widgets de imagem

#### Nível Basic
```cpp
// Exemplo de widget de imagem
#include "uiwidgetimage.h"

void createImageWidget() {{
    // Criar widget de imagem
    UIWidgetImagePtr imageWidget = UIWidgetImage::create();
    imageWidget->setSize(Size(256, 256));
    
    // Carregar imagem
    imageWidget->setImage("data/images/icon.png");
    
    // Configurar propriedades
    imageWidget->setStretched(true);  // Esticar para preencher o widget
    imageWidget->setSmooth(true);     // Suavização de pixels
    imageWidget->setRepeat(false);    // Não repetir a imagem
    
    // Configurar eventos
    imageWidget->onClick = []() {{
        std::cout << "Imagem clicada!" << std::endl;
    }};
    
    imageWidget->onHoverChange = [](bool hovered) {{
        if (hovered) {{
            std::cout << "Mouse sobre a imagem" << std::endl;
        }}
    }};
}}
```

#### Nível Intermediate
```cpp
// Exemplo de widget de imagem
#include "uiwidgetimage.h"

void createImageWidget() {{
    // Criar widget de imagem
    UIWidgetImagePtr imageWidget = UIWidgetImage::create();
    imageWidget->setSize(Size(256, 256));
    
    // Carregar imagem
    imageWidget->setImage("data/images/icon.png");
    
    // Configurar propriedades
    imageWidget->setStretched(true);  // Esticar para preencher o widget
    imageWidget->setSmooth(true);     // Suavização de pixels
    imageWidget->setRepeat(false);    // Não repetir a imagem
    
    // Configurar eventos
    imageWidget->onClick = []() {{
        std::cout << "Imagem clicada!" << std::endl;
    }};
    
    imageWidget->onHoverChange = [](bool hovered) {{
        if (hovered) {{
            std::cout << "Mouse sobre a imagem" << std::endl;
        }}
    }};
}}
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Exemplo de widget de imagem
#include "uiwidgetimage.h"

void createImageWidget() {{
    // Criar widget de imagem
    UIWidgetImagePtr imageWidget = UIWidgetImage::create();
    imageWidget->setSize(Size(256, 256));
    
    // Carregar imagem
    imageWidget->setImage("data/images/icon.png");
    
    // Configurar propriedades
    imageWidget->setStretched(true);  // Esticar para preencher o widget
    imageWidget->setSmooth(true);     // Suavização de pixels
    imageWidget->setRepeat(false);    // Não repetir a imagem
    
    // Configurar eventos
    imageWidget->onClick = []() {{
        std::cout << "Imagem clicada!" << std::endl;
    }};
    
    imageWidget->onHoverChange = [](bool hovered) {{
        if (hovered) {{
            std::cout << "Mouse sobre a imagem" << std::endl;
        }}
    }};
}}
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

### **Sistema de Estilos**
Como aplicar estilos aos widgets

#### Nível Basic
```cpp
// Exemplo de sistema de estilos
#include "uiwidgetbasestyle.h"

void applyStyles() {{
    // Criar widget
    UIWidgetPtr widget = g_ui.createWidget("UIButton");
    
    // Aplicar estilo básico
    UIWidgetBaseStylePtr style = UIWidgetBaseStyle::create();
    
    // Configurar cores
    style->setBackgroundColor(Color::darkBlue);
    style->setBorderColor(Color::white);
    style->setTextColor(Color::white);
    
    // Configurar bordas
    style->setBorderWidth(2);
    style->setBorderRadius(5);
    
    // Configurar padding e margin
    style->setPadding(UIEdge(5, 5, 5, 5));
    style->setMargin(UIEdge(2, 2, 2, 2));
    
    // Aplicar estilo ao widget
    widget->setStyle(style);
    
    // Criar estilo hover
    UIWidgetBaseStylePtr hoverStyle = UIWidgetBaseStyle::create();
    hoverStyle->setBackgroundColor(Color::blue);
    hoverStyle->setBorderColor(Color::yellow);
    
    // Aplicar estilo hover
    widget->setHoverStyle(hoverStyle);
}}
```

#### Nível Intermediate
```cpp
// Exemplo de sistema de estilos
#include "uiwidgetbasestyle.h"

void applyStyles() {{
    // Criar widget
    UIWidgetPtr widget = g_ui.createWidget("UIButton");
    
    // Aplicar estilo básico
    UIWidgetBaseStylePtr style = UIWidgetBaseStyle::create();
    
    // Configurar cores
    style->setBackgroundColor(Color::darkBlue);
    style->setBorderColor(Color::white);
    style->setTextColor(Color::white);
    
    // Configurar bordas
    style->setBorderWidth(2);
    style->setBorderRadius(5);
    
    // Configurar padding e margin
    style->setPadding(UIEdge(5, 5, 5, 5));
    style->setMargin(UIEdge(2, 2, 2, 2));
    
    // Aplicar estilo ao widget
    widget->setStyle(style);
    
    // Criar estilo hover
    UIWidgetBaseStylePtr hoverStyle = UIWidgetBaseStyle::create();
    hoverStyle->setBackgroundColor(Color::blue);
    hoverStyle->setBorderColor(Color::yellow);
    
    // Aplicar estilo hover
    widget->setHoverStyle(hoverStyle);
}}
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Exemplo de sistema de estilos
#include "uiwidgetbasestyle.h"

void applyStyles() {{
    // Criar widget
    UIWidgetPtr widget = g_ui.createWidget("UIButton");
    
    // Aplicar estilo básico
    UIWidgetBaseStylePtr style = UIWidgetBaseStyle::create();
    
    // Configurar cores
    style->setBackgroundColor(Color::darkBlue);
    style->setBorderColor(Color::white);
    style->setTextColor(Color::white);
    
    // Configurar bordas
    style->setBorderWidth(2);
    style->setBorderRadius(5);
    
    // Configurar padding e margin
    style->setPadding(UIEdge(5, 5, 5, 5));
    style->setMargin(UIEdge(2, 2, 2, 2));
    
    // Aplicar estilo ao widget
    widget->setStyle(style);
    
    // Criar estilo hover
    UIWidgetBaseStylePtr hoverStyle = UIWidgetBaseStyle::create();
    hoverStyle->setBackgroundColor(Color::blue);
    hoverStyle->setBorderColor(Color::yellow);
    
    // Aplicar estilo hover
    widget->setHoverStyle(hoverStyle);
}}
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

### **Internacionalização**
Como usar o sistema de tradução

#### Nível Basic
```cpp
// Exemplo de internacionalização
#include "uitranslator.h"

void setupInternationalization() {{
    // Criar tradutor
    UITranslatorPtr translator = UITranslator::create();
    
    // Carregar arquivo de tradução
    translator->loadFile("data/locales/pt_BR.lua");
    
    // Definir idioma
    translator->setLanguage("pt_BR");
    
    // Traduzir texto
    std::string translated = translator->translate("welcome_message");
    std::cout << "Traduzido: " << translated << std::endl;
    
    // Criar widget com texto traduzido
    UIWidgetTextPtr label = UIWidgetText::create();
    label->setText(translator->translate("login_button"));
    
    // Configurar callback para mudança de idioma
    translator->onLanguageChanged = [](const std::string& language) {{
        std::cout << "Idioma alterado para: " << language << std::endl;
        // Atualizar todos os widgets com texto traduzido
        g_ui.updateAllWidgets();
    }};
}}
```

#### Nível Intermediate
```cpp
// Exemplo de internacionalização
#include "uitranslator.h"

void setupInternationalization() {{
    // Criar tradutor
    UITranslatorPtr translator = UITranslator::create();
    
    // Carregar arquivo de tradução
    translator->loadFile("data/locales/pt_BR.lua");
    
    // Definir idioma
    translator->setLanguage("pt_BR");
    
    // Traduzir texto
    std::string translated = translator->translate("welcome_message");
    std::cout << "Traduzido: " << translated << std::endl;
    
    // Criar widget com texto traduzido
    UIWidgetTextPtr label = UIWidgetText::create();
    label->setText(translator->translate("login_button"));
    
    // Configurar callback para mudança de idioma
    translator->onLanguageChanged = [](const std::string& language) {{
        std::cout << "Idioma alterado para: " << language << std::endl;
        // Atualizar todos os widgets com texto traduzido
        g_ui.updateAllWidgets();
    }};
}}
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Exemplo de internacionalização
#include "uitranslator.h"

void setupInternationalization() {{
    // Criar tradutor
    UITranslatorPtr translator = UITranslator::create();
    
    // Carregar arquivo de tradução
    translator->loadFile("data/locales/pt_BR.lua");
    
    // Definir idioma
    translator->setLanguage("pt_BR");
    
    // Traduzir texto
    std::string translated = translator->translate("welcome_message");
    std::cout << "Traduzido: " << translated << std::endl;
    
    // Criar widget com texto traduzido
    UIWidgetTextPtr label = UIWidgetText::create();
    label->setText(translator->translate("login_button"));
    
    // Configurar callback para mudança de idioma
    translator->onLanguageChanged = [](const std::string& language) {{
        std::cout << "Idioma alterado para: " << language << std::endl;
        // Atualizar todos os widgets com texto traduzido
        g_ui.updateAllWidgets();
    }};
}}
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

## 🔗 Pontos de Integração

### **Core Framework**
Integração com sistema core (Application, EventDispatcher)

**Tipo:** dependency
**Arquivos:** ui.h, uimanager.h, uimanager.cpp

### **Graphics System**
Integração com sistema de gráficos para renderização

**Tipo:** integration
**Arquivos:** uiwidget.h, uiwidget.cpp, uiwidgetimage.h, uiwidgetimage.cpp

### **Network System**
Integração com sistema de rede para status de conexão

**Tipo:** integration
**Arquivos:** uiwidget.h, uiwidget.cpp

### **Lua Engine**
Exposição de APIs de UI para scripts Lua

**Tipo:** binding
**Arquivos:** ui.h, uiwidget.h, uimanager.h

### **Resource Management**
Integração com gerenciamento de recursos (imagens, fontes)

**Tipo:** dependency
**Arquivos:** uiwidgetimage.h, uiwidgettext.h

### **Event System**
Integração com sistema de eventos para interações

**Tipo:** integration
**Arquivos:** uiwidget.h, uiwidget.cpp

### **Localization**
Integração com sistema de localização

**Tipo:** integration
**Arquivos:** uitranslator.h, uitranslator.cpp



## 📋 Guia de Uso

### **Criação de Widgets**

#### Nível Basic
```cpp
#include "uiwidget.h"
#include "uimanager.h"

// Criar widget através do gerenciador
UIWidgetPtr widget = g_ui.createWidget("UIWidget");

// Configurar propriedades básicas
widget->setVisible(true);
widget->setEnabled(true);
widget->setSize(Size(100, 50));
widget->setPosition(Point(10, 10));
```

#### Nível Intermediate
```cpp
#include "uiwidget.h"
#include "uimanager.h"

// Criar widget através do gerenciador
UIWidgetPtr widget = g_ui.createWidget("UIWidget");

// Configurar propriedades básicas
widget->setVisible(true);
widget->setEnabled(true);
widget->setSize(Size(100, 50));
widget->setPosition(Point(10, 10));
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
#include "uiwidget.h"
#include "uimanager.h"

// Criar widget através do gerenciador
UIWidgetPtr widget = g_ui.createWidget("UIWidget");

// Configurar propriedades básicas
widget->setVisible(true);
widget->setEnabled(true);
widget->setSize(Size(100, 50));
widget->setPosition(Point(10, 10));
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

### **Sistema de Layouts**

#### Nível Basic
```cpp
#include "uiverticallayout.h"

// Criar layout vertical
UIVerticalLayoutPtr layout = UIVerticalLayout::create();
layout->setSpacing(5);
layout->setAlignment(UIAlign::Center);

// Adicionar widgets
UIWidgetPtr button1 = g_ui.createWidget("UIButton");
UIWidgetPtr button2 = g_ui.createWidget("UIButton");

layout->addWidget(button1);
layout->addWidget(button2);
```

#### Nível Intermediate
```cpp
#include "uiverticallayout.h"

// Criar layout vertical
UIVerticalLayoutPtr layout = UIVerticalLayout::create();
layout->setSpacing(5);
layout->setAlignment(UIAlign::Center);

// Adicionar widgets
UIWidgetPtr button1 = g_ui.createWidget("UIButton");
UIWidgetPtr button2 = g_ui.createWidget("UIButton");

layout->addWidget(button1);
layout->addWidget(button2);
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
#include "uiverticallayout.h"

// Criar layout vertical
UIVerticalLayoutPtr layout = UIVerticalLayout::create();
layout->setSpacing(5);
layout->setAlignment(UIAlign::Center);

// Adicionar widgets
UIWidgetPtr button1 = g_ui.createWidget("UIButton");
UIWidgetPtr button2 = g_ui.createWidget("UIButton");

layout->addWidget(button1);
layout->addWidget(button2);
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

### **Edição de Texto**

#### Nível Basic
```cpp
#include "uitextedit.h"

// Criar widget de edição
UITextEditPtr textEdit = UITextEdit::create();
textEdit->setText("Digite aqui...");
textEdit->setMaxLength(1000);

// Configurar eventos
textEdit->onTextChange = [](const std::string& text) {
    // Processar mudança de texto
};
```

#### Nível Intermediate
```cpp
#include "uitextedit.h"

// Criar widget de edição
UITextEditPtr textEdit = UITextEdit::create();
textEdit->setText("Digite aqui...");
textEdit->setMaxLength(1000);

// Configurar eventos
textEdit->onTextChange = [](const std::string& text) {
    // Processar mudança de texto
};
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
#include "uitextedit.h"

// Criar widget de edição
UITextEditPtr textEdit = UITextEdit::create();
textEdit->setText("Digite aqui...");
textEdit->setMaxLength(1000);

// Configurar eventos
textEdit->onTextChange = [](const std::string& text) {
    // Processar mudança de texto
};
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

## 🎨 Sistema de Layouts

### **Tipos de Layout Disponíveis**

#### **UIVerticalLayout**
- **Organização**: Widgets em coluna vertical
- **Propriedades**: Espaçamento, alinhamento
- **Uso**: Menus, listas, formulários

#### **UIHorizontalLayout**
- **Organização**: Widgets em linha horizontal
- **Propriedades**: Espaçamento, alinhamento
- **Uso**: Barras de ferramentas, controles

#### **UIGridLayout**
- **Organização**: Widgets em grade tabular
- **Propriedades**: Tamanho da grade, espaçamento
- **Uso**: Tabelas, painéis organizados

#### **UIAnchorLayout**
- **Organização**: Widgets ancorados em posições
- **Propriedades**: Âncoras, margens
- **Uso**: Interfaces complexas, responsivas

### **Exemplo de Layout Complexo**

#### Nível Basic
```cpp
// Criar layout principal
UIAnchorLayoutPtr mainLayout = UIAnchorLayout::create();

// Criar componentes
UIWidgetPtr header = g_ui.createWidget("UIWidget");
UIWidgetPtr sidebar = g_ui.createWidget("UIWidget");
UIWidgetPtr content = g_ui.createWidget("UIWidget");
UIWidgetPtr footer = g_ui.createWidget("UIWidget");

// Configurar âncoras
mainLayout->setAnchor(header, UIAnchor::Top | UIAnchor::Left | UIAnchor::Right);
mainLayout->setAnchor(sidebar, UIAnchor::Left | UIAnchor::Top | UIAnchor::Bottom);
mainLayout->setAnchor(content, UIAnchor::Top | UIAnchor::Right | UIAnchor::Bottom);
mainLayout->setAnchor(footer, UIAnchor::Bottom | UIAnchor::Left | UIAnchor::Right);
```

#### Nível Intermediate
```cpp
// Criar layout principal
UIAnchorLayoutPtr mainLayout = UIAnchorLayout::create();

// Criar componentes
UIWidgetPtr header = g_ui.createWidget("UIWidget");
UIWidgetPtr sidebar = g_ui.createWidget("UIWidget");
UIWidgetPtr content = g_ui.createWidget("UIWidget");
UIWidgetPtr footer = g_ui.createWidget("UIWidget");

// Configurar âncoras
mainLayout->setAnchor(header, UIAnchor::Top | UIAnchor::Left | UIAnchor::Right);
mainLayout->setAnchor(sidebar, UIAnchor::Left | UIAnchor::Top | UIAnchor::Bottom);
mainLayout->setAnchor(content, UIAnchor::Top | UIAnchor::Right | UIAnchor::Bottom);
mainLayout->setAnchor(footer, UIAnchor::Bottom | UIAnchor::Left | UIAnchor::Right);
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Criar layout principal
UIAnchorLayoutPtr mainLayout = UIAnchorLayout::create();

// Criar componentes
UIWidgetPtr header = g_ui.createWidget("UIWidget");
UIWidgetPtr sidebar = g_ui.createWidget("UIWidget");
UIWidgetPtr content = g_ui.createWidget("UIWidget");
UIWidgetPtr footer = g_ui.createWidget("UIWidget");

// Configurar âncoras
mainLayout->setAnchor(header, UIAnchor::Top | UIAnchor::Left | UIAnchor::Right);
mainLayout->setAnchor(sidebar, UIAnchor::Left | UIAnchor::Top | UIAnchor::Bottom);
mainLayout->setAnchor(content, UIAnchor::Top | UIAnchor::Right | UIAnchor::Bottom);
mainLayout->setAnchor(footer, UIAnchor::Bottom | UIAnchor::Left | UIAnchor::Right);
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

## 🎭 Sistema de Estilos

### **UIWidgetBaseStyle**
- **Cores**: Background, borda, texto
- **Bordas**: Largura, raio, estilo
- **Espaçamento**: Padding, margin
- **Estados**: Normal, hover, pressed, disabled

### **Aplicação de Estilos**

#### Nível Basic
```cpp
// Criar estilo
UIWidgetBaseStylePtr style = UIWidgetBaseStyle::create();
style->setBackgroundColor(Color::darkBlue);
style->setBorderColor(Color::white);
style->setBorderWidth(2);
style->setBorderRadius(5);

// Aplicar ao widget
widget->setStyle(style);
```

#### Nível Intermediate
```cpp
// Criar estilo
UIWidgetBaseStylePtr style = UIWidgetBaseStyle::create();
style->setBackgroundColor(Color::darkBlue);
style->setBorderColor(Color::white);
style->setBorderWidth(2);
style->setBorderRadius(5);

// Aplicar ao widget
widget->setStyle(style);
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Criar estilo
UIWidgetBaseStylePtr style = UIWidgetBaseStyle::create();
style->setBackgroundColor(Color::darkBlue);
style->setBorderColor(Color::white);
style->setBorderWidth(2);
style->setBorderRadius(5);

// Aplicar ao widget
widget->setStyle(style);
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

## 🌐 Internacionalização

### **UITranslator**
- **Carregamento**: Arquivos de tradução Lua
- **Idiomas**: Suporte a múltiplos idiomas
- **Eventos**: Mudança de idioma em tempo real
- **Fallback**: Texto padrão quando tradução não encontrada

### **Uso do Sistema de Tradução**

#### Nível Basic
```cpp
// Configurar tradutor
UITranslatorPtr translator = UITranslator::create();
translator->loadFile("data/locales/pt_BR.lua");
translator->setLanguage("pt_BR");

// Traduzir texto
std::string translated = translator->translate("welcome_message");
```

#### Nível Intermediate
```cpp
// Configurar tradutor
UITranslatorPtr translator = UITranslator::create();
translator->loadFile("data/locales/pt_BR.lua");
translator->setLanguage("pt_BR");

// Traduzir texto
std::string translated = translator->translate("welcome_message");
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Configurar tradutor
UITranslatorPtr translator = UITranslator::create();
translator->loadFile("data/locales/pt_BR.lua");
translator->setLanguage("pt_BR");

// Traduzir texto
std::string translated = translator->translate("welcome_message");
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

## 🖼️ Widgets Especializados

### **UIWidgetText**
- **Funcionalidades**: Exibição de texto
- **Propriedades**: Fonte, cor, alinhamento
- **Eventos**: Clique, hover

### **UIWidgetImage**
- **Funcionalidades**: Exibição de imagens
- **Propriedades**: Esticar, suavizar, repetir
- **Formatos**: PNG, JPG, GIF

### **UITextEdit**
- **Funcionalidades**: Edição de texto
- **Propriedades**: Máximo de caracteres, somente leitura
- **Eventos**: Mudança de texto, pressionar Enter

### **UIQRCode**
- **Funcionalidades**: Geração de códigos QR
- **Propriedades**: Dados, tamanho, correção de erro
- **Uso**: Compartilhamento de informações

### **UIParticles**
- **Funcionalidades**: Sistema de partículas
- **Propriedades**: Tipo, velocidade, vida útil
- **Uso**: Efeitos visuais, animações

## 📱 Responsividade

### **Sistema de Âncoras**
- **Flexibilidade**: Adaptação automática a diferentes resoluções
- **Precisão**: Posicionamento exato baseado em âncoras
- **Performance**: Cálculos otimizados de layout

### **Breakpoints**
- **Mobile**: Layouts adaptados para telas pequenas
- **Tablet**: Layouts intermediários
- **Desktop**: Layouts completos

## 🎯 Eventos e Interações

### **Tipos de Eventos**
- **Mouse**: Clique, duplo clique, hover, drag
- **Teclado**: Pressionar tecla, digitar
- **Foco**: Ganhar/perder foco
- **Redimensionamento**: Mudança de tamanho

### **Sistema de Callbacks**

#### Nível Basic
```cpp
// Configurar eventos
widget->onClick = []() {
    std::cout << "Widget clicado!" << std::endl;
};

widget->onHoverChange = [](bool hovered) {
    if (hovered) {
        widget->setStyle(hoverStyle);
    } else {
        widget->setStyle(normalStyle);
    }
};
```

#### Nível Intermediate
```cpp
// Configurar eventos
widget->onClick = []() {
    std::cout << "Widget clicado!" << std::endl;
};

widget->onHoverChange = [](bool hovered) {
    if (hovered) {
        widget->setStyle(hoverStyle);
    } else {
        widget->setStyle(normalStyle);
    }
};
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Configurar eventos
widget->onClick = []() {
    std::cout << "Widget clicado!" << std::endl;
};

widget->onHoverChange = [](bool hovered) {
    if (hovered) {
        widget->setStyle(hoverStyle);
    } else {
        widget->setStyle(normalStyle);
    }
};
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

## 🔧 Performance

### **Otimizações**
- **Lazy Loading**: Carregamento sob demanda
- **Caching**: Cache de estilos e recursos
- **Batching**: Agrupamento de operações de renderização
- **Dirty Checking**: Atualização apenas quando necessário

### **Métricas**
- **Renderização**: < 16ms por frame (60 FPS)
- **Memória**: < 50MB para interface complexa
- **CPU**: < 10% para interface normal
- **GPU**: Aceleração por hardware quando disponível

## 🚀 Próximos Passos

1. **Análise de Performance**: Profiling de UI
2. **Otimizações Avançadas**: Técnicas de otimização
3. **Integração com Canary**: Preparação para servidor
4. **Documentação de API**: Referência completa

---

*Análise gerada automaticamente pelo sistema Habdel - 2025-07-31 14:26:41*
