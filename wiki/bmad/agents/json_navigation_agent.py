#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agente Especializado em Navegação JSON
Integra com sistema Python para navegação fluida e atualizada
"""

import json
import os
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import subprocess
import sys

class JSONNavigationAgent:
    """Agente especializado em navegação JSON para integração fluida"""
    
    def __init__(self):
        self.project_root = Path(".")
        self.maps_path = self.project_root / "wiki" / "maps"
        self.rules_path = self.project_root / ".cursor" / "rules"
        self.update_path = self.project_root / "wiki" / "update"
        
        # Mapas principais de navegação
        self.navigation_maps = {
            "tags_index": self.maps_path / "tags_index.json",
            "wiki_map": self.maps_path / "wiki_map.json",
            "relationships": self.maps_path / "relationships.json",
            "enhanced_context": self.maps_path / "enhanced_context_system.json",
            "intelligent_navigation": self.maps_path / "intelligent_navigation.json",
            "otclient_source": self.maps_path / "otclient_source_index.json"
        }
        
        # Scripts de atualização
        self.update_scripts = {
            "all_maps": self.update_path / "auto_update_all_maps.py",
            "wiki_maps": self.update_path / "update_wiki_maps.py",
            "source_index": self.update_path / "update_source_index.py",
            "context_system": self.update_path / "update_context_system.py"
        }
        
        self.last_update_check = {}
        self.update_interval = 300  # 5 minutos
        
    def check_navigation_sync(self) -> Dict[str, Any]:
        """Verifica sincronização da navegação"""
        print("🔍 Verificando sincronização da navegação...")
        
        sync_status = {
            "timestamp": datetime.now().isoformat(),
            "maps_status": {},
            "scripts_status": {},
            "overall_sync": True,
            "issues": [],
            "recommendations": []
        }
        
        # Verificar mapas JSON
        for map_name, map_path in self.navigation_maps.items():
            status = self.check_map_status(map_path)
            sync_status["maps_status"][map_name] = status
            
            if not status["exists"]:
                sync_status["overall_sync"] = False
                sync_status["issues"].append(f"Mapa {map_name} não encontrado")
            elif not status["valid"]:
                sync_status["overall_sync"] = False
                sync_status["issues"].append(f"Mapa {map_name} inválido")
            elif status["needs_update"]:
                sync_status["recommendations"].append(f"Atualizar {map_name}")
        
        # Verificar scripts de atualização
        for script_name, script_path in self.update_scripts.items():
            status = self.check_script_status(script_path)
            sync_status["scripts_status"][script_name] = status
            
            if not status["exists"]:
                sync_status["overall_sync"] = False
                sync_status["issues"].append(f"Script {script_name} não encontrado")
            elif not status["executable"]:
                sync_status["issues"].append(f"Script {script_name} não executável")
        
        return sync_status
    
    def check_map_status(self, map_path: Path) -> Dict[str, Any]:
        """Verifica status de um mapa JSON"""
        status = {
            "exists": map_path.exists(),
            "valid": False,
            "needs_update": False,
            "last_updated": None,
            "size": 0,
            "error": None
        }
        
        if not status["exists"]:
            return status
        
        try:
            status["size"] = map_path.stat().st_size
            
            with open(map_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Verificar estrutura básica
            if "metadata" in data and "last_updated" in data["metadata"]:
                status["last_updated"] = data["metadata"]["last_updated"]
                status["valid"] = True
                
                # Verificar se precisa atualizar
                if status["last_updated"]:
                    last_update = datetime.fromisoformat(status["last_updated"].replace('Z', '+00:00'))
                    time_diff = (datetime.now() - last_update).total_seconds()
                    status["needs_update"] = time_diff > self.update_interval
            else:
                status["error"] = "Estrutura inválida - sem metadata"
                
        except Exception as e:
            status["error"] = str(e)
            status["valid"] = False
        
        return status
    
    def check_script_status(self, script_path: Path) -> Dict[str, Any]:
        """Verifica status de um script Python"""
        status = {
            "exists": script_path.exists(),
            "executable": False,
            "size": 0,
            "error": None
        }
        
        if not status["exists"]:
            return status
        
        try:
            status["size"] = script_path.stat().st_size
            
            # Verificar se é executável
            if script_path.suffix == '.py':
                status["executable"] = True
                
                # Verificar sintaxe básica
                try:
                    with open(script_path, 'r', encoding='utf-8') as f:
                        compile(f.read(), script_path, 'exec')
                except SyntaxError as e:
                    status["error"] = f"Erro de sintaxe: {e}"
                    status["executable"] = False
                    
        except Exception as e:
            status["error"] = str(e)
        
        return status
    
    def update_navigation_maps(self, force: bool = False) -> Dict[str, Any]:
        """Atualiza mapas de navegação"""
        print("🔄 Atualizando mapas de navegação...")
        
        update_result = {
            "timestamp": datetime.now().isoformat(),
            "scripts_executed": [],
            "scripts_failed": [],
            "maps_updated": [],
            "errors": []
        }
        
        # Verificar se precisa atualizar
        if not force:
            sync_status = self.check_navigation_sync()
            if sync_status["overall_sync"] and not sync_status["recommendations"]:
                print("✅ Navegação já está sincronizada")
                return update_result
        
        # Executar scripts de atualização
        for script_name, script_path in self.update_scripts.items():
            if script_path.exists() and script_path.suffix == '.py':
                try:
                    print(f"📝 Executando {script_name}...")
                    result = subprocess.run(
                        [sys.executable, str(script_path)],
                        capture_output=True,
                        text=True,
                        cwd=self.project_root,
                        timeout=60
                    )
                    
                    if result.returncode == 0:
                        update_result["scripts_executed"].append({
                            "script": script_name,
                            "output": result.stdout,
                            "execution_time": "completed"
                        })
                        print(f"✅ {script_name} executado com sucesso")
                    else:
                        update_result["scripts_failed"].append({
                            "script": script_name,
                            "error": result.stderr,
                            "return_code": result.returncode
                        })
                        update_result["errors"].append(f"Script {script_name} falhou")
                        print(f"❌ {script_name} falhou: {result.stderr}")
                        
                except subprocess.TimeoutExpired:
                    update_result["scripts_failed"].append({
                        "script": script_name,
                        "error": "Timeout",
                        "return_code": -1
                    })
                    update_result["errors"].append(f"Script {script_name} timeout")
                    print(f"⏰ {script_name} timeout")
                    
                except Exception as e:
                    update_result["scripts_failed"].append({
                        "script": script_name,
                        "error": str(e),
                        "return_code": -1
                    })
                    update_result["errors"].append(f"Erro ao executar {script_name}: {e}")
                    print(f"❌ Erro ao executar {script_name}: {e}")
        
        # Verificar mapas atualizados
        for map_name, map_path in self.navigation_maps.items():
            if map_path.exists():
                try:
                    with open(map_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    if "metadata" in data and "last_updated" in data["metadata"]:
                        update_result["maps_updated"].append({
                            "map": map_name,
                            "last_updated": data["metadata"]["last_updated"],
                            "size": map_path.stat().st_size
                        })
                except Exception as e:
                    update_result["errors"].append(f"Erro ao verificar {map_name}: {e}")
        
        return update_result
    
    def optimize_navigation_performance(self) -> Dict[str, Any]:
        """Otimiza performance da navegação"""
        print("⚡ Otimizando performance da navegação...")
        
        optimization_result = {
            "timestamp": datetime.now().isoformat(),
            "optimizations_applied": [],
            "performance_improvements": [],
            "cache_optimizations": [],
            "errors": []
        }
        
        # Otimizar cache de navegação
        try:
            # Criar cache de navegação rápida
            cache_data = {}
            
            for map_name, map_path in self.navigation_maps.items():
                if map_path.exists():
                    try:
                        with open(map_path, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                        
                        # Extrair dados essenciais para cache
                        cache_data[map_name] = {
                            "last_updated": data.get("metadata", {}).get("last_updated"),
                            "total_files": data.get("metadata", {}).get("total_files", 0),
                            "quick_access": self.extract_quick_access_data(data)
                        }
                        
                    except Exception as e:
                        optimization_result["errors"].append(f"Erro ao processar {map_name}: {e}")
            
            # Salvar cache otimizado
            cache_file = self.maps_path / "navigation_cache.json"
            with open(cache_file, 'w', encoding='utf-8') as f:
                json.dump(cache_data, f, indent=2, ensure_ascii=False)
            
            optimization_result["cache_optimizations"].append("Cache de navegação criado")
            print("✅ Cache de navegação otimizado")
            
        except Exception as e:
            optimization_result["errors"].append(f"Erro ao otimizar cache: {e}")
        
        return optimization_result
    
    def extract_quick_access_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Extrai dados para acesso rápido"""
        quick_access = {}
        
        # Extrair dados do tags_index
        if "files_by_tag" in data:
            quick_access["popular_tags"] = sorted(
                data["files_by_tag"].keys(),
                key=lambda x: len(data["files_by_tag"][x]),
                reverse=True
            )[:10]
        
        # Extrair dados do wiki_map
        if "categories" in data:
            quick_access["categories"] = list(data["categories"].keys())
        
        # Extrair dados de relationships
        if "relationships" in data:
            quick_access["relationship_count"] = len(data["relationships"])
        
        return quick_access
    
    def validate_navigation_integrity(self) -> Dict[str, Any]:
        """Valida integridade da navegação"""
        print("🔍 Validando integridade da navegação...")
        
        integrity_result = {
            "timestamp": datetime.now().isoformat(),
            "validation_passed": True,
            "issues": [],
            "warnings": [],
            "recommendations": []
        }
        
        # Validar consistência entre mapas
        try:
            # Verificar se arquivos referenciados existem
            tags_data = self.load_map_data("tags_index")
            wiki_map_data = self.load_map_data("wiki_map")
            
            if tags_data and wiki_map_data:
                # Verificar consistência de arquivos
                tags_files = set()
                for files in tags_data.get("files_by_tag", {}).values():
                    tags_files.update(files)
                
                wiki_files = set(wiki_map_data.get("files", {}).keys())
                
                # Verificar arquivos que estão em tags mas não na wiki
                missing_in_wiki = tags_files - wiki_files
                if missing_in_wiki:
                    integrity_result["warnings"].append(f"Arquivos em tags mas não na wiki: {missing_in_wiki}")
                
                # Verificar arquivos que estão na wiki mas não em tags
                missing_in_tags = wiki_files - tags_files
                if missing_in_tags:
                    integrity_result["warnings"].append(f"Arquivos na wiki mas não em tags: {missing_in_tags}")
                
                # Verificar se arquivos físicos existem
                for file_name in tags_files:
                    file_path = self.project_root / "wiki" / "otclient" / file_name
                    if not file_path.exists():
                        integrity_result["issues"].append(f"Arquivo não encontrado: {file_name}")
                        integrity_result["validation_passed"] = False
                
        except Exception as e:
            integrity_result["issues"].append(f"Erro na validação: {e}")
            integrity_result["validation_passed"] = False
        
        return integrity_result
    
    def load_map_data(self, map_name: str) -> Optional[Dict[str, Any]]:
        """Carrega dados de um mapa"""
        map_path = self.navigation_maps.get(map_name)
        if not map_path or not map_path.exists():
            return None
        
        try:
            with open(map_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return None
    
    def get_navigation_report(self) -> Dict[str, Any]:
        """Gera relatório completo da navegação"""
        print("📊 Gerando relatório de navegação...")
        
        # Verificar sincronização
        sync_status = self.check_navigation_sync()
        
        # Validar integridade
        integrity_status = self.validate_navigation_integrity()
        
        # Otimizar performance
        optimization_status = self.optimize_navigation_performance()
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "navigation_status": {
                "synchronized": sync_status["overall_sync"],
                "integrity_valid": integrity_status["validation_passed"],
                "performance_optimized": len(optimization_status["cache_optimizations"]) > 0
            },
            "sync_status": sync_status,
            "integrity_status": integrity_status,
            "optimization_status": optimization_status,
            "recommendations": []
        }
        
        # Gerar recomendações
        if not sync_status["overall_sync"]:
            report["recommendations"].append("Executar atualização de mapas")
        
        if not integrity_status["validation_passed"]:
            report["recommendations"].append("Corrigir problemas de integridade")
        
        if integrity_status["warnings"]:
            report["recommendations"].append("Revisar inconsistências entre mapas")
        
        return report

def main():
    """Função principal para execução do agente"""
    agent = JSONNavigationAgent()
    
    print("🚀 Agente de Navegação JSON iniciado")
    print("=" * 50)
    
    # Gerar relatório completo
    report = agent.get_navigation_report()
    
    # Salvar relatório
    report_file = agent.maps_path / "json_navigation_report.json"
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print("📊 Relatório salvo em: wiki/maps/json_navigation_report.json")
    
    # Mostrar resumo
    print("\n📋 RESUMO:")
    print(f"  Sincronização: {'✅' if report['navigation_status']['synchronized'] else '❌'}")
    print(f"  Integridade: {'✅' if report['navigation_status']['integrity_valid'] else '❌'}")
    print(f"  Performance: {'✅' if report['navigation_status']['performance_optimized'] else '❌'}")
    
    if report["recommendations"]:
        print("\n💡 RECOMENDAÇÕES:")
        for rec in report["recommendations"]:
            print(f"  - {rec}")

if __name__ == "__main__":
    main() 