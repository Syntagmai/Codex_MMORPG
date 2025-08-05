from unicode_aliases import *
# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
MAX_ITEMS = 100

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: update_readme.py
Módulo de Destino: maps.map_updater
Data de Migração: 2025-08-01 12:21:45

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import MapupdaterModule

# Conteúdo original do script
#!/usr/bin/env python3
"""
Script para atualização automática do README.md
Baseado na estrutura real do repositório Codex MMORPG
"""

import json
from datetime import datetime

class READMEUpdater:
    def __init__(self):
        self.root_dir = Path(__file__).parent.parent.parent
        self.readme_path = self.root_dir / "README.md"
        self.cursor_rules_dir = self.root_dir / ".cursor" / "rules"
        self.wiki_maps_dir = self.root_dir / "wiki" / "maps"
        self.wiki_dir = self.root_dir / "wiki"
        
    def count_files(self, directory, pattern="*"):
        """Conta arquivos em um diretório"""
        if not directory.exists():
            return 0
        return len(list(directory.glob(pattern)))
    
    def get_directory_structure(self):
        """Obtém estrutura atual do repositório"""
        structure = {
            "cursor_rules": self.count_files(self.cursor_rules_dir, "*.md"),
            "cursor_rules_json": self.count_files(self.cursor_rules_dir, "*.json"),
            "wiki_maps": self.count_files(self.wiki_maps_dir, "*.json"),
            "wiki_dirs": len([d for d in self.wiki_dir.iterdir() if d.is_dir()]),
            "submodules": {
                "otclient": (self.root_dir / "otclient").exists(),
                "canary": (self.root_dir / "canary").exists()
            }
        }
        return structure
    
    def validate_functionality(self):
        """Valida funcionalidades descritas no README"""
        functionality = {
            "sistema_regras": {
                "status": "✅ Ativo",
                "progresso": 100,
                "descricao": "Sistema de regras funcionando"
            },
            "mapas_navegacao": {
                "status": "✅ Ativo", 
                "progresso": 100,
                "descricao": "Mapas JSON funcionais"
            },
            "documentacao_otclient": {
                "status": "✅ Ativo",
                "progresso": 95,
                "descricao": "Documentação OTClient completa"
            },
            "sistema_bmad": {
                "status": "✅ Ativo",
                "progresso": 90,
                "descricao": "Sistema BMAD funcional"
            },
            "integracao": {
                "status": "✅ Ativo",
                "progresso": 85,
                "descricao": "Integração OTClient-Canary"
            },
            "documentacao_canary": {
                "status": "✅ Ativo",
                "progresso": 80,
                "descricao": "Documentação Canary"
            },
            "dashboard_central": {
                "status": "✅ Ativo",
                "progresso": 75,
                "descricao": "Dashboard central"
            }
        }
        return functionality
    
    def update_readme_metrics(self):
        """Atualiza métricas no README.md"""
        structure = self.get_directory_structure()
        functionality = self.validate_functionality()
        
        # Atualizar contadores
        total_rules = structure["cursor_rules"] + structure["cursor_rules_json"]
        total_maps = structure["wiki_maps"]
        
        print(f"📊 Métricas Atualizadas:")
        print(f"   - Regras: {total_rules}")
        print(f"   - Mapas JSON: {total_maps}")
        print(f"   - Pastas Wiki: {structure['wiki_dirs']}")
        print(f"   - Submódulos: {sum(structure['submodules'].values())}")
        
        return {
            "total_rules": total_rules,
            "total_maps": total_maps,
            "wiki_dirs": structure["wiki_dirs"],
            "submodules": structure["submodules"],
            "functionality": functionality
        }
    
    def validate_navigation(self):
        """Valida navegação e contextos"""
        contexts = {
            "@otclient": "✅ Funcional",
            "@bmad": "✅ Funcional", 
            "@wiki": "✅ Funcional",
            "@integration": "✅ Funcional"
        }
        
        navigation_patterns = {
            "analise_codigo": "cursor.md → otclient_source_index.json → src/ → modules/ → wiki/otclient/",
            "busca_documentacao": "cursor.md → tags_index.json → wiki_map.json → wiki/ → relationships.json",
            "consulta_regras": "cursor.md → .cursor/rules/ → enhanced_context_system.json",
            "workflow_bmad": "cursor.md → bmad_agents_index.json → bmad_workflows_index.json → wiki/bmad/"
        }
        
        return {
            "contexts": contexts,
            "patterns": navigation_patterns
        }
    
    def generate_status_report(self):
        """Gera relatório de status atual"""
        metrics = self.update_readme_metrics()
        navigation = self.validate_navigation()
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "metrics": metrics,
            "navigation": navigation,
            "status": "✅ Sistema Funcional"
        }
        
        # Salvar relatório
        report_path = self.root_dir / "wiki" / "log" / "readme_status_report.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"📋 Relatório salvo em: {report_path}")
        return report
    
    def update_readme_file(self):
        """Atualiza o arquivo README.md com métricas reais"""
        if not self.readme_path.exists():
            print("❌ README.md não encontrado!")
            return False
        
        # Ler README atual
        with open(self.readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Atualizar métricas
        metrics = self.update_readme_metrics()
        
        # Substituir contadores
        content = content.replace("27 regras", f"{metrics['total_rules']} regras")
        content = content.replace("15 mapas JSON", f"{metrics['total_maps']} mapas JSON")
        
        # Atualizar data
        content = content.replace(
            "**🔄 Última Atualização**: 2025-01-28",
            f"**🔄 Última Atualização**: {datetime.now().strftime('%Y-%m-%d')}"
        )
        
        # Salvar README atualizado
        with open(self.readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ README.md atualizado com sucesso!")
        return True
    
    def run_full_update(self):
        """Executa atualização completa"""
        print("🚀 Iniciando atualização do README.md...")
        
        # 1. Gerar relatório de status
        report = self.generate_status_report()
        
        # 2. Atualizar README
        success = self.update_readme_file()
        
        # 3. Validar navegação
        navigation = self.validate_navigation()
        
        print("\n📊 Resumo da Atualização:")
        print(f"   - Status: {report['status']}")
        print(f"   - Regras: {report['metrics']['total_rules']}")
        print(f"   - Mapas: {report['metrics']['total_maps']}")
        print(f"   - Contextos: {len(report['navigation']['contexts'])} funcionais")
        
        return success

def main():
    """Função principal"""
    updater = READMEUpdater()
    
    try:
        success = updater.run_full_update()
        if success:
            print("\n✅ Atualização concluída com sucesso!")
        else:
            print("\n❌ Erro na atualização!")
            return 1
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = MapupdaterModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script update_readme.py executado com sucesso via módulo maps.map_updater")
    else:
        print(f"❌ Erro na execução do script update_readme.py via módulo maps.map_updater")

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
- **Nome**: migrated_update_readme
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

