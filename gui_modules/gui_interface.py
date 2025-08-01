#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BMAD System GUI - Módulo de Interface Principal
Interface principal da aplicação

Autor: Sistema BMAD - Codex MMORPG
Versão: 1.0.0
Data: 2025-08-01
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
from datetime import datetime
import queue
import threading
from pathlib import Path

class GUIInterface:
    """Classe para gerenciar a interface principal"""
    
    def __init__(self, parent, base_path, log_callback=None):
        """Inicializa a interface principal"""
        self.parent = parent
        self.base_path = Path(base_path)
        self.log_callback = log_callback
        self.log_text = None
        self.stats_label = None
        self.status_var = None
        
    def create_main_interface(self):
        """Cria a interface principal"""
        # Frame principal
        main_frame = ttk.Frame(self.parent)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Título
        title_label = tk.Label(
            main_frame, 
            text="🧠 BMAD System - Sistema de Aprendizado Inteligente",
            font=("Arial", 18, "bold"),
            bg='#2b2b2b',
            fg='#ffffff'
        )
        title_label.pack(pady=(0, 20))
        
        # Subtítulo
        subtitle_label = tk.Label(
            main_frame,
            text="Interface Gráfica Unificada para Controle Total do Sistema BMAD",
            font=("Arial", 12),
            bg='#2b2b2b',
            fg='#cccccc'
        )
        subtitle_label.pack(pady=(0, 20))
        
        # Frame superior com controles
        control_frame = ttk.LabelFrame(main_frame, text="🎯 Controles do Sistema", padding=15)
        control_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Botões de ação rápida
        quick_actions_frame = ttk.Frame(control_frame)
        quick_actions_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Botão de ativação completa
        self.activate_all_btn = tk.Button(
            quick_actions_frame,
            text="🚀 ATIVAR SISTEMA COMPLETO",
            command=self.activate_complete_system,
            bg='#4CAF50',
            fg='white',
            font=("Arial", 14, "bold"),
            height=2,
            width=25
        )
        self.activate_all_btn.pack(side=tk.LEFT, padx=(0, 15))
        
        # Botão de parar
        self.stop_btn = tk.Button(
            quick_actions_frame,
            text="⏹️ PARAR SISTEMA",
            command=self.stop_all_tasks,
            bg='#f44336',
            fg='white',
            font=("Arial", 14, "bold"),
            height=2,
            width=20
        )
        self.stop_btn.pack(side=tk.LEFT, padx=(0, 15))
        
        # Botão de limpar logs
        self.clear_logs_btn = tk.Button(
            quick_actions_frame,
            text="🗑️ LIMPAR LOGS",
            command=self.clear_logs,
            bg='#FF9800',
            fg='white',
            font=("Arial", 14, "bold"),
            height=2,
            width=15
        )
        self.clear_logs_btn.pack(side=tk.LEFT, padx=(0, 15))
        
        # Botão de configurações
        self.config_btn = tk.Button(
            quick_actions_frame,
            text="⚙️ CONFIGURAÇÕES",
            command=self.open_configurations,
            bg='#2196F3',
            fg='white',
            font=("Arial", 14, "bold"),
            height=2,
            width=18
        )
        self.config_btn.pack(side=tk.LEFT, padx=(0, 15))
        
        # Botão de testes
        self.test_btn = tk.Button(
            quick_actions_frame,
            text="🧪 TESTES",
            command=self.run_system_tests,
            bg='#9C27B0',
            fg='white',
            font=("Arial", 14, "bold"),
            height=2,
            width=12
        )
        self.test_btn.pack(side=tk.LEFT)
        
        # Frame de estatísticas
        stats_frame = ttk.Frame(control_frame)
        stats_frame.pack(fill=tk.X, pady=(10, 0))
        
        # Estatísticas
        self.stats_label = tk.Label(
            stats_frame,
            text="📊 Agentes Ativos: 0 | Total: 16 | Status: 🟢 Pronto",
            font=("Arial", 11),
            bg='#2b2b2b',
            fg='#00ff00'
        )
        self.stats_label.pack(side=tk.LEFT)
        
        # Frame de logs
        logs_frame = ttk.LabelFrame(main_frame, text="📋 Logs do Sistema em Tempo Real", padding=15)
        logs_frame.pack(fill=tk.BOTH, expand=True)
        
        # Área de logs
        self.log_text = scrolledtext.ScrolledText(
            logs_frame,
            height=15,
            bg='#1e1e1e',
            fg='#ffffff',
            font=("Consolas", 10),
            insertbackground='#ffffff'
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("🟢 Sistema Pronto - BMAD System GUI v1.0.0")
        status_bar = tk.Label(
            main_frame,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W,
            bg='#2b2b2b',
            fg='#ffffff',
            font=("Arial", 10)
        )
        status_bar.pack(fill=tk.X, pady=(15, 0))
        
        return main_frame
    
    def log_message(self, message, level="INFO"):
        """Adiciona mensagem ao log"""
        if not self.log_text:
            return
            
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Cores por nível
        colors = {
            'INFO': '#00ff00',
            'WARNING': '#FF9800',
            'ERROR': '#f44336',
            'SUCCESS': '#4CAF50',
            'SYSTEM': '#2196F3'
        }
        
        color = colors.get(level, '#ffffff')
        
        # Formatar mensagem
        formatted_message = f"[{timestamp}] {message}\n"
        
        # Inserir no log
        self.log_text.insert(tk.END, formatted_message)
        
        # Aplicar cor
        start_index = self.log_text.index("end-2c linestart")
        end_index = self.log_text.index("end-1c")
        self.log_text.tag_add(f"level_{level}", start_index, end_index)
        self.log_text.tag_config(f"level_{level}", foreground=color)
        
        # Scroll para o final
        self.log_text.see(tk.END)
        
        # Limitar número de linhas (opcional)
        lines = int(self.log_text.index('end-1c').split('.')[0])
        if lines > 1000:
            self.log_text.delete('1.0', '2.0')
    
    def update_stats(self, active_agents=0, total_agents=16, status="🟢 Pronto"):
        """Atualiza estatísticas na interface"""
        if self.stats_label:
            self.stats_label.config(
                text=f"📊 Agentes Ativos: {active_agents} | Total: {total_agents} | Status: {status}"
            )
    
    def update_status(self, status):
        """Atualiza status na barra de status"""
        if self.status_var:
            self.status_var.set(status)
    
    def clear_logs(self):
        """Limpa a área de logs"""
        if self.log_text:
            self.log_text.delete(1.0, tk.END)
            self.log_message("🗑️ Logs limpos", "SYSTEM")
    
    def activate_complete_system(self):
        """Ativa o sistema completo (placeholder)"""
        self.log_message("🚀 Ativando sistema completo...", "SYSTEM")
        self.update_status("🟡 Sistema em ativação...")
        
        # Simular ativação
        def activation_thread():
            import time
            time.sleep(2)  # Simular tempo de ativação
            
            self.log_message("✅ Sistema ativado com sucesso!", "SUCCESS")
            self.update_status("🟢 Sistema Ativo - BMAD System GUI v1.0.0")
        
        thread = threading.Thread(target=activation_thread, daemon=True)
        thread.start()
    
    def stop_all_tasks(self):
        """Para todas as tarefas (placeholder)"""
        self.log_message("⏹️ Parando todas as tarefas...", "SYSTEM")
        self.update_status("🟡 Parando tarefas...")
        
        # Simular parada
        def stop_thread():
            import time
            time.sleep(1)  # Simular tempo de parada
            
            self.log_message("✅ Todas as tarefas paradas", "SUCCESS")
            self.update_status("🟢 Sistema Pronto - BMAD System GUI v1.0.0")
        
        thread = threading.Thread(target=stop_thread, daemon=True)
        thread.start()
    
    def open_configurations(self):
        """Abre configurações (placeholder)"""
        self.log_message("⚙️ Abrindo configurações...", "INFO")
        # Esta função será implementada pelo módulo de configurações
    
    def run_system_tests(self):
        """Executa testes do sistema (placeholder)"""
        self.log_message("🧪 Iniciando testes do sistema...", "SYSTEM")
        # Esta função será implementada pelo módulo de testes
    
    def set_callbacks(self, config_callback=None, test_callback=None):
        """Define callbacks para outras funcionalidades"""
        if config_callback:
            self.open_configurations = config_callback
        if test_callback:
            self.run_system_tests = test_callback 