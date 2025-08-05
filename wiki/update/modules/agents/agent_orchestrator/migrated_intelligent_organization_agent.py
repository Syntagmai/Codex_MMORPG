from unicode_aliases import *
# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
MAX_ITEMS = 100

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: intelligent_organization_agent.py
Módulo de Destino: agents.agent_orchestrator
Data de Migração: 2025-08-01 12:21:43

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import AgentorchestratorModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agente de Organização Inteligente - Sistema de Code Cleanup e Integração Canary
===============================================================================

Agente especializado em organização automática de arquivos, pastas e relatórios
baseado nas regras de code cleanup. Mantém o sistema sempre limpo e organizado.
Inclui suporte para integração total com Canary.

Autor: Sistema BMAD - OTClient Documentation
Data: 2025-01-27
Versão: 1.1 - Suporte Canary
"""

import shutil
import re
from datetime import datetime, timedelta
import logging

# Configuração de logging
log_dir = Path.cwd() / 'wiki' / 'log'
log_dir.mkdir(parents=True, exist_ok=True)
log_file = log_dir / 'intelligent_organization.log'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler()
    ]
)

class IntelligentOrganizationAgent:
    """Agente de organização inteligente para code cleanup e integração Canary"""
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.logger = logging.getLogger(__name__)
        
        # Estrutura de pastas
        self.wiki_path = self.base_path / "wiki"
        self.log_path = self.wiki_path / "log"
        self.update_path = self.wiki_path / "update"
        self.canary_path = self.wiki_path / "canary"
        self.maps_path = self.wiki_path / "maps"
        
        # Padrões de detecção (incluindo Canary)
        self.patterns = {
            "report": ["*_REPORT.md", "*_report.md", "Relatório_*.md", "RELATORIO_*.md"],
            "task": ["TASK_*.md", "*_task.md", "*_TASK.md"],
            "recipe": ["*_RECIPE.md", "*_recipe.md"],
            "log": ["*.log", "*_log.md", "*_LOG.md"],
            "config": ["*.json", "*.yaml", "*.yml"],
            "script": ["*.py", "*.sh", "*.bat"],
            "temp": ["*_temp.md", "*_tmp.md", "temp_*", "tmp_*", "*_backup.md", "*_old.md"],
            "obsolete": ["*_obsolete.md", "*_archive.md", "*_deprecated.md"],
            "canary": ["*_canary.md", "*_CANARY.md", "canary_*", "CANARY_*"],
            "integration": ["*_integration.md", "*_INTEGRATION.md", "integration_*", "INTEGRATION_*"],
            "template": ["*_template.md", "*_TEMPLATE.md", "template_*", "TEMPLATE_*"]
        }
        
        # Categorias de organização (incluindo Canary)
        self.categories = {
            "reports": {
                "patterns": self.patterns["report"],
                "destination": self.log_path / "reports" / "current",
                "archive_destination": self.log_path / "reports"
            },
            "completed_tasks": {
                "patterns": self.patterns["task"],
                "destination": self.log_path / "completed_tasks",
                "archive_destination": self.log_path / "archives" / "completed_tasks"
            },
            "recipes": {
                "patterns": self.patterns["recipe"],
                "destination": self.log_path / "recipes",
                "archive_destination": self.log_path / "archives" / "recipes"
            },
            "archives": {
                "patterns": self.patterns["obsolete"],
                "destination": self.log_path / "archives" / "obsolete_files",
                "archive_destination": self.log_path / "archives" / "obsolete_files"
            },
            "canary_integration": {
                "patterns": self.patterns["canary"] + self.patterns["integration"],
                "destination": self.canary_path / "integration",
                "archive_destination": self.canary_path / "archives"
            },
            "canary_templates": {
                "patterns": self.patterns["template"],
                "destination": self.canary_path / "templates",
                "archive_destination": self.canary_path / "archives" / "templates"
            },
            "integration_maps": {
                "patterns": ["*_integration_map.json", "*_canary_map.json"],
                "destination": self.maps_path / "integration",
                "archive_destination": self.maps_path / "archives"
            }
        }
        
        # Configurações de integração Canary
        self.canary_config = {
            "integration_phases": [
                "preparation",
                "structure_validation", 
                "template_creation",
                "workflow_setup",
                "testing",
                "final_integration"
            ],
            "compatibility_checks": [
                "file_structure",
                "api_interfaces",
                "documentation_format",
                "code_standards",
                "dependencies"
            ],
            "integration_points": [
                "src/",
                "modules/",
                "data/",
                "wiki/",
                "docs/"
            ]
        }
        
        self.logger.info("🤖 Agente de Organização Inteligente com suporte Canary inicializado")
    
    def detect_organization_issues(self) -> Dict[str, List[Path]]:
        """
        Detecta problemas de organização automaticamente.
        Inclui detecção específica para arquivos de integração Canary.
        
        Returns:
            Dicionário com problemas encontrados
        """
        self.logger.info("🔍 Detectando problemas de organização...")
        
        issues = {
            "files_in_wrong_location": [],
            "duplicate_files": [],
            "temp_files": [],
            "obsolete_files": [],
            "canary_integration_issues": [],
            "missing_integration_structure": []
        }
        
        # Detectar problemas gerais
        for file_path in self.base_path.rglob("*"):
            if file_path.is_file() and not self._is_ignored(file_path):
                if self.is_in_wrong_location(file_path):
                    issues["files_in_wrong_location"].append(file_path)
                elif self.is_temp_file(file_path):
                    issues["temp_files"].append(file_path)
                elif self.is_obsolete(file_path):
                    issues["obsolete_files"].append(file_path)
        
        # Detectar problemas específicos de integração Canary
        issues["canary_integration_issues"] = self._detect_canary_integration_issues()
        issues["missing_integration_structure"] = self._detect_missing_integration_structure()
        
        # Detectar duplicatas
        all_files = [f for f in self.base_path.rglob("*") if f.is_file() and not self._is_ignored(f)]
        duplicates = self.find_duplicates(all_files)
        issues["duplicate_files"] = [dup[0] for dup in duplicates]
        
        self.logger.info(f"🔍 Problemas detectados: {sum(len(v) for v in issues.values())} total")
        return issues
    
    def _detect_canary_integration_issues(self) -> List[Path]:
        """
        Detecta problemas específicos relacionados à integração Canary.
        
        Returns:
            Lista de arquivos com problemas de integração
        """
        issues = []
        
        # Verificar arquivos de integração fora da estrutura correta
        for file_path in self.base_path.rglob("*"):
            if file_path.is_file() and not self._is_ignored(file_path):
                if self._is_canary_integration_file(file_path):
                    if not self._is_in_correct_canary_location(file_path):
                        issues.append(file_path)
        
        return issues
    
    def _detect_missing_integration_structure(self) -> List[Path]:
        """
        Detecta estrutura de integração faltante.
        
        Returns:
            Lista de diretórios/arquivos faltantes
        """
        missing = []
        
        # Verificar estrutura de integração Canary
        required_structure = [
            self.canary_path,
            self.canary_path / "templates",
            self.canary_path / "workflows", 
            self.canary_path / "validation",
            self.canary_path / "integration",
            self.maps_path / "integration"
        ]
        
        for path in required_structure:
            if not path.exists():
                missing.append(path)
        
        return missing
    
    def _is_canary_integration_file(self, file_path: Path) -> bool:
        """
        Verifica se um arquivo é relacionado à integração Canary.
        
        Args:
            file_path: Caminho do arquivo
            
        Returns:
            True se for arquivo de integração Canary
        """
        filename = file_path.name.lower()
        return any(pattern in filename for pattern in ['canary', 'integration', 'template'])
    
    def _is_in_correct_canary_location(self, file_path: Path) -> bool:
        """
        Verifica se um arquivo de integração Canary está no local correto.
        
        Args:
            file_path: Caminho do arquivo
            
        Returns:
            True se estiver no local correto
        """
        # Verificar se está em uma das pastas de integração Canary
        canary_locations = [
            self.canary_path,
            self.maps_path / "integration"
        ]
        
        return any(str(file_path).startswith(str(loc)) for loc in canary_locations)
    
    def organize_canary_integration_files(self) -> Dict[str, int]:
        """
        Organiza arquivos relacionados à integração Canary.
        
        Returns:
            Dicionário com estatísticas de organização
        """
        self.logger.info("🔄 Organizando arquivos de integração Canary...")
        
        stats = {
            "canary_integration_moved": 0,
            "canary_templates_moved": 0,
            "integration_maps_moved": 0,
            "integration_structure_created": 0
        }
        
        try:
            # Criar estrutura de integração se não existir
            if self._create_canary_integration_structure():
                stats["integration_structure_created"] = 1
            
            # Organizar arquivos de integração Canary
            for file_path in self.base_path.rglob("*"):
                if file_path.is_file() and not self._is_ignored(file_path):
                    if self._is_canary_integration_file(file_path):
                        if self._organize_canary_file(file_path):
                            if "template" in file_path.name.lower():
                                stats["canary_templates_moved"] += 1
                            elif "map" in file_path.name.lower():
                                stats["integration_maps_moved"] += 1
                            else:
                                stats["canary_integration_moved"] += 1
            
            self.logger.info(f"✅ Organização Canary concluída: {sum(stats.values())} arquivos processados")
            return stats
            
        except Exception as e:
            self.logger.error(f"❌ Erro na organização Canary: {e}")
            return stats
    
    def _create_canary_integration_structure(self) -> bool:
        """
        Cria estrutura de integração Canary se não existir.
        
        Returns:
            True se estrutura foi criada ou já existia
        """
        try:
            structure = {
                'canary_reception': self.canary_path,
                'integration_maps': self.maps_path / 'integration',
                'templates': self.canary_path / 'templates',
                'workflows': self.canary_path / 'workflows',
                'validation': self.canary_path / 'validation',
                'reports': self.log_path / 'integration'
            }
            
            for name, path in structure.items():
                path.mkdir(parents=True, exist_ok=True)
                self.logger.info(f"📁 Estrutura Canary: {name} -> {path}")
            
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao criar estrutura Canary: {e}")
            return False
    
    def _organize_canary_file(self, file_path: Path) -> bool:
        """
        Organiza um arquivo específico de integração Canary.
        
        Args:
            file_path: Caminho do arquivo
            
        Returns:
            True se arquivo foi organizado com sucesso
        """
        try:
            filename = file_path.name.lower()
            
            # Determinar destino baseado no tipo de arquivo
            if "template" in filename:
                destination = self.canary_path / "templates" / file_path.name
            elif "map" in filename and file_path.suffix == ".json":
                destination = self.maps_path / "integration" / file_path.name
            elif "workflow" in filename:
                destination = self.canary_path / "workflows" / file_path.name
            elif "validation" in filename:
                destination = self.canary_path / "validation" / file_path.name
            else:
                destination = self.canary_path / "integration" / file_path.name
            
            # Mover arquivo se não estiver no local correto
            if file_path != destination:
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(file_path), str(destination))
                self.logger.info(f"📁 Movido: {file_path.name} -> {destination}")
                return True
            
            return False
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao organizar arquivo Canary {file_path}: {e}")
            return False
    
    def validate_canary_integration_structure(self) -> Dict[str, any]:
        """
        Valida a estrutura de integração Canary.
        
        Returns:
            Dicionário com resultados da validação
        """
        self.logger.info("🔍 Validando estrutura de integração Canary...")
        
        validation = {
            "structure_complete": False,
            "missing_components": [],
            "validation_score": 0,
            "recommendations": []
        }
        
        try:
            # Verificar componentes obrigatórios
            required_components = [
                self.canary_path,
                self.canary_path / "templates",
                self.canary_path / "workflows",
                self.canary_path / "validation",
                self.canary_path / "integration",
                self.maps_path / "integration"
            ]
            
            missing = []
            for component in required_components:
                if not component.exists():
                    missing.append(str(component))
            
            validation["missing_components"] = missing
            validation["structure_complete"] = len(missing) == 0
            
            # Calcular score de validação
            total_components = len(required_components)
            existing_components = total_components - len(missing)
            validation["validation_score"] = (existing_components / total_components) * 100
            
            # Gerar recomendações
            if missing:
                validation["recommendations"].append("Criar estrutura de integração Canary faltante")
            if validation["validation_score"] < 100:
                validation["recommendations"].append("Completar estrutura de integração")
            else:
                validation["recommendations"].append("Estrutura de integração pronta para uso")
            
            self.logger.info(f"✅ Validação Canary: {validation['validation_score']:.1f}%")
            return validation
            
        except Exception as e:
            self.logger.error(f"❌ Erro na validação Canary: {e}")
            validation["recommendations"].append(f"Erro na validação: {e}")
            return validation
    
    def is_in_wrong_location(self, file_path: Path) -> bool:
        """Verifica se arquivo está no local errado."""
        context = self.detect_file_context(file_path)
        
        if context == "report":
            return not self.is_in_reports_folder(file_path)
        elif context == "task":
            return not self.is_in_tasks_folder(file_path)
        elif context == "recipe":
            return not self.is_in_recipes_folder(file_path)
        elif context == "obsolete":
            return not self.is_in_archives_folder(file_path)
        
        return False
    
    def is_obsolete(self, file_path: Path) -> bool:
        """Verifica se arquivo é obsoleto."""
        # Verificar padrões de obsolescência
        for pattern in self.patterns["obsolete"]:
            if file_path.match(pattern):
                return True
        
        # Verificar data de modificação (mais de 30 dias)
        if file_path.exists():
            mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
            if datetime.now() - mtime > timedelta(days=30):
                return True
        
        return False
    
    def is_temp_file(self, file_path: Path) -> bool:
        """Verifica se arquivo é temporário."""
        for pattern in self.patterns["temp"]:
            if file_path.match(pattern):
                return True
        return False
    
    def has_category(self, file_path: Path) -> bool:
        """Verifica se arquivo tem categoria definida."""
        context = self.detect_file_context(file_path)
        return context != "other"
    
    def find_duplicates(self, files: List[Path]) -> List[Tuple[Path, Path]]:
        """Encontra arquivos duplicados."""
        duplicates = []
        file_contents = {}
        
        for file_path in files:
            if file_path.exists():
                try:
                    content = file_path.read_text(encoding='utf-8')
                    if content in file_contents:
                        duplicates.append((file_contents[content], file_path))
                    else:
                        file_contents[content] = file_path
                except Exception:
                    continue
        
        return duplicates
    
    def find_unorganized_reports(self) -> List[Path]:
        """Encontra relatórios não organizados."""
        unorganized = []
        
        # Verificar relatórios na raiz da pasta log
        for pattern in self.patterns["report"]:
            for file_path in self.log_path.glob(pattern):
                if file_path.parent == self.log_path:  # Está na raiz
                    unorganized.append(file_path)
        
        return unorganized
    
    def detect_file_context(self, file_path: Path) -> str:
        """Detecta contexto do arquivo automaticamente."""
        for context, pattern_list in self.patterns.items():
            for pattern in pattern_list:
                if file_path.match(pattern):
                    return context
        return "other"
    
    def is_in_reports_folder(self, file_path: Path) -> bool:
        """Verifica se arquivo está na pasta de relatórios."""
        return "reports" in str(file_path)
    
    def is_in_tasks_folder(self, file_path: Path) -> bool:
        """Verifica se arquivo está na pasta de tarefas."""
        return "completed_tasks" in str(file_path) or "temp_tasks" in str(file_path)
    
    def is_in_recipes_folder(self, file_path: Path) -> bool:
        """Verifica se arquivo está na pasta de receitas."""
        return "recipes" in str(file_path)
    
    def is_in_archives_folder(self, file_path: Path) -> bool:
        """Verifica se arquivo está na pasta de arquivos."""
        return "archives" in str(file_path)
    
    def organize_by_category(self) -> Dict[str, int]:
        """
        Organiza arquivos por categoria automaticamente.
        
        Returns:
            Dicionário com número de arquivos organizados por categoria
        """
        self.logger.info("📦 Organizando arquivos por categoria...")
        
        organized_count = {}
        
        for category, config in self.categories.items():
            organized_count[category] = 0
            
            # Criar pasta de destino se não existir
            config["destination"].mkdir(parents=True, exist_ok=True)
            
            # Encontrar arquivos da categoria
            for pattern in config["patterns"]:
                for file_path in self.log_path.rglob(pattern):
                    if file_path.parent != config["destination"]:
                        try:
                            # Mover arquivo
                            new_path = config["destination"] / file_path.name
                            
                            # Evitar sobrescrever arquivos existentes
                            if new_path.exists():
                                counter = 1
                                while new_path.exists():
                                    name = file_path.stem + f"_{counter}" + file_path.suffix
                                    new_path = config["destination"] / name
                                    counter += 1
                            
                            shutil.move(str(file_path), str(new_path))
                            organized_count[category] += 1
                            self.logger.info(f"  ✅ Movido: {file_path.name} → {category}")
                            
                        except Exception as e:
                            self.logger.error(f"  ❌ Erro ao mover {file_path.name}: {e}")
        
        self.logger.info(f"📊 Organização concluída: {sum(organized_count.values())} arquivos")
        return organized_count
    
    def organize_by_date(self) -> Dict[str, int]:
        """
        Organiza relatórios por data automaticamente.
        
        Returns:
            Dicionário com número de relatórios organizados por mês
        """
        self.logger.info("📅 Organizando relatórios por data...")
        
        organized_count = {}
        reports_dir = self.log_path / "reports"
        reports_dir.mkdir(exist_ok=True)
        
        # Encontrar todos os relatórios
        for pattern in self.patterns["report"]:
            for file_path in self.log_path.rglob(pattern):
                if file_path.exists():
                    try:
                        # Extrair data do arquivo ou usar data de modificação
                        file_date = self.extract_date_from_file(file_path)
                        
                        # Criar pasta do mês
                        month_dir = reports_dir / file_date.strftime("%Y-%m")
                        month_dir.mkdir(exist_ok=True)
                        
                        # Mover arquivo
                        new_path = month_dir / file_path.name
                        
                        # Evitar sobrescrever
                        if new_path.exists():
                            counter = 1
                            while new_path.exists():
                                name = file_path.stem + f"_{counter}" + file_path.suffix
                                new_path = month_dir / name
                                counter += 1
                        
                        shutil.move(str(file_path), str(new_path))
                        
                        month_key = file_date.strftime("%Y-%m")
                        organized_count[month_key] = organized_count.get(month_key, 0) + 1
                        
                        self.logger.info(f"  ✅ Organizado por data: {file_path.name} → {month_key}")
                        
                    except Exception as e:
                        self.logger.error(f"  ❌ Erro ao organizar por data {file_path.name}: {e}")
        
        self.logger.info(f"📊 Organização por data concluída: {sum(organized_count.values())} relatórios")
        return organized_count
    
    def extract_date_from_file(self, file_path: Path) -> datetime:
        """Extrai data do arquivo ou usa data de modificação."""
        # Tentar extrair data do nome do arquivo
        date_patterns = [
            r'(\d{4}-\d{2}-\d{2})',
            r'(\d{4}_\d{2}_\d{2})',
            r'(\d{8})'
        ]
        
        for pattern in date_patterns:
            match = re.search(pattern, file_path.name)
            if match:
                date_str = match.group(1)
                try:
                    if '_' in date_str:
                        date_str = date_str.replace('_', '-')
                    elif len(date_str) == 8:
                        date_str = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
                    return datetime.strptime(date_str, "%Y-%m-%d")
                except ValueError:
                    continue
        
        # Usar data de modificação
        return datetime.fromtimestamp(file_path.stat().st_mtime)
    
    def cleanup_temp_files(self) -> int:
        """
        Remove arquivos temporários automaticamente.
        
        Returns:
            Número de arquivos removidos
        """
        self.logger.info("🧹 Limpando arquivos temporários...")
        
        removed_count = 0
        
        for pattern in self.patterns["temp"]:
            for file_path in self.log_path.rglob(pattern):
                if file_path.exists():
                    try:
                        file_path.unlink()
                        removed_count += 1
                        self.logger.info(f"  🗑️ Removido: {file_path.name}")
                    except Exception as e:
                        self.logger.error(f"  ❌ Erro ao remover {file_path.name}: {e}")
        
        self.logger.info(f"📊 Limpeza concluída: {removed_count} arquivos removidos")
        return removed_count
    
    def remove_duplicates(self) -> int:
        """
        Remove arquivos duplicados.
        
        Returns:
            Número de duplicatas removidas
        """
        self.logger.info("🔍 Removendo arquivos duplicados...")
        
        removed_count = 0
        files = list(self.log_path.rglob("*.md"))
        files.extend(list(self.log_path.rglob("*.json")))
        
        duplicates = self.find_duplicates(files)
        
        for original, duplicate in duplicates:
            try:
                duplicate.unlink()
                removed_count += 1
                self.logger.info(f"  🗑️ Duplicata removida: {duplicate.name}")
            except Exception as e:
                self.logger.error(f"  ❌ Erro ao remover duplicata {duplicate.name}: {e}")
        
        self.logger.info(f"📊 Remoção de duplicatas concluída: {removed_count} arquivos")
        return removed_count
    
    def create_organization_structure(self) -> bool:
        """
        Cria estrutura de organização padrão.
        
        Returns:
            True se estrutura foi criada com sucesso
        """
        self.logger.info("🏗️ Criando estrutura de organização...")
        
        try:
            # Estrutura de pastas obrigatória
            structure = {
                "reports": {
                    "current": self.log_path / "reports" / "current",
                    "2025-01": self.log_path / "reports" / "2025-01",
                    "2025-02": self.log_path / "reports" / "2025-02"
                },
                "completed_tasks": {
                    "system_updates": self.log_path / "completed_tasks" / "system_updates",
                    "feature_implementations": self.log_path / "completed_tasks" / "feature_implementations",
                    "bug_fixes": self.log_path / "completed_tasks" / "bug_fixes"
                },
                "archives": {
                    "obsolete_files": self.log_path / "archives" / "obsolete_files",
                    "historical_data": self.log_path / "archives" / "historical_data",
                    "old_reports": self.log_path / "archives" / "old_reports"
                },
                "recipes": self.log_path / "recipes",
                "learning": self.log_path / "learning",
                "python_agent": self.log_path / "python_agent",
                "aaa_validation": self.log_path / "aaa_validation",
                "aaa_fixes": self.log_path / "aaa_fixes",
                "temp_tasks": self.log_path / "temp_tasks"
            }
            
            # Criar todas as pastas
            for category, paths in structure.items():
                if isinstance(paths, dict):
                    for subcategory, path in paths.items():
                        path.mkdir(parents=True, exist_ok=True)
                        self.logger.info(f"  ✅ Criada pasta: {path}")
                else:
                    paths.mkdir(parents=True, exist_ok=True)
                    self.logger.info(f"  ✅ Criada pasta: {paths}")
            
            self.logger.info("✅ Estrutura de organização criada com sucesso")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao criar estrutura: {e}")
            return False
    
    def generate_organization_report(self, results: Dict[str, Any]) -> str:
        """
        Gera relatório de organização.
        
        Args:
            results: Resultados da organização
            
        Returns:
            Relatório em formato markdown
        """
        report = f"""# Relatório de Organização Inteligente

