from unicode_aliases import *
# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
MAX_ITEMS = 100
MAX_SIZE = 1000

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: advanced_prompt_system.py
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
Sistema Avançado de Engenharia de Prompt BMAD
Implementa técnicas avançadas como Tree-of-Thought, Self-Consistency e otimização automática
"""

import json
import re
import hashlib
from datetime import datetime, timedelta
import statistics

@dataclass
class PromptOptimization:
    """Otimização de prompt"""
    original_prompt: str
    optimized_prompt: str
    technique_applied: str
    confidence_score: float
    reasoning: str
    expected_improvement: float

@dataclass
class ThoughtNode:
    """Nó de pensamento para Tree-of-Thought"""
    thought_id: str
    content: str
    parent_id: Optional[str] = None
    children: List[str] = None
    evaluation: str = "pending"  # pending, possible, correct, impossible
    confidence: float = 0.0
    depth: int = 0

@dataclass
class PromptEvaluation:
    """Avaliação de prompt"""
    prompt_id: str
    clarity_score: float
    specificity_score: float
    completeness_score: float
    overall_score: float
    suggestions: List[str]
    timestamp: str

class AdvancedPromptSystem:
    """Sistema avançado de engenharia de prompt"""
    
    def __init__(self, base_path: str = "wiki"):
        self.base_path = Path(base_path)
        self.prompt_engineering_path = self.base_path / "bmad" / "prompt_engineering"
        self.data_path = self.prompt_engineering_path / "data"
        self.models_path = self.prompt_engineering_path / "models"
        
        # Criar estrutura de pastas
        self.create_directory_structure()
        
        # Configurações
        self.config = self.load_config()
        self.max_thought_depth = self.config.get('max_thought_depth', 5)
        self.consistency_threshold = self.config.get('consistency_threshold', 0.7)
        self.optimization_threshold = self.config.get('optimization_threshold', 0.6)
        
        # Cache de otimizações
        self.optimization_cache = {}
        self.evaluation_cache = {}
        
        # Histórico de prompts
        self.prompt_history = deque(maxlen=1000)
    
    def create_directory_structure(self):
        """Cria estrutura de pastas necessária"""
        directories = [
            self.data_path,
            self.models_path,
            self.prompt_engineering_path / "logs",
            self.prompt_engineering_path / "evaluations"
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
    
    def load_config(self) -> Dict[str, Any]:
        """Carrega configurações do sistema"""
        config_file = self.prompt_engineering_path / "config.json"
        
        if config_file.exists():
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        # Configuração padrão
        default_config = {
            'max_thought_depth': 5,
            'consistency_threshold': 0.7,
            'optimization_threshold': 0.6,
            'enable_tree_of_thought': True,
            'enable_self_consistency': True,
            'enable_generated_knowledge': True,
            'max_optimization_attempts': 3,
            'evaluation_metrics': ['clarity', 'specificity', 'completeness']
        }
        
        self.save_config(default_config)
        return default_config
    
    def save_config(self, config: Dict[str, Any]):
        """Salva configurações do sistema"""
        config_file = self.prompt_engineering_path / "config.json"
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
    
    def optimize_prompt(self, original_prompt: str, context: Dict[str, Any] = None) -> PromptOptimization:
        """Otimiza um prompt usando técnicas avançadas"""
        
        # Verificar cache
        prompt_hash = hashlib.md5(original_prompt.encode()).hexdigest()
        if prompt_hash in self.optimization_cache:
            return self.optimization_cache[prompt_hash]
        
        # Avaliar prompt original
        evaluation = self.evaluate_prompt(original_prompt)
        
        # Determinar técnica de otimização
        optimization_technique = self._select_optimization_technique(evaluation, context)
        
        # Aplicar otimização
        optimized_prompt = self._apply_optimization_technique(
            original_prompt, optimization_technique, context
        )
        
        # Criar otimização
        optimization = PromptOptimization(
            original_prompt=original_prompt,
            optimized_prompt=optimized_prompt,
            technique_applied=optimization_technique,
            confidence_score=self._calculate_optimization_confidence(evaluation),
            reasoning=self._generate_optimization_reasoning(evaluation, optimization_technique),
            expected_improvement=self._estimate_improvement(evaluation)
        )
        
        # Salvar no cache
        self.optimization_cache[prompt_hash] = optimization
        
        # Registrar no histórico
        self.prompt_history.append({
            'timestamp': datetime.now().isoformat(),
            'original': original_prompt,
            'optimized': optimized_prompt,
            'technique': optimization_technique,
            'confidence': optimization.confidence_score
        })
        
        return optimization
    
    def evaluate_prompt(self, prompt: str) -> PromptEvaluation:
        """Avalia a qualidade de um prompt"""
        
        # Verificar cache
        prompt_hash = hashlib.md5(prompt.encode()).hexdigest()
        if prompt_hash in self.evaluation_cache:
            return self.evaluation_cache[prompt_hash]
        
        # Calcular métricas
        clarity_score = self._calculate_clarity_score(prompt)
        specificity_score = self._calculate_specificity_score(prompt)
        completeness_score = self._calculate_completeness_score(prompt)
        
        # Score geral
        overall_score = (clarity_score + specificity_score + completeness_score) / 3
        
        # Gerar sugestões
        suggestions = self._generate_evaluation_suggestions(
            clarity_score, specificity_score, completeness_score
        )
        
        evaluation = PromptEvaluation(
            prompt_id=prompt_hash,
            clarity_score=clarity_score,
            specificity_score=specificity_score,
            completeness_score=completeness_score,
            overall_score=overall_score,
            suggestions=suggestions,
            timestamp=datetime.now().isoformat()
        )
        
        # Salvar no cache
        self.evaluation_cache[prompt_hash] = evaluation
        
        return evaluation
    
    def apply_tree_of_thought(self, problem: str, max_depth: int = None) -> List[ThoughtNode]:
        """Aplica técnica Tree-of-Thought para problemas complexos"""
        
        if max_depth is None:
            max_depth = self.max_thought_depth
        
        # Nó raiz
        root_thought = ThoughtNode(
            thought_id="root",
            content=f"Problema: {problem}",
            depth=0
        )
        
        thoughts = [root_thought]
        thought_dict = {root_thought.thought_id: root_thought}
        
        # Expandir árvore de pensamentos
        for depth in range(1, max_depth + 1):
            current_level = [t for t in thoughts if t.depth == depth - 1]
            
            for parent_thought in current_level:
                if parent_thought.evaluation == "impossible":
                    continue
                
                # Gerar pensamentos filhos
                child_thoughts = self._generate_child_thoughts(parent_thought, depth)
                
                for child in child_thoughts:
                    thoughts.append(child)
                    thought_dict[child.thought_id] = child
                    
                    # Avaliar pensamento
                    child.evaluation = self._evaluate_thought(child)
                    child.confidence = self._calculate_thought_confidence(child)
        
        return thoughts
    
    def apply_self_consistency(self, prompt: str, num_samples: int = 5) -> Dict[str, Any]:
        """Aplica técnica Self-Consistency para maior precisão"""
        
        # Gerar múltiplas cadeias de pensamento
        chains = []
        for i in range(num_samples):
            chain = self._generate_thought_chain(prompt)
            chains.append(chain)
        
        # Analisar consistência
        consistency_analysis = self._analyze_consistency(chains)
        
        # Selecionar resposta mais consistente
        most_consistent = self._select_most_consistent_response(chains, consistency_analysis)
        
        return {
            'chains': chains,
            'consistency_analysis': consistency_analysis,
            'most_consistent_response': most_consistent,
            'confidence_score': consistency_analysis['overall_consistency']
        }
    
    def apply_generated_knowledge(self, prompt: str, context: Dict[str, Any] = None) -> str:
        """Aplica técnica Generated Knowledge Prompting"""
        
        # Gerar conhecimento relevante
        generated_knowledge = self._generate_relevant_knowledge(prompt, context)
        
        # Integrar conhecimento ao prompt
        enhanced_prompt = self._integrate_knowledge_into_prompt(prompt, generated_knowledge)
        
        return enhanced_prompt
    
    def _select_optimization_technique(self, evaluation: PromptEvaluation, context: Dict[str, Any]) -> str:
        """Seleciona técnica de otimização baseada na avaliação"""
        
        if evaluation.overall_score < 0.4:
            return "comprehensive_rewrite"
        elif evaluation.clarity_score < 0.6:
            return "clarity_enhancement"
        elif evaluation.specificity_score < 0.6:
            return "specificity_improvement"
        elif evaluation.completeness_score < 0.6:
            return "completeness_enhancement"
        elif context and context.get('complexity') == 'high':
            return "tree_of_thought"
        else:
            return "role_prompting"
    
    def _apply_optimization_technique(self, prompt: str, technique: str, context: Dict[str, Any]) -> str:
        """Aplica técnica específica de otimização"""
        
        if technique == "comprehensive_rewrite":
            return self._comprehensive_rewrite(prompt, context)
        elif technique == "clarity_enhancement":
            return self._enhance_clarity(prompt)
        elif technique == "specificity_improvement":
            return self._improve_specificity(prompt, context)
        elif technique == "completeness_enhancement":
            return self._enhance_completeness(prompt, context)
        elif technique == "tree_of_thought":
            return self._apply_tot_to_prompt(prompt, context)
        elif technique == "role_prompting":
            return self._apply_role_prompting(prompt, context)
        else:
            return prompt
    
    def _comprehensive_rewrite(self, prompt: str, context: Dict[str, Any]) -> str:
        """Reescreve prompt completamente"""
        
        # Detectar tipo de tarefa
        task_type = self._detect_task_type(prompt)
        
        # Template baseado no tipo de tarefa
        if task_type == "coding":
            return self._create_coding_prompt_template(prompt, context)
        elif task_type == "explanation":
            return self._create_explanation_prompt_template(prompt, context)
        elif task_type == "analysis":
            return self._create_analysis_prompt_template(prompt, context)
        else:
            return self._create_general_prompt_template(prompt, context)
    
    def _enhance_clarity(self, prompt: str) -> str:
        """Melhora clareza do prompt"""
        
        # Adicionar estrutura clara
        enhanced = f"""Por favor, seja claro e específico na sua resposta.

