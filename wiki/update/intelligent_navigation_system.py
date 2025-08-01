#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Navegação Inteligente Otimizada
==========================================

Este script implementa navegação inteligente otimizada entre documentos consolidados
com busca semântica e links contextuais.

Autor: Sistema BMAD - Navigation Agent
Data: 2025-08-01
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import logging

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class IntelligentNavigationSystem:
    """Sistema de navegação inteligente otimizada"""
    
    def __init__(self, consolidated_dir: str = "wiki/consolidated"):
        """
        Inicializa o sistema de navegação inteligente.
        
        Args:
            consolidated_dir: Diretório dos documentos consolidados
        """
        self.consolidated_dir = Path(consolidated_dir)
        self.navigation_index_file = self.consolidated_dir / "navigation_index.json"
        self.intelligent_nav_file = self.consolidated_dir / "intelligent_navigation.json"
        
        # Carregar índice de navegação existente
        self.navigation_data = self.load_navigation_index()
        
        # Estrutura de navegação inteligente
        self.intelligent_nav = {
            "navigation_graph": {},
            "semantic_links": {},
            "contextual_paths": {},
            "quick_access": {},
            "search_index": {},
            "breadcrumbs": {},
            "related_documents": {}
        }
        
    def load_navigation_index(self) -> Dict[str, Any]:
        """
        Carrega o índice de navegação existente.
        
        Returns:
            Dados do índice de navegação
        """
        if self.navigation_index_file.exists():
            try:
                with open(self.navigation_index_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Erro ao carregar índice de navegação: {e}")
        
        return {"structure": {}, "total_documents": 0}
    
    def analyze_document_content(self, file_path: Path) -> Dict[str, Any]:
        """
        Analisa o conteúdo de um documento para extrair informações de navegação.
        
        Args:
            file_path: Caminho para o documento
            
        Returns:
            Informações extraídas do documento
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extrair título
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else file_path.stem
            
            # Extrair tags
            tags_match = re.search(r'tags:\s*\[(.*?)\]', content)
            tags = []
            if tags_match:
                tags = [tag.strip() for tag in tags_match.group(1).split(',')]
            
            # Extrair links internos
            internal_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
            
            # Extrair palavras-chave
            keywords = re.findall(r'\b\w{4,}\b', content.lower())
            keywords = [kw for kw in keywords if len(kw) > 3][:20]
            
            return {
                "title": title,
                "tags": tags,
                "internal_links": internal_links,
                "keywords": keywords,
                "file_size": len(content),
                "word_count": len(content.split())
            }
            
        except Exception as e:
            logger.error(f"Erro ao analisar {file_path}: {e}")
            return {}
    
    def build_navigation_graph(self):
        """
        Constrói grafo de navegação entre documentos.
        """
        logger.info("🕸️ Construindo grafo de navegação...")
        
        graph = {}
        
        # Analisar todos os documentos
        for main_category in self.navigation_data.get("structure", {}).keys():
            category_dir = self.consolidated_dir / main_category
            if category_dir.exists():
                graph[main_category] = {}
                
                for subcategory in self.navigation_data["structure"][main_category].keys():
                    subcategory_dir = category_dir / subcategory
                    if subcategory_dir.exists():
                        graph[main_category][subcategory] = {}
                        
                        for file_path in subcategory_dir.glob("*.md"):
                            doc_info = self.analyze_document_content(file_path)
                            if doc_info:
                                graph[main_category][subcategory][file_path.name] = doc_info
        
        self.intelligent_nav["navigation_graph"] = graph
        logger.info("✅ Grafo de navegação construído")
    
    def create_semantic_links(self):
        """
        Cria links semânticos entre documentos relacionados.
        """
        logger.info("🔗 Criando links semânticos...")
        
        semantic_links = {}
        
        # Agrupar documentos por tags e palavras-chave
        tag_groups = {}
        keyword_groups = {}
        
        for main_cat, subcats in self.intelligent_nav["navigation_graph"].items():
            for subcat, docs in subcats.items():
                for doc_name, doc_info in docs.items():
                    # Agrupar por tags
                    for tag in doc_info.get("tags", []):
                        if tag not in tag_groups:
                            tag_groups[tag] = []
                        tag_groups[tag].append(f"{main_cat}/{subcat}/{doc_name}")
                    
                    # Agrupar por palavras-chave
                    for keyword in doc_info.get("keywords", []):
                        if keyword not in keyword_groups:
                            keyword_groups[keyword] = []
                        keyword_groups[keyword].append(f"{main_cat}/{subcat}/{doc_name}")
        
        # Criar links semânticos
        semantic_links["by_tags"] = tag_groups
        semantic_links["by_keywords"] = keyword_groups
        
        self.intelligent_nav["semantic_links"] = semantic_links
        logger.info(f"✅ Links semânticos criados: {len(tag_groups)} grupos por tags, {len(keyword_groups)} grupos por palavras-chave")
    
    def create_contextual_paths(self):
        """
        Cria caminhos contextuais entre documentos.
        """
        logger.info("🛤️ Criando caminhos contextuais...")
        
        contextual_paths = {}
        
        # Definir caminhos contextuais comuns
        common_paths = {
            "otclient_learning": [
                "otclient/research/OTCLIENT-001.md",
                "otclient/research/OTCLIENT-002.md",
                "otclient/research/OTCLIENT-003.md",
                "otclient/documentation/GettingStarted.md",
                "otclient/documentation/ModuleSystem.md"
            ],
            "canary_learning": [
                "canary/research/CANARY-001.md",
                "canary/research/CANARY-002.md",
                "canary/research/CANARY-003.md",
                "canary/research/api_reference.md"
            ],
            "bmad_development": [
                "bmad/agents/BMAD_System_Guide.md",
                "bmad/agents/agent_template.md",
                "bmad/agents/workflow_template.md",
                "bmad/agents/best_practices.md"
            ],
            "integration_guide": [
                "integration/comparisons/INTEGRATION-001.md",
                "integration/comparisons/INTEGRATION-002.md",
                "integration/comparisons/INTEGRATION-003.md",
                "integration/comparisons/integration_guide.md"
            ]
        }
        
        # Verificar quais caminhos existem
        for path_name, path_docs in common_paths.items():
            existing_docs = []
            for doc_path in path_docs:
                full_path = self.consolidated_dir / doc_path
                if full_path.exists():
                    existing_docs.append(doc_path)
            
            if existing_docs:
                contextual_paths[path_name] = existing_docs
        
        self.intelligent_nav["contextual_paths"] = contextual_paths
        logger.info(f"✅ Caminhos contextuais criados: {len(contextual_paths)} caminhos")
    
    def create_quick_access(self):
        """
        Cria sistema de acesso rápido.
        """
        logger.info("⚡ Criando sistema de acesso rápido...")
        
        quick_access = {
            "popular_documents": [],
            "recent_documents": [],
            "essential_guides": [],
            "api_references": [],
            "tutorials": []
        }
        
        # Identificar documentos populares (por tamanho e links)
        all_docs = []
        for main_cat, subcats in self.intelligent_nav["navigation_graph"].items():
            for subcat, docs in subcats.items():
                for doc_name, doc_info in docs.items():
                    all_docs.append({
                        "path": f"{main_cat}/{subcat}/{doc_name}",
                        "info": doc_info
                    })
        
        # Ordenar por popularidade (tamanho do arquivo)
        popular_docs = sorted(all_docs, key=lambda x: x["info"].get("file_size", 0), reverse=True)[:20]
        quick_access["popular_documents"] = [doc["path"] for doc in popular_docs]
        
        # Identificar guias essenciais
        essential_keywords = ["guide", "tutorial", "getting started", "api", "reference"]
        for doc in all_docs:
            title_lower = doc["info"].get("title", "").lower()
            if any(keyword in title_lower for keyword in essential_keywords):
                if "api" in title_lower or "reference" in title_lower:
                    quick_access["api_references"].append(doc["path"])
                elif "tutorial" in title_lower or "guide" in title_lower:
                    quick_access["tutorials"].append(doc["path"])
                else:
                    quick_access["essential_guides"].append(doc["path"])
        
        self.intelligent_nav["quick_access"] = quick_access
        logger.info("✅ Sistema de acesso rápido criado")
    
    def create_search_index(self):
        """
        Cria índice de busca para navegação rápida.
        """
        logger.info("🔍 Criando índice de busca...")
        
        search_index = {
            "by_title": {},
            "by_tags": {},
            "by_keywords": {},
            "by_category": {}
        }
        
        # Indexar por título
        for main_cat, subcats in self.intelligent_nav["navigation_graph"].items():
            for subcat, docs in subcats.items():
                for doc_name, doc_info in docs.items():
                    title = doc_info.get("title", doc_name)
                    search_index["by_title"][title.lower()] = f"{main_cat}/{subcat}/{doc_name}"
                    
                    # Indexar por categoria
                    if main_cat not in search_index["by_category"]:
                        search_index["by_category"][main_cat] = []
                    search_index["by_category"][main_cat].append(f"{main_cat}/{subcat}/{doc_name}")
        
        # Indexar por tags e palavras-chave
        for main_cat, subcats in self.intelligent_nav["navigation_graph"].items():
            for subcat, docs in subcats.items():
                for doc_name, doc_info in docs.items():
                    for tag in doc_info.get("tags", []):
                        if tag not in search_index["by_tags"]:
                            search_index["by_tags"][tag] = []
                        search_index["by_tags"][tag].append(f"{main_cat}/{subcat}/{doc_name}")
                    
                    for keyword in doc_info.get("keywords", []):
                        if keyword not in search_index["by_keywords"]:
                            search_index["by_keywords"][keyword] = []
                        search_index["by_keywords"][keyword].append(f"{main_cat}/{subcat}/{doc_name}")
        
        self.intelligent_nav["search_index"] = search_index
        logger.info("✅ Índice de busca criado")
    
    def create_breadcrumbs(self):
        """
        Cria sistema de breadcrumbs para navegação hierárquica.
        """
        logger.info("🍞 Criando sistema de breadcrumbs...")
        
        breadcrumbs = {}
        
        for main_cat, subcats in self.navigation_data.get("structure", {}).items():
            breadcrumbs[main_cat] = {
                "level": 1,
                "children": {}
            }
            
            for subcat in subcats.keys():
                breadcrumbs[main_cat]["children"][subcat] = {
                    "level": 2,
                    "parent": main_cat,
                    "path": f"{main_cat} > {subcat}"
                }
        
        self.intelligent_nav["breadcrumbs"] = breadcrumbs
        logger.info("✅ Sistema de breadcrumbs criado")
    
    def create_related_documents(self):
        """
        Cria sistema de documentos relacionados.
        """
        logger.info("🔗 Criando sistema de documentos relacionados...")
        
        related_docs = {}
        
        # Analisar links internos para criar relacionamentos
        for main_cat, subcats in self.intelligent_nav["navigation_graph"].items():
            for subcat, docs in subcats.items():
                for doc_name, doc_info in docs.items():
                    doc_path = f"{main_cat}/{subcat}/{doc_name}"
                    related_docs[doc_path] = {
                        "links_to": [],
                        "linked_from": [],
                        "similar_tags": [],
                        "same_category": []
                    }
                    
                    # Documentos com tags similares
                    doc_tags = set(doc_info.get("tags", []))
                    for other_main_cat, other_subcats in self.intelligent_nav["navigation_graph"].items():
                        for other_subcat, other_docs in other_subcats.items():
                            for other_doc_name, other_doc_info in other_docs.items():
                                other_doc_path = f"{other_main_cat}/{other_subcat}/{other_doc_name}"
                                if other_doc_path != doc_path:
                                    other_tags = set(other_doc_info.get("tags", []))
                                    if doc_tags & other_tags:  # Intersecção de tags
                                        related_docs[doc_path]["similar_tags"].append(other_doc_path)
                                    
                                    # Mesma categoria
                                    if other_main_cat == main_cat and other_subcat == subcat:
                                        related_docs[doc_path]["same_category"].append(other_doc_path)
        
        self.intelligent_nav["related_documents"] = related_docs
        logger.info("✅ Sistema de documentos relacionados criado")
    
    def generate_navigation_report(self) -> str:
        """
        Gera relatório de navegação inteligente.
        
        Returns:
            Caminho do relatório
        """
        logger.info("📋 Gerando relatório de navegação inteligente...")
        
        report = {
            "generation_date": datetime.now().isoformat(),
            "summary": {
                "total_documents": self.navigation_data.get("total_documents", 0),
                "navigation_graph_nodes": len(self.intelligent_nav["navigation_graph"]),
                "semantic_links_groups": len(self.intelligent_nav["semantic_links"].get("by_tags", {})),
                "contextual_paths": len(self.intelligent_nav["contextual_paths"]),
                "search_index_entries": len(self.intelligent_nav["search_index"].get("by_title", {}))
            },
            "features": {
                "navigation_graph": "Grafo completo de navegação entre documentos",
                "semantic_links": "Links baseados em tags e palavras-chave",
                "contextual_paths": "Caminhos pré-definidos para aprendizado",
                "quick_access": "Acesso rápido a documentos populares",
                "search_index": "Índice de busca por título, tags e categorias",
                "breadcrumbs": "Navegação hierárquica",
                "related_documents": "Documentos relacionados por similaridade"
            },
            "statistics": {
                "popular_documents": len(self.intelligent_nav["quick_access"].get("popular_documents", [])),
                "api_references": len(self.intelligent_nav["quick_access"].get("api_references", [])),
                "tutorials": len(self.intelligent_nav["quick_access"].get("tutorials", [])),
                "essential_guides": len(self.intelligent_nav["quick_access"].get("essential_guides", []))
            }
        }
        
        report_file = self.consolidated_dir / "intelligent_navigation_report.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        logger.info(f"✅ Relatório salvo em: {report_file}")
        return str(report_file)
    
    def save_intelligent_navigation(self):
        """
        Salva o sistema de navegação inteligente.
        """
        logger.info("💾 Salvando sistema de navegação inteligente...")
        
        with open(self.intelligent_nav_file, 'w', encoding='utf-8') as f:
            json.dump(self.intelligent_nav, f, indent=2, ensure_ascii=False)
        
        logger.info(f"✅ Sistema salvo em: {self.intelligent_nav_file}")
    
    def optimize_navigation(self) -> Dict[str, Any]:
        """
        Executa otimização completa da navegação.
        
        Returns:
            Resultados da otimização
        """
        logger.info("🚀 Iniciando otimização de navegação inteligente...")
        
        # Construir grafo de navegação
        self.build_navigation_graph()
        
        # Criar links semânticos
        self.create_semantic_links()
        
        # Criar caminhos contextuais
        self.create_contextual_paths()
        
        # Criar acesso rápido
        self.create_quick_access()
        
        # Criar índice de busca
        self.create_search_index()
        
        # Criar breadcrumbs
        self.create_breadcrumbs()
        
        # Criar documentos relacionados
        self.create_related_documents()
        
        # Salvar sistema
        self.save_intelligent_navigation()
        
        # Gerar relatório
        report_path = self.generate_navigation_report()
        
        results = {
            "success": True,
            "documents_analyzed": self.navigation_data.get("total_documents", 0),
            "navigation_graph_nodes": len(self.intelligent_nav["navigation_graph"]),
            "semantic_links_created": len(self.intelligent_nav["semantic_links"].get("by_tags", {})),
            "contextual_paths": len(self.intelligent_nav["contextual_paths"]),
            "search_index_entries": len(self.intelligent_nav["search_index"].get("by_title", {})),
            "report_path": report_path
        }
        
        logger.info("✅ Otimização de navegação concluída!")
        return results

def main():
    """Função principal do script."""
    print("🔄 Iniciando sistema de navegação inteligente...")
    
    nav_system = IntelligentNavigationSystem()
    
    # Executar otimização
    results = nav_system.optimize_navigation()
    
    print(f"\n✅ Navegação inteligente otimizada!")
    print(f"📊 Documentos analisados: {results['documents_analyzed']}")
    print(f"🕸️ Nós no grafo de navegação: {results['navigation_graph_nodes']}")
    print(f"🔗 Links semânticos criados: {results['semantic_links_created']}")
    print(f"🛤️ Caminhos contextuais: {results['contextual_paths']}")
    print(f"🔍 Entradas no índice de busca: {results['search_index_entries']}")
    print(f"📁 Relatório: {results['report_path']}")

if __name__ == "__main__":
    main() 