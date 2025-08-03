from unicode_aliases import *
# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
MAX_ITEMS = 100

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: migrated_habdel_wiki_integration.py
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
Script Migrado: habdel_wiki_integration.py
Módulo de Destino: documentation.documentation_organizer
Data de Migração: 2025-08-01 12:21:34

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import DocumentationorganizerModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Habdel Wiki Integration Script

Este script integra a documentação habdel com a wiki principal do OTClient,
criando links, índices e navegação unificada.
"""

import logging
import re
from datetime import datetime

class HabdelWikiIntegration:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent
        self.habdel_path = self.base_path / "habdel"
        self.otclient_path = self.base_path / "otclient"
        self.log_path = self.base_path / "log"
        
        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('HabdelWikiIntegration')
        
        # Mapeamento de arquivos habdel para wiki
        self.file_mapping = {
            # UI System
            'UIWidget_Reference.md': 'UI_System_Guide.md',
            'UIWidget.md': 'UI_System_Guide.md',
            'UIButton.md': 'UI_System_Guide.md',
            'UITextEdit.md': 'UI_System_Guide.md',
            'UILayouts.md': 'UI_System_Guide.md',
            'UIEvents.md': 'UI_System_Guide.md',
            'UIStyling.md': 'UI_System_Guide.md',
            'UIWidgetsSpecialized.md': 'UI_System_Guide.md',
            
            # Core System
            'ModuleSystem.md': 'Module_System_Guide.md',
            'Configuration.md': 'Configuration_Guide.md',
            'GraphicsSystem.md': 'Graphics_System_Guide.md',
            'SoundSystem.md': 'Sound_System_Guide.md',
            'ConfigurationAdvanced.md': 'Advanced_Configuration_Guide.md',
            'NetworkSystem.md': 'Network_System_Guide.md',
            
            # Game System
            'Protocol.md': 'Protocol_System_Guide.md',
            'WorldSystem.md': 'World_System_Guide.md',
            'CreatureSystem.md': 'Creature_System_Guide.md',
            'ItemSystem.md': 'Item_System_Guide.md',
            
            # Guides
            'GettingStarted.md': 'Getting_Started_Guide.md',
            'FirstModule.md': 'Module_Development_Guide.md',
            'BestPractices.md': 'Module_Development_Guide.md',
            
            # References
            'LuaAPI.md': 'Lua_API_Reference.md',
            'CheatSheet.md': 'Cheat_Sheet.md'
        }
        
        # Mapeamento reverso (wiki para habdel)
        self.reverse_mapping = {v: k for k, v in self.file_mapping.items()}
        
    def analyze_habdel_structure(self) -> Dict:
        """Analisa a estrutura da documentação habdel"""
        self.logger.info("🔍 Analisando estrutura da documentação habdel...")
        
        structure = {
            "total_files": 0,
            "categories": {},
            "stories": {},
            "files": []
        }
        
        # Analisar arquivos habdel
        for file_path in self.habdel_path.rglob("*.md"):
            if file_path.is_file():
                structure["total_files"] += 1
                
                # Determinar categoria
                category = self.determine_category(file_path.name)
                if category not in structure["categories"]:
                    structure["categories"][category] = []
                
                structure["categories"][category].append(file_path.name)
                structure["files"].append(str(file_path))
                
                # Extrair informações da story
                story_info = self.extract_story_info(file_path)
                if story_info:
                    structure["stories"][file_path.name] = story_info
        
        self.logger.info(f"✅ Estrutura analisada: {structure['total_files']} arquivos encontrados")
        return structure
    
    def determine_category(self, filename: str) -> str:
        """Determina a categoria do arquivo baseado no nome"""
        if filename.startswith('UI'):
            return 'UI'
        elif filename.startswith('GAME') or filename in ['Protocol.md', 'WorldSystem.md', 'CreatureSystem.md',
    'ItemSystem.md']:
            return 'Game'
        elif filename.startswith('CORE') or filename in ['ModuleSystem.md', 'Configuration.md', 'GraphicsSystem.md',
    'SoundSystem.md', 'NetworkSystem.md']:
            return 'Core'
        elif filename.startswith('GUIDE') or filename in ['GettingStarted.md', 'FirstModule.md', 'BestPractices.md']:
            return 'Guide'
        elif filename.startswith('REF') or filename in ['LuaAPI.md', 'CheatSheet.md']:
            return 'Reference'
        else:
            return 'Other'
    
    def extract_story_info(self, file_path: Path) -> Optional[Dict]:
        """Extrai informações da story do arquivo"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Procurar por padrões de story
            story_patterns = [
                r'UI-\d+',
                r'GAME-\d+',
                r'CORE-\d+',
                r'GUIDE-\d+',
                r'REF-\d+'
            ]
            
            for pattern in story_patterns:
                match = re.search(pattern, content)
                if match:
                    return {
                        "id": match.group(),
                        "title": self.extract_title(content),
                        "status": self.extract_status(content),
                        "category": self.determine_category(file_path.name)
                    }
            
            return None
            
        except Exception as e:
            self.logger.warning(f"⚠️ Erro ao extrair informações de {file_path}: {e}")
            return None
    
    def extract_title(self, content: str) -> str:
        """Extrai título do conteúdo"""
        lines = content.split('\n')
        for line in lines[:10]:  # Procurar nas primeiras 10 linhas
            if line.startswith('# '):
                return line[2:].strip()
        return "Sem título"
    
    def extract_status(self, content: str) -> str:
        """Extrai status do conteúdo"""
        if '✅' in content or 'completo' in content.lower():
            return 'completo'
        elif '🔄' in content or 'em andamento' in content.lower():
            return 'em_andamento'
        else:
            return 'planejado'
    
    def analyze_wiki_structure(self) -> Dict:
        """Analisa a estrutura da wiki principal"""
        self.logger.info("🔍 Analisando estrutura da wiki principal...")
        
        structure = {
            "total_files": 0,
            "categories": {},
            "files": []
        }
        
        # Analisar arquivos da wiki
        for file_path in self.otclient_path.rglob("*.md"):
            if file_path.is_file():
                structure["total_files"] += 1
                
                # Determinar categoria
                category = self.determine_wiki_category(file_path.name)
                if category not in structure["categories"]:
                    structure["categories"][category] = []
                
                structure["categories"][category].append(file_path.name)
                structure["files"].append(str(file_path))
        
        self.logger.info(f"✅ Estrutura analisada: {structure['total_files']} arquivos encontrados")
        return structure
    
    def determine_wiki_category(self, filename: str) -> str:
        """Determina a categoria do arquivo da wiki"""
        if 'UI' in filename or 'Widget' in filename:
            return 'UI'
        elif 'Game' in filename or 'Combat' in filename or 'World' in filename:
            return 'Game'
        elif 'Core' in filename or 'Module' in filename or 'Configuration' in filename:
            return 'Core'
        elif 'Guide' in filename or 'Getting' in filename:
            return 'Guide'
        elif 'Reference' in filename or 'API' in filename or 'Cheat' in filename:
            return 'Reference'
        else:
            return 'Other'
    
    def create_integration_index(self, habdel_structure: Dict, wiki_structure: Dict) -> str:
        """Cria índice de integração entre habdel e wiki"""
        self.logger.info("📋 Criando índice de integração...")
        
        index_content = f"""---
tags: [integration, habdel, wiki, index, navigation]
type: integration_index
status: active
priority: high
created: {datetime.now().strftime('%Y-%m-%d')}
---

# 🔗 Índice de Integração Habdel-Wiki

## 📋 Visão Geral

Este índice conecta a **documentação habdel** com a **wiki principal** do OTClient,
    fornecendo navegação unificada e referências cruzadas.

**Última Atualização**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Total de Arquivos Habdel**: {habdel_structure['total_files']}
**Total de Arquivos Wiki**: {wiki_structure['total_files']}

---

## 🎨 Sistema de Interface (UI)

### **📚 Documentação Habdel:**
"""
        
        # Adicionar seções por categoria
        for category in ['UI', 'Game', 'Core', 'Guide', 'Reference']:
            if category in habdel_structure['categories']:
                index_content += f"\n## {self.get_category_emoji(category)} {self.get_category_name(category)}\n\n"
                index_content += f"### **📚 Documentação Habdel:**\n"
                
                for file in habdel_structure['categories'][category]:
                    story_info = habdel_structure['stories'].get(file, {})
                    status_emoji = self.get_status_emoji(story_info.get('status', 'planejado'))
                    
                    index_content += f"- {status_emoji} **{file}**"
                    if story_info.get('id'):
                        index_content += f" ({story_info['id']})"
                    if story_info.get('title'):
                        index_content += f" - {story_info['title']}"
                    index_content += "\n"
                
                index_content += f"\n### **📖 Wiki Principal:**\n"
                
                if category in wiki_structure['categories']:
                    for file in wiki_structure['categories'][category]:
                        index_content += f"- 📄 **{file}**\n"
                else:
                    index_content += "- *Nenhum arquivo correspondente*\n"
                
                index_content += "\n### **🔗 Links de Integração:**\n"
                
                # Criar links de integração
                for habdel_file in habdel_structure['categories'][category]:
                    wiki_file = self.file_mapping.get(habdel_file)
                    if wiki_file:
                        index_content += f"- 🔗 **{habdel_file}** → **{wiki_file}**\n"
                    else:
                        index_content += f"- ⚠️ **{habdel_file}** → *Sem correspondência*\n"
                
                index_content += "\n---\n"
        
        # Adicionar seção de navegação
        index_content += f"""
## 🧭 Navegação Rápida

### **🎯 Por Categoria:**
- **UI**: {len(habdel_structure['categories'].get('UI',
    []))} arquivos habdel → {len(wiki_structure['categories'].get('UI', []))} arquivos wiki
- **Game**: {len(habdel_structure['categories'].get('Game',
    []))} arquivos habdel → {len(wiki_structure['categories'].get('Game', []))} arquivos wiki
- **Core**: {len(habdel_structure['categories'].get('Core',
    []))} arquivos habdel → {len(wiki_structure['categories'].get('Core', []))} arquivos wiki
- **Guide**: {len(habdel_structure['categories'].get('Guide',
    []))} arquivos habdel → {len(wiki_structure['categories'].get('Guide', []))} arquivos wiki
- **Reference**: {len(habdel_structure['categories'].get('Reference',
    []))} arquivos habdel → {len(wiki_structure['categories'].get('Reference', []))} arquivos wiki

### **📊 Estatísticas:**
- **Total de Mapeamentos**: {len(self.file_mapping)}
- **Cobertura**: {(len(self.file_mapping) / habdel_structure['total_files'] * 100):.1f}%
- **Arquivos Sem Mapeamento**: {habdel_structure['total_files'] - len(self.file_mapping)}

---

## 🔧 Como Usar

### **📖 Para Desenvolvedores:**
1. **Consulte a documentação habdel** para detalhes técnicos específicos
2. **Use a wiki principal** para guias práticos e exemplos
3. **Siga os links de integração** para navegação completa
4. **Atualize ambos** quando fizer mudanças

### **📝 Para Contribuidores:**
1. **Mantenha sincronização** entre habdel e wiki
2. **Atualize este índice** quando adicionar novos arquivos
3. **Use padrões consistentes** de nomenclatura
4. **Valide links** regularmente

---

## 📈 Status da Integração

### **✅ Integração Completa:**
- **UI System**: {len([f for f in habdel_structure['categories'].get('UI',
    []) if f in self.file_mapping])}/{len(habdel_structure['categories'].get('UI', []))} arquivos
- **Game System**: {len([f for f in habdel_structure['categories'].get('Game',
    []) if f in self.file_mapping])}/{len(habdel_structure['categories'].get('Game', []))} arquivos
- **Core System**: {len([f for f in habdel_structure['categories'].get('Core',
    []) if f in self.file_mapping])}/{len(habdel_structure['categories'].get('Core', []))} arquivos
- **Guide System**: {len([f for f in habdel_structure['categories'].get('Guide',
    []) if f in self.file_mapping])}/{len(habdel_structure['categories'].get('Guide', []))} arquivos
- **Reference System**: {len([f for f in habdel_structure['categories'].get('Reference',
    []) if f in self.file_mapping])}/{len(habdel_structure['categories'].get('Reference', []))} arquivos

### **🔄 Próximos Passos:**
1. **Completar mapeamentos** faltantes
2. **Validar links** de integração
3. **Criar navegação** automática
4. **Implementar busca** unificada

---

**Índice Criado**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Responsável**: Habdel Wiki Integration System
**Status**: 🟢 **Integração Ativa**
"""
        
        return index_content
    
    def get_category_emoji(self, category: str) -> str:
        """Retorna emoji para categoria"""
        emojis = {
            'UI': '🎨',
            'Game': '🎮',
            'Core': '🔧',
            'Guide': '📚',
            'Reference': '🔍'
        }
        return emojis.get(category, '📄')
    
    def get_category_name(self, category: str) -> str:
        """Retorna nome completo da categoria"""
        names = {
            'UI': 'Sistema de Interface',
            'Game': 'Sistema de Jogo',
            'Core': 'Sistema Central',
            'Guide': 'Guias e Tutoriais',
            'Reference': 'Referências'
        }
        return names.get(category, category)
    
    def get_status_emoji(self, status: str) -> str:
        """Retorna emoji para status"""
        emojis = {
            'completo': '✅',
            'em_andamento': '🔄',
            'planejado': '📋'
        }
        return emojis.get(status, '📋')
    
    def create_navigation_links(self, habdel_structure: Dict) -> str:
        """Cria links de navegação para arquivos habdel"""
        self.logger.info("🔗 Criando links de navegação...")
        
        navigation_content = f"""---
tags: [navigation, habdel, links, quick_access]
type: navigation_guide
status: active
priority: medium
created: {datetime.now().strftime('%Y-%m-%d')}
---

# 🧭 Guia de Navegação Habdel

## 📋 Links Rápidos por Categoria

### **🎨 Interface (UI)**
"""
        
        # Criar seções por categoria
        for category in ['UI', 'Game', 'Core', 'Guide', 'Reference']:
            if category in habdel_structure['categories']:
                navigation_content += f"\n### **{self.get_category_emoji(category)} {self.get_category_name(category)}**\n"
                
                for file in habdel_structure['categories'][category]:
                    story_info = habdel_structure['stories'].get(file, {})
                    status_emoji = self.get_status_emoji(story_info.get('status', 'planejado'))
                    
                    navigation_content += f"- {status_emoji} **[{file}](../habdel/{file})**"
                    if story_info.get('id'):
                        navigation_content += f" ({story_info['id']})"
                    if story_info.get('title'):
                        navigation_content += f" - {story_info['title']}"
                    navigation_content += "\n"
                
                navigation_content += "\n"
        
        navigation_content += f"""
## 🔍 Busca Rápida

### **📚 Por ID de Story:**
"""
        
        # Criar índice por ID de story
        story_ids = {}
        for file, story_info in habdel_structure['stories'].items():
            if story_info.get('id'):
                story_ids[story_info['id']] = file
        
        for story_id in sorted(story_ids.keys()):
            file = story_ids[story_id]
            story_info = habdel_structure['stories'][file]
            status_emoji = self.get_status_emoji(story_info.get('status', 'planejado'))
            
            navigation_content += f"- {status_emoji} **{story_id}**: [{file}](../habdel/{file}) - {story_info.get('title',
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    'Sem título')}\n"
        
        navigation_content += f"""
## 📊 Estatísticas de Navegação

- **Total de Arquivos**: {habdel_structure['total_files']}
- **Stories Identificadas**: {len(habdel_structure['stories'])}
- **Categorias**: {len(habdel_structure['categories'])}
- **Última Atualização**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

**Guia Criado**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Responsável**: Habdel Wiki Integration System
**Status**: 🟢 **Navegação Ativa**
"""
        
        return navigation_content
    
    def save_integration_files(self, habdel_structure: Dict, wiki_structure: Dict) -> List[str]:
        """Salva arquivos de integração"""
        self.logger.info("💾 Salvando arquivos de integração...")
        
        saved_files = []
        
        # Criar e salvar índice de integração
        integration_index = self.create_integration_index(habdel_structure, wiki_structure)
        integration_file = self.otclient_path / "Habdel_Integration_Index.md"
        
        try:
            with open(integration_file, 'w', encoding='utf-8') as f:
                f.write(integration_index)
            saved_files.append(str(integration_file))
            self.logger.info(f"✅ Índice de integração salvo: {integration_file}")
        except Exception as e:
            self.logger.error(f"❌ Erro ao salvar índice: {e}")
        
        # Criar e salvar guia de navegação
        navigation_guide = self.create_navigation_links(habdel_structure)
        navigation_file = self.otclient_path / "Habdel_Navigation_Guide.md"
        
        try:
            with open(navigation_file, 'w', encoding='utf-8') as f:
                f.write(navigation_guide)
            saved_files.append(str(navigation_file))
            self.logger.info(f"✅ Guia de navegação salvo: {navigation_file}")
        except Exception as e:
            self.logger.error(f"❌ Erro ao salvar guia: {e}")
        
        return saved_files
    
    def run(self) -> bool:
        """Executa a integração habdel-wiki"""
        self.logger.info("🚀 Iniciando integração habdel-wiki...")
        
        try:
            # Analisar estruturas
            habdel_structure = self.analyze_habdel_structure()
            wiki_structure = self.analyze_wiki_structure()
            
            # Salvar arquivos de integração
            saved_files = self.save_integration_files(habdel_structure, wiki_structure)
            
            # Log de resumo
            self.logger.info(f"📊 Resumo da Integração:")
            self.logger.info(f"   - Arquivos Habdel: {habdel_structure['total_files']}")
            self.logger.info(f"   - Arquivos Wiki: {wiki_structure['total_files']}")
            self.logger.info(f"   - Mapeamentos: {len(self.file_mapping)}")
            self.logger.info(f"   - Arquivos Criados: {len(saved_files)}")
            
            self.logger.info("✅ Integração habdel-wiki concluída com sucesso")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro na integração: {e}")
            return False

if __name__ == "__main__":
    integrator = HabdelWikiIntegration()
    success = integrator.run()
    
    if success:
        print("✅ Integração habdel-wiki executada com sucesso!")
    else:
        print("❌ Integração habdel-wiki falhou!") 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = DocumentationorganizerModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script habdel_wiki_integration.py executado com sucesso via módulo documentation.documentation_organizer")
    else:
        print(f"❌ Erro na execução do script habdel_wiki_integration.py via módulo documentation.documentation_organizer")


# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = MapupdaterModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script migrated_habdel_wiki_integration.py executado com sucesso via módulo maps.map_updater")
    else:
        print(f"❌ Erro na execução do script migrated_habdel_wiki_integration.py via módulo maps.map_updater")
