#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BMAD System GUI - Versão Simplificada
Interface otimizada com foco em UX e simplicidade

Autor: Sistema BMAD - Codex MMORPG
Versão: 3.0.0 (UX Simplificada)
Data: 2025-08-01
Sistema: Windows/Linux/Mac com Tkinter
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import sys
import os
from pathlib import Path
from datetime import datetime
import threading
import subprocess

# Importar módulo de estilos melhorado
try:
    from gui_modules.gui_styles_improved import GUIStylesImproved
except ImportError:
    print("❌ Módulo de estilos melhorado não encontrado")
    sys.exit(1)

class BMADSystemGUISimplified:
    """Classe principal do sistema BMAD GUI simplificado"""
    
    def __init__(self, root):
        """Inicializa o sistema simplificado"""
        self.root = root
        self.root.title("BMAD System - Sistema de Agentes Inteligentes")
        self.root.geometry("1000x700")
        
        # Configurações base
        self.base_path = Path.cwd()
        self.log_path = self.base_path / "wiki" / "log"
        self.log_path.mkdir(parents=True, exist_ok=True)
        
        # Inicializar estilos
        self.styles = GUIStylesImproved()
        self.styles.apply_light_theme_to_window(self.root)
        
        # Estado do sistema
        self.system_status = "Inativo"
        self.active_agents = 0
        self.total_agents = 16
        
        # Configurar interface
        self.setup_interface()
        
        # Inicializar logs
        self.log_message("BMAD System iniciado com sucesso!", "INFO")
    
    def setup_interface(self):
        """Configura a interface simplificada"""
        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header simplificado
        self.create_header(main_frame)
        
        # Cards informativos
        self.create_info_cards(main_frame)
        
        # Área de conteúdo principal
        self.create_main_content(main_frame)
        
        # Centralizar janela
        self.center_window()
    
    def create_header(self, parent):
        """Cria o cabeçalho simplificado"""
        header_frame = ttk.Frame(parent)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Título principal
        title_label = self.styles.create_simple_label(
            header_frame, 
            "BMAD System", 
            'heading_large'
        )
        title_label.pack(side=tk.LEFT)
        
        # Status do sistema
        self.status_indicator = self.styles.create_status_indicator(
            header_frame, 
            self.system_status
        )
        self.status_indicator.pack(side=tk.RIGHT, padx=(20, 0))
        
        # Botões de ação principais
        actions_frame = ttk.Frame(header_frame)
        actions_frame.pack(side=tk.RIGHT)
        
        self.start_btn = self.styles.create_simple_button(
            actions_frame,
            "Iniciar Sistema",
            self.start_system,
            'success'
        )
        self.start_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.stop_btn = self.styles.create_simple_button(
            actions_frame,
            "Parar Sistema",
            self.stop_system,
            'danger'
        )
        self.stop_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.config_btn = self.styles.create_simple_button(
            actions_frame,
            "Configurações",
            self.open_config,
            'secondary'
        )
        self.config_btn.pack(side=tk.LEFT)
    
    def create_info_cards(self, parent):
        """Cria cards informativos"""
        cards_frame = ttk.Frame(parent)
        cards_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Card de status do sistema
        self.system_card = self.styles.create_card(
            cards_frame,
            "Status do Sistema",
            f"{self.system_status}"
        )
        
        # Card de agentes
        self.agents_card = self.styles.create_card(
            cards_frame,
            "Agentes",
            f"{self.active_agents} de {self.total_agents} ativos"
        )
        
        # Card de saúde do sistema
        self.health_card = self.styles.create_card(
            cards_frame,
            "Saúde do Sistema",
            "95%"
        )
    
    def create_main_content(self, parent):
        """Cria o conteúdo principal"""
        content_frame = ttk.Frame(parent)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Frame esquerdo - Lista de agentes
        left_frame = ttk.Frame(content_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Título da seção
        agents_title = self.styles.create_simple_label(
            left_frame,
            "Agentes Disponíveis",
            'heading_small'
        )
        agents_title.pack(anchor=tk.W, pady=(0, 10))
        
        # Lista de agentes simplificada
        self.create_agents_list(left_frame)
        
        # Frame direito - Logs
        right_frame = ttk.Frame(content_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        # Título da seção
        logs_title = self.styles.create_simple_label(
            right_frame,
            "Logs do Sistema",
            'heading_small'
        )
        logs_title.pack(anchor=tk.W, pady=(0, 10))
        
        # Área de logs
        self.create_logs_area(right_frame)
    
    def create_agents_list(self, parent):
        """Cria lista de agentes simplificada"""
        # Frame para a lista
        list_frame = ttk.Frame(parent)
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        # Lista de agentes principais
        main_agents = [
            "Workflow Orchestrator",
            "File Organization", 
            "Cleanup Agent",
            "Validation Agent",
            "Metrics Agent",
            "Knowledge Manager"
        ]
        
        # Criar botões para agentes principais
        for agent in main_agents:
            agent_frame = ttk.Frame(list_frame)
            agent_frame.pack(fill=tk.X, pady=2)
            
            agent_btn = self.styles.create_simple_button(
                agent_frame,
                agent,
                lambda a=agent: self.run_agent(a),
                'primary'
            )
            agent_btn.pack(fill=tk.X)
        
        # Botão para ver todos os agentes
        all_agents_btn = self.styles.create_simple_button(
            list_frame,
            "Ver Todos os Agentes",
            self.show_all_agents,
            'secondary'
        )
        all_agents_btn.pack(fill=tk.X, pady=(10, 0))
    
    def create_logs_area(self, parent):
        """Cria área de logs simplificada"""
        # Frame para logs
        logs_frame = ttk.Frame(parent)
        logs_frame.pack(fill=tk.BOTH, expand=True)
        
        # Área de texto com scroll
        self.log_text = scrolledtext.ScrolledText(
            logs_frame,
            height=15,
            bg=self.styles.get_color('surface'),
            fg=self.styles.get_color('text_primary'),
            font=self.styles.get_font('body_small'),
            borderwidth=1,
            relief='solid'
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
        # Botões de controle de logs
        logs_controls = ttk.Frame(logs_frame)
        logs_controls.pack(fill=tk.X, pady=(10, 0))
        
        clear_logs_btn = self.styles.create_simple_button(
            logs_controls,
            "Limpar Logs",
            self.clear_logs,
            'secondary'
        )
        clear_logs_btn.pack(side=tk.LEFT)
        
        export_logs_btn = self.styles.create_simple_button(
            logs_controls,
            "Exportar Logs",
            self.export_logs,
            'secondary'
        )
        export_logs_btn.pack(side=tk.LEFT, padx=(10, 0))
    
    def start_system(self):
        """Inicia o sistema"""
        self.log_message("Iniciando sistema BMAD...", "INFO")
        self.system_status = "Ativo"
        self.update_status()
        self.log_message("Sistema iniciado com sucesso!", "SUCCESS")
    
    def stop_system(self):
        """Para o sistema"""
        self.log_message("Parando sistema BMAD...", "INFO")
        self.system_status = "Inativo"
        self.active_agents = 0
        self.update_status()
        self.log_message("Sistema parado", "SUCCESS")
    
    def run_agent(self, agent_name):
        """Executa um agente específico"""
        self.log_message(f"Executando agente: {agent_name}", "INFO")
        self.active_agents += 1
        self.update_status()
        
        # Simular execução do agente
        def run_agent_thread():
            try:
                # Aqui seria a execução real do agente
                self.log_message(f"Agente {agent_name} executado com sucesso", "SUCCESS")
            except Exception as e:
                self.log_message(f"Erro ao executar {agent_name}: {e}", "ERROR")
            finally:
                self.active_agents = max(0, self.active_agents - 1)
                self.update_status()
        
        thread = threading.Thread(target=run_agent_thread, daemon=True)
        thread.start()
    
    def show_all_agents(self):
        """Mostra todos os agentes disponíveis"""
        self.log_message("Abrindo lista completa de agentes...", "INFO")
        # Aqui seria implementada a janela com todos os agentes
        messagebox.showinfo("Agentes", "Lista completa de agentes seria exibida aqui")
    
    def open_config(self):
        """Abre configurações"""
        self.log_message("Abrindo configurações...", "INFO")
        # Aqui seria implementada a janela de configurações
        messagebox.showinfo("Configurações", "Configurações do sistema seriam exibidas aqui")
    
    def clear_logs(self):
        """Limpa os logs"""
        self.log_text.delete(1.0, tk.END)
        self.log_message("Logs limpos", "INFO")
    
    def export_logs(self):
        """Exporta os logs"""
        self.log_message("Exportando logs...", "INFO")
        # Aqui seria implementada a exportação
        messagebox.showinfo("Exportar", "Logs seriam exportados aqui")
    
    def log_message(self, message, level="INFO"):
        """Adiciona mensagem ao log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Cores para diferentes níveis
        colors = {
            'INFO': self.styles.get_color('text_primary'),
            'SUCCESS': self.styles.get_color('success'),
            'ERROR': self.styles.get_color('danger'),
            'WARNING': self.styles.get_color('warning')
        }
        
        # Formatar mensagem
        formatted_message = f"[{timestamp}] {level}: {message}\n"
        
        # Adicionar ao log
        self.log_text.insert(tk.END, formatted_message)
        self.log_text.see(tk.END)
        
        # Colorir texto (simplificado)
        # Em uma implementação completa, seria usado tags do Tkinter
    
    def update_status(self):
        """Atualiza o status do sistema"""
        # Atualizar indicador de status
        self.status_indicator.configure(text=f"● {self.system_status}")
        
        # Atualizar cards
        if hasattr(self, 'system_card'):
            # Atualizar conteúdo dos cards
            pass
        
        # Atualizar contador de agentes
        if hasattr(self, 'agents_card'):
            # Atualizar contador
            pass
    
    def center_window(self):
        """Centraliza a janela na tela"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

def main():
    """Função principal"""
    try:
        # Verificar se o módulo de estilos existe
        if not Path("gui_modules/gui_styles_improved.py").exists():
            print("❌ Módulo de estilos melhorado não encontrado!")
            print("📁 Certifique-se de que o arquivo 'gui_modules/gui_styles_improved.py' existe")
            return
        
        # Criar janela principal
        root = tk.Tk()
        app = BMADSystemGUISimplified(root)
        
        print("✅ BMAD System GUI Simplificado iniciado com sucesso!")
        print("🎯 Interface otimizada para melhor UX")
        
        root.mainloop()
        
    except Exception as e:
        print(f"❌ Erro fatal ao iniciar sistema: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 