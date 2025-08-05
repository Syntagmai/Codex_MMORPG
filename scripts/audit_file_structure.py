#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script simples para auditar estrutura de arquivos
"""

import os
import json
from datetime import datetime
from pathlib import Path

def audit_file_structure():
    """Audita a estrutura de arquivos do projeto"""
    print("🔍 Iniciando auditoria da estrutura de arquivos...")
    
    project_root = Path(".")
    audit_results = {
        "timestamp": datetime.now().isoformat(),
        "project_root": str(project_root.resolve()),
        "total_files": 0,
        "total_directories": 0,
        "issues": [],
        "obsolete_items": [],
        "empty_directories": [],
        "file_extensions": {},
        "directory_structure": {}
    }
    
    # Padrões obsoletos
    obsolete_patterns = ["backup", "old", "legacy", "deprecated", "temp", "tmp", "test_", "_test", "debug"]
    
    # Escaneia o projeto
    for root, dirs, files in os.walk(project_root):
        relative_root = Path(root).relative_to(project_root)
        
        # Conta arquivos e diretórios
        audit_results["total_directories"] += len(dirs)
        audit_results["total_files"] += len(files)
        
        # Verifica diretórios vazios
        if not dirs and not files:
            audit_results["empty_directories"].append(str(relative_root))
        
        # Verifica padrões obsoletos
        for dir_name in dirs:
            for pattern in obsolete_patterns:
                if pattern in dir_name.lower():
                    audit_results["obsolete_items"].append({
                        "type": "directory",
                        "path": str(relative_root / dir_name),
                        "pattern": pattern
                    })
                    break
        
        # Conta extensões de arquivos
        for file_name in files:
            file_path = Path(file_name)
            extension = file_path.suffix.lower()
            if extension:
                audit_results["file_extensions"][extension] = audit_results["file_extensions"].get(extension, 0) + 1
            
            # Verifica problemas de nomenclatura
            if ' ' in file_name:
                audit_results["issues"].append({
                    "type": "spaces_in_filename",
                    "path": str(relative_root / file_name)
                })
    
    # Salva relatório
    output_file = "wiki/docs/audit_reports/file_structure_audit_report.json"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(audit_results, f, indent=2, ensure_ascii=False)
    
    # Imprime resumo
    print("\n" + "="*60)
    print("📊 RESUMO DA AUDITORIA DE ESTRUTURA")
    print("="*60)
    print(f"📁 Total de diretórios: {audit_results['total_directories']}")
    print(f"📄 Total de arquivos: {audit_results['total_files']}")
    print(f"⚠️  Problemas encontrados: {len(audit_results['issues'])}")
    print(f"🗑️  Itens obsoletos: {len(audit_results['obsolete_items'])}")
    print(f"📂 Diretórios vazios: {len(audit_results['empty_directories'])}")
    print(f"📄 Extensões únicas: {len(audit_results['file_extensions'])}")
    
    # Mostra extensões mais comuns
    print(f"\n📄 EXTENSÕES MAIS COMUNS:")
    sorted_extensions = sorted(audit_results['file_extensions'].items(), key=lambda x: x[1], reverse=True)
    for ext, count in sorted_extensions[:10]:
        print(f"  • {ext}: {count} arquivos")
    
    # Mostra problemas
    if audit_results['issues']:
        print(f"\n⚠️  PROBLEMAS ENCONTRADOS:")
        for issue in audit_results['issues'][:5]:
            print(f"  • {issue['type']}: {issue['path']}")
    
    # Mostra itens obsoletos
    if audit_results['obsolete_items']:
        print(f"\n🗑️  ITENS OBSOLETOS:")
        for item in audit_results['obsolete_items'][:5]:
            print(f"  • {item['path']} (padrão: {item['pattern']})")
    
    print(f"\n📄 Relatório salvo em: {output_file}")
    print("="*60)
    
    return audit_results

if __name__ == "__main__":
    audit_file_structure() 