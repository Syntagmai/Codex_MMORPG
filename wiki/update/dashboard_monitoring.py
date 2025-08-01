from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional
import json
import logging
import os

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dashboard de Monitoramento
=========================

Este script cria interface para visualizar métricas do sistema BMAD
com gráficos, alertas e visualizações em tempo real.

Autor: Sistema BMAD - Dashboard Agent
Data: 2025-08-01
"""


# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DashboardMonitoring:
    """Dashboard de monitoramento do sistema"""
    
    def __init__(self, metrics_dir: str = "wiki/metrics", dashboard_dir: str = "wiki/dashboard"):
        """
        Inicializa o dashboard de monitoramento.
        
        Args:
            metrics_dir: Diretório das métricas
            dashboard_dir: Diretório do dashboard
        """
        self.metrics_dir = Path(metrics_dir)
        self.dashboard_dir = Path(dashboard_dir)
        self.dashboard_dir.mkdir(exist_ok=True)
        
        # Arquivos de métricas
        self.performance_file = self.metrics_dir / "performance_metrics.json"
        self.usage_file = self.metrics_dir / "usage_metrics.json"
        self.quality_file = self.metrics_dir / "quality_metrics.json"
        self.trends_file = self.metrics_dir / "trends_analysis.json"
        
        # Arquivos do dashboard
        self.dashboard_file = self.dashboard_dir / "monitoring_dashboard.json"
        self.alerts_file = self.dashboard_dir / "system_alerts.json"
        self.status_file = self.dashboard_dir / "system_status.json"
        
    def load_metrics_data(self) -> Dict[str, Any]:
        """
        Carrega dados das métricas.
        
        Returns:
            Dados das métricas
        """
        metrics_data = {
            "performance": [],
            "usage": [],
            "quality": [],
            "trends": {}
        }
        
        try:
            # Carregar métricas de performance
            if self.performance_file.exists():
                with open(self.performance_file, 'r', encoding='utf-8') as f:
                    metrics_data["performance"] = json.load(f)
            
            # Carregar métricas de uso
            if self.usage_file.exists():
                with open(self.usage_file, 'r', encoding='utf-8') as f:
                    metrics_data["usage"] = json.load(f)
            
            # Carregar métricas de qualidade
            if self.quality_file.exists():
                with open(self.quality_file, 'r', encoding='utf-8') as f:
                    metrics_data["quality"] = json.load(f)
            
            # Carregar análise de tendências
            if self.trends_file.exists():
                with open(self.trends_file, 'r', encoding='utf-8') as f:
                    metrics_data["trends"] = json.load(f)
            
        except Exception as e:
            logger.error(f"Erro ao carregar dados das métricas: {e}")
        
        return metrics_data
    
    def calculate_system_status(self, metrics_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calcula status geral do sistema.
        
        Args:
            metrics_data: Dados das métricas
            
        Returns:
            Status do sistema
        """
        status = {
            "timestamp": datetime.now().isoformat(),
            "overall_status": "🟢 Operacional",
            "components": {},
            "alerts": [],
            "recommendations": []
        }
        
        try:
            # Status de performance
            if metrics_data["performance"]:
                latest_perf = metrics_data["performance"][-1]
                total_files = latest_perf.get("total", {}).get("files", 0)
                total_size = latest_perf.get("total", {}).get("size_mb", 0)
                
                if total_files > 0:
                    status["components"]["performance"] = {
                        "status": "🟢 Boa",
                        "files": total_files,
                        "size_mb": total_size,
                        "details": latest_perf
                    }
                else:
                    status["components"]["performance"] = {
                        "status": "🔴 Crítico",
                        "files": 0,
                        "size_mb": 0,
                        "details": {}
                    }
                    status["alerts"].append("⚠️ Nenhum arquivo de performance encontrado")
            
            # Status de uso
            if metrics_data["usage"]:
                latest_usage = metrics_data["usage"][-1]
                total_docs = latest_usage.get("documents", {}).get("total", 0)
                indexed_docs = latest_usage.get("documents", {}).get("indexed", 0)
                
                if total_docs > 0:
                    coverage = (indexed_docs / total_docs) * 100
                    status["components"]["usage"] = {
                        "status": "🟢 Ativo" if coverage > 90 else "🟡 Parcial",
                        "total_documents": total_docs,
                        "indexed_documents": indexed_docs,
                        "coverage_percent": round(coverage, 2),
                        "details": latest_usage
                    }
                    
                    if coverage < 90:
                        status["alerts"].append(f"⚠️ Cobertura de busca baixa: {coverage:.1f}%")
                else:
                    status["components"]["usage"] = {
                        "status": "🔴 Crítico",
                        "total_documents": 0,
                        "indexed_documents": 0,
                        "coverage_percent": 0,
                        "details": {}
                    }
                    status["alerts"].append("⚠️ Nenhum documento encontrado")
            
            # Status de qualidade
            if metrics_data["quality"]:
                latest_quality = metrics_data["quality"][-1]
                quality_score = latest_quality.get("integrity", {}).get("quality_score", 0)
                
                if quality_score > 95:
                    quality_status = "🟢 Alta"
                elif quality_score > 80:
                    quality_status = "🟡 Média"
                else:
                    quality_status = "🔴 Baixa"
                
                status["components"]["quality"] = {
                    "status": quality_status,
                    "quality_score": quality_score,
                    "total_files": latest_quality.get("integrity", {}).get("total_files", 0),
                    "corrupted_files": latest_quality.get("integrity", {}).get("corrupted_files", 0),
                    "details": latest_quality
                }
                
                if quality_score < 95:
                    status["alerts"].append(f"⚠️ Qualidade baixa: {quality_score:.1f}%")
            
            # Verificar tendências
            if metrics_data["trends"]:
                trends = metrics_data["trends"]
                recommendations = trends.get("recommendations", [])
                status["recommendations"] = recommendations
            
            # Determinar status geral
            critical_count = sum(1 for comp in status["components"].values() if "🔴" in comp["status"])
            warning_count = sum(1 for comp in status["components"].values() if "🟡" in comp["status"])
            
            if critical_count > 0:
                status["overall_status"] = "🔴 Crítico"
            elif warning_count > 0:
                status["overall_status"] = "🟡 Atenção"
            else:
                status["overall_status"] = "🟢 Operacional"
            
        except Exception as e:
            logger.error(f"Erro ao calcular status do sistema: {e}")
            status["overall_status"] = "🔴 Erro"
            status["alerts"].append(f"❌ Erro ao calcular status: {e}")
        
        return status
    
    def generate_alerts(self, status: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Gera alertas baseados no status do sistema.
        
        Args:
            status: Status do sistema
            
        Returns:
            Lista de alertas
        """
        alerts = []
        
        try:
            # Alertas baseados no status geral
            if status["overall_status"] == "🔴 Crítico":
                alerts.append({
                    "level": "critical",
                    "message": "Sistema em estado crítico - ação imediata necessária",
                    "timestamp": datetime.now().isoformat(),
                    "component": "system"
                })
            elif status["overall_status"] == "🟡 Atenção":
                alerts.append({
                    "level": "warning",
                    "message": "Sistema requer atenção - verificar componentes",
                    "timestamp": datetime.now().isoformat(),
                    "component": "system"
                })
            
            # Alertas específicos por componente
            for component_name, component_data in status["components"].items():
                if "🔴" in component_data["status"]:
                    alerts.append({
                        "level": "critical",
                        "message": f"Componente {component_name} em estado crítico",
                        "timestamp": datetime.now().isoformat(),
                        "component": component_name,
                        "details": component_data
                    })
                elif "🟡" in component_data["status"]:
                    alerts.append({
                        "level": "warning",
                        "message": f"Componente {component_name} requer atenção",
                        "timestamp": datetime.now().isoformat(),
                        "component": component_name,
                        "details": component_data
                    })
            
            # Alertas baseados em métricas específicas
            if "quality" in status["components"]:
                quality_data = status["components"]["quality"]
                if quality_data["quality_score"] < 90:
                    alerts.append({
                        "level": "warning",
                        "message": f"Qualidade do sistema baixa: {quality_data['quality_score']:.1f}%",
                        "timestamp": datetime.now().isoformat(),
                        "component": "quality"
                    })
            
            if "usage" in status["components"]:
                usage_data = status["components"]["usage"]
                if usage_data["coverage_percent"] < 85:
                    alerts.append({
                        "level": "warning",
                        "message": f"Cobertura de busca baixa: {usage_data['coverage_percent']:.1f}%",
                        "timestamp": datetime.now().isoformat(),
                        "component": "usage"
                    })
            
        except Exception as e:
            logger.error(f"Erro ao gerar alertas: {e}")
            alerts.append({
                "level": "error",
                "message": f"Erro ao gerar alertas: {e}",
                "timestamp": datetime.now().isoformat(),
                "component": "dashboard"
            })
        
        return alerts
    
    def create_dashboard_data(self, metrics_data: Dict[str, Any], status: Dict[str, Any], alerts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Cria dados do dashboard.
        
        Args:
            metrics_data: Dados das métricas
            status: Status do sistema
            alerts: Alertas gerados
            
        Returns:
            Dados do dashboard
        """
        dashboard_data = {
            "generation_date": datetime.now().isoformat(),
            "system_status": status,
            "alerts": alerts,
            "metrics_summary": {},
            "charts_data": {},
            "quick_actions": []
        }
        
        try:
            # Resumo das métricas
            if metrics_data["performance"]:
                latest_perf = metrics_data["performance"][-1]
                dashboard_data["metrics_summary"]["performance"] = {
                    "total_files": latest_perf.get("total", {}).get("files", 0),
                    "total_size_mb": latest_perf.get("total", {}).get("size_mb", 0),
                    "consolidated_files": latest_perf.get("consolidated", {}).get("files", 0),
                    "agent_files": latest_perf.get("agents", {}).get("files", 0)
                }
            
            if metrics_data["usage"]:
                latest_usage = metrics_data["usage"][-1]
                dashboard_data["metrics_summary"]["usage"] = {
                    "total_documents": latest_usage.get("documents", {}).get("total", 0),
                    "indexed_documents": latest_usage.get("documents", {}).get("indexed", 0),
                    "tags_count": latest_usage.get("search", {}).get("tags", 0),
                    "keywords_count": latest_usage.get("search", {}).get("keywords", 0)
                }
            
            if metrics_data["quality"]:
                latest_quality = metrics_data["quality"][-1]
                dashboard_data["metrics_summary"]["quality"] = {
                    "quality_score": latest_quality.get("integrity", {}).get("quality_score", 0),
                    "total_files": latest_quality.get("integrity", {}).get("total_files", 0),
                    "corrupted_files": latest_quality.get("integrity", {}).get("corrupted_files", 0),
                    "empty_files": latest_quality.get("integrity", {}).get("empty_files", 0)
                }
            
            # Dados para gráficos
            dashboard_data["charts_data"] = {
                "performance_history": self.extract_performance_history(metrics_data["performance"]),
                "usage_history": self.extract_usage_history(metrics_data["usage"]),
                "quality_history": self.extract_quality_history(metrics_data["quality"])
            }
            
            # Ações rápidas
            dashboard_data["quick_actions"] = [
                {
                    "action": "refresh_metrics",
                    "description": "Atualizar métricas",
                    "command": "python wiki/update/metrics_system.py"
                },
                {
                    "action": "check_alerts",
                    "description": "Verificar alertas",
                    "command": "python wiki/update/dashboard_monitoring.py --check-alerts"
                },
                {
                    "action": "generate_report",
                    "description": "Gerar relatório",
                    "command": "python wiki/update/metrics_system.py --generate-report"
                }
            ]
            
        except Exception as e:
            logger.error(f"Erro ao criar dados do dashboard: {e}")
        
        return dashboard_data
    
    def extract_performance_history(self, performance_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Extrai histórico de performance para gráficos.
        
        Args:
            performance_data: Dados de performance
            
        Returns:
            Dados para gráficos
        """
        history = {
            "timestamps": [],
            "total_files": [],
            "total_size": [],
            "consolidated_files": [],
            "agent_files": []
        }
        
        try:
            for data in performance_data[-10:]:  # Últimos 10 registros
                history["timestamps"].append(data.get("timestamp", ""))
                history["total_files"].append(data.get("total", {}).get("files", 0))
                history["total_size"].append(data.get("total", {}).get("size_mb", 0))
                history["consolidated_files"].append(data.get("consolidated", {}).get("files", 0))
                history["agent_files"].append(data.get("agents", {}).get("files", 0))
        except Exception as e:
            logger.error(f"Erro ao extrair histórico de performance: {e}")
        
        return history
    
    def extract_usage_history(self, usage_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Extrai histórico de uso para gráficos.
        
        Args:
            usage_data: Dados de uso
            
        Returns:
            Dados para gráficos
        """
        history = {
            "timestamps": [],
            "total_documents": [],
            "indexed_documents": [],
            "tags_count": [],
            "keywords_count": []
        }
        
        try:
            for data in usage_data[-10:]:  # Últimos 10 registros
                history["timestamps"].append(data.get("timestamp", ""))
                history["total_documents"].append(data.get("documents", {}).get("total", 0))
                history["indexed_documents"].append(data.get("documents", {}).get("indexed", 0))
                history["tags_count"].append(data.get("search", {}).get("tags", 0))
                history["keywords_count"].append(data.get("search", {}).get("keywords", 0))
        except Exception as e:
            logger.error(f"Erro ao extrair histórico de uso: {e}")
        
        return history
    
    def extract_quality_history(self, quality_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Extrai histórico de qualidade para gráficos.
        
        Args:
            quality_data: Dados de qualidade
            
        Returns:
            Dados para gráficos
        """
        history = {
            "timestamps": [],
            "quality_score": [],
            "total_files": [],
            "corrupted_files": [],
            "empty_files": []
        }
        
        try:
            for data in quality_data[-10:]:  # Últimos 10 registros
                history["timestamps"].append(data.get("timestamp", ""))
                history["quality_score"].append(data.get("integrity", {}).get("quality_score", 0))
                history["total_files"].append(data.get("integrity", {}).get("total_files", 0))
                history["corrupted_files"].append(data.get("integrity", {}).get("corrupted_files", 0))
                history["empty_files"].append(data.get("integrity", {}).get("empty_files", 0))
        except Exception as e:
            logger.error(f"Erro ao extrair histórico de qualidade: {e}")
        
        return history
    
    def save_dashboard_data(self, dashboard_data: Dict[str, Any]):
        """
        Salva dados do dashboard.
        
        Args:
            dashboard_data: Dados do dashboard
        """
        try:
            with open(self.dashboard_file, 'w', encoding='utf-8') as f:
                json.dump(dashboard_data, f, indent=2, ensure_ascii=False)
            
            logger.info(f"✅ Dashboard salvo em: {self.dashboard_file}")
            
        except Exception as e:
            logger.error(f"Erro ao salvar dashboard: {e}")
    
    def save_alerts(self, alerts: List[Dict[str, Any]]):
        """
        Salva alertas do sistema.
        
        Args:
            alerts: Lista de alertas
        """
        try:
            with open(self.alerts_file, 'w', encoding='utf-8') as f:
                json.dump(alerts, f, indent=2, ensure_ascii=False)
            
            logger.info(f"✅ Alertas salvos em: {self.alerts_file}")
            
        except Exception as e:
            logger.error(f"Erro ao salvar alertas: {e}")
    
    def save_system_status(self, status: Dict[str, Any]):
        """
        Salva status do sistema.
        
        Args:
            status: Status do sistema
        """
        try:
            with open(self.status_file, 'w', encoding='utf-8') as f:
                json.dump(status, f, indent=2, ensure_ascii=False)
            
            logger.info(f"✅ Status do sistema salvo em: {self.status_file}")
            
        except Exception as e:
            logger.error(f"Erro ao salvar status do sistema: {e}")
    
    def generate_dashboard_report(self) -> str:
        """
        Gera relatório do dashboard.
        
        Returns:
            Caminho do relatório
        """
        logger.info("📋 Gerando relatório do dashboard...")
        
        # Carregar dados
        metrics_data = self.load_metrics_data()
        
        # Calcular status
        status = self.calculate_system_status(metrics_data)
        
        # Gerar alertas
        alerts = self.generate_alerts(status)
        
        # Criar dados do dashboard
        dashboard_data = self.create_dashboard_data(metrics_data, status, alerts)
        
        # Salvar dados
        self.save_dashboard_data(dashboard_data)
        self.save_alerts(alerts)
        self.save_system_status(status)
        
        # Gerar relatório
        report = {
            "generation_date": datetime.now().isoformat(),
            "dashboard_summary": {
                "overall_status": status["overall_status"],
                "components_count": len(status["components"]),
                "alerts_count": len(alerts),
                "critical_alerts": len([a for a in alerts if a["level"] == "critical"]),
                "warning_alerts": len([a for a in alerts if a["level"] == "warning"])
            },
            "files": {
                "dashboard_file": str(self.dashboard_file),
                "alerts_file": str(self.alerts_file),
                "status_file": str(self.status_file)
            }
        }
        
        report_file = self.dashboard_dir / "dashboard_report.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        logger.info(f"✅ Relatório do dashboard salvo em: {report_file}")
        return str(report_file)
    
    def create_monitoring_dashboard(self) -> Dict[str, Any]:
        """
        Cria dashboard completo de monitoramento.
        
        Returns:
            Resultados da criação
        """
        logger.info("🚀 Criando dashboard de monitoramento...")
        
        # Gerar relatório
        report_path = self.generate_dashboard_report()
        
        # Verificar arquivos criados
        files_created = []
        for file_path in [self.dashboard_file, self.alerts_file, self.status_file]:
            if file_path.exists():
                files_created.append(file_path.name)
        
        results = {
            "success": True,
            "dashboard_created": True,
            "files_created": files_created,
            "report_path": report_path,
            "dashboard_url": str(self.dashboard_file),
            "alerts_url": str(self.alerts_file),
            "status_url": str(self.status_file)
        }
        
        logger.info("✅ Dashboard de monitoramento criado!")
        return results

def main():
    """Função principal do script."""
    print("🔄 Criando dashboard de monitoramento...")
    
    dashboard = DashboardMonitoring()
    
    # Criar dashboard
    results = dashboard.create_monitoring_dashboard()
    
    print(f"\n✅ Dashboard de monitoramento criado!")
    print(f"📊 Dashboard criado: {results['dashboard_created']}")
    print(f"📁 Arquivos criados: {len(results['files_created'])}")
    print(f"📋 Relatório: {results['report_path']}")
    print(f"🔗 Dashboard: {results['dashboard_url']}")
    print(f"🚨 Alertas: {results['alerts_url']}")
    print(f"📈 Status: {results['status_url']}")

if __name__ == "__main__":
    main() 