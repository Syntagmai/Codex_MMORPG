# Diretrizes de Estrutura de Arquivos - Codex MMORPG

## 1. Organização de Diretórios
- **src/**: Código fonte principal
- **tests/**: Testes unitários e de integração
- **docs/**: Documentação do projeto
- **config/**: Arquivos de configuração
- **logs/**: Arquivos de log
- **temp/**: Arquivos temporários
- **backup/**: Backups automáticos
- **assets/**: Recursos estáticos (imagens, fontes, etc.)
- **data/**: Dados do projeto
- **scripts/**: Scripts utilitários

## 2. Nomenclatura de Arquivos
- Usar nomes descritivos e em inglês
- Evitar espaços (usar underscores ou hífens)
- Usar lowercase para nomes de arquivos
- Evitar caracteres especiais
- Manter nomes com menos de 255 caracteres
- Usar extensões apropriadas

## 3. Estrutura de Código
- Organizar por funcionalidade
- Separar interfaces de implementações
- Agrupar arquivos relacionados
- Usar namespaces/packages adequadamente
- Manter hierarquia lógica

## 4. Versionamento
- Não versionar arquivos temporários
- Usar .gitignore adequadamente
- Manter histórico de mudanças
- Fazer backups regulares
- Documentar mudanças estruturais

## 5. Limpeza Regular
- Remover arquivos obsoletos
- Limpar diretórios vazios
- Remover arquivos temporários
- Consolidar arquivos duplicados
- Manter estrutura organizada

## 6. Padrões de Arquivo
- **Código**: .py, .js, .cpp, .h, etc.
- **Configuração**: .json, .yaml, .ini, .conf
- **Documentação**: .md, .txt, .pdf
- **Dados**: .csv, .xml, .json
- **Recursos**: .png, .jpg, .svg, .mp3, .mp4

## 7. Segurança
- Não versionar dados sensíveis
- Usar variáveis de ambiente
- Proteger arquivos de configuração
- Validar entrada de dados
- Manter permissões adequadas

# 8. Desempenho
- Otimizar tamanho de arquivos
- Usar compressão quando apropriado
- Evitar arquivos muito grandes
- Implementar cache adequadamente
- Monitorar uso de espaço
