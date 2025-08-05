#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de teste para renomear apenas arquivos importantes primeiro
Task 19.2 - Padronizar Idioma (Teste)
"""

import os
import json
import shutil
import re
from pathlib import Path
from datetime import datetime

def renomear_arquivos_importantes():
    """Renomeia apenas os arquivos mais importantes primeiro"""
    
    # Lista de arquivos importantes para renomear primeiro
    arquivos_importantes = [
        {
            'caminho': 'README.md',
            'nome_atual': 'README.md',
            'nome_novo': 'leia_me.md',
            'descricao': 'Ponto de entrada principal da wiki'
        },
        {
            'caminho': 'bmad/BMAD_System_Guide.md',
            'nome_atual': 'BMAD_System_Guide.md',
            'nome_novo': 'guia_sistema_bmad.md',
            'descricao': 'Guia principal do sistema BMAD'
        },
        {
            'caminho': 'bmad/autonomous_system.md',
            'nome_atual': 'autonomous_system.md',
            'nome_novo': 'sistema_autonomo.md',
            'descricao': 'Sistema autônomo BMAD'
        },
        {
            'caminho': 'bmad/git_automation.md',
            'nome_atual': 'git_automation.md',
            'nome_novo': 'automacao_git.md',
            'descricao': 'Automação Git'
        },
        {
            'caminho': 'docs/readme_guidelines.md',
            'nome_atual': 'readme_guidelines.md',
            'nome_novo': 'diretrizes_leia_me.md',
            'descricao': 'Diretrizes para arquivos README'
        },
        {
            'caminho': 'docs/documentation_guidelines.md',
            'nome_atual': 'documentation_guidelines.md',
            'nome_novo': 'diretrizes_documentacao.md',
            'descricao': 'Diretrizes de documentação'
        },
        {
            'caminho': 'docs/config_guidelines.md',
            'nome_atual': 'config_guidelines.md',
            'nome_novo': 'diretrizes_configuracao.md',
            'descricao': 'Diretrizes de configuração'
        },
        {
            'caminho': 'docs/file_structure_guidelines.md',
            'nome_atual': 'file_structure_guidelines.md',
            'nome_novo': 'diretrizes_estrutura_arquivos.md',
            'descricao': 'Diretrizes de estrutura de arquivos'
        },
        {
            'caminho': 'docs/integration_guidelines.md',
            'nome_atual': 'integration_guidelines.md',
            'nome_novo': 'diretrizes_integracao.md',
            'descricao': 'Diretrizes de integração'
        },
        {
            'caminho': 'docs/performance_guidelines.md',
            'nome_atual': 'performance_guidelines.md',
            'nome_novo': 'diretrizes_desempenho.md',
            'descricao': 'Diretrizes de desempenho'
        },
        {
            'caminho': 'docs/python_guidelines.md',
            'nome_atual': 'python_guidelines.md',
            'nome_novo': 'diretrizes_python.md',
            'descricao': 'Diretrizes Python'
        },
        {
            'caminho': 'docs/security_guidelines.md',
            'nome_atual': 'security_guidelines.md',
            'nome_novo': 'diretrizes_seguranca.md',
            'descricao': 'Diretrizes de segurança'
        }
    ]
    
    sucessos = 0
    falhas = 0
    resultados = []
    
    print("🧪 TESTE DE RENOMEAÇÃO - ARQUIVOS IMPORTANTES")
    print("=" * 50)
    
    for arquivo in arquivos_importantes:
        caminho_completo = Path('wiki') / arquivo['caminho']
        diretorio = caminho_completo.parent
        nome_antigo = caminho_completo.name
        nome_novo = arquivo['nome_novo']
        
        print(f"\n🔄 Processando: {arquivo['descricao']}")
        print(f"   📁 {nome_antigo} → {nome_novo}")
        
        # Verificar se arquivo existe
        if not caminho_completo.exists():
            print(f"   ❌ Arquivo não encontrado: {caminho_completo}")
            falhas += 1
            resultados.append({
                'arquivo': arquivo['caminho'],
                'status': 'nao_encontrado',
                'erro': 'Arquivo não existe'
            })
            continue
        
        # Criar backup
        backup_path = diretorio / f"{nome_antigo}.backup"
        if not backup_path.exists():
            shutil.copy2(caminho_completo, backup_path)
            print(f"   💾 Backup criado: {backup_path.name}")
        
        # Renomear arquivo
        novo_caminho = diretorio / nome_novo
        
        # Verificar se já existe arquivo com o novo nome
        if novo_caminho.exists():
            print(f"   ⚠️ Arquivo já existe: {novo_caminho}")
            falhas += 1
            resultados.append({
                'arquivo': arquivo['caminho'],
                'status': 'ja_existe',
                'erro': f'Arquivo {nome_novo} já existe'
            })
            continue
        
        try:
            caminho_completo.rename(novo_caminho)
            print(f"   ✅ Renomeado com sucesso!")
            sucessos += 1
            resultados.append({
                'arquivo': arquivo['caminho'],
                'status': 'sucesso',
                'nome_novo': nome_novo
            })
        except Exception as e:
            print(f"   ❌ Erro ao renomear: {e}")
            falhas += 1
            resultados.append({
                'arquivo': arquivo['caminho'],
                'status': 'erro',
                'erro': str(e)
            })
    
    # Gerar relatório
    relatorio = f"""# 🧪 Relatório de Teste de Renomeação - Task 19.2

