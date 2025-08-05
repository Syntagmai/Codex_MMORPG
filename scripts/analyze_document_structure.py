#!/usr/bin/env python3
"""
Script para analisar a estrutura dos documentos da wiki e identificar seções muito longas.
Identifica documentos com mais de 200 linhas e propõe reorganização.
"""

import os
import re
import json
from datetime import datetime
from pathlib import Path

def analyze_document_structure():
    """Analisa a estrutura dos documentos da wiki."""
    
    wiki_path = Path("wiki")
    report_path = Path("wiki/maps/document_structure_analysis.json")
    
    # Padrões para identificar seções
    section_patterns = [
        r'^#{1,6}\s+(.+)$',  # Títulos (# ## ### etc)
        r'^---$',            # Separadores
        r'^> \[!.*\]',       # Callouts
    ]
    
    analysis_results = {
        "metadata": {
            "analysis_date": datetime.now().isoformat(),
            "total_files": 0,
            "files_analyzed": 0,
            "files_with_long_sections": 0,
            "total_sections": 0
        },
        "files_analysis": {},
        "recommendations": []
    }
    
    print("🔍 Analisando estrutura dos documentos da wiki...")
    
    # Analisar todos os arquivos .md na wiki
    for md_file in wiki_path.rglob("*.md"):
        if md_file.is_file():
            analysis_results["metadata"]["total_files"] += 1
            
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    lines = content.split('\n')
                    
                file_analysis = {
                    "file_path": str(md_file.relative_to(wiki_path)),
                    "total_lines": len(lines),
                    "sections": [],
                    "long_sections": [],
                    "needs_restructuring": False
                }
                
                # Identificar seções
                current_section = None
                section_start = 0
                section_lines = 0
                
                for i, line in enumerate(lines):
                    # Verificar se é início de nova seção
                    is_section_start = False
                    section_level = 0
                    section_title = ""
                    
                    for pattern in section_patterns:
                        match = re.match(pattern, line)
                        if match:
                            is_section_start = True
                            if pattern == r'^#{1,6}\s+(.+)$':
                                section_level = len(line) - len(line.lstrip('#'))
                                section_title = match.group(1).strip()
                            break
                    
                    if is_section_start:
                        # Finalizar seção anterior
                        if current_section and section_lines > 0:
                            current_section["end_line"] = i - 1
                            current_section["line_count"] = section_lines
                            
                            if section_lines > 200:
                                current_section["is_long"] = True
                                file_analysis["long_sections"].append(current_section)
                                file_analysis["needs_restructuring"] = True
                            
                            file_analysis["sections"].append(current_section)
                        
                        # Iniciar nova seção
                        current_section = {
                            "title": section_title,
                            "level": section_level,
                            "start_line": i,
                            "end_line": len(lines) - 1,
                            "line_count": 0,
                            "is_long": False
                        }
                        section_start = i
                        section_lines = 0
                    else:
                        section_lines += 1
                
                # Finalizar última seção
                if current_section and section_lines > 0:
                    current_section["end_line"] = len(lines) - 1
                    current_section["line_count"] = section_lines
                    
                    if section_lines > 200:
                        current_section["is_long"] = True
                        file_analysis["long_sections"].append(current_section)
                        file_analysis["needs_restructuring"] = True
                    
                    file_analysis["sections"].append(current_section)
                
                # Estatísticas do arquivo
                file_analysis["total_sections"] = len(file_analysis["sections"])
                file_analysis["long_sections_count"] = len(file_analysis["long_sections"])
                
                analysis_results["files_analysis"][str(md_file.relative_to(wiki_path))] = file_analysis
                analysis_results["metadata"]["files_analyzed"] += 1
                
                if file_analysis["needs_restructuring"]:
                    analysis_results["metadata"]["files_with_long_sections"] += 1
                
                analysis_results["metadata"]["total_sections"] += file_analysis["total_sections"]
                
                # Gerar recomendações
                if file_analysis["needs_restructuring"]:
                    recommendation = {
                        "file": str(md_file.relative_to(wiki_path)),
                        "total_lines": file_analysis["total_lines"],
                        "long_sections": len(file_analysis["long_sections"]),
                        "action": "reorganize",
                        "priority": "alta" if file_analysis["total_lines"] > 500 else "média",
                        "suggested_structure": generate_suggested_structure(file_analysis)
                    }
                    analysis_results["recommendations"].append(recommendation)
                
                print(f"📄 {md_file.name}: {len(lines)} linhas, {file_analysis['total_sections']} seções")
                
            except Exception as e:
                print(f"❌ Erro ao analisar {md_file}: {e}")
    
    # Salvar relatório
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(analysis_results, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Análise concluída!")
    print(f"📊 Arquivos analisados: {analysis_results['metadata']['files_analyzed']}")
    print(f"📊 Arquivos com seções longas: {analysis_results['metadata']['files_with_long_sections']}")
    print(f"📊 Total de seções: {analysis_results['metadata']['total_sections']}")
    print(f"📄 Relatório salvo: {report_path}")
    
    return analysis_results

def generate_suggested_structure(file_analysis):
    """Gera sugestão de estrutura para reorganização."""
    
    suggestions = []
    
    for section in file_analysis["long_sections"]:
        if section["line_count"] > 300:
            # Seção muito longa - dividir em subseções
            suggestions.append({
                "section": section["title"],
                "action": "dividir_em_subseções",
                "suggested_subseções": [
                    "Conceitos",
                    "Implementação", 
                    "Exemplos",
                    "Referência"
                ]
            })
        elif section["line_count"] > 200:
            # Seção longa - adicionar subseções
            suggestions.append({
                "section": section["title"],
                "action": "adicionar_subseções",
                "suggested_subseções": [
                    "Visão Geral",
                    "Detalhes",
                    "Exemplos"
                ]
            })
    
    return suggestions

if __name__ == "__main__":
    analyze_document_structure() 
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
- **Nome**: analyze_document_structure
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

