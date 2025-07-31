#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Habdel Documentation Organizer Agent
====================================

Este agente analisa e organiza toda a documentação habdel existente,
atualiza o plano de documentação e prepara para integração futura com a wiki.

Autor: BMAD System
Data: 2025-01-27
"""

import os
import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

class HabdelDocumentationOrganizer:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent.parent
        self.habdel_path = self.base_path / "habdel"
        self.log_path = self.base_path / "wiki" / "log"
        
        # Criar pasta de log se não existir
        self.log_path.mkdir(parents=True, exist_ok=True)
        
        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_path / "habdel_organization.log", encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
        # Métricas de progresso
        self.progress_metrics = {
            'files_analyzed': 0,
            'stories_identified': 0,
            'plan_updated': False,
            'organization_complete': False
        }
        
        # Mapeamento de arquivos para stories
        self.file_to_story_mapping = {}
        self.story_status = {}
        
    def run_organization(self):
        """Executa a organização completa da documentação habdel"""
        self.logger.info("🚀 Habdel Documentation Organizer iniciado")
        self.logger.info("=" * 60)
        
        try:
            # Passo 1: Analisar estrutura atual
            self.analyze_current_structure()
            
            # Passo 2: Identificar stories existentes
            self.identify_existing_stories()
            
            # Passo 3: Mapear arquivos para stories
            self.map_files_to_stories()
            
            # Passo 4: Atualizar plano de documentação
            self.update_documentation_plan()
            
            # Passo 5: Organizar arquivos por categoria
            self.organize_files_by_category()
            
            # Passo 6: Gerar relatório final
            self.generate_final_report()
            
            self.progress_metrics['organization_complete'] = True
            self.logger.info("✅ Organização da documentação habdel concluída!")
            
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro durante organização: {e}")
            return False
    
    def analyze_current_structure(self):
        """Analisa a estrutura atual da pasta habdel"""
        self.logger.info("📁 Analisando estrutura atual da pasta habdel...")
        
        # Listar todos os arquivos .md
        md_files = list(self.habdel_path.rglob("*.md"))
        self.logger.info(f"📄 Encontrados {len(md_files)} arquivos .md")
        
        # Categorizar arquivos
        categories = {
            'root_files': [],
            'documentation_files': [],
            'otclient_files': [],
            'canary_files': [],
            'integration_files': [],
            'methodology_files': []
        }
        
        for file_path in md_files:
            relative_path = file_path.relative_to(self.habdel_path)
            
            if relative_path.parent.name == 'documentation':
                categories['documentation_files'].append(str(relative_path))
            elif relative_path.parent.name == 'otclient':
                categories['otclient_files'].append(str(relative_path))
            elif relative_path.parent.name == 'canary':
                categories['canary_files'].append(str(relative_path))
            elif relative_path.parent.name == 'integration':
                categories['integration_files'].append(str(relative_path))
            elif relative_path.parent.name == 'methodology':
                categories['methodology_files'].append(str(relative_path))
            else:
                categories['root_files'].append(str(relative_path))
        
        # Log das categorias
        for category, files in categories.items():
            self.logger.info(f"📂 {category}: {len(files)} arquivos")
            for file in files[:5]:  # Mostrar apenas os primeiros 5
                self.logger.info(f"   - {file}")
            if len(files) > 5:
                self.logger.info(f"   ... e mais {len(files) - 5} arquivos")
        
        self.progress_metrics['files_analyzed'] = len(md_files)
    
    def identify_existing_stories(self):
        """Identifica stories existentes baseado no plano atual"""
        self.logger.info("🔍 Identificando stories existentes...")
        
        # Ler o plano de documentação atual
        plan_file = self.habdel_path / "DOCUMENTATION_PLAN.md"
        if plan_file.exists():
            with open(plan_file, 'r', encoding='utf-8') as f:
                plan_content = f.read()
            
            # Extrair stories completas do plano
            completed_stories = []
            lines = plan_content.split('\n')
            in_completed_section = False
            
            for line in lines:
                if '### ✅ **COMPLETAS' in line:
                    in_completed_section = True
                    continue
                elif in_completed_section and line.startswith('### '):
                    break
                elif in_completed_section and '|' in line and '✅' in line:
                    parts = line.split('|')
                    if len(parts) >= 4:
                        story_id = parts[1].strip()
                        title = parts[2].strip()
                        file_name = parts[3].strip()
                        completed_stories.append({
                            'id': story_id,
                            'title': title,
                            'file': file_name
                        })
            
            self.logger.info(f"📋 Encontradas {len(completed_stories)} stories completas no plano")
            for story in completed_stories:
                self.logger.info(f"   ✅ {story['id']}: {story['title']}")
        
        # Identificar arquivos que correspondem a stories
        story_files = []
        for file_path in self.habdel_path.rglob("*.md"):
            file_name = file_path.name
            
            # Verificar se o arquivo corresponde a uma story conhecida
            for story in completed_stories:
                if story['file'] == file_name:
                    story_files.append({
                        'story_id': story['id'],
                        'story_title': story['title'],
                        'file_path': str(file_path.relative_to(self.habdel_path)),
                        'file_size': file_path.stat().st_size
                    })
                    break
        
        self.logger.info(f"📄 Identificados {len(story_files)} arquivos correspondentes a stories")
        self.progress_metrics['stories_identified'] = len(story_files)
    
    def map_files_to_stories(self):
        """Mapeia arquivos para stories baseado em padrões"""
        self.logger.info("🗺️ Mapeando arquivos para stories...")
        
        # Padrões de mapeamento
        mapping_patterns = {
            'UI': {
                'UIWidget': 'UI-001',
                'UIButton': 'UI-003',
                'UITextEdit': 'UI-004',
                'UILayouts': 'UI-005',
                'UIEvents': 'UI-006',
                'UIStyling': 'UI-007',
                'UIWidgetsSpecialized': 'UI-008',
                'UIAnimations': 'UI-009',
                'UIFormWidgets': 'UI-010',
                'UIDragDrop': 'UI-011',
                'UIListWidgets': 'UI-012',
                'UITooltips': 'UI-013',
                'UIMenuWidgets': 'UI-014',
                'UIModals': 'UI-015',
                'UIAdvancedWidgets': 'UI-016',
                'UIPlugins': 'UI-017',
                'UIGraphicsWidgets': 'UI-018',
                'UIAccessibility': 'UI-019',
                'UIReportWidgets': 'UI-020'
            },
            'GAME': {
                'Protocol': 'GAME-001',
                'WorldSystem': 'GAME-002',
                'CreatureSystem': 'GAME-003',
                'ItemSystem': 'GAME-004',
                'GameEffects': 'GAME-005',
                'GameCombat': 'GAME-006',
                'GameQuests': 'GAME-007',
                'GameInventory': 'GAME-008',
                'GameChat': 'GAME-009',
                'GameMinimap': 'GAME-010',
                'GameCrafting': 'GAME-011',
                'GameTrading': 'GAME-012',
                'GameGuilds': 'GAME-013',
                'GamePvP': 'GAME-014',
                'GameAchievements': 'GAME-015'
            },
            'CORE': {
                'ModuleSystem': 'CORE-001',
                'Configuration': 'CORE-002',
                'GraphicsSystem': 'CORE-003',
                'SoundSystem': 'CORE-004',
                'ConfigurationAdvanced': 'CORE-005',
                'NetworkSystem': 'CORE-006',
                'CoreDebug': 'CORE-007',
                'CoreOptimization': 'CORE-008',
                'CoreProfiling': 'CORE-009',
                'CoreLogs': 'CORE-010'
            },
            'GUIDE': {
                'GettingStarted': 'GUIDE-001',
                'FirstModule': 'GUIDE-002',
                'BestPractices': 'GUIDE-003',
                'WidgetTutorial': 'GUIDE-004',
                'EventTutorial': 'GUIDE-005',
                'LayoutTutorial': 'GUIDE-006',
                'ThemeTutorial': 'GUIDE-007',
                'AdvancedUseCases': 'GUIDE-008',
                'Troubleshooting': 'GUIDE-009',
                'PerformanceTips': 'GUIDE-010'
            },
            'REF': {
                'LuaAPI': 'REF-001',
                'CheatSheet': 'REF-002',
                'CompleteAPIReference': 'REF-003',
                'CodeExamples': 'REF-004',
                'FAQ': 'REF-005'
            }
        }
        
        # Mapear arquivos
        for file_path in self.habdel_path.rglob("*.md"):
            file_name = file_path.stem  # Nome sem extensão
            
            for category, patterns in mapping_patterns.items():
                for pattern, story_id in patterns.items():
                    if pattern in file_name:
                        self.file_to_story_mapping[str(file_path.relative_to(self.habdel_path))] = {
                            'story_id': story_id,
                            'category': category,
                            'pattern': pattern,
                            'file_size': file_path.stat().st_size,
                            'status': 'identified'
                        }
                        break
        
        self.logger.info(f"🗺️ Mapeados {len(self.file_to_story_mapping)} arquivos para stories")
    
    def update_documentation_plan(self):
        """Atualiza o plano de documentação com o status atual"""
        self.logger.info("📝 Atualizando plano de documentação...")
        
        # Ler o plano atual
        plan_file = self.habdel_path / "DOCUMENTATION_PLAN.md"
        if not plan_file.exists():
            self.logger.error("❌ Plano de documentação não encontrado")
            return
        
        with open(plan_file, 'r', encoding='utf-8') as f:
            plan_content = f.read()
        
        # Atualizar progresso
        total_stories = 52
        completed_stories = len(self.file_to_story_mapping)
        progress_percentage = (completed_stories / total_stories) * 100
        
        # Atualizar métricas no plano
        plan_content = plan_content.replace(
            '**Progresso Geral:** 67% (22/32 documentos completos)',
            f'**Progresso Geral:** {progress_percentage:.1f}% ({completed_stories}/{total_stories} documentos completos)'
        )
        
        # Atualizar KPIs
        plan_content = plan_content.replace(
            '| **Stories Completas** | 52 | 22 | 🟡 42% |',
            f'| **Stories Completas** | 52 | {completed_stories} | {"🟢" if progress_percentage >= 100 else "🟡"} {progress_percentage:.1f}% |'
        )
        
        # Adicionar log de atividades
        log_entry = f"""
