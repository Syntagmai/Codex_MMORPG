#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unicode_aliases
"""
Learning Workflow Orchestrator - Sistema de Aprendizado Contínuo
===============================================================

Workflow único que usa agentes existentes + IA do chat para:
1. Criar módulos baseados em código existente (OTClient/Canary)
2. Analisar e comentar o código criado
3. Estudar se realmente funciona baseado no código existente
4. Coletar feedback e influenciar próximas criações
5. Evoluir para agentes criadores de código sem erros

Autor: Sistema BMAD
Versão: 1.0.0
Data: 2025-01-27
"""

import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import subprocess

class LearningWorkflowOrchestrator:
    """
    Orquestrador do workflow de aprendizado contínuo.
    """
    
    def __init__(self):
        """
        Inicializa o Learning Workflow Orchestrator.
        """
        self.base_path = Path(__file__).parent.parent.parent.parent
        self.log_path = self.base_path / "wiki" / "log" / "learning_workflow"
        self.log_path.mkdir(parents=True, exist_ok=True)
        
        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_path / "learning_workflow.log"),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
        # Agentes disponíveis
        self.available_agents = {
            'code_generator': 'wiki/bmad/agents/code_generator_agent.py',
            'deep_analyzer': 'wiki/bmad/agents/deep_source_analyzer.py',
            'professor': 'wiki/bmad/agents/professor_agent.py',
            'quality_assurance': 'wiki/bmad/agents/quality_assurance_agent.py',
            'documentation': 'wiki/bmad/agents/documentation_agent.py'
        }
        
        # Memória de aprendizado
        self.learning_memory = {
            'successful_patterns': [],
            'common_errors': [],
            'improvement_strategies': [],
            'feedback_history': []
        }
        
        self.logger.info("Learning Workflow Orchestrator inicializado")
    
    def log_message(self, message: str, level: str = "INFO"):
        """Log de mensagens com timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        print(log_entry)
        self.logger.info(message)
    
    def execute_agent(self, agent_name: str, parameters: Dict = None) -> bool:
        """
        Executa um agente específico.
        
        Args:
            agent_name: Nome do agente a executar
            parameters: Parâmetros para o agente
            
        Returns:
            bool: True se execução bem-sucedida
        """
        try:
            if agent_name not in self.available_agents:
                self.log_message(f"❌ Agente {agent_name} não encontrado", "ERROR")
                return False
            
            agent_path = self.base_path / self.available_agents[agent_name]
            if not agent_path.exists():
                self.log_message(f"❌ Arquivo do agente {agent_name} não encontrado", "ERROR")
                return False
            
            # Executar agente
            cmd = [sys.executable, str(agent_path)]
            if parameters:
                cmd.extend(["--params", json.dumps(parameters)])
            
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.base_path)
            
            if result.returncode == 0:
                self.log_message(f"✅ Agente {agent_name} executado com sucesso")
                return True
            else:
                self.log_message(f"❌ Erro na execução do agente {agent_name}: {result.stderr}", "ERROR")
                return False
                
        except Exception as e:
            self.log_message(f"❌ Erro ao executar agente {agent_name}: {str(e)}", "ERROR")
            return False
    
    def create_module_with_learning(self, module_name: str, language: str, purpose: str, 
                                  reference_source: str = "otclient") -> Dict:
        """
        Cria módulo com aprendizado contínuo.
        
        Args:
            module_name: Nome do módulo a criar
            language: Linguagem de programação
            purpose: Propósito do módulo
            reference_source: Fonte de referência (otclient/canary)
            
        Returns:
            Dict: Resultados do processo de aprendizado
        """
        self.log_message(f"🚀 Iniciando criação de módulo: {module_name}")
        
        results = {
            'module_name': module_name,
            'language': language,
            'purpose': purpose,
            'reference_source': reference_source,
            'creation_timestamp': datetime.now().isoformat(),
            'steps': [],
            'feedback': {},
            'learning_outcomes': []
        }
        
        # Etapa 1: Análise do código de referência
        self.log_message("🔍 Etapa 1: Analisando código de referência...")
        results['steps'].append({
            'step': 1,
            'action': 'analyze_reference',
            'status': 'running'
        })
        
        if self.execute_agent('deep_analyzer', {
            'target': reference_source,
            'module_type': module_name,
            'analysis_depth': 'comprehensive'
        }):
            results['steps'][-1]['status'] = 'completed'
            self.log_message("✅ Análise de referência concluída")
        else:
            results['steps'][-1]['status'] = 'failed'
            self.log_message("❌ Falha na análise de referência", "ERROR")
            return results
        
        # Etapa 2: Geração do módulo baseado no aprendizado
        self.log_message("🏗️ Etapa 2: Gerando módulo com aprendizado...")
        results['steps'].append({
            'step': 2,
            'action': 'generate_module',
            'status': 'running'
        })
        
        if self.execute_agent('code_generator', {
            'module_name': module_name,
            'language': language,
            'purpose': purpose,
            'learning_memory': self.learning_memory,
            'reference_analysis': True
        }):
            results['steps'][-1]['status'] = 'completed'
            self.log_message("✅ Geração do módulo concluída")
        else:
            results['steps'][-1]['status'] = 'failed'
            self.log_message("❌ Falha na geração do módulo", "ERROR")
            return results
        
        # Etapa 3: Análise educacional e comentários
        self.log_message("🧠 Etapa 3: Análise educacional e comentários...")
        results['steps'].append({
            'step': 3,
            'action': 'educational_analysis',
            'status': 'running'
        })
        
        if self.execute_agent('professor', {
            'action': 'analyze_created_module',
            'module_name': module_name,
            'add_comments': True,
            'explain_patterns': True
        }):
            results['steps'][-1]['status'] = 'completed'
            self.log_message("✅ Análise educacional concluída")
        else:
            results['steps'][-1]['status'] = 'failed'
            self.log_message("❌ Falha na análise educacional", "ERROR")
        
        # Etapa 4: Avaliação de qualidade
        self.log_message("📊 Etapa 4: Avaliando qualidade...")
        results['steps'].append({
            'step': 4,
            'action': 'quality_evaluation',
            'status': 'running'
        })
        
        if self.execute_agent('quality_assurance', {
            'action': 'evaluate_created_module',
            'module_name': module_name,
            'compare_with_reference': True
        }):
            results['steps'][-1]['status'] = 'completed'
            self.log_message("✅ Avaliação de qualidade concluída")
        else:
            results['steps'][-1]['status'] = 'failed'
            self.log_message("❌ Falha na avaliação de qualidade", "ERROR")
        
        # Etapa 5: Geração de documentação e feedback
        self.log_message("📝 Etapa 5: Gerando documentação e feedback...")
        results['steps'].append({
            'step': 5,
            'action': 'documentation_and_feedback',
            'status': 'running'
        })
        
        if self.execute_agent('documentation', {
            'action': 'create_learning_report',
            'module_name': module_name,
            'include_feedback': True,
            'learning_outcomes': True
        }):
            results['steps'][-1]['status'] = 'completed'
            self.log_message("✅ Documentação e feedback concluídos")
        else:
            results['steps'][-1]['status'] = 'failed'
            self.log_message("❌ Falha na documentação", "ERROR")
        
        # Etapa 6: Atualização da memória de aprendizado
        self.log_message("🔄 Etapa 6: Atualizando memória de aprendizado...")
        self.update_learning_memory(results)
        
        results['learning_outcomes'] = self.extract_learning_outcomes(results)
        
        self.log_message(f"🎉 Processo de aprendizado concluído para {module_name}")
        return results
    
    def update_learning_memory(self, results: Dict):
        """
        Atualiza a memória de aprendizado com os resultados.
        
        Args:
            results: Resultados do processo de aprendizado
        """
        try:
            # Extrair padrões de sucesso
            if results.get('feedback', {}).get('quality_score', 0) > 7.0:
                pattern = {
                    'module_type': results['module_name'],
                    'language': results['language'],
                    'successful_approach': results.get('feedback', {}).get('strengths', []),
                    'timestamp': results['creation_timestamp']
                }
                self.learning_memory['successful_patterns'].append(pattern)
            
            # Extrair erros comuns
            if results.get('feedback', {}).get('errors'):
                for error in results['feedback']['errors']:
                    error_pattern = {
                        'error_type': error.get('type'),
                        'module_type': results['module_name'],
                        'language': results['language'],
                        'avoidance_strategy': error.get('suggestion'),
                        'timestamp': results['creation_timestamp']
                    }
                    self.learning_memory['common_errors'].append(error_pattern)
            
            # Salvar memória atualizada
            memory_file = self.log_path / "learning_memory.json"
            with open(memory_file, 'w', encoding='utf-8') as f:
                json.dump(self.learning_memory, f, indent=2, ensure_ascii=False)
            
            self.log_message("✅ Memória de aprendizado atualizada")
            
        except Exception as e:
            self.log_message(f"❌ Erro ao atualizar memória de aprendizado: {str(e)}", "ERROR")
    
    def extract_learning_outcomes(self, results: Dict) -> List[Dict]:
        """
        Extrai lições aprendidas dos resultados.
        
        Args:
            results: Resultados do processo de aprendizado
            
        Returns:
            List[Dict]: Lições aprendidas
        """
        outcomes = []
        
        # Lições baseadas na qualidade
        quality_score = results.get('feedback', {}).get('quality_score', 0)
        if quality_score > 8.0:
            outcomes.append({
                'type': 'success_pattern',
                'message': f"Padrão de alta qualidade identificado para {results['module_name']}",
                'score': quality_score
            })
        elif quality_score < 5.0:
            outcomes.append({
                'type': 'improvement_needed',
                'message': f"Necessidade de melhoria identificada para {results['module_name']}",
                'score': quality_score
            })
        
        # Lições baseadas em erros
        errors = results.get('feedback', {}).get('errors', [])
        for error in errors:
            outcomes.append({
                'type': 'error_lesson',
                'message': f"Erro aprendido: {error.get('description', 'Erro não especificado')}",
                'suggestion': error.get('suggestion', 'Sem sugestão')
            })
        
        # Lições baseadas em comparação
        comparison = results.get('feedback', {}).get('comparison', {})
        if comparison.get('similarity_score', 0) > 0.8:
            outcomes.append({
                'type': 'pattern_recognition',
                'message': f"Padrão similar identificado com {comparison.get('similarity_score', 0):.2f} de similaridade",
                'reference': results['reference_source']
            })
        
        return outcomes
    
    def get_learning_statistics(self) -> Dict:
        """
        Obtém estatísticas de aprendizado.
        
        Returns:
            Dict: Estatísticas de aprendizado
        """
        return {
            'total_modules_created': len(self.learning_memory['successful_patterns']) + len(self.learning_memory['common_errors']),
            'successful_patterns': len(self.learning_memory['successful_patterns']),
            'common_errors': len(self.learning_memory['common_errors']),
            'improvement_strategies': len(self.learning_memory['improvement_strategies']),
            'feedback_entries': len(self.learning_memory['feedback_history']),
            'learning_memory_size': len(self.learning_memory['successful_patterns']) + len(self.learning_memory['common_errors'])
        }
    
    def generate_learning_report(self) -> str:
        """
        Gera relatório completo de aprendizado.
        
        Returns:
            str: Relatório de aprendizado
        """
        stats = self.get_learning_statistics()
        
        report = f"""
