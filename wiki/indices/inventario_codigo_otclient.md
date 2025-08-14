---
tags: [indice, inventario, otclient, enums, constantes, api, c++, lua, otui]
type: index
status: draft
level: especialista
created: 2025-08-05
updated: 2025-08-05
aliases: [inventario_otclient_codigo, otclient_code_inventory]
---

# Inventário de Código – OTClient

> Este índice orienta a varredura completa de `otclient/` para mapear enums, constantes e APIs públicas. Cada seção possui checklist e termos-semente para busca.

## Diretórios-Alvo
- `otclient/src/`
- `otclient/modules/`
- `otclient/data/`

## Tipos de Artefato
- C++: `.h`, `.cpp` (enums, `enum class`, `constexpr`, `static const`)
- Lua: `.lua` (tabelas `const_*`, mapas de ids)
- OTUI: `.otui` (propriedades e enums de widgets)

## Checklist de Varredura
- [ ] Mapear enums/constantes públicas por subsistema (C++)
- [ ] Indexar tabelas Lua `const_*` em `modules/`
- [ ] Catalogar propriedades relevantes em `.otui`
- [ ] Referenciar caminho exato do arquivo e snippet curto
- [ ] Vincular cada item às páginas da wiki existentes
- [ ] Marcar lacunas onde não há documentação

## Sementes de Busca (exemplos)
- C++: `Otc::ThingCategory`, `Otc::MagicEffect`, `Otc::Direction`, `KeyboardModifier`, `MouseButton`, `Proto::` (client)
- Lua: `g_game`, `g_ui`, `g_map`, `g_window`, `g_keyboard`, `g_mouse`, `const_`
- OTUI: `@on`, `anchors`, `focusable`, `draggable`, `autoRepeat`

## Tabela de Progresso
- A preencher durante a execução da Epic 25.

## Saídas Relacionadas
- `wiki/otclient_referencia_enums_constantes.md`
- `wiki/otclient_api_publica.md`

