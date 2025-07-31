#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎨 Module Generator Agent
Responsável por criar variações funcionais de módulos OTClient
"""

import os
import json
import re
import random
import string
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
from copy import deepcopy

class ModuleGeneratorAgent:
    """Agente especializado em geração de módulos OTClient"""
    
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
        self.templates_path = os.path.join(self.workspace_path, "wiki/bmad/templates")
        
        # Criar diretórios se não existirem
        os.makedirs(self.results_path, exist_ok=True)
        os.makedirs(os.path.join(self.results_path, "generated_modules"), exist_ok=True)
        os.makedirs(self.templates_path, exist_ok=True)
        
        # Carregar conhecimento da wiki
        self.load_wiki_knowledge()
        
        # Padrões de variação
        self.variation_patterns = {
            "function_variations": [
                "add_", "remove_", "update_", "get_", "set_", "toggle_", "reset_",
                "enable_", "disable_", "show_", "hide_", "open_", "close_"
            ],
            "variable_variations": [
                "is_", "has_", "can_", "should_", "will_", "did_", "was_",
                "enabled", "disabled", "visible", "hidden", "active", "inactive"
            ],
            "module_suffixes": [
                "_enhanced", "_improved", "_advanced", "_basic", "_simple",
                "_custom", "_extended", "_modified", "_optimized", "_light"
            ]
        }
    
    def load_wiki_knowledge(self):
        """Carrega conhecimento da wiki para geração"""
        try:
            # Carregar documentação OTClient
            otclient_docs = os.path.join(self.wiki_path, "otclient")
            self.otclient_knowledge = self.load_documentation(otclient_docs)
            
            # Carregar padrões conhecidos
            patterns_file = os.path.join(self.wiki_path, "maps", "patterns.json")
            if os.path.exists(patterns_file):
                with open(patterns_file, 'r', encoding='utf-8') as f:
                    self.known_patterns = json.load(f)
            else:
                self.known_patterns = {}
                
        except Exception as e:
            print(f"⚠️ Erro ao carregar conhecimento da wiki: {e}")
            self.otclient_knowledge = {}
            self.known_patterns = {}
    
    def load_documentation(self, docs_path: str) -> Dict[str, Any]:
        """Carrega documentação da pasta especificada"""
        knowledge = {}
        
        if not os.path.exists(docs_path):
            return knowledge
        
        for file_path in Path(docs_path).rglob("*.md"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    relative_path = str(file_path.relative_to(docs_path))
                    knowledge[relative_path] = content
            except Exception as e:
                print(f"⚠️ Erro ao carregar {file_path}: {e}")
        
        return knowledge
    
    def generate_module_variations(self, base_analysis: Dict[str, Any], 
                                 variation_count: int = 3) -> List[Dict[str, Any]]:
        """
        Gera variações de um módulo baseado na análise
        
        Args:
            base_analysis: Análise do módulo base
            variation_count: Número de variações a gerar
            
        Returns:
            Lista de variações geradas
        """
        print(f"🎨 Gerando {variation_count} variações do módulo: {base_analysis['module_name']}")
        
        variations = []
        
        for i in range(variation_count):
            variation_name = self.generate_variation_name(base_analysis['module_name'], i)
            
            variation = {
                "variation_id": i + 1,
                "base_module": base_analysis['module_name'],
                "variation_name": variation_name,
                "generation_date": datetime.now().isoformat(),
                "files": {},
                "modifications": {},
                "compatibility_score": 0.0
            }
            
            # Gerar arquivos da variação
            variation["files"] = self.generate_variation_files(base_analysis, variation_name)
            
            # Calcular modificações
            variation["modifications"] = self.calculate_modifications(base_analysis, variation)
            
            # Calcular score de compatibilidade
            variation["compatibility_score"] = self.calculate_compatibility_score(variation)
            
            variations.append(variation)
        
        # Salvar variações
        self.save_variations(base_analysis['module_name'], variations)
        
        return variations
    
    def generate_variation_name(self, base_name: str, variation_id: int) -> str:
        """Gera nome para a variação"""
        suffix = random.choice(self.variation_patterns["module_suffixes"])
        return f"{base_name}{suffix}_{variation_id + 1}"
    
    def generate_variation_files(self, base_analysis: Dict[str, Any], 
                               variation_name: str) -> Dict[str, Any]:
        """Gera arquivos da variação baseado no módulo original"""
        files = {}
        
        for file_path, file_analysis in base_analysis["files"].items():
            if file_analysis["file_type"] == ".lua":
                files[file_path] = self.generate_lua_variation(file_analysis, variation_name)
            elif file_analysis["file_type"] == ".otmod":
                files[file_path] = self.generate_otmod_variation(file_analysis, variation_name)
            elif file_analysis["file_type"] == ".otui":
                files[file_path] = self.generate_otui_variation(file_analysis, variation_name)
            else:
                # Copiar arquivo original para outros tipos
                files[file_path] = file_analysis
        
        return files
    
    def generate_lua_variation(self, file_analysis: Dict[str, Any], 
                             variation_name: str) -> Dict[str, Any]:
        """Gera variação de arquivo Lua"""
        content = file_analysis.get("content", "")
        structure = file_analysis.get("structure", {})
        
        # Aplicar variações
        modified_content = content
        
        # Variação 1: Adicionar novas funções
        modified_content = self.add_new_functions(modified_content, variation_name)
        
        # Variação 2: Modificar funções existentes
        modified_content = self.modify_existing_functions(modified_content, variation_name)
        
        # Variação 3: Adicionar novas variáveis
        modified_content = self.add_new_variables(modified_content, variation_name)
        
        # Variação 4: Adicionar comentários de documentação
        modified_content = self.add_documentation_comments(modified_content, variation_name)
        
        # Criar nova análise do arquivo modificado
        new_file_analysis = deepcopy(file_analysis)
        new_file_analysis["content"] = modified_content
        new_file_analysis["original_content"] = content
        new_file_analysis["modifications"] = {
            "new_functions": self.count_new_functions(content, modified_content),
            "modified_functions": self.count_modified_functions(content, modified_content),
            "new_variables": self.count_new_variables(content, modified_content)
        }
        
        return new_file_analysis
    
    def add_new_functions(self, content: str, variation_name: str) -> str:
        """Adiciona novas funções ao código Lua"""
        new_functions = []
        
        # Funções de utilidade
        utility_functions = [
            f"""
