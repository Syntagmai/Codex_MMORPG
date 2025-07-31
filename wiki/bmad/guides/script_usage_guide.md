---
tags: [bmad, guide, scripts, automation, system]
type: guide
aliases: [Script Usage Guide, Guia de Uso dos Scripts]
status: active
---

# Guia de Uso dos Scripts de Automação

## 📋 Visão Geral

Este guia fornece instruções detalhadas para usar os scripts de automação do sistema OTClient Documentation. Todos os scripts estão localizados na pasta `wiki/update/` e são projetados para automatizar tarefas comuns de manutenção e desenvolvimento.

## 🎯 Scripts Disponíveis

### **Scripts Principais**

#### 1. **auto_update_all_maps.py**
**Propósito**: Atualiza todos os mapas JSON do sistema
**Uso**: `python auto_update_all_maps.py`
**Frequência**: Diária ou após mudanças significativas

#### 2. **optimize_json_maps.py**
**Propósito**: Otimiza mapas JSON grandes para melhor performance
**Uso**: `python optimize_json_maps.py`
**Frequência**: Semanal ou quando necessário

#### 3. **enhanced_intelligent_orchestrator.py**
**Propósito**: Orquestração inteligente de tarefas
**Uso**: `python enhanced_intelligent_orchestrator.py`
**Frequência**: Conforme necessário

#### 4. **agent_organizer.py**
**Propósito**: Organiza e gerencia agentes BMAD
**Uso**: `python agent_organizer.py`
**Frequência**: Quando novos agentes são criados

### **Scripts Especializados**

#### 5. **update_source_index.py**
**Propósito**: Atualiza índice do código-fonte
**Uso**: `python update_source_index.py`
**Frequência**: Após mudanças no código

#### 6. **update_wiki_maps.py**
**Propósito**: Atualiza mapas da wiki
**Uso**: `python update_wiki_maps.py`
**Frequência**: Após mudanças na documentação

#### 7. **cleanup_system.py**
**Propósito**: Limpa arquivos temporários e organiza logs
**Uso**: `python cleanup_system.py`
**Frequência**: Semanal

## 🔧 Configuração Inicial

### **Requisitos do Sistema**
```bash
# Python 3.8 ou superior
python --version

# Módulos necessários (já incluídos no Python padrão)
import json
import os
import pathlib
import time
import logging
```

### **Estrutura de Diretórios**
```
wiki/update/
├── scripts/                    # Scripts principais
├── logs/                      # Logs de execução
├── temp/                      # Arquivos temporários
└── config/                    # Configurações
```

## 📝 Como Usar

### **Execução Básica**

1. **Navegar para o diretório**:
   ```bash
   cd wiki/update
   ```

2. **Executar script**:
   ```bash
   python nome_do_script.py
   ```

3. **Verificar logs**:
   ```bash
   cat logs/script_log.txt
   ```

### **Execução com Parâmetros**

#### **Otimização de Mapas**
```bash
# Otimização automática
python optimize_json_maps.py

# Otimização com estratégia específica
python optimize_json_maps.py --strategy compress

# Otimização com threshold personalizado
python optimize_json_maps.py --threshold 200
```

#### **Atualização de Mapas**
```bash
# Atualização completa
python auto_update_all_maps.py

# Atualização específica
python update_wiki_maps.py --type documentation

# Atualização com backup
python update_source_index.py --backup
```

### **Execução Programada**

#### **Windows (Task Scheduler)**
```batch
# Criar tarefa agendada
schtasks /create /tn "OTClient Maps Update" /tr "python C:\path\to\auto_update_all_maps.py" /sc daily /st 02:00
```

#### **Linux/Mac (Cron)**
```bash
# Adicionar ao crontab
0 2 * * * cd /path/to/wiki/update && python auto_update_all_maps.py
```

## 📊 Monitoramento

### **Logs de Execução**
Todos os scripts geram logs detalhados em:
- `wiki/update/logs/` - Logs gerais
- `wiki/log/` - Relatórios de conclusão

### **Verificação de Status**
```bash
# Verificar último log
tail -f logs/script_log.txt

# Verificar relatórios
ls -la ../log/*.md
```

