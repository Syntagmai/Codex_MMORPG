#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gerar relatório visual das métricas de arquivos órfãos
Relatório detalhado com gráficos ASCII e insights
"""

import json
from datetime import datetime
from pathlib import Path

class OrphanMetricsReporter:
    def __init__(self):
        self.wiki_path = Path("wiki")
        
    def load_analysis_data(self):
        """Carrega os dados da análise."""
        analysis_path = self.wiki_path / "log" / "orphan_files_analysis.json"
        
        if not analysis_path.exists():
            print("❌ Arquivo de análise não encontrado. Execute primeiro o orphan_files_analyzer.py")
            return None
        
        with open(analysis_path, "r", encoding="utf-8") as f:
            return json.load(f)
    
    def create_ascii_chart(self, percentage, width=50):
        """Cria um gráfico ASCII simples."""
        filled = int((percentage / 100) * width)
        empty = width - filled
        return "█" * filled + "░" * empty
    
    def generate_report(self):
        """Gera o relatório visual completo."""
        data = self.load_analysis_data()
        if not data:
            return
        
        results = data["results"]
        
        print("=" * 80)
        print("📊 RELATÓRIO DE MÉTRICAS - ARQUIVOS ÓRFÃOS NA WIKI")
        print("=" * 80)
        print(f"📅 Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print()
        
        # Métricas Gerais
        print("🎯 MÉTRICAS GERAIS")
        print("-" * 40)
        print(f"📁 Total de arquivos .md: {results['total_md_files']:,}")
        print(f"🔗 Arquivos com links: {results['linked_files']:,} ({results['linked_percentage']:.1f}%)")
        print(f"🚫 Arquivos órfãos: {results['orphan_files']:,} ({results['orphan_percentage']:.1f}%)")
        print()
        
        # Gráfico de distribuição
        print("📈 DISTRIBUIÇÃO DE ARQUIVOS")
        print("-" * 40)
        print("Com links:")
        print(f"  {self.create_ascii_chart(results['linked_percentage'])} {results['linked_percentage']:.1f}%")
        print("Órfãos:")
        print(f"  {self.create_ascii_chart(results['orphan_percentage'])} {results['orphan_percentage']:.1f}%")
        print()
        
        # Análise por Categoria
        print("📂 ANÁLISE POR CATEGORIA")
        print("-" * 40)
        print(f"{'Categoria':<15} {'Total':<8} {'Órfãos':<8} {'% Órfãos':<10} {'Status':<10}")
        print("-" * 60)
        
        category_stats = results["category_analysis"]
        sorted_categories = sorted(
            category_stats.items(),
            key=lambda x: (x[1]["orphan"] / x[1]["total"]) if x[1]["total"] > 0 else 0,
            reverse=True
        )
        
        for category, stats in sorted_categories:
            if stats["total"] > 0:
                orphan_percentage = (stats["orphan"] / stats["total"]) * 100
                status = "⚠️ CRÍTICO" if orphan_percentage > 80 else "🔴 ALTO" if orphan_percentage > 50 else "🟡 MÉDIO" if orphan_percentage > 20 else "🟢 BAIXO"
                print(f"{category:<15} {stats['total']:<8} {stats['orphan']:<8} {orphan_percentage:<10.1f} {status:<10}")
        
        print()
        
        # Top 10 Arquivos Órfãos
        print("🚫 TOP 10 ARQUIVOS ÓRFÃOS (Mais Importantes)")
        print("-" * 50)
        orphan_files = results["orphan_files_list"]
        
        # Priorizar arquivos da raiz e categorias importantes
        priority_files = []
        other_files = []
        
        for file in orphan_files:
            if file.count("\\") == 0 or file.startswith(("README", "Guia", "Glossario", "Conceitos")):
                priority_files.append(file)
            else:
                other_files.append(file)
        
        # Mostrar arquivos prioritários primeiro
        for i, file in enumerate(priority_files[:5], 1):
            print(f"{i:2d}. {file}")
        
        # Mostrar alguns outros arquivos
        for i, file in enumerate(other_files[:5], len(priority_files) + 1):
            print(f"{i:2d}. {file}")
        
        print()
        
        # Insights
        print("💡 INSIGHTS E RECOMENDAÇÕES")
        print("-" * 40)
        
        insights = results["insights"]
        for insight in insights:
            if insight["type"] == "orphan_categories":
                print("🎯 Categorias que precisam de atenção:")
                for cat in insight["categories"][:3]:
                    print(f"   • {cat['category']}: {cat['orphan_percentage']:.1f}% órfãos ({cat['orphan_count']}/{cat['total_count']})")
                print()
            
            elif insight["type"] == "recommendations":
                print("🔧 Ações Recomendadas:")
                for rec in insight["recommendations"]:
                    print(f"   • {rec}")
                print()
        
        # Estatísticas Adicionais
        print("📊 ESTATÍSTICAS ADICIONAIS")
        print("-" * 40)
        
        # Arquivos com mais links
        link_analysis = results["link_analysis"]
        most_linked = sorted(
            [(f, data) for f, data in link_analysis.items() if not data["is_orphan"]],
            key=lambda x: x[1]["link_count"],
            reverse=True
        )
        
        print("🔗 Arquivos mais linkados:")
        for i, (file, data) in enumerate(most_linked[:5], 1):
            print(f"   {i}. {file} ({data['link_count']} links)")
        
        print()
        
        # Qualidade da linkagem
        total_links = sum(data["link_count"] for data in link_analysis.values())
        avg_links_per_file = total_links / len(link_analysis) if link_analysis else 0
        
        print(f"📈 Qualidade da linkagem:")
        print(f"   • Total de links: {total_links:,}")
        print(f"   • Média de links por arquivo: {avg_links_per_file:.1f}")
        print(f"   • Taxa de arquivos órfãos: {results['orphan_percentage']:.1f}%")
        
        # Avaliação geral
        print()
        print("🏆 AVALIAÇÃO GERAL")
        print("-" * 40)
        
        orphan_percentage = results["orphan_percentage"]
        if orphan_percentage < 20:
            status = "🟢 EXCELENTE"
            description = "Linkagem muito boa, poucos arquivos órfãos"
        elif orphan_percentage < 40:
            status = "🟡 BOA"
            description = "Linkagem boa, mas pode ser melhorada"
        elif orphan_percentage < 60:
            status = "🟠 REGULAR"
            description = "Linkagem regular, precisa de melhorias"
        elif orphan_percentage < 80:
            status = "🔴 RUIM"
            description = "Linkagem ruim, muitos arquivos órfãos"
        else:
            status = "🚨 CRÍTICA"
            description = "Linkagem crítica, maioria dos arquivos está órfã"
        
        print(f"Status: {status}")
        print(f"Descrição: {description}")
        print()
        
        print("=" * 80)
        print("📋 RESUMO EXECUTIVO")
        print("=" * 80)
        print(f"• {results['total_md_files']:,} arquivos .md analisados")
        print(f"• {results['orphan_files']:,} arquivos órfãos ({results['orphan_percentage']:.1f}%)")
        print(f"• {results['linked_files']:,} arquivos com links ({results['linked_percentage']:.1f}%)")
        print(f"• {len(category_stats)} categorias de arquivos identificadas")
        print(f"• Qualidade geral: {status}")
        print()
        print("💡 Próximos passos sugeridos:")
        print("   1. Criar links para arquivos órfãos importantes")
        print("   2. Revisar categorias com alta taxa de arquivos órfãos")
        print("   3. Melhorar a navegabilidade da documentação")
        print("   4. Implementar sistema de links automáticos")
        print("=" * 80)
    
    def save_report(self):
        """Salva o relatório em arquivo de texto."""
        # Redirecionar output para arquivo
        report_path = self.wiki_path / "log" / "orphan_metrics_report.txt"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Salvar relatório
        with open(report_path, "w", encoding="utf-8") as f:
            # Aqui você pode implementar a lógica para salvar o relatório
            # Por simplicidade, vou apenas criar um arquivo com as métricas principais
            data = self.load_analysis_data()
            if data:
                results = data["results"]
                f.write(f"RELATÓRIO DE MÉTRICAS - ARQUIVOS ÓRFÃOS\n")
                f.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
                f.write(f"Total de arquivos .md: {results['total_md_files']:,}\n")
                f.write(f"Arquivos órfãos: {results['orphan_files']:,} ({results['orphan_percentage']:.1f}%)\n")
                f.write(f"Arquivos com links: {results['linked_files']:,} ({results['linked_percentage']:.1f}%)\n")

if __name__ == "__main__":
    reporter = OrphanMetricsReporter()
    reporter.generate_report()
    reporter.save_report() 
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
- **Nome**: orphan_metrics_report
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

