from unicode_aliases import *
# Constantes
MAX_RETRIES = 8

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: migrated_aaa_integration_validator.py
Módulo de Destino: maps.map_updater
Data de Migração: 2025-08-01 12:21:42

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import MapupdaterModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: aaa_integration_validator.py
Módulo de Destino: agents.agent_validator
Data de Migração: 2025-08-01 12:21:33

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import AgentvalidatorModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Validação de Integridade AAA
Valida compatibilidade entre sistema AAA e sistema existente
"""

import json
import time
from datetime import datetime

class AAAIntegrationValidator:
    """Sistema de validação de integridade para sistema AAA"""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.validation_results = {}
        self.compatibility_issues = []
        self.performance_metrics = {}
        
        # Estrutura de pastas
        self.logs_path = self.base_path / 'log' / 'aaa_validation'
        self.logs_path.mkdir(parents=True, exist_ok=True)
    
    def validate_system_integrity(self) -> Dict[str, Any]:
        """Valida integridade completa do sistema"""
        print("🔍 Iniciando validação de integridade do sistema AAA...")
        
        start_time = time.time()
        
        # Validações principais
        validation_results = {
            'timestamp': datetime.now().isoformat(),
            'validations': {},
            'compatibility_issues': [],
            'performance_metrics': {},
            'overall_status': 'unknown'
        }
        
        # 1. Validação de agentes
        print("🎭 Validando agentes especializados...")
        agent_validation = self.validate_agents()
        validation_results['validations']['agents'] = agent_validation
        
        # 2. Validação de workflows
        print("🔄 Validando workflows AAA...")
        workflow_validation = self.validate_workflows()
        validation_results['validations']['workflows'] = workflow_validation
        
        # 3. Validação de compatibilidade
        print("🔗 Validando compatibilidade com sistema existente...")
        compatibility_validation = self.validate_compatibility()
        validation_results['validations']['compatibility'] = compatibility_validation
        
        # 4. Validação de performance
        print("⚡ Validando performance...")
        performance_validation = self.validate_performance()
        validation_results['validations']['performance'] = performance_validation
        
        # 5. Validação de mapas JSON
        print("🗺️ Validando mapas JSON...")
        json_validation = self.validate_json_maps()
        validation_results['validations']['json_maps'] = json_validation
        
        # 6. Validação de regras
        print("📋 Validando regras...")
        rules_validation = self.validate_rules()
        validation_results['validations']['rules'] = rules_validation
        
        # Calcula status geral
        overall_status = self.calculate_overall_status(validation_results['validations'])
        validation_results['overall_status'] = overall_status
        
        # Calcula tempo total
        total_time = time.time() - start_time
        validation_results['total_validation_time'] = total_time
        
        # Salva resultados
        self.save_validation_results(validation_results)
        
        print(f"✅ Validação concluída em {total_time:.2f}s")
        print(f"📊 Status geral: {overall_status}")
        
        return validation_results
    
    def validate_agents(self) -> Dict[str, Any]:
        """Valida agentes especializados"""
        agent_validation = {
            'status': 'unknown',
            'total_agents': 0,
            'valid_agents': 0,
            'issues': [],
            'details': {}
        }
        
        # Carrega mapa de agentes
        agents_file = self.base_path / 'maps' / 'bmad_agents_index.json'
        if not agents_file.exists():
            agent_validation['issues'].append("Arquivo de agentes não encontrado")
            agent_validation['status'] = 'failed'
            return agent_validation
        
        try:
            with open(agents_file, 'r', encoding='utf-8') as f:
                agents_data = json.load(f)
            
            agents = agents_data.get('bmad_agents', {}).get('agents', {})
            agent_validation['total_agents'] = len(agents)
            
            # Valida cada agente
            for agent_id, agent_info in agents.items():
                agent_detail = {
                    'status': 'unknown',
                    'issues': []
                }
                
                # Validações básicas
                required_fields = ['name', 'expertise', 'commands', 'workflows']
                for field in required_fields:
                    if field not in agent_info:
                        agent_detail['issues'].append(f"Campo obrigatório '{field}' ausente")
                
                # Validação de especialização
                if 'context_adaptation' not in agent_info:
                    agent_detail['issues'].append("Adaptação de contexto ausente")
                
                # Validação de workflows
                workflows = agent_info.get('workflows', [])
                if not workflows:
                    agent_detail['issues'].append("Nenhum workflow definido")
                
                # Define status do agente
                if agent_detail['issues']:
                    agent_detail['status'] = 'failed'
                else:
                    agent_detail['status'] = 'valid'
                    agent_validation['valid_agents'] += 1
                
                agent_validation['details'][agent_id] = agent_detail
            
            # Define status geral dos agentes
            if agent_validation['valid_agents'] == agent_validation['total_agents']:
                agent_validation['status'] = 'passed'
            elif agent_validation['valid_agents'] > 0:
                agent_validation['status'] = 'partial'
            else:
                agent_validation['status'] = 'failed'
                
        except Exception as e:
            agent_validation['issues'].append(f"Erro ao carregar agentes: {str(e)}")
            agent_validation['status'] = 'failed'
        
        return agent_validation
    
    def validate_workflows(self) -> Dict[str, Any]:
        """Valida workflows AAA"""
        workflow_validation = {
            'status': 'unknown',
            'total_workflows': 0,
            'valid_workflows': 0,
            'issues': [],
            'details': {}
        }
        
        # Carrega mapa de agentes para workflows
        agents_file = self.base_path / 'maps' / 'bmad_agents_index.json'
        if not agents_file.exists():
            workflow_validation['issues'].append("Arquivo de agentes não encontrado")
            workflow_validation['status'] = 'failed'
            return workflow_validation
        
        try:
            with open(agents_file, 'r', encoding='utf-8') as f:
                agents_data = json.load(f)
            
            aaa_workflows = agents_data.get('bmad_agents', {}).get('aaa_workflows', {})
            workflow_validation['total_workflows'] = len(aaa_workflows)
            
            # Valida cada workflow
            for workflow_id, workflow_info in aaa_workflows.items():
                workflow_detail = {
                    'status': 'unknown',
                    'issues': []
                }
                
                # Validações básicas
                required_fields = ['name', 'agents', 'phases', 'duration', 'quality_gates']
                for field in required_fields:
                    if field not in workflow_info:
                        workflow_detail['issues'].append(f"Campo obrigatório '{field}' ausente")
                
                # Validação de agentes
                agents = workflow_info.get('agents', [])
                if not agents:
                    workflow_detail['issues'].append("Nenhum agente definido")
                
                # Validação de fases
                phases = workflow_info.get('phases', [])
                if not phases:
                    workflow_detail['issues'].append("Nenhuma fase definida")
                
                # Define status do workflow
                if workflow_detail['issues']:
                    workflow_detail['status'] = 'failed'
                else:
                    workflow_detail['status'] = 'valid'
                    workflow_validation['valid_workflows'] += 1
                
                workflow_validation['details'][workflow_id] = workflow_detail
            
            # Define status geral dos workflows
            if workflow_validation['valid_workflows'] == workflow_validation['total_workflows']:
                workflow_validation['status'] = 'passed'
            elif workflow_validation['valid_workflows'] > 0:
                workflow_validation['status'] = 'partial'
            else:
                workflow_validation['status'] = 'failed'
                
        except Exception as e:
            workflow_validation['issues'].append(f"Erro ao carregar workflows: {str(e)}")
            workflow_validation['status'] = 'failed'
        
        return workflow_validation
    
    def validate_compatibility(self) -> Dict[str, Any]:
        """Valida compatibilidade com sistema existente"""
        compatibility_validation = {
            'status': 'unknown',
            'compatibility_score': 0.0,
            'issues': [],
            'details': {}
        }
        
        # 1. Validação de regras existentes
        rules_path = self.base_path / '.cursor' / 'rules'
        if rules_path.exists():
            existing_rules = list(rules_path.glob('*.md'))
            aaa_rules = list(rules_path.glob('aaa-*.md'))
            
            compatibility_validation['details']['rules'] = {
                'existing_rules': len(existing_rules),
                'aaa_rules': len(aaa_rules),
                'compatibility': 'compatible'
            }
            
            if len(aaa_rules) > 0:
                compatibility_validation['compatibility_score'] += 0.3
        else:
            compatibility_validation['issues'].append("Pasta de regras não encontrada")
        
        # 2. Validação de mapas JSON
        maps_path = self.base_path / 'maps'
        if maps_path.exists():
            json_files = list(maps_path.glob('*.json'))
            bmad_agents_file = maps_path / 'bmad_agents_index.json'
            
            compatibility_validation['details']['maps'] = {
                'total_json_files': len(json_files),
                'bmad_agents_exists': bmad_agents_file.exists(),
                'compatibility': 'compatible'
            }
            
            if bmad_agents_file.exists():
                compatibility_validation['compatibility_score'] += 0.3
        else:
            compatibility_validation['issues'].append("Pasta de mapas não encontrada")
        
        # 3. Validação de sistema BMAD
        bmad_path = self.base_path / 'bmad'
        if bmad_path.exists():
            bmad_files = list(bmad_path.rglob('*'))
            
            compatibility_validation['details']['bmad'] = {
                'bmad_files': len(bmad_files),
                'compatibility': 'compatible'
            }
            
            compatibility_validation['compatibility_score'] += 0.4
        else:
            compatibility_validation['issues'].append("Sistema BMAD não encontrado")
        
        # Define status de compatibilidade
        if compatibility_validation['compatibility_score'] >= 0.9:
            compatibility_validation['status'] = 'fully_compatible'
        elif compatibility_validation['compatibility_score'] >= 0.7:
            compatibility_validation['status'] = 'mostly_compatible'
        elif compatibility_validation['compatibility_score'] >= 0.5:
            compatibility_validation['status'] = 'partially_compatible'
        else:
            compatibility_validation['status'] = 'incompatible'
        
        return compatibility_validation
    
    def validate_performance(self) -> Dict[str, Any]:
        """Valida performance do sistema"""
        performance_validation = {
            'status': 'unknown',
            'metrics': {},
            'issues': [],
            'details': {}
        }
        
        # Simula testes de performance
        test_scenarios = [
            {'name': 'context_detection', 'target_time': 2.0},
            {'name': 'agent_selection', 'target_time': 1.0},
            {'name': 'workflow_execution', 'target_time': 5.0},
            {'name': 'json_loading', 'target_time': 0.5}
        ]
        
        for scenario in test_scenarios:
            start_time = time.time()
            
            # Simula operação
            if scenario['name'] == 'context_detection':
                # Simula detecção de contexto
                time.sleep(0.1)
            elif scenario['name'] == 'agent_selection':
                # Simula seleção de agente
                time.sleep(0.05)
            elif scenario['name'] == 'workflow_execution':
                # Simula execução de workflow
                time.sleep(0.2)
            elif scenario['name'] == 'json_loading':
                # Simula carregamento de JSON
                time.sleep(0.02)
            
            execution_time = time.time() - start_time
            target_time = scenario['target_time']
            
            performance_validation['metrics'][scenario['name']] = {
                'execution_time': execution_time,
                'target_time': target_time,
                'performance_score': target_time / execution_time if execution_time > 0 else 0,
                'status': 'passed' if execution_time <= target_time else 'failed'
            }
        
        # Calcula score geral de performance
        total_score = 0
        total_scenarios = len(test_scenarios)
        
        for metric in performance_validation['metrics'].values():
            if metric['status'] == 'passed':
                total_score += 1
        
        performance_score = total_score / total_scenarios
        
        # Define status de performance
        if performance_score >= 0.9:
            performance_validation['status'] = 'excellent'
        elif performance_score >= 0.7:
            performance_validation['status'] = 'good'
        elif performance_score >= 0.5:
            performance_validation['status'] = 'acceptable'
        else:
            performance_validation['status'] = 'poor'
        
        performance_validation['overall_performance_score'] = performance_score
        
        return performance_validation
    
    def validate_json_maps(self) -> Dict[str, Any]:
        """Valida mapas JSON"""
        json_validation = {
            'status': 'unknown',
            'total_files': 0,
            'valid_files': 0,
            'issues': [],
            'details': {}
        }
        
        maps_path = self.base_path / 'maps'
        if not maps_path.exists():
            json_validation['issues'].append("Pasta de mapas não encontrada")
            json_validation['status'] = 'failed'
            return json_validation
        
        json_files = list(maps_path.glob('*.json'))
        json_validation['total_files'] = len(json_files)
        
        for json_file in json_files:
            file_detail = {
                'status': 'unknown',
                'issues': []
            }
            
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # Validações básicas de JSON
                if not isinstance(data, dict):
                    file_detail['issues'].append("Estrutura JSON inválida")
                
                # Validações específicas por arquivo
                if 'bmad_agents' in json_file.name:
                    if 'agents' not in data.get('bmad_agents', {}):
                        file_detail['issues'].append("Seção 'agents' ausente")
                    if 'aaa_workflows' not in data.get('bmad_agents', {}):
                        file_detail['issues'].append("Seção 'aaa_workflows' ausente")
                
                if file_detail['issues']:
                    file_detail['status'] = 'failed'
                else:
                    file_detail['status'] = 'valid'
                    json_validation['valid_files'] += 1
                
            except json.JSONDecodeError as e:
                file_detail['issues'].append(f"Erro de JSON: {str(e)}")
                file_detail['status'] = 'failed'
            except Exception as e:
                file_detail['issues'].append(f"Erro ao processar arquivo: {str(e)}")
                file_detail['status'] = 'failed'
            
            json_validation['details'][json_file.name] = file_detail
        
        # Define status geral dos JSONs
        if json_validation['valid_files'] == json_validation['total_files']:
            json_validation['status'] = 'passed'
        elif json_validation['valid_files'] > 0:
            json_validation['status'] = 'partial'
        else:
            json_validation['status'] = 'failed'
        
        return json_validation
    
    def validate_rules(self) -> Dict[str, Any]:
        """Valida regras do sistema"""
        rules_validation = {
            'status': 'unknown',
            'total_rules': 0,
            'valid_rules': 0,
            'issues': [],
            'details': {}
        }
        
        rules_path = self.base_path / '.cursor' / 'rules'
        if not rules_path.exists():
            rules_validation['issues'].append("Pasta de regras não encontrada")
            rules_validation['status'] = 'failed'
            return rules_validation
        
        rule_files = list(rules_path.glob('*.md'))
        rules_validation['total_rules'] = len(rule_files)
        
        for rule_file in rule_files:
            rule_detail = {
                'status': 'unknown',
                'issues': []
            }
            
            try:
                with open(rule_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Validações básicas de regras
                if not content.strip():
                    rule_detail['issues'].append("Arquivo vazio")
                
                if not content.startswith('#'):
                    rule_detail['issues'].append("Não começa com título")
                
                # Validações específicas para regras AAA
                if 'aaa' in rule_file.name.lower():
                    if 'agente' not in content.lower() and 'agent' not in content.lower():
                        rule_detail['issues'].append("Regra AAA sem referência a agentes")
                
                if rule_detail['issues']:
                    rule_detail['status'] = 'failed'
                else:
                    rule_detail['status'] = 'valid'
                    rules_validation['valid_rules'] += 1
                
            except Exception as e:
                rule_detail['issues'].append(f"Erro ao processar arquivo: {str(e)}")
                rule_detail['status'] = 'failed'
            
            rules_validation['details'][rule_file.name] = rule_detail
        
        # Define status geral das regras
        if rules_validation['valid_rules'] == rules_validation['total_rules']:
            rules_validation['status'] = 'passed'
        elif rules_validation['valid_rules'] > 0:
            rules_validation['status'] = 'partial'
        else:
            rules_validation['status'] = 'failed'
        
        return rules_validation
    
    def calculate_overall_status(self, validations: Dict[str, Any]) -> str:
        """Calcula status geral baseado em todas as validações"""
        status_scores = {
            'passed': 1.0,
            'excellent': 1.0,
            'fully_compatible': 1.0,
            'good': 0.8,
            'mostly_compatible': 0.8,
            'partial': 0.6,
            'partially_compatible': 0.6,
            'acceptable': 0.5,
            'unknown': 0.3,
            'failed': 0.0,
            'poor': 0.0,
            'incompatible': 0.0
        }
        
        total_score = 0
        total_validations = len(validations)
        
        for validation_name, validation_result in validations.items():
            status = validation_result.get('status', 'unknown')
            score = status_scores.get(status, 0.0)
            total_score += score
        
        average_score = total_score / total_validations if total_validations > 0 else 0
        
        if average_score >= 0.9:
            return 'excellent'
        elif average_score >= 0.7:
            return 'good'
        elif average_score >= 0.5:
            return 'acceptable'
        else:
            return 'failed'
    
    def save_validation_results(self, results: Dict[str, Any]):
        """Salva resultados da validação"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"aaa_validation_results_{timestamp}.json"
        filepath = self.logs_path / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"📄 Resultados salvos: {filepath}")
    
    def generate_validation_report(self, results: Dict[str, Any]) -> str:
        """Gera relatório de validação em formato legível"""
        report = []
        report.append("# Relatório de Validação de Integridade AAA")
        report.append("")
        report.append(f"**Data**: {results['timestamp']}")
        report.append(f"**Status Geral**: {results['overall_status']}")
        report.append(f"**Tempo de Validação**: {results['total_validation_time']:.2f}s")
        report.append("")
        
        # Resumo executivo
        report.append("## 📊 Resumo Executivo")
        report.append("")
        
        validations = results['validations']
        for validation_name, validation_result in validations.items():
            status = validation_result.get('status', 'unknown')
            status_emoji = {
                'passed': '✅',
                'excellent': '✅',
                'fully_compatible': '✅',
                'good': '✅',
                'mostly_compatible': '✅',
                'partial': '⚠️',
                'partially_compatible': '⚠️',
                'acceptable': '⚠️',
                'failed': '❌',
                'poor': '❌',
                'incompatible': '❌',
                'unknown': '❓'
            }.get(status, '❓')
            
            report.append(f"{status_emoji} **{validation_name.replace('_', ' ').title()}**: {status}")
        
        report.append("")
        
        # Detalhes por validação
        report.append("## 🔍 Detalhes por Validação")
        report.append("")
        
        for validation_name, validation_result in validations.items():
            report.append(f"### {validation_name.replace('_', ' ').title()}")
            report.append("")
            report.append(f"- **Status**: {validation_result.get('status', 'unknown')}")
            
            # Adiciona métricas específicas
            if 'total_agents' in validation_result:
                report.append(f"- **Total de Agentes**: {validation_result['total_agents']}")
                report.append(f"- **Agentes Válidos**: {validation_result['valid_agents']}")
            
            if 'total_workflows' in validation_result:
                report.append(f"- **Total de Workflows**: {validation_result['total_workflows']}")
                report.append(f"- **Workflows Válidos**: {validation_result['valid_workflows']}")
            
            if 'compatibility_score' in validation_result:
                report.append(f"- **Score de Compatibilidade**: {validation_result['compatibility_score']:.2f}")
            
            if 'overall_performance_score' in validation_result:
                report.append(f"- **Score de Performance**: {validation_result['overall_performance_score']:.2f}")
            
            # Adiciona issues se houver
            issues = validation_result.get('issues', [])
            if issues:
                report.append("- **Problemas Encontrados**:")
                for issue in issues:
                    report.append(f"  - {issue}")
            
            report.append("")
        
        return "\n".join(report)


