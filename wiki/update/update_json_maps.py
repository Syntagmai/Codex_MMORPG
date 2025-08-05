#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para atualizar mapas JSON após mudanças da Epic 19
Task 19.7 - Atualizar Mapas JSON e Índices
"""

import os
import re
import json
from datetime import datetime
from pathlib import Path

class JSONMapsUpdater:
    def __init__(self):
        self.wiki_path = Path("wiki")
        self.maps_path = self.wiki_path / "maps"
        self.results = {
            "files_processed": 0,
            "maps_updated": 0,
            "wiki_map_updated": False,
            "tags_index_updated": False,
            "search_index_updated": False,
            "relationships_updated": False,
            "new_files_found": 0,
            "renamed_files_found": 0,
            "errors": []
        }
        
    def scan_wiki_files(self):
        """Escaneia todos os arquivos markdown na wiki."""
        markdown_files = []
        
        for file_path in self.wiki_path.rglob("*.md"):
            if file_path.is_file():
                relative_path = file_path.relative_to(self.wiki_path)
                markdown_files.append(str(relative_path))
        
        return sorted(markdown_files)
    
    def extract_file_metadata(self, file_path):
        """Extrai metadados de um arquivo markdown."""
        try:
            # Tentar diferentes encodings
            encodings = ['utf-8', 'latin-1', 'cp1252']
            content = None
            
            for encoding in encodings:
                try:
                    with open(self.wiki_path / file_path, "r", encoding=encoding) as f:
                        content = f.read()
                    break
                except UnicodeDecodeError:
                    continue
            
            if content is None:
                # Se nenhum encoding funcionar, pular o arquivo
                return None
            
            # Extrair título do arquivo
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            file_path_obj = Path(file_path)
            title = title_match.group(1) if title_match else file_path_obj.stem
            
            # Extrair tags
            tags_match = re.search(r'tags:\s*\[(.*?)\]', content)
            tags = []
            if tags_match:
                tags_str = tags_match.group(1)
                tags = [tag.strip().strip('"\'') for tag in tags_str.split(',')]
            
            # Extrair tipo
            type_match = re.search(r'type:\s*(\w+)', content)
            file_type = type_match.group(1) if type_match else "document"
            
            # Extrair status
            status_match = re.search(r'status:\s*(\w+)', content)
            status = status_match.group(1) if status_match else "active"
            
            return {
                "title": title,
                "tags": tags,
                "type": file_type,
                "status": status,
                "path": str(file_path)
            }
        except Exception as e:
            self.results["errors"].append(f"Erro ao processar {file_path}: {e}")
            file_path_obj = Path(file_path)
            return {
                "title": file_path_obj.stem,
                "tags": [],
                "type": "document",
                "status": "active",
                "path": str(file_path)
            }
    
    def update_wiki_map(self, files_metadata):
        """Atualiza o wiki_map.json."""
        try:
            wiki_map_path = self.maps_path / "wiki_map.json"
            
            if wiki_map_path.exists():
                with open(wiki_map_path, "r", encoding="utf-8") as f:
                    wiki_map = json.load(f)
            else:
                wiki_map = {
                    "metadata": {
                        "version": "1.0",
                        "last_updated": "",
                        "total_documents": 0,
                        "context": "otclient",
                        "description": "OTCLIENT wiki map",
                        "optimized": True,
                        "optimization_date": ""
                    },
                    "categories": {},
                    "files": {}
                }
            
            # Remover duplicatas baseado no nome do arquivo
            unique_files = {}
            for metadata in files_metadata:
                filename = Path(metadata["path"]).name
                if filename not in unique_files:
                    unique_files[filename] = metadata
            
            # Atualizar metadados
            wiki_map["metadata"]["last_updated"] = datetime.now().isoformat()
            wiki_map["metadata"]["total_documents"] = len(unique_files)
            wiki_map["metadata"]["optimization_date"] = datetime.now().isoformat()
            
            # Categorizar arquivos
            categories = {
                "core": {"name": "Sistemas Core", "documents": []},
                "ui": {"name": "Interface do Usuário", "documents": []},
                "development": {"name": "Desenvolvimento", "documents": []},
                "reference": {"name": "Referência", "documents": []},
                "integration": {"name": "Integração", "documents": []},
                "guides": {"name": "Guias", "documents": []},
                "troubleshooting": {"name": "Solução de Problemas", "documents": []}
            }
            
            # Atualizar arquivos
            wiki_map["files"] = {}
            
            for filename, metadata in unique_files.items():
                # Determinar categoria
                category = "guides"  # padrão
                if "core" in filename.lower() or "CORE-" in filename:
                    category = "core"
                elif "ui" in filename.lower() or "interface" in filename.lower():
                    category = "ui"
                elif "development" in filename.lower() or "dev" in filename.lower():
                    category = "development"
                elif "reference" in filename.lower() or "api" in filename.lower():
                    category = "reference"
                elif "integration" in filename.lower() or "habdel" in filename.lower():
                    category = "integration"
                elif "troubleshooting" in filename.lower() or "debug" in filename.lower():
                    category = "troubleshooting"
                
                categories[category]["documents"].append(filename)
                
                # Adicionar ao files
                wiki_map["files"][filename] = {
                    "title": metadata["title"],
                    "tags": metadata["tags"],
                    "status": metadata["status"],
                    "aliases": [metadata["title"].lower().replace(" ", "_")],
                    "category": category,
                    "path": metadata["path"]
                }
            
            # Atualizar categorias
            wiki_map["categories"] = {k: v for k, v in categories.items() if v["documents"]}
            
            # Salvar
            with open(wiki_map_path, "w", encoding="utf-8") as f:
                json.dump(wiki_map, f, indent=2, ensure_ascii=False)
            
            self.results["wiki_map_updated"] = True
            self.results["maps_updated"] += 1
            
        except Exception as e:
            self.results["errors"].append(f"Erro ao atualizar wiki_map.json: {e}")
    
    def update_tags_index(self, files_metadata):
        """Atualiza o tags_index.json."""
        try:
            tags_index_path = self.maps_path / "tags_index.json"
            
            if tags_index_path.exists():
                with open(tags_index_path, "r", encoding="utf-8") as f:
                    tags_index = json.load(f)
            else:
                tags_index = {
                    "metadata": {
                        "version": "1.0",
                        "last_updated": "",
                        "total_files": 0,
                        "total_tags": 0,
                        "description": "OTCLIENT wiki tags index",
                        "optimized": True,
                        "optimization_date": "",
                        "portuguese_tags": 0
                    },
                    "files_by_tag": {},
                    "tags_by_file": {}
                }
            
            # Remover duplicatas baseado no nome do arquivo
            unique_files = {}
            for metadata in files_metadata:
                filename = Path(metadata["path"]).name
                if filename not in unique_files:
                    unique_files[filename] = metadata
            
            # Atualizar metadados
            tags_index["metadata"]["last_updated"] = datetime.now().isoformat()
            tags_index["metadata"]["total_files"] = len(unique_files)
            tags_index["metadata"]["optimization_date"] = datetime.now().isoformat()
            
            # Processar tags
            files_by_tag = {}
            tags_by_file = {}
            portuguese_tags = 0
            
            for filename, metadata in unique_files.items():
                tags = metadata["tags"]
                
                # Adicionar tags padrão se não houver
                if not tags:
                    tags = ["otclient", "documentation"]
                
                # Contar tags em português
                for tag in tags:
                    if any(word in tag.lower() for word in ["sistema", "guia", "configuracao", "desenvolvimento", "interface"]):
                        portuguese_tags += 1
                
                # Organizar por tag
                for tag in tags:
                    if tag not in files_by_tag:
                        files_by_tag[tag] = []
                    if filename not in files_by_tag[tag]:  # Evitar duplicatas
                        files_by_tag[tag].append(filename)
                
                # Organizar por arquivo
                tags_by_file[filename] = tags
            
            tags_index["metadata"]["total_tags"] = len(files_by_tag)
            tags_index["metadata"]["portuguese_tags"] = portuguese_tags
            tags_index["files_by_tag"] = files_by_tag
            tags_index["tags_by_file"] = tags_by_file
            
            # Salvar
            with open(tags_index_path, "w", encoding="utf-8") as f:
                json.dump(tags_index, f, indent=2, ensure_ascii=False)
            
            self.results["tags_index_updated"] = True
            self.results["maps_updated"] += 1
            
        except Exception as e:
            self.results["errors"].append(f"Erro ao atualizar tags_index.json: {e}")
    
    def update_search_index(self, files_metadata):
        """Atualiza o search_index.json."""
        try:
            search_index_path = self.maps_path / "search_index.json"
            
            if search_index_path.exists():
                with open(search_index_path, "r", encoding="utf-8") as f:
                    search_index = json.load(f)
            else:
                search_index = {
                    "metadata": {
                        "version": "2.0",
                        "optimized": True,
                        "created": ""
                    },
                    "quick_search": {},
                    "full_text_search": {}
                }
            
            # Atualizar metadados
            search_index["metadata"]["created"] = datetime.now().isoformat()
            
            # Processar busca rápida
            quick_search = {}
            
            for metadata in files_metadata:
                filename = Path(metadata["path"]).name
                title = metadata["title"]
                tags = metadata["tags"]
                
                # Adicionar por tags
                for tag in tags:
                    if tag not in quick_search:
                        quick_search[tag] = {
                            "files": [],
                            "count": 0,
                            "priority": "medium"
                        }
                    quick_search[tag]["files"].append(filename)
                    quick_search[tag]["count"] += 1
                
                # Adicionar por palavras-chave do título
                title_words = title.lower().split()
                for word in title_words:
                    if len(word) > 3:  # palavras com mais de 3 caracteres
                        if word not in quick_search:
                            quick_search[word] = {
                                "files": [],
                                "count": 0,
                                "priority": "low"
                            }
                        if filename not in quick_search[word]["files"]:
                            quick_search[word]["files"].append(filename)
                            quick_search[word]["count"] += 1
            
            search_index["quick_search"] = quick_search
            
            # Salvar
            with open(search_index_path, "w", encoding="utf-8") as f:
                json.dump(search_index, f, indent=2, ensure_ascii=False)
            
            self.results["search_index_updated"] = True
            self.results["maps_updated"] += 1
            
        except Exception as e:
            self.results["errors"].append(f"Erro ao atualizar search_index.json: {e}")
    
    def update_relationships(self, files_metadata):
        """Atualiza o relationships.json."""
        try:
            relationships_path = self.maps_path / "relationships.json"
            
            if relationships_path.exists():
                with open(relationships_path, "r", encoding="utf-8") as f:
                    relationships = json.load(f)
            else:
                relationships = {
                    "metadata": {
                        "version": "1.0",
                        "last_updated": "",
                        "context": "otclient",
                        "description": "OTCLIENT document relationships"
                    }
                }
            
            # Atualizar metadados
            relationships["metadata"]["last_updated"] = datetime.now().isoformat()
            
            # Processar relacionamentos
            for metadata in files_metadata:
                filename = Path(metadata["path"]).name
                title = metadata["title"]
                tags = metadata["tags"]
                
                # Determinar relacionamentos baseados em tags e título
                related = []
                prerequisites = []
                next_steps = []
                
                # Relacionamentos baseados em tags
                for other_metadata in files_metadata:
                    other_filename = Path(other_metadata["path"]).name
                    if other_filename != filename:
                        common_tags = set(tags) & set(other_metadata["tags"])
                        if common_tags:
                            related.append(other_filename)
                
                # Adicionar ao relationships
                relationships[filename] = {
                    "prerequisites": prerequisites,
                    "next_steps": next_steps,
                    "related": related[:5],  # máximo 5 relacionados
                    "integration_links": []
                }
            
            # Salvar
            with open(relationships_path, "w", encoding="utf-8") as f:
                json.dump(relationships, f, indent=2, ensure_ascii=False)
            
            self.results["relationships_updated"] = True
            self.results["maps_updated"] += 1
            
        except Exception as e:
            self.results["errors"].append(f"Erro ao atualizar relationships.json: {e}")
    
    def run(self):
        """Executa o processo de atualização."""
        print("🔄 Iniciando atualização dos mapas JSON...")
        
        # Escanear arquivos da wiki
        wiki_files = self.scan_wiki_files()
        self.results["files_processed"] = len(wiki_files)
        
        print(f"   📁 Arquivos encontrados: {len(wiki_files)}")
        
        # Extrair metadados
        files_metadata = []
        for file_path in wiki_files:
            metadata = self.extract_file_metadata(file_path)
            if metadata is not None:  # Pular arquivos que não puderam ser processados
                files_metadata.append(metadata)
        
        # Atualizar mapas
        self.update_wiki_map(files_metadata)
        self.update_tags_index(files_metadata)
        self.update_search_index(files_metadata)
        self.update_relationships(files_metadata)
        
        # Salvar relatório
        self.save_report()
        
        print(f"✅ Atualização concluída!")
        print(f"   📁 Arquivos processados: {self.results['files_processed']}")
        print(f"   🔄 Mapas atualizados: {self.results['maps_updated']}")
        print(f"   📊 Wiki Map: {'✅' if self.results['wiki_map_updated'] else '❌'}")
        print(f"   🏷️ Tags Index: {'✅' if self.results['tags_index_updated'] else '❌'}")
        print(f"   🔍 Search Index: {'✅' if self.results['search_index_updated'] else '❌'}")
        print(f"   🔗 Relationships: {'✅' if self.results['relationships_updated'] else '❌'}")
        
        if self.results["errors"]:
            print(f"   ⚠️ Erros encontrados: {len(self.results['errors'])}")
    
    def save_report(self):
        """Salva o relatório de atualização."""
        report = {
            "timestamp": datetime.now().isoformat(),
            "task": "19.7 - Atualizar Mapas JSON e Índices",
            "results": self.results
        }
        
        report_path = self.wiki_path / "log" / "json_maps_update_report.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    updater = JSONMapsUpdater()
    updater.run() 