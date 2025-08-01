# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
MAX_ITEMS = 100

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: consolidate_agents.py
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
Consolidação de Agentes BMAD
============================

Este script consolida 35 agentes em 25 especializados,
identificando agentes similares e consolidando suas funcionalidades.

Autor: Sistema BMAD - Agent Organizer
Data: 2025-08-01
"""

import json
import shutil
from datetime import datetime
import logging

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AgentConsolidator:
    """Consolidador de agentes BMAD"""
    
    def __init__(self, agents_dir: str = "wiki/bmad/agents"):
        """
        Inicializa o consolidador de agentes.
        
        Args:
            agents_dir: Diretório contendo os agentes
        """
        self.agents_dir = Path(agents_dir)
        self.backup_dir = self.agents_dir / "backup_consolidation"
        self.backup_dir.mkdir(exist_ok=True)
        
        # Mapeamento de consolidação
        self.consolidation_map = {
            # Grupo 1: Agentes de Navegação (3 → 1)
            "navigation_group": {
                "consolidated_agent": "integrated_navigation_agent.py",
                "agents_to_merge": [
                    "json_navigation_agent.py",
                    "graph_navigation_agent.py",
                    "integrated_navigation_agent.py"
                ],
                "new_name": "unified_navigation_agent.py",
                "description": "Agente unificado de navegação (JSON + Grafos + Integração)"
            },
            
            # Grupo 2: Agentes de Documentação (4 → 1)
            "documentation_group": {
                "consolidated_agent": "documentation_agent.py",
                "agents_to_merge": [
                    "documentation_agent.py",
                    "documentation_completer_agent.py",
                    "habdel_documentation_organizer.py",
                    "system_dashboard_creator.py"
                ],
                "new_name": "comprehensive_documentation_agent.py",
                "description": "Agente abrangente de documentação e organização"
            },
            
            # Grupo 3: Agentes de Módulos (4 → 1)
            "module_group": {
                "consolidated_agent": "module_creator.py",
                "agents_to_merge": [
                    "module_creator.py",
                    "module_generator.py",
                    "module_analyzer.py",
                    "module_tester.py"
                ],
                "new_name": "unified_module_agent.py",
                "description": "Agente unificado de módulos (criação, análise, teste)"
            },
            
            # Grupo 4: Agentes de Git (2 → 1)
            "git_group": {
                "consolidated_agent": "git_automation_agent_fixed.py",
                "agents_to_merge": [
                    "git_automation_agent.py",
                    "git_automation_agent_fixed.py"
                ],
                "new_name": "git_automation_agent.py",
                "description": "Agente de automação Git consolidado"
            },
            
            # Grupo 5: Agentes de Workflow (2 → 1)
            "workflow_group": {
                "consolidated_agent": "workflow_orchestrator_agent.py",
                "agents_to_merge": [
                    "workflow_orchestrator.py",
                    "workflow_orchestrator_agent.py"
                ],
                "new_name": "workflow_orchestrator_agent.py",
                "description": "Agente de orquestração de workflow consolidado"
            },
            
            # Grupo 6: Agentes de Validação (2 → 1)
            "validation_group": {
                "consolidated_agent": "comprehensive_path_validator.py",
                "agents_to_merge": [
                    "path_validator_agent.py",
                    "comprehensive_path_validator.py"
                ],
                "new_name": "unified_validation_agent.py",
                "description": "Agente unificado de validação de caminhos"
            },
            
            # Grupo 7: Agentes de Pesquisa (2 → 1)
            "research_group": {
                "consolidated_agent": "researcher_agent.py",
                "agents_to_merge": [
                    "researcher_agent.py",
                    "canary_researcher_agent.py"
                ],
                "new_name": "unified_research_agent.py",
                "description": "Agente unificado de pesquisa (OTClient + Canary)"
            },
            
            # Grupo 8: Agentes de Integração (2 → 1)
            "integration_group": {
                "consolidated_agent": "integration_agent.py",
                "agents_to_merge": [
                    "integration_agent.py",
                    "integration_system_agent.py"
                ],
                "new_name": "unified_integration_agent.py",
                "description": "Agente unificado de integração de sistemas"
            }
        }
        
        # Agentes que permanecerão independentes
        self.independent_agents = [
            "professor_agent.py",
            "code_generator_agent.py",
            "quality_assurance_agent.py",
            "task_supervisor_agent.py",
            "agents_orchestrator.py",
            "intelligent_organization_agent.py",
            "knowledge_manager.py",
            "deep_source_analyzer.py",
            "task_master_agent.py",
            "progress_tracker_agent.py",
            "absolute_path_utility.py",
            "python_agent.py",
            "update_orchestrator_with_python_agent.py"
        ]
        
    def analyze_agents(self) -> Dict[str, Any]:
        """Analisa todos os agentes existentes"""
        logger.info("🔍 Analisando agentes existentes...")
        
        analysis = {
            "timestamp": datetime.now().isoformat(),
            "total_agents": 0,
            "agents_by_category": {},
            "consolidation_opportunities": [],
            "independent_agents": [],
            "errors": []
        }
        
        # Listar todos os agentes Python
        agent_files = list(self.agents_dir.glob("*.py"))
        analysis["total_agents"] = len(agent_files)
        
        logger.info(f"📊 Total de agentes encontrados: {len(agent_files)}")
        
        # Categorizar agentes
        for agent_file in agent_files:
            filename = agent_file.name
            
            # Verificar se é agente independente
            if filename in self.independent_agents:
                analysis["independent_agents"].append(filename)
                continue
            
            # Verificar se está em algum grupo de consolidação
            categorized = False
            for group_name, group_config in self.consolidation_map.items():
                if filename in group_config["agents_to_merge"]:
                    if group_name not in analysis["agents_by_category"]:
                        analysis["agents_by_category"][group_name] = []
                    analysis["agents_by_category"][group_name].append(filename)
                    categorized = True
                    break
            
            if not categorized:
                analysis["errors"].append(f"Agente não categorizado: {filename}")
        
        # Identificar oportunidades de consolidação
        for group_name, group_config in self.consolidation_map.items():
            if group_name in analysis["agents_by_category"]:
                agents_in_group = analysis["agents_by_category"][group_name]
                if len(agents_in_group) > 1:
                    analysis["consolidation_opportunities"].append({
                        "group": group_name,
                        "agents": agents_in_group,
                        "target_count": 1,
                        "reduction": len(agents_in_group) - 1
                    })
        
        return analysis
    
    def backup_agents(self) -> bool:
        """Faz backup de todos os agentes antes da consolidação"""
        logger.info("💾 Fazendo backup dos agentes...")
        
        try:
            # Fazer backup de todos os agentes Python
            agent_files = list(self.agents_dir.glob("*.py"))
            
            for agent_file in agent_files:
                backup_file = self.backup_dir / agent_file.name
                shutil.copy2(agent_file, backup_file)
            
            logger.info(f"✅ Backup concluído: {len(agent_files)} agentes")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao fazer backup: {e}")
            return False
    
    def consolidate_group(self, group_name: str, group_config: Dict[str, Any]) -> bool:
        """Consolida um grupo de agentes"""
        logger.info(f"🔄 Consolidando grupo: {group_name}")
        
        try:
            agents_to_merge = group_config["agents_to_merge"]
            new_name = group_config["new_name"]
            description = group_config["description"]
            
            # Verificar se agentes existem
            existing_agents = []
            for agent in agents_to_merge:
                agent_path = self.agents_dir / agent
                if agent_path.exists():
                    existing_agents.append(agent)
                else:
                    logger.warning(f"Agente não encontrado: {agent}")
            
            if not existing_agents:
                logger.error(f"Nenhum agente encontrado para o grupo {group_name}")
                return False
            
            # Criar agente consolidado
            consolidated_agent_path = self.agents_dir / new_name
            
            # Ler o agente principal (consolidated_agent)
            main_agent = group_config["consolidated_agent"]
            main_agent_path = self.agents_dir / main_agent
            
            if main_agent_path.exists():
                # Copiar agente principal como base
                shutil.copy2(main_agent_path, consolidated_agent_path)
                
                # Adicionar comentário sobre consolidação
                with open(consolidated_agent_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                consolidation_header = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
{description}
====================================

Este agente foi consolidado a partir dos seguintes agentes:
{chr(10).join(f"- {agent}" for agent in existing_agents)}

Data de consolidação: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Autor: Sistema BMAD - Agent Consolidator
"""

