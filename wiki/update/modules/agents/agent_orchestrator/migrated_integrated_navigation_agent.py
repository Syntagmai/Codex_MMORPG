from unicode_aliases import *
# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
MAX_ITEMS = 100
MAX_SIZE = 1000
TIMEOUT_SECONDS = 60

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: integrated_navigation_agent.py
Módulo de Destino: agents.agent_orchestrator
Data de Migração: 2025-08-01 12:21:43

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import AgentorchestratorModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agente de Navegação Integrada
Combina navegação JSON tradicional com navegação por grafos
"""

import json
import time
from datetime import datetime

class IntegratedNavigationAgent:
    """Agente que integra navegação JSON e grafos"""
    
    def __init__(self):
        self.project_root = Path(".")
        self.maps_path = self.project_root / "wiki" / "maps"
        
        # Agentes especializados
        self.json_agent = JSONNavigationAgent()
        self.graph_agent = GraphNavigationAgent()
        
        # Cache integrado
        self.integrated_cache = {}
        
        # Métricas de performance
        self.metrics = {
            "json_queries": 0,
            "graph_queries": 0,
            "hybrid_queries": 0,
            "average_response_time": 0.0,
            "cache_hits": 0
        }
    
    def navigate(self, query: str, context: Optional[str] = None, 
                strategy: str = "hybrid") -> Dict[str, Any]:
        """
        Navegação integrada com múltiplas estratégias
        
        Estratégias:
        - 'json': Navegação JSON tradicional
        - 'graph': Navegação por grafos
        - 'hybrid': Combinação inteligente
        """
        start_time = time.time()
        
        # Verificar cache
        cache_key = f"{query}_{context}_{strategy}"
        if cache_key in self.integrated_cache:
            self.metrics["cache_hits"] += 1
            return self.integrated_cache[cache_key]
        
        result = {
            "query": query,
            "context": context,
            "strategy": strategy,
            "timestamp": datetime.now().isoformat(),
            "results": {},
            "suggestions": [],
            "performance": {}
        }
        
        if strategy == "json":
            result["results"] = self.json_navigation(query, context)
            self.metrics["json_queries"] += 1
            
        elif strategy == "graph":
            result["results"] = self.graph_navigation(query, context)
            self.metrics["graph_queries"] += 1
            
        elif strategy == "hybrid":
            result["results"] = self.hybrid_navigation(query, context)
            self.metrics["hybrid_queries"] += 1
        
        # Gerar sugestões
        result["suggestions"] = self.generate_suggestions(query, context, result["results"])
        
        # Métricas de performance
        execution_time = time.time() - start_time
        result["performance"] = {
            "execution_time": execution_time,
            "strategy_used": strategy,
            "cache_hit": False
        }
        
        # Cache do resultado
        self.integrated_cache[cache_key] = result
        
        return result
    
    def json_navigation(self, query: str, context: Optional[str] = None) -> Dict[str, Any]:
        """Navegação JSON tradicional"""
        results = {
            "method": "json",
            "files_found": [],
            "tags_found": [],
            "categories_found": [],
            "relationships": []
        }
        
        # Buscar em tags_index.json
        tags_file = self.maps_path / "tags_index.json"
        if tags_file.exists():
            with open(tags_file, 'r', encoding='utf-8') as f:
                tags_data = json.load(f)
            
            # Buscar por tag
            for tag, files in tags_data.get("files_by_tag", {}).items():
                if query.lower() in tag.lower():
                    results["tags_found"].append(tag)
                    results["files_found"].extend(files)
            
            # Buscar por arquivo
            for file_name, tags in tags_data.get("tags_by_file", {}).items():
                if query.lower() in file_name.lower():
                    results["files_found"].append(file_name)
        
        # Buscar em wiki_map.json
        wiki_map_file = self.maps_path / "wiki_map.json"
        if wiki_map_file.exists():
            with open(wiki_map_file, 'r', encoding='utf-8') as f:
                wiki_data = json.load(f)
            
            for category, cat_info in wiki_data.get("categories", {}).items():
                if query.lower() in category.lower():
                    results["categories_found"].append(category)
                
                for doc in cat_info.get("documents", []):
                    if query.lower() in doc.get("title", "").lower():
                        results["files_found"].append(doc.get("file", ""))
        
        return results
    
    def graph_navigation(self, query: str, context: Optional[str] = None) -> Dict[str, Any]:
        """Navegação por grafos"""
        results = {
            "method": "graph",
            "optimal_paths": [],
            "related_nodes": [],
            "centrality_scores": {},
            "communities": []
        }
        
        # Encontrar nós relacionados
        related_nodes = self.graph_agent.get_related_nodes(query, max_distance=2)
        
        for node_id, similarity in related_nodes:
            node_data = self.graph_agent.graph.nodes[node_id]
            results["related_nodes"].append({
                "node_id": node_id,
                "type": node_data.get("type"),
                "path": node_data.get("path"),
                "similarity": similarity,
                "metadata": node_data.get("metadata", {})
            })
        
        # Encontrar caminhos ótimos para nós importantes
        if related_nodes:
            target_node = related_nodes[0][0]  # Nó mais similar
            optimal_path = self.graph_agent.find_optimal_path(query, target_node, context)
            results["optimal_paths"].append({
                "source": query,
                "target": target_node,
                "path": optimal_path,
                "context": context
            })
        
        return results
    
    def hybrid_navigation(self, query: str, context: Optional[str] = None) -> Dict[str, Any]:
        """Navegação híbrida - combina JSON e grafos"""
        results = {
            "method": "hybrid",
            "json_results": {},
            "graph_results": {},
            "integrated_results": [],
            "confidence_scores": {}
        }
        
        # Executar navegação JSON
        json_results = self.json_navigation(query, context)
        results["json_results"] = json_results
        
        # Executar navegação por grafos
        graph_results = self.graph_navigation(query, context)
        results["graph_results"] = graph_results
        
        # Integrar resultados
        integrated = self.integrate_results(json_results, graph_results, context)
        results["integrated_results"] = integrated
        
        # Calcular scores de confiança
        results["confidence_scores"] = self.calculate_confidence_scores(integrated)
        
        return results
    
    def integrate_results(self, json_results: Dict[str, Any], 
                         graph_results: Dict[str, Any], 
                         context: Optional[str] = None) -> List[Dict[str, Any]]:
        """Integra resultados de JSON e grafos"""
        integrated = []
        
        # Mapear arquivos encontrados via JSON
        json_files = set(json_results.get("files_found", []))
        
        # Mapear nós encontrados via grafos
        graph_nodes = {}
        for node_info in graph_results.get("related_nodes", []):
            node_id = node_info["node_id"]
            if node_info["type"] == "document":
                # Extrair nome do arquivo do path
                path = node_info["path"]
                if path.startswith("wiki/otclient/"):
                    file_name = path.split("/")[-1]
                    graph_nodes[file_name] = node_info
        
        # Combinar resultados
        for file_name in json_files:
            confidence = 1.0  # Base JSON
            
            # Verificar se também encontrado via grafos
            if file_name in graph_nodes:
                graph_info = graph_nodes[file_name]
                confidence += graph_info["similarity"] * 0.5  # Bonus por grafos
            
            integrated.append({
                "file_name": file_name,
                "confidence": confidence,
                "sources": ["json"] + (["graph"] if file_name in graph_nodes else []),
                "metadata": graph_nodes.get(file_name, {}).get("metadata", {})
            })
        
        # Adicionar resultados apenas do grafo (alta similaridade)
        for node_info in graph_results.get("related_nodes", []):
            if node_info["similarity"] > 0.7:  # Alta similaridade
                path = node_info["path"]
                if path.startswith("wiki/otclient/"):
                    file_name = path.split("/")[-1]
                    
                    if file_name not in json_files:  # Não encontrado via JSON
                        integrated.append({
                            "file_name": file_name,
                            "confidence": node_info["similarity"],
                            "sources": ["graph"],
                            "metadata": node_info["metadata"]
                        })
        
        # Ordenar por confiança
        integrated.sort(key=lambda x: x["confidence"], reverse=True)
        
        return integrated
    
    def calculate_confidence_scores(self, integrated_results: List[Dict[str, Any]]) -> Dict[str, float]:
        """Calcula scores de confiança para os resultados"""
        scores = {
            "overall_confidence": 0.0,
            "json_confidence": 0.0,
            "graph_confidence": 0.0,
            "hybrid_confidence": 0.0
        }
        
        if not integrated_results:
            return scores
        
        # Calcular confiança geral
        total_confidence = sum(result["confidence"] for result in integrated_results)
        scores["overall_confidence"] = total_confidence / len(integrated_results)
        
        # Calcular confiança por fonte
        json_results = [r for r in integrated_results if "json" in r["sources"]]
        graph_results = [r for r in integrated_results if "graph" in r["sources"]]
        hybrid_results = [r for r in integrated_results if len(r["sources"]) > 1]
        
        if json_results:
            scores["json_confidence"] = sum(r["confidence"] for r in json_results) / len(json_results)
        
        if graph_results:
            scores["graph_confidence"] = sum(r["confidence"] for r in graph_results) / len(graph_results)
        
        if hybrid_results:
            scores["hybrid_confidence"] = sum(r["confidence"] for r in hybrid_results) / len(hybrid_results)
        
        return scores
    
    def generate_suggestions(self, query: str, context: Optional[str], 
                           results: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Gera sugestões de navegação"""
        suggestions = []
        
        # Sugestões baseadas nos resultados
        if "integrated_results" in results:
            for result in results["integrated_results"][:5]:  # Top 5
                suggestions.append({
                    "type": "related_document",
                    "title": result["metadata"].get("title", result["file_name"]),
                    "path": f"wiki/otclient/{result['file_name']}",
                    "confidence": result["confidence"],
                    "reason": f"Encontrado via {' + '.join(result['sources'])}"
                })
        
        # Sugestões baseadas no contexto
        if context == "documentation":
            suggestions.extend([
                {
                    "type": "navigation",
                    "title": "Buscar por tags relacionadas",
                    "action": f"tag:{query}",
                    "reason": "Explorar documentos com tags similares"
                },
                {
                    "type": "navigation", 
                    "title": "Ver categorias relacionadas",
                    "action": f"category:{query}",
                    "reason": "Explorar categorias similares"
                }
            ])
        
        elif context == "code":
            suggestions.extend([
                {
                    "type": "navigation",
                    "title": "Buscar funções relacionadas",
                    "action": f"function:{query}",
                    "reason": "Encontrar funções similares no código"
                },
                {
                    "type": "navigation",
                    "title": "Ver arquivos relacionados",
                    "action": f"file:{query}",
                    "reason": "Explorar arquivos de código similares"
                }
            ])
        
        return suggestions
    
    def get_performance_report(self) -> Dict[str, Any]:
        """Gera relatório de performance"""
        total_queries = (self.metrics["json_queries"] + 
                        self.metrics["graph_queries"] + 
                        self.metrics["hybrid_queries"])
        
        cache_hit_rate = (self.metrics["cache_hits"] / total_queries 
                         if total_queries > 0 else 0)
        
        return {
            "timestamp": datetime.now().isoformat(),
            "total_queries": total_queries,
            "json_queries": self.metrics["json_queries"],
            "graph_queries": self.metrics["graph_queries"],
            "hybrid_queries": self.metrics["hybrid_queries"],
            "cache_hits": self.metrics["cache_hits"],
            "cache_hit_rate": cache_hit_rate,
            "average_response_time": self.metrics["average_response_time"],
            "json_agent_metrics": self.json_agent.get_performance_metrics(),
            "graph_agent_metrics": self.graph_agent.get_performance_metrics()
        }
    
    def optimize_navigation(self) -> Dict[str, Any]:
        """Otimiza a navegação integrada"""
        print("⚡ Otimizando navegação integrada...")
        
        optimization_result = {
            "timestamp": datetime.now().isoformat(),
            "optimizations_applied": [],
            "performance_improvements": [],
            "cache_optimizations": []
        }
        
        # Otimizar cache
        if len(self.integrated_cache) > 1000:
            # Limpar cache antigo
            old_cache = self.integrated_cache.copy()
            self.integrated_cache.clear()
            
            # Manter apenas resultados recentes
            for key, value in old_cache.items():
                if "timestamp" in value:
                    cache_time = datetime.fromisoformat(value["timestamp"])
                    if (datetime.now() - cache_time).total_seconds() < 3600:  # 1 hora
                        self.integrated_cache[key] = value
            
            optimization_result["cache_optimizations"].append(f"Cache limpo: {len(old_cache)} → {len(self.integrated_cache)} entradas")
        
        # Otimizar agentes
        json_opt = self.json_agent.optimize_navigation_performance()
        graph_opt = self.graph_agent.optimize_graph()
        
        optimization_result["optimizations_applied"].extend([
            "Cache integrado otimizado",
            "Agente JSON otimizado",
            "Grafo de navegação otimizado"
        ])
        
        return optimization_result

