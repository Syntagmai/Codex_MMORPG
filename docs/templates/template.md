# Template para Novas Regras

## 📋 Estrutura Padrão

Use este template ao criar novas regras na pasta `.cursor/rules/`:

```markdown
## Regras de [Nome da Área]

1. **Regra Principal**: Descrição clara da regra principal
2. **Regra Secundária**: Descrição da regra secundária
3. **Regra de Exceção**: Descrição de exceções ou casos especiais
4. **Regra de Comentário**: Como fazer comentários ou sugestões
```

---

## 🎯 Exemplo Baseado no Modelo Atual

```markdown
## Regras de Escopo de Modificação

1. **Nunca modifique arquivos fora das pastas `habdel/`, `wiki/` e `.cursor/`, exceto sob minha autorização explícita.**
2. O único arquivo na raiz do projeto que pode ser alterado é `cursor.md`.
3. Considere todo o restante do projeto como **código-fonte imutável**, pois pertence a um fork do Canary/OTClient que deve ser mantido limpo.
4. Se precisar sugerir melhorias em outros arquivos, **faça comentários apenas, sem alterar o conteúdo original**.
```

---

## 📝 Template para Novas Regras

```markdown
## Regras de [Área Específica]

1. **[Regra Principal]**: Descrição detalhada da regra principal
2. **[Regra Secundária]**: Descrição da regra secundária
3. **[Regra de Exceção]**: Descrição de exceções ou casos especiais
4. **[Regra de Comentário]**: Como fazer comentários ou sugestões
```

---

## 🔄 Sistema de Atualização Automática

Quando uma nova regra for criada:

1. **Criar arquivo** na pasta `.cursor/rules/`
2. **Usar este template** como base
3. **Adicionar referência** no `cursor.md`
4. **Manter consistência** com regras existentes

---

## 📋 Checklist para Nova Regra

- [ ] Nome descritivo para o arquivo (ex: `documentation-rules.md`)
- [ ] Estrutura seguindo o template
- [ ] Regras claras e específicas
- [ ] Referência adicionada no `cursor.md`
- [ ] Testado e validado 