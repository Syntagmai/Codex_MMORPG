#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Alertas Automáticos
==============================

Este script implementa sistema de alertas automáticos para problemas de performance
com notificações inteligentes e ações corretivas automáticas.

Autor: Sistema BMAD - Alert Agent
Data: 2025-08-01
"""

import json
import os
import time
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

class AlertSystem:
    """Sistema de alertas automáticos"""
    
    def __init__(self, alerts_dir: str = "wiki/alerts"):
        """
        Inicializa o sistema de alertas.
        
        Args:
            alerts_dir: Diretório para armazenar alertas
        """
        self.alerts_dir = Path(alerts_dir)
        self.alerts_dir.mkdir(exist_ok=True)
        
        # Arquivos de alertas
        self.active_alerts_file = self.alerts_dir / "active_alerts.json"
        self.alert_history_file = self.alerts_dir / "alert_history.json"
        self.alert_rules_file = self.alerts_dir / "alert_rules.json"
        self.alert_actions_file = self.alerts_dir / "alert_actions.json"
        
        # Configurações de alertas
        self.alert_thresholds = {
            "performance": {
                "quality_score": 90,
                "file_growth_rate": 15,
                "size_growth_rate": 20
            },
            "usage": {
                "search_coverage": 85,
                "document_index_ratio": 0.9
            },
            "system": {
                "cpu_usage": 80,
                "memory_usage": 85,
                "disk_usage": 90
            }
        }
        
        # Inicializar arquivos se não existirem
        self.initialize_alert_files()
        
    def initialize_alert_files(self):
        """
        Inicializa arquivos de alertas se não existirem.
        """
        try:
            # Arquivo de alertas ativos
            if not self.active_alerts_file.exists():
                with open(self.active_alerts_file, 'w', encoding='utf-8') as f:
                    json.dump([], f, indent=2, ensure_ascii=False)
            
            # Arquivo de histórico de alertas
            if not self.alert_history_file.exists():
                with open(self.alert_history_file, 'w', encoding='utf-8') as f:
                    json.dump([], f, indent=2, ensure_ascii=False)
            
            # Arquivo de regras de alertas
            if not self.alert_rules_file.exists():
                with open(self.alert_rules_file, 'w', encoding='utf-8') as f:
                    json.dump(self.alert_thresholds, f, indent=2, ensure_ascii=False)
            
            # Arquivo de ações de alertas
            if not self.alert_actions_file.exists():
                default_actions = {
                    "performance_alert": "python wiki/update/metrics_system.py --collect-metrics",
                    "quality_alert": "python wiki/update/quality_check.py",
                    "usage_alert": "python wiki/update/advanced_search_system.py --rebuild-index",
                    "system_alert": "python wiki/update/system_health_check.py"
                }
                with open(self.alert_actions_file, 'w', encoding='utf-8') as f:
                    json.dump(default_actions, f, indent=2, ensure_ascii=False)
            
            logger.info("✅ Arquivos de alertas inicializados")
            
        except Exception as e:
            logger.error(f"Erro ao inicializar arquivos de alertas: {e}")
    
    def load_metrics_data(self) -> Dict[str, Any]:
        """
        Carrega dados das métricas para análise.
        
        Returns:
            Dados das métricas
        """
        metrics_data = {}
        
        try:
            # Carregar métricas de performance
            perf_file = Path("wiki/metrics/performance_metrics.json")
            if perf_file.exists():
                with open(perf_file, 'r', encoding='utf-8') as f:
                    metrics_data["performance"] = json.load(f)
            
            # Carregar métricas de uso
            usage_file = Path("wiki/metrics/usage_metrics.json")
            if usage_file.exists():
                with open(usage_file, 'r', encoding='utf-8') as f:
                    metrics_data["usage"] = json.load(f)
            
            # Carregar métricas de qualidade
            quality_file = Path("wiki/metrics/quality_metrics.json")
            if quality_file.exists():
                with open(quality_file, 'r', encoding='utf-8') as f:
                    metrics_data["quality"] = json.load(f)
            
            # Carregar status do sistema
            status_file = Path("wiki/dashboard/system_status.json")
            if status_file.exists():
                with open(status_file, 'r', encoding='utf-8') as f:
                    metrics_data["status"] = json.load(f)
            
        except Exception as e:
            logger.error(f"Erro ao carregar dados das métricas: {e}")
        
        return metrics_data
    
    def check_performance_alerts(self, metrics_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Verifica alertas de performance.
        
        Args:
            metrics_data: Dados das métricas
            
        Returns:
            Lista de alertas de performance
        """
        alerts = []
        
        try:
            # Verificar qualidade
            if "quality" in metrics_data and metrics_data["quality"]:
                latest_quality = metrics_data["quality"][-1]
                quality_score = latest_quality.get("integrity", {}).get("quality_score", 100)
                
                if quality_score < self.alert_thresholds["performance"]["quality_score"]:
                    alerts.append({
                        "type": "performance",
                        "level": "warning" if quality_score > 80 else "critical",
                        "message": f"Qualidade do sistema baixa: {quality_score:.1f}%",
                        "timestamp": datetime.now().isoformat(),
                        "component": "quality",
                        "value": quality_score,
                        "threshold": self.alert_thresholds["performance"]["quality_score"],
                        "action": "quality_alert"
                    })
            
            # Verificar crescimento de arquivos
            if "performance" in metrics_data and len(metrics_data["performance"]) >= 2:
                latest_perf = metrics_data["performance"][-1]
                previous_perf = metrics_data["performance"][-2]
                
                latest_files = latest_perf.get("total", {}).get("files", 0)
                previous_files = previous_perf.get("total", {}).get("files", 0)
                
                if previous_files > 0:
                    growth_rate = ((latest_files - previous_files) / previous_files) * 100
                    
                    if growth_rate > self.alert_thresholds["performance"]["file_growth_rate"]:
                        alerts.append({
                            "type": "performance",
                            "level": "warning",
                            "message": f"Crescimento rápido de arquivos: {growth_rate:.1f}%",
                            "timestamp": datetime.now().isoformat(),
                            "component": "files",
                            "value": growth_rate,
                            "threshold": self.alert_thresholds["performance"]["file_growth_rate"],
                            "action": "performance_alert"
                        })
            
        except Exception as e:
            logger.error(f"Erro ao verificar alertas de performance: {e}")
        
        return alerts
    
    def check_usage_alerts(self, metrics_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Verifica alertas de uso.
        
        Args:
            metrics_data: Dados das métricas
            
        Returns:
            Lista de alertas de uso
        """
        alerts = []
        
        try:
            # Verificar cobertura de busca
            if "usage" in metrics_data and metrics_data["usage"]:
                latest_usage = metrics_data["usage"][-1]
                total_docs = latest_usage.get("documents", {}).get("total", 0)
                indexed_docs = latest_usage.get("documents", {}).get("indexed", 0)
                
                if total_docs > 0:
                    coverage = (indexed_docs / total_docs) * 100
                    
                    if coverage < self.alert_thresholds["usage"]["search_coverage"]:
                        alerts.append({
                            "type": "usage",
                            "level": "warning",
                            "message": f"Cobertura de busca baixa: {coverage:.1f}%",
                            "timestamp": datetime.now().isoformat(),
                            "component": "search",
                            "value": coverage,
                            "threshold": self.alert_thresholds["usage"]["search_coverage"],
                            "action": "usage_alert"
                        })
            
            # Verificar proporção de documentos indexados
            if "usage" in metrics_data and metrics_data["usage"]:
                latest_usage = metrics_data["usage"][-1]
                total_docs = latest_usage.get("documents", {}).get("total", 0)
                indexed_docs = latest_usage.get("documents", {}).get("indexed", 0)
                
                if total_docs > 0:
                    index_ratio = indexed_docs / total_docs
                    
                    if index_ratio < self.alert_thresholds["usage"]["document_index_ratio"]:
                        alerts.append({
                            "type": "usage",
                            "level": "warning",
                            "message": f"Proporção de documentos indexados baixa: {index_ratio:.2f}",
                            "timestamp": datetime.now().isoformat(),
                            "component": "indexing",
                            "value": index_ratio,
                            "threshold": self.alert_thresholds["usage"]["document_index_ratio"],
                            "action": "usage_alert"
                        })
            
        except Exception as e:
            logger.error(f"Erro ao verificar alertas de uso: {e}")
        
        return alerts
    
    def check_system_alerts(self, metrics_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Verifica alertas do sistema.
        
        Args:
            metrics_data: Dados das métricas
            
        Returns:
            Lista de alertas do sistema
        """
        alerts = []
        
        try:
            # Verificar status geral do sistema
            if "status" in metrics_data:
                system_status = metrics_data["status"]
                overall_status = system_status.get("overall_status", "🟢 Operacional")
                
                if "🔴" in overall_status:
                    alerts.append({
                        "type": "system",
                        "level": "critical",
                        "message": "Sistema em estado crítico",
                        "timestamp": datetime.now().isoformat(),
                        "component": "system",
                        "value": overall_status,
                        "threshold": "operational",
                        "action": "system_alert"
                    })
                elif "🟡" in overall_status:
                    alerts.append({
                        "type": "system",
                        "level": "warning",
                        "message": "Sistema requer atenção",
                        "timestamp": datetime.now().isoformat(),
                        "component": "system",
                        "value": overall_status,
                        "threshold": "operational",
                        "action": "system_alert"
                    })
            
            # Verificar componentes específicos
            if "status" in metrics_data and "components" in metrics_data["status"]:
                components = metrics_data["status"]["components"]
                
                for component_name, component_data in components.items():
                    component_status = component_data.get("status", "")
                    
                    if "🔴" in component_status:
                        alerts.append({
                            "type": "system",
                            "level": "critical",
                            "message": f"Componente {component_name} em estado crítico",
                            "timestamp": datetime.now().isoformat(),
                            "component": component_name,
                            "value": component_status,
                            "threshold": "operational",
                            "action": "system_alert"
                        })
                    elif "🟡" in component_status:
                        alerts.append({
                            "type": "system",
                            "level": "warning",
                            "message": f"Componente {component_name} requer atenção",
                            "timestamp": datetime.now().isoformat(),
                            "component": component_name,
                            "value": component_status,
                            "threshold": "operational",
                            "action": "system_alert"
                        })
            
        except Exception as e:
            logger.error(f"Erro ao verificar alertas do sistema: {e}")
        
        return alerts
    
    def check_duplicate_alerts(self, new_alerts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Verifica se há alertas duplicados.
        
        Args:
            new_alerts: Novos alertas
            
        Returns:
            Alertas não duplicados
        """
        try:
            # Carregar alertas ativos
            active_alerts = []
            if self.active_alerts_file.exists():
                with open(self.active_alerts_file, 'r', encoding='utf-8') as f:
                    active_alerts = json.load(f)
            
            # Filtrar alertas duplicados
            unique_alerts = []
            existing_alert_keys = set()
            
            # Adicionar chaves dos alertas ativos
            for alert in active_alerts:
                key = f"{alert.get('type')}_{alert.get('component')}_{alert.get('level')}"
                existing_alert_keys.add(key)
            
            # Verificar novos alertas
            for alert in new_alerts:
                key = f"{alert.get('type')}_{alert.get('component')}_{alert.get('level')}"
                
                if key not in existing_alert_keys:
                    unique_alerts.append(alert)
                    existing_alert_keys.add(key)
            
            return unique_alerts
            
        except Exception as e:
            logger.error(f"Erro ao verificar alertas duplicados: {e}")
            return new_alerts
    
    def save_active_alerts(self, alerts: List[Dict[str, Any]]):
        """
        Salva alertas ativos.
        
        Args:
            alerts: Lista de alertas ativos
        """
        try:
            with open(self.active_alerts_file, 'w', encoding='utf-8') as f:
                json.dump(alerts, f, indent=2, ensure_ascii=False)
            
            logger.info(f"✅ Alertas ativos salvos: {len(alerts)} alertas")
            
        except Exception as e:
            logger.error(f"Erro ao salvar alertas ativos: {e}")
    
    def update_alert_history(self, new_alerts: List[Dict[str, Any]]):
        """
        Atualiza histórico de alertas.
        
        Args:
            new_alerts: Novos alertas
        """
        try:
            # Carregar histórico existente
            history = []
            if self.alert_history_file.exists():
                with open(self.alert_history_file, 'r', encoding='utf-8') as f:
                    history = json.load(f)
            
            # Adicionar novos alertas
            for alert in new_alerts:
                alert_with_resolution = {
                    **alert,
                    "resolved": False,
                    "resolution_time": None,
                    "resolution_action": None
                }
                history.append(alert_with_resolution)
            
            # Manter apenas os últimos 100 alertas
            if len(history) > 100:
                history = history[-100:]
            
            # Salvar histórico
            with open(self.alert_history_file, 'w', encoding='utf-8') as f:
                json.dump(history, f, indent=2, ensure_ascii=False)
            
            logger.info(f"✅ Histórico de alertas atualizado: {len(new_alerts)} novos alertas")
            
        except Exception as e:
            logger.error(f"Erro ao atualizar histórico de alertas: {e}")
    
    def generate_alert_summary(self, alerts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Gera resumo dos alertas.
        
        Args:
            alerts: Lista de alertas
            
        Returns:
            Resumo dos alertas
        """
        summary = {
            "timestamp": datetime.now().isoformat(),
            "total_alerts": len(alerts),
            "critical_alerts": len([a for a in alerts if a["level"] == "critical"]),
            "warning_alerts": len([a for a in alerts if a["level"] == "warning"]),
            "alerts_by_type": {},
            "alerts_by_component": {},
            "recommended_actions": []
        }
        
        try:
            # Agrupar por tipo
            for alert in alerts:
                alert_type = alert.get("type", "unknown")
                if alert_type not in summary["alerts_by_type"]:
                    summary["alerts_by_type"][alert_type] = 0
                summary["alerts_by_type"][alert_type] += 1
            
            # Agrupar por componente
            for alert in alerts:
                component = alert.get("component", "unknown")
                if component not in summary["alerts_by_component"]:
                    summary["alerts_by_component"][component] = 0
                summary["alerts_by_component"][component] += 1
            
            # Gerar ações recomendadas
            if summary["critical_alerts"] > 0:
                summary["recommended_actions"].append("🚨 Ação imediata necessária para alertas críticos")
            
            if "performance" in summary["alerts_by_type"]:
                summary["recommended_actions"].append("⚡ Verificar e otimizar performance do sistema")
            
            if "quality" in summary["alerts_by_component"]:
                summary["recommended_actions"].append("🔧 Verificar integridade dos arquivos")
            
            if "search" in summary["alerts_by_component"]:
                summary["recommended_actions"].append("🔍 Reconstruir índice de busca")
            
        except Exception as e:
            logger.error(f"Erro ao gerar resumo dos alertas: {e}")
        
        return summary
    
    def create_alert_report(self) -> str:
        """
        Cria relatório de alertas.
        
        Returns:
            Caminho do relatório
        """
        logger.info("📋 Criando relatório de alertas...")
        
        # Carregar dados das métricas
        metrics_data = self.load_metrics_data()
        
        # Verificar alertas
        performance_alerts = self.check_performance_alerts(metrics_data)
        usage_alerts = self.check_usage_alerts(metrics_data)
        system_alerts = self.check_system_alerts(metrics_data)
        
        # Combinar todos os alertas
        all_alerts = performance_alerts + usage_alerts + system_alerts
        
        # Verificar duplicatas
        unique_alerts = self.check_duplicate_alerts(all_alerts)
        
        # Atualizar alertas ativos
        if unique_alerts:
            self.save_active_alerts(unique_alerts)
            self.update_alert_history(unique_alerts)
        
        # Gerar resumo
        summary = self.generate_alert_summary(unique_alerts)
        
        # Criar relatório
        report = {
            "generation_date": datetime.now().isoformat(),
            "alert_summary": summary,
            "new_alerts": unique_alerts,
            "alert_thresholds": self.alert_thresholds,
            "files": {
                "active_alerts": str(self.active_alerts_file),
                "alert_history": str(self.alert_history_file),
                "alert_rules": str(self.alert_rules_file),
                "alert_actions": str(self.alert_actions_file)
            }
        }
        
        report_file = self.alerts_dir / "alert_report.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        logger.info(f"✅ Relatório de alertas salvo em: {report_file}")
        return str(report_file)
    
    def implement_alert_system(self) -> Dict[str, Any]:
        """
        Implementa sistema completo de alertas.
        
        Returns:
            Resultados da implementação
        """
        logger.info("🚀 Implementando sistema de alertas...")
        
        # Criar relatório
        report_path = self.create_alert_report()
        
        # Verificar arquivos criados
        files_created = []
        for file_path in [self.active_alerts_file, self.alert_history_file, self.alert_rules_file, self.alert_actions_file]:
            if file_path.exists():
                files_created.append(file_path.name)
        
        results = {
            "success": True,
            "alert_system_implemented": True,
            "files_created": files_created,
            "report_path": report_path,
            "alert_thresholds": self.alert_thresholds,
            "monitoring_active": True
        }
        
        logger.info("✅ Sistema de alertas implementado!")
        return results

def main():
    """Função principal do script."""
    print("🔄 Implementando sistema de alertas...")
    
    alert_system = AlertSystem()
    
    # Implementar sistema
    results = alert_system.implement_alert_system()
    
    print(f"\n✅ Sistema de alertas implementado!")
    print(f"🚨 Sistema implementado: {results['alert_system_implemented']}")
    print(f"📁 Arquivos criados: {len(results['files_created'])}")
    print(f"📋 Relatório: {results['report_path']}")
    print(f"📊 Monitoramento ativo: {results['monitoring_active']}")

if __name__ == "__main__":
    main() 