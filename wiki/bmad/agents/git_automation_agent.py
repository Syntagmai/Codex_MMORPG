#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agente de Automação Git - Sistema BMAD
======================================

Agente especializado em automação Git com boas práticas,
validação automática e geração inteligente de commits em português.

Funcionalidades:
- Análise automática de mudanças
- Geração inteligente de mensagens de commit
- Validação de boas práticas
- Integração com sistema de tarefas
- Hooks de pre-commit
- Atalhos no Cursor IDE
- Análise inteligente de diffs
- Separação automática de commits por contexto
- Detecção de arquivos abertos no IDE

Autor: Sistema BMAD - OTClient Documentation
Data: 2024-12-19
Versão: 1.1
"""

import subprocess
import re
import json
import logging
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import sys
import argparse
import difflib

# Configuração de logging
log_dir = Path.cwd() / 'wiki' / 'log'
log_dir.mkdir(parents=True, exist_ok=True)
log_file = log_dir / 'git_automation.log'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

class GitAutomationAgent:
    """Agente de automação Git com boas práticas em português."""
    
    def __init__(self, project_root: str = "."):
        """
        Inicializa o agente de automação Git.
        
        Args:
            project_root: Caminho raiz do projeto
        """
        self.project_root = Path(project_root)
        self.logger = logging.getLogger(__name__)
        
        # Tipos de commit convencionais
        self.conventional_types = {
            'feat': 'Nova funcionalidade',
            'fix': 'Correção de bug',
            'docs': 'Documentação',
            'style': 'Formatação',
            'refactor': 'Refatoração',
            'test': 'Testes',
            'chore': 'Manutenção',
            'perf': 'Melhoria de performance',
            'ci': 'Integração contínua',
            'build': 'Build do sistema'
        }
        
        # Padrões de arquivos por tipo
        self.file_patterns = {
            'docs': ['.md', '.txt', '.rst'],
            'test': ['test_', '_test.py', '.spec.js'],
            'style': ['.css', '.scss', '.less'],
            'build': ['Dockerfile', '.yml', '.yaml', 'package.json'],
            'ci': ['.github/', '.gitlab-ci.yml', 'travis.yml']
        }
        
        # Configurações de análise inteligente
        self.analysis_config = {
            'max_commit_size': 10,  # Máximo de arquivos por commit
            'context_threshold': 0.7,  # Similaridade mínima para agrupar
            'min_commit_size': 1,  # Mínimo de arquivos por commit
            'enable_smart_splitting': True,  # Ativar separação inteligente
            'detect_open_files': True,  # Detectar arquivos abertos
            'group_by_context': True,  # Agrupar por contexto
            'group_by_type': True,  # Agrupar por tipo de arquivo
            'group_by_directory': True,  # Agrupar por diretório
        }
        
        self.logger.info("Agente de Automação Git inicializado")
    
    def analyze_changes(self) -> Dict[str, Any]:
        """
        Analisa mudanças no repositório Git.
        
        Returns:
            Dicionário com informações das mudanças
        """
        try:
            self.logger.info("Analisando mudanças no repositório...")
            
            # Obter status das mudanças
            result = subprocess.run(
                ['git', 'status', '--porcelain'],
                capture_output=True, text=True, cwd=self.project_root
            )
            
            if result.returncode != 0:
                self.logger.error(f"Erro ao obter status Git: {result.stderr}")
                return {}
            
            changes = {
                'modified': [],
                'added': [],
                'deleted': [],
                'renamed': [],
                'untracked': [],
                'type': 'unknown',
                'summary': '',
                'task_context': self._detect_task_context(),
                'open_files': self._detect_open_files(),
                'commit_groups': []
            }
            
            # Processar cada linha do status
            for line in result.stdout.strip().split('\n'):
                if line:
                    status = line[:2]
                    file_path = line[3:]
                    
                    if status.startswith('M'):
                        changes['modified'].append(file_path)
                    elif status.startswith('A'):
                        changes['added'].append(file_path)
                    elif status.startswith('D'):
                        changes['deleted'].append(file_path)
                    elif status.startswith('R'):
                        changes['renamed'].append(file_path)
                    elif status == '??':
                        changes['untracked'].append(file_path)
            
            # Análise inteligente de mudanças
            if self.analysis_config['enable_smart_splitting']:
                changes['commit_groups'] = self._analyze_commit_groups(changes)
            
            # Determinar tipo de commit
            changes['type'] = self._determine_commit_type(changes)
            changes['summary'] = self._generate_change_summary(changes)
            
            self.logger.info(f"Tipo de commit detectado: {changes['type']}")
            self.logger.info(f"Resumo: {changes['summary']}")
            self.logger.info(f"Grupos de commit: {len(changes['commit_groups'])}")
            
            return changes
            
        except Exception as e:
            self.logger.error(f"Erro ao analisar mudanças: {e}")
            return {}
    
    def _detect_task_context(self) -> Dict[str, Any]:
        """
        Detecta contexto de tarefa atual.
        
        Returns:
            Informações do contexto de tarefa
        """
        try:
            # Verificar se existe tarefa ativa
            task_files = list(Path('wiki/log/temp_tasks').glob('TASK_*.md'))
            
            if task_files:
                latest_task = max(task_files, key=lambda x: x.stat().st_mtime)
                task_content = latest_task.read_text(encoding='utf-8')
                
                # Extrair informações da tarefa
                task_id_match = re.search(r'TASK-\d+', task_content)
                task_title_match = re.search(r'# Tarefa: (.+)', task_content)
                
                return {
                    'active_task': True,
                    'task_id': task_id_match.group() if task_id_match else 'Unknown',
                    'task_title': task_title_match.group(1) if task_title_match else 'Tarefa Ativa',
                    'task_file': str(latest_task)
                }
            
            return {'active_task': False}
            
        except Exception as e:
            self.logger.warning(f"Erro ao detectar contexto de tarefa: {e}")
            return {'active_task': False}
    
    def _detect_open_files(self) -> List[str]:
        """
        Detecta arquivos abertos no IDE.
        
        Returns:
            Lista de arquivos abertos
        """
        try:
            open_files = []
            
            # Verificar arquivos temporários do Cursor/VS Code
            cursor_temp_dir = Path.home() / '.cursor' / 'temp'
            vscode_temp_dir = Path.home() / '.vscode' / 'temp'
            
            # Verificar arquivos de sessão
            session_files = [
                '.vscode/settings.json',
                '.cursor/settings.json',
                '.git/index.lock'
            ]
            
            for session_file in session_files:
                if Path(session_file).exists():
                    open_files.append(session_file)
            
            # Verificar arquivos modificados recentemente (últimos 5 minutos)
            current_time = datetime.now()
            for file_path in Path('.').rglob('*'):
                if file_path.is_file() and not file_path.name.startswith('.'):
                    try:
                        mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
                        if (current_time - mtime).seconds < 300:  # 5 minutos
                            open_files.append(str(file_path))
                    except:
                        continue
            
            return list(set(open_files))  # Remover duplicatas
            
        except Exception as e:
            self.logger.warning(f"Erro ao detectar arquivos abertos: {e}")
            return []
    
    def _analyze_commit_groups(self, changes: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Analisa e agrupa mudanças para commits separados.
        
        Args:
            changes: Dicionário com informações das mudanças
            
        Returns:
            Lista de grupos de commit
        """
        try:
            all_files = changes['modified'] + changes['added'] + changes['deleted'] + changes['untracked']
            
            if len(all_files) <= self.analysis_config['max_commit_size']:
                # Se poucos arquivos, fazer commit único
                return [{
                    'type': changes['type'],
                    'files': all_files,
                    'reason': 'commit_único',
                    'message': self._generate_group_message(all_files, changes['type'])
                }]
            
            groups = []
            
            # Agrupar por diretório
            if self.analysis_config['group_by_directory']:
                dir_groups = self._group_by_directory(all_files)
                groups.extend(dir_groups)
            
            # Agrupar por tipo de arquivo
            if self.analysis_config['group_by_type']:
                type_groups = self._group_by_file_type(all_files)
                groups.extend(type_groups)
            
            # Agrupar por contexto (análise de diff)
            if self.analysis_config['group_by_context']:
                context_groups = self._group_by_context(all_files)
                groups.extend(context_groups)
            
            # Consolidar grupos sobrepostos
            consolidated_groups = self._consolidate_groups(groups)
            
            # Garantir que cada arquivo está em apenas um grupo
            final_groups = self._ensure_unique_files(consolidated_groups, all_files)
            
            return final_groups
            
        except Exception as e:
            self.logger.error(f"Erro ao analisar grupos de commit: {e}")
            return []
    
    def _group_by_directory(self, files: List[str]) -> List[Dict[str, Any]]:
        """
        Agrupa arquivos por diretório.
        
        Args:
            files: Lista de arquivos
            
        Returns:
            Lista de grupos por diretório
        """
        groups = {}
        
        for file_path in files:
            directory = str(Path(file_path).parent)
            
            if directory not in groups:
                groups[directory] = {
                    'type': self._determine_type_from_files([file_path]),
                    'files': [],
                    'reason': f'diretório_{directory}'
                }
            
            groups[directory]['files'].append(file_path)
        
        return list(groups.values())
    
    def _group_by_file_type(self, files: List[str]) -> List[Dict[str, Any]]:
        """
        Agrupa arquivos por tipo.
        
        Args:
            files: Lista de arquivos
            
        Returns:
            Lista de grupos por tipo
        """
        groups = {}
        
        for file_path in files:
            file_type = self._get_file_type(file_path)
            
            if file_type not in groups:
                groups[file_type] = {
                    'type': file_type,
                    'files': [],
                    'reason': f'tipo_{file_type}'
                }
            
            groups[file_type]['files'].append(file_path)
        
        return list(groups.values())
    
    def _group_by_context(self, files: List[str]) -> List[Dict[str, Any]]:
        """
        Agrupa arquivos por contexto usando análise de diff.
        
        Args:
            files: Lista de arquivos
            
        Returns:
            Lista de grupos por contexto
        """
        groups = []
        
        for file_path in files:
            if Path(file_path).exists():
                diff_content = self._get_file_diff(file_path)
                context = self._extract_context_from_diff(diff_content)
                
                # Procurar grupo similar
                similar_group = None
                for group in groups:
                    if self._is_similar_context(group.get('context', ''), context):
                        similar_group = group
                        break
                
                if similar_group:
                    similar_group['files'].append(file_path)
                else:
                    groups.append({
                        'type': self._determine_type_from_files([file_path]),
                        'files': [file_path],
                        'reason': 'contexto_similar',
                        'context': context
                    })
        
        return groups
    
    def _get_file_diff(self, file_path: str) -> str:
        """
        Obtém o diff de um arquivo.
        
        Args:
            file_path: Caminho do arquivo
            
        Returns:
            Conteúdo do diff
        """
        try:
            result = subprocess.run(
                ['git', 'diff', file_path],
                capture_output=True, text=True, cwd=self.project_root
            )
            
            if result.returncode == 0:
                return result.stdout
            else:
                # Se não há diff, verificar se é arquivo novo
                result = subprocess.run(
                    ['git', 'diff', '--cached', file_path],
                    capture_output=True, text=True, cwd=self.project_root
                )
                return result.stdout if result.returncode == 0 else ""
                
        except Exception as e:
            self.logger.warning(f"Erro ao obter diff de {file_path}: {e}")
            return ""
    
    def _extract_context_from_diff(self, diff_content: str) -> str:
        """
        Extrai contexto do diff.
        
        Args:
            diff_content: Conteúdo do diff
            
        Returns:
            Contexto extraído
        """
        try:
            # Extrair palavras-chave do diff
            lines = diff_content.split('\n')
            context_words = []
            
            for line in lines:
                if line.startswith('+') and not line.startswith('+++'):
                    # Linhas adicionadas
                    words = re.findall(r'\b\w+\b', line[1:])
                    context_words.extend(words[:5])  # Primeiras 5 palavras
                elif line.startswith('-') and not line.startswith('---'):
                    # Linhas removidas
                    words = re.findall(r'\b\w+\b', line[1:])
                    context_words.extend(words[:5])
            
            return ' '.join(context_words[:10])  # Primeiras 10 palavras
            
        except Exception as e:
            self.logger.warning(f"Erro ao extrair contexto: {e}")
            return ""
    
    def _is_similar_context(self, context1: str, context2: str) -> bool:
        """
        Verifica se dois contextos são similares.
        
        Args:
            context1: Primeiro contexto
            context2: Segundo contexto
            
        Returns:
            True se similares
        """
        try:
            if not context1 or not context2:
                return False
            
            # Usar difflib para calcular similaridade
            similarity = difflib.SequenceMatcher(None, context1.lower(), context2.lower()).ratio()
            return similarity >= self.analysis_config['context_threshold']
            
        except Exception as e:
            self.logger.warning(f"Erro ao comparar contextos: {e}")
            return False
    
    def _consolidate_groups(self, groups: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Consolida grupos sobrepostos.
        
        Args:
            groups: Lista de grupos
            
        Returns:
            Lista de grupos consolidados
        """
        if not groups:
            return []
        
        consolidated = []
        
        for group in groups:
            # Verificar se há sobreposição com grupos existentes
            merged = False
            for existing_group in consolidated:
                overlap = set(group['files']) & set(existing_group['files'])
                if overlap:
                    # Mesclar grupos
                    existing_group['files'].extend(group['files'])
                    existing_group['files'] = list(set(existing_group['files']))  # Remover duplicatas
                    existing_group['reason'] = f"mesclado_{group['reason']}"
                    merged = True
                    break
            
            if not merged:
                consolidated.append(group)
        
        return consolidated
    
    def _ensure_unique_files(self, groups: List[Dict[str, Any]], all_files: List[str]) -> List[Dict[str, Any]]:
        """
        Garante que cada arquivo está em apenas um grupo.
        
        Args:
            groups: Lista de grupos
            all_files: Lista de todos os arquivos
            
        Returns:
            Lista de grupos com arquivos únicos
        """
        used_files = set()
        final_groups = []
        
        for group in groups:
            unique_files = [f for f in group['files'] if f not in used_files]
            if unique_files:
                group['files'] = unique_files
                used_files.update(unique_files)
                final_groups.append(group)
        
        # Adicionar arquivos não agrupados
        unused_files = [f for f in all_files if f not in used_files]
        if unused_files:
            final_groups.append({
                'type': self._determine_type_from_files(unused_files),
                'files': unused_files,
                'reason': 'arquivos_não_agrupados',
                'message': self._generate_group_message(unused_files, 'chore')
            })
        
        return final_groups
    
    def _get_file_type(self, file_path: str) -> str:
        """
        Determina o tipo de um arquivo.
        
        Args:
            file_path: Caminho do arquivo
            
        Returns:
            Tipo do arquivo
        """
        file_path_lower = file_path.lower()
        
        for file_type, patterns in self.file_patterns.items():
            for pattern in patterns:
                if pattern in file_path_lower:
                    return file_type
        
        # Determinar por extensão
        ext = Path(file_path).suffix.lower()
        if ext in ['.md', '.txt', '.rst']:
            return 'docs'
        elif ext in ['.py']:
            return 'feat'
        elif ext in ['.lua']:
            return 'feat'
        elif ext in ['.json']:
            return 'chore'
        elif ext in ['.css', '.scss', '.less']:
            return 'style'
        elif ext in ['.js', '.ts']:
            return 'feat'
        else:
            return 'chore'
    
    def _determine_type_from_files(self, files: List[str]) -> str:
        """
        Determina o tipo de commit baseado em uma lista de arquivos.
        
        Args:
            files: Lista de arquivos
            
        Returns:
            Tipo de commit
        """
        if not files:
            return 'chore'
        
        # Contar tipos de arquivo
        type_counts = {}
        for file_path in files:
            file_type = self._get_file_type(file_path)
            type_counts[file_type] = type_counts.get(file_type, 0) + 1
        
        # Retornar o tipo mais comum
        return max(type_counts.items(), key=lambda x: x[1])[0]
    
    def _generate_group_message(self, files: List[str], commit_type: str) -> str:
        """
        Gera mensagem para um grupo de arquivos.
        
        Args:
            files: Lista de arquivos
            commit_type: Tipo de commit
            
        Returns:
            Mensagem gerada
        """
        if not files:
            return f"{commit_type}: sem arquivos"
        
        # Gerar resumo baseado nos arquivos
        file_types = [self._get_file_type(f) for f in files]
        type_counts = {}
        for ft in file_types:
            type_counts[ft] = type_counts.get(ft, 0) + 1
        
        # Criar descrição
        descriptions = []
        for file_type, count in type_counts.items():
            if count == 1:
                descriptions.append(f"1 arquivo {file_type}")
            else:
                descriptions.append(f"{count} arquivos {file_type}")
        
        return f"{commit_type}: {', '.join(descriptions)}"
    
    def _determine_commit_type(self, changes: Dict[str, Any]) -> str:
        """
        Determina o tipo de commit baseado nas mudanças.
        
        Args:
            changes: Dicionário com informações das mudanças
            
        Returns:
            Tipo de commit convencional
        """
        all_files = changes['modified'] + changes['added']
        
        # Verificar padrões específicos
        for file_type, patterns in self.file_patterns.items():
            for pattern in patterns:
                if any(pattern in file for file in all_files):
                    return file_type
        
        # Verificar por extensões
        if any('.md' in file for file in all_files):
            return 'docs'
        elif any('.py' in file for file in all_files):
            return 'feat' if 'test' in str(changes) else 'fix'
        elif any('.lua' in file for file in all_files):
            return 'feat'
        elif any('.json' in file for file in all_files):
            return 'chore'
        elif any('.txt' in file for file in all_files):
            return 'docs'
        
        # Padrão baseado no contexto de tarefa
        if changes.get('task_context', {}).get('active_task'):
            return 'feat'  # Assumir nova funcionalidade se há tarefa ativa
        
        return 'chore'
    
    def _generate_change_summary(self, changes: Dict[str, Any]) -> str:
        """
        Gera resumo das mudanças em português.
        
        Args:
            changes: Dicionário com informações das mudanças
            
        Returns:
            Resumo das mudanças
        """
        parts = []
        
        if changes['modified']:
            parts.append(f"modificados {len(changes['modified'])} arquivos")
        if changes['added']:
            parts.append(f"adicionados {len(changes['added'])} arquivos")
        if changes['deleted']:
            parts.append(f"removidos {len(changes['deleted'])} arquivos")
        if changes['renamed']:
            parts.append(f"renomeados {len(changes['renamed'])} arquivos")
        if changes['untracked']:
            parts.append(f"não rastreados {len(changes['untracked'])} arquivos")
        
        if not parts:
            return "sem mudanças detectadas"
        
        return ", ".join(parts)
    
    def generate_commit_message(self, changes: Dict[str, Any]) -> str:
        """
        Gera mensagem de commit inteligente em português.
        
        Args:
            changes: Dicionário com informações das mudanças
            
        Returns:
            Mensagem de commit formatada
        """
        commit_type = changes['type']
        summary = changes['summary']
        task_context = changes.get('task_context', {})
        
        # Gerar título principal
        if task_context.get('active_task'):
            task_id = task_context['task_id']
            title = f"{commit_type}: {summary} - {task_id}"
        else:
            title = f"{commit_type}: {summary}"
        
        # Adicionar corpo detalhado
        body_parts = []
        
        # Informações das mudanças
        if changes['modified']:
            modified_files = changes['modified'][:5]  # Limitar a 5 arquivos
            body_parts.append(f"**Arquivos modificados:** {', '.join(modified_files)}")
            if len(changes['modified']) > 5:
                body_parts.append(f"... e mais {len(changes['modified']) - 5} arquivos")
        
        if changes['added']:
            added_files = changes['added'][:5]
            body_parts.append(f"**Arquivos adicionados:** {', '.join(added_files)}")
            if len(changes['added']) > 5:
                body_parts.append(f"... e mais {len(changes['added']) - 5} arquivos")
        
        if changes['deleted']:
            deleted_files = changes['deleted'][:5]
            body_parts.append(f"**Arquivos removidos:** {', '.join(deleted_files)}")
            if len(changes['deleted']) > 5:
                body_parts.append(f"... e mais {len(changes['deleted']) - 5} arquivos")
        
        if changes['untracked']:
            untracked_files = changes['untracked'][:5]
            body_parts.append(f"**Arquivos não rastreados:** {', '.join(untracked_files)}")
            if len(changes['untracked']) > 5:
                body_parts.append(f"... e mais {len(changes['untracked']) - 5} arquivos")
        
        # Contexto da tarefa
        if task_context.get('active_task'):
            body_parts.append(f"\n**Contexto:** {task_context['task_title']}")
        
        # Timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        body_parts.append(f"\n**Gerado automaticamente em:** {timestamp}")
        
        # Montar mensagem completa
        message = title
        
        if body_parts:
            message += f"\n\n" + "\n".join(body_parts)
        
        return message
    
    def validate_commit_message(self, message: str) -> Dict[str, Any]:
        """
        Valida mensagem de commit seguindo boas práticas.
        
        Args:
            message: Mensagem de commit a ser validada
            
        Returns:
            Resultado da validação
        """
        validation = {
            'valid': True,
            'errors': [],
            'warnings': [],
            'score': 100,
            'suggestions': []
        }
        
        lines = message.split('\n')
        title = lines[0]
        
        # Verificar formato Conventional Commits
        conventional_pattern = r'^(feat|fix|docs|style|refactor|test|chore|perf|ci|build)(\(.+\))?: .+'
        if not re.match(conventional_pattern, title):
            validation['errors'].append("❌ Formato não segue Conventional Commits")
            validation['score'] -= 30
            validation['suggestions'].append("Use formato: tipo: descrição")
        
        # Verificar tamanho da linha
        if len(title) > 72:
            validation['warnings'].append("⚠️ Primeira linha muito longa (>72 caracteres)")
            validation['score'] -= 10
            validation['suggestions'].append("Mantenha a primeira linha curta e descritiva")
        
        # Verificar se tem descrição
        if ':' in title:
            description = title.split(': ', 1)[1]
            if len(description) < 10:
                validation['warnings'].append("⚠️ Descrição muito curta")
                validation['score'] -= 10
                validation['suggestions'].append("Adicione uma descrição mais detalhada")
        
        # Verificar se tem corpo
        if len(lines) == 1:
            validation['warnings'].append("⚠️ Sem corpo detalhado")
            validation['score'] -= 5
            validation['suggestions'].append("Considere adicionar detalhes no corpo da mensagem")
        
        # Verificar caracteres especiais
        if re.search(r'[^\w\s\-:()]', title):
            validation['warnings'].append("⚠️ Caracteres especiais na primeira linha")
            validation['score'] -= 5
        
        validation['valid'] = len(validation['errors']) == 0
        return validation
    
    def execute_commit(self, message: str, auto_push: bool = False) -> Dict[str, Any]:
        """
        Executa commit com validação.
        
        Args:
            message: Mensagem de commit
            auto_push: Se deve fazer push automático
            
        Returns:
            Resultado da execução
        """
        try:
            self.logger.info("Executando commit...")
            
            # Validar mensagem
            validation = self.validate_commit_message(message)
            if not validation['valid']:
                self.logger.error("Validação falhou")
                return {
                    'success': False,
                    'errors': validation['errors'],
                    'warnings': validation['warnings'],
                    'suggestions': validation['suggestions']
                }
            
            # Adicionar arquivos
            self.logger.info("Adicionando arquivos...")
            subprocess.run(['git', 'add', '.'], cwd=self.project_root, check=True)
            
            # Fazer commit
            self.logger.info("Criando commit...")
            subprocess.run(
                ['git', 'commit', '-m', message],
                cwd=self.project_root, check=True
            )
            
            # Push automático se configurado
            if auto_push:
                self.logger.info("Fazendo push...")
                subprocess.run(['git', 'push'], cwd=self.project_root, check=True)
            
            self.logger.info("Commit executado com sucesso!")
            
            return {
                'success': True,
                'message': message,
                'validation': validation,
                'pushed': auto_push,
                'timestamp': datetime.now().isoformat()
            }
            
        except subprocess.CalledProcessError as e:
            error_msg = f"Erro Git: {e}"
            self.logger.error(error_msg)
            return {
                'success': False,
                'errors': [error_msg],
                'warnings': []
            }
        except Exception as e:
            error_msg = f"Erro inesperado: {e}"
            self.logger.error(error_msg)
            return {
                'success': False,
                'errors': [error_msg],
                'warnings': []
            }
    
    def auto_commit(self, auto_push: bool = False) -> Dict[str, Any]:
        """
        Executa commit automático completo.
        
        Args:
            auto_push: Se deve fazer push automático
            
        Returns:
            Resultado da execução
        """
        self.logger.info("Iniciando commit automático...")
        
        # Analisar mudanças
        changes = self.analyze_changes()
        if not changes:
            return {'success': False, 'error': 'Nenhuma mudança detectada'}
        
        # Gerar mensagem
        message = self.generate_commit_message(changes)
        
        # Executar commit
        result = self.execute_commit(message, auto_push)
        
        # Adicionar informações extras ao resultado
        if result['success']:
            result['changes'] = changes
            result['commit_type'] = changes['type']
            result['task_context'] = changes.get('task_context', {})
        
        return result

    def execute_multiple_commits(self, commit_groups: List[Dict[str, Any]], auto_push: bool = False) -> List[Dict[str, Any]]:
        """
        Executa múltiplos commits baseado nos grupos.
        
        Args:
            commit_groups: Lista de grupos de commit
            auto_push: Se deve fazer push automático
            
        Returns:
            Lista de resultados dos commits
        """
        results = []
        
        for i, group in enumerate(commit_groups):
            self.logger.info(f"Executando commit {i+1}/{len(commit_groups)}: {group['reason']}")
            
            # Adicionar arquivos do grupo
            for file_path in group['files']:
                try:
                    subprocess.run(['git', 'add', file_path], cwd=self.project_root, check=True)
                except subprocess.CalledProcessError as e:
                    self.logger.warning(f"Erro ao adicionar {file_path}: {e}")
                    # Tentar adicionar diretório se for um diretório
                    if Path(file_path).is_dir():
                        subprocess.run(['git', 'add', file_path], cwd=self.project_root, check=True)
            
            # Gerar mensagem
            message = group.get('message', self._generate_group_message(group['files'], group['type']))
            
            # Executar commit
            result = self.execute_commit(message, auto_push=False)  # Não fazer push individual
            result['group_info'] = group
            results.append(result)
        
        # Fazer push final se configurado
        if auto_push and results:
            try:
                subprocess.run(['git', 'push'], cwd=self.project_root, check=True)
                self.logger.info("Push final realizado com sucesso!")
            except Exception as e:
                self.logger.error(f"Erro no push final: {e}")
        
        return results

def main():
    """Função principal do agente."""
    parser = argparse.ArgumentParser(description='Agente de Automação Git')
    parser.add_argument('--auto-commit', action='store_true', help='Executar commit automático')
    parser.add_argument('--push', action='store_true', help='Fazer push após commit')
    parser.add_argument('--validate', type=str, help='Validar mensagem de commit')
    parser.add_argument('--analyze', action='store_true', help='Apenas analisar mudanças')
    parser.add_argument('--smart-commit', action='store_true', help='Commit inteligente com separação automática')
    parser.add_argument('--show-groups', action='store_true', help='Mostrar grupos de commit sugeridos')
    parser.add_argument('--detect-open', action='store_true', help='Detectar arquivos abertos no IDE')
    parser.add_argument('--max-files', type=int, default=10, help='Máximo de arquivos por commit')
    parser.add_argument('--similarity', type=float, default=0.7, help='Threshold de similaridade para agrupar')
    
    args = parser.parse_args()
    
    agent = GitAutomationAgent()
    
    # Atualizar configurações se fornecidas
    if args.max_files:
        agent.analysis_config['max_commit_size'] = args.max_files
    if args.similarity:
        agent.analysis_config['context_threshold'] = args.similarity
    
    if args.validate:
        # Validar mensagem específica
        validation = agent.validate_commit_message(args.validate)
        print(f"📊 Score: {validation['score']}/100")
        print(f"✅ Válido: {validation['valid']}")
        
        if validation['errors']:
            print("❌ Erros:")
            for error in validation['errors']:
                print(f"  {error}")
        
        if validation['warnings']:
            print("⚠️ Avisos:")
            for warning in validation['warnings']:
                print(f"  {warning}")
        
        if validation['suggestions']:
            print("💡 Sugestões:")
            for suggestion in validation['suggestions']:
                print(f"  {suggestion}")
    
    elif args.analyze:
        # Apenas analisar mudanças
        changes = agent.analyze_changes()
        if changes:
            print(f"📋 Tipo: {changes['type']}")
            print(f"📝 Resumo: {changes['summary']}")
            print(f"📁 Modificados: {len(changes['modified'])}")
            print(f"➕ Adicionados: {len(changes['added'])}")
            print(f"➖ Removidos: {len(changes['deleted'])}")
            print(f"🎯 Grupos de commit: {len(changes.get('commit_groups', []))}")
            
            if changes.get('task_context', {}).get('active_task'):
                print(f"🎯 Tarefa Ativa: {changes['task_context']['task_id']}")
            
            if changes.get('open_files'):
                print(f"📂 Arquivos abertos: {len(changes['open_files'])}")
        else:
            print("❌ Nenhuma mudança detectada")
    
    elif args.show_groups:
        # Mostrar grupos de commit sugeridos
        changes = agent.analyze_changes()
        if changes and changes.get('commit_groups'):
            print("🎯 Grupos de Commit Sugeridos:")
            print("=" * 50)
            
            for i, group in enumerate(changes['commit_groups'], 1):
                print(f"\n📦 Grupo {i}: {group['reason']}")
                print(f"   Tipo: {group['type']}")
                print(f"   Arquivos: {len(group['files'])}")
                print(f"   Mensagem: {group.get('message', 'N/A')}")
                print(f"   Arquivos:")
                for file_path in group['files']:
                    print(f"     - {file_path}")
        else:
            print("❌ Nenhum grupo de commit sugerido")
    
    elif args.detect_open:
        # Detectar arquivos abertos
        open_files = agent._detect_open_files()
        if open_files:
            print("📂 Arquivos Abertos Detectados:")
            print("=" * 40)
            for file_path in open_files:
                print(f"  - {file_path}")
        else:
            print("❌ Nenhum arquivo aberto detectado")
    
    elif args.smart_commit:
        # Commit inteligente com separação automática
        changes = agent.analyze_changes()
        if changes and changes.get('commit_groups'):
            print(f"🚀 Executando {len(changes['commit_groups'])} commits inteligentes...")
            results = agent.execute_multiple_commits(changes['commit_groups'], auto_push=args.push)
            
            print(f"\n✅ {len(results)} commits realizados com sucesso!")
            for i, result in enumerate(results, 1):
                if result['success']:
                    print(f"  {i}. {result['message'][:50]}...")
                else:
                    print(f"  {i}. ❌ Erro: {result.get('error', 'Erro desconhecido')}")
            
            if args.push:
                print("🚀 Push realizado!")
        else:
            print("❌ Nenhuma mudança para commit")
    
    elif args.auto_commit:
        # Commit automático
        result = agent.auto_commit(auto_push=args.push)
        
        if result['success']:
            print(f"✅ Commit realizado com sucesso!")
            print(f"📝 Mensagem: {result['message'][:100]}...")
            print(f"📊 Score: {result['validation']['score']}/100")
            if args.push:
                print("🚀 Push realizado!")
        else:
            print(f"❌ Erro no commit: {result.get('error', result.get('errors', []))}")
    
    else:
        # Modo interativo
        print("🤖 Agente de Automação Git - Sistema BMAD")
        print("Use --help para ver opções disponíveis")

if __name__ == "__main__":
    main() 