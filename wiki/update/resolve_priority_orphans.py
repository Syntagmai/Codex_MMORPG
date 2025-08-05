#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para resolver arquivos órfãos prioritários
Task 20.3 - Resolver Arquivos Órfãos Prioritários
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

class PriorityOrphanResolver:
    def __init__(self):
        self.wiki_root = Path("wiki")
        self.priority_files = [
            "GLOSSARIO_TERMINOLOGIA_TECNICA.md",
            "Sistema_Orquestracao_Inteligente_Guia.md",
            "Sistema_OTClient_BMAD_Relatorio_Geral.md"
        ]
        
    def read_file_content(self, file_path):
        """Lê conteúdo do arquivo com tratamento de erro"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Erro ao ler {file_path}: {e}")
            return ""
    
    def write_file_content(self, file_path, content):
        """Escreve conteúdo no arquivo"""
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Arquivo atualizado: {file_path}")
        except Exception as e:
            print(f"❌ Erro ao escrever {file_path}: {e}")
    
    def add_navigation_section(self, content, file_name):
        """Adiciona seção de navegação ao arquivo"""
        navigation_template = f"""
---

## 🔗 **Navegação da Wiki**

> [!tip] **Links Relacionados**
> - [[README|Hub Central da Wiki]]
> - [[Indice_Principal_Categorias|Índice de Categorias]]
> - [[Guia_Navegacao_Categoria|Guia de Navegação]]

> [!info] **Sistemas Principais**
> - [[dashboard/task_master|Sistema de Tarefas]]
> - [[bmad/README|Sistema BMAD]]
> - [[habdel/README|Sistema Habdel]]

> [!note] **Relatórios e Métricas**
> - [[Relatorio_Qualidade_Linkagem|Relatório de Qualidade]]
> - [[Arquivos_Orfaos|Arquivos Órfãos]]
> - [[Arquivos_Linkados|Arquivos Linkados]]

---
"""
        return content + navigation_template
    
    def link_glossario_terminologia(self):
        """Linka o glossário de terminologia técnica"""
        file_path = self.wiki_root / "GLOSSARIO_TERMINOLOGIA_TECNICA.md"
        content = self.read_file_content(file_path)
        
        if "Navegação da Wiki" not in content:
            content = self.add_navigation_section(content, "GLOSSARIO_TERMINOLOGIA_TECNICA.md")
            
            # Adicionar links específicos para glossário
            glossario_links = """
> [!important] **Glossários Relacionados**
> - [[Glossario_Tecnico|Glossário Técnico Geral]]
> - [[Conceitos_Basicos|Conceitos Básicos]]
> - [[Troubleshooting_Comum|Solução de Problemas]]

> [!example] **Documentação de Referência**
> - [[Exemplos_Progressivos_OTClient|Exemplos Progressivos]]
> - [[Guia_Inicio_Rapido|Guia de Início Rápido]]

---
"""
            content = content.replace("---\n", "---\n" + glossario_links, 1)
            
            self.write_file_content(file_path, content)
            return True
        return False
    
    def link_sistema_orquestracao(self):
        """Linka o guia de orquestração inteligente"""
        file_path = self.wiki_root / "Sistema_Orquestracao_Inteligente_Guia.md"
        content = self.read_file_content(file_path)
        
        if "Navegação da Wiki" not in content:
            content = self.add_navigation_section(content, "Sistema_Orquestracao_Inteligente_Guia.md")
            
            # Adicionar links específicos para sistema de orquestração
            orquestracao_links = """
> [!important] **Sistemas de Automação**
> - [[bmad/README|Sistema BMAD]]
> - [[bmad/automacao_git|Automação Git]]
> - [[bmad/sistema_autonomo|Sistema Autônomo]]

> [!example] **Guias e Templates**
> - [[bmad/guides/Auto_Learning_Guide|Guia de Auto-Aprendizado]]
> - [[bmad/guides/git_automation_guide|Guia de Automação Git]]
> - [[bmad/templates/agent_template|Template de Agente]]

