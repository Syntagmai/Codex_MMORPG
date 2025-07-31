#!/usr/bin/env python3
"""
Script para indexação dos estilos OTUI do OTClient
Atualiza: wiki/maps/styles_index.json
"""
import os
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any

class StylesIndexer:
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.styles_path = self.project_root / "data" / "styles"
        self.styles = []
        self.categories = {
            "buttons": {"name": "Estilos de Botões", "styles": []},
            "windows": {"name": "Estilos de Janelas", "styles": []},
            "widgets": {"name": "Estilos de Widgets", "styles": []},
            "layout": {"name": "Estilos de Layout", "styles": []},
            "other": {"name": "Outros Estilos", "styles": []}
        }
        
    def scan_style_files(self) -> List[str]:
        """Escaneia todos os arquivos de estilo OTUI"""
        if not self.styles_path.exists():
            print(f"Pasta styles não encontrada: {self.styles_path}")
            return []
        
        style_files = []
        for file_path in self.styles_path.glob("*.otui"):
            style_files.append(str(file_path))
        
        return sorted(style_files)
    
    def analyze_style_file(self, file_path: str) -> Dict[str, Any]:
        """Analisa um arquivo de estilo OTUI"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            file_name = Path(file_path).name
            file_stem = Path(file_path).stem
            
            # Extrair widgets
            widgets = self.extract_widgets(content)
            
            # Extrair propriedades
            properties = self.extract_properties(content)
            
            # Extrair dependências
            dependencies = self.extract_dependencies(content)
            
            # Categorizar estilo
            category = self.categorize_style(file_name, content)
            
            style_info = {
                "name": file_stem,
                "file": file_name,
                "path": str(file_path),
                "category": category,
                "widgets": widgets,
                "properties": properties,
                "dependencies": dependencies,
                "lines": len(content.split('\n')),
                "size": len(content),
                "widgets_count": len(widgets),
                "properties_count": len(properties)
            }
            
            return style_info
            
        except Exception as e:
            print(f"Erro ao analisar arquivo {file_path}: {e}")
            return None
    
    def extract_widgets(self, content: str) -> List[Dict[str, Any]]:
        """Extrai widgets do arquivo de estilo"""
        widgets = []
        
        # Padrão para encontrar widgets
        widget_pattern = r'(\w+)\s*{([^}]+)}'
        matches = re.findall(widget_pattern, content)
        
        for widget_name, widget_content in matches:
            widget_info = {
                        "name": widget_name,
                "properties": self.extract_widget_properties(widget_content)
            }
            widgets.append(widget_info)
        
        return widgets
    
    def extract_widget_properties(self, widget_content: str) -> List[Dict[str, Any]]:
        """Extrai propriedades de um widget"""
        properties = []
        
        # Padrão para propriedades
        prop_pattern = r'(\w+)\s*:\s*([^;\n]+)'
        matches = re.findall(prop_pattern, widget_content)
        
        for prop_name, prop_value in matches:
            prop_info = {
                "name": prop_name.strip(),
                "value": prop_value.strip(),
                "type": self.guess_property_type(prop_value.strip())
            }
            properties.append(prop_info)
        
        return properties
    
    def guess_property_type(self, value: str) -> str:
        """Tenta adivinhar o tipo da propriedade"""
        value = value.strip()
        
        if value.isdigit():
            return "number"
        elif value.startswith('"') and value.endswith('"'):
            return "string"
        elif value.startswith("'") and value.endswith("'"):
            return "string"
        elif value.lower() in ['true', 'false']:
            return "boolean"
        elif value.startswith('#') or value.startswith('rgb'):
            return "color"
        elif 'px' in value or 'em' in value or '%' in value:
            return "size"
        else:
            return "unknown"
    
    def extract_properties(self, content: str) -> List[Dict[str, Any]]:
        """Extrai todas as propriedades do arquivo"""
        properties = []
        
        # Padrão para propriedades globais
        prop_pattern = r'(\w+)\s*:\s*([^;\n]+)'
        matches = re.findall(prop_pattern, content)
        
        for prop_name, prop_value in matches:
            prop_info = {
                "name": prop_name.strip(),
                "value": prop_value.strip(),
                "type": self.guess_property_type(prop_value.strip())
            }
            properties.append(prop_info)
        
        return properties
    
    def extract_dependencies(self, content: str) -> List[str]:
        """Extrai dependências do arquivo de estilo"""
        dependencies = []
        
        # Procurar por imports
        import_pattern = r'import\s+([a-zA-Z_][a-zA-Z0-9_]*)'
        imports = re.findall(import_pattern, content)
        dependencies.extend(imports)
        
        # Procurar por includes
        include_pattern = r'include\s+([a-zA-Z_][a-zA-Z0-9_]*)'
        includes = re.findall(include_pattern, content)
        dependencies.extend(includes)
        
        return list(set(dependencies))
    
    def categorize_style(self, file_name: str, content: str) -> str:
        """Categoriza um arquivo de estilo"""
        name_lower = file_name.lower()
        content_lower = content.lower()
        
        if 'button' in name_lower or 'button' in content_lower:
            return 'buttons'
        elif 'window' in name_lower or 'dialog' in name_lower:
            return 'windows'
        elif 'widget' in name_lower or 'component' in name_lower:
            return 'widgets'
        elif 'layout' in name_lower or 'grid' in name_lower or 'flex' in name_lower:
            return 'layout'
        else:
            return 'other'
    
    def categorize_styles(self):
        """Categoriza todos os estilos"""
        for style in self.styles:
            category = style.get('category', 'other')
            if category in self.categories:
                self.categories[category]['styles'].append(style)
            else:
                self.categories['other']['styles'].append(style)
    
    def generate_statistics(self) -> Dict[str, Any]:
        """Gera estatísticas dos estilos"""
        stats = {
            "total_styles": len(self.styles),
            "by_category": {},
            "total_widgets": 0,
            "total_properties": 0,
            "total_lines": 0,
            "total_size": 0
        }
        
        # Estatísticas por categoria
        for category, cat_info in self.categories.items():
            stats["by_category"][category] = len(cat_info["styles"])
        
        # Estatísticas gerais
        for style in self.styles:
            stats["total_widgets"] += style.get('widgets_count', 0)
            stats["total_properties"] += style.get('properties_count', 0)
            stats["total_lines"] += style.get('lines', 0)
            stats["total_size"] += style.get('size', 0)
        
        return stats
    
    def generate_search_index(self) -> Dict[str, Any]:
        """Gera índice de busca"""
        search_index = {
            "by_name": {},
            "by_widget": {},
            "by_property": {}
        }
        
        # Indexar por nome
        for style in self.styles:
            name = style.get('name', '').lower()
            search_index["by_name"][name] = style.get('name')
        
        # Indexar por widget
        for style in self.styles:
            for widget in style.get('widgets', []):
                widget_name = widget.get('name', '').lower()
                if widget_name not in search_index["by_widget"]:
                    search_index["by_widget"][widget_name] = []
                search_index["by_widget"][widget_name].append(style.get('name'))
        
        # Indexar por propriedade
        for style in self.styles:
            for prop in style.get('properties', []):
                prop_name = prop.get('name', '').lower()
                if prop_name not in search_index["by_property"]:
                    search_index["by_property"][prop_name] = []
                search_index["by_property"][prop_name].append(style.get('name'))
        
        return search_index
    
    def generate_styles_index(self) -> Dict[str, Any]:
        """Gera o índice completo dos estilos"""
        print("Gerando índice dos estilos...")
        
        # Escanear arquivos
        style_files = self.scan_style_files()
        print(f"Encontrados {len(style_files)} arquivos de estilo")
        
        # Analisar cada arquivo
        for file_path in style_files:
            style_info = self.analyze_style_file(file_path)
            if style_info:
                self.styles.append(style_info)
        
        # Categorizar estilos
        self.categorize_styles()
        
        # Gerar estatísticas
        statistics = self.generate_statistics()
        
        # Gerar índice de busca
        search_index = self.generate_search_index()
        
        # Estrutura final
        styles_index = {
            "metadata": {
                "version": "1.0",
                "last_updated": datetime.now().isoformat(),
                "total_styles": len(self.styles),
                "description": "Índice dos estilos OTUI do OTClient"
            },
            "categories": self.categories,
            "statistics": statistics,
            "search_index": search_index
        }
        
        return styles_index
    
    def save_index(self, styles_index: Dict[str, Any], output_file: str = "wiki/maps/styles_index.json"):
        """Salva o índice em arquivo JSON"""
        try:
            # Criar diretório se não existir
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(styles_index, f, indent=2, ensure_ascii=False)
            
            print(f"Índice salvo em {output_file}")
            
        except Exception as e:
            print(f"Erro ao salvar índice: {e}")
    
    def update_index(self):
        """Atualiza o índice dos estilos"""
        styles_index = self.generate_styles_index()
        return self.save_index(styles_index)

def main():
    """Função principal"""
    print("Iniciando indexação dos estilos...")
    
    try:
        indexer = StylesIndexer()
        success = indexer.update_index()
        
        if success:
            print("Indexação dos estilos concluída com sucesso!")
        else:
            print("Erro na indexação dos estilos!")
            
    except Exception as e:
        print(f"Erro durante indexação: {e}")

if __name__ == "__main__":
    main() 
