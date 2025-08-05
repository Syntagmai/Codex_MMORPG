# Regras de Otimização de Tokens

## 🎯 **Objetivo**

Implementar estratégia **20/80** para otimização de tokens:
- **20% de mudanças** que geram **80% de economia** de tokens
- **Inglês para IA** (scripts, mapas, metadados)
- **Português para usuário** (documentação final, tags, aliases)

---

## 📋 **Regras Principais**

### 🔄 **Estratégia de Linguagem**

1. **Para IA (Inglês)**:
   - Scripts Python
   - Metadados JSON
   - Descrições técnicas
   - Comentários de código
   - Nomes de variáveis/funções

2. **Para Usuário (Português)**:
   - Documentação final da wiki
   - Tags de navegação
   - Aliases de busca
   - Títulos de documentos
   - Explicações no chat

### 📊 **Otimizações Específicas**

#### **Mapas JSON**
- ✅ **Metadados**: Inglês (IA)
- ✅ **Descrições**: Inglês (IA)
- ✅ **Tags**: Português (usuário)
- ✅ **Aliases**: Português (usuário)
- ✅ **Categorias**: Inglês (IA)

#### **Scripts Python**
- ✅ **Comentários**: Português (usuário)
- ✅ **Strings de log**: Português (usuário)
- ✅ **Nomes de funções**: Inglês (IA)
- ✅ **Variáveis**: Inglês (IA)

#### **Documentação Wiki**
- ✅ **Conteúdo**: Português (usuário)
- ✅ **Títulos**: Português (usuário)
- ✅ **Tags**: Português (usuário)
- ✅ **Frontmatter**: Inglês (IA)

---

## 🛠️ **Implementação**

### **Script de Otimização**
```python
# wiki/update/optimize_maps_for_tokens.py
# Converte metadados para inglês mantendo tags em português
```

### **Ordem de Execução**
1. Gerar mapas JSON (inglês para IA)
2. Otimizar tokens (converter metadados)
3. Manter tags/aliases em português

### **Validação**
- Verificar economia de tokens
- Manter funcionalidade
- Preservar experiência do usuário

---

## 📈 **Benefícios Esperados**

### **Economia de Tokens**
- **Metadados**: ~40% redução
- **Descrições**: ~30% redução
- **Total estimado**: ~25% economia

### **Manutenção**
- **Scripts**: Mais legíveis para IA
- **Documentação**: Acessível ao usuário
- **Tags**: Navegação intuitiva

### **Escalabilidade**
- **Novos mapas**: Seguir padrão
- **Atualizações**: Automáticas
- **Consistência**: Garantida

---

## ⚠️ **Exceções e Limitações**

### **Não Otimizar**
- Tags de navegação (português)
- Aliases de busca (português)
- Títulos de documentos (português)
- Comentários de usuário (português)

### **Sempre Otimizar**
- Metadados JSON (inglês)
- Descrições técnicas (inglês)
- Nomes de funções (inglês)
- Variáveis de sistema (inglês)

---

## 🔄 **Processo de Atualização**

### **Automático**
1. Scripts geram mapas em inglês
2. Otimizador converte metadados
3. Tags/aliases mantidos em português
4. Validação de integridade

### **Manual**
1. Verificar economia de tokens
2. Testar funcionalidade
3. Validar experiência do usuário
4. Ajustar se necessário

---

## 📊 **Métricas de Sucesso**

### **Quantitativas**
- Redução de tokens: >20%
- Tempo de processamento: <5s
- Taxa de erro: <1%

### **Qualitativas**
- Funcionalidade preservada
- Experiência do usuário mantida
- Navegação intuitiva
- Documentação clara

---

## 🎯 **Próximos Passos**

1. **Implementar** otimização automática
2. **Monitorar** economia de tokens
3. **Ajustar** estratégia conforme necessário
4. **Expandir** para outros mapas
5. **Documentar** resultados

---

## 📝 **Exemplos**

### **Antes (Português)**
```json
{
  "metadata": {
    "description": "Índice de tags da wiki do OTClient"
  },
  "categories": {
    "ui": {
      "name": "Interface do Usuário"
    }
  }
}
```

### **Depois (Otimizado)**
```json
{
  "metadata": {
    "description": "OTClient wiki tags index"
  },
  "categories": {
    "ui": {
      "name": "User Interface"
    }
  },
  "tags": ["interface", "usuário", "widgets"] // Mantido em português
}
```

---

## ✅ **Checklist de Implementação**

- [ ] Script de otimização criado
- [ ] Regras definidas
- [ ] Processo automatizado
- [ ] Validação implementada
- [ ] Documentação atualizada
- [ ] Testes realizados
- [ ] Métricas coletadas
- [ ] Ajustes feitos 