> [!info] **Relatórios de Sistema**
> - [[Sistema_OTClient_BMAD_Relatorio_Geral|Relatório Geral OTClient-BMAD]]
> - [[bmad/RELATORIO_CRIACAO_MODULO_ZERO|Relatório Criação Módulo Zero]]

---
"""
            content = content.replace("---\n", "---\n" + orquestracao_links, 1)
            
            self.write_file_content(file_path, content)
            return True
        return False
    
    def link_relatorio_geral(self):
        """Linka o relatório geral OTClient-BMAD"""
        file_path = self.wiki_root / "Sistema_OTClient_BMAD_Relatorio_Geral.md"
        content = self.read_file_content(file_path)
        
        if "Navegação da Wiki" not in content:
            content = self.add_navigation_section(content, "Sistema_OTClient_BMAD_Relatorio_Geral.md")
            
            # Adicionar links específicos para relatório geral
            relatorio_links = """
> [!important] **Sistemas Integrados**
> - [[bmad/README|Sistema BMAD]]
> - [[habdel/README|Sistema Habdel]]
> - [[dashboard/task_master|Sistema de Tarefas]]

> [!example] **Documentação de Integração**
> - [[integration/README|Documentação de Integração]]
> - [[integration/comparisons/INTEGRATION-001_architecture_comparison|Comparação de Arquitetura]]

> [!info] **Relatórios Relacionados**
> - [[RELATORIO_MELHORIAS_WIKI|Relatório de Melhorias]]
> - [[bmad/RELATORIO_WORKFLOW_MODULOS|Relatório de Workflow]]

---
"""
            content = content.replace("---\n", "---\n" + relatorio_links, 1)
            
            self.write_file_content(file_path, content)
            return True
        return False
    
    def integrate_bmad_system(self):
        """Integra sistema BMAD com documentação principal"""
        bmad_readme = self.wiki_root / "bmad" / "README.md"
        
        if bmad_readme.exists():
            content = self.read_file_content(bmad_readme)
            
            if "Navegação da Wiki" not in content:
                bmad_navigation = """
---

## 🔗 **Integração com Wiki Principal**

> [!tip] **Hub Central**
> - [[../README|Hub Central da Wiki]]

> [!important] **Sistemas Relacionados**
> - [[../dashboard/task_master|Sistema de Tarefas]]
> - [[../habdel/README|Sistema Habdel]]
> - [[../integration/README|Sistema de Integração]]

> [!example] **Guias e Documentação**
> - [[../Sistema_Orquestracao_Inteligente_Guia|Guia de Orquestração]]
> - [[../GLOSSARIO_TERMINOLOGIA_TECNICA|Glossário Técnico]]
> - [[../Guia_Inicio_Rapido|Guia de Início Rápido]]

> [!info] **Relatórios e Métricas**
> - [[../Sistema_OTClient_BMAD_Relatorio_Geral|Relatório Geral]]
> - [[../Relatorio_Qualidade_Linkagem|Relatório de Qualidade]]

---
"""
                content = content + bmad_navigation
                self.write_file_content(bmad_readme, content)
                return True
        return False
    
    def integrate_dashboard_system(self):
        """Integra dashboard com sistema de tarefas"""
        dashboard_files = [
            "dashboard/task_master.md",
            "dashboard/cursor.md"
        ]
        
        for file_name in dashboard_files:
            file_path = self.wiki_root / file_name
            if file_path.exists():
                content = self.read_file_content(file_path)
                
                if "Navegação da Wiki" not in content:
                    dashboard_navigation = """
---

## 🔗 **Integração com Sistemas**

> [!tip] **Hub Central**
> - [[../README|Hub Central da Wiki]]

> [!important] **Sistemas de Automação**
> - [[../bmad/README|Sistema BMAD]]
> - [[../habdel/README|Sistema Habdel]]

