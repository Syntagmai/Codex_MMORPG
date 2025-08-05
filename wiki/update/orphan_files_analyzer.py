#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para analisar arquivos órfãos e métricas de linkagem na wiki
Análise completa de arquivos .md sem links
"""

import os
import re
import json
from datetime import datetime
from pathlib import Path
from collections import defaultdict

class OrphanFilesAnalyzer:
    def __init__(self):
        self.wiki_path = Path("wiki")
        self.results = {
            "total_md_files": 0,
            "orphan_files": 0,
            "linked_files": 0,
            "orphan_percentage": 0.0,
            "linked_percentage": 0.0,
            "orphan_files_list": [],
            "linked_files_list": [],
            "link_analysis": {},
            "category_analysis": {},
            "insights": []
        }
        
    def find_all_md_files(self):
        """Encontra todos os arquivos .md na wiki."""
        md_files = []
        for root, dirs, files in os.walk(self.wiki_path):
            # Pular pastas específicas
            dirs[:] = [d for d in dirs if d not in ['.obsidian', '.git', 'node_modules']]
            
            for file in files:
                if file.endswith('.md'):
                    file_path = Path(root) / file
                    relative_path = file_path.relative_to(self.wiki_path)
                    md_files.append(str(relative_path))
        
        return md_files
    
    def extract_links_from_file(self, file_path):
        """Extrai todos os links de um arquivo markdown."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Padrões de links markdown
            patterns = [
                r'\[([^\]]+)\]\(([^)]+)\)',  # [texto](link)
                r'\[\[([^\]]+)\]\]',  # [[wikilink]]
                r'!\[([^\]]*)\]\(([^)]+)\)',  # ![alt](image)
            ]
            
            links = []
            for pattern in patterns:
                matches = re.findall(pattern, content)
                for match in matches:
                    if isinstance(match, tuple):
                        link_text, link_url = match
                    else:
                        link_text = match
                        link_url = match
                    
                    # Filtrar links externos e ignorar links internos (#)
                    if not link_url.startswith(('http', 'https', 'mailto', '#')):
                        if link_url.endswith('.md'):
                            links.append(link_url)
                        elif not link_url.startswith(('http', 'https')):
                            # Pode ser um link relativo
                            links.append(link_url)
            
            return links
        except Exception as e:
            print(f"Erro ao ler arquivo {file_path}: {e}")
            return []
    
    def analyze_file_links(self, md_files):
        """Analisa os links de cada arquivo."""
        file_links = {}
        all_links = set()
        
        for md_file in md_files:
            file_path = self.wiki_path / md_file
            links = self.extract_links_from_file(file_path)
            file_links[md_file] = links
            all_links.update(links)
        
        return file_links, all_links
    
    def categorize_file(self, file_path):
        """Categoriza um arquivo baseado em sua localização."""
        path_parts = Path(file_path).parts
        
        if len(path_parts) == 1:
            return "Raiz"
        elif path_parts[0] == "dashboard":
            return "Dashboard"
        elif path_parts[0] == "maps":
            return "Mapas"
        elif path_parts[0] == "update":
            return "Scripts"
        elif path_parts[0] == "log":
            return "Logs"
        elif path_parts[0] == "bmad":
            return "BMAD"
        elif path_parts[0] == "docs":
            return "Documentação"
        elif path_parts[0] == "integration":
            return "Integração"
        elif path_parts[0] == "habdel":
            return "Habdel"
        elif path_parts[0] == "legacy_docs":
            return "Legacy"
        elif path_parts[0] == "educational":
            return "Educacional"
        elif path_parts[0] == "workflows":
            return "Workflows"
        elif path_parts[0] == "alerts":
            return "Alertas"
        elif path_parts[0] == "metrics":
            return "Métricas"
        elif path_parts[0] == "consolidated":
            return "Consolidado"
        elif path_parts[0] == "tools":
            return "Ferramentas"
        elif path_parts[0] == "cursor_core":
            return "Cursor Core"
        else:
            return "Outros"
    
    def generate_link_map(self, file_links):
        """Gera um mapa de linkagem para cada arquivo."""
        link_map = {}
        
        for file_path, links in file_links.items():
            link_map[file_path] = {
                "has_links": len(links) > 0,
                "link_count": len(links),
                "links": links,
                "category": self.categorize_file(file_path),
                "is_orphan": len(links) == 0
            }
        
        return link_map
    
    def analyze_categories(self, link_map):
        """Analisa as categorias de arquivos."""
        category_stats = defaultdict(lambda: {
            "total": 0,
            "orphan": 0,
            "linked": 0,
            "files": []
        })
        
        for file_path, data in link_map.items():
            category = data["category"]
            category_stats[category]["total"] += 1
            category_stats[category]["files"].append(file_path)
            
            if data["is_orphan"]:
                category_stats[category]["orphan"] += 1
            else:
                category_stats[category]["linked"] += 1
        
        return dict(category_stats)
    
    def generate_insights(self, link_map, category_stats):
        """Gera insights baseados na análise."""
        insights = []
        
        # Insight 1: Arquivos mais órfãos
        orphan_files = [f for f, data in link_map.items() if data["is_orphan"]]
        if orphan_files:
            insights.append({
                "type": "orphan_files",
                "title": "Arquivos Órfãos Identificados",
                "description": f"Encontrados {len(orphan_files)} arquivos sem links",
                "files": orphan_files[:10]  # Top 10
            })
        
        # Insight 2: Categorias com mais órfãos
        orphan_categories = []
        for category, stats in category_stats.items():
            if stats["orphan"] > 0:
                orphan_percentage = (stats["orphan"] / stats["total"]) * 100
                orphan_categories.append({
                    "category": category,
                    "orphan_count": stats["orphan"],
                    "total_count": stats["total"],
                    "orphan_percentage": orphan_percentage
                })
        
        orphan_categories.sort(key=lambda x: x["orphan_percentage"], reverse=True)
        insights.append({
            "type": "orphan_categories",
            "title": "Categorias com Mais Arquivos Órfãos",
            "description": "Categorias que precisam de mais linkagem",
            "categories": orphan_categories[:5]  # Top 5
        })
        
        # Insight 3: Arquivos com mais links
        linked_files = [(f, data) for f, data in link_map.items() if not data["is_orphan"]]
        linked_files.sort(key=lambda x: x[1]["link_count"], reverse=True)
        
        insights.append({
            "type": "most_linked",
            "title": "Arquivos Mais Linkados",
            "description": "Arquivos que são referenciados por muitos outros",
            "files": [{"file": f, "links": data["link_count"]} for f, data in linked_files[:10]]
        })
        
        # Insight 4: Recomendações
        recommendations = []
        if len(orphan_files) > 0:
            recommendations.append("Criar links para arquivos órfãos importantes")
        if any(cat["orphan_percentage"] > 50 for cat in orphan_categories):
            recommendations.append("Revisar categorias com alta taxa de arquivos órfãos")
        
        insights.append({
            "type": "recommendations",
            "title": "Recomendações",
            "description": "Ações sugeridas para melhorar a linkagem",
            "recommendations": recommendations
        })
        
        return insights
    
    def run(self):
        """Executa a análise completa."""
        print("🔍 Iniciando análise de arquivos órfãos...")
        
        # Encontrar todos os arquivos .md
        md_files = self.find_all_md_files()
        self.results["total_md_files"] = len(md_files)
        
        print(f"   📁 Arquivos .md encontrados: {len(md_files)}")
        
        # Analisar links
        file_links, all_links = self.analyze_file_links(md_files)
        
        # Gerar mapa de linkagem
        link_map = self.generate_link_map(file_links)
        
        # Identificar arquivos órfãos
        orphan_files = [f for f, data in link_map.items() if data["is_orphan"]]
        linked_files = [f for f, data in link_map.items() if not data["is_orphan"]]
        
        self.results["orphan_files"] = len(orphan_files)
        self.results["linked_files"] = len(linked_files)
        self.results["orphan_percentage"] = (len(orphan_files) / len(md_files)) * 100 if md_files else 0
        self.results["linked_percentage"] = (len(linked_files) / len(md_files)) * 100 if md_files else 0
        
        self.results["orphan_files_list"] = orphan_files
        self.results["linked_files_list"] = linked_files
        self.results["link_analysis"] = link_map
        
        # Análise por categoria
        category_stats = self.analyze_categories(link_map)
        self.results["category_analysis"] = category_stats
        
        # Gerar insights
        insights = self.generate_insights(link_map, category_stats)
        self.results["insights"] = insights
        
        # Salvar relatório
        self.save_report()
        
        # Exibir resultados
        print(f"✅ Análise concluída!")
        print(f"   📊 Total de arquivos .md: {self.results['total_md_files']}")
        print(f"   🔗 Arquivos com links: {self.results['linked_files']} ({self.results['linked_percentage']:.1f}%)")
        print(f"   🚫 Arquivos órfãos: {self.results['orphan_files']} ({self.results['orphan_percentage']:.1f}%)")
        
        if orphan_files:
            print(f"   📋 Primeiros 5 arquivos órfãos:")
            for file in orphan_files[:5]:
                print(f"      - {file}")
        
        # Mostrar insights principais
        if insights:
            print(f"   💡 Insights principais:")
            for insight in insights[:2]:  # Mostrar apenas os 2 primeiros insights
                print(f"      - {insight['title']}: {insight['description']}")
    
    def save_report(self):
        """Salva o relatório de análise."""
        report = {
            "timestamp": datetime.now().isoformat(),
            "analysis": "Orphan Files Analysis",
            "results": self.results
        }
        
        report_path = self.wiki_path / "log" / "orphan_files_analysis.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        # Salvar também um mapa simplificado
        link_map_simple = {}
        for file_path, data in self.results["link_analysis"].items():
            link_map_simple[file_path] = {
                "has_links": data["has_links"],
                "link_count": data["link_count"],
                "category": data["category"],
                "is_orphan": data["is_orphan"]
            }
        
        map_path = self.wiki_path / "maps" / "link_map.json"
        map_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(map_path, "w", encoding="utf-8") as f:
            json.dump(link_map_simple, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    analyzer = OrphanFilesAnalyzer()
    analyzer.run()

