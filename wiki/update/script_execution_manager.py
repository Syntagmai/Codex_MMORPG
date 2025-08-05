#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from unicode_aliases import *
"""
Gerenciador de Execução de Scripts Python
Gerencia a execução de scripts Python com resolução automática de erros
"""

import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

class ScriptExecutionManager:
    def __init__(self):
        self.project_root = Path(".")
        self.update_path = self.project_root / "wiki/update"
        self.log_path = self.project_root / "wiki/log"
        
        # Configurações
        self.max_retries = 3
        self.timeout_seconds = 60
        self.error_resolver_path = self.update_path / "python_error_resolver.py"
        
        # Cache de scripts executados
        self.execution_cache = {}
        
    def execute_script_with_error_resolution(self, script_path: str, args: List[str] = None) -> Dict[str, Any]:
        """Executa script Python com resolução automática de erros"""
        print(f"🚀 Executando script: {script_path}")
        
        if args is None:
            args = []
        
        execution_result = {
            "script_path": script_path,
            "args": args,
            "timestamp": datetime.now().isoformat(),
            "attempts": 0,
            "success": False,
            "error_resolved": False,
            "output": "",
            "error": "",
            "execution_time": 0
        }
        
        # Tentar executar o script
        for attempt in range(self.max_retries):
            execution_result["attempts"] = attempt + 1
            print(f"📋 Tentativa {attempt + 1}/{self.max_retries}")
            
            start_time = time.time()
            
            try:
                # Executar script
                cmd = [sys.executable, script_path] + args
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=self.timeout_seconds)
                
                execution_time = time.time() - start_time
                execution_result["execution_time"] = round(execution_time, 2)
                
                if result.returncode == 0:
                    execution_result["success"] = True
                    execution_result["output"] = result.stdout
                    print(f"✅ Script executado com sucesso em {execution_time:.2f}s")
                    break
                else:
                    execution_result["error"] = result.stderr
                    print(f"❌ Erro na execução: {result.stderr}")
                    
                    # Tentar resolver erro automaticamente
                    if self.resolve_script_error(script_path, result.stderr):
                        execution_result["error_resolved"] = True
                        print("🔄 Erro resolvido, tentando executar novamente...")
                        continue
                    else:
                        print("⚠️ Não foi possível resolver o erro automaticamente")
                        break
                        
            except subprocess.TimeoutExpired:
                execution_result["error"] = "Timeout: Script demorou muito para executar"
                print("⏰ Timeout na execução")
                break
            except Exception as e:
                execution_result["error"] = str(e)
                print(f"❌ Erro inesperado: {e}")
                break
        
        # Registrar resultado
        self.log_execution(execution_result)
        
        return execution_result
    
    def resolve_script_error(self, script_path: str, error_message: str) -> bool:
        """Resolve erro em script usando o resolver automático"""
        try:
            if not self.error_resolver_path.exists():
                print("⚠️ Resolver de erros não encontrado")
                return False
            
            # Executar resolver de erros
            cmd = [sys.executable, str(self.error_resolver_path), script_path]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                print("Erro resolvido automaticamente")
                return True
            else:
                print(f"❌ Resolver não conseguiu corrigir: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Erro ao executar resolver: {e}")
            return False
    
    def execute_script_safely(self, script_path: str, args: List[str] = None) -> bool:
        """Executa script de forma segura com fallback"""
        print(f"🛡️ Executando script com segurança: {script_path}")
        
        result = self.execute_script_with_error_resolution(script_path, args)
        
        if result["success"]:
            return True
        
        # Se falhou, tentar fallback
        print("🔄 Tentando modo fallback...")
        return self.execute_fallback_mode(script_path, args)
    
    def execute_fallback_mode(self, script_path: str, args: List[str] = None) -> bool:
        """Executa script em modo fallback (simplificado)"""
        try:
            print(f"🔄 Modo fallback para {script_path}")
            
            # Verificar se é um script de atualização de mapas
            if "update" in script_path and "maps" in script_path:
                print("📋 Detectado script de atualização de mapas")
                return self.create_basic_map_update(script_path)
            
            # Verificar se é um script de análise
            if "analyze" in script_path:
                print("📊 Detectado script de análise")
                return self.create_basic_analysis_report(script_path)
            
            # Fallback genérico
            print("⚠️ Fallback genérico - criando relatório básico")
            return self.create_basic_report(script_path)
            
        except Exception as e:
            print(f"❌ Erro no modo fallback: {e}")
            return False
    
    def create_basic_map_update(self, script_path: str) -> bool:
        """Cria atualização básica de mapas"""
        try:
            script_name = Path(script_path).stem
            
            # Determinar tipo de mapa baseado no nome do script
            if "source" in script_name:
                map_file = self.project_root / "wiki/maps/otclient_source_index.json"
                basic_data = {
                    "metadata": {
                        "version": "1.0",
                        "last_updated": datetime.now().isoformat(),
                        "status": "basic_fallback"
                    },
                    "source_files": []
                }
            elif "wiki" in script_name:
                map_file = self.project_root / "wiki/maps/wiki_map.json"
                basic_data = {
                    "metadata": {
                        "version": "1.0",
                        "last_updated": datetime.now().isoformat(),
                        "status": "basic_fallback"
                    },
                    "categories": {},
                    "files": {}
                }
            else:
                map_file = self.project_root / "wiki/maps/basic_fallback.json"
                basic_data = {
                    "metadata": {
                        "version": "1.0",
                        "last_updated": datetime.now().isoformat(),
                        "status": "basic_fallback",
                        "script": script_name
                    }
                }
            
            # Salvar mapa básico
            map_file.parent.mkdir(parents=True, exist_ok=True)
            with open(map_file, 'w', encoding='utf-8') as f:
                json.dump(basic_data, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Mapa básico criado: {map_file}")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao criar mapa básico: {e}")
            return False
    
    def create_basic_analysis_report(self, script_path: str) -> bool:
        """Cria relatório básico de análise"""
        try:
            script_name = Path(script_path).stem
            report_file = self.project_root / "wiki/maps" / f"{script_name}_fallback_report.json"
            
            basic_report = {
                "metadata": {
                    "version": "1.0",
                    "last_updated": datetime.now().isoformat(),
                    "status": "fallback_report",
                    "script": script_name
                },
                "analysis": {
                    "status": "basic_fallback",
                    "message": "Análise básica criada devido a erro no script original"
                }
            }
            
            report_file.parent.mkdir(parents=True, exist_ok=True)
            with open(report_file, 'w', encoding='utf-8') as f:
                json.dump(basic_report, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Relatório básico criado: {report_file}")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao criar relatório básico: {e}")
            return False
    
    def create_basic_report(self, script_path: str) -> bool:
        """Cria relatório básico genérico"""
        try:
            script_name = Path(script_path).stem
            report_file = self.project_root / "wiki/log" / f"{script_name}_fallback.log"
            
            basic_report = f"""
Script: {script_path}
Status: Fallback Mode
Timestamp: {datetime.now().isoformat()}
Message: Script executado em modo fallback devido a erros
            """.strip()
            
            report_file.parent.mkdir(parents=True, exist_ok=True)
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write(basic_report)
            
            print(f"✅ Relatório básico criado: {report_file}")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao criar relatório básico: {e}")
            return False
    
    def log_execution(self, execution_result: Dict[str, Any]):
        """Registra resultado da execução"""
        log_file = self.log_path / "script_executions.json"
        
        # Carregar log existente
        executions = []
        if log_file.exists():
            try:
                with open(log_file, 'r', encoding='utf-8') as f:
                    executions = json.load(f)
            except:
                executions = []
        
        # Adicionar nova execução
        executions.append(execution_result)
        
        # Manter apenas as últimas 100 execuções
        if len(executions) > 100:
            executions = executions[-100:]
        
        # Salvar log
        log_file.parent.mkdir(parents=True, exist_ok=True)
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(executions, f, indent=2, ensure_ascii=False)
        
        print(f"Execucao registrada em {log_file}")
    
    def get_execution_stats(self) -> Dict[str, Any]:
        """Obtém estatísticas de execução"""
        log_file = self.log_path / "script_executions.json"
        
        if not log_file.exists():
            return {"total_executions": 0, "success_rate": 0}
        
        try:
            with open(log_file, 'r', encoding='utf-8') as f:
                executions = json.load(f)
            
            total = len(executions)
            successful = sum(1 for e in executions if e.get("success", False))
            success_rate = (successful / total * 100) if total > 0 else 0
            
            return {
                "total_executions": total,
                "successful_executions": successful,
                "success_rate": round(success_rate, 2),
                "error_resolutions": sum(1 for e in executions if e.get("error_resolved", False))
            }
            
        except Exception as e:
            print(f"❌ Erro ao obter estatísticas: {e}")
            return {"total_executions": 0, "success_rate": 0}

def main():
    """Função principal"""
    if len(sys.argv) < 2:
        print("❌ Uso: python script_execution_manager.py <script_path> [args...]")
        sys.exit(1)
    
    script_path = sys.argv[1]
    args = sys.argv[2:] if len(sys.argv) > 2 else []
    
    manager = ScriptExecutionManager()
    
    # Executar script com resolução de erros
    result = manager.execute_script_with_error_resolution(script_path, args)
    
    # Exibir estatísticas
    stats = manager.get_execution_stats()
    print(f"\n📊 Estatísticas de Execução:")
    print(f"   Total de execuções: {stats['total_executions']}")
    print(f"   Taxa de sucesso: {stats['success_rate']}%")
    print(f"   Erros resolvidos: {stats.get('error_resolutions', 0)}")
    
    # Retornar código de saída
    if result["success"]:
        print("✅ Execução concluída com sucesso")
        sys.exit(0)
    else:
        print("❌ Execução não foi bem-sucedida")
        sys.exit(1)

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
- **Nome**: script_execution_manager
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

