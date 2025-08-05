from unicode_aliases import *
# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
MAX_ITEMS = 100

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: researcher_agent.py
Módulo de Destino: agents.agent_orchestrator
Data de Migração: 2025-08-01 12:21:44

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import AgentorchestratorModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pesquisador Especializado BMAD-Habdel
=====================================

Agente especializado que integra as melhores práticas do sistema habdel
(metodologia ágil, stories, profundidade técnica) com a estrutura da wiki atual
(navegação JSON, organização modular) para estudar tanto OTClient quanto Canary.

Autor: Sistema BMAD
Versão: 1.0.0
Data: 2025-01-27
"""

import os
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import logging

class ResearcherAgent:
    """
    Agente pesquisador especializado em análise metódica e integração com wiki.
    """
    
    def __init__(self, base_path: str = None):
        """
        Inicializa o agente pesquisador.
        
        Args:
            base_path: Caminho base do projeto (padrão: diretório atual)
        """
        self.base_path = Path(base_path) if base_path else Path.cwd()
        self.habdel_path = self.base_path / "wiki" / "habdel"
        self.wiki_path = self.base_path / "wiki" / "otclient"
        self.maps_path = self.base_path / "wiki" / "maps"
        
        # Configurar logging
        log_dir = self.base_path / 'wiki' / 'log'
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / 'researcher_agent.log'
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
        # Estrutura de stories
        self.stories = {
            'otclient': [],
            'canary': [],
            'integration': [],
            'methodology': []
        }
        
        # Métricas de progresso
        self.metrics = {
            'total_stories': 0,
            'completed_stories': 0,
            'otclient_coverage': 0,
            'canary_coverage': 0,
            'integration_coverage': 0
        }
        
        self.logger.info("Pesquisador Especializado BMAD-Habdel inicializado")
    
    def create_habdel_structure(self) -> bool:
        """
        Cria a estrutura de pastas do sistema habdel expandido.
        
        Returns:
            bool: True se criado com sucesso
        """
        try:
            # Estrutura principal
            structure = {
                'otclient': ['stories', 'documentation', 'analysis'],
                'canary': ['stories', 'documentation', 'analysis'],
                'integration': ['comparative', 'migration', 'patterns'],
                'methodology': ['templates', 'workflows', 'tools']
            }
            
            for main_dir, subdirs in structure.items():
                main_path = self.habdel_path / main_dir
                main_path.mkdir(parents=True, exist_ok=True)
                
                for subdir in subdirs:
                    sub_path = main_path / subdir
                    sub_path.mkdir(parents=True, exist_ok=True)
                    
                    # Criar arquivo README.md em cada pasta
                    readme_content = f"""# {main_dir.title()} - {subdir.title()}

Esta pasta contém {subdir} relacionados ao {main_dir}.

## Conteúdo
- Documentação específica do {main_dir}
- Análises e estudos
- Templates e ferramentas

