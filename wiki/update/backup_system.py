    import argparse
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional
import gzip
import hashlib
import json
import logging
import os
import shutil
import tarfile
import time

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Backup Automático
============================

Este script implementa um sistema completo de backup automático
para o projeto OTClient Documentation, incluindo backup incremental,
compressão e restauração.

Autor: Sistema BMAD - OTClient Documentation
Data: 2024-12-19
"""


# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BackupSystem:
    """Sistema de backup automático para OTClient Documentation."""
    
    def __init__(self, project_root: str = "../..", backup_dir: str = "../backups"):
        """
        Inicializa o sistema de backup.
        
        Args:
            project_root: Diretório raiz do projeto
            backup_dir: Diretório para armazenar backups
        """
        self.project_root = Path(project_root).resolve()
        self.backup_dir = Path(backup_dir).resolve()
        self.backup_dir.mkdir(exist_ok=True)
        
        # Configurações
        self.max_backups = 10
        self.compression_level = 6
        self.backup_types = {
            'full': ['wiki/', '.cursor/', 'cursor.md'],
            'incremental': ['wiki/maps/', 'wiki/log/'],
            'critical': ['.cursor/rules/', 'cursor.md']
        }
        
        # Arquivo de controle
        self.control_file = self.backup_dir / "backup_control.json"
        self.load_control()
    
    def load_control(self):
        """Carrega arquivo de controle de backups."""
        if self.control_file.exists():
            with open(self.control_file, 'r', encoding='utf-8') as f:
                self.control_data = json.load(f)
        else:
            self.control_data = {
                'backups': [],
                'last_full_backup': None,
                'last_incremental_backup': None,
                'settings': {
                    'max_backups': self.max_backups,
                    'compression_level': self.compression_level
                }
            }
    
    def save_control(self):
        """Salva arquivo de controle de backups."""
        with open(self.control_file, 'w', encoding='utf-8') as f:
            json.dump(self.control_data, f, indent=2, ensure_ascii=False)
    
    def calculate_file_hash(self, file_path: Path) -> str:
        """Calcula hash MD5 de um arquivo."""
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def get_file_list(self, backup_type: str) -> List[Path]:
        """Obtém lista de arquivos para backup."""
        files = []
        for pattern in self.backup_types[backup_type]:
            pattern_path = self.project_root / pattern
            
            if pattern_path.is_file():
                files.append(pattern_path)
            elif pattern_path.is_dir():
                for file_path in pattern_path.rglob('*'):
                    if file_path.is_file():
                        files.append(file_path)
        
        return files
    
    def create_backup(self, backup_type: str = 'incremental', force: bool = False) -> Dict[str, Any]:
        """
        Cria um backup do tipo especificado.
        
        Args:
            backup_type: Tipo de backup ('full', 'incremental', 'critical')
            force: Forçar backup mesmo se não necessário
            
        Returns:
            Dicionário com informações do backup
        """
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_name = f"otclient_backup_{backup_type}_{timestamp}"
        backup_path = self.backup_dir / backup_name
        
        logger.info(f"Iniciando backup {backup_type}: {backup_name}")
        
        try:
            # Verificar se backup é necessário
            if not force and not self._backup_needed(backup_type):
                logger.info(f"Backup {backup_type} não necessário")
                return {'status': 'skipped', 'reason': 'no_changes'}
            
            # Criar diretório temporário
            temp_dir = backup_path.with_suffix('.tmp')
            temp_dir.mkdir(exist_ok=True)
            
            # Obter lista de arquivos
            files = self.get_file_list(backup_type)
            logger.info(f"Backupando {len(files)} arquivos")
            
            # Copiar arquivos
            copied_files = []
            total_size = 0
            
            for file_path in files:
                try:
                    # Calcular caminho relativo
                    rel_path = file_path.relative_to(self.project_root)
                    dest_path = temp_dir / rel_path
                    
                    # Criar diretório de destino
                    dest_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    # Copiar arquivo
                    shutil.copy2(file_path, dest_path)
                    copied_files.append(str(rel_path))
                    total_size += file_path.stat().st_size
                    
                except Exception as e:
                    logger.warning(f"Erro ao copiar {file_path}: {e}")
            
            # Criar arquivo de metadados
            metadata = {
                'backup_type': backup_type,
                'timestamp': timestamp,
                'files': copied_files,
                'total_files': len(copied_files),
                'total_size_bytes': total_size,
                'total_size_mb': total_size / (1024 * 1024),
                'compression_level': self.compression_level
            }
            
            metadata_path = temp_dir / "backup_metadata.json"
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2, ensure_ascii=False)
            
            # Comprimir backup
            archive_path = backup_path.with_suffix('.tar.gz')
            with tarfile.open(archive_path, 'w:gz', compresslevel=self.compression_level) as tar:
                tar.add(temp_dir, arcname=backup_name)
            
            # Remover diretório temporário
            shutil.rmtree(temp_dir)
            
            # Calcular hash do arquivo
            file_hash = self.calculate_file_hash(archive_path)
            
            # Atualizar controle
            backup_info = {
                'name': backup_name,
                'type': backup_type,
                'timestamp': timestamp,
                'file_path': str(archive_path),
                'file_size_bytes': archive_path.stat().st_size,
                'file_size_mb': archive_path.stat().st_size / (1024 * 1024),
                'file_hash': file_hash,
                'metadata': metadata
            }
            
            self.control_data['backups'].append(backup_info)
            
            if backup_type == 'full':
                self.control_data['last_full_backup'] = timestamp
            elif backup_type == 'incremental':
                self.control_data['last_incremental_backup'] = timestamp
            
            self.save_control()
            
            # Limpar backups antigos
            self._cleanup_old_backups()
            
            logger.info(f"Backup concluído: {archive_path}")
            logger.info(f"Tamanho: {backup_info['file_size_mb']:.2f}MB")
            
            return {
                'status': 'success',
                'backup_info': backup_info
            }
            
        except Exception as e:
            logger.error(f"Erro ao criar backup: {e}")
            # Limpar arquivos temporários
            if temp_dir.exists():
                shutil.rmtree(temp_dir)
            if backup_path.with_suffix('.tar.gz').exists():
                backup_path.with_suffix('.tar.gz').unlink()
            
            return {
                'status': 'error',
                'error': str(e)
            }
    
    def _backup_needed(self, backup_type: str) -> bool:
        """Verifica se um backup é necessário."""
        if backup_type == 'full':
            # Backup completo a cada 7 dias
            if self.control_data['last_full_backup']:
                last_backup = datetime.strptime(self.control_data['last_full_backup'], '%Y%m%d_%H%M%S')
                return datetime.now() - last_backup > timedelta(days=7)
            return True
        
        elif backup_type == 'incremental':
            # Backup incremental a cada 24 horas
            if self.control_data['last_incremental_backup']:
                last_backup = datetime.strptime(self.control_data['last_incremental_backup'], '%Y%m%d_%H%M%S')
                return datetime.now() - last_backup > timedelta(hours=24)
            return True
        
        return True
    
    def _cleanup_old_backups(self):
        """Remove backups antigos mantendo apenas os mais recentes."""
        backups = self.control_data['backups']
        
        # Ordenar por timestamp
        backups.sort(key=lambda x: x['timestamp'], reverse=True)
        
        # Manter apenas os mais recentes
        if len(backups) > self.max_backups:
            backups_to_remove = backups[self.max_backups:]
            
            for backup in backups_to_remove:
                try:
                    backup_path = Path(backup['file_path'])
                    if backup_path.exists():
                        backup_path.unlink()
                        logger.info(f"Backup removido: {backup_path}")
                except Exception as e:
                    logger.warning(f"Erro ao remover backup {backup['name']}: {e}")
            
            # Atualizar lista
            self.control_data['backups'] = backups[:self.max_backups]
            self.save_control()
    
    def restore_backup(self, backup_name: str, restore_path: str = None) -> Dict[str, Any]:
        """
        Restaura um backup.
        
        Args:
            backup_name: Nome do backup para restaurar
            restore_path: Caminho para restaurar (padrão: projeto original)
            
        Returns:
            Dicionário com resultado da restauração
        """
        logger.info(f"Iniciando restauração: {backup_name}")
        
        try:
            # Encontrar backup
            backup_info = None
            for backup in self.control_data['backups']:
                if backup['name'] == backup_name:
                    backup_info = backup
                    break
            
            if not backup_info:
                return {
                    'status': 'error',
                    'error': f'Backup {backup_name} não encontrado'
                }
            
            backup_path = Path(backup_info['file_path'])
            if not backup_path.exists():
                return {
                    'status': 'error',
                    'error': f'Arquivo de backup não encontrado: {backup_path}'
                }
            
            # Verificar hash
            current_hash = self.calculate_file_hash(backup_path)
            if current_hash != backup_info['file_hash']:
                return {
                    'status': 'error',
                    'error': 'Hash do arquivo de backup não confere'
                }
            
            # Definir caminho de restauração
            if restore_path is None:
                restore_path = self.project_root
            else:
                restore_path = Path(restore_path)
            
            # Criar backup do estado atual antes da restauração
            safety_backup = self.create_backup('critical', force=True)
            
            # Extrair backup
            temp_dir = self.backup_dir / f"restore_temp_{int(time.time())}"
            temp_dir.mkdir(exist_ok=True)
            
            with tarfile.open(backup_path, 'r:gz') as tar:
                tar.extractall(temp_dir)
            
            # Encontrar diretório do backup
            backup_dir = None
            for item in temp_dir.iterdir():
                if item.is_dir() and item.name.startswith('otclient_backup_'):
                    backup_dir = item
                    break
            
            if not backup_dir:
                return {
                    'status': 'error',
                    'error': 'Estrutura de backup inválida'
                }
            
            # Restaurar arquivos
            restored_files = []
            for file_path in backup_dir.rglob('*'):
                if file_path.is_file() and file_path.name != 'backup_metadata.json':
                    try:
                        rel_path = file_path.relative_to(backup_dir)
                        dest_path = restore_path / rel_path
                        
                        # Criar diretório de destino
                        dest_path.parent.mkdir(parents=True, exist_ok=True)
                        
                        # Copiar arquivo
                        shutil.copy2(file_path, dest_path)
                        restored_files.append(str(rel_path))
                        
                    except Exception as e:
                        logger.warning(f"Erro ao restaurar {file_path}: {e}")
            
            # Limpar diretório temporário
            shutil.rmtree(temp_dir)
            
            logger.info(f"Restauração concluída: {len(restored_files)} arquivos")
            
            return {
                'status': 'success',
                'restored_files': restored_files,
                'safety_backup': safety_backup
            }
            
        except Exception as e:
            logger.error(f"Erro na restauração: {e}")
            return {
                'status': 'error',
                'error': str(e)
            }
    
    def list_backups(self) -> List[Dict[str, Any]]:
        """Lista todos os backups disponíveis."""
        return self.control_data['backups']
    
    def get_backup_status(self) -> Dict[str, Any]:
        """Obtém status atual do sistema de backup."""
        backups = self.control_data['backups']
        
        if not backups:
            return {
                'status': 'no_backups',
                'message': 'Nenhum backup encontrado'
            }
        
        latest_backup = max(backups, key=lambda x: x['timestamp'])
        total_size = sum(b['file_size_mb'] for b in backups)
        
        return {
            'status': 'active',
            'total_backups': len(backups),
            'latest_backup': latest_backup,
            'total_size_mb': total_size,
            'last_full_backup': self.control_data['last_full_backup'],
            'last_incremental_backup': self.control_data['last_incremental_backup']
        }

def main():
    """Função principal do script."""
    
    parser = argparse.ArgumentParser(description='Sistema de Backup OTClient')
    parser.add_argument('action', choices=['create', 'restore', 'list', 'status'],
                       help='Ação a executar')
    parser.add_argument('--type', choices=['full', 'incremental', 'critical'],
                       default='incremental', help='Tipo de backup')
    parser.add_argument('--force', action='store_true',
                       help='Forçar backup mesmo se não necessário')
    parser.add_argument('--backup-name', help='Nome do backup para restaurar')
    parser.add_argument('--restore-path', help='Caminho para restaurar backup')
    
    args = parser.parse_args()
    
    backup_system = BackupSystem()
    
    if args.action == 'create':
        print("🔄 Criando backup...")
        result = backup_system.create_backup(args.type, args.force)
        
        if result['status'] == 'success':
            print(f"✅ Backup criado: {result['backup_info']['name']}")
            print(f"📁 Arquivo: {result['backup_info']['file_path']}")
            print(f"📊 Tamanho: {result['backup_info']['file_size_mb']:.2f}MB")
        elif result['status'] == 'skipped':
            print(f"⏭️ Backup pulado: {result['reason']}")
        else:
            print(f"❌ Erro: {result['error']}")
    
    elif args.action == 'restore':
        if not args.backup_name:
            print("❌ Nome do backup é obrigatório para restauração")
            return
        
        print(f"🔄 Restaurando backup: {args.backup_name}")
        result = backup_system.restore_backup(args.backup_name, args.restore_path)
        
        if result['status'] == 'success':
            print(f"✅ Restauração concluída: {len(result['restored_files'])} arquivos")
        else:
            print(f"❌ Erro: {result['error']}")
    
    elif args.action == 'list':
        print("📋 Lista de backups:")
        backups = backup_system.list_backups()
        
        if not backups:
            print("  Nenhum backup encontrado")
        else:
            for backup in backups:
                print(f"  {backup['name']} ({backup['type']}) - {backup['file_size_mb']:.2f}MB")
    
    elif args.action == 'status':
        print("📊 Status do sistema de backup:")
        status = backup_system.get_backup_status()
        
        if status['status'] == 'active':
            print(f"  Total de backups: {status['total_backups']}")
            print(f"  Tamanho total: {status['total_size_mb']:.2f}MB")
            print(f"  Último backup completo: {status['last_full_backup']}")
            print(f"  Último backup incremental: {status['last_incremental_backup']}")
        else:
            print(f"  {status['message']}")

if __name__ == "__main__":
    main() 