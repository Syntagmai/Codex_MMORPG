# File Mover Script - Guia de Uso

## Visão Geral

O **File Mover Script** é uma ferramenta Python para mover arquivos de forma eficiente usando diretórios absolutos para melhor performance. Foi criado especificamente para organizar a documentação do projeto OTClient.

## Características

- ✅ **Diretórios Absolutos**: Usa caminhos absolutos para melhor performance
- ✅ **Operações em Lote**: Move múltiplos arquivos de uma vez
- ✅ **Configuração JSON**: Suporte a arquivos de configuração
- ✅ **Modo Interativo**: Interface interativa para seleção de arquivos
- ✅ **Modo Dry-Run**: Testa operações sem mover arquivos
- ✅ **Backup Automático**: Cria backup antes de mover arquivos
- ✅ **Logging Detalhado**: Registra todas as operações
- ✅ **Tratamento de Erros**: Gerencia erros de forma robusta

## Instalação

O script não requer dependências externas além das bibliotecas padrão do Python:

```bash
# Verificar se Python 3.6+ está instalado
python --version

# O script está pronto para uso
python file_mover.py --help
```

## Uso Básico

### 1. Modo Comando Direto

```bash
# Mover arquivos específicos
python file_mover.py \
  --source "/c/Users/Dell/Documents/GitHub/otclient_doc/wiki/habdel" \
  --destination "/c/Users/Dell/Documents/GitHub/otclient_doc/wiki/habdel/documentation" \
  --files "EffectsSystem.md" "NetworkSystem.md" "ConfigurationAdvanced.md"
```

### 2. Modo Configuração

```bash
# Usar arquivo de configuração JSON
python file_mover.py --config file_mover_example_config.json
```

### 3. Modo Interativo

```bash
# Interface interativa
python file_mover.py --interactive
```

### 4. Modo Teste (Dry-Run)

```bash
# Testar sem mover arquivos
python file_mover.py \
  --source "/c/Users/Dell/Documents/GitHub/otclient_doc/wiki/habdel" \
  --destination "/c/Users/Dell/Documents/GitHub/otclient_doc/wiki/habdel/documentation" \
  --files "EffectsSystem.md" "NetworkSystem.md" \
  --dry-run
```

## Arquivo de Configuração JSON

Exemplo de configuração (`file_mover_example_config.json`):

#### Nível Basic
```json
{
  "source_dir": "/c/Users/Dell/Documents/GitHub/otclient_doc/wiki/habdel",
  "destination_dir": "/c/Users/Dell/Documents/GitHub/otclient_doc/wiki/habdel/documentation",
  "files": [
    "EffectsSystem.md",
    "NetworkSystem.md",
    "ConfigurationAdvanced.md",
    "SoundSystem.md",
    "GraphicsSystem.md"
  ],
  "description": "Moving documentation files to organized structure",
  "backup_enabled": true,
  "dry_run": false
}
```

#### Nível Intermediate
```json
{
  "source_dir": "/c/Users/Dell/Documents/GitHub/otclient_doc/wiki/habdel",
  "destination_dir": "/c/Users/Dell/Documents/GitHub/otclient_doc/wiki/habdel/documentation",
  "files": [
    "EffectsSystem.md",
    "NetworkSystem.md",
    "ConfigurationAdvanced.md",
    "SoundSystem.md",
    "GraphicsSystem.md"
  ],
  "description": "Moving documentation files to organized structure",
  "backup_enabled": true,
  "dry_run": false
}
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```json
{
  "source_dir": "/c/Users/Dell/Documents/GitHub/otclient_doc/wiki/habdel",
  "destination_dir": "/c/Users/Dell/Documents/GitHub/otclient_doc/wiki/habdel/documentation",
  "files": [
    "EffectsSystem.md",
    "NetworkSystem.md",
    "ConfigurationAdvanced.md",
    "SoundSystem.md",
    "GraphicsSystem.md"
  ],
  "description": "Moving documentation files to organized structure",
  "backup_enabled": true,
  "dry_run": false
}
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

## Uso Programático

### Importar e Usar

```python
from file_mover import FileMover

# Criar instância
mover = FileMover(dry_run=False, create_backup=True)

# Executar movimento
result = mover.move_files(
    source_dir="/c/Users/Dell/Documents/GitHub/otclient_doc/wiki/habdel",
    destination_dir="/c/Users/Dell/Documents/GitHub/otclient_doc/wiki/habdel/documentation",
    files=["EffectsSystem.md", "NetworkSystem.md"]
)

print(f"Arquivos movidos: {result['moved']}")
print(f"Arquivos falharam: {result['failed']}")
```

### Exemplos Avançados

Execute o script de exemplos para ver diferentes cenários:

```bash
python file_mover_usage_example.py
```

## Casos de Uso no Projeto OTClient

### 1. Organização da Pasta Habdel

```bash
# Mover todos os arquivos de documentação para subpastas organizadas
python file_mover.py --config habdel_organization_config.json
```

### 2. Reorganização de Módulos

```bash
# Mover módulos específicos para novas estruturas
python file_mover.py \
  --source "/c/Users/Dell/Documents/GitHub/otclient_doc/modules" \
  --destination "/c/Users/Dell/Documents/GitHub/otclient_doc/modules/organized" \
  --files "client.lua" "background.lua" "topmenu.lua"
```

### 3. Backup e Migração

```bash
# Criar backup antes de mover arquivos críticos
python file_mover.py \
  --source "/c/Users/Dell/Documents/GitHub/otclient_doc/wiki" \
  --destination "/c/Users/Dell/Documents/GitHub/otclient_doc/wiki/backup" \
  --files "important_file.md" "critical_doc.md" \
  --no-backup  # Não criar backup adicional
```