> [!example] **Guias e Documentação**
> - [[../Sistema_Orquestracao_Inteligente_Guia|Guia de Orquestração]]
> - [[../GLOSSARIO_TERMINOLOGIA_TECNICA|Glossário Técnico]]

> [!info] **Relatórios**
> - [[../Sistema_OTClient_BMAD_Relatorio_Geral|Relatório Geral]]
> - [[../Relatorio_Qualidade_Linkagem|Relatório de Qualidade]]

---
"""
                    content = content + dashboard_navigation
                    self.write_file_content(file_path, content)
    
    def integrate_habdel_system(self):
        """Integra sistema Habdel com OTClient"""
        habdel_readme = self.wiki_root / "habdel" / "README.md"
        
        if habdel_readme.exists():
            content = self.read_file_content(habdel_readme)
            
            if "Navegação da Wiki" not in content:
                habdel_navigation = """
---

## 🔗 **Integração com OTClient**

> [!tip] **Hub Central**
> - [[../README|Hub Central da Wiki]]

> [!important] **Sistemas Relacionados**
> - [[../bmad/README|Sistema BMAD]]
> - [[../dashboard/task_master|Sistema de Tarefas]]

> [!example] **Documentação OTClient**
> - [[../docs/README|Documentação OTClient]]
> - [[../Exemplos_Progressivos_OTClient|Exemplos Progressivos]]
> - [[../Guia_Inicio_Rapido|Guia de Início Rápido]]

> [!info] **Relatórios**
> - [[../Sistema_OTClient_BMAD_Relatorio_Geral|Relatório Geral]]
> - [[../Relatorio_Qualidade_Linkagem|Relatório de Qualidade]]

---
"""
                content = content + habdel_navigation
                self.write_file_content(habdel_readme, content)
                return True
        return False
    
    def link_integration_files(self):
        """Linka arquivos de integração"""
        integration_readme = self.wiki_root / "integration" / "README.md"
        
        if integration_readme.exists():
            content = self.read_file_content(integration_readme)
            
            if "Navegação da Wiki" not in content:
                integration_navigation = """
---

## 🔗 **Integração com Sistemas**

> [!tip] **Hub Central**
> - [[../README|Hub Central da Wiki]]

> [!important] **Sistemas Integrados**
> - [[../bmad/README|Sistema BMAD]]
> - [[../habdel/README|Sistema Habdel]]
> - [[../dashboard/task_master|Sistema de Tarefas]]

> [!example] **Comparações e Análises**
> - [[comparisons/INTEGRATION-001_architecture_comparison|Comparação de Arquitetura]]
> - [[comparisons/INTEGRATION-002_protocol_analysis|Análise de Protocolo]]
> - [[comparisons/INTEGRATION-003_ui_framework_comparison|Comparação de UI]]

> [!info] **Relatórios**
> - [[../Sistema_OTClient_BMAD_Relatorio_Geral|Relatório Geral]]
> - [[../Relatorio_Qualidade_Linkagem|Relatório de Qualidade]]

---
"""
                content = content + integration_navigation
                self.write_file_content(integration_readme, content)
                return True
        return False
    
    def update_readme_links(self):
        """Atualiza README.md com links para arquivos prioritários"""
        readme_path = self.wiki_root / "README.md"
        content = self.read_file_content(readme_path)
        
        # Verificar se já tem seção de arquivos prioritários
        if "## 📚 **Documentação Prioritária**" not in content:
            priority_section = """
## 📚 **Documentação Prioritária**

### **🔧 Referência Técnica**
- [[GLOSSARIO_TERMINOLOGIA_TECNICA|Glossário de Terminologia Técnica]] - Padronização de termos
- [[Sistema_Orquestracao_Inteligente_Guia|Sistema de Orquestração Inteligente]] - Guia completo
- [[Sistema_OTClient_BMAD_Relatorio_Geral|Relatório Geral OTClient-BMAD]] - Integração de sistemas

