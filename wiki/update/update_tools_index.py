#!/usr/bin/env python3
"""
Script para indexação das ferramentas do OTClient
Atualiza: wiki/maps/tools_index.json
"""
import os
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any

class ToolsIndexer:
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.tools_path = self.project_root / "tools"
        self.tools = []
        self.categories = {
            "build": {"name": "Ferramentas de Build", "tools": []},
            "generator": {"name": "Geradores", "tools": []},
            "api": {"name": "APIs e Interfaces", "tools": []},
            "utility": {"name": "Utilitários", "tools": []},
            "other": {"name": "Outras Ferramentas", "tools": []}
        }
    
    def scan_tools(self) -> List[str]:
        """Escaneia todas as ferramentas"""
        if not self.tools_path.exists():
            print(f"Pasta tools não encontrada: {self.tools_path}")
            return []
        
        tools = []
        
        # Escanear arquivos e pastas
        for item in self.tools_path.iterdir():
            if item.is_file() or item.is_dir():
                tools.append(str(item))
        
        return sorted(tools)
    
    def analyze_tool(self, tool_path: str) -> Dict[str, Any]:
        """Analisa uma ferramenta"""
        try:
            item_path = Path(tool_path)
            item_name = item_path.name
            
            # Determinar tipo
            is_file = item_path.is_file()
            is_dir = item_path.is_dir()
            
            # Categorizar ferramenta
            category = self.categorize_tool(item_path)
            
            # Extrair informações
            tool_info = self.extract_tool_info(item_path)
            
            # Obter estatísticas
            stat = item_path.stat()
            
            tool_data = {
                "name": item_name,
                "path": str(tool_path),
                "type": "file" if is_file else "directory",
                "category": category,
                "size": stat.st_size if is_file else 0,
                "lines": self.count_lines(item_path) if is_file else 0,
                "last_modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                "info": tool_info
            }
            
            return tool_data
            
        except Exception as e:
            print(f"Erro ao analisar ferramenta {tool_path}: {e}")
            return None
    
    def categorize_tool(self, file_path: Path) -> str:
        """Categoriza uma ferramenta"""
        file_name = file_path.name.lower()
        file_ext = file_path.suffix.lower()
        
        # Categorizar por nome
        if 'build' in file_name or 'make' in file_name or 'compile' in file_name:
            return 'build'
        elif 'gen' in file_name or 'generator' in file_name or 'create' in file_name:
            return 'generator'
        elif 'api' in file_name or 'interface' in file_name:
            return 'api'
        elif 'util' in file_name or 'helper' in file_name or 'tool' in file_name:
            return 'utility'
        else:
            return 'other'
    
    def extract_tool_info(self, file_path: Path) -> Dict[str, Any]:
        """Extrai informações da ferramenta"""
        info = {}
        
        try:
            if file_path.is_file():
                # Analisar arquivo
                file_ext = file_path.suffix.lower()
                
                if file_ext in ['.py', '.lua', '.sh', '.bat']:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
                    info = {
                        "description": self.extract_description(content),
                        "language": self.get_language(file_ext),
                        "functions": self.extract_functions(content, file_ext),
                        "dependencies": self.extract_dependencies(content)
                    }
            else:
                    info = {
                        "description": f"Arquivo {file_ext}",
                        "language": "unknown"
                    }
            else:
                # Analisar diretório
                files = list(file_path.rglob("*"))
                info = {
                    "description": f"Diretório com {len(files)} itens",
                    "files_count": len(files),
                    "subdirectories": len([f for f in files if f.is_dir()])
                }
                
        except Exception:
            info = {"description": "Informações não disponíveis"}
        
        return info
    
    def extract_description(self, content: str) -> str:
        """Extrai descrição do conteúdo"""
        lines = content.split('\n')
        for line in lines[:10]:
            line = line.strip()
            if line.startswith('#') and len(line) > 1:
                return line[1:].strip()
            elif line.startswith('--') and len(line) > 2:
                return line[2:].strip()
            elif line.startswith('"""') or line.startswith("'''"):
                return line[3:].strip()
        
        return "Sem descrição disponível"
    
    def get_language(self, file_ext: str) -> str:
        """Determina a linguagem do arquivo"""
        language_map = {
            '.py': 'Python',
            '.lua': 'Lua',
            '.sh': 'Shell',
            '.bat': 'Batch',
            '.js': 'JavaScript',
            '.html': 'HTML',
            '.css': 'CSS',
            '.json': 'JSON',
            '.xml': 'XML'
        }
        
        return language_map.get(file_ext, 'Unknown')
    
    def extract_functions(self, content: str, file_ext: str) -> List[str]:
        """Extrai funções do arquivo"""
        functions = []
        
        try:
            if file_ext == '.py':
                # Funções Python
                pattern = r'def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
                functions = re.findall(pattern, content)
            elif file_ext == '.lua':
                # Funções Lua
                pattern = r'function\s+([a-zA-Z_][a-zA-Z0-9_:]*)\s*\('
                functions = re.findall(pattern, content)
            elif file_ext in ['.sh', '.bat']:
                # Funções Shell/Batch
                pattern = r'([a-zA-Z_][a-zA-Z0-9_]*)\s*\(\)\s*{'
                functions = re.findall(pattern, content)
                
        except Exception:
            pass
        
        return functions
    
    def extract_dependencies(self, content: str) -> List[str]:
        """Extrai dependências do arquivo"""
        dependencies = []
        
        try:
            # Procurar por imports/requires
            patterns = [
                r'import\s+([a-zA-Z_][a-zA-Z0-9_]*)',
                r'require\s*\([\'"]([^\'"]+)[\'"]\)',
                r'from\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+import'
            ]
            
            for pattern in patterns:
            matches = re.findall(pattern, content)
            dependencies.extend(matches)
            
        except Exception:
            pass
        
        return list(set(dependencies))
    
    def count_lines(self, file_path: Path) -> int:
        """Conta linhas de um arquivo"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return len(f.readlines())
        except Exception:
            return 0
    
    def categorize_tools(self):
        """Categoriza todas as ferramentas"""
        for tool in self.tools:
            category = tool.get('category', 'other')
            if category in self.categories:
                self.categories[category]['tools'].append(tool)
            else:
                self.categories['other']['tools'].append(tool)
    
    def generate_statistics(self) -> Dict[str, Any]:
        """Gera estatísticas das ferramentas"""
        stats = {
            "total_tools": len(self.tools),
            "by_category": {},
            "by_type": {},
            "by_language": {},
            "total_size": 0,
            "total_lines": 0
        }
        
        # Estatísticas por categoria
        for category, cat_info in self.categories.items():
            stats["by_category"][category] = len(cat_info["tools"])
        
        # Estatísticas por tipo e linguagem
        type_counts = {}
        language_counts = {}
        
        for tool in self.tools:
            tool_type = tool.get('type', 'unknown')
            type_counts[tool_type] = type_counts.get(tool_type, 0) + 1
            
            language = tool.get('info', {}).get('language', 'unknown')
            language_counts[language] = language_counts.get(language, 0) + 1
            
            stats["total_size"] += tool.get('size', 0)
            stats["total_lines"] += tool.get('lines', 0)
        
        stats["by_type"] = type_counts
        stats["by_language"] = language_counts
        
        return stats
    
    def generate_search_index(self) -> Dict[str, Any]:
        """Gera índice de busca"""
        search_index = {
            "by_name": {},
            "by_category": {},
            "by_language": {}
        }
        
        # Indexar por nome
        for tool in self.tools:
            name = tool.get('name', '').lower()
            search_index["by_name"][name] = tool.get('name')
        
        # Indexar por categoria
        for tool in self.tools:
            category = tool.get('category', 'other')
            if category not in search_index["by_category"]:
                search_index["by_category"][category] = []
            search_index["by_category"][category].append(tool.get('name'))
        
        # Indexar por linguagem
        for tool in self.tools:
            language = tool.get('info', {}).get('language', 'unknown')
            if language not in search_index["by_language"]:
                search_index["by_language"][language] = []
            search_index["by_language"][language].append(tool.get('name'))
        
        return search_index
    
    def generate_tools_index(self) -> Dict[str, Any]:
        """Gera o índice completo das ferramentas"""
        print("Gerando índice das ferramentas...")
        
        # Escanear ferramentas
        tool_paths = self.scan_tools()
        print(f"Encontradas {len(tool_paths)} ferramentas")
        
        # Analisar cada ferramenta
        for tool_path in tool_paths:
            tool_info = self.analyze_tool(tool_path)
            if tool_info:
                self.tools.append(tool_info)
        
        # Categorizar ferramentas
        self.categorize_tools()
        
        # Gerar estatísticas
        statistics = self.generate_statistics()
        
        # Gerar índice de busca
        search_index = self.generate_search_index()
        
        # Estrutura final
        tools_index = {
            "metadata": {
                "version": "1.0",
                "last_updated": datetime.now().isoformat(),
                "total_tools": len(self.tools),
                "description": "Índice das ferramentas do OTClient"
            },
            "categories": self.categories,
            "statistics": statistics,
            "search_index": search_index
        }
        
        return tools_index
    
    def save_index(self, tools_index: Dict[str, Any], output_file: str = "wiki/maps/tools_index.json"):
        """Salva o índice em arquivo JSON"""
        try:
            # Criar diretório se não existir
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(tools_index, f, indent=2, ensure_ascii=False)
            
            print(f"Índice salvo em {output_file}")
            
        except Exception as e:
            print(f"Erro ao salvar índice: {e}")
    
    def update_index(self):
        """Atualiza o índice das ferramentas"""
        tools_index = self.generate_tools_index()
        return self.save_index(tools_index)

def main():
    """Função principal"""
    print("Iniciando indexação das ferramentas...")
    
    try:
    indexer = ToolsIndexer()
    success = indexer.update_index()
    
    if success:
            print("Indexação das ferramentas concluída com sucesso!")
    else:
            print("Erro na indexação das ferramentas!")
    
    except Exception as e:
        print(f"Erro durante indexação: {e}")

if __name__ == "__main__":
    main()
