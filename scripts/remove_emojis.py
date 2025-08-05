#!/usr/bin/env python3
from unicode_aliases import *
"""
Script para remover emojis dos scripts de indexação
"""
import os
import re

def remove_emojis_from_file(file_path):
    """Remove emojis de um arquivo"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remover emojis comuns
        content = re.sub(r'[🚀🔄📁✅❌⚠️🔍⚙️📋🎯📚🎨📝🔗📎💡🔧⚡💰🎉📊⏱️⚡]', '', content)

        # Remover códigos Unicode de emojis
        content = re.sub(r'\\U0001f680', '', content)  # 🚀
        content = re.sub(r'\\U0001f504', '', content)  # 🔄
        content = re.sub(r'\\U0001f4c1', '', content)  # 📁
        content = re.sub(r'\\U00002705', '', content)  # ✅
        content = re.sub(r'\\U0000274c', '', content)  # ❌
        content = re.sub(r'\\U000026a0', '', content)  # ⚠️

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Emojis removidos de {file_path}")

    except Exception as e:
        print(f"Erro ao processar {file_path}: {e}")

def main():
    """Função principal"""
    scripts = [
        "wiki/update/update_source_index.py",
        "wiki/update/update_habdel_index.py",
        "wiki/update/update_modules_index.py",
        "wiki/update/update_styles_index.py",
        "wiki/update/update_resources_index.py",
        "wiki/update/update_tools_index.py",
        "wiki/update/auto_update_all_maps.py"
    ]

    for script in scripts:
        if os.path.exists(script):
            remove_emojis_from_file(script)
        else:
            print(f"Arquivo {script} não encontrado")

if __name__ == "__main__":
    main() 
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
- **Nome**: remove_emojis
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

