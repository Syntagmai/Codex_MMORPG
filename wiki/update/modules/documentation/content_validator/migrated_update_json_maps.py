from unicode_aliases import *
# Constantes
MAX_RETRIES = 8

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: update_json_maps.py
Módulo de Destino: documentation.content_validator
Data de Migração: 2025-08-01 12:21:35

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import ContentvalidatorModule

# Conteúdo original do script
#!/usr/bin/env python3
"""
Script para atualização automática dos mapas JSON da wiki do OTClient
Atualiza: maps/tags_index.json, maps/wiki_map.json, maps/relationships.json
"""

import json
import re
from datetime import datetime

class WikiJSONUpdater:
    def __init__(self, wiki_dir: str = "."):
        self.wiki_dir = Path(wiki_dir)
        self.md_files = []
        self.tags_index = {}
        self.wiki_map = {}
        self.relationships = {}
        
    def scan_markdown_files(self) -> List[str]:
        """Escaneia todos os arquivos markdown na pasta wiki"""
        md_files = []
        for file in self.wiki_dir.glob("*.md"):
            if not file.name.startswith(".") and file.name != "README.md":
                md_files.append(file.name)
        self.md_files = sorted(md_files)
        return md_files
    
    def extract_frontmatter(self, file_path: str) -> Dict[str, Any]:
        """Extrai frontmatter de um arquivo markdown"""
        frontmatter = {
            "title": file_path.replace(".md", ""),
            "tags": [],
            "status": "unknown",
            "aliases": [],
            "description": ""
        }
        
        try:
            with open(self.wiki_dir / file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extrair frontmatter
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    frontmatter_text = parts[1].strip()
                    
                    # Extrair tags
                    tags_match = re.search(r'tags:\s*\[(.*?)\]', frontmatter_text)
                    if tags_match:
                        tags_str = tags_match.group(1)
                        frontmatter["tags"] = [tag.strip() for tag in tags_str.split(",")]
                    
                    # Extrair status
                    status_match = re.search(r'status:\s*(\w+)', frontmatter_text)
                    if status_match:
                        frontmatter["status"] = status_match.group(1)
                    
                    # Extrair aliases
                    aliases_match = re.search(r'aliases:\s*\[(.*?)\]', frontmatter_text)
                    if aliases_match:
                        aliases_str = aliases_match.group(1)
                        frontmatter["aliases"] = [alias.strip() for alias in aliases_str.split(",")]
                    
                    # Extrair título
                    title_match = re.search(r'title:\s*(.+)', frontmatter_text)
                    if title_match:
                        frontmatter["title"] = title_match.group(1).strip()
                        
        except Exception as e:
            print(f"Erro ao processar {file_path}: {e}")
            
        return frontmatter
    
    def generate_tags_index(self) -> Dict[str, Any]:
        """Gera o índice de tags"""
        files_by_tag = {}
        tags_by_file = {}
        all_tags = set()
        
        # Processar cada arquivo
        for file in self.md_files:
            frontmatter = self.extract_frontmatter(file)
            tags = frontmatter["tags"]
            
            # Adicionar tags ao arquivo
            tags_by_file[file] = tags
            
            # Adicionar arquivo às tags
            for tag in tags:
                all_tags.add(tag)
                if tag not in files_by_tag:
                    files_by_tag[tag] = []
                files_by_tag[tag].append(file)
        
        # Gerar aliases de busca
        search_aliases = self.generate_search_aliases(files_by_tag)
        
        # Estrutura final
        tags_index = {
            "metadata": {
                "version": "1.0",
                "last_updated": datetime.now().isoformat(),
                "total_files": len(self.md_files),
                "total_tags": len(all_tags),
                "description": "Índice de tags da wiki do OTClient"
            },
            "files_by_tag": files_by_tag,
            "tags_by_file": tags_by_file,
            "search_aliases": search_aliases
        }
        
        return tags_index
    
    def generate_search_aliases(self, files_by_tag: Dict[str, List[str]]) -> Dict[str, str]:
        """Gera aliases de busca para tags"""
        aliases = {}
        
        # Aliases comuns
        common_aliases = {
            "ui": ["interface", "user interface", "widget", "gui"],
            "game": ["jogo", "gameplay", "mecanica"],
            "core": ["nucleo", "principal", "base"],
            "api": ["interface", "programacao", "desenvolvimento"],
            "guide": ["guia", "tutorial", "como fazer"],
            "reference": ["referencia", "documentacao", "manual"]
        }
        
        for tag, alias_list in common_aliases.items():
            if tag in files_by_tag:
                for alias in alias_list:
                    aliases[alias] = tag
        
        return aliases
    
    def generate_wiki_map(self) -> Dict[str, Any]:
        """Gera o mapa completo da wiki"""
        categories = {
            "core": {"name": "Sistema Core", "files": []},
            "ui": {"name": "Interface do Usuário", "files": []},
            "game": {"name": "Sistema de Jogo", "files": []},
            "api": {"name": "APIs e Desenvolvimento", "files": []},
            "guide": {"name": "Guias e Tutoriais", "files": []},
            "reference": {"name": "Referências", "files": []},
            "other": {"name": "Outros", "files": []}
        }
        
        # Categorizar documentos
        for file in self.md_files:
            frontmatter = self.extract_frontmatter(file)
            category = self.categorize_document(file, frontmatter)
            priority = self.get_priority(file, frontmatter)
            description = self.get_description(file, frontmatter)
            
            doc_info = {
                "file": file,
                "title": frontmatter["title"],
                "tags": frontmatter["tags"],
                "status": frontmatter["status"],
                "priority": priority,
                "description": description,
                "aliases": frontmatter["aliases"]
            }
            
            if category in categories:
                categories[category]["files"].append(doc_info)
            else:
                categories["other"]["files"].append(doc_info)
        
        # Gerar estatísticas
        statistics = self.generate_statistics(categories)
        
        # Gerar caminhos de navegação
        navigation = self.generate_navigation_paths(categories)
        
        # Estrutura final
        wiki_map = {
            "metadata": {
                "version": "1.0",
                "last_updated": datetime.now().isoformat(),
                "total_files": len(self.md_files),
                "description": "Mapa completo da wiki do OTClient"
            },
            "categories": categories,
            "statistics": statistics,
            "navigation": navigation
        }
        
        return wiki_map
    
    def categorize_document(self, file: str, frontmatter: Dict[str, Any]) -> str:
        """Categoriza um documento baseado em seu conteúdo"""
        tags = frontmatter["tags"]
        title = frontmatter["title"].lower()
        
        # Categorizar por tags
        if any(tag in ["ui", "interface", "widget"] for tag in tags):
            return "ui"
        elif any(tag in ["game", "jogo", "creature", "item"] for tag in tags):
            return "game"
        elif any(tag in ["core", "nucleo", "principal"] for tag in tags):
            return "core"
        elif any(tag in ["api", "programacao", "desenvolvimento"] for tag in tags):
            return "api"
        elif any(tag in ["guide", "guia", "tutorial"] for tag in tags):
            return "guide"
        elif any(tag in ["reference", "referencia", "manual"] for tag in tags):
            return "reference"
        
        # Categorizar por título
        if "ui" in title or "interface" in title:
            return "ui"
        elif "game" in title or "jogo" in title:
            return "game"
        elif "core" in title or "nucleo" in title:
            return "core"
        elif "api" in title or "programacao" in title:
            return "api"
        elif "guide" in title or "guia" in title:
            return "guide"
        elif "reference" in title or "referencia" in title:
            return "reference"
        
        return "other"
    
    def get_priority(self, file: str, frontmatter: Dict[str, Any]) -> int:
        """Determina a prioridade de um documento"""
        if "core" in frontmatter["tags"]:
            return 1
        elif "guide" in frontmatter["tags"]:
            return 2
        elif "api" in frontmatter["tags"]:
            return 3
        elif "ui" in frontmatter["tags"]:
            return 4
        elif "game" in frontmatter["tags"]:
            return 5
        else:
            return 6
    
    def get_description(self, file: str, frontmatter: Dict[str, Any]) -> str:
        """Extrai descrição do documento"""
        if frontmatter["description"]:
            return frontmatter["description"]
        
        # Gerar descrição baseada no título
        title = frontmatter["title"]
        if "ui" in title.lower():
            return f"Documentação sobre {title}"
        elif "game" in title.lower():
            return f"Documentação sobre {title}"
        elif "api" in title.lower():
            return f"Referência da API: {title}"
        else:
            return f"Documentação: {title}"
    
    def generate_statistics(self, categories: Dict[str, Any]) -> Dict[str, Any]:
        """Gera estatísticas da wiki"""
        stats = {
            "by_category": {},
            "by_status": {},
            "by_priority": {},
            "total_files": len(self.md_files)
        }
        
        # Estatísticas por categoria
        for category, cat_info in categories.items():
            stats["by_category"][category] = len(cat_info["files"])
        
        # Estatísticas por status
        status_counts = {}
        for category, cat_info in categories.items():
            for file_info in cat_info["files"]:
                status = file_info["status"]
                status_counts[status] = status_counts.get(status, 0) + 1
        stats["by_status"] = status_counts
        
        # Estatísticas por prioridade
        priority_counts = {}
        for category, cat_info in categories.items():
            for file_info in cat_info["files"]:
                priority = file_info["priority"]
                priority_counts[priority] = priority_counts.get(priority, 0) + 1
        stats["by_priority"] = priority_counts
        
        return stats
    
    def generate_navigation_paths(self, categories: Dict[str, Any]) -> Dict[str, List[str]]:
        """Gera caminhos de navegação"""
        paths = {
            "beginner": [],
            "intermediate": [],
            "advanced": []
        }
        
        # Caminho para iniciantes
        if "guide" in categories:
            paths["beginner"].extend([f["file"] for f in categories["guide"]["files"]])
        if "core" in categories:
            paths["beginner"].extend([f["file"] for f in categories["core"]["files"]])
        
        # Caminho intermediário
        if "ui" in categories:
            paths["intermediate"].extend([f["file"] for f in categories["ui"]["files"]])
        if "game" in categories:
            paths["intermediate"].extend([f["file"] for f in categories["game"]["files"]])
        
        # Caminho avançado
        if "api" in categories:
            paths["advanced"].extend([f["file"] for f in categories["api"]["files"]])
        if "reference" in categories:
            paths["advanced"].extend([f["file"] for f in categories["reference"]["files"]])
        
        return paths
    
    def generate_relationships(self) -> Dict[str, Any]:
        """Gera relacionamentos entre documentos"""
        relationships = {}
        learning_paths = self.generate_learning_paths()
        dependency_graph = self.generate_dependency_graph(relationships)
        topic_clusters = self.generate_topic_clusters()
        
        # Estrutura final
        relationships_data = {
            "metadata": {
                "version": "1.0",
                "last_updated": datetime.now().isoformat(),
                "total_files": len(self.md_files),
                "description": "Relacionamentos entre documentos da wiki"
            },
            "relationships": relationships,
            "learning_paths": learning_paths,
            "dependency_graph": dependency_graph,
            "topic_clusters": topic_clusters
        }
        
        return relationships_data
    
    def generate_learning_paths(self) -> Dict[str, List[str]]:
        """Gera caminhos de aprendizado"""
        paths = {
            "fundamentals": [],
            "ui_development": [],
            "game_development": [],
            "advanced_topics": []
        }
        
        # Caminho de fundamentos
        for file in self.md_files:
            frontmatter = self.extract_frontmatter(file)
            if "core" in frontmatter["tags"] or "guide" in frontmatter["tags"]:
                paths["fundamentals"].append(file)
        
        # Caminho de desenvolvimento de UI
        for file in self.md_files:
            frontmatter = self.extract_frontmatter(file)
            if "ui" in frontmatter["tags"]:
                paths["ui_development"].append(file)
        
        # Caminho de desenvolvimento de jogo
        for file in self.md_files:
            frontmatter = self.extract_frontmatter(file)
            if "game" in frontmatter["tags"]:
                paths["game_development"].append(file)
        
        # Caminho de tópicos avançados
        for file in self.md_files:
            frontmatter = self.extract_frontmatter(file)
            if "api" in frontmatter["tags"] or "reference" in frontmatter["tags"]:
                paths["advanced_topics"].append(file)
        
        return paths
    
    def generate_dependency_graph(self, relationships: Dict[str, Any]) -> Dict[str, Any]:
        """Gera grafo de dependências"""
        graph = {
            "nodes": [],
            "edges": []
        }
        
        # Adicionar nós (documentos)
        for file in self.md_files:
            frontmatter = self.extract_frontmatter(file)
            graph["nodes"].append({
                "id": file,
                "title": frontmatter["title"],
                "category": self.categorize_document(file, frontmatter)
            })
        
        # Adicionar arestas (relacionamentos)
        for file in self.md_files:
            frontmatter = self.extract_frontmatter(file)
            tags = frontmatter["tags"]
            
            # Relacionamentos baseados em tags
            for other_file in self.md_files:
                if file != other_file:
                    other_frontmatter = self.extract_frontmatter(other_file)
                    other_tags = other_frontmatter["tags"]
                    
                    # Se compartilham tags, criar relacionamento
                    common_tags = set(tags) & set(other_tags)
                    if common_tags:
                        graph["edges"].append({
                            "source": file,
                            "target": other_file,
                            "weight": len(common_tags)
                        })
        
        return graph
    
    def generate_topic_clusters(self) -> Dict[str, List[str]]:
        """Gera clusters de tópicos"""
        clusters = {}
        
        # Cluster de UI
        ui_files = []
        for file in self.md_files:
            frontmatter = self.extract_frontmatter(file)
            if "ui" in frontmatter["tags"]:
                ui_files.append(file)
        if ui_files:
            clusters["ui"] = ui_files
        
        # Cluster de Game
        game_files = []
        for file in self.md_files:
            frontmatter = self.extract_frontmatter(file)
            if "game" in frontmatter["tags"]:
                game_files.append(file)
        if game_files:
            clusters["game"] = game_files
        
        # Cluster de API
        api_files = []
        for file in self.md_files:
            frontmatter = self.extract_frontmatter(file)
            if "api" in frontmatter["tags"]:
                api_files.append(file)
        if api_files:
            clusters["api"] = api_files
        
        return clusters
    
    def update_all_json_files(self):
        """Atualiza todos os arquivos JSON"""
        print("Atualizando mapas JSON da wiki...")
        
        # Escanear arquivos markdown
        md_files = self.scan_markdown_files()
        print(f"Encontrados {len(md_files)} arquivos markdown")
        
        # Gerar tags_index.json
        print("Gerando tags_index.json...")
        self.tags_index = self.generate_tags_index()
        with open(self.wiki_dir / "maps/tags_index.json", 'w', encoding='utf-8') as f:
            json.dump(self.tags_index, f, indent=2, ensure_ascii=False)
        
        # Gerar wiki_map.json
        print("Gerando wiki_map.json...")
        self.wiki_map = self.generate_wiki_map()
        with open(self.wiki_dir / "maps/wiki_map.json", 'w', encoding='utf-8') as f:
            json.dump(self.wiki_map, f, indent=2, ensure_ascii=False)
        
        # Gerar relationships.json
        print("Gerando relationships.json...")
        self.relationships = self.generate_relationships()
        with open(self.wiki_dir / "maps/relationships.json", 'w', encoding='utf-8') as f:
            json.dump(self.relationships, f, indent=2, ensure_ascii=False)
        
        print("Todos os arquivos JSON foram atualizados!")

def main():
    """Função principal"""
    updater = WikiJSONUpdater("wiki")
    updater.update_all_json_files()

if __name__ == "__main__":
    main() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = ContentvalidatorModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script update_json_maps.py executado com sucesso via módulo documentation.content_validator")
    else:
        print(f"❌ Erro na execução do script update_json_maps.py via módulo documentation.content_validator")

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
- **Nome**: migrated_update_json_maps
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

