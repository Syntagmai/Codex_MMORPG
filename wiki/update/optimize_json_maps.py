#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Otimização de Mapas JSON
==================================

Este script otimiza mapas JSON grandes para melhorar performance
e reduzir uso de memória, mantendo funcionalidade completa.

Autor: Sistema BMAD - OTClient Documentation
Data: 2024-12-19
"""

import json
import os
import gzip
import shutil
from pathlib import Path
from typing import Dict, List, Any, Optional
import time
import logging

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class JSONMapOptimizer:
    """Otimizador de mapas JSON para melhorar performance."""
    
    def __init__(self, maps_dir: str = "../maps"):
        """
        Inicializa o otimizador.
        
        Args:
            maps_dir: Diretório contendo os mapas JSON
        """
        self.maps_dir = Path(maps_dir)
        self.optimized_dir = self.maps_dir / "optimized"
        self.backup_dir = self.maps_dir / "backup"
        
        # Criar diretórios se não existirem
        self.optimized_dir.mkdir(exist_ok=True)
        self.backup_dir.mkdir(exist_ok=True)
        
        # Configurações de otimização
        self.compression_threshold = 100 * 1024  # 100KB
        self.chunk_size = 1000  # Número de itens por chunk
        
    def analyze_map_size(self, file_path: Path) -> Dict[str, Any]:
        """
        Analisa o tamanho e estrutura de um mapa JSON.
        
        Args:
            file_path: Caminho para o arquivo JSON
            
        Returns:
            Dicionário com informações de análise
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            file_size = file_path.stat().st_size
            data_size = len(json.dumps(data, separators=(',', ':')))
            
            analysis = {
                'file_path': str(file_path),
                'file_size_bytes': file_size,
                'file_size_mb': file_size / (1024 * 1024),
                'data_size_bytes': data_size,
                'data_size_mb': data_size / (1024 * 1024),
                'structure_type': self._analyze_structure(data),
                'item_count': self._count_items(data),
                'needs_optimization': file_size > self.compression_threshold
            }
            
            logger.info(f"Análise de {file_path.name}: {analysis['file_size_mb']:.2f}MB")
            return analysis
            
        except Exception as e:
            logger.error(f"Erro ao analisar {file_path}: {e}")
            return {}
    
    def _analyze_structure(self, data: Any) -> str:
        """Analisa a estrutura dos dados JSON."""
        if isinstance(data, dict):
            if 'files' in data and 'metadata' in data:
                return 'wiki_map'
            elif 'files_by_tag' in data:
                return 'tags_index'
            elif 'relationships' in data:
                return 'relationships'
            else:
                return 'generic_dict'
        elif isinstance(data, list):
            return 'list'
        else:
            return 'simple'
    
    def _count_items(self, data: Any) -> int:
        """Conta o número de itens nos dados."""
        if isinstance(data, dict):
            if 'files' in data:
                return len(data['files'])
            elif 'files_by_tag' in data:
                return len(data['files_by_tag'])
            else:
                return len(data)
        elif isinstance(data, list):
            return len(data)
        else:
            return 1
    
    def optimize_map(self, file_path: Path, strategy: str = 'auto') -> bool:
        """
        Otimiza um mapa JSON usando a estratégia especificada.
        
        Args:
            file_path: Caminho para o arquivo JSON
            strategy: Estratégia de otimização ('auto', 'compress', 'chunk', 'both')
            
        Returns:
            True se a otimização foi bem-sucedida
        """
        try:
            # Fazer backup
            backup_path = self.backup_dir / f"{file_path.stem}_backup_{int(time.time())}.json"
            shutil.copy2(file_path, backup_path)
            logger.info(f"Backup criado: {backup_path}")
            
            # Carregar dados
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Determinar estratégia
            if strategy == 'auto':
                analysis = self.analyze_map_size(file_path)
                if analysis['file_size_bytes'] > 500 * 1024:  # 500KB
                    strategy = 'both'
                elif analysis['file_size_bytes'] > 100 * 1024:  # 100KB
                    strategy = 'compress'
                else:
                    strategy = 'none'
            
            optimized_data = data
            
            # Aplicar otimizações
            if strategy in ['compress', 'both']:
                optimized_data = self._compress_data(optimized_data)
            
            if strategy in ['chunk', 'both']:
                optimized_data = self._chunk_data(optimized_data, file_path)
            
            # Salvar versão otimizada
            optimized_path = self.optimized_dir / f"{file_path.stem}_optimized.json"
            with open(optimized_path, 'w', encoding='utf-8') as f:
                json.dump(optimized_data, f, separators=(',', ':'), ensure_ascii=False)
            
            # Criar versão comprimida se necessário
            if strategy in ['compress', 'both']:
                compressed_path = self.optimized_dir / f"{file_path.stem}_compressed.json.gz"
                with gzip.open(compressed_path, 'wt', encoding='utf-8') as f:
                    json.dump(optimized_data, f, separators=(',', ':'), ensure_ascii=False)
            
            # Calcular economia
            original_size = file_path.stat().st_size
            optimized_size = optimized_path.stat().st_size
            savings = ((original_size - optimized_size) / original_size) * 100
            
            logger.info(f"Otimização concluída: {file_path.name}")
            logger.info(f"Tamanho original: {original_size / 1024:.1f}KB")
            logger.info(f"Tamanho otimizado: {optimized_size / 1024:.1f}KB")
            logger.info(f"Economia: {savings:.1f}%")
            
            return True
            
        except Exception as e:
            logger.error(f"Erro ao otimizar {file_path}: {e}")
            return False
    
    def _compress_data(self, data: Any) -> Any:
        """Comprime dados removendo espaços desnecessários e otimizando estrutura."""
        if isinstance(data, dict):
            compressed = {}
            for key, value in data.items():
                if value is not None and value != "":
                    compressed[key] = self._compress_data(value)
            return compressed
        elif isinstance(data, list):
            return [self._compress_data(item) for item in data if item is not None]
        else:
            return data
    
    def _chunk_data(self, data: Dict[str, Any], file_path: Path) -> Dict[str, Any]:
        """Divide dados grandes em chunks menores."""
        if 'files' in data and len(data['files']) > self.chunk_size:
            chunks = {}
            files_list = list(data['files'].items())
            
            for i in range(0, len(files_list), self.chunk_size):
                chunk_num = i // self.chunk_size + 1
                chunk_data = dict(files_list[i:i + self.chunk_size])
                
                chunk_path = self.optimized_dir / f"{file_path.stem}_chunk_{chunk_num}.json"
                with open(chunk_path, 'w', encoding='utf-8') as f:
                    json.dump(chunk_data, f, separators=(',', ':'), ensure_ascii=False)
                
                chunks[f"chunk_{chunk_num}"] = str(chunk_path)
            
            # Criar arquivo de índice
            index_data = {
                'metadata': data.get('metadata', {}),
                'chunks': chunks,
                'total_files': len(data['files']),
                'chunk_size': self.chunk_size
            }
            
            return index_data
        
        return data
    
    def optimize_all_maps(self, strategy: str = 'auto') -> Dict[str, Any]:
        """
        Otimiza todos os mapas JSON no diretório.
        
        Args:
            strategy: Estratégia de otimização
            
        Returns:
            Relatório de otimização
        """
        logger.info("Iniciando otimização de todos os mapas JSON...")
        
        json_files = list(self.maps_dir.glob("*.json"))
        results = {
            'total_files': len(json_files),
            'optimized_files': 0,
            'failed_files': 0,
            'total_savings_mb': 0,
            'details': []
        }
        
        for file_path in json_files:
            if file_path.name.startswith('_') or 'backup' in file_path.name:
                continue
            
            logger.info(f"Otimizando: {file_path.name}")
            
            # Analisar antes da otimização
            analysis = self.analyze_map_size(file_path)
            
            # Otimizar
            success = self.optimize_map(file_path, strategy)
            
            if success:
                results['optimized_files'] += 1
                results['total_savings_mb'] += analysis.get('file_size_mb', 0)
                results['details'].append({
                    'file': file_path.name,
                    'original_size_mb': analysis.get('file_size_mb', 0),
                    'status': 'success'
                })
            else:
                results['failed_files'] += 1
                results['details'].append({
                    'file': file_path.name,
                    'status': 'failed'
                })
        
        logger.info(f"Otimização concluída: {results['optimized_files']}/{results['total_files']} arquivos")
        logger.info(f"Economia total: {results['total_savings_mb']:.2f}MB")
        
        return results
    
    def generate_optimization_report(self, results: Dict[str, Any]) -> str:
        """Gera relatório de otimização."""
        report_path = self.maps_dir / "optimization_report.json"
        
        report = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'optimization_results': results,
            'settings': {
                'compression_threshold': self.compression_threshold,
                'chunk_size': self.chunk_size
            }
        }
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        return str(report_path)

def main():
    """Função principal do script."""
    print("🔄 Iniciando otimização de mapas JSON...")
    
    optimizer = JSONMapOptimizer()
    
    # Analisar todos os mapas
    print("\n📊 Analisando mapas existentes...")
    json_files = list(optimizer.maps_dir.glob("*.json"))
    
    for file_path in json_files:
        if not file_path.name.startswith('_'):
            analysis = optimizer.analyze_map_size(file_path)
            if analysis:
                print(f"  {file_path.name}: {analysis['file_size_mb']:.2f}MB")
    
    # Otimizar mapas
    print("\n⚡ Iniciando otimização...")
    results = optimizer.optimize_all_maps(strategy='auto')
    
    # Gerar relatório
    print("\n📋 Gerando relatório...")
    report_path = optimizer.generate_optimization_report(results)
    
    print(f"\n✅ Otimização concluída!")
    print(f"📁 Relatório salvo em: {report_path}")
    print(f"📊 Arquivos otimizados: {results['optimized_files']}/{results['total_files']}")
    print(f"💾 Economia total: {results['total_savings_mb']:.2f}MB")

if __name__ == "__main__":
    main() 