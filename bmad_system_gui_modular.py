#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BMAD System GUI - Versão Modularizada
Sistema unificado de agentes BMAD com interface gráfica modular

Autor: Sistema BMAD - Codex MMORPG
Versão: 2.0.0 (Modular)
Data: 2025-08-01
Sistema: Windows/Linux/Mac com Tkinter
"""

import tkinter as tk
from tkinter import ttk
import sys
import os
from pathlib import Path

# Importar módulos
try:
    from gui_modules.gui_styles import GUIStyles
    from gui_modules.gui_interface import GUIInterface
    from gui_modules.gui_agents import GUIAgents
    from gui_modules.gui_config import GUIConfig
    from gui_modules.gui_tests import GUITests
    from gui_modules.gui_utils import GUIUtils
except ImportError as e:
    print(f"❌ Erro ao importar módulos: {e}")
    print("📁 Certifique-se de que a pasta 'gui_modules' existe e contém todos os módulos")
    sys.exit(1)

class BMADSystemGUIModular:
    """Classe principal do sistema BMAD GUI modularizado"""
    
    def __init__(self, root):
        """Inicializa o sistema modular"""
        self.root = root
        self.root.title("🧠 BMAD System - Sistema de Aprendizado Inteligente (Modular)")
        self.root.geometry("1200x800")
        self.root.configure(bg='#2b2b2b')
        
        # Configurações base
        self.base_path = Path.cwd()
        self.log_path = self.base_path / "wiki" / "log"
        self.log_path.mkdir(parents=True, exist_ok=True)
        
        # Inicializar módulos
        self.initialize_modules()
        
        # Configurar interface
        self.setup_interface()
        
        # Inicializar logs
        self.log_message("🧠 BMAD System GUI Modular iniciado com sucesso!", "INFO")
        self.log_message("📁 Caminho base: " + str(self.base_path), "INFO")
        self.log_message("🔧 Sistema modular carregado", "SUCCESS")
    
    def initialize_modules(self):
        """Inicializa todos os módulos do sistema"""
        try:
            # Módulo de estilos
            self.styles = GUIStyles()
            
            # Módulo de interface principal
            self.interface = GUIInterface(self.root, self.base_path, self.log_message)
            
            # Módulo de agentes
            self.agents = GUIAgents(self.root, self.base_path, self.log_message)
            
            # Módulo de configurações
            self.config = GUIConfig(self.root, self.base_path, self.log_message)
            
            # Módulo de testes
            self.tests = GUITests(self.root, self.base_path, self.log_message)
            
            # Módulo de utilitários
            self.utils = GUIUtils()
            
            self.log_message("✅ Todos os módulos inicializados com sucesso", "SUCCESS")
            
        except Exception as e:
            self.log_message(f"❌ Erro ao inicializar módulos: {e}", "ERROR")
            raise
    
    def setup_interface(self):
        """Configura a interface principal"""
        # Criar interface principal
        main_frame = self.interface.create_main_interface()
        
        # Criar frame de agentes
        agents_frame = self.agents.create_agents_frame(main_frame)
        
        # Configurar callbacks
        self.interface.set_callbacks(
            config_callback=self.open_configurations,
            test_callback=self.run_system_tests
        )
        
        # Configurar callbacks dos agentes
        self.setup_agent_callbacks()
        
        # Atualizar estatísticas iniciais
        self.update_stats()
        
        # Centralizar janela
        self.utils.center_window(self.root)
    
    def setup_agent_callbacks(self):
        """Configura callbacks para atualização de estatísticas"""
        # Sobrescrever métodos dos agentes para atualizar estatísticas
        original_stop_all = self.agents.stop_all_tasks
        original_run_all = self.agents.run_all_agents
        
        def stop_all_with_stats():
            original_stop_all()
            self.update_stats()
        
        def run_all_with_stats():
            original_run_all()
            self.update_stats()
        
        self.agents.stop_all_tasks = stop_all_with_stats
        self.agents.run_all_agents = run_all_with_stats
    
    def log_message(self, message, level="INFO"):
        """Log centralizado para todos os módulos"""
        # Log na interface principal
        if hasattr(self, 'interface') and self.interface:
            self.interface.log_message(message, level)
        
        # Log no console (para debug)
        print(f"[{level}] {message}")
    
    def update_stats(self):
        """Atualiza estatísticas na interface"""
        if hasattr(self, 'agents') and hasattr(self, 'interface'):
            active_count = self.agents.get_active_agents_count()
            total_count = self.agents.get_total_agents_count()
            self.interface.update_stats(active_count, total_count)
    
    def open_configurations(self):
        """Abre janela de configurações"""
        try:
            self.log_message("⚙️ Abrindo configurações...", "INFO")
            config_window = self.config.create_config_window()
            
            # Configurar callback para salvar
            def save_config():
                self.config.save_configurations(config_window)
                self.log_message("💾 Configurações salvas", "SUCCESS")
            
            # Substituir callback de salvar
            for widget in config_window.winfo_children():
                if hasattr(widget, 'winfo_children'):
                    for child in widget.winfo_children():
                        if isinstance(child, tk.Button) and "Salvar" in child.cget('text'):
                            child.config(command=save_config)
                            break
            
        except Exception as e:
            self.log_message(f"❌ Erro ao abrir configurações: {e}", "ERROR")
    
    def run_system_tests(self):
        """Executa testes do sistema"""
        try:
            self.log_message("🧪 Iniciando testes do sistema...", "SYSTEM")
            test_window = self.tests.create_test_window()
            
        except Exception as e:
            self.log_message(f"❌ Erro ao executar testes: {e}", "ERROR")
    
    def activate_complete_system(self):
        """Ativa o sistema completo"""
        self.log_message("🚀 Ativando sistema completo...", "SYSTEM")
        
        # Executar todos os agentes
        if hasattr(self, 'agents'):
            self.agents.run_all_agents()
        
        # Atualizar estatísticas
        self.update_stats()
        
        self.log_message("✅ Sistema completo ativado!", "SUCCESS")
    
    def stop_all_tasks(self):
        """Para todas as tarefas"""
        self.log_message("⏹️ Parando todas as tarefas...", "SYSTEM")
        
        # Parar todos os agentes
        if hasattr(self, 'agents'):
            self.agents.stop_all_tasks()
        
        # Atualizar estatísticas
        self.update_stats()
        
        self.log_message("✅ Todas as tarefas paradas", "SUCCESS")
    
    def clear_logs(self):
        """Limpa logs"""
        if hasattr(self, 'interface'):
            self.interface.clear_logs()
    
    def refresh_agents_list(self):
        """Atualiza lista de agentes"""
        if hasattr(self, 'agents'):
            self.agents.refresh_agents_list()
            self.update_stats()
    
    def run_selected_agent(self):
        """Executa agente selecionado"""
        if hasattr(self, 'agents'):
            self.agents.run_selected_agent()
            self.update_stats()
    
    def run_all_agents(self):
        """Executa todos os agentes"""
        if hasattr(self, 'agents'):
            self.agents.run_all_agents()
            self.update_stats()

def main():
    """Função principal"""
    try:
        # Verificar se os módulos existem
        modules_path = Path("gui_modules")
        if not modules_path.exists():
            print("❌ Pasta 'gui_modules' não encontrada!")
            print("📁 Certifique-se de que todos os módulos foram criados")
            return
        
        # Verificar arquivos necessários
        required_modules = [
            "gui_modules/__init__.py",
            "gui_modules/gui_styles.py",
            "gui_modules/gui_interface.py",
            "gui_modules/gui_agents.py",
            "gui_modules/gui_config.py",
            "gui_modules/gui_tests.py",
            "gui_modules/gui_utils.py"
        ]
        
        missing_modules = []
        for module in required_modules:
            if not Path(module).exists():
                missing_modules.append(module)
        
        if missing_modules:
            print("❌ Módulos faltando:")
            for module in missing_modules:
                print(f"   - {module}")
            return
        
        # Criar janela principal
        root = tk.Tk()
        app = BMADSystemGUIModular(root)
        
        # Configurar tema escuro
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar cores
        root.configure(bg='#2b2b2b')
        
        # Configurar ícone da janela (se disponível)
        try:
            root.iconbitmap('icon.ico')
        except:
            pass
        
        print("✅ BMAD System GUI Modular iniciado com sucesso!")
        print("🎯 Sistema pronto para uso")
        
        root.mainloop()
        
    except Exception as e:
        print(f"❌ Erro fatal ao iniciar sistema: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 