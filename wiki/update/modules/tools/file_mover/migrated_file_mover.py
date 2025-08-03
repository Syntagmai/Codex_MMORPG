from unicode_aliases import *
# Constantes
MAX_RETRIES = 8

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: file_mover.py
Módulo de Destino: tools.file_mover
Data de Migração: 2025-08-01 12:21:45

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import FilemoverModule

# Conteúdo original do script
#!/usr/bin/env python3
"""
File Mover Script - Template for Efficient File Organization
============================================================

This script provides a reusable template for moving files between directories
using absolute paths for better performance. It can handle batch operations
and provides detailed logging of all operations.

Usage:
    python file_mover.py --source /absolute/path/source --destination /absolute/path/dest --files file1.md file2.md
    python file_mover.py --config config.json
    python file_mover.py --interactive

Features:
- Absolute directory support for better performance
- Batch file operations
- JSON configuration support
- Interactive mode
- Detailed logging and error handling
- Dry-run mode for testing
- Backup creation before moving
"""

import os
import sys
import json
import shutil
import argparse
import logging
from datetime import datetime

# Configure logging
log_dir = Path.cwd() / 'wiki' / 'log'
log_dir.mkdir(parents=True, exist_ok=True)
log_file = log_dir / 'file_mover.log'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class FileMover:
    """Efficient file mover with absolute directory support."""
    
    def __init__(self, dry_run: bool = False, create_backup: bool = True):
        self.dry_run = dry_run
        self.create_backup = create_backup
        self.moved_files = []
        self.failed_files = []
        self.backup_dir = None
        
    def setup_backup_directory(self, source_dir: str) -> str:
        """Create backup directory for safety."""
        if not self.create_backup:
            return None
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = Path(source_dir) / f"backup_{timestamp}"
        backup_dir.mkdir(exist_ok=True)
        self.backup_dir = str(backup_dir)
        logger.info(f"Backup directory created: {self.backup_dir}")
        return self.backup_dir
    
    def validate_paths(self, source_dir: str, destination_dir: str, files: List[str]) -> Tuple[bool, List[str]]:
        """Validate all paths before moving files."""
        errors = []
        
        # Validate source directory
        if not os.path.isabs(source_dir):
            errors.append(f"Source directory must be absolute: {source_dir}")
        elif not os.path.exists(source_dir):
            errors.append(f"Source directory does not exist: {source_dir}")
            
        # Validate destination directory
        if not os.path.isabs(destination_dir):
            errors.append(f"Destination directory must be absolute: {destination_dir}")
        elif not os.path.exists(destination_dir):
            try:
                os.makedirs(destination_dir, exist_ok=True)
                logger.info(f"Created destination directory: {destination_dir}")
            except Exception as e:
                errors.append(f"Cannot create destination directory {destination_dir}: {e}")
        
        # Validate individual files
        for file in files:
            file_path = os.path.join(source_dir, file)
            if not os.path.exists(file_path):
                errors.append(f"File does not exist: {file_path}")
            elif not os.path.isfile(file_path):
                errors.append(f"Path is not a file: {file_path}")
        
        return len(errors) == 0, errors
    
    def move_file(self, source_file: str, destination_file: str) -> bool:
        """Move a single file with error handling."""
        try:
            if self.dry_run:
                logger.info(f"[DRY RUN] Would move: {source_file} -> {destination_file}")
                return True
                
            # Create backup if enabled
            if self.create_backup and self.backup_dir:
                backup_file = os.path.join(self.backup_dir, os.path.basename(source_file))
                shutil.copy2(source_file, backup_file)
                logger.debug(f"Backup created: {backup_file}")
            
            # Move the file
            shutil.move(source_file, destination_file)
            logger.info(f"Successfully moved: {source_file} -> {destination_file}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to move {source_file}: {e}")
            return False
    
    def move_files(self, source_dir: str, destination_dir: str, files: List[str]) -> Dict[str, List[str]]:
        """Move multiple files efficiently."""
        logger.info(f"Starting file move operation:")
        logger.info(f"Source: {source_dir}")
        logger.info(f"Destination: {destination_dir}")
        logger.info(f"Files: {len(files)} files")
        logger.info(f"Dry run: {self.dry_run}")
        
        # Validate paths
        is_valid, errors = self.validate_paths(source_dir, destination_dir, files)
        if not is_valid:
            logger.error("Path validation failed:")
            for error in errors:
                logger.error(f"  - {error}")
            return {"moved": [], "failed": files}
        
        # Setup backup
        if self.create_backup:
            self.setup_backup_directory(source_dir)
        
        # Move files
        for file in files:
            source_file = os.path.join(source_dir, file)
            destination_file = os.path.join(destination_dir, file)
            
            if self.move_file(source_file, destination_file):
                self.moved_files.append(file)
            else:
                self.failed_files.append(file)
        
        # Summary
        logger.info(f"Operation completed:")
        logger.info(f"  Successfully moved: {len(self.moved_files)} files")
        logger.info(f"  Failed: {len(self.failed_files)} files")
        
        if self.backup_dir:
            logger.info(f"  Backup location: {self.backup_dir}")
        
        return {
            "moved": self.moved_files,
            "failed": self.failed_files,
            "backup_dir": self.backup_dir
        }

