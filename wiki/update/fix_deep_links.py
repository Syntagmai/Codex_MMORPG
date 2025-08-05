#!/usr/bin/env python3
"""
Script para corrigir links quebrados mais comuns na wiki.
Baseado no relatório de análise de deep links.
"""
import os
import re
import json
from datetime import datetime
from pathlib import Path

def fix_deep_links():
    """Corrige links quebrados mais comuns."""
    
    wiki_path = Path("wiki")
    report_path = Path("wiki/maps/quick_deep_links_report.json")
    
    # Mapeamento de correções comuns
    link_fixes = {
        # Links do leia_me.md
        "docs/otclient/guides/Getting_Started_Guide|🚀 Guia de Primeiros Passos": "docs/otclient/guides/Getting_Started_Guide.md",
        "docs/otclient/guides/Getting_Started_Guide|Guia de Primeiros Passos": "docs/otclient/guides/Getting_Started_Guide.md",
        "docs/otclient/guides/Module_Development_Guide|🧩 Criando Seu Primeiro Módulo": "docs/otclient/guides/Module_Development_Guide.md",
        "docs/otclient/guides/Cheat_Sheet|📋 Cheat Sheet": "docs/otclient/guides/Cheat_Sheet.md",
        "docs/otclient/guides/Cheat_Sheet|Cheat Sheet": "docs/otclient/guides/Cheat_Sheet.md",
        "docs/otclient/guides/UI_System_Guide|Sistema de Interface": "docs/otclient/guides/UI_System_Guide.md",
        "docs/otclient/guides/Combat_System_Guide|⚔️ Sistema de Combate": "docs/otclient/guides/Combat_System_Guide.md",
        
        # Links do Guia_Inicio_Rapido.md
        "Conceitos_Basicos": "Conceitos_Basicos.md",
        "Troubleshooting_Comum": "Troubleshooting_Comum.md",
        "Glossario_Tecnico": "Glossario_Tecnico.md",
        
        # Links do Glossario_Tecnico.md
        "Conceitos_Basicos": "Conceitos_Basicos.md",
        "Troubleshooting_Comum": "Troubleshooting_Comum.md",
        
        # Links do Conceitos_Basicos.md
        "Troubleshooting_Comum": "Troubleshooting_Comum.md",
        "Glossario_Tecnico": "Glossario_Tecnico.md",
        
        # Links do Troubleshooting_Comum.md
        "Conceitos_Basicos": "Conceitos_Basicos.md",
        "Glossario_Tecnico": "Glossario_Tecnico.md",
    }
    
    # Arquivos para corrigir
    files_to_fix = [
        "leia_me.md",
        "Guia_Inicio_Rapido.md",
        "Glossario_Tecnico.md",
        "Conceitos_Basicos.md",
        "Troubleshooting_Comum.md"
    ]
    
    fixes_applied = []
    
    print(f"🔧 Corrigindo links quebrados em {len(files_to_fix)} arquivos...")
    
    for file_name in files_to_fix:
        file_path = wiki_path / file_name
        
        if not file_path.exists():
            print(f"⚠️ Arquivo não encontrado: {file_name}")
            continue
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            file_fixes = []
            
            # Aplicar correções
            for broken_link, correct_link in link_fixes.items():
                # Corrigir links wiki [[link]]
                if broken_link in content:
                    # Extrair o texto do link
                    link_text = broken_link.split('|')[-1] if '|' in broken_link else broken_link
                    new_link = f"[[{correct_link}|{link_text}]]"
                    old_link = f"[[{broken_link}]]"
                    
                    if old_link in content:
                        content = content.replace(old_link, new_link)
                        file_fixes.append({
                            "old": old_link,
                            "new": new_link,
                            "type": "wiki_link"
                        })
            
            # Salvar se houve mudanças
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                fixes_applied.append({
                    "file": file_name,
                    "fixes": file_fixes
                })
                
                print(f"✅ {file_name}: {len(file_fixes)} correções aplicadas")
            else:
                print(f"⏭️ {file_name}: Nenhuma correção necessária")
                
        except Exception as e:
            print(f"❌ Erro ao processar {file_name}: {e}")
    
    # Salvar relatório de correções
    report_data = {
        "metadata": {
            "fix_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "files_processed": len(files_to_fix),
            "files_fixed": len(fixes_applied),
            "total_fixes": sum(len(f["fixes"]) for f in fixes_applied)
        },
        "fixes_applied": fixes_applied,
        "link_fixes_mapping": link_fixes
    }
    
    report_file = Path("wiki/maps/deep_links_fixes_report.json")
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Correção concluída!")
    print(f"📊 Arquivos processados: {len(files_to_fix)}")
    print(f"🔧 Arquivos corrigidos: {len(fixes_applied)}")
    print(f"🔗 Total de correções: {sum(len(f['fixes']) for f in fixes_applied)}")
    print(f"📋 Relatório salvo: {report_file}")
    
    return report_data

if __name__ == "__main__":
    fix_deep_links() 