def main():
    """Função principal para teste do agente integrado"""
    agent = IntegratedNavigationAgent()
    
    print("🚀 Agente de Navegação Integrada iniciado")
    print("=" * 50)
    
    # Teste de navegação híbrida
    print("\n🧭 Teste de Navegação Híbrida:")
    
    # Exemplo: buscar por UI
    result = agent.navigate("UI", context="documentation", strategy="hybrid")
    
    print(f"Query: {result['query']}")
    print(f"Estratégia: {result['strategy']}")
    print(f"Tempo de execução: {result['performance']['execution_time']:.3f}s")
    
    print(f"\n📄 Resultados encontrados: {len(result['results'].get('integrated_results', []))}")
    
    for i, item in enumerate(result['results'].get('integrated_results', [])[:3]):
        print(f"  {i+1}. {item['file_name']} (confiança: {item['confidence']:.2f})")
    
    print(f"\n💡 Sugestões:")
    for suggestion in result['suggestions'][:3]:
        print(f"  - {suggestion['title']}: {suggestion['reason']}")
    
    # Relatório de performance
    report = agent.get_performance_report()
    print(f"\n📊 Relatório de Performance:")
    print(f"  Total de queries: {report['total_queries']}")
    print(f"  Cache hit rate: {report['cache_hit_rate']:.2%}")
    print(f"  Queries JSON: {report['json_queries']}")
    print(f"  Queries Graph: {report['graph_queries']}")
    print(f"  Queries Hybrid: {report['hybrid_queries']}")

if __name__ == "__main__":
    main() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = AgentorchestratorModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script integrated_navigation_agent.py executado com sucesso via módulo agents.agent_orchestrator")
    else:
        print(f"❌ Erro na execução do script integrated_navigation_agent.py via módulo agents.agent_orchestrator")

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
- **Nome**: migrated_integrated_navigation_agent
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

