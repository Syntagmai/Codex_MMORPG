# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
MAX_ITEMS = 100
TIMEOUT_SECONDS = 60

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: auto_monitor.py
Módulo de Destino: agents.agent_monitor
Data de Migração: 2025-08-01 12:21:34

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import AgentmonitorModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Auto-Monitoramento Contínuo BMAD
Monitora continuamente o estado do sistema e dispara ações automáticas
"""

import json
import time
import os
import subprocess
import sys
from datetime import datetime, timedelta
import threading
import logging

class AutoMonitor:
    def __init__(self):
        self.project_root = Path(".")
        self.log_path = self.project_root / "wiki/log"
        self.maps_path = self.project_root / "wiki/maps"
        self.update_path = self.project_root / "wiki/update"
        self.rules_path = self.project_root / ".cursor/rules"
        
        # Configurações de monitoramento
        self.monitoring_interval = 300  # 5 minutos
        self.health_threshold = 90      # Score mínimo
        self.error_threshold = 5        # Máximo de erros
        self.performance_threshold = 85 # Score mínimo de performance
        
        # Estado do sistema
        self.system_state = {
            "last_check": None,
            "health_score": 100,
            "error_count": 0,
            "performance_score": 100,
            "changes_detected": [],
            "optimizations_needed": []
        }
        
        # Configurar logging
        self.setup_logging()
        
        # Cache de arquivos para detecção de mudanças
        self.file_cache = {}
        self.last_scan_time = None
        
    def setup_logging(self):
        """Configura sistema de logging"""
        log_file = self.log_path / "auto_monitor.log"
        log_file.parent.mkdir(parents=True, exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def start_monitoring(self):
        """Inicia monitoramento contínuo"""
        self.logger.info("Iniciando sistema de auto-monitoramento BMAD")
        self.logger.info(f"Intervalo de monitoramento: {self.monitoring_interval} segundos")
        
        try:
            while True:
                self.logger.info("=== CICLO DE MONITORAMENTO ===")
                
                # Executar verificações
                self.check_system_health()
                self.detect_changes()
                self.analyze_performance()
                
                # Verificar se ações são necessárias
                self.check_and_trigger_actions()
                
                # Salvar estado atual
                self.save_system_state()
                
                # Aguardar próximo ciclo
                self.logger.info(f"Aguardando {self.monitoring_interval} segundos...")
                time.sleep(self.monitoring_interval)
                
        except KeyboardInterrupt:
            self.logger.info("Monitoramento interrompido pelo usuário")
        except Exception as e:
            self.logger.error(f"Erro no monitoramento: {e}")
            self.trigger_emergency_mode()
    
    def check_system_health(self):
        """Verifica saúde geral do sistema"""
        self.logger.info("Verificando saúde do sistema...")
        
        health_checks = {
            "maps_integrity": self.check_maps_integrity(),
            "rules_consistency": self.check_rules_consistency(),
            "scripts_functionality": self.check_scripts_functionality(),
            "file_permissions": self.check_file_permissions(),
            "json_validity": self.check_json_validity()
        }
        
        # Calcular score de saúde
        health_score = sum(health_checks.values()) / len(health_checks) * 100
        self.system_state["health_score"] = health_score
        
        self.logger.info(f"Score de saúde: {health_score:.1f}/100")
        
        if health_score < self.health_threshold:
            self.logger.warning(f"Saúde do sistema abaixo do threshold ({self.health_threshold})")
            self.system_state["optimizations_needed"].append("health_improvement")
    
    def check_maps_integrity(self) -> float:
        """Verifica integridade dos mapas JSON"""
        try:
            maps_to_check = [
                "tags_index.json",
                "wiki_map.json",
                "enhanced_context_system.json",
                "intelligent_navigation.json"
            ]
            
            valid_maps = 0
            for map_file in maps_to_check:
                map_path = self.maps_path / map_file
                if map_path.exists():
                    try:
                        with open(map_path, 'r', encoding='utf-8') as f:
                            json.load(f)
                        valid_maps += 1
                    except Exception as e:
                        self.logger.error(f"Erro no mapa {map_file}: {e}")
                else:
                    self.logger.warning(f"Mapa não encontrado: {map_file}")
            
            return valid_maps / len(maps_to_check)
            
        except Exception as e:
            self.logger.error(f"Erro ao verificar mapas: {e}")
            return 0.0
    
    def check_rules_consistency(self) -> float:
        """Verifica consistência das regras"""
        try:
            rules_to_check = [
                "rules.md",
                "performance-rules.md",
                "context-aware-rules.md",
                "python-agent-rules.md"
            ]
            
            valid_rules = 0
            for rule_file in rules_to_check:
                rule_path = self.rules_path / rule_file
                if rule_path.exists():
                    # Verificar se arquivo não está vazio
                    if rule_path.stat().st_size > 100:
                        valid_rules += 1
                    else:
                        self.logger.warning(f"Regra muito pequena: {rule_file}")
                else:
                    self.logger.warning(f"Regra não encontrada: {rule_file}")
            
            return valid_rules / len(rules_to_check)
            
        except Exception as e:
            self.logger.error(f"Erro ao verificar regras: {e}")
            return 0.0
    
    def check_scripts_functionality(self) -> float:
        """Verifica funcionalidade dos scripts Python"""
        try:
            scripts_to_check = [
                "python_error_resolver.py",
                "script_execution_manager.py",
                "analyze_navigation_optimization.py"
            ]
            
            valid_scripts = 0
            for script_file in scripts_to_check:
                script_path = self.update_path / script_file
                if script_path.exists():
                    # Verificar sintaxe Python
                    try:
                        result = subprocess.run(
                            [sys.executable, "-m", "py_compile", str(script_path)],
                            capture_output=True,
                            text=True,
                            timeout=10
                        )
                        if result.returncode == 0:
                            valid_scripts += 1
                        else:
                            self.logger.error(f"Erro de sintaxe em {script_file}")
                    except Exception as e:
                        self.logger.error(f"Erro ao verificar {script_file}: {e}")
                else:
                    self.logger.warning(f"Script não encontrado: {script_file}")
            
            return valid_scripts / len(scripts_to_check)
            
        except Exception as e:
            self.logger.error(f"Erro ao verificar scripts: {e}")
            return 0.0
    
    def check_file_permissions(self) -> float:
        """Verifica permissões de arquivos"""
        try:
            critical_paths = [
                self.maps_path,
                self.log_path,
                self.update_path,
                self.rules_path
            ]
            
            accessible_paths = 0
            for path in critical_paths:
                if path.exists() and os.access(path, os.R_OK | os.W_OK):
                    accessible_paths += 1
                else:
                    self.logger.warning(f"Problema de permissão em: {path}")
            
            return accessible_paths / len(critical_paths)
            
        except Exception as e:
            self.logger.error(f"Erro ao verificar permissões: {e}")
            return 0.0
    
    def check_json_validity(self) -> float:
        """Verifica validade de arquivos JSON"""
        try:
            json_files = list(self.maps_path.glob("*.json"))
            
            valid_jsons = 0
            for json_file in json_files:
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        json.load(f)
                    valid_jsons += 1
                except Exception as e:
                    self.logger.error(f"JSON inválido em {json_file.name}: {e}")
            
            return valid_jsons / len(json_files) if json_files else 1.0
            
        except Exception as e:
            self.logger.error(f"Erro ao verificar JSONs: {e}")
            return 0.0
    
    def detect_changes(self):
        """Detecta mudanças no sistema"""
        self.logger.info("Detectando mudanças no sistema...")
        
        current_time = datetime.now()
        changes = []
        
        # Verificar arquivos modificados
        for path in [self.maps_path, self.update_path, self.rules_path]:
            for file_path in path.rglob("*"):
                if file_path.is_file():
                    file_key = str(file_path)
                    current_mtime = file_path.stat().st_mtime
                    
                    if file_key in self.file_cache:
                        if current_mtime > self.file_cache[file_key]:
                            changes.append({
                                "type": "modified",
                                "file": file_key,
                                "timestamp": current_time
                            })
                    else:
                        changes.append({
                            "type": "new",
                            "file": file_key,
                            "timestamp": current_time
                        })
                    
                    self.file_cache[file_key] = current_mtime
        
        self.system_state["changes_detected"] = changes
        self.last_scan_time = current_time
        
        if changes:
            self.logger.info(f"Detectadas {len(changes)} mudanças")
            for change in changes:
                self.logger.info(f"  - {change['type']}: {change['file']}")
        else:
            self.logger.info("Nenhuma mudança detectada")
    
    def analyze_performance(self):
        """Analisa performance do sistema"""
        self.logger.info("Analisando performance do sistema...")
        
        performance_metrics = {
            "response_time": self.measure_response_time(),
            "memory_usage": self.measure_memory_usage(),
            "file_access_speed": self.measure_file_access_speed(),
            "script_execution_time": self.measure_script_execution_time()
        }
        
        # Calcular score de performance
        performance_score = sum(performance_metrics.values()) / len(performance_metrics) * 100
        self.system_state["performance_score"] = performance_score
        
        self.logger.info(f"Score de performance: {performance_score:.1f}/100")
        
        if performance_score < self.performance_threshold:
            self.logger.warning(f"Performance abaixo do threshold ({self.performance_threshold})")
            self.system_state["optimizations_needed"].append("performance_improvement")
    
    def measure_response_time(self) -> float:
        """Mede tempo de resposta do sistema"""
        try:
            start_time = time.time()
            
            # Simular operação típica
            self.maps_path.exists()
            list(self.maps_path.glob("*.json"))
            
            response_time = time.time() - start_time
            
            # Normalizar (0-1, onde 1 é melhor)
            if response_time < 0.1:
                return 1.0
            elif response_time < 1.0:
                return 0.8
            elif response_time < 5.0:
                return 0.5
            else:
                return 0.2
                
        except Exception as e:
            self.logger.error(f"Erro ao medir tempo de resposta: {e}")
            return 0.0
    
    def measure_memory_usage(self) -> float:
        """Mede uso de memória"""
        try:
            import psutil
            memory_percent = psutil.virtual_memory().percent
            
            # Normalizar (0-1, onde 1 é melhor)
            if memory_percent < 50:
                return 1.0
            elif memory_percent < 70:
                return 0.8
            elif memory_percent < 85:
                return 0.5
            else:
                return 0.2
                
        except ImportError:
            self.logger.warning("psutil não disponível, usando estimativa")
            return 0.8
        except Exception as e:
            self.logger.error(f"Erro ao medir memória: {e}")
            return 0.5
    
    def measure_file_access_speed(self) -> float:
        """Mede velocidade de acesso a arquivos"""
        try:
            start_time = time.time()
            
            # Testar acesso a arquivos críticos
            test_files = [
                self.maps_path / "tags_index.json",
                self.maps_path / "wiki_map.json",
                self.rules_path / "rules.md"
            ]
            
            for test_file in test_files:
                if test_file.exists():
                    with open(test_file, 'r', encoding='utf-8') as f:
                        f.read(1024)  # Ler 1KB
            
            access_time = time.time() - start_time
            
            # Normalizar (0-1, onde 1 é melhor)
            if access_time < 0.01:
                return 1.0
            elif access_time < 0.1:
                return 0.8
            elif access_time < 1.0:
                return 0.5
            else:
                return 0.2
                
        except Exception as e:
            self.logger.error(f"Erro ao medir acesso a arquivos: {e}")
            return 0.0
    
    def measure_script_execution_time(self) -> float:
        """Mede tempo de execução de scripts"""
        try:
            start_time = time.time()
            
            # Testar execução de script simples
            test_script = self.update_path / "analyze_navigation_optimization.py"
            if test_script.exists():
                result = subprocess.run(
                    [sys.executable, str(test_script)],
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                
                execution_time = time.time() - start_time
                
                # Normalizar (0-1, onde 1 é melhor)
                if execution_time < 5:
                    return 1.0
                elif execution_time < 15:
                    return 0.8
                elif execution_time < 30:
                    return 0.5
                else:
                    return 0.2
            else:
                return 0.5
                
        except Exception as e:
            self.logger.error(f"Erro ao medir execução de scripts: {e}")
            return 0.0
    
    def check_and_trigger_actions(self):
        """Verifica se ações automáticas são necessárias"""
        self.logger.info("Verificando necessidade de ações automáticas...")
        
        actions_triggered = []
        
        # Verificar se correção de saúde é necessária
        if self.system_state["health_score"] < self.health_threshold:
            self.logger.info("Disparando correção de saúde...")
            self.trigger_health_correction()
            actions_triggered.append("health_correction")
        
        # Verificar se otimização de performance é necessária
        if self.system_state["performance_score"] < self.performance_threshold:
            self.logger.info("Disparando otimização de performance...")
            self.trigger_performance_optimization()
            actions_triggered.append("performance_optimization")
        
        # Verificar se atualização é necessária
        if self.system_state["changes_detected"]:
            self.logger.info("Disparando atualização automática...")
            self.trigger_auto_update()
            actions_triggered.append("auto_update")
        
        if actions_triggered:
            self.logger.info(f"Ações disparadas: {', '.join(actions_triggered)}")
        else:
            self.logger.info("Nenhuma ação necessária")
    
    def trigger_health_correction(self):
        """Dispara correção de saúde do sistema"""
        try:
            # Executar script de correção
            correction_script = self.update_path / "python_error_resolver.py"
            if correction_script.exists():
                subprocess.run([sys.executable, str(correction_script)], timeout=60)
                self.logger.info("Correção de saúde executada")
        except Exception as e:
            self.logger.error(f"Erro na correção de saúde: {e}")
    
    def trigger_performance_optimization(self):
        """Dispara otimização de performance"""
        try:
            # Executar script de otimização
            optimization_script = self.update_path / "analyze_navigation_optimization.py"
            if optimization_script.exists():
                subprocess.run([sys.executable, str(optimization_script)], timeout=60)
                self.logger.info("Otimização de performance executada")
        except Exception as e:
            self.logger.error(f"Erro na otimização de performance: {e}")
    
    def trigger_auto_update(self):
        """Dispara atualização automática"""
        try:
            # Executar script de atualização
            update_script = self.update_path / "auto_update_all_maps.py"
            if update_script.exists():
                subprocess.run([sys.executable, str(update_script)], timeout=60)
                self.logger.info("Atualização automática executada")
        except Exception as e:
            self.logger.error(f"Erro na atualização automática: {e}")
    
    def trigger_emergency_mode(self):
        """Ativa modo de emergência"""
        self.logger.error("ATIVANDO MODO DE EMERGÊNCIA")
        
        # Salvar estado de emergência
        emergency_state = {
            "timestamp": datetime.now().isoformat(),
            "status": "emergency",
            "system_state": self.system_state,
            "error": "Monitoramento interrompido"
        }
        
        emergency_file = self.log_path / "emergency_state.json"
        with open(emergency_file, 'w', encoding='utf-8') as f:
            json.dump(emergency_state, f, indent=2, ensure_ascii=False)
    
    def save_system_state(self):
        """Salva estado atual do sistema"""
        try:
            self.system_state["last_check"] = datetime.now().isoformat()
            
            state_file = self.log_path / "auto_monitor_state.json"
            with open(state_file, 'w', encoding='utf-8') as f:
                json.dump(self.system_state, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            self.logger.error(f"Erro ao salvar estado: {e}")
    
    def get_system_status(self) -> Dict[str, Any]:
        """Retorna status atual do sistema"""
        return {
            "status": "monitoring",
            "health_score": self.system_state["health_score"],
            "performance_score": self.system_state["performance_score"],
            "last_check": self.system_state["last_check"],
            "changes_detected": len(self.system_state["changes_detected"]),
            "optimizations_needed": self.system_state["optimizations_needed"]
        }

def main():
    """Função principal"""
    print("Sistema de Auto-Monitoramento BMAD")
    print("Iniciando monitoramento contínuo...")
    
    monitor = AutoMonitor()
    
    # Iniciar monitoramento em thread separada
    monitor_thread = threading.Thread(target=monitor.start_monitoring, daemon=True)
    monitor_thread.start()
    
    try:
        # Loop principal para exibir status
        while True:
            status = monitor.get_system_status()
            print(f"\nStatus do Sistema:")
            print(f"  Saúde: {status['health_score']:.1f}/100")
            print(f"  Performance: {status['performance_score']:.1f}/100")
            print(f"  Mudanças: {status['changes_detected']}")
            print(f"  Última verificação: {status['last_check']}")
            
            time.sleep(60)  # Atualizar status a cada minuto
            
    except KeyboardInterrupt:
        print("\nMonitoramento interrompido")

if __name__ == "__main__":
    main() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = AgentmonitorModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script auto_monitor.py executado com sucesso via módulo agents.agent_monitor")
    else:
        print(f"❌ Erro na execução do script auto_monitor.py via módulo agents.agent_monitor")
