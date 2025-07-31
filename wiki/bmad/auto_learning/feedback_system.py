#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Feedback para Auto-Aprendizado
Coleta e processa feedback dos usuários para melhorar o sistema
"""

import json
import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from pathlib import Path
from dataclasses import dataclass, asdict
from collections import defaultdict
import statistics

@dataclass
class FeedbackRecord:
    """Registro de feedback do usuário"""
    feedback_id: str
    interaction_id: str
    feedback_text: str
    feedback_score: float
    feedback_type: str  # 'explicit', 'implicit', 'behavioral'
    timestamp: str
    metadata: Dict[str, Any]

@dataclass
class FeedbackAnalysis:
    """Análise de feedback"""
    interaction_id: str
    overall_score: float
    sentiment_score: float
    improvement_suggestions: List[str]
    confidence_level: float

class FeedbackSystem:
    """Sistema de coleta e análise de feedback"""
    
    def __init__(self, logs_path: Path):
        self.logs_path = logs_path
        self.feedback_file = logs_path / "feedback_data.json"
        self.analysis_file = logs_path / "feedback_analysis.json"
        
        # Carregar dados existentes
        self.feedback_data = self.load_feedback_data()
        self.feedback_analysis = self.load_feedback_analysis()
        
        # Configurações
        self.min_feedback_score = 0.0
        self.max_feedback_score = 1.0
        self.sentiment_threshold = 0.6
        
        # Palavras-chave para análise de sentimento
        self.positive_keywords = {
            'bom', 'ótimo', 'excelente', 'perfeito', 'funcionou', 'sucesso',
            'rápido', 'eficiente', 'útil', 'claro', 'fácil', 'intuitivo'
        }
        
        self.negative_keywords = {
            'ruim', 'péssimo', 'erro', 'falha', 'lento', 'confuso',
            'difícil', 'inútil', 'não funcionou', 'problema', 'bug'
        }
    
    def load_feedback_data(self) -> Dict[str, Any]:
        """Carrega dados de feedback do arquivo"""
        if self.feedback_file.exists():
            with open(self.feedback_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def load_feedback_analysis(self) -> Dict[str, Any]:
        """Carrega análises de feedback do arquivo"""
        if self.analysis_file.exists():
            with open(self.analysis_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def save_feedback_data(self):
        """Salva dados de feedback no arquivo"""
        with open(self.feedback_file, 'w', encoding='utf-8') as f:
            json.dump(self.feedback_data, f, indent=2, ensure_ascii=False)
    
    def save_feedback_analysis(self):
        """Salva análises de feedback no arquivo"""
        with open(self.analysis_file, 'w', encoding='utf-8') as f:
            json.dump(self.feedback_analysis, f, indent=2, ensure_ascii=False)
    
    def record_feedback(self, interaction_id: str, feedback_text: str, feedback_score: float, 
                       feedback_type: str = 'explicit', metadata: Optional[Dict] = None):
        """Registra feedback de uma interação"""
        # Validar score
        feedback_score = max(self.min_feedback_score, min(self.max_feedback_score, feedback_score))
        
        # Gerar ID único
        feedback_id = self.generate_feedback_id(interaction_id, feedback_text, feedback_score)
        
        # Criar registro
        feedback_record = FeedbackRecord(
            feedback_id=feedback_id,
            interaction_id=interaction_id,
            feedback_text=feedback_text,
            feedback_score=feedback_score,
            feedback_type=feedback_type,
            timestamp=datetime.now().isoformat(),
            metadata=metadata or {}
        )
        
        # Salvar feedback
        self.feedback_data[feedback_id] = asdict(feedback_record)
        self.save_feedback_data()
        
        # Analisar feedback
        analysis = self.analyze_feedback(feedback_record)
        self.feedback_analysis[interaction_id] = asdict(analysis)
        self.save_feedback_analysis()
        
        print(f"📝 Feedback registrado: {feedback_id} (Score: {feedback_score:.2f})")
        
        return feedback_id
    
    def generate_feedback_id(self, interaction_id: str, feedback_text: str, feedback_score: float) -> str:
        """Gera ID único para feedback"""
        content = f"{interaction_id}_{feedback_text}_{feedback_score}_{datetime.now().isoformat()}"
        return hashlib.md5(content.encode()).hexdigest()
    
    def analyze_feedback(self, feedback_record: FeedbackRecord) -> FeedbackAnalysis:
        """Analisa feedback e extrai insights"""
        # Análise de sentimento
        sentiment_score = self._analyze_sentiment(feedback_record.feedback_text)
        
        # Sugestões de melhoria
        improvement_suggestions = self._extract_improvement_suggestions(feedback_record.feedback_text)
        
        # Nível de confiança baseado no tipo de feedback
        confidence_level = self._calculate_confidence_level(feedback_record)
        
        # Score geral
        overall_score = (feedback_record.feedback_score + sentiment_score) / 2
        
        return FeedbackAnalysis(
            interaction_id=feedback_record.interaction_id,
            overall_score=overall_score,
            sentiment_score=sentiment_score,
            improvement_suggestions=improvement_suggestions,
            confidence_level=confidence_level
        )
    
    def _analyze_sentiment(self, feedback_text: str) -> float:
        """Analisa sentimento do feedback"""
        if not feedback_text:
            return 0.5
        
        text_lower = feedback_text.lower()
        
        # Contar palavras positivas e negativas
        positive_count = sum(1 for word in self.positive_keywords if word in text_lower)
        negative_count = sum(1 for word in self.negative_keywords if word in text_lower)
        
        # Calcular score de sentimento
        total_words = len(text_lower.split())
        if total_words == 0:
            return 0.5
        
        positive_ratio = positive_count / total_words
        negative_ratio = negative_count / total_words
        
        # Score baseado na diferença
        sentiment_score = 0.5 + (positive_ratio - negative_ratio) * 2
        
        # Normalizar entre 0 e 1
        return max(0.0, min(1.0, sentiment_score))
    
    def _extract_improvement_suggestions(self, feedback_text: str) -> List[str]:
        """Extrai sugestões de melhoria do feedback"""
        suggestions = []
        
        # Palavras-chave que indicam sugestões
        suggestion_keywords = [
            'poderia', 'deveria', 'seria melhor', 'sugiro', 'recomendo',
            'melhorar', 'otimizar', 'corrigir', 'adicionar', 'remover'
        ]
        
        sentences = feedback_text.split('.')
        
        for sentence in sentences:
            sentence_lower = sentence.lower()
            for keyword in suggestion_keywords:
                if keyword in sentence_lower:
                    # Limpar e adicionar sugestão
                    suggestion = sentence.strip()
                    if suggestion and len(suggestion) > 10:
                        suggestions.append(suggestion)
                    break
        
        return suggestions[:5]  # Limitar a 5 sugestões
    
    def _calculate_confidence_level(self, feedback_record: FeedbackRecord) -> float:
        """Calcula nível de confiança do feedback"""
        confidence = 0.5  # Base
        
        # Feedback explícito tem maior confiança
        if feedback_record.feedback_type == 'explicit':
            confidence += 0.3
        
        # Feedback com texto tem maior confiança
        if feedback_record.feedback_text and len(feedback_record.feedback_text) > 10:
            confidence += 0.2
        
        # Feedback extremo (muito bom ou muito ruim) tem maior confiança
        if feedback_record.feedback_score <= 0.2 or feedback_record.feedback_score >= 0.8:
            confidence += 0.1
        
        return min(1.0, confidence)
    
    def get_feedback_stats(self, days: int = 30) -> Dict[str, Any]:
        """Retorna estatísticas de feedback"""
        cutoff_date = datetime.now() - timedelta(days=days)
        
        # Filtrar feedback recente
        recent_feedback = [
            f for f in self.feedback_data.values()
            if datetime.fromisoformat(f['timestamp']) >= cutoff_date
        ]
        
        if not recent_feedback:
            return {
                'total_feedback': 0,
                'avg_score': 0.0,
                'sentiment_distribution': {},
                'feedback_types': {},
                'improvement_suggestions': []
            }
        
        # Estatísticas básicas
        scores = [f['feedback_score'] for f in recent_feedback]
        avg_score = statistics.mean(scores)
        
        # Distribuição de sentimento
        sentiment_scores = [f['feedback_score'] for f in recent_feedback]
        sentiment_distribution = {
            'positive': len([s for s in sentiment_scores if s >= 0.7]),
            'neutral': len([s for s in sentiment_scores if 0.4 <= s < 0.7]),
            'negative': len([s for s in sentiment_scores if s < 0.4])
        }
        
        # Tipos de feedback
        feedback_types = defaultdict(int)
        for f in recent_feedback:
            feedback_types[f['feedback_type']] += 1
        
        # Sugestões de melhoria
        all_suggestions = []
        for f in recent_feedback:
            if f['feedback_text']:
                suggestions = self._extract_improvement_suggestions(f['feedback_text'])
                all_suggestions.extend(suggestions)
        
        # Contar sugestões mais comuns
        suggestion_counts = defaultdict(int)
        for suggestion in all_suggestions:
            suggestion_counts[suggestion] += 1
        
        top_suggestions = sorted(suggestion_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        
        return {
            'total_feedback': len(recent_feedback),
            'avg_score': avg_score,
            'sentiment_distribution': sentiment_distribution,
            'feedback_types': dict(feedback_types),
            'improvement_suggestions': [{'suggestion': s, 'count': c} for s, c in top_suggestions]
        }
    
    def get_interaction_feedback(self, interaction_id: str) -> Optional[Dict[str, Any]]:
        """Retorna feedback de uma interação específica"""
        # Buscar feedback da interação
        feedback_records = [
            f for f in self.feedback_data.values()
            if f['interaction_id'] == interaction_id
        ]
        
        if not feedback_records:
            return None
        
        # Buscar análise
        analysis = self.feedback_analysis.get(interaction_id)
        
        return {
            'feedback_records': feedback_records,
            'analysis': analysis,
            'feedback_count': len(feedback_records)
        }
    
    def get_low_performing_interactions(self, threshold: float = 0.5, days: int = 7) -> List[Dict[str, Any]]:
        """Retorna interações com baixo desempenho"""
        cutoff_date = datetime.now() - timedelta(days=days)
        
        low_performing = []
        
        for interaction_id, analysis in self.feedback_analysis.items():
            if datetime.fromisoformat(analysis['timestamp']) >= cutoff_date:
                if analysis['overall_score'] <= threshold:
                    # Buscar feedback detalhado
                    feedback_info = self.get_interaction_feedback(interaction_id)
                    if feedback_info:
                        low_performing.append({
                            'interaction_id': interaction_id,
                            'overall_score': analysis['overall_score'],
                            'sentiment_score': analysis['sentiment_score'],
                            'improvement_suggestions': analysis['improvement_suggestions'],
                            'feedback_count': feedback_info['feedback_count']
                        })
        
        # Ordenar por score (pior primeiro)
        low_performing.sort(key=lambda x: x['overall_score'])
        
        return low_performing
    
    def get_improvement_recommendations(self) -> List[Dict[str, Any]]:
        """Gera recomendações de melhoria baseadas no feedback"""
        recommendations = []
        
        # Analisar feedback recente
        stats = self.get_feedback_stats(days=30)
        
        # Recomendação baseada na distribuição de sentimento
        if stats['sentiment_distribution']['negative'] > stats['sentiment_distribution']['positive']:
            recommendations.append({
                'type': 'sentiment_improvement',
                'priority': 'high',
                'description': 'Feedback negativo predominante - revisar workflows problemáticos',
                'suggested_actions': [
                    'Analisar interações com baixo score',
                    'Revisar seleção de agentes',
                    'Otimizar workflows comuns'
                ]
            })
        
        # Recomendação baseada em sugestões específicas
        if stats['improvement_suggestions']:
            top_suggestion = stats['improvement_suggestions'][0]
            if top_suggestion['count'] >= 3:  # Múltiplas menções
                recommendations.append({
                    'type': 'specific_improvement',
                    'priority': 'medium',
                    'description': f'Melhoria específica sugerida: {top_suggestion["suggestion"]}',
                    'suggested_actions': [
                        'Implementar melhoria sugerida',
                        'Testar com usuários',
                        'Coletar feedback adicional'
                    ]
                })
        
        # Recomendação baseada no score médio
        if stats['avg_score'] < 0.6:
            recommendations.append({
                'type': 'overall_improvement',
                'priority': 'high',
                'description': f'Score médio baixo ({stats["avg_score"]:.2f}) - revisão geral necessária',
                'suggested_actions': [
                    'Revisar sistema de detecção de contexto',
                    'Otimizar seleção de agentes',
                    'Melhorar workflows padrão'
                ]
            })
        
        return recommendations
    
    def record_implicit_feedback(self, interaction_id: str, success_score: float, 
                                execution_time: float, error_message: Optional[str] = None):
        """Registra feedback implícito baseado no comportamento"""
        feedback_text = ""
        feedback_score = success_score
        
        # Ajustar score baseado em outros fatores
        if error_message:
            feedback_text = f"Erro detectado: {error_message}"
            feedback_score *= 0.5  # Reduzir score se houve erro
        
        if execution_time > 10:  # Muito lento
            feedback_text += f" Execução lenta ({execution_time:.1f}s)"
            feedback_score *= 0.8
        
        # Normalizar score
        feedback_score = max(0.0, min(1.0, feedback_score))
        
        # Registrar feedback implícito
        self.record_feedback(
            interaction_id=interaction_id,
            feedback_text=feedback_text or "Feedback implícito baseado no comportamento",
            feedback_score=feedback_score,
            feedback_type='implicit',
            metadata={
                'execution_time': execution_time,
                'error_message': error_message,
                'success_score': success_score
            }
        )
    
    def cleanup_old_feedback(self, days_to_keep: int = 90):
        """Remove feedback antigo"""
        cutoff_date = datetime.now() - timedelta(days=days_to_keep)
        
        # Remover feedback antigo
        feedback_to_remove = []
        for feedback_id, feedback in self.feedback_data.items():
            if datetime.fromisoformat(feedback['timestamp']) < cutoff_date:
                feedback_to_remove.append(feedback_id)
        
        for feedback_id in feedback_to_remove:
            del self.feedback_data[feedback_id]
        
        # Remover análises antigas
        analysis_to_remove = []
        for interaction_id, analysis in self.feedback_analysis.items():
            if datetime.fromisoformat(analysis['timestamp']) < cutoff_date:
                analysis_to_remove.append(interaction_id)
        
        for interaction_id in analysis_to_remove:
            del self.feedback_analysis[interaction_id]
        
        # Salvar dados limpos
        self.save_feedback_data()
        self.save_feedback_analysis()
        
        print(f"🧹 Removidos {len(feedback_to_remove)} feedbacks antigos") 