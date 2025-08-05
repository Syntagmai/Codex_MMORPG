from unicode_aliases import *
from collections import defaultdict, Counter
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import argparse
import json
import os
import re
import sys

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OTClient Log Analyzer
Script especializado para análise de logs do OTClient e debug
"""


class OTClientLogAnalyzer:
    """Analisador especializado de logs do OTClient"""
    
    def __init__(self, work_dir: str = "."):
        self.work_dir = Path(work_dir)
        self.log_files = {
            "main": self.work_dir / "otclient.log",
            "debug": self.work_dir / "debug.log",
            "packet": self.work_dir / "packet.log",
            "crash": self.work_dir / "crash.log"
        }
        
        # Padrões de log do OTClient
        self.log_patterns = {
            "timestamp": r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]",
            "level": r"\[(TRACE|DEBUG|INFO|WARN|ERROR|FATAL)\]",
            "category": r"\[(SYSTEM|NETWORK|GAME|UI|COMBAT|INVENTORY|MODULE)\]",
            "message": r"\] (.+)$"
        }
        
        # Padrões de erro específicos
        self.error_patterns = {
            "crash": [
                r"FATAL.*crash",
                r"Exception.*thrown",
                r"Segmentation fault",
                r"Access violation",
                r"Stack overflow"
            ],
            "memory": [
                r"memory leak",
                r"out of memory",
                r"allocation failed",
                r"memory corruption"
            ],
            "network": [
                r"connection.*failed",
                r"timeout",
                r"protocol.*error",
                r"packet.*corrupted"
            ],
            "lua": [
                r"Lua.*error",
                r"script.*failed",
                r"module.*error",
                r"syntax.*error"
            ],
            "rendering": [
                r"OpenGL.*error",
                r"rendering.*failed",
                r"texture.*error",
                r"shader.*error"
            ]
        }
        
        # Análise de performance
        self.performance_metrics = {
            "fps": [],
            "memory_usage": [],
            "cpu_usage": [],
            "network_latency": []
        }
        
        # Estatísticas de análise
        self.analysis_stats = {
            "total_entries": 0,
            "error_count": 0,
            "warning_count": 0,
            "crash_count": 0,
            "performance_issues": 0
        }
    
    def analyze_logs(self, log_file: str = "main") -> Dict[str, Any]:
        """Analisa logs do OTClient"""
        print(f"🔍 Analisando logs do OTClient: {log_file}")
        
        log_path = self.log_files.get(log_file)
        if not log_path or not log_path.exists():
            print(f"❌ Arquivo de log não encontrado: {log_path}")
            return {}
        
        try:
            with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
                log_content = f.read()
            
            # Parsear entradas de log
            log_entries = self.parse_log_entries(log_content)
            
            # Analisar padrões
            analysis = {
                "file": str(log_path),
                "total_entries": len(log_entries),
                "time_range": self.get_time_range(log_entries),
                "level_distribution": self.analyze_level_distribution(log_entries),
                "category_distribution": self.analyze_category_distribution(log_entries),
                "error_analysis": self.analyze_errors(log_entries),
                "performance_analysis": self.analyze_performance(log_entries),
                "crash_analysis": self.analyze_crashes(log_entries),
                "pattern_analysis": self.analyze_patterns(log_entries),
                "recommendations": self.generate_recommendations(log_entries)
            }
            
            return analysis
            
        except Exception as e:
            print(f"❌ Erro ao analisar logs: {e}")
            return {}
    
    def parse_log_entries(self, log_content: str) -> List[Dict[str, Any]]:
        """Parseia entradas de log"""
        entries = []
        lines = log_content.split('\n')
        
        for line in lines:
            if not line.strip():
                continue
            
            entry = self.parse_log_line(line)
            if entry:
                entries.append(entry)
        
        return entries
    
    def parse_log_line(self, line: str) -> Optional[Dict[str, Any]]:
        """Parseia uma linha de log"""
        try:
            # Padrão básico: [timestamp][level][category] message
            pattern = r"\[([^\]]+)\]\[([^\]]+)\]\[([^\]]+)\]\s*(.+)"
            match = re.match(pattern, line)
            
            if match:
                timestamp, level, category, message = match.groups()
                return {
                    "timestamp": timestamp,
                    "level": level,
                    "category": category,
                    "message": message,
                    "raw_line": line
                }
            
            # Padrão alternativo: [timestamp][level] message
            pattern2 = r"\[([^\]]+)\]\[([^\]]+)\]\s*(.+)"
            match2 = re.match(pattern2, line)
            
            if match2:
                timestamp, level, message = match2.groups()
                return {
                    "timestamp": timestamp,
                    "level": level,
                    "category": "UNKNOWN",
                    "message": message,
                    "raw_line": line
                }
            
            return None
            
        except Exception as e:
            print(f"Erro ao parsear linha: {line[:100]}... - {e}")
            return None
    
    def get_time_range(self, entries: List[Dict[str, Any]]) -> Dict[str, str]:
        """Obtém o intervalo de tempo dos logs"""
        if not entries:
            return {"start": "", "end": ""}
        
        timestamps = [entry["timestamp"] for entry in entries if entry.get("timestamp")]
        if timestamps:
            return {
                "start": min(timestamps),
                "end": max(timestamps)
            }
        
        return {"start": "", "end": ""}
    
    def analyze_level_distribution(self, entries: List[Dict[str, Any]]) -> Dict[str, int]:
        """Analisa distribuição de níveis de log"""
        level_counts = Counter(entry["level"] for entry in entries if entry.get("level"))
        return dict(level_counts)
    
    def analyze_category_distribution(self, entries: List[Dict[str, Any]]) -> Dict[str, int]:
        """Analisa distribuição de categorias"""
        category_counts = Counter(entry["category"] for entry in entries if entry.get("category"))
        return dict(category_counts)
    
    def analyze_errors(self, entries: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analisa erros nos logs"""
        error_entries = [entry for entry in entries if entry.get("level") in ["ERROR", "FATAL"]]
        
        error_analysis = {
            "total_errors": len(error_entries),
            "error_types": {},
            "error_frequency": {},
            "error_contexts": []
        }
        
        for entry in error_entries:
            message = entry.get("message", "")
            category = entry.get("category", "UNKNOWN")
            
            # Classificar tipo de erro
            error_type = self.classify_error(message)
            error_analysis["error_types"][error_type] = error_analysis["error_types"].get(error_type, 0) + 1
            
            # Análise de frequência
            error_key = f"{category}:{error_type}"
            error_analysis["error_frequency"][error_key] = error_analysis["error_frequency"].get(error_key, 0) + 1
            
            # Contexto do erro
            error_analysis["error_contexts"].append({
                "timestamp": entry.get("timestamp"),
                "category": category,
                "type": error_type,
                "message": message
            })
        
        return error_analysis
    
    def classify_error(self, message: str) -> str:
        """Classifica o tipo de erro"""
        message_lower = message.lower()
        
        for error_type, patterns in self.error_patterns.items():
            for pattern in patterns:
                if re.search(pattern, message_lower, re.IGNORECASE):
                    return error_type
        
        return "unknown"
    
    def analyze_performance(self, entries: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analisa métricas de performance"""
        performance_analysis = {
            "fps_issues": [],
            "memory_issues": [],
            "network_issues": [],
            "performance_patterns": []
        }
        
        for entry in entries:
            message = entry.get("message", "")
            category = entry.get("category", "")
            
            # Análise de FPS
            if "fps" in message.lower() or "frame" in message.lower():
                fps_match = re.search(r"(\d+(?:\.\d+)?)\s*fps", message, re.IGNORECASE)
                if fps_match:
                    fps_value = float(fps_match.group(1))
                    if fps_value < 30:
                        performance_analysis["fps_issues"].append({
                            "timestamp": entry.get("timestamp"),
                            "fps": fps_value,
                            "message": message
                        })
            
            # Análise de memória
            if "memory" in message.lower() or "ram" in message.lower():
                memory_match = re.search(r"(\d+(?:\.\d+)?)\s*(?:mb|gb)", message, re.IGNORECASE)
                if memory_match:
                    memory_value = float(memory_match.group(1))
                    performance_analysis["memory_issues"].append({
                        "timestamp": entry.get("timestamp"),
                        "memory": memory_value,
                        "message": message
                    })
            
            # Análise de rede
            if category == "NETWORK" and ("latency" in message.lower() or "ping" in message.lower()):
                latency_match = re.search(r"(\d+(?:\.\d+)?)\s*(?:ms|milliseconds)", message, re.IGNORECASE)
                if latency_match:
                    latency_value = float(latency_match.group(1))
                    if latency_value > 100:
                        performance_analysis["network_issues"].append({
                            "timestamp": entry.get("timestamp"),
                            "latency": latency_value,
                            "message": message
                        })
        
        return performance_analysis
    
    def analyze_crashes(self, entries: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analisa crashes do cliente"""
        crash_entries = [entry for entry in entries if entry.get("level") == "FATAL"]
        
        crash_analysis = {
            "total_crashes": len(crash_entries),
            "crash_patterns": [],
            "crash_contexts": []
        }
        
        for entry in crash_entries:
            message = entry.get("message", "")
            
            # Identificar padrão de crash
            crash_pattern = self.identify_crash_pattern(message)
            
            crash_analysis["crash_patterns"].append({
                "pattern": crash_pattern,
                "timestamp": entry.get("timestamp"),
                "message": message
            })
            
            crash_analysis["crash_contexts"].append({
                "timestamp": entry.get("timestamp"),
                "category": entry.get("category"),
                "pattern": crash_pattern,
                "message": message
            })
        
        return crash_analysis
    
    def identify_crash_pattern(self, message: str) -> str:
        """Identifica padrão de crash"""
        message_lower = message.lower()
        
        if "segmentation fault" in message_lower:
            return "segmentation_fault"
        elif "access violation" in message_lower:
            return "access_violation"
        elif "stack overflow" in message_lower:
            return "stack_overflow"
        elif "out of memory" in message_lower:
            return "out_of_memory"
        elif "exception" in message_lower:
            return "exception"
        else:
            return "unknown_crash"
    
    def analyze_patterns(self, entries: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analisa padrões nos logs"""
        pattern_analysis = {
            "recurring_errors": [],
            "error_sequences": [],
            "performance_degradation": [],
            "unusual_patterns": []
        }
        
        # Análise de erros recorrentes
        error_messages = [entry["message"] for entry in entries if entry.get("level") in ["ERROR", "FATAL"]]
        error_counts = Counter(error_messages)
        
        for message, count in error_counts.most_common(10):
            if count > 1:
                pattern_analysis["recurring_errors"].append({
                    "message": message,
                    "count": count
                })
        
        # Análise de sequências de erro
        error_sequence = []
        for entry in entries:
            if entry.get("level") in ["ERROR", "FATAL"]:
                error_sequence.append({
                    "timestamp": entry.get("timestamp"),
                    "message": entry.get("message")
                })
        
        if len(error_sequence) > 1:
            pattern_analysis["error_sequences"] = error_sequence
        
        return pattern_analysis
    
    def generate_recommendations(self, entries: List[Dict[str, Any]]) -> List[str]:
        """Gera recomendações baseadas na análise"""
        recommendations = []
        
        # Analisar distribuição de níveis
        level_dist = self.analyze_level_distribution(entries)
        error_count = level_dist.get("ERROR", 0)
        fatal_count = level_dist.get("FATAL", 0)
        
        if error_count > 10:
            recommendations.append("🔴 Alto número de erros detectado. Recomenda-se investigação imediata.")
        
        if fatal_count > 0:
            recommendations.append("🚨 Crashes detectados. Prioridade máxima para correção.")
        
        # Analisar performance
        performance_analysis = self.analyze_performance(entries)
        
        if performance_analysis["fps_issues"]:
            recommendations.append("⚡ Problemas de FPS detectados. Verificar otimizações de renderização.")
        
        if performance_analysis["memory_issues"]:
            recommendations.append("💾 Problemas de memória detectados. Verificar vazamentos de memória.")
        
        if performance_analysis["network_issues"]:
            recommendations.append("🌐 Problemas de rede detectados. Verificar conectividade e latência.")
        
        # Verificar padrões de erro
        pattern_analysis = self.analyze_patterns(entries)
        
        if pattern_analysis["recurring_errors"]:
            recommendations.append("🔄 Erros recorrentes detectados. Implementar correções permanentes.")
        
        if not recommendations:
            recommendations.append("✅ Logs parecem normais. Continuar monitoramento.")
        
        return recommendations
    
    def generate_report(self, analysis: Dict[str, Any]) -> str:
        """Gera relatório de análise"""
        if not analysis:
            return "❌ Nenhuma análise disponível"
        
        report = f"""# Relatório de Análise de Logs OTClient

## 📊 Resumo Geral
- **Arquivo**: {analysis.get('file', 'N/A')}
- **Total de Entradas**: {analysis.get('total_entries', 0)}
- **Período**: {analysis.get('time_range', {}).get('start', 'N/A')} até {analysis.get('time_range', {}).get('end', 'N/A')}

## 📈 Distribuição por Nível
"""
        
        level_dist = analysis.get('level_distribution', {})
        for level, count in level_dist.items():
            report += f"- **{level}**: {count} entradas\n"
        
        report += "\n## 🏷️ Distribuição por Categoria\n"
        category_dist = analysis.get('category_distribution', {})
        for category, count in category_dist.items():
            report += f"- **{category}**: {count} entradas\n"
        
        # Análise de Erros
        error_analysis = analysis.get('error_analysis', {})
        if error_analysis.get('total_errors', 0) > 0:
            report += f"\n## 🚨 Análise de Erros\n"
            report += f"- **Total de Erros**: {error_analysis['total_errors']}\n"
            
            report += "\n### Tipos de Erro:\n"
            for error_type, count in error_analysis.get('error_types', {}).items():
                report += f"- **{error_type}**: {count}\n"
        
        # Análise de Performance
        performance_analysis = analysis.get('performance_analysis', {})
        if any(performance_analysis.values()):
            report += f"\n## ⚡ Análise de Performance\n"
            
            if performance_analysis.get('fps_issues'):
                report += f"- **Problemas de FPS**: {len(performance_analysis['fps_issues'])}\n"
            
            if performance_analysis.get('memory_issues'):
                report += f"- **Problemas de Memória**: {len(performance_analysis['memory_issues'])}\n"
            
            if performance_analysis.get('network_issues'):
                report += f"- **Problemas de Rede**: {len(performance_analysis['network_issues'])}\n"
        
        # Análise de Crashes
        crash_analysis = analysis.get('crash_analysis', {})
        if crash_analysis.get('total_crashes', 0) > 0:
            report += f"\n## 💥 Análise de Crashes\n"
            report += f"- **Total de Crashes**: {crash_analysis['total_crashes']}\n"
            
            report += "\n### Padrões de Crash:\n"
            for crash in crash_analysis.get('crash_patterns', []):
                report += f"- **{crash['pattern']}**: {crash['timestamp']}\n"
        
        # Recomendações
        recommendations = analysis.get('recommendations', [])
        if recommendations:
            report += f"\n## 💡 Recomendações\n"
            for rec in recommendations:
                report += f"- {rec}\n"
        
        return report
    
    def save_analysis(self, analysis: Dict[str, Any], output_file: str = "otclient_log_analysis.json"):
        """Salva análise em arquivo JSON"""
        try:
            output_path = self.work_dir / output_file
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(analysis, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Análise salva em: {output_path}")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao salvar análise: {e}")
            return False

def main():
    """Função principal"""
    parser = argparse.ArgumentParser(description="OTClient Log Analyzer")
    parser.add_argument("--work-dir", default=".", help="Diretório de trabalho")
    parser.add_argument("--log-file", default="main", choices=["main", "debug", "packet", "crash"], help="Arquivo de log para analisar")
    parser.add_argument("--output", default="otclient_log_analysis.json", help="Arquivo de saída")
    parser.add_argument("--report", action="store_true", help="Gerar relatório em markdown")
    
    args = parser.parse_args()
    
    print("🔍 OTClient Log Analyzer")
    print("=" * 50)
    
    # Inicializar analisador
    analyzer = OTClientLogAnalyzer(args.work_dir)
    
    # Analisar logs
    analysis = analyzer.analyze_logs(args.log_file)
    
    if analysis:
        # Salvar análise
        analyzer.save_analysis(analysis, args.output)
        
        # Gerar relatório
        if args.report:
            report = analyzer.generate_report(analysis)
            report_file = Path(args.work_dir) / "otclient_log_analysis_report.md"
            
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write(report)
            
            print(f"✅ Relatório salvo em: {report_file}")
        
        print("✅ Análise concluída com sucesso!")
    else:
        print("❌ Falha na análise")

if __name__ == "__main__":
    main() 
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
- **Nome**: otclient_log_analyzer
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

