#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gerar mapa visual da linkagem para Obsidian
Cria arquivos markdown com visualização da linkagem
"""

import json
from datetime import datetime
from pathlib import Path

class LinkMapVisualGenerator:
    def __init__(self):
        self.wiki_path = Path("wiki")
        
    def load_link_map(self):
        """Carrega o mapa de linkagem."""
        map_path = self.wiki_path / "maps" / "link_map.json"
        
        if not map_path.exists():
            print("❌ Mapa de linkagem não encontrado. Execute primeiro o orphan_files_analyzer.py")
            return None
        
        with open(map_path, "r", encoding="utf-8") as f:
            return json.load(f)
    
    def generate_orphan_files_list(self, link_map):
        """Gera lista de arquivos órfãos organizada."""
        orphan_files = {file: data for file, data in link_map.items() if data["is_orphan"]}
        
        # Organizar por categoria
        categories = {}
        for file, data in orphan_files.items():
            category = data["category"]
            if category not in categories:
                categories[category] = []
            categories[category].append(file)
        
        return categories
    
    def generate_linked_files_list(self, link_map):
        """Gera lista de arquivos com links organizada."""
        linked_files = {file: data for file, data in link_map.items() if not data["is_orphan"]}
        
        # Organizar por categoria
        categories = {}
        for file, data in linked_files.items():
            category = data["category"]
            if category not in categories:
                categories[category] = []
            categories[category].append((file, data["link_count"]))
        
        return categories
    
    def generate_orphan_files_md(self, orphan_categories):
        """Gera arquivo markdown com lista de arquivos órfãos."""
        content = []
        content.append("# 📋 Lista de Arquivos Órfãos")
        content.append("")
        content.append(f"*Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}*")
        content.append("")
        content.append("## 📊 Resumo")
        content.append("")
        
        total_orphans = sum(len(files) for files in orphan_categories.values())
        content.append(f"- **Total de arquivos órfãos**: {total_orphans}")
        content.append(f"- **Categorias afetadas**: {len(orphan_categories)}")
        content.append("")
        
        # Ordenar categorias por quantidade de arquivos órfãos
        sorted_categories = sorted(orphan_categories.items(), key=lambda x: len(x[1]), reverse=True)
        
        content.append("## 📂 Arquivos por Categoria")
        content.append("")
        
        for category, files in sorted_categories:
            content.append(f"### {category} ({len(files)} arquivos)")
            content.append("")
            
            # Ordenar arquivos alfabeticamente
            files.sort()
            
            for file in files:
                content.append(f"- `{file}`")
            
            content.append("")
        
        content.append("## 💡 Recomendações")
        content.append("")
        content.append("### Prioridade Alta")
        content.append("- Arquivos na raiz da wiki")
        content.append("- Guias e documentação principal")
        content.append("- Arquivos de referência")
        content.append("")
        
        content.append("### Prioridade Média")
        content.append("- Arquivos em categorias específicas")
        content.append("- Documentação técnica")
        content.append("")
        
        content.append("### Prioridade Baixa")
        content.append("- Arquivos de backup")
        content.append("- Logs e relatórios temporários")
        content.append("- Arquivos de teste")
        content.append("")
        
        content.append("## 🔗 Como Criar Links")
        content.append("")
        content.append("### Links Internos")
        content.append("```markdown")
        content.append("[[Nome do Arquivo]]")
        content.append("[Texto do Link](Nome do Arquivo.md)")
        content.append("```")
        content.append("")
        
        content.append("### Links para Seções")
        content.append("```markdown")
        content.append("[[Nome do Arquivo#Seção]]")
        content.append("[Texto do Link](Nome do Arquivo.md#seção)")
        content.append("```")
        content.append("")
        
        return "\n".join(content)
    
    def generate_linked_files_md(self, linked_categories):
        """Gera arquivo markdown com lista de arquivos linkados."""
        content = []
        content.append("# 🔗 Lista de Arquivos com Links")
        content.append("")
        content.append(f"*Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}*")
        content.append("")
        content.append("## 📊 Resumo")
        content.append("")
        
        total_linked = sum(len(files) for files in linked_categories.values())
        total_links = sum(link_count for files in linked_categories.values() for _, link_count in files)
        content.append(f"- **Total de arquivos com links**: {total_linked}")
        content.append(f"- **Total de links**: {total_links}")
        content.append(f"- **Categorias**: {len(linked_categories)}")
        content.append("")
        
        # Ordenar categorias por quantidade de links
        sorted_categories = sorted(linked_categories.items(), key=lambda x: sum(link_count for _, link_count in x[1]), reverse=True)
        
        content.append("## 📂 Arquivos por Categoria")
        content.append("")
        
        for category, files in sorted_categories:
            total_links_in_category = sum(link_count for _, link_count in files)
            content.append(f"### {category} ({len(files)} arquivos, {total_links_in_category} links)")
            content.append("")
            
            # Ordenar arquivos por quantidade de links
            files.sort(key=lambda x: x[1], reverse=True)
            
            for file, link_count in files:
                content.append(f"- `{file}` ({link_count} links)")
            
            content.append("")
        
        content.append("## 🏆 Top 10 Arquivos Mais Linkados")
        content.append("")
        
        # Encontrar os 10 arquivos com mais links
        all_files = []
        for files in linked_categories.values():
            all_files.extend(files)
        
        top_files = sorted(all_files, key=lambda x: x[1], reverse=True)[:10]
        
        for i, (file, link_count) in enumerate(top_files, 1):
            content.append(f"{i:2d}. `{file}` - **{link_count} links**")
        
        content.append("")
        
        return "\n".join(content)
    
    def generate_link_quality_report(self, link_map):
        """Gera relatório de qualidade da linkagem."""
        content = []
        content.append("# 📈 Relatório de Qualidade da Linkagem")
        content.append("")
        content.append(f"*Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}*")
        content.append("")
        
        # Estatísticas gerais
        total_files = len(link_map)
        orphan_files = sum(1 for data in link_map.values() if data["is_orphan"])
        linked_files = total_files - orphan_files
        total_links = sum(data["link_count"] for data in link_map.values())
        
        orphan_percentage = (orphan_files / total_files) * 100 if total_files > 0 else 0
        linked_percentage = (linked_files / total_files) * 100 if total_files > 0 else 0
        avg_links = total_links / total_files if total_files > 0 else 0
        
        content.append("## 📊 Métricas Gerais")
        content.append("")
        content.append(f"- **Total de arquivos**: {total_files:,}")
        content.append(f"- **Arquivos com links**: {linked_files:,} ({linked_percentage:.1f}%)")
        content.append(f"- **Arquivos órfãos**: {orphan_files:,} ({orphan_percentage:.1f}%)")
        content.append(f"- **Total de links**: {total_links:,}")
        content.append(f"- **Média de links por arquivo**: {avg_links:.1f}")
        content.append("")
        
        # Avaliação da qualidade
        content.append("## 🏆 Avaliação da Qualidade")
        content.append("")
        
        if orphan_percentage < 20:
            quality = "🟢 EXCELENTE"
            description = "Linkagem muito boa, poucos arquivos órfãos"
        elif orphan_percentage < 40:
            quality = "🟡 BOA"
            description = "Linkagem boa, mas pode ser melhorada"
        elif orphan_percentage < 60:
            quality = "🟠 REGULAR"
            description = "Linkagem regular, precisa de melhorias"
        elif orphan_percentage < 80:
            quality = "🔴 RUIM"
            description = "Linkagem ruim, muitos arquivos órfãos"
        else:
            quality = "🚨 CRÍTICA"
            description = "Linkagem crítica, maioria dos arquivos está órfã"
        
        content.append(f"- **Qualidade**: {quality}")
        content.append(f"- **Descrição**: {description}")
        content.append("")
        
        # Análise por categoria
        content.append("## 📂 Análise por Categoria")
        content.append("")
        
        categories = {}
        for file, data in link_map.items():
            category = data["category"]
            if category not in categories:
                categories[category] = {"total": 0, "orphan": 0, "linked": 0, "links": 0}
            
            categories[category]["total"] += 1
            categories[category]["links"] += data["link_count"]
            
            if data["is_orphan"]:
                categories[category]["orphan"] += 1
            else:
                categories[category]["linked"] += 1
        
        # Ordenar por porcentagem de arquivos órfãos
        sorted_categories = sorted(
            categories.items(),
            key=lambda x: (x[1]["orphan"] / x[1]["total"]) if x[1]["total"] > 0 else 0,
            reverse=True
        )
        
        content.append("| Categoria | Total | Órfãos | % Órfãos | Links | Status |")
        content.append("|-----------|-------|--------|----------|-------|--------|")
        
        for category, stats in sorted_categories:
            orphan_percentage = (stats["orphan"] / stats["total"]) * 100 if stats["total"] > 0 else 0
            
            if orphan_percentage > 80:
                status = "⚠️ CRÍTICO"
            elif orphan_percentage > 50:
                status = "🔴 ALTO"
            elif orphan_percentage > 20:
                status = "🟡 MÉDIO"
            else:
                status = "🟢 BAIXO"
            
            content.append(f"| {category} | {stats['total']} | {stats['orphan']} | {orphan_percentage:.1f}% | {stats['links']} | {status} |")
        
        content.append("")
        
        return "\n".join(content)
    
    def run(self):
        """Executa a geração dos mapas visuais."""
        print("🎨 Gerando mapas visuais da linkagem...")
        
        link_map = self.load_link_map()
        if not link_map:
            return
        
        # Gerar arquivos
        orphan_categories = self.generate_orphan_files_list(link_map)
        linked_categories = self.generate_linked_files_list(link_map)
        
        # Gerar conteúdo
        orphan_content = self.generate_orphan_files_md(orphan_categories)
        linked_content = self.generate_linked_files_md(linked_categories)
        quality_content = self.generate_link_quality_report(link_map)
        
        # Salvar arquivos
        files_to_save = [
            ("Arquivos_Orfaos.md", orphan_content),
            ("Arquivos_Linkados.md", linked_content),
            ("Relatorio_Qualidade_Linkagem.md", quality_content)
        ]
        
        for filename, content in files_to_save:
            file_path = self.wiki_path / filename
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"   ✅ {filename} gerado")
        
        print(f"✅ Mapas visuais gerados com sucesso!")
        print(f"   📁 Arquivos criados na pasta wiki/")
        print(f"   📊 {len(link_map)} arquivos analisados")
        print(f"   🚫 {sum(1 for data in link_map.values() if data['is_orphan'])} arquivos órfãos identificados")

if __name__ == "__main__":
    generator = LinkMapVisualGenerator()
    generator.run() 
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
- **Nome**: generate_link_map_visual
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

