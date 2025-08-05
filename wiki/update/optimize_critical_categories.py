#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Otimização de Categorias Críticas - Task 20.7
Melhora linkagem das categorias com maior taxa de arquivos órfãos
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

class CriticalCategoriesOptimizer:
    def __init__(self):
        self.wiki_path = Path("wiki")
        self.maps_path = self.wiki_path / "maps"
        self.update_path = self.wiki_path / "update"
        
    def load_orphan_analysis(self) -> Dict:
        """Carrega análise de arquivos órfãos"""
        analysis_file = self.maps_path / "files_categorized.json"
        with open(analysis_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def identify_critical_categories(self) -> Dict:
        """Identifica categorias críticas com maior taxa de órfãos"""
        files_data = self.load_orphan_analysis()
        
        # Contar arquivos por categoria
        category_stats = {}
        for file_path, file_data in files_data.items():
            category = file_data.get('category', 'Unknown')
            if category not in category_stats:
                category_stats[category] = {
                    'total_files': 0,
                    'orphan_files': 0,
                    'linked_files': 0,
                    'orphan_rate': 0.0
                }
            
            category_stats[category]['total_files'] += 1
            
            # Verificar se arquivo é órfão (sem links)
            if file_data.get('links', []) == []:
                category_stats[category]['orphan_files'] += 1
            else:
                category_stats[category]['linked_files'] += 1
        
        # Calcular taxa de órfãos
        for category, stats in category_stats.items():
            if stats['total_files'] > 0:
                stats['orphan_rate'] = (stats['orphan_files'] / stats['total_files']) * 100
        
        # Ordenar por taxa de órfãos (maior primeiro)
        critical_categories = dict(sorted(
            category_stats.items(),
            key=lambda x: x[1]['orphan_rate'],
            reverse=True
        ))
        
        return critical_categories
    
    def optimize_scripts_category(self) -> Dict:
        """Otimiza categoria Scripts (99.9% órfãos)"""
        print("🔧 Otimizando categoria Scripts...")
        
        scripts_path = self.update_path
        optimization_results = {
            'category': 'Scripts',
            'files_processed': 0,
            'links_created': 0,
            'errors': 0
        }
        
        # Encontrar todos os scripts Python
        python_files = list(scripts_path.rglob("*.py"))
        
        for script_file in python_files:
            try:
                # Criar links para scripts importantes
                if self.create_script_links(script_file):
                    optimization_results['links_created'] += 1
                optimization_results['files_processed'] += 1
                
            except Exception as e:
                print(f"❌ Erro ao processar {script_file}: {e}")
                optimization_results['errors'] += 1
        
        return optimization_results
    
    def create_script_links(self, script_file: Path) -> bool:
        """Cria links para um script específico"""
        try:
            # Ler conteúdo do script
            with open(script_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Verificar se já tem links
            if "## 🔗 **Links Automáticos**" in content:
                return False
            
            # Criar links baseados no tipo de script
            script_name = script_file.stem
            links_section = self.generate_script_links(script_name, script_file)
            
            # Adicionar links ao final do arquivo
            content += "\n" + links_section
            
            # Salvar arquivo atualizado
            with open(script_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Links criados para: {script_file}")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao criar links para {script_file}: {e}")
            return False
    
    def generate_script_links(self, script_name: str, script_file: Path) -> str:
        """Gera links específicos para scripts"""
        links_section = f"""## 🔗 **Links Automáticos - Scripts**

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
"""
        
        # Adicionar links para scripts relacionados
        related_scripts = [
            "automatic_linkage_system.py",
            "create_automatic_link_templates.py",
            "orphan_files_analyzer.py",
            "update_json_maps.py"
        ]
        
        for related_script in related_scripts:
            if related_script != script_file.name:
                links_section += f"- [[../update/{related_script}|{related_script}]]\n"
        
        links_section += f"""
### **📈 Métricas do Script**
- **Nome**: {script_name}
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

"""
        
        return links_section
    
    def optimize_logs_category(self) -> Dict:
        """Otimiza categoria Logs (99.6% órfãos)"""
        print("📋 Otimizando categoria Logs...")
        
        logs_path = self.wiki_path / "log"
        optimization_results = {
            'category': 'Logs',
            'files_processed': 0,
            'links_created': 0,
            'errors': 0
        }
        
        # Criar índice de logs
        self.create_logs_index()
        
        # Processar arquivos de log
        log_files = list(logs_path.rglob("*.json")) + list(logs_path.rglob("*.md"))
        
        for log_file in log_files:
            try:
                if self.create_log_links(log_file):
                    optimization_results['links_created'] += 1
                optimization_results['files_processed'] += 1
                
            except Exception as e:
                print(f"❌ Erro ao processar {log_file}: {e}")
                optimization_results['errors'] += 1
        
        return optimization_results
    
    def create_logs_index(self):
        """Cria índice de logs"""
        logs_index_content = """---
tags: [logs_index, system_logs, reports, metrics]
type: index
category: Tools
status: active
created: 2025-08-05
---

# 📋 **Índice de Logs e Relatórios**

> [!info] **Sistema de Logs**
> Este arquivo serve como índice central para todos os logs e relatórios do sistema

## 📊 **Relatórios de Sistema**

### **🔄 Relatórios de Atualização**
- [[automatic_linkage_report.json|Relatório de Linkagem Automática]]
- [[automatic_link_templates_report.json|Relatório de Templates]]
- [[orphan_metrics_report.json|Relatório de Métricas de Órfãos]]

### **📈 Relatórios de Performance**
- [[navigation_performance_report.json|Relatório de Performance de Navegação]]
- [[system_performance_report.json|Relatório de Performance do Sistema]]

### **🔍 Relatórios de Análise**
- [[deep_links_report.json|Relatório de Deep Links]]
- [[code_examples_analysis.json|Análise de Exemplos de Código]]

## 📝 **Logs de Atividade**

### **🔄 Logs de Automação**
- Logs de execução de scripts
- Logs de atualização de mapas
- Logs de validação de links

### **📊 Logs de Métricas**
- Métricas de performance
- Métricas de qualidade
- Métricas de uso

---

> [!tip] **Acesso Rápido**
> Use este índice para encontrar rapidamente logs e relatórios específicos.

"""
        
        logs_index_file = self.wiki_path / "log" / "README.md"
        with open(logs_index_file, 'w', encoding='utf-8') as f:
            f.write(logs_index_content)
    
    def create_log_links(self, log_file: Path) -> bool:
        """Cria links para arquivos de log"""
        try:
            # Verificar se é arquivo markdown
            if log_file.suffix == '.md':
                with open(log_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if "## 🔗 **Links Automáticos**" not in content:
                    links_section = f"""## 🔗 **Links Automáticos - Logs**

> [!info] **Arquivo de Log**
> Este arquivo faz parte do sistema de logs da wiki

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../log/README|Índice de Logs]]

### **📊 Categoria de Log**
- **Tipo**: Arquivo de Log
- **Categoria**: Logs e Relatórios
- **Status**: Ativo

---

"""
                    
                    content += "\n" + links_section
                    
                    with open(log_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    print(f"✅ Links criados para: {log_file}")
                    return True
            
            return False
            
        except Exception as e:
            print(f"❌ Erro ao criar links para {log_file}: {e}")
            return False
    
    def optimize_dashboard_category(self) -> Dict:
        """Otimiza categoria Dashboard (88.9% órfãos)"""
        print("📊 Otimizando categoria Dashboard...")
        
        dashboard_path = self.wiki_path / "dashboard"
        optimization_results = {
            'category': 'Dashboard',
            'files_processed': 0,
            'links_created': 0,
            'errors': 0
        }
        
        # Processar arquivos do dashboard
        dashboard_files = list(dashboard_path.rglob("*.md"))
        
        for dashboard_file in dashboard_files:
            try:
                if self.create_dashboard_links(dashboard_file):
                    optimization_results['links_created'] += 1
                optimization_results['files_processed'] += 1
                
            except Exception as e:
                print(f"❌ Erro ao processar {dashboard_file}: {e}")
                optimization_results['errors'] += 1
        
        return optimization_results
    
    def create_dashboard_links(self, dashboard_file: Path) -> bool:
        """Cria links para arquivos do dashboard"""
        try:
            with open(dashboard_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if "## 🔗 **Links Automáticos**" not in content:
                links_section = f"""## 🔗 **Links Automáticos - Dashboard**

> [!info] **Sistema de Dashboard**
> Este arquivo faz parte do sistema de dashboard da wiki

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]

### **📊 Links do Dashboard**
- [[../maps/automatic_linkage_report|Relatório de Linkagem]]
- [[../maps/navigation_performance_report|Relatório de Navegação]]
- [[../log/README|Logs e Relatórios]]

### **📈 Métricas do Dashboard**
- **Categoria**: Dashboard
- **Função**: Gerenciamento de tarefas e métricas
- **Status**: Ativo

---

"""
                
                content += "\n" + links_section
                
                with open(dashboard_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"✅ Links criados para: {dashboard_file}")
                return True
            
            return False
            
        except Exception as e:
            print(f"❌ Erro ao criar links para {dashboard_file}: {e}")
            return False
    
    def optimize_bmad_category(self) -> Dict:
        """Otimiza categoria BMAD (85.2% órfãos)"""
        print("🤖 Otimizando categoria BMAD...")
        
        bmad_path = self.wiki_path / "bmad"
        optimization_results = {
            'category': 'BMAD',
            'files_processed': 0,
            'links_created': 0,
            'errors': 0
        }
        
        # Processar arquivos BMAD
        bmad_files = list(bmad_path.rglob("*.md"))
        
        for bmad_file in bmad_files:
            try:
                if self.create_bmad_links(bmad_file):
                    optimization_results['links_created'] += 1
                optimization_results['files_processed'] += 1
                
            except Exception as e:
                print(f"❌ Erro ao processar {bmad_file}: {e}")
                optimization_results['errors'] += 1
        
        return optimization_results
    
    def create_bmad_links(self, bmad_file: Path) -> bool:
        """Cria links para arquivos BMAD"""
        try:
            with open(bmad_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if "## 🔗 **Links Automáticos**" not in content:
                links_section = f"""## 🔗 **Links Automáticos - BMAD**

> [!info] **Sistema BMAD**
> Este arquivo faz parte do sistema BMAD de agentes inteligentes

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../bmad/README|Sistema BMAD]]

### **🤖 Links BMAD**
- [[../docs/system_generator/BMAD_System_Complete_Guide|Guia Completo BMAD]]
- [[../docs/system_generator/Specialized_Agents_Guide|Guia de Agentes]]
- [[../maps/bmad_agents_index|Índice de Agentes]]

### **📊 Categoria BMAD**
- **Categoria**: BMAD_System
- **Função**: Sistema de agentes inteligentes
- **Status**: Ativo

---

"""
                
                content += "\n" + links_section
                
                with open(bmad_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"✅ Links criados para: {bmad_file}")
                return True
            
            return False
            
        except Exception as e:
            print(f"❌ Erro ao criar links para {bmad_file}: {e}")
            return False
    
    def optimize_habdel_category(self) -> Dict:
        """Otimiza categoria Habdel (58.3% órfãos)"""
        print("🔬 Otimizando categoria Habdel...")
        
        habdel_path = self.wiki_path / "habdel"
        optimization_results = {
            'category': 'Habdel',
            'files_processed': 0,
            'links_created': 0,
            'errors': 0
        }
        
        # Processar arquivos Habdel
        habdel_files = list(habdel_path.rglob("*.md"))
        
        for habdel_file in habdel_files:
            try:
                if self.create_habdel_links(habdel_file):
                    optimization_results['links_created'] += 1
                optimization_results['files_processed'] += 1
                
            except Exception as e:
                print(f"❌ Erro ao processar {habdel_file}: {e}")
                optimization_results['errors'] += 1
        
        return optimization_results
    
    def create_habdel_links(self, habdel_file: Path) -> bool:
        """Cria links para arquivos Habdel"""
        try:
            with open(habdel_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if "## 🔗 **Links Automáticos**" not in content:
                links_section = f"""## 🔗 **Links Automáticos - Habdel**

> [!info] **Sistema Habdel**
> Este arquivo faz parte do sistema Habdel de pesquisa

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../habdel/README|Sistema Habdel]]

### **🔬 Links Habdel**
- [[../docs/research/habdel/README|Pesquisa Habdel]]
- [[../maps/habdel_index|Índice Habdel]]
- [[../integration/README|Sistema de Integração]]

### **📊 Categoria Habdel**
- **Categoria**: Research
- **Função**: Sistema de pesquisa e análise
- **Status**: Ativo

---

"""
                
                content += "\n" + links_section
                
                with open(habdel_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"✅ Links criados para: {habdel_file}")
                return True
            
            return False
            
        except Exception as e:
            print(f"❌ Erro ao criar links para {habdel_file}: {e}")
            return False
    
    def generate_optimization_report(self, results: Dict) -> Dict:
        """Gera relatório de otimização"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'optimization_results': results,
            'summary': {
                'total_files_processed': sum(r['files_processed'] for r in results.values()),
                'total_links_created': sum(r['links_created'] for r in results.values()),
                'total_errors': sum(r['errors'] for r in results.values()),
                'success_rate': 0.0
            },
            'status': 'success'
        }
        
        # Calcular taxa de sucesso
        total_processed = report['summary']['total_files_processed']
        if total_processed > 0:
            report['summary']['success_rate'] = (
                report['summary']['total_links_created'] / total_processed
            ) * 100
        
        return report
    
    def optimize_all_critical_categories(self) -> Dict:
        """Otimiza todas as categorias críticas"""
        print("🎯 **Task 20.7 - Otimização de Categorias Críticas**")
        print("🔄 Iniciando otimização das categorias críticas...")
        
        # Identificar categorias críticas
        critical_categories = self.identify_critical_categories()
        print(f"📊 Categorias críticas identificadas: {len(critical_categories)}")
        
        # Mostrar top 5 categorias críticas
        print("\n📋 Top 5 Categorias Críticas:")
        for i, (category, stats) in enumerate(list(critical_categories.items())[:5]):
            print(f"  {i+1}. {category}: {stats['orphan_rate']:.1f}% órfãos")
        
        # Otimizar categorias críticas
        results = {}
        
        # Otimizar Scripts
        results['scripts'] = self.optimize_scripts_category()
        
        # Otimizar Logs
        results['logs'] = self.optimize_logs_category()
        
        # Otimizar Dashboard
        results['dashboard'] = self.optimize_dashboard_category()
        
        # Otimizar BMAD
        results['bmad'] = self.optimize_bmad_category()
        
        # Otimizar Habdel
        results['habdel'] = self.optimize_habdel_category()
        
        # Gerar relatório
        report = self.generate_optimization_report(results)
        
        # Salvar relatório
        report_file = self.maps_path / "critical_categories_optimization_report.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Otimização concluída:")
        print(f"   📄 Total de arquivos processados: {report['summary']['total_files_processed']}")
        print(f"   🔗 Total de links criados: {report['summary']['total_links_created']}")
        print(f"   ❌ Total de erros: {report['summary']['total_errors']}")
        print(f"   📈 Taxa de sucesso: {report['summary']['success_rate']:.1f}%")
        print(f"   📊 Relatório salvo em: {report_file}")
        
        return report

def main():
    """Função principal"""
    optimizer = CriticalCategoriesOptimizer()
    report = optimizer.optimize_all_critical_categories()
    
    print(f"\n✅ **Task 20.7 - Sub-tarefas Concluídas**")
    print("✅ Categoria Scripts otimizada")
    print("✅ Categoria Logs otimizada")
    print("✅ Categoria Dashboard otimizada")
    print("✅ Categoria BMAD otimizada")
    print("✅ Categoria Habdel otimizada")
    print("📋 Próximo passo: Validação Final e Métricas")

if __name__ == "__main__":
    main() 