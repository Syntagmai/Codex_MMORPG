# Constantes
MAX_RETRIES = 8

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: remove_emojis.py
Módulo de Destino: documentation.markdown_processor
Data de Migração: 2025-08-01 12:21:35

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import MarkdownprocessorModule

# Conteúdo original do script
#!/usr/bin/env python3
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

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = MarkdownprocessorModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script remove_emojis.py executado com sucesso via módulo documentation.markdown_processor")
    else:
        print(f"❌ Erro na execução do script remove_emojis.py via módulo documentation.markdown_processor")
