#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agente de Navegação por Grafos
Implementa navegação inteligente usando grafos para otimizar consultas JSON
"""

import json
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple, Set
from collections import defaultdict, deque
import heapq
import networkx as nx
from dataclasses import dataclass

@dataclass
class GraphNode:
    """Nó do grafo de navegação"""
    id: str
    type: str  # 'document', 'tag', 'category', 'file', 'function'
    path: str
    metadata: Dict[str, Any]
    weight: float = 1.0
    last_accessed: Optional[str] = None

@dataclass
class GraphEdge:
    """Aresta do grafo de navegação"""
    source: str
    target: str
    relationship: str  # 'references', 'depends_on', 'similar', 'tagged_with'
    weight: float = 1.0
    metadata: Dict[str, Any] = None

class GraphNavigationAgent:
    """Agente especializado em navegação por grafos"""
    
    def __init__(self):
        self.project_root = Path(".")
        self.maps_path = self.project_root / "wiki" / "maps"
        self.graph_file = self.maps_path / "navigation_graph.json"
        
        # Grafo principal de navegação
        self.graph = nx.DiGraph()
        
        # Cache de navegação
        self.navigation_cache = {}
        self.path_cache = {}
        
        # Métricas de performance
        self.metrics = {
            "queries_processed": 0,
            "cache_hits": 0,
            "average_path_length": 0.0,
            "response_times": []
        }
        
        # Carregar ou criar grafo
        self.load_or_create_graph()
    
    def load_or_create_graph(self):
        """Carrega grafo existente ou cria novo"""
        if self.graph_file.exists():
            print("📊 Carregando grafo de navegação existente...")
            self.load_graph()
        else:
            print("🔄 Criando novo grafo de navegação...")
            self.build_graph()
            self.save_graph()
    
    def build_graph(self):
        """Constrói grafo de navegação a partir dos mapas JSON"""
        print("🔨 Construindo grafo de navegação...")
        
        # Carregar mapas JSON
        maps_data = self.load_all_maps()
        
        # Adicionar nós do grafo
        self.add_document_nodes(maps_data)
        self.add_tag_nodes(maps_data)
        self.add_category_nodes(maps_data)
        self.add_function_nodes(maps_data)
        
        # Adicionar arestas do grafo
        self.add_document_relationships(maps_data)
        self.add_tag_relationships(maps_data)
        self.add_category_relationships(maps_data)
        self.add_function_relationships(maps_data)
        
        # Otimizar grafo
        self.optimize_graph()
        
        print(f"✅ Grafo construído: {self.graph.number_of_nodes()} nós, {self.graph.number_of_edges()} arestas")
    
    def load_all_maps(self) -> Dict[str, Any]:
        """Carrega todos os mapas JSON"""
        maps_data = {}
        
        map_files = {
            "tags_index": "tags_index.json",
            "wiki_map": "wiki_map.json", 
            "relationships": "relationships.json",
            "otclient_source": "otclient_source_index.json",
            "enhanced_context": "enhanced_context_system.json",
            "intelligent_navigation": "intelligent_navigation.json"
        }
        
        for map_name, filename in map_files.items():
            map_path = self.maps_path / filename
            if map_path.exists():
                try:
                    with open(map_path, 'r', encoding='utf-8') as f:
                        maps_data[map_name] = json.load(f)
                except Exception as e:
                    print(f"⚠️ Erro ao carregar {filename}: {e}")
        
        return maps_data
    
    def add_document_nodes(self, maps_data: Dict[str, Any]):
        """Adiciona nós de documentos ao grafo"""
        # Adicionar documentos da wiki
        if "wiki_map" in maps_data:
            wiki_data = maps_data["wiki_map"]
            for category, cat_info in wiki_data.get("categories", {}).items():
                for doc in cat_info.get("documents", []):
                    node_id = f"doc_{doc.get('id', doc.get('file', ''))}"
                    self.graph.add_node(node_id, 
                        type="document",
                        path=f"wiki/otclient/{doc.get('file', '')}",
                        metadata={
                            "title": doc.get("title", ""),
                            "category": category,
                            "status": doc.get("status", ""),
                            "tags": doc.get("tags", [])
                        }
                    )
        
        # Adicionar arquivos do código-fonte
        if "otclient_source" in maps_data:
            source_data = maps_data["otclient_source"]
            for category, cat_info in source_data.get("categories", {}).items():
                for file_info in cat_info.get("files", []):
                    node_id = f"file_{file_info.get('path', '').replace('/', '_')}"
                    self.graph.add_node(node_id,
                        type="file",
                        path=file_info.get("path", ""),
                        metadata={
                            "name": file_info.get("name", ""),
                            "category": category,
                            "functions": file_info.get("functions", []),
                            "classes": file_info.get("classes", [])
                        }
                    )
    
    def add_tag_nodes(self, maps_data: Dict[str, Any]):
        """Adiciona nós de tags ao grafo"""
        if "tags_index" in maps_data:
            tags_data = maps_data["tags_index"]
            for tag in tags_data.get("files_by_tag", {}).keys():
                node_id = f"tag_{tag}"
                self.graph.add_node(node_id,
                    type="tag",
                    path=f"tag:{tag}",
                    metadata={
                        "tag_name": tag,
                        "file_count": len(tags_data["files_by_tag"][tag])
                    }
                )
    
    def add_category_nodes(self, maps_data: Dict[str, Any]):
        """Adiciona nós de categorias ao grafo"""
        if "wiki_map" in maps_data:
            wiki_data = maps_data["wiki_map"]
            for category in wiki_data.get("categories", {}).keys():
                node_id = f"cat_{category}"
                self.graph.add_node(node_id,
                    type="category",
                    path=f"category:{category}",
                    metadata={
                        "category_name": category,
                        "document_count": len(wiki_data["categories"][category].get("documents", []))
                    }
                )
    
    def add_function_nodes(self, maps_data: Dict[str, Any]):
        """Adiciona nós de funções ao grafo"""
        if "otclient_source" in maps_data:
            source_data = maps_data["otclient_source"]
            for category, cat_info in source_data.get("categories", {}).items():
                for file_info in cat_info.get("files", []):
                    for func in file_info.get("functions", []):
                        node_id = f"func_{func}_{file_info.get('path', '').replace('/', '_')}"
                        self.graph.add_node(node_id,
                            type="function",
                            path=f"{file_info.get('path', '')}#{func}",
                            metadata={
                                "function_name": func,
                                "file_path": file_info.get("path", ""),
                                "category": category
                            }
                        )
    
    def add_document_relationships(self, maps_data: Dict[str, Any]):
        """Adiciona relacionamentos entre documentos"""
        if "relationships" in maps_data:
            rel_data = maps_data["relationships"]
            for rel in rel_data.get("relationships", []):
                source_id = f"doc_{rel.get('source', '')}"
                target_id = f"doc_{rel.get('target', '')}"
                
                if source_id in self.graph and target_id in self.graph:
                    self.graph.add_edge(source_id, target_id,
                        relationship="references",
                        weight=rel.get("strength", 1.0),
                        metadata=rel.get("metadata", {})
                    )
    
    def add_tag_relationships(self, maps_data: Dict[str, Any]):
        """Adiciona relacionamentos de tags"""
        if "tags_index" in maps_data:
            tags_data = maps_data["tags_index"]
            
            # Conectar documentos às suas tags
            for tag, files in tags_data.get("files_by_tag", {}).items():
                tag_id = f"tag_{tag}"
                
                for file_name in files:
                    doc_id = f"doc_{file_name}"
                    if doc_id in self.graph:
                        self.graph.add_edge(doc_id, tag_id,
                            relationship="tagged_with",
                            weight=1.0
                        )
                        self.graph.add_edge(tag_id, doc_id,
                            relationship="contains",
                            weight=1.0
                        )
    
    def add_category_relationships(self, maps_data: Dict[str, Any]):
        """Adiciona relacionamentos de categorias"""
        if "wiki_map" in maps_data:
            wiki_data = maps_data["wiki_map"]
            
            for category, cat_info in wiki_data.get("categories", {}).items():
                cat_id = f"cat_{category}"
                
                for doc in cat_info.get("documents", []):
                    doc_id = f"doc_{doc.get('id', doc.get('file', ''))}"
                    if doc_id in self.graph:
                        self.graph.add_edge(doc_id, cat_id,
                            relationship="belongs_to",
                            weight=1.0
                        )
                        self.graph.add_edge(cat_id, doc_id,
                            relationship="contains",
                            weight=1.0
                        )
    
    def add_function_relationships(self, maps_data: Dict[str, Any]):
        """Adiciona relacionamentos de funções"""
        if "otclient_source" in maps_data:
            source_data = maps_data["otclient_source"]
            
            for category, cat_info in source_data.get("categories", {}).items():
                for file_info in cat_info.get("files", []):
                    file_id = f"file_{file_info.get('path', '').replace('/', '_')}"
                    
                    for func in file_info.get("functions", []):
                        func_id = f"func_{func}_{file_info.get('path', '').replace('/', '_')}"
                        
                        if file_id in self.graph and func_id in self.graph:
                            self.graph.add_edge(file_id, func_id,
                                relationship="contains",
                                weight=1.0
                            )
                            self.graph.add_edge(func_id, file_id,
                                relationship="defined_in",
                                weight=1.0
                            )
    
    def optimize_graph(self):
        """Otimiza o grafo para melhor performance"""
        print("⚡ Otimizando grafo...")
        
        # Calcular centralidade
        centrality = nx.pagerank(self.graph)
        
        # Atualizar pesos dos nós baseado na centralidade
        for node, centrality_score in centrality.items():
            if node in self.graph:
                self.graph.nodes[node]["centrality"] = centrality_score
                self.graph.nodes[node]["weight"] = centrality_score
        
        # Identificar comunidades
        communities = list(nx.community.greedy_modularity_communities(self.graph.to_undirected()))
        
        # Adicionar informações de comunidade aos nós
        for i, community in enumerate(communities):
            for node in community:
                if node in self.graph:
                    self.graph.nodes[node]["community"] = i
        
        print(f"✅ Grafo otimizado: {len(communities)} comunidades identificadas")
    
    def find_optimal_path(self, source: str, target: str, 
                         context: Optional[str] = None) -> List[str]:
        """Encontra caminho ótimo entre dois nós"""
        start_time = time.time()
        
        # Verificar cache
        cache_key = f"{source}_{target}_{context}"
        if cache_key in self.path_cache:
            self.metrics["cache_hits"] += 1
            return self.path_cache[cache_key]
        
        # Encontrar nós correspondentes
        source_nodes = self.find_nodes_by_query(source)
        target_nodes = self.find_nodes_by_query(target)
        
        if not source_nodes or not target_nodes:
            return []
        
        # Encontrar caminho mais curto
        best_path = []
        best_weight = float('inf')
        
        for s_node in source_nodes:
            for t_node in target_nodes:
                try:
                    path = nx.shortest_path(self.graph, s_node, t_node, weight='weight')
                    path_weight = sum(self.graph[path[i]][path[i+1]]['weight'] 
                                    for i in range(len(path)-1))
                    
                    if path_weight < best_weight:
                        best_weight = path_weight
                        best_path = path
                        
                except nx.NetworkXNoPath:
                    continue
        
        # Aplicar contexto se especificado
        if context and best_path:
            best_path = self.apply_context_filter(best_path, context)
        
        # Cache do resultado
        self.path_cache[cache_key] = best_path
        
        # Atualizar métricas
        execution_time = time.time() - start_time
        self.metrics["response_times"].append(execution_time)
        self.metrics["queries_processed"] += 1
        
        return best_path
    
    def find_nodes_by_query(self, query: str) -> List[str]:
        """Encontra nós baseado em uma consulta"""
        nodes = []
        
        # Busca por ID exato
        if query in self.graph:
            nodes.append(query)
        
        # Busca por tipo
        if query.startswith("type:"):
            node_type = query.split(":", 1)[1]
            for node, attrs in self.graph.nodes(data=True):
                if attrs.get("type") == node_type:
                    nodes.append(node)
        
        # Busca por tag
        if query.startswith("tag:"):
            tag_name = query.split(":", 1)[1]
            tag_id = f"tag_{tag_name}"
            if tag_id in self.graph:
                nodes.append(tag_id)
        
        # Busca por categoria
        if query.startswith("category:"):
            cat_name = query.split(":", 1)[1]
            cat_id = f"cat_{cat_name}"
            if cat_id in self.graph:
                nodes.append(cat_id)
        
        # Busca por texto
        for node, attrs in self.graph.nodes(data=True):
            metadata = attrs.get("metadata", {})
            
            # Buscar em título
            if "title" in metadata and query.lower() in metadata["title"].lower():
                nodes.append(node)
            
            # Buscar em tags
            if "tags" in metadata:
                for tag in metadata["tags"]:
                    if query.lower() in tag.lower():
                        nodes.append(node)
        
        return list(set(nodes))
    
    def apply_context_filter(self, path: List[str], context: str) -> List[str]:
        """Aplica filtro de contexto ao caminho"""
        if context == "documentation":
            return [node for node in path if self.graph.nodes[node].get("type") == "document"]
        elif context == "code":
            return [node for node in path if self.graph.nodes[node].get("type") in ["file", "function"]]
        elif context == "tags":
            return [node for node in path if self.graph.nodes[node].get("type") == "tag"]
        
        return path
    
    def get_related_nodes(self, node_id: str, max_distance: int = 2) -> List[Tuple[str, float]]:
        """Encontra nós relacionados"""
        if node_id not in self.graph:
            return []
        
        related = []
        visited = set()
        queue = deque([(node_id, 0)])
        
        while queue:
            current, distance = queue.popleft()
            
            if current in visited or distance > max_distance:
                continue
            
            visited.add(current)
            
            if current != node_id:
                # Calcular similaridade baseada na distância e centralidade
                centrality = self.graph.nodes[current].get("centrality", 0.0)
                similarity = 1.0 / (distance + 1) * centrality
                related.append((current, similarity))
            
            # Adicionar vizinhos
            for neighbor in self.graph.neighbors(current):
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))
        
        # Ordenar por similaridade
        related.sort(key=lambda x: x[1], reverse=True)
        return related[:10]  # Retornar top 10
    
    def get_navigation_suggestions(self, current_node: str, 
                                 context: Optional[str] = None) -> List[Dict[str, Any]]:
        """Gera sugestões de navegação"""
        suggestions = []
        
        # Encontrar nós relacionados
        related = self.get_related_nodes(current_node)
        
        for node_id, similarity in related:
            node_data = self.graph.nodes[node_id]
            
            # Filtrar por contexto se especificado
            if context and node_data.get("type") != context:
                continue
            
            suggestion = {
                "node_id": node_id,
                "type": node_data.get("type"),
                "path": node_data.get("path"),
                "similarity": similarity,
                "metadata": node_data.get("metadata", {})
            }
            
            suggestions.append(suggestion)
        
        return suggestions
    
    def save_graph(self):
        """Salva grafo em formato JSON"""
        graph_data = {
            "metadata": {
                "version": "1.0",
                "last_updated": datetime.now().isoformat(),
                "nodes_count": self.graph.number_of_nodes(),
                "edges_count": self.graph.number_of_edges()
            },
            "nodes": {},
            "edges": []
        }
        
        # Salvar nós
        for node, attrs in self.graph.nodes(data=True):
            graph_data["nodes"][node] = attrs
        
        # Salvar arestas
        for source, target, attrs in self.graph.edges(data=True):
            graph_data["edges"].append({
                "source": source,
                "target": target,
                **attrs
            })
        
        with open(self.graph_file, 'w', encoding='utf-8') as f:
            json.dump(graph_data, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Grafo salvo em {self.graph_file}")
    
    def load_graph(self):
        """Carrega grafo do arquivo JSON"""
        try:
            with open(self.graph_file, 'r', encoding='utf-8') as f:
                graph_data = json.load(f)
            
            # Recriar grafo
            self.graph.clear()
            
            # Adicionar nós
            for node_id, attrs in graph_data["nodes"].items():
                self.graph.add_node(node_id, **attrs)
            
            # Adicionar arestas
            for edge in graph_data["edges"]:
                source = edge.pop("source")
                target = edge.pop("target")
                self.graph.add_edge(source, target, **edge)
            
            print(f"📊 Grafo carregado: {self.graph.number_of_nodes()} nós, {self.graph.number_of_edges()} arestas")
            
        except Exception as e:
            print(f"❌ Erro ao carregar grafo: {e}")
            self.build_graph()
    
    def get_performance_metrics(self) -> Dict[str, Any]:
        """Retorna métricas de performance"""
        avg_response_time = (sum(self.metrics["response_times"]) / 
                           len(self.metrics["response_times"])) if self.metrics["response_times"] else 0
        
        cache_hit_rate = (self.metrics["cache_hits"] / 
                         self.metrics["queries_processed"]) if self.metrics["queries_processed"] > 0 else 0
        
        return {
            "queries_processed": self.metrics["queries_processed"],
            "cache_hits": self.metrics["cache_hits"],
            "cache_hit_rate": cache_hit_rate,
            "average_response_time": avg_response_time,
            "graph_nodes": self.graph.number_of_nodes(),
            "graph_edges": self.graph.number_of_edges()
        }

def main():
    """Função principal para teste do agente"""
    agent = GraphNavigationAgent()
    
    print("🚀 Agente de Navegação por Grafos iniciado")
    print("=" * 50)
    
    # Teste de navegação
    print("\n🧭 Teste de Navegação:")
    
    # Exemplo: encontrar caminho entre UI e Lua
    path = agent.find_optimal_path("UI", "Lua", context="documentation")
    print(f"Caminho UI → Lua: {path}")
    
    # Exemplo: sugestões para documento atual
    suggestions = agent.get_navigation_suggestions("doc_UI_System_Guide.md", context="documentation")
    print(f"\n💡 Sugestões para UI_System_Guide.md:")
    for suggestion in suggestions[:5]:
        print(f"  - {suggestion['metadata'].get('title', suggestion['node_id'])} (similaridade: {suggestion['similarity']:.2f})")
    
    # Métricas de performance
    metrics = agent.get_performance_metrics()
    print(f"\n📊 Métricas de Performance:")
    print(f"  Queries processadas: {metrics['queries_processed']}")
    print(f"  Cache hit rate: {metrics['cache_hit_rate']:.2%}")
    print(f"  Tempo médio de resposta: {metrics['average_response_time']:.3f}s")
    print(f"  Nós no grafo: {metrics['graph_nodes']}")
    print(f"  Arestas no grafo: {metrics['graph_edges']}")

if __name__ == "__main__":
    main() 