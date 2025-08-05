#!/usr/bin/env python3
"""
Script para reorganizar o Sound_System_Guide.md dividindo seções longas em subseções.
"""

import os
import re
from pathlib import Path
from datetime import datetime

def restructure_sound_system_guide():
    """Reorganiza o Sound_System_Guide.md dividindo seções longas."""
    
    source_file = Path("wiki/docs/otclient/guides/Sound_System_Guide.md")
    backup_file = Path(f"wiki/docs/otclient/guides/Sound_System_Guide_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md")
    
    if not source_file.exists():
        print("❌ Arquivo Sound_System_Guide.md não encontrado!")
        return
    
    print("🔧 Reorganizando Sound_System_Guide.md...")
    
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
        if line.startswith('### Exemplo 1: Gerenciador de Áudio'):
            # Esta seção é muito longa - dividir em subseções
            print("📋 Dividindo seção 'Gerenciador de Áudio'...")
            
            # Adicionar subseções
            new_content.append('')
            new_content.append('#### 🔧 **Conceitos do Gerenciador**')
            new_content.append('')
            new_content.append('O gerenciador de áudio fornece uma interface completa para controle de todos os aspectos do sistema de som.')
            new_content.append('')
            
            # Continuar lendo até encontrar próxima seção
            i += 1
            while i < len(lines) and not lines[i].startswith('### '):
                if lines[i].startswith('```lua'):
                    new_content.append('')
                    new_content.append('#### 💻 **Implementação**')
                    new_content.append('')
                
                new_content.append(lines[i])
                i += 1
            
            # Adicionar seção de referência
            new_content.append('')
            new_content.append('#### 📚 **Referência da API**')
            new_content.append('')
            new_content.append('| Função | Descrição | Parâmetros |')
            new_content.append('|--------|-----------|------------|')
            new_content.append('| `audioManager.init()` | Inicializa o gerenciador | Nenhum |')
            new_content.append('| `audioManager.setupInterface()` | Configura a interface | Nenhum |')
            new_content.append('| `audioManager.onMasterVolumeChange()` | Controla volume master | slider, value |')
            new_content.append('| `audioManager.playTestSounds()` | Reproduz sons de teste | Nenhum |')
            new_content.append('| `audioManager.applyPreset()` | Aplica preset de volume | presetName |')
            new_content.append('')
            continue
        
        elif line.startswith('### Exemplo 3: Sistema de Efeitos Sonoros 3D'):
            # Esta seção também é longa - adicionar subseções
            print("📋 Reorganizando seção 'Sistema de Efeitos Sonoros 3D'...")
            
            new_content.append('')
            new_content.append('#### 🎯 **Visão Geral**')
            new_content.append('')
            new_content.append('O sistema de efeitos sonoros 3D permite posicionamento espacial de sons para criar uma experiência imersiva.')
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
            new_content.append('#### 🎮 **Exemplos Práticos**')
            new_content.append('')
            new_content.append('**Exemplo 1: Som de passos 3D**')
            new_content.append('```lua')
            new_content.append('-- Reproduzir som de passos na posição do jogador')
            new_content.append('local playerPos = player:getPosition()')
            new_content.append('g_sounds.play3D("sounds/footsteps.ogg", playerPos, 1.0, 1.0)')
            new_content.append('```')
            new_content.append('')
            new_content.append('**Exemplo 2: Efeito de explosão**')
            new_content.append('```lua')
            new_content.append('-- Explosão com fade out')
            new_content.append('local explosionPos = {x = 100, y = 200, z = 0}')
            new_content.append('g_sounds.play3D("sounds/explosion.ogg", explosionPos, 1.0, 1.0, 3000)')
            new_content.append('```')
            new_content.append('')
            continue
        
        i += 1
    
    # Salvar arquivo reorganizado
    with open(source_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_content))
    
    print(f"✅ Sound_System_Guide.md reorganizado!")
    print(f"📊 Linhas originais: {len(lines)}")
    print(f"📊 Linhas reorganizadas: {len(new_content)}")
    
    return True

if __name__ == "__main__":
    restructure_sound_system_guide() 
## 🔗 **Links Automáticos - Scripts**

> [!info] **Script de Automação**
> Este script faz parte do sistema de automação da wiki

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]

### **🔧 Links de Scripts**
- [[../update/README|Documentação de Scripts]]
- [[../maps/scripts_index|Índice de Scripts]]
- [[../templates/README|Templates de Scripts]]

### **📊 Scripts Relacionados**
- [[../update/automatic_linkage_system.py|automatic_linkage_system.py]]
- [[../update/create_automatic_link_templates.py|create_automatic_link_templates.py]]
- [[../update/orphan_files_analyzer.py|orphan_files_analyzer.py]]
- [[../update/update_json_maps.py|update_json_maps.py]]

### **📈 Métricas do Script**
- **Nome**: restructure_sound_system_guide
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

