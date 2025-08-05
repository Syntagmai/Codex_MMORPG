# Diretrizes de Documentação - Codex MMORPG

## 1. Estrutura de Documentos

### Frontmatter Obrigatório
```yaml
---
tags: [categoria, subcategoria, tipo]
type: documentation
status: active|draft|archived
priority: critical|high|medium|low
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

### Estrutura de Títulos
- Use `#` para título principal
- Use `##` para seções principais
- Use `###` para subseções
- Use `####` para sub-subseções
- Máximo 4 níveis de profundidade

## 2. Formatação

### Links
- Links internos: `[texto](caminho/arquivo.md)`
- Links externos: `[texto](https://url.com)`
- Links da wiki: `[[página]]` ou `[[página|texto]]`

### Imagens
- Use formato: `![alt](caminho/imagem.png)`
- Mantenha imagens em `wiki/images/`
- Use nomes descritivos

### Código
- Inline: `` `código` ``
- Blocos: ```python
código
```
- Especifique linguagem quando relevante

## 3. Conteúdo

### Qualidade
- Seja claro e conciso
- Use linguagem técnica apropriada
- Inclua exemplos práticos
- Mantenha consistência

### Organização
- Use listas para enumerar itens
- Use tabelas para dados estruturados
- Use callouts para informações importantes
- Mantenha hierarquia lógica

## 4. Manutenção

### Atualizações
- Atualize `updated` no frontmatter
- Revise links regularmente
- Verifique conteúdo desatualizado
- Mantenha tags atualizadas

### Versionamento
- Use controle de versão
- Documente mudanças importantes
- Mantenha histórico de alterações
- Use branches para mudanças grandes

## 5. Padrões Específicos

### Documentação Técnica
- Inclua pré-requisitos
- Forneça exemplos completos
- Documente limitações
- Inclua troubleshooting

### Guias de Usuário
- Use linguagem simples
- Inclua screenshots
- Forneça passo-a-passo
- Antecipe problemas comuns

### Documentação de API
- Documente todos os endpoints
- Inclua exemplos de request/response
- Documente códigos de erro
- Forneça SDK examples

## 6. Ferramentas

### Validação
- Use linters de markdown
- Verifique links automaticamente
- Valide frontmatter
- Teste exemplos de código

### Geração
- Use geradores automáticos
- Mantenha índices atualizados
- Gere documentação de API
- Automatize atualizações

## 7. Boas Práticas

### Escrita
- Use voz ativa
- Seja específico
- Evite jargão desnecessário
- Mantenha tom consistente

### Organização
- Agrupe conteúdo relacionado
- Use navegação clara
- Mantenha documentos focados
- Evite duplicação

### Acessibilidade
- Use alt text em imagens
- Mantenha contraste adequado
- Use estrutura semântica
- Teste com leitores de tela
