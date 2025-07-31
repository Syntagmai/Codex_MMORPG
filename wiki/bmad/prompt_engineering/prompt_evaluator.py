#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Avaliador de Prompts BMAD
Avalia qualidade e eficácia de prompts usando métricas específicas
"""

import re
import json
import statistics
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from pathlib import Path

@dataclass
class PromptMetrics:
    """Métricas de avaliação de prompt"""
    prompt_id: str
    clarity_score: float
    specificity_score: float
    completeness_score: float
    structure_score: float
    context_score: float
    overall_score: float
    suggestions: List[str]
    timestamp: str

@dataclass
class EvaluationResult:
    """Resultado completo de avaliação"""
    metrics: PromptMetrics
    detailed_analysis: Dict[str, Any]
    recommendations: List[str]
    confidence: float

class PromptEvaluator:
    """Avaliador especializado de prompts"""
    
    def __init__(self):
        # Configurações de avaliação
        self.weights = {
            'clarity': 0.25,
            'specificity': 0.20,
            'completeness': 0.20,
            'structure': 0.15,
            'context': 0.20
        }
        
        # Padrões de avaliação
        self.patterns = self._load_evaluation_patterns()
        
        # Histórico de avaliações
        self.evaluation_history = []
    
    def _load_evaluation_patterns(self) -> Dict[str, Any]:
        """Carrega padrões de avaliação"""
        return {
            'clarity_indicators': {
                'positive': [
                    'por favor', 'especificamente', 'detalhadamente',
                    'claramente', 'objetivamente', 'precisamente'
                ],
                'negative': [
                    'isso', 'aquilo', 'algo', 'coisa', 'tal',
                    'assim', 'dessa forma', 'mais ou menos'
                ]
            },
            'specificity_indicators': {
                'positive': [
                    'python', 'c++', 'lua', 'otclient', 'canary',
                    'função', 'classe', 'módulo', 'sistema'
                ],
                'negative': [
                    'código', 'programa', 'aplicação', 'sistema'
                ]
            },
            'completeness_indicators': {
                'positive': [
                    'incluindo', 'também', 'além disso', 'adicionalmente',
                    'considerando', 'levando em conta', 'tendo em mente'
                ],
                'negative': [
                    'apenas', 'só', 'simplesmente', 'basicamente'
                ]
            },
            'structure_indicators': {
                'positive': [
                    'primeiro', 'segundo', 'terceiro', 'passo',
                    'etapa', 'fase', 'seção', 'parte'
                ],
                'negative': [
                    'tudo junto', 'de uma vez', 'rapidamente'
                ]
            },
            'context_indicators': {
                'positive': [
                    'contexto', 'ambiente', 'situação', 'cenário',
                    'considerando', 'baseado em', 'dado que'
                ],
                'negative': [
                    'sem contexto', 'genérico', 'qualquer'
                ]
            }
        }
    
    def evaluate_prompt(self, prompt: str, context: Dict[str, Any] = None) -> EvaluationResult:
        """Avalia um prompt completo"""
        
        # Calcular métricas individuais
        clarity_score = self._calculate_clarity_score(prompt)
        specificity_score = self._calculate_specificity_score(prompt, context)
        completeness_score = self._calculate_completeness_score(prompt)
        structure_score = self._calculate_structure_score(prompt)
        context_score = self._calculate_context_score(prompt, context)
        
        # Calcular score geral
        overall_score = self._calculate_overall_score({
            'clarity': clarity_score,
            'specificity': specificity_score,
            'completeness': completeness_score,
            'structure': structure_score,
            'context': context_score
        })
        
        # Gerar sugestões
        suggestions = self._generate_suggestions({
            'clarity': clarity_score,
            'specificity': specificity_score,
            'completeness': completeness_score,
            'structure': structure_score,
            'context': context_score
        })
        
        # Criar métricas
        prompt_id = self._generate_prompt_id(prompt)
        metrics = PromptMetrics(
            prompt_id=prompt_id,
            clarity_score=clarity_score,
            specificity_score=specificity_score,
            completeness_score=completeness_score,
            structure_score=structure_score,
            context_score=context_score,
            overall_score=overall_score,
            suggestions=suggestions,
            timestamp=datetime.now().isoformat()
        )
        
        # Análise detalhada
        detailed_analysis = self._create_detailed_analysis(prompt, metrics)
        
        # Recomendações
        recommendations = self._generate_recommendations(metrics, context)
        
        # Confiança da avaliação
        confidence = self._calculate_evaluation_confidence(metrics)
        
        # Salvar no histórico
        self.evaluation_history.append({
            'timestamp': datetime.now().isoformat(),
            'prompt_id': prompt_id,
            'metrics': metrics,
            'context': context
        })
        
        return EvaluationResult(
            metrics=metrics,
            detailed_analysis=detailed_analysis,
            recommendations=recommendations,
            confidence=confidence
        )
    
    def _calculate_clarity_score(self, prompt: str) -> float:
        """Calcula score de clareza"""
        
        score = 0.5  # Score base
        
        # Análise de sentenças
        sentences = re.split(r'[.!?]+', prompt)
        avg_sentence_length = sum(len(s.split()) for s in sentences) / max(len(sentences), 1)
        
        # Penalizar sentenças muito longas
        if avg_sentence_length <= 15:
            score += 0.3
        elif avg_sentence_length <= 25:
            score += 0.1
        elif avg_sentence_length > 35:
            score -= 0.2
        
        # Análise de palavras positivas
        positive_count = sum(1 for word in self.patterns['clarity_indicators']['positive'] 
                           if word in prompt.lower())
        score += positive_count * 0.1
        
        # Penalizar palavras negativas
        negative_count = sum(1 for word in self.patterns['clarity_indicators']['negative'] 
                           if word in prompt.lower())
        score -= negative_count * 0.15
        
        return max(0.0, min(1.0, score))
    
    def _calculate_specificity_score(self, prompt: str, context: Dict[str, Any]) -> float:
        """Calcula score de especificidade"""
        
        score = 0.3  # Score base
        
        # Análise de palavras específicas
        specific_count = sum(1 for word in self.patterns['specificity_indicators']['positive'] 
                           if word in prompt.lower())
        score += specific_count * 0.15
        
        # Penalizar palavras genéricas
        generic_count = sum(1 for word in self.patterns['specificity_indicators']['negative'] 
                          if word in prompt.lower())
        score -= generic_count * 0.1
        
        # Bônus por contexto específico
        if context:
            if 'technologies' in context:
                tech_mentions = sum(1 for tech in context['technologies'] 
                                  if tech.lower() in prompt.lower())
                score += tech_mentions * 0.1
            
            if 'task_type' in context:
                if context['task_type'].lower() in prompt.lower():
                    score += 0.1
        
        return max(0.0, min(1.0, score))
    
    def _calculate_completeness_score(self, prompt: str) -> float:
        """Calcula score de completude"""
        
        score = 0.4  # Score base
        
        # Análise de palavras de completude
        complete_count = sum(1 for word in self.patterns['completeness_indicators']['positive'] 
                           if word in prompt.lower())
        score += complete_count * 0.1
        
        # Penalizar palavras de incompletude
        incomplete_count = sum(1 for word in self.patterns['completeness_indicators']['negative'] 
                             if word in prompt.lower())
        score -= incomplete_count * 0.1
        
        # Bônus por múltiplas instruções
        instruction_count = len(re.findall(r'[.!?]', prompt))
        if instruction_count >= 3:
            score += 0.2
        elif instruction_count >= 2:
            score += 0.1
        
        # Bônus por estrutura de lista
        if re.search(r'[1-9]\.|•|\-', prompt):
            score += 0.1
        
        return max(0.0, min(1.0, score))
    
    def _calculate_structure_score(self, prompt: str) -> float:
        """Calcula score de estrutura"""
        
        score = 0.3  # Score base
        
        # Análise de indicadores de estrutura
        structure_count = sum(1 for word in self.patterns['structure_indicators']['positive'] 
                            if word in prompt.lower())
        score += structure_count * 0.15
        
        # Penalizar falta de estrutura
        no_structure_count = sum(1 for word in self.patterns['structure_indicators']['negative'] 
                               if word in prompt.lower())
        score -= no_structure_count * 0.1
        
        # Bônus por formatação
        if re.search(r'[1-9]\.|•|\-', prompt):
            score += 0.2
        
        # Bônus por seções
        if re.search(r'[A-Z][a-z]+:', prompt):
            score += 0.1
        
        return max(0.0, min(1.0, score))
    
    def _calculate_context_score(self, prompt: str, context: Dict[str, Any]) -> float:
        """Calcula score de contexto"""
        
        score = 0.3  # Score base
        
        # Análise de indicadores de contexto
        context_count = sum(1 for word in self.patterns['context_indicators']['positive'] 
                          if word in prompt.lower())
        score += context_count * 0.1
        
        # Penalizar falta de contexto
        no_context_count = sum(1 for word in self.patterns['context_indicators']['negative'] 
                             if word in prompt.lower())
        score -= no_context_count * 0.1
        
        # Bônus por contexto fornecido
        if context:
            context_mentions = 0
            for key, value in context.items():
                if isinstance(value, str) and value.lower() in prompt.lower():
                    context_mentions += 1
                elif isinstance(value, list):
                    for item in value:
                        if item.lower() in prompt.lower():
                            context_mentions += 1
            
            score += context_mentions * 0.1
        
        return max(0.0, min(1.0, score))
    
    def _calculate_overall_score(self, scores: Dict[str, float]) -> float:
        """Calcula score geral ponderado"""
        
        overall = 0.0
        for metric, score in scores.items():
            overall += score * self.weights[metric]
        
        return overall
    
    def _generate_suggestions(self, scores: Dict[str, float]) -> List[str]:
        """Gera sugestões baseadas nos scores"""
        
        suggestions = []
        
        if scores['clarity'] < 0.6:
            suggestions.append("Melhorar clareza: Use sentenças mais curtas e diretas")
        
        if scores['specificity'] < 0.6:
            suggestions.append("Aumentar especificidade: Adicione contexto e detalhes específicos")
        
        if scores['completeness'] < 0.6:
            suggestions.append("Melhorar completude: Inclua mais instruções e considerações")
        
        if scores['structure'] < 0.6:
            suggestions.append("Melhorar estrutura: Organize o prompt em seções claras")
        
        if scores['context'] < 0.6:
            suggestions.append("Adicionar contexto: Inclua informações de background relevantes")
        
        if all(score < 0.5 for score in scores.values()):
            suggestions.append("Considerar reescrita completa do prompt")
        
        return suggestions
    
    def _create_detailed_analysis(self, prompt: str, metrics: PromptMetrics) -> Dict[str, Any]:
        """Cria análise detalhada do prompt"""
        
        return {
            'word_count': len(prompt.split()),
            'sentence_count': len(re.split(r'[.!?]+', prompt)),
            'avg_sentence_length': len(prompt.split()) / max(len(re.split(r'[.!?]+', prompt)), 1),
            'has_structure': bool(re.search(r'[1-9]\.|•|\-', prompt)),
            'has_context': bool(re.search(r'contexto|ambiente|situação', prompt.lower())),
            'has_specific_terms': bool(re.search(r'python|c\+\+|lua|otclient|canary', prompt.lower())),
            'metrics_breakdown': {
                'clarity': {
                    'score': metrics.clarity_score,
                    'weight': self.weights['clarity'],
                    'contribution': metrics.clarity_score * self.weights['clarity']
                },
                'specificity': {
                    'score': metrics.specificity_score,
                    'weight': self.weights['specificity'],
                    'contribution': metrics.specificity_score * self.weights['specificity']
                },
                'completeness': {
                    'score': metrics.completeness_score,
                    'weight': self.weights['completeness'],
                    'contribution': metrics.completeness_score * self.weights['completeness']
                },
                'structure': {
                    'score': metrics.structure_score,
                    'weight': self.weights['structure'],
                    'contribution': metrics.structure_score * self.weights['structure']
                },
                'context': {
                    'score': metrics.context_score,
                    'weight': self.weights['context'],
                    'contribution': metrics.context_score * self.weights['context']
                }
            }
        }
    
    def _generate_recommendations(self, metrics: PromptMetrics, context: Dict[str, Any]) -> List[str]:
        """Gera recomendações específicas"""
        
        recommendations = []
        
        # Recomendações baseadas em scores
        if metrics.clarity_score < 0.5:
            recommendations.append("Reescreva o prompt usando linguagem mais clara e direta")
        
        if metrics.specificity_score < 0.5:
            recommendations.append("Adicione detalhes específicos sobre tecnologias e contexto")
        
        if metrics.completeness_score < 0.5:
            recommendations.append("Inclua mais instruções e considerações no prompt")
        
        if metrics.structure_score < 0.5:
            recommendations.append("Organize o prompt em seções numeradas ou com marcadores")
        
        if metrics.context_score < 0.5:
            recommendations.append("Forneça contexto de background relevante")
        
        # Recomendações baseadas no contexto
        if context and 'technologies' in context:
            tech_list = ', '.join(context['technologies'])
            recommendations.append(f"Mencione especificamente as tecnologias: {tech_list}")
        
        if context and 'complexity' in context:
            if context['complexity'] == 'high':
                recommendations.append("Considere usar Chain-of-Thought para problemas complexos")
        
        return recommendations
    
    def _calculate_evaluation_confidence(self, metrics: PromptMetrics) -> float:
        """Calcula confiança da avaliação"""
        
        # Confiança baseada na consistência dos scores
        scores = [
            metrics.clarity_score,
            metrics.specificity_score,
            metrics.completeness_score,
            metrics.structure_score,
            metrics.context_score
        ]
        
        # Variância baixa = alta confiança
        variance = statistics.variance(scores)
        confidence = max(0.5, 1.0 - variance)
        
        return confidence
    
    def _generate_prompt_id(self, prompt: str) -> str:
        """Gera ID único para o prompt"""
        
        import hashlib
        return hashlib.md5(prompt.encode()).hexdigest()[:8]
    
    def batch_evaluate(self, prompts: List[str], context: Dict[str, Any] = None) -> List[EvaluationResult]:
        """Avalia múltiplos prompts"""
        
        results = []
        for prompt in prompts:
            result = self.evaluate_prompt(prompt, context)
            results.append(result)
        
        return results
    
    def get_evaluation_stats(self) -> Dict[str, Any]:
        """Retorna estatísticas de avaliação"""
        
        if not self.evaluation_history:
            return {}
        
        recent_evaluations = self.evaluation_history[-100:]  # Últimas 100
        
        scores = {
            'clarity': [e['metrics'].clarity_score for e in recent_evaluations],
            'specificity': [e['metrics'].specificity_score for e in recent_evaluations],
            'completeness': [e['metrics'].completeness_score for e in recent_evaluations],
            'structure': [e['metrics'].structure_score for e in recent_evaluations],
            'context': [e['metrics'].context_score for e in recent_evaluations],
            'overall': [e['metrics'].overall_score for e in recent_evaluations]
        }
        
        return {
            'total_evaluations': len(self.evaluation_history),
            'recent_evaluations': len(recent_evaluations),
            'average_scores': {
                metric: statistics.mean(score_list) for metric, score_list in scores.items()
            },
            'best_score': max(scores['overall']) if scores['overall'] else 0.0,
            'worst_score': min(scores['overall']) if scores['overall'] else 0.0,
            'improvement_trend': self._calculate_improvement_trend()
        }
    
    def _calculate_improvement_trend(self) -> str:
        """Calcula tendência de melhoria"""
        
        if len(self.evaluation_history) < 10:
            return "insufficient_data"
        
        recent_scores = [e['metrics'].overall_score for e in self.evaluation_history[-10:]]
        first_half = recent_scores[:5]
        second_half = recent_scores[5:]
        
        if not first_half or not second_half:
            return "insufficient_data"
        
        avg_first = statistics.mean(first_half)
        avg_second = statistics.mean(second_half)
        
        if avg_second > avg_first + 0.1:
            return "improving"
        elif avg_second < avg_first - 0.1:
            return "declining"
        else:
            return "stable" 