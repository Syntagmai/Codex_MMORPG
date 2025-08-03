#!/usr/bin/env python3
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
