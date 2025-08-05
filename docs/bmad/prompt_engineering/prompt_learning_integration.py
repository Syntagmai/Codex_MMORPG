#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Integração de Prompt Engineering com Auto-Aprendizado BMAD
Permite que o sistema aprenda e melhore técnicas de prompt automaticamente
"""

import os
import json
import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
from dataclasses import dataclass, asdict
from collections import defaultdict, deque
import statistics

@dataclass
class PromptLearningPattern:
    """Padrão aprendido sobre prompts"""
    pattern_id: str
    prompt_type: str
    technique_used: str
    success_rate: float
    context_applicability: Dict[str, float]
    optimization_effectiveness: float
    usage_count: int
    last_updated: str

@dataclass
class PromptOptimizationResult:
    """Resultado de otimização de prompt"""
    original_prompt: str
    optimized_prompt: str
    technique_applied: str
    success_score: float
    user_feedback: Optional[str] = None
    context: Dict[str, Any] = None

class PromptLearningIntegration:
    """Integração entre prompt engineering e auto-aprendizado"""
    
    def __init__(self, base_path: str = "wiki"):
        self.base_path = Path(base_path)
        self.prompt_learning_path = self.base_path / "bmad" / "prompt_engineering"
        self.data_path = self.prompt_learning_path / "learning_data"
        
        # Criar estrutura de pastas
        self.data_path.mkdir(parents=True, exist_ok=True)
        
        # Arquivos de dados
        self.patterns_file = self.data_path / "prompt_patterns.json"
        self.optimizations_file = self.data_path / "prompt_optimizations.json"
        self.learning_log_file = self.data_path / "prompt_learning_log.json"
        
        # Carregar dados existentes
        self.prompt_patterns = self.load_prompt_patterns()
        self.optimization_history = self.load_optimization_history()
        self.learning_log = self.load_learning_log()
        
        # Cache de aprendizados
        self.pattern_cache = {}
        self.cache_timestamp = None
        self.cache_validity = 300  # 5 minutos
    
    def load_prompt_patterns(self) -> Dict[str, Any]:
        """Carrega padrões de prompt aprendidos"""
        if self.patterns_file.exists():
            with open(self.patterns_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def load_optimization_history(self) -> Dict[str, Any]:
        """Carrega histórico de otimizações"""
        if self.optimizations_file.exists():
            with open(self.optimizations_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def load_learning_log(self) -> Dict[str, Any]:
        """Carrega log de aprendizado"""
        if self.learning_log_file.exists():
            with open(self.learning_log_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"optimizations": [], "patterns": [], "feedback": []}
    
    def save_prompt_patterns(self):
        """Salva padrões de prompt aprendidos"""
        with open(self.patterns_file, 'w', encoding='utf-8') as f:
            json.dump(self.prompt_patterns, f, indent=2, ensure_ascii=False)
    
    def save_optimization_history(self):
        """Salva histórico de otimizações"""
        with open(self.optimizations_file, 'w', encoding='utf-8') as f:
            json.dump(self.optimization_history, f, indent=2, ensure_ascii=False)
    
    def save_learning_log(self):
        """Salva log de aprendizado"""
        with open(self.learning_log_file, 'w', encoding='utf-8') as f:
            json.dump(self.learning_log, f, indent=2, ensure_ascii=False)
    
    def record_prompt_optimization(self, result: PromptOptimizationResult):
        """Registra resultado de otimização de prompt"""
        
        optimization_id = hashlib.md5(result.original_prompt.encode()).hexdigest()[:8]
        
        # Salvar no histórico
        self.optimization_history[optimization_id] = {
            'timestamp': datetime.now().isoformat(),
            'original_prompt': result.original_prompt,
            'optimized_prompt': result.optimized_prompt,
            'technique_applied': result.technique_applied,
            'success_score': result.success_score,
            'user_feedback': result.user_feedback,
            'context': result.context
        }
        
        # Adicionar ao log
        self.learning_log['optimizations'].append({
            'timestamp': datetime.now().isoformat(),
            'optimization_id': optimization_id,
            'technique': result.technique_applied,
            'success_score': result.success_score,
            'context': result.context
        })
        
        # Manter apenas últimos 1000 registros
        if len(self.learning_log['optimizations']) > 1000:
            self.learning_log['optimizations'] = self.learning_log['optimizations'][-1000:]
        
        self.save_optimization_history()
        self.save_learning_log()
        
        # Atualizar padrões se score for alto
        if result.success_score > 0.7:
            self._update_prompt_patterns(result)
    
    def _update_prompt_patterns(self, result: PromptOptimizationResult):
        """Atualiza padrões de prompt baseado em resultado bem-sucedido"""
        
        # Detectar tipo de prompt
        prompt_type = self._detect_prompt_type(result.original_prompt)
        
        # Criar ou atualizar padrão
        pattern_id = f"{prompt_type}_{result.technique_applied}"
        
        if pattern_id in self.prompt_patterns:
            # Atualizar padrão existente
            pattern = self.prompt_patterns[pattern_id]
            pattern['usage_count'] += 1
            pattern['success_rate'] = (pattern['success_rate'] + result.success_score) / 2
            pattern['last_updated'] = datetime.now().isoformat()
            
            # Atualizar aplicabilidade de contexto
            if result.context:
                for key, value in result.context.items():
                    if key not in pattern['context_applicability']:
                        pattern['context_applicability'][key] = result.success_score
                    else:
                        pattern['context_applicability'][key] = (
                            pattern['context_applicability'][key] + result.success_score
                        ) / 2
        else:
            # Criar novo padrão
            context_applicability = {}
            if result.context:
                for key, value in result.context.items():
                    context_applicability[key] = result.success_score
            
            self.prompt_patterns[pattern_id] = {
                'pattern_id': pattern_id,
                'prompt_type': prompt_type,
                'technique_used': result.technique_applied,
                'success_rate': result.success_score,
                'context_applicability': context_applicability,
                'optimization_effectiveness': result.success_score,
                'usage_count': 1,
                'last_updated': datetime.now().isoformat()
            }
        
        self.save_prompt_patterns()
    
    def _detect_prompt_type(self, prompt: str) -> str:
        """Detecta tipo de prompt"""
        
        prompt_lower = prompt.lower()
        
        if any(word in prompt_lower for word in ['código', 'programa', 'função', 'implementar']):
            return "coding"
        elif any(word in prompt_lower for word in ['explicar', 'como funciona', 'o que é']):
            return "explanation"
        elif any(word in prompt_lower for word in ['analisar', 'revisar', 'avaliar']):
            return "analysis"
        elif any(word in prompt_lower for word in ['criar', 'desenvolver', 'construir']):
            return "creation"
        else:
            return "general"
    
    def get_optimization_recommendation(self, prompt: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Obtém recomendação de otimização baseada em padrões aprendidos"""
        
        prompt_type = self._detect_prompt_type(prompt)
        
        # Buscar padrões relevantes
        relevant_patterns = []
        for pattern_id, pattern in self.prompt_patterns.items():
            if pattern['prompt_type'] == prompt_type:
                # Calcular relevância de contexto
                context_relevance = self._calculate_context_relevance(pattern, context)
                if context_relevance > 0.5:  # Threshold de relevância
                    relevant_patterns.append({
                        'pattern': pattern,
                        'context_relevance': context_relevance
                    })
        
        # Ordenar por sucesso e relevância
        relevant_patterns.sort(
            key=lambda x: x['pattern']['success_rate'] * x['context_relevance'],
            reverse=True
        )
        
        if relevant_patterns:
            best_pattern = relevant_patterns[0]
            return {
                'recommended_technique': best_pattern['pattern']['technique_used'],
                'confidence': best_pattern['pattern']['success_rate'],
                'context_relevance': best_pattern['context_relevance'],
                'usage_count': best_pattern['pattern']['usage_count'],
                'reasoning': f"Padrão bem-sucedido para prompts do tipo '{prompt_type}'"
            }
        else:
            return {
                'recommended_technique': 'role_prompting',  # Fallback
                'confidence': 0.5,
                'context_relevance': 0.5,
                'usage_count': 0,
                'reasoning': f"Nenhum padrão específico encontrado para '{prompt_type}'"
            }
    
    def _calculate_context_relevance(self, pattern: Dict[str, Any], context: Dict[str, Any]) -> float:
        """Calcula relevância de contexto para um padrão"""
        
        if not context:
            return 0.5  # Relevância neutra
        
        relevance_scores = []
        
        for context_key, context_value in context.items():
            if context_key in pattern['context_applicability']:
                relevance_scores.append(pattern['context_applicability'][context_key])
        
        if relevance_scores:
            return statistics.mean(relevance_scores)
        else:
            return 0.3  # Baixa relevância se não há sobreposição
    
    def analyze_optimization_effectiveness(self) -> Dict[str, Any]:
        """Analisa efetividade das otimizações"""
        
        if not self.learning_log['optimizations']:
            return {}
        
        # Análise por técnica
        technique_stats = defaultdict(lambda: {'count': 0, 'scores': []})
        
        for opt in self.learning_log['optimizations']:
            technique = opt['technique']
            technique_stats[technique]['count'] += 1
            technique_stats[technique]['scores'].append(opt['success_score'])
        
        # Calcular estatísticas por técnica
        technique_analysis = {}
        for technique, stats in technique_stats.items():
            technique_analysis[technique] = {
                'usage_count': stats['count'],
                'average_success': statistics.mean(stats['scores']),
                'success_rate': len([s for s in stats['scores'] if s > 0.7]) / len(stats['scores'])
            }
        
        # Análise temporal
        recent_optimizations = [
            opt for opt in self.learning_log['optimizations']
            if datetime.fromisoformat(opt['timestamp']) > datetime.now() - timedelta(days=7)
        ]
        
        if recent_optimizations:
            recent_avg = statistics.mean([opt['success_score'] for opt in recent_optimizations])
        else:
            recent_avg = 0.0
        
        return {
            'total_optimizations': len(self.learning_log['optimizations']),
            'technique_analysis': technique_analysis,
            'recent_average_success': recent_avg,
            'best_technique': max(technique_analysis.items(), 
                                key=lambda x: x[1]['average_success'])[0] if technique_analysis else "none",
            'most_used_technique': max(technique_analysis.items(), 
                                     key=lambda x: x[1]['usage_count'])[0] if technique_analysis else "none"
        }
    
    def get_learning_recommendations(self) -> List[str]:
        """Gera recomendações baseadas no aprendizado"""
        
        recommendations = []
        analysis = self.analyze_optimization_effectiveness()
        
        if not analysis:
            return ["Coletar mais dados de otimização para gerar recomendações"]
        
        # Recomendações baseadas em efetividade
        best_technique = analysis.get('best_technique')
        if best_technique and best_technique != "none":
            recommendations.append(f"Priorizar técnica '{best_technique}' - maior taxa de sucesso")
        
        # Recomendações baseadas em uso
        most_used = analysis.get('most_used_technique')
        if most_used and most_used != best_technique:
            recommendations.append(f"Considerar alternativas à técnica '{most_used}' - uso excessivo")
        
        # Recomendações baseadas em tendências
        recent_avg = analysis.get('recent_average_success', 0.0)
        if recent_avg < 0.6:
            recommendations.append("Melhorar qualidade das otimizações - taxa de sucesso recente baixa")
        
        # Recomendações baseadas em padrões
        if len(self.prompt_patterns) < 5:
            recommendations.append("Diversificar técnicas de otimização para criar mais padrões")
        
        return recommendations
    
    def generate_learning_report(self) -> Dict[str, Any]:
        """Gera relatório de aprendizado"""
        
        analysis = self.analyze_optimization_effectiveness()
        recommendations = self.get_learning_recommendations()
        
        return {
            'timestamp': datetime.now().isoformat(),
            'total_patterns_learned': len(self.prompt_patterns),
            'total_optimizations': len(self.learning_log['optimizations']),
            'effectiveness_analysis': analysis,
            'recommendations': recommendations,
            'pattern_summary': {
                'coding_patterns': len([p for p in self.prompt_patterns.values() if p['prompt_type'] == 'coding']),
                'explanation_patterns': len([p for p in self.prompt_patterns.values() if p['prompt_type'] == 'explanation']),
                'analysis_patterns': len([p for p in self.prompt_patterns.values() if p['prompt_type'] == 'analysis']),
                'creation_patterns': len([p for p in self.prompt_patterns.values() if p['prompt_type'] == 'creation'])
            },
            'top_patterns': self._get_top_patterns()
        }
    
    def _get_top_patterns(self) -> List[Dict[str, Any]]:
        """Retorna padrões mais bem-sucedidos"""
        
        patterns_list = []
        for pattern_id, pattern in self.prompt_patterns.items():
            patterns_list.append({
                'pattern_id': pattern_id,
                'prompt_type': pattern['prompt_type'],
                'technique': pattern['technique_used'],
                'success_rate': pattern['success_rate'],
                'usage_count': pattern['usage_count']
            })
        
        # Ordenar por sucesso e uso
        patterns_list.sort(
            key=lambda x: x['success_rate'] * x['usage_count'],
            reverse=True
        )
        
        return patterns_list[:5]  # Top 5
    
    def apply_learned_optimizations(self, prompt: str, context: Dict[str, Any] = None) -> str:
        """Aplica otimizações aprendidas a um prompt"""
        
        # Obter recomendação
        recommendation = self.get_optimization_recommendation(prompt, context)
        
        # Aplicar técnica recomendada
        technique = recommendation['recommended_technique']
        
        if technique == "role_prompting":
            return self._apply_role_prompting(prompt, context)
        elif technique == "chain_of_thought":
            return self._apply_chain_of_thought(prompt)
        elif technique == "specificity_improvement":
            return self._apply_specificity_improvement(prompt, context)
        elif technique == "clarity_enhancement":
            return self._apply_clarity_enhancement(prompt)
        else:
            return prompt  # Fallback
    
    def _apply_role_prompting(self, prompt: str, context: Dict[str, Any]) -> str:
        """Aplica role prompting baseado em contexto"""
        
        role = "um assistente especializado"
        
        if context and 'technologies' in context:
            techs = context['technologies']
            if 'Python' in techs:
                role = "um desenvolvedor Python sênior"
            elif 'C++' in techs:
                role = "um desenvolvedor C++ experiente"
            elif 'Lua' in techs:
                role = "um desenvolvedor Lua especializado"
        
        return f"""Você é {role}.

Tarefa: {prompt}

Por favor, responda de acordo com sua especialização e experiência."""
    
    def _apply_chain_of_thought(self, prompt: str) -> str:
        """Aplica chain-of-thought"""
        
        return f"""Este problema requer pensamento estruturado.

Problema: {prompt}

Por favor, siga este processo:
1. Analise o problema passo a passo
2. Identifique os componentes principais
3. Considere diferentes abordagens
4. Escolha a melhor solução
5. Implemente e explique sua escolha

Resposta estruturada:"""
    
    def _apply_specificity_improvement(self, prompt: str, context: Dict[str, Any]) -> str:
        """Aplica melhoria de especificidade"""
        
        context_info = ""
        if context:
            if 'technologies' in context:
                context_info += f"\nTecnologias: {', '.join(context['technologies'])}"
            if 'complexity' in context:
                context_info += f"\nComplexidade: {context['complexity']}"
        
        return f"""Tarefa específica: {prompt}{context_info}

Por favor, forneça uma resposta específica e detalhada."""
    
    def _apply_clarity_enhancement(self, prompt: str) -> str:
        """Aplica melhoria de clareza"""
        
        return f"""Por favor, seja claro e específico.

Tarefa: {prompt}

Instruções:
1. Responda de forma estruturada
2. Use linguagem clara e acessível
3. Forneça exemplos quando apropriado
4. Explique seu raciocínio

Resposta:""" 