# Relatório de Aprendizado - Learning Workflow Orchestrator

## 📊 Estatísticas Gerais
- **Total de módulos criados**: {stats['total_modules_created']}
- **Padrões de sucesso**: {stats['successful_patterns']}
- **Erros comuns**: {stats['common_errors']}
- **Estratégias de melhoria**: {stats['improvement_strategies']}
- **Entradas de feedback**: {stats['feedback_entries']}

## 🎯 Padrões de Sucesso Identificados
"""
        
        for pattern in self.learning_memory['successful_patterns'][-5:]:  # Últimos 5
            report += f"""
### {pattern['module_type']} ({pattern['language']})
- **Abordagem**: {', '.join(pattern['successful_approach'])}
- **Data**: {pattern['timestamp']}
"""
        
        report += """
## ❌ Erros Comuns e Estratégias de Evitação
"""
        
        for error in self.learning_memory['common_errors'][-5:]:  # Últimos 5
            report += f"""
### {error['error_type']} em {error['module_type']}
- **Estratégia de evitação**: {error['avoidance_strategy']}
- **Data**: {error['timestamp']}
"""
        
        report += """
## 🔄 Próximos Passos
1. Continuar refinando padrões de sucesso
2. Implementar estratégias de evitação de erros
3. Expandir análise para mais tipos de módulos
4. Integrar feedback de qualidade mais detalhado

