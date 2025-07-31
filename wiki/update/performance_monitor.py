#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Monitoramento de Performance
=======================================

Este script monitora a performance do sistema OTClient Documentation,
incluindo uso de recursos, tempo de resposta e métricas de qualidade.

Autor: Sistema BMAD - OTClient Documentation
Data: 2024-12-19
"""

import json
import os
import time
import psutil
import threading
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import logging

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PerformanceMonitor:
    """Sistema de monitoramento de performance."""
    
    def __init__(self, project_root: str = "../..", monitor_dir: str = "../monitoring"):
        """
        Inicializa o monitor de performance.
        
        Args:
            project_root: Diretório raiz do projeto
            monitor_dir: Diretório para armazenar dados de monitoramento
        """
        self.project_root = Path(project_root).resolve()
        self.monitor_dir = Path(monitor_dir).resolve()
        self.monitor_dir.mkdir(exist_ok=True)
        
        # Configurações
        self.monitoring_interval = 60  # segundos
        self.max_history_days = 30
        self.performance_thresholds = {
            'cpu_usage': 80.0,  # %
            'memory_usage': 85.0,  # %
            'disk_usage': 90.0,  # %
            'response_time': 5.0,  # segundos
            'file_size_mb': 100.0  # MB
        }
        
        # Dados de monitoramento
        self.metrics_file = self.monitor_dir / "performance_metrics.json"
        self.alerts_file = self.monitor_dir / "performance_alerts.json"
        self.load_metrics()
        
        # Status de monitoramento
        self.is_monitoring = False
        self.monitor_thread = None
    
    def load_metrics(self):
        """Carrega métricas de performance existentes."""
        if self.metrics_file.exists():
            with open(self.metrics_file, 'r', encoding='utf-8') as f:
                self.metrics_data = json.load(f)
        else:
            self.metrics_data = {
                'metrics': [],
                'alerts': [],
                'settings': {
                    'monitoring_interval': self.monitoring_interval,
                    'max_history_days': self.max_history_days,
                    'thresholds': self.performance_thresholds
                }
            }
        
        if self.alerts_file.exists():
            with open(self.alerts_file, 'r', encoding='utf-8') as f:
                self.alerts_data = json.load(f)
        else:
            self.alerts_data = {
                'alerts': [],
                'last_alert_time': None
            }
    
    def save_metrics(self):
        """Salva métricas de performance."""
        with open(self.metrics_file, 'w', encoding='utf-8') as f:
            json.dump(self.metrics_data, f, indent=2, ensure_ascii=False)
        
        with open(self.alerts_file, 'w', encoding='utf-8') as f:
            json.dump(self.alerts_data, f, indent=2, ensure_ascii=False)
    
    def collect_system_metrics(self) -> Dict[str, Any]:
        """Coleta métricas do sistema."""
        try:
            # CPU
            cpu_percent = psutil.cpu_percent(interval=1)
            cpu_count = psutil.cpu_count()
            
            # Memória
            memory = psutil.virtual_memory()
            memory_percent = memory.percent
            memory_available = memory.available / (1024 * 1024 * 1024)  # GB
            
            # Disco
            disk = psutil.disk_usage(self.project_root)
            disk_percent = (disk.used / disk.total) * 100
            disk_free = disk.free / (1024 * 1024 * 1024)  # GB
            
            # Processos Python
            python_processes = []
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    if 'python' in proc.info['name'].lower():
                        python_processes.append(proc.info)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            
            return {
                'timestamp': datetime.now().isoformat(),
                'cpu': {
                    'usage_percent': cpu_percent,
                    'count': cpu_count
                },
                'memory': {
                    'usage_percent': memory_percent,
                    'available_gb': memory_available,
                    'total_gb': memory.total / (1024 * 1024 * 1024)
                },
                'disk': {
                    'usage_percent': disk_percent,
                    'free_gb': disk_free,
                    'total_gb': disk.total / (1024 * 1024 * 1024)
                },
                'python_processes': python_processes
            }
            
        except Exception as e:
            logger.error(f"Erro ao coletar métricas do sistema: {e}")
            return {}
    
    def collect_project_metrics(self) -> Dict[str, Any]:
        """Coleta métricas específicas do projeto."""
        try:
            metrics = {
                'timestamp': datetime.now().isoformat(),
                'file_count': 0,
                'total_size_mb': 0,
                'largest_files': [],
                'recent_changes': [],
                'json_maps': {}
            }
            
            # Contar arquivos e tamanho
            for file_path in self.project_root.rglob('*'):
                if file_path.is_file():
                    metrics['file_count'] += 1
                    file_size_mb = file_path.stat().st_size / (1024 * 1024)
                    metrics['total_size_mb'] += file_size_mb
                    
                    # Manter lista dos maiores arquivos
                    if file_size_mb > 1.0:  # > 1MB
                        metrics['largest_files'].append({
                            'path': str(file_path.relative_to(self.project_root)),
                            'size_mb': file_size_mb
                        })
            
            # Ordenar maiores arquivos
            metrics['largest_files'].sort(key=lambda x: x['size_mb'], reverse=True)
            metrics['largest_files'] = metrics['largest_files'][:10]
            
            # Verificar mudanças recentes (últimas 24h)
            cutoff_time = datetime.now() - timedelta(hours=24)
            for file_path in self.project_root.rglob('*'):
                if file_path.is_file():
                    mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
                    if mtime > cutoff_time:
                        metrics['recent_changes'].append({
                            'path': str(file_path.relative_to(self.project_root)),
                            'modified': mtime.isoformat(),
                            'size_mb': file_path.stat().st_size / (1024 * 1024)
                        })
            
            # Analisar mapas JSON
            maps_dir = self.project_root / "wiki" / "maps"
            if maps_dir.exists():
                for json_file in maps_dir.glob("*.json"):
                    try:
                        file_size_mb = json_file.stat().st_size / (1024 * 1024)
                        metrics['json_maps'][json_file.name] = {
                            'size_mb': file_size_mb,
                            'modified': datetime.fromtimestamp(json_file.stat().st_mtime).isoformat()
                        }
                    except Exception as e:
                        logger.warning(f"Erro ao analisar {json_file}: {e}")
            
            return metrics
            
        except Exception as e:
            logger.error(f"Erro ao coletar métricas do projeto: {e}")
            return {}
    
    def check_performance_thresholds(self, system_metrics: Dict[str, Any], project_metrics: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Verifica se as métricas excedem os limites definidos."""
        alerts = []
        
        # Verificar CPU
        if system_metrics.get('cpu', {}).get('usage_percent', 0) > self.performance_thresholds['cpu_usage']:
            alerts.append({
                'type': 'high_cpu_usage',
                'severity': 'warning',
                'message': f"CPU usage: {system_metrics['cpu']['usage_percent']:.1f}%",
                'threshold': self.performance_thresholds['cpu_usage'],
                'timestamp': datetime.now().isoformat()
            })
        
        # Verificar memória
        if system_metrics.get('memory', {}).get('usage_percent', 0) > self.performance_thresholds['memory_usage']:
            alerts.append({
                'type': 'high_memory_usage',
                'severity': 'warning',
                'message': f"Memory usage: {system_metrics['memory']['usage_percent']:.1f}%",
                'threshold': self.performance_thresholds['memory_usage'],
                'timestamp': datetime.now().isoformat()
            })
        
        # Verificar disco
        if system_metrics.get('disk', {}).get('usage_percent', 0) > self.performance_thresholds['disk_usage']:
            alerts.append({
                'type': 'high_disk_usage',
                'severity': 'critical',
                'message': f"Disk usage: {system_metrics['disk']['usage_percent']:.1f}%",
                'threshold': self.performance_thresholds['disk_usage'],
                'timestamp': datetime.now().isoformat()
            })
        
        # Verificar tamanho total do projeto
        if project_metrics.get('total_size_mb', 0) > self.performance_thresholds['file_size_mb']:
            alerts.append({
                'type': 'large_project_size',
                'severity': 'info',
                'message': f"Project size: {project_metrics['total_size_mb']:.1f}MB",
                'threshold': self.performance_thresholds['file_size_mb'],
                'timestamp': datetime.now().isoformat()
            })
        
        # Verificar mapas JSON grandes
        for map_name, map_info in project_metrics.get('json_maps', {}).items():
            if map_info['size_mb'] > 50:  # > 50MB
                alerts.append({
                    'type': 'large_json_map',
                    'severity': 'info',
                    'message': f"Large JSON map: {map_name} ({map_info['size_mb']:.1f}MB)",
                    'threshold': 50,
                    'timestamp': datetime.now().isoformat()
                })
        
        return alerts
    
    def record_metrics(self, system_metrics: Dict[str, Any], project_metrics: Dict[str, Any], alerts: List[Dict[str, Any]]):
        """Registra métricas coletadas."""
        # Adicionar métricas
        combined_metrics = {
            'timestamp': datetime.now().isoformat(),
            'system': system_metrics,
            'project': project_metrics,
            'alerts': alerts
        }
        
        self.metrics_data['metrics'].append(combined_metrics)
        
        # Adicionar alertas
        for alert in alerts:
            self.alerts_data['alerts'].append(alert)
        
        # Limpar histórico antigo
        self._cleanup_old_metrics()
        
        # Salvar dados
        self.save_metrics()
    
    def _cleanup_old_metrics(self):
        """Remove métricas antigas para economizar espaço."""
        cutoff_date = datetime.now() - timedelta(days=self.max_history_days)
        
        # Limpar métricas antigas
        self.metrics_data['metrics'] = [
            metric for metric in self.metrics_data['metrics']
            if datetime.fromisoformat(metric['timestamp']) > cutoff_date
        ]
        
        # Limpar alertas antigos
        self.alerts_data['alerts'] = [
            alert for alert in self.alerts_data['alerts']
            if datetime.fromisoformat(alert['timestamp']) > cutoff_date
        ]
    
    def start_monitoring(self):
        """Inicia o monitoramento contínuo."""
        if self.is_monitoring:
            logger.warning("Monitoramento já está ativo")
            return
        
        self.is_monitoring = True
        self.monitor_thread = threading.Thread(target=self._monitoring_loop, daemon=True)
        self.monitor_thread.start()
        logger.info("Monitoramento de performance iniciado")
    
    def stop_monitoring(self):
        """Para o monitoramento contínuo."""
        self.is_monitoring = False
        if self.monitor_thread:
            self.monitor_thread.join()
        logger.info("Monitoramento de performance parado")
    
    def _monitoring_loop(self):
        """Loop principal de monitoramento."""
        while self.is_monitoring:
            try:
                # Coletar métricas
                system_metrics = self.collect_system_metrics()
                project_metrics = self.collect_project_metrics()
                
                # Verificar limites
                alerts = self.check_performance_thresholds(system_metrics, project_metrics)
                
                # Registrar métricas
                self.record_metrics(system_metrics, project_metrics, alerts)
                
                # Log de alertas críticos
                for alert in alerts:
                    if alert['severity'] == 'critical':
                        logger.critical(f"ALERTA CRÍTICO: {alert['message']}")
                    elif alert['severity'] == 'warning':
                        logger.warning(f"ALERTA: {alert['message']}")
                
                # Aguardar próximo ciclo
                time.sleep(self.monitoring_interval)
                
            except Exception as e:
                logger.error(f"Erro no loop de monitoramento: {e}")
                time.sleep(self.monitoring_interval)
    
    def get_performance_report(self) -> Dict[str, Any]:
        """Gera relatório de performance."""
        if not self.metrics_data['metrics']:
            return {
                'status': 'no_data',
                'message': 'Nenhuma métrica disponível'
            }
        
        # Métricas mais recentes
        latest_metrics = self.metrics_data['metrics'][-1]
        
        # Calcular médias das últimas 24h
        cutoff_time = datetime.now() - timedelta(hours=24)
        recent_metrics = [
            m for m in self.metrics_data['metrics']
            if datetime.fromisoformat(m['timestamp']) > cutoff_time
        ]
        
        if recent_metrics:
            avg_cpu = sum(m['system'].get('cpu', {}).get('usage_percent', 0) for m in recent_metrics) / len(recent_metrics)
            avg_memory = sum(m['system'].get('memory', {}).get('usage_percent', 0) for m in recent_metrics) / len(recent_metrics)
            avg_disk = sum(m['system'].get('disk', {}).get('usage_percent', 0) for m in recent_metrics) / len(recent_metrics)
        else:
            avg_cpu = avg_memory = avg_disk = 0
        
        # Alertas recentes
        recent_alerts = [
            alert for alert in self.alerts_data['alerts']
            if datetime.fromisoformat(alert['timestamp']) > cutoff_time
        ]
        
        return {
            'status': 'active',
            'current_metrics': latest_metrics,
            'averages_24h': {
                'cpu_usage': avg_cpu,
                'memory_usage': avg_memory,
                'disk_usage': avg_disk
            },
            'recent_alerts': recent_alerts,
            'total_metrics_recorded': len(self.metrics_data['metrics']),
            'total_alerts': len(self.alerts_data['alerts'])
        }