---
*Gerado automaticamente pelo Researcher Agent*
"""
                    readme_file = sub_path / "README.md"
                    if not readme_file.exists():
                        readme_file.write_text(readme_content, encoding='utf-8')
            
            self.logger.info("Estrutura habdel criada com sucesso")
            return True
            
        except Exception as e:
            self.logger.error(f"Erro ao criar estrutura habdel: {e}")
            return False
    
    def generate_story_system(self) -> Dict:
        """
        Gera o sistema de stories baseado na metodologia habdel.
        
        Returns:
            Dict: Sistema de stories organizado
        """
        story_system = {
            'otclient': {
                'title': 'Sistema OTClient',
                'stories': []
            },
            'canary': {
                'title': 'Sistema Canary', 
                'stories': []
            },
            'integration': {
                'title': 'Análises Comparativas',
                'stories': []
            },
            'methodology': {
                'title': 'Metodologia e Templates',
                'stories': []
            }
        }
        
        # Stories OTClient (OTCLIENT-001 a OTCLIENT-020)
        otclient_stories = [
            ('OTCLIENT-001', 'Core System Analysis', 'Análise profunda do sistema core'),
            ('OTCLIENT-002', 'Graphics System', 'Sistema de gráficos e renderização'),
            ('OTCLIENT-003', 'Network System', 'Sistema de rede e protocolos'),
            ('OTCLIENT-004', 'Audio System', 'Sistema de áudio e sons'),
            ('OTCLIENT-005', 'UI Framework', 'Framework de interface do usuário'),
            ('OTCLIENT-006', 'Module System', 'Sistema de módulos Lua'),
            ('OTCLIENT-007', 'Game Logic', 'Lógica do jogo e mecânicas'),
            ('OTCLIENT-008', 'Resource Management', 'Gerenciamento de recursos'),
            ('OTCLIENT-009', 'Configuration System', 'Sistema de configuração'),
            ('OTCLIENT-010', 'Event System', 'Sistema de eventos e callbacks'),
            ('OTCLIENT-011', 'Animation System', 'Sistema de animações'),
            ('OTCLIENT-012', 'Effect System', 'Sistema de efeitos visuais'),
            ('OTCLIENT-013', 'World System', 'Sistema de mundo e mapas'),
            ('OTCLIENT-014', 'Creature System', 'Sistema de criaturas'),
            ('OTCLIENT-015', 'Item System', 'Sistema de itens'),
            ('OTCLIENT-016', 'Combat System', 'Sistema de combate'),
            ('OTCLIENT-017', 'Storage System', 'Sistema de armazenamento'),
            ('OTCLIENT-018', 'Security System', 'Sistema de segurança'),
            ('OTCLIENT-019', 'Performance System', 'Sistema de performance'),
            ('OTCLIENT-020', 'Debug System', 'Sistema de debug e logging')
        ]
        
        # Stories Canary (CANARY-001 a CANARY-020)
        canary_stories = [
            ('CANARY-001', 'Core Architecture', 'Arquitetura core do Canary'),
            ('CANARY-002', 'Graphics Engine', 'Engine de gráficos'),
            ('CANARY-003', 'Network Protocol', 'Protocolo de rede'),
            ('CANARY-004', 'Audio Engine', 'Engine de áudio'),
            ('CANARY-005', 'UI System', 'Sistema de interface'),
            ('CANARY-006', 'Scripting System', 'Sistema de scripting'),
            ('CANARY-007', 'Game Mechanics', 'Mecânicas do jogo'),
            ('CANARY-008', 'Resource Engine', 'Engine de recursos'),
            ('CANARY-009', 'Config System', 'Sistema de configuração'),
            ('CANARY-010', 'Event Engine', 'Engine de eventos'),
            ('CANARY-011', 'Animation Engine', 'Engine de animações'),
            ('CANARY-012', 'Effect Engine', 'Engine de efeitos'),
            ('CANARY-013', 'World Engine', 'Engine de mundo'),
            ('CANARY-014', 'Creature Engine', 'Engine de criaturas'),
            ('CANARY-015', 'Item Engine', 'Engine de itens'),
            ('CANARY-016', 'Combat Engine', 'Engine de combate'),
            ('CANARY-017', 'Database System', 'Sistema de banco de dados'),
            ('CANARY-018', 'Security Engine', 'Engine de segurança'),
            ('CANARY-019', 'Performance Engine', 'Engine de performance'),
            ('CANARY-020', 'Debug Engine', 'Engine de debug')
        ]
        
        # Stories Integration (INTEGRATION-001 a INTEGRATION-010)
        integration_stories = [
            ('INTEGRATION-001', 'Architecture Comparison', 'Comparação de arquiteturas'),
            ('INTEGRATION-002', 'Protocol Analysis', 'Análise de protocolos'),
            ('INTEGRATION-003', 'UI Framework Comparison', 'Comparação de frameworks UI'),
            ('INTEGRATION-004', 'Scripting Comparison', 'Comparação de sistemas de scripting'),
            ('INTEGRATION-005', 'Performance Analysis', 'Análise de performance'),
            ('INTEGRATION-006', 'Migration Guide', 'Guia de migração'),
            ('INTEGRATION-007', 'Integration Patterns', 'Padrões de integração'),
            ('INTEGRATION-008', 'Best Practices', 'Melhores práticas'),
            ('INTEGRATION-009', 'Tooling Comparison', 'Comparação de ferramentas'),
            ('INTEGRATION-010', 'Future Roadmap', 'Roadmap futuro')
        ]
        
        # Stories Methodology (METHODOLOGY-001 a METHODOLOGY-005)
        methodology_stories = [
            ('METHODOLOGY-001', 'Research Templates', 'Templates de pesquisa'),
            ('METHODOLOGY-002', 'Analysis Workflows', 'Workflows de análise'),
            ('METHODOLOGY-003', 'Documentation Standards', 'Padrões de documentação'),
            ('METHODOLOGY-004', 'Quality Assurance', 'Garantia de qualidade'),
            ('METHODOLOGY-005', 'Integration Tools', 'Ferramentas de integração')
        ]
        
        # Adicionar stories às categorias
        for story_id, title, description in otclient_stories:
            story_system['otclient']['stories'].append({
                'id': story_id,
                'title': title,
                'description': description,
                'status': 'not_started',
                'priority': 'high' if int(story_id.split('-')[1]) <= 10 else 'medium',
                'estimated_hours': 8,
                'created': datetime.now().isoformat()
            })
        
        for story_id, title, description in canary_stories:
            story_system['canary']['stories'].append({
                'id': story_id,
                'title': title,
                'description': description,
                'status': 'not_started',
                'priority': 'high' if int(story_id.split('-')[1]) <= 10 else 'medium',
                'estimated_hours': 8,
                'created': datetime.now().isoformat()
            })
        
        for story_id, title, description in integration_stories:
            story_system['integration']['stories'].append({
                'id': story_id,
                'title': title,
                'description': description,
                'status': 'not_started',
                'priority': 'high' if int(story_id.split('-')[1]) <= 5 else 'medium',
                'estimated_hours': 12,
                'created': datetime.now().isoformat()
            })
        
        for story_id, title, description in methodology_stories:
            story_system['methodology']['stories'].append({
                'id': story_id,
                'title': title,
                'description': description,
                'status': 'not_started',
                'priority': 'high',
                'estimated_hours': 6,
                'created': datetime.now().isoformat()
            })
        
        return story_system
    
    def save_story_system(self, story_system: Dict) -> bool:
        """
        Salva o sistema de stories em arquivos JSON.
        
        Args:
            story_system: Sistema de stories a ser salvo
            
        Returns:
            bool: True se salvo com sucesso
        """
        try:
            # Salvar sistema completo
            system_file = self.habdel_path / "story_system.json"
            with open(system_file, 'w', encoding='utf-8') as f:
                json.dump(story_system, f, indent=2, ensure_ascii=False)
            
            # Salvar por categoria
            for category, data in story_system.items():
                category_file = self.habdel_path / category / "stories" / f"{category}_stories.json"
                category_file.parent.mkdir(parents=True, exist_ok=True)
                
                with open(category_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
            
            self.logger.info("Sistema de stories salvo com sucesso")
            return True
            
        except Exception as e:
            self.logger.error(f"Erro ao salvar sistema de stories: {e}")
            return False
    
    def create_research_template(self) -> str:
        """
        Cria template para documentação de pesquisa baseado no habdel.
        
        Returns:
            str: Template em markdown
        """
        template = """---
