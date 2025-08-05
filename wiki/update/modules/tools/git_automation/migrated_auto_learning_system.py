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
Script Migrado: auto_learning_system.py
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
Sistema de Auto-Aprendizado BMAD
Sistema principal que coordena coleta de dados, análise de padrões e otimização automática
"""

import json
import time
import threading
from datetime import datetime, timedelta
import statistics

# Importar componentes do sistema

@dataclass
class InteractionData:
    """Dados de uma interação do sistema"""
    timestamp: str
    user_request: str
    context_detected: Dict[str, Any]
    agents_selected: List[str]
    workflow_executed: str
    execution_time: float
    success_score: float
    user_feedback: Optional[str] = None
    error_message: Optional[str] = None
    optimization_applied: bool = False
    rules_used: Optional[List[str]] = None

@dataclass
class LearningPattern:
    """Padrão aprendido pelo sistema"""
    pattern_id: str
    pattern_type: str  # 'success', 'failure', 'optimization'
    context_keywords: List[str]
    agent_combinations: List[List[str]]
    workflow_types: List[str]
    success_rate: float
    avg_execution_time: float
    confidence_score: float
    last_updated: str
    usage_count: int

class AutoLearningSystem:
    """Sistema principal de auto aprendizado BMAD"""
    
    def __init__(self, base_path: str = "wiki"):
        self.base_path = Path(base_path)
        self.auto_learning_path = self.base_path / "bmad" / "auto_learning"
        self.data_path = self.auto_learning_path / "data"
        self.models_path = self.auto_learning_path / "models"
        self.logs_path = self.auto_learning_path / "logs"
        
        # Criar estrutura de pastas
        self.create_directory_structure()
        
        # Inicializar componentes
        self.data_collector = DataCollector(self.data_path)
        self.pattern_analyzer = PatternAnalyzer(self.models_path)
        self.feedback_system = FeedbackSystem(self.logs_path)
        self.optimization_engine = OptimizationEngine(self.models_path)
        self.visualization_interface = VisualizationInterface(self.auto_learning_path)
        self.rules_learning = RulesLearningIntegration(self.base_path)
        
        # Estado do sistema
        self.is_learning = False
        self.learning_thread = None
        self.interaction_buffer = deque(maxlen=1000)
        self.patterns_cache = {}
        self.optimization_history = []
        
        # Configurações
        self.config = self.load_config()
        self.learning_interval = self.config.get('learning_interval', 300)  # 5 minutos
        self.min_interactions_for_learning = self.config.get('min_interactions', 10)
        self.confidence_threshold = self.config.get('confidence_threshold', 0.7)
        
        # Iniciar sistema de aprendizado em background
        self.start_learning_background()
    
    def create_directory_structure(self):
        """Cria estrutura de pastas necessária"""
        directories = [
            self.data_path,
            self.models_path,
            self.logs_path,
            self.auto_learning_path / "reports",
            self.auto_learning_path / "visualizations"
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
    
    def load_config(self) -> Dict[str, Any]:
        """Carrega configuração do sistema"""
        config_file = self.auto_learning_path / "config.json"
        if config_file.exists():
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Configuração padrão
            default_config = {
                'learning_interval': 300,
                'min_interactions': 10,
                'confidence_threshold': 0.7,
                'max_patterns': 100,
                'optimization_enabled': True,
                'feedback_enabled': True,
                'visualization_enabled': True
            }
            self.save_config(default_config)
            return default_config
    
    def save_config(self, config: Dict[str, Any]):
        """Salva configuração do sistema"""
        config_file = self.auto_learning_path / "config.json"
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
    
    def start_learning_background(self):
        """Inicia thread de aprendizado em background"""
        if not self.is_learning:
            self.is_learning = True
            self.learning_thread = threading.Thread(target=self._learning_loop, daemon=True)
            self.learning_thread.start()
            print("🧠 Sistema de auto aprendizado iniciado em background")
    
    def stop_learning_background(self):
        """Para thread de aprendizado"""
        self.is_learning = False
        if self.learning_thread:
            self.learning_thread.join(timeout=5)
        print("🛑 Sistema de auto aprendizado parado")
    
    def _learning_loop(self):
        """Loop principal de aprendizado em background"""
        while self.is_learning:
            try:
                # Verificar se há dados suficientes para aprendizado
                if len(self.interaction_buffer) >= self.min_interactions_for_learning:
                    self._perform_learning_cycle()
                
                # Aguardar próximo ciclo
                time.sleep(self.learning_interval)
                
            except Exception as e:
                print(f"❌ Erro no loop de aprendizado: {e}")
                time.sleep(60)  # Aguardar 1 minuto antes de tentar novamente
    
    def _perform_learning_cycle(self):
        """Executa um ciclo completo de aprendizado"""
        print("🧠 Iniciando ciclo de aprendizado...")
        
        # 1. Coletar dados do buffer
        interactions = list(self.interaction_buffer)
        
        # 2. Analisar padrões
        patterns = self.pattern_analyzer.analyze_patterns(interactions)
        
        # 3. Aplicar otimizações
        optimizations = self.optimization_engine.apply_optimizations(patterns)
        
        # 4. Atualizar cache de padrões
        self.patterns_cache.update({p.pattern_id: p for p in patterns})
        
        # 5. Salvar resultados
        self._save_learning_results(patterns, optimizations)
        
        # 6. Limpar buffer processado
        self.interaction_buffer.clear()
        
        print(f"✅ Ciclo de aprendizado concluído: {len(patterns)} padrões identificados")
    
    def _save_learning_results(self, patterns: List[LearningPattern], optimizations: List[Dict]):
        """Salva resultados do aprendizado"""
        timestamp = datetime.now().isoformat()
        
        # Salvar padrões
        patterns_file = self.models_path / f"patterns_{timestamp[:10]}.json"
        with open(patterns_file, 'w', encoding='utf-8') as f:
            json.dump([asdict(p) for p in patterns], f, indent=2, ensure_ascii=False)
        
        # Salvar otimizações
        optimizations_file = self.models_path / f"optimizations_{timestamp[:10]}.json"
        with open(optimizations_file, 'w', encoding='utf-8') as f:
            json.dump(optimizations, f, indent=2, ensure_ascii=False)
        
        # Atualizar histórico
        self.optimization_history.append({
            'timestamp': timestamp,
            'patterns_count': len(patterns),
            'optimizations_count': len(optimizations)
        })
    
    def record_interaction(self, interaction_data: InteractionData):
        """Registra uma nova interação no sistema"""
        # Adicionar ao buffer para processamento
        self.interaction_buffer.append(interaction_data)
        
        # Salvar dados imediatamente
        self.data_collector.save_interaction(interaction_data)
        
        # Verificar se há otimizações aplicáveis
        if self.config.get('optimization_enabled', True):
            self._check_immediate_optimizations(interaction_data)
        
        # Registrar uso de regras se aplicável
        if hasattr(interaction_data, 'rules_used'):
            for rule_file in interaction_data.rules_used:
                self.rules_learning.record_rule_usage(
                    rule_file, 
                    interaction_data.context_detected,
                    interaction_data.success_score,
                    interaction_data.user_feedback
                )
    
    def _check_immediate_optimizations(self, interaction_data: InteractionData):
        """Verifica otimizações que podem ser aplicadas imediatamente"""
        # Buscar padrões similares no cache
        similar_patterns = self._find_similar_patterns(interaction_data)
        
        for pattern in similar_patterns:
            if pattern.confidence_score >= self.confidence_threshold:
                # Aplicar otimização imediata
                optimization = self.optimization_engine.apply_pattern_optimization(pattern, interaction_data)
                if optimization:
                    print(f"⚡ Otimização aplicada: {optimization['type']}")
    
    def _find_similar_patterns(self, interaction_data: InteractionData) -> List[LearningPattern]:
        """Encontra padrões similares à interação atual"""
        similar_patterns = []
        
        for pattern in self.patterns_cache.values():
            # Verificar similaridade de contexto
            context_similarity = self._calculate_context_similarity(
                interaction_data.context_detected, pattern.context_keywords
            )
            
            if context_similarity > 0.5:  # Threshold de similaridade
                similar_patterns.append(pattern)
        
        # Ordenar por similaridade
        similar_patterns.sort(key=lambda p: p.confidence_score, reverse=True)
        return similar_patterns[:5]  # Retornar top 5
    
    def _calculate_context_similarity(self, context: Dict, keywords: List[str]) -> float:
        """Calcula similaridade entre contexto e palavras-chave"""
        if not keywords:
            return 0.0
        
        # Extrair palavras do contexto
        context_text = " ".join(str(v) for v in context.values()).lower()
        context_words = set(context_text.split())
        
        # Calcular similaridade
        keyword_set = set(keywords)
        intersection = context_words.intersection(keyword_set)
        union = context_words.union(keyword_set)
        
        if not union:
            return 0.0
        
        return len(intersection) / len(union)
    
    def get_learning_stats(self) -> Dict[str, Any]:
        """Retorna estatísticas do sistema de aprendizado"""
        return {
            'total_interactions': len(self.interaction_buffer) + self.data_collector.get_total_interactions(),
            'patterns_learned': len(self.patterns_cache),
            'optimizations_applied': len(self.optimization_history),
            'learning_active': self.is_learning,
            'confidence_threshold': self.confidence_threshold,
            'last_optimization': self.optimization_history[-1] if self.optimization_history else None
        }
    
    def get_recommendations(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Retorna recomendações baseadas no contexto atual"""
        recommendations = []
        
        # Buscar padrões relevantes
        relevant_patterns = self._find_similar_patterns(InteractionData(
            timestamp=datetime.now().isoformat(),
            user_request="",
            context_detected=context,
            agents_selected=[],
            workflow_executed="",
            execution_time=0.0,
            success_score=0.0
        ))
        
        for pattern in relevant_patterns:
            if pattern.confidence_score >= self.confidence_threshold:
                recommendations.append({
                    'type': 'pattern_based',
                    'pattern_id': pattern.pattern_id,
                    'confidence': pattern.confidence_score,
                    'suggested_agents': pattern.agent_combinations[0] if pattern.agent_combinations else [],
                    'suggested_workflow': pattern.workflow_types[0] if pattern.workflow_types else None,
                    'expected_success_rate': pattern.success_rate
                })
        
        return recommendations
    
    def update_feedback(self, interaction_id: str, feedback: str, score: float):
        """Atualiza feedback de uma interação"""
        self.feedback_system.record_feedback(interaction_id, feedback, score)
        
        # Recalcular padrões se necessário
        if score < 0.5:  # Feedback negativo
            self._trigger_relearning()
    
    def _trigger_relearning(self):
        """Dispara relearning baseado em feedback negativo"""
        print("🔄 Feedback negativo detectado - disparando relearning...")
        
        # Forçar ciclo de aprendizado
        if len(self.interaction_buffer) > 0:
            self._perform_learning_cycle()
    
    def generate_learning_report(self) -> Dict[str, Any]:
        """Gera relatório completo do sistema de aprendizado"""
        stats = self.get_learning_stats()
        
        # Análise de padrões
        pattern_analysis = {
            'success_patterns': len([p for p in self.patterns_cache.values() if p.pattern_type == 'success']),
            'failure_patterns': len([p for p in self.patterns_cache.values() if p.pattern_type == 'failure']),
            'optimization_patterns': len([p for p in self.patterns_cache.values() if p.pattern_type == 'optimization']),
            'avg_confidence': statistics.mean([p.confidence_score for p in self.patterns_cache.values()]) if self.patterns_cache else 0.0
        }
        
        # Análise de performance
        performance_analysis = {
            'avg_execution_time': statistics.mean([p.avg_execution_time for p in self.patterns_cache.values()]) if self.patterns_cache else 0.0,
    
    
    
    
            'optimizations_applied': len(self.optimization_history),
            'learning_cycles': len(self.optimization_history)
        }
        
        return {
            'timestamp': datetime.now().isoformat(),
            'stats': stats,
            'pattern_analysis': pattern_analysis,
            'performance_analysis': performance_analysis,
            'recommendations': self._generate_system_recommendations(),
            'rules_learning': self.rules_learning.generate_rules_learning_report()
        }
    
    def _generate_system_recommendations(self) -> List[str]:
        """Gera recomendações para melhorar o sistema"""
        recommendations = []
        
        if len(self.patterns_cache) < 5:
            recommendations.append("Coletar mais dados para melhorar aprendizado")
        
        avg_confidence = statistics.mean([p.confidence_score for p in self.patterns_cache.values()]) if self.patterns_cache else 0.0
        if avg_confidence < 0.6:
            recommendations.append("Ajustar threshold de confiança para melhorar precisão")
        
        if len(self.optimization_history) > 0:
            recent_optimizations = [h for h in self.optimization_history if h['timestamp'] > (datetime.now() - timedelta(days=1)).isoformat()]
            if len(recent_optimizations) < 2:
                recommendations.append("Sistema pode se beneficiar de mais otimizações")
        
        return recommendations
    
    def shutdown(self):
        """Desliga o sistema de aprendizado"""
        print("🛑 Desligando sistema de auto aprendizado...")
        
        # Parar thread de aprendizado
        self.stop_learning_background()
        
        # Salvar estado atual
        self._save_current_state()
        
        print("✅ Sistema de auto aprendizado desligado")
    
    def _save_current_state(self):
        """Salva estado atual do sistema"""
        state = {
            'patterns_cache': {k: asdict(v) for k, v in self.patterns_cache.items()},
            'optimization_history': self.optimization_history,
            'config': self.config,
            'timestamp': datetime.now().isoformat()
        }
        
        state_file = self.auto_learning_path / "system_state.json"
        with open(state_file, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=2, ensure_ascii=False)
    
    def get_rule_recommendations(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Obtém recomendações de regras baseado no contexto"""
        return self.rules_learning.get_rule_recommendations(context)
    
    def apply_rule_optimizations(self) -> List[Dict[str, Any]]:
        """Aplica otimizações de regras aprendidas"""
        optimizations = self.rules_learning.generate_rule_optimizations()
        applied_optimizations = []
        
        for optimization in optimizations:
            if optimization.confidence > 0.7:  # Apenas otimizações com alta confiança
                success = self.rules_learning.apply_rule_optimization(optimization)
                if success:
                    applied_optimizations.append({
                        'rule_id': optimization.rule_id,
                        'type': optimization.optimization_type,
                        'confidence': optimization.confidence,
                        'impact_score': optimization.impact_score
                    })
        
        return applied_optimizations
    
    def analyze_rule_patterns(self) -> Dict[str, Any]:
        """Analisa padrões de uso das regras"""
        return self.rules_learning.analyze_rule_patterns() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = GitautomationModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script auto_learning_system.py executado com sucesso via módulo tools.git_automation")
    else:
        print(f"❌ Erro na execução do script auto_learning_system.py via módulo tools.git_automation")

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
- **Nome**: migrated_auto_learning_system
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