## Opções de Linha de Comando

| Opção | Descrição | Exemplo |
|-------|-----------|---------|
| `--source` | Diretório de origem (absoluto) | `--source "/path/to/source"` |
| `--destination` | Diretório de destino (absoluto) | `--destination "/path/to/dest"` |
| `--files` | Lista de arquivos para mover | `--files "file1.md" "file2.md"` |
| `--config` | Arquivo de configuração JSON | `--config "config.json"` |
| `--interactive` | Modo interativo | `--interactive` |
| `--dry-run` | Modo teste (não move arquivos) | `--dry-run` |
| `--no-backup` | Não criar backup | `--no-backup` |

## Logs e Relatórios

O script gera logs detalhados:

- **Console**: Saída em tempo real
- **Arquivo**: `file_mover.log` no diretório atual
- **Backup**: Diretório `backup_YYYYMMDD_HHMMSS` no diretório de origem

### Exemplo de Log

```
2024-01-15 10:30:15 - INFO - Starting file move operation:
2024-01-15 10:30:15 - INFO - Source: /c/Users/Dell/Documents/GitHub/otclient_doc/wiki/habdel
2024-01-15 10:30:15 - INFO - Destination: /c/Users/Dell/Documents/GitHub/otclient_doc/wiki/habdel/documentation
2024-01-15 10:30:15 - INFO - Files: 3 files
2024-01-15 10:30:15 - INFO - Backup directory created: /c/Users/Dell/Documents/GitHub/otclient_doc/wiki/habdel/backup_20240115_103015
2024-01-15 10:30:15 - INFO - Successfully moved: EffectsSystem.md
2024-01-15 10:30:15 - INFO - Successfully moved: NetworkSystem.md
2024-01-15 10:30:15 - INFO - Successfully moved: ConfigurationAdvanced.md
2024-01-15 10:30:15 - INFO - Operation completed:
2024-01-15 10:30:15 - INFO -   Successfully moved: 3 files
2024-01-15 10:30:15 - INFO -   Failed: 0 files
```

## Boas Práticas

### 1. Sempre Use Dry-Run Primeiro

```bash
# Teste antes de executar
python file_mover.py --config config.json --dry-run
```

### 2. Use Diretórios Absolutos

```bash
# ✅ Correto - Diretório absoluto
--source "/c/Users/Dell/Documents/GitHub/otclient_doc/wiki/habdel"

# ❌ Incorreto - Diretório relativo
--source "wiki/habdel"
```

### 3. Mantenha Backups

```bash
# ✅ Recomendado - Backup automático
python file_mover.py --config config.json

# ⚠️ Cuidado - Sem backup
python file_mover.py --config config.json --no-backup
```

### 4. Valide Configurações

```bash
# Verificar se arquivos existem
python file_mover.py --config config.json --dry-run
```

## Tratamento de Erros

O script trata automaticamente:

- ✅ Diretórios inexistentes (cria automaticamente)
- ✅ Arquivos inexistentes (registra erro e continua)
- ✅ Permissões insuficientes (registra erro)
- ✅ Espaço em disco insuficiente (registra erro)
- ✅ Arquivos em uso (registra erro)

## Integração com Agentes BMAD

O script pode ser integrado com os agentes BMAD:

```python
# Exemplo de integração com agente de organização
from file_mover import FileMover

class HabdelOrganizerAgent:
    def organize_documentation(self):
        mover = FileMover(dry_run=False, create_backup=True)
        
        # Organizar por categoria
        categories = {
            "ui": ["UIButton.md", "UITextEdit.md", "UIWidget.md"],
            "systems": ["EffectsSystem.md", "NetworkSystem.md", "SoundSystem.md"],
            "guides": ["BestPractices.md", "FirstModule.md", "GettingStarted.md"]
        }
        
        for category, files in categories.items():
            destination = f"/path/to/documentation/{category}"
            result = mover.move_files(source_dir, destination, files)
            print(f"Category {category}: {result}")
```

## Troubleshooting

### Problema: "Source directory must be absolute"

**Solução**: Use caminhos absolutos completos

```bash
# ✅ Correto
--source "/c/Users/Dell/Documents/GitHub/otclient_doc/wiki/habdel"

# ❌ Incorreto  
--source "wiki/habdel"
```

### Problema: "File does not exist"

**Solução**: Verifique se os arquivos existem no diretório de origem

```bash
# Listar arquivos disponíveis
ls /c/Users/Dell/Documents/GitHub/otclient_doc/wiki/habdel/*.md
```

### Problema: "Cannot create destination directory"

**Solução**: Verifique permissões e espaço em disco

```bash
# Verificar permissões
ls -la /c/Users/Dell/Documents/GitHub/otclient_doc/wiki/habdel/

# Verificar espaço em disco
df -h
```

## Contribuição

Para contribuir com melhorias no script:

1. Teste com `--dry-run` primeiro
2. Mantenha compatibilidade com Python 3.6+
3. Adicione logs detalhados para novas funcionalidades
4. Atualize este README com novas opções

## Licença

Este script faz parte do projeto OTClient e segue as mesmas diretrizes de licenciamento. 
## 🔗 **Links Automáticos**

> [!info] **Links Gerados Automaticamente**
> Estes links foram criados automaticamente pelo sistema de linkagem da categoria **UI_Systems**

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]
- [[../maps/styles_index|Índice de Estilos]]
- [[../maps/search_index|Busca por UI Systems]]

### **🧭 Navegação**
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]
- [[../maps/category_indices|Índices por Categoria]]
- [[../maps/relationships|Relacionamentos]]

### **📊 Métricas da Categoria**
- **Categoria**: UI_Systems
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

