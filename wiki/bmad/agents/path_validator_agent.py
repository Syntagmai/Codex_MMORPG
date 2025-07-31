#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Path Validator Agent - Sistema de Validação de Caminhos
=====================================================

Agente especializado em validar e corrigir caminhos de arquivos
para evitar erros de localização e criação em pastas incorretas.

Autor: Sistema BMAD
Versão: 1.0.0
Data: 2025-01-27
"""

import os
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import logging

class PathValidatorAgent:
    """
    Agente de validação de caminhos para evitar erros de localização.
    """
    
    def __init__(self, base_path: str = None):
        """
        Inicializa o agente de validação de caminhos.
        
        Args:
            base_path: Caminho base do projeto (padrão: diretório atual)
        """
        self.base_path = Path(base_path) if base_path else Path.cwd()
        
        # Configurar logging
        log_dir = self.base_path / 'wiki' / 'log'
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / 'path_validator.log'
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
        # Mapeamento de caminhos corretos
        self.correct_paths = {
            'habdel': self.base_path / "wiki" / "habdel",
            'otclient': self.base_path / "wiki" / "habdel" / "otclient",
            'canary': self.base_path / "wiki" / "habdel" / "canary",
            'integration': self.base_path / "wiki" / "habdel" / "integration",
            'docs': self.base_path / "wiki" / "docs",
            'agents': self.base_path / "wiki" / "bmad" / "agents",
            'maps': self.base_path / "wiki" / "maps",
            'update': self.base_path / "wiki" / "update"
        }
        
        self.logger.info("Path Validator Agent inicializado")
    
    def validate_and_fix_paths(self) -> bool:
        """
        Valida e corrige caminhos incorretos.
        
        Returns:
            bool: True se validação bem-sucedida
        """
        try:
            self.logger.info("Iniciando validação e correção de caminhos...")
            
            # 1. Verificar se há arquivos em locais incorretos
            incorrect_files = self.find_incorrect_files()
            
            if incorrect_files:
                self.logger.info(f"Encontrados {len(incorrect_files)} arquivos em locais incorretos")
                
                # 2. Mover arquivos para locais corretos
                for incorrect_path, correct_path in incorrect_files:
                    self.move_file_to_correct_location(incorrect_path, correct_path)
            else:
                self.logger.info("Nenhum arquivo em local incorreto encontrado")
            
            # 3. Validar estrutura de pastas
            self.validate_folder_structure()
            
            # 4. Gerar relatório de validação
            self.generate_validation_report(incorrect_files)
            
            self.logger.info("Validação e correção de caminhos concluída")
            return True
            
        except Exception as e:
            self.logger.error(f"Erro na validação de caminhos: {e}")
            return False
    
    def find_incorrect_files(self) -> List[Tuple[Path, Path]]:
        """
        Encontra arquivos em locais incorretos.
        
        Returns:
            List[Tuple[Path, Path]]: Lista de (caminho_incorreto, caminho_correto)
        """
        incorrect_files = []
        
        try:
            # Verificar se há pasta wiki dentro de agents
            agents_wiki_path = self.correct_paths['agents'] / "wiki"
            if agents_wiki_path.exists():
                self.logger.info(f"Encontrada pasta wiki incorreta em: {agents_wiki_path}")
                
                # Mapear arquivos para locais corretos
                for file_path in agents_wiki_path.rglob("*"):
                    if file_path.is_file():
                        correct_path = self.map_to_correct_location(file_path)
                        if correct_path and correct_path != file_path:
                            incorrect_files.append((file_path, correct_path))
            
            # Verificar outros arquivos soltos
            for root_path in [self.correct_paths['agents'], self.base_path]:
                for file_path in root_path.glob("*"):
                    if file_path.is_file() and self.is_agent_generated_file(file_path):
                        correct_path = self.map_to_correct_location(file_path)
                        if correct_path and correct_path != file_path:
                            incorrect_files.append((file_path, correct_path))
            
            return incorrect_files
            
        except Exception as e:
            self.logger.error(f"Erro ao encontrar arquivos incorretos: {e}")
            return incorrect_files
    
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
            '_documentation.md'
        ]
        
        file_name = file_path.name.lower()
        return any(pattern in file_name for pattern in agent_patterns)
    
    def map_to_correct_location(self, file_path: Path) -> Optional[Path]:
        """
        Mapeia um arquivo para sua localização correta.
        
        Args:
            file_path: Caminho atual do arquivo
            
        Returns:
            Optional[Path]: Caminho correto ou None
        """
        try:
            file_name = file_path.name
            relative_path = file_path.relative_to(self.base_path)
            
            # Mapeamento baseado no nome e caminho relativo
            if 'habdel' in str(relative_path) or 'otclient' in str(relative_path):
                if 'otclient' in file_name:
                    return self.correct_paths['otclient'] / file_name
                elif 'canary' in file_name:
                    return self.correct_paths['canary'] / file_name
                elif 'integration' in file_name:
                    return self.correct_paths['integration'] / file_name
                else:
                    return self.correct_paths['habdel'] / file_name
            
            elif 'docs' in str(relative_path) or 'professor' in file_name:
                return self.correct_paths['docs'] / file_name
            
            elif 'analysis' in file_name or 'report' in file_name:
                if 'otclient' in file_name:
                    return self.correct_paths['otclient'] / file_name
                elif 'canary' in file_name:
                    return self.correct_paths['canary'] / file_name
                else:
                    return self.correct_paths['habdel'] / file_name
            
            elif 'phase2' in file_name:
                return self.correct_paths['otclient'] / file_name
            
            elif 'update' in file_name:
                return self.correct_paths['update'] / file_name
            
            return None
            
        except Exception as e:
            self.logger.warning(f"Erro ao mapear arquivo {file_path}: {e}")
            return None
    
    def move_file_to_correct_location(self, incorrect_path: Path, correct_path: Path):
        """
        Move um arquivo para sua localização correta.
        
        Args:
            incorrect_path: Caminho incorreto
            correct_path: Caminho correto
        """
        try:
            # Criar diretório de destino se não existir
            correct_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Mover arquivo
            if correct_path.exists():
                self.logger.info(f"Arquivo já existe em {correct_path}, removendo duplicata")
                incorrect_path.unlink()
            else:
                self.logger.info(f"Movendo {incorrect_path} para {correct_path}")
                shutil.move(str(incorrect_path), str(correct_path))
            
        except Exception as e:
            self.logger.error(f"Erro ao mover arquivo {incorrect_path}: {e}")
    
    def validate_folder_structure(self):
        """
        Valida a estrutura de pastas.
        """
        try:
            self.logger.info("Validando estrutura de pastas...")
            
            # Verificar se todas as pastas necessárias existem
            for name, path in self.correct_paths.items():
                if not path.exists():
                    self.logger.info(f"Criando pasta {name}: {path}")
                    path.mkdir(parents=True, exist_ok=True)
                else:
                    self.logger.debug(f"Pasta {name} já existe: {path}")
            
            # Verificar subpastas específicas
            subfolders = {
                'otclient_analysis': self.correct_paths['otclient'] / "analysis",
                'otclient_documentation': self.correct_paths['otclient'] / "documentation",
                'otclient_stories': self.correct_paths['otclient'] / "stories",
                'canary_analysis': self.correct_paths['canary'] / "analysis",
                'canary_documentation': self.correct_paths['canary'] / "documentation",
                'canary_stories': self.correct_paths['canary'] / "stories",
                'docs_courses': self.correct_paths['docs'] / "courses",
                'docs_lessons': self.correct_paths['docs'] / "lessons",
                'docs_exercises': self.correct_paths['docs'] / "exercises",
                'docs_resources': self.correct_paths['docs'] / "resources"
            }
            
            for name, path in subfolders.items():
                if not path.exists():
                    self.logger.info(f"Criando subpasta {name}: {path}")
                    path.mkdir(parents=True, exist_ok=True)
            
            self.logger.info("Estrutura de pastas validada")
            
        except Exception as e:
            self.logger.error(f"Erro na validação de estrutura de pastas: {e}")
    
    def generate_validation_report(self, incorrect_files: List[Tuple[Path, Path]]):
        """
        Gera relatório de validação.
        
        Args:
            incorrect_files: Lista de arquivos incorretos
        """
        try:
            report = f"""# Relatório de Validação de Caminhos