**Data**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Tipo**: Teste com arquivos importantes

## 📊 Resultados

- **Total processado**: {len(arquivos_importantes)} arquivos
- **Sucessos**: {sucessos} arquivos
- **Falhas**: {falhas} arquivos
- **Taxa de sucesso**: {(sucessos/len(arquivos_importantes)*100):.1f}%

## 📋 Detalhes por Arquivo

"""
    
    for resultado in resultados:
        relatorio += f"### {resultado['arquivo']}\n"
        relatorio += f"- **Status**: {resultado['status']}\n"
        if resultado['status'] == 'sucesso':
            relatorio += f"- **Novo nome**: {resultado['nome_novo']}\n"
        elif 'erro' in resultado:
            relatorio += f"- **Erro**: {resultado['erro']}\n"
        relatorio += "\n"
    
    relatorio += """## ✅ Próximos Passos

1. **Verificar se os arquivos renomeados estão funcionando**
2. **Testar navegação entre os arquivos**
3. **Se tudo estiver OK, prosseguir com o lote completo**
4. **Se houver problemas, restaurar backups e ajustar script**

## 🔧 Comandos Úteis

```bash
# Verificar arquivos renomeados
ls -la wiki/leia_me.md
ls -la wiki/bmad/guia_sistema_bmad.md

# Restaurar backup se necessário
# mv wiki/leia_me.md.backup wiki/README.md
```
"""
    
    with open('wiki/log/teste_renomeacao_relatorio.md', 'w', encoding='utf-8') as f:
        f.write(relatorio)
    
    # Salvar resultados em JSON
    dados_json = {
        'data_teste': datetime.now().isoformat(),
        'total_arquivos': len(arquivos_importantes),
        'sucessos': sucessos,
        'falhas': falhas,
        'resultados': resultados
    }
    
    with open('wiki/maps/teste_renomeacao_resultados.json', 'w', encoding='utf-8') as f:
        json.dump(dados_json, f, indent=2, ensure_ascii=False)
    
    print(f"\n📊 RESULTADOS DO TESTE:")
    print(f"✅ Sucessos: {sucessos}")
    print(f"❌ Falhas: {falhas}")
    print(f"📋 Relatório: wiki/log/teste_renomeacao_relatorio.md")
    print(f"🗂️ Dados: wiki/maps/teste_renomeacao_resultados.json")
    
    if sucessos > 0:
        print(f"\n🎯 TESTE BEM-SUCEDIDO! Pode prosseguir com o lote completo.")
    else:
        print(f"\n⚠️ TESTE FALHOU! Verificar problemas antes de continuar.")

if __name__ == "__main__":
    renomear_arquivos_importantes() 