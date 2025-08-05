#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from unicode_aliases import *
"""
BMAD System GUI - Módulo de Agentes
Gerencia agentes na interface gráfica

Autor: Sistema BMAD - Codex MMORPG
Versão: 1.0.0
Data: 2025-08-01
"""

import tkinter as tk
from tkinter import ttk
import subprocess
import threading
import queue
from pathlib import Path
import sys

class GUIAgents:
    """Classe para gerenciar agentes na interface gráfica"""
    
    def __init__(self, parent, base_path, log_callback=None):
        """Inicializa o gerenciador de agentes"""
        self.parent = parent
        self.base_path = Path(base_path)
        self.agents_path = self.base_path / "wiki" / "bmad" / "agents"
        self.log_callback = log_callback
        self.running_tasks = {}
        self.task_queue = queue.Queue()
        self.agents = []
        self.agents_tree = None
        
        self.load_agents_list()
    
    def load_agents_list(self):
        """Carrega a lista de agentes disponíveis"""
        self.agents = [
            {
                'name': 'Workflow Orchestrator',
                'file': 'workflow_orchestrator_agent.py',
                'description': 'Orquestra workflows de aprendizado automatizados',
                'status': '🟡 Pronto'
            },
            {
                'name': 'File Organization',
                'file': 'file_organization_agent.py',
                'description': 'Organiza e estrutura arquivos do projeto',
                'status': '🟡 Pronto'
            },
            {
                'name': 'Cleanup Agent',
                'file': 'cleanup_agent.py',
                'description': 'Remove arquivos desnecessários e otimiza estrutura',
                'status': '🟡 Pronto'
            },
            {
                'name': 'Migration Agent',
                'file': 'migration_agent.py',
                'description': 'Migra dados e configurações entre versões',
                'status': '🟡 Pronto'
            },
            {
                'name': 'Structure Agent',
                'file': 'structure_agent.py',
                'description': 'Analisa e melhora estrutura do projeto',
                'status': '🟡 Pronto'
            },
            {
                'name': 'Validation Agent',
                'file': 'validation_agent.py',
                'description': 'Valida integridade e qualidade do código',
                'status': '🟡 Pronto'
            },
            {
                'name': 'Agents Orchestrator',
                'file': 'agents_orchestrator.py',
                'description': 'Coordena execução de múltiplos agentes',
                'status': '🟡 Pronto'
            },
            {
                'name': 'Metrics Agent',
                'file': 'metrics_agent.py',
                'description': 'Coleta e analisa métricas do sistema',
                'status': '🟡 Pronto'
            },
            {
                'name': 'Unified Validation',
                'file': 'unified_validation_agent.py',
                'description': 'Validação unificada de todos os componentes',
                'status': '🟡 Pronto'
            },
            {
                'name': 'Deep Source Analyzer',
                'file': 'deep_source_analyzer.py',
                'description': 'Análise profunda do código fonte',
                'status': '🟡 Pronto'
            },
            {
                'name': 'Knowledge Manager',
                'file': 'knowledge_manager.py',
                'description': 'Gerencia base de conhecimento do sistema',
                'status': '🟡 Pronto'
            },
            {
                'name': 'Unified Research',
                'file': 'unified_research_agent.py',
                'description': 'Pesquisa unificada e análise de dados',
                'status': '🟡 Pronto'
            },
            {
                'name': 'Alert Agent',
                'file': 'alert_agent.py',
                'description': 'Sistema de alertas e notificações',
                'status': '🟡 Pronto'
            },
            {
                'name': 'Dashboard Agent',
                'file': 'dashboard_agent.py',
                'description': 'Gerencia dashboard e visualizações',
                'status': '🟡 Pronto'
            },
            {
                'name': 'Quality Assurance',
                'file': 'quality_assurance_agent.py',
                'description': 'Garantia de qualidade e testes',
                'status': '🟡 Pronto'
            },
            {
                'name': 'Documentation Agent',
                'file': 'documentation_agent.py',
                'description': 'Gera e mantém documentação',
                'status': '🟡 Pronto'
            }
        ]
    
    def create_agents_frame(self, parent):
        """Cria o frame de agentes na interface"""
        # Frame de agentes
        agents_frame = ttk.LabelFrame(parent, text="🤖 Agentes BMAD Disponíveis", padding=15)
        agents_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        # Lista de agentes
        agents_list_frame = ttk.Frame(agents_frame)
        agents_list_frame.pack(fill=tk.BOTH, expand=True)
        
        # Treeview para agentes
        columns = ('Agente', 'Descrição', 'Status', 'Ação')
        self.agents_tree = ttk.Treeview(agents_list_frame, columns=columns, show='headings', height=10)
        
        # Configurar colunas
        self.agents_tree.heading('Agente', text='Agente')
        self.agents_tree.heading('Descrição', text='Descrição')
        self.agents_tree.heading('Status', text='Status')
        self.agents_tree.heading('Ação', text='Ação')
        
        self.agents_tree.column('Agente', width=200)
        self.agents_tree.column('Descrição', width=300)
        self.agents_tree.column('Status', width=100)
        self.agents_tree.column('Ação', width=100)
        
        self.agents_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Scrollbar para a lista
        scrollbar = ttk.Scrollbar(agents_list_frame, orient=tk.VERTICAL, command=self.agents_tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.agents_tree.configure(yscrollcommand=scrollbar.set)
        
        # Botões de ação para agentes
        agent_actions_frame = ttk.Frame(agents_frame)
        agent_actions_frame.pack(fill=tk.X, pady=(15, 0))
        
        self.run_agent_btn = tk.Button(
            agent_actions_frame,
            text="▶️ Executar Agente Selecionado",
            command=self.run_selected_agent,
            bg='#2196F3',
            fg='white',
            font=("Arial", 12, "bold"),
            height=2
        )
        self.run_agent_btn.pack(side=tk.LEFT, padx=(0, 15))
        
        self.run_all_agents_btn = tk.Button(
            agent_actions_frame,
            text="🔄 Executar Todos os Agentes",
            command=self.run_all_agents,
            bg='#9C27B0',
            fg='white',
            font=("Arial", 12, "bold"),
            height=2
        )
        self.run_all_agents_btn.pack(side=tk.LEFT, padx=(0, 15))
        
        self.refresh_btn = tk.Button(
            agent_actions_frame,
            text="🔄 Atualizar Lista",
            command=self.refresh_agents_list,
            bg='#607D8B',
            fg='white',
            font=("Arial", 12, "bold"),
            height=2
        )
        self.refresh_btn.pack(side=tk.LEFT)
        
        return agents_frame
    
    def refresh_agents_display(self):
        """Atualiza a exibição dos agentes na interface"""
        if not self.agents_tree:
            return
            
        # Limpar lista atual
        for item in self.agents_tree.get_children():
            self.agents_tree.delete(item)
        
        # Adicionar agentes
        for agent in self.agents:
            self.agents_tree.insert('', 'end', values=(
                agent['name'],
                agent['description'],
                agent['status'],
                '▶️ Executar'
            ))
    
    def run_agent(self, agent_name, agent_file, args=None):
        """Executa um agente específico"""
        if self.log_callback:
            self.log_callback(f"🚀 Iniciando agente: {agent_name}", "INFO")
        
        # Verificar se o agente já está rodando
        if agent_name in self.running_tasks:
            if self.log_callback:
                self.log_callback(f"⚠️ Agente {agent_name} já está em execução", "WARNING")
            return
        
        # Marcar como em execução
        self.running_tasks[agent_name] = True
        
        # Atualizar status na interface
        for agent in self.agents:
            if agent['name'] == agent_name:
                agent['status'] = '🟢 Executando'
                break
        
        self.refresh_agents_display()
        
        def run_agent_thread():
            try:
                # Construir comando
                agent_path = self.agents_path / agent_file
                cmd = [sys.executable, str(agent_path)]
                
                if args:
                    cmd.extend(args)
                
                # Executar agente
                process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    cwd=str(self.base_path)
                )
                
                # Capturar saída
                stdout, stderr = process.communicate()
                
                # Log de resultado
                if process.returncode == 0:
                    if self.log_callback:
                        self.log_callback(f"✅ Agente {agent_name} executado com sucesso", "SUCCESS")
                        if stdout.strip():
                            self.log_callback(f"📤 Saída: {stdout.strip()}", "INFO")
                else:
                    if self.log_callback:
                        self.log_callback(f"❌ Erro na execução do agente {agent_name}", "ERROR")
                        if stderr.strip():
                            self.log_callback(f"📤 Erro: {stderr.strip()}", "ERROR")
                
            except Exception as e:
                if self.log_callback:
                    self.log_callback(f"❌ Erro ao executar agente {agent_name}: {e}", "ERROR")
            
            finally:
                # Remover da lista de tarefas em execução
                if agent_name in self.running_tasks:
                    del self.running_tasks[agent_name]
                
                # Atualizar status
                for agent in self.agents:
                    if agent['name'] == agent_name:
                        agent['status'] = '🟡 Pronto'
                        break
                
                self.refresh_agents_display()
        
        # Executar em thread separada
        thread = threading.Thread(target=run_agent_thread, daemon=True)
        thread.start()
    
    def run_selected_agent(self):
        """Executa o agente selecionado na interface"""
        selection = self.agents_tree.selection()
        if not selection:
            if self.log_callback:
                self.log_callback("⚠️ Nenhum agente selecionado", "WARNING")
            return
        
        item = self.agents_tree.item(selection[0])
        agent_name = item['values'][0]
        
        # Encontrar agente
        for agent in self.agents:
            if agent['name'] == agent_name:
                self.run_agent(agent['name'], agent['file'])
                break
    
    def run_all_agents(self):
        """Executa todos os agentes disponíveis"""
        if self.log_callback:
            self.log_callback("🚀 Iniciando execução de todos os agentes...", "SYSTEM")
        
        for agent in self.agents:
            self.run_agent(agent['name'], agent['file'])
    
    def stop_all_tasks(self):
        """Para todas as tarefas em execução"""
        if self.log_callback:
            self.log_callback("⏹️ Parando todas as tarefas...", "SYSTEM")
        
        # Limpar tarefas em execução
        self.running_tasks.clear()
        
        # Atualizar status dos agentes
        for agent in self.agents:
            agent['status'] = '🟡 Pronto'
        
        self.refresh_agents_display()
        
        if self.log_callback:
            self.log_callback("✅ Todas as tarefas paradas", "SUCCESS")
    
    def refresh_agents_list(self):
        """Atualiza a lista de agentes"""
        if self.log_callback:
            self.log_callback("🔄 Atualizando lista de agentes...", "INFO")
        
        self.load_agents_list()
        self.refresh_agents_display()
        
        if self.log_callback:
            self.log_callback(f"✅ Lista atualizada: {len(self.agents)} agentes encontrados", "SUCCESS")
    
    def get_active_agents_count(self):
        """Retorna o número de agentes ativos"""
        return len(self.running_tasks)
    
    def get_total_agents_count(self):
        """Retorna o número total de agentes"""
        return len(self.agents) 