# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: optimization_engine.py
Módulo de Destino: tools.git_automation
Data de Migração: 2025-08-01 12:21:44

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import GitautomationModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motor de Otimização para Auto-Aprendizado
Aplica otimizações automáticas baseadas nos padrões aprendidos
"""

import json
from datetime import datetime, timedelta

@dataclass
class OptimizationRule:
    """Regra de otimização"""
    rule_id: str
    rule_type: str  # 'agent_selection', 'workflow_optimization', 'context_improvement'
    trigger_conditions: Dict[str, Any]
    optimization_actions: List[Dict[str, Any]]
    confidence_score: float
    success_rate: float
    usage_count: int
    last_updated: str

@dataclass
class OptimizationResult:
    """Resultado de uma otimização aplicada"""
    optimization_id: str
    rule_id: str
    interaction_id: str
    optimization_type: str
    applied_changes: Dict[str, Any]
    expected_improvement: float
    actual_improvement: Optional[float] = None
    timestamp: str = None

class OptimizationEngine:
    """Motor de otimização automática"""
    
    def __init__(self, models_path: Path):
        self.models_path = models_path
        self.rules_file = models_path / "optimization_rules.json"
        self.results_file = models_path / "optimization_results.json"
        
        # Carregar dados existentes
        self.optimization_rules = self.load_optimization_rules()
        self.optimization_results = self.load_optimization_results()
        
        # Configurações
        self.min_confidence_threshold = 0.7
        self.min_success_rate = 0.6
        self.max_rules_per_type = 20
        
        # Cache de otimizações
        self.optimization_cache = {}
        self.cache_timestamp = None
    
    def load_optimization_rules(self) -> Dict[str, Any]:
        """Carrega regras de otimização do arquivo"""
        if self.rules_file.exists():
            with open(self.rules_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def load_optimization_results(self) -> Dict[str, Any]:
        """Carrega resultados de otimização do arquivo"""
        if self.results_file.exists():
            with open(self.results_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def save_optimization_rules(self):
        """Salva regras de otimização no arquivo"""
        with open(self.rules_file, 'w', encoding='utf-8') as f:
            json.dump(self.optimization_rules, f, indent=2, ensure_ascii=False)
    
    def save_optimization_results(self):
        """Salva resultados de otimização no arquivo"""
        with open(self.results_file, 'w', encoding='utf-8') as f:
            json.dump(self.optimization_results, f, indent=2, ensure_ascii=False)
    
    def apply_optimizations(self, patterns: List[Any]) -> List[Dict[str, Any]]:
        """Aplica otimizações baseadas nos padrões aprendidos"""
        optimizations = []
        
        print(f"⚡ Aplicando otimizações baseadas em {len(patterns)} padrões...")
        
        # 1. Gerar regras de otimização dos padrões
        new_rules = self._generate_optimization_rules(patterns)
        
        # 2. Aplicar regras existentes
        for rule_id, rule in self.optimization_rules.items():
            if self._should_apply_rule(rule):
                optimization = self._apply_optimization_rule(rule)
                if optimization:
                    optimizations.append(optimization)
        
        # 3. Aplicar novas regras
        for rule in new_rules:
            if rule.confidence_score >= self.min_confidence_threshold:
                optimization = self._apply_optimization_rule(rule)
                if optimization:
                    optimizations.append(optimization)
        
        # 4. Salvar regras atualizadas
        self._update_optimization_rules(new_rules)
        self.save_optimization_rules()
        
        print(f"✅ Aplicadas {len(optimizations)} otimizações")
        return optimizations
    
    def _generate_optimization_rules(self, patterns: List[Any]) -> List[OptimizationRule]:
        """Gera regras de otimização a partir dos padrões"""
        rules = []
        
        for pattern in patterns:
            if pattern.pattern_type == 'success' and pattern.confidence_score >= self.min_confidence_threshold:
                # Regra para replicar sucesso
                rule = self._create_success_replication_rule(pattern)
                if rule:
                    rules.append(rule)
            
            elif pattern.pattern_type == 'failure' and pattern.confidence_score >= self.min_confidence_threshold:
                # Regra para evitar falhas
                rule = self._create_failure_avoidance_rule(pattern)
                if rule:
                    rules.append(rule)
            
            elif pattern.pattern_type == 'optimization' and pattern.confidence_score >= self.min_confidence_threshold:
                # Regra de otimização específica
                rule = self._create_specific_optimization_rule(pattern)
                if rule:
                    rules.append(rule)
        
        return rules
    
    def _create_success_replication_rule(self, pattern: Any) -> Optional[OptimizationRule]:
        """Cria regra para replicar padrões de sucesso"""
        rule_id = f"success_replication_{pattern.pattern_id}"
        
        # Condições de trigger
        trigger_conditions = {
            'context_keywords': pattern.context_keywords,
            'min_similarity': 0.7,
            'pattern_type': 'success'
        }
        
        # Ações de otimização
        optimization_actions = []
        
        # Ação: Selecionar agentes específicos
        if pattern.agent_combinations:
            optimization_actions.append({
                'action_type': 'agent_selection',
                'agents': pattern.agent_combinations[0],
                'priority': 'high'
            })
        
        # Ação: Usar workflow específico
        if pattern.workflow_types:
            optimization_actions.append({
                'action_type': 'workflow_selection',
                'workflow': pattern.workflow_types[0],
                'priority': 'medium'
            })
        
        # Ação: Aplicar configurações específicas
        optimization_actions.append({
            'action_type': 'configuration_optimization',
            'settings': {
                'expected_success_rate': pattern.success_rate,
                'target_execution_time': pattern.avg_execution_time
            },
            'priority': 'low'
        })
        
        return OptimizationRule(
            rule_id=rule_id,
            rule_type='success_replication',
            trigger_conditions=trigger_conditions,
            optimization_actions=optimization_actions,
            confidence_score=pattern.confidence_score,
            success_rate=pattern.success_rate,
            usage_count=0,
            last_updated=datetime.now().isoformat()
        )
    
    def _create_failure_avoidance_rule(self, pattern: Any) -> Optional[OptimizationRule]:
        """Cria regra para evitar padrões de falha"""
        rule_id = f"failure_avoidance_{pattern.pattern_id}"
        
        # Condições de trigger
        trigger_conditions = {
            'context_keywords': pattern.context_keywords,
            'min_similarity': 0.6,
            'pattern_type': 'failure',
            'avoid_failure': True
        }
        
        # Ações de otimização
        optimization_actions = []
        
        # Ação: Evitar combinações problemáticas
        if hasattr(pattern, 'agent_combinations') and pattern.agent_combinations:
            optimization_actions.append({
                'action_type': 'agent_avoidance',
                'avoid_agents': pattern.agent_combinations[0],
                'priority': 'high'
            })
        
        # Ação: Usar workflow alternativo
        optimization_actions.append({
            'action_type': 'workflow_alternative',
            'fallback_workflow': 'safe_workflow',
            'priority': 'medium'
        })
        
        # Ação: Aplicar verificações adicionais
        optimization_actions.append({
            'action_type': 'additional_validation',
            'validation_rules': ['context_check', 'agent_compatibility'],
            'priority': 'high'
        })
        
        return OptimizationRule(
            rule_id=rule_id,
            rule_type='failure_avoidance',
            trigger_conditions=trigger_conditions,
            optimization_actions=optimization_actions,
            confidence_score=pattern.confidence_score,
            success_rate=1.0 - pattern.success_rate,  # Inverter para otimização
            usage_count=0,
            last_updated=datetime.now().isoformat()
        )
    
    def _create_specific_optimization_rule(self, pattern: Any) -> Optional[OptimizationRule]:
        """Cria regra de otimização específica"""
        rule_id = f"specific_optimization_{pattern.pattern_id}"
        
        # Condições de trigger
        trigger_conditions = {
            'context_keywords': pattern.context_keywords,
            'min_similarity': 0.8,
            'pattern_type': 'optimization'
        }
        
        # Ações de otimização específicas
        optimization_actions = []
        
        if hasattr(pattern, 'optimization_triggers'):
            for trigger in pattern.optimization_triggers:
                optimization_actions.append({
                    'action_type': 'triggered_optimization',
                    'trigger': trigger,
                    'optimization_type': 'performance',
                    'priority': 'high'
                })
        
        # Ação: Otimização de performance
        optimization_actions.append({
            'action_type': 'performance_optimization',
            'target_execution_time': pattern.avg_execution_time * 0.8,  # 20% mais rápido
            'priority': 'medium'
        })
        
        return OptimizationRule(
            rule_id=rule_id,
            rule_type='specific_optimization',
            trigger_conditions=trigger_conditions,
            optimization_actions=optimization_actions,
            confidence_score=pattern.confidence_score,
            success_rate=pattern.success_rate,
            usage_count=0,
            last_updated=datetime.now().isoformat()
        )
    
    def _should_apply_rule(self, rule: Dict[str, Any]) -> bool:
        """Verifica se uma regra deve ser aplicada"""
        # Verificar confiança mínima
        if rule.get('confidence_score', 0) < self.min_confidence_threshold:
            return False
        
        # Verificar taxa de sucesso mínima
        if rule.get('success_rate', 0) < self.min_success_rate:
            return False
        
        # Verificar se não foi usada recentemente (evitar spam)
        last_updated = datetime.fromisoformat(rule.get('last_updated', '2020-01-01T00:00:00'))
        if (datetime.now() - last_updated).seconds < 300:  # 5 minutos
            return False
        
        return True
    
    def _apply_optimization_rule(self, rule: OptimizationRule) -> Optional[Dict[str, Any]]:
        """Aplica uma regra de otimização"""
        optimization_id = f"opt_{rule.rule_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Preparar mudanças a serem aplicadas
        applied_changes = {}
        
        for action in rule.optimization_actions:
            action_type = action.get('action_type')
            
            if action_type == 'agent_selection':
                applied_changes['selected_agents'] = action.get('agents', [])
            
            elif action_type == 'workflow_selection':
                applied_changes['selected_workflow'] = action.get('workflow')
            
            elif action_type == 'configuration_optimization':
                applied_changes['optimization_settings'] = action.get('settings', {})
            
            elif action_type == 'agent_avoidance':
                applied_changes['avoided_agents'] = action.get('avoid_agents', [])
            
            elif action_type == 'workflow_alternative':
                applied_changes['fallback_workflow'] = action.get('fallback_workflow')
            
            elif action_type == 'additional_validation':
                applied_changes['validation_rules'] = action.get('validation_rules', [])
            
            elif action_type == 'performance_optimization':
                applied_changes['performance_target'] = action.get('target_execution_time')
        
        # Criar resultado de otimização
        result = OptimizationResult(
            optimization_id=optimization_id,
            rule_id=rule.rule_id,
            interaction_id="",  # Será preenchido quando aplicado
            optimization_type=rule.rule_type,
            applied_changes=applied_changes,
            expected_improvement=rule.success_rate,
            timestamp=datetime.now().isoformat()
        )
        
        # Salvar resultado
        self.optimization_results[optimization_id] = asdict(result)
        self.save_optimization_results()
        
        # Atualizar contador de uso da regra
        rule.usage_count += 1
        rule.last_updated = datetime.now().isoformat()
        
        return {
            'optimization_id': optimization_id,
            'rule_id': rule.rule_id,
            'type': rule.rule_type,
            'changes': applied_changes,
            'expected_improvement': rule.success_rate,
            'confidence': rule.confidence_score
        }
    
    def apply_pattern_optimization(self, pattern: Any, interaction_data: Any) -> Optional[Dict[str, Any]]:
        """Aplica otimização baseada em um padrão específico"""
        # Verificar se o padrão é aplicável
        if pattern.confidence_score < self.min_confidence_threshold:
            return None
        
        # Criar regra temporária
        if pattern.pattern_type == 'success':
            rule = self._create_success_replication_rule(pattern)
        elif pattern.pattern_type == 'failure':
            rule = self._create_failure_avoidance_rule(pattern)
        elif pattern.pattern_type == 'optimization':
            rule = self._create_specific_optimization_rule(pattern)
        else:
            return None
        
        if not rule:
            return None
        
        # Aplicar regra
        optimization = self._apply_optimization_rule(rule)
        
        if optimization:
            # Associar com a interação atual
            optimization['interaction_id'] = getattr(interaction_data, 'interaction_id', 'unknown')
            return optimization
        
        return None
    
    def _update_optimization_rules(self, new_rules: List[OptimizationRule]):
        """Atualiza regras de otimização"""
        # Adicionar novas regras
        for rule in new_rules:
            self.optimization_rules[rule.rule_id] = asdict(rule)
        
        # Limitar número de regras por tipo
        self._limit_rules_per_type()
        
        # Remover regras obsoletas
        self._remove_obsolete_rules()
    
    def _limit_rules_per_type(self):
        """Limita número de regras por tipo"""
        rules_by_type = defaultdict(list)
        
        for rule_id, rule in self.optimization_rules.items():
            rules_by_type[rule.get('rule_type', 'unknown')].append((rule_id, rule))
        
        for rule_type, rules in rules_by_type.items():
            if len(rules) > self.max_rules_per_type:
                # Manter regras com maior confiança e sucesso
                rules.sort(key=lambda x: (x[1].get('confidence_score', 0), x[1].get('success_rate', 0)), reverse=True)
                rules_to_remove = rules[self.max_rules_per_type:]
                
                for rule_id, _ in rules_to_remove:
                    del self.optimization_rules[rule_id]
    
    def _remove_obsolete_rules(self):
        """Remove regras obsoletas"""
        cutoff_date = datetime.now() - timedelta(days=30)
        rules_to_remove = []
        
        for rule_id, rule in self.optimization_rules.items():
            last_updated = datetime.fromisoformat(rule.get('last_updated', '2020-01-01T00:00:00'))
            
            # Remover regras antigas com baixo uso
            if (last_updated < cutoff_date and 
                rule.get('usage_count', 0) < 3 and 
                rule.get('success_rate', 0) < 0.5):
                rules_to_remove.append(rule_id)
        
        for rule_id in rules_to_remove:
            del self.optimization_rules[rule_id]
    
    def get_optimization_stats(self) -> Dict[str, Any]:
        """Retorna estatísticas de otimização"""
        total_rules = len(self.optimization_rules)
        total_results = len(self.optimization_results)
        
        # Estatísticas por tipo de regra
        rules_by_type = defaultdict(int)
        for rule in self.optimization_rules.values():
            rules_by_type[rule.get('rule_type', 'unknown')] += 1
        
        # Estatísticas de sucesso
        successful_optimizations = [
            r for r in self.optimization_results.values()
            if r.get('actual_improvement', 0) > 0
        ]
        
        success_rate = len(successful_optimizations) / total_results if total_results > 0 else 0
        
        # Regras mais usadas
        most_used_rules = sorted(
            self.optimization_rules.items(),
            key=lambda x: x[1].get('usage_count', 0),
            reverse=True
        )[:10]
        
        return {
            'total_rules': total_rules,
            'total_optimizations': total_results,
            'success_rate': success_rate,
            'rules_by_type': dict(rules_by_type),
            'most_used_rules': [
                {
                    'rule_id': rule_id,
                    'rule_type': rule.get('rule_type'),
                    'usage_count': rule.get('usage_count', 0),
                    'success_rate': rule.get('success_rate', 0)
                }
                for rule_id, rule in most_used_rules
            ]
        }
    
    def update_optimization_result(self, optimization_id: str, actual_improvement: float):
        """Atualiza resultado de otimização com melhoria real"""
        if optimization_id in self.optimization_results:
            self.optimization_results[optimization_id]['actual_improvement'] = actual_improvement
            self.save_optimization_results()
            
            # Atualizar regra associada
            rule_id = self.optimization_results[optimization_id].get('rule_id')
            if rule_id and rule_id in self.optimization_rules:
                # Ajustar taxa de sucesso da regra
                rule = self.optimization_rules[rule_id]
                current_success_rate = rule.get('success_rate', 0)
                
                # Média ponderada
                usage_count = rule.get('usage_count', 1)
                new_success_rate = (current_success_rate * (usage_count - 1) + actual_improvement) / usage_count
                
                rule['success_rate'] = new_success_rate
                self.save_optimization_rules() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = GitautomationModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script optimization_engine.py executado com sucesso via módulo tools.git_automation")
    else:
        print(f"❌ Erro na execução do script optimization_engine.py via módulo tools.git_automation")
