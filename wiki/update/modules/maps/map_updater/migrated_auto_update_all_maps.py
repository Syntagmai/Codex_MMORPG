from unicode_aliases import *
# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
MAX_ITEMS = 100
TIMEOUT_SECONDS = 60

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: auto_update_all_maps.py
Módulo de Destino: maps.map_updater
Data de Migração: 2025-08-01 12:21:34

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import MapupdaterModule

# Conteúdo original do script
#!/usr/bin/env python3
"""
Script principal para atualização automática de todos os mapas JSON
Executa todos os scripts de indexação na ordem estabelecida
Usa contexto detectado automaticamente
"""
import os
import sys
import json
import subprocess
import time
from datetime import datetime

class AutoMapUpdater:
    def __init__(self):
        self.project_root = Path(".")
        
        # Detectar contexto
        self.context_data = self.load_context_data()
        self.context = self.context_data['context']
        
        # Definir scripts baseados no contexto
        self.scripts_order = self.get_context_scripts()
        self.maps_to_validate = self.get_context_maps()
        
        self.report = {
            "timestamp": datetime.now().isoformat(),
            "context": self.context,
            "scripts_executed": [],
            "scripts_failed": [],
            "maps_validated": [],
            "maps_invalid": [],
            "total_files_indexed": 0,
            "performance_metrics": {},
            "errors": []
        }
    
    def load_context_data(self) -> Dict[str, Any]:
        """Carrega dados de contexto detectado"""
        context_file = self.project_root / "wiki/maps/context_data.json"
        if context_file.exists():
            with open(context_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Fallback para contexto OTClient
            return {
                'context': 'otclient',
                'paths': {
                    'docs': 'wiki/otclient/',
                    'maps': 'wiki/maps/'
                }
            }
    
    def get_context_scripts(self) -> List[str]:
        """Retorna scripts baseados no contexto"""
        if self.context == "otclient":
            return [
                "wiki/update/update_source_index.py",
                "wiki/update/update_habdel_index.py",
                "wiki/update/update_modules_index.py",
                "wiki/update/update_styles_index.py",
                "wiki/update/update_resources_index.py",
                "wiki/update/update_tools_index.py",
                "wiki/update/update_wiki_maps.py",
                "wiki/update/update_bmad_maps.py",
                "wiki/update/optimize_maps_for_tokens.py",
                "wiki/update/expand_wiki_comprehensive.py"
            ]
        elif self.context == "canary":
            return [
                "wiki/update/update_canary_source_index.py",
                "wiki/update/update_canary_wiki_maps.py",
                "wiki/update/update_integration_maps.py",
                "wiki/update/optimize_maps_for_tokens.py"
            ]
        elif self.context == "unified":
            return [
                "wiki/update/update_unified_source_index.py",
                "wiki/update/update_unified_wiki_maps.py",
                "wiki/update/update_integration_maps.py",
                "wiki/update/update_cross_project_maps.py",
                "wiki/update/optimize_maps_for_tokens.py"
            ]
        else:
            # Fallback para OTClient
            return [
                "wiki/update/update_source_index.py",
                "wiki/update/update_wiki_maps.py",
                "wiki/update/optimize_maps_for_tokens.py"
            ]
    
    def get_context_maps(self) -> List[str]:
        """Retorna mapas baseados no contexto"""
        base_maps = [
            "wiki/maps/tags_index.json",
            "wiki/maps/wiki_map.json",
            "wiki/maps/relationships.json"
        ]
        
        if self.context == "otclient":
            return [
                "wiki/maps/otclient_source_index.json",
                "wiki/maps/habdel_index.json",
                "wiki/maps/modules_index.json",
                "wiki/maps/styles_index.json",
                "wiki/maps/resources_index.json",
                "wiki/maps/tools_index.json"
            ] + base_maps
        elif self.context == "canary":
            return [
                "wiki/maps/canary_source_index.json",
                "wiki/maps/canary_wiki_map.json"
            ] + base_maps
        elif self.context == "unified":
            return [
                "wiki/maps/unified_source_index.json",
                "wiki/maps/unified_wiki_map.json",
                "wiki/maps/integration_map.json",
                "wiki/maps/cross_project_relationships.json"
            ] + base_maps
        else:
            return base_maps

    def log(self, message: str, level: str = "INFO"):
        """Log com timestamp"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {level}: {message}")
    
    def execute_script(self, script_path: str) -> bool:
        """Executa um script específico"""
        if not os.path.exists(script_path):
            self.log(f"Script {script_path} não encontrado, pulando...", "WARN")
            return False
        
        try:
            start_time = time.time()
            result = subprocess.run([sys.executable, script_path], 
                                  capture_output=True, text=True, cwd=self.project_root)
            end_time = time.time()
            
            execution_time = end_time - start_time
            
            if result.returncode == 0:
                self.log(f"{script_path} executado com sucesso ({execution_time:.2f}s)")
                self.report["scripts_executed"].append({
                    "script": script_path,
                    "execution_time": execution_time,
                    "status": "success"
                })
                return True
            else:
                self.log(f"Erro ao executar {script_path}: {result.stderr}", "ERROR")
                self.report["scripts_failed"].append({
                    "script": script_path,
                    "error": result.stderr,
                    "status": "failed"
                })
                return False
                
        except Exception as e:
            self.log(f"Exceção ao executar {script_path}: {e}", "ERROR")
            self.report["scripts_failed"].append({
                "script": script_path,
                "error": str(e),
                "status": "exception"
            })
            return False
    
    def validate_map(self, map_path: str) -> bool:
        """Valida um mapa JSON"""
        try:
            with open(map_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Validações básicas
            if not isinstance(data, dict):
                return False
            
            if "metadata" not in data:
                return False
            
            self.log(f"{map_path} válido")
            self.report["maps_validated"].append(map_path)
            return True
            
        except Exception as e:
            self.log(f"{map_path} inválido: {e}", "ERROR")
            self.report["maps_invalid"].append({
                "map": map_path,
                "error": str(e)
            })
            return False
    
    def update_all_maps(self):
        """Executa atualização de todos os mapas"""
        self.log(f"Iniciando atualização automática de todos os mapas ({self.context.upper()})...")
        
        # Executar scripts na ordem definida
        for script in self.scripts_order:
            self.execute_script(script)
        
        # Validar integridade dos mapas
        self.log("Validando integridade dos mapas...")
        for map_path in self.maps_to_validate:
            if os.path.exists(map_path):
                self.validate_map(map_path)
            else:
                self.log(f"Mapa {map_path} não encontrado", "WARN")
        
        # Gerar relatório
        self.generate_report()
        
        # Salvar relatório
        self.save_report()

    def generate_report(self):
        """Gera relatório de atualização"""
        total_scripts = len(self.report["scripts_executed"]) + len(self.report["scripts_failed"])
        success_rate = (len(self.report["scripts_executed"]) / total_scripts * 100) if total_scripts > 0 else 0
        
        self.log("Relatório de Atualização:")
        self.log(f"  Scripts executados: {len(self.report['scripts_executed'])}/{total_scripts}")
        self.log(f"  Mapas válidos: {len(self.report['maps_validated'])}")
        self.log(f"  Taxa de sucesso: {success_rate:.1f}%")
        
        # Calcular total de arquivos indexados
        total_files = 0
        for map_path in self.report["maps_validated"]:
            try:
                with open(map_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if "metadata" in data and "total_files" in data["metadata"]:
                        total_files += data["metadata"]["total_files"]
            except:
                pass
        
        self.report["total_files_indexed"] = total_files
        self.log(f"  Arquivos indexados: {total_files}")
    
    def save_report(self, report_path: str = "wiki/maps/maps_update_report.json"):
        """Salva relatório de atualização"""
        try:
            with open(report_path, 'w', encoding='utf-8') as f:
                json.dump(self.report, f, indent=2, ensure_ascii=False)
            self.log(f"Relatório salvo em {report_path}")
        except Exception as e:
            self.log(f"Erro ao salvar relatório: {e}", "ERROR")
    
    def print_summary(self):
        """Imprime resumo da atualização"""
        total_scripts = len(self.scripts_order)
        executed_scripts = len(self.report["scripts_executed"])
        failed_scripts = len(self.report["scripts_failed"])
        success_rate = (executed_scripts / total_scripts * 100) if total_scripts > 0 else 0
        
        print("\n" + "=" * 60)
        print(" RESUMO DA ATUALIZAÇÃO DE MAPAS")
        print("=" * 60)
        print(f" Contexto: {self.context.upper()}")
        print(f" Scripts executados: {executed_scripts}")
        print(f" Scripts falharam: {failed_scripts}")
        print(f" Taxa de sucesso: {success_rate:.1f}%")
        print(f" Mapas válidos: {len(self.report['maps_validated'])}")
        print(f" Mapas inválidos: {len(self.report['maps_invalid'])}")
        print(f" Arquivos indexados: {self.report['total_files_indexed']}")
        print(f" Tempo total: {sum(s['execution_time'] for s in self.report['scripts_executed']):.2f}s")
        print(f" Tempo médio por script: {sum(s['execution_time'] for s in self.report['scripts_executed']) / executed_scripts:.2f}s" if executed_scripts > 0 else " Tempo médio por script: N/A")
        print("=" * 60)
        print("\n Atualização de mapas concluída com sucesso!\n")

if __name__ == "__main__":
    updater = AutoMapUpdater()
    updater.update_all_maps()
    updater.print_summary()

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = MapupdaterModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script auto_update_all_maps.py executado com sucesso via módulo maps.map_updater")
    else:
        print(f"❌ Erro na execução do script auto_update_all_maps.py via módulo maps.map_updater")
