#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para atualizar títulos internos dos documentos renomeados
Task 19.2 - Padronizar Idioma (Sub-tarefa 2)
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime

def carregar_mapeamento_renomeacao():
    """Carrega o mapeamento de arquivos renomeados"""
    
    try:
        with open('wiki/maps/teste_renomeacao_resultados.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        mapeamento = {}
        for resultado in dados['resultados']:
            if resultado['status'] == 'sucesso':
                # Extrair nome antigo do caminho
                nome_antigo = Path(resultado['arquivo']).name
                mapeamento[nome_antigo] = resultado['nome_novo']
        
        return mapeamento
    except FileNotFoundError:
        print("❌ Arquivo de mapeamento não encontrado!")
        return {}

def mapear_titulos_ingles_portugues():
    """Mapeia títulos em inglês para português"""
    
    mapeamento_titulos = {
        # Títulos básicos
        'README': 'LEIA-ME',
        'Readme': 'Leia-me',
        'readme': 'leia-me',
        
        # Guias e manuais
        'Guide': 'Guia',
        'guide': 'guia',
        'Manual': 'Manual',
        'manual': 'manual',
        'Tutorial': 'Tutorial',
        'tutorial': 'tutorial',
        
        # Documentação
        'Documentation': 'Documentação',
        'documentation': 'documentação',
        'Guidelines': 'Diretrizes',
        'guidelines': 'diretrizes',
        
        # Sistemas
        'System': 'Sistema',
        'system': 'sistema',
        'Systems': 'Sistemas',
        'systems': 'sistemas',
        
        # Configuração
        'Configuration': 'Configuração',
        'configuration': 'configuração',
        'Config': 'Config',
        'config': 'config',
        'Setup': 'Configuração',
        'setup': 'configuração',
        
        # Integração
        'Integration': 'Integração',
        'integration': 'integração',
        
        # Desempenho
        'Performance': 'Desempenho',
        'performance': 'desempenho',
        
        # Segurança
        'Security': 'Segurança',
        'security': 'segurança',
        
        # Automação
        'Automation': 'Automação',
        'automation': 'automação',
        
        # Estrutura
        'Structure': 'Estrutura',
        'structure': 'estrutura',
        'File Structure': 'Estrutura de Arquivos',
        'file structure': 'estrutura de arquivos',
        
        # Análise
        'Analysis': 'Análise',
        'analysis': 'análise',
        
        # Relatórios
        'Report': 'Relatório',
        'report': 'relatório',
        'Reports': 'Relatórios',
        'reports': 'relatórios',
        
        # Workflow
        'Workflow': 'Fluxo de Trabalho',
        'workflow': 'fluxo de trabalho',
        'Workflows': 'Fluxos de Trabalho',
        'workflows': 'fluxos de trabalho',
        
        # Módulos
        'Module': 'Módulo',
        'module': 'módulo',
        'Modules': 'Módulos',
        'modules': 'módulos',
        
        # Agentes
        'Agent': 'Agente',
        'agent': 'agente',
        'Agents': 'Agentes',
        'agents': 'agentes',
        
        # Especializado
        'Specialized': 'Especializado',
        'specialized': 'especializado',
        
        # Autônomo
        'Autonomous': 'Autônomo',
        'autonomous': 'autônomo',
        
        # Git
        'Git': 'Git',
        'git': 'git',
        
        # Python
        'Python': 'Python',
        'python': 'python',
        
        # BMAD
        'BMAD': 'BMAD',
        'bmad': 'bmad',
        
        # OTClient
        'OTClient': 'OTClient',
        'otclient': 'otclient',
        
        # Canary
        'Canary': 'Canary',
        'canary': 'canary'
    }
    
    return mapeamento_titulos

def atualizar_titulo_documento(conteudo, mapeamento_titulos):
    """Atualiza títulos em um documento"""
    
    conteudo_original = conteudo
    
    # Atualizar títulos principais (# Título)
    for ingles, portugues in mapeamento_titulos.items():
        # Padrão para títulos markdown
        padrao_titulo = rf'^#+\s*{re.escape(ingles)}\s*$'
        substituicao = rf'# {portugues}'
        conteudo = re.sub(padrao_titulo, substituicao, conteudo, flags=re.MULTILINE)
        
        # Padrão para títulos com outros caracteres
        padrao_titulo_geral = rf'^#+\s*([^#\n]*{re.escape(ingles)}[^#\n]*)\s*$'
        def substituir_titulo(match):
            titulo_completo = match.group(1)
            novo_titulo = titulo_completo.replace(ingles, portugues)
            return f'# {novo_titulo}'
        conteudo = re.sub(padrao_titulo_geral, substituir_titulo, conteudo, flags=re.MULTILINE)
    
    return conteudo

def atualizar_frontmatter(conteudo, mapeamento_titulos):
    """Atualiza frontmatter dos documentos"""
    
    # Padrão para frontmatter
    padrao_frontmatter = r'^---\s*\n(.*?)\n---\s*\n'
    
    def atualizar_frontmatter_match(match):
        frontmatter = match.group(1)
        
        # Atualizar título no frontmatter
        for ingles, portugues in mapeamento_titulos.items():
            # Padrão para title: no frontmatter
            padrao_title = rf'title:\s*["\']?([^"\'\n]*{re.escape(ingles)}[^"\'\n]*)["\']?'
            def substituir_title(title_match):
                titulo_completo = title_match.group(1)
                novo_titulo = titulo_completo.replace(ingles, portugues)
                return f'title: "{novo_titulo}"'
            frontmatter = re.sub(padrao_title, substituir_title, frontmatter)
        
        return f'---\n{frontmatter}\n---\n'
    
    conteudo = re.sub(padrao_frontmatter, atualizar_frontmatter_match, conteudo, flags=re.DOTALL)
    
    return conteudo

def processar_arquivo_renomeado(caminho_arquivo, mapeamento_titulos):
    """Processa um arquivo renomeado para atualizar títulos internos"""
    
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        
        conteudo_original = conteudo
        
        # Atualizar títulos
        conteudo = atualizar_titulo_documento(conteudo, mapeamento_titulos)
        
        # Atualizar frontmatter
        conteudo = atualizar_frontmatter(conteudo, mapeamento_titulos)
        
        # Salvar se houve mudanças
        if conteudo != conteudo_original:
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                f.write(conteudo)
            return True
        
        return False
        
    except Exception as e:
        print(f"⚠️ Erro ao processar {caminho_arquivo}: {e}")
        return False

def main():
    """Função principal"""
    
    print("🔤 ATUALIZANDO TÍTULOS INTERNOS - TASK 19.2")
    print("=" * 50)
    
    # Carregar mapeamento de renomeação
    mapeamento_renomeacao = carregar_mapeamento_renomeacao()
    if not mapeamento_renomeacao:
        print("❌ Nenhum arquivo renomeado encontrado!")
        return
    
    # Carregar mapeamento de títulos
    mapeamento_titulos = mapear_titulos_ingles_portugues()
    
    print(f"📊 Arquivos renomeados encontrados: {len(mapeamento_renomeacao)}")
    print(f"📝 Mapeamentos de títulos: {len(mapeamento_titulos)}")
    
    # Processar arquivos renomeados
    arquivos_processados = 0
    arquivos_atualizados = 0
    
    for nome_antigo, nome_novo in mapeamento_renomeacao.items():
        # Encontrar arquivo renomeado
        for arquivo_md in Path('wiki').rglob("*.md"):
            if arquivo_md.name == nome_novo:
                print(f"\n🔄 Processando: {arquivo_md.name}")
                
                if processar_arquivo_renomeado(arquivo_md, mapeamento_titulos):
                    print(f"   ✅ Títulos atualizados")
                    arquivos_atualizados += 1
                else:
                    print(f"   ℹ️ Nenhuma mudança necessária")
                
                arquivos_processados += 1
                break
    
    # Gerar relatório
    relatorio = f"""# 🔤 Relatório de Atualização de Títulos Internos - Task 19.2

**Data**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Sub-tarefa**: Atualizar títulos internos dos documentos

## 📊 Resultados

- **Arquivos processados**: {arquivos_processados}
- **Arquivos atualizados**: {arquivos_atualizados}
- **Taxa de atualização**: {(arquivos_atualizados/arquivos_processados*100):.1f}%

## 📋 Arquivos Processados

"""
    
    for nome_antigo, nome_novo in mapeamento_renomeacao.items():
        relatorio += f"- **{nome_antigo}** → **{nome_novo}**\n"
    
    relatorio += f"""

## ✅ Próximos Passos

1. **Verificar se os títulos estão corretos**
2. **Continuar com sub-tarefa 3**: Padronizar terminologia técnica
3. **Continuar com sub-tarefa 4**: Verificar consistência de idioma
4. **Continuar com sub-tarefa 5**: Atualizar aliases e tags

## 🔧 Mapeamentos Aplicados

"""
    
    for ingles, portugues in mapeamento_titulos.items():
        relatorio += f"- **{ingles}** → **{portugues}**\n"
    
    with open('wiki/log/atualizacao_titulos_relatorio.md', 'w', encoding='utf-8') as f:
        f.write(relatorio)
    
    print(f"\n📊 RESULTADOS:")
    print(f"📁 Arquivos processados: {arquivos_processados}")
    print(f"✅ Arquivos atualizados: {arquivos_atualizados}")
    print(f"📋 Relatório: wiki/log/atualizacao_titulos_relatorio.md")
    
    if arquivos_atualizados > 0:
        print(f"\n🎯 TÍTULOS ATUALIZADOS COM SUCESSO!")
        print(f"📝 Próxima sub-tarefa: Padronizar terminologia técnica")
    else:
        print(f"\nℹ️ Nenhuma atualização necessária nos títulos")

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
- **Nome**: atualizar_titulos_internos
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

