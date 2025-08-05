#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para resolver problemas de encoding de emojis/emoticons no Windows
Cria aliases para emojis e configura encoding UTF-8 automaticamente

Autor: Sistema BMAD - Codex MMORPG
Versão: 1.0.0
Data: 2025-08-01
"""

import os
import sys
import re
from pathlib import Path

# Configurar encoding UTF-8 para o console
def setup_unicode_console():
    """Configura o console para suportar Unicode/UTF-8"""
    if sys.platform == "win32":
        try:
            # Tentar configurar UTF-8 no Windows
            os.system("chcp 65001 > nul")
            # Configurar stdout para UTF-8
            sys.stdout.reconfigure(encoding='utf-8')
            sys.stderr.reconfigure(encoding='utf-8')
        except:
            pass

# Dicionário de aliases para emojis
EMOJI_ALIASES = {
    '✅': '[OK]',
    '❌': '[ERRO]',
    '⚠️': '[AVISO]',
    '🎯': '[ALVO]',
    '🚀': '[FOGUETE]',
    '📋': '[CLIPBOARD]',
    '🔧': '[FERRAMENTA]',
    '📁': '[PASTA]',
    '🎨': '[ARTE]',
    '📊': '[GRAFICO]',
    '🔗': '[LINK]',
    '📝': '[NOTA]',
    '🔄': '[ATUALIZAR]',
    '🧪': '[TESTE]',
    '📚': '[LIVRO]',
    '🤖': '[ROBO]',
    '⚡': '[RAIO]',
    '🔥': '[FOGO]',
    '🟡': '[AMARELO]',
    '🔵': '[AZUL]',
    '📖': '[LIVRO]',
    '🧩': '[PUZZLE]',
    '🎉': '[FESTA]',
    '📈': '[CRESCER]',
    '📉': '[DIMINUIR]',
    '💡': '[IDEA]',
    '🔍': '[LENTE]',
    '🎪': '[CIRCO]',
    '📦': '[CAIXA]',
    '🐍': '[PYTHON]',
    '🎪': '[CIRCO]',
    '📦': '[CAIXA]',
    '🐍': '[PYTHON]',
    '🎨': '[ARTE]',
    '🔧': '[FERRAMENTA]',
    '📊': '[GRAFICO]',
    '🔗': '[LINK]',
    '📝': '[NOTA]',
    '🔄': '[ATUALIZAR]',
    '🧪': '[TESTE]',
    '📚': '[LIVRO]',
    '🤖': '[ROBO]',
    '⚡': '[RAIO]',
    '🔥': '[FOGO]',
    '🟡': '[AMARELO]',
    '🔵': '[AZUL]',
    '📖': '[LIVRO]',
    '🧩': '[PUZZLE]',
    '🎉': '[FESTA]',
    '📈': '[CRESCER]',
    '📉': '[DIMINUIR]',
    '💡': '[IDEA]',
    '🔍': '[LENTE]',
    '🎪': '[CIRCO]',
    '📦': '[CAIXA]',
    '🐍': '[PYTHON]'
}

def create_emoji_aliases():
    """Cria arquivo com aliases de emojis"""
    alias_content = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aliases para emojis - Resolve problemas de encoding no Windows
Importe este arquivo no início dos seus scripts Python

Uso:
    from unicode_aliases import *
    print(OK + " Sucesso!")
    print(ERRO + " Erro encontrado!")
"""

# Configurar encoding UTF-8
import sys
import os

if sys.platform == "win32":
    try:
        os.system("chcp 65001 > nul")
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except:
        pass

# Aliases para emojis
OK = "✅"
ERRO = "❌"
AVISO = "⚠️"
ALVO = "🎯"
FOGUETE = "🚀"
CLIPBOARD = "📋"
FERRAMENTA = "🔧"
PASTA = "📁"
ARTE = "🎨"
GRAFICO = "📊"
LINK = "🔗"
NOTA = "📝"
ATUALIZAR = "🔄"
TESTE = "🧪"
LIVRO = "📚"
ROBO = "🤖"
RAIO = "⚡"
FOGO = "🔥"
AMARELO = "🟡"
AZUL = "🔵"
PUZZLE = "🧩"
FESTA = "🎉"
CRESCER = "📈"
DIMINUIR = "📉"
IDEA = "💡"
LENTE = "🔍"
CIRCO = "🎪"
CAIXA = "📦"
PYTHON = "🐍"

# Função para print seguro
def safe_print(text):
    """Print que funciona em qualquer encoding"""
    try:
        print(text)
    except UnicodeEncodeError:
        # Fallback para texto sem emojis
        for emoji, alias in {
            '✅': '[OK]', '❌': '[ERRO]', '⚠️': '[AVISO]', '🎯': '[ALVO]',
            '🚀': '[FOGUETE]', '📋': '[CLIPBOARD]', '🔧': '[FERRAMENTA]',
            '📁': '[PASTA]', '🎨': '[ARTE]', '📊': '[GRAFICO]', '🔗': '[LINK]',
            '📝': '[NOTA]', '🔄': '[ATUALIZAR]', '🧪': '[TESTE]', '📚': '[LIVRO]',
            '🤖': '[ROBO]', '⚡': '[RAIO]', '🔥': '[FOGO]', '🟡': '[AMARELO]',
            '🔵': '[AZUL]', '🧩': '[PUZZLE]', '🎉': '[FESTA]', '📈': '[CRESCER]',
            '📉': '[DIMINUIR]', '💡': '[IDEA]', '🔍': '[LENTE]', '🎪': '[CIRCO]',
            '📦': '[CAIXA]', '🐍': '[PYTHON]'
        }.items():
            text = text.replace(emoji, alias)
        print(text)

