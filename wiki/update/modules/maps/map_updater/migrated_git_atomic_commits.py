from unicode_aliases import *
# Constantes
MAX_RETRIES = 8

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: git_atomic_commits.py
Módulo de Destino: maps.map_updater
Data de Migração: 2025-08-01 12:21:34

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import MapupdaterModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para fazer commits atômicos organizados por categoria
Seguindo as regras de automação Git do sistema BMAD
"""

import subprocess
import os
import sys

def run_command(command, capture_output=True):
    """Executa comando e retorna resultado"""
    try:
        result = subprocess.run(command, shell=True, capture_output=capture_output, text=True, encoding='utf-8')
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def get_untracked_files():
    """Obtém lista de arquivos não rastreados"""
    success, output, error = run_command("git status --porcelain")
    if not success:
        print(f"Erro ao obter status: {error}")
        return []
    
    untracked = []
    for line in output.strip().split('\n'):
        if line.startswith('??'):
            file_path = line[3:].strip()
            untracked.append(file_path)
    
    return untracked

def categorize_files(files):
    """Categoriza arquivos por tipo"""
    categories = {
        'core': [],
        'guides': [],
        'ui': [],
        'integration': [],
        'tasks': []
    }
    
    for file_path in files:
        if 'CORE-' in file_path:
            categories['core'].append(file_path)
        elif 'GUIDE-' in file_path:
            categories['guides'].append(file_path)
        elif 'UI_' in file_path:
            categories['ui'].append(file_path)
        elif 'Integration' in file_path:
            categories['integration'].append(file_path)
        elif 'task.md' in file_path:
            categories['tasks'].append(file_path)
        else:
            categories['core'].append(file_path)
    
    return categories

def make_commit(files, category, description):
    """Faz commit de uma categoria de arquivos"""
    if not files:
        return True
    
    print(f"\n🔄 Fazendo commit {category}: {len(files)} arquivos")
    
    # Adiciona arquivos
    for file_path in files:
        success, output, error = run_command(f'git add "{file_path}"')
        if not success:
            print(f"❌ Erro ao adicionar {file_path}: {error}")
            return False
    
    # Faz commit
    commit_message = f"docs: {description}"
    success, output, error = run_command(f'git commit -m "{commit_message}"')
    
    if success:
        print(f"✅ Commit {category} realizado com sucesso")
        print(f"   Arquivos: {', '.join([os.path.basename(f) for f in files])}")
        return True
    else:
        print(f"❌ Erro no commit {category}: {error}")
        return False

def main():
    """Função principal"""
    print("🚀 Iniciando commits atômicos organizados...")
    
    # Verifica se estamos no repositório correto
    success, output, error = run_command("git rev-parse --git-dir")
    if not success:
        print("❌ Não estamos em um repositório Git válido")
        return False
    
    # Obtém arquivos não rastreados
    untracked_files = get_untracked_files()
    if not untracked_files:
        print("✅ Nenhum arquivo não rastreado encontrado")
        return True
    
    print(f"📁 Encontrados {len(untracked_files)} arquivos não rastreados")
    
    # Categoriza arquivos
    categories = categorize_files(untracked_files)
    
    # Define descrições para cada categoria
    descriptions = {
        'core': 'adiciona documentação core do sistema OTClient',
        'guides': 'adiciona guias avançados de desenvolvimento e troubleshooting',
        'ui': 'adiciona documentação de sistemas de interface do usuário',
        'integration': 'adiciona documentação de integração e relatórios',
        'tasks': 'adiciona tarefas e planos de desenvolvimento'
    }
    
    # Faz commits por categoria
    total_commits = 0
    for category, files in categories.items():
        if files:
            if make_commit(files, category, descriptions[category]):
                total_commits += 1
    
    print(f"\n🎉 Processo concluído! {total_commits} commits realizados")
    
    # Mostra status final
    print("\n📊 Status final:")
    run_command("git status", capture_output=False)
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = MapupdaterModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script git_atomic_commits.py executado com sucesso via módulo maps.map_updater")
    else:
        print(f"❌ Erro na execução do script git_atomic_commits.py via módulo maps.map_updater")

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
- **Nome**: migrated_git_atomic_commits
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

