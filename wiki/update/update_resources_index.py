#!/usr/bin/env python3
"""
Script para indexação dos recursos do OTClient
Atualiza: wiki/maps/resources_index.json
"""
import os
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any

class ResourcesIndexer:
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.data_path = self.project_root / "data"
        self.resources = []
        self.categories = {
            "images": {"name": "Imagens", "resources": []},
            "sounds": {"name": "Sons", "resources": []},
            "fonts": {"name": "Fontes", "resources": []},
            "locales": {"name": "Localização", "resources": []},
            "particles": {"name": "Partículas", "resources": []},
            "other": {"name": "Outros Recursos", "resources": []}
        }
        
    def scan_resources(self) -> List[str]:
        """Escaneia todos os recursos"""
        if not self.data_path.exists():
            print(f"Pasta data não encontrada: {self.data_path}")
            return []
        
        resources = []
        
        # Escanear diferentes tipos de recursos
        resource_paths = [
            ("images", ["*.png", "*.jpg", "*.jpeg", "*.gif", "*.bmp"]),
            ("sounds", ["*.ogg", "*.wav", "*.mp3"]),
            ("fonts", ["*.otfont", "*.ttf", "*.otf"]),
            ("locales", ["*.lua"]),
            ("particles", ["*.otps", "*.png"]),
            ("cursors", ["*.png", "*.otml"]),
            ("things", ["*.xml", "*.otml"])
        ]
        
        for category, extensions in resource_paths:
            category_path = self.data_path / category
            if category_path.exists():
                for ext in extensions:
                    for file_path in category_path.rglob(ext):
                        resources.append(str(file_path))
        
        return sorted(resources)
    
    def analyze_resource(self, resource_path: str) -> Dict[str, Any]:
        """Analisa um recurso"""
        try:
            file_path = Path(resource_path)
            file_name = file_path.name
            file_stem = file_path.stem
            file_ext = file_path.suffix.lower()
            
            # Determinar categoria
            category = self.categorize_resource(file_path)
            
            # Extrair metadados
            metadata = self.extract_metadata(file_path)
            
            # Obter estatísticas do arquivo
            stat = file_path.stat()
            
            resource_info = {
                "name": file_stem,
                "file": file_name,
                "path": str(resource_path),
                "category": category,
                "extension": file_ext,
                "size": stat.st_size,
                "lines": self.count_lines(file_path),
                "last_modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                "metadata": metadata
            }
            
            return resource_info
            
        except Exception as e:
            print(f"Erro ao analisar recurso {resource_path}: {e}")
            return None
    
    def categorize_resource(self, file_path: Path) -> str:
        """Categoriza um recurso"""
        file_ext = file_path.suffix.lower()
        parent_dir = file_path.parent.name.lower()
        
        # Categorizar por extensão
        if file_ext in ['.png', '.jpg', '.jpeg', '.gif', '.bmp']:
            return 'images'
        elif file_ext in ['.ogg', '.wav', '.mp3']:
            return 'sounds'
        elif file_ext in ['.otfont', '.ttf', '.otf']:
            return 'fonts'
        elif file_ext == '.lua' and parent_dir == 'locales':
            return 'locales'
        elif file_ext in ['.otps'] or (file_ext == '.png' and parent_dir == 'particles'):
            return 'particles'
        else:
            return 'other'
    
    def extract_metadata(self, file_path: Path) -> Dict[str, Any]:
        """Extrai metadados do arquivo"""
        metadata = {}
        file_ext = file_path.suffix.lower()
        
        try:
            if file_ext == '.otfont':
                metadata = self.extract_font_metadata(file_path)
            elif file_ext == '.lua' and file_path.parent.name == 'locales':
                metadata = self.extract_locale_metadata(file_path)
            elif file_ext == '.otps':
                metadata = self.extract_particle_metadata(file_path)
            elif file_ext in ['.png', '.jpg', '.jpeg', '.gif', '.bmp']:
                metadata = {
                    "type": "image",
                    "format": file_ext[1:].upper()
                }
        except Exception:
            pass
        
        return metadata
    
    def extract_font_metadata(self, file_path: Path) -> Dict[str, Any]:
        """Extrai metadados de fonte"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Tentar extrair informações da fonte
            metadata = {
                "type": "font",
                "format": "OTFont"
            }
            
            # Procurar por informações específicas
            if 'font' in content.lower():
                metadata["has_font_info"] = True
            
            return metadata
            
        except Exception:
            return {"type": "font", "format": "OTFont"}
    
    def extract_locale_metadata(self, file_path: Path) -> Dict[str, Any]:
        """Extrai metadados de localização"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Tentar identificar o idioma
            language = file_path.stem
            
            metadata = {
                "type": "locale",
                "language": language,
                "translations_count": len(re.findall(r'\["([^"]+)"\]', content))
            }
            
            return metadata
            
        except Exception:
            return {"type": "locale", "language": "unknown"}
    
    def extract_particle_metadata(self, file_path: Path) -> Dict[str, Any]:
        """Extrai metadados de partículas"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            metadata = {
                "type": "particle",
                "format": "OTPS",
                "particles_count": len(re.findall(r'particle\s*{', content))
            }
            
            return metadata
            
        except Exception:
            return {"type": "particle", "format": "OTPS"}
    
    def count_lines(self, file_path: Path) -> int:
        """Conta linhas de um arquivo"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return len(f.readlines())
        except Exception:
            return 0
    
    def categorize_resources(self):
        """Categoriza todos os recursos"""
        for resource in self.resources:
            category = resource.get('category', 'other')
            if category in self.categories:
                self.categories[category]['resources'].append(resource)
            else:
                self.categories['other']['resources'].append(resource)
    
    def generate_statistics(self) -> Dict[str, Any]:
        """Gera estatísticas dos recursos"""
        stats = {
            "total_resources": len(self.resources),
            "by_category": {},
            "by_extension": {},
            "total_size": 0,
            "total_lines": 0
        }
        
        # Estatísticas por categoria
        for category, cat_info in self.categories.items():
            stats["by_category"][category] = len(cat_info["resources"])
        
        # Estatísticas por extensão
        ext_counts = {}
        for resource in self.resources:
            ext = resource.get('extension', 'unknown')
            ext_counts[ext] = ext_counts.get(ext, 0) + 1
            stats["total_size"] += resource.get('size', 0)
            stats["total_lines"] += resource.get('lines', 0)
        
        stats["by_extension"] = ext_counts
        
        return stats
    
    def generate_search_index(self) -> Dict[str, Any]:
        """Gera índice de busca"""
        search_index = {
            "by_name": {},
            "by_category": {},
            "by_extension": {}
        }
        
        # Indexar por nome
        for resource in self.resources:
            name = resource.get('name', '').lower()
            search_index["by_name"][name] = resource.get('name')
        
        # Indexar por categoria
        for resource in self.resources:
            category = resource.get('category', 'other')
            if category not in search_index["by_category"]:
                search_index["by_category"][category] = []
            search_index["by_category"][category].append(resource.get('name'))
        
        # Indexar por extensão
        for resource in self.resources:
            ext = resource.get('extension', 'unknown')
            if ext not in search_index["by_extension"]:
                search_index["by_extension"][ext] = []
            search_index["by_extension"][ext].append(resource.get('name'))
        
        return search_index
    
    def generate_resources_index(self) -> Dict[str, Any]:
        """Gera o índice completo dos recursos"""
        print("Gerando índice dos recursos...")
        
        # Escanear recursos
        resource_files = self.scan_resources()
        print(f"Encontrados {len(resource_files)} recursos")
        
        # Analisar cada recurso
        for resource_path in resource_files:
            resource_info = self.analyze_resource(resource_path)
            if resource_info:
                self.resources.append(resource_info)
        
        # Categorizar recursos
        self.categorize_resources()
        
        # Gerar estatísticas
        statistics = self.generate_statistics()
        
        # Gerar índice de busca
        search_index = self.generate_search_index()
        
        # Estrutura final
        resources_index = {
            "metadata": {
                "version": "1.0",
                "last_updated": datetime.now().isoformat(),
                "total_resources": len(self.resources),
                "description": "Índice dos recursos do OTClient"
            },
            "categories": self.categories,
            "statistics": statistics,
            "search_index": search_index
        }
        
        return resources_index
    
    def save_index(self, resources_index: Dict[str, Any], output_file: str = "wiki/maps/resources_index.json"):
        """Salva o índice em arquivo JSON"""
        try:
            # Criar diretório se não existir
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(resources_index, f, indent=2, ensure_ascii=False)
            
            print(f"Índice salvo em {output_file}")
            
        except Exception as e:
            print(f"Erro ao salvar índice: {e}")
    
    def update_index(self):
        """Atualiza o índice dos recursos"""
        resources_index = self.generate_resources_index()
        return self.save_index(resources_index)

def main():
    """Função principal"""
    print("Iniciando indexação dos recursos...")
    
    try:
        indexer = ResourcesIndexer()
        success = indexer.update_index()
        
        if success:
            print("Indexação dos recursos concluída com sucesso!")
        else:
            print("Erro na indexação dos recursos!")
            
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
- **Nome**: update_resources_index
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

