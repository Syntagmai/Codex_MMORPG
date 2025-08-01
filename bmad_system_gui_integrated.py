#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BMAD System GUI - Versão Integrada
Interface que realmente executa os agentes BMAD

Autor: Sistema BMAD - Codex MMORPG
Versão: 4.0.0 (Integrada)
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
import json

# Importar módulo de estilos melhorado
try:
    from gui_modules.gui_styles_improved import GUIStylesImproved
except ImportError:
    print("❌ Módulo de estilos melhorado não encontrado")
    sys.exit(1)

class BMADSystemGUIIntegrated:
    """Classe principal do sistema BMAD GUI integrado"""
    
    def __init__(self, root):
        """Inicializa o sistema integrado"""
        self.root = root
        self.root.title("BMAD System - Sistema de Agentes Inteligentes (Integrado)")
        self.root.geometry("1000x700")
        
        # Configurações base
        self.base_path = Path.cwd()
        self.agents_path = self.base_path / "wiki" / "bmad" / "agents"
        self.log_path = self.base_path / "wiki" / "log"
        self.config_path = self.base_path / "wiki" / "config"
        
        # Criar diretórios necessários
        self.log_path.mkdir(parents=True, exist_ok=True)
        self.config_path.mkdir(parents=True, exist_ok=True)
        
        # Inicializar estilos
        self.styles = GUIStylesImproved()
        self.styles.apply_light_theme_to_window(self.root)
        
        # Estado do sistema
        self.system_status = "Inativo"
        self.active_agents = 0
        self.running_processes = {}
        
        # Carregar agentes disponíveis
        self.load_available_agents()
        
        # Configurar interface
        self.setup_interface()
        
        # Inicializar logs
        self.log_message("BMAD System Integrado iniciado com sucesso!", "INFO")
        self.log_message(f"Agentes encontrados: {len(self.available_agents)}", "INFO")
    
    def load_available_agents(self):
        """Carrega a lista de agentes disponíveis"""
        self.available_agents = []
        
        if self.agents_path.exists():
            for agent_file in self.agents_path.glob("*.py"):
                if agent_file.name.startswith("__"):
                    continue
                
                agent_name = agent_file.stem.replace("_", " ").title()
                self.available_agents.append({
                    'name': agent_name,
                    'file': agent_file.name,
                    'path': agent_file,
                    'status': 'Pronto'
                })
        
        # Ordenar agentes por nome
        self.available_agents.sort(key=lambda x: x['name'])
    
    def setup_interface(self):
        """Configura a interface integrada"""
        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header integrado
        self.create_header(main_frame)
        
        # Cards informativos
        self.create_info_cards(main_frame)
        
        # Área de conteúdo principal
        self.create_main_content(main_frame)
        
        # Centralizar janela
        self.center_window()
    
    def create_header(self, parent):
        """Cria o cabeçalho integrado"""
        header_frame = ttk.Frame(parent)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Título principal
        title_label = self.styles.create_simple_label(
            header_frame, 
            "BMAD System - Integrado", 
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
        
        self.refresh_btn = self.styles.create_simple_button(
            actions_frame,
            "Atualizar",
            self.refresh_agents,
            'secondary'
        )
        self.refresh_btn.pack(side=tk.LEFT)
    
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
            f"{self.active_agents} de {len(self.available_agents)} ativos"
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
            "Agentes BMAD Disponíveis",
            'heading_small'
        )
        agents_title.pack(anchor=tk.W, pady=(0, 10))
        
        # Lista de agentes integrada
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
        """Cria lista de agentes integrada"""
        # Frame para a lista com scroll
        list_container = ttk.Frame(parent)
        list_container.pack(fill=tk.BOTH, expand=True)
        
        # Canvas para scroll
        canvas = tk.Canvas(list_container, bg=self.styles.get_color('background'))
        scrollbar = ttk.Scrollbar(list_container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Criar botões para agentes
        for agent in self.available_agents:
            agent_frame = ttk.Frame(scrollable_frame)
            agent_frame.pack(fill=tk.X, pady=2)
            
            # Frame para botão e status
            button_frame = ttk.Frame(agent_frame)
            button_frame.pack(fill=tk.X)
            
            # Botão do agente
            agent_btn = self.styles.create_simple_button(
                button_frame,
                agent['name'],
                lambda a=agent: self.run_agent(a),
                'primary'
            )
            agent_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)
            
            # Status do agente
            status_label = self.styles.create_simple_label(
                button_frame,
                agent['status'],
                'caption'
            )
            status_label.pack(side=tk.RIGHT, padx=(10, 0))
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Botões de controle
        controls_frame = ttk.Frame(parent)
        controls_frame.pack(fill=tk.X, pady=(10, 0))
        
        run_all_btn = self.styles.create_simple_button(
            controls_frame,
            "Executar Todos",
            self.run_all_agents,
            'success'
        )
        run_all_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        stop_all_btn = self.styles.create_simple_button(
            controls_frame,
            "Parar Todos",
            self.stop_all_agents,
            'danger'
        )
        stop_all_btn.pack(side=tk.LEFT)
    
    def create_logs_area(self, parent):
        """Cria área de logs integrada"""
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
        
        save_logs_btn = self.styles.create_simple_button(
            logs_controls,
            "Salvar Logs",
            self.save_logs,
            'secondary'
        )
        save_logs_btn.pack(side=tk.LEFT, padx=(10, 0))
    
    def start_system(self):
        """Inicia o sistema BMAD"""
        self.log_message("Iniciando sistema BMAD...", "INFO")
        self.system_status = "Ativo"
        self.update_status()
        self.log_message("Sistema iniciado com sucesso!", "SUCCESS")
    
    def stop_system(self):
        """Para o sistema BMAD"""
        self.log_message("Parando sistema BMAD...", "INFO")
        self.stop_all_agents()
        self.system_status = "Inativo"
        self.update_status()
        self.log_message("Sistema parado", "SUCCESS")
    
    def run_agent(self, agent):
        """Executa um agente específico"""
        agent_name = agent['name']
        agent_file = agent['file']
        
        if agent_name in self.running_processes:
            self.log_message(f"Agente {agent_name} já está em execução", "WARNING")
            return
        
        self.log_message(f"Executando agente: {agent_name}", "INFO")
        
        # Atualizar status do agente
        agent['status'] = 'Executando'
        self.active_agents += 1
        self.update_status()
        
        def run_agent_thread():
            try:
                # Executar o agente
                cmd = [sys.executable, str(agent['path'])]
                process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    cwd=str(self.base_path)
                )
                
                # Armazenar processo
                self.running_processes[agent_name] = process
                
                # Capturar saída
                stdout, stderr = process.communicate()
                
                # Log de resultado
                if process.returncode == 0:
                    self.log_message(f"Agente {agent_name} executado com sucesso", "SUCCESS")
                    if stdout.strip():
                        self.log_message(f"Saída: {stdout.strip()}", "INFO")
                else:
                    self.log_message(f"Erro na execução do agente {agent_name}", "ERROR")
                    if stderr.strip():
                        self.log_message(f"Erro: {stderr.strip()}", "ERROR")
                
            except Exception as e:
                self.log_message(f"Erro ao executar {agent_name}: {e}", "ERROR")
            
            finally:
                # Limpar processo
                if agent_name in self.running_processes:
                    del self.running_processes[agent_name]
                
                # Atualizar status
                agent['status'] = 'Pronto'
                self.active_agents = max(0, self.active_agents - 1)
                self.update_status()
        
        thread = threading.Thread(target=run_agent_thread, daemon=True)
        thread.start()
    
    def run_all_agents(self):
        """Executa todos os agentes disponíveis"""
        self.log_message("Executando todos os agentes...", "INFO")
        
        for agent in self.available_agents:
            if agent['status'] == 'Pronto':
                self.run_agent(agent)
    
    def stop_all_agents(self):
        """Para todos os agentes em execução"""
        self.log_message("Parando todos os agentes...", "INFO")
        
        for agent_name, process in self.running_processes.items():
            try:
                process.terminate()
                self.log_message(f"Agente {agent_name} parado", "INFO")
            except:
                pass
        
        self.running_processes.clear()
        
        # Atualizar status dos agentes
        for agent in self.available_agents:
            agent['status'] = 'Pronto'
        
        self.active_agents = 0
        self.update_status()
        self.log_message("Todos os agentes parados", "SUCCESS")
    
    def refresh_agents(self):
        """Atualiza a lista de agentes"""
        self.log_message("Atualizando lista de agentes...", "INFO")
        self.load_available_agents()
        self.update_status()
        self.log_message(f"Lista atualizada: {len(self.available_agents)} agentes", "SUCCESS")
    
    def clear_logs(self):
        """Limpa os logs"""
        self.log_text.delete(1.0, tk.END)
        self.log_message("Logs limpos", "INFO")
    
    def save_logs(self):
        """Salva os logs em arquivo"""
        try:
            log_content = self.log_text.get(1.0, tk.END)
            log_file = self.log_path / f"bmad_gui_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            
            with open(log_file, 'w', encoding='utf-8') as f:
                f.write(log_content)
            
            self.log_message(f"Logs salvos em: {log_file}", "SUCCESS")
        except Exception as e:
            self.log_message(f"Erro ao salvar logs: {e}", "ERROR")
    
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
        
        # Verificar se os agentes existem
        agents_path = Path("wiki/bmad/agents")
        if not agents_path.exists():
            print("❌ Pasta de agentes não encontrada!")
            print("📁 Certifique-se de que a pasta 'wiki/bmad/agents' existe")
            return
        
        # Criar janela principal
        root = tk.Tk()
        app = BMADSystemGUIIntegrated(root)
        
        print("✅ BMAD System GUI Integrado iniciado com sucesso!")
        print("🎯 Sistema conectado aos agentes BMAD")
        
        root.mainloop()
        
    except Exception as e:
        print(f"❌ Erro fatal ao iniciar sistema: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 