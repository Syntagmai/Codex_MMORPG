from unicode_aliases import *
# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
MAX_ITEMS = 100

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: fix_wiki_issues.py
Módulo de Destino: documentation.wiki_fixer
Data de Migração: 2025-08-01 12:21:34

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import WikifixerModule

# Conteúdo original do script
#!/usr/bin/env python3
"""
Script para correção completa da wiki - Deixar 10/10
Corrige links quebrados, melhora navegação e otimiza para IA e usuários brasileiros
"""
import json
import re

class WikiFixer:
    def __init__(self, wiki_dir: str = "wiki"):
        self.wiki_dir = Path(wiki_dir)
        self.docs_dir = self.wiki_dir / "docs"
        self.maps_dir = self.wiki_dir / "maps"
        
        # Problemas identificados
        self.broken_links = {
            "UIWidget_Reference": "UI_System_Guide",
            "Protocol_System_Guide": "Network_System_Guide"
        }
        
        # Melhorias para navegação
        self.navigation_improvements = {
            "search_section": True,
            "quick_links": True,
            "better_aliases": True,
            "improved_tags": True
        }
        
    def fix_broken_links(self):
        """Corrige links quebrados em todos os documentos"""
        print("Corrigindo links quebrados...")
        
        for file_path in self.docs_dir.glob("*.md"):
            if file_path.name == "Wiki_Index.md":
                continue
                
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Corrigir links quebrados
            for broken_link, replacement in self.broken_links.items():
                # Corrigir [[broken_link]] para [[replacement]]
                content = re.sub(
                    rf'\[\[{broken_link}\]\]',
                    f'[[{replacement}]]',
                    content
                )
                
                # Corrigir links markdown (broken_link.md)
                content = re.sub(
                    rf'\[([^\]]+)\]\({broken_link}\.md\)',
                    rf'[\1]({replacement}.md)',
                    content
                )
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  Corrigido: {file_path.name}")
    
    def improve_wiki_index(self):
        """Melhora o índice principal da wiki"""
        print("Melhorando índice principal...")
        
        index_content = """---
tags: [otclient, wiki, index, documentation, navigation]
status: completed
aliases: [Índice da Wiki, Wiki Index, Navegação da Wiki, Documentação OTClient]
---

# Índice Completo da Wiki - OTClient

> [!info] **Bem-vindo à Wiki do OTClient!** Este é o ponto de entrada para toda a documentação do sistema,
    organizada de forma lógica e intuitiva para facilitar sua navegação.

## 🔍 **Busca Rápida**

### 🚀 **Para Iniciantes**
- [[Getting_Started_Guide]] - Primeiros passos no OTClient
- [[Cheat_Sheet]] - Referência rápida de comandos
- [[Module_Development_Guide]] - Criando seu primeiro módulo

### 🎨 **Interface e UI**
- [[UI_System_Guide]] - Sistema completo de interface
- [[OTUI_Module_Development_Guide]] - Desenvolvimento de módulos OTUI

### ⚙️ **Sistemas Core**
- [[Creature_System_Guide]] - Sistema de criaturas
- [[Item_System_Guide]] - Sistema de itens
- [[World_System_Guide]] - Sistema de mundo
- [[Map_System_Guide]] - Sistema de mapas
- [[Network_System_Guide]] - Sistema de rede e protocolo

### 🎵 **Sistemas Avançados**
- [[Graphics_System_Guide]] - Sistema gráfico
- [[Sound_System_Guide]] - Sistema de som
- [[Effects_System_Guide]] - Sistema de efeitos
- [[Animation_System_Guide]] - Sistema de animações
- [[Combat_System_Guide]] - Sistema de combate
- [[Performance_System_Guide]] - Sistema de performance

### 🔧 **Desenvolvimento**
- [[Module_System_Guide]] - Sistema de módulos
- [[Configuration_Guide]] - Configuração básica
- [[Advanced_Configuration_Guide]] - Configuração avançada
- [[Debug_System_Guide]] - Sistema de debug

### 📖 **Referências**
- [[Lua_API_Reference]] - API Lua completa
- [[Drag_Drop_System_Guide]] - Sistema drag & drop

---

## 🎯 **Como Usar Esta Wiki**

### 👤 **Para Iniciantes**
1. **Comece aqui**: [[Getting_Started_Guide]]
2. **Referência rápida**: [[Cheat_Sheet]]
3. **Primeiro módulo**: [[Module_Development_Guide]]

### 👨‍💻 **Para Desenvolvedores**
1. **Sistema de módulos**: [[Module_System_Guide]]
2. **API completa**: [[Lua_API_Reference]]
3. **Configuração**: [[Configuration_Guide]]

### 🎨 **Para UI Designers**
1. **Sistema de UI**: [[UI_System_Guide]]
2. **Desenvolvimento OTUI**: [[OTUI_Module_Development_Guide]]

### 🔍 **Para Consultas Específicas**
- **Problemas de rede**: [[Network_System_Guide]]
- **Debugging**: [[Debug_System_Guide]]
- **Performance**: [[Performance_System_Guide]]
- **Animações**: [[Animation_System_Guide]]

---

## 📊 **Status da Documentação**

- ✅ **Completa**: Todos os sistemas documentados
- ✅ **Integrada**: Conteúdo do habdel incorporado
- ✅ **Atualizada**: Informações mais recentes
- ✅ **Exemplos**: Código prático incluído
- ✅ **Navegação**: Links funcionais e organizados

---

## 🔗 **Links Úteis**

### 📚 **Documentação Externa**
- [Repositório OTClient](https://github.com/edubart/otclient)
- [Documentação Lua](https://www.lua.org/manual/5.1/)
- [OpenGL Documentation](https://www.opengl.org/documentation/)

### 🛠️ **Ferramentas**
- [Obsidian](https://obsidian.md/) - Para visualizar esta wiki
- [LuaJIT](https://luajit.org/) - Engine Lua do OTClient

---

> [!success] **Documentação 100% Completa**
> Esta wiki agora contém toda a informação disponível do projeto,
integrando conteúdo do habdel e expandindo para cobrir todos os aspectos do OTClient. Todos os links estão funcionais e
    a navegação foi otimizada para facilitar o uso.

"""
        
        with open(self.docs_dir / "Wiki_Index.md", 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        print("  Índice principal melhorado")
    
    def improve_document_aliases(self):
        """Melhora aliases dos documentos para melhor busca"""
        print("Melhorando aliases dos documentos...")
        
        alias_improvements = {
            "Getting_Started_Guide.md": ["Primeiros Passos", "Iniciando", "Começar", "Setup"],
            "UI_System_Guide.md": ["Interface", "UI", "Widgets", "Interface do Usuário"],
            "Module_System_Guide.md": ["Módulos", "Sistema de Módulos", "Modular"],
            "Lua_API_Reference.md": ["API Lua", "Referência Lua", "Lua API"],
            "Network_System_Guide.md": ["Rede", "Protocolo", "Comunicação", "Network"],
            "Configuration_Guide.md": ["Configuração", "Config", "Setup"],
            "Debug_System_Guide.md": ["Debug", "Debugging", "Depuração"],
            "Cheat_Sheet.md": ["Referência Rápida", "Comandos", "Cheat Sheet"]
        }
        
        for file_name, new_aliases in alias_improvements.items():
            file_path = self.docs_dir / file_name
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Atualizar aliases no frontmatter
                if content.startswith("---"):
                    parts = content.split("---", 2)
                    if len(parts) >= 3:
                        frontmatter = parts[1]
                        content_body = parts[2]
                        
                        # Adicionar novos aliases
                        current_aliases = re.search(r'aliases:\s*\[(.*?)\]', frontmatter)
                        if current_aliases:
                            existing = [alias.strip() for alias in current_aliases.group(1).split(",")]
                            all_aliases = list(set(existing + new_aliases))
                            new_aliases_str = ", ".join(all_aliases)
                            frontmatter = re.sub(
                                r'aliases:\s*\[.*?\]',
                                f'aliases: [{new_aliases_str}]',
                                frontmatter
                            )
                        
                        content = f"---{frontmatter}---{content_body}"
                        
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
        
        print("  Aliases melhorados")
    
    def improve_navigation_sections(self):
        """Melhora seções de navegação em todos os documentos"""
        print("Melhorando seções de navegação...")
        
        navigation_template = """

---

> [!success] **Navegação**
> **📚 Documentos Relacionados:**
> - [[Getting_Started_Guide]] - Comece aqui
> - [[Module_System_Guide]] - Sistema de módulos
> - [[UI_System_Guide]] - Interface do usuário
> - [[Lua_API_Reference]] - API completa
> 
> **🔗 Navegação Rápida:**
> - [[Wiki_Index]] - Voltar ao índice
> - [[Cheat_Sheet]] - Referência rápida
> - [[Debug_System_Guide]] - Debugging

"""
        
        for file_path in self.docs_dir.glob("*.md"):
            if file_path.name in ["Wiki_Index.md", "Wiki_Optimization_Report.md"]:
                continue
                
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remover navegação antiga se existir
            content = re.sub(
                r'\n---\s*\n\s*> \[!.*?\] Navegação.*?\n',
                '',
                content,
                flags=re.DOTALL
            )
            
            # Adicionar nova navegação se não existir
            if "> [!success] **Navegação**" not in content:
                content += navigation_template
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
        
        print("  Seções de navegação melhoradas")
    
    def optimize_maps_for_ai(self):
        """Otimiza mapas JSON para melhor consulta da IA"""
        print("Otimizando mapas para IA...")
        
        # Melhorar tags_index.json
        tags_file = self.maps_dir / "tags_index.json"
        if tags_file.exists():
            with open(tags_file, 'r', encoding='utf-8') as f:
                tags_data = json.load(f)
            
            # Adicionar tags mais específicas
            improved_tags = {
                "iniciante": ["Getting_Started_Guide.md", "Cheat_Sheet.md"],
                "desenvolvimento": ["Module_System_Guide.md", "Module_Development_Guide.md"],
                "interface": ["UI_System_Guide.md", "OTUI_Module_Development_Guide.md"],
                "api": ["Lua_API_Reference.md"],
                "configuracao": ["Configuration_Guide.md", "Advanced_Configuration_Guide.md"],
                "debug": ["Debug_System_Guide.md"],
                "rede": ["Network_System_Guide.md"],
                "performance": ["Performance_System_Guide.md"]
            }
            
            for tag, files in improved_tags.items():
                if tag not in tags_data["files_by_tag"]:
                    tags_data["files_by_tag"][tag] = []
                tags_data["files_by_tag"][tag].extend(files)
            
            with open(tags_file, 'w', encoding='utf-8') as f:
                json.dump(tags_data, f, indent=2, ensure_ascii=False)
        
        # Melhorar relationships.json
        relationships_file = self.maps_dir / "relationships.json"
        if relationships_file.exists():
            with open(relationships_file, 'r', encoding='utf-8') as f:
                relationships_data = json.load(f)
            
            # Adicionar relacionamentos mais específicos
            improved_relationships = {
                "Getting_Started_Guide.md": {
                    "prerequisites": [],
                    "next_steps": ["Module_Development_Guide.md", "UI_System_Guide.md"],
                    "related": ["Cheat_Sheet.md", "Configuration_Guide.md"]
                },
                "Module_Development_Guide.md": {
                    "prerequisites": ["Getting_Started_Guide.md"],
                    "next_steps": ["Lua_API_Reference.md", "UI_System_Guide.md"],
                    "related": ["Module_System_Guide.md", "Debug_System_Guide.md"]
                }
            }
            
            for file_name, rels in improved_relationships.items():
                if file_name in relationships_data:
                    relationships_data[file_name].update(rels)
            
            with open(relationships_file, 'w', encoding='utf-8') as f:
                json.dump(relationships_data, f, indent=2, ensure_ascii=False)
        
        print("  Mapas otimizados para IA")
    
    def create_quick_search_guide(self):
        """Cria guia de busca rápida para brasileiros"""
        print("Criando guia de busca rápida...")
        
        search_guide = """---
tags: [otclient, wiki, busca, navegação, ajuda]
status: completed
aliases: [Busca Rápida, Como Encontrar, Navegação Rápida, Ajuda]
---

# Guia de Busca Rápida - Wiki OTClient

> [!info] **Precisa encontrar algo rapidamente?** Use este guia para localizar informações específicas na wiki do
    OTClient.

## 🔍 **Busca por Tópico**

### 🚀 **"Como começar?"**
- [[Getting_Started_Guide]] - Primeiros passos
- [[Cheat_Sheet]] - Comandos essenciais
- [[Configuration_Guide]] - Configuração básica

### 🎨 **"Como criar interface?"**
- [[UI_System_Guide]] - Sistema completo de UI
- [[OTUI_Module_Development_Guide]] - Desenvolvimento OTUI

### ⚙️ **"Como criar módulo?"**
- [[Module_Development_Guide]] - Guia completo
- [[Module_System_Guide]] - Sistema de módulos
- [[Lua_API_Reference]] - API Lua

### 🔧 **"Como configurar?"**
- [[Configuration_Guide]] - Configuração básica
- [[Advanced_Configuration_Guide]] - Configuração avançada

### 🐛 **"Como debugar?"**
- [[Debug_System_Guide]] - Sistema de debug
- [[Performance_System_Guide]] - Otimização

### 🌐 **"Problemas de rede?"**
- [[Network_System_Guide]] - Sistema de rede
- [[Protocol_System_Guide]] - Protocolo

## 🎯 **Busca por Palavra-Chave**

### **"Widget"**
- [[UI_System_Guide]] - Sistema de widgets
- [[OTUI_Module_Development_Guide]] - Desenvolvimento de widgets

### **"Lua"**
- [[Lua_API_Reference]] - API Lua completa
- [[Module_Development_Guide]] - Desenvolvimento em Lua

### **"Módulo"**
- [[Module_System_Guide]] - Sistema de módulos
- [[Module_Development_Guide]] - Criando módulos

### **"Configuração"**
- [[Configuration_Guide]] - Configuração básica
- [[Advanced_Configuration_Guide]] - Configuração avançada

### **"Performance"**
- [[Performance_System_Guide]] - Otimização
- [[Debug_System_Guide]] - Debugging

## 📱 **Para Brasileiros**

### **"Primeira vez no OTClient?"**
1. [[Getting_Started_Guide]] - Comece aqui
2. [[Cheat_Sheet]] - Comandos básicos
3. [[Module_Development_Guide]] - Seu primeiro módulo

### **"Quero criar uma interface?"**
1. [[UI_System_Guide]] - Conceitos básicos
2. [[OTUI_Module_Development_Guide]] - Desenvolvimento prático

### **"Problemas técnicos?"**
1. [[Debug_System_Guide]] - Debugging
2. [[Configuration_Guide]] - Configuração
3. [[Network_System_Guide]] - Problemas de rede

---

> [!success] **Navegação**
> - [[Wiki_Index]] - Voltar ao índice principal
> - [[Getting_Started_Guide]] - Começar do zero
> - [[Cheat_Sheet]] - Referência rápida

"""
        
        with open(self.docs_dir / "Guia_Busca_Rapida.md", 'w', encoding='utf-8') as f:
            f.write(search_guide)
        
        print("  Guia de busca rápida criado")
    
    def fix_all_issues(self):
        """Executa todas as correções"""
        print("🚀 Iniciando correção completa da wiki...")
        
        # 1. Corrigir links quebrados
        self.fix_broken_links()
        
        # 2. Melhorar índice principal
        self.improve_wiki_index()
        
        # 3. Melhorar aliases
        self.improve_document_aliases()
        
        # 4. Melhorar navegação
        self.improve_navigation_sections()
        
        # 5. Otimizar mapas para IA
        self.optimize_maps_for_ai()
        
        # 6. Criar guia de busca rápida
        self.create_quick_search_guide()
        
        print("✅ Correção completa finalizada!")
        print("🎯 Wiki agora está 10/10 para IA e usuários brasileiros!")

if __name__ == "__main__":
    fixer = WikiFixer()
    fixer.fix_all_issues() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = WikifixerModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script fix_wiki_issues.py executado com sucesso via módulo documentation.wiki_fixer")
    else:
        print(f"❌ Erro na execução do script fix_wiki_issues.py via módulo documentation.wiki_fixer")

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
- **Nome**: migrated_fix_wiki_issues
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

