# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
MAX_ITEMS = 100

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: migrated_knowledge_consolidation_system.py
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
Script Migrado: knowledge_consolidation_system.py
Módulo de Destino: analysis.knowledge_consolidator
Data de Migração: 2025-08-01 12:21:34

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import KnowledgeconsolidatorModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Consolidação Automática de Conhecimento
==================================================

Este script integra 53 documentos + 23 mapas JSON em wiki unificada
com navegação inteligente e estrutura hierárquica.

Autor: Sistema BMAD - Knowledge Manager
Data: 2025-08-01
"""

import json
import shutil
from datetime import datetime
import logging

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class KnowledgeConsolidationSystem:
    """Sistema de consolidação automática de conhecimento"""
    
    def __init__(self, wiki_dir: str = "wiki"):
        """
        Inicializa o sistema de consolidação.
        
        Args:
            wiki_dir: Diretório da wiki
        """
        self.wiki_dir = Path(wiki_dir)
        self.consolidated_dir = self.wiki_dir / "consolidated"
        self.docs_dir = self.wiki_dir / "docs"
        self.maps_dir = self.wiki_dir / "maps"
        self.bmad_dir = self.wiki_dir / "bmad"
        
        # Criar diretório consolidado se não existir
        self.consolidated_dir.mkdir(exist_ok=True)
        
        # Estrutura de consolidação
        self.consolidation_structure = {
            "otclient": {
                "research": [],
                "documentation": [],
                "modules": [],
                "analysis": []
            },
            "canary": {
                "research": [],
                "documentation": [],
                "modules": [],
                "analysis": []
            },
            "bmad": {
                "agents": [],
                "workflows": [],
                "knowledge": [],
                "tools": []
            },
            "integration": {
                "comparisons": [],
                "guides": [],
                "patterns": [],
                "apis": []
            },
            "education": {
                "courses": [],
                "lessons": [],
                "exercises": [],
                "certifications": []
            },
            "performance": {
                "optimization": [],
                "metrics": [],
                "cache": [],
                "logs": []
            }
        }
        
    def scan_documents(self) -> Dict[str, List[str]]:
        """
        Escaneia todos os documentos disponíveis.
        
        Returns:
            Dicionário com documentos organizados por categoria
        """
        logger.info("🔍 Escaneando documentos para consolidação...")
        
        documents = {
            "markdown": [],
            "json": [],
            "python": [],
            "other": []
        }
        
        # Escanear docs/
        if self.docs_dir.exists():
            for file_path in self.docs_dir.rglob("*"):
                if file_path.is_file():
                    if file_path.suffix == ".md":
                        documents["markdown"].append(str(file_path))
                    elif file_path.suffix == ".json":
                        documents["json"].append(str(file_path))
                    elif file_path.suffix == ".py":
                        documents["python"].append(str(file_path))
                    else:
                        documents["other"].append(str(file_path))
        
        # Escanear bmad/
        if self.bmad_dir.exists():
            for file_path in self.bmad_dir.rglob("*"):
                if file_path.is_file():
                    if file_path.suffix == ".md":
                        documents["markdown"].append(str(file_path))
                    elif file_path.suffix == ".json":
                        documents["json"].append(str(file_path))
                    elif file_path.suffix == ".py":
                        documents["python"].append(str(file_path))
                    else:
                        documents["other"].append(str(file_path))
        
        # Escanear maps/
        if self.maps_dir.exists():
            for file_path in self.maps_dir.glob("*.json"):
                documents["json"].append(str(file_path))
        
        logger.info(f"📊 Documentos encontrados:")
        logger.info(f"  - Markdown: {len(documents['markdown'])}")
        logger.info(f"  - JSON: {len(documents['json'])}")
        logger.info(f"  - Python: {len(documents['python'])}")
        logger.info(f"  - Outros: {len(documents['other'])}")
        
        return documents
    
    def categorize_documents(self, documents: Dict[str, List[str]]) -> Dict[str, List[str]]:
        """
        Categoriza documentos por tipo de conteúdo.
        
        Args:
            documents: Documentos escaneados
            
        Returns:
            Documentos categorizados
        """
        logger.info("🏷️ Categorizando documentos...")
        
        categorized = {
            "otclient_research": [],
            "canary_research": [],
            "bmad_agents": [],
            "integration_studies": [],
            "educational_content": [],
            "performance_analysis": [],
            "documentation": [],
            "maps_and_indexes": []
        }
        
        for file_path in documents["markdown"]:
            path = Path(file_path)
            filename = path.name.lower()
            
            if "otclient" in filename or "otclient" in str(path):
                categorized["otclient_research"].append(file_path)
            elif "canary" in filename or "canary" in str(path):
                categorized["canary_research"].append(file_path)
            elif "agent" in filename or "bmad" in str(path):
                categorized["bmad_agents"].append(file_path)
            elif "integration" in filename or "comparison" in filename:
                categorized["integration_studies"].append(file_path)
            elif "course" in filename or "lesson" in filename or "education" in filename:
                categorized["educational_content"].append(file_path)
            elif "performance" in filename or "optimization" in filename:
                categorized["performance_analysis"].append(file_path)
            else:
                categorized["documentation"].append(file_path)
        
        # Categorizar mapas JSON
        for file_path in documents["json"]:
            path = Path(file_path)
            if "map" in path.name.lower() or "index" in path.name.lower():
                categorized["maps_and_indexes"].append(file_path)
        
        logger.info(f"📋 Documentos categorizados:")
        for category, files in categorized.items():
            logger.info(f"  - {category}: {len(files)} arquivos")
        
        return categorized
    
    def create_consolidation_structure(self, categorized_docs: Dict[str, List[str]]):
        """
        Cria estrutura de consolidação organizada.
        
        Args:
            categorized_docs: Documentos categorizados
        """
        logger.info("🏗️ Criando estrutura de consolidação...")
        
        # Criar diretórios principais
        for main_category in self.consolidation_structure.keys():
            category_dir = self.consolidated_dir / main_category
            category_dir.mkdir(exist_ok=True)
            
            for subcategory in self.consolidation_structure[main_category].keys():
                subcategory_dir = category_dir / subcategory
                subcategory_dir.mkdir(exist_ok=True)
        
        # Mapear documentos para estrutura
        mapping = {
            "otclient_research": ("otclient", "research"),
            "canary_research": ("canary", "research"),
            "bmad_agents": ("bmad", "agents"),
            "integration_studies": ("integration", "comparisons"),
            "educational_content": ("education", "courses"),
            "performance_analysis": ("performance", "optimization"),
            "documentation": ("otclient", "documentation"),
            "maps_and_indexes": ("integration", "patterns")
        }
        
        for category, files in categorized_docs.items():
            if category in mapping:
                main_cat, sub_cat = mapping[category]
                target_dir = self.consolidated_dir / main_cat / sub_cat
                
                for file_path in files:
                    source_path = Path(file_path)
                    target_path = target_dir / source_path.name
                    
                    try:
                        shutil.copy2(source_path, target_path)
                        logger.info(f"📄 Copiado: {source_path.name} → {target_path}")
                    except Exception as e:
                        logger.error(f"❌ Erro ao copiar {source_path}: {e}")
        
        logger.info("✅ Estrutura de consolidação criada")
    
    def create_navigation_index(self):
        """
        Cria índice de navegação para a wiki consolidada.
        """
        logger.info("🧭 Criando índice de navegação...")
        
        navigation_data = {
            "consolidation_date": datetime.now().isoformat(),
            "total_documents": 0,
            "structure": {},
            "quick_links": {},
            "search_index": {}
        }
        
        # Contar documentos e criar estrutura
        for main_category in self.consolidation_structure.keys():
            category_dir = self.consolidated_dir / main_category
            if category_dir.exists():
                navigation_data["structure"][main_category] = {}
                
                for subcategory in self.consolidation_structure[main_category].keys():
                    subcategory_dir = category_dir / subcategory
                    if subcategory_dir.exists():
                        files = list(subcategory_dir.glob("*"))
                        navigation_data["structure"][main_category][subcategory] = {
                            "file_count": len(files),
                            "files": [f.name for f in files if f.is_file()]
                        }
                        navigation_data["total_documents"] += len(files)
        
        # Criar links rápidos
        navigation_data["quick_links"] = {
            "otclient_research": "otclient/research/",
            "canary_research": "canary/research/",
            "bmad_agents": "bmad/agents/",
            "integration_studies": "integration/comparisons/",
            "educational_content": "education/courses/",
            "performance_analysis": "performance/optimization/"
        }
        
        # Salvar índice de navegação
        navigation_file = self.consolidated_dir / "navigation_index.json"
        with open(navigation_file, 'w', encoding='utf-8') as f:
            json.dump(navigation_data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"✅ Índice de navegação criado: {navigation_file}")
        logger.info(f"📊 Total de documentos consolidados: {navigation_data['total_documents']}")
        
        return navigation_data
    
    def create_consolidation_report(self, documents: Dict[str, List[str]], 
                                  navigation_data: Dict[str, Any]) -> str:
        """
        Cria relatório de consolidação.
        
        Args:
            documents: Documentos originais
            navigation_data: Dados de navegação
            
        Returns:
            Caminho do relatório
        """
        logger.info("📋 Criando relatório de consolidação...")
        
        report = {
            "consolidation_date": datetime.now().isoformat(),
            "summary": {
                "total_documents_processed": sum(len(files) for files in documents.values()),
                "total_documents_consolidated": navigation_data["total_documents"],
                "consolidation_efficiency": f"{(navigation_data['total_documents'] / sum(len(files) for files in documents.values()) * 100):.1f}%"
            },
            "document_types": {
                "markdown": len(documents["markdown"]),
                "json": len(documents["json"]),
                "python": len(documents["python"]),
                "other": len(documents["other"])
            },
            "structure_created": navigation_data["structure"],
            "quick_links": navigation_data["quick_links"]
        }
        
        report_file = self.consolidated_dir / "consolidation_report.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        logger.info(f"✅ Relatório salvo em: {report_file}")
        return str(report_file)
    
    def consolidate_knowledge(self) -> Dict[str, Any]:
        """
        Executa consolidação completa do conhecimento.
        
        Returns:
            Resultados da consolidação
        """
        logger.info("🚀 Iniciando consolidação de conhecimento...")
        
        # Escanear documentos
        documents = self.scan_documents()
        
        # Categorizar documentos
        categorized_docs = self.categorize_documents(documents)
        
        # Criar estrutura de consolidação
        self.create_consolidation_structure(categorized_docs)
        
        # Criar índice de navegação
        navigation_data = self.create_navigation_index()
        
        # Criar relatório
        report_path = self.create_consolidation_report(documents, navigation_data)
        
        results = {
            "success": True,
            "documents_processed": sum(len(files) for files in documents.values()),
            "documents_consolidated": navigation_data["total_documents"],
            "consolidation_efficiency": f"{(navigation_data['total_documents'] / sum(len(files) for files in documents.values()) * 100):.1f}%",
    
    
    
    
            "structure_created": navigation_data["structure"],
            "report_path": report_path
        }
        
        logger.info("✅ Consolidação de conhecimento concluída!")
        return results

def main():
    """Função principal do script."""
    print("🔄 Iniciando sistema de consolidação de conhecimento...")
    
    consolidator = KnowledgeConsolidationSystem()
    
    # Executar consolidação
    results = consolidator.consolidate_knowledge()
    
    print(f"\n✅ Consolidação concluída!")
    print(f"📊 Documentos processados: {results['documents_processed']}")
    print(f"📋 Documentos consolidados: {results['documents_consolidated']}")
    print(f"📈 Eficiência: {results['consolidation_efficiency']}")
    print(f"📁 Relatório: {results['report_path']}")

if __name__ == "__main__":
    main() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = KnowledgeconsolidatorModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script knowledge_consolidation_system.py executado com sucesso via módulo analysis.knowledge_consolidator")
    else:
        print(f"❌ Erro na execução do script knowledge_consolidation_system.py via módulo analysis.knowledge_consolidator")


# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = MapupdaterModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script migrated_knowledge_consolidation_system.py executado com sucesso via módulo maps.map_updater")
    else:
        print(f"❌ Erro na execução do script migrated_knowledge_consolidation_system.py via módulo maps.map_updater")