Tarefa: {prompt}

Instruções:
1. Responda de forma estruturada
2. Use linguagem clara e acessível
3. Forneça exemplos quando apropriado
4. Explique seu raciocínio

Resposta:"""
        
        return enhanced
    
    def _improve_specificity(self, prompt: str, context: Dict[str, Any]) -> str:
        """Melhora especificidade do prompt"""
        
        # Adicionar contexto específico
        context_info = ""
        if context:
            if 'technologies' in context:
                context_info += f"\nTecnologias: {', '.join(context['technologies'])}"
            if 'complexity' in context:
                context_info += f"\nComplexidade: {context['complexity']}"
            if 'task_type' in context:
                context_info += f"\nTipo de Tarefa: {context['task_type']}"
        
        enhanced = f"""Tarefa específica: {prompt}{context_info}

Por favor, forneça uma resposta específica e detalhada que aborde diretamente esta tarefa."""
        
        return enhanced
    
    def _enhance_completeness(self, prompt: str, context: Dict[str, Any]) -> str:
        """Melhora completude do prompt"""
        
        # Adicionar elementos que podem estar faltando
        enhanced = f"""Tarefa: {prompt}

Para uma resposta completa, por favor inclua:
1. Análise detalhada do problema
2. Solução passo a passo
3. Explicação do raciocínio
4. Exemplos práticos quando relevante
5. Considerações importantes ou limitações

