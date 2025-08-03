#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from unicode_aliases import *
"""
Conversor Obsidian → mdBook
==========================

Script que converte automaticamente arquivos do Obsidian para o formato mdBook,
mantendo a estrutura e convertendo links internos.

Autor: Sistema BMAD - Codex MMORPG
Versão: 1.0.0
Data: 2025-01-27
"""

import os
import re
import shutil
from pathlib import Path
from typing import Dict, List, Optional
import logging

class ObsidianToMdBookConverter:
    """Conversor de Obsidian para mdBook"""
    
    def __init__(self, obsidian_path: str = "wiki/docs", mdbook_path: str = "docs/src"):
        self.obsidian_path = Path(obsidian_path)
        self.mdbook_path = Path(mdbook_path)
        self.link_mapping = {}
        
        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
    def convert_wikilinks(self, content: str) -> str:
        """Converte links internos do Obsidian para Markdown padrão"""
        # Converter [[arquivo]] para [arquivo](arquivo.md)
        content = re.sub(r'\[\[([^\]]+)\]\]', r'[\1](\1.md)', content)
        
        # Converter [[arquivo|texto]] para [texto](arquivo.md)
        content = re.sub(r'\[\[([^|]+)\|([^\]]+)\]\]', r'[\2](\1.md)', content)
        
        return content
    
    def convert_callouts(self, content: str) -> str:
        """Converte callouts do Obsidian para HTML"""
        # Converter > [!info] para <div class="info">
        content = re.sub(r'> \[!(\w+)\](.*)', r'<div class="\1">\2', content)
        
        # Converter > [!warning] para <div class="warning">
        content = re.sub(r'> \[!warning\](.*)', r'<div class="warning">\1</div>', content)
        
        # Converter > [!success] para <div class="success">
        content = re.sub(r'> \[!success\](.*)', r'<div class="success">\1</div>', content)
        
        # Converter > [!error] para <div class="error">
        content = re.sub(r'> \[!error\](.*)', r'<div class="error">\1</div>', content)
        
        return content
    
    def convert_frontmatter(self, content: str) -> str:
        """Remove frontmatter do Obsidian (não suportado pelo mdBook)"""
        # Remover frontmatter entre ---
        content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
        
        return content
    
    def sanitize_filename(self, filename: str) -> str:
        """Sanitiza nome de arquivo para mdBook"""
        # Remover caracteres especiais
        filename = re.sub(r'[^\w\-_.]', '_', filename)
        # Converter para lowercase
        filename = filename.lower()
        return filename
    
    def convert_file(self, obsidian_file: Path, mdbook_file: Path) -> bool:
        """Converte um arquivo do Obsidian para mdBook"""
        try:
            # Ler conteúdo do arquivo Obsidian
            with open(obsidian_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Converter links internos
            content = self.convert_wikilinks(content)
            
            # Converter callouts
            content = self.convert_callouts(content)
            
            # Remover frontmatter
            content = self.convert_frontmatter(content)
            
            # Criar diretório de destino se não existir
            mdbook_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Salvar arquivo convertido
            with open(mdbook_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self.logger.info(f"✅ Convertido: {obsidian_file} → {mdbook_file}")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao converter {obsidian_file}: {e}")
            return False
    
    def get_mdbook_path(self, obsidian_file: Path) -> Path:
        """Calcula o caminho correspondente no mdBook"""
        # Calcular caminho relativo
        relative_path = obsidian_file.relative_to(self.obsidian_path)
        
        # Mapear pastas do Obsidian para mdBook
        path_mapping = {
            'otclient/guides/': 'otclient/',
            'canary/guides/': 'canary/',
            'courses/': 'courses/',
            'lessons/': 'courses/',
            'laboratory/': 'laboratory/',
            'integration/': 'integration/',
            'research/habdel/': 'research/habdel/',
            'dashboard/': 'dashboard/'
        }
        
        # Aplicar mapeamento
        path_str = str(relative_path)
        for obsidian_path, mdbook_path in path_mapping.items():
            if path_str.startswith(obsidian_path):
                path_str = path_str.replace(obsidian_path, mdbook_path, 1)
                break
        
        return self.mdbook_path / path_str
    
    def convert_directory(self) -> bool:
        """Converte todo o diretório Obsidian para mdBook"""
        self.logger.info("🔄 Iniciando conversão Obsidian → mdBook...")
        
        # Criar diretório de destino
        self.mdbook_path.mkdir(parents=True, exist_ok=True)
        
        # Converter arquivos recursivamente
        success_count = 0
        total_count = 0
        
        for obsidian_file in self.obsidian_path.rglob("*.md"):
            # Calcular caminho correspondente no mdBook
            mdbook_file = self.get_mdbook_path(obsidian_file)
            
            if self.convert_file(obsidian_file, mdbook_file):
                success_count += 1
            total_count += 1
        
        self.logger.info(f"✅ Conversão concluída: {success_count}/{total_count} arquivos")
        return success_count == total_count
    
    def update_summary(self) -> bool:
        """Atualiza o SUMMARY.md com base nos arquivos convertidos"""
        try:
            summary_content = "# Sumário\n\n[Introdução](README.md)\n\n"
            
            # Estrutura de seções
            sections = {
                'otclient': '# 📚 OTClient\n\n',
                'canary': '# 🗄️ Canary\n\n',
                'courses': '# 🎓 Cursos e Lições\n\n',
                'laboratory': '# 🧪 Laboratório\n\n',
                'integration': '# 🔗 Integração\n\n',
                'research': '# 📊 Pesquisa\n\n',
                'dashboard': '# 🎯 Dashboard\n\n'
            }
            
            # Coletar arquivos por seção
            for mdbook_file in self.mdbook_path.rglob("*.md"):
                if mdbook_file.name in ['README.md', 'SUMMARY.md']:
                    continue
                
                relative_path = mdbook_file.relative_to(self.mdbook_path)
                section = relative_path.parts[0] if relative_path.parts else 'other'
                
                if section in sections:
                    title = mdbook_file.stem.replace('_', ' ').title()
                    link = f"- [{title}]({relative_path})\n"
                    sections[section] += link
            
            # Montar SUMMARY.md
            for section_content in sections.values():
                if section_content != '# 📚 OTClient\n\n' and section_content != '# 🗄️ Canary\n\n' and section_content != '# 🎓 Cursos e Lições\n\n' and section_content != '# 🧪 Laboratório\n\n' and section_content != '# 🔗 Integração\n\n' and section_content != '# 📊 Pesquisa\n\n' and section_content != '# 🎯 Dashboard\n\n':
                    summary_content += section_content + "\n"
            
            # Salvar SUMMARY.md
            summary_file = self.mdbook_path / "SUMMARY.md"
            with open(summary_file, 'w', encoding='utf-8') as f:
                f.write(summary_content)
            
            self.logger.info("✅ SUMMARY.md atualizado")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao atualizar SUMMARY.md: {e}")
            return False

def main():
    """Função principal"""
    converter = ObsidianToMdBookConverter()
    
    # Converter arquivos
    if converter.convert_directory():
        print("🎉 Conversão bem-sucedida!")
        
        # Atualizar SUMMARY.md
        if converter.update_summary():
            print("✅ SUMMARY.md atualizado!")
        else:
            print("⚠️ Erro ao atualizar SUMMARY.md")
    else:
        print("⚠️ Conversão com erros")

if __name__ == "__main__":
    main() 