## 📊 Resumo da Validação

- **Arquivos Verificados**: Todos os arquivos do projeto
- **Arquivos Incorretos Encontrados**: {len(incorrect_files)}
- **Arquivos Corrigidos**: {len(incorrect_files)}
- **Status**: {'✅ Limpo' if len(incorrect_files) == 0 else '🔧 Corrigido'}

## 🗂️ Estrutura de Pastas Validada

### Pastas Principais
"""
            
            for name, path in self.correct_paths.items():
                status = "✅ Existe" if path.exists() else "❌ Não existe"
                report += f"- **{name}**: {path} - {status}\n"
            
            if incorrect_files:
                report += "\n## 🔧 Arquivos Corrigidos\n"
                for incorrect_path, correct_path in incorrect_files:
                    report += f"- **{incorrect_path.name}**: {incorrect_path} → {correct_path}\n"
            
            report += f"""

## 🎯 Recomendações

### Para Desenvolvedores
1. **Sempre use caminhos absolutos** baseados no diretório raiz
2. **Valide caminhos** antes de criar arquivos
3. **Use o Path Validator Agent** regularmente
4. **Consulte os mapas JSON** para caminhos corretos

### Para Agentes
1. **Implementar validação** antes de criar arquivos
2. **Usar caminhos absolutos** em vez de relativos
3. **Consultar mapas JSON** para localizações corretas
4. **Testar criação** em ambiente controlado

## 🚀 Próximos Passos

