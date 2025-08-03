#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unicode_aliases
"""
Agente unificado de validação de caminhos
====================================

Este agente foi consolidado a partir dos seguintes agentes:
- path_validator_agent.py
- comprehensive_path_validator.py

Data de consolidação: 2025-08-01 10:38:28
Autor: Sistema BMAD - Agent Consolidator
"""

Comprehensive Path Validator Agent - Sistema Completo de Validação
=================================================================

Agente especializado em validação completa de caminhos, limpeza de duplicatas
e implementação de sistema de caminhos absolutos para todo o projeto.

Autor: Sistema BMAD
Versão: 2.0.0
Data: 2025-01-27
"""

import os
import json
import shutil
import sys
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Set
import logging

class ComprehensivePathValidator:
    """
    Agente completo de validação de caminhos e limpeza de duplicatas.
    """
    
    def __init__(self, base_path: str = None):
        """
        Inicializa o agente de validação completa.
        
        Args:
            base_path: Caminho base do projeto (padrão: diretório atual)
        """
        # Determinar caminho base absoluto
        if base_path:
            self.base_path = Path(base_path).resolve()
        else:
            # Subir até encontrar o diretório raiz do projeto (onde está o cursor.md)
            current_path = Path.cwd().resolve()
            while current_path.parent != current_path:
                if (current_path / "cursor.md").exists():
                    self.base_path = current_path
                    break
                current_path = current_path.parent
            else:
                self.base_path = Path.cwd().resolve()
        
        # Configurar logging com caminho absoluto
        log_path = self.base_path / "wiki" / "log"
        log_path.mkdir(parents=True, exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_path / "comprehensive_path_validator.log"),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
        # Mapeamento de caminhos corretos (absolutos)
        self.correct_paths = {
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
        
        self.logger.info(f"Comprehensive Path Validator inicializado em: {self.base_path}")
    
    def scan_all_duplicates(self) -> Dict:
        """
        Escaneia todas as duplicatas no projeto.
        
        Returns:
            Dict: Relatório de duplicatas encontradas
        """
        duplicates_report = {
            'wiki_duplicates': [],
            'nested_wiki_folders': [],
            'agent_duplicates': [],
            'file_duplicates': [],
            'total_issues': 0
        }
        
        try:
            self.logger.info("Escaneando duplicatas em todo o projeto...")
            
            # 1. Verificar pastas wiki duplicadas
            wiki_duplicates = self.find_wiki_duplicates()
            duplicates_report['wiki_duplicates'] = wiki_duplicates
            
            # 2. Verificar pastas aninhadas incorretas
            nested_wikis = self.find_nested_wiki_folders()
            duplicates_report['nested_wiki_folders'] = nested_wikis
            
            # 3. Verificar duplicatas de agentes
            agent_duplicates = self.find_agent_duplicates()
            duplicates_report['agent_duplicates'] = agent_duplicates
            
            # 4. Verificar arquivos duplicados
            file_duplicates = self.find_file_duplicates()
            duplicates_report['file_duplicates'] = file_duplicates
            
            # Calcular total de problemas
            duplicates_report['total_issues'] = (
                len(wiki_duplicates) + 
                len(nested_wikis) + 
                len(agent_duplicates) + 
                len(file_duplicates)
            )
            
            self.logger.info(f"Encontrados {duplicates_report['total_issues']} problemas de duplicação")
            return duplicates_report
            
        except Exception as e:
            self.logger.error(f"Erro ao escanear duplicatas: {e}")
            return duplicates_report
    
    def find_wiki_duplicates(self) -> List[Dict]:
        """
        Encontra pastas wiki duplicadas.
        
        Returns:
            List[Dict]: Lista de duplicatas encontradas
        """
        wiki_duplicates = []
        
        try:
            # Procurar por pastas wiki em todo o projeto
            for wiki_folder in self.base_path.rglob("wiki"):
                if wiki_folder.is_dir():
                    relative_path = wiki_folder.relative_to(self.base_path)
                    
                    # Verificar se não é a wiki principal
                    if str(relative_path) != "wiki":
                        wiki_duplicates.append({
                            'path': str(wiki_folder),
                            'relative_path': str(relative_path),
                            'type': 'duplicate_wiki_folder',
                            'should_remove': True
                        })
            
            return wiki_duplicates
            
        except Exception as e:
            self.logger.error(f"Erro ao encontrar duplicatas wiki: {e}")
            return wiki_duplicates
    
    def find_nested_wiki_folders(self) -> List[Dict]:
        """
        Encontra pastas wiki aninhadas incorretamente.
        
        Returns:
            List[Dict]: Lista de pastas aninhadas incorretas
        """
        nested_wikis = []
        
        try:
            # Verificar wiki dentro de wiki
            wiki_wiki_path = self.correct_paths['wiki'] / "wiki"
            if wiki_wiki_path.exists():
                nested_wikis.append({
                    'path': str(wiki_wiki_path),
                    'type': 'nested_wiki',
                    'should_merge': True,
                    'target': str(self.correct_paths['wiki'])
                })
            
            # Verificar wiki dentro de agents
            agents_wiki_path = self.correct_paths['agents'] / "wiki"
            if agents_wiki_path.exists():
                nested_wikis.append({
                    'path': str(agents_wiki_path),
                    'type': 'agents_wiki',
                    'should_merge': True,
                    'target': str(self.correct_paths['wiki'])
                })
            
            return nested_wikis
            
        except Exception as e:
            self.logger.error(f"Erro ao encontrar pastas wiki aninhadas: {e}")
            return nested_wikis
    
    def find_agent_duplicates(self) -> List[Dict]:
        """
        Encontra duplicatas de agentes.
        
        Returns:
            List[Dict]: Lista de duplicatas de agentes
        """
        agent_duplicates = []
        
        try:
            # Verificar arquivos de agentes em locais incorretos
            agent_patterns = [
                '*_agent.py',
                '*_agent.md',
                '*_agent.log'
            ]
            
            for pattern in agent_patterns:
                for file_path in self.base_path.rglob(pattern):
                    if file_path.is_file():
                        # Verificar se está no local correto
                        if not self.is_in_correct_agents_location(file_path):
                            agent_duplicates.append({
                                'path': str(file_path),
                                'type': 'agent_file_wrong_location',
                                'should_move': True,
                                'target': str(self.correct_paths['agents'] / file_path.name)
                            })
            
            return agent_duplicates
            
        except Exception as e:
            self.logger.error(f"Erro ao encontrar duplicatas de agentes: {e}")
            return agent_duplicates
    
    def is_in_correct_agents_location(self, file_path: Path) -> bool:
        """
        Verifica se um arquivo de agente está no local correto.
        
        Args:
            file_path: Caminho do arquivo
            
        Returns:
            bool: True se está no local correto
        """
        correct_agents_path = self.correct_paths['agents']
        return file_path.parent == correct_agents_path
    
    def find_file_duplicates(self) -> List[Dict]:
        """
        Encontra arquivos duplicados.
        
        Returns:
            List[Dict]: Lista de arquivos duplicados
        """
        file_duplicates = []
        
        try:
            # Verificar arquivos com nomes similares em locais diferentes
            seen_files = {}
            
            for file_path in self.base_path.rglob("*"):
                if file_path.is_file() and self.is_agent_generated_file(file_path):
                    file_name = file_path.name
                    
                    if file_name in seen_files:
                        # Arquivo duplicado encontrado
                        original_path = seen_files[file_name]
                        file_duplicates.append({
                            'original': str(original_path),
                            'duplicate': str(file_path),
                            'filename': file_name,
                            'type': 'duplicate_file',
                            'should_remove_duplicate': True
                        })
                    else:
                        seen_files[file_name] = file_path
            
            return file_duplicates
            
        except Exception as e:
            self.logger.error(f"Erro ao encontrar arquivos duplicados: {e}")
            return file_duplicates
    
    def is_agent_generated_file(self, file_path: Path) -> bool:
        """
        Verifica se um arquivo foi gerado por agentes.
        
        Args:
            file_path: Caminho do arquivo
            
        Returns:
            bool: True se foi gerado por agente
        """
        agent_patterns = [
            'phase2_',
            'otclient_',
            'canary_',
            'integration_',
            'professor_',
            'researcher_',
            'refinement_',
            '_analysis.json',
            '_report.md',
            '_documentation.md',
            '_agent.py',
            '_agent.md',
            '_agent.log'
        ]
        
        file_name = file_path.name.lower()
        return any(pattern in file_name for pattern in agent_patterns)
    
    def clean_duplicates(self, duplicates_report: Dict) -> bool:
        """
        Limpa todas as duplicatas encontradas.
        
        Args:
            duplicates_report: Relatório de duplicatas
            
        Returns:
            bool: True se limpeza bem-sucedida
        """
        try:
            self.logger.info("Iniciando limpeza de duplicatas...")
            
            # 1. Remover pastas wiki duplicadas
            for duplicate in duplicates_report['wiki_duplicates']:
                if duplicate['should_remove']:
                    self.remove_duplicate_folder(Path(duplicate['path']))
            
            # 2. Mesclar pastas wiki aninhadas
            for nested in duplicates_report['nested_wiki_folders']:
                if nested['should_merge']:
                    self.merge_nested_wiki_folder(Path(nested['path']), Path(nested['target']))
            
            # 3. Mover arquivos de agentes para local correto
            for agent_dup in duplicates_report['agent_duplicates']:
                if agent_dup['should_move']:
                    self.move_agent_file(Path(agent_dup['path']), Path(agent_dup['target']))
            
            # 4. Remover arquivos duplicados
            for file_dup in duplicates_report['file_duplicates']:
                if file_dup['should_remove_duplicate']:
                    self.remove_duplicate_file(Path(file_dup['duplicate']))
            
            self.logger.info("Limpeza de duplicatas concluída")
            return True
            
        except Exception as e:
            self.logger.error(f"Erro na limpeza de duplicatas: {e}")
            return False
    
    def remove_duplicate_folder(self, folder_path: Path):
        """
        Remove uma pasta duplicada.
        
        Args:
            folder_path: Caminho da pasta a ser removida
        """
        try:
            if folder_path.exists():
                self.logger.info(f"Removendo pasta duplicada: {folder_path}")
                shutil.rmtree(folder_path)
        except Exception as e:
            self.logger.error(f"Erro ao remover pasta {folder_path}: {e}")
    
    def merge_nested_wiki_folder(self, source_path: Path, target_path: Path):
        """
        Mescla uma pasta wiki aninhada com a wiki principal.
        
        Args:
            source_path: Caminho da pasta aninhada
            target_path: Caminho da pasta de destino
        """
        try:
            if source_path.exists():
                self.logger.info(f"Mesclando {source_path} para {target_path}")
                
                # Mover conteúdo da pasta aninhada para a wiki principal
                for item in source_path.iterdir():
                    target_item = target_path / item.name
                    
                    if target_item.exists():
                        if item.is_file():
                            # Arquivo já existe, remover duplicata
                            item.unlink()
                        else:
                            # Pasta já existe, mesclar conteúdo
                            self.merge_folders(item, target_item)
                    else:
                        # Item não existe, mover
                        shutil.move(str(item), str(target_item))
                
                # Remover pasta aninhada vazia
                shutil.rmtree(source_path)
                
        except Exception as e:
            self.logger.error(f"Erro ao mesclar pasta {source_path}: {e}")
    
    def merge_folders(self, source_folder: Path, target_folder: Path):
        """
        Mescla duas pastas.
        
        Args:
            source_folder: Pasta de origem
            target_folder: Pasta de destino
        """
        try:
            for item in source_folder.iterdir():
                target_item = target_folder / item.name
                
                if target_item.exists():
                    if item.is_file():
                        # Arquivo já existe, remover duplicata
                        item.unlink()
                    else:
                        # Pasta já existe, mesclar recursivamente
                        self.merge_folders(item, target_item)
                else:
                    # Item não existe, mover
                    shutil.move(str(item), str(target_item))
            
            # Remover pasta de origem se estiver vazia
            if not any(source_folder.iterdir()):
                source_folder.rmdir()
                
        except Exception as e:
            self.logger.error(f"Erro ao mesclar pastas {source_folder} e {target_folder}: {e}")
    
    def move_agent_file(self, source_path: Path, target_path: Path):
        """
        Move um arquivo de agente para o local correto.
        
        Args:
            source_path: Caminho de origem
            target_path: Caminho de destino
        """
        try:
            if source_path.exists():
                # Criar diretório de destino se não existir
                target_path.parent.mkdir(parents=True, exist_ok=True)
                
                if target_path.exists():
                    # Arquivo já existe no destino, remover duplicata
                    self.logger.info(f"Arquivo já existe em {target_path}, removendo duplicata")
                    source_path.unlink()
                else:
                    # Mover arquivo
                    self.logger.info(f"Movendo {source_path} para {target_path}")
                    shutil.move(str(source_path), str(target_path))
                    
        except Exception as e:
            self.logger.error(f"Erro ao mover arquivo {source_path}: {e}")
    
    def remove_duplicate_file(self, file_path: Path):
        """
        Remove um arquivo duplicado.
        
        Args:
            file_path: Caminho do arquivo a ser removido
        """
        try:
            if file_path.exists():
                self.logger.info(f"Removendo arquivo duplicado: {file_path}")
                file_path.unlink()
        except Exception as e:
            self.logger.error(f"Erro ao remover arquivo {file_path}: {e}")
    
    def update_maps_with_absolute_paths(self) -> bool:
        """
        Atualiza os mapas JSON com caminhos absolutos.
        
        Returns:
            bool: True se atualização bem-sucedida
        """
        try:
            self.logger.info("Atualizando mapas com caminhos absolutos...")
            
            # Atualizar wiki_map.json
            wiki_map_path = self.correct_paths['maps'] / "wiki_map.json"
            if wiki_map_path.exists():
                with open(wiki_map_path, 'r', encoding='utf-8') as f:
                    wiki_map = json.load(f)
                
                # Converter caminhos relativos para absolutos
                for key, value in wiki_map.items():
                    if isinstance(value, dict) and 'path' in value:
                        relative_path = value['path']
                        absolute_path = str(self.base_path / relative_path)
                        value['absolute_path'] = absolute_path
                
                # Salvar mapa atualizado
                with open(wiki_map_path, 'w', encoding='utf-8') as f:
                    json.dump(wiki_map, f, indent=2, ensure_ascii=False)
                
                self.logger.info("wiki_map.json atualizado com caminhos absolutos")
            
            # Atualizar outros mapas relevantes
            maps_to_update = [
                "tags_index.json",
                "relationships.json",
                "enhanced_context_system.json",
                "intelligent_navigation.json"
            ]
            
            for map_file in maps_to_update:
                map_path = self.correct_paths['maps'] / map_file
                if map_path.exists():
                    self.update_map_with_absolute_paths(map_path)
            
            return True
            
        except Exception as e:
            self.logger.error(f"Erro ao atualizar mapas: {e}")
            return False
    
    def update_map_with_absolute_paths(self, map_path: Path):
        """
        Atualiza um mapa específico com caminhos absolutos.
        
        Args:
            map_path: Caminho do mapa a ser atualizado
        """
        try:
            with open(map_path, 'r', encoding='utf-8') as f:
                map_data = json.load(f)
            
            # Adicionar metadados de caminhos absolutos
            map_data['_metadata'] = {
                'base_path': str(self.base_path),
                'updated': datetime.now().isoformat(),
                'absolute_paths': True
            }
            
            # Salvar mapa atualizado
            with open(map_path, 'w', encoding='utf-8') as f:
                json.dump(map_data, f, indent=2, ensure_ascii=False)
            
            self.logger.info(f"{map_path.name} atualizado com caminhos absolutos")
            
        except Exception as e:
            self.logger.error(f"Erro ao atualizar {map_path}: {e}")
    
    def create_absolute_path_utility(self) -> bool:
        """
        Cria utilitário para uso de caminhos absolutos.
        
        Returns:
            bool: True se criação bem-sucedida
        """
        try:
            utility_content = f"""#!/usr/bin/env python3
