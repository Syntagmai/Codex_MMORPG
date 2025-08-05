from unicode_aliases import *
# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
MAX_ITEMS = 100
MAX_SIZE = 1000

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: pattern_analyzer.py
Módulo de Destino: analysis.source_analyzer
Data de Migração: 2025-08-01 12:21:44

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import SourceanalyzerModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analisador de Padrões para Auto-Aprendizado
Identifica padrões de sucesso e falha nas interações do sistema
"""

import json
import hashlib
from datetime import datetime, timedelta
import statistics

@dataclass
class PatternMatch:
    """Match de um padrão em uma interação"""
    pattern_id: str
    confidence: float
    matched_features: List[str]
    similarity_score: float

@dataclass
class PatternCluster:
    """Cluster de padrões similares"""
    cluster_id: str
    pattern_type: str  # 'success', 'failure', 'optimization'
    center_pattern: Dict[str, Any]
    member_patterns: List[str]
    confidence_score: float
    size: int

class PatternAnalyzer:
    """Analisador de padrões para identificação de aprendizados"""
    
    def __init__(self, models_path: Path):
        self.models_path = models_path
        self.patterns_file = models_path / "learned_patterns.json"
        self.clusters_file = models_path / "pattern_clusters.json"
        
        # Carregar padrões existentes
        self.patterns = self.load_patterns()
        self.clusters = self.load_clusters()
        
        # Configurações de análise
        self.min_pattern_confidence = 0.6
        self.min_cluster_size = 3
        self.similarity_threshold = 0.7
        self.max_patterns_per_type = 50
        
        # Inicializar vetorizador TF-IDF
        self.tfidf_vectorizer = TfidfVectorizer(
            max_features=1000,
            stop_words='english',
            ngram_range=(1, 2),
            min_df=2
        )
        
        # Cache de análise
        self.analysis_cache = {}
        self.cache_timestamp = None
    
    def load_patterns(self) -> Dict[str, Any]:
        """Carrega padrões aprendidos do arquivo"""
        if self.patterns_file.exists():
            with open(self.patterns_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def load_clusters(self) -> Dict[str, Any]:
        """Carrega clusters de padrões do arquivo"""
        if self.clusters_file.exists():
            with open(self.clusters_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def save_patterns(self):
        """Salva padrões aprendidos no arquivo"""
        with open(self.patterns_file, 'w', encoding='utf-8') as f:
            json.dump(self.patterns, f, indent=2, ensure_ascii=False)
    
    def save_clusters(self):
        """Salva clusters de padrões no arquivo"""
        with open(self.clusters_file, 'w', encoding='utf-8') as f:
            json.dump(self.clusters, f, indent=2, ensure_ascii=False)
    
    def analyze_patterns(self, interactions: List[Any]) -> List[Any]:
        """Analisa interações e identifica padrões"""
        if not interactions:
            return []
        
        print(f"🔍 Analisando {len(interactions)} interações para padrões...")
        
        # 1. Extrair características das interações
        features = self._extract_features(interactions)
        
        # 2. Identificar padrões de sucesso
        success_patterns = self._identify_success_patterns(interactions, features)
        
        # 3. Identificar padrões de falha
        failure_patterns = self._identify_failure_patterns(interactions, features)
        
        # 4. Identificar padrões de otimização
        optimization_patterns = self._identify_optimization_patterns(interactions, features)
        
        # 5. Criar clusters de padrões similares
        all_patterns = success_patterns + failure_patterns + optimization_patterns
        clusters = self._create_pattern_clusters(all_patterns)
        
        # 6. Calcular confiança e scores
        patterns_with_scores = self._calculate_pattern_scores(all_patterns, clusters)
        
        # 7. Filtrar padrões por confiança
        filtered_patterns = [
            p for p in patterns_with_scores 
            if p.confidence_score >= self.min_pattern_confidence
        ]
        
        # 8. Salvar padrões aprendidos
        self._save_learned_patterns(filtered_patterns)
        
        print(f"✅ Identificados {len(filtered_patterns)} padrões válidos")
        return filtered_patterns
    
    def _extract_features(self, interactions: List[Any]) -> Dict[str, List[Any]]:
        """Extrai características das interações"""
        features = {
            'text_features': [],
            'context_features': [],
            'agent_features': [],
            'workflow_features': [],
            'performance_features': []
        }
        
        for interaction in interactions:
            # Características de texto
            text = f"{interaction.user_request} {interaction.workflow_executed}"
            features['text_features'].append(text)
            
            # Características de contexto
            context_keys = list(interaction.context_detected.keys())
            features['context_features'].append(context_keys)
            
            # Características de agentes
            features['agent_features'].append(interaction.agents_selected)
            
            # Características de workflow
            features['workflow_features'].append(interaction.workflow_executed)
            
            # Características de performance
            perf_features = {
                'execution_time': interaction.execution_time,
                'success_score': interaction.success_score,
                'agent_count': len(interaction.agents_selected),
                'optimization_applied': interaction.optimization_applied
            }
            features['performance_features'].append(perf_features)
        
        return features
    
    def _identify_success_patterns(self, interactions: List[Any], features: Dict) -> List[Dict]:
        """Identifica padrões de sucesso"""
        success_patterns = []
        
        # Filtrar interações bem-sucedidas
        successful_interactions = [
            i for i in interactions if i.success_score >= 0.8
        ]
        
        if len(successful_interactions) < 3:
            return success_patterns
        
        # Analisar padrões de contexto
        context_patterns = self._analyze_context_patterns(successful_interactions)
        
        # Analisar padrões de agentes
        agent_patterns = self._analyze_agent_patterns(successful_interactions)
        
        # Analisar padrões de workflow
        workflow_patterns = self._analyze_workflow_patterns(successful_interactions)
        
        # Combinar padrões
        for context_pattern in context_patterns:
            for agent_pattern in agent_patterns:
                for workflow_pattern in workflow_patterns:
                    pattern = {
                        'pattern_id': self._generate_pattern_id('success', context_pattern, agent_pattern,
    workflow_pattern),
                        'pattern_type': 'success',
                        'context_keywords': context_pattern['keywords'],
                        'agent_combinations': agent_pattern['combinations'],
                        'workflow_types': workflow_pattern['types'],
                        'success_rate': context_pattern['success_rate'],
                        'avg_execution_time': context_pattern['avg_time'],
                        'confidence_score': 0.0,  # Será calculado depois
                        'last_updated': datetime.now().isoformat(),
                        'usage_count': 0
                    }
                    success_patterns.append(pattern)
        
        return success_patterns
    
    def _identify_failure_patterns(self, interactions: List[Any], features: Dict) -> List[Dict]:
        """Identifica padrões de falha"""
        failure_patterns = []
        
        # Filtrar interações com falha
        failed_interactions = [
            i for i in interactions if i.success_score < 0.5 or i.error_message
        ]
        
        if len(failed_interactions) < 2:
            return failure_patterns
        
        # Analisar padrões de erro
        error_patterns = self._analyze_error_patterns(failed_interactions)
        
        # Analisar padrões de contexto que levam a falha
        failure_context_patterns = self._analyze_context_patterns(failed_interactions)
        
        for error_pattern in error_patterns:
            for context_pattern in failure_context_patterns:
                pattern = {
                    'pattern_id': self._generate_pattern_id('failure', error_pattern, context_pattern),
                    'pattern_type': 'failure',
                    'context_keywords': context_pattern['keywords'],
                    'agent_combinations': [],
                    'workflow_types': [],
                    'error_types': error_pattern['error_types'],
                    'success_rate': 0.0,
                    'avg_execution_time': context_pattern['avg_time'],
                    'confidence_score': 0.0,
                    'last_updated': datetime.now().isoformat(),
                    'usage_count': 0
                }
                failure_patterns.append(pattern)
        
        return failure_patterns
    
    def _identify_optimization_patterns(self, interactions: List[Any], features: Dict) -> List[Dict]:
        """Identifica padrões de otimização"""
        optimization_patterns = []
        
        # Filtrar interações com otimização aplicada
        optimized_interactions = [
            i for i in interactions if i.optimization_applied
        ]
        
        if len(optimized_interactions) < 2:
            return optimization_patterns
        
        # Analisar padrões de otimização
        optimization_context_patterns = self._analyze_context_patterns(optimized_interactions)
        
        for context_pattern in optimization_context_patterns:
            pattern = {
                'pattern_id': self._generate_pattern_id('optimization', context_pattern),
                'pattern_type': 'optimization',
                'context_keywords': context_pattern['keywords'],
                'agent_combinations': [],
                'workflow_types': [],
                'optimization_triggers': context_pattern['keywords'],
                'success_rate': context_pattern['success_rate'],
                'avg_execution_time': context_pattern['avg_time'],
                'confidence_score': 0.0,
                'last_updated': datetime.now().isoformat(),
                'usage_count': 0
            }
            optimization_patterns.append(pattern)
        
        return optimization_patterns
    
    def _analyze_context_patterns(self, interactions: List[Any]) -> List[Dict]:
        """Analisa padrões de contexto"""
        context_patterns = []
        
        # Agrupar por palavras-chave de contexto
        context_groups = defaultdict(list)
        
        for interaction in interactions:
            context_keys = list(interaction.context_detected.keys())
            for key in context_keys:
                context_groups[key].append(interaction)
        
        # Analisar cada grupo
        for context_key, group_interactions in context_groups.items():
            if len(group_interactions) >= 2:
                success_scores = [i.success_score for i in group_interactions]
                execution_times = [i.execution_time for i in group_interactions]
                
                pattern = {
                    'keywords': [context_key],
                    'success_rate': statistics.mean(success_scores),
                    'avg_time': statistics.mean(execution_times),
                    'count': len(group_interactions)
                }
                context_patterns.append(pattern)
        
        return context_patterns
    
    def _analyze_agent_patterns(self, interactions: List[Any]) -> List[Dict]:
        """Analisa padrões de combinação de agentes"""
        agent_patterns = []
        
        # Agrupar por combinações de agentes
        agent_combinations = defaultdict(list)
        
        for interaction in interactions:
            agent_combo = tuple(sorted(interaction.agents_selected))
            agent_combinations[agent_combo].append(interaction)
        
        # Analisar cada combinação
        for agent_combo, group_interactions in agent_combinations.items():
            if len(group_interactions) >= 2:
                success_scores = [i.success_score for i in group_interactions]
                
                pattern = {
                    'combinations': [list(agent_combo)],
                    'success_rate': statistics.mean(success_scores),
                    'count': len(group_interactions)
                }
                agent_patterns.append(pattern)
        
        return agent_patterns
    
    def _analyze_workflow_patterns(self, interactions: List[Any]) -> List[Dict]:
        """Analisa padrões de workflow"""
        workflow_patterns = []
        
        # Agrupar por tipo de workflow
        workflow_groups = defaultdict(list)
        
        for interaction in interactions:
            workflow_groups[interaction.workflow_executed].append(interaction)
        
        # Analisar cada grupo
        for workflow_type, group_interactions in workflow_groups.items():
            if len(group_interactions) >= 2:
                success_scores = [i.success_score for i in group_interactions]
                
                pattern = {
                    'types': [workflow_type],
                    'success_rate': statistics.mean(success_scores),
                    'count': len(group_interactions)
                }
                workflow_patterns.append(pattern)
        
        return workflow_patterns
    
    def _analyze_error_patterns(self, interactions: List[Any]) -> List[Dict]:
        """Analisa padrões de erro"""
        error_patterns = []
        
        # Agrupar por tipo de erro
        error_groups = defaultdict(list)
        
        for interaction in interactions:
            if interaction.error_message:
                # Extrair tipo de erro do message
                error_type = self._extract_error_type(interaction.error_message)
                error_groups[error_type].append(interaction)
        
        # Analisar cada grupo
        for error_type, group_interactions in error_groups.items():
            if len(group_interactions) >= 2:
                pattern = {
                    'error_types': [error_type],
                    'count': len(group_interactions),
                    'avg_success_score': statistics.mean([i.success_score for i in group_interactions])
                }
                error_patterns.append(pattern)
        
        return error_patterns
    
    def _extract_error_type(self, error_message: str) -> str:
        """Extrai tipo de erro da mensagem"""
        error_message = error_message.lower()
        
        if 'timeout' in error_message:
            return 'timeout'
        elif 'permission' in error_message or 'access' in error_message:
            return 'permission'
        elif 'not found' in error_message or 'missing' in error_message:
            return 'not_found'
        elif 'invalid' in error_message or 'malformed' in error_message:
            return 'invalid_input'
        elif 'connection' in error_message or 'network' in error_message:
            return 'connection'
        else:
            return 'unknown'
    
    def _create_pattern_clusters(self, patterns: List[Dict]) -> List[PatternCluster]:
        """Cria clusters de padrões similares"""
        if len(patterns) < self.min_cluster_size:
            return []
        
        # Preparar dados para clustering
        pattern_texts = []
        for pattern in patterns:
            text = " ".join([
                " ".join(pattern.get('context_keywords', [])),
                " ".join([str(combo) for combo in pattern.get('agent_combinations', [])]),
                " ".join(pattern.get('workflow_types', []))
            ])
            pattern_texts.append(text)
        
        # Aplicar TF-IDF
        try:
            tfidf_matrix = self.tfidf_vectorizer.fit_transform(pattern_texts)
            
            # Aplicar DBSCAN clustering
            clustering = DBSCAN(
                eps=0.3,
                min_samples=self.min_cluster_size,
                metric='cosine'
            ).fit(tfidf_matrix)
            
            # Criar clusters
            clusters = []
            for cluster_id in set(clustering.labels_):
                if cluster_id == -1:  # Ruído
                    continue
                
                cluster_indices = [i for i, label in enumerate(clustering.labels_) if label == cluster_id]
                cluster_patterns = [patterns[i] for i in cluster_indices]
                
                if len(cluster_patterns) >= self.min_cluster_size:
                    # Calcular centro do cluster
                    center_pattern = self._calculate_cluster_center(cluster_patterns)
                    
                    cluster = PatternCluster(
                        cluster_id=f"cluster_{cluster_id}",
                        pattern_type=cluster_patterns[0]['pattern_type'],
                        center_pattern=center_pattern,
                        member_patterns=[p['pattern_id'] for p in cluster_patterns],
                        confidence_score=statistics.mean([p.get('confidence_score', 0) for p in cluster_patterns]),
                        size=len(cluster_patterns)
                    )
                    clusters.append(cluster)
        
        except Exception as e:
            print(f"⚠️ Erro no clustering: {e}")
            clusters = []
        
        return clusters
    
    def _calculate_cluster_center(self, patterns: List[Dict]) -> Dict[str, Any]:
        """Calcula o centro de um cluster de padrões"""
        if not patterns:
            return {}
        
        # Média dos scores
        avg_success_rate = statistics.mean([p.get('success_rate', 0) for p in patterns])
        avg_execution_time = statistics.mean([p.get('avg_execution_time', 0) for p in patterns])
        
        # União de keywords
        all_keywords = set()
        for pattern in patterns:
            all_keywords.update(pattern.get('context_keywords', []))
        
        # Tipo mais comum
        pattern_types = [p.get('pattern_type', 'unknown') for p in patterns]
        most_common_type = Counter(pattern_types).most_common(1)[0][0]
        
        return {
            'pattern_type': most_common_type,
            'context_keywords': list(all_keywords),
            'success_rate': avg_success_rate,
            'avg_execution_time': avg_execution_time,
            'pattern_count': len(patterns)
        }
    
    def _calculate_pattern_scores(self, patterns: List[Dict], clusters: List[PatternCluster]) -> List[Dict]:
        """Calcula scores de confiança para padrões"""
        for pattern in patterns:
            # Score baseado na taxa de sucesso
            success_score = pattern.get('success_rate', 0) * 0.4
            
            # Score baseado no número de ocorrências
            usage_score = min(pattern.get('usage_count', 0) / 10, 0.3)
            
            # Score baseado na similaridade com clusters
            cluster_score = 0.0
            for cluster in clusters:
                if pattern['pattern_id'] in cluster.member_patterns:
                    cluster_score = cluster.confidence_score * 0.3
                    break
            
            # Score final
            pattern['confidence_score'] = success_score + usage_score + cluster_score
        
        return patterns
    
    def _generate_pattern_id(self, pattern_type: str, *components) -> str:
        """Gera ID único para um padrão"""
        content = f"{pattern_type}_{datetime.now().isoformat()}"
        for component in components:
            content += str(component)
        return hashlib.md5(content.encode()).hexdigest()
    
    def _save_learned_patterns(self, patterns: List[Dict]):
        """Salva padrões aprendidos"""
        # Atualizar padrões existentes
        for pattern in patterns:
            pattern_id = pattern['pattern_id']
            if pattern_id in self.patterns:
                # Atualizar padrão existente
                existing = self.patterns[pattern_id]
                existing['usage_count'] += 1
                existing['last_updated'] = pattern['last_updated']
                existing['confidence_score'] = pattern['confidence_score']
            else:
                # Adicionar novo padrão
                self.patterns[pattern_id] = pattern
        
        # Limitar número de padrões por tipo
        self._limit_patterns_per_type()
        
        # Salvar no arquivo
        self.save_patterns()
    
    def _limit_patterns_per_type(self):
        """Limita número de padrões por tipo"""
        for pattern_type in ['success', 'failure', 'optimization']:
            type_patterns = [
                (pid, p) for pid, p in self.patterns.items() 
                if p.get('pattern_type') == pattern_type
            ]
            
            if len(type_patterns) > self.max_patterns_per_type:
                # Manter padrões com maior confiança
                type_patterns.sort(key=lambda x: x[1].get('confidence_score', 0), reverse=True)
                patterns_to_remove = type_patterns[self.max_patterns_per_type:]
                
                for pid, _ in patterns_to_remove:
                    del self.patterns[pid]
    
    def find_similar_patterns(self, context: Dict[str, Any], pattern_type: str = None) -> List[PatternMatch]:
        """Encontra padrões similares ao contexto atual"""
        matches = []
        
        for pattern_id, pattern in self.patterns.items():
            # Filtrar por tipo se especificado
            if pattern_type and pattern.get('pattern_type') != pattern_type:
                continue
            
            # Calcular similaridade
            similarity = self._calculate_pattern_similarity(context, pattern)
            
            if similarity >= self.similarity_threshold:
                match = PatternMatch(
                    pattern_id=pattern_id,
                    confidence=pattern.get('confidence_score', 0),
                    matched_features=self._get_matched_features(context, pattern),
                    similarity_score=similarity
                )
                matches.append(match)
        
        # Ordenar por similaridade
        matches.sort(key=lambda m: m.similarity_score, reverse=True)
        return matches
    
    def _calculate_pattern_similarity(self, context: Dict[str, Any], pattern: Dict[str, Any]) -> float:
        """Calcula similaridade entre contexto e padrão"""
        pattern_keywords = set(pattern.get('context_keywords', []))
        context_keys = set(context.keys())
        
        if not pattern_keywords:
            return 0.0
        
        intersection = pattern_keywords.intersection(context_keys)
        union = pattern_keywords.union(context_keys)
        
        return len(intersection) / len(union) if union else 0.0
    
    def _get_matched_features(self, context: Dict[str, Any], pattern: Dict[str, Any]) -> List[str]:
        """Retorna características que deram match"""
        pattern_keywords = set(pattern.get('context_keywords', []))
        context_keys = set(context.keys())
        
        return list(pattern_keywords.intersection(context_keys)) 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = SourceanalyzerModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script pattern_analyzer.py executado com sucesso via módulo analysis.source_analyzer")
    else:
        print(f"❌ Erro na execução do script pattern_analyzer.py via módulo analysis.source_analyzer")

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
- **Nome**: migrated_pattern_analyzer
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

