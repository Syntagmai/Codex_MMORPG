# Diretrizes de Configuração - Codex MMORPG

## 1. Padrões de Configuração
- **JSON**: Para configurações complexas e hierárquicas
- **YAML**: Para configurações legíveis e comentadas
- **INI**: Para configurações simples de seções
- **ENV**: Para variáveis de ambiente e segredos
- **TOML**: Para configurações com tipos de dados

## 2. Nomenclatura
- Use nomes descritivos e em inglês
- Use snake_case para chaves e variáveis
- Use UPPER_CASE para variáveis de ambiente
- Mantenha consistência entre arquivos

## 3. Validação
- Implemente validação de schema para JSON/YAML
- Valide tipos de dados e ranges
- Verifique variáveis obrigatórias
- Use valores padrão seguros

## 4. Segurança
- Nunca commite senhas ou chaves secretas
- Use variáveis de ambiente para dados sensíveis
- Valide entrada de configuração
- Implemente rotação de credenciais

## 5. Organização
- Separe configurações por ambiente (dev, test, prod)
- Use herança de configuração
- Mantenha configurações centralizadas
- Documente todas as opções

## 6. Versionamento
- Versionar schemas de configuração
- Manter compatibilidade com versões anteriores
- Documentar mudanças de configuração
- Testar configurações em CI/CD

## 7. Monitoramento
- Logar mudanças de configuração
- Monitorar valores críticos
- Alertar para configurações inválidas
- Implementar health checks

## 8. Backup e Recuperação
- Fazer backup de configurações críticas
- Implementar rollback de configurações
- Testar recuperação de configurações
- Manter histórico de mudanças

## 9. Padrões Específicos

### Timeouts
- Padrão: 30 segundos
- Máximo: 300 segundos
- Mínimo: 1 segundo

### Portas
- Padrão: 8080 (HTTP), 8443 (HTTPS)
- Range: 1024-65535
- Evitar portas reservadas

### Caminhos
- Usar separadores Unix (/)
- Caminhos relativos quando possível
- Validar existência de arquivos

### URLs
- Usar HTTPS em produção
- Validar formato de URL
- Implementar fallbacks
