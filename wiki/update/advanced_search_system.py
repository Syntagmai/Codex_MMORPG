from unicode_aliases import *
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import json
import logging
import os
import re

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Busca Avançada Semântica
===================================

Este script implementa sistema de busca avançada semântica na wiki consolidada
com busca por conteúdo, tags, categorias e similaridade.

Autor: Sistema BMAD - Search Agent
Data: 2025-08-01
"""


# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AdvancedSearchSystem:
    """Sistema de busca avançada semântica"""
    
    def __init__(self, consolidated_dir: str = "wiki/consolidated"):
        """
        Inicializa o sistema de busca avançada.
        
        Args:
            consolidated_dir: Diretório dos documentos consolidados
        """
        self.consolidated_dir = Path(consolidated_dir)
        self.intelligent_nav_file = self.consolidated_dir / "intelligent_navigation.json"
        self.search_index_file = self.consolidated_dir / "advanced_search_index.json"
        
        # Carregar dados de navegação inteligente
        self.nav_data = self.load_intelligent_navigation()
        
        # Índice de busca avançada
        self.search_index = {
            "content_index": {},
            "semantic_index": {},
            "category_index": {},
            "tag_index": {},
            "keyword_index": {},
            "metadata_index": {},
            "similarity_matrix": {}
        }
        
    def load_intelligent_navigation(self) -> Dict[str, Any]:
        """
        Carrega dados de navegação inteligente.
        
        Returns:
            Dados de navegação inteligente
        """
        if self.intelligent_nav_file.exists():
            try:
                with open(self.intelligent_nav_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Erro ao carregar navegação inteligente: {e}")
        
        return {}
    
    def extract_document_content(self, file_path: Path) -> Dict[str, Any]:
        """
        Extrai conteúdo completo de um documento.
        
        Args:
            file_path: Caminho para o documento
            
        Returns:
            Conteúdo extraído do documento
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extrair metadados
            metadata = {}
            
            # Título
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            metadata['title'] = title_match.group(1) if title_match else file_path.stem
            
            # Tags
            tags_match = re.search(r'tags:\s*\[(.*?)\]', content)
            metadata['tags'] = []
            if tags_match:
                metadata['tags'] = [tag.strip() for tag in tags_match.group(1).split(',')]
            
            # Tipo
            type_match = re.search(r'type:\s*(\w+)', content)
            metadata['type'] = type_match.group(1) if type_match else 'document'
            
            # Status
            status_match = re.search(r'status:\s*(\w+)', content)
            metadata['status'] = status_match.group(1) if status_match else 'active'
            
            # Extrair seções
            sections = re.split(r'^#{2,}\s+', content, flags=re.MULTILINE)
            
            # Extrair links
            links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
            
            # Extrair código
            code_blocks = re.findall(r'```[\w]*\n(.*?)\n```', content, re.DOTALL)
            
            return {
                'content': content,
                'metadata': metadata,
                'sections': sections,
                'links': links,
                'code_blocks': code_blocks,
                'word_count': len(content.split()),
                'file_size': len(content)
            }
            
        except Exception as e:
            logger.error(f"Erro ao extrair conteúdo de {file_path}: {e}")
            return {}
    
    def build_content_index(self):
        """
        Constrói índice de conteúdo para busca textual.
        """
        logger.info("📝 Construindo índice de conteúdo...")
        
        content_index = {}
        
        nav_graph = self.nav_data.get("navigation_graph", {})
        
        for main_cat, subcats in nav_graph.items():
            for subcat, docs in subcats.items():
                for doc_name, doc_info in docs.items():
                    doc_path = f"{main_cat}/{subcat}/{doc_name}"
                    full_path = self.consolidated_dir / doc_path
                    
                    if full_path.exists():
                        content_data = self.extract_document_content(full_path)
                        if content_data:
                            content_index[doc_path] = content_data
        
        self.search_index["content_index"] = content_index
        logger.info(f"✅ Índice de conteúdo construído: {len(content_index)} documentos")
    
    def build_semantic_index(self):
        """
        Constrói índice semântico baseado em similaridade de conteúdo.
        """
        logger.info("🧠 Construindo índice semântico...")
        
        semantic_index = {}
        content_index = self.search_index["content_index"]
        
        # Criar vetores de palavras-chave para cada documento
        for doc_path, content_data in content_index.items():
            content = content_data['content'].lower()
            
            # Extrair palavras-chave significativas
            words = re.findall(r'\b\w{4,}\b', content)
            word_freq = {}
            
            for word in words:
                if word not in word_freq:
                    word_freq[word] = 0
                word_freq[word] += 1
            
            # Ordenar por frequência
            sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:50]
            
            semantic_index[doc_path] = {
                'keywords': dict(sorted_words),
                'metadata': content_data['metadata'],
                'sections': content_data['sections']
            }
        
        self.search_index["semantic_index"] = semantic_index
        logger.info(f"✅ Índice semântico construído: {len(semantic_index)} documentos")
    
    def build_category_index(self):
        """
        Constrói índice por categorias.
        """
        logger.info("📂 Construindo índice por categorias...")
        
        category_index = {}
        content_index = self.search_index["content_index"]
        
        for doc_path, content_data in content_index.items():
            main_cat, subcat, _ = doc_path.split('/', 2)
            
            if main_cat not in category_index:
                category_index[main_cat] = {}
            
            if subcat not in category_index[main_cat]:
                category_index[main_cat][subcat] = []
            
            category_index[main_cat][subcat].append({
                'path': doc_path,
                'title': content_data['metadata'].get('title', ''),
                'type': content_data['metadata'].get('type', 'document'),
                'word_count': content_data['word_count']
            })
        
        self.search_index["category_index"] = category_index
        logger.info(f"✅ Índice por categorias construído: {len(category_index)} categorias principais")
    
    def build_tag_index(self):
        """
        Constrói índice por tags.
        """
        logger.info("🏷️ Construindo índice por tags...")
        
        tag_index = {}
        content_index = self.search_index["content_index"]
        
        for doc_path, content_data in content_index.items():
            tags = content_data['metadata'].get('tags', [])
            
            for tag in tags:
                if tag not in tag_index:
                    tag_index[tag] = []
                
                tag_index[tag].append({
                    'path': doc_path,
                    'title': content_data['metadata'].get('title', ''),
                    'type': content_data['metadata'].get('type', 'document')
                })
        
        self.search_index["tag_index"] = tag_index
        logger.info(f"✅ Índice por tags construído: {len(tag_index)} tags únicas")
    
    def build_keyword_index(self):
        """
        Constrói índice por palavras-chave.
        """
        logger.info("🔑 Construindo índice por palavras-chave...")
        
        keyword_index = {}
        semantic_index = self.search_index["semantic_index"]
        
        for doc_path, semantic_data in semantic_index.items():
            keywords = semantic_data['keywords']
            
            for keyword, frequency in keywords.items():
                if keyword not in keyword_index:
                    keyword_index[keyword] = []
                
                keyword_index[keyword].append({
                    'path': doc_path,
                    'frequency': frequency,
                    'title': semantic_data['metadata'].get('title', '')
                })
        
        # Ordenar por frequência
        for keyword in keyword_index:
            keyword_index[keyword].sort(key=lambda x: x['frequency'], reverse=True)
        
        self.search_index["keyword_index"] = keyword_index
        logger.info(f"✅ Índice por palavras-chave construído: {len(keyword_index)} palavras-chave únicas")
    
    def build_metadata_index(self):
        """
        Constrói índice por metadados.
        """
        logger.info("📊 Construindo índice por metadados...")
        
        metadata_index = {
            'by_type': {},
            'by_status': {},
            'by_size': {},
            'by_word_count': {}
        }
        
        content_index = self.search_index["content_index"]
        
        for doc_path, content_data in content_index.items():
            metadata = content_data['metadata']
            
            # Indexar por tipo
            doc_type = metadata.get('type', 'document')
            if doc_type not in metadata_index['by_type']:
                metadata_index['by_type'][doc_type] = []
            metadata_index['by_type'][doc_type].append(doc_path)
            
            # Indexar por status
            status = metadata.get('status', 'active')
            if status not in metadata_index['by_status']:
                metadata_index['by_status'][status] = []
            metadata_index['by_status'][status].append(doc_path)
            
            # Indexar por tamanho
            size = content_data['file_size']
            size_category = 'small' if size < 5000 else 'medium' if size < 20000 else 'large'
            if size_category not in metadata_index['by_size']:
                metadata_index['by_size'][size_category] = []
            metadata_index['by_size'][size_category].append(doc_path)
            
            # Indexar por contagem de palavras
            word_count = content_data['word_count']
            word_category = 'short' if word_count < 500 else 'medium' if word_count < 2000 else 'long'
            if word_category not in metadata_index['by_word_count']:
                metadata_index['by_word_count'][word_category] = []
            metadata_index['by_word_count'][word_category].append(doc_path)
        
        self.search_index["metadata_index"] = metadata_index
        logger.info("✅ Índice por metadados construído")
    
    def build_similarity_matrix(self):
        """
        Constrói matriz de similaridade entre documentos.
        """
        logger.info("🔗 Construindo matriz de similaridade...")
        
        similarity_matrix = {}
        semantic_index = self.search_index["semantic_index"]
        doc_paths = list(semantic_index.keys())
        
        for i, doc1_path in enumerate(doc_paths):
            similarity_matrix[doc1_path] = {}
            
            for j, doc2_path in enumerate(doc_paths):
                if i != j:
                    similarity = self.calculate_similarity(
                        semantic_index[doc1_path],
                        semantic_index[doc2_path]
                    )
                    similarity_matrix[doc1_path][doc2_path] = similarity
        
        self.search_index["similarity_matrix"] = similarity_matrix
        logger.info("✅ Matriz de similaridade construída")
    
    def calculate_similarity(self, doc1: Dict[str, Any], doc2: Dict[str, Any]) -> float:
        """
        Calcula similaridade entre dois documentos.
        
        Args:
            doc1: Dados do primeiro documento
            doc2: Dados do segundo documento
            
        Returns:
            Score de similaridade (0-1)
        """
        # Similaridade por palavras-chave
        keywords1 = set(doc1['keywords'].keys())
        keywords2 = set(doc2['keywords'].keys())
        
        if not keywords1 or not keywords2:
            return 0.0
        
        keyword_similarity = len(keywords1 & keywords2) / len(keywords1 | keywords2)
        
        # Similaridade por tags
        tags1 = set(doc1['metadata'].get('tags', []))
        tags2 = set(doc2['metadata'].get('tags', []))
        
        tag_similarity = 0.0
        if tags1 and tags2:
            tag_similarity = len(tags1 & tags2) / len(tags1 | tags2)
        
        # Similaridade por tipo
        type_similarity = 1.0 if doc1['metadata'].get('type') == doc2['metadata'].get('type') else 0.0
        
        # Média ponderada
        total_similarity = (keyword_similarity * 0.6 + tag_similarity * 0.3 + type_similarity * 0.1)
        
        return round(total_similarity, 3)
    
    def search_by_text(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Busca por texto nos documentos.
        
        Args:
            query: Query de busca
            limit: Limite de resultados
            
        Returns:
            Lista de resultados
        """
        query_lower = query.lower()
        results = []
        
        content_index = self.search_index["content_index"]
        
        for doc_path, content_data in content_index.items():
            content = content_data['content'].lower()
            title = content_data['metadata'].get('title', '').lower()
            
            # Calcular score
            score = 0
            
            # Busca no título
            if query_lower in title:
                score += 10
            
            # Busca no conteúdo
            content_matches = content.count(query_lower)
            score += content_matches * 2
            
            # Busca por palavras individuais
            query_words = query_lower.split()
            for word in query_words:
                if len(word) > 3:
                    word_matches = content.count(word)
                    score += word_matches
            
            if score > 0:
                results.append({
                    'path': doc_path,
                    'title': content_data['metadata'].get('title', ''),
                    'score': score,
                    'type': content_data['metadata'].get('type', 'document'),
                    'word_count': content_data['word_count'],
                    'snippet': self.extract_snippet(content_data['content'], query_lower)
                })
        
        # Ordenar por score
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:limit]
    
    def search_by_tags(self, tags: List[str], limit: int = 10) -> List[Dict[str, Any]]:
        """
        Busca por tags.
        
        Args:
            tags: Lista de tags para buscar
            limit: Limite de resultados
            
        Returns:
            Lista de resultados
        """
        results = []
        tag_index = self.search_index["tag_index"]
        
        for tag in tags:
            if tag in tag_index:
                for doc_info in tag_index[tag]:
                    results.append({
                        'path': doc_info['path'],
                        'title': doc_info['title'],
                        'type': doc_info['type'],
                        'matched_tag': tag
                    })
        
        # Remover duplicatas
        seen = set()
        unique_results = []
        for result in results:
            if result['path'] not in seen:
                seen.add(result['path'])
                unique_results.append(result)
        
        return unique_results[:limit]
    
    def search_by_category(self, category: str, subcategory: str = None, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Busca por categoria.
        
        Args:
            category: Categoria principal
            subcategory: Subcategoria (opcional)
            limit: Limite de resultados
            
        Returns:
            Lista de resultados
        """
        results = []
        category_index = self.search_index["category_index"]
        
        if category in category_index:
            if subcategory:
                if subcategory in category_index[category]:
                    results = category_index[category][subcategory]
            else:
                for subcat, docs in category_index[category].items():
                    results.extend(docs)
        
        return results[:limit]
    
    def search_similar(self, doc_path: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Busca documentos similares.
        
        Args:
            doc_path: Caminho do documento de referência
            limit: Limite de resultados
            
        Returns:
            Lista de documentos similares
        """
        results = []
        similarity_matrix = self.search_index["similarity_matrix"]
        
        if doc_path in similarity_matrix:
            similarities = similarity_matrix[doc_path]
            sorted_similarities = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
            
            for similar_doc, similarity_score in sorted_similarities[:limit]:
                if similarity_score > 0.1:  # Threshold mínimo
                    content_data = self.search_index["content_index"].get(similar_doc, {})
                    results.append({
                        'path': similar_doc,
                        'title': content_data.get('metadata', {}).get('title', ''),
                        'similarity': similarity_score,
                        'type': content_data.get('metadata', {}).get('type', 'document')
                    })
        
        return results
    
    def extract_snippet(self, content: str, query: str, max_length: int = 200) -> str:
        """
        Extrai snippet do conteúdo com a query destacada.
        
        Args:
            content: Conteúdo do documento
            query: Query de busca
            max_length: Tamanho máximo do snippet
            
        Returns:
            Snippet extraído
        """
        content_lower = content.lower()
        query_lower = query.lower()
        
        # Encontrar posição da query
        pos = content_lower.find(query_lower)
        
        if pos == -1:
            # Se não encontrar a query exata, procurar por palavras individuais
            words = query_lower.split()
            for word in words:
                if len(word) > 3:
                    pos = content_lower.find(word)
                    if pos != -1:
                        break
        
        if pos == -1:
            return content[:max_length] + "..."
        
        # Extrair snippet
        start = max(0, pos - max_length // 2)
        end = min(len(content), pos + max_length // 2)
        
        snippet = content[start:end]
        
        if start > 0:
            snippet = "..." + snippet
        if end < len(content):
            snippet = snippet + "..."
        
        return snippet
    
    def save_search_index(self):
        """
        Salva o índice de busca avançada.
        """
        logger.info("💾 Salvando índice de busca avançada...")
        
        with open(self.search_index_file, 'w', encoding='utf-8') as f:
            json.dump(self.search_index, f, indent=2, ensure_ascii=False)
        
        logger.info(f"✅ Índice salvo em: {self.search_index_file}")
    
    def generate_search_report(self) -> str:
        """
        Gera relatório do sistema de busca.
        
        Returns:
            Caminho do relatório
        """
        logger.info("📋 Gerando relatório do sistema de busca...")
        
        report = {
            "generation_date": datetime.now().isoformat(),
            "summary": {
                "total_documents": len(self.search_index["content_index"]),
                "total_tags": len(self.search_index["tag_index"]),
                "total_keywords": len(self.search_index["keyword_index"]),
                "total_categories": len(self.search_index["category_index"]),
                "similarity_matrix_size": len(self.search_index["similarity_matrix"])
            },
            "features": {
                "text_search": "Busca por texto com scoring inteligente",
                "tag_search": "Busca por tags específicas",
                "category_search": "Busca por categorias e subcategorias",
                "similarity_search": "Busca por documentos similares",
                "metadata_search": "Busca por metadados (tipo, status, tamanho)",
                "snippet_extraction": "Extração de snippets relevantes"
            },
            "statistics": {
                "documents_by_type": {k: len(v) for k, v in self.search_index["metadata_index"]["by_type"].items()},
                "documents_by_status": {k: len(v) for k, v in self.search_index["metadata_index"]["by_status"].items()},
                "documents_by_size": {k: len(v) for k, v in self.search_index["metadata_index"]["by_size"].items()}
            }
        }
        
        report_file = self.consolidated_dir / "advanced_search_report.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        logger.info(f"✅ Relatório salvo em: {report_file}")
        return str(report_file)
    
    def build_advanced_search(self) -> Dict[str, Any]:
        """
        Constrói sistema completo de busca avançada.
        
        Returns:
            Resultados da construção
        """
        logger.info("🚀 Iniciando construção do sistema de busca avançada...")
        
        # Construir índices
        self.build_content_index()
        self.build_semantic_index()
        self.build_category_index()
        self.build_tag_index()
        self.build_keyword_index()
        self.build_metadata_index()
        self.build_similarity_matrix()
        
        # Salvar índice
        self.save_search_index()
        
        # Gerar relatório
        report_path = self.generate_search_report()
        
        results = {
            "success": True,
            "documents_indexed": len(self.search_index["content_index"]),
            "tags_indexed": len(self.search_index["tag_index"]),
            "keywords_indexed": len(self.search_index["keyword_index"]),
            "categories_indexed": len(self.search_index["category_index"]),
            "similarity_matrix_size": len(self.search_index["similarity_matrix"]),
            "report_path": report_path
        }
        
        logger.info("✅ Sistema de busca avançada construído!")
        return results

def main():
    """Função principal do script."""
    print("🔄 Iniciando sistema de busca avançada...")
    
    search_system = AdvancedSearchSystem()
    
    # Construir sistema
    results = search_system.build_advanced_search()
    
    print(f"\n✅ Sistema de busca avançada construído!")
    print(f"📊 Documentos indexados: {results['documents_indexed']}")
    print(f"🏷️ Tags indexadas: {results['tags_indexed']}")
    print(f"🔑 Palavras-chave indexadas: {results['keywords_indexed']}")
    print(f"📂 Categorias indexadas: {results['categories_indexed']}")
    print(f"🔗 Matriz de similaridade: {results['similarity_matrix_size']} documentos")
    print(f"📁 Relatório: {results['report_path']}")

if __name__ == "__main__":
    main() 
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
- **Nome**: advanced_search_system
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