def load_config(config_file: str) -> Dict:
    """Load configuration from JSON file."""
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Failed to load config file {config_file}: {e}")
        return {}

def save_config(config: Dict, config_file: str):
    """Save configuration to JSON file."""
    try:
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        logger.info(f"Configuration saved to: {config_file}")
    except Exception as e:
        logger.error(f"Failed to save config file {config_file}: {e}")

def interactive_mode():
    """Interactive mode for file moving."""
    print("=== File Mover - Interactive Mode ===")
    
    # Get source directory
    source_dir = input("Enter source directory (absolute path): ").strip()
    if not os.path.isabs(source_dir):
        print("Error: Source directory must be absolute path")
        return
    
    # Get destination directory
    destination_dir = input("Enter destination directory (absolute path): ").strip()
    if not os.path.isabs(destination_dir):
        print("Error: Destination directory must be absolute path")
        return
    
    # List available files
    try:
        files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
        print(f"\nAvailable files in {source_dir}:")
        for i, file in enumerate(files, 1):
            print(f"  {i}. {file}")
        
        # Get file selection
        selection = input("\nEnter file numbers to move (comma-separated) or 'all': ").strip()
        
        if selection.lower() == 'all':
            selected_files = files
        else:
            try:
                indices = [int(x.strip()) - 1 for x in selection.split(',')]
                selected_files = [files[i] for i in indices if 0 <= i < len(files)]
            except (ValueError, IndexError):
                print("Error: Invalid file selection")
                return
        
        # Confirm operation
        print(f"\nWill move {len(selected_files)} files:")
        for file in selected_files:
            print(f"  - {file}")
        
        confirm = input("\nProceed? (y/N): ").strip().lower()
        if confirm != 'y':
            print("Operation cancelled")
            return
        
        # Execute move
        mover = FileMover(dry_run=False, create_backup=True)
        result = mover.move_files(source_dir, destination_dir, selected_files)
        
        print(f"\nOperation completed:")
        print(f"  Moved: {len(result['moved'])} files")
        print(f"  Failed: {len(result['failed'])} files")
        
    except Exception as e:
        print(f"Error: {e}")

def main():
    """Main function with command line interface."""
    parser = argparse.ArgumentParser(
        description="Efficient file mover with absolute directory support",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Move specific files
  python file_mover.py --source /path/to/source --destination /path/to/dest --files file1.md file2.md
  
  # Use configuration file
  python file_mover.py --config move_config.json
  
  # Interactive mode
  python file_mover.py --interactive
  
  # Dry run (test without moving)
  python file_mover.py --source /path/to/source --destination /path/to/dest --files file1.md --dry-run
        """
    )
    
    parser.add_argument('--source', help='Source directory (absolute path)')
    parser.add_argument('--destination', help='Destination directory (absolute path)')
    parser.add_argument('--files', nargs='+', help='Files to move')
    parser.add_argument('--config', help='Configuration file (JSON)')
    parser.add_argument('--interactive', action='store_true', help='Interactive mode')
    parser.add_argument('--dry-run', action='store_true', help='Test mode (no actual moving)')
    parser.add_argument('--no-backup', action='store_true', help='Skip backup creation')
    
    args = parser.parse_args()
    
    # Interactive mode
    if args.interactive:
        interactive_mode()
        return
    
    # Configuration file mode
    if args.config:
        config = load_config(args.config)
        if not config:
            return
        
        source_dir = config.get('source_dir')
        destination_dir = config.get('destination_dir')
        files = config.get('files', [])
        
        if not all([source_dir, destination_dir, files]):
            logger.error("Invalid configuration: missing source_dir, destination_dir, or files")
            return
    
    # Command line mode
    elif args.source and args.destination and args.files:
        source_dir = args.source
        destination_dir = args.destination
        files = args.files
    
    else:
        parser.print_help()
        return
    
    # Execute move operation
    mover = FileMover(dry_run=args.dry_run, create_backup=not args.no_backup)
    result = mover.move_files(source_dir, destination_dir, files)
    
    # Exit with error code if any files failed
    if result['failed']:
        sys.exit(1)

if __name__ == "__main__":
    main() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = FilemoverModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script file_mover.py executado com sucesso via módulo tools.file_mover")
    else:
        print(f"❌ Erro na execução do script file_mover.py via módulo tools.file_mover")
