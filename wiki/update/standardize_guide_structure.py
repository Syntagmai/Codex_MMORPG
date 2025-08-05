#!/usr/bin/env python3
"""
Script para padronizar a estrutura de todos os guias da wiki.
Adiciona índices detalhados e melhora formatação visual.
"""

import os
import re
from pathlib import Path
from datetime import datetime

def standardize_guide_structure():
    """Padroniza a estrutura de todos os guias da wiki."""
    
    guides_path = Path("wiki/docs/otclient/guides")
    
    if not guides_path.exists():
        print("❌ Pasta de guias não encontrada!")
        return
    
    print("🔧 Padronizando estrutura dos guias...")
    
    # Lista de arquivos de guia
    guide_files = list(guides_path.glob("*.md"))
    
    processed_count = 0
    
    for guide_file in guide_files:
        if guide_file.name.endswith('_backup_'):
            continue  # Pular arquivos de backup
        
        print(f"📄 Processando: {guide_file.name}")
        
        try:
            # Ler conteúdo
            with open(guide_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Fazer backup
            backup_file = guide_file.parent / f"{guide_file.stem}_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            with open(backup_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Padronizar estrutura
            new_content = standardize_single_guide(content, guide_file.name)
            
            # Salvar arquivo padronizado
            with open(guide_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            processed_count += 1
            print(f"✅ {guide_file.name} padronizado")
            
        except Exception as e:
            print(f"❌ Erro ao processar {guide_file.name}: {e}")
    
    print(f"\n✅ Processamento concluído!")
    print(f"📊 Guias processados: {processed_count}")
    
    return processed_count

def standardize_single_guide(content, filename):
    """Padroniza a estrutura de um único guia."""
    
    lines = content.split('\n')
    new_lines = []
    
    # Padrões para identificar seções
    section_pattern = r'^#{1,6}\s+(.+)$'
    
    # Extrair título principal
    title = filename.replace('.md', '').replace('_', ' ').title()
    
    # Adicionar frontmatter padronizado se não existir
    if not lines[0].startswith('---'):
        new_lines.extend([
            '---',
            f'title: {title}',
            'tags: [otclient, guide, documentation, system]',
            'type: guide',
            'status: active',
            'priority: alta',
            f'created: {datetime.now().strftime("%Y-%m-%d")}',
            f'updated: {datetime.now().strftime("%Y-%m-%d")}',
            '---',
            ''
        ])
    
    # Processar linhas
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Pular frontmatter existente
        if line.startswith('---') and i == 0:
            while i < len(lines) and not (lines[i] == '---' and i > 0):
                i += 1
            i += 1
            continue
        
        # Adicionar título principal se não existir
        if i == 0 and not line.startswith('# '):
            new_lines.append(f'# {title}')
            new_lines.append('')
            new_lines.append('> [!info] **GUIA COMPLETO**')
            new_lines.append(f'> Este guia fornece documentação completa sobre o {title.lower()}.')
            new_lines.append('')
        
        # Processar seções
        section_match = re.match(section_pattern, line)
        if section_match:
            section_title = section_match.group(1)
            section_level = len(line) - len(line.lstrip('#'))
            
            # Adicionar separador visual para seções principais
            if section_level == 2:
                new_lines.append('')
                new_lines.append('---')
                new_lines.append('')
            
            # Melhorar formatação de seções
            if section_level == 2:
                # Seção principal - adicionar emoji e formatação
                emoji = get_section_emoji(section_title)
                new_lines.append(f'{line} {emoji}')
            elif section_level == 3:
                # Subseção - adicionar emoji
                emoji = get_subsection_emoji(section_title)
                new_lines.append(f'{line} {emoji}')
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
        
        i += 1
    
    # Adicionar índice detalhado se não existir
    if not has_detailed_index(new_lines):
        new_lines = add_detailed_index(new_lines)
    
    # Adicionar seção de navegação se não existir
    if not has_navigation_section(new_lines):
        new_lines = add_navigation_section(new_lines)
    
    return '\n'.join(new_lines)

def get_section_emoji(section_title):
    """Retorna emoji apropriado para seção."""
    emoji_map = {
        'visão geral': '🎯',
        'visao geral': '🎯',
        'overview': '🎯',
        'introdução': '📖',
        'introducao': '📖',
        'introduction': '📖',
        'sistema': '⚙️',
        'system': '⚙️',
        'configuração': '🔧',
        'configuracao': '🔧',
        'configuration': '🔧',
        'exemplo': '💡',
        'examples': '💡',
        'exemplos': '💡',
        'api': '📚',
        'reference': '📚',
        'referência': '📚',
        'referencia': '📚',
        'troubleshooting': '🔍',
        'solução': '🔍',
        'solucao': '🔍',
        'problemas': '🔍',
        'performance': '⚡',
        'otimização': '⚡',
        'otimizacao': '⚡',
        'debug': '🐛',
        'depuração': '🐛',
        'depuracao': '🐛'
    }
    
    section_lower = section_title.lower()
    for key, emoji in emoji_map.items():
        if key in section_lower:
            return emoji
    
    return '📋'

def get_subsection_emoji(subsection_title):
    """Retorna emoji apropriado para subseção."""
    emoji_map = {
        'conceito': '🧠',
        'concept': '🧠',
        'implementação': '💻',
        'implementacao': '💻',
        'implementation': '💻',
        'exemplo': '🎮',
        'example': '🎮',
        'referência': '📚',
        'referencia': '📚',
        'reference': '📚',
        'visão geral': '👁️',
        'visao geral': '👁️',
        'overview': '👁️',
        'detalhes': '🔍',
        'details': '🔍',
        'estrutura': '🏗️',
        'structure': '🏗️',
        'função': '⚙️',
        'funcao': '⚙️',
        'function': '⚙️'
    }
    
    subsection_lower = subsection_title.lower()
    for key, emoji in emoji_map.items():
        if key in subsection_lower:
            return emoji
    
    return '📝'

def has_detailed_index(lines):
    """Verifica se o guia já tem índice detalhado."""
    for line in lines:
        if 'Índice' in line or 'Index' in line:
            return True
    return False

def add_detailed_index(lines):
    """Adiciona índice detalhado ao guia."""
    # Encontrar posição após título principal
    insert_pos = 0
    for i, line in enumerate(lines):
        if line.startswith('# ') and i > 0:
            insert_pos = i + 1
            break
    
    # Extrair seções para o índice
    sections = []
    for line in lines:
        if line.startswith('## '):
            section_title = line.replace('## ', '').split(' ')[-1]  # Remove emoji
            sections.append(section_title)
    
    # Criar índice
    index_lines = [
        '',
        '## 📋 **ÍNDICE DETALHADO**',
        '',
        '### **🎯 Navegação Rápida**',
        ''
    ]
    
    for i, section in enumerate(sections, 1):
        anchor = section.lower().replace(' ', '-').replace('ç', 'c').replace('ã', 'a')
        index_lines.append(f'{i}. [{section}](#{anchor})')
    
    index_lines.extend([
        '',
        '### **📚 Seções Principais**',
        '',
        '| Seção | Descrição |',
        '|-------|-----------|'
    ])
    
    for section in sections:
        description = get_section_description(section)
        index_lines.append(f'| {section} | {description} |')
    
    index_lines.append('')
    
    # Inserir índice
    lines[insert_pos:insert_pos] = index_lines
    
    return lines

def get_section_description(section):
    """Retorna descrição para seção do índice."""
    descriptions = {
        'visão geral': 'Conceitos fundamentais e arquitetura',
        'sistema': 'Funcionalidades e componentes principais',
        'configuração': 'Configurações e parâmetros',
        'exemplos': 'Casos de uso e exemplos práticos',
        'api': 'Referência completa da API',
        'troubleshooting': 'Solução de problemas comuns',
        'performance': 'Otimizações e melhores práticas'
    }
    
    section_lower = section.lower()
    for key, desc in descriptions.items():
        if key in section_lower:
            return desc
    
    return 'Documentação e referência'

def has_navigation_section(lines):
    """Verifica se o guia já tem seção de navegação."""
    for line in lines:
        if 'Navegação' in line or 'Navigation' in line:
            return True
    return False

def add_navigation_section(lines):
    """Adiciona seção de navegação ao final do guia."""
    nav_lines = [
        '',
        '---',
        '',
        '## 🧭 **NAVEGAÇÃO**',
        '',
        '### **📖 Guias Relacionados**',
        '',
        '- [Guia de Início Rápido](../Getting_Started_Guide.md)',
        '- [Guia de Configuração](../Configuration_Guide.md)',
        '- [Guia de Debug](../Debug_System_Guide.md)',
        '',
        '### **🔗 Links Úteis**',
        '',
        '- [Documentação Principal](../../../README.md)',
        '- [Índice da Wiki](../../../Wiki_Index.md)',
        '- [Sistema de Busca](../../../Navigation_Index_Search.md)',
        '',
        '### **📞 Suporte**',
        '',
        'Para dúvidas ou problemas:',
        '- Consulte a seção [Troubleshooting](#troubleshooting)',
        '- Verifique os [Exemplos Práticos](#exemplos-práticos)',
        '- Consulte a [Referência da API](#api)',
        ''
    ]
    
    lines.extend(nav_lines)
    return lines

if __name__ == "__main__":
    standardize_guide_structure() 