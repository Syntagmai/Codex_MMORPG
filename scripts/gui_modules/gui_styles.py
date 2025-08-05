#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BMAD System GUI - Módulo de Estilos
Gerencia estilos e temas da interface gráfica

Autor: Sistema BMAD - Codex MMORPG
Versão: 1.0.0
Data: 2025-08-01
"""

import tkinter as tk
from tkinter import ttk

class GUIStyles:
    """Classe para gerenciar estilos da interface gráfica"""
    
    def __init__(self):
        """Inicializa o sistema de estilos"""
        self.style = ttk.Style()
        self.setup_dark_theme()
    
    def setup_dark_theme(self):
        """Configura o tema escuro da interface"""
        self.style.theme_use('clam')
        
        # Configurar cores principais
        self.style.configure('Title.TLabel', 
                           background='#2b2b2b', 
                           foreground='#ffffff', 
                           font=('Arial', 16, 'bold'))
        
        self.style.configure('Status.TLabel', 
                           background='#2b2b2b', 
                           foreground='#00ff00', 
                           font=('Arial', 10))
        
        self.style.configure('Agent.Treeview', 
                           background='#3c3c3c', 
                           foreground='#ffffff',
                           fieldbackground='#3c3c3c')
        
        self.style.configure('Agent.Treeview.Heading', 
                           background='#4c4c4c', 
                           foreground='#ffffff',
                           font=('Arial', 10, 'bold'))
        
        # Configurar cores para botões
        self.style.configure('Success.TButton',
                           background='#4CAF50',
                           foreground='white',
                           font=('Arial', 12, 'bold'))
        
        self.style.configure('Danger.TButton',
                           background='#f44336',
                           foreground='white',
                           font=('Arial', 12, 'bold'))
        
        self.style.configure('Warning.TButton',
                           background='#FF9800',
                           foreground='white',
                           font=('Arial', 12, 'bold'))
        
        self.style.configure('Info.TButton',
                           background='#2196F3',
                           foreground='white',
                           font=('Arial', 12, 'bold'))
        
        self.style.configure('Purple.TButton',
                           background='#9C27B0',
                           foreground='white',
                           font=('Arial', 12, 'bold'))
    
    def get_button_style(self, button_type):
        """Retorna o estilo apropriado para botões"""
        styles = {
            'success': {'bg': '#4CAF50', 'fg': 'white'},
            'danger': {'bg': '#f44336', 'fg': 'white'},
            'warning': {'bg': '#FF9800', 'fg': 'white'},
            'info': {'bg': '#2196F3', 'fg': 'white'},
            'purple': {'bg': '#9C27B0', 'fg': 'white'},
            'gray': {'bg': '#607D8B', 'fg': 'white'}
        }
        return styles.get(button_type, styles['info'])
    
    def apply_dark_theme_to_window(self, window):
        """Aplica o tema escuro a uma janela específica"""
        window.configure(bg='#2b2b2b')
        
        # Configurar cores para widgets específicos
        for widget in window.winfo_children():
            if isinstance(widget, tk.Label):
                widget.configure(bg='#2b2b2b', fg='#ffffff')
            elif isinstance(widget, tk.Frame):
                widget.configure(bg='#2b2b2b')
    
    def create_styled_button(self, parent, text, command, button_type='info', **kwargs):
        """Cria um botão com estilo predefinido"""
        style = self.get_button_style(button_type)
        
        button = tk.Button(
            parent,
            text=text,
            command=command,
            bg=style['bg'],
            fg=style['fg'],
            font=("Arial", 12, "bold"),
            height=2,
            **kwargs
        )
        
        return button 