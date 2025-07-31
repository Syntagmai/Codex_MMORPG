#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agent Organizer
Script para organizar automaticamente agentes e migrar para estrutura BMAD
"""

import os
import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any

class AgentOrganizer:
    """Organizador automático de agentes"""
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.bmad_path = self.base_path / "bmad"
        self.agents_path = self.bmad_path / "agents"
        
        # Estrutura padrão para agentes
        self.standard_structure = {
            "patterns": ["error_patterns.json", "quality_patterns.json", "context_patterns.json"],
            "scripts": ["analyzer.py", "optimizer.py", "validator.py"],
            "knowledge": ["best_practices.md", "common_errors.md", "optimization_tips.md", "integration_guide.md"],
            "logs": ["error_log.json", "improvement_log.json", "performance_log.json"],
            "tests": ["test_integration.py", "test_functionality.py", "test_performance.py"],
            "docs": ["README.md", "API.md", "examples.md"],
            "config": ["agent_config.json", "integration_config.json"]
        }
    
    def detect_existing_agents(self) -> List[Dict[str, Any]]:
        """Detecta agentes existentes fora da estrutura BMAD"""
        print("🔍 Detectando agentes existentes...")
        
        agents = []
        
        # Padrões para detectar agentes
        agent_patterns = [
            "agente_*",
            "*_agent",
            "agent_*"
        ]
        
        # Procurar na pasta wiki
        for item in self.base_path.iterdir():
            if item.is_dir():
                item_name = item.name.lower()
                
                # Verificar se é um agente
                for pattern in agent_patterns:
                    if self.matches_pattern(item_name, pattern):
                        agents.append({
                            "name": item.name,
                            "path": str(item),
                            "type": self.detect_agent_type(item),
                            "structure": self.analyze_current_structure(item)
                        })
                        break
        
        print(f"✅ Encontrados {len(agents)} agentes para organização")
        return agents
    
    def matches_pattern(self, name: str, pattern: str) -> bool:
        """Verifica se nome corresponde ao padrão"""
        if pattern == "agente_*":
            return name.startswith("agente_")
        elif pattern == "*_agent":
            return name.endswith("_agent")
        elif pattern == "agent_*":
            return name.startswith("agent_")
        return False
    
    def detect_agent_type(self, agent_path: Path) -> str:
        """Detecta o tipo do agente baseado no conteúdo"""
        agent_name = agent_path.name.lower()
        
        if "python" in agent_name or "py" in agent_name:
            return "python"
        elif "lua" in agent_name:
            return "lua"
        elif "cpp" in agent_name or "c++" in agent_name:
            return "cpp"
        else:
            return "generic"
    
    def analyze_current_structure(self, agent_path: Path) -> Dict[str, Any]:
        """Analisa estrutura atual do agente"""
        structure = {
            "files": [],
            "folders": [],
            "has_main_agent": False,
            "has_patterns": False,
            "has_scripts": False,
            "has_knowledge": False
        }
        
        for item in agent_path.rglob("*"):
            if item.is_file():
                structure["files"].append(str(item.relative_to(agent_path)))
                
                # Verificar tipos de arquivos
                if "agent" in item.name.lower() and item.suffix == ".py":
                    structure["has_main_agent"] = True
                elif "pattern" in item.name.lower():
                    structure["has_patterns"] = True
                elif "script" in item.name.lower() or "analyzer" in item.name.lower():
                    structure["has_scripts"] = True
                elif "knowledge" in item.name.lower() or "practice" in item.name.lower():
                    structure["has_knowledge"] = True
            elif item.is_dir():
                structure["folders"].append(str(item.relative_to(agent_path)))
        
        return structure
    
    def create_bmad_agent_structure(self, agent_name: str, agent_type: str) -> Path:
        """Cria estrutura BMAD padrão para agente"""
        print(f"🏗️ Criando estrutura BMAD para agente: {agent_name}")
        
        # Nome padronizado do agente
        if not agent_name.endswith("_agent"):
            agent_name = f"{agent_name}_agent"
        
        agent_path = self.agents_path / agent_name
        agent_path.mkdir(parents=True, exist_ok=True)
        
        # Criar subpastas padrão
        for subfolder in self.standard_structure.keys():
            subfolder_path = agent_path / subfolder
            subfolder_path.mkdir(exist_ok=True)
            
            # Criar arquivos padrão para cada subpasta
            for filename in self.standard_structure[subfolder]:
                file_path = subfolder_path / filename
                if not file_path.exists():
                    self.create_standard_file(file_path, subfolder, filename, agent_type)
        
        # Criar arquivo principal do agente
        main_agent_file = agent_path / f"{agent_name}.py"
        if not main_agent_file.exists():
            self.create_main_agent_file(main_agent_file, agent_name, agent_type)
        
        # Criar README
        readme_file = agent_path / "README.md"
        if not readme_file.exists():
            self.create_agent_readme(readme_file, agent_name, agent_type)
        
        print(f"✅ Estrutura BMAD criada: {agent_path}")
        return agent_path
    
    def create_standard_file(self, file_path: Path, subfolder: str, filename: str, agent_type: str):
        """Cria arquivo padrão baseado no tipo"""
        
        if filename.endswith(".json"):
            # Arquivos JSON
            if "error_patterns" in filename:
                content = self.create_error_patterns_template(agent_type)
            elif "quality_patterns" in filename:
                content = self.create_quality_patterns_template(agent_type)
            elif "context_patterns" in filename:
                content = self.create_context_patterns_template(agent_type)
            elif "config" in filename:
                content = self.create_config_template(agent_type)
            else:
                content = "[]"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(json.loads(content), f, indent=2, ensure_ascii=False)
        
        elif filename.endswith(".md"):
            # Arquivos Markdown
            if "best_practices" in filename:
                content = self.create_best_practices_template(agent_type)
            elif "common_errors" in filename:
                content = self.create_common_errors_template(agent_type)
            elif "optimization_tips" in filename:
                content = self.create_optimization_tips_template(agent_type)
            elif "integration_guide" in filename:
                content = self.create_integration_guide_template(agent_type)
            else:
                content = f"# {filename.replace('.md', '').replace('_', ' ').title()}\n\nConteúdo para {agent_type} agent."
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        elif filename.endswith(".py"):
            # Arquivos Python
            if "analyzer" in filename:
                content = self.create_analyzer_template(agent_type)
            elif "optimizer" in filename:
                content = self.create_optimizer_template(agent_type)
            elif "validator" in filename:
                content = self.create_validator_template(agent_type)
            elif "test" in filename:
                content = self.create_test_template(agent_type)
            else:
                content = f"# {filename}\n# Template para {agent_type} agent"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
    
    def create_main_agent_file(self, file_path: Path, agent_name: str, agent_type: str):
        """Cria arquivo principal do agente"""
        content = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
{agent_name.replace('_', ' ').title()}
Agente especializado em {agent_type} development
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Any
from pathlib import Path

class {agent_name.replace('_', '').title()}Agent:
    """Agente especializado em {agent_type}"""
    
    def __init__(self, name: str = "{agent_name.replace('_', ' ').title()}", base_path: str = "wiki"):
        self.name = name
        self.base_path = Path(base_path)
        self.agent_path = self.base_path / "bmad" / "agents" / "{agent_name}"
        
        # Carregar configurações
        self.config = self.load_config()
        
    def load_config(self) -> Dict[str, Any]:
        """Carrega configurações do agente"""
        config_file = self.agent_path / "config" / "agent_config.json"
        if config_file.exists():
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {{"agent_type": "{agent_type}", "version": "1.0"}}
    
    def analyze(self, target: str) -> Dict[str, Any]:
        """Análise principal do agente"""
        return {{"status": "success", "message": "Análise implementada"}}
    
    def optimize(self, target: str) -> Dict[str, Any]:
        """Otimização principal do agente"""
        return {{"status": "success", "message": "Otimização implementada"}}
    
    def validate(self, target: str) -> Dict[str, Any]:
        """Validação principal do agente"""
        return {{"status": "success", "message": "Validação implementada"}}

def main():
    """Função principal"""
    agent = {agent_name.replace('_', '').title()}Agent()
    print(f"🤖 {agent.name} inicializado")

if __name__ == "__main__":
    main()
'''
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def create_agent_readme(self, file_path: Path, agent_name: str, agent_type: str):
        """Cria README do agente"""
        content = f'''# {agent_name.replace('_', ' ').title()}

## 📋 Descrição

Agente especializado em desenvolvimento e qualidade de código {agent_type}.

## 🎯 Funcionalidades

- **Análise automática** de código {agent_type}
- **Detecção de problemas** e sugestões de melhoria
- **Otimização automática** de código existente
- **Validação de qualidade** e padrões

## 📁 Estrutura

```
{agent_name}/
├── {agent_name}.py              # Implementação principal
├── patterns/                    # Padrões específicos
├── scripts/                     # Scripts auxiliares
├── knowledge/                   # Base de conhecimento
├── logs/                        # Logs específicos
├── tests/                       # Testes
├── docs/                        # Documentação
└── config/                      # Configurações
```

## 🚀 Uso

```python
from {agent_name}.{agent_name} import {agent_name.replace('_', '').title()}Agent

agent = {agent_name.replace('_', '').title()}Agent()
result = agent.analyze("target_file")
```

## 📚 Documentação

- [API Documentation](docs/API.md)
- [Examples](docs/examples.md)
- [Best Practices](knowledge/best_practices.md)

---
*Agente {agent_type} - Sistema BMAD*
'''
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def create_error_patterns_template(self, agent_type: str) -> str:
        """Template para padrões de erro"""
        return '''[
  {
    "error": "Example error pattern",
    "correction": "Example correction",
    "pattern": "error_description",
    "tag": "error-type"
  }
]'''
    
    def create_quality_patterns_template(self, agent_type: str) -> str:
        """Template para padrões de qualidade"""
        return '''[
  {
    "pattern": "quality_pattern",
    "description": "Description of quality pattern",
    "severity": "medium",
    "fix": "How to fix"
  }
]'''
    
    def create_context_patterns_template(self, agent_type: str) -> str:
        """Template para padrões de contexto"""
        return '''[
  {
    "context": "development_context",
    "keywords": ["keyword1", "keyword2"],
    "agents": ["agent_name"],
    "workflow": "workflow_name"
  }
]'''
    
    def create_config_template(self, agent_type: str) -> str:
        """Template para configuração"""
        return '''{
  "agent_type": "''' + agent_type + '''",
  "version": "1.0",
  "description": "''' + agent_type + ''' development agent",
  "capabilities": ["analysis", "optimization", "validation"],
  "settings": {
    "auto_analyze": true,
    "auto_optimize": false,
    "log_level": "info"
  }
}'''
    
    def create_best_practices_template(self, agent_type: str) -> str:
        """Template para melhores práticas"""
        return f'''# Melhores Práticas - Agente {agent_type.title()}

## 📋 Práticas Recomendadas

### 1. Estrutura de Código
- Mantenha estrutura consistente
- Use padrões estabelecidos
- Documente adequadamente

### 2. Qualidade
- Siga padrões de qualidade
- Implemente validações
- Mantenha logs detalhados

### 3. Performance
- Otimize quando necessário
- Monitore performance
- Implemente cache quando apropriado

---
*Melhores práticas para desenvolvimento {agent_type}*
'''
    
    def create_common_errors_template(self, agent_type: str) -> str:
        """Template para erros comuns"""
        return f'''# Erros Comuns - Agente {agent_type.title()}

## 🐛 Erros Frequentes

### 1. Erro de Sintaxe
**Descrição**: Erro de sintaxe comum
**Solução**: Corrigir sintaxe

### 2. Erro de Import
**Descrição**: Import não encontrado
**Solução**: Verificar imports

### 3. Erro de Configuração
**Descrição**: Configuração incorreta
**Solução**: Verificar configurações

---
*Erros comuns em desenvolvimento {agent_type}*
'''
    
    def create_optimization_tips_template(self, agent_type: str) -> str:
        """Template para dicas de otimização"""
        return f'''# Dicas de Otimização - Agente {agent_type.title()}

## ⚡ Otimizações Recomendadas

### 1. Performance
- Use algoritmos eficientes
- Implemente cache
- Otimize loops

### 2. Memória
- Gerencie memória adequadamente
- Evite vazamentos
- Use estruturas apropriadas

### 3. Código
- Refatore quando necessário
- Mantenha código limpo
- Use padrões estabelecidos

---
*Dicas para otimização {agent_type}*
'''
    
    def create_integration_guide_template(self, agent_type: str) -> str:
        """Template para guia de integração"""
        return f'''# Guia de Integração - Agente {agent_type.title()}

## 🔗 Integração com Sistema

### 1. Orquestrador
- Configure padrões de contexto
- Defina workflows específicos
- Integre com outros agentes

### 2. BMAD
- Siga estrutura BMAD
- Use templates padrão
- Mantenha documentação

### 3. Logs
- Configure logs adequados
- Mantenha histórico
- Gere relatórios

---
*Guia de integração para agente {agent_type}*
'''
    
    def create_analyzer_template(self, agent_type: str) -> str:
        """Template para analisador"""
        return f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analisador para Agente {agent_type.title()}
"""