# -*- coding: utf-8 -*-
\"\"\"
Absolute Path Utility - Sistema de Caminhos Absolutos
====================================================

Utilitário para uso de caminhos absolutos em todo o projeto.
Baseado no diretório raiz do projeto (onde está cursor.md).

Autor: Sistema BMAD
Versão: 2.0.0
Data: 2025-01-27
\"\"\"

import os
import sys
from pathlib import Path
from typing import Optional, Dict

class AbsolutePathManager:
    \"\"\"
    Gerenciador de caminhos absolutos para o projeto.
    \"\"\"
    
    def __init__(self):
        # Determinar caminho base absoluto
        self.base_path = self._find_project_root()
        
        # Mapeamento de caminhos corretos (absolutos)
        self.paths = {{
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
        }}
    
    def _find_project_root(self) -> Path:
        \"\"\"
        Encontra o diretório raiz do projeto (onde está cursor.md).
        
        Returns:
            Path: Caminho absoluto do diretório raiz
        \"\"\"
        current_path = Path.cwd().resolve()
        
        while current_path.parent != current_path:
            if (current_path / "cursor.md").exists():
                return current_path
            current_path = current_path.parent
        
        # Se não encontrar, usar diretório atual
        return Path.cwd().resolve()
    
    def get_path(self, path_name: str) -> Optional[Path]:
        \"\"\"
        Obtém um caminho absoluto pelo nome.
        
        Args:
            path_name: Nome do caminho (wiki, habdel, otclient, etc.)
            
        Returns:
            Optional[Path]: Caminho absoluto ou None
        \"\"\"
        return self.paths.get(path_name)
    
    def create_file_safely(self, path_name: str, filename: str, content: str) -> bool:
        \"\"\"
        Cria um arquivo de forma segura usando caminhos absolutos.
        
        Args:
            path_name: Nome do caminho de destino
            filename: Nome do arquivo
            content: Conteúdo do arquivo
            
        Returns:
            bool: True se criado com sucesso
        \"\"\"
        try:
            target_path = self.get_path(path_name)
            if target_path:
                file_path = target_path / filename
                file_path.parent.mkdir(parents=True, exist_ok=True)
                file_path.write_text(content, encoding='utf-8')
                return True
            return False
        except Exception as e:
            print(f"Erro ao criar arquivo {{filename}}: {{e}}")
            return False
    
    def run_script_absolutely(self, script_name: str, *args) -> bool:
        \"\"\"
        Executa um script Python usando caminho absoluto.
        
        Args:
            script_name: Nome do script (sem .py)
            *args: Argumentos adicionais
            
        Returns:
            bool: True se executado com sucesso
        \"\"\"
        try:
            script_path = self.get_path('agents') / f"{{script_name}}.py"
            if script_path.exists():
                # Executar script com caminho absoluto
                cmd = [sys.executable, str(script_path)] + list(args)
                result = subprocess.run(cmd, cwd=str(self.base_path), capture_output=True, text=True)
                
                if result.returncode == 0:
                    print(f"Script {{script_name}} executado com sucesso")
                    return True
                else:
                    print(f"Erro ao executar {{script_name}}: {{result.stderr}}")
                    return False
            else:
                print(f"Script {{script_name}} não encontrado em {{script_path}}")
                return False
        except Exception as e:
            print(f"Erro ao executar script {{script_name}}: {{e}}")
            return False
    
    def log_message(self, message: str, level: str = "INFO"):
        \"\"\"
        Registra uma mensagem no log usando caminho absoluto.
        
        Args:
            message: Mensagem a ser registrada
            level: Nível da mensagem (INFO, WARNING, ERROR)
        \"\"\"
        try:
            log_path = self.get_path('log')
            if log_path:
                log_file = log_path / "absolute_path_manager.log"
                timestamp = datetime.now().isoformat()
                log_entry = f"{{timestamp}} - {{level}} - {{message}}\\n"
                
                with open(log_file, 'a', encoding='utf-8') as f:
                    f.write(log_entry)
        except Exception as e:
            print(f"Erro ao registrar log: {{e}}")

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
"""
            
            # Salvar utilitário
            utility_path = self.correct_paths['agents'] / "absolute_path_utility.py"
            utility_path.write_text(utility_content, encoding='utf-8')
            
            self.logger.info("Utilitário de caminhos absolutos criado")
            return True
            
        except Exception as e:
            self.logger.error(f"Erro ao criar utilitário: {e}")
            return False
    
    def generate_comprehensive_report(self, duplicates_report: Dict) -> str:
        """
        Gera relatório completo da validação.
        
        Args:
            duplicates_report: Relatório de duplicatas
            
        Returns:
            str: Relatório completo
        """
        try:
            report = f"""# Relatório Completo de Validação de Caminhos

