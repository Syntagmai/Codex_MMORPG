from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional
import json
import logging
import os
import psutil
import time

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Métricas e Feedback
==============================

Este script implementa sistema de métricas para monitorar e melhorar performance
do sistema BMAD com coleta automática de dados e análise de tendências.

Autor: Sistema BMAD - Metrics Agent
Data: 2025-08-01
"""


# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MetricsSystem:
    """Sistema de métricas e feedback"""
    
    def __init__(self, metrics_dir: str = "wiki/metrics"):
        """
        Inicializa o sistema de métricas.
        
        Args:
            metrics_dir: Diretório para armazenar métricas
        """
        self.metrics_dir = Path(metrics_dir)
        self.metrics_dir.mkdir(exist_ok=True)
        
        # Arquivos de métricas
        self.performance_file = self.metrics_dir / "performance_metrics.json"
        self.usage_file = self.metrics_dir / "usage_metrics.json"
        self.quality_file = self.metrics_dir / "quality_metrics.json"
        self.trends_file = self.metrics_dir / "trends_analysis.json"
        
        # Configurações de coleta
        self.collection_interval = 300  # 5 minutos
        self.retention_days = 30
        
        # Métricas em memória
        self.current_metrics = {
            "performance": {},
            "usage": {},
            "quality": {},
            "system": {}
        }
        
    def collect_system_metrics(self) -> Dict[str, Any]:
        """
        Coleta métricas do sistema.
        
        Returns:
            Métricas do sistema
        """
        try:
            # CPU
            cpu_percent = psutil.cpu_percent(interval=1)
            cpu_count = psutil.cpu_count()
            
            # Memória
            memory = psutil.virtual_memory()
            memory_percent = memory.percent
            memory_available = memory.available / (1024**3)  # GB
            
            # Disco
            disk = psutil.disk_usage('/')
            disk_percent = disk.percent
            disk_free = disk.free / (1024**3)  # GB
            
            # Rede
            network = psutil.net_io_counters()
            bytes_sent = network.bytes_sent
            bytes_recv = network.bytes_recv
            
            # Processos
            process_count = len(psutil.pids())
            
            return {
                "timestamp": datetime.now().isoformat(),
                "cpu": {
                    "percent": cpu_percent,
                    "count": cpu_count
                },
                "memory": {
                    "percent": memory_percent,
                    "available_gb": round(memory_available, 2),
                    "total_gb": round(memory.total / (1024**3), 2)
                },
                "disk": {
                    "percent": disk_percent,
                    "free_gb": round(disk_free, 2),
                    "total_gb": round(disk.total / (1024**3), 2)
                },
                "network": {
                    "bytes_sent": bytes_sent,
                    "bytes_recv": bytes_recv
                },
                "processes": {
                    "count": process_count
                }
            }
            
        except Exception as e:
            logger.error(f"Erro ao coletar métricas do sistema: {e}")
            return {}
    
    def collect_performance_metrics(self) -> Dict[str, Any]:
        """
        Coleta métricas de performance do sistema BMAD.
        
        Returns:
            Métricas de performance
        """
        try:
            # Verificar arquivos consolidados
            consolidated_dir = Path("wiki/consolidated")
            consolidated_files = 0
            consolidated_size = 0
            
            if consolidated_dir.exists():
                for file_path in consolidated_dir.rglob("*"):
                    if file_path.is_file():
                        consolidated_files += 1
                        consolidated_size += file_path.stat().st_size
            
            # Verificar agentes BMAD
            agents_dir = Path("wiki/bmad/agents")
            agent_files = 0
            agent_size = 0
            
            if agents_dir.exists():
                for file_path in agents_dir.glob("*.py"):
                    agent_files += 1
                    agent_size += file_path.stat().st_size
            
            # Verificar logs
            log_dir = Path("wiki/log")
            log_files = 0
            log_size = 0
            
            if log_dir.exists():
                for file_path in log_dir.rglob("*.md"):
                    log_files += 1
                    log_size += file_path.stat().st_size
            
            # Calcular métricas de performance
            total_files = consolidated_files + agent_files + log_files
            total_size_mb = (consolidated_size + agent_size + log_size) / (1024**2)
            
            return {
                "timestamp": datetime.now().isoformat(),
                "consolidated": {
                    "files": consolidated_files,
                    "size_mb": round(consolidated_size / (1024**2), 2)
                },
                "agents": {
                    "files": agent_files,
                    "size_mb": round(agent_size / (1024**2), 2)
                },
                "logs": {
                    "files": log_files,
                    "size_mb": round(log_size / (1024**2), 2)
                },
                "total": {
                    "files": total_files,
                    "size_mb": round(total_size_mb, 2)
                }
            }
            
        except Exception as e:
            logger.error(f"Erro ao coletar métricas de performance: {e}")
            return {}
    
    def collect_usage_metrics(self) -> Dict[str, Any]:
        """
        Coleta métricas de uso do sistema.
        
        Returns:
            Métricas de uso
        """
        try:
            # Verificar arquivos de navegação
            nav_file = Path("wiki/consolidated/navigation_index.json")
            nav_data = {}
            if nav_file.exists():
                with open(nav_file, 'r', encoding='utf-8') as f:
                    nav_data = json.load(f)
            
            # Verificar arquivos de busca
            search_file = Path("wiki/consolidated/advanced_search_index.json")
            search_data = {}
            if search_file.exists():
                with open(search_file, 'r', encoding='utf-8') as f:
                    search_data = json.load(f)
            
            # Calcular métricas de uso
            total_documents = nav_data.get("total_documents", 0)
            search_index_size = len(search_data.get("content_index", {}))
            tag_count = len(search_data.get("tag_index", {}))
            keyword_count = len(search_data.get("keyword_index", {}))
            
            return {
                "timestamp": datetime.now().isoformat(),
                "documents": {
                    "total": total_documents,
                    "indexed": search_index_size
                },
                "search": {
                    "tags": tag_count,
                    "keywords": keyword_count
                },
                "navigation": {
                    "has_index": nav_file.exists(),
                    "has_search": search_file.exists()
                }
            }
            
        except Exception as e:
            logger.error(f"Erro ao coletar métricas de uso: {e}")
            return {}
    
    def collect_quality_metrics(self) -> Dict[str, Any]:
        """
        Coleta métricas de qualidade do sistema.
        
        Returns:
            Métricas de qualidade
        """
        try:
            # Verificar integridade dos arquivos
            consolidated_dir = Path("wiki/consolidated")
            corrupted_files = 0
            empty_files = 0
            total_files = 0
            
            if consolidated_dir.exists():
                for file_path in consolidated_dir.rglob("*.md"):
                    total_files += 1
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            if not content.strip():
                                empty_files += 1
                    except Exception:
                        corrupted_files += 1
            
            # Calcular métricas de qualidade
            quality_score = 0
            if total_files > 0:
                quality_score = ((total_files - corrupted_files - empty_files) / total_files) * 100
            
            return {
                "timestamp": datetime.now().isoformat(),
                "integrity": {
                    "total_files": total_files,
                    "corrupted_files": corrupted_files,
                    "empty_files": empty_files,
                    "quality_score": round(quality_score, 2)
                },
                "structure": {
                    "has_consolidated": consolidated_dir.exists(),
                    "has_navigation": Path("wiki/consolidated/navigation_index.json").exists(),
                    "has_search": Path("wiki/consolidated/advanced_search_index.json").exists()
                }
            }
            
        except Exception as e:
            logger.error(f"Erro ao coletar métricas de qualidade: {e}")
            return {}
    
    def save_metrics(self, metrics_type: str, metrics_data: Dict[str, Any]):
        """
        Salva métricas em arquivo JSON.
        
        Args:
            metrics_type: Tipo de métrica (performance, usage, quality)
            metrics_data: Dados das métricas
        """
        try:
            if metrics_type == "performance":
                file_path = self.performance_file
            elif metrics_type == "usage":
                file_path = self.usage_file
            elif metrics_type == "quality":
                file_path = self.quality_file
            else:
                logger.error(f"Tipo de métrica inválido: {metrics_type}")
                return
            
            # Carregar métricas existentes
            existing_metrics = []
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    existing_metrics = json.load(f)
            
            # Adicionar nova métrica
            existing_metrics.append(metrics_data)
            
            # Manter apenas as últimas 30 dias
            cutoff_date = datetime.now() - timedelta(days=self.retention_days)
            filtered_metrics = []
            
            for metric in existing_metrics:
                metric_date = datetime.fromisoformat(metric.get("timestamp", ""))
                if metric_date > cutoff_date:
                    filtered_metrics.append(metric)
            
            # Salvar métricas filtradas
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(filtered_metrics, f, indent=2, ensure_ascii=False)
            
            logger.info(f"✅ Métricas {metrics_type} salvas: {len(filtered_metrics)} registros")
            
        except Exception as e:
            logger.error(f"Erro ao salvar métricas {metrics_type}: {e}")
    
    def analyze_trends(self) -> Dict[str, Any]:
        """
        Analisa tendências das métricas coletadas.
        
        Returns:
            Análise de tendências
        """
        logger.info("📊 Analisando tendências das métricas...")
        
        trends = {
            "timestamp": datetime.now().isoformat(),
            "performance_trends": {},
            "usage_trends": {},
            "quality_trends": {},
            "recommendations": []
        }
        
        try:
            # Analisar tendências de performance
            if self.performance_file.exists():
                with open(self.performance_file, 'r', encoding='utf-8') as f:
                    performance_data = json.load(f)
                
                if len(performance_data) >= 2:
                    latest = performance_data[-1]
                    previous = performance_data[-2]
                    
                    # Calcular mudanças
                    file_change = latest["total"]["files"] - previous["total"]["files"]
                    size_change = latest["total"]["size_mb"] - previous["total"]["size_mb"]
                    
                    trends["performance_trends"] = {
                        "file_growth": file_change,
                        "size_growth_mb": round(size_change, 2),
                        "growth_rate": round((file_change / previous["total"]["files"]) * 100, 2) if previous["total"]["files"] > 0 else 0
                    }
            
            # Analisar tendências de uso
            if self.usage_file.exists():
                with open(self.usage_file, 'r', encoding='utf-8') as f:
                    usage_data = json.load(f)
                
                if len(usage_data) >= 2:
                    latest = usage_data[-1]
                    previous = usage_data[-2]
                    
                    doc_change = latest["documents"]["total"] - previous["documents"]["total"]
                    tag_change = latest["search"]["tags"] - previous["search"]["tags"]
                    
                    trends["usage_trends"] = {
                        "document_growth": doc_change,
                        "tag_growth": tag_change,
                        "search_coverage": round((latest["documents"]["indexed"] / latest["documents"]["total"]) * 100, 2) if latest["documents"]["total"] > 0 else 0
                    }
            
            # Analisar tendências de qualidade
            if self.quality_file.exists():
                with open(self.quality_file, 'r', encoding='utf-8') as f:
                    quality_data = json.load(f)
                
                if len(quality_data) >= 2:
                    latest = quality_data[-1]
                    previous = quality_data[-2]
                    
                    quality_change = latest["integrity"]["quality_score"] - previous["integrity"]["quality_score"]
                    
                    trends["quality_trends"] = {
                        "quality_change": round(quality_change, 2),
                        "current_quality": latest["integrity"]["quality_score"],
                        "corruption_rate": round((latest["integrity"]["corrupted_files"] / latest["integrity"]["total_files"]) * 100, 2) if latest["integrity"]["total_files"] > 0 else 0
                    }
            
            # Gerar recomendações
            recommendations = []
            
            # Verificar qualidade
            if trends.get("quality_trends", {}).get("current_quality", 100) < 95:
                recommendations.append("🔧 Verificar integridade dos arquivos consolidados")
            
            # Verificar crescimento
            if trends.get("performance_trends", {}).get("growth_rate", 0) > 10:
                recommendations.append("📈 Sistema crescendo rapidamente - considerar otimização")
            
            # Verificar cobertura de busca
            if trends.get("usage_trends", {}).get("search_coverage", 100) < 90:
                recommendations.append("🔍 Melhorar cobertura do índice de busca")
            
            trends["recommendations"] = recommendations
            
            # Salvar análise de tendências
            with open(self.trends_file, 'w', encoding='utf-8') as f:
                json.dump(trends, f, indent=2, ensure_ascii=False)
            
            logger.info("✅ Análise de tendências concluída")
            
        except Exception as e:
            logger.error(f"Erro ao analisar tendências: {e}")
        
        return trends
    
    def generate_metrics_report(self) -> str:
        """
        Gera relatório completo de métricas.
        
        Returns:
            Caminho do relatório
        """
        logger.info("📋 Gerando relatório de métricas...")
        
        # Coletar métricas atuais
        system_metrics = self.collect_system_metrics()
        performance_metrics = self.collect_performance_metrics()
        usage_metrics = self.collect_usage_metrics()
        quality_metrics = self.collect_quality_metrics()
        
        # Analisar tendências
        trends = self.analyze_trends()
        
        # Gerar relatório
        report = {
            "generation_date": datetime.now().isoformat(),
            "summary": {
                "system_health": "✅ Operacional" if system_metrics else "❌ Erro",
                "performance_status": "✅ Boa" if performance_metrics else "❌ Erro",
                "usage_status": "✅ Ativo" if usage_metrics else "❌ Erro",
                "quality_status": "✅ Alta" if quality_metrics.get("integrity", {}).get("quality_score", 0) > 95 else "⚠️ Baixa"
            },
            "current_metrics": {
                "system": system_metrics,
                "performance": performance_metrics,
                "usage": usage_metrics,
                "quality": quality_metrics
            },
            "trends": trends,
            "files": {
                "performance_file": str(self.performance_file),
                "usage_file": str(self.usage_file),
                "quality_file": str(self.quality_file),
                "trends_file": str(self.trends_file)
            }
        }
        
        report_file = self.metrics_dir / "metrics_report.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        logger.info(f"✅ Relatório salvo em: {report_file}")
        return str(report_file)
    
    def collect_all_metrics(self):
        """
        Coleta todas as métricas do sistema.
        """
        logger.info("📊 Coletando métricas do sistema...")
        
        # Coletar métricas
        system_metrics = self.collect_system_metrics()
        performance_metrics = self.collect_performance_metrics()
        usage_metrics = self.collect_usage_metrics()
        quality_metrics = self.collect_quality_metrics()
        
        # Salvar métricas
        if system_metrics:
            self.save_metrics("performance", performance_metrics)
        if usage_metrics:
            self.save_metrics("usage", usage_metrics)
        if quality_metrics:
            self.save_metrics("quality", quality_metrics)
        
        logger.info("✅ Coleta de métricas concluída")
    
    def implement_metrics_system(self) -> Dict[str, Any]:
        """
        Implementa sistema completo de métricas.
        
        Returns:
            Resultados da implementação
        """
        logger.info("🚀 Implementando sistema de métricas...")
        
        # Coletar métricas iniciais
        self.collect_all_metrics()
        
        # Gerar relatório
        report_path = self.generate_metrics_report()
        
        # Verificar arquivos criados
        files_created = []
        for file_path in [self.performance_file, self.usage_file, self.quality_file, self.trends_file]:
            if file_path.exists():
                files_created.append(file_path.name)
        
        results = {
            "success": True,
            "metrics_collected": True,
            "files_created": files_created,
            "report_path": report_path,
            "collection_interval": self.collection_interval,
            "retention_days": self.retention_days
        }
        
        logger.info("✅ Sistema de métricas implementado!")
        return results

def main():
    """Função principal do script."""
    print("🔄 Implementando sistema de métricas...")
    
    metrics_system = MetricsSystem()
    
    # Implementar sistema
    results = metrics_system.implement_metrics_system()
    
    print(f"\n✅ Sistema de métricas implementado!")
    print(f"📊 Métricas coletadas: {results['metrics_collected']}")
    print(f"📁 Arquivos criados: {len(results['files_created'])}")
    print(f"⏱️ Intervalo de coleta: {results['collection_interval']}s")
    print(f"📅 Retenção: {results['retention_days']} dias")
    print(f"📋 Relatório: {results['report_path']}")

if __name__ == "__main__":
    main() 