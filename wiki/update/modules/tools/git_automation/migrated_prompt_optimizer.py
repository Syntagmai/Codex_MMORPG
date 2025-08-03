from unicode_aliases import *
# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: prompt_optimizer.py
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
Otimizador de Prompts BMAD
Aplica técnicas específicas de otimização de prompts
"""

import re

@dataclass
class OptimizationResult:
    """Resultado de uma otimização de prompt"""
    original: str
    optimized: str
    technique: str
    improvement_score: float
    changes_made: List[str]
    reasoning: str

class PromptOptimizer:
    """Otimizador especializado de prompts"""
    
    def __init__(self):
        # Templates de otimização
        self.templates = self._load_optimization_templates()
        
        # Padrões de detecção
        self.patterns = self._load_detection_patterns()
    
    def _load_optimization_templates(self) -> Dict[str, str]:
        """Carrega templates de otimização"""
        return {
            'role_developer': """Você é um desenvolvedor {technology} experiente com {years} anos de experiência.

Tarefa: {task}

Por favor, forneça uma solução profissional e bem documentada.""",
            
            'role_teacher': """Você é um professor experiente especializado em {subject}.

Tarefa: {task}

Por favor, explique de forma didática e acessível, usando exemplos quando apropriado.""",
            
            'role_analyst': """Você é um analista técnico sênior com expertise em {domain}.

Tarefa: {task}

Por favor, forneça uma análise detalhada e estruturada.""",
            
            'chain_of_thought': """Este problema requer pensamento estruturado.

Problema: {task}

Por favor, siga este processo:
1. Analise o problema passo a passo
2. Identifique os componentes principais
3. Considere diferentes abordagens
4. Escolha a melhor solução
5. Implemente e explique sua escolha

Resposta estruturada:""",
            
            'few_shot': """Exemplos de formato esperado:

{examples}

Agora, aplique o mesmo formato para:

{task}

Resposta:""",
            
            'structured_output': """Por favor, responda usando este formato:

{format_structure}

Tarefa: {task}