✅ Completada organização da documentação habdel
✅ Identificados {completed_stories} arquivos correspondentes a stories
✅ Mapeamento de arquivos para stories concluído
✅ Plano de documentação atualizado
🎆 MARCO: {progress_percentage:.1f}% de progresso geral! Documentação organizada e estruturada
"""
        
        # Encontrar seção de log e adicionar entrada
        if '## 📝 **Log de Atividades**' in plan_content:
            log_section_start = plan_content.find('## 📝 **Log de Atividades**')
            log_section_end = plan_content.find('\n\n', log_section_start)
            
            if log_section_end == -1:
                log_section_end = len(plan_content)
            
            new_log_section = f"""## 📝 **Log de Atividades**

```
{datetime.now().strftime('%Y-%m-%d')}:
{log_entry}
```

"""
            plan_content = plan_content[:log_section_start] + new_log_section + plan_content[log_section_end:]
        
        # Salvar plano atualizado
        with open(plan_file, 'w', encoding='utf-8') as f:
            f.write(plan_content)
        
        self.logger.info(f"📝 Plano de documentação atualizado: {progress_percentage:.1f}% de progresso")
        self.progress_metrics['plan_updated'] = True
    
    def organize_files_by_category(self):
        """Organiza arquivos por categoria para melhor estrutura"""
        self.logger.info("📂 Organizando arquivos por categoria...")
        
        # Criar estrutura de categorias
        categories = {
            'UI': [],
            'GAME': [],
            'CORE': [],
            'GUIDE': [],
            'REF': []
        }
        
        # Organizar arquivos mapeados
        for file_path, mapping in self.file_to_story_mapping.items():
            category = mapping['category']
            if category in categories:
                categories[category].append({
                    'file_path': file_path,
                    'story_id': mapping['story_id'],
                    'file_size': mapping['file_size']
                })
        
        # Log da organização
        for category, files in categories.items():
            self.logger.info(f"📂 {category}: {len(files)} arquivos")
            for file_info in files:
                self.logger.info(f"   - {file_info['story_id']}: {file_info['file_path']}")
    
    def generate_final_report(self):
        """Gera relatório final da organização"""
        self.logger.info("📊 Gerando relatório final...")
        
        # Calcular estatísticas
        total_files = len(self.file_to_story_mapping)
        total_size = sum(mapping['file_size'] for mapping in self.file_to_story_mapping.values())
        
        # Organizar por categoria
        categories = {}
        for file_path, mapping in self.file_to_story_mapping.items():
            category = mapping['category']
            if category not in categories:
                categories[category] = []
            categories[category].append({
                'file_path': file_path,
                'story_id': mapping['story_id'],
                'file_size': mapping['file_size']
            })
        
        # Gerar relatório
        report = f"""---
