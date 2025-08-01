    from git_automation_agent import GitAutomationAgent
    import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, List
import json
import logging
import os
import re
import subprocess
import sys

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Integração Git + Sistema de Tarefas - Sistema Automático e Atômico
==================================================================

Script que integra o agente de automação Git com o sistema de tarefas BMAD,
permitindo commits automáticos durante o desenvolvimento com contexto de tarefa.
IMPLEMENTAÇÃO AUTOMÁTICA E ATÔMICA - NUNCA MANUAL!

Autor: Sistema BMAD - OTClient Documentation
Data: 2024-12-19
Versão: 2.0 - Automático e Atômico
"""


# Adicionar pasta do agente Git ao path
sys.path.append(str(Path(__file__).parent.parent / 'bmad' / 'agents'))

try:
except ImportError:
    print("❌ Erro: Agente Git não encontrado. Execute primeiro a criação do agente.")
    sys.exit(1)

# Configuração de logging
log_dir = Path.cwd() / 'wiki' / 'log'
log_dir.mkdir(parents=True, exist_ok=True)
log_file = log_dir / 'git_task_integration.log'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

class GitTaskIntegration:
    """Integração entre agente Git e sistema de tarefas - AUTOMÁTICO E ATÔMICO."""
    
    def __init__(self):
        """Inicializa a integração."""
        self.logger = logging.getLogger(__name__)
        self.git_agent = GitAutomationAgent()
        self.project_root = Path.cwd()
        self.task_log_dir = self.project_root / 'wiki' / 'log'
        
        self.logger.info("🚀 Integração Git + Sistema de Tarefas inicializada - MODO AUTOMÁTICO")
    
    def resolve_git_errors_automatically(self) -> bool:
        """
        Resolve erros Git automaticamente sem intervenção manual.
        
        Returns:
            True se todos os erros foram resolvidos
        """
        self.logger.info("🔧 Iniciando resolução automática de erros Git...")
        
        try:
            # 1. Verificar se é repositório Git
            if not self.is_git_repo():
                self.logger.info("📁 Inicializando repositório Git...")
                self.initialize_git_repo()
            
            # 2. Verificar arquivos não rastreados
            untracked_files = self.get_untracked_files()
            if untracked_files:
                self.logger.info(f"📄 Adicionando {len(untracked_files)} arquivos não rastreados...")
                self.add_untracked_files_automatically(untracked_files)
            
            # 3. Verificar arquivos modificados
            modified_files = self.get_modified_files()
            if modified_files:
                self.logger.info(f"📝 Adicionando {len(modified_files)} arquivos modificados...")
                self.add_modified_files_automatically(modified_files)
            
            # 4. Verificar arquivos deletados
            deleted_files = self.get_deleted_files()
            if deleted_files:
                self.logger.info(f"🗑️ Removendo {len(deleted_files)} arquivos deletados...")
                self.remove_deleted_files_automatically(deleted_files)
            
            # 5. Verificar conflitos de merge
            if self.has_merge_conflicts():
                self.logger.info("⚠️ Resolvendo conflitos de merge automaticamente...")
                self.resolve_merge_conflicts_automatically()
            
            # 6. Verificar staging area
            if self.is_staging_area_empty():
                self.logger.info("📦 Adicionando mudanças ao staging...")
                self.add_changed_files_automatically()
            
            self.logger.info("✅ Resolução automática de erros concluída!")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro na resolução automática: {e}")
            return False
    
    def is_git_repo(self) -> bool:
        """Verifica se é um repositório Git."""
        try:
            result = subprocess.run(['git', 'rev-parse', '--git-dir'], 
                                  capture_output=True, text=True, cwd=self.project_root)
            return result.returncode == 0
        except Exception:
            return False
    
    def initialize_git_repo(self) -> bool:
        """Inicializa repositório Git automaticamente."""
        try:
            subprocess.run(['git', 'init'], check=True, cwd=self.project_root)
            self.logger.info("✅ Repositório Git inicializado")
            return True
        except Exception as e:
            self.logger.error(f"❌ Erro ao inicializar Git: {e}")
            return False
    
    def get_untracked_files(self) -> List[str]:
        """Obtém lista de arquivos não rastreados."""
        try:
            result = subprocess.run(['git', 'status', '--porcelain'], 
                                  capture_output=True, text=True, cwd=self.project_root)
            untracked = []
            for line in result.stdout.splitlines():
                if line.startswith('??'):
                    file_path = line[3:].strip()
                    untracked.append(file_path)
            return untracked
        except Exception:
            return []
    
    def get_modified_files(self) -> List[str]:
        """Obtém lista de arquivos modificados."""
        try:
            result = subprocess.run(['git', 'status', '--porcelain'], 
                                  capture_output=True, text=True, cwd=self.project_root)
            modified = []
            for line in result.stdout.splitlines():
                if line.startswith(' M') or line.startswith('M '):
                    file_path = line[3:].strip()
                    modified.append(file_path)
            return modified
        except Exception:
            return []
    
    def get_deleted_files(self) -> List[str]:
        """Obtém lista de arquivos deletados."""
        try:
            result = subprocess.run(['git', 'status', '--porcelain'], 
                                  capture_output=True, text=True, cwd=self.project_root)
            deleted = []
            for line in result.stdout.splitlines():
                if line.startswith(' D') or line.startswith('D '):
                    file_path = line[3:].strip()
                    deleted.append(file_path)
            return deleted
        except Exception:
            return []
    
    def add_untracked_files_automatically(self, files: List[str]) -> bool:
        """Adiciona arquivos não rastreados automaticamente."""
        try:
            for file_path in files:
                subprocess.run(['git', 'add', file_path], check=True, cwd=self.project_root)
            self.logger.info(f"✅ {len(files)} arquivos não rastreados adicionados")
            return True
        except Exception as e:
            self.logger.error(f"❌ Erro ao adicionar arquivos: {e}")
            return False
    
    def add_modified_files_automatically(self, files: List[str]) -> bool:
        """Adiciona arquivos modificados automaticamente."""
        try:
            for file_path in files:
                subprocess.run(['git', 'add', file_path], check=True, cwd=self.project_root)
            self.logger.info(f"✅ {len(files)} arquivos modificados adicionados")
            return True
        except Exception as e:
            self.logger.error(f"❌ Erro ao adicionar arquivos modificados: {e}")
            return False
    
    def remove_deleted_files_automatically(self, files: List[str]) -> bool:
        """Remove arquivos deletados automaticamente."""
        try:
            for file_path in files:
                subprocess.run(['git', 'rm', file_path], check=True, cwd=self.project_root)
            self.logger.info(f"✅ {len(files)} arquivos deletados removidos")
            return True
        except Exception as e:
            self.logger.error(f"❌ Erro ao remover arquivos: {e}")
            return False
    
    def has_merge_conflicts(self) -> bool:
        """Verifica se há conflitos de merge."""
        try:
            result = subprocess.run(['git', 'status', '--porcelain'], 
                                  capture_output=True, text=True, cwd=self.project_root)
            return 'UU' in result.stdout or 'AA' in result.stdout
        except Exception:
            return False
    
    def resolve_merge_conflicts_automatically(self) -> bool:
        """Resolve conflitos de merge automaticamente."""
        try:
            # Estratégia: aceitar versão atual (ours)
            subprocess.run(['git', 'checkout', '--ours', '.'], check=True, cwd=self.project_root)
            subprocess.run(['git', 'add', '.'], check=True, cwd=self.project_root)
            self.logger.info("✅ Conflitos de merge resolvidos automaticamente")
            return True
        except Exception as e:
            self.logger.error(f"❌ Erro ao resolver conflitos: {e}")
            return False
    
    def is_staging_area_empty(self) -> bool:
        """Verifica se a staging area está vazia."""
        try:
            result = subprocess.run(['git', 'diff', '--cached', '--name-only'], 
                                  capture_output=True, text=True, cwd=self.project_root)
            return not result.stdout.strip()
        except Exception:
            return True
    
    def add_changed_files_automatically(self) -> bool:
        """Adiciona todas as mudanças automaticamente."""
        try:
            subprocess.run(['git', 'add', '.'], check=True, cwd=self.project_root)
            self.logger.info("✅ Todas as mudanças adicionadas ao staging")
            return True
        except Exception as e:
            self.logger.error(f"❌ Erro ao adicionar mudanças: {e}")
            return False
    
    def analyze_changes_by_context(self) -> Dict[str, List[str]]:
        """
        Analisa mudanças e as separa por contexto para commits atômicos.
        
        Returns:
            Dicionário com mudanças separadas por contexto
        """
        try:
            result = subprocess.run(['git', 'status', '--porcelain'], 
                                  capture_output=True, text=True, cwd=self.project_root)
            
            changes_by_context = {
                'documentation': [],
                'rules': [],
                'scripts': [],
                'wiki': [],
                'logs': [],
                'maps': [],
                'other': []
            }
            
            for line in result.stdout.splitlines():
                if not line.strip():
                    continue
                
                file_path = line[3:].strip()
                
                # Categorizar por contexto
                if file_path.startswith('.cursor/rules/'):
                    changes_by_context['rules'].append(file_path)
                elif file_path.startswith('wiki/update/'):
                    changes_by_context['scripts'].append(file_path)
                elif file_path.startswith('wiki/log/'):
                    changes_by_context['logs'].append(file_path)
                elif file_path.startswith('wiki/maps/'):
                    changes_by_context['maps'].append(file_path)
                elif file_path.startswith('wiki/') and file_path.endswith('.md'):
                    changes_by_context['wiki'].append(file_path)
                elif file_path.endswith('.md'):
                    changes_by_context['documentation'].append(file_path)
                else:
                    changes_by_context['other'].append(file_path)
            
            # Remover contextos vazios
            return {k: v for k, v in changes_by_context.items() if v}
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao analisar mudanças: {e}")
            return {}
    
    def create_atomic_commits(self, changes_by_context: Dict[str, List[str]], task_info: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Cria commits atômicos baseados no contexto das mudanças.
        
        Args:
            changes_by_context: Mudanças separadas por contexto
            task_info: Informações da tarefa ativa
            
        Returns:
            Lista de resultados dos commits
        """
        commit_results = []
        
        for context, files in changes_by_context.items():
            if not files:
                continue
            
            self.logger.info(f"📦 Criando commit atômico para contexto: {context}")
            
            # Adicionar apenas arquivos deste contexto
            try:
                for file_path in files:
                    subprocess.run(['git', 'add', file_path], check=True, cwd=self.project_root)
                
                # Gerar mensagem de commit baseada no contexto
                commit_message = self.generate_contextual_commit_message(context, files, task_info)
                
                # Executar commit
                result = subprocess.run(['git', 'commit', '-m', commit_message], 
                                      capture_output=True, text=True, cwd=self.project_root)
                
                if result.returncode == 0:
                    commit_hash = self.extract_commit_hash(result.stdout)
                    commit_result = {
                        'context': context,
                        'files': files,
                        'message': commit_message,
                        'hash': commit_hash,
                        'success': True
                    }
                    commit_results.append(commit_result)
                    self.logger.info(f"✅ Commit atômico criado: {commit_hash[:8]} - {context}")
                else:
                    commit_result = {
                        'context': context,
                        'files': files,
                        'message': commit_message,
                        'error': result.stderr,
                        'success': False
                    }
                    commit_results.append(commit_result)
                    self.logger.error(f"❌ Erro no commit: {result.stderr}")
                
            except Exception as e:
                self.logger.error(f"❌ Erro ao criar commit para {context}: {e}")
                commit_results.append({
                    'context': context,
                    'files': files,
                    'error': str(e),
                    'success': False
                })
        
        return commit_results
    
    def generate_contextual_commit_message(self, context: str, files: List[str], task_info: Optional[Dict[str, Any]] = None) -> str:
        """
        Gera mensagem de commit contextual em português.
        
        Args:
            context: Contexto das mudanças
            files: Lista de arquivos modificados
            task_info: Informações da tarefa ativa
            
        Returns:
            Mensagem de commit em formato Conventional Commits
        """
        # Mapear contexto para tipo de commit
        context_to_type = {
            'documentation': 'docs',
            'rules': 'refactor',
            'scripts': 'feat',
            'wiki': 'docs',
            'logs': 'chore',
            'maps': 'refactor',
            'other': 'chore'
        }
        
        commit_type = context_to_type.get(context, 'chore')
        
        # Gerar descrição baseada no contexto
        context_descriptions = {
            'documentation': 'atualizar documentação',
            'rules': 'atualizar regras do sistema',
            'scripts': 'melhorar scripts de automação',
            'wiki': 'atualizar documentação da wiki',
            'logs': 'atualizar logs do sistema',
            'maps': 'atualizar mapas JSON',
            'other': 'atualizar arquivos do sistema'
        }
        
        description = context_descriptions.get(context, 'atualizar arquivos')
        
        # Adicionar contexto de tarefa se disponível
        if task_info and task_info.get('task_id'):
            description += f" - {task_info['task_id']}"
        
        # Adicionar número de arquivos se relevante
        if len(files) > 1:
            description += f" ({len(files)} arquivos)"
        
        return f"{commit_type}: {description}"
    
    def extract_commit_hash(self, git_output: str) -> str:
        """Extrai hash do commit da saída do Git."""
        match = re.search(r'\[([a-f0-9]+)\]', git_output)
        if match:
            return match.group(1)
        
        # Fallback: buscar hash completo
        match = re.search(r'([a-f0-9]{40})', git_output)
        if match:
            return match.group(1)
        
        return "unknown"
    
    def get_active_task(self) -> Optional[Dict[str, Any]]:
        """
        Obtém informações da tarefa ativa.
        
        Returns:
            Informações da tarefa ativa ou None
        """
        try:
            temp_tasks_dir = self.task_log_dir / 'temp_tasks'
            if not temp_tasks_dir.exists():
                return None
            
            # Encontrar tarefa mais recente
            task_files = list(temp_tasks_dir.glob('TASK_*.md'))
            if not task_files:
                return None
            
            latest_task = max(task_files, key=lambda x: x.stat().st_mtime)
            task_content = latest_task.read_text(encoding='utf-8')
            
            # Extrair informações da tarefa
            task_info = {
                'file_path': str(latest_task),
                'modified_time': latest_task.stat().st_mtime,
                'content': task_content
            }
            
            # Extrair ID da tarefa
            task_id_match = re.search(r'TASK-\d+', task_content)
            if task_id_match:
                task_info['task_id'] = task_id_match.group()
            
            # Extrair título da tarefa
            title_match = re.search(r'# Tarefa: (.+)', task_content)
            if title_match:
                task_info['title'] = title_match.group(1).strip()
            
            # Extrair status da tarefa
            status_match = re.search(r'\*\*Status\*\*: (.+)', task_content)
            if status_match:
                task_info['status'] = status_match.group(1).strip()
            
            # Verificar se está em andamento
            if 'Em Andamento' in task_info.get('status', ''):
                self.logger.info(f"📋 Tarefa ativa encontrada: {task_info.get('task_id', 'Unknown')}")
                return task_info
            
            return None
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao obter tarefa ativa: {e}")
            return None
    
    def auto_commit_atomic(self, auto_push: bool = False) -> Dict[str, Any]:
        """
        Executa commit automático e atômico com resolução de erros.
        
        Args:
            auto_push: Se deve fazer push automático
            
        Returns:
            Resultado da operação
        """
        self.logger.info("🚀 Iniciando commit automático e atômico...")
        
        try:
            # 1. Resolver erros automaticamente
            if not self.resolve_git_errors_automatically():
                return {
                    'success': False,
                    'error': 'Falha na resolução automática de erros',
                    'timestamp': datetime.now().isoformat()
                }
            
            # 2. Obter tarefa ativa
            task_info = self.get_active_task()
            
            # 3. Analisar mudanças por contexto
            changes_by_context = self.analyze_changes_by_context()
            
            if not changes_by_context:
                return {
                    'success': True,
                    'message': 'Nenhuma mudança detectada',
                    'commits': [],
                    'timestamp': datetime.now().isoformat()
                }
            
            # 4. Criar commits atômicos
            commit_results = self.create_atomic_commits(changes_by_context, task_info)
            
            # 5. Fazer push se solicitado
            push_result = None
            if auto_push and any(c['success'] for c in commit_results):
                push_result = self.auto_push()
            
            # 6. Gerar relatório
            report = self.generate_commit_report(commit_results, task_info, push_result)
            
            return {
                'success': True,
                'commits': commit_results,
                'push': push_result,
                'report': report,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erro no commit automático: {e}")
            return {
                'success': False,
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    def auto_push(self) -> Dict[str, Any]:
        """Executa push automático."""
        try:
            result = subprocess.run(['git', 'push'], 
                                  capture_output=True, text=True, cwd=self.project_root)
            
            if result.returncode == 0:
                self.logger.info("✅ Push realizado com sucesso")
                return {
                    'success': True,
                    'message': 'Push realizado com sucesso'
                }
            else:
                self.logger.error(f"❌ Erro no push: {result.stderr}")
                return {
                    'success': False,
                    'error': result.stderr
                }
                
        except Exception as e:
            self.logger.error(f"❌ Erro no push: {e}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def generate_commit_report(self, commit_results: List[Dict[str, Any]], task_info: Optional[Dict[str, Any]], push_result: Optional[Dict[str, Any]]) -> str:
        """Gera relatório detalhado dos commits."""
        report = f"""# Relatório de Commit Automático e Atômico

**Data**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Status**: {'✅ Sucesso' if all(c['success'] for c in commit_results) else '⚠️ Parcial'}

## 📊 Resumo dos Commits

"""
        
        successful_commits = [c for c in commit_results if c['success']]
        failed_commits = [c for c in commit_results if not c['success']]
        
        report += f"- **Commits realizados**: {len(successful_commits)}\n"
        report += f"- **Commits com erro**: {len(failed_commits)}\n"
        report += f"- **Taxa de sucesso**: {len(successful_commits)/len(commit_results)*100:.1f}%\n\n"
        
        if task_info:
            report += f"## 📋 Contexto da Tarefa\n"
            report += f"- **ID**: {task_info.get('task_id', 'N/A')}\n"
            report += f"- **Título**: {task_info.get('title', 'N/A')}\n"
            report += f"- **Status**: {task_info.get('status', 'N/A')}\n\n"
        
        if successful_commits:
            report += "## ✅ Commits Realizados\n\n"
            for commit in successful_commits:
                report += f"### {commit['context'].title()}\n"
                report += f"- **Hash**: {commit['hash'][:8]}\n"
                report += f"- **Mensagem**: {commit['message']}\n"
                report += f"- **Arquivos**: {len(commit['files'])}\n\n"
        
        if failed_commits:
            report += "## ❌ Commits com Erro\n\n"
            for commit in failed_commits:
                report += f"### {commit['context'].title()}\n"
                report += f"- **Erro**: {commit.get('error', 'Erro desconhecido')}\n"
                report += f"- **Arquivos**: {len(commit['files'])}\n\n"
        
        if push_result:
            report += "## 🚀 Push\n"
            if push_result['success']:
                report += f"- **Status**: ✅ {push_result['message']}\n"
            else:
                report += f"- **Status**: ❌ {push_result['error']}\n"
        
        return report

def main():
    """Função principal."""
    
    parser = argparse.ArgumentParser(description='Integração Git + Sistema de Tarefas - Automático e Atômico')
    parser.add_argument('--auto-commit', action='store_true', help='Executar commit automático')
    parser.add_argument('--auto-push', action='store_true', help='Fazer push automático após commit')
    parser.add_argument('--resolve-errors', action='store_true', help='Apenas resolver erros Git')
    parser.add_argument('--analyze-changes', action='store_true', help='Apenas analisar mudanças')
    
    args = parser.parse_args()
    
    integration = GitTaskIntegration()
    
    if args.resolve_errors:
        success = integration.resolve_git_errors_automatically()
        print(f"{'✅' if success else '❌'} Resolução de erros {'concluída' if success else 'falhou'}")
        return
    
    if args.analyze_changes:
        changes = integration.analyze_changes_by_context()
        print("📊 Análise de mudanças por contexto:")
        for context, files in changes.items():
            print(f"  {context}: {len(files)} arquivos")
        return
    
    if args.auto_commit:
        result = integration.auto_commit_atomic(args.auto_push)
        if result['success']:
            print("✅ Commit automático e atômico realizado com sucesso!")
            print(f"📊 {len(result['commits'])} commits criados")
            if result.get('push', {}).get('success'):
                print("🚀 Push realizado com sucesso!")
        else:
            print(f"❌ Erro no commit automático: {result['error']}")
        return
    
    # Modo padrão: commit automático
    result = integration.auto_commit_atomic(False)
    if result['success']:
        print("✅ Commit automático e atômico realizado com sucesso!")
        print(f"📊 {len(result['commits'])} commits criados")
    else:
        print(f"❌ Erro no commit automático: {result['error']}")

if __name__ == '__main__':
    main() 