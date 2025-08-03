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