#!/usr/bin/env python3
"""
Script para extrair as recomendações de reorganização mais importantes do relatório de análise.
"""

import json
from pathlib import Path

def extract_recommendations():
    """Extrai as recomendações mais importantes para reorganização."""
    
    analysis_file = Path("wiki/maps/document_structure_analysis.json")
    
    if not analysis_file.exists():
        print("❌ Arquivo de análise não encontrado!")
        return
    
    try:
        with open(analysis_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Extrair recomendações
        recommendations = data.get("recommendations", [])
        
        # Ordenar por prioridade e tamanho
        high_priority = []
        medium_priority = []
        
        for rec in recommendations:
            if rec["priority"] == "alta":
                high_priority.append(rec)
            else:
                medium_priority.append(rec)
        
        # Ordenar por número de linhas (maior primeiro)
        high_priority.sort(key=lambda x: x["total_lines"], reverse=True)
        medium_priority.sort(key=lambda x: x["total_lines"], reverse=True)
        
        print("🎯 **RECOMENDAÇÕES DE REORGANIZAÇÃO**")
        print("=" * 50)
        
        print(f"\n📊 **ESTATÍSTICAS GERAIS**")
        print(f"Total de arquivos analisados: {data['metadata']['files_analyzed']}")
        print(f"Arquivos com seções longas: {data['metadata']['files_with_long_sections']}")
        print(f"Total de seções: {data['metadata']['total_sections']}")
        
        print(f"\n🔥 **PRIORIDADE ALTA** ({len(high_priority)} arquivos)")
        print("-" * 30)
        
        for i, rec in enumerate(high_priority[:10], 1):
            print(f"{i}. {rec['file']}")
            print(f"   📏 {rec['total_lines']} linhas, {rec['long_sections']} seções longas")
            print(f"   🎯 Ação: {rec['action']}")
            
            # Mostrar sugestões de estrutura
            for suggestion in rec['suggested_structure']:
                print(f"   📋 {suggestion['section']}: {suggestion['action']}")
                print(f"      Subseções sugeridas: {', '.join(suggestion['suggested_subseções'])}")
            print()
        
        if len(high_priority) > 10:
            print(f"... e mais {len(high_priority) - 10} arquivos")
        
        print(f"\n🟡 **PRIORIDADE MÉDIA** ({len(medium_priority)} arquivos)")
        print("-" * 30)
        
        for i, rec in enumerate(medium_priority[:5], 1):
            print(f"{i}. {rec['file']}")
            print(f"   📏 {rec['total_lines']} linhas, {rec['long_sections']} seções longas")
            print(f"   🎯 Ação: {rec['action']}")
            print()
        
        # Salvar resumo em arquivo separado
        summary = {
            "metadata": {
                "extraction_date": data["metadata"]["analysis_date"],
                "total_recommendations": len(recommendations),
                "high_priority_count": len(high_priority),
                "medium_priority_count": len(medium_priority)
            },
            "high_priority_files": high_priority[:15],
            "medium_priority_files": medium_priority[:10],
            "action_plan": {
                "phase_1": "Reorganizar arquivos com prioridade alta (>500 linhas)",
                "phase_2": "Reorganizar arquivos com prioridade alta (200-500 linhas)",
                "phase_3": "Reorganizar arquivos com prioridade média",
                "estimated_time": "16 horas total"
            }
        }
        
        summary_file = Path("wiki/maps/restructure_recommendations_summary.json")
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Resumo salvo em: {summary_file}")
        
        return summary
        
    except Exception as e:
        print(f"❌ Erro ao processar arquivo: {e}")
        return None

if __name__ == "__main__":
    extract_recommendations() 
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
- **Nome**: extract_restructure_recommendations
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

