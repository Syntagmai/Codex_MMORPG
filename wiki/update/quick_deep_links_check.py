#!/usr/bin/env python3
"""
Script simplificado para verificar deep links nos arquivos principais da wiki.
Foca nos arquivos mais importantes e evita problemas de encoding.
"""
import os
import re
import json
from datetime import datetime
from pathlib import Path

def quick_deep_links_check():
    """Verificação rápida de deep links nos arquivos principais."""
    
    wiki_path = Path("wiki")
    report_path = Path("wiki/maps/quick_deep_links_report.json")
    
    # Arquivos principais para verificar (evitar arquivos com problemas de encoding)
    main_files = [
        "README.md",
        "leia_me.md",
        "Guia_Inicio_Rapido.md",
        "Glossario_Tecnico.md",
        "Conceitos_Basicos.md",
        "Troubleshooting_Comum.md",
        "dashboard/task_master.md",
        "dashboard/integrated_task_manager.md",
        "docs/otclient/guides/Module_Development_Guide.md",
        "docs/otclient/guides/Getting_Started_Guide.md"
    ]
    
    # Padrões para identificar links
    link_patterns = [
        r'\[([^\]]+)\]\(([^)]+)\)',  # Markdown links [text](url)
        r'\[\[([^\]]+)\]\]',         # Wiki links [[page]]
    ]
    
    links_data = {
        "metadata": {
            "analysis_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "files_analyzed": [],
            "total_links_found": 0,
            "broken_links": 0,
            "valid_links": 0
        },
        "broken_links": [],
        "valid_links": [],
        "recommendations": []
    }
    
    # Coletar todos os arquivos existentes
    existing_files = set()
    for file_path in wiki_path.rglob("*.md"):
        try:
            relative_path = str(file_path.relative_to(wiki_path))
            existing_files.add(relative_path)
            existing_files.add(relative_path.replace('.md', ''))
        except:
            continue
    
    print(f"🔍 Analisando {len(main_files)} arquivos principais da wiki...")
    
    for file_name in main_files:
        file_path = wiki_path / file_name
        
        if not file_path.exists():
            print(f"⚠️ Arquivo não encontrado: {file_name}")
            continue
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            links_data["metadata"]["files_analyzed"].append(file_name)
            
            # Encontrar links
            for pattern in link_patterns:
                matches = re.finditer(pattern, content)
                
                for match in matches:
                    link_text = match.group(1) if len(match.groups()) > 0 else match.group(0)
                    link_url = match.group(2) if len(match.groups()) > 1 else None
                    
                    # Analisar link
                    link_info = analyze_link(link_text, link_url, file_name, existing_files)
                    
                    if link_info:
                        links_data["metadata"]["total_links_found"] += 1
                        
                        if link_info["status"] == "broken":
                            links_data["broken_links"].append(link_info)
                            links_data["metadata"]["broken_links"] += 1
                        else:
                            links_data["valid_links"].append(link_info)
                            links_data["metadata"]["valid_links"] += 1
                            
        except Exception as e:
            print(f"❌ Erro ao processar {file_name}: {e}")
    
    # Gerar recomendações
    generate_recommendations(links_data)
    
    # Salvar relatório
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(links_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Análise concluída!")
    print(f"📊 Total de links encontrados: {links_data['metadata']['total_links_found']}")
    print(f"❌ Links quebrados: {links_data['metadata']['broken_links']}")
    print(f"✅ Links válidos: {links_data['metadata']['valid_links']}")
    print(f"📋 Relatório salvo: {report_path}")
    
    return links_data

def analyze_link(link_text, link_url, source_file, existing_files):
    """Analisa um link específico."""
    
    # Se é um link markdown [text](url)
    if link_url:
        target = link_url
        
        # Remover âncora se houver
        if '#' in target:
            target = target.split('#')[0]
        
        # Verificar se é um link interno
        if target.startswith('./') or target.startswith('../') or not target.startswith(('http', 'mailto', '#')):
            # Normalizar caminho
            if target.startswith('./'):
                target = target[2:]
            elif target.startswith('../'):
                # Simplificar para análise
                target = target[3:]
            
            # Verificar se o arquivo existe
            if target and not target.endswith('.md'):
                target += '.md'
            
            if target in existing_files:
                return {
                    "source_file": source_file,
                    "link_text": link_text,
                    "link_url": link_url,
                    "target": target,
                    "status": "valid",
                    "type": "markdown"
                }
            else:
                return {
                    "source_file": source_file,
                    "link_text": link_text,
                    "link_url": link_url,
                    "target": target,
                    "status": "broken",
                    "type": "markdown",
                    "suggestion": suggest_correction(target, existing_files)
                }
    
    # Se é um wiki link [[page]]
    elif link_text and not link_url:
        target = link_text + '.md'
        
        if target in existing_files:
            return {
                "source_file": source_file,
                "link_text": link_text,
                "link_url": None,
                "target": target,
                "status": "valid",
                "type": "wiki"
            }
        else:
            return {
                "source_file": source_file,
                "link_text": link_text,
                "link_url": None,
                "target": target,
                "status": "broken",
                "type": "wiki",
                "suggestion": suggest_correction(target, existing_files)
            }
    
    return None

def suggest_correction(target, existing_files):
    """Sugere correção para link quebrado."""
    
    # Remover extensão para comparação
    target_base = target.replace('.md', '')
    
    # Buscar arquivos similares
    suggestions = []
    
    for existing_file in existing_files:
        existing_base = existing_file.replace('.md', '')
        
        # Verificar se contém o nome do arquivo
        if target_base.lower() in existing_base.lower():
            suggestions.append(existing_file)
        
        # Verificar similaridade
        elif similar_strings(target_base, existing_base):
            suggestions.append(existing_file)
    
    return suggestions[:3]  # Retornar até 3 sugestões

def similar_strings(str1, str2):
    """Verifica se duas strings são similares."""
    str1_lower = str1.lower()
    str2_lower = str2.lower()
    
    # Verificar se uma contém a outra
    if str1_lower in str2_lower or str2_lower in str1_lower:
        return True
    
    # Verificar similaridade por palavras
    words1 = set(str1_lower.split('_'))
    words2 = set(str2_lower.split('_'))
    
    if words1 & words2:  # Intersecção
        return True
    
    return False

def generate_recommendations(links_data):
    """Gera recomendações para correção."""
    
    recommendations = []
    
    # Recomendações para links quebrados
    if links_data["broken_links"]:
        recommendations.append({
            "type": "broken_links",
            "priority": "high",
            "description": f"Corrigir {len(links_data['broken_links'])} links quebrados",
            "action": "Verificar e corrigir links quebrados identificados"
        })
    
    # Recomendações gerais
    recommendations.append({
        "type": "navigation",
        "priority": "medium",
        "description": "Melhorar navegação entre documentos",
        "action": "Adicionar links de navegação e índices"
    })
    
    links_data["recommendations"] = recommendations

if __name__ == "__main__":
    quick_deep_links_check() 