Resposta completa:"""
        
        return enhanced
    
    def _apply_tot_to_prompt(self, prompt: str, context: Dict[str, Any]) -> str:
        """Aplica Tree-of-Thought ao prompt"""
        
        enhanced = f"""Este é um problema complexo que requer pensamento estruturado.

Problema: {prompt}

Instruções para resolução:
1. Primeiro, analise o problema e identifique os componentes principais
2. Gere múltiplas abordagens possíveis
3. Avalie cada abordagem considerando prós e contras
4. Escolha a melhor abordagem baseada na análise
5. Implemente a solução passo a passo
6. Verifique se a solução resolve completamente o problema

Por favor, siga este processo de pensamento estruturado e explique cada etapa."""
        
        return enhanced
    
    def _apply_role_prompting(self, prompt: str, context: Dict[str, Any]) -> str:
        """Aplica Role Prompting"""
        
        # Determinar papel apropriado baseado no contexto
        role = self._determine_appropriate_role(context)
        
        enhanced = f"""Você é {role}.

Tarefa: {prompt}

Por favor, responda de acordo com sua especialização e experiência."""
        
        return enhanced
    
    def _detect_task_type(self, prompt: str) -> str:
        """Detecta tipo de tarefa do prompt"""
        
        prompt_lower = prompt.lower()
        
        if any(word in prompt_lower for word in ['código', 'programa', 'função', 'classe', 'implementar']):
            return "coding"
        elif any(word in prompt_lower for word in ['explicar', 'como funciona', 'o que é', 'definição']):
            return "explanation"
        elif any(word in prompt_lower for word in ['analisar', 'revisar', 'avaliar', 'comparar']):
            return "analysis"
        else:
            return "general"
    
    def _determine_appropriate_role(self, context: Dict[str, Any]) -> str:
        """Determina papel apropriado baseado no contexto"""
        
        if not context:
            return "um assistente especializado"
        
        if 'technologies' in context:
            techs = context['technologies']
            if 'Python' in techs:
                return "um desenvolvedor Python sênior"
            elif 'C++' in techs:
                return "um desenvolvedor C++ experiente"
            elif 'Lua' in techs:
                return "um desenvolvedor Lua especializado"
        
        if context.get('task_type') == 'documentation':
            return "um documentador técnico experiente"
        elif context.get('task_type') == 'optimization':
            return "um engenheiro de performance"
        
        return "um assistente especializado"
    
    def _calculate_clarity_score(self, prompt: str) -> float:
        """Calcula score de clareza do prompt"""
        
        # Métricas de clareza
        word_count = len(prompt.split())
        sentence_count = len(re.split(r'[.!?]+', prompt))
        avg_sentence_length = word_count / max(sentence_count, 1)
        
        # Score baseado em comprimento de sentença (sentenças muito longas são menos claras)
        if avg_sentence_length <= 15:
            clarity_score = 0.9
        elif avg_sentence_length <= 25:
            clarity_score = 0.7
        elif avg_sentence_length <= 35:
            clarity_score = 0.5
        else:
            clarity_score = 0.3
        
        # Penalizar por ambiguidade
        ambiguous_words = ['isso', 'aquilo', 'algo', 'coisa', 'tal']
        ambiguous_count = sum(1 for word in ambiguous_words if word in prompt.lower())
        clarity_score -= ambiguous_count * 0.1
        
        return max(0.0, min(1.0, clarity_score))
    
    def _calculate_specificity_score(self, prompt: str) -> float:
        """Calcula score de especificidade do prompt"""
        
        # Métricas de especificidade
        specific_indicators = [
            'por favor', 'especificamente', 'detalhadamente', 'passo a passo',
            'com exemplos', 'incluindo', 'considerando', 'baseado em'
        ]
        
        specific_count = sum(1 for indicator in specific_indicators if indicator in prompt.lower())
        specificity_score = min(1.0, specific_count * 0.2)
        
        # Bônus por ter contexto específico
        if any(word in prompt.lower() for word in ['python', 'c++', 'lua', 'otclient', 'canary']):
            specificity_score += 0.2
        
        return max(0.0, min(1.0, specificity_score))
    
    def _calculate_completeness_score(self, prompt: str) -> float:
        """Calcula score de completude do prompt"""
        
        # Métricas de completude
        completeness_indicators = [
            'explique', 'analise', 'avalie', 'compare', 'considere',
            'incluindo', 'também', 'além disso', 'adicionalmente'
        ]
        
        completeness_count = sum(1 for indicator in completeness_indicators if indicator in prompt.lower())
        completeness_score = min(1.0, completeness_count * 0.15)
        
        # Bônus por ter múltiplas instruções
        instruction_count = len(re.findall(r'[.!?]', prompt))
        if instruction_count >= 3:
            completeness_score += 0.2
        
        return max(0.0, min(1.0, completeness_score))
    
    def _generate_evaluation_suggestions(self, clarity: float, specificity: float, completeness: float) -> List[str]:
        """Gera sugestões baseadas na avaliação"""
        
        suggestions = []
        
        if clarity < 0.6:
            suggestions.append("Melhorar clareza: Use sentenças mais curtas e diretas")
        
        if specificity < 0.6:
            suggestions.append("Aumentar especificidade: Adicione contexto e detalhes específicos")
        
        if completeness < 0.6:
            suggestions.append("Melhorar completude: Inclua mais instruções e considerações")
        
        if all(score < 0.5 for score in [clarity, specificity, completeness]):
            suggestions.append("Considerar reescrita completa do prompt")
        
        return suggestions
    
    def _calculate_optimization_confidence(self, evaluation: PromptEvaluation) -> float:
        """Calcula confiança da otimização"""
        
        # Confiança baseada na qualidade atual
        if evaluation.overall_score < 0.4:
            return 0.9  # Alta confiança para prompts ruins
        elif evaluation.overall_score < 0.7:
            return 0.7  # Confiança média para prompts medianos
        else:
            return 0.5  # Baixa confiança para prompts bons
    
    def _generate_optimization_reasoning(self, evaluation: PromptEvaluation, technique: str) -> str:
        """Gera explicação para a otimização"""
        
        reasoning = f"Aplicada técnica '{technique}' porque: "
        
        if technique == "comprehensive_rewrite":
            reasoning += f"Score geral baixo ({evaluation.overall_score:.2f})"
        elif technique == "clarity_enhancement":
            reasoning += f"Clareza baixa ({evaluation.clarity_score:.2f})"
        elif technique == "specificity_improvement":
            reasoning += f"Especificidade baixa ({evaluation.specificity_score:.2f})"
        elif technique == "completeness_enhancement":
            reasoning += f"Completude baixa ({evaluation.completeness_score:.2f})"
        
        return reasoning
    
    def _estimate_improvement(self, evaluation: PromptEvaluation) -> float:
        """Estima melhoria esperada"""
        
        # Estimativa baseada na qualidade atual
        if evaluation.overall_score < 0.4:
            return 0.4  # Grande melhoria esperada
        elif evaluation.overall_score < 0.7:
            return 0.2  # Melhoria moderada esperada
        else:
            return 0.1  # Pequena melhoria esperada
    
    def _generate_child_thoughts(self, parent_thought: ThoughtNode, depth: int) -> List[ThoughtNode]:
        """Gera pensamentos filhos para Tree-of-Thought"""
        
        children = []
        
        # Gerar diferentes abordagens
        approaches = [
            "Análise detalhada do problema",
            "Identificação de componentes principais",
            "Geração de hipóteses",
            "Avaliação de alternativas",
            "Planejamento de solução"
        ]
        
        for i, approach in enumerate(approaches):
            child = ThoughtNode(
                thought_id=f"{parent_thought.thought_id}_child_{i}",
                content=f"{approach}: {parent_thought.content}",
                parent_id=parent_thought.thought_id,
                depth=depth
            )
            children.append(child)
        
        return children
    
    def _evaluate_thought(self, thought: ThoughtNode) -> str:
        """Avalia um pensamento"""
        
        # Avaliação simples baseada no conteúdo
        content = thought.content.lower()
        
        if any(word in content for word in ['impossível', 'não pode', 'erro']):
            return "impossible"
        elif any(word in content for word in ['possível', 'pode', 'viável']):
            return "possible"
        elif any(word in content for word in ['correto', 'certo', 'solução']):
            return "correct"
        else:
            return "pending"
    
    def _calculate_thought_confidence(self, thought: ThoughtNode) -> float:
        """Calcula confiança de um pensamento"""
        
        # Confiança baseada na avaliação
        if thought.evaluation == "correct":
            return 0.9
        elif thought.evaluation == "possible":
            return 0.6
        elif thought.evaluation == "impossible":
            return 0.1
        else:
            return 0.3
    
    def _generate_thought_chain(self, prompt: str) -> List[str]:
        """Gera uma cadeia de pensamento"""
        
        # Simulação de cadeia de pensamento
        steps = [
            f"Analisando o prompt: {prompt}",
            "Identificando os requisitos principais",
            "Considerando diferentes abordagens",
            "Selecionando a melhor estratégia",
            "Implementando a solução"
        ]
        
        return steps
    
    def _analyze_consistency(self, chains: List[List[str]]) -> Dict[str, Any]:
        """Analisa consistência entre cadeias de pensamento"""
        
        # Análise simples de consistência
        all_steps = []
        for chain in chains:
            all_steps.extend(chain)
        
        # Contar frequência de passos similares
        step_frequency = defaultdict(int)
        for step in all_steps:
            step_frequency[step] += 1
        
        # Calcular consistência
        total_steps = len(all_steps)
        unique_steps = len(step_frequency)
        consistency = 1.0 - (unique_steps / total_steps)
        
        return {
            'overall_consistency': consistency,
            'step_frequency': dict(step_frequency),
            'total_chains': len(chains)
        }
    
    def _select_most_consistent_response(self, chains: List[List[str]], analysis: Dict[str, Any]) -> str:
        """Seleciona resposta mais consistente"""
        
        # Selecionar cadeia com passos mais frequentes
        step_frequency = analysis['step_frequency']
        
        best_chain = chains[0]  # Padrão
        best_score = 0
        
        for chain in chains:
            score = sum(step_frequency.get(step, 0) for step in chain)
            if score > best_score:
                best_score = score
                best_chain = chain
        
        return " -> ".join(best_chain)
    
    def _generate_relevant_knowledge(self, prompt: str, context: Dict[str, Any]) -> List[str]:
        """Gera conhecimento relevante para o prompt"""
        
        knowledge = []
        
        # Conhecimento baseado no tipo de tarefa
        task_type = self._detect_task_type(prompt)
        
        if task_type == "coding":
            knowledge.extend([
                "Boas práticas de programação",
                "Padrões de design relevantes",
                "Considerações de performance",
                "Tratamento de erros"
            ])
        elif task_type == "explanation":
            knowledge.extend([
                "Conceitos fundamentais",
                "Exemplos práticos",
                "Contexto histórico",
                "Aplicações reais"
            ])
        
        # Conhecimento baseado no contexto
        if context and 'technologies' in context:
            for tech in context['technologies']:
                knowledge.append(f"Especificidades da tecnologia {tech}")
        
        return knowledge
    
    def _integrate_knowledge_into_prompt(self, prompt: str, knowledge: List[str]) -> str:
        """Integra conhecimento ao prompt"""
        
        knowledge_text = "\n".join([f"- {k}" for k in knowledge])
        
        enhanced = f"""Contexto e conhecimento relevante:
{knowledge_text}

Tarefa: {prompt}

Por favor, considere o conhecimento acima ao responder."""
        
        return enhanced
    
    def get_optimization_stats(self) -> Dict[str, Any]:
        """Retorna estatísticas de otimização"""
        
        return {
            'total_optimizations': len(self.optimization_cache),
            'total_evaluations': len(self.evaluation_cache),
            'prompt_history_size': len(self.prompt_history),
            'average_confidence': statistics.mean([opt.confidence_score for opt in self.optimization_cache.values()]) if self.optimization_cache else 0.0,
    
            'most_used_technique': self._get_most_used_technique()
        }
    
    def _get_most_used_technique(self) -> str:
        """Retorna técnica mais usada"""
        
        technique_count = defaultdict(int)
        for opt in self.optimization_cache.values():
            technique_count[opt.technique_applied] += 1
        
        if technique_count:
            return max(technique_count.items(), key=lambda x: x[1])[0]
        return "none" 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = GitautomationModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script advanced_prompt_system.py executado com sucesso via módulo tools.git_automation")
    else:
        print(f"❌ Erro na execução do script advanced_prompt_system.py via módulo tools.git_automation")

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
- **Nome**: migrated_advanced_prompt_system
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

