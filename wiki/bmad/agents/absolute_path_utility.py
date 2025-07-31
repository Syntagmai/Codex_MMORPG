#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Absolute Path Utility - Sistema de Caminhos Absolutos
====================================================

Utilitário para uso de caminhos absolutos em todo o projeto.
Baseado no diretório raiz do projeto (onde está cursor.md).

Autor: Sistema BMAD
Versão: 2.0.0
Data: 2025-01-27
"""

import os
import sys
from pathlib import Path
from typing import Optional, Dict

class AbsolutePathManager:
    """
    Gerenciador de caminhos absolutos para o projeto.
    """
    
    def __init__(self):
        # Determinar caminho base absoluto
        self.base_path = self._find_project_root()
        
        # Mapeamento de caminhos corretos (absolutos)
        self.paths = {
            'base': self.base_path,
            'wiki': self.base_path / "wiki",
            'habdel': self.base_path / "wiki" / "habdel",
            'otclient': self.base_path / "wiki" / "habdel" / "otclient",
            'canary': self.base_path / "wiki" / "habdel" / "canary",
            'integration': self.base_path / "wiki" / "habdel" / "integration",
            'docs': self.base_path / "wiki" / "docs",
            'agents': self.base_path / "wiki" / "bmad" / "agents",
            'maps': self.base_path / "wiki" / "maps",
            'update': self.base_path / "wiki" / "update",
            'log': self.base_path / "wiki" / "log",
            'bmad': self.base_path / "wiki" / "bmad",
            'cursor_core': self.base_path / "wiki" / "cursor_core",
            'obsidian': self.base_path / "wiki" / ".obsidian"
        }
    
    def _find_project_root(self) -> Path:
        """
        Encontra o diretório raiz do projeto (onde está cursor.md).
        
        Returns:
            Path: Caminho absoluto do diretório raiz
        """
        current_path = Path.cwd().resolve()
        
        while current_path.parent != current_path:
            if (current_path / "cursor.md").exists():
                return current_path
            current_path = current_path.parent
        
        # Se não encontrar, usar diretório atual
        return Path.cwd().resolve()
    
    def get_path(self, path_name: str) -> Optional[Path]:
        """
        Obtém um caminho absoluto pelo nome.
        
        Args:
            path_name: Nome do caminho (wiki, habdel, otclient, etc.)
            
        Returns:
            Optional[Path]: Caminho absoluto ou None
        """
        return self.paths.get(path_name)
    
    def create_file_safely(self, path_name: str, filename: str, content: str) -> bool:
        """
        Cria um arquivo de forma segura usando caminhos absolutos.
        
        Args:
            path_name: Nome do caminho de destino
            filename: Nome do arquivo
            content: Conteúdo do arquivo
            
        Returns:
            bool: True se criado com sucesso
        """
        try:
            target_path = self.get_path(path_name)
            if target_path:
                file_path = target_path / filename
                file_path.parent.mkdir(parents=True, exist_ok=True)
                file_path.write_text(content, encoding='utf-8')
                return True
            return False
        except Exception as e:
            print(f"Erro ao criar arquivo {filename}: {e}")
            return False
    
    def run_script_absolutely(self, script_name: str, *args) -> bool:
        """
        Executa um script Python usando caminho absoluto.
        
        Args:
            script_name: Nome do script (sem .py)
            *args: Argumentos adicionais
            
        Returns:
            bool: True se executado com sucesso
        """
        try:
            script_path = self.get_path('agents') / f"{script_name}.py"
            if script_path.exists():
                # Executar script com caminho absoluto
                cmd = [sys.executable, str(script_path)] + list(args)
                result = subprocess.run(cmd, cwd=str(self.base_path), capture_output=True, text=True)
                
                if result.returncode == 0:
                    print(f"Script {script_name} executado com sucesso")
                    return True
                else:
                    print(f"Erro ao executar {script_name}: {result.stderr}")
                    return False
            else:
                print(f"Script {script_name} não encontrado em {script_path}")
                return False
        except Exception as e:
            print(f"Erro ao executar script {script_name}: {e}")
            return False
    
    def log_message(self, message: str, level: str = "INFO"):
        """
        Registra uma mensagem no log usando caminho absoluto.
        
        Args:
            message: Mensagem a ser registrada
            level: Nível da mensagem (INFO, WARNING, ERROR)
        """
        try:
            log_path = self.get_path('log')
            if log_path:
                log_file = log_path / "absolute_path_manager.log"
                timestamp = datetime.now().isoformat()
                log_entry = f"{timestamp} - {level} - {message}\n"
                
                with open(log_file, 'a', encoding='utf-8') as f:
                    f.write(log_entry)
        except Exception as e:
            print(f"Erro ao registrar log: {e}")

# Instância global para uso em outros módulos
path_manager = AbsolutePathManager()

# Funções de conveniência
def get_path(path_name: str) -> Optional[Path]:
    return path_manager.get_path(path_name)

def create_file_safely(path_name: str, filename: str, content: str) -> bool:
    return path_manager.create_file_safely(path_name, filename, content)

def run_script_absolutely(script_name: str, *args) -> bool:
    return path_manager.run_script_absolutely(script_name, *args)

def log_message(message: str, level: str = "INFO"):
    path_manager.log_message(message, level)

# Exemplo de uso:
# from absolute_path_utility import get_path, create_file_safely, run_script_absolutely
# 
# # Obter caminho absoluto
# otclient_path = get_path('otclient')
# 
# # Criar arquivo com caminho absoluto
# success = create_file_safely('otclient', 'meu_arquivo.md', '# Conteúdo')
# 
# # Executar script com caminho absoluto
# success = run_script_absolutely('path_validator_agent')
