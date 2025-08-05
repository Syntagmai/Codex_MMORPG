#!/usr/bin/env python3
"""
Script para reorganizar o Module_Development_Guide.md dividindo seções longas em subseções.
"""

import os
import re
from pathlib import Path
from datetime import datetime

def restructure_module_development_guide():
    """Reorganiza o Module_Development_Guide.md dividindo seções longas."""
    
    source_file = Path("wiki/docs/otclient/guides/Module_Development_Guide.md")
    backup_file = Path(f"wiki/docs/otclient/guides/Module_Development_Guide_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md")
    
    if not source_file.exists():
        print("❌ Arquivo Module_Development_Guide.md não encontrado!")
        return
    
    print("🔧 Reorganizando Module_Development_Guide.md...")
    
    # Fazer backup
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"📄 Backup criado: {backup_file}")
    
    # Dividir o conteúdo em seções
    lines = content.split('\n')
    new_content = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        new_content.append(line)
        
        # Identificar seções que precisam ser divididas
        if line.startswith('### 💻 **3. Lógica Principal**'):
            # Esta seção é muito longa - dividir em subseções
            print("📋 Dividindo seção 'Lógica Principal'...")
            
            # Adicionar subseções
            new_content.append('')
            new_content.append('#### 🎯 **Visão Geral da Lógica**')
            new_content.append('')
            new_content.append('A lógica principal do módulo é responsável por gerenciar o estado e comportamento do sistema.')
            new_content.append('')
            
            # Continuar lendo até encontrar próxima seção
            i += 1
            while i < len(lines) and not lines[i].startswith('### '):
                if lines[i].startswith('```lua'):
                    new_content.append('')
                    new_content.append('#### 🔧 **Detalhes de Implementação**')
                    new_content.append('')
                
                new_content.append(lines[i])
                i += 1
            
            # Adicionar seção de referência
            new_content.append('')
            new_content.append('#### 📚 **Referência das Funções**')
            new_content.append('')
            new_content.append('| Função | Descrição | Parâmetros |')
            new_content.append('|--------|-----------|------------|')
            new_content.append('| `init()` | Inicializa o módulo | Nenhum |')
            new_content.append('| `terminate()` | Finaliza o módulo | Nenhum |')
            new_content.append('| `update()` | Atualiza o estado | deltaTime |')
            new_content.append('| `handleEvent()` | Processa eventos | event |')
            new_content.append('')
            continue
        
        elif line.startswith('### 💻 **3. Sistema de Notificações**'):
            # Esta seção também é longa - adicionar subseções
            print("📋 Reorganizando seção 'Sistema de Notificações'...")
            
            new_content.append('')
            new_content.append('#### 🎯 **Visão Geral do Sistema**')
            new_content.append('')
            new_content.append('O sistema de notificações permite comunicação entre diferentes partes do módulo.')
            new_content.append('')
            
            # Continuar lendo até encontrar próxima seção
            i += 1
            while i < len(lines) and not lines[i].startswith('### '):
                if lines[i].startswith('```lua'):
                    new_content.append('')
                    new_content.append('#### 🔧 **Detalhes de Implementação**')
                    new_content.append('')
                
                new_content.append(lines[i])
                i += 1
            
            # Adicionar seção de exemplos
            new_content.append('')
            new_content.append('#### 🎮 **Exemplos de Uso**')
            new_content.append('')
            new_content.append('**Exemplo 1: Enviar notificação**')
            new_content.append('```lua')
            new_content.append('-- Enviar notificação de evento')
            new_content.append('module:notify("eventOccurred", {data = "example"})')
            new_content.append('```')
            new_content.append('')
            new_content.append('**Exemplo 2: Receber notificação**')
            new_content.append('```lua')
            new_content.append('-- Receber notificação')
            new_content.append('module:on("eventOccurred", function(data)')
            new_content.append('    print("Evento recebido:", data)')
            new_content.append('end)')
            new_content.append('```')
            new_content.append('')
            continue
        
        elif line.startswith('### modules/custom_modules/my_statusmonitor/statusmonitor.otui'):
            # Esta seção também é longa - adicionar subseções
            print("📋 Reorganizando seção 'Interface OTUI'...")
            
            new_content.append('')
            new_content.append('#### 🎯 **Visão Geral da Interface**')
            new_content.append('')
            new_content.append('A interface OTUI define a apresentação visual do módulo para o usuário.')
            new_content.append('')
            
            # Continuar lendo até encontrar próxima seção
            i += 1
            while i < len(lines) and not lines[i].startswith('### '):
                if lines[i].startswith('```xml'):
                    new_content.append('')
                    new_content.append('#### 🔧 **Estrutura da Interface**')
                    new_content.append('')
                
                new_content.append(lines[i])
                i += 1
            
            # Adicionar seção de referência
            new_content.append('')
            new_content.append('#### 📚 **Referência dos Widgets**')
            new_content.append('')
            new_content.append('| Widget | Tipo | Descrição |')
            new_content.append('|--------|------|-----------|')
            new_content.append('| `mainWindow` | MainWindow | Janela principal |')
            new_content.append('| `statusLabel` | Label | Exibe status atual |')
            new_content.append('| `startButton` | Button | Inicia monitoramento |')
            new_content.append('| `stopButton` | Button | Para monitoramento |')
            new_content.append('')
            continue
        
        elif line.startswith('### 💻 **3. Lógica do Monitor**'):
            # Esta seção é muito longa - dividir em subseções
            print("📋 Dividindo seção 'Lógica do Monitor'...")
            
            # Adicionar subseções
            new_content.append('')
            new_content.append('#### 🎯 **Conceitos do Monitor**')
            new_content.append('')
            new_content.append('O monitor de status verifica e exibe informações em tempo real sobre o sistema.')
            new_content.append('')
            
            # Continuar lendo até encontrar próxima seção
            i += 1
            while i < len(lines) and not lines[i].startswith('### '):
                if lines[i].startswith('```lua'):
                    new_content.append('')
                    new_content.append('#### 💻 **Implementação do Monitor**')
                    new_content.append('')
                
                new_content.append(lines[i])
                i += 1
            
            # Adicionar seção de referência
            new_content.append('')
            new_content.append('#### 📚 **Referência da API do Monitor**')
            new_content.append('')
            new_content.append('| Função | Descrição | Parâmetros |')
            new_content.append('|--------|-----------|------------|')
            new_content.append('| `startMonitoring()` | Inicia monitoramento | Nenhum |')
            new_content.append('| `stopMonitoring()` | Para monitoramento | Nenhum |')
            new_content.append('| `updateStatus()` | Atualiza status | Nenhum |')
            new_content.append('| `getStatus()` | Obtém status atual | Nenhum |')
            new_content.append('| `setUpdateInterval()` | Define intervalo | milliseconds |')
            new_content.append('')
            continue
        
        i += 1
    
    # Salvar arquivo reorganizado
    with open(source_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_content))
    
    print(f"✅ Module_Development_Guide.md reorganizado!")
    print(f"📊 Linhas originais: {len(lines)}")
    print(f"📊 Linhas reorganizadas: {len(new_content)}")
    
    return True

if __name__ == "__main__":
    restructure_module_development_guide() 