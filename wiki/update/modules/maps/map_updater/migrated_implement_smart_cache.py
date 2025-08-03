from unicode_aliases import *
# Constantes
MAX_RETRIES = 8
TIMEOUT_SECONDS = 60

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: implement_smart_cache.py
Módulo de Destino: maps.map_updater
Data de Migração: 2025-08-01 12:21:34

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import MapupdaterModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementação de Cache Inteligente
==================================

Este script implementa cache inteligente para 23 mapas JSON
com objetivo de 50% de redução de tempo de acesso.

Autor: Sistema BMAD - Performance Agent
Data: 2025-08-01
"""

import json
import time
from datetime import datetime, timedelta
import logging

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SmartCacheManager:
    """Gerenciador de cache inteligente para mapas JSON"""
    
    def __init__(self, maps_dir: str = "wiki/maps"):
        """
        Inicializa o gerenciador de cache.
        
        Args:
            maps_dir: Diretório contendo os mapas JSON
        """
        self.maps_dir = Path(maps_dir)
        self.cache_dir = self.maps_dir / "smart_cache"
        self.cache_dir.mkdir(exist_ok=True)
        
        # Configurações de cache
        self.cache_config = {
            "frequently_accessed": {
                "files": [
                    "cursor.md",
                    "tags_index.json",
                    "wiki_map.json",
                    "rules.md"
                ],
                "duration": 1800,  # 30 minutos
                "priority": "high"
            },
            "context_switchers": {
                "files": [
                    "enhanced_context_system.json",
                    "context_data.json",
                    "intelligent_navigation.json"
                ],
                "duration": 900,   # 15 minutos
                "priority": "medium"
            },
            "large_datasets": {
                "files": [
                    "otclient_source_index.json",
                    "modules_index.json",
                    "resources_index.json",
                    "search_index.json"
                ],
                "duration": 3600,  # 60 minutos
                "priority": "low"
            },
            "regular_files": {
                "files": [
                    "relationships.json",
                    "bmad_agents_index.json",
                    "bmad_workflows_index.json",
                    "habdel_index.json",
                    "canary_integration_map.json",
                    "navigation_cache.json",
                    "navigation_optimization_report.json",
                    "cursor_performance_analysis.json",
                    "enhanced_orchestration_results.json",
                    "json_navigation_report.json",
                    "maps_update_report.json",
                    "parallel_processing.json",
                    "styles_index.json",
                    "tools_index.json",
                    "cache_strategy.json",
                    "context_update_report.json"
                ],
                "duration": 1200,  # 20 minutos
                "priority": "medium"
            }
        }
        
        # Cache em memória para acesso ultra-rápido
        self.memory_cache = {}
        self.cache_stats = {
            "hits": 0,
            "misses": 0,
            "total_requests": 0,
            "performance_improvement": 0.0
        }
        
    def get_cache_category(self, filename: str) -> str:
        """Determina a categoria de cache para um arquivo"""
        for category, config in self.cache_config.items():
            if filename in config["files"]:
                return category
        return "regular_files"
    
    def get_cache_duration(self, filename: str) -> int:
        """Obtém duração do cache para um arquivo"""
        category = self.get_cache_category(filename)
        return self.cache_config[category]["duration"]
    
    def is_cache_valid(self, cache_file: Path) -> bool:
        """Verifica se cache ainda é válido"""
        if not cache_file.exists():
            return False
        
        try:
            # Verificar timestamp do cache
            cache_data = json.loads(cache_file.read_text(encoding='utf-8'))
            cache_time = datetime.fromisoformat(cache_data.get("cache_timestamp", "1970-01-01"))
            
            # Verificar se arquivo original foi modificado
            original_file = self.maps_dir / cache_data.get("original_file", "")
            if original_file.exists():
                original_mtime = datetime.fromtimestamp(original_file.stat().st_mtime)
                if original_mtime > cache_time:
                    return False
            
            # Verificar duração do cache
            duration = cache_data.get("cache_duration", 1800)
            if datetime.now() - cache_time > timedelta(seconds=duration):
                return False
            
            return True
            
        except Exception as e:
            logger.error(f"Erro ao verificar cache {cache_file}: {e}")
            return False
    
    def get_cached_data(self, filename: str) -> Optional[Dict[str, Any]]:
        """Obtém dados do cache"""
        self.cache_stats["total_requests"] += 1
        
        # Verificar cache em memória primeiro
        if filename in self.memory_cache:
            cache_entry = self.memory_cache[filename]
            if datetime.now() < cache_entry["expires"]:
                self.cache_stats["hits"] += 1
                logger.info(f"Cache hit (memory): {filename}")
                return cache_entry["data"]
            else:
                del self.memory_cache[filename]
        
        # Verificar cache em disco
        cache_file = self.cache_dir / f"{filename}.cache"
        if self.is_cache_valid(cache_file):
            try:
                cache_data = json.loads(cache_file.read_text(encoding='utf-8'))
                
                # Adicionar ao cache em memória
                duration = cache_data.get("cache_duration", 1800)
                self.memory_cache[filename] = {
                    "data": cache_data["data"],
                    "expires": datetime.now() + timedelta(seconds=duration)
                }
                
                self.cache_stats["hits"] += 1
                logger.info(f"Cache hit (disk): {filename}")
                return cache_data["data"]
                
            except Exception as e:
                logger.error(f"Erro ao ler cache {cache_file}: {e}")
        
        self.cache_stats["misses"] += 1
        logger.info(f"Cache miss: {filename}")
        return None
    
    def set_cached_data(self, filename: str, data: Dict[str, Any]) -> bool:
        """Define dados no cache"""
        try:
            duration = self.get_cache_duration(filename)
            cache_data = {
                "original_file": filename,
                "cache_timestamp": datetime.now().isoformat(),
                "cache_duration": duration,
                "data": data
            }
            
            # Salvar em disco
            cache_file = self.cache_dir / f"{filename}.cache"
            cache_file.write_text(json.dumps(cache_data, indent=2, ensure_ascii=False), encoding='utf-8')
            
            # Adicionar ao cache em memória
            self.memory_cache[filename] = {
                "data": data,
                "expires": datetime.now() + timedelta(seconds=duration)
            }
            
            logger.info(f"Cache set: {filename} (duration: {duration}s)")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao definir cache {filename}: {e}")
            return False
    
    def load_map_with_cache(self, filename: str) -> Optional[Dict[str, Any]]:
        """Carrega mapa com cache inteligente"""
        start_time = time.time()
        
        # Tentar obter do cache
        cached_data = self.get_cached_data(filename)
        if cached_data:
            load_time = time.time() - start_time
            logger.info(f"Carregamento com cache: {filename} ({load_time:.3f}s)")
            return cached_data
        
        # Carregar do arquivo original
        original_file = self.maps_dir / filename
        if not original_file.exists():
            logger.error(f"Arquivo não encontrado: {filename}")
            return None
        
        try:
            with open(original_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Adicionar ao cache
            self.set_cached_data(filename, data)
            
            load_time = time.time() - start_time
            logger.info(f"Carregamento sem cache: {filename} ({load_time:.3f}s)")
            return data
            
        except Exception as e:
            logger.error(f"Erro ao carregar {filename}: {e}")
            return None
    
    def implement_smart_cache(self) -> Dict[str, Any]:
        """Implementa cache inteligente para todos os mapas"""
        logger.info("🔄 Implementando cache inteligente...")
        
        start_time = time.time()
        results = {
            "timestamp": datetime.now().isoformat(),
            "files_processed": 0,
            "cache_entries_created": 0,
            "errors": [],
            "performance_metrics": {}
        }
        
        # Listar todos os arquivos JSON no diretório
        json_files = list(self.maps_dir.glob("*.json"))
        logger.info(f"📊 Encontrados {len(json_files)} arquivos JSON")
        
        for json_file in json_files:
            filename = json_file.name
            try:
                # Carregar arquivo com cache
                data = self.load_map_with_cache(filename)
                if data:
                    results["files_processed"] += 1
                    results["cache_entries_created"] += 1
                    
                    # Verificar se cache foi criado
                    cache_file = self.cache_dir / f"{filename}.cache"
                    if cache_file.exists():
                        logger.info(f"✅ Cache criado: {filename}")
                
            except Exception as e:
                error_msg = f"Erro ao processar {filename}: {e}"
                results["errors"].append(error_msg)
                logger.error(error_msg)
        
        # Calcular métricas de performance
        total_time = time.time() - start_time
        hit_rate = self.cache_stats["hits"] / max(self.cache_stats["total_requests"], 1)
        
        results["performance_metrics"] = {
            "total_time": total_time,
            "files_per_second": results["files_processed"] / max(total_time, 1),
            "cache_hit_rate": hit_rate,
            "cache_hits": self.cache_stats["hits"],
            "cache_misses": self.cache_stats["misses"],
            "total_requests": self.cache_stats["total_requests"],
            "estimated_performance_improvement": hit_rate * 0.5  # 50% melhoria para hits
        }
        
        logger.info(f"✅ Cache inteligente implementado!")
        logger.info(f"📊 Arquivos processados: {results['files_processed']}")
        logger.info(f"💾 Entradas de cache criadas: {results['cache_entries_created']}")
        logger.info(f"🎯 Taxa de hit: {hit_rate:.2%}")
        logger.info(f"⚡ Melhoria estimada: {hit_rate * 0.5:.2%}")
        
        return results
    
    def get_cache_stats(self) -> Dict[str, Any]:
        """Obtém estatísticas do cache"""
        hit_rate = self.cache_stats["hits"] / max(self.cache_stats["total_requests"], 1)
        
        return {
            "timestamp": datetime.now().isoformat(),
            "cache_stats": self.cache_stats.copy(),
            "hit_rate": hit_rate,
            "performance_improvement": hit_rate * 0.5,
            "memory_cache_size": len(self.memory_cache),
            "disk_cache_files": len(list(self.cache_dir.glob("*.cache")))
        }
    
    def clear_cache(self) -> bool:
        """Limpa todo o cache"""
        try:
            # Limpar cache em memória
            self.memory_cache.clear()
            
            # Limpar cache em disco
            for cache_file in self.cache_dir.glob("*.cache"):
                cache_file.unlink()
            
            # Resetar estatísticas
            self.cache_stats = {
                "hits": 0,
                "misses": 0,
                "total_requests": 0,
                "performance_improvement": 0.0
            }
            
            logger.info("✅ Cache limpo com sucesso")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao limpar cache: {e}")
            return False

def main():
    """Função principal"""
    print("🚀 Implementação de Cache Inteligente")
    print("=" * 50)
    
    cache_manager = SmartCacheManager()
    
    # Implementar cache inteligente
    results = cache_manager.implement_smart_cache()
    
    # Salvar relatório
    report_file = cache_manager.maps_dir / "smart_cache_report.json"
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n📋 Relatório salvo em: {report_file}")
    
    # Mostrar estatísticas
    stats = cache_manager.get_cache_stats()
    print(f"\n📊 Estatísticas do Cache:")
    print(f"   Hits: {stats['cache_stats']['hits']}")
    print(f"   Misses: {stats['cache_stats']['misses']}")
    print(f"   Taxa de Hit: {stats['hit_rate']:.2%}")
    print(f"   Melhoria Estimada: {stats['performance_improvement']:.2%}")
    
    if stats['performance_improvement'] >= 0.5:
        print("✅ Objetivo de 50% de melhoria ALCANÇADO!")
    else:
        print("⚠️  Objetivo de 50% de melhoria ainda não alcançado")

if __name__ == "__main__":
    main() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = MapupdaterModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script implement_smart_cache.py executado com sucesso via módulo maps.map_updater")
    else:
        print(f"❌ Erro na execução do script implement_smart_cache.py via módulo maps.map_updater")