# Função para detectar se o console suporta emojis
def supports_emojis():
    """Verifica se o console suporta emojis"""
    try:
        print("✅", end="")
        return True
    except UnicodeEncodeError:
        return False

# Configuração automática
if not supports_emojis():
    # Se não suporta emojis, usar aliases
    for key, value in globals().copy().items():
        if isinstance(value, str) and len(value) == 1 and ord(value) > 127:
            globals()[key] = f"[{key}]"
'''
    
    with open('unicode_aliases.py', 'w', encoding='utf-8') as f:
        f.write(alias_content)
    
    print("✅ Arquivo unicode_aliases.py criado")

def fix_python_files():
    """Adiciona import de unicode_aliases em todos os arquivos Python"""
    python_files = []
    
    # Encontrar todos os arquivos Python
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.py') and file != 'unicode_fix.py' and file != 'unicode_aliases.py':
                python_files.append(os.path.join(root, file))
    
    print(f"🔍 Encontrados {len(python_files)} arquivos Python")
    
    fixed_count = 0
    for file_path in python_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Verificar se já tem o import
            if 'from unicode_aliases import' in content or 'import unicode_aliases' in content:
                continue
            
            # Verificar se tem emojis
            has_emojis = any(emoji in content for emoji in EMOJI_ALIASES.keys())
            
            if has_emojis:
                # Adicionar import no início do arquivo
                lines = content.split('\n')
                
                # Encontrar onde adicionar o import (após shebang e encoding)
                insert_index = 0
                for i, line in enumerate(lines):
                    if line.startswith('#!') or line.startswith('# -*- coding:'):
                        insert_index = i + 1
                    elif line.strip() and not line.startswith('#'):
                        break
                
                # Adicionar import
                lines.insert(insert_index, 'from unicode_aliases import *')
                
                # Reescrever arquivo
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(lines))
                
                fixed_count += 1
                print(f"✅ Corrigido: {file_path}")
                
        except Exception as e:
            print(f"❌ Erro ao corrigir {file_path}: {e}")
    
    print(f"📊 Total de arquivos corrigidos: {fixed_count}")

def create_quick_fix():
    """Cria script de correção rápida"""
    quick_fix_content = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correção rápida para problemas de encoding de emojis
Execute este script antes de rodar qualquer script Python

Uso:
    python quick_unicode_fix.py
"""

import os
import sys

def fix_console():
    """Configura console para UTF-8"""
    if sys.platform == "win32":
        try:
            os.system("chcp 65001 > nul")
            sys.stdout.reconfigure(encoding='utf-8')
            sys.stderr.reconfigure(encoding='utf-8')
            print("✅ Console configurado para UTF-8")
        except:
            print("⚠️ Não foi possível configurar UTF-8 automaticamente")
            print("💡 Execute: chcp 65001")

def safe_print(text):
    """Print seguro para emojis"""
    try:
        print(text)
    except UnicodeEncodeError:
        # Substituir emojis por texto
        replacements = {
            '✅': '[OK]', '❌': '[ERRO]', '⚠️': '[AVISO]', '🎯': '[ALVO]',
            '🚀': '[FOGUETE]', '📋': '[CLIPBOARD]', '🔧': '[FERRAMENTA]',
            '📁': '[PASTA]', '🎨': '[ARTE]', '📊': '[GRAFICO]', '🔗': '[LINK]',
            '📝': '[NOTA]', '🔄': '[ATUALIZAR]', '🧪': '[TESTE]', '📚': '[LIVRO]',
            '🤖': '[ROBO]', '⚡': '[RAIO]', '🔥': '[FOGO]', '🟡': '[AMARELO]',
            '🔵': '[AZUL]', '🧩': '[PUZZLE]', '🎉': '[FESTA]', '📈': '[CRESCER]',
            '📉': '[DIMINUIR]', '💡': '[IDEA]', '🔍': '[LENTE]', '🎪': '[CIRCO]',
            '📦': '[CAIXA]', '🐍': '[PYTHON]'
        }
        for emoji, alias in replacements.items():
            text = text.replace(emoji, alias)
        print(text)

if __name__ == "__main__":
    fix_console()
    safe_print("🎉 Sistema de correção Unicode ativado!")
    safe_print("💡 Agora você pode executar scripts com emojis sem problemas")
'''
    
    with open('quick_unicode_fix.py', 'w', encoding='utf-8') as f:
        f.write(quick_fix_content)
    
    print("✅ Script quick_unicode_fix.py criado")

def main():
    """Função principal"""
    print("🔧 CORREÇÃO DE ENCODING UNICODE")
    print("=" * 40)
    
    # Configurar console
    setup_unicode_console()
    
    # Criar aliases
    create_emoji_aliases()
    
    # Corrigir arquivos Python
    fix_python_files()
    
    # Criar script de correção rápida
    create_quick_fix()
    
    print("\n🎉 CORREÇÃO CONCLUÍDA!")
    print("\n📋 COMO USAR:")
    print("1. Execute: python quick_unicode_fix.py")
    print("2. Ou adicione no início dos scripts: from unicode_aliases import *")
    print("3. Ou use: safe_print('✅ Sucesso!')")
    
    print("\n💡 DICA: Execute 'python quick_unicode_fix.py' antes de rodar qualquer script!")

if __name__ == "__main__":
    main() 