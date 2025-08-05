#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para mapear arquivos com nomes em inglês que precisam ser renomeados para português
Task 19.2 - Padronizar Idioma
"""

import os
import json
import re
from pathlib import Path

def identificar_arquivos_ingles():
    """Identifica arquivos com nomes em inglês que precisam ser renomeados"""
    
    wiki_path = Path("wiki")
    arquivos_ingles = []
    
    # Padrões de nomes em inglês
    padroes_ingles = [
        r'^[A-Z][a-z]+[A-Z][a-zA-Z]*\.md$',  # CamelCase
        r'^[a-z_]+\.md$',  # snake_case
        r'^[A-Z_]+\.md$',  # UPPER_CASE
        r'^[a-z]+[A-Z][a-zA-Z]*\.md$',  # camelCase
    ]
    
    # Palavras em inglês comuns em nomes de arquivos
    palavras_ingles = [
        'readme', 'guide', 'manual', 'tutorial', 'documentation', 'analysis',
        'system', 'module', 'config', 'setup', 'install', 'getting', 'started',
        'best', 'practices', 'api', 'reference', 'cheat', 'sheet', 'workflow',
        'template', 'example', 'sample', 'test', 'validation', 'security',
        'performance', 'integration', 'migration', 'cleanup', 'organization',
        'structure', 'protocol', 'network', 'graphics', 'sound', 'effects',
        'creature', 'item', 'world', 'ui', 'widget', 'button', 'form', 'layout',
        'modal', 'tab', 'text', 'edit', 'style', 'animation', 'drag', 'drop',
        'event', 'advanced', 'basic', 'intermediate', 'expert', 'beginner',
        'professional', 'developer', 'user', 'admin', 'manager', 'agent',
        'workflow', 'automation', 'script', 'tool', 'utility', 'helper',
        'assistant', 'controller', 'handler', 'processor', 'generator',
        'validator', 'analyzer', 'monitor', 'logger', 'reporter', 'tracker'
    ]
    
    for arquivo in wiki_path.rglob("*.md"):
        nome_arquivo = arquivo.name.lower()
        
        # Verificar se contém palavras em inglês
        tem_ingles = False
        for palavra in palavras_ingles:
            if palavra in nome_arquivo:
                tem_ingles = True
                break
        
        # Verificar padrões de nomenclatura em inglês
        for padrao in padroes_ingles:
            if re.match(padrao, arquivo.name):
                tem_ingles = True
                break
        
        if tem_ingles:
            arquivos_ingles.append({
                'caminho': str(arquivo.relative_to(wiki_path)),
                'nome_atual': arquivo.name,
                'sugestao_nome': sugerir_nome_portugues(arquivo.name),
                'tipo': identificar_tipo_arquivo(arquivo.name)
            })
    
    return arquivos_ingles

def sugerir_nome_portugues(nome_ingles):
    """Sugere nome em português para arquivo em inglês"""
    
    mapeamento = {
        # Palavras básicas
        'readme': 'leia_me',
        'guide': 'guia',
        'manual': 'manual',
        'tutorial': 'tutorial',
        'documentation': 'documentacao',
        'analysis': 'analise',
        'system': 'sistema',
        'module': 'modulo',
        'config': 'configuracao',
        'setup': 'configuracao',
        'install': 'instalacao',
        'getting': 'inicio',
        'started': 'rapido',
        'best': 'melhores',
        'practices': 'praticas',
        'api': 'api',
        'reference': 'referencia',
        'cheat': 'resumo',
        'sheet': 'rapido',
        'workflow': 'fluxo_trabalho',
        'template': 'modelo',
        'example': 'exemplo',
        'sample': 'exemplo',
        'test': 'teste',
        'validation': 'validacao',
        'security': 'seguranca',
        'performance': 'desempenho',
        'integration': 'integracao',
        'migration': 'migracao',
        'cleanup': 'limpeza',
        'organization': 'organizacao',
        'structure': 'estrutura',
        'protocol': 'protocolo',
        'network': 'rede',
        'graphics': 'graficos',
        'sound': 'som',
        'effects': 'efeitos',
        'creature': 'criatura',
        'item': 'item',
        'world': 'mundo',
        'ui': 'interface',
        'widget': 'componente',
        'button': 'botao',
        'form': 'formulario',
        'layout': 'layout',
        'modal': 'modal',
        'tab': 'aba',
        'text': 'texto',
        'edit': 'edicao',
        'style': 'estilo',
        'animation': 'animacao',
        'drag': 'arrastar',
        'drop': 'soltar',
        'event': 'evento',
        'advanced': 'avancado',
        'basic': 'basico',
        'intermediate': 'intermediario',
        'expert': 'especialista',
        'beginner': 'iniciante',
        'professional': 'profissional',
        'developer': 'desenvolvedor',
        'user': 'usuario',
        'admin': 'administrador',
        'manager': 'gerenciador',
        'agent': 'agente',
        'automation': 'automacao',
        'script': 'script',
        'tool': 'ferramenta',
        'utility': 'utilitario',
        'helper': 'ajudante',
        'assistant': 'assistente',
        'controller': 'controlador',
        'handler': 'manipulador',
        'processor': 'processador',
        'generator': 'gerador',
        'validator': 'validador',
        'analyzer': 'analisador',
        'monitor': 'monitor',
        'logger': 'registrador',
        'reporter': 'relator',
        'tracker': 'rastreador'
    }
    
    nome_sugerido = nome_ingles.lower()
    
    # Substituir palavras em inglês por português
    for ingles, portugues in mapeamento.items():
        nome_sugerido = nome_sugerido.replace(ingles, portugues)
    
    # Converter CamelCase para snake_case
    nome_sugerido = re.sub(r'([a-z])([A-Z])', r'\1_\2', nome_sugerido)
    nome_sugerido = nome_sugerido.lower()
    
    # Remover caracteres especiais e substituir por underscore
    nome_sugerido = re.sub(r'[^a-z0-9_]', '_', nome_sugerido)
    nome_sugerido = re.sub(r'_+', '_', nome_sugerido)
    nome_sugerido = nome_sugerido.strip('_')
    
    return nome_sugerido + '.md'

def identificar_tipo_arquivo(nome):
    """Identifica o tipo do arquivo baseado no nome"""
    
    if 'readme' in nome.lower():
        return 'documentacao_principal'
    elif 'guide' in nome.lower() or 'manual' in nome.lower():
        return 'guia'
    elif 'analysis' in nome.lower():
        return 'analise'
    elif 'system' in nome.lower():
        return 'sistema'
    elif 'api' in nome.lower() or 'reference' in nome.lower():
        return 'referencia'
    elif 'workflow' in nome.lower():
        return 'fluxo_trabalho'
    elif 'template' in nome.lower():
        return 'modelo'
    elif 'example' in nome.lower() or 'sample' in nome.lower():
        return 'exemplo'
    elif 'test' in nome.lower():
        return 'teste'
    elif 'report' in nome.lower():
        return 'relatorio'
    else:
        return 'documentacao_geral'

def main():
    """Função principal"""
    
    print("🔍 Mapeando arquivos com nomes em inglês...")
    
    arquivos_ingles = identificar_arquivos_ingles()
    
    # Salvar resultado em JSON
    resultado = {
        'total_arquivos': len(arquivos_ingles),
        'arquivos_para_renomear': arquivos_ingles,
        'resumo_por_tipo': {}
    }
    
    # Contar por tipo
    for arquivo in arquivos_ingles:
        tipo = arquivo['tipo']
        if tipo not in resultado['resumo_por_tipo']:
            resultado['resumo_por_tipo'][tipo] = 0
        resultado['resumo_por_tipo'][tipo] += 1
    
    # Salvar arquivo JSON
    with open('wiki/maps/arquivos_ingles_mapeados.json', 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)
    
    # Gerar relatório
    with open('wiki/log/mapeamento_arquivos_ingles_relatorio.md', 'w', encoding='utf-8') as f:
        f.write("# 📋 Relatório de Mapeamento de Arquivos em Inglês\n\n")
        f.write(f"**Data**: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**Total de arquivos identificados**: {len(arquivos_ingles)}\n\n")
        
        f.write("## 📊 Resumo por Tipo\n\n")
        for tipo, quantidade in resultado['resumo_por_tipo'].items():
            f.write(f"- **{tipo}**: {quantidade} arquivos\n")
        
        f.write("\n## 📁 Arquivos para Renomear\n\n")
        for arquivo in arquivos_ingles:
            f.write(f"### {arquivo['nome_atual']}\n")
            f.write(f"- **Caminho**: `{arquivo['caminho']}`\n")
            f.write(f"- **Tipo**: {arquivo['tipo']}\n")
            f.write(f"- **Sugestão**: `{arquivo['sugestao_nome']}`\n\n")
    
    print(f"✅ Mapeamento concluído!")
    print(f"📊 Total de arquivos identificados: {len(arquivos_ingles)}")
    print(f"📁 Relatório salvo em: wiki/log/mapeamento_arquivos_ingles_relatorio.md")
    print(f"🗂️ Dados salvos em: wiki/maps/arquivos_ingles_mapeados.json")

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
- **Nome**: mapear_arquivos_ingles
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

