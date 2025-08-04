#!/usr/bin/env python3
"""
Script para verificar deep links na wiki OTClient
Verifica todos os links internos e identifica problemas de navegação
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Set, Tuple
from datetime import datetime

class WikiLinkVerifier:
    def __init__(self, wiki_dir: str = ".."):
        self.wiki_dir = Path(wiki_dir)
        self.all_files = set()
        self.links_found = {}
        self.broken_links = []
        self.missing_links = []
        self.orphaned_files = []
        
    def scan_all_files(self):
        """Escaneia todos os arquivos .md na wiki"""
        print("🔍 Escaneando arquivos da wiki...")
        
        for file_path in self.wiki_dir.rglob("*.md"):
            if file_path.is_file():
                # Normalizar caminho relativo
                relative_path = file_path.relative_to(self.wiki_dir)
                self.all_files.add(str(relative_path))
                
        print(f"✅ Encontrados {len(self.all_files)} arquivos .md")
        
    def extract_links_from_file(self, file_path: Path) -> List[str]:
        """Extrai todos os links de um arquivo markdown"""
        links = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Padrões de links Obsidian
            patterns = [
                r'\[\[([^\]]+)\]\]',  # [[link]]
                r'\[([^\]]+)\]\(([^)]+)\)',  # [text](link)
                r'\[\[([^\]]+)\|([^\]]+)\]\]',  # [[link|text]]
            ]
            
            for pattern in patterns:
                matches = re.findall(pattern, content)
                for match in matches:
                    if isinstance(match, tuple):
                        # Para [[link|text]] ou [text](link)
                        link = match[0] if '|' not in match[0] else match[1]
                    else:
                        link = match
                    
                    # Limpar link
                    link = link.strip()
                    if link and not link.startswith('http'):
                        links.append(link)
                        
        except Exception as e:
            print(f"❌ Erro ao ler {file_path}: {e}")
            
        return links
    
    def verify_links(self):
        """Verifica todos os links na wiki"""
        print("🔗 Verificando links...")
        
        for file_path in self.wiki_dir.rglob("*.md"):
            if not file_path.is_file():
                continue
                
            relative_path = str(file_path.relative_to(self.wiki_dir))
            links = self.extract_links_from_file(file_path)
            
            if links:
                self.links_found[relative_path] = links
                
                for link in links:
                    if not self.is_link_valid(link, relative_path):
                        self.broken_links.append({
                            'file': relative_path,
                            'link': link,
                            'type': 'broken'
                        })
        
        print(f"✅ Verificados {len(self.links_found)} arquivos com links")
        
    def is_link_valid(self, link: str, source_file: str) -> bool:
        """Verifica se um link é válido"""
        # Remover âncora se existir
        if '#' in link:
            link = link.split('#')[0]
            
        # Se link vazio, considerar válido (âncora local)
        if not link:
            return True
            
        # Verificar se arquivo existe
        if link in self.all_files:
            return True
            
        # Verificar variações do link
        variations = [
            link,
            link + '.md',
            link.replace(' ', '_'),
            link.replace('_', ' '),
        ]
        
        for variation in variations:
            if variation in self.all_files:
                return True
                
        return False
        
    def find_orphaned_files(self):
        """Encontra arquivos sem links apontando para eles"""
        print("🔍 Procurando arquivos órfãos...")
        
        linked_files = set()
        for links in self.links_found.values():
            for link in links:
                if '#' in link:
                    link = link.split('#')[0]
                if link:
                    linked_files.add(link)
                    
        for file_path in self.all_files:
            if file_path not in linked_files:
                self.orphaned_files.append(file_path)
                
        print(f"✅ Encontrados {len(self.orphaned_files)} arquivos órfãos")
        
    def generate_report(self):
        """Gera relatório completo"""
        print("📊 Gerando relatório...")
        
        report = {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'total_files': len(self.all_files),
                'files_with_links': len(self.links_found),
                'total_links': sum(len(links) for links in self.links_found.values()),
                'broken_links': len(self.broken_links),
                'orphaned_files': len(self.orphaned_files)
            },
            'broken_links': self.broken_links,
            'orphaned_files': self.orphaned_files,
            'link_statistics': {
                'files_with_most_links': sorted(
                    self.links_found.items(),
                    key=lambda x: len(x[1]),
                    reverse=True
                )[:10]
            }
        }
        
        # Salvar relatório
        report_path = self.wiki_dir / 'maps' / 'deep_links_report.json'
        report_path.parent.mkdir(parents=True, exist_ok=True)
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
            
        print(f"📄 Relatório salvo em: {report_path}")
        
        return report
        
    def print_summary(self, report: Dict):
        """Imprime resumo do relatório"""
        print("\n" + "="*60)
        print("📊 RELATÓRIO DE VERIFICAÇÃO DE DEEP LINKS")
        print("="*60)
        
        metadata = report['metadata']
        print(f"📁 Total de arquivos: {metadata['total_files']}")
        print(f"🔗 Arquivos com links: {metadata['files_with_links']}")
        print(f"🔗 Total de links: {metadata['total_links']}")
        print(f"❌ Links quebrados: {metadata['broken_links']}")
        print(f"📄 Arquivos órfãos: {metadata['orphaned_files']}")
        
        if self.broken_links:
            print(f"\n❌ LINKS QUEBRADOS ENCONTRADOS:")
            for broken in self.broken_links[:10]:  # Mostrar apenas os primeiros 10
                print(f"  📄 {broken['file']} → {broken['link']}")
            if len(self.broken_links) > 10:
                print(f"  ... e mais {len(self.broken_links) - 10} links quebrados")
                
        if self.orphaned_files:
            print(f"\n📄 ARQUIVOS ÓRFÃOS:")
            for orphaned in self.orphaned_files[:10]:  # Mostrar apenas os primeiros 10
                print(f"  📄 {orphaned}")
            if len(self.orphaned_files) > 10:
                print(f"  ... e mais {len(self.orphaned_files) - 10} arquivos órfãos")
                
        print("\n" + "="*60)
        
    def run(self):
        """Executa verificação completa"""
        print("🚀 Iniciando verificação de deep links da wiki...")
        
        self.scan_all_files()
        self.verify_links()
        self.find_orphaned_files()
        
        report = self.generate_report()
        self.print_summary(report)
        
        return report

def main():
    """Função principal"""
    verifier = WikiLinkVerifier()
    report = verifier.run()
    
    # Retornar código de saída baseado nos problemas encontrados
    if report['metadata']['broken_links'] > 0 or report['metadata']['orphaned_files'] > 0:
        print("⚠️  Problemas encontrados na wiki!")
        return 1
    else:
        print("✅ Wiki está com links perfeitos!")
        return 0

if __name__ == "__main__":
    exit(main()) 