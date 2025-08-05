#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para renomear arquivos de inglês para português
Task 19.2 - Padronizar Idioma
"""

import os
import json
import shutil
import re
from pathlib import Path
from datetime import datetime

def carregar_mapeamento():
    """Carrega o mapeamento de arquivos gerado anteriormente"""
    
    try:
        with open('wiki/maps/arquivos_ingles_mapeados.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Arquivo de mapeamento não encontrado!")
        print("Execute primeiro: python wiki/update/mapear_arquivos_ingles.py")
        return None

def melhorar_nome_sugerido(nome_atual, sugestao_atual):
    """Melhora a sugestão de nome baseada no contexto"""
    
    # Mapeamento específico para nomes comuns
    mapeamento_especifico = {
        'README.md': 'leia_me.md',
        'readme_guidelines.md': 'diretrizes_leia_me.md',
        'documentation_guidelines.md': 'diretrizes_documentacao.md',
        'config_guidelines.md': 'diretrizes_configuracao.md',
        'file_structure_guidelines.md': 'diretrizes_estrutura_arquivos.md',
        'integration_guidelines.md': 'diretrizes_integracao.md',
        'performance_guidelines.md': 'diretrizes_desempenho.md',
        'python_guidelines.md': 'diretrizes_python.md',
        'security_guidelines.md': 'diretrizes_seguranca.md',
        'BMAD_System_Guide.md': 'guia_sistema_bmad.md',
        'autonomous_system.md': 'sistema_autonomo.md',
        'git_automation.md': 'automacao_git.md',
        'otclient_module_workflow.md': 'fluxo_trabalho_modulo_otclient.md',
        'README_MODULE_WORKFLOW.md': 'leia_me_fluxo_trabalho_modulos.md',
        'specialized_agents_plan.md': 'plano_agentes_especializados.md',
        'agents_roadmap.md': 'roteiro_agentes.md',
        'atomic_git_sync_system.md': 'sistema_sincronizacao_git_atomica.md',
        'continuous_development_plan.md': 'plano_desenvolvimento_continuo.md',
        'task_master.md': 'mestre_tarefas.md',
        'integrated_task_manager.md': 'gerenciador_tarefas_integrado.md',
        'task_master_archived.md': 'mestre_tarefas_arquivado.md'
    }
    
    # Verificar se há mapeamento específico
    if nome_atual in mapeamento_especifico:
        return mapeamento_especifico[nome_atual]
    
    # Melhorar sugestão genérica
    nome_melhorado = sugestao_atual
    
    # Remover sufixos desnecessários
    nome_melhorado = re.sub(r'_md\.md$', '.md', nome_melhorado)
    nome_melhorado = re.sub(r'_md$', '.md', nome_melhorado)
    
    # Corrigir traduções específicas
    nome_melhorado = nome_melhorado.replace('ginterfacea', 'guia')
    nome_melhorado = nome_melhorado.replace('sistema_md', 'sistema')
    nome_melhorado = nome_melhorado.replace('fluxo_trabalho_md', 'fluxo_trabalho')
    
    return nome_melhorado

def renomear_arquivo(caminho_antigo, nome_novo, backup=True):
    """Renomeia um arquivo com backup opcional"""
    
    caminho_completo = Path('wiki') / caminho_antigo
    diretorio = caminho_completo.parent
    nome_antigo = caminho_completo.name
    
    # Verificar se arquivo existe
    if not caminho_completo.exists():
        print(f"⚠️ Arquivo não encontrado: {caminho_completo}")
        return False
    
    # Criar backup se solicitado
    if backup:
        backup_path = diretorio / f"{nome_antigo}.backup"
        if not backup_path.exists():
            shutil.copy2(caminho_completo, backup_path)
    
    # Renomear arquivo
    novo_caminho = diretorio / nome_novo
    
    # Verificar se já existe arquivo com o novo nome
    if novo_caminho.exists():
        print(f"⚠️ Arquivo já existe: {novo_caminho}")
        return False
    
    try:
        caminho_completo.rename(novo_caminho)
        return True
    except Exception as e:
        print(f"❌ Erro ao renomear {caminho_completo}: {e}")
        return False

def processar_lote(arquivos, tamanho_lote=50):
    """Processa arquivos em lotes para evitar sobrecarga"""
    
    total_arquivos = len(arquivos)
    sucessos = 0
    falhas = 0
    
    print(f"🔄 Processando {total_arquivos} arquivos em lotes de {tamanho_lote}...")
    
    for i in range(0, total_arquivos, tamanho_lote):
        lote = arquivos[i:i+tamanho_lote]
        lote_numero = (i // tamanho_lote) + 1
        total_lotes = (total_arquivos + tamanho_lote - 1) // tamanho_lote
        
        print(f"\n📦 Processando lote {lote_numero}/{total_lotes} ({len(lote)} arquivos)...")
        
        for arquivo in lote:
            nome_melhorado = melhorar_nome_sugerido(arquivo['nome_atual'], arquivo['sugestao_nome'])
            
            print(f"  🔄 {arquivo['nome_atual']} → {nome_melhorado}")
            
            if renomear_arquivo(arquivo['caminho'], nome_melhorado):
                sucessos += 1
            else:
                falhas += 1
        
        # Pausa entre lotes para evitar sobrecarga
        if i + tamanho_lote < total_arquivos:
            print("⏳ Pausa de 2 segundos entre lotes...")
            import time
            time.sleep(2)
    
    return sucessos, falhas

def atualizar_referencias():
    """Atualiza referências nos arquivos após renomeação"""
    
    print("\n🔗 Atualizando referências nos arquivos...")
    
    # Carregar mapeamento de renomeação
    mapeamento = {}
    with open('wiki/maps/arquivos_ingles_mapeados.json', 'r', encoding='utf-8') as f:
        dados = json.load(f)
        
    for arquivo in dados['arquivos_para_renomear']:
        nome_melhorado = melhorar_nome_sugerido(arquivo['nome_atual'], arquivo['sugestao_nome'])
        mapeamento[arquivo['nome_atual']] = nome_melhorado
    
    # Atualizar referências em arquivos markdown
    wiki_path = Path('wiki')
    arquivos_atualizados = 0
    
    for arquivo_md in wiki_path.rglob("*.md"):
        try:
            with open(arquivo_md, 'r', encoding='utf-8') as f:
                conteudo = f.read()
            
            conteudo_original = conteudo
            
            # Substituir referências
            for nome_antigo, nome_novo in mapeamento.items():
                # Substituir links markdown
                conteudo = re.sub(
                    rf'\[([^\]]*)\]\({re.escape(nome_antigo)}\)',
                    rf'[\1]({nome_novo})',
                    conteudo
                )
                
                # Substituir referências diretas
                conteudo = conteudo.replace(nome_antigo, nome_novo)
            
            # Salvar se houve mudanças
            if conteudo != conteudo_original:
                with open(arquivo_md, 'w', encoding='utf-8') as f:
                    f.write(conteudo)
                arquivos_atualizados += 1
                
        except Exception as e:
            print(f"⚠️ Erro ao atualizar {arquivo_md}: {e}")
    
    print(f"✅ {arquivos_atualizados} arquivos atualizados com novas referências")

def gerar_relatorio_final(sucessos, falhas, tempo_inicio):
    """Gera relatório final da operação"""
    
    tempo_fim = datetime.now()
    duracao = tempo_fim - tempo_inicio
    
    relatorio = f"""# 📋 Relatório de Renomeação de Arquivos - Task 19.2