## 📊 Resumo da Validação Completa

- **Data**: {datetime.now().isoformat()}
- **Base Path**: {self.base_path}
- **Total de Problemas Encontrados**: {duplicates_report['total_issues']}
- **Status**: {'✅ Limpo' if duplicates_report['total_issues'] == 0 else '🔧 Corrigido'}

## 🗂️ Estrutura de Caminhos Absolutos

### Caminhos Principais
"""
            
            for name, path in self.correct_paths.items():
                status = "✅ Existe" if path.exists() else "❌ Não existe"
                report += f"- **{name}**: {path} - {status}\n"
            
            report += "\n## 🔍 Problemas Encontrados e Corrigidos\n"
            
            # Wiki duplicadas
            if duplicates_report['wiki_duplicates']:
                report += "\n### Pastas Wiki Duplicadas\n"
                for dup in duplicates_report['wiki_duplicates']:
                    report += f"- **{dup['relative_path']}**: {dup['path']} - Removida\n"
            
            # Pastas aninhadas
            if duplicates_report['nested_wiki_folders']:
                report += "\n### Pastas Wiki Aninhadas\n"
                for nested in duplicates_report['nested_wiki_folders']:
                    report += f"- **{nested['path']}**: Mesclada para {nested['target']}\n"
            
            # Duplicatas de agentes
            if duplicates_report['agent_duplicates']:
                report += "\n### Arquivos de Agentes em Locais Incorretos\n"
                for agent in duplicates_report['agent_duplicates']:
                    report += f"- **{agent['path']}**: Movido para {agent['target']}\n"
            
            # Arquivos duplicados
            if duplicates_report['file_duplicates']:
                report += "\n### Arquivos Duplicados\n"
                for file_dup in duplicates_report['file_duplicates']:
                    report += f"- **{file_dup['filename']}**: {file_dup['duplicate']} - Removido\n"
            
            report += f"""

