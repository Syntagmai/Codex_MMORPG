from unicode_aliases import *
# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
MAX_ITEMS = 100
MAX_SIZE = 1000

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: rules_learning_integration.py
Módulo de Destino: tools.git_automation
Data de Migração: 2025-08-01 12:21:45

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import GitautomationModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Integração de Auto-Aprendizado com Sistema de Regras
Permite que o sistema aprenda e melhore regras automaticamente baseado em interações
"""

import json
import re
import hashlib
from datetime import datetime, timedelta
import statistics

@dataclass
class RuleLearningPattern:
    """Padrão aprendido sobre regras"""
    rule_id: str
    rule_file: str
    rule_section: str
    usage_frequency: int
    success_rate: float
    context_applicability: Dict[str, float]
    suggested_improvements: List[str]
    last_updated: str
    confidence_score: float

@dataclass
class RuleOptimization:
    """Otimização sugerida para uma regra"""
    rule_id: str
    optimization_type: str  # 'add', 'modify', 'remove', 'reorganize'
    current_content: str
    suggested_content: str
    reasoning: str
    confidence: float
    impact_score: float

class RulesLearningIntegration:
    """Sistema de integração entre auto-aprendizado e regras"""
    
    def __init__(self, base_path: str = "wiki"):
        self.base_path = Path(base_path)
        self.rules_path = Path(".cursor/rules")
        self.auto_learning_path = self.base_path / "bmad" / "auto_learning"
        self.rules_learning_path = self.auto_learning_path / "rules_learning"
        
        # Criar estrutura de pastas
        self.rules_learning_path.mkdir(parents=True, exist_ok=True)
        
        # Arquivos de dados
        self.rule_patterns_file = self.rules_learning_path / "rule_patterns.json"
        self.rule_optimizations_file = self.rules_learning_path / "rule_optimizations.json"
        self.rule_usage_log_file = self.rules_learning_path / "rule_usage_log.json"
        
        # Carregar dados existentes
        self.rule_patterns = self.load_rule_patterns()
        self.rule_optimizations = self.load_rule_optimizations()
        self.rule_usage_log = self.load_rule_usage_log()
        
        # Cache de regras
        self.rules_cache = {}
        self.rules_cache_timestamp = None
        self.cache_validity = 300  # 5 minutos
        
        # Configurações
        self.min_usage_for_optimization = 5
        self.min_success_rate_for_improvement = 0.7
        self.max_optimizations_per_rule = 3
    
    def load_rule_patterns(self) -> Dict[str, Any]:
        """Carrega padrões de regras aprendidos"""
        if self.rule_patterns_file.exists():
            with open(self.rule_patterns_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def load_rule_optimizations(self) -> Dict[str, Any]:
        """Carrega otimizações de regras"""
        if self.rule_optimizations_file.exists():
            with open(self.rule_optimizations_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def load_rule_usage_log(self) -> Dict[str, Any]:
        """Carrega log de uso de regras"""
        if self.rule_usage_log_file.exists():
            with open(self.rule_usage_log_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"usage": [], "statistics": {}}
    
    def save_rule_patterns(self):
        """Salva padrões de regras aprendidos"""
        with open(self.rule_patterns_file, 'w', encoding='utf-8') as f:
            json.dump(self.rule_patterns, f, indent=2, ensure_ascii=False)
    
    def save_rule_optimizations(self):
        """Salva otimizações de regras"""
        with open(self.rule_optimizations_file, 'w', encoding='utf-8') as f:
            json.dump(self.rule_optimizations, f, indent=2, ensure_ascii=False)
    
    def save_rule_usage_log(self):
        """Salva log de uso de regras"""
        with open(self.rule_usage_log_file, 'w', encoding='utf-8') as f:
            json.dump(self.rule_usage_log, f, indent=2, ensure_ascii=False)
    
    def get_all_rules(self) -> Dict[str, str]:
        """Obtém todas as regras do sistema"""
        if (self.rules_cache_timestamp and 
            (datetime.now() - self.rules_cache_timestamp).seconds < self.cache_validity):
            return self.rules_cache
        
        rules = {}
        for rule_file in self.rules_path.glob("*.md"):
            try:
                with open(rule_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    rules[rule_file.name] = content
            except Exception as e:
                print(f"Erro ao ler regra {rule_file}: {e}")
        
        self.rules_cache = rules
        self.rules_cache_timestamp = datetime.now()
        return rules
    
    def parse_rule_content(self, content: str) -> Dict[str, Any]:
        """Analisa conteúdo de uma regra"""
        sections = {}
        current_section = "main"
        current_content = []
        
        for line in content.split('\n'):
            if line.startswith('## '):
                if current_content:
                    sections[current_section] = '\n'.join(current_content).strip()
                current_section = line[3:].strip()
                current_content = []
            else:
                current_content.append(line)
        
        if current_content:
            sections[current_section] = '\n'.join(current_content).strip()
        
        return sections
    
    def record_rule_usage(self, rule_file: str, context: Dict[str, Any], 
                         success_score: float, feedback: Optional[str] = None):
        """Registra uso de uma regra"""
        usage_entry = {
            "timestamp": datetime.now().isoformat(),
            "rule_file": rule_file,
            "context": context,
            "success_score": success_score,
            "feedback": feedback
        }
        
        self.rule_usage_log["usage"].append(usage_entry)
        
        # Manter apenas últimos 1000 usos
        if len(self.rule_usage_log["usage"]) > 1000:
            self.rule_usage_log["usage"] = self.rule_usage_log["usage"][-1000:]
        
        self.save_rule_usage_log()
    
    def analyze_rule_patterns(self) -> List[RuleLearningPattern]:
        """Analisa padrões de uso das regras"""
        patterns = []
        
        # Agrupar usos por regra
        rule_usage = defaultdict(list)
        for usage in self.rule_usage_log["usage"]:
            rule_usage[usage["rule_file"]].append(usage)
        
        for rule_file, usages in rule_usage.items():
            if len(usages) < self.min_usage_for_optimization:
                continue
            
            # Calcular estatísticas
            success_scores = [u["success_score"] for u in usages]
            avg_success = statistics.mean(success_scores)
            
            # Analisar contexto
            context_applicability = self._analyze_context_applicability(usages)
            
            # Gerar sugestões de melhoria
            suggestions = self._generate_rule_improvements(rule_file, usages)
            
            pattern = RuleLearningPattern(
                rule_id=hashlib.md5(rule_file.encode()).hexdigest()[:8],
                rule_file=rule_file,
                rule_section="main",
                usage_frequency=len(usages),
                success_rate=avg_success,
                context_applicability=context_applicability,
                suggested_improvements=suggestions,
                last_updated=datetime.now().isoformat(),
                confidence_score=min(len(usages) / 10, 1.0)
            )
            
            patterns.append(pattern)
        
        return patterns
    
    def _analyze_context_applicability(self, usages: List[Dict]) -> Dict[str, float]:
        """Analisa aplicabilidade da regra em diferentes contextos"""
        context_scores = defaultdict(list)
        
        for usage in usages:
            context = usage["context"]
            score = usage["success_score"]
            
            # Extrair palavras-chave do contexto
            keywords = self._extract_context_keywords(context)
            for keyword in keywords:
                context_scores[keyword].append(score)
        
        # Calcular scores médios por contexto
        applicability = {}
        for keyword, scores in context_scores.items():
            if len(scores) >= 3:  # Mínimo de 3 usos para ser relevante
                applicability[keyword] = statistics.mean(scores)
        
        return applicability
    
    def _extract_context_keywords(self, context: Dict[str, Any]) -> List[str]:
        """Extrai palavras-chave do contexto"""
        keywords = []
        
        # Extrair de diferentes campos do contexto
        if "technologies" in context:
            keywords.extend(context["technologies"])
        
        if "task_type" in context:
            keywords.append(context["task_type"])
        
        if "complexity" in context:
            keywords.append(context["complexity"])
        
        if "user_request" in context:
            # Extrair palavras-chave do pedido do usuário
            request_words = re.findall(r'\b\w+\b', context["user_request"].lower())
            keywords.extend([w for w in request_words if len(w) > 3])
        
        return list(set(keywords))  # Remover duplicatas
    
    def _generate_rule_improvements(self, rule_file: str, usages: List[Dict]) -> List[str]:
        """Gera sugestões de melhoria para uma regra"""
        suggestions = []
        
        # Analisar feedback negativo
        negative_feedback = [u for u in usages if u["success_score"] < 0.5]
        if negative_feedback:
            suggestions.append("Considerar casos de uso com baixo sucesso")
        
        # Analisar contexto específico
        context_applicability = self._analyze_context_applicability(usages)
        low_applicability = [k for k, v in context_applicability.items() if v < 0.6]
        if low_applicability:
            suggestions.append(f"Melhorar aplicabilidade em contextos: {', '.join(low_applicability)}")
        
        # Analisar frequência de uso
        if len(usages) > 50:
            suggestions.append("Regra muito utilizada - considerar otimização")
        
        return suggestions
    
    def generate_rule_optimizations(self) -> List[RuleOptimization]:
        """Gera otimizações para regras baseado em padrões aprendidos"""
        optimizations = []
        patterns = self.analyze_rule_patterns()
        
        for pattern in patterns:
            if pattern.success_rate < self.min_success_rate_for_improvement:
                # Regra com baixo sucesso - gerar otimização
                optimization = self._create_rule_optimization(pattern)
                if optimization:
                    optimizations.append(optimization)
        
        return optimizations
    
    def _create_rule_optimization(self, pattern: RuleLearningPattern) -> Optional[RuleOptimization]:
        """Cria otimização para uma regra específica"""
        try:
            # Ler conteúdo atual da regra
            rule_content = self.get_all_rules().get(pattern.rule_file, "")
            if not rule_content:
                return None
            
            # Analisar seções da regra
            sections = self.parse_rule_content(rule_content)
            
            # Gerar sugestões baseadas no padrão
            suggestions = pattern.suggested_improvements
            if not suggestions:
                return None
            
            # Criar otimização
            optimization = RuleOptimization(
                rule_id=pattern.rule_id,
                optimization_type="modify",
                current_content=rule_content[:200] + "...",  # Primeiros 200 chars
                suggested_content=self._generate_improved_content(rule_content, suggestions),
                reasoning="Baseado em análise de padrões de uso e feedback",
                confidence=pattern.confidence_score,
                impact_score=1.0 - pattern.success_rate  # Maior impacto para regras com baixo sucesso
            )
            
            return optimization
            
        except Exception as e:
            print(f"Erro ao criar otimização para {pattern.rule_file}: {e}")
            return None
    
    def _generate_improved_content(self, current_content: str, suggestions: List[str]) -> str:
        """Gera conteúdo melhorado baseado em sugestões"""
        # Implementação básica - pode ser expandida
        improved_content = current_content
        
        for suggestion in suggestions:
            if "casos de uso com baixo sucesso" in suggestion:
                improved_content += "\n\n### ⚠️ Casos de Uso Específicos\n"
                improved_content += "- **Para casos de baixo sucesso**: Considere contexto específico\n"
                improved_content += "- **Validação adicional**: Verifique se a regra se aplica\n"
            
            if "melhorar aplicabilidade" in suggestion:
                improved_content += "\n\n### 🎯 Contextos de Aplicação\n"
                improved_content += "- **Contextos suportados**: Lista de contextos onde a regra se aplica\n"
                improved_content += "- **Exceções**: Casos onde a regra não deve ser aplicada\n"
        
        return improved_content
    
    def apply_rule_optimization(self, optimization: RuleOptimization) -> bool:
        """Aplica uma otimização de regra"""
        try:
            rule_file_path = self.rules_path / optimization.rule_id
            
            # Encontrar arquivo de regra correspondente
            for rule_file in self.rules_path.glob("*.md"):
                if hashlib.md5(rule_file.name.encode()).hexdigest()[:8] == optimization.rule_id:
                    rule_file_path = rule_file
                    break
            
            if not rule_file_path.exists():
                return False
            
            # Fazer backup da regra atual
            backup_path = self.rules_learning_path / f"{rule_file_path.stem}_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            with open(rule_file_path, 'r', encoding='utf-8') as f:
                current_content = f.read()
            
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(current_content)
            
            # Aplicar otimização
            with open(rule_file_path, 'w', encoding='utf-8') as f:
                f.write(optimization.suggested_content)
            
            # Registrar otimização aplicada
            self.rule_optimizations[optimization.rule_id] = {
                "timestamp": datetime.now().isoformat(),
                "optimization": asdict(optimization),
                "backup_file": str(backup_path),
                "applied": True
            }
            
            self.save_rule_optimizations()
            return True
            
        except Exception as e:
            print(f"Erro ao aplicar otimização: {e}")
            return False
    
    def get_rule_recommendations(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Obtém recomendações de regras baseado no contexto"""
        recommendations = []
        patterns = self.analyze_rule_patterns()
        
        for pattern in patterns:
            # Calcular relevância para o contexto atual
            relevance_score = self._calculate_context_relevance(pattern, context)
            
            if relevance_score > 0.6:  # Threshold de relevância
                recommendation = {
                    "rule_file": pattern.rule_file,
                    "relevance_score": relevance_score,
                    "success_rate": pattern.success_rate,
                    "usage_frequency": pattern.usage_frequency,
                    "suggestions": pattern.suggested_improvements
                }
                recommendations.append(recommendation)
        
        # Ordenar por relevância
        recommendations.sort(key=lambda x: x["relevance_score"], reverse=True)
        return recommendations[:5]  # Top 5 recomendações
    
    def _calculate_context_relevance(self, pattern: RuleLearningPattern, context: Dict[str, Any]) -> float:
        """Calcula relevância de uma regra para o contexto atual"""
        context_keywords = self._extract_context_keywords(context)
        
        if not context_keywords:
            return 0.5  # Relevância neutra
        
        # Calcular sobreposição com contextos conhecidos
        overlap_score = 0.0
        for keyword in context_keywords:
            if keyword in pattern.context_applicability:
                overlap_score += pattern.context_applicability[keyword]
        
        if context_keywords:
            overlap_score /= len(context_keywords)
        
        return overlap_score
    
    def generate_rules_learning_report(self) -> Dict[str, Any]:
        """Gera relatório de aprendizado das regras"""
        patterns = self.analyze_rule_patterns()
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "total_rules_analyzed": len(patterns),
            "patterns": [asdict(p) for p in patterns],
            "optimizations_generated": len(self.generate_rule_optimizations()),
            "usage_statistics": {
                "total_usage_events": len(self.rule_usage_log["usage"]),
                "unique_rules_used": len(set(u["rule_file"] for u in self.rule_usage_log["usage"])),
                "avg_success_rate": statistics.mean([p.success_rate for p in patterns]) if patterns else 0.0
            },
            "recommendations": {
                "high_priority_optimizations": [p for p in patterns if p.success_rate < 0.6],
                "well_performing_rules": [p for p in patterns if p.success_rate > 0.8]
            }
        }
        
        return report 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = GitautomationModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script rules_learning_integration.py executado com sucesso via módulo tools.git_automation")
    else:
        print(f"❌ Erro na execução do script rules_learning_integration.py via módulo tools.git_automation")

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
- **Nome**: migrated_rules_learning_integration
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

