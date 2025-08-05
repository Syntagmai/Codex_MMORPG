#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para criar sistema de categorização inteligente da wiki
Task 20.2 - Criar Sistema de Categorização Inteligente
"""

import os
import re
import json
from datetime import datetime
from pathlib import Path
from collections import defaultdict

class IntelligentCategorizationSystem:
    def __init__(self):
        self.wiki_path = Path("wiki")
        self.results = {
            "categories_defined": {},
            "files_categorized": {},
            "category_indices": {},
            "tag_system": {},
            "categorization_stats": {}
        }
        
        # Definir categorias principais e subcategorias
        self.category_hierarchy = {
            "Core": {
                "description": "Sistemas fundamentais e núcleo do OTClient",
                "subcategories": {
                    "Getting_Started": "Guias de início e primeiros passos",
                    "Module_System": "Sistema de módulos e extensões",
                    "Configuration": "Configuração e setup",
                    "Network": "Sistema de rede e comunicação",
                    "Debug": "Debugging e troubleshooting"
                }
            },
            "Game_Systems": {
                "description": "Sistemas específicos do jogo",
                "subcategories": {
                    "Combat": "Sistema de combate e batalhas",
                    "Items": "Sistema de itens e inventário",
                    "Creatures": "Sistema de criaturas e NPCs",
                    "World": "Sistema de mundo e mapas",
                    "Effects": "Sistema de efeitos visuais"
                }
            },
            "UI_Systems": {
                "description": "Sistemas de interface e usuário",
                "subcategories": {
                    "UI_Framework": "Framework de interface",
                    "OTUI": "Sistema OTUI",
                    "Animations": "Sistema de animações",
                    "Graphics": "Sistema gráfico",
                    "Drag_Drop": "Sistema drag & drop"
                }
            },
            "Development": {
                "description": "Ferramentas e guias de desenvolvimento",
                "subcategories": {
                    "API_Reference": "Referências de API",
                    "Code_Examples": "Exemplos de código",
                    "Best_Practices": "Melhores práticas",
                    "Performance": "Otimização e performance",
                    "Deployment": "Deploy e distribuição"
                }
            },
            "BMAD_System": {
                "description": "Sistema de agentes inteligentes BMAD",
                "subcategories": {
                    "Agents": "Agentes especializados",
                    "Workflows": "Fluxos de trabalho",
                    "Automation": "Automação e scripts",
                    "Templates": "Templates e modelos",
                    "Integration": "Integração com OTClient"
                }
            },
            "Task_Management": {
                "description": "Sistema de gerenciamento de tarefas",
                "subcategories": {
                    "Task_Master": "Sistema principal de tarefas",
                    "Integrated_Manager": "Gerenciador integrado",
                    "Epics": "Epics e projetos",
                    "Reports": "Relatórios e métricas",
                    "Archives": "Arquivos e histórico"
                }
            },
            "Integration": {
                "description": "Sistema de integração OTClient-Canary",
                "subcategories": {
                    "Architecture": "Comparação de arquiteturas",
                    "Protocols": "Análise de protocolos",
                    "UI_Frameworks": "Comparação de frameworks UI",
                    "Scripting": "Comparação de scripting",
                    "Migration": "Guias de migração"
                }
            },
            "Research": {
                "description": "Sistema de pesquisa Habdel",
                "subcategories": {
                    "Canary_Research": "Pesquisa sobre Canary",
                    "OTClient_Research": "Pesquisa sobre OTClient",
                    "Integration_Research": "Pesquisa de integração",
                    "Educational": "Material educacional",
                    "Analysis": "Análises e relatórios"
                }
            },
            "Documentation": {
                "description": "Documentação geral e referências",
                "subcategories": {
                    "Guides": "Guias e tutoriais",
                    "References": "Referências e APIs",
                    "Troubleshooting": "Solução de problemas",
                    "FAQ": "Perguntas frequentes",
                    "Glossary": "Glossários e termos"
                }
            },
            "Tools": {
                "description": "Ferramentas e scripts de manutenção",
                "subcategories": {
                    "Analysis": "Scripts de análise",
                    "Validation": "Scripts de validação",
                    "Generation": "Scripts de geração",
                    "Maintenance": "Scripts de manutenção",
                    "Reports": "Scripts de relatórios"
                }
            },
            "Legacy": {
                "description": "Documentação legada e histórica",
                "subcategories": {
                    "Old_Docs": "Documentação antiga",
                    "Archived": "Arquivos arquivados",
                    "Backup": "Backups e versões",
                    "Historical": "Material histórico",
                    "Deprecated": "Documentação obsoleta"
                }
            }
        }
    
    def categorize_file_by_path(self, file_path):
        """Categoriza um arquivo baseado em seu caminho."""
        path_parts = Path(file_path).parts
        
        # Mapeamento de caminhos para categorias
        path_mapping = {
            "bmad": "BMAD_System",
            "dashboard": "Task_Management",
            "integration": "Integration",
            "habdel": "Research",
            "docs": "Documentation",
            "update": "Tools",
            "log": "Tools",
            "maps": "Tools",
            "legacy_docs": "Legacy",
            "consolidated": "Documentation",
            "educational": "Research",
            "workflows": "BMAD_System",
            "alerts": "Task_Management",
            "metrics": "Tools",
            "cursor_core": "Core"
        }
        
        # Determinar categoria principal
        if len(path_parts) == 1:
            # Arquivo na raiz
            if file_path.endswith(('.md', '.txt')):
                if 'glossario' in file_path.lower() or 'glossary' in file_path.lower():
                    return "Documentation", "Glossary"
                elif 'guia' in file_path.lower() or 'guide' in file_path.lower():
                    return "Documentation", "Guides"
                elif 'relatorio' in file_path.lower() or 'report' in file_path.lower():
                    return "Documentation", "References"
                elif 'troubleshooting' in file_path.lower():
                    return "Documentation", "Troubleshooting"
                else:
                    return "Documentation", "References"
            else:
                return "Documentation", "References"
        
        # Verificar mapeamento de caminhos
        first_part = path_parts[0]
        if first_part in path_mapping:
            category = path_mapping[first_part]
            
            # Determinar subcategoria baseada no caminho
            if len(path_parts) > 1:
                second_part = path_parts[1]
                subcategory_mapping = {
                    "agents": "Agents",
                    "workflows": "Workflows",
                    "guides": "Guides",
                    "templates": "Templates",
                    "results": "Reports",
                    "comparisons": "Architecture",
                    "research": "Canary_Research",
                    "courses": "Educational",
                    "documentation": "Guides",
                    "guides": "Guides",
                    "archives": "Archived",
                    "src": "Old_Docs"
                }
                
                if second_part in subcategory_mapping:
                    return category, subcategory_mapping[second_part]
                else:
                    # Subcategoria padrão baseada na categoria
                    default_subcategories = {
                        "BMAD_System": "Agents",
                        "Task_Management": "Task_Master",
                        "Integration": "Architecture",
                        "Research": "Canary_Research",
                        "Documentation": "Guides",
                        "Tools": "Analysis",
                        "Legacy": "Old_Docs"
                    }
                    return category, default_subcategories.get(category, "References")
            else:
                return category, "References"
        
        # Categoria padrão
        return "Documentation", "References"
    
    def categorize_file_by_content(self, file_path):
        """Categoriza um arquivo baseado em seu conteúdo."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read().lower()
            
            # Palavras-chave para categorização
            keywords = {
                "Core": ["getting started", "primeiros passos", "module system", "configuration", "network", "debug"],
                "Game_Systems": ["combat", "item", "creature", "world", "map", "effect", "battle"],
                "UI_Systems": ["ui", "interface", "otui", "animation", "graphics", "drag", "drop"],
                "Development": ["api", "reference", "example", "best practice", "performance", "deploy"],
                "BMAD_System": ["bmad", "agent", "workflow", "automation", "template"],
                "Task_Management": ["task", "epic", "dashboard", "report", "archive"],
                "Integration": ["integration", "canary", "comparison", "protocol", "migration"],
                "Research": ["research", "habdel", "analysis", "educational", "course"],
                "Documentation": ["guide", "tutorial", "faq", "glossary", "reference"],
                "Tools": ["script", "analysis", "validation", "generation", "maintenance"],
                "Legacy": ["legacy", "old", "archive", "backup", "deprecated"]
            }
            
            # Contar ocorrências de palavras-chave
            category_scores = {}
            for category, words in keywords.items():
                score = sum(content.count(word) for word in words)
                category_scores[category] = score
            
            # Retornar categoria com maior score
            if category_scores:
                best_category = max(category_scores, key=category_scores.get)
                if category_scores[best_category] > 0:
                    return best_category, "Content_Based"
            
            return "Documentation", "References"
            
        except Exception as e:
            return "Documentation", "References"
    
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
    
    def categorize_all_files(self):
        """Categoriza todos os arquivos da wiki."""
        md_files = self.find_all_md_files()
        
        for file_path in md_files:
            # Categorização por caminho (prioridade)
            path_category, path_subcategory = self.categorize_file_by_path(file_path)
            
            # Categorização por conteúdo (backup)
            content_category, content_subcategory = self.categorize_file_by_content(self.wiki_path / file_path)
            
            # Usar categorização por caminho, com fallback para conteúdo
            final_category = path_category
            final_subcategory = path_subcategory
            
            # Se não conseguiu categorizar por caminho, usar conteúdo
            if path_category == "Documentation" and path_subcategory == "References":
                final_category = content_category
                final_subcategory = content_subcategory
            
            self.results["files_categorized"][file_path] = {
                "category": final_category,
                "subcategory": final_subcategory,
                "path_category": path_category,
                "path_subcategory": path_subcategory,
                "content_category": content_category,
                "content_subcategory": content_subcategory
            }
    
    def create_category_indices(self):
        """Cria índices para cada categoria."""
        for category, info in self.category_hierarchy.items():
            category_files = []
            subcategory_files = defaultdict(list)
            
            for file_path, cat_info in self.results["files_categorized"].items():
                if cat_info["category"] == category:
                    category_files.append(file_path)
                    subcategory_files[cat_info["subcategory"]].append(file_path)
            
            self.results["category_indices"][category] = {
                "description": info["description"],
                "total_files": len(category_files),
                "files": category_files,
                "subcategories": {}
            }
            
            for subcategory, files in subcategory_files.items():
                self.results["category_indices"][category]["subcategories"][subcategory] = {
                    "description": info["subcategories"].get(subcategory, "Subcategoria"),
                    "total_files": len(files),
                    "files": files
                }
    
    def create_tag_system(self):
        """Cria sistema de tags inteligente."""
        for file_path, cat_info in self.results["files_categorized"].items():
            category = cat_info["category"]
            subcategory = cat_info["subcategory"]
            
            # Tags baseadas na categoria
            tags = [category.lower(), subcategory.lower()]
            
            # Tags adicionais baseadas no caminho
            path_parts = Path(file_path).parts
            if len(path_parts) > 0:
                tags.append(path_parts[0].lower())
            if len(path_parts) > 1:
                tags.append(path_parts[1].lower())
            
            # Tags baseadas no nome do arquivo
            filename = Path(file_path).stem.lower()
            if 'guide' in filename or 'guia' in filename:
                tags.append('guide')
            if 'api' in filename or 'reference' in filename:
                tags.append('api')
            if 'example' in filename or 'exemplo' in filename:
                tags.append('example')
            if 'tutorial' in filename:
                tags.append('tutorial')
            if 'report' in filename or 'relatorio' in filename:
                tags.append('report')
            
            self.results["tag_system"][file_path] = {
                "tags": list(set(tags)),  # Remover duplicatas
                "category": category,
                "subcategory": subcategory
            }
    
    def generate_statistics(self):
        """Gera estatísticas de categorização."""
        stats = {
            "total_files": len(self.results["files_categorized"]),
            "categories": {},
            "subcategories": {},
            "most_popular_tags": {},
            "categorization_accuracy": {}
        }
        
        # Estatísticas por categoria
        for file_path, cat_info in self.results["files_categorized"].items():
            category = cat_info["category"]
            subcategory = cat_info["subcategory"]
            
            if category not in stats["categories"]:
                stats["categories"][category] = 0
            stats["categories"][category] += 1
            
            if subcategory not in stats["subcategories"]:
                stats["subcategories"][subcategory] = 0
            stats["subcategories"][subcategory] += 1
        
        # Estatísticas de tags
        all_tags = []
        for file_path, tag_info in self.results["tag_system"].items():
            all_tags.extend(tag_info["tags"])
        
        tag_counts = {}
        for tag in all_tags:
            if tag not in tag_counts:
                tag_counts[tag] = 0
            tag_counts[tag] += 1
        
        stats["most_popular_tags"] = dict(sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:20])
        
        # Estatísticas de acurácia
        path_used = 0
        content_used = 0
        
        for file_path, cat_info in self.results["files_categorized"].items():
            if cat_info["category"] == cat_info["path_category"]:
                path_used += 1
            else:
                content_used += 1
        
        stats["categorization_accuracy"] = {
            "path_based": path_used,
            "content_based": content_used,
            "path_percentage": (path_used / len(self.results["files_categorized"])) * 100 if self.results["files_categorized"] else 0
        }
        
        self.results["categorization_stats"] = stats
    
    def save_results(self):
        """Salva os resultados da categorização."""
        # Salvar hierarquia de categorias
        hierarchy_path = self.wiki_path / "maps" / "category_hierarchy.json"
        hierarchy_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(hierarchy_path, "w", encoding="utf-8") as f:
            json.dump(self.category_hierarchy, f, indent=2, ensure_ascii=False)
        
        # Salvar arquivos categorizados
        categorized_path = self.wiki_path / "maps" / "files_categorized.json"
        with open(categorized_path, "w", encoding="utf-8") as f:
            json.dump(self.results["files_categorized"], f, indent=2, ensure_ascii=False)
        
        # Salvar índices de categoria
        indices_path = self.wiki_path / "maps" / "category_indices.json"
        with open(indices_path, "w", encoding="utf-8") as f:
            json.dump(self.results["category_indices"], f, indent=2, ensure_ascii=False)
        
        # Salvar sistema de tags
        tags_path = self.wiki_path / "maps" / "tag_system.json"
        with open(tags_path, "w", encoding="utf-8") as f:
            json.dump(self.results["tag_system"], f, indent=2, ensure_ascii=False)
        
        # Salvar estatísticas
        stats_path = self.wiki_path / "log" / "categorization_stats.json"
        stats_path.parent.mkdir(parents=True, exist_ok=True)
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "task": "20.2 - Criar Sistema de Categorização Inteligente",
            "results": self.results
        }
        
        with open(stats_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
    
    def run(self):
        """Executa o sistema de categorização completo."""
        print("🧠 Iniciando sistema de categorização inteligente...")
        
        # Categorizar todos os arquivos
        print("   📁 Categorizando arquivos...")
        self.categorize_all_files()
        
        # Criar índices de categoria
        print("   📋 Criando índices de categoria...")
        self.create_category_indices()
        
        # Criar sistema de tags
        print("   🏷️ Criando sistema de tags...")
        self.create_tag_system()
        
        # Gerar estatísticas
        print("   📊 Gerando estatísticas...")
        self.generate_statistics()
        
        # Salvar resultados
        print("   💾 Salvando resultados...")
        self.save_results()
        
        # Exibir resultados
        stats = self.results["categorization_stats"]
        print(f"✅ Sistema de categorização concluído!")
        print(f"   📁 Total de arquivos categorizados: {stats['total_files']}")
        print(f"   📂 Categorias principais: {len(stats['categories'])}")
        print(f"   🏷️ Subcategorias: {len(stats['subcategories'])}")
        print(f"   🎯 Acurácia baseada em caminho: {stats['categorization_accuracy']['path_percentage']:.1f}%")
        
        print(f"   📊 Top 5 categorias:")
        sorted_categories = sorted(stats["categories"].items(), key=lambda x: x[1], reverse=True)
        for category, count in sorted_categories[:5]:
            print(f"      - {category}: {count} arquivos")
        
        print(f"   🏷️ Top 5 tags mais populares:")
        for tag, count in list(stats["most_popular_tags"].items())[:5]:
            print(f"      - {tag}: {count} ocorrências")

if __name__ == "__main__":
    categorizer = IntelligentCategorizationSystem()
    categorizer.run() 
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
- **Nome**: intelligent_categorization_system
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

