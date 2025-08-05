# Sistema de Debug

Sistema de debug e desenvolvimento para OTClient

## 📋 Índice
1. [Visão Geral](#visão-geral)
2. [API C++](#api-c)
3. [API Lua](#api-lua)
4. [Exemplos](#exemplos)
5. [Melhores Práticas](#melhores-práticas)

## 🎯 Visão Geral

Ferramentas e utilitários para debug, profiling e desenvolvimento de módulos OTClient.

## 🔧 API C++

```cpp
// Debug de widgets
void debugWidget(UIWidget* widget) {
    std::cout << "Widget: " << widget->getId() << std::endl;
    std::cout << "Position: " << widget->getPosition() << std::endl;
}
```

## 🐍 API Lua

```lua
-- Debug de variáveis
function debugVar(name, value)
    print(string.format("[DEBUG] %s = %s", name, tostring(value)))
end
```

## 💡 Exemplos

```lua
-- Sistema de debug completo
function enableDebugMode()
    g_debug.enable()
    g_debug.setLevel("verbose")
    g_debug.addCallback(onDebugEvent)
end
```

## ✅ Melhores Práticas

- Use debug apenas em desenvolvimento
- Implemente níveis de debug
- Documente funções de debug

---

**Story ID**: CORE-007  
**Categoria**: CORE  
**Status**: ✅ Completo  
**Última Atualização**: 2025-07-29
