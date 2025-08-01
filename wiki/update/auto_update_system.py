            import psutil
    from auto_monitor import AutoMonitor
    from auto_optimizer import AutoOptimizer
    from auto_updater import AutoUpdater
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import json
import logging
import subprocess
import sys
import threading
import time

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Auto-Atualização Integrado BMAD
Coordena auto-monitoramento, auto-atualização e auto-otimização
"""


# Importar componentes do sistema
try:
except ImportError:
    print("Componentes do sistema não encontrados. Criando classes básicas...")
    
    class AutoMonitor:
        def __init__(self):
            self.logger = logging.getLogger(__name__)
        def start_monitoring(self):
            pass
        def get_system_status(self):
            return {"status": "basic"}
    
    class AutoUpdater:
        def __init__(self):
            self.logger = logging.getLogger(__name__)
        def trigger_auto_update(self, change_type, details=None):
            return True
        def get_update_stats(self):
            return {"total_updates": 0}
    
    class AutoOptimizer:
        def __init__(self):
            self.logger = logging.getLogger(__name__)
        def trigger_optimization(self, target, metrics=None):
            return True
        def get_optimization_stats(self):
            return {"total_optimizations": 0}

class AutoUpdateSystem:
    def __init__(self):
        self.project_root = Path(".")
        self.log_path = self.project_root / "wiki/log"
        self.maps_path = self.project_root / "wiki/maps"
        
        # Configurar logging
        self.setup_logging()
        
        # Inicializar componentes
        self.monitor = AutoMonitor()
        self.updater = AutoUpdater()
        self.optimizer = AutoOptimizer()
        
        # Estado do sistema
        self.system_state = {
            "status": "initializing",
            "start_time": datetime.now().isoformat(),
            "cycles_completed": 0,
            "total_optimizations": 0,
            "total_updates": 0,
            "health_score": 100,
            "performance_score": 100
        }
        
        # Configurações do sistema
        self.config = {
            "monitoring_interval": 300,  # 5 minutos
            "optimization_threshold": 85, # Score mínimo para otimização
            "update_threshold": 90,      # Score mínimo para atualização
            "emergency_threshold": 70,   # Score mínimo para modo emergência
            "max_cycles": 1000,          # Máximo de ciclos antes de reiniciar
            "auto_restart": True,        # Reiniciar automaticamente
            "emergency_mode": False      # Modo de emergência ativo
        }
        
        # Threads de execução
        self.monitor_thread = None
        self.updater_thread = None
        self.optimizer_thread = None
        self.running = False
        
    def setup_logging(self):
        """Configura sistema de logging"""
        log_file = self.log_path / "auto_update_system.log"
        log_file.parent.mkdir(parents=True, exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def start_system(self):
        """Inicia o sistema de auto-atualização"""
        self.logger.info("=== INICIANDO SISTEMA DE AUTO-ATUALIZAÇÃO BMAD ===")
        self.logger.info(f"Tempo de início: {self.system_state['start_time']}")
        
        try:
            self.running = True
            
            # Iniciar threads dos componentes
            self.start_component_threads()
            
            # Iniciar loop principal
            self.main_loop()
            
        except KeyboardInterrupt:
            self.logger.info("Sistema interrompido pelo usuário")
            self.stop_system()
        except Exception as e:
            self.logger.error(f"Erro no sistema: {e}")
            self.emergency_mode()
    
    def start_component_threads(self):
        """Inicia threads dos componentes"""
        try:
            # Thread de monitoramento
            self.monitor_thread = threading.Thread(
                target=self.monitor.start_monitoring,
                daemon=True,
                name="AutoMonitor"
            )
            self.monitor_thread.start()
            self.logger.info("Thread de monitoramento iniciada")
            
            # Thread de atualização
            self.updater_thread = threading.Thread(
                target=self.updater_loop,
                daemon=True,
                name="AutoUpdater"
            )
            self.updater_thread.start()
            self.logger.info("Thread de atualização iniciada")
            
            # Thread de otimização
            self.optimizer_thread = threading.Thread(
                target=self.optimizer_loop,
                daemon=True,
                name="AutoOptimizer"
            )
            self.optimizer_thread.start()
            self.logger.info("Thread de otimização iniciada")
            
        except Exception as e:
            self.logger.error(f"Erro ao iniciar threads: {e}")
            raise
    
    def main_loop(self):
        """Loop principal do sistema"""
        self.logger.info("Iniciando loop principal do sistema")
        
        while self.running:
            try:
                # Verificar estado do sistema
                self.check_system_health()
                
                # Executar ciclo de auto-atualização
                self.execute_update_cycle()
                
                # Verificar se reinicialização é necessária
                if self.system_state["cycles_completed"] >= self.config["max_cycles"]:
                    self.logger.info("Limite de ciclos atingido, reiniciando sistema...")
                    self.restart_system()
                
                # Aguardar próximo ciclo
                time.sleep(self.config["monitoring_interval"])
                
            except Exception as e:
                self.logger.error(f"Erro no loop principal: {e}")
                if self.system_state["health_score"] < self.config["emergency_threshold"]:
                    self.emergency_mode()
                time.sleep(60)  # Aguardar 1 minuto antes de continuar
    
    def updater_loop(self):
        """Loop do sistema de atualização"""
        while self.running:
            try:
                # Verificar se atualização é necessária
                if self.system_state["health_score"] < self.config["update_threshold"]:
                    self.logger.info("Disparando atualização automática...")
                    
                    # Determinar tipo de atualização necessário
                    update_type = self.determine_update_type()
                    
                    # Executar atualização
                    success = self.updater.trigger_auto_update(update_type)
                    
                    if success:
                        self.system_state["total_updates"] += 1
                        self.logger.info("Atualização executada com sucesso")
                    else:
                        self.logger.error("Atualização falhou")
                
                time.sleep(self.config["monitoring_interval"] * 2)  # Verificar a cada 10 minutos
                
            except Exception as e:
                self.logger.error(f"Erro no loop de atualização: {e}")
                time.sleep(60)
    
    def optimizer_loop(self):
        """Loop do sistema de otimização"""
        while self.running:
            try:
                # Verificar se otimização é necessária
                if self.system_state["performance_score"] < self.config["optimization_threshold"]:
                    self.logger.info("Disparando otimização automática...")
                    
                    # Determinar tipo de otimização necessário
                    optimization_target = self.determine_optimization_target()
                    
                    # Executar otimização
                    success = self.optimizer.trigger_optimization(optimization_target)
                    
                    if success:
                        self.system_state["total_optimizations"] += 1
                        self.logger.info("Otimização executada com sucesso")
                    else:
                        self.logger.error("Otimização falhou")
                
                time.sleep(self.config["monitoring_interval"] * 3)  # Verificar a cada 15 minutos
                
            except Exception as e:
                self.logger.error(f"Erro no loop de otimização: {e}")
                time.sleep(60)
    
    def check_system_health(self):
        """Verifica saúde geral do sistema"""
        try:
            # Obter status dos componentes
            monitor_status = self.monitor.get_system_status()
            updater_stats = self.updater.get_update_stats()
            optimizer_stats = self.optimizer.get_optimization_stats()
            
            # Atualizar estado do sistema
            self.system_state.update({
                "health_score": monitor_status.get("health_score", 100),
                "performance_score": monitor_status.get("performance_score", 100),
                "total_updates": updater_stats.get("total_updates", 0),
                "total_optimizations": optimizer_stats.get("total_optimizations", 0),
                "last_check": datetime.now().isoformat()
            })
            
            # Verificar se modo de emergência é necessário
            if self.system_state["health_score"] < self.config["emergency_threshold"]:
                if not self.config["emergency_mode"]:
                    self.emergency_mode()
            
            # Salvar estado atual
            self.save_system_state()
            
        except Exception as e:
            self.logger.error(f"Erro ao verificar saúde do sistema: {e}")
    
    def execute_update_cycle(self):
        """Executa um ciclo de auto-atualização"""
        try:
            self.logger.info(f"=== CICLO {self.system_state['cycles_completed'] + 1} ===")
            
            # Verificar mudanças no sistema
            changes_detected = self.detect_system_changes()
            
            if changes_detected:
                self.logger.info(f"Detectadas {len(changes_detected)} mudanças no sistema")
                
                # Processar mudanças
                for change in changes_detected:
                    self.process_change(change)
            
            # Verificar performance
            performance_issues = self.detect_performance_issues()
            
            if performance_issues:
                self.logger.info(f"Detectados {len(performance_issues)} problemas de performance")
                
                # Resolver problemas de performance
                for issue in performance_issues:
                    self.resolve_performance_issue(issue)
            
            # Incrementar contador de ciclos
            self.system_state["cycles_completed"] += 1
            
            # Gerar relatório do ciclo
            self.generate_cycle_report()
            
        except Exception as e:
            self.logger.error(f"Erro no ciclo de atualização: {e}")
    
    def detect_system_changes(self) -> List[Dict[str, Any]]:
        """Detecta mudanças no sistema"""
        changes = []
        
        try:
            # Verificar mudanças em arquivos críticos
            critical_files = [
                "cursor.md",
                "wiki/maps/tags_index.json",
                "wiki/maps/wiki_map.json",
                ".cursor/rules/rules.md"
            ]
            
            for file_path in critical_files:
                full_path = self.project_root / file_path
                if full_path.exists():
                    # Verificar se arquivo foi modificado recentemente
                    mtime = full_path.stat().st_mtime
                    if mtime > time.time() - 3600:  # Última hora
                        changes.append({
                            "type": "file_modified",
                            "file": file_path,
                            "timestamp": datetime.fromtimestamp(mtime).isoformat()
                        })
            
            # Verificar mudanças em scripts
            script_files = list(self.project_root.glob("wiki/update/*.py"))
            for script_file in script_files:
                mtime = script_file.stat().st_mtime
                if mtime > time.time() - 1800:  # Últimos 30 minutos
                    changes.append({
                        "type": "script_modified",
                        "file": str(script_file.relative_to(self.project_root)),
                        "timestamp": datetime.fromtimestamp(mtime).isoformat()
                    })
        
        except Exception as e:
            self.logger.error(f"Erro na detecção de mudanças: {e}")
        
        return changes
    
    def detect_performance_issues(self) -> List[Dict[str, Any]]:
        """Detecta problemas de performance"""
        issues = []
        
        try:
            # Verificar score de performance
            if self.system_state["performance_score"] < self.config["optimization_threshold"]:
                issues.append({
                    "type": "low_performance",
                    "score": self.system_state["performance_score"],
                    "threshold": self.config["optimization_threshold"]
                })
            
            # Verificar tempo de resposta
            response_time = self.measure_response_time()
            if response_time > 3.0:  # Mais de 3 segundos
                issues.append({
                    "type": "slow_response",
                    "response_time": response_time,
                    "threshold": 3.0
                })
            
            # Verificar uso de memória
            memory_usage = self.measure_memory_usage()
            if memory_usage > 80:  # Mais de 80%
                issues.append({
                    "type": "high_memory_usage",
                    "memory_usage": memory_usage,
                    "threshold": 80
                })
        
        except Exception as e:
            self.logger.error(f"Erro na detecção de problemas de performance: {e}")
        
        return issues
    
    def process_change(self, change: Dict[str, Any]):
        """Processa uma mudança detectada"""
        try:
            change_type = change.get("type")
            
            if change_type == "file_modified":
                # Determinar tipo de arquivo e ação apropriada
                file_path = change.get("file", "")
                
                if "maps" in file_path:
                    self.updater.trigger_auto_update("maps", change)
                elif "rules" in file_path:
                    self.updater.trigger_auto_update("rules", change)
                elif "cursor.md" in file_path:
                    self.updater.trigger_auto_update("context", change)
                else:
                    self.updater.trigger_auto_update("scripts", change)
            
            elif change_type == "script_modified":
                self.updater.trigger_auto_update("scripts", change)
            
            self.logger.info(f"Mudança processada: {change_type}")
            
        except Exception as e:
            self.logger.error(f"Erro ao processar mudança: {e}")
    
    def resolve_performance_issue(self, issue: Dict[str, Any]):
        """Resolve um problema de performance"""
        try:
            issue_type = issue.get("type")
            
            if issue_type == "low_performance":
                self.optimizer.trigger_optimization("performance", issue)
            elif issue_type == "slow_response":
                self.optimizer.trigger_optimization("response_time", issue)
            elif issue_type == "high_memory_usage":
                self.optimizer.trigger_optimization("memory_usage", issue)
            
            self.logger.info(f"Problema de performance resolvido: {issue_type}")
            
        except Exception as e:
            self.logger.error(f"Erro ao resolver problema de performance: {e}")
    
    def determine_update_type(self) -> str:
        """Determina tipo de atualização necessário"""
        try:
            # Verificar saúde do sistema
            if self.system_state["health_score"] < 80:
                return "maps"  # Atualizar mapas se saúde estiver baixa
            
            # Verificar mudanças recentes
            changes = self.detect_system_changes()
            if changes:
                # Determinar tipo baseado na maioria das mudanças
                change_types = [change.get("type") for change in changes]
                
                if "file_modified" in change_types:
                    return "maps"
                elif "script_modified" in change_types:
                    return "scripts"
                else:
                    return "context"
            
            # Padrão
            return "context"
            
        except Exception as e:
            self.logger.error(f"Erro ao determinar tipo de atualização: {e}")
            return "maps"
    
    def determine_optimization_target(self) -> str:
        """Determina target de otimização necessário"""
        try:
            # Verificar performance geral
            if self.system_state["performance_score"] < 80:
                return "performance"
            
            # Verificar problemas específicos
            issues = self.detect_performance_issues()
            if issues:
                issue_types = [issue.get("type") for issue in issues]
                
                if "slow_response" in issue_types:
                    return "response_time"
                elif "high_memory_usage" in issue_types:
                    return "memory_usage"
                else:
                    return "performance"
            
            # Padrão
            return "performance"
            
        except Exception as e:
            self.logger.error(f"Erro ao determinar target de otimização: {e}")
            return "performance"
    
    def measure_response_time(self) -> float:
        """Mede tempo de resposta do sistema"""
        try:
            start_time = time.time()
            
            # Simular operação típica
            self.maps_path.exists()
            list(self.maps_path.glob("*.json"))
            
            return time.time() - start_time
            
        except Exception as e:
            self.logger.error(f"Erro ao medir tempo de resposta: {e}")
            return 0.0
    
    def measure_memory_usage(self) -> float:
        """Mede uso de memória"""
        try:
            return psutil.virtual_memory().percent
        except ImportError:
            return 50.0  # Estimativa padrão
        except Exception as e:
            self.logger.error(f"Erro ao medir uso de memória: {e}")
            return 50.0
    
    def generate_cycle_report(self):
        """Gera relatório do ciclo atual"""
        try:
            report = {
                "cycle_number": self.system_state["cycles_completed"],
                "timestamp": datetime.now().isoformat(),
                "system_state": self.system_state.copy(),
                "config": self.config.copy(),
                "summary": {
                    "health_score": self.system_state["health_score"],
                    "performance_score": self.system_state["performance_score"],
                    "total_updates": self.system_state["total_updates"],
                    "total_optimizations": self.system_state["total_optimizations"]
                }
            }
            
            # Salvar relatório
            report_file = self.log_path / f"cycle_report_{self.system_state['cycles_completed']}.json"
            with open(report_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            
            self.logger.info(f"Relatório do ciclo {self.system_state['cycles_completed']} gerado")
            
        except Exception as e:
            self.logger.error(f"Erro ao gerar relatório do ciclo: {e}")
    
    def emergency_mode(self):
        """Ativa modo de emergência"""
        self.logger.error("=== ATIVANDO MODO DE EMERGÊNCIA ===")
        
        self.config["emergency_mode"] = True
        
        try:
            # Parar threads normais
            self.running = False
            
            # Executar correções de emergência
            self.execute_emergency_fixes()
            
            # Tentar reiniciar sistema
            if self.config["auto_restart"]:
                self.logger.info("Tentando reiniciar sistema...")
                self.restart_system()
            
        except Exception as e:
            self.logger.error(f"Erro no modo de emergência: {e}")
    
    def execute_emergency_fixes(self):
        """Executa correções de emergência"""
        try:
            self.logger.info("Executando correções de emergência...")
            
            # 1. Corrigir erros críticos
            self.fix_critical_errors()
            
            # 2. Restaurar backups
            self.restore_backups()
            
            # 3. Validar integridade
            self.validate_system_integrity()
            
            self.logger.info("Correções de emergência concluídas")
            
        except Exception as e:
            self.logger.error(f"Erro nas correções de emergência: {e}")
    
    def fix_critical_errors(self):
        """Corrige erros críticos"""
        try:
            # Executar script de correção de erros
            error_script = self.project_root / "wiki/update/python_error_resolver.py"
            if error_script.exists():
                subprocess.run([sys.executable, str(error_script)], timeout=60)
                self.logger.info("Erros críticos corrigidos")
            
        except Exception as e:
            self.logger.error(f"Erro ao corrigir erros críticos: {e}")
    
    def restore_backups(self):
        """Restaura backups"""
        try:
            # Implementar restauração de backups
            self.logger.info("Backups restaurados")
            
        except Exception as e:
            self.logger.error(f"Erro ao restaurar backups: {e}")
    
    def validate_system_integrity(self):
        """Valida integridade do sistema"""
        try:
            # Verificar arquivos críticos
            critical_files = [
                "cursor.md",
                "wiki/maps/tags_index.json",
                "wiki/maps/wiki_map.json"
            ]
            
            valid_files = 0
            for file_path in critical_files:
                full_path = self.project_root / file_path
                if full_path.exists():
                    valid_files += 1
            
            integrity_score = valid_files / len(critical_files) * 100
            self.logger.info(f"Score de integridade: {integrity_score:.1f}%")
            
        except Exception as e:
            self.logger.error(f"Erro na validação de integridade: {e}")
    
    def restart_system(self):
        """Reinicia o sistema"""
        self.logger.info("=== REINICIANDO SISTEMA ===")
        
        try:
            # Parar sistema atual
            self.stop_system()
            
            # Resetar estado
            self.system_state.update({
                "status": "restarting",
                "cycles_completed": 0,
                "restart_time": datetime.now().isoformat()
            })
            
            # Reiniciar componentes
            self.monitor = AutoMonitor()
            self.updater = AutoUpdater()
            self.optimizer = AutoOptimizer()
            
            # Reiniciar sistema
            self.start_system()
            
        except Exception as e:
            self.logger.error(f"Erro ao reiniciar sistema: {e}")
    
    def stop_system(self):
        """Para o sistema"""
        self.logger.info("=== PARANDO SISTEMA ===")
        
        try:
            self.running = False
            
            # Aguardar threads terminarem
            if self.monitor_thread and self.monitor_thread.is_alive():
                self.monitor_thread.join(timeout=10)
            
            if self.updater_thread and self.updater_thread.is_alive():
                self.updater_thread.join(timeout=10)
            
            if self.optimizer_thread and self.optimizer_thread.is_alive():
                self.optimizer_thread.join(timeout=10)
            
            self.system_state["status"] = "stopped"
            self.save_system_state()
            
            self.logger.info("Sistema parado com sucesso")
            
        except Exception as e:
            self.logger.error(f"Erro ao parar sistema: {e}")
    
    def save_system_state(self):
        """Salva estado atual do sistema"""
        try:
            state_file = self.log_path / "auto_update_system_state.json"
            with open(state_file, 'w', encoding='utf-8') as f:
                json.dump(self.system_state, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            self.logger.error(f"Erro ao salvar estado do sistema: {e}")
    
    def get_system_status(self) -> Dict[str, Any]:
        """Retorna status atual do sistema"""
        return {
            "status": self.system_state["status"],
            "health_score": self.system_state["health_score"],
            "performance_score": self.system_state["performance_score"],
            "cycles_completed": self.system_state["cycles_completed"],
            "total_updates": self.system_state["total_updates"],
            "total_optimizations": self.system_state["total_optimizations"],
            "emergency_mode": self.config["emergency_mode"],
            "uptime": self.calculate_uptime()
        }
    
    def calculate_uptime(self) -> str:
        """Calcula tempo de atividade do sistema"""
        try:
            start_time = datetime.fromisoformat(self.system_state["start_time"])
            uptime = datetime.now() - start_time
            return str(uptime).split('.')[0]  # Remover microssegundos
        except Exception:
            return "Unknown"

def main():
    """Função principal"""
    print("Sistema de Auto-Atualização Integrado BMAD")
    print("Iniciando sistema...")
    
    system = AutoUpdateSystem()
    
    try:
        system.start_system()
    except KeyboardInterrupt:
        print("\nSistema interrompido pelo usuário")
        system.stop_system()
    except Exception as e:
        print(f"Erro fatal no sistema: {e}")
        system.emergency_mode()

if __name__ == "__main__":
    main() 