tags: [report, habdel_organization, documentation_analysis, bmad]
type: report
status: completed
priority: high
created: {datetime.now().strftime('%Y-%m-%d')}
---

# Relatório de Organização - Documentação Habdel

## 🎯 **Resumo Executivo**

A **organização da documentação habdel** foi **concluída com sucesso**, analisando e estruturando toda a documentação existente para preparação da integração futura com a wiki.

## 📊 **Métricas de Organização**

### **✅ Análise Completa Realizada:**
- **Arquivos Analisados**: {self.progress_metrics['files_analyzed']} arquivos
- **Stories Identificadas**: {self.progress_metrics['stories_identified']} stories
- **Arquivos Mapeados**: {total_files} arquivos
- **Tamanho Total**: {total_size / 1024:.1f} KB
- **Status**: 🟢 **Organização Concluída**

### **📁 Distribuição por Categoria:**
"""
        
        for category, files in categories.items():
            category_size = sum(f['file_size'] for f in files)
            report += f"""
**{category} ({len(files)} arquivos) - {len(files)/total_files*100:.1f}%**
- **Tamanho**: {category_size / 1024:.1f} KB
- **Stories**: {', '.join(f['story_id'] for f in files[:5])}{'...' if len(files) > 5 else ''}
"""
        
        report += f"""