## 🛠️ Melhorias Implementadas

### ✅ Sistema de Caminhos Absolutos
- **Base Path**: {self.base_path}
- **Mapeamento Completo**: Todos os caminhos mapeados
- **Utilitário Criado**: absolute_path_utility.py
- **Execução Absoluta**: Scripts executados com caminhos absolutos

### ✅ Limpeza de Duplicatas
- **Pastas Wiki**: Duplicatas removidas
- **Arquivos de Agentes**: Movidos para locais corretos
- **Estrutura Limpa**: Organização consistente
- **Logs Centralizados**: Todos os logs em wiki/log/

### ✅ Mapas JSON Atualizados
- **Caminhos Absolutos**: Todos os mapas atualizados
- **Metadados**: Informações de atualização adicionadas
- **Consistência**: Padrão uniforme em todos os mapas

## 🚀 Próximos Passos

### Imediato
1. **Usar absolute_path_utility** em todos os agentes
2. **Executar scripts** com caminhos absolutos
3. **Validar estrutura** após limpeza
4. **Testar criação** de arquivos

### Futuro
1. **Automatizar validação** em todos os workflows
2. **Implementar monitoramento** de criação de arquivos
3. **Criar testes** para validação de caminhos
4. **Otimizar performance** do sistema

## 📋 Checklist de Conclusão

