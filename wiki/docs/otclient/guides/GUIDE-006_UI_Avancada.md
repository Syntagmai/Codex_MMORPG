
# 🎨 Guia de UI Avançada - OTClient

## 📋 **ÍNDICE DETALHADO**

### **🎯 Navegação Rápida**

1. [🎯](#🎯)
2. [📋](#📋)
3. [📋](#📋)
4. [⚙️](#⚙️)
5. [📋](#📋)
6. [⚙️](#⚙️)
7. [📋](#📋)
8. [⚙️](#⚙️)
9. [📋](#📋)

### **📚 Seções Principais**

| Seção | Descrição |
|-------|-----------|
| 🎯 | Documentação e referência |
| 📋 | Documentação e referência |
| 📋 | Documentação e referência |
| ⚙️ | Documentação e referência |
| 📋 | Documentação e referência |
| ⚙️ | Documentação e referência |
| 📋 | Documentação e referência |
| ⚙️ | Documentação e referência |
| 📋 | Documentação e referência |



---

## 🎯 **Visão Geral** 🎯

Este guia fornece técnicas avançadas de desenvolvimento de interface do usuário para o OTClient, incluindo widgets customizados, animações, layouts responsivos, temas e melhores práticas para desenvolvedores e agentes de IA.


---

## 📚 **Pré-requisitos** 📋

- ✅ Conhecimento básico do OTClient
- ✅ Familiaridade com Lua
- ✅ Compreensão de widgets básicos
- ✅ Conhecimento de OTUI (sistema de UI do OTClient)

---


---

## 🧩 **1. Widgets Avançados** 📋

### **1.1 Widget Customizado Base** 📝

#### Inicialização e Configuração
```lua
-- Classe base para widgets customizados
local CustomWidget = {}

function CustomWidget:new()
    local widget = {}
    setmetatable(widget, {__index = CustomWidget})
    
    widget.properties = {}
    widget.children = {}
    widget.events = {}
    widget.styles = {}
    
    return widget
end

function CustomWidget:setProperty(name, value)
    self.properties[name] = value
    self:updateDisplay()
end

function CustomWidget:getProperty(name)
```

#### Funcionalidade 1
```lua
    return self.properties[name]
end

function CustomWidget:addChild(child)
    table.insert(self.children, child)
    child.parent = self
    self:updateLayout()
end

function CustomWidget:removeChild(child)
    for i, c in ipairs(self.children) do
        if c == child then
            table.remove(self.children, i)
            break
        end
    end
    self:updateLayout()
end

function CustomWidget:onEvent(eventType, callback)
    self.events[eventType] = callback
end
```

#### Finalização
```lua

function CustomWidget:triggerEvent(eventType, data)
    if self.events[eventType] then
        self.events[eventType](self, data)
    end
end

function CustomWidget:updateDisplay()
    -- Implementação específica do widget
end

function CustomWidget:updateLayout()
    -- Implementação específica do layout
end
```

### **1.2 Widget de Progresso Avançado** 📝

#### Inicialização e Configuração
```lua
-- Widget de progresso com animações e temas
local AdvancedProgressBar = CustomWidget:new()

function AdvancedProgressBar:new()
    local widget = CustomWidget:new()
    setmetatable(widget, {__index = AdvancedProgressBar})
    
    widget.value = 0
    widget.maxValue = 100
    widget.animationSpeed = 0.3
    widget.theme = "default"
    widget.showText = true
    widget.textFormat = "{current}/{max} ({percentage}%)"
    
    return widget
end

function AdvancedProgressBar:setValue(value)
    local oldValue = self.value
    self.value = math.max(0, math.min(value, self.maxValue))
    
    -- Animar mudança de valor
    if oldValue ~= self.value then
        self:animateValueChange(oldValue, self.value)
    end
```

#### Funcionalidade 1
```lua
    
    self:updateDisplay()
end

function AdvancedProgressBar:setMaxValue(maxValue)
    self.maxValue = maxValue
    self:updateDisplay()
end

function AdvancedProgressBar:animateValueChange(fromValue, toValue)
    local duration = self.animationSpeed * 1000 -- ms
    local startTime = os.clock()
    local startValue = fromValue
    
    local function animate()
        local elapsed = (os.clock() - startTime) * 1000
        local progress = math.min(elapsed / duration, 1)
        
        -- Easing function (ease-out)
        progress = 1 - (1 - progress) * (1 - progress)
        
        local currentValue = startValue + (toValue - startValue) * progress
        self:setDisplayValue(currentValue)
        
        if progress < 1 then
            scheduleEvent(animate, 16) -- ~60 FPS
        end
```

#### Funcionalidade 2
```lua
    end
    
    animate()
end

function AdvancedProgressBar:setDisplayValue(value)
    -- Atualizar display sem animação
    self.displayValue = value
    self:updateDisplay()
end

function AdvancedProgressBar:updateDisplay()
    local percentage = (self.displayValue or self.value) / self.maxValue
    
    -- Atualizar barra de progresso
    if self.progressBar then
        self.progressBar:setWidth(self:getWidth() * percentage)
    end
    
    -- Atualizar texto
    if self.showText and self.textLabel then
        local text = self.textFormat
        text = text:gsub("{current}", math.floor(self.displayValue or self.value))
        text = text:gsub("{max}", self.maxValue)
        text = text:gsub("{percentage}", math.floor(percentage * 100))
        self.textLabel:setText(text)
    end
```

#### Funcionalidade 3
```lua
    
    -- Aplicar tema
    self:applyTheme()
end

function AdvancedProgressBar:applyTheme()
    local themes = {
        default = {
            background = "#2C2C2C",
            progress = "#4CAF50",
            text = "#FFFFFF"
        },
        health = {
            background = "#2C2C2C",
            progress = "#F44336",
            text = "#FFFFFF"
        },
        mana = {
            background = "#2C2C2C",
            progress = "#2196F3",
            text = "#FFFFFF"
        },
```

#### Funcionalidade 4
```lua
        experience = {
            background = "#2C2C2C",
            progress = "#FF9800",
            text = "#FFFFFF"
        }
    }
    
    local theme = themes[self.theme] or themes.default
    
    if self.background then
        self.background:setBackgroundColor(theme.background)
    end
    
    if self.progressBar then
        self.progressBar:setBackgroundColor(theme.progress)
    end
    
    if self.textLabel then
        self.textLabel:setColor(theme.text)
    end
end
```

#### Finalização
```lua

function AdvancedProgressBar:setTheme(theme)
    self.theme = theme
    self:applyTheme()
end
```

### **1.3 Widget de Tooltip Avançado** 📝

#### Inicialização e Configuração
```lua
-- Widget de tooltip com formatação rica e animações
local AdvancedTooltip = CustomWidget:new()

function AdvancedTooltip:new()
    local widget = CustomWidget:new()
    setmetatable(widget, {__index = AdvancedTooltip})
    
    widget.content = {}
    widget.maxWidth = 300
    widget.showDelay = 500 -- ms
    widget.fadeInDuration = 200 -- ms
    widget.fadeOutDuration = 150 -- ms
    widget.offset = {x = 10, y = 10}
    
    return widget
end

function AdvancedTooltip:setContent(content)
    self.content = content
    self:updateDisplay()
end
```

#### Funcionalidade 1
```lua

function AdvancedTooltip:addSection(title, items)
    table.insert(self.content, {
        type = "section",
        title = title,
        items = items
    })
    self:updateDisplay()
end

function AdvancedTooltip:addItem(text, color, icon)
    table.insert(self.content, {
        type = "item",
        text = text,
        color = color or "#FFFFFF",
        icon = icon
    })
    self:updateDisplay()
end

function AdvancedTooltip:show(target, position)
```

#### Funcionalidade 2
```lua
    self.target = target
    self.position = position or self:calculatePosition(target)
    
    -- Delay antes de mostrar
    self.showTimer = scheduleEvent(function()
        self:showImmediate()
    end, self.showDelay)
end

function AdvancedTooltip:hide()
    if self.showTimer then
        self.showTimer:cancel()
        self.showTimer = nil
    end
    
    self:fadeOut()
end

function AdvancedTooltip:showImmediate()
    self:setVisible(true)
    self:setPosition(self.position)
    self:fadeIn()
end
```

#### Funcionalidade 3
```lua

function AdvancedTooltip:fadeIn()
    self:setOpacity(0)
    
    local duration = self.fadeInDuration
    local startTime = os.clock()
    
    local function animate()
        local elapsed = (os.clock() - startTime) * 1000
        local progress = math.min(elapsed / duration, 1)
        
        self:setOpacity(progress)
        
        if progress < 1 then
            scheduleEvent(animate, 16)
        end
    end
    
    animate()
end

function AdvancedTooltip:fadeOut()
```

#### Funcionalidade 4
```lua
    local duration = self.fadeOutDuration
    local startTime = os.clock()
    local startOpacity = self:getOpacity()
    
    local function animate()
        local elapsed = (os.clock() - startTime) * 1000
        local progress = math.min(elapsed / duration, 1)
        
        self:setOpacity(startOpacity * (1 - progress))
        
        if progress < 1 then
            scheduleEvent(animate, 16)
        else
            self:setVisible(false)
        end
    end
    
    animate()
end

function AdvancedTooltip:calculatePosition(target)
```

#### Funcionalidade 5
```lua
    local targetPos = target:getPosition()
    local targetSize = target:getSize()
    local screenSize = g_graphics.getScreenSize()
    
    local x = targetPos.x + targetSize.width + self.offset.x
    local y = targetPos.y + self.offset.y
    
    -- Ajustar se sair da tela
    if x + self:getWidth() > screenSize.width then
        x = targetPos.x - self:getWidth() - self.offset.x
    end
    
    if y + self:getHeight() > screenSize.height then
        y = targetPos.y - self:getHeight() - self.offset.y
    end
    
    return {x = x, y = y}
end

function AdvancedTooltip:updateDisplay()
    -- Limpar conteúdo anterior
    self:clearChildren()
    
    local y = 0
    
    for _, item in ipairs(self.content) do
        if item.type == "section" then
            -- Criar seção
            local sectionTitle = g_ui.createWidget('Label', self)
            sectionTitle:setText(item.title)
            sectionTitle:setColor("#FFD700") -- Dourado
            sectionTitle:setPosition({x = 5, y = y})
            y = y + sectionTitle:getHeight() + 5
            
            -- Adicionar itens da seção
            for _, sectionItem in ipairs(item.items) do
                local itemLabel = g_ui.createWidget('Label', self)
                itemLabel:setText(sectionItem.text)
                itemLabel:setColor(sectionItem.color or "#FFFFFF")
                itemLabel:setPosition({x = 15, y = y})
                y = y + itemLabel:getHeight() + 2
            end
```

#### Finalização
```lua
        elseif item.type == "item" then
            -- Criar item simples
            local itemLabel = g_ui.createWidget('Label', self)
            itemLabel:setText(item.text)
            itemLabel:setColor(item.color)
            itemLabel:setPosition({x = 5, y = y})
            y = y + itemLabel:getHeight() + 2
        end
    end
    
    -- Ajustar tamanho
    self:setHeight(y + 5)
end
```

---


---

## 🎭 **2. Sistema de Animações** ⚙️

### **2.1 Animation Manager** 📝

#### Inicialização e Configuração
```lua
-- Gerenciador de animações
local AnimationManager = {
    animations = {},
    nextId = 1
}

function AnimationManager:createAnimation(target, properties, duration, easing)
    local animation = {
        id = self.nextId,
        target = target,
        properties = properties,
        duration = duration,
        easing = easing or "linear",
        startTime = os.clock(),
        startValues = {},
        endValues = {},
        completed = false,
        onComplete = nil,
        onUpdate = nil
    }
    
    -- Capturar valores iniciais
    for property, endValue in pairs(properties) do
        animation.startValues[property] = self:getPropertyValue(target, property)
        animation.endValues[property] = endValue
    end
```

#### Funcionalidade 1
```lua
    
    self.nextId = self.nextId + 1
    table.insert(self.animations, animation)
    
    return animation.id
end

function AnimationManager:getPropertyValue(target, property)
    if property == "x" then
        return target:getPosition().x
    elseif property == "y" then
        return target:getPosition().y
    elseif property == "width" then
        return target:getWidth()
    elseif property == "height" then
        return target:getHeight()
    elseif property == "opacity" then
        return target:getOpacity()
    elseif property == "scale" then
        return target:getScale()
    else
        return target[property]
    end
```

#### Funcionalidade 2
```lua
end

function AnimationManager:setPropertyValue(target, property, value)
    if property == "x" then
        local pos = target:getPosition()
        target:setPosition({x = value, y = pos.y})
    elseif property == "y" then
        local pos = target:getPosition()
        target:setPosition({x = pos.x, y = value})
    elseif property == "width" then
        target:setWidth(value)
    elseif property == "height" then
        target:setHeight(value)
    elseif property == "opacity" then
        target:setOpacity(value)
    elseif property == "scale" then
        target:setScale(value)
    else
        target[property] = value
    end
end
```

#### Funcionalidade 3
```lua

function AnimationManager:update()
    local currentTime = os.clock()
    local completedAnimations = {}
    
    for i, animation in ipairs(self.animations) do
        if not animation.completed then
            local elapsed = (currentTime - animation.startTime) * 1000
            local progress = math.min(elapsed / animation.duration, 1)
            
            -- Aplicar easing
            progress = self:applyEasing(progress, animation.easing)
            
            -- Atualizar propriedades
            for property, _ in pairs(animation.properties) do
                local startValue = animation.startValues[property]
                local endValue = animation.endValues[property]
                local currentValue = startValue + (endValue - startValue) * progress
                
                self:setPropertyValue(animation.target, property, currentValue)
            end
```

#### Funcionalidade 4
```lua
            
            -- Chamar callback de atualização
            if animation.onUpdate then
                animation.onUpdate(animation.target, progress)
            end
            
            -- Verificar se completou
            if progress >= 1 then
                animation.completed = true
                table.insert(completedAnimations, i)
                
                if animation.onComplete then
                    animation.onComplete(animation.target)
                end
            end
        end
    end
    
    -- Remover animações completadas
    for i = #completedAnimations, 1, -1 do
        table.remove(self.animations, completedAnimations[i])
    end
```

#### Funcionalidade 5
```lua
end

function AnimationManager:applyEasing(progress, easing)
    if easing == "linear" then
        return progress
    elseif easing == "easeIn" then
        return progress * progress
    elseif easing == "easeOut" then
        return 1 - (1 - progress) * (1 - progress)
    elseif easing == "easeInOut" then
        if progress < 0.5 then
            return 2 * progress * progress
        else
            return 1 - 2 * (1 - progress) * (1 - progress)
        end
    elseif easing == "bounce" then
        if progress < 1/2.75 then
            return 7.5625 * progress * progress
        elseif progress < 2/2.75 then
            return 7.5625 * (progress - 1.5/2.75) * (progress - 1.5/2.75) + 0.75
        elseif progress < 2.5/2.75 then
            return 7.5625 * (progress - 2.25/2.75) * (progress - 2.25/2.75) + 0.9375
        else
            return 7.5625 * (progress - 2.625/2.75) * (progress - 2.625/2.75) + 0.984375
        end
```

#### Finalização
```lua
    end
    
    return progress
end

function AnimationManager:stopAnimation(animationId)
    for i, animation in ipairs(self.animations) do
        if animation.id == animationId then
            table.remove(self.animations, i)
            break
        end
    end
end

function AnimationManager:stopAllAnimations()
    self.animations = {}
end

-- Iniciar loop de atualização
scheduleEvent(function()
    AnimationManager:update()
end, 16) -- ~60 FPS
```

### **2.2 Animações Pré-definidas** 📝

#### Inicialização e Configuração
```lua
-- Biblioteca de animações pré-definidas
local AnimationLibrary = {}

function AnimationLibrary:fadeIn(target, duration, callback)
    target:setOpacity(0)
    return AnimationManager:createAnimation(target, {opacity = 1}, duration or 300, "easeOut", callback)
end

function AnimationLibrary:fadeOut(target, duration, callback)
    return AnimationManager:createAnimation(target, {opacity = 0}, duration or 300, "easeIn", callback)
end

function AnimationLibrary:slideIn(target, direction, duration, callback)
    local startPos = target:getPosition()
    local endPos = {x = startPos.x, y = startPos.y}
    
    if direction == "left" then
        target:setPosition({x = startPos.x - target:getWidth(), y = startPos.y})
        endPos.x = startPos.x
    elseif direction == "right" then
        target:setPosition({x = startPos.x + target:getWidth(), y = startPos.y})
        endPos.x = startPos.x
```

#### Funcionalidade 1
```lua
    elseif direction == "up" then
        target:setPosition({x = startPos.x, y = startPos.y - target:getHeight()})
        endPos.y = startPos.y
    elseif direction == "down" then
        target:setPosition({x = startPos.x, y = startPos.y + target:getHeight()})
        endPos.y = startPos.y
    end
    
    return AnimationManager:createAnimation(target, endPos, duration or 400, "easeOut", callback)
end

function AnimationLibrary:slideOut(target, direction, duration, callback)
    local startPos = target:getPosition()
    local endPos = {x = startPos.x, y = startPos.y}
    
    if direction == "left" then
        endPos.x = startPos.x - target:getWidth()
    elseif direction == "right" then
        endPos.x = startPos.x + target:getWidth()
    elseif direction == "up" then
        endPos.y = startPos.y - target:getHeight()
```

#### Funcionalidade 2
```lua
    elseif direction == "down" then
        endPos.y = startPos.y + target:getHeight()
    end
    
    return AnimationManager:createAnimation(target, endPos, duration or 400, "easeIn", callback)
end

function AnimationLibrary:scaleIn(target, duration, callback)
    target:setScale(0)
    return AnimationManager:createAnimation(target, {scale = 1}, duration or 300, "bounce", callback)
end

function AnimationLibrary:scaleOut(target, duration, callback)
    return AnimationManager:createAnimation(target, {scale = 0}, duration or 300, "easeIn", callback)
end

function AnimationLibrary:pulse(target, duration, callback)
    local originalScale = target:getScale()
    
    AnimationManager:createAnimation(target, {scale = originalScale * 1.1}, duration or 150, "easeOut", function()
        AnimationManager:createAnimation(target, {scale = originalScale}, duration or 150, "easeIn", callback)
    end)
```

#### Funcionalidade 3
```lua
end

function AnimationLibrary:shake(target, intensity, duration, callback)
    local originalPos = target:getPosition()
    local shakeCount = math.floor(duration / 50) -- 50ms por shake
    
    local function shake(remaining)
        if remaining <= 0 then
            target:setPosition(originalPos)
            if callback then callback() end
            return
        end
        
        local offsetX = (math.random() - 0.5) * intensity
        local offsetY = (math.random() - 0.5) * intensity
        
        target:setPosition({
            x = originalPos.x + offsetX,
            y = originalPos.y + offsetY
        })
        
        scheduleEvent(function()
            shake(remaining - 1)
        end, 50)
```

#### Finalização
```lua
    end
    
    shake(shakeCount)
end
```

---


---

## 📐 **3. Layouts Responsivos** 📋

### **3.1 Layout Manager** 📝

#### Inicialização e Configuração
```lua
-- Gerenciador de layouts responsivos
local LayoutManager = {
    layouts = {},
    breakpoints = {
        mobile = 768,
        tablet = 1024,
        desktop = 1200
    }
}

function LayoutManager:createLayout(name, config)
    local layout = {
        name = name,
        config = config,
        containers = {},
        rules = {}
    }
    
    self.layouts[name] = layout
    return layout
end
```

#### Funcionalidade 1
```lua

function LayoutManager:addContainer(layoutName, container)
    local layout = self.layouts[layoutName]
    if layout then
        table.insert(layout.containers, container)
        self:applyLayout(layoutName)
    end
end

function LayoutManager:addRule(layoutName, rule)
    local layout = self.layouts[layoutName]
    if layout then
        table.insert(layout.rules, rule)
        self:applyLayout(layoutName)
    end
end

function LayoutManager:applyLayout(layoutName)
    local layout = self.layouts[layoutName]
    if not layout then return end
    
    local screenSize = g_graphics.getScreenSize()
    local breakpoint = self:getCurrentBreakpoint(screenSize.width)
    
    for _, container in ipairs(layout.containers) do
        self:applyContainerLayout(container, layout.config, breakpoint)
    end
```

#### Funcionalidade 2
```lua
    
    for _, rule in ipairs(layout.rules) do
        self:applyRule(rule, breakpoint)
    end
end

function LayoutManager:getCurrentBreakpoint(width)
    if width < self.breakpoints.mobile then
        return "mobile"
    elseif width < self.breakpoints.tablet then
        return "tablet"
    elseif width < self.breakpoints.desktop then
        return "desktop"
    else
        return "large"
    end
end

function LayoutManager:applyContainerLayout(container, config, breakpoint)
    local layoutConfig = config[breakpoint] or config.default
    
    if layoutConfig.position then
        container:setPosition(layoutConfig.position)
    end
```

#### Funcionalidade 3
```lua
    
    if layoutConfig.size then
        container:setSize(layoutConfig.size)
    end
    
    if layoutConfig.visible ~= nil then
        container:setVisible(layoutConfig.visible)
    end
    
    if layoutConfig.opacity then
        container:setOpacity(layoutConfig.opacity)
    end
end

function LayoutManager:applyRule(rule, breakpoint)
    local ruleConfig = rule[breakpoint] or rule.default
    
    if ruleConfig.selector then
        local widgets = g_ui.getWidgetsBySelector(ruleConfig.selector)
        for _, widget in ipairs(widgets) do
            if ruleConfig.apply then
                ruleConfig.apply(widget, ruleConfig)
            end
```

#### Finalização
```lua
        end
    end
end
```

### **3.2 Grid Layout** 📝

#### Inicialização e Configuração
```lua
-- Sistema de grid responsivo
local GridLayout = {
    grids = {}
}

function GridLayout:createGrid(name, columns, gap)
    local grid = {
        name = name,
        columns = columns,
        gap = gap or 5,
        items = {},
        breakpoints = {
            mobile = {columns = math.min(columns, 2)},
            tablet = {columns = math.min(columns, 4)},
            desktop = {columns = columns},
            large = {columns = columns}
        }
    }
    
    self.grids[name] = grid
    return grid
end
```

#### Funcionalidade 1
```lua

function GridLayout:addItem(gridName, widget, row, col, rowSpan, colSpan)
    local grid = self.grids[gridName]
    if not grid then return end
    
    local item = {
        widget = widget,
        row = row,
        col = col,
        rowSpan = rowSpan or 1,
        colSpan = colSpan or 1
    }
    
    table.insert(grid.items, item)
    self:updateGrid(gridName)
end

function GridLayout:updateGrid(gridName)
    local grid = self.grids[gridName]
    if not grid then return end
    
    local screenSize = g_graphics.getScreenSize()
    local breakpoint = LayoutManager:getCurrentBreakpoint(screenSize.width)
    local currentColumns = grid.breakpoints[breakpoint].columns
    
    -- Calcular posições dos itens
    local positions = self:calculateGridPositions(grid, currentColumns)
    
    -- Aplicar posições
    for _, item in ipairs(grid.items) do
        local position = positions[item]
        if position then
            item.widget:setPosition(position)
        end
```

#### Finalização
```lua
    end
end

function GridLayout:calculateGridPositions(grid, columns)
    local positions = {}
    local cellWidth = (grid.container:getWidth() - (columns - 1) * grid.gap) / columns
    local cellHeight = cellWidth -- Assumindo células quadradas
    
    for _, item in ipairs(grid.items) do
        local x = (item.col - 1) * (cellWidth + grid.gap)
        local y = (item.row - 1) * (cellHeight + grid.gap)
        
        positions[item] = {
            x = x,
            y = y,
            width = cellWidth * item.colSpan + (item.colSpan - 1) * grid.gap,
            height = cellHeight * item.rowSpan + (item.rowSpan - 1) * grid.gap
        }
    end
    
    return positions
end
```

---


---

## 🎨 **4. Sistema de Temas** ⚙️

### **4.1 Theme Manager** 📝

#### Inicialização e Configuração
```lua
-- Gerenciador de temas
local ThemeManager = {
    themes = {},
    currentTheme = "default",
    customProperties = {}
}

function ThemeManager:createTheme(name, config)
    local theme = {
        name = name,
        config = config,
        variables = config.variables or {},
        components = config.components or {}
    }
    
    self.themes[name] = theme
    return theme
end

function ThemeManager:setTheme(name)
    local theme = self.themes[name]
    if not theme then return end
    
    self.currentTheme = name
    self:applyTheme(theme)
end
```

#### Funcionalidade 1
```lua

function ThemeManager:applyTheme(theme)
    -- Aplicar variáveis CSS
    for variable, value in pairs(theme.variables) do
        self:setCSSVariable(variable, value)
    end
    
    -- Aplicar estilos de componentes
    for component, styles in pairs(theme.components) do
        self:applyComponentStyles(component, styles)
    end
    
    -- Notificar mudança de tema
    self:notifyThemeChange(theme)
end

function ThemeManager:setCSSVariable(name, value)
    -- Implementar definição de variáveis CSS
    g_ui.setCSSVariable(name, value)
end

function ThemeManager:applyComponentStyles(component, styles)
```

#### Funcionalidade 2
```lua
    local widgets = g_ui.getWidgetsByClass(component)
    
    for _, widget in ipairs(widgets) do
        for property, value in pairs(styles) do
            self:setWidgetProperty(widget, property, value)
        end
    end
end

function ThemeManager:setWidgetProperty(widget, property, value)
    if property == "backgroundColor" then
        widget:setBackgroundColor(value)
    elseif property == "color" then
        widget:setColor(value)
    elseif property == "borderColor" then
        widget:setBorderColor(value)
    elseif property == "fontSize" then
        widget:setFontSize(value)
    elseif property == "fontFamily" then
        widget:setFontFamily(value)
    end
```

#### Finalização
```lua
end

function ThemeManager:notifyThemeChange(theme)
    -- Notificar widgets sobre mudança de tema
    local event = {
        type = "themeChanged",
        theme = theme
    }
    
    g_ui.dispatchEvent(event)
end

function ThemeManager:getThemeVariable(name)
    local theme = self.themes[self.currentTheme]
    if theme and theme.variables then
        return theme.variables[name]
    end
    return nil
end
```

### **4.2 Temas Pré-definidos** 📝

#### Inicialização e Configuração
```lua
-- Temas pré-definidos
local PredefinedThemes = {
    default = {
        variables = {
            "--primary-color" = "#4CAF50",
            "--secondary-color" = "#2196F3",
            "--accent-color" = "#FF9800",
            "--background-color" = "#2C2C2C",
            "--surface-color" = "#3C3C3C",
            "--text-color" = "#FFFFFF",
            "--text-secondary" = "#B0B0B0",
            "--border-color" = "#555555",
            "--error-color" = "#F44336",
            "--success-color" = "#4CAF50",
            "--warning-color" = "#FF9800"
        },
        components = {
            Button = {
                backgroundColor = "#4CAF50",
                color = "#FFFFFF",
                borderColor = "#45A049"
            },
```

#### Funcionalidade 1
```lua
            Label = {
                color = "#FFFFFF"
            },
            Panel = {
                backgroundColor = "#3C3C3C",
                borderColor = "#555555"
            }
        }
    },
    
    dark = {
        variables = {
            "--primary-color" = "#BB86FC",
            "--secondary-color" = "#03DAC6",
            "--accent-color" = "#FF7597",
            "--background-color" = "#121212",
            "--surface-color" = "#1E1E1E",
            "--text-color" = "#FFFFFF",
            "--text-secondary" = "#B3B3B3",
            "--border-color" = "#333333",
            "--error-color" = "#CF6679",
            "--success-color" = "#03DAC6",
            "--warning-color" = "#FF7597"
        }
```

#### Finalização
```lua
    },
    
    light = {
        variables = {
            "--primary-color" = "#6200EE",
            "--secondary-color" = "#03DAC6",
            "--accent-color" = "#FF6B6B",
            "--background-color" = "#FFFFFF",
            "--surface-color" = "#F5F5F5",
            "--text-color" = "#000000",
            "--text-secondary" = "#666666",
            "--border-color" = "#E0E0E0",
            "--error-color" = "#B00020",
            "--success-color" = "#4CAF50",
            "--warning-color" = "#FF9800"
        }
    }
}

-- Registrar temas pré-definidos
for name, config in pairs(PredefinedThemes) do
    ThemeManager:createTheme(name, config)
end
```

---


---

## 🎯 **5. Melhores Práticas de UI** 📋

### **5.1 Princípios de Design** 📝

1. **Consistência**: Manter padrões visuais consistentes
2. **Hierarquia**: Usar tamanhos e cores para estabelecer hierarquia
3. **Feedback**: Fornecer feedback visual para ações do usuário
4. **Acessibilidade**: Garantir que a interface seja acessível
5. **Performance**: Otimizar renderização e animações

### **5.2 Padrões de UI** 📝

#### Inicialização e Configuração
```lua
-- Padrões de UI comuns
local UIPatterns = {
    -- Modal Dialog
    createModalDialog = function(title, content, buttons)
        local modal = g_ui.createWidget('Panel')
        modal:setSize({width = 400, height = 300})
        modal:setPosition({x = (g_graphics.getScreenSize().width - 400) / 2, y = 100})
        
        -- Overlay
        local overlay = g_ui.createWidget('Panel')
        overlay:setSize(g_graphics.getScreenSize())
        overlay:setBackgroundColor("#000000")
        overlay:setOpacity(0.5)
        
        -- Título
        local titleLabel = g_ui.createWidget('Label', modal)
        titleLabel:setText(title)
        titleLabel:setPosition({x = 10, y = 10})
        
        -- Conteúdo
        local contentLabel = g_ui.createWidget('Label', modal)
        contentLabel:setText(content)
        contentLabel:setPosition({x = 10, y = 50})
        
        -- Botões
        local buttonY = 250
        for i, button in ipairs(buttons) do
            local btn = g_ui.createWidget('Button', modal)
            btn:setText(button.text)
            btn:setPosition({x = 10 + (i-1) * 100, y = buttonY})
            btn.onClick = button.onClick
        end
```

#### Funcionalidade 1
```lua
        
        return modal
    end,
    
    -- Toast Notification
    createToast = function(message, type, duration)
        local toast = g_ui.createWidget('Panel')
        toast:setSize({width = 300, height = 60})
        toast:setPosition({x = g_graphics.getScreenSize().width - 320, y = 20})
        
        local messageLabel = g_ui.createWidget('Label', toast)
        messageLabel:setText(message)
        messageLabel:setPosition({x = 10, y = 20})
        
        -- Aplicar tipo
        local colors = {
            success = "#4CAF50",
            error = "#F44336",
            warning = "#FF9800",
            info = "#2196F3"
        }
```

#### Funcionalidade 2
```lua
        
        toast:setBackgroundColor(colors[type] or colors.info)
        
        -- Auto-hide
        scheduleEvent(function()
            AnimationLibrary:fadeOut(toast, 300, function()
                toast:destroy()
            end)
        end, duration or 3000)
        
        return toast
    end,
    
    -- Loading Spinner
    createLoadingSpinner = function(size)
        local spinner = g_ui.createWidget('Panel')
        spinner:setSize({width = size or 40, height = size or 40})
        
        -- Implementar animação de rotação
        local angle = 0
        scheduleEvent(function()
            angle = angle + 10
            spinner:setRotation(angle)
        end, 50)
```

#### Finalização
```lua
        
        return spinner
    end
}
```

### **5.3 Checklist de UI** 📝

#### Nível Basic
```lua
local uiChecklist = {
    "Verificar responsividade em diferentes resoluções",
    "Verificar consistência de cores e fontes",
    "Testar em diferentes temas",
    "Verificar performance de renderização"
```

#### Nível Intermediate
```lua
local uiChecklist = {
    "Verificar responsividade em diferentes resoluções",
    "Testar acessibilidade (contraste, tamanho de fonte)",
    "Validar feedback visual para ações",
    "Verificar consistência de cores e fontes",
    "Testar animações e transições",
    "Validar hierarquia visual",
    "Testar em diferentes temas",
    "Verificar performance de renderização"
}
```

#### Nível Advanced
```lua
local uiChecklist = {
    "Verificar responsividade em diferentes resoluções",
    "Testar acessibilidade (contraste, tamanho de fonte)",
    "Validar feedback visual para ações",
    "Verificar consistência de cores e fontes",
    "Testar animações e transições",
    "Validar hierarquia visual",
    "Testar em diferentes temas",
    "Verificar performance de renderização"
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

---


---

## 🔄 **6. Integração com Sistema de UI** ⚙️

### **6.1 Uso com UI Stories** 📝

Este guia complementa as UI Stories documentadas no sistema, fornecendo:

- ✅ Widgets avançados e customizados
- ✅ Sistema de animações robusto
- ✅ Layouts responsivos
- ✅ Sistema de temas flexível
- ✅ Melhores práticas de design
- ✅ Padrões de UI reutilizáveis

### **6.2 Benefícios para Agentes** 📝

- **Autonomia**: Agentes podem criar interfaces complexas
- **Consistência**: Sistema de temas garante consistência visual
- **Responsividade**: Layouts adaptam-se a diferentes resoluções
- **Performance**: Animações otimizadas e widgets eficientes

---


---

## 📊 **Status do Guia** 📋

### **✅ Concluído:** 📝
- ✅ Widgets avançados
- ✅ Sistema de animações
- ✅ Layouts responsivos
- ✅ Sistema de temas
- ✅ Melhores práticas
- ✅ Padrões de UI
- ✅ Integração com UI Stories

### **🎯 Próximo:** 📝
- 🔄 GUIDE-007: Guia de Game Systems

---

**Guia Criado**: 2025-01-27  
**Responsável**: Sistema de Task Manager  
**Status**: ✅ **COMPLETO**  
**Próximo**: 🔥 **GUIDE-007 - Game Systems** 
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

