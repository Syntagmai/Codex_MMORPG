#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Classificação Automática de Arquivos .md
Classifica todos os arquivos .md do projeto por categoria e função
"""

import os
import re
import json
import shutil
from pathlib import Path
from typing import Dict, List, Tuple, Set
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MDFileClassifier:
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.categories = {
            'reports': {
                'keywords': ['relatório', 'report', 'análise', 'analysis', 'resultado', 'result', 'estatística', 'statistics'],
                'patterns': [r'relatorio', r'report', r'analise', r'analysis', r'resultado', r'result'],
                'dest_path': 'logs/reports',
                'description': 'Relatórios e análises'
            },
            'indexes': {
                'keywords': ['índice', 'index', 'indice', 'categoria', 'category', 'lista', 'list'],
                'patterns': [r'indice', r'index', r'categoria', r'category', r'lista', r'list'],
                'dest_path': 'docs/indexes',
                'description': 'Índices e listas de categorização'
            },
            'guides': {
                'keywords': ['guia', 'guide', 'tutorial', 'como', 'how', 'manual', 'instrução', 'instruction'],
                'patterns': [r'guia', r'guide', r'tutorial', r'como', r'how', r'manual'],
                'dest_path': 'docs/guides',
                'description': 'Guias e tutoriais'
            },
            'glossary': {
                'keywords': ['glossário', 'glossary', 'termo', 'term', 'definição', 'definition', 'conceito', 'concept'],
                'patterns': [r'glossario', r'glossary', r'termo', r'term', r'definicao', r'definition'],
                'dest_path': 'docs/glossary',
                'description': 'Glossários e definições'
            },
            'systems': {
                'keywords': ['sistema', 'system', 'arquitetura', 'architecture', 'componente', 'component'],
                'patterns': [r'sistema', r'system', r'arquitetura', r'architecture', r'componente'],
                'dest_path': 'docs/systems',
                'description': 'Sistemas internos e arquitetura'
            },
            'habdel': {
                'keywords': ['habdel', 'metodologia', 'methodology', 'pesquisa', 'research', 'story', 'história'],
                'patterns': [r'habdel', r'metodologia', r'methodology', r'pesquisa', r'research'],
                'dest_path': 'habdel',
                'description': 'Metodologia Habdel e stories'
            },
            'educational': {
                'keywords': ['educacional', 'educational', 'aprendizado', 'learning', 'curso', 'course', 'exemplo', 'example'],
                'patterns': [r'educacional', r'educational', r'aprendizado', r'learning', r'curso', r'course'],
                'dest_path': 'wiki',
                'description': 'Conteúdo educacional para Obsidian'
            }
        }
        
        self.classification_results = {
            'total_files': 0,
            'classified_files': 0,
            'unclassified_files': 0,
            'categories': {},
            'errors': []
        }
        
        # Inicializar contadores por categoria
        for category in self.categories:
            self.classification_results['categories'][category] = {
                'count': 0,
                'files': []
            }

    def find_md_files(self) -> List[Path]:
        """Encontra todos os arquivos .md no projeto"""
        md_files = []
        for root, dirs, files in os.walk(self.project_root):
            # Ignorar pastas específicas
            dirs[:] = [d for d in dirs if d not in ['.git', '.obsidian', '__pycache__', 'node_modules']]
            
            for file in files:
                if file.endswith('.md'):
                    file_path = Path(root) / file
                    md_files.append(file_path)
        
        logger.info(f"Encontrados {len(md_files)} arquivos .md")
        return md_files

    def analyze_file_content(self, file_path: Path) -> Dict:
        """Analisa o conteúdo de um arquivo .md"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().lower()
            
            # Extrair frontmatter se existir
            frontmatter = {}
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    frontmatter_text = parts[1]
                    # Parse simples do frontmatter
                    for line in frontmatter_text.split('\n'):
                        if ':' in line:
                            key, value = line.split(':', 1)
                            frontmatter[key.strip()] = value.strip()
            
            # Extrair tags
            tags = []
            if 'tags:' in content:
                tags_match = re.search(r'tags:\s*\[(.*?)\]', content)
                if tags_match:
                    tags_text = tags_match.group(1)
                    tags = [tag.strip() for tag in tags_text.split(',')]
            
            return {
                'content': content,
                'frontmatter': frontmatter,
                'tags': tags,
                'size': len(content),
                'lines': content.count('\n')
            }
        except Exception as e:
            logger.error(f"Erro ao analisar {file_path}: {e}")
            return {'error': str(e)}

    def classify_file(self, file_path: Path, analysis: Dict) -> str:
        """Classifica um arquivo baseado em seu conteúdo e localização"""
        if 'error' in analysis:
            return 'error'
        
        content = analysis['content']
        tags = analysis['tags']
        frontmatter = analysis['frontmatter']
        
        # Verificar se já está na pasta correta
        relative_path = file_path.relative_to(self.project_root)
        
        # Se já está na wiki, provavelmente é educacional
        if str(relative_path).startswith('wiki/'):
            return 'educational'
        
        # Se já está na pasta habdel, manter lá
        if str(relative_path).startswith('habdel/'):
            return 'habdel'
        
        # Calcular score para cada categoria
        scores = {}
        for category, config in self.categories.items():
            score = 0
            
            # Verificar keywords no conteúdo
            for keyword in config['keywords']:
                if keyword in content:
                    score += 2
            
            # Verificar patterns no nome do arquivo
            filename = file_path.name.lower()
            for pattern in config['patterns']:
                if re.search(pattern, filename):
                    score += 3
            
            # Verificar tags
            for tag in tags:
                for keyword in config['keywords']:
                    if keyword in tag.lower():
                        score += 1
            
            # Verificar frontmatter
            if 'type' in frontmatter:
                type_value = frontmatter['type'].lower()
                for keyword in config['keywords']:
                    if keyword in type_value:
                        score += 2
            
            scores[category] = score
        
        # Retornar categoria com maior score
        if scores:
            best_category = max(scores, key=scores.get)
            if scores[best_category] > 0:
                return best_category
        
        return 'unclassified'

    def create_destination_dirs(self):
        """Cria as pastas de destino se não existirem"""
        for category, config in self.categories.items():
            dest_path = self.project_root / config['dest_path']
            dest_path.mkdir(parents=True, exist_ok=True)
            logger.info(f"Criada pasta: {dest_path}")

    def move_file(self, file_path: Path, category: str) -> bool:
        """Move um arquivo para sua categoria apropriada"""
        try:
            if category in self.categories:
                dest_path = self.project_root / self.categories[category]['dest_path'] / file_path.name
                
                # Se arquivo já existe no destino, adicionar sufixo
                counter = 1
                original_dest = dest_path
                while dest_path.exists():
                    stem = original_dest.stem
                    suffix = original_dest.suffix
                    dest_path = original_dest.parent / f"{stem}_{counter}{suffix}"
                    counter += 1
                
                shutil.move(str(file_path), str(dest_path))
                logger.info(f"Movido: {file_path.name} -> {dest_path}")
                return True
            else:
                logger.warning(f"Categoria não encontrada: {category}")
                return False
        except Exception as e:
            logger.error(f"Erro ao mover {file_path}: {e}")
            self.classification_results['errors'].append({
                'file': str(file_path),
                'error': str(e)
            })
            return False

    def classify_all_files(self, dry_run: bool = True) -> Dict:
        """Classifica todos os arquivos .md"""
        logger.info("Iniciando classificação de arquivos .md")
        
        # Criar pastas de destino
        if not dry_run:
            self.create_destination_dirs()
        
        # Encontrar todos os arquivos .md
        md_files = self.find_md_files()
        self.classification_results['total_files'] = len(md_files)
        
        # Classificar cada arquivo
        for file_path in md_files:
            logger.info(f"Analisando: {file_path}")
            
            # Analisar conteúdo
            analysis = self.analyze_file_content(file_path)
            
            # Classificar arquivo
            category = self.classify_file(file_path, analysis)
            
            # Registrar resultado
            if category in self.categories:
                self.classification_results['categories'][category]['count'] += 1
                self.classification_results['categories'][category]['files'].append(str(file_path))
                self.classification_results['classified_files'] += 1
                
                # Mover arquivo se não for dry run
                if not dry_run:
                    self.move_file(file_path, category)
            else:
                self.classification_results['unclassified_files'] += 1
                logger.warning(f"Arquivo não classificado: {file_path}")
        
        return self.classification_results

    def generate_report(self) -> str:
        """Gera relatório da classificação"""
        report = []
        report.append("# Relatório de Classificação de Arquivos .md")
        report.append("")
        report.append(f"**Total de arquivos analisados**: {self.classification_results['total_files']}")
        report.append(f"**Arquivos classificados**: {self.classification_results['classified_files']}")
        report.append(f"**Arquivos não classificados**: {self.classification_results['unclassified_files']}")
        report.append("")
        
        report.append("## Distribuição por Categoria")
        report.append("")
        for category, data in self.classification_results['categories'].items():
            if data['count'] > 0:
                config = self.categories.get(category, {})
                description = config.get('description', '')
                dest_path = config.get('dest_path', '')
                report.append(f"### {category.title()} ({data['count']} arquivos)")
                report.append(f"- **Descrição**: {description}")
                report.append(f"- **Destino**: {dest_path}")
                report.append("")
        
        if self.classification_results['errors']:
            report.append("## Erros Encontrados")
            report.append("")
            for error in self.classification_results['errors']:
                report.append(f"- **{error['file']}**: {error['error']}")
            report.append("")
        
        return "\n".join(report)

def main():
    """Função principal"""
    classifier = MDFileClassifier()
    
    # Primeiro fazer uma análise (dry run)
    logger.info("Executando análise inicial (dry run)...")
    results = classifier.classify_all_files(dry_run=True)
    
    # Gerar relatório
    report = classifier.generate_report()
    
    # Salvar relatório
    with open('logs/reports/md_classification_report.md', 'w', encoding='utf-8') as f:
        f.write(report)
    
    # Salvar resultados em JSON
    with open('logs/reports/md_classification_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    logger.info("Análise concluída. Verifique os relatórios em logs/reports/")
    logger.info("Para executar a classificação real, execute com --execute")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--execute":
        classifier = MDFileClassifier()
        results = classifier.classify_all_files(dry_run=False)
        report = classifier.generate_report()
        
        with open('logs/reports/md_classification_final_report.md', 'w', encoding='utf-8') as f:
            f.write(report)
        
        logger.info("Classificação executada com sucesso!")
    else:
        main() 