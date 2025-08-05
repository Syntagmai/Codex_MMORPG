#!/usr/bin/env python3
"""
Testing and Validation Agent - Epic 18 Task 18.9
Realiza testes abrangentes para validar todas as correções realizadas na Epic 18
"""
import os
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

class TestingValidationAgent:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.audit_reports_dir = self.project_root / "wiki" / "docs" / "audit_reports"
        self.correction_reports_dir = self.audit_reports_dir
        self.validation_report = {
            "timestamp": datetime.now().isoformat(),
            "security_tests": [],
            "python_tests": [],
            "performance_tests": [],
            "integration_tests": [],
            "file_structure_tests": [],
            "config_tests": [],
            "documentation_tests": [],
            "readme_tests": [],
            "overall_score": 0,
            "tests_passed": 0,
            "tests_failed": 0,
            "total_tests": 0,
            "validation_status": "pending"
        }
    
    def load_correction_reports(self):
        """Carrega todos os relatórios de correção da Epic 18"""
        reports = {}
        report_files = [
            "security_correction_report.json",
            "python_correction_report.json",
            "performance_correction_report.json",
            "integration_correction_report.json",
            "file_structure_correction_report.json",
            "config_correction_report.json",
            "documentation_correction_report.json",
            "readme_update_report.json"
        ]
        
        for report_file in report_files:
            report_path = self.correction_reports_dir / report_file
            if report_path.exists():
                try:
                    with open(report_path, 'r', encoding='utf-8') as f:
                        reports[report_file.replace('.json', '')] = json.load(f)
                except Exception as e:
                    print(f"❌ Erro ao carregar {report_file}: {e}")
        
        return reports
    
    def test_security_corrections(self, security_report):
        """Testa correções de segurança"""
        tests = []
        
        # Testa se o gerenciador de segurança foi criado
        security_manager = self.project_root / "wiki" / "bmad" / "security" / "security_manager.py"
        if security_manager.exists():
            tests.append({
                "test": "Security Manager Creation",
                "status": "PASSED",
                "description": "Gerenciador de segurança criado com sucesso"
            })
        else:
            tests.append({
                "test": "Security Manager Creation",
                "status": "FAILED",
                "description": "Gerenciador de segurança não encontrado"
            })
        
        # Testa se as diretrizes de segurança foram criadas
        security_guidelines = self.project_root / "wiki" / "docs" / "security_guidelines.md"
        if security_guidelines.exists():
            tests.append({
                "test": "Security Guidelines Creation",
                "status": "PASSED",
                "description": "Diretrizes de segurança criadas com sucesso"
            })
        else:
            tests.append({
                "test": "Security Guidelines Creation",
                "status": "FAILED",
                "description": "Diretrizes de segurança não encontradas"
            })
        
        # Testa score de segurança
        if security_report and "statistics" in security_report:
            score_before = security_report.get("score_before", 0)
            score_after = security_report.get("score_after", 0)
            if score_after > score_before:
                tests.append({
                    "test": "Security Score Improvement",
                    "status": "PASSED",
                    "description": f"Score de segurança melhorou de {score_before} para {score_after}"
                })
            else:
                tests.append({
                    "test": "Security Score Improvement",
                    "status": "FAILED",
                    "description": f"Score de segurança não melhorou: {score_before} → {score_after}"
                })
        
        self.validation_report["security_tests"] = tests
        return tests
    
    def test_python_corrections(self, python_report):
        """Testa correções de Python"""
        tests = []
        
        # Testa se as diretrizes de Python foram criadas
        python_guidelines = self.project_root / "wiki" / "docs" / "python_guidelines.md"
        if python_guidelines.exists():
            tests.append({
                "test": "Python Guidelines Creation",
                "status": "PASSED",
                "description": "Diretrizes de Python criadas com sucesso"
            })
        else:
            tests.append({
                "test": "Python Guidelines Creation",
                "status": "FAILED",
                "description": "Diretrizes de Python não encontradas"
            })
        
        # Testa se há erros de sintaxe nos agentes criados
        agent_files = [
            "security_correction_agent.py",
            "python_correction_agent.py",
            "performance_correction_agent.py",
            "integration_correction_agent.py",
            "file_structure_correction_agent.py",
            "config_correction_agent.py",
            "documentation_correction_agent.py",
            "readme_update_agent.py"
        ]
        
        syntax_errors = 0
        for agent_file in agent_files:
            agent_path = self.project_root / "wiki" / "bmad" / "agents" / agent_file
            if agent_path.exists():
                try:
                    # Testa sintaxe Python
                    result = subprocess.run([sys.executable, "-m", "py_compile", str(agent_path)], 
                                          capture_output=True, text=True)
                    if result.returncode == 0:
                        tests.append({
                            "test": f"Python Syntax - {agent_file}",
                            "status": "PASSED",
                            "description": "Sintaxe Python válida"
                        })
                    else:
                        syntax_errors += 1
                        tests.append({
                            "test": f"Python Syntax - {agent_file}",
                            "status": "FAILED",
                            "description": f"Erro de sintaxe: {result.stderr}"
                        })
                except Exception as e:
                    syntax_errors += 1
                    tests.append({
                        "test": f"Python Syntax - {agent_file}",
                        "status": "FAILED",
                        "description": f"Erro ao testar: {e}"
                    })
        
        if syntax_errors == 0:
            tests.append({
                "test": "All Agents Syntax Valid",
                "status": "PASSED",
                "description": "Todos os agentes têm sintaxe Python válida"
            })
        else:
            tests.append({
                "test": "All Agents Syntax Valid",
                "status": "FAILED",
                "description": f"{syntax_errors} agentes com erros de sintaxe"
            })
        
        self.validation_report["python_tests"] = tests
        return tests
    
    def test_performance_corrections(self, performance_report):
        """Testa correções de performance"""
        tests = []
        
        # Testa se os módulos de otimização foram criados
        optimization_modules = [
            "database_optimizer.py",
            "network_optimizer.py",
            "memory_optimizer.py",
            "cpu_optimizer.py"
        ]
        
        modules_created = 0
        for module in optimization_modules:
            module_path = self.project_root / "wiki" / "bmad" / "optimization" / module
            if module_path.exists():
                modules_created += 1
                tests.append({
                    "test": f"Optimization Module - {module}",
                    "status": "PASSED",
                    "description": "Módulo de otimização criado"
                })
            else:
                tests.append({
                    "test": f"Optimization Module - {module}",
                    "status": "FAILED",
                    "description": "Módulo de otimização não encontrado"
                })
        
        if modules_created == len(optimization_modules):
            tests.append({
                "test": "All Optimization Modules Created",
                "status": "PASSED",
                "description": "Todos os módulos de otimização foram criados"
            })
        else:
            tests.append({
                "test": "All Optimization Modules Created",
                "status": "FAILED",
                "description": f"Apenas {modules_created}/{len(optimization_modules)} módulos criados"
            })
        
        # Testa se as diretrizes de performance foram criadas
        performance_guidelines = self.project_root / "wiki" / "docs" / "performance_guidelines.md"
        if performance_guidelines.exists():
            tests.append({
                "test": "Performance Guidelines Creation",
                "status": "PASSED",
                "description": "Diretrizes de performance criadas"
            })
        else:
            tests.append({
                "test": "Performance Guidelines Creation",
                "status": "FAILED",
                "description": "Diretrizes de performance não encontradas"
            })
        
        self.validation_report["performance_tests"] = tests
        return tests
    
    def test_integration_corrections(self, integration_report):
        """Testa correções de integração"""
        tests = []
        
        # Testa se as diretrizes de integração foram criadas
        integration_guidelines = self.project_root / "wiki" / "docs" / "integration_guidelines.md"
        if integration_guidelines.exists():
            tests.append({
                "test": "Integration Guidelines Creation",
                "status": "PASSED",
                "description": "Diretrizes de integração criadas"
            })
        else:
            tests.append({
                "test": "Integration Guidelines Creation",
                "status": "FAILED",
                "description": "Diretrizes de integração não encontradas"
            })
        
        # Testa se há dependências circulares nos agentes
        agent_files = [
            "security_correction_agent.py",
            "python_correction_agent.py",
            "performance_correction_agent.py",
            "integration_correction_agent.py",
            "file_structure_correction_agent.py",
            "config_correction_agent.py",
            "documentation_correction_agent.py",
            "readme_update_agent.py"
        ]
        
        circular_deps = 0
        for agent_file in agent_files:
            agent_path = self.project_root / "wiki" / "bmad" / "agents" / agent_file
            if agent_path.exists():
                try:
                    with open(agent_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Verifica imports que podem causar dependências circulares
                    if "import " + agent_file.replace('.py', '') in content:
                        circular_deps += 1
                        tests.append({
                            "test": f"Circular Dependency - {agent_file}",
                            "status": "FAILED",
                            "description": "Possível dependência circular detectada"
                        })
                    else:
                        tests.append({
                            "test": f"Circular Dependency - {agent_file}",
                            "status": "PASSED",
                            "description": "Sem dependências circulares"
                        })
                except Exception as e:
                    tests.append({
                        "test": f"Circular Dependency - {agent_file}",
                        "status": "FAILED",
                        "description": f"Erro ao analisar: {e}"
                    })
        
        if circular_deps == 0:
            tests.append({
                "test": "No Circular Dependencies",
                "status": "PASSED",
                "description": "Nenhuma dependência circular detectada"
            })
        else:
            tests.append({
                "test": "No Circular Dependencies",
                "status": "FAILED",
                "description": f"{circular_deps} possíveis dependências circulares"
            })
        
        self.validation_report["integration_tests"] = tests
        return tests
    
    def test_file_structure_corrections(self, file_structure_report):
        """Testa correções de estrutura de arquivos"""
        tests = []
        
        # Testa se as diretrizes de estrutura foram criadas
        structure_guidelines = self.project_root / "wiki" / "docs" / "file_structure_guidelines.md"
        if structure_guidelines.exists():
            tests.append({
                "test": "File Structure Guidelines Creation",
                "status": "PASSED",
                "description": "Diretrizes de estrutura de arquivos criadas"
            })
        else:
            tests.append({
                "test": "File Structure Guidelines Creation",
                "status": "FAILED",
                "description": "Diretrizes de estrutura de arquivos não encontradas"
            })
        
        # Testa se diretórios organizados foram criados
        organized_dirs = [
            "wiki/bmad/security",
            "wiki/bmad/optimization",
            "wiki/bmad/config",
            "wiki/docs/audit_reports"
        ]
        
        dirs_created = 0
        for dir_path in organized_dirs:
            full_path = self.project_root / dir_path
            if full_path.exists():
                dirs_created += 1
                tests.append({
                    "test": f"Organized Directory - {dir_path}",
                    "status": "PASSED",
                    "description": "Diretório organizado criado"
                })
            else:
                tests.append({
                    "test": f"Organized Directory - {dir_path}",
                    "status": "FAILED",
                    "description": "Diretório organizado não encontrado"
                })
        
        if dirs_created == len(organized_dirs):
            tests.append({
                "test": "All Organized Directories Created",
                "status": "PASSED",
                "description": "Todos os diretórios organizados foram criados"
            })
        else:
            tests.append({
                "test": "All Organized Directories Created",
                "status": "FAILED",
                "description": f"Apenas {dirs_created}/{len(organized_dirs)} diretórios criados"
            })
        
        self.validation_report["file_structure_tests"] = tests
        return tests
    
    def test_config_corrections(self, config_report):
        """Testa correções de configuração"""
        tests = []
        
        # Testa se o gerenciador de configuração foi criado
        config_manager = self.project_root / "wiki" / "bmad" / "config" / "config_manager.py"
        if config_manager.exists():
            tests.append({
                "test": "Config Manager Creation",
                "status": "PASSED",
                "description": "Gerenciador de configuração criado"
            })
        else:
            tests.append({
                "test": "Config Manager Creation",
                "status": "FAILED",
                "description": "Gerenciador de configuração não encontrado"
            })
        
        # Testa se as regras de validação foram criadas
        validation_rules = self.project_root / "wiki" / "docs" / "config_validation_rules.md"
        if validation_rules.exists():
            tests.append({
                "test": "Config Validation Rules Creation",
                "status": "PASSED",
                "description": "Regras de validação de configuração criadas"
            })
        else:
            tests.append({
                "test": "Config Validation Rules Creation",
                "status": "FAILED",
                "description": "Regras de validação de configuração não encontradas"
            })
        
        # Testa se as diretrizes de configuração foram criadas
        config_guidelines = self.project_root / "wiki" / "docs" / "config_guidelines.md"
        if config_guidelines.exists():
            tests.append({
                "test": "Config Guidelines Creation",
                "status": "PASSED",
                "description": "Diretrizes de configuração criadas"
            })
        else:
            tests.append({
                "test": "Config Guidelines Creation",
                "status": "FAILED",
                "description": "Diretrizes de configuração não encontradas"
            })
        
        self.validation_report["config_tests"] = tests
        return tests
    
    def test_documentation_corrections(self, documentation_report):
        """Testa correções de documentação"""
        tests = []
        
        # Testa se as diretrizes de documentação foram criadas
        doc_guidelines = self.project_root / "wiki" / "docs" / "documentation_guidelines.md"
        if doc_guidelines.exists():
            tests.append({
                "test": "Documentation Guidelines Creation",
                "status": "PASSED",
                "description": "Diretrizes de documentação criadas"
            })
        else:
            tests.append({
                "test": "Documentation Guidelines Creation",
                "status": "FAILED",
                "description": "Diretrizes de documentação não encontradas"
            })
        
        # Testa se relatórios de correção foram criados
        correction_reports = [
            "security_correction_report.json",
            "python_correction_report.json",
            "performance_correction_report.json",
            "integration_correction_report.json",
            "file_structure_correction_report.json",
            "config_correction_report.json",
            "documentation_correction_report.json",
            "readme_update_report.json"
        ]
        
        reports_created = 0
        for report in correction_reports:
            report_path = self.correction_reports_dir / report
            if report_path.exists():
                reports_created += 1
                tests.append({
                    "test": f"Correction Report - {report}",
                    "status": "PASSED",
                    "description": "Relatório de correção criado"
                })
            else:
                tests.append({
                    "test": f"Correction Report - {report}",
                    "status": "FAILED",
                    "description": "Relatório de correção não encontrado"
                })
        
        if reports_created == len(correction_reports):
            tests.append({
                "test": "All Correction Reports Created",
                "status": "PASSED",
                "description": "Todos os relatórios de correção foram criados"
            })
        else:
            tests.append({
                "test": "All Correction Reports Created",
                "status": "FAILED",
                "description": f"Apenas {reports_created}/{len(correction_reports)} relatórios criados"
            })
        
        self.validation_report["documentation_tests"] = tests
        return tests
    
    def test_readme_corrections(self, readme_report):
        """Testa correções do README"""
        tests = []
        
        # Testa se o README foi atualizado
        readme_path = self.project_root / "README.md"
        if readme_path.exists():
            try:
                with open(readme_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Verifica se tem badges
                if "![License: MIT]" in content:
                    tests.append({
                        "test": "README Badges",
                        "status": "PASSED",
                        "description": "Badges adicionados ao README"
                    })
                else:
                    tests.append({
                        "test": "README Badges",
                        "status": "FAILED",
                        "description": "Badges não encontrados no README"
                    })
                
                # Verifica se tem seções importantes
                important_sections = ["Visão Geral", "Funcionalidades", "Instalação", "Como Usar", "Contribuição", "Licença"]
                sections_found = 0
                for section in important_sections:
                    if section in content:
                        sections_found += 1
                
                if sections_found == len(important_sections):
                    tests.append({
                        "test": "README Important Sections",
                        "status": "PASSED",
                        "description": "Todas as seções importantes presentes"
                    })
                else:
                    tests.append({
                        "test": "README Important Sections",
                        "status": "FAILED",
                        "description": f"Apenas {sections_found}/{len(important_sections)} seções encontradas"
                    })
                
                # Verifica se tem links funcionais
                if "wiki/dashboard/task_master.md" in content:
                    tests.append({
                        "test": "README Functional Links",
                        "status": "PASSED",
                        "description": "Links funcionais adicionados"
                    })
                else:
                    tests.append({
                        "test": "README Functional Links",
                        "status": "FAILED",
                        "description": "Links funcionais não encontrados"
                    })
                
            except Exception as e:
                tests.append({
                    "test": "README Content Analysis",
                    "status": "FAILED",
                    "description": f"Erro ao analisar README: {e}"
                })
        else:
            tests.append({
                "test": "README Existence",
                "status": "FAILED",
                "description": "README.md não encontrado"
            })
        
        # Testa se as diretrizes do README foram criadas
        readme_guidelines = self.project_root / "wiki" / "docs" / "readme_guidelines.md"
        if readme_guidelines.exists():
            tests.append({
                "test": "README Guidelines Creation",
                "status": "PASSED",
                "description": "Diretrizes do README criadas"
            })
        else:
            tests.append({
                "test": "README Guidelines Creation",
                "status": "FAILED",
                "description": "Diretrizes do README não encontradas"
            })
        
        self.validation_report["readme_tests"] = tests
        return tests
    
    def calculate_overall_score(self):
        """Calcula score geral baseado nos testes"""
        all_tests = []
        all_tests.extend(self.validation_report["security_tests"])
        all_tests.extend(self.validation_report["python_tests"])
        all_tests.extend(self.validation_report["performance_tests"])
        all_tests.extend(self.validation_report["integration_tests"])
        all_tests.extend(self.validation_report["file_structure_tests"])
        all_tests.extend(self.validation_report["config_tests"])
        all_tests.extend(self.validation_report["documentation_tests"])
        all_tests.extend(self.validation_report["readme_tests"])
        
        total_tests = len(all_tests)
        passed_tests = len([test for test in all_tests if test["status"] == "PASSED"])
        failed_tests = len([test for test in all_tests if test["status"] == "FAILED"])
        
        if total_tests > 0:
            overall_score = (passed_tests / total_tests) * 100
        else:
            overall_score = 0
        
        self.validation_report["overall_score"] = overall_score
        self.validation_report["tests_passed"] = passed_tests
        self.validation_report["tests_failed"] = failed_tests
        self.validation_report["total_tests"] = total_tests
        
        if overall_score >= 80:
            self.validation_report["validation_status"] = "PASSED"
        elif overall_score >= 60:
            self.validation_report["validation_status"] = "PARTIAL"
        else:
            self.validation_report["validation_status"] = "FAILED"
        
        return overall_score
    
    def create_validation_report(self):
        """Cria relatório de validação"""
        report_file = self.audit_reports_dir / "epic_18_validation_report.json"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(self.validation_report, f, indent=2, ensure_ascii=False)
        
        return str(report_file)
    
    def run_comprehensive_validation(self):
        """Executa validação completa"""
        print("🧪 Iniciando testes e validação completa...")
        
        # Carrega relatórios de correção
        print("📊 Carregando relatórios de correção...")
        correction_reports = self.load_correction_reports()
        
        print(f"✅ {len(correction_reports)} relatórios de correção carregados")
        
        # Executa testes para cada área
        print("\n🔒 Testando correções de segurança...")
        self.test_security_corrections(correction_reports.get("security_correction_report", {}))
        
        print("🐍 Testando correções de Python...")
        self.test_python_corrections(correction_reports.get("python_correction_report", {}))
        
        print("⚡ Testando correções de performance...")
        self.test_performance_corrections(correction_reports.get("performance_correction_report", {}))
        
        print("🔗 Testando correções de integração...")
        self.test_integration_corrections(correction_reports.get("integration_correction_report", {}))
        
        print("🗂️ Testando correções de estrutura de arquivos...")
        self.test_file_structure_corrections(correction_reports.get("file_structure_correction_report", {}))
        
        print("⚙️ Testando correções de configuração...")
        self.test_config_corrections(correction_reports.get("config_correction_report", {}))
        
        print("📚 Testando correções de documentação...")
        self.test_documentation_corrections(correction_reports.get("documentation_correction_report", {}))
        
        print("📖 Testando correções do README...")
        self.test_readme_corrections(correction_reports.get("readme_update_report", {}))
        
        # Calcula score geral
        print("\n📊 Calculando score geral...")
        overall_score = self.calculate_overall_score()
        
        # Cria relatório
        report_file = self.create_validation_report()
        
        # Estatísticas finais
        print(f"\n✅ Validação completa concluída!")
        print(f"📊 Score Geral: {overall_score:.1f}/100")
        print(f"✅ Testes Passados: {self.validation_report['tests_passed']}")
        print(f"❌ Testes Falharam: {self.validation_report['tests_failed']}")
        print(f"📋 Total de Testes: {self.validation_report['total_tests']}")
        print(f"🎯 Status: {self.validation_report['validation_status']}")
        print(f"📄 Relatório salvo em: {report_file}")
        
        if self.validation_report["validation_status"] == "PASSED":
            print(f"\n🎉 Epic 18 está pronta para finalização!")
        elif self.validation_report["validation_status"] == "PARTIAL":
            print(f"\n⚠️ Epic 18 tem algumas questões que precisam de atenção.")
        else:
            print(f"\n❌ Epic 18 precisa de mais correções antes da finalização.")
        
        return self.validation_report["validation_status"] == "PASSED"

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        project_root = sys.argv[1]
    else:
        project_root = "."
    
    agent = TestingValidationAgent(project_root)
    result = agent.run_comprehensive_validation() 