def main():
    """Função principal do script."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Monitor de Performance OTClient')
    parser.add_argument('action', choices=['start', 'stop', 'status', 'report'],
                       help='Ação a executar')
    parser.add_argument('--interval', type=int, default=60,
                       help='Intervalo de monitoramento em segundos')
    parser.add_argument('--duration', type=int, default=0,
                       help='Duração do monitoramento em segundos (0 = indefinido)')
    
    args = parser.parse_args()
    
    monitor = PerformanceMonitor()
    
    if args.action == 'start':
        print("🔄 Iniciando monitoramento de performance...")
        monitor.monitoring_interval = args.interval
        monitor.start_monitoring()
        
        if args.duration > 0:
            print(f"⏱️ Monitoramento por {args.duration} segundos...")
            time.sleep(args.duration)
            monitor.stop_monitoring()
            print("✅ Monitoramento concluído")
        else:
            print("🔄 Monitoramento contínuo ativo (Ctrl+C para parar)")
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                monitor.stop_monitoring()
                print("\n✅ Monitoramento parado")
    
    elif args.action == 'stop':
        print("🛑 Parando monitoramento...")
        monitor.stop_monitoring()
        print("✅ Monitoramento parado")
    
    elif args.action == 'status':
        print("📊 Status do monitoramento:")
        if monitor.is_monitoring:
            print("  Status: Ativo")
            print(f"  Intervalo: {monitor.monitoring_interval} segundos")
        else:
            print("  Status: Inativo")
    
    elif args.action == 'report':
        print("📋 Relatório de performance:")
        report = monitor.get_performance_report()
        
        if report['status'] == 'no_data':
            print("  Nenhum dado disponível")
        else:
            current = report['current_metrics']
            averages = report['averages_24h']
            
            print(f"  CPU atual: {current['system']['cpu']['usage_percent']:.1f}%")
            print(f"  CPU média (24h): {averages['cpu_usage']:.1f}%")
            print(f"  Memória atual: {current['system']['memory']['usage_percent']:.1f}%")
            print(f"  Memória média (24h): {averages['memory_usage']:.1f}%")
            print(f"  Disco atual: {current['system']['disk']['usage_percent']:.1f}%")
            print(f"  Disco média (24h): {averages['disk_usage']:.1f}%")
            print(f"  Tamanho do projeto: {current['project']['total_size_mb']:.1f}MB")
            print(f"  Arquivos: {current['project']['file_count']}")
            print(f"  Alertas recentes: {len(report['recent_alerts'])}")

if __name__ == "__main__":
    main() 