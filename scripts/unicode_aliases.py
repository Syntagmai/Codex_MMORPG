#!/usr/bin/env python3
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
