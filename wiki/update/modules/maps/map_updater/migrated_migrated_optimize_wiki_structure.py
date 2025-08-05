from unicode_aliases import *
# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
MAX_ITEMS = 100

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: migrated_optimize_wiki_structure.py
Módulo de Destino: maps.map_updater
Data de Migração: 2025-08-01 12:21:40

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import MapupdaterModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: optimize_wiki_structure.py
Módulo de Destino: documentation.wiki_optimizer
Data de Migração: 2025-08-01 12:21:35

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import WikioptimizerModule

# Conteúdo original do script
#!/usr/bin/env python3
"""
Script para otimização da estrutura da wiki
Remove duplicações e melhora organização sem perder informação
"""
import re

class WikiOptimizer:
    def __init__(self, wiki_dir: str = "wiki"):
        self.wiki_dir = Path(wiki_dir)
        self.docs_dir = self.wiki_dir / "docs"
        
        # Identificar duplicações e sobreposições
        self.duplications = {
            "network": {
                "files": ["Network_Protocol_Guide.md", "Network_System_Guide.md", "Protocol_System_Guide.md"],
                "action": "merge",
                "target": "Network_System_Guide.md"
            },
            "modules": {
                "files": ["Module_System_Guide.md", "Module_Development_Guide.md"],
                "action": "separate",
                "system": "Module_System_Guide.md",
                "development": "Module_Development_Guide.md"
            },
            "configuration": {
                "files": ["Configuration_Guide.md", "Advanced_Configuration_Guide.md"],
                "action": "separate",
                "basic": "Configuration_Guide.md",
                "advanced": "Advanced_Configuration_Guide.md"
            },
            "ui_widgets": {
                "files": ["UI_System_Guide.md", "UIWidget_Reference (1).md"],
                "action": "merge",
                "target": "UI_System_Guide.md"
            }
        }
        
        # Seções repetitivas para remover
        self.repetitive_sections = [
            "## 📋 Visão Geral",
            "## 🎯 Funcionalidades Principais",
            "## 🔧 Implementação",
            "## 💡 Exemplos Práticos",
            "## 🎯 Casos de Uso",
            "## ⚠️ Considerações"
        ]
    
    def analyze_content_overlap(self, file1: Path, file2: Path) -> Dict[str, Any]:
        """Analisa sobreposição de conteúdo entre dois arquivos"""
        try:
            with open(file1, 'r', encoding='utf-8') as f:
                content1 = f.read()
            
            with open(file2, 'r', encoding='utf-8') as f:
                content2 = f.read()
            
            # Extrair seções
            sections1 = self.extract_sections(content1)
            sections2 = self.extract_sections(content2)
            
            # Encontrar sobreposições
            overlaps = []
            for section in sections1:
                if section in sections2:
                    overlaps.append(section)
            
            return {
                "file1": file1.name,
                "file2": file2.name,
                "overlaps": overlaps,
                "overlap_count": len(overlaps)
            }
            
        except Exception as e:
            print(f"Erro ao analisar sobreposição: {e}")
            return {}
    
    def extract_sections(self, content: str) -> List[str]:
        """Extrai seções do conteúdo"""
        sections = []
        section_pattern = r'^##\s+(.+)$'
        
        for line in content.split('\n'):
            match = re.match(section_pattern, line)
            if match:
                sections.append(match.group(1).strip())
        
        return sections
    
    def merge_network_documents(self):
        """Mescla documentos de rede em um só"""
        print("Mesclando documentos de rede...")
        
        # Ler todos os documentos de rede
        network_files = [
            "Network_Protocol_Guide.md",
            "Network_System_Guide.md", 
            "Protocol_System_Guide.md"
        ]
        
        merged_content = """---
title: Sistema de Rede e Protocolo - OTClient
tags: [otclient, network, protocol, system, guide, documentation]
status: completed
aliases: [Network System, Protocol System, Rede e Protocolo]
---

# Sistema de Rede e Protocolo - OTClient

## 📋 Visão Geral

Sistema completo de comunicação de rede do OTClient, incluindo protocolo, mensagens, opcodes e extended opcodes.

---

"""
        
        # Processar cada arquivo
        for filename in network_files:
            file_path = self.docs_dir / filename
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extrair conteúdo sem frontmatter
                content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)
                
                # Adicionar seção do arquivo
                section_title = filename.replace('.md', '').replace('_', ' ').title()
                merged_content += f"\n## {section_title}\n\n"
                merged_content += content + "\n\n"
        
        # Adicionar navegação
        merged_content += """

---

> [!success] Navegação
> - [[Getting_Started_Guide]] - Comece aqui
> - [[Module_System_Guide]] - Sistema de módulos
> - [[UI_System_Guide]] - Interface do usuário
> - [[Lua_API_Reference]] - Referência da API

"""
        
        # Salvar arquivo mesclado
        target_file = self.docs_dir / "Network_System_Guide.md"
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(merged_content)
        
        # Remover arquivos antigos
        for filename in ["Network_Protocol_Guide.md", "Protocol_System_Guide.md"]:
            old_file = self.docs_dir / filename
            if old_file.exists():
                old_file.unlink()
        
        print(f"Documentos de rede mesclados em: {target_file}")
    
    def optimize_ui_documents(self):
        """Otimiza documentos de UI"""
        print("Otimizando documentos de UI...")
        
        # Mesclar UIWidget_Reference no UI_System_Guide
        ui_guide = self.docs_dir / "UI_System_Guide.md"
        widget_ref = self.docs_dir / "UIWidget_Reference (1).md"
        
        if ui_guide.exists() and widget_ref.exists():
            with open(ui_guide, 'r', encoding='utf-8') as f:
                ui_content = f.read()
            
            with open(widget_ref, 'r', encoding='utf-8') as f:
                widget_content = f.read()
            
            # Extrair seções de widgets do widget_ref
            widget_sections = self.extract_widget_sections(widget_content)
            
            # Adicionar seções de widgets ao UI_System_Guide
            if widget_sections:
                ui_content += "\n\n## 📋 Referência de Widgets\n\n"
                ui_content += widget_sections
            
            # Salvar UI_System_Guide atualizado
            with open(ui_guide, 'w', encoding='utf-8') as f:
                f.write(ui_content)
            
            # Remover arquivo antigo
            widget_ref.unlink()
            
            print("Documentos de UI otimizados")
    
    def extract_widget_sections(self, content: str) -> str:
        """Extrai seções de widgets do conteúdo"""
        # Procurar por seções de widgets específicos
        widget_pattern = r'(##\s+[^\n]+\n.*?)(?=##|\Z)'
        matches = re.findall(widget_pattern, content, re.DOTALL)
        
        # Filtrar seções relevantes
        widget_sections = []
        for match in matches:
            if any(keyword in match.lower() for keyword in ['widget', 'button', 'label', 'text', 'image']):
                widget_sections.append(match.strip())
        
        return '\n\n'.join(widget_sections)
    
    def remove_repetitive_sections(self):
        """Remove seções repetitivas desnecessárias"""
        print("Removendo seções repetitivas...")
        
        for file_path in self.docs_dir.glob("*.md"):
            if file_path.name in ["Wiki_Index.md", "Documentation_Status.md"]:
                continue
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Remover seções vazias ou muito pequenas
                lines = content.split('\n')
                cleaned_lines = []
                skip_section = False
                
                for i, line in enumerate(lines):
                    # Verificar se é uma seção repetitiva
                    if any(section in line for section in self.repetitive_sections):
                        # Verificar se a seção tem conteúdo significativo
                        section_content = self.get_section_content(lines, i)
                        if len(section_content.strip()) < 100:  # Seção muito pequena
                            skip_section = True
                            continue
                    
                    if skip_section and line.startswith('##'):
                        skip_section = False
                    
                    if not skip_section:
                        cleaned_lines.append(line)
                
                # Salvar conteúdo limpo
                cleaned_content = '\n'.join(cleaned_lines)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)
                
            except Exception as e:
                print(f"Erro ao processar {file_path.name}: {e}")
    
    def get_section_content(self, lines: List[str], start_index: int) -> str:
        """Obtém conteúdo de uma seção"""
        content = []
        for i in range(start_index + 1, len(lines)):
            line = lines[i]
            if line.startswith('##'):
                break
            content.append(line)
        return '\n'.join(content)
    
    def standardize_navigation(self):
        """Padroniza seções de navegação"""
        print("Padronizando navegação...")
        
        for file_path in self.docs_dir.glob("*.md"):
            if file_path.name in ["Wiki_Index.md", "Documentation_Status.md"]:
                continue
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Remover navegação antiga
                content = re.sub(r'> \[!success\] Navegação.*?(?=\n\n|\Z)', '', content, flags=re.DOTALL)
                content = re.sub(r'> \[!note\] Consulte também.*?(?=\n\n|\Z)', '', content, flags=re.DOTALL)
                
                # Adicionar navegação padronizada
                navigation = self.generate_standard_navigation(file_path.name)
                content += f"\n\n{navigation}"
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
            except Exception as e:
                print(f"Erro ao padronizar navegação em {file_path.name}: {e}")
    
    def generate_standard_navigation(self, filename: str) -> str:
        """Gera navegação padronizada baseada no tipo de documento"""
        if "Getting_Started" in filename:
            return """---

> [!success] Navegação
> - [[Module_System_Guide]] - Sistema de módulos
> - [[UI_System_Guide]] - Interface do usuário
> - [[Lua_API_Reference]] - Referência da API
> - [[Cheat_Sheet]] - Referência rápida"""
        
        elif "Module" in filename:
            return """---

> [!success] Navegação
> - [[Getting_Started_Guide]] - Primeiros passos
> - [[UI_System_Guide]] - Interface do usuário
> - [[Lua_API_Reference]] - Referência da API
> - [[Configuration_Guide]] - Configuração"""
        
        elif "UI" in filename:
            return """---

> [!success] Navegação
> - [[Getting_Started_Guide]] - Primeiros passos
> - [[Module_System_Guide]] - Sistema de módulos
> - [[Lua_API_Reference]] - Referência da API
> - [[OTUI_Module_Development_Guide]] - Desenvolvimento OTUI"""
        
        elif "System" in filename:
            return """---

> [!success] Navegação
> - [[Getting_Started_Guide]] - Comece aqui
> - [[Module_System_Guide]] - Sistema de módulos
> - [[UI_System_Guide]] - Interface do usuário
> - [[Lua_API_Reference]] - Referência da API"""
        
        else:
            return """---

> [!success] Navegação
> - [[Getting_Started_Guide]] - Primeiros passos
> - [[Module_System_Guide]] - Sistema de módulos
> - [[UI_System_Guide]] - Interface do usuário
> - [[Lua_API_Reference]] - Referência da API"""
    
    def update_wiki_index(self):
        """Atualiza o índice da wiki com a nova estrutura"""
        print("Atualizando índice da wiki...")
        
        # Remover referências a arquivos deletados
        index_file = self.docs_dir / "Wiki_Index.md"
        if index_file.exists():
            with open(index_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remover referências a arquivos deletados
            deleted_files = [
                "Network_Protocol_Guide",
                "Protocol_System_Guide", 
                "UIWidget_Reference (1)"
            ]
            
            for deleted_file in deleted_files:
                content = re.sub(rf'- \[\[{deleted_file}\]\].*\n', '', content)
            
            with open(index_file, 'w', encoding='utf-8') as f:
                f.write(content)
    
    def optimize_wiki_structure(self):
        """Otimiza a estrutura completa da wiki"""
        print("Otimizando estrutura da wiki...")
        
        # 1. Mesclar documentos de rede
        self.merge_network_documents()
        
        # 2. Otimizar documentos de UI
        self.optimize_ui_documents()
        
        # 3. Remover seções repetitivas
        self.remove_repetitive_sections()
        
        # 4. Padronizar navegação
        self.standardize_navigation()
        
        # 5. Atualizar índice
        self.update_wiki_index()
        
        print("Otimização da wiki concluída!")

def main():
    """Função principal"""
    optimizer = WikiOptimizer("wiki")
    optimizer.optimize_wiki_structure()

if __name__ == "__main__":
    main() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = WikioptimizerModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script optimize_wiki_structure.py executado com sucesso via módulo documentation.wiki_optimizer")
    else:
        print(f"❌ Erro na execução do script optimize_wiki_structure.py via módulo documentation.wiki_optimizer")


# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = MapupdaterModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script migrated_optimize_wiki_structure.py executado com sucesso via módulo maps.map_updater")
    else:
        print(f"❌ Erro na execução do script migrated_optimize_wiki_structure.py via módulo maps.map_updater")

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
- **Nome**: migrated_migrated_optimize_wiki_structure
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