-- Função de utilidade para {variation_name}
function {variation_name}_getInfo()
    return {{
        name = "{variation_name}",
        version = "1.0",
        description = "Variação do módulo original"
    }}
end
""",
            f"""
-- Função de configuração para {variation_name}
function {variation_name}_configure()
    local config = {{
        enabled = true,
        autoSave = true,
        debugMode = false
    }}
    return config
end
""",
            f"""
-- Função de inicialização para {variation_name}
function {variation_name}_init()
    print("Inicializando {variation_name}")
    local config = {variation_name}_configure()
    return config
end
"""
        ]
        
        # Adicionar funções aleatórias
        num_functions = random.randint(1, 3)
        selected_functions = random.sample(utility_functions, num_functions)
        new_functions.extend(selected_functions)
        
        # Adicionar ao final do arquivo
        if new_functions:
            content += "\n" + "\n".join(new_functions)
        
        return content
    
    def modify_existing_functions(self, content: str, variation_name: str) -> str:
        """Modifica funções existentes"""
        # Encontrar funções existentes
        function_pattern = r'function\s+(\w+)\s*\([^)]*\)'
        functions = re.findall(function_pattern, content)
        
        if not functions:
            return content
        
        # Selecionar função aleatória para modificar
        target_function = random.choice(functions)
        
        # Adicionar prefixo à função
        new_function_name = f"{variation_name}_{target_function}"
        
        # Substituir nome da função
        content = re.sub(
            rf'function\s+{target_function}\s*\(',
            f'function {new_function_name}(',
            content
        )
        
        # Adicionar comentário explicativo
        comment = f"\n-- Função {target_function} modificada para {variation_name}"
        content = content.replace(f'function {new_function_name}(', comment + f'\nfunction {new_function_name}(')
        
        return content
    
    def add_new_variables(self, content: str, variation_name: str) -> str:
        """Adiciona novas variáveis ao código Lua"""
        new_variables = []
        
        # Variáveis de configuração
        config_variables = [
            f"local {variation_name}_enabled = true",
            f"local {variation_name}_debug = false",
            f"local {variation_name}_version = '1.0'",
            f"local {variation_name}_config = {{}}"
        ]
        
        # Adicionar variáveis aleatórias
        num_variables = random.randint(2, 4)
        selected_variables = random.sample(config_variables, num_variables)
        new_variables.extend(selected_variables)
        
        # Adicionar no início do arquivo (após comentários)
        if new_variables:
            # Encontrar posição após comentários iniciais
            lines = content.splitlines()
            insert_pos = 0
            
            for i, line in enumerate(lines):
                if line.strip() and not line.strip().startswith('--'):
                    insert_pos = i
                    break
            
            # Inserir variáveis
            lines.insert(insert_pos, "")
            lines.insert(insert_pos, f"-- Configurações para {variation_name}")
            for var in new_variables:
                lines.insert(insert_pos + 1, var)
            
            content = "\n".join(lines)
        
        return content
    
    def add_documentation_comments(self, content: str, variation_name: str) -> str:
        """Adiciona comentários de documentação"""
        # Adicionar cabeçalho de documentação
        header = f"""
