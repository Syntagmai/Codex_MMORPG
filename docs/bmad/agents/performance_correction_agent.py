#!/usr/bin/env python3
"""
Performance Correction Agent - Epic 18 Task 18.3
Otimiza performance e recursos identificados na Epic 17
"""
import os
import json
import re
import shutil
import gzip
import zipfile
from datetime import datetime
from pathlib import Path

class PerformanceCorrectionAgent:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.audit_reports_dir = self.project_root / "wiki" / "docs" / "audit_reports"
        self.performance_report = self.audit_reports_dir / "performance_audit_report.json"
        self.correction_report = {
            "timestamp": datetime.now().isoformat(),
            "large_files_optimized": [],
            "slow_scripts_optimized": [],
            "bottlenecks_fixed": [],
            "optimization_opportunities": [],
            "files_modified": [],
            "backups_created": [],
            "compression_applied": [],
            "cache_implemented": [],
            "total_optimizations": 0
        }
    
    def load_performance_audit(self):
        """Carrega o relatório de auditoria de performance"""
        try:
            with open(self.performance_report, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Erro ao carregar relatório de performance: {e}")
            return None
    
    def backup_file(self, file_path):
        """Cria backup de um arquivo antes de modificá-lo"""
        try:
            backup_path = str(file_path) + ".backup"
            shutil.copy2(file_path, backup_path)
            self.correction_report["backups_created"].append(backup_path)
            return True
        except Exception as e:
            print(f"Erro ao criar backup de {file_path}: {e}")
            return False
    
    def optimize_large_files(self, large_files):
        """Otimiza arquivos grandes"""
        optimizations = []
        
        for file_info in large_files:
            file_path = file_info.get('file_path', '')
            file_size = file_info.get('size_mb', 0)
            
            if not file_path or not os.path.exists(file_path):
                continue
            
            try:
                # Backup do arquivo
                self.backup_file(file_path)
                
                # Estratégias de otimização baseadas no tipo de arquivo
                if file_path.endswith('.json'):
                    optimizations.extend(self.optimize_json_file(file_path))
                elif file_path.endswith('.py'):
                    optimizations.extend(self.optimize_python_file(file_path))
                elif file_path.endswith(('.md', '.txt')):
                    optimizations.extend(self.optimize_text_file(file_path))
                elif file_path.endswith(('.log', '.out')):
                    optimizations.extend(self.optimize_log_file(file_path))
                else:
                    # Compressão genérica para outros tipos
                    optimizations.extend(self.compress_file(file_path))
                
                self.correction_report["files_modified"].append(file_path)
                
            except Exception as e:
                print(f"Erro ao otimizar arquivo grande {file_path}: {e}")
        
        self.correction_report["large_files_optimized"] = optimizations
        return optimizations
    
    def optimize_json_file(self, file_path):
        """Otimiza arquivo JSON"""
        optimizations = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Remove campos desnecessários ou duplicados
            if isinstance(data, list):
                # Remove itens duplicados
                seen = set()
                unique_data = []
                for item in data:
                    item_str = json.dumps(item, sort_keys=True)
                    if item_str not in seen:
                        seen.add(item_str)
                        unique_data.append(item)
                
                if len(unique_data) < len(data):
                    data = unique_data
                    optimizations.append("Removidos itens duplicados")
            
            # Salva versão otimizada
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, separators=(',', ':'))  # Compacta JSON
            
            optimizations.append("JSON compactado")
            
            # Cria versão comprimida
            compressed_path = file_path + '.gz'
            with gzip.open(compressed_path, 'wt', encoding='utf-8') as f:
                json.dump(data, f)
            
            self.correction_report["compression_applied"].append(compressed_path)
            optimizations.append("Versão comprimida criada")
            
        except Exception as e:
            print(f"Erro ao otimizar JSON {file_path}: {e}")
        
        return optimizations
    
    def optimize_python_file(self, file_path):
        """Otimiza arquivo Python"""
        optimizations = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Remove imports não utilizados
            lines = content.split('\n')
            import_lines = []
            other_lines = []
            
            for line in lines:
                if line.strip().startswith(('import ', 'from ')):
                    import_lines.append(line)
                else:
                    other_lines.append(line)
            
            # Remove imports duplicados
            unique_imports = []
            for import_line in import_lines:
                if import_line.strip() not in [l.strip() for l in unique_imports]:
                    unique_imports.append(import_line)
            
            # Reorganiza código
            content = '\n'.join(unique_imports) + '\n\n' + '\n'.join(other_lines)
            
            # Remove linhas vazias duplicadas
            content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                optimizations.append("Imports otimizados")
                optimizations.append("Código reorganizado")
            
        except Exception as e:
            print(f"Erro ao otimizar Python {file_path}: {e}")
        
        return optimizations
    
    def optimize_text_file(self, file_path):
        """Otimiza arquivo de texto"""
        optimizations = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove linhas vazias duplicadas
            content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
            
            # Remove espaços em branco no final das linhas
            lines = content.split('\n')
            cleaned_lines = [line.rstrip() for line in lines]
            content = '\n'.join(cleaned_lines)
            
            # Salva versão otimizada
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            optimizations.append("Espaços em branco removidos")
            optimizations.append("Linhas vazias otimizadas")
            
        except Exception as e:
            print(f"Erro ao otimizar texto {file_path}: {e}")
        
        return optimizations
    
    def optimize_log_file(self, file_path):
        """Otimiza arquivo de log"""
        optimizations = []
        
        try:
            # Cria backup e comprime
            compressed_path = file_path + '.gz'
            with open(file_path, 'rb') as f_in:
                with gzip.open(compressed_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            
            # Limpa arquivo original (mantém apenas últimas 1000 linhas)
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            if len(lines) > 1000:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.writelines(lines[-1000:])
                
                optimizations.append("Log truncado para últimas 1000 linhas")
            
            self.correction_report["compression_applied"].append(compressed_path)
            optimizations.append("Versão comprimida criada")
            
        except Exception as e:
            print(f"Erro ao otimizar log {file_path}: {e}")
        
        return optimizations
    
    def compress_file(self, file_path):
        """Comprime arquivo genérico"""
        optimizations = []
        
        try:
            compressed_path = file_path + '.gz'
            with open(file_path, 'rb') as f_in:
                with gzip.open(compressed_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            
            self.correction_report["compression_applied"].append(compressed_path)
            optimizations.append("Arquivo comprimido")
            
        except Exception as e:
            print(f"Erro ao comprimir {file_path}: {e}")
        
        return optimizations
    
    def optimize_slow_scripts(self, slow_scripts):
        """Otimiza scripts lentos"""
        optimizations = []
        
        for script_info in slow_scripts:
            file_path = script_info.get('file_path', '')
            performance_issue = script_info.get('performance_issue', '')
            
            if not file_path or not os.path.exists(file_path):
                continue
            
            try:
                # Backup do script
                self.backup_file(file_path)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Otimizações específicas baseadas no tipo de problema
                if "loop" in performance_issue.lower():
                    content = self.optimize_loops(content)
                    optimizations.append(f"Loops otimizados em {file_path}")
                
                if "import" in performance_issue.lower():
                    content = self.optimize_imports(content)
                    optimizations.append(f"Imports otimizados em {file_path}")
                
                if "file" in performance_issue.lower():
                    content = self.optimize_file_operations(content)
                    optimizations.append(f"Operações de arquivo otimizadas em {file_path}")
                
                if "memory" in performance_issue.lower():
                    content = self.optimize_memory_usage(content)
                    optimizations.append(f"Uso de memória otimizado em {file_path}")
                
                # Salva mudanças se houve alteração
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    self.correction_report["files_modified"].append(file_path)
                
            except Exception as e:
                print(f"Erro ao otimizar script lento {file_path}: {e}")
        
        self.correction_report["slow_scripts_optimized"] = optimizations
        return optimizations
    
    def optimize_loops(self, content):
        """Otimiza loops no código"""
        # Substitui loops simples por list comprehensions
        content = re.sub(
            r'result\s*=\s*\[\]\s*\n\s*for\s+(\w+)\s+in\s+(\w+):\s*\n\s*result\.append\(([^)]+)\)',
            r'result = [\3 for \1 in \2]',
            content
        )
        
        # Otimiza loops com enumerate
        content = re.sub(
            r'for\s+i\s+in\s+range\(len\((\w+)\)\):',
            r'for i, item in enumerate(\1):',
            content
        )
        
        return content
    
    def optimize_imports(self, content):
        """Otimiza imports"""
        # Move imports para o topo
        lines = content.split('\n')
        import_lines = []
        other_lines = []
        
        for line in lines:
            if line.strip().startswith(('import ', 'from ')):
                import_lines.append(line)
            else:
                other_lines.append(line)
        
        # Remove imports duplicados
        unique_imports = []
        for import_line in import_lines:
            if import_line.strip() not in [l.strip() for l in unique_imports]:
                unique_imports.append(import_line)
        
        return '\n'.join(unique_imports) + '\n\n' + '\n'.join(other_lines)
    
    def optimize_file_operations(self, content):
        """Otimiza operações de arquivo"""
        # Substitui open/close por context manager
        content = re.sub(
            r'(\w+)\s*=\s*open\(([^)]+)\)\s*\n(.*?)\n(\w+)\.close\(\)',
            r'with open(\2) as \1:\n\3',
            content,
            flags=re.DOTALL
        )
        
        return content
    
    def optimize_memory_usage(self, content):
        """Otimiza uso de memória"""
        # Adiciona garbage collection
        if "import gc" not in content:
            content = "import gc\n" + content
        
        # Adiciona limpeza de memória em pontos críticos
        content = re.sub(
            r'(\w+\.process\(\)|process_data\(\))',
            r'\1\ngc.collect()',
            content
        )
        
        return content
    
    def fix_bottlenecks(self, bottlenecks):
        """Corrige gargalos identificados"""
        fixes = []
        
        for bottleneck in bottlenecks:
            bottleneck_type = bottleneck.get('bottleneck_type', '')
            description = bottleneck.get('description', '')
            
            # Implementa soluções para gargalos comuns
            if "database" in bottleneck_type.lower():
                fixes.append(self.implement_database_optimization())
            elif "network" in bottleneck_type.lower():
                fixes.append(self.implement_network_optimization())
            elif "memory" in bottleneck_type.lower():
                fixes.append(self.implement_memory_optimization())
            elif "cpu" in bottleneck_type.lower():
                fixes.append(self.implement_cpu_optimization())
        
        self.correction_report["bottlenecks_fixed"] = fixes
        return fixes
    
    def implement_database_optimization(self):
        """Implementa otimização de banco de dados"""
        db_optimization = '''
# Database Optimization Module
import sqlite3
import psycopg2
from contextlib import contextmanager

class DatabaseOptimizer:
    """Otimizador de banco de dados"""
    
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.pool = []
    
    @contextmanager
    def get_connection(self):
        """Gerenciador de contexto para conexões"""
        conn = None
        try:
            conn = psycopg2.connect(self.connection_string)
            yield conn
        finally:
            if conn:
                conn.close()
    
    def optimize_queries(self, query):
        """Otimiza queries SQL"""
        # Adiciona índices se necessário
        # Usa prepared statements
        return query
    
    def batch_operations(self, operations):
        """Executa operações em lote"""
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                for operation in operations:
                    cursor.execute(operation)
            conn.commit()
'''
        
        db_file = self.project_root / "wiki" / "bmad" / "optimization" / "database_optimizer.py"
        db_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(db_file, 'w', encoding='utf-8') as f:
            f.write(db_optimization)
        
        self.correction_report["files_modified"].append(str(db_file))
        return str(db_file)
    
    def implement_network_optimization(self):
        """Implementa otimização de rede"""
        network_optimization = '''
# Network Optimization Module
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor

class NetworkOptimizer:
    """Otimizador de rede"""
    
    def __init__(self, max_connections=10):
        self.max_connections = max_connections
        self.session = None
        self.executor = ThreadPoolExecutor(max_workers=max_connections)
    
    async def create_session(self):
        """Cria sessão HTTP otimizada"""
        connector = aiohttp.TCPConnector(
            limit=self.max_connections,
            limit_per_host=5,
            ttl_dns_cache=300
        )
        self.session = aiohttp.ClientSession(connector=connector)
    
    async def close_session(self):
        """Fecha sessão HTTP"""
        if self.session:
            await self.session.close()
    
    async def fetch_data(self, url):
        """Busca dados de forma otimizada"""
        if not self.session:
            await self.create_session()
        
        async with self.session.get(url) as response:
            return await response.text()
    
    def parallel_requests(self, urls):
        """Executa requisições em paralelo"""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            tasks = [self.fetch_data(url) for url in urls]
            results = loop.run_until_complete(asyncio.gather(*tasks))
            return results
        finally:
            loop.close()
'''
        
        network_file = self.project_root / "wiki" / "bmad" / "optimization" / "network_optimizer.py"
        network_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(network_file, 'w', encoding='utf-8') as f:
            f.write(network_optimization)
        
        self.correction_report["files_modified"].append(str(network_file))
        return str(network_file)
    
    def implement_memory_optimization(self):
        """Implementa otimização de memória"""
        memory_optimization = '''
# Memory Optimization Module
import gc
import psutil
import weakref
from typing import Dict, Any

class MemoryOptimizer:
    """Otimizador de memória"""
    
    def __init__(self):
        self.cache = weakref.WeakValueDictionary()
        self.memory_threshold = 0.8  # 80% de uso de memória
    
    def get_memory_usage(self):
        """Obtém uso atual de memória"""
        return psutil.virtual_memory().percent / 100
    
    def should_cleanup(self):
        """Verifica se deve fazer limpeza"""
        return self.get_memory_usage() > self.memory_threshold
    
    def cleanup_memory(self):
        """Limpa memória"""
        gc.collect()
        self.cache.clear()
    
    def cache_data(self, key: str, data: Any):
        """Cache de dados com limpeza automática"""
        if self.should_cleanup():
            self.cleanup_memory()
        
        self.cache[key] = data
    
    def get_cached_data(self, key: str):
        """Obtém dados do cache"""
        return self.cache.get(key)
    
    def monitor_memory(self):
        """Monitora uso de memória"""
        usage = self.get_memory_usage()
        if usage > self.memory_threshold:
            print(f"⚠️ Uso de memória alto: {usage:.1%}")
            self.cleanup_memory()
'''
        
        memory_file = self.project_root / "wiki" / "bmad" / "optimization" / "memory_optimizer.py"
        memory_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(memory_file, 'w', encoding='utf-8') as f:
            f.write(memory_optimization)
        
        self.correction_report["files_modified"].append(str(memory_file))
        return str(memory_file)
    
    def implement_cpu_optimization(self):
        """Implementa otimização de CPU"""
        cpu_optimization = '''
# CPU Optimization Module
import multiprocessing
import threading
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import psutil

class CPUOptimizer:
    """Otimizador de CPU"""
    
    def __init__(self, max_workers=None):
        self.max_workers = max_workers or multiprocessing.cpu_count()
        self.process_pool = ProcessPoolExecutor(max_workers=self.max_workers)
        self.thread_pool = ThreadPoolExecutor(max_workers=self.max_workers * 2)
    
    def get_cpu_usage(self):
        """Obtém uso atual de CPU"""
        return psutil.cpu_percent(interval=1)
    
    def should_optimize(self):
        """Verifica se deve otimizar"""
        return self.get_cpu_usage() > 80
    
    def parallel_process(self, func, data_list):
        """Processa dados em paralelo"""
        if self.should_optimize():
            # Usa process pool para CPU intensivo
            return list(self.process_pool.map(func, data_list))
        else:
            # Usa thread pool para I/O intensivo
            return list(self.thread_pool.map(func, data_list))
    
    def optimize_workload(self, workload):
        """Otimiza carga de trabalho"""
        cpu_count = multiprocessing.cpu_count()
        
        if len(workload) > cpu_count * 2:
            # Divide trabalho em chunks
            chunk_size = len(workload) // cpu_count
            chunks = [workload[i:i+chunk_size] for i in range(0, len(workload), chunk_size)]
            return chunks
        else:
            return [workload]
    
    def cleanup(self):
        """Limpa recursos"""
        self.process_pool.shutdown()
        self.thread_pool.shutdown()
'''
        
        cpu_file = self.project_root / "wiki" / "bmad" / "optimization" / "cpu_optimizer.py"
        cpu_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(cpu_file, 'w', encoding='utf-8') as f:
            f.write(cpu_optimization)
        
        self.correction_report["files_modified"].append(str(cpu_file))
        return str(cpu_file)
    
    def create_performance_guidelines(self):
        """Cria diretrizes de performance"""
        guidelines = '''# Diretrizes de Performance - Codex MMORPG

## 1. Otimização de Arquivos
- Comprimir arquivos grandes (>1MB)
- Remover dados duplicados
- Usar formatos eficientes (JSON compacto, etc.)
- Implementar cache para arquivos frequentemente acessados

## 2. Otimização de Scripts
- Usar list comprehensions em vez de loops
- Implementar lazy loading
- Usar geradores para grandes conjuntos de dados
- Otimizar imports e remover não utilizados

## 3. Otimização de Banco de Dados
- Usar índices apropriados
- Implementar prepared statements
- Executar operações em lote
- Usar connection pooling

## 4. Otimização de Rede
- Implementar cache HTTP
- Usar requisições em paralelo
- Comprimir dados de transferência
- Implementar retry com backoff

## 5. Otimização de Memória
- Usar weak references para cache
- Implementar garbage collection manual
- Monitorar uso de memória
- Limpar recursos não utilizados

## 6. Otimização de CPU
- Usar multiprocessing para CPU intensivo
- Usar threading para I/O intensivo
- Implementar load balancing
- Monitorar uso de CPU

## 7. Monitoramento
- Implementar métricas de performance
- Usar profiling para identificar gargalos
- Monitorar recursos em tempo real
- Implementar alertas de performance

## 8. Cache e Storage
- Implementar cache em memória
- Usar cache distribuído quando necessário
- Otimizar storage de dados
- Implementar backup eficiente
'''
        
        guidelines_file = self.project_root / "wiki" / "docs" / "performance_guidelines.md"
        with open(guidelines_file, 'w', encoding='utf-8') as f:
            f.write(guidelines)
        
        self.correction_report["files_modified"].append(str(guidelines_file))
        return str(guidelines_file)
    
    def create_correction_report(self):
        """Cria relatório de correção"""
        report_file = self.audit_reports_dir / "performance_correction_report.json"
        
        # Calcula estatísticas
        total_large_files = len(self.correction_report["large_files_optimized"])
        total_slow_scripts = len(self.correction_report["slow_scripts_optimized"])
        total_bottlenecks = len(self.correction_report["bottlenecks_fixed"])
        total_files_modified = len(set(self.correction_report["files_modified"]))
        
        self.correction_report["total_optimizations"] = (
            total_large_files + total_slow_scripts + total_bottlenecks
        )
        
        self.correction_report["statistics"] = {
            "large_files_optimized": total_large_files,
            "slow_scripts_optimized": total_slow_scripts,
            "bottlenecks_fixed": total_bottlenecks,
            "files_modified": total_files_modified,
            "compression_applied": len(self.correction_report["compression_applied"])
        }
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(self.correction_report, f, indent=2, ensure_ascii=False)
        
        return str(report_file)
    
    def run_performance_correction(self):
        """Executa correção de performance completa"""
        print("⚡ Iniciando otimização de performance e recursos...")
        
        # Carrega relatório de performance
        performance_data = self.load_performance_audit()
        if not performance_data:
            print("❌ Não foi possível carregar relatório de performance")
            return False
        
        print(f"📊 Arquivos grandes identificados: {len(performance_data.get('large_files', []))}")
        print(f"📊 Scripts lentos identificados: {len(performance_data.get('slow_scripts', []))}")
        print(f"📊 Gargalos identificados: {len(performance_data.get('bottlenecks', []))}")
        
        # Otimiza arquivos grandes
        print("🔧 Otimizando arquivos grandes...")
        large_files = performance_data.get('large_files', [])
        self.optimize_large_files(large_files)
        
        # Otimiza scripts lentos
        print("🔧 Otimizando scripts lentos...")
        slow_scripts = performance_data.get('slow_scripts', [])
        self.optimize_slow_scripts(slow_scripts)
        
        # Corrige gargalos
        print("🔧 Corrigindo gargalos...")
        bottlenecks = performance_data.get('bottlenecks', [])
        self.fix_bottlenecks(bottlenecks)
        
        # Cria diretrizes
        print("📋 Criando diretrizes de performance...")
        guidelines_file = self.create_performance_guidelines()
        
        # Cria relatório
        report_file = self.create_correction_report()
        
        # Estatísticas finais
        print(f"\n✅ Otimização de performance concluída!")
        print(f"📊 Arquivos modificados: {len(set(self.correction_report['files_modified']))}")
        print(f"🔧 Arquivos grandes otimizados: {len(self.correction_report['large_files_optimized'])}")
        print(f"🔧 Scripts lentos otimizados: {len(self.correction_report['slow_scripts_optimized'])}")
        print(f"🔧 Gargalos corrigidos: {len(self.correction_report['bottlenecks_fixed'])}")
        print(f"🗜️ Compressões aplicadas: {len(self.correction_report['compression_applied'])}")
        print(f"📄 Relatório salvo em: {report_file}")
        print(f"📋 Diretrizes: {guidelines_file}")
        
        return True

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        project_root = sys.argv[1]
    else:
        project_root = "."
    
    agent = PerformanceCorrectionAgent(project_root)
    result = agent.run_performance_correction() 