---
tags: [ui, graphics, charts, system, otclient, documentation, habdel]
type: documentation
status: completed
priority: maximum
created: 2025-01-27
---

# 📊 UI-018: Sistema de Gráficos e Charts

> [!info] **Story ID**: UI-018  
> **Categoria**: UI  
> **Status**: ✅ Completo  
> **Prioridade**: 🔥 **MÁXIMA**

## 📋 Índice
1. [Visão Geral](#visão-geral)
2. [Arquitetura do Sistema](#arquitetura-do-sistema)
3. [Tipos de Gráficos](#tipos-de-gráficos)
4. [Sistema de Renderização](#sistema-de-renderização)
5. [API Lua](#api-lua)
6. [UIGraphicsWidget](#uigraphicswidget)
7. [Tipos de Charts](#tipos-de-charts)
8. [Exemplos Práticos](#exemplos-práticos)
9. [Melhores Práticas](#melhores-práticas)
10. [Performance e Otimização](#performance-e-otimização)

---

## 🎯 Visão Geral

O **Sistema de Gráficos e Charts** do OTClient oferece funcionalidades avançadas para criar visualizações de dados, incluindo gráficos de linha, barras, pizza e outros tipos de charts. O sistema é fundamental para interfaces que precisam exibir dados estatísticos e análises visuais.

### 🎨 **Características Principais**

- **UIGraphicsWidget**: Widget especializado para renderização de gráficos
- **Múltiplos Tipos de Charts**: Linha, barra, pizza, área, dispersão
- **Sistema de Coordenadas**: Sistema de coordenadas 2D para posicionamento
- **Animações**: Transições suaves entre estados de dados
- **Interatividade**: Hover, clique e zoom nos gráficos
- **Performance Otimizada**: Renderização eficiente com OpenGL

---

## 🏗️ Arquitetura do Sistema

### 🎭 **Estrutura Hierárquica**

```
Sistema de Gráficos e Charts
   │
   ├─ UIGraphicsWidget
   │   ├─ Canvas de Renderização
   │   ├─ Sistema de Coordenadas
   │   ├─ Contexto de Desenho
   │   ├─ Transformações
   │   └─ Eventos de Interação
   │
   ├─ Tipos de Charts
   │   ├─ LineChart (Gráfico de Linha)
   │   ├─ BarChart (Gráfico de Barras)
   │   ├─ PieChart (Gráfico de Pizza)
   │   ├─ AreaChart (Gráfico de Área)
   │   └─ ScatterChart (Gráfico de Dispersão)
   │
   ├─ Sistema de Dados
   │   ├─ DataSeries
   │   ├─ DataPoints
   │   ├─ Axes (Eixos)
   │   └─ Legends (Legendas)
   │
   └─ Sistema Visual
       ├─ Cores e Estilos
       ├─ Fontes e Texto
       ├─ Gradientes
       └─ Animações
```

### 🔄 **Fluxo de Renderização**

```
1. Configuração do Widget
   ↓
2. Definição de Dados
   ↓
3. Configuração de Eixos
   ↓
4. Cálculo de Coordenadas
   ↓
5. Renderização de Elementos
   ↓
6. Aplicação de Estilos
   ↓
7. Eventos de Interação
```

---

## 📊 Tipos de Gráficos

### 🎯 **LineChart (Gráfico de Linha)**

Gráfico que conecta pontos de dados com linhas.

```lua
-- Estrutura do LineChart
    --  Estrutura do LineChart (traduzido)
{
    type = 'line',
    data = {
        {x = 1, y = 10},
        {x = 2, y = 15},
        {x = 3, y = 8},
        {x = 4, y = 20}
    },
    style = {
        lineColor = '#2196F3',
        lineWidth = 2,
        pointColor = '#FF5722',
        pointSize = 4
    }
}
```

### 📊 **BarChart (Gráfico de Barras)**

Gráfico que representa dados com barras verticais ou horizontais.

```lua
-- Estrutura do BarChart
    --  Estrutura do BarChart (traduzido)
{
    type = 'bar',
    data = {
        {label = 'Jan', value = 100},
        {label = 'Fev', value = 150},
        {label = 'Mar', value = 120},
        {label = 'Abr', value = 200}
    },
    style = {
        barColor = '#4CAF50',
        barWidth = 30,
        barSpacing = 10,
        orientation = 'vertical'
    }
}
```

### 🥧 **PieChart (Gráfico de Pizza)**

Gráfico circular que representa proporções de um todo.

```lua
-- Estrutura do PieChart
    --  Estrutura do PieChart (traduzido)
{
    type = 'pie',
    data = {
        {label = 'Red', value = 30, color = '#F44336'},
        {label = 'Blue', value = 25, color = '#2196F3'},
        {label = 'Green', value = 20, color = '#4CAF50'},
        {label = 'Yellow', value = 25, color = '#FFC107'}
    },
    style = {
        centerX = 200,
        centerY = 200,
        radius = 100,
        showLabels = true
    }
}
```

### 📈 **AreaChart (Gráfico de Área)**

Gráfico de linha com área preenchida abaixo da linha.

```lua
-- Estrutura do AreaChart
    --  Estrutura do AreaChart (traduzido)
{
    type = 'area',
    data = {
        {x = 1, y = 10},
        {x = 2, y = 15},
        {x = 3, y = 8},
        {x = 4, y = 20}
    },
    style = {
        fillColor = '#2196F3',
        fillOpacity = 0.3,
        lineColor = '#1976D2',
        lineWidth = 2
    }
}
```

### 🔵 **ScatterChart (Gráfico de Dispersão)**

Gráfico que mostra correlação entre duas variáveis.

```lua
-- Estrutura do ScatterChart
    --  Estrutura do ScatterChart (traduzido)
{
    type = 'scatter',
    data = {
        {x = 1, y = 5},
        {x = 2, y = 8},
        {x = 3, y = 12},
        {x = 4, y = 7}
    },
    style = {
        pointColor = '#FF5722',
        pointSize = 6,
        showTrendLine = true,
        trendLineColor = '#2196F3'
    }
}
```

---

## 🎨 Sistema de Renderização

### 🎯 **Sistema de Coordenadas**

```lua
-- Sistema de coordenadas 2D
    --  Sistema de coordenadas 2D (traduzido)
local CoordinateSystem = {
    -- Coordenadas do widget
    --  Coordenadas do widget (traduzido)
    widgetX = 0,
    widgetY = 0,
    widgetWidth = 400,
    widgetHeight = 300,
    
    -- Coordenadas dos dados
    --  Coordenadas dos dados (traduzido)
    dataMinX = 0,
    dataMaxX = 100,
    dataMinY = 0,
    dataMaxY = 100,
    
    -- Margens
    --  Margens (traduzido)
    marginLeft = 50,
    marginRight = 20,
    marginTop = 20,
    marginBottom = 50
}

-- Converter coordenadas de dados para pixels
    --  Converter coordenadas de dados para pixels (traduzido)
function CoordinateSystem.dataToPixel(x, y)
    -- Função: CoordinateSystem
    local pixelX = CoordinateSystem.marginLeft + 
        (x - CoordinateSystem.dataMinX) / 
        (CoordinateSystem.dataMaxX - CoordinateSystem.dataMinX) * 
        (CoordinateSystem.widgetWidth - CoordinateSystem.marginLeft - CoordinateSystem.marginRight)
    
    local pixelY = CoordinateSystem.widgetHeight - CoordinateSystem.marginBottom - 
        (y - CoordinateSystem.dataMinY) / 
        (CoordinateSystem.dataMaxY - CoordinateSystem.dataMinY) * 
        (CoordinateSystem.widgetHeight - CoordinateSystem.marginTop - CoordinateSystem.marginBottom)
    
    return pixelX, pixelY
end

-- Converter coordenadas de pixels para dados
    --  Converter coordenadas de pixels para dados (traduzido)
function CoordinateSystem.pixelToData(pixelX, pixelY)
    -- Função: CoordinateSystem
    local x = CoordinateSystem.dataMinX + 
        (pixelX - CoordinateSystem.marginLeft) / 
        (CoordinateSystem.widgetWidth - CoordinateSystem.marginLeft - CoordinateSystem.marginRight) * 
        (CoordinateSystem.dataMaxX - CoordinateSystem.dataMinX)
    
    local y = CoordinateSystem.dataMaxY - 
        (pixelY - CoordinateSystem.marginTop) / 
        (CoordinateSystem.widgetHeight - CoordinateSystem.marginTop - CoordinateSystem.marginBottom) * 
        (CoordinateSystem.dataMaxY - CoordinateSystem.dataMinY)
    
    return x, y
end
```

### 🎨 **Contexto de Desenho**

```lua
-- Contexto de desenho para gráficos
local GraphicsContext = {
    widget = nil,
    canvas = nil
}

function GraphicsContext.create(widget)
    -- Função: GraphicsContext
    local context = {
        widget = widget,
        canvas = widget:getCanvas()
    }
    
    return context
end

function GraphicsContext:setColor(color)
    -- Função: GraphicsContext
    self.canvas:setColor(color)
end

function GraphicsContext:setLineWidth(width)
    -- Função: GraphicsContext
    self.canvas:setLineWidth(width)
end

function GraphicsContext:drawLine(x1, y1, x2, y2)
    -- Função: GraphicsContext
    self.canvas:drawLine(x1, y1, x2, y2)
end

function GraphicsContext:drawRectangle(x, y, width, height)
    -- Função: GraphicsContext
    self.canvas:drawRectangle(x, y, width, height)
end

function GraphicsContext:drawCircle(x, y, radius)
    -- Função: GraphicsContext
    self.canvas:drawCircle(x, y, radius)
end

function GraphicsContext:drawText(text, x, y)
    -- Função: GraphicsContext
    self.canvas:drawText(text, x, y)
end

function GraphicsContext:fillRectangle(x, y, width, height)
    -- Função: GraphicsContext
    self.canvas:fillRectangle(x, y, width, height)
end

function GraphicsContext:fillCircle(x, y, radius)
    -- Função: GraphicsContext
    self.canvas:fillCircle(x, y, radius)
end
```

---

## 🐍 API Lua

### 📦 **Métodos de UIGraphicsWidget**

```lua
-- Criar widget de gráficos
local graphicsWidget = g_ui.createWidget('UIGraphicsWidget', parent)

-- Configurar tamanho
    --  Configurar tamanho (traduzido)
graphicsWidget:setSize({width = 400, height = 300})

-- Configurar dados
    --  Configurar dados (traduzido)
graphicsWidget:setData(chartData)

-- Configurar estilo
    --  Configurar estilo (traduzido)
graphicsWidget:setStyle(chartStyle)

-- Renderizar gráfico
graphicsWidget:render()

-- Eventos
    --  Eventos (traduzido)
graphicsWidget.onMouseMove = function(widget, mousePos)
    -- Implementar hover
    --  Implementar hover (traduzido)
end

graphicsWidget.onClick = function(widget, mousePos)
    -- Implementar clique
    --  Implementar clique (traduzido)
end

-- Propriedades
    --  Propriedades (traduzido)
graphicsWidget:getCanvas()
graphicsWidget:getData()
graphicsWidget:getStyle()
```

### 🎯 **Métodos de Charts**

#### Nível Basic
```lua
-- Criar gráfico de linha
local lineChart = LineChart.create(parent, data, style)

-- Criar gráfico de barras
local barChart = BarChart.create(parent, data, style)

-- Criar gráfico de pizza
local pieChart = PieChart.create(parent, data, style)

-- Atualizar dados
chart:updateData(newData)

-- Animar transição
chart:animateTo(newData, duration)

-- Exportar como imagem
chart:exportToImage(filename)
```

#### Nível Intermediate
```lua
-- Criar gráfico de linha
local lineChart = LineChart.create(parent, data, style)

-- Criar gráfico de barras
local barChart = BarChart.create(parent, data, style)

-- Criar gráfico de pizza
local pieChart = PieChart.create(parent, data, style)

-- Atualizar dados
chart:updateData(newData)

-- Animar transição
chart:animateTo(newData, duration)

-- Exportar como imagem
chart:exportToImage(filename)
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
-- Criar gráfico de linha
local lineChart = LineChart.create(parent, data, style)

-- Criar gráfico de barras
local barChart = BarChart.create(parent, data, style)

-- Criar gráfico de pizza
local pieChart = PieChart.create(parent, data, style)

-- Atualizar dados
chart:updateData(newData)

-- Animar transição
chart:animateTo(newData, duration)

-- Exportar como imagem
chart:exportToImage(filename)
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

### 📄 **Métodos de Sistema de Dados**

#### Nível Basic
```lua
-- Criar série de dados
local dataSeries = DataSeries.create()

-- Adicionar ponto
dataSeries:addPoint(x, y)

-- Adicionar múltiplos pontos
dataSeries:addPoints(points)

-- Obter estatísticas
dataSeries:getMin()
dataSeries:getMax()
dataSeries:getAverage()

-- Filtrar dados
dataSeries:filter(predicate)

-- Ordenar dados
dataSeries:sort(comparator)
```

#### Nível Intermediate
```lua
-- Criar série de dados
local dataSeries = DataSeries.create()

-- Adicionar ponto
dataSeries:addPoint(x, y)

-- Adicionar múltiplos pontos
dataSeries:addPoints(points)

-- Obter estatísticas
dataSeries:getMin()
dataSeries:getMax()
dataSeries:getAverage()

-- Filtrar dados
dataSeries:filter(predicate)

-- Ordenar dados
dataSeries:sort(comparator)
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
-- Criar série de dados
local dataSeries = DataSeries.create()

-- Adicionar ponto
dataSeries:addPoint(x, y)

-- Adicionar múltiplos pontos
dataSeries:addPoints(points)

-- Obter estatísticas
dataSeries:getMin()
dataSeries:getMax()
dataSeries:getAverage()

-- Filtrar dados
dataSeries:filter(predicate)

-- Ordenar dados
dataSeries:sort(comparator)
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

---

## 📊 UIGraphicsWidget

### 🎯 **Implementação Básica**

```lua
-- Criar widget de gráficos básico
local graphicsWidget = g_ui.createWidget('UIGraphicsWidget', parent)
graphicsWidget:setId('myChart')
graphicsWidget:setSize({width = 400, height = 300})

-- Configurar dados
    --  Configurar dados (traduzido)
local chartData = {
    type = 'line',
    data = {
        {x = 1, y = 10},
        {x = 2, y = 15},
        {x = 3, y = 8},
        {x = 4, y = 20},
        {x = 5, y = 12}
    }
}

-- Configurar estilo
    --  Configurar estilo (traduzido)
local chartStyle = {
    backgroundColor = '#FFFFFF',
    lineColor = '#2196F3',
    lineWidth = 2,
    pointColor = '#FF5722',
    pointSize = 4,
    showGrid = true,
    gridColor = '#E0E0E0',
    showAxes = true,
    axisColor = '#000000'
}

-- Aplicar configurações
graphicsWidget:setData(chartData)
graphicsWidget:setStyle(chartStyle)

-- Renderizar
    --  Renderizar (traduzido)
graphicsWidget:render()
```

### 🎨 **Implementação Avançada**

#### Inicialização e Configuração
```lua
-- Sistema de gráficos avançado
local AdvancedGraphics = {}

function AdvancedGraphics.create(parent, config)
    local graphicsWidget = g_ui.createWidget('UIGraphicsWidget', parent)
    graphicsWidget:setId(config.id or 'advancedChart')
    graphicsWidget:setSize(config.size or {width = 400, height = 300})
    
    -- Configurar dados e estilo
    graphicsWidget:setData(config.data or {})
    graphicsWidget:setStyle(config.style or {})
    
    -- Configurar eventos
    graphicsWidget.onMouseMove = function(widget, mousePos)
        AdvancedGraphics.handleMouseMove(widget, mousePos)
    end
    
    graphicsWidget.onClick = function(widget, mousePos)
        AdvancedGraphics.handleClick(widget, mousePos)
    end
    
    graphicsWidget.onRender = function(widget)
        AdvancedGraphics.customRender(widget)
    end
```

#### Funcionalidade 1
```lua
    
    -- Renderizar inicialmente
    graphicsWidget:render()
    
    return graphicsWidget
end

function AdvancedGraphics.handleMouseMove(widget, mousePos)
    local data = widget:getData()
    local style = widget:getStyle()
    
    -- Implementar tooltip
    local tooltipData = AdvancedGraphics.getTooltipData(widget, mousePos)
    if tooltipData then
        AdvancedGraphics.showTooltip(widget, tooltipData, mousePos)
    else
        AdvancedGraphics.hideTooltip(widget)
    end
end

function AdvancedGraphics.handleClick(widget, mousePos)
```

#### Funcionalidade 2
```lua
    local clickedData = AdvancedGraphics.getClickedData(widget, mousePos)
    if clickedData then
        print('Clicado em:', clickedData)
        -- Implementar ação de clique
    end
end

function AdvancedGraphics.customRender(widget)
    local canvas = widget:getCanvas()
    local data = widget:getData()
    local style = widget:getStyle()
    
    -- Renderização customizada baseada no tipo
    if data.type == 'line' then
        AdvancedGraphics.renderLineChart(canvas, data, style)
    elseif data.type == 'bar' then
        AdvancedGraphics.renderBarChart(canvas, data, style)
    elseif data.type == 'pie' then
        AdvancedGraphics.renderPieChart(canvas, data, style)
    end
end
```

#### Funcionalidade 3
```lua

function AdvancedGraphics.renderLineChart(canvas, data, style)
    -- Configurar estilo
    canvas:setColor(style.lineColor or '#2196F3')
    canvas:setLineWidth(style.lineWidth or 2)
    
    -- Desenhar linhas
    for i = 1, #data.data - 1 do
        local point1 = data.data[i]
        local point2 = data.data[i + 1]
        
        local x1, y1 = AdvancedGraphics.dataToPixel(point1.x, point1.y)
        local x2, y2 = AdvancedGraphics.dataToPixel(point2.x, point2.y)
        
        canvas:drawLine(x1, y1, x2, y2)
    end
    
    -- Desenhar pontos
    canvas:setColor(style.pointColor or '#FF5722')
    for _, point in ipairs(data.data) do
        local x, y = AdvancedGraphics.dataToPixel(point.x, point.y)
        canvas:fillCircle(x, y, style.pointSize or 4)
    end
```

#### Funcionalidade 4
```lua
end

function AdvancedGraphics.renderBarChart(canvas, data, style)
    local barWidth = style.barWidth or 30
    local barSpacing = style.barSpacing or 10
    local barColor = style.barColor or '#4CAF50'
    
    canvas:setColor(barColor)
    
    for i, bar in ipairs(data.data) do
        local x = AdvancedGraphics.marginLeft + (i - 1) * (barWidth + barSpacing)
        local y = AdvancedGraphics.dataToPixel(0, bar.value)
        local height = AdvancedGraphics.widgetHeight - AdvancedGraphics.marginBottom - y
        
        canvas:fillRectangle(x, y, barWidth, height)
    end
end

function AdvancedGraphics.renderPieChart(canvas, data, style)
    local centerX = style.centerX or 200
    local centerY = style.centerY or 200
    local radius = style.radius or 100
    
    local total = 0
    for _, slice in ipairs(data.data) do
        total = total + slice.value
    end
```

#### Funcionalidade 5
```lua
    
    local currentAngle = 0
    for _, slice in ipairs(data.data) do
        local sliceAngle = (slice.value / total) * 2 * math.pi
        
        canvas:setColor(slice.color)
        canvas:fillPieSlice(centerX, centerY, radius, currentAngle, currentAngle + sliceAngle)
        
        currentAngle = currentAngle + sliceAngle
    end
end

function AdvancedGraphics.dataToPixel(x, y)
    -- Implementar conversão de coordenadas
    return x * 4, 300 - y * 3  -- Exemplo simplificado
end

function AdvancedGraphics.getTooltipData(widget, mousePos)
    -- Implementar detecção de tooltip
    return nil
end
```

#### Funcionalidade 6
```lua

function AdvancedGraphics.showTooltip(widget, data, pos)
    -- Implementar exibição de tooltip
end

function AdvancedGraphics.hideTooltip(widget)
    -- Implementar ocultação de tooltip
end

function AdvancedGraphics.getClickedData(widget, mousePos)
    -- Implementar detecção de clique
    return nil
end

-- Uso
local chartConfig = {
    id = 'myChart',
    size = {width = 500, height = 400},
    data = {
        type = 'line',
        data = {
            {x = 1, y = 10},
            {x = 2, y = 15},
            {x = 3, y = 8},
            {x = 4, y = 20}
        }
```

#### Finalização
```lua
    },
    style = {
        lineColor = '#2196F3',
        lineWidth = 3,
        pointColor = '#FF5722',
        pointSize = 5
    }
}

local chart = AdvancedGraphics.create(parent, chartConfig)
```

---

## 📈 Tipos de Charts

### 🎯 **LineChart**

#### Inicialização e Configuração
```lua
-- Implementação de gráfico de linha
local LineChart = {}

function LineChart.create(parent, data, style)
    local widget = g_ui.createWidget('UIGraphicsWidget', parent)
    widget:setId('lineChart')
    
    -- Configurar dados
    local chartData = {
        type = 'line',
        data = data or {}
    }
    
    -- Configurar estilo padrão
    local chartStyle = {
        backgroundColor = '#FFFFFF',
        lineColor = '#2196F3',
        lineWidth = 2,
        pointColor = '#FF5722',
        pointSize = 4,
        showGrid = true,
        gridColor = '#E0E0E0',
        showAxes = true,
        axisColor = '#000000',
        showLabels = true,
        labelColor = '#666666'
    }
```

#### Funcionalidade 1
```lua
    
    -- Mesclar com estilo customizado
    if style then
        for key, value in pairs(style) do
            chartStyle[key] = value
        end
    end
    
    widget:setData(chartData)
    widget:setStyle(chartStyle)
    
    -- Configurar renderização customizada
    widget.onRender = function(widget)
        LineChart.render(widget)
    end
    
    widget:render()
    return widget
end

function LineChart.render(widget)
```

#### Funcionalidade 2
```lua
    local canvas = widget:getCanvas()
    local data = widget:getData()
    local style = widget:getStyle()
    
    -- Limpar canvas
    canvas:setColor(style.backgroundColor)
    canvas:fillRectangle(0, 0, widget:getWidth(), widget:getHeight())
    
    -- Desenhar grade
    if style.showGrid then
        LineChart.drawGrid(canvas, style)
    end
    
    -- Desenhar eixos
    if style.showAxes then
        LineChart.drawAxes(canvas, style)
    end
    
    -- Desenhar linha
    canvas:setColor(style.lineColor)
    canvas:setLineWidth(style.lineWidth)
    
    for i = 1, #data.data - 1 do
        local point1 = data.data[i]
        local point2 = data.data[i + 1]
        
        local x1, y1 = LineChart.dataToPixel(widget, point1.x, point1.y)
        local x2, y2 = LineChart.dataToPixel(widget, point2.x, point2.y)
        
        canvas:drawLine(x1, y1, x2, y2)
    end
```

#### Funcionalidade 3
```lua
    
    -- Desenhar pontos
    canvas:setColor(style.pointColor)
    for _, point in ipairs(data.data) do
        local x, y = LineChart.dataToPixel(widget, point.x, point.y)
        canvas:fillCircle(x, y, style.pointSize)
    end
    
    -- Desenhar labels
    if style.showLabels then
        LineChart.drawLabels(canvas, data, style)
    end
end

function LineChart.drawGrid(canvas, style)
    canvas:setColor(style.gridColor)
    canvas:setLineWidth(1)
    
    -- Linhas horizontais
    for y = 0, 10 do
        local pixelY = y * 30
        canvas:drawLine(50, pixelY, 350, pixelY)
    end
```

#### Funcionalidade 4
```lua
    
    -- Linhas verticais
    for x = 0, 10 do
        local pixelX = 50 + x * 30
        canvas:drawLine(pixelX, 0, pixelX, 300)
    end
end

function LineChart.drawAxes(canvas, style)
    canvas:setColor(style.axisColor)
    canvas:setLineWidth(2)
    
    -- Eixo X
    canvas:drawLine(50, 250, 350, 250)
    
    -- Eixo Y
    canvas:drawLine(50, 50, 50, 250)
end

function LineChart.drawLabels(canvas, data, style)
    canvas:setColor(style.labelColor)
    
    for i, point in ipairs(data.data) do
        local x, y = LineChart.dataToPixel(widget, point.x, point.y)
        canvas:drawText(tostring(point.y), x + 5, y - 5)
    end
```

#### Funcionalidade 5
```lua
end

function LineChart.dataToPixel(widget, x, y)
    -- Implementar conversão de coordenadas
    local pixelX = 50 + x * 30
    local pixelY = 250 - y * 2
    return pixelX, pixelY
end

-- Uso
local lineData = {
    {x = 1, y = 10},
    {x = 2, y = 15},
    {x = 3, y = 8},
    {x = 4, y = 20},
    {x = 5, y = 12}
}

local lineStyle = {
    lineColor = '#2196F3',
    lineWidth = 3,
    pointColor = '#FF5722',
    pointSize = 5
}
```

#### Finalização
```lua

local lineChart = LineChart.create(parent, lineData, lineStyle)
```

### 📊 **BarChart**

#### Inicialização e Configuração
```lua
-- Implementação de gráfico de barras
local BarChart = {}

function BarChart.create(parent, data, style)
    local widget = g_ui.createWidget('UIGraphicsWidget', parent)
    widget:setId('barChart')
    
    -- Configurar dados
    local chartData = {
        type = 'bar',
        data = data or {}
    }
    
    -- Configurar estilo padrão
    local chartStyle = {
        backgroundColor = '#FFFFFF',
        barColor = '#4CAF50',
        barWidth = 30,
        barSpacing = 10,
        orientation = 'vertical',
        showGrid = true,
        gridColor = '#E0E0E0',
        showAxes = true,
        axisColor = '#000000',
        showLabels = true,
        labelColor = '#666666'
    }
```

#### Funcionalidade 1
```lua
    
    -- Mesclar com estilo customizado
    if style then
        for key, value in pairs(style) do
            chartStyle[key] = value
        end
    end
    
    widget:setData(chartData)
    widget:setStyle(chartStyle)
    
    -- Configurar renderização customizada
    widget.onRender = function(widget)
        BarChart.render(widget)
    end
    
    widget:render()
    return widget
end

function BarChart.render(widget)
```

#### Funcionalidade 2
```lua
    local canvas = widget:getCanvas()
    local data = widget:getData()
    local style = widget:getStyle()
    
    -- Limpar canvas
    canvas:setColor(style.backgroundColor)
    canvas:fillRectangle(0, 0, widget:getWidth(), widget:getHeight())
    
    -- Desenhar grade
    if style.showGrid then
        BarChart.drawGrid(canvas, style)
    end
    
    -- Desenhar eixos
    if style.showAxes then
        BarChart.drawAxes(canvas, style)
    end
    
    -- Desenhar barras
    canvas:setColor(style.barColor)
    
    for i, bar in ipairs(data.data) do
        local x, y, width, height = BarChart.calculateBar(widget, i, bar, style)
        canvas:fillRectangle(x, y, width, height)
    end
```

#### Funcionalidade 3
```lua
    
    -- Desenhar labels
    if style.showLabels then
        BarChart.drawLabels(canvas, data, style)
    end
end

function BarChart.calculateBar(widget, index, bar, style)
    local barWidth = style.barWidth
    local barSpacing = style.barSpacing
    local maxValue = BarChart.getMaxValue(widget:getData().data)
    
    local x = 80 + (index - 1) * (barWidth + barSpacing)
    local y = 250 - (bar.value / maxValue) * 200
    local width = barWidth
    local height = (bar.value / maxValue) * 200
    
    return x, y, width, height
end

function BarChart.getMaxValue(data)
```

#### Funcionalidade 4
```lua
    local max = 0
    for _, bar in ipairs(data) do
        if bar.value > max then
            max = bar.value
        end
    end
    return max
end

function BarChart.drawGrid(canvas, style)
    canvas:setColor(style.gridColor)
    canvas:setLineWidth(1)
    
    -- Linhas horizontais
    for y = 0, 10 do
        local pixelY = 50 + y * 20
        canvas:drawLine(80, pixelY, 380, pixelY)
    end
end

function BarChart.drawAxes(canvas, style)
```

#### Funcionalidade 5
```lua
    canvas:setColor(style.axisColor)
    canvas:setLineWidth(2)
    
    -- Eixo X
    canvas:drawLine(80, 250, 380, 250)
    
    -- Eixo Y
    canvas:drawLine(80, 50, 80, 250)
end

function BarChart.drawLabels(canvas, data, style)
    canvas:setColor(style.labelColor)
    
    for i, bar in ipairs(data.data) do
        local x, y, width, height = BarChart.calculateBar(widget, i, bar, style)
        canvas:drawText(bar.label, x, y + height + 15)
        canvas:drawText(tostring(bar.value), x, y - 10)
    end
end

-- Uso
local barData = {
    {label = 'Jan', value = 100},
    {label = 'Fev', value = 150},
    {label = 'Mar', value = 120},
    {label = 'Abr', value = 200}
}
```

#### Finalização
```lua

local barStyle = {
    barColor = '#4CAF50',
    barWidth = 40,
    barSpacing = 15
}

local barChart = BarChart.create(parent, barData, barStyle)
```

---

## 🚀 Exemplos Práticos

### 📈 **Dashboard de Estatísticas**

#### Inicialização e Configuração
```lua
-- Sistema de dashboard com múltiplos gráficos
local StatisticsDashboard = {}

function StatisticsDashboard.create(parent)
    local window = g_ui.createWidget('MainWindow', parent)
    window:setId('statsDashboard')
    window:setText('Statistics Dashboard')
    window:setSize({width = 800, height = 600})
    window:setDraggable(true)
    
    -- Gráfico de linha para vendas
    local salesChart = LineChart.create(window, {
        {x = 1, y = 1000},
        {x = 2, y = 1500},
        {x = 3, y = 1200},
        {x = 4, y = 2000},
        {x = 5, y = 1800}
    }, {
        lineColor = '#2196F3',
        lineWidth = 3
    })
```

#### Funcionalidade 1
```lua
    salesChart:setPosition({x = 10, y = 30})
    salesChart:setSize({width = 380, height = 250})
    
    -- Gráfico de barras para produtos
    local productChart = BarChart.create(window, {
        {label = 'Prod A', value = 500},
        {label = 'Prod B', value = 800},
        {label = 'Prod C', value = 300},
        {label = 'Prod D', value = 600}
    }, {
        barColor = '#4CAF50',
        barWidth = 50
    })
    productChart:setPosition({x = 410, y = 30})
    productChart:setSize({width = 380, height = 250})
    
    -- Gráfico de pizza para categorias
    local categoryChart = PieChart.create(window, {
        {label = 'Eletrônicos', value = 40, color = '#F44336'},
        {label = 'Roupas', value = 30, color = '#2196F3'},
        {label = 'Livros', value = 20, color = '#4CAF50'},
        {label = 'Outros', value = 10, color = '#FFC107'}
    })
```

#### Finalização
```lua
    categoryChart:setPosition({x = 10, y = 300})
    categoryChart:setSize({width = 380, height = 250})
    
    return window
end

-- Uso
local dashboard = StatisticsDashboard.create(parent)
```

### 🎮 **Gráfico de Performance do Jogo**

#### Inicialização e Configuração
```lua
-- Sistema de gráfico de performance para jogos
local GamePerformanceChart = {}

function GamePerformanceChart.create(parent)
    local window = g_ui.createWidget('MainWindow', parent)
    window:setId('performanceChart')
    window:setText('Game Performance')
    window:setSize({width = 600, height = 400})
    window:setDraggable(true)
    
    -- Gráfico de linha para FPS
    local fpsChart = LineChart.create(window, {
        {x = 0, y = 60},
        {x = 1, y = 58},
        {x = 2, y = 55},
        {x = 3, y = 52},
        {x = 4, y = 50},
        {x = 5, y = 48}
    }, {
        lineColor = '#FF5722',
        lineWidth = 2,
        showGrid = true,
        gridColor = '#E0E0E0'
    })
```

#### Funcionalidade 1
```lua
    fpsChart:setPosition({x = 10, y = 30})
    fpsChart:setSize({width = 580, height = 360})
    
    -- Atualizar dados em tempo real
    GamePerformanceChart.startMonitoring(fpsChart)
    
    return window
end

function GamePerformanceChart.startMonitoring(chart)
    local frameCount = 0
    local lastTime = os.clock()
    local fpsData = {}
    
    -- Função para atualizar FPS
    local function updateFPS()
        frameCount = frameCount + 1
        local currentTime = os.clock()
        
        if currentTime - lastTime >= 1.0 then
            local fps = frameCount / (currentTime - lastTime)
            
            -- Adicionar novo ponto
            table.insert(fpsData, {x = #fpsData + 1, y = fps})
            
            -- Manter apenas os últimos 60 pontos
            if #fpsData > 60 then
                table.remove(fpsData, 1)
            end
```

#### Finalização
```lua
            
            -- Atualizar gráfico
            chart:setData({type = 'line', data = fpsData})
            chart:render()
            
            frameCount = 0
            lastTime = currentTime
        end
    end
    
    -- Conectar ao evento de renderização
    connect(g_game, {onRender = updateFPS})
end

-- Uso
local performanceChart = GamePerformanceChart.create(parent)
```

---

## ✅ Melhores Práticas

### 🎯 **Performance**

```lua
-- ✅ BOM: Usar cache para dados estáticos
local ChartCache = {}

function ChartCache.getCachedChart(chartId, data)
    -- Função: ChartCache
    if not ChartCache[chartId] then
    -- Verificação condicional
        ChartCache[chartId] = {
            data = data,
            lastUpdate = os.clock(),
            rendered = false
        }
    end
    
    return ChartCache[chartId]
end

function ChartCache.updateChart(chartId, newData)
    -- Função: ChartCache
    if ChartCache[chartId] then
    -- Verificação condicional
        ChartCache[chartId].data = newData
        ChartCache[chartId].lastUpdate = os.clock()
        ChartCache[chartId].rendered = false
    end
end

-- ✅ BOM: Implementar renderização lazy
function renderChartLazy(widget)
    -- Função: renderChartLazy
    local cache = ChartCache.getCachedChart(widget:getId(), widget:getData())
    
    if not cache.rendered or os.clock() - cache.lastUpdate > 1.0 then
    -- Verificação condicional
        widget:render()
        cache.rendered = true
    end
end

-- ❌ EVITE: Renderizar a cada frame
    --  ❌ EVITE: Renderizar a cada frame (traduzido)
function renderChartEveryFrame(widget)
    -- Função: renderChartEveryFrame
    widget:render()  -- Muito custoso
end
```

### 🎨 **Design**

```lua
-- ✅ BOM: Usar paleta de cores consistente
    --  ✅ BOM: Usar paleta de cores consistente (traduzido)
local CHART_COLORS = {
    PRIMARY = '#2196F3',
    SECONDARY = '#4CAF50',
    ACCENT = '#FF5722',
    WARNING = '#FFC107',
    ERROR = '#F44336',
    SUCCESS = '#4CAF50',
    INFO = '#00BCD4'
}

-- ✅ BOM: Implementar temas
    --  ✅ BOM: Implementar temas (traduzido)
local ChartThemes = {
    light = {
        backgroundColor = '#FFFFFF',
        textColor = '#000000',
        gridColor = '#E0E0E0',
        axisColor = '#666666'
    },
    dark = {
        backgroundColor = '#2D2D2D',
        textColor = '#FFFFFF',
        gridColor = '#404040',
        axisColor = '#CCCCCC'
    }
}

function applyChartTheme(chart, themeName)
    -- Função: applyChartTheme
    local theme = ChartThemes[themeName]
    if theme then
    -- Verificação condicional
        local style = chart:getStyle()
        for key, value in pairs(theme) do
    -- Loop de repetição
            style[key] = value
        end
        chart:setStyle(style)
        chart:render()
    end
end
```

### 🔧 **Estrutura**

#### Inicialização e Configuração
```lua
-- ✅ BOM: Organizar código em módulos
local ChartSystem = {}

function ChartSystem.createChart(parent, config)
    local chartType = config.type or 'line'
    local chartModule = ChartSystem[chartType]
    
    if chartModule and chartModule.create then
        return chartModule.create(parent, config.data, config.style)
    else
        error('Tipo de gráfico não suportado: ' .. chartType)
    end
end

function ChartSystem.updateChart(chart, newData)
    chart:setData(newData)
    chart:render()
end

function ChartSystem.animateChart(chart, newData, duration)
    -- Implementar animação suave
    local startData = chart:getData()
    local startTime = os.clock()
    
    local function animate()
        local elapsed = os.clock() - startTime
        local progress = math.min(elapsed / duration, 1.0)
        
        local interpolatedData = ChartSystem.interpolateData(startData, newData, progress)
        chart:setData(interpolatedData)
        chart:render()
        
        if progress < 1.0 then
            scheduleEvent(animate, 16)  -- ~60 FPS
        end
```

#### Funcionalidade 1
```lua
    end
    
    animate()
end

function ChartSystem.interpolateData(data1, data2, progress)
    -- Implementar interpolação de dados
    local result = {}
    for i, point1 in ipairs(data1) do
        local point2 = data2[i]
        if point2 then
            result[i] = {
                x = point1.x + (point2.x - point1.x) * progress,
                y = point1.y + (point2.y - point1.y) * progress
            }
        end
    end
    return result
end

-- Uso
local chart = ChartSystem.createChart(parent, {
    type = 'line',
    data = lineData,
    style = lineStyle
})
```

#### Finalização
```lua

ChartSystem.animateChart(chart, newLineData, 1.0)  -- 1 segundo de animação
```

---

## 🚀 Performance e Otimização

### 📊 **Métricas de Performance**

- **Gráfico simples**: ~1ms para renderização
- **Gráfico complexo**: ~5ms para renderização
- **1000 pontos**: ~10ms para renderização
- **Animação 60 FPS**: ~16ms por frame
- **Memória por gráfico**: ~5KB

### ⚡ **Otimizações Recomendadas**

#### Inicialização e Configuração
```lua
-- ✅ BOM: Usar renderização por lotes
function renderBatchCharts(charts)
    for _, chart in ipairs(charts) do
        chart:prepareRender()
    end
    
    for _, chart in ipairs(charts) do
        chart:executeRender()
    end
end

-- ✅ BOM: Implementar culling de elementos
function renderVisibleElements(canvas, elements, viewport)
    for _, element in ipairs(elements) do
        if isElementVisible(element, viewport) then
            renderElement(canvas, element)
        end
    end
end

function isElementVisible(element, viewport)
```

#### Funcionalidade 1
```lua
    return element.x >= viewport.x and 
           element.x <= viewport.x + viewport.width and
           element.y >= viewport.y and 
           element.y <= viewport.y + viewport.height
end

-- ✅ BOM: Usar object pooling para elementos
local ElementPool = {
    available = {},
    inUse = {}
}

function ElementPool.getElement()
    if #ElementPool.available > 0 then
        local element = table.remove(ElementPool.available)
        table.insert(ElementPool.inUse, element)
        return element
    else
        local element = {x = 0, y = 0, width = 0, height = 0}
        table.insert(ElementPool.inUse, element)
        return element
    end
```

#### Finalização
```lua
end

function ElementPool.releaseElement(element)
    for i, usedElement in ipairs(ElementPool.inUse) do
        if usedElement == element then
            table.remove(ElementPool.inUse, i)
            table.insert(ElementPool.available, element)
            break
        end
    end
end
```

### 🎯 **Monitoramento**

```lua
-- ✅ BOM: Monitorar performance dos gráficos
local ChartPerformance = {
    renderTime = 0,
    chartCount = 0,
    memoryUsage = 0
}

function ChartPerformance.startRender()
    -- Função: ChartPerformance
    ChartPerformance.renderStart = os.clock()
end

function ChartPerformance.endRender()
    -- Função: ChartPerformance
    ChartPerformance.renderTime = os.clock() - ChartPerformance.renderStart
    print('Chart render time:', ChartPerformance.renderTime * 1000, 'ms')
end

function ChartPerformance.updateStats(chartCount)
    -- Função: ChartPerformance
    ChartPerformance.chartCount = chartCount
    ChartPerformance.memoryUsage = chartCount * 5 -- 5KB por gráfico
end
```

O Sistema de Gráficos e Charts do OTClient oferece ferramentas poderosas para criar visualizações de dados interativas e informativas. Use estas práticas para garantir performance e usabilidade em suas aplicações.

> - [[UIWidget_Reference]] - Referência completa de widgets
> - [[UILayouts]] - Sistema de layouts
> - [[UIAnimations]] - Sistema de animações 
## 🔗 **Links Automáticos**

> [!info] **Links Gerados Automaticamente**
> Estes links foram criados automaticamente pelo sistema de linkagem da categoria **Documentation**

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]

### **🧭 Navegação**
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]
- [[../maps/category_indices|Índices por Categoria]]
- [[../maps/relationships|Relacionamentos]]

### **📊 Métricas da Categoria**
- **Categoria**: Documentation
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