**Data**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Agente**: Intelligent Organization Agent  
**Status**: ✅ **ORGANIZAÇÃO CONCLUÍDA**

---

## 📊 Resumo da Organização

### **Problemas Detectados**:
- **Arquivos no local errado**: {len(results.get('issues', {}).get('files_in_wrong_location', []))}
- **Arquivos duplicados**: {len(results.get('issues', {}).get('duplicate_files', []))}
- **Arquivos obsoletos**: {len(results.get('issues', {}).get('obsolete_files', []))}
- **Relatórios não organizados**: {len(results.get('issues', {}).get('unorganized_reports', []))}
- **Arquivos temporários**: {len(results.get('issues', {}).get('temp_files_not_cleaned', []))}

### **Ações Realizadas**:
- **Arquivos organizados por categoria**: {sum(results.get('organized_by_category', {}).values())}
- **Relatórios organizados por data**: {sum(results.get('organized_by_date', {}).values())}
- **Arquivos temporários removidos**: {results.get('temp_files_removed', 0)}
- **Duplicatas removidas**: {results.get('duplicates_removed', 0)}

---

## 📁 Estrutura Criada

### **Pastas de Relatórios**:
- `reports/current/` - Relatórios atuais
- `reports/2025-01/` - Relatórios de janeiro 2025
- `reports/2025-02/` - Relatórios de fevereiro 2025

