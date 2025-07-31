## Regras da Pasta Wiki

1. **Sempre use extensão .md**: Todos os arquivos criados na pasta wiki devem ter extensão `.md` (Markdown).
2. **Use frontmatter obrigatório**: Todo arquivo deve ter frontmatter com tags, status e aliases seguindo o padrão estabelecido.
3. **Siga formatação Obsidian**: Utilize callouts, wikilinks, separadores e emojis como nos arquivos existentes.
4. **Mantenha estrutura hierárquica**: Use índices com wikilinks, seções bem definidas e separadores `---`.
5. **Proteção da pasta .obsidian**: A pasta `.obsidian/` contém configurações do programa Obsidian e **NÃO deve ser modificada** sem autorização prévia explícita.

---

## ⚠️ Proteção de Arquivos

### 📁 Pasta .obsidian
- **Localização**: `wiki/.obsidian/`
- **Propósito**: Configurações e funcionamento do programa Obsidian
- **Regra**: **NUNCA modifique** arquivos nesta pasta sem autorização prévia
- **Conteúdo**: Snippets, templates, configurações de plugins, etc.
- **Exceção**: Apenas com autorização explícita do usuário

### 📄 Arquivos Permitidos
- **Arquivos .md** na pasta `wiki/` (exceto `.obsidian/`)
- **Novos documentos** seguindo as diretrizes estabelecidas
- **Modificações** em arquivos .md existentes (seguindo padrões)

---

## 📋 Estrutura Obrigatória

### Frontmatter Padrão
```yaml
---
tags: [otclient, categoria, tipo, status]
status: completed/draft/in-progress
aliases: [Nome Alternativo, Alias 1, Alias 2]
---
```

### Estrutura de Conteúdo
```markdown
# Título do Documento

> [!info] Descrição breve do documento

## 📋 Índice
- [[#Seção 1]]
- [[#Seção 2]]

---

## Seção 1

Conteúdo aqui...

---

## Seção 2

Conteúdo aqui...

---

> [!success] Consulte também:
> - [[Documento Relacionado 1]]
> - [[Documento Relacionado 2]]
```

---

## 🎨 Elementos de Formatação Obrigatórios

### Callouts
- `> [!info]` - Informações gerais
- `> [!tip]` - Dicas e sugestões
- `> [!warning]` - Avisos importantes
- `> [!success]` - Conclusões positivas
- `> [!note]` - Notas adicionais
- `> [!example]` - Exemplos práticos

### Wikilinks
- `[[#Seção]]` - Links internos
- `[[Documento]]` - Links para outros documentos
- `[[Documento#Seção]]` - Links para seções específicas

### Separadores
- `---` - Separadores entre seções principais

### Emojis
- Use emojis para categorizar seções (📋, 🎯, 🔧, etc.)

---

## 📝 Checklist para Novos Arquivos

- [ ] Extensão `.md`
- [ ] Frontmatter com tags, status e aliases
- [ ] Título principal com `#`
- [ ] Callout informativo no início
- [ ] Índice com wikilinks
- [ ] Separadores `---` entre seções
- [ ] Emojis para categorização
- [ ] Callout de referências no final
- [ ] Linguagem clara e objetiva
- [ ] Exemplos práticos quando aplicável
- [ ] **NÃO modificar pasta `.obsidian/`** sem autorização 