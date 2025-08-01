#!/usr/bin/env python3
"""
Quality Assurance Agent - Sistema de Validação e Teste
Responsável por validar e testar o sistema de workflow de aprendizado.
"""

import os
import sys
import json
import argparse
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

# Importar utilitário de caminhos absolutos
try:
    from absolute_path_utility import get_path, create_file_safely, log_message
except ImportError:
    def get_path(path_name: str):
        return None
    def create_file_safely(path_name: str, filename: str, content: str):
        return False
    def log_message(message: str, level: str = "INFO"):
        print(f"{level}: {message}")


class QualityAssuranceAgent:
    """
    Agente responsável por validar e testar o sistema de workflow de aprendizado.
    """
    
    def __init__(self):
        # Configurar logging
        log_path = get_path('log')
        if log_path:
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s',
                handlers=[
                    logging.FileHandler(log_path / "quality_assurance_agent.log"),
                    logging.StreamHandler()
                ]
            )
        self.logger = logging.getLogger(__name__)
        
        self.base_path = get_path('wiki')
        if not self.base_path:
            self.base_path = Path('wiki')
        self.workflows_path = self.base_path / "workflows"
        self.courses_path = self.base_path / "docs" / "courses"
        self.certificates_path = self.base_path / "certificates"
        
        self.logger.info("Quality Assurance Agent inicializado")
        
    def validate_workflow(self) -> bool:
        """
        Valida o sistema de workflow de aprendizado completo.
        
        Returns:
            bool: True se validação bem-sucedida
        """
        try:
            self.logger.info("🔍 Iniciando validação do sistema de workflow...")
            
            validation_results = {
                'workflow_config': False,
                'automation_system': False,
                'certification_system': False,
                'courses_structure': False,
                'certificates_directory': False,
                'integration_tests': False
            }
            
            # 1. Validar configuração do workflow
            self.logger.info("📋 Validando configuração do workflow...")
            workflow_config_path = self.workflows_path / 'learning_workflow_config.json'
            if workflow_config_path.exists():
                try:
                    with open(workflow_config_path, 'r', encoding='utf-8') as f:
                        workflow_config = json.load(f)
                    
                    # Validar estrutura do workflow
                    required_keys = ['workflow_id', 'name', 'version', 'status', 'features', 'execution_rules', 'courses']
                    if all(key in workflow_config for key in required_keys):
                        validation_results['workflow_config'] = True
                        self.logger.info("✅ Configuração do workflow válida")
                    else:
                        self.logger.error("❌ Configuração do workflow inválida")
                except Exception as e:
                    self.logger.error(f"❌ Erro ao validar workflow: {e}")
            else:
                self.logger.error("❌ Arquivo de configuração do workflow não encontrado")
            
            # 2. Validar sistema de automação
            self.logger.info("🤖 Validando sistema de automação...")
            automation_path = self.workflows_path / 'automation_system.json'
            if automation_path.exists():
                try:
                    with open(automation_path, 'r', encoding='utf-8') as f:
                        automation_config = json.load(f)
                    
                    # Validar estrutura da automação
                    required_keys = ['scheduler', 'progress_tracker', 'certification_system']
                    if all(key in automation_config for key in required_keys):
                        validation_results['automation_system'] = True
                        self.logger.info("✅ Sistema de automação válido")
                    else:
                        self.logger.error("❌ Sistema de automação inválido")
                except Exception as e:
                    self.logger.error(f"❌ Erro ao validar automação: {e}")
            else:
                self.logger.error("❌ Arquivo de automação não encontrado")
            
            # 3. Validar sistema de certificação
            self.logger.info("🏆 Validando sistema de certificação...")
            certification_path = self.workflows_path / 'certification_system.json'
            if certification_path.exists():
                try:
                    with open(certification_path, 'r', encoding='utf-8') as f:
                        certification_config = json.load(f)
                    
                    # Validar estrutura da certificação
                    required_keys = ['certification_id', 'name', 'version', 'status', 'certification_types', 'badge_system']
                    if all(key in certification_config for key in required_keys):
                        validation_results['certification_system'] = True
                        self.logger.info("✅ Sistema de certificação válido")
                    else:
                        self.logger.error("❌ Sistema de certificação inválido")
                except Exception as e:
                    self.logger.error(f"❌ Erro ao validar certificação: {e}")
            else:
                self.logger.error("❌ Arquivo de certificação não encontrado")
            
            # 4. Validar estrutura de cursos
            self.logger.info("📚 Validando estrutura de cursos...")
            if self.courses_path.exists():
                # Verificar se há cursos disponíveis
                course_dirs = [d for d in self.courses_path.iterdir() if d.is_dir()]
                if len(course_dirs) > 0:
                    validation_results['courses_structure'] = True
                    self.logger.info(f"✅ Estrutura de cursos válida ({len(course_dirs)} cursos encontrados)")
                else:
                    self.logger.error("❌ Nenhum curso encontrado")
            else:
                self.logger.error("❌ Diretório de cursos não encontrado")
            
            # 5. Validar diretório de certificados
            self.logger.info("📁 Validando diretório de certificados...")
            if self.certificates_path.exists():
                validation_results['certificates_directory'] = True
                self.logger.info("✅ Diretório de certificados válido")
            else:
                self.logger.error("❌ Diretório de certificados não encontrado")
            
            # 6. Testes de integração
            self.logger.info("🔗 Executando testes de integração...")
            integration_success = self.run_integration_tests()
            validation_results['integration_tests'] = integration_success
            
            # 7. Gerar relatório de validação
            validation_report = self.generate_validation_report(validation_results)
            
            # 8. Salvar relatório
            report_path = self.save_validation_report(validation_report)
            
            # 9. Calcular score de validação
            total_tests = len(validation_results)
            passed_tests = sum(validation_results.values())
            validation_score = (passed_tests / total_tests) * 100
            
            self.logger.info(f"📊 Score de validação: {validation_score:.1f}% ({passed_tests}/{total_tests})")
            self.logger.info(f"📋 Relatório salvo em: {report_path}")
            
            if validation_score >= 80:
                self.logger.info("✅ Sistema de workflow validado com sucesso!")
                return True
            else:
                self.logger.warning("⚠️ Sistema de workflow com problemas identificados")
                return False
                
        except Exception as e:
            self.logger.error(f"❌ Erro na validação do workflow: {e}")
            return False
    
    def run_integration_tests(self) -> bool:
        """
        Executa testes de integração do sistema.
        
        Returns:
            bool: True se testes passaram
        """
        try:
            self.logger.info("🧪 Executando testes de integração...")
            
            test_results = {
                'workflow_automation_integration': False,
                'certification_workflow_integration': False,
                'courses_certification_integration': False,
                'file_permissions': False,
                'json_validation': False
            }
            
            # Teste 1: Integração workflow-automação
            try:
                workflow_config_path = self.workflows_path / 'learning_workflow_config.json'
                automation_path = self.workflows_path / 'automation_system.json'
                
                if workflow_config_path.exists() and automation_path.exists():
                    with open(workflow_config_path, 'r') as f:
                        workflow = json.load(f)
                    with open(automation_path, 'r') as f:
                        automation = json.load(f)
                    
                    # Verificar se as configurações são compatíveis
                    if workflow.get('status') == 'active' and automation.get('scheduler'):
                        test_results['workflow_automation_integration'] = True
                        self.logger.info("✅ Integração workflow-automação: OK")
                    else:
                        self.logger.error("❌ Integração workflow-automação: FALHA")
                else:
                    self.logger.error("❌ Arquivos necessários não encontrados")
            except Exception as e:
                self.logger.error(f"❌ Erro no teste workflow-automação: {e}")
            
            # Teste 2: Integração certificação-workflow
            try:
                certification_path = self.workflows_path / 'certification_system.json'
                if certification_path.exists():
                    with open(certification_path, 'r') as f:
                        certification = json.load(f)
                    
                    if certification.get('status') == 'active':
                        test_results['certification_workflow_integration'] = True
                        self.logger.info("✅ Integração certificação-workflow: OK")
                    else:
                        self.logger.error("❌ Integração certificação-workflow: FALHA")
                else:
                    self.logger.error("❌ Arquivo de certificação não encontrado")
            except Exception as e:
                self.logger.error(f"❌ Erro no teste certificação-workflow: {e}")
            
            # Teste 3: Integração cursos-certificação
            try:
                if self.courses_path.exists() and self.certificates_path.exists():
                    test_results['courses_certification_integration'] = True
                    self.logger.info("✅ Integração cursos-certificação: OK")
                else:
                    self.logger.error("❌ Integração cursos-certificação: FALHA")
            except Exception as e:
                self.logger.error(f"❌ Erro no teste cursos-certificação: {e}")
            
            # Teste 4: Permissões de arquivo
            try:
                test_file = self.workflows_path / 'test_permissions.json'
                test_content = '{"test": "permissions"}'
                
                with open(test_file, 'w') as f:
                    f.write(test_content)
                
                with open(test_file, 'r') as f:
                    content = f.read()
                
                if content == test_content:
                    test_results['file_permissions'] = True
                    self.logger.info("✅ Permissões de arquivo: OK")
                else:
                    self.logger.error("❌ Permissões de arquivo: FALHA")
                
                # Limpar arquivo de teste
                test_file.unlink()
            except Exception as e:
                self.logger.error(f"❌ Erro no teste de permissões: {e}")
            
            # Teste 5: Validação JSON
            try:
                workflow_config_path = self.workflows_path / 'learning_workflow_config.json'
                if workflow_config_path.exists():
                    with open(workflow_config_path, 'r') as f:
                        json.load(f)  # Testa se é JSON válido
                    test_results['json_validation'] = True
                    self.logger.info("✅ Validação JSON: OK")
                else:
                    self.logger.error("❌ Validação JSON: FALHA")
            except Exception as e:
                self.logger.error(f"❌ Erro na validação JSON: {e}")
            
            # Calcular resultado geral
            total_tests = len(test_results)
            passed_tests = sum(test_results.values())
            integration_score = (passed_tests / total_tests) * 100
            
            self.logger.info(f"📊 Score de integração: {integration_score:.1f}% ({passed_tests}/{total_tests})")
            
            return integration_score >= 80
            
        except Exception as e:
            self.logger.error(f"❌ Erro nos testes de integração: {e}")
            return False
    
    def generate_validation_report(self, results: Dict[str, bool]) -> str:
        """
        Gera relatório de validação.
        
        Args:
            results: Resultados da validação
            
        Returns:
            str: Relatório formatado
        """
        total_tests = len(results)
        passed_tests = sum(results.values())
        validation_score = (passed_tests / total_tests) * 100
        
        report = f"""# 🔍 Relatório de Validação - Sistema de Workflow

## 📋 **Informações Gerais**
- **Data de Validação**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Agente Responsável**: Quality Assurance Agent
- **Total de Testes**: {total_tests}
- **Testes Aprovados**: {passed_tests}
- **Score de Validação**: {validation_score:.1f}%

## 🎯 **Resultados dos Testes**

"""
        
        for test_name, result in results.items():
            status = "✅ APROVADO" if result else "❌ REPROVADO"
            report += f"""### **{test_name.replace('_', ' ').title()}**
- **Status**: {status}
- **Descrição**: {'Teste passou com sucesso' if result else 'Teste falhou'}

"""
        
        report += f"""## 📊 **Análise de Qualidade**

### **✅ Pontos Fortes:**
"""
        
        for test_name, result in results.items():
            if result:
                report += f"- {test_name.replace('_', ' ').title()}\n"
        
        report += f"""
### **⚠️ Pontos de Atenção:**
"""
        
        for test_name, result in results.items():
            if not result:
                report += f"- {test_name.replace('_', ' ').title()}\n"
        
        report += f"""
## 🎯 **Recomendações**

"""
        
        if validation_score >= 90:
            report += """### **🟢 Sistema Excelente:**
- Sistema está funcionando perfeitamente
- Manter monitoramento regular
- Considerar expansão de funcionalidades
"""
        elif validation_score >= 80:
            report += """### **🟡 Sistema Bom:**
- Sistema está funcionando adequadamente
- Corrigir pontos de atenção identificados
- Melhorar testes de integração
"""
        else:
            report += """### **🔴 Sistema Precisa de Correções:**
- Corrigir problemas críticos identificados
- Revisar configurações do sistema
- Executar validação novamente após correções
"""
        
        report += f"""
## 📈 **Métricas de Qualidade**

### **📊 Score Geral**: {validation_score:.1f}%
### **🎯 Status**: {'✅ APROVADO' if validation_score >= 80 else '❌ REPROVADO'}
### **🔧 Ações Necessárias**: {'Nenhuma' if validation_score >= 80 else 'Correções urgentes'}

---

**Validado por**: Quality Assurance Agent  
**Data**: {datetime.now().isoformat()}  
**Status**: {'🟢 Sistema Validado' if validation_score >= 80 else '🔴 Sistema com Problemas'}
"""
        
        return report
    
    def save_validation_report(self, report: str) -> Path:
        """
        Salva relatório de validação.
        
        Args:
            report: Conteúdo do relatório
            
        Returns:
            Path: Caminho do arquivo salvo
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = f"workflow_validation_report_{timestamp}.md"
        report_path = self.base_path / "log" / report_filename
        
        report_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        return report_path


def main():
    """Função principal do agente."""
    parser = argparse.ArgumentParser(description='Quality Assurance Agent')
    parser.add_argument('--validate-workflow', action='store_true',
                       help='Valida o sistema de workflow de aprendizado')
    
    args = parser.parse_args()
    
    agent = QualityAssuranceAgent()
    
    if args.validate_workflow:
        success = agent.validate_workflow()
        if success:
            print("✅ Sistema de workflow validado com sucesso!")
            sys.exit(0)
        else:
            print("❌ Falha na validação do sistema de workflow")
            sys.exit(1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main() 