### **🎯 Sistemas Principais**
- [[bmad/README|Sistema BMAD]] - Automação e agentes inteligentes
- [[habdel/README|Sistema Habdel]] - Integração com OTClient
- [[dashboard/task_master|Sistema de Tarefas]] - Gerenciamento de projetos
- [[integration/README|Sistema de Integração]] - Comparações e análises

"""
            # Inserir após a primeira seção principal
            content = content.replace("## 🎯 **Navegação Rápida por Perfil**", 
                                    priority_section + "\n## 🎯 **Navegação Rápida por Perfil**")
            
            self.write_file_content(readme_path, content)
            return True
        return False
    
    def run(self):
        """Executa a resolução de arquivos órfãos prioritários"""
        print("🚀 Iniciando Task 20.3 - Resolver Arquivos Órfãos Prioritários")
        print("=" * 60)
        
        results = {
            "files_updated": [],
            "systems_integrated": [],
            "errors": []
        }
        
        # 1. Linkar arquivos da raiz órfãos
        print("\n📋 1. Linkando arquivos prioritários da raiz...")
        
        if self.link_glossario_terminologia():
            results["files_updated"].append("GLOSSARIO_TERMINOLOGIA_TECNICA.md")
        
        if self.link_sistema_orquestracao():
            results["files_updated"].append("Sistema_Orquestracao_Inteligente_Guia.md")
        
        if self.link_relatorio_geral():
            results["files_updated"].append("Sistema_OTClient_BMAD_Relatorio_Geral.md")
        
        # 2. Integrar sistema BMAD
        print("\n📋 2. Integrando sistema BMAD...")
        if self.integrate_bmad_system():
            results["systems_integrated"].append("BMAD System")
        
        # 3. Conectar Dashboard
        print("\n📋 3. Conectando Dashboard...")
        self.integrate_dashboard_system()
        results["systems_integrated"].append("Dashboard System")
        
        # 4. Linkar sistema Habdel
        print("\n📋 4. Linkando sistema Habdel...")
        if self.integrate_habdel_system():
            results["systems_integrated"].append("Habdel System")
        
        # 5. Linkar arquivos de Integração
        print("\n📋 5. Linkando arquivos de Integração...")
        if self.link_integration_files():
            results["systems_integrated"].append("Integration System")
        
        # 6. Atualizar README.md
        print("\n📋 6. Atualizando README.md...")
        if self.update_readme_links():
            results["files_updated"].append("README.md")
        
        # Salvar relatório
        report = {
            "timestamp": datetime.now().isoformat(),
            "task": "20.3 - Resolver Arquivos Órfãos Prioritários",
            "results": results,
            "summary": {
                "files_updated": len(results["files_updated"]),
                "systems_integrated": len(results["systems_integrated"]),
                "errors": len(results["errors"])
            }
        }
        
        report_path = self.wiki_root / "log" / "priority_orphans_resolution.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        # Resumo final
        print("\n" + "=" * 60)
        print("✅ Task 20.3 Concluída!")
        print(f"📁 Arquivos atualizados: {len(results['files_updated'])}")
        print(f"🔗 Sistemas integrados: {len(results['systems_integrated'])}")
        print(f"❌ Erros: {len(results['errors'])}")
        
        if results["files_updated"]:
            print(f"\n📋 Arquivos atualizados:")
            for file in results["files_updated"]:
                print(f"   ✅ {file}")
        
        if results["systems_integrated"]:
            print(f"\n🔗 Sistemas integrados:")
            for system in results["systems_integrated"]:
                print(f"   ✅ {system}")
        
        print(f"\n📊 Relatório salvo: {report_path}")
        return report

if __name__ == "__main__":
    resolver = PriorityOrphanResolver()
    resolver.run() 
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
- **Nome**: resolve_priority_orphans
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

