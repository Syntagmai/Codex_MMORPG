#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BMAD System GUI - Módulo de Estilos Melhorado
Estilos simplificados e otimizados para melhor UX

Autor: Sistema BMAD - Codex MMORPG
Versão: 2.0.0 (UX Melhorada)
Data: 2025-08-01
"""

import tkinter as tk
from tkinter import ttk

class GUIStylesImproved:
    """Classe para gerenciar estilos melhorados da interface gráfica"""
    
    def __init__(self):
        """Inicializa o sistema de estilos melhorado"""
        self.style = ttk.Style()
        
        # Paleta de cores simplificada
        self.colors = {
            'primary': '#2563eb',      # Azul principal
            'secondary': '#64748b',     # Cinza neutro
            'success': '#059669',       # Verde sutil
            'danger': '#dc2626',        # Vermelho sutil
            'warning': '#d97706',       # Laranja sutil
            'background': '#ffffff',    # Fundo branco
            'surface': '#f8fafc',       # Superfície clara
            'text_primary': '#1e293b',  # Texto principal
            'text_secondary': '#64748b', # Texto secundário
            'border': '#e2e8f0',        # Bordas
            'hover': '#f1f5f9'          # Hover
        }
        
        # Sistema de tipografia
        self.typography = {
            'heading_large': ('Segoe UI', 24, 'bold'),
            'heading_medium': ('Segoe UI', 18, 'bold'),
            'heading_small': ('Segoe UI', 14, 'bold'),
            'body_large': ('Segoe UI', 16, 'normal'),
            'body_medium': ('Segoe UI', 14, 'normal'),
            'body_small': ('Segoe UI', 12, 'normal'),
            'caption': ('Segoe UI', 11, 'normal')
        }
        
        self.setup_light_theme()
    
    def setup_light_theme(self):
        """Configura o tema claro simplificado"""
        self.style.theme_use('clam')
        
        # Configurar cores principais
        self.style.configure('Title.TLabel', 
                           background=self.colors['background'], 
                           foreground=self.colors['text_primary'], 
                           font=self.typography['heading_medium'])
        
        self.style.configure('Subtitle.TLabel', 
                           background=self.colors['background'], 
                           foreground=self.colors['text_secondary'], 
                           font=self.typography['body_medium'])
        
        self.style.configure('Status.TLabel', 
                           background=self.colors['background'], 
                           foreground=self.colors['success'], 
                           font=self.typography['body_small'])
        
        # Estilos para botões simplificados
        self.style.configure('Primary.TButton',
                           background=self.colors['primary'],
                           foreground='white',
                           font=self.typography['body_medium'],
                           borderwidth=1,
                           relief='flat')
        
        self.style.configure('Secondary.TButton',
                           background=self.colors['secondary'],
                           foreground='white',
                           font=self.typography['body_medium'],
                           borderwidth=1,
                           relief='flat')
        
        self.style.configure('Success.TButton',
                           background=self.colors['success'],
                           foreground='white',
                           font=self.typography['body_medium'],
                           borderwidth=1,
                           relief='flat')
        
        self.style.configure('Danger.TButton',
                           background=self.colors['danger'],
                           foreground='white',
                           font=self.typography['body_medium'],
                           borderwidth=1,
                           relief='flat')
        
        # Estilos para Treeview
        self.style.configure('Clean.Treeview', 
                           background=self.colors['surface'], 
                           foreground=self.colors['text_primary'],
                           fieldbackground=self.colors['surface'],
                           borderwidth=1,
                           relief='flat')
        
        self.style.configure('Clean.Treeview.Heading', 
                           background=self.colors['background'], 
                           foreground=self.colors['text_primary'],
                           font=self.typography['body_small'],
                           borderwidth=1,
                           relief='flat')
        
        # Estilos para frames
        self.style.configure('Card.TFrame',
                           background=self.colors['surface'],
                           borderwidth=1,
                           relief='solid')
        
        self.style.configure('Sidebar.TFrame',
                           background=self.colors['background'],
                           borderwidth=1,
                           relief='solid')
    
    def create_simple_button(self, parent, text, command, button_type='primary', **kwargs):
        """Cria um botão com estilo simplificado"""
        button = tk.Button(
            parent,
            text=text,
            command=command,
            bg=self.colors[button_type],
            fg='white',
            font=self.typography['body_medium'],
            borderwidth=0,
            relief='flat',
            padx=16,
            pady=8,
            cursor='hand2',
            **kwargs
        )
        
        # Efeitos hover
        button.bind('<Enter>', lambda e: button.configure(bg=self.get_hover_color(button_type)))
        button.bind('<Leave>', lambda e: button.configure(bg=self.colors[button_type]))
        
        return button
    
    def get_hover_color(self, color_type):
        """Retorna cor de hover para o tipo especificado"""
        hover_colors = {
            'primary': '#1d4ed8',
            'secondary': '#475569',
            'success': '#047857',
            'danger': '#b91c1c',
            'warning': '#b45309'
        }
        return hover_colors.get(color_type, self.colors[color_type])
    
    def create_card(self, parent, title, content, **kwargs):
        """Cria um card informativo"""
        card_frame = ttk.Frame(parent, style='Card.TFrame')
        card_frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)
        
        # Título do card
        title_label = tk.Label(
            card_frame,
            text=title,
            font=self.typography['heading_small'],
            bg=self.colors['surface'],
            fg=self.colors['text_primary']
        )
        title_label.pack(anchor=tk.W, padx=12, pady=(12, 8))
        
        # Conteúdo do card
        content_label = tk.Label(
            card_frame,
            text=content,
            font=self.typography['body_medium'],
            bg=self.colors['surface'],
            fg=self.colors['text_secondary']
        )
        content_label.pack(anchor=tk.W, padx=12, pady=(0, 12))
        
        return card_frame
    
    def create_sidebar_button(self, parent, text, command, icon=None, **kwargs):
        """Cria um botão de sidebar"""
        button_frame = tk.Frame(parent, bg=self.colors['background'])
        button_frame.pack(fill=tk.X, padx=4, pady=2)
        
        button = tk.Button(
            button_frame,
            text=f"{icon} {text}" if icon else text,
            command=command,
            bg=self.colors['background'],
            fg=self.colors['text_primary'],
            font=self.typography['body_medium'],
            borderwidth=0,
            relief='flat',
            anchor=tk.W,
            padx=16,
            pady=12,
            cursor='hand2',
            **kwargs
        )
        button.pack(fill=tk.X)
        
        # Efeitos hover
        button.bind('<Enter>', lambda e: button.configure(bg=self.colors['hover']))
        button.bind('<Leave>', lambda e: button.configure(bg=self.colors['background']))
        
        return button
    
    def create_status_indicator(self, parent, status, **kwargs):
        """Cria um indicador de status"""
        status_colors = {
            'active': self.colors['success'],
            'inactive': self.colors['text_secondary'],
            'error': self.colors['danger'],
            'warning': self.colors['warning']
        }
        
        indicator = tk.Label(
            parent,
            text=f"● {status}",
            font=self.typography['body_small'],
            bg=self.colors['background'],
            fg=status_colors.get(status.lower(), self.colors['text_secondary']),
            **kwargs
        )
        
        return indicator
    
    def create_simple_label(self, parent, text, label_type='body', **kwargs):
        """Cria um label com tipografia consistente"""
        font_map = {
            'heading_large': self.typography['heading_large'],
            'heading_medium': self.typography['heading_medium'],
            'heading_small': self.typography['heading_small'],
            'body_large': self.typography['body_large'],
            'body_medium': self.typography['body_medium'],
            'body_small': self.typography['body_small'],
            'caption': self.typography['caption']
        }
        
        label = tk.Label(
            parent,
            text=text,
            font=font_map.get(label_type, self.typography['body_medium']),
            bg=self.colors['background'],
            fg=self.colors['text_primary'],
            **kwargs
        )
        
        return label
    
    def apply_light_theme_to_window(self, window):
        """Aplica o tema claro a uma janela"""
        window.configure(bg=self.colors['background'])
        
        # Configurar cores para widgets específicos
        for widget in window.winfo_children():
            if isinstance(widget, tk.Label):
                widget.configure(bg=self.colors['background'], fg=self.colors['text_primary'])
            elif isinstance(widget, tk.Frame):
                widget.configure(bg=self.colors['background'])
            elif isinstance(widget, tk.Button):
                # Manter cores dos botões como estão
                pass
    
    def create_clean_treeview(self, parent, columns, **kwargs):
        """Cria um Treeview com estilo limpo"""
        tree = ttk.Treeview(parent, columns=columns, show='headings', style='Clean.Treeview', **kwargs)
        
        # Configurar colunas
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150, anchor=tk.W)
        
        return tree
    
    def get_color(self, color_name):
        """Retorna uma cor específica da paleta"""
        return self.colors.get(color_name, self.colors['text_primary'])
    
    def get_font(self, font_type):
        """Retorna uma fonte específica do sistema"""
        return self.typography.get(font_type, self.typography['body_medium']) 