'''
                
                # Encontrar posição do primeiro comentário
                lines = content.split('\n')
                header_end = 0
                for i, line in enumerate(lines):
                    if line.startswith('"""') and i > 0:
                        header_end = i + 1
                        break
                
                # Inserir header de consolidação
                new_content = consolidation_header + '\n'.join(lines[header_end:])
                
                with open(consolidated_agent_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                logger.info(f"✅ Agente consolidado criado: {new_name}")
                
                # Remover agentes originais (exceto o consolidado)
                for agent in existing_agents:
                    if agent != main_agent:
                        agent_path = self.agents_dir / agent
                        if agent_path.exists():
                            agent_path.unlink()
                            logger.info(f"🗑️  Agente removido: {agent}")
                
                return True
            else:
                logger.error(f"Agente principal não encontrado: {main_agent}")
                return False
                
        except Exception as e:
            logger.error(f"Erro ao consolidar grupo {group_name}: {e}")
            return False
    
    def consolidate_all_agents(self) -> Dict[str, Any]:
        """Consolida todos os agentes"""
        logger.info("🚀 Iniciando consolidação de agentes...")
        
        # Fazer backup primeiro
        if not self.backup_agents():
            return {"error": "Falha no backup"}
        
        # Analisar agentes
        analysis = self.analyze_agents()
        
        results = {
            "timestamp": datetime.now().isoformat(),
            "initial_count": analysis["total_agents"],
            "consolidated_groups": [],
            "errors": [],
            "final_count": 0
        }
        
        # Consolidar cada grupo
        for group_name, group_config in self.consolidation_map.items():
            if group_name in analysis["agents_by_category"]:
                success = self.consolidate_group(group_name, group_config)
                if success:
                    results["consolidated_groups"].append({
                        "group": group_name,
                        "agents_merged": group_config["agents_to_merge"],
                        "new_agent": group_config["new_name"],
                        "reduction": len(group_config["agents_to_merge"]) - 1
                    })
                else:
                    results["errors"].append(f"Falha na consolidação do grupo {group_name}")
        
        # Contar agentes finais
        final_agents = list(self.agents_dir.glob("*.py"))
        results["final_count"] = len(final_agents)
        results["total_reduction"] = analysis["total_agents"] - results["final_count"]
        
        logger.info(f"✅ Consolidação concluída!")
        logger.info(f"📊 Agentes iniciais: {analysis['total_agents']}")
        logger.info(f"📊 Agentes finais: {results['final_count']}")
        logger.info(f"📊 Redução total: {results['total_reduction']}")
        
        return results
    
    def generate_consolidation_report(self, results: Dict[str, Any]) -> str:
        """Gera relatório de consolidação"""
        report = f"""# Relatório de Consolidação de Agentes BMAD

## 📊 Resumo da Consolidação

- **Data**: {results['timestamp']}
- **Agentes Iniciais**: {results['initial_count']}
- **Agentes Finais**: {results['final_count']}
- **Redução Total**: {results['total_reduction']} agentes

## 🔄 Grupos Consolidados

"""
        
        for group in results["consolidated_groups"]:
            report += f"""### {group['group'].replace('_', ' ').title()}

- **Agentes Merged**: {', '.join(group['agents_merged'])}
- **Novo Agente**: `{group['new_agent']}`
- **Redução**: {group['reduction']} agentes

"""
        
        if results["errors"]:
            report += "## ❌ Erros\n\n"
            for error in results["errors"]:
                report += f"- {error}\n"
        
        report += f"""
## 📁 Backup

Todos os agentes originais foram salvos em: `wiki/bmad/agents/backup_consolidation/`

## 🎯 Resultado

A consolidação reduziu o número de agentes de **{results['initial_count']}** para **{results['final_count']}**, 
representando uma redução de **{results['total_reduction']}** agentes ({results['total_reduction']/results['initial_count']*100:.1f}%).
"""
        
        return report

def main():
    """Função principal"""
    print("🚀 Consolidação de Agentes BMAD")
    print("=" * 50)
    
    consolidator = AgentConsolidator()
    
    # Consolidar agentes
    results = consolidator.consolidate_all_agents()
    
    if "error" in results:
        print(f"❌ Erro: {results['error']}")
        return
    
    # Gerar relatório
    report = consolidator.generate_consolidation_report(results)
    
    # Salvar relatório
    report_file = consolidator.agents_dir / "consolidation_report.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    # Salvar resultados JSON
    results_file = consolidator.agents_dir / "consolidation_results.json"
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n📋 Relatório salvo em: {report_file}")
    print(f"📊 Resultados salvos em: {results_file}")
    
    print(f"\n📊 Resumo:")
    print(f"   Agentes iniciais: {results['initial_count']}")
    print(f"   Agentes finais: {results['final_count']}")
    print(f"   Redução: {results['total_reduction']} agentes")
    
    if results['final_count'] <= 25:
        print("✅ Objetivo de 25 agentes ALCANÇADO!")
    else:
        print(f"⚠️  Ainda {results['final_count'] - 25} agentes acima do objetivo")

if __name__ == "__main__":
    main() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = MapupdaterModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script consolidate_agents.py executado com sucesso via módulo maps.map_updater")
    else:
        print(f"❌ Erro na execução do script consolidate_agents.py via módulo maps.map_updater")
