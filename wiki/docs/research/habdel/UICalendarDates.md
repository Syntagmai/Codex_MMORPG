---
tags: [ui, calendar, dates, system, otclient, documentation, habdel]
type: documentation
status: completed
priority: maximum
created: 2025-01-27
---

# 📅 UI-019: Sistema de Calendário e Datas

> [!info] **Story ID**: UI-019  
> **Categoria**: UI  
> **Status**: ✅ Completo  
> **Prioridade**: 🔥 **MÁXIMA**

## 📋 Índice
1. [Visão Geral](#visão-geral)
2. [Arquitetura do Sistema](#arquitetura-do-sistema)
3. [Tipos de Calendário](#tipos-de-calendário)
4. [API Lua](#api-lua)
5. [Exemplos Práticos](#exemplos-práticos)
6. [Melhores Práticas](#melhores-práticas)

---

## 🎯 Visão Geral

O **Sistema de Calendário e Datas** do OTClient oferece funcionalidades para criar calendários interativos, seletores de data e widgets de agendamento. O sistema é fundamental para interfaces que precisam gerenciar datas e eventos.

### 🎨 **Características Principais**

- **UICalendar**: Widget de calendário completo
- **UIDatePicker**: Seletor de data simples
- **Sistema de Eventos**: Gerenciamento de eventos por data
- **Localização**: Suporte a diferentes formatos de data
- **Validação**: Verificação de datas válidas
- **Animações**: Transições suaves entre meses

---

## 🏗️ Arquitetura do Sistema

### 🎭 **Estrutura Hierárquica**

```
Sistema de Calendário e Datas
   │
   ├─ UICalendar
   │   ├─ Header (Mês/Ano)
   │   ├─ Dias da Semana
   │   ├─ Grid de Dias
   │   ├─ Navegação (Anterior/Próximo)
   │   └─ Eventos por Dia
   │
   ├─ UIDatePicker
   │   ├─ Campo de Data
   │   ├─ Popup de Calendário
   │   ├─ Validação
   │   └─ Formatação
   │
   ├─ Sistema de Eventos
   │   ├─ Event Storage
   │   ├─ Event Display
   │   ├─ Event Creation
   │   └─ Event Management
   │
   └─ Utilitários de Data
       ├─ Date Parsing
       ├─ Date Formatting
       ├─ Date Validation
       └─ Date Calculations
```

---

## 📅 Tipos de Calendário

### 🎯 **UICalendar (Completo)**

```lua
-- Estrutura do UICalendar
    --  Estrutura do UICalendar (traduzido)
{
    currentDate = os.date('*t'),
    selectedDate = nil,
    events = {},
    showWeekNumbers = false,
    firstDayOfWeek = 1,  -- 1 = Domingo, 2 = Segunda
    locale = 'pt_BR'
}
```

### 📅 **UIDatePicker (Simples)**

```lua
-- Estrutura do UIDatePicker
    --  Estrutura do UIDatePicker (traduzido)
{
    selectedDate = nil,
    minDate = nil,
    maxDate = nil,
    format = '%d/%m/%Y',
    placeholder = 'Selecione uma data'
}
```

---

## 🐍 API Lua

### 📦 **Métodos de UICalendar**

```lua
-- Criar calendário
local calendar = g_ui.createWidget('UICalendar', parent)

-- Configurar data atual
    --  Configurar data atual (traduzido)
calendar:setCurrentDate(os.date('*t'))

-- Selecionar data
    --  Selecionar data (traduzido)
calendar:selectDate(dateTable)

-- Adicionar evento
    --  Adicionar evento (traduzido)
calendar:addEvent(date, eventData)

-- Navegar meses
    --  Navegar meses (traduzido)
calendar:previousMonth()
calendar:nextMonth()

-- Eventos
    --  Eventos (traduzido)
calendar.onDateSelected = function(widget, date)
    print('Data selecionada:', date)
end
```

### 🎯 **Métodos de UIDatePicker**

```lua
-- Criar date picker
    --  Criar date picker (traduzido)
local datePicker = g_ui.createWidget('UIDatePicker', parent)

-- Configurar data
    --  Configurar data (traduzido)
datePicker:setDate(dateTable)
datePicker:setMinDate(minDate)
datePicker:setMaxDate(maxDate)

-- Obter data
    --  Obter data (traduzido)
local date = datePicker:getDate()

-- Eventos
    --  Eventos (traduzido)
datePicker.onDateChanged = function(widget, date)
    print('Data alterada:', date)
end
```

---

## 🚀 Exemplos Práticos

### 📅 **Calendário de Eventos**

#### Nível Basic
```lua
-- Sistema de calendário de eventos
local EventCalendar = {}

function EventCalendar.create(parent)
    local window = g_ui.createWidget('MainWindow', parent)
    window:setId('eventCalendar')
    window:setText('Calendário de Eventos')
    window:setSize({width = 400, height = 500})
    
    -- Calendário principal
    local calendar = g_ui.createWidget('UICalendar', window)
    calendar:setPosition({x = 10, y = 30})
    calendar:setSize({width = 380, height = 400})
    
    -- Eventos do calendário
    calendar.onDateSelected = function(widget, date)
        EventCalendar.showEventsForDate(date)
    end
    
    return window
end

function EventCalendar.addEvent(date, title, description)
    local eventData = {
        title = title,
        description = description,
        date = date
    }
    
    -- Adicionar ao calendário
    calendar:addEvent(date, eventData)
end

-- Uso
local calendar = EventCalendar.create(parent)
EventCalendar.addEvent({day = 15, month = 1, year = 2025}, 'Reunião', 'Reunião importante')
```

#### Nível Intermediate
```lua
-- Sistema de calendário de eventos
local EventCalendar = {}

function EventCalendar.create(parent)
    local window = g_ui.createWidget('MainWindow', parent)
    window:setId('eventCalendar')
    window:setText('Calendário de Eventos')
    window:setSize({width = 400, height = 500})
    
    -- Calendário principal
    local calendar = g_ui.createWidget('UICalendar', window)
    calendar:setPosition({x = 10, y = 30})
    calendar:setSize({width = 380, height = 400})
    
    -- Eventos do calendário
    calendar.onDateSelected = function(widget, date)
        EventCalendar.showEventsForDate(date)
    end
    
    return window
end

function EventCalendar.addEvent(date, title, description)
    local eventData = {
        title = title,
        description = description,
        date = date
    }
    
    -- Adicionar ao calendário
    calendar:addEvent(date, eventData)
end

-- Uso
local calendar = EventCalendar.create(parent)
EventCalendar.addEvent({day = 15, month = 1, year = 2025}, 'Reunião', 'Reunião importante')
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
-- Sistema de calendário de eventos
local EventCalendar = {}

function EventCalendar.create(parent)
    local window = g_ui.createWidget('MainWindow', parent)
    window:setId('eventCalendar')
    window:setText('Calendário de Eventos')
    window:setSize({width = 400, height = 500})
    
    -- Calendário principal
    local calendar = g_ui.createWidget('UICalendar', window)
    calendar:setPosition({x = 10, y = 30})
    calendar:setSize({width = 380, height = 400})
    
    -- Eventos do calendário
    calendar.onDateSelected = function(widget, date)
        EventCalendar.showEventsForDate(date)
    end
    
    return window
end

function EventCalendar.addEvent(date, title, description)
    local eventData = {
        title = title,
        description = description,
        date = date
    }
    
    -- Adicionar ao calendário
    calendar:addEvent(date, eventData)
end

-- Uso
local calendar = EventCalendar.create(parent)
EventCalendar.addEvent({day = 15, month = 1, year = 2025}, 'Reunião', 'Reunião importante')
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

### 📅 **Seletor de Data**

```lua
-- Sistema de seletor de data
    --  Sistema de seletor de data (traduzido)
local DateSelector = {}

function DateSelector.create(parent)
    -- Função: DateSelector
    local container = g_ui.createWidget('UIWidget', parent)
    
    -- Label
    --  Label (traduzido)
    local label = g_ui.createWidget('Label', container)
    label:setText('Data de Nascimento:')
    label:setPosition({x = 10, y = 10})
    
    -- Date picker
    --  Date picker (traduzido)
    local datePicker = g_ui.createWidget('UIDatePicker', container)
    datePicker:setPosition({x = 150, y = 10})
    datePicker:setSize({width = 120, height = 25})
    datePicker:setPlaceholder('dd/mm/aaaa')
    
    -- Validação
    datePicker.onDateChanged = function(widget, date)
        if DateSelector.isValidBirthDate(date) then
    -- Verificação condicional
            widget:setBorderColor('#4CAF50')
        else
            widget:setBorderColor('#F44336')
        end
    end
    
    return container
end

function DateSelector.isValidBirthDate(date)
    -- Função: DateSelector
    local currentYear = os.date('%Y')
    local birthYear = date.year
    
    return birthYear >= 1900 and birthYear <= currentYear
end

-- Uso
    --  Uso (traduzido)
local dateSelector = DateSelector.create(parent)
```

---

## ✅ Melhores Práticas

### 🎯 **Performance**

```lua
-- ✅ BOM: Usar cache para eventos
    --  ✅ BOM: Usar cache para eventos (traduzido)
local EventCache = {}

function EventCache.getEventsForMonth(year, month)
    -- Função: EventCache
    local key = year .. '-' .. month
    if not EventCache[key] then
    -- Verificação condicional
        EventCache[key] = loadEventsFromDatabase(year, month)
    end
    return EventCache[key]
end

-- ✅ BOM: Implementar lazy loading
    --  ✅ BOM: Implementar lazy loading (traduzido)
function loadCalendarEvents(calendar, year, month)
    -- Função: loadCalendarEvents
    local events = EventCache.getEventsForMonth(year, month)
    for _, event in ipairs(events) do
    -- Loop de repetição
        calendar:addEvent(event.date, event)
    end
end
```

### 🎨 **Design**

```lua
-- ✅ BOM: Usar constantes para configuração
local CALENDAR_CONFIG = {
    FIRST_DAY_OF_WEEK = 2,  -- Segunda-feira
    SHOW_WEEK_NUMBERS = false,
    LOCALE = 'pt_BR',
    DATE_FORMAT = '%d/%m/%Y'
}

-- ✅ BOM: Implementar temas
    --  ✅ BOM: Implementar temas (traduzido)
local CalendarThemes = {
    light = {
        backgroundColor = '#FFFFFF',
        textColor = '#000000',
        selectedColor = '#2196F3',
        todayColor = '#FF5722'
    },
    dark = {
        backgroundColor = '#2D2D2D',
        textColor = '#FFFFFF',
        selectedColor = '#4CAF50',
        todayColor = '#FFC107'
    }
}
```

O Sistema de Calendário e Datas do OTClient oferece ferramentas completas para criar interfaces de agendamento e seleção de datas. Use estas práticas para garantir usabilidade e performance.

> - [[UIWidget_Reference]] - Referência completa de widgets
> - [[UIFormWidgets]] - Widgets de formulário
> - [[UIEvents]] - Sistema de eventos 