### **Pastas de Tarefas**:
- `completed_tasks/system_updates/` - Atualizações do sistema
- `completed_tasks/feature_implementations/` - Implementações de features
- `completed_tasks/bug_fixes/` - Correções de bugs

### **Pastas de Arquivo**:
- `archives/obsolete_files/` - Arquivos obsoletos
- `archives/historical_data/` - Dados históricos
- `archives/old_reports/` - Relatórios antigos

---

## 🎯 Benefícios Alcançados

### **🧹 Organização**:
- ✅ Sistema limpo e organizado
- ✅ Arquivos fáceis de encontrar
- ✅ Estrutura consistente
- ✅ Histórico rastreável

### **📊 Eficiência**:
- ✅ Busca rápida de informações
- ✅ Navegação intuitiva
- ✅ Manutenção simplificada
- ✅ Produtividade aumentada

---

## 📝 Próximos Passos

1. **Monitoramento contínuo** da organização
2. **Execução automática** diária
3. **Validação periódica** da estrutura
4. **Otimização contínua** do sistema

---

*Relatório gerado automaticamente pelo Intelligent Organization Agent*
"""
        
        return report
    
    def run_full_organization(self) -> Dict[str, Any]:
        """
        Executa organização completa do sistema.
        
        Returns:
            Resultados da organização
        """
        self.logger.info("🚀 Iniciando organização completa do sistema...")
        
        try:
            # 1. Criar estrutura de organização
            structure_created = self.create_organization_structure()
            
            # 2. Detectar problemas
            issues = self.detect_organization_issues()
            
            # 3. Organizar por categoria
            organized_by_category = self.organize_by_category()
            
            # 4. Organizar por data
            organized_by_date = self.organize_by_date()
            
            # 5. Limpar arquivos temporários
            temp_files_removed = self.cleanup_temp_files()
            
            # 6. Remover duplicatas
            duplicates_removed = self.remove_duplicates()
            
            # 7. Gerar relatório
            results = {
                "timestamp": datetime.now().isoformat(),
                "structure_created": structure_created,
                "issues": issues,
                "organized_by_category": organized_by_category,
                "organized_by_date": organized_by_date,
                "temp_files_removed": temp_files_removed,
                "duplicates_removed": duplicates_removed,
                "success": True
            }
            
            # Salvar relatório
            report_content = self.generate_organization_report(results)
            report_path = self.log_path / "reports" / "current" / f"ORGANIZATION_REPORT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            report_path.parent.mkdir(parents=True, exist_ok=True)
            report_path.write_text(report_content, encoding='utf-8')
            
            self.logger.info("✅ Organização completa concluída com sucesso!")
            return results
            
        except Exception as e:
            self.logger.error(f"❌ Erro durante organização: {e}")
            return {
                "timestamp": datetime.now().isoformat(),
                "success": False,
                "error": str(e)
            }

    def _is_ignored(self, file_path: Path) -> bool:
        """
        Verifica se um arquivo deve ser ignorado pela organização.
        
        Args:
            file_path: Caminho do arquivo
            
        Returns:
            True se o arquivo deve ser ignorado
        """
        # Ignorar arquivos do sistema
        ignored_patterns = [
            '.git',
            '.gitignore',
            '__pycache__',
            '.pyc',
            '.DS_Store',
            'Thumbs.db',
            '.obsidian'
        ]
        
        # Ignorar submódulos (fontes de verdade imutáveis)
        submodule_patterns = [
            'otclient/',
            'canary/'
        ]
        
        file_str = str(file_path)
        
        # Verificar padrões do sistema
        if any(pattern in file_str for pattern in ignored_patterns):
            return True
        
        # Verificar se está em submódulo (não deve ser organizado)
        if any(pattern in file_str for pattern in submodule_patterns):
            return True
        
        return False

def main():
    """Função principal."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Agente de Organização Inteligente')
    parser.add_argument('--full', action='store_true', help='Executar organização completa')
    parser.add_argument('--detect', action='store_true', help='Apenas detectar problemas')
    parser.add_argument('--cleanup', action='store_true', help='Apenas limpeza de arquivos temporários')
    parser.add_argument('--organize', action='store_true', help='Apenas organização por categoria')
    
    args = parser.parse_args()
    
    agent = IntelligentOrganizationAgent()
    
    if args.detect:
        issues = agent.detect_organization_issues()
        print("🔍 Problemas detectados:")
        for issue_type, files in issues.items():
            print(f"  {issue_type}: {len(files)} arquivos")
    
    elif args.cleanup:
        removed = agent.cleanup_temp_files()
        print(f"🧹 {removed} arquivos temporários removidos")
    
    elif args.organize:
        organized = agent.organize_by_category()
        print("📦 Arquivos organizados por categoria:")
        for category, count in organized.items():
            print(f"  {category}: {count} arquivos")
    
    elif args.full:
        results = agent.run_full_organization()
        if results["success"]:
            print("✅ Organização completa concluída!")
            print(f"📊 {sum(results['organized_by_category'].values())} arquivos organizados")
            print(f"🧹 {results['temp_files_removed']} arquivos temporários removidos")
        else:
            print(f"❌ Erro: {results['error']}")
    
    else:
        # Modo padrão: organização completa
        results = agent.run_full_organization()
        if results["success"]:
            print("✅ Organização completa concluída!")
        else:
            print(f"❌ Erro: {results['error']}")

if __name__ == '__main__':
    main() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = AgentorchestratorModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script intelligent_organization_agent.py executado com sucesso via módulo agents.agent_orchestrator")
    else:
        print(f"❌ Erro na execução do script intelligent_organization_agent.py via módulo agents.agent_orchestrator")

## 🔗 **Links Automáticos - Scripts**

> [!info] **Script de Automação**
> Este script faz parte do sistema de automação da wiki

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]

### **🔧 Links de Scripts**
- [[../update/README|Documentação de Scripts]]
- [[../maps/scripts_index|Índice de Scripts]]
- [[../templates/README|Templates de Scripts]]

### **📊 Scripts Relacionados**
- [[../update/automatic_linkage_system.py|automatic_linkage_system.py]]
- [[../update/create_automatic_link_templates.py|create_automatic_link_templates.py]]
- [[../update/orphan_files_analyzer.py|orphan_files_analyzer.py]]
- [[../update/update_json_maps.py|update_json_maps.py]]

### **📈 Métricas do Script**
- **Nome**: migrated_intelligent_organization_agent
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

