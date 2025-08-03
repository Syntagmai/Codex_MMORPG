from unicode_aliases import *
# Constantes
MAX_RETRIES = 8

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: update_wiki_maps.py
Módulo de Destino: maps.wiki_indexer
Data de Migração: 2025-08-01 12:21:35

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import WikiindexerModule

# Conteúdo original do script
#!/usr/bin/env python3
"""
Script para atualização automática dos mapas JSON da wiki do OTClient
Atualiza: maps/tags_index.json, maps/wiki_map.json, maps/relationships.json
Usa contexto detectado automaticamente
"""
import json
import re
from datetime import datetime

class WikiJSONUpdater:
    def __init__(self, wiki_dir: str = "wiki"):
        self.wiki_dir = Path(wiki_dir)
        self.md_files = []
        self.tags_index = {}
        self.wiki_map = {}
        self.relationships = {}
        
        # Detectar contexto
        self.context_data = self.load_context_data()
        self.docs_path = self.context_data['paths']['docs']
        self.maps_path = self.context_data['paths']['maps']
        
    def load_context_data(self) -> Dict[str, Any]:
        """Carrega dados de contexto detectado"""
        context_file = Path("wiki/maps/context_data.json")
        if context_file.exists():
            with open(context_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Fallback para contexto OTClient
            return {
                'context': 'otclient',
                'paths': {
                    'docs': 'wiki/otclient/',
                    'maps': 'wiki/maps/'
                }
            }
        
    def scan_markdown_files(self) -> List[str]:
        """Escaneia todos os arquivos markdown na pasta de documentação"""
        md_files = []
        docs_dir = self.wiki_dir / self.docs_path.replace('wiki/', '')
        
        if docs_dir.exists():
            for file in docs_dir.glob("*.md"):
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
            docs_dir = self.wiki_dir / self.docs_path.replace('wiki/', '')
            with open(docs_dir / file_path, 'r', encoding='utf-8') as f:
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
        """Gera índice de tags"""
        tags_index = {
            "metadata": {
                "version": "1.0",
                "last_updated": datetime.now().isoformat(),
                "total_files": len(self.md_files),
                "total_tags": 0,
                "description": f"{self.context_data['context'].upper()} wiki tags index"
            },
            "files_by_tag": {}
        }
        
        all_tags = set()
        
        for file_name in self.md_files:
            frontmatter = self.extract_frontmatter(file_name)
            
            for tag in frontmatter["tags"]:
                all_tags.add(tag)
                if tag not in tags_index["files_by_tag"]:
                    tags_index["files_by_tag"][tag] = []
                tags_index["files_by_tag"][tag].append(file_name)
        
        tags_index["metadata"]["total_tags"] = len(all_tags)
        return tags_index
    
    def generate_wiki_map(self) -> Dict[str, Any]:
        """Gera mapa da wiki"""
        wiki_map = {
            "metadata": {
                "version": "1.0",
                "last_updated": datetime.now().isoformat(),
                "total_documents": len(self.md_files),
                "context": self.context_data['context'],
                "description": f"{self.context_data['context'].upper()} wiki map"
            },
            "categories": {
                "core": {
                    "name": "Core Systems",
                    "documents": []
                },
                "ui": {
                    "name": "User Interface",
                    "documents": []
                },
                "development": {
                    "name": "Development",
                    "documents": []
                },
                "reference": {
                    "name": "Reference",
                    "documents": []
                },
                "integration": {
                    "name": "Integration",
                    "documents": []
                }
            },
            "files": {}
        }
        
        for file_name in self.md_files:
            frontmatter = self.extract_frontmatter(file_name)
            
            # Categorizar documento
            category = self.categorize_document(file_name, frontmatter)
            if category in wiki_map["categories"]:
                wiki_map["categories"][category]["documents"].append(file_name)
            
            # Adicionar informações do arquivo
            wiki_map["files"][file_name] = {
                "title": frontmatter["title"],
                "tags": frontmatter["tags"],
                "status": frontmatter["status"],
                "aliases": frontmatter["aliases"],
                "category": category,
                "description": frontmatter["description"]
            }
        
        return wiki_map
    
    def categorize_document(self, file_name: str, frontmatter: Dict[str, Any]) -> str:
        """Categoriza documento baseado no nome e tags"""
        file_lower = file_name.lower()
        tags_lower = [tag.lower() for tag in frontmatter["tags"]]
        
        # Categorias baseadas no contexto
        if self.context_data['context'] == 'otclient':
            if any(keyword in file_lower for keyword in ['ui', 'widget', 'interface']):
                return "ui"
            elif any(keyword in file_lower for keyword in ['module', 'development']):
                return "development"
            elif any(keyword in file_lower for keyword in ['api', 'reference']):
                return "reference"
            elif any(keyword in tags_lower for keyword in ['integration', 'canary']):
                return "integration"
            else:
                return "core"
        elif self.context_data['context'] == 'canary':
            if any(keyword in file_lower for keyword in ['game', 'logic', 'server']):
                return "core"
            elif any(keyword in file_lower for keyword in ['database', 'world']):
                return "development"
            elif any(keyword in file_lower for keyword in ['api', 'reference']):
                return "reference"
            elif any(keyword in tags_lower for keyword in ['integration', 'otclient']):
                return "integration"
            else:
                return "core"
        else:  # unified
            if any(keyword in file_lower for keyword in ['integration', 'cross']):
                return "integration"
            elif any(keyword in file_lower for keyword in ['api', 'reference']):
                return "reference"
            elif any(keyword in file_lower for keyword in ['development', 'module']):
                return "development"
            else:
                return "core"
    
    def generate_relationships(self) -> Dict[str, Any]:
        """Gera relacionamentos entre documentos"""
        relationships = {
            "metadata": {
                "version": "1.0",
                "last_updated": datetime.now().isoformat(),
                "context": self.context_data['context'],
                "description": f"{self.context_data['context'].upper()} document relationships"
            }
        }
        
        for file_name in self.md_files:
            frontmatter = self.extract_frontmatter(file_name)
            
            relationships[file_name] = {
                "prerequisites": [],
                "next_steps": [],
                "related": [],
                "integration_links": []
            }
            
            # Adicionar links de integração se relevante
            if self.context_data['integration_enabled']:
                if any(tag in frontmatter["tags"] for tag in ['integration', 'canary', 'otclient']):
                    relationships[file_name]["integration_links"] = [
                        "OTClient_Canary_Integration.md"
                    ]
        
        return relationships
    
    def update_all_json_files(self):
        """Atualiza todos os arquivos JSON"""
        print(f"Atualizando mapas JSON da wiki ({self.context_data['context'].upper()})...")
        
        # Escanear arquivos markdown
        md_files = self.scan_markdown_files()
        print(f"Encontrados {len(md_files)} arquivos markdown")
        
        # Gerar tags_index.json
        print("Gerando tags_index.json...")
        self.tags_index = self.generate_tags_index()
        with open(self.wiki_dir / self.maps_path.replace('wiki/', '') / "tags_index.json", 'w', encoding='utf-8') as f:
            json.dump(self.tags_index, f, indent=2, ensure_ascii=False)
        
        # Gerar wiki_map.json
        print("Gerando wiki_map.json...")
        self.wiki_map = self.generate_wiki_map()
        with open(self.wiki_dir / self.maps_path.replace('wiki/', '') / "wiki_map.json", 'w', encoding='utf-8') as f:
            json.dump(self.wiki_map, f, indent=2, ensure_ascii=False)
        
        # Gerar relationships.json
        print("Gerando relationships.json...")
        self.relationships = self.generate_relationships()
        with open(self.wiki_dir / self.maps_path.replace('wiki/', '') / "relationships.json", 'w',
    encoding='utf-8') as f:
            json.dump(self.relationships, f, indent=2, ensure_ascii=False)
        
        print("Todos os arquivos JSON foram atualizados!")

if __name__ == "__main__":
    updater = WikiJSONUpdater()
    updater.update_all_json_files() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = WikiindexerModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script update_wiki_maps.py executado com sucesso via módulo maps.wiki_indexer")
    else:
        print(f"❌ Erro na execução do script update_wiki_maps.py via módulo maps.wiki_indexer")
