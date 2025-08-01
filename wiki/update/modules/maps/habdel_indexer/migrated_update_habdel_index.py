# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: update_habdel_index.py
Módulo de Destino: maps.habdel_indexer
Data de Migração: 2025-08-01 12:21:35

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import HabdelindexerModule

# Conteúdo original do script
#!/usr/bin/env python3
"""
Script para indexação da pasta habdel - Documentação Original e Planejamento
Atualiza: wiki/maps/habdel_index.json
"""
import json
import re
from datetime import datetime

class HabdelIndexer:
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.habdel_path = self.project_root / "wiki" / "habdel"
        self.stories = []
        self.categories = {
            "UI": {"name": "Sistema de Interface", "stories": []},
            "GAME": {"name": "Sistema de Jogo", "stories": []},
            "CORE": {"name": "Sistema Central", "stories": []},
            "GUIDE": {"name": "Guias e Tutoriais", "stories": []},
            "REF": {"name": "Referências", "stories": []}
        }
        
    def scan_habdel_files(self) -> List[str]:
        """Escaneia todos os arquivos da pasta habdel"""
        if not self.habdel_path.exists():
            print(f"Pasta habdel não encontrada: {self.habdel_path}")
            return []
        
        habdel_files = []
        for file_path in self.habdel_path.glob("*.md"):
            habdel_files.append(str(file_path))
        
        return sorted(habdel_files)
    
    def extract_story_info(self, file_path: str) -> Dict[str, Any]:
        """Extrai informações de story de um arquivo"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            file_name = Path(file_path).name
            file_stem = Path(file_path).stem
            
            # Tentar extrair ID da story do nome do arquivo
            story_id = None
            story_category = None
            
            # Padrões de ID de story
            patterns = [
                r'(UI-\d+)',
                r'(GAME-\d+)', 
                r'(CORE-\d+)',
                r'(GUIDE-\d+)',
                r'(REF-\d+)'
            ]
            
            for pattern in patterns:
                match = re.search(pattern, file_name)
                if match:
                    story_id = match.group(1)
                    story_category = story_id.split('-')[0]
                    break
            
            # Se não encontrou ID, tentar categorizar pelo nome
            if not story_category:
                if 'ui' in file_name.lower() or 'widget' in file_name.lower():
                    story_category = 'UI'
                elif 'game' in file_name.lower() or 'creature' in file_name.lower() or 'item' in file_name.lower():
                    story_category = 'GAME'
                elif 'core' in file_name.lower() or 'module' in file_name.lower() or 'config' in file_name.lower():
                    story_category = 'CORE'
                elif 'guide' in file_name.lower() or 'start' in file_name.lower() or 'practice' in file_name.lower():
                    story_category = 'GUIDE'
                elif 'ref' in file_name.lower() or 'api' in file_name.lower() or 'cheat' in file_name.lower():
                    story_category = 'REF'
                else:
                    story_category = 'UNKNOWN'
            
            # Extrair título do conteúdo
            title = self.extract_title(content, file_stem)
            
            # Extrair descrição
            description = self.extract_description(content)
            
            # Determinar status baseado no conteúdo
            status = self.determine_status(content, file_name)
            
            # Extrair tags
            tags = self.extract_tags(content)
            
            # Contar linhas e tamanho
            lines = len(content.split('\n'))
            size = len(content)
            
            story_info = {
                "id": story_id or f"{story_category}-{file_stem}",
                "file": file_name,
                "path": str(file_path),
                "title": title,
                "category": story_category,
                "status": status,
                "description": description,
                "tags": tags,
                "lines": lines,
                "size": size,
                "last_modified": datetime.fromtimestamp(Path(file_path).stat().st_mtime).isoformat()
            }
            
            return story_info
            
        except Exception as e:
            print(f"Erro ao processar {file_path}: {e}")
            return None
    
    def extract_title(self, content: str, file_stem: str) -> str:
        """Extrai título do conteúdo"""
        # Tentar encontrar título no início do arquivo
        lines = content.split('\n')
        for line in lines[:10]:  # Primeiras 10 linhas
            line = line.strip()
            if line.startswith('# '):
                return line[2:].strip()
            elif line.startswith('## '):
                return line[3:].strip()
        
        # Se não encontrou, usar nome do arquivo
        return file_stem.replace('_', ' ').replace('-', ' ').title()
    
    def extract_description(self, content: str) -> str:
        """Extrai descrição do conteúdo"""
        lines = content.split('\n')
        for line in lines[:20]:  # Primeiras 20 linhas
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('---'):
                return line[:200] + "..." if len(line) > 200 else line
        
        return "Sem descrição disponível"
    
    def determine_status(self, content: str, file_name: str) -> str:
        """Determina status baseado no conteúdo"""
        content_lower = content.lower()
        
        if 'done' in content_lower or 'complete' in content_lower or 'finished' in content_lower:
            return 'done'
        elif 'in progress' in content_lower or 'wip' in content_lower or 'working' in content_lower:
            return 'in_progress'
        elif 'todo' in content_lower or 'pending' in content_lower or 'planned' in content_lower:
            return 'todo'
        elif 'draft' in content_lower or 'sketch' in content_lower:
            return 'draft'
        else:
            return 'unknown'
    
    def extract_tags(self, content: str) -> List[str]:
        """Extrai tags do conteúdo"""
        tags = []
        
        # Procurar por tags no formato [tag] ou #tag
        tag_patterns = [
            r'\[([^\]]+)\]',
            r'#(\w+)',
            r'tags?:\s*\[([^\]]+)\]'
        ]
        
        for pattern in tag_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                if isinstance(match, str):
                    tags.extend([tag.strip() for tag in match.split(',')])
        
        return list(set(tags))  # Remover duplicatas
    
    def categorize_stories(self):
        """Categoriza as stories"""
        for story in self.stories:
            category = story.get('category', 'UNKNOWN')
            if category in self.categories:
                self.categories[category]['stories'].append(story)
            else:
                self.categories['UNKNOWN'] = self.categories.get('UNKNOWN', {'name': 'Desconhecido', 'stories': []})
                self.categories['UNKNOWN']['stories'].append(story)
    
    def generate_statistics(self) -> Dict[str, Any]:
        """Gera estatísticas da pasta habdel"""
        stats = {
            "total_stories": len(self.stories),
            "by_category": {},
            "by_status": {},
            "total_lines": 0,
            "total_size": 0
        }
        
        # Estatísticas por categoria
        for category, cat_info in self.categories.items():
            stats["by_category"][category] = len(cat_info["stories"])
        
        # Estatísticas por status
        status_counts = {}
        for story in self.stories:
            status = story.get('status', 'unknown')
            status_counts[status] = status_counts.get(status, 0) + 1
            stats["total_lines"] += story.get('lines', 0)
            stats["total_size"] += story.get('size', 0)
        
        stats["by_status"] = status_counts
        
        return stats
    
    def generate_search_index(self) -> Dict[str, Any]:
        """Gera índice de busca"""
        search_index = {
            "by_title": {},
            "by_tag": {},
            "by_status": {},
            "by_category": {}
        }
        
        # Indexar por título
        for story in self.stories:
            title = story.get('title', '').lower()
            if title not in search_index["by_title"]:
                search_index["by_title"][title] = []
            search_index["by_title"][title].append(story['id'])
        
        # Indexar por tag
        for story in self.stories:
            for tag in story.get('tags', []):
                tag_lower = tag.lower()
                if tag_lower not in search_index["by_tag"]:
                    search_index["by_tag"][tag_lower] = []
                search_index["by_tag"][tag_lower].append(story['id'])
        
        # Indexar por status
        for story in self.stories:
            status = story.get('status', 'unknown')
            if status not in search_index["by_status"]:
                search_index["by_status"][status] = []
            search_index["by_status"][status].append(story['id'])
        
        # Indexar por categoria
        for story in self.stories:
            category = story.get('category', 'UNKNOWN')
            if category not in search_index["by_category"]:
                search_index["by_category"][category] = []
            search_index["by_category"][category].append(story['id'])
        
        return search_index
    
    def generate_habdel_index(self) -> Dict[str, Any]:
        """Gera o índice completo da pasta habdel"""
        print("Gerando índice da pasta habdel...")
        
        # Escanear arquivos
        habdel_files = self.scan_habdel_files()
        print(f"Encontrados {len(habdel_files)} arquivos")
        
        # Processar cada arquivo
        for file_path in habdel_files:
            story_info = self.extract_story_info(file_path)
            if story_info:
                self.stories.append(story_info)
        
        # Categorizar stories
        self.categorize_stories()
        
        # Gerar estatísticas
        statistics = self.generate_statistics()
        
        # Gerar índice de busca
        search_index = self.generate_search_index()
        
        # Estrutura final
        habdel_index = {
            "metadata": {
                "version": "1.0",
                "last_updated": datetime.now().isoformat(),
                "total_files": len(habdel_files),
                "description": "Índice da documentação original e planejamento (pasta habdel)"
            },
            "categories": self.categories,
            "statistics": statistics,
            "search_index": search_index
        }
        
        return habdel_index
    
    def save_index(self, habdel_index: Dict[str, Any], output_file: str = "wiki/maps/habdel_index.json"):
        """Salva o índice em arquivo JSON"""
        try:
            # Criar diretório se não existir
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(habdel_index, f, indent=2, ensure_ascii=False)
            
            print(f"Índice salvo em {output_file}")
            
        except Exception as e:
            print(f"Erro ao salvar índice: {e}")
    
    def update_index(self):
        """Atualiza o índice da pasta habdel"""
        habdel_index = self.generate_habdel_index()
        return self.save_index(habdel_index)

def main():
    """Função principal"""
    print("Iniciando indexação da pasta habdel...")
    
    try:
        indexer = HabdelIndexer()
        success = indexer.update_index()
        
        if success:
            print("Indexação da pasta habdel concluída com sucesso!")
        else:
            print("Erro na indexação da pasta habdel!")
            
    except Exception as e:
        print(f"Erro durante indexação: {e}")

if __name__ == "__main__":
    main() 


# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = HabdelindexerModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script update_habdel_index.py executado com sucesso via módulo maps.habdel_indexer")
    else:
        print(f"❌ Erro na execução do script update_habdel_index.py via módulo maps.habdel_indexer")
