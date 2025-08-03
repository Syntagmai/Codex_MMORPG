#!/usr/bin/env python3
from unicode_aliases import *
"""
Script para iniciar automaticamente a pesquisa habdel
Baseado na metodologia habdel para OTClient e Canary
"""
import os
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

class HabdelResearchStarter:
    def __init__(self):
        self.base_path = Path(__file__).parent
        self.otclient_path = self.base_path.parent.parent / "otclient"
        self.canary_path = self.base_path.parent.parent / "canary"
        self.research_plan_path = self.base_path / "research_plan.json"
        self.status_report_path = self.base_path / "status_report.md"
        
    def validate_environment(self):
        """Valida se o ambiente está pronto para pesquisa"""
        print("🔍 Validando ambiente de pesquisa...")
        
        # Verificar se os submodules estão presentes
        if not self.otclient_path.exists():
            print("❌ OTClient não encontrado!")
            return False
            
        if not self.canary_path.exists():
            print("❌ Canary não encontrado!")
            return False
            
        # Verificar se os diretórios de pesquisa existem
        otclient_research = self.base_path / "otclient"
        canary_research = self.base_path / "canary"
        
        if not otclient_research.exists():
            print("📁 Criando diretório de pesquisa OTClient...")
            otclient_research.mkdir(parents=True, exist_ok=True)
            
        if not canary_research.exists():
            print("📁 Criando diretório de pesquisa Canary...")
            canary_research.mkdir(parents=True, exist_ok=True)
            
        print("✅ Ambiente validado com sucesso!")
        return True
        
    def load_research_plan(self):
        """Carrega o plano de pesquisa"""
        if not self.research_plan_path.exists():
            print("❌ Plano de pesquisa não encontrado!")
            return None
            
        with open(self.research_plan_path, 'r', encoding='utf-8') as f:
            return json.load(f)
            
    def create_story_template(self, story_id, title, description, target_path):
        """Cria template para uma story de pesquisa"""
        template = f"""---
tags: [habdel_research, {story_id.lower()}, research_story]
type: research_story
status: pending
priority: critical
created: {datetime.now().strftime('%Y-%m-%d')}
target: {target_path}
---

# {story_id}: {title}

## 🎯 **Objetivo**
{description}

## 📋 **Tarefas de Pesquisa**

### **1. Análise do Código-Fonte**
- [ ] Identificar arquivos relevantes
- [ ] Analisar estrutura e arquitetura
- [ ] Documentar principais componentes
- [ ] Mapear dependências

### **2. Documentação Técnica**
- [ ] Criar documentação detalhada
- [ ] Incluir exemplos práticos
- [ ] Documentar APIs e interfaces
- [ ] Criar diagramas quando necessário

### **3. Validação**
- [ ] Validar completude da documentação
- [ ] Verificar qualidade técnica
- [ ] Testar exemplos práticos
- [ ] Revisar integração com wiki

## 📊 **Progresso**
- **Status**: 🔴 Pendente
- **Progresso**: 0%
- **Iniciado**: Não
- **Concluído**: Não

## 📝 **Notas de Pesquisa**
<!-- Adicionar notas durante a pesquisa -->

## 🔗 **Links Relacionados**
- [Documentação Principal](../../README.md)
- [Plano de Pesquisa](../research_plan.json)
- [Status Geral](../status_report.md)

---
*Story criada automaticamente pelo HabdelResearchStarter*
"""
        
        story_file = self.base_path / target_path / f"{story_id}.md"
        story_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(story_file, 'w', encoding='utf-8') as f:
            f.write(template)
            
        return story_file
        
    def create_research_stories(self, research_plan):
        """Cria todas as stories de pesquisa"""
        print("📝 Criando stories de pesquisa...")
        
        stories_created = 0
        
        for phase in research_plan.get('phases', []):
            phase_id = phase['id']
            phase_name = phase['name']
            stories = phase.get('stories', [])
            
            print(f"📋 Processando fase: {phase_name}")
            
            for story_id in stories:
                # Determinar target path baseado no tipo de story
                if story_id.startswith('OTCLIENT'):
                    target_path = "otclient"
                    title = f"Análise {story_id.split('-')[1]}"
                    description = f"Pesquisa profunda do sistema {story_id.split('-')[1]} no OTClient"
                elif story_id.startswith('CANARY'):
                    target_path = "canary"
                    title = f"Análise {story_id.split('-')[1]}"
                    description = f"Pesquisa profunda do sistema {story_id.split('-')[1]} no Canary"
                elif story_id.startswith('METHODOLOGY'):
                    target_path = "methodology"
                    title = f"Metodologia {story_id.split('-')[1]}"
                    description = f"Desenvolvimento da metodologia {story_id.split('-')[1]}"
                elif story_id.startswith('INTEGRATION'):
                    target_path = "integration"
                    title = f"Integração {story_id.split('-')[1]}"
                    description = f"Análise de integração {story_id.split('-')[1]}"
                else:
                    target_path = "general"
                    title = f"Pesquisa {story_id}"
                    description = f"Pesquisa geral {story_id}"
                
                story_file = self.create_story_template(story_id, title, description, target_path)
                if story_file:
                    stories_created += 1
                    print(f"  ✅ Criada: {story_id}")
                    
        print(f"📊 Total de stories criadas: {stories_created}")
        return stories_created
        
    def update_status_report(self, stories_created):
        """Atualiza o relatório de status"""
        status_content = f"""# Relatório de Status - Pesquisador Especializado

## 📊 Métricas Gerais

- **Total de Stories**: {stories_created}
- **Stories Completas**: 0
- **Progresso Geral**: 0.0%

## 🎯 Status por Categoria

### Sistema OTClient
- **Progresso**: 0.0% (0/20)
- **Status**: 🔴 Não Iniciado

### Sistema Canary
- **Progresso**: 0.0% (0/20)
- **Status**: 🔴 Não Iniciado

### Análises Comparativas
- **Progresso**: 0.0% (0/10)
- **Status**: 🔴 Não Iniciado

### Metodologia e Templates
- **Progresso**: 0.0% (0/5)
- **Status**: 🔴 Não Iniciado

## 🚀 Próximos Passos

1. **Iniciar Epic 1.1**: Configurar ambiente de pesquisa OTClient
2. **Iniciar Epic 2.1**: Configurar ambiente de pesquisa Canary
3. **Executar primeiras stories**: OTCLIENT-001 e CANARY-001
4. **Validar metodologia**: METHODOLOGY-001

## 📁 Estrutura Criada

```
wiki/habdel/
├── otclient/          # Análises OTClient (20 stories)
├── canary/            # Análises Canary (20 stories)  
├── integration/       # Comparações (10 stories)
└── methodology/       # Templates e workflows (5 stories)
```

## 🔥 **PRIORIDADES CRÍTICAS**

### **Epic 1: Pesquisa Profunda OTClient**
- **Status**: 🔴 Não Iniciado
- **Próxima Story**: OTCLIENT-001
- **Critério**: Todas as 20 stories completas

### **Epic 2: Pesquisa Profunda Canary**
- **Status**: 🔴 Não Iniciado
- **Próxima Story**: CANARY-001
- **Critério**: Todas as 20 stories completas

---
*Relatório atualizado automaticamente pelo HabdelResearchStarter - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
        
        with open(self.status_report_path, 'w', encoding='utf-8') as f:
            f.write(status_content)
            
        print("📊 Relatório de status atualizado!")
        
    def create_research_environment(self):
        """Cria ambiente completo de pesquisa"""
        print("🚀 Iniciando configuração do ambiente de pesquisa habdel...")
        
        # Validar ambiente
        if not self.validate_environment():
            print("❌ Falha na validação do ambiente!")
            return False
            
        # Carregar plano de pesquisa
        research_plan = self.load_research_plan()
        if not research_plan:
            print("❌ Falha ao carregar plano de pesquisa!")
            return False
            
        # Criar stories
        stories_created = self.create_research_stories(research_plan)
        
        # Atualizar status
        self.update_status_report(stories_created)
        
        print("✅ Ambiente de pesquisa habdel configurado com sucesso!")
        print(f"📊 Stories criadas: {stories_created}")
        print("🎯 Próximo passo: Iniciar Epic 1.1 - Configurar ambiente OTClient")
        
        return True
        
    def show_next_steps(self):
        """Mostra os próximos passos"""
        print("\n" + "="*60)
        print("🎯 PRÓXIMOS PASSOS - PESQUISA HABDEL")
        print("="*60)
        print("1. 🔥 Epic 1.1: Configurar ambiente de pesquisa OTClient")
        print("2. 🔥 Epic 2.1: Configurar ambiente de pesquisa Canary")
        print("3. ⚡ Epic 3.1: Executar METHODOLOGY-001")
        print("4. 📚 Iniciar OTCLIENT-001: Análise da Arquitetura Core")
        print("5. 📚 Iniciar CANARY-001: Análise da Arquitetura Core")
        print("\n📋 Comandos úteis:")
        print("   python wiki/habdel/habdel_research_starter.py")
        print("   python wiki/tools/update_readme.py")
        print("   python wiki/update/auto_update_all_maps.py")
        print("="*60)

def main():
    starter = HabdelResearchStarter()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print("HabdelResearchStarter - Iniciador de Pesquisa Habdel")
        print("Uso: python habdel_research_starter.py")
        print("Opções:")
        print("  --help     Mostra esta ajuda")
        return
        
    success = starter.create_research_environment()
    
    if success:
        starter.show_next_steps()
    else:
        print("❌ Falha na configuração do ambiente de pesquisa!")

if __name__ == "__main__":
    main() 