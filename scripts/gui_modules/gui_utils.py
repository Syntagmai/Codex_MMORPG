#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BMAD System GUI - Módulo de Utilitários
Funções utilitárias para a interface gráfica

Autor: Sistema BMAD - Codex MMORPG
Versão: 1.0.0
Data: 2025-08-01
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime
import json
import os
from pathlib import Path

class GUIUtils:
    """Classe com utilitários para a interface gráfica"""
    
    @staticmethod
    def center_window(window, width=None, height=None):
        """Centraliza uma janela na tela"""
        window.update_idletasks()
        
        if width is None:
            width = window.winfo_width()
        if height is None:
            height = window.winfo_height()
        
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        
        window.geometry(f'{width}x{height}+{x}+{y}')
    
    @staticmethod
    def create_scrolled_text(parent, height=15, **kwargs):
        """Cria um widget de texto com scroll"""
        default_kwargs = {
            'height': height,
            'bg': '#1e1e1e',
            'fg': '#ffffff',
            'font': ("Consolas", 10),
            'insertbackground': '#ffffff'
        }
        default_kwargs.update(kwargs)
        
        return scrolledtext.ScrolledText(parent, **default_kwargs)
    
    @staticmethod
    def create_label(parent, text, **kwargs):
        """Cria um label com estilo padrão"""
        default_kwargs = {
            'font': ("Arial", 10),
            'bg': '#2b2b2b',
            'fg': '#ffffff'
        }
        default_kwargs.update(kwargs)
        
        return tk.Label(parent, text=text, **default_kwargs)
    
    @staticmethod
    def create_title_label(parent, text, **kwargs):
        """Cria um label de título com estilo padrão"""
        default_kwargs = {
            'font': ("Arial", 16, "bold"),
            'bg': '#2b2b2b',
            'fg': '#ffffff'
        }
        default_kwargs.update(kwargs)
        
        return tk.Label(parent, text=text, **default_kwargs)
    
    @staticmethod
    def create_subtitle_label(parent, text, **kwargs):
        """Cria um label de subtítulo com estilo padrão"""
        default_kwargs = {
            'font': ("Arial", 12),
            'bg': '#2b2b2b',
            'fg': '#cccccc'
        }
        default_kwargs.update(kwargs)
        
        return tk.Label(parent, text=text, **default_kwargs)
    
    @staticmethod
    def format_timestamp():
        """Formata timestamp atual para logs"""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def get_level_color(level):
        """Retorna cor apropriada para nível de log"""
        colors = {
            'INFO': '#00ff00',
            'WARNING': '#FF9800',
            'ERROR': '#f44336',
            'SUCCESS': '#4CAF50',
            'SYSTEM': '#2196F3'
        }
        return colors.get(level, '#ffffff')
    
    @staticmethod
    def show_info_message(title, message):
        """Mostra mensagem de informação"""
        messagebox.showinfo(title, message)
    
    @staticmethod
    def show_error_message(title, message):
        """Mostra mensagem de erro"""
        messagebox.showerror(title, message)
    
    @staticmethod
    def show_warning_message(title, message):
        """Mostra mensagem de aviso"""
        messagebox.showwarning(title, message)
    
    @staticmethod
    def ask_yes_no(title, message):
        """Pergunta sim/não ao usuário"""
        return messagebox.askyesno(title, message)
    
    @staticmethod
    def load_json_file(file_path):
        """Carrega arquivo JSON com tratamento de erro"""
        try:
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return {}
        except Exception as e:
            print(f"Erro ao carregar arquivo JSON {file_path}: {e}")
            return {}
    
    @staticmethod
    def save_json_file(file_path, data):
        """Salva dados em arquivo JSON com tratamento de erro"""
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Erro ao salvar arquivo JSON {file_path}: {e}")
            return False
    
    @staticmethod
    def ensure_directory(path):
        """Garante que um diretório existe"""
        Path(path).mkdir(parents=True, exist_ok=True)
        return Path(path)
    
    @staticmethod
    def format_file_size(size_bytes):
        """Formata tamanho de arquivo em bytes para formato legível"""
        if size_bytes == 0:
            return "0 B"
        
        size_names = ["B", "KB", "MB", "GB", "TB"]
        i = 0
        while size_bytes >= 1024 and i < len(size_names) - 1:
            size_bytes /= 1024.0
            i += 1
        
        return f"{size_bytes:.1f} {size_names[i]}"
    
    @staticmethod
    def truncate_text(text, max_length=50):
        """Trunca texto se exceder o comprimento máximo"""
        if len(text) <= max_length:
            return text
        return text[:max_length-3] + "..." 