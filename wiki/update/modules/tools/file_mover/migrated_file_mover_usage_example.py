from unicode_aliases import *
# Constantes
MAX_RETRIES = 8

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: file_mover_usage_example.py
Módulo de Destino: tools.file_mover
Data de Migração: 2025-08-01 12:21:45

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import FilemoverModule

# Conteúdo original do script
#!/usr/bin/env python3
"""
File Mover Usage Examples
=========================

This script demonstrates how to use the file_mover.py script programmatically
for different scenarios in the OTClient documentation project.

Usage:
    python file_mover_usage_example.py
"""

import os
import sys
import json

# Add the tools directory to the path so we can import file_mover
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def example_1_basic_usage():
    """Example 1: Basic file moving with absolute paths."""
    print("=== Example 1: Basic File Moving ===")
    
    # Define paths (using absolute paths for better performance)
    workspace_root = Path(__file__).parent.parent.parent
    source_dir = str(workspace_root / "wiki" / "habdel")
    destination_dir = str(workspace_root / "wiki" / "habdel" / "documentation")
    
    # Files to move
    files_to_move = [
        "EffectsSystem.md",
        "NetworkSystem.md",
        "ConfigurationAdvanced.md"
    ]
    
    print(f"Source: {source_dir}")
    print(f"Destination: {destination_dir}")
    print(f"Files: {files_to_move}")
    
    # Create mover instance
    mover = FileMover(dry_run=True, create_backup=True)  # Dry run for safety
    
    # Execute move
    result = mover.move_files(source_dir, destination_dir, files_to_move)
    
    print(f"Result: {result}")
    print()

def example_2_configuration_file():
    """Example 2: Using configuration file."""
    print("=== Example 2: Configuration File ===")
    
    workspace_root = Path(__file__).parent.parent.parent
    
    # Create configuration
    config = {
        "source_dir": str(workspace_root / "wiki" / "habdel"),
        "destination_dir": str(workspace_root / "wiki" / "habdel" / "documentation"),
        "files": [
            "SoundSystem.md",
            "GraphicsSystem.md",
            "ItemSystem.md"
        ],
        "description": "Moving system documentation files",
        "backup_enabled": True,
        "dry_run": True
    }
    
    # Save configuration
    config_file = "temp_move_config.json"
    save_config(config, config_file)
    print(f"Configuration saved to: {config_file}")
    
    # Load and use configuration
    with open(config_file, 'r') as f:
        loaded_config = json.load(f)
    
    print(f"Loaded config: {loaded_config}")
    
    # Clean up
    os.remove(config_file)
    print()

def example_3_batch_operations():
    """Example 3: Batch operations for different file types."""
    print("=== Example 3: Batch Operations ===")
    
    workspace_root = Path(__file__).parent.parent.parent
    source_dir = str(workspace_root / "wiki" / "habdel")
    
    # Different destinations for different file types
    operations = [
        {
            "destination": str(workspace_root / "wiki" / "habdel" / "documentation" / "ui"),
            "files": ["UIButton.md", "UITextEdit.md", "UIWidget.md", "UIStyling.md", "UIEvents.md"]
        },
        {
            "destination": str(workspace_root / "wiki" / "habdel" / "documentation" / "systems"),
            "files": ["EffectsSystem.md", "NetworkSystem.md", "SoundSystem.md", "GraphicsSystem.md"]
        },
        {
            "destination": str(workspace_root / "wiki" / "habdel" / "documentation" / "guides"),
            "files": ["BestPractices.md", "FirstModule.md", "GettingStarted.md", "CheatSheet.md"]
        }
    ]
    
    # Execute batch operations
    for i, operation in enumerate(operations, 1):
        print(f"Operation {i}:")
        print(f"  Destination: {operation['destination']}")
        print(f"  Files: {operation['files']}")
        
        # Create destination directory if it doesn't exist
        os.makedirs(operation['destination'], exist_ok=True)
        
        # Execute move (dry run)
        mover = FileMover(dry_run=True, create_backup=True)
        result = mover.move_files(source_dir, operation['destination'], operation['files'])
        
        print(f"  Result: {len(result['moved'])} moved, {len(result['failed'])} failed")
        print()

def example_4_conditional_moving():
    """Example 4: Conditional moving based on file content or metadata."""
    print("=== Example 4: Conditional Moving ===")
    
    workspace_root = Path(__file__).parent.parent.parent
    source_dir = str(workspace_root / "wiki" / "habdel")
    destination_dir = str(workspace_root / "wiki" / "habdel" / "documentation")
    
    # Get all .md files in source directory
    source_path = Path(source_dir)
    all_md_files = [f.name for f in source_path.glob("*.md")]
    
    # Filter files based on conditions
    files_to_move = []
    files_to_keep = []
    
    for file in all_md_files:
        file_path = source_path / file
        
        # Check file size
        file_size = file_path.stat().st_size
        
        # Check if file contains certain keywords
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Move files that are documentation (not system files)
            if any(keyword in content.lower() for keyword in ['documentation', 'guide', 'tutorial', 'api']):
                files_to_move.append(file)
            else:
                files_to_keep.append(file)
                
        except Exception as e:
            print(f"Error reading {file}: {e}")
            files_to_keep.append(file)
    
    print(f"Files to move ({len(files_to_move)}): {files_to_move}")
    print(f"Files to keep ({len(files_to_keep)}): {files_to_keep}")
    
    # Execute move for filtered files
    if files_to_move:
        mover = FileMover(dry_run=True, create_backup=True)
        result = mover.move_files(source_dir, destination_dir, files_to_move)
        print(f"Move result: {result}")
    
    print()

def example_5_error_handling():
    """Example 5: Error handling and recovery."""
    print("=== Example 5: Error Handling ===")
    
    workspace_root = Path(__file__).parent.parent.parent
    source_dir = str(workspace_root / "wiki" / "habdel")
    destination_dir = str(workspace_root / "wiki" / "habdel" / "documentation")
    
    # Try to move non-existent files to test error handling
    non_existent_files = ["NonExistentFile1.md", "NonExistentFile2.md"]
    
    print("Testing error handling with non-existent files...")
    
    mover = FileMover(dry_run=False, create_backup=True)
    result = mover.move_files(source_dir, destination_dir, non_existent_files)
    
    print(f"Result: {result}")
    print(f"Failed files: {result['failed']}")
    print()

def main():
    """Run all examples."""
    print("File Mover Usage Examples")
    print("=" * 50)
    print()
    
    try:
        example_1_basic_usage()
        example_2_configuration_file()
        example_3_batch_operations()
        example_4_conditional_moving()
        example_5_error_handling()
        
        print("All examples completed successfully!")
        
    except Exception as e:
        print(f"Error running examples: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = FilemoverModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script file_mover_usage_example.py executado com sucesso via módulo tools.file_mover")
    else:
        print(f"❌ Erro na execução do script file_mover_usage_example.py via módulo tools.file_mover")

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
- **Nome**: migrated_file_mover_usage_example
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

