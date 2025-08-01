# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
MAX_ITEMS = 100
MAX_SIZE = 1000
TIMEOUT_MS = 500

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: migrated_navigation_index_generator.py
Módulo de Destino: maps.source_indexer
Data de Migração: 2025-08-01 12:21:40

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import SourceindexerModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: navigation_index_generator.py
Módulo de Destino: analysis.research_manager
Data de Migração: 2025-08-01 12:21:34

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import ResearchmanagerModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Navigation Index Generator

Este script gera índices de navegação para facilitar a busca e navegação
na documentação integrada habdel-wiki.
"""

import logging
import re
from datetime import datetime

class NavigationIndexGenerator:
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
        self.logger = logging.getLogger('NavigationIndexGenerator')
        
        # Configurações de indexação
        self.config = {
            "index_types": ["alphabetical", "categorical", "story_based", "topic_based"],
            "search_keywords": ["API", "guide", "tutorial", "reference", "system", "widget"],
            "priority_tags": ["critical", "high", "medium", "low"]
        }
        
    def scan_all_documents(self) -> Dict:
        """Escaneia todos os documentos para criar índice completo"""
        self.logger.info("🔍 Escaneando todos os documentos...")
        
        documents = {
            "habdel": [],
            "wiki": [],
            "total": 0,
            "categories": {},
            "tags": {},
            "stories": {}
        }
        
        # Escanear documentos habdel
        for file_path in self.habdel_path.rglob("*.md"):
            if file_path.is_file():
                doc_info = self.extract_document_info(file_path, "habdel")
                documents["habdel"].append(doc_info)
                documents["total"] += 1
                
                # Categorizar
                category = self.categorize_document(doc_info)
                if category not in documents["categories"]:
                    documents["categories"][category] = []
                documents["categories"][category].append(doc_info)
                
                # Extrair tags
                for tag in doc_info.get("tags", []):
                    if tag not in documents["tags"]:
                        documents["tags"][tag] = []
                    documents["tags"][tag].append(doc_info)
                
                # Extrair stories
                if doc_info.get("story_id"):
                    documents["stories"][doc_info["story_id"]] = doc_info
        
        # Escanear documentos wiki
        for file_path in self.otclient_path.rglob("*.md"):
            if file_path.is_file():
                doc_info = self.extract_document_info(file_path, "wiki")
                documents["wiki"].append(doc_info)
                documents["total"] += 1
                
                # Categorizar
                category = self.categorize_document(doc_info)
                if category not in documents["categories"]:
                    documents["categories"][category] = []
                documents["categories"][category].append(doc_info)
                
                # Extrair tags
                for tag in doc_info.get("tags", []):
                    if tag not in documents["tags"]:
                        documents["tags"][tag] = []
                    documents["tags"][tag].append(doc_info)
        
        self.logger.info(f"✅ Documentos escaneados: {documents['total']} total")
        return documents
    
    def extract_document_info(self, file_path: Path, source: str) -> Dict:
        """Extrai informações do documento"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extrair frontmatter
            frontmatter = self.extract_frontmatter(content)
            
            # Extrair título
            title = self.extract_title(content)
            
            # Extrair story ID
            story_id = self.extract_story_id(content, file_path.name)
            
            # Extrair tags
            tags = frontmatter.get("tags", [])
            
            # Extrair status
            status = frontmatter.get("status", "active")
            
            # Extrair prioridade
            priority = frontmatter.get("priority", "medium")
            
            # Calcular tamanho
            size = len(content)
            size_category = self.categorize_size(size)
            
            # Extrair palavras-chave
            keywords = self.extract_keywords(content)
            
            return {
                "filename": file_path.name,
                "path": str(file_path.relative_to(self.base_path)),
                "source": source,
                "title": title,
                "story_id": story_id,
                "tags": tags,
                "status": status,
                "priority": priority,
                "size": size,
                "size_category": size_category,
                "keywords": keywords,
                "last_modified": datetime.fromtimestamp(file_path.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            }
            
        except Exception as e:
            self.logger.warning(f"⚠️ Erro ao extrair informações de {file_path}: {e}")
            return {
                "filename": file_path.name,
                "path": str(file_path.relative_to(self.base_path)),
                "source": source,
                "title": "Erro na extração",
                "story_id": None,
                "tags": [],
                "status": "error",
                "priority": "low",
                "size": 0,
                "size_category": "small",
                "keywords": [],
                "last_modified": "unknown"
            }
    
    def extract_frontmatter(self, content: str) -> Dict:
        """Extrai frontmatter do conteúdo"""
        frontmatter = {}
        
        # Procurar por frontmatter
        frontmatter_match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if frontmatter_match:
            frontmatter_text = frontmatter_match.group(1)
            
            # Extrair tags
            tags_match = re.search(r'tags:\s*\[(.*?)\]', frontmatter_text)
            if tags_match:
                tags_str = tags_match.group(1)
                tags = [tag.strip() for tag in tags_str.split(',')]
                frontmatter["tags"] = tags
            
            # Extrair status
            status_match = re.search(r'status:\s*(\w+)', frontmatter_text)
            if status_match:
                frontmatter["status"] = status_match.group(1)
            
            # Extrair prioridade
            priority_match = re.search(r'priority:\s*(\w+)', frontmatter_text)
            if priority_match:
                frontmatter["priority"] = priority_match.group(1)
        
        return frontmatter
    
    def extract_title(self, content: str) -> str:
        """Extrai título do conteúdo"""
        lines = content.split('\n')
        for line in lines[:10]:  # Procurar nas primeiras 10 linhas
            if line.startswith('# '):
                return line[2:].strip()
        return "Sem título"
    
    def extract_story_id(self, content: str, filename: str) -> Optional[str]:
        """Extrai ID da story"""
        # Procurar por padrões de story ID
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
                return match.group()
        
        return None
    
    def categorize_document(self, doc_info: Dict) -> str:
        """Categoriza o documento"""
        filename = doc_info["filename"].lower()
        
        if any(ui_word in filename for ui_word in ['ui', 'widget', 'button', 'layout']):
            return 'UI'
        elif any(game_word in filename for game_word in ['game', 'combat', 'world', 'creature', 'item']):
            return 'Game'
        elif any(core_word in filename for core_word in ['core', 'module', 'config', 'network', 'graphics']):
            return 'Core'
        elif any(guide_word in filename for guide_word in ['guide', 'tutorial', 'getting', 'best']):
            return 'Guide'
        elif any(ref_word in filename for ref_word in ['reference', 'api', 'cheat', 'lua']):
            return 'Reference'
        else:
            return 'Other'
    
    def categorize_size(self, size: int) -> str:
        """Categoriza o tamanho do documento"""
        if size < 1000:
            return "small"
        elif size < 10000:
            return "medium"
        elif size < 50000:
            return "large"
        else:
            return "xlarge"
    
    def extract_keywords(self, content: str) -> List[str]:
        """Extrai palavras-chave do conteúdo"""
        keywords = []
        
        # Procurar por palavras-chave específicas
        for keyword in self.config["search_keywords"]:
            if keyword.lower() in content.lower():
                keywords.append(keyword)
        
        # Procurar por padrões específicos
        patterns = [
            r'class\s+(\w+)',
            r'function\s+(\w+)',
            r'API\s+(\w+)',
            r'System\s+(\w+)'
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            keywords.extend(matches[:5])  # Limitar a 5 por padrão
        
        return list(set(keywords))  # Remover duplicatas
    
    def create_alphabetical_index(self, documents: Dict) -> str:
        """Cria índice alfabético"""
        self.logger.info("📋 Criando índice alfabético...")
        
        # Organizar por ordem alfabética
        all_docs = documents["habdel"] + documents["wiki"]
        all_docs.sort(key=lambda x: x["title"].lower())
        
        index_content = f"""---
tags: [index, alphabetical, navigation, search]
type: alphabetical_index
status: active
priority: medium
created: {datetime.now().strftime('%Y-%m-%d')}
---

# 🔤 Índice Alfabético - Documentação Completa

## 📋 Visão Geral

Este índice organiza todos os documentos por ordem alfabética, facilitando a busca rápida por título.

**Total de Documentos**: {documents['total']}
**Última Atualização**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 📚 Documentos por Ordem Alfabética

"""
        
        current_letter = ""
        for doc in all_docs:
            first_letter = doc["title"][0].upper() if doc["title"] else "?"
            
            if first_letter != current_letter:
                current_letter = first_letter
                index_content += f"\n### **{current_letter}**\n\n"
            
            # Emoji baseado na fonte
            source_emoji = "📚" if doc["source"] == "habdel" else "📖"
            
            # Emoji baseado no status
            status_emoji = {
                "active": "✅",
                "completed": "✅",
                "in_progress": "🔄",
                "planned": "📋",
                "error": "❌"
            }.get(doc["status"], "📄")
            
            index_content += f"- {source_emoji} {status_emoji} **[{doc['title']}]({doc['path']})**"
            
            if doc["story_id"]:
                index_content += f" ({doc['story_id']})"
            
            index_content += f" - {doc['source'].title()}\n"
        
        index_content += f"""
---

## 📊 Estatísticas

- **Documentos Habdel**: {len(documents['habdel'])}
- **Documentos Wiki**: {len(documents['wiki'])}
- **Total**: {documents['total']}

---

**Índice Criado**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Responsável**: Navigation Index Generator
**Status**: 🟢 **Índice Ativo**
"""
        
        return index_content
    
    def create_categorical_index(self, documents: Dict) -> str:
        """Cria índice por categorias"""
        self.logger.info("📋 Criando índice por categorias...")
        
        index_content = f"""---
tags: [index, categorical, navigation, organization]
type: categorical_index
status: active
priority: high
created: {datetime.now().strftime('%Y-%m-%d')}
---

# 🗂️ Índice por Categorias - Documentação Organizada

## 📋 Visão Geral

Este índice organiza todos os documentos por categorias funcionais, facilitando a navegação por área de interesse.

**Total de Documentos**: {documents['total']}
**Categorias**: {len(documents['categories'])}
**Última Atualização**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

"""
        
        # Organizar categorias por ordem de importância
        category_order = ['UI', 'Game', 'Core', 'Guide', 'Reference', 'Other']
        
        for category in category_order:
            if category in documents["categories"]:
                docs = documents["categories"][category]
                
                # Emoji da categoria
                category_emoji = {
                    'UI': '🎨',
                    'Game': '🎮',
                    'Core': '🔧',
                    'Guide': '📚',
                    'Reference': '🔍',
                    'Other': '📄'
                }.get(category, '📄')
                
                index_content += f"## {category_emoji} {category}\n\n"
                index_content += f"**Total de Documentos**: {len(docs)}\n\n"
                
                # Subdividir por fonte
                habdel_docs = [d for d in docs if d["source"] == "habdel"]
                wiki_docs = [d for d in docs if d["source"] == "wiki"]
                
                if habdel_docs:
                    index_content += "### **📚 Documentação Habdel:**\n"
                    for doc in habdel_docs:
                        status_emoji = "✅" if doc["status"] == "active" else "📋"
                        index_content += f"- {status_emoji} **[{doc['title']}]({doc['path']})**"
                        if doc["story_id"]:
                            index_content += f" ({doc['story_id']})"
                        index_content += "\n"
                    index_content += "\n"
                
                if wiki_docs:
                    index_content += "### **📖 Wiki Principal:**\n"
                    for doc in wiki_docs:
                        status_emoji = "✅" if doc["status"] == "active" else "📋"
                        index_content += f"- {status_emoji} **[{doc['title']}]({doc['path']})**\n"
                    index_content += "\n"
                
                index_content += "---\n\n"
        
        index_content += f"""
## 📊 Estatísticas por Categoria

"""
        
        for category in category_order:
            if category in documents["categories"]:
                docs = documents["categories"][category]
                index_content += f"- **{category}**: {len(docs)} documentos\n"
        
        index_content += f"""
---

**Índice Criado**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Responsável**: Navigation Index Generator
**Status**: 🟢 **Índice Ativo**
"""
        
        return index_content
    
    def create_story_based_index(self, documents: Dict) -> str:
        """Cria índice baseado em stories"""
        self.logger.info("📋 Criando índice baseado em stories...")
        
        index_content = f"""---
tags: [index, story_based, navigation, development]
type: story_based_index
status: active
priority: high
created: {datetime.now().strftime('%Y-%m-%d')}
---

# 📖 Índice Baseado em Stories - Desenvolvimento Organizado

## 📋 Visão Geral

Este índice organiza documentos baseado no sistema de stories do habdel,
    facilitando o acompanhamento do desenvolvimento.

**Total de Stories**: {len(documents['stories'])}
**Última Atualização**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 🏷️ Stories por Categoria

"""
        
        # Organizar stories por categoria
        story_categories = {}
        for story_id, doc in documents["stories"].items():
            category = doc["story_id"][:2] if doc["story_id"] else "Other"
            if category not in story_categories:
                story_categories[category] = []
            story_categories[category].append((story_id, doc))
        
        # Ordenar por categoria
        category_order = ['UI', 'GA', 'CO', 'GU', 'RE', 'Other']
        
        for category in category_order:
            if category in story_categories:
                stories = story_categories[category]
                stories.sort(key=lambda x: x[0])  # Ordenar por ID
                
                # Nome da categoria
                category_name = {
                    'UI': 'Interface (UI)',
                    'GA': 'Game',
                    'CO': 'Core',
                    'GU': 'Guide',
                    'RE': 'Reference',
                    'Other': 'Outros'
                }.get(category, category)
                
                # Emoji da categoria
                category_emoji = {
                    'UI': '🎨',
                    'GA': '🎮',
                    'CO': '🔧',
                    'GU': '📚',
                    'RE': '🔍',
                    'Other': '📄'
                }.get(category, '📄')
                
                index_content += f"## {category_emoji} {category_name}\n\n"
                
                for story_id, doc in stories:
                    status_emoji = "✅" if doc["status"] == "active" else "📋"
                    source_emoji = "📚" if doc["source"] == "habdel" else "📖"
                    
                    index_content += f"- {status_emoji} {source_emoji} **{story_id}**: [{doc['title']}]({doc['path']})\n"
                
                index_content += "\n---\n\n"
        
        index_content += f"""
## 📊 Estatísticas de Stories

"""
        
        for category in category_order:
            if category in story_categories:
                stories = story_categories[category]
                index_content += f"- **{category}**: {len(stories)} stories\n"
        
        index_content += f"""
---

**Índice Criado**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Responsável**: Navigation Index Generator
**Status**: 🟢 **Índice Ativo**
"""
        
        return index_content
    
    def create_search_index(self, documents: Dict) -> str:
        """Cria índice de busca"""
        self.logger.info("📋 Criando índice de busca...")
        
        index_content = f"""---
tags: [index, search, keywords, navigation]
type: search_index
status: active
priority: medium
created: {datetime.now().strftime('%Y-%m-%d')}
---

# 🔍 Índice de Busca - Palavras-Chave

## 📋 Visão Geral

Este índice organiza documentos por palavras-chave, facilitando a busca por tópicos específicos.

**Total de Documentos**: {documents['total']}
**Última Atualização**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 🔑 Palavras-Chave Principais

"""
        
        # Coletar todas as palavras-chave
        all_keywords = set()
        keyword_docs = {}
        
        for doc in documents["habdel"] + documents["wiki"]:
            for keyword in doc.get("keywords", []):
                all_keywords.add(keyword)
                if keyword not in keyword_docs:
                    keyword_docs[keyword] = []
                keyword_docs[keyword].append(doc)
        
        # Ordenar palavras-chave
        sorted_keywords = sorted(all_keywords)
        
        for keyword in sorted_keywords:
            docs = keyword_docs[keyword]
            
            index_content += f"### **{keyword}** ({len(docs)} documentos)\n\n"
            
            for doc in docs:
                status_emoji = "✅" if doc["status"] == "active" else "📋"
                source_emoji = "📚" if doc["source"] == "habdel" else "📖"
                
                index_content += f"- {status_emoji} {source_emoji} **[{doc['title']}]({doc['path']})**"
                if doc["story_id"]:
                    index_content += f" ({doc['story_id']})"
                index_content += f" - {doc['source'].title()}\n"
            
            index_content += "\n"
        
        index_content += f"""
## 📊 Estatísticas de Busca

- **Palavras-Chave Únicas**: {len(all_keywords)}
- **Documentos Indexados**: {documents['total']}
- **Média de Keywords por Doc**: {sum(len(doc.get('keywords',
    [])) for doc in documents['habdel'] + documents['wiki']) / max(documents['total'], 1):.1f}

---

**Índice Criado**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Responsável**: Navigation Index Generator
**Status**: 🟢 **Índice Ativo**
"""
        
        return index_content
    
    def save_indexes(self, documents: Dict) -> List[str]:
        """Salva todos os índices"""
        self.logger.info("💾 Salvando índices de navegação...")
        
        saved_files = []
        
        # Criar e salvar índices
        indexes = [
            ("alphabetical", self.create_alphabetical_index),
            ("categorical", self.create_categorical_index),
            ("story_based", self.create_story_based_index),
            ("search", self.create_search_index)
        ]
        
        for index_type, generator_func in indexes:
            try:
                index_content = generator_func(documents)
                index_file = self.otclient_path / f"Navigation_Index_{index_type.title()}.md"
                
                with open(index_file, 'w', encoding='utf-8') as f:
                    f.write(index_content)
                
                saved_files.append(str(index_file))
                self.logger.info(f"✅ Índice {index_type} salvo: {index_file}")
                
            except Exception as e:
                self.logger.error(f"❌ Erro ao salvar índice {index_type}: {e}")
        
        return saved_files
    
    def run(self) -> bool:
        """Executa a geração de índices"""
        self.logger.info("🚀 Iniciando geração de índices de navegação...")
        
        try:
            # Escanear documentos
            documents = self.scan_all_documents()
            
            # Salvar índices
            saved_files = self.save_indexes(documents)
            
            # Log de resumo
            self.logger.info(f"📊 Resumo da Geração de Índices:")
            self.logger.info(f"   - Documentos Escaneados: {documents['total']}")
            self.logger.info(f"   - Categorias: {len(documents['categories'])}")
            self.logger.info(f"   - Stories: {len(documents['stories'])}")
            self.logger.info(f"   - Índices Criados: {len(saved_files)}")
            
            self.logger.info("✅ Geração de índices concluída com sucesso")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro na geração de índices: {e}")
            return False

if __name__ == "__main__":
    generator = NavigationIndexGenerator()
    success = generator.run()
    
    if success:
        print("✅ Geração de índices executada com sucesso!")
    else:
        print("❌ Geração de índices falhou!") 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = ResearchmanagerModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script navigation_index_generator.py executado com sucesso via módulo analysis.research_manager")
    else:
        print(f"❌ Erro na execução do script navigation_index_generator.py via módulo analysis.research_manager")


# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = SourceindexerModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script migrated_navigation_index_generator.py executado com sucesso via módulo maps.source_indexer")
    else:
        print(f"❌ Erro na execução do script migrated_navigation_index_generator.py via módulo maps.source_indexer")