---
*Relatório gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
        
        return report
    
    def run_learning_workflow(self, module_name: str, language: str, purpose: str, 
                            reference_source: str = "otclient") -> bool:
        """
        Executa o workflow completo de aprendizado.
        
        Args:
            module_name: Nome do módulo
            language: Linguagem de programação
            purpose: Propósito do módulo
            reference_source: Fonte de referência
            
        Returns:
            bool: True se workflow executado com sucesso
        """
        try:
            self.log_message("🚀 Iniciando workflow de aprendizado contínuo...")
            
            # Executar workflow de criação com aprendizado
            results = self.create_module_with_learning(
                module_name, language, purpose, reference_source
            )
            
            # Verificar se workflow foi bem-sucedido
            failed_steps = [step for step in results['steps'] if step['status'] == 'failed']
            
            if failed_steps:
                self.log_message(f"⚠️ Workflow concluído com {len(failed_steps)} falhas", "WARNING")
                return False
            else:
                self.log_message("✅ Workflow de aprendizado executado com sucesso")
                
                # Gerar relatório
                report = self.generate_learning_report()
                report_file = self.log_path / f"learning_report_{module_name}.md"
                with open(report_file, 'w', encoding='utf-8') as f:
                    f.write(report)
                
                self.log_message(f"📝 Relatório salvo em: {report_file}")
                return True
                
        except Exception as e:
            self.log_message(f"❌ Erro no workflow de aprendizado: {str(e)}", "ERROR")
            return False

def main():
    """Função principal para execução do workflow."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Learning Workflow Orchestrator')
    parser.add_argument('--module', required=True, help='Nome do módulo a criar')
    parser.add_argument('--language', required=True, help='Linguagem de programação')
    parser.add_argument('--purpose', required=True, help='Propósito do módulo')
    parser.add_argument('--reference', default='otclient', help='Fonte de referência (otclient/canary)')
    parser.add_argument('--report', action='store_true', help='Gerar relatório de aprendizado')
    
    args = parser.parse_args()
    
    orchestrator = LearningWorkflowOrchestrator()
    
    if args.report:
        # Apenas gerar relatório
        report = orchestrator.generate_learning_report()
        print(report)
    else:
        # Executar workflow completo
        success = orchestrator.run_learning_workflow(
            args.module, args.language, args.purpose, args.reference
        )
        
        if success:
            print("✅ Workflow de aprendizado executado com sucesso!")
        else:
            print("❌ Workflow de aprendizado falhou!")
            sys.exit(1)

if __name__ == "__main__":
    main() 