#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para atualizar regras e navegação após reorganização da estrutura
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Set

class SystemUpdater:
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.new_structure = {
            'wiki': 'Conteúdo educacional (Obsidian)',
            'habdel': 'Metodologia de pesquisa e stories',
            'docs': 'Documentação interna do sistema',
            'logs': 'Relatórios, monitoramento e alertas',
            'data': 'Dados do sistema',
            'scripts': 'Scripts e ferramentas',
            'backup': 'Sistema de backup',
            'temp': 'Arquivos temporários'
        }
        
    def update_cursor_md(self):
        """Atualizar cursor.md com nova estrutura"""
        cursor_path = self.project_root / "cursor.md"
        
        if not cursor_path.exists():
            print("❌ cursor.md não encontrado")
            return False
            
        with open(cursor_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Atualizar referências de pastas
        updates = {
            'wiki/dashboard/task_master.md': 'logs/reports/task_master.md',
            'wiki/dashboard/integrated_task_manager.md': 'docs/dashboard/integrated_task_manager.md',
            'wiki/maps/': 'data/maps/',
            'wiki/update/': 'scripts/',
            'wiki/bmad/': 'docs/bmad/',
            'wiki/log/': 'logs/',
            'wiki/backup/': 'backup/'
        }
        
        for old_path, new_path in updates.items():
            content = content.replace(old_path, new_path)
        
        # Adicionar seção sobre nova estrutura
        new_structure_section = """
## 📁 **NOVA ESTRUTURA DO PROJETO (PÓS-REORGANIZAÇÃO)**

### **🎯 Estrutura Atualizada:**
- **`wiki/`** - Conteúdo educacional (Obsidian)
- **`habdel/`** - Metodologia de pesquisa e stories
- **`docs/`** - Documentação interna do sistema
- **`logs/`** - Relatórios, monitoramento e alertas
- **`data/`** - Dados do sistema
- **`scripts/`** - Scripts e ferramentas
- **`backup/`** - Sistema de backup
- **`temp/`** - Arquivos temporários

### **🔄 Mudanças Principais:**
- **Task Master**: Movido para `logs/reports/task_master.md`
- **Documentação**: Separada em `docs/` por categoria
- **Guias**: Movidos para `docs/guides/`
- **Sistemas**: Movidos para `docs/systems/`
- **Relatórios**: Centralizados em `logs/reports/`
- **Scripts**: Centralizados em `scripts/`

### **📋 Navegação Atualizada:**
- **Task Master**: `logs/reports/task_master.md`
- **Dashboard**: `docs/dashboard/integrated_task_manager.md`
- **Guias**: `docs/guides/`
- **Sistemas**: `docs/systems/`
- **Mapas**: `data/maps/`
- **Scripts**: `scripts/`
"""
        
        # Inserir nova seção após o índice
        if "## 🚀 **ÍNDICE DE NAVEGAÇÃO RÁPIDA**" in content:
            content = content.replace(
                "## 🚀 **ÍNDICE DE NAVEGAÇÃO RÁPIDA**",
                "## 🚀 **ÍNDICE DE NAVEGAÇÃO RÁPIDA**" + new_structure_section
            )
        
        with open(cursor_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ cursor.md atualizado com nova estrutura")
        return True
    
    def update_rules_files(self):
        """Atualizar arquivos de regras com novos caminhos"""
        rules_dir = self.project_root / ".cursor" / "rules"
        
        if not rules_dir.exists():
            print("❌ Pasta .cursor/rules não encontrada")
            return False
        
        # Mapeamento de atualizações
        path_updates = {
            'wiki/dashboard/': 'logs/reports/',
            'wiki/maps/': 'data/maps/',
            'wiki/update/': 'scripts/',
            'wiki/bmad/': 'docs/bmad/',
            'wiki/log/': 'logs/',
            'wiki/backup/': 'backup/',
            'wiki/guides/': 'docs/guides/',
            'wiki/systems/': 'docs/systems/'
        }
        
        updated_files = 0
        for rule_file in rules_dir.glob("*.md"):
            try:
                with open(rule_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Aplicar atualizações de caminhos
                for old_path, new_path in path_updates.items():
                    content = content.replace(old_path, new_path)
                
                if content != original_content:
                    with open(rule_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    updated_files += 1
                    print(f"✅ {rule_file.name} atualizado")
                    
            except Exception as e:
                print(f"❌ Erro ao atualizar {rule_file.name}: {e}")
        
        print(f"✅ {updated_files} arquivos de regras atualizados")
        return True
    
    def create_navigation_index(self):
        """Criar índice de navegação atualizado"""
        navigation_data = {
            "structure": self.new_structure,
            "key_files": {
                "task_master": "logs/reports/task_master.md",
                "dashboard": "docs/dashboard/integrated_task_manager.md",
                "cursor": "cursor.md",
                "rules": ".cursor/rules/"
            },
            "documentation": {
                "guides": "docs/guides/",
                "systems": "docs/systems/",
                "templates": "docs/templates/",
                "workflows": "docs/workflows/",
                "bmad": "docs/bmad/"
            },
            "data": {
                "maps": "data/maps/",
                "consolidated": "data/consolidated/"
            },
            "logs": {
                "reports": "logs/reports/",
                "monitoring": "logs/monitoring/",
                "alerts": "logs/alerts/",
                "metrics": "logs/metrics/"
            },
            "scripts": "scripts/",
            "backup": "backup/",
            "temp": "temp/"
        }
        
        nav_file = self.project_root / "data" / "maps" / "navigation_index.json"
        nav_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(nav_file, 'w', encoding='utf-8') as f:
            json.dump(navigation_data, f, indent=2, ensure_ascii=False)
        
        print("✅ Índice de navegação criado")
        return True
    
    def validate_system(self):
        """Validar se todos os sistemas ainda funcionam"""
        print("\n🔍 Validando sistema...")
        
        # Verificar arquivos críticos
        critical_files = [
            "logs/reports/task_master.md",
            "docs/dashboard/integrated_task_manager.md",
            "cursor.md",
            ".cursor/rules/"
        ]
        
        missing_files = []
        for file_path in critical_files:
            if not (self.project_root / file_path).exists():
                missing_files.append(file_path)
        
        if missing_files:
            print(f"❌ Arquivos críticos não encontrados: {missing_files}")
            return False
        
        # Verificar pastas principais
        main_dirs = list(self.new_structure.keys())
        missing_dirs = []
        
        for dir_name in main_dirs:
            if not (self.project_root / dir_name).exists():
                missing_dirs.append(dir_name)
        
        if missing_dirs:
            print(f"❌ Pastas principais não encontradas: {missing_dirs}")
            return False
        
        print("✅ Sistema validado - todos os componentes encontrados")
        return True
    
    def create_recovery_guide(self):
        """Criar guia de recuperação para arquivos movidos"""
        recovery_guide = """# 🔄 Guia de Recuperação - Arquivos Movidos

## 📁 **Onde Encontrar Arquivos Após Reorganização**

### **📚 Documentação Educacional (Wiki Original)**
**Localização Atual**: `wiki/`
- Cursos principais (canary_course.md, fundamentals_course.md, etc.)
- Visões gerais educacionais
- Conteúdo para Obsidian

### **🔬 Metodologia Habdel**
**Localização Atual**: `habdel/`
- Stories CANARY-* (pesquisa sobre servidor Canary)
- Stories INTEGRATION-* (integração de sistemas)
- Stories OTCLIENT-* (pesquisa sobre cliente OTClient)
- Stories METHODOLOGY-* (metodologia de pesquisa)
- Agentes de pesquisa (researcher_agent.md, task_researcher_agent.md)

### **📖 Guias e Tutoriais**
**Localização Atual**: `docs/guides/`
- Getting Started Guides
- Module Development Guides
- UI System Guides
- Graphics System Guides
- Configuration Guides
- Todos os guias técnicos

### **⚙️ Sistemas e Arquitetura**
**Localização Atual**: `docs/systems/`
- Análises de sistemas OTClient
- Guias de sistemas de jogo
- Documentação de arquitetura
- Padrões de design

### **📊 Relatórios e Logs**
**Localização Atual**: `logs/reports/`
- Task Master (task_master.md)
- Relatórios de análise
- Relatórios de validação
- Relatórios de progresso

### **🔧 Scripts e Ferramentas**
**Localização Atual**: `scripts/`
- Agentes inteligentes
- Ferramentas de validação
- Utilitários de manutenção
- Sistemas de automação

### **🗺️ Mapas e Dados**
**Localização Atual**: `data/maps/`
- Mapas JSON de navegação
- Índices de busca
- Dados estruturados

### **💾 Dados Consolidados**
**Localização Atual**: `data/consolidated/`
- Dados agregados
- Configurações consolidadas

## 🔍 **Como Buscar Arquivos Específicos**

### **Para Documentação OTClient:**
1. Verificar `docs/guides/` para guias
2. Verificar `docs/systems/` para análises
3. Verificar `habdel/` para pesquisa OTCLIENT-*

### **Para Documentação Canary:**
1. Verificar `habdel/` para pesquisa CANARY-*
2. Verificar `docs/guides/` para guias de integração

### **Para Sistemas e Agentes:**
1. Verificar `docs/bmad/` para sistema BMAD
2. Verificar `scripts/` para agentes automatizados
3. Verificar `docs/workflows/` para fluxos de trabalho

## ✅ **Sistema de Navegação Atualizado**

Todos os arquivos foram preservados e reorganizados de forma lógica:
- **Conteúdo educacional** → `wiki/`
- **Pesquisa e metodologia** → `habdel/`
- **Documentação técnica** → `docs/`
- **Relatórios e logs** → `logs/`
- **Scripts e ferramentas** → `scripts/`
- **Dados e mapas** → `data/`

---
*Última atualização: 2025-08-05*
*Epic 22 - Reorganização Completa de Diretórios*
"""
        
        recovery_file = self.project_root / "RECOVERY_GUIDE.md"
        with open(recovery_file, 'w', encoding='utf-8') as f:
            f.write(recovery_guide)
        
        print("✅ Guia de recuperação criado: RECOVERY_GUIDE.md")
        return True
    
    def run_full_update(self):
        """Executar atualização completa do sistema"""
        print("🚀 Iniciando atualização do sistema após reorganização...")
        
        steps = [
            ("Validando sistema", self.validate_system),
            ("Atualizando cursor.md", self.update_cursor_md),
            ("Atualizando regras", self.update_rules_files),
            ("Criando índice de navegação", self.create_navigation_index),
            ("Criando guia de recuperação", self.create_recovery_guide)
        ]
        
        for step_name, step_func in steps:
            print(f"\n📋 {step_name}...")
            try:
                if step_func():
                    print(f"✅ {step_name} concluído")
                else:
                    print(f"❌ {step_name} falhou")
            except Exception as e:
                print(f"❌ Erro em {step_name}: {e}")
        
        print("\n🎉 Atualização do sistema concluída!")
        print("📖 Consulte RECOVERY_GUIDE.md para localizar arquivos movidos")

if __name__ == "__main__":
    updater = SystemUpdater()
    updater.run_full_update() 