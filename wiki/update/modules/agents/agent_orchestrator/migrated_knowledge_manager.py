# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: knowledge_manager.py
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
📚 Knowledge Manager Agent
Responsável por gerenciar navegação da wiki e extrair insights dos resultados
"""

import os
import json
from datetime import datetime

class KnowledgeManagerAgent:
    """Agente especializado em gerenciamento de conhecimento e navegação da wiki"""
    
    def __init__(self, workspace_path: str = None):
        self.workspace_path = workspace_path or os.getcwd()
        # Ajustar caminho para encontrar módulos na raiz do projeto
        if os.path.basename(self.workspace_path) == "bmad":
            # Se estamos na pasta bmad, subir um nível
            self.workspace_path = os.path.dirname(self.workspace_path)
        if os.path.basename(self.workspace_path) == "wiki":
            # Se estamos na pasta wiki, subir um nível
            self.workspace_path = os.path.dirname(self.workspace_path)
        
        self.wiki_path = os.path.join(self.workspace_path, "wiki")
        self.maps_path = os.path.join(self.wiki_path, "maps")
        self.results_path = os.path.join(self.workspace_path, "wiki/bmad/results")
        self.knowledge_path = os.path.join(self.workspace_path, "wiki/bmad/knowledge")
        
        # Criar diretórios se não existirem
        os.makedirs(self.results_path, exist_ok=True)
        os.makedirs(os.path.join(self.results_path, "learning_data"), exist_ok=True)
        os.makedirs(self.knowledge_path, exist_ok=True)
        
        # Carregar mapas de navegação
        self.load_navigation_maps()
        
        # Base de conhecimento
        self.knowledge_base = {
            "patterns": {},
            "insights": {},
            "rules": {},
            "best_practices": {},
            "error_patterns": {},
            "success_patterns": {}
        }
    
    def load_navigation_maps(self):
        """Carrega mapas de navegação da wiki"""
        try:
            # Carregar tags_index.json
            tags_file = os.path.join(self.maps_path, "tags_index.json")
            if os.path.exists(tags_file):
                with open(tags_file, 'r', encoding='utf-8') as f:
                    self.tags_index = json.load(f)
            else:
                self.tags_index = {}
            
            # Carregar wiki_map.json
            wiki_map_file = os.path.join(self.maps_path, "wiki_map.json")
            if os.path.exists(wiki_map_file):
                with open(wiki_map_file, 'r', encoding='utf-8') as f:
                    self.wiki_map = json.load(f)
            else:
                self.wiki_map = {}
            
            # Carregar relationships.json
            relationships_file = os.path.join(self.maps_path, "relationships.json")
            if os.path.exists(relationships_file):
                with open(relationships_file, 'r', encoding='utf-8') as f:
                    self.relationships = json.load(f)
            else:
                self.relationships = {}
                
        except Exception as e:
            print(f"⚠️ Erro ao carregar mapas de navegação: {e}")
            self.tags_index = {}
            self.wiki_map = {}
            self.relationships = {}
    
    def process_workflow_results(self, analysis_results: Dict[str, Any], 
                               generation_results: List[Dict[str, Any]], 
                               test_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Processa resultados do workflow completo e extrai insights
        
        Args:
            analysis_results: Resultados do Module Analyzer
            generation_results: Resultados do Module Generator
            test_results: Resultados do Module Tester
            
        Returns:
            Insights e aprendizados extraídos
        """
        print("📚 Processando resultados do workflow e extraindo insights")
        
        learning_data = {
            "processing_date": datetime.now().isoformat(),
            "original_module": analysis_results.get("module_name", "unknown"),
            "insights": {},
            "patterns": {},
            "rules": {},
            "recommendations": [],
            "knowledge_updates": {}
        }
        
        # Extrair insights dos resultados de análise
        analysis_insights = self.extract_analysis_insights(analysis_results)
        learning_data["insights"]["analysis"] = analysis_insights
        
        # Extrair insights dos resultados de geração
        generation_insights = self.extract_generation_insights(generation_results)
        learning_data["insights"]["generation"] = generation_insights
        
        # Extrair insights dos resultados de teste
        test_insights = self.extract_test_insights(test_results)
        learning_data["insights"]["testing"] = test_insights
        
        # Identificar padrões
        learning_data["patterns"] = self.identify_patterns(analysis_results, generation_results, test_results)
        
        # Gerar regras
        learning_data["rules"] = self.generate_rules(learning_data["insights"], learning_data["patterns"])
        
        # Gerar recomendações
        learning_data["recommendations"] = self.generate_recommendations(learning_data)
        
        # Atualizar base de conhecimento
        learning_data["knowledge_updates"] = self.update_knowledge_base(learning_data)
        
        # Salvar dados de aprendizado
        self.save_learning_data(analysis_results.get("module_name", "unknown"), learning_data)
        
        return learning_data
    
    def extract_analysis_insights(self, analysis_results: Dict[str, Any]) -> Dict[str, Any]:
        """Extrai insights dos resultados de análise"""
        insights = {
            "module_complexity": {},
            "code_patterns": {},
            "dependencies": {},
            "structure_insights": {},
            "quality_metrics": {}
        }
        
        # Análise de complexidade
        metrics = analysis_results.get("metrics", {})
        insights["module_complexity"] = {
            "overall_complexity": metrics.get("complexity", 0),
            "coverage": metrics.get("coverage", 0),
            "documentation_quality": metrics.get("documentation_quality", 0),
            "pattern_diversity": metrics.get("pattern_diversity", 0)
        }
        
        # Padrões de código
        patterns = analysis_results.get("patterns", {})
        insights["code_patterns"] = {
            "lua_patterns": patterns.get("lua_patterns", {}),
            "otmod_patterns": patterns.get("otmod_patterns", {}),
            "otui_patterns": patterns.get("otui_patterns", {}),
            "common_patterns": patterns.get("common_patterns", {})
        }
        
        # Dependências
        dependencies = analysis_results.get("dependencies", {})
        insights["dependencies"] = {
            "api_dependencies": dependencies.get("api_deps", []),
            "module_dependencies": dependencies.get("module_deps", []),
            "internal_dependencies": dependencies.get("internal_deps", [])
        }
        
        # Estrutura
        structure = analysis_results.get("structure", {})
        insights["structure_insights"] = {
            "file_count": len(analysis_results.get("files", {})),
            "file_types": self.analyze_file_types(analysis_results.get("files", {})),
            "structure_complexity": structure
        }
        
        return insights
    
    def extract_generation_insights(self, generation_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Extrai insights dos resultados de geração"""
        insights = {
            "generation_success": {},
            "variation_patterns": {},
            "modification_insights": {},
            "compatibility_insights": {}
        }
        
        if not generation_results:
            return insights
        
        # Sucesso da geração
        total_variations = len(generation_results)
        successful_variations = sum(1 for v in generation_results if v.get("compatibility_score", 0) > 0.7)
        
        insights["generation_success"] = {
            "total_variations": total_variations,
            "successful_variations": successful_variations,
            "success_rate": successful_variations / total_variations if total_variations > 0 else 0
        }
        
        # Padrões de variação
        variation_patterns = defaultdict(int)
        modification_patterns = defaultdict(int)
        
        for variation in generation_results:
            # Padrões de nomenclatura
            variation_name = variation.get("variation_name", "")
            if "_enhanced" in variation_name:
                variation_patterns["enhanced"] += 1
            elif "_improved" in variation_name:
                variation_patterns["improved"] += 1
            elif "_basic" in variation_name:
                variation_patterns["basic"] += 1
            
            # Padrões de modificação
            modifications = variation.get("modifications", {})
            for mod_type, count in modifications.items():
                modification_patterns[mod_type] += count
        
        insights["variation_patterns"] = dict(variation_patterns)
        insights["modification_insights"] = dict(modification_patterns)
        
        # Insights de compatibilidade
        compatibility_scores = [v.get("compatibility_score", 0) for v in generation_results]
        insights["compatibility_insights"] = {
            "average_score": sum(compatibility_scores) / len(compatibility_scores) if compatibility_scores else 0,
            "min_score": min(compatibility_scores) if compatibility_scores else 0,
            "max_score": max(compatibility_scores) if compatibility_scores else 0,
            "score_distribution": self.analyze_score_distribution(compatibility_scores)
        }
        
        return insights
    
    def extract_test_insights(self, test_results: Dict[str, Any]) -> Dict[str, Any]:
        """Extrai insights dos resultados de teste"""
        insights = {
            "test_success": {},
            "error_patterns": {},
            "quality_insights": {},
            "performance_insights": {},
            "security_insights": {}
        }
        
        # Sucesso dos testes
        summary = test_results.get("summary", {})
        insights["test_success"] = {
            "total_variations": summary.get("total_variations", 0),
            "passed_variations": summary.get("passed_variations", 0),
            "failed_variations": summary.get("failed_variations", 0),
            "pass_rate": summary.get("passed_variations", 0) / max(summary.get("total_variations", 1), 1)
        }
        
        # Padrões de erro
        error_patterns = defaultdict(int)
        for variation_result in test_results.get("variation_results", []):
            for error in variation_result.get("errors", []):
                error_patterns[error] += 1
        
        insights["error_patterns"] = dict(error_patterns)
        
        # Insights de qualidade
        insights["quality_insights"] = {
            "average_quality_score": summary.get("average_quality_score", 0),
            "average_compatibility_score": summary.get("average_compatibility_score", 0),
            "average_performance_score": summary.get("average_performance_score", 0),
            "total_errors": summary.get("total_errors", 0),
            "total_warnings": summary.get("total_warnings", 0)
        }
        
        return insights
    
    def identify_patterns(self, analysis_results: Dict[str, Any], 
                         generation_results: List[Dict[str, Any]], 
                         test_results: Dict[str, Any]) -> Dict[str, Any]:
        """Identifica padrões nos resultados"""
        patterns = {
            "success_patterns": {},
            "failure_patterns": {},
            "code_patterns": {},
            "structural_patterns": {}
        }
        
        # Padrões de sucesso
        successful_variations = [v for v in generation_results if v.get("compatibility_score", 0) > 0.8]
        if successful_variations:
            patterns["success_patterns"] = self.analyze_success_patterns(successful_variations)
        
        # Padrões de falha
        failed_variations = [v for v in generation_results if v.get("compatibility_score", 0) < 0.5]
        if failed_variations:
            patterns["failure_patterns"] = self.analyze_failure_patterns(failed_variations)
        
        # Padrões de código
        patterns["code_patterns"] = self.analyze_code_patterns(analysis_results)
        
        # Padrões estruturais
        patterns["structural_patterns"] = self.analyze_structural_patterns(analysis_results, generation_results)
        
        return patterns
    
    def analyze_success_patterns(self, successful_variations: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analisa padrões de sucesso"""
        patterns = {
            "modification_characteristics": {},
            "naming_patterns": {},
            "structure_characteristics": {}
        }
        
        # Características de modificação
        mod_counts = defaultdict(int)
        for variation in successful_variations:
            modifications = variation.get("modifications", {})
            for mod_type, count in modifications.items():
                mod_counts[mod_type] += count
        
        patterns["modification_characteristics"] = dict(mod_counts)
        
        # Padrões de nomenclatura
        naming_patterns = defaultdict(int)
        for variation in successful_variations:
            name = variation.get("variation_name", "")
            for suffix in ["_enhanced", "_improved", "_advanced", "_basic", "_simple"]:
                if suffix in name:
                    naming_patterns[suffix] += 1
        
        patterns["naming_patterns"] = dict(naming_patterns)
        
        return patterns
    
    def analyze_failure_patterns(self, failed_variations: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analisa padrões de falha"""
        patterns = {
            "error_types": {},
            "modification_issues": {},
            "compatibility_issues": {}
        }
        
        # Tipos de erro
        error_types = defaultdict(int)
        for variation in failed_variations:
            # Simular análise de erros (baseado em score baixo)
            if variation.get("compatibility_score", 0) < 0.3:
                error_types["very_low_compatibility"] += 1
            elif variation.get("compatibility_score", 0) < 0.5:
                error_types["low_compatibility"] += 1
        
        patterns["error_types"] = dict(error_types)
        
        return patterns
    
    def analyze_code_patterns(self, analysis_results: Dict[str, Any]) -> Dict[str, Any]:
        """Analisa padrões de código"""
        patterns = {
            "function_patterns": {},
            "variable_patterns": {},
            "api_usage_patterns": {},
            "file_structure_patterns": {}
        }
        
        # Padrões de função
        lua_patterns = analysis_results.get("patterns", {}).get("lua_patterns", {})
        patterns["function_patterns"] = {
            "total_functions": len(lua_patterns.get("function_patterns", [])),
            "common_function_names": self.get_common_patterns(lua_patterns.get("function_patterns", []))
        }
        
        # Padrões de variável
        patterns["variable_patterns"] = {
            "total_variables": len(lua_patterns.get("variable_patterns", [])),
            "common_variable_names": self.get_common_patterns(lua_patterns.get("variable_patterns", []))
        }
        
        # Padrões de uso de API
        patterns["api_usage_patterns"] = {
            "total_api_calls": len(lua_patterns.get("api_usage", [])),
            "common_apis": self.get_common_patterns(lua_patterns.get("api_usage", []))
        }
        
        return patterns
    
    def analyze_structural_patterns(self, analysis_results: Dict[str, Any], 
                                  generation_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analisa padrões estruturais"""
        patterns = {
            "file_organization": {},
            "module_structure": {},
            "dependency_patterns": {}
        }
        
        # Organização de arquivos
        files = analysis_results.get("files", {})
        file_types = defaultdict(int)
        for file_path in files.keys():
            ext = Path(file_path).suffix
            file_types[ext] += 1
        
        patterns["file_organization"] = dict(file_types)
        
        # Estrutura do módulo
        patterns["module_structure"] = {
            "total_files": len(files),
            "has_lua_files": any(f.endswith('.lua') for f in files.keys()),
            "has_otmod_files": any(f.endswith('.otmod') for f in files.keys()),
            "has_otui_files": any(f.endswith('.otui') for f in files.keys())
        }
        
        return patterns
    
    def generate_rules(self, insights: Dict[str, Any], patterns: Dict[str, Any]) -> Dict[str, Any]:
        """Gera regras baseadas nos insights e padrões"""
        rules = {
            "generation_rules": [],
            "testing_rules": [],
            "quality_rules": [],
            "best_practices": []
        }
        
        # Regras de geração
        generation_insights = insights.get("generation", {})
        success_rate = generation_insights.get("generation_success", {}).get("success_rate", 0)
        
        if success_rate > 0.8:
            rules["generation_rules"].append("Manter padrões de geração atuais - alta taxa de sucesso")
        elif success_rate < 0.5:
            rules["generation_rules"].append("Revisar critérios de geração - baixa taxa de sucesso")
        
        # Regras de teste
        test_insights = insights.get("testing", {})
        pass_rate = test_insights.get("test_success", {}).get("pass_rate", 0)
        
        if pass_rate < 0.7:
            rules["testing_rules"].append("Melhorar critérios de validação - muitas falhas nos testes")
        
        # Regras de qualidade
        quality_insights = test_insights.get("quality_insights", {})
        avg_quality = quality_insights.get("average_quality_score", 0)
        
        if avg_quality < 0.8:
            rules["quality_rules"].append("Melhorar validação de sintaxe e estrutura")
        
        # Melhores práticas
        if patterns.get("success_patterns"):
            rules["best_practices"].append("Seguir padrões identificados em variações bem-sucedidas")
        
        return rules
    
    def generate_recommendations(self, learning_data: Dict[str, Any]) -> List[str]:
        """Gera recomendações baseadas nos dados de aprendizado"""
        recommendations = []
        
        insights = learning_data.get("insights", {})
        patterns = learning_data.get("patterns", {})
        
        # Recomendações baseadas em insights de geração
        generation_insights = insights.get("generation", {})
        success_rate = generation_insights.get("generation_success", {}).get("success_rate", 0)
        
        if success_rate < 0.6:
            recommendations.append("Revisar algoritmos de geração para melhorar taxa de sucesso")
        
        # Recomendações baseadas em insights de teste
        test_insights = insights.get("testing", {})
        pass_rate = test_insights.get("test_success", {}).get("pass_rate", 0)
        
        if pass_rate < 0.7:
            recommendations.append("Melhorar critérios de teste para reduzir falsos positivos")
        
        # Recomendações baseadas em padrões
        if patterns.get("failure_patterns"):
            recommendations.append("Analisar e corrigir padrões de falha identificados")
        
        # Recomendações gerais
        if not recommendations:
            recommendations.append("Workflow funcionando bem - manter configurações atuais")
        
        return recommendations
    
    def update_knowledge_base(self, learning_data: Dict[str, Any]) -> Dict[str, Any]:
        """Atualiza base de conhecimento com novos dados"""
        updates = {
            "patterns_updated": {},
            "rules_updated": {},
            "insights_updated": {},
            "best_practices_updated": {}
        }
        
        # Atualizar padrões
        new_patterns = learning_data.get("patterns", {})
        for pattern_type, patterns in new_patterns.items():
            if patterns:
                self.knowledge_base["patterns"][pattern_type] = patterns
                updates["patterns_updated"][pattern_type] = len(patterns)
        
        # Atualizar regras
        new_rules = learning_data.get("rules", {})
        for rule_type, rules in new_rules.items():
            if rules:
                self.knowledge_base["rules"][rule_type] = rules
                updates["rules_updated"][rule_type] = len(rules)
        
        # Atualizar insights
        new_insights = learning_data.get("insights", {})
        for insight_type, insights in new_insights.items():
            if insights:
                self.knowledge_base["insights"][insight_type] = insights
                updates["insights_updated"][insight_type] = len(insights)
        
        # Salvar base de conhecimento atualizada
        self.save_knowledge_base()
        
        return updates
    
    def save_knowledge_base(self):
        """Salva base de conhecimento em arquivo"""
        knowledge_file = os.path.join(self.knowledge_path, "knowledge_base.json")
        
        try:
            with open(knowledge_file, 'w', encoding='utf-8') as f:
                json.dump(self.knowledge_base, f, indent=2, ensure_ascii=False)
            print(f"✅ Base de conhecimento salva em: {knowledge_file}")
        except Exception as e:
            print(f"⚠️ Erro ao salvar base de conhecimento: {e}")
    
    def save_learning_data(self, module_name: str, learning_data: Dict[str, Any]):
        """Salva dados de aprendizado"""
        learning_file = os.path.join(
            self.results_path, 
            "learning_data", 
            f"{module_name}_learning_data.json"
        )
        
        try:
            with open(learning_file, 'w', encoding='utf-8') as f:
                json.dump(learning_data, f, indent=2, ensure_ascii=False)
            print(f"✅ Dados de aprendizado salvos em: {learning_file}")
        except Exception as e:
            print(f"⚠️ Erro ao salvar dados de aprendizado: {e}")
    
    def analyze_file_types(self, files: Dict[str, Any]) -> Dict[str, int]:
        """Analisa tipos de arquivo"""
        file_types = defaultdict(int)
        for file_path in files.keys():
            ext = Path(file_path).suffix
            file_types[ext] += 1
        return dict(file_types)
    
    def analyze_score_distribution(self, scores: List[float]) -> Dict[str, int]:
        """Analisa distribuição de scores"""
        distribution = {
            "excellent": 0,  # 0.9-1.0
            "good": 0,       # 0.7-0.9
            "fair": 0,       # 0.5-0.7
            "poor": 0        # 0.0-0.5
        }
        
        for score in scores:
            if score >= 0.9:
                distribution["excellent"] += 1
            elif score >= 0.7:
                distribution["good"] += 1
            elif score >= 0.5:
                distribution["fair"] += 1
            else:
                distribution["poor"] += 1
        
        return distribution
    
    def get_common_patterns(self, patterns: List[str], top_n: int = 5) -> List[Tuple[str, int]]:
        """Obtém padrões mais comuns"""
        pattern_counts = defaultdict(int)
        for pattern in patterns:
            pattern_counts[pattern] += 1
        
        # Retornar top N padrões mais comuns
        sorted_patterns = sorted(pattern_counts.items(), key=lambda x: x[1], reverse=True)
        return sorted_patterns[:top_n]
    
    def get_wiki_knowledge(self, topic: str) -> Dict[str, Any]:
        """Obtém conhecimento da wiki sobre um tópico específico"""
        knowledge = {
            "related_docs": [],
            "patterns": {},
            "examples": [],
            "best_practices": []
        }
        
        # Buscar documentos relacionados
        if self.tags_index:
            for doc_path, tags in self.tags_index.items():
                if topic.lower() in [tag.lower() for tag in tags]:
                    knowledge["related_docs"].append(doc_path)
        
        # Buscar no wiki_map
        if self.wiki_map:
            for doc_path, doc_info in self.wiki_map.items():
                if topic.lower() in doc_info.get("title", "").lower():
                    knowledge["related_docs"].append(doc_path)
        
        return knowledge
    
    def update_navigation_maps(self):
        """Atualiza mapas de navegação com novos dados"""
        # Esta função seria chamada quando novos documentos são criados
        # Por enquanto, apenas recarrega os mapas existentes
        self.load_navigation_maps()
        print("🗺️ Mapas de navegação atualizados")

def main():
    """Função principal para teste do agente"""
    knowledge_manager = KnowledgeManagerAgent()
    
    # Exemplo de dados de teste
    analysis_results = {
        "module_name": "client",
        "metrics": {"complexity": 10, "coverage": 5},
        "patterns": {"lua_patterns": {"function_patterns": ["init", "startup"]}},
        "dependencies": {"api_deps": ["game", "ui"]},
        "files": {"client.lua": {}, "client.otmod": {}}
    }
    
    generation_results = [
        {
            "variation_name": "client_enhanced_1",
            "compatibility_score": 0.8,
            "modifications": {"functions_added": 2}
        }
    ]
    
    test_results = {
        "summary": {
            "total_variations": 1,
            "passed_variations": 1,
            "average_quality_score": 0.85
        }
    }
    
    # Processar resultados
    learning_data = knowledge_manager.process_workflow_results(
        analysis_results, generation_results, test_results
    )
    
    print(f"✅ Processamento concluído")
    print(f"📊 Insights extraídos: {len(learning_data['insights'])}")

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
        print(f"✅ Script knowledge_manager.py executado com sucesso via módulo agents.agent_orchestrator")
    else:
        print(f"❌ Erro na execução do script knowledge_manager.py via módulo agents.agent_orchestrator")
