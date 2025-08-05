#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from unicode_aliases import *
"""
Script Migrado: comprehensive_documentation_agent.py
Módulo de Destino: agents.agent_orchestrator
Data de Migração: 2025-08-01 12:21:42

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import AgentorchestratorModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agente abrangente de documentação e organização
====================================

Este agente foi consolidado a partir dos seguintes agentes:
- documentation_agent.py
- documentation_completer_agent.py
- habdel_documentation_organizer.py
- system_dashboard_creator.py

Data de consolidação: 2025-08-01 10:38:28
Autor: Sistema BMAD - Agent Consolidator
"""

Documentation Agent - Sistema de Geração Automática de Documentação

Este agente é responsável por:
- Gerar documentação automaticamente para código
- Criar documentação da wiki
- Manter documentação atualizada
- Validar qualidade da documentação
- Integrar com o sistema de task management
"""

import json
import logging
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class DocumentationAgent:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent.parent
        self.dashboard_path = self.base_path / "wiki" / "dashboard"
        self.log_path = self.base_path / "wiki" / "log"
        self.docs_path = self.base_path / "wiki" / "docs"
        
        # Criar pasta de docs se não existir
        self.docs_path.mkdir(exist_ok=True)
        
        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('DocumentationAgent')
        
        # Carregar configurações
        self.load_configuration()
        
    def load_configuration(self):
        """Carrega configurações do sistema"""
        self.logger.info("🔧 Carregando configurações do Documentation Agent...")
        
        # Configurações padrão
        self.config = {
            "supported_formats": ["markdown", "html", "pdf", "rst"],
            "default_format": "markdown",
            "auto_update": True,
            "quality_check": True,
            "templates": {
                "api_doc": "api_documentation_template.md",
                "user_guide": "user_guide_template.md",
                "technical_doc": "technical_documentation_template.md",
                "readme": "readme_template.md"
            },
            "quality_threshold": 0.8
        }
        
        self.logger.info("✅ Configurações carregadas com sucesso")
    
    def analyze_code_for_documentation(self, code_file: str) -> Dict:
        """Analisa código para gerar documentação"""
        self.logger.info(f"📋 Analisando código: {code_file}")
        
        try:
            with open(code_file, 'r', encoding='utf-8') as f:
                code_content = f.read()
            
            analysis = {
                "file_path": code_file,
                "language": self.detect_language(code_file),
                "classes": self.extract_classes(code_content),
                "functions": self.extract_functions(code_content),
                "imports": self.extract_imports(code_content),
                "comments": self.extract_comments(code_content),
                "complexity": self.assess_complexity(code_content),
                "documentation_needs": self.identify_documentation_needs(code_content)
            }
            
            self.logger.info(f"✅ Análise concluída: {len(analysis['classes'])} classes,
    {len(analysis['functions'])} funções")
            return analysis
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao analisar código: {e}")
            return {}
    
    def detect_language(self, file_path: str) -> str:
        """Detecta linguagem do arquivo baseado na extensão"""
        extensions = {
            '.py': 'python',
            '.lua': 'lua',
            '.cpp': 'cpp',
            '.h': 'cpp',
            '.js': 'javascript',
            '.html': 'html',
            '.css': 'css'
        }
        
        file_ext = Path(file_path).suffix.lower()
        return extensions.get(file_ext, 'unknown')
    
    def extract_classes(self, code: str) -> List[Dict]:
        """Extrai classes do código"""
        classes = []
        
        # Padrões para diferentes linguagens
        patterns = {
            'python': r'class\s+(\w+)(?:\(([^)]+)\))?:',
            'cpp': r'class\s+(\w+)(?:\s*:\s*(?:public|private|protected)\s+(\w+))?',
            'javascript': r'class\s+(\w+)',
            'lua': r'(\w+)\s*=\s*{}'
        }
        
        for language, pattern in patterns.items():
            matches = re.finditer(pattern, code, re.MULTILINE)
            for match in matches:
                class_name = match.group(1)
                inheritance = match.group(2) if len(match.groups()) > 1 else None
                
                classes.append({
                    "name": class_name,
                    "language": language,
                    "inheritance": inheritance,
                    "line": code[:match.start()].count('\n') + 1
                })
        
        return classes
    
    def extract_functions(self, code: str) -> List[Dict]:
        """Extrai funções do código"""
        functions = []
        
        # Padrões para diferentes linguagens
        patterns = {
            'python': r'def\s+(\w+)\s*\(([^)]*)\):',
            'cpp': r'(\w+)\s+(\w+)\s*\(([^)]*)\)',
            'javascript': r'function\s+(\w+)\s*\(([^)]*)\)',
            'lua': r'function\s+(\w+)\s*\(([^)]*)\)'
        }
        
        for language, pattern in patterns.items():
            matches = re.finditer(pattern, code, re.MULTILINE)
            for match in matches:
                if language == 'cpp':
                    return_type = match.group(1)
                    func_name = match.group(2)
                    params = match.group(3)
                else:
                    func_name = match.group(1)
                    params = match.group(2)
                    return_type = None
                
                functions.append({
                    "name": func_name,
                    "language": language,
                    "parameters": self.parse_parameters(params),
                    "return_type": return_type,
                    "line": code[:match.start()].count('\n') + 1
                })
        
        return functions
    
    def extract_imports(self, code: str) -> List[str]:
        """Extrai imports do código"""
        imports = []
        
        # Padrões para diferentes linguagens
        patterns = {
            'python': r'(?:from\s+(\w+)\s+import|\s+import\s+(\w+))',
            'cpp': r'#include\s*[<"]([^>"]+)[>"]',
            'javascript': r'import\s+(?:.*\s+from\s+)?[\'"]([^\'"]+)[\'"]',
            'lua': r'require\s*[\'"]([^\'"]+)[\'"]'
        }
        
        for language, pattern in patterns.items():
            matches = re.finditer(pattern, code, re.MULTILINE)
            for match in matches:
                import_name = match.group(1)
                if import_name:
                    imports.append(f"{language}:{import_name}")
        
        return imports
    
    def extract_comments(self, code: str) -> List[Dict]:
        """Extrai comentários do código"""
        comments = []
        
        # Padrões para diferentes linguagens
        patterns = {
            'python': [
                (r'#\s*(.+)', 'single_line'),
                (r'"""(.*?)"""', 'docstring'),
                (r"'''(.*?)'''", 'docstring')
            ],
            'cpp': [
                (r'//\s*(.+)', 'single_line'),
                (r'/\*(.*?)\*/', 'multi_line')
            ],
            'javascript': [
                (r'//\s*(.+)', 'single_line'),
                (r'/\*(.*?)\*/', 'multi_line')
            ],
            'lua': [
                (r'--\s*(.+)', 'single_line'),
                (r'--\[\[(.*?)\]\]', 'multi_line')
            ]
        }
        
        for language, lang_patterns in patterns.items():
            for pattern, comment_type in lang_patterns:
                matches = re.finditer(pattern, code, re.MULTILINE | re.DOTALL)
                for match in matches:
                    comment_text = match.group(1).strip()
                    if comment_text:
                        comments.append({
                            "text": comment_text,
                            "type": comment_type,
                            "language": language,
                            "line": code[:match.start()].count('\n') + 1
                        })
        
        return comments
    
    def parse_parameters(self, params_str: str) -> List[Dict]:
        """Parse parâmetros de função"""
        if not params_str.strip():
            return []
        
        params = []
        param_list = [p.strip() for p in params_str.split(',')]
        
        for param in param_list:
            if '=' in param:
                name, default = param.split('=', 1)
                params.append({
                    "name": name.strip(),
                    "default": default.strip(),
                    "required": False
                })
            else:
                params.append({
                    "name": param.strip(),
                    "default": None,
                    "required": True
                })
        
        return params
    
    def assess_complexity(self, code: str) -> str:
        """Avalia complexidade do código"""
        lines = code.split('\n')
        functions = len(self.extract_functions(code))
        classes = len(self.extract_classes(code))
        
        complexity_score = len(lines) + functions * 5 + classes * 10
        
        if complexity_score <= 100:
            return "low"
        elif complexity_score <= 500:
            return "medium"
        else:
            return "high"
    
    def identify_documentation_needs(self, code: str) -> List[str]:
        """Identifica necessidades de documentação"""
        needs = []
        
        # Verificar se há docstrings
        if '"""' not in code and "'''" not in code:"
            needs.append("Adicionar docstrings")
        
        # Verificar se há comentários
        if not re.search(r'#|//|--', code):
            needs.append("Adicionar comentários")
        
        # Verificar se há README
        if not Path(self.base_path / "README.md").exists():
            needs.append("Criar README")
        
        # Verificar se há documentação de API
        if len(self.extract_functions(code)) > 5:
            needs.append("Criar documentação de API")
        
        return needs
    
    def generate_api_documentation(self, analysis: Dict) -> str:
        """Gera documentação de API"""
        self.logger.info(f"📚 Gerando documentação de API para {analysis['file_path']}")
        
        doc_template = f"""# API Documentation - {Path(analysis['file_path']).name}

## 📋 Visão Geral

Este documento descreve a API do arquivo `{analysis['file_path']}`.

**Linguagem**: {analysis['language']}
**Complexidade**: {analysis['complexity']}
**Gerado em**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 🔗 Imports

"""
        
        if analysis['imports']:
            for imp in analysis['imports']:
                doc_template += f"- `{imp}`\n"
        else:
            doc_template += "- Nenhum import encontrado\n"
        
        doc_template += "\n## 🏗️ Classes\n\n"
        
        if analysis['classes']:
            for cls in analysis['classes']:
                doc_template += f"### {cls['name']}\n\n"
                doc_template += f"- **Linguagem**: {cls['language']}\n"
                if cls['inheritance']:
                    doc_template += f"- **Herança**: {cls['inheritance']}\n"
                doc_template += f"- **Linha**: {cls['line']}\n\n"
        else:
            doc_template += "Nenhuma classe encontrada.\n\n"
        
        doc_template += "## ⚙️ Funções\n\n"
        
        if analysis['functions']:
            for func in analysis['functions']:
                doc_template += f"### {func['name']}\n\n"
                doc_template += f"- **Linguagem**: {func['language']}\n"
                if func['return_type']:
                    doc_template += f"- **Retorno**: {func['return_type']}\n"
                doc_template += f"- **Linha**: {func['line']}\n"
                
                if func['parameters']:
                    doc_template += "- **Parâmetros**:\n"
                    for param in func['parameters']:
                        required = "Obrigatório" if param['required'] else "Opcional"
                        default = f" (padrão: {param['default']})" if param['default'] else ""
                        doc_template += f"  - `{param['name']}`: {required}{default}\n"
                
                doc_template += "\n"
        else:
            doc_template += "Nenhuma função encontrada.\n\n"
        
        doc_template += f"""## 📝 Comentários

Encontrados {len(analysis['comments'])} comentários no código.

## 🔧 Necessidades de Documentação

"""
        
        if analysis['documentation_needs']:
            for need in analysis['documentation_needs']:
                doc_template += f"- {need}\n"
        else:
            doc_template += "- Documentação adequada\n"
        
        doc_template += f"""
## 📊 Estatísticas

- **Total de linhas**: {len(analysis.get('code_content', '').split('\\n'))}
- **Classes**: {len(analysis['classes'])}
- **Funções**: {len(analysis['functions'])}
- **Imports**: {len(analysis['imports'])}
- **Comentários**: {len(analysis['comments'])}

---
**Documentação gerada**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Responsável**: Documentation Agent
"""
        
        return doc_template
    
    def generate_readme(self, analysis: Dict) -> str:
        """Gera README para o projeto"""
        self.logger.info("📚 Gerando README...")
        
        readme_template = f"""# {Path(analysis['file_path']).stem}

## 📋 Descrição

Documentação gerada automaticamente para `{analysis['file_path']}`.

## 🚀 Instalação

```bash
# Instalar dependências
pip install -r requirements.txt
```

## 🔧 Uso

```{analysis['language']}
# Exemplo de uso
from {Path(analysis['file_path']).stem} import main

main()
```

## 📚 Documentação

- [API Documentation](api_documentation.md)
- [User Guide](user_guide.md)
- [Technical Documentation](technical_documentation.md)

## 🏗️ Estrutura

```
{Path(analysis['file_path']).parent}/
├── {Path(analysis['file_path']).name}
├── api_documentation.md
├── user_guide.md
└── technical_documentation.md
```

## 📊 Estatísticas

- **Linguagem**: {analysis['language']}
- **Complexidade**: {analysis['complexity']}
- **Classes**: {len(analysis['classes'])}
- **Funções**: {len(analysis['functions'])}

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT.

---
**Gerado automaticamente**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Responsável**: Documentation Agent
"""
        
        return readme_template
    
    def validate_documentation_quality(self, documentation: str) -> Dict:
        """Valida qualidade da documentação"""
        self.logger.info("🔍 Validando qualidade da documentação...")
        
        quality_score = 0.0
        issues = []
        suggestions = []
        
        # Verificar se há seções importantes
        required_sections = ['# ', '## ', '### ']
        for section in required_sections:
            if section in documentation:
                quality_score += 0.2
            else:
                issues.append(f"Seção {section} não encontrada")
        
        # Verificar se há exemplos de código
        if '```' in documentation:
            quality_score += 0.2
        else:
            suggestions.append("Adicionar exemplos de código")
        
        # Verificar se há links
        if '[' in documentation and '](' in documentation:
            quality_score += 0.1
        else:
            suggestions.append("Adicionar links para referências")
        
        # Verificar se há listas
        if '- ' in documentation or '* ' in documentation:
            quality_score += 0.1
        else:
            suggestions.append("Usar listas para melhor organização")
        
        # Verificar se há tabelas
        if '|' in documentation:
            quality_score += 0.1
        else:
            suggestions.append("Considerar usar tabelas para dados estruturados")
        
        # Verificar se há emojis para melhor visualização
        if any(emoji in documentation for emoji in ['📋', '🚀', '🔧', '📚', '🏗️', '📊', '🤝', '📄']):
            quality_score += 0.1
        else:
            suggestions.append("Adicionar emojis para melhor visualização")
        
        # Verificar se há informações de contato/autoria
        if 'Responsável' in documentation or 'Autor' in documentation:
            quality_score += 0.1
        else:
            suggestions.append("Adicionar informações de autoria")
        
        quality_score = min(quality_score, 1.0)
        
        validation = {
            "quality_score": quality_score,
            "is_acceptable": quality_score >= self.config["quality_threshold"],
            "issues": issues,
            "suggestions": suggestions
        }
        
        self.logger.info(f"✅ Qualidade validada: {quality_score:.2f}/1.0")
        return validation
    
    def save_documentation(self, documentation: str, analysis: Dict, doc_type: str) -> str:
        """Salva documentação gerada"""
        file_name = f"{Path(analysis['file_path']).stem}_{doc_type}.md"
        output_path = self.docs_path / file_name
        
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(documentation)
            
            self.logger.info(f"✅ Documentação salva em: {output_path}")
            return str(output_path)
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao salvar documentação: {e}")
            return ""
    
    def run(self, code_file: str = None) -> bool:
        """Executa o Documentation Agent"""
        self.logger.info("🚀 Iniciando Documentation Agent...")
        
        try:
            # Se não há arquivo especificado, usar exemplo
            if not code_file:
                code_file = str(self.base_path / "wiki" / "bmad" / "agents" / "task_master_agent.py")
            
            # Verificar se arquivo existe
            if not Path(code_file).exists():
                self.logger.error(f"❌ Arquivo não encontrado: {code_file}")
                return False
            
            # Analisar código
            analysis = self.analyze_code_for_documentation(code_file)
            if not analysis:
                return False
            
            # Gerar documentação de API
            api_doc = self.generate_api_documentation(analysis)
            api_doc_path = self.save_documentation(api_doc, analysis, "api")
            
            # Gerar README
            readme = self.generate_readme(analysis)
            readme_path = self.save_documentation(readme, analysis, "readme")
            
            # Validar qualidade
            if self.config["quality_check"]:
                api_quality = self.validate_documentation_quality(api_doc)
                readme_quality = self.validate_documentation_quality(readme)
                
                self.logger.info(f"📊 Qualidade da documentação:")
                self.logger.info(f"   - API Doc: {api_quality['quality_score']:.2f}/1.0")
                self.logger.info(f"   - README: {readme_quality['quality_score']:.2f}/1.0")
            
            self.logger.info("✅ Documentation Agent executado com sucesso")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro na execução do Documentation Agent: {e}")
            return False

if __name__ == "__main__":
    agent = DocumentationAgent()
    success = agent.run()
    
    if success:
        print("✅ Documentation Agent executado com sucesso!")
    else:
        print("❌ Documentation Agent falhou na execução!") 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = AgentorchestratorModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script comprehensive_documentation_agent.py executado com sucesso via módulo agents.agent_orchestrator")
    else:
        print(f"❌ Erro na execução do script comprehensive_documentation_agent.py via módulo agents.agent_orchestrator")

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
- **Nome**: migrated_comprehensive_documentation_agent
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