def analyze_{agent_type}_code(target: str) -> dict:
    """Analisa código {agent_type}"""
    return {{"status": "success", "analysis": "Implementar análise"}}

if __name__ == "__main__":
    result = analyze_{agent_type}_code("test_target")
    print(result)
'''
    
    def create_optimizer_template(self, agent_type: str) -> str:
        """Template para otimizador"""
        return f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Otimizador para Agente {agent_type.title()}
"""

def optimize_{agent_type}_code(target: str) -> dict:
    """Otimiza código {agent_type}"""
    return {{"status": "success", "optimization": "Implementar otimização"}}

if __name__ == "__main__":
    result = optimize_{agent_type}_code("test_target")
    print(result)
'''
    
    def create_validator_template(self, agent_type: str) -> str:
        """Template para validador"""
        return f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validador para Agente {agent_type.title()}
"""

def validate_{agent_type}_code(target: str) -> dict:
    """Valida código {agent_type}"""
    return {{"status": "success", "validation": "Implementar validação"}}

if __name__ == "__main__":
    result = validate_{agent_type}_code("test_target")
    print(result)
'''
    
    def create_test_template(self, agent_type: str) -> str:
        """Template para teste"""
        return f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste para Agente {agent_type.title()}
"""

def test_{agent_type}_agent():
    """Testa funcionalidades do agente {agent_type}"""
    print("🧪 Testando agente {agent_type}")
    return True

