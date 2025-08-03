from unicode_aliases import *
# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
TIMEOUT_SECONDS = 60

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: script_migration_agent.py
Módulo de Destino: maps.map_updater
Data de Migração: 2025-08-01 12:21:35

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import MapupdaterModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 Script Migration Agent - Epic 12 Task 12.3
=============================================

Script para migrar 172 scripts Python existentes para 50 módulos organizados.
Baseado na estrutura modular unificada criada na Task 12.2.

Responsável: Migration Agent
Duração: 5-7 dias
Dependência: Task 12.2 (Estrutura modular unificada)
"""

import json
import ast
from datetime import datetime
import logging

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ScriptMigrationAgent:
    """Agente para migração de scripts Python para módulos organizados."""
    
    def __init__(self):
        self.project_root = Path(__file__).parent.parent.parent
        self.update_path = self.project_root / "wiki/update"
        self.modules_path = self.project_root / "wiki/update/modules"
        
        # Carregar configuração da estrutura modular
        self.structure_config = self.load_structure_config()
        self.script_mapping = self.load_script_mapping()
        
        # Estatísticas de migração
        self.migration_stats = {
            "total_scripts": 0,
            "scripts_migrated": 0,
            "scripts_failed": 0,
            "modules_updated": 0,
            "errors": [],
            "warnings": []
        }
        
    def load_structure_config(self) -> Dict[str, Any]:
        """Carrega configuração da estrutura modular."""
        config_file = self.modules_path / "structure_config.json"
        if config_file.exists():
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            logger.error("❌ Arquivo de configuração da estrutura não encontrado")
            return {}
    
    def load_script_mapping(self) -> Dict[str, str]:
        """Carrega mapeamento de scripts para módulos."""
        mapping_file = self.modules_path / "script_mapping.json"
        if mapping_file.exists():
            with open(mapping_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            logger.error("❌ Arquivo de mapeamento de scripts não encontrado")
            return {}
    
    def discover_python_scripts(self) -> List[Path]:
        """Descobre todos os scripts Python no projeto."""
        logger.info("🔍 Descobrindo scripts Python...")
        
        scripts = []
        search_paths = [
            self.update_path,
            self.project_root / "wiki/bmad",
            self.project_root / "wiki/tools"
        ]
        
        for search_path in search_paths:
            if search_path.exists():
                for py_file in search_path.rglob("*.py"):
                    # Excluir arquivos de teste e cache
                    if not any(exclude in str(py_file) for exclude in ["__pycache__", "test_", "_test"]):
                        scripts.append(py_file)
        
        logger.info(f"📊 Encontrados {len(scripts)} scripts Python")
        return scripts
    
    def analyze_script(self, script_path: Path) -> Dict[str, Any]:
        """Analisa um script Python para extrair informações."""
        try:
            # Tentar diferentes encodings
            content = None
            for encoding in ['utf-8', 'latin-1', 'cp1252']:
                try:
                    with open(script_path, 'r', encoding=encoding) as f:
                        content = f.read()
                    break
                except UnicodeDecodeError:
                    continue
            
            if content is None:
                logger.error(f"❌ Não foi possível ler {script_path} com nenhum encoding")
                return {
                    "path": str(script_path),
                    "name": script_path.name,
                    "error": "encoding_error",
                    "size": script_path.stat().st_size if script_path.exists() else 0
                }
            
            # Análise básica do script
            analysis = {
                "path": str(script_path),
                "name": script_path.name,
                "size": script_path.stat().st_size,
                "lines": len(content.split('\n')),
                "classes": [],
                "functions": [],
                "imports": [],
                "dependencies": [],
                "complexity": "low",
                "content": content
            }
            
            # Análise AST para extrair classes e funções
            try:
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        analysis["classes"].append(node.name)
                    elif isinstance(node, ast.FunctionDef):
                        analysis["functions"].append(node.name)
                    elif isinstance(node, ast.Import):
                        for alias in node.names:
                            analysis["imports"].append(alias.name)
                    elif isinstance(node, ast.ImportFrom):
                        if node.module:
                            analysis["imports"].append(node.module)
            except SyntaxError:
                analysis["syntax_error"] = True
            
            # Determinar complexidade
            if len(analysis["classes"]) > 5 or len(analysis["functions"]) > 20:
                analysis["complexity"] = "high"
            elif len(analysis["classes"]) > 2 or len(analysis["functions"]) > 10:
                analysis["complexity"] = "medium"
            
            return analysis
            
        except Exception as e:
            logger.error(f"❌ Erro ao analisar {script_path}: {e}")
            return {
                "path": str(script_path),
                "name": script_path.name,
                "error": str(e),
                "size": script_path.stat().st_size if script_path.exists() else 0
            }
    
    def determine_target_module(self, script_analysis: Dict[str, Any]) -> Optional[str]:
        """Determina o módulo de destino para um script."""
        script_name = script_analysis["name"]
        
        # Verificar mapeamento direto
        if script_name in self.script_mapping:
            return self.script_mapping[script_name]
        
        # Análise baseada no conteúdo e nome
        script_path = script_analysis["path"].lower()
        script_content = script_analysis.get("content", "").lower()
        
        # Mapeamento baseado em palavras-chave
        keyword_mapping = {
            "map": "maps",
            "index": "maps",
            "update": "maps",
            "agent": "agents",
            "orchestrator": "agents",
            "workflow": "agents",
            "metrics": "metrics",
            "monitor": "metrics",
            "dashboard": "metrics",
            "analyze": "analysis",
            "search": "analysis",
            "context": "analysis",
            "python": "python",
            "script": "python",
            "error": "python",
            "test": "python",
            "tool": "tools",
            "file": "tools",
            "backup": "tools",
            "cleanup": "tools",
            "git": "tools",
            "wiki": "documentation",
            "documentation": "documentation",
            "markdown": "documentation"
        }
        
        for keyword, category in keyword_mapping.items():
            if keyword in script_path or keyword in script_name.lower():
                # Encontrar módulo específico na categoria
                category_modules = self.structure_config.get("categories", {}).get(category, {}).get("modules", {})
                for module_name in category_modules.keys():
                    if keyword in module_name:
                        return f"{category}.{module_name}"
        
        # Fallback para módulo genérico
        return "python.python_agent"
    
    def migrate_script_to_module(self, script_path: Path, target_module: str) -> bool:
        """Migra um script para o módulo de destino."""
        try:
            # Determinar caminho do módulo de destino
            category, module_name = target_module.split('.')
            module_path = self.modules_path / category / module_name
            
            if not module_path.exists():
                logger.error(f"❌ Módulo de destino não encontrado: {target_module}")
                return False
            
            # Ler conteúdo do script
            with open(script_path, 'r', encoding='utf-8') as f:
                script_content = f.read()
            
            # Criar versão migrada do script
            migrated_content = self.create_migrated_script(script_content, script_path.name, target_module)
            
            # Salvar no módulo de destino
            migrated_file = module_path / f"migrated_{script_path.name}"
            with open(migrated_file, 'w', encoding='utf-8') as f:
                f.write(migrated_content)
            
            # Atualizar __init__.py do módulo
            self.update_module_init(module_path, script_path.name, target_module)
            
            # Atualizar configuração do módulo
            self.update_module_config(module_path, script_path.name, target_module)
            
            logger.info(f"✅ Script {script_path.name} migrado para {target_module}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Erro ao migrar {script_path}: {e}")
            self.migration_stats["errors"].append(f"{script_path}: {e}")
            return False
    
    def create_migrated_script(self, original_content: str, script_name: str, target_module: str) -> str:
        """Cria versão migrada do script."""
        category, module_name = target_module.split('.')
        
        migrated_content = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: {script_name}
Módulo de Destino: {target_module}
Data de Migração: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo

# Conteúdo original do script
{original_content}

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = {module_name.replace('_', '').title()}Module()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script {script_name} executado com sucesso via módulo {target_module}")
    else:
        print(f"❌ Erro na execução do script {script_name} via módulo {target_module}")
'''
        
        return migrated_content
    
    def update_module_init(self, module_path: Path, script_name: str, target_module: str):
        """Atualiza __init__.py do módulo para incluir script migrado."""
        init_file = module_path / "__init__.py"
        
        if init_file.exists():
            with open(init_file, 'r', encoding='utf-8') as f:
                init_content = f.read()
            
            # Adicionar import do script migrado
            import_line = f'from .migrated_{script_name.replace(".py", "")} import integrate_with_module\n'
            
            if import_line not in init_content:
                # Inserir após os imports existentes
                lines = init_content.split('\n')
                insert_index = 0
                for i, line in enumerate(lines):
                    if line.startswith('import ') or line.startswith('from '):
                        insert_index = i + 1
                
                lines.insert(insert_index, import_line)
                init_content = '\n'.join(lines)
                
                with open(init_file, 'w', encoding='utf-8') as f:
                    f.write(init_content)
    
    def update_module_config(self, module_path: Path, script_name: str, target_module: str):
        """Atualiza configuração do módulo."""
        config_file = module_path / "config.json"
        
        if config_file.exists():
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            # Adicionar script migrado à configuração
            if "migrated_scripts" not in config:
                config["migrated_scripts"] = []
            
            script_info = {
                "name": script_name,
                "original_path": str(self.update_path / script_name),
                "migration_date": datetime.now().isoformat(),
                "status": "migrated"
            }
            
            if script_info not in config["migrated_scripts"]:
                config["migrated_scripts"].append(script_info)
                
                with open(config_file, 'w', encoding='utf-8') as f:
                    json.dump(config, f, indent=2, ensure_ascii=False)
    
    def migrate_all_scripts(self) -> bool:
        """Migra todos os scripts descobertos."""
        logger.info("🚀 Iniciando migração de scripts...")
        
        # Descobrir scripts
        scripts = self.discover_python_scripts()
        self.migration_stats["total_scripts"] = len(scripts)
        
        if not scripts:
            logger.warning("⚠️ Nenhum script Python encontrado")
            return False
        
        # Migrar cada script
        for script_path in scripts:
            logger.info(f"📋 Processando: {script_path.name}")
            
            # Analisar script
            analysis = self.analyze_script(script_path)
            
            # Determinar módulo de destino
            target_module = self.determine_target_module(analysis)
            
            if target_module:
                # Migrar script
                success = self.migrate_script_to_module(script_path, target_module)
                
                if success:
                    self.migration_stats["scripts_migrated"] += 1
                else:
                    self.migration_stats["scripts_failed"] += 1
            else:
                logger.warning(f"⚠️ Não foi possível determinar módulo para {script_path.name}")
                self.migration_stats["warnings"].append(f"Não foi possível determinar módulo para {script_path.name}")
                self.migration_stats["scripts_failed"] += 1
        
        # Atualizar estatísticas
        self.migration_stats["modules_updated"] = len(set(
            target_module.split('.')[0] for target_module in self.script_mapping.values()
        ))
        
        logger.info("✅ Migração de scripts concluída!")
        return True
    
    def generate_migration_report(self) -> Dict[str, Any]:
        """Gera relatório da migração."""
        return {
            "task": "12.3",
            "description": "Migrar scripts existentes para módulos",
            "status": "completed",
            "timestamp": datetime.now().isoformat(),
            "migration_stats": self.migration_stats,
            "structure_info": {
                "total_modules": 50,
                "total_categories": 7,
                "scripts_mapped": len(self.script_mapping)
            },
            "next_task": "12.4 - Implementar sistema de catálogo de funções"
        }
    
    def save_migration_report(self, report: Dict[str, Any]):
        """Salva relatório da migração."""
        report_file = self.project_root / "wiki/log/task_12_3_migration_report.json"
        report_file.parent.mkdir(exist_ok=True)
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        logger.info(f"📄 Relatório salvo em: {report_file}")

def main():
    """Função principal do script."""
    print("🚀 Script Migration Agent - Epic 12 Task 12.3")
    print("=" * 60)
    
    agent = ScriptMigrationAgent()
    
    # Executar migração
    success = agent.migrate_all_scripts()
    
    if success:
        # Gerar relatório
        report = agent.generate_migration_report()
        agent.save_migration_report(report)
        
        stats = report["migration_stats"]
        print("\n✅ Migração de scripts concluída com sucesso!")
        print(f"📊 Scripts processados: {stats['total_scripts']}")
        print(f"✅ Scripts migrados: {stats['scripts_migrated']}")
        print(f"❌ Scripts com falha: {stats['scripts_failed']}")
        print(f"🔄 Módulos atualizados: {stats['modules_updated']}")
        print(f"⚠️ Avisos: {len(stats['warnings'])}")
        print(f"❌ Erros: {len(stats['errors'])}")
        print(f"📋 Próxima task: {report['next_task']}")
        
        if stats['warnings']:
            print("\n⚠️ Avisos:")
            for warning in stats['warnings'][:5]:  # Mostrar apenas os primeiros 5
                print(f"  - {warning}")
        
        if stats['errors']:
            print("\n❌ Erros:")
            for error in stats['errors'][:5]:  # Mostrar apenas os primeiros 5
                print(f"  - {error}")
        
    else:
        print("❌ Erro na migração de scripts")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = MapupdaterModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script script_migration_agent.py executado com sucesso via módulo maps.map_updater")
    else:
        print(f"❌ Erro na execução do script script_migration_agent.py via módulo maps.map_updater")