tags: [research, {category}, {story_id}, {project}]
type: research
status: {status}
priority: {priority}
created: {created}
story_id: {story_id}
project: {project}
---

# {title}

{description}

## 📋 Índice
1. [Visão Geral](#visão-geral)
2. [Análise Técnica](#análise-técnica)
3. [API e Interfaces](#api-e-interfaces)
4. [Exemplos Práticos](#exemplos-práticos)
5. [Comparação com Outros Sistemas](#comparação-com-outros-sistemas)
6. [Melhores Práticas](#melhores-práticas)
7. [Integração com Wiki](#integração-com-wiki)

## 🎯 Visão Geral

[Descrição detalhada do sistema/componente]

### 🏗️ Arquitetura
```
[Diagrama ou descrição da arquitetura]
```

### 🔧 Componentes Principais
- **Componente 1**: Descrição
- **Componente 2**: Descrição
- **Componente 3**: Descrição

## 🔍 Análise Técnica

### 📊 Métricas de Performance
- **Tempo de resposta**: X ms
- **Uso de memória**: X MB
- **Throughput**: X ops/sec

### 🐛 Pontos de Atenção
- [ ] Item 1
- [ ] Item 2
- [ ] Item 3

## 🔌 API e Interfaces

### C++ API
```cpp
// Exemplos de código C++
```

### Lua API
```lua
-- Exemplos de código Lua
```

## 💡 Exemplos Práticos

### Exemplo 1: Uso Básico
```lua
-- Código de exemplo
```

### Exemplo 2: Uso Avançado
```lua
-- Código de exemplo avançado
```

## 🔄 Comparação com Outros Sistemas

| Aspecto | {project} | Outro Sistema |
|---------|-----------|---------------|
| Performance | X | Y |
| Flexibilidade | X | Y |
| Facilidade | X | Y |

## ✅ Melhores Práticas

1. **Prática 1**: Descrição
2. **Prática 2**: Descrição
3. **Prática 3**: Descrição

## 🔗 Integração com Wiki

### Links Relacionados
- [[{related_doc_1}]]
- [[{related_doc_2}]]
- [[{related_doc_3}]]

### Tags e Metadados
- **Categoria**: {category}
- **Sistema**: {system}
- **Prioridade**: {priority}

---

**Status**: {status}  
**Última Atualização**: {updated}  
**Responsável**: Researcher Agent
"""
        return template
    
    def analyze_otclient_source(self) -> Dict:
        """
        Analisa o código-fonte do OTClient para identificar sistemas.
        
        Returns:
            Dict: Análise estruturada
        """
        analysis = {
            'systems': [],
            'files_analyzed': 0,
            'total_lines': 0,
            'complexity_score': 0
        }
        
        try:
            src_path = self.base_path / "src"
            if not src_path.exists():
                self.logger.warning("Pasta src não encontrada")
                return analysis
            
            # Análise básica da estrutura
            for item in src_path.rglob("*.cpp"):
                analysis['files_analyzed'] += 1
                
                try:
                    with open(item, 'r', encoding='utf-8') as f:
                        content = f.read()
                        analysis['total_lines'] += len(content.split('\n'))
                        
                        # Análise simples de complexidade
                        analysis['complexity_score'] += content.count('class') * 2
                        analysis['complexity_score'] += content.count('function') * 1
                        
                except Exception as e:
                    self.logger.warning(f"Erro ao ler {item}: {e}")
            
            self.logger.info(f"Análise OTClient: {analysis['files_analyzed']} arquivos,
    {analysis['total_lines']} linhas")
            return analysis
            
        except Exception as e:
            self.logger.error(f"Erro na análise OTClient: {e}")
            return analysis
    
    def generate_research_plan(self) -> Dict:
        """
        Gera plano de pesquisa baseado na análise do código.
        
        Returns:
            Dict: Plano de pesquisa estruturado
        """
        plan = {
            'phases': [],
            'timeline': {},
            'resources': [],
            'deliverables': []
        }
        
        # Fase 1: Estrutura e Metodologia
        plan['phases'].append({
            'id': 'phase_1',
            'name': 'Estrutura e Metodologia',
            'duration': '2 semanas',
            'stories': ['METHODOLOGY-001', 'METHODOLOGY-002', 'METHODOLOGY-003'],
            'deliverables': [
                'Estrutura de pastas habdel',
                'Sistema de stories',
                'Templates de pesquisa'
            ]
        })
        
        # Fase 2: Análise OTClient
        plan['phases'].append({
            'id': 'phase_2',
            'name': 'Análise OTClient',
            'duration': '4 semanas',
            'stories': [f'OTCLIENT-{i:03d}' for i in range(1, 21)],
            'deliverables': [
                'Documentação completa OTClient',
                'Análises técnicas detalhadas',
                'Exemplos práticos'
            ]
        })
        
        # Fase 3: Análise Canary
        plan['phases'].append({
            'id': 'phase_3',
            'name': 'Análise Canary',
            'duration': '4 semanas',
            'stories': [f'CANARY-{i:03d}' for i in range(1, 21)],
            'deliverables': [
                'Documentação completa Canary',
                'Análises técnicas detalhadas',
                'Exemplos práticos'
            ]
        })
        
        # Fase 4: Integração e Comparação
        plan['phases'].append({
            'id': 'phase_4',
            'name': 'Integração e Comparação',
            'duration': '2 semanas',
            'stories': [f'INTEGRATION-{i:03d}' for i in range(1, 11)],
            'deliverables': [
                'Análises comparativas',
                'Guias de migração',
                'Sistema integrado'
            ]
        })
        
        return plan
    
    def run_initial_setup(self) -> bool:
        """
        Executa configuração inicial do pesquisador.
        
        Returns:
            bool: True se configurado com sucesso
        """
        try:
            self.logger.info("Iniciando configuração do pesquisador...")
            
            # 1. Criar estrutura de pastas
            if not self.create_habdel_structure():
                return False
            
            # 2. Gerar sistema de stories
            story_system = self.generate_story_system()
            
            # 3. Salvar sistema de stories
            if not self.save_story_system(story_system):
                return False
            
            # 4. Criar template de pesquisa
            template = self.create_research_template()
            template_file = self.habdel_path / "methodology" / "templates" / "research_template.md"
            template_file.parent.mkdir(parents=True, exist_ok=True)
            template_file.write_text(template, encoding='utf-8')
            
            # 5. Gerar plano de pesquisa
            plan = self.generate_research_plan()
            plan_file = self.habdel_path / "research_plan.json"
            with open(plan_file, 'w', encoding='utf-8') as f:
                json.dump(plan, f, indent=2, ensure_ascii=False)
            
            # 6. Analisar código-fonte OTClient
            analysis = self.analyze_otclient_source()
            analysis_file = self.habdel_path / "otclient" / "analysis" / "source_analysis.json"
            analysis_file.parent.mkdir(parents=True, exist_ok=True)
            with open(analysis_file, 'w', encoding='utf-8') as f:
                json.dump(analysis, f, indent=2, ensure_ascii=False)
            
            self.logger.info("Configuração inicial concluída com sucesso!")
            return True
            
        except Exception as e:
            self.logger.error(f"Erro na configuração inicial: {e}")
            return False
    
    def generate_status_report(self) -> str:
        """
        Gera relatório de status do pesquisador.
        
        Returns:
            str: Relatório em markdown
        """
        try:
            # Carregar sistema de stories
            system_file = self.habdel_path / "story_system.json"
            if system_file.exists():
                with open(system_file, 'r', encoding='utf-8') as f:
                    story_system = json.load(f)
            else:
                story_system = {}
            
            # Calcular métricas
            total_stories = 0
            completed_stories = 0
            
            for category, data in story_system.items():
                if 'stories' in data:
                    total_stories += len(data['stories'])
                    completed_stories += len([s for s in data['stories'] if s.get('status') == 'completed'])
            
            progress = (completed_stories / total_stories * 100) if total_stories > 0 else 0
            
            report = f"""# Relatório de Status - Pesquisador Especializado

## 📊 Métricas Gerais

- **Total de Stories**: {total_stories}
- **Stories Completas**: {completed_stories}
- **Progresso Geral**: {progress:.1f}%

## 🎯 Status por Categoria

"""
            
            for category, data in story_system.items():
                if 'stories' in data:
                    cat_total = len(data['stories'])
                    cat_completed = len([s for s in data['stories'] if s.get('status') == 'completed'])
                    cat_progress = (cat_completed / cat_total * 100) if cat_total > 0 else 0
                    
                    report += f"### {data.get('title', category.title())}\n"
                    report += f"- **Progresso**: {cat_progress:.1f}% ({cat_completed}/{cat_total})\n"
report += f"- **Status**: {'🟢 Completo' if cat_progress == 100 else '🟡 Em Progresso' if cat_progress > 0 else '🔴 Não
    Iniciado'}\n\n"
            
            report += """## 🚀 Próximos Passos

1. **Completar análise OTClient** (Fase 2)
2. **Iniciar análise Canary** (Fase 3)
3. **Desenvolver integrações** (Fase 4)
4. **Validar qualidade** e integração com wiki

## 📁 Estrutura Criada

```
wiki/habdel/
├── otclient/          # Análises OTClient
├── canary/            # Análises Canary  
├── integration/       # Comparações
└── methodology/       # Templates e workflows
```

---
*Relatório gerado automaticamente pelo Researcher Agent*
"""
            
            return report
            
        except Exception as e:
            self.logger.error(f"Erro ao gerar relatório: {e}")
            return f"Erro ao gerar relatório: {e}"

def main():
    """
    Função principal para execução do agente pesquisador.
    """
    print("🔬 Pesquisador Especializado BMAD-Habdel")
    print("=" * 50)
    
    # Inicializar agente
    agent = ResearcherAgent()
    
    # Executar configuração inicial
    if agent.run_initial_setup():
        print("✅ Configuração inicial concluída!")
        
        # Gerar relatório de status
        report = agent.generate_status_report()
        
        # Salvar relatório
        report_file = agent.habdel_path / "status_report.md"
        report_file.write_text(report, encoding='utf-8')
        
        print("\n📊 Relatório de Status:")
        print(report)
        
        print(f"\n📁 Arquivos criados em: {agent.habdel_path}")
        print("🎯 Próximo passo: Iniciar análise OTClient (Fase 2)")
        
    else:
        print("❌ Erro na configuração inicial")
        sys.exit(1)

if __name__ == "__main__":
    main() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = AgentorchestratorModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script researcher_agent.py executado com sucesso via módulo agents.agent_orchestrator")
    else:
        print(f"❌ Erro na execução do script researcher_agent.py via módulo agents.agent_orchestrator")

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
- **Nome**: migrated_researcher_agent
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

