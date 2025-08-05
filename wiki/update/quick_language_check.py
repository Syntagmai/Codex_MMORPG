#!/usr/bin/env python3
"""
Script rápido para verificar consistência de idioma em arquivos importantes da wiki.
"""

import os
import re
import json
from datetime import datetime
from pathlib import Path

def quick_language_check():
    """Verificação rápida de consistência de idioma."""
    
    # Arquivos importantes para verificar
    important_files = [
        "wiki/leia_me.md",
        "wiki/GLOSSARIO_TERMINOLOGIA_TECNICA.md",
        "wiki/dashboard/task_master.md",
        "wiki/dashboard/integrated_task_manager.md"
    ]
    
    # Termos técnicos principais que devem estar em português
    technical_terms = {
        "function": "função",
        "class": "classe",
        "method": "método",
        "variable": "variável",
        "parameter": "parâmetro",
        "return": "retornar",
        "import": "importar",
        "export": "exportar",
        "module": "módulo",
        "interface": "interface",
        "event": "evento",
        "callback": "função de retorno",
        "system": "sistema",
        "component": "componente",
        "widget": "widget",
        "button": "botão",
        "window": "janela",
        "file": "arquivo",
        "folder": "pasta",
        "directory": "diretório",
        "config": "configuração",
        "settings": "configurações",
        "debug": "depuração",
        "error": "erro",
        "warning": "aviso",
        "info": "informação",
        "success": "sucesso"
    }
    
    results = []
    total_issues = 0
    
    print("🔍 Verificação rápida de consistência de idioma...")
    
    for file_path in important_files:
        if not os.path.exists(file_path):
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"❌ Erro ao ler {file_path}: {e}")
            continue
        
        issues = []
        
        # Verificar termos técnicos em inglês
        for english_term, portuguese_term in technical_terms.items():
            pattern = r'\b' + re.escape(english_term) + r'\b'
            matches = re.finditer(pattern, content, re.IGNORECASE)
            
            for match in matches:
                # Verificar se não é uma exceção (nomes próprios)
                if english_term.lower() not in ['lua', 'python', 'c++', 'otclient', 'otui', 'api', 'ui', 'gui']:
                    issues.append({
                        "term": english_term,
                        "sugestao": portuguese_term,
                        "linha": content[:match.start()].count('\n') + 1
                    })
        
        results.append({
            "file": file_path,
            "issues": issues,
            "total_issues": len(issues)
        })
        
        total_issues += len(issues)
        
        if issues:
            print(f"⚠️  {file_path}: {len(issues)} problemas encontrados")
        else:
            print(f"✅ {file_path}: Sem problemas")
    
    # Salvar relatório
    report = {
        "metadata": {
            "timestamp": datetime.now().isoformat(),
            "total_files": len(results),
            "total_issues": total_issues,
            "description": "Verificação rápida de consistência de idioma"
        },
        "files": results
    }
    
    report_path = "wiki/maps/quick_language_report.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\n📊 RESUMO:")
    print(f"📁 Arquivos verificados: {len(results)}")
    print(f"❌ Total de problemas: {total_issues}")
    print(f"📄 Relatório salvo em: {report_path}")
    
    if total_issues > 0:
        print(f"\n🔍 PROBLEMAS ENCONTRADOS:")
        for result in results:
            if result['total_issues'] > 0:
                print(f"\n📄 {result['file']}:")
                for issue in result['issues']:
                    print(f"  - Linha {issue['linha']}: '{issue['term']}' → '{issue['sugestao']}'")
    
    return report

if __name__ == "__main__":
    quick_language_check() 