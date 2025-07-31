#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code Generator Agent - Sistema de Geração Automática de Código

Este agente é responsável por:
- Gerar código automaticamente baseado em especificações
- Criar templates de código reutilizáveis
- Validar código gerado
- Integrar com o sistema de task management
- Gerar documentação de código
"""

import json
import logging
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class CodeGeneratorAgent:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent.parent
        self.dashboard_path = self.base_path / "wiki" / "dashboard"
        self.log_path = self.base_path / "wiki" / "log"
        self.templates_path = self.base_path / "wiki" / "bmad" / "templates"
        
        # Criar pasta de templates se não existir
        self.templates_path.mkdir(exist_ok=True)
        
        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('CodeGeneratorAgent')
        
        # Carregar configurações
        self.load_configuration()
        
    def load_configuration(self):
        """Carrega configurações do sistema"""
        self.logger.info("🔧 Carregando configurações do Code Generator Agent...")
        
        # Configurações padrão
        self.config = {
            "supported_languages": ["python", "lua", "cpp", "javascript", "html", "css"],
            "template_dir": "templates",
            "output_dir": "generated",
            "auto_validate": True,
            "generate_docs": True,
            "templates": {
                "python_agent": "python_agent_template.py",
                "lua_module": "lua_module_template.lua",
                "cpp_class": "cpp_class_template.cpp",
                "javascript_module": "javascript_module_template.js",
                "html_page": "html_page_template.html",
                "css_style": "css_style_template.css"
            }
        }
        
        self.logger.info("✅ Configurações carregadas com sucesso")
    
    def analyze_requirements(self, requirements: Dict) -> Dict:
        """Analisa requisitos para geração de código"""
        self.logger.info("📋 Analisando requisitos para geração de código...")
        
        analysis = {
            "language": requirements.get('language', 'python'),
            "type": requirements.get('type', 'agent'),
            "name": requirements.get('name', ''),
            "description": requirements.get('description', ''),
            "features": requirements.get('features', []),
            "dependencies": requirements.get('dependencies', []),
            "output_path": requirements.get('output_path', ''),
            "template": self.select_template(requirements),
            "complexity": self.assess_complexity(requirements)
        }
        
        self.logger.info(f"✅ Requisitos analisados: {analysis['type']} em {analysis['language']}")
        return analysis
    
    def select_template(self, requirements: Dict) -> str:
        """Seleciona template apropriado baseado nos requisitos"""
        language = requirements.get('language', 'python')
        code_type = requirements.get('type', 'agent')
        
        template_mapping = {
            'python': {
                'agent': 'python_agent_template.py',
                'module': 'python_module_template.py',
                'class': 'python_class_template.py',
                'script': 'python_script_template.py'
            },
            'lua': {
                'module': 'lua_module_template.lua',
                'function': 'lua_function_template.lua',
                'class': 'lua_class_template.lua'
            },
            'cpp': {
                'class': 'cpp_class_template.cpp',
                'header': 'cpp_header_template.h',
                'function': 'cpp_function_template.cpp'
            },
            'javascript': {
                'module': 'javascript_module_template.js',
                'class': 'javascript_class_template.js',
                'function': 'javascript_function_template.js'
            }
        }
        
        return template_mapping.get(language, {}).get(code_type, f"{language}_{code_type}_template.{language}")
    
    def assess_complexity(self, requirements: Dict) -> str:
        """Avalia complexidade do código a ser gerado"""
        features = requirements.get('features', [])
        dependencies = requirements.get('dependencies', [])
        
        complexity_score = len(features) + len(dependencies) * 2
        
        if complexity_score <= 3:
            return "low"
        elif complexity_score <= 7:
            return "medium"
        else:
            return "high"
    
    def load_template(self, template_name: str) -> str:
        """Carrega template do arquivo"""
        template_file = self.templates_path / template_name
        
        if not template_file.exists():
            self.logger.warning(f"⚠️ Template não encontrado: {template_file}")
            return self.get_default_template(template_name)
        
        try:
            with open(template_file, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            self.logger.error(f"❌ Erro ao carregar template: {e}")
            return self.get_default_template(template_name)
    
    def get_default_template(self, template_name: str) -> str:
        """Gera template padrão se arquivo não existir"""
        if 'python' in template_name and 'agent' in template_name:
            return self.get_python_agent_template()
        elif 'lua' in template_name and 'module' in template_name:
            return self.get_lua_module_template()
        elif 'cpp' in template_name and 'class' in template_name:
            return self.get_cpp_class_template()
        else:
            return self.get_generic_template(template_name)
    
    def get_python_agent_template(self) -> str:
        """Template padrão para agente Python"""
        return '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
{agent_name} - {description}

Este agente é responsável por:
{features_list}
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class {agent_class_name}:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent.parent
        self.dashboard_path = self.base_path / "wiki" / "dashboard"
        self.log_path = self.base_path / "wiki" / "log"
        
        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('{agent_class_name}')
        
        # Carregar configurações
        self.load_configuration()
        
    def load_configuration(self):
        """Carrega configurações do sistema"""
        self.logger.info("🔧 Carregando configurações do {agent_name}...")
        
        # Configurações padrão
        self.config = {{
            "enabled": True,
            "auto_commit": True,
            "priority": "medium"
        }}
        
        self.logger.info("✅ Configurações carregadas com sucesso")
    
    def run(self):
        """Executa o {agent_name}"""
        self.logger.info("🚀 Iniciando {agent_name}...")
        
        try:
            # Implementar lógica do agente aqui
            self.logger.info("✅ {agent_name} executado com sucesso")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro na execução do {agent_name}: {{e}}")
            return False

if __name__ == "__main__":
    agent = {agent_class_name}()
    success = agent.run()
    
    if success:
        print("✅ {agent_name} executado com sucesso!")
    else:
        print("❌ {agent_name} falhou na execução!")
'''
    
    def get_lua_module_template(self) -> str:
        """Template padrão para módulo Lua"""
        return '''--[[
{module_name} - {description}

Este módulo é responsável por:
{features_list}
--]]

local {module_name} = {{}}

-- Configurações do módulo
{module_name}.config = {{
    enabled = true,
    version = "1.0.0",
    author = "BMAD System"
}}

-- Função de inicialização
function {module_name}:init()
    print("🔧 Inicializando {module_name}...")
    
    -- Implementar inicialização aqui
    
    print("✅ {module_name} inicializado com sucesso")
    return true
end

-- Função principal
function {module_name}:run()
    print("🚀 Executando {module_name}...")
    
    -- Implementar lógica principal aqui
    
    print("✅ {module_name} executado com sucesso")
    return true
end

-- Função de limpeza
function {module_name}:cleanup()
    print("🧹 Limpando {module_name}...")
    
    -- Implementar limpeza aqui
    
    print("✅ {module_name} limpo com sucesso")
end

return {module_name}
'''
    
    def get_cpp_class_template(self) -> str:
        """Template padrão para classe C++"""
        return '''#include <iostream>
#include <string>
#include <vector>

/**
 * {class_name} - {description}
 * 
 * Esta classe é responsável por:
{features_list}
 */
class {class_name} {{
private:
    std::string name;
    bool enabled;
    
public:
    // Construtor
    {class_name}(const std::string& name = "{class_name}") 
        : name(name), enabled(true) {{
        std::cout << "🔧 Inicializando " << name << "..." << std::endl;
    }}
    
    // Destrutor
    ~{class_name}() {{
        std::cout << "🧹 Destruindo " << name << "..." << std::endl;
    }}
    
    // Função principal
    bool run() {{
        std::cout << "🚀 Executando " << name << "..." << std::endl;
        
        // Implementar lógica principal aqui
        
        std::cout << "✅ " << name << " executado com sucesso" << std::endl;
        return true;
    }}
    
    // Getters e setters
    std::string getName() const {{ return name; }}
    void setName(const std::string& newName) {{ name = newName; }}
    
    bool isEnabled() const {{ return enabled; }}
    void setEnabled(bool newEnabled) {{ enabled = newEnabled; }}
}};

// Função principal para teste
int main() {{
    {class_name} agent;
    return agent.run() ? 0 : 1;
}}
'''
    
    def get_generic_template(self, template_name: str) -> str:
        """Template genérico para outros tipos"""
        return f'''/*
 * {template_name} - Template Gerado Automaticamente
 * 
 * Este arquivo foi gerado automaticamente pelo Code Generator Agent
 * 
 * Data de geração: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
 * Agente responsável: Code Generator Agent
 */

// TODO: Implementar funcionalidade específica
// TODO: Adicionar documentação
// TODO: Implementar testes

console.log("🚀 {template_name} carregado com sucesso");
'''
    
    def generate_code(self, analysis: Dict) -> str:
        """Gera código baseado na análise"""
        self.logger.info(f"🔨 Gerando código para {analysis['name']}...")
        
        # Carregar template
        template = self.load_template(analysis['template'])
        
        # Preparar dados para substituição
        replacement_data = {
            'agent_name': analysis['name'],
            'agent_class_name': self.to_class_name(analysis['name']),
            'module_name': analysis['name'].lower().replace(' ', '_'),
            'class_name': self.to_class_name(analysis['name']),
            'description': analysis['description'],
            'features_list': self.format_features(analysis['features']),
            'dependencies_list': self.format_dependencies(analysis['dependencies']),
            'language': analysis['language'],
            'type': analysis['type'],
            'complexity': analysis['complexity'],
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Substituir placeholders no template
        generated_code = template
        for key, value in replacement_data.items():
            placeholder = f"{{{key}}}"
            generated_code = generated_code.replace(placeholder, str(value))
        
        self.logger.info(f"✅ Código gerado para {analysis['name']}")
        return generated_code
    
    def to_class_name(self, name: str) -> str:
        """Converte nome para formato de classe"""
        return ''.join(word.capitalize() for word in name.replace('-', ' ').replace('_', ' ').split())
    
    def format_features(self, features: List[str]) -> str:
        """Formata lista de features para template"""
        if not features:
            return "- Funcionalidade básica"
        
        formatted = []
        for feature in features:
            formatted.append(f"- {feature}")
        
        return '\n'.join(formatted)
    
    def format_dependencies(self, dependencies: List[str]) -> str:
        """Formata lista de dependências para template"""
        if not dependencies:
            return "Nenhuma dependência externa"
        
        formatted = []
        for dep in dependencies:
            formatted.append(f"- {dep}")
        
        return '\n'.join(formatted)
    
    def validate_code(self, code: str, language: str) -> Dict:
        """Valida código gerado"""
        self.logger.info(f"🔍 Validando código {language}...")
        
        validation = {
            "valid": True,
            "warnings": [],
            "errors": [],
            "suggestions": []
        }
        
        # Validações básicas
        if not code.strip():
            validation["valid"] = False
            validation["errors"].append("Código vazio")
        
        # Validações específicas por linguagem
        if language == "python":
            validation.update(self.validate_python_code(code))
        elif language == "lua":
            validation.update(self.validate_lua_code(code))
        elif language == "cpp":
            validation.update(self.validate_cpp_code(code))
        
        self.logger.info(f"✅ Validação concluída: {'válido' if validation['valid'] else 'inválido'}")
        return validation
    
    def validate_python_code(self, code: str) -> Dict:
        """Valida código Python"""
        validation = {"warnings": [], "errors": [], "suggestions": []}
        
        # Verificar imports
        if "import" not in code and "from" not in code:
            validation["warnings"].append("Nenhum import encontrado")
        
        # Verificar classes
        if "class" not in code:
            validation["warnings"].append("Nenhuma classe definida")
        
        # Verificar funções
        if "def" not in code:
            validation["warnings"].append("Nenhuma função definida")
        
        # Verificar documentação
        if '"""' not in code and "'''" not in code:
            validation["suggestions"].append("Adicionar docstrings")
        
        return validation
    
    def validate_lua_code(self, code: str) -> Dict:
        """Valida código Lua"""
        validation = {"warnings": [], "errors": [], "suggestions": []}
        
        # Verificar comentários
        if "--" not in code:
            validation["warnings"].append("Nenhum comentário encontrado")
        
        # Verificar funções
        if "function" not in code:
            validation["warnings"].append("Nenhuma função definida")
        
        # Verificar retorno
        if "return" not in code:
            validation["suggestions"].append("Adicionar return statement")
        
        return validation
    
    def validate_cpp_code(self, code: str) -> Dict:
        """Valida código C++"""
        validation = {"warnings": [], "errors": [], "suggestions": []}
        
        # Verificar includes
        if "#include" not in code:
            validation["warnings"].append("Nenhum include encontrado")
        
        # Verificar classes
        if "class" not in code:
            validation["warnings"].append("Nenhuma classe definida")
        
        # Verificar namespace
        if "namespace" not in code:
            validation["suggestions"].append("Considerar usar namespace")
        
        return validation
    
    def save_code(self, code: str, analysis: Dict) -> str:
        """Salva código gerado em arquivo"""
        output_path = analysis.get('output_path', '')
        
        if not output_path:
            # Gerar caminho padrão
            language = analysis['language']
            name = analysis['name'].lower().replace(' ', '_')
            extension = self.get_file_extension(language)
            output_path = f"generated/{name}.{extension}"
        
        # Criar diretório se não existir
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(code)
            
            self.logger.info(f"✅ Código salvo em: {output_file}")
            return str(output_file)
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao salvar código: {e}")
            return ""
    
    def get_file_extension(self, language: str) -> str:
        """Retorna extensão de arquivo para linguagem"""
        extensions = {
            "python": "py",
            "lua": "lua",
            "cpp": "cpp",
            "javascript": "js",
            "html": "html",
            "css": "css"
        }
        
        return extensions.get(language, "txt")
    
    def generate_documentation(self, code: str, analysis: Dict) -> str:
        """Gera documentação para o código"""
        self.logger.info(f"📚 Gerando documentação para {analysis['name']}...")
        
        doc_template = f"""# {analysis['name']}

## 📋 Descrição

{analysis['description']}

## 🎯 Funcionalidades

{self.format_features(analysis['features'])}

## 🔗 Dependências

{self.format_dependencies(analysis['dependencies'])}

## 📊 Informações Técnicas

- **Linguagem**: {analysis['language']}
- **Tipo**: {analysis['type']}
- **Complexidade**: {analysis['complexity']}
- **Gerado em**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Agente**: Code Generator Agent

## 🔧 Como Usar

```{analysis['language']}
{code[:500]}...
```

## 📝 Notas

- Este código foi gerado automaticamente pelo Code Generator Agent
- Revise e ajuste conforme necessário
- Adicione testes antes de usar em produção

---
**Documentação gerada**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Responsável**: Code Generator Agent
"""
        
        return doc_template
    
    def run(self, requirements: Dict = None) -> bool:
        """Executa o Code Generator Agent"""
        self.logger.info("🚀 Iniciando Code Generator Agent...")
        
        try:
            # Se não há requisitos, usar exemplo padrão
            if not requirements:
                requirements = {
                    "language": "python",
                    "type": "agent",
                    "name": "Example Agent",
                    "description": "Agente de exemplo gerado automaticamente",
                    "features": ["Funcionalidade básica", "Logging", "Configuração"],
                    "dependencies": ["json", "logging", "pathlib"],
                    "output_path": "generated/example_agent.py"
                }
            
            # Analisar requisitos
            analysis = self.analyze_requirements(requirements)
            
            # Gerar código
            code = self.generate_code(analysis)
            
            # Validar código
            if self.config["auto_validate"]:
                validation = self.validate_code(code, analysis['language'])
                if not validation["valid"]:
                    self.logger.error(f"❌ Código inválido: {validation['errors']}")
                    return False
            
            # Salvar código
            output_file = self.save_code(code, analysis)
            
            # Gerar documentação
            if self.config["generate_docs"]:
                documentation = self.generate_documentation(code, analysis)
                doc_file = Path(output_file).with_suffix('.md')
                with open(doc_file, 'w', encoding='utf-8') as f:
                    f.write(documentation)
                self.logger.info(f"✅ Documentação salva em: {doc_file}")
            
            self.logger.info("✅ Code Generator Agent executado com sucesso")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro na execução do Code Generator Agent: {e}")
            return False

if __name__ == "__main__":
    agent = CodeGeneratorAgent()
    success = agent.run()
    
    if success:
        print("✅ Code Generator Agent executado com sucesso!")
    else:
        print("❌ Code Generator Agent falhou na execução!") 