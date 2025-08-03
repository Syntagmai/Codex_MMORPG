#!/usr/bin/env python3
"""
Performance Auditor Agent - Epic 17 Task 17.6
Analisa performance e recursos do sistema
"""

import os
import json
import time
import psutil
import re
from datetime import datetime
from pathlib import Path

class PerformanceAuditor:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.report = {
            "timestamp": datetime.now().isoformat(),
            "project_root": str(self.project_root),
            "performance_issues": [],
            "large_files": [],
            "slow_scripts": [],
            "memory_usage": {},
            "bottlenecks": [],
            "optimization_opportunities": [],
            "metrics": {}
        }
    
    def analyze_large_files(self):
        """Analisa arquivos grandes que podem impactar performance"""
        print("🔍 Analisando arquivos grandes...")
        
        large_files = []
        for root, dirs, files in os.walk(self.project_root):
            for file in files:
                file_path = Path(root) / file
                try:
                    size = file_path.stat().st_size
                    if size > 1024 * 1024:  # > 1MB
                        large_files.append({
                            "path": str(file_path.relative_to(self.project_root)),
                            "size_mb": round(size / (1024 * 1024), 2),
                            "type": file_path.suffix
                        })
                except:
                    continue
        
        # Ordenar por tamanho
        large_files.sort(key=lambda x: x["size_mb"], reverse=True)
        self.report["large_files"] = large_files[:20]  # Top 20
    
    def analyze_slow_scripts(self):
        """Analisa scripts que podem ser lentos"""
        print("🔍 Analisando scripts lentos...")
        
        slow_scripts = []
        for root, dirs, files in os.walk(self.project_root):
            for file in files:
                if file.endswith(('.py', '.lua', '.js', '.sh', '.bat')):
                    file_path = Path(root) / file
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            
                        # Indicadores de scripts lentos
                        indicators = {
                            "loops": len(re.findall(r'\b(for|while)\b', content)),
                            "file_operations": len(re.findall(r'\b(open|read|write|file)\b', content)),
                            "network_calls": len(re.findall(r'\b(requests|urllib|http|socket)\b', content)),
                            "database_queries": len(re.findall(r'\b(select|insert|update|delete|query)\b', content, re.IGNORECASE)),
                            "complexity": len(content.split('\n'))
                        }
                        
                        # Score de complexidade
                        complexity_score = (
                            indicators["loops"] * 2 +
                            indicators["file_operations"] * 3 +
                            indicators["network_calls"] * 5 +
                            indicators["database_queries"] * 4 +
                            indicators["complexity"] * 0.1
                        )
                        
                        if complexity_score > 50:
                            slow_scripts.append({
                                "path": str(file_path.relative_to(self.project_root)),
                                "complexity_score": round(complexity_score, 2),
                                "indicators": indicators
                            })
                    except:
                        continue
        
        # Ordenar por score
        slow_scripts.sort(key=lambda x: x["complexity_score"], reverse=True)
        self.report["slow_scripts"] = slow_scripts[:15]  # Top 15
    
    def analyze_memory_usage(self):
        """Analisa uso de memória do sistema"""
        print("🔍 Analisando uso de memória...")
        
        try:
            process = psutil.Process()
            memory_info = process.memory_info()
            
            self.report["memory_usage"] = {
                "rss_mb": round(memory_info.rss / (1024 * 1024), 2),
                "vms_mb": round(memory_info.vms / (1024 * 1024), 2),
                "percent": process.memory_percent()
            }
        except:
            self.report["memory_usage"] = {"error": "Não foi possível obter informações de memória"}
    
    def identify_bottlenecks(self):
        """Identifica gargalos potenciais"""
        print("🔍 Identificando gargalos...")
        
        bottlenecks = []
        
        # Verificar arquivos de configuração
        config_patterns = [
            r'max_connections\s*=\s*\d+',
            r'timeout\s*=\s*\d+',
            r'cache_size\s*=\s*\d+',
            r'buffer_size\s*=\s*\d+'
        ]
        
        for root, dirs, files in os.walk(self.project_root):
            for file in files:
                if file.endswith(('.conf', '.config', '.ini', '.json', '.yml', '.yaml')):
                    file_path = Path(root) / file
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            
                        for pattern in config_patterns:
                            matches = re.findall(pattern, content, re.IGNORECASE)
                            if matches:
                                bottlenecks.append({
                                    "type": "config_bottleneck",
                                    "file": str(file_path.relative_to(self.project_root)),
                                    "pattern": pattern,
                                    "matches": len(matches)
                                })
                    except:
                        continue
        
        # Verificar loops infinitos ou muito longos
        for root, dirs, files in os.walk(self.project_root):
            for file in files:
                if file.endswith(('.py', '.lua', '.js')):
                    file_path = Path(root) / file
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            
                        # Verificar loops sem break ou condição de saída
                        lines = content.split('\n')
                        for i, line in enumerate(lines):
                            if re.search(r'\bwhile\s+True\b', line):
                                # Verificar se há break nas próximas linhas
                                next_lines = lines[i+1:i+10]
                                if not any('break' in l for l in next_lines):
                                    bottlenecks.append({
                                        "type": "infinite_loop",
                                        "file": str(file_path.relative_to(self.project_root)),
                                        "line": i + 1,
                                        "code": line.strip()
                                    })
                    except:
                        continue
        
        self.report["bottlenecks"] = bottlenecks[:20]  # Top 20
    
    def find_optimization_opportunities(self):
        """Encontra oportunidades de otimização"""
        print("🔍 Encontrando oportunidades de otimização...")
        
        opportunities = []
        
        # Verificar imports desnecessários
        for root, dirs, files in os.walk(self.project_root):
            for file in files:
                if file.endswith('.py'):
                    file_path = Path(root) / file
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            
                        # Verificar imports não utilizados
                        import_lines = re.findall(r'^import\s+(\w+)', content, re.MULTILINE)
                        from_imports = re.findall(r'^from\s+(\w+)\s+import', content, re.MULTILINE)
                        
                        all_imports = import_lines + from_imports
                        
                        for imp in all_imports:
                            # Verificar se o import é usado no código
                            if imp not in ['os', 'sys', 'json', 're', 'time', 'datetime']:  # Imports comuns
                                if content.count(imp) <= 1:  # Só aparece no import
                                    opportunities.append({
                                        "type": "unused_import",
                                        "file": str(file_path.relative_to(self.project_root)),
                                        "import": imp
                                    })
                    except:
                        continue
        
        # Verificar duplicação de código
        code_snippets = {}
        for root, dirs, files in os.walk(self.project_root):
            for file in files:
                if file.endswith(('.py', '.lua')):
                    file_path = Path(root) / file
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            
                        # Dividir em funções/blocos
                        functions = re.findall(r'def\s+(\w+)\s*\([^)]*\):\s*([^#]*?)(?=def|\Z)', content, re.DOTALL)
                        
                        for func_name, func_body in functions:
                            body_hash = hash(func_body.strip())
                            if body_hash in code_snippets:
                                opportunities.append({
                                    "type": "code_duplication",
                                    "file": str(file_path.relative_to(self.project_root)),
                                    "function": func_name,
                                    "duplicate_of": code_snippets[body_hash]
                                })
                            else:
                                code_snippets[body_hash] = f"{file_path.name}:{func_name}"
                    except:
                        continue
        
        self.report["optimization_opportunities"] = opportunities[:15]  # Top 15
    
    def calculate_metrics(self):
        """Calcula métricas gerais de performance"""
        print("🔍 Calculando métricas...")
        
        total_files = 0
        total_size = 0
        file_types = {}
        
        for root, dirs, files in os.walk(self.project_root):
            for file in files:
                total_files += 1
                file_path = Path(root) / file
                try:
                    size = file_path.stat().st_size
                    total_size += size
                    
                    ext = file_path.suffix.lower()
                    file_types[ext] = file_types.get(ext, 0) + 1
                except:
                    continue
        
        self.report["metrics"] = {
            "total_files": total_files,
            "total_size_mb": round(total_size / (1024 * 1024), 2),
            "file_types": dict(sorted(file_types.items(), key=lambda x: x[1], reverse=True)[:10]),
            "average_file_size_kb": round((total_size / total_files) / 1024, 2) if total_files > 0 else 0
        }
    
    def run_audit(self):
        """Executa auditoria completa"""
        print("🚀 Iniciando auditoria de performance e recursos...")
        
        self.analyze_large_files()
        self.analyze_slow_scripts()
        self.analyze_memory_usage()
        self.identify_bottlenecks()
        self.find_optimization_opportunities()
        self.calculate_metrics()
        
        # Salvar relatório
        report_path = self.project_root / "wiki" / "docs" / "audit_reports" / "performance_audit_report.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(self.report, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Relatório salvo em: {report_path}")
        
        # Resumo
        print("\n📊 RESUMO DA AUDITORIA DE PERFORMANCE:")
        print(f"📁 Arquivos grandes (>1MB): {len(self.report['large_files'])}")
        print(f"🐌 Scripts lentos identificados: {len(self.report['slow_scripts'])}")
        print(f"⚠️ Gargalos encontrados: {len(self.report['bottlenecks'])}")
        print(f"🔧 Oportunidades de otimização: {len(self.report['optimization_opportunities'])}")
        print(f"📈 Total de arquivos: {self.report['metrics']['total_files']}")
        print(f"💾 Tamanho total: {self.report['metrics']['total_size_mb']} MB")
        
        return self.report

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        project_root = sys.argv[1]
    else:
        project_root = "."
    
    auditor = PerformanceAuditor(project_root)
    auditor.run_audit() 