Resposta estruturada:"""
        }
    
    def _load_detection_patterns(self) -> Dict[str, List[str]]:
        """Carrega padrões de detecção"""
        return {
            'coding_keywords': [
                'código', 'programa', 'função', 'classe', 'implementar',
                'desenvolver', 'criar', 'escrever', 'debug', 'otimizar'
            ],
            'explanation_keywords': [
                'explicar', 'como funciona', 'o que é', 'definição',
                'conceito', 'entender', 'compreender', 'descrever'
            ],
            'analysis_keywords': [
                'analisar', 'revisar', 'avaliar', 'comparar', 'examinar',
                'investigar', 'estudar', 'considerar', 'verificar'
            ],
            'ambiguous_words': [
                'isso', 'aquilo', 'algo', 'coisa', 'tal', 'assim',
                'dessa forma', 'desse jeito', 'mais ou menos'
            ]
        }
    
    def optimize_prompt(self, prompt: str, context: Dict[str, Any] = None) -> OptimizationResult:
        """Otimiza um prompt usando múltiplas técnicas"""
        
        original_prompt = prompt
        optimized_prompt = prompt
        applied_techniques = []
        changes_made = []
        reasoning = []
        
        # 1. Detectar tipo de tarefa
        task_type = self._detect_task_type(prompt)
        reasoning.append(f"Tipo de tarefa detectado: {task_type}")
        
        # 2. Aplicar Role Prompting
        if self._needs_role_prompting(prompt):
            optimized_prompt = self._apply_role_prompting(optimized_prompt, task_type, context)
            applied_techniques.append("role_prompting")
            changes_made.append("Adicionado contexto de papel específico")
            reasoning.append("Prompt beneficiaria de contexto de especialista")
        
        # 3. Melhorar clareza
        if self._needs_clarity_improvement(prompt):
            optimized_prompt = self._improve_clarity(optimized_prompt)
            applied_techniques.append("clarity_improvement")
            changes_made.append("Melhorada clareza e estrutura")
            reasoning.append("Detectadas ambiguidades e falta de estrutura")
        
        # 4. Aplicar Chain-of-Thought se necessário
        if self._needs_chain_of_thought(prompt, task_type):
            optimized_prompt = self._apply_chain_of_thought(optimized_prompt)
            applied_techniques.append("chain_of_thought")
            changes_made.append("Adicionado processo de pensamento estruturado")
            reasoning.append("Tarefa complexa requer pensamento passo a passo")
        
        # 5. Melhorar especificidade
        if self._needs_specificity_improvement(prompt):
            optimized_prompt = self._improve_specificity(optimized_prompt, context)
            applied_techniques.append("specificity_improvement")
            changes_made.append("Aumentada especificidade e contexto")
            reasoning.append("Prompt muito genérico, adicionado contexto específico")
        
        # 6. Estruturar saída se necessário
        if self._needs_structured_output(prompt, task_type):
            optimized_prompt = self._add_structured_output(optimized_prompt, task_type)
            applied_techniques.append("structured_output")
            changes_made.append("Adicionado formato de saída estruturado")
            reasoning.append("Tarefa beneficiaria de resposta estruturada")
        
        # Calcular score de melhoria
        improvement_score = self._calculate_improvement_score(original_prompt, optimized_prompt)
        
        return OptimizationResult(
            original=original_prompt,
            optimized=optimized_prompt,
            technique=" + ".join(applied_techniques) if applied_techniques else "none",
            improvement_score=improvement_score,
            changes_made=changes_made,
            reasoning="; ".join(reasoning)
        )
    
    def _detect_task_type(self, prompt: str) -> str:
        """Detecta tipo de tarefa do prompt"""
        
        prompt_lower = prompt.lower()
        
        if any(keyword in prompt_lower for keyword in self.patterns['coding_keywords']):
            return "coding"
        elif any(keyword in prompt_lower for keyword in self.patterns['explanation_keywords']):
            return "explanation"
        elif any(keyword in prompt_lower for keyword in self.patterns['analysis_keywords']):
            return "analysis"
        else:
            return "general"
    
    def _needs_role_prompting(self, prompt: str) -> bool:
        """Verifica se prompt precisa de role prompting"""
        
        # Verificar se já tem contexto de papel
        role_indicators = ['você é', 'atuando como', 'sendo um', 'como um']
        has_role = any(indicator in prompt.lower() for indicator in role_indicators)
        
        return not has_role
    
    def _needs_clarity_improvement(self, prompt: str) -> bool:
        """Verifica se prompt precisa de melhoria de clareza"""
        
        # Verificar ambiguidades
        has_ambiguous = any(word in prompt.lower() for word in self.patterns['ambiguous_words'])
        
        # Verificar estrutura
        sentences = re.split(r'[.!?]+', prompt)
        long_sentences = [s for s in sentences if len(s.split()) > 25]
        
        return has_ambiguous or len(long_sentences) > 0
    
    def _needs_chain_of_thought(self, prompt: str, task_type: str) -> bool:
        """Verifica se prompt precisa de chain-of-thought"""
        
        # Tarefas complexas ou de análise
        complex_keywords = ['complexo', 'difícil', 'análise', 'investigar', 'resolver problema']
        has_complex = any(keyword in prompt.lower() for keyword in complex_keywords)
        
        return has_complex or task_type == "analysis"
    
    def _needs_specificity_improvement(self, prompt: str) -> bool:
        """Verifica se prompt precisa de melhoria de especificidade"""
        
        # Verificar se é muito genérico
        generic_phrases = ['faz isso', 'ajuda aí', 'resolva', 'faça']
        is_generic = any(phrase in prompt.lower() for phrase in generic_phrases)
        
        # Verificar se tem contexto específico
        has_context = any(word in prompt.lower() for word in ['python', 'c++', 'lua', 'otclient', 'canary'])
        
        return is_generic and not has_context
    
    def _needs_structured_output(self, prompt: str, task_type: str) -> bool:
        """Verifica se prompt precisa de saída estruturada"""
        
        # Tarefas que se beneficiam de estrutura
        structured_tasks = ['analysis', 'comparison', 'evaluation', 'review']
        
        return task_type in structured_tasks
    
    def _apply_role_prompting(self, prompt: str, task_type: str, context: Dict[str, Any]) -> str:
        """Aplica role prompting"""
        
        if task_type == "coding":
            technology = self._extract_technology(context)
            years = "10+"
            template = self.templates['role_developer'].format(
                technology=technology,
                years=years,
                task=prompt
            )
        elif task_type == "explanation":
            subject = self._extract_subject(context)
            template = self.templates['role_teacher'].format(
                subject=subject,
                task=prompt
            )
        elif task_type == "analysis":
            domain = self._extract_domain(context)
            template = self.templates['role_analyst'].format(
                domain=domain,
                task=prompt
            )
        else:
            template = f"""Você é um assistente especializado.

Tarefa: {prompt}