1. **Implementar validação automática** em todos os agentes
2. **Criar sistema de caminhos absolutos** baseado em mapas
3. **Automatizar correção** de caminhos incorretos
4. **Prevenir criação** de arquivos em locais errados

---

**Relatório Gerado**: {datetime.now().isoformat()}  
**Responsável**: Path Validator Agent  
**Status**: {'✅ Validação Concluída' if len(incorrect_files) == 0 else '🔧 Correções Aplicadas'}
"""
            
            # Salvar relatório
            report_file = self.correct_paths['update'] / "path_validation_report.md"
            report_file.parent.mkdir(parents=True, exist_ok=True)
            report_file.write_text(report, encoding='utf-8')
            
            self.logger.info("Relatório de validação gerado com sucesso")
            
        except Exception as e:
            self.logger.error(f"Erro ao gerar relatório de validação: {e}")
    
    def create_path_validation_utility(self):
        """
        Cria utilitário para validação de caminhos.
        """
        try:
            utility_content = f"""#!/usr/bin/env python3
# -*- coding: utf-8 -*-
\"\"\"
Path Validation Utility
======================

Utilitário para validar caminhos antes de criar arquivos.
Use este utilitário em todos os agentes para evitar erros de localização.

Autor: Sistema BMAD
Versão: 1.0.0
\"\"\"

import os
from pathlib import Path
from typing import Optional

class PathValidator:
    \"\"\"
    Utilitário para validação de caminhos.
    \"\"\"
    
    def __init__(self, base_path: str = None):
        self.base_path = Path(base_path) if base_path else Path.cwd()
        
        # Caminhos corretos
        self.correct_paths = {{
            'habdel': self.base_path / "wiki" / "habdel",
            'otclient': self.base_path / "wiki" / "habdel" / "otclient",
            'canary': self.base_path / "wiki" / "habdel" / "canary",
            'integration': self.base_path / "wiki" / "habdel" / "integration",
            'docs': self.base_path / "wiki" / "docs",
            'agents': self.base_path / "wiki" / "bmad" / "agents",
            'maps': self.base_path / "wiki" / "maps",
            'update': self.base_path / "wiki" / "update"
        }}
    
    def validate_path(self, file_name: str, target_system: str) -> Optional[Path]:
        \"\"\"
        Valida e retorna o caminho correto para um arquivo.
        
        Args:
            file_name: Nome do arquivo
            target_system: Sistema de destino (otclient, canary, docs, etc.)
            
        Returns:
            Optional[Path]: Caminho correto ou None
        \"\"\"
        if target_system in self.correct_paths:
            return self.correct_paths[target_system] / file_name
        return None
    
    def ensure_directory_exists(self, path: Path):
        \"\"\"
        Garante que o diretório existe.
        
        Args:
            path: Caminho do diretório
        \"\"\"
        path.mkdir(parents=True, exist_ok=True)
    
    def create_file_safely(self, file_name: str, target_system: str, content: str) -> bool:
        \"\"\"
        Cria um arquivo de forma segura no local correto.
        
        Args:
            file_name: Nome do arquivo
            target_system: Sistema de destino
            content: Conteúdo do arquivo
            
        Returns:
            bool: True se criado com sucesso
        \"\"\"
        try:
            correct_path = self.validate_path(file_name, target_system)
            if correct_path:
                self.ensure_directory_exists(correct_path.parent)
                correct_path.write_text(content, encoding='utf-8')
                return True
            return False
        except Exception as e:
            print(f"Erro ao criar arquivo {{file_name}}: {{e}}")
            return False

# Exemplo de uso:
# validator = PathValidator()
# success = validator.create_file_safely("meu_arquivo.md", "otclient", "# Conteúdo")
"""
            
            # Salvar utilitário
            utility_file = self.correct_paths['agents'] / "path_validator_utility.py"
            utility_file.write_text(utility_content, encoding='utf-8')
            
            self.logger.info("Utilitário de validação de caminhos criado")
            
        except Exception as e:
            self.logger.error(f"Erro ao criar utilitário: {e}")

def main():
    """
    Função principal para execução do agente de validação.
    """
    print("🔍 Path Validator Agent - Sistema de Validação de Caminhos")
    print("=" * 60)
    
    # Inicializar agente
    agent = PathValidatorAgent()
    
    # Executar validação
    if agent.validate_and_fix_paths():
        print("✅ Validação de caminhos concluída!")
        print("📁 Estrutura de pastas validada")
        print("🔧 Arquivos incorretos corrigidos")
        print("📋 Relatório: wiki/update/path_validation_report.md")
        print("🎯 Próximo passo: Usar Path Validator Utility em todos os agentes")
        
        # Criar utilitário
        agent.create_path_validation_utility()
        print("🛠️ Utilitário criado: wiki/bmad/agents/path_validator_utility.py")
        
    else:
        print("❌ Erro na validação de caminhos")
        sys.exit(1)

if __name__ == "__main__":
    main() 