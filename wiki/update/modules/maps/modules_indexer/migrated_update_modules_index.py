from unicode_aliases import *
# Constantes
MAX_RETRIES = 8

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: update_modules_index.py
Módulo de Destino: maps.modules_indexer
Data de Migração: 2025-08-01 12:21:35

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import ModulesindexerModule

# Conteúdo original do script
#!/usr/bin/env python3
"""
Script para indexação dos módulos Lua do OTClient
Atualiza: wiki/maps/modules_index.json
"""
import json
import re
from datetime import datetime

class ModulesIndexer:
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.modules_path = self.project_root / "modules"
        self.modules = []
        self.categories = {
            "client": {"name": "Módulos do Cliente", "modules": []},
            "game": {"name": "Módulos de Jogo", "modules": []},
            "core": {"name": "Módulos Core", "modules": []},
            "ui": {"name": "Módulos de Interface", "modules": []},
            "other": {"name": "Outros Módulos", "modules": []}
        }
        
    def scan_modules(self) -> List[str]:
        """Escaneia todos os módulos Lua"""
        if not self.modules_path.exists():
            print(f"Pasta modules não encontrada: {self.modules_path}")
            return []
        
        modules = []
        for module_dir in self.modules_path.iterdir():
            if module_dir.is_dir():
                modules.append(str(module_dir))
        
        return sorted(modules)
    
    def analyze_module(self, module_path: str) -> Dict[str, Any]:
        """Analisa um módulo Lua"""
        try:
            module_dir = Path(module_path)
            module_name = module_dir.name
            
            # Encontrar arquivos Lua
            lua_files = list(module_dir.glob("*.lua"))
            otmod_files = list(module_dir.glob("*.otmod"))
            otui_files = list(module_dir.glob("*.otui"))
            
            # Analisar arquivo principal
            main_lua = None
            for lua_file in lua_files:
                if lua_file.name == f"{module_name}.lua":
                    main_lua = lua_file
                    break
            
            if not main_lua and lua_files:
                main_lua = lua_files[0]
            
            # Extrair informações do arquivo principal
            module_info = {
                "name": module_name,
                "path": str(module_path),
                "files": {
                    "lua": [str(f) for f in lua_files],
                    "otmod": [str(f) for f in otmod_files],
                    "otui": [str(f) for f in otui_files]
                },
                "main_file": str(main_lua) if main_lua else None,
                "total_files": len(lua_files) + len(otmod_files) + len(otui_files),
                "lua_files_count": len(lua_files),
                "otmod_files_count": len(otmod_files),
                "otui_files_count": len(otui_files)
            }
            
            # Analisar conteúdo se houver arquivo principal
            if main_lua:
                with open(main_lua, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                module_info.update({
                    "description": self.extract_description(content),
                    "apis": self.extract_lua_apis(main_lua),
                    "dependencies": self.extract_dependencies(content),
                    "lines": len(content.split('\n')),
                    "size": len(content)
                })
            
            # Categorizar módulo
            module_info["category"] = self.categorize_module(module_name)
            
            return module_info
            
        except Exception as e:
            print(f"Erro ao analisar módulo {module_path}: {e}")
            return None
    
    def extract_description(self, content: str) -> str:
        """Extrai descrição do módulo"""
        lines = content.split('\n')
        for line in lines[:20]:
            line = line.strip()
            if line.startswith('--') and len(line) > 2:
                return line[2:].strip()
            elif line.startswith('---') and len(line) > 3:
                return line[3:].strip()
        
        return "Sem descrição disponível"
    
    def extract_lua_apis(self, file_path: Path) -> List[Dict[str, Any]]:
        """Extrai APIs Lua do arquivo"""
        apis = []
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Encontrar funções
            function_pattern = r'function\s+([a-zA-Z_][a-zA-Z0-9_:]*)\s*\([^)]*\)'
            functions = re.findall(function_pattern, content)
            
            for func in functions:
                apis.append({
                    "type": "function",
                    "name": func,
                    "file": str(file_path)
                })
            
            # Encontrar classes/tabelas
            class_pattern = r'([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*{}'
            classes = re.findall(class_pattern, content)
            
            for cls in classes:
                    apis.append({
                    "type": "class",
                    "name": cls,
                    "file": str(file_path)
                })
                
        except Exception:
            pass
            
            return apis
            
    def extract_dependencies(self, content: str) -> List[str]:
        """Extrai dependências do módulo"""
        dependencies = []
        
        # Procurar por require
        require_pattern = r'require\s*\([\'"]([^\'"]+)[\'"]\)'
        requires = re.findall(require_pattern, content)
        dependencies.extend(requires)
        
        # Procurar por imports
        import_pattern = r'import\s+([a-zA-Z_][a-zA-Z0-9_]*)'
        imports = re.findall(import_pattern, content)
        dependencies.extend(imports)
        
        return list(set(dependencies))
    
    def categorize_module(self, module_name: str) -> str:
        """Categoriza um módulo"""
        name_lower = module_name.lower()
        
        if 'client' in name_lower:
            return 'client'
        elif 'game' in name_lower or 'battle' in name_lower or 'creature' in name_lower:
            return 'game'
        elif 'core' in name_lower or 'lib' in name_lower:
            return 'core'
        elif 'ui' in name_lower or 'interface' in name_lower or 'widget' in name_lower:
            return 'ui'
        else:
            return 'other'
    
    def categorize_modules(self):
        """Categoriza todos os módulos"""
        for module in self.modules:
            category = module.get('category', 'other')
            if category in self.categories:
                self.categories[category]['modules'].append(module)
            else:
                self.categories['other']['modules'].append(module)
    
    def generate_statistics(self) -> Dict[str, Any]:
        """Gera estatísticas dos módulos"""
        stats = {
            "total_modules": len(self.modules),
            "by_category": {},
            "total_files": 0,
            "total_lua_files": 0,
            "total_otmod_files": 0,
            "total_otui_files": 0,
            "total_lines": 0,
            "total_size": 0
        }
        
        # Estatísticas por categoria
        for category, cat_info in self.categories.items():
            stats["by_category"][category] = len(cat_info["modules"])
        
        # Estatísticas gerais
        for module in self.modules:
            stats["total_files"] += module.get('total_files', 0)
            stats["total_lua_files"] += module.get('lua_files_count', 0)
            stats["total_otmod_files"] += module.get('otmod_files_count', 0)
            stats["total_otui_files"] += module.get('otui_files_count', 0)
            stats["total_lines"] += module.get('lines', 0)
            stats["total_size"] += module.get('size', 0)
        
        return stats
    
    def generate_search_index(self) -> Dict[str, Any]:
        """Gera índice de busca"""
        search_index = {
            "by_name": {},
            "by_api": {},
            "by_dependency": {}
        }
        
        # Indexar por nome
        for module in self.modules:
            name = module.get('name', '').lower()
            search_index["by_name"][name] = module.get('name')
        
        # Indexar por API
        for module in self.modules:
            for api in module.get('apis', []):
                api_name = api.get('name', '').lower()
                if api_name not in search_index["by_api"]:
                    search_index["by_api"][api_name] = []
                search_index["by_api"][api_name].append(module.get('name'))
        
        # Indexar por dependência
        for module in self.modules:
            for dep in module.get('dependencies', []):
                dep_lower = dep.lower()
                if dep_lower not in search_index["by_dependency"]:
                    search_index["by_dependency"][dep_lower] = []
                search_index["by_dependency"][dep_lower].append(module.get('name'))
        
        return search_index
    
    def generate_modules_index(self) -> Dict[str, Any]:
        """Gera o índice completo dos módulos"""
        print("Gerando índice dos módulos...")
        
        # Escanear módulos
        modules_paths = self.scan_modules()
        print(f"Encontrados {len(modules_paths)} módulos")
        
        # Analisar cada módulo
        for module_path in modules_paths:
            module_info = self.analyze_module(module_path)
            if module_info:
                self.modules.append(module_info)
        
        # Categorizar módulos
        self.categorize_modules()
        
        # Gerar estatísticas
        statistics = self.generate_statistics()
        
        # Gerar índice de busca
        search_index = self.generate_search_index()
        
        # Estrutura final
        modules_index = {
            "metadata": {
                "version": "1.0",
                "last_updated": datetime.now().isoformat(),
                "total_modules": len(self.modules),
                "description": "Índice dos módulos Lua do OTClient"
            },
            "categories": self.categories,
            "statistics": statistics,
            "search_index": search_index
        }
        
        return modules_index
    
    def save_index(self, modules_index: Dict[str, Any], output_file: str = "wiki/maps/modules_index.json"):
        """Salva o índice em arquivo JSON"""
        try:
            # Criar diretório se não existir
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(modules_index, f, indent=2, ensure_ascii=False)
            
            print(f"Índice salvo em {output_file}")
            
        except Exception as e:
            print(f"Erro ao salvar índice: {e}")
    
    def update_index(self):
        """Atualiza o índice dos módulos"""
        modules_index = self.generate_modules_index()
        return self.save_index(modules_index)

def main():
    """Função principal"""
    print("Iniciando indexação dos módulos...")
    
    try:
        indexer = ModulesIndexer()
        success = indexer.update_index()
        
        if success:
            print("Indexação dos módulos concluída com sucesso!")
        else:
            print("Erro na indexação dos módulos!")
            
    except Exception as e:
        print(f"Erro durante indexação: {e}")

if __name__ == "__main__":
    main() 


# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = ModulesindexerModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script update_modules_index.py executado com sucesso via módulo maps.modules_indexer")
    else:
        print(f"❌ Erro na execução do script update_modules_index.py via módulo maps.modules_indexer")
