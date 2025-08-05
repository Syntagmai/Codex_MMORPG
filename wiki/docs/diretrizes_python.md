# Diretrizes de Python - Codex MMORPG
## 1. Imports e Dependências
- Sempre usar imports absolutos quando possível
- Evitar imports circulares
- Usar imports específicos: `from module import function`
- Remover imports não utilizados
- Não usar imports obsoletos (unicode_aliases, etc.)

## 2. Sintaxe e Estrutura
- Usar indentação de 4 espaços (não tabs)
- Seguir PEP 8 para estilo de código
- Usar docstrings para funções e classes
- Manter linhas com máximo de 79 caracteres
- Usar nomes descritivos para variáveis e funções

## 3. Tratamento de Erros
- Usar try/except para tratamento de exceções
- Especificar tipos de exceção quando possível
- Evitar except genérico sem especificar exceção
- Usar logging para registrar erros

# 4. Desempenho
- Evitar loops desnecessários
- Usar list comprehensions quando apropriado
- Otimizar imports e dependências
- Usar geradores para grandes conjuntos de dados

## 5. Segurança
- Validar todas as entradas de usuário
- Usar prepared statements para SQL
- Evitar eval() e exec() com entrada do usuário
- Sanitizar dados antes de processar

## 6. Compatibilidade
- Usar Python 3.6+ features
- Evitar código específico de versão
- Testar em múltiplas versões do Python
- Usar type hints quando possível

## 7. Documentação
- Documentar funções e classes
- Usar docstrings no formato Google ou NumPy
- Manter README atualizado
- Documentar APIs e interfaces

## 8. Testes
- Escrever testes unitários
- Usar pytest para testes
- Manter cobertura de código alta
- Testar casos de erro e edge cases
