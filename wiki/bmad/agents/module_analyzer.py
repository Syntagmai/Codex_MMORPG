#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🤖 Module Analyzer Agent
Responsável por analisar módulos OTClient existentes e extrair padrões
"""

import os
import json
import re
import ast
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

class ModuleAnalyzerAgent:
    """Agente especializado em análise de módulos OTClient"""
    
    def __init__(self, workspace_path: str = None):
        self.workspace_path = workspace_path or os.getcwd()
        # Ajustar caminho para encontrar módulos na raiz do projeto
        if os.path.basename(self.workspace_path) == "bmad":
            # Se estamos na pasta bmad, subir um nível
            self.workspace_path = os.path.dirname(self.workspace_path)
        if os.path.basename(self.workspace_path) == "wiki":
            # Se estamos na pasta wiki, subir um nível
            self.workspace_path = os.path.dirname(self.workspace_path)
        
        self.modules_path = os.path.join(self.workspace_path, "modules")
        self.wiki_path = os.path.join(self.workspace_path, "wiki")
        self.results_path = os.path.join(self.workspace_path, "wiki/bmad/results")
        
        # Criar diretórios se não existirem
        os.makedirs(self.results_path, exist_ok=True)
        os.makedirs(os.path.join(self.results_path, "analysis"), exist_ok=True)
        
        # Carregar mapas de navegação
        self.load_navigation_maps()
        
    def load_navigation_maps(self):
        """Carrega mapas de navegação da wiki"""
        maps_path = os.path.join(self.wiki_path, "maps")
        
        try:
            # Carregar tags_index.json
            tags_file = os.path.join(maps_path, "tags_index.json")
            if os.path.exists(tags_file):
                with open(tags_file, 'r', encoding='utf-8') as f:
                    self.tags_index = json.load(f)
            else:
                self.tags_index = {}
                
            # Carregar wiki_map.json
            wiki_map_file = os.path.join(maps_path, "wiki_map.json")
            if os.path.exists(wiki_map_file):
                with open(wiki_map_file, 'r', encoding='utf-8') as f:
                    self.wiki_map = json.load(f)
            else:
                self.wiki_map = {}
                
        except Exception as e:
            print(f"⚠️ Erro ao carregar mapas de navegação: {e}")
            self.tags_index = {}
            self.wiki_map = {}
    
    def analyze_module(self, module_name: str) -> Dict[str, Any]:
        """
        Analisa um módulo OTClient específico
        
        Args:
            module_name: Nome do módulo (ex: 'client', 'game_inventory')
            
        Returns:
            Dicionário com análise completa do módulo
        """
        print(f"🔍 Analisando módulo: {module_name}")
        
        module_path = os.path.join(self.modules_path, module_name)
        if not os.path.exists(module_path):
            raise FileNotFoundError(f"Módulo '{module_name}' não encontrado")
        
        analysis = {
            "module_name": module_name,
            "analysis_date": datetime.now().isoformat(),
            "module_path": module_path,
            "files": {},
            "structure": {},
            "patterns": {},
            "dependencies": {},
            "documentation": {},
            "metrics": {}
        }
        
        # Analisar arquivos do módulo
        analysis["files"] = self.analyze_module_files(module_path)
        
        # Analisar estrutura
        analysis["structure"] = self.analyze_module_structure(analysis["files"])
        
        # Extrair padrões
        analysis["patterns"] = self.extract_patterns(analysis["files"])
        
        # Identificar dependências
        analysis["dependencies"] = self.identify_dependencies(analysis["files"])
        
        # Gerar documentação
        analysis["documentation"] = self.generate_documentation(analysis)
        
        # Calcular métricas
        analysis["metrics"] = self.calculate_metrics(analysis)
        
        # Salvar análise
        self.save_analysis(module_name, analysis)
        
        return analysis
    
    def analyze_module_files(self, module_path: str) -> Dict[str, Any]:
        """Analisa todos os arquivos de um módulo"""
        files_analysis = {}
        
        for file_path in Path(module_path).rglob("*"):
            if file_path.is_file():
                relative_path = str(file_path.relative_to(module_path))
                file_analysis = self.analyze_file(file_path)
                files_analysis[relative_path] = file_analysis
        
        return files_analysis
    
    def analyze_module_structure(self, files_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Analisa estrutura geral do módulo"""
        structure = {
            "total_files": len(files_analysis),
            "file_types": {},
            "main_files": [],
            "dependencies": {},
            "complexity": 0
        }
        
        # Contar tipos de arquivo
        for file_path, file_analysis in files_analysis.items():
            file_type = file_analysis.get("file_type", "unknown")
            structure["file_types"][file_type] = structure["file_types"].get(file_type, 0) + 1
            
            # Identificar arquivos principais
            if file_type in [".lua", ".otmod"]:
                structure["main_files"].append(file_path)
            
            # Acumular complexidade
            file_structure = file_analysis.get("structure", {})
            structure["complexity"] += file_structure.get("complexity", 0)
        
        return structure
    
    def analyze_file(self, file_path: Path) -> Dict[str, Any]:
        """Analisa um arquivo específico"""
        file_analysis = {
            "file_type": file_path.suffix,
            "size": file_path.stat().st_size,
            "lines": 0,
            "content": "",
            "structure": {},
            "patterns": {}
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                file_analysis["content"] = content
                file_analysis["lines"] = len(content.splitlines())
            
            # Análise específica por tipo de arquivo
            if file_path.suffix == '.lua':
                file_analysis["structure"] = self.analyze_lua_file(content)
                file_analysis["patterns"] = self.extract_lua_patterns(content)
            elif file_path.suffix == '.otmod':
                file_analysis["structure"] = self.analyze_otmod_file(content)
                file_analysis["patterns"] = self.extract_otmod_patterns(content)
            elif file_path.suffix == '.otui':
                file_analysis["structure"] = self.analyze_otui_file(content)
                file_analysis["patterns"] = self.extract_otui_patterns(content)
                
        except Exception as e:
            file_analysis["error"] = str(e)
        
        return file_analysis
    
    def analyze_lua_file(self, content: str) -> Dict[str, Any]:
        """Analisa estrutura de arquivo Lua"""
        structure = {
            "functions": [],
            "variables": [],
            "imports": [],
            "comments": [],
            "complexity": 0
        }
        
        lines = content.splitlines()
        
        for i, line in enumerate(lines, 1):
            line = line.strip()
            
            # Detectar funções
            if re.match(r'^function\s+\w+', line):
                func_match = re.match(r'^function\s+(\w+)', line)
                if func_match:
                    structure["functions"].append({
                        "name": func_match.group(1),
                        "line": i,
                        "definition": line
                    })
            
            # Detectar variáveis locais
            elif re.match(r'^local\s+\w+', line):
                var_match = re.match(r'^local\s+(\w+)', line)
                if var_match:
                    structure["variables"].append({
                        "name": var_match.group(1),
                        "line": i,
                        "definition": line
                    })
            
            # Detectar imports
            elif re.match(r'^require\s*\(', line):
                structure["imports"].append({
                    "line": i,
                    "definition": line
                })
            
            # Detectar comentários
            elif line.startswith('--'):
                structure["comments"].append({
                    "line": i,
                    "content": line
                })
        
        # Calcular complexidade (número de funções + variáveis)
        structure["complexity"] = len(structure["functions"]) + len(structure["variables"])
        
        return structure
    
    def analyze_otmod_file(self, content: str) -> Dict[str, Any]:
        """Analisa estrutura de arquivo .otmod"""
        structure = {
            "module_info": {},
            "scripts": [],
            "load_later": [],
            "events": []
        }
        
        lines = content.splitlines()
        current_section = None
        
        for line in lines:
            line = line.strip()
            
            if not line or line.startswith('#'):
                continue
            
            # Detectar seções
            if line == 'Module':
                current_section = 'module_info'
            elif line == 'load-later:':
                current_section = 'load_later'
            elif line.startswith('scripts:'):
                current_section = 'scripts'
            elif line.startswith('@'):
                # Eventos
                event_match = re.match(r'@(\w+):\s*(.+)', line)
                if event_match:
                    structure["events"].append({
                        "event": event_match.group(1),
                        "action": event_match.group(2)
                    })
            elif current_section == 'module_info':
                # Informações do módulo
                if ':' in line:
                    key, value = line.split(':', 1)
                    structure["module_info"][key.strip()] = value.strip()
            elif current_section == 'scripts':
                # Scripts
                if line.startswith('-'):
                    script = line[1:].strip()
                    structure["scripts"].append(script)
            elif current_section == 'load_later':
                # Módulos carregados depois
                if line.startswith('-'):
                    module = line[1:].strip()
                    structure["load_later"].append(module)
        
        return structure
    
    def analyze_otui_file(self, content: str) -> Dict[str, Any]:
        """Analisa estrutura de arquivo .otui"""
        structure = {
            "widgets": [],
            "properties": [],
            "events": []
        }
        
        lines = content.splitlines()
        
        for line in lines:
            line = line.strip()
            
            if not line or line.startswith('#'):
                continue
            
            # Detectar widgets
            if re.match(r'^\w+\s+\w+', line) and ':' not in line:
                widget_match = re.match(r'^(\w+)\s+(\w+)', line)
                if widget_match:
                    structure["widgets"].append({
                        "type": widget_match.group(1),
                        "name": widget_match.group(2)
                    })
            
            # Detectar propriedades
            elif ':' in line and not line.startswith('@'):
                prop_match = re.match(r'(\w+):\s*(.+)', line)
                if prop_match:
                    structure["properties"].append({
                        "name": prop_match.group(1),
                        "value": prop_match.group(2)
                    })
            
            # Detectar eventos
            elif line.startswith('@'):
                event_match = re.match(r'@(\w+):\s*(.+)', line)
                if event_match:
                    structure["events"].append({
                        "event": event_match.group(1),
                        "action": event_match.group(2)
                    })
        
        return structure
    
    def extract_patterns(self, files_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Extrai padrões dos arquivos analisados"""
        patterns = {
            "lua_patterns": {},
            "otmod_patterns": {},
            "otui_patterns": {},
            "common_patterns": {}
        }
        
        # Padrões Lua
        lua_files = {k: v for k, v in files_analysis.items() if k.endswith('.lua')}
        if lua_files:
            patterns["lua_patterns"] = self.extract_lua_patterns_from_files(lua_files)
        
        # Padrões OTMod
        otmod_files = {k: v for k, v in files_analysis.items() if k.endswith('.otmod')}
        if otmod_files:
            patterns["otmod_patterns"] = self.extract_otmod_patterns_from_files(otmod_files)
        
        # Padrões OTUI
        otui_files = {k: v for k, v in files_analysis.items() if k.endswith('.otui')}
        if otui_files:
            patterns["otui_patterns"] = self.extract_otui_patterns_from_files(otui_files)
        
        # Padrões comuns
        patterns["common_patterns"] = self.extract_common_patterns(files_analysis)
        
        return patterns
    
    def extract_lua_patterns_from_files(self, lua_files: Dict[str, Any]) -> Dict[str, Any]:
        """Extrai padrões específicos de arquivos Lua"""
        patterns = {
            "function_patterns": [],
            "variable_patterns": [],
            "import_patterns": [],
            "api_usage": []
        }
        
        for file_path, file_analysis in lua_files.items():
            content = file_analysis.get("content", "")
            
            # Padrões de funções
            function_matches = re.findall(r'function\s+(\w+)', content)
            patterns["function_patterns"].extend(function_matches)
            
            # Padrões de variáveis
            variable_matches = re.findall(r'local\s+(\w+)', content)
            patterns["variable_patterns"].extend(variable_matches)
            
            # Padrões de import
            import_matches = re.findall(r'require\s*\([\'"]([^\'"]+)[\'"]\)', content)
            patterns["import_patterns"].extend(import_matches)
            
            # Uso de APIs OTClient
            api_patterns = [
                r'g_game\.(\w+)',
                r'g_ui\.(\w+)',
                r'g_sounds\.(\w+)',
                r'g_graphics\.(\w+)',
                r'connect\s*\((\w+)',
                r'disconnect\s*\((\w+)'
            ]
            
            for pattern in api_patterns:
                matches = re.findall(pattern, content)
                patterns["api_usage"].extend(matches)
        
        return patterns
    
    def extract_otmod_patterns_from_files(self, otmod_files: Dict[str, Any]) -> Dict[str, Any]:
        """Extrai padrões específicos de arquivos OTMod"""
        patterns = {
            "module_properties": [],
            "script_patterns": [],
            "load_later_patterns": [],
            "event_patterns": []
        }
        
        for file_path, file_analysis in otmod_files.items():
            content = file_analysis.get("content", "")
            
            # Propriedades de módulo
            prop_matches = re.findall(r'(\w+):\s*(.+)', content)
            patterns["module_properties"].extend(prop_matches)
            
            # Scripts
            script_matches = re.findall(r'-\s*(\w+)', content)
            patterns["script_patterns"].extend(script_matches)
            
            # Eventos
            event_matches = re.findall(r'@(\w+):', content)
            patterns["event_patterns"].extend(event_matches)
        
        return patterns
    
    def extract_otui_patterns_from_files(self, otui_files: Dict[str, Any]) -> Dict[str, Any]:
        """Extrai padrões específicos de arquivos OTUI"""
        patterns = {
            "widget_types": [],
            "property_patterns": [],
            "event_patterns": []
        }
        
        for file_path, file_analysis in otui_files.items():
            content = file_analysis.get("content", "")
            
            # Tipos de widgets
            widget_matches = re.findall(r'^(\w+)\s+\w+', content, re.MULTILINE)
            patterns["widget_types"].extend(widget_matches)
            
            # Propriedades
            prop_matches = re.findall(r'(\w+):\s*(.+)', content)
            patterns["property_patterns"].extend(prop_matches)
            
            # Eventos
            event_matches = re.findall(r'@(\w+):', content)
            patterns["event_patterns"].extend(event_matches)
        
        return patterns
    
    def extract_common_patterns(self, files_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Extrai padrões comuns entre todos os arquivos"""
        patterns = {
            "file_structure": {},
            "naming_conventions": {},
            "code_style": {}
        }
        
        # Estrutura de arquivos
        file_types = {}
        for file_path in files_analysis.keys():
            ext = Path(file_path).suffix
            file_types[ext] = file_types.get(ext, 0) + 1
        
        patterns["file_structure"] = file_types
        
        # Convenções de nomenclatura
        naming_patterns = {
            "snake_case": 0,
            "camelCase": 0,
            "PascalCase": 0
        }
        
        for file_path, file_analysis in files_analysis.items():
            content = file_analysis.get("content", "")
            
            # Contar padrões de nomenclatura
            snake_case = len(re.findall(r'\b[a-z_][a-z0-9_]*\b', content))
            camel_case = len(re.findall(r'\b[a-z][a-zA-Z0-9]*\b', content))
            pascal_case = len(re.findall(r'\b[A-Z][a-zA-Z0-9]*\b', content))
            
            naming_patterns["snake_case"] += snake_case
            naming_patterns["camelCase"] += camel_case
            naming_patterns["PascalCase"] += pascal_case
        
        patterns["naming_conventions"] = naming_patterns
        
        return patterns
    
    def identify_dependencies(self, files_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Identifica dependências do módulo"""
        dependencies = {
            "internal_deps": [],
            "external_deps": [],
            "api_deps": [],
            "module_deps": []
        }
        
        for file_path, file_analysis in files_analysis.items():
            if file_path.endswith('.lua'):
                content = file_analysis.get("content", "")
                
                # Dependências internas (outros arquivos do módulo)
                internal_matches = re.findall(r'require\s*\([\'"]([^\'"]+)[\'"]\)', content)
                dependencies["internal_deps"].extend(internal_matches)
                
                # Dependências de APIs OTClient
                api_matches = re.findall(r'g_(\w+)\.', content)
                dependencies["api_deps"].extend(api_matches)
                
            elif file_path.endswith('.otmod'):
                content = file_analysis.get("content", "")
                
                # Dependências de módulos
                module_matches = re.findall(r'-\s*(\w+)', content)
                dependencies["module_deps"].extend(module_matches)
        
        # Remover duplicatas
        for key in dependencies:
            dependencies[key] = list(set(dependencies[key]))
        
        return dependencies
    
    def generate_documentation(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Gera documentação técnica do módulo"""
        documentation = {
            "overview": "",
            "structure_summary": "",
            "api_reference": "",
            "usage_examples": "",
            "patterns_documentation": ""
        }
        
        module_name = analysis["module_name"]
        structure = analysis["structure"]
        patterns = analysis["patterns"]
        dependencies = analysis["dependencies"]
        
        # Visão geral
        documentation["overview"] = f"""
# Módulo {module_name}

## Descrição
Este módulo implementa funcionalidades relacionadas a {module_name}.

## Arquivos
- Total de arquivos: {len(analysis['files'])}
- Tipos de arquivo: {', '.join(set(Path(f).suffix for f in analysis['files'].keys()))}

## Dependências
- APIs OTClient: {', '.join(dependencies['api_deps'])}
- Módulos: {', '.join(dependencies['module_deps'])}
"""
        
        # Resumo da estrutura
        documentation["structure_summary"] = f"""
## Estrutura

### Arquivos Lua
- Funções encontradas: {len(patterns.get('lua_patterns', {}).get('function_patterns', []))}
- Variáveis locais: {len(patterns.get('lua_patterns', {}).get('variable_patterns', []))}
- Imports: {len(patterns.get('lua_patterns', {}).get('import_patterns', []))}

### APIs Utilizadas
{chr(10).join(f"- {api}" for api in dependencies['api_deps'])}
"""
        
        return documentation
    
    def calculate_metrics(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Calcula métricas de qualidade da análise"""
        metrics = {
            "coverage": 0,
            "complexity": 0,
            "documentation_quality": 0,
            "pattern_diversity": 0
        }
        
        files = analysis["files"]
        patterns = analysis["patterns"]
        
        # Cobertura (número de arquivos analisados)
        metrics["coverage"] = len(files)
        
        # Complexidade (soma da complexidade de todos os arquivos)
        total_complexity = 0
        for file_analysis in files.values():
            structure = file_analysis.get("structure", {})
            total_complexity += structure.get("complexity", 0)
        metrics["complexity"] = total_complexity
        
        # Qualidade da documentação (baseada em comentários)
        total_comments = 0
        total_lines = 0
        for file_analysis in files.values():
            structure = file_analysis.get("structure", {})
            total_comments += len(structure.get("comments", []))
            total_lines += file_analysis.get("lines", 0)
        
        if total_lines > 0:
            metrics["documentation_quality"] = (total_comments / total_lines) * 100
        
        # Diversidade de padrões
        pattern_count = 0
        for pattern_type in patterns.values():
            if isinstance(pattern_type, dict):
                pattern_count += len(pattern_type)
            elif isinstance(pattern_type, list):
                pattern_count += len(pattern_type)
        metrics["pattern_diversity"] = pattern_count
        
        return metrics
    
    def save_analysis(self, module_name: str, analysis: Dict[str, Any]):
        """Salva análise em arquivo JSON"""
        output_file = os.path.join(self.results_path, "analysis", f"{module_name}_analysis.json")
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(analysis, f, indent=2, ensure_ascii=False)
            print(f"✅ Análise salva em: {output_file}")
        except Exception as e:
            print(f"⚠️ Erro ao salvar análise: {e}")
    
    def get_available_modules(self) -> List[str]:
        """Retorna lista de módulos disponíveis para análise"""
        if not os.path.exists(self.modules_path):
            return []
        
        modules = []
        for item in os.listdir(self.modules_path):
            item_path = os.path.join(self.modules_path, item)
            if os.path.isdir(item_path) and not item.startswith('.'):
                modules.append(item)
        
        return sorted(modules)

def main():
    """Função principal para teste do agente"""
    analyzer = ModuleAnalyzerAgent()
    
    # Listar módulos disponíveis
    modules = analyzer.get_available_modules()
    print(f"📋 Módulos disponíveis: {len(modules)}")
    
    # Analisar módulo de exemplo
    if modules:
        example_module = modules[0]  # Primeiro módulo
        print(f"🔍 Analisando módulo de exemplo: {example_module}")
        
        try:
            analysis = analyzer.analyze_module(example_module)
            print(f"✅ Análise concluída para {example_module}")
            print(f"📊 Métricas: {analysis['metrics']}")
        except Exception as e:
            print(f"❌ Erro na análise: {e}")

if __name__ == "__main__":
    main() 