Por favor, forneça uma resposta profissional e bem estruturada."""
        
        return template
    
    def _improve_clarity(self, prompt: str) -> str:
        """Melhora clareza do prompt"""
        
        # Substituir palavras ambíguas
        replacements = {
            'isso': 'o problema específico',
            'aquilo': 'o item mencionado',
            'algo': 'uma solução específica',
            'coisa': 'o elemento',
            'tal': 'o mencionado'
        }
        
        improved = prompt
        for ambiguous, specific in replacements.items():
            improved = improved.replace(ambiguous, specific)
        
        # Adicionar estrutura
        improved = f"""Por favor, seja claro e específico.

Tarefa: {improved}

Instruções:
1. Responda de forma estruturada
2. Use linguagem clara e acessível
3. Forneça exemplos quando apropriado
4. Explique seu raciocínio

Resposta:"""
        
        return improved
    
    def _apply_chain_of_thought(self, prompt: str) -> str:
        """Aplica chain-of-thought"""
        
        return self.templates['chain_of_thought'].format(task=prompt)
    
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
        
        improved = f"""Tarefa específica: {prompt}{context_info}

Por favor, forneça uma resposta específica e detalhada que aborde diretamente esta tarefa."""
        
        return improved
    
    def _add_structured_output(self, prompt: str, task_type: str) -> str:
        """Adiciona estrutura de saída"""
        
        if task_type == "analysis":
            format_structure = """
- Resumo Executivo
- Análise Detalhada
- Principais Descobertas
- Recomendações
- Conclusão"""
        elif task_type == "comparison":
            format_structure = """
- Critérios de Comparação
- Análise do Item A
- Análise do Item B
- Comparação Direta
- Recomendação Final"""
        else:
            format_structure = """
- Introdução
- Desenvolvimento
- Conclusão"""
        
        return self.templates['structured_output'].format(
            format_structure=format_structure,
            task=prompt
        )
    
    def _extract_technology(self, context: Dict[str, Any]) -> str:
        """Extrai tecnologia do contexto"""
        
        if context and 'technologies' in context:
            return context['technologies'][0] if context['technologies'] else "programação"
        return "programação"
    
    def _extract_subject(self, context: Dict[str, Any]) -> str:
        """Extrai assunto do contexto"""
        
        if context and 'technologies' in context:
            return f"{context['technologies'][0]} e desenvolvimento"
        return "tecnologia e desenvolvimento"
    
    def _extract_domain(self, context: Dict[str, Any]) -> str:
        """Extrai domínio do contexto"""
        
        if context and 'technologies' in context:
            return f"análise de {context['technologies'][0]}"
        return "análise técnica"
    
    def _calculate_improvement_score(self, original: str, optimized: str) -> float:
        """Calcula score de melhoria"""
        
        # Métricas simples de melhoria
        original_words = len(original.split())
        optimized_words = len(optimized.split())
        
        # Score baseado em aumento de detalhes
        word_ratio = optimized_words / max(original_words, 1)
        
        # Score baseado em estrutura
        has_structure = any(indicator in optimized.lower() for indicator in ['instruções:', 'formato:', 'passo'])
        structure_bonus = 0.2 if has_structure else 0.0
        
        # Score baseado em especificidade
        has_specific = any(word in optimized.lower() for word in ['específico', 'detalhado', 'estruturado'])
        specific_bonus = 0.1 if has_specific else 0.0
        
        # Score final
        base_score = min(1.0, (word_ratio - 1) * 0.5)
        total_score = min(1.0, base_score + structure_bonus + specific_bonus)
        
        return total_score
    
    def batch_optimize(self, prompts: List[str], context: Dict[str, Any] = None) -> List[OptimizationResult]:
        """Otimiza múltiplos prompts"""
        
        results = []
        for prompt in prompts:
            result = self.optimize_prompt(prompt, context)
            results.append(result)
        
        return results
    
    def get_optimization_stats(self, results: List[OptimizationResult]) -> Dict[str, Any]:
        """Retorna estatísticas de otimização"""
        
        if not results:
            return {}
        
        techniques_used = {}
        for result in results:
            if result.technique != "none":
                techniques_used[result.technique] = techniques_used.get(result.technique, 0) + 1
        
        return {
            'total_prompts': len(results),
            'optimized_prompts': len([r for r in results if r.technique != "none"]),
            'average_improvement': sum(r.improvement_score for r in results) / len(results),
            'techniques_used': techniques_used,
            'most_common_technique': max(techniques_used.items(), key=lambda x: x[1])[0] if techniques_used else "none"
        } 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = GitautomationModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script prompt_optimizer.py executado com sucesso via módulo tools.git_automation")
    else:
        print(f"❌ Erro na execução do script prompt_optimizer.py via módulo tools.git_automation")