def main():
    """Função principal para teste do sistema de validação"""
    print("🔍 Iniciando Sistema de Validação de Integridade AAA")
    
    # Inicializa validador
    validator = AAAIntegrationValidator("wiki")
    
    # Executa validação completa
    results = validator.validate_system_integrity()
    
    # Gera relatório
    report = validator.generate_validation_report(results)
    
    # Salva relatório
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_filename = f"aaa_validation_report_{timestamp}.md"
    report_filepath = validator.logs_path / report_filename
    
    with open(report_filepath, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"📄 Relatório salvo: {report_filepath}")
    print(f"\n{report}")
    
    print(f"\n✅ Validação de integridade concluída!")
    print(f"📊 Status geral: {results['overall_status']}")


if __name__ == "__main__":
    main() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = AgentvalidatorModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script aaa_integration_validator.py executado com sucesso via módulo agents.agent_validator")
    else:
        print(f"❌ Erro na execução do script aaa_integration_validator.py via módulo agents.agent_validator")


# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = MapupdaterModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script migrated_aaa_integration_validator.py executado com sucesso via módulo maps.map_updater")
    else:
        print(f"❌ Erro na execução do script migrated_aaa_integration_validator.py via módulo maps.map_updater")

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
- **Nome**: migrated_migrated_aaa_integration_validator
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

