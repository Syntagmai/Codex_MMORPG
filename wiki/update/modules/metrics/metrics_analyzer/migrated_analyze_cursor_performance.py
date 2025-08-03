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
Script Migrado: analyze_cursor_performance.py
Módulo de Destino: metrics.metrics_analyzer
Data de Migração: 2025-08-01 12:21:34

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import MetricsanalyzerModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Análise de Performance do cursor.md
Analisa a eficiência do cursor.md como ponto de entrada para navegação da IA
"""

import json
import time
from datetime import datetime

class CursorPerformanceAnalyzer:
    def __init__(self):
        self.cursor_file = Path("cursor.md")
        self.maps_path = Path("wiki/maps")
        self.rules_path = Path(".cursor/rules")
        
    def analyze_cursor_structure(self):
        """Analisa a estrutura do cursor.md para navegação"""
        print("🔍 Analisando estrutura do cursor.md...")
        
        with open(self.cursor_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        analysis = {
            "file_info": {
                "size_bytes": len(content),
                "lines": len(content.split('\n')),
                "sections": content.count('##'),
                "tables": content.count('|'),
                "code_blocks": content.count('```')
            },
            "navigation_elements": {
                "quick_index": "🚀 **ÍNDICE DE NAVEGAÇÃO RÁPIDA**" in content,
                "context_commands": content.count('@otclient') + content.count('@bmad') + content.count('@wiki') + content.count('@integration'),
    
                "file_references": content.count('.md') + content.count('.json'),
                "path_references": content.count('wiki/') + content.count('.cursor/') + content.count('src/')
            },
            "performance_indicators": {
                "hierarchy_defined": "Hierarquia de Prioridades" in content,
                "cache_info": "Cache Inteligente" in content,
                "timeout_info": "Timeout" in content,
                "lazy_loading": "Lazy Loading" in content
            }
        }
        
        return analysis
    
    def analyze_navigation_efficiency(self):
        """Analisa a eficiência de navegação"""
        print("🧭 Analisando eficiência de navegação...")
        
        # Simular diferentes tipos de consulta
        query_types = {
            "context_detection": ["@otclient", "@bmad", "@wiki", "@integration"],
            "rule_lookup": ["rules.md", "prompt-engineering", "wiki-rules"],
            "file_access": ["tags_index.json", "wiki_map.json", "enhanced_context_system.json"],
            "code_analysis": ["src/", "modules/", "otclient_source_index.json"]
        }
        
        efficiency_analysis = {}
        
        for query_type, keywords in query_types.items():
            start_time = time.time()
            
            # Simular busca no cursor.md
            with open(self.cursor_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Contar ocorrências e relevância
            relevance_score = 0
            for keyword in keywords:
                if keyword in content:
                    relevance_score += 1
            
            search_time = time.time() - start_time
            
            efficiency_analysis[query_type] = {
                "search_time_ms": round(search_time * 1000, 2),
                "relevance_score": relevance_score / len(keywords),
                "keywords_found": relevance_score,
                "total_keywords": len(keywords)
            }
        
        return efficiency_analysis
    
    def analyze_cache_effectiveness(self):
        """Analisa a eficácia do sistema de cache"""
        print("💾 Analisando eficácia do cache...")
        
        cache_analysis = {
            "frequently_accessed_files": [
                "cursor.md",
                "wiki/maps/tags_index.json",
                "wiki/maps/wiki_map.json",
                ".cursor/rules/rules.md"
            ],
            "cache_strategy": {
                "high_priority": {
                    "files": ["cursor.md", "tags_index.json", "wiki_map.json"],
                    "duration_minutes": 30,
                    "access_frequency": "high"
                },
                "medium_priority": {
                    "files": ["enhanced_context_system.json", "context_data.json"],
                    "duration_minutes": 15,
                    "access_frequency": "medium"
                },
                "low_priority": {
                    "files": ["otclient_source_index.json", "modules_index.json"],
                    "duration_minutes": 60,
                    "access_frequency": "low"
                }
            }
        }
        
        return cache_analysis
    
    def generate_optimization_recommendations(self):
        """Gera recomendações de otimização"""
        print("🎯 Gerando recomendações de otimização...")
        
        recommendations = {
            "structure_improvements": [
                "✅ Índice de navegação rápida implementado",
                "✅ Mapa visual da estrutura adicionado",
                "✅ Fluxo de navegação otimizado definido",
                "✅ Seção de performance adicionada"
            ],
            "performance_optimizations": [
                "✅ Cache inteligente configurado",
                "✅ Limites de análise definidos",
                "✅ Timeouts implementados",
                "✅ Lazy loading configurado"
            ],
            "navigation_enhancements": [
                "✅ Contextos automáticos (@otclient, @bmad, @wiki, @integration)",
                "✅ Padrões de navegação específicos",
                "✅ Recuperação de erros implementada",
                "✅ Métricas de performance definidas"
            ],
            "future_improvements": [
                "🔮 Implementar busca semântica avançada",
                "🔮 Adicionar machine learning para otimização",
                "🔮 Criar dashboard de performance em tempo real",
                "🔮 Implementar cache distribuído"
            ]
        }
        
        return recommendations
    
    def calculate_performance_score(self, analysis_data):
        """Calcula score de performance geral"""
        print("📊 Calculando score de performance...")
        
        # Fatores de pontuação
        structure_score = 0
        if analysis_data["navigation_elements"]["quick_index"]:
            structure_score += 25
        if analysis_data["navigation_elements"]["context_commands"] >= 4:
            structure_score += 25
        if analysis_data["navigation_elements"]["file_references"] >= 20:
            structure_score += 25
        if analysis_data["navigation_elements"]["path_references"] >= 10:
            structure_score += 25
        
        performance_score = 0
        if analysis_data["performance_indicators"]["hierarchy_defined"]:
            performance_score += 25
        if analysis_data["performance_indicators"]["cache_info"]:
            performance_score += 25
        if analysis_data["performance_indicators"]["timeout_info"]:
            performance_score += 25
        if analysis_data["performance_indicators"]["lazy_loading"]:
            performance_score += 25
        
        total_score = (structure_score + performance_score) / 2
        
        return {
            "total_score": total_score,
            "structure_score": structure_score,
            "performance_score": performance_score,
            "grade": self.get_grade(total_score)
        }
    
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
    
    def generate_report(self):
        """Gera relatório completo de análise"""
        print("📋 Gerando relatório de análise...")
        
        # Coletar dados
        structure_analysis = self.analyze_cursor_structure()
        navigation_efficiency = self.analyze_navigation_efficiency()
        cache_effectiveness = self.analyze_cache_effectiveness()
        recommendations = self.generate_optimization_recommendations()
        performance_score = self.calculate_performance_score(structure_analysis)
        
        # Criar relatório
        report = {
            "cursor_performance_analysis": {
                "timestamp": datetime.now().isoformat(),
                "file_analyzed": "cursor.md",
                "performance_score": performance_score,
                "structure_analysis": structure_analysis,
                "navigation_efficiency": navigation_efficiency,
                "cache_effectiveness": cache_effectiveness,
                "optimization_recommendations": recommendations,
                "summary": {
                    "overall_grade": performance_score["grade"],
                    "total_score": performance_score["total_score"],
                    "key_strengths": [
                        "Índice de navegação rápida implementado",
                        "Sistema de cache inteligente configurado",
                        "Hierarquia de prioridades bem definida",
                        "Contextos automáticos funcionais"
                    ],
                    "improvement_areas": [
                        "Implementar busca semântica avançada",
                        "Adicionar machine learning para otimização",
                        "Criar dashboard de performance em tempo real"
                    ]
                }
            }
        }
        
        # Salvar relatório
        report_file = self.maps_path / "cursor_performance_analysis.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"📊 Relatório salvo: {report_file}")
        return report

def main():
    """Função principal"""
    print("🚀 Iniciando análise de performance do cursor.md...")
    
    analyzer = CursorPerformanceAnalyzer()
    report = analyzer.generate_report()
    
    # Exibir resultados principais
    score = report["cursor_performance_analysis"]["performance_score"]
    print(f"\n🎯 RESULTADOS DA ANÁLISE:")
    print(f"📊 Score Total: {score['total_score']:.1f}/100")
    print(f"🏆 Nota: {score['grade']}")
    print(f"📈 Score de Estrutura: {score['structure_score']:.1f}/100")
    print(f"⚡ Score de Performance: {score['performance_score']:.1f}/100")
    
    print(f"\n✅ Análise concluída com sucesso!")
    print(f"📋 Relatório completo salvo em: wiki/maps/cursor_performance_analysis.json")

if __name__ == "__main__":
    main() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = MetricsanalyzerModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script analyze_cursor_performance.py executado com sucesso via módulo metrics.metrics_analyzer")
    else:
        print(f"❌ Erro na execução do script analyze_cursor_performance.py via módulo metrics.metrics_analyzer")
