#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from unicode_aliases import *
"""
BMAD System GUI - Módulo de Configurações
Gerencia configurações do sistema na interface gráfica

Autor: Sistema BMAD - Codex MMORPG
Versão: 1.0.0
Data: 2025-08-01
"""

import tkinter as tk
from tkinter import ttk, filedialog
import json
import os
from pathlib import Path

class GUIConfig:
    """Classe para gerenciar configurações do sistema"""
    
    def __init__(self, parent, base_path, log_callback=None):
        """Inicializa o gerenciador de configurações"""
        self.parent = parent
        self.base_path = Path(base_path)
        self.config_path = self.base_path / "wiki" / "config"
        self.config_file = self.config_path / "bmad_gui_config.json"
        self.log_callback = log_callback
        self.agent_vars = {}
        
        # Garantir que o diretório existe
        self.config_path.mkdir(parents=True, exist_ok=True)
        
        # Carregar configurações padrão
        self.default_config = {
            'tema': 'Escuro',
            'timeout': 300,
            'execucao_paralela': 'Não',
            'logs_detalhados': 'Sim',
            'auto_save': 'Sim',
            'notificacoes': 'Sim',
            'max_agentes': 3,
            'intervalo_atualizacao': 1000,
            'limite_logs': 1000,
            'cache_config': 'Sim'
        }
        
        # Carregar configurações salvas ou usar padrões
        self.current_config = self.load_configurations()
    
    def create_config_window(self):
        """Cria janela de configurações"""
        config_window = tk.Toplevel(self.parent)
        config_window.title("⚙️ Configurações do Sistema BMAD")
        config_window.geometry("600x500")
        config_window.configure(bg='#2b2b2b')
        config_window.resizable(False, False)
        
        # Centralizar janela
        config_window.transient(self.parent)
        config_window.grab_set()
        
        # Frame principal
        main_frame = ttk.Frame(config_window)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título
        title_label = tk.Label(
            main_frame,
            text="⚙️ Configurações do Sistema BMAD",
            font=("Arial", 16, "bold"),
            bg='#2b2b2b',
            fg='#ffffff'
        )
        title_label.pack(pady=(0, 20))
        
        # Notebook para abas
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill=tk.BOTH, expand=True)
        
        # Aba Geral
        general_frame = ttk.Frame(notebook)
        notebook.add(general_frame, text=" Geral ")
        
        # Configurações gerais
        general_configs = [
            ("Tema da Interface", "tema", ["Escuro", "Claro"], "Escuro"),
            ("Timeout dos Agentes (segundos)", "timeout", [60, 120, 300, 600], 300),
            ("Execução Paralela", "execucao_paralela", ["Sim", "Não"], "Não"),
            ("Logs Detalhados", "logs_detalhados", ["Sim", "Não"], "Sim"),
            ("Auto-save", "auto_save", ["Sim", "Não"], "Sim"),
            ("Notificações", "notificacoes", ["Sim", "Não"], "Sim")
        ]
        
        for i, (label, key, options, default) in enumerate(general_configs):
            frame = ttk.Frame(general_frame)
            frame.pack(fill=tk.X, padx=10, pady=5)
            
            tk.Label(
                frame,
                text=label + ":",
                font=("Arial", 10),
                bg='#2b2b2b',
                fg='#ffffff'
            ).pack(side=tk.LEFT)
            
            if isinstance(options, list):
                var = tk.StringVar(value=self.current_config.get(key, default))
                combo = ttk.Combobox(
                    frame,
                    textvariable=var,
                    values=options,
                    state="readonly",
                    width=15
                )
                combo.pack(side=tk.RIGHT)
                setattr(self, f"config_{key}", var)
            else:
                var = tk.IntVar(value=self.current_config.get(key, default))
                spinbox = ttk.Spinbox(
                    frame,
                    from_=options[0],
                    to=options[1],
                    textvariable=var,
                    width=15
                )
                spinbox.pack(side=tk.RIGHT)
                setattr(self, f"config_{key}", var)
        
        # Aba Performance
        performance_frame = ttk.Frame(notebook)
        notebook.add(performance_frame, text=" Performance ")
        
        # Configurações de performance
        perf_configs = [
            ("Máximo de Agentes Simultâneos", "max_agentes", [1, 2, 3, 5, 10], 3),
            ("Intervalo de Atualização (ms)", "intervalo_atualizacao", [100, 500, 1000, 2000], 1000),
            ("Limite de Logs", "limite_logs", [100, 500, 1000, 2000], 1000),
            ("Cache de Configurações", "cache_config", ["Sim", "Não"], "Sim")
        ]
        
        for i, (label, key, options, default) in enumerate(perf_configs):
            frame = ttk.Frame(performance_frame)
            frame.pack(fill=tk.X, padx=10, pady=5)
            
            tk.Label(
                frame,
                text=label + ":",
                font=("Arial", 10),
                bg='#2b2b2b',
                fg='#ffffff'
            ).pack(side=tk.LEFT)
            
            if isinstance(options, list):
                var = tk.StringVar(value=self.current_config.get(key, default))
                combo = ttk.Combobox(
                    frame,
                    textvariable=var,
                    values=options,
                    state="readonly",
                    width=15
                )
                combo.pack(side=tk.RIGHT)
                setattr(self, f"config_{key}", var)
            else:
                var = tk.IntVar(value=self.current_config.get(key, default))
                spinbox = ttk.Spinbox(
                    frame,
                    from_=options[0],
                    to=options[1],
                    textvariable=var,
                    width=15
                )
                spinbox.pack(side=tk.RIGHT)
                setattr(self, f"config_{key}", var)
        
        # Aba Agentes
        agents_frame = ttk.Frame(notebook)
        notebook.add(agents_frame, text=" Agentes ")
        
        # Lista de agentes com checkboxes
        agents_label = tk.Label(
            agents_frame,
            text="Agentes Habilitados:",
            font=("Arial", 12, "bold"),
            bg='#2b2b2b',
            fg='#ffffff'
        )
        agents_label.pack(pady=(10, 10))
        
        # Frame com scroll para agentes
        agents_scroll_frame = ttk.Frame(agents_frame)
        agents_scroll_frame.pack(fill=tk.BOTH, expand=True, padx=10)
        
        canvas = tk.Canvas(agents_scroll_frame, bg='#2b2b2b', highlightthickness=0)
        scrollbar = ttk.Scrollbar(agents_scroll_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Lista de agentes padrão
        default_agents = [
            'Workflow Orchestrator', 'File Organization', 'Cleanup Agent',
            'Migration Agent', 'Structure Agent', 'Validation Agent',
            'Agents Orchestrator', 'Metrics Agent', 'Unified Validation',
            'Deep Source Analyzer', 'Knowledge Manager', 'Unified Research',
            'Alert Agent', 'Dashboard Agent', 'Quality Assurance', 'Documentation Agent'
        ]
        
        # Adicionar checkboxes para agentes
        self.agent_vars = {}
        for agent in default_agents:
            var = tk.BooleanVar(value=True)
            self.agent_vars[agent] = var
            
            checkbox = tk.Checkbutton(
                scrollable_frame,
                text=agent,
                variable=var,
                font=("Arial", 10),
                bg='#2b2b2b',
                fg='#ffffff',
                selectcolor='#4CAF50',
                activebackground='#2b2b2b',
                activeforeground='#ffffff'
            )
            checkbox.pack(anchor=tk.W, padx=10, pady=2)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Botões de ação
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(fill=tk.X, pady=(20, 0))
        
        # Botão Salvar
        save_btn = tk.Button(
            buttons_frame,
            text="💾 Salvar Configurações",
            command=lambda: self.save_configurations(config_window),
            bg='#4CAF50',
            fg='white',
            font=("Arial", 12, "bold"),
            height=2
        )
        save_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Botão Carregar
        load_btn = tk.Button(
            buttons_frame,
            text="📂 Carregar Configurações",
            command=self.load_configurations,
            bg='#2196F3',
            fg='white',
            font=("Arial", 12, "bold"),
            height=2
        )
        load_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Botão Padrão
        default_btn = tk.Button(
            buttons_frame,
            text="🔄 Restaurar Padrões",
            command=self.reset_to_defaults,
            bg='#FF9800',
            fg='white',
            font=("Arial", 12, "bold"),
            height=2
        )
        default_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Botão Cancelar
        cancel_btn = tk.Button(
            buttons_frame,
            text="❌ Cancelar",
            command=config_window.destroy,
            bg='#f44336',
            fg='white',
            font=("Arial", 12, "bold"),
            height=2
        )
        cancel_btn.pack(side=tk.RIGHT)
        
        return config_window
    
    def save_configurations(self, config_window=None):
        """Salva as configurações atuais"""
        try:
            # Coletar configurações dos widgets
            config_data = {}
            
            # Configurações gerais
            for key in ['tema', 'execucao_paralela', 'logs_detalhados', 'auto_save', 'notificacoes', 'cache_config']:
                var = getattr(self, f"config_{key}", None)
                if var:
                    config_data[key] = var.get()
            
            # Configurações numéricas
            for key in ['timeout', 'max_agentes', 'intervalo_atualizacao', 'limite_logs']:
                var = getattr(self, f"config_{key}", None)
                if var:
                    config_data[key] = var.get()
            
            # Configurações de agentes
            config_data['agentes_habilitados'] = {
                agent: var.get() for agent, var in self.agent_vars.items()
            }
            
            # Salvar arquivo
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config_data, f, indent=2, ensure_ascii=False)
            
            # Atualizar configuração atual
            self.current_config = config_data
            
            if self.log_callback:
                self.log_callback("💾 Configurações salvas com sucesso", "SUCCESS")
            
            if config_window:
                config_window.destroy()
                
        except Exception as e:
            if self.log_callback:
                self.log_callback(f"❌ Erro ao salvar configurações: {e}", "ERROR")
    
    def load_configurations(self):
        """Carrega configurações salvas"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config_data = json.load(f)
                
                if self.log_callback:
                    self.log_callback("📂 Configurações carregadas com sucesso", "SUCCESS")
                
                return config_data
            else:
                if self.log_callback:
                    self.log_callback("📂 Usando configurações padrão", "INFO")
                
                return self.default_config.copy()
                
        except Exception as e:
            if self.log_callback:
                self.log_callback(f"❌ Erro ao carregar configurações: {e}", "ERROR")
            
            return self.default_config.copy()
    
    def reset_to_defaults(self):
        """Restaura configurações padrão"""
        try:
            # Restaurar valores padrão nos widgets
            for key, value in self.default_config.items():
                var = getattr(self, f"config_{key}", None)
                if var:
                    var.set(value)
            
            # Restaurar agentes
            for agent, var in self.agent_vars.items():
                var.set(True)
            
            if self.log_callback:
                self.log_callback("🔄 Configurações restauradas para padrão", "SUCCESS")
                
        except Exception as e:
            if self.log_callback:
                self.log_callback(f"❌ Erro ao restaurar configurações: {e}", "ERROR")
    
    def get_config(self, key, default=None):
        """Obtém valor de uma configuração específica"""
        return self.current_config.get(key, default)
    
    def set_config(self, key, value):
        """Define valor de uma configuração específica"""
        self.current_config[key] = value
    
    def get_enabled_agents(self):
        """Retorna lista de agentes habilitados"""
        enabled = []
        for agent, var in self.agent_vars.items():
            if var.get():
                enabled.append(agent)
        return enabled 