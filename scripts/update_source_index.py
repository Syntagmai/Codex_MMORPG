#!/usr/bin/env python3
"""
Script para indexação automática do código-fonte do OTClient e Canary (submódulos)
Gera otclient_source_index.json com informações sobre arquivos C++ e Lua
Adaptado para estrutura com submódulos otclient/ e canary/
"""
import os
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any

class SourceIndexer:
    def __init__(self):
        self.project_root = Path(".")
        self.source_files = []
        self.categories = {
            "core": {"name": "Sistema Core", "files": []},
            "ui": {"name": "Interface do Usuário", "files": []},
            "game": {"name": "Sistema de Jogo", "files": []},
            "network": {"name": "Rede e Comunicação", "files": []},
            "resource": {"name": "Recursos e Assets", "files": []},
            "module": {"name": "Módulos Lua", "files": []},
            "other": {"name": "Outros", "files": []}
        }

    def scan_source_files(self) -> List[str]:
        """Escaneia arquivos de código-fonte nos submódulos"""
        source_extensions = {'.cpp', '.h', '.lua'}
        source_files = []
        
        # Escanear otclient/src/ (C++ OTClient)
        otclient_src_dir = self.project_root / "otclient" / "src"
        if otclient_src_dir.exists():
            for file_path in otclient_src_dir.rglob("*"):
                if file_path.is_file() and file_path.suffix in source_extensions:
                    source_files.append(str(file_path))
        
        # Escanear otclient/modules/ (Lua OTClient)
        otclient_modules_dir = self.project_root / "otclient" / "modules"
        if otclient_modules_dir.exists():
            for file_path in otclient_modules_dir.rglob("*.lua"):
                if file_path.is_file():
                    source_files.append(str(file_path))
        
        # Escanear canary/src/ (C++ Canary)
        canary_src_dir = self.project_root / "canary" / "src"
        if canary_src_dir.exists():
            for file_path in canary_src_dir.rglob("*"):
                if file_path.is_file() and file_path.suffix in source_extensions:
                    source_files.append(str(file_path))
        
        # Escanear canary/modules/ (Lua Canary)
        canary_modules_dir = self.project_root / "canary" / "modules"
        if canary_modules_dir.exists():
            for file_path in canary_modules_dir.rglob("*.lua"):
                if file_path.is_file():
                    source_files.append(str(file_path))
        
        self.source_files = sorted(source_files)
        return source_files

    def categorize_file(self, file_path: str) -> str:
        """Categoriza um arquivo baseado em seu caminho e conteúdo"""
        path_lower = file_path.lower()
        
        # Categorização para OTClient
        if "otclient/src/client" in path_lower:
            return "ui"
        elif "otclient/src/game" in path_lower or "otclient/modules/game" in path_lower:
            return "game"
        elif "otclient/src/network" in path_lower or "protocol" in path_lower:
            return "network"
        elif "otclient/src/resource" in path_lower or "otclient/data" in path_lower:
            return "resource"
        elif "otclient/modules" in path_lower:
            return "module"
        elif "otclient/src/core" in path_lower or "otclient/src/framework" in path_lower:
            return "core"
        
        # Categorização para Canary
        elif "canary/src/client" in path_lower:
            return "ui"
        elif "canary/src/game" in path_lower or "canary/modules/game" in path_lower:
            return "game"
        elif "canary/src/network" in path_lower or "canary/protocol" in path_lower:
            return "network"
        elif "canary/src/resource" in path_lower or "canary/data" in path_lower:
            return "resource"
        elif "canary/modules" in path_lower:
            return "module"
        elif "canary/src/core" in path_lower or "canary/src/framework" in path_lower:
            return "core"
        else:
            return "other"

    def extract_functions(self, file_path: str) -> List[str]:
        """Extrai funções de um arquivo"""
        functions = []
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            if file_path.endswith('.lua'):
                # Extrair funções Lua
                lua_functions = re.findall(r'function\s+([a-zA-Z_][a-zA-Z0-9_:]*)', content)
                functions.extend(lua_functions)
            else:
                # Extrair funções C++
                cpp_functions = re.findall(r'(\w+)\s+\w+\s*\([^)]*\)\s*{', content)
                functions.extend(cpp_functions)
                
        except Exception:
            pass
        
        return functions

    def extract_classes(self, file_path: str) -> List[str]:
        """Extrai classes de um arquivo"""
        classes = []
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            if not file_path.endswith('.lua'):
                # Extrair classes C++
                cpp_classes = re.findall(r'class\s+([a-zA-Z_][a-zA-Z0-9_]*)', content)
                classes.extend(cpp_classes)
                
        except Exception:
            pass
        
        return classes

    def generate_source_index(self) -> Dict[str, Any]:
        """Gera o índice completo do código-fonte"""
        print("Iniciando indexação do código-fonte...")
        
        # Escanear arquivos
        source_files = self.scan_source_files()
        print(f"Encontrados {len(source_files)} arquivos de código-fonte")
        
        # Processar cada arquivo
        for file_path in source_files:
            category = self.categorize_file(file_path)
            functions = self.extract_functions(file_path)
            classes = self.extract_classes(file_path)
            
            file_info = {
                "path": file_path,
                "name": Path(file_path).name,
                "extension": Path(file_path).suffix,
                "functions": functions,
                "classes": classes,
                "lines": len(open(file_path, 'r', encoding='utf-8', errors='ignore').readlines())
            }
            
            self.categories[category]["files"].append(file_info)
        
        # Gerar estatísticas
        statistics = self.generate_statistics()
        
        # Gerar índice de busca
        search_index = self.generate_search_index()
        
        # Estrutura final
        source_index = {
            "metadata": {
                "version": "1.0",
                "last_updated": datetime.now().isoformat(),
                "total_files": len(source_files),
                "description": "Índice do código-fonte do OTClient"
            },
            "categories": self.categories,
            "statistics": statistics,
            "search_index": search_index
        }
        
        return source_index
    
    def generate_statistics(self) -> Dict[str, Any]:
        """Gera estatísticas do código-fonte"""
        stats = {
            "by_category": {},
            "by_extension": {},
            "total_functions": 0,
            "total_classes": 0,
            "total_lines": 0
        }
        
        # Estatísticas por categoria
        for category, cat_info in self.categories.items():
            stats["by_category"][category] = len(cat_info["files"])
            
            # Contar funções e classes
            for file_info in cat_info["files"]:
                stats["total_functions"] += len(file_info["functions"])
                stats["total_classes"] += len(file_info["classes"])
                stats["total_lines"] += file_info["lines"]
                
                # Estatísticas por extensão
                ext = file_info["extension"]
                if ext not in stats["by_extension"]:
                    stats["by_extension"][ext] = 0
                stats["by_extension"][ext] += 1
        
        return stats
    
    def generate_search_index(self) -> Dict[str, List[str]]:
        """Gera índice de busca"""
        search_index = {
            "functions": {},
            "classes": {},
            "files": {}
        }
        
        # Indexar funções
        for category, cat_info in self.categories.items():
            for file_info in cat_info["files"]:
                for function in file_info["functions"]:
                    if function not in search_index["functions"]:
                        search_index["functions"][function] = []
                    search_index["functions"][function].append(file_info["path"])
                
                for class_name in file_info["classes"]:
                    if class_name not in search_index["classes"]:
                        search_index["classes"][class_name] = []
                    search_index["classes"][class_name].append(file_info["path"])
                
                # Indexar arquivo
                file_name = file_info["name"]
                if file_name not in search_index["files"]:
                    search_index["files"][file_name] = []
                search_index["files"][file_name].append(file_info["path"])
        
        return search_index
    
    def save_index(self, source_index: Dict[str, Any], output_file: str = "wiki/maps/otclient_source_index.json"):
        """Salva o índice em arquivo JSON"""
        try:
            # Criar diretório se não existir
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(source_index, f, indent=2, ensure_ascii=False)
            
            print(f"Índice salvo em {output_file}")
            
        except Exception as e:
            print(f"Erro ao salvar índice: {e}")

def main():
    """Função principal"""
    indexer = SourceIndexer()
    
    try:
        # Gerar índice
        source_index = indexer.generate_source_index()
        
        # Salvar índice
        indexer.save_index(source_index)
        
        print("Indexação do código-fonte concluída!")
            
    except Exception as e:
        print(f"Erro durante indexação: {e}")

if __name__ == "__main__":
    main() 

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
- **Nome**: update_source_index
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

