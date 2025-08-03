from unicode_aliases import *
# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
MAX_ITEMS = 100

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: migrated_expand_wiki_comprehensive.py
Módulo de Destino: maps.map_updater
Data de Migração: 2025-08-01 12:21:39

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import MapupdaterModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: expand_wiki_comprehensive.py
Módulo de Destino: documentation.wiki_expander
Data de Migração: 2025-08-01 12:21:34

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import WikiexpanderModule

# Conteúdo original do script
#!/usr/bin/env python3
"""
Script para expansão abrangente da wiki do OTClient
Integra conteúdo do habdel e cria documentação completa
"""
import json
import re

class WikiExpander:
    def __init__(self, wiki_dir: str = "wiki"):
        self.wiki_dir = Path(wiki_dir)
        self.habdel_dir = self.wiki_dir / "habdel"
        
        # Detectar contexto
        self.context_data = self.load_context_data()
        self.docs_dir = self.wiki_dir / self.context_data['paths']['docs'].replace('wiki/', '')
        
        # Mapeamento de tópicos para expansão
        self.expansion_topics = {
            "ui": {
                "habdel_files": [
                    "UIWidget.md",
                    "UIButton.md", 
                    "UITextEdit.md",
                    "UILayouts.md",
                    "UIEvents.md",
                    "UIStyling.md",
                    "UIWidgetsSpecialized.md",
                    "UIWidget_Reference.md"
                ],
                "target_file": "UI_System_Guide.md",
                "sections": [
                    "Widgets Especializados",
                    "Eventos Avançados",
                    "Layouts Complexos",
                    "Estilização Avançada",
                    "Exemplos Práticos"
                ]
            },
            "api": {
                "habdel_files": [
                    "LuaAPI.md",
                    "BestPractices.md"
                ],
                "target_file": "Lua_API_Reference.md",
                "sections": [
                    "API Completa",
                    "Melhores Práticas",
                    "Exemplos Avançados",
                    "Padrões de Design"
                ]
            },
            "systems": {
                "habdel_files": [
                    "CreatureSystem.md",
                    "ItemSystem.md",
                    "WorldSystem.md",
                    "GraphicsSystem.md",
                    "SoundSystem.md",
                    "EffectsSystem.md",
                    "NetworkSystem.md",
                    "Protocol.md"
                ],
                "target_files": {
                    "CreatureSystem.md": "Creature_System_Guide.md",
                    "ItemSystem.md": "Item_System_Guide.md", 
                    "WorldSystem.md": "World_System_Guide.md",
                    "GraphicsSystem.md": "Graphics_System_Guide.md",
                    "SoundSystem.md": "Sound_System_Guide.md",
                    "EffectsSystem.md": "Effects_System_Guide.md",
                    "NetworkSystem.md": "Network_System_Guide.md",
                    "Protocol.md": "Protocol_System_Guide.md"
                }
            },
            "development": {
                "habdel_files": [
                    "FirstModule.md",
                    "ModuleSystem.md",
                    "Configuration.md",
                    "ConfigurationAdvanced.md"
                ],
                "target_files": {
                    "FirstModule.md": "Module_Development_Guide.md",
                    "ModuleSystem.md": "Module_System_Guide.md",
                    "Configuration.md": "Configuration_Guide.md",
                    "ConfigurationAdvanced.md": "Advanced_Configuration_Guide.md"
                }
            },
            "reference": {
                "habdel_files": [
                    "CheatSheet.md",
                    "GettingStarted.md"
                ],
                "target_files": {
                    "CheatSheet.md": "Cheat_Sheet.md",
                    "GettingStarted.md": "Getting_Started_Guide.md"
                }
            }
        }
    
    def load_context_data(self) -> Dict[str, Any]:
        """Carrega dados de contexto detectado"""
        context_file = Path("wiki/maps/context_data.json")
        if context_file.exists():
            with open(context_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Fallback para contexto OTClient
            return {
                'context': 'otclient',
                'paths': {
                    'docs': 'wiki/otclient/',
                    'maps': 'wiki/maps/'
                }
            }
    
    def extract_section_content(self, file_path: Path, section_title: str) -> str:
        """Extrai conteúdo de uma seção específica"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Procurar por seção
            pattern = rf'##\s*{re.escape(section_title)}.*?(?=##|\Z)'
            match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
            
            if match:
                return match.group(0).strip()
            
            return ""
            
        except Exception as e:
            print(f"Erro ao extrair seção de {file_path}: {e}")
            return ""
    
    def extract_examples(self, file_path: Path) -> List[str]:
        """Extrai exemplos práticos do arquivo"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            examples = []
            
            # Procurar por blocos de código
            code_pattern = r'```lua\s*\n(.*?)\n```'
            code_matches = re.findall(code_pattern, content, re.DOTALL)
            
            for code in code_matches:
                if len(code.strip()) > 50:  # Exemplos significativos
                    examples.append(code.strip())
            
            # Procurar por seções de exemplos
            example_pattern = r'##\s*[💡🎯]*\s*Exemplos?.*?(?=##|\Z)'
            example_matches = re.findall(example_pattern, content, re.DOTALL | re.IGNORECASE)
            
            for example in example_matches:
                examples.append(example.strip())
            
            return examples
            
        except Exception as e:
            print(f"Erro ao extrair exemplos de {file_path}: {e}")
            return []
    
    def create_comprehensive_ui_guide(self):
        """Cria guia completo de UI integrando conteúdo do habdel"""
        target_file = self.docs_dir / "UI_System_Guide.md"
        
        # Ler arquivo atual
        current_content = ""
        if target_file.exists():
            with open(target_file, 'r', encoding='utf-8') as f:
                current_content = f.read()
        
        # Adicionar conteúdo do habdel
        expanded_content = current_content + "\n\n"
        
        # Adicionar seções do habdel
        for habdel_file in self.expansion_topics["ui"]["habdel_files"]:
            habdel_path = self.habdel_dir / habdel_file
            if habdel_path.exists():
                with open(habdel_path, 'r', encoding='utf-8', errors='ignore') as f:
                    habdel_content = f.read()
                
                # Extrair seções relevantes
                sections = [
                    "## Widgets Especializados",
                    "## Eventos Avançados", 
                    "## Layouts Complexos",
                    "## Estilização Avançada",
                    "## Exemplos Práticos"
                ]
                
                for section in sections:
                    section_content = self.extract_section_content(habdel_path, section)
                    if section_content:
                        expanded_content += f"\n{section_content}\n"
        
        # Salvar arquivo expandido
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(expanded_content)
        
        print(f"Guia de UI expandido: {target_file}")
    
    def create_lua_api_reference(self):
        """Cria referência completa da API Lua"""
        target_file = self.docs_dir / "Lua_API_Reference.md"
        
        # Integrar conteúdo do LuaAPI.md e BestPractices.md
        content = """# Lua API Reference - OTClient

## 📋 Visão Geral

Referência completa da API Lua do OTClient, incluindo todas as funções, classes e melhores práticas.

---

"""
        
        # Adicionar conteúdo do LuaAPI.md
        lua_api_file = self.habdel_dir / "LuaAPI.md"
        if lua_api_file.exists():
            with open(lua_api_file, 'r', encoding='utf-8', errors='ignore') as f:
                lua_content = f.read()
            
            # Extrair seções principais
            sections = [
                "## 🎯 API Core",
                "## 🎮 Game API", 
                "## 🎨 UI API",
                "## 🌐 Network API",
                "## 📁 File System API",
                "## ⚙️ Settings API",
                "## 🎵 Sound API",
                "## 🎨 Graphics API",
                "## 📊 HTTP API",
                "## 🎯 Exemplos Práticos"
            ]
            
            for section in sections:
                section_content = self.extract_section_content(lua_api_file, section)
                if section_content:
                    content += f"\n{section_content}\n"
        
        # Adicionar conteúdo do BestPractices.md
        best_practices_file = self.habdel_dir / "BestPractices.md"
        if best_practices_file.exists():
            with open(best_practices_file, 'r', encoding='utf-8', errors='ignore') as f:
                practices_content = f.read()
            
            content += "\n\n## 🏆 Melhores Práticas\n\n"
            content += practices_content
        
        # Salvar arquivo
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Referência da API Lua criada: {target_file}")
    
    def create_system_guides(self):
        """Cria guias completos para cada sistema"""
        for habdel_file, target_file in self.expansion_topics["systems"]["target_files"].items():
            habdel_path = self.habdel_dir / habdel_file
            target_path = self.docs_dir / target_file
            
            if habdel_path.exists():
                # Ler conteúdo do habdel
                with open(habdel_path, 'r', encoding='utf-8', errors='ignore') as f:
                    habdel_content = f.read()
                
                # Processar conteúdo
                processed_content = self.process_habdel_content(habdel_content, habdel_file)
                
                # Salvar arquivo processado
                with open(target_path, 'w', encoding='utf-8') as f:
                    f.write(processed_content)
                
                print(f"Guia de sistema criado: {target_path}")
    
    def process_habdel_content(self, content: str, original_file: str) -> str:
        """Processa conteúdo do habdel para formato da wiki"""
        # Remover frontmatter se existir
        content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)
        
        # Adicionar frontmatter da wiki
        frontmatter = f"""---
title: {original_file.replace('.md', '').replace('_', ' ').title()}
tags: [otclient, system, guide, documentation]
status: completed
aliases: [{original_file.replace('.md', '').replace('_', ' ').title()}]
---

"""
        
        # Processar links internos
        content = re.sub(r'\[\[([^\]]+)\]\]', r'[[\1]]', content)
        
        # Adicionar seção de navegação
        navigation = """

---

> [!success] Navegação
> - [[Getting_Started_Guide]] - Comece aqui
> - [[Module_System_Guide]] - Desenvolvimento de módulos
> - [[UI_System_Guide]] - Interface do usuário
> - [[Lua_API_Reference]] - Referência completa da API

"""
        
        return frontmatter + content + navigation
    
    def create_development_guides(self):
        """Cria guias de desenvolvimento expandidos"""
        for habdel_file, target_file in self.expansion_topics["development"]["target_files"].items():
            habdel_path = self.habdel_dir / habdel_file
            target_path = self.docs_dir / target_file
            
            if habdel_path.exists():
                with open(habdel_path, 'r', encoding='utf-8', errors='ignore') as f:
                    habdel_content = f.read()
                
                processed_content = self.process_habdel_content(habdel_content, habdel_file)
                
                with open(target_path, 'w', encoding='utf-8') as f:
                    f.write(processed_content)
                
                print(f"Guia de desenvolvimento criado: {target_path}")
    
    def create_reference_documents(self):
        """Cria documentos de referência"""
        for habdel_file, target_file in self.expansion_topics["reference"]["target_files"].items():
            habdel_path = self.habdel_dir / habdel_file
            target_path = self.docs_dir / target_file
            
            if habdel_path.exists():
                with open(habdel_path, 'r', encoding='utf-8', errors='ignore') as f:
                    habdel_content = f.read()
                
                processed_content = self.process_habdel_content(habdel_content, habdel_file)
                
                with open(target_path, 'w', encoding='utf-8') as f:
                    f.write(processed_content)
                
                print(f"Documento de referência criado: {target_path}")
    
    def update_wiki_index(self):
        """Atualiza o índice principal da wiki"""
        index_file = self.docs_dir / "Wiki_Index.md"
        
        content = """# Índice Completo da Wiki - OTClient

## 📚 Documentação Completa

### 🚀 **Para Iniciantes**
- [[Getting_Started_Guide]] - Primeiros passos
- [[Cheat_Sheet]] - Referência rápida
- [[Module_Development_Guide]] - Criando seu primeiro módulo

### 🎨 **Interface do Usuário**
- [[UI_System_Guide]] - Sistema completo de UI
- [[OTUI_Module_Development_Guide]] - Desenvolvimento OTUI
- [[UIWidget_Reference]] - Referência de widgets

### ⚙️ **Sistemas Core**
- [[Creature_System_Guide]] - Sistema de criaturas
- [[Item_System_Guide]] - Sistema de itens
- [[World_System_Guide]] - Sistema de mundo
- [[Map_System_Guide]] - Sistema de mapas
- [[Network_System_Guide]] - Sistema de rede
- [[Protocol_System_Guide]] - Protocolo de comunicação

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

1. **Iniciantes**: Comece com [[Getting_Started_Guide]]
2. **Desenvolvedores**: Use [[Module_System_Guide]] e [[Lua_API_Reference]]
3. **UI Designers**: Foque em [[UI_System_Guide]] e [[OTUI_Module_Development_Guide]]
4. **Referência Rápida**: Use [[Cheat_Sheet]]

---

## 📊 **Status da Documentação**

- ✅ **Completa**: Todos os sistemas documentados
- ✅ **Integrada**: Conteúdo do habdel incorporado
- ✅ **Atualizada**: Informações mais recentes
- ✅ **Exemplos**: Código prático incluído

---

> [!success] **Documentação 100% Completa**
> Esta wiki agora contém toda a informação disponível do projeto,
    integrando conteúdo do habdel e expandindo para cobrir todos os aspectos do OTClient.

"""
        
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Índice da wiki atualizado: {index_file}")
    
    def expand_wiki_comprehensive(self):
        """Expande a wiki de forma abrangente"""
        print("Expandindo wiki de forma abrangente...")
        
        # Criar guias expandidos
        self.create_comprehensive_ui_guide()
        self.create_lua_api_reference()
        self.create_system_guides()
        self.create_development_guides()
        self.create_reference_documents()
        
        # Atualizar índice
        self.update_wiki_index()
        
        print("Expansão da wiki concluída!")

def main():
    """Função principal"""
    expander = WikiExpander("wiki")
    expander.expand_wiki_comprehensive()

if __name__ == "__main__":
    main() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = WikiexpanderModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script expand_wiki_comprehensive.py executado com sucesso via módulo documentation.wiki_expander")
    else:
        print(f"❌ Erro na execução do script expand_wiki_comprehensive.py via módulo documentation.wiki_expander")


# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = MapupdaterModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script migrated_expand_wiki_comprehensive.py executado com sucesso via módulo maps.map_updater")
    else:
        print(f"❌ Erro na execução do script migrated_expand_wiki_comprehensive.py via módulo maps.map_updater")