if __name__ == "__main__":
    test_{agent_type}_agent()
'''
    
    def migrate_agent(self, agent_info: Dict[str, Any]) -> bool:
        """Migra agente para estrutura BMAD"""
        print(f"🔄 Migrando agente: {agent_info['name']}")
        
        # Criar estrutura BMAD
        bmad_agent_path = self.create_bmad_agent_structure(
            agent_info['name'], 
            agent_info['type']
        )
        
        # Migrar arquivos existentes
        source_path = Path(agent_info['path'])
        
        # Mapear arquivos para nova estrutura
        file_mapping = self.map_files_to_structure(agent_info['structure'])
        
        # Copiar arquivos
        for old_path, new_path in file_mapping.items():
            old_file = source_path / old_path
            new_file = bmad_agent_path / new_path
            
            if old_file.exists():
                # Criar diretório se necessário
                new_file.parent.mkdir(parents=True, exist_ok=True)
                
                # Copiar arquivo
                shutil.copy2(old_file, new_file)
                print(f"  ✅ Copiado: {old_path} → {new_path}")
        
        # Remover estrutura antiga
        shutil.rmtree(source_path)
        print(f"  🗑️ Removida estrutura antiga: {source_path}")
        
        return True
    
    def map_files_to_structure(self, structure: Dict[str, Any]) -> Dict[str, str]:
        """Mapeia arquivos para nova estrutura BMAD"""
        mapping = {}
        
        for file_path in structure['files']:
            file_name = Path(file_path).name
            
            # Mapear baseado no nome e tipo
            if "agent" in file_name.lower() and file_name.endswith(".py"):
                mapping[file_path] = f"{file_name}"
            elif "pattern" in file_name.lower():
                mapping[file_path] = f"patterns/{file_name}"
            elif "script" in file_name.lower() or "analyzer" in file_name.lower():
                mapping[file_path] = f"scripts/{file_name}"
            elif "knowledge" in file_name.lower() or "practice" in file_name.lower():
                mapping[file_path] = f"knowledge/{file_name}"
            elif "test" in file_name.lower():
                mapping[file_path] = f"tests/{file_name}"
            elif "config" in file_name.lower():
                mapping[file_path] = f"config/{file_name}"
            else:
                mapping[file_path] = f"docs/{file_name}"
        
        return mapping
    
    def update_bmad_documentation(self):
        """Atualiza documentação BMAD"""
        print("📝 Atualizando documentação BMAD...")
        
        # Atualizar BMAD_Agents_Guide.md
        agents_guide = self.bmad_path / "agents" / "BMAD_Agents_Guide.md"
        if agents_guide.exists():
            self.update_agents_guide(agents_guide)
        
        print("✅ Documentação BMAD atualizada")
    
    def update_agents_guide(self, guide_path: Path):
        """Atualiza guia de agentes"""
        # Listar agentes existentes
        agents = []
        for agent_dir in self.agents_path.iterdir():
            if agent_dir.is_dir() and agent_dir.name != "__pycache__":
                agents.append(agent_dir.name)
        
        # Criar conteúdo atualizado
        content = f"""# BMAD Agents Guide

## 📋 Agentes Disponíveis

"""
        
        for agent in sorted(agents):
            agent_name = agent.replace('_', ' ').title()
            content += f"""### {agent_name}

- **Pasta**: `{agent}`
- **Tipo**: Agente especializado
- **Documentação**: [{agent}/README.md]({agent}/README.md)

"""
        
        content += """## 🚀 Como Usar

Cada agente possui sua própria documentação e exemplos de uso.

## 📁 Estrutura Padrão

Todos os agentes seguem a estrutura padrão BMAD:

```
agent_name/
├── agent_name.py              # Implementação principal
├── patterns/                  # Padrões específicos
├── scripts/                   # Scripts auxiliares
├── knowledge/                 # Base de conhecimento
├── logs/                      # Logs específicos
├── tests/                     # Testes
├── docs/                      # Documentação
└── config/                    # Configurações
```

---
*Guia dos Agentes BMAD - Atualizado automaticamente*
"""
        
        with open(guide_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def organize_all_agents(self) -> Dict[str, Any]:
        """Organiza todos os agentes automaticamente"""
        print("🤖 ORGANIZADOR AUTOMÁTICO DE AGENTES")
        print("=" * 50)
        
        # Detectar agentes existentes
        existing_agents = self.detect_existing_agents()
        
        if not existing_agents:
            print("✅ Nenhum agente encontrado para organização")
            return {"status": "success", "message": "Nenhum agente para organizar"}
        
        # Migrar cada agente
        migrated_agents = []
        for agent in existing_agents:
            try:
                success = self.migrate_agent(agent)
                if success:
                    migrated_agents.append(agent['name'])
            except Exception as e:
                print(f"❌ Erro ao migrar {agent['name']}: {e}")
        
        # Atualizar documentação
        self.update_bmad_documentation()
        
        # Relatório final
        report = {
            "status": "success",
            "timestamp": datetime.now().isoformat(),
            "agents_migrated": migrated_agents,
            "total_agents": len(existing_agents),
            "successful_migrations": len(migrated_agents)
        }
        
        print(f"\n📊 RELATÓRIO FINAL")
        print(f"✅ Agentes migrados: {len(migrated_agents)}/{len(existing_agents)}")
        print(f"📁 Estrutura BMAD atualizada")
        print(f"📝 Documentação atualizada")
        
        return report

def main():
    """Função principal"""
    organizer = AgentOrganizer()
    report = organizer.organize_all_agents()
    
    # Salvar relatório
    report_file = Path("wiki/log/reports/agent_organization_report.json")
    report_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"📋 Relatório salvo: {report_file}")

if __name__ == "__main__":
    main() 