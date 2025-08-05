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
Script Migrado: analyze_navigation_optimization.py
Módulo de Destino: python.code_analyzer
Data de Migração: 2025-08-01 12:21:34

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import CodeanalyzerModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Análise de Otimização de Navegação
Analisa se todos os caminhos referenciados no cursor.md estão otimizados
"""

import json
import time
from datetime import datetime

class NavigationOptimizationAnalyzer:
    def __init__(self):
        self.cursor_file = Path("cursor.md")
        self.maps_path = Path("wiki/maps")
        self.rules_path = Path(".cursor/rules")
        self.wiki_path = Path("wiki")
        
    def analyze_tags_index_optimization(self):
        """Analisa otimização do tags_index.json"""
        print("Analisando otimizacao do tags_index.json...")
        
        tags_file = self.maps_path / "tags_index.json"
        if not tags_file.exists():
            return {"status": "missing", "score": 0}
        
        with open(tags_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        analysis = {
            "status": "exists",
            "metadata": {
                "has_version": "version" in data.get("metadata", {}),
                "has_last_updated": "last_updated" in data.get("metadata", {}),
                "has_total_files": "total_files" in data.get("metadata", {}),
                "has_total_tags": "total_tags" in data.get("metadata", {})
            },
            "structure": {
                "has_files_by_tag": "files_by_tag" in data,
                "has_tags_by_file": "tags_by_file" in data,
                "tag_count": len(data.get("files_by_tag", {})),
                "file_count": len(data.get("tags_by_file", {}))
            },
            "optimization": {
                "has_quick_access": "quick_access" in data,
                "has_search_index": "search_index" in data,
                "has_performance_metrics": "performance_metrics" in data
            }
        }
        
        # Calcular score
        score = 0
        if analysis["status"] == "exists":
            score += 20  # Arquivo existe
            if analysis["metadata"]["has_version"]: score += 10
            if analysis["metadata"]["has_last_updated"]: score += 10
            if analysis["metadata"]["has_total_files"]: score += 10
            if analysis["metadata"]["has_total_tags"]: score += 10
            if analysis["structure"]["has_files_by_tag"]: score += 15
            if analysis["structure"]["has_tags_by_file"]: score += 15
            if analysis["optimization"]["has_quick_access"]: score += 5
            if analysis["optimization"]["has_search_index"]: score += 3
            if analysis["optimization"]["has_performance_metrics"]: score += 2
        
        analysis["score"] = score
        return analysis
    
    def analyze_wiki_map_optimization(self):
        """Analisa otimização do wiki_map.json"""
        print("Analisando otimizacao do wiki_map.json...")
        
        wiki_map_file = self.maps_path / "wiki_map.json"
        if not wiki_map_file.exists():
            return {"status": "missing", "score": 0}
        
        with open(wiki_map_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        analysis = {
            "status": "exists",
            "metadata": {
                "has_version": "version" in data.get("metadata", {}),
                "has_last_updated": "last_updated" in data.get("metadata", {}),
                "has_total_documents": "total_documents" in data.get("metadata", {}),
                "has_context": "context" in data.get("metadata", {})
            },
            "structure": {
                "has_categories": "categories" in data,
                "has_files": "files" in data,
                "category_count": len(data.get("categories", {})),
                "file_count": len(data.get("files", {}))
            },
            "optimization": {
                "has_navigation_paths": "navigation_paths" in data,
                "has_quick_access": "quick_access" in data,
                "has_performance_metrics": "performance_metrics" in data
            }
        }
        
        # Calcular score
        score = 0
        if analysis["status"] == "exists":
            score += 20  # Arquivo existe
            if analysis["metadata"]["has_version"]: score += 10
            if analysis["metadata"]["has_last_updated"]: score += 10
            if analysis["metadata"]["has_total_documents"]: score += 10
            if analysis["metadata"]["has_context"]: score += 10
            if analysis["structure"]["has_categories"]: score += 15
            if analysis["structure"]["has_files"]: score += 15
            if analysis["optimization"]["has_navigation_paths"]: score += 5
            if analysis["optimization"]["has_quick_access"]: score += 3
            if analysis["optimization"]["has_performance_metrics"]: score += 2
        
        analysis["score"] = score
        return analysis
    
    def analyze_rules_optimization(self):
        """Analisa otimização das regras"""
        print("Analisando otimizacao das regras...")
        
        rules_analysis = {}
        total_score = 0
        total_rules = 0
        
        # Verificar regras principais mencionadas no cursor.md
        key_rules = [
            "rules.md",
            "wiki-json-navigation-rules.md",
            "context-aware-rules.md",
            "performance-rules.md",
            "simplification-rules.md"
        ]
        
        for rule_file in key_rules:
            rule_path = self.rules_path / rule_file
            if rule_path.exists():
                with open(rule_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                analysis = {
                    "status": "exists",
                    "size_bytes": len(content),
                    "lines": len(content.split('\n')),
                    "has_structure": "##" in content,
                    "has_examples": "```" in content,
                    "has_checklist": "✅" in content or "❌" in content,
                    "has_performance_info": "performance" in content.lower() or "otimização" in content.lower()
                }
                
                # Calcular score individual
                score = 0
                if analysis["status"] == "exists": score += 20
                if analysis["has_structure"]: score += 20
                if analysis["has_examples"]: score += 20
                if analysis["has_checklist"]: score += 20
                if analysis["has_performance_info"]: score += 20
                
                analysis["score"] = score
                total_score += score
                total_rules += 1
            else:
                analysis = {"status": "missing", "score": 0}
            
            rules_analysis[rule_file] = analysis
        
        return {
            "individual_rules": rules_analysis,
            "average_score": total_score / total_rules if total_rules > 0 else 0,
            "total_rules_analyzed": total_rules
        }
    
    def analyze_enhanced_context_system(self):
        """Analisa otimização do sistema de contexto avançado"""
        print("Analisando sistema de contexto avancado...")
        
        context_file = self.maps_path / "enhanced_context_system.json"
        if not context_file.exists():
            return {"status": "missing", "score": 0}
        
        with open(context_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        context_system = data.get("context_system", {})
        
        analysis = {
            "status": "exists",
            "version": context_system.get("version", "unknown"),
            "components": {
                "has_repository_info": "repository_info" in context_system,
                "has_directory_structure": "directory_structure" in context_system,
                "has_navigation_system": "navigation_system" in context_system,
                "has_performance_optimization": "performance_optimization" in context_system,
                "has_context_detection": "context_detection" in context_system
            },
            "optimization": {
                "has_cache_strategy": "cache_strategy" in context_system.get("performance_optimization", {}),
                "has_search_limits": "search_limits" in context_system.get("performance_optimization", {}),
                "has_lazy_loading": "lazy_loading" in context_system.get("performance_optimization", {}),
                "has_quick_access": "quick_access" in context_system.get("navigation_system", {})
            }
        }
        
        # Calcular score
        score = 0
        if analysis["status"] == "exists":
            score += 20  # Arquivo existe
            for component in analysis["components"].values():
                if component: score += 10
            for optimization in analysis["optimization"].values():
                if optimization: score += 5
        
        analysis["score"] = score
        return analysis
    
    def analyze_intelligent_navigation(self):
        """Analisa otimização da navegação inteligente"""
        print("Analisando navegacao inteligente...")
        
        nav_file = self.maps_path / "intelligent_navigation.json"
        if not nav_file.exists():
            return {"status": "missing", "score": 0}
        
        with open(nav_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        nav_system = data.get("intelligent_navigation", {})
        
        analysis = {
            "status": "exists",
            "version": nav_system.get("version", "unknown"),
            "components": {
                "has_navigation_patterns": "navigation_patterns" in nav_system,
                "has_smart_caching": "smart_caching" in nav_system,
                "has_performance_metrics": "performance_metrics" in nav_system,
                "has_context_switching": "context_switching" in nav_system,
                "has_error_recovery": "error_recovery" in nav_system
            },
            "patterns": {
                "has_context_aware": "context_aware" in nav_system.get("navigation_patterns", {}),
                "has_task_based": "task_based" in nav_system.get("navigation_patterns", {}),
                "has_cache_strategy": "file_access_patterns" in nav_system.get("smart_caching", {}),
                "has_search_optimization": "search_optimization" in nav_system.get("smart_caching", {})
            }
        }
        
        # Calcular score
        score = 0
        if analysis["status"] == "exists":
            score += 20  # Arquivo existe
            for component in analysis["components"].values():
                if component: score += 10
            for pattern in analysis["patterns"].values():
                if pattern: score += 5
        
        analysis["score"] = score
        return analysis
    
    def analyze_performance_metrics(self):
        """Analisa métricas de performance dos caminhos"""
        print("Analisando metricas de performance...")
        
        # Simular tempos de acesso para diferentes caminhos
        paths_to_test = [
            "wiki/maps/tags_index.json",
            "wiki/maps/wiki_map.json",
            "wiki/maps/enhanced_context_system.json",
            "wiki/maps/intelligent_navigation.json",
            ".cursor/rules/rules.md",
            ".cursor/rules/wiki-json-navigation-rules.md"
        ]
        
        performance_data = {}
        total_time = 0
        
        for path in paths_to_test:
            path_obj = Path(path)
            if path_obj.exists():
                start_time = time.time()
                
                # Simular leitura
                if path.endswith('.json'):
                    with open(path_obj, 'r', encoding='utf-8') as f:
                        json.load(f)
                else:
                    with open(path_obj, 'r', encoding='utf-8') as f:
                        f.read()
                
                access_time = (time.time() - start_time) * 1000  # ms
                total_time += access_time
                
                performance_data[path] = {
                    "status": "accessible",
                    "access_time_ms": round(access_time, 2),
                    "size_bytes": path_obj.stat().st_size,
                    "optimization_score": self.calculate_path_optimization_score(path, access_time)
                }
            else:
                performance_data[path] = {
                    "status": "missing",
                    "access_time_ms": 0,
                    "size_bytes": 0,
                    "optimization_score": 0
                }
        
        return {
            "path_performance": performance_data,
            "average_access_time_ms": round(total_time / len(paths_to_test), 2),
            "total_paths_tested": len(paths_to_test)
        }
    
    def calculate_path_optimization_score(self, path, access_time):
        """Calcula score de otimização para um caminho"""
        score = 100
        
        # Penalizar por tempo de acesso
        if access_time > 10:  # > 10ms
            score -= 20
        elif access_time > 5:  # > 5ms
            score -= 10
        
        # Bônus para arquivos otimizados
        if "enhanced" in path or "intelligent" in path:
            score += 10
        
        return max(0, score)
    
    def generate_optimization_report(self):
        """Gera relatório completo de otimização"""
        print("Gerando relatorio de otimizacao...")
        
        # Coletar análises
        tags_analysis = self.analyze_tags_index_optimization()
        wiki_map_analysis = self.analyze_wiki_map_optimization()
        rules_analysis = self.analyze_rules_optimization()
        context_analysis = self.analyze_enhanced_context_system()
        navigation_analysis = self.analyze_intelligent_navigation()
        performance_analysis = self.analyze_performance_metrics()
        
        # Calcular score geral
        scores = [
            tags_analysis["score"],
            wiki_map_analysis["score"],
            rules_analysis["average_score"],
            context_analysis["score"],
            navigation_analysis["score"]
        ]
        
        overall_score = sum(scores) / len(scores)
        
        # Criar relatório
        report = {
            "navigation_optimization_analysis": {
                "timestamp": datetime.now().isoformat(),
                "overall_score": overall_score,
                "grade": self.get_grade(overall_score),
                "individual_scores": {
                    "tags_index": tags_analysis["score"],
                    "wiki_map": wiki_map_analysis["score"],
                    "rules": rules_analysis["average_score"],
                    "context_system": context_analysis["score"],
                    "intelligent_navigation": navigation_analysis["score"]
                },
                "detailed_analysis": {
                    "tags_index_optimization": tags_analysis,
                    "wiki_map_optimization": wiki_map_analysis,
                    "rules_optimization": rules_analysis,
                    "enhanced_context_system": context_analysis,
                    "intelligent_navigation": navigation_analysis,
                    "performance_metrics": performance_analysis
                },
                "optimization_status": {
                    "highly_optimized": overall_score >= 80,
                    "needs_improvement": overall_score < 60,
                    "recommendations": self.generate_optimization_recommendations(overall_score)
                }
            }
        }
        
        # Salvar relatório
        report_file = self.maps_path / "navigation_optimization_report.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"Relatorio salvo: {report_file}")
        return report
    
    def get_grade(self, score):
        """Converte score em nota"""
        if score >= 90:
            return "A+ (Excelente)"
        elif score >= 80:
            return "A (Muito Bom)"
        elif score >= 70:
            return "B+ (Bom)"
        elif score >= 60:
            return "B (Satisfatório)"
        elif score >= 50:
            return "C (Aceitável)"
        else:
            return "D (Necessita Melhorias)"
    
    def generate_optimization_recommendations(self, score):
        """Gera recomendações baseadas no score"""
        if score >= 80:
            return [
                "✅ Sistema altamente otimizado",
                "🔮 Considerar implementar machine learning",
                "📊 Monitorar performance em tempo real",
                "🚀 Explorar otimizações avançadas"
            ]
        elif score >= 60:
            return [
                "📈 Implementar cache inteligente",
                "🔍 Adicionar índices de busca",
                "⚡ Otimizar tempos de acesso",
                "📋 Melhorar estrutura de dados"
            ]
        else:
            return [
                "🚨 Revisar estrutura fundamental",
                "📁 Reorganizar arquivos de navegação",
                "🔧 Implementar sistema de cache básico",
                "📊 Adicionar métricas de performance"
            ]

def main():
    """Função principal"""
    print("Iniciando analise de otimizacao de navegacao...")
    
    analyzer = NavigationOptimizationAnalyzer()
    report = analyzer.generate_optimization_report()
    
    # Exibir resultados principais
    score = report["navigation_optimization_analysis"]["overall_score"]
    grade = report["navigation_optimization_analysis"]["grade"]
    
    print(f"\nRESULTADOS DA ANALISE DE OTIMIZACAO:")
    print(f"Score Geral: {score:.1f}/100")
    print(f"Nota: {grade}")
    
    individual_scores = report["navigation_optimization_analysis"]["individual_scores"]
    print(f"\nScores Individuais:")
    for component, score in individual_scores.items():
        print(f"  • {component}: {score:.1f}/100")
    
    print(f"\nAnalise concluida com sucesso!")
    print(f"Relatorio completo salvo em: wiki/maps/navigation_optimization_report.json")

if __name__ == "__main__":
    main() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = CodeanalyzerModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script analyze_navigation_optimization.py executado com sucesso via módulo python.code_analyzer")
    else:
        print(f"❌ Erro na execução do script analyze_navigation_optimization.py via módulo python.code_analyzer")

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
- **Nome**: migrated_analyze_navigation_optimization
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

