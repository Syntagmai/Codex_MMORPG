from unicode_aliases import *
# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
MAX_ITEMS = 100
MAX_SIZE = 1000

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: data_collector.py
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
Sistema de Coleta de Dados para Auto-Aprendizado
Coleta e armazena dados de todas as interações do sistema BMAD
"""

import json
import sqlite3
import hashlib
from datetime import datetime, timedelta
import threading

@dataclass
class InteractionRecord:
    """Registro de uma interação no banco de dados"""
    interaction_id: str
    timestamp: str
    user_request: str
    context_detected: str  # JSON string
    agents_selected: str   # JSON string
    workflow_executed: str
    execution_time: float
    success_score: float
    user_feedback: Optional[str] = None
    error_message: Optional[str] = None
    optimization_applied: bool = False
    metadata: str = ""  # JSON string para dados adicionais

class DataCollector:
    """Sistema de coleta e armazenamento de dados de interações"""
    
    def __init__(self, data_path: Path):
        self.data_path = data_path
        self.db_path = data_path / "interactions.db"
        self.json_path = data_path / "interactions"
        
        # Criar pastas necessárias
        self.json_path.mkdir(parents=True, exist_ok=True)
        
        # Inicializar banco de dados
        self.init_database()
        
        # Lock para operações thread-safe
        self.db_lock = threading.Lock()
        
        # Cache de estatísticas
        self.stats_cache = {}
        self.stats_cache_timestamp = None
        self.cache_validity = 300  # 5 minutos
    
    def init_database(self):
        """Inicializa banco de dados SQLite"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Tabela principal de interações
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS interactions (
                    interaction_id TEXT PRIMARY KEY,
                    timestamp TEXT NOT NULL,
                    user_request TEXT NOT NULL,
                    context_detected TEXT NOT NULL,
                    agents_selected TEXT NOT NULL,
                    workflow_executed TEXT NOT NULL,
                    execution_time REAL NOT NULL,
                    success_score REAL NOT NULL,
                    user_feedback TEXT,
                    error_message TEXT,
                    optimization_applied BOOLEAN DEFAULT FALSE,
                    metadata TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Tabela de índices para busca rápida
            cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_timestamp ON interactions(timestamp)
            ''')
            cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_success_score ON interactions(success_score)
            ''')
            cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_workflow ON interactions(workflow_executed)
            ''')
            cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_optimization ON interactions(optimization_applied)
            ''')
            
            # Tabela de feedback
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS feedback (
                    feedback_id TEXT PRIMARY KEY,
                    interaction_id TEXT NOT NULL,
                    feedback_text TEXT NOT NULL,
                    feedback_score REAL NOT NULL,
                    timestamp TEXT NOT NULL,
                    FOREIGN KEY (interaction_id) REFERENCES interactions (interaction_id)
                )
            ''')
            
            # Tabela de métricas agregadas
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS aggregated_metrics (
                    metric_id TEXT PRIMARY KEY,
                    metric_name TEXT NOT NULL,
                    metric_value REAL NOT NULL,
                    metric_count INTEGER NOT NULL,
                    time_period TEXT NOT NULL,
                    timestamp TEXT NOT NULL
                )
            ''')
            
            conn.commit()
    
    def generate_interaction_id(self, user_request: str, timestamp: str) -> str:
        """Gera ID único para uma interação"""
        content = f"{user_request}_{timestamp}"
        return hashlib.md5(content.encode()).hexdigest()
    
    def save_interaction(self, interaction_data) -> str:
        """Salva uma nova interação no sistema"""
        # Gerar ID único
        interaction_id = self.generate_interaction_id(
            interaction_data.user_request, 
            interaction_data.timestamp
        )
        
        # Preparar dados para banco
        record = InteractionRecord(
            interaction_id=interaction_id,
            timestamp=interaction_data.timestamp,
            user_request=interaction_data.user_request,
            context_detected=json.dumps(interaction_data.context_detected, ensure_ascii=False),
            agents_selected=json.dumps(interaction_data.agents_selected, ensure_ascii=False),
            workflow_executed=interaction_data.workflow_executed,
            execution_time=interaction_data.execution_time,
            success_score=interaction_data.success_score,
            user_feedback=interaction_data.user_feedback,
            error_message=interaction_data.error_message,
            optimization_applied=interaction_data.optimization_applied,
            metadata=json.dumps({
                'context_keywords': list(interaction_data.context_detected.keys()),
                'agent_count': len(interaction_data.agents_selected),
                'complexity_score': self._calculate_complexity(interaction_data)
            }, ensure_ascii=False)
        )
        
        # Salvar no banco de dados
        with self.db_lock:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT OR REPLACE INTO interactions 
                    (interaction_id, timestamp, user_request, context_detected, 
                     agents_selected, workflow_executed, execution_time, success_score,
                     user_feedback, error_message, optimization_applied, metadata)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    record.interaction_id, record.timestamp, record.user_request,
                    record.context_detected, record.agents_selected, record.workflow_executed,
                    record.execution_time, record.success_score, record.user_feedback,
                    record.error_message, record.optimization_applied, record.metadata
                ))
                conn.commit()
        
        # Salvar backup em JSON
        self._save_json_backup(record)
        
        # Invalidar cache de estatísticas
        self.stats_cache = {}
        self.stats_cache_timestamp = None
        
        return interaction_id
    
    def _calculate_complexity(self, interaction_data) -> float:
        """Calcula score de complexidade da interação"""
        complexity = 0.0
        
        # Complexidade baseada no número de agentes
        complexity += len(interaction_data.agents_selected) * 0.2
        
        # Complexidade baseada no tempo de execução
        if interaction_data.execution_time > 10:
            complexity += 0.3
        elif interaction_data.execution_time > 5:
            complexity += 0.2
        elif interaction_data.execution_time > 2:
            complexity += 0.1
        
        # Complexidade baseada no contexto
        context_size = len(interaction_data.context_detected)
        complexity += min(context_size * 0.1, 0.5)
        
        # Complexidade baseada no tamanho da requisição
        request_length = len(interaction_data.user_request)
        complexity += min(request_length / 1000, 0.3)
        
        return min(complexity, 1.0)
    
    def _save_json_backup(self, record: InteractionRecord):
        """Salva backup em formato JSON"""
        date_str = record.timestamp[:10]  # YYYY-MM-DD
        json_file = self.json_path / f"interactions_{date_str}.json"
        
        # Carregar dados existentes ou criar novo
        if json_file.exists():
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        else:
            data = []
        
        # Adicionar novo registro
        data.append(asdict(record))
        
        # Salvar arquivo
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def get_interaction(self, interaction_id: str) -> Optional[Dict[str, Any]]:
        """Recupera uma interação específica"""
        with self.db_lock:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT * FROM interactions WHERE interaction_id = ?
                ''', (interaction_id,))
                
                row = cursor.fetchone()
                if row:
                    return self._row_to_dict(row, cursor.description)
                return None
    
    def get_interactions(self, limit: int = 100, offset: int = 0, 
                        filters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Recupera múltiplas interações com filtros"""
        query = "SELECT * FROM interactions"
        params = []
        
        # Aplicar filtros
        if filters:
            conditions = []
            for key, value in filters.items():
                if key == 'min_success_score':
                    conditions.append("success_score >= ?")
                    params.append(value)
                elif key == 'max_execution_time':
                    conditions.append("execution_time <= ?")
                    params.append(value)
                elif key == 'workflow_type':
                    conditions.append("workflow_executed LIKE ?")
                    params.append(f"%{value}%")
                elif key == 'date_from':
                    conditions.append("timestamp >= ?")
                    params.append(value)
                elif key == 'date_to':
                    conditions.append("timestamp <= ?")
                    params.append(value)
            
            if conditions:
                query += " WHERE " + " AND ".join(conditions)
        
        # Ordenar e limitar
        query += " ORDER BY timestamp DESC LIMIT ? OFFSET ?"
        params.extend([limit, offset])
        
        with self.db_lock:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                
                rows = cursor.fetchall()
                return [self._row_to_dict(row, cursor.description) for row in rows]
    
    def _row_to_dict(self, row: tuple, description) -> Dict[str, Any]:
        """Converte linha do banco em dicionário"""
        result = {}
        for i, (name, *_) in enumerate(description):
            value = row[i]
            
            # Converter JSON strings de volta para objetos
            if name in ['context_detected', 'agents_selected', 'metadata'] and value:
                try:
                    result[name] = json.loads(value)
                except json.JSONDecodeError:
                    result[name] = value
            else:
                result[name] = value
        
        return result
    
    def get_total_interactions(self) -> int:
        """Retorna total de interações no sistema"""
        with self.db_lock:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT COUNT(*) FROM interactions")
                return cursor.fetchone()[0]
    
    def get_interaction_stats(self) -> Dict[str, Any]:
        """Retorna estatísticas das interações"""
        # Verificar cache
        if (self.stats_cache and self.stats_cache_timestamp and 
            (datetime.now() - self.stats_cache_timestamp).seconds < self.cache_validity):
            return self.stats_cache
        
        with self.db_lock:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Estatísticas básicas
                cursor.execute("SELECT COUNT(*) FROM interactions")
                total_interactions = cursor.fetchone()[0]
                
                cursor.execute("SELECT AVG(success_score) FROM interactions")
                avg_success = cursor.fetchone()[0] or 0.0
                
                cursor.execute("SELECT AVG(execution_time) FROM interactions")
                avg_execution_time = cursor.fetchone()[0] or 0.0
                
                cursor.execute("SELECT COUNT(*) FROM interactions WHERE optimization_applied = 1")
                optimized_interactions = cursor.fetchone()[0]
                
                # Estatísticas por workflow
                cursor.execute('''
                    SELECT workflow_executed, COUNT(*) as count, AVG(success_score) as avg_success
                    FROM interactions 
                    GROUP BY workflow_executed 
                    ORDER BY count DESC 
                    LIMIT 10
                ''')
                workflow_stats = cursor.fetchall()
                
                # Estatísticas por período
                cursor.execute('''
                    SELECT DATE(timestamp) as date, COUNT(*) as count
                    FROM interactions 
                    GROUP BY DATE(timestamp)
                    ORDER BY date DESC 
                    LIMIT 30
                ''')
                daily_stats = cursor.fetchall()
                
                stats = {
                    'total_interactions': total_interactions,
                    'avg_success_score': avg_success,
                    'avg_execution_time': avg_execution_time,
                    'optimized_interactions': optimized_interactions,
                    'optimization_rate': (optimized_interactions / total_interactions * 100) if total_interactions > 0 else 0,
    
                    'workflow_stats': [
                        {'workflow': w[0], 'count': w[1], 'avg_success': w[2]} 
                        for w in workflow_stats
                    ],
                    'daily_stats': [
                        {'date': d[0], 'count': d[1]} 
                        for d in daily_stats
                    ]
                }
                
                # Atualizar cache
                self.stats_cache = stats
                self.stats_cache_timestamp = datetime.now()
                
                return stats
    
    def add_feedback(self, interaction_id: str, feedback_text: str, feedback_score: float):
        """Adiciona feedback a uma interação"""
        feedback_id = hashlib.md5(f"{interaction_id}_{feedback_text}".encode()).hexdigest()
        
        with self.db_lock:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT OR REPLACE INTO feedback 
                    (feedback_id, interaction_id, feedback_text, feedback_score, timestamp)
                    VALUES (?, ?, ?, ?, ?)
                ''', (feedback_id, interaction_id, feedback_text, feedback_score, datetime.now().isoformat()))
                
                # Atualizar interação com feedback
                cursor.execute('''
                    UPDATE interactions 
                    SET user_feedback = ? 
                    WHERE interaction_id = ?
                ''', (feedback_text, interaction_id))
                
                conn.commit()
    
    def cleanup_old_data(self, days_to_keep: int = 90):
        """Remove dados antigos do sistema"""
        cutoff_date = (datetime.now() - timedelta(days=days_to_keep)).isoformat()
        
        with self.db_lock:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Remover interações antigas
                cursor.execute('''
                    DELETE FROM interactions WHERE timestamp < ?
                ''', (cutoff_date,))
                
                # Remover feedback de interações removidas
                cursor.execute('''
                    DELETE FROM feedback 
                    WHERE interaction_id NOT IN (SELECT interaction_id FROM interactions)
                ''')
                
                # Remover métricas antigas
                cursor.execute('''
                    DELETE FROM aggregated_metrics WHERE timestamp < ?
                ''', (cutoff_date,))
                
                conn.commit()
        
        # Limpar arquivos JSON antigos
        self._cleanup_old_json_files(days_to_keep)
    
    def _cleanup_old_json_files(self, days_to_keep: int):
        """Remove arquivos JSON antigos"""
        cutoff_date = datetime.now() - timedelta(days=days_to_keep)
        
        for json_file in self.json_path.glob("interactions_*.json"):
            try:
                # Extrair data do nome do arquivo
                date_str = json_file.stem.split('_')[1]
                file_date = datetime.strptime(date_str, '%Y-%m-%d')
                
                if file_date < cutoff_date:
                    json_file.unlink()
            except (ValueError, IndexError):
                # Se não conseguir extrair data, manter arquivo
                continue 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = GitautomationModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script data_collector.py executado com sucesso via módulo tools.git_automation")
    else:
        print(f"❌ Erro na execução do script data_collector.py via módulo tools.git_automation")

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
- **Nome**: migrated_data_collector
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