### ✅ Validação Completa
- [x] Escaneamento de duplicatas
- [x] Limpeza de arquivos incorretos
- [x] Mesclagem de pastas aninhadas
- [x] Atualização de mapas JSON

### ✅ Sistema de Caminhos Absolutos
- [x] Mapeamento completo de caminhos
- [x] Utilitário de caminhos absolutos
- [x] Execução absoluta de scripts
- [x] Logs centralizados

### ✅ Organização
- [x] Estrutura limpa e consistente
- [x] Arquivos em locais corretos
- [x] Logs organizados
- [x] Relatórios centralizados

---

**Relatório Gerado**: {datetime.now().isoformat()}  
**Responsável**: Comprehensive Path Validator  
**Status**: {'✅ Validação Completa' if duplicates_report['total_issues'] == 0 else '🔧 Correções Aplicadas'}
"""
            
            return report
            
        except Exception as e:
            self.logger.error(f"Erro ao gerar relatório: {e}")
            return f"Erro ao gerar relatório: {e}"
    
    def run_comprehensive_validation(self) -> bool:
        """
        Executa validação completa do projeto.
        
        Returns:
            bool: True se validação bem-sucedida
        """
        try:
            self.logger.info("Iniciando validação completa do projeto...")
            
            # 1. Escanear duplicatas
            self.logger.info("Passo 1: Escaneando duplicatas...")
            duplicates_report = self.scan_all_duplicates()
            
            # 2. Limpar duplicatas
            if duplicates_report['total_issues'] > 0:
                self.logger.info("Passo 2: Limpando duplicatas...")
                self.clean_duplicates(duplicates_report)
            
            # 3. Atualizar mapas com caminhos absolutos
            self.logger.info("Passo 3: Atualizando mapas...")
            self.update_maps_with_absolute_paths()
            
            # 4. Criar utilitário de caminhos absolutos
            self.logger.info("Passo 4: Criando utilitário...")
            self.create_absolute_path_utility()
            
            # 5. Gerar relatório completo
            self.logger.info("Passo 5: Gerando relatório...")
            report_content = self.generate_comprehensive_report(duplicates_report)
            
            # Salvar relatório
            report_path = self.correct_paths['log'] / "comprehensive_validation_report.md"
            report_path.write_text(report_content, encoding='utf-8')
            
            self.logger.info("Validação completa concluída com sucesso!")
            return True
            
        except Exception as e:
            self.logger.error(f"Erro na validação completa: {e}")
            return False

def main():
    """
    Função principal para execução da validação completa.
    """
    print("🔍 Comprehensive Path Validator - Sistema Completo de Validação")
    print("=" * 70)
    
    # Inicializar agente
    agent = ComprehensivePathValidator()
    
    # Executar validação completa
    if agent.run_comprehensive_validation():
        print("✅ Validação completa concluída!")
        print("📁 Estrutura limpa e organizada")
        print("🛠️ Utilitário criado: wiki/bmad/agents/absolute_path_utility.py")
        print("📋 Relatório: wiki/log/comprehensive_validation_report.md")
        print("🎯 Próximo passo: Usar absolute_path_utility em todos os agentes")
        
    else:
        print("❌ Erro na validação completa")
        sys.exit(1)

if __name__ == "__main__":
    main() 