# Regras Principais do Sistema

## 🎯 **Regras de Escopo de Modificação**

### **📋 Permissões de Modificação**

1. **Nunca modifique arquivos fora das pastas `habdel/`, `wiki/` e `.cursor/`, exceto sob minha autorização explícita.**
2. O único arquivo na raiz do projeto que pode ser alterado é `cursor.md`.
3. Considere todo o restante do projeto como **código-fonte imutável**, pois pertence a um fork do Canary/OTClient que deve ser mantido limpo.
4. Se precisar sugerir melhorias em outros arquivos, **faça comentários apenas, sem alterar o conteúdo original**.

### **🔧 Estrutura de Pastas**

| Pasta | Permissão | Descrição |
|-------|-----------|-----------|
| `wiki/` | ✅ **Modificação permitida** | Documentação estruturada |
| `.cursor/` | ✅ **Modificação permitida** | Regras e configurações |
| `cursor.md` | ✅ **Modificação permitida** | Orquestrador principal |
| **TODOS OS OUTROS** | ❌ **Apenas leitura** | Código-fonte imutável |

### **📝 Exemplos de Uso**

#### **✅ Permitido:**
```markdown
- Criar arquivos em `wiki/`
- Modificar regras em `.cursor/rules/`
- Atualizar `cursor.md`
- Comentar sugestões em código-fonte
```

#### **❌ Proibido:**
```markdown
- Modificar arquivos em `src/`
- Alterar arquivos em `modules/`
- Editar `CMakeLists.txt`
- Modificar `README.md` original
```

### **🎯 Hierarquia de Prioridades**

1. **CRÍTICO**: Respeitar permissões de modificação
2. **IMPORTANTE**: Manter estrutura organizada
3. **OPCIONAL**: Sugerir melhorias via comentários

### **📊 Métricas de Conformidade**

- **Taxa de conformidade**: 100% obrigatória
- **Validação**: Automática antes de qualquer modificação
- **Fallback**: Modo somente leitura se permissão negada

---

## ✅ **Checklist de Validação**

- [ ] Verificar pasta de destino antes de modificar
- [ ] Confirmar permissões de modificação
- [ ] Usar estrutura de pastas correta
- [ ] Manter código-fonte imutável
- [ ] Documentar alterações quando necessário