**Data**: {tempo_fim.strftime('%Y-%m-%d %H:%M:%S')}
**Duração**: {duracao}

## 📊 Resultados

- **Total processado**: {sucessos + falhas} arquivos
- **Sucessos**: {sucessos} arquivos
- **Falhas**: {falhas} arquivos
- **Taxa de sucesso**: {(sucessos/(sucessos+falhas)*100):.1f}%

## ✅ Próximos Passos

1. **Verificar backups**: Todos os arquivos originais foram salvos com extensão .backup
2. **Testar navegação**: Verificar se os links funcionam corretamente
3. **Continuar Task 19.3**: Melhorar estrutura e organização dos guias

## 🔧 Comandos Úteis

```bash
# Verificar arquivos renomeados
find wiki -name "*.backup" | wc -l

# Restaurar backup se necessário
# mv arquivo.md.backup arquivo.md

# Continuar para próxima task
# Task 19.3: Melhorar Estrutura e Organização dos Guias
```
"""
    
    with open('wiki/log/renomeacao_arquivos_relatorio_final.md', 'w', encoding='utf-8') as f:
        f.write(relatorio)
    
    print(f"\n📋 Relatório final salvo em: wiki/log/renomeacao_arquivos_relatorio_final.md")

def main():
    """Função principal"""
    
    print("🎯 TASK 19.2: PADRONIZAR IDIOMA - TÍTULOS E CONTEÚDO")
    print("=" * 60)
    
    tempo_inicio = datetime.now()
    
    # Carregar mapeamento
    dados = carregar_mapeamento()
    if not dados:
        return
    
    print(f"📊 Total de arquivos identificados: {dados['total_arquivos']}")
    
    # Perguntar confirmação
    resposta = input("\n❓ Deseja continuar com a renomeação? (s/N): ").lower()
    if resposta != 's':
        print("❌ Operação cancelada pelo usuário")
        return
    
    # Processar renomeação
    sucessos, falhas = processar_lote(dados['arquivos_para_renomear'])
    
    # Atualizar referências
    atualizar_referencias()
    
    # Gerar relatório final
    gerar_relatorio_final(sucessos, falhas, tempo_inicio)
    
    print(f"\n✅ Task 19.2 concluída!")
    print(f"📊 Resultados: {sucessos} sucessos, {falhas} falhas")
    print(f"🎯 Próxima task: 19.3 - Melhorar Estrutura e Organização dos Guias")

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
- **Nome**: renomear_arquivos_ingles
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

