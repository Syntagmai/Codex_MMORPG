---
tags: [indice, inventario, canary, enums, constantes, api, c++, lua, xml]
type: index
status: draft
level: especialista
created: 2025-08-05
updated: 2025-08-05
aliases: [inventario_canary_codigo, canary_code_inventory]
---

# Inventário de Código – Canary

> Este índice orienta a varredura completa de `canary/` para mapear enums, constantes e APIs públicas. Cada seção possui checklist e termos-semente para busca.

## Diretórios-Alvo
- `canary/src/`
- `canary/data/`
- `canary/data-canary/`
- `canary/data-otservbr-global/`
- `canary/**/XML/`

## Tipos de Artefato
- C++: `.hpp`, `.cpp` (enums, `enum class`, `constexpr`, `static const`, flags `|`, bitmasks)
- Lua: `.lua` (tabelas `const_*`, `*_t`, mapas de ids, aliases)
- XML: `.xml` (atributos de tipos, categorias, efeitos)

## Checklist de Varredura
- [ ] Mapear enums/constantes públicas por módulo (C++)
- [ ] Indexar tabelas Lua `const_*` em `data/libs/` e `data/scripts/`
- [ ] Catalogar atributos relevantes em `XML/` (itens, raids, channel, events)
- [ ] Referenciar caminho exato do arquivo e snippet curto
- [ ] Vincular cada item às páginas da wiki existentes
- [ ] Marcar lacunas onde não há documentação

## Sementes de Busca (exemplos)
- C++: `MagicEffect`, `Condition`, `ConditionType`, `WeaponType`, `Voc`, `Skull`, `Guild`, `Party`, `ItemAttribute`, `CombatType`, `Stats`, `Slot`, `Direction`, `CreatureType`, `GameState`
- Lua: `const_ani`, `const_effect`, `const_item`, `MESSAGE_`, `COLOR_`, `CONDITION_`, `COMBAT_`, `PLAYERFLAG_`, `GROUP_`, `VOCATION_`, `STORAGE_`
- XML: `effect`, `duration`, `chance`, `interval`, `max`, `type`, `id`, `attribute`

## Tabela de Progresso
- A preencher durante a execução da Epic 25.

## Saídas Relacionadas
- `wiki/canary_referencia_enums_constantes.md`
- `wiki/canary_api_publica.md`