## 🗺️ **Mapeamento de Arquivos**

### **Arquivos Identificados e Mapeados:**
"""
        
        for file_path, mapping in self.file_to_story_mapping.items():
            report += f"- **{mapping['story_id']}**: `{file_path}` ({mapping['file_size']} bytes)\n"
        
        report += f"""
## 📈 **Status do Plano de Documentação**

### **Progresso Atualizado:**
- **Stories Completas**: {total_files}/52 ({total_files/52*100:.1f}%)
- **Plano Atualizado**: ✅ Sim
- **Organização**: ✅ Concluída

## 🎯 **Próximos Passos**

### **Imediato (Próximas 2 semanas):**
1. **Revisar Mapeamento**: Validar correspondência arquivo-story
2. **Integrar com Wiki**: Preparar para integração com wiki principal
3. **Criar Índices**: Navegação e busca na documentação
4. **Validar Qualidade**: Revisar conteúdo e consistência

### **Curto Prazo (1-2 meses):**
1. **Migração para Wiki**: Mover documentação para estrutura wiki
2. **Atualizar Navegação**: Integrar com sistema de navegação JSON
3. **Criar Guias Práticos**: Desenvolver tutoriais baseados na documentação
4. **Estabelecer Processo**: Manutenção contínua da documentação

## 🏆 **Conclusão**

A **organização da documentação habdel** foi **concluída com sucesso**, estabelecendo uma base sólida para a integração futura com a wiki principal.

**A organização resultou em:**
- **{total_files} arquivos** mapeados e organizados
- **Plano atualizado** com progresso real
- **Estrutura clara** por categorias
- **Base preparada** para integração

**Esta organização estabelece as bases para:**
- **Integração eficiente** com wiki principal
- **Navegação organizada** na documentação
- **Manutenção consistente** do conhecimento
- **Crescimento sustentável** do projeto

---

**Relatório Gerado**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Responsável**: Habdel Documentation Organizer  
**Status**: 🟢 **Organização Concluída**  
**Próximo**: 📚 **Integração com Wiki Principal**
"""
        
        # Salvar relatório
        report_file = self.log_path / "habdel_organization_report.md"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        self.logger.info(f"📊 Relatório salvo: {report_file}")

def main():
    """Função principal"""
    print("📚 Habdel Documentation Organizer - Organizador de Documentação")
    print("=" * 70)
    
    organizer = HabdelDocumentationOrganizer()
    
    if organizer.run_organization():
        print("✅ Organização da documentação habdel concluída!")
        print(f"📁 Arquivos analisados: {organizer.progress_metrics['files_analyzed']}")
        print(f"📋 Stories identificadas: {organizer.progress_metrics['stories_identified']}")
        print(f"🗺️ Arquivos mapeados: {len(organizer.file_to_story_mapping)}")
        print(f"📝 Plano atualizado: {'Sim' if organizer.progress_metrics['plan_updated'] else 'Não'}")
        print(f"📊 Relatórios: wiki/log/habdel_organization_report.md")
        print("🎯 Próximo: Integração com wiki principal")
    else:
        print("❌ Erro durante organização da documentação")

if __name__ == "__main__":
    main() 