### **Métricas de Performance**
- **Tempo de execução**: Registrado em cada log
- **Arquivos processados**: Contagem detalhada
- **Erros encontrados**: Lista de problemas
- **Economia de espaço**: Para scripts de otimização

## 🚨 Tratamento de Erros

### **Erros Comuns**

#### **1. Arquivo não encontrado**
```bash
# Solução: Verificar caminhos
python -c "import os; print(os.getcwd())"
```

#### **2. Permissão negada**
```bash
# Solução: Verificar permissões
ls -la nome_do_script.py
chmod +x nome_do_script.py
```

#### **3. Módulo não encontrado**
```bash
# Solução: Verificar Python
python -c "import json, os, pathlib; print('OK')"
```

### **Recuperação Automática**
Os scripts incluem:
- **Backup automático** antes de modificações
- **Retry automático** para operações falhadas
- **Rollback** em caso de erro crítico

## 🔧 Configuração Avançada

### **Variáveis de Ambiente**
```bash
# Configurar variáveis
export OTCLIENT_WIKI_PATH="/path/to/wiki"
export LOG_LEVEL="INFO"
export BACKUP_ENABLED="true"
```

### **Arquivo de Configuração**
```json
{
  "scripts": {
    "auto_update_all_maps": {
      "enabled": true,
      "timeout": 3600,
      "retry_attempts": 3
    },
    "optimize_json_maps": {
      "enabled": true,
      "compression_threshold": 100000,
      "chunk_size": 1000
    }
  },
  "logging": {
    "level": "INFO",
    "file": "logs/script.log",
    "max_size": "10MB"
  }
}
```

## 📈 Otimização de Performance

### **Dicas para Uso Eficiente**

1. **Executar em horários de baixo uso**
2. **Usar otimização incremental** quando possível
3. **Monitorar uso de recursos** durante execução
4. **Limpar logs antigos** regularmente

### **Configurações Recomendadas**
```bash
# Para sistemas com recursos limitados
python optimize_json_maps.py --chunk-size 500 --compression-level 6

# Para execução rápida
python auto_update_all_maps.py --parallel --max-workers 4
```

## 🔗 Integração com Outros Sistemas

### **Git Hooks**
```bash
# Pre-commit hook
#!/bin/bash
cd wiki/update
python update_wiki_maps.py --quick
```

### **CI/CD Pipeline**
```yaml
# GitHub Actions
- name: Update Maps
  run: |
    cd wiki/update
    python auto_update_all_maps.py
    python optimize_json_maps.py
```

## 📚 Exemplos Práticos

### **Exemplo 1: Atualização Diária**
```bash
#!/bin/bash
cd /path/to/wiki/update

# Atualizar mapas
python auto_update_all_maps.py

# Otimizar se necessário
python optimize_json_maps.py --auto

# Limpar logs antigos
python cleanup_system.py --older-than 7
```

### **Exemplo 2: Manutenção Semanal**
```bash
#!/bin/bash
cd /path/to/wiki/update

# Backup completo
python backup_system.py --full

# Atualização completa
python auto_update_all_maps.py --force

# Otimização completa
python optimize_json_maps.py --strategy both

# Relatório de status
python generate_status_report.py
```

### **Exemplo 3: Recuperação de Erro**
```bash
#!/bin/bash
cd /path/to/wiki/update

# Verificar logs de erro
grep "ERROR" logs/*.log

# Restaurar backup se necessário
python restore_backup.py --latest

# Reexecutar script com debug
python auto_update_all_maps.py --debug --verbose
```

## 🆘 Suporte e Troubleshooting

### **Comandos de Diagnóstico**
```bash
# Verificar saúde do sistema
python diagnose_system.py

# Verificar integridade dos mapas
python validate_maps.py

# Testar conectividade
python test_connectivity.py
```

### **Contatos de Suporte**
- **Documentação**: Verificar este guia
- **Logs**: Consultar arquivos de log
- **Issues**: Criar issue no repositório

---

## 🔄 Atualizações

### **Histórico de Versões**
- **v1.0**: Guia inicial
- **v1.1**: Adicionado exemplos práticos
- **v1.2**: Incluído troubleshooting

### **Próximas Melhorias**
- Interface web para execução
- Dashboard de monitoramento
- Integração com Slack/Discord

---

*Guia criado pelo Sistema BMAD - OTClient Documentation* 