-- ========================================
-- Módulo: {variation_name}
-- Descrição: Variação funcional do módulo original
-- Data de criação: {datetime.now().strftime('%Y-%m-%d')}
-- ========================================

"""
        
        content = header + content
        
        return content
    
    def generate_otmod_variation(self, file_analysis: Dict[str, Any], 
                               variation_name: str) -> Dict[str, Any]:
        """Gera variação de arquivo .otmod"""
        content = file_analysis.get("content", "")
        
        # Modificar informações do módulo
        modified_content = content
        
        # Alterar nome do módulo
        modified_content = re.sub(
            r'name:\s*\w+',
            f'name: {variation_name}',
            modified_content
        )
        
        # Alterar descrição
        modified_content = re.sub(
            r'description:\s*[^\n]+',
            f'description: Variação funcional do módulo original',
            modified_content
        )
        
        # Adicionar informações extras
        extra_info = f"""
  author: Module Generator Agent
  website: Generated variation
  reloadable: true
  sandboxed: true
"""
        
        # Inserir após a linha "Module"
        modified_content = modified_content.replace("Module", "Module" + extra_info)
        
        # Criar nova análise
        new_file_analysis = deepcopy(file_analysis)
        new_file_analysis["content"] = modified_content
        new_file_analysis["original_content"] = content
        new_file_analysis["modifications"] = {
            "name_changed": True,
            "description_changed": True,
            "extra_info_added": True
        }
        
        return new_file_analysis
    
    def generate_otui_variation(self, file_analysis: Dict[str, Any], 
                              variation_name: str) -> Dict[str, Any]:
        """Gera variação de arquivo .otui"""
        content = file_analysis.get("content", "")
        
        # Modificar nomes de widgets
        modified_content = content
        
        # Substituir nomes de widgets com prefixo da variação
        widget_pattern = r'(\w+)\s+(\w+)'
        
        def replace_widget_name(match):
            widget_type = match.group(1)
            widget_name = match.group(2)
            new_name = f"{variation_name}_{widget_name}"
            return f"{widget_type} {new_name}"
        
        modified_content = re.sub(widget_pattern, replace_widget_name, modified_content)
        
        # Criar nova análise
        new_file_analysis = deepcopy(file_analysis)
        new_file_analysis["content"] = modified_content
        new_file_analysis["original_content"] = content
        new_file_analysis["modifications"] = {
            "widget_names_changed": True
        }
        
        return new_file_analysis
    
    def calculate_modifications(self, base_analysis: Dict[str, Any], 
                              variation: Dict[str, Any]) -> Dict[str, Any]:
        """Calcula modificações feitas na variação"""
        modifications = {
            "total_files_modified": 0,
            "functions_added": 0,
            "functions_modified": 0,
            "variables_added": 0,
            "widgets_modified": 0,
            "structure_changes": 0
        }
        
        for file_path, file_analysis in variation["files"].items():
            file_mods = file_analysis.get("modifications", {})
            
            if file_mods:
                modifications["total_files_modified"] += 1
                modifications["functions_added"] += file_mods.get("new_functions", 0)
                modifications["functions_modified"] += file_mods.get("modified_functions", 0)
                modifications["variables_added"] += file_mods.get("new_variables", 0)
                
                if file_mods.get("widget_names_changed"):
                    modifications["widgets_modified"] += 1
        
        return modifications
    
    def calculate_compatibility_score(self, variation: Dict[str, Any]) -> float:
        """Calcula score de compatibilidade da variação"""
        score = 1.0  # Score base
        
        modifications = variation.get("modifications", {})
        
        # Penalizar muitas modificações
        total_mods = sum(modifications.values())
        if total_mods > 10:
            score -= 0.2
        elif total_mods > 5:
            score -= 0.1
        
        # Penalizar modificações estruturais
        if modifications.get("structure_changes", 0) > 0:
            score -= 0.3
        
        # Bonus para modificações balanceadas
        if 1 <= modifications.get("functions_added", 0) <= 3:
            score += 0.1
        
        # Garantir score mínimo
        return max(0.0, min(1.0, score))
    
    def count_new_functions(self, original_content: str, modified_content: str) -> int:
        """Conta novas funções adicionadas"""
        original_functions = set(re.findall(r'function\s+(\w+)', original_content))
        modified_functions = set(re.findall(r'function\s+(\w+)', modified_content))
        
        return len(modified_functions - original_functions)
    
    def count_modified_functions(self, original_content: str, modified_content: str) -> int:
        """Conta funções modificadas"""
        original_functions = set(re.findall(r'function\s+(\w+)', original_content))
        modified_functions = set(re.findall(r'function\s+(\w+)', modified_content))
        
        return len(original_functions & modified_functions)
    
    def count_new_variables(self, original_content: str, modified_content: str) -> int:
        """Conta novas variáveis adicionadas"""
        original_vars = set(re.findall(r'local\s+(\w+)', original_content))
        modified_vars = set(re.findall(r'local\s+(\w+)', modified_content))
        
        return len(modified_vars - original_vars)
    
    def save_variations(self, base_module_name: str, variations: List[Dict[str, Any]]):
        """Salva variações geradas"""
        output_file = os.path.join(
            self.results_path, 
            "generated_modules", 
            f"{base_module_name}_variations.json"
        )
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(variations, f, indent=2, ensure_ascii=False)
            print(f"✅ Variações salvas em: {output_file}")
        except Exception as e:
            print(f"⚠️ Erro ao salvar variações: {e}")
    
    def create_physical_files(self, variation: Dict[str, Any]) -> str:
        """Cria arquivos físicos da variação"""
        variation_name = variation["variation_name"]
        variation_path = os.path.join(self.results_path, "generated_modules", variation_name)
        
        # Criar diretório da variação
        os.makedirs(variation_path, exist_ok=True)
        
        # Criar arquivos
        for file_path, file_analysis in variation["files"].items():
            file_content = file_analysis.get("content", "")
            full_file_path = os.path.join(variation_path, file_path)
            
            # Criar diretórios necessários
            os.makedirs(os.path.dirname(full_file_path), exist_ok=True)
            
            # Escrever arquivo
            try:
                with open(full_file_path, 'w', encoding='utf-8') as f:
                    f.write(file_content)
            except Exception as e:
                print(f"⚠️ Erro ao criar arquivo {full_file_path}: {e}")
        
        return variation_path

def main():
    """Função principal para teste do agente"""
    generator = ModuleGeneratorAgent()
    
    # Exemplo de análise base (simulado)
    base_analysis = {
        "module_name": "client",
        "files": {
            "client.lua": {
                "content": "function init()\n  print('Hello')\nend",
                "file_type": ".lua",
                "structure": {"functions": [{"name": "init"}]}
            },
            "client.otmod": {
                "content": "Module\n  name: client\n  description: Test module",
                "file_type": ".otmod"
            }
        }
    }
    
    # Gerar variações
    variations = generator.generate_module_variations(base_analysis, 2)
    
    print(f"✅ Geradas {len(variations)} variações")
    for i, variation in enumerate(variations):
        print(f"  Variação {i+1}: {variation['variation_name']} (Score: {variation['compatibility_score']:.2f})")

if __name__ == "__main__":
    main() 